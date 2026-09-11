"""Deterministic tests for the inactive Soil support-type profile."""
from __future__ import annotations

import contextlib
import copy
import io
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.domains.soil.support_type import validate_support_type_profile as validator

from tools.validators.domains.soil.support_type.validate_support_type_profile import (
    FIXTURE_ROOT,
    PROFILE_PATH,
    Finding,
    validate_candidate,
    validate_file,
    validate_fixture_tree,
)


def _load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _digest(label: str) -> str:
    return "sha256:" + hashlib.sha256(label.encode("utf-8")).hexdigest()


class SoilSupportTypeProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = _load(PROFILE_PATH)
        cls.base_candidate = _load(
            FIXTURE_ROOT / "valid/station_soil_moisture.json"
        )

    def test_persisted_valid_fixtures_cover_every_support_type_once(self) -> None:
        expected = {
            rule["support_type"]
            for rule in self.profile["support_types"]
        }
        fixtures = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
        observed: dict[str, str] = {}

        for path in fixtures:
            candidate = _load(path)
            support_type = candidate["support_type"]
            self.assertNotIn(
                support_type,
                observed,
                f"duplicate positive fixture for {support_type}",
            )
            result = validate_file(path)
            self.assertTrue(result.ok, (path.name, result.findings))
            observed[support_type] = path.name

        self.assertEqual(set(observed), expected)
        self.assertEqual(len(fixtures), len(expected))

    def test_every_declared_support_type_accepts_a_minimal_candidate(self) -> None:
        rules = self.profile["support_types"]
        self.assertEqual(len(rules), 8)
        for index, rule in enumerate(rules):
            candidate = copy.deepcopy(self.base_candidate)
            candidate["candidate_id"] = (
                f"soil-support-candidate:generated-{index:04d}"
            )
            candidate["content_spec_hash"] = _digest(rule["support_type"])
            candidate["support_type"] = rule["support_type"]
            candidate["source_family"] = rule["source_families"][0]
            candidate["source_role"] = rule["source_roles"][0]
            candidate["spatial_support"] = rule["spatial_support"][0]
            candidate["claim_kind"] = rule["claim_kinds"][0]
            candidate["source_refs"] = [
                f"source:{candidate['source_family']}"
            ]
            candidate["evidence_refs"] = [
                f"evidence:synthetic-{index:04d}"
            ]
            with self.subTest(support_type=rule["support_type"]):
                result = validate_candidate(candidate, self.profile)
                self.assertTrue(result.ok, result.findings)
                self.assertEqual(result.outcome, "PASS")

    def test_fixture_tree_has_positive_and_negative_polarity(self) -> None:
        self.assertEqual(validate_fixture_tree(), ())

    def test_station_cannot_masquerade_as_satellite_grid(self) -> None:
        path = FIXTURE_ROOT / "invalid/station_as_satellite_grid.json"
        result = validate_file(path)
        codes = {finding.code for finding in result.findings}
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("CLAIM_KIND_NOT_ALLOWED", codes)
        self.assertIn("FORBIDDEN_CLAIM_KIND", codes)

    def test_satellite_grid_cannot_masquerade_as_station(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["candidate_id"] = (
            "soil-support-candidate:generated-satellite-collapse"
        )
        candidate["support_type"] = "satellite_soil_moisture_grid"
        candidate["source_family"] = "nasa_smap"
        candidate["source_role"] = "satellite_grid_measurement"
        candidate["spatial_support"] = "satellite_grid_cell"
        candidate["claim_kind"] = "current_station_condition"
        result = validate_candidate(candidate, self.profile)
        codes = {finding.code for finding in result.findings}
        self.assertIn("CLAIM_KIND_NOT_ALLOWED", codes)
        self.assertIn("FORBIDDEN_CLAIM_KIND", codes)

    def test_profile_digest_binding_is_required(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["profile_spec_hash"] = _digest("wrong-profile")
        result = validate_candidate(candidate, self.profile)
        self.assertIn(
            Finding("PROFILE_HASH_BINDING_MISMATCH", "/profile_spec_hash"),
            result.findings,
        )

    def test_public_use_request_fails_closed(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["public_use_requested"] = True
        result = validate_candidate(candidate, self.profile)
        codes = {finding.code for finding in result.findings}
        self.assertIn("CANDIDATE_SCHEMA_INVALID", codes)
        self.assertIn("PUBLIC_USE_DENIED", codes)

    def test_reference_order_is_deterministic(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["source_refs"] = ["source:z", "source:a"]
        result = validate_candidate(candidate, self.profile)
        self.assertIn(
            Finding("REFS_NOT_CANONICAL", "/source_refs"),
            result.findings,
        )

    def test_input_is_not_mutated(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        snapshot = copy.deepcopy(candidate)
        result = validate_candidate(candidate, self.profile)
        self.assertTrue(result.ok)
        self.assertEqual(candidate, snapshot)

    def test_duplicate_json_keys_are_rejected_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"SoilSupportTypeCandidate",'
                '"object_type":"duplicate"}',
                encoding="utf-8",
            )
            result = validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn(Finding("JSON_DUPLICATE_KEY", "/"), result.findings)

    def test_findings_are_sorted_and_repeatable(self) -> None:
        path = FIXTURE_ROOT / "invalid/station_as_satellite_grid.json"
        first = validate_file(path)
        second = validate_file(path)
        self.assertEqual(first, second)
        self.assertEqual(first.findings, tuple(sorted(first.findings)))


class SoilFixtureExecutionTests(unittest.TestCase):
    """Fixture execution must prove rejection, not reward evaluation failure."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for group in ("valid", "invalid"):
            (self.root / group).mkdir()
        self.positive = self.root / "valid/control.json"
        self.negative = self.root / "invalid/control.json"
        self.positive.write_bytes(
            (FIXTURE_ROOT / "valid/station_soil_moisture.json").read_bytes()
        )
        self.negative.write_bytes(
            (FIXTURE_ROOT / "invalid/station_as_satellite_grid.json").read_bytes()
        )

    def run_cli(self, *arguments: str) -> tuple[int, dict[str, object]]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = validator.main(list(arguments))
        return code, json.loads(output.getvalue())

    def test_cli_explicit_missing_profile_cannot_pass(self) -> None:
        code, report = self.run_cli(
            "--fixtures", "--fixture-root", str(self.root),
            "--profile", str(self.root / "missing.json"),
        )
        self.assertEqual(code, 1)
        self.assertEqual(report["outcome"], "ERROR")
        self.assertIn(
            {"code": "FILE_NOT_FOUND", "field": "/"}, report["findings"]
        )

    def test_cli_modes_are_exclusive_before_validation(self) -> None:
        with mock.patch.object(validator, "validate_fixture_tree") as fixtures:
            with mock.patch.object(validator, "validate_file") as candidate:
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as raised:
                        validator.main([
                            "--fixtures", "--candidate", str(self.negative),
                        ])
        self.assertEqual(raised.exception.code, 2)
        fixtures.assert_not_called()
        candidate.assert_not_called()

    def test_cli_requires_a_mode(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                validator.main([])
        self.assertEqual(raised.exception.code, 2)

    def test_explicit_valid_profile_is_used_for_every_fixture(self) -> None:
        profile = _load(PROFILE_PATH)
        profile["profile_version"] = "1.0.1"
        payload = json.dumps(
            {key: value for key, value in profile.items() if key != "spec_hash"},
            sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        ).encode("utf-8")
        profile["spec_hash"] = "sha256:" + hashlib.sha256(payload).hexdigest()
        profile_path = self.root / "selected-profile.json"
        profile_path.write_text(json.dumps(profile), encoding="utf-8")
        for path in (self.positive, self.negative):
            candidate = _load(path)
            candidate["profile_version"] = profile["profile_version"]
            candidate["profile_spec_hash"] = profile["spec_hash"]
            path.write_text(json.dumps(candidate), encoding="utf-8")
        code, report = self.run_cli(
            "--fixtures", "--fixture-root", str(self.root),
            "--profile", str(profile_path),
        )
        self.assertEqual((code, report["outcome"]), (0, "PASS"))
        self.assertEqual(report["findings"], [])
        # The same candidates must fail against the default profile.
        self.assertIn(
            Finding("VALID_FIXTURE_REJECTED", "/valid/control.json"),
            validate_fixture_tree(self.root),
        )

    def test_invalid_profile_stops_before_fixture_evaluation(self) -> None:
        for content in ("{", "{}", PROFILE_PATH.read_text().replace(
            '"profile_version": "1.0.0"', '"profile_version": "1.0.1"'
        )):
            with self.subTest(profile=content[:30]):
                path = self.root / "invalid-profile.json"
                path.write_text(content, encoding="utf-8")
                with mock.patch.object(validator, "validate_candidate") as evaluate:
                    findings = validate_fixture_tree(self.root, profile_path=path)
                self.assertEqual(validator.ValidationResult(findings).outcome, "ERROR")
                self.assertIn(Finding("PROFILE_INVALID", "/profile"), findings)
                evaluate.assert_not_called()

    def test_unreadable_negative_is_not_a_successful_rejection(self) -> None:
        malformed = (
            b"{", b"\xff", b'{"key":1,"key":2}', b'{"key":NaN}',
            b'{"key":1e999}', b"[]", b" " * (validator.MAX_JSON_BYTES + 1),
        )
        for payload in malformed:
            with self.subTest(payload=payload[:30]):
                self.negative.write_bytes(payload)
                code, report = self.run_cli(
                    "--fixtures", "--fixture-root", str(self.root),
                )
                self.assertEqual((code, report["outcome"]), (1, "ERROR"))
                self.assertEqual(report["findings"], [
                    {"code": "FIXTURE_EVALUATION_ERROR", "field": "/invalid/control.json"}
                ])

    def test_unreadable_positive_is_an_evaluation_error(self) -> None:
        self.positive.write_text("{", encoding="utf-8")
        findings = validate_fixture_tree(self.root)
        self.assertEqual(validator.ValidationResult(findings).outcome, "ERROR")
        self.assertIn(Finding("FIXTURE_EVALUATION_ERROR", "/valid/control.json"), findings)

    def test_disappearing_fixture_fails_closed(self) -> None:
        original = validator._read_object

        def read(path: Path):
            if path == self.negative:
                return None, [Finding("FILE_NOT_FOUND", "/")]
            return original(path)

        with mock.patch.object(validator, "_read_object", side_effect=read):
            findings = validate_fixture_tree(self.root)
        self.assertIn(Finding("FIXTURE_EVALUATION_ERROR", "/invalid/control.json"), findings)
        self.assertEqual(validator.ValidationResult(findings).outcome, "ERROR")

    def test_schema_failure_is_not_a_negative_control_success(self) -> None:
        with mock.patch.object(validator, "CANDIDATE_SCHEMA_PATH", self.root / "absent.json"):
            findings = validate_fixture_tree(self.root)
        self.assertEqual(validator.ValidationResult(findings).outcome, "ERROR")
        self.assertEqual(findings, (
            Finding("FIXTURE_EVALUATION_ERROR", "/invalid/control.json"),
            Finding("FIXTURE_EVALUATION_ERROR", "/valid/control.json"),
        ))

    def test_accepted_negative_is_still_denied(self) -> None:
        self.negative.write_bytes(self.positive.read_bytes())
        findings = validate_fixture_tree(self.root)
        self.assertEqual(findings, (
            Finding("INVALID_FIXTURE_ACCEPTED", "/invalid/control.json"),
        ))
        self.assertEqual(validator.ValidationResult(findings).outcome, "DENY")

    def test_rejected_positive_is_still_denied(self) -> None:
        self.positive.write_bytes(self.negative.read_bytes())
        findings = validate_fixture_tree(self.root)
        self.assertEqual(findings, (
            Finding("VALID_FIXTURE_REJECTED", "/valid/control.json"),
        ))

    def test_both_fixture_polarities_remain_required(self) -> None:
        for group in ("valid", "invalid"):
            with self.subTest(group=group):
                path = self.root / group / "control.json"
                payload = path.read_bytes()
                path.unlink()
                try:
                    findings = validate_fixture_tree(self.root)
                    self.assertIn(Finding(f"{group.upper()}_FIXTURES_MISSING", f"/{group}"), findings)
                finally:
                    path.write_bytes(payload)

    def test_candidate_cli_and_report_boundary_are_unchanged(self) -> None:
        for path, expected, exit_code in (
            (self.positive, "PASS", 0), (self.negative, "DENY", 1),
        ):
            with self.subTest(expected=expected):
                code, report = self.run_cli("--candidate", str(path))
                self.assertEqual((code, report["outcome"]), (exit_code, expected))
                self.assertEqual(report["authority"], "NONE")
                self.assertEqual(report["scope"], validator.SCOPE)
                self.assertEqual(set(report), {"scope", "outcome", "findings", "authority", "non_effects"})

    def test_fixture_check_is_repeatable_read_only_and_no_network(self) -> None:
        before = {p: p.read_bytes() for p in self.root.rglob("*.json")}
        with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
            with mock.patch("socket.create_connection", side_effect=AssertionError("network denied")):
                with mock.patch("urllib.request.urlopen", side_effect=AssertionError("network denied")):
                    first = self.run_cli("--fixtures", "--fixture-root", str(self.root))
                    second = self.run_cli("--fixtures", "--fixture-root", str(self.root))
        self.assertEqual(first, second)
        self.assertEqual(first[0], 0)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*.json")})


class SoilJsonBoundaryTests(unittest.TestCase):
    """Schema evaluation is local-only and malformed inputs stay finite."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / "input.json"
        self.path.write_text("{}", encoding="utf-8")

    def schema_findings(self, text: str, value=None):
        self.path.write_text(text, encoding="utf-8")
        return validator._schema_findings(
            {} if value is None else value, self.path, "TEST_SCHEMA_INVALID"
        )

    def test_read_is_bounded_even_when_opened_content_has_grown(self) -> None:
        class TrackedBytes(io.BytesIO):
            def __init__(self, payload):
                super().__init__(payload)
                self.requests = []

            def read(self, size=-1):
                self.requests.append(size)
                return super().read(size)

        # The path's size observation is only two bytes; its opened stream is
        # deliberately larger. Never use the separate stat as the read budget.
        stream = TrackedBytes(b" " * (validator.MAX_JSON_BYTES + 20))
        with mock.patch.object(Path, "open", return_value=stream) as opened:
            value, findings = validator._read_object(self.path)
        opened.assert_called_once_with("rb")
        self.assertEqual(stream.requests, [validator.MAX_JSON_BYTES + 1])
        self.assertIsNone(value)
        self.assertEqual(findings, [Finding("FILE_TOO_LARGE", "/")])

    def test_exact_byte_limit_is_accepted_and_one_more_is_error(self) -> None:
        payload = b"{}" + b" " * (validator.MAX_JSON_BYTES - 2)
        self.path.write_bytes(payload)
        self.assertEqual(validator._read_object(self.path), ({}, []))
        self.path.write_bytes(payload + b" ")
        _, findings = validator._read_object(self.path)
        self.assertEqual(findings, [Finding("FILE_TOO_LARGE", "/")])
        self.assertEqual(validator.ValidationResult(tuple(findings)).outcome, "ERROR")

    def test_byte_limit_precedes_utf8_decoding(self) -> None:
        self.path.write_bytes(b"\xff" * (validator.MAX_JSON_BYTES + 1))
        self.assertEqual(validator._read_object(self.path), (
            None, [Finding("FILE_TOO_LARGE", "/")]
        ))

    def test_parser_limits_have_finite_sanitized_findings(self) -> None:
        for exception in (ValueError, RecursionError):
            with self.subTest(exception=exception.__name__):
                with mock.patch.object(
                    validator.json, "loads", side_effect=exception("PRIVATE-SENTINEL")
                ):
                    value, findings = validator._read_object(self.path)
                self.assertIsNone(value)
                self.assertEqual(findings, [Finding("JSON_COMPLEXITY_LIMIT", "/")])
                result = validator.ValidationResult(tuple(findings))
                self.assertEqual(result.outcome, "ERROR")
                self.assertNotIn("PRIVATE-SENTINEL", json.dumps(validator._report(result)))

    def test_duplicate_nested_schema_key_cannot_weaken_validation(self) -> None:
        findings = self.schema_findings(
            '{"type":"object","properties":'
            '{"x":{"type":"integer","type":"string"}}}', {"x": "text"}
        )
        self.assertEqual(findings, [Finding("SCHEMA_UNAVAILABLE", "/")])

    def test_nonfinite_and_malformed_schema_inputs_are_unavailable(self) -> None:
        for text in ("{", "[]", "true", '{"maximum":NaN}',
                     '{"minimum":Infinity}', '{"maximum":1e999}'):
            with self.subTest(schema=text):
                self.assertEqual(self.schema_findings(text), [
                    Finding("SCHEMA_UNAVAILABLE", "/")
                ])

    def test_schema_error_does_not_escape_the_report(self) -> None:
        self.assertEqual(self.schema_findings('{"type":"not-a-real-type"}'), [
            Finding("SCHEMA_UNAVAILABLE", "/")
        ])

    def test_oversized_schema_uses_the_same_byte_budget(self) -> None:
        self.assertEqual(self.schema_findings(
            '{"description":"' + "x" * validator.MAX_JSON_BYTES + '"}'
        ), [Finding("SCHEMA_UNAVAILABLE", "/")])

    def test_external_references_never_attempt_retrieval(self) -> None:
        for keyword in ("$ref", "$dynamicRef"):
            for uri in ("https://example.invalid/schema.json",
                        "file:///never-read-kfm-test.json", "relative.json"):
                with self.subTest(keyword=keyword, uri=uri):
                    with mock.patch("urllib.request.urlopen") as urlopen:
                        with mock.patch("socket.socket") as socket:
                            with mock.patch("socket.create_connection") as connect:
                                findings = self.schema_findings(json.dumps({keyword: uri}))
                    self.assertEqual(findings, [Finding("SCHEMA_UNAVAILABLE", "/")])
                    urlopen.assert_not_called()
                    socket.assert_not_called()
                    connect.assert_not_called()

    def test_local_fragment_resolution_preserves_validation(self) -> None:
        schema = '{"$defs":{"value":{"type":"integer"}},"$ref":"#/$defs/value"}'
        self.assertEqual(self.schema_findings(schema, 7), [])
        self.assertEqual(self.schema_findings(schema, "seven"), [
            Finding("TEST_SCHEMA_INVALID", "/")
        ])
        self.assertEqual(self.schema_findings('{"$ref":"#/$defs/missing"}'), [
            Finding("SCHEMA_UNAVAILABLE", "/")
        ])

    def test_recursive_schema_failure_is_finite(self) -> None:
        self.assertEqual(self.schema_findings('{"$ref":"#"}'), [
            Finding("SCHEMA_UNAVAILABLE", "/")
        ])

    def test_invalid_schema_is_error_in_candidate_and_fixture_modes(self) -> None:
        self.path.write_text('{"type":"not-a-real-type"}', encoding="utf-8")
        for schema_path in ("PROFILE_SCHEMA_PATH", "CANDIDATE_SCHEMA_PATH"):
            for mode in (["--candidate", str(FIXTURE_ROOT / "valid/station_soil_moisture.json")],
                         ["--fixtures"]):
                with self.subTest(schema=schema_path, mode=mode[0]):
                    output = io.StringIO()
                    with mock.patch.object(validator, schema_path, self.path):
                        with contextlib.redirect_stdout(output):
                            code = validator.main(mode)
                    report = json.loads(output.getvalue())
                    self.assertEqual((code, report["outcome"]), (1, "ERROR"))
                    self.assertEqual(report["authority"], "NONE")
                    self.assertNotIn("not-a-real-type", output.getvalue())


if __name__ == "__main__":
    unittest.main()
