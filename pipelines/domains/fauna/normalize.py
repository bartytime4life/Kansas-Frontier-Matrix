#!/usr/bin/env python3
"""Offline Fauna normalization rehearsal; stdout contains aggregate status only.

This entrypoint reads explicitly named local inputs. It never writes lifecycle
stores, emits occurrence payloads, fetches sources, or promotes/releases data.
Applications may call normalize_batch and retain its internal results under
their separately governed storage and access controls.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence

from jsonschema import FormatChecker

ROOT = Path(__file__).resolve().parents[3]
for source in (ROOT / "packages/hashing/src", ROOT / "packages/domains/fauna/src"):
    if str(source) not in sys.path:
        sys.path.insert(0, str(source))

from fauna import NormalizationResult, TaxonomyCatalog, normalize_occurrence
from hashing import JsonInputError, load_json_file

SCHEMAS = ROOT / "schemas/contracts/v1/domains/fauna"
MAX_BATCH_RECORDS = 1000


@dataclass(frozen=True)
class BatchResult:
    results: tuple[NormalizationResult, ...] = field(repr=False)

    def summary(self) -> dict[str, Any]:
        errors = sum(result.outcome == "error" for result in self.results)
        denied = sum(result.outcome == "deny" for result in self.results)
        return {
            "status": "ERROR" if errors else "DENIED" if denied else "HELD" if self.results else "EMPTY",
            "processed": len(self.results),
            "normalized": sum(result.occurrence is not None for result in self.results),
            "quarantined": sum(result.outcome == "quarantine" for result in self.results),
            "errors": errors,
            "denied": denied,
            "public_ready": False,
            "scope": "local-normalization-rehearsal",
        }


def normalize_batch(
    records: object, *, taxonomy: TaxonomyCatalog,
    schema: Mapping[str, Any], validated_at: str,
) -> BatchResult:
    if not isinstance(records, list) or len(records) > MAX_BATCH_RECORDS:
        raise ValueError("schema.batch_invalid")
    if not isinstance(validated_at, str) or not FormatChecker().conforms(validated_at, "date-time"):
        raise ValueError("schema.validation_time_invalid")
    # Preserve ordering and every source record. The compatibility occurrence
    # digest is not a global or cross-source deduplication key.
    return BatchResult(tuple(
        normalize_occurrence(
            record, taxonomy=taxonomy, schema=schema, validated_at=validated_at
        ) for record in records
    ))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path,
                        help="Local draft OccurrenceEvidence object or array (max 1000).")
    parser.add_argument("--taxonomy", required=True, type=Path,
                        help="Local candidate taxonomy snapshot, not a live authority URL.")
    parser.add_argument("--validated-at", required=True,
                        help="Explicit RFC3339 validation time; never observation time.")
    args = parser.parse_args(argv)
    try:
        schema = load_json_file(SCHEMAS / "occurrence_evidence.schema.json")
        taxonomy_schema = load_json_file(SCHEMAS / "taxonomy_snapshot.schema.json")
        taxonomy = TaxonomyCatalog.from_candidate(
            load_json_file(args.taxonomy), schema=taxonomy_schema
        )
        records = load_json_file(args.input)
        if isinstance(records, dict):
            records = [records]
        batch = normalize_batch(
            records, taxonomy=taxonomy, schema=schema, validated_at=args.validated_at
        )
    except (JsonInputError, OSError, UnicodeError, ValueError, TypeError, RecursionError):
        # Neither file paths, names, coordinates nor parser messages are logged.
        print(json.dumps({"status": "ERROR", "code": "fauna.input_invalid", "public_ready": False}))
        return 2
    print(json.dumps(batch.summary(), sort_keys=True))
    return 1 if batch.summary()["errors"] or batch.summary()["denied"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
