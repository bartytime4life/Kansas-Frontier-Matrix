#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "policy/decision/reviewer_roles.v1.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/policy_reviewer_role_vocabulary/cases.json"

ALLOWED_SCOPES = {"domain", "evidence", "policy", "release", "security_privacy"}
AUTHORITY_FLAGS = {"assigns_people", "records_approval", "policy_authorized", "promotion_authorized", "release_authorized", "publication_authorized"}
# The workflow runs only this validator, so it also enforces the schema's shape: no extra keys anywhere
# (a role must not carry authority or a named person), the fixed identity and inactive status, and code form.
IDENTITY = {"object_type": "PolicyReviewerRoleVocabulary", "vocabulary_id": "policy-reviewer-role-vocabulary:v1",
            "version": "v1", "status": "PROPOSED_INACTIVE"}
ROLE_KEYS = {"code", "review_scopes", "description"}
CODE = re.compile(r"[A-Z][A-Z0-9_]{2,95}")


def validate(record):
    if not isinstance(record, dict):
        return "ERROR"
    roles = record.get("roles")
    governance = record.get("governance")
    if not isinstance(roles, list) or not roles or not isinstance(governance, dict):
        return "DENY"
    if set(record) != set(IDENTITY) | {"roles", "governance"} or any(record[k] != v for k, v in IDENTITY.items()):
        return "DENY"
    codes = []
    aliases = []
    for role in roles:
        # "aliases" is the contract's optional synonym list; overlapping aliases fail validation.
        if not isinstance(role, dict) or not ROLE_KEYS <= set(role) <= ROLE_KEYS | {"aliases"}:
            return "DENY"
        code, scopes, description = role["code"], role["review_scopes"], role["description"]
        if not isinstance(code, str) or not CODE.fullmatch(code) or not isinstance(description, str) or not 1 <= len(description) <= 240:
            return "DENY"
        if not isinstance(scopes, list) or not scopes or not all(isinstance(scope, str) for scope in scopes):
            return "DENY"
        if scopes != sorted(set(scopes)) or any(scope not in ALLOWED_SCOPES for scope in scopes):
            return "DENY"
        role_aliases = role.get("aliases", [])
        if not isinstance(role_aliases, list) or not all(isinstance(alias, str) and alias for alias in role_aliases):
            return "DENY"
        codes.append(code)
        aliases.extend(role_aliases)
    if codes != sorted(codes) or len(codes) != len(set(codes)):
        return "DENY"
    # Checked after every code is known, so an alias cannot shadow a role defined later in the list.
    if len(aliases) != len(set(aliases)) or set(aliases) & set(codes):
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
