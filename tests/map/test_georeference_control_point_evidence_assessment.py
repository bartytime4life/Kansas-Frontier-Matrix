"""Focused tests for fixture-only GCP evidence assessment."""
from __future__ import annotations

import copy
import json
import socket
import tempfile
from pathlib import Path
from unittest import mock

from tools.validators.map import validate_georeference_control_point_evidence_assessment as target


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
        expected = tuple(
            target.Finding(item["code"], item["path"])
            for item in definition["expected_findings"]
        )
        assert result.outcome == definition["expected_outcome"], definition["name"]
        assert result.findings == expected, definition["name"]
        counts[result.outcome] += 1
    assert counts == {"PASS": 1, "ABSTAIN": 8, "DENY": 19, "ERROR": 6}


def test_identity_is_deterministic_and_changes_with_observation():
    _, candidate = _case("complete_evidence_ready_for_review")
    assert candidate == target.assign_identity(candidate)
    assert candidate["assessment_id"].startswith(target.IDENTITY_PREFIX)
    changed = copy.deepcopy(candidate)
    changed["control_points"][0]["contrast"] = "ADEQUATE"
    changed["summary"] = target.expected_summary(changed)
    changed = target.assign_identity(changed)
    assert changed["spec_hash"] != candidate["spec_hash"]
    assert changed["assessment_id"] != candidate["assessment_id"]


def test_identity_subject_excludes_only_identity_fields():
    _, candidate = _case("complete_evidence_ready_for_review")
    subject = target.identity_subject(candidate)
    assert set(candidate) - set(subject) == {"assessment_id", "spec_hash"}


def test_pass_is_ready_for_review_with_zero_authority():
    _, candidate = _case("complete_evidence_ready_for_review")
    result = target.validate_payload(candidate)
    payload = json.loads(target._serialize(result))
    assert result.outcome == "PASS"
    assert candidate["recommendation"] == "READY_FOR_REVIEW"
    assert candidate["review_state"] == "HOLD"
    assert all(value is False for value in payload["authority"].values())


def test_partial_evidence_abstains_and_adverse_evidence_denies():
    _, partial = _case("point_visibility_partial")
    _, obscured = _case("point_visibility_obscured")
    assert target.validate_payload(partial).outcome == "ABSTAIN"
    assert target.validate_payload(obscured).outcome == "DENY"


def test_summary_is_derived_only_from_point_observations():
    _, candidate = _case("point_contrast_unknown")
    assert candidate["summary"] == {
        "clear_visibility_count": 5,
        "acceptable_contrast_count": 4,
        "adequate_scale_count": 5,
        "verified_match_count": 5,
    }


def test_source_idea_and_upstream_set_are_bound():
    document = json.loads(target.CASES.read_text(encoding="utf-8"))
    assert document["source_idea_ids"] == ["KFM-P18-INV-317"]
    assert document["base"]["source_idea_id"] == "KFM-P18-INV-317"
    assert document["base"]["control_point_set_ref"].startswith("kfm:georeference-gcp-set:sha256:")


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


def test_diagnostics_do_not_echo_candidate_references():
    for _definition, candidate in target.load_fixture_cases():
        result = target.validate_payload(candidate)
        diagnostic = target._serialize(result)
        assert candidate["control_point_set_ref"] not in diagnostic
        for reference in candidate["evidence_refs"]:
            assert reference not in diagnostic
