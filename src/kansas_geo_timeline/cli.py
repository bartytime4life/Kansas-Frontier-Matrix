#!/usr/bin/env python3
"""
kansas_geo_timeline.cli
=======================

Command-line utilities for the Kansas Geo Timeline / Kansas-Frontier-Matrix stack.

Subcommands
-----------
- validate-stac:  Validate STAC Item JSON files against the local schema.
- render-config:  Render web/app.config.json from STAC Items + optional extra layers/basemaps.
- list-stac:      Print a compact table of STAC Items (id, datetime/range, bbox).

Design
------
- dependency-light by default (stdlib). Optional extras:
  * jsonschema  — if installed, enables strict STAC validation.
  * jinja2      — if installed, enables template rendering for app.config.json.

Examples
--------
# Validate all STAC items
kgt validate-stac data/stac/*.json

# Render app config to web/app.config.json using default template
kgt render-config \
  --stac data/stac/*.json \
  --output web/app.config.json

# Provide custom context JSON for basemaps/layers
kgt render-config --stac data/stac/*.json --context configs/render_context.json

"""

from __future__ import annotations

import argparse
import glob
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

# Optional deps
try:  # jsonschema is optional; we fall back to basic checks if absent.
    import jsonschema  # type: ignore

    HAS_JSONSCHEMA = True
except Exception:
    HAS_JSONSCHEMA = False

try:  # jinja2 is optional; only needed for render-config.
    import jinja2  # type: ignore

    HAS_JINJA2 = True
except Exception:
    HAS_JINJA2 = False


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _read_json(p: Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def _iter_paths(patterns: Iterable[str]) -> Iterable[Path]:
    for pat in patterns:
        # Support direct files, dirs, and globs
        p = Path(pat)
        if p.is_dir():
            yield from sorted(p.glob("**/*.json"))
        else:
            for m in sorted(glob.glob(pat)):
                yield Path(m)


def _extract_year(props: Dict[str, Any]) -> Optional[int]:
    # Prefer single datetime if present
    dt = props.get("datetime")
    if isinstance(dt, str) and len(dt) >= 4 and dt[:4].isdigit():
        return int(dt[:4])
    # Else a range
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


def load_stac_items(paths: Iterable[str]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for p in _iter_paths(paths):
        try:
            data = _read_json(p)
            items.append(data)
        except Exception as e:
            print(f"[WARN] Failed to read {p}: {e}", file=sys.stderr)
    return items


def validate_stac_items(
    items: List[Dict[str, Any]],
    schema_file: Optional[Path] = None,
    strict: bool = True,
) -> Tuple[int, int]:
    """
    Validate a list of STAC Item dicts. Returns (n_valid, n_invalid).
    If jsonschema is not installed, performs minimal structural checks.
    """
    n_ok = 0
    n_bad = 0

    if schema_file is None:
        schema_file = schema_path("stac_item.schema.json")

    schema = load_json_schema(schema_file.name)

    if HAS_JSONSCHEMA and strict:
        validator = jsonschema.Draft202012Validator(schema)  # type: ignore[attr-defined]
        for it in items:
            errs = sorted(validator.iter_errors(it), key=lambda e: e.path)
            if errs:
                n_bad += 1
                print(f"[FAIL] {it.get('id', '<no id>')}:")
                for e in errs[:10]:
                    where = "/".join(str(x) for x in e.path)
                    print(f"  - {where}: {e.message}")
                if len(errs) > 10:
                    print(f"  ... and {len(errs) - 10} more error(s)")
            else:
                n_ok += 1
        return n_ok, n_bad

    # Minimal fallback checks (no jsonschema)
    required_top = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]
    for it in items:
        missing = [k for k in required_top if k not in it]
        if missing:
            n_bad += 1
            print(f"[FAIL] {it.get('id','<no id>')}: missing {missing}", file=sys.stderr)
            continue
        if it.get("type") != "Feature":
            n_bad += 1
            print(f"[FAIL] {it.get('id','<no id>')}: type must be 'Feature'", file=sys.stderr)
            continue
        n_ok += 1

    if strict and not HAS_JSONSCHEMA:
        print("[WARN] jsonschema not installed; performed minimal checks only.", file=sys.stderr)

    return n_ok, n_bad


def render_app_config(
    stac_items: List[Dict[str, Any]],
    template_name: str = "app.config.json.j2",
    output: Optional[Path] = None,
    context_path: Optional[Path] = None,
    extra_ctx: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Render the web/app.config.json using a Jinja2 template and provided context.
    Returns the rendered JSON text. If 'output' is provided, writes to that path.
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
        try:
            with context_path.open("r", encoding="utf-8") as f:
                ext = json.load(f)
            if isinstance(ext, dict):
                ctx.update(ext)
        except Exception as e:
            print(f"[WARN] Failed reading context {context_path}: {e}", file=sys.stderr)

    # Merge extra_ctx last
    if extra_ctx:
        ctx.update(extra_ctx)

    # Provide a best-effort year per item for the template (if not present)
    for it in ctx.get("stac_items", []):
        props = it.get("properties", {}) or {}
        year = _extract_year(props)
        # Attach a convenience field: properties._year (non-STAC, template-only)
        props["_year"] = year
        it["properties"] = props

    # Load template
    t_path = template_path(template_name)
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(t_path.parent)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    tmpl = env.get_template(t_path.name)
    rendered = tmpl.render(**ctx)

    # Optional write
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"[OK] wrote {output}")
    return rendered


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
    ap.add_argument("--no-strict", action="store_true", help="If set, use minimal checks when jsonschema is present.")
    args = ap.parse_args(argv)

    items = load_stac_items(args.paths)
    if not items:
        print("[WARN] No STAC items found.", file=sys.stderr)
        return 1

    n_ok, n_bad = validate_stac_items(items, schema_file=args.schema, strict=not args.no_strict)
    print(f"[RESULT] {n_ok} valid, {n_bad} invalid")
    return 0 if n_bad == 0 else 2


def _cmd_render_config(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="kgt render-config", description="Render web/app.config.json from STAC Items.")
    _add_common_args(ap)
    ap.add_argument("--stac", nargs="+", required=True, help="Files / directories / globs for STAC Item JSON.")
    ap.add_argument("--template", default="app.config.json.j2", help="Template file name under templates/.")
    ap.add_argument("--output", type=Path, required=True, help="Output path (e.g., web/app.config.json).")
    ap.add_argument("--context", type=Path, help="Additional context JSON with basemaps/layers/etc.")
    ap.add_argument("--ctx", type=str, default=None, help="Inline JSON to merge into context (last).")
    args = ap.parse_args(argv)

    items = load_stac_items(args.stac)
    if not items:
        print("[ERROR] No STAC items to render.", file=sys.stderr)
        return 1

    extra_ctx = None
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
        )
    except Exception as e:
        print(f"[ERROR] render-config failed: {e}", file=sys.stderr)
        return 2

    return 0


def _cmd_list_stac(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="kgt list-stac", description="List STAC Items (id, year/range, bbox).")
    _add_common_args(ap)
    ap.add_argument("paths", nargs="+", help="Files / directories / globs for STAC Item JSON.")
    args = ap.parse_args(argv)

    items = load_stac_items(args.paths)
    if not items:
        print("[WARN] No STAC items found.", file=sys.stderr)
        return 1

    print(f"{'ID':40}  {'TIME':20}  BBOX")
    print("-" * 92)
    for it in items:
        pid = str(it.get("id", ""))[:40].ljust(40)
        props = it.get("properties", {}) or {}
        dt = props.get("datetime")
        sd = props.get("start_datetime")
        ed = props.get("end_datetime")
        time_str = ""
        if isinstance(dt, str):
            time_str = dt
        elif isinstance(sd, str) or isinstance(ed, str):
            time_str = f"{sd or ''}/{ed or ''}"
        else:
            time_str = "n/a"
        time_str = time_str[:20].ljust(20)
        bbox = _compact_bbox(it.get("bbox"))
        print(f"{pid}  {time_str}  {bbox}")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        # Top-level help
        print(
            "kgt — Kansas Geo Timeline CLI\n"
            "Usage:\n"
            "  kgt validate-stac <paths...> [--schema PATH] [--no-strict]\n"
            "  kgt render-config --stac <paths...> --output web/app.config.json [--template NAME] [--context JSON] [--ctx JSON]\n"
            "  kgt list-stac <paths...>\n"
            "Options:\n"
            "  -V, --version    Show version\n",
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

