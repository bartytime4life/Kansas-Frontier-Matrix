#!/usr/bin/env python3
"""Compare frozen synthetic NHDPlus HR network snapshots without network access."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

PROFILE_ID = "kfm.nhdplus-network-revision.synthetic.v1"
MAX_JSON_BYTES = 2 * 1024 * 1024
AREA_DELTA_THRESHOLD_PCT = 0.1
CENTROID_SHIFT_THRESHOLD_M = 100.0

TOP_LEVEL_FIELDS = frozenset({"profile_id", "fixture_only", "source", "flowlines"})
SOURCE_FIELDS = frozenset(
    {
        "source_ref",
        "product",
        "product_version",
        "metadata_timestamp",
        "source_role",
        "rights_state",
    }
)
FLOWLINE_FIELDS = frozenset(
    {
        "comid",
        "reachcode",
        "hydroseq",
        "from_measure",
        "to_measure",
        "vpuid",
        "huc12",
        "geometry_metrics",
    }
)
GEOMETRY_FIELDS = frozenset(
    {"catchment_area_m2", "centroid_easting_m", "centroid_northing_m"}
)
LINEAR_FIELDS = ("reachcode", "hydroseq", "from_measure", "to_measure", "vpuid")


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class LoadResult:
    candidate: dict[str, Any] | None
    findings: tuple[Finding, ...]


@dataclass(frozen=True)
class CompareResult:
    outcome: str
    reason_code: str
    findings: tuple[Finding, ...]
    report: dict[str, Any] | None


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _is_finite_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.utcoffset() is not None else None


def _undeclared(
    findings: set[Finding],
    value: Mapping[str, Any],
    allowed: frozenset[str],
    path: str,
) -> None:
    for key in sorted(set(value) - allowed):
        findings.add(Finding("UNDECLARED_FIELD", f"{path}/{key}"))


def _validate_snapshot(snapshot: object) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    if not isinstance(snapshot, dict):
        return (Finding("ROOT_NOT_OBJECT", "/"),)

    _undeclared(findings, snapshot, TOP_LEVEL_FIELDS, "")
    if snapshot.get("profile_id") != PROFILE_ID:
        findings.add(Finding("PROFILE_ID_INVALID", "/profile_id"))
    if snapshot.get("fixture_only") is not True:
        findings.add(Finding("FIXTURE_ONLY_REQUIRED", "/fixture_only"))

    source = snapshot.get("source")
    if not isinstance(source, dict):
        findings.add(Finding("SOURCE_INVALID", "/source"))
    else:
        _undeclared(findings, source, SOURCE_FIELDS, "/source")
        if not (
            isinstance(source.get("source_ref"), str)
            and source["source_ref"].startswith("fixture://source/")
        ):
            findings.add(Finding("SOURCE_REF_INVALID", "/source/source_ref"))
        if source.get("product") != "NHDPlus HR":
            findings.add(Finding("SOURCE_PRODUCT_INVALID", "/source/product"))
        if not _is_nonempty_string(source.get("product_version")):
            findings.add(Finding("SOURCE_VERSION_INVALID", "/source/product_version"))
        if _parse_utc(source.get("metadata_timestamp")) is None:
            findings.add(
                Finding("METADATA_TIMESTAMP_INVALID", "/source/metadata_timestamp")
            )
        if source.get("source_role") != "derived_topology_context":
            findings.add(Finding("SOURCE_ROLE_INVALID", "/source/source_role"))
        if source.get("rights_state") != "public_domain_fixture":
            findings.add(Finding("RIGHTS_STATE_INVALID", "/source/rights_state"))

    flowlines = snapshot.get("flowlines")
    if not isinstance(flowlines, list) or not flowlines:
        findings.add(Finding("FLOWLINES_REQUIRED", "/flowlines"))
        return tuple(sorted(findings))

    seen: set[int] = set()
    for index, flowline in enumerate(flowlines):
        path = f"/flowlines/{index}"
        if not isinstance(flowline, dict):
            findings.add(Finding("FLOWLINE_NOT_OBJECT", path))
            continue
        _undeclared(findings, flowline, FLOWLINE_FIELDS, path)

        comid = flowline.get("comid")
        if not isinstance(comid, int) or isinstance(comid, bool) or comid <= 0:
            findings.add(Finding("COMID_INVALID", f"{path}/comid"))
        elif comid in seen:
            findings.add(Finding("COMID_DUPLICATE", f"{path}/comid"))
        else:
            seen.add(comid)

        reachcode = flowline.get("reachcode")
        if not (
            isinstance(reachcode, str)
            and len(reachcode) == 14
            and reachcode.isascii()
            and reachcode.isdigit()
        ):
            findings.add(Finding("REACHCODE_INVALID", f"{path}/reachcode"))

        hydroseq = flowline.get("hydroseq")
        if not isinstance(hydroseq, int) or isinstance(hydroseq, bool) or hydroseq <= 0:
            findings.add(Finding("HYDROSEQ_INVALID", f"{path}/hydroseq"))

        from_measure = flowline.get("from_measure")
        to_measure = flowline.get("to_measure")
        if not _is_finite_number(from_measure) or not 0 <= float(from_measure) <= 100:
            findings.add(Finding("FROM_MEASURE_INVALID", f"{path}/from_measure"))
        if not _is_finite_number(to_measure) or not 0 <= float(to_measure) <= 100:
            findings.add(Finding("TO_MEASURE_INVALID", f"{path}/to_measure"))
        if (
            _is_finite_number(from_measure)
            and _is_finite_number(to_measure)
            and float(from_measure) > float(to_measure)
        ):
            findings.add(Finding("MEASURE_ORDER_INVALID", path))

        if not _is_nonempty_string(flowline.get("vpuid")):
            findings.add(Finding("VPUID_INVALID", f"{path}/vpuid"))
        huc12 = flowline.get("huc12")
        if not (
            isinstance(huc12, str)
            and len(huc12) == 12
            and huc12.isascii()
            and huc12.isdigit()
        ):
            findings.add(Finding("HUC12_INVALID", f"{path}/huc12"))

        geometry = flowline.get("geometry_metrics")
        if not isinstance(geometry, dict):
            findings.add(Finding("GEOMETRY_METRICS_INVALID", f"{path}/geometry_metrics"))
            continue
        _undeclared(findings, geometry, GEOMETRY_FIELDS, f"{path}/geometry_metrics")
        area = geometry.get("catchment_area_m2")
        if not _is_finite_number(area) or float(area) <= 0:
            findings.add(
                Finding(
                    "CATCHMENT_AREA_INVALID",
                    f"{path}/geometry_metrics/catchment_area_m2",
                )
            )
        for key in ("centroid_easting_m", "centroid_northing_m"):
            if not _is_finite_number(geometry.get(key)):
                findings.add(
                    Finding("CENTROID_METRIC_INVALID", f"{path}/geometry_metrics/{key}")
                )

    return tuple(sorted(findings))


def load_snapshot(path: Path) -> LoadResult:
    try:
        if path.is_symlink():
            return LoadResult(None, (Finding("INPUT_SYMLINK_DENIED", "/"),))
        if not path.is_file():
            return LoadResult(None, (Finding("INPUT_NOT_FILE", "/"),))
        if path.stat().st_size > MAX_JSON_BYTES:
            return LoadResult(None, (Finding("INPUT_TOO_LARGE", "/"),))
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except UnicodeError:
        return LoadResult(None, (Finding("JSON_NOT_UTF8", "/"),))
    except DuplicateKeyError:
        return LoadResult(None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        return LoadResult(None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except json.JSONDecodeError:
        return LoadResult(None, (Finding("JSON_INVALID", "/"),))
    except OSError:
        return LoadResult(None, (Finding("INPUT_UNREADABLE", "/"),))

    findings = _validate_snapshot(value)
    return LoadResult(value if not findings else None, findings)


def _canonical_blob(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")


def _sha256(value: object) -> str:
    return "sha256:" + hashlib.sha256(_canonical_blob(value)).hexdigest()


def _canonical_flowlines(snapshot: Mapping[str, Any]) -> list[dict[str, Any]]:
    return sorted(snapshot["flowlines"], key=lambda item: int(item["comid"]))


def _snapshot_summary(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    flowlines = _canonical_flowlines(snapshot)
    network_spec_hash = _sha256({"flowlines": flowlines})
    retrieval_hash = _sha256(
        {"network_spec_hash": network_spec_hash, "source": snapshot["source"]}
    )
    return {
        "network_spec_hash": network_spec_hash,
        "retrieval_hash": retrieval_hash,
        "product_version": snapshot["source"]["product_version"],
        "record_count": len(flowlines),
    }


def _change(
    comid: int,
    change_type: str,
    impact: str,
    changed_fields: Iterable[str],
    *,
    area_delta_pct: float | None = None,
    centroid_shift_m: float | None = None,
) -> dict[str, Any]:
    value: dict[str, Any] = {
        "comid": comid,
        "change_type": change_type,
        "impact": impact,
        "changed_fields": sorted(changed_fields),
    }
    if area_delta_pct is not None:
        value["area_delta_pct"] = round(area_delta_pct, 6)
    if centroid_shift_m is not None:
        value["centroid_shift_m"] = round(centroid_shift_m, 3)
    return value


def _compare_flowline(prior: Mapping[str, Any], current: Mapping[str, Any]) -> list[dict[str, Any]]:
    comid = int(prior["comid"])
    changes: list[dict[str, Any]] = []

    linear_changed = [field for field in LINEAR_FIELDS if prior[field] != current[field]]
    if linear_changed:
        changes.append(
            _change(comid, "LINEAR_REFERENCE_CHANGE", "HIGH", linear_changed)
        )

    if prior["huc12"] != current["huc12"]:
        changes.append(
            _change(comid, "HUC12_ASSIGNMENT_CHANGE", "HIGH", ["huc12"])
        )

    prior_geometry = prior["geometry_metrics"]
    current_geometry = current["geometry_metrics"]
    geometry_fields: list[str] = []
    if prior_geometry["catchment_area_m2"] != current_geometry["catchment_area_m2"]:
        geometry_fields.append("catchment_area")
    if (
        prior_geometry["centroid_easting_m"] != current_geometry["centroid_easting_m"]
        or prior_geometry["centroid_northing_m"]
        != current_geometry["centroid_northing_m"]
    ):
        geometry_fields.append("centroid_position")
    if geometry_fields:
        prior_area = float(prior_geometry["catchment_area_m2"])
        current_area = float(current_geometry["catchment_area_m2"])
        area_delta_pct = abs(current_area - prior_area) / prior_area * 100.0
        dx = float(current_geometry["centroid_easting_m"]) - float(
            prior_geometry["centroid_easting_m"]
        )
        dy = float(current_geometry["centroid_northing_m"]) - float(
            prior_geometry["centroid_northing_m"]
        )
        centroid_shift_m = math.hypot(dx, dy)
        high = (
            area_delta_pct > AREA_DELTA_THRESHOLD_PCT
            or centroid_shift_m > CENTROID_SHIFT_THRESHOLD_M
        )
        changes.append(
            _change(
                comid,
                "GEOMETRY_SHIFT" if high else "GEOMETRY_CORRECTION",
                "HIGH" if high else "LOW",
                geometry_fields,
                area_delta_pct=area_delta_pct,
                centroid_shift_m=centroid_shift_m,
            )
        )

    return changes


def _required_actions(changes: Sequence[Mapping[str, Any]]) -> list[str]:
    types = {str(change["change_type"]) for change in changes}
    actions: set[str] = set()
    if types & {
        "COMID_ADDED",
        "COMID_REMOVED",
        "HUC12_ASSIGNMENT_CHANGE",
        "GEOMETRY_SHIFT",
        "GEOMETRY_CORRECTION",
    }:
        actions.add("RECOMPUTE_COMID_HUC12")
    if types & {"COMID_ADDED", "COMID_REMOVED", "LINEAR_REFERENCE_CHANGE"}:
        actions.add("REFRESH_LINEAR_REFERENCED_EVENTS")
    if types & {
        "COMID_ADDED",
        "COMID_REMOVED",
        "LINEAR_REFERENCE_CHANGE",
        "HUC12_ASSIGNMENT_CHANGE",
    }:
        actions.add("REINDEX_NWM_FORECAST_ATTACHMENTS")
    if types & {"GEOMETRY_SHIFT", "GEOMETRY_CORRECTION"}:
        actions.add("REVIEW_GEOMETRY_ALIGNMENT")
    return sorted(actions)


def compare_snapshots(
    prior: Mapping[str, Any], current: Mapping[str, Any]
) -> CompareResult:
    prior_findings = _validate_snapshot(prior)
    current_findings = _validate_snapshot(current)
    findings = tuple(
        sorted(
            [Finding(item.code, f"/prior{item.path}") for item in prior_findings]
            + [Finding(item.code, f"/current{item.path}") for item in current_findings]
        )
    )
    if findings:
        return CompareResult(
            "ERROR", "NHDPLUS_SNAPSHOT_VALIDATION_ERROR", findings, None
        )

    prior_summary = _snapshot_summary(prior)
    current_summary = _snapshot_summary(current)
    prior_index = {int(item["comid"]): item for item in _canonical_flowlines(prior)}
    current_index = {int(item["comid"]): item for item in _canonical_flowlines(current)}

    changes: list[dict[str, Any]] = []
    for comid in sorted(set(prior_index) - set(current_index)):
        changes.append(_change(comid, "COMID_REMOVED", "HIGH", ["comid"]))
    for comid in sorted(set(current_index) - set(prior_index)):
        changes.append(_change(comid, "COMID_ADDED", "MEDIUM", ["comid"]))
    for comid in sorted(set(prior_index) & set(current_index)):
        changes.extend(_compare_flowline(prior_index[comid], current_index[comid]))

    changes.sort(key=lambda item: (item["comid"], item["change_type"]))
    high_impact = any(change["impact"] == "HIGH" for change in changes)
    if not changes:
        outcome = "NO_MATERIAL_CHANGE"
        reason_code = "NHDPLUS_NO_MATERIAL_CHANGE"
    elif high_impact:
        outcome = "ABSTAIN"
        reason_code = "NHDPLUS_HIGH_IMPACT_NETWORK_REVISION"
    else:
        outcome = "PROPOSED_WORK_RECORD"
        reason_code = "NHDPLUS_NETWORK_REVISION"

    compared_at = max(
        str(prior["source"]["metadata_timestamp"]),
        str(current["source"]["metadata_timestamp"]),
    )
    report = {
        "object_type": "NhdplusNetworkRevisionReport",
        "schema_version": "1.0.0",
        "profile_id": PROFILE_ID,
        "comparison_id": _sha256(
            {
                "profile_id": PROFILE_ID,
                "prior": prior_summary["network_spec_hash"],
                "current": current_summary["network_spec_hash"],
            }
        ),
        "compared_at": compared_at,
        "prior_snapshot": prior_summary,
        "current_snapshot": current_summary,
        "changes": changes,
        "required_actions": _required_actions(changes),
        "decision": {"outcome": outcome, "reason_codes": [reason_code]},
        "governance": {
            "steward_review_required": bool(changes),
            "promotion_allowed": False,
            "publication": False,
        },
    }
    return CompareResult(outcome, reason_code, (), report)


def compare_files(prior_path: Path, current_path: Path) -> CompareResult:
    prior = load_snapshot(prior_path)
    current = load_snapshot(current_path)
    findings = tuple(
        sorted(
            [Finding(item.code, f"/prior{item.path}") for item in prior.findings]
            + [Finding(item.code, f"/current{item.path}") for item in current.findings]
        )
    )
    if prior.candidate is None or current.candidate is None:
        return CompareResult(
            "ERROR", "NHDPLUS_SNAPSHOT_VALIDATION_ERROR", findings, None
        )
    return compare_snapshots(prior.candidate, current.candidate)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare fixture-only NHDPlus HR network snapshots."
    )
    parser.add_argument("prior", type=Path)
    parser.add_argument("current", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = compare_files(args.prior, args.current)
    output = {
        "ok": result.outcome != "ERROR",
        "outcome": result.outcome,
        "reason_code": result.reason_code,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "report": result.report,
        "authority": {
            "source_admission": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 1 if result.outcome == "ERROR" else 0


if __name__ == "__main__":
    sys.exit(main())
