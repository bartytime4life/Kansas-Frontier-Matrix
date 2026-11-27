"""Offline checks for source-receipt indexing and private Qwen draft boundaries."""
from contextlib import closing, redirect_stdout
from dataclasses import replace
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from tools.local_data import ai_acceptance, manage, sql_feed_metadata as metadata, sql_feeds as core


class FakeQwen:
    model = "qwen3.5:test"
    digest = "a" * 64

    def __init__(self):
        self.calls = []
        self.unavailable = False
        self.extra = {}
        self.before_response = lambda: None

    def identity(self):
        if self.unavailable:
            raise ai_acceptance.ProviderError("LOCAL_QWEN_UNAVAILABLE_OR_INVALID")

    def call(self, path, payload):
        self.calls.append((path, payload))
        self.before_response()
        result = {"title": "County drought source", "description": "This receipt describes a completed import for the drought feed. The contents were not inspected by the model.",
                  "domain": "hydrology", "evidence": ["feed", "imported_rows"], **self.extra}
        return {"model": self.model, "done": True, "message": {"content": json.dumps(result)}}


class MetadataTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name) / "store"
        manage.init_store(self.root)
        self.db_path = self.root / "data/work/observations.sqlite"
        self.notes = []
        self.ctx = core.Context(root=self.root, db_path=self.db_path,
                                lock=self.root / "pipeline.lock", floor=0, log=self.notes.append,
                                now=lambda: datetime(2026, 11, 27, 15, tzinfo=timezone.utc))
        core.init_bulk(self.ctx)
        self.client = FakeQwen()

    def add_source(self, name, *, state="complete", date=None):
        url = "https://provider.example/county?token=not-for-a-model"
        receipt_extra = {"window": ["2026-11-10", "2026-11-20"], "license": "Provider-declared term"}
        capture_ctx = replace(self.ctx, now=lambda: datetime.fromisoformat(date)) if date else self.ctx
        path, digest = core.store_raw(capture_ctx, "drought", name, b"source values " + name.encode(),
                                      url=url, extra=receipt_extra)
        with closing(core.open_db(self.ctx)) as db:
            record = core.begin_source(db, self.ctx, "usdm-county-stats", path, digest, url,
                                       core.receipt_for(self.ctx, path))
            core.finish_source(db, record, 3)
            db.execute("UPDATE kfm_sql_sources SET state=? WHERE file_id=?", (state, record))
        return path, digest

    def rows(self, statement, args=()):
        with closing(sqlite3.connect(self.db_path)) as db, db:
            return db.execute(statement, args).fetchall()

    def test_index_exact_receipt_then_generate_private_draft_idempotently(self):
        _, digest = self.add_source("new.csv")
        self.add_source("partial.csv", state="loading")
        self.add_source("old.csv", state="superseded")
        before = self.rows("SELECT * FROM kfm_sql_sources")
        result = metadata.review_metadata(self.ctx, limit=10)
        self.assertEqual(result["verified"], 1)
        self.assertEqual(result["drafted"], 0)
        state, evidence = self.rows("SELECT state, evidence_json FROM kfm_sql_source_metadata")[0]
        evidence = json.loads(evidence)
        self.assertEqual(state, "verified")
        self.assertEqual(evidence["source_sha256"], digest)
        self.assertEqual(evidence["provider_host"], "provider.example")
        self.assertEqual(evidence["retrieved_at"], "2026-11-27T15:00:00Z")
        self.assertEqual(evidence["provider_declared"]["query_window"], ["2026-11-10", "2026-11-20"])
        self.assertEqual(evidence["provider_declared"]["license"], "Provider-declared term")
        self.assertEqual(evidence["imported_rows"], 3)

        result = metadata.review_metadata(self.ctx, limit=10, client=self.client)
        self.assertEqual(result["verified"], 0)
        self.assertEqual(result["drafted"], 1)
        endpoint, payload = self.client.calls[0]
        self.assertEqual(endpoint, "/api/chat")
        message = payload["messages"][1]["content"]
        for forbidden in ("not-for-a-model", "source values", str(self.root), "Provider-declared term"):
            self.assertNotIn(forbidden, message)
        model, model_digest, draft, response_digest = self.rows(
            "SELECT model, model_digest, draft_json, response_sha256 FROM kfm_sql_source_metadata_drafts")[0]
        self.assertEqual(model, self.client.model)
        self.assertEqual(model_digest, self.client.digest)
        self.assertEqual(json.loads(draft)["evidence"], [{"id": "feed", "value": "drought"}, {"id": "imported_rows", "value": 3}])
        self.assertRegex(response_digest, r"^[a-f0-9]{64}$")
        self.assertEqual(metadata.review_metadata(self.ctx, limit=10, client=self.client)["drafted"], 0)
        self.assertEqual(len(self.client.calls), 1)
        self.assertEqual(self.rows("SELECT * FROM kfm_sql_sources"), before)

    def test_failed_model_resumes_without_reindexing_or_writing_a_false_draft(self):
        self.add_source("outage.csv")
        self.client.unavailable = True
        result = metadata.review_metadata(self.ctx, limit=1, client=self.client)
        self.assertEqual(result["model_pause"], "LOCAL_QWEN_UNAVAILABLE_OR_INVALID")
        self.assertEqual(result["verified"], 1)
        self.assertEqual(self.rows("SELECT * FROM kfm_sql_source_metadata_drafts"), [])
        self.client.unavailable = False
        result = metadata.review_metadata(self.ctx, limit=1, client=self.client)
        self.assertEqual(result["verified"], 0)
        self.assertEqual(result["drafted"], 1)

    def test_source_holds_need_an_exact_recheck(self):
        path, digest = self.add_source("damaged.csv")
        original = path.read_bytes()
        path.write_bytes(b"x" * len(original))
        result = metadata.review_metadata(self.ctx, limit=1, client=self.client)
        self.assertEqual(result["evidence_held"], 1)
        self.assertEqual(self.rows("SELECT state, hold_reason FROM kfm_sql_source_metadata"),
                         [("held", "SQL_METADATA_RAW_DIGEST_MISMATCH")])
        self.assertEqual(self.client.calls, [])
        path.write_bytes(original)
        self.assertEqual(metadata.review_metadata(self.ctx, limit=1)["verified"], 0)
        result = metadata.review_metadata(self.ctx, limit=1, source_sha=digest, retry_held=True, client=self.client)
        self.assertEqual((result["verified"], result["drafted"]), (1, 1))

    def test_model_cannot_assign_sql_or_disposition(self):
        _, digest = self.add_source("grounded.csv")
        self.client.extra = {"sql": "DROP TABLE kfm_sql_sources", "authority": "approve"}
        result = metadata.review_metadata(self.ctx, limit=2, client=self.client)
        self.assertEqual(result["draft_held"], 1)
        self.assertEqual(self.rows("SELECT state, draft_json, hold_reason FROM kfm_sql_source_metadata_drafts"),
                         [("held", None, "SQL_METADATA_DRAFT_INVALID_OR_UNGROUNDED")])
        self.assertEqual(self.rows("SELECT COUNT(*) FROM kfm_sql_sources"), [(1,)])
        self.client.extra = {"evidence": ["made_up"]}
        self.assertEqual(metadata.review_metadata(self.ctx, limit=2, source_sha=digest, retry_held=True,
                                                 client=self.client)["draft_held"], 1)
        self.client.extra = {}
        self.assertEqual(metadata.review_metadata(self.ctx, limit=2, source_sha=digest, retry_held=True,
                                                 client=self.client)["drafted"], 1)

    def test_source_superseded_during_inference_does_not_write_a_stale_draft(self):
        _, digest = self.add_source("revision.csv")
        self.client.before_response = lambda: self.rows("UPDATE kfm_sql_sources SET state='superseded' WHERE sha256=?", (digest,))
        counts = metadata.review_metadata(self.ctx, limit=1, client=self.client)
        self.assertEqual(counts["source_changed"], 1)
        self.assertEqual(self.rows("SELECT * FROM kfm_sql_source_metadata_drafts"), [])

    def test_receipt_mismatch_is_held_and_missing_database_is_not_created(self):
        path, _ = self.add_source("receipt.csv")
        relative = path.relative_to(self.root / metadata.RAW_PREFIX)
        receipt = self.root / metadata.RECEIPT_PREFIX / (str(relative) + ".json")
        changed = json.loads(receipt.read_text())
        changed["license"] = "Changed provider attribution"
        receipt.write_text(json.dumps(changed))
        self.assertEqual(metadata.review_metadata(self.ctx, limit=1)["evidence_held"], 1)
        self.assertEqual(self.rows("SELECT hold_reason FROM kfm_sql_source_metadata"),
                         [("SQL_METADATA_RETAINED_RECEIPT_MISMATCH",)])
        self.ctx.db_path = self.root / "data/work/missing.sqlite"
        with self.assertRaises(FileNotFoundError):
            metadata.review_metadata(self.ctx, limit=1)
        self.assertFalse(self.ctx.db_path.exists())

    def test_cli_since_ignores_legacy_completed_records_and_resumes_the_next_batch(self):
        self.add_source("old.csv", date="2026-11-16T00:00:00Z")
        self.add_source("one.csv")
        self.add_source("two.csv")
        self.rows("INSERT INTO kfm_sql_sources VALUES (42,'legacy','missing','legacy-digest',1,'','broken',0,'complete')")
        args = ["--root", str(self.root), "--db", str(self.db_path), "review-metadata", "--limit", "1",
                "--since", "2026-11-26T00:00:00Z"]
        for expected in (1, 1, 0):
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(core.main(args), 0)
            result = json.loads(output.getvalue())
            self.assertEqual(result["verified"], expected)
        self.assertEqual(self.rows("SELECT COUNT(*) FROM kfm_sql_source_metadata"), [(2,)])

    def test_bulk_selection_routes_metadata_to_the_named_database_only(self):
        self.add_source("observations.csv")
        observations_path = self.db_path
        self.db_path = self.ctx.db_path = self.root / "data/work/bulk.sqlite"
        core.init_bulk(self.ctx)
        self.add_source("bulk.csv")
        args = ["--root", str(self.root), "--db", str(observations_path), "--bulk-db", str(self.db_path),
                "review-metadata", "--database", "bulk"]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(core.main(args), 0)
        self.assertEqual(self.rows("SELECT COUNT(*) FROM kfm_sql_source_metadata"), [(1,)])
        self.db_path = observations_path
        self.assertEqual(self.rows("SELECT name FROM sqlite_master WHERE name='kfm_sql_source_metadata'"), [])
