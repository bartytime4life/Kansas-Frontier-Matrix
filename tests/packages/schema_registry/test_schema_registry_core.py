from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages" / "schema-registry" / "src"
sys.path.insert(0, str(PACKAGE_SRC))

from schema_registry import (  # noqa: E402
    LookupOutcome,
    RegistryErrorCode,
    SchemaRegistryError,
    build_registry_snapshot,
)

FIXTURES = REPO_ROOT / "fixtures" / "packages" / "schema-registry"


def _write_schema(path: Path, schema_id: str | None, *, title: str) -> None:
    value: dict[str, object] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": title,
        "type": "object",
    }
    if schema_id is not None:
        value["$id"] = schema_id
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def test_fixture_snapshot_is_deterministic_and_visible() -> None:
    first = build_registry_snapshot(FIXTURES / "valid")
    second = build_registry_snapshot(FIXTURES / "valid")

    assert first == second
    assert first.schema_ids == (
        "https://schemas.kfm.local/contracts/v1/test/alpha.schema.json",
        "https://schemas.kfm.local/contracts/v1/test/beta.schema.json",
    )
    assert [item.reason for item in first.skipped] == ["MISSING_ID"]
    assert first.snapshot_sha256.startswith("sha256:")
    assert first.as_dict()["authority"] == "helper_only"


def test_snapshot_digest_is_independent_of_creation_order(tmp_path: Path) -> None:
    left = tmp_path / "left"
    right = tmp_path / "right"
    ids = (
        "https://schemas.kfm.local/contracts/v1/test/a.schema.json",
        "https://schemas.kfm.local/contracts/v1/test/z.schema.json",
    )
    _write_schema(left / "z.schema.json", ids[1], title="Z")
    _write_schema(left / "a.schema.json", ids[0], title="A")
    _write_schema(right / "a.schema.json", ids[0], title="A")
    _write_schema(right / "z.schema.json", ids[1], title="Z")

    assert (
        build_registry_snapshot(left).snapshot_sha256
        == build_registry_snapshot(right).snapshot_sha256
    )


def test_lookup_and_referencing_registry_resolve_local_document() -> None:
    snapshot = build_registry_snapshot(FIXTURES / "valid")
    schema_id = "https://schemas.kfm.local/contracts/v1/test/alpha.schema.json"

    result = snapshot.lookup(schema_id)
    assert result.outcome is LookupOutcome.RESOLVED
    assert result.record is not None
    assert result.record.document()["title"] == "Alpha"
    assert snapshot.lookup("https://schemas.kfm.local/missing").outcome is LookupOutcome.UNRESOLVED
    assert snapshot.to_referencing_registry().contents(schema_id)["title"] == "Alpha"


def test_duplicate_id_fails_closed() -> None:
    with pytest.raises(SchemaRegistryError) as caught:
        build_registry_snapshot(FIXTURES / "duplicate")
    assert caught.value.code is RegistryErrorCode.DUPLICATE_ID
    assert caught.value.path == "two.schema.json"


def test_duplicate_json_key_fails_closed() -> None:
    with pytest.raises(SchemaRegistryError) as caught:
        build_registry_snapshot(FIXTURES / "invalid")
    assert caught.value.code is RegistryErrorCode.JSON_DUPLICATE_KEY


def test_missing_root_has_stable_outcome(tmp_path: Path) -> None:
    with pytest.raises(SchemaRegistryError) as caught:
        build_registry_snapshot(tmp_path / "missing")
    assert caught.value.code is RegistryErrorCode.ROOT_NOT_FOUND


def test_file_limit_is_enforced(tmp_path: Path) -> None:
    path = tmp_path / "large.schema.json"
    _write_schema(path, "https://schemas.kfm.local/large", title="Large")
    with pytest.raises(SchemaRegistryError) as caught:
        build_registry_snapshot(tmp_path, max_schema_bytes=8)
    assert caught.value.code is RegistryErrorCode.FILE_TOO_LARGE


def test_symlink_is_denied(tmp_path: Path) -> None:
    target = tmp_path / "outside.schema.json"
    _write_schema(target, "https://schemas.kfm.local/outside", title="Outside")
    root = tmp_path / "root"
    root.mkdir()
    link = root / "linked.schema.json"
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks are unavailable on this platform")

    with pytest.raises(SchemaRegistryError) as caught:
        build_registry_snapshot(root)
    assert caught.value.code is RegistryErrorCode.SYMLINK_DENIED


def test_cli_is_deterministic_and_uses_no_network(monkeypatch: pytest.MonkeyPatch) -> None:
    def deny_network(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("network access is forbidden")

    monkeypatch.setattr(socket, "create_connection", deny_network)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PACKAGE_SRC)
    command = [
        sys.executable,
        "-m",
        "schema_registry.cli",
        str(FIXTURES / "valid"),
    ]
    first = subprocess.run(command, check=False, capture_output=True, text=True, env=env)
    second = subprocess.run(command, check=False, capture_output=True, text=True, env=env)

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert first.stdout == second.stdout
    payload = json.loads(first.stdout)
    assert payload["outcome"] == "RESOLVED"
    assert payload["snapshot"]["record_count"] == 2
    assert payload["snapshot"]["skipped_count"] == 1
