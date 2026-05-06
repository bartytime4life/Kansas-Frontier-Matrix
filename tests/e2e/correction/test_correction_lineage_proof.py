from __future__ import annotations

from pathlib import Path

from tools.resolvers.release import resolve_release_manifest as release_resolver

ROOT = Path(__file__).resolve().parents[3]

UNRESOLVED_MANIFEST = ROOT / "tests/fixtures/release/invalid/unresolved_artifact.release-manifest.json"


def _disable_external_validators(monkeypatch) -> None:
    for key in list(release_resolver.VALIDATORS):
        monkeypatch.setitem(release_resolver.VALIDATORS, key, ROOT / "_missing_validator.py")


def test_unresolved_release_artifact_is_visible_and_fail_closed(monkeypatch) -> None:
    _disable_external_validators(monkeypatch)

    closure = release_resolver.resolve_release_manifest(UNRESOLVED_MANIFEST)

    assert closure.status == "DENY"
    assert any("path does not exist" in failure for failure in closure.failures)
    assert any("artifacts[0].artifact_ref" in failure for failure in closure.failures)
