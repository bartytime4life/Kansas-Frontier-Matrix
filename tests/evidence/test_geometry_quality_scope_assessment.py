"""Focused tests for fixture-only geometry quality scope assessment."""
from __future__ import annotations

import copy
import json
import socket
import tempfile
from pathlib import Path
from unittest import mock

from tools.validators.evidence import validate_geometry_quality_scope_assessment as target


def _case(name: str):
    return next(item for item in target.load_fixture_cases() if item[0]["name"] == name)


def test_schema_is_draft_2020_12_and_meta_valid():
    schema = json.loads(target.SCHEMA.read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    target.Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_four_way_polarity():
    counts = {"PASS": 0, "ABSTAIN": 0, "DENY": 0, "ERROR": 0}
    for definition, candidate in target.load_fixture_cases():
        result = target.validate_payload(candidate)
        expected = tuple(target.Finding(item["code"], item["path"]) for item in definition["expected_findings"])
        assert result.outcome == definition["expected_outcome"], definition["name"]
        assert result.findings == expected, definition["name"]
        counts[result.outcome] += 1
    assert counts == {"PASS": 4, "ABSTAIN": 5, "DENY": 14, "ERROR": 3}


def test_identity_is_deterministic_and_binds_quality_dimensions():
    _, candidate = _case("dataset_quality_inherited_ready_for_review")
    assert candidate == target.assign_identity(candidate)
    changed = copy.deepcopy(candidate)
    changed["quality_records"][0]["precision_class"] = "KILOMETER_OR_COARSER"
    changed["quality_records"][0]["derivation"]["precision_effect"] = "COARSENED"
    changed = target.assign_identity(changed)
    assert changed["spec_hash"] != candidate["spec_hash"]
    assert changed["assessment_id"] != candidate["assessment_id"]


def test_identity_subject_excludes_only_identity_fields():
    _, candidate = _case("dataset_quality_inherited_ready_for_review")
    subject = target.identity_subject(candidate)
    assert set(candidate) - set(subject) == {"assessment_id", "spec_hash"}


def test_pass_is_fitness_review_only_with_zero_authority():
    _, candidate = _case("dataset_quality_inherited_ready_for_review")
    result = target.validate_payload(candidate)
    payload = json.loads(target._serialize(result))
    assert result.outcome == "PASS"
    assert candidate["recommendation"] == "READY_FOR_FITNESS_REVIEW"
    assert candidate["review_state"] == "HOLD"
    assert all(value is False for value in payload["authority"].values())


def test_fine_precision_does_not_imply_accuracy():
    _, candidate = _case("fine_precision_does_not_imply_accuracy")
    record = candidate["quality_records"][0]
    assert record["precision_class"] == "SUB_METER"
    assert record["accuracy_class"] == "HUNDRED_METER"
    assert target.validate_payload(candidate).outcome == "PASS"


def test_dataset_feature_and_mixed_attachment_modes_are_supported():
    names = (
        "dataset_quality_inherited_ready_for_review",
        "feature_explicit_quality",
        "mixed_dataset_default_with_feature_override",
    )
    modes = set()
    for name in names:
        _, candidate = _case(name)
        assert target.validate_payload(candidate).outcome == "PASS"
        modes.add(candidate["quality_scope"]["mode"])
    assert modes == {"DATASET_INHERITED", "FEATURE_EXPLICIT", "MIXED_OVERRIDE"}


def test_unknown_dimensions_and_scope_abstain():
    for name in ("quality_scope_unknown", "accuracy_unknown", "precision_unknown"):
        _, candidate = _case(name)
        assert target.validate_payload(candidate).outcome == "ABSTAIN"


def test_derived_quality_cannot_claim_improvement():
    _, accuracy = _case("derived_accuracy_cannot_improve")
    _, precision = _case("derived_precision_cannot_improve")
    assert "ACCURACY_IMPROVEMENT_UNSUPPORTED" in {item.code for item in target.validate_payload(accuracy).findings}
    assert "PRECISION_IMPROVEMENT_UNSUPPORTED" in {item.code for item in target.validate_payload(precision).findings}


def test_summary_is_derived_from_quality_records():
    _, candidate = _case("mixed_dataset_default_with_feature_override")
    assert candidate["summary"] == {
        "record_count": 2,
        "dataset_record_count": 1,
        "feature_record_count": 1,
        "resolved_accuracy_count": 2,
        "resolved_precision_count": 2,
    }


def test_source_idea_and_no_coordinate_boundary_are_bound():
    document = json.loads(target.CASES.read_text(encoding="utf-8"))
    assert document["source_idea_id"] == target.SOURCE_IDEA
    assert "coordinates" not in document["base"]
    assert document["base"]["effects"]["coordinates_read"] is False
    assert document["base"]["effects"]["feature_identities_disclosed"] is False


def test_fixture_replay_needs_no_network():
    def deny(*_args, **_kwargs):
        raise AssertionError("network access attempted")

    with (
        mock.patch.object(socket, "socket", side_effect=deny),
        mock.patch.object(socket, "create_connection", side_effect=deny),
        mock.patch.object(socket, "getaddrinfo", side_effect=deny),
    ):
        assert target.replay_fixtures() == 0


def test_duplicate_key_nonfinite_and_nonobject_are_errors():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        duplicate = root / "duplicate.json"
        nonfinite = root / "nonfinite.json"
        nonobject = root / "nonobject.json"
        duplicate.write_text('{"profile":"x","profile":"y"}', encoding="utf-8")
        nonfinite.write_text('{"value":NaN}', encoding="utf-8")
        nonobject.write_text("[]", encoding="utf-8")
        assert target.validate_file(duplicate).findings == (target.Finding("JSON_DUPLICATE_KEY", "/"),)
        assert target.validate_file(nonfinite).findings == (target.Finding("JSON_NONFINITE_NUMBER", "/"),)
        assert target.validate_file(nonobject).findings == (target.Finding("ROOT_NOT_OBJECT", "/"),)


def test_symlink_input_is_denied():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        real = root / "real.json"
        link = root / "link.json"
        real.write_text("{}", encoding="utf-8")
        try:
            link.symlink_to(real)
        except (OSError, NotImplementedError):
            return
        assert target.validate_file(link).findings == (target.Finding("INPUT_SYMLINK_DENIED", "/"),)


def test_cli_contract():
    assert target.main([]) == 2
    assert target.main(["--fixtures", str(target.CASES)]) == 2
    assert target.main(["--fixtures"]) == 0


def test_validator_does_not_import_network_or_geospatial_runtimes():
    source = Path(target.__file__).read_text(encoding="utf-8")
    denied = (
        "import requests", "import httpx", "import urllib", "import subprocess",
        "import rasterio", "import pyproj", "from osgeo", "import geopandas",
    )
    assert not any(marker in source for marker in denied)


def test_diagnostics_do_not_echo_dataset_or_provenance_refs():
    for _definition, candidate in target.load_fixture_cases():
        diagnostic = target._serialize(target.validate_payload(candidate))
        assert candidate["dataset_ref"] not in diagnostic
        for record in candidate["quality_records"]:
            if record["provenance_ref"] is not None:
                assert record["provenance_ref"] not in diagnostic
