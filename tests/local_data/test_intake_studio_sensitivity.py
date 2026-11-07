"""Synthetic, private-inbox regressions for durable sensitivity holds."""

import copy
import hashlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from tests.local_data.test_intake_studio import fake_extract
from tools.local_data.intake_studio.intake_server import Store, flags_for


class SensitivityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = Store(self.root, self.root / "missing-runtime")
        self.body = b"\x89PNG\r\n\x1a\nsynthetic sensitivity regression"
        with patch(
            "tools.local_data.intake_studio.intake_server.subprocess.run",
            side_effect=fake_extract,
        ):
            self.record, _ = self.store.ingest("synthetic.png", self.body)
        self.id = self.record["id"]
        self.original_analysis = (
            self.store.objects / self.record["sha256"] / "analysis.json"
        ).read_bytes()

    def save_review(self, **changes):
        record = self.store.get(self.id)
        return self.store.review(
            self.id, {**record["review"], "version": record["version"], **changes}
        )

    def ready(self):
        return self.save_review(
            source="Synthetic QA source",
            rights="Owned by me",
            sensitivity="Public",
            domain="hydrology",
            surface="Reference library",
            reviewer="Synthetic QA reviewer",
            decision="Ready for integration review",
        )

    def assert_held(self, record, expected):
        self.assertEqual(set(record["analysis"]["flags"]), set(expected))
        self.assertNotEqual(
            record["review"]["decision"], "Ready for integration review"
        )
        self.assertEqual(record["integration"]["state"], "QUARANTINED_REVIEW_ONLY")

    def test_description_replacement_cannot_clear_recorded_flag(self):
        flagged = self.save_review(description="archaeological burial location")
        flags = flagged["analysis"]["flags"]
        edited = self.save_review(description="Harmless water field notes")
        self.assert_held(edited, flags)
        before = copy.deepcopy(edited)
        with self.assertRaisesRegex(ValueError, "separate governed review"):
            self.ready()
        self.assertEqual(self.store.get(self.id), before)

    def test_multiple_edits_and_transitions_accumulate_flags_once(self):
        expected = []
        for description, decision in [
            ("archaeological burial location", "Needs review"),
            ("Harmless description", "Keep quarantined"),
            ("patient medical notes", "Needs review"),
            ("rare species nesting site", "Keep quarantined"),
            ("critical infrastructure pipeline", "Needs review"),
            ("archaeological burial location", "Keep quarantined"),
            ("", "Needs review"),
        ]:
            with self.subTest(description=description, decision=decision):
                expected = list(dict.fromkeys(expected + flags_for(description)))
                saved = self.save_review(description=description, decision=decision)
                self.assert_held(saved, expected)
                self.assertEqual(len(saved["analysis"]["flags"]), len(expected))
        with self.assertRaisesRegex(ValueError, "separate governed review"):
            self.ready()

    def test_interrupted_save_and_reopened_store_preserve_last_commit(self):
        flagged = self.save_review(description="archaeological burial location")
        stale = {**flagged["review"], "version": flagged["version"]}
        edited = self.save_review(description="Harmless text")
        # Simulate a lost response followed by retrying the old session's save.
        with self.assertRaises(RuntimeError):
            self.store.review(self.id, stale)
        # A failure at the persistence boundary must not change the saved row.
        with (
            patch.object(self.store, "save", side_effect=OSError("interrupted")),
            self.assertRaises(OSError),
        ):
            self.save_review(description="Another harmless edit")
        self.store = Store(self.root, self.root / "missing-runtime")
        self.assertEqual(self.store.get(self.id), edited)
        self.assert_held(self.store.get(self.id), flagged["analysis"]["flags"])
        with self.assertRaisesRegex(ValueError, "separate governed review"):
            self.ready()

    def test_legacy_erased_flags_recovered_from_history_without_rewriting_disk(self):
        flagged = self.save_review(description="archaeological burial location")
        legacy = self.save_review(description="Harmless text")
        # Model a record already affected by the merged bug, including a saved
        # ready decision. Existing review history is the recovery evidence.
        legacy["analysis"]["flags"] = []
        legacy["review"]["decision"] = "Ready for integration review"
        self.store.save(legacy)
        with self.store.db() as db:
            persisted = db.execute(
                "SELECT data FROM files WHERE id=?", (self.id,)
            ).fetchone()[0]
        history = copy.deepcopy(legacy["history"])
        self.store = Store(self.root, self.root / "missing-runtime")
        for record in (self.store.get(self.id), self.store.list()[0]):
            self.assert_held(record, flagged["analysis"]["flags"])
            self.assertEqual(record["history"], history)
        with self.store.db() as db:
            self.assertEqual(
                db.execute("SELECT data FROM files WHERE id=?", (self.id,)).fetchone()[
                    0
                ],
                persisted,
            )
        with self.assertRaisesRegex(ValueError, "separate governed review"):
            self.ready()

        saved = self.save_review(decision="Needs review")
        self.assert_held(saved, flagged["analysis"]["flags"])
        self.assertEqual(saved["history"][:-1], history)
        self.assertEqual(saved["history"][-1]["previousReview"], legacy["review"])

    def test_current_description_and_extraction_flags_remain_held(self):
        # Recovery also covers older records without per-review history.
        for flags, description in [
            (["Synthetic extraction restriction"], "Harmless text"),
            ([], "patient medical notes"),
        ]:
            with self.subTest(flags=flags, description=description):
                record = copy.deepcopy(self.record)
                record["analysis"]["flags"] = flags
                record["review"]["description"] = description
                self.store.save(record)
                expected = flags + flags_for(description)
                self.assert_held(self.save_review(description=""), expected)
                with self.assertRaisesRegex(ValueError, "separate governed review"):
                    self.ready()

    def test_review_payload_cannot_authorize_clearance(self):
        self.save_review(description="archaeological burial location")
        before = self.store.get(self.id)
        for field, value in [
            ("flags", []),
            ("analysis", {"flags": []}),
            ("clearSensitivity", True),
        ]:
            with self.subTest(field=field):
                with self.assertRaisesRegex(ValueError, "Unexpected review field"):
                    self.save_review(**{field: value})
                self.assertEqual(self.store.get(self.id), before)

    def test_recorded_audit_flags_and_previous_review_snapshots_are_recovered(self):
        record = copy.deepcopy(self.record)
        record["history"].append(
            {
                "previousReview": {"description": "archaeological burial location"},
                "review": {"description": "Harmless text"},
                "sensitivityFlags": ["Synthetic historical extraction restriction"],
            }
        )
        self.store.save(record)
        expected = ["Synthetic historical extraction restriction"] + flags_for(
            "archaeological burial location"
        )
        self.assert_held(self.store.get(self.id), expected)
        self.assert_held(self.save_review(description=""), expected)
        with self.assertRaisesRegex(ValueError, "separate governed review"):
            self.ready()

    def test_exports_and_provenance_preserved_after_edits(self):
        flagged = self.save_review(description="archaeological burial location")
        old_export = self.store.export(self.id)
        self.save_review(description="Harmless text")
        self.store = Store(self.root, self.root / "missing-runtime")
        for payload in (old_export, self.store.export(self.id)):
            with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                proposal = json.loads(archive.read("review-proposal.json"))
                self.assert_held(proposal["record"], flagged["analysis"]["flags"])
                self.assertFalse(any(proposal["authority"].values()))
                self.assertEqual(archive.read("original/synthetic.png"), self.body)
                for name, digest in json.loads(archive.read("checksums.json")).items():
                    self.assertEqual(
                        hashlib.sha256(archive.read(name)).hexdigest(), digest
                    )
        current = self.store.get(self.id)
        self.assertEqual(current["history"][:2], flagged["history"])
        self.assertEqual(current["occurrences"], self.record["occurrences"])
        self.assertEqual(
            (self.store.objects / current["sha256"] / "analysis.json").read_bytes(),
            self.original_analysis,
        )


if __name__ == "__main__":
    unittest.main()
