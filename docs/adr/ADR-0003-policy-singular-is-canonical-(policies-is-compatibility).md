<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0003-policy-singular-canonical
title: "ADR-0003 — `policy/` (singular) is canonical; `policies/` is compatibility"
type: standard
version: v1
status: proposed
owners: Governance steward · Architecture steward · Policy substrate owner (TODO confirm CODEOWNERS)
created: 2026-05-10
updated: 2026-05-10
policy_label: public
related:
  - docs/adr/ADR-0001-schema-home.md            # NEEDS VERIFICATION (path/title)
  - docs/adr/ADR-0002-*.md                       # NEEDS VERIFICATION (existence/title)
  - directory-rules.md
  - policy/README.md                              # PROPOSED to exist
  - policies/README.md                            # PROPOSED to exist (frozen-mirror class)
  - control_plane/deprecation_register.yaml       # PROPOSED, per Directory Rules §14.2
tags: [kfm, adr, governance, policy, directory-rules, compatibility-root]
notes:
  - "Resolves the NEEDS VERIFICATION item in directory-rules.md §18: ‘Whether policies/ or policy/ is canonical.’"
  - "Numbering (ADR-0003) is per user-supplied filename; repo ADR index NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# ADR-0003 — `policy/` (singular) is canonical; `policies/` is compatibility

**Pick one home for the OPA/Conftest/Rego policy substrate, freeze the other to a non-evolving compatibility mirror, and prevent the most common drift in KFM: two homes for the same authority.**

[![ADR](https://img.shields.io/badge/ADR-0003-1f6feb)](#)
[![Status: proposed](https://img.shields.io/badge/status-proposed-f0ad4e)](#1-status)
[![Doctrine: Directory Rules §5, §8, §13.5](https://img.shields.io/badge/doctrine-Directory%20Rules%20%C2%A75%20%C2%A78%20%C2%A713.5-6f42c1)](./directory-rules.md)
[![Supersedes: none](https://img.shields.io/badge/supersedes-none-lightgrey)](#)
[![Supersedes ADR](https://img.shields.io/badge/superseded%20by-none-lightgrey)](#)
[![Last updated](https://img.shields.io/badge/last%20updated-2026--05--10-informational)](#)

> [!IMPORTANT]
> **Status:** PROPOSED · **Owners:** Governance steward · Architecture steward · **Last updated:** 2026-05-10
> Acceptance gates this ADR: (a) `policy/README.md` declares **canonical**; (b) `policies/README.md` declares compatibility class `mirror` or `legacy`; (c) Path-Validation Checklist (`directory-rules.md` §16) updated to cite this ADR; (d) a `control_plane/deprecation_register.yaml` entry exists for `policies/` if it carries content.

---

## Contents

- [1. Status](#1-status)
- [2. Context](#2-context)
- [3. Decision](#3-decision)
- [4. Authority diagram](#4-authority-diagram)
- [5. Scope of `policy/` (what belongs, what does not)](#5-scope-of-policy-what-belongs-what-does-not)
- [6. Consequences](#6-consequences)
- [7. Alternatives considered](#7-alternatives-considered)
- [8. Migration plan](#8-migration-plan)
- [9. Rollback plan](#9-rollback-plan)
- [10. Validation](#10-validation)
- [11. Open questions and NEEDS VERIFICATION](#11-open-questions-and-needs-verification)
- [12. Related docs and references](#12-related-docs-and-references)
- [Appendix A — Proposed `policy/` subtree](#appendix-a--proposed-policy-subtree)
- [Appendix B — Reviewer checklist (mapped to Directory Rules §16)](#appendix-b--reviewer-checklist-mapped-to-directory-rules-16)

---

## 1. Status

| Field | Value |
|---|---|
| ADR ID | **ADR-0003** *(numbering NEEDS VERIFICATION against the live `docs/adr/` index)* |
| Status | **proposed** |
| Decision date | TBD on acceptance |
| Supersedes | _none_ |
| Superseded by | _none_ |
| Decision class | Compatibility root resolution (per `directory-rules.md` §2.4 / §8) |
| Migration class | Structural move (per `directory-rules.md` §14.2) |
| Authors / owners | Governance steward · Architecture steward · Policy substrate owner *(TODO confirm CODEOWNERS)* |
| Reviewers | Schema steward · Release steward · Documentation steward *(TODO confirm)* |

> [!NOTE]
> This ADR formalizes a default already stated in `directory-rules.md` §5 and §18:
> *"`policy/` — **Canonical (singular)** — If `policies/` exists, treat it as compatibility / mirror until ADR resolves."*
> The doctrine is settled in writing; what this ADR adds is the ratified decision, the migration plan, and the rollback path.

---

## 2. Context

KFM treats **policy as executable substrate**, not documentation. The corpus selects OPA + Conftest + Rego: policies live in version-controlled `.rego` files, and the Promotion Gate evaluates the full bundle on every promotion attempt. Every license rule, sensitivity classifier, consent block, obligation, and revocation rule is a `.rego` file or rule inside that bundle.

There is, however, a recurring ambiguity in KFM repositories about where that bundle lives. Two paths exist or can plausibly exist:

- **`policy/`** — singular, used throughout the doctrine and Idea Index when referring to the "policy bundle directory."
- **`policies/`** — plural, an entrenched convention from prior project iterations and from many third-party OPA examples.

`directory-rules.md` flags this directly in three places:

1. **§5 — Authority table.** `policy/` is listed as *"**Canonical (singular)** — If `policies/` exists, treat it as compatibility / mirror until ADR resolves."*
2. **§8.1 — Compatibility roots and their canonical homes.** `policies/` → canonical `policy/`, class default `mirror` or `legacy`, recommended action *"Pick canonical `policy/`; freeze writes to `policies/` and migrate."*
3. **§13.5 — Additional anti-patterns.** **Schema mirror divergence:** *"`schemas/` and `contracts/` (or `policies/` and `policy/`) evolve separately — One canonical, the other is a generated mirror or frozen legacy. ADR if unclear."*
4. **§18 — Open Questions / NEEDS VERIFICATION.** *"Whether `policies/` or `policy/` is canonical. Default is `policy/`; resolve by inspection."*

> [!WARNING]
> **The drift this ADR prevents is the most common in KFM.** From `directory-rules.md` §8.3: *"Two homes for the same authority is the most common drift in KFM. If both exist, the compatibility root MUST NOT evolve independently."*
> When two homes evolve independently, the Promotion Gate cannot identify "the" policy bundle, audits cannot identify which rule version produced a DENY, and `DecisionEnvelope` outcomes lose their reproducibility guarantee.

The forces in play:

| Force | Pull toward `policy/` | Pull toward `policies/` |
|---|---|---|
| KFM doctrine and Directory Rules §5 / §8.1 | ✅ named canonical singular | ❌ named compatibility root |
| KFM Idea Index — POL substrate references | ✅ "policy bundle directory (`policy/`)" | — |
| Generic OPA / Conftest tutorials and many third-party examples | — | ✅ "policies/" is a common convention |
| Operational reproducibility | ✅ one bundle, one decision log keying | ❌ ambiguous bundle on a Promotion Gate run |
| Migration cost if KFM had built on `policies/` | ❌ rename cost if widespread | ✅ no rename needed (status quo) |
| Mirror discipline (§8.3) — "compatibility MUST NOT evolve independently" | ✅ single canonical lane | ❌ encourages parallel authority |

KFM's invariants (`directory-rules.md` §3, §4, §13.5, §16) and the project's stated default (`directory-rules.md` §5, §18) point the same direction.

---

## 3. Decision

**`policy/` (singular) is the canonical home for the KFM policy substrate.**
**`policies/` (plural) is a compatibility root with class `mirror` or `legacy`.**

Concretely:

1. The OPA / Conftest / Rego bundle — consent, revocation, promotion, sensitivity, license, and obligation modules — lives at **`policy/`**.
2. The Promotion Gate, CI workflows, validators, and the gate orchestration script point at **`policy/`** as the single bundle root.
3. Where `policies/` exists in a given KFM repository:
   - It MUST carry a `README.md` per `directory-rules.md` §15 declaring class **`mirror`** (regenerated from `policy/`) or **`legacy`** (frozen pending removal).
   - It MUST NOT be edited directly.
   - It MUST NOT evolve independently (per `directory-rules.md` §8.3).
   - New rules, fields, and policy updates land in `policy/` first; mirrors regenerate or migrate.
4. Reviewers cite this ADR (ADR-0003) for any PR that touches either `policy/` or `policies/`, per `directory-rules.md` §16 ("Rule cited in PR description").

> [!TIP]
> **Mental model.** `policy/` is the executable substrate the Promotion Gate consumes. `policies/`, if it exists, is at best a printout — never a co-authority.

---

## 4. Authority diagram

```mermaid
flowchart LR
    subgraph CANON[policy/ — CANONICAL bundle]
        direction TB
        A[consent/*.rego]
        B[revocation/*.rego]
        C[promotion/*.rego]
        D[sensitivity/*.rego]
        E[license/*.rego]
        F[obligations/*.rego]
        T[tests/*.rego]
    end

    subgraph COMPAT[policies/ — COMPATIBILITY mirror or legacy]
        direction TB
        M["Frozen mirror<br/>(or empty after migration)"]
    end

    GATE["Promotion Gate<br/>(OPA + Conftest)"]
    DECISION["DecisionEnvelope<br/>(ALLOW / DENY / ABSTAIN / ERROR)"]

    CANON --> GATE
    GATE --> DECISION

    CANON -. "(regenerate; never reverse)" .-> COMPAT
    COMPAT -. "forbidden write path<br/>(§8.3)" .x CANON

    classDef canon fill:#1f6feb,stroke:#0b3d91,color:#ffffff;
    classDef compat fill:#f0ad4e,stroke:#a06b00,color:#1b1f23;
    classDef ops fill:#6f42c1,stroke:#3b1d6a,color:#ffffff;
    class CANON canon;
    class COMPAT compat;
    class GATE,DECISION ops;
```

> [!NOTE]
> **Diagram status:** the canonical lane is CONFIRMED by `directory-rules.md` §5, §8.1, and §13.5. The compatibility lane is CONFIRMED as policy doctrine, but whether `policies/` is currently present in the repo and what content it holds is **NEEDS VERIFICATION** (see §11).

---

## 5. Scope of `policy/` (what belongs, what does not)

The scope below is grounded in the KFM POL substrate doctrine and in the policy-bundle directory description in the Idea Index. Specific module names should be confirmed against the live `policy/` tree on acceptance.

| Belongs in `policy/` | Notes |
|---|---|
| `consent/` Rego modules | Consent-block evaluation; lawful-basis checks; expiration |
| `revocation/` Rego modules | `revoke_delta` propagation; revocation feed gates |
| `promotion/` Rego modules | Promotion Gate A–G rules; deny-by-default; explainable reason objects |
| `sensitivity/` Rego modules | Public / public-derived / restricted-aggregate / restricted-precise / internal / embargoed |
| `license/` Rego modules | License recognition; intersection rule for derivatives |
| `obligations/` Rego modules | Downstream-duty propagation |
| `tests/` | Conftest test patterns: label propagation, deny-by-default, required-fields |
| `README.md` | Per `directory-rules.md` §15 — canonical authority level |

| Does **NOT** belong in `policy/` | Lives in |
|---|---|
| Policy decision **outputs** (run receipts, DecisionEnvelope artifacts) | `data/receipts/`, `release/` |
| EvidenceBundle resolution code | `packages/evidence-resolver/` |
| Policy runtime evaluator code | `packages/policy-runtime/` |
| Validators that wrap policy outputs into CI assertions | `tools/validators/` |
| Domain-specific policy fixtures | `data/fixtures/<domain>/` or `tests/fixtures/` |
| Narrative documentation about policy intent | `docs/architecture/` |

---

## 6. Consequences

### 6.1 Positive

- **Single authority for executable policy.** Eliminates the most common KFM drift (Directory Rules §8.3, §13.5) for the policy lane.
- **Reproducible decisions.** Every DENY / ABSTAIN carries a structured reason tied to a rule in a single bundle; `DecisionEnvelope` records remain replayable.
- **Cleaner Promotion Gate wiring.** CI workflows, Conftest invocations, and gate orchestration scripts point at one path.
- **Tighter compatibility discipline.** `policies/`, where it exists, becomes a `mirror` or `legacy` class folder with an explicit README contract (Directory Rules §15) — no parallel evolution.
- **Reviewer leverage.** Path-Validation Checklist (Directory Rules §16) now has a concrete ADR citation for any PR touching either path.

### 6.2 Negative / costs

- **One-time migration.** Any content currently authoritative in `policies/` must be moved under `policy/` with a migration manifest (Directory Rules §14.2).
- **External convention friction.** Many third-party OPA examples use `policies/`; contributors may default to plural and need a reviewer redirect.
- **Tooling reconfiguration.** Conftest invocations, CI workflow paths, and editor settings that point at `policies/` must be updated.
- **Documentation churn.** Internal docs, READMEs, and example commands that reference `policies/` need an update pass.

### 6.3 Neutral

- No schema field changes — this is a path decision, not a contract change.
- No identity changes — policies still hash to the same `spec_hash` regardless of their on-disk root.
- No external API surface change — the public path remains the governed API (`apps/governed-api/`).

---

## 7. Alternatives considered

| Alternative | Pros | Cons | Outcome |
|---|---|---|---|
| **A. `policy/` canonical, `policies/` mirror/legacy** *(chosen)* | Aligns with `directory-rules.md` §5, §8.1, §18 default; matches KFM corpus language ("policy bundle directory `policy/`"); singular matches `schemas/` / `data/` / `release/` root style; mirror discipline simple. | One-time migration if `policies/` carries content. | **Selected.** |
| B. `policies/` canonical, `policy/` mirror/legacy | Matches common third-party OPA convention; reduces friction with contributors familiar with external examples. | Contradicts `directory-rules.md` §5 and §18 default; requires either revising Directory Rules or relabeling the canonical singular table entry; doesn't match KFM corpus terminology. | Rejected. Deviates from KFM doctrine without offsetting benefit. |
| C. Both paths allowed as parallel authorities | No migration cost; status quo if both currently exist. | Directly violates `directory-rules.md` §8.3 ("Compatibility roots are not parallel authority") and §13.5 (anti-pattern: schema mirror divergence). Promotion Gate must pick a bundle root at runtime; ambiguity breaks audit and replay. | Rejected. The drift this ADR exists to prevent. |
| D. Defer the decision | Zero immediate cost. | Leaves `directory-rules.md` §18 NEEDS VERIFICATION item open indefinitely; each PR re-litigates placement; drift accrues silently. | Rejected. The cost of deferring is precisely the cost an ADR is designed to retire. |

---

## 8. Migration plan

Per `directory-rules.md` §14.2 (structural moves):

1. **Inspect repo state.** Identify whether `policy/`, `policies/`, both, or neither currently exist; enumerate their contents. *Status: **NEEDS VERIFICATION** against the live workspace.*
2. **Open this ADR.** Reference it from any PR that touches either path.
3. **`git mv` content** from `policies/` to `policy/` preserving history. Use `git mv` so blame and history survive (`directory-rules.md` §14.1).
4. **Update references** in code, docs, schemas, fixtures, tests, workflows, and CI. Search targets include:
   - `conftest.toml` / `.conftest.toml`
   - `.github/workflows/*.yml` policy paths
   - `tools/validators/**`
   - `packages/policy-runtime/**`
   - `apps/governed-api/**`
   - `docs/**/*.md` cross-links
5. **Update `directory-rules.md`** — change §18 ("Whether `policies/` or `policy/` is canonical") from open question to resolved-by-ADR-0003, cite the ADR in §5 and §8.1.
6. **Add migration manifest** under `migrations/` listing every `policies/<path>` → `policy/<path>` mapping with `git_sha_before`, `git_sha_after` (Directory Rules §14.2 step 3).
7. **Add deprecation entry** in `control_plane/deprecation_register.yaml` for `policies/` with a sunset date (Directory Rules §14.2 step 5).
8. **Create `policies/README.md`** declaring class **`mirror`** (if regenerated for IDE/tooling convenience) or **`legacy`** (if frozen and slated for removal). The README MUST follow the §15 contract.
9. **Create / update `policy/README.md`** declaring authority level **canonical**, listing what belongs and what does not (per §5 above), and linking to this ADR.
10. **Verify rollback** with a dry-run rollback card before merge (Directory Rules §14.2 step 6).
11. **Run the validator suite** and verify no new drift entries open.
12. **Close the migration** by removing the `policies/` mirror only after the documented verification window passes (Directory Rules §14.2 step 7). If `policies/` is kept as a `mirror` indefinitely (e.g., for external-export reasons), no removal is required but the README class MUST remain accurate.

---

## 9. Rollback plan

If migration introduces regressions that block release:

1. Re-enable `policies/` as an editable path for the duration of the rollback window.
2. Revert the migration commit(s) with `git revert`, preserving history.
3. Emit a `rollback_receipt` per `directory-rules.md` §14.2 step 6.
4. Mark this ADR `superseded` and open ADR-XXXX with a revised plan (or defer with reasons).
5. Restore `directory-rules.md` §18 to its prior open-question wording until a replacement ADR lands.

> [!CAUTION]
> Rollback restores **path topology**, not deleted content. Any `policy/` content authored during the migration window MUST be carried forward in the rollback commit; otherwise the rollback loses material added during the window.

---

## 10. Validation

The decision is enforceable through evidence — not narrative.

| Validation surface | What it checks | Status |
|---|---|---|
| `policy/README.md` exists, declares **canonical** per §15 contract | Authority declared on disk | PROPOSED |
| `policies/README.md` exists (if folder exists), declares `mirror` or `legacy` per §15 | Compatibility declared on disk | PROPOSED |
| Path-Validation Checklist (`directory-rules.md` §16) entry references ADR-0003 | Reviewer leverage | PROPOSED |
| CI repository-shape validator: fail when `.rego` is added under `policies/` without a `mirror`-class README | Prevent parallel evolution | NEEDS VERIFICATION (proposed tool) |
| Promotion Gate config (`conftest.toml` or workflow input) points at `policy/` | Single bundle root | NEEDS VERIFICATION (current path) |
| `migrations/` manifest entry exists for any `policies/` → `policy/` move | Migration discipline (§14.2 step 3) | PROPOSED |
| `control_plane/deprecation_register.yaml` entry exists for `policies/` | Deprecation tracking (§14.2 step 5) | PROPOSED |
| Drift register entry closed for the policy-home ambiguity | Resolution recorded | PROPOSED |

> [!NOTE]
> Each "PROPOSED" or "NEEDS VERIFICATION" row above is a concrete CI or repo-shape artifact whose absence is itself the validation gap. Treat them as acceptance criteria for moving this ADR from **proposed** → **accepted**.

---

## 11. Open questions and NEEDS VERIFICATION

- **ADR numbering.** "ADR-0003" follows the filename supplied with this work. The live `docs/adr/` index, the title of ADR-0002, and any reserved numbers are **NEEDS VERIFICATION**. If ADR-0003 is already taken, renumber and update cross-references.
- **Current repo state.** Whether `policy/`, `policies/`, both, or neither exist in the live repo is **NEEDS VERIFICATION**. The migration plan in §8 adapts to any of those starting states, but step 1 must run before steps 2–12.
- **Mirror-class default.** If `policies/` is kept (e.g., for IDE / tooling familiarity), the README class default is `mirror`. If `policies/` is slated for removal, the class is `legacy` with a sunset date. The choice is OPEN and resolves at acceptance.
- **Subtree shape under `policy/`.** Section 5 lists the module families the KFM POL substrate calls for; the exact subtree (e.g., domain folders, shared modules, test layout) is PROPOSED and resolves against the live `policy/` directory.
- **CI enforcement.** Whether a CI rule will block `.rego` adds under `policies/` is PROPOSED. Without it, the discipline rests on reviewers and the Path-Validation Checklist.
- **CODEOWNERS.** Owners listed in the meta block are placeholders and require confirmation against the live `CODEOWNERS` file.

---

## 12. Related docs and references

- `directory-rules.md` — §3 (responsibility roots), §5 (authority table — `policy/` canonical singular), §8 (compatibility roots), §8.1 (`policies/` → `policy/` row), §8.3 (no parallel authority), §13.5 (schema mirror divergence anti-pattern), §14.2 (structural-move migration discipline), §15 (README contract), §16 (Path-Validation Checklist), §18 (resolved open question).
- `docs/adr/ADR-0001-*.md` — Schema home / spec normalization (referenced by Directory Rules §5 for `schemas/`). **NEEDS VERIFICATION** of exact filename.
- `docs/adr/ADR-0002-*.md` — Existence and subject **NEEDS VERIFICATION**.
- `policy/README.md` — Canonical README contract entry. PROPOSED to exist.
- `policies/README.md` — Compatibility-class README contract entry. PROPOSED to exist where the folder is present.
- KFM doctrine on the policy substrate: OPA + Conftest + Rego; deny-by-default with explainable reason objects; bundle directory `policy/` with consent / revocation / promotion / sensitivity / license modules.

[⬆ Back to top](#adr-0003--policy-singular-is-canonical-policies-is-compatibility)

---

## Appendix A — Proposed `policy/` subtree

<details>
<summary>Click to expand the proposed canonical subtree under <code>policy/</code></summary>

```text
policy/
├── README.md                       # canonical; per directory-rules.md §15
├── consent/
│   ├── basis.rego
│   ├── expiration.rego
│   └── tests/
├── revocation/
│   ├── revoke_delta.rego
│   └── tests/
├── promotion/
│   ├── gate_a_schema.rego
│   ├── gate_b_identity.rego
│   ├── gate_c_provenance.rego
│   ├── gate_d_catalog_closure.rego
│   ├── gate_e_signing.rego
│   ├── gate_f_dedupe.rego
│   ├── gate_g_evidence_drawer.rego
│   └── tests/
├── sensitivity/
│   ├── classes.rego                # public, public-derived, restricted-aggregate,
│   │                               # restricted-precise, internal, embargoed
│   ├── precise_points_default_deny.rego
│   └── tests/
├── license/
│   ├── recognition.rego
│   ├── intersection.rego
│   └── tests/
├── obligations/
│   ├── propagation.rego
│   └── tests/
└── shared/
    ├── reason_object.rego          # structured DENY reasons (POL-003 explainability)
    └── tests/
```

> [!NOTE]
> **Status:** PROPOSED. Subtree shape is derived from KFM POL substrate doctrine; the live `policy/` tree NEEDS VERIFICATION. Module names map to the families named in the policy substrate; exact filenames may differ.

</details>

---

## Appendix B — Reviewer checklist (mapped to Directory Rules §16)

<details>
<summary>Click to expand the reviewer checklist for any PR touching <code>policy/</code> or <code>policies/</code></summary>

- [ ] **Responsibility identified.** The file's primary responsibility is executable policy substrate.
- [ ] **Right root.** New `.rego` and policy-test files land under `policy/`, not `policies/`.
- [ ] **No new root without ADR.** No new policy-authority root introduced beyond `policy/`.
- [ ] **No parallel authority.** No rule is added or modified under `policies/` directly.
- [ ] **README present.** Both `policy/README.md` (canonical) and, where it exists, `policies/README.md` (mirror or legacy) meet `directory-rules.md` §15.
- [ ] **Compatibility root not evolving independently.** If `policies/` is touched, it is a regeneration from `policy/` or a frozen-history fix only.
- [ ] **Migration discipline followed (§14.2)** for any move from `policies/` → `policy/`: `git mv`, references updated, migration manifest entry, deprecation register entry, rollback dry-run.
- [ ] **Rule cited in PR description.** The PR cites **ADR-0003** and the relevant `directory-rules.md` section.

</details>

[⬆ Back to top](#adr-0003--policy-singular-is-canonical-policies-is-compatibility)

---

### Related docs

- [`directory-rules.md`](./directory-rules.md) — §5, §8, §13.5, §14.2, §15, §16, §18
- [`docs/adr/ADR-0001-*.md`](./ADR-0001-schema-home.md) *(NEEDS VERIFICATION — exact filename)*
- [`docs/adr/ADR-0002-*.md`](./) *(existence and subject NEEDS VERIFICATION)*
- [`policy/README.md`](../../policy/README.md) *(PROPOSED)*
- [`policies/README.md`](../../policies/README.md) *(PROPOSED, compatibility-class README where the folder exists)*

**Last updated:** 2026-05-10 · **Status:** proposed · **ADR ID:** ADR-0003

[⬆ Back to top](#adr-0003--policy-singular-is-canonical-policies-is-compatibility)
