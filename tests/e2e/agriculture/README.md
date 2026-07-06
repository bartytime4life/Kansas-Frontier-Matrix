<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-e2e-agriculture-readme
title: Agriculture End-to-End Tests README
type: e2e-test-readme
version: v0.1
status: draft; empty-placeholder-replaced; agriculture-e2e-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Agriculture domain steward
  - OWNER_TBD - E2E test steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Governed API steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - Map/UI steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; e2e; agriculture; no-network-default; governed-api; aggregate-only; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, e2e, agriculture, governed-api, aggregate-only, catalog-closure, policy-deny, rollback, schema, ssurgo-lineage, soil-moisture, veg-index, EvidenceBundle, EvidenceRef, AggregationReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ../../domains/README.md
  - ../../domains/agriculture/README.md
  - ../../domains/agriculture/aggregate_only/README.md
  - ../../domains/agriculture/catalog_closure/README.md
  - ../../domains/agriculture/policy_deny/README.md
  - ../../domains/agriculture/rollback_drill/README.md
  - ../../domains/agriculture/schema/README.md
  - ../../domains/agriculture/soil_moisture/README.md
  - ../../domains/agriculture/ssurgo_lineage/README.md
  - ../../domains/agriculture/veg_index/README.md
  - ../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../docs/domains/agriculture/API_CONTRACTS.md
  - ../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../contracts/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../fixtures/domains/agriculture/
  - ../../../policy/domains/agriculture/
  - ../../../release/candidates/agriculture/
notes:
  - "This README replaces the empty placeholder content at tests/e2e/agriculture/README.md."
  - "Directory Rules place enforceability proof under tests/. This lane is an end-to-end test documentation lane; it is not source, contract, schema, policy, fixture, proof, receipt, release, public artifact, map, API, package, pipeline, or AI authority."
  - "The parent tests/e2e/README.md was observed as a greenfield stub during authoring. This child lane is self-contained until the e2e parent index is expanded."
  - "Agriculture domain tests already cover domain-level guardrails. This E2E lane should verify governed composition across released or synthetic envelopes, not duplicate them."
  - "Executable E2E tests, fixtures, service harness, CI jobs, public-surface invalidation, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture end-to-end tests

> End-to-end test-lane documentation for Agriculture public-safe flows. This lane should prove that Agriculture requests move through governed envelopes without bypassing evidence, policy, aggregation, release, correction, rollback, or no-network constraints.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: e2e" src="https://img.shields.io/badge/lane-e2e-purple">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-green">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: E2E not publication" src="https://img.shields.io/badge/boundary-e2e__not__publication-success">
</p>

**Path:** `tests/e2e/agriculture/README.md`  
**Status:** draft / empty placeholder replaced / E2E test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `e2e`  
**Domain segment:** `agriculture`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED `tests/e2e/README.md` exists as a greenfield stub; CONFIRMED `tests/domains/agriculture/README.md` documents domain test lanes and no-network obligations; CONFIRMED Agriculture runbook, lifecycle, and API docs describe no-network, aggregate-only, fail-closed, finite-outcome, release-gated behavior; NEEDS VERIFICATION for executable E2E tests, service harnesses, fixtures, CI coverage, pass rates, and public-surface invalidation.

---

## Purpose

`tests/e2e/agriculture/` is the Agriculture end-to-end test lane.

This lane should verify a complete governed Agriculture request path using safe local fixtures and mocked interfaces. It should test whether a public-safe Agriculture flow can traverse request envelope, source-role checks, schema/contract expectations, EvidenceRef resolution, AggregationReceipt requirements, policy decision, review state, release manifest, public API or map envelope, correction path, and rollback target without crossing the trust membrane.

A passing E2E test here should **not** mean that an Agriculture claim is true, a field condition is known, an operator or parcel fact is public, an aggregate cell is per-place truth, a map layer is published, a release is approved, or an AI answer is authoritative. It should mean only that the scoped end-to-end guardrail behaved as expected against bounded synthetic fixtures and local files.

[Back to top](#top)

---

## Placement Basis

Directory Rules classify `tests/` as the responsibility root for enforceability proof. The `tests/e2e/` lane is appropriate for composed system-path tests that span multiple responsibility roots through governed interfaces. It must not become a shadow implementation, source loader, release root, public artifact root, or domain authority.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Agriculture E2E tests | `tests/e2e/agriculture/` | This directory. |
| E2E parent index | `tests/e2e/README.md` | Confirmed greenfield stub; needs expansion. |
| Agriculture domain tests | `tests/domains/agriculture/` | Domain-level guardrail tests; upstream to this E2E lane. |
| Agriculture fixtures | `fixtures/domains/agriculture/` | Preferred fixture home; not duplicated here unless test-local and documented. |
| Semantic contracts | `contracts/domains/agriculture/` | Tested through expectations; not authored here. |
| Machine schemas | `schemas/contracts/v1/domains/agriculture/` and runtime/release schema homes | Tested through expectations; not authored here. |
| Policy authority | `policy/domains/agriculture/` or accepted policy roots | Referenced by tests; not defined here. |
| Evidence, receipts, proofs | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic or safe fixture refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic ReleaseManifest and rollback refs; not decided here. |
| Public API and map surfaces | Governed API, map, tile, and artifact roots | Exercised only through safe mocked or fixture envelopes. |

> [!IMPORTANT]
> E2E means governed composition across boundaries. It does not mean live-source fetching, direct RAW/WORK reads, direct canonical-store reads, release approval, public artifact writes, or unrestricted UI/API access.

---

## Invariant Under Test

> **Agriculture E2E tests prove governed public-safe flow; they do not publish or prove Agriculture truth.**

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Trust membrane boundary | Test flow does not read RAW, WORK, QUARANTINE, canonical stores, unpublished candidates, or direct model runtime outputs as public truth. | validation failure / `ERROR`. |
| Governed interface boundary | Flow uses mocked governed API/runtime envelopes or released fixture envelopes, not internal data shortcuts. | validation failure. |
| Aggregate-only boundary | Aggregate products remain aggregate and cannot become field, parcel, operator, or person-level truth. | `DENY` / `ABSTAIN`. |
| Aggregation receipt boundary | Public-safe aggregate outputs cite an AggregationReceipt where material. | promotion block / `ABSTAIN`. |
| Source-role boundary | Source roles remain fixed across schema, catalog, API, map, Focus Mode, and generated-answer carriers. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claims that depend on evidence require EvidenceRef-to-EvidenceBundle support or fail closed. | `ABSTAIN`. |
| Policy boundary | Field-level, operator-identifying, proprietary, rights-restricted, farm-specific, pesticide, crop-insurance, and sensitive joins fail closed. | `DENY` / `ABSTAIN`. |
| Cross-lane boundary | Soil, Hydrology, People/Land, Atmosphere, Habitat, Flora, Fauna, Geology, and Hazards authority is cited and not reauthored by Agriculture E2E tests. | validation failure. |
| Release boundary | E2E success does not become ReleaseManifest approval, publication, or cache activation. | promotion block. |
| Public-surface boundary | Map, tile, API, export, Focus Mode, and AI carriers return finite governed outcomes and do not overstate confidence. | `DENY` / `ABSTAIN` / `ERROR`. |
| Correction and rollback boundary | Corrections, withdrawals, invalidations, and rollback targets stay explicit and auditable. | validation failure. |
| No-network boundary | Default E2E tests do not call live USDA, NRCS, SSURGO/SDA, Mesonet, SCAN/AWDB, USCRN, SMAP, HLS, map, public API, release, graph, or AI services. | validation failure / `ERROR`. |

---

## Expected E2E Test Families

| Family | Purpose | Boundary |
|---|---|---|
| Public aggregate flow | Verify a public-safe aggregate Agriculture response with evidence, AggregationReceipt, policy decision, release posture, and finite outcome. | Aggregate is not per-field truth. |
| Field-level deny flow | Verify field, operator, parcel, proprietary yield, pesticide, crop-insurance, and private operation requests deny or abstain. | Sensitive detail fails closed. |
| Catalog-to-API flow | Verify catalog/release fixture envelopes can feed governed API-style responses without direct lifecycle reads. | Catalog presence is not publication. |
| Map/Focus Mode flow | Verify layer/feature/focus carriers only use release-safe envelopes and do not expose restricted details. | Public UI is release-gated. |
| Soil/crop context flow | Verify Soil context joins preserve Soil authority and do not make Agriculture owner of soil semantics. | Cross-lane authority stays separate. |
| Soil-moisture context flow | Verify station/satellite/moisture context preserves Soil/Hydrology/source-role boundaries. | Context is not field truth. |
| Vegetation-index flow | Verify vegetation index products remain modeled/contextual and do not become crop/yield truth. | Model output is not observation. |
| Correction and rollback flow | Verify correction, withdrawal, and rollback fixture refs invalidate dependent public carriers. | Rollback is not deletion. |
| Governed AI boundary flow | Verify generated summaries cite released evidence and abstain when evidence, policy, or release state is missing. | AI is not sovereign truth. |
| No-network flow | Verify E2E default execution is local and deterministic. | Integration tests require separate gates. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable inputs belong in this lane:

- synthetic Agriculture request envelopes and response envelopes with fake refs
- synthetic fixture refs from Agriculture domain fixtures, not copied production payloads
- synthetic SourceDescriptor, EvidenceRef, EvidenceBundle stub, AggregationReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs
- synthetic public-safe layer, feature, map, tile, API, Focus Mode, export, and AI citation envelopes
- synthetic cross-lane refs for Soil, Hydrology, Atmosphere, Habitat, Flora, Fauna, Geology, Hazards, and People/Land where authority separation is under test
- canary values that make source-role collapse, aggregate-to-field collapse, person/parcel leakage, operator leakage, proprietary record leakage, public-surface leakage, map-truth leakage, AI leakage, or release approval obvious
- local validation reports emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, E2E case ID, domain, object family, source role, aggregation receipt ref, evidence ref, policy decision ID, review record ID, release ref, public surface type, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this E2E lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real USDA, NRCS, SSURGO/SDA, Mesonet, SCAN/AWDB, USCRN, SMAP, HLS, CDL, QuickStats, or Drought Monitor payloads | Default E2E tests must stay synthetic, deterministic, and no-network. |
| Direct reads from RAW, WORK, QUARANTINE, canonical/internal stores, unpublished candidates, direct model runtime outputs, or public production stores | Bypasses the trust membrane. |
| Real field/operator/parcel identifiers, proprietary yield, pesticide records, crop insurance, farm operation detail, private irrigation detail, or person-land joins | Sensitive and rights-restricted material must fail closed. |
| Secrets, credentials, private endpoints, production logs, or production telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |
| Public map layers, tiles, screenshots, exports, Focus Mode outputs, AI context packets, or public API payloads | Publication requires governed release. |

---

## Suggested Layout

```text
tests/e2e/agriculture/
|-- README.md
|-- test_public_aggregate_flow.py
|-- test_field_level_request_denies.py
|-- test_catalog_to_governed_api_flow.py
|-- test_map_focus_mode_release_gate.py
|-- test_soil_crop_context_preserves_soil_authority.py
|-- test_soil_moisture_context_preserves_source_role.py
|-- test_veg_index_context_not_crop_truth.py
|-- test_correction_withdrawal_rollback_flow.py
|-- test_governed_ai_abstains_without_release.py
`-- test_agriculture_e2e_no_network.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable E2E runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/e2e/agriculture
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no private field/operator/parcel data, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal E2E Fixture

Synthetic E2E fixtures should make the full governed path inspectable without carrying real Agriculture data.

```json
{
  "fixture_id": "agriculture-e2e-public-aggregate-example",
  "domain": "agriculture",
  "e2e_case": "public_aggregate_response",
  "request_envelope_ref": "request-envelope-fixture-ag-e2e-001",
  "object_family": "CropObservationAggregate",
  "source_descriptor_id": "source-descriptor-fixture-ag-e2e-001",
  "source_role": "aggregate",
  "evidence_ref": "evidence-ref-fixture-ag-e2e-001",
  "aggregation_receipt_ref": "aggregation-receipt-fixture-ag-e2e-001",
  "policy_decision_ref": "policy-decision-fixture-ag-e2e-001",
  "review_record_ref": "review-record-fixture-ag-e2e-001",
  "release_manifest_ref": "release-manifest-fixture-ag-e2e-001",
  "rollback_card_ref": "rollback-card-fixture-ag-e2e-001",
  "public_surface": "governed_api_feature_summary",
  "expected_outcome": "ABSTAIN",
  "reason_code": "E2E_FIXTURE_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
    "FIELD_LEVEL_TRUTH_CANARY",
    "OPERATOR_IDENTITY_CANARY",
    "PARCEL_JOIN_CANARY",
    "PROPRIETARY_YIELD_CANARY",
    "PESTICIDE_RECORD_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, source-role vocabulary, public-surface vocabulary, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; E2E tests belong under a test responsibility lane, not as authority roots. | Does not prove executable E2E tests, fixtures, CI, or pass rates. |
| `tests/e2e/README.md` | CONFIRMED repo evidence | E2E parent path exists as a greenfield stub. | Parent does not yet provide mature E2E lane guidance. |
| `tests/domains/agriculture/README.md` | CONFIRMED repo evidence | Agriculture domain tests define enforceability scope, child lanes, no-network behavior, source-role preservation, aggregate-only handling, catalog/release/rollback boundaries, and non-authority posture. | Domain README does not prove executable tests or E2E composition. |
| `docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md` | CONFIRMED repo evidence | No-network is the default first lane; live source calls, live model calls, field-level sensitive data, and public artifacts are excluded; Agriculture tests should prove schema, policy, evidence, catalog, release, rollback, and API envelope behavior with synthetic fixtures. | Many paths in the runbook are PROPOSED until implementation verification. |
| `docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED repo evidence | Defines RAW to PUBLISHED lifecycle, aggregation discipline, field-level deny-by-default posture, cross-lane ownership, EvidenceBundle support, correction, and rollback posture. | The doc marks path-shaped claims and implementation details as PROPOSED where not inspected. |
| `docs/domains/agriculture/API_CONTRACTS.md` | CONFIRMED repo evidence | Defines governed API posture, finite runtime outcomes, aggregate-only/public-safe defaults, fail-closed behavior, and direct RAW/WORK/QUARANTINE access as out of scope. | Route names, DTO names, and paths remain PROPOSED / NEEDS VERIFICATION in that doc. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/e2e/agriculture/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |

---

## Validation Checklist

- [ ] Expand or confirm the parent E2E index at `tests/e2e/README.md`.
- [ ] Confirm accepted fixture home and naming convention for Agriculture E2E fixtures.
- [ ] Confirm accepted E2E harness pattern: mocked governed API process, in-process envelope validator, static fixture runner, or other approved no-network shape.
- [ ] Confirm accepted schemas for request envelope, response envelope, EvidenceRef, EvidenceBundle stub, AggregationReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs.
- [ ] Add executable tests for aggregate public flow, field-level deny flow, catalog-to-API flow, map/Focus Mode release gate, Soil context boundary, soil-moisture boundary, veg-index boundary, correction/withdrawal/rollback, governed AI abstention, and no-network behavior.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, private field/operator/parcel data, or public artifact writes.
- [ ] Confirm public API, map, tile, screenshot, Focus Mode, export, and AI outputs cannot bypass EvidenceBundle resolution, source role, aggregation receipt, policy, review, release, correction, withdrawal, or rollback controls.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this E2E lane starts to store real source data, trust-bearing records, production release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, pipeline implementation, map implementation, API implementation, AI runtime behavior, or direct public outputs instead of documenting and testing boundaries.

Rollback is also required if this lane treats an E2E pass as Agriculture truth, field-level truth, operator identity, parcel truth, proprietary-yield truth, pesticide-record truth, crop-insurance truth, public map truth, AI truth, release approval, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent E2E placement, fixtures, schemas, source-role handling, aggregation handling, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, public-surface invalidation, and CI integration are reverified.

[Back to top](#top)