"""Bounded synthetic closure checks for #3371 and #4415.

The fixture is intentionally not a release candidate.  It only proves that the
existing no-network promotion-verification packet keeps catalog provenance,
rollback, and readiness-decision evidence bound to one synthetic artifact.
"""
from __future__ import annotations

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
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-release-readme
title: tests/release/ — Release-Prerequisite Test Inventory and Authority Boundary
type: readme; directory-readme; release-test-boundary; executable-inventory
version: v1.2
status: repository-grounded; executable; mixed-dependency; no-release-authority
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent QA, release, and separation-of-duties stewardship remain NEEDS VERIFICATION"
created: 2026-07-06
updated: 2026-08-30
supersedes: v1.1 documentation at the same path; no test, fixture, validator, workflow, release object, or public surface is superseded
policy_label: public-doc; tests; release-prerequisites; promotion-safety; synthetic; fail-closed; non-authoritative
current_path: tests/release/README.md
truth_posture: CONFIRMED fifteen direct modules and 123 source-defined tests at the pinned snapshot / PARTIAL aggregate local execution and cross-family coverage / UNKNOWN required-check status, complete collection count, and independent stewardship
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  target_prior_blob: 8e4e14eb35dcd2026b7bf0de37ec9751f75a710d
  direct_modules: 15
  source_defined_tests: 123
  count_note: source-defined test functions or methods; parametrization and collection behavior may change collected-case totals
related:
  - ../README.md
  - ../../release/README.md
  - ../../contracts/release/README.md
  - ../../schemas/contracts/v1/release/README.md
  - ../../fixtures/release/README.md
  - ../../tools/release/README.md
  - ../../tools/validators/release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../Makefile
  - ../../pyproject.toml
tags: [kfm, tests, release, promotion, rollback, publication-deny, compatibility, no-network, fail-closed]
notes:
  - "v1.2 replaces a stale three-module thin-slice inventory and proposed future tree with the complete direct current-main inventory."
  - "Every direct module has a workflow binding, but the workflows use different dependency sets and commands; no single canonical full-lane target is established."
  - "Passing tests and workflows are bounded evidence only and never approve review, promotion, release, deployment, publication, correction, withdrawal, or rollback."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
