from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import yaml

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
    assert any("accepted entry requires exact decision blob and accepted commit" in error or "is not valid" in error for error in errors)


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
