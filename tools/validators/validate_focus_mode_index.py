#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_focus_mode_index.py — Lightweight validator for the KFM County Focus Mode control plane.

Status: PROPOSED implementation. Stdlib-only (no PyYAML, no third-party deps) so the validator
runs in any CI lane and can be vendored without negotiation. Discovered and orchestrated by
tools/validate_all.py per directory-rules.md §7.5.a.

Doctrine basis (CONFIRMED):
  - directory-rules.md §6.7 (Focus Modes placement contract)
  - directory-rules.md §6.7.2 (per-host-root casing)
  - directory-rules.md §15 (per-root README contract)
  - kfm_repository_structure_guiding_document.md §8 (Focus Mode placement contract)
  - Master_MapLibre_Components-Functions-Features_v2_1_FULL.md §16.3 (COUNTY-01..04)

Checks performed (mirror docs/focus-modes/README.md §8):
  C01: COUNTY_INDEX.md parses; table has exactly the 105 KS counties; no duplicates.
  C02: Statuses are in the declared enum.
  C03: Every row with status >= 'planned' has a matching lane folder.
  C04: Every lane folder contains the seven required files.
  C05: Every build-plan.md has YAML-like front-matter with required keys.
  C06: ui_shell front-matter value is "apps/explorer-web" (apps/web is drift per OPEN-DR-06).
  C07: No .schema.json files anywhere under docs/focus-modes/ (schema-home violation).
  C08: No 'apps/web/src/focus-modes/' references in any lane file.
  C09: Area lane names match kebab-case + scope suffix pattern.
  C10: No county is claimed by two different area lanes.
  C11: Every acceptance-checklist.md mentions the 8 COUNTY-01 acceptance items (a)..(h).
  C12: Internal markdown links resolve (best-effort; relative paths only).

Exit codes:
  0 = all pass
  1 = at least one check failed
  2 = system error (paths missing, parse error)

Usage:
  python tools/validators/validate_focus_mode_index.py docs/focus-modes/
  python tools/validators/validate_focus_mode_index.py docs/focus-modes/ --emit-json out.json
  python tools/validators/validate_focus_mode_index.py docs/focus-modes/ --strict
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ----------------------------------------------------------------------
# Reference data
# ----------------------------------------------------------------------

# CONFIRMED: 105 Kansas counties (alphabetical).
KANSAS_COUNTIES: Tuple[str, ...] = (
    "Allen", "Anderson", "Atchison", "Barber", "Barton", "Bourbon", "Brown",
    "Butler", "Chase", "Chautauqua", "Cherokee", "Cheyenne", "Clark", "Clay",
    "Cloud", "Coffey", "Comanche", "Cowley", "Crawford", "Decatur", "Dickinson",
    "Doniphan", "Douglas", "Edwards", "Elk", "Ellis", "Ellsworth", "Finney",
    "Ford", "Franklin", "Geary", "Gove", "Graham", "Grant", "Gray", "Greeley",
    "Greenwood", "Hamilton", "Harper", "Harvey", "Haskell", "Hodgeman",
    "Jackson", "Jefferson", "Jewell", "Johnson", "Kearny", "Kingman", "Kiowa",
    "Labette", "Lane", "Leavenworth", "Lincoln", "Linn", "Logan", "Lyon",
    "Marion", "Marshall", "McPherson", "Meade", "Miami", "Mitchell",
    "Montgomery", "Morris", "Morton", "Nemaha", "Neosho", "Ness", "Norton",
    "Osage", "Osborne", "Ottawa", "Pawnee", "Phillips", "Pottawatomie", "Pratt",
    "Rawlins", "Reno", "Republic", "Rice", "Riley", "Rooks", "Rush", "Russell",
    "Saline", "Scott", "Sedgwick", "Seward", "Shawnee", "Sheridan", "Sherman",
    "Smith", "Stafford", "Stanton", "Stevens", "Sumner", "Thomas", "Trego",
    "Wabaunsee", "Wallace", "Washington", "Wichita", "Wilson", "Woodson",
    "Wyandotte",
)
assert len(KANSAS_COUNTIES) == 105, "KANSAS_COUNTIES list must contain exactly 105 entries"

VALID_STATUSES: Tuple[str, ...] = (
    "not-started", "planned", "draft", "validated",
    "payload-ready", "released", "rolled-back", "deprecated",
)
STATUS_ORDER = {s: i for i, s in enumerate(VALID_STATUSES)}
STATUS_REQUIRES_LANE_AT_OR_ABOVE = "planned"  # status >= planned requires a lane folder

VALID_SCOPES: Tuple[str, ...] = ("county", "region", "corridor")
VALID_PRIORITIES: Tuple[str, ...] = ("P1", "P2", "P3", "—", "")

REQUIRED_LANE_FILES: Tuple[str, ...] = (
    "README.md",
    "build-plan.md",
    "layer-registry.md",
    "evidence-model.md",
    "acceptance-checklist.md",
    "source-seed-list.md",
    "public-safety-notes.md",
)

REQUIRED_FRONTMATTER_KEYS: Tuple[str, ...] = (
    "schema_version", "kfm_artifact", "area", "status", "owner",
    "priority", "last_reviewed", "plan_anchors", "ui_shell",
    "canonical_paths", "sensitivity_lanes", "sensitivity_overrides",
    "source_seed_families", "release",
)

ACCEPTANCE_ITEMS: Tuple[str, ...] = (
    "(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)",
)

LANE_NAME_RE = re.compile(r"^[a-z][a-z0-9\-]*-(county|region|corridor)$")
COUNTY_SLUG_RE = re.compile(r"^[a-z][a-z0-9\-]*$")

# Markers we refuse to see anywhere in lane content
FORBIDDEN_PATH_SUBSTRINGS: Tuple[str, ...] = (
    "apps/web/src/focus-modes/",  # OPEN-DR-06 drift
)


# ----------------------------------------------------------------------
# Data classes
# ----------------------------------------------------------------------

@dataclass
class CheckResult:
    name: str
    status: str  # "pass" | "fail" | "warn" | "skip"
    details: List[str] = field(default_factory=list)
    affected: List[str] = field(default_factory=list)

    def add(self, msg: str, item: Optional[str] = None) -> None:
        self.details.append(msg)
        if item:
            self.affected.append(item)


@dataclass
class IndexRow:
    county: str
    lane: str
    status: str
    owner: str
    priority: str
    sensitivity_hot_lanes: str
    source_seed_family: str
    validation: str
    source_line: int


@dataclass
class ValidationReport:
    schema_version: str
    focus_modes_dir: str
    checks: List[CheckResult]
    overall_status: str  # "pass" | "fail" | "error"

    def to_dict(self) -> Dict:
        return {
            "schema_version": self.schema_version,
            "focus_modes_dir": self.focus_modes_dir,
            "overall_status": self.overall_status,
            "checks": [asdict(c) for c in self.checks],
        }


# ----------------------------------------------------------------------
# Parsing helpers (stdlib only)
# ----------------------------------------------------------------------

def _slugify_county(name: str) -> str:
    """Convert 'McPherson' -> 'mcpherson', 'Wyandotte' -> 'wyandotte'."""
    return name.strip().lower()


def parse_index_table(index_md: Path) -> Tuple[List[IndexRow], List[str]]:
    """
    Parse the §3 markdown table in COUNTY_INDEX.md.

    Returns (rows, parse_errors). Parse errors do NOT raise; the caller decides.
    The parser is intentionally simple: it locates the first table whose header
    contains 'County', 'Lane', 'Status' in that order.
    """
    errors: List[str] = []
    if not index_md.exists():
        errors.append(f"COUNTY_INDEX.md not found at {index_md}")
        return ([], errors)

    text = index_md.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Locate header line and separator
    header_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("|") and "County" in stripped and "Lane" in stripped and "Status" in stripped:
            # Verify next line is a separator (| --- | ...)
            if i + 1 < len(lines) and re.match(r"^\|\s*[-:]+", lines[i + 1].strip()):
                header_idx = i
                break

    if header_idx is None:
        errors.append("Could not locate the master county table (header with 'County | Lane | Status').")
        return ([], errors)

    # Parse header to map column positions
    header_cells = [c.strip() for c in lines[header_idx].strip().strip("|").split("|")]
    col_map = {name: idx for idx, name in enumerate(header_cells)}
    required_cols = ("County", "Lane", "Status", "Owner", "Priority",
                     "Sensitivity hot lanes", "Source-seed family", "Validation")
    for col in required_cols:
        if col not in col_map:
            errors.append(f"Master table missing required column: {col!r}")
    if errors:
        return ([], errors)

    rows: List[IndexRow] = []
    for i in range(header_idx + 2, len(lines)):
        line = lines[i].strip()
        if not line.startswith("|"):
            break
        if re.match(r"^\|\s*[-:]+", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < len(header_cells):
            errors.append(f"Line {i + 1}: row has {len(cells)} cells; expected {len(header_cells)}")
            continue
        rows.append(
            IndexRow(
                county=cells[col_map["County"]],
                lane=cells[col_map["Lane"]].strip("`"),
                status=cells[col_map["Status"]],
                owner=cells[col_map["Owner"]],
                priority=cells[col_map["Priority"]],
                sensitivity_hot_lanes=cells[col_map["Sensitivity hot lanes"]],
                source_seed_family=cells[col_map["Source-seed family"]],
                validation=cells[col_map["Validation"]],
                source_line=i + 1,
            )
        )
    return (rows, errors)


def extract_frontmatter(md_path: Path) -> Tuple[Dict[str, str], List[str]]:
    """
    Extract YAML-like front-matter from a markdown file.

    Returns (top_level_keys_present, errors). This is intentionally minimal:
    it does NOT parse nested structures; it only confirms required *top-level*
    keys appear after the opening '---' fence at the head of the file.

    For deeper validation, a follow-up pass with PyYAML is recommended once
    PyYAML is approved as a tools/validators/ dependency (ADR-class decision).
    """
    errors: List[str] = []
    keys_present: Dict[str, str] = {}
    if not md_path.exists():
        errors.append(f"{md_path} not found")
        return (keys_present, errors)

    text = md_path.read_text(encoding="utf-8")
    # Allow leading HTML comment and blank lines before the front-matter fence
    fm_match = re.search(r"(?:\A|\n)---\n(.*?)\n---\n", text, re.DOTALL)
    if not fm_match:
        errors.append(f"{md_path}: no YAML front-matter block found")
        return (keys_present, errors)

    body = fm_match.group(1)
    for raw_line in body.splitlines():
        # Skip comments and blank lines
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        # Top-level key:value (no leading whitespace)
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", raw_line)
        if m and not raw_line.startswith((" ", "\t")):
            key = m.group(1)
            val = m.group(2).strip()
            keys_present[key] = val
    return (keys_present, errors)


def get_frontmatter_value(md_path: Path, key: str) -> Optional[str]:
    """
    Best-effort retrieval of a top-level scalar value (e.g., ui_shell).
    Returns None if not found.
    """
    keys, _errs = extract_frontmatter(md_path)
    raw = keys.get(key)
    if raw is None:
        return None
    # Strip surrounding quotes
    raw = raw.strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        raw = raw[1:-1]
    return raw


def find_markdown_links(text: str) -> List[str]:
    """Return relative-path link targets ([text](path)) excluding http(s), mailto, anchors."""
    targets = []
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        tgt = m.group(1).strip()
        if tgt.startswith(("http://", "https://", "mailto:", "#")):
            continue
        targets.append(tgt)
    return targets


# ----------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------

def check_c01_index_parses_and_counties(rows: List[IndexRow], parse_errors: List[str]) -> CheckResult:
    r = CheckResult(name="C01_index_parses_and_105_counties", status="pass")
    if parse_errors:
        r.status = "fail"
        for e in parse_errors:
            r.add(e)
        return r
    counties_seen = [row.county for row in rows]
    if len(counties_seen) != 105:
        r.status = "fail"
        r.add(f"Expected 105 county rows; found {len(counties_seen)}")
    expected = set(KANSAS_COUNTIES)
    actual = set(counties_seen)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        r.status = "fail"
        r.add(f"Counties missing from index: {missing}")
        r.affected.extend(missing)
    if extra:
        r.status = "fail"
        r.add(f"Counties not in Kansas (typos or extras): {extra}")
        r.affected.extend(extra)
    # Duplicate detection
    seen: Set[str] = set()
    dups: List[str] = []
    for c in counties_seen:
        if c in seen:
            dups.append(c)
        seen.add(c)
    if dups:
        r.status = "fail"
        r.add(f"Duplicate county rows: {sorted(set(dups))}")
        r.affected.extend(sorted(set(dups)))
    return r


def check_c02_statuses_in_enum(rows: List[IndexRow]) -> CheckResult:
    r = CheckResult(name="C02_statuses_in_enum", status="pass")
    for row in rows:
        if row.status not in VALID_STATUSES:
            r.status = "fail"
            r.add(f"Line {row.source_line}: status {row.status!r} not in {list(VALID_STATUSES)}", row.county)
    return r


def check_c03_lane_folders_exist(rows: List[IndexRow], focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C03_lane_folder_present_when_status_planned_or_above", status="pass")
    threshold = STATUS_ORDER[STATUS_REQUIRES_LANE_AT_OR_ABOVE]
    for row in rows:
        if row.status not in STATUS_ORDER:
            continue
        if STATUS_ORDER[row.status] >= threshold:
            lane_dir = focus_modes_dir / row.lane
            if not lane_dir.is_dir():
                r.status = "fail"
                r.add(
                    f"Line {row.source_line}: status={row.status!r} but lane folder absent: {lane_dir}",
                    row.lane,
                )
    return r


def check_c04_required_lane_files(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C04_seven_required_files_per_lane", status="pass")
    if not focus_modes_dir.is_dir():
        r.status = "skip"
        r.add(f"{focus_modes_dir} is not a directory")
        return r
    for child in sorted(focus_modes_dir.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith("_") or child.name.startswith("."):
            continue  # skip _template, hidden
        if not LANE_NAME_RE.match(child.name):
            continue  # naming check is C09
        missing = []
        for fname in REQUIRED_LANE_FILES:
            if not (child / fname).is_file():
                missing.append(fname)
        if missing:
            r.status = "fail"
            r.add(f"{child.name}: missing required files: {missing}", child.name)
    return r


def check_c05_frontmatter_keys(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C05_build_plan_frontmatter_required_keys", status="pass")
    for child in sorted(focus_modes_dir.iterdir()) if focus_modes_dir.is_dir() else []:
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        bp = child / "build-plan.md"
        if not bp.exists():
            continue  # absence reported by C04
        keys, errs = extract_frontmatter(bp)
        if errs:
            r.status = "fail"
            for e in errs:
                r.add(e, child.name)
            continue
        missing = [k for k in REQUIRED_FRONTMATTER_KEYS if k not in keys]
        if missing:
            r.status = "fail"
            r.add(f"{bp.relative_to(focus_modes_dir.parent.parent if focus_modes_dir.parent.parent else focus_modes_dir.parent)}: missing front-matter keys: {missing}", child.name)
    return r


def check_c06_ui_shell_is_explorer_web(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C06_ui_shell_is_apps_explorer_web", status="pass")
    expected = "apps/explorer-web"
    for child in sorted(focus_modes_dir.iterdir()) if focus_modes_dir.is_dir() else []:
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        bp = child / "build-plan.md"
        if not bp.exists():
            continue
        val = get_frontmatter_value(bp, "ui_shell")
        if val is None:
            continue  # absence reported by C05
        if val != expected:
            r.status = "fail"
            r.add(f"{child.name}/build-plan.md: ui_shell={val!r} (expected {expected!r}; apps/web is drift per OPEN-DR-06)", child.name)
    return r


def check_c07_no_schema_json_under_docs(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C07_no_schema_json_under_docs_focus_modes", status="pass")
    if not focus_modes_dir.is_dir():
        return r
    for p in focus_modes_dir.rglob("*.schema.json"):
        r.status = "fail"
        r.add(f"schema-home violation: {p} (machine schemas live at schemas/contracts/v1/focus_mode/)", str(p))
    return r


def check_c08_no_apps_web_references(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C08_no_apps_web_references_in_lane_files", status="pass")
    if not focus_modes_dir.is_dir():
        return r
    for md in focus_modes_dir.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for needle in FORBIDDEN_PATH_SUBSTRINGS:
            if needle in text:
                # Allow if explicitly inside a 'do NOT use' or 'drift' annotation block — too brittle
                # to detect reliably; instead emit a warn and let humans inspect.
                r.status = "warn" if r.status == "pass" else r.status
                r.add(f"{md}: contains {needle!r} (drift per OPEN-DR-06; verify it's not an authoritative reference)", str(md))
    return r


def check_c09_lane_naming(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C09_lane_naming_kebab_plus_scope", status="pass")
    if not focus_modes_dir.is_dir():
        return r
    for child in sorted(focus_modes_dir.iterdir()):
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        if not LANE_NAME_RE.match(child.name):
            r.status = "fail"
            r.add(f"Lane folder {child.name!r} does not match kebab-case + scope suffix pattern (expected <slug>-{{county|region|corridor}})", child.name)
    return r


def check_c10_no_duplicate_county_claims(focus_modes_dir: Path) -> CheckResult:
    """
    Detect a county claimed by two different area lanes by examining each
    build-plan.md's front-matter `area.county` (best-effort scalar extraction).
    """
    r = CheckResult(name="C10_no_duplicate_county_claims", status="pass")
    seen: Dict[str, str] = {}  # county_lower -> lane
    if not focus_modes_dir.is_dir():
        return r
    for child in sorted(focus_modes_dir.iterdir()):
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        bp = child / "build-plan.md"
        if not bp.exists():
            continue
        text = bp.read_text(encoding="utf-8")
        # Best-effort: find `county: "<Name>"` line under area:
        m = re.search(r"^\s+county:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text, re.MULTILINE)
        if not m:
            continue
        county = m.group(1).strip().lower()
        if county in seen and seen[county] != child.name:
            r.status = "fail"
            r.add(f"County {county!r} claimed by both {seen[county]!r} and {child.name!r}", child.name)
        else:
            seen[county] = child.name
    return r


def check_c11_acceptance_items(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C11_acceptance_checklist_has_eight_items", status="pass")
    if not focus_modes_dir.is_dir():
        return r
    for child in sorted(focus_modes_dir.iterdir()):
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        ac = child / "acceptance-checklist.md"
        if not ac.exists():
            continue
        text = ac.read_text(encoding="utf-8")
        missing = [item for item in ACCEPTANCE_ITEMS if item not in text]
        if missing:
            r.status = "fail"
            r.add(f"{ac}: acceptance-checklist.md missing items {missing}", child.name)
    return r


def check_c12_links(focus_modes_dir: Path) -> CheckResult:
    r = CheckResult(name="C12_internal_markdown_links_resolve", status="pass")
    if not focus_modes_dir.is_dir():
        return r
    for md in focus_modes_dir.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for tgt in find_markdown_links(text):
            # Strip anchors; resolve relative
            path_part = tgt.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                r.status = "warn" if r.status == "pass" else r.status
                r.add(f"{md}: broken relative link target {tgt!r} (resolved to {resolved})", str(md))
    return r


# ----------------------------------------------------------------------
# Orchestration
# ----------------------------------------------------------------------

def run_all(focus_modes_dir: Path) -> ValidationReport:
    index_md = focus_modes_dir / "COUNTY_INDEX.md"
    rows, parse_errors = parse_index_table(index_md)

    checks: List[CheckResult] = []
    checks.append(check_c01_index_parses_and_counties(rows, parse_errors))
    checks.append(check_c02_statuses_in_enum(rows))
    checks.append(check_c03_lane_folders_exist(rows, focus_modes_dir))
    checks.append(check_c04_required_lane_files(focus_modes_dir))
    checks.append(check_c05_frontmatter_keys(focus_modes_dir))
    checks.append(check_c06_ui_shell_is_explorer_web(focus_modes_dir))
    checks.append(check_c07_no_schema_json_under_docs(focus_modes_dir))
    checks.append(check_c08_no_apps_web_references(focus_modes_dir))
    checks.append(check_c09_lane_naming(focus_modes_dir))
    checks.append(check_c10_no_duplicate_county_claims(focus_modes_dir))
    checks.append(check_c11_acceptance_items(focus_modes_dir))
    checks.append(check_c12_links(focus_modes_dir))

    has_fail = any(c.status == "fail" for c in checks)
    has_warn = any(c.status == "warn" for c in checks)
    overall = "fail" if has_fail else ("warn" if has_warn else "pass")

    return ValidationReport(
        schema_version="1",
        focus_modes_dir=str(focus_modes_dir),
        checks=checks,
        overall_status=overall,
    )


def print_human(report: ValidationReport) -> None:
    print(f"validate_focus_mode_index v{report.schema_version}")
    print(f"focus_modes_dir: {report.focus_modes_dir}")
    print(f"overall_status:  {report.overall_status}")
    print()
    for c in report.checks:
        flag = {"pass": "PASS", "fail": "FAIL", "warn": "WARN", "skip": "SKIP"}[c.status]
        print(f"  [{flag}] {c.name}")
        for d in c.details:
            print(f"         - {d}")
    print()


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("focus_modes_dir", type=Path, help="Path to docs/focus-modes/")
    parser.add_argument("--emit-json", type=Path, default=None, help="Write report JSON to this path")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args(argv)

    if not args.focus_modes_dir.exists():
        print(f"error: focus_modes_dir does not exist: {args.focus_modes_dir}", file=sys.stderr)
        return 2

    try:
        report = run_all(args.focus_modes_dir)
    except Exception as exc:  # noqa: BLE001 -- surface as system error per exit-code contract
        print(f"system error: {exc}", file=sys.stderr)
        return 2

    print_human(report)

    if args.emit_json:
        args.emit_json.parent.mkdir(parents=True, exist_ok=True)
        args.emit_json.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")

    if report.overall_status == "fail":
        return 1
    if args.strict and report.overall_status == "warn":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
