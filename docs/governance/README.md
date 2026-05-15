<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-docs-governance-readme
title: KFM Governance — Roles, Review Burden, and Separation of Duties
type: standard
version: v1
status: draft
owners: Docs steward (lead); subsystem owners (review); TODO named individuals
created: TODO-YYYY-MM-DD
updated: 2026-05-15
policy_label: public
related: [docs/doctrine/directory-rules.md, docs/adr/, docs/registers/AUTHORITY_LADDER.md, docs/registers/DRIFT_REGISTER.md, control_plane/, release/]
tags: [kfm, governance, roles, review-burden, separation-of-duties]
notes: [Updated from attached README baseline; current repo implementation depth and tooling enforcement remain UNKNOWN until mounted-repo evidence is inspected.]
[/KFM_META_BLOCK_V2] -->

# 🧭 KFM Governance — Roles, Review Burden, and Separation of Duties

> Human-facing home for the **people side** of KFM governance: who owns what, when an
> author may also approve their own work, and where separation of duties is required
> before a claim becomes public.

<p>
  <img alt="status" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="authority" src="https://img.shields.io/badge/authority-governance--bearing-blue">
  <img alt="truth posture" src="https://img.shields.io/badge/truth%20posture-CONFIRMED%20doctrine%20%2F%20UNKNOWN%20enforcement-6E40C9">
  <img alt="open ADRs" src="https://img.shields.io/badge/open%20ADRs-ADR--S--09-orange">
  <img alt="last reviewed" src="https://img.shields.io/badge/last%20reviewed-2026--05--12-lightgrey">
  <img alt="last updated" src="https://img.shields.io/badge/last%20updated-2026--05--15-lightgrey">
</p>

| Field | Value |
|---|---|
| **Target path** | `docs/governance/README.md` |
| **Document type** | README-like governance doc |
| **Authority level** | Governance-bearing placement under `docs/`; current repo presence `NEEDS VERIFICATION` |
| **Truth posture** | `CONFIRMED` doctrine / `PROPOSED` role-scope expansion / `UNKNOWN` tooling enforcement |
| **Status** | `PROPOSED` — doctrine CONFIRMED; folder contents, owners, CODEOWNERS path, and workflow gates `NEEDS VERIFICATION` |
| **Owners** | Docs steward (lead) · subsystem owners (review) · `TODO` named individuals |
| **Last reviewed** | 2026-05-12 |
| **Last updated** | 2026-05-15 |

> [!IMPORTANT]
> This README defines the **expected human governance posture** for roles, review burden,
> and separation of duties. It is not proof that CODEOWNERS, branch protections,
> release-manifest checks, or policy-bundle gates currently enforce that posture. Treat
> enforcement as `UNKNOWN` until current repo files, workflows, branch rules, and emitted
> release evidence are inspected.

---

## Contents

- [1. Purpose](#1-purpose)
- [2. Authority level and status](#2-authority-level-and-status)
- [3. Scope and repo fit](#3-scope-and-repo-fit)
- [4. Role topology](#4-role-topology-diagram)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does NOT belong here](#6-what-does-not-belong-here)
- [7. Directory layout (PROPOSED)](#7-directory-layout-proposed)
- [8. The eight roles](#8-the-eight-roles)
- [9. Separation-of-duties matrix](#9-separation-of-duties-matrix)
- [10. Maturity progression — when separation tightens](#10-maturity-progression--when-separation-tightens)
- [11. Validation](#11-validation)
- [12. Review burden and CODEOWNERS](#12-review-burden-and-codeowners)
- [13. Anti-patterns](#13-anti-patterns)
- [14. Related folders and docs](#14-related-folders-and-docs)
- [15. Open ADRs that affect this folder](#15-open-adrs-that-affect-this-folder)
- [16. FAQ](#16-faq)
- [17. Last reviewed](#17-last-reviewed)

---

## 1. Purpose

This folder is the **human-facing operating manual for KFM governance roles**. It names
people-shaped responsibilities that the rest of the system relies on — admission,
review, release, correction, rollback, and AI-surface stewardship — and describes when
separation of duties is required before a claim or artifact is treated as public.

> `CONFIRMED` doctrine (KFM operating-law invariant 9): *KFM separates policy-significant
> release duties when maturity justifies it.* The rules in this folder operationalize
> that invariant without claiming that enforcement is already wired.

Specifically, `docs/governance/` answers four recurring questions:

1. **Who owns this kind of decision?** For example, admission of a new source, release
   of a sensitive layer, approval of a `CorrectionNotice`, or review of an AI template.
2. **When is the author allowed to also approve?**
3. **When must a separate reviewer sign off — and which reviewer?**
4. **When is review enforced by tooling vs. by custom?** See open ADR-S-09.

`docs/governance/` does **not** own doctrine itself, directory rules, machine-readable
registers, schemas, policy code, or release objects. Those live in their own roots — see
[§14](#14-related-folders-and-docs).

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 2. Authority level and status

| Field | Value | Basis |
|---|---|---|
| **Authority class** | Governance-bearing README under `docs/` | Directory Rules place governance prose under the docs control plane; current mounted-repo presence remains `NEEDS VERIFICATION`. |
| **Doctrine label** | `CONFIRMED` | KFM operating law requires separation of policy-significant release duties when maturity justifies it. |
| **Roles list** | `PROPOSED` scope statements | The role catalog is a reference for ADR discussion until role homes and owner mappings are verified. |
| **Separation-of-duties matrix** | `PROPOSED` reference matrix | The matrix states expected posture; it is not yet verified as tooling-enforced. |
| **Enforcement maturity** | `UNKNOWN` | No mounted-repo evidence in this update proves CODEOWNERS, branch protections, release workflows, or policy gates enforce the matrix. |
| **Commit readiness** | `NEEDS VERIFICATION` | Relative links, named owners, CODEOWNERS location, and ADR statuses should be checked in the real checkout before merge. |

> [!IMPORTANT]
> The **doctrine** in this folder is settled. The **enforcement** is not. Until ADR-S-09
> records the tooling threshold and repo evidence confirms implementation, this folder
> describes the *expected* posture, not a verified runtime guarantee. Do not cite this
> README as proof that separation of duties is mechanically blocked at PR or release time.

---

## 3. Scope and repo fit

**Repo fit (Directory Rules basis; current repo presence `NEEDS VERIFICATION`):**

```text
docs/
├── README.md
├── doctrine/        ← operating law, lifecycle law, trust membrane, authority ladder
├── architecture/    ← system context, deployment topology, governed API, map shell
├── adr/             ← architectural decision records (including ADR-S-09 reviewer separation)
├── domains/         ← per-domain dossiers
├── sources/         ← source descriptor standards, source families
├── standards/       ← external standards KFM conforms to (STAC, DCAT, PROV, …)
├── runbooks/        ← ops procedures, rollback drills
├── security/        ← threat model, exposure posture
├── governance/      ← ← YOU ARE HERE: roles, review burden, separation of duties
├── registers/       ← AUTHORITY_LADDER, DRIFT_REGISTER, VERIFICATION_BACKLOG, …
├── intake/          ← IDEA_INTAKE, NEW_IDEAS_INDEX
├── archive/         ← lineage/, exploratory/, deprecated/
├── reports/         ← generated review/release reports (read-only)
└── brand/           ← style guide, logo, voice (only if not in packages/ui/)
```

**Input / output contract:**

| Direction | Reads or writes | Notes |
|---|---|---|
| **Reads from** | `docs/doctrine/`, `docs/adr/`, `docs/registers/AUTHORITY_LADDER.md`, per-domain dossiers, sensitivity policy, release doctrine | This folder applies doctrine and accepted decisions; it does not create them. |
| **Writes / defines** | Human-readable role definitions, review burden expectations, separation-of-duties posture, CODEOWNERS-policy rationale, escalation notes | These are prose governance controls until machine registers and enforcement gates are verified. |
| **Downstream consumers** | PR reviewers, release authorities, sensitivity reviewers, rights-holder representatives, CODEOWNERS authors, drift triage, release-manifest validators | Consumers may cite this README for expected posture, but not as evidence of tooling enforcement. |
| **Machine-readable counterparts** | `control_plane/` role and policy-gate registers; `release/` manifests; `policy/` gates | `PROPOSED` until actual paths and schemas are verified. |

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 4. Role topology (diagram)

The diagram below names the eight roles and the lifecycle gates each role principally
acts on. It is a **responsibility map**, not a workflow. Roles may collaborate on a
single gate; the matrix in [§9](#9-separation-of-duties-matrix) names when more than one
must.

```mermaid
flowchart LR
  %% Roles
  SS["Source steward"]:::role
  DS["Domain steward"]:::role
  SR["Sensitivity reviewer"]:::role
  RR["Rights-holder representative"]:::role
  RA["Release authority"]:::role
  CR["Correction reviewer"]:::role
  AS["AI surface steward"]:::role
  DOCS["Docs steward"]:::role

  %% Lifecycle gates
  G1((Admission)):::gate
  G2((Normalization)):::gate
  G3((Validation)):::gate
  G4((Catalog / Triplet)):::gate
  G5((Release)):::gate
  G6((Correction / Rollback)):::gate
  FOCUS([Focus Mode / AIReceipt]):::ai
  ATLAS([Atlas · ADR · Drift Register]):::doc

  SS --> G1
  RR --> G1
  DS --> G2
  DS --> G3
  SR --> G2
  SR --> G3
  DS --> G4
  RA --> G5
  SR --> G5
  RR --> G5
  CR --> G6
  RA --> G6
  AS --> FOCUS
  DOCS --> ATLAS
  DOCS -. periodic audit .-> G3

  classDef role fill:#EEF2FF,stroke:#4F46E5,color:#312E81;
  classDef gate fill:#FEF3C7,stroke:#B45309,color:#78350F;
  classDef ai   fill:#ECFEFF,stroke:#0891B2,color:#155E75;
  classDef doc  fill:#F0FDF4,stroke:#15803D,color:#14532D;
```

> [!NOTE]
> `PROPOSED`: the diagram reflects the current role topology in the attached README
> baseline. It should be regenerated from the machine-readable role register in
> `control_plane/` once that register lands and ADR-S-09 is accepted.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 5. What belongs here

Files in `docs/governance/` describe **who is accountable for which governance action**,
in prose that humans can read in a PR. Accepted content:

- **Role definitions** — one file per role or one consolidated `roles.md`, expanding the
  role catalog with KFM-specific scope notes.
- **Separation-of-duties policy** — when the author may also approve, when not, and which
  reviewer must sign.
- **Review burden tables** — per-action lists of required reviewers, expected receipts,
  and the failure-closed outcome when review is missing.
- **CODEOWNERS policy notes** — *not* the `CODEOWNERS` file itself, but the rationale for
  ownership assignments and the mapping from roles defined here to CODEOWNERS entries.
- **Escalation paths** — what happens when a reviewer is unavailable, conflicted, or the
  lane is sensitive enough to require a rights-holder representative.
- **Maturity thresholds** — at what point separation must move from custom to tooling.
- **Linkouts** to the doctrine, ADRs, registers, and policy gates that make these rules
  normative.

> [!TIP]
> If a file becomes primarily machine-readable, move it out of this prose folder and into
> the appropriate governance root (`control_plane/`, `policy/`, `release/`, or
> `schemas/`) through the Directory Rules and ADR process.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 6. What does NOT belong here

> [!WARNING]
> Putting any of the following here is a placement violation and a drift candidate.

| Content | Correct home | Why not here |
|---|---|---|
| Operating-law statements, lifecycle law, trust-membrane definition | `docs/doctrine/` | This folder *applies* doctrine; it does not author it. |
| Directory Rules authority decisions | `docs/doctrine/directory-rules.md` | Directory doctrine has its own canonical home. |
| Architectural decision records, including ADR-S-09 | `docs/adr/` | ADRs have their own lifecycle and template. |
| Machine-readable role / owner registers | `control_plane/` (for example, `policy_gate_register.yaml`) | Structured registers belong in the machine-readable governance layer, not prose. |
| Threat model, exposure posture, incident response | `docs/security/` | Security is a peer governance root, not a child of this folder. |
| Drift register entries, verification backlog | `docs/registers/` | Registers track state; this folder defines roles. |
| The `CODEOWNERS` file itself | repo root or `.github/CODEOWNERS` (`NEEDS VERIFICATION`) | This folder may describe CODEOWNERS policy; it does not host the file. |
| Per-PR review checklists for code | `.github/PULL_REQUEST_TEMPLATE/` (`NEEDS VERIFICATION`) | Workflow templates live with GitHub config. |
| Per-domain role assignments | `docs/domains/<domain>/` under that domain's review section | Domain dossiers own their own steward names and lane-specific review posture. |

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 7. Directory layout (PROPOSED)

> [!NOTE]
> `PROPOSED` tree. Directory Rules support this folder as a governance-bearing docs
> sub-root, but the *contents* below are inferred from the folder's stated purpose
> (roles, review burden, separation of duties). They are `NEEDS VERIFICATION` until
> mounted-repo evidence confirms which files actually exist.

```text
docs/governance/
├── README.md                       ← this file
├── roles.md                        ← PROPOSED: expanded definitions for the 8 roles
├── separation-of-duties.md         ← PROPOSED: action-by-action matrix; machine parity source
├── review-burden.md                ← PROPOSED: required reviewers + receipts per action
├── codeowners-policy.md            ← PROPOSED: rationale for CODEOWNERS mapping
├── escalation.md                   ← PROPOSED: unavailable / conflicted reviewer paths
├── maturity-thresholds.md          ← PROPOSED: when separation tightens; pre-ADR-S-09 notes
└── reviewer-rotation/              ← PROPOSED: optional cadence notes; not steward-of-record
```

Any file added under `docs/governance/` MUST satisfy the per-root README contract in
Directory Rules: purpose, authority level, status, what belongs here, what does not
belong here, inputs, outputs, validation, review burden, related folders, ADRs, and last
reviewed. A folder without a conforming README is a drift candidate.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 8. The eight roles

The role catalog below is `CONFIRMED` as the governing role set in this README baseline.
The individual role *scope statements* are `PROPOSED` pending ADR-S-09, owner mapping,
and per-role expansion in the files listed in [§7](#7-directory-layout-proposed).

| # | Role | Owns | Principal scope |
|:-:|---|---|---|
| 1 | **Source steward** | Admission, rights confirmation, source terms, and sensitivity tagging for a named source family. | `SourceDescriptor` lifecycle; source edge → RAW admission posture. |
| 2 | **Domain steward** | Meaning, contracts, schemas, fixtures, and validators of a domain's object families. | Domain semantics; validator authorship; review of domain-internal promotion candidates. |
| 3 | **Sensitivity reviewer** | Redaction, generalization, withholding, delayed release, and tier decisions for sensitive content. | `RedactionReceipt`; public-safe transformations; sensitive-lane release posture. |
| 4 | **Rights-holder representative** | Sovereignty, cultural-heritage, consent-based, living-person, and DNA-related release decisions. | Rights and consent checks for sensitive, sovereign, cultural, living-person, and restricted data. |
| 5 | **Release authority** | `ReleaseManifest`, release decision, and rollback authorization. | PUBLISHED transitions; material release approval; rollback authorization; author separation when required. |
| 6 | **Correction reviewer** | `CorrectionNotice` / `RollbackCard` review before a PUBLISHED claim is amended. | Post-publication corrections; rollback scope; derivative invalidation review. |
| 7 | **AI surface steward** | Focus Mode templates, `AIReceipt` sampling, policy bindings, and cite-or-abstain audits. | AI behavior vs. doctrine; prompt/template changes; bounded-answer review. |
| 8 | **Docs steward** | Governance documentation, ADR index, drift register, Atlas / supplement integrity. | The `docs/` tree; ADR index; `docs/registers/DRIFT_REGISTER.md`; documentation-control audits. |

> [!TIP]
> A single person MAY hold multiple roles in early-stage operation. The matrix in
> [§9](#9-separation-of-duties-matrix) controls when that is acceptable — not the role
> definitions themselves.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 9. Separation-of-duties matrix

`PROPOSED` reference matrix; enforcement maturity is `UNKNOWN` pending ADR-S-09 and
current repo verification.

| Action | May author also approve? | Required separation | Missing-review outcome |
|---|---|---|---|
| Source admission (source edge → RAW) | **Yes** for routine; **No** when source has unresolved rights, sovereignty, or sensitivity. | Source steward + rights-holder representative where applicable. | Hold at admission; do not enter RAW if rights or sensitivity are unresolved. |
| Normalization receipts | **Yes** for routine; **No** when transforms are sensitivity-relevant. | Domain steward; sensitivity reviewer if sensitivity-relevant. | Keep in WORK or QUARANTINE; no processed artifact. |
| Validator authorship and run | **Yes** for deterministic validators. | Domain steward; periodic audit by docs steward. | Validator can run, but audit backlog remains open. |
| Promotion to PROCESSED / CATALOG | **Yes** for non-sensitive routine; **No** for sensitive lanes. | Domain steward + sensitivity reviewer for sensitive lanes. | No promotion; retain rollback target and validation report. |
| Release to PUBLISHED | **No** when materiality applies. | Author ≠ release authority; rights-holder representative where applicable. | DENY release; no public surface update. |
| Sensitive-lane release | **No**. | Author + sensitivity reviewer + release authority + rights-holder representative. | DENY release; keep exact or sensitive material withheld. |
| Correction / rollback | **No** when correction is steward-significant. | Author / detector + correction reviewer + release authority. | Hold correction; do not republish until derivative invalidation is reviewed. |
| AI surface change (template / policy binding) | **No**. | AI surface steward + docs steward for policy binding. | ABSTAIN or disable changed surface until review completes. |
| Atlas / supplement publication | **No**. | Docs steward + at least one subsystem owner. | Hold publication; retain prior version as current. |

> [!IMPORTANT]
> "Materiality" and "sensitivity-relevant" are not self-defined here. They resolve via
> the sensitivity tier scheme and the per-domain rules in `docs/domains/<domain>/`. When
> in doubt, **escalate to a separate reviewer**. The fail-safe default is more separation,
> not less.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 10. Maturity progression — when separation tightens

> [!NOTE]
> `CONFIRMED` doctrine: separation of duties is maturity-dependent. Early-stage doctrine
> work may be authored and approved by the same actor when materiality is low. As
> maturity rises and the public trust surface expands, separation must move into tooling,
> not custom.

The intended progression:

1. **Pre-public stage.** Author = approver permitted for non-sensitive, low-materiality
   doctrine and internal review work. The matrix is aspirational and cited in PR notes.
2. **Early public surface.** Matrix becomes a PR-time custom: reviewers cite this README
   when refusing self-approval on sensitive lanes. Tooling may route review but does not
   yet prove separation.
3. **Mature public surface.** Separation moves into tooling — CODEOWNERS, branch
   protections, required-reviewer workflows, policy-bundle checks, and release-manifest
   checks that fail closed when a required role is missing.

The threshold between stages 2 and 3 is the subject of **open ADR-S-09** (*Reviewer
role separation: when is separation enforced by tooling vs. custom*). Until ADR-S-09 is
accepted and repo evidence confirms enforcement, this README does **not** claim that any
tooling enforces the matrix.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 11. Validation

> [!NOTE]
> `PROPOSED` validation strategy. None of the validators below has been verified as
> present, wired, or passing in mounted-repo evidence in this update.

| Check | What it would validate | Status | Failure posture |
|---|---|---|---|
| README contract check | Every file under `docs/governance/` has a conforming README or is covered by this README. | `PROPOSED` | Flag drift; do not treat orphan prose as authority. |
| Meta-block check | KFM Meta Block v2 exists and `updated` is current. | `PROPOSED` | Flag documentation-control drift. |
| Role-name vocabulary lint | Role names used elsewhere in `docs/` match the eight names in [§8](#8-the-eight-roles). | `PROPOSED` | Flag term drift before merge. |
| Separation-of-duties register parity | Machine-readable matrix in `control_plane/` matches the prose matrix here. | `PROPOSED` (depends on register existing) | Fail closed on release gates if mismatch is material. |
| CODEOWNERS ↔ role mapping check | Every role named here resolves to at least one CODEOWNERS path / team. | `PROPOSED` | Review routing remains `UNKNOWN`; require manual reviewer assignment. |
| Release-manifest required-reviewer check | A `ReleaseManifest` for a sensitive lane carries reviewer references in all required roles. | `PROPOSED` (release tooling not verified) | DENY release. |
| ADR-S-09 acceptance check | ADR-S-09 has reached `status: accepted` and this README links to it. | `PROPOSED` (ADR-S-09 currently open) | Keep tooling-enforcement claims out of this README. |
| Relative-link check | Links in [§14](#14-related-folders-and-docs) resolve from `docs/governance/README.md`. | `NEEDS VERIFICATION` | Leave link target as TODO / NEEDS VERIFICATION. |

**Pre-merge verification checklist:**

- [ ] Confirm `docs/governance/README.md` exists in the mounted repo or create it through an ADR-backed placement path.
- [ ] Confirm named owners or keep `TODO` placeholders visible.
- [ ] Confirm the actual CODEOWNERS path (`CODEOWNERS` vs `.github/CODEOWNERS`).
- [ ] Confirm ADR-S-09 and related ADR IDs exist in `docs/adr/` or keep them `PROPOSED`.
- [ ] Confirm role names match any machine-readable role register in `control_plane/`.
- [ ] Confirm no public release path relies on this README instead of a governed release gate.
- [ ] Confirm relative links from this file resolve or are deliberately marked `NEEDS VERIFICATION`.

**Rollback path for this README:** revert the README change, restore the previous `Last updated`
value, and open or update a `DRIFT_REGISTER` entry if the rollback is caused by path-home,
owner, ADR, or enforcement conflicts. No release artifacts should need invalidation unless a
public release cited this README as enforcement proof.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 12. Review burden and CODEOWNERS

Review burden = the **minimum set of human approvals** a change must collect before
merging or releasing. This folder describes burden in two layers:

1. **Doc-level burden** (what this folder's own files need to merge): Docs steward
   review by default; sensitivity reviewer co-sign if a change touches sensitive-lane
   role scopes; release authority co-sign if a change weakens release-time separation.
2. **System-level burden** (what changes elsewhere need, by role): captured in the
   matrix in [§9](#9-separation-of-duties-matrix).

> [!CAUTION]
> `CODEOWNERS` is a GitHub mechanism; it expresses *who is auto-requested for review on
> a path*. It does **not** by itself enforce separation of duties — an author with commit
> access can still self-merge unless branch protections require approvals from someone
> other than the author. Treat CODEOWNERS as a **routing tool**, not as a trust-membrane
> control. Tooling-enforced separation requires branch protections, required-reviewer
> rules, and release-manifest checks *in addition to* CODEOWNERS.

`PROPOSED` CODEOWNERS-policy mapping (to be specified in `codeowners-policy.md`):

| Path pattern | Required reviewer role(s) | Status |
|---|---|---|
| `docs/governance/**` | Docs steward | `PROPOSED` |
| `docs/doctrine/**` | Docs steward + accepted-ADR reference | `PROPOSED` |
| `docs/adr/**` | Docs steward + at least one subsystem owner | `PROPOSED` |
| `release/manifests/**` | Release authority (+ rights-holder representative for sovereign lanes) | `PROPOSED` |
| `policy/sensitivity/**` | Sensitivity reviewer + release authority | `PROPOSED` |
| `apps/governed-api/**` | Subsystem owner + docs steward for any policy-binding change | `PROPOSED` / path `NEEDS VERIFICATION` |
| `runtime/model_adapters/**`, `apps/governed-api/src/ai/**` | AI surface steward | `PROPOSED` / paths `NEEDS VERIFICATION` |

A CODEOWNERS-policy entry SHOULD record:

- the path pattern;
- the role being routed;
- the reviewer team or named owner (`TODO` until verified);
- the separation rule it supports;
- the fallback when the reviewer is unavailable;
- whether branch protection or release tooling enforces the separation.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 13. Anti-patterns

> [!WARNING]
> The following are governance-process anti-patterns. They are KFM-explicit, not generic.

- **Documenting a change instead of validating it.** Docs are part of the working system
  but never substitute for validators, fixtures, schemas, policies, or release gates.
- **Approving one's own release on a sensitive lane.** Matrix [§9](#9-separation-of-duties-matrix)
  requires release authority to be distinct from author when materiality applies.
- **Treating an Atlas summary or matrix as evidence.** Atlas, supplements, and master
  matrices are reference views; `EvidenceBundle` remains authoritative.
- **Silent migrations between role homes.** Moving role definitions out of
  `docs/governance/` without an ADR fragments authority and is a drift candidate.
- **Promotion that "upgrades" a source role** (for example, modeled → observed). Source
  role is fixed at admission; promotion does not transform source authority.
- **Re-publishing a corrected claim without invalidating derivatives.** A
  `CorrectionNotice` must list invalidated derivatives; use a `RollbackCard` when needed.
- **Using CODEOWNERS as a trust-membrane control.** See [§12](#12-review-burden-and-codeowners).
- **Letting AI review collapse author and approver.** AI can help surface evidence gaps;
  it cannot act as the separate human reviewer required by this matrix.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 14. Related folders and docs

| Folder / file | Why it's related | Status |
|---|---|---|
| `../doctrine/` | Operating law, lifecycle law, trust membrane, authority ladder — this folder operationalizes them. | `NEEDS VERIFICATION` link target |
| `../doctrine/directory-rules.md` | Authoritative placement and responsibility-root rules. | `NEEDS VERIFICATION` link target |
| `../adr/` | ADRs that affect role separation, most importantly ADR-S-09. | `NEEDS VERIFICATION` link target |
| `../registers/AUTHORITY_LADDER.md` | Authority ranking; reviewers cite this when sources disagree. | `TODO` link target |
| `../registers/DRIFT_REGISTER.md` | Where drift between this folder and repo state should be recorded. | `TODO` link target |
| `../registers/VERIFICATION_BACKLOG.md` | Open verification items including matrix-tooling parity. | `TODO` link target |
| `../security/` | Threat model and exposure posture; peer governance root. | `NEEDS VERIFICATION` link target |
| `../sources/SOURCE_DESCRIPTOR_STANDARD.md` | Source steward's authoring surface. | `TODO` link target |
| `../../control_plane/` | Machine-readable governance maps (role / policy-gate / release-state registers). | `PROPOSED` path |
| `../../release/` | Release decisions; release authority outputs and rollback targets. | `PROPOSED` path |
| Repo-root `CODEOWNERS` *or* `.github/CODEOWNERS` | The actual ownership routing file. | `NEEDS VERIFICATION` which path the repo uses |

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 15. Open ADRs that affect this folder

| ADR | Question | Why it matters here | Status |
|---|---|---|---|
| **ADR-S-09** | Reviewer role separation: when is separation enforced by tooling vs. custom? | Sets the threshold at which the matrix in [§9](#9-separation-of-duties-matrix) becomes a fail-closed tooling rule rather than a PR-time custom. | `PROPOSED` / open |
| ADR-S-04 | Source-role enum — canonical vocabulary, evolution rule. | The source steward's authoring vocabulary; affects role scope in [§8](#8-the-eight-roles). | `PROPOSED` / `NEEDS VERIFICATION` |
| ADR-S-05 | Sensitivity tier scheme (T0–T4) — adopt as canonical or revise. | Defines what "sensitivity-relevant" means in the matrix. | `PROPOSED` / `NEEDS VERIFICATION` |
| ADR-S-13 | Drift register triage — how often, by whom, with what outcome. | Names the docs steward's recurring duty for drift handling. | `PROPOSED` / `NEEDS VERIFICATION` |
| ADR-S-15 | Atlas / supplement lifecycle — cadence, deprecation, supersession. | Governs this folder's review cadence if Atlas / supplement material is used as reference. | `PROPOSED` / `NEEDS VERIFICATION` |

> [!NOTE]
> Identifiers `ADR-S-04 / 05 / 09 / 13 / 15` come from the attached README baseline's
> ADR backlog framing. They remain **PROPOSED** ADR titles until accepted ADRs are filed
> in `docs/adr/` and verified in the mounted repo.

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 16. FAQ

<details>
<summary><strong>Q: Can one person hold more than one role?</strong></summary>

Yes, especially in early-stage operation. The eight roles are **responsibilities**, not
job titles. The control that matters is not how many roles a person holds in the
abstract, but whether the [§9 matrix](#9-separation-of-duties-matrix) requires that a
*different* person sign off for a *specific action*. A single person who is both domain
steward and release authority MAY do routine non-sensitive work alone, but MAY NOT
self-approve a sensitive-lane release.

</details>

<details>
<summary><strong>Q: Where is the actual list of named owners?</strong></summary>

Named owners belong in the repo `CODEOWNERS` file and in per-domain
`docs/domains/<domain>/` dossiers in their review sections. This README intentionally
does **not** name people, so that it stays stable when staffing changes. `TODO`: link to
CODEOWNERS once its location is verified.

</details>

<details>
<summary><strong>Q: Why isn't this folder just CODEOWNERS plus a comment?</strong></summary>

CODEOWNERS is a routing tool. It says *who gets auto-requested for review on a path*.
It cannot express the four properties this folder must express:

1. Which **role** a reviewer is acting as.
2. When **multiple roles** must co-sign for one action.
3. When the **author** is forbidden from also approving.
4. When the **reviewer must be external** to the lane.

CODEOWNERS plus branch protections plus release-manifest reviewer checks can together
*enforce* the rules. This folder *defines* them.

</details>

<details>
<summary><strong>Q: How do we propose a change to the matrix?</strong></summary>

Open a PR against `docs/governance/separation-of-duties.md` (once created) **and** an
ADR in `docs/adr/`. A change to the matrix is by definition a separation-of-duties
change and therefore requires docs-steward review plus a subsystem owner. The PR
description SHOULD reference the affected matrix row, the proposed new row, the
materiality argument, and rollback impact.

</details>

<details>
<summary><strong>Q: What happens if a required reviewer is unavailable?</strong></summary>

`PROPOSED` (to be expanded in `escalation.md`): the action holds at its current
lifecycle gate and fails closed — no public surface change occurs. The release authority
MAY name a temporary alternate for non-sensitive routine work, but MAY NOT name a
temporary alternate for sensitive-lane release, rights-holder representation, or
correction/rollback. Sensitive lanes wait.

</details>

<details>
<summary><strong>Q: Is the AI surface steward responsible for what the AI says?</strong></summary>

The AI surface steward is responsible for the **templates, policy bindings, and audit
cadence** that bound what the AI can say — not for individual generated answers.
Individual answers are governed by Focus Mode's cite-or-abstain rule, the
`PolicyDecision` pre/post checks, and the `AIReceipt`. When AI behavior drifts from
doctrine (for example, uncited language or synthetic-as-observed presentation), the AI
surface steward opens the corrective ticket and co-signs the template or policy-binding
change with the docs steward.

</details>

<details>
<summary><strong>Q: What if the mounted repo does not match this directory plan?</strong></summary>

Do not silently conform this README to drift and call the drift canon. Record the
conflict in `docs/registers/DRIFT_REGISTER.md`, then resolve it through an ADR or a
migration plan. Until resolved, mark affected paths `PROPOSED` / `CONFLICTED` and avoid
creating parallel homes for roles, policies, release proofs, or machine-readable
registers.

</details>

[Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)

---

## 17. Last reviewed

| Field | Value |
|---|---|
| Last reviewed | **2026-05-12** |
| Last updated | **2026-05-15** |
| Next review due | 2026-11-12 (six-month review cadence; verify against Directory Rules before relying on this date) |
| Reviewed by | Docs steward (`TODO` named) |
| Updated by | ChatGPT update pass using attached Markdown baseline; not a substitute for docs-steward review |
| Reviewed against | Atlas / role catalog lineage; KFM operating law; Directory Rules placement and README-contract doctrine (`NEEDS VERIFICATION` in mounted repo) |
| Remaining blockers | Verify actual path, ADR-S-09 status, CODEOWNERS path, role-register parity, relative links, named owners, and enforcement workflows. |

**Last updated:** 2026-05-15 · [Back to top](#-kfm-governance--roles-review-burden-and-separation-of-duties)
