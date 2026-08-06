#!/usr/bin/env python3
"""Evaluate MapLibre GL JS v6 readiness without installing or running MapLibre.

The validator combines bounded repository inspection with an optional committed
probe-results record. It can prove dependency pinning, ESM/ES2022 posture,
import-boundary hygiene, absence of known internal API use, and whether the
required browser probes were recorded. It cannot prove rendering equivalence,
WebGL2 availability, CSP behavior, or query parity unless those external probes
have been executed and their finite results are supplied.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Mapping, Sequence

PROFILE = "kfm-maplibre-v6-readiness-v1"
PROBE_NAMES = (
    "webgl2_failure_handling",
    "worker_csp_loading",
    "style_spec_v25",
    "geojson_set_data",
    "query_rendered_features",
    "visual_pixel_diff",
)
SOURCE_SUFFIXES = frozenset({".js", ".jsx", ".mjs", ".ts", ".tsx"})
MAX_SOURCE_FILES = 1000
CASES_PATH = Path(__file__).resolve().parents[3] / "fixtures/maplibre/v6_readiness/cases.json"


class Outcome(StrEnum):
    READY = "READY"
    HOLD = "HOLD"
    ERROR = "ERROR"


@dataclass(frozen=True)
class ReadinessResult:
    outcome: Outcome
    reasons: tuple[str, ...]
    selected_version: str | None
    module_mode: str | None
    typescript_target: str | None
    probes: Mapping[str, str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "module_mode": self.module_mode,
            "outcome": self.outcome,
            "profile": PROFILE,
            "probes": dict(sorted(self.probes.items())),
            "reasons": list(self.reasons),
            "selected_version": self.selected_version,
            "typescript_target": self.typescript_target,
        }


def _load_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None, "FILE_NOT_FOUND"
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, "JSON_UNREADABLE"
    if not isinstance(value, dict):
        return None, "JSON_ROOT_NOT_OBJECT"
    return value, None


def _dependency_version(manifest: Mapping[str, Any]) -> str | None:
    values: list[str] = []
    for section in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        section_value = manifest.get(section)
        if isinstance(section_value, Mapping):
            value = section_value.get("maplibre-gl")
            if isinstance(value, str):
                values.append(value)
    if not values:
        return None
    if len(set(values)) != 1:
        return "CONFLICT"
    return values[0]


def _major(version: str) -> int | None:
    match = re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)", version)
    return int(match.group(1)) if match else None


def _source_files(root: Path) -> tuple[list[Path], bool]:
    files: list[Path] = []
    for base in (root / "apps/explorer-web/src", root / "packages/maplibre/src"):
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES:
                files.append(path)
                if len(files) > MAX_SOURCE_FILES:
                    return files[:MAX_SOURCE_FILES], True
    return files, False


def _scan_sources(root: Path) -> tuple[list[str], list[str], bool]:
    internal: list[str] = []
    boundary: list[str] = []
    files, truncated = _source_files(root)
    import_pattern = re.compile(r"(?:from\s+|import\s*\(|require\s*\()\s*['\"]maplibre-gl['\"]")
    internal_patterns = (
        re.compile(r"\bmap\s*\.\s*transform\b"),
        re.compile(r"\bmap\s*\[\s*['\"]transform['\"]\s*\]"),
        re.compile(r"\b_map\s*\.\s*transform\b"),
    )
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        rel = path.relative_to(root).as_posix()
        if any(pattern.search(text) for pattern in internal_patterns):
            internal.append(rel)
        if import_pattern.search(text) and not rel.startswith("packages/maplibre/"):
            boundary.append(rel)
    return sorted(set(internal)), sorted(set(boundary)), truncated


def _probe_results(root: Path) -> tuple[dict[str, str], str | None]:
    path = root / "configs/maplibre/v6-probe-results.json"
    value, error = _load_json(path)
    if error == "FILE_NOT_FOUND":
        return {name: "NOT_RUN" for name in PROBE_NAMES}, None
    if error or value is None:
        return {}, "PROBE_RESULTS_INVALID"
    if value.get("profile") != PROFILE:
        return {}, "PROBE_PROFILE_INVALID"
    probes = value.get("probes")
    if not isinstance(probes, Mapping):
        return {}, "PROBE_RESULTS_INVALID"
    result: dict[str, str] = {}
    for name in PROBE_NAMES:
        status = probes.get(name)
        if status not in {"PASS", "FAIL", "NOT_RUN"}:
            return {}, "PROBE_RESULTS_INVALID"
        result[name] = str(status)
    return result, None


def scan_repository(root: Path) -> ReadinessResult:
    reasons: list[str] = []
    root_manifest, root_error = _load_json(root / "package.json")
    explorer_manifest, explorer_error = _load_json(root / "apps/explorer-web/package.json")
    tsconfig, ts_error = _load_json(root / "apps/explorer-web/tsconfig.json")
    if root_error or explorer_error or ts_error or root_manifest is None or explorer_manifest is None or tsconfig is None:
        codes = [code for code in (root_error, explorer_error, ts_error) if code]
        return ReadinessResult(Outcome.ERROR, tuple(sorted(set(codes))), None, None, None, {})

    versions = [value for value in (_dependency_version(root_manifest), _dependency_version(explorer_manifest)) if value is not None]
    selected_version: str | None
    if not versions:
        selected_version = None
        reasons.append("MAPLIBRE_DEPENDENCY_UNPINNED")
    elif len(set(versions)) != 1 or "CONFLICT" in versions:
        selected_version = None
        reasons.append("MAPLIBRE_DEPENDENCY_CONFLICT")
    else:
        selected_version = versions[0]
        major = _major(selected_version)
        if major is None:
            reasons.append("MAPLIBRE_VERSION_NOT_EXACT")
        elif major < 6:
            reasons.append("MAPLIBRE_V6_NOT_SELECTED")
        elif major > 6:
            reasons.append("MAPLIBRE_MAJOR_UNREVIEWED")

    module_mode = explorer_manifest.get("type") if isinstance(explorer_manifest.get("type"), str) else None
    if module_mode != "module":
        reasons.append("ESM_MODE_REQUIRED")
    compiler = tsconfig.get("compilerOptions") if isinstance(tsconfig.get("compilerOptions"), Mapping) else {}
    target = compiler.get("target") if isinstance(compiler.get("target"), str) else None
    if target != "ES2022":
        reasons.append("ES2022_TARGET_REQUIRED")

    internal, boundary, truncated = _scan_sources(root)
    if internal:
        reasons.append("INTERNAL_TRANSFORM_ACCESS_PRESENT")
    if boundary:
        reasons.append("MAPLIBRE_IMPORT_BOUNDARY_VIOLATION")
    if truncated:
        reasons.append("SOURCE_SCAN_TRUNCATED")

    probes, probe_error = _probe_results(root)
    if probe_error:
        return ReadinessResult(Outcome.ERROR, (probe_error,), selected_version, module_mode, target, probes)
    failed = [name for name, status in probes.items() if status == "FAIL"]
    pending = [name for name, status in probes.items() if status == "NOT_RUN"]
    if failed:
        reasons.append("RUNTIME_PROBE_FAILED")
    if pending:
        reasons.append("RUNTIME_PROBES_PENDING")

    outcome = Outcome.READY if not reasons and _major(selected_version or "") == 6 else Outcome.HOLD
    return ReadinessResult(outcome, tuple(sorted(set(reasons))), selected_version, module_mode, target, probes)


def evaluate_manifest(value: Mapping[str, Any]) -> ReadinessResult:
    reasons: list[str] = []
    if value.get("profile") != PROFILE:
        return ReadinessResult(Outcome.ERROR, ("PROFILE_INVALID",), None, None, None, {})
    version = value.get("selected_version") if isinstance(value.get("selected_version"), str) else None
    module_mode = value.get("module_mode") if isinstance(value.get("module_mode"), str) else None
    target = value.get("typescript_target") if isinstance(value.get("typescript_target"), str) else None
    probes_value = value.get("probes")
    if not isinstance(probes_value, Mapping):
        return ReadinessResult(Outcome.ERROR, ("PROBES_INVALID",), version, module_mode, target, {})
    probes: dict[str, str] = {}
    for name in PROBE_NAMES:
        status = probes_value.get(name)
        if status not in {"PASS", "FAIL", "NOT_RUN"}:
            return ReadinessResult(Outcome.ERROR, ("PROBES_INVALID",), version, module_mode, target, {})
        probes[name] = str(status)
    if _major(version or "") != 6:
        reasons.append("MAPLIBRE_V6_EXACT_VERSION_REQUIRED")
    if module_mode != "module":
        reasons.append("ESM_MODE_REQUIRED")
    if target != "ES2022":
        reasons.append("ES2022_TARGET_REQUIRED")
    if value.get("internal_transform_access") is not False:
        reasons.append("INTERNAL_TRANSFORM_ACCESS_PRESENT")
    violations = value.get("direct_import_boundary_violations")
    if not isinstance(violations, list) or violations:
        reasons.append("MAPLIBRE_IMPORT_BOUNDARY_VIOLATION")
    if any(status == "FAIL" for status in probes.values()):
        reasons.append("RUNTIME_PROBE_FAILED")
    if any(status == "NOT_RUN" for status in probes.values()):
        reasons.append("RUNTIME_PROBES_PENDING")
    computed = Outcome.READY if not reasons else Outcome.HOLD
    declared = value.get("outcome")
    if declared != computed:
        reasons.append("DECLARED_OUTCOME_MISMATCH")
        computed = Outcome.ERROR
    governance = value.get("governance")
    if not isinstance(governance, Mapping) or any(governance.get(key) is not False for key in ("authority_created", "upgrade_authorized", "release_authorized", "publication_authorized")):
        reasons.append("GOVERNANCE_BOUNDARY_VIOLATION")
        computed = Outcome.ERROR
    return ReadinessResult(computed, tuple(sorted(set(reasons))), version, module_mode, target, probes)


def validate_fixtures() -> int:
    try:
        value = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        print("ERROR: MapLibre case manifest unavailable")
        return 1
    if not isinstance(value, dict) or not isinstance(value.get("valid"), list) or not isinstance(value.get("invalid"), list):
        print("ERROR: MapLibre case manifest invalid")
        return 1
    valid_cases = value["valid"]
    invalid_cases = value["invalid"]
    if not valid_cases or not invalid_cases:
        print("ERROR: MapLibre case lanes must be non-empty")
        return 1
    failed = False
    for entry in valid_cases:
        candidate = entry.get("candidate") if isinstance(entry, Mapping) else None
        name = str(entry.get("name", "valid")) if isinstance(entry, Mapping) else "valid"
        result = ReadinessResult(Outcome.ERROR, ("ROOT_INVALID",), None, None, None, {}) if not isinstance(candidate, Mapping) else evaluate_manifest(candidate)
        print(json.dumps({"file": name, **result.to_dict()}, sort_keys=True, separators=(",", ":")))
        failed = failed or result.outcome == Outcome.ERROR
    for entry in invalid_cases:
        candidate = entry.get("candidate") if isinstance(entry, Mapping) else None
        name = str(entry.get("name", "invalid")) if isinstance(entry, Mapping) else "invalid"
        expected = sorted(str(code) for code in entry.get("expected", [])) if isinstance(entry, Mapping) else []
        result = ReadinessResult(Outcome.ERROR, ("ROOT_INVALID",), None, None, None, {}) if not isinstance(candidate, Mapping) else evaluate_manifest(candidate)
        print(json.dumps({"file": name, **result.to_dict()}, sort_keys=True, separators=(",", ":")))
        failed = failed or sorted(result.reasons) != expected
    return 1 if failed else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan-root", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    selected = sum(bool(item) for item in (args.scan_root, args.manifest, args.fixtures))
    if selected != 1:
        parser.error("select exactly one of --scan-root, --manifest, or --fixtures")
    if args.fixtures:
        return validate_fixtures()
    if args.scan_root:
        result = scan_repository(args.scan_root)
    else:
        assert args.manifest is not None
        value, error = _load_json(args.manifest)
        result = ReadinessResult(Outcome.ERROR, (error or "ROOT_INVALID",), None, None, None, {}) if value is None else evaluate_manifest(value)
    print(json.dumps(result.to_dict(), sort_keys=True, separators=(",", ":")))
    return 0 if result.outcome == Outcome.READY else (3 if result.outcome == Outcome.HOLD else 1)


if __name__ == "__main__":
    raise SystemExit(main())
