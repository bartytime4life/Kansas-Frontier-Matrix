"""Focused tests for the fixture-only retrieval query assessment."""
from __future__ import annotations

import copy
import json
import socket
import tempfile
from pathlib import Path
from unittest import mock

from tools.validators.source import validate_retrieval_intent_query_snapshot_assessment as target


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
    assert counts == {"PASS": 2, "ABSTAIN": 2, "DENY": 20, "ERROR": 4}


def test_identity_and_query_hash_are_deterministic():
    _, candidate = _case("matched_complete_ready_for_review")
    assert candidate == target.assign_identity(candidate)
    assert candidate["assessment_id"].startswith(target.IDENTITY_PREFIX)
    changed = copy.deepcopy(candidate)
    changed["query_snapshot"]["result_count"] = 28
    target._derive_receipt(changed)
    changed = target.assign_identity(changed)
    assert changed["query_snapshot"]["query_hash"] != candidate["query_snapshot"]["query_hash"]
    assert changed["spec_hash"] != candidate["spec_hash"]


def test_identity_subject_excludes_only_assessment_identity_fields():
    _, candidate = _case("matched_complete_ready_for_review")
    subject = target.identity_subject(candidate)
    assert set(candidate) - set(subject) == {"assessment_id", "spec_hash"}


def test_pass_is_review_only_with_zero_authority():
    _, candidate = _case("matched_complete_ready_for_review")
    result = target.validate_payload(candidate)
    payload = json.loads(target._serialize(result))
    assert result.outcome == "PASS"
    assert candidate["decision"] == {"recommendation": "READY_FOR_REVIEW", "review_state": "HOLD"}
    assert all(value is False for value in payload["authority"].values())


def test_incomplete_and_failed_retrievals_abstain():
    _, partial = _case("partial_execution_abstains")
    _, failed = _case("failed_execution_abstains_without_empty_claim")
    assert target.validate_payload(partial).outcome == "ABSTAIN"
    assert partial["retrieval_receipt"]["result_interpretation"] == "RESULT_INCOMPLETE_NO_CLAIM"
    assert target.validate_payload(failed).outcome == "ABSTAIN"
    assert failed["retrieval_receipt"]["result_interpretation"] == "RETRIEVAL_FAILED_NO_CLAIM"


def test_changed_query_is_denied_with_exact_deviation():
    _, candidate = _case("requested_fields_changed")
    result = target.validate_payload(candidate)
    assert result.outcome == "DENY"
    assert candidate["retrieval_receipt"]["outcome"] == "CHANGED_QUERY"
    assert candidate["retrieval_receipt"]["deviation_codes"] == ["FIELDS_CHANGED"]


def test_zero_records_remains_no_claim():
    _, candidate = _case("matched_zero_records_is_no_claim")
    assert target.validate_payload(candidate).outcome == "PASS"
    assert candidate["retrieval_receipt"]["result_interpretation"] == "ZERO_RECORDS_NO_CLAIM"


def test_source_ideas_and_secret_exclusion_are_bound():
    document = json.loads(target.CASES.read_text(encoding="utf-8"))
    assert document["source_idea_ids"] == target.SOURCE_IDEAS
    assert document["base"]["retrieval_intent"]["secrets_embedded"] is False
    assert document["base"]["query_snapshot"]["secret_values_recorded"] is False


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


def test_validator_does_not_import_network_or_source_runtimes():
    source = Path(target.__file__).read_text(encoding="utf-8")
    denied = (
        "import requests", "import httpx", "import urllib", "import subprocess",
        "import boto", "import sqlalchemy", "import psycopg", "from connectors",
    )
    assert not any(marker in source for marker in denied)


def test_diagnostics_do_not_echo_descriptor_or_digests():
    for _definition, candidate in target.load_fixture_cases():
        diagnostic = target._serialize(target.validate_payload(candidate))
        assert candidate["source_descriptor_ref"] not in diagnostic
        assert candidate["query_snapshot"]["request_digest"] not in diagnostic
        if candidate["query_snapshot"]["response_digest"] is not None:
            assert candidate["query_snapshot"]["response_digest"] not in diagnostic
