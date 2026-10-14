"""Audited, bounded private-review transfer. Never a released data carrier."""
import base64
import json
from pathlib import Path

from .land_records import MAX_BYTES, canonical, digest, stamp
from .land_store import audit, connection, evidence_bundle, immutable, read_file

PROFILE = "kfm.land-review-transfer/v1"


def export_review(root, destination, *, capture_ids=()):
    """Export active captures and their original bytes after deterministic replay.

    No credential, withdrawn occurrence or release decision enters the bundle.
    Explicit destination must be outside every Git checkout. Receipts retained
    locally remain authority for replay; the browser verifies integrity only.
    """
    root, destination = Path(root), Path(destination)
    if any((p / ".git").is_file() or (p / ".git/HEAD").is_file() for p in (destination.parent, *destination.parents)):
        raise ValueError("TRANSFER_MUST_BE_OUTSIDE_GIT")
    audit(root)
    q = root / "data/quarantine/land-records"
    objects, captures = {}, []
    wanted = set(capture_ids)
    if len(wanted) > 20:
        raise ValueError("TRANSFER_CAPTURE_LIMIT")
    with connection(root, readonly=True) as db:
        selection = " AND c.id IN (" + ",".join("?" for _ in wanted) + ")" if wanted else ""
        rows = db.execute("SELECT r.receipt FROM runs r JOIN captures c ON c.id=json_extract(r.receipt, '$.capture_id') WHERE NOT EXISTS (SELECT 1 FROM controls x WHERE x.capture_id=c.id)" + selection + " ORDER BY c.id LIMIT 21", sorted(wanted)).fetchall()
        if len(rows) > 20:
            raise ValueError("TRANSFER_CAPTURE_LIMIT")
        for row in rows:
            receipt = json.loads(row[0])
            if wanted and receipt["capture_id"] not in wanted:
                continue
            manifest = json.loads(read_file(q / "captures" / (receipt["capture_id"][7:] + ".json")))
            candidate = json.loads(read_file(q / "candidates" / (receipt["candidate_id"][7:] + ".json")))
            members = {manifest["payload_sha256"], *(d["sha256"] for d in manifest["documents"])}
            content = {key: read_file(q / "objects" / key[7:]) for key in members}
            objects.update({key: base64.b64encode(raw).decode("ascii") for key, raw in content.items()})
            captures.append({"manifest": manifest, "candidate": candidate,
                             "evidence": [evidence_bundle(r, manifest, candidate, {k: len(v) for k, v in content.items()}) for r in candidate["records"]]})
    if not captures or wanted - {c["manifest"]["capture_id"] for c in captures}:
        raise ValueError("ACTIVE_CAPTURE_REQUIRED")
    if sum(len(c["candidate"]["records"]) for c in captures) > 1000:
        raise ValueError("TRANSFER_RECORD_LIMIT")
    value = {"profile": PROFILE, "created_at": stamp(), "authority": "PRIVATE_REVIEW_ONLY",
             "review_state": "PENDING", "release_state": "UNRELEASED", "captures": captures, "objects": objects}
    value["transfer_digest"] = digest(canonical(value))
    raw = canonical(value)
    if len(raw) > MAX_BYTES:
        raise ValueError("TRANSFER_BYTE_LIMIT")
    immutable(destination, raw)
    return {"outcome": "EXPORTED", "captures": len(captures), "records": sum(len(c["candidate"]["records"]) for c in captures),
            "bytes": len(raw), "transfer_digest": value["transfer_digest"], "authority": "PRIVATE_REVIEW_ONLY", "release_state": "UNRELEASED"}
