#!/usr/bin/env python3
"""
kansas_geo_timeline.cli
=======================

Command-line utilities for the Kansas Geo Timeline / Kansas-Frontier-Matrix stack.

Subcommands
-----------
- validate-stac : Validate STAC Item JSON files against the local schema.
- render-config : Render web/app.config.json from STAC Items + optional extra layers/basemaps.
- list-stac     : Print/export a compact table of STAC Items (id, datetime/range, bbox).

Design
------
- dependency-light by default (stdlib). Optional extras:
  * jsonschema  — if installed, enables strict STAC validation.
  * jinja2      — if installed, enables template rendering for app.config.json.

Examples
--------
# Validate all STAC items
kgt validate-stac stac/items

# Render app config to web/app.config.json using default template
kgt render-config --stac stac/items --output web/app.config.json --pretty

# Provide custom context JSON for basemaps/layers
kgt render-config --stac stac/items --context configs/render_context.json --output web/app.config.json

# List items as JSON Lines to stdout
kgt list-stac stac/items --format jsonl --output -
"""

from __future__ import annotations

import argparse
import csv
import glob
import io
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from . import (
    __version__,
    load_json_schema,
    schema_path,
    template_path,
)

# Optional deps (soft)
try:
    import jsonschema  # type: ignore
    HAS_JSONSCHEMA = True
except Exception:  # pragma: no cover
    HAS_JSONSCHEMA = False

try:
    import jinja2  # type: ignore
    HAS_JINJA2 = True
except Exception:  # pragma: no cover
    HAS_JINJA2 = False


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _read_json(p: Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def _iter_paths(patterns: Iterable[str]) -> Iterable[Path]:
    """
    Yield JSON file paths from a mix of files/dirs/globs in stable sorted order.
    - Directories are searched recursively for *.json
    - Globs are honored
    - Duplicates are removed
    """
    seen: set[Path] = set()
    for pat in patterns:
        p = Path(pat)
        if p.is_dir():
            for m in sorted(p.glob("**/*.json")):
                if m not in seen:
                    seen.add(m)
                    yield m
        else:
            for m in sorted(glob.glob(pat, recursive=True)):
                mp = Path(m)
                if mp.is_file() and mp.suffix.lower() == ".json" and mp not in seen:
                    seen.add(mp)
                    yield mp


def _is_item(obj: Dict[str, Any]) -> bool:
    """Heuristic: STAC Item = GeoJSON Feature with required keys present."""
    try:
        return (obj.get("type") == "Feature" and
                isinstance(obj.get("id"), str) and
                isinstance(obj.get("properties"), dict) and
                isinstance(obj.get("assets"), dict))
    except Exception:
        return False


def _extract_year(props: Dict[str, Any]) -> Optional[int]:
    dt = props.get("datetime")
    if isinstance(dt, str) and len(dt) >= 4 and dt[:4].isdigit():
        return int(dt[:4])
    sdt = props.get("start_datetime")
    edt = props.get("end_datetime")
    for v in (edt, sdt):
        if isinstance(v, str) and len(v) >= 4 and v[:4].isdigit():
            return int(v[:4])
    return None


def _compact_bbox(bbox: Any) -> str:
    try:
        if isinstance(bbox, (list, tuple)) and len(bbox) >= 4:
            return f"[{bbox[0]:.4f}, {bbox[1]:.4f}, {bbox[2]:.4f}, {bbox[3]:.4f}]"
    except Exception:
        pass
    return "[]"


def load_stac_items(paths: Iterable[str], quiet: bool = False) -> List[Dict[str, Any]]:
    """
    Read JSON from the given paths/globs/dirs and return only STAC Items (Feature).
    Non-Item JSON files are ignored (with a WARN unless --quiet).
    """
    items: List[Dict[str, Any]] = []
    for p in _iter_paths(paths):
        try:
            data = _read_json(p)
            if _is_item(data):
                items.append(data)
            else:
                if not quiet:
                    print(f"[WARN] Skipping non-Item JSON: {p}", file=sys.stderr)
        except Exception as e:
            if not quiet:
                print(f"[WARN] Failed to read {p}: {e}", file=sys.stderr)
    return items


# -----------------------------------------------------------------------------
# Validation
# -----------------------------------------------------------------------------

def validate_stac_items(
    items: List[Dict[str, Any]],
    schema_file: Optional[Path] = None,
    strict: bool = True,
    fail_fast: bool = False,
    quiet: bool = False,
) -> Tuple[int, int, List[Dict[str, Any]]]:
    """
    Validate a list of STAC Item dicts.
    Returns (n_valid, n_invalid, report_entries).

    If jsonschema is not installed (or strict=False), performs minimal structural checks.
    """
    n_ok = 0
    n_bad = 0
    report: List[Dict[str, Any]] = []

    if schema_file is None:
        schema_file = schema_path("stac_item.schema.json")

    schema = load_json_schema(schema_file.name)

    if HAS_JSONSCHEMA and strict:
        validator = jsonschema.Draft202012Validator(schema)  # type: ignore[attr-defined]
        for it in items:
            id_ = it.get("id", "<no id>")
            errs = sorted(validator.iter_errors(it), key=lambda e: (list(e.path), e.message))
            if errs:
                n_bad += 1
                if not quiet:
                    print(f"[FAIL] {id_}:", file=sys.stderr)
                    for e in errs[:10]:
                        where = "/".join(str(x) for x in e.path)
                        print(f"  - {where}: {e.message}", file=sys.stderr)
                    if len(errs) > 10:
                        print(f"  ... and {len(errs) - 10} more error(s)", file=sys.stderr)
                report.append({
                    "id": id_,
                    "valid": False,
                    "errors": [{"path": list(e.path), "message": e.message} for e in errs],
                })
                if fail_fast:
                    return n_ok, n_bad, report
            else:
                n_ok += 1
                report.append({"id": id_, "valid": True, "errors": []})
        return n_ok, n_bad, report

    # Minimal fallback checks (no jsonschema or not strict)
    required_top = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]
    for it in items:
        id_ = it.get("id", "<no id>")
        missing = [k for k in required_top if k not in it]
        extra_msgs: List[str] = []
        if it.get("type") != "Feature":
            extra_msgs.append("type must be 'Feature'")
        if missing:
            extra_msgs.append(f"missing {missing}")
        if extra_msgs:
            n_bad += 1
            if not quiet:
                print(f"[FAIL] {id_}: " + "; ".join(extra_msgs), file=sys.stderr)
            report.append({
                "id": id_,
                "valid": False,
                "errors": [{"path": [], "message": " ; ".join(extra_msgs)}],
            })
            if fail_fast:
                return n_ok, n_bad, report
            continue
        n_ok += 1
        report.append({"id": id_, "valid": True, "errors": []})

    if strict and not HAS_JSONSCHEMA and not quiet:
        print("[WARN] jsonschema not installed; performed minimal checks only.", file=sys.stderr)

    return n_ok, n_bad, report


# -----------------------------------------------------------------------------
# Rendering
# -----------------------------------------------------------------------------

def render_app_config(
    stac_items: List[Dict[str, Any]],
    template_name: str = "app.config.json.j2",
    output: Optional[Path] = None,
    context_path: Optional[Path] = None,
    extra_ctx: Optional[Dict[str, Any]] = None,
    pretty: bool = False,
) -> str:
    """
    Render the web/app.config.json using a Jinja2 template and provided context.
    Returns the rendered JSON text. If 'output' is provided (or '-' for stdout), writes there.
    """
    if not HAS_JINJA2:
        raise RuntimeError("Jinja2 is required for render-config (pip install jinja2).")

    # Baseline context
    ctx: Dict[str, Any] = {
        "title": "Kansas Geo Timeline",
        "subtitle": "Historical + geological layers over time",
        "stac_items": stac_items,
    }

    # Merge optional external context (JSON file)
    if context_path:
        with context_path.open("r", encoding="utf-8") as f:
            ext = json.load(f)
        if isinstance(ext, dict):
            ctx.update(ext)
        else:
            raise ValueError(f"Context file must be a JSON object: {context_path}")

    # Merge extra_ctx last
    if extra_ctx:
        if not isinstance(extra_ctx, dict):
            raise ValueError("extra_ctx must be a dict")
        ctx.update(extra_ctx)

    # Provide a best-effort year per item for the template (if not present)
    for it in ctx.get("stac_items", []):
        props = it.get("properties", {}) or {}
        props["_year"] = _extract_year(props)
        it["properties"] = props

    # Load and render template
    t_path = template_path(template_name)
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(t_path.parent)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    tmpl = env.get_template(t_path.name)
    rendered = tmpl.render(**ctx)

    # Validate it is valid JSON; pretty-print if requested (ensures canonical formatting)
    parsed = json.loads(rendered)
    if pretty:
        rendered = json.dumps(parsed, ensure_ascii=False, indent=2, sort_keys=False)
    else:
        rendered = json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))

    # Write if requested
    if output:
        if str(output) == "-":
            sys.stdout.write(rendered + ("\n" if not rendered.endswith("\n") else ""))
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("w", encoding="utf-8") as f:
                f.write(rendered)
            print(f"[OK] wrote {output}")
    return rendered


# -----------------------------------------------------------------------------
# list-stac
# -----------------------------------------------------------------------------

def _write_table(items: List[Dict[str, Any]], out: io.TextIOBase) -> None:
    header = f"{'ID':40}  {'TIME':20}  BBOX"
    out.write(header + "\n")
    out.write("-" * len(header) + "\n")
    for it in items:
        pid = str(it.get("id", ""))[:40].ljust(40)
        props = it.get("properties", {}) or {}
        dt = props.get("datetime")
        sd = props.get("start_datetime")
        ed = props.get("end_datetime")
        if isinstance(dt, str):
            time_str = dt
        elif isinstance(sd, str) or isinstance(ed, str):
            time_str = f"{sd or ''}/{ed or ''}"
        else:
            time_str = "n/a"
        time_str = time_str[:20].ljust(20)
        bbox = _compact_bbox(it.get("bbox"))
        out.write(f"{pid}  {time_str}  {bbox}\n")


def _write_jsonl(items: List[Dict[str, Any]], out: io.TextIOBase) -> None:
    for it in items:
        out.write(json.dumps(it, ensure_ascii=False) + "\n")


def _write_csv(items: List[Dict[str, Any]], out: io.TextIOBase) -> None:
    writer = csv.writer(out)
    writer.writerow(["id", "time", "bbox"])
    for it in items:
        pid = str(it.get("id", ""))
        props = it.get("properties", {}) or {}
        dt = props.get("datetime")
        sd = props.get("start_datetime")
        ed = props.get("end_datetime")
        if isinstance(dt, str):
            time_str = dt
        elif isinstance(sd, str) or isinstance(ed, str):
            time_str = f"{sd or ''}/{ed or ''}"
        else:
            time_str = ""
        bbox = _compact_bbox(it.get("bbox"))
        writer.writerow([pid, time_str, bbox])


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def _add_common_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("-q", "--quiet", action="store_true", help="Reduce log verbosity.")
    p.add_argument("-V", "--version", action="version", version=f"kansas_geo_timeline {__version__}")


def _cmd_validate_stac(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="kgt validate-stac", description="Validate STAC Item JSON files.")
    _add_common_args(ap)
    ap.add_argument("paths", nargs="+", help="Files / directories / globs for STAC Item JSON.")
    ap.add_argument("--schema", type=Path, default=None, help="Path to schema JSON (defaults to stac_item.schema.json).")
    ap.add_argument("--no-strict", action="store_true", help="If set, use minimal checks even if jsonschema is present.")
    ap.add_argument("--fail-fast", action="store_true", help="Stop at first invalid item.")
    ap.add_argument("--report-json", type=Path, help="Optional JSON report path with per-item results.")
    args = ap.parse_args(argv)

    items = load_stac_items(args.paths, quiet=args.quiet)
    if not items:
        if not args.quiet:
            print("[WARN] No STAC items found.", file=sys.stderr)
        return 1

    n_ok, n_bad, report = validate_stac_items(
        items,
        schema_file=args.schema,
        strict=not args.no_strict,
        fail_fast=args.fail_fast,
        quiet=args.quiet,
    )
    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        with args.report_json.open("w", encoding="utf-8") as f:
            json.dump({"valid": n_ok, "invalid": n_bad, "items": report}, f, ensure_ascii=False, indent=2)
        if not args.quiet:
            print(f"[OK] wrote {args.report_json}")

    if not args.quiet:
        print(f"[RESULT] {n_ok} valid, {n_bad} invalid")
    return 0 if n_bad == 0 else 2


def _cmd_render_config(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="kgt render-config", description="Render web/app.config.json from STAC Items.")
    _add_common_args(ap)
    ap.add_argument("--stac", nargs="+", required=True, help="Files / directories / globs for STAC Item JSON.")
    ap.add_argument("--template", default="app.config.json.j2", help="Template file name under templates/.")
    ap.add_argument("--output", type=Path, required=True, help="Output path (e.g., web/app.config.json or '-' for stdout).")
    ap.add_argument("--context", type=Path, help="Additional context JSON with basemaps/layers/etc.")
    ap.add_argument("--ctx", type=str, default=None, help="Inline JSON to merge into context (last).")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = ap.parse_args(argv)

    items = load_stac_items(args.stac, quiet=args.quiet)
    if not items:
        print("[ERROR] No STAC items to render.", file=sys.stderr)
        return 1

    extra_ctx: Optional[Dict[str, Any]] = None
    if args.ctx:
        try:
            extra_ctx = json.loads(args.ctx)
            if not isinstance(extra_ctx, dict):
                raise ValueError("Inline --ctx JSON must be an object")
        except Exception as e:
            print(f"[ERROR] --ctx parse error: {e}", file=sys.stderr)
            return 2

    try:
        render_app_config(
            items,
            template_name=args.template,
            output=args.output,
            context_path=args.context,
            extra_ctx=extra_ctx,
            pretty=args.pretty,
        )
    except Exception as e:
        print(f"[ERROR] render-config failed: {e}", file=sys.stderr)
        return 2

    return 0


def _cmd_list_stac(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="kgt list-stac", description="List STAC Items (id, time, bbox).")
    _add_common_args(ap)
    ap.add_argument("paths", nargs="+", help="Files / directories / globs for STAC Item JSON.")
    ap.add_argument("--format", choices=["table", "jsonl", "csv"], default="table", help="Output format.")
    ap.add_argument("--output", type=Path, help="Write to file path, or '-' for stdout (default: stdout for table/jsonl; csv also allowed).")
    args = ap.parse_args(argv)

    items = load_stac_items(args.paths, quiet=args.quiet)
    if not items:
        if not args.quiet:
            print("[WARN] No STAC items found.", file=sys.stderr)
        return 1

    # Determine sink
    sink: io.TextIOBase
    close_sink = False
    if args.output and str(args.output) not in ("-", ""):
        args.output.parent.mkdir(parents=True, exist_ok=True)
        sink = args.output.open("w", encoding="utf-8", newline="")
        close_sink = True
    else:
        sink = sys.stdout

    try:
        if args.format == "table":
            _write_table(items, sink)
        elif args.format == "jsonl":
            _write_jsonl(items, sink)
        else:  # csv
            _write_csv(items, sink)
    finally:
        if close_sink:
            sink.close()

    return 0


def main(argv: Optional[List[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        # Top-level help
        print(
            "kgt — Kansas Geo Timeline CLI\n"
            "Usage:\n"
            "  kgt validate-stac <paths...> [--schema PATH] [--no-strict] [--fail-fast] [--report-json PATH]\n"
            "  kgt render-config --stac <paths...> --output PATH|'-' [--template NAME] [--context JSON] [--ctx JSON] [--pretty]\n"
            "  kgt list-stac <paths...> [--format table|jsonl|csv] [--output PATH|'-']\n"
            "Options:\n"
            "  -V, --version    Show version\n"
            "  -q, --quiet      Reduce log verbosity\n",
            file=sys.stderr,
        )
        return 1

    cmd, *rest = argv
    if cmd in ("validate-stac", "validate", "vs"):
        return _cmd_validate_stac(rest)
    if cmd in ("render-config", "render", "rc"):
        return _cmd_render_config(rest)
    if cmd in ("list-stac", "list", "ls"):
        return _cmd_list_stac(rest)

    print(f"[ERROR] Unknown command: {cmd}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
