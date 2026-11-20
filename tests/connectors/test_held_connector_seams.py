"""Held connector seams refuse retrieval and admission without side effects.

Eight connectors have no admitted source: each ``descriptor.yaml`` still leaves
``role`` and ``rights`` as ``TBD``. Their ``fetch.py`` (and, where present,
``admit.py``) modules are fail-closed seams. These tests prove the seams import
inertly, raise their named hold for any call, and import no network or
filesystem machinery. They also fail if a descriptor is resolved, so admitting a
source has to replace the hold deliberately rather than leave it in place.
"""
from __future__ import annotations

import ast
import importlib.util
import socket
from pathlib import Path
from types import ModuleType

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
HELD_CONNECTORS = {
    "ahgp": ("fetch", "admit"),
    "familysearch": ("fetch",),
    "kansas_state_archives": ("fetch", "admit"),
    "kdwp": ("fetch", "admit"),
    "khri": ("fetch", "admit"),
    "ksgs": ("fetch", "admit"),
    "ksu_research_extension": ("fetch", "admit"),
    "loc": ("fetch", "admit"),
}
SEAMS = {
    "fetch": ("retrieve", "ConnectorFetchHold", "CONNECTOR_FETCH_NOT_ADMITTED"),
    "admit": ("admit", "ConnectorAdmissionHold", "CONNECTOR_ADMISSION_NOT_ADMITTED"),
}
CASES = sorted((connector, seam) for connector, seams in HELD_CONNECTORS.items() for seam in seams)
FORBIDDEN_IMPORTS = {"socket", "urllib", "http", "requests", "httpx", "ssl", "subprocess",
                     "os", "shutil", "pathlib", "io", "tempfile", "connectors_core"}


def _source(connector: str, seam: str) -> Path:
    return REPO_ROOT / "connectors" / connector / "src" / connector / f"{seam}.py"


def _load(connector: str, seam: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        f"held_connector_{connector}_{seam}", _source(connector, seam)
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def no_sockets(monkeypatch: pytest.MonkeyPatch) -> None:
    def refuse(*args: object, **kwargs: object) -> None:
        raise AssertionError("a held connector seam attempted network access")

    monkeypatch.setattr(socket, "socket", refuse)
    monkeypatch.setattr(socket, "create_connection", refuse)
    monkeypatch.setattr(socket, "getaddrinfo", refuse)


@pytest.mark.parametrize(("connector", "seam"), CASES)
def test_seam_raises_its_named_hold_for_any_call(connector: str, seam: str,
                                                 no_sockets: None) -> None:
    module = _load(connector, seam)
    function_name, hold_name, reason_code = SEAMS[seam]
    hold = getattr(module, hold_name)

    assert module.CONNECTOR == connector
    assert module.HOLD_REASON_CODE == reason_code
    for args, kwargs in (((), {}), (("https://example.invalid/",), {"timeout": 1})):
        with pytest.raises(hold) as raised:
            getattr(module, function_name)(*args, **kwargs)
        assert raised.value.reason_code == reason_code
        assert raised.value.connector == connector
        assert str(raised.value).startswith(f"{reason_code}: the {connector} connector")


@pytest.mark.parametrize(("connector", "seam"), CASES)
def test_seam_imports_no_network_or_filesystem_machinery(connector: str, seam: str) -> None:
    tree = ast.parse(_source(connector, seam).read_text(encoding="utf-8"))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    assert imported <= {"__future__"}, sorted(imported & FORBIDDEN_IMPORTS) or sorted(imported)


@pytest.mark.parametrize("connector", sorted(HELD_CONNECTORS))
def test_hold_matches_an_unresolved_descriptor(connector: str) -> None:
    descriptor = REPO_ROOT / "connectors" / connector / "src" / connector / "descriptor.yaml"
    fields = dict(
        line.split(":", 1) for line in descriptor.read_text(encoding="utf-8").splitlines()
        if ":" in line and not line.lstrip().startswith("#")
    )
    assert fields["name"].strip() == connector
    assert fields["role"].strip() == "TBD", (
        f"{connector} descriptor role is resolved; replace the held seams with a reviewed "
        "connector instead of keeping the hold"
    )
    assert fields["rights"].strip() == "TBD", (
        f"{connector} descriptor rights are resolved; replace the held seams with a reviewed "
        "connector instead of keeping the hold"
    )


def test_every_held_seam_is_listed() -> None:
    held = set()
    for path in (REPO_ROOT / "connectors").glob("*/src/*/*.py"):
        if path.stem in SEAMS and "_NOT_ADMITTED" in path.read_text(encoding="utf-8"):
            held.add((path.parent.name, path.stem))
    assert held == set(CASES)
