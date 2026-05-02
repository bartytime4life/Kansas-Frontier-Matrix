#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator




def replay(bundle: dict, policy_input: dict) -> str:
    for rule in bundle.get("rules", []):
        cond = rule.get("if")
        if cond:
            if "review_complete" in cond and policy_input.get("review_complete") != cond["review_complete"]:
                continue
            if "risk_score_max" in cond and policy_input.get("risk_score", 10**9) > cond["risk_score_max"]:
                continue
            return rule.get("then", "deny")
        if "else" in rule:
            return rule["else"]
    return "deny"


def canonical_hash(path: Path) -> str:
    obj = json.loads(path.read_text(encoding="utf-8"))
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256-" + hashlib.sha256(blob).hexdigest()


def fixture_to_path(url: str) -> Path:
    return Path("tests") / url.replace("fixtures://", "fixtures/")


def validate(decision_log_path: Path, run_receipt_path: Path, bundle_path: Path, input_path: Path) -> dict:
    checks, errors = [], []
    schema = json.loads(Path("schemas/governance/decision_log.schema.json").read_text(encoding="utf-8"))
    log = json.loads(decision_log_path.read_text(encoding="utf-8"))
    receipt = json.loads(run_receipt_path.read_text(encoding="utf-8"))
    policy_bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    schema_ok = True
    for e in Draft202012Validator(schema).iter_errors(log):
        schema_ok = False
        errors.append(f"schema:{e.message}")
    checks.append({"name": "schema", "ok": schema_ok})

    spec_ok = log.get("input_ref", {}).get("kfm", {}).get("spec_hash") == canonical_hash(input_path)
    checks.append({"name": "spec_hash_determinism", "ok": spec_ok})
    if not spec_ok:
        errors.append("spec_hash mismatch")

    receipt_ok = (
        log.get("input_ref", {}).get("run_receipt_id") == receipt.get("run_receipt_id")
        and log.get("input_ref", {}).get("kfm", {}).get("spec_hash") == receipt.get("spec_hash")
    )
    checks.append({"name": "run_receipt_link", "ok": receipt_ok})
    if not receipt_ok:
        errors.append("run_receipt mismatch")

    bundle_ok = log.get("policy_bundle", {}).get("bundle_spec_hash") == canonical_hash(bundle_path)
    checks.append({"name": "policy_bundle_hash", "ok": bundle_ok})
    if not bundle_ok:
        errors.append("policy_bundle hash mismatch")

    sig_url = log.get("signature", {}).get("dsse", {}).get("cosign_bundle_url", "")
    signature_ok = bool(sig_url) and fixture_to_path(sig_url).exists()
    checks.append({"name": "signature_bundle_presence", "ok": signature_ok})
    if not signature_ok:
        errors.append("signature bundle missing")

    replay_result = replay(policy_bundle, json.loads(input_path.read_text(encoding="utf-8")))
    replay_ok = replay_result == log.get("result")
    checks.append({"name": "policy_replay", "ok": replay_ok})
    if not replay_ok:
        errors.append("replay result mismatch")

    ok = all(c["ok"] for c in checks)
    return {
        "ok": ok,
        "decision_id": log.get("decision_id", ""),
        "checks": checks,
        "errors": errors,
        "replay": {
            "expected_result": log.get("result"),
            "actual_result": replay_result,
            "result_match": replay_ok,
        },
    }


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("usage: validate_decision_log.py <decision_log.json> <run_receipt.json> <policy_bundle.json> <policy_input.json>")
        raise SystemExit(2)
    out = validate(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))
    raise SystemExit(0 if out["ok"] else 1)
