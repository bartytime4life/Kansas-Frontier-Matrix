from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .evidence_ref_resolver import resolve_evidence_ref_from_file


EXIT_PASS = 0
EXIT_ABSTAIN = 1
EXIT_MISSING_INPUT = 2
EXIT_MISSING_SCHEMA = 3
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m packages.evidence",
        description="Resolve a KFM EvidenceRef and emit a cite-or-abstain result.",
    )

    parser.add_argument(
        "--evidence-ref",
        required=True,
        help="Path to the evidence_ref JSON object to resolve.",
    )

    parser.add_argument(
        "--schema",
        default="schemas/contracts/v1/evidence/evidence_ref.schema.json",
        help="Path to the evidence_ref schema.",
    )

    parser.add_argument(
        "--expected-digest",
        default=None,
        help="Expected sha256 digest (format: sha256:<hex>) for integrity verification.",
    )

    parser.add_argument(
        "--out",
        default=None,
        help="Optional path to write the resolution result as JSON.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    evidence_ref_path = Path(args.evidence_ref)
    schema_path = Path(args.schema)

    if not evidence_ref_path.exists():
        print(f"missing evidence-ref input: {evidence_ref_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    if not schema_path.exists():
        print(f"missing schema: {schema_path}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA

    try:
        result = resolve_evidence_ref_from_file(
            evidence_ref_path=evidence_ref_path,
            schema_path=schema_path,
            expected_digest=args.expected_digest,
        )
    except Exception as exc:
        print(f"internal error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    output = {
        "evidence_ref_id": result.evidence_ref_id,
        "render": result.render,
        "decision": result.decision,
        "error_code": result.error_code,
        "reason": result.reason,
        "release_state": result.release_state,
    }

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(output, indent=2) + "\n",
            encoding="utf-8",
        )

    if result.render:
        print(f"cite: {result.evidence_ref_id}")
        return EXIT_PASS
    else:
        print(
            f"abstain: {result.evidence_ref_id} [{result.error_code}]: {result.reason}",
            file=sys.stderr,
        )
        return EXIT_ABSTAIN


if __name__ == "__main__":
    raise SystemExit(main())
