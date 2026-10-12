"""Pinned private review: bounded bytes, negative paths and no lifecycle changes."""
import hashlib
import json
import os
from pathlib import Path
import struct
import tempfile
import unittest

from tests.local_data import test_intake as service_tests
from tools.local_data import intake_service, review_packages as review
from tools.local_data.manage import init_store


class ReviewPackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "store"
        init_store(self.root)
        self.package = self.root / "data/work/hydrology/example"
        self.package.mkdir(parents=True)
        self.file = self.package / "series.json"
        self.file.write_text(json.dumps({"rows": [{"station": "Kansas <script>alert(1)</script>", "value": None,
                                                  "released": False}] * 45}))
        self.manifest = {"profile": "kfm-water-metadata-availability-review/v1", "review_state": "PENDING",
                         "released": False, "published": False, "source_role": "Metadata, not observations"}
        self.pin()

    def tearDown(self):
        self.temporary.cleanup()

    def pin(self, *, outputs=None):
        files = [self.file] if outputs is None else outputs
        if files and isinstance(files[0], Path):
            files = [{"file": str(p.relative_to(self.package)), "bytes": p.stat().st_size,
                      "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
        self.manifest["outputs"] = files
        self.manifest["output_bytes"] = sum(r["bytes"] for r in files)
        self.manifest_path = self.package / "review-manifest.json"
        self.manifest_path.write_text(json.dumps(self.manifest))
        self.digest = hashlib.sha256(self.manifest_path.read_bytes()).hexdigest()
        self.binding = str(self.manifest_path.relative_to(self.root)) + "@" + self.digest
        self.model = review.ReviewPackages(self.root, [self.binding])
        self.member = review.member_id(files[0]) if files else None

    def test_empty_selection_never_discovers_work_or_source_bytes(self):
        self.assertEqual(review.ReviewPackages(self.root).catalog()["packages"], [])
        with self.assertRaisesRegex(ValueError, "PACKAGE_UNKNOWN"):
            review.ReviewPackages(self.root).preview(self.digest, self.member)

    def test_search_preserves_missing_values_and_false_authority_with_explicit_limits(self):
        value, mime = self.model.preview(self.digest, self.member, text="Kansas")
        self.assertEqual((mime, value["matchedRows"], value["shownRows"]), ("application/json", 45, 40))
        self.assertTrue(value["truncated"])
        self.assertIsNone(json.loads(value["text"])[0]["value"])
        self.assertFalse(any(value["authority"].values()))
        self.assertIn("<script>", value["text"])  # must remain text in the DOM
        self.assertEqual(self.manifest_path.read_text(), json.dumps(self.manifest))

    def test_changed_member_is_rejected_even_when_size_and_mtime_are_preserved(self):
        info = self.file.stat()
        self.file.write_text(self.file.read_text().replace("Kansas", "Nebras"))
        os.utime(self.file, ns=(info.st_atime_ns, info.st_mtime_ns))
        with self.assertRaisesRegex(ValueError, "MEMBER_CHANGED"):
            self.model.preview(self.digest, self.member)

    def test_changed_manifest_is_rejected_by_catalog_and_preview(self):
        self.manifest_path.write_text(self.manifest_path.read_text() + " ")
        for operation in (self.model.catalog, lambda: self.model.preview(self.digest, self.member)):
            with self.assertRaisesRegex(ValueError, "MANIFEST_CHANGED"): operation()

    def test_traversal_links_special_files_and_unselected_members_are_denied(self):
        for path in ("../outside", "/etc/passwd", "data/work/../raw/a/review-manifest.json", "data/work/a//review-manifest.json",
                     "data/raw/a/review-manifest.json", "data/work/.private/a/review-manifest.json"):
            with self.subTest(path=path), self.assertRaises(ValueError): review.ReviewPackages(self.root, [path + "@" + self.digest])
        for bad in ("../outside", "a" * 64):
            with self.assertRaises(ValueError): self.model.preview(self.digest, bad)
        retained = self.package / "retained.json"; self.file.rename(retained); self.file.symlink_to(retained)
        with self.assertRaisesRegex(ValueError, "SYMLINK"): self.model.preview(self.digest, self.member)
        self.file.unlink(); os.mkfifo(self.file)
        with self.assertRaisesRegex(ValueError, "SPECIAL"): self.model.preview(self.digest, self.member)

    def test_manifest_symlink_and_linked_parent_are_denied(self):
        retained = self.package / "retained-manifest.json"; self.manifest_path.rename(retained); self.manifest_path.symlink_to(retained)
        with self.assertRaisesRegex(ValueError, "SYMLINK"): review.ReviewPackages(self.root, [self.binding])
        self.manifest_path.unlink(); retained.rename(self.manifest_path)
        moved = self.package.with_name("retained"); self.package.rename(moved); self.package.symlink_to(moved)
        with self.assertRaisesRegex(ValueError, "SYMLINK"): self.model.catalog()

    def test_release_flags_unsupported_formats_and_expansion_budgets_fail_closed(self):
        for field, value in (("released", True), ("published", True), ("review_state", "APPROVED"), ("profile", "unknown")):
            old = self.manifest[field]; self.manifest[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "STATE_UNSUPPORTED"): self.pin()
            self.manifest[field] = old
        for file in ("../outside.json", "raw.pdf", "script.svg", "review-manifest.json"):
            with self.subTest(file=file), self.assertRaises(ValueError):
                self.pin(outputs=[{"file": file, "bytes": 1, "sha256": "a" * 64}])
        with self.assertRaisesRegex(ValueError, "BYTE_LIMIT"):
            self.pin(outputs=[{"file": f"{i}.json", "bytes": review.MEMBER_LIMIT, "sha256": "a" * 64} for i in range(17)])

    def test_png_dimensions_are_bounded_and_svg_is_never_returned(self):
        png = self.package / "page.png"
        png.write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", 3200, 1974) + b"\x08\x02" + b"\0" * 7)
        self.pin(outputs=[png])
        raw, mime = self.model.preview(self.digest, self.member)
        self.assertEqual((raw, mime), (png.read_bytes(), "image/png"))
        png.write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", 4097, 1) + b"\x08\x02" + b"\0" * 7)
        self.pin(outputs=[png])
        with self.assertRaisesRegex(ValueError, "IMAGE_LIMIT"): self.model.preview(self.digest, self.member)

    def test_busy_preview_recovers_after_capacity_is_released(self):
        self.model.slots.acquire(); self.model.slots.acquire()
        with self.assertRaisesRegex(ValueError, "BUSY"): self.model.preview(self.digest, self.member)
        self.model.slots.release(); self.model.slots.release()
        self.assertEqual(self.model.preview(self.digest, self.member)[0]["reviewState"], "PENDING")


class ReviewServiceTests(unittest.TestCase):
    request = service_tests.ServiceTests.request
    pin = ReviewPackageTests.pin
    tearDown = ReviewPackageTests.tearDown

    def setUp(self):
        ReviewPackageTests.setUp(self)
        self.desk = intake_service.Desk(self.root, review_bindings=[self.binding])

    def test_private_routes_require_session_and_reject_explorer_origins(self):
        path = f"/api/reviews/{self.digest}/{self.member}"
        for request in ("/api/reviews", path):
            self.assertEqual(self.request("GET", request, headers={"X-KFM-Session": None})[0], 403)
            self.assertEqual(self.request("GET", request, headers={"Origin": "http://127.0.0.1:4173"})[0], 403)
            self.assertEqual(self.request("GET", request, headers={"Origin": None})[0], 200)
        self.assertFalse(any(self.request("GET", path)[1]["authority"].values()))

    def test_queries_do_not_accept_paths_unknown_fields_or_duplicate_filters(self):
        path = f"/api/reviews/{self.digest}/{self.member}"
        for query in ("?path=/etc/passwd", "?text=a&text=b", "?text=" + "x" * 101):
            self.assertEqual(self.request("GET", path + query)[0], 400)
        self.assertEqual(self.request("GET", "/api/reviews/../outside")[0], 400)
        self.assertEqual(self.request("GET", path + "?text=Kansas")[1]["matchedRows"], 45)

    def test_parallel_review_desk_cannot_start_analysis_or_apply_any_action(self):
        self.desk.read_only = True
        self.assertFalse(self.desk.status()["analysisAllowed"])
        with self.assertRaisesRegex(ValueError, "READ_ONLY_DESK"): self.desk.start({})
        for path in ("/api/analyze", "/api/cancel", "/api/apply", "/api/atlas/preview"):
            self.assertEqual(self.request("POST", path)[0:2], (403, {"error": "READ_ONLY_DESK"}))
        self.assertEqual(self.request("GET", "/api/reviews")[0], 200)
        for path in ("/api/overview", "/api/items", "/api/budget", "/api/release-plan"):
            self.assertEqual(self.request("GET", path)[0:2], (403, {"error": "READ_ONLY_DESK"}))

    def test_nondefault_loopback_port_keeps_exact_host_and_origin_checks(self):
        self.assertEqual(self.request("GET", "/api/reviews", port=8772)[0], 200)
        self.assertEqual(self.request("GET", "/api/reviews", port=8772, headers={"Host": "127.0.0.1:8771"})[0], 403)
        self.assertEqual(self.request("GET", "/api/reviews", port=8772, headers={"Origin": "http://127.0.0.1:8771"})[0], 403)


if __name__ == "__main__":
    unittest.main()
