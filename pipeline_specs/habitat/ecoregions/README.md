<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-ecoregions-readme
title: pipeline_specs/habitat/ecoregions/ — Governed Habitat Ecoregions Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; no-active-ecoregion-spec-established; join-sensitivity-aware
owners: OWNER_TBD — Pipeline-spec steward · Habitat steward · Ecoregions steward · Spatial Foundation reviewer · Source and rights steward · Fauna/Flora join reviewer · Sensitivity/geoprivacy reviewer · Pipeline consumer owner · Temporal/vintage steward · Validation steward · Evidence steward · Policy steward · Release steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; habitat; ecoregions; regionalization-context; declarative-only; framework-aware; hierarchy-aware; source-role-aware; version-aware; time-aware; CRS-aware; topology-aware; cross-lane-aware; join-sensitivity-aware; reconstruction-resistant; no-secrets; no-live-activation; no-direct-source-access; no-direct-lifecycle-write; no-release-authority
current_path: pipeline_specs/habitat/ecoregions/README.md
truth_posture: CONFIRMED current target and prior blob, parent Habitat spec README, README-only direct ecoregions spec lane in bounded indexed search, absent pipeline_specs/habitat/ecoregions.yaml exact path, draft executable ecoregion pipeline documentation, README-only candidate semantic-contract lane, schema index with no confirmed concrete ecoregion schemas, source-registry child with subtype-first/domain-first topology conflict, draft test and fixture READMEs with executable payload and consumer alignment unverified, generic Habitat policy scaffold and absent standalone sensitivity README, Habitat validator index with no confirmed child validators, Habitat receipt parent with no ecoregion child confirmed, draft Habitat proof/catalog/release-candidate/published-layer documentation, TODO-only domain-habitat workflow, and placeholder CODEOWNERS / PROPOSED minimum active-spec contract, finite status and outcome vocabularies, deterministic parser and consumer binding, framework/version/hierarchy/identity/time/CRS/topology/context-join gates, activation/deactivation discipline, validation matrix, correction propagation, and rollback requirements / UNKNOWN accepted ecoregion pipeline-spec schema, parser, registry, discovery, scheduler, activation records, executable consumers, runtime behavior, substantive CI enforcement, emitted ecoregion receipts, proof closure, release integration, deployed schedules, and public use / NEEDS VERIFICATION owners, exhaustive recursive inventory, canonical source-registry topology, canonical source-role mapping, admitted SourceDescriptors, current rights and terms, accepted framework/version vocabularies, object contracts and schemas, temporal semantics, CRS/scale/topology profiles, field-level policy, public attribute allowlists, fixture payloads, executable tests, validator wiring, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9ede51fb0999fcda37e3335a4cf747850908510c
  prior_blob: 0309f16998ab65f6d3ef599b6a401c7798981266
  direct_lane_files:
    - pipeline_specs/habitat/ecoregions/README.md
  direct_lane_posture: README-only in bounded indexed search; no active child profile established
  workflow_posture: domain-habitat is pull-request-triggered TODO scaffolding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../../pipelines/domains/habitat/ecoregions/README.md
  - ../../../configs/domains/habitat/README.md
  - ../../../contracts/domains/habitat/ecoregions/README.md
  - ../../../schemas/contracts/v1/domains/habitat/ecoregions/README.md
  - ../../../data/registry/sources/habitat/ecoregions/README.md
  - ../../../data/receipts/habitat/README.md
  - ../../../data/proofs/habitat/README.md
  - ../../../data/catalog/domain/habitat/ecoregions/README.md
  - ../../../data/published/layers/habitat/ecoregions/README.md
  - ../../../tests/domains/habitat/ecoregions/README.md
  - ../../../fixtures/domains/habitat/ecoregions/README.md
  - ../../../tools/validators/domains/habitat/README.md
  - ../../../policy/domains/habitat/README.md
  - ../../../release/candidates/habitat/ecoregions/README.md
  - ../../../.github/workflows/domain-habitat.yml
  - ../../../.github/CODEOWNERS
notes:
  - "v0.2 replaces the planning-only proposed profile tree with commit-pinned repository evidence and classifies the direct specification lane as README-only."
  - "The exact pipeline_specs/habitat/ecoregions.yaml path referenced by executable documentation was not present at the evidence snapshot."
  - "The verified test and fixture homes are tests/domains/habitat/ecoregions/ and fixtures/domains/habitat/ecoregions/. The verified Habitat receipt parent is data/receipts/habitat/; no ecoregion child receipt lane was confirmed."
  - "Ecoregions are regionalization context. Framework, version, hierarchy, source role, time, geometry lineage, public-safe representation, and owning-domain truth must remain explicit."
  - "No executable specification, source record, connector, pipeline, config payload, schema, contract, policy rule, fixture, test, validator, workflow, lifecycle object, receipt instance, proof, catalog object, release object, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Habitat Ecoregions Pipeline Specification Boundary

`pipeline_specs/habitat/ecoregions/`

> Declarative run-intent boundary for Habitat ecoregion and biophysical-regionalization processing. A reviewed active specification may state **what** a verified consumer should process, against which admitted sources, under which framework, version, hierarchy, time, CRS, topology, evidence, sensitivity, policy, receipt, review, correction, and release gates. It does not execute a pipeline, admit a source, decide ecological or regulatory truth, create evidence, perform a public-safe transform, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-README--only-lightgrey)
![truth](https://img.shields.io/badge/ecoregions-context__not__occurrence-critical)
![sensitivity](https://img.shields.io/badge/join__risk-fail__closed-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)
![posture](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit-and-corrected-paths) · [Contract](#minimum-active-specification-contract) · [Activation](#status-activation-and-discovery) · [Sources](#sources-rights-and-source-roles) · [Frameworks](#framework-version-hierarchy-and-identity) · [Time](#time-vintage-freshness-and-correction) · [Space](#spatial-support-crs-topology-and-public-representation) · [Joins](#context-joins-sensitivity-and-reconstruction-risk) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Evidence](#evidence-receipts-proof-catalog-and-release) · [Validation](#validation-and-enforceability) · [Review](#review-activation-and-change-discipline) · [Done](#definition-of-done-for-an-active-specification) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@9ede51fb0999fcda37e3335a4cf747850908510c`  
> **Target blob before this revision:** `0309f16998ab65f6d3ef599b6a401c7798981266`  
> **Direct lane:** this README only in bounded indexed search  
> **Active specifications:** none established  
> **Referenced `pipeline_specs/habitat/ecoregions.yaml`:** not present at the exact checked path  
> **Activation:** filename, merge state, syntax validity, schedule text, fixture success, policy prose, catalog presence, or a successful dry run activates nothing

> [!CAUTION]
> A valid ecoregion specification cannot turn a regionalization polygon into species occurrence, plant occurrence, HabitatPatch quality, critical-habitat designation, hydrologic truth, soil truth, hazard truth, agricultural truth, land/title truth, or release approval. Missing framework, version, hierarchy, source role, rights, time, CRS, boundary lineage, evidence, policy, review, correction, rollback, or release state fails closed.

---

## Purpose

`pipeline_specs/habitat/ecoregions/` is the Habitat ecoregions segment under the `pipeline_specs/` responsibility root.

Its safe future role is to hold small, reviewed, deterministic declarative profiles that bind:

- stable specification identity, immutable version and digest, owner, status, and supersession lineage;
- one accepted parser and one verified executable consumer;
- admitted `SourceDescriptor` references and canonical source roles;
- source rights, attribution, redistribution, terms, access, cadence, and authority limits;
- ecoregion framework identity, native classification system, hierarchy level, source version, and boundary version;
- region identity, native code, native label, parent/child relations, and crosswalk posture;
- source, valid, retrieval, processing, release, correction, and supersession times;
- source CRS, processing CRS, tiling CRS, spatial support, extent, scale, resolution, topology, and uncertainty;
- input and output lifecycle states;
- context-join ownership and sensitivity rules;
- public attribute allowlists and public-safe representation requirements;
- validation, evidence, policy, review, receipt, proof, catalog, release, correction, and rollback requirements;
- deterministic no-network fixtures, finite outcomes, idempotency, and replay expectations.

This README is not a pipeline-spec schema, parser, registry, scheduler, activation decision, executable pipeline, source descriptor, semantic contract, schema, policy decision, geoprivacy transform, receipt, proof, catalog record, release record, public API, map layer, or generated answer.

### Audience

- Habitat and ecoregions stewards;
- Spatial Foundation, CRS, topology, and map-layer reviewers;
- source, rights, and source-role stewards;
- Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Archaeology, and People/Land liaisons;
- sensitivity, geoprivacy, cultural, and reconstruction-risk reviewers;
- pipeline-spec maintainers and executable consumer owners;
- validation, evidence, policy, release, correction, rollback, security, and documentation reviewers.

[Back to top](#top)

---

## Authority and anti-collapse

### What an active specification may declare

A reviewed active specification may declare:

- which verified executable consumer is eligible to read it;
- which admitted source identifiers and roles are in scope;
- which framework, version, hierarchy level, extent, and object family are requested;
- which input and output lifecycle states are allowed;
- which geometry, time, evidence, policy, review, receipt, catalog, and release gates apply;
- which finite outcome is required when a gate cannot close.

### What this lane cannot decide

A specification cannot decide:

- that a source is admitted, active, current, authoritative, or rights-cleared;
- that a legacy source-role word is an accepted canonical role;
- that two frameworks, levels, codes, labels, regions, boundaries, snapshots, or crosswalk entries are equivalent;
- that a newer source version silently supersedes an older release;
- that an ecoregion proves species or plant presence;
- that an ecoregion is a habitat patch, ecological-system observation, suitability result, regulatory designation, watershed, survey unit, or land parcel;
- that a derived crosswalk is lossless or authoritative;
- that exact or generalized geometry is public-safe;
- that a public attribute allowlist has been reviewed or applied;
- that evidence closes a claim;
- that validation, policy, review, catalog closure, or release approval exists;
- that public clients may bypass governed interfaces.

### Disallowed collapses

```text
spec file -> executable pipeline
parse success -> active specification
profile merge -> source activation
source list -> source authority
legacy role word -> accepted source role
framework A -> framework B
Level III -> Level IV
native code -> stable KFM identity
crosswalk -> identity equivalence
source snapshot -> current truth
ecoregion polygon -> species occurrence
ecoregion polygon -> plant occurrence
ecoregion polygon -> HabitatPatch
ecoregion context -> critical-habitat designation
ecoregion context -> hydrology / soil / hazards / agriculture truth
PLSS or HUC boundary -> ecoregion identity
model or aggregate -> observation
representation requirement -> performed transform
tile or render output -> canonical geometry
successful run -> EvidenceBundle
catalog entry -> release approval
publish profile -> PUBLISHED
generated summary -> evidence
```

### Required separations

| Concern | Authority home | Specification relationship |
|---|---|---|
| Human doctrine and ecoregion explanation | `docs/domains/habitat/` | Reference only. |
| Semantic object meaning | `contracts/domains/habitat/ecoregions/` | Reference accepted contract IDs. |
| Machine shape | `schemas/contracts/v1/domains/habitat/ecoregions/` or accepted schema home | Validate against accepted schema IDs. |
| Source identity, role, rights, cadence, and admission | Accepted source-registry home | Reference admitted records; do not recreate them. |
| Executable behavior | `pipelines/domains/habitat/ecoregions/` or accepted consumer | Bind to one verified consumer. |
| Configuration support | `configs/domains/habitat/` | Reference accepted settings; do not hide authority in config. |
| Policy and sensitivity decisions | `policy/` and review artifacts | Require decisions; do not assert them. |
| Lifecycle records | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` | Declare allowed transitions only. |
| Receipts | `data/receipts/habitat/` and accepted shared receipt homes | Declare required receipt classes. |
| Proof and evidence closure | `data/proofs/habitat/` and accepted evidence homes | Require resolvable references. |
| Catalog | `data/catalog/domain/habitat/ecoregions/` and governed projections | Require closure; never create catalog truth here. |
| Release | `release/` | Require release inputs; never approve release. |
| Public clients | Governed APIs and released artifacts | No direct access to specs or internal stores. |

[Back to top](#top)

---

## Current status

### Repository maturity matrix

| Surface | Current-session status | What is established | What is not established |
|---|---|---|---|
| Target README | CONFIRMED v0.1 before revision | Existing declarative boundary | Active specification behavior |
| Direct spec lane | CONFIRMED README-only in bounded indexed search | Documentation path | Child profiles, registry entries, active specs |
| Referenced `pipeline_specs/habitat/ecoregions.yaml` | CONFIRMED absent at exact checked path | Documentation drift signal | Replacement path or migration decision |
| Parent Habitat spec README | CONFIRMED v0.1 draft | Parent declarative doctrine | Grounded active profiles |
| Executable ecoregion pipeline README | CONFIRMED draft documentation | Intended executable boundary | Concrete consumer, schedule, runtime, tests |
| Habitat config lane | CONFIRMED README plus `.gitkeep` in its evidence snapshot | Non-authoritative config boundary | Ecoregion payload or direct consumer binding |
| Ecoregion contract lane | CONFIRMED README-only candidate index | Candidate semantic families | Accepted individual contracts |
| Ecoregion schema lane | CONFIRMED draft index | Proposed schema home | Concrete accepted schemas |
| Source registry | CONFIRMED child README | Admission guidance and topology conflict | Admitted ecoregion descriptors or activation decisions |
| Source-role vocabulary | CONFLICTED | Registry lists canonical seven-role vocabulary | Mapping from legacy `authority/context/model` prose |
| Domain policy | CONFIRMED greenfield scaffold | Policy root exists | Ecoregion-specific binding policy |
| Standalone Habitat sensitivity README | CONFIRMED absent at exact checked path | No file at checked path | Final sensitivity-policy topology |
| Habitat validator lane | CONFIRMED index-only README | Proposed validator boundary | Ecoregion validator child or executable validator |
| Ecoregion tests | CONFIRMED draft README | Intended test home and invariants | Executable tests, runners, pass rates |
| Ecoregion fixtures | CONFIRMED draft README | Intended fixture home | Verified fixture payloads and consumers |
| Habitat receipts | CONFIRMED domain parent README | Receipt family and land-cover child | Ecoregion receipt child or emitted receipts |
| Habitat proofs | CONFIRMED draft README | Proposed proof responsibilities | Emitted proof packs and closure |
| Ecoregion catalog | CONFIRMED draft README | CATALOG-stage boundary | Actual catalog inventory and closure |
| Ecoregion release candidate | CONFIRMED short draft README | Pre-release review boundary | Candidate dossiers and decisions |
| Published ecoregion layer lane | CONFIRMED draft README | PUBLISHED responsibility boundary | Verified released artifact inventory |
| `domain-habitat` workflow | CONFIRMED TODO-only | PR-triggered scaffold | Substantive ecoregion enforcement |
| CODEOWNERS | CONFIRMED placeholder | Broad ownership placeholders | Named Habitat/ecoregion owners |
| Runtime and public use | UNKNOWN | None established | Deployment, schedules, routes, consumers |

### Safe conclusion

The repository documents a coherent intended ecoregion trust path, but the direct pipeline-specification lane is not active. No current-session evidence establishes a machine schema, parser, registry, scheduler, activation record, executable consumer, ecoregion-specific validator, spec-specific test, emitted receipt, proof closure, or release integration.

[Back to top](#top)

---

## Current inspected inventory

### Direct lane

```text
pipeline_specs/habitat/ecoregions/
└── README.md
```

This inventory is bounded by current indexed search and exact-path checks. It is not an exhaustive recursive filesystem assertion beyond the evidence available in this session.

### Planning-only names removed from the current tree claim

The v0.1 README listed these as proposed future names:

```text
ingest.yaml
normalize.yaml
validate.yaml
catalog.yaml
triplets.yaml
publish.yaml
rollback.yaml
watchers.yaml
framework_epa_omernik.yaml
framework_usfs_bailey.yaml
hierarchy_checks.yaml
geometry_release.yaml
```

v0.2 preserves their conceptual coverage but does not present them as repository files. Any future profile requires Directory Rules review, accepted schema and consumer binding, activation discipline, tests, and rollback.

[Back to top](#top)

---

## Repository fit and corrected paths

### Owning root

`pipeline_specs/` owns declarative run intent—the **what**. The existing `habitat/ecoregions/` nesting is a domain-and-sublane segment within that responsibility root, not a new authority root.

### Corrected current-session paths

| Responsibility | Verified or bounded path | Current posture |
|---|---|---|
| Ecoregion specification docs | `pipeline_specs/habitat/ecoregions/` | README-only |
| Executable ecoregion pipeline docs | `pipelines/domains/habitat/ecoregions/` | Draft documentation |
| Ecoregion contracts | `contracts/domains/habitat/ecoregions/` | README-only candidate index |
| Ecoregion schemas | `schemas/contracts/v1/domains/habitat/ecoregions/` | Draft index; no concrete schema confirmed |
| Ecoregion tests | `tests/domains/habitat/ecoregions/` | Draft README; executable coverage unverified |
| Ecoregion fixtures | `fixtures/domains/habitat/ecoregions/` | Draft README; payload inventory unverified |
| Ecoregion source registry | `data/registry/sources/habitat/ecoregions/` | Draft child; topology unresolved |
| Habitat receipt parent | `data/receipts/habitat/` | Confirmed parent; no ecoregion child confirmed |
| Habitat proofs | `data/proofs/habitat/` | Draft proof guide |
| Ecoregion catalog | `data/catalog/domain/habitat/ecoregions/` | Draft CATALOG boundary |
| Ecoregion release candidates | `release/candidates/habitat/ecoregions/` | Short draft README |
| Released ecoregion layers | `data/published/layers/habitat/ecoregions/` | Draft PUBLISHED boundary |

### Placement conflicts and drift

1. **Source registry topology:** both subtype-first and domain-first Habitat source-registry forms are documented. Do not maintain divergent source authority.
2. **Source-role vocabulary:** doctrine and older notes use `authority`, `context`, and `model`; current source-registry guidance lists `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`. Mapping is unresolved.
3. **Missing flat spec path:** executable documentation references `pipeline_specs/habitat/ecoregions.yaml`, but that exact path is absent.
4. **Sensitivity-policy topology:** `policy/domains/habitat/README.md` is a generic scaffold; the exact standalone `policy/sensitivity/habitat/README.md` path is absent.
5. **Receipt topology:** the old pipeline-specific ecoregion receipt path is absent; the verified parent is `data/receipts/habitat/`, whose exact subtype layout remains unresolved.
6. **Schema maturity:** the ecoregion schema path is an index only; candidate schemas are not implementation evidence.

These are surfaced for steward resolution. This README does not choose a canonical alternative by assertion.

[Back to top](#top)

---

## Minimum active specification contract

A specification is not eligible for active discovery until every required field is machine-valid, references resolve, review closes, and a separate activation record authorizes use.

### Identity and governance

Required:

- stable `spec_id`;
- immutable semantic version;
- canonical content digest and canonicalization profile;
- domain `habitat`;
- sublane `ecoregions`;
- finite status;
- owner and required reviewer roles;
- creation and update time;
- supersedes and rollback lineage;
- reason for activation or deactivation.

### Parser, registry, consumer, and activation

Required:

- accepted schema identifier and version;
- accepted parser identifier and version;
- deterministic duplicate and precedence behavior;
- one verified executable consumer identifier and version;
- discovery or registry entry;
- separate activation-record identifier and state;
- effective time and optional expiration;
- source, framework, version, and environment scope;
- fail-closed behavior for unknown fields, missing refs, unsupported versions, or consumer mismatch.

### Source and rights

Required per source:

- admitted `SourceDescriptor` reference;
- canonical source role;
- upstream authority and authority limit;
- access method;
- rights, attribution, redistribution, derivative-use, and terms posture;
- source cadence and expected update behavior;
- source-head or release identity;
- source version, publication date, retrieval time, and checksum or manifest reference;
- sensitivity and restricted-join posture;
- correction, withdrawal, and supersession references.

### Framework and hierarchy

Required:

- stable framework identifier;
- native framework name and version;
- hierarchy vocabulary and level identifier;
- native region code and label;
- stable region identity strategy;
- parent and child constraints;
- allowed root and leaf levels;
- duplicate, cycle, orphan, and conflicting-parent behavior;
- cross-framework crosswalk reference, method, loss statement, review state, and rollback target when used;
- explicit prohibition on silent framework or level substitution.

### Spatial and temporal context

Required:

- source CRS;
- processing CRS where different;
- tiling/render CRS where different;
- transformation profile reference;
- source extent and expected domain extent;
- geometry type;
- topology profile;
- scale, resolution, and uncertainty;
- source, valid, retrieval, processing, release, correction, and supersession times;
- stale-state and source-version-change behavior;
- boundary lineage and correction propagation.

### Lifecycle and trust gates

Required:

- allowed input lifecycle state;
- allowed output lifecycle state;
- quarantine reasons;
- accepted contracts and schema refs;
- validation profile refs;
- evidence requirements;
- policy and review requirements;
- receipt classes;
- proof and catalog closure requirements;
- release-candidate and ReleaseManifest requirements;
- correction, withdrawal, invalidation, and rollback targets;
- public attribute allowlist and geometry representation profile for public candidates.

### Security and minimization

Required:

- no embedded credentials, tokens, cookies, private endpoints, or secrets;
- no uncontrolled network access;
- bounded payload size, feature count, geometry complexity, and processing time;
- safe logging and telemetry;
- no exact sensitive join keys or restricted occurrence detail;
- no operational geoprivacy parameters in public-facing documentation or logs;
- deterministic finite failure behavior.

[Back to top](#top)

---

## Status, activation, and discovery

### Proposed finite specification statuses

| Status | Meaning | Discoverable for execution |
|---|---|---:|
| `PLACEHOLDER` | Inventory or planning artifact only | No |
| `DRAFT` | In authoring; incomplete | No |
| `READY_FOR_REVIEW` | Validation complete enough for review | No |
| `APPROVED_INACTIVE` | Reviewed, but not activated | No |
| `ACTIVE` | Separate activation record permits bounded use | Yes |
| `SUSPENDED` | Temporarily disabled | No |
| `SUPERSEDED` | Replaced by a newer reviewed version | No |
| `RETIRED` | Permanently inactive but retained for audit | No |
| `REJECTED` | Review rejected | No |

### Activation invariant

```text
valid spec + merge + approval != active spec
active spec = approved immutable spec + verified consumer + separate activation record
```

Activation must identify:

- exact spec digest;
- parser and consumer versions;
- source and framework scope;
- allowed environment;
- activation owner and reviewer;
- effective time;
- rollback target;
- reason code.

### Illustrative inactive shape

The following is intentionally incomplete and non-canonical. It demonstrates boundary fields only.

```yaml
status: DRAFT
active: false

identity:
  spec_id: "kfm-pipeline-spec:habitat:ecoregions:example"
  version: "0.0.0-example"
  digest: "DIGEST_TBD"

binding:
  schema_ref: "SCHEMA_TBD"
  parser_ref: "PARSER_TBD"
  consumer_ref: "CONSUMER_TBD"
  activation_ref: null

scope:
  framework_ref: "FRAMEWORK_TBD"
  framework_version: "VERSION_TBD"
  hierarchy_level: "LEVEL_TBD"
  source_descriptor_refs: []

spatial:
  source_crs: "CRS_TBD"
  processing_crs: "CRS_TBD"
  public_representation_profile_ref: "PROFILE_TBD"

time:
  source_time: "TIME_TBD"
  valid_time: "TIME_TBD"
  retrieval_time: "TIME_TBD"

gates:
  validation_refs: []
  evidence_requirements: []
  policy_refs: []
  review_refs: []
  receipt_classes: []
  release_requirements: []

failure:
  unresolved_reference: HOLD
  unsafe_join: DENY
  evidence_gap: ABSTAIN
  internal_error: ERROR
```

No implementation should parse this example as an accepted schema or active profile.

[Back to top](#top)

---

## Sources, rights, and source roles

### Admission before reference

A specification may reference only admitted source identifiers. It cannot create or upgrade source admission.

```text
candidate source
-> SourceDescriptor
-> rights / role / cadence / sensitivity review
-> activation decision
-> eligible for bounded pipeline-spec reference
```

### Source-role discipline

The current source-registry guidance lists:

```text
observed
regulatory
modeled
aggregate
administrative
candidate
synthetic
```

Legacy words such as `authority`, `context`, and `model` must not be copied into active specs without an accepted mapping. `Context` is usually a use case or relation, not automatically a source role.

### Source-family boundaries

| Source family or fabric | Safe specification treatment | Forbidden upgrade |
|---|---|---|
| EPA/Omernik ecoregions | Named framework/version regionalization context after admission | Species, plant, patch-quality, or regulatory truth |
| USFS/Bailey ecoregions | Separate named framework/version after admission | Silent equivalence with EPA/Omernik |
| State or regional ecoregion crosswalk | Reviewed advisory transform with loss statement | Identity equivalence |
| PLSS | Administrative survey/location context | Ecoregion or land-title truth |
| WBD/HUC context | Hydrology-owned administrative/aggregate context | Habitat-owned hydrologic truth |
| GAP/LANDFIRE or similar classifications | Modeled or aggregate context per descriptor | Observation or occurrence truth |
| Derived ecoregion summaries | Aggregate or modeled output with receipts | Source authority |

### Rights and terms

An active spec must not infer redistribution, derivative-use, public-layer, or attribute-release rights from public accessibility. Missing or expired rights evidence yields `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN`, according to the governing policy.

[Back to top](#top)

---

## Framework, version, hierarchy, and identity

### Framework identity

Every record and run must preserve:

- framework identifier;
- native framework name;
- source authority;
- source version or edition;
- hierarchy vocabulary;
- level;
- region code;
- native label;
- source geometry lineage;
- source role.

Framework names are not interchangeable aliases. A cross-framework comparison is a relation, not an identity merge.

### Snapshot identity

A proposed `EcoregionSnapshot` identity should bind at least:

```text
framework
+ framework version
+ hierarchy level
+ source extent
+ boundary version
+ valid time
+ source digest
```

The accepted deterministic identity algorithm remains **NEEDS VERIFICATION**.

### Hierarchy rules

Validation must reject or hold:

- missing framework or level;
- unknown hierarchy vocabulary;
- duplicate native code within the same framework/version/level scope;
- parent/child cycles;
- orphan regions where a parent is required;
- child assigned to multiple conflicting parents;
- cross-framework parentage without an accepted crosswalk relation;
- silent Level III/Level IV substitution;
- inconsistent source and boundary versions.

### Crosswalk rules

A crosswalk must record:

- source and target frameworks and versions;
- source and target levels;
- method;
- confidence or uncertainty;
- known loss and many-to-many behavior;
- evidence and reviewer refs;
- correction and rollback targets.

A crosswalk is advisory unless a separate accepted contract and policy say otherwise. It never overwrites native classifications.

[Back to top](#top)

---

## Time, vintage, freshness, and correction

### Time kinds

An active specification must keep distinct where material:

| Time | Meaning |
|---|---|
| `source_time` | Time represented or published by the upstream source |
| `valid_time` | Time interval for which the regionalization or boundary is intended to apply |
| `retrieval_time` | Time KFM retrieved the source |
| `processing_time` | Time a governed run transformed the source |
| `release_time` | Time a released artifact became effective |
| `correction_time` | Time a correction or withdrawal became effective |
| `supersession_time` | Time a newer framework/boundary version replaced prior use |

A file modification time is not source vintage.

### Freshness behavior

A spec must declare:

- expected cadence or static-source posture;
- stale threshold profile reference where applicable;
- behavior for source outage, missing version, or changed source head;
- whether an unchanged source yields deterministic `NOOP`;
- whether a new version triggers `HOLD`, review, or bounded candidate generation;
- correction propagation to processed records, catalog entries, tiles, indexes, caches, summaries, and released artifacts.

### Boundary change posture

A new boundary version does not silently rewrite historical joins. It creates new lineage and requires review of:

- changed identities and parentage;
- affected context joins;
- public layers and attributes;
- released summaries;
- correction or supersession notices;
- rollback targets.

[Back to top](#top)

---

## Spatial support, CRS, topology, and public representation

### Required spatial declarations

An active spec must state:

- source CRS and axis-order expectations;
- processing CRS;
- render or tiling CRS if different;
- accepted transformation profile;
- source extent and clipping posture;
- geometry type;
- topology rules;
- scale and resolution;
- uncertainty or positional-quality posture;
- boundary-version lineage;
- public representation profile.

### CRS discipline

Source CRS is provenance and must be retained. A render-oriented reprojection does not become canonical geometry. The doctrine describes preserving source CRS and using a web-map CRS only for tiling; the exact accepted profile and implementation remain **NEEDS VERIFICATION**.

### Topology checks

At minimum:

- geometry is valid under the accepted profile;
- rings and coordinate order are valid;
- no unexpected empty geometry;
- extent is plausible for the declared source;
- same-level overlaps and gaps follow the framework’s declared rules;
- parent coverage and child containment are checked where required;
- geometry repair does not silently change identity;
- every repair or generalization is receipt-backed where material.

### Public attribute and geometry posture

A public-layer candidate requires:

- explicit attribute include-list;
- exclusion of internal notes, join keys, unpublished IDs, sensitive flags, and restricted references;
- public-safe geometry profile;
- release-linked source/version summary;
- evidence and attribution refs;
- correction and rollback support.

A requirement to generalize is not proof that generalization occurred.

[Back to top](#top)

---

## Context joins, sensitivity, and reconstruction risk

Ecoregion polygons are usually low intrinsic sensitivity. Their joins can be high risk.

### Join ownership

A context join must preserve the owning domain for every joined claim:

| Joined concern | Owning authority retained |
|---|---|
| Animal occurrence and telemetry | Fauna |
| Plant occurrence, specimen, and rare-plant records | Flora |
| HabitatPatch condition or quality | Habitat patch/condition sublane |
| Regulatory critical habitat | Regulatory source and critical-habitat lane |
| Watersheds and hydrologic units | Hydrology |
| Soil properties and interpretations | Soil |
| Hazards | Hazards |
| Agricultural production or management | Agriculture |
| Archaeological, paleontological, cave, or cultural locations | Owning sensitive domain and steward |
| Parcels, title, and private identities | People/Land and rights authority |

### Fail-closed conditions

Use `DENY`, `RESTRICT`, `HOLD`, `QUARANTINE`, or `ABSTAIN` when:

- a join can reveal exact or reconstructable sensitive occurrence or site detail;
- small counts, small cells, unique categories, or repeated queries enable inference;
- public attributes expose restricted source IDs or join keys;
- the owning domain’s evidence, policy, review, or release state is missing;
- rights or cultural/stewardship authority is unresolved;
- a public summary can be reverse engineered into restricted detail;
- logs, receipts, notifications, exports, search indexes, vector indexes, graph edges, caches, tiles, or generated text would expose more than the approved derivative.

### No-leak rule

Do not place in active specs, examples, logs, reports, receipts, notifications, or public docs:

- real sensitive coordinates;
- rare-species or rare-plant locality clues;
- restricted site identifiers or join keys;
- private-person or landowner identities;
- culturally restricted knowledge;
- operational geoprivacy parameters;
- private endpoints or credentials;
- query patterns that facilitate reconstruction.

### Generated language

AI summaries may describe a released, evidence-backed ecoregion context. They cannot infer occurrence, condition, regulatory status, or sensitive presence from regionalization alone.

[Back to top](#top)

---

## Lifecycle gates and finite outcomes

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A specification declares eligible transitions. It does not perform or approve promotion.

### Proposed finite run outcomes

| Outcome | Meaning |
|---|---|
| `READY` | All preconditions for the next governed handoff are satisfied |
| `NOOP` | Inputs and relevant source state are unchanged |
| `HOLD` | Awaiting a resolvable dependency, review, or source state |
| `QUARANTINE` | Material requires isolated investigation |
| `NEEDS_REVIEW` | Human or steward decision is required |
| `ABSTAIN` | Evidence is insufficient for the requested claim or output |
| `DENY` | Policy or sensitivity prohibits the operation or exposure |
| `BLOCKED` | A required contract, schema, source, consumer, or release dependency is unavailable |
| `ERROR` | Deterministic internal or infrastructure failure |

### Minimum reason-code families

- `SPEC_*`
- `SOURCE_*`
- `RIGHTS_*`
- `FRAMEWORK_*`
- `HIERARCHY_*`
- `VERSION_*`
- `TIME_*`
- `CRS_*`
- `GEOMETRY_*`
- `TOPOLOGY_*`
- `JOIN_*`
- `SENSITIVITY_*`
- `EVIDENCE_*`
- `POLICY_*`
- `REVIEW_*`
- `RECEIPT_*`
- `CATALOG_*`
- `RELEASE_*`
- `CORRECTION_*`
- `ROLLBACK_*`
- `INTERNAL_*`

The accepted exact vocabulary remains **NEEDS VERIFICATION**.

### No-op and idempotency

Given identical accepted inputs, spec digest, parser, consumer, framework, source head, and policy context, replay must produce the same finite outcome and equivalent output digests. A no-op must still be auditable without fabricating a new source or release state.

[Back to top](#top)

---

## Evidence, receipts, proof, catalog, and release

### Trust-object separation

```text
specification != execution
execution receipt != proof
proof != catalog
catalog != release
release != public answer
```

### Expected references

An active spec may require references to:

- `SourceDescriptor`;
- source activation or intake decision;
- `RunReceipt`;
- transform, hierarchy, geometry, crosswalk, aggregation, model, validation, or public-representation receipts;
- `ValidationReport`;
- `PolicyDecision`;
- `ReviewRecord`;
- `EvidenceRef` and `EvidenceBundle`;
- proof pack or closure artifact;
- catalog record;
- release candidate;
- `PromotionDecision` and `ReleaseManifest`;
- `CorrectionNotice`;
- `RollbackCard`.

The exact accepted object names and homes remain **NEEDS VERIFICATION**.

### Corrected receipt posture

The verified Habitat receipt parent is:

```text
data/receipts/habitat/
```

No substantive ecoregion child receipt README was confirmed. The absent old path must not be used as proof that a pipeline-specific receipt topology exists.

### Catalog posture

`data/catalog/domain/habitat/ecoregions/` is a CATALOG-stage boundary. Catalog presence does not prove public release. A public-facing catalog entry must bind source, framework, version, evidence, policy, representation, release, correction, and rollback context.

### Published-layer posture

`data/published/layers/habitat/ecoregions/` is reserved for released public-safe bytes and direct sidecars. Directory presence does not prove that any specific artifact is released. Public clients resolve released artifacts through governed interfaces and release records.

[Back to top](#top)

---

## Validation and enforceability

### Structural specification checks

- accepted schema and version;
- canonical serialization and digest;
- required fields;
- unknown-field behavior;
- stable identity and immutable version;
- parser and consumer compatibility;
- activation-record resolution;
- source and contract reference resolution;
- no secrets or private endpoints;
- bounded resource profile.

### Framework and hierarchy checks

- framework and version present;
- hierarchy vocabulary and level valid;
- native code and label present;
- duplicate identities rejected;
- parent/child cycles rejected;
- orphan handling deterministic;
- conflicting parents rejected;
- cross-framework relations require reviewed crosswalk;
- level substitution prohibited;
- boundary and source versions consistent.

### Spatial and time checks

- source and processing CRS declared;
- transformation profile accepted;
- extent plausible;
- geometry and topology valid;
- source and boundary lineage retained;
- valid/retrieval/release/correction times distinct;
- stale and changed-source behavior deterministic;
- public allowlist and representation profile present for public candidates.

### Anti-collapse and sensitivity checks

- ecoregion cannot satisfy an occurrence requirement;
- ecoregion cannot satisfy HabitatPatch quality or critical-habitat designation;
- administrative and hydrologic context cannot become Habitat-owned truth;
- modeled or aggregate context cannot become observation;
- sensitive joins fail closed;
- public derivatives resist reconstruction across map, API, tile, export, search, graph, cache, log, receipt, notification, and generated-text surfaces.

### Evidence, policy, and release checks

- every claim-bearing output resolves evidence or returns a finite non-answer;
- policy and review refs resolve;
- required receipts exist and match exact inputs/outputs;
- proof and catalog closure are checked separately;
- release candidate is not treated as release;
- correction and rollback targets resolve;
- revoked or superseded artifacts are not publicly resolvable.

### Required negative tests

| Scenario | Expected result |
|---|---|
| Missing framework, level, source role, or version | `ERROR` or `HOLD` |
| Unknown schema, parser, consumer, or activation ref | `BLOCKED` |
| Duplicate region identity | validation failure |
| Parent/child cycle or conflicting parent | validation failure |
| Silent framework or level substitution | `DENY` or validation failure |
| Unreviewed lossy crosswalk | `NEEDS_REVIEW` or `HOLD` |
| Source rights unresolved | `HOLD`, `QUARANTINE`, or `DENY` |
| Ecoregion used as species/plant occurrence proof | `ABSTAIN` or `DENY` |
| Ecoregion used as patch-quality or regulatory proof | `ABSTAIN` or validation failure |
| Sensitive join would expose restricted detail | `DENY` or `RESTRICT` |
| Public layer lacks attribute allowlist or representation profile | promotion block |
| Evidence or policy service unavailable | `ERROR` or `ABSTAIN`, never public exposure |
| Source version changes without review | `HOLD` or candidate-only output |
| Correction lacks downstream invalidation plan | `BLOCKED` |
| Rollback target missing | release block |
| Replay differs for identical declared inputs | idempotency failure |

### Current CI limitation

The inspected `domain-habitat` workflow runs only TODO echo commands. A green result from that workflow is not proof of specification parsing, framework or hierarchy validation, source admission, sensitive-join enforcement, receipt emission, catalog closure, rollback, or publication safety.

[Back to top](#top)

---

## Review, activation, and change discipline

### Required review burden

Before an ecoregion specification can become `ACTIVE`, require review from:

- pipeline-spec steward;
- Habitat and ecoregions stewards;
- executable consumer owner;
- Spatial Foundation, CRS, geometry, and topology reviewer;
- source and rights steward;
- Fauna and Flora reviewer when occurrence-linked joins exist;
- Hydrology reviewer when WBD/HUC context exists;
- sensitivity, geoprivacy, cultural, archaeology, and reconstruction-risk reviewer where applicable;
- validation and evidence steward;
- policy and release steward;
- security reviewer for endpoints, logging, limits, and secrets;
- documentation steward.

### Separation of duties

The same unreviewed actor should not author a trust-significant spec, approve activation, operate the consumer, approve sensitivity exceptions, and approve release.

### Change classes

| Change | Minimum posture |
|---|---|
| Documentation clarification | Normal review; no activation effect |
| Non-semantic metadata correction | Review and digest/version discipline |
| Source or framework version change | Source, hierarchy, time, and downstream-impact review |
| Hierarchy or identity change | Contract/schema/identity review and migration plan |
| CRS, topology, or representation change | Spatial review, fixtures, negative tests, receipts |
| Context-join change | Owning-domain and sensitivity review |
| Rights or source-role change | Source/rights review; likely reactivation |
| Consumer or parser change | Compatibility tests and new activation record |
| Public attribute allowlist change | Sensitivity, policy, release, and reconstruction-risk review |
| Breaking semantic change | New immutable version, migration, correction, rollback, possible ADR |

[Back to top](#top)

---

## Definition of done for an active specification

An ecoregion profile is not done until:

1. the final path is verified against Directory Rules;
2. the profile has a stable identity, immutable version, canonical digest, and owner;
3. an accepted schema exists;
4. an accepted parser validates deterministically;
5. one executable consumer is verified;
6. discovery, precedence, and duplicate behavior are tested;
7. a separate activation record exists;
8. every source reference resolves to an admitted descriptor;
9. source roles and legacy-role mappings are accepted;
10. rights, attribution, redistribution, and derivative-use posture are current;
11. framework, version, level, native codes, labels, and hierarchy rules are explicit;
12. snapshot and boundary identity rules are accepted;
13. source, valid, retrieval, release, correction, and supersession times are explicit;
14. CRS, extent, scale, topology, and uncertainty profiles are accepted;
15. context joins preserve owning-domain truth;
16. sensitive and reconstructable joins fail closed;
17. public attribute allowlist and representation profile are reviewed;
18. contracts, schemas, fixtures, tests, and validators align;
19. deterministic no-network positive and negative tests pass;
20. evidence, policy, review, receipt, proof, catalog, and release gates are enforceable;
21. correction propagation and downstream invalidation are tested;
22. rollback and deactivation are tested;
23. CODEOWNERS or equivalent review enforcement is in place;
24. generated-work provenance and human review are complete.

[Back to top](#top)

---

## Rollback, correction, and deactivation

### Documentation rollback

Before merge, close the PR and abandon the scoped branch.

After merge, use a transparent revert commit or revert PR restoring the prior README and removing its generated receipt. Do not rewrite shared history.

### Active-spec rollback

A future active-spec rollback must:

1. suspend discovery and scheduling;
2. identify the exact spec, parser, consumer, source, framework, version, and activation digests;
3. stop new runs;
4. hold pending candidates;
5. preserve run, receipt, proof, catalog, and release lineage;
6. restore a reviewed prior profile or remain disabled;
7. re-evaluate source roles, rights, framework version, hierarchy, CRS, time, sensitivity, and public allowlist;
8. inventory processed records, catalog entries, tiles, exports, caches, indexes, graph edges, summaries, notifications, and generated answers;
9. issue correction, withdrawal, supersession, or rollback records;
10. invalidate unsafe or stale derivatives;
11. verify revoked artifacts are no longer publicly resolvable;
12. rerun deterministic validation and reconstruction-risk tests.

### Emergency deactivation triggers

- source rights or terms become invalid;
- framework or boundary source is withdrawn or corrected;
- hierarchy or identity corruption is discovered;
- public attributes or joins expose restricted detail;
- parser or consumer compatibility breaks;
- evidence, policy, review, release, correction, or rollback references no longer resolve;
- public derivatives cannot be reliably invalidated.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| ECO-SPEC-001 | Is `pipeline_specs/habitat/ecoregions/` the accepted final profile home? | NEEDS VERIFICATION |
| ECO-SPEC-002 | Which machine schema governs an active ecoregion spec? | UNKNOWN |
| ECO-SPEC-003 | Which parser, registry, and discovery mechanism are accepted? | UNKNOWN |
| ECO-SPEC-004 | Which executable consumer owns each profile family? | UNKNOWN |
| ECO-SPEC-005 | How is activation recorded, reviewed, and revoked? | UNKNOWN |
| ECO-SPEC-006 | Should the absent flat `pipeline_specs/habitat/ecoregions.yaml` reference be removed, redirected, or migrated? | NEEDS VERIFICATION |
| ECO-SPEC-007 | Which source-registry topology is canonical? | NEEDS VERIFICATION |
| ECO-SPEC-008 | What mapping resolves legacy source-role words into the accepted vocabulary? | NEEDS VERIFICATION |
| ECO-SPEC-009 | Which ecoregion sources are admitted and active? | UNKNOWN |
| ECO-SPEC-010 | What are the current rights and derivative-use terms for each source? | NEEDS VERIFICATION |
| ECO-SPEC-011 | Which framework, version, level, and identity vocabularies are accepted? | NEEDS VERIFICATION |
| ECO-SPEC-012 | What deterministic identity algorithm governs snapshots and boundaries? | UNKNOWN |
| ECO-SPEC-013 | Which crosswalk contracts are accepted, and how is loss represented? | UNKNOWN |
| ECO-SPEC-014 | Which time and freshness profiles are accepted? | NEEDS VERIFICATION |
| ECO-SPEC-015 | Which CRS, scale, topology, and uncertainty profiles are accepted? | NEEDS VERIFICATION |
| ECO-SPEC-016 | Which public attribute allowlists and geometry profiles are accepted? | UNKNOWN |
| ECO-SPEC-017 | Where is binding ecoregion sensitivity policy implemented? | UNKNOWN |
| ECO-SPEC-018 | Which ecoregion fixture payloads and executable tests exist? | UNKNOWN |
| ECO-SPEC-019 | Which validators are executable and wired to CI? | UNKNOWN |
| ECO-SPEC-020 | What receipt subtype layout is canonical for ecoregion runs? | NEEDS VERIFICATION |
| ECO-SPEC-021 | Are proof, catalog, release, correction, and rollback integrations implemented? | UNKNOWN |
| ECO-SPEC-022 | Are any schedules, runtimes, APIs, map layers, or public artifacts deployed? | UNKNOWN |
| ECO-SPEC-023 | Which named owners and reviewers are enforced by CODEOWNERS? | NEEDS VERIFICATION |
| ECO-SPEC-024 | How are downstream tiles, caches, indexes, graph edges, summaries, and answers invalidated after correction? | UNKNOWN |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `pipeline_specs/habitat/ecoregions/README.md` prior blob | CONFIRMED | Existing v0.1 boundary and proposed profile concepts | Did not prove files or activation |
| Bounded direct-lane search | CONFIRMED search result | README was the only direct-lane file surfaced | Not exhaustive recursive filesystem proof |
| Exact `pipeline_specs/habitat/ecoregions.yaml` check | CONFIRMED absent | Documentation drift | Does not choose replacement |
| `pipeline_specs/habitat/README.md` | CONFIRMED draft | Parent declarative doctrine | Parent active profiles unverified |
| `pipelines/domains/habitat/ecoregions/README.md` | CONFIRMED draft | Executable responsibility and anti-collapse | Runtime and consumer unverified |
| `configs/domains/habitat/README.md` | CONFIRMED v0.4 draft | README-only config boundary and vocabulary conflicts | No ecoregion config payload |
| `contracts/domains/habitat/ecoregions/README.md` | CONFIRMED experimental README | Candidate semantic families | Individual contracts unverified |
| `schemas/contracts/v1/domains/habitat/ecoregions/README.md` | CONFIRMED draft index | Proposed schema home | No concrete schema confirmed |
| `data/registry/sources/habitat/ecoregions/README.md` | CONFIRMED draft child | Admission guidance, source roles, topology conflict | No admitted descriptors proven |
| `policy/domains/habitat/README.md` | CONFIRMED scaffold | Policy root exists | Binding policy absent |
| Exact `policy/sensitivity/habitat/README.md` check | CONFIRMED absent | Sensitivity-path gap | Other policy files may exist elsewhere |
| `tools/validators/domains/habitat/README.md` | CONFIRMED index-only | Validator boundary and fail-closed posture | No ecoregion validator confirmed |
| `tests/domains/habitat/ecoregions/README.md` | CONFIRMED draft | Correct test home and intended invariants | Executable tests unverified |
| `fixtures/domains/habitat/ecoregions/README.md` | CONFIRMED draft | Correct fixture home and design rules | Payloads and consumers unverified |
| `data/receipts/habitat/README.md` | CONFIRMED draft parent | Receipt boundary and corrected parent path | No ecoregion child or emitted receipts |
| `data/proofs/habitat/README.md` | CONFIRMED draft | Proof responsibilities | Proof packs unverified |
| `data/catalog/domain/habitat/ecoregions/README.md` | CONFIRMED draft | Catalog-stage boundary | Inventory and closure unverified |
| `release/candidates/habitat/ecoregions/README.md` | CONFIRMED short draft | Candidate-review boundary | No candidate dossier proven |
| `data/published/layers/habitat/ecoregions/README.md` | CONFIRMED draft | PUBLISHED boundary and governed public path | Released inventory unverified |
| `.github/workflows/domain-habitat.yml` | CONFIRMED TODO-only | Workflow exists | No substantive validation |
| `.github/CODEOWNERS` | CONFIRMED placeholder | Broad root ownership | No named Habitat/ecoregion enforcement |
| `docs/doctrine/directory-rules.md` | CONFIRMED placement doctrine | Responsibility-root placement and lifecycle separation | Does not prove implementation |

[Back to top](#top)

---

## v0.1 preservation assessment

v0.2 preserves the useful v0.1 intent:

- declarative **what** remains separate from executable **how**;
- framework, hierarchy, source version, geometry, evidence, receipts, and release blockers remain central;
- ecoregions remain context rather than occurrence, patch-quality, regulatory, or cross-domain truth;
- lifecycle, correction, and rollback remain governed;
- future ingest, normalize, validate, catalog, publish, rollback, watcher, framework, hierarchy, and geometry-release profile families remain possible.

v0.2 changes the truth posture by:

- replacing the proposed flat tree with the observed README-only lane;
- correcting test, fixture, and receipt paths to current verified homes;
- surfacing the absent flat spec reference;
- separating legacy and current source-role vocabularies;
- distinguishing documentation, schemas, validators, tests, fixtures, receipts, proof, catalog, release, and public-layer maturity;
- requiring immutable identity, parser/consumer binding, separate activation, deterministic outcomes, sensitive-join controls, correction propagation, and rollback before any active use.

---

<p align="right"><a href="#top">Back to top</a></p>
