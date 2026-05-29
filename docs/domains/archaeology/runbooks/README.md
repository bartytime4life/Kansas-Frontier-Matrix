<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-runbooks-archaeology-readme
title: Archaeology Runbooks — README
type: standard
version: v1.1
status: draft
owners: <TODO: archaeology-steward; docs-steward; sovereignty-review-liaison; release-steward>
created: 2026-05-27
updated: 2026-05-29
policy_label: public
related:
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ARCHITECTURE.md
  - docs/domains/archaeology/VERIFICATION_BACKLOG.md
  - docs/runbooks/README.md
  - docs/runbooks/archaeology/rollback-drill.md
  - docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/adr/README.md
  - policy/sensitivity/archaeology/
tags: [kfm, archaeology, runbooks, operations, governance, sensitive-domain]
notes:
  - CONTRACT_VERSION = "3.0.0" (pinned per ai-build-operating-contract.md §37 versioning + CONTRACT_VERSION pinning convention).
  - PLACEMENT RECONCILED in v1.1 — this README documents the canonical docs/runbooks/archaeology/ folder (Directory Rules §6.1.b Pattern A; OPEN-DR-02 recommends Pattern A). The earlier draft documented a "Pattern C" folder under the domain dossier (docs/domains/archaeology/runbooks/), which Directory Rules does not define as a runbook home and which would create a parallel root (§13.5). Pattern C is retained below as recorded rationale, not as this folder's identity.
  - The OPEN-DR-02 ADR (Pattern A vs Pattern B under docs/runbooks/) is still required to freeze the subfolder convention — see OQ-AR-RB-01.
  - Inherits Archaeology domain sensitivity envelope: T4 default for site coords (T1 generalized only after steward review, Atlas §24.14), T4 forever for human remains / sacred sites (Atlas §24.5.2).
[/KFM_META_BLOCK_V2] -->

# Archaeology Runbooks — `README`

> Per-folder README for the Archaeology-domain operational-procedures folder under the canonical runbooks root: **`docs/runbooks/archaeology/`**. Indexes the runbooks the domain requires (sovereignty review, emergency disablement, source refresh, correction / withdrawal, rollback drill, etc.), declares the §15 folder contract, and carries the inherited T4 sensitivity envelope.

<p align="left">
  <img alt="Edition" src="https://img.shields.io/badge/edition-v1.1%20draft-1f6feb">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Folder class: canonical runbooks subfolder" src="https://img.shields.io/badge/class-canonical%20runbooks%20subfolder-2da44e">
  <img alt="Sensitivity envelope: T4 inherited" src="https://img.shields.io/badge/sensitivity-T4%20inherited-c62828">
  <img alt="Sovereignty review path: required" src="https://img.shields.io/badge/sovereignty%20review-required-c62828">
  <img alt="Placement: docs/runbooks Pattern A" src="https://img.shields.io/badge/placement-docs%2Frunbooks%20Pattern%20A-2da44e">
  <img alt="Runbooks planned: 7" src="https://img.shields.io/badge/runbooks%20planned-7-555">
  <img alt="CONTRACT_VERSION 3.0.0" src="https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-555">
  <!-- TODO: replace with live Shields.io endpoints (CI status, last-updated, runbook authoring progress, sovereignty-review readiness) once verified against the mounted repo. -->
</p>

**Status:** draft · **Owners:** _TODO: archaeology-steward; docs-steward; sovereignty-review-liaison; release-steward_ · **Last updated:** 2026-05-29

> [!CAUTION]
> **Sensitivity inherited from the Archaeology domain.** Site coordinates default to **T4 (Denied)** (T1 generalized only after steward review, Atlas §24.14); human remains and sacred sites are **T4 forever** (Atlas v1.1 §24.5.2). Every runbook authored under this folder MUST treat T4 content as a **deny-by-default operational class**: never include exact coordinates, site identifiers, oral-history transcripts, cultural-knowledge notes, or sovereignty-sensitive material as runbook examples or fixture inputs. Enforcement of Archaeology sensitivity lives in `policy/sensitivity/archaeology/`, not in runbooks. Runbooks **invoke** policy; they do not **encode** it.

> [!IMPORTANT]
> **Placement reconciled in v1.1 — canonical home is `docs/runbooks/archaeology/`.** Directory Rules §6.1.b establishes `docs/runbooks/` as the canonical home for operational procedures (source refresh, rollback drills, incident response, steward review), and OPEN-DR-02 recommends the **Pattern A** domain-segment subfolder (`docs/runbooks/<domain>/`), already in use by the fauna source-refresh runbook (`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`). The earlier draft of this README documented a **"Pattern C"** folder under the domain dossier (`docs/domains/archaeology/runbooks/`); that is **not a Directory-Rules-defined runbook home** and would stand up a parallel operational root — the §13.5 "parallel home" / §3 "domain folder must not own a responsibility root" drift. This README now documents the canonical Pattern A folder; the Pattern C discussion is retained in [§7](#7-the-pattern-a-vs-pattern-c-decision-recorded-rationale) as recorded rationale. The remaining open item is the **OPEN-DR-02 ADR** (Pattern A vs Pattern B), tracked as [OQ-AR-RB-01](#10-open-questions-register).

---

## 0. Status & Authority

| Field | Value |
|---|---|
| **Document type** | Per-folder README under the Directory Rules §15 contract. |
| **Edition** | v1.1 draft (v1 → v1.1; placement reconciliation + citation corrections). |
| **Canonical repo path** | **`docs/runbooks/archaeology/README.md`** (Directory Rules §6.1.b Pattern A; OPEN-DR-02 recommended). |
| **Non-canonical alternative (rejected in v1.1)** | `docs/domains/archaeology/runbooks/README.md` ("Pattern C") — not a Directory-Rules-defined runbook home; would create a parallel root. |
| **Folder class** | **Canonical runbooks subfolder** under the canonical responsibility root `docs/`, runbooks sub-root `docs/runbooks/`, domain segment `archaeology/`. Not a compatibility root. |
| **Placement basis** | **CONFIRMED rule** — Directory Rules §6.1.b (`docs/runbooks/` canonical operational-procedure home); §4 Step 3 (domain is a segment inside the responsibility root); OPEN-DR-02 (Pattern A recommended pending ADR). |
| **Operating contract** | `ai-build-operating-contract.md` — `CONTRACT_VERSION = "3.0.0"`. |
| **Sensitivity envelope** | **T4 inherited** from the Archaeology domain (Atlas v1.1 §24.5.2; §24.14 site-coord tier). Sovereignty-review path required (Atlas v1.1 §24.13). |
| **Sensitivity enforcement home** | `policy/sensitivity/archaeology/`. Runbooks here **invoke** that policy; they never substitute for it. |
| **Authoring posture** | Operational only. Runbooks **explain how to operate** (Directory Rules §6.1.b); they do not encode policy (`policy/`) or object meaning (`contracts/`). |
| **Status of this file in any repo** | `draft` until reviewed and merged. AI-authored — `GENERATED_RECEIPT.json` required at merge per contract §34. |
| **Required reviewers** | Docs steward + Archaeology-domain steward + policy steward + sovereignty-review liaison + release steward + AI surface steward (AI-authored content review per contract §33). |

---

## Contents

1. [Purpose and scope](#1-purpose-and-scope)
2. [Authority level and folder class (§15 contract)](#2-authority-level-and-folder-class-15-contract)
3. [What belongs here](#3-what-belongs-here)
4. [What does NOT belong here](#4-what-does-not-belong-here)
5. [Planned runbooks (index)](#5-planned-runbooks-index)
6. [Inputs, outputs, validation, review burden (§15 contract)](#6-inputs-outputs-validation-review-burden-15-contract)
7. [The Pattern A vs Pattern C decision (recorded rationale)](#7-the-pattern-a-vs-pattern-c-decision-recorded-rationale)
8. [Sensitivity envelope (inherited)](#8-sensitivity-envelope-inherited)
9. [Runbook authoring conventions](#9-runbook-authoring-conventions)
10. [Open questions register](#10-open-questions-register)
11. [Open verification backlog](#11-open-verification-backlog)
12. [Definition of done](#12-definition-of-done)
13. [Related docs and ADRs](#13-related-docs-and-adrs)

---

## 1. Purpose and scope

This folder holds **operational runbooks for the Archaeology domain** — the procedural complement to the policy text in `policy/sensitivity/archaeology/`, the schemas in `schemas/contracts/v1/domains/archaeology/`, the object meaning in `contracts/domains/archaeology/`, and the verification items in `docs/domains/archaeology/VERIFICATION_BACKLOG.md`.

> [!NOTE]
> Schema and contract homes use the Directory Rules §12 `domains/` segment (`schemas/contracts/v1/domains/archaeology/`, `contracts/domains/archaeology/`), consistent with the sibling `CANONICAL_PATHS.md` and `ARCHITECTURE.md`. The Atlas v1.1 §24.13 / ENCY §7.13 shorthand (`schemas/contracts/v1/archaeology/`, `contracts/archaeology/`) is LINEAGE; the repo-wide `domains/`-segment decision is tracked at `OQ-CP-01` / `OQ-CI-02` / `OQ-CD-02` / `OQ-ARCH-01`.

### What runbooks are (CONFIRMED, Directory Rules §6.1.b)

Runbooks **explain how to operate**: source refresh, rollback drills, validation runs, incident response, evaluator workflows, steward review. They do not encode policy, object meaning, or schema shape.

### What Archaeology runbooks specifically must cover (CONFIRMED, Atlas v1.0 Ch. 15 §N)

The Atlas verification backlog names four open items, **each of which implies a runbook**:

1. Verify steward authority and confidentiality. → steward-authority-verification runbook.
2. Define public geometry thresholds and transform profiles. → public-geometry-threshold runbook.
3. Verify oral history / cultural knowledge protocol. → sovereignty-review runbook.
4. Verify emergency public-layer disablement and rollback drill. → emergency-disablement runbook (+ the paired `rollback-drill.md`, already drafted in this folder).

Plus the standard cross-domain runbook set (Unified Implementation Build Manual) that every domain needs: source intake / source refresh, rights review, sensitivity review, correction / withdrawal.

### What this folder is NOT

- Not policy. `policy/sensitivity/archaeology/` is the deny-rule home.
- Not schema. `schemas/contracts/v1/domains/archaeology/` is the shape home.
- Not contracts. `contracts/domains/archaeology/` is the meaning home.
- Not data. No site content lives here.
- Not a content store of any kind. Runbooks reference policy, schemas, fixtures, and review records — they do not contain T4-class material.

[↑ Back to top](#contents)

---

## 2. Authority level and folder class (§15 contract)

Per Directory Rules §15, every folder has a README declaring its class via twelve fields. This folder's declaration:

| §15 field | Value |
|---|---|
| **Purpose** | Operational procedures for the Archaeology domain (source refresh, sovereignty review, sensitivity review, emergency disablement, correction / withdrawal, rollback drill, etc.). |
| **Authority level** | **CONFIRMED — canonical runbooks subfolder** (`docs/` → `docs/runbooks/` per §6.1.b → `archaeology/` domain segment per §4 Step 3). Not a compatibility root. |
| **Status** | **PROPOSED placement / CONFIRMED rule.** The §6.1.b rule is CONFIRMED; mounted-repo presence of this folder is NEEDS VERIFICATION. The Pattern A vs Pattern B subfolder convention is the open OPEN-DR-02 ADR. |
| **What belongs here** | See [§3](#3-what-belongs-here). |
| **What does NOT belong here** | See [§4](#4-what-does-not-belong-here). Broad and explicit. |
| **Inputs** | Atlas v1.0 Ch. 15 §N verification items; `policy/sensitivity/archaeology/` rules; `schemas/contracts/v1/domains/archaeology/` schemas; `data/registry/sources/archaeology/` descriptors (by stable ID). Runbooks consume these as **references**; they do not own them. |
| **Outputs** | Steward-runnable procedure documents. Each runbook produces an audit trail (`ReviewRecord`, `RunReceipt`, `RollbackCard`, `CorrectionNotice`) — those audit artifacts live in `data/receipts/`, `release/rollback_cards/`, and `release/correction_notices/`, not here. |
| **Validation** | (PROPOSED) `tests/domains/archaeology/test_runbooks_no_t4_leak.py` — content scan asserting no runbook contains T4-class material. (PROPOSED) `tools/validators/runbook_lint.py` — asserting every runbook follows the §9 authoring conventions. |
| **Review burden** | Every PR touching this folder: docs steward + archaeology-domain steward + sovereignty-review liaison. Runbooks touching release / rollback procedures additionally require release steward. AI-authored PRs additionally require AI surface steward per contract §33. |
| **Related folders** | `docs/runbooks/` (canonical runbooks root parent), `docs/domains/archaeology/` (domain dossier), `policy/sensitivity/archaeology/` (enforcement), `release/rollback_cards/`, `release/correction_notices/`, `data/receipts/`. |
| **ADRs governing this folder** | **NEEDS** — OPEN-DR-02 ADR (Pattern A vs Pattern B subfolder convention); see [OQ-AR-RB-01](#10-open-questions-register). |
| **Last reviewed** | 2026-05-29. |

[↑ Back to top](#contents)

---

## 3. What belongs here

CONFIRMED scope. The following runbook classes belong in `docs/runbooks/archaeology/` (full list in [§5](#5-planned-runbooks-index)):

- **This README** (`README.md`) — the §15-contract README you are reading.
- **`rollback-drill.md`** — the rollback drill runbook (drafted; the paired-drill complement to emergency disablement).
- Source intake / source refresh runbooks (one per source family or grouped).
- Sovereignty review runbook (oral history / cultural knowledge protocol).
- Sensitivity review runbook (T4 enforcement; `RedactionReceipt` workflow).
- Public geometry threshold runbook (generalization profiles; T4 → T1 transitions).
- Emergency public-layer disablement runbook (Atlas v1.0 Ch. 15 §N item 4).
- Steward authority verification runbook (Atlas v1.0 Ch. 15 §N item 1).
- Correction / withdrawal runbook (`CorrectionNotice` + `RollbackCard` workflow for T4 leaks).

> [!NOTE]
> The only open structural question is the **subfolder convention** (Pattern A `docs/runbooks/archaeology/<file>` vs Pattern B flat `docs/runbooks/archaeology_<topic>.md`), resolved by the OPEN-DR-02 ADR. The recommendation pending that ADR is Pattern A, which this folder adopts. There is no longer a live "Pattern C" (domain-dossier) proposal; see [§7](#7-the-pattern-a-vs-pattern-c-decision-recorded-rationale).

[↑ Back to top](#contents)

---

## 4. What does NOT belong here

EXPLICIT deny list. The §15 contract treats "what does NOT belong" as load-bearing as "what does belong."

**Sensitivity-class deny (T4-inherited, ABSOLUTE):**

- ❌ Archaeological site coordinates, exact or generalized — even as runbook examples.
- ❌ Site names, codes, or identifiers tied to a real location.
- ❌ Human remains location, burial site, or sacred-site information.
- ❌ Oral history transcripts or cultural-knowledge notes.
- ❌ Sovereignty-sensitive material of any kind (treaty, tribal-relationship, repatriation context).
- ❌ Private landowner details, collection-security details, looting-risk exposure.
- ❌ Real `CandidateFeature` records that have not cleared sovereignty review.
- ❌ Field-survey records, excavation records, provenience packets.
- ❌ Artifact / collection / repository records.
- ❌ Source-credential information (SHPO access tokens, lab-report credentials, etc.).

**Authority-class deny (runbooks invoke; never encode):**

- ❌ Policy text. Lives in `policy/sensitivity/archaeology/`. Runbooks reference policy by name and link; they do not restate or override it.
- ❌ Object-family contract text. Lives in `contracts/domains/archaeology/`.
- ❌ Schema files. Live in `schemas/contracts/v1/domains/archaeology/`.
- ❌ Source descriptors. Live in `data/registry/sources/archaeology/`. Runbooks may *cite* a descriptor by stable ID; they do not *contain* one.
- ❌ Release manifests, rollback cards, correction notices. Those are *emitted by* runbooks but *live in* `release/`.
- ❌ Receipts (`RunReceipt`, `AIReceipt`, `GENERATED_RECEIPT`, `RedactionReceipt`, `AggregationReceipt`). Live in `data/receipts/` or `release/`.
- ❌ Verification-backlog items. Live in `docs/domains/archaeology/VERIFICATION_BACKLOG.md` (per-domain) or `docs/registers/VERIFICATION_BACKLOG.md` (cross-domain).

**Operational deny:**

- ❌ AI-drafted runbooks without `GENERATED_RECEIPT.json` per contract §34.
- ❌ Runbooks that bypass the trust membrane (e.g., describe direct queries against `data/raw/` or `data/processed/` from a public client). Runbooks that traverse the lifecycle MUST do so via governed APIs.
- ❌ Runbooks that present AI-generated language as steward-approved without an explicit `ReviewRecord` step.
- ❌ Runbooks that omit a `RollbackCard` step when the procedure changes public state.
- ❌ Filenames that themselves reveal sensitive identifiers.

> [!CAUTION]
> A runbook that needs T4-class material to demonstrate a procedure (e.g., "here is how the redaction transform looks on a real site record") MUST use a **synthetic, public-safe fixture** with a Reality Boundary Note and Representation Receipt, never real data. Synthetic-as-observed presentation is itself a §38 anti-pattern (Atlas §24.1.2: "Synthetic content presented as observed reality → DENY publication; HOLD for steward review; ABSTAIN at AI").

[↑ Back to top](#contents)

---

## 5. Planned runbooks (index)

PROPOSED. Each row names a runbook this folder should carry. Atlas-anchored runbooks are CONFIRMED-needed (Ch. 15 §N); cross-domain-standard runbooks are CONFIRMED-needed (Unified Implementation Build Manual set). Filenames follow the casing convention pending OPEN-DR-04 / `OQ-AR-RB-03` — the fauna precedent is UPPERCASE_WITH_UNDERSCORES (`SOURCE_REFRESH_RUNBOOK.md`), while the drafted `rollback-drill.md` uses lowercase-with-hyphens; this inconsistency is the casing question, not yet frozen.

| Filename (PROPOSED) | Purpose | Atlas / doctrine anchor | Status |
|---|---|---|---|
| `rollback-drill.md` | Scheduled drill exercising emergency public-layer disablement + rollback against a synthetic T4 fixture. | **Atlas v1.0 Ch. 15 §N item 4** (load-bearing). | **drafted** (sibling doc) |
| `SOURCE_REFRESH_RUNBOOK.md` | Refresh of SHPO / state inventory, NRHP-like listings, survey forms, lab reports, historic maps. Mirrors fauna Pattern A precedent. | UIBM "Source refresh"; Atlas Ch. 15 §D source families. | _not yet authored_ |
| `STEWARD_AUTHORITY_VERIFICATION_RUNBOOK.md` | Verify the domain steward's authority and confidentiality obligations are in force before any release. | **Atlas v1.0 Ch. 15 §N item 1.** | _not yet authored_ |
| `PUBLIC_GEOMETRY_THRESHOLD_RUNBOOK.md` | Define and apply generalization thresholds and transform profiles for T4 → T1 site-location releases. Emits `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`. | **Atlas v1.0 Ch. 15 §N item 2.** | _not yet authored_ |
| `SOVEREIGNTY_REVIEW_RUNBOOK.md` | Oral history and cultural-knowledge protocol; handles tribal-relationship, treaty, repatriation, and rights-holder review for any record sourced from oral history / cultural knowledge. | **Atlas v1.0 Ch. 15 §N item 3** + Atlas §24.13 sovereignty-review notes. | _not yet authored_ |
| `EMERGENCY_DISABLEMENT_RUNBOOK.md` | Disable a public archaeology layer immediately on T4 leak detection; emit `CorrectionNotice` + `RollbackCard`; the real-incident procedure that `rollback-drill.md` rehearses. | **Atlas v1.0 Ch. 15 §N item 4** (load-bearing). | _not yet authored_ |
| `SENSITIVITY_REVIEW_RUNBOOK.md` | Cross-domain sensitivity-review pattern applied to archaeology: T4 enforcement, `RedactionReceipt` lifecycle, steward sign-off. | UIBM "Sensitivity review"; Atlas §24.5.2. | _not yet authored_ |
| `CORRECTION_AND_WITHDRAWAL_RUNBOOK.md` | Handle detected errors or new evidence requiring `CorrectionNotice`, withdrawal, derivative invalidation, and steward-approved supersession. | UIBM "Correction/withdrawal"; contract §10.9 corrections-first-class. | _not yet authored_ |

> [!IMPORTANT]
> The **emergency disablement runbook** (and its paired `rollback-drill.md`, already drafted) is the single most load-bearing artifact this folder hosts. Atlas v1.0 Ch. 15 §N item 4 names it as a verification item; without a tested rollback drill, public Archaeology release is blocked. The sovereignty-review runbook is a close second, since it grounds the steward-authority chain that several other runbooks invoke (see `OQ-AR-RB-05`).

[↑ Back to top](#contents)

---

## 6. Inputs, outputs, validation, review burden (§15 contract)

| §15 field | Detail |
|---|---|
| **Inputs** | Atlas v1.0 Ch. 15 §N verification items; `policy/sensitivity/archaeology/` rule names; `schemas/contracts/v1/domains/archaeology/` schema names; `data/registry/sources/archaeology/` source descriptors (by stable ID only). No source-data inputs. No T4 content. |
| **Outputs** | Each runbook is a step-by-step procedure document. Procedures may **emit** governed artifacts (`ReviewRecord`, `RunReceipt`, `RollbackCard`, `CorrectionNotice`, `RedactionReceipt`), but those artifacts land in their canonical homes (`data/receipts/`, `release/rollback_cards/`, `release/correction_notices/`), not here. |
| **Validation** | (PROPOSED) `tests/domains/archaeology/test_runbooks_no_t4_leak.py` content scan against `policy/sensitivity/archaeology/` term lists. (PROPOSED) `tools/validators/runbook_lint.py` enforcing §9 authoring conventions (preconditions, steps, gates, rollback, receipts). Both validators are PROPOSED and depend on policy / tooling that itself is PROPOSED. |
| **Review burden** | Docs steward + archaeology-domain steward + sovereignty-review liaison on **every** PR touching this folder. Runbooks that change rollback / correction procedures additionally require release steward sign-off. PRs that introduce new runbook examples must include explicit acknowledgement that examples are synthetic (per §4). AI-authored PRs require AI surface steward review per contract §33. |
| **Related folders** | `docs/runbooks/` (canonical runbooks root; see §7), `docs/domains/archaeology/` (domain dossier), `policy/sensitivity/archaeology/` (enforcement home), `release/rollback_cards/`, `release/correction_notices/`, `data/receipts/`, `data/quarantine/`. |
| **ADRs governing this folder** | None yet accepted. OPEN-DR-02 ADR proposed (Pattern A vs Pattern B). |
| **Last reviewed** | 2026-05-29. |

[↑ Back to top](#contents)

---

## 7. The Pattern A vs Pattern C decision (recorded rationale)

PROPOSED rationale, retained for the record. The canonical runbooks home is `docs/runbooks/` (Directory Rules §6.1, §6.1.b). The fauna source-refresh runbook lives at `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` — the Pattern A precedent. An earlier draft of this folder proposed a third pattern (runbooks under the domain dossier); that proposal is **not adopted**.

```mermaid
flowchart TB
    NEED[An Archaeology runbook needs<br/>to be authored]
    PA[Pattern A — ADOPTED<br/>docs/runbooks/archaeology/]
    PB[Pattern B — alternative<br/>docs/runbooks/archaeology_*.md]
    PC[Pattern C — rejected<br/>docs/domains/archaeology/runbooks/]
    DR[Directory Rules §6.1.b<br/>+ OPEN-DR-02 recommendation]
    ADR[OPEN-DR-02<br/>ADR-class question §2.4]
    PREC[Pattern A precedent:<br/>docs/runbooks/fauna/<br/>SOURCE_REFRESH_RUNBOOK.md]

    NEED --> PA
    NEED -.legacy convention.-> PB
    NEED -.x rejected.-> PC

    PA --> DR
    PB --> ADR
    PC -.parallel root §13.5.-> PC

    DR -.recommends.-> PA
    PREC -.supports.-> PA

    classDef pref fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px,color:#000;
    classDef reject fill:#ffebee,stroke:#c62828,stroke-width:1px,color:#000;
    classDef neut fill:#eceff1,stroke:#37474f,stroke-width:1px,color:#000;

    class PA pref;
    class PC reject;
    class PB neut;
```

| Pattern | Path shape | Status | Trade-offs |
|---|---|---|---|
| **A — ADOPTED** | `docs/runbooks/archaeology/<RUNBOOK>.md` | CONFIRMED canonical per §6.1.b; recommended per OPEN-DR-02; this folder. | Co-locates archaeology runbooks with all other domain runbooks; standardizes review path; matches fauna precedent. Splits archaeology dossier content across `docs/domains/archaeology/` and `docs/runbooks/archaeology/` — acceptable, since runbooks are a distinct responsibility. |
| **B — flat** | `docs/runbooks/archaeology_<topic>.md` | PROPOSED in some legacy planning. | Simple for one-or-two-runbook domains. Filenames grow long as topics accumulate. Less preferred per OPEN-DR-02. The OPEN-DR-02 ADR decides A vs B. |
| **C — rejected** | `docs/domains/archaeology/runbooks/<RUNBOOK>.md` | **Rejected in v1.1.** | Would keep all archaeology dossier content in one place, but Directory Rules §6.1.b does not define a runbook home under the domain dossier; it would create a parallel operational root (§13.5 "parallel home"; §3 "domain folder must not own a responsibility root"). Not adopted. |

> [!IMPORTANT]
> **Decision:** runbooks live at `docs/runbooks/archaeology/<RUNBOOK>.md` (Pattern A). The only remaining ADR is **OPEN-DR-02** (Pattern A vs Pattern B under `docs/runbooks/`), which the project SHOULD file to freeze the subfolder convention repo-wide. If any "Pattern C" file is found under `docs/domains/archaeology/runbooks/`, it is migrated to this folder and the move is logged in `docs/registers/DRIFT_REGISTER.md`.

[↑ Back to top](#contents)

---

## 8. Sensitivity envelope (inherited)

CONFIRMED, Atlas v1.1 §24.5.2 + §24.14 + Encyclopedia §7.13. The envelope flows into every runbook authored under this folder unchanged.

| Object class | Default tier | Allowed transforms | Required gates |
|---|---|---|---|
| Archaeological site location | **T4** (T1 generalized only after steward review, Atlas §24.14) | Steward + cultural review + generalized geometry (coarse cell) + `RedactionReceipt` → T2 / T1. | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`. |
| Human remains / sacred sites | **T4 forever** | No transform releases this to T0; T3 only under explicit named authorization. | Sovereignty review + `ReviewRecord` + `PolicyDecision`. |
| Oral history / cultural knowledge | Source-rights `NEEDS VERIFICATION`; sensitive joins fail closed. | Per source rights; default deny. | Source-rights review + steward review. |
| Private landowner / collection-security details | **T4** | None permit public release without policy + steward review. | `PolicyDecision` + `ReviewRecord`. |
| `CandidateFeature` (not yet promoted) | Held in WORK / QUARANTINE | Not public; promotion requires review. | Promotion gate; no PUBLISHED edge to WORK / QUARANTINE. |

**Runbook implication.** Every Archaeology runbook MUST:

- name the exact `policy/sensitivity/archaeology/` rule it depends on;
- name the exact `ReviewRecord`, `PolicyDecision`, `RedactionReceipt`, or `RollbackCard` it emits;
- specify the gate that fails closed if any of the above are missing;
- use synthetic fixtures for any example output;
- defer to the domain steward and sovereignty-review liaison on ambiguous cases.

> [!CAUTION]
> **A runbook that loosens sensitivity bounds in its procedure** — for example, by describing a "fast path" that skips sovereignty review for "low-risk" sites — is itself a doctrine drift. File such cases to `docs/registers/DRIFT_REGISTER.md` and route to steward review. T4 defaults do not have fast paths.

[↑ Back to top](#contents)

---

## 9. Runbook authoring conventions

PROPOSED. Every runbook authored under this folder SHOULD follow these conventions. The conventions are designed to be enforceable by the `runbook_lint.py` validator proposed in §6.

### Required runbook sections

```text
1. KFM Meta Block v2
2. Title + one-line purpose
3. Badge row (status, sensitivity envelope, last-rehearsed-date)
4. Status & Authority table
5. Preconditions (what MUST be true before the runbook runs)
6. Roles (who runs which step; CODEOWNERS-aligned)
7. Procedure (numbered, atomic steps)
8. Gates (which step requires which receipt / review / policy decision)
9. Emitted artifacts (RunReceipt, ReviewRecord, RollbackCard, CorrectionNotice, ...)
10. Rollback path (every public-state change MUST have one)
11. Failure modes and DENY conditions
12. Post-conditions (what MUST be true after the runbook completes)
13. Rehearsal cadence (drill schedule — at minimum annually for emergency runbooks)
14. Open questions register
15. Definition of done
16. Related docs and ADRs
```

### Required posture

- **Steward-driven, not AI-driven.** AI MAY draft the prose; the steward signs off on the procedure. `AIReceipt` and `GENERATED_RECEIPT.json` MUST be emitted for AI-drafted runbooks per contract §34.
- **Fail-closed everywhere.** Any step that cannot produce its required receipt halts the runbook and routes to steward review.
- **Receipt-emitting.** Every governed transition emits a receipt; receipts land in their canonical homes (`data/receipts/`, `release/`).
- **Rollback-bearing.** Every public-state change has a named `RollbackCard` and a tested drill.
- **Synthetic-only examples.** No real archaeological content in examples (§4 deny list).
- **Negative-state-exercising.** Procedures and their validators MUST exercise DENY / ABSTAIN / quarantine paths, not just the happy path (contract §38 negative-state expectation).

### Forbidden patterns

- "Skip review if X" — no fast paths around steward / sovereignty / sensitivity gates.
- "AI summary is sufficient" — AI summaries are NOT review.
- "Cite the dashboard" — dashboards are not sovereign truth (contract §38; Atlas §23.4 "no dashboard is sovereign truth by display alone").
- "Backfill the receipt later" — receipts are emitted at the transition, not retrofitted.
- "The map shows it, so it is true" — Atlas §24.1.2 / Master MapLibre §10.

[↑ Back to top](#contents)

---

## 10. Open questions register

PROPOSED. Questions about this folder, distinct from Archaeology-domain verification items.

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| **OQ-AR-RB-01** | **(Reframed in v1.1.)** Domain runbooks live at `docs/runbooks/<domain>/` (Pattern A, this folder) per Directory Rules §6.1.b. The remaining open question is **OPEN-DR-02**: Pattern A (subfolder) vs Pattern B (flat with domain prefix) under `docs/runbooks/`. The earlier "Pattern C" (domain-dossier) proposal is rejected (§7). | Docs steward + Directory-Rules editor + archaeology-domain steward + release steward | ADR for OPEN-DR-02 (Pattern A vs B). Migrate any stray Pattern C file to this folder; log in `DRIFT_REGISTER.md`. |
| **OQ-AR-RB-02** | If a domain ever wants the dossier-internal layout, is that per-domain elective or repo-wide? (Largely moot given §7's rejection of Pattern C, but recorded in case a future ADR revisits it.) | Docs steward + each domain steward | ADR; document outcome in Directory Rules §6.1.b. |
| **OQ-AR-RB-03** | Filename casing for runbooks: `UPPERCASE_WITH_UNDERSCORES` (the fauna `SOURCE_REFRESH_RUNBOOK.md` precedent) vs `lowercase-with-hyphens` (the drafted `rollback-drill.md`). This is Directory Rules §18.b OPEN-DR-04; connects to the casing conflict flagged in the sibling api-contracts doc (`OQ-AR-API-07`) and the rollback-drill doc (`OQ-AR-RB-DRILL-03`). | Docs steward | Convention decision; codify in `docs/runbooks/README.md` or Directory Rules §6.1.b. |
| **OQ-AR-RB-04** | Should the `runbook_lint.py` validator (§6 PROPOSED) be repo-wide and folder-agnostic, or domain-scoped? | Docs steward + tools owner | ADR if cross-domain. |
| **OQ-AR-RB-05** | Authoring order: which of the §5 runbooks lands first after `rollback-drill.md`? §5 calls out emergency disablement as load-bearing; the steward roster may prefer to lead with the sovereignty-review runbook to ground the steward-authority chain before further drill rehearsal. | Archaeology steward + sovereignty-review liaison | Steward roster decision; document here and in `docs/domains/archaeology/VERIFICATION_BACKLOG.md`. |

[↑ Back to top](#contents)

---

## 11. Open verification backlog

PROPOSED. Items that remain `NEEDS VERIFICATION` for this folder before promotion from `draft` to `published`.

1. Confirm placement at `docs/runbooks/archaeology/README.md` (Directory Rules §6.1.b Pattern A) and confirm `docs/runbooks/archaeology/` exists or is recognized as the Pattern A target. If any Pattern C folder (`docs/domains/archaeology/runbooks/`) exists, log the parallel-home drift to `DRIFT_REGISTER.md` and migrate.
2. Confirm `docs/runbooks/README.md` (canonical runbooks root README) exists.
3. Confirm `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` (Pattern A precedent) exists in the mounted repo; verify its conventions to template archaeology runbooks against.
4. Confirm `policy/sensitivity/archaeology/` exists with a term list that the proposed `test_runbooks_no_t4_leak.py` validator can scan against.
5. Confirm `release/rollback_cards/`, `release/correction_notices/`, and `data/receipts/` exist as canonical homes for emitted artifacts.
6. Confirm `archaeology-steward`, `docs-steward`, `sovereignty-review-liaison`, `release-steward`, `policy-steward`, and `AI-surface-steward` are roles defined in `CODEOWNERS`.
7. Confirm `GENERATED_RECEIPT.json` for this file's authorship is emitted at merge and references `CONTRACT_VERSION = "3.0.0"` (contract §34, §34.4 well-formedness gates).
8. Confirm OPEN-DR-02 status (Directory Rules §18.b) and the runbook-casing OPEN-DR-04 — they materially constrain `OQ-AR-RB-01` / `OQ-AR-RB-03`.
9. Confirm the drafted `rollback-drill.md` is co-located in this folder (it was reconciled to `docs/runbooks/archaeology/rollback-drill.md` in its own v1.1).
10. Confirm any in-flight or accidentally-committed runbook drafts pass the §4 deny list. If not, quarantine immediately.

[↑ Back to top](#contents)

---

## 12. Definition of done

This README (and the folder it documents) is done enough to enter the repository when:

- the folder is placed at `docs/runbooks/archaeology/` per Directory Rules §6.1.b (Pattern A), **with this README at its root** — **not** under the domain dossier;
- docs steward, archaeology-domain steward, policy steward, sovereignty-review liaison, and release steward have reviewed and approved it;
- **the OPEN-DR-02 ADR is filed** (Pattern A vs Pattern B under `docs/runbooks/`) — the folder MAY land before the ADR is accepted, but the ADR SHOULD be open at merge to legitimize the subfolder convention (`OQ-AR-RB-01`);
- it is linked from `docs/runbooks/README.md` (canonical runbooks root) and from `docs/domains/archaeology/README.md` (so a reader at the dossier can find the runbooks);
- any stray Pattern C folder (`docs/domains/archaeology/runbooks/`) is migrated here and the move is logged in `docs/registers/DRIFT_REGISTER.md`;
- the PROPOSED validators from §6 are at least planned (issues exist), even if the tests are not yet written;
- the `GENERATED_RECEIPT.json` planned for AI authorship is wired into CI per contract §34 with `CONTRACT_VERSION = "3.0.0"`;
- no file in the folder, including this README, contains any T4-class archaeological content per §4;
- future changes follow contract §37 lifecycle.

[↑ Back to top](#contents)

---

## 13. Related docs and ADRs

PROPOSED links. All paths are PROPOSED until verified against a mounted repo. Relative paths assume the canonical location `docs/runbooks/archaeology/README.md`.

- [`docs/doctrine/ai-build-operating-contract.md`](../../doctrine/ai-build-operating-contract.md) — _TODO_ — operating contract v3.0; `CONTRACT_VERSION = "3.0.0"`; §§33, 34, 37, 38.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — _TODO_ — placement; §6.1.b runbooks contract; §15 per-folder README contract; §18.b OPEN-DR-02 / OPEN-DR-04.
- [`./rollback-drill.md`](./rollback-drill.md) — rollback drill runbook (drafted; sibling in this folder).
- [`docs/runbooks/README.md`](../README.md) — _TODO_ — canonical runbooks root README.
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../fauna/SOURCE_REFRESH_RUNBOOK.md) — _TODO_ — Pattern A precedent; template for archaeology source-refresh runbook.
- [`docs/domains/archaeology/README.md`](../../domains/archaeology/README.md) — _TODO_ — Archaeology domain README (existence NEEDS VERIFICATION).
- [`docs/domains/archaeology/ARCHITECTURE.md`](../../domains/archaeology/ARCHITECTURE.md) — Archaeology domain architecture; §13 publication/correction/rollback links the rollback drill.
- [`docs/domains/archaeology/VERIFICATION_BACKLOG.md`](../../domains/archaeology/VERIFICATION_BACKLOG.md) — _TODO_ — Archaeology verification backlog (per-domain).
- [`docs/domains/archaeology/CHANGELOG.md`](../../domains/archaeology/CHANGELOG.md) — _TODO_ — Archaeology dossier changelog (PROPOSED).
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — _TODO_ — drift entries (especially any stray Pattern C folder, and runbook filename casing).
- [`docs/adr/README.md`](../../adr/README.md) — _TODO_ — ADR index; OPEN-DR-02 to be filed here.
- [`policy/sensitivity/archaeology/`](../../../policy/sensitivity/archaeology/) — _TODO_ — sensitivity enforcement (canonical). Runbooks invoke; never substitute.
- [`release/rollback_cards/`](../../../release/rollback_cards/) — _TODO_ — canonical home for `RollbackCard` artifacts emitted by runbooks.
- [`release/correction_notices/`](../../../release/correction_notices/) — _TODO_ — canonical home for `CorrectionNotice` artifacts emitted by runbooks.

**ADRs governing this folder (when filed):**

- ADR-PROPOSED — Domain-runbook subfolder convention freeze (Directory Rules OPEN-DR-02 / `OQ-AR-RB-01`); resolves Pattern A vs Pattern B.
- ADR-PROPOSED — Runbook / standards filename casing (Directory Rules OPEN-DR-04 / `OQ-AR-RB-03`).

---

> [!NOTE]
> **Last updated:** 2026-05-29 · **Edition:** v1.1 draft · **`CONTRACT_VERSION = "3.0.0"`** · **Folder class:** canonical runbooks subfolder (`docs/runbooks/archaeology/`) · **Sensitivity:** T4 inherited · **Authority:** Directory Rules §6.1.b runbooks placement contract + §15 per-folder README contract.

[↑ Back to top](#contents)
