from __future__ import annotations

import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators import validate_trace_temporal_closure as module

from tools.validators.validate_trace_temporal_closure import (
    FIXTURE_ROOT,
    canonical_closure_id,
    fixture_cases,
    validate_candidate,
    validate_closure,
)


VALID, INVALID = fixture_cases()


class TraceTemporalClosureTests(unittest.TestCase):
    def test_valid_fixture_passes(self) -> None:
        result = validate_candidate(VALID)
        self.assertTrue(result.ok, result.findings)

    def test_closure_id_is_recomputed_from_cross_contract_anchors(self) -> None:
        candidate = copy.deepcopy(VALID)
        self.assertEqual(candidate["closure_id"], canonical_closure_id(candidate))

    def test_invalid_fixtures_match_exact_findings(self) -> None:
        for name, candidate, expected in INVALID:
            with self.subTest(name=name):
                result = validate_candidate(candidate)
                self.assertEqual(sorted({item.code for item in result.findings}), sorted(expected))

    def test_changed_artifact_bytes_fail_even_when_fixture_json_is_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            candidate = copy.deepcopy(VALID)
            artifact_rel = candidate["temporal_slice"]["materialization"]["artifacts"][0]["artifact_path"]
            artifact = root / artifact_rel
            artifact.parent.mkdir(parents=True)
            artifact.write_text("changed bytes\n", encoding="utf-8")
            fixture = root / "closure.json"
            fixture.write_text(json.dumps(candidate), encoding="utf-8")
            result = validate_closure(fixture, repo_root=root)
            self.assertIn("ARTIFACT_DIGEST_MISMATCH", {item.code for item in result.findings})

    def test_noncanonical_artifact_path_fails_closed(self) -> None:
        candidate = copy.deepcopy(VALID)
        candidate["temporal_slice"]["materialization"]["artifacts"][0]["artifact_path"] = "../escape.json"
        candidate["closure_id"] = canonical_closure_id(candidate)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as stream:
            json.dump(candidate, stream)
            path = Path(stream.name)
        try:
            result = validate_closure(path)
            self.assertIn("ARTIFACT_PATH_INVALID", {item.code for item in result.findings})
        finally:
            path.unlink(missing_ok=True)

    def test_governance_flags_never_create_authority(self) -> None:
        candidate = copy.deepcopy(VALID)
        candidate = copy.deepcopy(candidate)
        candidate["temporal_slice"]["governance"]["release_authorized"] = True
        candidate["closure_id"] = canonical_closure_id(candidate)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as stream:
            json.dump(candidate, stream)
            path = Path(stream.name)
        try:
            result = validate_closure(path)
            self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", {item.code for item in result.findings})
        finally:
            path.unlink(missing_ok=True)


def rebound(change) -> dict:
    """The valid fixture with one change and a recomputed closure_id, so only that change can fail it."""
    candidate = copy.deepcopy(VALID)
    change(candidate)
    try:
        candidate["closure_id"] = canonical_closure_id(candidate)
    except ValueError:
        pass
    return candidate


def run_id_holders(candidate: dict) -> list[dict]:
    link = candidate["trace_receipt_link"]
    return [candidate["run_receipt"], candidate["evidence_bundle"], link["run_receipt"], link["evidence_bundle"], link["run_anchor"]]


def codes(candidate: dict) -> set[str]:
    return {item.code for item in validate_candidate(candidate).findings}


class IdentityAndByteClosureTests(unittest.TestCase):
    def test_absent_or_empty_identities_do_not_bind(self) -> None:
        # Missing everywhere, every equality check used to compare None with None and pass.
        def drop_run_ids(candidate: dict) -> None:
            for holder in run_id_holders(candidate):
                holder.pop("run_id", None)

        def blank_run_ids(candidate: dict) -> None:
            for holder in run_id_holders(candidate):
                holder["run_id"] = ""

        def drop_receipt_refs(candidate: dict) -> None:
            candidate["run_receipt"].pop("receipt_ref")
            candidate["trace_receipt_link"]["run_receipt"].pop("receipt_ref")
            candidate["temporal_slice"]["provenance"].pop("run_receipt_ref")

        def drop_bundle_refs(candidate: dict) -> None:
            candidate["evidence_bundle"].pop("bundle_ref")
            candidate["trace_receipt_link"]["evidence_bundle"].pop("bundle_ref")

        cases = {
            "run_id missing everywhere": (drop_run_ids, {"RUN_ID_MISMATCH"}),
            "run_id empty everywhere": (blank_run_ids, {"RUN_ID_MISMATCH"}),
            "receipt_ref missing everywhere": (drop_receipt_refs, {"RUN_RECEIPT_REF_MISMATCH"}),
            "bundle_ref missing": (drop_bundle_refs, {"EVIDENCE_REF_MISMATCH", "TEMPORAL_EVIDENCE_REF_MISMATCH"}),
        }
        for name, (change, expected) in cases.items():
            with self.subTest(name):
                self.assertEqual(codes(rebound(change)), expected)

    def test_unhashable_run_ids_are_findings_not_crashes(self) -> None:
        for value in (["run"], {"id": "run"}):
            with self.subTest(value=value):
                self.assertEqual(codes(rebound(lambda c, v=value: c["run_receipt"].update(run_id=v))), {"RUN_ID_MISMATCH"})

    def test_byte_closure_needs_a_materialized_artifact(self) -> None:
        empty = rebound(lambda c: c["temporal_slice"]["materialization"].update(artifacts=[]))
        self.assertEqual(codes(empty), {"ARTIFACT_SET_EMPTY"})
        missing = rebound(lambda c: c["temporal_slice"].pop("materialization"))
        self.assertEqual(codes(missing), {"ARTIFACT_SET_EMPTY"})

    def test_reference_rules_name_their_defect(self) -> None:
        cases = {
            "RUN_RECEIPT_REF_MISMATCH": lambda c: c["trace_receipt_link"]["run_receipt"].update(receipt_ref="receipt:other"),
            "EVIDENCE_REF_MISMATCH": lambda c: c["trace_receipt_link"]["evidence_bundle"].update(bundle_ref="bundle:other"),
            "TEMPORAL_RUN_RECEIPT_REF_MISMATCH": lambda c: c["temporal_slice"]["provenance"].update(run_receipt_ref="receipt:other"),
            "TEMPORAL_EVIDENCE_REFS_NOT_CANONICAL": lambda c: c["temporal_slice"]["provenance"]["evidence_bundle_refs"].append(
                c["evidence_bundle"]["bundle_ref"]),
            "ARTIFACT_REF_DUPLICATE_OR_INVALID": lambda c: c["temporal_slice"]["materialization"]["artifacts"].append(
                copy.deepcopy(c["temporal_slice"]["materialization"]["artifacts"][0])),
            "RECORD_TYPE_INVALID": lambda c: c.update(record_type="Other"),
            "FIXTURE_ONLY_REQUIRED": lambda c: c.update(fixture_only=False),
            "NETWORK_ACCESS_NOT_FORBIDDEN": lambda c: c.update(network_access="allowed"),
        }
        for expected, change in cases.items():
            with self.subTest(expected):
                self.assertIn(expected, codes(rebound(change)))

    def test_closure_id_must_be_well_formed_and_current(self) -> None:
        malformed = copy.deepcopy(VALID)
        malformed["closure_id"] = "urn:kfm:trace-temporal-closure:sha256:" + "A" * 64
        self.assertEqual(codes(malformed), {"CLOSURE_ID_FORMAT_INVALID"})
        stale = copy.deepcopy(VALID)
        stale["run_receipt"]["receipt_ref"] = stale["trace_receipt_link"]["run_receipt"]["receipt_ref"] = "receipt:moved"
        stale["temporal_slice"]["provenance"]["run_receipt_ref"] = "receipt:moved"
        self.assertEqual(codes(stale), set(), "receipt_ref is not a closure anchor")
        stale["temporal_slice"]["slice_id"] = "slice:moved"
        self.assertEqual(codes(stale), {"CLOSURE_ID_MISMATCH"})


class CommandLineTests(unittest.TestCase):
    def run_main(self, *argv: str) -> tuple[int, list[str]]:
        out = io.StringIO()
        with redirect_stdout(out):
            code = module.main(list(argv))
        return code, out.getvalue().splitlines()

    def test_fixture_replay_and_explicit_files(self) -> None:
        code, lines = self.run_main("--fixtures")
        self.assertEqual(code, 0)
        self.assertTrue(lines[-1].startswith("CONFIRMED: 1 valid and 6 invalid"))
        with tempfile.TemporaryDirectory() as temp:
            good = Path(temp) / "good.json"
            good.write_text(json.dumps(VALID), encoding="utf-8")
            bad = Path(temp) / "bad.json"
            bad.write_text(json.dumps(rebound(lambda c: c["temporal_slice"]["materialization"].update(artifacts=[]))), encoding="utf-8")
            self.assertEqual(self.run_main(str(good))[0], 0)
            code, lines = self.run_main(str(good), str(bad))
            self.assertEqual(code, 1)
            self.assertEqual([json.loads(line)["outcome"] for line in lines], ["FAIL", "PASS"])

    def test_unreadable_inputs_are_named_findings(self) -> None:
        cases = {
            "JSON_DUPLICATE_KEY": '{"a": 1, "a": 2}',
            "JSON_NONFINITE_NUMBER": '{"a": NaN}',
            "JSON_INVALID": '{"a": ',
            "ROOT_NOT_OBJECT": "[]",
        }
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "closure.json"
            for expected, content in cases.items():
                with self.subTest(expected):
                    path.write_text(content, encoding="utf-8")
                    self.assertIn(expected, {item.code for item in validate_closure(path).findings})
            bounded = {
                "JSON_COMPLEXITY_LIMIT": ('{"a": ' + "[" * 100_000 + "]" * 100_000 + "}", '{"a": ' + "9" * 5000 + "}"),
                "JSON_NONFINITE_NUMBER": ('{"a": 1e400}',),
            }
            for expected, contents in bounded.items():
                for content in contents:
                    with self.subTest(expected, content=content[:12]):
                        path.write_text(content, encoding="utf-8")
                        self.assertEqual({item.code for item in validate_closure(path).findings}, {expected})

    def test_fixture_replay_fails_on_wrong_polarity_or_bad_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest = Path(temp) / "cases.json"
            original = json.loads(module.CASES_PATH.read_text(encoding="utf-8"))
            wrong = copy.deepcopy(original)
            wrong["invalid"][0]["expected"] = ["NOT_THE_FINDING"]
            for content, expected_line in ((json.dumps(wrong), "FIXTURE_POLARITY_ERROR"), ("{", "ERROR: closure case manifest")):
                with self.subTest(expected_line):
                    manifest.write_text(content, encoding="utf-8")
                    with patch.object(module, "CASES_PATH", manifest):
                        code, lines = self.run_main("--fixtures")
                    self.assertEqual(code, 1)
                    self.assertTrue(any(expected_line in line for line in lines))


if __name__ == "__main__":
    unittest.main()
