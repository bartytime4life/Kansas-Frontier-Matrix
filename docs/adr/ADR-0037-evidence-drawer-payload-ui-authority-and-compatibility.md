<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0037
adr_id: ADR-0037
title: "ADR-0037 — Keep EvidenceDrawerPayload authority in the UI family"
type: adr
version: v1.0
status: proposed
owners:
  - "NEEDS VERIFICATION — UI contract steward"
owner_status: "CODEOWNERS routes this record to @bartytime4life; routing is not stewardship assignment, review evidence, decision quorum, or acceptance authority"
reviewers_required:
  - Architecture steward
  - Docs steward
  - UI contract steward
  - Evidence contract steward
  - Schema steward
  - Migration and compatibility reviewer
created: 2026-08-26
updated: 2026-08-26
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: Record the proposed EvidenceDrawerPayload object-family authority and compatibility decision without independently implementing, accepting, releasing, deploying, or publishing it.
current_path: docs/adr/ADR-0037-evidence-drawer-payload-ui-authority-and-compatibility.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0eb7a527cb2157504a5a03a9d024a4127fc5e45c
  target_prior_blob: null
  adr_index_blob: 8f90c75e662918f8062c4a9d139b19f268295c55
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  ui_contract_blob: 412a0a86c85c98748ac08e263a94c7eaac760c04
  evidence_contract_blob: 8da00be879a60923fe1af6e3475797f329a65e97
  ui_schema_blob: 4eefa03cffd7d5b97a24df0daf250bc31f7137ca
  evidence_schema_blob: 662396d418be3a258c15ab7923a4186184ec2136
  runtime_schema_blob: 952992e72b89b93e4d8f55eceb85d9cfd9e0299a
  convergence_validator_blob: f72ac15805bccd5f33a068f3c071d96099a20d73
  convergence_tests_blob: 3f8d99e24be679bcaa4994414fac260f75a87370
  convergence_workflow_blob: a7aeedc59f6117a415676b3216552353d7f525ad
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/evidence-drawer.md
  - contracts/ui/evidence_drawer_payload.md
  - contracts/evidence/evidence_drawer_payload.md
  - schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json
  - schemas/contracts/v1/runtime/evidence_drawer_payload.schema.json
  - tools/validators/validate_evidence_drawer_schema_convergence.py
  - tests/validators/test_evidence_drawer_schema_convergence.py
  - migrations/schema/README.md
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3368
tags: [kfm, adr, evidence-drawer, ui, evidence, schemas, compatibility, migration, M02]
notes:
  - "This record begins proposed; file presence, a commit, a pull request, a merge, or an index row does not accept it."
  - "This decision packet changes no contract, schema, validator, fixture, consumer, policy, release, deployment, publication, source, or repository setting."
  - "Dependent convergence remains a separate post-acceptance migration change under DIR-AUTH-004."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0037 — Keep `EvidenceDrawerPayload` authority in the UI family

> **Proposed decision.** KFM will keep the public-safe `EvidenceDrawerPayload` semantic contract at `contracts/ui/evidence_drawer_payload.md` and its one canonical machine shape at `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`; evidence-, runtime-, and domain-family siblings will become read-only compatibility projections after this ADR is accepted.

> [!IMPORTANT]
> **This ADR is proposed.** It is not binding until this record and the canonical index carry a synchronized, reviewed acceptance transition. Under `DIR-AUTH-004`, no dependent contract or schema migration may use this proposal as authority.

> [!NOTE]
> **Non-effects.** This record does not change the payload field set, migrate consumers, activate a source, read live data, weaken policy or sensitivity controls, release, deploy, promote, publish, or change repository settings.

**Quick navigation:** [Status](#1-status-and-authority) · [Evidence](#2-evidence-boundary) · [Context](#3-context) · [Decision](#4-decision) · [Consequences](#5-consequences-and-risks) · [Alternatives](#6-alternatives-considered) · [Implementation](#7-implementation-migration-and-compatibility) · [Validation](#8-validation-and-acceptance) · [Rollback](#9-rollback-correction-and-supersession) · [Sensitivity](#10-security-rights-sensitivity-and-sovereignty) · [Open work](#11-open-questions-and-verification-backlog) · [References](#12-evidence-and-references) · [History](#13-change-history)

---

## 1. Status and authority

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0037` — proposed addition to [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0037-evidence-drawer-payload-ui-authority-and-compatibility.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` — not binding |
| **Decision class** | Authority-changing object-family placement and compatibility decision |
| **Decision scope** | `EvidenceDrawerPayload` semantics, machine-shape home, and sibling compatibility posture only |
| **Primary responsibility** | UI public-safe projection semantics; schema authority remains a separate machine-shape responsibility |
| **Required reviewers** | Architecture, docs, UI contract, evidence contract, schema, and migration/compatibility review functions |
| **Governing authority** | Accepted ADR-0029 and its pinned Directory Rules v2 bytes |
| **Implementation maturity** | `PARTIAL / CONFLICTED`: one closed executable UI profile; two permissive family anchors; mixed domain projections |
| **Delivery state** | Proposed record; draft-PR ceiling |
| **Publication effect** | None |
| **Supersedes** | None |
| **Superseded by** | None |
| **Rollback target for this document** | Remove the unaccepted record and synchronized index entry |

### 1.1 State separation

| Axis | Current state | Evidence |
|---|---|---|
| ADR lifecycle | `proposed` | This record and canonical index row |
| Truth posture | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` per claim | Pinned evidence in §2 |
| Implementation maturity | `PARTIAL / CONFLICTED` | Sixteen schema paths with three incompatible shape postures |
| KFM lifecycle/release | Not applicable; no payload instances or release objects change | Scope boundary |
| Hosted validation | `PENDING` until an exact PR head runs | Pull-request checks |

### 1.2 Scope

**In scope**

- Select the UI family for public-safe drawer-payload meaning and shape.
- Classify evidence, runtime, and domain siblings as compatibility projections.
- Define the post-acceptance migration order, validation, correction, and rollback boundaries.

**Out of scope / explicitly unchanged**

- The current field set, profile constant, outcome vocabulary, or trust-state semantics.
- `EvidenceBundle`, `EvidenceRef`, citation validation, policy, review, release, correction, or proof authority.
- Live API composition, source admission, data promotion, deployment, release, or publication.

[Back to top](#top)

---

## 2. Evidence boundary

The repository was inspected at `main@0eb7a527cb2157504a5a03a9d024a4127fc5e45c`. The intervening merge after the initial scan changed only `apps/workers/src/correction_worker/README.md`; no Evidence Drawer or ADR control-plane evidence changed. No open pull request or branch named for `ADR-0037` was returned by the connected GitHub searches at the repinned checkpoint.

| Evidence surface | Truth label | Current observation | What it proves—and does not prove |
|---|---|---|---|
| Accepted ADR-0029 and Directory Rules blob `fd49a0b…` | `CONFIRMED` | Object-family owner changes require an accepted ADR; dependent migration follows acceptance | Governs ordering; does not select this family by itself |
| `contracts/ui/evidence_drawer_payload.md` | `CONFIRMED` | Bounded public-safe projection contract with fixtures, validator, and Explorer consumer links | Strong current semantic candidate; still marked proposed |
| `contracts/evidence/evidence_drawer_payload.md` | `CONFIRMED / CONFLICTED` | Expanded sibling semantics are explicitly `PATH-NEEDS-REVIEW` | Preserves evidence-boundary reasoning; does not establish sole authority |
| UI schema blob `4eefa03c…` | `CONFIRMED` | Closed Draft 2020-12 object: 11 declared top-level properties, 10 required fields, `additionalProperties: false` | Executable public-safe profile; not release or acceptance evidence |
| Evidence schema blob `662396d4…` | `CONFIRMED / CONFLICTED` | Empty permissive object with no contract link and `additionalProperties: true` | Competing writable shape scaffold, not an implemented profile |
| Runtime schema blob `952992e7…` | `CONFIRMED / CONFLICTED` | Empty permissive object with no contract link and `additionalProperties: true` | Competing writable shape scaffold, not an implemented profile |
| Thirteen domain schema siblings | `CONFIRMED / PARTIAL` | Six reference the UI schema; seven retain local permissive `id`-only scaffolds | Migration inventory; not evidence of external consumer closure |
| Exact-path reference inventory | `CONFIRMED` | Excluding the ignored generated-receipt archive, the UI schema path appears in 61 repository files; evidence in 7; runtime in 3 | Current documentation, validation, and implementation reference gravity—not a verified consumer count; external consumers remain `UNKNOWN` |
| UI fixtures, validator, Explorer adapter, and tests | `CONFIRMED` | The UI path has valid/invalid fixtures, a no-network validator, a fail-closed adapter, and tests | Current executable behavior; not production deployment proof |
| Convergence validator/workflow | `CONFIRMED / PARTIAL` | Checks parseability, draft, IDs, and three anchors but intentionally leaves placement `NEEDS_REVIEW` | Provides a migration enforcement seam after acceptance; currently does not prevent permissive duplicates |
| GitHub milestone issue #3368 | `CONFIRMED` | M02 requests a conflict-and-coverage matrix and one reversible slice | Coordinates work; does not accept this decision |

### 2.1 Current schema conflict matrix

| Schema class | Count | Current shape | Current disposition |
|---|---:|---|---|
| UI public-safe profile | 1 | Closed, fielded, fixture-backed | `PROPOSED` canonical target |
| Evidence-family anchor | 1 | Empty and permissive | `HOLD` until acceptance; then compatibility projection |
| Runtime-family anchor | 1 | Empty and permissive | `HOLD` until acceptance; then compatibility projection |
| Domain profiles already referencing UI | 6 | `$ref` compatibility projection | Preserve and normalize after acceptance |
| Domain-local permissive scaffolds | 7 | Local `id`-only shape, `additionalProperties: true` | `HOLD` until acceptance; then migrate to UI reference |

The six current UI references are atmosphere, fauna, geology, hydrology, roads-rail-trade, and soil. The seven local scaffolds are agriculture, archaeology, flora, habitat, hazards, people-dna-land, and settlements-infrastructure.

[Back to top](#top)

---

## 3. Context

`EvidenceDrawerPayload` is a public trust-surface projection, not evidence closure. The working UI profile already validates and renders finite outcomes, citations, limitations, trust state, and bounded negative/correction history without reading lifecycle stores or resolving evidence in the browser.

The same object-family filename also exists under evidence, runtime, and all thirteen domain schema lanes. Those siblings do not form a coherent compatibility system: two root-family anchors and seven domain profiles accept arbitrary fields, while six domains already reference the closed UI profile. The result violates the single-definition direction in `DIR-SCOPELANE-004` and leaves aliases more permissive than the candidate target, contrary to `DIR-COMPAT-002`.

Current implementation gravity favors the UI family, but repository convention alone is not authority. Directory Rules §2.3 classifies an object-family owner change as ADR work, §2.2 prohibits an unaccepted ADR from authorizing dependent migration in the same batch, and §18 requires decision-first migration with compatibility, validation, correction, and rollback evidence.

### 3.1 Decision drivers

- **One semantic owner and one machine shape** — shared object families must not evolve independently by domain or responsibility lane.
- **Preserve working fail-closed behavior** — the closed UI profile, fixtures, validator, and Explorer consumer are the only complete executable chain found.
- **Keep evidence authority upstream** — the drawer projects EvidenceBundle support and must not become evidence closure.
- **Bound compatibility** — retained paths must be no more permissive or authoritative than the selected target.
- **Reversibility** — current paths and IDs remain addressable until producer/consumer closure is proven.

### 3.2 Non-goals

- Redesign the drawer payload or add fields.
- Decide EvidenceBundle, policy, release, or correction schemas.
- Delete historical paths or claim external consumer closure.
- Treat passing tests, an ADR merge, or a schema reference as release approval.

[Back to top](#top)

---

## 4. Decision

> **Decision:** KFM will keep `EvidenceDrawerPayload` as a UI-family public-safe projection: `contracts/ui/evidence_drawer_payload.md` owns its semantic interface and `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` owns its machine shape. Every evidence-, runtime-, and domain-family schema with that object-family name becomes a read-only compatibility projection to the UI schema after acceptance; the evidence-family contract path becomes a compatibility boundary note pointing to the UI contract while retaining EvidenceBundle/EvidenceRef separation.

### 4.1 Normative rules

1. **MUST** keep all new semantic writes for this object family in `contracts/ui/evidence_drawer_payload.md`.
2. **MUST** keep all new machine-shape writes in `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`.
3. **MUST** preserve `EvidenceBundle`, `EvidenceRef`, policy, review, release, correction, and proof as upstream or adjacent authorities; drawer content may reference them but does not own them.
4. **MUST** make every retained evidence, runtime, or domain schema path a reference-only compatibility profile with a unique retained `$id`, canonical-target metadata, and no independently editable local fields.
5. **MUST NOT** make an alias more permissive, public, mutable, or authoritative than the UI target.
6. **MUST NOT** perform the dependent migration until this ADR is accepted and the implementation base is repinned.
7. **SHOULD** retain old paths indefinitely when external-consumer closure cannot be proven; deletion is not required for convergence.
8. **MAY** preserve domain-specific presentation behavior in app code or separate domain contracts, but it may not redefine `EvidenceDrawerPayload` shape.

### 4.2 Responsibility and placement

| Artifact | Authority owner | Candidate path | Rules | Outcome after acceptance |
|---|---|---|---|---|
| Public-safe projection semantics | UI contract responsibility | `contracts/ui/evidence_drawer_payload.md` | `DIR-SIGNATURE-001`, `DIR-AUTHROOT-001`–`003` | `PLACE` |
| Canonical machine shape | Schema responsibility | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` | `DIR-AUTHROOT-001`, `DIR-SCOPELANE-004` | `PLACE` |
| Evidence-family semantic sibling | Compatibility documentation | `contracts/evidence/evidence_drawer_payload.md` | `DIR-COMPAT-001`–`003` | `MIGRATE` to read-only boundary note |
| Evidence/runtime schema siblings | Compatibility schema profiles | Existing paths | `DIR-COMPAT-001`–`002`, `DIR-MIGRATE-001`–`004` | `MIGRATE` to reference-only profiles |
| Thirteen domain schema siblings | Domain-scoped compatibility profiles | Existing paths | `DIR-SCOPELANE-004`, `DIR-COMPAT-001`–`002` | `MIGRATE` or normalize to references |
| Proposed ADR | Human decision record | This file | `DIR-AUTH-004` | `PLACE` as proposed, no implementation authority |

### 4.3 Non-effects

This decision does not:

- accept the current payload content as released or immutable;
- make the UI a source, evidence, policy, review, or release authority;
- permit browser access to RAW, WORK, QUARANTINE, canonical/internal, proof, or unreleased stores;
- authorize deletion, source activation, deployment, promotion, publication, or repository-settings changes; or
- infer review from CODEOWNERS routing.

[Back to top](#top)

---

## 5. Consequences and risks

### 5.1 Positive consequences

- One working public-safe profile becomes the only shape writer.
- Evidence and runtime boundaries remain explicit without parallel permissive schemas.
- Domain schemas converge on shared shape while retaining stable profile paths and IDs.
- The existing convergence validator can graduate from inventory-only checks to rejecting local shape authority.

### 5.2 Negative consequences and costs

- Acceptance and implementation require separate changes.
- Unknown external consumers may rely on permissive siblings; retained reference paths reduce but cannot eliminate that risk.
- Seven domain scaffolds and two family anchors need coordinated migration and negative tests.
- Documentation that currently says placement is unresolved must be updated after acceptance.

### 5.3 Risk ledger

| Risk | Likelihood / impact | Mitigation | Residual risk / owner |
|---|---|---|---|
| Hidden consumer depends on arbitrary alias fields | Unknown / high | Retain paths and `$id`s; inventory repository consumers; use reference-only aliases; no deletion | External-consumer closure remains `UNKNOWN`; schema/migration review |
| Migration silently weakens public safety | Low / high | Canonical closed schema, valid/invalid fixture parity, fail-closed validator and Explorer tests | UI/schema review |
| Evidence semantics are lost during tombstoning | Medium / medium | Preserve boundary rules and link to EvidenceBundle/EvidenceRef authorities; review exact diff | Evidence contract review |
| Rollback recreates permissive writers | Medium / high | Forward-fix aliases; never restore parallel writable shape as rollback | Migration reviewer |
| ADR is mistaken for acceptance or implementation | Medium / high | Proposed status, synchronized index, explicit two-change rule and non-effects | Architecture/docs review |

[Back to top](#top)

---

## 6. Alternatives considered

### 6.1 Selected option — UI authority with retained compatibility projections

- **Summary:** Keep the complete public-safe UI profile and convert sibling paths to references after acceptance.
- **Why selected:** It matches current executable consumers, is closed and fixture-backed, preserves evidence boundaries, and supports dual-read/single-write compatibility without deletion.

### 6.2 Evidence-family canonical shape

- **Summary:** Move the fielded UI shape to `schemas/contracts/v1/evidence/` and make UI a projection alias.
- **Why rejected:** The drawer is presentation projection rather than evidence closure, and no working evidence-family schema, validator, fixtures, or consumer chain exists. This would migrate the only working chain without a demonstrated benefit.

### 6.3 Split evidence payload and UI payload into independently evolving objects

- **Summary:** Treat similarly named evidence and UI objects as separate schemas.
- **Why rejected:** Current paths and prose use the same stable object-family name without a versioned semantic split. Independent evolution would preserve ambiguity and parallel authority.

### 6.4 Leave placement unresolved

- **Summary:** Continue inventory-only checks and permissive scaffolds.
- **Why rejected:** Seven domain stubs and two family anchors remain more permissive than the working UI profile, so drift can expand while M02 remains blocked.

[Back to top](#top)

---

## 7. Implementation, migration, and compatibility

> [!IMPORTANT]
> **Decision and implementation are separate transitions.** Acceptance must occur first. The implementation change then repins `main`, rechecks overlap, and cites the accepted ADR; this proposal cannot authorize its own migration.

### 7.1 Ordered change sequence

| Order | Change | Dependency | Review boundary | Reversible? |
|---:|---|---|---|---:|
| 1 | Record this proposed ADR and synchronized inventory updates | Current accepted doctrine | Decision proposal review | yes |
| 2 | Transition ADR and index together after explicit review | Acceptance evidence from required functions | Status review | yes |
| 3 | Add a schema-migration packet and convert semantic/schema siblings | Accepted ADR; repinned base; renewed consumer inventory | Contract/schema/migration review | yes, by forward fix |
| 4 | Graduate convergence validator, tests, workflow summary, and current docs | Canonical/alias bytes in the same implementation change | Validation/docs review | yes |
| 5 | Retire any path only after zero-writer, zero-consumer, and link-closure evidence | Verified exit criteria | Separate destructive review | no immediate deletion proposed |

### 7.2 Old-to-new mapping

| Current surface | Post-acceptance role | Identity and write rule |
|---|---|---|
| `contracts/ui/evidence_drawer_payload.md` | Canonical semantic contract | Sole semantic writer |
| `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` | Canonical shape | Sole shape writer; preserve current `$id` and profile constant unless separately versioned |
| `contracts/evidence/evidence_drawer_payload.md` | Read-only compatibility and evidence-boundary note | No duplicated field list or independent semantics |
| Evidence/runtime schema paths | Compatibility projections | Retain path and unique `$id`; `$ref` UI; no local shape fields |
| Thirteen domain schema paths | Compatibility projections | Retain path and unique `$id`; `$ref` UI; no domain-local payload fields |

Compatibility is dual-read/single-write: consumers may resolve retained paths, but new semantic and shape writes go only to the UI family. The compatibility window remains open until repository and known external consumers are closed; an unknown external inventory favors retention over deletion.

### 7.3 Direct dependency closure for the implementation change

| Artifact | Why directly required | Planned home | Validation |
|---|---|---|---|
| Schema migration packet | Pins old/new identities, consumers, compatibility, and recovery | `migrations/schema/` under its existing lane contract | Parse and migration review |
| Evidence boundary note | Removes competing semantics without losing evidence separation | Existing evidence contract path | Metadata, link, and semantic review |
| Fifteen compatibility schemas | Eliminates permissive/local shape authority | Existing evidence/runtime/domain paths | Meta-schema, `$ref` resolution, no-local-shape negative checks |
| Convergence validator/tests | Prevents recurrence | Existing validator and test paths | Positive and negative pytest coverage |
| Current workflow summary | Reports the accepted convergence posture accurately | Existing read-only workflow | Workflow security and hosted run |
| Consumer and docs updates | Removes stale `PATH-NEEDS-REVIEW` statements after acceptance | Existing current docs only | Link/metadata/docs checks |
| Paired recovery record or reviewed forward-fix plan | Prevents rollback to two writers | Existing migration recovery lane | Recovery review |

### 7.4 Deferred work

- Payload-field changes or a new profile version.
- Live governed-API composition and production adoption.
- Physical path deletion or compatibility retirement.
- External consumer verification beyond accessible repository evidence.

[Back to top](#top)

---

## 8. Validation and acceptance

A passing check proves only its declared scope. It does not accept this ADR or prove implementation, policy, release, deployment, or publication.

### 8.1 Checks for this proposal

| Check / inspection | Scope | Initial state |
|---|---|---|
| `python tools/validators/validate_adr_index.py` | ADR identity/index coherence | To run on proposal head |
| `python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers` | ADR validator negative paths | To run on proposal head |
| Evidence Drawer schema audit and focused tests | Confirm pinned baseline remains unchanged | Baseline `PASS`; rerun on proposal head |
| Exact-path and schema-shape inventory | Consumer/conflict matrix | `PASS` for repository snapshot |
| Open PR and branch search | Collision/overlap | No `ADR-0037` or open EvidenceDrawerPayload PR returned at proposal start |
| Hosted checks | Exact pull-request head | `PENDING` |

### 8.2 Acceptance criteria

| Criterion | Required evidence | Current state | Reviewer function |
|---|---|---|---|
| Decision is singular and unambiguous | Reviewed directive and scope | `PROPOSED` | Architecture |
| Current conflict is pinned | Blob identities and reproducible inventory | `CONFIRMED` | Docs/schema |
| UI/evidence boundary is preserved | Contract review | `NEEDS VERIFICATION` | UI and evidence |
| Compatibility and unknown consumers are handled | Reviewed retained-path plan | `NEEDS VERIFICATION` | Schema/migration |
| Security and sensitivity posture is not weakened | Closed-profile and no-store-read review | `NEEDS VERIFICATION` | UI/security/policy as applicable |
| Required reviewers acted | Explicit review evidence, not routing alone | `HOLD` | Named review functions |
| ADR and canonical index agree | Validator pass | `PENDING` | Docs/architecture |
| Dependent implementation remains separate | No contract/schema/validator migration in this proposal | `CONFIRMED` by changed-file review | Architecture |

### 8.3 Post-acceptance verification

- Reproduce the 16-schema inventory at the new base.
- Verify all 15 noncanonical profiles resolve to the UI schema and define no local shape.
- Re-run schema meta-validation, UI fixture validator, Explorer tests, admission tests, convergence tests, docs controls, workflow security, and repository topology.
- Record introduced versus inherited findings and keep `SKIPPED` or `NOT RUN` distinct from `PASS`.

[Back to top](#top)

---

## 9. Rollback, correction, and supersession

### 9.1 Proposal rollback

Before acceptance, revert this new record and its synchronized inventory-summary edits, then rerun ADR validation. No runtime or schema rollback applies because this proposal changes no dependent implementation.

### 9.2 Post-acceptance implementation recovery

- **Trigger conditions:** unresolved `$ref`, valid fixture rejection, invalid fixture acceptance, consumer regression, leaked fields, lost evidence boundary, or an alias becoming more permissive than the target.
- **Recovery posture:** preserve the canonical UI writer and forward-fix the compatibility projection or consumer. Do not restore empty permissive schemas or independent semantic writers.
- **Compatibility after recovery:** retain old paths and IDs; keep writes on the UI target.
- **Released references:** any future released artifact impact requires separate correction, withdrawal, cache, graph, index, and release review. None is authorized here.

### 9.3 Supersession

This ADR supersedes no numbered record. A later reversal requires an accepted successor with reciprocal source/index links and a migration plan that does not recreate parallel authority.

[Back to top](#top)

---

## 10. Security, rights, sensitivity, and sovereignty

| Concern | Applies? | Required control or reviewer | Evidence |
|---|---:|---|---|
| Public trust-surface disclosure | Yes | Preserve closed fields, finite outcomes, HTTPS citations, and fail-closed parsing | UI schema, fixtures, validator, Explorer tests |
| Direct lifecycle-store access | Yes | Browser must not read RAW, WORK, QUARANTINE, internal/canonical, proof, or unreleased stores | Current adapter/test boundary; Directory Rules |
| Rights, license, or redistribution | Indirect | Keep policy and release state upstream; this change moves no data | Contract boundary |
| Archaeology, rare species, infrastructure, living-person, DNA, or exact harmful location | Potential through domain use | No domain alias may add local fields or weaken the public-safe target; qualified policy/domain review remains upstream | Closed canonical target; no payload instances in scope |
| Secrets or credentials | No | No external endpoint, credential, or live payload belongs in the packet | Changed-file review |

Unknown high-risk handling returns `HOLD` or `DENY`; path convergence cannot make sensitive content public-safe.

[Back to top](#top)

---

## 11. Open questions and verification backlog

| Item | Status | Next evidence | Blocks |
|---|---|---|---|
| Required reviewer identities beyond current CODEOWNERS route | `NEEDS VERIFICATION` | Explicit review participation | Acceptance |
| External consumers of evidence/runtime/domain paths | `UNKNOWN` | Owner-supplied inventory or observed integration evidence | Physical retirement, not retained-path convergence |
| Exact schema migration and recovery record filenames | `NEEDS VERIFICATION` | Apply current migration-lane rules at post-acceptance base | Implementation |
| Whether any domain needs a separately named wrapper object | `NEEDS VERIFICATION` | Domain contract evidence with distinct semantics and identity | Separate future ADR or versioned contract; does not justify local `EvidenceDrawerPayload` fields |
| Hosted exact-head checks | `PENDING` | GitHub Actions results | Proposal delivery assessment |

Durable coordination remains in [M02 issue #3368](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3368).

[Back to top](#top)

---

## 12. Evidence and references

### 12.1 Repository evidence ledger

| Evidence | Immutable identity at proposal base | Claim supported | Limit |
|---|---|---|---|
| `docs/doctrine/directory-rules.md` | blob `fd49a0b83e55cef52c1124281f093e263526898d` | Accepted placement and migration sequence | Does not select the target |
| `docs/adr/INDEX.md` | blob `8f90c75e662918f8062c4a9d139b19f268295c55` | `ADR-0037` was unassigned at base | Later work must recheck |
| UI/evidence contracts | blobs `412a0a86…` / `8da00be8…` | Conflicting semantic-home posture | Proposals, not acceptance evidence |
| UI/evidence/runtime schemas | blobs `4eefa03c…` / `662396d4…` / `952992e7…` | Closed UI versus permissive siblings | Repository bytes only |
| Convergence validator/tests/workflow | blobs `f72ac158…` / `3f8d99e2…` / `a7aeedc5…` | Inventory-only current enforcement | Does not resolve placement |
| `main` | commit `0eb7a527cb2157504a5a03a9d024a4127fc5e45c` | Complete proposal evidence checkpoint | No production/runtime inspection |

### 12.2 Governing decisions and doctrine

- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md), especially `DIR-AUTH-004`, `DIR-SIGNATURE-001`–`004`, `DIR-AUTHROOT-001`–`004`, `DIR-SCOPELANE-004`, `DIR-COMPAT-001`–`003`, and `DIR-MIGRATE-001`–`004`

### 12.3 Current implementation evidence

- [`contracts/ui/evidence_drawer_payload.md`](../../contracts/ui/evidence_drawer_payload.md)
- [`contracts/evidence/evidence_drawer_payload.md`](../../contracts/evidence/evidence_drawer_payload.md)
- [`schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`](../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json)
- [`docs/architecture/evidence-drawer.md`](../architecture/evidence-drawer.md)
- [`tools/validators/validate_evidence_drawer_schema_convergence.py`](../../tools/validators/validate_evidence_drawer_schema_convergence.py)
- [`migrations/schema/README.md`](../../migrations/schema/README.md)

[Back to top](#top)

---

## 13. Change history

| Date | Record status | Change | Evidence / PR |
|---|---|---|---|
| 2026-08-26 | proposed | Initial M02 authority and compatibility decision packet | Draft PR pending |
