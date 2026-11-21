"""Roads/Rail/Trade EvidenceBundle closure stays held until domain bundles exist.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): EvidenceBundle closure for domain claims.

No Roads/Rail/Trade EvidenceBundle has been emitted: data/proofs/roads-rail-trade/
holds only its README. Bundle shape is covered by
tests/validators/domains/roads-rail-trade/test_roads_rail_trade_evidence_bundle_schema_convergence.py.
The hold fails with EVIDENCE_BUNDLE_CLOSURE_NOT_IMPLEMENTED as soon as a bundle lands.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
LANE = "data/proofs/roads-rail-trade"


def _payloads(relative: str) -> list[str]:
    root = REPO_ROOT / relative
    assert root.is_dir(), f"{relative} moved; point this hold at the lane's new home."
    return sorted(p.relative_to(REPO_ROOT).as_posix() for p in root.rglob("*")
                  if p.is_file() and p.name not in {"README.md", ".gitkeep"})


def test_proof_lane_has_no_records_yet() -> None:
    assert _payloads(LANE) == [], (
        "EVIDENCE_BUNDLE_CLOSURE_NOT_IMPLEMENTED: records now exist in " + LANE + ". Replace this hold with closure tests for each bundle."
    )
