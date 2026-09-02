#!/usr/bin/env python3
"""Compare frozen synthetic CDL sidecars and emit a review signal.

This is a fixture-first, no-network watcher helper.  It does not fetch CDL,
admit a source, create a SourceIntakeRecord or receipt, start a pipeline,
promote lifecycle state, or publish.  The profile is deliberately narrower
than the still-proposed live CDL sidecar and threshold contracts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    validate_fixture_file,
)


PROFILE_ID = "kfm-cdl-watch-fixture-v1"
FIXTURE_SOURCE_DESCRIPTOR_REF = "fixture://source/usda-nass-cdl"
FIXTURE_COUNTY_FIPS = "99999"
HASH_PREFIX = "sha256:"
PPM_DENOMINATOR = 1_000_000
MAX_CLASS_COUNT = 256
MAX_AREA_M2 = 10**14

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "profile_id",
        "fixture_only",
        "source_descriptor_ref",
        "cdl_year",
        "county_fips",
        "observed_at",
        "source_metadata",
        "classmap_version",
        "county_geometry_hash",
        "county_area_m2",
        "class_histogram_m2",
        "thresholds",
        "profile_hash",
    }
)
ALLOWED_SOURCE_METADATA_FIELDS = frozenset(
    {"etag", "last_modified", "content_length", "sha256"}
)
ALLOWED_THRESHOLD_FIELDS = frozenset(
    {
        "relative_change_ppm",
        "absolute_change_m2_floor",
        "absolute_county_ppm",
    }
)
SAFE_EXIT_OUTCOMES = frozenset({"NO_MATERIAL_CHANGE", "PROPOSED_WORK_RECORD"})
BLOCKING_OUTCOMES = frozenset(
    {"STALE_INPUT", "CLASSMAP_DRIFT", "GEOMETRY_DRIFT", "ABSTAIN", "ERROR"}
)
NEXT_REVIEW = (
    "confirm the canonical source descriptor and rights posture",
    "review the caller-supplied materiality profile",
    "run source admission and pipeline workflows only if separately approved",
    "require evidence, policy, review, release, correction, and rollback closure before public use",
)

_ASCII_TOKEN = re.compile(r"^[\x21-\x7e]+$")
_CLASS_ID = re.compile(r"^(?:0|[1-9][0-9]{0,3})$")
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


@dataclass(frozen=True)
class LoadedSidecar:
    """One decoded sidecar or its non-echoing validation findings."""

    candidate: dict[str, object] | None
    findings: tuple[Finding, ...]


def _is_ascii_token(value: object, *, maximum: int = 200) -> bool:
    return (
        isinstance(value, str)
        and 0 < len(value) <= maximum
        and _ASCII_TOKEN.fullmatch(value) is not None
    )


def _is_canonical_utc(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return parsed.strftime("%Y-%m-%dT%H:%M:%SZ") == value


def _is_positive_bounded_int(value: object, *, maximum: int) -> bool:
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and 0 < value <= maximum
    )


def _is_nonnegative_bounded_int(value: object, *, maximum: int) -> bool:
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and 0 <= value <= maximum
    )


def _canonical_profile_bytes(candidate: Mapping[str, object]) -> bytes:
    """Return canonical bytes for the restricted integer/string fixture profile.

    This function is intentionally not a general RFC 8785 implementation and
    does not claim KFM-wide ``spec_hash`` authority.  The profile validator
    permits only JSON types for which sorted compact JSON is stable here.
    """

    payload = {
        key: value
        for key, value in candidate.items()
        if key not in {"observed_at", "profile_hash"}
    }
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("ascii")


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    """Compute the fixture-only profile hash."""

    digest = hashlib.sha256(_canonical_profile_bytes(candidate)).hexdigest()
    return HASH_PREFIX + digest


def _validate_source_metadata(
    findings: set[Finding], metadata: object
) -> None:
    path = "$.source_metadata"
    if not isinstance(metadata, dict):
        add_finding(findings, "SOURCE_METADATA_INVALID", path)
        return
    find_undeclared_fields(
        findings,
        metadata,
        ALLOWED_SOURCE_METADATA_FIELDS,
        "UNDECLARED_SOURCE_METADATA_FIELD",
        path,
    )
    if not _is_ascii_token(metadata.get("etag")):
        add_finding(findings, "SOURCE_ETAG_INVALID", f"{path}.etag")
    if not _is_canonical_utc(metadata.get("last_modified")):
        add_finding(
            findings,
            "SOURCE_LAST_MODIFIED_INVALID",
            f"{path}.last_modified",
        )
    if not _is_positive_bounded_int(
        metadata.get("content_length"), maximum=10**12
    ):
        add_finding(
            findings,
            "SOURCE_CONTENT_LENGTH_INVALID",
            f"{path}.content_length",
        )
    digest = metadata.get("sha256")
    if (
        not isinstance(digest, str)
        or _SHA256.fullmatch(digest) is None
        or digest == HASH_PREFIX + ("0" * 64)
    ):
        add_finding(findings, "SOURCE_SHA256_INVALID", f"{path}.sha256")


def _validate_thresholds(findings: set[Finding], thresholds: object) -> None:
    path = "$.thresholds"
    if not isinstance(thresholds, dict):
        add_finding(findings, "THRESHOLDS_INVALID", path)
        return
    find_undeclared_fields(
        findings,
        thresholds,
        ALLOWED_THRESHOLD_FIELDS,
        "UNDECLARED_THRESHOLD_FIELD",
        path,
    )
    if not _is_positive_bounded_int(
        thresholds.get("relative_change_ppm"), maximum=PPM_DENOMINATOR
    ):
        add_finding(
            findings,
            "RELATIVE_THRESHOLD_INVALID",
            f"{path}.relative_change_ppm",
        )
    if not _is_positive_bounded_int(
        thresholds.get("absolute_change_m2_floor"), maximum=MAX_AREA_M2
    ):
        add_finding(
            findings,
            "ABSOLUTE_THRESHOLD_INVALID",
            f"{path}.absolute_change_m2_floor",
        )
    if not _is_positive_bounded_int(
        thresholds.get("absolute_county_ppm"), maximum=PPM_DENOMINATOR
    ):
        add_finding(
            findings,
            "ABSOLUTE_COUNTY_THRESHOLD_INVALID",
            f"{path}.absolute_county_ppm",
        )


def _validate_histogram(
    findings: set[Finding], histogram: object, county_area_m2: object
) -> None:
    path = "$.class_histogram_m2"
    if not isinstance(histogram, dict) or not histogram:
        add_finding(findings, "CLASS_HISTOGRAM_INVALID", path)
        return
    if len(histogram) > MAX_CLASS_COUNT:
        add_finding(findings, "CLASS_COUNT_EXCEEDED", path)
        return

    total = 0
    for class_id, area in sorted(
        histogram.items(), key=lambda item: (type(item[0]).__name__, repr(item[0]))
    ):
        class_path = f"{path}.{class_id}"
        if not isinstance(class_id, str) or _CLASS_ID.fullmatch(class_id) is None:
            add_finding(findings, "CLASS_ID_INVALID", class_path)
        if not _is_nonnegative_bounded_int(area, maximum=MAX_AREA_M2):
            add_finding(findings, "CLASS_AREA_INVALID", class_path)
            continue
        total += area

    if total == 0:
        add_finding(findings, "CLASS_HISTOGRAM_ZERO_COVERAGE", path)
    if (
        _is_positive_bounded_int(county_area_m2, maximum=MAX_AREA_M2)
        and total > county_area_m2
    ):
        add_finding(findings, "HISTOGRAM_AREA_EXCEEDS_COUNTY", path)


def validate_sidecar(candidate: object) -> list[Finding]:
    """Validate one sidecar against the frozen synthetic profile."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("SIDECAR_NOT_OBJECT", "$")]

    find_undeclared_fields(
        findings,
        candidate,
        ALLOWED_TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )
    if candidate.get("profile_id") != PROFILE_ID:
        add_finding(findings, "PROFILE_ID_INVALID", "$.profile_id")
    if candidate.get("fixture_only") is not True:
        add_finding(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("source_descriptor_ref") != FIXTURE_SOURCE_DESCRIPTOR_REF:
        add_finding(
            findings,
            "FIXTURE_SOURCE_DESCRIPTOR_REF_INVALID",
            "$.source_descriptor_ref",
        )
    year = candidate.get("cdl_year")
    if (
        not isinstance(year, int)
        or isinstance(year, bool)
        or not 1900 <= year <= 9999
    ):
        add_finding(findings, "CDL_YEAR_INVALID", "$.cdl_year")
    if candidate.get("county_fips") != FIXTURE_COUNTY_FIPS:
        add_finding(findings, "FIXTURE_COUNTY_FIPS_INVALID", "$.county_fips")
    observed_at = candidate.get("observed_at")
    if not _is_canonical_utc(observed_at):
        add_finding(findings, "OBSERVED_AT_INVALID", "$.observed_at")

    source_metadata = candidate.get("source_metadata")
    _validate_source_metadata(findings, source_metadata)
    if (
        isinstance(year, int)
        and not isinstance(year, bool)
        and _is_canonical_utc(observed_at)
    ):
        if year > int(observed_at[:4]):
            add_finding(findings, "CDL_YEAR_AFTER_OBSERVED", "$.cdl_year")
    if isinstance(source_metadata, dict):
        last_modified = source_metadata.get("last_modified")
        if _is_canonical_utc(observed_at) and _is_canonical_utc(last_modified):
            if last_modified > observed_at:
                add_finding(
                    findings,
                    "SOURCE_LAST_MODIFIED_AFTER_OBSERVED",
                    "$.source_metadata.last_modified",
                )

    if not _is_ascii_token(candidate.get("classmap_version"), maximum=100):
        add_finding(findings, "CLASSMAP_VERSION_INVALID", "$.classmap_version")
    geometry_hash = candidate.get("county_geometry_hash")
    if (
        not isinstance(geometry_hash, str)
        or _SHA256.fullmatch(geometry_hash) is None
        or geometry_hash == HASH_PREFIX + ("0" * 64)
    ):
        add_finding(
            findings,
            "COUNTY_GEOMETRY_HASH_INVALID",
            "$.county_geometry_hash",
        )

    county_area_m2 = candidate.get("county_area_m2")
    if not _is_positive_bounded_int(county_area_m2, maximum=MAX_AREA_M2):
        add_finding(findings, "COUNTY_AREA_INVALID", "$.county_area_m2")
    _validate_histogram(
        findings, candidate.get("class_histogram_m2"), county_area_m2
    )
    _validate_thresholds(findings, candidate.get("thresholds"))

    profile_hash = candidate.get("profile_hash")
    if not isinstance(profile_hash, str) or _SHA256.fullmatch(profile_hash) is None:
        add_finding(findings, "PROFILE_HASH_INVALID", "$.profile_hash")
    else:
        try:
            expected_hash = compute_profile_hash(candidate)
        except (TypeError, ValueError, UnicodeError, OverflowError):
            add_finding(findings, "PROFILE_HASH_INPUT_INVALID", "$.profile_hash")
        else:
            if profile_hash != expected_hash:
                add_finding(findings, "PROFILE_HASH_MISMATCH", "$.profile_hash")

    return sorted(findings)


def load_sidecar(path: Path | str) -> LoadedSidecar:
    """Load one bounded sidecar using the repository's shared JSON mechanics."""

    decoded: list[object] = []

    def capture(candidate: object) -> list[Finding]:
        decoded.append(candidate)
        return validate_sidecar(candidate)

    findings = tuple(validate_fixture_file(path, capture))
    if findings or not decoded or not isinstance(decoded[0], dict):
        return LoadedSidecar(candidate=None, findings=findings)
    return LoadedSidecar(candidate=decoded[0], findings=())


def _input_error_report(
    prior_path: Path, current_path: Path, prior: LoadedSidecar, current: LoadedSidecar
) -> dict[str, object]:
    reason_codes = {
        f"PRIOR_{finding.code}" for finding in prior.findings
    } | {f"CURRENT_{finding.code}" for finding in current.findings}
    if not reason_codes:
        reason_codes.add("SIDECAR_LOAD_ERROR")
    return _report(
        prior_path=prior_path,
        current_path=current_path,
        outcome="ERROR",
        reason_codes=sorted(reason_codes),
        checks={
            "metadata_drift": "not_evaluated",
            "cdl_year": "not_evaluated",
            "classmap_drift": "not_evaluated",
            "county_geometry_hash": "not_evaluated",
            "county_area_m2": "not_evaluated",
            "threshold_profile": "not_evaluated",
            "histogram_drift": "not_evaluated",
        },
        current=None,
    )


def _ceil_fraction(value: int, numerator: int, denominator: int) -> int:
    return (value * numerator + denominator - 1) // denominator


def _report(
    *,
    prior_path: Path,
    current_path: Path,
    outcome: str,
    reason_codes: Sequence[str],
    checks: Mapping[str, object],
    current: Mapping[str, object] | None,
) -> dict[str, object]:
    report: dict[str, object] = {
        "tool": "cdl-watch",
        "report_profile": PROFILE_ID,
        "status": outcome,
        "inputs": {
            "prior_sidecar": str(prior_path),
            "current_sidecar": str(current_path),
        },
        "checks": dict(checks),
        "decision": {
            "outcome": outcome,
            "reason_codes": sorted(set(reason_codes)),
            "blocking": outcome in BLOCKING_OUTCOMES,
            "publication": False,
            "promotion_required": True,
        },
        "next_review": list(NEXT_REVIEW),
    }
    if current is not None:
        report.update(
            {
                "source_descriptor_ref": current["source_descriptor_ref"],
                "cdl_year": current["cdl_year"],
                "county_fips": current["county_fips"],
            }
        )
    return report


def compare_sidecars(
    prior_path: Path | str, current_path: Path | str
) -> dict[str, object]:
    """Compare two sidecars and return one deterministic review report."""

    prior_file = Path(prior_path)
    current_file = Path(current_path)
    prior_loaded = load_sidecar(prior_file)
    current_loaded = load_sidecar(current_file)
    if prior_loaded.findings or current_loaded.findings:
        return _input_error_report(
            prior_file, current_file, prior_loaded, current_loaded
        )

    prior = prior_loaded.candidate
    current = current_loaded.candidate
    assert prior is not None and current is not None

    checks: dict[str, object] = {
        "metadata_drift": (
            "same"
            if prior["source_metadata"] == current["source_metadata"]
            else "changed"
        ),
        "cdl_year": (
            "same"
            if prior["cdl_year"] == current["cdl_year"]
            else (
                "advanced"
                if current["cdl_year"] > prior["cdl_year"]  # type: ignore[operator]
                else "regressed"
            )
        ),
        "classmap_drift": (
            "same"
            if prior["classmap_version"] == current["classmap_version"]
            else "changed"
        ),
        "county_geometry_hash": (
            "same"
            if prior["county_geometry_hash"] == current["county_geometry_hash"]
            else "changed"
        ),
        "county_area_m2": (
            "same"
            if prior["county_area_m2"] == current["county_area_m2"]
            else "changed"
        ),
        "threshold_profile": (
            "same" if prior["thresholds"] == current["thresholds"] else "changed"
        ),
        "histogram_drift": "not_evaluated",
    }

    if prior["source_descriptor_ref"] != current["source_descriptor_ref"]:
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome="ABSTAIN",
            reason_codes=["SOURCE_DESCRIPTOR_REF_DRIFT"],
            checks=checks,
            current=current,
        )
    if prior["county_fips"] != current["county_fips"]:
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome="ABSTAIN",
            reason_codes=["COUNTY_SCOPE_DRIFT"],
            checks=checks,
            current=current,
        )
    prior_metadata = prior["source_metadata"]
    current_metadata = current["source_metadata"]
    assert isinstance(prior_metadata, dict)
    assert isinstance(current_metadata, dict)

    stale_reasons: list[str] = []
    if current["cdl_year"] < prior["cdl_year"]:  # type: ignore[operator]
        stale_reasons.append("CDL_YEAR_REGRESSED")
    if current["observed_at"] < prior["observed_at"]:  # type: ignore[operator]
        stale_reasons.append("OBSERVED_AT_REGRESSED")
    if current_metadata["last_modified"] < prior_metadata["last_modified"]:
        stale_reasons.append("SOURCE_LAST_MODIFIED_REGRESSED")
    if stale_reasons:
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome="STALE_INPUT",
            reason_codes=stale_reasons,
            checks=checks,
            current=current,
        )
    if checks["threshold_profile"] == "changed":
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome="ABSTAIN",
            reason_codes=["MATERIALITY_PROFILE_DRIFT"],
            checks=checks,
            current=current,
        )
    if checks["classmap_drift"] == "changed":
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome="CLASSMAP_DRIFT",
            reason_codes=["CDL_CLASSMAP_DRIFT_REQUIRES_REMAP_REVIEW"],
            checks=checks,
            current=current,
        )
    geometry_reasons: list[str] = []
    if checks["county_geometry_hash"] == "changed":
        geometry_reasons.append("COUNTY_GEOMETRY_DRIFT_REQUIRES_REBASE")
    if checks["county_area_m2"] == "changed":
        geometry_reasons.append("COUNTY_AREA_DRIFT_REQUIRES_REBASE")
    if geometry_reasons:
        return _report(
            prior_path=prior_file,
            current_path=current_file,
            outcome="GEOMETRY_DRIFT",
            reason_codes=geometry_reasons,
            checks=checks,
            current=current,
        )

    prior_histogram = prior["class_histogram_m2"]
    current_histogram = current["class_histogram_m2"]
    thresholds = current["thresholds"]
    county_area_m2 = current["county_area_m2"]
    assert isinstance(prior_histogram, dict)
    assert isinstance(current_histogram, dict)
    assert isinstance(thresholds, dict)
    assert isinstance(county_area_m2, int)

    relative_ppm = thresholds["relative_change_ppm"]
    absolute_floor = thresholds["absolute_change_m2_floor"]
    absolute_county_ppm = thresholds["absolute_county_ppm"]
    assert isinstance(relative_ppm, int)
    assert isinstance(absolute_floor, int)
    assert isinstance(absolute_county_ppm, int)
    absolute_threshold = max(
        absolute_floor,
        _ceil_fraction(county_area_m2, absolute_county_ppm, PPM_DENOMINATOR),
    )

    max_change = 0
    relative_reached = False
    absolute_reached = False
    for class_id in sorted(set(prior_histogram) | set(current_histogram)):
        prior_area = prior_histogram.get(class_id, 0)
        current_area = current_histogram.get(class_id, 0)
        assert isinstance(prior_area, int) and isinstance(current_area, int)
        change = abs(current_area - prior_area)
        max_change = max(max_change, change)
        relative_reached = relative_reached or (
            change * PPM_DENOMINATOR >= county_area_m2 * relative_ppm
        )
        absolute_reached = absolute_reached or change >= absolute_threshold

    material = relative_reached or absolute_reached
    if max_change == 0:
        checks["histogram_drift"] = "same"
    elif material:
        checks["histogram_drift"] = "material"
    else:
        checks["histogram_drift"] = "below_threshold"
    checks["maximum_class_change_m2"] = max_change
    checks["absolute_change_threshold_m2"] = absolute_threshold

    reason_codes: list[str] = []
    if relative_reached:
        reason_codes.append("CDL_HISTOGRAM_RELATIVE_THRESHOLD_REACHED")
    if absolute_reached:
        reason_codes.append("CDL_HISTOGRAM_ABSOLUTE_THRESHOLD_REACHED")

    outcome = "PROPOSED_WORK_RECORD" if material else "NO_MATERIAL_CHANGE"
    return _report(
        prior_path=prior_file,
        current_path=current_file,
        outcome=outcome,
        reason_codes=reason_codes,
        checks=checks,
        current=current,
    )


def serialize_report(report: Mapping[str, object]) -> str:
    return json.dumps(report, sort_keys=True, separators=(",", ":"))


def _resolved_output_path(path: Path) -> Path:
    """Resolve the actual output target and deny every repository destination."""

    if path.name in {"", ".", ".."}:
        raise OSError("report output filename is invalid")
    candidate = path if path.is_absolute() else Path.cwd() / path
    try:
        resolved_parent = candidate.parent.resolve(strict=True)
        resolved_repo = REPO_ROOT.resolve(strict=True)
    except OSError as error:
        raise OSError("report output parent could not be resolved safely") from error
    if not resolved_parent.is_dir():
        raise OSError("report output parent must be an existing directory")

    resolved_candidate = resolved_parent / candidate.name
    try:
        resolved_candidate.relative_to(resolved_repo)
    except ValueError:
        return resolved_candidate
    raise OSError("report output inside the repository is denied")


def write_report(path: Path, serialized: str) -> None:
    """Create one explicit report outside the repository without overwriting."""

    output_path = _resolved_output_path(path)

    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)
    descriptor = os.open(output_path, flags, stat.S_IRUSR | stat.S_IWUSR)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            stream.write((serialized + "\n").encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two frozen synthetic CDL sidecars and emit a review-only "
            "material-change report."
        )
    )
    parser.add_argument("--prior", required=True, type=Path)
    parser.add_argument("--current", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        required=True,
        help="acknowledge that this helper cannot publish or promote",
    )
    args = parser.parse_args(argv)

    report = compare_sidecars(args.prior, args.current)
    serialized = serialize_report(report)
    if args.output is None:
        print(serialized)
    else:
        try:
            write_report(args.output, serialized)
        except OSError:
            print("report output could not be created safely", file=sys.stderr)
            return 2

    decision = report.get("decision")
    outcome = decision.get("outcome") if isinstance(decision, dict) else "ERROR"
    return 0 if outcome in SAFE_EXIT_OUTCOMES else 1


if __name__ == "__main__":
    raise SystemExit(main())
