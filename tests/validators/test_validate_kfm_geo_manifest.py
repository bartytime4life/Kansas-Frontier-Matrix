"""Deterministic no-network tests for the KFMGeoManifest fixture profile."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import os
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.evidence._kfm_geo_manifest import (
    MAX_MANIFEST_BYTES,
    MAX_SCHEMA_FINDINGS,
)
from tools.validators.evidence.validate_kfm_geo_manifest import (
    FIXTURE_ROOT,
    SCHEMA_PATH,
    canonical_spec_hash,
    load_fixture_cases,
    main,
    materialize_case,
    validate_manifest,
)


class KFMGeoManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "manifest.json"
        self.corpus = load_fixture_cases()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _case(self, lane: str, name: str) -> dict[str, object]:
        for case in self.corpus[lane]:
            if case.get("name") == name:
                return copy.deepcopy(dict(case))
        raise AssertionError(f"fixture case not found: {lane}/{name}")

    def _write(self, manifest: dict[str, object]) -> Path:
        self.path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        return self.path

    def assertCode(self, manifest: dict[str, object], code: str, payload: str | None = None) -> None:
        path = self._write(manifest)
        payload_path = None
        if payload is not None:
            payload_path = self.root / "payload.bin"
            payload_path.write_bytes(payload.encode("utf-8"))
        result = validate_manifest(path, payload_path)
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_three_valid_artifact_profiles_pass_with_exact_byte_binding(self) -> None:
        valid = self.corpus["valid"]
        self.assertEqual(len(valid), 3)
        observed = set()
        for case in valid:
            with self.subTest(case=case["name"]):
                manifest, payload = materialize_case(case, self.root)
                result = validate_manifest(manifest, payload)
                self.assertTrue(result.ok, result.findings)
                observed.add(case["manifest"]["artifact"]["artifact_type"])
        self.assertEqual(observed, {"pmtiles", "cog", "geojson"})

    def test_schema_and_semantic_negative_cases_match_exact_codes(self) -> None:
        self.assertEqual(len(self.corpus["invalid"]), 4)
        self.assertEqual(len(self.corpus["semantic_invalid"]), 11)
        for lane in ("invalid", "semantic_invalid"):
            for case in self.corpus[lane]:
                with self.subTest(lane=lane, case=case["name"]):
                    manifest, payload = materialize_case(case, self.root)
                    result = validate_manifest(manifest, payload if case.get("use_payload") is True else None)
                    actual = {finding.code for finding in result.findings}
                    self.assertFalse(result.ok)
                    self.assertEqual(actual, set(case["expected_codes"]))

    def test_semantic_negative_cases_remain_schema_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for case in self.corpus["semantic_invalid"]:
            with self.subTest(case=case["name"]):
                self.assertEqual(list(validator.iter_errors(case["manifest"])), [])

    def test_spec_hash_is_deterministic_profile_local_and_identity_bound(self) -> None:
        manifest = self._case("valid", "valid_pmtiles_release_candidate")["manifest"]
        self.assertEqual(manifest["spec_hash"], canonical_spec_hash(manifest))
        self.assertEqual(canonical_spec_hash(manifest), canonical_spec_hash(copy.deepcopy(manifest)))
        changed = copy.deepcopy(manifest)
        changed["id"] = "geo-manifest:synthetic:pmtiles-release-candidate:v2"
        self.assertNotEqual(canonical_spec_hash(manifest), canonical_spec_hash(changed))
        changed = copy.deepcopy(manifest)
        changed["spec_hash"] = "sha256:" + ("0" * 64)
        self.assertEqual(canonical_spec_hash(manifest), canonical_spec_hash(changed))

    def test_payload_digest_and_length_bind_exact_local_bytes(self) -> None:
        case = self._case("valid", "valid_pmtiles_release_candidate")
        manifest = case["manifest"]
        payload = case["payload_text"]
        wrong_same_length = payload[:-3] + "x1\n"
        self.assertEqual(len(payload.encode()), len(wrong_same_length.encode()))
        manifest_path = self._write(manifest)
        payload_path = self.root / "wrong-payload.bin"
        payload_path.write_bytes(wrong_same_length.encode("utf-8"))
        codes = {finding.code for finding in validate_manifest(manifest_path, payload_path).findings}
        self.assertIn("PAYLOAD_DIGEST_MISMATCH", codes)
        self.assertNotIn("PAYLOAD_LENGTH_MISMATCH", codes)

    def test_artifact_media_and_tiling_rules_fail_closed(self) -> None:
        pm = self._case("valid", "valid_pmtiles_release_candidate")["manifest"]
        mutated = copy.deepcopy(pm)
        mutated["artifact"]["media_type"] = "application/geo+json"
        mutated["spec_hash"] = canonical_spec_hash(mutated)
        self.assertCode(mutated, "MEDIA_TYPE_MISMATCH")

        mutated = copy.deepcopy(pm)
        mutated["spatial"]["scale_or_resolution"]["min_zoom"] = 15
        mutated["spatial"]["tiling_profile"]["min_zoom"] = 15
        mutated["spec_hash"] = canonical_spec_hash(mutated)
        self.assertCode(mutated, "ZOOM_RANGE_INVALID")

    def test_transform_chain_and_sensitive_transform_receipts_fail_closed(self) -> None:
        cog = self._case("valid", "valid_cog_generalized_derivative")["manifest"]
        mutated = copy.deepcopy(cog)
        mutated["derivation"]["transforms"][1]["input_digest"] = "sha256:" + ("1" * 64)
        mutated["spec_hash"] = canonical_spec_hash(mutated)
        self.assertCode(mutated, "TRANSFORM_CHAIN_BROKEN")

        mutated = copy.deepcopy(cog)
        mutated["derivation"]["transforms"][1]["receipt_ref"] = None
        mutated["spec_hash"] = canonical_spec_hash(mutated)
        self.assertCode(mutated, "SENSITIVITY_TRANSFORM_RECEIPT_REQUIRED")

    def test_governance_temporal_and_lineage_rules_fail_closed(self) -> None:
        pm = self._case("valid", "valid_pmtiles_release_candidate")["manifest"]
        mutations = (
            (lambda value: value["governance"].update(rights_state="unknown"), "PUBLIC_CANDIDATE_RIGHTS_BLOCKED"),
            (lambda value: value["governance"].update(policy_decision_ref=None), "POLICY_REFERENCE_REQUIRED"),
            (
                lambda value: value["claim_scope"]["temporal_scope"].update(
                    valid_from="2027-01-01T00:00:00Z",
                    valid_to="2026-01-01T00:00:00Z",
                ),
                "TEMPORAL_SCOPE_INVALID",
            ),
            (
                lambda value: value["lineage"].update(
                    supersedes=value["id"],
                    correction_refs=["correction:synthetic:self"],
                ),
                "SELF_LINEAGE_REFERENCE",
            ),
        )
        for mutate, code in mutations:
            with self.subTest(code=code):
                mutated = copy.deepcopy(pm)
                mutate(mutated)
                mutated["spec_hash"] = canonical_spec_hash(mutated)
                self.assertCode(mutated, code)

    def test_reference_arrays_must_be_canonical(self) -> None:
        pm = self._case("valid", "valid_pmtiles_release_candidate")["manifest"]
        mutated = copy.deepcopy(pm)
        mutated["evidence"]["evidence_refs"] = [
            "evidence-ref:synthetic:z",
            "evidence-ref:synthetic:a",
        ]
        mutated["spec_hash"] = canonical_spec_hash(mutated)
        self.assertCode(mutated, "REFERENCE_ARRAY_NOT_CANONICAL")

    def test_duplicate_keys_nonfinite_numbers_and_excessive_nesting_fail_closed(self) -> None:
        case = self._case("valid", "valid_pmtiles_release_candidate")
        text = json.dumps(case["manifest"], indent=2)
        duplicate = text.replace(
            '  "schema_version": "1.0.0",',
            '  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
            1,
        )
        self.path.write_text(duplicate, encoding="utf-8")
        self.assertIn("DUPLICATE_KEY", {finding.code for finding in validate_manifest(self.path).findings})

        self.path.write_text('{"value": NaN}\n', encoding="utf-8")
        self.assertIn("NONFINITE_NUMBER", {finding.code for finding in validate_manifest(self.path).findings})

        nested = "[" * 100 + "0" + "]" * 100
        self.path.write_text('{"nested":' + nested + "}\n", encoding="utf-8")
        self.assertIn("JSON_COMPLEXITY_LIMIT", {finding.code for finding in validate_manifest(self.path).findings})

    def test_oversized_symlink_and_fifo_inputs_fail_closed(self) -> None:
        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_MANIFEST_BYTES + 1))
        self.assertIn("FILE_TOO_LARGE", {finding.code for finding in validate_manifest(oversized).findings})

        target = self._write(self._case("valid", "valid_pmtiles_release_candidate")["manifest"])
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertIn("UNSAFE_FILE", {finding.code for finding in validate_manifest(linked).findings})

        if hasattr(os, "mkfifo"):
            fifo = self.root / "manifest.fifo"
            os.mkfifo(fifo)
            self.assertIn("UNSAFE_FILE", {finding.code for finding in validate_manifest(fifo).findings})

    def test_schema_findings_are_bounded(self) -> None:
        manifest = self._case("valid", "valid_pmtiles_release_candidate")["manifest"]
        mutated = copy.deepcopy(manifest)
        mutated["limitations"] = list(range(MAX_SCHEMA_FINDINGS + 50))
        result = validate_manifest(self._write(mutated))
        codes = {finding.code for finding in result.findings}
        self.assertIn("SCHEMA_FINDINGS_TRUNCATED", codes)
        self.assertLessEqual(len(result.findings), MAX_SCHEMA_FINDINGS + 1)

    def test_validation_performs_no_network_io(self) -> None:
        case = self._case("valid", "valid_pmtiles_release_candidate")
        manifest, payload = materialize_case(case, self.root)

        def unexpected_network(*_args, **_kwargs):
            raise AssertionError("KFMGeoManifest validation attempted network access")

        with (
            mock.patch.object(socket.socket, "connect", unexpected_network),
            mock.patch.object(socket, "create_connection", unexpected_network),
            mock.patch.object(urllib.request, "urlopen", unexpected_network),
        ):
            result = validate_manifest(manifest, payload)
        self.assertTrue(result.ok, result.findings)

    def test_cli_output_is_deterministic_and_does_not_echo_values(self) -> None:
        manifest = self._case("valid", "valid_pmtiles_release_candidate")["manifest"]
        sensitive_marker = "artifact:synthetic:private-marker"
        manifest["artifact"]["artifact_ref"] = sensitive_marker
        manifest["governance"]["public_use_allowed"] = True
        path = self._write(manifest)
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                code = main([str(path)])
            self.assertEqual(code, 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(sensitive_marker, outputs[0])

    def test_fixture_cli_passes(self) -> None:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(["--fixtures"])
        self.assertEqual(code, 0, stream.getvalue())
        self.assertNotIn("FIXTURE_POLARITY_ERROR", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
