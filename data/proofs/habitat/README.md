<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/proofs/habitat/readme
title: Habitat Proofs README
type: data-lifecycle-readme
version: v0.1
status: draft
owners: <PLACEHOLDER — Data steward · Habitat lane steward · Proof/release steward>
created: 2026-06-25
updated: 2026-06-25
policy_label: internal-planning
intended_path: data/proofs/habitat/README.md
owning_root: data/
lifecycle_area: proofs
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/domains/habitat/README.md
  - docs/domains/fauna/README.md
  - data/receipts/habitat/README.md
  - data/catalog/README.md
  - data/published/habitat/README.md
  - release/manifests/habitat/README.md
  - schemas/contracts/v1/habitat/
  - policy/sensitivity/habitat/
tags: [kfm, data, proofs, habitat, evidence, validation, policy, release, rollback, geoprivacy]
notes:
  - "This README governs the habitat proof lane only; it is not itself a proof object, release decision, or publication manifest."
  - "Implementation depth remains UNKNOWN until verified against the mounted repository, schemas, validators, fixtures, CI, and emitted artifacts."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Proofs

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success?style=flat-square)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-orange?style=flat-square)
![area](https://img.shields.io/badge/data%20area-proofs-blue?style=flat-square)
![domain](https://img.shields.io/badge/domain-habitat-brightgreen?style=flat-square)
![publication](https://img.shields.io/badge/publication-not%20by%20file%20move-critical?style=flat-square)

> **One-line purpose.** `data/proofs/habitat/` stores machine-checkable proof objects that support habitat-domain validation, evidence closure, policy decisions, catalog closure, release review, correction, and rollback.

---

## Mini table of contents

- [1. Scope](#1-scope)
- [2. Directory contract](#2-directory-contract)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Habitat proof responsibilities](#5-habitat-proof-responsibilities)
- [6. Expected object families](#6-expected-object-families)
- [7. Naming and identity](#7-naming-and-identity)
- [8. Minimum proof closure checklist](#8-minimum-proof-closure-checklist)
- [9. Habitat + fauna thin-slice proof pattern](#9-habitat--fauna-thin-slice-proof-pattern)
- [10. Policy and sensitivity posture](#10-policy-and-sensitivity-posture)
- [11. Validation expectations](#11-validation-expectations)
- [12. Promotion, publication, and rollback](#12-promotion-publication-and-rollback)
- [13. Maintenance checklist](#13-maintenance-checklist)
- [14. Open verification backlog](#14-open-verification-backlog)

---

## 1. Scope

This directory is the habitat-domain lane under the KFM proof lifecycle area.

It exists to hold proof artifacts for claims and derived outputs involving habitat patches, land-cover observations, ecological systems, habitat quality, suitability models, connectivity edges, corridors, restoration opportunities, stewardship zones, uncertainty surfaces, and public-safe habitat assignment products.

The proof lane supports review and publication decisions. It does **not** publish anything by itself.

### Truth posture

| Statement | Status |
|---|---:|
| `data/proofs/habitat/` is the intended home for habitat proof artifacts. | **PROPOSED** until verified against the mounted repo and Directory Rules version in force. |
| Habitat proofs must remain downstream of source descriptors, evidence records, validation, policy, and review state. | **CONFIRMED doctrine / PROPOSED lane application**. |
| Existing habitat proof schemas, validators, CI jobs, fixtures, and emitted proof packs are present. | **UNKNOWN** until inspected in a mounted checkout. |

---

## 2. Directory contract

`data/proofs/habitat/` is a responsibility-rooted lane, not a topic bucket.

It answers to:

- the `data/` lifecycle root;
- the `proofs/` lifecycle area;
- the habitat domain lane;
- evidence, validation, policy, release, correction, and rollback governance;
- the KFM rule that promotion is a governed state transition, not a file move.

### Contract summary

| Field | Value |
|---|---|
| Root owner | `data/` lifecycle stewardship |
| Area owner | Proof / release support stewardship |
| Domain lane | Habitat |
| Public exposure | None by direct file path |
| Normal public path | Governed API → released artifact / catalog / EvidenceBundle projection |
| Adjacent lifecycle roots | `data/receipts/`, `data/catalog/`, `data/published/`, `release/` |
| Forbidden shortcut | Direct UI, API, model, or map access to this folder as public truth |

---

## 3. What belongs here

Store proof objects that can be independently inspected, validated, hashed, compared, cited by a release decision, and used for rollback or correction review.

Examples include:

| Proof artifact | Purpose | Status |
|---|---|---:|
| `proofpack.<habitat_object_id>.<run_id>.json` | Bundled proof closure for one habitat object, candidate layer, model run, or derived assignment. | **PROPOSED** |
| `validation-proof.<run_id>.json` | Shows schema, geometry, CRS, temporal, and source-reference validation outcomes. | **PROPOSED** |
| `policy-proof.<run_id>.json` | Records rights, sensitivity, source-role, release-state, and access-decision checks. | **PROPOSED** |
| `evidence-closure-proof.<evidence_bundle_id>.json` | Confirms every material claim has resolvable evidence support. | **PROPOSED** |
| `catalog-closure-proof.<catalog_record_id>.json` | Confirms catalog, provenance, citation, and digest closure before release review. | **PROPOSED** |
| `public-safe-geometry-proof.<artifact_id>.json` | Documents generalization, suppression, precision degradation, or withheld geometry. | **PROPOSED** |
| `model-support-proof.<model_run_id>.json` | Documents suitability/connectivity/model assumptions, inputs, outputs, uncertainty, and limitations. | **PROPOSED** |
| `rollback-proof.<release_candidate_id>.json` | Confirms a rollback target exists and is sufficient before release. | **PROPOSED** |

Proof objects should be small, structured, deterministic where practical, and reproducible from the referenced inputs.

---

## 4. What does not belong here

Do **not** store these in `data/proofs/habitat/`:

| Do not store | Correct home | Reason |
|---|---|---|
| Raw source payloads, downloads, rasters, archives, or source API dumps | `data/raw/habitat/` or `data/raw/<source-family>/` | Raw material must remain in the RAW lifecycle area. |
| Work-in-progress transforms or failed normalization outputs | `data/work/habitat/` or `data/quarantine/habitat/` | Proofs cite work; they are not the work surface. |
| Validated processed habitat objects | `data/processed/habitat/` | Processed objects are source-derived records, not proof records. |
| STAC, DCAT, PROV, or other catalog records | `data/catalog/` | Catalog records have their own lifecycle responsibility. |
| Runtime receipts | `data/receipts/habitat/` | Receipts record runs/actions; proofs support closure and decisions. |
| Release manifests, promotion decisions, rollback cards | `release/` | Release authority belongs to the release responsibility root. |
| Public PMTiles, GeoParquet, GeoJSON, COG, or API payload exports | `data/published/habitat/` | Published artifacts are the released delivery surface. |
| Policy rules | `policy/` | Policy authority does not live inside proof data. |
| Schemas | `schemas/contracts/v1/habitat/` | Schema authority belongs under the schema root. |
| Tests or fixtures | `tests/` and `fixtures/` | Test evidence belongs in test/fixture roots, not in lifecycle data. |

---

## 5. Habitat proof responsibilities

Habitat proofs should answer these questions before a habitat artifact can support a public or semi-public claim:

1. **Source support:** Which source descriptors support this habitat object or derived artifact?
2. **Evidence closure:** Which EvidenceBundle supports each material claim?
3. **Spatial support:** What geometry, CRS, scale, resolution, and generalization rules apply?
4. **Temporal support:** What source, observed, valid, retrieval, release, and correction times matter?
5. **Policy support:** Are rights, terms, sensitivity, geoprivacy, and steward review requirements satisfied?
6. **Validation support:** Which validators passed, failed, abstained, denied, or require review?
7. **Release support:** Which release candidate or manifest cites this proof?
8. **Correction support:** What stale-state, correction, and rollback path exists?

A proof object should be rejected if it cannot identify the source, evidence, policy, validation, and release context it is meant to support.

---

## 6. Expected object families

Habitat proof objects may support, but do not replace, these habitat-domain object families:

| Habitat object family | Proof concern |
|---|---|
| `HabitatPatch` | Boundary support, classification basis, source role, temporal scope, uncertainty. |
| `LandCoverObservation` | Classification system, class code, resolution, source date, retrieval date, transform digest. |
| `EcologicalSystem` | Classification vocabulary, crosswalk support, source authority, uncertainty. |
| `HabitatQualityScore` | Scoring method, input features, weights, uncertainty, reviewer status. |
| `SuitabilityModel` | Model run identity, inputs, assumptions, validation, uncertainty, non-truth warning. |
| `ConnectivityEdge` | Graph method, impedance/cost surface support, corridor assumptions, scale. |
| `Corridor` | Geometry generalization, ecological interpretation limits, source support. |
| `RestorationOpportunity` | Suitability basis, ownership/sensitivity caveats, planning-not-authority posture. |
| `StewardshipZone` | Rights, steward review, access rules, public-safe exposure. |
| `UncertaintySurface` | Method, inputs, resolution, uncertainty semantics, downstream use limits. |
| `OccurrenceHabitatAssignment` | Public-safe occurrence handling, geoprivacy, habitat join method, confidence, withheld precision. |

When a proof references fauna or flora evidence, it must preserve the owning lane and should not collapse fauna/flora claims into habitat authority.

---

## 7. Naming and identity

Use names that are deterministic enough to diff and inspect.

Recommended pattern:

```text
<proof_family>.<domain>.<stable_object_or_candidate_id>.<run_id>.json
```

Examples:

```text
proofpack.habitat.habitat_patch_ks_20091_demo.run_20260625T000000Z.json
validation-proof.habitat.landcover_observation_nlcd2021_demo.run_20260625T000000Z.json
policy-proof.habitat.occurrence_assignment_demo_sensitive_case.run_20260625T000000Z.json
catalog-closure-proof.habitat.layer_candidate_demo.run_20260625T000000Z.json
public-safe-geometry-proof.habitat.occurrence_assignment_demo_sensitive_case.run_20260625T000000Z.json
```

### Identity guidance

A proof record should carry, at minimum:

- `proof_id`
- `proof_family`
- `domain`
- `object_id` or `release_candidate_id`
- `run_id`
- `source_descriptor_ids`
- `evidence_bundle_ids`
- `policy_decision_ids`
- `validation_report_ids`
- `receipt_ids`
- `catalog_record_ids`
- `release_manifest_ids` when applicable
- `input_digests`
- `output_digests`
- `spec_hash`
- `created_at`
- `review_state`
- `status`

Use stable IDs and digests instead of human names wherever the proof must be reproducible.

---

## 8. Minimum proof closure checklist

A habitat proof is not ready to support release review unless all applicable checks are satisfied or explicitly recorded as blocked.

| Check | Required evidence | Outcome if missing |
|---|---|---|
| Source descriptor exists | Source ID, role, rights, citation, update cadence, retrieval time, digest. | **DENY** or **ABSTAIN** |
| EvidenceBundle resolves | Evidence references resolve to inspectable evidence. | **ABSTAIN** |
| Geometry is valid | CRS, geometry type, precision, topology, bounds, and scale are declared. | **DENY** or **REVIEW_REQUIRED** |
| Time is explicit | Source, observed, valid, retrieval, release, and correction times are separated where material. | **ABSTAIN** or **STALE** |
| Sensitivity is checked | Rare species, precise occurrence, stewardship, cultural, or private-location exposure handled. | **DENY** |
| Rights are checked | License, terms, citation, redistribution, and derivative-use posture recorded. | **DENY** |
| Validation report exists | Schema, domain, geometry, temporal, and catalog validations are linked. | **DENY** |
| Receipts exist | Transform, validation, policy, catalog, or release-support run receipts are linked. | **REVIEW_REQUIRED** |
| Catalog closure exists | STAC/DCAT/PROV or KFM catalog closure proof is linked where applicable. | **DENY** |
| Rollback target exists | Rollback target or correction path is linked for release candidates. | **DENY** |

---

## 9. Habitat + fauna thin-slice proof pattern

The safest first habitat proof lane is a fixture-first habitat + fauna assignment slice.

### Proof question

Can KFM prove one public-safe occurrence-to-habitat assignment from source intake through evidence-backed release review without exposing sensitive exact locations?

### Recommended no-network fixture set

| Fixture | Purpose |
|---|---|
| One non-sensitive synthetic occurrence | Demonstrates public-safe assignment. |
| One sensitive synthetic occurrence | Demonstrates exact-geometry denial, precision degradation, or withheld details. |
| One habitat or land-cover context record | Demonstrates habitat classification support. |
| One EvidenceBundle | Demonstrates cite-or-abstain behavior. |
| One ValidationReport | Demonstrates schema and geometry validation. |
| One PolicyDecision | Demonstrates sensitivity and rights checks. |
| One LayerManifest or artifact candidate | Demonstrates map/drawer readiness without release bypass. |
| One ReleaseManifest dry-run reference | Demonstrates promotion support without public publication. |
| One RollbackCard or rollback reference | Demonstrates reversibility. |

### Expected proof outputs

```text
data/proofs/habitat/
  proofpack.habitat.occurrence_assignment_demo_public.<run_id>.json
  proofpack.habitat.occurrence_assignment_demo_sensitive.<run_id>.json
  validation-proof.habitat.occurrence_assignment_demo_public.<run_id>.json
  validation-proof.habitat.occurrence_assignment_demo_sensitive.<run_id>.json
  policy-proof.habitat.occurrence_assignment_demo_public.<run_id>.json
  policy-proof.habitat.occurrence_assignment_demo_sensitive.<run_id>.json
  public-safe-geometry-proof.habitat.occurrence_assignment_demo_sensitive.<run_id>.json
  catalog-closure-proof.habitat.assignment_layer_candidate.<run_id>.json
```

This thin slice should prove governance before live sources such as GBIF, eBird, iNaturalist, KDWP, NatureServe, NLCD, GAP, PAD-US, or other source systems are activated.

---

## 10. Policy and sensitivity posture

Habitat can look low-risk until it is joined with fauna, flora, land ownership, field survey, restoration, rare species, cultural sites, or stewardship data.

Default posture:

- precise sensitive occurrences are **DENY by default** for public exposure;
- uncertain rights are **DENY by default**;
- unsupported habitat assignments **ABSTAIN**;
- model-derived habitat suitability must be labeled as model support, not observed truth;
- habitat + fauna joins are derived artifacts, not canonical species truth;
- public-safe geometry transforms must emit proof and receipt records;
- withheld precision must be visible in steward/review surfaces and safe public drawers where appropriate.

### Sensitive cases

| Case | Default handling |
|---|---|
| Rare or listed species occurrence tied to habitat | Suppress or generalize exact geometry; record withheld precision. |
| Modeled habitat suitability | Label model, inputs, uncertainty, and review state. |
| Critical habitat vs modeled habitat | Keep regulatory, modeled, and interpreted habitat separate. |
| Stewardship or restoration zone | Check rights, access, ownership, sensitivity, and review state. |
| Cross-lane fauna/flora evidence | Preserve owning lane, source role, and EvidenceBundle support. |
| Archaeology/cultural overlap | Defer to stricter cultural sensitivity controls. |

---

## 11. Validation expectations

A validator for this lane should verify at least:

- proof JSON is valid against the relevant schema;
- required IDs and digests are present;
- referenced evidence, receipts, validation reports, policy decisions, and catalog records resolve;
- geometry status is explicit, including CRS and public-safe transform state;
- temporal fields are explicit where material;
- rights and sensitivity decisions are present;
- no proof claims release when no release manifest or promotion decision exists;
- no proof collapses habitat, fauna, flora, hydrology, soil, or hazards ownership;
- no proof treats a map tile, model output, AI answer, graph projection, or summary as root truth.

Recommended validator home:

```text
tools/validators/validate_habitat_proof.py
```

Recommended schema home:

```text
schemas/contracts/v1/habitat/habitat_proof.schema.json
schemas/contracts/v1/habitat/habitat_proofpack.schema.json
```

These paths are **PROPOSED** until verified against the mounted repository and accepted schema-home ADRs.

---

## 12. Promotion, publication, and rollback

A proof can support a promotion decision, but it does not promote anything by existing.

Publication requires a separate governed release path with:

1. evidence closure;
2. validation closure;
3. policy and sensitivity closure;
4. catalog closure;
5. review state;
6. release manifest;
7. rollback target;
8. correction path;
9. stale-state rule;
10. public-safe API or artifact exposure.

### Adjacent artifacts

| Artifact | Expected home | Relationship to this directory |
|---|---|---|
| Run receipts | `data/receipts/habitat/` | Proofs cite receipts; receipts do not live here. |
| Catalog records | `data/catalog/` | Proofs cite catalog closure; catalog records do not live here. |
| Release manifests | `release/manifests/habitat/` | Release manifests cite proofs; manifests do not live here. |
| Published artifacts | `data/published/habitat/` | Published artifacts cite proofs indirectly through release records. |
| Rollback cards | `release/rollback_cards/` or repo-approved rollback home | Proofs may cite rollback targets; rollback authority stays separate. |

---

## 13. Maintenance checklist

Before merging changes in this directory:

- [ ] Confirm the file belongs under `data/proofs/habitat/`, not `data/receipts/`, `data/catalog/`, `release/`, `policy/`, or `schemas/`.
- [ ] Confirm every proof record has stable IDs, digests, and a clear proof family.
- [ ] Confirm no proof object contains raw source payloads or unpublished sensitive details beyond policy-approved internal scope.
- [ ] Confirm source descriptors and EvidenceBundles resolve.
- [ ] Confirm policy decisions are linked and sensitivity outcomes are explicit.
- [ ] Confirm public-safe geometry transforms are recorded when applicable.
- [ ] Confirm release-support proofs cite release candidates without claiming publication.
- [ ] Confirm rollback and correction references exist for release candidates.
- [ ] Confirm generated proof files are reproducible from declared inputs.
- [ ] Record drift in `docs/registers/DRIFT_REGISTER.md` if the live repo structure conflicts with this README.

---

## 14. Open verification backlog

| Item | Evidence needed | Status |
|---|---|---:|
| Confirm `data/proofs/habitat/` exists in the mounted repo. | Repo tree inspection. | **UNKNOWN** |
| Confirm parent `data/proofs/README.md` contract. | Mounted repo file. | **UNKNOWN** |
| Confirm habitat proof schemas. | `schemas/contracts/v1/habitat/` inspection. | **UNKNOWN** |
| Confirm habitat proof validator path. | `tools/validators/` or live validator registry inspection. | **UNKNOWN** |
| Confirm CI validates proof artifacts. | Workflow logs or CI config. | **UNKNOWN** |
| Confirm proof-to-release manifest linkage. | Release dry-run artifact or release manifest fixture. | **UNKNOWN** |
| Confirm sensitive occurrence geoprivacy transform rules. | Policy files, fixtures, review records. | **UNKNOWN** |
| Confirm official source descriptors for habitat/land-cover and habitat-fauna slices. | Source registry files and rights review. | **UNKNOWN** |
| Confirm public-safe Evidence Drawer behavior for withheld precision. | UI fixture, governed API response, test evidence. | **UNKNOWN** |

---

## Maintainer note

This README is intentionally conservative. It keeps habitat proofs inspectable and useful without letting proof files become canonical truth, release authority, catalog records, receipts, or public artifacts. If a future implementation needs a different proof-home shape, record the reason through Directory Rules, ADR, and drift-register discipline before creating a parallel authority path.
