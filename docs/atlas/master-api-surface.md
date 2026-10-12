<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-atlas-master-api-surface-compatibility-pointer
title: Master API Surface Compatibility Pointer and Current Evidence Boundary
type: compatibility-pointer; api-surface; atlas-lineage; repository-evidence
version: v2.0
status: deprecated; repository-grounded; pointer-only; non-executable; non-release; non-publication
owner: "@bartytime4life via CODEOWNERS; independent docs, API, evidence, policy, release, security, and publication stewardship NEEDS VERIFICATION"
created: 2026-05-25
updated: 2026-08-22
policy_label: repository-public; documentation; compatibility; governed-api; finite-outcomes; cite-or-abstain
owning_root: docs/
responsibility: >-
  Preserve the legacy docs/atlas/master-api-surface.md backlink, direct readers
  to the current atlas, Governed API, contract, schema, validator, test, and
  review surfaces, and state the current executable API boundary without
  becoming a route registry, contract, schema, policy, release record, OpenAPI
  document, or publication authority.
authority: >-
  Human-readable compatibility routing and repository-evidence orientation
  only. Current route bytes live under apps/governed-api/; runtime meaning lives
  under contracts/; machine shape lives under schemas/; policy, evidence,
  release, correction, rollback, deployment, and public behavior remain with
  their owning roots and accountable decisions.
current_path: docs/atlas/master-api-surface.md
canonical_relationship: >-
  This path is a deprecated singular-lane compatibility pointer. Accepted
  Directory Rules v2 places curated atlas material under docs/atlases/, but the
  current repository has no standalone docs/atlases/master-api-surface.md
  carrier and the canonical atlas lane records unresolved carrier naming and
  legacy-lane convergence. This revision therefore preserves the pointer in
  place and keeps creation, migration, or deletion HOLD pending a reviewed
  carrier decision, consumer closure, validation, and rollback.
truth_posture: >-
  CONFIRMED the current pointer path and prior blob, accepted Directory Rules
  authority, canonical docs/atlases lane, absence of a standalone
  docs/atlases/master-api-surface.md file at the pinned commit, the active
  Governed API architecture landing page, the executable WSGI dispatcher, the
  exact three-route registry, schema-shaped ABSTAIN and ERROR scaffold
  responses, bounded route tests, and the RuntimeResponseEnvelope
  contract/schema/validator family / LINEAGE the Atlas v1.0 Chapter 20 Master
  API Surface register, its six historical API-family groupings, and older
  architecture-manual route names / PROPOSED future substantive route
  families, a standalone atlas extract, accepted route-versioning and
  reason-code registries, composed evidence/policy/release response building,
  and public deployment / UNKNOWN caller authentication, authorization,
  live policy evaluation, authoritative evidence resolution, release and
  correction lookup, governed ANSWER execution, client transport, deployment,
  operational telemetry, and public parity / NEEDS VERIFICATION every claim
  beyond the inspected repository bytes and bounded tests.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2481e12958cbc237b7339302c69e2ebe17263d5b
  target_prior_blob: b5bd266b1f04b2aebcd49d4f5a7d620dbad52cb1
  canonical_atlases_readme_blob: 5dd756497b9eb20b4ffa55cd2cfadcd77ee2f3b4
  atlas_source_carrier_blob: 4a1a4aad7a3cde90dcb784f6a66dde8b8be06637
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  governed_api_architecture_blob: a1cc67ea693f8f83614b63e01ea43b6cef28592f
  governed_api_app_readme_blob: 4f21150852f133ba919b11f4f8792185fa870dae
  governed_api_main_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  governed_api_route_registry_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 371e60d9f96c78e31c8a1e6109d19dee5da4213b
  governed_api_route_test_blob: 2be20f5d93c03da7677c34b11a31875a00b2ed28
  runtime_response_contract_blob: 9dfc286984b5b52b383753fe6215a2b31df8c876
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  runtime_response_validator_blob: 44ce7d51038a9adf9fcbdb18108cc27da8381e33
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
inspection_boundary: >-
  Current-session GitHub reads covered current main, the complete prior target,
  the canonical and legacy atlas lane READMEs, the repository-present Atlas v1.1
  source carrier, accepted Directory Rules and ADR-0029, the current Governed
  API architecture and app boundaries, WSGI entry point, exact route registry,
  route stubs, RuntimeResponseEnvelope contract/schema, bounded route tests,
  CODEOWNERS, open pull-request overlap, and matching task branches. No mounted
  checkout, repository-native command, identity provider, authorization
  middleware, live policy engine, authoritative evidence registry, release
  service, deployed API, browser transport, runtime log, dashboard, or public
  request was exercised.
related:
  - ./README.md
  - ../atlases/README.md
  - ../atlases/domains-atlas-v1.1.md
  - ../atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - ../architecture/governed-api/README.md
  - ../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../doctrine/directory-rules.md
  - ../../apps/governed-api/README.md
  - ../../apps/governed-api/routes/README.md
  - ../../apps/governed-api/src/governed_api/main.py
  - ../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../apps/governed-api/src/governed_api/stub.py
  - ../../apps/governed-api/tests/test_abstain_routes.py
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../tools/validators/validate_runtime_response_envelope.py
  - ../../.github/CODEOWNERS
tags: [kfm, docs, atlas, compatibility, pointer, master-api-surface, governed-api, runtime-response-envelope, finite-outcomes, repository-grounded, non-publication]
notes:
  - "v2.0 replaces a corpus-only deprecated pointer with a current-repository evidence boundary while preserving the path and legacy anchors."
  - "No standalone docs/atlases/master-api-surface.md file exists at the pinned commit; this revision does not create one."
  - "The executable Governed API surface currently consists of GET /bootstrap, GET /layers, and GET /evidence, each returning ABSTAIN / NOT_IMPLEMENTED; unknown paths and unsupported methods fail closed with safe ERROR envelopes."
  - "The historical Atlas API-family table is retained as lineage and navigation, not represented as the current route manifest."
  - "Physical removal of this pointer and the singular legacy lane remains HOLD pending consumer closure and a reviewed migration."
  - "No API, contract, schema, policy, evidence, release, correction, rollback, deployment, or publication behavior is changed by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="master-api-surface"></a>

# Master API Surface — Compatibility Pointer and Current Evidence Boundary

> **Purpose.** Preserve a legacy backlink while directing readers to the
> repository surfaces that currently own API architecture, executable routes,
> runtime-envelope meaning, machine shape, validation, atlas lineage, and review.

[![path](https://img.shields.io/badge/path-deprecated%20compatibility-b42318?style=flat-square)](#1-status-and-evidence-boundary)
[![current routes](https://img.shields.io/badge/current%20routes-3%20ABSTAIN-0969da?style=flat-square)](#4-current-executable-api-checkpoint)
[![answer](https://img.shields.io/badge/governed%20ANSWER-HOLD-b42318?style=flat-square)](#4-current-executable-api-checkpoint)
[![standalone atlas](https://img.shields.io/badge/standalone%20atlas-absent-6e7781?style=flat-square)](#3-where-current-content-lives)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#2-responsibility-and-placement-boundary)

> [!IMPORTANT]
> **This file is a pointer, not the Master API Surface register.** It does not
> define a route, DTO, contract, schema, reason code, policy decision, evidence
> result, release state, OpenAPI description, or public API commitment.

> [!WARNING]
> **The current executable route manifest is much narrower than the historical
> atlas design.** At the pinned commit, only `GET /bootstrap`, `GET /layers`,
> and `GET /evidence` are registered. Each returns
> `ABSTAIN / NOT_IMPLEMENTED`. Historical six-family tables and `/api/...`
> examples remain design lineage, not proof of live routes.

> [!CAUTION]
> **Do not create the absent standalone target by following the old pointer
> literally.** `docs/atlases/master-api-surface.md` is not tracked at the
> evidence snapshot, while the canonical atlas-lane README records unresolved
> carrier naming and incomplete legacy-lane convergence. Creating another
> carrier remains `HOLD`.

> [!NOTE]
> **Physical deletion is also held.** Accepted Directory Rules v2 makes
> `docs/atlases/` the curated atlas lane, but removal of this compatibility
> pointer still requires an accepted migration disposition, inbound and external
> consumer closure, link validation, a correction path, and a rollback target.

**Quick navigation:** [Status](#1-status-and-evidence-boundary) ·
[Placement](#2-responsibility-and-placement-boundary) ·
[Redirects](#3-where-current-content-lives) ·
[Executable checkpoint](#4-current-executable-api-checkpoint) ·
[Atlas lineage](#5-historical-atlas-lineage) ·
[Authority map](#6-api-authority-map) ·
[Use rules](#7-pointer-use-rules-and-anti-patterns) ·
[Validation](#8-validation-correction-and-rollback) ·
[Open work](#9-open-verification-backlog) ·
[References](#10-related-surfaces) ·
[History](#11-change-history-and-non-effects)

---

## 1. Status and evidence boundary

| Question | Current bounded answer | Truth label |
|---|---|---|
| Does this legacy path exist? | Yes. The prior pointer is tracked at blob `b5bd266b1f04b2aebcd49d4f5a7d620dbad52cb1`. | `CONFIRMED` |
| Is this file the API register or an executable API specification? | No. It is a human compatibility pointer only. | `CONFIRMED` |
| Is `docs/atlases/` the current atlas lane? | Yes, under accepted Directory Rules v2 and the repository-present lane README. | `CONFIRMED` placement |
| Does `docs/atlases/master-api-surface.md` exist? | No file at that exact path was present at the pinned commit. | `CONFIRMED` absence at snapshot |
| Has one canonical atlas carrier name been accepted? | No accepted carrier-name decision was verified; the lane README records naming conflict and incomplete convergence. | `CONFLICTED` / `NEEDS VERIFICATION` |
| What executable public routes are registered now? | `/bootstrap`, `/layers`, and `/evidence`, all `GET` only. | `CONFIRMED` code shape |
| What do those routes return? | Schema-shaped `ABSTAIN` envelopes with `reason_code=NOT_IMPLEMENTED`. | `CONFIRMED` code and bounded test |
| Does an executable governed `ANSWER` path exist? | No inspected route authenticates a caller, resolves authoritative evidence, evaluates live policy, binds release state, or emits a substantive answer. | `UNKNOWN`; current route result is negative only |
| Do unknown routes and unsupported methods fail closed? | Unknown paths return `404`; non-GET requests to registered paths return `405`; both use a safe `ERROR` envelope. | `CONFIRMED` dispatcher shape |
| Does a green route/schema test prove a complete trust membrane? | No. It proves only its bounded negative-envelope and structural assertions. | `CONFIRMED` boundary |
| May this pointer be deleted now? | No verified consumer-closure or accepted removal packet was inspected. | `HOLD` |
| Does this documentation update release, deploy, or publish anything? | No. | `CONFIRMED` |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current-session repository bytes or remote state. |
| `PROPOSED` | Design, route family, carrier, vocabulary, or behavior not accepted or proved. |
| `UNKNOWN` | Available evidence does not establish the claim. |
| `NEEDS VERIFICATION` | A concrete repository, runtime, reviewer, or consumer check remains. |
| `CONFLICTED` | Current carriers, paths, or writable surfaces make incompatible authority claims. |
| `LINEAGE` | Retained historical design or source framing; not current implementation authority. |
| `HOLD` | Proceeding would cross an unresolved placement, consumer, policy, review, release, or rollback boundary. |

Repository presence proves bytes and bounded implementation shape. It does not
prove policy correctness, evidence closure, caller authority, release state,
deployment, service availability, or public parity.

[Back to top](#top)

---

<a id="4-why-this-file-is-here-as-a-pointer"></a>

## 2. Responsibility and placement boundary

### This file owns

- the legacy backlink at `docs/atlas/master-api-surface.md`;
- a current redirect map to repository-present authority surfaces;
- a bounded summary of the executable route manifest;
- explicit separation of atlas lineage from current route evidence;
- correction and rollback guidance for this pointer.

### This file does not own

| Responsibility | Owning surface | Effect here |
|---|---|---|
| Atlas-lane navigation and carrier inventory | [`docs/atlases/README.md`](../atlases/README.md) | Governs current atlas-lane posture and naming conflicts |
| Governed API architecture | [`docs/architecture/governed-api/README.md`](../architecture/governed-api/README.md) | Current repository-grounded architecture landing page |
| Executable route dispatch | [`apps/governed-api/src/governed_api/main.py`](../../apps/governed-api/src/governed_api/main.py) and route registry | Current code outranks historical route prose |
| Runtime response semantics | [`RuntimeResponseEnvelope` contract](../../contracts/runtime/runtime_response_envelope.md) | This pointer cannot add fields or outcomes |
| Runtime response machine shape | [Paired JSON Schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | This pointer cannot redefine shape |
| Runtime-envelope validation | [Runtime validator](../../tools/validators/validate_runtime_response_envelope.py) and tests/fixtures | A passing check remains bounded evidence |
| Evidence, policy, rights, sensitivity, and access | Their owning contracts, schemas, policy, resolver, review, and data surfaces | This pointer cannot allow, deny, redact, or support a claim |
| Release, correction, withdrawal, and rollback | `release/` and governed accountability records | This pointer creates no released state |
| OpenAPI, HTTP versioning, authentication, authorization, rate limits, and deployment | Accepted API decisions plus executable/configuration roots | None is established here |

### Directory Rules decision

Accepted ADR-0029 adopts Directory Rules v2. Those rules place human-readable
material under `docs/`, make `docs/atlases/` the curated atlas lane, and require a
single authority owner for each artifact.

| Proposed action | Placement outcome | Basis |
|---|---|---|
| Correct this existing pointer in place | `PLACE` | Existing human compatibility document; no authority or lifecycle change |
| Add substantive route/register content here | `DENY` | Would make a deprecated compatibility path a parallel API/atlas authority |
| Create `docs/atlases/master-api-surface.md` in this slice | `HOLD` | Exact target is absent; carrier naming and canonical relationship remain unsettled |
| Move or delete this pointer now | `HOLD` | Consumer closure, deprecation state, link migration, and rollback evidence are incomplete |
| Change runtime routes, contracts, schemas, or policy through this file | `DENY` | Documentation cannot mutate another responsibility root |

[Back to top](#top)

---

<a id="1-what-this-register-is-orientation-only"></a>
<a id="2-where-the-canonical-content-lives"></a>

## 3. Where current content lives

Use the surface matching the question. No single document below substitutes for
the others.

| Reader need | Current surface | What it can establish |
|---|---|---|
| Atlas-lane status, inventory, naming conflict, and legacy convergence | [`docs/atlases/README.md`](../atlases/README.md) | Current human documentation-lane boundary |
| Atlas v1.1 source structure and Chapter 20/24 lineage | [`docs/atlases/domains-atlas-v1.1.md`](../atlases/domains-atlas-v1.1.md) | Human source carrier and lineage; registers remain navigational |
| Consolidated atlas navigation | [`KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md`](../atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md) | Repository-present consolidated navigation carrier |
| Current Governed API architecture and maturity | [`docs/architecture/governed-api/README.md`](../architecture/governed-api/README.md) | Repository-grounded architecture boundary and current holds |
| App-level trust-membrane intent | [`apps/governed-api/README.md`](../../apps/governed-api/README.md) | Application boundary; older uncertainty should be reconciled with current code |
| Route-family design guidance | [`apps/governed-api/routes/README.md`](../../apps/governed-api/routes/README.md) | Proposed route-family obligations; not a live route manifest |
| Current executable route manifest | [`routes/registry.py`](../../apps/governed-api/src/governed_api/routes/registry.py) | Exact registered routes at the pinned commit |
| Current dispatch behavior | [`main.py`](../../apps/governed-api/src/governed_api/main.py) | GET dispatch, `404`, and `405` behavior |
| Current negative-envelope builder | [`stub.py`](../../apps/governed-api/src/governed_api/stub.py) | ABSTAIN and safe ERROR scaffold shape |
| Client-facing runtime meaning | [`RuntimeResponseEnvelope` contract](../../contracts/runtime/runtime_response_envelope.md) | Proposed semantic meaning and boundaries |
| Machine-valid envelope shape | [Runtime response schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | Closed field shape and finite outcome enum |
| Bounded route proof | [`test_abstain_routes.py`](../../apps/governed-api/tests/test_abstain_routes.py) | Deterministic negative-route assertions and schema-subset checks |
| Review routing | [`.github/CODEOWNERS`](../../.github/CODEOWNERS) | GitHub review request routing only; not approval or release authority |

> [!NOTE]
> The active architecture landing page is
> `docs/architecture/governed-api/README.md`. The former flat
> `docs/architecture/governed-api.md` entrypoint was retired. Do not restore or
> cite the retired flat path as current authority.

[Back to top](#top)

---

## 4. Current executable API checkpoint

The current surface is a **fail-closed scaffold**, not a general API.

### 4.1 Registered routes

| Method and path | Code owner | Current response | Evidence-backed interpretation |
|---|---|---|---|
| `GET /bootstrap` | [`bootstrap.py`](../../apps/governed-api/src/governed_api/routes/bootstrap.py) | `ABSTAIN / NOT_IMPLEMENTED` | Route exists; no bootstrap payload is implemented |
| `GET /layers` | [`layers.py`](../../apps/governed-api/src/governed_api/routes/layers.py) | `ABSTAIN / NOT_IMPLEMENTED` | Route exists; no released layer catalogue is returned |
| `GET /evidence` | [`evidence.py`](../../apps/governed-api/src/governed_api/routes/evidence.py) | `ABSTAIN / NOT_IMPLEMENTED` | Route exists; no authoritative EvidenceBundle resolution occurs |
| Non-GET on a registered path | [`main.py`](../../apps/governed-api/src/governed_api/main.py) | HTTP `405` + `ERROR / SAFE_RUNTIME_ERROR` | Unsupported mutation is rejected |
| Unknown path | [`main.py`](../../apps/governed-api/src/governed_api/main.py) | HTTP `404` + `ERROR / SAFE_RUNTIME_ERROR` | Unknown routes fail closed |

The exact route registry contains three entries. It does not contain `/focus`,
`/story`, `/compare`, `/exports`, `/review`, `/corrections`, `/diagnostics`, or
historical `/api/...` examples.

### 4.2 Envelope checkpoint

The scaffold emits the ten unconditional `RuntimeResponseEnvelope` fields:

```text
id
spec_hash
version
issued_at
outcome
reason_code
evidence_refs
policy_state
freshness
correction_state
```

For the three registered routes:

- `outcome` is `ABSTAIN`;
- `reason_code` is `NOT_IMPLEMENTED`;
- `evidence_refs` is empty;
- the `spec_hash` is a deliberate scaffold placeholder, not an accepted release
  or truth digest;
- no substantive payload is returned.

The paired runtime schema permits exactly:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

For `ANSWER`, the schema additionally requires nonempty evidence references and
`precision_actually_used`; it forbids that precision object for the other three
outcomes. The current route code exercises only the negative scaffold profile.

### 4.3 What is not proved

No inspected path establishes:

- caller identity, authentication, authorization, audience, or role grants;
- live policy, rights, sensitivity, redaction, or obligation evaluation;
- authoritative `EvidenceRef -> EvidenceBundle` resolution;
- released artifact, correction, withdrawal, or rollback lookup;
- a governed substantive payload or `ANSWER`;
- a live browser-to-API transport;
- deployed isolation, ingress, health, operational logs, dashboards, or public
  availability.

[Back to top](#top)

---

## 5. Historical atlas lineage

The phrase **Master API Surface** comes from Atlas v1.0 Chapter 20. That source
organized API families, domains, DTOs, and finite outcomes for human navigation.
Atlas v1.1 retains v1.0 by extension and adds Chapter 24 references.

The repository-present Atlas v1.1 carrier also states that its master tables are
**navigational, not authoritative**. Contracts, schemas, evidence, policy, and
current implementation remain separate.

### Lineage-to-current crosswalk

| Historical surface | Current interpretation |
|---|---|
| Atlas v1.0 Chapter 20 API Surface | `LINEAGE` human register; not a live route manifest |
| Atlas v1.1 §24.3 Decision Outcome Envelope Reference | Human consolidation of per-domain J tables and Chapter 20; not machine authority |
| Six historical API-family groupings | Useful design categories; current implementation must be checked family by family |
| Older `/api/...` examples | Architecture proposal lineage unless current route code, tests, HTTP binding, and deployment prove them |
| `docs/atlases/master-api-surface.md` | Suggested old extraction target; absent at the evidence snapshot and not created here |

### No silent upgrade rule

A historical atlas row becomes a current API claim only after the relevant
repository evidence closes:

```text
accepted semantic contract
  -> canonical machine schema
  -> route code and HTTP binding
  -> authorization and policy enforcement
  -> evidence and release integration
  -> deterministic positive and negative fixtures
  -> tests and operational evidence
  -> reviewed public posture
```

Until then, use `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="3-per-api-family-redirects"></a>

## 6. API authority map

This section maps responsibility classes, not historical route names.

| Concern | Authority surface | Current bounded posture |
|---|---|---|
| Route registration and dispatch | `apps/governed-api/src/governed_api/` | Three negative GET routes are executable |
| App-local route-family organization | `apps/governed-api/routes/` and source-package route README | Design and documentation; broader route families remain proposed |
| Client-facing finite response meaning | `contracts/runtime/runtime_response_envelope.md` | Draft/proposed semantic contract; paired and repository-grounded |
| Client-facing machine shape | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | Closed schema; four outcomes and conditional ANSWER precision rules |
| Deterministic validation | `tools/validators/validate_runtime_response_envelope.py`, fixtures, tests | Bounded shape and cross-field proof when run |
| Runtime decision detail | `contracts/runtime/decision_envelope.md` | Companion object, not the client response or policy authority |
| Evidence support | Evidence contracts, schemas, resolver, and governed data/proof lanes | Component and documentation evidence exist; authoritative request-time closure is unproved |
| Policy and access | `policy/`, policy contracts/schemas, accountable evaluation | Not executed by this pointer or current route scaffold |
| Review | Governance contracts, schemas, records, and authorized reviewers | CODEOWNERS routing is not a ReviewRecord |
| Release, correction, rollback | `release/` and governed accountability objects | No current route binds or mutates these states |
| Atlas synthesis | `docs/atlases/` | Human navigation only |
| Public deployment | `infra/`, deployment configuration, runtime evidence, and release authority | `UNKNOWN` / `HOLD` |

### Conflict-safe linking rule

When an object family has case, singular/plural, compatibility, or schema-home
drift, link to its current family README or accepted authority decision rather
than selecting a path by guesswork. This pointer does not settle source,
governance, policy, domain-envelope, or route-versioning path conflicts.

[Back to top](#top)

---

<a id="5-what-this-file-does-not-contain"></a>

## 7. Pointer use rules and anti-patterns

### Use this file to

- preserve a legacy inbound link;
- find the current atlas, architecture, code, contract, schema, validator, test,
  and review surfaces;
- distinguish current executable routes from historical API designs;
- identify the evidence needed before a proposed API family can be called live;
- understand why migration or deletion is still held.

### Do not use this file to

- publish a Master API Surface register body;
- declare a historical route or DTO live;
- create or restore an absent `docs/atlases/master-api-surface.md` carrier;
- redefine `RuntimeResponseEnvelope`, `DecisionEnvelope`, `EvidenceBundle`,
  `PolicyDecision`, `ReviewRecord`, or domain-object shape;
- author policy, evidence, review, release, correction, or rollback decisions;
- serve as OpenAPI, AsyncAPI, HTTP binding, authentication, authorization,
  versioning, rate-limit, or deprecation policy;
- claim that a schema, test, workflow, badge, commit, pull request, or merge
  proves deployment or publication;
- add substantive atlas material under the deprecated singular lane.

### Anti-pattern register

| Anti-pattern | Failure | Required posture |
|---|---|---|
| Historical table equals live API | Atlas design is represented as executable current behavior | Pin current code, schema, tests, HTTP binding, and deployment evidence |
| Pointer becomes authority | DTO fields or route rules are authored here | Move meaning, shape, policy, and implementation to their owning roots |
| Absent target fabricated | A proposed standalone carrier is described as tracked | State absence; keep creation `HOLD` |
| README outranks code | Older uncertainty or route prose overrides current bytes | Prefer current code for current behavior and disclose documentation drift |
| Schema-valid equals supported | A negative envelope is treated as evidence-backed or released | Resolve evidence, policy, review, release, and correction state |
| Scaffold equals membrane | Three ABSTAIN routes are called a complete governed API | Preserve bounded maturity and graduation gates |
| Link cleanup equals deletion authority | Internal links are changed, then the pointer is removed without external closure | Require accepted migration, consumer inventory, and rollback |
| Git state equals KFM publication | Merge or release badge is treated as public truth | Keep repository delivery separate from governed publication |

[Back to top](#top)

---

<a id="6-verification-checklist"></a>
<a id="7-rollback--removal"></a>

## 8. Validation, correction, and rollback

### 8.1 Validation for this pointer

A documentation change to this file should verify:

- one complete `KFM_META_BLOCK_V2` and one H1;
- all legacy anchors remain available;
- every same-document fragment resolves;
- every repository-relative link points to a repository-present target at the
  proposed head;
- current route names exactly match the route registry;
- historical route names remain labeled `LINEAGE` or `PROPOSED`;
- the absent standalone atlas path is not represented as present;
- no substantive API register, DTO shape, policy, schema, route code, OpenAPI
  content, or release decision is introduced;
- UTF-8, LF line endings, final newline, no conflict markers, no tabs, and no
  trailing whitespace;
- the generated-work receipt binds the exact final Markdown bytes.

### 8.2 Correction procedure

1. Pin the affected pointer blob and repository commit.
2. Identify the stale, false, conflicted, or overbroad claim.
3. Cite the current code, contract, schema, policy, test, accepted decision,
   release record, or runtime evidence that corrects it.
4. Preserve this path and legacy anchors unless a separate migration authorizes
   otherwise.
5. Distinguish documentation correction from implementation, contract, schema,
   policy, release, or public-state work.
6. Keep unsupported behavior labeled `PROPOSED`, `UNKNOWN`, or
   `NEEDS VERIFICATION`.
7. Update the generated-work receipt for AI-authored bytes.
8. Define a transparent repository rollback and any separate public correction.

### 8.3 Documentation rollback

Before merge, close or abandon the draft pull request and branch. Branch deletion
is a separate action.

After an authorized merge, restore prior target blob
`b5bd266b1f04b2aebcd49d4f5a7d620dbad52cb1` through a transparent revert, or
issue a bounded forward correction. Do not rewrite shared history.

Restoring the prior pointer bytes would not reverse an API route, policy decision,
evidence result, release, deployment, or publication state—none is changed here.

### 8.4 Future physical removal gates

Physical removal of this file remains `HOLD` until all of the following are
verified:

- an accepted carrier and compatibility disposition;
- repository inbound links redirected and validation passing;
- external or undocumented consumer risk assessed;
- a deprecation/alias record with a concrete effective and sunset state;
- no active writer or authoritative content under the singular lane;
- correction and rollback targets recorded;
- human review of the final migration diff.

[Back to top](#top)

---

## 9. Open verification backlog

| Item | Current status | Closure evidence |
|---|---|---|
| Decide whether a standalone Master API Surface extract should exist | `HOLD` | Accepted carrier/naming decision and no duplicate-scope conflict |
| Converge `docs/atlas/` and `docs/atlases/` | `HOLD` | Consumer inventory, migration record, link closure, rollback |
| Refresh the legacy parent README | `NEEDS VERIFICATION` | Same-path repository-grounded correction or governed retirement |
| Reconcile historical API families with current route/code families | `PROPOSED` | Versioned route inventory and contract/schema crosswalk |
| Ratify ADR-0004 or choose another dynamic trust-boundary decision | `PROPOSED` | Reviewed ADR status transition and dependency closure |
| Establish caller identity, authorization, and audience vocabulary | `UNKNOWN` | Accepted contracts/policy, middleware, fixtures, tests, operational evidence |
| Wire authoritative evidence resolution | `UNKNOWN` | Request-time EvidenceRef-to-EvidenceBundle closure and negative tests |
| Wire policy, rights, sensitivity, and obligations | `UNKNOWN` | Active policy evaluation, safe reason handling, denial tests |
| Bind release, correction, freshness, and rollback state | `UNKNOWN` | Governed resolver, records, cache/client propagation, replay tests |
| Implement and prove a governed `ANSWER` path | `HOLD` | Evidence, policy, release, precision, payload, citation, and client tests |
| Adopt reason-code, HTTP-binding, versioning, and deprecation rules | `NEEDS VERIFICATION` | Accepted vocabulary/contracts, compatibility tests, consumer plan |
| Prove deployment and public parity | `UNKNOWN` | Exact build, start, health, ingress, environment, logs, and bounded client evidence |
| Name accountable owners and independent reviewers | `NEEDS VERIFICATION` | Verified assignments; CODEOWNERS alone is insufficient |

[Back to top](#top)

---

## 10. Related surfaces

### Current repository evidence

- [Canonical atlas lane](../atlases/README.md)
- [Atlas v1.1 source carrier](../atlases/domains-atlas-v1.1.md)
- [Governed API architecture boundary](../architecture/governed-api/README.md)
- [Governed API app boundary](../../apps/governed-api/README.md)
- [Current WSGI dispatcher](../../apps/governed-api/src/governed_api/main.py)
- [Exact route registry](../../apps/governed-api/src/governed_api/routes/registry.py)
- [Negative-envelope builder](../../apps/governed-api/src/governed_api/stub.py)
- [Bounded route tests](../../apps/governed-api/tests/test_abstain_routes.py)

### Meaning, shape, and validation

- [`RuntimeResponseEnvelope` contract](../../contracts/runtime/runtime_response_envelope.md)
- [Runtime response schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json)
- [Runtime response validator](../../tools/validators/validate_runtime_response_envelope.py)

### Placement and review

- [Accepted Directory Rules v2 adoption](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules v2 bytes](../doctrine/directory-rules.md)
- [Proposed Governed API ADR](../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md)
- [CODEOWNERS review routing](../../.github/CODEOWNERS)

[Back to top](#top)

---

## 11. Change history and non-effects

| Version | Date | Change |
|---|---|---|
| v1 | 2026-05-25 | Initial corpus-grounded deprecated pointer with proposed canonical targets and historical six-family redirects. |
| v2.0 | 2026-08-22 | Current-repository reconciliation: records the absent standalone target, accepted Directory Rules authority, current atlas-lane conflict, exact three-route negative scaffold, RuntimeResponseEnvelope stack, held removal, and legacy anchor compatibility. |

This update does **not**:

- create `docs/atlases/master-api-surface.md`;
- add, remove, or rename an API route;
- accept ADR-0004;
- authenticate or authorize a caller;
- resolve evidence or evaluate policy;
- issue an `ANSWER`;
- create or mutate a contract, schema, fixture, test, policy, review record,
  evidence bundle, release manifest, correction notice, or rollback card;
- move or delete the singular atlas lane;
- change a client, cache, deployment, runtime, or repository setting;
- release, deploy, promote, publish, merge, or approve itself.

---

**Current document status:** deprecated compatibility pointer · **Same-path
placement:** `PLACE` · **Standalone atlas carrier:** absent / creation `HOLD` ·
**Current executable route surface:** three schema-shaped
`ABSTAIN / NOT_IMPLEMENTED` GET routes · **Governed ANSWER and public
deployment:** `HOLD` / `UNKNOWN`

[Back to top](#top)
