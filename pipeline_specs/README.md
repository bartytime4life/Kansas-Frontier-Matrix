<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-readme
title: pipeline_specs/ — Governed Declarative Pipeline Specification Root
type: readme; directory-readme; declarative-pipeline-spec-root; compatibility-and-activation-boundary
version: v0.3
status: draft; repository-grounded; placeholder-heavy; mixed-lane-maturity; no-active-root-spec-system-established
owners:
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Pipeline owner
  - OWNER_TBD — Domain stewards
  - OWNER_TBD — Source and rights steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Validation and CI steward
  - OWNER_TBD — Evidence and receipt steward
  - OWNER_TBD — Policy and sensitivity steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Security reviewer
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-18
supersedes: v0.2
policy_label: public-doc; pipeline-specs; declarative-only; no-secrets; no-live-activation; no-direct-fetch; no-direct-admission; no-direct-lifecycle-write; no-direct-release; source-role-aware; rights-aware; sensitivity-aware; evidence-bound; policy-gated; review-gated; correction-aware; rollback-aware
current_path: pipeline_specs/README.md
truth_posture: CONFIRMED target README, pipeline_specs responsibility root, pipelines executable companion root, pipelines/specs compatibility guardrail, bounded seventeen direct child README lanes, representative empty-stage YAML scaffolds, representative short PROPOSED documentation-inventory placeholders, README-only compatibility aliases, checked absence of root AGENTS.md and pipeline_specs/AGENTS.md, checked absence of tests/pipeline_specs/README.md and fixtures/pipeline_specs/README.md, repository-grounded tests/pipelines boundary, current CODEOWNERS routing, and no open PR targeting this README / PROPOSED accepted pipeline-spec schema, deterministic canonicalization and hashing, parser and consumer registry, activation states, source binding, lifecycle grammar, finite outcomes, reason-code vocabulary, no-network fixture contract, spec-to-implementation agreement tests, receipt bindings, deactivation, correction propagation, and rollback / CONFLICTED air versus atmosphere, people versus people-dna-land, settlement versus settlements-infrastructure, shared versus domain watcher placement, direct domain lanes versus historical pipeline_specs/domains references, child README inventories versus current path evidence, and pipeline_specs versus pipelines/specs compatibility semantics / UNKNOWN exhaustive recursive inventory, accepted active specifications, parser discovery, consumers, scheduler, source activation, runtime execution, emitted pipeline receipts, substantive spec CI, promotion dependency, branch protection, production use, and public effects / NEEDS VERIFICATION named owners, accepted Directory Rules copy, schema and ID vocabulary, alias and migration decisions, child-lane inventory freshness, source-registry topology, rights and sensitivity policy, fixtures and tests, workflow path filters, correction behavior, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 527ac01444c23046f0406dbb9e4cf5b2a74cd4cc
  target_prior_blob: 3a6599898606126604298a281de53e39fdba98ce
  bounded_direct_child_readmes:
    - pipeline_specs/agriculture/README.md
    - pipeline_specs/air/README.md
    - pipeline_specs/archaeology/README.md
    - pipeline_specs/atmosphere/README.md
    - pipeline_specs/fauna/README.md
    - pipeline_specs/flora/README.md
    - pipeline_specs/geology/README.md
    - pipeline_specs/habitat/README.md
    - pipeline_specs/hazards/README.md
    - pipeline_specs/hydrology/README.md
    - pipeline_specs/people-dna-land/README.md
    - pipeline_specs/people/README.md
    - pipeline_specs/roads-rail-trade/README.md
    - pipeline_specs/settlement/README.md
    - pipeline_specs/settlements-infrastructure/README.md
    - pipeline_specs/soil/README.md
    - pipeline_specs/watchers/README.md
  bounded_nested_readmes:
    - pipeline_specs/fauna/watchers/README.md
    - pipeline_specs/flora/watchers/README.md
    - pipeline_specs/habitat/ecoregions/README.md
    - pipeline_specs/habitat/land_cover/README.md
    - pipeline_specs/people-dna-land/land-ownership/README.md
  checked_absent_paths:
    - AGENTS.md
    - pipeline_specs/AGENTS.md
    - tests/pipeline_specs/README.md
    - fixtures/pipeline_specs/README.md
  inventory_method: GitHub connector exact file reads plus bounded code-index queries; counts and absence claims are not full-history or all-branch assertions
related:
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../docs/architecture/directory-rules.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../pipelines/README.md
  - ../pipelines/specs/README.md
  - ../tests/pipelines/README.md
  - agriculture/README.md
  - air/README.md
  - archaeology/README.md
  - atmosphere/README.md
  - fauna/README.md
  - flora/README.md
  - geology/README.md
  - habitat/README.md
  - hazards/README.md
  - hydrology/README.md
  - people-dna-land/README.md
  - people/README.md
  - roads-rail-trade/README.md
  - settlement/README.md
  - settlements-infrastructure/README.md
  - soil/README.md
  - watchers/README.md
  - ../data/registry/sources/
  - ../data/receipts/generated/README.md
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../.github/workflows/README.md
  - ../.github/CODEOWNERS
  - ../.github/PULL_REQUEST_TEMPLATE.md
notes:
  - "v0.3 replaces the planning-oriented root tree with a commit-pinned maturity and routing boundary."
  - "Current YAML payloads are placeholder-heavy: representative files are either empty-stage scaffolds or short PROPOSED inventory placeholders derived from documentation."
  - "A child README, YAML parse, merge, schedule string, workflow conclusion, or source reference activates nothing without an accepted schema, parser, consumer, source decision, fixtures, tests, and review state."
  - "This documentation-only revision changes no YAML payload, parser, pipeline, connector, source activation, schema, contract, policy, fixture, test, workflow, lifecycle record, receipt instance beyond generated provenance, release object, runtime behavior, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipeline_specs/` — Governed Declarative Pipeline Specification Root

> Declarative control boundary for stating **what** a KFM pipeline may attempt, against which admitted sources, through which lifecycle and governance gates, with which deterministic outputs, receipts, finite failures, correction obligations, and rollback targets—without becoming executable code, source authority, lifecycle data, evidence, policy, release approval, or a public serving surface.

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow">
  <img alt="Direct child README lanes: seventeen" src="https://img.shields.io/badge/direct__README__lanes-17-informational">
  <img alt="Payload maturity: placeholder heavy" src="https://img.shields.io/badge/payload__maturity-placeholder--heavy-orange">
  <img alt="Active root spec system: not established" src="https://img.shields.io/badge/active__spec__system-not__established-critical">
  <img alt="Tests: not established" src="https://img.shields.io/badge/spec__tests-not__established-orange">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Path:** `pipeline_specs/README.md`  
**Version:** `v0.3`  
**Status:** draft / repository-grounded / placeholder-heavy / mixed lane maturity  
**Owning root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Executable companion:** [`pipelines/`](../pipelines/README.md) — executable pipeline logic, the **how**  
**Compatibility guardrail:** [`pipelines/specs/`](../pipelines/specs/README.md) — not an alternate authoritative spec root  
**Public posture:** no direct public path; public clients use governed APIs and released artifacts  
**Evidence snapshot:** `main@527ac01444c23046f0406dbb9e4cf5b2a74cd4cc`

> [!IMPORTANT]
> The repository contains many files under `pipeline_specs/`, but bounded inspection did not establish an accepted root schema, active parser, consumer registry, scheduler, source activation binding, dedicated spec-test suite, or substantive root CI gate. File presence is repository evidence; it is not activation or implementation proof.

> [!CAUTION]
> Two placeholder shapes currently recur:
>
> 1. small stage scaffolds containing `name`, `version: 1`, and `stages: []`;
> 2. short inventory placeholders containing `status: PROPOSED`, a path, and one or more source-document references.
>
> Neither shape is an active pipeline specification.

> [!WARNING]
> Specs, examples, logs, receipts, pull requests, and generated summaries must not contain credentials, private endpoints, restricted source payloads, exact sensitive locations, living-person or DNA data, owner-resolved private-land joins, infrastructure vulnerability detail, cultural knowledge, or other reconstructive sensitive content.

---

## Quick navigation

[Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Inventory](#bounded-root-inventory) · [Payloads](#current-payload-taxonomy) · [Lanes](#direct-lane-registry) · [Compatibility](#compatibility-alias-and-placement-conflicts) · [Minimum contract](#minimum-future-active-spec-contract) · [Sources](#source-admission-rights-and-activation) · [Lifecycle](#lifecycle-and-promotion-boundary) · [Outcomes](#finite-outcomes-and-reason-codes) · [Sensitivity](#sensitive-domain-and-public-safe-representation) · [Binding](#parser-consumer-and-runtime-binding) · [Validation](#validation-tests-fixtures-and-ci) · [Review](#review-versioning-and-change-discipline) · [Rollback](#deactivation-correction-and-rollback) · [Done](#definition-of-done-for-an-active-specification) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [History](#change-history)

---

## Purpose

`pipeline_specs/` is KFM's declarative pipeline-configuration root.

A mature specification may state:

- stable profile identity, version, state, owners, and digest;
- the exact executable consumer allowed to interpret it;
- admitted `SourceDescriptor` references and fixed source roles;
- schedule, cadence, freshness, valid-time, source-vintage, and stale-state behavior;
- allowed lifecycle input states and candidate output states;
- contract and schema references;
- domain-specific anti-collapse and cross-lane boundaries;
- evidence, policy, rights, sensitivity, review, and release prerequisites;
- deterministic no-network fixture and replay behavior;
- idempotency, retry, cancellation, quarantine, and no-op behavior;
- expected reports, receipts, hashes, and safe observability;
- correction, withdrawal, supersession, deactivation, and rollback posture;
- finite outcomes and stable reason codes.

A specification does **not** execute itself. Executable pipeline code belongs under [`pipelines/`](../pipelines/README.md), shared packages, approved tools, or another verified implementation root selected by primary responsibility.

### Audience

- pipeline-spec and pipeline maintainers;
- domain, source, rights, sensitivity, evidence, policy, validation, security, and release reviewers;
- connector and runtime owners binding admitted sources to controlled execution;
- test and CI maintainers proving spec shape and spec-to-consumer agreement;
- maintainers resolving compatibility aliases, duplicate lanes, or stale inventory.

### Non-goals

This README does not:

- declare any current YAML file active;
- define an accepted pipeline-spec schema;
- create a parser, registry, scheduler, consumer, or runtime;
- activate a source or authorize network access;
- validate source payloads or domain claims;
- create `EvidenceBundle`, catalog, triplet, release, correction, or rollback authority;
- resolve every alias or historical path by assertion;
- prove the full recursive inventory;
- publish data, maps, APIs, exports, alerts, dashboards, or generated answers.

[Back to top](#top)

---

## Authority boundary

The root owns declarative intent only.

| Concern | Owning responsibility | Relationship to `pipeline_specs/` |
|---|---|---|
| Declarative run intent | `pipeline_specs/` | Owns accepted specifications and compatibility guidance. |
| Executable pipeline behavior | [`pipelines/`](../pipelines/README.md) | Implements the **how**; must be bound explicitly. |
| Misplaced-spec guardrail | [`pipelines/specs/`](../pipelines/specs/README.md) | Compatibility path only; not parallel authority. |
| Source access | `connectors/` | Fetches or stages under approved terms; a spec cannot grant access. |
| Source identity and activation | `data/registry/sources/` or accepted source-control home | Owns source role, rights, sensitivity, cadence, and activation. |
| Semantic meaning | `contracts/` | Defines objects and invariants. |
| Machine shape | `schemas/` | Defines accepted structure. |
| Admissibility | `policy/` | Decides allow, deny, restrict, hold, or abstain behavior. |
| Enforceability | `tests/` and `fixtures/` | Proves bounded behavior with deterministic cases. |
| Lifecycle records | `data/raw|work|quarantine|processed|catalog|triplets|published/` | Stores governed records; never beside a spec. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Records process memory and evidence closure. |
| Release, correction, rollback | `release/` | Owns public-state decisions. |
| Public delivery | governed applications and released artifacts | Must not read specs as public truth. |

Short rule:

```text
pipeline_specs/  = WHAT may run and under which gates
pipelines/       = HOW governed execution occurs
connectors/      = HOW an approved source is accessed or staged
data/registry/   = WHICH source is admitted, in which role, under which rights
contracts/       = WHAT objects mean
schemas/         = WHAT accepted objects look like
policy/          = WHETHER use or exposure is allowed
tests/fixtures/  = WHETHER bounded behavior is enforceable
data/            = WHERE lifecycle records, receipts, proofs, catalogs, and artifacts live
release/         = WHETHER public state changes
```

> [!IMPORTANT]
> A specification may require a gate. Naming the gate does not satisfy it.

[Back to top](#top)

---

## Confirmed current state

The following conclusions are bounded to the evidence snapshot.

### Safe conclusions

- **CONFIRMED:** `pipeline_specs/README.md` exists and defines a declarative root.
- **CONFIRMED:** [`pipelines/README.md`](../pipelines/README.md) defines the executable companion root.
- **CONFIRMED:** [`pipelines/specs/README.md`](../pipelines/specs/README.md) is a compatibility guardrail, not an alternate spec root.
- **CONFIRMED:** bounded code-index search surfaced seventeen direct child README lanes and five nested README sublanes.
- **CONFIRMED:** representative YAML files use empty-stage scaffold or short documentation-inventory placeholder shapes.
- **CONFIRMED:** `air/`, `people/`, and `settlement/` are documented compatibility paths rather than proven active parallel authorities.
- **CONFIRMED:** checked `tests/pipeline_specs/README.md` and `fixtures/pipeline_specs/README.md` paths are absent.
- **CONFIRMED:** [`tests/pipelines/README.md`](../tests/pipelines/README.md) records the direct shared pipeline-test lane as README-only and no dedicated pipeline suite as established.
- **CONFIRMED:** bounded search did not surface a file named or identified as a canonical pipeline-spec schema.
- **CONFIRMED:** bounded search for `source_descriptor_refs:` found README/documentation examples rather than active YAML bindings.
- **CONFIRMED:** `.github/CODEOWNERS` routes `/pipeline_specs/` to `@bartytime4life`; this is review routing, not proof of steward approval.
- **UNKNOWN:** exhaustive inventory, accepted active specs, parser, consumers, scheduler, runtime use, receipt emission, promotion dependency, branch protection, and production effects.

### Maturity matrix

| Capability | Current status | Evidence-bounded interpretation |
|---|---:|---|
| Root README | `CONFIRMED` | Declarative responsibility boundary exists. |
| Child README lanes | `CONFIRMED: 17 bounded direct lanes` | Path/document presence; not active-spec proof. |
| Nested README lanes | `CONFIRMED: 5 bounded sublanes` | Specialized boundaries; not exhaustive inventory. |
| YAML payloads | `MIXED / PLACEHOLDER-HEAVY` | Empty-stage scaffolds and short inventory placeholders are common. |
| Canonical root schema | `NOT ESTABLISHED` | No accepted schema surfaced. |
| Canonicalization and digest | `NOT ESTABLISHED` | No accepted normalization/hash contract surfaced. |
| Parser and registry | `UNKNOWN` | No verified discovery mechanism established. |
| Consumer binding | `UNKNOWN` | File paths/names do not prove executable binding. |
| Source activation binding | `NOT ESTABLISHED` | Representative YAML lacks governed source refs. |
| Root fixture suite | `NOT FOUND AT CHECKED PATH` | No `fixtures/pipeline_specs/README.md`. |
| Root spec test suite | `NOT FOUND AT CHECKED PATH` | No `tests/pipeline_specs/README.md`. |
| Shared pipeline tests | `README-ONLY / DISTRIBUTED COVERAGE` | Some negative guards exist elsewhere; no dedicated suite established. |
| Dedicated root CI | `NOT ESTABLISHED` | No substantive root gate verified. |
| Active-spec inventory | `NOT ESTABLISHED` | No accepted activation registry inspected. |
| Production/runtime use | `UNKNOWN` | No deployment or run evidence inspected. |
| Publication authority | `DENIED` | Specs cannot publish. |

[Back to top](#top)

---

## Bounded root inventory

The direct README lanes surfaced by bounded search are:

```text
pipeline_specs/
├── README.md
├── agriculture/
├── air/                         # compatibility guardrail
├── archaeology/
├── atmosphere/                  # preferred Atmosphere/Air lane
├── fauna/
├── flora/
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── people-dna-land/             # governing People/Genealogy/DNA/Land lane
├── people/                      # compatibility alias
├── roads-rail-trade/
├── settlement/                  # compatibility alias
├── settlements-infrastructure/  # governing settlement/infrastructure lane
├── soil/
└── watchers/                    # shared watcher intent; placement-sensitive
```

Bounded nested README lanes:

```text
pipeline_specs/fauna/watchers/
pipeline_specs/flora/watchers/
pipeline_specs/habitat/ecoregions/
pipeline_specs/habitat/land_cover/
pipeline_specs/people-dna-land/land-ownership/
```

This is not a recursive manifest. Before migration, activation, or release dependence, generate a pinned recursive inventory and compare it with every affected README and registry.

### Inventory integrity rule

A child README inventory is a navigation aid, not source authority. When a README and exact path evidence disagree:

1. preserve both observations;
2. label the inconsistency `CONFLICTED` or `NEEDS VERIFICATION`;
3. regenerate the pinned tree;
4. inspect history and consumers;
5. update the README or migration record;
6. do not silently delete or activate files.

[Back to top](#top)

---

## Current payload taxonomy

### 1. Empty-stage scaffold

Representative shape:

```yaml
name: agriculture-normalize
version: 1
stages: []
```

Safe interpretation:

- a YAML path and basic name/version scaffold exist;
- no operation graph is declared;
- no source, contract, schema, policy, evidence, receipt, or release binding is present;
- no parser, consumer, schedule, runtime behavior, or activation is proven.

### 2. Documentation-inventory placeholder

Representative shape:

```yaml
status: PROPOSED
source_doc: docs/domains/example/MISSING_OR_PLANNED_FILES.md
path: pipeline_specs/example/example.yaml
notes:
  - Placeholder created from docs/domains markdown inventory.
```

Safe interpretation:

- the file preserves a documented planning reference;
- it is not an executable or complete declarative profile;
- it should not be discovered as active merely because it parses;
- promotion requires explicit conversion, schema validation, fixtures, tests, and review.

### 3. Compatibility alias or guardrail

Examples include:

- [`air/`](air/README.md) relative to [`atmosphere/`](atmosphere/README.md);
- [`people/`](people/README.md) relative to [`people-dna-land/`](people-dna-land/README.md);
- [`settlement/`](settlement/README.md) relative to [`settlements-infrastructure/`](settlements-infrastructure/README.md);
- [`pipelines/specs/`](../pipelines/specs/README.md) relative to this root.

Compatibility paths must not become second active authorities without a governed decision and migration plan.

### 4. README-only boundary

A README-only lane may be valuable governance and routing documentation. It does not prove concrete profiles, a parser, consumers, fixtures, tests, workflows, receipts, or runtime use.

### Proposed state vocabulary

Until an accepted schema defines states, use these labels as documentation guidance only:

| State | Meaning |
|---|---|
| `inventory_placeholder` | Planning pointer with no accepted operational contract. |
| `stage_scaffold` | Basic name/version/stage shell, usually with no stages. |
| `proposed` | Reviewed design candidate, not activated. |
| `candidate` | Schema-valid and fixture-tested, pending activation decision. |
| `active_internal` | Approved for bounded internal execution only. |
| `active_public_candidate` | Eligible to feed release-candidate workflows; not released. |
| `deprecated` | Still readable during migration; no new adoption. |
| `disabled` | Execution blocked pending repair, incident review, or policy decision. |
| `retired` | Historical only; new execution denied. |

No current file is upgraded to these states by this README.

[Back to top](#top)

---

## Direct lane registry

| Lane | Current bounded posture | Key governance issue |
|---|---|---|
| [`agriculture/`](agriculture/README.md) | Repository-grounded README; placeholder payloads and empty-stage scaffolds. | Aggregate versus field/operator specificity; child inventory freshness. |
| [`air/`](air/README.md) | Compatibility guardrail. | Avoid parallel authority with Atmosphere. |
| [`archaeology/`](archaeology/README.md) | Sensitive-domain declarative boundary; documentation placeholders present. | Exact location, sovereignty, cultural review, rights. |
| [`atmosphere/`](atmosphere/README.md) | Preferred Atmosphere/Air declarative lane; scaffold maturity. | Observation/model/advisory separation and life-safety limits. |
| [`fauna/`](fauna/README.md) | Sensitive-domain boundary; stage scaffolds and nested watcher README. | Rare-species geoprivacy and source-role preservation. |
| [`flora/`](flora/README.md) | Sensitive-domain boundary; stage scaffolds and duplicated plants-drift planning paths. | Rare plants, cultural/stewardship rights, watcher placement. |
| [`geology/`](geology/README.md) | Domain boundary with stage scaffolds and inventory placeholders. | Occurrence/deposit/reserve/permit/production/title distinctions. |
| [`habitat/`](habitat/README.md) | Domain boundary with nested sublanes and placeholders. | Context is not species occurrence; nested ownership. |
| [`hazards/`](hazards/README.md) | Hazard context boundary with several source-oriented placeholders. | Not emergency or official alert authority. |
| [`hydrology/`](hydrology/README.md) | Mixed stage scaffolds and source-specific placeholders. | Observation/model/regulatory-context distinctions; first-proof-lane claims require evidence. |
| [`people-dna-land/`](people-dna-land/README.md) | Governing sensitive-domain lane; five empty-stage scaffolds. | Living-person, consent/revocation, DNA, title, parcel boundaries. |
| [`people/`](people/README.md) | README-only compatibility alias. | No parallel authority or lighter governance path. |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | Domain boundary with scaffolds/placeholders. | Network identity, operational status, sensitive infrastructure, transport naming. |
| [`settlement/`](settlement/README.md) | README-only compatibility alias. | No parallel authority with Settlements/Infrastructure. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | Governing lane with five empty-stage scaffolds. | Legal status, operational status, infrastructure sensitivity. |
| [`soil/`](soil/README.md) | Repository-grounded boundary with five empty-stage scaffolds. | Static survey, grids, stations, satellite, pedon, interpretation separation. |
| [`watchers/`](watchers/README.md) | Shared placeholder-only boundary; placement-conflicted. | Shared/domain delegation and non-publisher invariant. |

### Lane admission rule

A new direct lane requires:

- a responsibility-root and domain-placement basis;
- an identified implementation consumer;
- source, rights, sensitivity, fixture, test, and receipt posture;
- no parallel canonical lane;
- a migration record if replacing or aliasing an existing lane;
- owner and reviewer assignments;
- rollback instructions.

Do not create empty directories or placeholder files merely to complete a diagram.

[Back to top](#top)

---

## Compatibility, alias, and placement conflicts

### `pipeline_specs/` versus `pipelines/specs/`

[`pipelines/specs/`](../pipelines/specs/README.md) is a compatibility guardrail. New authoritative declarative specs belong here unless an accepted ADR changes the root contract.

### `air/` versus `atmosphere/`

Current child documentation treats `air/` as compatibility-oriented and `atmosphere/` as preferred. Do not duplicate active IDs, schedules, source refs, consumers, or release semantics across both.

### `people/` versus `people-dna-land/`

`people/` is an alias boundary. The sensitive People/Genealogy/DNA/Land lane remains governed under `people-dna-land/` unless an accepted migration says otherwise.

### `settlement/` versus `settlements-infrastructure/`

`settlement/` is an alias boundary. Governing domain behavior remains under `settlements-infrastructure/` unless a reviewed migration changes it.

### Shared versus domain watchers

Shared watcher intent belongs in [`watchers/`](watchers/README.md) only when behavior is truly cross-domain. Domain source roles, rights, sensitivity, materiality, or review rules favor a domain watcher sublane. Duplicate active watcher specs are prohibited.

### Historical `pipeline_specs/domains/...` references

Some repository documentation references a nested `pipeline_specs/domains/` pattern, while checked root and exact-path evidence did not establish a parent README at that path. Treat such references as drift signals, not current canonical placement.

### Directory Rules copies

The repository retains multiple Directory Rules artifacts and an open placement question. This README follows the shared responsibility-root rule without resolving the doctrine file's own canonical location.

### Conflict handling

When a conflict appears:

1. stop automatic activation and discovery;
2. identify every duplicate ID, path, parser, consumer, source, schedule, and output;
3. preserve current files and history;
4. record drift and impact;
5. select authority through the required ADR or migration review;
6. test compatibility and rollback;
7. retire aliases only after consumers move.

[Back to top](#top)

---

## Minimum future active spec contract

No accepted root schema was established by this review. The following is a **PROPOSED requirement set**, not current executable syntax.

| Field family | Minimum obligation |
|---|---|
| Identity | Stable `spec_id`, semantic version, state, domain/lane, owners, and digest. |
| Canonicalization | Accepted normalization and content-hash algorithm. |
| Consumer | Exact parser and executable implementation identity plus version compatibility. |
| Sources | Stable SourceDescriptor refs, source roles, activation states, versions, and rights posture. |
| Support | Spatial/temporal support, scale/resolution, uncertainty, and domain knowledge character. |
| Lifecycle | Allowed input states, candidate output states, quarantine/no-op behavior, prohibited transitions. |
| Contracts and schemas | Resolvable refs without duplicate inline authority. |
| Gates | Evidence, policy, rights, sensitivity, validation, review, receipt, catalog, release, correction, rollback. |
| Execution | Dry-run default, network posture, resource bounds, side effects, idempotency, retry, cancellation. |
| Outcomes | Finite outcomes and stable reason codes. |
| Observability | Run ID, input/output digests, safe diagnostics, receipt refs, and no-sensitive-log rules. |
| Migration | Supersession, deactivation, withdrawal, correction, and rollback refs. |

### Illustrative inactive shape

```yaml
schema_version: kfm.pipeline_spec.v1-proposed
spec_id: kfm.pipeline_spec.example.placeholder
version: 0.0.0-proposed
state: inventory_placeholder
lane: example

consumer:
  parser_ref: NEEDS_VERIFICATION
  implementation_ref: NEEDS_VERIFICATION
  accepted_versions: []

sources:
  source_descriptor_refs: []
  activation_required: true

lifecycle:
  allowed_inputs: []
  candidate_outputs: []
  prohibited_outputs:
    - PUBLISHED

gates:
  contract_schema_required: true
  evidence_required: true
  policy_required: true
  review_required: true
  receipts_required: true
  release_manifest_required: true
  rollback_target_required: true

execution:
  dry_run_default: true
  network_default: deny
  idempotency_required: true

outcomes:
  - PASS
  - NO_OP
  - ABSTAIN
  - DENY
  - HOLD
  - QUARANTINE
  - ERROR
```

Do not copy this into an active file until schema, parser, consumer, fixtures, tests, policy, and review are established.

[Back to top](#top)

---

## Source admission, rights, and activation

A spec may reference an admitted source. It cannot admit or activate one.

Before activation, every source ref should resolve to a governed record containing:

- stable identity and source family;
- source role and permitted claim families;
- rights, attribution, redistribution, and access terms;
- sensitivity and public-safe defaults;
- source head, version, vintage, endpoint/snapshot basis, and retrieval method;
- cadence, freshness, outage, stale-state, and correction behavior;
- spatial scale/resolution and temporal support;
- reviewer, decision date, activation state, re-review date, and rollback target.

[`ADR-0017`](../docs/adr/ADR-0017-source-descriptor-admission-process.md) documents a proposed source-admission flow. Its existence does not prove the source registry, activation records, validators, or enforcement are complete.

### Network posture

Default CI should be deterministic and no-network. Live network use requires:

- an explicit active source decision;
- a reviewed connector or source-edge implementation;
- least-privilege credentials and secret handling;
- rate limits, timeout, retry, cancellation, and circuit-breaker posture;
- bounded writes to allowed lifecycle homes;
- safe logs and receipts;
- a kill switch;
- no direct promotion or publication.

### Source-role preservation

Normalization, validation, aggregation, modeling, mapping, and generated language must not silently upcast source authority. A spec must carry source role or resolve it from the governed descriptor.

[Back to top](#top)

---

## Lifecycle and promotion boundary

The governing lifecycle remains:

```text
Pre-RAW source decision
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

A specification may describe allowed transitions and prerequisites. It cannot perform promotion by declaring a later state.

| Lifecycle concern | Spec may declare | Spec must not do |
|---|---|---|
| Pre-RAW | Source refs, activation requirement, retrieval mode. | Grant source authority. |
| RAW | Immutable input ref, digest, provenance requirements. | Store the payload beside the spec. |
| WORK | Transform profile, contract/schema refs, candidate output. | Treat candidate as canonical truth. |
| QUARANTINE | Reason codes, retained refs, re-entry conditions. | Silently discard or auto-clear risk. |
| PROCESSED | Validation and derivation requirements. | Claim evidence or policy closure from shape alone. |
| CATALOG / TRIPLET | Candidate mappings and closure prerequisites. | Turn index/graph projection into truth. |
| PUBLISHED | Release-readiness prerequisites only. | Write or approve public state. |

### Root gates

A non-trivial active specification should require:

1. identity and digest;
2. parser and consumer binding;
3. source activation and source-role resolution;
4. contract/schema resolution;
5. lifecycle transition validation;
6. domain anti-collapse checks;
7. evidence support;
8. rights and sensitivity policy;
9. deterministic validation and negative cases;
10. receipt emission;
11. catalog/triplet closure where applicable;
12. independent review and release decision;
13. correction and rollback readiness.

[Back to top](#top)

---

## Finite outcomes and reason codes

A spec-driven operation should return bounded outcomes rather than ambiguous success.

| Outcome | Meaning |
|---|---|
| `PASS` | Declared bounded operation completed; not release approval. |
| `NO_OP` | Inputs or source state did not produce an authorized delta. |
| `ABSTAIN` | Evidence, source role, temporal support, or claim support is insufficient. |
| `DENY` | Rights, sensitivity, policy, security, or prohibited transition blocks action. |
| `HOLD` | A resolvable prerequisite or review is pending. |
| `QUARANTINE` | Material requires isolated review before re-entry. |
| `ERROR` | Parser, consumer, validator, storage, receipt, or other operation failed. |
| `CANCELLED` | An operator, policy, timeout, supersession, or kill switch stopped execution. |

Candidate reason-code families:

```text
SPEC_SCHEMA_MISSING
SPEC_SCHEMA_INVALID
SPEC_DIGEST_MISMATCH
SPEC_CONSUMER_UNRESOLVED
SPEC_VERSION_INCOMPATIBLE
SOURCE_DESCRIPTOR_MISSING
SOURCE_NOT_ACTIVE
SOURCE_ROLE_MISMATCH
RIGHTS_UNRESOLVED
SENSITIVITY_REVIEW_REQUIRED
LIFECYCLE_TRANSITION_DENIED
CONTRACT_SCHEMA_UNRESOLVED
EVIDENCE_UNRESOLVED
POLICY_DENY
VALIDATION_FAILED
RECEIPT_MISSING
CATALOG_CLOSURE_MISSING
REVIEW_PENDING
RELEASE_MANIFEST_MISSING
ROLLBACK_TARGET_MISSING
```

The final vocabulary requires accepted contracts, schemas, policy, validators, tests, and steward review.

[Back to top](#top)

---

## Sensitive-domain and public-safe representation

Risk-bearing behavior must be explicit and fail closed.

| Domain or concern | Required boundary |
|---|---|
| Archaeology, cultural, Indigenous, burial, sacred places | No exact or reconstructive exposure without appropriate authority and review. |
| Fauna and Flora | Rare/protected occurrence locations and steward-controlled data deny exact public exposure by default. |
| People, genealogy, DNA, genomic data | Consent, revocation, living-person classification, retention, and private joins remain independent gates. |
| Land and settlement | Parcel geometry is not title truth; records do not automatically establish legal or operational status. |
| Infrastructure and transport | Restrict vulnerability, dependency, operator, and sensitive operational details. |
| Hazards and atmosphere | KFM specs are not official warning, emergency, medical, navigation, or life-safety authority. |
| Hydrology | Regulatory flood context, forecasts, models, observations, and inundation remain distinct. |
| Soil and agriculture | Survey, grid, station, satellite, pedon, interpretation, aggregate, field, and operator claims remain distinct. |
| Geology and resources | Occurrence, deposit, reserve, permit, production, ownership, and extraction remain distinct. |

Generalization, aggregation, interpolation, redaction, suppression, or delayed release must be separate derived operations with explicit parameters, receipts, policy decisions, validation, review, correction, and rollback implications.

[Back to top](#top)

---

## Parser, consumer, and runtime binding

An active spec system needs deterministic agreement among five surfaces:

```text
spec bytes
  -> canonicalized content and digest
  -> accepted schema
  -> parser/discovery registry
  -> verified implementation consumer
  -> deterministic fixtures and agreement tests
```

### Parser requirements

- reject unknown or unsupported schema versions;
- reject duplicate IDs and incompatible aliases;
- fail closed on unresolved refs;
- preserve source role, lifecycle state, and policy fields;
- avoid network access while parsing;
- produce stable validation diagnostics;
- never treat parse success as activation.

### Consumer requirements

- identify the exact supported spec versions;
- prove stage/action mappings;
- reject undeclared side effects;
- enforce allowed lifecycle transitions;
- emit deterministic run identity and receipts;
- honor no-network, dry-run, cancellation, and kill-switch settings;
- deny direct publication;
- surface partial state and rollback needs.

### Discovery and activation

Directory scanning alone is unsafe as an activation mechanism because the tree contains placeholders and compatibility paths. Activation should require a governed registry or explicit decision record.

[Back to top](#top)

---

## Validation, tests, fixtures, and CI

### Current limitations

- checked `tests/pipeline_specs/README.md` is absent;
- checked `fixtures/pipeline_specs/README.md` is absent;
- the shared [`tests/pipelines/`](../tests/pipelines/README.md) lane is README-only;
- sampled specs are placeholders or empty-stage scaffolds;
- no accepted root schema, parser, discovery registry, active-spec registry, or substantive root CI gate was established;
- current pass rate, coverage, mutation score, flake rate, runtime, and promotion dependency are unknown.

### Minimum future fixture set

```text
fixtures/pipeline_specs/
├── valid/
├── invalid/
├── denied/
├── held/
├── abstain/
├── no_op/
├── migration/
└── sensitive_canaries/
```

Do not create these directories until concrete payloads and consumers justify them.

### Minimum future tests

- schema and canonicalization conformance;
- stable ID and digest behavior;
- duplicate-ID and alias conflict denial;
- parser/consumer version agreement;
- source-descriptor and activation resolution;
- source-role preservation;
- lifecycle allow/deny matrix;
- no-direct-publish enforcement;
- contract/schema/evidence/policy ref resolution;
- domain anti-collapse cases;
- rights/sensitivity negative cases;
- no-network default and explicit live-network gating;
- deterministic replay, idempotency, retry, cancellation, and partial state;
- required receipt and digest assertions;
- correction, withdrawal, supersession, and rollback behavior;
- zero-test-collection failure for a claimed active lane.

### CI requirements

A substantive root workflow should:

- use pull-request-safe events;
- declare least-privilege permissions;
- use repository-owned commands rather than duplicate inline logic;
- validate changed specs and their dependency closure;
- run positive and negative fixtures;
- block activation or release dependency on failure;
- avoid secrets for default PR checks;
- publish only bounded reviewer artifacts;
- expose stable job names and a disable/rollback path.

A green workflow means the declared check completed. It does not prove source authority, domain truth, evidence closure, policy approval, release approval, or publication.

[Back to top](#top)

---

## Review, versioning, and change discipline

### Required review roles

Depending on scope, identify:

- pipeline-spec and pipeline owners;
- affected domain steward;
- source and rights steward;
- contract/schema and validation steward;
- evidence/receipt steward;
- policy/sensitivity/security reviewer;
- release steward when release-readiness semantics change;
- docs steward.

CODEOWNERS routing does not replace `ReviewRecord`, stewardship assignment, policy decision, or release approval.

### Change classes

| Change | Minimum burden |
|---|---|
| README clarification | Documentation review, link/structure checks, generated receipt when AI-authored. |
| Placeholder to candidate conversion | Schema, parser, consumer, fixtures, tests, source, policy, receipt, and owner review. |
| Add or change source ref | Source admission, rights, sensitivity, role, and activation review. |
| Add network/schedule behavior | Security, credentials, rate-limit, outage, kill-switch, no-network CI, and incident review. |
| Change lifecycle output | Contract/schema/policy/test review and migration/rollback plan. |
| Add catalog or publish-readiness behavior | Evidence, receipt, review, release, correction, and rollback closure. |
| Rename/move/alias | Consumer inventory, deprecation window, migration note, tests, and rollback. |
| Change root or authority | Accepted ADR before implementation. |

### Versioning rules

- do not reuse a version for different semantics;
- preserve immutable digests and supersession lineage;
- distinguish file version from schema version and implementation version;
- record backward compatibility and consumer support;
- never activate an alias automatically;
- treat merge, activation, execution, promotion, and publication as separate events.

[Back to top](#top)

---

## Deactivation, correction, and rollback

### Documentation rollback

For this README, rollback is ordinary Git rollback: close the draft PR before merge or revert its documentation commit afterward.

### Spec deactivation

An active spec should be disabled through an explicit record, not silent deletion. Preserve:

- spec ID, version, digest, and state;
- reason and effective time;
- affected sources, consumers, schedules, and runs;
- last successful and failed runs;
- lifecycle, receipt, proof, catalog, release, and public-artifact refs;
- correction/withdrawal obligations;
- rollback target;
- reviewer and decision state.

### Correction propagation

A corrected or superseded spec, source, contract, schema, policy, or implementation may invalidate:

- queued and completed runs;
- work, quarantine, and processed candidates;
- receipts and EvidenceBundles;
- catalog/triplet projections;
- release candidates and manifests;
- tiles, layers, exports, API payloads, screenshots, and generated summaries;
- downstream specifications derived from the corrected state.

The repository should eventually maintain an inspectable dependency graph for this propagation. This README does not prove that machinery exists.

### Migration rollback

Moves or alias retirements should preserve old/new paths, spec IDs/digests, consumer refs, deprecation period, compatibility behavior, test evidence, and mechanical rollback steps.

[Back to top](#top)

---

## Definition of done for an active specification

A YAML file is not active merely because it exists, parses, or contains stages.

An active specification should satisfy all applicable items:

- [ ] Stable spec ID, semantic version, state, owners, and immutable digest.
- [ ] Accepted machine schema and canonicalization rules.
- [ ] Accepted parser and deterministic discovery.
- [ ] Verified implementation consumer and compatible version.
- [ ] Resolvable SourceDescriptor refs and activation decisions.
- [ ] Explicit source roles, rights, sensitivity, scale, temporal support, and uncertainty.
- [ ] Allowed lifecycle inputs and candidate outputs.
- [ ] Direct `PUBLISHED` writes prohibited.
- [ ] Contract and schema refs resolve.
- [ ] Domain anti-collapse and cross-lane boundaries are explicit.
- [ ] Valid, invalid, denied, held, abstain, no-op, and migration fixtures exist.
- [ ] Spec-to-consumer agreement tests pass.
- [ ] Default CI is deterministic and no-network.
- [ ] Idempotency, replay, retry, cancellation, quarantine, and partial-state behavior are tested.
- [ ] Evidence, policy, review, and receipt obligations are enforced.
- [ ] Catalog/triplet handoffs preserve provenance and correction lineage.
- [ ] Publish-readiness requires an independent ReleaseManifest or accepted equivalent.
- [ ] Activation, deactivation, incident hold, correction, withdrawal, supersession, and rollback are documented.
- [ ] Human review is separate from generation, implementation, validation, merge, activation, and release.
- [ ] CI and branch-protection dependencies are verified where relied upon.

Until then, use `inventory_placeholder`, `stage_scaffold`, `proposed`, or `candidate` rather than `active`.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Exhaustive recursive root inventory | `NEEDS VERIFICATION` | Pinned recursive tree and generated inventory report. |
| Canonical pipeline-spec schema | `UNKNOWN` | Accepted schema and ADR/contract. |
| Canonicalization and digest algorithm | `UNKNOWN` | Accepted normalization and hashing specification. |
| Parser and discovery mechanism | `UNKNOWN` | Code, registry, tests, and version contract. |
| Consumer binding | `UNKNOWN` | Deterministic registry and agreement tests. |
| Active specification inventory | `NOT ESTABLISHED` | Activation records and current registry. |
| Meaning of `version: 1` in stage scaffolds | `UNKNOWN` | Versioning contract. |
| Alias decisions for air, people, and settlement | `NEEDS VERIFICATION` | ADR/migration records. |
| Shared versus domain watcher placement | `CONFLICTED` | Delegation rule and migration decision. |
| Historical `pipeline_specs/domains/...` references | `CONFLICTED` | Pinned tree, drift entry, and migration decision. |
| Child README inventory freshness | `NEEDS VERIFICATION` | Automated tree-to-README check. |
| Source registry topology and activation vocabulary | `NEEDS VERIFICATION` | Accepted source-control contract and records. |
| Root fixtures and spec tests | `NOT ESTABLISHED` | Concrete files and current run results. |
| Dedicated root CI | `NOT ESTABLISHED` | Workflow, commands, fixtures, and passing runs. |
| Default no-network enforcement | `NEEDS VERIFICATION` | Harness and workflow evidence. |
| Rights/sensitivity policy enforcement | `NEEDS VERIFICATION` | Executable policy, fixtures, tests, and decisions. |
| Receipt schema bindings for pipeline runs | `UNKNOWN` | Accepted schemas, emitters, and examples. |
| Promotion dependency | `UNKNOWN` | Release workflow and branch-protection evidence. |
| Correction propagation and rollback drills | `UNKNOWN` | Dependency graph, runbooks, records, and drill results. |
| Named owners and independent reviewers | `NEEDS VERIFICATION` | Steward assignments and review records. |
| Production execution and public effects | `UNKNOWN` | Runtime, deployment, release, and monitoring evidence. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation supported | Status |
|---|---|---:|
| This README at `527ac01444c23046f0406dbb9e4cf5b2a74cd4cc` | Existing v0.2 root contract and prior blob `3a6599898606126604298a281de53e39fdba98ce`. | `CONFIRMED` |
| [`pipelines/README.md`](../pipelines/README.md) | Executable behavior belongs under `pipelines/`; implementation claims remain unverified without tests/runtime evidence. | `CONFIRMED root boundary` |
| [`pipelines/specs/README.md`](../pipelines/specs/README.md) | `pipelines/specs/` is a guardrail, not an alternate spec root. | `CONFIRMED` |
| Bounded `doc_id` search | Seventeen direct child README lanes and five nested README sublanes surfaced. | `CONFIRMED bounded result` |
| `pipeline_specs/agriculture/normalize.yaml` | Representative empty-stage scaffold: name, version, `stages: []`. | `CONFIRMED` |
| `pipeline_specs/soil/ingest.yaml` | Representative empty-stage scaffold. | `CONFIRMED` |
| `pipeline_specs/archaeology/ingest.spec.yaml` | Representative short documentation-inventory placeholder. | `CONFIRMED` |
| `pipeline_specs/geology/well_logs.spec.yaml` | Representative short documentation-inventory placeholder. | `CONFIRMED` |
| `pipeline_specs/hazards/fema_nfhl.yaml` | Representative short documentation-inventory placeholder. | `CONFIRMED` |
| `pipeline_specs/hydrology/wbd_huc12_ingest.yaml` | Representative short documentation-inventory placeholder. | `CONFIRMED` |
| `pipeline_specs/roads-rail-trade/wzdx_v4.yaml` | Representative short documentation-inventory placeholder. | `CONFIRMED` |
| [`agriculture/README.md`](agriculture/README.md) plus exact payload read | Child README inventory and current path evidence do not fully agree. | `CONFIRMED drift signal` |
| [`air/README.md`](air/README.md) | Air is a compatibility guardrail; Atmosphere is preferred. | `CONFIRMED documentation boundary` |
| [`people/README.md`](people/README.md) | People is a README-only alias subordinate to People/DNA/Land. | `CONFIRMED` |
| [`settlement/README.md`](settlement/README.md) | Settlement is a README-only alias subordinate to Settlements/Infrastructure. | `CONFIRMED` |
| [`watchers/README.md`](watchers/README.md) | Shared watcher lane is placeholder-only and placement-conflicted. | `CONFIRMED` |
| [`tests/pipelines/README.md`](../tests/pipelines/README.md) | Direct pipeline test lane is README-only; dedicated suite and root spec tests are not established. | `CONFIRMED documentation inventory` |
| Exact checks for `tests/pipeline_specs/README.md` and `fixtures/pipeline_specs/README.md` | Both checked paths are absent. | `CONFIRMED checked-path absence` |
| Search for `pipeline_spec.schema` | No result surfaced. | `CONFIRMED bounded no-result` |
| Search for `source_descriptor_refs:` | Occurrences surfaced in README/docs, not active YAML payloads. | `CONFIRMED bounded result` |
| [`docs/architecture/directory-rules.md`](../docs/architecture/directory-rules.md) | Responsibility-root placement and unresolved Directory Rules self-placement conflict. | `CONFIRMED file / conflict open` |
| [`ADR-0017`](../docs/adr/ADR-0017-source-descriptor-admission-process.md) | Proposed source descriptor and activation process; not accepted implementation proof. | `CONFIRMED proposed ADR` |
| [`.github/CODEOWNERS`](../.github/CODEOWNERS) | `/pipeline_specs/` routes to `@bartytime4life`; enforcement and role separation remain unverified. | `CONFIRMED routing` |
| [`data/receipts/generated/README.md`](../data/receipts/generated/README.md) | Generated receipts are process provenance, not proof or approval. | `CONFIRMED lane contract` |

### Evidence limits

- Code-index search is bounded and may lag branch-local or newly generated content.
- Checked-path absence is not a full-history, ignored-file, or all-branch absence claim.
- Child README inventories can become stale.
- No repository clone, recursive tree command, repository-native test run, branch-protection setting, deployment, source system, dashboard, or production runtime was inspected in this documentation revision.
- Planning documents and placeholders preserve lineage but do not prove intended behavior exists.

[Back to top](#top)

---

## Change history

### v0.3 — 2026-07-18

- replaced the planning-oriented root tree with a commit-pinned maturity and routing boundary;
- recorded seventeen bounded direct README lanes and five nested README sublanes;
- classified current payloads as empty-stage scaffolds, documentation-inventory placeholders, compatibility aliases, or README-only boundaries;
- surfaced child README inventory drift and required pinned tree regeneration before activation;
- documented `pipeline_specs/` versus `pipelines/specs/` authority;
- strengthened source activation, lifecycle, finite outcome, sensitivity, parser/consumer binding, validation, correction, and rollback requirements;
- added a root lane registry, active-spec definition of done, open verification register, and evidence ledger;
- changed documentation only.

### v0.2 — 2026-06-13

- expanded the former short root stub into a governed declarative configuration contract;
- defined declarative-versus-executable separation, lifecycle gates, anti-collapse rules, lane map, minimal profile example, validation expectations, and open questions;
- presented a recommended root tree without a current repository-grounded payload maturity inventory.

[Back to top](#top)
