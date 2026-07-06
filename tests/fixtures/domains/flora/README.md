<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-flora-readme
title: Flora Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; flora-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Flora domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; flora; synthetic-only; no-network; public-safe; rare-plant-aware; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, flora, synthetic-fixtures, no-network, public-safe, rare-plants, geoprivacy, SourceDescriptor, EvidenceRef, EvidenceBundle, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/flora/README.md
  - ../../../../fixtures/domains/flora/README.md
  - ../../../../fixtures/domains/flora/golden/README.md
  - ../../../../fixtures/domains/flora/valid/README.md
  - ../../../../fixtures/domains/flora/invalid/README.md
  - ../../../../fixtures/domains/flora/synthetic/README.md
  - ../../../../fixtures/domains/flora/source_descriptors/README.md
  - ../../../../fixtures/domains/flora/sources/README.md
  - ../../../../fixtures/domains/flora/sources/plants/README.md
  - ../../../../fixtures/domains/flora/plants_drift/README.md
  - ../../../../fixtures/domains/flora/plant_taxon/README.md
  - ../../../../fixtures/domains/flora/flora_occurrence/README.md
  - ../../../../fixtures/domains/flora/rare_plant_record/README.md
  - ../../../../fixtures/domains/flora/vegetation_community/README.md
  - ../../../../fixtures/domains/flora/invasive_plant_record/README.md
  - ../../../../fixtures/domains/flora/phenology_observation/README.md
  - ../../../../fixtures/domains/flora/evidence_bundles/README.md
  - ../../../../fixtures/domains/flora/decision_envelopes/README.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/API_CONTRACTS.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../policy/domains/flora/
  - ../../../../policy/sensitivity/flora/
  - ../../../../release/candidates/flora/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/flora/README.md."
  - "This lane documents test-local expectations for Flora fixtures. Canonical reusable Flora fixtures live under fixtures/domains/flora/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/README.md or tests/fixtures/domains/README.md during authoring. This lane is self-contained until those parent indexes are authored."
  - "Executable tests, fixture payload inventory, test harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora test fixtures

> Test-lane documentation for Flora fixtures referenced from `tests/fixtures/domains/flora/`. This path describes how tests may use synthetic fixture material without turning fixture examples into source truth, botanical truth, catalog truth, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: test fixtures" src="https://img.shields.io/badge/lane-test__fixtures-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-green">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not truth" src="https://img.shields.io/badge/boundary-fixtures__not__truth-success">
</p>

**Path:** `tests/fixtures/domains/flora/README.md`  
**Status:** draft / empty placeholder replaced / Flora test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/flora`  
**Canonical reusable fixture root:** `fixtures/domains/flora/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED canonical Flora fixture README exists under `fixtures/domains/flora/`; CONFIRMED Flora canonical path guidance recognizes `tests/fixtures/domains/flora/` as an alternative test-local fixture home when the repository chooses `tests/fixtures/`; NEEDS VERIFICATION for executable tests, fixture payload inventory, fixture schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/flora/` is a test-local documentation lane for Flora fixture expectations.

This lane should explain how test code may reference, mirror, stub, or locally constrain Flora fixture material while preserving the authority of the canonical fixture root. It can describe test-only fixture behavior, expected fixture families, validation expectations, negative cases, no-network posture, public-safe geometry rules, rare-plant denial cases, and safe-output behavior.

A fixture used from this lane should not mean that a Flora claim is true, a plant taxon has been resolved, a specimen has been admitted, an occurrence has been verified, a catalog record is closed, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Test-local Flora fixture expectations | `tests/fixtures/domains/flora/` | This directory. |
| Reusable Flora fixtures | `fixtures/domains/flora/` | Canonical fixture root; referenced, not replaced. |
| Flora domain tests | `tests/domains/flora/` | Consumers and validators; not fixture authority. |
| Semantic contracts | `contracts/domains/flora/` | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/flora/` | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/flora/` and `policy/sensitivity/flora/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, and sensitivity records; not owned here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second fixture root unless a parent README or ADR explicitly allows test-local copies. Prefer references to `fixtures/domains/flora/` for reusable fixture payloads.

---

## Invariant under test

> **Flora fixtures are synthetic bounded examples, not Flora truth.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/flora/`; test-local copies require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake identifiers, mock markers, minimized geometry, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, map services, release services, public APIs, or AI runtimes. | `ERROR`. |
| Rare-plant safety boundary | Exact sensitive rare-plant coordinates are never present in public-safe fixture payloads. | `DENY`. |
| Geoprivacy boundary | Public occurrence fixtures use generalized, binned, withheld, or clearly synthetic geometry where sensitivity matters. | `DENY` / validation failure. |
| Source-role boundary | Source roles remain fixed and cannot be upcast by fixtures, validators, catalog helpers, API envelopes, map renderers, or generated text. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claim-like fixtures include EvidenceRef expectations or explicitly mark evidence as out of scope. | `ABSTAIN`. |
| Receipt boundary | Redaction, validation, correction, withdrawal, and rollback refs are explicit where material. | validation failure. |
| Policy boundary | Rights, sensitivity, precision, source-license, steward-review, and release blockers fail closed in negative fixtures. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected fixture-test families

| Family | Purpose | Boundary |
|---|---|---|
| Valid fixture smoke checks | Prove known-good synthetic fixture envelopes satisfy expected shape. | Valid fixture is not true Flora data. |
| Invalid fixture checks | Prove malformed, ambiguous, unsafe, or unsupported examples fail for finite reasons. | Negative examples are not production incidents. |
| No-network fixture checks | Prove fixture loading is local and deterministic. | No live connectors by default. |
| Taxonomy-resolution checks | Prove `PlantTaxon`, crosswalk, synonym, and unresolved-name cases stay explicit. | Taxonomy fixture is not taxonomic authority. |
| Specimen and occurrence checks | Prove specimen-backed and occurrence-like examples preserve source identity, date, uncertainty, evidence, and rights posture. | Fixture records are synthetic. |
| Rare-plant denial checks | Prove exact sensitive/public unsafe records are denied, generalized, or withheld. | No real rare-plant locations. |
| Geoprivacy transform checks | Prove redaction/generalization outputs carry expected synthetic `RedactionReceipt` refs. | Transform receipt is not production proof. |
| Vegetation community checks | Prove polygon/classification examples remain public-safe and evidence-bounded. | Community fixture is not official vegetation mapping. |
| Invasive plant checks | Prove invasive-plant examples stay source-role-aware and cross-lane safe. | No automatic regulatory or management claim. |
| Phenology checks | Prove observed/source/retrieval/release time expectations stay distinct. | Synthetic seasonal pattern is not a real trend. |
| Evidence and receipt checks | Prove EvidenceRef and receipt expectations are present where material. | Fixture refs are synthetic. |
| Runtime envelope checks | Prove ANSWER / ABSTAIN / DENY / ERROR cases remain finite and policy-aware. | Runtime shape is not release approval. |
| Cross-lane context checks | Prove Habitat, Fauna, Hydrology, Soil, Agriculture, Roads, Settlements, Archaeology, and People/Land refs remain external authority. | Context is not ownership transfer. |

---

## Relationship to canonical Flora fixtures

The canonical Flora fixture root documents reusable fixture lanes for golden, valid, invalid, synthetic, source-descriptor, source-family, PLANTS drift, plant taxon, Flora occurrence, rare plant record, vegetation community, invasive plant record, phenology observation, EvidenceBundle, decision envelope, and related runtime examples.

This `tests/fixtures/...` lane should therefore avoid duplicating those payloads. It should instead document how tests consume them, what local wrappers may exist, and what safety checks must run before fixture material is accepted by test code.

| Question | Preferred answer |
|---|---|
| Need a reusable fixture payload? | Put it under `fixtures/domains/flora/`. |
| Need a test-only wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source/lifecycle roots. |
| Need policy or schema authority? | Do not put it here. Use policy or schema roots. |
| Need release authority? | Do not put it here. Use release roots. |
| Need exact sensitive flora coordinates? | Do not put them in public, fixture, or test-local material; use synthetic geometry or policy-denial canaries. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Flora fixtures under `fixtures/domains/flora/`
- test-local fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RedactionReceipt`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `PlantTaxon`, `FloraTaxonCrosswalk`, `SpecimenRecord`, `FloraOccurrence`, `RarePlantRecord`, `VegetationCommunity`, `InvasivePlantRecord`, `PhenologyObservation`, `RangePolygon`, `HabitatAssociation`, `BotanicalSurvey`, and `RestorationPlanting` examples
- synthetic valid, invalid, denied, abstention, correction, withdrawal, stale-state, and rollback cases
- canary values that make source-role collapse, exact-location leakage, rare-plant exposure, taxonomy drift, geoprivacy failure, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, source role, evidence ref, policy decision ID, redaction receipt ref, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, or runtime outputs | Bypasses the trust membrane. |
| Exact rare-plant coordinates, protected-species locations, steward-controlled locality data, culturally sensitive plant knowledge, or private property/person joins | Sensitive and rights-limited material must fail closed. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/domains/flora/
|-- README.md
|-- manifest_expectations.json
|-- test_fixture_manifest_shape.py
|-- test_no_network_fixture_loading.py
|-- test_taxonomy_fixture_no_silent_resolution.py
|-- test_rare_plant_exact_location_denial_canaries.py
|-- test_geoprivacy_redaction_receipt_refs.py
|-- test_source_role_fixture_no_upcast.py
|-- test_evidence_fixture_refs_required.py
`-- test_release_fixture_refs_do_not_authorize_publication.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/flora
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no exact sensitive flora locations, no steward-controlled locality data, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal fixture manifest

Synthetic test-local manifests should describe fixture expectations without carrying real Flora data.

```json
{
  "fixture_manifest_id": "flora-test-fixture-manifest-example",
  "domain": "flora",
  "canonical_fixture_ref": "fixtures/domains/flora/valid/example-fixture.json",
  "fixture_family": "public_safe_occurrence",
  "source_role": "observed",
  "sensitivity_posture": "public_safe_synthetic",
  "evidence_ref": "evidence:synthetic:flora:test:example",
  "policy_decision_ref": "policy:synthetic:flora:allow-public-safe-example",
  "redaction_receipt_ref": "receipt:synthetic:flora:redaction:not-required",
  "expected_outcome": "PASS",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, the manifest should make the denial cause explicit:

```json
{
  "fixture_manifest_id": "flora-test-fixture-manifest-deny-sensitive-exact-location",
  "domain": "flora",
  "fixture_family": "rare_plant_exact_location_denial",
  "source_role": "observed",
  "sensitivity_posture": "sensitive_exact_location_synthetic_canary",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SENSITIVE_EXACT_LOCATION_BLOCKED",
    "PUBLIC_GEOMETRY_NOT_ALLOWED"
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
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | Public-safe generalized occurrence fixture loads locally. |
| `ABSTAIN` | The fixture resembles a claim but lacks enough synthetic evidence closure to answer. | Missing EvidenceRef for a claim-like output. |
| `DENY` | Policy, rights, sensitivity, review, release, or exact-geometry checks block exposure. | Synthetic rare-plant exact-location canary. |
| `ERROR` | The fixture or loader is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live source request. |

---

## Public-safe geometry rules

Flora fixture geometry must be intentionally boring and safe.

| Geometry class | Fixture posture |
|---|---|
| Toy point | Allowed only when obviously synthetic and not representing a sensitive real location. |
| Generalized point or grid cell | Preferred for public-safe occurrence examples. |
| County, ecoregion, watershed, or coarse polygon | Appropriate for aggregate/range examples when synthetic and clearly labeled. |
| Exact rare-plant locality | Not allowed. Use a denial canary with fake geometry or no geometry. |
| Steward-controlled locality | Not allowed. Use synthetic placeholders only. |
| Joined sensitive product | Allowed only as a negative test proving the join is denied or generalized. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/flora/` unless there is a test-local reason
- [ ] source role, evidence state, rights state, sensitivity state, policy state, review state, release state, correction state, and expected outcome are explicit where material
- [ ] no real source records, exact sensitive locations, private data, credentials, logs, or public artifacts are present
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
| Add a test-local manifest | Add expected outcome, reason code, canonical fixture ref, and no-network posture. |
| Add a reusable payload | Prefer `fixtures/domains/flora/`; link it here only if tests consume it. |
| Add a negative fixture | State the finite failure outcome and policy/evidence reason. |
| Add a sensitive-geometry case | Use synthetic canaries; do not use real coordinates. |
| Add a new object-family fixture | Confirm the corresponding contract/schema/policy home or mark it PROPOSED. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle, and record the correction path. |

---

## Verification status

- Target README: replaced empty placeholder content.
- Parent test-fixture READMEs: not found at `tests/fixtures/README.md` or `tests/fixtures/domains/README.md` during authoring; this file remains self-contained until parent indexes exist.
- Canonical Flora fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Flora path-register alignment: verified against `docs/domains/flora/CANONICAL_PATHS.md` for the test/fixture lane distinction.
- Contract/schema alignment: NEEDS VERIFICATION per child lane because several object-family schemas may still be draft or PROPOSED.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, source-admission checks, watcher dry-runs, and policy checks.
- Tests and validators: NOT RUN.
