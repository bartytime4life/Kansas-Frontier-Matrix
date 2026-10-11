"""Owner-process staging and atomic activation mechanics for local rehearsal.

Never import this module in a serving route or acquisition worker. Decisions
must be supplied by the trusted operator's review workflow. The library cannot
verify the human review represented by external references and grants none.
"""
from pathlib import Path
import os
import sqlite3
import tempfile
import uuid
from typing import Callable

from connectors_core.captured_json import canonical_bytes
from .core import MAX_PACKAGE_BYTES, SOIL, WATER, WEATHER, validate_snapshot
from .local_store import FAMILIES, LocalReleaseStore, family_names, regular_bytes

SCHEMA = "".join(f"""
CREATE TABLE IF NOT EXISTS {n['packages']}(package_id TEXT PRIMARY KEY, object_key TEXT NOT NULL UNIQUE, staged_at TEXT NOT NULL, staged_by TEXT NOT NULL, state TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS {n['active']}(singleton INTEGER PRIMARY KEY CHECK(singleton=1), package_id TEXT NOT NULL, decision_json TEXT NOT NULL, previous_package_id TEXT, revision INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS {n['events']}(event_id TEXT PRIMARY KEY, package_id TEXT NOT NULL, previous_package_id TEXT, decision_json TEXT NOT NULL, occurred_at TEXT NOT NULL, action TEXT NOT NULL);
""" for n in FAMILIES.values())
PROFILES = {"water": WATER, "weather": WEATHER, "soil": SOIL}


def _project(family: str):
    if family == "weather":
        from .weather_projection import project
    elif family == "soil":
        from .soil_projection import project
    else:
        from .water_projection import project
    return project


def _validated_review_snapshot(raw: bytes, validator: Callable[[dict], dict], family: str = "water") -> dict:
    family_names(family)
    manifest, values = validate_snapshot(raw, profile=PROFILES[family])
    # The carrier binds bytes, but its embedded PASS receipt is untrusted input.
    # The owner supplies the domain validator; packages do not import pipelines.
    try:
        expected = validator(values["candidate.json"])
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
    for names in FAMILIES.values():
        objects = root / names["objects"]
        if objects.is_symlink():
            raise ValueError("STORE_SYMLINK_DENIED")
        objects.mkdir(mode=0o700, exist_ok=True)
    database = root / "activation.sqlite"
    if database.exists() or database.is_symlink():
        regular_bytes(database, 16*1024*1024)
    with sqlite3.connect(database, timeout=1) as db:
        db.executescript(SCHEMA)
    os.chmod(database, 0o600)


def stage(root: Path, raw: bytes, *, actor: str, now: str, validator: Callable[[dict], dict], family: str = "water") -> str:
    names = family_names(family)
    manifest = _validated_review_snapshot(raw, validator, family)
    initialize(root)
    name = manifest["package_id"].split(":")[1] + ".json"
    path = root / names["objects"] / name
    fd, temporary = tempfile.mkstemp(dir=root / names["objects"], prefix=".stage-")
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
        db.execute(f"INSERT OR IGNORE INTO {names['packages']} VALUES(?,?,?,?,?)", (manifest["package_id"], name, now, actor, "STAGED"))
    return manifest["package_id"]


def activate(root: Path, package_id: str, trusted_decision: dict, *, expected_active: str | None, now: str, validator: Callable[[dict], dict], rollback=False,
             family: str = "water"):
    from .core import DIGEST
    names = family_names(family)
    LocalReleaseStore(str(root))
    if not DIGEST.fullmatch(package_id):
        raise ValueError("PACKAGE_ID_INVALID")
    raw = regular_bytes(root / names["objects"] / (package_id.split(":")[1] + ".json"), MAX_PACKAGE_BYTES)
    manifest = _validated_review_snapshot(raw, validator, family)
    if manifest["package_id"] != package_id or trusted_decision.get("package_id") != package_id:
        raise ValueError("ACTIVATION_BINDING_MISMATCH")
    response = _project(family)(raw, trusted_decision, view="layers", now=now)
    if response["envelope"]["outcome"] != "ANSWER":
        raise ValueError("ACTIVATION_REVIEW_OR_EVIDENCE_HOLD")
    database = root / "activation.sqlite"
    regular_bytes(database, 16*1024*1024)
    with sqlite3.connect(database, timeout=1) as db:
        db.execute("BEGIN IMMEDIATE")
        current = db.execute(f"SELECT package_id, previous_package_id, revision FROM {names['active']} WHERE singleton=1").fetchone()
        if (current[0] if current else None) != expected_active:
            raise ValueError("ACTIVATION_CONFLICT")
        if rollback and (current is None or current[1] != package_id):
            raise ValueError("ROLLBACK_TARGET_MISMATCH")
        if not rollback and manifest["rollback_target"] != expected_active:
            raise ValueError("ROLLBACK_BINDING_MISMATCH")
        staged = db.execute(f"SELECT state FROM {names['packages']} WHERE package_id=?", (package_id,)).fetchone()
        if staged is None or staged[0] != "STAGED":
            raise ValueError("PACKAGE_NOT_STAGED")
        serialized = canonical_bytes(trusted_decision).decode()
        revision = current[2] + 1 if current else 1
        db.execute(f"INSERT OR REPLACE INTO {names['active']} VALUES(1,?,?,?,?)", (package_id, serialized, expected_active, revision))
        event = family + ":" + uuid.uuid4().hex
        db.execute(f"INSERT INTO {names['events']} VALUES(?,?,?,?,?,?)", (event, package_id, expected_active, serialized, now, "ROLLBACK" if rollback else "ACTIVATE"))
    return {"event_id": event, "package_id": package_id, "previous_package_id": expected_active, "revision": revision}
