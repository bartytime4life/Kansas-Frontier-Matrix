"""Non-vacuous no-network smoke proof for the accepted CorridorRoute slice."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = (
    ROOT / "tools/validators/domains/roads-rail-trade/validate_corridor_route.py"
)
FIXTURES_ROOT = ROOT / "fixtures/domains/roads-rail-trade/corridor_route"


def _load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "roads_rail_trade_corridor_route_validator", VALIDATOR_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_corridor_route_smoke_proves_pass_abstain_and_deny_without_network():
    module = _load_validator_module()
    cases = (
        ("valid/valid_historic_candidate.json", "PASS"),
        ("valid/valid_unresolved_evidence.json", "ABSTAIN"),
        ("invalid/invalid_live_routing_authority.json", "DENY"),
    )

    for relative_path, expected_outcome in cases:
        path = FIXTURES_ROOT / relative_path
        document = module.load_object(path)
        fixture_meta = document["_fixture_meta"]
        assert fixture_meta["network_status"] == "no_network_required"
        assert fixture_meta["sensitive_data"] is False
        assert fixture_meta["synthetic"] is True
        assert module.validate_file(path) == expected_outcome
