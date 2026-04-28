from __future__ import annotations

import json
from pathlib import Path

from tools.release.publish_release import build_publish_plan
from tools.resolvers.release import resolve_release_manifest as release_resolver

ROOT = Path(__file__).resolve().parents[3]

VALID_MANIFEST = ROOT / "tests/fixtures/release/valid/minimal.release-manifest.json"
INVALID_MANIFEST = ROOT / "tests/fixtures/release/invalid/missing_provenance_ref.release-manifest.json"


def _disable_external_validators(monkeypatch) -> None:
    for key in list(release_resolver.VALIDATORS):
        monkeypatch.setitem(release_resolver.VALIDATORS, key, ROOT / "_missing_validator.py")


def test_release_manifest_closure_publishable(monkeypatch) -> None:
    _disable_external_validators(monkeypatch)

    closure = release_resolver.resolve_release_manifest(VALID_MANIFEST)

    assert closure.status == "PUBLISHABLE"
    assert closure.failures == []


def test_release_manifest_missing_provenance_is_denied(monkeypatch) -> None:
    _disable_external_validators(monkeypatch)

    closure = release_resolver.resolve_release_manifest(INVALID_MANIFEST)

    assert closure.status == "DENY"
    assert any("missing reference" in failure for failure in closure.failures)


def test_publish_plan_is_built_from_publishable_closure(monkeypatch) -> None:
    _disable_external_validators(monkeypatch)

    manifest = json.loads(VALID_MANIFEST.read_text(encoding="utf-8"))
    closure = release_resolver.resolve_release_manifest(VALID_MANIFEST)

    assert closure.status == "PUBLISHABLE"

    plan = build_publish_plan(VALID_MANIFEST, manifest, {"status": closure.status})
    assert plan["closure_status"] == "PUBLISHABLE"
    assert plan["artifact_count"] == 1
    assert plan["release_id"] == manifest["release_id"]
