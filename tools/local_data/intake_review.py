"""Explicit, digest-bound operator decisions for the private intake desk."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re
import uuid

from tools.local_data import intake_route
from tools.local_data.file_io import hash_regular, write_new
from tools.local_data.manage import canonical, utc_now

DOMAINS = ("agriculture", "archaeology", "atmosphere", "fauna", "flora", "geology", "habitat", "hazards",
           "hydrology", "people-dna-land", "roads-rail-trade", "settlements-infrastructure", "soil")
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS item_reviews (
  revision INTEGER PRIMARY KEY AUTOINCREMENT, item_id TEXT NOT NULL, sha256 TEXT NOT NULL,
  basis TEXT NOT NULL, review_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS item_reviews_item ON item_reviews(item_id, revision);
"""
FIELDS = {"id", "sha256", "revision", "decision", "domain", "rights", "sensitivity", "reference", "reviewer", "note", "confirmed"}


def _text(value, maximum, minimum=0):
    return (isinstance(value, str) and minimum <= len(value.strip()) <= maximum
            and not any(ord(c) < 32 and c != "\n" or ord(c) == 127 for c in value))


def basis(item, profile):
    declared = {k: v for k, v in (item.get("declared") or {}).items() if k != "binding_count"}
    return hashlib.sha256(canonical({"declared": declared, "profile": {k: profile.get(k) for k in
        ("analyzer_version", "format", "hints", "issues")}})).hexdigest()


def history(conn, identity):
    # Imported catalog snapshots remain immutable and can predate this feature.
    if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='item_reviews'").fetchone():
        return []
    rows = conn.execute("SELECT revision, review_json FROM item_reviews WHERE item_id=? ORDER BY revision DESC LIMIT 50", (identity,))
    return [{**json.loads(body), "revision": revision} for revision, body in rows]


def has_review(conn, identity):
    return conn.execute("SELECT 1 FROM item_reviews WHERE item_id=? LIMIT 1", (identity,)).fetchone() is not None


def current(conn, item, profile):
    row = conn.execute("SELECT revision, sha256, basis, review_json FROM item_reviews WHERE item_id=? ORDER BY revision DESC LIMIT 1", (item["id"],)).fetchone()
    if row is None or row[1] != item.get("sha256") or row[2] != basis(item, profile):
        return None
    value = {**json.loads(row[3]), "revision": row[0]}
    return value if value["decision"] != "reopen" else None


def route(item, profile, budget, review):
    if review is None:
        return intake_route.decide(item, profile, budget)
    p, effective = deepcopy(profile), dict(item)
    hints = p.setdefault("hints", {})
    # decide() derives sensitive_domain from the routing domain, so carry the analyzed domain's flag
    # forward: choosing another domain must not clear a sensitivity restriction.
    if hints.get("domain") in intake_route.REVIEW_DOMAINS:
        hints["review_flags"] = sorted(set(hints.get("review_flags", [])) | {"sensitive_domain"})
    hints["domain"] = review["domain"] or None
    declared = deepcopy(item.get("declared") or {})
    declared["rights"] = {"redistribution": review["rights"], "license_id": review["reference"] or None}
    declared["sensitivity"] = review["sensitivity"]
    effective["declared"] = declared
    result = intake_route.decide(effective, p, budget)
    if result["blocking_issues"]:
        raise ValueError("REVIEW_BLOCKED_FILE")
    if review["decision"] == "public":
        if result["status"] != "ready" or result["holds"]:
            raise ValueError("REVIEW_PUBLIC_HOLDS_REMAIN")
    else:
        result["status"] = "reviewed"
        for placement in result["placements"]:
            if placement["tier"] in {"git_repo", "github_release"}:
                placement.update(action="hold", reason="REVIEWED_LOCAL_ONLY")
                placement.pop("asset_parts", None)
        result["holds"] = sorted(set(result["holds"]) | {"REVIEWED_LOCAL_ONLY"})
    result["operator_review"] = review
    return result


def decision(conn, item, profile, budget):
    review = current(conn, item, profile)
    try:
        return route(item, profile, budget, review)
    except ValueError:
        # A previously accepted file can acquire new blockers or tighter budgets.
        return intake_route.decide(item, profile, budget)


def save(root: Path, value: dict, budget):
    from tools.local_data import intake

    if not isinstance(value, dict) or set(value) != FIELDS:
        raise ValueError("REVIEW_REQUEST_INVALID")
    identity = intake._validated_identity(value["id"])
    if not isinstance(value["sha256"], str) or not re.fullmatch(r"[a-f0-9]{64}", value["sha256"]):
        raise ValueError("REVIEW_DIGEST_REQUIRED")
    if type(value["revision"]) is not int or value["revision"] < 0 or value["confirmed"] is not True:
        raise ValueError("REVIEW_CONFIRMATION_REQUIRED")
    if any(not isinstance(value[k], str) for k in ("decision", "domain", "rights", "sensitivity", "reference", "reviewer", "note")):
        raise ValueError("REVIEW_FIELDS_INVALID")
    if (value["decision"] not in {"local", "public", "reopen"} or not isinstance(value["domain"], str)
            or value["domain"] not in ("", *DOMAINS)
            or value["rights"] not in {"unknown", "allowed", "restricted", "denied"}
            or value["sensitivity"] not in {"unknown", "public", "restricted", "controlled"}
            or not _text(value["reference"], 512) or not _text(value["reviewer"], 80, 1)
            or not _text(value["note"], 1600, 8)):
        raise ValueError("REVIEW_FIELDS_INVALID")
    if value["decision"] == "public" and (not value["domain"] or value["rights"] != "allowed"
            or value["sensitivity"] != "public" or not value["reference"].strip()):
        raise ValueError("REVIEW_PUBLIC_DETAILS_REQUIRED")
    with intake.writer_lock(root):
        item = intake.get_item(root, identity)
        if not item["present"] or item["lane"] == "inbox" or not item.get("store_path"):
            raise ValueError("REVIEW_CAPTURE_REQUIRED")
        if item["sha256"] != value["sha256"]:
            raise ValueError("REVIEW_STALE_FILE")
        source = item["store_path"]
        if (not source.startswith(("data/raw/", "data/quarantine/"))
                or ".." in Path(source).parts):
            raise ValueError("REVIEW_SOURCE_UNSAFE")
        digest, _ = hash_regular(root / source, intake.DEFAULT_HASH_LIMIT, expected_size=item["size_bytes"])
        if digest != value["sha256"]:
            raise ValueError("REVIEW_CONTENT_CHANGED_REANALYZE")
        declared = item.get("declared") or {}
        if value["decision"] == "public" and ((declared.get("rights") or {}).get("redistribution") in {"restricted", "denied"}
                or declared.get("sensitivity") in {"restricted", "controlled"}):
            raise ValueError("REVIEW_CAPTURE_RESTRICTION_REMAINS")
        review = {k: value[k].strip() if isinstance(value[k], str) else value[k]
                  for k in ("decision", "domain", "rights", "sensitivity", "reference", "reviewer", "note")}
        review.update(schema="kfm-intake-operator-review/v1", item_id=identity, sha256=digest, reviewed_at=utc_now(),
                      authority={"source_admission": False, "release": False, "publication": False})
        with intake.open_index(root) as conn:
            previous = history(conn, identity)
            if value["revision"] != (previous[0]["revision"] if previous else 0):
                raise ValueError("REVIEW_STALE_DECISION")
            if review["decision"] != "reopen":
                route(item, item["profile"], budget, review)  # Validate before creating a receipt.
            relative = f"data/receipts/intake/{identity}/review-{uuid.uuid4().hex}.json"
            review["receipt"] = relative
            review_basis = basis(item, item["profile"])
            cursor = conn.execute("INSERT INTO item_reviews(item_id, sha256, basis, review_json) VALUES (?,?,?,?)",
                                  (identity, digest, review_basis, json.dumps(review, sort_keys=True)))
            review["revision"] = cursor.lastrowid
            decision_value = route(item, item["profile"], budget, None if review["decision"] == "reopen" else review)
            conn.execute("UPDATE items SET decision_json=?, domain=?, status=? WHERE id=?",
                         (json.dumps(decision_value, sort_keys=True), decision_value["domain"], decision_value["status"], identity))
    return {"outcome": "REVIEW_SAVED", "status": decision_value["status"], "review": review}
