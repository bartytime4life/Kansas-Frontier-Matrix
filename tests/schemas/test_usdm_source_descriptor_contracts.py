"""
tests/schemas/test_usdm_source_descriptor_contracts.py

Boundary and governance tests for the U.S. Drought Monitor (USDM) inactive
SourceDescriptor candidate and no-network connector fixtures.

These tests verify:
  1. The USDM source descriptor fixture is inactive and not released.
  2. No connector activation, live schedule, release, or publication authority
     is granted by the descriptor alone.
  3. Polygon spatial products and aggregate statistics are represented as
     separate artifact types.
  4. Native D0-D4 classifications and impact markers are preserved in fixtures.
  5. Connector outcome posture forbids writes to processed, catalog, triplet,
     proof, published, and release targets.
  6. No-network fixtures contain no sensitive data and require no live network.

None of these tests activate a connector, fetch from a live endpoint, or
produce catalog, release, or publication objects.
"""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

USDM_DESCRIPTOR_PATH = (
    ROOT
    / "fixtures/contracts/v1/source/source_descriptor/valid/valid_usdm_inactive.json"
)
GIS_FIXTURE_PATH = (
    ROOT / "fixtures/connectors/drought_monitor/gis_metadata_response.json"
)
STATISTICS_FIXTURE_PATH = (
    ROOT / "fixtures/connectors/drought_monitor/statistics_response.json"
)

FORBIDDEN_CONNECTOR_WRITE_TARGETS = [
    "data/processed",
    "data/catalog",
    "data/triplets",
    "data/proofs",
    "data/published",
    "release/",
]

EXPECTED_PERMITTED_OUTCOMES = {
    "admit_raw",
    "quarantine",
    "deny",
    "no_change",
    "superseded",
    "rate_limited",
    "skipped",
    "error",
}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# SourceDescriptor governance tests
# ---------------------------------------------------------------------------


def test_usdm_descriptor_fixture_exists():
    assert USDM_DESCRIPTOR_PATH.exists(), (
        f"USDM inactive SourceDescriptor fixture not found: {USDM_DESCRIPTOR_PATH}"
    )


def test_usdm_descriptor_is_proposed_not_active():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    assert descriptor["lifecycle"]["registry_state"] == "proposed", (
        "USDM SourceDescriptor must have registry_state='proposed', not 'active'. "
        "SourceDescriptor activation is a separate reviewed decision."
    )


def test_usdm_descriptor_connector_is_disabled():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    assert "connectors" in descriptor, "USDM descriptor must include connectors field."
    assert descriptor["connectors"]["activation_state"] == "disabled", (
        "USDM connector must remain disabled in the candidate descriptor. "
        "Activation requires explicit authorization."
    )


def test_usdm_descriptor_public_release_denied():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    assert descriptor["public_release"]["allowed"] is False, (
        "Public release must be denied in the USDM candidate descriptor. "
        "Release is a separate reviewed decision."
    )
    assert descriptor["public_release"]["requires_review"] is True, (
        "Public release must require review before it can be allowed."
    )


def test_usdm_descriptor_release_state_not_released():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    assert descriptor["release_state"] == "not_released", (
        "USDM SourceDescriptor must be 'not_released'. "
        "Documentation alone does not create a release."
    )


def test_usdm_descriptor_review_state_needs_review():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    assert descriptor["review_state"] == "needs_review", (
        "USDM SourceDescriptor must have review_state='needs_review'. "
        "It has not yet been through formal review."
    )


def test_usdm_descriptor_covers_correct_domains():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    domain_scope = set(descriptor["domain_scope"])
    expected = {"agriculture", "hydrology", "hazards"}
    assert expected == domain_scope, (
        f"USDM domain scope should be {expected}, got {domain_scope}."
    )


def test_usdm_descriptor_source_id_format():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    source_id = descriptor["source_id"]
    assert source_id.startswith("src:") or source_id.startswith("kfm://source/"), (
        f"source_id must use 'src:' or 'kfm://source/' prefix, got: {source_id!r}"
    )


def test_usdm_descriptor_rights_not_verified():
    """Rights must remain 'unknown' — not prematurely asserted as verified_open."""
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    rights_status = descriptor["rights"]["rights_status"]
    assert rights_status != "verified_open", (
        "USDM rights must not be 'verified_open' until rights are formally verified. "
        f"Current status: {rights_status!r}"
    )


def test_usdm_descriptor_not_for_life_safety():
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    prohibited = descriptor["admissibility_limits"]["prohibited_claim_roles"]
    assert "not_for_life_safety" in prohibited, (
        "USDM descriptor must prohibit 'not_for_life_safety' claim role. "
        "USDM is not an emergency declaration."
    )


# ---------------------------------------------------------------------------
# No-network fixture presence tests
# ---------------------------------------------------------------------------


def test_gis_fixture_exists():
    assert GIS_FIXTURE_PATH.exists(), (
        f"USDM GIS metadata no-network fixture not found: {GIS_FIXTURE_PATH}"
    )


def test_statistics_fixture_exists():
    assert STATISTICS_FIXTURE_PATH.exists(), (
        f"USDM statistics no-network fixture not found: {STATISTICS_FIXTURE_PATH}"
    )


def test_gis_fixture_requires_no_network():
    gis = _load(GIS_FIXTURE_PATH)
    meta = gis["_fixture_meta"]
    assert meta["network_status"] == "no_network_required", (
        "GIS fixture must declare network_status='no_network_required'."
    )


def test_statistics_fixture_requires_no_network():
    stats = _load(STATISTICS_FIXTURE_PATH)
    meta = stats["_fixture_meta"]
    assert meta["network_status"] == "no_network_required", (
        "Statistics fixture must declare network_status='no_network_required'."
    )


def test_gis_fixture_has_no_sensitive_data():
    gis = _load(GIS_FIXTURE_PATH)
    assert gis["_fixture_meta"]["sensitive_data"] is False


def test_statistics_fixture_has_no_sensitive_data():
    stats = _load(STATISTICS_FIXTURE_PATH)
    assert stats["_fixture_meta"]["sensitive_data"] is False


def test_gis_fixture_is_correct_source():
    gis = _load(GIS_FIXTURE_PATH)
    assert gis["_fixture_meta"]["source_id"] == "src:usdm-weekly"


def test_statistics_fixture_is_correct_source():
    stats = _load(STATISTICS_FIXTURE_PATH)
    assert stats["_fixture_meta"]["source_id"] == "src:usdm-weekly"


# ---------------------------------------------------------------------------
# Artifact separation tests
# ---------------------------------------------------------------------------


def test_gis_and_statistics_are_separate_artifact_types():
    """Polygon spatial products and aggregate statistics must be separate artifact types."""
    gis = _load(GIS_FIXTURE_PATH)
    stats = _load(STATISTICS_FIXTURE_PATH)
    assert gis["artifact_type"] == "polygon_spatial_product"
    assert stats["artifact_type"] == "aggregate_statistics"
    assert gis["artifact_type"] != stats["artifact_type"], (
        "GIS polygon product and statistics must be separate artifact types; "
        "they must not be collapsed into one record."
    )


def test_gis_and_statistics_share_release_identity():
    """Both artifacts from the same release week should share a release identity."""
    gis = _load(GIS_FIXTURE_PATH)
    stats = _load(STATISTICS_FIXTURE_PATH)
    assert gis["release_identity"]["release_week"] == stats["release_identity"]["release_week"], (
        "GIS and statistics artifacts from the same release week must share release_week identity."
    )
    assert gis["release_identity"]["source_valid_date"] == stats["release_identity"]["source_valid_date"]


def test_gis_fixture_preserves_temporal_fields():
    """Fixture must preserve separate cutoff, valid-date, and release-time fields."""
    gis = _load(GIS_FIXTURE_PATH)
    ri = gis["release_identity"]
    assert "source_data_cutoff_native" in ri, "source_data_cutoff_native must be present"
    assert "source_released_at_native" in ri, "source_released_at_native must be present"
    assert "source_valid_date" in ri, "source_valid_date must be present"
    # Cutoff and release times must be recorded separately — not collapsed
    assert ri["source_data_cutoff_native"] != ri["source_released_at_native"], (
        "Data cutoff and release time must be separate fields, not collapsed."
    )


def test_statistics_fixture_preserves_temporal_fields():
    """Statistics fixture must also preserve separate temporal fields."""
    stats = _load(STATISTICS_FIXTURE_PATH)
    ri = stats["release_identity"]
    assert "source_data_cutoff_native" in ri
    assert "source_released_at_native" in ri
    assert "source_valid_date" in ri


# ---------------------------------------------------------------------------
# Native classification preservation tests
# ---------------------------------------------------------------------------


def test_gis_fixture_preserves_d0_d4_classifications():
    gis = _load(GIS_FIXTURE_PATH)
    native_codes = {
        c["code"] for c in gis["native_classifications"]["categories"]
    }
    expected_codes = {None, "D0", "D1", "D2", "D3", "D4"}
    assert expected_codes == native_codes, (
        f"GIS fixture must preserve all D0-D4 classifications plus None. "
        f"Got: {native_codes}"
    )


def test_gis_fixture_preserves_impact_markers():
    gis = _load(GIS_FIXTURE_PATH)
    markers = gis["native_classifications"]["impact_markers"]
    assert "short_term" in markers
    assert "long_term" in markers
    assert "combined" in markers


def test_gis_fixture_crosswalk_is_advisory_only():
    gis = _load(GIS_FIXTURE_PATH)
    assert gis["native_classifications"]["crosswalk_posture"] == "advisory_only", (
        "Native USDM classifications must not be silently recoded; crosswalk is advisory only."
    )


def test_statistics_fixture_includes_all_drought_categories():
    stats = _load(STATISTICS_FIXTURE_PATH)
    categories = stats["statistics_structure"]["area_by_category"]["categories"]
    expected = {"None", "D0", "D1", "D2", "D3", "D4"}
    assert expected == set(categories), (
        f"Statistics fixture must include all drought categories. Got: {set(categories)}"
    )


# ---------------------------------------------------------------------------
# Connector boundary / authority tests
# ---------------------------------------------------------------------------


def test_gis_fixture_forbids_downstream_write_targets():
    gis = _load(GIS_FIXTURE_PATH)
    forbidden = set(gis["connector_outcome_posture"]["forbidden_targets"])
    for target in FORBIDDEN_CONNECTOR_WRITE_TARGETS:
        assert target in forbidden, (
            f"GIS fixture must list '{target}' as a forbidden connector write target."
        )


def test_statistics_fixture_forbids_downstream_write_targets():
    stats = _load(STATISTICS_FIXTURE_PATH)
    forbidden = set(stats["connector_outcome_posture"]["forbidden_targets"])
    for target in FORBIDDEN_CONNECTOR_WRITE_TARGETS:
        assert target in forbidden, (
            f"Statistics fixture must list '{target}' as a forbidden connector write target."
        )


def test_gis_fixture_permits_only_bounded_outcomes():
    gis = _load(GIS_FIXTURE_PATH)
    permitted = set(gis["connector_outcome_posture"]["permitted_outcomes"])
    assert permitted == EXPECTED_PERMITTED_OUTCOMES, (
        f"GIS fixture permitted outcomes must be exactly {EXPECTED_PERMITTED_OUTCOMES}. "
        f"Got: {permitted}"
    )


def test_statistics_fixture_permits_only_bounded_outcomes():
    stats = _load(STATISTICS_FIXTURE_PATH)
    permitted = set(stats["connector_outcome_posture"]["permitted_outcomes"])
    assert permitted == EXPECTED_PERMITTED_OUTCOMES, (
        f"Statistics fixture permitted outcomes must be exactly {EXPECTED_PERMITTED_OUTCOMES}. "
        f"Got: {permitted}"
    )


def test_usdm_descriptor_admissibility_prohibits_not_for_title_truth():
    """USDM must not be used for legal/title determinations."""
    descriptor = _load(USDM_DESCRIPTOR_PATH)
    prohibited = descriptor["admissibility_limits"]["prohibited_claim_roles"]
    assert "not_for_title_truth" in prohibited, (
        "USDM admissibility must prohibit 'not_for_title_truth'. "
        "USDM is not a legal or parcel determination."
    )
