<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-readme
title: release/ — Release Governance Root
type: readme; root-readme; canonical-release-decision-plane; correction-withdrawal-rollback-boundary; drift-index
version: v2.1
status: draft; repository-grounded; canonical-root-confirmed; mixed-maturity; bounded-fixture-validation-confirmed; operational-release-hold; non-authoritative
owner: NEEDS VERIFICATION — CODEOWNERS routes /release/ to @bartytime4life; no independent release steward, runtime release authority, or enforced separation of duties is verified
created: 2026-07-03
updated: 2026-08-09
supersedes: v2.0 documentation at the same path; no release, promotion, correction, withdrawal, rollback, signing, deployment, publication, data, policy, contract, scheme, or runtime state is superseded
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: "repository-facing; release-decision-plane; candidate-is-not-release; promotion-is-state-transition; no-payloads; no-policy-source; append-only; audit-bound; cite-or-abstain; correction-aware; withdrawal-aware; rollback-aware"
owning_root: release/
responsibility: explain and index the release decision plane without becoming a release decision, proof, receipt, policy, schema, data payload, generated output, or publication authority
truth_posture: >-
  CONFIRMED current same-path README, accepted Directory Rules v2 placement law,
  active canonical root projection, direct-child inventory, bounded fixture-first
  ReleaseManifest, PromotionDecision, ReviewRecord, A-G promotion-gate, RollbackCard,
  and Rego validation surfaces, and current workflow holds / PROPOSED release objects
  and inactive profiles that have not crossed governed adoption or operational gates /
  CONFLICTED root-level policy source, domain-first, singular, generic, and empty-scaffold
  lanes / UNKNOWN production assembly, authenticated release authority, signing custody,
  operational promotion, rollback, invalidation, correction propagation, and public parity /
  NEEDS VERIFICATION named stewards, accepted profiles, consumer closure, ruleset coupling,
  current hosted checks, external storage, and the first governed release
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
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../control_plane/root_registry.yaml
  - ../.github/CODEOWNERS
  - ../.github/workflows/release-dry-run.yml
  - ../.github/workflows/promotion-gate.yml
  - ../.github/workflows/rollback-drill.yml
  - ../.github/workflows/pass12-release-policy-v1.yml
  - ../contracts/release/
  - ../schemas/contracts/v1/release/
  - ../policy/release/
  - ../policy/rego/release_gate_v1.rego
  - ../fixtures/release/
  - ../tools/release/
  - ../tools/validators/release/
  - ../tools/validators/promotion_gate/
  - ../tests/release/
  - ../data/receipts/
  - ../data/proofs/
  - ../data/published/
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
notes:
  - "The first twelve H2 sections implement the adopted Directory Rules v2 ROOT_FULL contract in exact order."
  - "ADR-0029 adopts the exact Directory Rules bytes even though the source document retains its historical proposal label."
  - "make publish-check is a bounded fixture-validation target; make release-dry-run remains a TODO-only marker."
  - "This revision changes this README and its generated provenance receipt only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="release-root"></a>

# `release/` — Release Governance Root

> **One-line purpose.** `release/` owns append-only decisions that authorize, correct, withdraw, supersede, or roll back KFM releases; it does not own published payloads, policy source, evidence, proofs, receipts, schemas, generated output, or runtime publication.

> [!IMPORTANT]
> **Release governance is not publication.** A candidate, review, schema-valid record, manifest, promotion result, signature packet, correction notice, rollback card, workflow result, pull request, merge, or GitHub release does not by itself create KFM `PUBLISHED` state. Released public-safe carriers belong under [`data/published/`](../data/published/) only after the applicable evidence, policy, validation, accountable review, decision, correction, and rollback gates are satisfied.

> [!CAUTION]
> **Repository maturity is mixed.** Several fixture-first validators exist and `make publish-check` executes a bounded A–G readiness proof. Candidate assembly, authenticated review, policy evaluation over live evidence, attestation verification, release mutation, rollback execution, published-alias verification, and operational correction propagation remain held or unverified.

> [!WARNING]
> **Placement drift is visible, not normalized.** Adopted Directory Rules v2 deny policy source under `release/`, require object-family-first lanes, and name canonical collection spellings. Existing root-level Rego scaffolds, domain-first directories, singular or generic lanes, and empty scaffolds remain migration candidates or holds.

**Quick navigation:** [purpose](#purpose) · [authority](#authority-level) · [status](#status) · [validation](#validation) · [lanes](#current-lane-index) · [workflow holds](#workflow-readiness-boundaries) · [states](#release-state-model) · [open verification](#open-verification) · [rollback](#maintenance-correction-and-rollback)

---

## Purpose

`release/` is the canonical KFM **release decision plane**. It makes every transition into, within, or away from released state inspectable and reversible by binding stable identity, immutable artifact versions, evidence, validation, policy, accountable review, finite decisions, manifests, signatures, correction or withdrawal lineage, and rollback targets.

It must not infer approval from folder movement, badge color, generated prose, workflow success, pull-request or merge state, mutable aliases, map visibility, or model output. This README is the root boundary contract; it creates no release decision and upgrades no child lane from proposed, fixture-only, placeholder, or held status.

[Back to top](#top)

---

<a id="authority-level"></a>
<a id="status--authority"></a>
<a id="placement-basis"></a>

## Root class and authority owner

| Field | Current bounded result |
|---|---|
| Root class | **CONFIRMED canonical / ACTIVE** in [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml). |
| Primary responsibility | Release, correction, withdrawal, rollback, promotion, and signature decisions. |
| Allowed durable artifact class | `release_decision`, plus this ROOT_FULL boundary README. |
| Prohibited artifact classes | `data_instance`, `generated_output`, and `policy_rule`. |
| Exposure, mutability, retention | `internal`, `append_only`, `audit_bound`. The repository is public, so committed records must still be safe for public source visibility. |
| Human placement authority | [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md), adopted byte-for-byte by [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). |
| GitHub review route | [`.github/CODEOWNERS`](../.github/CODEOWNERS) routes `/release/` to `@bartytime4life`; routing is not approval or a `ReviewRecord`. |
| Operational writer/decider | **NEEDS VERIFICATION.** No authenticated runtime release role, independent approver, or enforced separation-of-duties assignment is proven. |
| Publication authority | **NOT CREATED** by this root, README, CODEOWNERS, workflow, fixture, PR, merge, or GitHub release. |

| Concern | Owning authority | Role of `release/` |
|---|---|---|
| Meaning and shape | [`contracts/release/`](../contracts/release/) and [`schemas/contracts/v1/release/`](../schemas/contracts/v1/release/) | References accepted profiles; does not redefine them in records. |
| Admissibility | [`policy/`](../policy/) | References versioned outcomes; policy source under `release/` is denied. |
| Evidence, proofs, receipts | [`data/proofs/`](../data/proofs/) and [`data/receipts/`](../data/receipts/) | References support; does not duplicate it. |
| Published carriers | [`data/published/`](../data/published/) | Authorizes named releases after gates; stores no payloads. |
| Tools and CI | [`tools/release/`](../tools/release/), [`tools/validators/`](../tools/validators/), and [`.github/workflows/`](../.github/workflows/) | Consumes bounded results; tool success is not authority. |

[Back to top](#top)

---

<a id="status"></a>

## Adoption and conformance status

| Surface | Status | Safe conclusion |
|---|---:|---|
| Root placement and class | `CONFIRMED` | `release/` is the active canonical release decision plane. |
| Root README | `CONFIRMED / DRAFT` | Boundary documentation exists; human review of v2.1 remains pending. |
| Canonical v2 lanes | `CONFIRMED, mixed` | Canonical directory families exist; presence does not prove admitted instances or operational release. |
| ReleaseManifest profile | `PROPOSED_INACTIVE / FIXTURE_ONLY` | A preserved legacy branch and closed strict fixture profile, validator, and grouped cases exist; no candidate assembly or release is proven. |
| PromotionDecision profile | `PROPOSED / FIXTURE-VALIDATED` | Closed shape, non-empty valid/invalid fixtures, dedicated tests, and workflow binding exist; policy, evidence, review authority, and transition remain separate. |
| ReviewRecord projection | `PROPOSED / FIXTURE_ONLY` | Synthetic identity, authority, self-review, time, scope, subject, obligations, and hash checks exist; no accountable release review record exists. |
| A–G promotion readiness | `IMPLEMENTED, BOUNDED` | `make publish-check` executes side-effect-free fixtures with `PASS`, `ABSTAIN`, `DENY`, and `ERROR`; it emits no decision or release. |
| Shared RollbackCard profile | `PROPOSED / FIXTURE-VALIDATED` | Closed candidate-shape profile, validator, and fixtures exist; generic entry point and execution remain placeholders. |
| Candidate assembly | `WORKFLOW_HOLD` | No candidate payload or accepted assembly command is established. |
| Promotion and rollback execution | `WORKFLOW_HOLD` | No live support authentication, state mutation, invalidation, restoration, or publication is established. |
| Bounded Rego profile | `PROPOSED_INACTIVE` | One separately governed profile exists under `policy/rego/`; it does not make root Rego scaffolds conforming or create a general policy runtime. |
| Human review enforcement | `NEEDS VERIFICATION` | Required review, independent approval, ruleset coupling, and runtime authority remain unproven. |
| Production parity | `UNKNOWN` | No deployed registry, production signing, operational release, dashboard, or tested recovery is claimed. |

A workflow may pass by proving a hold remains visible and fail-closed. That is useful validation evidence, not proof that the held capability exists.

[Back to top](#top)

---

<a id="what-belongs-here"></a>
<a id="what-does-not-belong-here"></a>

## What belongs here and what is prohibited

Canonical release families are object-family first and domain second:

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

**Belongs:** root/lane boundary READMEs; candidate dossiers; immutable release manifests; finite promotion decisions; correction and withdrawal notices; rollback decision cards; verified signature/attestation packets; release-level human-readable history; domain-scoped records beneath the owning family.

**Prohibited:** lifecycle payloads; datasets, tiles, exports, or model files; receipts; proofs or EvidenceBundles; source registries; contracts; schemas; policy source or Rego; validators, tools, pipelines, connectors, apps, or runtime code; generated summaries presented as truth; placeholder instances in canonical trust collections; secrets, keys, private endpoints, restricted payloads, or harmful exact locations; and any state transition inferred from a file move.

`PLACE` applies to a directory family, not automatically to every contained record. Each instance still needs admitted shape, evidence, policy, review, correction, and rollback support appropriate to its effect.

[Back to top](#top)

---

<a id="inputs"></a>
<a id="outputs"></a>

## Inputs, outputs, and permitted writers

| Input family | Minimum posture |
|---|---|
| Candidate | Stable identity, bounded scope, intended transition, artifact identities, and current candidate state. |
| Evidence | Resolvable `EvidenceRef -> EvidenceBundle` support where release claims depend on evidence. |
| Validation and integrity | Applicable schema, contract, geometry, temporal, citation, catalog, digest, signature, and public-safety results. |
| Policy | Versioned rights, sensitivity, access, stale-state, public-safety outcome, and obligations. |
| Review and authority | Authenticated actor, current assignment, subject/scope/hash binding, reasons, obligations, time, and separation of duties. |
| Manifest, correction, withdrawal, rollback | Included records, prior state, public effect, notice, invalidation, successor or restoration target. |
| Signature support | Verified signature or attestation references and revocation posture; never raw key material. |

Outputs may include candidate state, manifests, decisions, correction/withdrawal notices, rollback cards, signature packets, changelog entries, and explicit hold/abstain/deny/no-action outcomes. Released carriers remain under `data/published/`.

| Actor class | Permitted durable write | Explicit limit |
|---|---|---|
| Candidate producer | `release/candidates/` through an admitted interface | Cannot approve, manifest, release, correct, withdraw, or roll back. |
| Authenticated release authority | Accepted decision family after applicable gates | Identity and assignment remain NEEDS VERIFICATION. |
| Correction/withdrawal authority | New append-only notice or decision | Cannot silently mutate prior records or payloads. |
| Rollback authority | New rollback card after target, review, policy, and invalidation checks | Writing a card does not execute restoration. |
| Publisher | Immutable `data/published/` carriers after an accepted decision | Cannot write its own release decision. |
| Contributor or AI builder | Feature-branch drafts and reviewable repository changes | Cannot approve, merge, release, deploy, publish, or claim adoption. |
| Watcher, connector, pipeline, renderer, AI runtime, or public client | No release-decision writes by default | May propose candidates or correction requests only through governed interfaces. |

[Back to top](#top)

---

## Public exposure and sensitivity posture

The machine projection classifies `release/` as internal while the Git repository is public. Committed records must therefore be safe for public source visibility. Restricted operational details may live in governed external storage with a versioned logical record, digest, media type, rights/sensitivity labels, retention, release, correction, and rollback references.

Public clients consume governed APIs and released public-safe carriers, not this directory as a direct trust store. Public summaries expose only policy-permitted identity, status, lineage, and reasons. Redact, generalize, restrict, or omit denial detail, private reviewer notes, incident/security detail, protected locations, living-person information, DNA/genomic data, restricted cultural material, private-land detail, or source terms.

Use `HOLD`, `ABSTAIN`, or `DENY` when rights, sovereignty, consent, sensitivity, reviewer authority, public scope, or harmful precision is unresolved. Never place private keys, tokens, OIDC credentials, or recovery material in this root.

[Back to top](#top)

---

## Mutability, retention, generation, and physical storage

| Property | Rule |
|---|---|
| Mutability | Durable decisions are append-only; create successor, correction, withdrawal, supersession, or rollback records instead of silently editing history. |
| Retention | Audit-bound; preserve stable identity, prior state, decision basis, correction lineage, and rollback target while reliance or policy requires. |
| Generation | Generated material is never independent release authority; a generated candidate declares producer, inputs, digest, and edit policy. |
| Placeholders | Canonical trust collections must not contain self-identified placeholder/scaffold instances. |
| Physical storage | Small public-safe records may be Git-tracked; larger/restricted operational records use governed external storage with a versioned logical record. |
| Locators | URL, object key, registry tag, Git path, or mutable alias is a locator, not authority. |
| Cache/index effects | State-changing decisions name affected caches, aliases, catalogs, APIs, maps, search, graph, exports, and AI surfaces where applicable. |
| Deletion | Last resort after authority, retention, reference closure, correction handling, and rollback/forward-fix review. |

Current physical-storage conflicts: three root `.rego` files are nonconforming policy source; two root RollbackCard JSON files remain non-schema-admissible documentation placeholders; `source_role_anti_collapse/` is README plus `.gitkeep`; and domain-first children require inventory before migration.

[Back to top](#top)

---

<a id="validation"></a>

## Validation and negative checks

| Command or workflow | Current bounded meaning | Does not prove |
|---|---|---|
| `make validate` | Aggregate schema validators and schema/contract tests. | Complete release closure, authenticated review, promotion, rollback, or publication. |
| `make publish-check` | Fixture-only ReviewRecord and A–G promotion-gate validators plus unit tests. | Live evidence, policy execution, review authority, decision emission, transition, or publication. |
| `python tools/validators/release/validate_release_manifest.py --fixtures` | Validates the preserved fixture-only ReleaseManifest profile. | Candidate assembly, accepted profile authority, or release. |
| `python tools/validators/release/validate_rollback_card.py --fixtures` | Validates the bounded shared RollbackCard candidate profile. | Target authorization, rollback execution, invalidation, receipt, or restoration. |
| `make release-dry-run` | Prints `TODO: tools/release dry-run`. | Any dry run or candidate assembly. |
| `release-dry-run`, `promotion-gate`, `rollback-drill` | Read-only readiness and fixture checks with explicit holds. | Candidate, decision, receipt, proof, signature, state mutation, rollback, or publication. |
| Pass 12 release-policy workflow | Tests one checksum-pinned `PROPOSED_INACTIVE` Rego profile under `policy/rego/`. | General OPA runtime, `PolicyDecision`, release, or publication. |

> [!CAUTION]
> `make release-dry-run` exits successfully after printing a TODO marker. Do not cite it as a successful dry run.

Applicable negative cases include unresolved/stale evidence; unbound hashes; unknown rights, sensitivity, role, scope, or policy; self-review or stale/superseded review; missing authority, manifest, catalog closure, attestation, correction path, or rollback target; nondeterministic geometry/time; placeholder trust instances; policy source under `release/`; direct public access to internal stores; and any workflow/PR/map/AI output misclassified as release authority.

[Back to top](#top)

---

<a id="review-burden"></a>

## Owner, reviewers, and escalation path

| Role or control | Current evidence | Status |
|---|---|---:|
| GitHub route | `/release/ @bartytime4life` in CODEOWNERS | `CONFIRMED`, routing only |
| Root-registry owner/writer | `@bartytime4life` in machine projection | `CONFIRMED` projection, not runtime assignment |
| Independent release steward | No verified identity or assignment | `NEEDS VERIFICATION` |
| Evidence, policy, security/privacy, correction, rollback, signing, and domain reviewers | Responsibilities are clear; assignments are not | `NEEDS VERIFICATION` |
| Required reviews and separation of duties | Not established for this task | `NEEDS VERIFICATION` |
| Runtime release authority/signing custody | No operational evidence inspected | `UNKNOWN` |

Review requirements scale with effect: documentation needs accuracy/no-loss review; profiles need contract/schema/fixture/validator/policy review; decisions need authenticated authority and subject/scope/hash binding; correction/withdrawal needs public-effect and invalidation analysis; rollback needs valid target, review/signature, execution receipt, restoration verification, and forward-fix comparison; policy/sensitive/public-path changes fail closed when authority is unresolved.

Escalate with finite outcomes: `PASS`/`APPROVE_READY` for bounded validation only, `ABSTAIN`/`HOLD` for incomplete support, `DENY` for policy or invariant violations, and `ERROR` when safe evaluation cannot complete.

[Back to top](#top)

---

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

Migration candidates remain out of this PR: singular `manifest/`; generic/singular correction and rollback lanes; domain-first children; `release/policy/`; root Rego files; generic reviews/decisions; and empty `source_role_anti_collapse/`. Each requires exact object classification, stable identity, reference/consumer repair, compatibility, validation, and rollback.

[Back to top](#top)

---

<a id="repo-fit"></a>
<a id="current-lane-index"></a>

## Direct-child directory map

### Canonical v2 families

| Path | Current bounded role | Outcome |
|---|---|---:|
| [`candidates/`](candidates/) | Candidate dossiers; no release authority. | `PLACE` |
| [`manifests/`](manifests/) | Canonical ReleaseManifest collection. | `PLACE` |
| [`promotion_decisions/`](promotion_decisions/) | Promotion decisions; current smoke record remains non-authoritative. | `PLACE` |
| [`correction_notices/`](correction_notices/) | Canonical correction-lineage notice family. | `PLACE` |
| [`withdrawal_notices/`](withdrawal_notices/) | Withdrawal-lineage notice family. | `PLACE` |
| [`rollback_cards/`](rollback_cards/) | Canonical rollback decision/target family; current root JSON placeholders are not admitted records. | `PLACE`, records mixed |
| [`signatures/`](signatures/) | Signature/attestation packets; no private keys. | `PLACE` |
| [`changelog/`](changelog/) | Release-level human-readable history. | `PLACE` |

### Drift, compatibility, and classification surfaces

| Path | Current bounded role | Outcome |
|---|---|---:|
| [`manifest/`](manifest/) | Singular compatibility lane. | `MIGRATE` after inventory |
| [`correction/`](correction/) and [`corrections/`](corrections/) | Overlapping generic/domain correction lanes. | `HOLD / MIGRATE` |
| [`rollback/`](rollback/) | Generic rollback review lane. | `MIGRATE` after classification |
| [`decisions/`](decisions/) and [`reviews/`](reviews/) | Generic guidance lanes overlapping canonical decision/review support. | `HOLD` |
| [`policy/`](policy/) | Release-facing policy index; source must remain under canonical `policy/`. | `HOLD` |
| [`agriculture/`](agriculture/) and [`people-dna-land/`](people-dna-land/) | Domain-first release routers/material. | `MIGRATE` with inventory and sensitivity review |
| [`source_role_anti_collapse/`](source_role_anti_collapse/) | README and `.gitkeep` only; no owned record/consumer proven. | `HOLD` |
| [`hydrology_publication.rego`](hydrology_publication.rego) | Proposed fail-closed policy scaffold under wrong root. | `DENY_NEW_WRITES / MIGRATE` |
| [`public_safe_geometry.rego`](public_safe_geometry.rego) | Proposed fail-closed policy scaffold under wrong root. | `DENY_NEW_WRITES / MIGRATE` |
| [`source_role_anti_collapse.rego`](source_role_anti_collapse.rego) | Proposed fail-closed policy scaffold under wrong root. | `DENY_NEW_WRITES / MIGRATE` |

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last evidence review and review trigger

| Field | Value |
|---|---|
| Last evidence review | 2026-08-09 |
| Base / prior blob | `main@9c080014926e6f3ba4dc630eaf7a615fff46c7fc` / `0752610b1df6d11143158f6f162f65ecd650e6a6` |
| Release tree | `210ccf37b9f90986590a3e0995a0eeda7f758042` |
| Open target-overlap PRs | `0` at discovery |
| Result | Same-path ROOT_FULL v2.1 modernization, evidence refresh, drift visibility, and generated provenance only. |
| Implementation effect | No path move, record, policy, schema, workflow, runtime, data, release, rollback, deployment, publication, or settings change. |
| Maximum staleness | Six months unless a trigger occurs sooner. |

Re-review when a direct-child path or meaning changes; a migration starts/completes/reverts; a fixture profile becomes accepted or operational; a candidate/review/manifest/decision/correction/withdrawal/rollback/signature/published alias is exercised; release automation or public consumers change; steward/ruleset/signing authority changes; or production/runtime evidence becomes available.

[Back to top](#top)

---

<a id="lifecycle-boundary"></a>
<a id="root-responsibilities"></a>

## Lifecycle and authority boundary

```text
PRE_RAW -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS
                                                  + PROOF
                                                  + RELEASE DECISION
                                                    -> PUBLISHED
```

`release/` owns the decision that authorizes or changes a release. `data/published/` owns the immutable release-approved carrier. Promotion emits a governed state/version and is never inferred from copying, moving, naming, workflow completion, or a mutable alias.

[Back to top](#top)

---

<a id="release-state-model"></a>

## Release state model

Keep record, validator, workflow, PR, and public-artifact states distinct.

| Release-facing state | Meaning |
|---|---|
| `DRAFT` | Exists, not ready for accountable review. |
| `READY_FOR_REVIEW` | Review inputs appear complete; no release authority yet. |
| `HELD` | Evidence, validation, policy, rights, sensitivity, authority, correction, or rollback support is unresolved. |
| `READY_FOR_MANIFEST` | Reviewed candidate may support manifest preparation; not released. |
| `APPROVED` | Governed decision approves named scope; publication still needs complete transition. |
| `RELEASED` | Governed release state is complete for a named version and scope. |
| `CORRECTED`, `SUPERSEDED`, `WITHDRAWN` | Append-only lineage changes public reliance while preserving history. |
| `NO_ACTION` | Review authorizes no state change. |

Validator (`PASS/ABSTAIN/DENY/ERROR`), readiness (`APPROVE_READY/HOLD/...`), workflow, PR, decision, and published-carrier vocabularies must not be silently mapped to one another.

[Back to top](#top)

---

## Workflow readiness boundaries

- **`release-dry-run`:** read-only assertions for candidate absence, ReleaseManifest fixtures (`4` valid, `17` invalid grouped cases), PromotionDecision/A–G readiness, and RollbackCard fixtures. The helper and Make target remain placeholders; no record or release is emitted.
- **`promotion-gate`:** read-only fail-closed doctrine and proposed-shape checks plus Gate G synthetic identity, authority, self-review, scope, subject, time, obligations, supersession, and hash binding. `release/reviews/` contains guidance and an empty Atmosphere scaffold, not accountable review records.
- **`rollback-drill`:** read-only shared RollbackCard fixture validation and hold assertions. Generic entry point, rollback pipeline/apply helper, Agriculture profile, published aliases, invalidation, receipts, and restoration remain held.
- **Pass 12 Rego lane:** separately governed `PROPOSED_INACTIVE` profile under [`policy/rego/`](../policy/rego/release_gate_v1.rego). It does not resolve evidence, authenticate review, emit `PolicyDecision`, or create a general runtime.

[Back to top](#top)

---

## Bounded implemented validation slices

| Slice | Confirmed evidence | Authority limit |
|---|---|---|
| ReleaseManifest fixture profile | Contract/schema metadata, closed strict branch, grouped cases, validator, test, workflow assertions. | Fixture-only; no assembly or release. |
| PromotionDecision shape | Closed schema, non-empty fixtures, test, workflow binding. | Proposed; no live policy/evidence/review/transition. |
| ReviewRecord projection | Validator/tests with finite outcomes and reason mapping. | Synthetic; no live actor or authority. |
| A–G promotion gate | Side-effect-free validator, fixtures, tests, Make target, read-only workflows. | Declared closure only; emits no decision. |
| Shared RollbackCard profile | Closed candidate profile, fixtures, validator, workflow binding. | Local consistency only; no execution. |
| Pass 12 release policy | Rego, native tests, fixtures, pinned workflow. | Inactive bounded profile; no general runtime. |

[Back to top](#top)

---

<a id="required-release-root-record-fields"></a>
<a id="minimal-release-root-record"></a>

## Release record minimum contract

An accepted release-decision record should bind stable ID/version/type; finite outcome/reasons; subject, scope, time, sensitivity, and immutable digests; evidence, validation, policy, review/authority, manifest, signature, correction/withdrawal/supersession, rollback/invalidation, and public-effect references; predecessor/successor lineage; recorded-at/actor; retention; and unresolved obligations.

A missing required field produces hold, abstain, deny, or error. It never implies completion through an empty field, filename, default allow, workflow status, or prose note. Accepted contracts and schemas outrank illustrative templates.

[Back to top](#top)

---

<a id="review-checklist"></a>

## Review checklist

- [ ] Canonical object-family-first lane, stable identity/version, subject/scope/time, and immutable digests are explicit.
- [ ] Evidence, validation, integrity, citation, catalog, rights, sensitivity, access, and public-safety support resolve.
- [ ] Reviewer/decider identity, authority, scope, time, subject/hash binding, obligations, and separation of duties are explicit.
- [ ] Manifest, signature, correction/withdrawal/supersession, notice, rollback, invalidation, and restoration requirements are satisfied where applicable.
- [ ] No payload, receipt, proof, source, schema, contract, policy, validator, application, or generated-output authority is duplicated here.
- [ ] No generated text, map, tile, workflow, PR, merge, GitHub release, or signature packet is used as approval by itself.
- [ ] Sensitive information is absent or handled through approved restricted storage.
- [ ] The diff is bounded, reversible, and linked to correction or rollback.

[Back to top](#top)

---

<a id="naming-guidance"></a>

## Naming and identity guidance

Use object-family-first/domain-second paths, registered stable IDs and versions inside records, lowercase ASCII path segments, plural collection directories, singular record filenames, explicit canonicalized digests, and distinct path/object/display/locator/alias identities. Dates in filenames are navigation aids, not identity or temporal truth. Never create new domain-first release homes.

[Back to top](#top)

---

## Compatibility and placement conflicts

| Conflict | Safe next step |
|---|---|
| `manifest/` vs `manifests/` | Inventory IDs/references, migrate with compatibility and zero-writer/consumer evidence, then retire singular lane. |
| `correction/`, `corrections/`, `correction_notices/` | Classify review, decision, notice, and domain records before migration. |
| `rollback/` vs `rollback_cards/` | Classify decisions vs execution receipts; target cards under `release/rollback_cards/`, process records under `data/receipts/rollback/`. |
| `reviews/`, `decisions/`, `promotion_decisions/` | Define accepted ReviewRecord and decision placement; do not collapse from filenames. |
| Domain-first children | Migrate each object to its owning family with sensitivity review and reference repair. |
| `release/policy/` and root Rego | Move policy source to canonical `policy/`; preserve release records as references only. |
| Empty source-role lane | Establish a real owned object and consumer or retire through governed migration. |
| Shared/domain ReleaseManifest and receipt-like profiles | Define shared-kernel/extension rules and prevent parallel writable authority. |
| Published `current` aliases | Define immutable pointer identity, rollback binding, negative tests, cache behavior, and receipts before activation. |

These are facts and work items, not permission for broad cleanup in this documentation PR.

[Back to top](#top)

---

<a id="open-verification"></a>

## Open verification register

1. Named release/evidence/policy/security/privacy/correction/rollback/signing/domain authorities and enforced independent review.
2. Full object/reference/consumer inventory and migration plans for every drift lane.
3. Accepted shared-kernel/domain-extension catalog for release objects and version/deprecation policy.
4. Deterministic no-write candidate assembly and operational evidence closure.
5. Accepted policy runtime, authenticated review/authority, attestation/signing, and catalog/manifest closure.
6. Side-effect-controlled promotion and publisher boundaries that cannot self-publish.
7. Rollback target selection, simulation, invalidation, execution receipts, restoration, and forward-fix fallback.
8. Correction/withdrawal propagation through catalog, API, MapLibre, search, graph, export, citations, caches, and AI.
9. Compatibility retirement, external consumers, production storage/registry, observability, incident response, retention, and recovery.
10. Current hosted exact-head checks and human adoption of this documentation revision.

[Back to top](#top)

---

## Definition of done

This documentation slice is complete when the exact repo/base/path/root/blob/tree are verified; ROOT_FULL order is correct; stale claims and all current children/conflicts are reconciled; identity, anchors, links, Markdown, receipt/hash closure, remote bytes, parentage, diff, draft PR, and hosted status are verified; and no unrelated behavior or authority change exists.

Operational release remains separate and requires admitted evidence, accepted contracts/schemas/policies/identities, positive and negative fixtures, deterministic bounded execution, accountable review, manifest/proof/receipt/catalog/signature/correction/rollback closure, immutable public-safe carrier production, propagation and recovery drills, truntime/storage/observability evidence, and a separately authorized release/publication transition.

[Back to top](#top)

---

<a id="maintenance-correction-and-rollback"></a>

## Maintenance, correction, and rollback

No release, promotion, correction, rollback execution, deployment, or publication is performed by this documentation change.

For documentation correction: pin current main and target; reconcile overlap; read the full governing/implementation neighborhood; classify drift; make the smallest same-path edit; validate; emit provenance; push without force; and deliver one draft PR.

Before merge, close or abandon the draft PR/branch. After an authorized merge, use a transparent revert or forward-fix PR; never rewrite shared history. Reverting this README and generated receipt restores documentation bytes only, not any release, policy, schema, workflow, candidate, published artifact, cache, alias, or runtime state.

Rollback target for this slice: README blob `0752610b1df6d11143158f6f162f65ecd650e6a6` at `main@9c080014926e6f3ba4dc630eaf7a615fff46c7fc`; remove the generated receipt only through the reviewed revert of the same packet.

[Back to top](#top)

---

## Changelog

| Version | Date | Change |
|---:|---:|---|
| v 1 | 2026-07-03 | Expanded the compact root stub into release-governance guidance. |
| v2.0 | 2026-07-23 | Reordered the root contract, refreshed evidence, added lane coverage, workflow holds, CODEOWNERS limits, open verification, and documentation-vs-operational rollback boundaries. |
| v2.1 | 2026-08-09 | Adopted exact Directory Rules v2 ROOT_FULL order; repinned current evidence; corrected Make/ReleaseManifest/ReviewRecord/promotion-gate/RollbackCard maturity; classified all direct children and root Rego drift; preserved operational release, signing, rollback, alias, and publication holds. |

[Back to top](#top)
