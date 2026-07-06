<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-hazards-readme
title: Hazards Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; hazards-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Hazards domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; hazards; synthetic-only; no-network; public-safe; life-safety-boundary; freshness-aware; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, hazards, synthetic-fixtures, no-network, public-safe, life-safety-boundary, not-emergency-alert-system, freshness, expiry, SourceDescriptor, EvidenceRef, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/hazards/README.md
  - ../../../../fixtures/domains/hazards/README.md
  - ../../../../fixtures/domains/hazards/valid/README.md
  - ../../../../fixtures/domains/hazards/negative/README.md
  - ../../../../fixtures/domains/hazards/invalid/README.md
  - ../../../../fixtures/domains/hazards/golden/README.md
  - ../../../../fixtures/domains/hazards/feature_resolver/README.md
  - ../../../../fixtures/domains/hazards/drawer/README.md
  - ../../../../fixtures/domains/hazards/focus/README.md
  - ../../../../fixtures/domains/hazards/identity/README.md
  - ../../../../fixtures/domains/hazards/layer_manifest/README.md
  - ../../../../docs/domains/hazards/README.md
  - ../../../../docs/domains/hazards/CANONICAL_PATHS.md
  - ../../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../../docs/domains/hazards/API_CONTRACTS.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../../contracts/hazards/
  - ../../../../contracts/domains/hazards/
  - ../../../../schemas/contracts/v1/hazards/
  - ../../../../schemas/contracts/v1/domains/hazards/
  - ../../../../policy/domains/hazards/
  - ../../../../policy/release/hazards/
  - ../../../../data/registry/sources/hazards/
  - ../../../../release/candidates/hazards/
notes:
  - "This README replaces placeholder content at tests/fixtures/domains/hazards/README.md."
  - "This lane documents test-local expectations for Hazards fixtures. Canonical reusable Hazards fixtures live under fixtures/domains/hazards/ unless an ADR or parent README says otherwise."
  - "Hazards has an elevated life-safety boundary: KFM fixtures may test not-emergency-alert behavior, but they must not act as operational warnings or advisories."
  - "Executable tests, fixture payload inventory, test harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards test fixtures

> Test-lane documentation for Hazards fixtures referenced from `tests/fixtures/domains/hazards/`. This path describes how tests may use synthetic fixture material without turning fixture examples into source truth, hazard truth, emergency alert authority, catalog truth, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: test fixtures" src="https://img.shields.io/badge/lane-test__fixtures-purple">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-orange">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: not emergency alert authority" src="https://img.shields.io/badge/boundary-not__emergency__alert__authority-critical">
</p>

**Path:** `tests/fixtures/domains/hazards/README.md`  
**Status:** draft / placeholder replaced / Hazards test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/hazards`  
**Canonical reusable fixture root:** `fixtures/domains/hazards/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED canonical Hazards fixture README exists under `fixtures/domains/hazards/`; CONFIRMED Hazards canonical path guidance allows `fixtures/domains/hazards/` or `tests/fixtures/domains/hazards/` per repo convention while requiring one documented fixture home; NEEDS VERIFICATION for executable tests, fixture payload inventory, fixture schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/hazards/` is a test-local documentation lane for Hazards fixture expectations.

This lane should explain how test code may reference, mirror, stub, or locally constrain Hazards fixture material while preserving the authority of the canonical fixture root. It can describe test-only fixture behavior, expected fixture families, validation expectations, negative cases, no-network posture, public-safe geometry rules, source-role preservation, freshness and expiry checks, not-emergency-alert posture, official-source referral, and safe-output behavior.

A fixture used from this lane should not mean that a hazard event is happening, a warning is current, an advisory is authoritative, an observed event has been admitted, a regulatory layer has been accepted, a catalog record is closed, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. Hazards path guidance records a fixture-home tension between `fixtures/domains/hazards/` and `tests/fixtures/domains/hazards/`, so this lane must remain explicitly test-scoped unless a parent README or ADR chooses otherwise.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Test-local Hazards fixture expectations | `tests/fixtures/domains/hazards/` | This directory. |
| Reusable Hazards fixtures | `fixtures/domains/hazards/` | Canonical fixture root; referenced, not replaced. |
| Hazards domain tests | `tests/domains/hazards/` | Consumers and validators; not fixture authority. |
| Semantic contracts | `contracts/hazards/` or `contracts/domains/hazards/` pending repo convention | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/hazards/` or `schemas/contracts/v1/domains/hazards/` pending ADR | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/hazards/` and `policy/release/hazards/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/hazards/` | Source identity, role, rights, sensitivity, and freshness records; not owned here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second fixture root unless a parent README or ADR explicitly allows test-local copies. Prefer references to `fixtures/domains/hazards/` for reusable fixture payloads.

---

## Invariant under test

> **Hazards fixtures are synthetic bounded examples, not hazard truth or emergency alert authority.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/hazards/`; test-local copies require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake identifiers, mock markers, minimized geometry, toy timestamps, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live NOAA, NWS, FEMA, USGS, NASA, state EM, map, release, public API, or AI services. | `ERROR`. |
| Life-safety boundary | Fixtures never instruct users what to do in an emergency and never present KFM as an alerting authority. | `DENY`. |
| Freshness/expiry boundary | Operational-context examples carry synthetic issue, observed, source, retrieval, release, expiry, stale, and correction states where material. | `DENY` / `ABSTAIN`. |
| Official-referral boundary | Operational-context examples refer users to official issuing authorities in expected output. | `DENY` / validation failure. |
| Source-role boundary | Observed events, regulatory zones, modeled surfaces, aggregate summaries, administrative declarations, candidate records, and synthetic examples stay distinct. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claim-like fixtures include EvidenceRef expectations or explicitly mark evidence as out of scope. | `ABSTAIN`. |
| Policy boundary | Rights, sensitivity, precision, source-license, stale-state, critical-infrastructure, review, and release blockers fail closed in negative fixtures. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected fixture-test families

| Family | Purpose | Boundary |
|---|---|---|
| Valid fixture smoke checks | Prove known-good synthetic fixture envelopes satisfy expected shape. | Valid fixture is not true Hazards data. |
| Negative fixture checks | Prove bounded but risky examples fail closed or require review. | Negative examples are not production incidents. |
| Invalid fixture checks | Prove malformed, ambiguous, unsafe, unsupported, or stale examples fail for finite reasons. | Invalid examples are not live alerts. |
| No-network fixture checks | Prove fixture loading is local and deterministic. | No live connectors by default. |
| Feature resolver checks | Prove synthetic feature/detail resolver cases preserve finite outcomes, citations, disclaimers, and source roles. | Resolver fixture is not API proof. |
| Evidence Drawer checks | Prove drawer payload examples expose evidence, policy, freshness, correction, and rollback context. | Drawer fixture is not evidence closure. |
| Focus Mode checks | Prove Focus answers remain bounded, citation-aware, disclaimer-visible, and policy-constrained. | Focus fixture is not AI authority. |
| Identity checks | Prove stable IDs, duplicate handling, temporal scope, correction lineage, and supersession remain explicit. | Identity fixture is not canonical identity proof. |
| Layer manifest checks | Prove layer examples include public-safe posture, freshness, release refs, rollback refs, and not-emergency-alert flags. | Manifest fixture is not release approval. |
| Source-role checks | Prove warning/advisory context is not silently converted into observed event truth. | Source role fixed at admission. |
| Freshness and stale-state checks | Prove expired operational-context examples deny, abstain, or show stale state visibly. | Stale fixture is not current condition. |
| Cross-lane sensitivity checks | Prove infrastructure exposure, roads/rail closure, hydrology flood/drought context, atmosphere smoke/heat, habitat/fire, and settlement exposure refs stay governed by owning lanes. | Context is not ownership transfer. |

---

## Relationship to canonical Hazards fixtures

The canonical Hazards fixture root documents reusable fixture lanes for valid, negative, invalid, golden, feature resolver, Evidence Drawer, Focus Mode, identity, layer manifest, and related expected-output examples.

This `tests/fixtures/...` lane should therefore avoid duplicating those payloads. It should instead document how tests consume them, what local wrappers may exist, and what safety checks must run before fixture material is accepted by test code.

| Question | Preferred answer |
|---|---|
| Need a reusable fixture payload? | Put it under `fixtures/domains/hazards/`. |
| Need a test-only wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source/lifecycle roots. |
| Need policy or schema authority? | Do not put it here. Use policy or schema roots. |
| Need release authority? | Do not put it here. Use release roots. |
| Need operational alerting behavior? | Do not create KFM alert authority; use synthetic canaries that prove referral to official sources and fail-closed behavior. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Hazards fixtures under `fixtures/domains/hazards/`
- test-local fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, `LayerManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `HazardEvent`, `HazardObservation`, `WarningContext`, `AdvisoryContext`, `DisasterDeclaration`, `FloodContext`, `WildfireDetection`, `SmokeContext`, `DroughtIndicator`, `EarthquakeEvent`, `HeatColdEvent`, `ExposureSummary`, `ResilienceSummary`, `HazardTimeline`, and `ImpactArea` examples
- synthetic feature resolver, drawer, Focus, identity, layer manifest, valid, negative, invalid, golden, stale-state, correction, withdrawal, and rollback cases
- canary values that make life-safety drift, source-role collapse, expired-warning exposure, stale-state failure, critical-infrastructure exposure, direct-public-read leakage, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, source role, evidence ref, policy decision ID, review record ID, release ref, layer manifest ref, freshness state, expiry state, finite outcome, reason code, official-referral URL placeholder, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Live warnings, watches, advisories, alerts, emergency instructions, or operational public-safety guidance | KFM is not an alert authority. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, or runtime outputs | Bypasses the trust membrane. |
| Exact critical-infrastructure geometry, private facility exposure, sensitive personal/property joins, or restricted incident records | Sensitive and rights-limited material must fail closed. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/domains/hazards/
|-- README.md
|-- manifest_expectations.json
|-- test_fixture_manifest_shape.py
|-- test_no_network_fixture_loading.py
|-- test_not_emergency_alert_boundary.py
|-- test_operational_context_expiry_canaries.py
|-- test_source_role_fixture_no_upcast.py
|-- test_official_referral_fixture_required.py
|-- test_evidence_fixture_refs_required.py
`-- test_release_fixture_refs_do_not_authorize_publication.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/hazards
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no live alerting or operational warning content, no critical-infrastructure exposure, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal fixture manifest

Synthetic test-local manifests should describe fixture expectations without carrying real Hazards data.

```json
{
  "fixture_manifest_id": "hazards-test-fixture-manifest-example",
  "domain": "hazards",
  "canonical_fixture_ref": "fixtures/domains/hazards/valid/example-fixture.json",
  "fixture_family": "public_safe_hazard_context",
  "source_role": "synthetic",
  "sensitivity_posture": "public_safe_synthetic",
  "evidence_ref": "evidence:synthetic:hazards:test:example",
  "policy_decision_ref": "policy:synthetic:hazards:allow-public-safe-example",
  "expected_outcome": "PASS",
  "not_emergency_alert_system": true,
  "official_referral_required": true,
  "freshness_state": "synthetic_not_current",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, the manifest should make the denial cause explicit:

```json
{
  "fixture_manifest_id": "hazards-test-fixture-manifest-deny-expired-operational-context",
  "domain": "hazards",
  "fixture_family": "expired_operational_context_denial",
  "source_role": "synthetic",
  "freshness_state": "expired_synthetic_canary",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "OPERATIONAL_CONTEXT_EXPIRED",
    "NOT_EMERGENCY_ALERT_AUTHORITY"
  ],
  "not_emergency_alert_system": true,
  "official_referral_required": true,
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | Public-safe non-operational hazard context fixture loads locally. |
| `ABSTAIN` | The fixture resembles a claim but lacks enough synthetic evidence closure, freshness support, or citation support to answer. | Missing EvidenceRef or official referral for a claim-like output. |
| `DENY` | Policy, rights, sensitivity, review, freshness, release, life-safety, or exact-geometry checks block exposure. | Synthetic expired warning or KFM-as-alert-authority canary. |
| `ERROR` | The fixture or loader is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live source request. |

---

## Public-safe geometry and freshness rules

Hazards fixture geometry and time must be intentionally boring and safe.

| Class | Fixture posture |
|---|---|
| Toy point, line, polygon, or grid cell | Allowed only when obviously synthetic and not representing a live hazard or sensitive facility. |
| Generalized polygon or coarse context area | Preferred for public-safe hazard-context examples. |
| Operational warning/watch/advisory geometry | Use only as synthetic stale/expiry/referral canaries; never live. |
| Critical infrastructure or private exposure overlay | Not allowed as a positive fixture; use generalized or denial canaries. |
| Expired operational context | Allowed only as a negative fixture proving `DENY`, `ABSTAIN`, stale-state display, correction, or rollback behavior. |
| Current-condition language | Avoid unless explicitly synthetic and paired with `not_emergency_alert_system` posture and official referral behavior. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/hazards/` unless there is a test-local reason
- [ ] source role, evidence state, rights state, sensitivity state, freshness state, policy state, review state, release state, correction state, rollback state, and expected outcome are explicit where material
- [ ] observed events, regulatory zones, modeled surfaces, administrative declarations, aggregate summaries, candidate records, and synthetic examples are not flattened into one source role
- [ ] no real source records, live warnings/advisories, emergency instructions, critical-infrastructure exposure, private data, credentials, logs, or public artifacts are present
- [ ] negative fixtures use finite outcomes and reason codes
- [ ] public-safe geometry is generalized, synthetic, binned, withheld, or deliberately denied
- [ ] `not_emergency_alert_system` posture and official referral expectations are present for operational-context examples
- [ ] test-local wrappers do not become a parallel fixture authority
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, and policy references are updated when consumer behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a test-local manifest | Add expected outcome, reason code, canonical fixture ref, freshness state, and no-network posture. |
| Add a reusable payload | Prefer `fixtures/domains/hazards/`; link it here only if tests consume it. |
| Add a negative fixture | State the finite failure outcome and policy/evidence/freshness reason. |
| Add an operational-context case | Use synthetic canaries; do not use live warning/advisory content. |
| Add a new object-family fixture | Confirm the corresponding contract/schema/policy home or mark it PROPOSED. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Parent test-fixture READMEs: not verified during this update; this file remains self-contained until parent indexes exist.
- Canonical Hazards fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Hazards path-register alignment: verified against `docs/domains/hazards/CANONICAL_PATHS.md` for the fixture-home tension, lifecycle, source-role, release-plane, and life-safety boundary.
- Contract/schema alignment: NEEDS VERIFICATION because Hazards has a documented flat-vs-segment schema-home tension pending ADR-S-01 / ADR-0001.
- Consumer alignment: NEEDS VERIFICATION against validators, valid-fixture checks, negative-fixture checks, invalid-fixture checks, golden-file checks, governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, identity checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, freshness checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
