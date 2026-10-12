"""Deterministic tests for fail-closed connector descriptor reading."""
from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "packages/connectors-core/src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from connectors_core.descriptor_gate import (  # noqa: E402
    MAX_BYTES,
    descriptor_blockers,
    load_descriptor,
    sensitivity_floor_blockers,
)


@pytest.mark.parametrize("text,keys", [
    ("# header\nname: usgs\nrole: a\nrights: b\n", ("name", "role", "rights")),
    ("name: usgs\nrole: a\nrole: b\n", ()),
    ("name: usgs\nnested:\n  key: v\n", ()),
    ("name: usgs\n  role: a\n", ()),
    ("name: usgs\nunknown: x\n", ()),
    ("name usgs\n", ()),
])
def test_load_is_strict(tmp_path, text, keys):
    path = tmp_path / "descriptor.yaml"
    path.write_text(text, encoding="utf-8")
    assert tuple(load_descriptor(path)) == keys


def test_unreadable_oversized_and_undecodable_are_empty(tmp_path):
    assert load_descriptor(tmp_path / "missing.yaml") == {}
    big = tmp_path / "big.yaml"
    big.write_bytes(b"name: usgs\n" + b"# pad\n" * MAX_BYTES)
    assert load_descriptor(big) == {}
    bad = tmp_path / "bad.yaml"
    bad.write_bytes(b"name: \xff\n")
    assert load_descriptor(bad) == {}


@pytest.mark.parametrize("value", ["TBD", "NEEDS VERIFICATION", "needs-verification",
                                   "Needs_Verification", " TBD ", "'TBD'", "_TBD_",
                                   "PROPOSED", "OWNER_TBD", "unknown", ""])
def test_documented_unresolved_spellings_block(value):
    assert descriptor_blockers({"name": "x", "role": value, "rights": value}, name="x") == (
        "DESCRIPTOR_ROLE_UNRESOLVED", "DESCRIPTOR_RIGHTS_UNRESOLVED")


def test_resolved_and_invalid_descriptors():
    assert descriptor_blockers({"name": "x", "role": "needs verification by steward",
                                "rights": "public-domain"}, name="x") == ()
    assert descriptor_blockers({"name": "x", "role": "a", "rights": "TBD"}, name="x") == (
        "DESCRIPTOR_RIGHTS_UNRESOLVED",)
    assert descriptor_blockers({"name": "y", "role": "a", "rights": "b"}, name="x") == (
        "DESCRIPTOR_INVALID",)
    assert descriptor_blockers({}, name="x") == ("DESCRIPTOR_INVALID",)
    assert descriptor_blockers("name: x", name="x") == ("DESCRIPTOR_INVALID",)


# Connectors whose role/rights the repository owner resolved (2026-09-28: U.S. federal
# works). Adding a connector here is a steward decision and must be deliberate.
OPENED_CONNECTORS = (
    "connectors/blm/src/blm/descriptor.yaml",
    "connectors/census/src/census/descriptor.yaml",
    "connectors/epa/src/epa/descriptor.yaml",
    "connectors/fema/src/fema/descriptor.yaml",
    "connectors/noaa/src/noaa/descriptor.yaml",
    "connectors/nrcs/src/nrcs/descriptor.yaml",
    "connectors/usgs/src/usgs/descriptor.yaml",
)


def test_only_deliberately_resolved_connector_descriptors_open_routes():
    # Guard: a descriptor edit that resolves role/rights is a steward decision and must
    # be deliberate; this lists which connectors open a candidate route.
    opened = []
    for path in sorted(ROOT.glob("connectors/*/src/*/descriptor.yaml")):
        descriptor = load_descriptor(path)
        name = descriptor.get("name", "")
        if not descriptor_blockers(descriptor, name=name):
            opened.append(str(path.relative_to(ROOT)))
    assert tuple(opened) == OPENED_CONNECTORS


@pytest.mark.parametrize("floor", ["generalized", "Restricted", "QUARANTINE", " restricted "])
def test_reviewed_non_public_floors_pass(floor):
    assert sensitivity_floor_blockers({"sensitivity_floor": floor}) == ()


@pytest.mark.parametrize("floor", ["public", "PUBLIC", "TBD", "", "publc", "internal",
                                   "unknown", "needs verification", "restricted-ish"])
def test_other_floors_block(floor):
    assert sensitivity_floor_blockers({"sensitivity_floor": floor}) == (
        "DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED",)


def test_missing_or_malformed_descriptor_blocks():
    assert sensitivity_floor_blockers({}) == ("DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED",)
    assert sensitivity_floor_blockers("sensitivity_floor: restricted") == (
        "DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED",)
