"""Tests for Kansas water-planning domain schemas (Slice 2).

Validates that:
- All 15 water-planning entity schema valid fixtures pass validation.
- All invalid fixtures are rejected.
- The FY2027 ApplicationWindow stores the Central Time deadline correctly.
- HB 2462 is represented as a ProgramVersion, not overwriting prior history
  (supersedes_ref points to a prior version, not null).
- geometry_confidence rejects values outside the governed enum
  (no guessing of unresolved geometry).
- All 15 entity types have distinct schemas (anti-collapse check via title).
- RAC region numbers are bounded to 1–14.
"""

import json
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "contracts" / "v1" / "domains" / "water_planning"
FIXTURE_DIR = ROOT / "fixtures" / "domains" / "water_planning"

ENTITY_NAMES = [
    "planning_region",
    "public_meeting",
    "advisory_committee_meeting",
    "program_version",
    "scoring_matrix_version",
    "application_window",
    "application",
    "eligibility_decision",
    "recommendation",
    "award",
    "funding_agreement",
    "project",
    "construction_milestone",
    "completion",
    "correction_or_withdrawal",
]


def _schema(name: str) -> Path:
    return SCHEMA_DIR / f"{name}.schema.json"


def _valid_fixture(name: str, n: int = 1) -> Path:
    return FIXTURE_DIR / name / "valid" / f"valid_{n}.json"


def _invalid_fixture(name: str, n: int = 1) -> Path:
    return FIXTURE_DIR / name / "invalid" / f"invalid_{n}.json"


# ---------------------------------------------------------------------------
# Schema-file existence
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", ENTITY_NAMES)
def test_schema_file_exists(name: str) -> None:
    assert _schema(name).exists(), f"Schema file missing: {_schema(name)}"


# ---------------------------------------------------------------------------
# Schema titles are distinct (anti-collapse)
# ---------------------------------------------------------------------------


def test_all_schema_titles_are_distinct() -> None:
    titles = []
    for name in ENTITY_NAMES:
        schema = json.loads(_schema(name).read_text())
        titles.append(schema.get("title"))
    assert len(titles) == len(set(titles)), (
        f"Duplicate schema titles detected — entity types must not collapse: {titles}"
    )


# ---------------------------------------------------------------------------
# Valid fixtures pass, invalid fixtures fail
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", ENTITY_NAMES)
def test_valid_fixture_passes(name: str) -> None:
    schema_path = _schema(name)
    fixture_path = _valid_fixture(name)
    assert fixture_path.exists(), f"Valid fixture missing: {fixture_path}"
    validator = load_validator(schema_path)
    doc = json.loads(fixture_path.read_text(encoding="utf-8"))
    errors = list(validator.iter_errors(doc))
    assert not errors, f"{name} valid fixture failed:\n" + "\n".join(
        e.message for e in errors
    )


@pytest.mark.parametrize("name", ENTITY_NAMES)
def test_invalid_fixture_fails(name: str) -> None:
    schema_path = _schema(name)
    fixture_path = _invalid_fixture(name)
    assert fixture_path.exists(), f"Invalid fixture missing: {fixture_path}"
    validator = load_validator(schema_path)
    doc = json.loads(fixture_path.read_text(encoding="utf-8"))
    errors = list(validator.iter_errors(doc))
    assert errors, f"{name} invalid fixture should have failed but passed"


# ---------------------------------------------------------------------------
# Acceptance-criteria tests
# ---------------------------------------------------------------------------


def test_fy2027_deadline_stored_with_central_time() -> None:
    """FY 2027 deadline must be stored with explicit Central Time handling."""
    fixture = json.loads(_valid_fixture("application_window").read_text())
    closes_at = fixture["closes_at"]
    source_tz = fixture["source_timezone"]

    # The KWO-stated deadline: 11:59 p.m. on September 15, 2026 Central Time.
    assert "2026-09-15" in closes_at, (
        f"closes_at must reference the FY2027 deadline date; got {closes_at!r}"
    )
    assert "23:59" in closes_at, (
        f"closes_at must include the 23:59 time; got {closes_at!r}"
    )
    # UTC offset for Central Time (CDT = -05:00 in September).
    assert closes_at.endswith("-05:00") or closes_at.endswith("-06:00"), (
        f"closes_at must include a Central Time UTC offset; got {closes_at!r}"
    )
    assert source_tz == "America/Chicago", (
        f"source_timezone must be America/Chicago; got {source_tz!r}"
    )


def test_hb2462_represented_as_new_program_version() -> None:
    """HB 2462 must create a new ProgramVersion with supersedes_ref, not overwrite history."""
    fixture = json.loads(_valid_fixture("program_version").read_text())
    assert fixture["statutory_basis"] == "2026 HB 2462", (
        "statutory_basis must reference HB 2462"
    )
    assert fixture["supersedes_ref"] is not None, (
        "HB 2462 ProgramVersion must supersede a prior version (not null)"
    )
    assert fixture["fiscal_year"] == "FY2027", (
        "fiscal_year must follow FYnnnn pattern"
    )


def test_planning_region_rac_number_bounded_to_14() -> None:
    """RAC region numbers must be 1–14 (Kansas has exactly 14 RAC planning areas)."""
    schema_path = _schema("planning_region")
    validator = load_validator(schema_path)

    valid_doc = json.loads(_valid_fixture("planning_region").read_text())
    assert not list(validator.iter_errors(valid_doc))

    # rac_number = 15 must be rejected.
    invalid_doc = json.loads(_invalid_fixture("planning_region").read_text())
    assert invalid_doc["rac_number"] == 15
    errors = list(validator.iter_errors(invalid_doc))
    assert errors, "rac_number 15 must be rejected by the schema"


def test_geometry_confidence_rejects_guessed() -> None:
    """geometry_confidence must reject 'guessed' — missing geometry must be stored as unresolved."""
    schema_path = _schema("project")
    validator = load_validator(schema_path)
    invalid_doc = json.loads(_invalid_fixture("project").read_text())
    assert invalid_doc["geometry_confidence"] == "guessed"
    errors = list(validator.iter_errors(invalid_doc))
    assert errors, "'guessed' geometry_confidence must be rejected"


def test_unresolved_applicant_identity_is_explicit() -> None:
    """Missing applicant identity must be stored as applicant_resolution_status: unresolved."""
    fixture = json.loads(_valid_fixture("application").read_text())
    assert fixture["applicant_ref"] is None
    assert fixture["applicant_resolution_status"] == "unresolved"


def test_unresolved_recipient_identity_is_explicit() -> None:
    """Missing recipient identity must be stored as recipient_resolution_status: unresolved."""
    fixture = json.loads(_valid_fixture("project").read_text())
    assert fixture["recipient_ref"] is None
    assert fixture["recipient_resolution_status"] == "unresolved"


def test_amounts_are_distinct_across_event_types() -> None:
    """requested, recommended, awarded, and paid amounts must live in distinct entity types."""
    application_schema = json.loads(_schema("application").read_text())
    recommendation_schema = json.loads(_schema("recommendation").read_text())
    award_schema = json.loads(_schema("award").read_text())
    funding_agreement_schema = json.loads(_schema("funding_agreement").read_text())

    assert "requested_amount" in application_schema["properties"]
    assert "recommended_amount" in recommendation_schema["properties"]
    assert "awarded_amount" in award_schema["properties"]
    assert "paid_amount" in funding_agreement_schema["properties"]

    # None of the other schemas should claim another's amount field.
    assert "awarded_amount" not in application_schema["properties"]
    assert "paid_amount" not in award_schema["properties"]
    assert "requested_amount" not in award_schema["properties"]


def test_application_window_requires_source_timezone() -> None:
    """ApplicationWindow must require source_timezone for Central Time traceability."""
    invalid_fixture = json.loads(_invalid_fixture("application_window").read_text())
    schema_path = _schema("application_window")
    validator = load_validator(schema_path)
    errors = list(validator.iter_errors(invalid_fixture))
    assert errors
    assert any("source_timezone" in e.message for e in errors)


def test_scoring_matrix_and_program_version_are_distinct() -> None:
    """A scoring matrix is not a program version — they must have distinct schemas and titles."""
    pm_schema = json.loads(_schema("program_version").read_text())
    sm_schema = json.loads(_schema("scoring_matrix_version").read_text())
    assert pm_schema["title"] != sm_schema["title"]
    assert "program_name" in pm_schema["properties"]
    assert "program_name" not in sm_schema["properties"]
    assert "digest" in sm_schema["properties"]


def test_completion_is_distinct_from_award() -> None:
    """A completion event is not an award — they must have distinct schemas."""
    completion_schema = json.loads(_schema("completion").read_text())
    award_schema = json.loads(_schema("award").read_text())
    assert completion_schema["title"] != award_schema["title"]
    assert "completion_state" in completion_schema["properties"]
    assert "completion_state" not in award_schema["properties"]
