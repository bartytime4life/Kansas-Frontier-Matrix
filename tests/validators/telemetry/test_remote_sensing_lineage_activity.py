"""Focused no-network tests for the remote-sensing lineage companion."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

BUILDER_PATH = (
    REPO_ROOT
    / "tools/generators/telemetry/build_remote_sensing_lineage_activity.py"
)
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/telemetry/validate_remote_sensing_lineage_activity.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/telemetry/remote_sensing_lineage_activity.schema.json"
)
CONTRACT_PATH = (
    REPO_ROOT / "contracts/telemetry/remote_sensing_lineage_activity.md"
)
WORKFLOW_PATH = (
    REPO_ROOT / ".github/workflows/remote-sensing-lineage-activity.yml"
)


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


BUILDER = _load_module("test_kfm_remote_sensing_builder", BUILDER_PATH)
VALIDATOR = _load_module("test_kfm_remote_sensing_validator", VALIDATOR_PATH)


class RemoteSensingLineageActivityTests(unittest.TestCase):
    def test_schema_is_draft_2020_12_valid_and_composes_openlineage(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(VALIDATOR._SCHEMA_VALIDATOR.iter_errors(BUILDER.build_document()))
        self.assertEqual(errors, [])
        self.assertEqual(
            schema["properties"]["source_openlineage_projection"]["$ref"],
            "https://schemas.kfm.local/contracts/v1/telemetry/"
            "openlineage_run_event_projection.schema.json",
        )

    def test_contract_preserves_inactive_no_network_boundary(self) -> None:
        contract = CONTRACT_PATH.read_text(encoding="utf-8").lower()
        self.assertIn(
            "status: draft; proposed; fixture-first; local-only; no-network; "
            "non-authoritative",
            contract,
        )
        self.assertIn("does not fetch imagery", contract)

    def test_fixture_suite_covers_exact_positive_and_negative_cases(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 11)

    def test_activity_is_deterministic_and_binds_source_projection(self) -> None:
        first = BUILDER.build_document()
        second = BUILDER.build_document()
        self.assertEqual(first, second)
        self.assertTrue(first["activity_id"].startswith("kfm:remote-sensing-activity:"))
        self.assertEqual(first["decision"]["outcome"], "PASS")
        self.assertEqual(
            first["remote_sensing_facet"]["activityId"], first["activity_id"]
        )
        self.assertEqual(first["prov_activity"]["id"], first["activity_id"])
        self.assertEqual(
            first["source_openlineage_projection"]["decision"]["outcome"],
            "PASS",
        )

    def test_success_and_failure_metrics_are_recorded_without_authority(self) -> None:
        success = BUILDER.build_document()
        failed = BUILDER.build_document(
            processed_scene_count=7,
            failed_scene_count=1,
            retry_count=2,
            run_outcome="FAIL",
        )
        self.assertIn(
            "REMOTE_SENSING_SUCCESS_RECORDED",
            success["decision"]["reason_codes"],
        )
        self.assertIn(
            "REMOTE_SENSING_FAILURE_RECORDED",
            failed["decision"]["reason_codes"],
        )
        self.assertEqual(
            failed["source_openlineage_projection"]["event"]["eventType"],
            "FAIL",
        )
        self.assertEqual(failed["authority"], "NONE")

    def test_partial_or_policy_denied_source_never_becomes_pass(self) -> None:
        partial = BUILDER.build_document(run_outcome="PARTIAL")
        denied = BUILDER.build_document(telemetry_allowed=False)
        self.assertEqual(partial["decision"]["outcome"], "ABSTAIN")
        self.assertEqual(denied["decision"]["outcome"], "DENY")

    def test_incoherent_counts_runtime_and_links_are_finite_denials(self) -> None:
        for mutation, reason in (
            ("COUNT_MISMATCH", "SCENE_COUNT_MISMATCH"),
            ("RUNTIME_MISMATCH", "RUNTIME_MISMATCH"),
            ("SOURCE_LINK_MISSING", "SOURCE_LINK_CLOSURE_MISMATCH"),
        ):
            with self.subTest(mutation=mutation):
                document = BUILDER.build_case({"mutation": mutation})
                self.assertEqual(document["decision"]["outcome"], "DENY")
                self.assertIn(reason, document["decision"]["reason_codes"])
                self.assertEqual(VALIDATOR.validate_document(document).outcome, "PASS")

    def test_invalid_embedded_openlineage_projection_fails_companion(self) -> None:
        document = BUILDER.build_document()
        document["source_openlineage_projection"]["spec_hash"] = "sha256:" + "f" * 64
        BUILDER._reidentify(document)
        result = VALIDATOR.validate_document(document)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "SOURCE_PROJECTION_INVALID",
            {finding.code for finding in result.findings},
        )

    def test_validator_does_not_mutate_candidate(self) -> None:
        document = BUILDER.build_document()
        before = copy.deepcopy(document)
        self.assertEqual(VALIDATOR.validate_document(document).outcome, "PASS")
        self.assertEqual(document, before)

    def test_closed_shape_rejects_coordinate_side_channel(self) -> None:
        result = VALIDATOR.validate_document(
            BUILDER.build_case({"mutation": "EXTRA_COORDINATES"})
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual({item.code for item in result.findings}, {"SCHEMA_INVALID"})

    def test_source_has_no_network_export_signing_or_repository_write_client(self) -> None:
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (BUILDER_PATH, VALIDATOR_PATH)
        )
        for forbidden in (
            "import requests",
            "from requests",
            "urllib.request",
            "subprocess",
            "socket",
            "openlineage.client",
            "sigstore",
            "cosign",
            "git commit",
        ):
            self.assertNotIn(forbidden, source)

    def test_workflow_is_read_only_and_immutable_pinned(self) -> None:
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("KFM_NO_NETWORK: \"1\"", workflow)
        self.assertNotIn("pull-requests: write", workflow)
        for line in workflow.splitlines():
            if "uses:" in line:
                self.assertRegex(line, r"uses: [^ ]+@[0-9a-f]{40}")


if __name__ == "__main__":
    unittest.main()
