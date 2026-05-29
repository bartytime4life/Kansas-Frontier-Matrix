<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-archaeology-missing-or-planned-files-readme
title: Archaeology Dossier — missing_or_planned_files/ README
type: standard
version: v1.1
status: draft
owners: <TODO: archaeology-steward; docs-steward; sovereignty-review-liaison>
created: 2026-05-27
updated: 2026-05-29
policy_label: public
related:
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ARCHITECTURE.md
  - docs/domains/archaeology/VERIFICATION_BACKLOG.md
  - docs/domains/archaeology/CHANGELOG.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/adr/README.md
  - policy/sensitivity/archaeology/
tags: [kfm, archaeology, planning, dossier, governance, sensitive-domain]
notes:
  - CONTRACT_VERSION = "3.0.0" (pinned per ai-build-operating-contract.md §37 versioning + CONTRACT_VERSION pinning convention).
  - Planning index ONLY — NEVER a content store for archaeology data.
  - Folder placement and naming are PROPOSED and ADR-class per Directory Rules §2.4(5) (new parallel home); see OQ-AR-MPF-01. There is NO canonical Directory-Rules home for a per-domain planning subfolder — the preferred alternative is the CHANGELOG.md "_not yet authored_" rows pattern.
  - Inherits Archaeology domain sensitivity envelope: T4 default for site coords (T1 generalized only after steward review, Atlas §24.14), T4 forever for human remains / sacred sites (Atlas §24.5.2).
[/KFM_META_BLOCK_V2] -->

# Archaeology Dossier — `missing_or_planned_files/` README

> Per-folder README for a **planning index** inside the Archaeology dossier. Tracks the existence and intended scope of dossier files that have been referenced from sibling docs but **not yet authored** — and **forbids** the folder from becoming a content store for sensitive archaeological material. The README is candid that this folder is **not a Directory-Rules-defined construct**: the preferred path is to retire it in favor of the lighter `CHANGELOG.md` "_not yet authored_" row pattern (see §6).

<p align="left">
  <img alt="Edition" src="https://img.shields.io/badge/edition-v1.1%20draft-1f6feb">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Folder class: domain-internal" src="https://img.shields.io/badge/class-domain--internal-blue">
  <img alt="Sensitivity envelope: T4 inherited" src="https://img.shields.io/badge/sensitivity-T4%20inherited-c62828">
  <img alt="Sovereignty review path: required" src="https://img.shields.io/badge/sovereignty%20review-required-c62828">
  <img alt="Placement: PROPOSED — ADR-class (§2.4-5)" src="https://img.shields.io/badge/placement-PROPOSED%20%C2%B7%20ADR--class%20%C2%A72.4(5)-orange">
  <img alt="CONTRACT_VERSION 3.0.0" src="https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-555">
  <!-- TODO: replace with live Shields.io endpoints (CI status, last-updated, sovereignty-review-status) once verified against the mounted repo. -->
</p>

**Status:** draft · **Owners:** _TODO: archaeology-steward; docs-steward; sovereignty-review-liaison_ · **Last updated:** 2026-05-29

> [!CAUTION]
> **This folder is a planning index. It is NOT a content store.** Archaeology defaults to **T4 (Denied)** for site coordinates (T1 generalized only after steward review, Atlas §24.14) and **T4 forever** for human remains, sacred sites, and sovereignty-sensitive material (Atlas v1.1 §24.5.2). Nothing in this folder may carry actual site geometry, coordinates, oral-history transcripts, cultural-knowledge notes, candidate-site lists, collection-security details, or any T4-class content — **even in draft, even commented out, even in filenames**. Enforcement of Archaeology sensitivity lives in `policy/sensitivity/archaeology/`, not here.

> [!WARNING]
> **Placement is PROPOSED and is ADR-class.** This folder creates a **parallel home** for planning/intake content already served by `docs/registers/VERIFICATION_BACKLOG.md`, the per-domain `VERIFICATION_BACKLOG.md`, and the per-domain `CHANGELOG.md` "_not yet authored_" rows. Directory Rules **§2.4(5)** flags "a new parallel home or split" as ADR-class (the same trigger that makes the receipt-class-home question ADR-S-03 ADR-class). There is **no Directory-Rules construct** for a per-domain `missing_or_planned_files/` folder; unlike runbooks (which have a canonical home at `docs/runbooks/`), this folder has no canonical home to relocate to — the doctrine-correct alternative is to **not have the folder** and use the `CHANGELOG.md` row pattern instead. See [OQ-AR-MPF-01](#8-open-questions-register). Until that ADR is filed and accepted, the folder MUST stay narrowly scoped per §3 below.

---

## 0. Status & Authority

| Field | Value |
|---|---|
| **Document type** | Per-folder README under the Directory Rules §15 contract. |
| **Edition** | v1.1 draft (v1 → v1.1; citation + namespace corrections). |
| **Proposed repo path** | `docs/domains/archaeology/missing_or_planned_files/README.md` |
| **Folder class** | **Domain-internal subfolder** (PROPOSED). Not a canonical root, not a compatibility root. Sits beneath the canonical responsibility root `docs/` and the per-domain dossier `docs/domains/archaeology/`. **Not a Directory-Rules-defined construct.** |
| **Placement basis** | **PROPOSED / ADR-class.** Directory Rules §4 Step 3 admits the parent dossier; the subfolder itself is a **new parallel planning home**, ADR-class per **§2.4(5)**. See OQ-AR-MPF-01. |
| **Naming convention** | **PROPOSED — non-standard.** `missing_or_planned_files` uses lowercase_with_underscores; Directory Rules' documented folder conventions are lowercase (`runbooks/`) or lowercase-with-hyphens (`roads-rail-trade/`). A rename to `missing-or-planned-files/` would match the multi-word convention. Flagged at [OQ-AR-MPF-02](#8-open-questions-register). |
| **Operating contract** | `ai-build-operating-contract.md` — `CONTRACT_VERSION = "3.0.0"`. |
| **Sensitivity envelope** | **T4 inherited** from the Archaeology domain. Site location T4 default (T1 after steward review, Atlas §24.14); human remains / sacred sites T4 forever (Atlas v1.1 §24.5.2). Sovereignty-review path required for any release (Atlas v1.1 §24.13). |
| **Sensitivity enforcement home** | `policy/sensitivity/archaeology/` (PROPOSED canonical, Atlas §24.13). **Not** this folder. |
| **Status of this file in any repo** | `draft` until reviewed and merged. AI-authored — `GENERATED_RECEIPT.json` required at merge per contract §34. |
| **Required reviewers** | Docs steward + Archaeology-domain steward + policy steward + sovereignty-review liaison + AI surface steward (AI-authored content review per contract §33). |

---

## Contents

1. [Purpose and scope](#1-purpose-and-scope)
2. [Authority level and folder class (§15 contract)](#2-authority-level-and-folder-class-15-contract)
3. [What belongs here](#3-what-belongs-here)
4. [What does NOT belong here](#4-what-does-not-belong-here)
5. [Inputs, outputs, validation, review burden (§15 contract)](#5-inputs-outputs-validation-review-burden-15-contract)
6. [Relationship to existing planning surfaces](#6-relationship-to-existing-planning-surfaces)
7. [Sensitivity envelope (inherited)](#7-sensitivity-envelope-inherited)
8. [Open questions register](#8-open-questions-register)
9. [Open verification backlog](#9-open-verification-backlog)
10. [Definition of done](#10-definition-of-done)
11. [Related docs and ADRs](#11-related-docs-and-adrs)

---

## 1. Purpose and scope

This folder exists to **track placeholders** for Archaeology dossier files that have been referenced from sibling documents but not yet authored — and to **prevent those placeholders from quietly accumulating sensitive content** under a benign folder name.

### What this folder does

- Holds a **planning index** (this README plus, optionally, very thin per-file stubs that contain only forward-looking metadata).
- Names files that other Archaeology dossier docs reference as TODO targets, so reviewers can see in one place what is promised but not delivered.
- Surfaces the placement and naming question (OQ-AR-MPF-01, OQ-AR-MPF-02) for ADR resolution.

### What this folder is NOT

- Not a register. Not a backlog. Not an intake. Not a CHANGELOG. Not a sensitivity policy.
- Not a substitute for `docs/registers/VERIFICATION_BACKLOG.md` or the per-domain `VERIFICATION_BACKLOG.md` (when they exist).
- Not a substitute for the `CHANGELOG.md` "_not yet authored_" row pattern.
- Not a holding pen for sensitive archaeological material in any form.

> [!IMPORTANT]
> If a planned file's content turns out to need sensitive material (e.g., a draft of a preservation/transform matrix discussing site-specific transforms), that file is authored **outside this folder** — under the proper responsibility root (`policy/sensitivity/archaeology/` for policy text, `data/quarantine/` for unresolved candidate material, etc.). This folder receives only the **stub marker**, not the content.

[↑ Back to top](#contents)

---

## 2. Authority level and folder class (§15 contract)

Per Directory Rules §15, every folder has a README declaring its class via twelve fields. This folder's declaration:

| §15 field | Value |
|---|---|
| **Purpose** | Planning index for not-yet-authored files referenced from the Archaeology dossier; surfaces the ADR-class placement question. |
| **Authority level** | **Domain-internal subfolder.** **Not** canonical. **Not** compatibility. **Not** a Directory-Rules-defined construct. The class is **PROPOSED**; if adopted across domains, it would need an entry in Directory Rules §6.1. |
| **Compatibility class** (if compatibility) | N/A. |
| **Status** | **PROPOSED.** ADR-class per Directory Rules §2.4(5) (new parallel home). |
| **What belongs here** | See [§3](#3-what-belongs-here). Narrow. |
| **What does NOT belong here** | See [§4](#4-what-does-not-belong-here). Broad and explicit. |
| **Inputs** | TODO references from sibling Archaeology dossier docs (e.g., `README.md`, `VERIFICATION_BACKLOG.md`, `CHANGELOG.md`); no source-data inputs. |
| **Outputs** | Planning visibility only. No artifacts feed downstream consumers. |
| **Validation** | Stub-file content scan: no T4-class material may appear in any file in this folder. Validator PROPOSED; see [§9 item 4](#9-open-verification-backlog). |
| **Review burden** | Docs steward + archaeology-domain steward + sovereignty-review liaison on every PR touching this folder. |
| **Related folders** | `docs/domains/archaeology/` (parent), `docs/registers/`, `policy/sensitivity/archaeology/`. |
| **ADRs** | **NEEDS** — ADR proposed to resolve OQ-AR-MPF-01 (does this folder pass §2.4(5), or should it be retired?). |
| **Last reviewed** | 2026-05-29. |

[↑ Back to top](#contents)

---

## 3. What belongs here

CONFIRMED narrow scope. The full list:

- **This README** (`README.md`) — the §15-contract README you are reading.
- **Optional thin stub files**, one per planned dossier file, named identically to the planned file (e.g., `ARCHITECTURE.md` would already exist; a not-yet-authored file like `OBJECT_FAMILIES.md`). Each stub MUST contain only:
  - the KFM Meta Block v2 with `status: planned`;
  - a one-paragraph statement of intended scope (no archaeological content);
  - a link to the doc(s) that reference it as a TODO;
  - a target authoring date (PROPOSED) and owner role;
  - the same sensitivity callout from §0 of this README.
- Nothing else.

Stub files SHOULD remain under ~30 lines. A stub that grows beyond that is signaling it should become an authored draft — at which point it belongs in `docs/domains/archaeology/` (the parent), not here.

> [!TIP]
> The cleanest pattern is: **no per-file stubs at all.** List planned files in the Archaeology `CHANGELOG.md` "_not yet authored_" rows (the pattern established for the Agriculture dossier) and use this folder for the README alone — or retire the folder entirely. Per-file stubs are PROPOSED here only because the folder exists by request; the README does not claim they are doctrine.

[↑ Back to top](#contents)

---

## 4. What does NOT belong here

EXPLICIT deny list. The §15 contract treats "what does NOT belong" as load-bearing as "what does belong." For an archaeology subfolder, that list is broader and stricter than usual.

**Sensitivity-class deny (T4-inherited, ABSOLUTE):**

- ❌ Archaeological site coordinates, exact or generalized.
- ❌ Site names, codes, or identifiers tied to a real location.
- ❌ Human remains location, burial site, or sacred-site information.
- ❌ Oral history transcripts or cultural-knowledge notes.
- ❌ Sovereignty-sensitive material of any kind (treaty, tribal-relationship, repatriation context).
- ❌ Private landowner details, collection-security details, looting-risk exposure.
- ❌ Candidate features that have not cleared sovereignty review.
- ❌ Field-survey records, excavation records, provenience packets.
- ❌ Artifact / collection / repository records.
- ❌ Source-credential information (SHPO access tokens, lab-report credentials, etc.).
- ❌ Anything that, if leaked, would violate a `policy/sensitivity/archaeology/` rule.

**Authority-class deny:**

- ❌ Sensitivity-policy text (lives in `policy/sensitivity/archaeology/`).
- ❌ Object-family contract text (lives in `contracts/domains/archaeology/`).
- ❌ Schema files (live in `schemas/contracts/v1/domains/archaeology/` per the §12 lane pattern; the Atlas/ENCY `schemas/contracts/v1/archaeology/` shorthand is LINEAGE — the repo-wide `domains/`-segment decision is `OQ-CP-01` / ADR-S-01).
- ❌ Source descriptors (live in `data/registry/sources/archaeology/`).
- ❌ Release manifests, rollback cards, correction notices (live in `release/`).
- ❌ Verification-backlog items (live in `docs/domains/archaeology/VERIFICATION_BACKLOG.md` per-domain or `docs/registers/VERIFICATION_BACKLOG.md` cross-domain).
- ❌ Receipts of any kind (`RunReceipt`, `AIReceipt`, `GENERATED_RECEIPT.json`, `RedactionReceipt`, `AggregationReceipt`).

**Operational deny:**

- ❌ AI-drafted summaries of archaeological content, even abstracted.
- ❌ Commented-out content (commented sensitive material is still sensitive material).
- ❌ Filenames that themselves reveal site names or identifiers.
- ❌ Any content that would benefit from a Reality Boundary Note to render safely.

> [!CAUTION]
> If a contributor finds themselves writing a deny-listed item into a file here, the file does not belong in this folder. Stop, move the work to the proper responsibility root, and quarantine any in-progress draft per `policy/sensitivity/archaeology/` (PROPOSED). When in doubt, **abstain and route to the archaeology-domain steward**.

[↑ Back to top](#contents)

---

## 5. Inputs, outputs, validation, review burden (§15 contract)

| §15 field | Detail |
|---|---|
| **Inputs** | TODO references and "_not yet authored_" markers from sibling Archaeology dossier docs. No source-data inputs of any kind. No connector output. No AI-drafted archaeological content. |
| **Outputs** | Planning visibility only. Reviewers learn which dossier files are promised but not delivered. **No downstream consumer** (pipeline, governed-API route, catalog matrix, release manifest) reads from this folder. |
| **Validation** | (PROPOSED) `tests/domains/archaeology/test_missing_or_planned_files_no_t4_leak.py` — a content scan asserting that no file in this folder contains site coordinates, identifiers, sensitive geometry, or terms blacklisted by `policy/sensitivity/archaeology/`. Fail-closed: PR rejected at CI. |
| **Review burden** | Every PR touching this folder requires: docs steward + archaeology-domain steward + sovereignty-review liaison. PRs that add stub files require an explicit acknowledgement that the stub contains no archaeological content. AI-authored PRs additionally require AI surface steward review per contract §33. |
| **Related folders** | `docs/domains/archaeology/` (parent dossier), `docs/registers/` (cross-domain registers), `policy/sensitivity/archaeology/` (sensitivity enforcement), `data/quarantine/` (unresolved candidate material). |
| **ADRs governing this folder** | None yet accepted. ADR proposed for OQ-AR-MPF-01 (parallel-home question) and optionally OQ-AR-MPF-02 (naming convention). |
| **Last reviewed** | 2026-05-29. |

[↑ Back to top](#contents)

---

## 6. Relationship to existing planning surfaces

PROPOSED. The KFM doctrine stack already has planning surfaces. This folder, if retained, must not duplicate them.

```mermaid
flowchart TB
    NEED[A planned dossier file<br/>referenced from sibling docs]
    THIS[docs/domains/archaeology/<br/>missing_or_planned_files/<br/>← this folder]
    CHGL[docs/domains/archaeology/<br/>CHANGELOG.md<br/>_not yet authored_ rows]
    VBL[docs/domains/archaeology/<br/>VERIFICATION_BACKLOG.md<br/>NEEDS VERIFICATION items]
    XREG[docs/registers/<br/>VERIFICATION_BACKLOG.md<br/>cross-domain register]
    SENS[policy/sensitivity/<br/>archaeology/<br/>enforcement]

    NEED -.option A — this folder.-> THIS
    NEED -.option B — PREFERRED.-> CHGL
    NEED -.if checkable claim.-> VBL
    VBL -.rolls up to.-> XREG
    NEED -.never.-> SENS

    classDef self fill:#fff3e0,stroke:#e65100,stroke-width:1px,color:#000;
    classDef pref fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px,color:#000;
    classDef deny fill:#ffebee,stroke:#c62828,stroke-width:1px,color:#000;

    class THIS self;
    class CHGL pref;
    class SENS deny;
```

| Surface | Tracks | Why this folder is not a replacement |
|---|---|---|
| **`CHANGELOG.md` "_not yet authored_" rows** (preferred) | Files referenced as TODO across the dossier | Lighter, single-file, already established for the Agriculture dossier; no parallel-home concern. |
| **`VERIFICATION_BACKLOG.md`** (per-domain) | Items that NEEDS VERIFICATION | Tracks claims to verify, not files to write. Different object of trust. |
| **`docs/registers/VERIFICATION_BACKLOG.md`** | Cross-domain roll-up | Same as above, broader scope. |
| **`policy/sensitivity/archaeology/`** | Sensitivity enforcement | Authority, not planning. This folder never substitutes for policy. |

> [!IMPORTANT]
> The **preferred** path forward is to track not-yet-authored Archaeology dossier files as "_not yet authored_" rows in `docs/domains/archaeology/CHANGELOG.md` (mirroring the Agriculture dossier pattern), and to **retire this folder** once OQ-AR-MPF-01 is resolved. The folder is honored here because it was requested; the README does not pretend the folder is essential, and Directory Rules does not define it.

[↑ Back to top](#contents)

---

## 7. Sensitivity envelope (inherited)

The Archaeology domain's sensitivity envelope (CONFIRMED, Atlas v1.1 §24.5.2 + §24.14) flows into this folder unchanged:

| Object class | Default tier | Allowed transforms | Required gates |
|---|---|---|---|
| Archaeological site location | **T4** (T1 generalized only after steward review, Atlas §24.14) | Steward + cultural review + generalized geometry (coarse cell) + `RedactionReceipt` → T2 / T1. | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`. |
| Human remains / sacred sites | **T4 forever** | No transform releases this to T0; T3 only under explicit named authorization. | Sovereignty review + `ReviewRecord` + `PolicyDecision`. |
| Oral history / cultural knowledge | **Source-rights NEEDS VERIFICATION; sensitive joins fail closed** (Atlas v1.0 Ch. 15 §D / DOM-ARCH §D). | Per source rights; default deny. | Source-rights review + steward review. |
| Private landowner / collection-security details | **T4** | None permit public release without policy + steward review. | `PolicyDecision` + `ReviewRecord`. |
| `CandidateFeature` (not yet promoted) | Held in WORK / QUARANTINE | Not public; promotion requires review. | Promotion gate; no PUBLISHED edge to WORK / QUARANTINE. |

This folder participates in the envelope by hosting **none of the above**. It is a planning index. The envelope is named here so reviewers and contributors know what they are committing to keep out.

> [!CAUTION]
> Even in a benign planning folder, the deny boundary holds: **KFM is never an aggregator of site locations, even in draft folders**. The cross-cutting principle that no display surface is sovereign truth (Atlas §23.4) has a sensitivity corollary — no convenience folder is a sensitivity exception.

[↑ Back to top](#contents)

---

## 8. Open questions register

PROPOSED. Questions about this folder, distinct from Archaeology-domain verification items.

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| **OQ-AR-MPF-01** | Does `docs/domains/<domain>/missing_or_planned_files/` create a **parallel registry/planning home** under Directory Rules §2.4(5)? It does — §2.4(5) makes "a new parallel home or split" ADR-class (cf. ADR-S-03). Preferred-path question: should the ADR **retire** the folder in favor of the `CHANGELOG.md` "_not yet authored_" rows pattern, rather than legitimize it? | Docs steward + Directory-Rules editor + archaeology-domain steward | ADR; default recommendation is retire-and-use-CHANGELOG. Adoption beyond this placement requires the ADR first. |
| **OQ-AR-MPF-02** | If retained, should the folder be renamed `missing-or-planned-files/` (lowercase-with-hyphens) to match the multi-word folder convention (`roads-rail-trade/`, `people-dna-land/`)? `missing_or_planned_files` (underscores) does not match Directory Rules §6.1's documented conventions. | Docs steward | Routine rename in the same PR sequence as OQ-AR-MPF-01 if folder is retained. |
| **OQ-AR-MPF-03** | Should the **planned-file stub** pattern (PROPOSED in §3) be canonized or rejected? Per-file stubs are easy to misuse as drafts; a single index inside this README — or the `CHANGELOG.md` rows — may suffice. | Docs steward + archaeology-domain steward | Convention decision; codify in this README or in `docs/doctrine/` if generalized. |
| **OQ-AR-MPF-04** | If this folder is generalized across all domains (`docs/domains/<domain>/missing_or_planned_files/`), what is the minimum sensitivity envelope each domain inherits? Archaeology, Fauna, Flora, People/DNA, Settlements/Infrastructure-critical assets, and Hazards all carry T4 lanes — each needs its own deny list. | Docs steward + each domain steward | ADR; produce a template README per domain. |
| **OQ-AR-MPF-05** | Should the validator `tests/domains/archaeology/test_missing_or_planned_files_no_t4_leak.py` (PROPOSED §5) be a **repo-wide** scanner across all dossier subfolders, or stay domain-scoped? | Docs steward + policy steward | ADR if cross-domain. |
| **OQ-AR-MPF-06** | Does an idea-intake surface (the doc previously referenced `docs/intake/NEW_IDEAS_INDEX.md`) actually exist in the doctrine stack? It is **not verified** in the current corpus. If no canonical intake home exists, this folder must not be justified by analogy to one. | Docs steward | Confirm against mounted repo / doctrine index; if absent, drop the reference. |

[↑ Back to top](#contents)

---

## 9. Open verification backlog

PROPOSED. Items that remain `NEEDS VERIFICATION` for this file (and this folder) before promotion from `draft` to `published`.

1. Confirm placement at `docs/domains/archaeology/missing_or_planned_files/README.md` exists (or land it there) — **and** that OQ-AR-MPF-01's ADR has at least been filed, since the folder is ADR-class per §2.4(5).
2. Confirm `docs/domains/archaeology/README.md` exists and references this folder; if it does not, that absence is a gap, not drift.
3. Confirm `docs/domains/archaeology/CHANGELOG.md` (PROPOSED, parallel to the Agriculture pattern) is the **preferred** alternative — i.e., that adopting the "_not yet authored_" row pattern there would supersede this folder's purpose.
4. Confirm the PROPOSED validator (`test_missing_or_planned_files_no_t4_leak.py`) is feasible against `policy/sensitivity/archaeology/` term lists; if `policy/sensitivity/archaeology/` does not yet define a term list, defer to OQ-AR-MPF-01 / OQ-AR-MPF-05.
5. Confirm `archaeology-steward`, `docs-steward`, `sovereignty-review-liaison`, and `policy-steward` are roles defined in `CODEOWNERS` (or equivalent).
6. Confirm `GENERATED_RECEIPT.json` for this file's authorship is emitted at merge and references `CONTRACT_VERSION = "3.0.0"` (contract §34, §34.4 well-formedness gates).
7. Confirm any in-flight or accidentally-committed stub files in this folder pass the deny list in §4. If not, quarantine immediately.
8. Confirm whether a canonical idea-intake surface exists (OQ-AR-MPF-06); if not, remove the analogy.

[↑ Back to top](#contents)

---

## 10. Definition of done

This README (and the folder it documents) is done enough to enter the repository when:

- the folder is placed at `docs/domains/archaeology/missing_or_planned_files/` per Directory Rules §4 Step 3, **with this README at its root** — **but only after** OQ-AR-MPF-01's ADR is at least filed, since §2.4(5) makes the folder ADR-class;
- a docs steward, the archaeology-domain steward, the policy steward, and a sovereignty-review liaison have reviewed and approved it;
- it is linked from `docs/domains/archaeology/README.md` (when authored) and from any sibling doc that references planned dossier files;
- **OQ-AR-MPF-01 has at minimum been filed as a PROPOSED ADR** — the folder MUST NOT land without the ADR being open, and the ADR's default recommendation is retire-and-use-`CHANGELOG.md`;
- any conflict between this folder and the preferred `CHANGELOG.md` "_not yet authored_" row pattern is logged in `docs/registers/DRIFT_REGISTER.md`;
- the PROPOSED validator from §5 is at least planned (a `tests/domains/archaeology/` issue exists, even if the test is not yet written);
- the `GENERATED_RECEIPT.json` planned for AI authorship is wired into CI per contract §34 with `CONTRACT_VERSION = "3.0.0"`;
- no file in the folder, including this README, contains any T4-class archaeological content per §4;
- future changes follow contract §37 lifecycle.

[↑ Back to top](#contents)

---

## 11. Related docs and ADRs

PROPOSED links. All paths are PROPOSED until verified against a mounted repo.

- [`docs/doctrine/ai-build-operating-contract.md`](../../../doctrine/ai-build-operating-contract.md) — _TODO_ — operating contract v3.0; `CONTRACT_VERSION = "3.0.0"`; §§33, 34, 37.
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — _TODO_ — placement, ADR triggers (§2.4, esp. §2.4(5) parallel home), §15 per-folder README contract.
- [`../README.md`](../README.md) — _TODO_ — Archaeology domain README (existence NEEDS VERIFICATION).
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md) — Archaeology domain architecture (sibling, authored).
- [`../VERIFICATION_BACKLOG.md`](../VERIFICATION_BACKLOG.md) — _TODO_ — Archaeology verification backlog (per-domain).
- [`../CHANGELOG.md`](../CHANGELOG.md) — _TODO_ — Archaeology dossier changelog (PROPOSED; **preferred** home for "_not yet authored_" rows).
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../../registers/VERIFICATION_BACKLOG.md) — _TODO_ — cross-domain register.
- [`docs/registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md) — _TODO_ — drift between this folder and the preferred pattern (when applicable).
- [`docs/adr/README.md`](../../../adr/README.md) — _TODO_ — ADR index; OQ-AR-MPF-01 and OQ-AR-MPF-02 to be filed here.
- [`policy/sensitivity/archaeology/`](../../../../policy/sensitivity/archaeology/) — _TODO_ — sensitivity enforcement (canonical per Atlas v1.1 §24.13).

**ADRs governing this folder (when filed):**

- ADR-PROPOSED — Parallel-home question for per-domain `missing_or_planned_files/` subfolders (OQ-AR-MPF-01); default recommendation is retire-and-use-`CHANGELOG.md`.
- ADR-PROPOSED — Per-domain sensitivity-aware planning-subfolder template, if generalized (OQ-AR-MPF-04).

---

> [!NOTE]
> **Last updated:** 2026-05-29 · **Edition:** v1.1 draft · **`CONTRACT_VERSION = "3.0.0"`** · **Folder class:** domain-internal subfolder (PROPOSED; not a Directory-Rules construct) · **Sensitivity:** T4 inherited · **Authority:** Directory Rules §15 per-folder README contract; §2.4(5) ADR trigger.

[↑ Back to top](#contents)
