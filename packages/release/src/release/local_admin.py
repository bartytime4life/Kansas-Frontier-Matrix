"""Owner-process staging and atomic activation mechanics for local rehearsal.

Never import this module in a serving route or acquisition worker. Decisions
must be supplied by the trusted operator's review workflow. The library cannot
verify the human review represented by external references and grants none.
"""
from pathlib import Path
import json
import os
import sqlite3
import tempfile
import uuid

from connectors_core.captured_json import canonical_bytes
from .core import MAX_PACKAGE_BYTES, validate_snapshot
from .local_store import LocalReleaseStore, regular_bytes
from .water_projection import project

SCHEMA = """
CREATE TABLE IF NOT EXISTS water_packages(package_id TEXT PRIMARY KEY, object_key TEXT NOT NULL UNIQUE, staged_at TEXT NOT NULL, staged_by TEXT NOT NULL, state TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS water_active(singleton INTEGER PRIMARY KEY CHECK(singleton=1), package_id TEXT NOT NULL, decision_json TEXT NOT NULL, previous_package_id TEXT, revision INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS water_activation_events(event_id TEXT PRIMARY KEY, package_id TEXT NOT NULL, previous_package_id TEXT, decision_json TEXT NOT NULL, occurred_at TEXT NOT NULL, action TEXT NOT NULL);
"""


def _validated_review_snapshot(raw: bytes) -> dict:
    manifest, values = validate_snapshot(raw)
    # The carrier binds bytes, but its embedded PASS receipt is untrusted input.
    # Replay the domain validator at both owner-controlled transition points.
    from pipelines.domains.hydrology.validate import validate_candidate

    try:
        expected = validate_candidate(values["candidate.json"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("CANDIDATE_VALIDATION_FAILED") from exc
    if values["validation.json"] != expected:
        raise ValueError("VALIDATION_RECEIPT_MISMATCH")
    return manifest


def initialize(root: Path):
    if not root.is_absolute() or root.is_symlink() or any(p.is_symlink() for p in root.parents):
        raise ValueError("PRIVATE_ABSOLUTE_STORE_REQUIRED")
    root.mkdir(mode=0o700, parents=False, exist_ok=True)
    LocalReleaseStore(str(root))
    objects = root / "objects"
    if objects.is_symlink():
        raise ValueError("STORE_SYMLINK_DENIED")
    objects.mkdir(mode=0o700, exist_ok=True)
    database = root / "activation.sqlite"
    if database.exists() or database.is_symlink():
        regular_bytes(database, 16*1024*1024)
    with sqlite3.connect(database, timeout=1) as db:
        db.executescript(SCHEMA)
    os.chmod(database, 0o600)


def stage(root: Path, raw: bytes, *, actor: str, now: str) -> str:
    manifest = _validated_review_snapshot(raw)
    initialize(root)
    name = manifest["package_id"].split(":")[1] + ".json"
    path = root / "objects" / name
    fd, temporary = tempfile.mkstemp(dir=root / "objects", prefix=".stage-")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw); handle.flush(); os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            if regular_bytes(path, MAX_PACKAGE_BYTES) != raw:
                raise ValueError("IMMUTABLE_OBJECT_CONFLICT")
    finally:
        Path(temporary).unlink(missing_ok=True)
    with sqlite3.connect(root / "activation.sqlite", timeout=1) as db:
        db.execute("INSERT OR IGNORE INTO water_packages VALUES(?,?,?,?,?)", (manifest["package_id"], name, now, actor, "STAGED"))
    return manifest["package_id"]


def activate(root: Path, package_id: str, trusted_decision: dict, *, expected_active: str | None, now: str, rollback=False):
    from .core import DIGEST
    LocalReleaseStore(str(root))
    if not DIGEST.fullmatch(package_id):
        raise ValueError("PACKAGE_ID_INVALID")
    raw = regular_bytes(root / "objects" / (package_id.split(":")[1] + ".json"), MAX_PACKAGE_BYTES)
    manifest = _validated_review_snapshot(raw)
    if manifest["package_id"] != package_id or trusted_decision.get("package_id") != package_id:
        raise ValueError("ACTIVATION_BINDING_MISMATCH")
    response = project(raw, trusted_decision, view="layers", now=now)
    if response["envelope"]["outcome"] != "ANSWER":
        raise ValueError("ACTIVATION_REVIEW_OR_EVIDENCE_HOLD")
    database = root / "activation.sqlite"
    regular_bytes(database, 16*1024*1024)
    with sqlite3.connect(database, timeout=1) as db:
        db.execute("BEGIN IMMEDIATE")
        current = db.execute("SELECT package_id, previous_package_id, revision FROM water_active WHERE singleton=1").fetchone()
        if (current[0] if current else None) != expected_active:
            raise ValueError("ACTIVATION_CONFLICT")
        if rollback and (current is None or current[1] != package_id):
            raise ValueError("ROLLBACK_TARGET_MISMATCH")
        if not rollback and manifest["rollback_target"] != expected_active:
            raise ValueError("ROLLBACK_BINDING_MISMATCH")
        staged = db.execute("SELECT state FROM water_packages WHERE package_id=?", (package_id,)).fetchone()
        if staged is None or staged[0] != "STAGED":
            raise ValueError("PACKAGE_NOT_STAGED")
        serialized = canonical_bytes(trusted_decision).decode()
        revision = current[2] + 1 if current else 1
        db.execute("INSERT OR REPLACE INTO water_active VALUES(1,?,?,?,?)", (package_id, serialized, expected_active, revision))
        event = "water:" + uuid.uuid4().hex
        db.execute("INSERT INTO water_activation_events VALUES(?,?,?,?,?,?)", (event, package_id, expected_active, serialized, now, "ROLLBACK" if rollback else "ACTIVATE"))
    return {"event_id": event, "package_id": package_id, "previous_package_id": expected_active, "revision": revision}
