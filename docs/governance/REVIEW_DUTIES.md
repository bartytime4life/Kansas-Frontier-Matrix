<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/review-duties
title: Review Duties — Reviewer Roles and Separation-of-Duties Matrix
type: standard
version: v1-draft
status: draft
owners: Docs steward; co-reviewed by Release authority
created: 2026-05-12
updated: 2026-05-15
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/authority-ladder.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/adr/ADR-S-09-reviewer-separation-threshold.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - release/manifests/
  - release/correction_notices/
  - release/rollback_cards/
  - schemas/contracts/v1/review/review_record.schema.json
tags: [kfm, governance, review, separation-of-duties, release]
notes:
  - Consolidates Atlas v1.1 Ch. 24.7 (Reviewer Role and Separation-of-Duties Matrix).
  - All role definitions and matrix rows are PROPOSED pending ADR-S-09.
  - Operating-Law Invariant 9 (separation of duties when maturity justifies) is CONFIRMED.
  - This revision tightens repo-evidence boundaries, path-status labels, ReviewRecord closure rules, and maintainer verification steps.
[/KFM_META_BLOCK_V2] -->

# Review Duties — Reviewer Roles and Separation-of-Duties Matrix

> **Who is allowed to author what, who must approve what, and at which lifecycle gate that separation becomes mandatory.** This is the governance face of KFM's release discipline; it is *not* an access-control implementation.

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![authority: doctrine](https://img.shields.io/badge/authority-doctrine-blue)
![invariant: OL--9](https://img.shields.io/badge/invariant-OL--9-purple)
![separation: maturity--dependent](https://img.shields.io/badge/separation-maturity--dependent-orange)
![enforcement: by--custom-(today)](https://img.shields.io/badge/enforcement-by--custom_today-lightgrey)
![repo depth: unknown](https://img.shields.io/badge/repo_depth-unknown-lightgrey)
![ADR: ADR--S--09 open](https://img.shields.io/badge/ADR-ADR--S--09_open-red)

| Field | Value |
|---|---|
| **Doc class** | Governance reference (standard doc) |
| **Target path** | `docs/governance/REVIEW_DUTIES.md` — **PROPOSED / NEEDS VERIFICATION** until mounted-repo placement is confirmed |
| **Authority of these rules** | **CONFIRMED** for Operating-Law Invariant 9; **PROPOSED** for the role catalogue and matrix rows (per Atlas v1.1 Ch. 24.7) |
| **Owner** | Docs steward |
| **Reviewers required for change** | Docs steward + Release authority; **ADR required** to amend the matrix in a way that loosens separation for any sensitive-lane row |
| **Supersedes** | None — first consolidated review-duty doc in the `docs/governance/` responsibility area; live repo status remains **UNKNOWN** without inspection |
| **Status** | `draft` |
| **Last updated** | `2026-05-15` |

> [!IMPORTANT]
> This document **describes** the duty model. It does not, by itself, enforce anything.
> Today, known enforcement is by custom (PR review, named approvers, manual receipts);
> tooling enforcement (`CODEOWNERS`, branch protection, OPA two-key gate) is the
> **PROPOSED** target state and is gated on **ADR-S-09 — Reviewer separation-of-duties threshold**.

> [!NOTE]
> **Evidence boundary:** this revision is grounded in the attached Markdown baseline,
> KFM Markdown Updater instructions, and Directory Rules doctrine. A mounted KFM repo,
> live `CODEOWNERS`, branch-protection settings, policy bundles, emitted `ReviewRecord`s,
> and release artifacts were **not** inspected here. Treat implementation claims as
> **UNKNOWN** unless marked otherwise.

---

## Contents

1. [Purpose & scope](#1-purpose--scope)
2. [Doctrinal basis](#2-doctrinal-basis)
3. [Reviewer roles](#3-reviewer-roles)
4. [Separation-of-Duties matrix](#4-separation-of-duties-matrix)
5. [Review flow at a glance](#5-review-flow-at-a-glance)
6. [The `ReviewRecord` contract](#6-the-reviewrecord-contract)
7. [Sensitivity-tier transitions (cross-reference)](#7-sensitivity-tier-transitions-cross-reference)
8. [Maturity model & the tooling threshold (ADR-S-09)](#8-maturity-model--the-tooling-threshold-adr-s-09)
9. [How to invoke a review](#9-how-to-invoke-a-review)
10. [Drift patterns & anti-patterns](#10-drift-patterns--anti-patterns)
11. [Related docs](#11-related-docs)
12. [Open questions & NEEDS VERIFICATION](#12-open-questions--needs-verification)
13. [Maintainer verification & rollback](#13-maintainer-verification--rollback)

---

## 1. Purpose & scope

`docs/governance/REVIEW_DUTIES.md` is the **PROPOSED target home** for the single human-facing reference for who reviews what across the KFM lifecycle. It answers four questions that the rest of the doctrine assumes have an answer somewhere:

- **Which roles exist** as reviewers in the KFM system, and what each one *owns*.
- **Which actions** require a reviewer who is *not* the author.
- **Under which conditions** that separation becomes mandatory rather than advisory.
- **Which artifact** (`ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `RollbackCard`) records the decision so it remains auditable later.

**In scope.** Role catalogue · separation matrix · review-flow narrative · `ReviewRecord` shape · sensitivity-tier transition reviewers · maturity-vs-tooling threshold · drift patterns · maintainer verification checklist.

**Out of scope.** This doc intentionally does **not** define or implement:

- Object-family meaning → `contracts/`.
- Field-level shape of receipts → `schemas/contracts/v1/`.
- Policy rules that *evaluate* a decision → `policy/`.
- Code-level identity, auth, RBAC plumbing → `apps/governed-api/` + `infra/`.
- GitHub-team membership, branch settings, or runtime enforcement → **UNKNOWN** until repo evidence exists.

> [!NOTE]
> This doc is **doctrine + reference**. It does not assume a mounted repo, and it does not
> claim any of these roles are implemented as named GitHub teams, `CODEOWNERS` entries, or
> OPA-enforced gates yet. Those mappings live in the repo when they exist, and are
> tracked in `docs/registers/DRIFT_REGISTER.md` until they do.

[⬆ back to top](#contents)

---

## 2. Doctrinal basis

KFM's separation-of-duties model is grounded in layered sources. Directory Rules remain the placement authority, but Directory Rules also distinguish doctrine from verified live repo state: a quoted path is not automatically proof that the path exists in the mounted repository.

| Layer | Source | What it gives this doc | Status |
|---|---|---|---|
| Operating Law | KFM Operating Law, Invariant 9 — *"separate policy-significant release duties when maturity justifies it"* | The non-negotiable principle | **CONFIRMED** doctrine |
| Doctrine consolidation | Atlas v1.1 **Ch. 24.7** — *Master Reviewer Role and Separation-of-Duties Matrix* | The eight-role catalogue + the action-by-action matrix | Section is **CONFIRMED**; individual rows labelled **PROPOSED** by Atlas v1.1 |
| Placement & change discipline | `docs/doctrine/directory-rules.md` §6.1 and §2.4 | `docs/governance/` is the responsibility area for roles, review burden, and separation of duties; material placement/schema/parallel-home changes are ADR-class | **CONFIRMED** doctrine; specific path presence **NEEDS VERIFICATION** |
| Schema-home convention | ADR-0001 / Directory Rules schema-home convention | Default machine-schema home is `schemas/contracts/v1/<…>` | **CONFIRMED** doctrine; `review_record.schema.json` live presence **NEEDS VERIFICATION** |

> [!NOTE]
> The roles and matrix below were **named-only** in Atlas v1.1: the supplement explicitly
> says these are *"PROPOSED reference for ADR discussion"* — primarily **ADR-S-09**. This
> document carries that PROPOSED status forward. Promoting any row from PROPOSED
> to CONFIRMED happens via ADR, not via README edit.

[⬆ back to top](#contents)

---

## 3. Reviewer roles

The eight roles below are KFM's named reviewer surface. They are **role labels**, not job titles — one person may hold several roles, and tooling enforcement (when it lands) will key on the role, not on the person.

> [!NOTE]
> Role scope is **PROPOSED** (Atlas v1.1 Ch. 24.7.1). Treat the "Scope" column as the
> reviewable boundary, not as a binding charter, until ADR-S-09 closes.

| Role | Owns (PROPOSED) | Acts on (PROPOSED) | Primary receipts produced |
|---|---|---|---|
| **Source steward** | Admission, rights confirmation, and sensitivity tag for a named source family. | `SourceDescriptor` lifecycle; admission gate (— → RAW). | `SourceDescriptor`, `PolicyDecision`. |
| **Domain steward** | Meaning, contracts, and validators of a domain's object families. | Domain contracts and schemas; validator authorship; domain-internal promotions. | `ValidationReport`, `TransformReceipt`. |
| **Sensitivity reviewer** | Redaction, generalization, withholding, and tier decisions for sensitive content. | `RedactionReceipt`; tier transitions for sensitive lanes (Archaeology, Fauna, Flora, People/DNA, sensitive Settlements). | `RedactionReceipt`, `ReviewRecord`. |
| **Rights-holder representative** | Sovereignty, cultural-heritage, or consent-based release decisions. | Archaeology, sovereign data, living-person data, DNA data. | `ReviewRecord` (with `role: rights-holder-rep`). |
| **Release authority** | Issues `ReleaseManifest`s and authorizes PUBLISHED transitions; **distinct from authorship** when materiality applies. | PUBLISHED transitions; rollback authorization. | `ReleaseManifest`, `RollbackCard`. |
| **Correction reviewer** | Reviews `CorrectionNotice` / `RollbackCard` before they amend a PUBLISHED claim. | Post-publication corrections and rollbacks. | `CorrectionNotice` (countersigned), `RollbackCard`. |
| **AI surface steward** | Reviews Focus Mode templates, `AIReceipt`s, and policy bindings; audits AI behaviour against cite-or-abstain doctrine. | Focus Mode; `AIReceipt` sampling; cite-or-abstain audits. | `AIReceipt` audit notes; `ReviewRecord`. |
| **Docs steward** | Governance documentation, ADR index, drift register, and Atlas / supplement integrity. | `docs/` tree; ADR index; `docs/registers/DRIFT_REGISTER.md`. | `ReviewRecord` for doctrine artifacts; supersession entries. |

> [!TIP]
> A useful mental model: **stewards admit and shape; reviewers gate; authorities release.**
> The same person *may* play several roles, but the **receipts they produce must show
> which role they were acting in**, because that field drives both audit and future
> tooling enforcement.

### 3.1 Role combination vs approval independence

KFM permits role combination while the team is small, but role combination is not the same thing as approval independence.

| Situation | Allowed? | Required posture |
|---|---|---|
| Same person holds multiple role labels in staffing roster | Yes, especially early. | Record the active `role` in every receipt. |
| Same person authors routine non-sensitive validator and runs it | Yes, per §4 row 3. | Emit `ValidationReport`; periodic docs-steward audit remains allowed. |
| Same person authors and approves a §4 row 5, 6, 8, or 9 action | **No.** | Require a distinct approving actor and a `ReviewRecord`. |
| Same team label appears in author and reviewer fields | **NEEDS VERIFICATION.** | Tooling should resolve whether named people are distinct; fail closed where materiality applies. |
| Rights or sensitivity status is unclear | No public approval until resolved. | `HOLD`, `DENY`, redaction, generalization, or quarantine. |

[⬆ back to top](#contents)

---

## 4. Separation-of-Duties matrix

This is the operational core of the document. Each row is a governed action; the second column says whether the author may also approve it; the third column names the separation that must be present when the answer is "No"; the fourth column names the receipt that records the decision.

> [!IMPORTANT]
> Every row below is **PROPOSED** per Atlas v1.1 Ch. 24.7.2. The matrix is **stable
> enough to design against** but is not frozen until ADR-S-09 lands. Loosening any
> sensitive-lane row from "No" to "Yes" is **ADR-class** per Directory Rules §2.4.

### 4.1 How to read the matrix

- **"Yes" never means "no receipt."** It means same-actor approval is not barred for that row under routine, non-sensitive conditions.
- **"No" means the approving actor must be distinct from the author/detector/template author/release proposer.** The `ReviewRecord` should make that distinction inspectable.
- **Rights, sovereignty, cultural sensitivity, living-person data, DNA, rare-species locations, archaeology, critical infrastructure, or exact sensitive location exposure fail closed** when unclear.
- **Rows 5, 6, 8, and 9 do not become routine with maturity.** They become more enforceable with maturity.

| # | Action | May the author also approve? | Required separation (PROPOSED) | Decision recorded in |
|---|---|---|---|---|
| 1 | **Source admission** (— → RAW) | Yes for routine; **No** when source has unresolved rights, sovereignty, cultural-permission, or sensitivity posture. | Source steward + rights-holder rep where applicable. | `SourceDescriptor` + `ReviewRecord` (when separation triggers). |
| 2 | **Normalization receipts** (RAW → WORK/QUARANTINE) | Yes for routine; **No** when transforms are sensitivity-relevant. | Domain steward; sensitivity reviewer if sensitivity-relevant. | `TransformReceipt` + `RedactionReceipt` (if applies). |
| 3 | **Validator authorship & run** | Yes — validators are deterministic. | Domain steward; periodic audit by docs steward. | `ValidationReport`. |
| 4 | **Promotion to PROCESSED / CATALOG** | Yes for non-sensitive routine; **No** for sensitive lanes. | Domain steward + sensitivity reviewer (sensitive lanes). | `ValidationReport` + `ReviewRecord` (sensitive lanes). |
| 5 | **Release to PUBLISHED** | **No** when materiality applies. | Author ≠ Release authority; rights-holder rep where applicable. | `ReleaseManifest` + `ReviewRecord`. |
| 6 | **Sensitive-lane release** | **No** — always separate. | Author must not be sole approver; sensitivity reviewer + Release authority + rights-holder rep where applicable. | `ReleaseManifest` + `ReviewRecord` + `RedactionReceipt`. |
| 7 | **Correction / rollback** | **No** when correction is steward-significant. | Author / detector + correction reviewer + Release authority. | `CorrectionNotice` and/or `RollbackCard` + `ReviewRecord`. |
| 8 | **AI surface change** (template / policy binding) | **No**. | AI surface steward + docs steward (policy binding); model output is never approver. | `ReviewRecord`; downstream `AIReceipt` sampling. |
| 9 | **Atlas / supplement publication** | **No**. | Docs steward + at least one relevant subsystem owner; ADR required when the change loosens duties or alters placement/schema authority. | `ReviewRecord`; supersession entry in `docs/archive/lineage/`. |

> [!WARNING]
> Rows 5, 6, 8, and 9 are **never** routine: there is no maturity level at which the
> author of a PUBLISHED release, a sensitive-lane release, an AI policy binding, or a
> doctrine publication is allowed to also approve it. The other rows soften with
> maturity; these four do not. See §8.

[⬆ back to top](#contents)

---

## 5. Review flow at a glance

The lifecycle gates already require certain receipts (Atlas v1.1 Ch. 24.6). This diagram overlays the **reviewer who must be present** at each gate when the conditions in §4 trigger.

```mermaid
flowchart LR
    A[Source candidate]:::ext --> ADM{Admission gate}
    ADM -->|SourceDescriptor| RAW[(RAW)]
    ADM -. rights / sovereignty unresolved .-> RHR((Rights-holder rep))
    RHR --> ADM

    RAW --> NORM{Normalization gate}
    NORM -->|TransformReceipt + ValidationReport| WORK[(WORK)]
    NORM -. sensitivity-relevant .-> SR((Sensitivity reviewer))
    SR --> NORM

    WORK --> VAL{Validation gate}
    VAL -->|ValidationReport| PROC[(PROCESSED)]

    PROC --> CAT{Catalog gate}
    CAT -->|EvidenceBundle + CatalogMatrix| TRI[(CATALOG / TRIPLET)]
    CAT -. sensitive lane .-> SR

    TRI --> REL{Release gate}
    REL -->|ReleaseManifest + ReviewRecord| PUB[(PUBLISHED)]
    REL -. materiality .-> RA((Release authority))
    REL -. sensitive lane .-> SR
    REL -. rights .-> RHR
    RA --> REL

    PUB --> CORR{Correction gate}
    CORR -. steward-significant .-> CR((Correction reviewer))
    CR --> CORR
    CORR -->|CorrectionNotice| PUBp[(PUBLISHED')]
    CORR -->|RollbackCard| PRIOR[(prior release)]

    classDef ext fill:#eef,stroke:#88a,color:#224
    classDef phase fill:#fff,stroke:#666,color:#222
    class RAW,WORK,PROC,TRI,PUB,PUBp,PRIOR phase
```

> [!NOTE]
> The diagram reflects **PROPOSED** reviewer placement per Atlas v1.1 Ch. 24.7. If a
> mounted repo turns out to wire reviewers differently (e.g. via `CODEOWNERS`), file the
> conflict in `docs/registers/DRIFT_REGISTER.md` rather than silently amending the
> diagram.

[⬆ back to top](#contents)

---

## 6. The `ReviewRecord` contract

`ReviewRecord` is the receipt that records a steward, rights-holder, or policy review of a candidate transition. It is the artifact that makes every "No" cell in §4 auditable later. The shape below mirrors Atlas v1.1 Ch. 24.2 (Receipt Catalog), with closure fields made explicit for future validators.

> [!IMPORTANT]
> **Schema home:** the canonical JSON Schema is **PROPOSED** at
> `schemas/contracts/v1/review/review_record.schema.json` per ADR-0001 (schema home).
> Treat the path as `PROPOSED / NEEDS VERIFICATION` until a mounted-repo inspection
> confirms it.

| Field | Shape (PROPOSED) | Notes |
|---|---|---|
| `review_record_id` | deterministic id or stable receipt id | Enables supersession, lookup, and rollback linkage. |
| `subject_ref` | id of the object under review | Source id, claim id, layer id, release id, template id, policy binding id, etc. |
| `action` | enum / controlled string | Should map to one §4 row. |
| `target_transition` | controlled string | Example: `CATALOG → PUBLISHED`, `T2 → T1`, `template:v3 → template:v4`. |
| `author_ref` | identity of author / proposer / detector | Must be distinct from `reviewer` for §4 rows 5, 6, 8, and 9. |
| `reviewer` | identity (string id; may be a team or named person) | The actor; **never** the author when separation is mandatory. |
| `role` | enum: one of the eight roles in §3 | Drives audit and future tooling enforcement. |
| `decision` | enum: `ALLOW` \| `RESTRICT` \| `DENY` \| `HOLD` | `HOLD` is a real outcome; it keeps the transition closed without burning the candidate. |
| `reason_codes[]` | array of controlled strings | Examples: `RIGHTS_UNCLEAR`, `REDACTION_REQUIRED`, `REVIEW_INSUFFICIENT`, `RELEASE_OK`. |
| `evidence_refs[]` | array of `EvidenceRef` | Must resolve to an `EvidenceBundle` for non-trivial decisions. |
| `policy_ref` | id of the `policy/` rule(s) consulted | Pairs with a `PolicyDecision`. |
| `receipt_refs[]` | array of related receipts | `RedactionReceipt`, `ValidationReport`, `ReleaseManifest`, `CorrectionNotice`, etc. |
| `created_at` / `time` | RFC 3339 timestamp | Used by the freshness / staleness layer. Prefer one canonical field once schema lands. |
| `supersedes_review_record_id` | nullable id | Corrections supersede; they do not silently edit. |
| `notes` | free text (bounded) | Steward narrative; non-authoritative. |

### 6.1 Closure rules

A `ReviewRecord` is not closed merely because a reviewer has typed a decision. It is closed when:

1. required `evidence_refs[]` resolve to `EvidenceBundle` where evidence is material;
2. required policy references are named;
3. reviewer role matches the §4 row being approved;
4. author/reviewer identity separation is satisfied where required;
5. related receipts are present for the target transition; and
6. the record is immutable except through supersession.

A gate that cannot verify these checks should fail closed as `REVIEW_NEEDED`, `REVIEW_INSUFFICIENT`, or `REVIEW_REJECTED`.

<details>
<summary><b>Illustrative <code>ReviewRecord</code> for a sensitive-lane release (PROPOSED shape, not from a mounted repo)</b></summary>

```json
{
  "review_record_id": "rr:review:fauna:rare-occurrence:2026-05-12-001",
  "subject_ref": "claim:fauna:occurrence:abc-123",
  "action": "sensitive-lane-release",
  "target_transition": "T2 → T1",
  "author_ref": "team:fauna-domain-stewards",
  "reviewer": "team:sensitivity-reviewers",
  "role": "sensitivity-reviewer",
  "decision": "RESTRICT",
  "reason_codes": ["REDACTION_REQUIRED", "PUBLIC_EXACT_GEOMETRY_DENIED"],
  "evidence_refs": ["evidence:fauna:occurrence:abc-123:bundle:v3"],
  "policy_ref": "policy/sensitivity/fauna.rego#sensitive_occurrence",
  "receipt_refs": ["redaction:point_10km_hex_seeded_v1"],
  "subject_target_tier": "T1",
  "transforms_required": ["redaction:point_10km_hex_seeded_v1"],
  "created_at": "2026-05-12T14:33:00Z",
  "notes": "Geometry generalized to 10 km hex; release at T1 conditional on RedactionReceipt presence."
}
```

This example is illustrative; the field set is derived from Atlas v1.1 Ch. 24.2 plus closure fields that make future validation easier. The exact JSON Schema is not verified in this session.
</details>

[⬆ back to top](#contents)

---

## 7. Sensitivity-tier transitions (cross-reference)

Reviewer presence is tier-aware. Atlas v1.1 Ch. 24.5.3 defines who must be present for each **tier transition** (T0 = open, T4 = denied). This table reflects that schedule.

> [!NOTE]
> The **T0–T4** scheme is itself **PROPOSED** pending **ADR-S-05**. The reviewer
> requirements below are the *consequences* of that scheme as it stands in v1.1.

| From → To | Required receipt(s) | Required reviewer(s) | Reversibility |
|---|---|---|---|
| T4 → T3 | `PolicyDecision` + `ReviewRecord` + named agreement | Steward + **rights-holder rep** (where applicable) | Reversible via agreement revocation + `CorrectionNotice`. |
| T4 → T2 | `PolicyDecision` + `ReviewRecord` | Steward | Reversible via review revocation. |
| T4 → T1 | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible; correction may demote a published T1 back to T4. |
| T3 → T2 | `PolicyDecision` + `ReviewRecord` | Steward | Reversible. |
| T2 → T1 | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible. |
| T1 → T0 | `ReleaseManifest` + `ReviewRecord` | **Steward + Release authority** | Reversible via `RollbackCard`. |
| Any → T4 (downgrade) | `CorrectionNotice` + `ReviewRecord` | Steward + rights-holder where applicable | Always permitted; precedes derivative invalidation. |

> [!TIP]
> **Reading shortcut.** *Up* (toward more public exposure) always needs a
> `ReviewRecord` plus either a policy decision, a transform/redaction receipt, a named
> agreement, or a release manifest. *Down* (toward less public exposure) is always
> permitted through the correction path and should invalidate unsafe derivatives.

[⬆ back to top](#contents)

---

## 8. Maturity model & the tooling threshold (ADR-S-09)

KFM Operating Law treats separation of duties as **maturity-dependent**, not as a fixed gate. The text in Atlas v1.1 Ch. 24.7.2 is direct:

> *"Early-stage doctrine work may be authored and approved by the same actor when materiality is low. As maturity rises and the public trust surface expands, separation must be enforced through tooling, not custom; the supplement does not pretend the enforcement exists yet."*

That sentence is the posture of this document. The matrix in §4 is the **target**; current known enforcement in this document is by **custom** (PR review, named approvers, manual `ReviewRecord` authoring). Mounted-repo enforcement remains **UNKNOWN** until inspected.

### 8.1 Maturity bands (PROPOSED)

| Maturity band | Public trust surface | Posture for §4 rows 1–4 | Posture for §4 rows 5–9 | Enforcement |
|---|---|---|---|---|
| **Doctrine-only** | None (no public release surface live) | Same-actor permitted with documented exceptions for sensitive lanes. | Same-actor **not** permitted, but enforced by review custom. | Custom (PR, manual). |
| **Internal-release** | Stewards + named collaborators only | Same-actor permitted only for non-sensitive routine. | Two-actor required and named in `ReviewRecord`. | Custom + `CODEOWNERS` where verified. |
| **Public-release** | Public governed-API surface live | Same-actor permitted only when row 4 reads "Yes for non-sensitive routine"; otherwise blocked. | Two-actor **mandatory**, enforced by branch protection + OPA gate G (two-key). | Tooling. |
| **High-exposure** (3D, AI surface, archaeology, DNA) | Sensitive content visible | Two-actor mandatory across the board. | Two-actor + rights-holder rep + Release authority, blocked at gate. | Tooling, fail-closed. |

> [!IMPORTANT]
> **ADR-S-09 — Reviewer separation-of-duties threshold** is the open ADR that fixes the
> transitions between these bands. Until it lands, the table above is a **PROPOSED**
> reading. The bands themselves, the matrix, and the role catalogue all derive from
> Atlas v1.1 Ch. 24.7 and are intentionally compatible with the **C5-01 Gate Matrix A–G**
> framing, where Gate **G** = "Reviewability with two-key approval."

### 8.2 What "enforced by tooling" looks like (target, not current)

These are the artefacts that, **once present and wired**, move a duty from "custom" to "tooling-enforced." All entries are **PROPOSED / NEEDS VERIFICATION** until a mounted repo confirms them.

- `CODEOWNERS` entries that bind each `policy/`, `release/`, `data/published/`, and `schemas/contracts/v1/review/` path to the correct role.
- Branch protection that requires **two distinct reviewers** for paths covered by §4 rows 5–9.
- OPA / Conftest fixtures under `policy/promotion/` that **deny** a release when `ReleaseManifest.author == ReviewRecord.reviewer` for sensitive-lane content.
- `tools/validators/review/` that re-runs the `ReviewRecord` schema check and the role-vs-action consistency check in CI.
- A starter verification pack (for example: `CODEOWNERS`, `tool-versions.yaml`, `policy-bundle.json`, `sbom.yaml`, `run_receipt.schema.json`, `integrity.yml`, `verify.sh`) present, versioned, and wired into CI.

[⬆ back to top](#contents)

---

## 9. How to invoke a review

This section is procedural. It assumes the actor has read §3–§4 and knows which row applies.

1. **Identify the row.** Locate the action in the §4 matrix.
2. **If "Yes" applies and the lane is not sensitive** — proceed; emit the routine receipt (`TransformReceipt`, `ValidationReport`, etc.) and note the actor in the receipt.
3. **If "No" applies** — stop. Open a review request that identifies:
   - the **subject** (source id, claim id, layer id, release id, template id, policy binding id),
   - the **target transition** (e.g. `T2 → T1`, `CATALOG → PUBLISHED`, or `template:v3 → template:v4`),
   - the **§4 row** that triggered review,
   - the **role** of the reviewer being requested,
   - the **author/proposer identity** that must be separated from the reviewer,
   - the **evidence refs** and receipt refs that the reviewer needs.
4. **The reviewer** authors a `ReviewRecord` per §6 with `decision ∈ {ALLOW, RESTRICT, DENY, HOLD}`.
5. **Closure.** The transition's required receipts (per Atlas v1.1 Ch. 24.6) must include the `ReviewRecord` *before* the gate evaluates. A missing or insufficient `ReviewRecord` fails the gate closed with reason code `REVIEW_NEEDED`, `REVIEW_INSUFFICIENT`, or `REVIEW_REJECTED`.
6. **If the decision is `HOLD`, `DENY`, or `RESTRICT`,** the candidate remains closed to public release until required evidence, redaction, rights, or correction work is complete.
7. **Audit.** Every `ReviewRecord` is preserved; corrections supersede, they do not overwrite.

> [!CAUTION]
> Do **not** retroactively edit a `ReviewRecord` after the gate has closed. If the
> decision was wrong, the correction path is a **new** `ReviewRecord` + a
> `CorrectionNotice` (and, if the release has shipped, a `RollbackCard`). Silent edits
> are an Operating-Law violation.

[⬆ back to top](#contents)

---

## 10. Drift patterns & anti-patterns

These are the failure modes the matrix exists to prevent. They are drawn from Atlas v1.1 Ch. 24.9 (Failure-Mode and Anti-Pattern Register) and Directory Rules drift discipline — not invented here.

| Drift / anti-pattern | Why it's dangerous | Where it most often shows up |
|---|---|---|
| **Author = Release authority** for a material release | Collapses the trust membrane; turns publication into self-attestation. | §4 row 5, sensitive lanes (§4 row 6). |
| **Same actor admits and releases a sensitive source** | Hides the rights / sovereignty checkpoint. | §4 row 1 + row 6. |
| **Silent `ReviewRecord` edit after closure** | Erases the audit trail Operating Law depends on. | §6, §9. |
| **`AIReceipt` without an AI surface steward audit** | Cite-or-abstain becomes "say it fluently and call it cited." | §4 row 8. |
| **Tier upgrade without `RedactionReceipt` or a policy-backed alternative** | Sensitive content reaches public surface without transform support. | §7 (T4→T1 / T2→T1). |
| **`CODEOWNERS`-as-implementation, `ReviewRecord`-not-emitted** | Looks enforced; isn't auditable. The receipt is the truth, not the GitHub approval. | §8.2. |
| **"It's still doctrine-only, so the rule doesn't apply yet"** for §4 rows 5, 6, 8, 9 | Those rows do not soften with maturity. See §8. | §8.1. |
| **Matrix loosened by README edit instead of ADR** | Bypasses Directory Rules and makes policy-significant release duties mutable by prose patch. | §2, §4. |
| **Role label without identity resolution** | A team label can hide same-person author/reviewer overlap. | §3.1, §6. |
| **Release-side path treated as live because it appears in a doc** | Confuses doctrine placement with mounted-repo evidence. | §11, §12. |

[⬆ back to top](#contents)

---

## 11. Related docs

- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — governs placement; §6.1 places governance docs under `docs/`; §2.4 governs ADR-class changes.
- [`docs/doctrine/authority-ladder.md`](../doctrine/authority-ladder.md) — what outranks what when sources conflict.
- [`docs/doctrine/trust-membrane.md`](../doctrine/trust-membrane.md) — the boundary the matrix protects.
- [`docs/doctrine/lifecycle-law.md`](../doctrine/lifecycle-law.md) — RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED.
- [`docs/architecture/governed-api.md`](../architecture/governed-api.md) — the operational form of the trust membrane; live path **NEEDS VERIFICATION**.
- [`docs/adr/README.md`](../adr/README.md) — ADR index. **ADR-S-09** (reviewer separation threshold) is the open ADR that closes the maturity-band table in §8.
- [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) — file any conflict between this matrix and observed repo behaviour here.
- [`docs/registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) — track open repo, policy, schema, owner, and enforcement checks.
- `release/manifests/`, `release/correction_notices/`, `release/rollback_cards/` — **PROPOSED / NEEDS VERIFICATION** release-side homes for artifacts referenced in §4.
- `schemas/contracts/v1/review/review_record.schema.json` — **PROPOSED / NEEDS VERIFICATION** canonical schema home.

[⬆ back to top](#contents)

---

## 12. Open questions & NEEDS VERIFICATION

These items are intentionally **not** resolved in this document. Track them in `docs/registers/VERIFICATION_BACKLOG.md` and resolve via ADR, per-root README, or mounted-repo evidence.

- **NEEDS VERIFICATION:** Whether `docs/governance/REVIEW_DUTIES.md` is present in the live repo and linked from adjacent docs.
- **NEEDS VERIFICATION:** Whether `schemas/contracts/v1/review/review_record.schema.json` is the live schema home, or whether a `<domain>/review/` layout exists.
- **NEEDS VERIFICATION:** Whether a `policy/review/` or `policy/promotion/` Rego bundle exists today and what its deny rules look like.
- **NEEDS VERIFICATION:** Whether `CODEOWNERS` is present at repo root or under `.github/`, and which paths it covers.
- **NEEDS VERIFICATION:** Whether branch protection can require two distinct human reviewers for rows 5, 6, 8, and 9.
- **NEEDS VERIFICATION:** Whether any `ReviewRecord` instances have been emitted to date and where they live (`data/receipts/review/`? `release/review/`? elsewhere?).
- **NEEDS VERIFICATION:** Whether release-side homes (`release/manifests/`, `release/correction_notices/`, `release/rollback_cards/`) exist and match Directory Rules.
- **OPEN (ADR-S-09):** Concrete thresholds that move a duty from "custom" to "tooling-enforced." Maturity bands in §8.1 are PROPOSED placeholders.
- **OPEN (ADR-S-05):** Adoption of the T0–T4 tier scheme as canonical (affects §7).
- **OPEN:** Whether AI surface review (§4 row 8) requires its own dedicated receipt class or whether `AIReceipt` + `ReviewRecord` is sufficient.
- **UNKNOWN:** Whether the team currently in place can staff all eight roles in §3, or whether some are formally combined. This is a staffing question, not a doctrine question.

[⬆ back to top](#contents)

---

## 13. Maintainer verification & rollback

Use this section as the pre-commit checklist for this doc and for any PR that tries to operationalize it.

### 13.1 Verification checklist

- [ ] Confirm `docs/governance/REVIEW_DUTIES.md` is the intended live path under Directory Rules.
- [ ] Confirm this doc is linked from `docs/README.md`, `docs/doctrine/README.md`, `docs/adr/README.md`, and the Drift Register if those files exist.
- [ ] Confirm ADR-S-09 exists or add a `PROPOSED` ADR stub that owns the tooling threshold.
- [ ] Confirm ADR-S-05 status before relying on T0–T4 terminology in automation.
- [ ] Confirm the live schema home for `review_record.schema.json` before creating or updating machine-readable shape.
- [ ] Confirm policy bundle names before adding Rego references to this doc.
- [ ] Confirm `CODEOWNERS` / branch-protection / OPA checks before changing the enforcement badge from `by-custom-(today)`.
- [ ] Confirm release/correction/rollback artifact homes before marking those paths CONFIRMED.
- [ ] Add or update `docs/registers/DRIFT_REGISTER.md` if observed repo placement conflicts with this doc.
- [ ] Add or update `docs/registers/VERIFICATION_BACKLOG.md` for unresolved checks.

### 13.2 Rollback path

Rollback is required if a change to this document weakens separation for sensitive lanes, removes author/reviewer distinction for §4 rows 5–9, creates a parallel schema/policy/release home without ADR, or claims enforcement that is not supported by repo evidence.

Rollback target: restore the last reviewed `v1-draft` text, preserve this revision as superseded lineage, and file a `CorrectionNotice` if any downstream policy, release, or automation change relied on the incorrect text.

[⬆ back to top](#contents)

---

<details>
<summary><b>Appendix A — Glossary (placement-relevant terms)</b></summary>

| Term | Short definition |
|---|---|
| **Operating Law / Invariant 9** | The KFM rule that policy-significant release duties are separated when maturity justifies. CONFIRMED. |
| **Role** | A reviewer surface defined in §3. May be held by a team or a named person. |
| **Materiality** | The condition under which a release affects the public trust surface (public release, sensitive lane, AI surface, doctrine publication). Triggers the "No" cells in §4. |
| **Trust membrane** | The boundary that prevents RAW / WORK / QUARANTINE / canonical / internal state from becoming public truth. Operational form: `apps/governed-api/`; live path **NEEDS VERIFICATION**. |
| **`ReviewRecord`** | The receipt that records a review decision. See §6. |
| **`ReleaseManifest`** | The release decision artifact; proposed home `release/manifests/` until repo inspection confirms it. |
| **`CorrectionNotice` / `RollbackCard`** | Post-publication correction artifacts; proposed homes `release/correction_notices/` and `release/rollback_cards/` until repo inspection confirms them. |
| **Gate G (two-key approval)** | C5-01 framing for the gate enforced when §4 rows 5–9 reach tooling-enforced maturity (§8). |
| **ADR-S-09** | The open ADR that fixes the separation-of-duties threshold. |

</details>

<details>
<summary><b>Appendix B — Quick mapping: action → role → receipt</b></summary>

| Action | Primary role | Adds when sensitive | Primary receipt | Decision receipt |
|---|---|---|---|---|
| Source admission | Source steward | + Rights-holder rep | `SourceDescriptor` | `ReviewRecord` (when triggered) |
| Normalization | Domain steward | + Sensitivity reviewer | `TransformReceipt` | — / `RedactionReceipt` |
| Validation | Domain steward | (audit by docs steward) | `ValidationReport` | — |
| Catalog closure | Domain steward | + Sensitivity reviewer | `CatalogMatrix` entry + `EvidenceBundle` | `ReviewRecord` (sensitive) |
| Release | Release authority (≠ author) | + Sensitivity reviewer + Rights-holder rep | `ReleaseManifest` | `ReviewRecord` |
| Correction | Correction reviewer + Release authority | + Rights-holder rep | `CorrectionNotice` | `ReviewRecord` |
| Rollback | Release authority | — | `RollbackCard` | `ReviewRecord` |
| AI surface change | AI surface steward + Docs steward | — | `ReviewRecord` | downstream `AIReceipt` sampling |
| Atlas publication | Docs steward + subsystem owner | — | supersession entry | `ReviewRecord` |

</details>

---

**Related docs:** [Directory Rules](../doctrine/directory-rules.md) · [Authority Ladder](../doctrine/authority-ladder.md) · [Trust Membrane](../doctrine/trust-membrane.md) · [Lifecycle Law](../doctrine/lifecycle-law.md) · [ADR Index](../adr/README.md) · [Drift Register](../registers/DRIFT_REGISTER.md) · [Verification Backlog](../registers/VERIFICATION_BACKLOG.md)

**Last updated:** 2026-05-15 · **Version:** v1-draft · [⬆ Back to top](#review-duties--reviewer-roles-and-separation-of-duties-matrix)
