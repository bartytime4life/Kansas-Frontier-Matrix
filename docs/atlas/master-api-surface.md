<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PATH_TBD_AFTER_REPO_INSPECTION
title: docs/atlas/decision-outcome-envelope.md — Deprecated Pointer
type: standard
version: v1
status: deprecated
owners: OWNER_TBD (docs steward; placement steward)
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlas/README.md
  - docs/atlases/decision-outcome-envelope.md
  - docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/adr/ADR-S-02-docs-dossiers-vs-docs-atlases.md
  - contracts/runtime/decision_envelope.md
  - schemas/contracts/v1/runtime/decision_envelope.schema.json
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, atlas, pointer, deprecated, decision-outcome-envelope, redirect]
notes:
  - "This is a pointer page in a deprecated compatibility lane. It carries no atlas content of its own."
  - "Canonical atlas-register home (PROPOSED): docs/atlases/decision-outcome-envelope.md (NEEDS VERIFICATION — file may not exist yet)."
  - "Canonical meaning-contract home (PROPOSED): contracts/runtime/decision_envelope.md."
  - "Canonical schema home (PROPOSED, per KFM-P5-PROG-0001): schemas/contracts/v1/runtime/decision_envelope.schema.json."
  - "Authoritative reference today: Atlas v1.1 §24.3 — Master Decision Outcome Envelope Reference."
  - "Sunset: this pointer file SHOULD be removed when docs/atlas/ is retired at the end of the 30-day mirror window."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/atlas/decision-outcome-envelope.md` — Deprecated Pointer

> This file is a **deprecation pointer** in the [`docs/atlas/`](./README.md) compatibility lane. It carries no register content. Read the canonical sources listed below.

![status: DEPRECATED](https://img.shields.io/badge/status-DEPRECATED-red)
![authority: compatibility · pointer](https://img.shields.io/badge/authority-compatibility%20%C2%B7%20pointer-lightgrey)
![canonical lane: docs/atlases/](https://img.shields.io/badge/canonical%20lane-docs%2Fatlases%2F-blue)
![canonical target: PROPOSED](https://img.shields.io/badge/canonical%20target-PROPOSED-yellow)
![ADR: ADR-S-02](https://img.shields.io/badge/ADR-ADR--S--02-yellow)

> [!IMPORTANT]
> **Status:** `DEPRECATED` (doctrine-CONFIRMED per [`docs/atlas/README.md`](./README.md) §5–§6).
> **Owner:** `OWNER_TBD` — docs steward.
> **Sunset:** end of the 30-day `docs/atlas/` mirror window. This file SHOULD be removed when the parent folder is retired.
> **Truth posture:** `CONFIRMED` deprecation framing / `PROPOSED` canonical target paths / `NEEDS VERIFICATION` mounted-repo presence of every target listed below / `UNKNOWN` repo implementation depth.

**Quick jumps:** [What this object family is](#1-what-this-object-family-is-orientation-only) · [Where the canonical content lives](#2-where-the-canonical-content-lives) · [Why this file is here as a pointer](#3-why-this-file-is-here-as-a-pointer) · [What this file does NOT contain](#4-what-this-file-does-not-contain) · [Verification checklist](#5-verification-checklist) · [Rollback / removal](#6-rollback--removal)

---

## 1. What this object family is (orientation only)

`CONFIRMED doctrine — every governed API surface, validator, policy gate, and Focus Mode answer in KFM returns a finite outcome from a small, well-known set.` (Atlas v1.1 §24.3; *Connected-Dots Architecture Brief* §11; *AI Build Operating Contract* §9.2.)

This object family appears in the corpus under two related-but-distinct names:

| Term | Role | Canonical responsibility root | Stable ID (where applicable) |
|---|---|---|---|
| **Decision Outcome Envelope** *(atlas-register form)* | Cross-surface reference register enumerating outcome classes and their per-surface mappings. | `docs/atlases/` | (Atlas v1.1 §24.3) |
| **`DecisionEnvelope`** *(policy-output object form)* | Finite-shape envelope `{decision_id, outcome, policy_family, reasons[], obligations[], evaluated_at}` emitted by every policy module. | `contracts/runtime/` (meaning) + `schemas/contracts/v1/runtime/` (shape) | `KFM-P5-PROG-0001` |
| **`RuntimeResponseEnvelope`** *(governed-API runtime form)* | Finite, governed response shape returned by runtime surfaces; outcomes drawn from the same vocabulary. | `contracts/runtime/` (meaning) + `schemas/contracts/v1/runtime/` (shape) | *(see AI Build Operating Contract §9.2)* |

These are **three distinct files** in their canonical homes — a docs-side register, a meaning contract, and a runtime contract. **None of them lives at `docs/atlas/`.**

> [!NOTE]
> This section is orientation, not content. It states what the family **is** and where its real definitions live. It does not enumerate outcome classes, surface mappings, or schema fields — those belong only at the canonical homes.

[↑ back to top](#top)

---

## 2. Where the canonical content lives

| If you want to read… | Go to | Responsibility root | Status |
|---|---|---|---|
| The **master cross-surface register** (outcome classes, surface mapping, validator-class outcomes) | `docs/atlases/decision-outcome-envelope.md` *(as a standalone register extract)* | `docs/` — atlas lane | `PROPOSED` — file `NEEDS VERIFICATION`; may not yet exist as a standalone extract |
| The **authoritative current source** for the master register | `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` § "24.3 Master Decision Outcome Envelope Reference" | `docs/` — atlas lane | `PROPOSED placement` per Atlas v1.1 Appendix G; mounted-repo presence `NEEDS VERIFICATION` |
| The **edition-of-record PDF** for the master register | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` § Ch. 24.3 | `docs/` — atlas lane | `PROPOSED placement` per Atlas v1.1 Appendix G G.4; mounted-repo presence `NEEDS VERIFICATION` |
| The **object-family meaning contract** for `DecisionEnvelope` | `contracts/runtime/decision_envelope.md` | `contracts/` — meaning | `PROPOSED` — `NEEDS VERIFICATION` |
| The **JSON Schema** for `DecisionEnvelope` | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | `schemas/` — shape | `PROPOSED` per `KFM-P5-PROG-0001`; `NEEDS VERIFICATION` |
| The **doctrine** binding the outcome vocabulary to governed-AI behavior | `docs/doctrine/ai-build-operating-contract.md` §9.2 (Trust objects: `RuntimeResponseEnvelope`) | `docs/doctrine/` | `CONFIRMED` in attached corpus |
| The **governed-API surface mapping** (per-resolver outcomes) | Atlas v1.0 §20.3 "Master API Surface Table" (retained verbatim inside Atlas v1.1) | `docs/` — atlas lane | `CONFIRMED reference in corpus`; physical placement `NEEDS VERIFICATION` |
| The **architecture binding** between outcome envelope and finite-outcome runtime surfaces | `docs/architecture/connected-dots-architecture-brief.md` §11 *(or equivalent)* | `docs/architecture/` | `CONFIRMED in corpus`; exact filename `NEEDS VERIFICATION` |

> [!CAUTION]
> All relative paths above are `PROPOSED` from this file's location and have not been verified against a mounted repo. Treat them as redirect targets to confirm, not as proof that the target file exists today.

[↑ back to top](#top)

---

## 3. Why this file is here as a pointer

`CONFIRMED doctrine:`

1. `docs/atlas/` (singular) is a **deprecated compatibility mirror** during a 30-day sunset window. See [`docs/atlas/README.md`](./README.md).
2. The canonical doc-lane for atlas-class artifacts is `docs/atlases/` (plural), per `directory-rules.md` v1.2 §6.1 + §13.5 row "Docs naming duplication", per the *KFM Repository Structure Guiding Document* migration plan row `Docs naming`, and per Atlas v1.1 Appendix G G.4.
3. During the sunset window, `docs/atlas/` is permitted to carry **only** the deprecation README and conforming pointer pages — no atlas content, no master register, no contract, no schema. *(Per [`docs/atlas/README.md`](./README.md) §5–§6.)*
4. This file is a conforming pointer page. It carries the deprecation banner, the redirect table, and no register content.

If you arrived here from a legacy backlink, the redirect table in §2 lists every canonical home you might be looking for. Update your backlink to one of those targets and stop linking into `docs/atlas/`.

[↑ back to top](#top)

---

## 4. What this file does NOT contain

`CONFIRMED — this pointer page intentionally OMITS:`

- The outcome-class enumeration (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR` / `HOLD` / `PASS` / `FAIL` / optional `NARROWED` / `BOUNDED`).
- The outcome × surface mapping table.
- The required-artifact table per outcome.
- The validator-class outcome subset.
- The `DecisionEnvelope` field shape (`decision_id`, `outcome`, `policy_family`, `reasons[]`, `obligations[]`, `evaluated_at`).
- Reason-code catalogs, obligation-shape catalogs, or deny-reason families.
- Per-domain envelope variants (consent, sensitivity, render, promotion, capability).

> [!WARNING]
> If a future PR adds any of the above content to this file, the PR re-opens parallel-authority drift and should be refused at review. The substantive content belongs at the canonical homes listed in §2.

[↑ back to top](#top)

---

## 5. Verification checklist

- [ ] Confirm the canonical atlas-register file exists at `docs/atlases/decision-outcome-envelope.md` *(or)* confirm that Atlas v1.1 §24.3 inside `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` is the authoritative reference and that no standalone register extract is needed.
- [ ] Confirm the meaning contract exists at `contracts/runtime/decision_envelope.md` *(or)* file a routine PR to author it per `KFM-P5-PROG-0001`.
- [ ] Confirm the JSON Schema exists at `schemas/contracts/v1/runtime/decision_envelope.schema.json` *(or)* file a routine PR to author it per `KFM-P5-PROG-0001` "Suggested path".
- [ ] Confirm that every internal repo backlink to `docs/atlas/decision-outcome-envelope.md` has been redirected to the canonical home selected in step 1.
- [ ] Confirm an entry exists in `control_plane/deprecation_register.yaml` for this pointer file's removal at sunset, or rely on the parent-folder entry from [`docs/atlas/README.md`](./README.md).
- [ ] Confirm no substantive register content has been added to this file (see §4).

[↑ back to top](#top)

---

## 6. Rollback / removal

This file **should be removed**, not maintained, when the `docs/atlas/` mirror window closes. The doctrinally-correct end-state is:

- `docs/atlas/` no longer exists in the repo.
- Every backlink that previously pointed at `docs/atlas/decision-outcome-envelope.md` now points to one of the canonical homes in §2.
- The deprecation entry in `control_plane/deprecation_register.yaml` is closed.

`PROPOSED rollback path` (if removal causes link breakage that the redirect map did not catch): restore this exact pointer file from git history under the original `docs/atlas/decision-outcome-envelope.md` path, extend the mirror window in the deprecation register, and reopen the migration manifest for a second pass of backlink redirection.

**Rollback target:** `ROLLBACK_TARGET_TBD` — record the migration manifest `git_sha_before` here once known.

[↑ back to top](#top)

---

<details>
<summary><strong>Appendix A — Evidence basis (source ledger)</strong></summary>

| Source | Status | Supports | Limits |
|---|---|---|---|
| `docs/atlas/README.md` (prior turn, this session) | `CONFIRMED doctrine framing` | `docs/atlas/` is a deprecated mirror; only README and pointer pages permitted. | Doctrine framing only; mounted-repo state `NEEDS VERIFICATION`. |
| `directory-rules.md` v1.2 §6.1 + §13.5 row "Docs naming duplication" | `CONFIRMED doctrine` | Canonical lane is `docs/atlases/`. | Commit-pinned doctrine, not a `ls` of the working tree. |
| Atlas v1.1 §24.3 "Master Decision Outcome Envelope Reference" | `CONFIRMED corpus content` | Outcome class enumeration, per-surface mapping, validator-class outcomes. | Atlas-level reference; not a contract or schema. |
| Atlas v1.1 Appendix G G.4 "Edition identity and citation form" | `CONFIRMED edition statement` | Canonical placement of the v1.1 PDF and (by inheritance) of any extracted register at `docs/atlases/`. | Atlas explicitly notes "Final repo placement … NEEDS VERIFICATION". |
| `KFM-P5-PROG-0001` (Pass 23/32 consolidated atlas card) | `PROPOSED implementation`, `CONFIRMED card content` | `DecisionEnvelope` shape, suggested schema path. | Idea-card status; not implementation proof. |
| `ai-build-operating-contract.md` §9.2 Trust objects | `CONFIRMED doctrine` | `RuntimeResponseEnvelope` finite outcome vocabulary. | Doctrine, not implementation depth. |
| `connected-dots-architecture-brief.md` §11 finite-outcome envelope vocabulary | `CONFIRMED doctrine reference` | Outcome × required-artifact × surface-effect mapping. | Brief reference, not contract authority. |

**Memory is not evidence.** No mounted repo, CI run, workflow, dashboard, or branch state was inspected for this pointer page. Every implementation claim above is bounded to doctrine.

</details>

[↑ back to top](#top)
