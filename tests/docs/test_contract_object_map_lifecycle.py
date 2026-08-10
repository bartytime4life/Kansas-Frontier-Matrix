from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/docs/validate_contract_object_map_lifecycle.py"
MAP_PATH = REPO_ROOT / "contracts/OBJECT_MAP.md"

SPEC = importlib.util.spec_from_file_location("contract_object_map_lifecycle_validator", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def _write_mutation(tmp_path: Path, old: str, new: str) -> Path:
    candidate = tmp_path / "OBJECT_MAP.md"
    text = MAP_PATH.read_text(encoding="utf-8")
    assert old in text
    candidate.write_text(text.replace(old, new, 1), encoding="utf-8")
    return candidate


def _codes(result: object) -> set[str]:
    return {finding.code for finding in result.findings}


def test_current_map_passes_bounded_profile() -> None:
    result = validator.validate_object_map()
    assert result.ok, result.findings


def test_required_resource_tokens_are_declared() -> None:
    text = MAP_PATH.read_text(encoding="utf-8")
    section, findings = validator._bounded_section(text)
    assert not findings and section is not None
    assert all(f"`{resource}`" in section for resource in validator.REQUIRED_RESOURCES)


def test_missing_referenced_path_fails_closed(tmp_path: Path) -> None:
    candidate = _write_mutation(
        tmp_path,
        "`SourceDescriptor` | `contracts/source/source_descriptor.md` ·",
        "`SourceDescriptor` | `contracts/source/source_descriptor_missing.md` ·",
    )
    result = validator.validate_object_map(candidate)
    assert "PATH_NOT_FOUND" in _codes(result)


def test_route_table_drift_fails_closed(tmp_path: Path) -> None:
    candidate = _write_mutation(tmp_path, "| `/layers` |", "| `/layerz` |")
    result = validator.validate_object_map(candidate)
    assert "ROUTE_INVENTORY_MISMATCH" in _codes(result)


def test_missing_overlay_marker_fails_closed(tmp_path: Path) -> None:
    candidate = _write_mutation(tmp_path, validator.START_MARKER, "")
    result = validator.validate_object_map(candidate)
    assert _codes(result) == {"SECTION_MARKER_INVALID"}


def test_non_abstaining_registered_handler_fails_closed() -> None:
    routes, findings = validator._load_routes(REPO_ROOT)
    assert not findings and routes is not None
    mutated = dict(routes)
    mutated["/layers"] = lambda: {"decision": "GRANT", "outcome": "GRANT"}
    result = validator.validate_object_map(routes=mutated)
    assert "ROUTE_NOT_ABSTAIN" in _codes(result)


def test_cli_output_is_deterministic() -> None:
    command = [sys.executable, str(VALIDATOR_PATH), str(MAP_PATH), "--repo-root", str(REPO_ROOT)]
    environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"}
    first = subprocess.run(command, check=True, capture_output=True, text=True, env=environment)
    second = subprocess.run(command, check=True, capture_output=True, text=True, env=environment)
    assert first.stdout == second.stdout
    assert '"outcome":"PASS"' in first.stdout


def test_validator_has_no_network_or_process_client_imports() -> None:
    source = VALIDATOR_PATH.read_text(encoding="utf-8")
    forbidden = (
        "import requests",
        "from requests",
        "import urllib",
        "from urllib",
        "import socket",
        "from socket",
        "import subprocess",
        "from subprocess",
    )
    assert not any(marker in source for marker in forbidden)
