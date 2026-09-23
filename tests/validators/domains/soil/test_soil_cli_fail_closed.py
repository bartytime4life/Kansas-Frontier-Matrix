"""Single-file CLI proof for the soil evaluate-style validators.

Each validator must exit 0 only for its passing outcome, and must return a
finite ERROR (never a traceback) for unreadable, non-object, or structurally
malformed candidates.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOIL = ROOT / "tools/validators/domains/soil"

# validator stem -> (cases.json, passing outcomes)
VALIDATORS = {
    "soil_component": ("fixtures/domains/soil/soil_component/cases.json", {"PASS"}),
    "soil_map_unit": ("fixtures/domains/soil/soil_map_unit/cases.json", {"PASS"}),
    "component_horizon_join": ("fixtures/domains/soil/component_horizon_join/cases.json", {"PASS"}),
    "domain_observation": ("fixtures/domains/soil/domain_observation/cases.json", {"PASS"}),
    "domain_layer_descriptor": ("fixtures/domains/soil/domain_layer_descriptor/cases.json", {"PASS"}),
    "domain_validation_report": ("fixtures/domains/soil/domain_validation_report/cases.json", {"PASS"}),
    "domain_feature_identity": ("fixtures/domains/soil/domain_feature_identity/cases.json", {"PASS"}),
    "catalog_closure_assessment": (
        "fixtures/contracts/v1/domains/soil/catalog_closure_assessment/cases.json",
        {"READY_FOR_REVIEW", "HOLD"},
    ),
}

MALFORMED = {
    "list_root": "[]",
    "null_root": "null",
    "string_root": '"soil"',
    "unhashable_values": json.dumps(
        {
            "support_type": [],
            "geometry_posture": {},
            "temporal_scope": [1],
            "evidence_refs": [{"a": 1}, "b"],
            "source_refs": [1, "a"],
            "input_refs": [[1]],
            "findings": [{"code": "A", "severity": "x"}, {}],
            "object_role": [],
            "lifecycle_stage": [],
            "dimensions": [1],
        }
    ),
    "truncated_json": '{"profile": ',
}


def _run(stem: str, path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SOIL / f"validate_{stem}.py"), str(path)],
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


def _outcome(stdout: str) -> str:
    line = stdout.strip().splitlines()[-1]
    return json.loads(line)["outcome"] if line.startswith("{") else line


class SoilCliFailClosedTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)

    def test_malformed_inputs_are_finite_errors(self) -> None:
        for stem in VALIDATORS:
            for name, text in (*MALFORMED.items(), ("missing_file", None)):
                with self.subTest(validator=stem, case=name):
                    path = self.tmp / f"{stem}-{name}.json"
                    if text is not None:
                        path.write_text(text, encoding="utf-8")
                    result = _run(stem, path)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertEqual(1, result.returncode)
                    self.assertEqual("ERROR", _outcome(result.stdout))

    def test_exit_code_tracks_fixture_outcome(self) -> None:
        for stem, (cases_path, passing) in VALIDATORS.items():
            cases = json.loads((ROOT / cases_path).read_text(encoding="utf-8"))["cases"]
            for case in cases:
                expected = case.get("expected_outcome", case.get("expected"))
                with self.subTest(validator=stem, case=case["name"], expected=expected):
                    path = self.tmp / f"{stem}-{case['name']}.json"
                    path.write_text(json.dumps(case["candidate"]), encoding="utf-8")
                    result = _run(stem, path)
                    self.assertEqual(expected, _outcome(result.stdout))
                    self.assertEqual(0 if expected in passing else 1, result.returncode)


if __name__ == "__main__":
    unittest.main()
