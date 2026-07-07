<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-hydrology-readme
title: Hydrology Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; hydrology-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Hydrology domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; hydrology; synthetic-only; no-network; public-safe; source-role-aware; temporal-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, hydrology, synthetic-fixtures, no-network, public-safe, temporal-logic, source-role, SourceDescriptor, EvidenceRef, EvidenceBundle, RunReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/hydrology/README.md
  - ../../../../fixtures/domains/hydrology/README.md
  - ../../../../fixtures/domains/hydrology/decision_envelope/README.md
  - ../../../../fixtures/domains/hydrology/decision_envelope/valid/README.md
  - ../../../../fixtures/domains/hydrology/decision_envelope/invalid/README.md
  - ../../../../fixtures/domains/hydrology/evidence_bundle/README.md
  - ../../../../fixtures/domains/hydrology/evidence_bundle/valid/README.md
  - ../../../../fixtures/domains/hydrology/evidence_bundle/invalid/README.md
  - ../../../../fixtures/domains/hydrology/run_receipt/README.md
  - ../../../../fixtures/domains/hydrology/run_receipt/valid/README.md
  - ../../../../fixtures/domains/hydrology/run_receipt/invalid/README.md
  - ../../../../fixtures/domains/hydrology/sources/README.md
  - ../../../../fixtures/domains/hydrology/valid/README.md
  - ../../../../fixtures/domains/hydrology/invalid/README.md
  - ../../../../fixtures/domains/hydrology/negative/README.md
  - ../../../../fixtures/domains/hydrology/golden/README.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hydrology/CANONICAL_PATHS.md
  - ../../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/sensitivity/hydrology/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../release/candidates/hydrology/
notes:
  - "This README replaces placeholder content at tests/fixtures/domains/hydrology/README.md."
  - "This lane documents test-local expectations for Hydrology fixtures. Canonical reusable Hydrology fixtures live under fixtures/domains/hydrology/ unless an ADR or parent README says otherwise."
  - "Hydrology source roles must remain distinct: NFHL regulatory context, NWIS observation, NHD/NHDPlus/3DHP reference geometry, forecasts/model output, and emergency/status context must not collapse."
  - "Executable tests, fixture payload inventory, test harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology test fixtures

> Test-lane documentation for Hydrology fixtures referenced from `tests/fixtures/domains/hydrology/`. This path describes how tests may use synthetic fixture material without turning fixture examples into source truth, hydrology truth, emergency-system authority, catalog truth, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: test fixtures" src="https://img.shields.io/badge/lane-test__fixtures-purple">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not truth" src="https://img.shields.io/badge/boundary-fixtures__not__truth-success">
</p>

**Path:** `tests/fixtures/domains/hydrology/README.md`  
**Status:** draft / placeholder replaced / Hydrology test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/hydrology`  
**Canonical reusable fixture root:** `fixtures/domains/hydrology/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED canonical Hydrology fixture README exists under `fixtures/domains/hydrology/`; CONFIRMED Hydrology canonical path guidance places fixture authority under `fixtures/domains/hydrology/` and warns against duplicating root fixtures under `tests/fixtures/`; NEEDS VERIFICATION for executable tests, fixture payload inventory, fixture schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/hydrology/` is a test-local documentation lane for Hydrology fixture expectations.

This lane should explain how test code may reference, mirror, stub, or locally constrain Hydrology fixture material while preserving the authority of the canonical fixture root. It can describe test-only fixture behavior, expected fixture families, validation expectations, negative cases, no-network posture, public-safe geometry rules, source-role preservation, temporal-role separation, evidence refs, run receipts, and safe-output behavior.

A fixture used from this lane should not mean that a water condition is current, a gauge value has been admitted, a flood zone has been accepted, an inundation claim is verified, a forecast is authoritative, a catalog record is closed, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. Hydrology path guidance warns against fixture sprawl and specifically says that if the repo uses root `fixtures/` as authority, content should not be duplicated under `tests/fixtures/domains/hydrology/`. This requested lane must therefore remain test-scoped unless a parent README or ADR chooses otherwise.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Test-local Hydrology fixture expectations | `tests/fixtures/domains/hydrology/` | This directory. |
| Reusable Hydrology fixtures | `fixtures/domains/hydrology/` | Canonical fixture root; referenced, not replaced. |
| Hydrology domain tests | `tests/domains/hydrology/` | Consumers and validators; not fixture authority. |
| Semantic contracts | `contracts/domains/hydrology/` | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/hydrology/` and `policy/sensitivity/hydrology/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/hydrology/` | Source identity, role, rights, sensitivity, cadence, and freshness records; not owned here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second fixture root unless a parent README or ADR explicitly allows test-local copies. Prefer references to `fixtures/domains/hydrology/` for reusable fixture payloads.

---

## Invariant under test

> **Hydrology fixtures are synthetic bounded examples, not Hydrology truth.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/hydrology/`; test-local copies require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake identifiers, mock markers, minimized geometry, toy timestamps, toy source heads, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live USGS, FEMA, state water office, NOAA, map, release, public API, or AI services. | `ERROR`. |
| Source-role boundary | NFHL regulatory context, NWIS observations, NHD/NHDPlus/3DHP reference geometry, forecast/model output, administrative/status context, and synthetic examples stay distinct. | `DENY` / `ABSTAIN`. |
| Temporal boundary | Observed time, valid time, source time, retrieval time, release time, expiry time, and stale-state markers remain separate. | `DENY` / `ABSTAIN`. |
| Emergency-system boundary | Fixtures never present KFM as an emergency warning, flood instruction, evacuation, or operational alert system. | `DENY`. |
| Evidence boundary | Claim-like fixtures include EvidenceRef expectations or explicitly mark evidence as out of scope. | `ABSTAIN`. |
| Receipt boundary | RunReceipt, validation, source-head, correction, withdrawal, and rollback refs are explicit where material. | validation failure. |
| Policy boundary | Rights, sensitivity, precision, source-license, freshness, groundwater-well precision, review, and release blockers fail closed in negative fixtures. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected fixture-test families

| Family | Purpose | Boundary |
|---|---|---|
| Valid fixture smoke checks | Prove known-good synthetic fixture envelopes satisfy expected shape. | Valid fixture is not true Hydrology data. |
| Invalid fixture checks | Prove malformed, ambiguous, unsafe, unsupported, or stale examples fail for finite reasons. | Invalid examples are not live conditions. |
| Negative fixture checks | Stage bounded fail-closed examples before they are promoted into stable invalid cases. | Negative examples are not production incidents. |
| No-network fixture checks | Prove fixture loading is local and deterministic. | No live connectors by default. |
| Decision-envelope checks | Prove Hydrology runtime envelopes preserve `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, review-required, or blocked-render states. | Runtime fixture is not API proof. |
| EvidenceBundle checks | Prove claim-scope evidence support, citations, rights, sensitivity, transforms, and checksums remain explicit. | Evidence fixture is not proof closure. |
| RunReceipt checks | Prove synthetic run provenance carries inputs, outputs, source refs, validation refs, spec hash, and outcome. | Receipt fixture is not production receipt storage. |
| Source fixture checks | Prove source-like examples preserve role, rights, sensitivity, cadence, source-head, and admission state. | Source fixture is not SourceDescriptor authority. |
| HUC and watershed checks | Prove HUC/WBD examples preserve hierarchy and identity scope. | HUC fixture is not official WBD truth. |
| Gauge and observation checks | Prove NWIS-like observation examples preserve unit, timestamp, retrieval state, evidence, and freshness. | Gauge fixture is not a live gauge reading. |
| NFHL regulatory-context checks | Prove NFHL-like examples stay regulatory context and are not treated as observed inundation. | Regulatory context is not flood observation truth. |
| Temporal logic checks | Prove observed/source/retrieval/release/expiry times do not collapse. | Synthetic time series is not current condition. |
| Cross-lane context checks | Prove Hazards flood/drought, Habitat wetlands, Soil drainage, Agriculture irrigation, Roads flood closure, Settlements exposure, and People/Land joins stay governed by owning lanes. | Context is not ownership transfer. |

---

## Relationship to canonical Hydrology fixtures

The canonical Hydrology fixture root documents reusable fixture lanes for decision envelopes, EvidenceBundle-like examples, RunReceipt-like examples, sources, valid, invalid, negative, golden, and related expected-output examples.

This `tests/fixtures/...` lane should therefore avoid duplicating those payloads. It should instead document how tests consume them, what local wrappers may exist, and what safety checks must run before fixture material is accepted by test code.

| Question | Preferred answer |
|---|---|
| Need a reusable fixture payload? | Put it under `fixtures/domains/hydrology/`. |
| Need a test-only wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source/lifecycle roots. |
| Need policy or schema authority? | Do not put it here. Use policy or schema roots. |
| Need release authority? | Do not put it here. Use release roots. |
| Need live water/flood/emergency behavior? | Do not create KFM emergency authority; use synthetic canaries that prove source-role separation, freshness visibility, official-source referral, and fail-closed behavior. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Hydrology fixtures under `fixtures/domains/hydrology/`
- test-local fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RunReceipt`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, `LayerManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `Watershed`, `HUCUnit`, `HydroFeature`, `ReachIdentity`, `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `GroundwaterWell`, `AquiferObservation`, `NFHLZone`, and `Hydrograph` examples
- synthetic source-head, cadence, freshness, source-role, rights, sensitivity, valid, invalid, negative, golden, stale-state, correction, withdrawal, and rollback cases
- canary values that make source-role collapse, temporal collapse, NFHL-as-observed-inundation misuse, stale gauge exposure, groundwater precision leakage, direct-public-read leakage, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, source role, evidence ref, run receipt ref, validation ref, policy decision ID, review record ID, release ref, layer manifest ref, freshness state, source-head state, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Live gauge readings, flood warnings, advisories, forecasts, evacuation instructions, or operational public-safety guidance | KFM is not an emergency system. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, or runtime outputs | Bypasses the trust membrane. |
| Sensitive groundwater-well precision, private property/person joins, critical infrastructure exposure, or restricted incident records | Sensitive and rights-limited material must fail closed. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/domains/hydrology/
|-- README.md
|-- manifest_expectations.json
|-- test_fixture_manifest_shape.py
|-- test_no_network_fixture_loading.py
|-- test_source_role_fixture_no_upcast.py
|-- test_temporal_fields_do_not_collapse.py
|-- test_nfhl_regulatory_context_not_observed_inundation.py
|-- test_evidence_fixture_refs_required.py
|-- test_run_receipt_fixture_refs_required.py
`-- test_release_fixture_refs_do_not_authorize_publication.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/hydrology
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no live gauge/warning/forecast content, no sensitive groundwater precision, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal fixture manifest

Synthetic test-local manifests should describe fixture expectations without carrying real Hydrology data.

```json
{
  "fixture_manifest_id": "hydrology-test-fixture-manifest-example",
  "domain": "hydrology",
  "canonical_fixture_ref": "fixtures/domains/hydrology/decision_envelope/valid/example-fixture.json",
  "fixture_family": "public_safe_hydrology_context",
  "source_role": "synthetic",
  "sensitivity_posture": "public_safe_synthetic",
  "evidence_ref": "evidence:synthetic:hydrology:test:example",
  "run_receipt_ref": "receipt:synthetic:hydrology:run:example",
  "policy_decision_ref": "policy:synthetic:hydrology:allow-public-safe-example",
  "expected_outcome": "PASS",
  "freshness_state": "synthetic_not_current",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, the manifest should make the denial cause explicit:

```json
{
  "fixture_manifest_id": "hydrology-test-fixture-manifest-deny-nfhl-as-observed-inundation",
  "domain": "hydrology",
  "fixture_family": "source_role_collapse_denial",
  "source_role": "regulatory_context",
  "attempted_interpretation": "observed_inundation",
  "freshness_state": "synthetic_not_current",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SOURCE_ROLE_COLLAPSE_BLOCKED",
    "NFHL_IS_REGULATORY_CONTEXT_NOT_OBSERVED_INUNDATION"
  ],
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | Public-safe hydrology context fixture loads locally. |
| `ABSTAIN` | The fixture resembles a claim but lacks enough synthetic evidence closure, freshness support, source-role support, or citation support to answer. | Missing EvidenceRef for a claim-like flow observation. |
| `DENY` | Policy, rights, sensitivity, review, freshness, release, source-role, temporal, or precision checks block exposure. | Synthetic NFHL-as-observed-inundation canary. |
| `ERROR` | The fixture or loader is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live USGS or FEMA request. |

---

## Public-safe geometry and time rules

Hydrology fixture geometry and time must be intentionally boring and safe.

| Class | Fixture posture |
|---|---|
| Toy point, line, polygon, or grid cell | Allowed only when obviously synthetic and not representing a live gauge, facility, or sensitive place. |
| Generalized watershed, HUC, reach, or coarse context area | Preferred for public-safe hydrology examples. |
| NFHL-like polygon | Allowed only when synthetic and labeled as regulatory context, never observed inundation. |
| Gauge-like time series | Allowed only with toy values and explicit synthetic source/retrieval/freshness state. |
| Groundwater-well precision | Use generalized or denial canaries; do not use real well precision. |
| Current-condition language | Avoid unless explicitly synthetic and paired with source-role, freshness, and non-emergency-system posture. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/hydrology/` unless there is a test-local reason
- [ ] source role, evidence state, rights state, sensitivity state, freshness state, source-head state, policy state, review state, release state, correction state, rollback state, and expected outcome are explicit where material
- [ ] regulatory context, observations, reference geometry, model/forecast output, administrative/status context, and synthetic examples are not flattened into one source role
- [ ] observed time, valid time, source time, retrieval time, release time, expiry time, and stale-state markers remain separate where material
- [ ] no real source records, live readings, emergency instructions, sensitive groundwater precision, private data, credentials, logs, or public artifacts are present
- [ ] negative fixtures use finite outcomes and reason codes
- [ ] public-safe geometry is generalized, synthetic, binned, withheld, or deliberately denied
- [ ] test-local wrappers do not become a parallel fixture authority
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, and policy references are updated when consumer behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a test-local manifest | Add expected outcome, reason code, canonical fixture ref, source-role state, freshness state, and no-network posture. |
| Add a reusable payload | Prefer `fixtures/domains/hydrology/`; link it here only if tests consume it. |
| Add a negative fixture | State the finite failure outcome and policy/evidence/freshness/source-role reason. |
| Add a live-source-like case | Use synthetic canaries; do not use live gauge, flood, forecast, or warning content. |
| Add a new object-family fixture | Confirm the corresponding contract/schema/policy home or mark it PROPOSED. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Parent test-fixture READMEs: not verified during this update; this file remains self-contained until parent indexes exist.
- Canonical Hydrology fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Hydrology path-register alignment: verified against `docs/domains/hydrology/CANONICAL_PATHS.md` for the fixture/test lane distinction, fixture-sprawl warning, source-role separation, lifecycle invariant, and no-network posture.
- Contract/schema alignment: NEEDS VERIFICATION per child lane because several object-family schemas may still be draft or PROPOSED.
- Consumer alignment: NEEDS VERIFICATION against validators, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, run-receipt checks, source-descriptor checks, source-role checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, source-head checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
