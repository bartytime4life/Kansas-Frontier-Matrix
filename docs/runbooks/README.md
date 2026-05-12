<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-runbooks-readme
title: docs/runbooks — Operational Runbooks Index
type: standard
version: v1
status: draft
owners: docs-steward; subsystem-owners (per-runbook)
created: 2026-05-12
updated: 2026-05-12
policy_label: public
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/README.md
  - docs/architecture/ui/README.md
  - docs/architecture/governed-ai/README.md
  - docs/security/README.md
  - docs/adr/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - data/receipts/README.md
  - data/proofs/README.md
  - release/README.md
  - migrations/rollback/README.md
tags: [kfm, runbooks, operations, validation, rollback, correction, governance]
notes:
  - Canonical-root child README per directory-rules.md §15 README Contract.
  - Per-runbook PROPOSED file list sourced from the KFM Whole-UI + Governed AI Expansion Report (Appendix B).
  - Implementation maturity of named runbooks is PROPOSED until verified against the mounted repository.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/runbooks/` — Operational Runbooks Index

> The canonical home for KFM operational procedures: **local development setup, validation runs, rollback drills, kill-switch procedures, correction flows, and incident response.** Runbooks turn governance doctrine into repeatable, reviewable, reversible action.

<!-- Badges: targets are placeholders pending CI workflow / policy verification. -->
![Status](https://img.shields.io/badge/status-draft-blue?style=flat-square)
![Authority](https://img.shields.io/badge/authority-canonical-success?style=flat-square)
![Policy](https://img.shields.io/badge/policy_label-public-lightgrey?style=flat-square)
![CI](https://img.shields.io/badge/ci-TODO_verify_workflow-orange?style=flat-square)
![Last reviewed](https://img.shields.io/badge/last_reviewed-2026--05--12-informational?style=flat-square)
![ADR](https://img.shields.io/badge/ADR-pending-yellow?style=flat-square)

| Field | Value |
|---|---|
| **Status** | draft (PROPOSED — pending repo verification) |
| **Authority level** | Canonical (`docs/` is the human-facing control plane) |
| **Owners** | Docs steward · per-subsystem owner (UI, Governed AI, Story, Review, Map, Release) |
| **Policy label** | public |
| **Last reviewed** | 2026-05-12 |

> [!IMPORTANT]
> Runbooks **describe** governed procedures; they do not **authorize** them. A runbook never overrides policy, review state, or release state. If a runbook step appears to bypass the trust membrane (`RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`), stop and open a `docs/registers/DRIFT_REGISTER.md` entry instead of proceeding.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Authority level](#2-authority-level)
- [3. Status](#3-status)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does NOT belong here](#5-what-does-not-belong-here)
- [6. Runbook index (PROPOSED)](#6-runbook-index-proposed)
- [7. Runbook structure (required sections)](#7-runbook-structure-required-sections)
- [8. Inputs](#8-inputs)
- [9. Outputs](#9-outputs)
- [10. Diagram — runbooks across the KFM lifecycle](#10-diagram--runbooks-across-the-kfm-lifecycle)
- [11. Validation](#11-validation)
- [12. Review burden](#12-review-burden)
- [13. Lifecycle integration matrix](#13-lifecycle-integration-matrix)
- [14. Correction and rollback model](#14-correction-and-rollback-model)
- [15. Related folders](#15-related-folders)
- [16. ADRs](#16-adrs)
- [17. Open questions / NEEDS VERIFICATION](#17-open-questions--needs-verification)
- [Appendix A — Runbook authoring template](#appendix-a--runbook-authoring-template)
- [Appendix B — Reviewer checklist](#appendix-b--reviewer-checklist)

---

## 1. Purpose

**CONFIRMED.** `docs/runbooks/` owns the **executable-by-humans** procedures that KFM operators, subsystem owners, and stewards follow to bring up, validate, correct, and roll back governed surfaces. It is the action layer of the human-facing control plane: doctrine (`docs/doctrine/`) says *what must be true*, registers (`docs/registers/`) say *what governs what*, ADRs (`docs/adr/`) say *why a choice was made*, and runbooks here say **how to actually do the thing without breaking governance**.

Runbooks are read by people during real operations — first-time setup, a pre-release validation pass, a paged incident, a deprecation drill. They must be unambiguous, copy-paste-friendly where appropriate, and **explicit about what they cannot do** (publish, approve, mutate canonical stores, bypass policy).

[Back to top ↑](#top)

---

## 2. Authority level

**CONFIRMED:** Canonical, per `docs/doctrine/directory-rules.md` §5 ("Per-root authority status" — `docs/` is canonical for doctrine, registers, runbooks, ADRs) and §6.1 (`runbooks/` is the listed child of `docs/` for "ops procedures, rollback drills, validation runs").

Runbooks are **implementation-bearing documentation**: they encode steps a human (or a constrained automation harness) executes. They are **not** themselves policy, schema, or release decisions. If a runbook step needs to *authorize* something, the authority lives elsewhere (`policy/`, `release/`, an ADR, a `ReleaseManifest`, a `ReviewRecord`).

[Back to top ↑](#top)

---

## 3. Status

| Item | Status |
|---|---|
| `docs/runbooks/` as canonical home | **CONFIRMED** (directory-rules.md §6.1) |
| README contract sections below | **CONFIRMED** doctrine (directory-rules.md §15) |
| Specific runbook files listed in §6 | **PROPOSED** (Whole-UI + Governed AI Expansion Report, Appendix B) |
| Per-runbook owner assignments | **PROPOSED** — role-typed placeholders pending CODEOWNERS confirmation |
| Mounted-repo presence of the listed runbook files | **UNKNOWN** — not verified in this session |
| CI workflow names referenced in badges | **NEEDS VERIFICATION** — placeholders only |

[Back to top ↑](#top)

---

## 4. What belongs here

Runbooks that meet **all** of the following:

- **Human-executable.** A reader can follow the steps; an automation harness may also execute them, but the document is written for humans.
- **Operationally repeatable.** The same procedure produces the same governed outcome on repeat runs.
- **Lifecycle- or governance-bound.** The procedure crosses a lifecycle phase (`RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`), a governance boundary (policy, review, release), or an operational state (local dev, validation, rollback, kill switch, correction, incident).
- **Subsystem-scoped or governance-scoped.** Either a named subsystem (UI, Governed AI, Story, Review, Map, Pipelines) or a cross-cutting governance procedure (rollback drill, deprecation drill, secret-leak incident, drift triage).
- **Cite-or-abstain compliant.** Where a step relies on evidence, it points to an `EvidenceBundle`, a register entry, an ADR, a schema, a policy module, or a test/fixture — not to memory or to "we usually do X."
- **Reversible by design.** Every runbook that touches a public surface names its rollback target.

**File-naming convention (PROPOSED, per Whole-UI + Governed AI Expansion Report Appendix B):**

````text
<subsystem>_<LIFECYCLE_STAGE>.md
````

Examples: `ui_LOCAL_DEV.md`, `ui_VALIDATION.md`, `ui_ROLLBACK.md`, `governed_ai_LOCAL_DEV.md`, `governed_ai_VALIDATION.md`, `governed_ai_ROLLBACK.md`. The `LIFECYCLE_STAGE` slug is upper-snake (`LOCAL_DEV`, `VALIDATION`, `ROLLBACK`, `INCIDENT`, `CORRECTION`, `DEPRECATION`, `KILL_SWITCH`). The subsystem slug is lower-snake (`ui`, `governed_ai`, `story`, `review`, `map`, `pipelines`, `release`).

[Back to top ↑](#top)

---

## 5. What does NOT belong here

> [!WARNING]
> **A runbook never substitutes for a governed control surface.** If a piece of content actually *decides* something, it belongs in `policy/`, `release/`, `contracts/`, `schemas/`, or `control_plane/` — not here.

Do not place the following in `docs/runbooks/`:

- **Architecture overviews** — those belong in `docs/architecture/<subsystem>/README.md`.
- **Schemas, contracts, or DTOs** — `schemas/contracts/v1/...` and `contracts/` are the homes (per directory-rules.md §5 and ADR-0001).
- **Policy rules or Rego** — belongs in `policy/<subsystem>/`.
- **Release manifests, rollback cards, correction notices** as authoritative artifacts — those are emitted instances and live in `release/`, `data/receipts/`, `data/proofs/`. A runbook may *reference* and *produce* them but does not *store* them.
- **ADR text** — decisions go in `docs/adr/`. A runbook may cite the ADR but does not replace it.
- **Secrets, credentials, or environment-specific tokens** — never. If real secrets ever appear in `configs/`, write a runbook entry here and treat it as an incident (per directory-rules.md §10.3).
- **Source-of-truth tables** — registers under `docs/registers/` and `control_plane/` own those.
- **Generic third-party tool tutorials** — link out instead of re-hosting.
- **One-off shell commands with no governance context** — those belong in `scripts/` or a developer's local notes.

[Back to top ↑](#top)

---

## 6. Runbook index (PROPOSED)

> [!NOTE]
> The runbooks listed below are **PROPOSED** per the Whole-UI + Governed AI Expansion Report (Appendix B). Their **presence in the mounted repository is UNKNOWN** in this session. Mark each row CONFIRMED only after the file exists, is linked, and has been reviewed.

### 6.1 UI subsystem

| Path (PROPOSED) | Action | Truth label | Purpose | Owner |
|---|---|---|---|---|
| [`ui_LOCAL_DEV.md`](./ui_LOCAL_DEV.md) | CREATE | PROPOSED | Local UI setup, mock fixture wiring, feature-flag-off bring-up. | Docs steward + UI owner |
| [`ui_VALIDATION.md`](./ui_VALIDATION.md) | CREATE | PROPOSED | UI contract validation, accessibility checks, e2e smoke. | Docs steward + UI owner |
| [`ui_ROLLBACK.md`](./ui_ROLLBACK.md) | CREATE | PROPOSED | UI rollback, feature-flag disablement, schema deprecation steps. | Docs steward + UI owner |

### 6.2 Governed AI subsystem

| Path (PROPOSED) | Action | Truth label | Purpose | Owner |
|---|---|---|---|---|
| [`governed_ai_LOCAL_DEV.md`](./governed_ai_LOCAL_DEV.md) | CREATE | PROPOSED | `MockAdapter` and provider-adapter local dev bring-up. | Docs steward + Governed AI owner |
| [`governed_ai_VALIDATION.md`](./governed_ai_VALIDATION.md) | CREATE | PROPOSED | Focus Mode evidence resolution, citation validation, policy gate checks. | Docs steward + Governed AI owner |
| [`governed_ai_ROLLBACK.md`](./governed_ai_ROLLBACK.md) | CREATE | PROPOSED | AI adapter rollback, kill switch, response-envelope withdrawal. | Docs steward + Governed AI owner |

### 6.3 Cross-cutting (PROPOSED — not yet enumerated in source reports)

These are reasonable additions implied by directory-rules.md §10–§14 (incident response, migrations with rollback, drift triage). They are **PROPOSED** placeholders pending owner agreement; do **not** assume they exist.

| Path (PROPOSED) | Truth label | Purpose | Owner |
|---|---|---|---|
| `secret_leak_INCIDENT.md` | PROPOSED | Real secret found in `configs/` → rotate, audit, write entry (per directory-rules.md §10.3). | Security owner + docs steward |
| `migration_ROLLBACK.md` | PROPOSED | Migration rollback drill referencing `migrations/rollback/` (per directory-rules.md §10.4 and §14). | Migration owner + docs steward |
| `drift_TRIAGE.md` | PROPOSED | Triage flow for entries added to `docs/registers/DRIFT_REGISTER.md`. | Docs steward + subsystem owner |
| `release_DEPRECATION.md` | PROPOSED | Deprecation drill referencing `control_plane/deprecation_register.yaml`. | Release owner + docs steward |
| `kill_switch_DRILL.md` | PROPOSED | Periodic kill-switch verification (fail-closed publish gate). | Release owner + security owner |

[Back to top ↑](#top)

---

## 7. Runbook structure (required sections)

Every runbook in this folder **MUST** include the sections below, in order. Sections may be expanded or sub-divided; none may be silently omitted. Where a section does not apply, write "Not applicable — \<reason\>" rather than removing the heading.

1. **Header / meta block** — KFM Meta Block v2 (per `docs/doctrine/` standard doc rules).
2. **Purpose** — one paragraph; who runs this, when, why.
3. **Scope** — subsystem(s), lifecycle phase(s), and policy surface(s) touched.
4. **Preconditions** — required state, flags, fixtures, branches, access, receipts.
5. **Inputs** — files, manifests, fixtures, envelopes, configs (paths + types).
6. **Procedure** — numbered steps; commands in fenced code blocks with explicit language tags; destructive steps clearly flagged.
7. **Expected outputs** — receipts, validation reports, manifests, UI states, log lines.
8. **Failure modes** — common failure paths with reason codes (e.g., `MISSING_RECEIPT`, `SCHEMA_MISMATCH`, `RIGHTS_UNKNOWN`) per the Decision Outcome reason-code catalog.
9. **Rollback target** — explicit prior-safe state or `RollbackCard` reference. **Required.**
10. **Correction path** — when to issue a `CorrectionNotice` instead of (or in addition to) rolling back.
11. **Evidence references** — `EvidenceBundle`, `EvidenceRef`, ADR, schema, policy, fixture, test paths.
12. **Validation hooks** — which workflows / validators / tests confirm a successful run.
13. **Review burden** — who must sign off; whether release-duty separation applies.
14. **Last reviewed** — ISO date.

> [!TIP]
> A runbook that lacks a **rollback target** is a drift candidate. Open an entry in `docs/registers/DRIFT_REGISTER.md` rather than merging the runbook.

[Back to top ↑](#top)

---

## 8. Inputs

What feeds into the runbooks in this folder:

- **Doctrine** — `docs/doctrine/directory-rules.md`, `docs/doctrine/lifecycle-law.md`, `docs/doctrine/trust-membrane.md`, `docs/doctrine/truth-posture.md`.
- **Architecture** — `docs/architecture/<subsystem>/README.md`, `BOUNDARIES.md`, `ROUTE_MAP.md`, `STATE_OWNERSHIP.md`, `CONTINUITY_NOTES.md`.
- **Object families** — `contracts/OBJECT_MAP.md` and named contracts (`EvidenceBundle`, `EvidenceRef`, `RunReceipt`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `RollbackCard`, `PolicyDecision`, response envelopes).
- **Schemas** — `schemas/contracts/v1/<subsystem>/...`.
- **Policy** — `policy/<subsystem>/`.
- **Fixtures and tests** — `tests/fixtures/<subsystem>/`, `tests/e2e/`, `tests/accessibility/`.
- **Registers** — `docs/registers/DRIFT_REGISTER.md`, `docs/registers/VERIFICATION_BACKLOG.md`, `control_plane/policy_gate_register.yaml`, `control_plane/release_state_register.yaml`.
- **Generated artifacts** — `data/receipts/`, `data/proofs/`, `data/manifests/`, `release/`.

[Back to top ↑](#top)

---

## 9. Outputs

What runbook execution produces (none of which are stored *here* — runbooks reference them):

- **Generated artifacts** under `data/receipts/`, `data/proofs/`, `data/manifests/`, `release/`.
- **Validation reports** consumed by CI summary jobs (e.g., the proposed `tools/ci/render_ui_validation_summary.py` path).
- **`CorrectionNotice` / `RollbackCard` records** in `release/` when correction/rollback runbooks fire.
- **Drift entries** in `docs/registers/DRIFT_REGISTER.md` when a runbook surfaces an unresolved issue.
- **Verification-backlog tickets** in `docs/registers/VERIFICATION_BACKLOG.md` when a step cannot be checked in the current session.

[Back to top ↑](#top)

---

## 10. Diagram — runbooks across the KFM lifecycle

This diagram is illustrative of the **PROPOSED** mapping of runbook stages onto the canonical KFM lifecycle. Exact runbook-to-phase bindings should be confirmed against mounted-repo workflows.

````mermaid
flowchart LR
  subgraph LIFECYCLE["KFM Lifecycle (CONFIRMED doctrine)"]
    R[RAW] --> WQ["WORK / QUARANTINE"]
    WQ --> P[PROCESSED]
    P --> CT["CATALOG / TRIPLET"]
    CT --> PUB[PUBLISHED]
  end

  subgraph RUNBOOKS["docs/runbooks/ (PROPOSED)"]
    LD["*_LOCAL_DEV"]
    VAL["*_VALIDATION"]
    RB["*_ROLLBACK"]
    KS["kill_switch_DRILL"]
    INC["secret_leak_INCIDENT"]
    DEP["release_DEPRECATION"]
    DRF["drift_TRIAGE"]
  end

  LD -.bring up locally with mock fixtures.-> WQ
  VAL -.gate promotion with receipts and policy.-> P
  VAL -.gate catalog and triplet closure.-> CT
  KS -.fail-closed publish gate.-> PUB
  RB -.restore prior digest-pinned release.-> PUB
  INC -.rotate, audit, contain.-> R
  DEP -.sunset and remove mirror.-> CT
  DRF -.feed registers when drift observed.-> WQ

  classDef phase fill:#eef6ff,stroke:#2b6cb0,color:#1a365d
  classDef book fill:#fef3c7,stroke:#a16207,color:#713f12
  class R,WQ,P,CT,PUB phase
  class LD,VAL,RB,KS,INC,DEP,DRF book
````

> [!NOTE]
> **NEEDS VERIFICATION.** The arrows above describe the **doctrinal** binding of runbook stages to lifecycle phases. Whether a specific runbook actually fires at the indicated transition depends on workflow wiring that has not been inspected here.

[Back to top ↑](#top)

---

## 11. Validation

How runbooks themselves are validated (separate from the validation procedures they describe):

- **Link integrity** — every relative link in a runbook resolves; absolute links are reviewed for stability.
- **Schema-reference integrity** — every `schemas/contracts/v1/...` path cited exists.
- **Contract-reference integrity** — every contract / object family named (`EvidenceBundle`, `RunReceipt`, etc.) is listed in `contracts/OBJECT_MAP.md`.
- **Rollback-target presence** — automated check that every runbook contains a non-empty rollback section.
- **Reviewer sign-off** — per directory-rules.md §15, runbook PRs require the docs steward plus the relevant subsystem owner.
- **CI surfacing** — the proposed `.github/workflows/ui-governed.yml` and `.github/workflows/contracts-ui-ai.yml` are intended to surface runbook-relevant validation summaries. **NEEDS VERIFICATION** that these workflow names are the live ones in the mounted repo.

<details>
<summary>Suggested local validation pass (PROPOSED — adjust to repo conventions)</summary>

````bash
# Markdown link check (replace with the repo's actual tool)
# CONFIRMED need: link integrity. Tool choice: NEEDS VERIFICATION.
markdown-link-check docs/runbooks/*.md

# Schema-path existence sweep (illustrative)
grep -hoE 'schemas/contracts/v1/[A-Za-z0-9_/.-]+\.schema\.json' docs/runbooks/*.md \
  | sort -u \
  | while read p; do test -e "$p" || echo "MISSING: $p"; done

# Rollback-target presence (illustrative)
for f in docs/runbooks/*.md; do
  grep -q -i '^## .*rollback' "$f" || echo "NO ROLLBACK SECTION: $f"
done
````

These commands are **illustrative** and intentionally minimal. Replace with the repo's validator tools once verified.

</details>

[Back to top ↑](#top)

---

## 12. Review burden

| Change to a runbook | Required reviewers |
|---|---|
| Typo, link fix, clarification | Docs steward |
| Step addition or removal (non-policy) | Docs steward + subsystem owner |
| Step that touches policy, release, or rollback semantics | Docs steward + subsystem owner + release/policy owner |
| New runbook (new file in `docs/runbooks/`) | Docs steward + subsystem owner; cite directory-rules.md §15 in the PR |
| Runbook that bends a doctrinal invariant | ADR required (per directory-rules.md §17); reviewed by doctrine owner |

Reviewer authority and CODEOWNERS mapping are **NEEDS VERIFICATION** until the repo's `CODEOWNERS` (or `.github/CODEOWNERS`) is inspected.

[Back to top ↑](#top)

---

## 13. Lifecycle integration matrix

How runbook families bind to KFM control objects. **CONFIRMED** doctrine for the object families; **PROPOSED** for the specific runbook-to-object mappings (sourced from the Whole-UI + Governed AI Expansion Report §24 "Update-propagation matrix").

| Runbook family | Owns / drives | Reads | Emits | Rollback path |
|---|---|---|---|---|
| `*_LOCAL_DEV` | Local bring-up; mock fixtures; feature-flag-off mode | `tests/fixtures/<subsystem>/`, `runtime/mock/` | Local logs only (no `RunReceipt` in CATALOG/PUBLISHED) | Re-clone; feature flags off |
| `*_VALIDATION` | Contract, accessibility, policy, e2e smoke | Schemas, fixtures, policy modules, `EvidenceBundle` | `ValidationReport`, `PolicyDecision`, drift entries if needed | Block promotion; do not advance phase |
| `*_ROLLBACK` | Withdraw or supersede published surface | `ReleaseManifest`, `EvidenceBundle`, `data/receipts/` | `RollbackCard`, optional `CorrectionNotice` | Restore prior digest-pinned release |
| `kill_switch_DRILL` | Verify fail-closed publish gate | Workflow check rollups, branch protection | Test-only fail receipts | Re-arm; revert kill-switch fixture |
| `secret_leak_INCIDENT` | Containment, rotation, audit | `configs/`, secret-store references | Incident record, rotation log, drift entry | Rotate again if compromise persists |
| `*_CORRECTION` | Defect classification, supersession | `EvidenceBundle`, prior `ReleaseManifest` | `CorrectionNotice`, superseding `ReleaseManifest` | Roll back to prior release if correction infeasible |
| `*_DEPRECATION` | Sunset and remove mirror | `control_plane/deprecation_register.yaml` | Deprecation record, drift entry on missed sunset | Re-mirror temporarily |

[Back to top ↑](#top)

---

## 14. Correction and rollback model

**CONFIRMED doctrine** (from `KFM_Unified_Implementation_Architecture_Build_Manual` correction-and-rollback model): correction and rollback are **publication requirements, not afterthoughts**. A released claim, layer, catalog record, artifact, or AI answer must have a visible correction path and rollback target before it is treated as safely publishable.

**PROPOSED** runbook posture by defect class:

| Defect class | Correction posture | Rollback posture |
|---|---|---|
| Evidence gap | ABSTAIN or withdraw unsupported claim | Restore prior evidence-supported release |
| Rights defect | DENY public use; quarantine source/artifact | Withdraw affected artifacts |
| Sensitivity leak | Redact/generalize and notify stewards | Immediate public disablement |
| Geometry defect | Rebuild derivative layer and `EvidenceBundle` | Restore previous digest-pinned artifact |
| Temporal defect | Correct valid/source/retrieval/release time | Mark stale until rebuilt |
| Policy defect | Re-run policy and decision envelope | Disable route/layer if gate failed |
| AI answer defect | Invalidate `AIReceipt` and response envelope | Remove answer; preserve `EvidenceBundle` |
| Catalog defect | Re-emit catalog closure after proof repair | Restore previous catalog state |

> [!CAUTION]
> A rollback is **never** a hidden file copy. It is a governed state transition that emits a `RollbackCard`, updates the relevant `ReleaseManifest`, preserves audit receipts, and is reviewable. If a runbook step ever silently mutates a published artifact, treat it as a doctrine violation and open an ADR or drift entry.

[Back to top ↑](#top)

---

## 15. Related folders

- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — placement law, README contract.
- [`docs/architecture/`](../architecture/) — subsystem boundaries, route maps, state ownership.
- [`docs/adr/`](../adr/) — file-home and trust-boundary decisions runbooks must respect.
- [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) — opened by runbooks when drift is observed.
- [`docs/registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) — opened when a runbook step cannot be checked.
- [`docs/security/`](../security/) — incident-response posture; pairs with secret-leak and kill-switch runbooks.
- [`policy/`](../../policy/) — gate logic invoked by validation runbooks.
- [`tests/`](../../tests/) and [`fixtures/`](../../fixtures/) — what validation runbooks exercise.
- [`data/receipts/`](../../data/receipts/), [`data/proofs/`](../../data/proofs/), [`data/manifests/`](../../data/manifests/) — emitted artifacts referenced by runbooks.
- [`release/`](../../release/) — `ReleaseManifest`, `RollbackCard`, `CorrectionNotice` homes.
- [`migrations/rollback/`](../../migrations/rollback/) — every migration must have a rollback runbook entry.
- [`runtime/mock/`](../../runtime/mock/) — `MockAdapter` used by local-dev runbooks.

> [!NOTE]
> All paths above are **PROPOSED** as link targets per directory-rules.md and the Whole-UI + Governed AI Expansion Report. Their **presence in the mounted repository is UNKNOWN** in this session.

[Back to top ↑](#top)

---

## 16. ADRs

Runbooks must remain consistent with active ADRs. The following are **PROPOSED** and relevant to runbook authors; they are not confirmed present in the mounted repo:

- `ADR-0001-schema-home.md` — schemas home (`schemas/contracts/v1/...`).
- `ADR-ui-schema-home.md` — UI schema home decision.
- `ADR-maplibre-adapter-boundary.md` — MapLibre adapter and renderer containment.
- `ADR-focus-model-adapter-boundary.md` — no direct browser-to-model path.
- `ADR-story-node-3d-boundary.md` — Story Node and 3D boundary.

When a runbook step appears to contradict an ADR, **stop** and open a PR amending the ADR (or the runbook) rather than diverging silently.

[Back to top ↑](#top)

---

## 17. Open questions / NEEDS VERIFICATION

Tracked here for the docs steward; mirror in `docs/registers/VERIFICATION_BACKLOG.md` once that register exists.

- **NEEDS VERIFICATION** — Whether the runbook files listed in §6 already exist in the mounted repository, and if so, what their current contents and review state are.
- **NEEDS VERIFICATION** — Whether the proposed file-naming convention (`<subsystem>_<LIFECYCLE_STAGE>.md`) is the convention actually in use, or whether the repo uses an alternative casing/separator.
- **NEEDS VERIFICATION** — Which CI workflow(s) surface runbook-validation summaries. Badge targets above are placeholders.
- **NEEDS VERIFICATION** — `CODEOWNERS` mapping for `docs/runbooks/`. Owner names in §6 are role-typed placeholders.
- **OPEN** — Whether kill-switch, secret-leak, deprecation, drift-triage, and migration-rollback runbooks should live here as a separate "cross-cutting" sub-folder (`docs/runbooks/cross/`) or remain flat. Recommend keeping flat until ≥ ~12 files exist.
- **OPEN** — Whether runbooks should carry a per-file machine-readable manifest (front-matter or sibling `*.runbook.yaml`) for automated index generation. Defer to ADR if it becomes useful.

[Back to top ↑](#top)

---

## Last reviewed

`2026-05-12` — initial draft. ISO date; re-review when any of the following changes: directory rules §6.1 / §15, the Whole-UI + Governed AI Expansion Report Appendix B, or the listed runbook files.

---

## Appendix A — Runbook authoring template

A new runbook should start from this skeleton. Copy, then fill. Do **not** remove sections silently.

<details>
<summary>Click to expand the runbook template</summary>

````markdown
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-<subsystem>-<stage>
title: <Subsystem> — <Stage> Runbook
type: standard
version: v1
status: draft
owners: <docs-steward>; <subsystem-owner>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related:
  - docs/architecture/<subsystem>/README.md
  - contracts/OBJECT_MAP.md
  - policy/<subsystem>/README.md
tags: [kfm, runbook, <subsystem>, <stage>]
notes:
  - PROPOSED until verified against mounted repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# <Subsystem> — <Stage> Runbook

> One-line purpose. Who runs this, when, why.

## 1. Scope
Subsystem, lifecycle phase, policy surface.

## 2. Preconditions
Required state, flags, fixtures, branches, access, receipts.

## 3. Inputs
Files, manifests, fixtures, envelopes (paths + types).

## 4. Procedure
1. Step …
2. Step …
3. Step (mark destructive steps clearly).

## 5. Expected outputs
Receipts, validation reports, manifests, UI states.

## 6. Failure modes
Reason codes (e.g., MISSING_RECEIPT, SCHEMA_MISMATCH, RIGHTS_UNKNOWN) and the recovery path.

## 7. Rollback target
Explicit prior-safe state or `RollbackCard` reference. **Required.**

## 8. Correction path
When to issue a `CorrectionNotice` instead of (or in addition to) rolling back.

## 9. Evidence references
EvidenceBundle / EvidenceRef / ADR / schema / policy / fixture / test paths.

## 10. Validation hooks
Which workflows / validators / tests confirm a successful run.

## 11. Review burden
Who must sign off; release-duty separation if applicable.

## Last reviewed
YYYY-MM-DD
````

</details>

[Back to top ↑](#top)

---

## Appendix B — Reviewer checklist

Use this when reviewing a PR that adds or edits a runbook. Pairs with the path-validation checklist in directory-rules.md §16.

- [ ] **Right home.** The file is a runbook (human-executable, lifecycle/governance-bound) and not actually a policy, schema, contract, ADR, or release decision.
- [ ] **Naming.** Filename matches `<subsystem>_<LIFECYCLE_STAGE>.md` (PROPOSED convention).
- [ ] **Header.** KFM Meta Block v2 present; `doc_id`, `owners`, `status`, `policy_label` filled.
- [ ] **Purpose paragraph.** Clearly states who runs it, when, why.
- [ ] **Preconditions explicit.** Required state, flags, fixtures listed.
- [ ] **Steps are reproducible.** Commands have language-tagged fences; destructive steps flagged with a callout.
- [ ] **Cite-or-abstain.** Every evidence-bearing step references an `EvidenceBundle`, ADR, schema, fixture, or test path.
- [ ] **Rollback target.** Section present and non-empty.
- [ ] **Correction path.** Section present; defect class addressed.
- [ ] **Failure modes.** Reason codes named and mapped to recovery.
- [ ] **Trust membrane respected.** No step reaches `RAW`, `WORK`, `QUARANTINE`, canonical stores, vector indexes, model runtimes, credentials, or internal service handles from a public surface.
- [ ] **No secret in `configs/` or runbook text.** Triggers the secret-leak incident runbook.
- [ ] **Links validate.** Relative links resolve; cited schemas/contracts exist.
- [ ] **Last reviewed date updated.**

[Back to top ↑](#top)

---

> **Related docs:** [`docs/README.md`](../README.md) · [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) · [`docs/architecture/README.md`](../architecture/README.md) · [`docs/adr/README.md`](../adr/README.md) · [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) · [`docs/security/README.md`](../security/README.md)
>
> **Last updated:** 2026-05-12 · **Authority:** Canonical (per `docs/doctrine/directory-rules.md` §6.1) · [Back to top ↑](#top)
