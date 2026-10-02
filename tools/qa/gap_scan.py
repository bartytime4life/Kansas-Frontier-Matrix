#!/usr/bin/env python3
"""Census repository gaps that the scaffold ratchet does not cover, and ratchet them.

The scaffold inventory (``scaffold_inventory.py``) owns placeholder, stub, blank,
and vacuous files on executable and contract surfaces. This helper covers the
complementary gaps found while auditing the tree:

* ``STRUCTURED_PARSE_ERROR``   tracked JSON, GeoJSON, YAML, or TOML that does not parse,
                               outside declared negative-fixture locations
* ``TEST_PACKAGE_SHADOW``      ``tests/<name>/__init__.py`` turning ``tests/<name>`` into a
                               top-level ``<name>`` package that shadows an imported repository
                               root of the same name under pytest's default import mode
* ``BROKEN_LOCAL_LINK``        inline Markdown link whose repository-local target is absent
                               (``docs/archive/`` is frozen lineage and is excluded)
* ``UNRATCHETED_PLACEHOLDER``  non-Markdown file outside the scaffold surfaces whose header
                               declares a PROPOSED/greenfield placeholder or scaffold

Parse errors and shadowing packages are invariants: ``--check`` fails on any.
Broken links and unratcheted placeholders are census counts: ``--check`` fails
only when a count rises above ``gap_scan_baseline.json``. Lower counts pass and
print a reminder to tighten the baseline with ``--write-baseline``.

The scan is local, deterministic, and makes no network requests. Its output is a
review aid; it grants no readiness, release, admission, or publication authority.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tomllib
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ROOT / "tools" / "qa" / "gap_scan_baseline.json"
SCHEMA_VERSION = "kfm.gap-scan/v1"
INVARIANT_KINDS = ("STRUCTURED_PARSE_ERROR", "TEST_PACKAGE_SHADOW")
CENSUS_KINDS = ("BROKEN_LOCAL_LINK", "UNRATCHETED_PLACEHOLDER")

# Kept in step with scaffold_inventory.SURFACES; files there are already ratcheted.
SCAFFOLD_SURFACES = ("scripts", "tools", "pipelines", "pipeline_specs", "connectors",
                     "packages", "apps", "tests", ".github/workflows", "schemas",
                     "contracts", "policy")
STRUCTURED_SUFFIXES = frozenset({".json", ".geojson", ".yaml", ".yml", ".toml"})
NEGATIVE_SEGMENTS = frozenset({"invalid", "malformed", "negative", "bad", "broken"})
NEGATIVE_NAME = re.compile(r"(?:^|[_.-])(?:invalid|malformed|bad|broken|corrupt)(?:[_.-]|$)")
MARKER = re.compile(r"\b(?:greenfield|PROPOSED)\s+(?:placeholder|scaffold)\b", re.IGNORECASE)
HEADER_LINES = 6
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(\s*(?:<([^>]+)>|([^)\s]+))(?:\s+"[^"]*")?\s*\)')
FENCE = re.compile(r"^\s*(?:```|~~~)")
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
IMPORT_NAME = r"^\s*(?:from|import)\s+{name}(?:\.|\s|$)"


def tracked_files(root: Path) -> list[str]:
    """Tracked paths that are present as regular files in the working tree."""
    completed = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True,
                               check=True)
    paths = (p for p in completed.stdout.decode("utf-8").split("\0") if p)
    return sorted(p for p in paths
                  if (root / p).is_file() and not (root / p).is_symlink())


def _directories(paths: list[str]) -> set[str]:
    dirs: set[str] = set()
    for path in paths:
        while "/" in path:
            path = path.rsplit("/", 1)[0]
            if path in dirs:
                break
            dirs.add(path)
    return dirs


def is_negative_fixture(path: str) -> bool:
    parts = path.split("/")
    if NEGATIVE_SEGMENTS & {part.lower() for part in parts[:-1]}:
        return True
    return bool(NEGATIVE_NAME.search(Path(parts[-1]).stem.lower()))


def _parse_error(path: str, data: bytes) -> str | None:
    suffix = Path(path).suffix.lower()
    try:
        text = data.decode("utf-8")
        if suffix in {".json", ".geojson"}:
            json.loads(text)
        elif suffix in {".yaml", ".yml"}:
            list(yaml.safe_load_all(text))
        elif suffix == ".toml":
            tomllib.loads(text)
        else:
            return None
    except (ValueError, UnicodeDecodeError, yaml.YAMLError) as exc:
        message = str(exc)
        return message.splitlines()[0][:160] if message else type(exc).__name__
    return None


def scan_parse_errors(root: Path, files: list[str]) -> list[dict[str, str]]:
    findings = []
    for path in files:
        if Path(path).suffix.lower() not in STRUCTURED_SUFFIXES or is_negative_fixture(path):
            continue
        detail = _parse_error(path, (root / path).read_bytes())
        if detail is not None:
            findings.append({"kind": "STRUCTURED_PARSE_ERROR", "path": path, "detail": detail})
    return findings


def scan_test_shadows(root: Path, files: list[str]) -> list[dict[str, str]]:
    findings = []
    python_files = [p for p in files if p.endswith(".py")]
    for path in files:
        parts = path.split("/")
        if len(parts) != 3 or parts[0] != "tests" or parts[2] != "__init__.py":
            continue
        name = parts[1]
        if not (root / name).is_dir() or (root / "tests" / "__init__.py").exists():
            continue
        pattern = re.compile(IMPORT_NAME.format(name=re.escape(name)), re.MULTILINE)
        importers = [p for p in python_files if not p.startswith(f"tests/{name}/")
                     and pattern.search((root / p).read_text(encoding="utf-8", errors="ignore"))]
        if importers:
            findings.append({"kind": "TEST_PACKAGE_SHADOW", "path": path,
                             "detail": f"shadows root '{name}/' imported by {len(importers)} "
                                       f"module(s), e.g. {importers[0]}"})
    return findings


def _link_targets(text: str):
    in_fence = False
    for number, line in enumerate(text.split("\n"), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK.finditer(line):
            yield number, match.group(1) or match.group(2)


def scan_links(root: Path, files: list[str]) -> list[dict[str, str]]:
    present = set(files) | _directories(files)
    findings = []
    for path in files:
        if not path.endswith(".md") or path.startswith("docs/archive/"):
            continue
        try:
            text = (root / path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for number, url in _link_targets(text):
            if SCHEME.match(url) or url.startswith("#"):
                continue
            target = unquote(url.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = os.path.normpath(target.lstrip("/") if target.startswith("/")
                                        else os.path.join(os.path.dirname(path), target))
            if resolved == "." or resolved in present:
                continue
            findings.append({"kind": "BROKEN_LOCAL_LINK", "path": f"{path}:{number}",
                             "detail": resolved})
    return findings


def scan_placeholders(root: Path, files: list[str]) -> list[dict[str, str]]:
    findings = []
    for path in files:
        if path.endswith(".md") or any(path == s or path.startswith(s + "/")
                                       for s in SCAFFOLD_SURFACES):
            continue
        if path.startswith(("data/receipts/", "docs/")):
            continue  # receipts and prose quote the marker; they are not scaffolds.
        try:
            head = (root / path).read_text(encoding="utf-8").splitlines()[:HEADER_LINES]
        except (OSError, UnicodeDecodeError):
            continue
        if MARKER.search("\n".join(head)):
            findings.append({"kind": "UNRATCHETED_PLACEHOLDER", "path": path, "detail": ""})
    return findings


def scan(root: Path = ROOT) -> list[dict[str, str]]:
    files = tracked_files(root)
    return (scan_parse_errors(root, files) + scan_test_shadows(root, files)
            + scan_links(root, files) + scan_placeholders(root, files))


def _root_of(finding: dict[str, str]) -> str:
    target = finding["detail"] if finding["kind"] == "BROKEN_LOCAL_LINK" else finding["path"]
    return target.split("/", 1)[0]


def summarize(findings: list[dict[str, str]]) -> dict[str, object]:
    counts = Counter(f["kind"] for f in findings)
    links = [f for f in findings if f["kind"] == "BROKEN_LOCAL_LINK"]
    return {
        "schema_version": SCHEMA_VERSION,
        "counts": {kind: counts.get(kind, 0) for kind in INVARIANT_KINDS + CENSUS_KINDS},
        "broken_link_targets": len({f["detail"] for f in links}),
        "broken_links_by_target_root": dict(sorted(Counter(_root_of(f) for f in links).items())),
        "top_missing_targets": [{"target": t, "references": n} for t, n in
                                sorted(Counter(f["detail"] for f in links).items(),
                                       key=lambda item: (-item[1], item[0]))[:25]],
        "authority_boundary": "Review aid only; not readiness, release, admission, or "
                              "publication evidence.",
    }


def load_baseline(path: Path = BASELINE) -> dict[str, int]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION or not isinstance(
            payload.get("census"), dict):
        raise ValueError("gap-scan baseline has an unexpected shape")
    return {kind: int(payload["census"][kind]) for kind in CENSUS_KINDS}


def evaluate(summary: dict[str, object], baseline: dict[str, int]) -> tuple[int, list[str]]:
    counts = summary["counts"]
    messages: list[str] = []
    status = 0
    for kind in INVARIANT_KINDS:
        if counts[kind]:
            status = 1
            messages.append(f"{kind}: {counts[kind]} finding(s); this class must stay at zero.")
    for kind in CENSUS_KINDS:
        if counts[kind] > baseline[kind]:
            status = 1
            messages.append(f"{kind}: {counts[kind]} exceeds baseline {baseline[kind]}; fix the "
                            "new gap instead of raising the baseline.")
        elif counts[kind] < baseline[kind]:
            messages.append(f"{kind}: {counts[kind]} is below baseline {baseline[kind]}; run "
                            "`python tools/qa/gap_scan.py --write-baseline` to tighten it.")
    return status, messages


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="fail on invariant findings or census counts above the baseline")
    mode.add_argument("--write-baseline", action="store_true",
                      help="rewrite tools/qa/gap_scan_baseline.json census counts")
    parser.add_argument("--list", action="store_true", help="include every finding in output")
    args = parser.parse_args(argv)
    findings = scan()
    report = summarize(findings)
    if args.write_baseline:
        census = {kind: report["counts"][kind] for kind in CENSUS_KINDS}
        BASELINE.write_text(json.dumps({"schema_version": SCHEMA_VERSION, "census": census},
                                       indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {BASELINE.relative_to(ROOT)}: {census}")
        return 0
    status = 0
    if args.check:
        status, messages = evaluate(report, load_baseline())
        for message in messages:
            print(message, file=sys.stderr)
    if args.list:
        report["findings"] = findings
    elif args.check and status:
        report["findings"] = [f for f in findings if f["kind"] in INVARIANT_KINDS]
    print(json.dumps(report, indent=2, sort_keys=True))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
