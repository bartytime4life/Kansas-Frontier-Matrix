"""Resumable, chunk-verified Studio uploads and streamed originals; synthetic bytes only."""
import hashlib
import io
import json
import os
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from unittest.mock import patch

from tests.local_data.studio_auth import signed_in_headers
from tools.local_data.intake_studio import handoff, intake_backend, large_upload
from tools.local_data.intake_studio.intake_server import Server, Store

PNG = b"\x89PNG\r\n\x1a\n"
CHUNK = 4096
SINGLE = 1024


def fake_extract(cmd, **kwargs):
    if "--bind" not in cmd:  # capability probes report missing tools
        return type("Result", (), {"returncode": 1})()
    work = Path(cmd[cmd.index("--bind") + 1])
    (work / "analysis.json").write_text(json.dumps({
        "status": "Partial", "method": "Synthetic unit-test extraction", "pages": 1,
        "text": "water river aquifer", "metadata": {}, "warnings": [], "suggestions": [], "flags": []}))
    return type("Result", (), {"returncode": 0})()


def body(size, seed=b"large evidence"):
    out = bytearray(PNG)
    counter = 0
    while len(out) < size:
        out += hashlib.sha256(seed + counter.to_bytes(8, "big")).digest()
        counter += 1
    return bytes(out[:size])


def sha(data):
    return hashlib.sha256(data).hexdigest()


class LargeUploadStoreTests(unittest.TestCase):
    def setUp(self):
        self.enterContext(patch.multiple(intake_backend, UPLOAD_CHUNK_BYTES=CHUNK, SINGLE_UPLOAD_BYTES=SINGLE))
        self.enterContext(patch("tools.local_data.intake_studio.intake_server.subprocess.run",
                                side_effect=fake_extract))
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        self.store = Store(self.root / "studio", self.root / "missing-runtime")
        self.uploads = self.store.uploads

    def send_all(self, upload, data):
        for offset in range(0, len(data), CHUNK):
            part = data[offset:offset + CHUNK]
            upload = self.uploads.append(upload["id"], offset, part, sha(part))
        return upload

    def test_parts_reassemble_into_one_verified_record(self):
        data = body(3 * CHUNK + 123)
        upload = self.uploads.create("survey-map.png", len(data))
        self.assertEqual((upload["received"], upload["chunkBytes"]), (0, CHUNK))
        self.assertEqual(self.send_all(upload, data)["received"], len(data))
        record, duplicate = self.store.ingest_upload(upload["id"])
        self.assertFalse(duplicate)
        self.assertEqual((record["size"], record["sha256"], record["mime"], record["name"]),
                         (len(data), sha(data), "image/png", "survey-map.png"))
        self.assertEqual(self.store.original_bytes(record), data)
        self.assertEqual(list((self.root / "studio" / "uploads").iterdir()), [])
        self.assertEqual(list((self.root / "studio").glob("upload-*")), [])
        # The same bytes again make a second record over one stored object.
        again = self.uploads.create("copy.png", len(data))
        self.send_all(again, data)
        second, duplicate = self.store.ingest_upload(again["id"])
        self.assertTrue(duplicate)
        self.assertNotEqual(second["id"], record["id"])
        self.assertEqual(second["sha256"], record["sha256"])

    def test_resume_uses_the_stored_byte_count(self):
        data = body(2 * CHUNK + 10)
        upload = self.uploads.create("resume.png", len(data))
        self.uploads.append(upload["id"], 0, data[:CHUNK], sha(data[:CHUNK]))
        # An interrupted write leaves a correct prefix; status reports it.
        with open(self.root / "studio" / "uploads" / upload["id"] / "data", "ab") as stream:
            stream.write(data[CHUNK:CHUNK + 100])
        status = self.uploads.status(upload["id"])
        self.assertEqual(status["received"], CHUNK + 100)
        with self.assertRaisesRegex(RuntimeError, f"at byte {CHUNK + 100}"):
            self.uploads.append(upload["id"], CHUNK, data[CHUNK:2 * CHUNK], sha(data[CHUNK:2 * CHUNK]))
        offset = status["received"]
        while offset < len(data):
            part = data[offset:offset + CHUNK]
            offset = self.uploads.append(upload["id"], offset, part, sha(part))["received"]
        record, _ = self.store.ingest_upload(upload["id"])
        self.assertEqual(record["sha256"], sha(data))

    def test_bad_parts_are_refused_before_any_write(self):
        data = body(CHUNK + 10)
        upload = self.uploads.create("bad.png", len(data))
        path = self.root / "studio" / "uploads" / upload["id"] / "data"
        cases = [
            (data[:CHUNK], "0" * 64, ValueError, "integrity"),
            (data[:CHUNK], "not-a-digest", ValueError, "SHA-256"),
            (b"", sha(b""), ValueError, "empty"),
            (data[:CHUNK] + b"x", sha(data[:CHUNK] + b"x"), ValueError, "larger than the part size"),
            (b"GIF89a" + data[6:CHUNK], sha(b"GIF89a" + data[6:CHUNK]), ValueError, "Unsupported file content"),
        ]
        for part, digest, error, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(error, message):
                self.uploads.append(upload["id"], 0, part, digest)
            self.assertEqual(path.stat().st_size, 0)
        self.uploads.append(upload["id"], 0, data[:CHUNK], sha(data[:CHUNK]))
        overflow = data[CHUNK:] + b"overflow"
        with self.assertRaisesRegex(ValueError, "past the declared file size"):
            self.uploads.append(upload["id"], CHUNK, overflow, sha(overflow))
        with self.assertRaisesRegex(ValueError, f"incomplete: {CHUNK} of {len(data)}"):
            self.store.ingest_upload(upload["id"])

    def test_session_limits_and_identifiers(self):
        for name, size, message in [("", 10, "file name"), ("a\nb.png", 10, "file name"),
                                    ("x" * 256 + ".png", 10, "file name"),
                                    ("zero.png", 0, "1 byte to 2 GiB"),
                                    ("huge.png", intake_backend.MAX_BYTES + 1, "1 byte to 2 GiB"),
                                    ("float.png", 10.0, "1 byte to 2 GiB")]:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, message):
                self.uploads.create(name, size)
        for bad in ("../" + "a" * 30, "A" * 32, "a" * 31, "a" * 32):
            with self.subTest(bad=bad), self.assertRaises(KeyError):
                self.uploads.status(bad)
        made = [self.uploads.create(f"{n}.png", 10) for n in range(large_upload.MAX_ACTIVE_SESSIONS)]
        with self.assertRaisesRegex(RuntimeError, "Too many unfinished uploads"):
            self.uploads.create("one-more.png", 10)
        self.uploads.cancel(made[0]["id"])
        with self.assertRaises(KeyError):
            self.uploads.status(made[0]["id"])
        self.uploads.create("after-cancel.png", 10)

    def test_free_space_is_checked_before_accepting_bytes(self):
        usage = type("Usage", (), {"free": large_upload.FREE_SPACE_MARGIN + 99})
        with patch.object(large_upload.shutil, "disk_usage", return_value=usage):
            with self.assertRaisesRegex(ValueError, "free disk space"):
                self.uploads.create("big.png", 100)
            upload = self.uploads.create("fits.png", 99)
        usage.free = large_upload.FREE_SPACE_MARGIN + 10
        part = body(50)
        with patch.object(large_upload.shutil, "disk_usage", return_value=usage):
            with self.assertRaisesRegex(ValueError, "free disk space"):
                self.uploads.append(upload["id"], 0, part, sha(part))

    def test_stale_sessions_are_removed(self):
        clock = [1_000_000.0]
        self.uploads.clock = lambda: clock[0]
        stale = self.uploads.create("stale.png", 10)
        session = self.root / "studio" / "uploads" / stale["id"]
        os.utime(session, (clock[0], clock[0]))
        clock[0] += large_upload.STALE_SECONDS + 1
        self.uploads.create("fresh.png", 10)
        self.assertFalse(session.exists())

    def test_streamed_readers_verify_before_and_preserve_bytes(self):
        data = body(3 * CHUNK)
        upload = self.uploads.create("export.png", len(data))
        self.send_all(upload, data)
        record, _ = self.store.ingest_upload(upload["id"])
        with self.store.open_original(record) as stream:
            self.assertEqual(stream.read(), data)
        package = io.BytesIO()
        self.store.export_to(record["id"], package)
        with zipfile.ZipFile(io.BytesIO(package.getvalue())) as archive:
            self.assertIsNone(archive.testzip())
            original = archive.getinfo("original/export.png")
            # Above the single-request size, originals are stored, not recompressed.
            self.assertEqual(original.compress_type, zipfile.ZIP_STORED)
            self.assertEqual(archive.read(original), data)
            checksums = json.loads(archive.read("checksums.json"))
            self.assertEqual(checksums["original/export.png"], sha(data))
            for name, digest in checksums.items():
                self.assertEqual(sha(archive.read(name)), digest)
        original_path = self.root / "studio" / "objects" / record["sha256"] / "original"
        os.chmod(original_path, 0o600)
        original_path.write_bytes(data[:-1] + b"!")
        for reader in (lambda: self.store.verify_original(record),
                       lambda: self.store.export_to(record["id"], io.BytesIO())):
            with self.assertRaisesRegex(ValueError, "integrity"):
                reader()

    def test_single_request_ingest_still_accepts_bytes(self):
        data = body(SINGLE)
        record, duplicate = self.store.ingest("single.png", data)
        self.assertFalse(duplicate)
        self.assertEqual(self.store.original_bytes(record), data)
        self.assertEqual(list((self.root / "studio").glob("upload-*")), [])
        with self.assertRaisesRegex(ValueError, "Unsupported file content"):
            self.store.ingest("text.png", b"plain text")
        self.assertEqual(list((self.root / "studio").glob("upload-*")), [])

    def test_handoff_accepts_every_stored_size(self):
        self.assertEqual(handoff.MAX_BYTES, intake_backend.MAX_BYTES)
        self.assertEqual(intake_backend.MAX_BYTES, 2 * 1024 ** 3)


@unittest.skipIf(os.environ.get("KFM_NO_NETWORK") == "1",
                 "Loopback HTTP is tested separately; keep the no-network guard enforced")
class LargeUploadHttpTests(unittest.TestCase):
    def setUp(self):
        self.enterContext(patch.multiple(intake_backend, UPLOAD_CHUNK_BYTES=CHUNK, SINGLE_UPLOAD_BYTES=SINGLE))
        self.enterContext(patch("tools.local_data.intake_studio.intake_server.subprocess.run",
                                side_effect=fake_extract))
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        self.server = Server(0, Store(root / "studio", root / "missing-runtime"))
        self.auth = signed_in_headers(self, self.server.accounts)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def call(self, path, data=None, headers=None, kind="application/json"):
        request = urllib.request.Request(self.server.origin + path, data=data, method="POST" if data is not None else "GET",
                                         headers={**self.auth, "Origin": self.server.origin, "Content-Type": kind,
                                                  **(headers or {})})
        try:
            with urllib.request.urlopen(request) as response:
                return response.status, response.read()
        except urllib.error.HTTPError as error:
            with error:
                return error.code, error.read()

    def test_protocol_round_trip_and_streamed_downloads(self):
        status, raw = self.call("/api/session")
        session = json.loads(raw)
        self.assertEqual((status, session["maxBytes"], session["singleUploadBytes"], session["uploadChunkBytes"]),
                         (200, 2 * 1024 ** 3, SINGLE, CHUNK))
        data = body(2 * CHUNK + 77)
        status, raw = self.call("/api/upload?name=too-big.png", data[:SINGLE + 1], kind="application/octet-stream")
        self.assertEqual(status, 413)
        status, raw = self.call("/api/uploads", json.dumps({"name": "map.png", "size": len(data)}).encode())
        self.assertEqual(status, 201)
        upload = json.loads(raw)["upload"]
        status, raw = self.call(f"/api/uploads/{upload['id']}/chunk?offset=0", data[:CHUNK],
                                kind="application/octet-stream")
        self.assertEqual(status, 400)
        self.assertIn(b"SHA-256", raw)
        offset = 0
        while offset < len(data):
            part = data[offset:offset + CHUNK]
            status, raw = self.call(f"/api/uploads/{upload['id']}/chunk?offset={offset}", part,
                                    {"X-KFM-Chunk-SHA256": sha(part)}, "application/octet-stream")
            self.assertEqual(status, 200, raw)
            offset = json.loads(raw)["upload"]["received"]
        status, raw = self.call(f"/api/uploads/{upload['id']}/chunk?offset=0", data[:CHUNK],
                                {"X-KFM-Chunk-SHA256": sha(data[:CHUNK])}, "application/octet-stream")
        self.assertEqual(status, 409)
        status, raw = self.call(f"/api/uploads/{upload['id']}")
        self.assertEqual(json.loads(raw)["upload"]["received"], len(data))
        status, raw = self.call(f"/api/uploads/{upload['id']}/complete", b"{}")
        self.assertEqual(status, 201, raw)
        record = json.loads(raw)["file"]
        status, original = self.call(f"/api/files/{record['id']}/original")
        self.assertEqual((status, original), (200, data))
        status, package = self.call(f"/api/files/{record['id']}/export")
        self.assertEqual(status, 200)
        with zipfile.ZipFile(io.BytesIO(package)) as archive:
            self.assertEqual(archive.read("original/map.png"), data)
        status, _ = self.call(f"/api/uploads/{upload['id']}")
        self.assertEqual(status, 404)

    def test_viewers_and_anonymous_clients_cannot_upload(self):
        start = json.dumps({"name": "map.png", "size": 10}).encode()
        anonymous = urllib.request.Request(self.server.origin + "/api/uploads", data=start, method="POST",
                                           headers={"Origin": self.server.origin, "Content-Type": "application/json"})
        with self.assertRaises(urllib.error.HTTPError) as error:
            urllib.request.urlopen(anonymous)
        self.assertEqual(error.exception.code, 401)
        error.exception.close()
        status, _ = self.call("/api/uploads", start, {"X-KFM-CSRF": "wrong"})
        self.assertEqual(status, 403)
        principal = self.server.accounts.session(self.auth["Cookie"].split("=", 1)[1])
        with patch.object(self.server.accounts, "session", return_value={**principal, "role": "viewer"}):
            status, raw = self.call("/api/uploads", start)
        self.assertEqual((status, json.loads(raw)["error"]), (403, "READ_ONLY_ACCOUNT"))


if __name__ == "__main__":
    unittest.main()
