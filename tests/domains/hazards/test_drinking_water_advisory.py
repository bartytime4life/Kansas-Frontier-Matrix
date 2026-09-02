from __future__ import annotations

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/domains/hazards/validate_drinking_water_advisory.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hazards/drinking_water_advisory.schema.json"
)
COMMON_SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/common/advisory_event_envelope.schema.json"
)


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "drinking_water_advisory_validator",
        VALIDATOR_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("validator module unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = _load_module()


class DrinkingWaterAdvisoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = validator.load_fixture_cases()
        cls.by_name = {
            raw_case["name"]: (raw_case, candidate)
            for raw_case, candidate in cls.cases
        }
        cls.valid = {
            name: candidate
            for name, (_, candidate) in cls.by_name.items()
            if name.startswith("valid_")
        }

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        observed = {"PASS": 0, "DENY": 0, "ERROR": 0}
        for raw_case, candidate in self.cases:
            result = validator.validate_payload(candidate)
            observed[result.outcome] += 1
            self.assertEqual(result.outcome, raw_case["expected_outcome"], raw_case["name"])
            self.assertEqual(
                sorted({finding.code for finding in result.findings}),
                raw_case["expected_findings"],
                raw_case["name"],
            )
        self.assertEqual(observed, {"PASS": 5, "DENY": 12, "ERROR": 1})

    def test_finite_valid_status_partition(self) -> None:
        self.assertEqual(
            {
                candidate["advisory"]["normalized_status"]
                for candidate in self.valid.values()
            },
            {
                "ISSUED",
                "ACTIVE_CONFIRMED",
                "RESCINDED",
                "STATUS_UNCONFIRMED",
                "IDENTITY_CONFLICT",
            },
        )
        for candidate in self.valid.values():
            self.assertEqual(set(candidate["effects"].values()), {False})
            self.assertFalse(candidate["controls"]["public_use_allowed"])
            self.assertFalse(candidate["controls"]["alerts_allowed"])
            self.assertEqual(candidate["controls"]["release_state"], "UNRELEASED")

    def test_every_source_failure_stays_unconfirmed(self) -> None:
        base = self.valid["valid_source_failure_unconfirmed"]
        for outcome in sorted(validator.SOURCE_FAILURES):
            candidate = copy.deepcopy(base)
            candidate["source_surface"]["source_check_outcome"] = outcome
            candidate = validator.assign_identity(candidate)
            result = validator.validate_payload(candidate)
            self.assertTrue(result.ok, (outcome, result.findings))
            self.assertEqual(candidate["advisory"]["normalized_status"], "STATUS_UNCONFIRMED")
            self.assertFalse(candidate["advisory"]["clears_prior_advisory"])

    def test_only_complete_authoritative_rescission_clears(self) -> None:
        valid = self.valid["valid_authoritative_rescission"]
        self.assertTrue(valid["advisory"]["clears_prior_advisory"])
        mutations = (
            ("authority", "rescission_notice_ref", None),
            ("authority", "rescission_authority_ref", None),
            ("authority", "rescission_authority_status", "UNRESOLVED"),
            ("advisory", "rescinded_at", None),
            ("controls", "prior_advisory_ref", None),
            ("source_surface", "source_check_outcome", "NOT_FOUND"),
        )
        for section, field, value in mutations:
            candidate = copy.deepcopy(valid)
            candidate[section][field] = value
            candidate = validator.assign_identity(candidate)
            result = validator.validate_payload(candidate)
            self.assertFalse(result.ok, (section, field))
            self.assertIn(
                "RESCISSION_REQUIRED",
                {finding.code for finding in result.findings},
            )

    def test_unknown_offsets_are_not_used_as_exact_temporal_evidence(self) -> None:
        base = self.valid["valid_authoritative_rescission"]
        timestamp_fields = (
            ("source_surface", "checked_at"),
            ("advisory", "issued_at"),
            ("advisory", "effective_at"),
            ("advisory", "expires_at"),
            ("advisory", "rescinded_at"),
        )
        for section, field in timestamp_fields:
            candidate = copy.deepcopy(base)
            value = candidate[section][field]
            self.assertIsInstance(value, str)
            candidate[section][field] = value.removesuffix("Z") + "-00:00"
            candidate = validator.assign_identity(candidate)

            result = validator.validate_payload(candidate)

            self.assertEqual(result.outcome, "DENY", (section, field, result.findings))
            expected_findings = {
                ("TIMESTAMP_UNKNOWN_OFFSET", f"/{section}/{field}")
            }
            if section == "advisory" and field == "rescinded_at":
                expected_findings.add(("RESCISSION_REQUIRED", "/advisory"))
            self.assertEqual(
                {(finding.code, finding.path) for finding in result.findings},
                expected_findings,
            )
            self.assertNotIn(
                "TEMPORAL_ORDER_INVALID",
                {finding.code for finding in result.findings},
            )

    def test_unknown_offset_preserves_independent_temporal_findings(self) -> None:
        candidate = copy.deepcopy(self.valid["valid_authoritative_rescission"])
        candidate["advisory"]["expires_at"] = "2026-08-12T13:00:00-00:00"
        candidate["advisory"]["issued_at"] = "2026-08-10T13:30:00Z"
        candidate = validator.assign_identity(candidate)

        result = validator.validate_payload(candidate)

        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            {(finding.code, finding.path) for finding in result.findings},
            {
                ("TEMPORAL_ORDER_INVALID", "/advisory/issued_at"),
                ("TIMESTAMP_UNKNOWN_OFFSET", "/advisory/expires_at"),
            },
        )

    def test_temporal_order_findings_bind_to_corrective_fields(self) -> None:
        scenarios = (
            ("valid_issued", "issued_at", "2026-08-10T13:30:00Z", "/advisory/issued_at"),
            ("valid_issued", "effective_at", "2026-08-10T15:00:00Z", "/advisory/effective_at"),
            ("valid_issued", "expires_at", "2026-08-10T12:30:00Z", "/advisory/expires_at"),
            ("valid_authoritative_rescission", "rescinded_at", "2026-08-10T12:30:00Z", "/advisory/rescinded_at"),
            ("valid_authoritative_rescission", "rescinded_at", "2026-08-12T12:00:00Z", "/advisory/rescinded_at"),
        )
        for base_name, field, value, expected_path in scenarios:
            with self.subTest(field=field, value=value):
                candidate = copy.deepcopy(self.valid[base_name])
                candidate["advisory"][field] = value
                candidate = validator.assign_identity(candidate)

                result = validator.validate_payload(candidate)

                self.assertEqual(result.outcome, "DENY")
                self.assertEqual(
                    {(finding.code, finding.path) for finding in result.findings},
                    {("TEMPORAL_ORDER_INVALID", expected_path)},
                )

    def test_current_status_cannot_outlive_exact_expiry(self) -> None:
        for base_name in ("valid_issued", "valid_active_not_modified"):
            with self.subTest(base_name=base_name):
                candidate = copy.deepcopy(self.valid[base_name])
                candidate["advisory"]["expires_at"] = "2026-08-10T13:30:00Z"
                candidate = validator.assign_identity(candidate)

                result = validator.validate_payload(candidate)

                self.assertEqual(result.outcome, "DENY")
                self.assertEqual(
                    {(finding.code, finding.path) for finding in result.findings},
                    {("TEMPORAL_ORDER_INVALID", "/advisory/expires_at")},
                )

    def test_unknown_intermediate_preserves_independent_time_bounds(self) -> None:
        scenarios = (
            ("valid_issued", "issued_at", "2026-08-10T15:00:00Z", "/advisory/issued_at"),
            ("valid_issued", "expires_at", "2026-08-10T11:00:00Z", "/advisory/expires_at"),
            (
                "valid_authoritative_rescission",
                "rescinded_at",
                "2026-08-10T11:00:00Z",
                "/advisory/rescinded_at",
            ),
        )
        for base_name, field, value, expected_path in scenarios:
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.valid[base_name])
                candidate["advisory"]["effective_at"] = (
                    "2026-08-10T13:00:00-00:00"
                )
                candidate["advisory"][field] = value
                candidate = validator.assign_identity(candidate)

                result = validator.validate_payload(candidate)

                self.assertEqual(result.outcome, "DENY")
                self.assertEqual(
                    {(finding.code, finding.path) for finding in result.findings},
                    {
                        ("TEMPORAL_ORDER_INVALID", expected_path),
                        ("TIMESTAMP_UNKNOWN_OFFSET", "/advisory/effective_at"),
                    },
                )

    def test_semantic_time_admission_matches_schema_format(self) -> None:
        lowercase = copy.deepcopy(self.valid["valid_authoritative_rescission"])
        for section, field in (
            ("source_surface", "checked_at"),
            ("advisory", "issued_at"),
            ("advisory", "effective_at"),
            ("advisory", "expires_at"),
            ("advisory", "rescinded_at"),
        ):
            lowercase[section][field] = lowercase[section][field].replace("T", "t")
        lowercase = validator.assign_identity(lowercase)
        self.assertTrue(validator.validate_payload(lowercase).ok)

        malformed = copy.deepcopy(self.valid["valid_authoritative_rescission"])
        malformed["advisory"]["issued_at"] = "2026-08-10 13:30:00+00:00"
        malformed = validator.assign_identity(malformed)
        result = validator.validate_payload(malformed)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            {(finding.code, finding.path) for finding in result.findings},
            {("SCHEMA_INVALID", "/advisory/issued_at")},
        )

    def test_malformed_unknown_offset_suffix_cannot_support_rescission(self) -> None:
        candidate = copy.deepcopy(self.valid["valid_authoritative_rescission"])
        candidate["advisory"]["rescinded_at"] = "nonsense-00:00"
        candidate = validator.assign_identity(candidate)

        result = validator.validate_payload(candidate)

        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            {(finding.code, finding.path) for finding in result.findings},
            {
                ("RESCISSION_REQUIRED", "/advisory"),
                ("SCHEMA_INVALID", "/advisory/rescinded_at"),
            },
        )
        self.assertNotIn(
            "TIMESTAMP_UNKNOWN_OFFSET",
            {finding.code for finding in result.findings},
        )

    def test_service_area_is_not_administrative_context(self) -> None:
        for name in (
            "valid_issued",
            "valid_active_not_modified",
            "valid_authoritative_rescission",
        ):
            self.assertEqual(self.valid[name]["scope"]["scope_role"], "SERVICE_AREA")
        unconfirmed = self.valid["valid_source_failure_unconfirmed"]
        self.assertEqual(unconfirmed["scope"]["scope_role"], "ADMINISTRATIVE_CONTEXT")
        self.assertIsNone(unconfirmed["scope"]["service_area_ref"])
        collapse = self.by_name["city_boundary_as_service_area"][1]
        self.assertEqual(
            {finding.code for finding in validator.validate_payload(collapse).findings},
            {"ADMINISTRATIVE_SCOPE_COLLAPSE"},
        )

    def test_shared_advisory_mechanics_crosswalk_is_bounded(self) -> None:
        common = json.loads(COMMON_SCHEMA_PATH.read_text(encoding="utf-8"))
        advisory = common["$defs"]["advisory"]["properties"]
        common_statuses = set(advisory["normalized_status"]["enum"])
        status_map = {
            "ISSUED": "ISSUED",
            "ACTIVE_CONFIRMED": "ACTIVE_CONFIRMED",
            "UPDATED": "UPDATED",
            "RESCINDED": "RESCINDED",
            "STATUS_UNCONFIRMED": "STATUS_UNCONFIRMED",
            "IDENTITY_CONFLICT": "IDENTITY_CONFLICT",
            "SOURCE_CONFLICT": "STATUS_UNCONFIRMED",
        }
        self.assertTrue(set(status_map.values()).issubset(common_statuses))
        self.assertIn("regulatory_advisory", advisory["basis"]["enum"])
        common_scope_roles = set(
            common["$defs"]["scope"]["properties"]["geometry_role"]["enum"]
        )
        scope_map = {
            "SERVICE_AREA": "advisory_area",
            "ADMINISTRATIVE_CONTEXT": "administrative_zone",
            "UNRESOLVED": "unresolved",
        }
        self.assertTrue(set(scope_map.values()).issubset(common_scope_roles))
        for candidate in self.valid.values():
            self.assertEqual(
                candidate["shared_mechanics"]["contract_ref"],
                "contracts/common/advisory_event_envelope.md",
            )

    def test_identity_is_stable_across_mapping_key_order(self) -> None:
        candidate = self.valid["valid_issued"]
        reordered = {key: candidate[key] for key in reversed(list(candidate))}
        self.assertEqual(validator.canonical_spec_hash(reordered), candidate["spec_hash"])
        self.assertEqual(validator.expected_advisory_id(reordered), candidate["advisory_id"])

    def test_duplicate_key_nonfinite_and_symlink_paths_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inputs = {
                "duplicate.json": '{"profile":"a","profile":"b"}',
                "nonfinite.json": '{"value":NaN}',
            }
            expected = {
                "duplicate.json": "JSON_DUPLICATE_KEY",
                "nonfinite.json": "JSON_NONFINITE_NUMBER",
            }
            for name, content in inputs.items():
                path = root / name
                path.write_text(content, encoding="utf-8")
                result = validator.validate_file(path)
                self.assertEqual(result.outcome, "ERROR")
                self.assertEqual(result.findings[0].code, expected[name])
            if hasattr(os, "symlink"):
                target = root / "target.json"
                target.write_text("{}", encoding="utf-8")
                link = root / "link.json"
                link.symlink_to(target)
                result = validator.validate_file(link)
                self.assertEqual(result.outcome, "ERROR")
                self.assertEqual(result.findings[0].code, "INPUT_SYMLINK_DENIED")

                nested = root / "nested"
                nested.mkdir()
                nested_input = nested / "input.json"
                nested_input.write_text("{}", encoding="utf-8")
                alias = root / "alias"
                alias.symlink_to(nested, target_is_directory=True)
                result = validator.validate_file(alias / "input.json")
                self.assertEqual(result.outcome, "ERROR")
                self.assertEqual(result.findings[0].code, "INPUT_SYMLINK_DENIED")

                loop = root / "loop"
                loop.symlink_to(loop, target_is_directory=True)
                result = validator.validate_file(loop / "input.json")
                self.assertEqual(result.outcome, "ERROR")
                self.assertEqual(result.findings[0].code, "INPUT_SYMLINK_DENIED")

    def test_regular_file_ancestor_is_not_reported_as_a_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            ancestor = Path(directory) / "ancestor.json"
            ancestor.write_text("{}", encoding="utf-8")

            result = validator.validate_file(ancestor / "input.json")

            self.assertEqual(result.outcome, "ERROR")
            self.assertEqual(
                [(finding.code, finding.path) for finding in result.findings],
                [("FILE_NOT_FOUND", "/")],
            )

    def test_embedded_nul_path_is_not_reported_as_invalid_json(self) -> None:
        result = validator.validate_file(Path("input\x00.json"))

        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            [(finding.code, finding.path) for finding in result.findings],
            [("FILE_NOT_FOUND", "/")],
        )

    def test_descriptor_traversal_binds_read_to_opened_directory(self) -> None:
        if not getattr(os, "O_NOFOLLOW", 0) or not getattr(os, "O_DIRECTORY", 0):
            self.skipTest("descriptor no-follow traversal unavailable")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "input.json").write_text(
                '{"origin":"safe"}',
                encoding="utf-8",
            )
            attacker = root / "attacker"
            attacker.mkdir()
            (attacker / "input.json").write_text(
                '{"origin":"attacker"}',
                encoding="utf-8",
            )
            pinned = root / "source-pinned"
            original_open = os.open
            swapped = False

            def racing_open(path, flags, mode=0o600, *, dir_fd=None):
                nonlocal swapped
                if dir_fd is None:
                    descriptor = original_open(path, flags, mode)
                else:
                    descriptor = original_open(path, flags, mode, dir_fd=dir_fd)
                if path == "source" and flags & os.O_DIRECTORY and not swapped:
                    source.rename(pinned)
                    source.symlink_to(attacker, target_is_directory=True)
                    swapped = True
                return descriptor

            with mock.patch.object(validator.os, "open", side_effect=racing_open):
                candidate, findings = validator._read(source / "input.json")

            self.assertTrue(swapped)
            self.assertEqual(findings, [])
            self.assertEqual(candidate, {"origin": "safe"})

    def test_fifo_input_fails_without_waiting_for_a_writer(self) -> None:
        if not hasattr(os, "mkfifo") or not getattr(os, "O_NONBLOCK", 0):
            self.skipTest("nonblocking FIFO admission unavailable")
        with tempfile.TemporaryDirectory() as directory:
            fifo = Path(directory) / "input.json"
            os.mkfifo(fifo, mode=0o600)

            result = validator.validate_file(fifo)

            self.assertEqual(result.outcome, "ERROR")
            self.assertEqual(
                [(finding.code, finding.path) for finding in result.findings],
                [("FILE_NOT_FOUND", "/")],
            )

    def test_file_growth_after_fstat_remains_size_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_bytes(b"{}")
            original_fstat = os.fstat
            grew = False

            def growing_fstat(file_descriptor):
                nonlocal grew
                metadata = original_fstat(file_descriptor)
                if not grew:
                    with path.open("ab") as stream:
                        stream.write(b" " * validator.MAX_FILE_BYTES)
                    grew = True
                return metadata

            with mock.patch.object(
                validator.os,
                "fstat",
                side_effect=growing_fstat,
            ):
                result = validator.validate_file(path)

            self.assertTrue(grew)
            self.assertEqual(result.outcome, "ERROR")
            self.assertEqual(
                [(finding.code, finding.path) for finding in result.findings],
                [("FILE_TOO_LARGE", "/")],
            )

    def test_validator_has_no_network_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import httpx",
            "import aiohttp",
            "import socket",
            "from urllib",
            "urlopen(",
        )
        self.assertFalse(any(token in source for token in forbidden))

    def test_cli_pass_is_bounded_and_value_free(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(json.dumps(self.valid["valid_issued"]), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["findings"], [])
        self.assertEqual(set(payload["authority"].values()), {False})
        self.assertNotIn("KS-SYNTHETIC-PWS-001", completed.stdout)
        self.assertNotIn("synthetic-city-001", completed.stdout)

    def test_fixture_cli_replays_every_case(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        rows = [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
        self.assertEqual(len(rows), 18)
        self.assertEqual({row["outcome"] for row in rows}, {"PASS", "DENY", "ERROR"})

    def test_cli_rejects_ambiguous_fixture_modes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(json.dumps(self.valid["valid_issued"]), encoding="utf-8")
            commands = (
                ["--fixture"],
                ["--fixtures", str(path)],
                ["--fixtures", "--fixtures"],
            )
            for arguments in commands:
                with self.subTest(arguments=arguments):
                    completed = subprocess.run(
                        [sys.executable, str(VALIDATOR_PATH), *arguments],
                        cwd=REPO_ROOT,
                        check=False,
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(completed.returncode, 2)
                    self.assertEqual(completed.stdout, "")

    def test_option_terminator_allows_fixture_named_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "--fixtures"
            path.write_text(json.dumps(self.valid["valid_issued"]), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), "--", path.name],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["name"], "--fixtures")


if __name__ == "__main__":
    unittest.main()
