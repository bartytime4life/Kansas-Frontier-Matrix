#!/usr/bin/env python3
import argparse, hashlib, json, sys
from pathlib import Path
import jsonschema

FORBIDDEN_FIELDS = {"decimalLatitude", "decimalLongitude", "geometry", "raw_payload", "private_identifier", "dna_sequence", "token"}
ALLOWED_ACTIONS = {"SUPPRESS", "GENERALIZE", "DELETE"}
ACTION_OUTCOMES = {
    "SUPPRESS": {"SUPPRESSED", "APPLIED", "BLOCKED", "RECOMPUTE_REQUIRED"},
    "GENERALIZE": {"GENERALIZED", "APPLIED", "BLOCKED"},
    "DELETE": {"DELETED", "APPLIED", "BLOCKED"},
}


def canonical_hash(obj):
    return "sha256:" + hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def compute_id(obj):
    c = dict(obj)
    c.pop("id", None)
    return canonical_hash(c)


def load_schema(root, name):
    return json.loads((root / "schemas" / "governance" / name).read_text())


def validate_file(instance, schema, code, errors):
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except Exception as e:
        errors.append(f"{code}: {e.__class__.__name__}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--repo-root", default=Path(__file__).resolve().parents[3])
    args = ap.parse_args()

    root = Path(args.repo_root)
    data = json.loads(Path(args.bundle).read_text())
    errors = []

    oer_s = load_schema(root, "obligation_execution_receipt.schema.json")
    rq_s = load_schema(root, "recompute_queue_item.schema.json")
    per_s = load_schema(root, "publish_enforcement_report.schema.json")
    rir_s = load_schema(root, "revocation_impact_report.schema.json")

    for rec in data.get("obligation_execution_receipts", []):
        validate_file(rec, oer_s, "SCHEMA_OER", errors)
        if rec.get("id") != compute_id(rec):
            errors.append("HASH_MISMATCH: obligation_execution_receipt")
        if rec.get("spec_hash") != canonical_hash(rec.get("obligation_ref", {})):
            errors.append("SPEC_HASH_MISMATCH: obligation_execution_receipt")

    for rec in data.get("recompute_queue_items", []):
        validate_file(rec, rq_s, "SCHEMA_RQI", errors)
        if rec.get("id") != compute_id(rec):
            errors.append("HASH_MISMATCH: recompute_queue_item")

    rep = data.get("publish_enforcement_report", {})
    validate_file(rep, per_s, "SCHEMA_PER", errors)
    if rep.get("id") != compute_id(rep):
        errors.append("HASH_MISMATCH: publish_enforcement_report")

    rev = data.get("revocation_impact_report", {})
    validate_file(rev, rir_s, "SCHEMA_RIR", errors)
    if rev.get("id") != compute_id(rev):
        errors.append("HASH_MISMATCH: revocation_impact_report")

    obligations = data.get("obligations", [])
    receipts = {r["obligation_ref"]["obligation_id"]: r for r in data.get("obligation_execution_receipts", []) if "obligation_ref" in r}
    for ob in obligations:
        rid = ob["obligation_id"]
        if ob.get("action") not in ALLOWED_ACTIONS:
            errors.append("UNKNOWN_ACTION")
        if rid not in receipts:
            errors.append("MISSING_RECEIPT")
            continue
        rr = receipts[rid]
        action = ob["action"]
        if rr.get("execution", {}).get("outcome") not in ACTION_OUTCOMES.get(action, set()):
            errors.append("ACTION_OUTCOME_MISMATCH")
        refs = rr.get("receipt_refs", {})
        if action == "GENERALIZE" and not refs.get("redaction_receipt_id"):
            errors.append("MISSING_GENERALIZATION_RECEIPT")
        if action == "DELETE" and not refs.get("deletion_receipt_id"):
            errors.append("MISSING_DELETION_RECEIPT")

    if any(data.get("consent_revoked_subject_ids", [])):
        allowed = {"SUPPRESSED", "RECOMPUTE_REQUIRED", "BLOCKED"}
        if not any(r.get("execution", {}).get("outcome") in allowed for r in data.get("obligation_execution_receipts", [])):
            errors.append("REVOKED_CONSENT_NOT_ENFORCED")

    if data.get("retention_expired") and rep.get("publish_decision") == "ALLOW":
        errors.append("RETENTION_EXPIRED_PUBLISH_ALLOW")

    if rep.get("queue_summary", {}).get("unresolved_count", 0) > 0 and rep.get("publish_decision") == "ALLOW":
        errors.append("UNRESOLVED_RECOMPUTE_QUEUE")

    forbidden = set(data.get("public_artifact_fields", [])) & FORBIDDEN_FIELDS
    if forbidden:
        errors.append("FORBIDDEN_PUBLIC_FIELDS")

    run = data.get("run_receipt", {})
    if not run.get("signed") or not run.get("verified"):
        errors.append("RUN_RECEIPT_UNVERIFIED")

    if errors:
        print(json.dumps({"ok": False, "errors": sorted(set(errors))}, indent=2))
        return 1
    print(json.dumps({"ok": True}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
