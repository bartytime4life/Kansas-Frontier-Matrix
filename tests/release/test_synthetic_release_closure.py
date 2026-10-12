"""Bounded synthetic closure checks for #3371 and #4415.

The fixture is intentionally not a release candidate.  It only proves that the
existing no-network promotion-verification packet keeps catalog provenance,
rollback, and readiness-decision evidence bound to one synthetic artifact.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.release.release_dry_run import build_report

ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = ROOT / "fixtures/release/promotion_verification_execution"


def load(relative_path: str) -> dict[str, object]:
    value = json.loads((FIXTURE_ROOT / relative_path).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_synthetic_catalog_and_rollback_references_share_the_manifest_identity() -> None:
    """Keep STAC, DCAT, PROV, evidence, and rollback on one synthetic subject."""

    packet = load("valid/pass.json")
    manifest = load("artifacts/release_manifest.json")
    expected_spec_hash = manifest["spec_hash"]
    expected_artifact_digests = manifest["artifact_digests"]
    carrier_binding = packet["carrier"]
    assert isinstance(carrier_binding, dict)
    carrier_path = ROOT / carrier_binding["path"]
    carrier_digest = "sha256:" + hashlib.sha256(carrier_path.read_bytes()).hexdigest()
    assert carrier_binding["sha256"] == carrier_digest
    assert carrier_digest in expected_artifact_digests

    references = packet["references"]
    assert isinstance(references, list)
    assert {entry["kind"] for entry in references if isinstance(entry, dict)} == {
        "EVIDENCE_BUNDLE",
        "STAC",
        "DCAT",
        "PROV",
        "ROLLBACK",
    }

    for entry in references:
        assert isinstance(entry, dict)
        reference = load(entry["path"].removeprefix("fixtures/release/promotion_verification_execution/"))
        assert reference["kind"] == entry["kind"]
        assert reference["ref_id"] == entry["ref_id"]
        assert reference["subject_spec_hash"] == expected_spec_hash
        assert reference["artifact_digest"] in expected_artifact_digests


def test_production_readiness_dry_run_remains_non_authorizing() -> None:
    """A complete synthetic packet cannot create a production transition."""

    packet = load("valid/pass.json")
    governance = packet["governance"]
    assert isinstance(governance, dict)
    assert governance == {
        "fixture_only": True,
        "network_access": "DENIED",
        "lifecycle_write": False,
        "promotion_authorized": False,
        "release_authorized": False,
        "deployment_authorized": False,
        "publication_authorized": False,
    }

    report = build_report()
    assert report["dry_run_status"] == "PASS"
    assert report["authority_created"] is False
    assert report["decision_created"] is False
    assert report["release_candidate_assembled"] is False
    assert report["publication_created"] is False
