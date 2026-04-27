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


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python tools/attest/verify_decision_envelope.py",
        description="Verify a deterministic KFM decision-envelope signing result artifact.",
    )
    parser.add_argument("artifact_uri", help="Artifact URI expected to match the sign result.")
    parser.add_argument("--decision", default="decision.json", help="Path to decision envelope JSON.")
    parser.add_argument(
        "--sign-result",
        default="decision-sign-result.json",
        help="Path to decision-sign-result JSON produced by sign_decision_envelope.py.",
    )
    parser.add_argument("--output", required=True, help="Output path for decision-verify-result JSON.")
    parser.add_argument(
        "--key-env",
        default="KFM_ATTEST_SIGNING_KEY",
        help="Environment variable containing signing key material.",
    )
    return parser


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("expected JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    decision_path = Path(args.decision)
    sign_result_path = Path(args.sign_result)
    output_path = Path(args.output)

    if not decision_path.exists():
        print(f"missing decision: {decision_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT
    if not sign_result_path.exists():
        print(f"missing sign result: {sign_result_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    try:
        decision = load_json(decision_path)
        sign_result = load_json(sign_result_path)

        decision_digest = sha256_hex(canonical_json(decision))
        signer = str(sign_result.get("signature", {}).get("signer", ""))
        signature_value = str(sign_result.get("signature", {}).get("value", ""))
        key_material = os.environ.get(args.key_env, "")

        expected_signature = sha256_hex(f"{args.artifact_uri}\n{decision_digest}\n{signer}\n{key_material}")

        checks = {
            "artifact_uri_match": sign_result.get("artifact_uri") == args.artifact_uri,
            "decision_sha256_match": sign_result.get("decision_sha256") == decision_digest,
            "signature_match": signature_value == expected_signature,
            "result_type_match": sign_result.get("result_type") == "kfm:DecisionEnvelopeSignResult",
        }
        verified = all(checks.values())

        verify_result = {
            "result_type": "kfm:DecisionEnvelopeVerifyResult",
            "status": "verified" if verified else "verification_failed",
            "verified": verified,
            "artifact_uri": args.artifact_uri,
            "decision_path": str(decision_path),
            "sign_result_path": str(sign_result_path),
            "decision_sha256": decision_digest,
            "checks": checks,
            "checked_at": utc_now_iso(),
            "tool": "tools/attest/verify_decision_envelope.py",
        }
        write_json(output_path, verify_result)
    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except Exception as exc:
        print(f"verify error: {exc}", file=sys.stderr)
        return EXIT_FAILURE

    if verify_result["verified"]:
        print(f"decision verification: verified ({output_path})")
        return EXIT_PASS

    print(f"decision verification: failed ({output_path})", file=sys.stderr)
    return EXIT_FAILURE


if __name__ == "__main__":
    raise SystemExit(main())
