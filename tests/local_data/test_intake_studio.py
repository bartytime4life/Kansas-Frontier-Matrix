import os, unittest, tempfile, io, json, zipfile, hashlib, threading, urllib.request, urllib.error
from pathlib import Path
from unittest.mock import patch

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    Image = ImageDraw = ImageFont = None
from tools.local_data.intake_studio.intake_server import (
    Store,
    Server,
    signature,
    clean_name,
)

RUNTIME = Path(
    os.environ.get(
        "KFM_INTAKE_TEST_RUNTIME", str(Path.home() / ".local/share/kfm-intake-runtime")
    )
)
NATIVE = os.environ.get("KFM_INTAKE_NATIVE_TESTS") == "1"


def fake_extract(cmd, **kwargs):
    work = Path(cmd[cmd.index("--bind") + 1])
    (work / "analysis.json").write_text(
        json.dumps(
            {
                "status": "Partial",
                "method": "Synthetic unit-test extraction",
                "pages": 1,
                "text": "water river aquifer",
                "metadata": {},
                "warnings": [],
                "suggestions": [],
                "flags": [],
            }
        )
    )
    return type("Result", (), {"returncode": 0})()


def fixture():
    im = Image.new("RGB", (1400, 500), "white")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
    draw.text((55, 70), "KANSAS WATER FIELD NOTES", fill="black", font=font)
    draw.text(
        (55, 170), "River water and aquifer observations", fill="black", font=font
    )
    out = io.BytesIO()
    im.save(out, format="PNG")
    return out.getvalue()


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.store = Store(cls.temp.name, RUNTIME)
        cls.image = fixture() if NATIVE else b"\x89PNG\r\n\x1a\nsynthetic"
        cls.record = None
        if not NATIVE:
            cls.mock = patch(
                "tools.local_data.intake_studio.intake_server.subprocess.run",
                side_effect=fake_extract,
            )
            cls.mock.start()
        cls.record, _ = cls.store.ingest("water-notes.png", cls.image)

    @classmethod
    def tearDownClass(cls):
        if not NATIVE:
            cls.mock.stop()
        cls.temp.cleanup()

    @unittest.skipUnless(
        NATIVE,
        "Set KFM_INTAKE_NATIVE_TESTS=1 with the sandbox, Pillow and OCR runtime installed",
    )
    def test_ocr_and_preview(self):
        a = self.record["analysis"]
        self.assertNotEqual(a["status"], "Failed", a)
        self.assertIn("water", a["text"].lower())
        self.assertTrue(self.record["preview"])
        self.assertEqual(a["suggestions"][0]["domain"], "hydrology")

    def test_missing_runtime_is_not_reported_available(self):
        with tempfile.TemporaryDirectory() as root:
            store = Store(root, Path(root) / "missing-runtime")
            with patch(
                "tools.local_data.intake_studio.intake_server.subprocess.run",
                return_value=type("Result", (), {"returncode": 0})(),
            ):
                capabilities = store.capabilities()
            self.assertFalse(capabilities["ocr"])
            self.assertFalse(capabilities["pdf"])

    def test_empty_ingest_refused(self):
        with self.assertRaises(ValueError):
            self.store.ingest("empty.png", b"")

    def test_corrupt_original_export_refused(self):
        with tempfile.TemporaryDirectory() as root:
            store = Store(root, RUNTIME)
            record, _ = store.ingest("copy.png", self.image)
            (store.objects / record["sha256"] / "original").write_bytes(b"corrupt")
            with self.assertRaisesRegex(ValueError, "integrity"):
                store.export(record["id"])

    def test_duplicate_keeps_separate_provenance(self):
        r, duplicate = self.store.ingest("second-source.png", self.image)
        self.assertTrue(duplicate)
        self.assertNotEqual(r["id"], self.record["id"])
        self.assertEqual(r["review"]["rights"], "Unknown")
        self.assertEqual(r["sha256"], self.record["sha256"])

    def test_unknown_and_executable_refused(self):
        with self.assertRaises(ValueError):
            signature(b"<script>alert(1)</script>")

    def test_safe_filename(self):
        self.assertEqual(clean_name(".."), "uploaded-file")
        self.assertNotIn("/", clean_name("../../unsafe.png"))

    def test_review_requirements_and_stale_version(self):
        r, _ = self.store.ingest("review.png", self.image)
        value = {
            "version": 1,
            **r["review"],
            "decision": "Ready for integration review",
        }
        with self.assertRaises(ValueError):
            self.store.review(r["id"], value)
        value.update(
            source="Synthetic test fixture owned by QA",
            rights="Owned by me",
            sensitivity="Public",
            domain="hydrology",
            surface="Reference library",
            reviewer="QA",
        )
        updated = self.store.review(r["id"], value)
        self.assertEqual(updated["review"]["decision"], "Ready for integration review")
        with self.assertRaises(RuntimeError):
            self.store.review(r["id"], value)
        updated = self.store.review(
            r["id"], {**value, "version": 2, "description": "Changed source context"}
        )
        self.assertEqual(updated["review"]["decision"], "Needs review")
        self.assertEqual(updated["integration"]["state"], "QUARANTINED_REVIEW_ONLY")

    def test_export_integrity(self):
        out = self.store.export(self.record["id"])
        z = zipfile.ZipFile(io.BytesIO(out))
        hashes = json.loads(z.read("checksums.json"))
        for name, digest in hashes.items():
            self.assertEqual(hashlib.sha256(z.read(name)).hexdigest(), digest)
        self.assertEqual(z.read("original/water-notes.png"), self.image)
        self.assertFalse(
            json.loads(z.read("review-proposal.json"))["authority"]["publication"]
        )

    def test_restart_persistence(self):
        self.assertEqual(
            Store(self.temp.name, RUNTIME).get(self.record["id"])["sha256"],
            self.record["sha256"],
        )

    @unittest.skipUnless(
        NATIVE,
        "Set KFM_INTAKE_NATIVE_TESTS=1 with the sandbox, Pillow and OCR runtime installed",
    )
    def test_malformed_image_preserved_and_held(self):
        r, _ = self.store.ingest("bad.png", b"\x89PNG\r\n\x1a\ninvalid")
        self.assertEqual(r["analysis"]["status"], "Failed")
        self.assertEqual(r["review"]["decision"], "Needs review")

    def test_sensitivity_flags(self):
        r, _ = self.store.ingest("flags.png", self.image)
        v = {
            "version": 1,
            **r["review"],
            "description": "archaeological burial location",
            "source": "test",
            "rights": "Owned by me",
            "sensitivity": "Public",
            "domain": "archaeology",
            "surface": "Reference library",
            "reviewer": "QA",
            "decision": "Ready for integration review",
        }
        r = self.store.review(r["id"], v)
        self.assertEqual(r["review"]["decision"], "Needs review")
        self.assertTrue(r["analysis"]["flags"])

    @unittest.skipUnless(
        NATIVE,
        "Set KFM_INTAKE_NATIVE_TESTS=1 with the sandbox, Pillow and OCR runtime installed",
    )
    def test_pdf_scanned(self):
        im = Image.open(io.BytesIO(self.image))
        out = io.BytesIO()
        im.save(out, format="PDF")
        r, _ = self.store.ingest("scan.pdf", out.getvalue())
        self.assertEqual(r["analysis"]["pages"], 1)
        self.assertIn("water", r["analysis"]["text"].lower())
        self.assertTrue(r["preview"])

    @unittest.skipIf(
        os.environ.get("KFM_NO_NETWORK") == "1",
        "Loopback HTTP is tested separately; keep the no-network guard enforced",
    )
    def test_http_boundaries(self):
        server = Server(0, self.store)
        server.origin = f"http://127.0.0.1:{server.server_port}"
        threading.Thread(target=server.serve_forever, daemon=True).start()

        def request(path, headers={}):
            return urllib.request.urlopen(
                urllib.request.Request(server.origin + path, headers=headers)
            )

        try:
            with patch.object(
                self.store, "capabilities", return_value={"note": "synthetic test"}
            ):
                with request("/api/session") as r:
                    session = json.load(r)
            for path, headers in [
                ("/api/files", {}),
                ("/api/session", {"Origin": "https://example.org"}),
                ("/api/session", {"Host": "evil.test"}),
            ]:
                with self.assertRaises(urllib.error.HTTPError) as e:
                    request(path, headers)
                self.assertEqual(e.exception.code, 403)
                e.exception.close()
            with request("/api/files", {"X-KFM-Token": session["token"]}) as r:
                self.assertTrue(json.load(r)["files"])
            with self.assertRaises(urllib.error.HTTPError) as error:
                request("/acceptance/../../intake_server.py")
            error.exception.close()
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
