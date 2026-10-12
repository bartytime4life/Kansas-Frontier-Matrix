"""The Explorer Site and the Python release projection read the same water fixtures.

tools/fixtures/regenerate.py proves the Python projection reproduces the
reviewed fixtures, and the Site's tests/governed-water.test.mjs proves the Site
projection reproduces its copy. Byte parity between the two copies is what
makes those separate proofs one contract; it grants no release or hosted parity.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROFILE = ROOT / "control_plane/readiness/fixture-regeneration-manifest.json"
SITE_FIXTURES = ROOT / "apps/site/source/tests/fixtures/governed-water"


def test_site_water_fixtures_match_reviewed_release_fixtures():
    profile = json.loads(PROFILE.read_text())
    reviewed = ROOT / profile["reviewed_root"]
    names = sorted(profile["outputs"])
    assert sorted(path.name for path in SITE_FIXTURES.iterdir()) == names
    drift = [name for name in names if (SITE_FIXTURES / name).read_bytes() != (reviewed / name).read_bytes()]
    assert drift == [], f"Site water fixtures differ from {profile['reviewed_root']}: {drift}"
