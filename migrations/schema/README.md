<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-schema-readme
title: migrations/schema/ — Governed Schema, Contract-Shape, Compatibility, and Adoption Transitions
type: README; per-directory-readme; nested-migration-lane; schema-change-control
version: v1.1
status: draft; repository-grounded; documented-lane; configured-validation-surface-confirmed; concrete-migration-payloads-unestablished; adoption-ledger-unestablished; compatibility-retirement-unverified; recovery-pairing-unverified; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable schema, contract, migration, validator, producer, consumer, data, graph, policy, security, and release stewardship assignments were not established
created: 2026-07-03
updated: 2026-07-24
supersedes: v1 documentation at the same path; no schema, contract, validator, fixture, producer, consumer, migration payload, lifecycle state, runtime behavior, release state, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; migrations; schema-compatibility; contract-shape; adoption-aware; rollback-aware; evidence-first; fail-closed; non-publisher
current_path: migrations/schema/README.md
owning_root: migrations/
responsibility: govern schema and contract-shape transition mechanics, compatibility classification, producer and consumer adoption, validation rollout, deprecation, and recovery without becoming semantic-contract, canonical-schema, policy, lifecycle-data, runtime, release, or publication authority
truth_posture: >
  CONFIRMED same-path target; canonical migrations responsibility root; documented schema and rollback lanes; Directory Rules assignment
  of schema migrations to migrations/schema/; mandatory paired recovery posture; current CODEOWNERS routing; schemas/ as the
  machine-shape responsibility root; contracts/ as the semantic-meaning root; configured schemas/contracts/v1 validation surface;
  Draft 2020-12 and unique-$id checks; six fixture-backed validator families; schema and contract tests; proposed ADR-0001 and
  ADR-0002 status; and empty object-family and deprecation registers / PROPOSED schema-migration classification, minimum packet,
  compatibility matrix, adoption ledger, deprecation protocol, validation evidence model, coordinated rollout, recovery, and
  definition-of-done contracts / UNKNOWN exhaustive schema inventory, concrete schema migration payloads, generated clients,
  active producer and consumer versions, target environments, applied migration history, release adoption, and production parity /
  NEEDS VERIFICATION one-to-one recovery pairing, same-PR enforcement, schema-version convention, compatibility policy,
  object-family registry population, deprecation retirement records, structured adoption receipts, steward assignments, independent
  approval, dedicated schema-migration CI, and release integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: a27d8af412a887d041268ff82cd106ccaee0d44d
  parent_readme_blob: 48da6b62000d145359bfbd7f8383961c9f285b2a
  schemas_readme_blob: 15c84131862c00584664dfafa497c012ae765d33
  contracts_readme_blob: 1561841b0bfdc64c07e8d3bf0aa6a6d5cc240a88
  schema_home_adr_blob: 3c520ea8f2f8bcb3d478329a87d98b135ea335fd
  contract_schema_split_adr_blob: 2da10fcf5836a44d46186c233b6b9664c9ccfda5
  schema_validation_workflow_blob: e6b26337aa1eea142b96560e041419f855c44d59
  object_family_register_blob: 930a9da30d5481f8d7ed5b7789d7846a30d3f4e1
  deprecation_register_blob: 1fb7219dcdb7a437e38fa8ca92ba34e29667d3fa
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  codeowners_status: repository default routing resolves this path to @bartytime4life; role-level stewardship and independent approval remain unverified
  inspection_method: exact GitHub file reads, current workflow and register inspection, bounded repository search, branch-name search, and open-PR overlap search; no recursive Git tree, generated-client pipeline, deployment environment, live producer or consumer, release artifact, runtime trace, or production payload was inspected
related:
  - ../README.md
  - ../database/README.md
  - ../data/README.md
  - ../graph/README.md
  - ../rollback/README.md
  - ../../schemas/README.md
  - ../../schemas/contracts/v1/README.md
  - ../../contracts/README.md
  - ../../policy/README.md
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../tests/schemas/README.md
  - ../../tools/validators/README.md
  - ../../release/README.md
  - ../../control_plane/object_family_register.yaml
  - ../../control_plane/deprecation_register.yaml
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/runbooks/README.md
  - ../../docs/governance/SEPARATION_OF_DUTIES.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/CODEOWNERS
notes:
  - "v1.1 is a same-path documentation-only modernization grounded in current repository evidence."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "The configured v1 validation surface is confirmed, but concrete schema migration payloads, an adoption ledger, complete compatibility retirement, generated-client rollout, and verified recovery coverage were not established."
  - "ADR-0001 and ADR-0002 remain proposed; this README records current configuration without converting either proposal into accepted authority."
  - "Static badges summarize inspected repository state only; they are not migration approval, adoption, compatibility, release, or publication proof."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/schema/` — Governed Schema, Contract-Shape, Compatibility, and Adoption Transitions

> **One-line purpose.** Govern deliberate transitions in KFM machine shape and contract-backed payload compatibility so producers, consumers, validators, fixtures, data, graph projections, public interfaces, and recovery plans remain coordinated without turning migration records into schema, semantic, policy, or release authority.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lane: schema migration](https://img.shields.io/badge/lane-schema%20migration-1f6feb?style=flat-square)](#authority-level)
[![Configured surface: v1](https://img.shields.io/badge/configured%20surface-schemas%2Fcontracts%2Fv1-2da44e?style=flat-square)](#status)
[![ADRs: proposed](https://img.shields.io/badge/schema%20ADRs-proposed-d4a72c?style=flat-square)](#adrs)
[![Adoption ledger: not established](https://img.shields.io/badge/adoption%20ledger-not%20established-b42318?style=flat-square)](#producer-and-consumer-adoption)
[![Recovery pairing: needs verification](https://img.shields.io/badge/recovery%20pairing-needs%20verification-d4a72c?style=flat-square)](#recovery-and-forward-fix)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** `migrations/schema/` is a documented migration lane beneath the canonical `migrations/` responsibility root. The repository confirms a configured `schemas/contracts/v1/` validation surface and bounded schema/contract checks, but current inspection does **not** establish concrete schema-migration payloads, a complete object-family registry, an adoption ledger, generated-client rollout, compatibility retirement, complete recovery pairing, or production producer/consumer parity.

> [!CAUTION]
> A schema diff, passing meta-schema check, green test, generated type, branch, pull request, or merged commit does not prove that producers and consumers adopted a compatible contract. Adoption requires pinned old and new definitions, affected-system inventory, fixture and validator evidence, producer and consumer rollout evidence, deprecation state, post-adoption checks, and recovery posture.

> [!WARNING]
> This directory is not a parallel schema home, contract home, policy root, fixture root, generated-code store, lifecycle-data store, release lane, or publication surface. Canonical schemas remain under their governed schema root; semantic meaning remains under `contracts/`; migration records coordinate change but do not redefine either authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Classes](#schema-migration-classification) · [Packet](#minimum-schema-migration-packet) · [Compatibility](#compatibility-and-semantic-change-matrix) · [Adoption](#producer-and-consumer-adoption) · [Validation rollout](#validation-fixtures-and-generated-clients) · [Deprecation](#deprecation-aliases-and-retirement) · [Coordination](#coordinated-migrations) · [Recovery](#recovery-and-forward-fix) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

<a id="status--authority"></a>
<a id="repo-fit"></a>
<a id="schema-migration-contract"></a>
<a id="required-migration-record"></a>
<a id="compatibility-classes"></a>
<a id="open-verification"></a>

## Purpose

`migrations/schema/` owns the **change mechanics, compatibility analysis, adoption plan, and review packet** for transitions that alter KFM machine shape or contract-backed payload compatibility.

Typical work includes:

- adding, renaming, splitting, merging, moving, deprecating, or removing fields;
- changing requiredness, nullability, types, formats, bounds, enums, references, or composition;
- introducing a new schema version or compatibility envelope;
- migrating `$id`, `$ref`, object-family identity, or version-routing behavior;
- changing validator behavior that affects accepted or rejected instances;
- coordinating producer, consumer, fixture, test, generated-client, data, graph, API, UI, and release adoption;
- retiring legacy or compatibility schema paths without creating parallel authority;
- documenting rollback or forward-fix posture for incompatible adoption.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A schema migration can support governed lifecycle processing and release. It does not promote data, approve policy, prove evidence closure, certify a release, or publish a payload.

A schema migration must answer:

1. Which semantic contract and machine schema are changing?
2. Which exact versions or digests define the old and new states?
3. What compatibility class applies?
4. Which producers emit the shape?
5. Which consumers read, validate, store, project, render, or export it?
6. Which fixtures, tests, validators, clients, and registries must change?
7. Which rollout order preserves compatibility?
8. Which deprecation and removal conditions apply?
9. Which evidence proves adoption?
10. How can the transition be reversed, disabled, or forward-fixed?

[Back to top](#top)

---

## Authority level

**Nested migration lane for schema and contract-shape transitions; subordinate to the roots that define meaning, machine shape, admissibility, evidence, lifecycle state, runtime behavior, and release.**

| Concern | Controlling authority | Role of `migrations/schema/` |
|---|---|---|
| Human-readable object meaning and field intent | [`contracts/`](../../contracts/README.md) | Preserves and coordinates semantic changes; does not define meaning independently. |
| Machine-checkable shape | [`schemas/`](../../schemas/README.md), currently configured through `schemas/contracts/v1/` | Plans and records transitions; canonical schema files remain in the schema root. |
| Schema-home decision | Directory Rules plus accepted ADRs | Records current configured behavior while ADR-0001 and ADR-0002 remain proposed. |
| Policy, rights, sensitivity, access, release rules | [`policy/`](../../policy/README.md) | Identifies policy impact; cannot approve or weaken policy. |
| Examples and boundary cases | [`fixtures/`](../../fixtures/README.md) | Requires representative migration fixtures; does not own fixture authority. |
| Executable proof | [`tests/`](../../tests/README.md) | Requires relevant tests and observed results; does not own test implementation. |
| Reusable validation | [`tools/validators/`](../../tools/validators/README.md) | Coordinates validator rollout; does not own validator code. |
| Database structure | [`migrations/database/`](../database/README.md) | References paired DDL when persistence shape changes. |
| Data state | [`migrations/data/`](../data/README.md) | References backfill, repair, remap, or rebuild work. |
| Graph/triplet state | [`migrations/graph/`](../graph/README.md) | References topology, identity, or projection changes. |
| Migration recovery | [`migrations/rollback/`](../rollback/README.md) | Requires a paired recovery entry. |
| Application/runtime adoption | Governed `apps/`, `packages/`, `runtime/`, and pipeline roots | Names affected producers and consumers; does not claim deployment. |
| Release, correction, withdrawal, public rollback | [`release/`](../../release/README.md) | Identifies release impact; cannot approve or execute release state. |

### Authority anti-collapse rules

This lane must never treat:

- schema validity as semantic correctness;
- a contract edit as machine-shape adoption;
- a generated client as proof of deployment;
- an additive field as automatically compatible;
- an optional field as semantically optional;
- a default value as policy approval;
- a fixture as evidence of production behavior;
- a passing validator as evidence closure or truth;
- a migration plan as an applied migration;
- a compatibility alias as a second canonical schema;
- a merged PR as producer/consumer adoption;
- a migration receipt as release approval.

[Back to top](#top)

---

## Status

| Surface | Current evidence | Status |
|---|---|---|
| `migrations/schema/README.md` | Present at the same path; this revision modernizes documentation | **CONFIRMED** |
| Parent `migrations/` lane | Present and documents database, schema, data, graph, and rollback lanes | **CONFIRMED — documentation** |
| Canonical machine-shape root | `schemas/` documented as machine-shape authority | **CONFIRMED — repository guidance** |
| Configured v1 validation surface | `schemas/contracts/v1/` is checked by `schema-validation` | **CONFIRMED — configured behavior** |
| Semantic contract root | `contracts/` documented as semantic-meaning authority | **CONFIRMED — repository guidance** |
| JSON Schema dialect check | Canonical v1 schemas must declare Draft 2020-12 | **CONFIRMED — workflow definition** |
| Canonical `$id` checks | v1 schemas require nonempty, unique `$id` values | **CONFIRMED — workflow definition** |
| Configured validator families | Six aggregate fixture-backed families are required | **CONFIRMED — bounded coverage** |
| Schema/contract tests | Workflow runs `tests/schemas` and `tests/contracts` | **CONFIRMED — command-bearing definition** |
| Structured validation report or adoption receipt | Workflow emits process output and job summary only | **NOT ESTABLISHED** |
| ADR-0001 | Present with status `proposed` | **CONFIRMED — not accepted** |
| ADR-0002 | Present with source status `draft` and effective decision `proposed` | **CONFIRMED — not accepted** |
| Concrete payloads under `migrations/schema/` | Not found in bounded repository search beyond this README | **UNKNOWN / NEEDS VERIFICATION** |
| Complete object-family crosswalk | `control_plane/object_family_register.yaml` contains `entries: []` | **NOT ESTABLISHED** |
| Deprecation retirement inventory | `control_plane/deprecation_register.yaml` contains `entries: []` | **NOT ESTABLISHED** |
| Producer and consumer adoption ledger | Not established in bounded inspection | **UNKNOWN** |
| Generated-client or DTO regeneration pipeline | Not established in bounded inspection | **UNKNOWN** |
| Complete schema inventory and compatibility classification | Not recursively established in this update | **UNKNOWN** |
| One-to-one recovery pairing | Required by doctrine; coverage not recursively verified | **NEEDS VERIFICATION** |
| Same-PR migration enforcement | Not established | **NEEDS VERIFICATION** |
| Ownership and independent approval | CODEOWNERS routing confirmed; stewardship and rules unverified | **NEEDS VERIFICATION** |
| Production producer/consumer parity | No live environment inspected | **UNKNOWN** |
| Release or publication authority | Not owned by this lane | **DENIED by boundary** |

### Current maturity statement

This lane is **documentation-heavy, validation-aware, and adoption-unverified**.

Current configuration proves that selected machine-shape checks exist. It does not establish:

- complete schema-family coverage;
- accepted schema-home governance;
- semantic parity between contracts and schemas;
- all producer and consumer versions;
- compatibility across all applications and artifacts;
- generated-client parity;
- completed deprecation or alias retirement;
- production adoption;
- release readiness.

[Back to top](#top)

---

## What belongs here

Use `migrations/schema/` when the **primary responsibility is coordinating a machine-shape or contract-backed compatibility transition**.

Accepted material includes:

- schema-version transition plans;
- compatibility classifications and matrices;
- old-to-new field and enum crosswalks;
- producer and consumer inventories;
- validator, fixture, test, and generated-client rollout plans;
- deprecation, warning, alias, sunset, and removal plans;
- schema-home consolidation plans;
- `$id`, `$ref`, namespace, or version-routing transition plans;
- compatibility-lane classification and retirement records;
- adoption sequencing across apps, packages, pipelines, data, graph, API, UI, exports, and release artifacts;
- dry-run and validation summaries that do not contain sensitive payloads;
- sanitized adoption receipts;
- migration manifests binding old and new schema digests, contracts, validation, dependencies, and recovery;
- forward-fix records when direct rollback is unsafe.

A schema migration record may reference canonical schemas, contracts, policies, fixtures, validators, tests, applications, data, graphs, and releases. It must not duplicate those artifacts as parallel authority.

[Back to top](#top)

---

## What does NOT belong here

Do not use this directory as a second home for schemas, contracts, policy, fixtures, generated clients, runtime payloads, or release decisions.

The following do not belong here:

- canonical JSON Schema, JSON-LD context, or other machine-shape files;
- human-readable semantic contracts as the primary authority;
- executable policy bundles or policy decisions;
- valid, invalid, edge, golden, denied, abstaining, stale, correction, or rollback fixtures;
- reusable validator implementations or test modules;
- generated SDKs, clients, DTOs, bindings, compiled models, or build artifacts;
- database DDL, primary data backfills, or primary graph rewrites;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads;
- schema registries or deprecation registers that belong under the accepted control-plane path;
- release manifests, promotion decisions, rollback cards, correction notices, or withdrawal records;
- secrets, credentials, tokens, private endpoints, DSNs, service-account material, or production configuration;
- unredacted restricted payload samples;
- breaking changes without compatibility, adoption, validation, and recovery analysis;
- aliases or copies that can evolve independently from the controlling schema;
- AI-generated migration mappings promoted without deterministic validation and review.

When an artifact is misplaced, stop and move it through the correct governed path. When a duplicate authority surface is discovered, classify it before editing: canonical candidate, generated mirror, compatibility adapter, frozen legacy, deprecated alias, or unresolved conflict.

[Back to top](#top)

---

## Inputs

A schema migration packet consumes **references and pinned evidence**, not uncontrolled copies.

| Input | Minimum requirement | Owning authority |
|---|---|---|
| Migration identity | Stable migration ID or deterministic name | `migrations/schema/` |
| Old schema state | Path, `$id`, version, commit, and digest | `schemas/` |
| New schema state | Path, `$id`, version, commit, and digest | `schemas/` |
| Semantic contract | Contract path, version, and changed meaning summary | `contracts/` |
| Change rationale | Issue, ADR, defect, drift, policy need, evidence requirement, or consumer mismatch | Applicable authority |
| Compatibility classification | Explicit class and rationale | Migration record |
| Producer inventory | Emitters and versions in scope | Application/package/runtime owners |
| Consumer inventory | Readers, validators, stores, projections, clients, and versions | Consumer owners |
| Fixture matrix | Valid, invalid, edge, old-version, new-version, and cross-version cases | `fixtures/` |
| Validator/test inventory | Named checks and expected outcomes | `tools/validators/`, `tests/` |
| Policy/sensitivity review | Impact on rights, sensitivity, source role, evidence, release, or access | `policy/` and review records |
| Dependency plan | Database, data, graph, app, pipeline, API, UI, export, and release order | Coordinated migration packet |
| Recovery entry | Paired rollback, disablement, restore, or forward-fix record | `migrations/rollback/` |
| Base-state evidence | Current producer/consumer compatibility and known drift | Receipts, reports, tests, inventories |
| Approval evidence | Required review records; CODEOWNERS routing alone is insufficient | Governance controls |

### Input admission rules

Reject or hold the migration packet when:

- the old or new schema cannot be pinned;
- semantic meaning is changed without a contract update or explicit no-semantic-change rationale;
- affected producers or consumers are unknown;
- compatibility is asserted without testable cases;
- required policy or sensitivity fields are weakened without review;
- removal is proposed without deprecation evidence;
- a compatibility path can diverge from its controlling schema;
- recovery posture is absent;
- the target path conflicts with Directory Rules or an accepted ADR;
- the packet relies on generated prose instead of deterministic evidence.

[Back to top](#top)

---

## Outputs

This lane may produce governance and migration-control records such as:

- a schema migration plan;
- compatibility matrix;
- producer/consumer adoption matrix;
- old/new field or enum crosswalk;
- schema-home or path migration map;
- validator, fixture, and test rollout checklist;
- deprecation and retirement plan;
- sanitized dry-run or diff summary;
- coordinated migration sequence;
- adoption status record;
- residual-risk statement;
- paired recovery reference;
- post-adoption verification summary;
- supersession record for an obsolete migration plan.

Outputs from this lane are **not** automatically:

- canonical schemas;
- semantic contracts;
- policy decisions;
- validation receipts with governed authority;
- production deployments;
- release manifests;
- public artifacts;
- publication approval.

A migration output must state its evidence level:

| Evidence level | Meaning |
|---|---|
| `DOCUMENTED` | Plan or matrix exists; no execution is implied. |
| `STATIC_VALIDATED` | Definitions, references, fixtures, or scripts passed named static checks. |
| `TESTED` | Named executable tests ran against pinned inputs. |
| `ADOPTED_BY_COMPONENT` | A named producer or consumer version has evidence of adoption. |
| `COEXISTENCE_VERIFIED` | Old and new versions operated together under the defined compatibility window. |
| `RETIREMENT_VERIFIED` | Old path or version is no longer required by the verified inventory. |
| `PRODUCTION_VERIFIED` | Observed production evidence exists for the named scope; this level was not established in this update. |

[Back to top](#top)

---

## Validation

Validation is layered. No single layer proves the whole transition.

### Required validation layers

| Layer | Questions | Evidence |
|---|---|---|
| Placement | Does the migration belong here, and do canonical files remain in their authority roots? | Directory/PR review |
| Syntax | Are JSON, YAML, Markdown, references, and manifests parseable? | Parser output |
| Meta-schema | Do schema documents satisfy the declared dialect? | JSON Schema meta-validation |
| Identity | Are `$id`, version, path, and digest rules valid and non-conflicting? | Identity report |
| Semantic parity | Does machine shape preserve the controlling contract meaning? | Contract/schema review |
| Compatibility | Do old/new producers and consumers behave as classified? | Compatibility tests |
| Fixture polarity | Do valid and invalid cases produce expected outcomes? | Fixture validation |
| Validator parity | Do reusable validators use the intended schema and preserve fail-closed behavior? | Validator tests |
| Producer adoption | Can named producers emit the new shape correctly? | Producer test or receipt |
| Consumer adoption | Can named consumers read and handle old/new shapes as planned? | Consumer test or receipt |
| Cross-version operation | Does the transition window work without ambiguity or silent loss? | Coexistence tests |
| Data compatibility | Are stored or lifecycle payloads valid or explicitly migrated? | Data validation |
| Graph compatibility | Are triplets, identities, references, and projections preserved? | Graph validation |
| Policy/sensitivity | Are rights, sensitivity, evidence, source-role, and release obligations preserved? | Policy/review evidence |
| Recovery | Can the old safe state be restored or forward-fixed? | Paired recovery evidence |
| Release impact | Are public API, UI, MapLibre, exports, caches, and artifacts handled? | Release review |
| Post-adoption | Are drift, warnings, deprecated usage, and residual risk measured? | Verification summary |

### Current configured validation boundary

The inspected `schema-validation` workflow currently:

1. parses every JSON file under `schemas/`;
2. meta-validates every `*.schema.json`;
3. requires canonical v1 schemas to declare Draft 2020-12;
4. requires nonempty, unique `$id` values in the v1 tree;
5. requires six configured validators with nonempty valid and invalid fixture lanes;
6. runs the aggregate schema validators;
7. runs `tests/schemas` and `tests/contracts`;
8. emits process output and a job summary, not a structured validation report, receipt, proof, policy decision, or release decision.

That is useful bounded proof. It is not a complete schema-migration adoption gate.

### Minimum validation result vocabulary

| Result | Meaning |
|---|---|
| `PASS` | Named checks passed for the pinned scope. |
| `FAIL` | One or more required checks failed. |
| `HOLD` | Evidence, review, inventory, or dependency is incomplete. |
| `NOT_APPLICABLE` | A layer does not apply and a reviewed rationale is recorded. |
| `UNKNOWN` | The check was not run or evidence cannot be resolved. |

A schema migration must not report overall `PASS` while a required layer is `UNKNOWN`.

[Back to top](#top)

---

## Review burden

CODEOWNERS routing is not stewardship, approval, or proof of review. Required roles below are **review functions** until concrete assignments and enforcement are verified.

| Change class | Minimum review functions |
|---|---|
| README-only guidance with no behavioral change | Documentation review and migration-lane review |
| Additive optional field with no semantic change | Schema review plus affected producer and consumer review |
| Required field or stricter validation | Schema, contract, producer, consumer, validator, and migration review |
| Semantic reinterpretation without shape change | Contract, schema, policy as applicable, producer, consumer, and migration review |
| Field rename, split, merge, move, or type change | Contract, schema, producer, consumer, data/graph as applicable, and migration review |
| Enum or controlled-value change | Contract, schema, policy/domain as applicable, producer, consumer, and migration review |
| `$id`, `$ref`, namespace, or schema-home transition | Architecture, schema, validator, producer/consumer, and migration review |
| Deprecation or alias introduction | Schema, contract, producer/consumer, registry, and migration review |
| Removal or compatibility retirement | Schema, contract, all verified producer/consumer owners, recovery, and release review as applicable |
| Generated-client or DTO regeneration | Schema, generator/tooling, application, compatibility, and migration review |
| Migration paired with database change | Schema, database, application, and migration review |
| Migration paired with data backfill or repair | Schema, data, application, and migration review |
| Migration paired with graph/triplet change | Schema, graph, application, and migration review |
| Public API, UI, MapLibre, export, or published artifact impact | Governed API, consumer, release, schema, and migration review |
| Rights, sensitivity, living-person, DNA, archaeology, rare-species, infrastructure, or sovereignty impact | Policy/sensitivity, relevant domain, schema, contract, and release review as applicable |
| Forward-fix-only transition | Migration, schema, affected consumers, recovery review, and documented risk acceptance |

### Separation expectations

Where materiality, sensitivity, destructive removal, public impact, or forward-fix-only posture applies:

- the author should not be the sole approver;
- compatibility classification should be independently reviewed;
- execution evidence should be reviewed separately from the implementation claim;
- release approval remains outside this lane.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../`](../README.md) | Canonical migration root and cross-lane contract |
| [`../database/`](../database/README.md) | Database structure changes paired with schema adoption |
| [`../data/`](../data/README.md) | Backfills, repairs, remaps, and stored-payload transitions |
| [`../graph/`](../graph/README.md) | Graph/triplet identity, relationship, and projection transitions |
| [`../rollback/`](../rollback/README.md) | Required recovery posture for every schema migration |
| [`../../schemas/`](../../schemas/README.md) | Machine-shape authority |
| [`../../schemas/contracts/v1/`](../../schemas/contracts/v1/README.md) | Current configured v1 validation surface |
| [`../../contracts/`](../../contracts/README.md) | Semantic meaning and compatibility promises |
| [`../../policy/`](../../policy/README.md) | Admissibility, rights, sensitivity, access, and release rules |
| [`../../fixtures/`](../../fixtures/README.md) | Representative old/new and valid/invalid examples |
| [`../../tests/`](../../tests/README.md) | Executable compatibility and negative-path proof |
| [`../../tools/validators/`](../../tools/validators/README.md) | Reusable validation implementation |
| [`../../control_plane/object_family_register.yaml`](../../control_plane/object_family_register.yaml) | Proposed object-family crosswalk; currently empty |
| [`../../control_plane/deprecation_register.yaml`](../../control_plane/deprecation_register.yaml) | Proposed deprecation inventory; currently empty |
| [`../../release/`](../../release/README.md) | Release, correction, withdrawal, and public rollback authority |
| [`../../docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Recorded authority, compatibility, and implementation drift |
| [`../../.github/workflows/schema-validation.yml`](../../.github/workflows/schema-validation.yml) | Current configured bounded schema-validation workflow |

### Directory Rules basis

`migrations/schema/` is valid because its responsibility is **change control for machine-shape compatibility**, not canonical schema storage. New schema artifacts remain under the schema responsibility root; semantic contract updates remain under `contracts/`; migration records remain here; recovery records remain under `migrations/rollback/`.

[Back to top](#top)

---

## ADRs

| ADR or decision surface | Current status | Relevance |
|---|---|---|
| [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | `proposed` | Proposes `schemas/contracts/v1/` as the default canonical contract-backed schema home. |
| [`ADR-0002`](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | Source metadata `draft`; effective decision `proposed` | Proposes the contracts/schemas/policy/fixtures/tests/validators responsibility split. |
| Directory Rules | Governing doctrine | Assigns migration lanes and prohibits parallel authority. |
| Future schema-versioning ADR | **PROPOSED / not found** | Needed if version identity, support windows, or major/minor compatibility rules become binding. |
| Future generated-client ADR | **PROPOSED / not found** | Needed if generated SDK or DTO rollout becomes repository-wide authority. |

### ADR posture

This README does not accept ADR-0001 or ADR-0002.

Until acceptance:

- current configured behavior may be described as **CONFIRMED implementation evidence**;
- canonical architectural decisions remain **PROPOSED**;
- compatibility paths must not silently evolve;
- migration plans must remain reversible and evidence-bearing;
- conflicts must be recorded rather than normalized away.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review status | Repository-grounded v1.1 documentation modernization |
| Evidence boundary | GitHub repository files and workflow definitions; no live runtime, producer, consumer, deployment, or release environment inspected |
| Next review trigger | First concrete schema migration payload; accepted schema-home ADR; populated object-family or deprecation register; generated-client rollout; breaking schema change; compatibility retirement; public payload change; or recovery-linked migration PR |

[Back to top](#top)

---

## Current bounded topology

```text
migrations/
├── README.md
├── database/
│   └── README.md
├── schema/
│   └── README.md       ◀── this lane
├── data/
│   └── README.md
├── graph/
│   └── README.md
└── rollback/
    └── README.md
```

The bounded search found this README as the only concrete path directly under `migrations/schema/`. That does not prove the directory is recursively empty under every ref or unindexed path; it means no additional payload was established strongly enough to describe as current implementation.

### Responsibility flow

```text
contracts/ semantic change
          │
          ▼
schemas/ machine-shape change
          │
          ▼
migrations/schema/ compatibility + adoption plan
          │
          ├── fixtures + tests + validators
          ├── producers + consumers
          ├── database/data/graph coordination
          └── migrations/rollback/ recovery posture
```

[Back to top](#top)

---

## Schema migration classification

Every migration must select one primary class and any applicable secondary classes.

| Class | Meaning | Default posture |
|---|---|---|
| `ADDITIVE_OPTIONAL` | Adds an optional field or compatible object branch | Validate semantic optionality, unknown-field behavior, defaults, and consumers |
| `ADDITIVE_REQUIRED_WITH_DEFAULT` | Adds a required field supplied through a deterministic default or transformation | Treat as potentially breaking until all producers, stored instances, and consumers are proven compatible |
| `CONSTRAINT_TIGHTENING` | Narrows type, range, format, enum, cardinality, pattern, or requiredness | Breaking unless evidence proves no affected instance or consumer |
| `CONSTRAINT_RELAXATION` | Broadens accepted shape | Review semantic, evidence, policy, and downstream ambiguity risks |
| `FIELD_RENAME` | Replaces one field name with another | Require coexistence or crosswalk, warnings, adoption evidence, and retirement trigger |
| `FIELD_SPLIT_OR_MERGE` | Changes one field into many or many into one | Require deterministic mapping, loss analysis, and data/graph coordination |
| `TYPE_OR_FORMAT_CHANGE` | Changes primitive, object, array, geometry, timestamp, URI, identifier, or encoding shape | Require old/new compatibility tests and stored-data analysis |
| `ENUM_OR_VOCABULARY_CHANGE` | Adds, removes, renames, merges, or changes controlled values | Pair with semantic contract and policy/domain review |
| `REFERENCE_CHANGE` | Changes `$id`, `$ref`, namespace, URI, version routing, or external reference behavior | Require resolver, registry, caching, and consumer analysis |
| `SEMANTIC_CHANGE_SAME_SHAPE` | Meaning or interpretation changes without machine-shape change | Contract migration; schema record still required when validators or consumers change |
| `VALIDATION_BEHAVIOR_CHANGE` | Validator accepts or rejects different instances without canonical schema movement | Require validator version and fixture polarity evidence |
| `VERSION_INTRODUCTION` | Adds a new version family while preserving an older version | Define coexistence, translation, default routing, and retirement |
| `COMPATIBILITY_ALIAS` | Adds a transitional path or wrapper | Freeze authority, prevent divergence, and define sunset |
| `HOME_OR_PATH_MIGRATION` | Moves schema authority from a legacy or compatibility path | Requires identity preservation, mirrors/adapters, drift control, and rollback |
| `DEPRECATION` | Marks an old field, value, version, or path for retirement | Require warnings, inventory, replacement, deadline or trigger, and recovery |
| `REMOVAL` | Removes an old field, value, version, path, or compatibility surface | Require verified zero-use or approved break, recovery, and release analysis |
| `DOC_ONLY` | Changes migration guidance without machine or semantic behavior | Verify no schema, contract, validator, fixture, producer, or consumer behavior changed |
| `COORDINATED` | Schema transition is inseparable from database, data, graph, policy, app, or release work | Use one umbrella sequence and per-lane records |
| `FORWARD_FIX_ONLY` | Direct reversal would be unsafe or invalid | Explain why; pair with explicit corrective migration and risk acceptance |

### Compatibility is not inferred from filename or syntax

Examples of unsafe assumptions:

- “optional” does not mean every consumer tolerates the field;
- “additive” does not mean strict consumers ignore unknown properties;
- “defaulted” does not mean old stored objects can be reconstructed safely;
- “enum addition” may break exhaustive switches;
- “constraint relaxation” may admit semantically invalid or policy-sensitive instances;
- “same JSON shape” may hide a breaking semantic change;
- “generated client compiles” does not prove old/new runtime interoperability.

[Back to top](#top)

---

## Minimum schema migration packet

The following YAML is a **PROPOSED record contract**, not a confirmed implemented schema.

```yaml
migration:
  id: KFM-SCHEMA-MIG-YYYYMMDD-NNN
  title: short-purpose
  status: PROPOSED
  evidence_level: DOCUMENTED
  primary_class: ADDITIVE_OPTIONAL
  secondary_classes: []
  issue_refs: []
  adr_refs: []
  drift_refs: []

authority:
  semantic_contracts:
    - path: contracts/<family>/<object>.md
      version: "<pinned>"
      digest: "<sha256>"
  old_schemas:
    - path: schemas/<controlled-path>.schema.json
      schema_id: "<$id>"
      version: "<old>"
      commit: "<sha>"
      digest: "<sha256>"
  new_schemas:
    - path: schemas/<controlled-path>.schema.json
      schema_id: "<$id>"
      version: "<new>"
      commit: "<sha>"
      digest: "<sha256>"
  canonical_status: CONFIRMED_CONFIGURED | PROPOSED | ACCEPTED | COMPATIBILITY
  no_parallel_authority_attestation: "<review reference>"

change:
  semantic_change: true
  semantic_summary: "<what meaning changes or explicit none>"
  shape_summary: "<what machine shape changes>"
  compatibility_claim: "<bounded claim>"
  incompatibilities: []
  information_loss_risks: []
  policy_or_sensitivity_impacts: []
  evidence_or_source_role_impacts: []
  temporal_or_spatial_impacts: []

crosswalk:
  field_mappings: []
  enum_mappings: []
  default_rules: []
  rejected_or_quarantined_cases: []
  unmappable_cases: []
  mapping_digest: "<sha256 or N/A>"

adoption:
  producers: []
  consumers: []
  validators: []
  fixtures: []
  tests: []
  generated_clients: []
  stored_data: []
  graph_projections: []
  APIs_and_UIs: []
  exports_and_releases: []
  rollout_order: []
  coexistence_window: "<defined or N/A>"
  removal_trigger: "<evidence-based trigger or N/A>"

validation:
  static_checks: []
  compatibility_tests: []
  negative_tests: []
  old_producer_new_consumer_tests: []
  new_producer_old_consumer_tests: []
  stored_payload_checks: []
  policy_checks: []
  post_adoption_checks: []
  expected_result: PASS

recovery:
  record: migrations/rollback/<matching-record>.md
  posture: REVERSIBLE | PARTIAL | DISABLE | RESTORE | FORWARD_FIX_ONLY | BLOCKED
  old_safe_state: "<pinned state>"
  irreversible_effects: []
  residual_risks: []

review:
  author: "<identity>"
  schema_review: "<record>"
  contract_review: "<record>"
  producer_reviews: []
  consumer_reviews: []
  policy_or_sensitivity_review: "<record or N/A>"
  recovery_review: "<record>"
  release_review: "<record or N/A>"

receipts:
  static_validation: []
  test_runs: []
  adoption_evidence: []
  coexistence_evidence: []
  retirement_evidence: []
  post_adoption_verification: []
```

### Record requirements

A packet is incomplete when it omits:

- old and new pinned states;
- a compatibility class;
- producer and consumer inventories;
- a contract parity statement;
- validation and negative-path evidence;
- a rollout order;
- a deprecation/removal trigger when applicable;
- a paired recovery record;
- unresolved risks.

[Back to top](#top)

---

## Compatibility and semantic-change matrix

Compatibility has multiple dimensions. A migration may pass one and fail another.

| Dimension | Question | Example failure |
|---|---|---|
| Syntactic | Can the payload parse? | Malformed JSON or unresolved reference |
| Meta-schema | Is the schema itself valid? | Invalid Draft 2020-12 keyword use |
| Structural | Does an instance match required shape? | Missing required field |
| Producer | Can old/new producers emit the expected shape? | Producer omits new required value |
| Consumer | Can old/new consumers safely read the shape? | Strict parser rejects unknown field |
| Semantic | Does the instance mean the same thing? | Field keeps type but changes interpretation |
| Evidence | Are evidence links and support obligations preserved? | EvidenceRef becomes optional without review |
| Source role | Are primary, corroborating, context, and restricted roles preserved? | Context source silently treated as primary |
| Policy | Do rights, sensitivity, access, and release rules still evaluate correctly? | New enum bypasses a deny rule |
| Temporal | Are valid time, observed time, publication time, and update time preserved? | Timestamp field is collapsed or reinterpreted |
| Spatial | Are CRS, geometry, precision, generalization, and location sensitivity preserved? | Geometry field changes without CRS migration |
| Identity | Are object, schema, source, claim, release, and relationship identities stable or mapped? | ID is regenerated without lineage |
| Stored data | Can existing instances remain valid or be deterministically migrated? | Old records become invalid without backfill |
| Graph | Do triplets and projections retain valid references and meaning? | Relationship endpoint field is renamed without graph migration |
| API/UI | Do governed interfaces preserve bounded behavior? | UI treats absent new field as approval |
| Release | Can released artifacts coexist, be corrected, or be withdrawn safely? | Public payload changes before consumer adoption |
| Recovery | Can the prior safe state be restored or compensated? | New producer emits irreversible shape with no old-reader path |

### Compatibility claim template

A strong claim is bounded:

> `CONFIRMED` for producer versions A–B and consumer versions C–D against fixtures E and tests F at commit G. `UNKNOWN` for other producers, consumers, stored payloads, and production environments.

Avoid claims such as:

- “fully backward compatible” without an inventory;
- “non-breaking” based only on JSON Schema comparison;
- “all clients updated” without adoption evidence;
- “safe to remove” without verified zero-use or approved breakage.

[Back to top](#top)

---

## Producer and consumer adoption

A schema migration closes only when applicable participants have evidence-bearing outcomes.

### Adoption matrix

| Participant | Required fields |
|---|---|
| Producer | Component, version, emitted object family, old/new capability, rollout state, evidence |
| Consumer | Component, version, accepted versions, unknown-field behavior, fallback behavior, evidence |
| Validator | Validator path/version, controlling schema digest, fail-closed behavior, evidence |
| Fixture set | Old/new/cross-version cases and expected polarity |
| Generated client | Generator version, schema digest, language/runtime, compatibility evidence |
| Stored data | Inventory, migration need, invalid/quarantined counts, evidence |
| Graph projection | Source schema, mapping version, rebuild or compatibility state |
| API/UI/export | Payload version, routing behavior, fallback, public-impact state |
| Release | Candidate or release IDs affected, hold/correction/rollback requirements |

### Adoption states

| State | Meaning |
|---|---|
| `NOT_IN_SCOPE` | Reviewed and explicitly not applicable |
| `IDENTIFIED` | Participant is known but not tested |
| `READY` | Change is implemented and locally validated |
| `DUAL_READ` | Consumer reads both versions |
| `DUAL_WRITE` | Producer emits both versions under governed rules |
| `MIGRATED` | Participant uses the new version |
| `VERIFIED` | Observed evidence confirms the named scope |
| `DEPRECATED_USE` | Participant still depends on the old version |
| `BLOCKED` | Adoption cannot proceed |
| `FAILED` | Attempted adoption failed |
| `RETIRED` | Old dependency is removed with evidence |
| `UNKNOWN` | State is not established |

### Adoption closure rule

Do not close a migration merely because the schema PR merged.

Closure requires:

1. all in-scope participants are inventoried;
2. required compatibility tests pass;
3. old/new coexistence works where required;
4. adoption evidence resolves;
5. deprecated dependencies are tracked;
6. removal conditions are met or the old surface remains supported;
7. recovery posture remains valid;
8. residual risk is recorded.

[Back to top](#top)

---

## Validation, fixtures, and generated clients

### Fixture requirements

A material schema migration should include applicable cases for:

- old valid payload;
- old invalid payload;
- new valid payload;
- new invalid payload;
- old producer to new consumer;
- new producer to old consumer;
- omitted optional field;
- explicit null where allowed or denied;
- unknown field behavior;
- deprecated field warning;
- conflicting old and new fields;
- crosswalk success;
- unmappable or quarantined case;
- policy-denied or sensitivity-restricted case;
- evidence-resolution failure;
- rollback or forward-fix case.

### Validator requirements

Validators must:

- resolve the intended pinned schema;
- fail closed when required authority or references are missing;
- distinguish expected-invalid fixtures from runner failure;
- avoid embedding policy decisions unless policy evaluation is explicitly part of the validator contract;
- emit enough evidence to reproduce the result;
- avoid mutating canonical schemas or lifecycle data during validation.

### Generated-client posture

Generated SDKs, DTOs, and bindings are **UNKNOWN** in the bounded repository inspection.

When introduced, a generated-client migration must pin:

- schema digest;
- generator name and version;
- generation configuration;
- language/runtime version;
- output package identity;
- manual patch policy;
- compatibility tests;
- publication or distribution state;
- rollback or regeneration procedure.

Generated code must not become an independent schema authority.

[Back to top](#top)

---

## Deprecation, aliases, and retirement

Deprecation is a governed transition, not a comment or warning alone.

### Deprecation record

Every deprecation should identify:

- deprecated field, value, version, path, or object family;
- replacement;
- semantic differences;
- first deprecated version/date;
- affected producers and consumers;
- warning mechanism;
- compatibility adapter or crosswalk;
- sunset date **or** evidence-based removal trigger;
- owner/review functions;
- recovery posture;
- current usage evidence;
- retirement verification.

### Alias and mirror rules

A compatibility alias or mirror must be:

- subordinate to one controlling schema;
- generated or mechanically synchronized where practical;
- blocked from independent field evolution;
- covered by drift detection;
- labeled with replacement and sunset posture;
- excluded from new canonical authoring;
- removable through a migration with rollback or forward fix.

### Current register state

The inspected proposed registers are empty:

```text
control_plane/object_family_register.yaml  -> entries: []
control_plane/deprecation_register.yaml    -> entries: []
```

Therefore, repository-wide object-family coverage and deprecation closure are **not established**.

### Retirement gate

Do not remove a deprecated surface until:

- the controlling authority is clear;
- the verified inventory shows no unapproved dependency;
- all required migrations are complete;
- compatibility adapters are no longer required;
- tests and validators reject unintended legacy use;
- public and release impact is resolved;
- recovery is reviewed;
- the retirement record is preserved.

[Back to top](#top)

---

## Coordinated migrations

Schema transitions frequently cross responsibility roots. Keep the per-lane records separate but sequence them through one umbrella plan.

### Common coordination patterns

| Pattern | Typical order |
|---|---|
| Additive field backed by database storage | Database expansion → schema addition → producer write → consumer read → data validation |
| Required field with backfill | Schema permits transition → database/data backfill → producer adoption → constraint tightening → old path retirement |
| Field rename | New field added → dual read/write or crosswalk → consumers migrate → producers migrate → deprecated field removal |
| Enum replacement | Contract/value mapping → schema accepts both → policy and consumers update → data/graph remap → old value removal |
| Identifier change | Contract and identity decision → schema/version update → data and graph remap → API/client adoption → alias retirement |
| Schema-home move | Classify old/new authority → establish controlling path → update validators/resolvers → freeze mirror → verify consumers → retire old path |
| Breaking API envelope | New version introduced → governed API dual support → clients migrate → release review → old version withdrawal |
| Sensitivity-field change | Contract/policy review → schema transition → validators/fixtures → data/graph/API adoption → release review |
| Forward-fix-only change | New corrective schema/migration → coordinated adoption → residual old state handling → recovery and incident/release handoff |

### Coordination rules

- one umbrella plan may reference many lane records;
- each lane retains its authority and recovery posture;
- dependency order must be explicit;
- no step may silently publish or promote data;
- normal public clients continue through governed interfaces;
- intermediate states must fail safely;
- rollback order must be defined, not assumed to be the reverse of rollout.

[Back to top](#top)

---

## Recovery and forward fix

Every schema migration requires a corresponding entry under `migrations/rollback/`, including documentation-only or not-applicable cases with a reason.

Recovery may involve:

- reverting the schema definition before adoption;
- disabling new producer output;
- restoring old version routing;
- re-enabling a compatibility adapter;
- rolling back generated clients;
- restoring prior database/data/graph state;
- quarantining incompatible payloads;
- compensating with a new schema and crosswalk;
- forward-fixing when direct reversal would corrupt meaning or data.

### Recovery questions

1. Which exact old schema and contract state is safe?
2. Which producers may already emit the new shape?
3. Which consumers may already depend on it?
4. Which stored, graph, cached, exported, or released instances exist?
5. Which effects are irreversible?
6. Which aliases or adapters must be restored?
7. Which validation proves recovery?
8. Which release, correction, withdrawal, or incident actions are separate and still required?

### Forward-fix-only rule

`FORWARD_FIX_ONLY` is not a convenience label.

It requires:

- explicit reason direct rollback is unsafe;
- named corrective migration;
- affected-system inventory;
- containment plan;
- validation and recovery evidence;
- documented residual risk;
- independent review appropriate to materiality.

[Back to top](#top)

---

## Definition of done

A schema migration is complete only when all applicable items are closed.

### Authority and identity

- [ ] Old and new semantic contracts are pinned.
- [ ] Old and new schemas are pinned by path, `$id`, version, commit, and digest.
- [ ] Canonical and compatibility paths are classified.
- [ ] No parallel authority can evolve independently.
- [ ] ADR status is represented accurately.

### Compatibility and adoption

- [ ] Primary and secondary migration classes are recorded.
- [ ] Producer and consumer inventories are complete for the claimed scope.
- [ ] Compatibility tests cover old/new directions as applicable.
- [ ] Stored data and graph impacts are resolved.
- [ ] API, UI, export, and release impacts are resolved.
- [ ] Generated clients are updated or explicitly not applicable.
- [ ] Adoption evidence resolves for every required participant.

### Validation and policy

- [ ] Schema and references parse.
- [ ] Meta-schema and identity checks pass.
- [ ] Fixtures cover positive, negative, edge, and cross-version cases.
- [ ] Validators and tests pass for pinned inputs.
- [ ] Semantic parity is reviewed.
- [ ] Evidence, source-role, temporal, spatial, rights, sensitivity, and policy obligations are preserved.
- [ ] Unknown or not-applicable layers are explicit.

### Deprecation and recovery

- [ ] Deprecation and removal triggers are documented.
- [ ] Remaining old-version dependencies are visible.
- [ ] Paired recovery entry exists.
- [ ] Recovery or forward-fix posture is reviewed.
- [ ] Residual risk is recorded.
- [ ] Post-adoption verification is complete.
- [ ] Superseded migration records remain auditable.

A merged PR is not the definition of done.

[Back to top](#top)

---

## Open verification register

| ID | Verification item | Current label | Closure evidence |
|---|---|---|---|
| `SCHEMA-MIG-OV-001` | Confirm exhaustive contents of `migrations/schema/` | NEEDS VERIFICATION | Recursive tree inventory |
| `SCHEMA-MIG-OV-002` | Confirm required same-PR pairing with `migrations/rollback/` | NEEDS VERIFICATION | Ruleset, validator, or accepted workflow |
| `SCHEMA-MIG-OV-003` | Confirm schema versioning and support-window convention | NEEDS VERIFICATION | Accepted ADR and tests |
| `SCHEMA-MIG-OV-004` | Confirm compatibility policy for additive, deprecating, and breaking changes | NEEDS VERIFICATION | Accepted contract/ADR |
| `SCHEMA-MIG-OV-005` | Populate authoritative object-family crosswalk | OPEN / PROPOSED | Reviewed nonempty register |
| `SCHEMA-MIG-OV-006` | Populate deprecation and retirement inventory | OPEN / PROPOSED | Reviewed nonempty register |
| `SCHEMA-MIG-OV-007` | Confirm structured migration/adoption receipt home and schema | NEEDS VERIFICATION | Contract, schema, example, validator |
| `SCHEMA-MIG-OV-008` | Confirm generated-client or DTO regeneration process | UNKNOWN | Tooling, workflow, tests, package evidence |
| `SCHEMA-MIG-OV-009` | Confirm complete producer and consumer inventory | UNKNOWN | Generated or reviewed inventory |
| `SCHEMA-MIG-OV-010` | Confirm compatibility-path drift detection | NEEDS VERIFICATION | Validator and failing fixture |
| `SCHEMA-MIG-OV-011` | Confirm complete recovery pairing coverage | NEEDS VERIFICATION | Coverage report |
| `SCHEMA-MIG-OV-012` | Confirm required review and separation-of-duties enforcement | NEEDS VERIFICATION | Branch rules, review records, assignments |
| `SCHEMA-MIG-OV-013` | Confirm release-review triggers for public payload changes | NEEDS VERIFICATION | Release contract and gate evidence |
| `SCHEMA-MIG-OV-014` | Confirm production producer/consumer parity | UNKNOWN | Observed runtime and deployment evidence |
| `SCHEMA-MIG-OV-015` | Resolve ADR-0001 and ADR-0002 acceptance state | OPEN | Reviewed accepted, rejected, or superseded decisions |

### No-loss ledger

| Strong baseline element | Preservation in v1.1 |
|---|---|
| Lifecycle law | Preserved and bounded |
| Schema/contract responsibility split | Preserved and expanded |
| Database/data/graph/rollback lane split | Preserved |
| Compatibility classes | Preserved and expanded |
| Producer and consumer review | Preserved and expanded into adoption states |
| Crosswalk requirement | Preserved with loss and quarantine handling |
| Fixture and validator checks | Preserved and tied to current workflow evidence |
| Deprecation path | Preserved and expanded into retirement gates |
| Policy and sensitivity preservation | Preserved and expanded |
| Rollback/forward-fix rule | Preserved and expanded |
| Legacy anchors | Preserved |
| Open verification list | Preserved as a structured register |

[Back to top](#top)

---

## Changelog

### v1.1 — 2026-07-24

- Modernized the README in place.
- Reordered the first twelve H2 sections to the Directory Rules contract.
- Replaced placeholder owners with evidence-bounded routing and stewardship labels.
- Distinguished configured schema validation from complete migration adoption.
- Recorded ADR-0001 and ADR-0002 as proposed rather than accepted.
- Added migration classes, minimum packet, compatibility dimensions, adoption states, fixture/client guidance, deprecation gates, coordination, recovery, definition of done, and open verification.
- Preserved legacy anchors and strong v1 content.
- Changed documentation only.

### v1 — 2026-07-03

- Established the initial schema migration lane guidance.

[Back to top](#top)
