"""Roads/Rail/Trade ReleaseManifest presence stays held until a release candidate exists.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): ReleaseManifest presence on published artifacts.

release/candidates/roads-rail-trade/ holds only its README, so there is no
artifact that needs a manifest. The hold fails with RELEASE_MANIFEST_NOT_IMPLEMENTED
as soon as a candidate lands.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
LANE = "release/candidates/roads-rail-trade"


def _payloads(relative: str) -> list[str]:
    root = REPO_ROOT / relative
    assert root.is_dir(), f"{relative} moved; point this hold at the lane's new home."
    return sorted(p.relative_to(REPO_ROOT).as_posix() for p in root.rglob("*")
                  if p.is_file() and p.name not in {"README.md", ".gitkeep"})


def test_release_candidate_lane_has_no_records_yet() -> None:
    assert _payloads(LANE) == [], (
        "RELEASE_MANIFEST_NOT_IMPLEMENTED: records now exist in " + LANE + ". Replace this hold with ReleaseManifest presence tests."
    )
