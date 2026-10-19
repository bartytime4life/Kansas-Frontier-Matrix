from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
CANONICAL_PATH = ROOT / "tools/validators/evidence/validate_evidence_temporal_posture_assessment.py"
LEGACY_PATH = ROOT / "tools/validators/evidence/validate_temporal_authority_envelope.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CANONICAL = load_module("canonical_evidence_temporal_posture", CANONICAL_PATH)
LEGACY = load_module("legacy_evidence_temporal_posture", LEGACY_PATH)
NOW = datetime(2026, 8, 17, tzinfo=timezone.utc)
CANONICAL_ROOT = ROOT / "fixtures/contracts/v1/evidence/evidence_temporal_posture_assessment"
LEGACY_ROOT = ROOT / "fixtures/contracts/v1/evidence/temporal_authority_envelope"


def load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


class EvidenceTemporalPostureAssessmentTests(unittest.TestCase):
    def test_schema_is_distinct_and_meta_valid(self) -> None:
        schema = load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json")
        Draft202012Validator.check_schema(schema)
        self.assertEqual("EvidenceTemporalPostureAssessment", schema["title"])
        self.assertNotEqual(
            "https://schemas.kfm.local/contracts/v1/common/temporal_authority_envelope.schema.json",
            schema["$id"],
        )

    def test_canonical_fixture_polarity(self) -> None:
        valid = CANONICAL.validate_doc(load(CANONICAL_ROOT / "valid/current_observation.json"), now=NOW)
        self.assertEqual([], valid)
        inverted = CANONICAL.validate_doc(load(CANONICAL_ROOT / "invalid/inverted_validity.json"), now=NOW)
        self.assertTrue(any("valid_from" in error for error in inverted))
        source_after = CANONICAL.validate_doc(load(CANONICAL_ROOT / "invalid/source_after_retrieval.json"), now=NOW)
        self.assertTrue(any("source_updated_at" in error for error in source_after))

    def test_legacy_and_canonical_fixture_bytes_are_identical(self) -> None:
        canonical = sorted(path.relative_to(CANONICAL_ROOT) for path in CANONICAL_ROOT.rglob("*.json"))
        legacy = sorted(path.relative_to(LEGACY_ROOT) for path in LEGACY_ROOT.rglob("*.json"))
        self.assertEqual(legacy, canonical)
        for relative in canonical:
            self.assertEqual((LEGACY_ROOT / relative).read_bytes(), (CANONICAL_ROOT / relative).read_bytes())

    def test_legacy_and_canonical_diagnostics_are_identical(self) -> None:
        for relative in sorted(path.relative_to(CANONICAL_ROOT) for path in CANONICAL_ROOT.rglob("*.json")):
            canonical = CANONICAL.validate_doc(load(CANONICAL_ROOT / relative), now=NOW)
            legacy = LEGACY.validate_doc(load(LEGACY_ROOT / relative), now=NOW)
            self.assertEqual(legacy, canonical, relative)

    def test_legacy_identifiers_remain_resolvable(self) -> None:
        candidate = load(CANONICAL_ROOT / "valid/current_observation.json")
        self.assertTrue(str(candidate["envelope_id"]).startswith("kfm:temporal-authority:"))
        self.assertEqual([], CANONICAL.validate_doc(candidate, now=NOW))
        self.assertEqual([], LEGACY.validate_doc(candidate, now=NOW))

    def test_common_and_evidence_shapes_reject_each_other(self) -> None:
        common_schema = load(ROOT / "schemas/contracts/v1/common/temporal_authority_envelope.schema.json")
        assessment_schema = load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json")
        evidence_fixture = load(CANONICAL_ROOT / "valid/current_observation.json")
        common_fixture = load(ROOT / "fixtures/contracts/v1/common/temporal_authority_envelope/valid/valid_3_corrected_revision.json")
        common_errors = list(Draft202012Validator(common_schema, format_checker=FormatChecker()).iter_errors(evidence_fixture))
        evidence_errors = list(Draft202012Validator(assessment_schema, format_checker=FormatChecker()).iter_errors(common_fixture))
        self.assertTrue(common_errors)
        self.assertTrue(evidence_errors)

    def test_incompatible_correction_chronology_remains_explicit(self) -> None:
        candidate = load(CANONICAL_ROOT / "valid/current_observation.json")
        candidate["temporal_posture"] = "UNKNOWN"
        candidate["freshness_deadline"] = None
        times = candidate["times"]
        assert isinstance(times, dict)
        times["released_at"] = "2026-08-08T00:07:00Z"
        times["corrected_at"] = "2026-08-08T00:08:00Z"
        self.assertEqual([], CANONICAL.validate_doc(candidate, now=NOW))
        times["corrected_at"] = "2026-08-08T00:06:30Z"
        self.assertIn(
            "corrected_at requires and must not precede released_at",
            CANONICAL.validate_doc(candidate, now=NOW),
        )
        common_fixture = load(ROOT / "fixtures/contracts/v1/common/temporal_authority_envelope/valid/valid_3_corrected_revision.json")
        common_times = common_fixture["time"]
        assert isinstance(common_times, dict)
        self.assertLessEqual(common_times["corrected_at"], common_times["retrieved_at"])

    def test_source_role_is_not_source_descriptor_binding(self) -> None:
        assessment_schema = load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json")
        common_schema = load(ROOT / "schemas/contracts/v1/common/temporal_authority_envelope.schema.json")
        self.assertIn("source_role", assessment_schema["properties"])
        self.assertNotIn("source_descriptor_ref", assessment_schema["properties"])
        self.assertIn("source", common_schema["properties"])

    def test_advisory_reference_remains_bound_to_common_schema(self) -> None:
        advisory = load(ROOT / "schemas/contracts/v1/common/advisory_event_envelope.schema.json")
        self.assertEqual(
            "https://schemas.kfm.local/contracts/v1/common/temporal_authority_envelope.schema.json",
            advisory["properties"]["temporal_authority"]["$ref"],
        )

    def test_unreadable_inputs_are_finite_errors(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            truncated = Path(tmp) / "truncated.json"
            truncated.write_text('{"time": ', encoding="utf-8")
            missing = Path(tmp) / "missing.json"
            for module in (CANONICAL, LEGACY):
                for path in (truncated, missing):
                    with self.subTest(module=module.__name__, path=path.name):
                        self.assertEqual(["input is not readable JSON"], module.validate_file(path))

    def test_no_third_same_named_semantic_family(self) -> None:
        schemas = [
            load(ROOT / "schemas/contracts/v1/common/temporal_authority_envelope.schema.json"),
            load(ROOT / "schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"),
            load(ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json"),
        ]
        self.assertEqual(2, sum(schema.get("title") in {"TemporalAuthorityEnvelope", "temporal_authority_envelope"} for schema in schemas))
        self.assertEqual("EvidenceTemporalPostureAssessment", schemas[2]["title"])


class TemporalRuleTests(unittest.TestCase):
    """Each chronology and posture rule, run through both entry points from the valid fixture."""

    def candidate(self, **times: object) -> dict[str, object]:
        candidate = load(CANONICAL_ROOT / "valid/current_observation.json")
        candidate_times = candidate["times"]
        assert isinstance(candidate_times, dict)
        candidate_times.update(times)
        return candidate

    def errors(self, candidate: dict[str, object], now: datetime | None = NOW) -> list[str]:
        canonical = CANONICAL.validate_doc(candidate, now=now)
        self.assertEqual(LEGACY.validate_doc(candidate, now=now), canonical)
        return canonical

    def test_each_rule_names_its_defect(self) -> None:
        cases = {
            "source_updated_at must not exceed retrieved_at": self.candidate(source_updated_at="2026-08-08T00:07:00Z"),
            "released_at must not precede retrieved_at": self.candidate(released_at="2026-08-08T00:05:00Z"),
            "corrected_at requires and must not precede released_at": self.candidate(corrected_at="2026-08-08T00:09:00Z"),
            "SUPERSEDED requires supersedes_ref": {**self.candidate(), "temporal_posture": "SUPERSEDED"},
            "WITHDRAWN requires withdrawal_ref": {**self.candidate(), "temporal_posture": "WITHDRAWN"},
            "CURRENT envelope freshness_deadline is elapsed": {**self.candidate(), "freshness_deadline": "2026-08-16T23:59:59Z"},
        }
        for expected, candidate in cases.items():
            with self.subTest(expected):
                self.assertEqual([expected], self.errors(candidate))
        self.assertEqual([], self.errors({**self.candidate(), "temporal_posture": "SUPERSEDED", "supersedes_ref": "envelope:prior"}))
        self.assertEqual([], self.errors({**self.candidate(), "temporal_posture": "WITHDRAWN", "withdrawal_ref": "withdrawal:1"}))
        # Only a CURRENT posture is held to its deadline.
        self.assertEqual([], self.errors({**self.candidate(), "temporal_posture": "STALE", "freshness_deadline": "2026-08-16T00:00:00Z"}))

    def test_lowercase_rfc3339_separators_are_compared_not_crashed(self) -> None:
        lowered = {key: value.lower() for key, value in self.candidate()["times"].items() if isinstance(value, str)}
        self.assertEqual([], self.errors(self.candidate(**lowered)))
        self.assertEqual(["valid_from must not exceed valid_to"],
                         self.errors(self.candidate(**{**lowered, "valid_from": "2026-08-08t02:00:00z"})))
        self.assertEqual(["CURRENT envelope freshness_deadline is elapsed"],
                         self.errors({**self.candidate(**lowered), "freshness_deadline": "2026-08-16t00:00:00z"}))

    def test_offsets_are_compared_as_instants(self) -> None:
        # 00:30-01:00 is 01:30Z, after the 01:00Z valid_to; a textual comparison would accept it.
        self.assertEqual(["valid_from must not exceed valid_to"], self.errors(self.candidate(valid_from="2026-08-08T00:30:00-01:00")))
        self.assertEqual([], self.errors(self.candidate(valid_from="2026-08-08T01:30:00+01:00")))

    def test_unparseable_or_naive_times_are_findings_when_format_is_not_enforced(self) -> None:
        # Without rfc3339-validator, jsonschema skips the date-time format, so the rules see raw strings.
        schema = load(CANONICAL.CANONICAL_SCHEMA)
        schema["properties"]["freshness_deadline"].pop("format")
        for field in schema["properties"]["times"]["properties"].values():
            field.pop("format", None)
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            permissive = Path(tmp) / "schema.json"
            permissive.write_text(json.dumps(schema), encoding="utf-8")
            candidate = {**self.candidate(valid_to="2026-08-08T01:00:00", retrieved_at="yesterday"),
                         "freshness_deadline": "2027-08-08"}
            self.assertEqual(
                [
                    "valid_to has no UTC offset: '2026-08-08T01:00:00'",
                    "retrieved_at is not a parseable date-time: 'yesterday'",
                    "freshness_deadline has no UTC offset: '2027-08-08'",
                ],
                CANONICAL.validate_doc(candidate, schema_path=permissive, now=NOW),
            )

    def test_validation_now_comes_from_the_environment(self) -> None:
        stale = {**self.candidate(), "freshness_deadline": "2026-08-16T00:00:00Z"}
        from unittest.mock import patch

        with patch.dict("os.environ", {"KFM_VALIDATION_NOW": "2026-08-15t00:00:00z"}):
            self.assertEqual([], self.errors(stale, now=None))
        with patch.dict("os.environ", {"KFM_VALIDATION_NOW": "2026-08-17T00:00:00+00:00"}):
            self.assertEqual(["CURRENT envelope freshness_deadline is elapsed"], self.errors(stale, now=None))
        for configured, message in (("garbage", "KFM_VALIDATION_NOW is not a parseable date-time: 'garbage'"),
                                    ("2026-08-17T00:00:00", "KFM_VALIDATION_NOW has no UTC offset: '2026-08-17T00:00:00'")):
            with self.subTest(configured), patch.dict("os.environ", {"KFM_VALIDATION_NOW": configured}):
                with self.assertRaises(ValueError) as raised:
                    CANONICAL.validate_doc(stale)
                self.assertEqual(message, str(raised.exception))

    def test_cli_exit_codes(self) -> None:
        import io
        import tempfile
        from contextlib import redirect_stderr, redirect_stdout
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmp:
            lowered = Path(tmp) / "lowered.json"
            lowered.write_text(json.dumps(self.candidate(retrieved_at="2026-08-08t00:06:00z")), encoding="utf-8")
            listed = Path(tmp) / "list.json"
            listed.write_text("[]", encoding="utf-8")
            pinned = {"KFM_VALIDATION_NOW": NOW.isoformat()}  # the fixture's deadline must not age into a failure
            cases = [
                (lowered, pinned, 0, "valid\n", ""),
                (CANONICAL_ROOT / "invalid/inverted_validity.json", pinned, 1, "", "valid_from must not exceed valid_to\n"),
                (listed, pinned, 1, "", "input root must be an object\n"),
                (lowered, {"KFM_VALIDATION_NOW": "garbage"}, 2, "", "KFM_VALIDATION_NOW is not a parseable date-time: 'garbage'\n"),
            ]
            for module in (CANONICAL, LEGACY):
                for path, environ, code, out, err in cases:
                    stdout, stderr = io.StringIO(), io.StringIO()
                    with self.subTest(module=module.__name__, path=path.name, environ=environ), \
                            patch.dict("os.environ", environ), redirect_stdout(stdout), redirect_stderr(stderr):
                        self.assertEqual(code, module.main([str(path)]))
                    self.assertEqual((out, err), (stdout.getvalue(), stderr.getvalue()))


if __name__ == "__main__":
    unittest.main()
