#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EXIT_PASS = 0
EXIT_FAILURE = 1
EXIT_MISSING_INPUT = 2
EXIT_CONFIRM_REQUIRED = 4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python tools/attest/sign_decision_envelope.py",
        description="Create a deterministic KFM decision-envelope signing result artifact.",
    )
    parser.add_argument("decision", help="Path to decision envelope JSON.")
    parser.add_argument("--artifact-uri", required=True, help="Artifact URI bound to this signature.")
    parser.add_argument("--output", required=True, help="Output path for decision-sign-result JSON.")
    parser.add_argument("--signer", default="local-dev-signer", help="Signer identifier recorded in the result.")
    parser.add_argument(
        "--key-env",
        default="KFM_ATTEST_SIGNING_KEY",
        help="Environment variable containing signing key material.",
    )
    parser.add_argument("--yes", action="store_true", help="Acknowledge explicit signing intent.")
    return parser


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("decision envelope must be a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.yes:
        print("explicit confirmation required: pass --yes", file=sys.stderr)
        return EXIT_CONFIRM_REQUIRED

    decision_path = Path(args.decision)
    output_path = Path(args.output)

    if not decision_path.exists():
        print(f"missing decision: {decision_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    try:
        decision = load_json(decision_path)
        decision_digest = sha256_hex(canonical_json(decision))
        key_material = os.environ.get(args.key_env, "")
        signature = sha256_hex(f"{args.artifact_uri}\n{decision_digest}\n{args.signer}\n{key_material}")

        result = {
            "result_type": "kfm:DecisionEnvelopeSignResult",
            "status": "signed",
            "artifact_uri": args.artifact_uri,
            "decision_path": str(decision_path),
            "decision_sha256": decision_digest,
            "signature": {
                "alg": "sha256",
                "value": signature,
                "signer": args.signer,
                "key_source": f"env:{args.key_env}",
            },
            "signed_at": utc_now_iso(),
            "tool": "tools/attest/sign_decision_envelope.py",
        }
        write_json(output_path, result)
    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except Exception as exc:
        print(f"sign error: {exc}", file=sys.stderr)
        return EXIT_FAILURE

    print(f"decision signature: {output_path}")
    print(f"decision sha256: {decision_digest}")
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
