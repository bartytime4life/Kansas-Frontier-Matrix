"""Private append-only land intake ledger, immutable objects and replayable index.

    Objects, candidates, EvidenceBundle candidates and receipts remain in
    QUARANTINE. SQLite is an administrative index, never title or release truth.
"""
from __future__ import annotations

from contextlib import contextmanager
import json
import os
from pathlib import Path
import sqlite3
import stat

from .land_records import MAX_BYTES, canonical, digest, instant, normalize, source_url

MARKER = {"profile": "kfm.private-land-records-store/v1", "exposure": "OWNER_REVIEW_ONLY", "release_writer": False}
LANES = ("data/quarantine/land-records/objects", "data/quarantine/land-records/captures", "data/quarantine/land-records/candidates", "data/quarantine/land-records/evidence", "data/receipts/ingest/land-records", "data/receipts/pipeline/land-records", "data/work/people-dna-land/land-records")


def directory(path, *, create=False):
    p = Path(path)
    if not p.is_absolute() or ".." in p.parts:
        raise ValueError("ABSOLUTE_SAFE_PATH_REQUIRED")
    here = Path(p.anchor)
    for part in p.parts[1:]:
        here /= part
        try:
            mode = here.lstat().st_mode
        except FileNotFoundError:
            if not create:
                raise ValueError("DIRECTORY_MISSING") from None
            here.mkdir(mode=0o700)
            mode = here.lstat().st_mode
        if not stat.S_ISDIR(mode):
            raise ValueError("SYMLINK_OR_SPECIAL_DIRECTORY")
    return p


def read_file(path, limit=MAX_BYTES):
    path = Path(path)
    directory(path.parent)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as handle:
        info = os.fstat(handle.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > limit:
            raise ValueError("FILE_TYPE_OR_SIZE_INVALID")
        raw = handle.read(limit + 1)
        final = os.fstat(handle.fileno())
        if len(raw) > limit or (info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns) != (final.st_ino, final.st_size, final.st_mtime_ns, final.st_ctime_ns):
            raise ValueError("FILE_CHANGED_OR_SIZE_LIMIT")
        return raw


def immutable(path, raw):
    path = Path(path)
    directory(path.parent, create=True)
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    except FileExistsError:
        if read_file(path, max(len(raw), MAX_BYTES)) != raw:
            raise ValueError("IMMUTABLE_OBJECT_CONFLICT") from None
        return
    with os.fdopen(fd, "wb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())


def initialize(root):
    root = Path(root)
    # An empty directory named .git (for example a temporary test artifact)
    # is not a checkout. Worktree .git files and real repositories are held.
    if root == Path(root.anchor) or any((p / ".git").is_file() or (p / ".git/HEAD").is_file() for p in (root, *root.parents)):
        raise ValueError("STORE_MUST_BE_OUTSIDE_GIT")
    directory(root, create=True)
    if root.stat().st_mode & 0o077:
        raise ValueError("STORE_PERMISSIONS_NOT_PRIVATE")
    marker = root / ".kfm-land-store.json"
    if marker.exists():
        if read_file(marker, 1024) != canonical(MARKER):
            raise ValueError("STORE_MARKER_INVALID")
    elif list(root.iterdir()):
        raise ValueError("FRESH_OR_INITIALIZED_STORE_REQUIRED")
    else:
        immutable(marker, canonical(MARKER))
    for lane in LANES:
        directory(root / lane, create=True)
    with connection(root) as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS captures (id TEXT PRIMARY KEY, manifest TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS versions (digest TEXT PRIMARY KEY, record_id TEXT NOT NULL, source TEXT NOT NULL, county TEXT, kind TEXT NOT NULL, event_date TEXT NOT NULL, record TEXT NOT NULL);
        CREATE INDEX IF NOT EXISTS land_date ON versions(event_date, digest);
        CREATE INDEX IF NOT EXISTS land_source ON versions(source, event_date, digest);
        CREATE INDEX IF NOT EXISTS land_county ON versions(county, event_date, digest);
        CREATE INDEX IF NOT EXISTS land_kind ON versions(kind, event_date, digest);
        CREATE TABLE IF NOT EXISTS occurrences (capture_id TEXT NOT NULL REFERENCES captures(id), digest TEXT NOT NULL REFERENCES versions(digest), candidate_id TEXT NOT NULL, evidence TEXT NOT NULL, PRIMARY KEY(capture_id, digest, candidate_id));
        CREATE TABLE IF NOT EXISTS runs (id TEXT PRIMARY KEY, receipt TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS controls (capture_id TEXT PRIMARY KEY REFERENCES captures(id), receipt TEXT NOT NULL);
        """)
    return root


@contextmanager
def connection(root, *, readonly=False):
    root = directory(root)
    path = root / "data/work/people-dna-land/land-records/index.sqlite3"
    directory(path.parent)
    if path.exists() or path.is_symlink():
        if not stat.S_ISREG(path.lstat().st_mode):
            raise ValueError("INDEX_SYMLINK_OR_SPECIAL")
    elif not readonly:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        os.close(fd)
    db = sqlite3.connect(path.as_uri() + ("?mode=ro" if readonly else "?mode=rw"), uri=True, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    try:
        with db:
            yield db
    finally:
        db.close()


def evidence_bundle(record, manifest, candidate, sizes):
    value = {"profile": "kfm.land-evidence-bundle-candidate/v1", "evidence_ref": record["evidence_ref"],
             "record_digest": record["record_digest"], "capture_id": manifest["capture_id"], "candidate_id": candidate["candidate_id"],
             "source_url": manifest["source_url"], "retrieved_at": manifest["retrieved_at"], "capture_method": manifest["capture_method"],
             "members": [{"sha256": key, "bytes": sizes[key]} for key in sorted(sizes)],
             "locators": candidate["locators"][record["record_digest"]], "documents": manifest["documents"],
             "review_state": "PENDING", "release_state": "UNRELEASED"}
    value["bundle_digest"] = digest(canonical(value))
    return value


def stage(root, manifest, objects, candidate):
    """Atomic index transaction after verified immutable file writes; replay repairs index.

    A failed index commit can leave immutable, unindexed objects in QUARANTINE.
    Replaying the same import repairs it, without approving or replacing anything.
    """
    fields = {"profile", "source_id", "source_url", "retrieved_at", "format", "capture_method", "payload_sha256", "bytes", "documents", "total_bytes", "source_admission", "release_state", "capture_id"}
    if (set(manifest) != fields or manifest.get("profile") != "kfm.land-records-capture/v1"
            or manifest.get("source_admission") != "PENDING" or manifest.get("release_state") != "UNRELEASED"
            or manifest.get("capture_method") != ("BROWSER_DOM_TEXT" if manifest.get("format") == "glo-text" else "EXPLICIT_EXPORT_OR_TRANSCRIPTION")):
        raise ValueError("CAPTURE_AUTHORITY_OR_SHAPE_INVALID")
    for document in manifest["documents"]:
        if set(document) != {"source_url", "sha256", "bytes"}:
            raise ValueError("DOCUMENT_FIELDS_INVALID")
        source_url(manifest["source_id"], document["source_url"])
    if manifest["total_bytes"] != manifest["bytes"] + sum(d["bytes"] for d in manifest["documents"]):
        raise ValueError("CAPTURE_BYTE_ACCOUNTING_INVALID")
    body = {k: v for k, v in manifest.items() if k != "capture_id"}
    if manifest.get("capture_id") != digest(canonical(body)) or candidate.get("capture_id") != manifest["capture_id"]:
        raise ValueError("CAPTURE_DIGEST_INVALID")
    if candidate.get("candidate_id") != digest(canonical({k: v for k, v in candidate.items() if k != "candidate_id"})):
        raise ValueError("CANDIDATE_DIGEST_INVALID")
    source_url(manifest["source_id"], manifest["source_url"])
    instant(manifest["retrieved_at"])
    expected = {manifest["payload_sha256"]: manifest["bytes"], **{d["sha256"]: d["bytes"] for d in manifest["documents"]}}
    if set(objects) != set(expected) or any(not isinstance(raw, bytes) or digest(raw) != key or len(raw) != expected[key] for key, raw in objects.items()) or sum(expected.values()) > MAX_BYTES:
        raise ValueError("OBJECT_CLOSURE_INVALID")
    # A self-hashed candidate cannot attest its own validation or source binding.
    replay = normalize(objects[manifest["payload_sha256"]], manifest, mapping=candidate.get("mapping"), max_records=1000)
    if canonical(replay) != canonical(candidate):
        raise ValueError("NORMALIZATION_REPLAY_MISMATCH")
    root = initialize(root)
    q = root / "data/quarantine/land-records"
    for key, raw in objects.items():
        immutable(q / "objects" / key[7:], raw)
    immutable(q / "captures" / (manifest["capture_id"][7:] + ".json"), canonical(manifest))
    immutable(q / "candidates" / (candidate["candidate_id"][7:] + ".json"), canonical(candidate))
    bundles = {}
    for record in candidate["records"]:
        evidence = evidence_bundle(record, manifest, candidate, expected)
        immutable(q / "evidence" / (evidence["bundle_digest"][7:] + ".json"), canonical(evidence))
        bundles[record["record_digest"]] = evidence
    run = digest(canonical([manifest["capture_id"], candidate["candidate_id"]]))
    receipt = {"profile": "kfm.land-records-ingest-receipt/v1", "run_id": run, "capture_id": manifest["capture_id"], "candidate_id": candidate["candidate_id"],
               "source_id": manifest["source_id"], "records": len(candidate["records"]), "payload_bytes": manifest["bytes"], "total_input_bytes": manifest["total_bytes"],
               "coverage": candidate["coverage"], "outcome": "QUARANTINE_CANDIDATE_READY", "authority": "CANDIDATE_ONLY",
               "source_admission": "PENDING", "review_state": "PENDING", "release_state": "UNRELEASED"}
    receipt["receipt_digest"] = digest(canonical(receipt))
    immutable(root / "data/receipts/ingest/land-records" / (run[7:] + ".json"), canonical(receipt))
    with connection(root) as db:
        db.execute("INSERT OR IGNORE INTO captures VALUES (?,?)", (manifest["capture_id"], canonical(manifest).decode()))
        for record in candidate["records"]:
            db.execute("INSERT OR IGNORE INTO versions VALUES (?,?,?,?,?,?,?)", (record["record_digest"], record["id"], record["source_id"], record["county"], record["instrument_type"], record["event_date"], canonical(record).decode()))
            if db.execute("SELECT record FROM versions WHERE digest=?", (record["record_digest"],)).fetchone()[0] != canonical(record).decode():
                raise ValueError("RECORD_INDEX_MISMATCH")
            db.execute("INSERT OR IGNORE INTO occurrences VALUES (?,?,?,?)", (manifest["capture_id"], record["record_digest"], candidate["candidate_id"], canonical(bundles[record["record_digest"]]).decode()))
        db.execute("INSERT OR IGNORE INTO runs VALUES (?,?)", (run, canonical(receipt).decode()))
    return receipt


def list_records(root, *, source=None, county=None, kind=None, start=None, end=None, after=None, limit=25):
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError("PAGE_LIMIT_INVALID")
    predicates, args = ["EXISTS (SELECT 1 FROM occurrences o WHERE o.digest=versions.digest AND NOT EXISTS (SELECT 1 FROM controls c WHERE c.capture_id=o.capture_id))"], []
    for key, value in (("source", source), ("county", county), ("kind", kind), ("event_date >=", start), ("event_date <=", end)):
        if value is not None:
            predicates.append(key + (" ?" if " " in key else " = ?"))
            args.append(value)
    if after:
        if not isinstance(after, str) or len(after) > 85 or "|" not in after:
            raise ValueError("CURSOR_INVALID")
        day, sha = after.split("|", 1)
        from .land_records import HEX, iso_date
        iso_date(day, required=True)
        if not HEX.fullmatch(sha):
            raise ValueError("CURSOR_INVALID")
        predicates.append("(event_date, digest) > (?, ?)")
        args += [day, sha]
    sql = "SELECT record, event_date, digest FROM versions" + (" WHERE " + " AND ".join(predicates) if predicates else "") + " ORDER BY event_date, digest LIMIT ?"
    with connection(root, readonly=True) as db:
        rows = db.execute(sql, (*args, limit + 1)).fetchall()
    selected = rows[:limit]
    return {"records": [json.loads(row["record"]) for row in selected], "next_cursor": selected[-1]["event_date"] + "|" + selected[-1]["digest"] if len(rows) > limit else None,
            "scope": "OWNER_REVIEW_ONLY", "release_state": "UNRELEASED"}


def evidence_for(root, record_digest):
    from .land_records import HEX
    if not isinstance(record_digest, str) or not HEX.fullmatch(record_digest):
        raise ValueError("RECORD_DIGEST_INVALID")
    with connection(root, readonly=True) as db:
        rows = db.execute("SELECT evidence FROM occurrences o WHERE digest=? AND NOT EXISTS (SELECT 1 FROM controls c WHERE c.capture_id=o.capture_id) ORDER BY capture_id, candidate_id LIMIT 100", (record_digest,)).fetchall()
    return [json.loads(row[0]) for row in rows]


def status(root):
    with connection(root, readonly=True) as db:
        counts = {name: db.execute("SELECT COUNT(*) FROM " + name).fetchone()[0] for name in ("captures", "versions", "runs")}
        counts["withdrawn_captures"] = db.execute("SELECT COUNT(*) FROM controls").fetchone()[0]
        sources = [dict(r) for r in db.execute("SELECT source, COUNT(*) AS records, MIN(event_date) AS first_date, MAX(event_date) AS last_date FROM versions GROUP BY source ORDER BY source")]
    return {"profile": MARKER["profile"], "counts": counts, "sources": sources, "scope": "OWNER_REVIEW_ONLY", "release_state": "UNRELEASED", "coverage": "NOT_ESTABLISHED", "public_records": 0}


def audit(root):
    """Verify every indexed run against preserved bytes and deterministic replay."""
    root = directory(root)
    if read_file(root / ".kfm-land-store.json", 1024) != canonical(MARKER):
        raise ValueError("STORE_MARKER_INVALID")
    q = root / "data/quarantine/land-records"
    verified = set()
    with connection(root, readonly=True) as db:
        runs = db.execute("SELECT id, receipt FROM runs ORDER BY id LIMIT 1001").fetchall()
        if len(runs) > 1000:
            raise ValueError("AUDIT_RUN_BUDGET_EXCEEDED")
        for run in runs:
            receipt = json.loads(run["receipt"])
            if canonical(receipt) != read_file(root / "data/receipts/ingest/land-records" / (run["id"][7:] + ".json")) or receipt["receipt_digest"] != digest(canonical({k: v for k, v in receipt.items() if k != "receipt_digest"})):
                raise ValueError("RECEIPT_INTEGRITY_FAILED")
            manifest = json.loads(read_file(q / "captures" / (receipt["capture_id"][7:] + ".json")))
            if manifest["capture_id"] != digest(canonical({k: v for k, v in manifest.items() if k != "capture_id"})):
                raise ValueError("CAPTURE_INTEGRITY_FAILED")
            indexed = db.execute("SELECT manifest FROM captures WHERE id=?", (manifest["capture_id"],)).fetchone()
            if indexed is None or indexed[0] != canonical(manifest).decode():
                raise ValueError("CAPTURE_INDEX_MISMATCH")
            candidate = json.loads(read_file(q / "candidates" / (receipt["candidate_id"][7:] + ".json")))
            objects = {d["sha256"]: read_file(q / "objects" / d["sha256"][7:]) for d in manifest["documents"]}
            objects[manifest["payload_sha256"]] = read_file(q / "objects" / manifest["payload_sha256"][7:])
            if any(digest(raw) != key for key, raw in objects.items()) or any(len(objects[d["sha256"]]) != d["bytes"] for d in manifest["documents"]):
                raise ValueError("OBJECT_INTEGRITY_FAILED")
            replay = normalize(objects[manifest["payload_sha256"]], manifest, mapping=candidate["mapping"], max_records=1000)
            if canonical(replay) != canonical(candidate):
                raise ValueError("CANDIDATE_REPLAY_FAILED")
            if receipt["records"] != len(candidate["records"]) or receipt["run_id"] != digest(canonical([manifest["capture_id"], candidate["candidate_id"]])):
                raise ValueError("RECEIPT_SCOPE_MISMATCH")
            for record in candidate["records"]:
                row = db.execute("SELECT record FROM versions WHERE digest=?", (record["record_digest"],)).fetchone()
                if row is None or row[0] != canonical(record).decode():
                    raise ValueError("RECORD_INDEX_MISMATCH")
                evidence = db.execute("SELECT evidence FROM occurrences WHERE capture_id=? AND digest=? AND candidate_id=?", (manifest["capture_id"], record["record_digest"], candidate["candidate_id"])).fetchone()
                if evidence is None:
                    raise ValueError("EVIDENCE_CLOSURE_FAILED")
                bundle = json.loads(evidence[0])
                if (canonical(bundle) != canonical(evidence_bundle(record, manifest, candidate, {k: len(v) for k, v in objects.items()}))
                        or read_file(q / "evidence" / (bundle["bundle_digest"][7:] + ".json")) != canonical(bundle)):
                    raise ValueError("EVIDENCE_CLOSURE_FAILED")
                verified.add(record["record_digest"])
        if db.execute("SELECT COUNT(*) FROM versions").fetchone()[0] != len(verified):
            raise ValueError("UNATTESTED_INDEX_RECORDS")
        for row in db.execute("SELECT capture_id, receipt FROM controls"):
            control = json.loads(row["receipt"])
            if control["capture_id"] != row["capture_id"] or control["state"] != "WITHDRAWN" or control["receipt_digest"] != digest(canonical({k: v for k, v in control.items() if k != "receipt_digest"})) or read_file(root / "data/receipts/pipeline/land-records" / (row["capture_id"][7:] + ".json")) != canonical(control):
                raise ValueError("WITHDRAWAL_INTEGRITY_FAILED")
    return {"outcome": "PASS", "runs": len(runs), "record_versions": len(verified), "authority": "INTEGRITY_ONLY", "release_state": "UNRELEASED"}


def withdraw_capture(root, capture_id, reason):
    """Append a private intake withdrawal; retains bytes and all old receipts."""
    from .land_records import HEX, stamp, text
    if not isinstance(capture_id, str) or not HEX.fullmatch(capture_id):
        raise ValueError("CAPTURE_ID_INVALID")
    reason = text(reason, 1024, required=True)
    initialize(root)
    with connection(root) as db:
        if db.execute("SELECT 1 FROM captures WHERE id=?", (capture_id,)).fetchone() is None:
            raise ValueError("CAPTURE_NOT_FOUND")
        prior = db.execute("SELECT receipt FROM controls WHERE capture_id=?", (capture_id,)).fetchone()
        if prior:
            return json.loads(prior[0])
        control = {"profile": "kfm.land-intake-withdrawal/v1", "capture_id": capture_id, "state": "WITHDRAWN", "reason": reason, "recorded_at": stamp(), "authority": "PRIVATE_INTAKE_ONLY"}
        control["receipt_digest"] = digest(canonical(control))
        path = Path(root) / "data/receipts/pipeline/land-records" / (capture_id[7:] + ".json")
        if path.exists():
            # Recover a completed immutable write after an interrupted SQL commit.
            control = json.loads(read_file(path))
            if control.get("capture_id") != capture_id or control.get("receipt_digest") != digest(canonical({k: v for k, v in control.items() if k != "receipt_digest"})):
                raise ValueError("WITHDRAWAL_INTEGRITY_FAILED")
        else:
            immutable(path, canonical(control))
        db.execute("INSERT INTO controls VALUES (?,?)", (capture_id, canonical(control).decode()))
    return control
