from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/sources/source_descriptor.schema.json"
DESCRIPTOR_PATH = (
    ROOT / "data/registry/sources/geology/kgs-m118-surficial-geology.source.json"
)


def _load() -> dict[str, object]:
    return json.loads(DESCRIPTOR_PATH.read_text(encoding="utf-8"))


def _expected_spec_hash(document: dict[str, object]) -> str:
    subject = copy.deepcopy(document)
    subject.pop("spec_hash", None)
    payload = json.dumps(
        subject,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def test_kgs_m118_descriptor_passes_shared_source_descriptor_schema() -> None:
    validator = load_validator(SCHEMA_PATH, check_formats=True)
    descriptor = _load()
    errors = sorted(validator.iter_errors(descriptor), key=lambda error: list(error.path))
    assert not errors, [error.message for error in errors]


def test_kgs_m118_descriptor_identity_is_content_derived() -> None:
    descriptor = _load()
    assert descriptor["spec_hash"] == _expected_spec_hash(descriptor)


def test_kgs_m118_is_scale_bound_interpreted_map_authority() -> None:
    descriptor = _load()
    joined = " ".join(
        [
            str(descriptor["description"]),
            str(descriptor["authority_notes"]),
            str(descriptor["admissibility_limits"]["limitations"]),
            str(descriptor["source_head"]["content_identity"]["upstream_version"]),
        ]
    ).lower()

    assert descriptor["source_id"] == "kfm://source/kgs/maps/m118-surficial-geology-of-kansas"
    assert descriptor["domain_scope"] == ["geology"]
    assert descriptor["source_type"] == "map_artifact"
    assert descriptor["source_role"] == "authoritative_for_claim"
    assert descriptor["authority_rank"] == "authoritative_for_role"
    assert "1:500,000" in joined
    assert "interpreted" in joined
    assert "point observation" in joined


def test_rights_conflict_keeps_descriptor_inactive_and_unreleased() -> None:
    descriptor = _load()

    assert descriptor["rights"]["rights_status"] == "unknown"
    assert descriptor["rights"]["redistribution_allowed"] == "unknown"
    assert descriptor["rights"]["commercial_use_allowed"] == "unknown"
    assert descriptor["public_release"]["allowed"] is False
    assert descriptor["public_release"]["requires_review"] is True
    assert descriptor["review_state"] == "needs_review"
    assert descriptor["release_state"] == "not_released"
    assert descriptor["lifecycle"]["registry_state"] == "proposed"


def test_connector_and_source_material_access_remain_disabled() -> None:
    descriptor = _load()
    connector = descriptor["connectors"]
    source_head = descriptor["source_head"]

    assert connector["activation_state"] == "disabled"
    assert "connector_ref" not in connector
    assert "watcher_ref" not in connector
    assert source_head["method"] == "manual_review"
    assert "content_sha256" not in source_head["content_identity"]
    assert "etag" not in source_head["content_identity"]


def test_m05_source_assessment_matrix_remains_fail_closed() -> None:
    descriptor = _load()
    rights = descriptor["rights"]
    cadence = descriptor["cadence"]
    admissibility = descriptor["admissibility_limits"]
    public_release = descriptor["public_release"]
    release_conditions = " ".join(public_release["release_conditions"]).lower()

    # Identity, authority role, terms, and cadence stay explicit and bounded to
    # the reviewed M-118 map artifact rather than a live source or point truth.
    assert descriptor["publisher"]["name"] == "Kansas Geological Survey"
    assert descriptor["owner_or_steward"]["name"] == "Kansas Geological Survey"
    assert descriptor["source_role"] == "authoritative_for_claim"
    assert rights["rights_status"] == "unknown"
    assert rights["license_url"].startswith("https://")
    assert rights["terms_url"].startswith("https://")
    assert cadence["update_cadence"] == "static"
    assert cadence["staleness_policy"] == "review_required"

    # Public-safety posture preserves the published map scale and prevents a
    # broadly public map from becoming authority for precise protected detail.
    assert descriptor["sensitivity_default"] == "public"
    assert "protected subsurface" in descriptor["sensitivity_notes"].lower()
    assert "scale-bound" in admissibility["limitations"]
    assert (
        "1:500,000"
        in descriptor["source_head"]["content_identity"]["upstream_version"]
    )
    assert public_release["redaction_required"] is False
    assert "scale" in release_conditions

    # Unknown rights, review, correction, and rollback remain prerequisites;
    # the source cannot become active or releasable through this descriptor.
    assert "rights" in release_conditions
    assert "review" in release_conditions
    assert "correction" in release_conditions
    assert "rollback" in release_conditions
    assert public_release["allowed"] is False
    assert descriptor["connectors"]["activation_state"] == "disabled"
    assert descriptor["review_state"] == "needs_review"
    assert descriptor["release_state"] == "not_released"


def test_only_official_kgs_https_endpoints_are_declared() -> None:
    descriptor = _load()
    endpoints = descriptor["access"]["endpoints"]
    allowed_hosts = {"kgs.ku.edu", "www.kgs.ku.edu"}

    assert endpoints
    for endpoint in endpoints:
        parsed = urlparse(endpoint["uri"])
        assert parsed.scheme == "https"
        assert parsed.hostname in allowed_hosts


def test_claim_roles_preserve_map_and_observation_boundaries() -> None:
    descriptor = _load()
    allowed = descriptor["admissibility_limits"]["allowed_claim_roles"]
    prohibited = descriptor["admissibility_limits"]["prohibited_claim_roles"]

    assert allowed == sorted(set(allowed))
    assert prohibited == sorted(set(prohibited))
    assert set(allowed).isdisjoint(prohibited)
    assert {"citation_support", "map_display"} <= set(allowed)
    assert {"observation", "not_for_life_safety", "not_for_title_truth"} <= set(prohibited)


def test_descriptor_contains_no_secret_or_source_payload() -> None:
    descriptor = _load()
    forbidden_keys = {
        "api_key",
        "credential",
        "password",
        "secret",
        "source_payload",
        "token",
    }
    keys: set[str] = set()

    def collect(value: object) -> None:
        if isinstance(value, dict):
            keys.update(str(key).lower() for key in value)
            for item in value.values():
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)

    collect(descriptor)
    assert forbidden_keys.isdisjoint(keys)
    assert descriptor["access"]["auth"]["auth_required"] is False
    assert descriptor["access"]["auth"]["auth_type"] == "none"
