<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/agriculture/readme
title: Agriculture Runbooks — Operational Procedure Index
type: readme
subtype: domain-runbook-boundary
version: v0.1
status: draft; repository-grounded; mixed-child-maturity; documentation-only; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Agriculture, source, test, policy, evidence, rights/sensitivity, release, rollback, and independent-review stewards"
created: 2026-08-23
updated: 2026-08-23
policy_label: public-review; agriculture; operational-documentation; fail-closed; no-publication-authority
current_path: docs/runbooks/agriculture/README.md
owning_root: docs/
responsibility: "Define the human-facing boundary, navigation, inheritance, current maturity, and maintenance contract for Agriculture operational procedures without granting source admission, evidence, policy, lifecycle, review, release, deployment, promotion, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational-documentation index
canonical_relationship: same-path completion of an existing tracked blank file; canonical lane boundary under docs/runbooks/agriculture; no sibling authority created
repository: bartytime4life/Kansas-Frontier-Matrix
base_ref: main
base_commit: 2c010b36609bf2ceb94e5a2d61fa62493e6f298f
target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
directory_tree: c0bd163c95b695aef8901df7a1c1c9ce319e4efe
parent_runbooks_readme_blob: 7b6f266a41f7723cba50ea3c093d341063c08f4d
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
no_network_test_runbook_blob: a2b98be38bab40cd0985f4b7cf4fcac7d84c3ea0
promotion_runbook_blob: aa2f3e8edc2928b261dfb57782e167eef94fc98a
rollback_runbook_blob: d86230acfdad2e6e7bafc04e6b1d3d64cc44d2e4
source_refresh_runbook_blob: f213ef17f4880b3850b48e62168c5c959351e055
related:
  - docs/runbooks/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/agriculture/DOMAIN.md
  - docs/domains/agriculture/ARCHITECTURE.md
  - docs/domains/agriculture/DATA_LIFECYCLE.md
  - docs/domains/agriculture/SENSITIVITY.md
  - docs/domains/agriculture/runbooks/README.md
  - docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/agriculture/PROMOTION_RUNBOOK.md
  - docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md
  - docs/runbooks/agriculture/SOURCE_REFRESH_RUNBOOK.md
  - .github/CODEOWNERS
  - .github/workflows/domain-agriculture.yml
  - .github/workflows/docs-meta-block.yml
  - .github/workflows/validator-suite.yml
notes:
  - "The prior target was a tracked one-byte blank file. This edition adds the missing local boundary contract without moving or renaming any procedure."
  - "NO_NETWORK_TEST_RUNBOOK.md and ROLLBACK_RUNBOOK.md are repository-grounded v0.2 drafts; PROMOTION_RUNBOOK.md and SOURCE_REFRESH_RUNBOOK.md retain proposal-era v0.1 assumptions and require reconciliation before operational reliance."
  - "The domain-side docs/domains/agriculture/runbooks/README.md remains an orientation surface, not the canonical procedure lane; its stale proposed-path claims are separate follow-up work."
  - "This document changes no executable procedure, source, connector, contract, schema, policy, fixture, validator, workflow, evidence object, lifecycle object, release record, deployment, promotion, rollback execution, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Runbooks — Operational Procedure Index

> **Start here for Agriculture source-refresh, no-network validation, promotion, rollback, withdrawal, and recovery procedures.** This directory explains how an authorized actor should proceed; it does not grant the authority, evidence, policy decision, review, release decision, or public state that a procedure depends on.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![Procedure files: 4](https://img.shields.io/badge/procedure%20files-4-0969da?style=flat-square)](#direct-child-map)
[![Bounded no-network slices: present](https://img.shields.io/badge/no--network%20slices-present-1f883d?style=flat-square)](#current-repository-state)
[![Broader operations: HOLD](https://img.shields.io/badge/broader%20operations-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Runbooks are instruction surfaces, not authority surfaces.** A runbook may name a `SourceDescriptor`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `RollbackCard`, validator result, or workflow conclusion. It cannot create, approve, replace, or execute those objects by prose alone.

> [!CAUTION]
> **This lane has mixed maturity.** The no-network and rollback documents have been reconciled against repository evidence. The promotion and source-refresh documents still contain proposal-era paths, placeholder owners, and no-mounted-repository assumptions. Treat those two files as planning procedures until they receive their own repository-grounded updates.

> [!WARNING]
> Exact field, farm, parcel, operator, well, private-party, proprietary yield, pesticide, insurance, or other sensitive Agriculture detail fails closed by default. Do not use style hiding, a map filter, a test fixture, or a Markdown statement as a substitute for source-rights review, sensitivity policy, aggregation, redaction, quarantine, or denial.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Placement](#placement-and-canonical-relationship) · [State](#current-repository-state) · [Children](#direct-child-map) · [Start here](#start-here) · [Lifecycle](#lifecycle-and-state-separation) · [Boundaries](#what-belongs-here) · [Inputs and outputs](#inputs-outputs-and-permitted-actors) · [Safety](#agriculture-specific-safety-rules) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Validation](#validation-and-rehearsal-boundary) · [Maintenance](#maintenance-and-review-triggers) · [Open work](#open-verification-backlog) · [Related](#related-surfaces) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

## Purpose

`docs/runbooks/agriculture/` is the Agriculture domain lane inside KFM's human-readable operational-procedure root. It helps maintainers, reviewers, stewards, developers, and operators answer bounded questions such as:

- Which Agriculture procedure applies to the current task or failure state?
- Is the procedure repository-grounded, proposal-era, executable, held, or unverified?
- Which evidence, source identity, policy result, review, release object, permissions, fixtures, and rollback target are prerequisites?
- Which action belongs to a tool, workflow, source registry, lifecycle store, policy engine, review authority, or release system rather than Markdown?
- Which outcome should stop the operation, retain a candidate in `WORK`, move it to `QUARANTINE`, withhold a claim, or escalate it for review?
- Which records must remain inspectable after correction, withdrawal, rollback, or replay?

The directory is documentation-first. Executable behavior and trust-bearing objects remain in their owning responsibility roots. The runbooks should make the governed path usable without embedding a second source registry, contract system, schema authority, policy engine, evidence store, release plane, or publication mechanism in documentation.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md). The adopted rules place human operational procedures under `docs/runbooks/` and require README boundaries to explain ownership, inheritance, exposure, mutation, lifecycle behavior, and non-effects without creating parallel authority.

| Concern | Owning authority | This directory's role |
|---|---|---|
| Documentation placement and inheritance | Accepted Directory Rules plus the parent [`docs/runbooks/` contract](../README.md) | Define the Agriculture procedure boundary and disclose drift |
| Agriculture domain meaning | [`docs/domains/agriculture/`](../../domains/agriculture/) plus semantic contracts | Orient readers; do not redefine the domain |
| Object meaning | `contracts/` | Cite semantics; do not restate a competing contract |
| Machine shape | `schemas/` | Cite versions and required fields; do not host schema authority |
| Allow, deny, restrict, hold, or abstain | `policy/` plus required review | Explain how to obtain and respond to a decision |
| Source identity and admission | SourceDescriptor and source-registry authorities | Describe safe handling; do not activate or admit a source |
| Evidence and citations | EvidenceRef, EvidenceBundle, receipts, and proofs | Require support; do not manufacture evidence |
| Executable behavior | `tools/`, `pipelines/`, `connectors/`, packages, applications, runtime, and workflows according to role | Point to reviewed entry points and interpret bounded outcomes |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe a transition; do not perform one by file movement |
| Promotion, release, correction, withdrawal, rollback | `release/` and linked accountability objects | Explain the authorized procedure; do not approve or execute it |
| This README | Human navigation, inheritance, maturity disclosure, and maintenance contract | No source, policy, evidence, review, release, deployment, promotion, rollback-execution, or publication authority |

A procedure must stop when its named authority, identity, permission, evidence, policy, review, or rollback target is unresolved. A README cannot convert `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD` into permission.

[Back to top](#top)

---

## Placement and canonical relationship

**Placement outcome: `PLACE` — CONFIRMED for this same-path additive update.**

| Property | Current result |
|---|---|
| Path | `docs/runbooks/agriculture/README.md` |
| Owning root | `docs/` — human-readable operational documentation |
| Scope | Agriculture domain runbook lane |
| Prior path state | Existing tracked one-byte blank file at blob `8b137891…` |
| Structural effect | None; no create, move, rename, split, mirror, compatibility lane, or delete |
| Authority effect | None; documents existing boundaries and current evidence |
| Review route | `@bartytime4life` through the repository default CODEOWNERS rule |
| Accountable and independent stewardship | `NEEDS VERIFICATION` |
| Release and publication effect | None |

This README is the canonical local boundary for the procedure files in this directory. [`docs/domains/agriculture/runbooks/README.md`](../../domains/agriculture/runbooks/README.md) is a domain-side orientation surface. It may point here, but it does not become a second writable procedure authority. When the two disagree, current repository evidence and the canonical procedure files in this lane control the operational-description claim, subject to higher contracts, schemas, policy, evidence, review, release, correction, and rollback authorities.

The parent [`docs/runbooks/README.md`](../README.md) retains a repository-wide inventory snapshot pinned to an earlier commit. Its historical statement that no direct domain lane had a populated boundary README predates this completion and should be refreshed only through a later full inventory reconciliation, not by silently rewriting its historical evidence block here.

[Back to top](#top)

---

## Current repository state

The observations below are pinned to `main@2c010b36609bf2ceb94e5a2d61fa62493e6f298f`. They describe tracked bytes and bounded executable evidence. They do not establish live source operation, operational admission, release readiness, deployment, or publication.

| Surface | CONFIRMED evidence at the pinned revision | Bounded conclusion |
|---|---|---|
| This README | Existing tracked file contained only a newline | Local lane boundary was absent in substance |
| Direct procedure packet | Four tracked procedure files plus this README | The lane has a stable four-procedure documentation packet |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Repository-grounded v0.2 draft with five bounded fixture-only slices | Useful for deterministic offline checks; broader Agriculture validation remains `HOLD` |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Repository-grounded v0.2 draft; shared `RollbackCard` contract, schema, validator, fixtures, and focused tests are present | Candidate validation exists; rollback decision and execution remain separate |
| Agriculture rollback drill | Referenced drill lane remains documentation-only in the reconciled rollback runbook | Agriculture-specific executable recovery proof remains `HOLD` |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | v0.1 draft with placeholder owners, proposed paths, and proposal-era prerequisite claims | Planning reference only until repository-grounded reconciliation |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | v0.1 draft with placeholder owners, proposed source homes/cadences, and no-mounted-repository assumptions | Planning reference only; no source is admitted or activated by this file |
| [`domain-agriculture`](../../../.github/workflows/domain-agriculture.yml) | Read-only pull-request/main workflow; one synthetic CDL watcher proof and separate bounded Agriculture suites; broader validation, proof, and release-dry-run producers held | Workflow presence is bounded orchestration evidence, not Agriculture truth or release authority |
| CODEOWNERS | Default GitHub review route is `@bartytime4life`; no Agriculture runbook-specific rule | Review routing exists; accountable stewardship and independent approval remain unverified |
| Live sources, operational promotion, rollback execution, deployment, publication | Not established by this directory | `UNKNOWN` or `HOLD` until owning surfaces provide exact-revision evidence |

### Bounded executable slices currently named by the no-network runbook

1. Synthetic Cropland Data Layer material-change watcher.
2. Deterministic NDVI delta computation.
3. HLS NDVI zonal materiality assessment.
4. NDVI readiness assessment.
5. Vegetation-connectivity gate and fixture replay.

These slices prove only their named fixture and validator behavior. They do not establish a source as authoritative, prove a public claim, create an EvidenceBundle, approve policy, promote lifecycle state, release an artifact, deploy a service, or publish a map layer.

[Back to top](#top)

---

## Direct-child map

Directory Rules require a lane README to show the directory it governs and its direct children, not a speculative repository tree.

```text
docs/runbooks/agriculture/
├── README.md
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── ROLLBACK_RUNBOOK.md
└── SOURCE_REFRESH_RUNBOOK.md
```

| Child | Primary question | Current documentation posture | Use boundary |
|---|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Which Agriculture checks can run deterministically without network access, and what do their results prove? | `CONFIRMED` repository-grounded v0.2 draft | Use for the named offline slices only |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | How should an already-admitted source be refreshed through the lifecycle? | `NEEDS VERIFICATION`; proposal-era v0.1 draft | Do not use to admit, activate, schedule, or fetch a live source |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Which gates would be required before Agriculture candidates could become released public-safe artifacts? | `NEEDS VERIFICATION`; proposal-era v0.1 draft | Do not treat named paths, signers, gates, or commands as current implementation proof |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | How should a rollback, withdrawal, hold, or recovery candidate be assembled and reviewed? | `CONFIRMED` repository-grounded v0.2 draft; execution held | Candidate validation is not rollback approval or execution |

[Back to top](#top)

---

## Start here

| Need | Entry point | Required posture before action |
|---|---|---|
| Run a deterministic Agriculture fixture check | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Use the exact checked revision, `KFM_NO_NETWORK=1`, synthetic/public-safe fixtures, and the named bounded command |
| Assess or design a source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Reconcile its proposed paths, source identity, rights, cadence, and current repository implementation first |
| Prepare a promotion review packet | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Treat it as a proposal; verify current contracts, schemas, policy, evidence closure, review duties, release homes, signatures, and rollback machinery |
| Assemble a rollback or withdrawal candidate | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Resolve current release identity and support; validate a candidate without implying decision or execution authority |
| Handle possible sensitive exposure | [`../SENSITIVITY_ESCALATION.md`](../SENSITIVITY_ESCALATION.md) and Agriculture [`SENSITIVITY.md`](../../domains/agriculture/SENSITIVITY.md) | Contain only through an already-authorized mechanism; preserve evidence and audit lineage |
| Handle a repository or operational incident | [`../INCIDENT_RESPONSE.md`](../INCIDENT_RESPONSE.md) | Use the cross-cutting incident procedure and the appropriate Agriculture-specific evidence and policy context |
| Correct an evidence-backed public claim | [`../EVIDENCE_CORRECTION.md`](../EVIDENCE_CORRECTION.md) | Correction, withdrawal, release, cache invalidation, and rollback remain distinct actions |

When two procedures appear applicable, choose the narrowest procedure that owns the immediate action and link the handoff to the next authority. Do not combine source admission, validation, policy, review, promotion, release, deployment, and publication into one undocumented operator path.

[Back to top](#top)

---

## Lifecycle and state separation

The Agriculture lane inherits KFM's lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Promotion is a governed state transition, not a path move, copy, commit, pull request, workflow result, badge, release tag, or map-layer toggle.

Keep these axes separate:

| Axis | Example | What it does not prove |
|---|---|---|
| File presence | A runbook, fixture, schema, or validator exists | Current correctness or operational admission |
| Documentation state | Draft, repository-grounded, proposal-era, corrected | Executable behavior |
| Validation state | A named check passes or fails | Source authority, evidence truth, policy approval, or review completion |
| Rehearsal state | A procedure ran in an approved non-public environment | Production readiness or release approval |
| Source state | Candidate, admitted, held, denied, withdrawn | Lifecycle promotion or public exposure |
| Evidence state | EvidenceRef resolves to an admissible EvidenceBundle | Policy or release approval |
| Review state | Required review is pending or complete | Merge, release, deployment, or publication by itself |
| Lifecycle state | An object is in RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, or PUBLISHED | Correctness merely from its path |
| Release state | A specific immutable release is candidate, held, approved, withdrawn, or superseded | Deployment or publication unless separately evidenced |
| Deployment state | A service or carrier is deployed | Public-safe publication or truth authority |
| Publication state | A governed public-safe carrier is exposed | Sovereign truth independent of its evidence and correction lineage |

[Back to top](#top)

---

## What belongs here

- The local boundary and navigation contract for Agriculture operational procedures.
- Step-by-step human procedures for recurring Agriculture operations and recovery actions.
- Preconditions, authority references, environment constraints, finite outcomes, stop conditions, handoffs, and rollback instructions.
- Current repository evidence about whether a named procedure is executable, proposal-era, held, or unverified.
- Links to the exact contracts, schemas, policies, fixtures, validators, workflows, evidence objects, lifecycle objects, release objects, and domain documentation that own the procedure's dependencies.
- Agriculture-specific public-safety, source-role, temporal, spatial-support, rights, sensitivity, aggregation, correction, and rollback cautions.

## What does not belong here

| Material | Owning root or surface | Why it stays out of this directory |
|---|---|---|
| Semantic object definitions | `contracts/` | Runbooks consume meaning; they do not define it |
| JSON Schema or other machine shape | `schemas/` | Runbooks cite machine requirements; they do not become schema authority |
| Policy rules or allow/deny logic | `policy/` | Documentation cannot decide admissibility |
| Executable source connectors or refresh code | `connectors/`, `pipelines/`, tools, packages, applications | Procedures describe reviewed execution; they do not replace it |
| Test assertions and fixtures | `tests/`, `fixtures/` | Tests prove bounded behavior; prose is not a fixture |
| Source descriptors and authority registers | Governed registry/control-plane surfaces | A source table in Markdown is navigational only |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED instances | Governed `data/` lanes | Lifecycle state cannot be created by documentation placement |
| Evidence, receipts, proofs, or review records | Their governed accountability families | Referenced support must remain independently resolvable |
| Release manifests, promotion decisions, correction notices, rollback cards | `release/` and linked object families | Runbooks cannot approve or execute release state |
| Public API, map, tile, dashboard, export, or AI response | Governed applications and released carriers | Delivery surfaces are downstream of trust |
| Secrets, credentials, private endpoints, signed URLs, or sensitive records | Never tracked here | Documentation must not expand exposure |

[Back to top](#top)

---

## Inputs, outputs, and permitted actors

### Required inputs before following a procedure

- The exact repository revision, release identity, source identity, or candidate identity under review.
- The current procedure bytes and all applicable higher-authority contracts, schemas, policy, accepted decisions, and Directory Rules.
- Resolvable evidence, rights, sensitivity, temporal, spatial-support, and source-role information appropriate to the action.
- The required actor permissions and review assignments; placeholders are not authority.
- Synthetic or approved public-safe fixtures when deterministic testing can prove the behavior.
- A defined stop condition, audit record, correction path, and rollback target proportional to the operation.

### Permitted documentation outputs

| Output | Permitted meaning | Limit |
|---|---|---|
| Checklist or procedure state | Human progress aid | Not lifecycle or release state |
| `PASS`, `FAIL`, `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, or `ESCALATE` report | Bounded result from the named procedure or owning validator | Does not expand the authority of the underlying result |
| Handoff packet | Links exact evidence, findings, candidate objects, and unresolved decisions | Does not self-approve the handoff |
| Drift or verification item | Records a concrete mismatch or missing proof | Does not authorize a guessed repair |
| Rollback instructions for documentation | Restores or forward-fixes repository prose | Does not roll back public state |

### Permitted actors

Maintainers, stewards, reviewers, developers, and operators may read these runbooks. Acting on a step requires the permissions and authority named by the owning system. GitHub review routing to `@bartytime4life` is `CONFIRMED`; Agriculture, source, evidence, policy, rights/sensitivity, release, rollback, and independent-review assignments remain `NEEDS VERIFICATION` unless a current authority record resolves them.

[Back to top](#top)

---

## Agriculture-specific safety rules

1. **Public-safe aggregation is the default posture.** County, HUC, or reviewed grid aggregates may be appropriate; exact field or operator detail is not made public merely because it can be computed.
2. **Source roles must remain explicit.** Observation, estimate, model, classification, forecast, aggregate, regulatory record, contextual support, and synthetic fixture cannot substitute for one another.
3. **Modeled and derived products remain derived.** NDVI, suitability, drought-stress, pest-stress, interpolation, classification, and connectivity outputs require their own method, input, uncertainty, validation, and representation records.
4. **Rights uncertainty fails closed.** Unknown license, redistribution, attribution, rate-limit, consent, or contractual terms produce `HOLD`, `QUARANTINE`, `ABSTAIN`, or `DENY` rather than assumed permission.
5. **Sensitive joins require separate review.** Person-parcel, operator-field, ownership, well, insurance, pesticide, proprietary yield, or other private-party joins remain restricted unless explicitly admitted and reviewed.
6. **Watchers and refresh jobs are non-publishers.** They may detect change, capture candidates, emit receipts, and open review work; they do not write directly to governed public state.
7. **Map and AI surfaces are downstream carriers.** A layer, popup, dashboard, search result, Focus Mode answer, or generated summary cannot outrank the EvidenceBundle, policy, review, release, and correction state behind it.
8. **Emergency and advisory authority stays external.** KFM may provide bounded historical or contextual Agriculture information but must redirect current life-safety, weather, drought, smoke, pest, or emergency guidance to the appropriate official authority.

[Back to top](#top)

---

## Finite outcomes and stop conditions

| Outcome | Meaning in this lane | Next action |
|---|---|---|
| `PASS` | The named deterministic check satisfied its bounded acceptance criteria | Record exact revision and continue only to the next separately authorized gate |
| `FAIL` | A substantive expected check did not pass | Stop, preserve diagnostics, and repair or quarantine according to the owning procedure |
| `HOLD` | Required authority, evidence, rights, sensitivity, review, implementation, or rollback proof is unresolved | Do not advance the affected action |
| `ABSTAIN` | Evidence is insufficient for the requested claim or interpretation | Withhold the claim and record the missing support |
| `DENY` | Policy or a hard trust boundary prohibits the action | Stop; preserve the decision and obligations |
| `ERROR` | The procedure or tool could not produce a trustworthy result | Preserve context; do not reinterpret the error as fail-closed success |
| `ROLLBACK_CANDIDATE` | A candidate recovery packet is locally consistent | Obtain required policy, review, and release decisions; do not execute from validation alone |
| `WITHDRAWAL_CANDIDATE` | Removal or withholding is proposed without a replacement target | Review impact, correction, invalidation, and public notice requirements |
| `ESCALATE` | The action requires a different owner, higher-risk review, or cross-domain decision | Hand off exact evidence and stop local mutation |

Stop immediately when:

- the repository, source, release, evidence, or target identity cannot be resolved;
- a procedure names a missing or stale contract, schema, policy, path, command, or owner that is necessary for safe action;
- live network access, credentials, production stores, or public mutation appear in a no-network or review-only path;
- exact sensitive or rights-limited data would enter an unapproved fixture, log, PR, public artifact, or model context;
- a derived or modeled value is being relabeled as observation;
- a watcher, workflow, runbook, test, map, or model is being treated as release or publication authority;
- rollback or correction would erase audit history, recreate parallel authority, or silently mutate released bytes.

[Back to top](#top)

---

## Validation and rehearsal boundary

### Documentation checks for this lane

A change to this README or a child runbook should receive, at minimum:

1. Complete-file review and material no-loss comparison.
2. `KFM_META_BLOCK_V2` validation where a metadata block is present.
3. Internal anchor and relative-link validation.
4. Direct-child inventory comparison against the exact Git tree.
5. Repository-topology and workflow-security ratchets through the existing aggregate validator suite.
6. Review of any triggered workflow that can access secrets, elevated permissions, external systems, or mutation authority.

Repository-native commands available in a full checkout include:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/meta-block \
  --pattern 'test_*.py' \
  --verbose

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  docs/runbooks/agriculture/README.md

make workflow-security
make repository-topology
```

### Operational validation

Use the exact commands in [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) only when the corresponding implementation, fixtures, and dependencies are in scope. Do not rerun live-source, release, or rollback operations merely to validate a documentation-only change.

### What green checks do not prove

A green metadata check, link check, unit test, domain workflow, validator suite, or hosted CI run does not prove:

- live source admission or freshness;
- EvidenceRef-to-EvidenceBundle closure for every Agriculture claim;
- rights or sensitivity approval;
- completed human or independent review;
- operational promotion, signing, release, rollback, deployment, or publication;
- scientific validity beyond the exact fixture and assertion executed.

Rehearsal evidence must record the exact revision, environment, fixtures, commands, outputs, actor, and limitations. Production or public readiness remains separate.

[Back to top](#top)

---

## Maintenance and review triggers

Review this README and the affected child procedure when any of the following changes:

- a child runbook is added, removed, renamed, superseded, or materially modernized;
- an Agriculture contract, schema, policy, source role, sensitivity rule, lifecycle rule, or release family changes;
- a command, fixture, validator, workflow, dependency, runner, permission, or network posture changes;
- a source becomes admitted, denied, withdrawn, stale, rights-limited, or operationally active;
- a bounded no-network slice graduates, regresses, or is replaced;
- an executable Agriculture rollback drill lands or its topology changes;
- a correction, withdrawal, rollback, cache invalidation, or public-notice obligation changes;
- the domain-side orientation index or parent runbook inventory conflicts with this canonical lane;
- accountable or independent stewardship becomes verifiable.

For each update, pin the base commit and target blob, inspect open PR overlap, preserve stable anchors where practical, update direct references, run proportionate validation, and keep review, merge, release, deployment, promotion, and publication separate.

[Back to top](#top)

---

## Open verification backlog

| Item | Current state | Evidence needed to close |
|---|---|---|
| Reconcile [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | `NEEDS VERIFICATION` / `HOLD` | Current repository paths, contracts, schemas, policy, release objects, commands, owners, negative tests, and rollback evidence |
| Reconcile [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | `NEEDS VERIFICATION` / `HOLD` | Current source registry, admitted sources, connector state, rights/cadence fields, exact commands, fixtures, validators, and no-publication proof |
| Agriculture rollback drill | `HOLD` | Deterministic fixture, executable procedure, validator/workflow evidence, expected failure cases, and reviewable recovery outputs |
| Accountable Agriculture and release stewardship | `NEEDS VERIFICATION` | Current authority records with verified identities and separation-of-duty posture |
| Live source activation and operational refresh | `UNKNOWN` | SourceDescriptor admission, terms/rights review, connector identity, bounded network profile, receipts, and exact-run evidence |
| Full Agriculture evidence and policy closure | `UNKNOWN` / `HOLD` | Resolvable EvidenceBundles, policy decisions, review records, proofs, and negative-path coverage for a named slice |
| Operational promotion, signing, rollback, deployment, publication | `UNKNOWN` / `HOLD` | Exact immutable release flow, signer custody, approval, recovery drill, deployment evidence, public-state verification, correction and rollback paths |
| Domain-side orientation drift | `NEEDS VERIFICATION` | Reconcile or narrow `docs/domains/agriculture/runbooks/README.md` without creating a second procedure authority |
| Parent runbook inventory refresh | `NEEDS VERIFICATION` | Full repository-wide rescan so historical counts and boundary-README coverage can be updated coherently |
| Dedicated aggregate runbook validator | `UNKNOWN` at the parent inventory snapshot | Repository-owned contract, fixtures, validator, tests, registry wiring, and CI behavior if such a gate is commissioned |

These are follow-up candidates, not implied authorization to implement, activate, release, deploy, promote, publish, or change repository settings.

[Back to top](#top)

---

## Related surfaces

### Governing documentation

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Adopted Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Adoption decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- Agriculture domain boundary: [`DOMAIN.md`](../../domains/agriculture/DOMAIN.md)
- Agriculture architecture: [`ARCHITECTURE.md`](../../domains/agriculture/ARCHITECTURE.md)
- Agriculture lifecycle: [`DATA_LIFECYCLE.md`](../../domains/agriculture/DATA_LIFECYCLE.md)
- Agriculture sensitivity and rights posture: [`SENSITIVITY.md`](../../domains/agriculture/SENSITIVITY.md)
- Domain-side runbook orientation: [`docs/domains/agriculture/runbooks/README.md`](../../domains/agriculture/runbooks/README.md)

### Repository evidence and orchestration

- Agriculture domain workflow: [`.github/workflows/domain-agriculture.yml`](../../../.github/workflows/domain-agriculture.yml)
- Documentation metadata workflow: [`.github/workflows/docs-meta-block.yml`](../../../.github/workflows/docs-meta-block.yml)
- Aggregate validator workflow: [`.github/workflows/validator-suite.yml`](../../../.github/workflows/validator-suite.yml)
- Review routing: [`.github/CODEOWNERS`](../../../.github/CODEOWNERS)
- Agriculture tests index: [`tests/domains/agriculture/README.md`](../../../tests/domains/agriculture/README.md)
- Agriculture release boundary: [`release/agriculture/README.md`](../../../release/agriculture/README.md)

[Back to top](#top)

---

## Evidence basis

| Evidence | What it supports | What it cannot prove |
|---|---|---|
| `main@2c010b36609bf2ceb94e5a2d61fa62493e6f298f` | Immutable repository checkpoint for this review | Runtime or public behavior by commit alone |
| Target prior blob `8b137891…` | The target was tracked but blank in substance | Why it was left blank or whether anyone relied on that state |
| Directory tree `c0bd163c…` | Exact five-child inventory at the checkpoint | Current operational maturity |
| Four child runbook blobs recorded in metadata | Current document bytes and their self-declared/evidence-backed maturity | Live-source, policy, review, release, or publication state beyond their support |
| Accepted ADR-0029 and adopted Directory Rules blob | Placement, one-owner, README inheritance, and non-authority rules | Implementation or operational approval |
| CODEOWNERS blob `dd2a84aa…` | Verified GitHub review route | Independent review or stewardship authority |
| `domain-agriculture.yml` | Current read-only orchestration and explicit bounded/held posture | Agriculture truth, proof, release, deployment, or publication |
| Documentation and validator workflows | Expected repository QA paths | Hosted result for a future branch until those checks execute |

Memory, generic best practice, and proposal repetition are not implementation evidence.

[Back to top](#top)

---

## Document change rollback

This file is documentation-only and has no runtime, source, lifecycle, release, deployment, promotion, rollback-execution, or publication side effect.

- **Before merge:** close or abandon the draft pull request. No public or governed data state needs reversal.
- **After merge:** revert the implementation commit or submit a smaller forward-fix PR against the actual merged head. Do not rewrite shared history.
- **If links or child responsibilities changed after merge:** prefer a forward fix that preserves one writable local boundary rather than restoring parallel or ambiguous authority.
- **Historical preimage:** blob `8b137891791fe96927ad78e64b0aad7bded08bdc` restores the prior one-byte blank file exactly.

A Git revert of this README would not correct any separate source, evidence, policy, release, deployment, or publication state. Those transitions require their own owning correction paths.

[Back to top](#top)
