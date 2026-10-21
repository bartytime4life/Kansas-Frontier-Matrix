"""Private SQLite rehearsal, explicitly NOT the hosted MySQL migration/engine.

Only metadata from an inspected FAA capture is processed; no live DB writes.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sqlite3
import time

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("faa_airports", ROOT / "pipelines/domains/roads-rail-trade/faa_airports.py")
faa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(faa)


def inspect_selection(candidate, revision_id):
    """Private review chain only. Never a public report or released evidence."""
    matches = [r for r in candidate["records"] if r["revision_id"] == revision_id]
    if len(matches) != 1:
        raise ValueError("SELECTION_NOT_FOUND")
    record = matches[0]
    bundle = record["bundle"]
    subject = {k: v for k, v in bundle.items() if k != "spec_hash"}
    if bundle["spec_hash"]["value"] != faa.sha(faa.canonical(subject)) or record["evidence_ref"] not in bundle["evidence_refs"]:
        raise ValueError("EVIDENCE_DIGEST_MISMATCH")
    return {"release_state": "HELD", "entity_id": record["entity_id"], "revision_id": revision_id,
            "evidence_ref": record["evidence_ref"], "bundle": bundle,
            "report": "PRIVATE REVIEW DRAFT - HELD\n" + record["name"] + "\nReference edition: " + record["edition"]
                      + "\nEvidence: " + record["evidence_ref"]["ref"] + "\nSource: " + bundle["citations"][0]
                      + "\nResearch/context only; not for navigation or flight planning. No release or public-use claim."}


def rehearse(candidate, database):
    """Isolated caller-owned test database; a retry cannot overwrite a revision."""
    with sqlite3.connect(database) as db:
        db.execute("CREATE TABLE IF NOT EXISTS faa_candidate (candidate TEXT, revision TEXT, state TEXT, county TEXT, record TEXT, PRIMARY KEY(candidate,revision))")
        db.execute("CREATE INDEX IF NOT EXISTS faa_county ON faa_candidate(candidate,state,county,revision)")
        rows = [(candidate["candidate_id"], r["revision_id"], r["state"], r["county_name"], json.dumps(r)) for r in candidate["records"]]
        before = db.total_changes
        db.executemany("INSERT OR IGNORE INTO faa_candidate VALUES(?,?,?,?,?)", rows)
        inserted = db.total_changes - before
        db.commit()
        start = time.perf_counter()
        sample = db.execute("SELECT record FROM faa_candidate WHERE candidate=? AND state=? AND county=? ORDER BY revision LIMIT 200",
                            (candidate["candidate_id"], "KS", "ELLSWORTH")).fetchall()
        elapsed = (time.perf_counter() - start) * 1000
        plan = db.execute("EXPLAIN QUERY PLAN SELECT record FROM faa_candidate WHERE candidate=? AND state=? AND county=? ORDER BY revision LIMIT 200",
                          (candidate["candidate_id"], "KS", "ELLSWORTH")).fetchall()
        return {"engine": sqlite3.sqlite_version, "purpose": "ISOLATED_REHEARSAL_ONLY", "inserted": inserted,
                "rows": db.execute("SELECT COUNT(*) FROM faa_candidate WHERE candidate=?", (candidate["candidate_id"],)).fetchone()[0],
                "county_result_count": len(sample), "query_ms": elapsed, "query_plan": plan,
                "integrity": db.execute("PRAGMA integrity_check").fetchone()[0], "release_state": "HELD"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture", type=Path)
    parser.add_argument("output", type=Path, help="new private directory outside Git")
    args = parser.parse_args()
    args.output.mkdir(mode=0o700, parents=False, exist_ok=False)
    candidate = faa.prepare((args.capture / "archive.zip").read_bytes(), json.loads((args.capture / "receipt.json").read_text()))
    (args.output / "candidate.json").write_bytes(faa.canonical(candidate))
    first = rehearse(candidate, args.output / "rehearsal.sqlite")
    retry = rehearse(candidate, args.output / "rehearsal.sqlite")
    (args.output / "validation.json").write_text(json.dumps({"first": first, "retry": retry}, indent=2))
    print(json.dumps({"candidate_id": candidate["candidate_id"], "records": len(candidate["records"]), "rejects": len(candidate["rejects"]), "first": first, "retry": retry}))
