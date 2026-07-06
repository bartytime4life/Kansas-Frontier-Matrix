<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-habitat-readme
title: Habitat Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; habitat-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Habitat domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; habitat; synthetic-only; no-network; public-safe; sensitive-join-aware; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, habitat, synthetic-fixtures, no-network, public-safe, sensitive-joins, geoprivacy, SourceDescriptor, EvidenceRef, EvidenceBundle, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/habitat/README.md
  - ../../../../fixtures/domains/habitat/README.md
  - ../../../../fixtures/domains/habitat/ecoregions/README.md
  - ../../../../fixtures/domains/habitat/golden/README.md
  - ../../../../fixtures/domains/habitat/invalid/README.md
  - ../../../../fixtures/domains/habitat/habitat_fauna_thin_slice/README.md
  - ../../../../fixtures/domains/habitat/land_cover/change_summary/README.md
  - ../../../../fixtures/domains/habitat/land_cover/class_scheme/README.md
  - ../../../../fixtures/domains/habitat/land_cover/crosswalk/README.md
  - ../../../../fixtures/domains/habitat/land_cover/layer_manifest/README.md
  - ../../../../fixtures/domains/habitat/land_cover/model_run/README.md
  - ../../../../fixtures/domains/habitat/land_cover/observation/README.md
  - ../../../../fixtures/domains/habitat/land_cover/uncertainty/README.md
  - ../../../../fixtures/domains/habitat/land_cover/watcher/README.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../../../contracts/domains/habitat/
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/candidates/habitat/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/habitat/README.md."
  - "This lane documents test-local expectations for Habitat fixtures. Canonical reusable Habitat fixtures live under fixtures/domains/habitat/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/README.md or tests/fixtures/domains/README.md during the matching Flora authoring pass; this lane remains self-contained until parent indexes are authored."
  - "Executable tests, fixture payload inventory, test harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat test fixtures

> Test-lane documentation for Habitat fixtures referenced from `tests/fixtures/domains/habitat/`. This path describes how tests may use synthetic fixture material without turning fixture examples into source truth, habitat truth, species-occurrence truth, catalog truth, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: test fixtures" src="https://img.shields.io/badge/lane-test__fixtures-purple">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-green">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not truth" src="https://img.shields.io/badge/boundary-fixtures__not__truth-success">
</p>

**Path:** `tests/fixtures/domains/habitat/README.md`  
**Status:** draft / empty placeholder replaced / Habitat test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/habitat`  
**Canonical reusable fixture root:** `fixtures/domains/habitat/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED canonical Habitat fixture README exists under `fixtures/domains/habitat/`; CONFIRMED Habitat canonical path guidance places reusable fixture proof under `fixtures/domains/habitat/` and Habitat domain tests under `tests/domains/habitat/`; NEEDS VERIFICATION for executable tests, fixture payload inventory, fixture schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/habitat/` is a test-local documentation lane for Habitat fixture expectations.

This lane should explain how test code may reference, mirror, stub, or locally constrain Habitat fixture material while preserving the authority of the canonical fixture root. It can describe test-only fixture behavior, expected fixture families, validation expectations, negative cases, no-network posture, public-safe geometry rules, sensitive Habitat × Flora/Fauna join denial cases, and safe-output behavior.

A fixture used from this lane should not mean that a Habitat claim is true, an ecological system has been verified, a modeled surface has been accepted, a land-cover observation has been admitted, a sensitive join is safe, a catalog record is closed, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Test-local Habitat fixture expectations | `tests/fixtures/domains/habitat/` | This directory. |
| Reusable Habitat fixtures | `fixtures/domains/habitat/` | Canonical fixture root; referenced, not replaced. |
| Habitat domain tests | `tests/domains/habitat/` | Consumers and validators; not fixture authority. |
| Semantic contracts | `contracts/domains/habitat/` | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/habitat/` | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/habitat/` and `policy/sensitivity/habitat/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, and sensitivity records; not owned here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second fixture root unless a parent README or ADR explicitly allows test-local copies. Prefer references to `fixtures/domains/habitat/` for reusable fixture payloads.

---

## Invariant under test

> **Habitat fixtures are synthetic bounded examples, not Habitat truth.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/habitat/`; test-local copies require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake identifiers, mock markers, minimized geometry, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, map services, release services, public APIs, or AI runtimes. | `ERROR`. |
| Sensitive-join boundary | Habitat × Fauna and Habitat × Flora exact-occurrence joins fail closed unless a synthetic redaction/generalization path is explicitly being tested. | `DENY` / `ABSTAIN`. |
| Geoprivacy boundary | Public habitat-context fixtures use generalized, binned, withheld, or clearly synthetic geometry where sensitivity matters. | `DENY` / validation failure. |
| Source-role boundary | Regulatory critical habitat, observed land cover, modeled habitat, context layers, and synthetic examples stay distinct. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claim-like fixtures include EvidenceRef expectations or explicitly mark evidence as out of scope. | `ABSTAIN`. |
| Receipt boundary | Redaction, validation, model-run, correction, withdrawal, and rollback refs are explicit where material. | validation failure. |
| Policy boundary | Rights, sensitivity, precision, source-license, steward-review, and release blockers fail closed in negative fixtures. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected fixture-test families

| Family | Purpose | Boundary |
|---|---|---|
| Valid fixture smoke checks | Prove known-good synthetic fixture envelopes satisfy expected shape. | Valid fixture is not true Habitat data. |
| Invalid fixture checks | Prove malformed, ambiguous, unsafe, or unsupported examples fail for finite reasons. | Negative examples are not production incidents. |
| No-network fixture checks | Prove fixture loading is local and deterministic. | No live connectors by default. |
| Habitat patch checks | Prove `HabitatPatch` examples preserve extent, source role, evidence refs, and public-safe geometry. | Patch fixture is not official habitat mapping. |
| Land-cover observation checks | Prove land-cover examples keep class scheme, observation/model status, and time context explicit. | Land-cover fixture is not source authority. |
| Ecoregion context checks | Prove ecoregion examples are contextual boundaries, not habitat truth by themselves. | Context is not ownership transfer. |
| Suitability model checks | Prove modeled outputs remain labeled as modeled and do not replace observed or regulatory records. | Model fixture is not observation truth. |
| Connectivity and corridor checks | Prove synthetic edge/corridor examples preserve uncertainty, method, and review posture. | Corridor fixture is not release approval. |
| Habitat × Fauna thin-slice checks | Prove public-safe occurrence-to-habitat assignment works only through redacted/generalized inputs. | Restricted occurrences never cross. |
| Habitat × Flora join-denial checks | Prove rare-plant/exact-location habitat joins deny, abstain, or require a transform receipt. | No real sensitive locations. |
| Evidence and receipt checks | Prove EvidenceRef, redaction receipt, validation receipt, and model-run receipt expectations are present where material. | Fixture refs are synthetic. |
| Runtime envelope checks | Prove ANSWER / ABSTAIN / DENY / ERROR cases remain finite and policy-aware. | Runtime shape is not release approval. |
| Cross-lane context checks | Prove Soil, Hydrology, Hazards, Agriculture, Flora, Fauna, Roads, Settlements, Archaeology, and People/Land refs remain external authority. | Context is not ownership transfer. |

---

## Relationship to canonical Habitat fixtures

The canonical Habitat fixture root documents reusable fixture lanes for ecoregions, golden, invalid, Habitat × Fauna thin slice, land-cover change summary, class scheme, crosswalk, layer manifest, model run, observation, uncertainty, watcher, and related expected-output examples.

This `tests/fixtures/...` lane should therefore avoid duplicating those payloads. It should instead document how tests consume them, what local wrappers may exist, and what safety checks must run before fixture material is accepted by test code.

| Question | Preferred answer |
|---|---|
| Need a reusable fixture payload? | Put it under `fixtures/domains/habitat/`. |
| Need a test-only wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source/lifecycle roots. |
| Need policy or schema authority? | Do not put it here. Use policy or schema roots. |
| Need release authority? | Do not put it here. Use release roots. |
| Need sensitive exact occurrence joins? | Do not put them in public, fixture, or test-local material; use synthetic denial canaries or generalized transform examples. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Habitat fixtures under `fixtures/domains/habitat/`
- test-local fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RedactionReceipt`, `ModelRunReceipt`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, `HabitatQualityScore`, `SuitabilityModel`, `ConnectivityEdge`, `Corridor`, `RestorationOpportunity`, `StewardshipZone`, and `UncertaintySurface` examples
- synthetic ecoregion, class scheme, crosswalk, layer manifest, watcher, valid, invalid, denied, abstention, correction, withdrawal, stale-state, and rollback cases
- canary values that make source-role collapse, exact-location leakage, sensitive-join exposure, model-vs-observation collapse, regulatory-vs-modeled flattening, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, source role, evidence ref, policy decision ID, redaction receipt ref, validation receipt ref, model-run receipt ref, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, or runtime outputs | Bypasses the trust membrane. |
| Exact species occurrence coordinates, rare-plant locations, nest/den/roost/hibernacula/spawning sites, culturally sensitive habitat context, or private property/person joins | Sensitive and rights-limited material must fail closed. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/domains/habitat/
|-- README.md
|-- manifest_expectations.json
|-- test_fixture_manifest_shape.py
|-- test_no_network_fixture_loading.py
|-- test_land_cover_fixture_source_role_no_upcast.py
|-- test_sensitive_join_denial_canaries.py
|-- test_geoprivacy_redaction_receipt_refs.py
|-- test_model_vs_observation_fixture_labels.py
|-- test_evidence_fixture_refs_required.py
`-- test_release_fixture_refs_do_not_authorize_publication.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/habitat
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no exact sensitive occurrence locations, no steward-controlled locality data, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal fixture manifest

Synthetic test-local manifests should describe fixture expectations without carrying real Habitat data.

```json
{
  "fixture_manifest_id": "habitat-test-fixture-manifest-example",
  "domain": "habitat",
  "canonical_fixture_ref": "fixtures/domains/habitat/land_cover/observation/example-fixture.json",
  "fixture_family": "public_safe_land_cover_observation",
  "source_role": "observed",
  "sensitivity_posture": "public_safe_synthetic",
  "evidence_ref": "evidence:synthetic:habitat:test:example",
  "policy_decision_ref": "policy:synthetic:habitat:allow-public-safe-example",
  "redaction_receipt_ref": "receipt:synthetic:habitat:redaction:not-required",
  "expected_outcome": "PASS",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, the manifest should make the denial cause explicit:

```json
{
  "fixture_manifest_id": "habitat-test-fixture-manifest-deny-sensitive-join",
  "domain": "habitat",
  "fixture_family": "sensitive_occurrence_habitat_join_denial",
  "source_role": "observed",
  "sensitivity_posture": "sensitive_join_synthetic_canary",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SENSITIVE_JOIN_BLOCKED",
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
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | Public-safe land-cover observation fixture loads locally. |
| `ABSTAIN` | The fixture resembles a claim but lacks enough synthetic evidence closure to answer. | Missing EvidenceRef for a claim-like habitat assignment. |
| `DENY` | Policy, rights, sensitivity, review, release, or exact-geometry checks block exposure. | Synthetic sensitive occurrence × habitat join canary. |
| `ERROR` | The fixture or loader is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live source request. |

---

## Public-safe geometry rules

Habitat fixture geometry must be intentionally boring and safe.

| Geometry class | Fixture posture |
|---|---|
| Toy polygon | Allowed only when obviously synthetic and not representing a sensitive real location. |
| Generalized polygon, grid cell, or buffered coarse area | Preferred for public-safe habitat and land-cover examples. |
| Ecoregion, watershed, county, or coarse context area | Appropriate for context/range examples when synthetic and clearly labeled. |
| Exact species occurrence × habitat overlay | Not allowed as a positive fixture. Use a denial canary or generalized transform example. |
| Rare plant, nest, den, roost, hibernacula, spawning, or culturally sensitive locality | Not allowed. Use synthetic placeholders only. |
| Joined sensitive product | Allowed only as a negative test proving the join is denied or generalized. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/habitat/` unless there is a test-local reason
- [ ] source role, evidence state, rights state, sensitivity state, policy state, review state, release state, correction state, rollback state, and expected outcome are explicit where material
- [ ] modeled habitat, observed land cover, regulatory critical habitat, and synthetic examples are not flattened into one source role
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
| Add a reusable payload | Prefer `fixtures/domains/habitat/`; link it here only if tests consume it. |
| Add a negative fixture | State the finite failure outcome and policy/evidence reason. |
| Add a sensitive-join case | Use synthetic canaries; do not use real coordinates. |
| Add a new object-family fixture | Confirm the corresponding contract/schema/policy home or mark it PROPOSED. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle, and record the correction path. |

---

## Verification status

- Target README: replaced empty placeholder content.
- Parent test-fixture READMEs: not verified during this update; this file remains self-contained until parent indexes exist.
- Canonical Habitat fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Habitat path-register alignment: verified against `docs/domains/habitat/CANONICAL_PATHS.md` for the fixture/test lane distinction and sensitive-join posture.
- Contract/schema alignment: NEEDS VERIFICATION per child lane because several object-family schemas may still be draft or PROPOSED.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, source-role checks, context-join checks, watcher dry-runs, proof checks, pipeline dry-runs, and policy checks.
- Tests and validators: NOT RUN.
