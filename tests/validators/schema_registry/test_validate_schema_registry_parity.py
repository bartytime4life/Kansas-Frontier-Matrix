from __future__ import annotations

import json
import socket
import sys
from pathlib import Path

from referencing import Registry, Resource

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages" / "schema-registry" / "src"
sys.path.insert(0, str(PACKAGE_SRC))
sys.path.insert(0, str(REPO_ROOT))

from tools.validators.schema_registry import validate_schema_registry_parity as parity


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


def _repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    schemas = root / "schemas" / "contracts" / "v1"
    _write_schema(
        schemas / "a.schema.json",
        "https://schemas.kfm.local/contracts/v1/test/a.schema.json",
        title="A",
    )
    _write_schema(
        schemas / "z.schema.json",
        "https://schemas.kfm.local/contracts/v1/test/z.schema.json",
        title="Z",
    )
    _write_schema(schemas / "no-id.schema.json", None, title="No id")
    return root


def test_exact_registry_parity_passes(tmp_path: Path) -> None:
    report = parity.validate_parity(_repo(tmp_path))

    assert report.ok
    assert report.legacy_id_count == 2
    assert report.package_id_count == 2
    assert report.skipped_missing_id_count == 1
    assert report.findings == ()


def test_id_set_mismatch_is_visible(tmp_path: Path, monkeypatch) -> None:
    root = _repo(tmp_path)
    resource = Resource.from_contents(
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://schemas.kfm.local/contracts/v1/test/a.schema.json",
            "title": "A",
            "type": "object",
        }
    )
    reduced = Registry().with_resource(
        "https://schemas.kfm.local/contracts/v1/test/a.schema.json", resource
    )
    monkeypatch.setattr(parity, "build_legacy_registry", lambda _root: reduced)

    report = parity.validate_parity(root)

    assert not report.ok
    assert [finding.code for finding in report.findings] == [
        "ID_ONLY_IN_PACKAGE_REGISTRY"
    ]


def test_document_mismatch_is_visible(tmp_path: Path, monkeypatch) -> None:
    root = _repo(tmp_path)
    mismatched = Registry().with_resources(
        [
            (
                "https://schemas.kfm.local/contracts/v1/test/a.schema.json",
                Resource.from_contents(
                    {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "$id": "https://schemas.kfm.local/contracts/v1/test/a.schema.json",
                        "title": "Changed",
                        "type": "object",
                    }
                ),
            ),
            (
                "https://schemas.kfm.local/contracts/v1/test/z.schema.json",
                Resource.from_contents(
                    {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "$id": "https://schemas.kfm.local/contracts/v1/test/z.schema.json",
                        "title": "Z",
                        "type": "object",
                    }
                ),
            ),
        ]
    )
    monkeypatch.setattr(parity, "build_legacy_registry", lambda _root: mismatched)

    report = parity.validate_parity(root)

    assert not report.ok
    assert [finding.code for finding in report.findings] == [
        "REGISTRY_CONTENT_MISMATCH"
    ]


def test_legacy_build_error_is_bounded(tmp_path: Path, monkeypatch) -> None:
    root = _repo(tmp_path)

    def fail(_root: Path):
        raise ValueError("untrusted details are not emitted")

    monkeypatch.setattr(parity, "build_legacy_registry", fail)
    report = parity.validate_parity(root)

    assert not report.ok
    assert report.findings[0].code == "LEGACY_REGISTRY_ERROR"
    assert "untrusted details" not in report.findings[0].detail


def test_validator_uses_no_network(tmp_path: Path, monkeypatch) -> None:
    def deny_network(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("network access is forbidden")

    monkeypatch.setattr(socket, "create_connection", deny_network)
    report = parity.validate_parity(_repo(tmp_path))
    assert report.ok


def test_cli_output_is_deterministic(tmp_path: Path, capsys) -> None:
    root = _repo(tmp_path)
    assert parity.main(["--repo-root", str(root)]) == 0
    first = capsys.readouterr().out
    assert parity.main(["--repo-root", str(root)]) == 0
    second = capsys.readouterr().out

    assert first == second
    payload = json.loads(first)
    assert payload["outcome"] == "PASS"
    assert payload["authority"] == "validation_only"
