from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import yaml
import pytest

from tools.validators.directory_governance.validate_repository_topology_correction_register import (
    DEFAULT_REGISTER,
    DEFAULT_SCHEMA,
    main,
    validate,
)


def _load() -> dict:
    return yaml.safe_load(DEFAULT_REGISTER.read_text(encoding="utf-8"))


def _write(tmp_path: Path, value: dict) -> Path:
    path = tmp_path / "register.yaml"
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
    return path


def test_repository_register_passes_shape_validation() -> None:
    assert validate() == []


def test_cli_passes_for_repository_register(capsys) -> None:
    assert main([]) == 0
    assert capsys.readouterr().out.splitlines()[0] == "PASS"


def test_proposed_entry_must_remain_inert(tmp_path: Path) -> None:
    value = _load()
    entry = value["entries"][0]
    assert entry["status"] == "proposed"
    assert entry["decision_ref"]["blob"] is None
    assert entry["decision_ref"]["accepted_commit"] is None
    assert validate(_write(tmp_path, value), DEFAULT_SCHEMA) == []


def test_accepted_entry_requires_bound_decision(tmp_path: Path) -> None:
    value = _load()
    value["entries"][0]["status"] = "accepted"
    errors = validate(_write(tmp_path, value), DEFAULT_SCHEMA)
    assert any(error.startswith("schema:entries.0.decision_ref.blob:") for error in errors)
    assert any(error.startswith("schema:entries.0.decision_ref.accepted_commit:") for error in errors)


def test_wrong_target_blob_fails_schema(tmp_path: Path) -> None:
    value = _load()
    value["entries"][0]["to"]["blob"] = "not-a-git-blob"
    errors = validate(_write(tmp_path, value), DEFAULT_SCHEMA)
    assert any("blob" in error for error in errors)


def test_cardinality_change_fails_internal_invariant(tmp_path: Path) -> None:
    value = _load()
    value["entries"][0]["to"]["member_count"] = 44
    errors = validate(_write(tmp_path, value), DEFAULT_SCHEMA)
    assert any("equal member counts" in error for error in errors)


def test_second_changed_member_fails_schema(tmp_path: Path) -> None:
    value = _load()
    value["entries"][0]["exact_delta"]["added"].append(
        "catalog/domain/example/README.md@1111111111111111111111111111111111111111"
    )
    errors = validate(_write(tmp_path, value), DEFAULT_SCHEMA)
    assert any("added" in error for error in errors)


def test_duplicate_correction_id_fails(tmp_path: Path) -> None:
    value = _load()
    value["entries"].append(deepcopy(value["entries"][0]))
    errors = validate(_write(tmp_path, value), DEFAULT_SCHEMA)
    assert any("duplicate correction_id" in error for error in errors)


def test_schema_is_valid_draft_2020_12_json() -> None:
    schema = json.loads(DEFAULT_SCHEMA.read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"


@pytest.mark.parametrize("invalid_entries", [None, 1, "entry", {}, [None], [False]])
def test_malformed_entries_fail_without_raising(tmp_path: Path, capsys, invalid_entries) -> None:
    value = _load()
    value["entries"] = invalid_entries
    path = _write(tmp_path, value)
    errors = validate(path)
    assert errors
    assert errors == sorted(set(errors))
    assert main(["--register", str(path)]) == 1
    assert capsys.readouterr().out.splitlines()[0] == "FAIL_INVALID"


@pytest.mark.parametrize("invalid_id", [[], {}, ["unhashable"]])
def test_malformed_correction_id_fails_without_raising(tmp_path: Path, invalid_id) -> None:
    value = _load()
    value["entries"][0]["correction_id"] = invalid_id
    assert validate(_write(tmp_path, value))


@pytest.mark.parametrize("state", ["from", "to", "exact_delta", "decision_ref"])
def test_malformed_transition_objects_fail_without_raising(tmp_path: Path, state: str) -> None:
    value = _load()
    value["entries"][0][state] = None
    assert validate(_write(tmp_path, value))


@pytest.mark.parametrize("member,state", [("removed", "from"), ("added", "to")])
@pytest.mark.parametrize("mismatch", ["path", "blob"])
def test_exact_delta_must_bind_declared_transition(
    tmp_path: Path, member: str, state: str, mismatch: str,
) -> None:
    value = _load()
    entry = value["entries"][0]
    path = "catalog/domain/unrelated/README.md" if mismatch == "path" else entry["path"]
    blob = "1" * 40 if mismatch == "blob" else entry[state]["blob"]
    entry["exact_delta"][member] = [f"{path}@{blob}"]
    errors = validate(_write(tmp_path, value))
    assert f"entry[0]:{member} member must bind path and {state}.blob" in errors


@pytest.mark.parametrize("field", ["blob", "fingerprint"])
def test_noop_transition_is_not_a_replacement(tmp_path: Path, field: str) -> None:
    value = _load()
    entry = value["entries"][0]
    entry["to"][field] = entry["from"][field]
    if field == "blob":
        entry["exact_delta"]["added"] = entry["exact_delta"]["removed"][:]
    errors = validate(_write(tmp_path, value))
    assert f"entry[0]:correction requires distinct source and target {field}s" in errors


def test_consistent_synthetic_transition_is_only_shape_evidence(tmp_path: Path) -> None:
    value = _load()
    entry = value["entries"][0]
    entry["path"] = "catalog/domain/synthetic/README.md"
    entry["from"]["blob"] = "1" * 40
    entry["to"]["blob"] = "2" * 40
    entry["exact_delta"]["removed"] = [f"{entry['path']}@{entry['from']['blob']}"]
    entry["exact_delta"]["added"] = [f"{entry['path']}@{entry['to']['blob']}"]
    assert validate(_write(tmp_path, value)) == []
    assert entry["status"] == "proposed"
    assert entry["decision_ref"]["blob"] is None
    assert entry["decision_ref"]["accepted_commit"] is None
