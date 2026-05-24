#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_focus_mode_index.py — KFM Focus Mode lane validator (v3).

Implements docs/focus-mode/ORGANIZATION_RULES.md v0.2 §3 (categorization rules)
and §8 (categorizer contract). Replaces the pre-ADR-0029 v1 validator that
encoded the seven-file split, kebab-case area dirs, and plural `focus-modes/`
lane name.

Doctrine basis (CONFIRMED):
  - docs/doctrine/directory-rules.md v1.3 §6.7.2 (placement table; amended per ADR-0029)
  - docs/doctrine/directory-rules.md v1.3 §6.7.3 (casing convention; closes OPEN-DR-08)
  - docs/focus-mode/ORGANIZATION_RULES.md v0.2 §3 (categorization rules; this spec)
  - docs/focus-mode/README.md v0.5 §14 (13-domain coverage)
  - docs/adr/ADR-0029-focus-mode-lane-structure-canonized.md §3 + §6.3 (decisions + validator rules)
  - docs/adr/ADR-0028-state-scale-focus-mode-scope.md §3 (13-domain coverage rule)
  - kfm_repository_structure_guiding_document.md §8 (Focus Mode placement contract)

Checks performed:
  C01: Lane root has REQUIRED files (README.md, ORGANIZATION_RULES.md) per §3.1
  C02: Container subdirs (counties/, state/, regions/, corridors/) — if present, have
       REQUIRED files (README.md, <SCOPE>_INDEX.md) per §3.2
  C03: Each container's _template/ has the canonical consolidated template filename
       per §3.3
  C04: Per-area lanes (snake_case + _<scope> suffix) have REQUIRED files (README.md
       and <area>_<scope>_focus_mode_build_plan.md) per §3.4
  C05: Per-area build plan filename matches its parent directory name exactly
       (self-describing-filename principle per ADR-0029 §4.3)
  C06: In-lane domain folders have canonical names (the 13 from ADR-0028 §3)
       and each has a README.md per §3.5
  C07: No drift-out-of-lane files (.schema.json, .rego, .py, fixtures, source
       descriptors, release manifests anywhere under docs/focus-mode/) per §3.6
  C08: No `apps/web/src/focus-modes/` references in any lane file (preserved
       from v1 — OPEN-DR-06 drift)
  C09: counties/COUNTY_INDEX.md (if present) parses; table covers Kansas counties
       (preserved/adapted from v1 C01)
  C10: ui_shell front-matter value is "apps/explorer-web" in any build-plan files
       (preserved from v1 C06)
  C11: 13-domain coverage map in per-area build plans enumerates the 13 canonical
       keys exactly (per ADR-0028 §3)
  C12: Per-file disposition report (machine-readable; not pass/fail itself)

Exit codes:
  0 = all pass (no drift-out-of-lane or unknown dispositions)
  1 = at least one check failed
  2 = system error (paths missing, parse error)

Usage:
  python tools/validators/validate_focus_mode_index.py docs/focus-mode/
  python tools/validators/validate_focus_mode_index.py docs/focus-mode/ --emit-json out.json
  python tools/validators/validate_focus_mode_index.py docs/focus-mode/ --strict

Migration window (per ORGANIZATION_RULES.md v0.2 §6.3): for one minor version of
directory-rules.md after ADR-0029 acceptance, legacy filenames (kebab-case area
dirs, seven-file split, etc.) are tolerated as warnings; after the migration
window they become failures. The --strict flag treats warnings as failures
immediately.
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
# Doctrine constants (per ORGANIZATION_RULES.md v0.2 + ADR-0028 + ADR-0029)
# ----------------------------------------------------------------------

LANE_ROOT_REQUIRED: Set[str] = {"README.md", "ORGANIZATION_RULES.md"}

CANONICAL_CONTAINERS: Set[str] = {"counties", "state", "regions", "corridors"}
CONTAINER_REQUIRED_INDEX: Dict[str, str] = {
    "counties": "COUNTY_INDEX.md",
    "state": "STATE_INDEX.md",
    "regions": "REGION_INDEX.md",
    "corridors": "CORRIDOR_INDEX.md",
}
CONTAINER_TEMPLATE_FILE: Dict[str, str] = {
    "counties": "county_focus_mode_build_plan.md",
    "state": "state_focus_mode_build_plan.md",
    "regions": "region_focus_mode_build_plan.md",
    "corridors": "corridor_focus_mode_build_plan.md",
}
# Container → expected scope-suffix for area dirs inside it
CONTAINER_SCOPE: Dict[str, str] = {
    "counties": "county",
    "state": "state",
    "regions": "region",
    "corridors": "corridor",
}

# 13 canonical thematic domains per ADR-0028 §3 + README v0.5 §14.1
CANONICAL_DOMAINS: Tuple[str, ...] = (
    "agriculture", "archaeology", "atmosphere_air", "fauna", "flora",
    "geology", "habitat", "hazards", "hydrology", "people_dna_land",
    "roads_rail", "settlements_infrastructure", "soil",
)
CANONICAL_DOMAINS_SET: Set[str] = set(CANONICAL_DOMAINS)
assert len(CANONICAL_DOMAINS) == 13, "CANONICAL_DOMAINS must contain exactly 13 entries"

VALID_SCOPES: Tuple[str, ...] = ("county", "state", "region", "corridor")

# Per-area lane directory naming: snake_case + _<scope> suffix per ADR-0029 §3.3
AREA_LANE_RE = re.compile(r"^([a-z][a-z0-9_]*)_(county|state|region|corridor)$")

# Legacy patterns (migration window per ORGANIZATION_RULES.md v0.2 §6.3)
LEGACY_KEBAB_AREA_RE = re.compile(r"^([a-z][a-z0-9-]*)-(county|state|region|corridor)$")
LEGACY_SEVEN_FILE_SPLIT: Set[str] = {
    "build-plan.md", "layer-registry.md", "evidence-model.md",
    "acceptance-checklist.md", "source-seed-list.md", "public-safety-notes.md",
}
LEGACY_TEMPLATE_NAMES: Set[str] = {
    "county-build-plan.md", "state-build-plan.md",
    "region-build-plan.md", "corridor-build-plan.md",
}

# Drift-out-of-lane patterns (per ORGANIZATION_RULES.md v0.2 §3.6)
DRIFT_OUT_PATTERNS: List[Tuple[re.Pattern, str]] = [
    (re.compile(r".*\.schema\.json$"),
     "schemas live in schemas/contracts/v1/focus_mode/ per directory-rules.md §6.4 + ADR-0001"),
    (re.compile(r".*\.rego$"),
     "policies live in policy/ per directory-rules.md §6.5"),
    (re.compile(r".*\.py$"),
     "Python tools live in tools/ per directory-rules.md §6.6"),
    (re.compile(r".*/(valid|invalid)/.*\.json$"),
     "fixtures live in fixtures/focus_modes/<area>/{valid,invalid}/ per directory-rules.md §6.7.2"),
    (re.compile(r"^(.*/)?source[-_]descriptors\.ya?ml$"),
     "source descriptors live in data/catalog/sources/<area>/ per directory-rules.md §6.7.2"),
    (re.compile(r".*[Rr]elease.*[Mm]anifest.*\.json$"),
     "release manifests live in release/manifests/focus_modes/ per directory-rules.md §6.7.2"),
]
ROOT_LEVEL_DRIFT_OUT: Dict[str, str] = {
    "MIGRATION_NOTE.md": "belongs under migrations/<migration-id>/ per directory-rules.md §2.5",
    "CHANGELOG.md": "belongs under migrations/<migration-id>/ or at repo root",
}

# Forbidden substrings (preserved from v1 — OPEN-DR-06)
FORBIDDEN_PATH_SUBSTRINGS: Tuple[str, ...] = ("apps/web/src/focus-modes/",)

# Optional file patterns
OPTIONAL_NOTES_RE = re.compile(r"^.*-notes\.md$")

# 105 Kansas counties (preserved from v1 for C09)
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
assert len(KANSAS_COUNTIES) == 105

# ----------------------------------------------------------------------
# Disposition + signature vocabularies (per ORGANIZATION_RULES.md v0.2 §5)
# ----------------------------------------------------------------------

DISP_KEEP_ROOT = "keep-root"
DISP_KEEP_AREA = "keep-area"
DISP_KEEP_TEMPLATE = "keep-template"
DISP_OPTIONAL = "optional-keep"
DISP_DRIFT_WITHIN = "drift-within-lane"
DISP_DRIFT_OUT = "drift-out-of-lane"
DISP_UNKNOWN = "unknown"
ALL_DISPOSITIONS = (DISP_KEEP_ROOT, DISP_KEEP_AREA, DISP_KEEP_TEMPLATE,
                    DISP_OPTIONAL, DISP_DRIFT_WITHIN, DISP_DRIFT_OUT, DISP_UNKNOWN)
CLEAN_DISPOSITIONS = {DISP_KEEP_ROOT, DISP_KEEP_AREA, DISP_KEEP_TEMPLATE, DISP_OPTIONAL}
DIRTY_DISPOSITIONS = {DISP_DRIFT_WITHIN, DISP_DRIFT_OUT, DISP_UNKNOWN}

# ----------------------------------------------------------------------
# Data classes
# ----------------------------------------------------------------------

@dataclass
class FileClassification:
    path: str                            # path relative to lane root
    disposition: str
    signatures: List[str] = field(default_factory=list)
    rationale: str = ""

@dataclass
class CheckResult:
    name: str
    status: str                          # "pass" | "fail" | "warn" | "skip"
    details: List[str] = field(default_factory=list)
    affected: List[str] = field(default_factory=list)

    def add(self, msg: str, item: Optional[str] = None) -> None:
        self.details.append(msg)
        if item:
            self.affected.append(item)

@dataclass
class ValidationReport:
    schema_version: str
    lane_root: str
    file_count: int
    classifications: List[FileClassification]
    checks: List[CheckResult]
    overall_status: str                  # "pass" | "warn" | "fail" | "error"

    def to_dict(self) -> Dict:
        return {
            "schema_version": self.schema_version,
            "lane_root": self.lane_root,
            "file_count": self.file_count,
            "overall_status": self.overall_status,
            "classifications": [asdict(c) for c in self.classifications],
            "checks": [asdict(c) for c in self.checks],
        }

# ----------------------------------------------------------------------
# Classifier — applies ORGANIZATION_RULES.md v0.2 §3 rules
# ----------------------------------------------------------------------

def classify(rel: Path) -> FileClassification:
    """Apply §3.1 → §3.6 rules in order; first match wins."""
    parts = rel.parts
    name = rel.name
    posix = rel.as_posix()

    # §3.6 catch-all drift-out patterns first (they apply at any depth)
    for pattern, reason in DRIFT_OUT_PATTERNS:
        if pattern.match(posix) or pattern.match(name):
            return FileClassification(path=posix, disposition=DISP_DRIFT_OUT,
                                      signatures=["drift-out"], rationale=reason)

    # §3.1 Lane-root files
    if len(parts) == 1:
        if name in LANE_ROOT_REQUIRED:
            return FileClassification(path=posix, disposition=DISP_KEEP_ROOT,
                rationale=f"canonical lane-root file per ORGANIZATION_RULES.md v0.2 §3.1")
        if name in ROOT_LEVEL_DRIFT_OUT:
            return FileClassification(path=posix, disposition=DISP_DRIFT_OUT,
                signatures=["drift-out"], rationale=ROOT_LEVEL_DRIFT_OUT[name])
        # Legacy: COUNTY_INDEX.md / STATE_INDEX.md at lane root (now container-scoped)
        if name in ("COUNTY_INDEX.md", "STATE_INDEX.md", "REGION_INDEX.md", "CORRIDOR_INDEX.md"):
            return FileClassification(path=posix, disposition=DISP_DRIFT_WITHIN,
                signatures=["legacy-lane-root-index"],
                rationale="container-scoped index per ADR-0029 §3.2; move to <container>/")
        return FileClassification(path=posix, disposition=DISP_UNKNOWN,
            signatures=["unknown"], rationale="loose file at lane root; not in canonical set")

    top = parts[0]

    # §3.5 In-lane domain folders
    if top in CANONICAL_DOMAINS_SET:
        if len(parts) == 2 and name == "README.md":
            return FileClassification(path=posix, disposition=DISP_KEEP_AREA,
                rationale=f"required in-lane domain README for canonical domain `{top}` per ORGANIZATION_RULES.md v0.2 §3.5")
        if len(parts) == 2 and OPTIONAL_NOTES_RE.match(name):
            return FileClassification(path=posix, disposition=DISP_OPTIONAL,
                rationale=f"optional framing-notes file in `{top}` per ORGANIZATION_RULES.md v0.2 §3.5")
        if len(parts) > 2:
            return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                signatures=["unknown"],
                rationale=f"file in unexpected subdir of `{top}/`; in-lane domain folders are flat")
        return FileClassification(path=posix, disposition=DISP_UNKNOWN,
            signatures=["unknown"], rationale=f"unrecognized file in `{top}/`")

    # Non-canonical domain folder names (legacy drift)
    if top in {"atmosphere", "hydrogeology", "people", "settlements-infrastructure",
               "roads", "railroads"}:
        return FileClassification(path=posix, disposition=DISP_DRIFT_WITHIN,
            signatures=["#6-domain-name-mismatch"],
            rationale=f"non-canonical domain folder `{top}/`; rename per ADR-0029 §10.2 + Atlas Appendix C")

    # §3.2 / §3.3 / §3.4 Container subdirectories
    if top in CANONICAL_CONTAINERS:
        if len(parts) == 1:
            # The container dir itself — shouldn't classify as a "file"
            return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                signatures=["unknown"], rationale="unexpected: container path classified as file")

        # §3.2 Container-level files
        if len(parts) == 2:
            if name == "README.md":
                return FileClassification(path=posix, disposition=DISP_KEEP_AREA,
                    rationale=f"required container README per ORGANIZATION_RULES.md v0.2 §3.2")
            if name == CONTAINER_REQUIRED_INDEX.get(top):
                return FileClassification(path=posix, disposition=DISP_KEEP_AREA,
                    rationale=f"required container index per ORGANIZATION_RULES.md v0.2 §3.2")
            if top == "counties" and name == "domains.md":
                return FileClassification(path=posix, disposition=DISP_OPTIONAL,
                    rationale="optional cross-domain composition reference per ORGANIZATION_RULES.md v0.2 §3.2")
            if OPTIONAL_NOTES_RE.match(name):
                return FileClassification(path=posix, disposition=DISP_OPTIONAL,
                    rationale=f"optional framing-notes file in `{top}/` per ORGANIZATION_RULES.md v0.2 §3.2")
            return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                signatures=["unknown"], rationale=f"unexpected file directly under `{top}/`")

        # §3.3 Template files
        if parts[1] == "_template":
            canonical_tpl = CONTAINER_TEMPLATE_FILE.get(top)
            if len(parts) == 3 and name == canonical_tpl:
                return FileClassification(path=posix, disposition=DISP_KEEP_TEMPLATE,
                    rationale=f"canonical consolidated template per ADR-0029 §3.4")
            if len(parts) == 3 and name in LEGACY_TEMPLATE_NAMES:
                return FileClassification(path=posix, disposition=DISP_DRIFT_WITHIN,
                    signatures=["legacy-template-kebab"],
                    rationale=f"legacy kebab template; rename to {canonical_tpl} per ADR-0029 §3.4")
            if len(parts) == 3 and name == "README.md":
                return FileClassification(path=posix, disposition=DISP_OPTIONAL,
                    rationale="optional template-overview README per ORGANIZATION_RULES.md v0.2 §3.3")
            if len(parts) > 3:
                return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                    signatures=["unknown"], rationale="templates are flat; no nested subdirs allowed")
            return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                signatures=["unknown"], rationale=f"unexpected file in `{top}/_template/`")

        # §3.4 Per-area lane files
        area_dir = parts[1]
        m = AREA_LANE_RE.match(area_dir)
        if m:
            expected_scope = CONTAINER_SCOPE[top]
            actual_scope = m.group(2)
            if actual_scope != expected_scope:
                return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                    signatures=["scope-container-mismatch"],
                    rationale=f"area dir `{area_dir}` has scope `{actual_scope}` but lives in container `{top}/` (expects `{expected_scope}`)")

            if len(parts) == 3 and name == "README.md":
                return FileClassification(path=posix, disposition=DISP_KEEP_AREA,
                    rationale=f"required per-area README per ORGANIZATION_RULES.md v0.2 §3.4")
            if len(parts) == 3 and name == f"{area_dir}_focus_mode_build_plan.md":
                return FileClassification(path=posix, disposition=DISP_KEEP_AREA,
                    rationale=f"required per-area consolidated build plan per ADR-0029 §3.4")
            if len(parts) == 3 and OPTIONAL_NOTES_RE.match(name):
                return FileClassification(path=posix, disposition=DISP_OPTIONAL,
                    rationale=f"optional framing-notes file per ORGANIZATION_RULES.md v0.2 §3.4")
            if len(parts) == 3 and name in LEGACY_SEVEN_FILE_SPLIT:
                return FileClassification(path=posix, disposition=DISP_DRIFT_WITHIN,
                    signatures=["legacy-seven-file-split"],
                    rationale=f"legacy seven-file split; consolidate into {area_dir}_focus_mode_build_plan.md per ADR-0029 §3.4")
            if len(parts) > 3:
                return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                    signatures=["unknown"], rationale="per-area lanes are flat; no nested subdirs allowed")
            return FileClassification(path=posix, disposition=DISP_UNKNOWN,
                signatures=["unknown"], rationale=f"unrecognized file in per-area lane `{area_dir}/`")

        # Legacy kebab-case area dirs
        m2 = LEGACY_KEBAB_AREA_RE.match(area_dir)
        if m2:
            return FileClassification(path=posix, disposition=DISP_DRIFT_WITHIN,
                signatures=["#5-kebab-area-dir"],
                rationale=f"legacy kebab-case area dir `{area_dir}/`; rename to snake_case per ADR-0029 §3.3")

        return FileClassification(path=posix, disposition=DISP_UNKNOWN,
            signatures=["unknown"], rationale=f"non-canonical subdir under `{top}/`: `{area_dir}/`")

    return FileClassification(path=posix, disposition=DISP_UNKNOWN,
        signatures=["unknown"],
        rationale=f"file under non-canonical lane-root subdir `{top}/`")

# ----------------------------------------------------------------------
# Walk + check pipeline
# ----------------------------------------------------------------------

def walk_lane(lane_root: Path) -> List[FileClassification]:
    out: List[FileClassification] = []
    for p in sorted(lane_root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(lane_root)
        if any(part.startswith(".") for part in rel.parts):
            continue
        out.append(classify(rel))
    return out

def check_c01_lane_root_required(lane_root: Path) -> CheckResult:
    """C01: Lane root has REQUIRED files per §3.1."""
    chk = CheckResult(name="C01 lane-root REQUIRED files", status="pass")
    present = {p.name for p in lane_root.iterdir() if p.is_file()}
    for req in LANE_ROOT_REQUIRED:
        if req not in present:
            chk.status = "fail"
            chk.add(f"missing REQUIRED lane-root file: {req}", item=req)
    return chk

def check_c02_container_required(lane_root: Path) -> CheckResult:
    """C02: Containers (if present) have REQUIRED README + <SCOPE>_INDEX.md per §3.2."""
    chk = CheckResult(name="C02 container REQUIRED files", status="pass")
    for container in sorted(CANONICAL_CONTAINERS):
        cdir = lane_root / container
        if not cdir.is_dir():
            continue
        present = {p.name for p in cdir.iterdir() if p.is_file()}
        for req in ("README.md", CONTAINER_REQUIRED_INDEX[container]):
            if req not in present:
                chk.status = "fail"
                chk.add(f"missing REQUIRED file in {container}/: {req}", item=f"{container}/{req}")
    if not chk.details:
        chk.add("all present-container REQUIRED files found")
    return chk

def check_c03_templates(lane_root: Path) -> CheckResult:
    """C03: Each container's _template/ has canonical template filename per §3.3."""
    chk = CheckResult(name="C03 canonical template filenames", status="pass")
    found_any = False
    for container, tpl in CONTAINER_TEMPLATE_FILE.items():
        tdir = lane_root / container / "_template"
        if not tdir.is_dir():
            continue
        found_any = True
        if not (tdir / tpl).exists():
            chk.status = "warn"
            chk.add(f"missing canonical template {container}/_template/{tpl}", item=str(tdir / tpl))
        for f in tdir.iterdir():
            if f.is_file() and f.name in LEGACY_TEMPLATE_NAMES:
                chk.status = "warn"
                chk.add(f"legacy template present: {container}/_template/{f.name} — rename to {tpl}",
                        item=str(f))
    if not found_any:
        chk.status = "skip"
        chk.add("no container _template/ directories present")
    return chk

def check_c04_per_area_required(lane_root: Path, classifications: List[FileClassification]) -> CheckResult:
    """C04: Per-area lanes have REQUIRED files (README.md + <area>_<scope>_focus_mode_build_plan.md) per §3.4."""
    chk = CheckResult(name="C04 per-area lane REQUIRED files", status="pass")
    area_dirs: Dict[str, Path] = {}
    for container in CANONICAL_CONTAINERS:
        cdir = lane_root / container
        if not cdir.is_dir():
            continue
        for sub in cdir.iterdir():
            if sub.is_dir() and AREA_LANE_RE.match(sub.name) and sub.name != "_template":
                area_dirs[f"{container}/{sub.name}"] = sub
    if not area_dirs:
        chk.status = "skip"
        chk.add("no per-area lanes found")
        return chk
    for label, adir in sorted(area_dirs.items()):
        area_name = adir.name
        files = {p.name for p in adir.iterdir() if p.is_file()}
        if "README.md" not in files:
            chk.status = "fail"
            chk.add(f"missing README.md in {label}/", item=label)
        expected_bp = f"{area_name}_focus_mode_build_plan.md"
        if expected_bp not in files:
            chk.status = "fail"
            chk.add(f"missing build plan in {label}/: {expected_bp}", item=label)
    return chk

def check_c05_build_plan_filename_matches_dir(lane_root: Path) -> CheckResult:
    """C05: Build plan filename matches parent directory name (ADR-0029 §4.3)."""
    chk = CheckResult(name="C05 self-describing build-plan filename", status="pass")
    found_any = False
    for container in CANONICAL_CONTAINERS:
        cdir = lane_root / container
        if not cdir.is_dir():
            continue
        for sub in cdir.iterdir():
            if not (sub.is_dir() and AREA_LANE_RE.match(sub.name) and sub.name != "_template"):
                continue
            found_any = True
            expected = f"{sub.name}_focus_mode_build_plan.md"
            for f in sub.iterdir():
                if not f.is_file():
                    continue
                if f.name.endswith("_focus_mode_build_plan.md") and f.name != expected:
                    chk.status = "fail"
                    chk.add(f"build-plan filename mismatch: {container}/{sub.name}/{f.name} — expected {expected}",
                            item=f"{container}/{sub.name}/{f.name}")
    if not found_any:
        chk.status = "skip"
    return chk

def check_c06_canonical_domain_folders(lane_root: Path) -> CheckResult:
    """C06: 13 canonical domain folders present with READMEs (§3.5 + ADR-0028 §3)."""
    chk = CheckResult(name="C06 13 canonical in-lane domain folders", status="pass")
    missing = []
    no_readme = []
    for d in CANONICAL_DOMAINS:
        dpath = lane_root / d
        if not dpath.is_dir():
            missing.append(d)
            continue
        if not (dpath / "README.md").is_file():
            no_readme.append(d)
    if missing:
        chk.status = "fail"
        chk.add(f"missing canonical domain folder(s): {', '.join(missing)}", item=",".join(missing))
    if no_readme:
        chk.status = "fail"
        chk.add(f"domain folder(s) without README.md: {', '.join(no_readme)}", item=",".join(no_readme))
    if not (missing or no_readme):
        chk.add(f"all 13 canonical domain folders present with READMEs")
    # Non-canonical domain folders (drift)
    non_canon = []
    for sub in lane_root.iterdir():
        if not sub.is_dir():
            continue
        if sub.name in CANONICAL_CONTAINERS or sub.name in CANONICAL_DOMAINS_SET:
            continue
        non_canon.append(sub.name)
    if non_canon:
        if chk.status == "pass":
            chk.status = "warn"
        chk.add(f"non-canonical lane-root subdir(s) present (drift): {', '.join(sorted(non_canon))}")
    return chk

def check_c07_drift_out(classifications: List[FileClassification]) -> CheckResult:
    """C07: No drift-out-of-lane files (§3.6)."""
    chk = CheckResult(name="C07 no drift-out-of-lane files", status="pass")
    drifted = [c for c in classifications if c.disposition == DISP_DRIFT_OUT]
    if drifted:
        chk.status = "fail"
        for c in drifted[:20]:
            chk.add(f"{c.path} — {c.rationale}", item=c.path)
        if len(drifted) > 20:
            chk.add(f"(+{len(drifted)-20} more)")
    return chk

def check_c08_no_apps_web(lane_root: Path) -> CheckResult:
    """C08: No bare `apps/web/src/focus-modes/` references in any lane file (OPEN-DR-06).

    Skips occurrences inside backtick-delimited inline code or fenced code blocks
    — those are documentation of the forbidden pattern, not uses of it.
    """
    chk = CheckResult(name="C08 no apps/web/ references (OPEN-DR-06)", status="pass")
    for p in lane_root.rglob("*.md"):
        if any(part.startswith(".") for part in p.relative_to(lane_root).parts):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        # Strip fenced code blocks and inline code spans, then check
        stripped = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        stripped = re.sub(r"`[^`\n]*`", "", stripped)
        for forbidden in FORBIDDEN_PATH_SUBSTRINGS:
            if forbidden in stripped:
                chk.status = "fail"
                # Count bare occurrences for the report
                bare_count = stripped.count(forbidden)
                chk.add(f"forbidden path substring `{forbidden}` ({bare_count} bare occurrence{'s' if bare_count != 1 else ''}) in {p.relative_to(lane_root)}",
                        item=str(p.relative_to(lane_root)))
    return chk

def check_c09_county_index_coverage(lane_root: Path) -> CheckResult:
    """C09: counties/COUNTY_INDEX.md (if present) covers Kansas counties (preserved from v1 C01)."""
    chk = CheckResult(name="C09 COUNTY_INDEX.md county coverage", status="pass")
    idx = lane_root / "counties" / "COUNTY_INDEX.md"
    if not idx.is_file():
        chk.status = "skip"
        chk.add("counties/COUNTY_INDEX.md not present")
        return chk
    try:
        text = idx.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        chk.status = "fail"
        chk.add(f"could not read {idx} as UTF-8")
        return chk
    # Best-effort: count how many of the 105 county names appear as words
    found: Set[str] = set()
    for c in KANSAS_COUNTIES:
        if re.search(r"\b" + re.escape(c) + r"\b", text):
            found.add(c)
    missing = sorted(set(KANSAS_COUNTIES) - found)
    if missing:
        chk.status = "warn"
        chk.add(f"COUNTY_INDEX.md does not mention {len(missing)} of 105 counties: {missing[:5]}{'...' if len(missing) > 5 else ''}")
    else:
        chk.add(f"all 105 Kansas counties mentioned in COUNTY_INDEX.md")
    return chk

def check_c10_ui_shell(lane_root: Path) -> CheckResult:
    """C10: ui_shell front-matter value is apps/explorer-web (preserved from v1 C06)."""
    chk = CheckResult(name="C10 ui_shell is apps/explorer-web (OPEN-DR-06)", status="pass")
    ui_re = re.compile(r"^\s*ui_shell\s*:\s*(.+?)\s*(?:#.*)?$", re.MULTILINE)
    found_any = False
    for p in lane_root.rglob("*_focus_mode_build_plan.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for m in ui_re.finditer(text):
            found_any = True
            val = m.group(1).strip().strip('"').strip("'")
            if val != "apps/explorer-web":
                chk.status = "fail"
                chk.add(f"non-canonical ui_shell in {p.relative_to(lane_root)}: `{val}` (expected apps/explorer-web)",
                        item=str(p.relative_to(lane_root)))
    if not found_any:
        chk.status = "skip"
        chk.add("no build-plan files with ui_shell front-matter found")
    return chk

def check_c11_domain_coverage(lane_root: Path) -> CheckResult:
    """C11: build-plan domain_coverage map enumerates the 13 canonical keys (ADR-0028 §3)."""
    chk = CheckResult(name="C11 13-domain coverage in per-area build plans", status="pass")
    coverage_re = re.compile(r"^\s*domain_coverage\s*:\s*$", re.MULTILINE)
    found_any = False
    for p in lane_root.rglob("*_focus_mode_build_plan.md"):
        # Skip template files
        if "_template" in p.parts:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        m = coverage_re.search(text)
        if not m:
            continue
        found_any = True
        # Crude extraction: lines after `domain_coverage:` matching `  <key>: <value>`
        after = text[m.end():]
        block_lines = []
        for line in after.splitlines():
            if not line.startswith((" ", "\t")):
                break
            if re.match(r"^\s*#", line):
                continue
            block_lines.append(line)
            if len(block_lines) > 30:
                break
        keys = set()
        for line in block_lines:
            km = re.match(r"^\s+([a-z_]+)\s*:", line)
            if km:
                keys.add(km.group(1))
        missing = CANONICAL_DOMAINS_SET - keys
        extra = keys - CANONICAL_DOMAINS_SET
        if missing or extra:
            chk.status = "fail"
            msg = []
            if missing: msg.append(f"missing keys: {sorted(missing)}")
            if extra:   msg.append(f"extra keys: {sorted(extra)}")
            chk.add(f"{p.relative_to(lane_root)} — domain_coverage has {'; '.join(msg)}",
                    item=str(p.relative_to(lane_root)))
    if not found_any:
        chk.status = "skip"
        chk.add("no per-area build plans with domain_coverage block found")
    return chk

# ----------------------------------------------------------------------
# Orchestrator
# ----------------------------------------------------------------------

def run_all(lane_root: Path) -> ValidationReport:
    classifications = walk_lane(lane_root)
    checks: List[CheckResult] = [
        check_c01_lane_root_required(lane_root),
        check_c02_container_required(lane_root),
        check_c03_templates(lane_root),
        check_c04_per_area_required(lane_root, classifications),
        check_c05_build_plan_filename_matches_dir(lane_root),
        check_c06_canonical_domain_folders(lane_root),
        check_c07_drift_out(classifications),
        check_c08_no_apps_web(lane_root),
        check_c09_county_index_coverage(lane_root),
        check_c10_ui_shell(lane_root),
        check_c11_domain_coverage(lane_root),
    ]
    # Categorization-based pass/warn/fail
    unknowns = [c for c in classifications if c.disposition == DISP_UNKNOWN]
    drift_within = [c for c in classifications if c.disposition == DISP_DRIFT_WITHIN]
    c12 = CheckResult(name="C12 per-file categorization summary", status="pass")
    c12.add(f"{len(classifications)} files classified")
    by_disp: Dict[str, int] = {}
    for c in classifications:
        by_disp[c.disposition] = by_disp.get(c.disposition, 0) + 1
    for d in ALL_DISPOSITIONS:
        if by_disp.get(d, 0) > 0:
            c12.add(f"  {d}: {by_disp[d]}")
    if unknowns:
        c12.status = "fail"
        c12.add(f"{len(unknowns)} file(s) with `unknown` disposition — halt for human review")
    elif drift_within:
        c12.status = "warn"
        c12.add(f"{len(drift_within)} file(s) with `drift-within-lane` — migration-window warnings")
    checks.append(c12)

    has_fail = any(c.status == "fail" for c in checks)
    has_warn = any(c.status == "warn" for c in checks)
    overall = "fail" if has_fail else ("warn" if has_warn else "pass")

    return ValidationReport(
        schema_version="3",
        lane_root=str(lane_root),
        file_count=len(classifications),
        classifications=classifications,
        checks=checks,
        overall_status=overall,
    )

def print_human(report: ValidationReport) -> None:
    print(f"validate_focus_mode_index v{report.schema_version} (per ORGANIZATION_RULES.md v0.2 + ADR-0029)")
    print(f"lane_root:       {report.lane_root}")
    print(f"file_count:      {report.file_count}")
    print(f"overall_status:  {report.overall_status}")
    print()
    for c in report.checks:
        flag = {"pass": "PASS", "fail": "FAIL", "warn": "WARN", "skip": "SKIP"}[c.status]
        print(f"  [{flag}] {c.name}")
        for d in c.details[:8]:
            print(f"         - {d}")
        if len(c.details) > 8:
            print(f"         - (+{len(c.details)-8} more)")
    print()

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("lane_root", type=Path, help="Path to docs/focus-mode/")
    parser.add_argument("--emit-json", type=Path, default=None, help="Write report JSON to this path")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args(argv)

    if not args.lane_root.exists():
        print(f"error: lane_root does not exist: {args.lane_root}", file=sys.stderr)
        return 2
    if not args.lane_root.is_dir():
        print(f"error: lane_root is not a directory: {args.lane_root}", file=sys.stderr)
        return 2

    try:
        report = run_all(args.lane_root)
    except Exception as exc:
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
