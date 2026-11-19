"""Bounded local GBIF Darwin Core intake rehearsal; CLI emits aggregate status only.

Compose the existing Flora normalizer, schemas and intake classifier. No API
retrieval, taxonomy inference, lifecycle writes or release decisions occur.
The CLI accepts only two committed synthetic fixtures; library callers own the
provenance and private handling of their supplied bytes and in-memory results.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes
from packages.domains.flora.normalizers import dwc_occurrence, intake_governance
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[3]
MAX_BYTES = 1024 * 1024
MAX_RECORDS = 300
FIXTURES = {"big-bluestem": "gbif_big_bluestem.json", "no-coordinate": "gbif_no_coordinate.json"}


@dataclass(frozen=True)
class BatchResult:
    candidates: tuple[dict, ...] = field(repr=False)
    decisions: tuple[dict, ...] = field(repr=False)
    issues: tuple[tuple[int, str], ...]

    def summary(self) -> dict:
        outcomes = [decision["decision"]["outcome"] for decision in self.decisions]
        return {
            "outcome": ("PARTIAL" if self.candidates else "ERROR") if self.issues else "REVIEW_REQUIRED",
            "normalized": len(self.candidates), "invalid": len({index for index, _ in self.issues}),
            "quarantined": sum(d["rights"]["disposition"] == "QUARANTINE" for d in self.decisions),
            "held": sum(d["sensitivity"]["disposition"] != "NO_SPECIAL_HANDLING" for d in self.decisions),
            "duplicates": outcomes.count("DEDUPLICATE"),
            "proposed_for_work": outcomes.count("ACCEPT_FOR_WORK"),
            "result_digest": digest_bytes(canonical_bytes({
                "candidates": self.candidates, "decisions": self.decisions, "issues": self.issues})),
            "source_admitted": False, "review_completed": False,
            "lifecycle_transition_executed": False, "promotion_authorized": False,
            "release_authorized": False, "publication_authorized": False,
            "public_use_allowed": False,
        }


def _validator(name: str) -> Draft202012Validator:
    schema = json.loads((ROOT / "schemas/contracts/v1/domains/flora" / (name + ".schema.json")).read_text())
    return Draft202012Validator(schema, format_checker=FormatChecker())


def prepare_records(raw: bytes) -> BatchResult:
    """Normalize bounded records to private candidates and proposed intake decisions.

    Reject a malformed batch or duplicate source identity as a whole. Individual
    record failures remain explicit by input index; valid siblings are retained.
    No candidate or decision is approved by this function. Schema validation
    precedes intake, including the existing exact-geometry and rights holds.
    """
    packet = decode_object(raw, limit=MAX_BYTES)
    records = packet.get("records")
    if (set(packet) != {"records"} or not isinstance(records, list)
            or not 1 <= len(records) <= MAX_RECORDS or any(not isinstance(record, dict) for record in records)):
        raise ValueError("GBIF_BATCH_SHAPE_INVALID")
    candidate_validator = _validator("flora_occurrence_candidate")
    decision_validator = _validator("flora_occurrence_intake_decision")
    candidates, decisions, issues, seen, normalized_records = [], [], [], set(), []
    for index, record in enumerate(records):
        normalized = dwc_occurrence.normalize_record(record, source_profile="GBIF_DWC", source_id="gbif")
        if not normalized.ok:
            issues.extend((index, finding.code) for finding in normalized.findings)
            continue
        candidate = dict(normalized.candidate)
        if not candidate_validator.is_valid(candidate):
            issues.append((index, "FLORA_CANDIDATE_SCHEMA_INVALID"))
            continue
        identity = candidate["candidate_id"]
        if identity in seen:
            raise ValueError("GBIF_DUPLICATE_SOURCE_IDENTITY")
        seen.add(identity)
        normalized_records.append((index, candidate))
    # Stable candidate identity selects the same proposed duplicate target even
    # when the caller supplies the source records in a different order.
    for index, candidate in sorted(normalized_records, key=lambda item: item[1]["candidate_id"]):
        classified = intake_governance.classify_candidate(candidate, peers=candidates)
        if not classified.ok or not decision_validator.is_valid(classified.decision):
            issues.append((index, "FLORA_INTAKE_DECISION_INVALID"))
            continue
        candidates.append(candidate)
        decisions.append(dict(classified.decision))
    return BatchResult(tuple(candidates), tuple(decisions), tuple(sorted(issues)))


def replay_fixture(name: str) -> BatchResult:
    if name not in FIXTURES:
        raise ValueError("GBIF_FIXTURE_UNKNOWN")
    path = ROOT / "fixtures/domains/flora/flora_occurrence_candidate/input" / FIXTURES[name]
    record = decode_object(read_regular(path, MAX_BYTES), limit=MAX_BYTES)
    return prepare_records(canonical_bytes({"records": [record]}))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", choices=sorted(FIXTURES))
    args = parser.parse_args(argv)
    try:
        summary = replay_fixture(args.fixture).summary()
    except (ValueError, OSError):
        print(canonical_bytes({"outcome": "ERROR", "reason": "GBIF_FIXTURE_REPLAY_FAILED"}).decode(), file=sys.stderr)
        return 1
    print(canonical_bytes(summary).decode())
    return 1 if summary["invalid"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
