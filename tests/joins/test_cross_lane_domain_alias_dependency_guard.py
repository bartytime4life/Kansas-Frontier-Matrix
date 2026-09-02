from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates_domain_alias_dependency_guard", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

AUTHORITY_ENVELOPE = (
    "version: v1\n"
    "registry: domain_lane_register\n"
    "authority: machine_projection_only\n"
)


def _rule_counts(decision: dict[str, object]) -> dict[str, int]:
    return {
        item["rule_code"]: item["failure_count"]
        for item in decision["rule_results"]
    }


def _base_candidate() -> dict[str, object]:
    return copy.deepcopy(MODULE.fixture_cases()[0][0])


def test_valid_alias_projection_keeps_unrelated_pair_candidate_eligible() -> None:
    candidate = _base_candidate()
    candidate["endpoints"]["left"]["domain"] = "geology"
    candidate["endpoints"]["right"]["domain"] = "hydrology"

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["reason_codes"] == ["JOIN_PREDICATE_SATISFIED"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 0
    assert not any(decision["effects"].values())


def test_missing_alias_projection_fails_closed_as_dependency_error(tmp_path: Path, monkeypatch) -> None:
    candidate = _base_candidate()
    missing = tmp_path / "domain_lane_register.yaml"
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", missing)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())


def test_symlinked_alias_projection_fails_closed_as_dependency_error(tmp_path: Path, monkeypatch) -> None:
    candidate = _base_candidate()
    target = tmp_path / "alternate_authority.yaml"
    target.write_text(
        AUTHORITY_ENVELOPE
        + "unresolved_aliases:\n  air: atmosphere\nentries:\n  - lane_id: atmosphere\n",
        encoding="utf-8",
    )
    projection = tmp_path / "domain_lane_register.yaml"
    projection.symlink_to(target)
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", projection)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())


def test_aliased_projection_fails_closed_like_canonical_validator(
    tmp_path: Path, monkeypatch
) -> None:
    candidate = _base_candidate()
    candidate["endpoints"]["left"]["domain"] = "geology"
    candidate["endpoints"]["right"]["domain"] = "hydrology"
    projection = tmp_path / "domain_lane_register.yaml"
    projection.write_text(
        AUTHORITY_ENVELOPE
        + "unresolved_aliases: &aliases\n  air: atmosphere\n"
        + "alias_copy: *aliases\n"
        + "entries:\n  - lane_id: atmosphere\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", projection)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())


def test_malformed_alias_projection_fails_closed_as_dependency_error(tmp_path: Path, monkeypatch) -> None:
    candidate = _base_candidate()
    malformed = tmp_path / "domain_lane_register.yaml"
    malformed.write_text(
        AUTHORITY_ENVELOPE + "unresolved_aliases: [air, atmosphere]\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", malformed)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())


def _assert_projection_fails_closed(
    candidate: dict[str, object],
    tmp_path: Path,
    monkeypatch,
    projection: str,
    *,
    include_authority_envelope: bool = True,
) -> None:
    ambiguous = tmp_path / "domain_lane_register.yaml"
    ambiguous.write_text(
        (AUTHORITY_ENVELOPE if include_authority_envelope else "") + projection,
        encoding="utf-8",
    )
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", ambiguous)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())


def test_duplicate_alias_projection_block_fails_closed(tmp_path: Path, monkeypatch) -> None:
    _assert_projection_fails_closed(
        _base_candidate(),
        tmp_path,
        monkeypatch,
        "unresolved_aliases:\n  air: atmosphere\nunresolved_aliases:\n  transport: roads-rail-trade\n",
    )


def test_duplicate_alias_name_fails_closed(tmp_path: Path, monkeypatch) -> None:
    _assert_projection_fails_closed(
        _base_candidate(),
        tmp_path,
        monkeypatch,
        "unresolved_aliases:\n  air: atmosphere\n  air: geology\n",
    )

def test_custom_valid_alias_projection_resolves_registered_target(tmp_path: Path) -> None:
    projection = tmp_path / "domain_lane_register.yaml"
    projection.write_text(
        AUTHORITY_ENVELOPE
        + "unresolved_aliases:\n  air: atmosphere\nentries:\n  - lane_id: atmosphere\n",
        encoding="utf-8",
    )

    assert MODULE._unresolved_domain_aliases(projection) == {"air": "atmosphere"}


def test_missing_authority_envelope_fails_closed(tmp_path: Path, monkeypatch) -> None:
    _assert_projection_fails_closed(
        _base_candidate(),
        tmp_path,
        monkeypatch,
        "unresolved_aliases:\n  air: atmosphere\nentries:\n  - lane_id: atmosphere\n",
        include_authority_envelope=False,
    )


def test_authority_overclaim_fails_closed(tmp_path: Path, monkeypatch) -> None:
    _assert_projection_fails_closed(
        _base_candidate(),
        tmp_path,
        monkeypatch,
        (
            "version: v1\n"
            "registry: domain_lane_register\n"
            "authority: domain_identity_authority\n"
            "unresolved_aliases:\n"
            "  air: atmosphere\n"
            "entries:\n"
            "  - lane_id: atmosphere\n"
        ),
        include_authority_envelope=False,
    )


def test_unknown_alias_target_fails_closed(tmp_path: Path, monkeypatch) -> None:
    _assert_projection_fails_closed(
        _base_candidate(),
        tmp_path,
        monkeypatch,
        "unresolved_aliases:\n  air: atmosphere\nentries:\n  - lane_id: climate\n",
    )


def test_chained_alias_target_fails_closed(tmp_path: Path, monkeypatch) -> None:
    _assert_projection_fails_closed(
        _base_candidate(),
        tmp_path,
        monkeypatch,
        (
            "unresolved_aliases:\n"
            "  air: atmosphere\n"
            "  atmosphere: climate\n"
            "entries:\n"
            "  - lane_id: atmosphere\n"
            "  - lane_id: climate\n"
        ),
    )
