<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-uuid>
title: Corrections Are First-Class
type: standard
version: v1
status: draft
owners: <TODO: doctrine maintainers (e.g., Governance Steward + Release Authority)>
created: 2026-05-12
updated: 2026-05-12
policy_label: public
related:
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-posture.md
  - docs/doctrine/ai-as-assistant.md
  - docs/architecture/release-and-publication.md
  - docs/runbooks/RB-CORRECTION-ROUTINE.md
  - docs/runbooks/RB-ROLLBACK-EXECUTION.md
  - docs/runbooks/RB-PRIVACY-REQUEST.md
  - docs/runbooks/RB-INCIDENT-INTEGRITY-FAILURE.md
  - schemas/contracts/v1/correction_notice.schema.json
  - schemas/contracts/v1/rollback_plan.schema.json
  - schemas/contracts/v1/supersession_record.schema.json
  - tests/corrections/
  - tests/rollback/
tags: [kfm, doctrine, corrections, rollback, release, governance, trust]
notes:
  - Codifies "Corrections are first-class" as a normative KFM doctrine.
  - Operationalizes steps 10 and 11 of the eleven-step publication transition.
  - Sets the failure outcome: ERROR if a published artifact lacks a correction path.
[/KFM_META_BLOCK_V2] -->

# Corrections Are First-Class

**Doctrine for how Kansas Frontier Matrix handles errors, disputes, supersessions, withdrawals, and rollback — as named, schema-bearing, publicly visible operations, never as silent edits.**

![Status](https://img.shields.io/badge/status-draft-orange)
![Doctrine](https://img.shields.io/badge/track-doctrine-blue)
![Trust posture](https://img.shields.io/badge/posture-cite_or_abstain-1f6feb)
![Failure mode](https://img.shields.io/badge/failure-fail_closed-critical)
![Last updated](https://img.shields.io/badge/updated-2026--05--12-lightgrey)

> **Status:** draft · **Owners:** `<TODO: Governance Steward + Release Authority>` · **Last updated:** 2026-05-12
>
> **Doctrine track:** [`docs/doctrine/`](./) · **Companion docs:** [`lifecycle-law.md`](./lifecycle-law.md) · [`trust-posture.md`](./trust-posture.md) · [`ai-as-assistant.md`](./ai-as-assistant.md)

---

## Quick jump

- [Why this is doctrine](#why-this-is-doctrine)
- [Scope and definitions](#scope-and-definitions)
- [The four invariants](#the-four-invariants)
- [Triggering scenarios and required behavior](#triggering-scenarios-and-required-behavior)
- [Trust-object schemas](#trust-object-schemas)
- [Correction-and-rollback flow](#correction-and-rollback-flow)
- [Public visibility rules](#public-visibility-rules)
- [AI boundary in corrections](#ai-boundary-in-corrections)
- [Validation and tests](#validation-and-tests)
- [Day-2 connections](#day-2-connections)
- [Acceptance checklist](#acceptance-checklist)
- [Anti-patterns](#anti-patterns)
- [Related docs](#related-docs)

---

## Why this is doctrine

A system that publishes evidence must, eventually, publish something wrong. KFM's commitment is not to be infallible; it is to **fail openly and recover honestly**. Three properties of real-world evidence force this stance:

1. **Sources change after publication.** Gauges are re-calibrated, units flip mid-day, parcel rolls are corrected, oral-history transcripts are revised, satellite products are reprocessed, and observation networks restate their archives. A release that cannot be superseded is a release that quietly drifts away from its source.
2. **Rights and sensitivity are not static.** A permission can be withdrawn. A record can be re-classified by a cultural authority. A living person can request review. A `PolicyDecision` that was sound at release time can become unsound the next morning. The system MUST be able to act on that without overwriting history.
3. **Mistakes happen.** Validators have gaps. Reviewers miss things. Pipelines have bugs. Models hallucinate. A correction path is not an admission of weakness — it is the operational shape of integrity.

KFM names this stance in its core principles register as the **CONFIRMED doctrine "Corrections are first-class"** with the build rule that corrections, withdrawals, supersessions, rollback, and lineage are visible and queryable, and the failure outcome `ERROR if a published artifact lacks a correction path`. This doctrine document is that principle in operational form.

> [!IMPORTANT]
> Silent replacement is a defect. If a public artifact is changed without a `CorrectionNotice`, a `SupersessionRecord`, or a `RollbackPlan`, the change is not a correction — it is a regression of trust posture and MUST be reverted.

---

## Scope and definitions

This doctrine governs every change to material that has crossed the `PUBLISHED` boundary defined in [`lifecycle-law.md`](./lifecycle-law.md). It does not govern routine edits within `data/work/` or candidate iteration within `data/processed/` before release.

| Term | Meaning |
|---|---|
| **Correction** | Any post-release change to a published claim, dataset, layer, export, or report that alters its meaning, scope, geometry, time, rights, or sensitivity. |
| **Supersession** | A correction that replaces a published artifact with a new release while retaining the old release in audit. |
| **Withdrawal** | A correction that removes a published artifact from public routes (typically for rights or sensitivity reasons) while retaining audit. |
| **Rollback** | The operational reversion of public pointers, caches, and indexes from one release to a prior `target_release_id`, accompanied by a notice. |
| **Public notice** | The human-readable record visible at a stable URL describing what changed and why, with pointers into the affected evidence. |
| **First-class** | Possessing its own schema, fixture, validator, receipt path, test directory, runbook, and public visibility rule — equivalent in standing to publication itself. |

Lifecycle stage names (`RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`) carry the meaning defined in [`lifecycle-law.md`](./lifecycle-law.md) and MUST NOT be paraphrased in correction artifacts.

---

## The four invariants

Every correction operation in KFM satisfies all four of the invariants below. A change that violates any one of them is not a correction — it is a defect.

| # | Invariant | What it means in practice | Failure outcome |
|---|---|---|---|
| **I-1** | **Named operation** | Every change has a typed artifact (`CorrectionNotice`, `SupersessionRecord`, `RollbackPlan`, withdrawal). There is no "fix in place." | `ERROR` if a published asset is mutated without a typed correction artifact. |
| **I-2** | **Append-only history** | Corrections add records. Old releases, manifests, and proof packs remain inspectable; pointers move, history does not. | `ERROR` if any audit record is overwritten in place. |
| **I-3** | **Public visibility** | The fact that a correction occurred, its scope, its reason, and where to inspect the evidence are reachable from a stable public URL. | `ERROR` if a correction is applied without a public notice path. |
| **I-4** | **Path to rebuild** | Every release MUST declare a `rollback_target` and a `correction_path` at publication time, before public exposure. | `DENY release.unreviewed` if a `ReleaseManifest` lacks `correction_path` or `rollback_target`. |

> [!NOTE]
> Invariants **I-1** and **I-2** are CONFIRMED at the doctrine layer. Invariants **I-3** and **I-4** are CONFIRMED at the doctrine layer but the exact route, path, and field names that satisfy them are `PROPOSED` until inspected in the implementation.

[⬆ Back to top](#corrections-are-first-class)

---

## Triggering scenarios and required behavior

Eight named scenarios trigger this doctrine. Each has a required model behavior (what the system MUST do internally) and a required public behavior (what users MUST be able to see). This table is the reference for the **Correction validator** (`tests/corrections/`) and the **Rollback validator** (`tests/rollback/`).

| Scenario | Required model behavior | Required public behavior |
|---|---|---|
| **Error in claim** | Create `CorrectionNotice`; mark affected claims; build superseding candidate through the standard release path. | Public notice visible; old artifact NOT silently overwritten. |
| **Disputed claim** | Attach dispute status; route to steward review queue with `review_state: steward_review`. | `ABSTAIN` or attach caveat to public answer until resolved if the dispute is material. |
| **Source update** | New `SourceDescriptor` / `DatasetVersion`; emit a comparison receipt versus the prior version. | Supersession only through the release process. No drift-by-pipeline. |
| **Rights change** | `PolicyDecision` update; possible withdrawal; `ReviewRecord` for legal sign-off if required. | `DENY` public access if rights no longer support publication. |
| **Sensitivity change** | Apply redaction, generalization, or withdrawal; emit a `CorrectionNotice`. | Exact-location exposure closed immediately. Public learns scope of redaction, not the redacted content. |
| **Stale evidence** | Mark stale on the affected `DatasetVersion` / `LayerManifest`; runtime returns `ABSTAIN freshness.stale` or attaches a stale caveat. | Do not pretend current status. The stale state MUST be visible in the Evidence Drawer. |
| **Superseded artifact** | Create `SupersessionRecord` with `old_release` / `new_release` and `effective_time`. | Public sees `superseded_by` link on the old artifact and a forward pointer to the replacement. |
| **Withdrawn release** | Withdraw assets from public routes; preserve audit; require `RollbackPlan` or a withdrawal notice. | Public sees withdrawal reason at a stable URL; old assets are not silently 404'd without context. |

> [!WARNING]
> A correction that lowers the visible **sensitivity** of a record (e.g., re-exposing a previously redacted exact location) MUST traverse the **same review gate** as the original release. It is not a "rollback in the easy direction." The default outcome for ambiguous reclassification is `DENY policy.sensitive_geometry`.

[⬆ Back to top](#corrections-are-first-class)

---

## Trust-object schemas

The schemas below are the doctrinal shape of correction artifacts. Field names are CONFIRMED from the project's core schemas register; their **canonical home** (file path under `schemas/contracts/v1/`) is `PROPOSED` until inspected in the implementation. Implementations MUST publish JSON Schema documents that conform to **JSON Schema 2020-12** unless an ADR records a different choice.

### `CorrectionNotice`

The primary public artifact of this doctrine. Every correction emits one.

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `notice_id` | string | ✓ | Stable identifier; format `cn-<scope>-<date>-<seq>`. |
| `affected_claims` / `affected_assets` | array | ✓ | At least one MUST be non-empty. |
| `reason` | enum / string | ✓ | Reason code (e.g., `unit_mismatch`, `rights_revoked`, `sensitivity_reclassified`, `source_revised`). |
| `severity` | enum | ✓ | `minor`, `moderate`, `severe`, `integrity` — drives review and rollback decisions. |
| `source_refs` | array of `EvidenceRef` | ✓ | Evidence supporting the reason. `EvidenceRef` MUST resolve to a real `EvidenceBundle`. |
| `created_by_role` | string | ✓ | Role identifier (`hydrology_steward`, `legal_reviewer`, `admin`, etc.). |
| `review_state` | enum | ✓ | One of: `draft`, `steward_review`, `approved`, `rejected`, `withdrawn`, `superseded`. |
| `public_summary` | string | ✓ | Plain-language summary safe for the Evidence Drawer. |
| `supersedes` / `superseded_by` | array | — | Pointers to previous / replacement claims or releases. |
| `rollback_target` | string | — | `release_id` to revert to if rollback is executed. |

<details>
<summary>Illustrative <code>CorrectionNotice</code> JSON (hydrology unit-mismatch example, labeled illustrative)</summary>

```json
{
  "notice_id": "cn-cl-001-2024-04-23",
  "affected_claims": ["cl-001"],
  "reason": "unit_mismatch",
  "severity": "moderate",
  "source_refs": ["ref-cl-001-001"],
  "created_by_role": "hydrology_steward",
  "review_state": "approved",
  "public_summary": "The gauge value previously published assumed feet; the source switched to meters mid-day. The claim is superseded.",
  "supersedes": [],
  "superseded_by": ["cl-002"],
  "rollback_target": "rel-hydrology-2024-04-21-baseline"
}
```

> This payload is illustrative. The canonical example is the worked hydrology slice in [`docs/architecture/release-and-publication.md`](../architecture/release-and-publication.md) (`NEEDS VERIFICATION` — path is `PROPOSED`).

</details>

### `RollbackPlan`

The operational counterpart to a severe-severity `CorrectionNotice`. Required at release time for every release; executed only when needed.

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `rollback_id` | string | ✓ | Stable identifier; format `rb-<release_id>`. |
| `release_id` | string | ✓ | The release being rolled back. |
| `target_release_id` | string | ✓ | The release pointers will revert to. MUST already exist and be inspectable. |
| `asset_pointer_changes` | array | ✓ | Concrete `{path, from, to}` redirections (API routes, layer registry entries, tile manifests). |
| `cache_invalidation` | array | ✓ | CDN / tile-cache / browser-cache keys to purge. |
| `verification_steps` | array | ✓ | Post-execution checks proving rollback succeeded (fetch + compare). |
| `public_notice` | string | ✓ | `notice_id` of the accompanying public notice. |
| `executor_role` | string | ✓ | Authorized role to execute (typically `admin`). |

<details>
<summary>Illustrative <code>RollbackPlan</code> JSON (continuing the hydrology example)</summary>

```json
{
  "rollback_id": "rb-rel-hydrology-2024-04-23-001",
  "release_id": "rel-hydrology-2024-04-23-001",
  "target_release_id": "rel-hydrology-2024-04-21-baseline",
  "asset_pointer_changes": [
    {"path": "/api/v1/claims/cl-001", "from": "cl-002", "to": "cl-001-baseline"}
  ],
  "cache_invalidation": ["cdn://layers/lay-hydro-iv-001/*"],
  "verification_steps": [
    "fetch cl-001 returns baseline",
    "fetch correction returns withdrawn"
  ],
  "public_notice": "cn-cl-001-2024-04-23-rollback",
  "executor_role": "admin"
}
```

</details>

### `SupersessionRecord`

The lineage artifact that links an old release to its replacement.

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `old_release` | string | ✓ | `release_id` being superseded. |
| `new_release` | string | ✓ | `release_id` of the replacement. |
| `reason` | string | ✓ | Short reason code; matches the originating `CorrectionNotice.reason` when applicable. |
| `effective_time` | timestamp | ✓ | When the public pointer moved. |
| `retained_access_rule` | enum / string | ✓ | How the old release is reachable for audit (`audit_only`, `read_with_banner`, `withdrawn_with_summary`). |

### `ReviewState`

The shared enum for correction-artifact lifecycle. Identical values are used by `CorrectionNotice.review_state` and by `ReviewRecord` for the originating release.

```text
draft → steward_review → approved
                       → rejected
approved      → superseded (when replaced by a newer correction)
approved      → withdrawn (when correction itself is withdrawn)
```

### Public notice

The human-facing artifact derived from a `CorrectionNotice`. Lives at a stable URL under the release authority (`release/corrections/<release_id>/` per the project's two-tier release pattern; **`PROPOSED`** path).

| Field | Required | Notes |
|---|:---:|---|
| Human-readable reason | ✓ | Drawn from `public_summary`. |
| Affected scope | ✓ | Claims, layers, exports, or assets. |
| `corrected_on` / `withdrawn_on` | ✓ | ISO 8601 timestamps. |
| Where to inspect evidence | ✓ | Stable links to the `EvidenceBundle`, `CorrectionNotice`, and `ReleaseManifest`. |

[⬆ Back to top](#corrections-are-first-class)

---

## Correction-and-rollback flow

The diagram below shows how the eight triggering scenarios route through the doctrine. It reflects the PROPOSED implementation of the doctrine; the canonical state machine is the release state machine in [`docs/architecture/release-and-publication.md`](../architecture/release-and-publication.md) (`NEEDS VERIFICATION` — exact path).

```mermaid
flowchart TB
  classDef trigger fill:#FFF6D6,stroke:#999,color:#222;
  classDef artifact fill:#E1ECFB,stroke:#456,color:#222;
  classDef decision fill:#FCE4D6,stroke:#a55,color:#222;
  classDef public fill:#D9EAD3,stroke:#385,color:#222;

  P[Published release]:::public
  P -->|defect / change detected| T{Trigger}
  T --> E[Error in claim]:::trigger
  T --> D[Disputed claim]:::trigger
  T --> S[Source update]:::trigger
  T --> R[Rights change]:::trigger
  T --> SC[Sensitivity change]:::trigger
  T --> ST[Stale evidence]:::trigger
  T --> SU[Superseded artifact]:::trigger
  T --> W[Withdrawal request]:::trigger

  E --> CN[CorrectionNotice]:::artifact
  D --> CN
  S --> CN
  R --> CN
  SC --> CN
  ST --> CN
  SU --> CN
  W --> CN

  CN --> RV[ReviewState: steward_review]:::artifact
  RV --> SEV{severity?}:::decision

  SEV -->|minor / moderate| SR[Superseding release through normal release path]:::artifact
  SEV -->|severe / integrity| RB[RollbackPlan executed]:::artifact
  SEV -->|rights / sensitivity| WD[Withdrawal: assets unreachable, audit retained]:::artifact

  SR --> SREC[SupersessionRecord]:::artifact
  RB --> SREC
  WD --> SREC

  SREC --> PN[Public notice at stable URL]:::public
  PN --> ED[Evidence Drawer + /api/v1/corrections]:::public
```

> [!NOTE]
> The diagram is `NEEDS VERIFICATION` against the implementation: route names, the exact severity → branch mapping, and the Evidence Drawer endpoint are `PROPOSED`. The doctrinal claim — that every trigger ends in a `CorrectionNotice`, a typed downstream artifact, and a public notice — is CONFIRMED.

### Numeric flow (eleven-step transition, correction-relevant steps)

Steps 10 and 11 of the eleven-step publication transition are the doctrinal foothold of this document. They MUST be satisfied at release time, not retrofitted on detection of an error.

1. *(steps 1–9 from `release-and-publication.md` — candidate → validation → policy → review → manifest → proof → published → catalog → API availability)*
2. **Correction path** — the `CorrectionNotice` path is visible. A user can report a correction or see a supersession from the public artifact.
3. **Rollback path** — a `RollbackPlan` and `target_release_id` are ready. **Rollback rehearsal exists before release** — an untested rollback is not a rollback.

> [!IMPORTANT]
> A `ReleaseManifest` without a `correction_path` or `rollback_target` MUST be rejected by the **Publication manifest validator** (`tools/release/validate_manifest.py`; `PROPOSED` path). This is the enforcement edge of invariant **I-4**.

[⬆ Back to top](#corrections-are-first-class)

---

## Public visibility rules

Correction artifacts are public-by-default because invisibility defeats the doctrine. The rules below define the minimum public surface; implementations MAY expose more.

| Surface | What it MUST show | What it MUST NOT show |
|---|---|---|
| **Evidence Drawer** (UI) | Correction state of the artifact; link to `CorrectionNotice`; `corrected_on` / `withdrawn_on`. | Restricted source content, redacted exact locations, raw model output. |
| **Public API** (`GET /api/v1/claims/<id>`) | `DecisionEnvelope` whose `outcome` is `superseded` or `withdrawn` when applicable; forward pointer to replacement. | Stack traces, internal paths, draft `CorrectionNotice` records. |
| **Corrections feed** (`GET /api/v1/corrections`) | List of approved `CorrectionNotice` records, filterable by scope. | Notices in `draft` or `rejected` review state. |
| **Catalog record** | `release_state` reflecting supersession or withdrawal; link to manifest, proof, evidence, and notice. | Direct links to `data/raw/` or `data/work/`. |
| **Release authority** (`release/corrections/<release_id>/`) | The signed, hashed correction artifacts. | (No restrictions — this is the audit surface.) |

Routes and paths above are `PROPOSED`. The CONFIRMED doctrinal claim is that **for every approved correction there exists at least one stable public URL** at which its existence, scope, and reason can be inspected.

> [!TIP]
> When a correction is in `draft` or `steward_review`, the **runtime** SHOULD return `ABSTAIN` with reason `evidence.under_review` for queries that touch the affected claim, rather than serve the pre-correction answer with no caveat. This is consistent with KFM's cite-or-abstain posture under [`trust-posture.md`](./trust-posture.md).

[⬆ Back to top](#corrections-are-first-class)

---

## AI boundary in corrections

This section operationalizes [`ai-as-assistant.md`](./ai-as-assistant.md) inside the corrections workflow. AI participation is bounded; the boundaries below are CONFIRMED doctrine.

| AI may | AI may NOT |
|---|---|
| Draft the `public_summary` text of a `CorrectionNotice` for human review. | Decide that a correction is warranted. |
| Suggest a `reason` code from the controlled enum. | Approve a `CorrectionNotice` (`review_state: approved`). |
| Cluster incoming user-reported issues into candidate notices. | Move a release to `superseded` or `withdrawn`. |
| Generate diff prose for two releases ("what changed between `rel-X` and `rel-Y`"). | Execute a `RollbackPlan`. |
| Surface plausibly stale `DatasetVersion` records for steward attention. | Modify retained audit records under any circumstance. |

> [!CAUTION]
> A correction record that cites only an AI output as its `source_refs` is not a correction. Per [`ai-as-assistant.md`](./ai-as-assistant.md), model output is not a citation; the `Citation validator` MUST reject any `CorrectionNotice` whose `source_refs` do not resolve to a real `EvidenceBundle`.

[⬆ Back to top](#corrections-are-first-class)

---

## Validation and tests

The doctrine is enforced by named validators that run in CI. Validator names and test directories below are `PROPOSED` paths from the project's CI plan; implementations MUST verify them before relying on them.

| Validator | Enforces | Implementation home (PROPOSED) |
|---|---|---|
| **Correction validator** | `CorrectionNotice` shape, supersession, withdrawal, and public notice path. | `tests/corrections/` |
| **Rollback validator** | `RollbackPlan` target hash, route / cache / data reversion, public notice. | `tests/rollback/` |
| **Publication manifest validator** | `ReleaseManifest` declares `correction_path` and `rollback_target`. | `tools/release/validate_manifest.py`; `tests/release/` |
| **Citation validator** | `source_refs` resolve to real `EvidenceBundle` objects. | `tests/runtime/` |
| **Rollback rehearsal** (CI job) | Simulate rollback of the proof slice; verify pointer revert and notice emission. | CI job `rollback-rehearsal` |
| **Release dry-run** (CI job) | Compile `ReleaseManifest` / `ProofPack` without publishing; verify manifest closure. | CI job `release-dry-run` |

### Negative paths

The following negative-path tests MUST exist and pass. Each row maps to a row in the `Negative-path catalogue` in the implementation plan.

| Negative-path test | Expected outcome |
|---|---|
| `ReleaseManifest` missing `correction_path` | `DENY release.unreviewed` — no public publication. |
| `ReleaseManifest` missing `rollback_target` | `DENY release.unreviewed` — no public publication. |
| `CorrectionNotice` with empty `source_refs` | Rejected by Citation validator. |
| `CorrectionNotice` approved without `steward_review` transition | Rejected by Correction validator. |
| Rollback executed without rehearsal artifact | Rejected by Rollback validator. |
| Public surface mutated without a `CorrectionNotice` | `ERROR` — invariant **I-1** violated. |
| Audit record overwritten in place | `ERROR` — invariant **I-2** violated. |

[⬆ Back to top](#corrections-are-first-class)

---

## Day-2 connections

Four PROPOSED runbooks consume this doctrine directly. Their names, owners, and post-incident requirements are from the project's runbook index.

| Runbook | Trigger | Owner | Post-incident requirement |
|---|---|---|---|
| `RB-CORRECTION-ROUTINE` | Steward identifies non-emergency error in published claim. | Steward | Correction notice; superseding release; public-facing summary. |
| `RB-ROLLBACK-EXECUTION` | Rollback authorized by admin and required by correction or integrity issue. | Admin | Rollback plan executed; verification steps recorded; notice published. |
| `RB-PRIVACY-REQUEST` | Privacy / takedown request received from a living person identified in records. | Steward + Legal | Triage; redaction or withdrawal; correction notice; legal-record retention. |
| `RB-INCIDENT-INTEGRITY-FAILURE` | Hash mismatch on any released artifact. | Admin + Steward | Integrity investigation; possible rollback; correction notice if data was served. |

> [!NOTE]
> Drill cadence is `PROPOSED`: at L1, each runbook MUST be drilled at least annually; at L2, quarterly. Drills produce a `DrillRecord` with the same schema as a real incident, marked `drill: true`. **Drills that do not produce a record are not drills.**

[⬆ Back to top](#corrections-are-first-class)

---

## Acceptance checklist

Use this list when reviewing a `ReleaseManifest`, a `CorrectionNotice`, or a `RollbackPlan`. `[PROPOSED at implementation level]` — the checklist itself is doctrine; the path-shaped enforcement is `PROPOSED`.

- [ ] Every `ReleaseManifest` declares both `correction_path` and `rollback_target`.
- [ ] A rollback rehearsal artifact exists for the release before public exposure.
- [ ] Every `CorrectionNotice` has a non-empty `source_refs` that resolves to a real `EvidenceBundle`.
- [ ] Every `CorrectionNotice` traverses `draft → steward_review → approved` before becoming public.
- [ ] Severe-severity corrections trigger a `RollbackPlan` evaluation; if rollback is chosen, the plan is executed by `executor_role: admin`.
- [ ] Sensitivity downgrades traverse the same review gate as the original release.
- [ ] Public notice path is reachable at a stable URL for every approved correction.
- [ ] Superseded releases remain inspectable per `retained_access_rule`.
- [ ] Old audit records are not overwritten — append-only enforced.
- [ ] AI-drafted prose in `public_summary` is reviewed and signed by a human before approval.
- [ ] No public route is mutated without an accompanying `CorrectionNotice` and notice.

[⬆ Back to top](#corrections-are-first-class)

---

## Anti-patterns

The list below names the failure modes this doctrine is designed to prevent. Each one is a `DENY` or `ERROR` outcome, not a stylistic preference.

| Anti-pattern | Why it fails | Correct shape |
|---|---|---|
| "Hot-patch" the published file. | Violates **I-1** (named operation) and **I-2** (append-only). | Issue `CorrectionNotice`; build superseding release. |
| Delete the bad release entirely. | Destroys audit; breaks links from other artifacts. | Withdraw with notice; preserve via `retained_access_rule`. |
| Move pointers without a notice. | Violates **I-3** (public visibility); users see drift, not correction. | Emit public notice at stable URL before / with pointer change. |
| Treat AI output as the source of the correction. | Model output is not a citation. | `source_refs` MUST resolve to a real `EvidenceBundle`. |
| Skip the rollback rehearsal "because it's a small release." | An untested rollback is not a rollback. | Run `rollback-rehearsal` CI job for every release. |
| Re-expose a redacted exact location through a "rollback." | Sensitivity downgrade without review gate. | Treat as new release; require steward + (where applicable) cultural-authority review. |
| Mix release authority with the materialization index. | Conflates `/release` and `/data/releases`; either lets pipelines bypass review or scatters release authority. | Keep two-tier release pattern per [`lifecycle-law.md`](./lifecycle-law.md). |
| Issue a correction without a `public_summary`. | A correction nobody can read isn't a correction. | `public_summary` is REQUIRED on every `CorrectionNotice`. |

[⬆ Back to top](#corrections-are-first-class)

---

## Related docs

- [`docs/doctrine/lifecycle-law.md`](./lifecycle-law.md) — `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED` and the publication state transition this doctrine extends. `[CONFIRMED sibling.]`
- [`docs/doctrine/trust-posture.md`](./trust-posture.md) — Cite-or-abstain rule that governs how corrections-in-progress surface to users. `[NEEDS VERIFICATION — confirm exact filename.]`
- [`docs/doctrine/ai-as-assistant.md`](./ai-as-assistant.md) — Operationalized by the [AI boundary section](#ai-boundary-in-corrections) of this doc. `[CONFIRMED sibling.]`
- [`docs/architecture/release-and-publication.md`](../architecture/release-and-publication.md) — The eleven-step release state machine; canonical source for steps 1–9 that precede the correction-and-rollback steps. `[NEEDS VERIFICATION — exact path.]`
- [`docs/runbooks/RB-CORRECTION-ROUTINE.md`](../runbooks/RB-CORRECTION-ROUTINE.md) — Day-2 routine correction. `[TODO — confirm path.]`
- [`docs/runbooks/RB-ROLLBACK-EXECUTION.md`](../runbooks/RB-ROLLBACK-EXECUTION.md) — Day-2 rollback execution. `[TODO — confirm path.]`
- [`docs/runbooks/RB-PRIVACY-REQUEST.md`](../runbooks/RB-PRIVACY-REQUEST.md) — Day-2 privacy / takedown handling. `[TODO — confirm path.]`
- [`docs/runbooks/RB-INCIDENT-INTEGRITY-FAILURE.md`](../runbooks/RB-INCIDENT-INTEGRITY-FAILURE.md) — Day-2 integrity failure. `[TODO — confirm path.]`
- `schemas/contracts/v1/correction_notice.schema.json` — Machine-readable schema. `[PROPOSED path.]`
- `schemas/contracts/v1/rollback_plan.schema.json` — Machine-readable schema. `[PROPOSED path.]`
- `schemas/contracts/v1/supersession_record.schema.json` — Machine-readable schema. `[PROPOSED path.]`
- ADR — *Two-tier release pattern: `/release` as authority vs `/data/releases` as materialization*. `[TODO — ADR not yet authored.]`

---

<sub>**Last updated:** 2026-05-12 · **Version:** v1 (draft) · **Doctrine track:** `docs/doctrine/`</sub>

[⬆ Back to top](#corrections-are-first-class)
