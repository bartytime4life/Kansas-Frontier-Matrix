<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-land-cover-readme
title: pipeline_specs/habitat/land_cover/ — Governed Habitat Land-Cover Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; permissive-schema-scaffolds-present; no-active-land-cover-spec-established
owners: OWNER_TBD — Pipeline-spec steward · Habitat steward · Land-cover steward · Source/rights steward · Native-classification/crosswalk steward · Raster/CRS steward · Sensitive-join reviewer · Consumer owner · Validation/evidence/policy/release stewards · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; habitat; land-cover; declarative-only; source-role-aware; native-classification-preserving; crosswalk-advisory; raster-aware; time-aware; model-aware; rights-aware; join-sensitivity-aware; no-secrets; no-live-activation; no-direct-lifecycle-write; no-release-authority
current_path: pipeline_specs/habitat/land_cover/README.md
truth_posture: CONFIRMED current target and prior blob, README-only direct lane in bounded indexed search, absent flat pipeline_specs/habitat/land_cover.yaml path, draft pipeline/config/contract/test/fixture/receipt/processed/published documentation, five nested and one flat permissive PROPOSED land-cover schema scaffolds, unresolved nested/flat contract-schema authority, subtype-first/domain-first source-registry conflict, two PROPOSED NLCD registry placeholders, README-only duplicate NLCD connector boundaries, broad Habitat policy scaffold, absent land-cover and Habitat sensitivity policy READMEs, index-only Habitat validator lane, TODO-only Habitat workflow, and placeholder CODEOWNERS / PROPOSED minimum active-spec contract, finite status/outcome vocabularies, deterministic parser/consumer binding, source/class/epoch/raster/crosswalk/model/uncertainty/join gates, activation/deactivation discipline, validation, correction, and rollback requirements / UNKNOWN accepted land-cover spec schema, parser, registry, scheduler, activation records, executable consumers, runtime behavior, substantive CI, emitted receipts, proof/catalog/release closure, deployed schedules, and public use / NEEDS VERIFICATION owners, exhaustive inventory, canonical source/connector and contract/schema topology, source-role mapping, admitted sources, rights, class-scheme and crosswalk authority, temporal/raster/materiality profiles, field-level policy, public allowlists, fixtures, tests, validators, invalidation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2ad80d6362541db0d1933fe729e9a552f7aa19a9
  prior_blob: c3683a2a549556159cc581ac2fd641bd7453f9fe
  direct_lane_files:
    - pipeline_specs/habitat/land_cover/README.md
  direct_lane_posture: README-only in bounded indexed search; no active child profile established
  schema_posture: five nested and one flat PROPOSED permissive schema scaffolds observed; none provides field-level enforcement
  workflow_posture: domain-habitat is pull-request-triggered TODO scaffolding
related:
  - ../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../pipelines/domains/habitat/land_cover/README.md
  - ../../../configs/domains/habitat/README.md
  - ../../../contracts/domains/habitat/land_cover/
  - ../../../contracts/domains/habitat/land_cover_observation.md
  - ../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json
  - ../../../data/registry/sources/habitat/README.md
  - ../../../data/registry/sources/habitat/nlcd.yaml
  - ../../../data/registry/habitat/sources/nlcd.yaml
  - ../../../connectors/nlcd/README.md
  - ../../../data/receipts/habitat/land_cover/README.md
  - ../../../data/processed/habitat/land_cover/README.md
  - ../../../data/published/layers/habitat/land_cover/README.md
  - ../../../tests/domains/habitat/land_cover/README.md
  - ../../../fixtures/domains/habitat/land_cover/observation/README.md
  - ../../../tools/validators/domains/habitat/README.md
  - ../../../policy/domains/habitat/README.md
  - ../../../.github/workflows/domain-habitat.yml
  - ../../../.github/CODEOWNERS
notes:
  - "v0.2 replaces the planning-only proposed file tree with commit-pinned repository evidence and classifies the direct specification lane as README-only."
  - "The flat pipeline_specs/habitat/land_cover.yaml path referenced by executable documentation was not present at the evidence snapshot."
  - "All six inspected land-cover schema surfaces are permissive PROPOSED scaffolds with empty properties and additionalProperties=true."
  - "No source, specification, parser, consumer, schedule, pipeline, policy, lifecycle object, receipt instance, proof, catalog object, release object, or public artifact is activated or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Habitat Land-Cover Pipeline Specification Boundary

`pipeline_specs/habitat/land_cover/`

> Declarative run-intent boundary for Habitat land-cover processing. A reviewed active specification may state **what** a verified consumer should process, against which admitted sources and class schemes, under which source-role, epoch, time, raster, CRS, crosswalk, uncertainty, evidence, sensitivity, policy, receipt, review, correction, and release gates. It does not execute a pipeline, activate a source, silently recode classes, create evidence, decide Habitat truth, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-README--only-lightgrey)
![schemas](https://img.shields.io/badge/schemas-permissive__scaffolds-orange)
![crosswalk](https://img.shields.io/badge/crosswalk-advisory__only-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Status](#current-status) · [Placement](#repository-fit) · [Authority](#authority-and-anti-collapse) · [Families](#profile-and-object-family-boundaries) · [Contract](#minimum-active-specification-contract) · [Example](#illustrative-inactive-profile) · [Sources](#sources-rights-and-source-roles) · [Classes](#native-classification-and-crosswalks) · [Time](#time-vintage-and-change) · [Raster](#raster-crs-grid-and-valid-pixel-support) · [Sensitivity](#sensitivity-and-reconstruction-risk) · [Lifecycle](#lifecycle-and-finite-outcomes) · [Evidence](#evidence-receipts-proof-catalog-and-release) · [Validation](#validation-and-enforceability) · [Done](#definition-of-done) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@2ad80d6362541db0d1933fe729e9a552f7aa19a9`  
> **Prior target blob:** `c3683a2a549556159cc581ac2fd641bd7453f9fe`  
> **Direct lane:** this README only in bounded indexed search  
> **Active specifications:** none established  
> **Referenced flat spec:** `pipeline_specs/habitat/land_cover.yaml` was not present at the exact checked path  
> **Activation:** filename, merge state, syntax validity, permissive-schema acceptance, fixture prose, schedule text, source placeholder presence, map rendering, or a successful dry run activates nothing

> [!CAUTION]
> A land-cover specification cannot turn a source classification into field observation, a crosswalk into authority, a modeled pixel into direct measurement, CDL into Habitat crop truth, NWI into a regulatory wetland determination, LANDFIRE into a current hazard decision, land cover into species occurrence, a processed raster into a released public layer, or generated language into evidence. Missing source role, rights, epoch, class scheme, crosswalk loss, CRS, mask, valid-pixel support, uncertainty, evidence, policy, review, correction, rollback, or release state fails closed.

---

<a id="purpose"></a>

## Purpose

This lane may eventually hold small, reviewed, deterministic profiles that bind:

- stable specification identity, version, digest, ownership, status, and supersession;
- one accepted parser and one verified executable consumer;
- admitted `SourceDescriptor` references and activation records;
- product, sub-product, release/collection, source epoch, and source-head identity;
- native class-scheme identity, version, class-map digest, nodata, unknown, and reserved codes;
- directional, versioned, loss-aware crosswalk references;
- source, observation, valid, retrieval, processing, release, correction, and supersession times;
- source/analysis/tiling CRS, grid, resolution, transform, extent, mask, nodata, resampling, and valid-pixel support;
- observed, modeled, aggregate, administrative, candidate, synthetic, crosswalk-derived, and public-derivative knowledge character;
- lifecycle input/output states;
- sensitive-join and public-attribute allowlist requirements;
- validation, evidence, receipts, proof, catalog, review, policy, release, correction, invalidation, and rollback gates;
- deterministic no-network tests, finite outcomes, idempotency, and replay expectations.

This README is not a schema, parser, scheduler, activation decision, connector, pipeline, source descriptor, class-map authority, crosswalk, contract, policy decision, raster transform, receipt, proof, catalog record, release record, public API, map layer, tile set, search index, graph projection, or generated answer.

[Back to top](#top)

---

<a id="current-status"></a>

## Current status

### Repository maturity matrix

| Surface | Current evidence | Status | Safe conclusion |
|---|---|---:|---|
| Direct spec lane | Bounded search surfaced this README only. | **CONFIRMED / search-limited** | No active child profile is established. |
| Flat spec reference | `pipeline_specs/habitat/land_cover.yaml` returned `Not Found`. | **CONFIRMED exact absence** | Executable docs contain a stale or future path. |
| Parent Habitat specs | Draft README. | **CONFIRMED draft** | Parent prose does not activate this lane. |
| Executable pipeline | Detailed draft README. | **CONFIRMED docs; behavior NEEDS VERIFICATION** | No runnable consumer or schedule is established. |
| Habitat config | README plus empty `.gitkeep`; no indexed consumer. | **CONFIRMED README-only** | No loader, precedence, or binding is established. |
| Nested contracts | Observation, class scheme, crosswalk, change summary, uncertainty, model-run receipt. | **CONFIRMED drafts** | Meaning is documented; runtime enforcement is not proven. |
| Flat compatibility contracts | Parallel land-cover observation surfaces are indexed. | **CONFLICTED / NEEDS VERIFICATION** | Canonical naming and path ownership remain unresolved. |
| Nested schema index | Draft and apparently incomplete. | **CONFIRMED draft** | Its inventory is not sufficient evidence of full current shape. |
| Nested schemas | Five `PROPOSED` schemas with empty properties and `additionalProperties: true`. | **CONFIRMED permissive scaffolds** | No field-level enforcement. |
| Flat observation schema | Separate permissive compatibility schema. | **CONFIRMED scaffold / CONFLICTED authority** | Duplicate `$id`, title, and contract-path posture need resolution. |
| Source registry | Subtype-first parent and domain-first sibling. | **CONFIRMED topology conflict** | Do not duplicate admission authority. |
| NLCD registry records | One seven-line placeholder and one legacy-role template. | **CONFIRMED placeholders** | Neither is admitted or active. |
| NLCD connector | README-only duplicate connector boundaries. | **CONFIRMED documentation; placement open** | No runnable connector or source activation is proven. |
| Policy | Generic Habitat greenfield scaffold. | **CONFIRMED scaffold** | No field-level land-cover policy is established. |
| Sensitivity policy | Expected Habitat sensitivity README not found. | **CONFIRMED exact absence** | Join-sensitivity enforcement is not established. |
| Validators | Habitat index with no land-cover child confirmed. | **CONFIRMED index-only** | No executable land-cover validator is established. |
| Tests | Parent and child README hierarchy. | **CONFIRMED documentation** | Executable modules and pass rates remain unverified. |
| Fixtures | Child fixture READMEs; no parent README or payload inventory established. | **PARTIALLY CONFIRMED** | Fixture prose is not payload or regression evidence. |
| Receipts | Dedicated land-cover receipt README. | **CONFIRMED draft** | No emitted receipt instances; exact layout unresolved. |
| Processed data | Draft processed-lane README. | **CONFIRMED documentation** | No payload inventory or public authority. |
| Catalog child | No dedicated land-cover child surfaced in bounded search. | **NOT OBSERVED / search-limited** | Do not invent a child catalog home. |
| Release-candidate child | No dedicated child surfaced in bounded search. | **NOT OBSERVED / search-limited** | Use verified parent release lanes until placement is accepted. |
| Published layer | Draft public-layer README. | **CONFIRMED documentation** | File presence does not prove released bytes or manifests. |
| CI | Three `echo TODO` Habitat jobs. | **CONFIRMED scaffold-only** | Green status is not land-cover enforcement. |
| Ownership | Generic placeholder CODEOWNERS. | **CONFIRMED placeholder** | Land-cover review is not repository-enforced. |
| Runtime/public use | No activation or deployment evidence in bounded searches. | **UNKNOWN** | Assume inactive and non-public. |

### Bottom line

The lane is documentation-only at the inspected snapshot. Implementation-shaped contracts and schemas exist, but the schemas are permissive scaffolds and the repository does not establish an active spec, parser, consumer, admitted source, field-level policy, executable validator, receipt chain, proof/catalog closure, release decision, or public deployment.

[Back to top](#top)

---

<a id="repository-fit"></a>

## Repository fit

Directory Rules assigns files by responsibility:

| Responsibility | Verified or candidate home | Boundary |
|---|---|---|
| Declarative land-cover run intent | `pipeline_specs/habitat/land_cover/` | This lane; currently README-only. |
| Executable processing | `pipelines/domains/habitat/land_cover/` | **How**, not declarative authority. |
| Safe configuration support | `configs/domains/habitat/` | README-only; no consumer binding established. |
| Semantic meaning | `contracts/domains/habitat/land_cover/` and compatibility surfaces | Draft; canonical path/naming unresolved. |
| Machine shape | `schemas/contracts/v1/domains/habitat/land_cover/` and compatibility schema | Draft permissive scaffolds; authority unresolved. |
| Source admission | `data/registry/sources/habitat/` or topology-resolved registry | Source metadata and activation, not payloads. |
| Source retrieval | `connectors/<source-or-family>/` | May admit to RAW/QUARANTINE only. |
| Policy | `policy/domains/habitat/` and accepted sensitivity roots | No field-level land-cover policy established. |
| Tests | `tests/domains/habitat/land_cover/` | Correct verified test documentation home. |
| Fixtures | Child lanes under `fixtures/domains/habitat/land_cover/` | Payload inventory and consumers unverified. |
| Receipts | `data/receipts/habitat/land_cover/` | Process memory, not proof or release. |
| Processed artifacts | `data/processed/habitat/land_cover/` | PROCESSED only; not public. |
| Proof | `data/proofs/habitat/` or accepted proof lanes | Evidence support; implementation unverified. |
| Catalog | Verified Habitat catalog parents or ADR-resolved child | No child home should be invented here. |
| Release review | Verified Habitat release parents | No child home should be invented here. |
| Public land-cover bytes | `data/published/layers/habitat/land_cover/` | Released public-safe artifacts only. |
| Generated-work provenance | `data/receipts/generated/` | Per-artifact authorship receipt, not run evidence. |

### Corrected v0.1 paths

Use:

```text
tests/domains/habitat/land_cover/
fixtures/domains/habitat/land_cover/<verified-child>/
data/receipts/habitat/land_cover/
```

Do not present these stale planning paths as current facts:

```text
tests/pipeline_specs/habitat/land_cover/
fixtures/pipeline_specs/habitat/land_cover/
data/receipts/pipeline/habitat/land_cover/
```

The dedicated receipt child exists, but its README contains stale prose about the parent Habitat receipt README and explicitly leaves final subtype layout unresolved. Reconcile that documentation before treating the child layout as canonical.

[Back to top](#top)

---

<a id="authority-and-anti-collapse"></a>

## Authority and anti-collapse

An active specification may declare requested processing and gates. It cannot decide:

- source admission, activation, authority, currency, or rights clearance;
- canonical source-role mapping;
- connector topology;
- native class meaning or equivalence;
- that a crosswalk is lossless, reversible, symmetric, or authoritative;
- that a modeled classification is direct observation;
- that a source raster proves HabitatPatch quality, suitability, restoration priority, species occurrence, crop truth, soil truth, hydrology truth, hazard state, regulatory status, land title, or management suitability;
- that geometry or attributes are public-safe;
- that evidence, policy, review, proof, catalog closure, or release approval exists;
- that published bytes are valid merely because they are present.

Required distinctions:

```text
pipeline spec                 != executable pipeline
source descriptor             != source payload
source product                != LandCoverObservation
native class scheme           != crosswalk
crosswalk                     != silent recode
modeled classification        != direct field measurement
LandCoverObservation          != HabitatPatch
land-cover context            != species or plant occurrence
CDL adjacency                 != Habitat crop truth
NWI context                   != jurisdictional wetland determination
LANDFIRE context              != current hazard decision
processed artifact            != catalog closure
catalog record                != release approval
receipt                       != proof
published bytes               != proof by file presence
generated language            != evidence
```

[Back to top](#top)

---

<a id="profile-and-object-family-boundaries"></a>

## Profile and object-family boundaries

| Family | Meaning | Must remain separate from |
|---|---|---|
| `LandCoverObservation` | Source-role-aware classification over declared space and time. | Scheme, crosswalk, patch, model receipt, release. |
| `ClassSchemeProfile` | Versioned native vocabulary and class inventory. | Observation or crosswalk. |
| `CoverClassCrosswalk` | Directional mapping between scheme versions/families. | Native source authority. |
| `LandCoverChangeSummary` | Derived comparison over declared analysis support. | Source observations and current-condition truth. |
| `UncertaintySurface` | Accuracy, confidence, valid-pixel, model, vintage, or mapping uncertainty. | Proof that classes are correct. |
| `ModelRunReceipt` | Process memory for modeled/derived execution. | Evidence closure, observation truth, release. |
| Watcher result | Source-head comparison and proposed-work/no-op signal. | Activation, ingestion, promotion, publication. |
| Layer descriptor/manifest | Carrier metadata for candidate or released artifact. | Source truth, proof, release approval. |
| Published artifact | Release-approved public-safe bytes. | Canonical source or EvidenceBundle authority. |

Candidate source-family profiles such as NLCD, LANDFIRE, GAP, NWI context, remote-sensing products, steward inventories, or Agriculture-owned CDL adjacency are **not current files**. Create them only after source, parser, consumer, rights, class-map, policy, test, and activation gates are verified.

[Back to top](#top)

---

<a id="minimum-active-specification-contract"></a>

## Minimum active-specification contract

A child profile must not become `ACTIVE` until all applicable fields have accepted representations and enforceable validation.

### Identity and binding

- stable `spec_id`, version, digest, owner, status, and supersession lineage;
- accepted spec schema `$id` and version;
- parser ID/version;
- exact executable consumer ID/version;
- accepted discovery and precedence rule;
- separate activation record with effective/expiry/review times;
- correction and rollback target.

### Source and product

- authoritative `SourceDescriptor` reference and revision;
- source activation reference;
- canonical source role;
- product, sub-product, release/collection, epoch, and source-head identity;
- rights, attribution, redistribution, derivative-use, access, cadence, and authority limits;
- withdrawal, supersession, and correction references.

### Classification

- native class-scheme ID/version and class-map digest;
- native codes, labels, hierarchy, nodata, unknown, unclassified, reserved, and deprecated values;
- explicit preservation of native classes downstream;
- crosswalk ID/version/digest, source/target schemes, direction, mapping type, coverage, loss, uncertainty, evidence, reviewers, allowed uses, correction, and rollback.

### Raster, vector, and time

- source/analysis/tiling CRS;
- dimensions, bands, data type, transform, resolution, grid origin/alignment, extent, and footprint;
- nodata, mask, quality/cloud rules, and valid-pixel support;
- resampling/reprojection method and category-preserving behavior;
- source, acquisition/observation, valid, retrieval, processing, release, correction, and supersession times;
- freshness and materiality profile references.

### Knowledge character and governance

- source-native, observed, modeled, aggregate, administrative, candidate, synthetic, crosswalk-derived, summary-derived, or public-derivative labels;
- allowed input and expected output lifecycle states;
- evidence, validation, policy, review, receipt, proof, catalog, release, correction, invalidation, and rollback requirements;
- sensitive-join and public attribute/geometry allowlist references;
- deterministic no-network fixtures, finite outcomes, idempotency, and replay expectations;
- bounded resource, network, logging, error, and secret-handling behavior.

[Back to top](#top)

---

<a id="illustrative-inactive-profile"></a>

## Illustrative inactive profile

This example is incomplete, non-canonical, and intentionally inactive.

```yaml
schema_ref: kfm.pipeline_spec.habitat.land_cover.NEEDS_VERIFICATION
spec_id: habitat.land_cover.example_inactive
version: 0.0.0
status: DRAFT
activation:
  active: false
  activation_record_ref: null
parser_binding:
  parser_id: NEEDS_VERIFICATION
  parser_version: NEEDS_VERIFICATION
consumer_binding:
  consumer_id: NEEDS_VERIFICATION
  consumer_version: NEEDS_VERIFICATION
sources:
  - source_descriptor_ref: NEEDS_VERIFICATION
    source_activation_ref: NEEDS_VERIFICATION
    source_role: NEEDS_VERIFICATION
    product_ref: NEEDS_VERIFICATION
    source_epoch: NEEDS_VERIFICATION
classification:
  native_scheme_ref: NEEDS_VERIFICATION
  native_scheme_version: NEEDS_VERIFICATION
  preserve_native_classes: true
  crosswalk_ref: null
spatial:
  source_crs: NEEDS_VERIFICATION
  analysis_crs: NEEDS_VERIFICATION
  grid_profile_ref: NEEDS_VERIFICATION
  valid_pixel_profile_ref: NEEDS_VERIFICATION
temporal:
  source_vintage: NEEDS_VERIFICATION
  valid_time: NEEDS_VERIFICATION
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  no_direct_public_write: true
  evidence_bundle_required: true
  policy_decision_required: true
  correction_path_required: true
  rollback_target_required: true
outcome_on_unresolved_gate: NEEDS_REVIEW
```

A validator should reject or hold this profile because required references remain unresolved.

[Back to top](#top)

---

<a id="sources-rights-and-source-roles"></a>

## Sources, rights, and source roles

Current Habitat source-registry evidence contains both:

```text
data/registry/sources/habitat/
data/registry/habitat/sources/
```

Use one reviewed authoritative descriptor, not divergent copies.

New Habitat registry documentation uses:

```text
observed
regulatory
modeled
aggregate
administrative
candidate
synthetic
```

Older templates use words such as `primary`, `corroborating`, `context`, `restricted`, `authority`, or `derived`. A profile must reference an accepted mapping decision or fail validation. It must not copy a legacy word into an active role field by convenience.

### NLCD boundary

Current evidence shows:

- duplicate README-only connector boundaries;
- no proven executable connector;
- no activated source-authority entry;
- one seven-line subtype-first source placeholder;
- one domain-first template using legacy roles;
- connector doctrine treating NLCD pixels as modeled/classifier-assigned values rather than direct field measurements.

An NLCD-named spec remains inactive until source identity, role, rights, product/release/epoch, class map, parser, consumer, and activation are separately resolved.

[Back to top](#top)

---

<a id="native-classification-and-crosswalks"></a>

## Native classification and crosswalks

### Native-first invariant

Every source-derived record must preserve:

- source product and epoch;
- native scheme ID/version;
- native code and label;
- native hierarchy/grouping;
- nodata, unknown, unclassified, reserved, and deprecated semantics;
- class-map artifact and digest;
- source caveats;
- original knowledge character.

A harmonized class is additional derived state, not a replacement.

### Crosswalk rules

A crosswalk is directional:

```text
scheme A -> scheme B
```

This does not imply `scheme B -> scheme A`.

Each mapping must declare whether it is one-to-one, one-to-many, many-to-one, partial, conditional, probabilistic, aggregate, unmapped, unknown, reserved/nodata, or denied for the requested use.

Required controls:

- source and target schemes/versions;
- crosswalk version/digest;
- class coverage and unmapped handling;
- loss and uncertainty;
- method and evidence;
- reviewer and policy references;
- permitted and prohibited uses;
- correction and rollback.

A mapping accepted for internal comparison is not automatically acceptable for public tiles, exports, Focus Mode, generated summaries, or governed APIs.

[Back to top](#top)

---

<a id="time-vintage-and-change"></a>

## Time, vintage, and change

Keep distinct:

| Time | Meaning |
|---|---|
| Source vintage | Product release, edition, year, or source-defined temporal identity. |
| Acquisition/observation time | When source observations were collected. |
| Valid time | Period represented by the classification. |
| Retrieval time | When KFM obtained source material. |
| Processing time | When a pipeline transformed it. |
| Release time | When a governed public release became effective. |
| Correction time | When a correction was issued. |
| Supersession time | When a reviewed replacement took effect. |

A recent retrieval is not freshness proof. Freshness requires source-head comparison and an accepted staleness profile.

A `LandCoverChangeSummary` must bind compatible observations, schemes/crosswalks, grids, extents, masks, resolutions, time windows, materiality profile, evidence, review, correction, and rollback. Change/no-change must remain distinct from uncertainty and classification disagreement.

[Back to top](#top)

---

<a id="raster-crs-grid-and-valid-pixel-support"></a>

## Raster, CRS, grid, and valid-pixel support

An active profile must preserve:

- width, height, bands, data types, and band semantics;
- CRS and axis/order assumptions;
- affine transform, pixel size, grid origin/alignment, bounds, and footprint;
- source resolution and analysis support;
- nodata and mask semantics;
- cloud/quality exclusions;
- valid-pixel footprint;
- resampling and reprojection method;
- category-preserving versus continuous-value behavior;
- overview/tiling state;
- digest of exact source or normalized artifact.

Categorical classes must not use interpolation that invents class values.

A visual extent is not necessarily valid data support. Keep file bounds, footprint, valid-pixel mask, analysis support, and public-display support distinct.

Raster-to-vector and public generalization must carry threshold/morphology refs, topology checks, small-feature handling, transform receipts, public field allowlists, reconstruction-risk review, correction, and rollback.

[Back to top](#top)

---

<a id="sensitivity-and-reconstruction-risk"></a>

## Sensitivity and reconstruction risk

Land-cover products may be low sensitivity alone but become restricted through joins, filtering, fine time series, sparse cells, or inference.

Fail closed for joins with:

- rare or protected Fauna occurrences;
- rare plants, specimens, herbarium locality clues, restoration or seed-source sites;
- archaeological, paleontological, cave, cultural, or sovereign-sensitive locations;
- private land, owners, operators, stewards, collectors, or living-person data;
- protected-area stewardship detail;
- critical infrastructure or access routes;
- small counts/cells and sparse class combinations;
- restricted partner or steward datasets.

Review combined exposure across maps, APIs, tiles, downloads, search, graph edges, caches, logs, receipts, screenshots, notifications, generated summaries, Evidence Drawer, Focus Mode, and historical releases.

Public surfaces must not expose credentials, signed URLs, restricted locators, private identities, exact join keys, internal geoprivacy seeds/offsets/parameters, raw provider errors, or small-cell details that defeat aggregation.

A field hidden by a style is not redacted from downloadable bytes.

[Back to top](#top)

---

<a id="lifecycle-and-finite-outcomes"></a>

## Lifecycle and finite outcomes

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec declares intent and required gates; it does not perform promotion.

Minimum sequence:

1. resolve spec identity and activation;
2. resolve parser and consumer;
3. resolve source descriptor, source activation, role, rights, and source head;
4. validate product/epoch/class-scheme identity;
5. validate raster/vector structure and integrity;
6. preserve native classes and masks;
7. resolve crosswalk loss where used;
8. validate temporal and spatial support;
9. apply policy and sensitivity checks;
10. execute only the allowed lifecycle transition;
11. emit receipts and validation reports;
12. resolve evidence/proof/catalog requirements;
13. obtain review and release authority before publication;
14. preserve correction, invalidation, and rollback targets.

Finite outcomes should include:

| Outcome | Meaning |
|---|---|
| `NO_OP` | Governed inputs and state are unchanged. |
| `PROPOSED_WORK` | Change detected; reviewable proposal only. |
| `QUARANTINED` | Held for unresolved integrity, role, rights, class, grid, time, evidence, or sensitivity. |
| `DENIED` | Policy or rights prohibit the action. |
| `ABSTAINED` | Evidence or authority is insufficient. |
| `NEEDS_REVIEW` | Named reviewer must decide. |
| `VALIDATED_CANDIDATE` | Passed bounded validation; not promoted or public. |
| `FAILED` | Deterministic failure with safe reason code. |
| `SUSPENDED` | Spec/source/consumer disabled; no new run. |
| `SUPERSEDED` | Replaced; downstream lineage requires reevaluation. |

[Back to top](#top)

---

<a id="evidence-receipts-proof-catalog-and-release"></a>

## Evidence, receipts, proof, catalog, and release

The dedicated receipt README is:

```text
data/receipts/habitat/land_cover/README.md
```

It documents process-memory intent. It does not prove emitted receipts, final layout, signing, policy enforcement, proof closure, or release integration. Its statement that the parent Habitat receipt README is still a stub is stale relative to current parent documentation and must be reconciled.

Depending on the run, an active profile may require refs to source-intake, transform, raster/grid, class-map, crosswalk, model-run, aggregation/materiality, validation, policy, review, public-safe geometry, catalog-build, release-support, correction, withdrawal, supersession, and rollback receipts.

A receipt is not proof.

Consequential claims should resolve:

```text
EvidenceRef -> EvidenceBundle
```

No dedicated land-cover catalog or release-candidate child was observed in bounded search. Do not create one by assertion. Use verified Habitat parent lanes until an accepted ADR or migration establishes a child.

Normal public path:

```text
released public-safe artifact
-> layer/catalog registry
-> ReleaseManifest / PromotionDecision
-> governed API or resolver
-> MapLibre / Evidence Drawer / approved export
```

Forbidden:

```text
spec / source raster / fixture / processed candidate / receipt
-> direct public map, API, export, search, graph, or generated answer
```

[Back to top](#top)

---

<a id="validation-and-enforceability"></a>

## Validation and enforceability

Required validation layers:

| Layer | Required checks | Current evidence |
|---|---|---|
| Markdown | Links, headings, tables, paths, truth labels. | Checkable now. |
| Spec schema | Required fields, enums, refs, versions, unknown fields. | No accepted spec schema established. |
| Object schemas | Observation, scheme, crosswalk, change, uncertainty. | Permissive PROPOSED scaffolds only. |
| Contracts | Object meaning and anti-collapse. | Draft contracts exist. |
| Source admission | Descriptor, role, rights, activation, source head. | Placeholders; activation unverified. |
| Raster | CRS, grid, resolution, nodata, masks, valid pixels, digest. | Implementation unverified. |
| Crosswalk | Direction, coverage, loss, uncertainty, reviewers. | Implementation unverified. |
| Policy/sensitivity | Rights, joins, public fields/geometry. | Child policy files absent/scaffolded. |
| Tests/fixtures | Positive, negative, idempotency, correction, rollback. | README lanes; payload/modules unverified. |
| Receipts/proof/catalog | Emission, resolution, closure, signatures. | Documentation only. |
| Release/public carriers | Manifest, allowlist, digest, invalidation, rollback. | Documentation only. |
| CI | Relevant executable jobs. | Habitat workflow is TODO-only. |

Required negative cases include missing/duplicate IDs, unknown schema/version, no activation, inactive source, legacy role, rights ambiguity, missing class scheme/epoch, unknown classes, backwards/lossless crosswalk claims, invalid categorical resampling, CRS/grid/mask mismatch, modeled-as-observed output, NWI-as-jurisdictional truth, CDL-as-Habitat crop truth, land-cover-as-occurrence proof, unsafe joins, missing evidence/policy/correction/rollback, direct public writes, secret leakage, and stale superseded artifacts remaining resolvable.

The current Habitat workflow runs only:

```text
echo TODO validate-habitat
echo TODO build-proof-habitat
echo TODO publish-dry-run-habitat
```

A green run is scaffold evidence only.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

A child profile is active only when:

- [ ] stable ID, version, digest, owner, and lineage exist;
- [ ] restrictive accepted spec schema exists;
- [ ] accepted parser and exact consumer exist;
- [ ] separate activation record exists;
- [ ] authoritative source registry and admitted source refs exist;
- [ ] rights and canonical source role are resolved;
- [ ] product, epoch, class scheme, class map, and digest are resolved;
- [ ] crosswalk direction/loss/review are resolved where used;
- [ ] time and freshness semantics are resolved;
- [ ] CRS, grid, mask, nodata, resampling, valid pixels, and uncertainty are resolved;
- [ ] knowledge character is preserved;
- [ ] lifecycle transition is constrained;
- [ ] deterministic fixtures/tests and executable validators pass;
- [ ] policy and sensitivity gates are machine-enforced;
- [ ] receipts and safe reason codes are emitted;
- [ ] evidence/proof/catalog requirements close;
- [ ] public field/geometry allowlists exist where relevant;
- [ ] review and release prerequisites close;
- [ ] correction, invalidation, and rollback are tested;
- [ ] caches, tiles, search, graph, exports, and AI surfaces invalidate safely;
- [ ] CODEOWNERS or equivalent review enforcement exists;
- [ ] documentation matches implemented behavior.

Until then, status remains `DRAFT`, `VALIDATED_DRAFT`, or `APPROVED_INACTIVE`.

[Back to top](#top)

---

<a id="rollback-correction-and-deactivation"></a>

## Rollback, correction, and deactivation

Documentation-only rollback:

- before merge, close the draft PR and abandon the scoped branch;
- after merge, use a transparent revert commit or revert PR;
- restore v0.1 and remove the generated-work receipt for this revision;
- do not rewrite shared history.

A future active-profile rollback must:

1. suspend discovery and scheduling;
2. preserve withdrawn spec and activation records;
3. stop new runs and hold pending candidates;
4. identify the last reviewed safe spec/parser/consumer/source/class-scheme set;
5. restore that set or remain disabled;
6. inventory processed, catalog, triplet, proof, receipt, tile, cache, search, graph, export, and generated-answer surfaces;
7. reevaluate sources, roles, rights, epochs, schemes, crosswalks, grids, times, sensitivity, evidence, and release state;
8. issue correction, withdrawal, supersession, and rollback records;
9. invalidate unsafe or stale derivatives;
10. rerun deterministic validation and reconstruction-risk checks;
11. verify revoked artifacts are no longer publicly resolvable;
12. retain audit linkage to replacement state.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-HAB-LC-001` | What schema governs active land-cover specs? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-002` | What parser/registry discovers them? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-003` | Which executable consumer owns each profile? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-004` | Nested lane or flat compatibility spec? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-HAB-LC-005` | Which nested/flat contract and schema paths are canonical? | CONFLICTED |
| `PIPE-SPEC-HAB-LC-006` | Why does the schema index undercount scaffold files? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-007` | Which Habitat source-registry topology is canonical? | CONFLICTED |
| `PIPE-SPEC-HAB-LC-008` | What maps legacy to canonical source roles? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-009` | Which connector path is canonical for NLCD? | CONFLICTED |
| `PIPE-SPEC-HAB-LC-010` | Which land-cover source is admitted first? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-011` | What rights and terms govern each product? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-012` | What class-scheme identity and digest contract is accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-013` | What crosswalk direction/loss/reviewer vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-014` | What epoch/time vocabulary is accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-015` | What CRS/grid/resampling/valid-pixel profiles are accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-016` | Where do materiality/change thresholds live? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-017` | What knowledge-character enums are accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-018` | Where is field-level policy enforced? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-019` | Where is join-sensitivity policy enforced? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-020` | What validator implementation/reports are accepted? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-021` | Which fixture payloads and executable tests exist? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-022` | Is the receipt child canonical and how is stale parent prose corrected? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-023` | Is a dedicated catalog child accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-HAB-LC-024` | Is a dedicated release-candidate child accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-HAB-LC-025` | What public attribute/derivative allowlists are accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-026` | What correction cascade invalidates all derivatives? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-027` | What rollback drill proves public revocation? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-028` | When will CI move beyond TODO jobs? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-029` | Who owns/reviews this lane in CODEOWNERS? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-030` | Is any profile, schedule, runtime, API, map layer, or public consumer deployed? | UNKNOWN |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | CONFIRMED | v0.1 boundary and speculative tree. | Did not prove files or activation. |
| Direct-lane search | CONFIRMED search result | README-only observed inventory. | Not exhaustive recursive absence. |
| Flat spec fetch | CONFIRMED `Not Found` | Stale/future flat path. | Does not decide replacement. |
| Parent spec and pipeline READMEs | CONFIRMED drafts | Intent/execution split and stale reference. | Do not prove runtime. |
| Habitat config README | CONFIRMED v0.4 | README-only config and compatibility conflicts. | No loader/binding. |
| Land-cover doctrine/contracts | CONFIRMED drafts | Object families and anti-collapse. | Naming/enforcement unresolved. |
| Five nested schemas | CONFIRMED files | Machine-shaped placeholders. | Empty properties; permissive. |
| Flat observation schema | CONFIRMED file | Compatibility scaffold. | Duplicate authority unresolved. |
| Habitat source registry | CONFIRMED draft | Role posture and topology warning. | No land-cover child activation. |
| Two NLCD registry records | CONFIRMED placeholders | Topology/vocabulary conflict. | Neither admitted nor active. |
| NLCD connector README | CONFIRMED v0.2 | README-only connector and modeled-classification boundary. | No runnable connector. |
| Habitat policy and validator READMEs | CONFIRMED scaffolds/index | Responsibility homes. | No field-level enforcement. |
| Land-cover tests and fixture child README | CONFIRMED drafts | Intended test/fixture design. | Payload/modules/pass rates unverified. |
| Land-cover receipt README | CONFIRMED draft | Dedicated process-memory child. | No emitted receipts; stale parent prose. |
| Processed and published READMEs | CONFIRMED drafts | Lifecycle/public boundaries. | No payload/release proof. |
| Catalog/release child searches | NOT OBSERVED / search-limited | Avoid inventing homes. | Not exhaustive absence. |
| Habitat workflow | CONFIRMED | Three TODO jobs. | No substantive enforcement. |
| CODEOWNERS | CONFIRMED placeholder | Generic review state. | No land-cover ownership enforcement. |
| Directory Rules v1.4 | CONFIRMED doctrine | Responsibility roots and lifecycle invariant. | Specific paths still need repo evidence. |

### v0.1 preservation assessment

Preserved:

- declarative **what** versus executable **how**;
- native-class preservation and advisory crosswalks;
- source epoch, raster/geometry, lifecycle, evidence, receipt, release, correction, and rollback boundaries;
- land cover as context rather than occurrence or neighboring-domain truth.

Strengthened:

- speculative tree replaced with actual bounded inventory;
- stale test/fixture/receipt paths corrected;
- absent flat spec surfaced;
- permissive schema and nested/flat conflicts surfaced;
- source registry, connector, and source-role conflicts surfaced;
- activation separated from merge/file presence;
- raster grid, masks, valid pixels, resampling, model/observation, crosswalk loss, uncertainty, sensitive joins, finite outcomes, invalidation, and rollback controls expanded;
- implementation maturity bounded by current evidence.

[Back to top](#top)

---

## Maintainer note

Keep this lane declarative and inactive until schema, parser, consumer, source, class scheme, crosswalk, raster profile, policy, tests, receipts, evidence, review, correction, invalidation, and rollback gates close. Do not place executable code, connectors, source descriptors, class-map authority, schemas, policy rules, lifecycle payloads, receipts, proofs, catalog records, release records, public tiles, caches, search indexes, graph projections, or generated claims here.

A specification may reference authority. It does not acquire authority through proximity.

[Back to top](#top)
