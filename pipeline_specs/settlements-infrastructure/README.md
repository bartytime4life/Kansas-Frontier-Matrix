<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-settlements-infrastructure-readme
title: pipeline_specs/settlements-infrastructure/ — Settlements / Infrastructure Pipeline Specification Lane
type: readme
version: v0.2
status: draft; repository-grounded; canonical-working-domain-lane; five-inert-stage-scaffolds; no-active-stage-implementation-established
owners: OWNER_TBD — Pipeline-spec steward · Settlements/Infrastructure domain steward · Settlements sublane steward · Infrastructure sublane steward · Source steward · Rights reviewer · Sensitivity reviewer · Evidence steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-13
updated: 2026-07-17
supersedes: v0.1
policy_label: public-doctrine; settlements-infrastructure; declarative-only; legal-status-sensitive; operational-status-sensitive; critical-infrastructure-sensitive; private-property-sensitive; living-person-sensitive; cultural-location-sensitive; source-role-aware; temporal; evidence-first; no-secrets; no-live-activation; no-public-path; no-publication; release-gated
current_path: pipeline_specs/settlements-infrastructure/README.md
truth_posture: CONFIRMED current target file, pipeline_specs root contract, five canonical companion YAML files with empty stages arrays, current settlement compatibility-alias README, governing executable lane README, contract-lane README, source-registry README, schema and policy scaffolds, Directory Rules placement conflict, domain canonical-path register, CODEOWNERS route, and TODO-only domain workflow / PROPOSED canonical machine contract, parser and registry behavior, deterministic identity, state and activation model, stage semantics, source-role and rights gates, legal-status and operational-status boundaries, temporal semantics, critical-infrastructure controls, public-safe representation, finite outcomes, receipts, validation matrix, correction, deactivation, and rollback behavior / UNKNOWN accepted pipeline-spec schema, parser, registry, loader, scheduler, executable stage consumers, active source bindings, active schedules, substantive stage definitions, stage-specific fixtures and tests, validator wiring, automatic receipt emission, branch-protection enforcement, release integration, and production use / NEEDS VERIFICATION owners, exhaustive recursive inventory, final settlement versus settlements-infrastructure migration decision, exact source-role enum, source-registry topology, schema and policy maturity, legal-status authority, infrastructure sensitivity enforcement, cultural and sovereignty review, correction propagation, rollback execution, and public-safe representation implementation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "dd376c703b7b297f7cb62c729aec69fefafcb5b8"
  prior_blob: cce8a5b42c1820bd14679cd3f532585d21611fcd
  request_sha256: c0dec7ff91c5d7dff669495432d0c4d6cd6777c2780ce9327c0217a9331dd00e
  confirmed_lane_files:
    - pipeline_specs/settlements-infrastructure/README.md
    - pipeline_specs/settlements-infrastructure/ingest.yaml
    - pipeline_specs/settlements-infrastructure/normalize.yaml
    - pipeline_specs/settlements-infrastructure/validate.yaml
    - pipeline_specs/settlements-infrastructure/catalog.yaml
    - pipeline_specs/settlements-infrastructure/publish.yaml
  confirmed_stage_posture: "all five checked YAML files contain version: 1 and stages: []"
  checked_absent_paths:
    - pipeline_specs/settlements-infrastructure/triplets.yaml
    - pipeline_specs/settlements-infrastructure/rollback.yaml
    - pipeline_specs/settlements-infrastructure/watchers.yaml
    - tests/pipeline_specs/settlements-infrastructure/README.md
    - fixtures/pipeline_specs/settlements-infrastructure/README.md
  alias_posture: "pipeline_specs/settlement/README.md is a repository-grounded compatibility alias subordinate to this lane"
  workflow_posture: ".github/workflows/domain-settlements-infrastructure.yml runs on pull requests and main pushes but all three jobs are TODO-only echo scaffolds"
related:
  - ../README.md
  - ../settlement/README.md
  - ../../pipelines/domains/settlements-infrastructure/README.md
  - ../../pipelines/domains/settlement/README.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../contracts/domains/settlements-infrastructure/README.md
  - ../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../policy/domains/settlements-infrastructure/README.md
  - ../../data/registry/sources/settlements-infrastructure/README.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/domain-settlements-infrastructure.yml
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, pipeline-specs, settlements-infrastructure, canonical-working-lane, settlement-alias, ingest, normalize, validate, catalog, publish, inert-scaffolds, settlement-identity, municipality, census-place, townsite, ghost-town, reservation-community, critical-infrastructure, facility, service-area, operator, condition-observation, dependency, source-role, temporal, evidence, receipts, release-gated, governance, no-parallel-authority]
notes:
  - "v0.2 replaces proposed directory trees and generic profile claims with a commit-pinned account of the six confirmed lane files and the five inert stage YAML scaffolds."
  - "The hyphenated settlements-infrastructure segment is the current working canonical domain lane; the shorter settlement path remains a compatibility alias unless an accepted ADR and migration record change that relationship."
  - "File presence, parseable YAML, version: 1, stages: [], a workflow conclusion, a source descriptor, a map feature, or a schedule does not establish activation, source authority, legal status, operational status, evidence closure, policy approval, catalog closure, release approval, or publication."
  - "Restricted facility details, dependency or vulnerability topology, operator-sensitive material, private-property or living-person joins, exact culturally sensitive or burial-adjacent locations, unresolved legal status, and unclear-rights sources fail closed by default."
  - "This revision changes documentation and generated process provenance only. It does not create or activate pipeline specs, schemas, policies, sources, fixtures, tests, executable logic, lifecycle objects, pipeline receipts, proofs, releases, or public surfaces."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Pipeline Specification Lane

`pipeline_specs/settlements-infrastructure/`

> **One-line purpose.** Govern declarative Settlements / Infrastructure run intent while keeping source admission, executable processing, evidence, policy, lifecycle state, catalog closure, release decisions, and public delivery in their separate authority roots.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![version](https://img.shields.io/badge/version-v0.2-informational)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-canonical__working__lane-blueviolet)
![inventory](https://img.shields.io/badge/inventory-README%20%2B%205%20YAMLs-lightgrey)
![stages](https://img.shields.io/badge/stages-all__empty-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-fail__closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> [!IMPORTANT]
> **Evidence snapshot:** `main@dd376c703b7b297f7cb62c729aec69fefafcb5b8`  
> **Target blob before this revision:** `cce8a5b42c1820bd14679cd3f532585d21611fcd`  
> **Confirmed lane inventory:** `README.md`, `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, and `publish.yaml`  
> **Confirmed stage posture:** every checked YAML file contains `version: 1` and `stages: []`  
> **Activation:** a path, filename, merge, parseable YAML file, workflow conclusion, source-list entry, schedule, map layer, or empty stage declaration activates nothing by itself

> [!CAUTION]
> A settlement candidate is not an incorporated municipality. A census place is not municipality truth. A gazetteer entry is not current legal status. A mapped facility is not proof of current operation. A service area is not a service guarantee. A condition observation is time-bounded evidence, not evergreen operational status. A successful run is not an `EvidenceBundle`, `PolicyDecision`, catalog closure, `ReleaseManifest`, or release.

> [!WARNING]
> Do not place restricted facility details, dependency or vulnerability topology, operator-sensitive records, private person-or-property joins, exact culturally sensitive or burial-adjacent locations, credentials, secrets, or unreleased lifecycle data in specs, examples, fixtures, logs, screenshots, or pull-request bodies. Use synthetic, generalized, or irreversibly redacted examples and fail closed when rights, sensitivity, source role, legal status, operational status, evidence, review, or release state is unresolved.

## Quick navigation

- [Purpose](#purpose)
- [Current status](#current-status)
- [Authority and anti-collapse](#authority-and-anti-collapse)
- [Bounded context and ubiquitous language](#bounded-context-and-ubiquitous-language)
- [Current inspected inventory](#current-inspected-inventory)
- [Canonical lane and compatibility alias](#canonical-lane-and-compatibility-alias)
- [Explicit non-ownership](#explicit-non-ownership)
- [Stage scaffold contract](#stage-scaffold-contract)
- [Minimum future machine contract](#minimum-future-machine-contract)
- [State and activation model](#state-and-activation-model)
- [Sources, roles, rights, and authority](#sources-roles-rights-and-authority)
- [Settlement identity and legal-status boundaries](#settlement-identity-and-legal-status-boundaries)
- [Infrastructure and operational-status boundaries](#infrastructure-and-operational-status-boundaries)
- [Temporal and source-vintage semantics](#temporal-and-source-vintage-semantics)
- [Lifecycle gates and finite outcomes](#lifecycle-gates-and-finite-outcomes)
- [Ingest profile](#ingest-profile)
- [Normalize profile](#normalize-profile)
- [Validate profile](#validate-profile)
- [Catalog profile](#catalog-profile)
- [Publish profile](#publish-profile)
- [Absent profile families](#absent-profile-families)
- [Watchers, dry runs, and no-op discipline](#watchers-dry-runs-and-no-op-discipline)
- [Receipts, evidence, and emitted artifacts](#receipts-evidence-and-emitted-artifacts)
- [Security, logging, network, and representation](#security-logging-network-and-representation)
- [Public trust membrane](#public-trust-membrane)
- [Validation and enforceability](#validation-and-enforceability)
- [Review and change discipline](#review-and-change-discipline)
- [Correction, deactivation, migration, and rollback](#correction-deactivation-migration-and-rollback)
- [Directory map](#directory-map)
- [Maintainer checklist](#maintainer-checklist)
- [Definition of done](#definition-of-done)
- [Open verification register](#open-verification-register)
- [Evidence ledger](#evidence-ledger)

---

## Purpose

`pipeline_specs/settlements-infrastructure/` is the current working canonical domain lane for declarative Settlements / Infrastructure pipeline intent.

Its safe role is to define **what may be attempted and under which gates**, including:

- stage identity, profile identity, version, owner, and review state;
- admitted source descriptor references and source-role expectations;
- lifecycle input and proposed output states;
- temporal, source-vintage, freshness, and stale-source handling;
- settlement identity and legal-status boundaries;
- infrastructure identity and operational-status boundaries;
- rights, sensitivity, private-property, living-person, cultural, sovereignty, and critical-asset controls;
- EvidenceRef and EvidenceBundle prerequisites;
- validation, receipt, policy, review, release-readiness, correction, and rollback requirements;
- deterministic no-op, deny, quarantine, and abstain behavior.

This lane does **not** currently establish active stage behavior. The five confirmed YAML files are scaffolds with empty `stages` arrays.

### Audience

- pipeline-spec and Settlements / Infrastructure maintainers;
- settlement identity, municipal/legal-status, infrastructure, service-area, operator, condition, dependency, and historic-community stewards;
- source, rights, sensitivity, temporal, evidence, policy, validation, release, security, and documentation reviewers;
- maintainers implementing a future schema, parser, registry, loader, scheduler, or executable consumer;
- reviewers preventing empty scaffolds or the `settlement` alias from being mistaken for activation or authority.

[Back to top](#top)

---

## Current status

| Surface | Repository evidence at the snapshot | Status |
|---|---|---|
| Lane README | `pipeline_specs/settlements-infrastructure/README.md` exists. | **CONFIRMED file / revised here** |
| `ingest.yaml` | Exists with `name: settlements-infrastructure-ingest`, `version: 1`, and `stages: []`. | **CONFIRMED inert scaffold** |
| `normalize.yaml` | Exists with `name: settlements-infrastructure-normalize`, `version: 1`, and `stages: []`. | **CONFIRMED inert scaffold** |
| `validate.yaml` | Exists with `name: settlements-infrastructure-validate`, `version: 1`, and `stages: []`. | **CONFIRMED inert scaffold** |
| `catalog.yaml` | Exists with `name: settlements-infrastructure-catalog`, `version: 1`, and `stages: []`. | **CONFIRMED inert scaffold** |
| `publish.yaml` | Exists with `name: settlements-infrastructure-publish`, `version: 1`, and `stages: []`. | **CONFIRMED inert scaffold** |
| `triplets.yaml` | Exact-path probe returned not found. | **CONFIRMED absent at checked path** |
| `rollback.yaml` | Exact-path probe returned not found. | **CONFIRMED absent at checked path** |
| `watchers.yaml` | Exact-path probe returned not found. | **CONFIRMED absent at checked path** |
| Compatibility alias | `pipeline_specs/settlement/README.md` exists as a repository-grounded README-only alias subordinate to this lane. | **CONFIRMED file / no active alias spec** |
| Executable lane | `pipelines/domains/settlements-infrastructure/README.md` exists. | **CONFIRMED file / runtime depth NEEDS VERIFICATION** |
| Contract lane | `contracts/domains/settlements-infrastructure/README.md` identifies the hyphenated path as the canonical working semantic lane. | **CONFIRMED file / draft contract posture** |
| Schema lane | `schemas/contracts/v1/domains/settlements-infrastructure/README.md` exists as a greenfield scaffold. | **CONFIRMED file / implementation PROPOSED** |
| Policy lane | `policy/domains/settlements-infrastructure/README.md` exists as a greenfield scaffold. | **CONFIRMED file / implementation PROPOSED** |
| Source registry | `data/registry/sources/settlements-infrastructure/README.md` exists and records unresolved registry topology. | **CONFIRMED file / topology NEEDS VERIFICATION** |
| Domain path register | `CANONICAL_PATHS.md` uses `settlements-infrastructure` as the working domain slug and records singular `settlement` variance. | **CONFIRMED file / draft register** |
| Domain workflow | `domain-settlements-infrastructure.yml` runs on pull requests and main pushes, but all three jobs only echo TODO messages. | **CONFIRMED orchestration stub / no domain enforcement** |
| Spec tests | Checked `tests/pipeline_specs/settlements-infrastructure/README.md` does not exist. | **CONFIRMED absent at checked path** |
| Spec fixtures | Checked `fixtures/pipeline_specs/settlements-infrastructure/README.md` does not exist. | **CONFIRMED absent at checked path** |
| Accepted pipeline-spec schema, parser, registry, loader, scheduler | Not established by this bounded inspection. | **UNKNOWN** |
| Active stage definitions, source bindings, schedules, automatic receipts | Not established. | **UNKNOWN** |
| Production use or release integration | Not established. | **UNKNOWN** |

> [!NOTE]
> This inventory is bounded to exact paths, pinned file reads, and indexed default-branch results inspected for this revision. It is not a recursive proof across every ref, ignored path, generated artifact, deployment, or external system.

[Back to top](#top)

---

## Authority and anti-collapse

### Responsibility split

```text
pipeline_specs/  = declarative run intent: WHAT may run and under which gates
pipelines/       = executable behavior: HOW processing occurs
connectors/      = source access and retrieval support; never publication authority
configs/         = safe-to-commit consumer settings; never secrets or activation authority
data/registry/   = source admission and authority-control records
data/            = lifecycle state, receipts, proofs, catalog/triplets, and published artifacts
contracts/       = semantic meaning
schemas/         = machine-checkable shape
policy/          = admissibility, rights, sensitivity, access, and release obligations
tests/fixtures/  = enforceability proof and controlled synthetic/generalized examples
release/         = promotion, release, correction, withdrawal, and rollback authority
apps/            = governed serving surfaces; never direct reads from specs or internal stores
```

Directory Rules assign declarative configuration to `pipeline_specs/` and executable behavior to `pipelines/`. `settlements-infrastructure` is a domain segment inside responsibility roots, not a new root.

### What this README may decide

This README may define the maintenance boundary for this lane:

- what the confirmed files currently contain;
- what future specs would have to declare;
- what must remain under another responsibility root;
- which anti-collapse, sensitivity, evidence, validation, review, and release gates must be preserved;
- which claims remain `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.

### What this README cannot decide

This README cannot:

- admit or activate a source;
- make an empty stage executable;
- establish a canonical machine schema;
- define semantic object truth in place of contracts;
- satisfy policy, rights, sensitivity, evidence, or review requirements;
- validate lifecycle data;
- assert municipal, operational, ownership, service, safety, or emergency truth;
- close a catalog or graph projection;
- approve release, publication, access, or public representation;
- resolve the `settlement` versus `settlements-infrastructure` path conflict;
- prove runtime, deployment, branch-protection, or production behavior.

### Disallowed collapses

```text
file presence -> implementation
parseable YAML -> valid governed spec
version: 1 -> accepted schema version
stages: [] -> successful no-op run
pipeline spec -> executable pipeline
pipeline spec -> source admission
source descriptor ref -> source authority for every claim
source list -> evidence closure
schedule -> freshness proof
ingest spec -> RAW capture
normalize spec -> correct transformation
validate spec -> EvidenceBundle
catalog spec -> catalog truth
publish spec -> ReleaseManifest
successful workflow -> substantive domain validation
settlement candidate -> incorporated municipality
census place -> municipal legal status
gazetteer record -> current legal status
facility record -> current operation
condition observation -> evergreen operational status
service area -> guaranteed service
dependency edge -> public-safe topology
public profile -> publication
generated summary -> evidence
settlement alias -> parallel canonical authority
```

[Back to top](#top)

---

## Bounded context and ubiquitous language

The domain combines two related but distinct sublanes. A future spec must preserve the distinction rather than flattening all place and infrastructure records into one generic feature type.

### Settlements sublane

| Term | Working meaning | Must not be collapsed into |
|---|---|---|
| `Settlement` | A place/community identity candidate supported by source-role and temporal evidence. | Municipality, census place, parcel, address, or current occupancy truth. |
| `Municipality` | A legal incorporated-place claim requiring appropriate legal-status authority and valid-time scope. | Census place, informal settlement, postal name, or gazetteer entry. |
| `CensusPlace` | A statistical/geographic census identity tied to a source vintage. | Municipal incorporation or current legal boundary truth. |
| `Townsite` | A platted, founded, promoted, or historically recorded place identity. | Continuing settlement or legal municipality. |
| `GhostTown` | A historical settlement identity with uncertainty and possible archaeology/cultural sensitivity. | Public-safe exact location by default. |
| `Fort` | A military-post/place identity that may be historic, archaeological, or culturally sensitive. | Current operational facility status. |
| `Mission` | A religious mission/place identity that may require cultural, sovereignty, or burial-adjacent review. | Unrestricted exact-location publication. |
| `ReservationCommunity` | A community identity whose treatment may implicate tribal sovereignty and cultural review. | Ordinary municipal or census-place handling. |

### Infrastructure sublane

| Term | Working meaning | Must not be collapsed into |
|---|---|---|
| `InfrastructureAsset` | A physical or logical infrastructure identity candidate. | Public-safe detail, current operation, or parcel ownership. |
| `NetworkNode` | A node in an infrastructure network projection. | Road/rail transport graph node unless separately governed. |
| `NetworkSegment` | A segment in an infrastructure network projection. | Road/rail route truth or public-safe dependency topology. |
| `Facility` | A facility or operational-complex identity candidate. | Current operation, safe access, ownership, or public-release approval. |
| `ServiceArea` | A time-scoped served or planned footprint. | Guaranteed present service or legal service obligation. |
| `Operator` | An organization or role associated with an asset, network, or facility. | Ownership, liability, access authority, or current operational control without supporting evidence. |
| `ConditionObservation` | A time-bounded observation, inspection, or status statement. | Evergreen condition, safety advice, or emergency guidance. |
| `Dependency` | A governed relationship between assets, systems, services, places, or facilities. | Automatically public-safe topology or vulnerability analysis. |

### Cross-domain boundaries

- Roads/Rail/Trade owns transport-route and transport-network truth.
- People/DNA/Land owns living-person, parcel, title, ownership, and private person-property joins.
- Archaeology owns archaeological and sensitive cultural-site truth.
- Hazards owns hazard events, warnings, declarations, and emergency-status truth.
- Hydrology owns water-body, gage, aquifer, watershed, and hydrologic evidence.
- Spatial Foundation owns shared spatial-reference and foundational geometry concerns.
- Settlements / Infrastructure may reference these lanes as governed context; it must not absorb their authority.

[Back to top](#top)

---

## Current inspected inventory

### Confirmed files

```text
pipeline_specs/settlements-infrastructure/
├── README.md
├── ingest.yaml
├── normalize.yaml
├── validate.yaml
├── catalog.yaml
└── publish.yaml
```

### Confirmed YAML shape

Every checked stage file currently follows this minimal scaffold pattern:

```yaml
# pipeline_specs :: settlements-infrastructure :: <stage>
name: settlements-infrastructure-<stage>
version: 1
stages: []
```

This is **repository evidence of scaffold presence**, not an accepted pipeline-spec contract.

### Checked absent paths

```text
pipeline_specs/settlements-infrastructure/triplets.yaml
pipeline_specs/settlements-infrastructure/rollback.yaml
pipeline_specs/settlements-infrastructure/watchers.yaml
tests/pipeline_specs/settlements-infrastructure/README.md
fixtures/pipeline_specs/settlements-infrastructure/README.md
```

Do not infer that all tests, fixtures, profiles, or generated files are absent everywhere. The claim is limited to the exact checked paths.

### Interpretation

The current lane is best described as:

- **CONFIRMED:** a README plus five YAML scaffolds;
- **CONFIRMED:** each scaffold has an empty stage list;
- **PROPOSED:** future governed stage contracts and machine validation;
- **UNKNOWN:** consumers, activation, schedules, stage implementations, automatic receipts, and runtime use.

[Back to top](#top)

---

## Canonical lane and compatibility alias

The current working relationship is:

```text
pipeline_specs/settlements-infrastructure/  # governing whole-domain declarative lane
pipeline_specs/settlement/                  # compatibility alias; README-only at the inspected snapshot
```

Rules:

1. Whole-domain stage specifications belong in the hyphenated lane.
2. The shorter alias must not define duplicate source bindings, schemas, policies, lifecycle outputs, release behavior, or public surfaces.
3. Any future alias profile must bind explicitly to this lane and preserve all infrastructure controls.
4. An alias file must not silently override or shadow a canonical profile.
5. Migration or consolidation requires an accepted ADR or equivalent decision record, a path map, compatibility plan, validator coverage, receipts, correction handling, and rollback instructions.
6. The existence of both paths is a visible governance conflict, not permission to operate two authorities.

> [!IMPORTANT]
> The alias may narrow scope; it may not weaken source-role, legal-status, operational-status, temporal, sensitivity, evidence, policy, review, release, correction, or rollback requirements.

[Back to top](#top)

---

## Explicit non-ownership

| This lane does not own | Governing responsibility root or lane |
|---|---|
| Source fetching clients, credentials, endpoint retry behavior | `connectors/`, runtime secret stores, and approved infrastructure |
| Source admission and source authority records | `data/registry/sources/` and accepted registry topology |
| Semantic definitions of domain objects | `contracts/domains/settlements-infrastructure/` |
| Machine-checkable domain schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted ADR-selected home |
| Admissibility, rights, sensitivity, access, redaction, and release policy | `policy/` responsibility roots |
| Executable transformations | `pipelines/domains/settlements-infrastructure/` and shared executable lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| Pipeline run receipts | Accepted `data/receipts/` lanes |
| EvidenceBundles and proof packs | Accepted `data/proofs/` lanes |
| Catalog and graph truth | Governed catalog/triplet artifacts after validation |
| Municipal legal status | Appropriate legal authorities represented through admitted sources and evidence |
| Parcel, title, ownership, or living-person truth | People/DNA/Land lanes and appropriate authorities |
| Current facility operation, service availability, or safety guidance | Current authoritative sources, policy, review, and emergency/operational authorities |
| Release, correction, withdrawal, takedown, or rollback decisions | `release/` |
| Public API, UI, tile, scene, map, or AI delivery | Governed applications using released artifacts |

[Back to top](#top)

---

## Stage scaffold contract

The existing files are named by lifecycle-oriented pipeline stage, but their empty `stages` arrays establish no behavior.

### Current guarantees

A current scaffold guarantees only that:

- the file exists at the checked path;
- GitHub returned the recorded blob;
- the file is small YAML-shaped text;
- it carries a `name`, integer `version`, and empty `stages` list.

### Current non-guarantees

A current scaffold does not guarantee:

- conformance to an accepted schema;
- registration in a loader or scheduler;
- a valid executable implementation reference;
- source admission or source availability;
- stage ordering or dependency resolution;
- input/output lifecycle correctness;
- policy, rights, sensitivity, or evidence closure;
- receipt emission;
- idempotence, retry safety, or rollback;
- any runtime, deployment, or public effect.

### Safe handling rule

Until an accepted parser and schema say otherwise, consumers should treat `stages: []` as **inactive or non-runnable**, not as a successful governed no-op.

[Back to top](#top)

---

## Minimum future machine contract

The repository does not currently establish an accepted Settlements / Infrastructure pipeline-spec schema. The following is a **PROPOSED design contract**, not a current file format.

A future machine-readable profile should carry at least:

| Field family | Minimum intent |
|---|---|
| Identity | Stable `spec_id`, profile type, domain, version, digest, owner, status, and supersession refs. |
| Authority | Canonical lane ref, alias posture, contract refs, schema refs, policy refs, and reviewer requirements. |
| Implementation | Executable target ref, implementation version/digest, supported operation, and dry-run support. |
| Sources | Source descriptor refs, source roles, authority scopes, rights states, source heads, vintages, and admission prerequisites. |
| Lifecycle | Allowed input states, proposed output state, quarantine outcomes, and promotion prerequisites. |
| Time | Retrieval, issue, observation, valid, effective, release, correction, expiry, and stale-after semantics where applicable. |
| Identity boundaries | Settlement, municipality, census place, townsite, historic community, facility, operator, service area, condition, and dependency distinctions. |
| Risk | Sensitivity, privacy, critical-asset, cultural, sovereignty, exact-location, legal-status, operational-status, and representation gates. |
| Evidence | Required EvidenceRefs, EvidenceBundle closure, citation policy, validation reports, and abstention behavior. |
| Receipts | Run, transform, validation, quarantine, redaction/generalization, representation, catalog, release-readiness, and rollback-readiness receipts. |
| Outcomes | Finite allow, deny, quarantine, abstain, no-op, stale, superseded, and error states. |
| Release | Release candidate refs, review requirements, correction path, rollback target, and an explicit default of not release-ready. |

Illustrative only:

```yaml
schema_version: PROPOSED-kfm.pipeline-spec.v1
spec_id: settlements-infrastructure.<profile>
domain: settlements-infrastructure
profile_type: <ingest|normalize|validate|catalog|publish>
version: 0.1.0
status: draft
canonical_lane: pipeline_specs/settlements-infrastructure
implementation_ref:
  path: pipelines/domains/settlements-infrastructure/<operation>
  digest: NEEDS_VERIFICATION
sources:
  descriptor_refs: []
  required_roles: []
lifecycle:
  allowed_inputs: []
  proposed_output: null
time:
  stale_after: null
requirements:
  rights_closed: false
  sensitivity_closed: false
  evidence_bundle_required: true
  policy_decision_required: true
  review_record_required: true
  release_ready: false
outcomes:
  allowed: [deny, quarantine, abstain, no_op]
```

Do not create a concrete schema or parser from this README alone. That requires schema/contract/policy alignment, tests, fixtures, validator wiring, migration notes, and review.

[Back to top](#top)

---

## State and activation model

No accepted activation state machine was found. The following is **PROPOSED** for future implementation.

```text
DRAFT
  -> VALIDATED
  -> REVIEWED
  -> ELIGIBLE
  -> ACTIVE
  -> DEACTIVATED
  -> SUPERSEDED
```

Side states:

```text
INVALID
DENIED
QUARANTINED
STALE
WITHDRAWN
ERROR
```

### Activation prerequisites

A future profile should not become `ACTIVE` unless all applicable conditions close:

- accepted machine schema;
- deterministic identity and content digest;
- canonical-lane registration;
- executable implementation reference and version;
- source descriptor admission and source-role review;
- rights and redistribution review;
- sensitivity, privacy, cultural, sovereignty, critical-asset, and exact-location review;
- lifecycle input/output validation;
- temporal and stale-state rules;
- fixture and negative-test coverage;
- receipt emission;
- reviewer approval separate from generation;
- release/correction/rollback posture where outputs can progress toward publication.

### Non-activation events

The following must not activate a profile:

- creating or renaming a file;
- merging a README;
- parsing YAML successfully;
- incrementing `version`;
- adding a schedule string;
- a TODO-only workflow passing;
- a source becoming reachable;
- a map layer rendering;
- an AI summary naming the profile.

[Back to top](#top)

---

## Sources, roles, rights, and authority

A stage profile may reference source descriptors. It must not turn source references into claim authority.

### Source role requirements

A future profile should declare the role each source may play for each claim family. Examples include:

- authoritative or primary legal-status evidence;
- corroborating observation;
- contextual or historical evidence;
- model-derived or inferred evidence;
- restricted evidence;
- disallowed evidence for a claim type.

The exact repository enum is **NEEDS VERIFICATION**. Do not hard-code a new enum here without checking the accepted source schema and registries.

### Source admission versus source use

```text
source discovered
  -> source descriptor reviewed
  -> rights/sensitivity/authority scope assessed
  -> source admitted for bounded purposes
  -> source material retrieved to RAW by governed connector
  -> claim-specific use evaluated
```

Admission is not blanket authority. A source may be admissible for one purpose and disallowed for another.

### Rights gates

A profile should fail closed when it cannot resolve:

- license and redistribution terms;
- required attribution;
- endpoint terms and access limits;
- derivative and cache rights;
- public-release permissions;
- retention and deletion obligations;
- living-person or private-property restrictions;
- tribal, cultural, archival, or community-specific obligations;
- operator-provided restrictions;
- source-vintage and supersession status.

### Source families

Domain documentation identifies source families such as census geography, gazetteers, state/local GIS, legal records, historical maps, infrastructure operators, transportation/facility sources, and hazard/resilience sources. Their current terms, authority scopes, cadence, and release posture remain source-specific and **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Settlement identity and legal-status boundaries

Future specs must preserve separate identity and status claims.

### Required distinctions

```text
named place
settlement candidate
census place
incorporated municipality
unincorporated community
townsite
historic settlement
ghost town
fort
mission
reservation community
postal place name
administrative unit
```

### Legal-status rule

A profile may configure how legal-status evidence is evaluated. It cannot itself declare incorporation, annexation, dissolution, boundary validity, jurisdiction, or official current status.

Legal-status claims require:

- an appropriate authority source;
- explicit source role and authority scope;
- source and valid time;
- supersession and correction handling;
- geometry provenance where a boundary is involved;
- review proportionate to consequence;
- EvidenceBundle closure before authoritative presentation;
- release review before public use.

### Identity conflict handling

When sources disagree:

1. retain source-specific assertions;
2. do not overwrite one assertion with another;
3. preserve source vintage and retrieval time;
4. create a reviewable conflict record;
5. quarantine or abstain when resolution affects legal or public consequence;
6. issue corrections or supersession records when a previously released claim changes.

[Back to top](#top)

---

## Infrastructure and operational-status boundaries

Infrastructure records can create public-safety, security, privacy, commercial, and operational risk. The default is fail closed.

### Critical distinctions

```text
asset identity != public-safe asset detail
facility existence != current operation
operator association != ownership or control
service area != guaranteed service
condition observation != evergreen condition
dependency relation != public-safe topology
network model != current operational network
map feature != access authorization
```

### Working sensitivity posture

The domain canonical-path register records a working posture of:

- T4 default for critical-asset detail;
- T1 for generalized public-safe footprints;
- T0 for legal-status settlement names.

That is evidence of the draft register’s posture, not proof that every policy, validator, API, tile, or release path enforces it. Implementation remains **NEEDS VERIFICATION**.

### Fail-closed triggers

A profile should deny, quarantine, generalize, redact, or abstain when it encounters unresolved:

- exact critical-facility geometry;
- vulnerability or dependency topology;
- operator-sensitive details;
- current access, staffing, capacity, condition, outage, or readiness information;
- private property or living-person associations;
- sensitive cultural, burial-adjacent, sacred, or tribal context;
- precise historic locations whose exposure may increase harm;
- uncertain public-release rights;
- inferred operational claims generated from stale or indirect evidence.

### Emergency and safety boundary

This lane must not generate operational instructions, emergency guidance, access advice, or safety assurances. Public-facing safety information must come from appropriate current authorities through governed release channels.

[Back to top](#top)

---

## Temporal and source-vintage semantics

Time is not one field. A future profile must distinguish time kinds when material.

| Time kind | Meaning |
|---|---|
| Retrieval time | When KFM obtained the source material. |
| Source issue time | When the source published or issued the record. |
| Observation time | When an observed condition or event was measured. |
| Valid time | When the assertion is intended to hold. |
| Effective time | When a legal or administrative change takes effect. |
| Source vintage | Edition, survey, census, database, or release vintage. |
| Processing time | When KFM transformed or validated the material. |
| Release time | When a governed artifact was released. |
| Correction time | When a prior assertion or release was corrected. |
| Expiry/stale time | When a source or assertion should no longer be treated as current without review. |

### Temporal rules

- Never present a source retrieval date as the observation or valid date.
- Never present a census vintage as current municipal legal status.
- Never treat a condition observation as evergreen.
- Never infer current operation from a historical or undated facility record.
- A stale source may remain historical evidence but must not silently support a current-status claim.
- Correction and supersession must preserve prior versions and their release context where policy permits.
- Public summaries must expose enough time context to prevent stale-state overclaiming.

[Back to top](#top)

---

## Lifecycle gates and finite outcomes

KFM’s lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A pipeline spec can declare prerequisites for a transition. It cannot perform or approve the transition by existing.

### Stage-to-lifecycle relationship

| Profile | May declare intent around | Must not be mistaken for |
|---|---|---|
| `ingest` | admitted source retrieval and RAW handoff prerequisites | source admission or successful RAW capture |
| `normalize` | WORK transforms and normalized candidate outputs | semantic truth or processed acceptance |
| `validate` | checks, quarantine routing, and PROCESSED eligibility | EvidenceBundle closure or policy approval |
| `catalog` | catalog-candidate and EvidenceBundle handoff requirements | catalog truth or public discovery approval |
| `publish` | release-candidate prerequisites | release approval or PUBLISHED state |

### Finite outcomes

A future stage should produce one explicit terminal outcome per bounded item or run:

```text
accepted_for_next_gate
denied
quarantined
abstained
no_material_change
stale
superseded
withdrawn
failed
```

Avoid ambiguous “success” states that conceal whether evidence, policy, release, or publication actually occurred.

### Quarantine

Quarantine must record:

- reason code;
- affected object/source/spec refs;
- evidence gap or policy blocker;
- sensitivity and rights posture;
- retry/review eligibility;
- correction or supersession refs;
- reviewer and timestamp when resolved.

[Back to top](#top)

---

## Ingest profile

`ingest.yaml` is currently an inert scaffold.

A future ingest profile may declare:

- admitted source descriptor refs;
- source head, retrieval window, cadence, and rate constraints;
- retrieval implementation ref;
- expected immutable RAW artifact naming and digest behavior;
- rights, sensitivity, and credential prerequisites;
- source-vintage capture;
- retry, partial-failure, and no-op behavior;
- required retrieval and RAW-capture receipts.

It must not:

- contain credentials or private tokens;
- admit its own source;
- fetch directly from public clients;
- convert RAW material into authoritative domain truth;
- bypass quarantine or policy;
- treat network success as evidence closure.

### Ingest no-op

A safe no-op should be explicit, such as “source head unchanged and no governed retrieval required,” with a receipt. An empty `stages` list is not that receipt.

[Back to top](#top)

---

## Normalize profile

`normalize.yaml` is currently an inert scaffold.

A future normalize profile may declare:

- accepted RAW/WORK input classes;
- transformation implementation ref and digest;
- field mapping and controlled vocabulary refs;
- coordinate reference, geometry repair, and generalization requirements;
- identity-candidate construction;
- source assertion preservation;
- temporal normalization without collapsing time kinds;
- uncertainty and conflict handling;
- required transform and representation receipts.

It must not:

- overwrite source assertions without provenance;
- turn a source label into a canonical identity without review;
- infer municipality status from a census or gazetteer record;
- infer current facility operation from presence;
- erase uncertainty, source vintage, or valid time;
- publish exact sensitive geometry.

[Back to top](#top)

---

## Validate profile

`validate.yaml` is currently an inert scaffold.

A future validate profile may declare checks for:

- accepted schema and contract conformance;
- deterministic identity;
- required source descriptors and source roles;
- rights and redistribution state;
- temporal completeness and stale-state handling;
- settlement versus municipality versus census-place boundaries;
- operational-status overclaim prevention;
- geometry, topology, and cross-domain ownership boundaries;
- critical-asset, private-property, living-person, cultural, sovereignty, and exact-location sensitivity;
- EvidenceRef resolution and EvidenceBundle prerequisites;
- quarantine routing and finite outcomes;
- required validation and policy-decision receipts.

A validation pass must not be represented as:

- legal-status authority;
- operational truth;
- EvidenceBundle closure unless the evidence contract is actually satisfied;
- catalog closure;
- release approval;
- public-safe representation approval unless that review is separately recorded.

[Back to top](#top)

---

## Catalog profile

`catalog.yaml` is currently an inert scaffold.

A future catalog profile may declare:

- eligible PROCESSED inputs;
- catalog record contract and schema refs;
- EvidenceBundle linkage;
- source-role, temporal, rights, sensitivity, and review prerequisites;
- discovery metadata and public/private visibility posture;
- graph/triplet handoff requirements;
- correction, supersession, and withdrawal refs;
- catalog-build receipts.

It must not:

- make catalog presence equivalent to truth;
- expose restricted internal records through discovery;
- omit source-vintage or correction state;
- publish unresolved exact facility or cultural locations;
- create public AI-answer authority without released evidence.

[Back to top](#top)

---

## Publish profile

`publish.yaml` is currently an inert scaffold.

A future publish profile may declare prerequisites for constructing a release candidate, including:

- released-artifact contract and schema refs;
- EvidenceBundle closure;
- policy and sensitivity decisions;
- rights and attribution closure;
- public-safe geometry and representation receipts;
- human review state;
- catalog/triplet closure where required;
- correction path, rollback target, and withdrawal behavior;
- ReleaseManifest input requirements.

It must default to:

```yaml
release_ready: false
```

A publish profile must not:

- approve itself;
- write directly to public clients or canonical public stores without release authority;
- convert a successful dry run into publication;
- expose precise critical-asset, private, or culturally sensitive details;
- omit correction and rollback support.

[Back to top](#top)

---

## Absent profile families

The following exact paths were checked and are absent:

- `triplets.yaml`;
- `rollback.yaml`;
- `watchers.yaml`.

Their absence matters because the lifecycle and root README discuss triplet, rollback, and watcher responsibilities. Do not describe them as implemented.

### Future `triplets` profile

A future triplet profile would require graph-projection contracts, evidence linkage, relation ownership, sensitivity propagation, provenance, correction, and derived-not-canonical labeling.

### Future `rollback` profile

A future rollback profile would describe rollback-readiness checks. Rollback authority and execution would remain under release/runtime governance.

### Future `watchers` profile

A future watcher profile would observe source or registry changes and emit bounded change reports. Watchers must remain non-publishers.

Create these files only when real consumers, schemas, tests, fixtures, receipts, and owners exist. Avoid empty placeholder proliferation.

[Back to top](#top)

---

## Watchers, dry runs, and no-op discipline

### Watchers

A watcher may:

- compare source heads or registry versions;
- detect material changes;
- emit a change report or queue a governed run;
- identify stale or withdrawn sources.

A watcher may not:

- admit a source;
- write RAW source payloads unless it is also a governed connector operation;
- promote lifecycle state;
- publish or alter released artifacts;
- convert a detected change into truth;
- bypass rights, sensitivity, policy, review, correction, or rollback.

### Dry runs

A dry run should:

- use synthetic, generalized, redacted, or approved fixture data;
- avoid network access unless explicitly governed;
- produce no public or canonical lifecycle mutation;
- emit a dry-run receipt;
- expose proposed decisions and blockers without approving them.

### No-op

A no-op is a finite governed outcome. It should record why no action was required, which source/spec versions were compared, and whether stale-state review remains necessary.

`stages: []` is not proof that a no-op was evaluated.

[Back to top](#top)

---

## Receipts, evidence, and emitted artifacts

### Separation

```text
spec                  -> declarative intent
run receipt           -> process memory
validation report     -> check results
EvidenceRef           -> pointer to evidence
EvidenceBundle        -> governed evidence closure
PolicyDecision        -> admissibility/access/release decision
ReviewRecord          -> human or governed review state
catalog/triplet       -> discovery or derived relationship projection
ReleaseManifest       -> release authority record
published artifact    -> released public or restricted representation
```

None of these may substitute for another.

### Future receipt expectations

Depending on stage and risk, a future run may require:

- source-head and retrieval receipt;
- RAW capture receipt;
- transform receipt;
- identity-resolution receipt;
- temporal-normalization receipt;
- validation report;
- quarantine receipt;
- rights and sensitivity decision;
- redaction/generalization receipt;
- public-safe representation receipt;
- catalog-build receipt;
- release-readiness receipt;
- correction or supersession receipt;
- rollback-readiness receipt.

### Evidence rule

Claims derived from pipeline outputs require EvidenceRefs that resolve to EvidenceBundles when the claim significance demands it. Generated language, a map render, a spec, a receipt, or a successful workflow is not evidence by itself.

[Back to top](#top)

---

## Security, logging, network, and representation

### Secrets

Specs must not contain:

- passwords;
- API keys;
- bearer tokens;
- private keys;
- connection strings;
- sensitive endpoint credentials;
- private contact records;
- unreleased security details.

Reference approved secret identifiers or runtime configuration contracts instead.

### Logs

Logs and receipts should avoid:

- exact restricted facility coordinates;
- dependency/vulnerability topology;
- private addresses or person-property joins;
- culturally sensitive exact locations;
- raw source payloads;
- secrets;
- unrestricted operator-sensitive records.

Use stable identifiers, digests, counts, generalized areas, reason codes, and redacted samples.

### Network

A spec may declare network prerequisites. Executable network access belongs to governed connectors or runtime implementations with:

- bounded hosts and methods;
- timeout and retry limits;
- rate-limit handling;
- credential isolation;
- rights and endpoint-term review;
- deterministic source-head capture;
- audit logging;
- fail-closed behavior.

### Representation

Public-safe representation may require:

- geometry generalization;
- coordinate rounding;
- aggregation;
- class suppression;
- temporal delay;
- label redaction;
- removal of dependency edges;
- removal of operational attributes;
- staged or restricted access.

Every material representation transform should be receipted and reversible to an internal governed source artifact where policy permits.

[Back to top](#top)

---

## Public trust membrane

Public clients must not read pipeline specs or internal lifecycle stores directly.

```text
governed release
  -> released artifact
  -> governed API
  -> public UI / map / AI response
```

The normal public path must preserve:

- release state;
- source and evidence traceability;
- policy and sensitivity decisions;
- public-safe representation;
- citation behavior;
- correction notices;
- rollback and withdrawal handling;
- bounded confidence or abstention.

A spec may inform a pipeline run. It is never a public truth surface.

[Back to top](#top)

---

## Validation and enforceability

### Current validation evidence

| Check | Current evidence | Status |
|---|---|---|
| YAML text presence | Five files read from the pinned commit. | **CONFIRMED** |
| Basic keys | Each file has `name`, `version`, and `stages`. | **CONFIRMED** |
| Empty stages | Every file has `stages: []`. | **CONFIRMED** |
| Accepted schema validation | No accepted schema/validator was established. | **UNKNOWN** |
| Loader/registry validation | No loader or registry was established. | **UNKNOWN** |
| Stage implementation refs | None are present in the current scaffolds. | **CONFIRMED absent in file content** |
| Stage-specific tests/fixtures | Checked README paths absent; exhaustive inventory not proven. | **NEEDS VERIFICATION** |
| Domain workflow enforcement | Workflow jobs only echo TODO. | **CONFIRMED no substantive domain enforcement** |
| Runtime execution | Not established. | **UNKNOWN** |

### Required positive cases for future implementation

1. Valid canonical profile with accepted schema and digest.
2. Valid implementation ref and compatible version.
3. Admitted source descriptor with allowed role and authority scope.
4. Complete temporal/source-vintage handling.
5. Deterministic identity and idempotent rerun.
6. Correct lifecycle input/output boundary.
7. Required receipts emitted.
8. EvidenceRef resolution where required.
9. Rights, sensitivity, and policy closure.
10. Alias profile resolves to canonical authority without shadowing.
11. Public-safe representation removes restricted details.
12. Correction and rollback refs resolve.

### Required negative cases

1. Unknown schema version.
2. Empty stage list treated as active.
3. Missing implementation ref.
4. Unadmitted or withdrawn source.
5. Source role incompatible with claim.
6. Census place presented as municipality.
7. Gazetteer entry presented as current legal status.
8. Facility presence presented as current operation.
9. Service area presented as guarantee.
10. Stale condition presented as current.
11. Exact critical-asset geometry in public profile.
12. Dependency topology in public output.
13. Private person-property join without authority.
14. Sensitive cultural location without review.
15. Missing EvidenceBundle for a significant claim.
16. Missing rights or attribution state.
17. Alias profile shadows canonical profile.
18. Publish profile self-approves release.
19. Watcher publishes.
20. Rollback profile performs release rollback without authority.
21. Unknown outcome or silent partial success.
22. Missing correction path for release-capable output.

### Validation layers

```text
syntax
  -> schema
  -> contract
  -> source registry and role
  -> rights and sensitivity policy
  -> lifecycle and temporal checks
  -> identity and domain-boundary checks
  -> evidence closure
  -> review
  -> release readiness
```

A pass at one layer does not imply a pass at the next.

[Back to top](#top)

---

## Review and change discipline

### Review burden

Changes should be reviewed by the smallest set that covers the affected authority:

| Change | Minimum review concern |
|---|---|
| README wording only | Pipeline-spec/domain/docs maintainers; ensure no implementation overclaim. |
| Scaffold key changes | Pipeline-spec, schema, executable-consumer, validation, and migration review. |
| Source binding | Source, rights, domain, evidence, and policy review. |
| Settlement legal-status logic | Domain and legal-status authority review. |
| Infrastructure detail or dependency handling | Infrastructure sensitivity/security and policy review. |
| Public-safe representation | Sensitivity, release, API/UI, and correction review. |
| Activation or schedule | Runtime, operations, security, source, and rollback review. |
| Alias/canonical path change | ADR/path-map/migration/compatibility/rollback review. |

CODEOWNERS currently routes `/pipeline_specs/` to `@bartytime4life`. That routes GitHub review; it is not proof of stewardship assignment, independent approval, policy decision, or release authority.

### Smallest reversible change

Prefer:

- one stage or contract change at a time;
- explicit versioning and supersession;
- schema and fixtures before activation;
- dry run before lifecycle mutation;
- deny-by-default for unresolved risk;
- a documented rollback path;
- no broad renames without a migration decision.

[Back to top](#top)

---

## Correction, deactivation, migration, and rollback

### Documentation rollback

This README-only revision can be reversed by reverting its commit and generated receipt commit or closing the draft PR before merge. It changes no runtime, lifecycle, release, or public state.

### Future spec correction

A correction should:

1. identify the affected spec and digest;
2. preserve the prior version;
3. state the defect and affected outputs;
4. identify affected receipts, EvidenceBundles, catalog/triplet records, releases, and public artifacts;
5. deactivate or supersede the profile where necessary;
6. re-run validation with corrected fixtures;
7. issue correction, withdrawal, or rollback records through their authority roots;
8. verify downstream propagation.

### Deactivation

Deactivation must be explicit and receipted. Removing a schedule or renaming a file is not sufficient proof that every consumer stopped.

### Path migration

Moving between `settlement` and `settlements-infrastructure` requires:

- accepted decision record;
- canonical and compatibility path map;
- inventory of references and consumers;
- schema/registry/loader migration;
- redirect or compatibility behavior;
- tests preventing split authority;
- source, receipt, catalog, release, and documentation updates;
- rollback instructions.

### Release rollback

A pipeline spec may declare rollback prerequisites. Release rollback remains a governed release operation and must identify a valid prior release target, affected consumers, correction notices, and verification receipts.

[Back to top](#top)

---

## Directory map

### Confirmed current lane

```text
pipeline_specs/settlements-infrastructure/
├── README.md        # CONFIRMED
├── ingest.yaml      # CONFIRMED; version 1; stages: []
├── normalize.yaml   # CONFIRMED; version 1; stages: []
├── validate.yaml    # CONFIRMED; version 1; stages: []
├── catalog.yaml     # CONFIRMED; version 1; stages: []
└── publish.yaml     # CONFIRMED; version 1; stages: []
```

### Checked absent, not implemented

```text
pipeline_specs/settlements-infrastructure/triplets.yaml
pipeline_specs/settlements-infrastructure/rollback.yaml
pipeline_specs/settlements-infrastructure/watchers.yaml
```

### Related responsibility roots

```text
pipeline_specs/settlement/                                  # compatibility alias
pipelines/domains/settlements-infrastructure/               # executable behavior
contracts/domains/settlements-infrastructure/               # semantic meaning
schemas/contracts/v1/domains/settlements-infrastructure/    # machine shape
policy/domains/settlements-infrastructure/                   # domain policy
data/registry/sources/settlements-infrastructure/            # source admission records
data/raw|work|quarantine|processed/...                       # lifecycle data
data/receipts/...                                            # process memory
data/proofs/...                                              # evidence/proof
release/...                                                  # release/correction/rollback authority
apps/governed-api/ and apps/explorer-web/                    # governed public delivery
```

Paths shown here reflect confirmed files or responsibility-root doctrine. Deeper implementation maturity remains separately labeled.

[Back to top](#top)

---

## Maintainer checklist

Before changing this lane:

- [ ] Pin the base commit and target blob.
- [ ] Inspect the current stage YAMLs and adjacent alias.
- [ ] Check Directory Rules, ADRs, drift registers, and canonical-path documentation.
- [ ] Confirm the change belongs under `pipeline_specs/`.
- [ ] Separate documentation, schema, policy, executable code, data, receipts, proofs, and release authority.
- [ ] Preserve settlement, municipality, census-place, historic-place, facility, service-area, operator, condition, and dependency distinctions.
- [ ] Define source roles and authority scopes.
- [ ] Resolve rights, sensitivity, privacy, cultural, sovereignty, and critical-asset handling.
- [ ] Define time kinds and stale-state behavior.
- [ ] Define finite outcomes and quarantine reason codes.
- [ ] Add accepted schema validation.
- [ ] Add positive and negative fixtures.
- [ ] Add substantive tests and workflow enforcement.
- [ ] Add deterministic identity, versioning, and supersession.
- [ ] Add receipts and EvidenceRef/EvidenceBundle requirements.
- [ ] Add correction, deactivation, migration, and rollback behavior.
- [ ] Keep release approval outside the spec.
- [ ] Keep public clients behind governed APIs and released artifacts.
- [ ] Reconcile target drift before writing.
- [ ] Review the final diff for unintended authority or sensitive-content changes.

[Back to top](#top)

---

## Definition of done

This README revision is complete when it:

- accurately records the six confirmed lane files;
- records all five YAML files as inert `stages: []` scaffolds;
- marks checked absent profile/test/fixture paths without overgeneralizing;
- preserves `pipeline_specs/` as declarative intent and `pipelines/` as executable behavior;
- treats `settlements-infrastructure` as the current working canonical lane and `settlement` as subordinate compatibility;
- preserves source admission, contract, schema, policy, lifecycle, evidence, catalog, release, and public-interface boundaries;
- defines settlement legal-status and infrastructure operational-status anti-collapse rules;
- surfaces critical-asset, privacy, cultural, sovereignty, rights, temporal, and representation risks;
- separates current evidence from proposed future design;
- provides validation, review, correction, migration, and rollback guidance;
- changes no active spec, runtime, data, release, or public behavior.

A future stage profile is not done until it has:

- an accepted schema and deterministic identity;
- a real executable consumer;
- admitted sources and bounded roles;
- rights and sensitivity closure;
- temporal and lifecycle semantics;
- positive and negative fixtures;
- substantive tests and CI;
- receipts and evidence requirements;
- finite outcomes;
- review separate from generation;
- correction, deactivation, and rollback support;
- release gating appropriate to consequence.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Required evidence |
|---|---|---|---|
| `PIPE-SPEC-SI-001` | Which machine schema is accepted for pipeline specs? | **UNKNOWN** | Accepted schema, ADR, registry, validators, fixtures, and CI. |
| `PIPE-SPEC-SI-002` | Which parser, registry, loader, and scheduler consume these YAMLs? | **UNKNOWN** | Code paths, configs, imports, runtime logs, and tests. |
| `PIPE-SPEC-SI-003` | Does any consumer interpret `stages: []` as inactive, valid no-op, or error? | **NEEDS VERIFICATION** | Parser/consumer behavior and tests. |
| `PIPE-SPEC-SI-004` | Are any of the five stage scaffolds registered or scheduled? | **UNKNOWN** | Registry, scheduler, deployment, and runtime evidence. |
| `PIPE-SPEC-SI-005` | What is the accepted `settlement` alias migration decision? | **NEEDS VERIFICATION / ADR-class** | Accepted ADR, path map, compatibility and rollback plan. |
| `PIPE-SPEC-SI-006` | What source-role enum and authority-scope model are canonical? | **NEEDS VERIFICATION** | Source schemas, registries, contracts, validators, and policy tests. |
| `PIPE-SPEC-SI-007` | Which source registry topology is canonical? | **NEEDS VERIFICATION** | Registry ADR/inventory resolving subtype-first and domain-first lanes. |
| `PIPE-SPEC-SI-008` | Which authorities support municipal and legal-status claims? | **NEEDS VERIFICATION** | Source-specific authority records, legal review, contracts, and evidence. |
| `PIPE-SPEC-SI-009` | Which infrastructure sensitivity and disclosure rules are implemented? | **NEEDS VERIFICATION** | Accepted policy, tests, redaction/generalization validators, API behavior. |
| `PIPE-SPEC-SI-010` | How are tribal sovereignty and cultural-location reviews enforced? | **NEEDS VERIFICATION** | Policy, stewardship assignments, review records, fixtures, and release tests. |
| `PIPE-SPEC-SI-011` | Are stage-specific fixtures and tests present under other paths? | **NEEDS VERIFICATION** | Recursive repository inventory and test collection. |
| `PIPE-SPEC-SI-012` | Which workflow provides substantive domain validation? | **UNKNOWN** | Non-TODO jobs, logs, required-check configuration, and failure fixtures. |
| `PIPE-SPEC-SI-013` | Which receipts are emitted automatically by each stage? | **UNKNOWN** | Emitter code, schemas, sample receipts, tests, and run logs. |
| `PIPE-SPEC-SI-014` | How are corrections propagated to catalogs, graphs, releases, APIs, maps, and AI answers? | **UNKNOWN** | Correction workflow, dependency index, receipts, and rollback tests. |
| `PIPE-SPEC-SI-015` | Is branch protection or independent code-owner approval enforced? | **NEEDS VERIFICATION** | Repository rulesets and required-review configuration. |
| `PIPE-SPEC-SI-016` | Is this lane used in production? | **UNKNOWN** | Deployment manifests, scheduler state, observability, and release records. |
| `PIPE-SPEC-SI-017` | Which Directory Rules copy is canonical? | **CONFLICTED / ADR-class** | Accepted placement ADR or registry resolution. |
| `PIPE-SPEC-SI-018` | Should triplets, rollback, and watcher profiles exist here? | **PROPOSED / NEEDS VERIFICATION** | Real consumers, contracts, schemas, tests, fixtures, and ownership. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation used | Truth label |
|---|---|---|
| `pipeline_specs/settlements-infrastructure/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Existing v0.1 target; prior blob `cce8a5b42c1820bd14679cd3f532585d21611fcd`. | **CONFIRMED** |
| `pipeline_specs/settlements-infrastructure/ingest.yaml@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | `version: 1`; `stages: []`. | **CONFIRMED inert scaffold** |
| `pipeline_specs/settlements-infrastructure/normalize.yaml@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | `version: 1`; `stages: []`. | **CONFIRMED inert scaffold** |
| `pipeline_specs/settlements-infrastructure/validate.yaml@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | `version: 1`; `stages: []`. | **CONFIRMED inert scaffold** |
| `pipeline_specs/settlements-infrastructure/catalog.yaml@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | `version: 1`; `stages: []`. | **CONFIRMED inert scaffold** |
| `pipeline_specs/settlements-infrastructure/publish.yaml@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | `version: 1`; `stages: []`. | **CONFIRMED inert scaffold** |
| Exact path probes | `triplets.yaml`, `rollback.yaml`, `watchers.yaml`, and checked test/fixture READMEs were not found. | **CONFIRMED absent at checked paths** |
| `pipeline_specs/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Root owns declarative intent; specs do not satisfy their own gates. | **CONFIRMED root documentation** |
| `pipeline_specs/settlement/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | README-only compatibility alias; canonical lane subordinate relationship. | **CONFIRMED file / draft documentation** |
| `pipelines/domains/settlements-infrastructure/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Executable lane boundary exists; runtime depth not proven here. | **CONFIRMED file / NEEDS VERIFICATION implementation** |
| `contracts/domains/settlements-infrastructure/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Semantic working lane and object-family boundaries. | **CONFIRMED file / draft contract posture** |
| `schemas/contracts/v1/domains/settlements-infrastructure/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Schema lane exists as greenfield scaffold. | **CONFIRMED file / PROPOSED implementation** |
| `policy/domains/settlements-infrastructure/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Policy lane exists as greenfield scaffold. | **CONFIRMED file / PROPOSED implementation** |
| `data/registry/sources/settlements-infrastructure/README.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Source admission boundary and unresolved registry topology. | **CONFIRMED file / topology NEEDS VERIFICATION** |
| `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Hyphenated working slug, singular-path conflict, and critical-asset sensitivity posture. | **CONFIRMED file / draft register** |
| `docs/architecture/directory-rules.md` and `docs/doctrine/directory-rules.md` | Responsibility-root and domain-segment placement law; document placement conflict remains open. | **CONFIRMED conflict** |
| `.github/CODEOWNERS@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | `/pipeline_specs/` routes review to `@bartytime4life`; enforcement remains separate. | **CONFIRMED routing / NEEDS VERIFICATION enforcement** |
| `.github/workflows/domain-settlements-infrastructure.yml@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Pull-request/main workflow with three TODO-only echo jobs. | **CONFIRMED orchestration stub** |
| `schemas/contracts/v1/receipts/generated_receipt.schema.json@dd376c703b7b297f7cb62c729aec69fefafcb5b8` | Machine shape for generated-work provenance receipt. | **CONFIRMED file** |

---

## Maintainer note

Keep this lane declarative, evidence-aware, and inactive by default. Do not add executable code, credentials, source payloads, semantic contracts, schemas, policy decisions, lifecycle outputs, pipeline receipts, EvidenceBundles, release decisions, public API/UI code, municipal legal determinations, operational assurances, restricted-facility details, dependency exposure packages, private person-property joins, culturally sensitive exact locations, or generated summaries here.

Add each artifact to its responsibility root, reference it by stable identifier or path, validate it with fixtures and tests, preserve correction and rollback, and require separate review before activation or release.
