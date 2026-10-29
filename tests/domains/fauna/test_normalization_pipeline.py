"""CLI and batch rehearsal tests, including local-input and output boundaries."""
from __future__ import annotations

from contextlib import redirect_stdout
import copy
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "packages/domains/fauna/src"))
sys.path.insert(0, str(ROOT / "packages/hashing/src"))

from fauna import TaxonomyCatalog
from pipelines.domains.fauna.normalize import MAX_BATCH_RECORDS, main, normalize_batch

SCHEMA = json.loads((ROOT / "schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json").read_text())
TAXONOMY_SCHEMA = json.loads((ROOT / "schemas/contracts/v1/domains/fauna/taxonomy_snapshot.schema.json").read_text())
SNAPSHOT_PATH = ROOT / "fixtures/domains/fauna/normalization/taxonomy_snapshot.json"
SNAPSHOT = json.loads(SNAPSHOT_PATH.read_text())
SOURCE_PATH = ROOT / "fixtures/domains/fauna/occurrence_evidence/valid/valid_observed_open.json"
SOURCE = json.loads(SOURCE_PATH.read_text())
VALIDATED_AT = "2026-10-29T00:00:00Z"
BUNDLES_PATH = ROOT / "fixtures/domains/fauna/evidence_bindings/bundles.json"


class NormalizationPipelineTests(unittest.TestCase):
    def setUp(self):
        patcher = patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden"))
        patcher.start()
        self.addCleanup(patcher.stop)
        self.taxonomy = TaxonomyCatalog.from_candidate(SNAPSHOT, schema=TAXONOMY_SCHEMA)

    def run_batch(self, records):
        return normalize_batch(records, taxonomy=self.taxonomy, schema=SCHEMA, validated_at=VALIDATED_AT)

    def cli(self, source, taxonomy=SNAPSHOT_PATH, evidence_bundles=None):
        output = io.StringIO()
        evidence_args = [] if evidence_bundles is None else ["--evidence-bundles", str(evidence_bundles)]
        with redirect_stdout(output):
            code = main(["--input", str(source), "--taxonomy", str(taxonomy), "--validated-at", VALIDATED_AT, *evidence_args])
        return code, json.loads(output.getvalue()), output.getvalue()

    def test_rehearsal_cli_reports_held_without_writing_or_dumping_input(self):
        before = SOURCE_PATH.read_bytes(), SNAPSHOT_PATH.read_bytes()
        code, result, rendered = self.cli(SOURCE_PATH)
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "HELD")
        self.assertEqual(result["normalized"], 1)
        self.assertEqual(result["quarantined"], 1)
        self.assertFalse(result["public_ready"])
        for private in (SOURCE["source_record_id"], "Specimen fictivus", "latitude", "longitude", "source_uri"):
            self.assertNotIn(private, rendered)
        self.assertEqual(before, (SOURCE_PATH.read_bytes(), SNAPSHOT_PATH.read_bytes()))

    def test_batch_keeps_same_identity_from_different_source_families_separate(self):
        second = copy.deepcopy(SOURCE)
        second["source_family"] = "inat"
        result = self.run_batch([SOURCE, second])
        self.assertEqual(len(result.results), 2)
        self.assertEqual(result.summary()["normalized"], 2)
        self.assertEqual(result.results[0].occurrence["source_family"], "other")
        self.assertEqual(result.results[1].occurrence["source_family"], "inat")
        # Compatibility digest intentionally unchanged; no dedup/overwrite.
        self.assertEqual(result.results[0].occurrence["spec_hash"], result.results[1].occurrence["spec_hash"])

    def test_batch_has_finite_error_hold_and_denial_states(self):
        unknown = copy.deepcopy(SOURCE)
        unknown["taxon"]["scientific_name"] = "Specimen unknownus"
        denied = copy.deepcopy(SOURCE)
        denied["validation"]["validator_result"] = "deny"
        result = self.run_batch([SOURCE, unknown, None, denied])
        self.assertEqual(result.summary()["processed"], 4)
        self.assertEqual(result.summary()["normalized"], 1)
        self.assertEqual(result.summary()["quarantined"], 2)
        self.assertEqual(result.summary()["errors"], 1)
        self.assertEqual(result.summary()["denied"], 1)
        self.assertFalse(result.summary()["public_ready"])

    def test_empty_batch_is_not_reported_as_healthy_or_released(self):
        result = self.run_batch([]).summary()
        self.assertEqual(result["status"], "EMPTY")
        self.assertEqual(result["processed"], 0)
        self.assertFalse(result["public_ready"])

    def test_batch_rejects_non_arrays_and_unbounded_inventory(self):
        for records in ({}, None, "record", [None] * (MAX_BATCH_RECORDS + 1)):
            with self.assertRaisesRegex(ValueError, "schema.batch_invalid"):
                self.run_batch(records)

    def test_even_empty_batch_requires_explicit_rfc3339_validation_time(self):
        with self.assertRaisesRegex(ValueError, "schema.validation_time_invalid"):
            normalize_batch([], taxonomy=self.taxonomy, schema=SCHEMA, validated_at="unknown")

    def test_cli_rejects_duplicate_keys_nonfinite_and_non_json_without_data_leak(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "input.json"
            for raw in ('{"latitude":1,"latitude":2}', '{"latitude":NaN}', 'private-location-clue', '"' + 'x' * 1_000_001 + '"'):
                path.write_text(raw)
                code, result, rendered = self.cli(path)
                self.assertEqual(code, 2)
                self.assertEqual(result["code"], "fauna.input_invalid")
                self.assertNotIn("private-location-clue", rendered)
                self.assertNotIn(str(path), rendered)

    def test_cli_denies_symlink_and_missing_input(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "input.json"
            path.symlink_to(SOURCE_PATH)
            self.assertEqual(self.cli(path)[0], 2)
            self.assertEqual(self.cli(Path(temporary) / "missing.json")[0], 2)

    def test_cli_failure_does_not_dump_a_bad_taxonomy_snapshot(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "taxonomy.json"
            path.write_text('{"authority":"private-authority-clue"}')
            code, _, rendered = self.cli(SOURCE_PATH, taxonomy=path)
            self.assertEqual(code, 2)
            self.assertNotIn("private-authority-clue", rendered)

    def test_repository_cli_runs_outside_repo_without_installed_fauna(self):
        result = subprocess.run(
            [sys.executable, "-I", str(ROOT / "pipelines/domains/fauna/normalize.py"),
             "--input", str(SOURCE_PATH), "--taxonomy", str(SNAPSHOT_PATH),
             "--validated-at", VALIDATED_AT],
            cwd=ROOT.parent, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "HELD")

    def test_opt_in_bundle_rehearsal_reports_counts_and_preserves_input_bytes(self):
        before = BUNDLES_PATH.read_bytes(), SOURCE_PATH.read_bytes()
        code, result, rendered = self.cli(SOURCE_PATH, evidence_bundles=BUNDLES_PATH)
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "HELD")
        self.assertFalse(result["public_ready"])
        self.assertEqual(result["evidence_bindings"], {
            "checked": 1, "linked": 1, "abstained": 0, "errors": 0,
            "skipped": 0, "integrity_verified": False,
        })
        for private in ("fixture:bundle", "fixture:evidence", SOURCE["source_record_id"], "Specimen", "latitude", str(BUNDLES_PATH)):
            self.assertNotIn(private, rendered)
        self.assertEqual(before, (BUNDLES_PATH.read_bytes(), SOURCE_PATH.read_bytes()))

    def test_opt_in_empty_inventory_is_checked_and_abstains_without_becoming_an_error(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "bundles.json"
            path.write_text("[]")
            code, result, _ = self.cli(SOURCE_PATH, evidence_bundles=path)
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "HELD")
        self.assertEqual(result["evidence_bindings"]["abstained"], 1)
        self.assertEqual(result["evidence_bindings"]["linked"], 0)

    def test_no_bundle_inventory_preserves_the_existing_summary_shape(self):
        self.assertNotIn("evidence_bindings", self.cli(SOURCE_PATH)[1])

    def test_no_normalized_record_is_reported_as_evidence_checked(self):
        from pipelines.domains.fauna.normalize import load_evidence_catalog
        unknown = copy.deepcopy(SOURCE)
        unknown["taxon"]["scientific_name"] = "Specimen unknownus"
        result = normalize_batch(
            [SOURCE, unknown, None], taxonomy=self.taxonomy, schema=SCHEMA,
            validated_at=VALIDATED_AT, evidence_catalog=load_evidence_catalog(BUNDLES_PATH),
        ).summary()
        self.assertEqual(result["evidence_bindings"]["checked"], 1)
        self.assertEqual(result["evidence_bindings"]["skipped"], 2)
        self.assertEqual(result["status"], "ERROR")

    def test_bad_bundle_inventory_fails_closed_without_echoing_paths_or_values(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "private-inventory.json"
            for raw in ('{"private-place":1,"private-place":2}', '[{"bundle_id":"private-location-clue"}]', 'null'):
                path.write_text(raw)
                code, result, rendered = self.cli(SOURCE_PATH, evidence_bundles=path)
                self.assertEqual(code, 2)
                self.assertEqual(result["code"], "fauna.input_invalid")
                self.assertNotIn("private-location-clue", rendered)
                self.assertNotIn(str(path), rendered)
            path.unlink()
            path.symlink_to(BUNDLES_PATH)
            self.assertEqual(self.cli(SOURCE_PATH, evidence_bundles=path)[0], 2)

    def test_opt_in_cli_runs_in_isolated_python_outside_repository(self):
        result = subprocess.run(
            [sys.executable, "-I", str(ROOT / "pipelines/domains/fauna/normalize.py"),
             "--input", str(SOURCE_PATH), "--taxonomy", str(SNAPSHOT_PATH),
             "--validated-at", VALIDATED_AT, "--evidence-bundles", str(BUNDLES_PATH)],
            cwd=ROOT.parent, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["evidence_bindings"]["linked"], 1)


if __name__ == "__main__":
    unittest.main()
