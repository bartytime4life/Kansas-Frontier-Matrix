<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-soil-readme
title: Soil Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; soil-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; soil; synthetic-only; no-network; public-safe; support-type-aware; source-resolution-aware; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, soil, synthetic-fixtures, no-network, public-safe, support-type-separation, resolution-tagging, MUKEY, COKEY, CHKEY, SourceDescriptor, EvidenceRef, EvidenceBundle, RunReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/soil/README.md
  - ../../../../fixtures/domains/soil/README.md
  - ../../../../docs/domains/soil/README.md
  - ../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../contracts/domains/soil/
  - ../../../../contracts/soil/
  - ../../../../schemas/contracts/v1/domains/soil/
  - ../../../../schemas/contracts/v1/soil/
  - ../../../../policy/domains/soil/
  - ../../../../policy/sensitivity/soil/
  - ../../../../data/registry/sources/soil/
  - ../../../../release/candidates/soil/
notes:
  - "This README replaces placeholder content at tests/fixtures/domains/soil/README.md."
  - "This lane documents test-local expectations for Soil fixtures. Canonical reusable Soil fixtures should live under fixtures/domains/soil/ unless an ADR or parent README says otherwise."
  - "The current fixtures/domains/soil/README.md is a greenfield stub in the repo; fixture payload inventory and child-lane coverage remain NEEDS VERIFICATION."
  - "Soil contract/schema homes have a documented flat-vs-segment open question; this README references both without resolving the ADR question."
  - "Executable tests, fixture payload inventory, test harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil test fixtures

> Test-lane documentation for Soil fixtures referenced from `tests/fixtures/domains/soil/`. This path describes how tests may use synthetic fixture material without turning fixture examples into source truth, soil truth, source-registry authority, catalog truth, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: test fixtures" src="https://img.shields.io/badge/lane-test__fixtures-purple">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not truth" src="https://img.shields.io/badge/boundary-fixtures__not__truth-success">
</p>

**Path:** `tests/fixtures/domains/soil/README.md`  
**Status:** draft / placeholder replaced / Soil test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/soil`  
**Canonical reusable fixture root:** `fixtures/domains/soil/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `fixtures/domains/soil/README.md` exists but is only a greenfield stub; CONFIRMED Soil canonical path guidance places enforceability proof under `tests/domains/soil/` and reusable fixtures under `fixtures/domains/soil/`; NEEDS VERIFICATION for executable tests, fixture payload inventory, child fixture lanes, fixture schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/soil/` is a test-local documentation lane for Soil fixture expectations.

This lane should explain how test code may reference, mirror, stub, or locally constrain Soil fixture material while preserving the authority of the canonical fixture root. It can describe test-only fixture behavior, expected fixture families, validation expectations, negative cases, no-network posture, public-safe geometry rules, support-type separation, resolution-tagging expectations, source-role preservation, evidence refs, run receipts, and safe-output behavior.

A fixture used from this lane should not mean that a soil map unit is authoritative, a component/horizon join has been admitted, a soil-moisture value is current, a gridded derivative is compatible with a survey polygon, a catalog record is closed, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. Soil path guidance names `tests/domains/soil/` and `fixtures/domains/soil/` as the enforceability-proof surface and calls out Soil-specific golden/adversarial fixtures. This requested lane must therefore remain test-scoped unless a parent README or ADR chooses otherwise.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Test-local Soil fixture expectations | `tests/fixtures/domains/soil/` | This directory. |
| Reusable Soil fixtures | `fixtures/domains/soil/` | Canonical fixture root; currently README-backed but greenfield-stubbed. |
| Soil domain tests | `tests/domains/soil/` | Consumers and validators; not fixture authority. |
| Semantic contracts | `contracts/domains/soil/` or `contracts/soil/` pending OPEN-SOIL-01 | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/soil/` or `schemas/contracts/v1/soil/` pending OPEN-SOIL-01 | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/soil/` and `policy/sensitivity/soil/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/soil/` | Source identity, role, rights, sensitivity, support type, resolution, and freshness records; not owned here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second fixture root unless a parent README or ADR explicitly allows test-local copies. Prefer references to `fixtures/domains/soil/` for reusable fixture payloads once that root is populated.

---

## Invariant under test

> **Soil fixtures are synthetic bounded examples, not Soil truth.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/soil/`; test-local copies require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake MUKEY/COKEY/CHKEY values, toy source refs, minimized geometry, toy timestamps, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live NRCS, SDA, Mesonet, SCAN, USCRN, SMAP, SoilGrids, map, release, public API, or AI services. | `ERROR`. |
| Support-type boundary | Static survey, gridded derivative, station moisture, satellite grid, pedon evidence, interpretation, and synthetic examples stay distinct. | `DENY` / `ABSTAIN`. |
| Resolution boundary | SSURGO, gSSURGO, gNATSGO, SoilGrids, SMAP, and station examples carry explicit source resolution, depth, unit, or resampling posture where material. | `DENY` / validation failure. |
| Identity boundary | MUKEY, COKEY, CHKEY, component, horizon, pedon, and derived-view identities do not collapse. | validation failure. |
| Evidence boundary | Claim-like fixtures include EvidenceRef expectations or explicitly mark evidence as out of scope. | `ABSTAIN`. |
| Receipt boundary | RunReceipt, validation, source-head, correction, withdrawal, and rollback refs are explicit where material. | validation failure. |
| Policy boundary | Rights, sensitivity, precision, landowner-identifying joins, source-license, review, and release blockers fail closed in negative fixtures. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected fixture-test families

| Family | Purpose | Boundary |
|---|---|---|
| Valid fixture smoke checks | Prove known-good synthetic fixture envelopes satisfy expected shape. | Valid fixture is not true Soil data. |
| Invalid fixture checks | Prove malformed, ambiguous, unsafe, unsupported, or rights-limited examples fail for finite reasons. | Invalid examples are not production incidents. |
| No-network fixture checks | Prove fixture loading is local and deterministic. | No live connectors by default. |
| MUKEY / COKEY / CHKEY identity checks | Prove map-unit, component, and horizon identifiers remain distinct and stable in examples. | Toy keys are not official NRCS keys. |
| Component-horizon join checks | Prove join examples preserve component percent, horizon depth, and evidence refs. | Join fixture is not join authority. |
| Horizon-depth edge checks | Prove invalid depths, overlaps, unit drift, and missing bounds fail closed. | Synthetic edge case is not source error proof. |
| Soil-moisture observation checks | Prove unit, depth, QC, station/grid support, observed time, retrieval time, and freshness remain explicit. | Fixture is not current moisture condition. |
| Support-type separation checks | Prove survey, gridded derivative, station, satellite, pedon, and interpretation examples are not silently fused. | No unified surface without support badges. |
| Resolution/resampling checks | Prove source resolution and resampling method are explicit for gridded or composite examples. | No silent resampling into a false precision. |
| Rights and sensitivity checks | Prove landowner-identifying joins, parcel/pedon joins, restricted precision, or unresolved rights deny or abstain. | No real property/person data. |
| Evidence and receipt checks | Prove EvidenceRef, RunReceipt, ValidationReport, correction, and rollback expectations are present where material. | Fixture refs are synthetic. |
| Cross-lane context checks | Prove Agriculture crop/yield, Hydrology streamflow/groundwater/flood, Geology lithology, Habitat context, Hazards exposure, and People/Land joins stay governed by owning lanes. | Context is not ownership transfer. |

---

## Relationship to canonical Soil fixtures

The canonical Soil fixture root currently exists as `fixtures/domains/soil/README.md`, but that README is a greenfield stub in the repo. This `tests/fixtures/...` lane should not pretend that a reusable fixture inventory already exists.

Until `fixtures/domains/soil/` is populated, this lane may document expected test-local fixture contracts, canary cases, and future consumer checks. Once reusable payloads are added, this lane should reference them instead of duplicating them.

| Question | Preferred answer |
|---|---|
| Need a reusable fixture payload? | Put it under `fixtures/domains/soil/`. |
| Need a test-only wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source/lifecycle roots. |
| Need policy or schema authority? | Do not put it here. Use policy or schema roots. |
| Need release authority? | Do not put it here. Use release roots. |
| Need real SSURGO/SDA/Mesonet/SMAP/SoilGrids data? | Do not put it here; use synthetic canaries or route through the governed lifecycle. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Soil fixtures under `fixtures/domains/soil/` once that root is populated
- test-local fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RunReceipt`, `ValidationReport`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, `LayerManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `SoilMapUnit`, `SoilComponent`, `Horizon`, `SoilProperty`, `HydrologicSoilGroup`, `SoilMoistureObservation`, `Pedon`, `SoilProfileView`, `ErosionRisk`, `SuitabilityRating`, `ComponentHorizonJoin`, and `SoilTimeCaveat` examples
- synthetic support-type, source-resolution, resampling, depth, unit, QC, rights, sensitivity, valid, invalid, denied, abstention, correction, withdrawal, stale-state, and rollback cases
- canary values that make support-type fusion, resolution silent-resampling, source-role collapse, MUKEY/COKEY/CHKEY collapse, landowner-identifying join exposure, direct-public-read leakage, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, support type, source role, source resolution, unit, depth, QC state, evidence ref, run receipt ref, validation ref, policy decision ID, review record ID, release ref, layer manifest ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Live soil-moisture station values, real SSURGO/SDA query results, gSSURGO/gNATSGO rasters, SMAP granules, SoilGrids COGs, or Mesonet/SCAN/USCRN records | Source material belongs in governed lifecycle roots. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, or runtime outputs | Bypasses the trust membrane. |
| Landowner-identifying joins, parcel/pedon/person joins, sensitive groundwater/well precision, private property data, or restricted field notes | Sensitive and rights-limited material must fail closed. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/domains/soil/
|-- README.md
|-- manifest_expectations.json
|-- test_fixture_manifest_shape.py
|-- test_no_network_fixture_loading.py
|-- test_mukey_cokey_chkey_identity_no_collapse.py
|-- test_support_type_fixture_no_fusion.py
|-- test_resolution_resampling_tags_required.py
|-- test_landowner_join_denial_canaries.py
|-- test_evidence_fixture_refs_required.py
`-- test_release_fixture_refs_do_not_authorize_publication.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/soil
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no live station values, no real SSURGO/SDA/SMAP/SoilGrids payloads, no landowner-identifying joins, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal fixture manifest

Synthetic test-local manifests should describe fixture expectations without carrying real Soil data.

```json
{
  "fixture_manifest_id": "soil-test-fixture-manifest-example",
  "domain": "soil",
  "canonical_fixture_ref": "fixtures/domains/soil/valid/example-fixture.json",
  "fixture_family": "public_safe_soil_map_unit_context",
  "source_role": "synthetic",
  "support_type": "synthetic_static_survey_example",
  "source_resolution": "toy_polygon",
  "sensitivity_posture": "public_safe_synthetic",
  "evidence_ref": "evidence:synthetic:soil:test:example",
  "run_receipt_ref": "receipt:synthetic:soil:run:example",
  "policy_decision_ref": "policy:synthetic:soil:allow-public-safe-example",
  "expected_outcome": "PASS",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, the manifest should make the denial cause explicit:

```json
{
  "fixture_manifest_id": "soil-test-fixture-manifest-deny-support-type-fusion",
  "domain": "soil",
  "fixture_family": "support_type_fusion_denial",
  "source_role": "synthetic",
  "attempted_interpretation": "unified_soil_condition_surface_without_support_badges",
  "support_types_present": [
    "static_survey",
    "gridded_derivative",
    "station_soil_moisture",
    "satellite_grid"
  ],
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SUPPORT_TYPE_FUSION_BLOCKED",
    "SOURCE_RESOLUTION_TAG_REQUIRED"
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
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | Public-safe soil map-unit context fixture loads locally. |
| `ABSTAIN` | The fixture resembles a claim but lacks enough synthetic evidence closure, support-type support, rights support, or citation support to answer. | Missing EvidenceRef for a claim-like soil property. |
| `DENY` | Policy, rights, sensitivity, review, release, support-type, resolution, identity, or precision checks block exposure. | Synthetic support-type fusion or landowner-join canary. |
| `ERROR` | The fixture or loader is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live NRCS/SDA request. |

---

## Public-safe geometry, identity, and resolution rules

Soil fixture geometry, keys, and resolution must be intentionally boring and safe.

| Class | Fixture posture |
|---|---|
| Toy polygon, grid cell, or point | Allowed only when obviously synthetic and not representing a real parcel, pedon, station, or well. |
| Toy MUKEY / COKEY / CHKEY | Required for identity tests; must be fake and marked synthetic. |
| Generalized map-unit or coarse context area | Preferred for public-safe examples. |
| Station-like moisture series | Allowed only with toy values, toy depths, toy units, QC state, and synthetic source/retrieval/freshness state. |
| Gridded derivative example | Must carry source resolution and resampling posture. |
| Landowner or parcel join | Not allowed as a positive fixture; use denial canaries only. |
| Unified condition surface | Allowed only when support-type and source-resolution tags are explicit or the fixture proves denial. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/soil/` unless there is a test-local reason
- [ ] source role, support type, source resolution, evidence state, rights state, sensitivity state, policy state, review state, release state, correction state, rollback state, and expected outcome are explicit where material
- [ ] static survey, gridded derivative, station reading, satellite grid, pedon evidence, interpretation, and synthetic examples are not flattened into one source role or support type
- [ ] MUKEY, COKEY, CHKEY, component, horizon, pedon, and derived-view identities remain separate where material
- [ ] no real source records, live readings, exact property/person joins, sensitive precision, private data, credentials, logs, or public artifacts are present
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
| Add a test-local manifest | Add expected outcome, reason code, canonical fixture ref, source-role state, support-type state, source-resolution state, and no-network posture. |
| Add a reusable payload | Prefer `fixtures/domains/soil/`; link it here only if tests consume it. |
| Add a negative fixture | State the finite failure outcome and policy/evidence/support-type/resolution reason. |
| Add a live-source-like case | Use synthetic canaries; do not use live NRCS, SDA, Mesonet, SCAN, USCRN, SMAP, or SoilGrids content. |
| Add a new object-family fixture | Confirm the corresponding contract/schema/policy home or mark it PROPOSED. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Parent test-fixture READMEs: not verified during this update; this file remains self-contained until parent indexes exist.
- Canonical Soil fixture root: verified as present, but only as a greenfield stub during authoring.
- Fixture payload inventory: not verified in this update.
- Soil path-register alignment: verified against `docs/domains/soil/CANONICAL_PATHS.md` for the domain-placement lane, test/fixture responsibilities, lifecycle invariant, support-type separation, source-resolution warnings, connector discipline, public-path discipline, and open flat-vs-segment contract/schema question.
- Contract/schema alignment: NEEDS VERIFICATION because Soil has a documented flat-vs-segment contract/schema-home question under OPEN-SOIL-01.
- Consumer alignment: NEEDS VERIFICATION against validators, Soil governed-API tests, schema checks, policy checks, source-role checks, support-type-separation checks, resolution/resampling checks, identity checks, Evidence Drawer checks, Focus Mode checks, renderer checks, release-readiness checks, rollback-readiness checks, and CI coverage.
- Tests and validators: NOT RUN.
