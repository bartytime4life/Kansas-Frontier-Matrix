"""Focused no-network tests for the KFM OpenLineage terminal projection."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
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
    / "tools/generators/telemetry/"
    "build_openlineage_run_event_projection.py"
)
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/telemetry/"
    "validate_openlineage_run_event_projection.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/telemetry/"
    "openlineage_run_event_projection.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/telemetry/"
    "openlineage_run_event_projection/cases.json"
)
WORKFLOW_PATH = REPO_ROOT / ".github/workflows/openlineage-run-event-projection.yml"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


BUILDER = _load_module("test_kfm_openlineage_builder", BUILDER_PATH)
VALIDATOR = _load_module("test_kfm_openlineage_validator", VALIDATOR_PATH)


class OpenLineageRunEventProjectionTests(unittest.TestCase):
    def test_schema_is_draft_2020_12_valid_and_resolves_runtime_receipt(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(VALIDATOR._SCHEMA_VALIDATOR.iter_errors(BUILDER.build_document()))
        self.assertEqual(errors, [])
        self.assertEqual(
            schema["properties"]["source_run_receipt"]["$ref"],
            "../runtime/run_receipt.schema.json",
        )

    def test_fixture_suite_covers_exact_positive_and_negative_cases(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 18)
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_internal_projection_is_deterministic_and_pinned(self) -> None:
        first = BUILDER.build_document(sensitivity_level="internal")
        second = BUILDER.build_document(sensitivity_level="internal")
        self.assertEqual(first, second)
        self.assertEqual(
            first["projection_id"],
            "kfm:openlineage-projection:"
            "0aa8503568a8898e26a4c30f668e890ad3bf29359c3b026ec44c4de1197bc773",
        )
        self.assertEqual(
            first["spec_hash"],
            "sha256:0aa8503568a8898e26a4c30f668e890ad3bf29359c3b026ec44c4de1197bc773",
        )

    def test_event_time_is_normalized_to_utc_seconds(self) -> None:
        document = BUILDER.build_document(
            sensitivity_level="internal",
            event_time="2026-08-06T21:00:00-05:00",
        )
        self.assertEqual(document["request"]["event_time"], "2026-08-07T02:00:00Z")
        self.assertEqual(document["event"]["eventTime"], "2026-08-07T02:00:00Z")

    def test_success_and_failed_receipts_map_to_terminal_event_types(self) -> None:
        complete = BUILDER.build_document(sensitivity_level="internal")
        failed = BUILDER.build_document(
            run_outcome="FAIL",
            dataset_stage="WORK",
            evidence_release_state="WORK",
            sensitivity_level="internal",
        )
        self.assertEqual(complete["event"]["eventType"], "COMPLETE")
        self.assertEqual(failed["decision"]["outcome"], "PASS")
        self.assertEqual(failed["event"]["eventType"], "FAIL")
        self.assertIn("RUN_FAILURE_RECORDED", failed["decision"]["reason_codes"])

    def test_partial_receipt_abstains_without_event(self) -> None:
        partial = BUILDER.build_document(
            run_outcome="PARTIAL",
            dataset_stage="WORK",
            evidence_release_state="WORK",
            sensitivity_level="internal",
        )
        self.assertEqual(partial["decision"], {
            "outcome": "ABSTAIN",
            "reason_codes": ["RUN_RECEIPT_PARTIAL"],
        })
        self.assertIsNone(partial["event"])
        self.assertEqual(VALIDATOR.validate_document(partial).outcome, "PASS")

    def test_public_projection_requires_released_public_safe_support(self) -> None:
        valid = BUILDER.build_document(
            visibility="PUBLIC",
            dataset_stage="PUBLISHED",
            public_safe=True,
            evidence_release_state="PUBLISHED",
            sensitivity_level="generalized",
            public_use_allowed=True,
        )
        denied = BUILDER.build_document(
            visibility="PUBLIC",
            sensitivity_level="public",
        )
        self.assertEqual(valid["decision"]["outcome"], "PASS")
        self.assertIsNotNone(valid["event"])
        self.assertEqual(denied["decision"]["outcome"], "DENY")
        self.assertIsNone(denied["event"])
        self.assertIn("PUBLIC_DATASET_NOT_PUBLISHED", denied["decision"]["reason_codes"])

    def test_restricted_or_telemetry_denied_evidence_emits_no_event(self) -> None:
        restricted = BUILDER.build_document(sensitivity_level="restricted")
        denied = BUILDER.build_document(
            sensitivity_level="internal", telemetry_allowed=False
        )
        self.assertEqual(restricted["decision"]["outcome"], "DENY")
        self.assertEqual(denied["decision"]["outcome"], "DENY")
        self.assertIsNone(restricted["event"])
        self.assertIsNone(denied["event"])

    def test_event_binds_receipt_and_evidence_bundle_digests_without_payload(self) -> None:
        event = BUILDER.build_document(sensitivity_level="internal")["event"]
        run_facet = event["run"]["facets"]["kfm_run_receipt"]
        dataset_facet = event["outputs"][0]["facets"]["kfm_dataset_state"]
        projection_facet = event["job"]["facets"]["kfm_projection"]
        profile_schema = (
            "https://schemas.kfm.local/contracts/v1/telemetry/"
            "openlineage_run_event_projection.schema.json"
        )
        self.assertEqual(
            run_facet["_schemaURL"], profile_schema + "#/$defs/runReceiptFacet"
        )
        self.assertEqual(
            dataset_facet["_schemaURL"], profile_schema + "#/$defs/datasetFacet"
        )
        self.assertEqual(
            projection_facet["_schemaURL"], profile_schema + "#/$defs/projectionFacet"
        )
        self.assertTrue(run_facet["sourceRunSpecHash"].startswith("sha256:"))
        self.assertTrue(
            dataset_facet["evidenceBundles"][0]["bundleSpecHash"].startswith(
                "sha256:"
            )
        )
        serialized = json.dumps(event, sort_keys=True)
        for forbidden in (
            '"geometry"',
            '"coordinates"',
            '"payload"',
            '"sourcePayload"',
            '"raw"',
        ):
            self.assertNotIn(forbidden, serialized)

    def test_closed_schema_rejects_geometry_side_channel(self) -> None:
        case = {"mutation": "EXTRA_GEOMETRY"}
        result = VALIDATOR.validate_document(BUILDER.build_case(case))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual({item.code for item in result.findings}, {"SCHEMA_INVALID"})

    def test_projection_identity_and_run_uuid_change_with_receipt_identity(self) -> None:
        first = BUILDER.build_document(sensitivity_level="internal")
        changed = copy.deepcopy(first)
        changed["source_run_receipt"]["spec_hash"] = "sha256:" + "9" * 64
        BUILDER.finalize(changed)
        self.assertNotEqual(first["projection_id"], changed["projection_id"])
        self.assertNotEqual(
            first["event"]["run"]["runId"], changed["event"]["run"]["runId"]
        )

    def test_validator_does_not_mutate_candidate(self) -> None:
        document = BUILDER.build_document(sensitivity_level="internal")
        before = copy.deepcopy(document)
        result = VALIDATOR.validate_document(document)
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(document, before)

    def test_source_contains_no_network_or_repository_write_clients(self) -> None:
        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (BUILDER_PATH, VALIDATOR_PATH)
        )
        for forbidden in (
            "import requests",
            "from requests",
            "urllib.request",
            "import socket",
            "subprocess",
            "httpx",
            "aiohttp",
            "git push",
            "create_pull_request",
        ):
            self.assertNotIn(forbidden, combined)

    def test_cli_output_and_candidate_validation_are_deterministic(self) -> None:
        command = [
            sys.executable,
            str(BUILDER_PATH),
            "--case",
            "valid-internal-success-complete",
            "--manifest",
            str(FIXTURE_PATH),
        ]
        first = subprocess.run(command, check=True, capture_output=True, text=True)
        second = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertEqual(first.stdout, second.stdout)

        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "candidate.json"
            candidate.write_text(first.stdout, encoding="utf-8")
            validation = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR_PATH),
                    "--candidate",
                    str(candidate),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        report = json.loads(validation.stdout)
        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(report["declared_decision"], "PASS")
        self.assertEqual(report["event_type"], "COMPLETE")

    def test_workflow_is_read_only_pinned_and_no_network_at_runtime(self) -> None:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow_text)
        self.assertIn('KFM_NO_NETWORK: "1"', workflow_text)
        self.assertIn(
            "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            workflow_text,
        )
        self.assertIn(
            "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97",
            workflow_text,
        )
        for forbidden in (
            "pull-requests: write",
            "contents: write",
            "id-token: write",
            "curl ",
            "wget ",
            "OPENLINEAGE_ENDPOINT",
        ):
            self.assertNotIn(forbidden, workflow_text)


if __name__ == "__main__":
    unittest.main()
