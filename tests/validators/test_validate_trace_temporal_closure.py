from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
