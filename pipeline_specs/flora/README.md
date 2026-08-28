<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-flora-readme
title: pipeline_specs/flora/ — Governed Flora Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; placeholder-profiles-present; no-active-top-level-spec-established; placement-conflicts-visible; sensitive-domain
owners: OWNER_TBD — Pipeline-spec steward · Flora steward · Plant taxonomy/herbarium steward · Source and rights steward · Cultural/stewardship reviewer · Sensitivity/geoprivacy reviewer · Pipeline owner · Temporal/freshness steward · Validation steward · Evidence steward · Policy steward · Release steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; flora; declarative-only; source-role-aware; taxonomy-aware; specimen-aware; occurrence-class-aware; cultural-rights-aware; sensitivity-aware; geoprivacy-aware; reconstruction-resistant; rights-aware; time-aware; no-secrets; no-live-activation; no-direct-source-access; no-direct-lifecycle-write; no-release-authority
current_path: pipeline_specs/flora/README.md
truth_posture: CONFIRMED current target, five seven-line PROPOSED YAML placeholders, grounded watcher README, draft executable Flora documentation, README-only config lane, draft source registry with unresolved topology, scaffold contracts parent, one permissive redaction-receipt schema scaffold, scaffold policy lanes, conflicted sensitivity docs, README-backed tests, populated synthetic fixture lanes with unverified consumer alignment, two documented receipt lanes with unresolved layout, draft proof and release-candidate lanes, TODO-only Flora workflow, and placeholder CODEOWNERS / PROPOSED active-spec contract, parser-consumer binding, source-role, taxonomy, cultural-rights, lifecycle, sensitivity, evidence, activation, correction, and rollback gates / UNKNOWN accepted schema, parser, registry, scheduler, activation records, executable consumers, runtime behavior, substantive CI, emitted receipts, proof closure, release integration, and public use / NEEDS VERIFICATION owners, canonical source-registry and receipt topology, admitted sources, rights and terms, cultural authority, taxonomy authorities, object schemas, time/freshness vocabularies, sensitivity policy, protective transforms, fixtures, executable tests, validators, correction propagation, and rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ee77864fff2c28994ab8dc07723955d1ece3dbdb
  prior_blob: 857f1cf44afbcc4791d5af598cb612cc4134703a
  direct_lane_files:
    - pipeline_specs/flora/README.md
    - pipeline_specs/flora/gbif_ingest.yaml
    - pipeline_specs/flora/inaturalist_ingest.yaml
    - pipeline_specs/flora/usfws_ecos_ingest.yaml
    - pipeline_specs/flora/flora_publish_dryrun.yaml
    - pipeline_specs/flora/plants_drift_watcher.yaml
    - pipeline_specs/flora/watchers/README.md
  placeholder_posture: all five YAML files are seven-line PROPOSED inventory placeholders without indexed parser, consumer, activation, or executable-test binding
  watcher_sublane_posture: grounded README-only boundary; no active watcher profile established
  workflow_posture: domain-flora is pull-request-triggered TODO scaffolding
related:
  - ../README.md
  - ./gbif_ingest.yaml
  - ./inaturalist_ingest.yaml
  - ./usfws_ecos_ingest.yaml
  - ./flora_publish_dryrun.yaml
  - ./plants_drift_watcher.yaml
  - ./watchers/README.md
  - ../watchers/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../docs/domains/flora/SENSITIVITY.md
  - ../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../pipelines/domains/flora/README.md
  - ../../pipelines/domains/flora/watchers/README.md
  - ../../pipelines/watchers/plants/README.md
  - ../../configs/domains/flora/README.md
  - ../../data/registry/sources/flora/README.md
  - ../../data/receipts/flora/README.md
  - ../../data/receipts/pipeline/flora/README.md
  - ../../data/proofs/flora/README.md
  - ../../contracts/domains/flora/
  - ../../schemas/contracts/v1/domains/flora/README.md
  - ../../policy/domains/flora/README.md
  - ../../policy/sensitivity/flora/README.md
  - ../../tests/domains/flora/README.md
  - ../../fixtures/domains/flora/README.md
  - ../../release/candidates/flora/README.md
  - ../../.github/workflows/domain-flora.yml
  - ../../.github/CODEOWNERS
notes:
  - "v0.2 replaces the proposed flat tree with commit-pinned evidence and classifies all five direct YAML files as placeholders."
  - "The grounded watchers/ README is documentation, not watcher activation or execution evidence."
  - "Both data/receipts/flora/ and data/receipts/pipeline/flora/ exist; their canonical relationship remains NEEDS VERIFICATION."
  - "Rare, protected, medicinal, ceremonial, culturally sensitive, restoration-sensitive, steward-controlled, and reconstructable plant locations and knowledge fail closed."
  - "No executable specification, source, pipeline, policy, lifecycle object, receipt instance, proof, release object, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Flora Pipeline Specification Boundary

`pipeline_specs/flora/`

> Declarative run-intent boundary for Flora pipelines. A reviewed specification may state **what** a verified consumer should process, against which admitted sources, with which taxonomy, specimen/occurrence, cultural-rights, time, sensitivity, evidence, policy, receipt, review, correction, and release gates. It does not execute a pipeline, admit a source, decide botanical truth, lower sensitivity, create evidence, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-5__placeholders-lightgrey)
![sensitivity](https://img.shields.io/badge/rare__plant__locations-deny__by__default-critical)
![activation](https://img.shields.io/badge/activation-separate-critical)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-evidence-and-maturity) · [Inventory](#repository-fit-and-inventory) · [Contract](#minimum-active-specification-contract) · [Example](#illustrative-inactive-yaml) · [Sources](#sources-rights-cultural-authority-and-admission) · [Objects](#object-family-and-knowledge-character-boundaries) · [Sensitivity](#sensitivity-geoprivacy-cultural-rights-and-reconstruction-risk) · [Lifecycle](#lifecycle-evidence-and-release) · [Validation](#validation-review-and-activation) · [Rollback](#rollback-correction-and-deactivation) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@ee77864fff2c28994ab8dc07723955d1ece3dbdb`  
> **Prior target blob:** `857f1cf44afbcc4791d5af598cb612cc4134703a`  
> **Direct lane:** this README, five seven-line `PROPOSED` YAML placeholders, and `watchers/README.md`  
> **Activation:** filename, merge state, schedule text, syntax validity, fixture success, or a dry run activates nothing

> [!CAUTION]
> A valid-looking spec cannot turn an aggregator into source authority, a specimen into current occurrence, a crosswalk into settled identity, a conservation listing into occurrence evidence, a range/model into observation, culturally restricted knowledge into redistributable data, a restricted record into public geometry, or a successful run into evidence or release. Exact or reconstructable rare/protected/culturally sensitive locations, herbarium locality detail, restoration and seed-source sites, private identities, and risky joins fail closed.

## Purpose

This lane may eventually hold small, reviewed, deterministic profiles binding:

- immutable identity/version/digest, owners, reviewers, status, and supersession;
- one accepted parser and one verified executable consumer;
- admitted `SourceDescriptor` refs with origin roles preserved;
- rights, attribution, redistribution, cultural authority, stewardship, sensitivity, and activation;
- taxonomy/nomenclature authority and specimen-versus-occurrence knowledge character;
- lifecycle states, time facets, spatial support, uncertainty, evidence, policy, review, receipts, correction, and rollback;
- deterministic no-network fixtures and finite outcomes.

This README is not a schema, parser, registry, scheduler, activation decision, executable pipeline, source descriptor, taxonomy authority, cultural permission, policy decision, receipt, proof, catalog record, release record, public API, map layer, or generated answer.

[Back to top](#top)

## Authority and anti-collapse

```text
pipeline_specs/  = WHAT may run and under which gates
pipelines/       = HOW executable behavior occurs
connectors/      = upstream access
data/registry/   = source identity, role, rights, sensitivity, admission
contracts/       = object meaning
schemas/         = machine shape
policy/          = admissibility and sensitivity decisions
data/            = lifecycle records, receipts, proofs, catalogs, published artifacts
release/         = promotion, correction, withdrawal, rollback
apps/            = governed released serving surfaces
```

A spec may require a gate. Naming it does not satisfy it.

### Disallowed collapses

```text
spec file                  -> executable pipeline or activation
source list                -> source authority
aggregator access          -> origin evidence role
taxonomy crosswalk         -> settled taxonomic truth
specimen record            -> current occurrence
status/listing record      -> occurrence evidence
range/model/habitat        -> observed occurrence
cultural reference         -> redistribution permission
restricted occurrence      -> public occurrence
representation requirement -> performed redaction
schedule                   -> freshness proof
successful run             -> EvidenceBundle
publish dry run            -> ReleaseManifest
generated summary          -> evidence
```

### Authority homes

| Concern | Authority home | Spec relationship |
|---|---|---|
| Human Flora doctrine | `docs/domains/flora/` | Reference only |
| Semantic meaning | `contracts/domains/flora/` | Reference accepted contract IDs |
| Machine shape | `schemas/contracts/v1/domains/flora/` | Validate against accepted schema IDs |
| Source admission | Accepted source registry | Reference admitted records |
| Executable behavior | `pipelines/` | Bind one verified consumer |
| Policy/sensitivity/cultural authority | `policy/` plus review artifacts | Require decisions |
| Lifecycle | Governed `data/` states | Declare allowed transitions only |
| Receipts | Accepted Flora/shared receipt homes | Require classes; do not select unresolved topology |
| Proof | `data/proofs/flora/` | Require resolvable evidence |
| Release | `release/` | Require inputs; never approve |
| Public clients | Governed APIs/released artifacts | No direct spec/internal-store access |

[Back to top](#top)

## Current evidence and maturity

| Surface | Inspected status | Not established |
|---|---|---|
| Parent README | Draft v0.1 before revision | Active behavior |
| Five YAML files | Seven-line `PROPOSED` placeholders | IDs, schema, source refs, consumers, gates, activation |
| `watchers/README.md` | Grounded v0.2 documentation | Active watcher profiles/execution |
| Pipeline-spec schema/parser/registry | UNKNOWN | Accepted shape, loader, precedence, scheduler |
| Executable Flora pipeline | Draft documentation | Runtime and consumer binding |
| Flora config | README-only | Loader/deployment binding |
| Source registry | Draft with topology conflict | Canonical active descriptors |
| Contracts/schemas | Scaffold parent; several semantic contracts; one permissive schema scaffold | Complete accepted machine enforcement |
| Policy/sensitivity | Scaffold binding lanes; conflicted human docs | Runtime enforcement |
| Tests/fixtures | README-backed coverage and synthetic lanes | Spec-specific executable tests/consumer alignment |
| Receipts | Domain and pipeline READMEs | Canonical topology and emitted receipts |
| Proof/release | Draft proof and candidate lanes | Runtime closure/promotion |
| CI/CODEOWNERS | TODO workflow and placeholder ownership | Substantive enforcement |
| Runtime/public use | UNKNOWN | Production consumption or publication |

**Current status:** five placeholders and one grounded child README exist; no active top-level Flora specification is established.

[Back to top](#top)

## Repository fit and inventory

```text
pipeline_specs/flora/
├── README.md
├── gbif_ingest.yaml
├── inaturalist_ingest.yaml
├── usfws_ecos_ingest.yaml
├── flora_publish_dryrun.yaml
├── plants_drift_watcher.yaml
└── watchers/
    └── README.md
```

| File | Safe classification | Critical missing elements |
|---|---|---|
| `gbif_ingest.yaml` | Inventory placeholder | Origin-publisher preservation, source refs, rights, parser, consumer, lifecycle, tests |
| `inaturalist_ingest.yaml` | Inventory placeholder | Source-role limits, geoprivacy, terms, source refs, consumer, tests |
| `usfws_ecos_ingest.yaml` | Inventory placeholder | Status-versus-occurrence boundary, source refs, rights, consumer, tests |
| `flora_publish_dryrun.yaml` | Inventory placeholder | Candidate input, proof, policy, review, release, correction, rollback |
| `plants_drift_watcher.yaml` | Inventory placeholder | Canonical placement, baseline, checks, consumer, outcomes, receipts |
| `watchers/README.md` | Documentation boundary | Profiles, schema, parser, scheduler, activation |

All five YAML files contain only `status`, `source_doc`, `path`, and a placeholder note.

### Visible placement conflicts

- Plants drift appears under both `pipeline_specs/flora/` and shared `pipeline_specs/watchers/`.
- Candidate watcher execution appears under both `pipelines/domains/flora/watchers/` and `pipelines/watchers/plants/`.
- Source registry evidence includes both subtype-first and domain-first paths.
- Receipt evidence includes both `data/receipts/flora/` and `data/receipts/pipeline/flora/`.

Resolve these through an accepted ADR, migration/delegation note, or drift entry with rollback—not by copying authority.

[Back to top](#top)

## Minimum active specification contract

| Area | Minimum requirement |
|---|---|
| Identity | Stable ID, domain/lane, immutable version/digest, owner/reviewers, timestamps |
| Schema/status | Accepted schema/version; finite status separate from activation |
| Binding | Parser, consumer, compatibility tests, discovery/precedence, duplicate handling |
| Activation | Separate record with digest, environment, approvers, effective time, rollback |
| Sources | Admitted descriptor refs; origin publisher and aggregator roles preserved |
| Rights/culture | License, terms, attribution, redistribution, cultural authority, stewardship |
| Taxonomy | Authority/version, identifier namespace, synonym/crosswalk/unresolved behavior |
| Objects | Accepted contracts/schemas and explicit knowledge character |
| Time/space | Material time facets, stale/correction behavior, support, precision, uncertainty |
| Lifecycle | Allowed input/output states and hold/quarantine behavior |
| Sensitivity | Policy/profile refs, public-safe requirements, reconstruction checks, deny behavior |
| Evidence | `EvidenceRef` resolving to `EvidenceBundle` |
| Validation | Validators, fixtures, no-network replay, finite outcomes/reason codes |
| Receipts/review | Required run/transform/validation/redaction/review/policy records |
| Release | Candidate-only unless separate release workflow closes all gates |
| Correction/security | Derivative invalidation; no secrets, private endpoints, or restricted logs |
| Rollback | Known-good digest/baseline, deactivation, affected-surface inventory |

### Proposed statuses

```text
STUB
PROPOSED
REVIEW_REQUIRED
VALIDATED
APPROVED_INACTIVE
ACTIVE
SUSPENDED
SUPERSEDED
RETIRED
REJECTED
```

### Proposed outcomes

```text
PASS
NO_OP
HOLD
QUARANTINE
NEEDS_REVIEW
ABSTAIN
DENY
RETRY
SOURCE_STALE
RIGHTS_UNRESOLVED
CULTURAL_AUTHORITY_UNRESOLVED
TAXONOMY_UNRESOLVED
SENSITIVITY_UNRESOLVED
EVIDENCE_MISSING
VALIDATION_FAILED
ERROR
```

A validated spec may still be inactive. Do not convert blocked state into empty success.

[Back to top](#top)

## Illustrative inactive YAML

> [!WARNING]
> Incomplete, non-canonical, inactive, and unsafe for production.

```yaml
schema_version: kfm.pipeline_spec.flora.example.v0
spec_id: flora.example.inactive
version: 0.0.0-example
status: PROPOSED
active: false
owner: OWNER_TBD

binding:
  parser_ref: null
  consumer_ref: null
  activation_record_ref: null

sources:
  source_descriptor_refs: []
  origin_roles_required: true
  rights_review_required: true
  cultural_authority_review_required: true

objects:
  input_contract_refs: []
  output_contract_refs: []
  knowledge_character: candidate

lifecycle:
  allowed_input_states: [WORK, QUARANTINE]
  candidate_output_states: [WORK, QUARANTINE]
  may_publish: false

gates:
  taxonomy_required: true
  sensitivity_required: true
  evidence_bundle_required: true
  review_record_required: true
  correction_path_required: true
  rollback_target_required: true

validation:
  no_network: true
  fixture_refs: []
  accepted_outcomes: [PASS, HOLD, QUARANTINE, ABSTAIN, DENY, ERROR]
```

[Back to top](#top)

## Sources, rights, cultural authority, and admission

A spec may reference an admitted source; it cannot admit one.

- **GBIF/aggregators:** preserve origin publisher, dataset, license, basis of record, uncertainty, geoprivacy, and role.
- **iNaturalist/community science:** preserve quality, obscuration, observer privacy, taxonomic confidence, licensing, and origin.
- **USFWS ECOS/status:** status supports status claims, not current presence or exact locality.
- **Herbarium/specimen portals:** collection evidence has collection time and locality constraints; it does not prove present-day occurrence.
- **Steward/tribal/landowner records:** cultural authority and rights may override technical accessibility.
- **Remote sensing/vegetation products:** classified or modeled context is not direct occurrence.

Before activation, verify source identity, origin/distributor roles, rights/terms, sensitivity/cultural authority, cadence/version/correction, connector handling outside the spec, and explicit activation/deactivation records.

[Back to top](#top)

## Object family and knowledge-character boundaries

| Family | Required distinction | Prohibited collapse |
|---|---|---|
| Plant taxon/crosswalk | Authority, concept, version, confidence | Name/crosswalk equals settled identity |
| Specimen | Collected evidence with event/time/locality | Specimen equals current occurrence |
| Flora occurrence | Method, time, evidence, uncertainty | Report equals verified occurrence |
| Rare plant record | Restricted/sensitive context | Restricted equals public |
| Vegetation community | Classification and spatial support | Polygon equals species occurrence |
| Invasive plant record | Occurrence/status/management context | Management equals unbiased distribution |
| Phenology | Stage, method, observation time | Stage equals general occurrence |
| Range/distribution | Extent/model lineage | Range/model equals observation |
| Botanical survey | Effort, targets, detections/non-detections | Non-detection equals absence |
| Restoration planting | Planted material, source, project | Planting equals wild occurrence |
| Status record | Authority, jurisdiction, effective dates | Status equals occurrence |
| Public-safe derivative | Protective transform plus receipts | Derivative replaces restricted canonical record |

Taxonomy reconciliation is interpretive. Retain original determinations and correction lineage; invalidate affected caches, maps, exports, indexes, embeddings, and generated summaries when accepted interpretation changes.

[Back to top](#top)

## Sensitivity, geoprivacy, cultural rights, and reconstruction risk

Fail closed for rare/protected/medicinal/ceremonial/culturally significant plants; exact or reconstructable localities; herbarium locality text; restoration and seed-source sites; private identities; small counts/cells; precise times; risky joins; culturally restricted knowledge; and protected payloads.

A spec may reference an approved transform profile. It must not embed operational radii, grid sizes, seeds, offsets, suppression thresholds, credentials, private endpoints, or restricted examples.

Public-safe eligibility requires appropriate evidence, rights/cultural review, sensitivity policy, deterministic transform receipt, review, validation, release manifest, correction path, and rollback. Logs, errors, issues, notifications, metrics, traces, caches, search/vector indexes, embeddings, and generated summaries are exposure surfaces too.

[Back to top](#top)

## Lifecycle, evidence, and release

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec declares proposed transitions only. Governed implementation plus evidence, policy, review, and release authority performs them.

```text
specification != execution
execution != receipt
receipt != proof
proof != catalog
catalog != release
```

Current repository evidence documents both Flora receipt paths; neither settles final topology. Active specs must reference accepted receipt types/IDs, not infer authority from directory names.

Required failure codes should include `SPEC_INVALID`, `SPEC_INACTIVE`, `CONSUMER_UNBOUND`, `SOURCE_NOT_ADMITTED`, `SOURCE_ROLE_UNRESOLVED`, `RIGHTS_UNRESOLVED`, `CULTURAL_AUTHORITY_UNRESOLVED`, `TAXONOMY_UNRESOLVED`, `SENSITIVITY_UNRESOLVED`, `EVIDENCE_MISSING`, `REVIEW_MISSING`, `POLICY_DENIED`, `RELEASE_BLOCKED`, and `ROLLBACK_TARGET_MISSING`.

[Back to top](#top)

## Validation, review, and activation

### Required checks

- schema, unique ID, immutable version/digest, finite status/outcome;
- parser/consumer compatibility and discovery/precedence;
- separate activation record;
- admitted sources with origin roles;
- rights, terms, attribution, cultural authority, sensitivity;
- accepted object contracts/schemas and explicit knowledge character;
- time, spatial support, precision, uncertainty, lifecycle legality;
- no secrets, private endpoints, restricted payloads, or exposure parameters;
- evidence, receipt, review, policy, correction, and rollback refs;
- unknown fields/versions fail closed.

### Required deterministic scenarios

| Scenario | Expected result |
|---|---|
| Placeholder submitted for activation | `SPEC_INVALID` |
| Parser/consumer missing | `CONSUMER_UNBOUND` |
| Source not admitted | `SOURCE_NOT_ADMITTED` |
| Aggregator origin missing | Hold/quarantine |
| Specimen presented as current occurrence | Contract failure |
| Status presented as occurrence | Contract failure |
| Rights/cultural authority unresolved | Block |
| Exact rare-plant geometry targets public output | `DENY` |
| Evidence/review/policy/receipt missing | Block |
| Dry-run attempts release | `RELEASE_BLOCKED` |
| Default test calls network | Fail |
| Correction changes taxonomy/sensitivity | Invalidate and hold affected derivatives |
| Rollback target missing | `ROLLBACK_TARGET_MISSING` |

Current enforcement remains bounded: domain tests and fixtures document intent, indexed search found no spec-specific test/fixture implementation beyond v0.1 references, and `domain-flora` runs only three `echo TODO` jobs.

Activation review should include the spec steward, consumer owner, Flora steward, taxonomy/herbarium reviewer, source/rights reviewer, cultural/stewardship reviewer, sensitivity reviewer, temporal reviewer, validation/evidence reviewer, and policy/release reviewer.

[Back to top](#top)

## Rollback, correction, and deactivation

For a future active profile:

1. suspend discovery and scheduling;
2. preserve exact spec/digest, activation, parser/consumer, baseline, and run lineage;
3. stop new runs and hold candidates;
4. restore a reviewed prior profile/baseline or remain disabled;
5. re-evaluate source roles, rights, terms, cultural authority, taxonomy, sensitivity, and freshness;
6. inventory processed records, catalogs, triplets, releases, maps, tiles, exports, APIs, caches, indexes, embeddings, notifications, and summaries;
7. issue correction, withdrawal, supersession, review, policy, and rollback records;
8. restrict unsafe derivatives first;
9. rerun deterministic validation;
10. record final disposition.

A first active profile is not done until schema, binding, source admission, rights/cultural authority, taxonomy/object contracts, sensitivity, evidence, receipts, tests, CI, CODEOWNERS, correction, deactivation, and rollback are all enforceable and human-reviewed.

[Back to top](#top)

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-FLORA-001` | Accepted schema/version? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-002` | Parser, registry, discovery, precedence, scheduler? | UNKNOWN |
| `PIPE-SPEC-FLORA-003` | Supported executable consumers? | UNKNOWN |
| `PIPE-SPEC-FLORA-004` | Activation record authority? | UNKNOWN |
| `PIPE-SPEC-FLORA-005` | Complete, migrate, consolidate, or retire each placeholder? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-006` | Canonical plants-drift declarative/executable placement? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-FLORA-007` | Canonical source-registry topology? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-FLORA-008` | Canonical receipt topology and vocabulary? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-FLORA-009` | Active admitted sources, roles, rights, terms, cultural authority? | UNKNOWN |
| `PIPE-SPEC-FLORA-010` | Binding taxonomy authorities/crosswalks? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-011` | Accepted object contracts/schemas? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-012` | Binding time/freshness vocabularies? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-013` | Enforced sensitivity tiers/transforms? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-014` | Required cultural/stewardship review artifacts? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-015` | Binding receipt/proof/policy/release schemas? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-016` | Spec-specific fixture/test home and consumers? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-017` | Substantive validators, CI, CODEOWNERS? | UNKNOWN |
| `PIPE-SPEC-FLORA-018` | Correction/invalidation propagation? | NEEDS VERIFICATION |
| `PIPE-SPEC-FLORA-019` | Rollback drills? | UNKNOWN |
| `PIPE-SPEC-FLORA-020` | Any deployed runtime/public use? | UNKNOWN |

[Back to top](#top)

## Evidence ledger

| Evidence | Status used |
|---|---|
| Parent README | Prior v0.1 target/blob |
| Five Flora YAML files | Seven-line `PROPOSED` placeholders |
| Flora watcher README | Grounded child documentation |
| Shared plants-drift placeholder | Duplicate planning concern |
| Flora pipeline/watcher READMEs | Draft behavior boundaries; runtime unverified |
| Flora config/source registry | README-only config and registry topology conflict |
| Contracts/schema index | Semantic candidates plus permissive schema scaffold |
| Policy/sensitivity docs | Scaffold binding lanes and human-doc conflict |
| Domain tests/fixtures | Intended coverage; consumer alignment incomplete |
| Both Flora receipt READMEs | Process-memory boundaries; unresolved layout |
| Flora proof/release candidate READMEs | Evidence-first and candidate-not-release posture |
| Flora workflow/CODEOWNERS | TODO-only CI and placeholder ownership |
| Directory Rules | Responsibility-root separation and anti-duplication |

v0.2 preserves v0.1's valid principles—declarative versus executable separation, lifecycle integrity, evidence/policy/review/release gates, rare/culturally sensitive fail-closed behavior, no-network validation, correction, and rollback—while replacing the unsupported proposed tree with verified inventory and explicit unknowns.

## Maintainer rule

Keep this directory declarative. Do not place executable code, clients, credentials, private endpoints, payloads, schemas, contracts, policy decisions, lifecycle outputs, emitted receipts, proofs, release decisions, exact sensitive locations, culturally restricted knowledge, public UI/API code, or generated authoritative summaries here.

[Back to top](#top)
