<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-readme
title: pipeline_specs/habitat/ — Governed Habitat Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; five-placeholder-profiles; two-grounded-child-boundaries; no-active-habitat-spec-established; sensitive-domain
owners: OWNER_TBD — Pipeline-spec steward · Habitat steward · Source/rights steward · Object-family stewards · Model/method steward · Spatial/temporal steward · Sensitivity/geoprivacy/cultural reviewer · Consumer owner · Validation/evidence/policy/release stewards · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; habitat; declarative-only; source-role-aware; object-family-aware; model-aware; regulatory-aware; spatially-aware; temporally-aware; rights-aware; sensitivity-aware; reconstruction-resistant; no-secrets; no-live-activation; no-direct-source-access; no-direct-lifecycle-write; no-release-authority
current_path: pipeline_specs/habitat/README.md
truth_posture: CONFIRMED current target and prior blob, parent pipeline-spec contract, direct Habitat lane containing this README, five seven-line PROPOSED inventory placeholders, grounded ecoregions and land-cover child READMEs, draft executable Habitat pipeline documentation, README-only Habitat config lane, draft semantic contracts, broad and partially stale schema inventory with permissive PROPOSED scaffolds and compatibility aliases, subtype-first/domain-first source-registry conflict, empty PROPOSED source-authority register, broad Habitat policy scaffold plus a seven-line sensitivity placeholder, documentation-rich tests and fixtures with executable payloads and pass rates unverified, index-only Habitat validator lane, Habitat receipt parent with only land-cover child confirmed, draft proof/catalog/release-candidate lanes, two seven-line layer-registry placeholders, TODO-only domain-habitat workflow, and placeholder CODEOWNERS / PROPOSED minimum active-spec contract, finite status and outcome vocabularies, deterministic parser and consumer binding, source/object/time/space/model/sensitivity/lifecycle/evidence/release gates, activation/deactivation discipline, validation matrix, correction propagation, and rollback requirements / UNKNOWN accepted Habitat pipeline-spec schema, parser, registry, discovery, scheduler, activation records, executable consumers, runtime behavior, substantive CI enforcement, emitted receipts, proof closure, release-manifest integration, deployed schedules, and public use / NEEDS VERIFICATION owners, exhaustive recursive inventory, canonical source-registry and contract/schema topology, admitted SourceDescriptors, current rights and terms, object-family schemas, source-role mapping, temporal and spatial profiles, model fitness requirements, field-level policy, public attribute allowlists, fixture payloads, executable tests, validator wiring, correction propagation, derived-output invalidation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 49392f54b1e994164000c083366daddf68a6a38a
  prior_blob: e85126e78efd5af06fc69f64a02d319d69812096
  direct_lane_files:
    - pipeline_specs/habitat/README.md
    - pipeline_specs/habitat/nlcd_landcover.yaml
    - pipeline_specs/habitat/nwi_wetlands.yaml
    - pipeline_specs/habitat/connectivity.yaml
    - pipeline_specs/habitat/suitability_model.yaml
    - pipeline_specs/habitat/critical_habitat.yaml
    - pipeline_specs/habitat/ecoregions/README.md
    - pipeline_specs/habitat/land_cover/README.md
  direct_lane_posture: five flat YAML inventory placeholders plus two grounded child README boundaries; no active specification established
  workflow_posture: domain-habitat is pull-request-triggered TODO scaffolding
related:
  - ../README.md
  - ./nlcd_landcover.yaml
  - ./nwi_wetlands.yaml
  - ./connectivity.yaml
  - ./suitability_model.yaml
  - ./critical_habitat.yaml
  - ./ecoregions/README.md
  - ./land_cover/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/habitat/README.md
  - ../../docs/domains/habitat/MISSING_OR_PLANNED_FILES.md
  - ../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../docs/domains/habitat/sublanes/critical-habitat.md
  - ../../pipelines/domains/habitat/README.md
  - ../../configs/domains/habitat/README.md
  - ../../contracts/domains/habitat/README.md
  - ../../schemas/contracts/v1/domains/habitat/README.md
  - ../../data/registry/sources/habitat/README.md
  - ../../data/receipts/habitat/README.md
  - ../../data/proofs/habitat/README.md
  - ../../data/catalog/domain/habitat/README.md
  - ../../tests/domains/habitat/README.md
  - ../../fixtures/domains/habitat/README.md
  - ../../tools/validators/domains/habitat/README.md
  - ../../policy/domains/habitat/README.md
  - ../../release/candidates/habitat/README.md
  - ../../.github/workflows/domain-habitat.yml
  - ../../.github/CODEOWNERS
notes:
  - "v0.2 replaces the planning-only proposed flat tree with commit-pinned repository evidence and classifies all five flat YAMLs as inactive inventory placeholders."
  - "The ecoregions/ and land_cover/ child READMEs are governed documentation boundaries, not evidence of active child profiles, parser binding, scheduling, source activation, or execution."
  - "The verified Habitat receipt parent is data/receipts/habitat/ and only land_cover/ is confirmed as a child receipt README. The previously referenced data/receipts/pipeline/habitat/ path is not used as the parent authority here."
  - "The verified Habitat test and fixture parents are tests/domains/habitat/ and fixtures/domains/habitat/. The previously referenced tests/pipeline_specs/habitat/ and fixtures/pipeline_specs/habitat/ paths are not treated as current facts."
  - "No executable specification, source record, connector, pipeline, config payload, schema, contract, policy rule, fixture, test, validator, workflow, lifecycle object, receipt instance, proof, catalog object, release object, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Habitat Pipeline Specification Boundary

`pipeline_specs/habitat/`

> Declarative run-intent boundary for Habitat processing. A reviewed active specification may state **what** a verified consumer should process, against which admitted sources, for which Habitat object family, under which source-role, rights, time, spatial-support, model, evidence, sensitivity, policy, receipt, review, correction, and release gates. It does not execute a pipeline, admit a source, decide ecological or regulatory truth, create evidence, perform a geoprivacy transform, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-5__placeholders__%2B__2__child__READMEs-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitive__joins-fail__closed-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit) · [Authority](#authority-and-anti-collapse) · [Families](#profile-family-boundaries) · [Contract](#minimum-active-specification-contract) · [Activation](#status-activation-discovery-and-precedence) · [Sources](#sources-rights-and-source-roles) · [Objects](#object-family-and-knowledge-character-boundaries) · [Time](#time-freshness-and-correction) · [Space](#spatial-support-scale-crs-and-public-representation) · [Models](#models-methods-and-uncertainty) · [Sensitivity](#sensitivity-geoprivacy-and-reconstruction-risk) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Evidence](#evidence-receipts-proof-catalog-and-release) · [Example](#illustrative-inactive-profile) · [Validation](#validation-and-enforceability) · [Review](#review-activation-and-change-discipline) · [Done](#definition-of-done-for-an-active-specification) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@49392f54b1e994164000c083366daddf68a6a38a`  
> **Target blob before this revision:** `e85126e78efd5af06fc69f64a02d319d69812096`  
> **Direct-lane result:** this README, five flat YAML placeholders, and two child README boundaries  
> **Active specifications:** none established  
> **Source-authority register:** `PROPOSED`, with an empty `entries` list  
> **Activation:** path presence, filename, merge state, YAML validity, schedule text, schema acceptance, fixture prose, layer-registry presence, map rendering, or a successful dry run activates nothing

> [!CAUTION]
> Habitat is a context and derived-analysis domain, not a shortcut around owning-domain truth. A valid Habitat specification cannot turn a land-cover class into species occurrence, a suitability model into regulatory critical habitat, a corridor into observed movement, NWI into a regulatory wetland determination, an ecoregion into a HabitatPatch, a stewardship boundary into land-title truth, or a tile, catalog record, generated summary, or successful run into evidence or release approval. Exact or reconstructable sensitive joins fail closed.

---

<a id="purpose"></a>

## Purpose

`pipeline_specs/habitat/` is the Habitat domain segment under the `pipeline_specs/` responsibility root.

Its safe future role is to hold small, reviewed, deterministic declarative profiles that bind:

- stable specification identity, immutable version, digest, owner, status, and supersession lineage;
- one accepted parser and one verified executable consumer;
- explicit discovery, precedence, duplicate-handling, activation, deactivation, and rollback rules;
- admitted `SourceDescriptor` references and canonical source roles;
- rights, license, attribution, redistribution, access, cadence, and authority limits;
- Habitat object-family and knowledge-character boundaries;
- source, observed, valid, retrieval, processing, release, correction, embargo, and supersession times;
- spatial support, CRS, scale, resolution, topology, precision, uncertainty, and public-safe representation;
- model identity, method, inputs, calibration, fitness, uncertainty, and non-truth posture;
- input and output lifecycle states;
- sensitive-join, geoprivacy, cultural, private-land, and reconstruction-risk gates;
- schema, contract, validation, evidence, policy, review, receipt, proof, catalog, and release requirements;
- no-network fixtures, deterministic replay, finite outcomes, idempotency, correction propagation, and rollback.

This README is not a pipeline-spec schema, parser, registry, scheduler, activation decision, executable pipeline, connector, source descriptor, object contract, machine schema, policy decision, review record, geoprivacy transform, receipt, proof, catalog record, release record, public API, map layer, search index, graph projection, or generated answer.

### Audience

- Habitat, source, rights, object-family, model, spatial, temporal, and sensitivity stewards;
- pipeline-spec maintainers and executable consumer owners;
- Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Archaeology, Spatial Foundation, and People/Land reviewers for cross-lane joins;
- validation, evidence, policy, release, correction, rollback, security, and documentation reviewers;
- connector owners preparing governed source-intake handoffs;
- maintainers planning activation, deactivation, supersession, or rollback.

[Back to top](#top)

---

<a id="current-status"></a>

## Current status

### Repository maturity matrix

| Surface | Current evidence | Status | Safe conclusion |
|---|---|---:|---|
| Parent Habitat spec README | v0.1 draft before this revision | **CONFIRMED** | Existing declarative boundary, not active behavior |
| Five flat YAML profiles | Seven-line `PROPOSED` planning placeholders | **CONFIRMED placeholders** | Inventory slots only |
| `ecoregions/README.md` | Grounded v0.2 README-only child boundary | **CONFIRMED documentation** | No active ecoregion profile |
| `land_cover/README.md` | Grounded v0.2 README-only child boundary | **CONFIRMED documentation** | No active land-cover profile |
| Pipeline-spec schema | No accepted Habitat spec schema surfaced | **UNKNOWN** | Canonical shape and versioning are unverified |
| Parser / registry / discovery | No accepted Habitat binding surfaced | **UNKNOWN** | Loader, precedence, duplicate handling, and activation lookup are unverified |
| Scheduler / activation records | No verified records surfaced | **UNKNOWN** | Assume inactive |
| Executable Habitat pipeline | Detailed draft README | **CONFIRMED docs; behavior NEEDS VERIFICATION** | No runnable parent consumer is established |
| Habitat configuration | README plus `.gitkeep`, no indexed consumer | **CONFIRMED README-only** | No loader, precedence, or runtime binding |
| Semantic contracts | Broad draft Habitat contract surface | **CONFIRMED drafts** | Meaning is documented; runtime enforcement is not proven |
| Machine schemas | Broad scaffold inventory; parent index is incomplete | **CONFIRMED partial inventory** | Many shapes remain permissive `PROPOSED` scaffolds |
| Source registry | Subtype-first and domain-first Habitat lanes | **CONFIRMED topology conflict** | Do not duplicate source authority |
| Source-authority register | `PROPOSED`; `entries: []` | **CONFIRMED empty register** | No source activation is established |
| Policy | Generic Habitat greenfield scaffold | **CONFIRMED scaffold** | No field-level Habitat policy is established |
| Sensitivity policy | `habitat_classes.yaml` seven-line placeholder | **CONFIRMED placeholder** | No field-level sensitivity enforcement |
| Validators | Habitat index, no child validators confirmed | **CONFIRMED index-only** | No executable Habitat validator is established |
| Tests | Broad parent and child README hierarchy | **CONFIRMED documentation** | Executable modules and pass rates remain unverified |
| Fixtures | Broad child README inventory | **CONFIRMED documentation** | Payload inventory and consumer binding remain unverified |
| Receipts | Habitat parent; land-cover child confirmed | **CONFIRMED drafts** | No emitted receipt chain; exact subtype layout unresolved |
| Proofs | Draft Habitat proof lane | **CONFIRMED documentation** | Emitted proof packs, schemas, validators, and CI are unknown |
| Domain catalog | Draft parent; ecoregions child confirmed | **CONFIRMED documentation** | Broader inventory and closure are unverified |
| Layer registry | Connectivity and critical-habitat placeholders | **CONFIRMED placeholders** | Registration does not prove release or public availability |
| Release candidates | Draft parent; ecoregions and thin-slice children | **CONFIRMED documentation** | Candidate is not release |
| Habitat release-manifest README | Exact path not found | **CONFIRMED exact absence** | Do not invent manifest integration |
| CI | Three `echo TODO` Habitat jobs | **CONFIRMED scaffold-only** | Green status is not Habitat enforcement |
| Ownership | Generic placeholder CODEOWNERS | **CONFIRMED placeholder** | Habitat spec review is not repository-enforced |
| Runtime / public use | No activation or deployment evidence surfaced | **UNKNOWN** | Assume inactive and non-public |

### Bottom line

The current lane is a mixture of planning placeholders and governed documentation:

- five flat YAML files preserve planned profile names but do not contain active specification contracts;
- two child directories now have repository-grounded README boundaries;
- adjacent contracts, schemas, tests, fixtures, receipts, catalogs, and release-candidate docs are useful design evidence but do not establish executable closure;
- no parser, registry, scheduler, source activation, active consumer, receipt chain, proof closure, release manifest, or public deployment is established.

[Back to top](#top)

---

<a id="current-inspected-inventory"></a>

## Current inspected inventory

### Direct lane

```text
pipeline_specs/habitat/
├── README.md
├── nlcd_landcover.yaml
├── nwi_wetlands.yaml
├── connectivity.yaml
├── suitability_model.yaml
├── critical_habitat.yaml
├── ecoregions/
│   └── README.md
└── land_cover/
    └── README.md
```

### Inventory classification

| Path | Observed content | Classification | Active? |
|---|---|---|---:|
| `README.md` | Parent boundary documentation | Draft documentation | No |
| `nlcd_landcover.yaml` | Seven-line planning placeholder | `PROPOSED` inventory placeholder | No |
| `nwi_wetlands.yaml` | Seven-line planning placeholder | `PROPOSED` inventory placeholder | No |
| `connectivity.yaml` | Seven-line planning placeholder | `PROPOSED` inventory placeholder | No |
| `suitability_model.yaml` | Seven-line planning placeholder | `PROPOSED` inventory placeholder | No |
| `critical_habitat.yaml` | Seven-line planning placeholder | `PROPOSED` inventory placeholder | No |
| `ecoregions/README.md` | Grounded child specification boundary | README-only documentation | No |
| `land_cover/README.md` | Grounded child specification boundary | README-only documentation | No |

### Why the YAML files are not specifications

Each flat YAML contains only:

- `status: PROPOSED`;
- a planning-document pointer;
- its own path;
- a placeholder note.

They do not establish:

- `spec_id`, version, digest, owner, status vocabulary, or supersession;
- schema identity or parser compatibility;
- executable consumer, discovery, precedence, or activation;
- admitted sources, source roles, rights, or source-head references;
- input/output lifecycle states;
- object-family, model, time, spatial, sensitivity, or evidence gates;
- finite outcomes, receipts, review state, correction, or rollback.

A filename can preserve an idea without creating an executable contract.

### Child boundary interpretation

The child READMEs establish scoped design and governance boundaries:

- `ecoregions/` preserves framework, version, hierarchy, context-join, CRS, topology, and public-representation requirements;
- `land_cover/` preserves native classification, source epoch, crosswalk, raster, valid-pixel, model, and public-representation requirements.

Neither child README proves:

- active child YAML profiles;
- accepted spec schemas;
- parser or consumer binding;
- source activation;
- scheduling;
- executable tests;
- runtime behavior;
- public release.

[Back to top](#top)

---

<a id="repository-fit"></a>

## Repository fit

Directory Rules assigns files by responsibility, not topic.

| Responsibility | Verified or candidate home | Spec relationship |
|---|---|---|
| Declarative Habitat run intent | `pipeline_specs/habitat/` | This lane |
| Executable Habitat behavior | `pipelines/domains/habitat/` | Bind to a verified consumer; do not duplicate code |
| Safe configuration support | `configs/domains/habitat/` | Reference only after a consumer binding exists |
| Human-facing doctrine | `docs/domains/habitat/` | Reference scope, vocabulary, and constraints |
| Semantic object meaning | `contracts/domains/habitat/` | Reference accepted contract IDs |
| Machine shape | `schemas/contracts/v1/domains/habitat/` or accepted compatibility home | Validate against accepted schema IDs |
| Source identity, rights, role, and admission | Accepted Habitat source-registry home | Reference admitted records |
| Connector behavior | Source-specific `connectors/` lanes | Consume governed RAW/QUARANTINE handoffs only |
| Policy and sensitivity | `policy/` responsibility roots | Require decisions; do not embed hidden authority |
| Tests | `tests/domains/habitat/` | Prove behavior; do not activate specs |
| Fixtures | `fixtures/domains/habitat/` | Synthetic examples only |
| Validators | `tools/validators/domains/habitat/` or accepted shared validator lanes | Enforce accepted contracts and policy |
| RAW / WORK / QUARANTINE / PROCESSED | `data/` lifecycle roots | Declare transitions; do not store data here |
| Receipts | `data/receipts/habitat/` and accepted shared receipt homes | Declare required receipt classes |
| Proofs | `data/proofs/habitat/` and accepted shared proof homes | Require resolvable proof references |
| Catalog / triplet | `data/catalog/`, `data/triplets/` | Require closure; never write directly by assertion |
| Release candidates and decisions | `release/` | Require release inputs; never approve release |
| Published artifacts | `data/published/` after release | Reference released outputs only |
| Public clients | Governed APIs and released artifacts | No direct spec or internal-store access |

### Corrected v0.1 paths

The v0.1 README used planning paths that are not adopted here as current facts.

| v0.1 reference | Current evidence-backed posture |
|---|---|
| `tests/pipeline_specs/habitat/` | Use `tests/domains/habitat/` as the verified parent documentation lane |
| `fixtures/pipeline_specs/habitat/` | Use `fixtures/domains/habitat/` as the verified parent fixture lane |
| `data/receipts/pipeline/habitat/` | Use `data/receipts/habitat/` as the verified Habitat receipt parent |
| `data/proofs/evidence_bundle/` as sole Habitat proof path | `data/proofs/habitat/` is the verified Habitat proof README; shared proof topology still needs verification |
| `release/manifests/habitat/` as confirmed | Exact Habitat manifest README was not present at the inspected path |
| proposed flat lifecycle-stage YAML tree | Current direct inventory is the five placeholders and two child README lanes listed above |

### Topology conflicts that remain open

This README does not resolve:

- subtype-first versus domain-first Habitat source-registry paths;
- segmented versus flat Habitat contract and schema aliases;
- incomplete parent schema indexes versus broader actual scaffold inventory;
- legacy source-role words versus the current seven-role registry vocabulary;
- receipt subtype layout;
- release-manifest path and schema;
- child directory versus flat-file profile conventions;
- compatibility `biotopes` paths versus Habitat-owned paths.

Resolving an authority conflict requires an ADR, migration note, registry decision, or accepted steward review—not a README assertion.

[Back to top](#top)

---

<a id="authority-and-anti-collapse"></a>

## Authority and anti-collapse

### What an active Habitat specification may declare

A reviewed active profile may declare:

- which verified executable consumer is eligible to read it;
- which admitted sources and source roles are in scope;
- which Habitat object family or processing stage is requested;
- which model, regulatory, observed, aggregate, administrative, candidate, synthetic, or derived knowledge character applies;
- which input and output lifecycle states are allowed;
- which time, spatial, model, sensitivity, evidence, policy, review, receipt, catalog, and release gates apply;
- which finite outcome is required when a gate cannot close.

### What this lane cannot decide

A Habitat specification cannot decide:

- that a source is admitted, active, current, authoritative, rights-cleared, or safe;
- that a legacy role word is an accepted source role;
- that two object-family records are identical;
- that exact or generalized geometry is public-safe;
- that a model is calibrated, fit, causal, current, or authoritative;
- that a crosswalk is lossless or authoritative;
- that a regulatory designation is observed or modeled;
- that an occurrence belongs to Habitat rather than Fauna or Flora;
- that evidence closes a claim;
- that a geoprivacy, redaction, aggregation, or generalization transform occurred;
- that validation, policy, review, catalog closure, or release approval exists;
- that public clients may bypass governed interfaces.

### Disallowed collapses

```text
spec file -> executable pipeline
parse success -> active specification
profile merge -> source activation
source list -> source authority
planning tracker -> implementation proof
layer-registry placeholder -> released layer
schedule -> freshness proof
source product -> Habitat truth
land-cover class -> species or plant occurrence
land-cover class -> HabitatPatch quality
NWI class -> regulatory wetland determination
NWI class -> Hydrology truth
CDL class -> Habitat crop truth
EPA ecoregion -> occurrence or HabitatPatch
critical habitat -> observed or modeled habitat
suitability model -> regulatory critical habitat
suitability model -> species occurrence
connectivity edge -> observed movement
corridor -> conservation instruction
stewardship zone -> land-title truth
model output -> observation
crosswalk -> identity equivalence
representation requirement -> performed transform
successful run -> EvidenceBundle
receipt -> proof
catalog entry -> release approval
publish profile -> PUBLISHED
tile / style / popup -> canonical truth
generated summary -> evidence
```

### Required separations

| Concern | Must remain distinct from |
|---|---|
| Land-cover observation | Class scheme, crosswalk, HabitatPatch, suitability, occurrence, release |
| Ecoregion context | Occurrence, HabitatPatch, critical habitat, hydrology, soil, release |
| Critical habitat | Modeled suitability, observation, occurrence, legal advice |
| Suitability model | Observation, occurrence, regulatory designation, management decision |
| Connectivity / corridor | Observed movement, causal proof, conservation instruction |
| Wetland context | Regulatory delineation, jurisdictional determination, Hydrology truth |
| HabitatPatch | Land-cover observation, ecoregion, suitability score, occurrence |
| Restoration opportunity | Restoration decision, success claim, landowner instruction |
| Stewardship zone | Title, ownership, consent, ecological condition |
| Public-safe derivative | Canonical source, processed truth, release decision |
| Receipt | EvidenceBundle, proof pack, catalog record, ReleaseManifest |
| Generated language | Source evidence, policy, review, release state |

[Back to top](#top)

---

<a id="profile-family-boundaries"></a>

## Profile family boundaries

### `nlcd_landcover.yaml`

Current posture: seven-line `PROPOSED` placeholder.

A future active NLCD profile would need to bind:

- an admitted source descriptor and source activation record;
- product, release/collection, epoch, sub-product, class-map version, and source-head identity;
- native class codes and labels without silent recoding;
- source role appropriate to the specific product;
- source CRS, resolution, extent, nodata, valid-pixel support, and raster profile;
- rights, attribution, redistribution, and public-use posture;
- parser/consumer binding, finite outcomes, receipts, proof, correction, and rollback.

It must not treat a classifier-assigned pixel as direct field measurement or a land-cover class as Habitat truth.

### `nwi_wetlands.yaml`

Current posture: seven-line `PROPOSED` placeholder.

A future active NWI profile would need to bind:

- the exact admitted product and source role;
- native wetland classification and source vintage;
- distinction between wetland observation/context, regulatory designation, and jurisdictional determination;
- Hydrology and regulatory-owner boundaries;
- sensitivity and private-land join controls;
- evidence, policy, review, public representation, correction, and rollback.

It must not imply a legal wetland determination or hydrologic truth merely from an NWI classification.

### `connectivity.yaml`

Current posture: seven-line `PROPOSED` placeholder.

A future active connectivity profile would need to bind:

- accepted `ConnectivityEdge` / `Corridor` contracts and schemas;
- method, graph construction, resistance/cost surface, scale, temporal scope, and uncertainty;
- source inputs and roles;
- model/run identity and receipts;
- no-observed-movement and no-causal-proof posture;
- sensitive habitat and infrastructure exposure controls;
- public generalization, validation, correction, and rollback.

It must not turn a derived edge or corridor into observed movement or a management instruction.

### `suitability_model.yaml`

Current posture: seven-line `PROPOSED` placeholder.

A future active suitability profile would need to bind:

- accepted `SuitabilityModel` contract/schema and model card;
- model identity, version, digest, code/config refs, training/calibration scope, target, features, assumptions, limitations, and fitness;
- input EvidenceBundle and source-role closure;
- spatial and temporal scope;
- uncertainty, validation, drift, stale-state, correction, and invalidation;
- downstream allowed and denied uses;
- public representation and release gates.

It must not turn suitability into observed occurrence, habitat condition, critical-habitat designation, legal advice, or management prescription.

### `critical_habitat.yaml`

Current posture: seven-line `PROPOSED` placeholder.

A future active critical-habitat profile would need to bind:

- an admitted regulatory source and source activation record;
- designation identity, authority, legal scope, effective time, revision/supersession, and cited source;
- explicit `regulatory` source role;
- taxon/listing references owned by Fauna or Flora;
- separation from modeled habitat and occurrence evidence;
- rights, public representation, correction, withdrawal, and rollback;
- legal-advice denial and authority-scope notices.

It must preserve the bidirectional anti-collapse rule:

```text
modeled suitability != regulatory critical habitat
regulatory critical habitat != observation or modeled estimate
```

### `ecoregions/`

Current posture: grounded v0.2 child README, no active child profile.

The child owns declarative requirements for:

- framework and source version;
- hierarchy level and parent/child relations;
- boundary version, CRS, topology, scale, and uncertainty;
- crosswalk loss and context-join posture;
- public-safe representation.

The parent must not flatten that scope into the generic Habitat YAML namespace.

### `land_cover/`

Current posture: grounded v0.2 child README, no active child profile.

The child owns declarative requirements for:

- source product, epoch, native classification, class-map version, and crosswalk;
- raster/grid/mask/nodata/valid-pixel support;
- model-versus-observation posture;
- land-cover-specific sensitivity and release requirements.

The parent must not create a second land-cover profile authority beside the child without an explicit migration decision.

### Future profile families

Other Habitat profile families may be useful, but remain `PROPOSED` until created and grounded:

- habitat patch;
- ecological system;
- habitat quality or condition;
- restoration opportunity;
- stewardship zone;
- wetland/riparian context beyond the NWI placeholder;
- source refresh or watcher;
- catalog/triplet closure;
- public-safe release readiness;
- rollback readiness.

Do not create them merely because the v0.1 tree listed plausible names.

[Back to top](#top)

---

<a id="minimum-active-specification-contract"></a>

## Minimum active specification contract

A Habitat profile is not eligible for activation until every applicable requirement below is represented by accepted fields or resolvable references.

### 1. Immutable specification identity

Required:

- `spec_id`;
- semantic version or immutable revision;
- normalized digest;
- owner and reviewer classes;
- domain and profile family;
- status;
- created, reviewed, activated, corrected, deprecated, and superseded times where applicable;
- predecessor and successor refs;
- deactivation and rollback target.

Identity must not be derived only from a mutable path or friendly filename.

### 2. Accepted schema and parser

Required:

- accepted pipeline-spec schema ID and revision;
- parser package/module/version/digest;
- strict unknown-field behavior;
- deterministic normalization and digest rules;
- duplicate-key rejection;
- enum and reference validation;
- bounded input size and nesting;
- no unsafe YAML tags or object construction;
- error reason codes;
- compatibility and migration policy.

A permissive domain-object schema is not a pipeline-spec schema.

### 3. Verified executable consumer

Required:

- one consumer ID;
- executable path/package and version;
- supported spec schema range;
- supported profile families;
- discovery and loading contract;
- precedence and duplicate handling;
- dry-run behavior;
- no-network fixture mode;
- output and receipt contract;
- deactivation behavior.

A README or proposed pipeline path is not a consumer binding.

### 4. Discovery, precedence, and activation

Required:

- registry or manifest that discovers the profile;
- explicit default-inactive posture;
- activation decision ref;
- activation actor and review state;
- environment and scope;
- conflict and duplicate behavior;
- precedence among parent, child, environment, and local profiles;
- schedule binding, if any;
- kill switch;
- deactivation and supersession procedure.

Merge and activation must be separate reviewable events.

### 5. Sources, roles, rights, and authority limits

For every source:

- stable SourceDescriptor ref and revision;
- activation decision ref;
- canonical source role;
- authority scope;
- product/sub-product/version/edition/source-head;
- spatial and temporal scope;
- rights, license, attribution, redistribution, access, and derived-use posture;
- cadence and stale-state rules;
- sensitivity floor;
- correction and withdrawal path.

A provider name or filename never establishes authority.

### 6. Object-family and knowledge-character scope

Required:

- accepted object-family contract/schema refs;
- allowed input and output object families;
- allowed knowledge character;
- denied role upgrades;
- cross-lane ownership;
- identity and deduplication posture;
- candidate, observation, model, regulatory, aggregate, administrative, synthetic, generalized, and released distinctions.

### 7. Temporal contract

Required as applicable:

- source publication/version time;
- observation/acquisition/event time;
- valid time;
- retrieval time;
- processing time;
- model-run time;
- release time;
- correction time;
- embargo time;
- supersession time;
- cadence, freshness, stale threshold, and outage behavior.

A schedule is not freshness proof.

### 8. Spatial-support contract

Required as applicable:

- source and analysis CRS;
- tiling/display CRS;
- source geometry or raster support;
- spatial unit, extent, scale, resolution, and precision;
- grid, transform, alignment, resampling, mask, nodata, and valid-pixel posture;
- topology and boundary lineage;
- uncertainty and quality;
- public representation profile;
- reconstruction-risk review.

### 9. Model and method contract

For modeled or derived profiles:

- model/method ID, version, digest, owner, and card;
- code/config/environment refs;
- input feature and source refs;
- target definition;
- training/calibration/validation scope;
- assumptions and limitations;
- uncertainty and confidence;
- drift and stale-state rules;
- allowed and denied uses;
- model-run receipt;
- correction and invalidation behavior.

A model cannot inherit regulatory or observational authority.

### 10. Sensitivity, rights, and public-use contract

Required:

- sensitivity classification and policy refs;
- rights and cultural/sovereign review refs where material;
- join-induced sensitivity evaluation;
- public attribute allowlist;
- geometry exposure posture;
- redaction/generalization/aggregation profile refs;
- transform receipt requirements;
- minimum-cell and reconstruction-risk review without publishing operational thresholds here;
- role-based access and audit refs;
- deny/abstain/restrict behavior.

### 11. Lifecycle contract

Required:

- allowed input stage;
- allowed output stage;
- quarantine reason codes;
- promotion prerequisites;
- atomic write and idempotency posture;
- input/output hashes;
- run identity and lineage;
- correction propagation;
- rollback target.

The invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

### 12. Evidence, validation, receipts, and proof

Required:

- EvidenceRef requirements;
- EvidenceBundle closure rules;
- validator IDs and versions;
- validation-report destination;
- run, transform, model, aggregation, redaction, catalog, correction, and release-support receipt classes as applicable;
- proof requirements;
- citation validation;
- unresolved-evidence behavior;
- audit and retention posture.

### 13. Catalog, release, correction, and rollback

Required for release-capable profiles:

- catalog and triplet closure requirements;
- release-candidate ref;
- ReleaseManifest / PromotionDecision requirements;
- released artifact and layer-registry refs;
- correction, withdrawal, supersession, and rollback refs;
- cache, tile, export, search, graph, vector index, and generated-summary invalidation;
- verification that revoked artifacts are no longer publicly resolvable.

### 14. Security and operational safety

Required:

- no secrets in the profile;
- secret-manager/environment indirection only;
- endpoint allowlist refs, not private endpoints in documentation;
- bounded timeouts, retries, concurrency, object size, and resource use;
- path traversal and archive safety;
- sanitized logging and error output;
- no sensitive coordinates, private identities, restricted join keys, or operational exposure parameters in logs or receipts;
- dependency and parser hardening;
- kill switch and incident owner.

[Back to top](#top)

---

<a id="status-activation-discovery-and-precedence"></a>

## Status, activation, discovery, and precedence

### Proposed finite profile statuses

| Status | Meaning | Discoverable? | Runnable? |
|---|---|---:|---:|
| `INVENTORY_PLACEHOLDER` | Name/path preserved from planning inventory | No | No |
| `DRAFT` | Authored but incomplete or unreviewed | Optional review discovery only | No |
| `VALIDATED_DRAFT` | Shape-valid with fixtures, still inactive | Review only | Dry-run only if separately allowed |
| `READY_FOR_REVIEW` | Required evidence assembled | Review only | No |
| `APPROVED_INACTIVE` | Approved contract, deliberately inactive | Yes | No |
| `ACTIVE` | Separately activated for a bounded scope | Yes | Yes |
| `SUSPENDED` | Temporarily blocked | Yes | No |
| `SUPERSEDED` | Replaced by a reviewed successor | Historical | No |
| `DEPRECATED` | Retained for compatibility during migration | Historical/controlled | No new use |
| `WITHDRAWN` | Removed from eligible use | Historical/audit | No |
| `REJECTED` | Reviewed and not accepted | Historical/audit | No |

The five current flat YAML files are `INVENTORY_PLACEHOLDER` in effect, regardless of their literal `status: PROPOSED`.

### Activation decision

An activation decision should identify:

- profile ID, version, and digest;
- parser and consumer versions;
- source activation refs;
- scope and environment;
- schedule binding;
- allowed lifecycle transitions;
- policy and review refs;
- approver classes;
- activation timestamp;
- kill-switch owner;
- rollback target;
- expiry or re-review trigger.

### Precedence rules

Until an accepted precedence contract exists:

- parent and child profiles must not silently merge;
- environment or local overrides must not weaken policy, sensitivity, evidence, review, or release gates;
- duplicate `spec_id` values must fail closed;
- different paths with the same digest require explicit alias handling;
- same path with a different digest requires a new revision and review;
- deprecated compatibility paths must point to—not fork—authority;
- missing refs must produce a finite non-success outcome.

### Schedules and watchers

A schedule or watcher may observe, compare, or propose work. It must not:

- activate a source;
- admit RAW data;
- promote lifecycle state;
- approve a model or crosswalk;
- decide sensitivity;
- publish;
- update a release pointer;
- feed public UI directly.

Watchers are non-publishers and non-admitters.

[Back to top](#top)

---

<a id="sources-rights-and-source-roles"></a>

## Sources, rights, and source roles

### Current source posture

The Habitat source registry is experimental and topology-conflicted:

- `data/registry/sources/habitat/` is a subtype-first lane;
- domain-first Habitat registry material also exists;
- only the ecoregions child README is confirmed under the subtype-first parent;
- the source-authority register is `PROPOSED` and contains no entries;
- source-family files or connector READMEs do not establish activation.

### Canonical role posture

New Habitat specifications should reference the accepted source-role vocabulary:

- `observed`;
- `regulatory`;
- `modeled`;
- `aggregate`;
- `administrative`;
- `candidate`;
- `synthetic`.

Legacy terms such as `authority`, `context`, `primary`, `corroborating`, `restricted`, `derived`, or `model` must be mapped through a reviewed compatibility contract before claim-bearing use. They must not be copied into active profiles by convenience.

### Source-family cautions

| Family | Typical role posture | Required guardrail |
|---|---|---|
| NLCD-style land cover | Product-specific modeled/aggregate/observed classification posture | Preserve native classes and epoch; no field-measurement claim |
| NWI wetlands | Product-specific observed/regulatory/administrative posture | No jurisdictional or hydrologic-truth shortcut |
| GAP / LANDFIRE / ecological systems | Modeled or aggregate | Preserve model/product/version and uncertainty |
| Regulatory critical habitat | Regulatory | Preserve issuing authority, effective time, legal scope, and taxon-owner boundary |
| Ecoregions | Administrative or aggregate context | Preserve framework/version/level; no occurrence claim |
| Stewardship / protected areas | Administrative | No land-title, consent, condition, or management-decision claim |
| Occurrence context | Owning Fauna/Flora role | Preserve domain ownership and geoprivacy |
| Remote sensing / vegetation indices | Observed, modeled, or aggregate by product | Preserve sensor/product/method/time/uncertainty |
| Field or steward data | Observed or candidate | Preserve terms, identities, review, and precise-location sensitivity |

### Rights gate

Unknown or unresolved rights require:

- `HOLD`, `QUARANTINE`, `ABSTAIN`, `DENY`, or `NEEDS_REVIEW`;
- no public release;
- no inference that public availability equals redistribution permission;
- no hidden endpoint, credential, private agreement term, or access route in the spec;
- explicit correction and withdrawal handling if terms change.

[Back to top](#top)

---

<a id="object-family-and-knowledge-character-boundaries"></a>

## Object-family and knowledge-character boundaries

### Habitat object families referenced by specs

A parent or child profile may reference accepted contracts for:

- `LandCoverObservation`;
- `ClassSchemeProfile`;
- `CoverClassCrosswalk`;
- `LandCoverChangeSummary`;
- `EcoregionFramework`;
- `EcoregionSnapshot`;
- `EcoregionContextJoin`;
- `HabitatPatch`;
- `EcologicalSystem`;
- `HabitatQualityScore`;
- `SuitabilityModel`;
- `ConnectivityEdge`;
- `Corridor`;
- `RestorationOpportunity`;
- `StewardshipZone`;
- `UncertaintySurface`;
- `ModelRunReceipt`;
- domain validation and layer descriptor objects.

Reference does not imply that all contracts or schemas are canonical, complete, or field-enforced.

### Knowledge character

Every claim-bearing output should preserve whether it is:

- source-native observation;
- reviewed observation;
- regulatory designation;
- modeled estimate;
- aggregate summary;
- administrative boundary/context;
- candidate;
- synthetic fixture;
- crosswalk-derived interpretation;
- generalized public derivative;
- released carrier;
- generated explanation.

### Cross-domain ownership

| Concern | Owning lane | Habitat use |
|---|---|---|
| Animal occurrence and taxonomy | Fauna | Governed public-safe context only |
| Plant taxon, specimen, occurrence, rare-plant record | Flora | Governed public-safe context only |
| Waterbody, flow, watershed, measurement | Hydrology | Context; no ownership transfer |
| Soil unit, component, horizon, property | Soil | Context; no ownership transfer |
| Crop, rotation, field, agricultural practice | Agriculture | Context; CDL is not Habitat truth |
| Hazard event, risk, alert, life-safety guidance | Hazards | Context; no alert authority |
| Archaeological/cultural site or knowledge | Archaeology/cultural authority | Restricted, policy- and rights-gated context |
| Parcel, title, owner, consent | People/Land | Administrative context only |
| CRS, basemap, tiling, generalization | Spatial Foundation | Shared spatial support; Habitat retains domain meaning |
| Release | Release authority | Habitat supplies candidates, not decisions |

[Back to top](#top)

---

<a id="time-freshness-and-correction"></a>

## Time, freshness, and correction

Habitat profiles should preserve relevant time kinds separately.

| Time kind | Examples | Rule |
|---|---|---|
| Source publication/version | Agency release or edition | Preserve source-native identity |
| Observation/acquisition | Survey, imagery, scene, or classification time | Do not substitute retrieval time |
| Valid time | Period the record or designation applies | Required for time-bounded claims |
| Retrieval time | When KFM obtained source material | Not observation time |
| Processing time | Pipeline execution | Not source or valid time |
| Model-run time | When a model generated output | Preserve model and input versions |
| Release time | When an artifact became released | Requires release authority |
| Effective time | Regulatory effective date | Distinct from publication or retrieval |
| Correction time | When a correction became active | Must propagate downstream |
| Embargo time | Restricted-until period | Enforced by policy, not prose |
| Supersession time | When a successor replaced a version | Preserve history and rollback |

### Freshness requirements

An active profile should declare:

- source-head comparison method;
- cadence and expected lag;
- stale threshold or review trigger;
- outage and retry behavior;
- no-op outcome;
- source-version change outcome;
- materiality review;
- correction and invalidation cascade;
- public stale-state behavior.

A successful scheduled run does not prove source freshness.

### Correction propagation

A source, contract, schema, model, policy, or review correction should trigger an inventory of:

- RAW/WORK/QUARANTINE/PROCESSED records;
- catalog and triplet records;
- receipts and proofs;
- release candidates and manifests;
- published layers and exports;
- layer-registry pointers;
- caches and `latest` pointers;
- search and graph indexes;
- Evidence Drawer and Focus Mode projections;
- generated summaries and AI retrieval indexes.

[Back to top](#top)

---

<a id="spatial-support-scale-crs-and-public-representation"></a>

## Spatial support, scale, CRS, and public representation

An active profile must make spatial semantics inspectable.

### Minimum spatial fields

- source geometry/raster/grid identity;
- source CRS;
- analysis CRS;
- tiling/display CRS;
- spatial support type;
- extent and coverage;
- scale and resolution;
- precision and significant digits;
- topology and boundary lineage;
- raster transform and alignment;
- resampling method;
- nodata and valid-pixel treatment;
- uncertainty and quality;
- public representation profile;
- transform receipt refs.

### Scale discipline

Habitat outputs must not be used beyond their supported scale.

Examples:

- national land-cover classes do not become parcel-level field observations;
- regional suitability surfaces do not become site-specific occurrence proof;
- ecoregion boundaries do not become fine-scale HabitatPatch boundaries;
- generalized public layers do not become canonical internal geometry;
- small-cell or sparse summaries may remain reconstructable even when coordinates are absent.

### Public representation

Public profiles should require:

- explicit field allowlist;
- geometry precision/generalization posture;
- zoom and scale limits;
- source role, vintage, uncertainty, and caveat fields;
- evidence resolver keys;
- release and rollback refs;
- denial of internal IDs, restricted join keys, private identities, hidden coordinates, or operational transform parameters.

Hiding a field in a style is not publication control.

[Back to top](#top)

---

<a id="models-methods-and-uncertainty"></a>

## Models, methods, and uncertainty

### Model-versus-observation rule

```text
modeled != observed
modeled != regulatory
aggregate != source-native
prediction != occurrence
suitability != critical habitat
connectivity != observed movement
opportunity != decision
```

### Required model support

A modeled or derived Habitat profile should require:

- model/method card;
- code/config/environment identity;
- input dataset and EvidenceBundle refs;
- source roles and time windows;
- target and output semantics;
- assumptions and limitations;
- calibration and validation;
- uncertainty;
- fairness/bias or representativeness concerns where material;
- spatial transferability and scale;
- temporal validity and drift monitoring;
- allowed and denied use cases;
- model-run receipt;
- correction, invalidation, withdrawal, and rollback.

### Uncertainty

Uncertainty must travel with the output, not remain only in internal reports.

Potential forms include:

- classification accuracy;
- source-vintage gap;
- valid-pixel coverage;
- crosswalk ambiguity;
- model confidence;
- spatial boundary uncertainty;
- temporal uncertainty;
- missing-source uncertainty;
- reviewer disagreement;
- policy uncertainty.

Unknown uncertainty is not zero uncertainty.

[Back to top](#top)

---

<a id="sensitivity-geoprivacy-and-reconstruction-risk"></a>

## Sensitivity, geoprivacy, and reconstruction risk

Habitat sensitivity is often **join-induced**.

A broadly public habitat or land-cover layer may become restricted when combined with:

- rare species or rare plants;
- nests, dens, roosts, hibernacula, spawning, breeding, or nursery sites;
- exact vulnerable habitat;
- archaeology, paleontology, caves, sacred or cultural places;
- traditional ecological knowledge;
- stewardship-controlled sites;
- private parcels, owners, collectors, observers, or living persons;
- infrastructure or operational access routes;
- small counts, sparse cells, or narrow time windows;
- other surfaces that enable reverse engineering.

### Fail-closed rules

When sensitivity, rights, sovereignty, cultural authority, private-party exposure, or reconstruction risk is unresolved:

- do not activate the profile;
- do not publish exact geometry;
- do not expose restricted attributes;
- do not include operational redaction/generalization parameters in public docs, logs, receipts, or notifications;
- do not permit a parent profile to weaken a child sensitivity rule;
- route to `HOLD`, `QUARANTINE`, `RESTRICT`, `ABSTAIN`, `DENY`, `NEEDS_REVIEW`, or `ERROR`.

### Surfaces requiring parity

The same approved exposure posture must hold across:

- maps and tiles;
- APIs and exports;
- search and filters;
- graph/triplet projections;
- vector and semantic indexes;
- caches;
- screenshots and reports;
- logs and telemetry;
- receipts and notifications;
- Evidence Drawer and Focus Mode;
- generated summaries and AI responses.

A location hidden on the map but exposed in search, export, graph, or generated text is still exposed.

### No-leak documentation posture

This README must not contain:

- real sensitive coordinates;
- real restricted occurrence clues;
- private identities;
- restricted join keys;
- operational generalization radii, offsets, seeds, or thresholds;
- credentials;
- private endpoints;
- field-access routes;
- exact reconstruction recipes.

[Back to top](#top)

---

<a id="lifecycle-gates-and-finite-outcomes"></a>

## Lifecycle gates and finite outcomes

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare allowed transitions. It cannot perform or approve them merely by existing.

### Proposed finite run outcomes

| Outcome | Meaning |
|---|---|
| `NO_OP` | No eligible or material change |
| `PROPOSED_WORK` | Work package proposed for review |
| `RAW_CAPTURED` | Controlled source admission completed |
| `QUARANTINED` | Input held due to unresolved or failed gates |
| `PROCESSED_CANDIDATE` | Candidate produced, not cataloged or public |
| `VALIDATION_FAILED` | Contract/schema/domain validation failed |
| `HOLD` | Awaiting evidence, rights, policy, review, or dependency |
| `NEEDS_REVIEW` | Human or authority review required |
| `RESTRICT` | Use permitted only under constrained access |
| `ABSTAIN` | Insufficient support for the requested claim/action |
| `DENY` | Policy or governance prohibits the action |
| `ERROR` | Bounded technical failure; no unsafe fallback |
| `CATALOG_READY` | Catalog handoff candidate, not catalog closure |
| `RELEASE_CANDIDATE_READY` | Candidate packet assembled, not approved |
| `RELEASED` | Only after a valid release decision and manifest |
| `CORRECTED` | Correction applied with downstream propagation |
| `SUPERSEDED` | Replaced while preserving lineage |
| `ROLLED_BACK` | Reviewed rollback completed and verified |

### Promotion prerequisites

A profile must not promote a candidate when any required item is missing:

- source admission and rights;
- accepted contract/schema;
- parser and consumer identity;
- validation;
- evidence closure;
- policy decision;
- sensitivity/public representation;
- review record;
- required receipts and proof;
- catalog closure;
- release decision;
- correction path;
- rollback target.

### Idempotency

Given the same:

- spec digest;
- parser/consumer versions;
- source-head refs;
- input hashes;
- config and policy refs;
- model/method refs;

a replay should produce the same normalized result or a documented finite variance. Undocumented nondeterminism blocks promotion.

[Back to top](#top)

---

<a id="evidence-receipts-proof-catalog-and-release"></a>

## Evidence, receipts, proof, catalog, and release

### Object-family separation

```text
specification != run
run receipt != EvidenceBundle
receipt != proof
proof != catalog
catalog != release
release manifest != published bytes
published bytes != canonical source
generated explanation != evidence
```

### Evidence

A claim-bearing Habitat output should resolve:

```text
EvidenceRef -> EvidenceBundle
```

If evidence cannot resolve:

- narrow the claim;
- return a finite non-answer;
- hold or quarantine the candidate;
- do not substitute generated prose or a map layer.

### Receipts

The verified Habitat receipt parent is:

```text
data/receipts/habitat/
```

The only confirmed child receipt README is:

```text
data/receipts/habitat/land_cover/
```

A spec may require receipt classes, but it does not emit a receipt by itself.

Possible classes include:

- run;
- source/intake;
- transform;
- validation;
- model run;
- crosswalk;
- aggregation;
- redaction/generalization;
- policy decision;
- catalog build;
- correction;
- rollback;
- release support.

Exact receipt schema and subtype layout remain `NEEDS VERIFICATION`.

### Proof

`data/proofs/habitat/` is a draft proof lane. Current evidence does not establish emitted proof packs, complete schemas, executable validators, CI integration, or release consumption.

### Catalog

`data/catalog/domain/habitat/` is a draft catalog parent. The only confirmed child README is `ecoregions/`. Catalog presence does not make a claim true or public.

### Layer registry

The observed connectivity and critical-habitat layer-registry YAMLs are placeholders. A layer-registry entry must not be used as release evidence.

### Release

`release/candidates/habitat/` is a draft review lane with documented ecoregions and Habitat–Fauna thin-slice children.

A release candidate is not a release.

The exact `release/manifests/habitat/README.md` path was not present at the evidence snapshot. Active specs must therefore reference only a verified release contract or remain release-blocked.

[Back to top](#top)

---

<a id="illustrative-inactive-profile"></a>

## Illustrative inactive profile

The example below is intentionally incomplete, non-canonical, inactive, and unsuitable for execution. It illustrates separation of concerns; it does not define the accepted schema.

```yaml
# ILLUSTRATIVE ONLY — NOT ACTIVE — NOT CANONICAL
spec_id: habitat.example.review-only
spec_version: 0.0.0
status: DRAFT
active: false

binding:
  schema_ref: NEEDS_VERIFICATION
  parser_ref: NEEDS_VERIFICATION
  consumer_ref: NEEDS_VERIFICATION
  activation_decision_ref: null

scope:
  domain: habitat
  profile_family: example
  object_families: []
  allowed_input_states: []
  proposed_output_state: null

sources:
  source_descriptor_refs: []
  require_activation_decisions: true
  require_rights_clearance: true
  require_canonical_roles: true

time:
  require_source_time: true
  require_valid_time: true
  require_retrieval_time: true
  stale_behavior: HOLD

space:
  source_crs_ref: NEEDS_VERIFICATION
  analysis_crs_ref: NEEDS_VERIFICATION
  spatial_support_ref: NEEDS_VERIFICATION
  public_representation_ref: NEEDS_VERIFICATION

models:
  model_card_refs: []
  model_run_receipt_required: false
  model_is_observation: false
  model_is_regulatory: false

governance:
  evidence_bundle_required: true
  policy_decision_required: true
  human_review_required: true
  release_manifest_required: true
  correction_path_required: true
  rollback_target_required: true

failure:
  unresolved_source: HOLD
  unresolved_rights: DENY
  unresolved_sensitivity: RESTRICT
  unresolved_evidence: ABSTAIN
  policy_unavailable: ERROR
```

Do not copy this example into an active profile without an accepted schema, parser, consumer, source, policy, validation, review, receipt, proof, catalog, release, and rollback chain.

[Back to top](#top)

---

<a id="validation-and-enforceability"></a>

## Validation and enforceability

### Static validation

An active profile should pass:

- UTF-8 and final-newline checks;
- safe YAML parsing;
- duplicate-key rejection;
- schema and enum validation;
- required ref resolution;
- stable digest generation;
- path and authority-root validation;
- no-secrets scanning;
- no private-endpoint or sensitive-payload scanning;
- compatibility and migration checks;
- forbidden-field and forbidden-role-upgrade checks.

### Binding validation

Prove:

- the parser accepts the exact spec schema revision;
- the named consumer exists and declares compatibility;
- discovery resolves exactly one active profile;
- precedence is deterministic;
- duplicate specs fail closed;
- inactive/suspended/superseded profiles cannot run;
- source descriptors and activation records resolve;
- schedule binding is bounded and reviewable;
- kill switch works.

### Domain validation

Prove:

- object-family boundaries;
- source-role preservation;
- model/observation/regulatory separation;
- time-kind separation;
- spatial-support and scale discipline;
- native-class and crosswalk preservation;
- critical-habitat anti-collapse;
- NWI legal/hydrology boundary;
- connectivity/corridor non-observation posture;
- sensitivity and reconstruction-risk parity;
- evidence closure;
- finite non-answer behavior.

### Lifecycle validation

Prove:

- only allowed input stages are read;
- unresolved inputs route to quarantine or a finite blocker;
- writes are atomic and idempotent;
- output hashes and lineage are recorded;
- no direct jump to catalog, triplet, published, or release occurs;
- receipts are emitted to accepted homes;
- failed runs cannot mutate release pointers;
- correction and rollback preserve audit history.

### Public-surface validation

Prove parity across:

- API;
- map/tile;
- export;
- search;
- graph;
- vector index;
- cache;
- report;
- Evidence Drawer;
- Focus Mode;
- generated summary.

### Required negative scenarios

At minimum, tests should cover:

1. missing `spec_id`;
2. unknown schema revision;
3. duplicate YAML key;
4. unknown profile status;
5. inactive profile selected;
6. duplicate active profile;
7. missing parser or consumer;
8. unsupported parser/consumer version;
9. missing SourceDescriptor;
10. missing source activation;
11. unresolved rights;
12. legacy source role without reviewed mapping;
13. modeled result labeled observed;
14. suitability labeled critical habitat;
15. critical habitat labeled modeled;
16. NWI used as legal determination;
17. land cover used as occurrence proof;
18. ecoregion used as HabitatPatch;
19. connectivity used as observed movement;
20. missing time facet;
21. stale source;
22. CRS/grid mismatch;
23. missing valid-pixel or mask support;
24. unsafe cross-lane sensitive join;
25. missing EvidenceBundle;
26. policy engine unavailable;
27. receipt path unresolved;
28. catalog closure missing;
29. release manifest missing;
30. rollback target missing;
31. correction fails to invalidate downstream artifacts;
32. revoked artifact remains publicly resolvable.

### CI interpretation

The current Habitat workflow runs only:

```text
echo TODO validate-habitat
echo TODO build-proof-habitat
echo TODO publish-dry-run-habitat
```

A green result from those jobs is scaffold evidence only. It does not prove any requirement in this section.

[Back to top](#top)

---

<a id="review-activation-and-change-discipline"></a>

## Review, activation, and change discipline

### Minimum reviewer classes

Depending on scope:

- pipeline-spec steward;
- Habitat domain steward;
- executable consumer owner;
- source and rights steward;
- relevant object-family steward;
- model/method reviewer;
- spatial/CRS/topology reviewer;
- temporal/freshness reviewer;
- Fauna/Flora/Hydrology/Soil/Agriculture/Hazards cross-lane reviewer;
- sensitivity/geoprivacy/cultural/sovereignty reviewer;
- validation and evidence reviewer;
- policy reviewer;
- release and rollback reviewer;
- security reviewer.

### Change classes

| Change | Minimum posture |
|---|---|
| Documentation clarification | Routine review; no activation |
| Placeholder edit | Preserve inactive status |
| New draft profile | Schema, parser, consumer, source, test, and owner review |
| Source or rights change | Source/rights review and downstream impact analysis |
| Role or object-family change | Contract/schema/policy review |
| Model or method change | Model-card, validation, uncertainty, and invalidation review |
| Spatial precision/public representation change | Sensitivity and reconstruction-risk review |
| Activation | Separate approval record and rollback target |
| Schedule change | Freshness, load, incident, and kill-switch review |
| Release-capable change | Evidence, policy, catalog, release, correction, rollback closure |
| Canonical path/topology change | ADR or migration note as required |

### Separation of duties

At higher maturity, separate:

- author;
- validator/reviewer;
- source or rights approver;
- sensitivity/policy approver;
- release approver.

One generated change should not silently author, approve, activate, and release itself.

[Back to top](#top)

---

<a id="definition-of-done-for-an-active-specification"></a>

## Definition of done for an active specification

A Habitat profile is active only when all applicable items are verified:

- [ ] stable ID, version, digest, owner, and lineage;
- [ ] accepted pipeline-spec schema;
- [ ] hardened deterministic parser;
- [ ] verified executable consumer;
- [ ] discovery, precedence, duplicate, and activation contracts;
- [ ] separate activation decision;
- [ ] admitted SourceDescriptor refs and source activation records;
- [ ] rights, terms, attribution, access, and authority limits;
- [ ] canonical source-role mapping;
- [ ] accepted object-family contracts and schemas;
- [ ] knowledge-character and anti-collapse gates;
- [ ] temporal and freshness contract;
- [ ] spatial-support, CRS, scale, topology, and public representation;
- [ ] model/method card, validation, and uncertainty where applicable;
- [ ] sensitivity, geoprivacy, cultural, private-party, and reconstruction-risk review;
- [ ] lifecycle transitions and quarantine reasons;
- [ ] deterministic fixtures and executable positive/negative tests;
- [ ] validator versions and reports;
- [ ] EvidenceRef/EvidenceBundle closure;
- [ ] required receipts and proofs;
- [ ] catalog/triplet closure;
- [ ] release candidate and verified release contract;
- [ ] correction, invalidation, withdrawal, supersession, and rollback paths;
- [ ] security, no-secrets, bounded-resource, and logging review;
- [ ] CODEOWNERS or equivalent review enforcement;
- [ ] substantive CI;
- [ ] activation and rollback drill;
- [ ] public resolver verification if the profile can publish.

Until then, keep the profile inactive.

[Back to top](#top)

---

<a id="rollback-correction-and-deactivation"></a>

## Rollback, correction, and deactivation

### Documentation rollback

Before merge:

- close the draft PR;
- abandon the scoped branch.

After merge:

- use a transparent revert commit or revert PR;
- restore v0.1 if required;
- remove the paired generated receipt only through the same transparent revert;
- do not rewrite shared history.

No runtime rollback is required for this README-only change.

### Future active-profile rollback

A governed rollback should:

1. suspend discovery and scheduling;
2. revoke or suspend the activation decision;
3. preserve spec, parser, consumer, source, policy, model, and run lineage;
4. prevent new lifecycle writes;
5. hold pending candidates;
6. restore a reviewed prior profile or remain disabled;
7. re-evaluate source roles, rights, time, space, model, sensitivity, evidence, and release state;
8. inventory downstream records and artifacts;
9. emit correction, withdrawal, supersession, and rollback records;
10. invalidate affected catalog, triplet, layer-registry, cache, tile, export, search, graph, vector-index, and generated-summary surfaces;
11. rerun deterministic validation and reconstruction-risk checks;
12. verify revoked artifacts are no longer publicly resolvable;
13. record closure and lessons learned.

### Emergency deactivation

An emergency kill switch may stop execution. It must not erase evidence or silently rewrite release state. Follow with a reviewed correction and rollback process.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Status |
|---|---|---|
| `HAB-SPEC-001` | Confirm Habitat pipeline-spec owner and CODEOWNERS coverage | NEEDS VERIFICATION |
| `HAB-SPEC-002` | Confirm exhaustive direct-lane inventory | NEEDS VERIFICATION |
| `HAB-SPEC-003` | Decide whether flat placeholders remain, migrate to child lanes, or retire | NEEDS VERIFICATION / ADR or migration note |
| `HAB-SPEC-004` | Confirm accepted Habitat pipeline-spec schema | UNKNOWN |
| `HAB-SPEC-005` | Confirm parser, registry, discovery, and precedence | UNKNOWN |
| `HAB-SPEC-006` | Confirm executable consumers and supported profile families | UNKNOWN |
| `HAB-SPEC-007` | Confirm scheduler and activation-record authority | UNKNOWN |
| `HAB-SPEC-008` | Confirm source-registry topology | NEEDS VERIFICATION |
| `HAB-SPEC-009` | Confirm source-role vocabulary and legacy mapping | NEEDS VERIFICATION |
| `HAB-SPEC-010` | Confirm admitted Habitat SourceDescriptors | UNKNOWN |
| `HAB-SPEC-011` | Confirm source rights, terms, attribution, and cadence | NEEDS VERIFICATION |
| `HAB-SPEC-012` | Confirm NLCD connector and source-record topology | NEEDS VERIFICATION |
| `HAB-SPEC-013` | Confirm NWI source and regulatory/hydrology boundary | NEEDS VERIFICATION |
| `HAB-SPEC-014` | Confirm critical-habitat source, rights, legal scope, and correction | NEEDS VERIFICATION |
| `HAB-SPEC-015` | Confirm canonical Habitat contract paths and aliases | NEEDS VERIFICATION |
| `HAB-SPEC-016` | Confirm complete Habitat schema inventory | NEEDS VERIFICATION |
| `HAB-SPEC-017` | Confirm which schemas are field-complete and active | UNKNOWN |
| `HAB-SPEC-018` | Confirm schema registry and migration records | UNKNOWN |
| `HAB-SPEC-019` | Confirm object-family identity rules | NEEDS VERIFICATION |
| `HAB-SPEC-020` | Confirm temporal and freshness vocabularies | NEEDS VERIFICATION |
| `HAB-SPEC-021` | Confirm CRS, scale, topology, raster, mask, and precision profiles | NEEDS VERIFICATION |
| `HAB-SPEC-022` | Confirm model-card, calibration, fitness, and uncertainty requirements | NEEDS VERIFICATION |
| `HAB-SPEC-023` | Confirm field-level Habitat policy | UNKNOWN |
| `HAB-SPEC-024` | Confirm sensitivity/geoprivacy policy and transform profiles | UNKNOWN |
| `HAB-SPEC-025` | Confirm cultural, sovereign, private-land, and living-person review paths | NEEDS VERIFICATION |
| `HAB-SPEC-026` | Confirm public attribute allowlists and reconstruction-risk tests | NEEDS VERIFICATION |
| `HAB-SPEC-027` | Confirm fixture payload inventory and consumers | NEEDS VERIFICATION |
| `HAB-SPEC-028` | Confirm executable test modules and pass rates | UNKNOWN |
| `HAB-SPEC-029` | Confirm executable Habitat validators | UNKNOWN |
| `HAB-SPEC-030` | Confirm receipt schemas, destinations, and emitted instances | NEEDS VERIFICATION |
| `HAB-SPEC-031` | Confirm proof schemas, validators, and emitted proof packs | UNKNOWN |
| `HAB-SPEC-032` | Confirm catalog/triplet closure and child topology | NEEDS VERIFICATION |
| `HAB-SPEC-033` | Confirm layer-registry authority and released layer refs | UNKNOWN |
| `HAB-SPEC-034` | Confirm release-manifest path/schema and Habitat instances | UNKNOWN |
| `HAB-SPEC-035` | Confirm correction propagation and downstream invalidation | NEEDS VERIFICATION |
| `HAB-SPEC-036` | Confirm rollback tooling and drills | UNKNOWN |
| `HAB-SPEC-037` | Replace TODO-only Habitat CI with substantive checks | NEEDS VERIFICATION |
| `HAB-SPEC-038` | Confirm runtime deployment, schedules, APIs, layers, and public consumers | UNKNOWN |
| `HAB-SPEC-039` | Reconcile planning tracker against current repo evidence | NEEDS VERIFICATION |
| `HAB-SPEC-040` | Confirm documentation update triggers for child profile changes | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `pipeline_specs/habitat/README.md` prior blob | CONFIRMED | Existing v0.1 parent boundary and stale proposed tree | Did not reflect actual inventory |
| Five flat Habitat YAML files | CONFIRMED placeholders | Preserved planned profile names | No active spec contract |
| `pipeline_specs/habitat/ecoregions/README.md` | CONFIRMED v0.2 documentation | Grounded ecoregion child boundary | No active child profile |
| `pipeline_specs/habitat/land_cover/README.md` | CONFIRMED v0.2 documentation | Grounded land-cover child boundary | No active child profile |
| `pipeline_specs/README.md` | CONFIRMED root contract | Specs are declarative what, not executable how | Does not prove Habitat implementation |
| `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` | CONFIRMED planning tracker | Origin of placeholder inventory | Explicitly not repo implementation proof |
| `pipelines/domains/habitat/README.md` | CONFIRMED draft docs | Executable responsibility and anti-collapse intent | Behavior, schedules, activation, CI, release unverified |
| `configs/domains/habitat/README.md` | CONFIRMED README-only config lane | No-secrets and non-authority posture | No executable consumer binding |
| `contracts/domains/habitat/README.md` | CONFIRMED draft contracts | Semantic object boundaries | Does not enforce runtime behavior |
| `schemas/contracts/v1/domains/habitat/README.md` | CONFIRMED draft index | Schema-lane placement | Inventory incomplete and stale |
| Representative Habitat schemas | CONFIRMED permissive scaffolds | Machine-shaped placeholders | Empty properties / no field enforcement |
| `data/registry/sources/habitat/README.md` | CONFIRMED experimental registry | Admission and source-role posture | Topology unresolved; sources not proven active |
| `control_plane/source_authority_register.yaml` | CONFIRMED empty PROPOSED register | No registered source activation | Does not prove absence of all other controls |
| `policy/domains/habitat/README.md` | CONFIRMED scaffold | Policy responsibility home | No field-level Habitat policy |
| `policy/sensitivity/habitat_classes.yaml` | CONFIRMED placeholder | Sensitivity inventory slot | No enforcement |
| `tests/domains/habitat/README.md` | CONFIRMED documentation index | Broad intended test coverage | Executable tests and pass rates unverified |
| `fixtures/domains/habitat/README.md` | CONFIRMED documentation index | Broad fixture child inventory | No parent payload inventory verified |
| `tools/validators/domains/habitat/README.md` | CONFIRMED index-only | Validator responsibilities | No child validators confirmed |
| `data/receipts/habitat/README.md` | CONFIRMED draft | Habitat receipt parent, land-cover child | No emitted chain; layout unresolved |
| `data/proofs/habitat/README.md` | CONFIRMED draft | Intended proof responsibilities | Emitted proof packs unknown |
| `data/catalog/domain/habitat/README.md` | CONFIRMED draft | Catalog parent and ecoregions child | Broader inventory and closure unverified |
| Layer-registry placeholder YAMLs | CONFIRMED placeholders | Planned layer slots | No release/public authority |
| `release/candidates/habitat/README.md` | CONFIRMED draft | Candidate review lane | Candidate is not release |
| `.github/workflows/domain-habitat.yml` | CONFIRMED TODO-only | Workflow trigger and scaffold jobs | No substantive Habitat validation |
| `.github/CODEOWNERS` | CONFIRMED placeholder | Generic repository ownership | No Habitat spec review enforcement |
| `docs/doctrine/directory-rules.md` | CONFIRMED placement doctrine | Responsibility-root and lifecycle boundaries | Specific paths still require repo verification |

### Evidence interpretation

The evidence supports strong claims about:

- current file presence;
- placeholder shape;
- documentation boundaries;
- unresolved topology and authority conflicts;
- absence at exact checked paths;
- lack of proven parser/activation/consumer binding in bounded searches.

It does not support claims that:

- the repository has no relevant code anywhere;
- any source is active;
- any schema is canonical or complete;
- tests pass;
- policy is enforced;
- receipts/proofs are emitted;
- a public layer is released;
- a runtime or schedule is deployed.

[Back to top](#top)

---

## v0.1 preservation assessment

### Preserved

- `pipeline_specs/` versus `pipelines/` separation;
- lifecycle invariant;
- Habitat context and anti-collapse posture;
- source, evidence, receipt, policy, release, correction, and rollback gates;
- land-cover, suitability, connectivity, restoration, stewardship, wetland/riparian, and public-safe profile concepts;
- no public release or executable side effect from specs.

### Corrected

- speculative flat tree replaced with actual direct inventory;
- five YAMLs classified as placeholders rather than active or merely future filenames;
- ecoregions and land-cover child READMEs indexed;
- tests and fixtures pointed to verified domain lanes;
- receipt guidance pointed to the verified Habitat receipt parent;
- proof, catalog, source, release, schema, policy, validator, CI, and ownership maturity bounded by evidence;
- activation separated from merge, parse, schedule, layer registration, and dry-run success;
- source-role, model/regulatory, time, spatial, sensitivity, and reconstruction-risk requirements strengthened.

### Not resolved

- canonical spec schema;
- active parser/consumer;
- source activation;
- topology conflicts;
- field-level schema/policy enforcement;
- substantive tests/validators/CI;
- receipt/proof/catalog/release closure;
- runtime/public deployment.

---

## Maintainer checklist

Before adding or editing a Habitat profile:

- [ ] confirm the responsibility path against Directory Rules;
- [ ] inspect current parent and child inventories;
- [ ] avoid parallel authority;
- [ ] choose an accepted schema;
- [ ] identify parser and consumer;
- [ ] keep the profile inactive by default;
- [ ] reference admitted sources and roles;
- [ ] preserve object-family and cross-domain ownership;
- [ ] declare time and spatial support;
- [ ] preserve model/regulatory/observation distinctions;
- [ ] fail closed on sensitivity and rights;
- [ ] define lifecycle and finite outcomes;
- [ ] require evidence, receipts, proof, review, catalog, and release as applicable;
- [ ] add deterministic positive and negative tests;
- [ ] define correction, invalidation, and rollback;
- [ ] update this README when inventory or topology changes;
- [ ] attach generated-work provenance for AI-authored changes.

---

## Maintainer note

Keep this lane declarative.

Do not place executable code, source clients, source descriptors, contracts, schemas, policy decisions, real fixtures, tests, lifecycle outputs, receipt instances, EvidenceBundles, proof packs, catalog records, release decisions, public API/UI code, tiles, sensitive locations, private identities, credentials, private endpoints, or generated claims here.

Reference accepted authority-bearing objects by stable identifier and revision. When evidence is incomplete, narrow the profile, keep it inactive, and record the blocker.

[Back to top](#top)
