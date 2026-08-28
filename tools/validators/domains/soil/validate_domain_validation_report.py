#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CASES = ROOT / "fixtures/domains/soil/domain_validation_report/cases.json"
PROFILE = "kfm.domains.soil.domain-validation-report.v1"
FALSE_EFFECTS = {
    "evidence_admitted": False,
    "policy_approved": False,
    "promoted": False,
    "released": False,
    "deployed": False,
    "published": False,
}


def canonical_hash(candidate: dict) -> str:
    payload = dict(candidate)
    payload.pop("id", None)
    payload.pop("spec_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def evaluate(candidate: dict) -> tuple[str, list[str]]:
    findings: list[str] = []
    if candidate.get("profile") != PROFILE or candidate.get("status") != "PROPOSED_INACTIVE":
        findings.append("PROFILE_MISMATCH")
    if candidate.get("domain") != "soil" or candidate.get("version") != "1.0.0":
        findings.append("IDENTITY_PROFILE_MISMATCH")
    if not candidate.get("subject_ref") or not candidate.get("validator_ref"):
        findings.append("BINDING_MISSING")
    input_refs = candidate.get("input_refs")
    if not isinstance(input_refs, list) or not input_refs or input_refs != sorted(set(input_refs)):
        findings.append("NONCANONICAL_INPUT_REFS")
    report_findings = candidate.get("findings")
    if not isinstance(report_findings, list):
        findings.append("FINDINGS_INVALID")
    else:
        normalized = [(item.get("code"), item.get("severity")) for item in report_findings if isinstance(item, dict)]
        if normalized != sorted(set(normalized)):
            findings.append("NONCANONICAL_FINDINGS")
        outcome = candidate.get("outcome")
        if outcome == "PASS" and report_findings:
            findings.append("PASS_HAS_FINDINGS")
        if outcome in {"FAIL", "HOLD", "ERROR"} and not report_findings:
            findings.append("NONPASS_MISSING_FINDINGS")
    if candidate.get("public_use_allowed") is not False:
        findings.append("PUBLIC_USE_OVERCLAIM")
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append("EFFECT_OVERCLAIM")
    digest = canonical_hash(candidate)
    if candidate.get("spec_hash") != f"sha256:{digest}":
        findings.append("SPEC_HASH_MISMATCH")
    if candidate.get("id") != f"soil-validation:{digest[:24]}":
        findings.append("ID_MISMATCH")
    findings = sorted(set(findings))
    if findings:
        return ("DENY" if any(item in {"PUBLIC_USE_OVERCLAIM", "EFFECT_OVERCLAIM"} for item in findings) else "ERROR", findings)
    return "PASS", []


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args()
    if args.fixtures:
        cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
        failures = 0
        for case in cases:
            outcome, findings = evaluate(case["candidate"])
            print(json.dumps({"name": case["name"], "outcome": outcome, "findings": findings}, sort_keys=True))
            failures += outcome != case["expected_outcome"] or findings != case["expected_findings"]
        raise SystemExit(1 if failures else 0)
    if not args.path:
        parser.error("path or --fixtures required")
    outcome, findings = evaluate(json.loads(Path(args.path).read_text(encoding="utf-8")))
    print(json.dumps({"outcome": outcome, "findings": findings}, sort_keys=True))
    raise SystemExit(0 if outcome == "PASS" else 1)


if __name__ == "__main__":
    main()
