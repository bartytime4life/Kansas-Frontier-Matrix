#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "policy/decision/reviewer_roles.v1.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/policy_reviewer_role_vocabulary/cases.json"

ALLOWED_SCOPES = {"domain", "evidence", "policy", "release", "security_privacy"}
AUTHORITY_FLAGS = {"assigns_people", "records_approval", "policy_authorized", "promotion_authorized", "release_authorized", "publication_authorized"}


def validate(record):
    if not isinstance(record, dict):
        return "ERROR"
    roles = record.get("roles")
    governance = record.get("governance")
    if not isinstance(roles, list) or not roles or not isinstance(governance, dict):
        return "DENY"
    codes = []
    aliases = set()
    for role in roles:
        if not isinstance(role, dict):
            return "DENY"
        code = role.get("code")
        scopes = role.get("review_scopes")
        if not isinstance(code, str) or not code or not isinstance(scopes, list) or not scopes:
            return "DENY"
        if scopes != sorted(set(scopes)) or any(scope not in ALLOWED_SCOPES for scope in scopes):
            return "DENY"
        codes.append(code)
        for alias in role.get("aliases", []):
            if alias in aliases or alias in codes:
                return "DENY"
            aliases.add(alias)
    if codes != sorted(codes) or len(codes) != len(set(codes)):
        return "DENY"
    if set(governance) != AUTHORITY_FLAGS or any(governance[k] is not False for k in AUTHORITY_FLAGS):
        return "DENY"
    return "PASS"


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--registry", action="store_true")
    p.add_argument("--fixtures", action="store_true")
    args = p.parse_args()
    if args.registry:
        outcome = validate(json.loads(REGISTRY.read_text()))
        print(outcome)
        raise SystemExit(0 if outcome == "PASS" else 1)
    if args.fixtures:
        data = json.loads(FIXTURES.read_text())
        registry = json.loads(REGISTRY.read_text())
        failures = []
        for case in data["cases"]:
            record = registry if case.get("path") else case.get("record")
            got = validate(record)
            if got != case["expected"]:
                failures.append(f"{case['name']}: expected {case['expected']} got {got}")
        if failures:
            print("\n".join(failures))
            raise SystemExit(1)
        print(f"PASS {len(data['cases'])} cases")
        return
    p.error("choose --registry or --fixtures")


if __name__ == "__main__":
    main()
