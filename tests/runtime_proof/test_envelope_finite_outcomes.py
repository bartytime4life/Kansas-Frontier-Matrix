"""No-network proof of the finite RuntimeResponseEnvelope shape boundary.

These tests prove repository fixture shape and compatibility aliasing only.
They do not execute a runtime, resolve evidence, evaluate policy, authorize a
release, or establish that a response is safe to publish.
"""

from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import re
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CANONICAL_SCHEMA_PATH = REPOSITORY_ROOT / (
    "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
)
FOCUS_ALIAS_PATH = REPOSITORY_ROOT / (
    "schemas/contracts/v1/focus/runtime_response_envelope.schema.json"
)
FIXTURE_ROOT = REPOSITORY_ROOT / (
    "fixtures/contracts/v1/runtime/runtime_response_envelope"
)
EXPECTED_OUTCOMES = ("ANSWER", "ABSTAIN", "DENY", "ERROR")


def _load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected a JSON object: {path}")
    return value


def _shape_findings(
    value: dict[str, object], schema: dict[str, object]
) -> set[str]:
    """Check the closed top-level profile with only the Python standard library."""

    findings: set[str] = set()
    required = set(schema["required"])
    properties = schema["properties"]

    if missing := required - set(value):
        findings.add("required:" + ",".join(sorted(missing)))
    if schema.get("additionalProperties") is False and (
        extras := set(value) - set(properties)
    ):
        findings.add("additional:" + ",".join(sorted(extras)))

    for name in ("id", "spec_hash"):
        candidate = value.get(name)
        pattern = properties[name]["pattern"]
        if not isinstance(candidate, str) or re.fullmatch(pattern, candidate) is None:
            findings.add(f"pattern:{name}")

    if value.get("outcome") not in properties["outcome"]["enum"]:
        findings.add("enum:outcome")

    issued_at = value.get("issued_at")
    try:
        if not isinstance(issued_at, str):
            raise ValueError
        datetime.fromisoformat(issued_at.replace("Z", "+00:00"))
    except ValueError:
        findings.add("format:issued_at")

    for name in (
        "version",
        "reason_code",
        "policy_state",
        "freshness",
        "correction_state",
    ):
        if not isinstance(value.get(name), str):
            findings.add(f"type:{name}")

    evidence_refs = value.get("evidence_refs")
    if not isinstance(evidence_refs, list):
        findings.add("type:evidence_refs")
    else:
        for index, evidence_ref in enumerate(evidence_refs):
            if not isinstance(evidence_ref, dict):
                findings.add(f"type:evidence_refs/{index}")
                continue
            if not isinstance(evidence_ref.get("ref"), str):
                findings.add(f"required:evidence_refs/{index}/ref")
            if evidence_ref.get("kind") not in {
                "measurement",
                "record",
                "dataset",
                "artifact",
            }:
                findings.add(f"enum:evidence_refs/{index}/kind")
            if set(evidence_ref) - {"ref", "kind", "bundle_ref"}:
                findings.add(f"additional:evidence_refs/{index}")

    return findings


class FiniteRuntimeEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = _load_json(CANONICAL_SCHEMA_PATH)
        cls.focus_alias = _load_json(FOCUS_ALIAS_PATH)

    def test_canonical_schema_is_closed_to_four_outcomes(self) -> None:
        self.assertEqual(
            self.schema["properties"]["outcome"]["enum"],
            list(EXPECTED_OUTCOMES),
        )
        self.assertIs(self.schema["additionalProperties"], False)
        self.assertEqual(len(self.schema["required"]), 10)

    def test_focus_path_is_a_compatibility_alias_not_a_second_shape(self) -> None:
        self.assertEqual(self.focus_alias["$ref"], self.schema["$id"])
        self.assertEqual(
            self.focus_alias["x-kfm"]["canonical_schema"],
            CANONICAL_SCHEMA_PATH.relative_to(REPOSITORY_ROOT).as_posix(),
        )
        self.assertEqual(self.focus_alias["x-kfm"]["role"], "compatibility-alias")
        self.assertNotIn("properties", self.focus_alias)
        self.assertNotIn("additionalProperties", self.focus_alias)

    def test_valid_fixtures_cover_every_finite_outcome(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        fixtures = [_load_json(path) for path in paths]

        self.assertEqual(
            {fixture["outcome"] for fixture in fixtures}, set(EXPECTED_OUTCOMES)
        )
        self.assertEqual(
            len({fixture["id"] for fixture in fixtures}), len(fixtures)
        )
        for path, fixture in zip(paths, fixtures):
            self.assertEqual(_shape_findings(fixture, self.schema), set(), path)

        answer = next(item for item in fixtures if item["outcome"] == "ANSWER")
        self.assertTrue(answer["evidence_refs"])
        for outcome in ("DENY", "ERROR"):
            bounded = next(item for item in fixtures if item["outcome"] == outcome)
            self.assertEqual(bounded["evidence_refs"], [])

    def test_invalid_fixtures_fail_the_closed_shape(self) -> None:
        paths = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
        findings = {path.name: _shape_findings(_load_json(path), self.schema) for path in paths}

        self.assertTrue(all(finding_set for finding_set in findings.values()), findings)
        self.assertIn("required:id", findings["invalid_1.json"])
        self.assertIn("additional:extra_field", findings["invalid_2.json"])
        self.assertIn("pattern:id", findings["invalid_3.json"])
        self.assertIn("enum:outcome", findings["invalid_4.json"])


if __name__ == "__main__":
    unittest.main()
