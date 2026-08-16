from __future__ import annotations

import importlib.util
import io
import json
import socket
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/governance/assess_temporal_authority_envelope_conflict.py"
)
SPEC = importlib.util.spec_from_file_location(
    "kfm_assess_temporal_authority_envelope_conflict", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class TemporalAuthorityEnvelopeConflictAssessmentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self._build_complete_conflict()

    def _write(self, relative: str, text: str = "placeholder\n") -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def _build_complete_conflict(self) -> None:
        common_text = (
            "# TemporalAuthorityEnvelope\n"
            f"Schema: `{module.COMMON_SCHEMA}`\n"
            "public_use_allowed = false\n"
        )
        evidence_text = (
            "# TemporalAuthorityEnvelope\n"
            f"Schema: `{module.EVIDENCE_SCHEMA}`\n"
            "CURRENT | STALE | SUPERSEDED | WITHDRAWN | UNKNOWN\n"
        )
        file_contents = {
            module.COMMON_CONTRACT: common_text,
            module.COMMON_SCHEMA: json.dumps(
                {
                    "$id": module.COMMON_SCHEMA,
                    "title": "TemporalAuthorityEnvelope",
                    "type": "object",
                },
                sort_keys=True,
            )
            + "\n",
            module.COMMON_VALIDATOR: f'SCHEMA = "{module.COMMON_SCHEMA}"\n',
            module.COMMON_TEST: f'VALIDATOR = "{module.COMMON_VALIDATOR}"\n',
            module.COMMON_WORKFLOW: f"run: python {module.COMMON_VALIDATOR}\n",
            module.EVIDENCE_CONTRACT: evidence_text,
            module.EVIDENCE_SCHEMA: json.dumps(
                {
                    "$id": module.EVIDENCE_SCHEMA,
                    "title": "TemporalAuthorityEnvelope",
                    "type": "object",
                },
                sort_keys=True,
            )
            + "\n",
            module.EVIDENCE_VALIDATOR: f'SCHEMA = "{module.EVIDENCE_SCHEMA}"\n',
            module.EVIDENCE_TEST: f'VALIDATOR = "{module.EVIDENCE_VALIDATOR}"\n',
            module.EVIDENCE_WORKFLOW: f"run: python {module.EVIDENCE_VALIDATOR}\n",
            module.ADR_0014: (
                "status: proposed\n"
                "TemporalAuthorityEnvelope parallel authority conflict remains unresolved.\n"
            ),
            module.ADR_0029: "status: accepted\nAdopts Directory Rules.\n",
        }
        for relative, text in file_contents.items():
            self._write(relative, text)
        for directories in module.REQUIRED_FIXTURE_DIRS.values():
            for directory in directories:
                self._write(f"{directory}/case.json", '{"fixture": true}\n')

    def test_complete_scan_returns_explicit_hold_without_authority(self) -> None:
        self._write(
            "contracts/common/condition_relation.md",
            f"Uses `{module.COMMON_CONTRACT}` and TemporalAuthorityEnvelope.\n",
        )
        code, report = module.assess(self.root, revision="abc123")

        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual("HOLD_UNRESOLVED", report["outcome"])
        self.assertEqual("HOLD", report["disposition"])
        self.assertTrue(report["scan_complete"])
        self.assertEqual("abc123", report["revision"])
        self.assertFalse(any(report["authority"].values()))
        self.assertEqual([], report["findings"])
        self.assertEqual([], report["scan_gaps"])
        self.assertEqual(
            [module.COMMON_CONTRACT, module.EVIDENCE_CONTRACT],
            report["same_name_family_discovery"]["contracts"],
        )
        by_path = {item["path"]: item for item in report["reference_inventory"]}
        consumer = by_path["contracts/common/condition_relation.md"]
        self.assertEqual("semantic_consumer", consumer["classification"])
        self.assertEqual("exact_path", consumer["reference_mode"])
        self.assertEqual(["common"], consumer["families"])
        self.assertIn("KFM-TAE-MIGRATION-NOT-AUTHORIZED", report["reason_codes"])
        self.assertIn(
            "KFM-TAE-TRACKED-TEXT-INVENTORY-COMPLETE", report["reason_codes"]
        )
        self.assertTrue(report["inventory_scope"]["tracked_repository_text"])
        self.assertFalse(report["inventory_scope"]["runtime_observation"])

    def test_report_is_deterministic_and_value_minimized(self) -> None:
        secret = "ghp_this_value_must_not_be_echoed"
        self._write(
            "docs/note.md",
            f"{secret} TemporalAuthorityEnvelope {module.COMMON_CONTRACT}\n",
        )
        first_code, first = module.assess(self.root, revision="fixed")
        second_code, second = module.assess(self.root, revision="fixed")

        self.assertEqual(module.EXIT_HOLD, first_code)
        self.assertEqual(first_code, second_code)
        self.assertEqual(first, second)
        serialized = json.dumps(first, sort_keys=True)
        self.assertNotIn(secret, serialized)
        self.assertRegex(first["report_sha256"], r"^sha256:[0-9a-f]{64}$")
        self.assertEqual(first["report_sha256"], module._report_hash(first))

    def test_missing_family_file_fails_invariant(self) -> None:
        (self.root / module.EVIDENCE_SCHEMA).unlink()
        code, report = module.assess(self.root)

        self.assertEqual(module.EXIT_FAIL, code)
        self.assertEqual("FAIL_INVARIANT", report["outcome"])
        self.assertIn(
            "KFM-TAE-CONFLICT-SHAPE-DRIFT",
            report["reason_codes"],
        )
        self.assertTrue(
            any(
                finding["code"] == "KFM-TAE-FAMILY-001"
                and finding["path"] == module.EVIDENCE_SCHEMA
                for finding in report["findings"]
            )
        )

    def test_third_same_named_family_fails_invariant(self) -> None:
        self._write(
            "contracts/runtime/temporal_authority_envelope.md",
            "# TemporalAuthorityEnvelope\n",
        )
        self._write(
            "schemas/contracts/v1/runtime/temporal_authority_envelope.schema.json",
            '{"title": "TemporalAuthorityEnvelope"}\n',
        )
        self._write(
            "tools/validators/runtime/validate_temporal_authority_envelope.py",
            "# third validator\n",
        )
        code, report = module.assess(self.root)

        self.assertEqual(module.EXIT_FAIL, code)
        self.assertEqual("FAIL_INVARIANT", report["outcome"])
        self.assertTrue(
            any(finding["code"] == "KFM-TAE-FAMILY-005" for finding in report["findings"])
        )

    def test_runtime_and_persisted_references_are_reported_not_authorized(self) -> None:
        self._write(
            "apps/governed-api/consumer.py",
            f'COMMON_SCHEMA = "{module.COMMON_SCHEMA}"\n',
        )
        self._write(
            "data/processed/example.json",
            '{"object_type": "TemporalAuthorityEnvelope"}\n',
        )
        code, report = module.assess(self.root)

        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual(2, report["reference_counts"]["critical_consumer_count"])
        self.assertEqual(
            ["apps/governed-api/consumer.py", "data/processed/example.json"],
            report["critical_consumer_paths"],
        )
        self.assertIn("KFM-TAE-CRITICAL-CONSUMER-PRESENT", report["reason_codes"])
        self.assertFalse(report["authority"]["authorizes_migration"])

    def test_name_only_reference_is_ambiguous(self) -> None:
        self._write("docs/note.md", "TemporalAuthorityEnvelope remains under review.\n")
        code, report = module.assess(self.root)

        self.assertEqual(module.EXIT_HOLD, code)
        self.assertIn("docs/note.md", report["ambiguous_reference_paths"])
        entry = next(
            item for item in report["reference_inventory"] if item["path"] == "docs/note.md"
        )
        self.assertEqual("name_only", entry["reference_mode"])
        self.assertEqual(["ambiguous"], entry["families"])

    def test_oversized_text_candidate_is_error_not_false_complete_scan(self) -> None:
        with mock.patch.object(module, "MAX_TEXT_BYTES", 128):
            self._write(
                "docs/oversized.md",
                "TemporalAuthorityEnvelope\n" + ("x" * 128) + "\n",
            )
            code, report = module.assess(self.root)

        self.assertEqual(module.EXIT_ERROR, code)
        self.assertEqual("ERROR_VALIDATOR", report["outcome"])
        self.assertFalse(report["scan_complete"])
        self.assertTrue(
            any(gap["code"] == "KFM-TAE-SCAN-002" for gap in report["scan_gaps"])
        )

    def test_cli_emits_hold_json_and_exit_three(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            code = module.main(
                [
                    "--root",
                    str(self.root),
                    "--revision",
                    "deadbeef",
                    "--format",
                    "json",
                ]
            )
        report = json.loads(output.getvalue())

        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual("HOLD_UNRESOLVED", report["outcome"])
        self.assertEqual("deadbeef", report["revision"])

    def test_assessment_makes_no_network_call(self) -> None:
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual("HOLD_UNRESOLVED", report["outcome"])


if __name__ == "__main__":
    unittest.main()
