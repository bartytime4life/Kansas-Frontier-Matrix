#!/usr/bin/env python3
"""Compare two frozen synthetic EPA AQS site-metadata snapshots.

The result is a deterministic review signal only. A record missing from the
current snapshot is an absence requiring SourceRecordAbsenceAssessment; this
comparator never calls it a removal, clears state, deletes history, promotes,
releases, publishes, or provides air-quality guidance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

PROFILE_ID = "kfm.aqs-site-metadata.synthetic.v1"
REPORT_SCHEMA_VERSION = "1.1.0"
SOURCE_DESCRIPTOR_REF = "fixture://source/epa-aqs"
SOURCE_RECORD_ABSENCE_CONTRACT_REF = (
    "kfm:contract:source-record-absence-assessment:v1"
)
REPORT_SCHEMA = (
    Path(__file__).resolve().parents[3]
    / "schemas/contracts/v1/domains/atmosphere/"
    "aqs_site_metadata_delta_report.schema.json"
)
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_SITES = 500
LOCATION_SHIFT_THRESHOLD_M = 250.0

SITE_ID_RE = re.compile(r"20-[0-9]{3}-[0-9]{4}\Z")
CODE_RE = re.compile(r"[0-9A-Z_.-]{1,32}\Z")
PARAMETER_RE = re.compile(r"[0-9]{5}\Z")
UTC_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z")
TOP_FIELDS = frozenset(
    {"profile_id", "fixture_only", "source_descriptor_ref", "captured_at", "source_revision", "sites"}
)
SITE_FIELDS = frozenset(
    {"site_id", "site_name", "status", "latitude", "longitude", "parameter_code", "method_code", "method_name", "poc"}
)
STATUSES = frozenset({"ACTIVE", "INACTIVE", "RETIRED"})


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class LoadedSnapshot:
    candidate: dict[str, Any] | None
    findings: tuple[Finding, ...]


@dataclass(frozen=True)
class ComparisonResult:
    outcome: str
    reason_code: str
    report: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "NO_MATERIAL_CHANGE" and self.report is not None


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _canonical(value: object) -> bytes:
    return json.dumps(
        value, allow_nan=False, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def _sha256(value: object) -> str:
    return "sha256:" + hashlib.sha256(_canonical(value)).hexdigest()


def _utc(value: object) -> bool:
    if not isinstance(value, str) or UTC_RE.fullmatch(value) is None:
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    offset = parsed.utcoffset()
    return parsed.tzinfo is not None and offset is not None and offset.total_seconds() == 0


def _finite(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code, path))


def load_snapshot(path: Path) -> LoadedSnapshot:
    findings: set[Finding] = set()
    try:
        if path.is_symlink():
            return LoadedSnapshot(None, (Finding("INPUT_SYMLINK_DENIED", "/"),))
        if not path.is_file():
            return LoadedSnapshot(None, (Finding("INPUT_NOT_FILE", "/"),))
        if path.stat().st_size > MAX_JSON_BYTES:
            return LoadedSnapshot(None, (Finding("INPUT_TOO_LARGE", "/"),))
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
        )
    except UnicodeError:
        return LoadedSnapshot(None, (Finding("JSON_NOT_UTF8", "/"),))
    except DuplicateKeyError:
        return LoadedSnapshot(None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        return LoadedSnapshot(None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except json.JSONDecodeError:
        return LoadedSnapshot(None, (Finding("JSON_INVALID", "/"),))
    except OSError:
        return LoadedSnapshot(None, (Finding("INPUT_UNREADABLE", "/"),))
    except (RecursionError, ValueError):
        return LoadedSnapshot(None, (Finding("JSON_COMPLEXITY_LIMIT", "/"),))

    if not isinstance(value, dict):
        return LoadedSnapshot(None, (Finding("ROOT_NOT_OBJECT", "/"),))

    for field in sorted(set(value) - TOP_FIELDS):
        _add(findings, "TOP_LEVEL_FIELD_UNKNOWN", f"/{field}")
    for field in sorted(TOP_FIELDS - set(value)):
        _add(findings, "TOP_LEVEL_FIELD_MISSING", f"/{field}")
    if value.get("profile_id") != PROFILE_ID:
        _add(findings, "PROFILE_ID_INVALID", "/profile_id")
    if value.get("fixture_only") is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "/fixture_only")
    if value.get("source_descriptor_ref") != SOURCE_DESCRIPTOR_REF:
        _add(findings, "SOURCE_DESCRIPTOR_REF_INVALID", "/source_descriptor_ref")
    if not _utc(value.get("captured_at")):
        _add(findings, "CAPTURED_AT_INVALID", "/captured_at")
    if not _text(value.get("source_revision")):
        _add(findings, "SOURCE_REVISION_INVALID", "/source_revision")

    sites = value.get("sites")
    if not isinstance(sites, list) or not sites:
        _add(findings, "SITES_INVALID", "/sites")
        return LoadedSnapshot(None, tuple(sorted(findings)))
    if len(sites) > MAX_SITES:
        _add(findings, "SITE_COUNT_EXCEEDED", "/sites")

    seen: set[str] = set()
    for index, site in enumerate(sites):
        base = f"/sites/{index}"
        if not isinstance(site, dict):
            _add(findings, "SITE_NOT_OBJECT", base)
            continue
        for field in sorted(set(site) - SITE_FIELDS):
            _add(findings, "SITE_FIELD_UNKNOWN", f"{base}/{field}")
        for field in sorted(SITE_FIELDS - set(site)):
            _add(findings, "SITE_FIELD_MISSING", f"{base}/{field}")

        site_id = site.get("site_id")
        if not isinstance(site_id, str) or SITE_ID_RE.fullmatch(site_id) is None:
            _add(findings, "SITE_ID_INVALID", f"{base}/site_id")
        elif site_id in seen:
            _add(findings, "SITE_ID_DUPLICATE", f"{base}/site_id")
        else:
            seen.add(site_id)
        if not _text(site.get("site_name")):
            _add(findings, "SITE_NAME_INVALID", f"{base}/site_name")
        if site.get("status") not in STATUSES:
            _add(findings, "SITE_STATUS_INVALID", f"{base}/status")
        latitude, longitude = site.get("latitude"), site.get("longitude")
        if not _finite(latitude) or not -90 <= float(latitude) <= 90:
            _add(findings, "LATITUDE_INVALID", f"{base}/latitude")
        if not _finite(longitude) or not -180 <= float(longitude) <= 180:
            _add(findings, "LONGITUDE_INVALID", f"{base}/longitude")
        parameter = site.get("parameter_code")
        if not isinstance(parameter, str) or PARAMETER_RE.fullmatch(parameter) is None:
            _add(findings, "PARAMETER_CODE_INVALID", f"{base}/parameter_code")
        method_code = site.get("method_code")
        if not isinstance(method_code, str) or CODE_RE.fullmatch(method_code) is None:
            _add(findings, "METHOD_CODE_INVALID", f"{base}/method_code")
        if not _text(site.get("method_name")):
            _add(findings, "METHOD_NAME_INVALID", f"{base}/method_name")
        poc = site.get("poc")
        if not isinstance(poc, int) or isinstance(poc, bool) or not 1 <= poc <= 99:
            _add(findings, "POC_INVALID", f"{base}/poc")

    return LoadedSnapshot(None if findings else value, tuple(sorted(findings)))


def _sorted_sites(snapshot: Mapping[str, Any]) -> list[dict[str, Any]]:
    return sorted((dict(site) for site in snapshot["sites"]), key=lambda site: site["site_id"])


def snapshot_content_hash(snapshot: Mapping[str, Any]) -> str:
    return _sha256(
        {
            "profile_id": snapshot["profile_id"],
            "fixture_only": snapshot["fixture_only"],
            "source_descriptor_ref": snapshot["source_descriptor_ref"],
            "sites": _sorted_sites(snapshot),
        }
    )


def snapshot_retrieval_hash(snapshot: Mapping[str, Any]) -> str:
    payload = dict(snapshot)
    payload["sites"] = _sorted_sites(snapshot)
    return _sha256(payload)


def _distance_m(prior: Mapping[str, Any], current: Mapping[str, Any]) -> float:
    lat1, lon1 = math.radians(float(prior["latitude"])), math.radians(float(prior["longitude"]))
    lat2, lon2 = math.radians(float(current["latitude"])), math.radians(float(current["longitude"]))
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 6_371_008.8 * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))


def _change(
    site_id: str,
    change_type: str,
    impact: str,
    fields: Sequence[str],
    *,
    distance_m: float | None = None,
    absence: bool = False,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "site_id": site_id,
        "change_type": change_type,
        "impact": impact,
        "changed_fields": sorted(set(fields)),
    }
    if distance_m is not None:
        result["distance_m"] = round(distance_m, 3)
    if absence:
        result["absence_assessment_required"] = True
        result["absence_contract_ref"] = SOURCE_RECORD_ABSENCE_CONTRACT_REF
    return result


def classify_changes(prior: Mapping[str, Any], current: Mapping[str, Any]) -> list[dict[str, Any]]:
    old_by_id = {site["site_id"]: site for site in _sorted_sites(prior)}
    new_by_id = {site["site_id"]: site for site in _sorted_sites(current)}
    changes: list[dict[str, Any]] = []
    for site_id in sorted(set(old_by_id) | set(new_by_id)):
        old, new = old_by_id.get(site_id), new_by_id.get(site_id)
        if old is None:
            changes.append(_change(site_id, "SITE_ADDED", "MEDIUM", ["site"]))
            continue
        if new is None:
            changes.append(
                _change(
                    site_id,
                    "SITE_ABSENT_FROM_CURRENT_SNAPSHOT",
                    "HIGH",
                    ["site"],
                    absence=True,
                )
            )
            continue
        if old["status"] != new["status"]:
            changes.append(_change(site_id, "SITE_LIFECYCLE", "HIGH", ["status"]))
        distance = _distance_m(old, new)
        if distance > LOCATION_SHIFT_THRESHOLD_M:
            changes.append(
                _change(site_id, "LOCATION_SHIFT", "HIGH", ["latitude", "longitude"], distance_m=distance)
            )
        elif distance > 0:
            changes.append(
                _change(site_id, "LOCATION_CORRECTION", "LOW", ["latitude", "longitude"], distance_m=distance)
            )
        method_fields = [field for field in ("method_code", "method_name") if old[field] != new[field]]
        if method_fields:
            changes.append(_change(site_id, "METHOD_CHANGE", "HIGH", method_fields))
        if old["parameter_code"] != new["parameter_code"]:
            changes.append(_change(site_id, "PARAMETER_CHANGE", "HIGH", ["parameter_code"]))
        if old["poc"] != new["poc"]:
            changes.append(_change(site_id, "POC_REASSIGNMENT", "HIGH", ["poc"]))
        if old["site_name"] != new["site_name"]:
            changes.append(_change(site_id, "METADATA_CORRECTION", "LOW", ["site_name"]))
    return sorted(changes, key=lambda item: (item["site_id"], item["change_type"]))


def _summary(changes: Sequence[Mapping[str, Any]], prior_count: int, current_count: int) -> dict[str, Any]:
    by_type: dict[str, int] = {}
    by_impact = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for change in changes:
        change_type = str(change["change_type"])
        by_type[change_type] = by_type.get(change_type, 0) + 1
        by_impact[str(change["impact"])] += 1
    return {
        "sites_prior": prior_count,
        "sites_current": current_count,
        "changes_total": len(changes),
        "high_impact_changes": by_impact["HIGH"],
        "medium_impact_changes": by_impact["MEDIUM"],
        "low_impact_changes": by_impact["LOW"],
        "changes_by_type": dict(sorted(by_type.items())),
    }


def _report_schema_findings(report: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(REPORT_SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(report),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("REPORT_SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding(
            "REPORT_SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path) if error.absolute_path else "/",
        )
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (tuple(str(part) for part in item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("REPORT_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def compare_snapshots(prior: Mapping[str, Any], current: Mapping[str, Any]) -> ComparisonResult:
    prior_content = snapshot_content_hash(prior)
    current_content = snapshot_content_hash(current)
    changes = classify_changes(prior, current)
    if prior_content == current_content and changes:
        return ComparisonResult(
            "ERROR",
            "AQS_SITE_DELTA_INCONSISTENT",
            None,
            (Finding("UNCHANGED_HASH_WITH_CLASSIFIED_CHANGE", "/"),),
        )
    if prior_content != current_content and not changes:
        return ComparisonResult(
            "ERROR",
            "AQS_SITE_DELTA_INCONSISTENT",
            None,
            (Finding("CHANGED_HASH_WITHOUT_CLASSIFIED_CHANGE", "/"),),
        )

    has_absence = any(
        change["change_type"] == "SITE_ABSENT_FROM_CURRENT_SNAPSHOT" for change in changes
    )
    high = any(change["impact"] == "HIGH" for change in changes)
    if has_absence:
        outcome = "ABSTAIN"
        reason_codes = [
            "SOURCE_RECORD_ABSENCE_REQUIRES_ASSESSMENT",
            "SOURCE_SURFACE_CHANGED",
        ]
        reason_code = "AQS_SOURCE_RECORD_ABSENCE_REQUIRES_ASSESSMENT"
    elif high:
        outcome = "ABSTAIN"
        reason_codes = ["HIGH_IMPACT_CHANGE_REQUIRES_REVIEW", "SOURCE_SURFACE_CHANGED"]
        reason_code = "AQS_HIGH_IMPACT_CHANGE_REQUIRES_REVIEW"
    elif changes:
        outcome = "PROPOSED_WORK_RECORD"
        reason_codes = ["SOURCE_SURFACE_CHANGED"]
        reason_code = "AQS_SOURCE_SURFACE_CHANGED"
    else:
        outcome = "NO_MATERIAL_CHANGE"
        reason_codes = []
        reason_code = "AQS_NO_MATERIAL_CHANGE"

    prior_sites, current_sites = _sorted_sites(prior), _sorted_sites(current)
    report = {
        "object_type": "AqsSiteMetadataDeltaReport",
        "schema_version": REPORT_SCHEMA_VERSION,
        "report_id": "aqs-site-delta:"
        + hashlib.sha256((prior_content + "\n" + current_content).encode("utf-8")).hexdigest(),
        "profile_id": PROFILE_ID,
        "fixture_only": True,
        "source_record_absence_contract_ref": SOURCE_RECORD_ABSENCE_CONTRACT_REF,
        "prior_snapshot": {
            "content_hash": prior_content,
            "retrieval_hash": snapshot_retrieval_hash(prior),
            "captured_at": prior["captured_at"],
            "source_revision": prior["source_revision"],
        },
        "current_snapshot": {
            "content_hash": current_content,
            "retrieval_hash": snapshot_retrieval_hash(current),
            "captured_at": current["captured_at"],
            "source_revision": current["source_revision"],
        },
        "summary": _summary(changes, len(prior_sites), len(current_sites)),
        "changes": changes,
        "decision": {"outcome": outcome, "reason_codes": reason_codes},
        "governance": {
            "steward_review_required": bool(changes),
            "promotion_allowed": False,
            "publication": False,
        },
    }
    findings = tuple(sorted(_report_schema_findings(report)))
    if findings:
        return ComparisonResult("ERROR", "AQS_REPORT_SCHEMA_ERROR", None, findings)
    return ComparisonResult(outcome, reason_code, report, ())


def compare_files(prior_path: Path, current_path: Path) -> ComparisonResult:
    prior, current = load_snapshot(prior_path), load_snapshot(current_path)
    findings = tuple(
        sorted(
            {Finding(item.code, f"/prior{item.path}") for item in prior.findings}
            | {Finding(item.code, f"/current{item.path}") for item in current.findings}
        )
    )
    if prior.candidate is None or current.candidate is None:
        return ComparisonResult("ERROR", "AQS_SNAPSHOT_VALIDATION_ERROR", None, findings)
    return compare_snapshots(prior.candidate, current.candidate)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compare two fixture-only EPA AQS site metadata snapshots."
    )
    parser.add_argument("--prior", type=Path, required=True)
    parser.add_argument("--current", type=Path, required=True)
    args = parser.parse_args(argv)
    result = compare_files(args.prior, args.current)
    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "reason_code": result.reason_code,
                "findings": [
                    {"code": finding.code, "path": finding.path} for finding in result.findings
                ],
                "report": result.report,
                "authority": {
                    "source_admission": False,
                    "evidence_resolution": False,
                    "promotion": False,
                    "release": False,
                    "publication": False,
                },
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.outcome == "NO_MATERIAL_CHANGE" else 1


if __name__ == "__main__":
    sys.exit(main())
