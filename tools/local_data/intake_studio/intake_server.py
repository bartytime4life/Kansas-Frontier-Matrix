#!/usr/bin/python3
"""Loopback-only intake review companion. Never writes to a KFM repository/store."""

from __future__ import annotations
from contextlib import contextmanager
import argparse, hashlib, io, json, mimetypes, os, re, secrets, shutil, sqlite3, subprocess, tempfile, threading, uuid, zipfile
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

APP = Path(__file__).resolve().parent
MAX_BYTES = 25 * 1024 * 1024
DOMAINS = {
    "hydrology": (
        "water",
        "river",
        "stream",
        "aquifer",
        "groundwater",
        "watershed",
        "flood",
        "usgs",
    ),
    "geology": (
        "geology",
        "geologic",
        "bedrock",
        "limestone",
        "mineral",
        "stratigraphy",
    ),
    "soil": ("soil", "ssurgo", "erosion", "clay"),
    "agriculture": ("agriculture", "crop", "farm", "wheat", "irrigation"),
    "flora": ("flora", "plant", "botanical", "vegetation"),
    "fauna": ("fauna", "wildlife", "bird", "animal"),
    "habitat": ("habitat", "ecosystem", "wetland", "prairie"),
    "atmosphere": ("weather", "atmosphere", "rainfall", "temperature", "climate"),
    "hazards": ("hazard", "tornado", "earthquake", "wildfire", "disaster"),
    "archaeology": ("archaeology", "archaeological", "artifact", "burial"),
    "people-dna-land": ("genealogy", "census", "ancestry", "dna", "landowner"),
    "roads-rail-trade": ("railroad", "railway", "highway", "transportation", "trade"),
    "settlements-infrastructure": (
        "settlement",
        "infrastructure",
        "municipal",
        "building",
        "town",
    ),
}
SURFACES = [
    "Reference library",
    "Map evidence attachment",
    "Dataset source documentation",
    "Historical timeline",
    "Story / interpretive context",
    "Unassigned",
]
RIGHTS = [
    "Unknown",
    "Owned by me",
    "Permission documented",
    "Public domain",
    "Restricted",
]
SENSITIVITY = [
    "Unknown",
    "Public",
    "Private / personal",
    "Sensitive location / cultural",
]
DECISIONS = ["Needs review", "Ready for integration review", "Keep quarantined"]
REVIEW_FIELDS = [
    "title",
    "source",
    "rights",
    "sensitivity",
    "domain",
    "surface",
    "description",
    "location",
    "observedAt",
    "reviewer",
    "decision",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def suggest(text, description=""):
    combined = (text + "\n" + description)[:300000]
    out = []
    for domain, words in DOMAINS.items():
        evidence = []
        for word in words:
            m = re.search(r"\b" + re.escape(word) + r"\b", combined, re.I)
            if m:
                evidence.append(
                    {
                        "term": word,
                        "excerpt": combined[
                            max(0, m.start() - 60) : m.end() + 100
                        ].replace("\n", " "),
                    }
                )
        if evidence:
            out.append(
                {
                    "domain": domain,
                    "surface": "Reference library",
                    "score": len(evidence),
                    "evidence": evidence[:4],
                    "reason": "Rule-based topic suggestion from matched text, not a verified classification or automatic integration.",
                }
            )
    return sorted(out, key=lambda x: (-x["score"], x["domain"]))[:4]


def flags_for(text):
    rules = [
        (
            r"\b(burial|archaeolog\w*|sacred|tribal|indigenous)\b",
            "Possible cultural or archaeological sensitivity. Review rights and exact-location disclosure.",
        ),
        (
            r"\b(dna|social security|patient|payroll|paycheck|birth date|medical)\b",
            "Possible personal information. Keep private until reviewed.",
        ),
        (
            r"\b(endangered|rare species|nesting site)\b",
            "Possible sensitive species location. Consider generalization.",
        ),
        (
            r"\b(substation|pipeline|critical infrastructure)\b",
            "Possible infrastructure sensitivity. Review precision and access.",
        ),
    ]
    return [reason for pattern, reason in rules if re.search(pattern, text, re.I)]


def signature(raw):
    if raw.startswith(b"%PDF-"):
        return "application/pdf"
    if raw.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if raw.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if raw[:4] == b"RIFF" and raw[8:12] == b"WEBP":
        return "image/webp"
    if raw[:4] in (b"II*\x00", b"MM\x00*"):
        return "image/tiff"
    raise ValueError("Unsupported file content. Choose a PDF, JPEG, PNG, WebP or TIFF.")


def clean_name(name):
    return re.sub(r"[\x00-\x1f\x7f\\/]", "_", name)[:180].strip(" .") or "uploaded-file"


def integration(review):
    return {
        "state": "QUARANTINED_REVIEW_ONLY",
        "logicalOwner": "data/",
        "proposedLane": "Capture into existing KFM quarantine through the reviewed local-data intake workflow; WORK staging only after its checks.",
        "domain": review["domain"],
        "surface": review["surface"],
        "publicUse": "No publication; owner review required",
        "basis": [
            "docs/doctrine/directory-rules.md via accepted ADR-0029",
            "docs/runbooks/raw-data-intake.md",
            "Domain lane inventory is PROPOSED, not an adopted new registry.",
        ],
    }


class Store:
    def __init__(self, root, runtime):
        self.root = Path(root).expanduser().resolve()
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(self.root, 0o700)
        self.objects = self.root / "objects"
        self.objects.mkdir(exist_ok=True, mode=0o700)
        self.runtime = Path(runtime).expanduser().resolve()
        self.lock = threading.RLock()
        self.extract_lock = threading.Lock()
        with self.db() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS files(id TEXT PRIMARY KEY, data TEXT NOT NULL)"
            )

    @contextmanager
    def db(self):
        db = sqlite3.connect(self.root / "intake.sqlite", timeout=10)
        try:
            db.execute("PRAGMA journal_mode=WAL")
            with db:
                yield db
        finally:
            db.close()

    def get(self, id):
        with self.db() as db:
            row = db.execute("SELECT data FROM files WHERE id=?", (id,)).fetchone()
        if not row:
            raise KeyError("File not found.")
        return json.loads(row[0])

    def list(self):
        with self.db() as db:
            return [
                json.loads(r[0])
                for r in db.execute("SELECT data FROM files ORDER BY rowid DESC")
            ]

    def save(self, record):
        with self.db() as db:
            db.execute(
                "INSERT OR REPLACE INTO files VALUES(?,?)",
                (record["id"], json.dumps(record, ensure_ascii=False)),
            )

    def capabilities(self):
        sandbox = all(Path(p).is_file() for p in ("/usr/bin/bwrap", "/usr/bin/prlimit"))
        pillow = (
            subprocess.run(
                ["/usr/bin/python3", "-c", "import PIL"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        )
        ocr = (self.runtime / "root/usr/bin/tesseract").is_file()
        pdf = all(
            Path("/usr/bin", p).is_file() for p in ("pdfinfo", "pdftoppm", "pdftotext")
        )
        return {
            "pdf": sandbox and pillow and ocr and pdf,
            "ocr": sandbox and pillow and ocr,
            "images": sandbox and pillow and ocr,
            "sandbox": sandbox,
            "pillow": pillow,
            "ocrRuntime": ocr,
            "pdfTools": pdf,
            "note": "Dependency presence only; successful extraction is verified per file.",
        }

    def ingest(self, name, body):
        if not 0 < len(body) <= MAX_BYTES:
            raise ValueError("File must contain 1 byte to 25 MiB.")
        mime = signature(body[:20])
        digest = hashlib.sha256(body).hexdigest()
        dest = self.objects / digest
        with self.extract_lock:
            duplicate = dest.exists()
            if not duplicate:
                work = Path(tempfile.mkdtemp(prefix="extract-", dir=self.root))
                try:
                    (work / "original").write_bytes(body)
                    cmd = [
                        "/usr/bin/prlimit",
                        "--as=1610612736",
                        "--cpu=90",
                        "--fsize=67108864",
                        "--",
                        "/usr/bin/bwrap",
                        "--die-with-parent",
                        "--unshare-all",
                        "--new-session",
                        "--cap-drop",
                        "ALL",
                        "--ro-bind",
                        "/usr",
                        "/usr",
                        "--symlink",
                        "usr/lib",
                        "/lib",
                        "--symlink",
                        "usr/lib64",
                        "/lib64",
                        "--proc",
                        "/proc",
                        "--dev",
                        "/dev",
                        "--tmpfs",
                        "/tmp",
                        "--dir",
                        "/etc",
                        "--ro-bind",
                        str(APP / "intake_worker.py"),
                        "/worker.py",
                        "--ro-bind",
                        str(self.runtime / "root"),
                        "/ocr",
                        "--bind",
                        str(work),
                        "/work",
                        "--chdir",
                        "/work",
                        "--clearenv",
                        "--setenv",
                        "PATH",
                        "/usr/bin:/bin",
                        "--setenv",
                        "LANG",
                        "C.UTF-8",
                        "/usr/bin/python3",
                        "/worker.py",
                    ]
                    try:
                        p = subprocess.run(
                            cmd,
                            stdin=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.PIPE,
                            timeout=100,
                        )
                        if p.returncode or not (work / "analysis.json").is_file():
                            raise ValueError("Sandbox extraction did not complete.")
                        analysis = json.loads((work / "analysis.json").read_text())
                    except Exception:
                        analysis = {
                            "status": "Failed",
                            "method": "Sandboxed extraction unavailable",
                            "pages": None,
                            "text": "",
                            "metadata": {},
                            "textTruncated": False,
                            "warnings": [
                                "Local extraction failed or exceeded its limit. Original retained; manual review is available."
                            ],
                            "suggestions": [],
                            "flags": [],
                        }
                    analysis["suggestions"] = suggest(analysis["text"])
                    analysis["flags"] += flags_for(analysis["text"])
                    (work / "analysis.json").write_text(json.dumps(analysis))
                    for child in work.iterdir():
                        if child.name not in (
                            "original",
                            "analysis.json",
                            "preview.png",
                        ):
                            child.unlink()
                    work.rename(dest)
                finally:
                    if work.exists():
                        shutil.rmtree(work)
            analysis = json.loads((dest / "analysis.json").read_text())
        name = clean_name(name)
        at = now()
        review = {
            "title": Path(name).stem,
            "source": "",
            "rights": "Unknown",
            "sensitivity": "Unknown",
            "domain": "Unassigned",
            "surface": "Unassigned",
            "description": "",
            "location": "",
            "observedAt": "",
            "reviewer": "",
            "decision": "Needs review",
        }
        record = {
            "id": uuid.uuid4().hex,
            "version": 1,
            "name": name,
            "mime": mime,
            "size": len(body),
            "sha256": digest,
            "uploadedAt": at,
            "analysis": analysis,
            "preview": (dest / "preview.png").exists(),
            "review": review,
            "history": [
                {
                    "at": at,
                    "action": "Uploaded into private local review inbox; no KFM admission",
                    "version": 1,
                }
            ],
            "occurrences": [{"at": at, "name": name}],
            "integration": integration(review),
        }
        self.save(record)
        return record, duplicate

    def review(self, id, value):
        with self.lock:
            record = self.get(id)
            if value.get("version") != record["version"]:
                raise RuntimeError("This record changed. Reload it before saving.")
            if set(value) - set(REVIEW_FIELDS) - {"version"}:
                raise ValueError("Unexpected review field.")
            for key in REVIEW_FIELDS:
                if not isinstance(value.get(key), str) or len(value[key]) > 10000:
                    raise ValueError(
                        "Review fields must be text, at most 10,000 characters."
                    )
            r = {key: value[key].strip() for key in REVIEW_FIELDS}
            if (
                r["rights"] not in RIGHTS
                or r["sensitivity"] not in SENSITIVITY
                or r["domain"] not in [*DOMAINS, "Unassigned"]
                or r["surface"] not in SURFACES
                or r["decision"] not in DECISIONS
            ):
                raise ValueError("Invalid review selection.")
            if r["decision"] == "Ready for integration review":
                if (
                    not all(r[k] for k in ("title", "source", "reviewer"))
                    or r["rights"] in ("Unknown", "Restricted")
                    or r["sensitivity"] != "Public"
                    or r["domain"] == "Unassigned"
                    or r["surface"] == "Unassigned"
                ):
                    raise ValueError(
                        "Choose a destination, supply source and reviewer, document usable rights, and confirm Public sensitivity; otherwise keep the file in review."
                    )
                if record["analysis"]["status"] == "Failed":
                    raise ValueError(
                        "Extraction failed. Keep this file quarantined and resolve the parsing failure before preparing integration review."
                    )
                if record["analysis"]["flags"]:
                    raise ValueError(
                        "Sensitivity flags require a separate governed review. Export the held package; this desk cannot clear those flags."
                    )
            changed = any(
                r[k] != record["review"][k]
                for k in REVIEW_FIELDS
                if k not in ("decision", "reviewer")
            )
            if (
                changed
                and record["review"]["decision"] == "Ready for integration review"
            ):
                r["decision"] = "Needs review"
            record["version"] += 1
            old = record["review"]
            record["review"] = r
            # Raw extraction stays immutable; operator description can add explicit suggestion context.
            record["analysis"]["suggestions"] = suggest(
                record["analysis"]["text"], r["description"]
            )
            original = json.loads(
                (self.objects / record["sha256"] / "analysis.json").read_text()
            )
            record["analysis"]["flags"] = list(
                dict.fromkeys(original["flags"] + flags_for(r["description"]))
            )
            if (
                record["analysis"]["flags"]
                and r["decision"] == "Ready for integration review"
            ):
                r["decision"] = "Needs review"
            record["integration"] = integration(r)
            record["history"].append(
                {
                    "at": now(),
                    "action": "Review saved; publication hold retained",
                    "version": record["version"],
                    "previousReview": old,
                    "review": dict(r),
                }
            )
            self.save(record)
            return record

    def export(self, id):
        record = self.get(id)
        obj = self.objects / record["sha256"]
        original = (obj / "original").read_bytes()
        if hashlib.sha256(original).hexdigest() != record["sha256"]:
            raise ValueError("Original integrity check failed. Export refused.")
        content = {
            "kind": "KFM_LOCAL_INTAKE_REVIEW_PROPOSAL",
            "schemaVersion": 1,
            "exportedAt": now(),
            "authority": {
                "sourceAdmission": False,
                "promotion": False,
                "publication": False,
            },
            "record": record,
            "nextStep": "Review this package with the existing tools/local_data intake workflow. No source admission or release has occurred.",
        }
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            items = {
                "review-proposal.json": json.dumps(
                    content, indent=2, ensure_ascii=False
                ).encode(),
                "extracted-text.txt": record["analysis"]["text"].encode(),
                "original/" + record["name"]: original,
                "README.txt": b"PRIVATE HELD REVIEW PACKAGE. Original preserved. OCR is derivative, not root truth. No admission, promotion, publication or public website change. Use existing KFM local-data review and capture workflow.",
            }
            if (obj / "preview.png").exists():
                items["preview.png"] = (obj / "preview.png").read_bytes()
            for name, b in items.items():
                z.writestr(name, b)
            z.writestr(
                "checksums.json",
                json.dumps(
                    {name: hashlib.sha256(b).hexdigest() for name, b in items.items()},
                    indent=2,
                ),
            )
        return out.getvalue()


class Server(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, port, store):
        self.store = store
        self.token = secrets.token_urlsafe(32)
        super().__init__(("127.0.0.1", port), Handler)
        self.origin = f"http://127.0.0.1:{self.server_port}"


class Handler(BaseHTTPRequestHandler):
    server_version = "KFM-Local-Intake/1"

    def log_message(self, *args):
        pass

    def respond(self, code, body, kind="application/json", attachment=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False).encode()
        if isinstance(body, str):
            body = body.encode()
        if not isinstance(kind, str):
            kind = str(kind)
        kind = kind.replace("\r", "").replace("\n", "").replace("\x00", "").strip()
        if not kind:
            kind = "application/octet-stream"
        self.send_response(code)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Permissions-Policy", "camera=(self), microphone=(), geolocation=()"
        )
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' blob: data:; connect-src 'self'; media-src 'self' blob:; font-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'",
        )
        if attachment:
            safe_attachment = re.sub(r'[\r\n\x00-\x1f\x7f"]+', "_", str(attachment)).strip()
            if not safe_attachment:
                safe_attachment = "download"
            self.send_header(
                "Content-Disposition", f'attachment; filename="{safe_attachment}"'
            )
        self.end_headers()
        self.wfile.write(body)

    def guard(self, token=True):
        if self.headers.get("Host") != self.server.origin[7:]:
            self.respond(403, {"error": "Exact loopback address required."})
            return False
        if self.headers.get("Origin") not in (
            None,
            self.server.origin,
        ) or self.headers.get("Sec-Fetch-Site") not in (None, "same-origin", "none"):
            self.respond(403, {"error": "Same-origin local access required."})
            return False
        if token and not secrets.compare_digest(
            self.headers.get("X-KFM-Token", ""), self.server.token
        ):
            self.respond(
                403, {"error": "Session expired. Refresh this local workspace."}
            )
            return False
        return True

    def do_GET(self):
        path = urlsplit(self.path).path
        if not self.guard(token=path.startswith("/api/") and path != "/api/session"):
            return
        try:
            if path == "/api/session":
                return self.respond(
                    200,
                    {
                        "app": "kfm-local-intake-studio",
                        "token": self.server.token,
                        "storagePath": str(self.server.store.root),
                        "maxBytes": MAX_BYTES,
                        "capabilities": self.server.store.capabilities(),
                        "authority": {
                            "publication": False,
                            "sourceAdmission": False,
                            "productionData": False,
                        },
                    },
                )
            if path == "/api/files":
                return self.respond(200, {"files": self.server.store.list()})
            m = re.fullmatch(
                r"/api/files/([a-f0-9]{32})(?:/(preview|original|export))?", path
            )
            if m:
                record = self.server.store.get(m[1])
                obj = self.server.store.objects / record["sha256"]
                if not m[2]:
                    return self.respond(200, {"file": record})
                if m[2] == "export":
                    return self.respond(
                        200,
                        self.server.store.export(m[1]),
                        "application/zip",
                        "kfm-held-review-" + m[1][:8] + ".zip",
                    )
                if m[2] == "preview":
                    return self.respond(
                        200, (obj / "preview.png").read_bytes(), "image/png"
                    )
                ext = {
                    "application/pdf": "pdf",
                    "image/png": "png",
                    "image/jpeg": "jpg",
                    "image/webp": "webp",
                    "image/tiff": "tiff",
                }[record["mime"]]
                return self.respond(
                    200,
                    (obj / "original").read_bytes(),
                    "application/octet-stream",
                    "original-" + m[1][:8] + "." + ext,
                )
            # Static assets are explicit; user-supplied files are never served as executable content.
            if path in ("/", "/index.html", "/app.js", "/style.css"):
                file = APP / "local-web" / ("index.html" if path == "/" else path[1:])
            else:
                raise KeyError()
            if not file.is_file() or file.is_symlink():
                raise KeyError()
            kind = mimetypes.guess_type(file.name)[0] or "application/octet-stream"
            return self.respond(200, file.read_bytes(), kind)
        except (KeyError, FileNotFoundError):
            self.respond(404, {"error": "Not found."})
        except ValueError as e:
            self.respond(400, {"error": str(e)})
        except Exception:
            self.respond(
                500, {"error": "Local read failed. Original files remain preserved."}
            )

    def do_POST(self):
        if not self.guard():
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            path = urlsplit(self.path)
            maximum = MAX_BYTES if path.path == "/api/upload" else 150000
            if not 0 < length <= maximum:
                return self.respond(
                    413,
                    {
                        "error": "File is empty or exceeds the allowed size (25 MB per upload)."
                    },
                )
            self.connection.settimeout(30)
            body = self.rfile.read(length)
            if len(body) != length:
                raise ValueError("Upload interrupted. Choose the file again.")
            if path.path == "/api/upload":
                name = parse_qs(path.query).get("name", ["uploaded-file"])[0]
                record, duplicate = self.server.store.ingest(name, body)
                return self.respond(201, {"file": record, "duplicate": duplicate})
            m = re.fullmatch(r"/api/files/([a-f0-9]{32})/review", path.path)
            if m:
                value = json.loads(body)
                if not isinstance(value, dict):
                    raise ValueError("Invalid review.")
                return self.respond(
                    200, {"file": self.server.store.review(m[1], value)}
                )
            self.respond(404, {"error": "Unknown action."})
        except RuntimeError as e:
            self.respond(409, {"error": str(e)})
        except (ValueError, KeyError) as e:
            self.respond(400, {"error": str(e)})
        except Exception:
            self.respond(
                500,
                {
                    "error": "Local operation failed. Please retry; no KFM production data was changed."
                },
            )


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8776)
    parser.add_argument(
        "--store", default=str(Path.home() / ".local/share/kfm-intake-studio")
    )
    parser.add_argument(
        "--runtime", default=str(Path.home() / ".local/share/kfm-intake-runtime")
    )
    a = parser.parse_args()
    store = Store(a.store, a.runtime)
    server = Server(a.port, store)
    print(f"KFM Local Intake: {server.origin}", flush=True)
    print(f"Private inbox: {store.root}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
