"""Private acceptance evidence desk; never grants intake or publication authority."""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

PREFIX = "/api/workspace/acceptance"
MAX_BYTES = 2 * 1024 * 1024
MAX_RECEIPTS = 32
MAX_EVENTS = 1000
MAX_TOTAL_BYTES = 16 * 1024 * 1024
SCHEMA = "kfm-pr5856-continuation-evidence/v1"
LANES = ("repository", "focused_tests", "browser_catalog", "rendered_browser",
         "installed", "deployment", "download_provider")
ENVIRONMENTS = ("candidate", "installed", "deployed", "public")
RESULTS = ("PASS", "FAIL", "HOLD", "UNVERIFIED")
AUTHORITY = {"sourceAdmission": False, "sensitivityClearance": False,
             "publication": False, "deployment": False, "intakeReview": False}
WEB = Path(__file__).resolve().parent / "local-web"


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("DUPLICATE_JSON_KEY")
        value[key] = item
    return value


def decode(raw):
    if not isinstance(raw, bytes) or not 0 < len(raw) <= MAX_BYTES:
        raise ValueError("EVIDENCE_BYTE_LIMIT")
    def invalid(_):
        raise ValueError("NONFINITE_JSON_NUMBER")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs,
                           parse_constant=invalid)
        canonical(value)
        return value
    except (UnicodeError, RecursionError, OverflowError) as exc:
        raise ValueError("INVALID_EVIDENCE_JSON") from exc


def envelope(value):
    if (not isinstance(value, dict) or value.get("algorithm") != "SHA-256"
            or not isinstance(value.get("payload"), dict)
            or not isinstance(value.get("digest"), str)
            or not re.fullmatch(r"[a-f0-9]{64}", value["digest"])):
        raise ValueError("INVALID_RECEIPT_ENVELOPE")
    if sha(canonical(value["payload"])) != value["digest"]:
        raise ValueError("RECEIPT_DIGEST_MISMATCH")
    return value["payload"]


def validate_receipt(raw):
    value = decode(raw)
    payload = envelope(value)
    if payload.get("schema") != SCHEMA:
        raise ValueError("UNSUPPORTED_RECEIPT_SCHEMA")
    if (not isinstance(payload.get("candidateSha"), str)
            or not re.fullmatch(r"[a-f0-9]{40}", payload["candidateSha"])):
        raise ValueError("CANDIDATE_REVISION_REQUIRED")
    sources = payload.get("sourceInventory")
    if not isinstance(sources, list) or len(sources) != 59:
        raise ValueError("EXPECTED_59_SOURCE_CASES")
    identifiers = set()
    for source in sources:
        if (not isinstance(source, dict)
                or not isinstance(source.get("id"), str)
                or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,100}", source["id"])
                or source["id"] in identifiers
                or not all(isinstance(source.get(key), str) and source[key]
                           for key in ("title", "category"))
                or not isinstance(source.get("testCase"), dict)
                or not all(isinstance(source["testCase"].get(key), list)
                           and all(isinstance(item, str) for item in source["testCase"][key])
                           for key in ("steps", "expected"))):
            raise ValueError("INVALID_SOURCE_CASE")
        identifiers.add(source["id"])
    envelope(payload.get("candidateEvidence"))
    downloads = envelope(payload.get("downloadEvidence"))
    results = downloads.get("results")
    if (not isinstance(results, list) or len(results) != 13
            or any(not isinstance(item, dict) or item.get("sourceId") not in identifiers
                   for item in results)
            or len({item["sourceId"] for item in results}) != 13):
        raise ValueError("EXPECTED_13_DOWNLOAD_CASES")
    return value


def text(value, name, maximum=4000, required=True):
    item = value.get(name, "")
    if not isinstance(item, str) or len(item) > maximum or (required and not item.strip()):
        raise ValueError("INVALID_" + name.upper())
    return item.strip()


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.utcoffset() is None:
            raise ValueError()
    except (ValueError, TypeError) as exc:
        raise ValueError("TIMEZONE_REQUIRED") from exc
    return value


class EvidenceStore:
    """Independent SQLite ledger below the private Studio root. Reads do not create it."""
    def __init__(self, studio_root):
        self.root = Path(studio_root)
        self.path = self.root / "acceptance.sqlite3"

    def connect(self, write=False):
        if self.root.is_symlink() or not self.root.is_dir() or self.path.is_symlink():
            raise ValueError("UNSAFE_EVIDENCE_STORAGE")
        if self.path.exists() and not self.path.is_file():
            raise ValueError("UNSAFE_EVIDENCE_STORAGE")
        if not write and not self.path.exists():
            return None
        if write and not self.path.exists():
            # Exclusive creation refuses replacement/symlink races at this step.
            import os
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.close(fd)
        db = sqlite3.connect(self.path.as_uri() + ("?mode=rw" if write else "?mode=ro"),
                             uri=True, timeout=3)
        db.row_factory = sqlite3.Row
        if write:
            db.execute("CREATE TABLE IF NOT EXISTS receipts (id TEXT PRIMARY KEY, imported_at TEXT NOT NULL, body BLOB NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS events (sequence INTEGER PRIMARY KEY, receipt_id TEXT NOT NULL, body TEXT NOT NULL, previous TEXT NOT NULL, digest TEXT NOT NULL, run_id TEXT, UNIQUE(receipt_id,run_id))")
            db.commit()
        return db

    @staticmethod
    def quota(db, additional):
        size = sum(db.execute("SELECT COALESCE(SUM(length(CAST(body AS BLOB))),0) FROM " + table).fetchone()[0]
                   for table in ("receipts", "events"))
        if size + additional > MAX_TOTAL_BYTES:
            raise ValueError("EVIDENCE_STORAGE_LIMIT")

    def import_receipt(self, raw):
        validate_receipt(raw)
        identity = sha(raw)
        db = self.connect(write=True)
        try:
            db.execute("BEGIN IMMEDIATE")
            duplicate = db.execute("SELECT 1 FROM receipts WHERE id=?", (identity,)).fetchone() is not None
            if not duplicate:
                if db.execute("SELECT COUNT(*) FROM receipts").fetchone()[0] >= MAX_RECEIPTS:
                    raise ValueError("RECEIPT_COUNT_LIMIT")
                self.quota(db, len(raw))
                db.execute("INSERT INTO receipts VALUES (?,?,?)",
                           (identity, datetime.now(timezone.utc).isoformat(), raw))
            db.commit()
        finally:
            db.close()
        return {"id": identity, "duplicate": duplicate, "acceptance": "UNREVIEWED",
                "authority": AUTHORITY}

    def raw(self, identity):
        if not re.fullmatch(r"[a-f0-9]{64}", identity):
            raise ValueError("INVALID_RECEIPT_ID")
        db = self.connect()
        if db is None:
            raise KeyError(identity)
        try:
            row = db.execute("SELECT body FROM receipts WHERE id=?", (identity,)).fetchone()
        finally:
            db.close()
        if row is None:
            raise KeyError(identity)
        raw = bytes(row["body"])
        if sha(raw) != identity:
            raise ValueError("STORED_EVIDENCE_CORRUPT")
        validate_receipt(raw)
        return raw

    def snapshot(self):
        db = self.connect()
        if db is None:
            return {"schema": "kfm-local-acceptance-ledger/v1", "receipts": [], "events": [],
                    "overallAcceptance": "HOLD", "authority": AUTHORITY}
        try:
            db.execute("BEGIN")
            receipts = []
            for row in db.execute("SELECT * FROM receipts ORDER BY id"):
                raw = bytes(row["body"])
                if sha(raw) != row["id"]:
                    raise ValueError("STORED_EVIDENCE_CORRUPT")
                receipts.append({"id": row["id"], "importedAt": row["imported_at"],
                                 "importStatus": "UNREVIEWED", "receipt": validate_receipt(raw)})
            receipt_ids = {item["id"] for item in receipts}
            events, previous = [], "0" * 64
            for row in db.execute("SELECT * FROM events ORDER BY sequence"):
                if row["receipt_id"] not in receipt_ids:
                    raise ValueError("ORPHANED_EVIDENCE_EVENT")
                body = decode(row["body"].encode())
                digest = sha(canonical({"sequence": row["sequence"], "previous": previous,
                                        "receiptId": row["receipt_id"], "event": body}))
                if row["previous"] != previous or row["digest"] != digest:
                    raise ValueError("LEDGER_INTEGRITY_FAILURE")
                events.append({"sequence": row["sequence"], "receiptId": row["receipt_id"],
                               "event": body, "previous": previous, "digest": digest})
                previous = digest
            return {"schema": "kfm-local-acceptance-ledger/v1", "receipts": receipts,
                    "events": events, "overallAcceptance": "HOLD", "authority": AUTHORITY}
        finally:
            db.close()

    def append(self, value):
        if not isinstance(value, dict):
            raise ValueError("EVENT_OBJECT_REQUIRED")
        identity = text(value, "receiptId", 64)
        payload = validate_receipt(self.raw(identity))["payload"]
        kind = value.get("kind")
        common = {"receiptId", "kind", "actor", "observedAt"}
        event = {"kind": kind, "actor": text(value, "actor", 128),
                 "observedAt": timestamp(text(value, "observedAt", 64)),
                 "recordedAt": datetime.now(timezone.utc).isoformat()}
        if kind == "observation":
            fields = {"sourceId", "lane", "environment", "result", "buildIdentity", "revision",
                      "browser", "viewport", "webgl2", "steps", "expected", "observed",
                      "evidence", "risk", "retestOf", "intakeFileId", "runId"}
            if set(value) - common - fields:
                raise ValueError("UNKNOWN_OBSERVATION_FIELDS")
            for key in fields:
                event[key] = text(value, key, 8000 if key in {"steps", "expected", "observed", "evidence", "risk"} else 256, False)
            if (event["lane"] not in LANES or event["environment"] not in ENVIRONMENTS
                    or event["result"] not in RESULTS):
                raise ValueError("INVALID_OBSERVATION_CONTEXT")
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}", event["runId"]):
                raise ValueError("RUN_ID_REQUIRED")
            if event["sourceId"] and event["sourceId"] not in {s["id"] for s in payload["sourceInventory"]}:
                raise ValueError("UNKNOWN_SOURCE")
            if event["revision"] and not re.fullmatch(r"[a-f0-9]{40}", event["revision"]):
                raise ValueError("FULL_REVISION_REQUIRED")
            if event["intakeFileId"] and not re.fullmatch(r"[a-f0-9]{32}", event["intakeFileId"]):
                raise ValueError("INVALID_INTAKE_REFERENCE")
            if not all(event[key] for key in ("steps", "expected", "observed")):
                raise ValueError("REPRODUCTION_REQUIRED")
            if event["result"] == "PASS":
                if not event["evidence"] or not event["buildIdentity"]:
                    raise ValueError("PASS_EVIDENCE_REQUIRED")
                if event["lane"] in {"rendered_browser", "installed", "deployment"} and not event["revision"]:
                    raise ValueError("PASS_REVISION_REQUIRED")
                if event["lane"] == "rendered_browser" and (event["webgl2"] != "available" or not event["browser"] or not event["viewport"]):
                    raise ValueError("RENDERED_BROWSER_EVIDENCE_REQUIRED")
        elif kind == "review":
            if set(value) - common - {"observation", "decision", "reason"}:
                raise ValueError("UNKNOWN_REVIEW_FIELDS")
            event.update(observation=text(value, "observation", 10),
                         decision=text(value, "decision", 32), reason=text(value, "reason", 4000))
            if event["decision"] not in {"HOLD", "RETEST", "ACCEPT_EVIDENCE"}:
                raise ValueError("INVALID_REVIEW_DECISION")
        else:
            raise ValueError("INVALID_EVENT_KIND")
        # Verify prior evidence first; an external file mutation does not silently become trusted history.
        self.snapshot()
        db = self.connect(write=True)
        try:
            db.execute("BEGIN IMMEDIATE")
            if kind == "observation":
                existing = db.execute("SELECT sequence,digest,body FROM events WHERE receipt_id=? AND run_id=?",
                                      (identity, event["runId"])).fetchone()
                if existing:
                    old = decode(existing["body"].encode())
                    comparable = {k: v for k, v in event.items() if k != "recordedAt"}
                    if {k: v for k, v in old.items() if k != "recordedAt"} != comparable:
                        raise ValueError("RUN_ID_CONFLICT")
                    return {"sequence": existing["sequence"], "digest": existing["digest"],
                            "duplicate": True, "overallAcceptance": "HOLD"}
            last = db.execute("SELECT sequence,digest FROM events ORDER BY sequence DESC LIMIT 1").fetchone()
            sequence = last["sequence"] + 1 if last else 1
            if sequence > MAX_EVENTS:
                raise ValueError("EVENT_COUNT_LIMIT")
            reference = event.get("observation") if kind == "review" else event.get("retestOf")
            if reference:
                if not re.fullmatch(r"[1-9][0-9]{0,9}", reference):
                    raise ValueError("INVALID_EVENT_REFERENCE")
                prior = db.execute("SELECT * FROM events WHERE sequence=? AND receipt_id=?",
                                   (int(reference), identity)).fetchone()
                if prior is None:
                    raise ValueError("REFERENCE_NOT_IN_THIS_RECEIPT")
                target = decode(prior["body"].encode())
                if target["kind"] != "observation":
                    raise ValueError("OBSERVATION_REFERENCE_REQUIRED")
                if kind == "review" and event["decision"] == "ACCEPT_EVIDENCE" and target["result"] != "PASS":
                    raise ValueError("ONLY_PASS_EVIDENCE_CAN_BE_ACCEPTED")
                if kind == "observation" and any(target[key] != event[key] for key in ("lane", "sourceId", "environment")):
                    raise ValueError("RETEST_SCOPE_MISMATCH")
            previous = last["digest"] if last else "0" * 64
            digest = sha(canonical({"sequence": sequence, "previous": previous,
                                    "receiptId": identity, "event": event}))
            self.quota(db, len(canonical(event)))
            db.execute("INSERT INTO events VALUES (?,?,?,?,?,?)",
                       (sequence, identity, canonical(event).decode(), previous, digest, event.get("runId")))
            db.commit()
        finally:
            db.close()
        return {"sequence": sequence, "digest": digest, "overallAcceptance": "HOLD"}

    def export(self):
        payload = self.snapshot()
        return canonical({"algorithm": "SHA-256", "digest": sha(canonical(payload)),
                          "canonicalization": "UTF-8 JSON; sorted keys; preserved arrays; payload-only hash",
                          "payload": payload})


def dispatch(request, method, studio_store):
    """Invoked only by the established same-origin Workspace dispatcher."""
    path = urlsplit(request.path).path
    assets = {PREFIX + "/page": ("acceptance.html", "text/html"),
              PREFIX + "/app.js": ("acceptance.js", "application/javascript"),
              PREFIX + "/style.css": ("acceptance.css", "text/css")}
    if not request.guard(token=path not in assets, header="X-KFM-Session"):
        return
    try:
        if path in assets:
            if method != "GET":
                return request.respond(405, {"error": "READ_ONLY_ASSET"})
            name, mime = assets[path]
            content = (WEB / name).read_text()
            if name == "acceptance.html":
                # Static, versioned sidebar only; imported text never enters HTML templates.
                source = (WEB / "index.html").read_text()
                sidebar = re.search(r'<aside class="sidebar">.*?</aside>', source, re.S).group()
                sidebar = sidebar.replace("nav-item active", "nav-item").replace(' aria-current="page"', '')
                sidebar = sidebar.replace('<span id="count">0</span>', '')
                sidebar = sidebar.replace('class="nav-item" id="acceptance-nav"', 'class="nav-item active" aria-current="page" id="acceptance-nav"')
                content = content.replace("<!-- WORKSPACE_SIDEBAR -->", sidebar)
            return request.respond(200, content, mime)
        store = EvidenceStore(studio_store.root)
        if method == "GET" and path == PREFIX + "/state":
            return request.respond(200, store.snapshot())
        if method == "GET" and path == PREFIX + "/export":
            return request.respond(200, store.export(), "application/json", "kfm-acceptance-ledger.json")
        if method == "GET" and path.startswith(PREFIX + "/original/"):
            return request.respond(200, store.raw(path.rsplit("/", 1)[-1]), "application/json", "kfm-original-receipt.json")
        if method != "POST" or path not in {PREFIX + "/import", PREFIX + "/events"}:
            return request.respond(404, {"error": "ACCEPTANCE_ROUTE_NOT_FOUND"})
        if request.headers.get("Origin") != request.server.origin:
            return request.respond(403, {"error": "EXACT_ORIGIN_REQUIRED"})
        if request.headers.get("Content-Type") != "application/json" or request.headers.get("Transfer-Encoding"):
            return request.respond(415, {"error": "BOUNDED_JSON_REQUIRED"})
        length = int(request.headers.get("Content-Length", "0"))
        if not 0 < length <= (MAX_BYTES if path.endswith("/import") else 65536):
            return request.respond(413, {"error": "EVIDENCE_BYTE_LIMIT"})
        request.connection.settimeout(10)
        raw = request.rfile.read(length)
        if len(raw) != length:
            raise ValueError("INTERRUPTED_EVIDENCE_REQUEST")
        studio_store.check_volume()
        result = store.import_receipt(raw) if path.endswith("/import") else store.append(decode(raw))
        return request.respond(200, result)
    except KeyError:
        return request.respond(404, {"error": "EVIDENCE_NOT_FOUND"})
    except sqlite3.Error:
        return request.respond(503, {"error": "EVIDENCE_STORE_BUSY_OR_UNAVAILABLE"})
    except (ValueError, RuntimeError, OSError, AttributeError) as exc:
        code = str(exc)
        return request.respond(400, {"error": code if re.fullmatch(r"[A-Z][A-Z0-9_]{2,90}", code) else "EVIDENCE_REQUEST_REJECTED"})
