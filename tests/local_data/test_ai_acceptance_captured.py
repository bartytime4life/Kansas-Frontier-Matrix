"""Synthetic captured payloads exercise extraction and private-review boundaries."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

from tests.local_data import test_ai_acceptance as acceptance
from tools.local_data import ai_acceptance as ai, intake, intake_review, intake_route, manage


class CapturedAcceptanceTests(unittest.TestCase):
    setUp = acceptance.AcceptanceTests.setUp
    finish = acceptance.AcceptanceTests.finish
    request = acceptance.AcceptanceTests.request
    run_batch = acceptance.AcceptanceTests.run_batch

    def capture(self, *, name="notes/hydrology.TXT.GZ", content=None, **overrides):
        self.path.unlink(missing_ok=True)
        content = content if content is not None else gzip.compress(
            b"Synthetic Kansas river water notes for local QA only.", mtime=0)
        digest = hashlib.sha256(content).hexdigest()
        relative = f"qa-source/objects/sha256/{digest}/payload"
        payload = self.root / "data/quarantine" / relative
        payload.parent.mkdir(parents=True, exist_ok=True)
        payload.write_bytes(content)
        declared = {"source_id":"qa-source", "dataset_id":"notes", "version":"v1",
            "relative_path":name, "source_uri":"https://example.test/synthetic-water-notes",
            "domain":"hydrology", "sha256":digest, "size_bytes":len(content),
            "rights":{"redistribution":"unknown", "license_id":None}, "sensitivity":"unknown",
            **overrides}
        binding = self.root / "data/quarantine/qa-source/versions/notes/v1/notes.json"
        binding.parent.mkdir(parents=True, exist_ok=True)
        binding.write_bytes(manage.canonical(declared))
        intake.analyze(self.root)
        self.id = intake.item_id("quarantine", relative)
        return payload, binding

    def item(self):
        return intake.get_item(self.root, self.id)

    def queue_without_worker(self):
        with patch.object(self.manager, "launch", side_effect=lambda job, fd:os.close(fd)):
            self.manager.start(self.request())
        return self.manager.status()["job"]

    def test_declared_txt_gzip_extracts_payload_and_preserves_evidence_and_authority(self):
        payload, _ = self.capture()
        before = payload.read_bytes()
        packet = ai.packet_for(self.root, self.item())
        self.assertEqual(payload.name, "payload")
        self.assertIn("Synthetic Kansas river water", next(
            f["text"] for f in packet["facts"] if f["id"] == "gzip_text_1"))
        self.assertEqual(self.run_batch()["counts"], {"accepted":1})
        item = self.item()
        result = item["ai_review"]
        self.assertEqual(result["attribution"]["model_digest"], self.client.digest)
        self.assertEqual(result["attribution"]["requested_by"], "Test admin")
        self.assertTrue(result["attribution"]["text_extraction"]["crc_validated"])
        packet_bytes = (self.root / result["attribution"]["input_path"]).read_bytes()
        self.assertEqual(hashlib.sha256(packet_bytes).hexdigest(), result["attribution"]["input_sha256"])
        self.assertFalse(any(result["authority"].values()))
        self.assertFalse(any(item["decision"]["authority"].values()))
        self.assertIn("REVIEWED_LOCAL_ONLY", item["decision"]["holds"])
        self.assertEqual(intake.release_plan(self.root, intake_route.load_budget())["selected"], [])
        for lane in ("registry", "processed", "catalog", "triplets", "published"):
            self.assertEqual(list((self.root / "data" / lane).rglob("*")), [])
        self.assertEqual(payload.read_bytes(), before)

    def test_declared_name_selects_format_but_is_never_opened(self):
        decoy = Path(self.temp.name) / "outside.txt.gz"
        decoy.write_bytes(gzip.compress(b"OUTSIDE FILE MUST NEVER BE READ", mtime=0))
        payload, _ = self.capture(name=str(decoy))
        original = ai.text_sample.gzip_text
        with patch.object(ai.text_sample, "gzip_text", wraps=original) as reader:
            packet = ai.packet_for(self.root, self.item())
        reader.assert_called_once_with(payload)
        text = "".join(f["text"] for f in packet["facts"] if f["id"].startswith("gzip_text_"))
        self.assertIn("Synthetic Kansas", text)
        self.assertNotIn("OUTSIDE FILE", text)

    def test_nontext_declared_archive_remains_uninspected(self):
        self.capture(name="hydrology.csv.gz")
        with patch.object(ai.text_sample, "gzip_text") as reader:
            self.assertEqual(self.run_batch()["counts"], {"held":1})
        reader.assert_not_called()
        self.assertIn("ARCHIVE_CONTENT_NOT_INSPECTED", self.item()["ai_review"]["holds"])

    def test_declared_nontext_name_overrides_txt_gzip_physical_name(self):
        import copy
        self.path.unlink()
        self.path = self.root / "data/raw/hydrology.txt.gz"
        self.path.write_bytes(gzip.compress(b"Synthetic water notes.", mtime=0))
        intake.analyze(self.root)
        item = copy.deepcopy(intake.get_item(self.root, intake.item_id("raw", self.path.name)))
        item["declared"] = {"relative_path":"hydrology.bin.gz"}
        with patch.object(ai.text_sample, "gzip_text", wraps=ai.text_sample.gzip_text) as reader:
            packet = ai.packet_for(self.root, item)
        reader.assert_not_called()
        self.assertFalse(any(f["id"] == "gzip_inspection" for f in packet["facts"]))

    def test_corrupt_captured_archives_retain_deterministic_holds(self):
        valid = gzip.compress(b"Synthetic Kansas river water notes for QA.", mtime=0)
        invalid = {
            "truncated":valid[:-4],
            "crc":valid[:-8] + bytes([valid[-8] ^ 255]) + valid[-7:],
            "trailing":valid + b"unchecked trailing bytes",
        }
        for label, content in invalid.items():
            with self.subTest(label=label):
                self.capture(content=content)
                self.run_batch(retryHeld=True)
                item = self.item()
                self.assertEqual(item["status"], "review")
                self.assertIn("GZIP_EXTRACTION_REQUIRES_ADMIN", item["ai_review"]["holds"])
                self.assertEqual(item["review_history"], [])

    def test_declared_restrictions_cannot_be_cleared_by_a_high_confidence_model(self):
        restrictions = [
            {"sensitivity":"controlled"}, {"sensitivity":"restricted"},
            {"rights":{"redistribution":"restricted"}}, {"rights":{"redistribution":"denied"}},
        ]
        for restriction in restrictions:
            with self.subTest(restriction=restriction):
                self.capture(**restriction)
                self.run_batch(retryHeld=True)
                self.assertEqual(self.item()["status"], "review")
                self.assertEqual(self.item()["review_history"], [])
                self.assertTrue(self.item()["ai_review"]["holds"])

    def test_sensitive_content_concern_cannot_be_overridden_by_accept_local(self):
        self.capture()
        original = self.client.review
        def review(packet):
            result, digest = original(packet)
            result["concerns"] = [ai.grounded_review.CONCERNS["sensitive_content"]]
            return result, digest
        self.client.review = review
        self.assertEqual(self.run_batch()["counts"], {"held":1})
        self.assertIn("CONTENT_SENSITIVITY_REQUIRES_ADMIN", self.item()["ai_review"]["holds"])
        self.assertEqual(self.item()["review_history"], [])

    def test_ai_save_cannot_request_public_clearance_or_rewrite_capture_restrictions(self):
        self.capture(sensitivity="controlled")
        item = self.item()
        request = {"id":self.id, "sha256":item["sha256"], "revision":0,
            "decision":"local", "domain":"hydrology", "rights":"unknown", "sensitivity":"controlled",
            "reference":"", "reviewer":"Synthetic AI", "note":"Synthetic boundary test only.", "confirmed":True}
        attribution = {"kind":"local-ai", "model_digest":self.client.digest, "requested_by":"Test admin"}
        for changes in ({}, {"sensitivity":"public"}, {"rights":"allowed"},
                        {"decision":"public", "rights":"allowed", "sensitivity":"public", "reference":"QA"}):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "AI_REVIEW_"):
                intake_review.save(self.root, {**request, **changes}, intake_route.load_budget(),
                                   ai_attribution=attribution, expected_context=intake_review.context(item))
        self.assertEqual(self.item()["review_history"], [])

    def test_interrupted_captured_batch_recovers_one_receipt_without_duplicate_review(self):
        self.capture()
        job = self.queue_without_worker()
        with self.manager.db() as db:
            task = db.execute("SELECT job,seq,item,sha,context,cache_key FROM ai_acceptance_tasks WHERE job=?", (job["id"],)).fetchone()
            db.execute("UPDATE ai_acceptance_tasks SET state='working' WHERE job=?", (job["id"],))
        self.manager.process(job, task)
        restarted = ai.Manager(self.root, self.client)
        self.manager = restarted
        self.assertEqual(restarted.status()["job"]["state"], "paused")
        restarted.control("resume"); restarted.thread.join(10)
        self.assertEqual(restarted.status()["job"]["counts"], {"accepted":1})
        self.assertEqual(self.client.calls, 1)
        self.assertEqual(len(self.item()["review_history"]), 1)

    def test_changed_capture_fingerprint_after_queue_is_stale_before_inference(self):
        _, binding = self.capture()
        before = intake_review.context(self.item())
        self.queue_without_worker()
        declared = json.loads(binding.read_bytes())
        declared["source_uri"] = "https://example.test/changed-synthetic-provenance"
        binding.write_bytes(manage.canonical(declared))
        intake.analyze(self.root)
        self.assertNotEqual(intake_review.context(self.item()), before)
        self.manager.control("resume"); self.manager.thread.join(10)
        self.assertEqual(self.manager.status()["job"]["counts"], {"stale":1})
        self.assertEqual(self.client.calls, 0)
        self.assertEqual(self.item()["review_history"], [])

    def test_changed_capture_fingerprint_during_inference_cannot_save(self):
        _, binding = self.capture()
        def change(packet):
            declared = json.loads(binding.read_bytes())
            declared["source_uri"] = "https://example.test/changed-during-review"
            binding.write_bytes(manage.canonical(declared))
            intake.analyze(self.root)
        self.client.before = change
        self.assertEqual(self.run_batch()["counts"], {"failed":1})
        self.assertEqual(self.item()["review_history"], [])

    def test_changed_payload_after_queue_is_refused_even_if_size_and_mtime_match(self):
        payload, _ = self.capture()
        self.queue_without_worker()
        before = payload.stat()
        content = bytearray(payload.read_bytes()); content[12] ^= 1
        payload.write_bytes(content)
        os.utime(payload, ns=(before.st_atime_ns, before.st_mtime_ns))
        self.manager.control("resume"); self.manager.thread.join(10)
        self.assertEqual(self.manager.status()["job"]["counts"], {"failed":1})
        self.assertEqual(self.client.calls, 0)
        self.assertEqual(self.item()["review_history"], [])

    def test_changed_packet_policy_prevents_resuming_old_paused_batch(self):
        self.capture()
        self.queue_without_worker()
        with patch.object(ai, "PROMPT_VERSION", "different-packet-policy"):
            with self.assertRaisesRegex(ValueError, "AI_PROMPT_CHANGED_START_NEW_BATCH"):
                self.manager.control("resume")
        self.assertEqual(self.client.calls, 0)

    def test_changed_model_pin_prevents_resuming_old_paused_batch(self):
        self.capture()
        self.queue_without_worker()
        self.client.digest = "b" * 64
        with self.assertRaisesRegex(ValueError, "AI_MODEL_PIN_CHANGED"):
            self.manager.control("resume")
        self.assertEqual(self.client.calls, 0)

    def test_qwen_transport_uses_literal_loopback_without_proxies(self):
        from unittest.mock import MagicMock
        with patch.object(ai.urllib.request, "build_opener") as build:
            client = ai.Qwen(self.client.model, self.client.digest)
        self.assertEqual(build.call_args.args[0].proxies, {})
        self.assertIsInstance(build.call_args.args[1], ai.NoRedirect)
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{}'
        client.opener.open.return_value = response
        client.call("/api/tags", timeout=5)
        request = client.opener.open.call_args.args[0]
        self.assertEqual(request.full_url, "http://127.0.0.1:11434/api/tags")


if __name__ == "__main__":
    unittest.main()
