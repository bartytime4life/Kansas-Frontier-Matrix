#!/usr/bin/env python3
"""Validate inactive EO asset-prefilter reports without network access."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PROFILE_PATH = REPO_ROOT / "pipeline_specs/source/eo_asset_prefilter_profile.v1.json"
PROFILE_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/eo_asset_prefilter_profile.schema.json"
REPORT_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/eo_asset_prefilter_report.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/eo_asset_prefilter_report"
MAX_BYTES = 2 * 1024 * 1024
ZERO_SHA256 = "sha256:" + "0" * 64
SCOPE = "eo-asset-prefilter-report-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    decision: str | None

    @property
    def ok(self) -> bool:
        return not self.findings


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _constant(_value: str) -> None:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise NonFiniteNumberError
    return result


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_object,
            parse_constant=_constant,
            parse_float=_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("ROOT_NOT_OBJECT", "/")])


def _ptr(parts: Iterable[Any]) -> str:
    values = [str(v).replace("~", "~0").replace("/", "~1") for v in parts]
    return "/" + "/".join(values) if values else "/"


def _schema(value: Mapping[str, Any], path: Path, *, profile: bool = False) -> list[Finding]:
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
            key=lambda error: (_ptr(error.absolute_path), str(error.validator)),
        )[:100]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings: list[Finding] = []
    for error in errors:
        field = _ptr(error.absolute_path)
        if not profile and (
            field in {"/scope/query_ref", "/scope/geography_ref"}
            or field.endswith("/item_ref")
            or field.endswith("/asset_ref")
            or field.endswith("/evidence_ref")
        ):
            code = "LOCATOR_NOT_GOVERNED"
        elif field.startswith("/governance"):
            code = "GOVERNANCE_BOUNDARY_VIOLATION"
        else:
            code = "PROFILE_SCHEMA_INVALID" if profile else "SCHEMA_INVALID"
        findings.append(Finding(code, field))
    return findings


def _map(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _canonical(values: list[Any]) -> bool:
    return all(isinstance(value, str) for value in values) and values == sorted(set(values))


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _time(value: Any) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")) if isinstance(value, str) else None
    except ValueError:
        return None


def _replay(asset: Mapping[str, Any]) -> bool:
    return bool(asset.get("etag") and asset.get("etag_strength") == "strong") or bool(asset.get("last_modified"))


def _expected(candidate: Mapping[str, Any], profile: Mapping[str, Any]) -> dict[str, Any]:
    req = _map(profile.get("requirements"))
    items = [_map(v) for v in _list(candidate.get("items"))]
    assets = [_map(v) for item in items for v in _list(item.get("assets"))]
    missing = sum(asset.get("missing") is True for asset in assets)
    found = len(assets) - missing
    no_replay = sum(asset.get("missing") is not True and not _replay(asset) for asset in assets)
    min_valid = req.get("minimum_valid_pixel_fraction")
    max_cloud = req.get("maximum_cloud_cover_percent")
    min_per_item = req.get("minimum_assets_per_item")
    min_items = req.get("minimum_items_found")
    min_assets = req.get("minimum_assets_found")
    valid = sum(isinstance(item.get("valid_pixel_fraction"), (int, float)) and item["valid_pixel_fraction"] >= min_valid for item in items)
    cloud = sum(isinstance(item.get("cloud_cover_percent"), (int, float)) and item["cloud_cover_percent"] <= max_cloud for item in items)
    usable = 0
    for item in items:
        item_assets = [_map(v) for v in _list(item.get("assets"))]
        usable += int(
            item.get("valid_pixel_fraction", -1) >= min_valid
            and item.get("cloud_cover_percent", 101) <= max_cloud
            and len(item_assets) >= min_per_item
            and all(asset.get("missing") is False and _replay(asset) for asset in item_assets)
        )
    reasons: list[str] = []
    if not items:
        reasons.append("NO_ITEMS_FOUND")
    if missing:
        reasons.append("ASSET_MISSING")
    if reasons:
        decision = "DENY"
    else:
        if len(items) < min_items:
            reasons.append("INSUFFICIENT_ITEMS")
        if found < min_assets:
            reasons.append("INSUFFICIENT_ASSETS")
        if usable < min_items:
            reasons.append("INSUFFICIENT_USABLE_ITEMS")
        if no_replay:
            reasons.append("REPLAY_VALIDATOR_MISSING")
        decision = "HOLD" if reasons else "PASS"
        if not reasons:
            reasons = ["PREFILTER_REQUIREMENTS_MET"]
    return {
        "items_checked": len(items),
        "items_found": len(items),
        "assets_checked": len(assets),
        "assets_found": found,
        "items_meeting_valid_pixel_fraction": valid,
        "items_meeting_cloud_cover": cloud,
        "items_usable": usable,
        "assets_missing": missing,
        "assets_without_replay_validator": no_replay,
        "decision": decision,
        "reason_codes": sorted(reasons),
    }


def _profile_findings(profile: Mapping[str, Any]) -> list[Finding]:
    findings = _schema(profile, PROFILE_SCHEMA_PATH, profile=True)
    supplied = profile.get("spec_hash")
    if supplied == ZERO_SHA256:
        findings.append(Finding("DIGEST_PLACEHOLDER", "/profile/spec_hash"))
    elif isinstance(supplied, str) and supplied != canonical_spec_hash(profile):
        findings.append(Finding("PROFILE_HASH_MISMATCH", "/profile/spec_hash"))
    governance = _map(profile.get("governance"))
    if profile.get("status") != "PROPOSED_INACTIVE" or any(
        governance.get(key) is not False
        for key in ("source_activated", "network_performed", "policy_evaluated", "promotion_authorized", "public_use_allowed")
    ) or governance.get("release_ref") is not None:
        findings.append(Finding("PROFILE_GOVERNANCE_VIOLATION", "/profile/governance"))
    return findings


def _semantic(candidate: Mapping[str, Any], profile: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    supplied = candidate.get("spec_hash")
    if supplied == ZERO_SHA256:
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))
    elif isinstance(supplied, str) and supplied != canonical_spec_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    binding = _map(candidate.get("profile"))
    if (
        binding.get("profile_ref") != profile.get("profile_id")
        or binding.get("profile_version") != profile.get("profile_version")
        or binding.get("profile_spec_hash") != profile.get("spec_hash")
    ):
        findings.append(Finding("PROFILE_BINDING_MISMATCH", "/profile"))
    scope = _map(candidate.get("scope"))
    collections = _list(scope.get("collections"))
    if not _canonical(collections):
        findings.append(Finding("REFS_NOT_CANONICAL", "/scope/collections"))
    if scope.get("cloud_cover_lte_percent", 101) > _map(profile.get("requirements")).get("maximum_cloud_cover_percent", 100):
        findings.append(Finding("QUERY_THRESHOLD_WEAKER_THAN_PROFILE", "/scope/cloud_cover_lte_percent"))
    start, end = _time(_map(scope.get("datetime")).get("start")), _time(_map(scope.get("datetime")).get("end"))
    if start and end and start > end:
        findings.append(Finding("TIME_WINDOW_INVALID", "/scope/datetime"))
    items = [_map(v) for v in _list(candidate.get("items"))]
    if not _canonical([item.get("item_ref") for item in items]):
        findings.append(Finding("REFS_NOT_CANONICAL", "/items"))
    for i, item in enumerate(items):
        if item.get("collection") not in collections:
            findings.append(Finding("COLLECTION_OUT_OF_SCOPE", f"/items/{i}/collection"))
        observed = _time(item.get("observed_at"))
        if start and end and observed and not start <= observed <= end:
            findings.append(Finding("ITEM_OUTSIDE_WINDOW", f"/items/{i}/observed_at"))
        assets = [_map(v) for v in _list(item.get("assets"))]
        if item.get("asset_count") != len(assets):
            findings.append(Finding("ITEM_ASSET_COUNT_MISMATCH", f"/items/{i}/asset_count"))
        if not _canonical([asset.get("asset_ref") for asset in assets]):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/items/{i}/assets"))
        for j, asset in enumerate(assets):
            etag, strength = asset.get("etag"), asset.get("etag_strength")
            field = f"/items/{i}/assets/{j}/etag"
            if isinstance(etag, str) and (etag.startswith("W/") or '"' in etag or any(c.isspace() for c in etag)):
                findings.append(Finding("ETAG_NOT_NORMALIZED", field))
            if (strength in {"strong", "weak"} and not isinstance(etag, str)) or (strength == "missing" and etag is not None):
                findings.append(Finding("ETAG_STATE_INCONSISTENT", field))
            if asset.get("missing") is True and (asset.get("content_length") != 0 or etag is not None or asset.get("last_modified") is not None):
                findings.append(Finding("MISSING_ASSET_METADATA_INCONSISTENT", f"/items/{i}/assets/{j}"))
    governance = _map(candidate.get("governance"))
    if any(
        governance.get(key) is not False
        for key in ("source_activated", "network_performed", "raw_admitted", "evidence_resolved", "policy_evaluated", "promotion_authorized", "public_use_allowed")
    ) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    expected, actual = _expected(candidate, profile), _map(candidate.get("summary"))
    count_fields = tuple(expected)[:-2]
    if any(actual.get(field) != expected[field] for field in count_fields):
        findings.append(Finding("SUMMARY_COUNT_MISMATCH", "/summary"))
    if actual.get("decision") != expected["decision"] or actual.get("reason_codes") != expected["reason_codes"]:
        findings.append(Finding("DECISION_MISMATCH", "/summary"))
    if not _canonical(_list(actual.get("reason_codes"))):
        findings.append(Finding("REFS_NOT_CANONICAL", "/summary/reason_codes"))
    return findings


def validate_report(report_path: Path, profile_path: Path = PROFILE_PATH) -> ValidationResult:
    profile, findings = _read(profile_path)
    if profile is None:
        return ValidationResult(tuple(sorted(set(findings))), None)
    profile_findings = _profile_findings(profile)
    if profile_findings:
        return ValidationResult(tuple(sorted(set(profile_findings))), None)
    candidate, findings = _read(report_path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))), None)
    findings = _schema(candidate, REPORT_SCHEMA_PATH) + _semantic(candidate, profile)
    decision = _map(candidate.get("summary")).get("decision")
    return ValidationResult(tuple(sorted(set(findings))), decision if isinstance(decision, str) else None)


def _render(path: Path, result: ValidationResult) -> str:
    payload = {
        "decision": result.decision,
        "file": path.as_posix(),
        "findings": [{"code": item.code, "field": item.field} for item in result.findings],
        "outcome": "PASS" if result.ok else "FAIL",
        "scope": SCOPE,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def run_fixture_profile() -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    try:
        expected_valid = json.loads((FIXTURE_ROOT / "valid/expected_decisions_manifest.json").read_text())
        expected_invalid = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text())
    except (OSError, UnicodeError, json.JSONDecodeError):
        print("EO_PREFILTER_FIXTURES_ERROR manifests_unavailable")
        return 2
    passed = bool(valid and invalid)
    for path in valid:
        result = validate_report(path)
        print(_render(path, result))
        expected = expected_valid.get(path.name, {})
        candidate = json.loads(path.read_text())
        passed = passed and result.ok and result.decision == expected.get("decision") and candidate["summary"]["reason_codes"] == expected.get("reason_codes")
    for path in invalid:
        result = validate_report(path)
        print(_render(path, result))
        passed = passed and not result.ok and sorted({f.code for f in result.findings}) == sorted(expected_invalid.get(path.name, []))
    print("EO_PREFILTER_FIXTURES_VALID" if passed else "EO_PREFILTER_FIXTURES_INVALID", f"valid={len(valid)} invalid={len(invalid)} network=not_performed")
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate inactive synthetic EO asset prefilter reports.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_PATH)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files or args.profile != PROFILE_PATH:
            parser.error("--fixtures cannot be combined with files or --profile")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_report(path, args.profile)
        print(_render(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
