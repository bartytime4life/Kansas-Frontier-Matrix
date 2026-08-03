from __future__ import annotations

import ast
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver.core import (  # noqa: E402
    BoundedJSONError,
    MAX_INPUT_BYTES,
    evaluate_resolution_candidate,
    loads_bounded,
    result_json,
)


FIXTURES = REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1"


class EvidenceResolutionCandidateTests(unittest.TestCase):
    def _cases(self) -> list[tuple[Path, dict[str, object]]]:
        cases = []
        for path in sorted(FIXTURES.rglob("*.json")):
            cases.append((path, json.loads(path.read_text(encoding="utf-8"))))
        self.assertTrue(cases)
        return cases

    def test_all_fixtures_have_exact_outcomes(self) -> None:
        for path, case in self._cases():
            with self.subTest(path=path.name):
                result = evaluate_resolution_candidate(case["request"])
                self.assertEqual(case["expected"]["status"], result.status)
                self.assertEqual(
                    sorted(case["expected"]["issue_codes"]),
                    [issue.code for issue in result.issues],
                )

    def test_result_is_deterministic_and_non_authoritative(self) -> None:
        case = json.loads(
            (FIXTURES / "valid/resolved.json").read_text(encoding="utf-8")
        )
        first = evaluate_resolution_candidate(case["request"])
        second = evaluate_resolution_candidate(case["request"])
        self.assertEqual(result_json(first), result_json(second))
        self.assertFalse(first.as_dict()["authoritative"])
        self.assertIn("claim_scope_not_machine_checked", first.as_dict()["limitations"])

    def test_policy_deny_precedes_unresolved(self) -> None:
        case = json.loads(
            (FIXTURES / "invalid/policy_denied.json").read_text(encoding="utf-8")
        )
        request = case["request"]
        request["bundle_candidate"] = None
        result = evaluate_resolution_candidate(request)
        self.assertEqual("DENIED", result.status)
        self.assertIn("lookup/not-found", {issue.code for issue in result.issues})
        self.assertIsNone(result.bundle_id)

        history_case = json.loads(
            (FIXTURES / "invalid/verification_revoked.json").read_text(
                encoding="utf-8"
            )
        )
        history_case["request"]["lookup_context"]["policy_outcome"] = "DENY"
        history_case["request"]["lookup_context"]["policy_decision_ref"] = (
            "policy:synthetic:deny-002"
        )
        history_result = evaluate_resolution_candidate(history_case["request"])
        self.assertEqual("DENIED", history_result.status)
        self.assertIn(
            "verification/revoked", {issue.code for issue in history_result.issues}
        )

    def test_non_resolved_objects_do_not_retain_bundle_identity(self) -> None:
        for filename in (
            "not_current_head.json",
            "policy_abstained.json",
            "verification_corrected.json",
            "verification_revoked.json",
        ):
            with self.subTest(filename=filename):
                case = json.loads(
                    (FIXTURES / "invalid" / filename).read_text(encoding="utf-8")
                )
                result = evaluate_resolution_candidate(case["request"])
                self.assertNotEqual("RESOLVED", result.status)
                self.assertIsNone(result.bundle_id)

    def test_negative_diagnostics_do_not_echo_input(self) -> None:
        case = json.loads(
            (FIXTURES / "invalid/ref_not_member.json").read_text(encoding="utf-8")
        )
        sentinel = "protected-location-sentinel-do-not-echo"
        case["request"]["evidence_ref"]["ref"] = sentinel
        serialized = result_json(evaluate_resolution_candidate(case["request"]))
        self.assertNotIn(sentinel, serialized)

    def test_bounded_parser_rejects_duplicate_nonfinite_and_oversized(self) -> None:
        invalid = (
            (b'{"a":1,"a":2}', "input/duplicate-key"),
            (b'{"a":NaN}', "input/non-finite-number"),
            (b'{"a":1e999}', "input/non-finite-number"),
            (b'{"a":' + b"9" * 129 + b"}", "input/number-too-large"),
            (b"x" * (MAX_INPUT_BYTES + 1), "input/too-large"),
            ('{"a":"\ud800"}', "input/not-utf8"),
        )
        for payload, expected in invalid:
            with self.subTest(expected=expected):
                with self.assertRaises(BoundedJSONError) as captured:
                    loads_bounded(payload)
                self.assertEqual(expected, captured.exception.code)

    def test_bounded_parser_rejects_excessive_depth(self) -> None:
        payload = "[" * 21 + "0" + "]" * 21
        with self.assertRaises(BoundedJSONError) as captured:
            loads_bounded(payload)
        self.assertEqual("input/max-depth", captured.exception.code)

    def test_direct_object_evaluation_enforces_structure_bounds(self) -> None:
        result = evaluate_resolution_candidate({"unsafe": float("inf")})
        self.assertEqual("ERROR", result.status)
        self.assertEqual("input/non-finite-number", result.issues[0].code)
        self.assertEqual(("input_structure_bounds",), result.checks_performed)
        huge = evaluate_resolution_candidate({"unsafe": 10**128})
        self.assertEqual("ERROR", huge.status)
        self.assertEqual("input/number-too-large", huge.issues[0].code)

    def test_evaluation_performs_no_network_access(self) -> None:
        case = json.loads(
            (FIXTURES / "valid/resolved.json").read_text(encoding="utf-8")
        )
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "getaddrinfo", side_effect=AssertionError("dns denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("socket denied")
        ):
            self.assertEqual(
                "RESOLVED",
                evaluate_resolution_candidate(case["request"]).status,
            )

    def test_core_imports_only_standard_library_and_local_history_modules(self) -> None:
        def import_roots(path: Path) -> set[str]:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            roots: set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    roots.update(alias.name.split(".", 1)[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    roots.add(node.module.split(".", 1)[0])
            return roots

        core_path = PACKAGE_SRC / "evidence_resolver/core.py"
        history_path = PACKAGE_SRC / "evidence_resolver/verification_history.py"
        roots = import_roots(core_path)
        self.assertLessEqual(
            roots,
            {
                "__future__",
                "dataclasses",
                "datetime",
                "json",
                "math",
                "re",
                "typing",
                "verification_history",
            },
        )
        self.assertLessEqual(
            import_roots(history_path),
            {
                "__future__",
                "dataclasses",
                "datetime",
                "hashlib",
                "json",
                "re",
                "typing",
            },
        )

    def test_verification_history_is_required_and_fails_closed(self) -> None:
        case = json.loads(
            (FIXTURES / "valid/resolved.json").read_text(encoding="utf-8")
        )
        del case["request"]["verification_history"]
        result = evaluate_resolution_candidate(case["request"])
        self.assertEqual("ERROR", result.status)
        self.assertEqual(["input/missing-field"], [issue.code for issue in result.issues])

    def test_profile_is_pinned_to_current_proposed_schema_surfaces(self) -> None:
        history_schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/evidence/verification_state_history.schema.json"
            ).read_text(encoding="utf-8")
        )
        ref_schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/evidence/evidence_ref.schema.json"
            ).read_text(encoding="utf-8")
        )
        bundle_schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/evidence/evidence_bundle.schema.json"
            ).read_text(encoding="utf-8")
        )
        policy_schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/policy/policy_decision.schema.json"
            ).read_text(encoding="utf-8")
        )
        sensitivity_schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/policy/sensitivity_label.schema.json"
            ).read_text(encoding="utf-8")
        )
        spec_hash_schema = json.loads(
            (
                REPO_ROOT
                / "schemas/contracts/v1/common/spec_hash.schema.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual("PROPOSED", ref_schema["x-kfm"]["status"])
        self.assertEqual("PROPOSED", bundle_schema["x-kfm"]["status"])
        self.assertEqual("PROPOSED", policy_schema["x-kfm"]["status"])
        self.assertEqual("PROPOSED", sensitivity_schema["x-kfm"]["status"])
        self.assertEqual("PROPOSED", history_schema["x-kfm"]["status"])
        self.assertFalse(ref_schema["additionalProperties"])
        self.assertFalse(bundle_schema["additionalProperties"])
        self.assertEqual(["ref", "kind"], ref_schema["required"])
        self.assertEqual(
            {"ref", "kind", "bundle_ref"}, set(ref_schema["properties"])
        )
        self.assertEqual(
            {"measurement", "record", "dataset", "artifact"},
            set(ref_schema["properties"]["kind"]["enum"]),
        )
        self.assertEqual(
            {
                "bundle_id",
                "claim_scope",
                "evidence_refs",
                "source_records",
                "citations",
                "rights",
                "sensitivity",
                "transforms",
                "checksums",
                "spec_hash",
            },
            set(bundle_schema["required"]),
        )
        self.assertEqual(
            set(bundle_schema["required"]), set(bundle_schema["properties"])
        )
        self.assertEqual(
            "^[a-z][a-z0-9_:.-]*$",
            bundle_schema["properties"]["bundle_id"]["pattern"],
        )
        self.assertEqual(
            1, bundle_schema["properties"]["evidence_refs"]["minItems"]
        )
        self.assertEqual(
            ref_schema["$id"],
            bundle_schema["properties"]["evidence_refs"]["items"]["$ref"],
        )
        self.assertEqual(
            1, bundle_schema["properties"]["source_records"]["minItems"]
        )
        self.assertEqual(
            1, bundle_schema["properties"]["citations"]["minItems"]
        )
        self.assertEqual(
            ["license"], bundle_schema["properties"]["rights"]["required"]
        )
        self.assertFalse(
            bundle_schema["properties"]["rights"]["additionalProperties"]
        )
        self.assertEqual(
            1, bundle_schema["properties"]["checksums"]["minProperties"]
        )
        self.assertEqual(
            "^sha256:[a-f0-9]{64}$",
            bundle_schema["properties"]["checksums"]["additionalProperties"][
                "pattern"
            ],
        )
        self.assertEqual(
            "https://schemas.kfm.local/contracts/v1/policy/sensitivity_label.schema.json",
            bundle_schema["properties"]["sensitivity"]["$ref"],
        )
        self.assertEqual(
            spec_hash_schema["$id"],
            bundle_schema["properties"]["spec_hash"]["$ref"],
        )
        self.assertEqual(["value"], spec_hash_schema["required"])
        self.assertFalse(spec_hash_schema["additionalProperties"])
        self.assertEqual(
            "^sha256:[a-f0-9]{64}$",
            spec_hash_schema["properties"]["value"]["pattern"],
        )
        self.assertEqual(
            {"level", "reason", "applied_at"},
            set(sensitivity_schema["required"]),
        )
        self.assertFalse(sensitivity_schema["additionalProperties"])
        self.assertEqual(
            {"public", "generalized", "restricted", "quarantine"},
            set(sensitivity_schema["properties"]["level"]["enum"]),
        )
        self.assertEqual(
            "date-time",
            sensitivity_schema["properties"]["applied_at"]["format"],
        )
        self.assertEqual(
            {"ANSWER", "ABSTAIN", "DENY", "ERROR"},
            set(policy_schema["properties"]["outcome"]["enum"]),
        )
        self.assertFalse(history_schema["additionalProperties"])
        self.assertEqual(
            {
                "schema_version",
                "history_id",
                "subject_ref",
                "profile_id",
                "spec_hash",
                "events",
            },
            set(history_schema["required"]),
        )
        self.assertEqual(128, history_schema["properties"]["events"]["maxItems"])


if __name__ == "__main__":
    unittest.main()
