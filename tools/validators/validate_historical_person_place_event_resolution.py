#!/usr/bin/env python3
"""Validate a fixture-only historical person-place-event resolution candidate.

The validator is deterministic and no-network. A valid result proves only that a
synthetic candidate matches this bounded profile. It does not establish identity,
residence, migration, land ownership, patent validity, title, rights, policy,
review, release, or publication.
"""
from __future__ import annotations

import argparse
import errno
import hashlib
import json
import math
import os
import re
import stat
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution"
PROFILE_ID = "kfm-people-dna-land-historical-person-place-event-resolution-v1"
OBJECT_FAMILY = "HistoricalPersonPlaceEventResolutionCandidate"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 50
SUPPORTS_SECURE_DIR_FD = hasattr(os, "O_NOFOLLOW") and os.open in os.supports_dir_fd
COUNTABLE_AUTHORITIES = frozenset({"lcnaf", "viaf", "isni", "wikidata"})
PRIMARY_ORDER = ("lcnaf", "viaf", "isni", "wikidata", "local")
FORBIDDEN_RAW_DNA_KEYS = frozenset({
    "dna_segments", "genotype", "raw_dna", "raw_genotype", "sequence",
    "triangulation", "vendor_kit_id", "kit_id",
})
FORBIDDEN_PRIVATE_OR_PRECISE_KEYS = frozenset({
    "address", "coordinates", "latitude", "longitude", "parcel_id",
    "private_parcel_id", "street_address",
})


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class FileIdentity:
    device: int
    inode: int
    size: int
    modified_ns: int
    changed_ns: int


@dataclass(frozen=True)
class DirectoryIdentity:
    device: int
    inode: int
    size: int
    modified_ns: int
    changed_ns: int


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputNotRegularFileError(OSError):
    pass


class InputTooLargeError(OSError):
    pass


class FixtureInventoryError(OSError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def candidate_spec_hash(candidate: Mapping[str, Any]) -> str:
    payload = {key: value for key, value in candidate.items() if key != "spec_hash"}
    return "sha256:" + hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def _directory_flags() -> int:
    flags = os.O_RDONLY
    for flag_name in ("O_CLOEXEC", "O_DIRECTORY", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)
    return flags


def _file_flags() -> int:
    flags = os.O_RDONLY
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NONBLOCK", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)
    return flags


def _file_identity(metadata: os.stat_result) -> FileIdentity:
    return FileIdentity(
        device=metadata.st_dev,
        inode=metadata.st_ino,
        size=metadata.st_size,
        modified_ns=metadata.st_mtime_ns,
        changed_ns=metadata.st_ctime_ns,
    )


def _directory_identity(metadata: os.stat_result) -> DirectoryIdentity:
    return DirectoryIdentity(
        device=metadata.st_dev,
        inode=metadata.st_ino,
        size=metadata.st_size,
        modified_ns=metadata.st_mtime_ns,
        changed_ns=metadata.st_ctime_ns,
    )


def _open_secure_directory(path: Path) -> int:
    if not SUPPORTS_SECURE_DIR_FD:
        raise InputNotRegularFileError

    absolute_path = path.absolute()
    parts = absolute_path.parts
    if not parts or ".." in parts:
        raise InputNotRegularFileError

    directory_descriptor = os.open(parts[0], _directory_flags())
    try:
        for component in parts[1:]:
            try:
                child_descriptor = os.open(
                    component,
                    _directory_flags(),
                    dir_fd=directory_descriptor,
                )
            except OSError as error:
                if error.errno in {errno.ELOOP, errno.ENOTDIR}:
                    raise InputNotRegularFileError from error
                raise
            os.close(directory_descriptor)
            directory_descriptor = child_descriptor
        return directory_descriptor
    except BaseException:
        os.close(directory_descriptor)
        raise


def _open_bounded_regular_at(
    directory_descriptor: int,
    name: str,
    *,
    max_bytes: int = MAX_JSON_BYTES,
    expected_identity: FileIdentity | None = None,
) -> bytes:
    if not SUPPORTS_SECURE_DIR_FD or name in {"", ".", ".."} or os.sep in name:
        raise InputNotRegularFileError

    descriptor = -1
    try:
        try:
            descriptor = os.open(
                name,
                _file_flags(),
                dir_fd=directory_descriptor,
            )
        except OSError as error:
            if error.errno in {errno.ELOOP, errno.ENOTDIR}:
                raise InputNotRegularFileError from error
            raise

        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise InputNotRegularFileError
        identity = _file_identity(metadata)
        if expected_identity is not None and identity != expected_identity:
            raise InputNotRegularFileError
        if metadata.st_size > max_bytes:
            raise InputTooLargeError

        with os.fdopen(descriptor, "rb") as handle:
            descriptor = -1
            payload = handle.read(max_bytes + 1)
            identity_after_read = _file_identity(os.fstat(handle.fileno()))
        if identity_after_read != identity:
            raise InputNotRegularFileError
        if len(payload) > max_bytes:
            raise InputTooLargeError
        return payload
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _open_bounded_regular_file(path: Path, *, max_bytes: int = MAX_JSON_BYTES) -> bytes:
    """Read a regular file while holding no-follow descriptors for its parents."""
    absolute_path = path.absolute()
    parts = absolute_path.parts
    if len(parts) < 2 or ".." in parts:
        raise InputNotRegularFileError

    directory_descriptor = _open_secure_directory(Path(*parts[:-1]))
    try:
        return _open_bounded_regular_at(directory_descriptor, parts[-1], max_bytes=max_bytes)
    finally:
        os.close(directory_descriptor)


def _load_candidate_payload(payload: bytes) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        value = json.loads(
            payload.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "$")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "$")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "$")]
    except (UnicodeError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "$")]
    if not isinstance(value, dict):
        return None, [Finding("CANDIDATE_NOT_OBJECT", "$")]
    return value, []


def load_candidate(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        payload = _open_bounded_regular_file(path)
    except InputNotRegularFileError:
        return None, [Finding("INPUT_NOT_REGULAR_FILE", "$")]
    except InputTooLargeError:
        return None, [Finding("INPUT_TOO_LARGE", "$")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "$")]
    return _load_candidate_payload(payload)


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return findings


def _scan_forbidden(value: object, path: str, findings: set[Finding]) -> None:
    if isinstance(value, dict):
        for key in sorted(value):
            child = f"{path}.{key}"
            normalized = key.casefold()
            if normalized in FORBIDDEN_RAW_DNA_KEYS:
                findings.add(Finding("RAW_DNA_FIELD_DENIED", child))
            if normalized in FORBIDDEN_PRIVATE_OR_PRECISE_KEYS:
                findings.add(Finding("PRIVATE_OR_PRECISE_FIELD_DENIED", child))
            _scan_forbidden(value[key], child, findings)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan_forbidden(item, f"{path}[{index}]", findings)


def authority_points(candidate: Mapping[str, Any]) -> int:
    person = candidate.get("person")
    matches = person.get("authority_matches") if isinstance(person, dict) else None
    if not isinstance(matches, list):
        return 0
    for item in matches:
        if not isinstance(item, dict):
            continue
        refs = item.get("source_refs")
        if (
            item.get("authority") in COUNTABLE_AUTHORITIES
            and item.get("exact_match") is True
            and isinstance(refs, list)
            and len(set(ref for ref in refs if isinstance(ref, str))) >= 2
        ):
            return 3
    return 0


def co_mention_points(candidate: Mapping[str, Any]) -> int:
    place = candidate.get("place")
    mentions = candidate.get("co_mentions")
    if not isinstance(place, dict) or not isinstance(mentions, list):
        return 0
    county = place.get("county_fips")
    time_slice = place.get("time_slice")
    families: set[str] = set()
    source_refs: set[str] = set()
    for item in mentions:
        if not isinstance(item, dict):
            continue
        source_ref = item.get("source_ref")
        if source_ref in source_refs:
            continue
        if item.get("county_fips") == county and item.get("time_slice") == time_slice:
            family = item.get("source_family")
            if isinstance(family, str) and isinstance(source_ref, str):
                families.add(family)
                source_refs.add(source_ref)
    return 2 if len(families) >= 3 else 0


def glo_points(candidate: Mapping[str, Any]) -> int:
    place = candidate.get("place")
    anchor = candidate.get("glo_anchor")
    if not isinstance(place, dict) or not isinstance(anchor, dict):
        return 0
    place_legal = place.get("legal_description")
    anchor_legal = anchor.get("legal_description")
    if not isinstance(place_legal, dict) or not isinstance(anchor_legal, dict):
        return 0
    keys = ("township", "range", "section")
    exact = all(anchor_legal.get(key) == place_legal.get(key) for key in keys)
    return 2 if anchor.get("present") is True and anchor.get("exact_place_block") is True and exact else 0


def negative_points(candidate: Mapping[str, Any]) -> int:
    negatives = candidate.get("negative_evidence")
    if not isinstance(negatives, list):
        return 0
    return -3 if any(isinstance(item, dict) and item.get("strength") == "strong" for item in negatives) else 0


def expected_score(candidate: Mapping[str, Any]) -> int:
    return authority_points(candidate) + co_mention_points(candidate) + glo_points(candidate) + negative_points(candidate)


def expected_confidence(score: int) -> str:
    if score >= 5:
        return "high"
    if score >= 2:
        return "medium"
    return "low"


def expected_disposition(candidate: Mapping[str, Any], confidence: str) -> str:
    if negative_points(candidate) < 0:
        return "hold_for_review"
    if confidence == "high":
        return "candidate_review"
    if confidence == "medium":
        return "hold_for_review"
    return "abstain"


def _expected_primary(candidate: Mapping[str, Any]) -> str:
    person = candidate.get("person")
    matches = person.get("authority_matches") if isinstance(person, dict) else None
    exact: set[str] = set()
    if isinstance(matches, list):
        for item in matches:
            if isinstance(item, dict) and item.get("exact_match") is True:
                authority = item.get("authority")
                if authority in PRIMARY_ORDER:
                    exact.add(authority)
    return next((authority for authority in PRIMARY_ORDER if authority in exact), "local")


def validate_candidate(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set(_schema_findings(candidate))
    _scan_forbidden(candidate, "$", findings)

    scope = candidate.get("candidate_scope")
    if not isinstance(scope, dict):
        findings.add(Finding("CANDIDATE_SCOPE_INVALID", "$.candidate_scope"))
    else:
        if scope.get("synthetic_fixture") is not True or scope.get("historical_only") is not True:
            findings.add(Finding("SYNTHETIC_HISTORICAL_SCOPE_REQUIRED", "$.candidate_scope"))
        if scope.get("living_person") is not False:
            findings.add(Finding("LIVING_PERSON_DENIED", "$.candidate_scope.living_person"))
        if scope.get("public_release") is not False:
            findings.add(Finding("PUBLIC_RELEASE_DENIED", "$.candidate_scope.public_release"))

    governance = candidate.get("governance")
    if isinstance(governance, dict):
        if governance.get("release_state") != "not_released" or governance.get("public_exposure") is not False:
            findings.add(Finding("PUBLIC_RELEASE_DENIED", "$.governance"))
        if governance.get("promotion_eligible") is not False:
            findings.add(Finding("PROMOTION_ELIGIBILITY_DENIED", "$.governance.promotion_eligible"))
    else:
        findings.add(Finding("GOVERNANCE_INVALID", "$.governance"))

    person = candidate.get("person")
    if isinstance(person, dict) and person.get("primary_authority") != _expected_primary(candidate):
        findings.add(Finding("PRIMARY_AUTHORITY_ORDER_INVALID", "$.person.primary_authority"))

    score = expected_score(candidate)
    if candidate.get("score") != score:
        findings.add(Finding("SCORE_MISMATCH", "$.score"))
    confidence = expected_confidence(score)
    if candidate.get("confidence") != confidence:
        findings.add(Finding("CONFIDENCE_MISMATCH", "$.confidence"))
    disposition = expected_disposition(candidate, confidence)
    if candidate.get("disposition") != disposition:
        findings.add(Finding("DISPOSITION_MISMATCH", "$.disposition"))
    if isinstance(governance, dict) and governance.get("review_state") != disposition:
        findings.add(Finding("REVIEW_STATE_MISMATCH", "$.governance.review_state"))

    declared_hash = candidate.get("spec_hash")
    if declared_hash != candidate_spec_hash(candidate):
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))

    if candidate.get("profile_id") != PROFILE_ID or candidate.get("object_family") != OBJECT_FAMILY:
        findings.add(Finding("PROFILE_OR_OBJECT_FAMILY_INVALID", "$"))
    return sorted(findings)


def validate_file(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    candidate, findings = load_candidate(path)
    if candidate is None:
        return None, findings
    return candidate, validate_candidate(candidate)


def _expected_code(path: Path) -> str | None:
    sidecar = path.with_suffix(".expected_error.txt")
    try:
        payload = _open_bounded_regular_file(sidecar, max_bytes=256)
        lines = [line.strip() for line in payload.decode("utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError):
        return None
    return lines[0] if len(lines) == 1 else None


def _fixture_lane_inventory(directory_descriptor: int) -> dict[str, FileIdentity]:
    try:
        identity_before = _directory_identity(os.fstat(directory_descriptor))
        names = os.listdir(directory_descriptor)
        inventory: dict[str, FileIdentity] = {}
        for name in names:
            metadata = os.stat(name, dir_fd=directory_descriptor, follow_symlinks=False)
            if not stat.S_ISREG(metadata.st_mode):
                raise FixtureInventoryError
            inventory[name] = _file_identity(metadata)
        if _directory_identity(os.fstat(directory_descriptor)) != identity_before:
            raise FixtureInventoryError
        return inventory
    except (OSError, TypeError, ValueError) as error:
        raise FixtureInventoryError from error


def _validate_fixture_at(
    directory_descriptor: int,
    name: str,
    expected_identity: FileIdentity,
) -> list[Finding]:
    try:
        payload = _open_bounded_regular_at(
            directory_descriptor,
            name,
            expected_identity=expected_identity,
        )
    except InputNotRegularFileError:
        return [Finding("INPUT_NOT_REGULAR_FILE", "$")]
    except InputTooLargeError:
        return [Finding("INPUT_TOO_LARGE", "$")]
    except OSError:
        return [Finding("INPUT_UNREADABLE", "$")]
    candidate, findings = _load_candidate_payload(payload)
    if candidate is None:
        return findings
    return validate_candidate(candidate)


def _expected_code_at(
    directory_descriptor: int,
    candidate_name: str,
    inventory: Mapping[str, FileIdentity],
) -> str | None:
    sidecar_name = Path(candidate_name).with_suffix(".expected_error.txt").name
    expected_identity = inventory.get(sidecar_name)
    if expected_identity is None:
        return None
    try:
        payload = _open_bounded_regular_at(
            directory_descriptor,
            sidecar_name,
            max_bytes=256,
            expected_identity=expected_identity,
        )
        lines = [line.strip() for line in payload.decode("utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError):
        return None
    return lines[0] if len(lines) == 1 else None


def run_fixtures(root: Path = FIXTURE_ROOT) -> int:
    root_descriptor = valid_descriptor = invalid_descriptor = -1
    try:
        root_descriptor = _open_secure_directory(root)
        root_names = os.listdir(root_descriptor)
        lane_identities: dict[str, DirectoryIdentity] = {}
        for name in root_names:
            metadata = os.stat(name, dir_fd=root_descriptor, follow_symlinks=False)
            if name in {"valid", "invalid"}:
                if not stat.S_ISDIR(metadata.st_mode):
                    raise FixtureInventoryError
                lane_identities[name] = _directory_identity(metadata)
            elif not stat.S_ISREG(metadata.st_mode):
                raise FixtureInventoryError
        if set(lane_identities) != {"valid", "invalid"}:
            raise FixtureInventoryError
        valid_descriptor = os.open("valid", _directory_flags(), dir_fd=root_descriptor)
        if _directory_identity(os.fstat(valid_descriptor)) != lane_identities["valid"]:
            raise FixtureInventoryError
        invalid_descriptor = os.open("invalid", _directory_flags(), dir_fd=root_descriptor)
        if _directory_identity(os.fstat(invalid_descriptor)) != lane_identities["invalid"]:
            raise FixtureInventoryError
        valid_inventory = _fixture_lane_inventory(valid_descriptor)
        invalid_inventory = _fixture_lane_inventory(invalid_descriptor)
        valid_names = sorted(name for name in valid_inventory if name.endswith(".json"))
        invalid_names = sorted(name for name in invalid_inventory if name.endswith(".json"))
    except (OSError, FixtureInventoryError, InputNotRegularFileError):
        for descriptor in (invalid_descriptor, valid_descriptor, root_descriptor):
            if descriptor >= 0:
                os.close(descriptor)
        print("HISTORICAL_RESOLUTION_FIXTURES_ERROR fixture inventory unreadable")
        return 2
    try:
        failures: list[str] = []
        if not valid_names or not invalid_names:
            print("HISTORICAL_RESOLUTION_FIXTURES_ERROR nonempty valid and invalid lanes required")
            return 2
        for name in valid_names:
            if _validate_fixture_at(valid_descriptor, name, valid_inventory[name]):
                failures.append(f"valid/{name}")
        for name in invalid_names:
            findings = _validate_fixture_at(invalid_descriptor, name, invalid_inventory[name])
            expected = _expected_code_at(invalid_descriptor, name, invalid_inventory)
            if expected is None or expected not in {finding.code for finding in findings}:
                failures.append(f"invalid/{name}")
        if failures:
            for item in failures:
                print(f"HISTORICAL_RESOLUTION_FIXTURE_POLARITY_FAIL file={item}")
            return 1
        print(f"HISTORICAL_RESOLUTION_FIXTURES_VALID valid={len(valid_names)} invalid={len(invalid_names)}")
        return 0
    finally:
        for descriptor in (invalid_descriptor, valid_descriptor, root_descriptor):
            if descriptor >= 0:
                os.close(descriptor)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.paths:
            raise SystemExit("--fixtures cannot be combined with paths")
        return run_fixtures()
    if not args.paths:
        raise SystemExit("at least one path is required unless --fixtures is used")
    failed = False
    for input_index, path in enumerate(args.paths, start=1):
        candidate, findings = validate_file(path)
        if findings:
            failed = True
            for finding in findings:
                print(
                    "HISTORICAL_RESOLUTION_INVALID "
                    f"input_index={input_index} code={finding.code} field={finding.field}"
                )
        else:
            assert candidate is not None
            print(
                "HISTORICAL_RESOLUTION_VALID "
                f"input_index={input_index} score={candidate['score']} confidence={candidate['confidence']} "
                f"disposition={candidate['disposition']}"
            )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
