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
MODULE_PATH = REPO_ROOT / "tools/validators/governance/assess_temporal_authority_envelope_conflict.py"
SPEC = importlib.util.spec_from_file_location("kfm_assess_tae_split", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class TemporalAuthorityEnvelopeSplitAssessmentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self._build_complete_split()

    def _write(self, relative: str, text: str = "placeholder\n") -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def _schema(self, schema_id: str, title: str) -> str:
        return json.dumps({
            "$schema":"https://json-schema.org/draft/2020-12/schema",
            "$id":schema_id,
            "title":title,
            "type":"object",
            "additionalProperties":False,
            "required":["value"],
            "properties":{"value":{"type":"string"}},
        }, sort_keys=True) + "\n"

    def _build_complete_split(self) -> None:
        common = self._schema(module.COMMON_SCHEMA_ID, "temporal_authority_envelope")
        legacy = self._schema(module.LEGACY_SCHEMA_ID, "TemporalAuthorityEnvelope")
        canonical_value = json.loads(legacy)
        canonical_value["$id"] = module.CANONICAL_SCHEMA_ID
        canonical_value["title"] = "EvidenceTemporalPostureAssessment"
        canonical_value["description"] = "distinct evidence assessment"
        canonical_value["x-kfm"] = {"legacy_compatibility_schema": module.LEGACY_SCHEMA}
        canonical = json.dumps(canonical_value, sort_keys=True) + "\n"
        files = {
            module.ADR_0014: "status: proposed\nparallel conflict remains independent\n",
            module.ADR_0029: "status: accepted\n",
            module.COMMON_CONTRACT: "# TemporalAuthorityEnvelope\n",
            module.COMMON_SCHEMA: common,
            module.CANONICAL_CONTRACT: "# EvidenceTemporalPostureAssessment\nCompatibility split.\n",
            module.CANONICAL_SCHEMA: canonical,
            module.CANONICAL_VALIDATOR: "# EvidenceTemporalPostureAssessment\n",
            module.CANONICAL_TEST: "# canonical test\n",
            module.CANONICAL_WORKFLOW: "name: evidence-temporal-posture-assessment\n",
            module.LEGACY_CONTRACT: "# Legacy TemporalAuthorityEnvelope compatibility alias\n",
            module.LEGACY_SCHEMA: legacy,
            module.LEGACY_VALIDATOR: "from validate_evidence_temporal_posture_assessment import validate_doc\nLEGACY_SCHEMA = 'legacy'\n",
            module.LEGACY_TEST: "# legacy test\n",
            module.LEGACY_WORKFLOW: "name: temporal-authority-envelope\n",
            module.ADVISORY_SCHEMA: json.dumps({"properties":{"temporal_authority":{"$ref":module.COMMON_SCHEMA_ID}}}) + "\n",
            module.PROGRAM_CONTRACT: f"Uses `{module.COMMON_CONTRACT}`.\n",
            module.PROGRAM_MODEL: f'REF = "{module.PROGRAM_LEGACY_REFERENCE}"\n',
        }
        for relative, text in files.items():
            self._write(relative, text)
        for base in (module.CANONICAL_FIXTURES, module.LEGACY_FIXTURES):
            self._write(f"{base}/valid/case.json", '{"value":"valid"}\n')
            self._write(f"{base}/invalid/case.json", '{"value":"invalid"}\n')

    def test_complete_split_returns_compatibility_hold(self) -> None:
        code, report = module.assess(self.root, revision="abc123")
        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual("HOLD_COMPATIBILITY", report["outcome"])
        self.assertEqual("SPLIT", report["disposition"])
        self.assertTrue(report["scan_complete"])
        self.assertEqual([], report["findings"])
        self.assertFalse(any(report["authority"].values()))
        self.assertEqual("EvidenceTemporalPostureAssessment", json.loads((self.root / module.CANONICAL_SCHEMA).read_text())["title"])
        self.assertEqual("legacy_compatibility", report["split_state"]["program_outcome_chain_reference"]["classification"])
        self.assertFalse(report["split_state"]["program_outcome_chain_reference"]["conformance_inferred"])
        self.assertIn("KFM-TAE-EXTERNAL-INVENTORY-REQUIRED-BEFORE-REMOVAL", report["reason_codes"])

    def test_schema_or_fixture_divergence_fails_closed(self) -> None:
        canonical = json.loads((self.root / module.CANONICAL_SCHEMA).read_text())
        canonical["properties"]["new_field"] = {"type":"string"}
        (self.root / module.CANONICAL_SCHEMA).write_text(json.dumps(canonical), encoding="utf-8")
        code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_FAIL, code)
        self.assertTrue(any(item["code"] == "KFM-TAE-COMPAT-002" for item in report["findings"]))

    def test_advisory_ref_cannot_move_to_evidence_assessment(self) -> None:
        self._write(module.ADVISORY_SCHEMA, json.dumps({"properties":{"temporal_authority":{"$ref":module.CANONICAL_SCHEMA_ID}}}) + "\n")
        code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_FAIL, code)
        self.assertTrue(any(item["code"] == "KFM-TAE-ADVISORY-001" for item in report["findings"]))

    def test_unclassified_runtime_reference_fails_closed(self) -> None:
        self._write("apps/example/consumer.py", 'REF = "kfm:temporal-authority:new-unqualified"\n')
        code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_FAIL, code)
        self.assertEqual(["apps/example/consumer.py"], report["runtime_unresolved_reference_paths"])

    def test_documentation_name_only_reference_is_held_not_authorized(self) -> None:
        self._write("docs/note.md", "TemporalAuthorityEnvelope remains under review.\n")
        code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_HOLD, code)
        self.assertIn("docs/note.md", report["unresolved_reference_paths"])
        self.assertIn("KFM-TAE-UNRESOLVED-REFERENCES-HELD", report["reason_codes"])

    def test_missing_canonical_surface_fails_invariant(self) -> None:
        (self.root / module.CANONICAL_SCHEMA).unlink()
        code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_FAIL, code)
        self.assertTrue(any(item["code"] == "KFM-TAE-FAMILY-001" for item in report["findings"]))

    def test_report_is_deterministic_and_value_minimized(self) -> None:
        secret = "ghp_do_not_echo"
        self._write("docs/secret.md", f"{secret} TemporalAuthorityEnvelope\n")
        first_code, first = module.assess(self.root, revision="fixed")
        second_code, second = module.assess(self.root, revision="fixed")
        self.assertEqual(first_code, second_code)
        self.assertEqual(first, second)
        self.assertNotIn(secret, json.dumps(first, sort_keys=True))
        self.assertEqual(first["report_sha256"], module._report_hash(first))

    def test_cli_emits_hold_json_and_exit_three(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            code = module.main(["--root", str(self.root), "--revision", "deadbeef", "--format", "json"])
        report = json.loads(output.getvalue())
        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual("HOLD_COMPATIBILITY", report["outcome"])
        self.assertEqual("deadbeef", report["revision"])

    def test_assessment_makes_no_network_call(self) -> None:
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            code, report = module.assess(self.root)
        self.assertEqual(module.EXIT_HOLD, code)
        self.assertEqual("HOLD_COMPATIBILITY", report["outcome"])


if __name__ == "__main__":
    unittest.main()
