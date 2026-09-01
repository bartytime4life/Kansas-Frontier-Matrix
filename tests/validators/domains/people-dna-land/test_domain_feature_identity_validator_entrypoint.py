from __future__ import annotations

import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_domain_feature_identity.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/people-dna-land/domain_feature_identity.schema.json"
)
VALID_FIXTURE = (
    REPO_ROOT
    / "fixtures/domains/people-dna-land/domain_feature_identity/valid/"
    "synthetic_public_safe_historical_aggregate.json"
)

FORBIDDEN_PUBLIC_FIXTURE_KEYS = {
    "address",
    "birth_date",
    "community_genetics",
    "current_owner",
    "dna",
    "full_name",
    "genome",
    "genomic",
    "health_trait",
    "kit_id",
    "kinship",
    "latitude",
    "longitude",
    "name",
    "parcel_id",
    "paternity",
    "person_parcel_join",
    "segment",
    "tribal_genetics",
    "vendor_id",
}


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "people_dna_land_domain_feature_identity_validator", MODULE_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fixture_polarity_is_executable_and_fail_closed():
    module = _load_module()
    assert module.main(["--fixtures"]) == 0


def test_no_input_fails_closed():
    module = _load_module()
    assert module.main([]) == 2


def test_fixture_mode_cannot_silently_skip_an_explicit_candidate():
    module = _load_module()
    assert module.main(["--fixtures", str(VALID_FIXTURE)]) == 2


def test_schema_declares_the_executable_fixture_and_validator_bindings():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    bindings = schema["x-kfm"]

    assert bindings["fixtures_root"] == (
        "fixtures/domains/people-dna-land/domain_feature_identity/"
    )
    assert bindings["validator"] == (
        "tools/validators/domains/people-dna-land/"
        "validate_domain_feature_identity.py"
    )
    assert (REPO_ROOT / bindings["fixtures_root"]).is_dir()
    assert (REPO_ROOT / bindings["validator"]).is_file()


def test_valid_fixture_is_public_safe_aggregate_and_non_authoritative():
    fixture = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))

    assert fixture["id"].startswith("pdl-feature-identity:synthetic-")
    assert fixture["domain"] == "people-dna-land"
    assert fixture["object_role"] == "HistoricalPopulationAggregate"
    assert fixture["sensitivity"] == "public-safe-aggregate"
    assert fixture["temporal_scope"]["precision"] == "decade"
    assert fixture["authority"]
    assert all(value is False for value in fixture["authority"].values())

    def keys(value):
        if isinstance(value, dict):
            for key, nested in value.items():
                yield key
                yield from keys(nested)
        elif isinstance(value, list):
            for nested in value:
                yield from keys(nested)

    assert FORBIDDEN_PUBLIC_FIXTURE_KEYS.isdisjoint(keys(fixture))
