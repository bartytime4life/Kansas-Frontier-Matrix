"""Operator review decisions persist, bind to bytes, and retain sharing restrictions."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest

from tests.local_data import intake_samples as samples, test_intake as fixtures
from tools.local_data import intake, intake_review, intake_service
from tools.local_data.manage import init_store


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "store"
        init_store(self.root)
        self.source = self.root / "data/raw/misc/gauges.geojson"
        self.source.parent.mkdir(parents=True)
        self.source.write_bytes(samples.GEOJSON)
        self.budget = fixtures.budget(github_limit_bytes=10**12, reserved_for_code_and_interface_bytes=10**11, committed=[])
        intake.analyze(self.root, budget=self.budget)
        self.identity = intake.item_id("raw", "misc/gauges.geojson")

    def tearDown(self):
        self.temporary.cleanup()

    def item(self):
        return intake.get_item(self.root, self.identity)

    def request(self, **patch):
        item = self.item()
        return {"id": self.identity, "sha256": item["sha256"], "revision": item["review_history"][0]["revision"] if item["review_history"] else 0,
                "decision": "local", "domain": "hydrology", "rights": "unknown", "sensitivity": "unknown",
                "reference": "", "reviewer": "Test operator", "note": "Checked the file metadata for local use.", "confirmed": True, **patch}

    def save(self, **patch):
        return intake_review.save(self.root, self.request(**patch), self.budget)

    def test_local_review_clears_queue_without_enabling_sharing_and_survives_analysis(self):
        before = self.source.read_bytes()
        result = self.save()
        self.assertEqual(result["status"], "reviewed")
        item = self.item()
        self.assertEqual(item["decision"]["status"], "reviewed")
        self.assertIn("RIGHTS_UNKNOWN", item["decision"]["holds"])
        self.assertFalse(any(p["action"] in {"candidate", "metadata_card"} for p in item["decision"]["placements"]))
        self.assertEqual(intake.release_plan(self.root, self.budget)["selected"], [])
        self.assertEqual(intake.overview(self.root, self.budget)["by_status"]["reviewed"]["files"], 1)
        self.assertTrue((self.root / result["review"]["receipt"]).is_file())
        intake.analyze(self.root, budget=self.budget)
        self.assertEqual(self.item()["decision"]["operator_review"]["reviewer"], "Test operator")
        self.assertEqual(self.item()["decision"]["status"], "reviewed")
        self.assertEqual(before, self.source.read_bytes())
        self.assertIsNone(self.item()["declared"])

    def test_public_review_requires_explicit_details_and_enables_only_planning(self):
        with self.assertRaisesRegex(ValueError, "REVIEW_PUBLIC_DETAILS_REQUIRED"):
            self.save(decision="public")
        result = self.save(decision="public", rights="allowed", sensitivity="public", reference="Test provider redistribution policy")
        self.assertEqual(result["status"], "ready")
        self.assertEqual(len(intake.release_plan(self.root, self.budget)["selected"]), 1)
        card = intake.cards(self.root)[0]
        self.assertEqual(card["operator_review"]["reference"], "Test provider redistribution policy")
        self.assertNotIn("reviewer", card["operator_review"])
        self.assertNotIn("note", card["operator_review"])
        self.assertFalse(any(self.item()["decision"]["authority"].values()))
        intake.analyze(self.root, budget=self.budget)
        self.assertEqual(self.item()["decision"]["status"], "ready")

    def test_reopen_restores_original_holds_and_preserves_audit_history(self):
        first = self.save()
        second = self.save(decision="reopen", note="Reopened to investigate a remaining question.")
        self.assertGreater(second["review"]["revision"], first["review"]["revision"])
        self.assertEqual(self.item()["status"], "review")
        self.assertNotIn("operator_review", self.item()["decision"])
        self.assertEqual([r["decision"] for r in self.item()["review_history"]], ["reopen", "local"])
        intake.analyze(self.root, budget=self.budget)
        self.assertEqual(self.item()["status"], "review")

    def test_stale_revision_and_changed_bytes_are_rejected_without_new_decisions(self):
        old = self.request()
        self.save()
        with self.assertRaisesRegex(ValueError, "REVIEW_STALE_DECISION"):
            intake_review.save(self.root, old, self.budget)
        self.source.write_bytes(samples.GEOJSON.replace(b"2021-03-04", b"2022-03-04"))
        with self.assertRaisesRegex(ValueError, "REVIEW_CONTENT_CHANGED_REANALYZE"):
            self.save()
        self.assertEqual(len(self.item()["review_history"]), 1)

    def test_byte_changes_revoke_prior_public_review_even_if_size_and_mtime_match(self):
        self.save(decision="public", rights="allowed", sensitivity="public", reference="Test provider redistribution policy")
        info = self.source.stat()
        self.source.write_bytes(samples.GEOJSON.replace(b"2021-03-04", b"2022-03-04"))
        os.utime(self.source, ns=(info.st_atime_ns, info.st_mtime_ns))
        intake.analyze(self.root, budget=self.budget)
        self.assertEqual(self.item()["status"], "review")
        self.assertNotIn("operator_review", self.item()["decision"])
        self.assertEqual(len(self.item()["review_history"]), 1)

    def test_decision_does_not_spread_to_same_bytes_in_another_source(self):
        other = self.root / "data/raw/other/gauges.geojson"
        other.parent.mkdir()
        other.write_bytes(samples.GEOJSON)
        intake.analyze(self.root, budget=self.budget)
        self.save()
        self.assertEqual(intake.get_item(self.root, intake.item_id("raw", "other/gauges.geojson"))["status"], "review")

    def test_known_capture_restrictions_cannot_be_cleared_by_public_review(self):
        with intake.open_index(self.root) as conn:
            conn.execute("UPDATE items SET declared_json=? WHERE id=?", (json.dumps({"rights": {"redistribution": "restricted"}, "sensitivity": "public"}), self.identity))
        with self.assertRaisesRegex(ValueError, "REVIEW_CAPTURE_RESTRICTION_REMAINS"):
            self.save(decision="public", rights="allowed", sensitivity="public", reference="A new unqualified reference")
        self.assertEqual(self.item()["review_history"], [])

    def test_sensitive_flags_cannot_be_cleared_by_public_review(self):
        profile = self.item()["profile"]
        with intake.open_index(self.root) as conn:
            profile["hints"]["review_flags"] = ["possible_living_persons"]
            conn.execute("UPDATE items SET profile_json=? WHERE id=?", (json.dumps(profile), self.identity))
        with self.assertRaisesRegex(ValueError, "REVIEW_PUBLIC_HOLDS_REMAIN"):
            self.save(decision="public", rights="allowed", sensitivity="public", reference="Test provider policy")
        self.assertEqual(self.save()["status"], "reviewed")
        self.assertIn("REVIEW_FLAGS", self.item()["decision"]["holds"])

    def test_choosing_another_domain_does_not_clear_a_sensitive_domain_flag(self):
        profile = self.item()["profile"]
        with intake.open_index(self.root) as conn:
            profile["hints"]["domain"], profile["hints"]["review_flags"] = "archaeology", []
            conn.execute("UPDATE items SET profile_json=? WHERE id=?", (json.dumps(profile), self.identity))
        with self.assertRaisesRegex(ValueError, "REVIEW_PUBLIC_HOLDS_REMAIN"):
            self.save(decision="public", domain="hydrology", rights="allowed", sensitivity="public", reference="Test provider policy")
        self.assertEqual(self.save(domain="hydrology")["status"], "reviewed")
        decision = self.item()["decision"]
        self.assertIn("sensitive_domain", decision["review_flags"])
        self.assertIn("REVIEW_FLAGS", decision["holds"])
        self.assertEqual(intake.release_plan(self.root, self.budget)["selected"], [])

    def test_confirmation_and_a_meaningful_note_are_required(self):
        for patch in ({"confirmed": False}, {"note": "ok"}, {"reviewer": ""}, {"domain": "../../outside"}, {"decision": []}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                self.save(**patch)
        self.assertEqual(self.item()["review_history"], [])

    def test_changed_capture_context_invalidates_the_decision(self):
        self.save()
        item = self.item()
        with intake.open_index(self.root) as conn:
            item["declared"] = {"sensitivity": "controlled"}
            self.assertIsNone(intake_review.current(conn, item, item["profile"]))


class ReviewApiTests(unittest.TestCase):
    request = fixtures.ServiceTests.request

    def setUp(self):
        self.fixture = ReviewTests()
        self.fixture.setUp()
        self.root = self.fixture.root
        self.desk = intake_service.Desk(self.root, budget=self.fixture.budget)

    def tearDown(self):
        self.fixture.tearDown()

    def test_authenticated_same_origin_review_updates_item(self):
        status, body, _ = self.request("POST", "/api/review", self.fixture.request(), port=8772)
        self.assertEqual((status, body["status"]), (200, "reviewed"))
        self.assertTrue(self.request("GET", "/api/status", port=8772)[1]["reviewAllowed"])

    def test_review_rejects_missing_token_foreign_origin_and_read_only_desk(self):
        body = self.fixture.request()
        self.assertEqual(self.request("POST", "/api/review", body, {"X-KFM-Session": None})[0], 403)
        self.assertEqual(self.request("POST", "/api/review", body, {"Origin": "https://other.example"})[0], 403)
        self.assertEqual(self.request("POST", "/api/review", body, {"Origin": next(iter(intake_service.SITE_ORIGINS))})[0], 403)
        self.desk.read_only = True
        self.assertEqual(self.request("POST", "/api/review", body)[0], 403)
        self.desk.read_only, self.desk.catalog_only = False, True
        self.assertEqual(self.request("POST", "/api/review", body)[0], 403)
        self.assertEqual(self.fixture.item()["review_history"], [])

    def test_review_does_not_race_active_analysis(self):
        self.desk.job["state"] = "running"
        status, body, _ = self.request("POST", "/api/review", self.fixture.request())
        self.assertEqual((status, body["error"]), (400, "ANALYSIS_ALREADY_RUNNING"))


if __name__ == "__main__":
    unittest.main()
