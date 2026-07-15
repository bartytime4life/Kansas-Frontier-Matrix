<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-geology-readme
title: pipeline_specs/geology/ — Governed Geology and Natural Resources Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; six-placeholder-specs-present; no-active-geology-spec-established; sensitivity-aware
owners: OWNER_TBD — Pipeline-spec steward · Geology steward · Stratigraphy/interpretation steward · Natural-resources steward · Source and rights steward · Subsurface/infrastructure sensitivity reviewer · Pipeline consumer owner · Spatial/CRS/datum reviewer · Temporal/vintage steward · Validation steward · Evidence steward · Policy steward · Release steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; geology; natural-resources; declarative-only; source-role-aware; observation-interpretation-model-aware; resource-anti-collapse; scale-aware; depth-aware; datum-aware; rights-aware; sensitivity-aware; reconstruction-resistant; no-secrets; no-live-activation; no-direct-source-access; no-direct-lifecycle-write; no-release-authority
current_path: pipeline_specs/geology/README.md
truth_posture: CONFIRMED current target, parent pipeline-spec contract, six direct seven-line PROPOSED inventory placeholders, draft executable Geology pipeline and child-lane documentation, README-only Geology config lane, draft source registry with subtype-first/domain-first topology conflict, maintained semantic-contract lane with naming drift, schema index with no confirmed concrete Geology schema files, greenfield domain-policy README plus three six-line default-deny Rego scaffolds, README-backed test lanes with unverified executable coverage, populated synthetic fixture README lanes with unverified payload/consumer alignment, draft Geology receipt/proof/release-candidate lanes, absent pipeline-specific Geology receipt path, TODO-only domain-geology workflow, and placeholder CODEOWNERS / PROPOSED minimum active-spec contract, finite status and outcome vocabularies, deterministic parser and consumer binding, scale/depth/datum and interpretation gates, source-role and resource anti-collapse, activation/deactivation discipline, validation matrix, correction propagation, and rollback requirements / UNKNOWN accepted Geology pipeline-spec schema, parser, registry, discovery, scheduler, activation records, executable consumers, runtime behavior, substantive CI enforcement, emitted receipts, proof closure, release integration, and public use / NEEDS VERIFICATION owners, exhaustive recursive inventory, canonical source-registry topology, receipt subtype layout, admitted SourceDescriptors, source roles and current rights, canonical object names, map/interpretation lineage, CRS/vertical-datum/depth vocabularies, scale and uncertainty profiles, concrete object schemas, field-level policy implementation, fixture payloads, executable tests, validator wiring, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 28de9ef2710d978a5c00f3057cc33868cbedd698
  prior_blob: 29e61bbddc806c9aa6a4d0f1b9987d5968b29540
  direct_lane_files:
    - pipeline_specs/geology/README.md
    - pipeline_specs/geology/bedrock_units.spec.yaml
    - pipeline_specs/geology/surficial_units.spec.yaml
    - pipeline_specs/geology/boreholes.spec.yaml
    - pipeline_specs/geology/well_logs.spec.yaml
    - pipeline_specs/geology/cross_sections.spec.yaml
    - pipeline_specs/geology/mineral_occurrences.spec.yaml
  direct_profile_posture: all six YAML files are seven-line PROPOSED documentation-inventory placeholders; none is active or consumer-bound
  workflow_posture: domain-geology is pull-request-triggered TODO scaffolding
related:
  - ../README.md
  - ./bedrock_units.spec.yaml
  - ./surficial_units.spec.yaml
  - ./boreholes.spec.yaml
  - ./well_logs.spec.yaml
  - ./cross_sections.spec.yaml
  - ./mineral_occurrences.spec.yaml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/geology/README.md
  - ../../docs/domains/geology/ARCHITECTURE.md
  - ../../docs/domains/geology/DATA_LIFECYCLE.md
  - ../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../docs/domains/geology/IDENTITY_MODEL.md
  - ../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../docs/domains/geology/SENSITIVITY.md
  - ../../docs/domains/geology/POLICY.md
  - ../../docs/domains/geology/PRESERVATION_MATRIX.md
  - ../../pipelines/domains/geology/README.md
  - ../../configs/domains/geology/README.md
  - ../../data/registry/sources/geology/README.md
  - ../../data/receipts/geology/README.md
  - ../../data/proofs/geology/README.md
  - ../../contracts/domains/geology/README.md
  - ../../schemas/contracts/v1/domains/geology/README.md
  - ../../policy/domains/geology/README.md
  - ../../policy/domains/geology/sensitivity/borehole_exact_geometry.rego
  - ../../policy/domains/geology/sensitivity/well_log_disclosure.rego
  - ../../policy/domains/geology/sensitivity/extraction_site_exposure.rego
  - ../../tests/domains/geology/README.md
  - ../../fixtures/domains/geology/README.md
  - ../../release/candidates/geology/README.md
  - ../../.github/workflows/domain-geology.yml
  - ../../.github/CODEOWNERS
notes:
  - "v0.2 replaces a planning-only proposed profile tree with commit-pinned repository evidence and classifies all six direct YAML files as placeholders rather than active specifications."
  - "No accepted parser, registry, scheduler, source activation, activation record, executable consumer binding, spec-specific executable test, or production runtime was found in bounded indexed searches."
  - "The source registry has subtype-first and domain-first paths; the receipt parent is data/receipts/geology/, while the old data/receipts/pipeline/geology/ reference is absent. This README surfaces rather than resolves those topology questions."
  - "Exact or reconstructable subsurface, private-well, core/sample, well-log, resource-target, extraction/storage infrastructure, operator/parcel, archaeological, and culturally sensitive details fail closed. No protected coordinates, operational exposure parameters, credentials, or private endpoints appear here."
  - "No placeholder profile, source record, connector, pipeline, config payload, schema, semantic contract, policy rule, fixture, test, validator, workflow, lifecycle object, receipt instance, proof, catalog object, release object, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Geology and Natural Resources Pipeline Specification Boundary

`pipeline_specs/geology/`

> Declarative run-intent boundary for Geology and Natural Resources pipelines. A reviewed active specification may state **what** a verified consumer should process, against which admitted sources, with which object-role, source-role, scale, depth, datum, time, evidence, sensitivity, policy, receipt, review, correction, and release gates. It does not execute a pipeline, admit source material, decide geologic interpretation, establish a mineral resource, expose restricted subsurface detail, create evidence, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-six__placeholders-lightgrey)
![anti-collapse](https://img.shields.io/badge/resource__claims-no__collapse-critical)
![sensitivity](https://img.shields.io/badge/subsurface__details-fail__closed-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Scope](#geology-specification-scope) · [Profiles](#profile-family-boundaries) · [Contract](#minimum-active-specification-contract) · [Sources](#sources-rights-and-admission) · [Meaning](#object-role-interpretation-and-resource-boundaries) · [Space](#spatial-support-scale-depth-datum-and-uncertainty) · [Time](#time-vintage-freshness-and-correction) · [Sensitivity](#sensitivity-public-safe-geometry-and-reconstruction-risk) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Evidence](#evidence-receipts-proof-and-release) · [Validation](#validation-and-enforceability) · [Review](#review-activation-and-change-discipline) · [Done](#definition-of-done-for-an-active-specification) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@28de9ef2710d978a5c00f3057cc33868cbedd698`  
> **Target blob before this revision:** `29e61bbddc806c9aa6a4d0f1b9987d5968b29540`  
> **Direct lane:** this README plus six seven-line `PROPOSED` inventory placeholders  
> **Active specifications:** none established  
> **Activation:** filename, merge state, syntax validity, schedule text, fixture success, policy default-deny, or a successful dry run activates nothing

> [!CAUTION]
> A valid Geology specification cannot turn a map unit into verified point geology, a borehole into regional continuity, an interpretation or cross-section into observation, a mineral occurrence into a deposit, a deposit into an estimate, a permit into production, production into a reserve, an administrative record into title, or a generalized geometry into public approval. Missing source role, scale, depth, datum, vintage, rights, evidence, policy, review, correction, rollback, or release state fails closed.

---

## Purpose

`pipeline_specs/geology/` is the Geology domain segment under the `pipeline_specs/` responsibility root.

Its safe future role is to hold small, reviewed, deterministic declarative profiles that bind:

- stable specification identity, immutable version and digest, owner, status, and supersession lineage;
- one accepted parser and one verified executable consumer;
- admitted `SourceDescriptor` references and source roles;
- source rights, license, attribution, redistribution, terms, and access constraints;
- object-family and claim-role boundaries;
- observed, measured, inferred, interpreted, modeled, aggregated, synthetic, administrative, and candidate knowledge character;
- source map edition, survey vintage, interpretation version, and correction lineage;
- horizontal CRS, vertical datum, depth datum/reference, units, sign convention, spatial support, scale, resolution, and uncertainty;
- input and output lifecycle states;
- validation, evidence, policy, review, receipt, proof, release, correction, and rollback requirements;
- deterministic no-network fixtures, finite outcomes, security controls, and resource limits.

This README is not a pipeline-spec schema, parser, registry, scheduler, activation decision, executable pipeline, source descriptor, geologic interpretation, resource estimate, permit or title decision, policy decision, receipt, evidence object, catalog record, release record, engineering conclusion, hazard warning, public API, map layer, 3D scene, or generated answer.

### Audience

- Geology, stratigraphy, subsurface, natural-resources, source, rights, sensitivity, policy, evidence, validation, and release stewards;
- pipeline-spec maintainers and executable pipeline owners;
- KGS, KCC, USGS, NGMDB, GeMS, MRDS, borehole, well-log, and related connector owners;
- Hydrology, Soil, Hazards, Archaeology, People/Land, Infrastructure, and map/3D reviewers;
- security reviewers checking restricted geometry, endpoints, credentials, logging, and reconstruction risk;
- maintainers planning tests, fixtures, activation, deactivation, correction, migration, or rollback.

[Back to top](#top)

---

## Authority and anti-collapse

### What this lane may declare

A reviewed active profile may declare:

- which accepted parser and executable consumer may read it;
- which admitted source identifiers and source roles are in scope;
- which object family, sublane, or processing stage is requested;
- which input and output lifecycle states are allowed;
- which scale, datum, depth, time, uncertainty, and geometry constraints apply;
- which validation, evidence, policy, review, receipt, proof, release, correction, and rollback gates apply;
- which finite outcome is required when any gate cannot close.

### What this lane cannot decide

A specification cannot decide:

- that a source is admitted, active, current, authoritative, rights-cleared, or redistributable;
- that an aggregator or catalog inherits the authority of an originating map, survey, log, sample, laboratory, operator, or agency;
- that two units, boundaries, boreholes, logs, samples, structures, occurrences, deposits, permits, sites, or records are identical;
- that a geologic map, cross-section, model, interpolation, inversion, or AI narrative is observation;
- that a map polygon or line supports point-level or subsurface truth;
- that a historical source describes present conditions;
- that exact or generalized geometry is safe;
- that a resource occurrence, deposit, estimate, production record, reserve statement, permit, extraction site, reclamation record, or ownership/title assertion can substitute for another;
- that evidence closes a claim;
- that a validation, policy, review, release, correction, or rollback decision exists;
- that public clients may bypass governed interfaces.

### Disallowed collapses

```text
spec file                         -> executable pipeline
spec parse success                -> active specification
profile merge                     -> source activation
source list                       -> source authority
catalog / aggregator access       -> origin evidence role
mapped unit polygon               -> geology at an arbitrary point
borehole / core / well log        -> regional continuity
cross-section / interpolation     -> observation
model / inversion                 -> measured geology
historical map                    -> current condition
mineral occurrence                -> deposit
deposit                           -> estimate or reserve
permit                            -> production
production                        -> reserve
extraction site                   -> mineral-rights or title truth
reclamation record                -> completed obligation
generalized geometry              -> public approval
successful run                    -> EvidenceBundle or release
generated summary                 -> geologic evidence
```

### Responsibility-root split

| Concern | Authority home | Specification relationship |
|---|---|---|
| Human doctrine and domain explanation | `docs/domains/geology/` | Reference only. |
| Semantic object meaning | `contracts/domains/geology/` | Reference accepted contract IDs; preserve naming/version drift. |
| Machine shape | `schemas/contracts/v1/domains/geology/` or ADR-resolved home | Validate against accepted schema IDs; none confirmed concrete in inspected index. |
| Source identity, role, rights, sensitivity, and admission | Accepted source-registry home | Reference admitted records; never recreate them. |
| Executable behavior | `pipelines/`, packages, and tools | Bind to one verified consumer. |
| Policy and sensitivity | `policy/` plus review artifacts | Require decisions; do not encode approval as a spec assertion. |
| Lifecycle records | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` | Declare allowed transitions only. |
| Receipts | `data/receipts/geology/` and accepted shared receipt homes | Declare required receipt classes; final subtype layout is unresolved. |
| Proof and evidence closure | `data/proofs/geology/` and accepted evidence homes | Require resolvable references. |
| Release | `release/` | Require release inputs; never approve publication. |
| Public clients | Governed APIs and released artifacts | No direct access to specs or internal stores. |

[Back to top](#top)

---

## Current status

### Repository maturity matrix

| Surface | Inspected status | What is established | What is not established |
|---|---|---|---|
| Parent Geology spec README | CONFIRMED draft v0.1 before this revision | Existing declarative boundary | Active profile behavior |
| Six direct YAML files | CONFIRMED seven-line `PROPOSED` placeholders | Inventory names and source-doc pointers | Schema, identity, sources, consumer, lifecycle, gates, activation |
| Pipeline-spec schema | UNKNOWN | None accepted in inspected evidence | Canonical shape, versioning, migration |
| Parser / registry / discovery | UNKNOWN | None verified | Loader, precedence, duplicate handling, activation lookup |
| Executable Geology pipeline | Draft documentation | Responsibility and fail-closed design | Concrete runtime behavior and direct consumer binding |
| Geology child pipelines | README-backed lanes for bedrock, surficial, boreholes, well logs, cross sections, mineral occurrences | Candidate placement and scope | Verified code, imports, runtime behavior, spec binding |
| Geology config lane | README-only in its bounded search | Safe config boundary | Loader, precedence, direct consumer, runtime binding |
| Source registry | Draft subtype-first lane plus domain-first sibling | Source-admission doctrine and topology conflict | Canonical active descriptors and production admission |
| Semantic contracts | Maintained draft lane with many object files | Human semantic boundaries | Complete accepted versions and machine enforcement |
| Schemas | Draft index and proposed sublane indexes | Intended schema responsibility | Concrete Geology `.schema.json` inventory |
| Domain policy | Greenfield README | Policy responsibility root | Complete field-level domain policy |
| Sensitivity policy | Three six-line default-deny Rego scaffolds | Fail-closed defaults for boreholes, well logs, extraction sites | Complete decision inputs, reason codes, tests, integration |
| Tests | README-backed coverage map | Intended no-network and fail-closed invariants | Executable modules, runner, CI coverage, pass rates |
| Fixtures | Populated README lanes | Synthetic/public-safe fixture design | Payload inventory and verified consumers |
| Receipts | Draft `data/receipts/geology/` parent | Receipt/process-memory boundary | Emitted instances, subtype layout, schemas, signing |
| Proofs | Draft `data/proofs/geology/` guide | Evidence/proof separation and anti-collapse posture | Actual proof inventory and runtime closure |
| Release candidate lane | Draft documentation | Pre-publication review boundary | ReleaseManifest integration and promoted artifacts |
| Domain workflow | Three `echo TODO` jobs | PR/push trigger exists | Substantive validation, proof build, or release dry run |
| CODEOWNERS | Placeholder | Generic root ownership entries | Geology spec and sensitivity reviewer enforcement |
| Runtime/public use | Not established | None | Production loading, execution, scheduling, or public behavior |

**Current conclusion:** the repository contains six Geology specification-shaped placeholders and substantial adjacent documentation, but no active Geology pipeline specification is established.

### Present files are not active

The six YAML files have only:

- `status: PROPOSED`;
- a `source_doc` pointer;
- their own `path`;
- one inventory-placeholder note.

They lack every activation-critical element listed in [Minimum active specification contract](#minimum-active-specification-contract).

[Back to top](#top)

---

## Current inspected inventory

```text
pipeline_specs/geology/
├── README.md
├── bedrock_units.spec.yaml
├── surficial_units.spec.yaml
├── boreholes.spec.yaml
├── well_logs.spec.yaml
├── cross_sections.spec.yaml
└── mineral_occurrences.spec.yaml
```

| File | Current status | Safe interpretation |
|---|---|---|
| `bedrock_units.spec.yaml` | `PROPOSED` inventory placeholder | Candidate slot for mapped bedrock-unit processing intent. |
| `surficial_units.spec.yaml` | `PROPOSED` inventory placeholder | Candidate slot for surficial-unit processing intent. |
| `boreholes.spec.yaml` | `PROPOSED` inventory placeholder | Candidate slot for borehole-reference processing intent; exact geometry fails closed. |
| `well_logs.spec.yaml` | `PROPOSED` inventory placeholder | Candidate slot for well-log processing intent; disclosure/rights gates required. |
| `cross_sections.spec.yaml` | `PROPOSED` inventory placeholder | Candidate slot for interpretive cross-section processing; observation/model boundary required. |
| `mineral_occurrences.spec.yaml` | `PROPOSED` inventory placeholder | Candidate slot for mineral-occurrence processing; occurrence/deposit/estimate/resource anti-collapse required. |

Bounded searches for the proposed schema identifier, `tests/pipeline_specs/geology`, and direct filename consumers surfaced placeholders and documentation references, not an accepted parser, scheduler, consumer, activation record, or executable spec-specific test.

### Placement and topology conflicts surfaced

| Question | Evidence | Status |
|---|---|---|
| Source registry | Both `data/registry/sources/geology/` and `data/registry/geology/sources/` are documented. | NEEDS VERIFICATION / migration or ADR |
| Receipt parent | `data/receipts/geology/` exists; prior `data/receipts/pipeline/geology/` reference is absent. | `data/receipts/geology/` CONFIRMED parent; subtype layout unresolved |
| Sensitivity policy | No `policy/sensitivity/geology/README.md` at snapshot; Rego scaffolds live under `policy/domains/geology/sensitivity/`. | NEEDS VERIFICATION / policy placement review |
| Schema sublanes | `schemas/contracts/v1/domains/geology/sublanes/` exists as index guidance; convention marked unresolved. | NEEDS VERIFICATION / ADR-sensitive |
| Object naming | Short, `Reference`, PascalCase, snake_case, and alias forms appear across docs/contracts/schema planning. | CONFLICTED / migration required before binding |
| Release manifests | Singular/plural manifest paths appear in adjacent documentation. | NEEDS VERIFICATION |

This README does not canonicalize, migrate, mirror, or deprecate any of those paths.

[Back to top](#top)

---

## Geology specification scope

A future active Geology specification may request bounded processing for:

- bedrock and surficial geologic units;
- lithology, geologic age, stratigraphic intervals, correlations, and nomenclature;
- faults, folds, structures, lineaments, and boundary versions;
- borehole, core, sample, and well-log references;
- geophysical and geochemical observations;
- hydrostratigraphic units and Geology-to-Hydrology handoffs;
- cross-sections, interpolations, models, and 3D-scene candidates with explicit interpretation boundaries;
- mineral occurrences, resource deposits, estimates, extraction sites, and reclamation records without role collapse;
- catalog/triplet candidates and public-safe map derivatives;
- validation-only, proof-only, dry-run, correction, deactivation, and rollback-readiness profiles.

### Out of scope

A specification must not:

- fetch source payloads or hold credentials;
- activate a source;
- admit bytes into RAW;
- define object meaning or schema shape;
- decide a source role, rights posture, permit state, mineral right, title, engineering safety, or regulatory compliance;
- perform or approve a public-safe geometry transform;
- write directly to catalog, triplet, published, or release lanes;
- assert an occurrence, deposit, estimate, reserve, production state, or ownership fact;
- expose restricted coordinates or operational infrastructure detail;
- serve public clients.

[Back to top](#top)

---

## Profile family boundaries

| Profile family | Requested intent | Mandatory non-collapse |
|---|---|---|
| Bedrock units | Process mapped bedrock units and boundaries. | Map interpretation is not point observation; scale and edition stay visible. |
| Surficial units | Process surficial units, parent material, and boundaries. | Surficial mapping does not replace Soil or site-specific observation. |
| Boreholes | Process admitted borehole references and bounded attributes. | A borehole is local evidence, not regional continuity; exact geometry may be restricted. |
| Well logs | Process admitted log references and permitted derived attributes. | Log access is not redistribution permission; interpretation is not observed lithology. |
| Cross sections | Build bounded interpretive candidates. | Interpolation, correlation, and reconstruction remain interpretation/model outputs. |
| Mineral occurrences | Process occurrence candidates. | Occurrence is not deposit, estimate, reserve, permit, production, title, or extraction right. |
| Stratigraphy | Reconcile accepted nomenclature and correlations. | Correlation and age assignment preserve source authority and uncertainty. |
| Structures | Process faults, folds, and related interpretations. | Mapped structure is scale/version-bound; it is not a site-specific hazard forecast. |
| Geophysics/geochemistry | Process measurements and derived candidates. | Observation, processing, inversion, anomaly, model, and interpretation remain distinct. |
| Hydrostratigraphy | Prepare Geology-owned candidates for governed bridge use. | Does not replace Hydrology groundwater, aquifer, water-quality, or water-right authority. |
| Public derivative | Prepare generalized/released candidates only. | Transform requirement is not transform completion or approval. |
| Correction/rollback | Re-evaluate or withdraw prior derived candidates. | Must preserve prior identity, evidence, release, and invalidation lineage. |

[Back to top](#top)

---

## Minimum active specification contract

A profile is **not active** until every applicable field below is machine-valid, reviewed, bound to implementation, and linked to a separate activation record.

### Identity and immutable lineage

- accepted `schema_id` and `schema_version`;
- stable `spec_id`;
- immutable semantic version and canonical digest;
- owner and required reviewers;
- finite lifecycle status;
- creation, supersession, deprecation, and rollback lineage;
- changelog and migration notes.

### Parser, discovery, consumer, and activation

- accepted parser identifier and version;
- one verified executable consumer path and version;
- deterministic discovery and precedence;
- duplicate-ID and digest-collision behavior;
- explicit compatibility range;
- separate activation record with actor, review refs, commit, digest, scope, environment, effective time, expiry, and rollback target;
- deny activation when the parser, consumer, source, schema, policy, or reviewer path cannot resolve.

### Source admission and rights

- admitted `SourceDescriptor` identifiers only;
- source family, origin publisher, distributor/aggregator, and canonical source role;
- rights, license, attribution, redistribution, access, embargo, and term-expiry state;
- source map edition, survey/program, package version, retrieval method, and source vintage;
- prohibited claim families and authority limits;
- correction, withdrawal, and supersession refs;
- no credentials or private endpoints in the profile.

### Object family and claim role

- accepted semantic contract ID and version;
- accepted machine schema ID and version;
- canonical object-family name and migration aliases;
- explicit claim role: `OBSERVATION`, `MEASUREMENT`, `INTERPRETATION`, `MODEL`, `AGGREGATE`, `ADMINISTRATIVE`, `CANDIDATE`, or another accepted finite value;
- explicit resource role where applicable: occurrence, deposit, estimate, permit, production, reserve, extraction, reclamation;
- deterministic identity and deduplication policy;
- adjacency boundaries with Soil, Hydrology, Hazards, Archaeology, People/Land, Infrastructure, and map/3D carriers.

### Spatial, depth, scale, and uncertainty

- horizontal CRS identifier;
- vertical CRS/datum and elevation reference where applicable;
- depth reference, sign convention, units, and datum;
- geometry type and spatial support;
- source scale, intended use scale, resolution, and minimum zoom/use limits;
- positional, vertical, depth, attribute, correlation, model, and interpretation uncertainty;
- topology and boundary-version requirements;
- public/internal geometry classification;
- no silent reprojection, datum substitution, unit conversion, or precision inflation.

### Time and version semantics

- source creation/publication time;
- observation or measurement time;
- map/survey/log/sample vintage;
- retrieval and processing time;
- interpretation/model version time;
- valid time where applicable;
- review, release, correction, supersession, and withdrawal time;
- stale-state, outage, retry, and correction behavior;
- no use of file modification time as scientific validity time unless explicitly defined.

### Lifecycle and side effects

- allowed input state and accepted input object classes;
- allowed output state and candidate object classes;
- explicit QUARANTINE and HOLD routes;
- bounded side-effect allowlist;
- no direct `PUBLISHED` or release write;
- deterministic idempotency key and prior-run behavior;
- resource limits, timeout, cancellation, and partial-failure semantics;
- atomicity and cleanup behavior;
- correction and rollback target.

### Sensitivity and public-safe geometry

- applicable sensitivity class and policy refs;
- exact borehole, well-log, core/sample, private-well, resource-target, extraction/storage infrastructure, operator/parcel, archaeological, and culturally sensitive handling;
- join-induced and reconstruction-risk assessment;
- transform family reference without embedding operational exposure parameters;
- required `PolicyDecision`, `ReviewRecord`, and transform receipt refs;
- suppression of restricted values from logs, diffs, receipts, issue text, notifications, caches, summaries, and public errors;
- explicit deny/hold behavior when classification or policy is unresolved.

### Evidence, validation, receipts, review, and release

- resolvable `EvidenceRef` requirements and expected `EvidenceBundle` closure;
- accepted validators and versions;
- finite validation outcomes and reason codes;
- required run, transform, validation, aggregation, model, redaction, review, and correction receipt classes;
- reviewer roles and separation of duties;
- release-candidate requirements, but no release-ready boolean as authority;
- correction, withdrawal, supersession, invalidation, and rollback requirements;
- public clients limited to governed APIs and released artifacts.

### Security and observability

- secret references only, never secret values;
- endpoint allowlist and network posture;
- no dynamic code execution or unreviewed plugin loading;
- bounded logs, metrics, traces, and error text;
- actor/runner identity and spec/consumer/source digests;
- no restricted coordinates, private identities, proprietary log content, or reconstructive diffs in observability outputs;
- deterministic audit and receipt linkage.

[Back to top](#top)

---

## Illustrative inactive YAML

> [!WARNING]
> The following is intentionally incomplete, non-canonical, and inactive. It demonstrates separation of concerns only. It must not be copied into production or treated as an accepted schema.

```yaml
schema_id: PROPOSED-kfm.pipeline_spec.geology
schema_version: PROPOSED-v1
spec_id: geology.example.inactive
version: 0.0.0-example
status: PROPOSED
active: false

implementation:
  parser_ref: NEEDS_VERIFICATION
  consumer_ref: NEEDS_VERIFICATION
  execution_mode: no_network_fixture_only

sources:
  source_descriptor_refs: []
  require_admitted: true
  preserve_origin_role: true

object:
  contract_ref: NEEDS_VERIFICATION
  schema_ref: NEEDS_VERIFICATION
  claim_role: CANDIDATE

spatial:
  horizontal_crs: NEEDS_VERIFICATION
  vertical_datum: NEEDS_VERIFICATION
  depth_reference: NEEDS_VERIFICATION
  source_scale: NEEDS_VERIFICATION
  public_geometry: DENY_UNTIL_REVIEWED

lifecycle:
  input_state: WORK
  output_state: QUARANTINE
  direct_publish: false

requirements:
  evidence_bundle_required: true
  policy_decision_required: true
  review_required: true
  receipts_required: []
  rollback_target_required: true

activation:
  separate_record_required: true
```

Syntax validity would not make this example active, safe, complete, or authoritative.

[Back to top](#top)

---

## Sources, rights, and admission

### Source-role preservation

Geology specifications must preserve:

- originating agency, survey, operator, laboratory, or steward;
- distributor or aggregator separately from origin;
- source role separately from access route;
- map edition, program, series, source scale, and survey vintage;
- rights, attribution, redistribution, and source-term limits;
- model/interpretation status separately from observation;
- correction and withdrawal lineage.

Examples of sources such as KGS, KCC, USGS, NGMDB, GeMS, MRDS, borehole/log systems, or third-party catalogs do not receive blanket authority by name. Each admitted descriptor must define the claim families it may support and the constraints that travel with it.

### Admission sequence

```text
source documentation
    -> SourceDescriptor review
    -> rights / role / sensitivity / cadence checks
    -> separate activation decision
    -> governed connector capture
    -> RAW
```

A profile may reference that sequence. It cannot perform or approve it.

### Fail-closed source conditions

Return a finite hold, deny, abstain, or error when:

- descriptor resolution fails;
- source role is missing or incompatible;
- current terms or redistribution rights are unresolved;
- source version, map edition, datum, scale, or vintage is missing where material;
- source correction or withdrawal state is unresolved;
- origin identity is lost behind an aggregator;
- sensitive-detail handling is unspecified;
- the requested claim exceeds source authority.

[Back to top](#top)

---

## Object-role, interpretation, and resource boundaries

### Knowledge character must travel with every candidate

| Character | Meaning | Forbidden upgrade |
|---|---|---|
| Observation | Directly observed source record with bounded support | Cannot become regional certainty. |
| Measurement | Instrumental or laboratory value with method and uncertainty | Cannot become interpreted unit/resource truth automatically. |
| Interpretation | Human or governed interpretive classification/correlation | Cannot be relabeled as observation. |
| Model | Computed, interpolated, inverted, simulated, or predicted result | Cannot be shown as measured geology. |
| Aggregate | Generalized summary over bounded inputs | Cannot imply hidden exact records. |
| Administrative | Permit, operator, regulatory, reclamation, or program record | Cannot prove geology, production, reserve, title, or ownership. |
| Candidate | Unreviewed or incomplete proposed object | Cannot enter public release. |
| Synthetic | Test/example material | Cannot support real claims. |

### Resource claim anti-collapse

```text
MineralOccurrence
    != ResourceDeposit
    != ResourceEstimate
    != ReserveStatement
    != Permit
    != ProductionRecord
    != ExtractionSite
    != ReclamationRecord
    != MineralRight / title / ownership
```

A specification that requests more than one role must state separate contracts, schemas, evidence requirements, reviewers, and output classes. A single `resource` label is insufficient.

### Map, section, and 3D reality boundaries

- mapped contacts and unit polygons are scale-, edition-, and interpretation-bound;
- cross-sections are interpretations constrained by evidence, not exposed subsurface observations;
- interpolated surfaces and 3D scenes remain models or carriers;
- renderer success does not validate geology;
- vertical exaggeration, clipping, smoothing, draping, and generalization must be visible;
- public maps and scenes cite released evidence and preserve caveats;
- generated narrative never fills missing strata, contacts, depths, or resource classifications.

[Back to top](#top)

---

## Spatial support, scale, depth, datum, and uncertainty

An active specification must reject ambiguous spatial meaning rather than infer silently.

### Required spatial semantics

- declared horizontal CRS;
- declared vertical datum where elevation is used;
- declared depth datum/reference, sign, and units;
- source geometry type and support;
- source and intended-use scale;
- coordinate, elevation, and depth uncertainty;
- boundary/generalization lineage;
- topology expectations and known exceptions;
- map/section/model extent and clipping behavior;
- conversion and reprojection receipt requirements.

### Scale law

A product must not be used at a finer decision scale than its source, processing, uncertainty, and release profile support.

Examples:

- statewide map polygons do not prove parcel- or site-scale lithology;
- a generalized public layer does not support reconstruction of exact restricted locations;
- an interpreted cross-section does not prove continuous contacts outside its bounded evidence;
- a point borehole cannot silently populate a regional volume;
- a raster or interpolated surface must retain cell size, method, support, and uncertainty.

### Depth and vertical references

Profiles touching subsurface records must declare:

- measured depth versus true vertical depth;
- ground-surface, sea-level, Kelly bushing, casing, or other reference;
- elevation/depth sign convention;
- units and conversion lineage;
- vertical CRS/datum;
- interval top/base ordering;
- missing, estimated, corrected, and superseded depth state.

Ambiguity routes to `QUARANTINE`, `HOLD`, or `ABSTAIN`.

[Back to top](#top)

---

## Time, vintage, freshness, and correction

Geology time is multi-dimensional.

| Time kind | Example |
|---|---|
| Source publication time | Map, database, bulletin, package, or release publication. |
| Observation time | Field observation, drilling, logging, sampling, survey, or measurement. |
| Retrieval time | Connector capture time. |
| Processing time | Pipeline run time. |
| Interpretation version time | Correlation, map interpretation, model, or cross-section version. |
| Valid/effective time | Permit, status, administrative, or regulatory validity where applicable. |
| Release time | Governed public release. |
| Correction/supersession time | When a source, interpretation, or release changed. |

An active specification must:

- distinguish source vintage from freshness;
- preserve superseded maps, correlations, logs, and interpretations;
- define stale-state budgets by source family and use;
- avoid treating no upstream change as proof of current geologic truth;
- propagate corrections to affected candidates, evidence, catalogs, maps, scenes, caches, indexes, and summaries;
- preserve prior versions and rollback targets.

[Back to top](#top)

---

## Sensitivity, public-safe geometry, and reconstruction risk

### Default posture

Exact or reconstructable detail fails closed when it involves:

- boreholes, cores, samples, private wells, or proprietary well logs;
- sensitive resource targets, exploration detail, extraction/storage infrastructure, or operator/parcel joins;
- archaeological, paleontological, cave, cultural, burial, or sovereign-sensitive locations;
- critical infrastructure or security-adjacent subsurface information;
- private identities, landowner contacts, access details, or contractual restrictions;
- small counts, unique identifiers, attribute combinations, or cross-layer joins that re-identify restricted locations.

The three inspected Rego modules currently establish default denial only. They do not establish complete policy inputs, exceptions, review roles, reason codes, transform parameters, testing, or runtime integration.

### No-leak requirements

Restricted values or reconstructive clues must not appear in:

- specification examples;
- Git diffs and issue text;
- logs, metrics, traces, stack traces, or test snapshots;
- run receipts or public receipt indexes;
- notifications or watcher summaries;
- generated narrative;
- vector/search indexes or embeddings;
- map tiles, scene metadata, feature-state, source URLs, cache keys, or download manifests;
- filenames or stable IDs that encode coordinates.

### Public-safe transformation

A specification may require an accepted transform family, but it cannot define public approval. Public-safe use requires:

- policy decision;
- sensitivity and rights review;
- deterministic transform with receipt;
- reconstruction-risk tests;
- released public derivative identity;
- correction and rollback lineage;
- invalidation of stale or unsafe derived surfaces.

[Back to top](#top)

---

## Lifecycle gates and finite outcomes

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

A specification may declare a requested transition only when:

- the source is separately admitted;
- input state and object class are verified;
- the executable consumer is bound and reviewed;
- contracts, schemas, validators, and fixtures resolve;
- source role, rights, scale, datum, depth, time, sensitivity, and evidence requirements close;
- required receipts and review paths exist;
- release, correction, and rollback requirements are explicit.

### Proposed finite specification statuses

```text
DRAFT
REVIEW_REQUIRED
APPROVED_INACTIVE
ACTIVE
SUSPENDED
DEPRECATED
SUPERSEDED
REVOKED
```

Path presence or merge state is not an activation status.

### Proposed finite run outcomes

```text
NO_OP
CANDIDATE_CREATED
QUARANTINED
HELD_FOR_REVIEW
ABSTAINED
DENIED
REJECTED
FAILED_RETRYABLE
FAILED_TERMINAL
CANCELLED
ROLLED_BACK
```

Every non-success outcome requires a bounded reason code and safe diagnostic message.

### Example blocker reason families

- `SPEC_SCHEMA_UNRESOLVED`
- `PARSER_UNRESOLVED`
- `CONSUMER_UNRESOLVED`
- `SOURCE_NOT_ADMITTED`
- `SOURCE_ROLE_MISSING`
- `RIGHTS_UNKNOWN`
- `SOURCE_VINTAGE_UNKNOWN`
- `OBJECT_ROLE_AMBIGUOUS`
- `RESOURCE_ROLE_COLLAPSE`
- `CRS_UNKNOWN`
- `VERTICAL_DATUM_UNKNOWN`
- `DEPTH_REFERENCE_UNKNOWN`
- `SCALE_UNSUPPORTED`
- `SENSITIVITY_UNRESOLVED`
- `EVIDENCE_MISSING`
- `POLICY_DENY`
- `REVIEW_MISSING`
- `RECEIPT_MISSING`
- `RELEASE_BLOCKED`
- `ROLLBACK_TARGET_MISSING`

[Back to top](#top)

---

## Evidence, receipts, proof, and release

### Evidence order

```text
define scope
    -> resolve source and object identity
    -> retrieve governed evidence
    -> resolve EvidenceRef -> EvidenceBundle
    -> apply source-role, rights, scale, datum, time, sensitivity, and policy checks
    -> validate
    -> review
    -> prepare candidate
    -> governed release decision
```

A specification controls none of those authorities by itself.

### Artifact-family separation

| Artifact | Records | Does not prove |
|---|---|---|
| Run/transform/validation receipt | What a governed process did | Geologic truth or release |
| PolicyDecision | Policy disposition for bounded inputs | Evidence or execution |
| ReviewRecord | Human/steward review state | Source truth or publication by itself |
| EvidenceBundle | Claim support and provenance | Policy clearance or release |
| Catalog record | Discovery/description/projection closure | Scientific truth beyond evidence |
| ReleaseManifest / promotion decision | Approved released artifact and lineage | Unbounded claims or future validity |
| CorrectionNotice / RollbackCard | Correction and reversal action | That every derivative was invalidated without verification |

The verified domain receipt parent is `data/receipts/geology/`. Final subtype placement remains **NEEDS VERIFICATION**. The absent old `data/receipts/pipeline/geology/` path must not be invented by this README.

### Release readiness

A profile may require a release candidate dossier, but it must never contain or interpret a `release_ready: true` flag as authority. Release requires separate policy, review, evidence, validation, manifest, correction, and rollback objects.

[Back to top](#top)

---

## Validation and enforceability

### Required positive tests

An active specification needs deterministic, no-network tests proving:

- schema, parser, consumer, spec ID, version, and digest resolution;
- source descriptors resolve and are active for the requested role;
- rights, attribution, redistribution, and terms gates close;
- contract and schema refs match the requested object family;
- source role and knowledge character are preserved;
- occurrence/deposit/estimate/permit/production/reserve roles do not collapse;
- CRS, vertical datum, depth reference, units, scale, and uncertainty are validated;
- input/output lifecycle transitions are allowlisted;
- required evidence, policy, review, receipt, and release refs resolve;
- idempotent reruns do not duplicate outputs;
- corrections and supersessions propagate;
- deactivation and rollback restore a known safe state.

### Required negative tests

Tests must reject or safely route:

- malformed, unknown, or unsupported schema versions;
- duplicate spec IDs with different digests;
- missing parser, consumer, owner, reviewer, or activation record;
- inactive, stale, withdrawn, or rights-unclear sources;
- aggregator-only origin identity;
- ambiguous object or resource role;
- missing map edition, survey/log vintage, scale, CRS, vertical datum, depth reference, units, or uncertainty;
- map-unit-to-point, borehole-to-region, model-to-observation, or occurrence-to-resource upgrades;
- exact restricted geometry in logs, receipts, notifications, public candidates, tiles, scenes, or summaries;
- missing evidence, policy, review, receipt, correction, or rollback refs;
- direct catalog, published, release, API, UI, map, tile, or scene writes;
- network calls during no-network tests;
- partial failure that leaves discoverable unsafe artifacts.

### Current enforceability boundary

README and fixture presence does not prove executable validation. The inspected `domain-geology` workflow executes only TODO echo steps. A green workflow result is scaffold health, not Geology spec enforcement.

[Back to top](#top)

---

## Review, activation, and change discipline

### Required review before activation

At minimum:

- pipeline-spec steward;
- Geology domain steward;
- stratigraphy/interpretation reviewer for meaning-bearing profiles;
- natural-resources/regulatory reviewer for resource or extraction profiles;
- source and rights steward;
- subsurface/infrastructure/cultural sensitivity reviewer where applicable;
- executable consumer owner;
- CRS/vertical datum/depth/scale reviewer;
- validation and evidence steward;
- policy and release steward for public-facing paths.

### Activation is a governed record

Activation must be separate from the YAML file and include:

- spec ID, version, digest, and commit;
- parser and consumer versions;
- source descriptor and activation refs;
- environment and allowed scope;
- actor, reviewers, and review refs;
- effective time, expiry, and suspension state;
- baseline, prior spec, and rollback target;
- finite activation outcome and reason.

### Change categories

| Change | Minimum posture |
|---|---|
| Documentation-only clarification | Routine reviewed PR; no activation change. |
| Non-semantic metadata | Validate and review; preserve digest rules. |
| Source, role, rights, cadence, scale, datum, depth, or sensitivity change | New semantic version and activation review. |
| Contract/schema/consumer/parser change | Compatibility analysis, fixtures, migration, rollback. |
| Public representation or release-gate change | Policy, sensitivity, release, correction, and rollback review. |
| Deprecation or migration | Preserve old version, deactivation record, references, and rollback target. |

[Back to top](#top)

---

## Definition of done for an active specification

A future Geology specification is not done until:

- [ ] canonical placement is accepted;
- [ ] owner and reviewer roles are assigned;
- [ ] schema, parser, registry, discovery, and precedence are accepted;
- [ ] spec ID, semantic version, digest, and supersession lineage are stable;
- [ ] one executable consumer is implemented and tested;
- [ ] source descriptors and activation decisions resolve;
- [ ] source roles, rights, terms, vintage, authority limits, and correction state are explicit;
- [ ] object/claim/resource roles and semantic contracts are explicit;
- [ ] machine schemas exist and validate;
- [ ] CRS, vertical datum, depth reference, units, scale, support, and uncertainty are explicit;
- [ ] sensitivity and public-safe geometry policy refs resolve;
- [ ] no-leak and reconstruction-risk tests pass;
- [ ] lifecycle transitions and side effects are allowlisted;
- [ ] deterministic positive, negative, idempotency, correction, and rollback tests pass;
- [ ] required receipts, evidence, proof, review, and release refs are enforced;
- [ ] substantive CI runs the accepted validators;
- [ ] CODEOWNERS or equivalent review enforcement is present;
- [ ] a separate activation record exists;
- [ ] correction, deactivation, invalidation, and rollback drills are proven;
- [ ] documentation and evidence ledger are current.

The six existing placeholders satisfy none of these requirements beyond path, status, source-doc pointer, and inventory intent.

[Back to top](#top)

---

## Rollback, correction, and deactivation

### README-only rollback

Before merge, close the draft PR and abandon the scoped branch.

After merge, use a transparent revert commit or revert PR restoring v0.1 and removing the generated receipt. Do not rewrite shared history.

### Future active-spec deactivation

1. Suspend discovery and scheduling using a reviewed activation/deactivation record.
2. Preserve spec, version, digest, parser, consumer, source, baseline, and run lineage.
3. Stop new work and hold pending candidates.
4. Restore a reviewed prior profile and baseline or remain disabled.
5. Re-evaluate source roles, rights, map/log vintage, object/resource roles, scale, datum, depth, sensitivity, and evidence.
6. Inventory every derived surface: processed records, catalogs, triplets, proofs, receipts, releases, APIs, tiles, scenes, exports, caches, indexes, embeddings, and generated summaries.
7. Issue correction, withdrawal, supersession, or rollback records as required.
8. Invalidate unsafe or stale derivatives.
9. Re-run deterministic validation and reconstruction-risk checks.
10. Verify public clients can no longer resolve revoked artifacts.

Rollback success must be evidenced, not inferred from file restoration.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-GEOL-001` | Which pipeline-spec schema and version are accepted? | UNKNOWN |
| `PIPE-SPEC-GEOL-002` | Which parser, registry, discovery, precedence, and scheduler are accepted? | UNKNOWN |
| `PIPE-SPEC-GEOL-003` | Which activation/deactivation record contract is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-004` | Should the six placeholders be completed, consolidated, renamed, migrated, or retired? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-005` | Which executable consumer owns each profile? | UNKNOWN |
| `PIPE-SPEC-GEOL-006` | Which source-registry path is canonical and which records are admitted? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-GEOL-007` | Which source-role and rights vocabularies are accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-008` | Which object-family names and aliases are canonical? | CONFLICTED / migration required |
| `PIPE-SPEC-GEOL-009` | Which Geology machine schemas are implemented and accepted? | UNKNOWN |
| `PIPE-SPEC-GEOL-010` | Is the `schemas/.../sublanes/` convention accepted? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-GEOL-011` | Which CRS, vertical datum, depth-reference, unit, scale, and uncertainty profiles are canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-012` | Which time/vintage/freshness semantics apply by source family? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-013` | Which field-level sensitivity policy and reason-code vocabulary are accepted? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-014` | Where should Geology sensitivity policy documentation and executable policy canonically live? | NEEDS VERIFICATION / placement review |
| `PIPE-SPEC-GEOL-015` | Which receipt subtype layout is canonical under `data/receipts/geology/`? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-016` | Which fixture payloads and executable tests consume each spec family? | UNKNOWN |
| `PIPE-SPEC-GEOL-017` | Which validators and substantive CI jobs enforce the active contract? | UNKNOWN |
| `PIPE-SPEC-GEOL-018` | Which reviewers and separation-of-duties controls are enforced? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-019` | How do corrections propagate across catalogs, maps, scenes, caches, indexes, and summaries? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-020` | Has any Geology spec been deployed, scheduled, or used by a public path? | UNKNOWN |
| `PIPE-SPEC-GEOL-021` | Which release-manifest path and object family are canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-022` | Which rollback drills demonstrate full derivative invalidation? | UNKNOWN |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observed result |
|---|---|
| `pipeline_specs/geology/README.md` | Draft v0.1 planning-oriented parent before this revision. |
| Six direct `.spec.yaml` files | Each is a seven-line `PROPOSED` documentation-inventory placeholder. |
| Indexed spec/consumer/test searches | No accepted schema ID, parser, scheduler, activation record, direct consumer, or spec-specific executable test surfaced. |
| `pipelines/domains/geology/README.md` | Detailed draft executable boundary; runtime and direct consumer binding unverified. |
| `configs/domains/geology/README.md` | v0.3 README-only config lane; source/receipt/schema/release conflicts documented. |
| `data/registry/sources/geology/README.md` | Draft source registry; subtype-first/domain-first topology conflict and no public path. |
| `contracts/domains/geology/README.md` | Maintained semantic-contract boundary with naming/version drift and no runtime claim. |
| `schemas/contracts/v1/domains/geology/README.md` | Draft index; no concrete Geology schema file confirmed in its inspection. |
| `docs/domains/geology/SENSITIVITY.md` | Draft classification rubric; no dedicated ratified Geology row; restrictive default applies. |
| `policy/domains/geology/README.md` | Greenfield policy README. |
| Three Geology sensitivity Rego files | Six-line `PROPOSED` scaffolds with `default allow := false`. |
| `tests/domains/geology/README.md` | README-backed coverage map; executable modules, runner, CI, and pass rates unverified. |
| `fixtures/domains/geology/README.md` | Populated synthetic child README lanes; payload and consumer alignment unverified. |
| `data/receipts/geology/README.md` | Draft receipt parent; no child receipt lanes confirmed and subtype layout unresolved. |
| `data/receipts/pipeline/geology/README.md` | Not present at evidence snapshot. |
| `data/proofs/geology/README.md` | Draft proof guide; actual proof schemas/inventory/runtime closure unverified. |
| `release/candidates/geology/README.md` | Draft pre-publication review lane, not release authority. |
| `.github/workflows/domain-geology.yml` | Three TODO echo jobs only. |
| `.github/CODEOWNERS` | Placeholder; no Geology spec ownership rule. |
| `docs/doctrine/directory-rules.md` | Confirms responsibility-root placement and governed lifecycle invariant. |

[Back to top](#top)

---

## v0.1 preservation assessment

v0.2 preserves the useful v0.1 intent while replacing unsupported planning claims:

- preserves `pipeline_specs/` versus `pipelines/` separation;
- preserves the Geology and Natural Resources scope;
- preserves anti-collapse among occurrence, deposit, estimate, permit, production, reserve, title, and extraction;
- preserves lifecycle, evidence, sensitivity, receipt, release, correction, and rollback gates;
- preserves fail-closed subsurface and private-well posture;
- replaces the speculative flat tree with the six files actually observed;
- corrects the absent pipeline-specific receipt path;
- adds source-role, object-role, scale, depth, datum, uncertainty, activation, no-leak, validation, and rollback discipline;
- keeps all unverified implementation claims visibly bounded.

---

## Maintainer note

Keep this directory declarative. Do not add executable code, connectors, credentials, source payloads, schemas, semantic contracts, policy decisions, lifecycle outputs, receipt instances, EvidenceBundles, catalog records, release decisions, public API/UI/map/scene code, restricted geometry, engineering guidance, mineral-rights conclusions, hazard warnings, or generated authoritative geology here.

A future profile should remain small, immutable, consumer-bound, machine-valid, reviewed, separately activated, deterministic, testable, correctable, and reversible.

[Back to top](#top)
