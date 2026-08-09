<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-readme
title: release/ — Release Governance Root
type: readme; root-readme; canonical-release-decision-plane; drift-index
version: v2.1
status: draft; repository-grounded; canonical-root-confirmed; mixed-maturity; operational-release-hold; non-authoritative
owner: NEEDS VERIFICATION — CODEOWNERS routes /release/ to @bartytime4life; independent release authority and enforced separation of duties are not verified
created: 2026-07-03
updated: 2026-08-09
supersedes: v2.0 documentation at the same path; no release, promotion, correction, withdrawal, rollback, signing, deployment, publication, data, policy, contract, schema, or runtime state is superseded
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: "release-decision-plane; candidate-is-not-release; promotion-is-state-transition; no-payloads; no-policy-source; append-only; audit-bound; cite-or-abstain; correction-aware; withdrawal-aware; rollback-aware"
owning_root: release/
responsibility: explain and index release decisions without becoming a release decision, proof, receipt, policy, schema, data payload, generated output, or publication authority
truth_posture: >-
  CONFIRMED current same-path README, accepted Directory Rules v2 placement law,
  active root projection, current direct-child inventory, bounded fixture-first
  ReleaseManifest, PromotionDecision, ReviewRecord, A-G promotion-gate,
  RollbackCard, and Rego validation surfaces, and current workflow holds /
  PROPOSED release objects and inactive profiles that have not crossed governed
  adoption or operational gates / CONFLICTED root policy source, domain-first,
  singular, generic, and empty-scaffold lanes / UNKNOWN production assembly,
  authenticated release authority, signing custody, operational promotion,
  rollback, invalidation, correction propagation, and public parity /
  NEEDS VERIFICATION named stewards, accepted profiles, consumer closure,
  ruleset coupling, hosted checks, external storage, and first governed release
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 9c080014926e6f3ba4dc630eaf7a615fff46c7fc
  prior_blob: 0752610b1df6d11143158f6f162f65ecd650e6a6
  release_tree: 210ccf37b9f90986590a3e0995a0eeda7f758042
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_decision: ADR-0029 accepted
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  makefile_blob: 4abc7f941ce25d7d14703e87e387cef6e96d1592
  direct_child_directories: 18
  root_rego_files: 3
  open_prs_touching_target: 0
related:
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../control_plane/root_registry.yaml
  - ../.github/CODEOWNERS
  - ../.github/workflows/release-dry-run.yml
  - ../.github/workflows/promotion-gate.yml
  - ../.github/workflows/rollback-drill.yml
  - ../contracts/release/
  - ../schemas/contracts/v1/release/
  - ../policy/release/
  - ../data/receipts/
  - ../data/proofs/
  - ../data/published/
notes:
  - "The first twelve H2 sections implement the adopted Directory Rules v2 ROOT_FULL contract in exact order."
  - "make publish-check is bounded fixture validation; make release-dry-run remains a TODO-only marker."
  - "This revision changes this README and its generated provenance receipt only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="release-root"></a>

# `release/` — Release Governance Root

> **One-line purpose.** `release/` owns append-only decisions that authorize, correct, withdraw, supersede, or roll back KFM releases; it does not own published payloads, policy source, evidence, proofs, receipts, schemas, generated output, or runtime publication.

> [!IMPORTANT]
> **Release governance is not publication.** A candidate, review, valid schema, manifest, promotion result, signature packet, correction notice, rollback card, workflow result, pull request, merge, or GitHub release does not by itself create KFM `PUBLISHED` state. Released public-safe carriers belong under [`data/published/`](../data/published/) only after applicable evidence, policy, validation, accountable review, decision, correction, and rollback gates are satisfied.

> [!CAUTION]
> **Repository maturity is mixed.** Fixture-first validators and a bounded A–G readiness proof exist. Candidate assembly, authenticated review, live policy and evidence evaluation, attestation verification, release mutation, rollback execution, alias verification, and correction propagation remain held or unverified.

> [!WARNING]
> **Placement drift is visible, not normalized.** Adopted Directory Rules v2 deny policy source under `release/`, require object-family-first lanes, and define canonical collection spellings. Existing root Rego files, domain-first directories, singular or generic lanes, and empty scaffolds remain migration candidates or holds.

**Navigate:** [purpose](#purpose) · [authority](#authority-level) · [status](#status) · [validation](#validation) · [lanes](#current-lane-index) · [workflow holds](#workflow-readiness-boundaries) · [states](#release-state-model) · [open verification](#open-verification) · [rollback](#maintenance-correction-and-rollback)

## Purpose

`release/` is the canonical KFM **release decision plane**. It makes transitions into, within, or away from released state inspectable and reversible by binding stable identity, immutable artifact versions, evidence, validation, policy, accountable review, finite decisions, manifests, signatures, correction or withdrawal lineage, and rollback targets.

It must not infer approval from folder movement, badges, generated prose, workflow success, pull-request or merge state, mutable aliases, map visibility, or model output. This README is a boundary contract; it creates no release decision and upgrades no child lane from proposed, fixture-only, placeholder, or held status.

[Back to top](#top)

<a id="authority-level"></a>
<a id="status--authority"></a>
<a id="placement-basis"></a>

## Root class and authority owner

| Field | Current bounded result |
|---|---|
| Root class | **CONFIRMED canonical / ACTIVE** in [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml). |
| Responsibility | Release, correction, withdrawal, rollback, promotion, and signature decisions. |
| Allowed durable class | `release_decision`, plus this ROOT_FULL boundary README. |
| Prohibited classes | `data_instance`, `generated_output`, and `policy_rule`. |
| Exposure / mutability / retention | `internal` / `append_only` / `audit_bound`; committed records must still be safe in a public repository. |
| Placement authority | [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md), adopted byte-for-byte by [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). |
| GitHub review route | [`.github/CODEOWNERS`](../.github/CODEOWNERS) routes `/release/` to `@bartytime4life`; routing is not approval or a `ReviewRecord`. |
| Operational writer/decider | **NEEDS VERIFICATION.** No authenticated runtime release role, independent approver, or enforced separation-of-duties assignment is proven. |
| Publication authority | **NOT CREATED** by this root, README, workflow, fixture, PR, merge, or GitHub release. |

| Concern | Owning authority | Role of `release/` |
|---|---|---|
| Meaning and shape | [`contracts/release/`](../contracts/release/) and [`schemas/contracts/v1/release/`](../schemas/contracts/v1/release/) | References accepted profiles; does not redefine them. |
| Admissibility | [`policy/`](../policy/) | References versioned outcomes; policy source under `release/` is denied. |
| Proof and process memory | [`data/proofs/`](../data/proofs/) and [`data/receipts/`](../data/receipts/) | References support; does not duplicate it. |
| Published carriers | [`data/published/`](../data/published/) | Authorizes named releases after gates; stores no payload. |
| Tools and CI | [`tools/release/`](../tools/release/), [`tools/validators/`](../tools/validators/), and [`.github/workflows/`](../.github/workflows/) | Consumes bounded results; tool success is not authority. |

[Back to top](#top)

<a id="status"></a>

## Adoption and conformance status

| Surface | Status | Safe conclusion |
|---|---:|---|
| Root placement | `CONFIRMED` | `release/` is the active canonical release decision plane. |
| Root README | `CONFIRMED / DRAFT` | Boundary documentation exists; human review of v2.1 remains pending. |
| Canonical v2 lanes | `CONFIRMED, mixed` | Directory families exist; presence does not prove admitted instances or operational release. |
| ReleaseManifest | `PROPOSED_INACTIVE / FIXTURE_ONLY` | Legacy and strict fixture branches, validator, and grouped cases exist; no assembly or release is proven. |
| PromotionDecision | `PROPOSED / FIXTURE-VALIDATED` | Closed shape, non-empty fixtures, tests, and workflow binding exist; policy, evidence, review, and transition remain separate. |
| ReviewRecord | `PROPOSED / FIXTURE_ONLY` | Synthetic identity, authority, self-review, time, scope, subject, obligations, and hash checks exist; no accountable review record exists. |
| A–G readiness | `IMPLEMENTED, BOUNDED` | `make publish-check` runs side-effect-free fixtures with `PASS`, `ABSTAIN`, `DENY`, and `ERROR`; it emits no decision or release. |
| Shared RollbackCard | `PROPOSED / FIXTURE-VALIDATED` | Closed candidate profile, validator, and fixtures exist; generic entry and execution remain placeholders. |
| Candidate assembly | `WORKFLOW_HOLD` | No candidate payload or accepted assembly command is established. |
| Promotion / rollback execution | `WORKFLOW_HOLD` | No live support authentication, state mutation, invalidation, restoration, or publication is established. |
| Bounded Rego profile | `PROPOSED_INACTIVE` | One governed profile exists under `policy/rego/`; no general policy runtime is established. |
| Human review enforcement | `NEEDS VERIFICATION` | Required review, independent approval, ruleset coupling, and runtime authority are unproven. |
| Production parity | `UNKNOWN` | No deployed registry, production signing, operational release, dashboard, or tested recovery is claimed. |

A workflow may pass by proving that a hold remains visible and fail-closed. That is validation evidence, not proof that the held capability exists.

[Back to top](#top)

<a id="what-belongs-here"></a>
<a id="what-does-not-belong-here"></a>

## What belongs here and what is prohibited

Canonical families are object-family first and domain second:

```text
release/
├── candidates/
├── manifests/
├── promotion_decisions/
├── correction_notices/
├── withdrawal_notices/
├── rollback_cards/
├── signatures/
└── changelog/
```

**Belongs:** root and lane READMEs; candidate dossiers; immutable manifests; finite promotion decisions; correction and withdrawal notices; rollback decision cards; verified signature or attestation packets without private keys; release-level history; and domain-scoped records beneath the owning family.

**Prohibited:** lifecycle payloads; datasets, tiles, exports, or model files; receipts; proofs or EvidenceBundles; source registries; contracts; schemas; policy source or Rego; validators, tools, pipelines, connectors, apps, or runtime code; generated summaries presented as truth; placeholder instances in canonical trust collections; secrets, private endpoints, restricted payloads, harmful exact locations; and any state transition inferred from a file move.

`PLACE` describes a directory family, not every contained record. Each instance still needs admitted shape, evidence, policy, review, correction, and rollback support appropriate to its effect.

[Back to top](#top)

<a id="inputs"></a>
<a id="outputs"></a>

## Inputs, outputs, and permitted writers

| Input family | Minimum posture |
|---|---|
| Candidate | Stable identity, bounded scope, intended transition, artifact identities, current state. |
| Evidence | Resolvable `EvidenceRef -> EvidenceBundle` support where claims depend on evidence. |
| Validation / integrity | Applicable schema, contract, geometry, temporal, citation, catalog, digest, signature, and public-safety results. |
| Policy | Versioned rights, sensitivity, access, stale-state, public-safety outcome, and obligations. |
| Review / authority | Authenticated actor, current assignment, subject/scope/hash binding, reasons, obligations, time, and separation of duties. |
| Manifest / correction / rollback | Included records, prior state, public effect, notice, invalidation, successor or restoration target. |
| Signature support | Verified signature or attestation references and revocation posture; never raw key material. |

Outputs may include candidate state, manifests, decisions, correction or withdrawal notices, rollback cards, signature packets, changelog entries, and explicit hold, abstain, deny, or no-action outcomes. Released carriers remain under `data/published/`.

| Actor class | Permitted durable write | Limit |
|---|---|---|
| Candidate producer | `release/candidates/` through an admitted interface | Cannot approve, manifest, release, correct, withdraw, or roll back. |
| Authenticated release authority | Accepted decision family after applicable gates | Identity and assignment remain `NEEDS VERIFICATION`. |
| Correction / withdrawal authority | New append-only notice or decision | Cannot silently mutate prior records or payloads. |
| Rollback authority | New rollback card after target, review, policy, and invalidation checks | Writing a card does not execute restoration. |
| Publisher | Immutable `data/published/` carriers after an accepted decision | Cannot write its own release decision. |
| Contributor or AI builder | Feature-branch drafts | Cannot approve, merge, release, deploy, publish, or claim adoption. |
| Watcher, connector, pipeline, renderer, AI runtime, or public client | No release-decision writes by default | May propose candidates or correction requests only through governed interfaces. |

[Back to top](#top)

## Public exposure and sensitivity posture

The machine projection classifies `release/` as internal while the Git repository is public. Committed records must therefore be safe for public source visibility. Restricted operational details may live in governed external storage with a versioned logical record, digest, media type, rights or sensitivity labels, retention, release, correction, and rollback references.

Public clients consume governed APIs and released public-safe carriers, not this directory as a direct trust store. Redact, generalize, restrict, or omit denial detail, private reviewer notes, incident or security detail, protected locations, living-person information, DNA or genomic data, restricted cultural material, private-land detail, and source terms.

Use `HOLD`, `ABSTAIN`, or `DENY` when rights, sovereignty, consent, sensitivity, reviewer authority, public scope, or harmful precision is unresolved. Never place private keys, tokens, OIDC credentials, or recovery material here.

[Back to top](#top)

## Mutability, retention, generation, and physical storage

| Property | Rule |
|---|---|
| Mutability | Durable decisions are append-only; create successor, correction, withdrawal, supersession, or rollback records. |
| Retention | Audit-bound; preserve identity, prior state, decision basis, correction lineage, and rollback target while reliance or policy requires. |
| Generation | Generated material is never independent release authority; generated candidates declare producer, inputs, digest, and edit policy. |
| Placeholders | Canonical trust collections reject self-identified placeholder or scaffold instances. |
| Physical storage | Small public-safe records may be Git-tracked; larger or restricted records use governed external storage plus a versioned logical record. |
| Locators | URL, object key, registry tag, Git path, or mutable alias is a locator, not authority. |
| Cache / index effects | State changes name affected caches, aliases, catalogs, APIs, maps, search, graph, exports, and AI surfaces. |
| Deletion | Last resort after authority, retention, reference closure, correction, and rollback or forward-fix review. |

Current conflicts: three root `.rego` files are nonconforming policy source; two root RollbackCard JSON files are non-schema-admissible documentation placeholders; `source_role_anti_collapse/` is README plus `.gitkeep`; and domain-first children require inventory before migration.

[Back to top](#top)

<a id="validation"></a>

## Validation and negative checks

| Command or workflow | Current bounded meaning | Does not prove |
|---|---|---|
| `make validate` | Aggregate schema validators and schema or contract tests. | Complete release closure, authenticated review, promotion, rollback, or publication. |
| `make publish-check` | Fixture-only ReviewRecord and A–G promotion-gate validators plus tests. | Live evidence, policy execution, review authority, decision emission, transition, or publication. |
| `python tools/validators/release/validate_release_manifest.py --fixtures` | Validates the preserved fixture-only ReleaseManifest profile. | Candidate assembly, accepted profile authority, or release. |
| `python tools/validators/release/validate_rollback_card.py --fixtures` | Validates the bounded shared RollbackCard candidate profile. | Target authorization, rollback execution, invalidation, receipt, or restoration. |
| `make release-dry-run` | Prints `TODO: tools/release dry-run`. | Any dry run or candidate assembly. |
| `release-dry-run`, `promotion-gate`, `rollback-drill` | Read-only readiness and fixture checks with explicit holds. | Candidate, decision, receipt, proof, signature, mutation, rollback, or publication. |
| Pass 12 release-policy workflow | Tests one checksum-pinned inactive Rego profile under `policy/rego/`. | General OPA runtime, `PolicyDecision`, release, or publication. |

> [!CAUTION]
> `make release-dry-run` exits successfully after printing a TODO marker. Do not cite it as a successful dry run.

Negative cases include unresolved or stale evidence; unbound hashes; unknown rights, sensitivity, role, scope, or policy; self-review or stale review; missing authority, manifest, catalog closure, attestation, correction path, or rollback target; nondeterministic geometry or time; placeholder trust instances; policy source under `release/`; direct public access to internal stores; and any workflow, PR, map, or AI output misclassified as release authority.

[Back to top](#top)

<a id="review-burden"></a>

## Owner, reviewers, and escalation path

| Role or control | Current evidence | Status |
|---|---|---:|
| GitHub route | `/release/ @bartytime4life` in CODEOWNERS | `CONFIRMED`, routing only |
| Root-registry owner / writer | `@bartytime4life` in machine projection | `CONFIRMED`, not runtime assignment |
| Independent release steward | No verified identity or assignment | `NEEDS VERIFICATION` |
| Evidence, policy, security, privacy, correction, rollback, signing, and domain reviewers | Responsibilities are clear; assignments are not | `NEEDS VERIFICATION` |
| Required reviews and separation of duties | Not established for this task | `NEEDS VERIFICATION` |
| Runtime release authority / signing custody | No operational evidence inspected | `UNKNOWN` |

Review burden scales with effect. Documentation needs accuracy and no-loss review. Profiles need contract, schema, fixture, validator, and policy review. Decisions need authenticated authority and subject, scope, and hash binding. Correction or withdrawal needs public-effect and invalidation analysis. Rollback needs a valid target, review or signature, execution receipt, restoration verification, and forward-fix comparison.

Use `PASS` or `APPROVE_READY` for bounded validation only, `ABSTAIN` or `HOLD` for incomplete support, `DENY` for policy or invariant violations, and `ERROR` when safe evaluation cannot complete.

[Back to top](#top)

<a id="related-folders"></a>
<a id="adrs"></a>

## Governing ADRs, migrations, aliases, and canonical target

| Authority | Status | Consequence |
|---|---:|---|
| [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `ACCEPTED` | Adopts exact Directory Rules v2 bytes as the writable human placement authority. |
| [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) | Adopted exact bytes | Defines object-family-first lanes, append-only decisions, and policy-source denial. |
| [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) | `ACTIVE` projection | Classifies this root as canonical, internal, append-only, audit-bound, and release-decision-only. |
| [`ADR-0011`](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `PROPOSED` | Design evidence only; does not authorize migration. |

Canonical target: `release/`, with `manifests/`, `rollback_cards/`, `correction_notices/`, and policy source under `policy/`. No mutable `current` alias is release authority. No new root or parallel home is authorized.

Migration candidates outside this PR: singular `manifest/`; generic or plural correction and rollback lanes; domain-first children; `release/policy/`; root Rego files; generic reviews or decisions; and empty `source_role_anti_collapse/`. Each requires exact object classification, stable identity, reference and consumer repair, compatibility, validation, and rollback.

[Back to top](#top)

<a id="repo-fit"></a>
<a id="current-lane-index"></a>

## Direct-child directory map

| Outcome | Current direct children |
|---|---|
| `PLACE` family | `candidates/`, `manifests/`, `promotion_decisions/`, `correction_notices/`, `withdrawal_notices/`, `rollback_cards/`, `signatures/`, `changelog/` |
| `MIGRATE` after inventory | `manifest/`, `rollback/`, `agriculture/`, `people-dna-land/` |
| `HOLD / MIGRATE` | `correction/`, `corrections/` |
| `HOLD` | `decisions/`, `reviews/`, `policy/`, `source_role_anti_collapse/` |
| `DENY_NEW_WRITES / MIGRATE` | `hydrology_publication.rego`, `public_safe_geometry.rego`, `source_role_anti_collapse.rego` |

`PLACE` describes the family, not every contained record. `release/reviews/` has guidance and an empty Atmosphere scaffold, not an accountable review record. `source_role_anti_collapse/` owns no proven decision or consumer.

[Back to top](#top)

<a id="last-reviewed"></a>

## Last evidence review and review trigger

| Field | Value |
|---|---|
| Last evidence review | 2026-08-09 |
| Base / prior blob | `main@9c080014926e6f3ba4dc630eaf7a615fff46c7fc` / `0752610b1df6d11143158f6f162f65ecd650e6a6` |
| Release tree | `210ccf37b9f90986590a3e0995a0eeda7f758042` |
| Open target-overlap PRs | `0` at discovery |
| Result | Same-path ROOT_FULL v2.1 modernization, evidence refresh, drift visibility, and generated provenance only. |
| Effect | No path move, record, policy, schema, workflow, runtime, data, release, rollback, deployment, publication, or settings change. |
| Maximum staleness | Six months unless a trigger occurs sooner. |

Review when a direct-child path or meaning changes; a migration changes state; a fixture profile becomes accepted or operational; a candidate, review, manifest, decision, correction, withdrawal, rollback, signature, or published alias is exercised; release automation or public consumers change; steward, ruleset, or signing authority changes; or production evidence becomes available.

[Back to top](#top)

<a id="lifecycle-boundary"></a>
<a id="root-responsibilities"></a>

## Lifecycle and authority boundary

```text
PRE_RAW -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS
                                                  + PROOF
                                                  + RELEASE DECISION
                                                    -> PUBLISHED
```

`release/` owns the decision that authorizes or changes a release. `data/published/` owns the immutable release-approved carrier. Promotion emits a governed state and version and is never inferred from copying, moving, naming, workflow completion, or a mutable alias.

[Back to top](#top)

<a id="release-state-model"></a>

## Release state model

| Release-facing state | Meaning |
|---|---|
| `DRAFT` | Exists, not ready for accountable review. |
| `READY_FOR_REVIEW` | Review inputs appear complete; no release authority yet. |
| `HELD` | Evidence, validation, policy, rights, sensitivity, authority, correction, or rollback support is unresolved. |
| `READY_FOR_MANIFEST` | Reviewed candidate may support manifest preparation; not released. |
| `APPROVED` | Governed decision approves named scope; publication still needs the complete transition. |
| `RELEASED` | Governed release state is complete for a named version and scope. |
| `CORRECTED`, `SUPERSEDED`, `WITHDRAWN` | Append-only lineage changes public reliance while preserving history. |
| `NO_ACTION` | Review authorizes no state change. |

Validator, readiness, workflow, pull-request, decision, and published-carrier vocabularies must not be silently mapped to one another.

[Back to top](#top)

<a id="workflow-readiness-boundaries"></a>

## Workflow readiness boundaries

- **`release-dry-run`:** read-only assertions for candidate absence, ReleaseManifest fixtures (`4` valid and `17` invalid grouped cases), PromotionDecision and A–G readiness, and RollbackCard fixtures. The helper and Make target remain placeholders; no record or release is emitted.
- **`promotion-gate`:** read-only fail-closed doctrine and proposed-shape checks plus Gate G synthetic identity, authority, self-review, scope, subject, time, obligations, supersession, and hash binding. `release/reviews/` contains guidance and an empty Atmosphere scaffold, not accountable review records.
- **`rollback-drill`:** read-only RollbackCard fixture validation and hold assertions. Generic entry point, rollback pipeline or apply helper, published aliases, invalidation, receipts, and restoration remain held.
- **Pass 12 Rego lane:** separately governed inactive profile under [`policy/rego/`](../policy/rego/release_gate_v1.rego). It does not resolve evidence, authenticate review, emit `PolicyDecision`, or create a general runtime.

[Back to top](#top)

<a id="bounded-implemented-validation-slices"></a>

## Bounded implemented validation slices

| Slice | Confirmed evidence | Authority limit |
|---|---|---|
| ReleaseManifest fixture profile | Contract or schema metadata, strict fixture branch, grouped cases, validator, test, workflow assertions. | Fixture-only; no assembly or release. |
| PromotionDecision shape | Closed schema, non-empty fixtures, test, workflow binding. | Proposed; no live policy, evidence, review, or transition. |
| ReviewRecord projection | Validator and tests with finite outcomes and reason mapping. | Synthetic; no live actor or authority. |
| A–G promotion gate | Side-effect-free validator, fixtures, tests, Make target, read-only workflows. | Declared closure only; emits no decision. |
| Shared RollbackCard | Closed candidate profile, fixtures, validator, workflow binding. | Local consistency only; no execution. |
| Pass 12 release policy | Rego, native tests, fixtures, pinned workflow. | Inactive bounded profile; no general runtime. |

[Back to top](#top)

<a id="required-release-root-record-fields"></a>
<a id="minimal-release-root-record"></a>

## Release record minimum contract

An accepted release-decision record should bind stable ID, version, and type; finite outcome and reason codes; subject, scope, time, sensitivity, and immutable digests; evidence, validation, policy, review or authority, manifest, signature, correction, withdrawal, supersession, rollback, invalidation, and public-effect references; predecessor and successor lineage; recorded-at and actor; retention; and unresolved obligations.

A missing required field produces hold, abstain, deny, or error. It never implies completion through an empty field, filename, default allow, workflow status, or prose note. Accepted contracts and schemas outrank illustrative templates.

[Back to top](#top)

<a id="review-checklist"></a>

## Review checklist

- [ ] Canonical object-family-first lane, stable identity and version, subject, scope, time, and immutable digests are explicit.
- [ ] Evidence, validation, integrity, citation, catalog, rights, sensitivity, access, and public-safety support resolve.
- [ ] Reviewer or decider identity, authority, scope, time, subject or hash binding, obligations, and separation of duties are explicit.
- [ ] Manifest, signature, correction, withdrawal, supersession, notice, rollback, invalidation, and restoration requirements are satisfied where applicable.
- [ ] No payload, receipt, proof, source, schema, contract, policy, validator, application, or generated-output authority is duplicated here.
- [ ] No generated text, map, tile, workflow, PR, merge, GitHub release, or signature packet is used as approval by itself.
- [ ] Sensitive information is absent or handled through approved restricted storage.
- [ ] The diff is bounded, reversible, and linked to correction or rollback.

[Back to top](#top)

<a id="naming-guidance"></a>

## Naming and identity guidance

Use object-family-first and domain-second paths, registered stable IDs and versions inside records, lowercase ASCII path segments, plural collection directories, singular record filenames, canonicalized digests, and distinct path, object, display, locator, and alias identities. Dates in filenames are navigation aids, not identity or temporal truth. Never create new domain-first release homes.

[Back to top](#top)

## Compatibility and placement conflicts

| Conflict | Safe next step |
|---|---|
| `manifest/` vs `manifests/` | Inventory IDs and references, migrate with compatibility and zero-writer or consumer evidence, then retire singular lane. |
| `correction/`, `corrections/`, `correction_notices/` | Classify review, decision, notice, and domain records before migration. |
| `rollback/` vs `rollback_cards/` | Classify decisions versus execution receipts; target cards under `release/rollback_cards/`, process records under `data/receipts/rollback/`. |
| `reviews/`, `decisions/`, `promotion_decisions/` | Define accepted ReviewRecord and decision placement; do not collapse from filenames. |
| Domain-first children | Migrate each object to its owning family with sensitivity review and reference repair. |
| `release/policy/` and root Rego | Move policy source to canonical `policy/`; preserve release records as references only. |
| Empty source-role lane | Establish a real owned object and consumer or retire through governed migration. |
| Shared or domain ReleaseManifest and receipt-like profiles | Define shared-kernel and extension rules and prevent parallel writable authority. |
| Published `current` aliases | Define immutable pointer identity, rollback binding, negative tests, cache behavior, and receipts before activation. |

These are facts and work items, not permission for broad cleanup in this documentation PR.

[Back to top](#top)

<a id="open-verification"></a>

## Open verification register

1. Named release, evidence, policy, security, privacy, correction, rollback, signing, and domain authorities, plus enforced independent review.
2. Full object, reference, and consumer inventory and migration plans for every drift lane.
3. Accepted shared-kernel and domain-extension catalog for release objects and version or deprecation policy.
4. Deterministic no-write candidate assembly and operational evidence closure.
5. Accepted policy runtime, authenticated review or authority, attestation or signing, and catalog or manifest closure.
6. Side-effect-controlled promotion and publisher boundaries that cannot self-publish.
7. Rollback target selection, simulation, invalidation, execution receipts, restoration, and forward-fix fallback.
8. Correction or withdrawal propagation through catalog, API, MapLibre, search, graph, export, citations, caches, and AI.
9. Compatibility retirement, external consumers, production storage or registry, observability, incident response, retention, and recovery.
10. Current hosted exact-head checks and human adoption of this documentation revision.

[Back to top](#top)

## Definition of done

This documentation slice is complete when the exact repository, base, path, root, blob, and tree are verified; ROOT_FULL order is correct; stale claims and current children or conflicts are reconciled; identity, anchors, links, Markdown, receipt and hash closure, remote bytes, parentage, diff, draft PR, and hosted status are verified; and no unrelated behavior or authority change exists.

Operational release remains separate and requires admitted evidence, accepted contracts, schemas, policies, identities, positive and negative fixtures, deterministic bounded execution, accountable review, manifest, proof, receipt, catalog, signature, correction, and rollback closure, immutable public-safe carrier production, propagation and recovery drills, runtime, storage, and observability evidence, and separate release or publication authority.

[Back to top](#top)

<a id="maintenance-correction-and-rollback"></a>

## Maintenance, correction, and rollback

No release, promotion, correction, rollback execution, deployment, or publication is performed by this documentation change.

For documentation correction: pin current main and target; reconcile overlap; read the governing and implementation neighborhood; classify drift; make the smallest same-path edit; validate; emit provenance; push without force; and deliver one draft PR.

Before merge, close or abandon the draft PR and branch. After an authorized merge, use a transparent revert or forward-fix PR; never rewrite shared history. Reverting this README and generated receipt restores documentation bytes only, not release, policy, schema, workflow, candidate, published artifact, cache, alias, or runtime state.

Rollback target: README blob `0752610b1df6d11143158f6f162f65ecd650e6a6` at `main@9c080014926e6f3ba4dc630eaf7a615fff46c7fc`; remove the generated receipt only through the reviewed revert of the same packet.

[Back to top](#top)

## Changelog

| Version | Date | Change |
|---:|---:|---|
| v1 | 2026-07-03 | Expanded the compact root stub into release-governance guidance. |
| v2.0 | 2026-07-23 | Refreshed evidence, lane coverage, workflow holds, review limits, open verification, and rollback boundaries. |
| v2.1 | 2026-08-09 | Applied exact ROOT_FULL order; repinned evidence; corrected validation maturity; classified current children and root Rego drift; preserved release, signing, rollback, alias, and publication holds. |

[Back to top](#top)
