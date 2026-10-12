"""Standard-library proof of the finite RuntimeResponseEnvelope shape boundary.

This suite intentionally avoids importing the repository's jsonschema-based
validator. The canonical validator is exercised by schema/validator workflows;
this bounded proof keeps the `focus-mock-test` job dependency-free after Python
setup while checking the same fixture family, finite outcomes, compatibility
alias, and critical precision-disclosure invariants.

The proof does not resolve evidence, evaluate policy, authorize an answer,
establish release state, or publish.
"""
from __future__ import annotations

import ast
from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path
import re
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CANONICAL_SCHEMA_PATH = (
    REPOSITORY_ROOT
    / "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
)
FOCUS_ALIAS_PATH = (
    REPOSITORY_ROOT
    / "schemas/contracts/v1/focus/runtime_response_envelope.schema.json"
)
FIXTURE_ROOT = (
    REPOSITORY_ROOT
    / "fixtures/contracts/v1/runtime/runtime_response_envelope"
)
VALIDATOR_PATH = (
    REPOSITORY_ROOT
    / "tools/validators/validate_runtime_response_envelope.py"
)
EXPECTED_OUTCOMES = ("ANSWER", "ABSTAIN", "DENY", "ERROR")
TOP_REQUIRED = frozenset(
    {
        "id",
        "spec_hash",
        "version",
        "issued_at",
        "outcome",
        "reason_code",
        "evidence_refs",
        "policy_state",
        "freshness",
        "correction_state",
    }
)
TOP_ALLOWED = TOP_REQUIRED | {"precision_actually_used"}
ID_RE = re.compile(r"^[a-z][a-z0-9_:.-]*$")
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
RECEIPT_REF_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$")
EVIDENCE_KINDS = frozenset({"measurement", "record", "dataset", "artifact"})
SPATIAL_REPRESENTATIONS = frozenset(
    {"point", "line", "polygon", "grid", "raster", "aggregate", "none"}
)
FRESHNESS_CLASSES = frozenset(
    {"current", "stale-accepted", "historical", "unknown"}
)


def _load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected a JSON object: {path}")
    return value


def _canonical(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def _is_unique(values: object) -> bool:
    return isinstance(values, list) and len(values) == len(
        {_canonical(item) for item in values}
    )


def _is_datetime(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        instant = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return instant.tzinfo is not None


def _bounded_text(value: object) -> bool:
    return isinstance(value, str) and 1 <= len(value) <= 256


def _valid_evidence_ref(value: object) -> bool:
    if not isinstance(value, dict):
        return False
    if not {"ref", "kind"} <= set(value) <= {"ref", "kind", "bundle_ref"}:
        return False
    if not isinstance(value.get("ref"), str):
        return False
    if value.get("kind") not in EVIDENCE_KINDS:
        return False
    return "bundle_ref" not in value or isinstance(value.get("bundle_ref"), str)


def _exact_object(
    value: object,
    *,
    required: frozenset[str],
    optional: frozenset[str] = frozenset(),
) -> bool:
    return (
        isinstance(value, dict)
        and required <= set(value)
        and set(value) <= required | optional
    )


def _precision_findings(
    precision: object,
    top_evidence_refs: object,
) -> list[str]:
    findings: set[str] = set()
    required = frozenset(
        {
            "spatial",
            "temporal",
            "attribute",
            "evidence_refs",
            "transform_receipt_refs",
        }
    )
    if not _exact_object(
        precision,
        required=required,
        optional=frozenset({"requested_precision"}),
    ):
        return ["PRECISION_SHAPE_INVALID"]
    assert isinstance(precision, dict)

    spatial = precision["spatial"]
    if not _exact_object(
        spatial,
        required=frozenset(
            {
                "representation",
                "resolution",
                "accuracy",
                "generalization_applied",
            }
        ),
    ):
        findings.add("SPATIAL_PRECISION_INVALID")
    else:
        assert isinstance(spatial, dict)
        if spatial.get("representation") not in SPATIAL_REPRESENTATIONS:
            findings.add("SPATIAL_PRECISION_INVALID")
        if not _bounded_text(spatial.get("resolution")):
            findings.add("SPATIAL_PRECISION_INVALID")
        if not _bounded_text(spatial.get("accuracy")):
            findings.add("SPATIAL_PRECISION_INVALID")
        if not isinstance(spatial.get("generalization_applied"), bool):
            findings.add("SPATIAL_PRECISION_INVALID")

    temporal = precision["temporal"]
    if not _exact_object(
        temporal,
        required=frozenset(
            {"granularity", "observation_interval", "freshness_class"}
        ),
    ):
        findings.add("TEMPORAL_PRECISION_INVALID")
    else:
        assert isinstance(temporal, dict)
        if not _bounded_text(temporal.get("granularity")):
            findings.add("TEMPORAL_PRECISION_INVALID")
        if temporal.get("freshness_class") not in FRESHNESS_CLASSES:
            findings.add("TEMPORAL_PRECISION_INVALID")
        interval = temporal.get("observation_interval")
        if not _exact_object(
            interval,
            required=frozenset({"start", "end"}),
        ):
            findings.add("TEMPORAL_PRECISION_INVALID")
        else:
            assert isinstance(interval, dict)
            start = interval.get("start")
            end = interval.get("end")
            if not _is_datetime(start) or not _is_datetime(end):
                findings.add("TEMPORAL_PRECISION_INVALID")
            else:
                assert isinstance(start, str) and isinstance(end, str)
                start_instant = datetime.fromisoformat(
                    start.replace("Z", "+00:00")
                )
                end_instant = datetime.fromisoformat(
                    end.replace("Z", "+00:00")
                )
                if start_instant > end_instant:
                    findings.add("PRECISION_INTERVAL_INVERTED")

    attribute = precision["attribute"]
    if not _exact_object(
        attribute,
        required=frozenset(
            {
                "measure",
                "unit",
                "significant_precision",
                "classification_granularity",
            }
        ),
    ):
        findings.add("ATTRIBUTE_PRECISION_INVALID")
    else:
        assert isinstance(attribute, dict)
        if not _bounded_text(attribute.get("measure")):
            findings.add("ATTRIBUTE_PRECISION_INVALID")
        if not _bounded_text(attribute.get("unit")):
            findings.add("ATTRIBUTE_PRECISION_INVALID")
        significant = attribute.get("significant_precision")
        if type(significant) is not int or not 0 <= significant <= 12:
            findings.add("ATTRIBUTE_PRECISION_INVALID")
        granularity = attribute.get("classification_granularity")
        if granularity is not None and not _bounded_text(granularity):
            findings.add("ATTRIBUTE_PRECISION_INVALID")

    requested = precision.get("requested_precision")
    if requested is not None:
        if (
            not isinstance(requested, dict)
            or not requested
            or not set(requested) <= {"spatial", "temporal", "attribute"}
            or any(not _bounded_text(item) for item in requested.values())
        ):
            findings.add("REQUESTED_PRECISION_INVALID")

    precision_refs = precision["evidence_refs"]
    if (
        not isinstance(precision_refs, list)
        or not precision_refs
        or len(precision_refs) > 128
        or not _is_unique(precision_refs)
        or any(not _valid_evidence_ref(item) for item in precision_refs)
    ):
        findings.add("PRECISION_EVIDENCE_INVALID")
    elif isinstance(top_evidence_refs, list):
        top = {_canonical(item) for item in top_evidence_refs}
        if any(_canonical(item) not in top for item in precision_refs):
            findings.add("PRECISION_EVIDENCE_NOT_TOP_LEVEL")

    receipt_refs = precision["transform_receipt_refs"]
    if (
        not isinstance(receipt_refs, list)
        or len(receipt_refs) > 128
        or not _is_unique(receipt_refs)
        or any(
            not isinstance(item, str)
            or not RECEIPT_REF_RE.fullmatch(item)
            for item in receipt_refs
        )
    ):
        findings.add("TRANSFORM_RECEIPTS_INVALID")
    if (
        isinstance(spatial, dict)
        and spatial.get("generalization_applied") is True
        and isinstance(receipt_refs, list)
        and not receipt_refs
    ):
        findings.add("GENERALIZATION_RECEIPT_REQUIRED")

    return sorted(findings)


def _shape_findings(value: dict[str, object]) -> list[str]:
    findings: set[str] = set()
    keys = set(value)
    if not TOP_REQUIRED <= keys:
        findings.add("REQUIRED_FIELD_MISSING")
    if not keys <= TOP_ALLOWED:
        findings.add("ADDITIONAL_PROPERTY")
    if findings:
        return sorted(findings)

    if not isinstance(value.get("id"), str) or not ID_RE.fullmatch(
        str(value["id"])
    ):
        findings.add("ID_INVALID")
    if not isinstance(value.get("spec_hash"), str) or not SHA256_RE.fullmatch(
        str(value["spec_hash"])
    ):
        findings.add("SPEC_HASH_INVALID")
    for name in (
        "version",
        "reason_code",
        "policy_state",
        "freshness",
        "correction_state",
    ):
        if not isinstance(value.get(name), str):
            findings.add(f"{name.upper()}_INVALID")
    if not _is_datetime(value.get("issued_at")):
        findings.add("ISSUED_AT_INVALID")
    if value.get("outcome") not in EXPECTED_OUTCOMES:
        findings.add("OUTCOME_INVALID")

    evidence_refs = value.get("evidence_refs")
    if (
        not isinstance(evidence_refs, list)
        or len(evidence_refs) > 128
        or not _is_unique(evidence_refs)
        or any(not _valid_evidence_ref(item) for item in evidence_refs)
    ):
        findings.add("EVIDENCE_REFS_INVALID")

    if value.get("outcome") == "ANSWER":
        if not isinstance(evidence_refs, list) or not evidence_refs:
            findings.add("ANSWER_EVIDENCE_REQUIRED")
        findings.update(
            _precision_findings(
                value.get("precision_actually_used"),
                evidence_refs,
            )
        )
    elif "precision_actually_used" in value:
        findings.add("PRECISION_FORBIDDEN")

    return sorted(findings)


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
        self.assertEqual(
            frozenset(self.schema["required"]),
            TOP_REQUIRED,
        )
        self.assertIn(
            "precision_actually_used",
            self.schema["properties"],
        )
        self.assertTrue(self.schema["allOf"])

    def test_focus_path_is_a_compatibility_alias_not_a_second_shape(self) -> None:
        self.assertEqual(self.focus_alias["$ref"], self.schema["$id"])
        self.assertEqual(
            self.focus_alias["x-kfm"]["canonical_schema"],
            CANONICAL_SCHEMA_PATH.relative_to(REPOSITORY_ROOT).as_posix(),
        )
        self.assertEqual(
            self.focus_alias["x-kfm"]["role"],
            "compatibility-alias",
        )
        self.assertNotIn("properties", self.focus_alias)

    def test_valid_fixtures_cover_outcomes_and_disclose_answer_precision(
        self,
    ) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        fixtures = [_load_json(path) for path in paths]
        self.assertEqual(
            {item["outcome"] for item in fixtures},
            set(EXPECTED_OUTCOMES),
        )
        self.assertEqual(
            len({item["id"] for item in fixtures}),
            len(fixtures),
        )
        for path, value in zip(paths, fixtures):
            self.assertEqual(_shape_findings(value), [], path)
            if value["outcome"] == "ANSWER":
                self.assertIn("precision_actually_used", value)
                self.assertTrue(value["evidence_refs"])
            else:
                self.assertNotIn("precision_actually_used", value)

    def test_existing_invalid_fixtures_remain_rejected(self) -> None:
        paths = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
        findings = {
            path.name: _shape_findings(_load_json(path))
            for path in paths
        }
        self.assertTrue(all(value for value in findings.values()), findings)
        self.assertEqual(
            set(findings),
            {
                "invalid_1.json",
                "invalid_2.json",
                "invalid_3.json",
                "invalid_4.json",
            },
        )

    def test_precision_semantics_fail_closed_without_external_packages(
        self,
    ) -> None:
        answer = _load_json(FIXTURE_ROOT / "valid/valid_2.json")

        unsupported = deepcopy(answer)
        unsupported["precision_actually_used"]["evidence_refs"] = [
            {"ref": "obs:other", "kind": "measurement"}
        ]
        self.assertIn(
            "PRECISION_EVIDENCE_NOT_TOP_LEVEL",
            _shape_findings(unsupported),
        )

        generalized = deepcopy(answer)
        generalized["precision_actually_used"]["spatial"][
            "generalization_applied"
        ] = True
        self.assertIn(
            "GENERALIZATION_RECEIPT_REQUIRED",
            _shape_findings(generalized),
        )

        inverted = deepcopy(answer)
        inverted["precision_actually_used"]["temporal"][
            "observation_interval"
        ] = {
            "start": "2026-05-10T00:00:00Z",
            "end": "2026-05-09T00:00:00Z",
        }
        self.assertIn(
            "PRECISION_INTERVAL_INVERTED",
            _shape_findings(inverted),
        )

    def test_canonical_validator_source_remains_wired(self) -> None:
        validator_text = VALIDATOR_PATH.read_text(encoding="utf-8")
        ast.parse(validator_text, filename=str(VALIDATOR_PATH))
        self.assertIn(
            "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json",
            validator_text,
        )
        self.assertIn(
            "fixtures/contracts/v1/runtime/runtime_response_envelope",
            validator_text,
        )


if __name__ == "__main__":
    unittest.main()
