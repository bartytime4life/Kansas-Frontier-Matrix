#!/usr/bin/env python3
"""Classify normalized Flora occurrence candidates for bounded intake handling.

This no-network classifier proposes WORK/QUARANTINE handling, deterministic
record deduplication, and conservative license/sensitivity dispositions.  It is
not a legal opinion, policy engine, review approval, lifecycle transition,
release decision, or publication mechanism.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

MAX_FILE_BYTES = 1_048_576
HASH_PROFILE = "kfm-fixture-json-v1"
ENGINE_ID = "flora-occurrence-intake-governance"
ENGINE_VERSION = "1.0.0"
RIGHTS_PROFILE_ID = "flora-occurrence-license-map-v1"
SCOPE = "flora-occurrence-work-intake-classification-only"

OPEN_LICENSES = {
    "CC-BY-4.0",
    "CC0-1.0",
    "PDDL-1.0",
    "PUBLIC-DOMAIN",
}
CONDITIONAL_MARKERS = (
    "CC-BY-NC",
    "CC-BY-SA",
    "ODBL",
    "RESTRICTED",
    "CUSTOM",
)


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class DecisionResult:
    outcome: str
    findings: tuple[Finding, ...]
    decision: Mapping[str, Any] | None = None

    @property
    def ok(self) -> bool:
        return self.outcome in {
            "ACCEPT_FOR_WORK",
            "DEDUPLICATE",
            "HOLD_FOR_REVIEW",
            "QUARANTINE",
        } and self.decision is not None


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_json(path: Path) -> tuple[Any | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, (Finding("FILE_TOO_LARGE", "/"),)
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, (Finding("JSON_NOT_UTF8", "/"),)
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except json.JSONDecodeError:
        return None, (Finding("JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("FILE_READ_ERROR", "/"),)
    except (RecursionError, ValueError):
        return None, (Finding("JSON_COMPLEXITY_LIMIT", "/"),)
    return value, ()


def _canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def candidate_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    return _canonical_digest(projected)


def decision_spec_hash(decision: Mapping[str, Any]) -> str:
    projected = dict(decision)
    projected.pop("spec_hash", None)
    return _canonical_digest(projected)


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _text(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = " ".join(value.split())
    return cleaned or None


def _candidate_findings(candidate: Mapping[str, Any], prefix: str = "") -> list[Finding]:
    findings: list[Finding] = []
    field = lambda suffix: f"{prefix}{suffix}" or "/"
    if candidate.get("object_type") != "FloraOccurrenceCandidate":
        findings.append(Finding("CANDIDATE_OBJECT_TYPE_INVALID", field("/object_type")))
    if candidate.get("schema_version") != "1.0.0":
        findings.append(Finding("CANDIDATE_SCHEMA_VERSION_INVALID", field("/schema_version")))
    candidate_id = candidate.get("candidate_id")
    if not isinstance(candidate_id, str) or not candidate_id.startswith("flora-occurrence-candidate:"):
        findings.append(Finding("CANDIDATE_ID_INVALID", field("/candidate_id")))
    supplied_hash = candidate.get("spec_hash")
    if not isinstance(supplied_hash, str) or supplied_hash != candidate_spec_hash(candidate):
        findings.append(Finding("CANDIDATE_SPEC_HASH_MISMATCH", field("/spec_hash")))
    governance = _mapping(candidate.get("governance"))
    if (
        governance.get("lifecycle_state") != "WORK"
        or any(
            governance.get(name) is not False
            for name in (
                "source_admitted",
                "evidence_bundle_resolved",
                "policy_evaluated",
                "review_completed",
                "promotion_authorized",
                "release_authorized",
                "publication_authorized",
                "public_use_allowed",
            )
        )
        or governance.get("release_ref") is not None
    ):
        findings.append(Finding("CANDIDATE_GOVERNANCE_INVALID", field("/governance")))
    source = _mapping(candidate.get("source_context"))
    taxon = _mapping(candidate.get("taxon"))
    if _text(source.get("source_record_id")) is None:
        findings.append(Finding("CANDIDATE_SOURCE_RECORD_ID_MISSING", field("/source_context/source_record_id")))
    if _text(taxon.get("scientific_name")) is None:
        findings.append(Finding("CANDIDATE_SCIENTIFIC_NAME_MISSING", field("/taxon/scientific_name")))
    return findings


def _normalize_key(value: Any) -> str | None:
    text = _text(value)
    return text.casefold() if text is not None else None


def _primary_key(candidate: Mapping[str, Any]) -> str | None:
    source = _mapping(candidate.get("source_context"))
    institution = _normalize_key(source.get("institution_code"))
    catalog = _normalize_key(source.get("catalog_number"))
    if institution is None or catalog is None:
        return None
    return f"institution={institution}\x1fcatalog={catalog}"


def _fallback_key(candidate: Mapping[str, Any]) -> str | None:
    taxon = _normalize_key(_mapping(candidate.get("taxon")).get("scientific_name"))
    event_date = _text(_mapping(candidate.get("occurrence")).get("event_date"))
    geometry = _mapping(_mapping(candidate.get("spatial")).get("geometry"))
    coordinates = _array(geometry.get("coordinates"))
    if taxon is None or event_date is None or len(coordinates) != 2:
        return None
    lon, lat = coordinates
    if not isinstance(lon, (int, float)) or isinstance(lon, bool):
        return None
    if not isinstance(lat, (int, float)) or isinstance(lat, bool):
        return None
    # Four decimal places are a deterministic comparison aid only; they do not
    # generalize, publish, or overwrite source geometry.
    return f"taxon={taxon}\x1fdate={event_date}\x1flon={float(lon):.4f}\x1flat={float(lat):.4f}"


def _fingerprint(value: str | None) -> str | None:
    return None if value is None else "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def _classify_license(value: Any) -> tuple[str, str, list[str]]:
    text = _text(value)
    if text is None:
        return "UNKNOWN", "QUARANTINE", ["LICENSE_MISSING"]
    normalized = text.upper().replace("_", "-")
    if normalized in OPEN_LICENSES:
        return "OPEN_DECLARED", "ALLOW_WORK", ["LICENSE_OPEN_PROFILE_MATCH"]
    if any(marker in normalized for marker in CONDITIONAL_MARKERS):
        return "RESTRICTED_OR_CONDITIONAL", "QUARANTINE", ["LICENSE_REQUIRES_STEWARD_REVIEW"]
    return "UNKNOWN", "QUARANTINE", ["LICENSE_UNRECOGNIZED"]


def _classify_sensitivity(candidate: Mapping[str, Any]) -> tuple[bool, list[str], str, list[str]]:
    spatial = _mapping(candidate.get("spatial"))
    exact = spatial.get("geometry") is not None and spatial.get("coordinate_exposure") == "INTERNAL_EXACT"
    hints = sorted({item for item in _array(candidate.get("sensitivity_hints")) if isinstance(item, str)})
    if hints and exact:
        return exact, hints, "GENERALIZE_REQUIRED", ["SENSITIVE_EXACT_GEOMETRY_REQUIRES_REVIEW"]
    if hints:
        return exact, hints, "HOLD_FOR_REVIEW", ["SOURCE_SENSITIVITY_HINT_REQUIRES_REVIEW"]
    return exact, hints, "NO_SPECIAL_HANDLING", ["NO_SOURCE_SENSITIVITY_HINT"]


def _peer_set(peers: Sequence[Mapping[str, Any]]) -> tuple[list[Mapping[str, Any]], list[Finding]]:
    findings: list[Finding] = []
    ordered = sorted(peers, key=lambda item: str(item.get("candidate_id", "")))
    ids = [item.get("candidate_id") for item in ordered]
    if any(not isinstance(item, str) for item in ids) or len(ids) != len(set(ids)):
        findings.append(Finding("PEER_SET_IDENTITY_INVALID", "/peers"))
    for index, peer in enumerate(ordered):
        findings.extend(_candidate_findings(peer, f"/peers/{index}"))
    return ordered, findings


def classify_candidate(
    candidate: Mapping[str, Any], peers: Sequence[Mapping[str, Any]] = ()
) -> DecisionResult:
    findings = _candidate_findings(candidate)
    ordered_peers, peer_findings = _peer_set(peers)
    findings.extend(peer_findings)
    candidate_id = candidate.get("candidate_id")
    if isinstance(candidate_id, str) and any(peer.get("candidate_id") == candidate_id for peer in ordered_peers):
        findings.append(Finding("PEER_SET_CONTAINS_CANDIDATE", "/peers"))
    if findings:
        return DecisionResult("ERROR", tuple(sorted(set(findings))))

    primary = _primary_key(candidate)
    fallback = _fallback_key(candidate)
    duplicate_of: str | None = None
    duplicate_method = "NONE"
    duplicate_fingerprint: str | None = None

    if primary is not None:
        for peer in ordered_peers:
            if _primary_key(peer) == primary:
                duplicate_of = str(peer["candidate_id"])
                duplicate_method = "PRIMARY_INSTITUTION_CATALOG"
                duplicate_fingerprint = _fingerprint(primary)
                break
    if duplicate_of is None and fallback is not None:
        for peer in ordered_peers:
            if _fallback_key(peer) == fallback:
                duplicate_of = str(peer["candidate_id"])
                duplicate_method = "FALLBACK_SPATIOTEMPORAL_TAXON"
                duplicate_fingerprint = _fingerprint(fallback)
                break

    source = _mapping(candidate.get("source_context"))
    license_class, rights_disposition, rights_reasons = _classify_license(source.get("license"))
    exact, sensitivity_hints, sensitivity_disposition, sensitivity_reasons = _classify_sensitivity(candidate)

    if duplicate_of is not None:
        outcome = "DEDUPLICATE"
        decision_reasons = ["DUPLICATE_CANDIDATE_MATCHED"]
        target = "WORK"
    elif rights_disposition == "QUARANTINE":
        outcome = "QUARANTINE"
        decision_reasons = sorted(set(rights_reasons))
        target = "QUARANTINE"
    elif sensitivity_disposition != "NO_SPECIAL_HANDLING":
        outcome = "HOLD_FOR_REVIEW"
        decision_reasons = sorted(set(sensitivity_reasons))
        target = "WORK"
    else:
        outcome = "ACCEPT_FOR_WORK"
        decision_reasons = ["BOUNDED_INTAKE_CHECKS_PASSED"]
        target = "WORK"

    peer_set_digest = _canonical_digest(ordered_peers)
    candidate_hash = str(candidate["spec_hash"])
    decision_key = f"{candidate_hash}\x1f{peer_set_digest}\x1f{ENGINE_VERSION}".encode("utf-8")
    decision_id = "flora-occurrence-intake-decision:" + hashlib.sha256(decision_key).hexdigest()[:32]

    decision: dict[str, Any] = {
        "object_type": "FloraOccurrenceIntakeDecision",
        "schema_version": "1.0.0",
        "decision_id": decision_id,
        "hash_profile": HASH_PROFILE,
        "spec_hash": "",
        "candidate_ref": str(candidate_id),
        "candidate_spec_hash": candidate_hash,
        "duplicate": {
            "method": duplicate_method,
            "duplicate_of_candidate_ref": duplicate_of,
            "comparison_count": len(ordered_peers),
            "fingerprint": duplicate_fingerprint,
        },
        "rights": {
            "profile_id": RIGHTS_PROFILE_ID,
            "input_license": _text(source.get("license")),
            "license_class": license_class,
            "disposition": rights_disposition,
            "reason_codes": sorted(set(rights_reasons)),
        },
        "sensitivity": {
            "exact_geometry_present": exact,
            "source_hints": sensitivity_hints,
            "disposition": sensitivity_disposition,
            "reason_codes": sorted(set(sensitivity_reasons)),
        },
        "decision": {
            "outcome": outcome,
            "reason_codes": sorted(set(decision_reasons)),
            "canonical_candidate_ref": duplicate_of,
            "proposed_target_lifecycle": target,
        },
        "provenance": {
            "candidate_digest": candidate_hash,
            "peer_set_digest": peer_set_digest,
            "engine_id": ENGINE_ID,
            "engine_version": ENGINE_VERSION,
        },
        "governance": {
            "source_admission_decided": False,
            "legal_rights_decided": False,
            "policy_evaluated": False,
            "review_completed": False,
            "lifecycle_transition_executed": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
            "public_use_allowed": False,
            "release_ref": None,
        },
    }
    decision["spec_hash"] = decision_spec_hash(decision)
    return DecisionResult(outcome, (), decision)


def classify_files(candidate_path: Path, peers_path: Path | None = None) -> DecisionResult:
    candidate, candidate_findings = read_json(candidate_path)
    if candidate_findings:
        return DecisionResult("ERROR", candidate_findings)
    if not isinstance(candidate, dict):
        return DecisionResult("ERROR", (Finding("CANDIDATE_NOT_OBJECT", "/"),))
    peers: list[Mapping[str, Any]] = []
    if peers_path is not None:
        raw_peers, peer_findings = read_json(peers_path)
        if peer_findings:
            return DecisionResult("ERROR", peer_findings)
        if not isinstance(raw_peers, list) or any(not isinstance(item, dict) for item in raw_peers):
            return DecisionResult("ERROR", (Finding("PEER_SET_NOT_ARRAY_OF_OBJECTS", "/peers"),))
        peers = raw_peers
    return classify_candidate(candidate, peers)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize_result(path: Path, result: DecisionResult) -> str:
    return json.dumps(
        {
            "decision": result.decision,
            "file": _display_path(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def run_fixture_profile(root: Path) -> int:
    try:
        manifest = json.loads((root / "expected_outcomes.json").read_text(encoding="utf-8"))
        cases = manifest["cases"]
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError):
        print('{"outcome":"FIXTURE_MANIFEST_INVALID"}', file=sys.stderr)
        return 1
    passed = True
    for case in cases:
        candidate_rel = case["candidate"]
        peers_rel = case.get("peers")
        result = classify_files(root / candidate_rel, root / peers_rel if peers_rel else None)
        print(serialize_result(root / candidate_rel, result))
        actual_findings = sorted({item.code for item in result.findings})
        if result.outcome != case["outcome"] or actual_findings != sorted(case.get("findings", [])):
            passed = False
            print(
                json.dumps(
                    {
                        "actual_findings": actual_findings,
                        "actual_outcome": result.outcome,
                        "expected_findings": sorted(case.get("findings", [])),
                        "expected_outcome": case["outcome"],
                        "file": candidate_rel,
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
        expected_rel = case.get("expected_decision")
        if isinstance(expected_rel, str):
            try:
                expected = json.loads((root / expected_rel).read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError):
                expected = None
            if result.decision != expected:
                passed = False
                print(
                    json.dumps(
                        {"file": candidate_rel, "outcome": "FIXTURE_DECISION_MISMATCH"},
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                    file=sys.stderr,
                )
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Classify one Flora occurrence WORK candidate.")
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--peers", type=Path)
    parser.add_argument("--fixtures", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures is not None:
        if args.candidate is not None or args.peers is not None:
            print("--fixtures cannot be combined with candidate arguments", file=sys.stderr)
            return 2
        return run_fixture_profile(args.fixtures)
    if args.candidate is None:
        print("candidate or --fixtures is required", file=sys.stderr)
        return 2
    result = classify_files(args.candidate, args.peers)
    print(serialize_result(args.candidate, result))
    return 2 if result.outcome == "ERROR" else 0


if __name__ == "__main__":
    raise SystemExit(main())
