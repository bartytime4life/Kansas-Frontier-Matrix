"""Validate a bounded inventory of existing KFM contract fixture families.

The manifest is test inventory only. A PASS proves declared schema/fixture
presence and valid/invalid JSON Schema polarity; it does not establish semantic
truth, policy approval, evidence closure, release, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry

TOOL = "validate-contract-fixture-manifest"
TOOL_VERSION = "1.0.0"
MANIFEST_KIND = "ContractFixtureManifest"
MANIFEST_VERSION = "1.0.0"
MAX_MANIFEST_BYTES = 1_000_000
MAX_CASE_BYTES = 2_000_000
MAX_DEPTH = 64
MAX_NODES = 100_000
MAX_FAMILIES = 100
MAX_CASES = 5_000
MAX_SCHEMA_FINDINGS = 100
MAX_REPORT_FINDINGS = 200
SAFE_TOKEN = re.compile(r"^[a-z0-9][a-z0-9-]{2,63}$")
SCHEMA_PREFIX = ("schemas", "contracts", "v1")
FIXTURE_PREFIX = ("fixtures", "contracts", "v1")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    severity: str
    code: str
    family: str
    path: str


@dataclass(frozen=True, order=True)
class FamilySummary:
    family: str
    schema_path: str
    fixture_root: str
    valid_cases: int
    invalid_cases: int
    passed_cases: int


@dataclass(frozen=True)
class ValidationReport:
    manifest: str
    wave: str | None
    outcome: str
    families: tuple[FamilySummary, ...]
    findings: tuple[Finding, ...]

    @property
    def case_count(self) -> int:
        return sum(item.valid_cases + item.invalid_cases for item in self.families)

    @property
    def passed_case_count(self) -> int:
        return sum(item.passed_cases for item in self.families)

    @property
    def exit_code(self) -> int:
        return {"PASS": 0, "FAIL": 1, "ERROR": 2}[self.outcome]


def _reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _complexity(value: object, depth: int = 0) -> tuple[int, int]:
    if depth > MAX_DEPTH:
        return depth, MAX_NODES + 1
    if isinstance(value, Mapping):
        children = list(value.values())
    elif isinstance(value, list):
        children = value
    else:
        return depth, 1
    max_depth, nodes = depth, 1
    for child in children:
        child_depth, child_nodes = _complexity(child, depth + 1)
        max_depth = max(max_depth, child_depth)
        nodes += child_nodes
        if nodes > MAX_NODES:
            break
    return max_depth, nodes


def _has_symlink(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _read_json(path: Path, limit: int) -> tuple[dict[str, object] | None, str | None]:
    try:
        if _has_symlink(path) or not path.is_file():
            return None, "UNSAFE_FILE" if path.exists() else "FILE_MISSING"
        if path.stat().st_size > limit:
            return None, "FILE_TOO_LARGE"
        data = path.read_bytes()
        if len(data) > limit:
            return None, "FILE_TOO_LARGE"
        value = json.loads(
            data.decode("utf-8"),
            object_pairs_hook=_reject_duplicates,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, "DUPLICATE_KEY"
    except NonFiniteNumberError:
        return None, "NONFINITE_NUMBER"
    except (UnicodeError, json.JSONDecodeError):
        return None, "INVALID_JSON"
    except (OSError, RecursionError, ValueError):
        return None, "READ_ERROR"
    depth, nodes = _complexity(value)
    if depth > MAX_DEPTH or nodes > MAX_NODES:
        return None, "JSON_COMPLEXITY_LIMIT"
    if not isinstance(value, dict):
        return None, "ROOT_TYPE"
    return value, None


def _relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except (OSError, ValueError):
        return path.as_posix()


def _manifest_path(path: Path, repo_root: Path) -> Path | None:
    candidate = path if path.is_absolute() else repo_root / path
    try:
        root = repo_root.resolve(strict=True)
        resolved = candidate.resolve(strict=False)
        resolved.relative_to(root)
        return resolved
    except (OSError, ValueError):
        return None


def _declared_path(
    raw: object,
    repo_root: Path,
    prefix: tuple[str, ...],
    *,
    suffix: str | None = None,
) -> Path | None:
    if not isinstance(raw, str) or not raw or "\\" in raw or raw.startswith("/"):
        return None
    pure = PurePosixPath(raw)
    if str(pure) != raw or any(part in {".", ".."} for part in pure.parts):
        return None
    if tuple(pure.parts[: len(prefix)]) != prefix:
        return None
    if suffix and not raw.endswith(suffix):
        return None
    candidate = repo_root.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(repo_root.resolve(strict=True))
    except (OSError, ValueError):
        return None
    return None if _has_symlink(candidate) else candidate


def _add(
    findings: list[Finding],
    severity: str,
    code: str,
    path: str,
    family: str = "",
) -> None:
    findings.append(Finding(severity, code, family, path))


def _manifest_records(
    manifest: Mapping[str, object],
    repo_root: Path,
) -> tuple[list[tuple[str, str, str, Path, Path]], list[Finding]]:
    findings: list[Finding] = []
    records: list[tuple[str, str, str, Path, Path]] = []
    required = {"kind", "manifest_version", "wave", "description", "families"}

    for key in sorted(required - set(manifest)):
        _add(findings, "ERROR", "MANIFEST_FIELD_MISSING", f"/{key}")
    for key in sorted(set(manifest) - required):
        _add(findings, "ERROR", "MANIFEST_FIELD_UNDECLARED", f"/{key}")
    if manifest.get("kind") != MANIFEST_KIND:
        _add(findings, "ERROR", "MANIFEST_KIND_INVALID", "/kind")
    if manifest.get("manifest_version") != MANIFEST_VERSION:
        _add(findings, "ERROR", "MANIFEST_VERSION_INVALID", "/manifest_version")

    wave = manifest.get("wave")
    if not isinstance(wave, str) or SAFE_TOKEN.fullmatch(wave) is None:
        _add(findings, "ERROR", "MANIFEST_WAVE_INVALID", "/wave")
    description = manifest.get("description")
    if not isinstance(description, str) or not 1 <= len(description) <= 500:
        _add(findings, "ERROR", "MANIFEST_DESCRIPTION_INVALID", "/description")

    families = manifest.get("families")
    if not isinstance(families, list):
        _add(findings, "ERROR", "MANIFEST_FAMILIES_INVALID", "/families")
        return records, findings
    if not families:
        _add(findings, "ERROR", "MANIFEST_FAMILIES_EMPTY", "/families")
        return records, findings
    if len(families) > MAX_FAMILIES:
        _add(findings, "ERROR", "MANIFEST_FAMILIES_LIMIT", "/families")
        return records, findings

    seen_names: set[str] = set()
    seen_schemas: set[str] = set()
    seen_roots: set[str] = set()
    names: list[str] = []
    family_keys = {"family", "schema_path", "fixture_root"}

    for index, raw in enumerate(families):
        base = f"/families/{index}"
        if not isinstance(raw, dict):
            _add(findings, "ERROR", "FAMILY_ROOT_TYPE", base)
            continue
        for key in sorted(family_keys - set(raw)):
            _add(findings, "ERROR", "FAMILY_FIELD_MISSING", f"{base}/{key}")
        for key in sorted(set(raw) - family_keys):
            _add(findings, "ERROR", "FAMILY_FIELD_UNDECLARED", f"{base}/{key}")

        name = raw.get("family")
        family = name if isinstance(name, str) else ""
        if not family or SAFE_TOKEN.fullmatch(family) is None:
            _add(findings, "ERROR", "FAMILY_NAME_INVALID", f"{base}/family", family)
            continue
        names.append(family)
        if family in seen_names:
            _add(findings, "ERROR", "FAMILY_DUPLICATE", f"{base}/family", family)
            continue
        seen_names.add(family)

        schema_raw = raw.get("schema_path")
        fixture_raw = raw.get("fixture_root")
        schema = _declared_path(
            schema_raw, repo_root, SCHEMA_PREFIX, suffix=".schema.json"
        )
        fixture = _declared_path(fixture_raw, repo_root, FIXTURE_PREFIX)
        if schema is None:
            _add(findings, "ERROR", "SCHEMA_PATH_INVALID", f"{base}/schema_path", family)
        if fixture is None:
            _add(findings, "ERROR", "FIXTURE_ROOT_INVALID", f"{base}/fixture_root", family)
        if schema is None or fixture is None:
            continue

        schema_text, fixture_text = str(schema_raw), str(fixture_raw)
        if schema_text in seen_schemas:
            _add(findings, "ERROR", "SCHEMA_PATH_DUPLICATE", f"{base}/schema_path", family)
            continue
        if fixture_text in seen_roots:
            _add(findings, "ERROR", "FIXTURE_ROOT_DUPLICATE", f"{base}/fixture_root", family)
            continue
        seen_schemas.add(schema_text)
        seen_roots.add(fixture_text)
        records.append((family, schema_text, fixture_text, schema, fixture))

    if names != sorted(names):
        _add(findings, "ERROR", "FAMILY_ORDER_INVALID", "/families")
    return records, findings


def _load_validator(
    schema_path: Path,
    repo_root: Path,
) -> tuple[Draft202012Validator | None, str | None]:
    schema, error = _read_json(schema_path, MAX_CASE_BYTES)
    if schema is None:
        return None, error
    try:
        Draft202012Validator.check_schema(schema)
        return (
            Draft202012Validator(
                schema,
                registry=build_registry(repo_root),
                format_checker=FormatChecker(),
            ),
            None,
        )
    except Exception:
        return None, "SCHEMA_LOAD_ERROR"


def _validate_family(
    family: str,
    schema_text: str,
    fixture_text: str,
    schema_path: Path,
    fixture_root: Path,
    repo_root: Path,
) -> tuple[FamilySummary, list[Finding]]:
    findings: list[Finding] = []
    if not schema_path.is_file():
        _add(findings, "ERROR", "SCHEMA_MISSING", schema_text, family)
        return FamilySummary(family, schema_text, fixture_text, 0, 0, 0), findings
    if not fixture_root.is_dir():
        _add(findings, "ERROR", "FIXTURE_ROOT_MISSING", fixture_text, family)
        return FamilySummary(family, schema_text, fixture_text, 0, 0, 0), findings

    validator, error = _load_validator(schema_path, repo_root)
    if validator is None:
        _add(findings, "ERROR", error or "SCHEMA_LOAD_ERROR", schema_text, family)
        return FamilySummary(family, schema_text, fixture_text, 0, 0, 0), findings

    valid_dir = fixture_root / "valid"
    invalid_dir = fixture_root / "invalid"
    valid_files = sorted(valid_dir.glob("valid_*.json"))
    invalid_files = sorted(invalid_dir.glob("invalid_*.json"))
    if not valid_files:
        _add(findings, "ERROR", "VALID_LANE_EMPTY", _relative(valid_dir, repo_root), family)
    if not invalid_files:
        _add(findings, "ERROR", "INVALID_LANE_EMPTY", _relative(invalid_dir, repo_root), family)
    if len(valid_files) + len(invalid_files) > MAX_CASES:
        _add(findings, "ERROR", "CASE_COUNT_LIMIT", fixture_text, family)
        return FamilySummary(
            family, schema_text, fixture_text, len(valid_files), len(invalid_files), 0
        ), findings

    passed = 0
    cases = [*((path, True) for path in valid_files), *((path, False) for path in invalid_files)]
    for path, expect_valid in cases:
        relative = _relative(path, repo_root)
        candidate, read_error = _read_json(path, MAX_CASE_BYTES)
        if candidate is None:
            _add(findings, "ERROR", f"CASE_{read_error or 'READ_ERROR'}", relative, family)
            continue
        try:
            errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
        except Exception:
            _add(findings, "ERROR", "SCHEMA_EVALUATION_ERROR", relative, family)
            continue
        if len(errors) > MAX_SCHEMA_FINDINGS:
            _add(findings, "ERROR", "SCHEMA_FINDINGS_LIMIT", relative, family)
            continue
        if expect_valid and errors:
            _add(findings, "FAIL", "VALID_CASE_REJECTED", relative, family)
        elif not expect_valid and not errors:
            _add(findings, "FAIL", "INVALID_CASE_ACCEPTED", relative, family)
        else:
            passed += 1

    return FamilySummary(
        family,
        schema_text,
        fixture_text,
        len(valid_files),
        len(invalid_files),
        passed,
    ), findings


def validate_manifest(
    manifest_path: Path,
    *,
    repo_root: Path = REPO_ROOT,
) -> ValidationReport:
    resolved = _manifest_path(manifest_path, repo_root)
    label = manifest_path.as_posix()
    if resolved is None:
        finding = Finding("ERROR", "MANIFEST_PATH_ESCAPE", "", label)
        return ValidationReport(label, None, "ERROR", (), (finding,))

    label = _relative(resolved, repo_root)
    manifest, error = _read_json(resolved, MAX_MANIFEST_BYTES)
    if manifest is None:
        finding = Finding("ERROR", f"MANIFEST_{error or 'READ_ERROR'}", "", label)
        return ValidationReport(label, None, "ERROR", (), (finding,))

    records, findings = _manifest_records(manifest, repo_root)
    summaries: list[FamilySummary] = []
    if not any(item.severity == "ERROR" for item in findings):
        for record in records:
            summary, family_findings = _validate_family(*record, repo_root)
            summaries.append(summary)
            findings.extend(family_findings)
            if len(findings) > MAX_REPORT_FINDINGS:
                findings = findings[:MAX_REPORT_FINDINGS]
                _add(findings, "ERROR", "REPORT_FINDINGS_TRUNCATED", "/")
                break

    final_findings = tuple(sorted(set(findings)))
    if any(item.severity == "ERROR" for item in final_findings):
        outcome = "ERROR"
    elif any(item.severity == "FAIL" for item in final_findings):
        outcome = "FAIL"
    else:
        outcome = "PASS"
    wave = manifest.get("wave")
    return ValidationReport(
        label,
        wave if isinstance(wave, str) else None,
        outcome,
        tuple(sorted(summaries)),
        final_findings,
    )


def _report_object(report: ValidationReport) -> dict[str, object]:
    return {
        "authority": "contract-fixture-inventory-and-schema-polarity-only",
        "families": [
            {
                "family": item.family,
                "fixture_root": item.fixture_root,
                "invalid_cases": item.invalid_cases,
                "passed_cases": item.passed_cases,
                "schema_path": item.schema_path,
                "valid_cases": item.valid_cases,
            }
            for item in report.families
        ],
        "findings": [
            {
                "code": item.code,
                "family": item.family or None,
                "path": item.path,
                "severity": item.severity,
            }
            for item in report.findings
        ],
        "manifest": report.manifest,
        "outcome": report.outcome,
        "summary": {
            "cases": report.case_count,
            "families": len(report.families),
            "findings": len(report.findings),
            "passed_cases": report.passed_case_count,
        },
        "tool": TOOL,
        "tool_version": TOOL_VERSION,
        "wave": report.wave,
    }


def serialize_json(report: ValidationReport) -> str:
    return json.dumps(_report_object(report), sort_keys=True, separators=(",", ":"))


def serialize_text(report: ValidationReport) -> str:
    lines = [
        "Contract fixture manifest validation",
        f"tool={TOOL} version={TOOL_VERSION}",
        f"manifest={report.manifest}",
        f"wave={report.wave or 'UNKNOWN'}",
        f"outcome={report.outcome}",
        (
            f"families={len(report.families)} cases={report.case_count} "
            f"passed_cases={report.passed_case_count} findings={len(report.findings)}"
        ),
    ]
    for item in report.families:
        lines.append(
            f"- family={item.family} valid={item.valid_cases} "
            f"invalid={item.invalid_cases} passed={item.passed_cases}"
        )
    for item in report.findings:
        lines.append(
            f"! severity={item.severity} code={item.code} "
            f"family={item.family or '-'} path={item.path}"
        )
    lines.append(
        "BOUNDARY: PASS proves only declared schema/fixture presence and expected JSON Schema polarity."
    )
    lines.append(
        "BOUNDARY: It does not prove semantic truth, policy approval, evidence closure, release, or publication."
    )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a bounded manifest of existing KFM contract fixture families."
    )
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args(argv)

    report = validate_manifest(args.manifest, repo_root=args.repo_root)
    print(serialize_text(report) if args.format == "text" else serialize_json(report))
    return report.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
