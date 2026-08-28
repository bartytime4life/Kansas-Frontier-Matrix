<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: KFM Domains Culmination Atlas v1.1 — Pointer File (Underscored Variant)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlases/domains-atlas-v1.1.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md
  - docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  - docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - docs/atlases/domains-v1.1.md
  - docs/atlases/domains-v1.1-ch14.md
  - docs/doctrine/directory-rules.md
tags: [kfm, atlas, source-a, v1.1, pointer, carrier, naming-conflicted]
notes:
  - EIGHTH atlas-family path under docs/atlases/. Authored as a minimal pointer file at the underscored-UpperCase convention that matches Atlas v1.1 front matter's PROPOSED PDF home (KFM_Domains_Culmination_Atlas_v1_1.pdf).
  - Doctrinal twin of domains-atlas-v1.1.md (same scope, different naming convention). Defers to twin on all content.
  - No orphan-reference justification (unlike the seventh carrier); exists only to occupy the underscored-UpperCase name slot.
  - Atlas-Markdown naming ADR is now SEVERELY BLOCKING; this file expects to be SUPERSEDED on ADR resolution.
  - Owners, doc_id, related-path verification all remain placeholders.
[/KFM_META_BLOCK_V2] -->

# KFM Domains Culmination Atlas v1.1 — Pointer File *(underscored variant)*

> **Pure pointer to the canonical Source-A carrier (`domains-atlas-v1.1.md`).**
> Exists to occupy the underscored-UpperCase filename slot that matches Atlas v1.1 front matter's PROPOSED PDF home (`KFM_Domains_Culmination_Atlas_v1_1.pdf`), in case any downstream reference adopts that convention.
> **Contains no atlas content.** Routes to canonical carriers and surfaces the unresolved naming-convention drift.

<p align="center">
  <img alt="Status: pointer" src="https://img.shields.io/badge/status-pointer%20file-blue">
  <img alt="Authority: none" src="https://img.shields.io/badge/authority-none%20(pointer%20only)-lightgrey">
  <img alt="Doctrinal twin: domains-atlas-v1.1.md" src="https://img.shields.io/badge/twin-domains--atlas--v1.1.md-orange">
  <img alt="Atlas-family files: 8" src="https://img.shields.io/badge/atlas--family%20paths-8-critical">
  <img alt="ADR: SEVERELY BLOCKING" src="https://img.shields.io/badge/atlas--md%20naming%20ADR-SEVERELY%20BLOCKING-red">
  <img alt="Expected lifespan: until ADR" src="https://img.shields.io/badge/lifespan-until%20ADR%20resolves-yellow">
</p>

> [!IMPORTANT]
> **Status:** `PROPOSED file` / **POINTER ONLY — no atlas content** / `CONFLICTED filename` / expected `SUPERSEDED` on ADR resolution.
> **Owner:** `OWNER_TBD`
> **Proposed path:** `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.md`
> **Canonical carrier this points to:** **`docs/atlases/domains-atlas-v1.1.md`** *(Source-A standalone carrier)*.
> **Why this file exists:** the filename pattern `KFM_Domains_Culmination_Atlas_v1_1.*` is referenced by Atlas v1.1 front matter as the PROPOSED PDF home. This file occupies the matching `.md` slot so that any downstream artifact that adopts the same underscored-UpperCase convention for Markdown finds a real file rather than a 404.
> **Truth posture:** *This file is a pointer, not a carrier.* No claims about the Domains Culmination Atlas v1.1 are made here. **Go to the twin** (`domains-atlas-v1.1.md`) for all content.

---

## 1. Routing

> If you arrived at this file expecting atlas content, use these instead:

| You want… | Go to |
|---|---|
| **The Domains Culmination Atlas v1.1 as a standalone citable artifact** (cover supersession block, edition note, supersession scope rules, conflict rule, what's-new, Chapter 24 sections, Appendix G, reversibility property) | **`docs/atlases/domains-atlas-v1.1.md`** *(doctrinal twin of this file)* |
| The full-text Markdown conversion of the consolidated atlas | `docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` |
| Top-level navigation across Source A + Source B + wrapper + v1.3 overlay | `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` |
| Top-level navigation at the underscored-UpperCase convention | `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` |
| 16 domain chapters at single granularity | `docs/atlases/domains-v1.1.md` |
| One domain chapter at A–N granularity *(example: Ch. 14)* | `docs/atlases/domains-v1.1-ch14.md` |
| Master Receipt Catalog (Atlas §24.2) | `docs/atlases/receipt-catalog.md` |
| Master Pipeline Gate Reference (Atlas §24.6) | `docs/atlases/pipeline-gate-reference.md` |
| Master MapLibre + v1.3 renderer overlay | `docs/atlases/maplibre-master.md` |
| The source PDF of Atlas v1.1 | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` *(mounted-repo presence `NEEDS VERIFICATION`)* |

**For Atlas v1.1's own cover supersession block, edition note, conflict rule, non-collapse rule, reversibility property, or any reproduced atlas wording — go to `domains-atlas-v1.1.md`.** This file deliberately does not reproduce that content.

---

## 2. The seven-variant proliferation, now eight

> [!WARNING]
> **`CONFLICTED`** — this file is the **eighth** atlas-family path under `docs/atlases/` and the **seventh** session-authored Markdown carrier. The atlas-Markdown naming ADR is **severely blocking** any further atlas-family authoring.

### 2.1 All atlas-family paths under `docs/atlases/` (current state)

| # | Path | Naming pattern | Scope |
|---|---|---|---|
| 1 | `KFM_Domains_Culmination_Atlas_v1_1.pdf` | underscored UpperCase, `.pdf` | Atlas v1.1 (Source A) as PDF |
| 2 | `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` | full-title with `_-_` / `___` separators | Full-text Markdown of the consolidated artifact |
| 3 | `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` | kebab-lowercase + `kfm-` prefix | Consolidated atlas navigation |
| 4 | `domains-v1.1.md` | kebab-lowercase, `domains-` family | Domain-focused (16 chapters) |
| 5 | `domains-v1.1-ch14.md` | kebab-lowercase + chapter suffix | Per-chapter (Ch. 14) |
| 6 | `domains-atlas-v1.1.md` | kebab-lowercase + `domains-atlas` noun phrase | Source A standalone *(twin of this file)* |
| 7 | `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` | underscored UpperCase + `_plus_` joiner | Consolidated atlas (resolves orphan refs) |
| **8** | **`KFM_Domains_Culmination_Atlas_v1_1.md`** *(this file)* | **underscored UpperCase, no `_plus_`** | **Pointer only — twins #6** |

### 2.2 What this file does and does not do

| Action | Status |
|---|---|
| Resolve a dangling `related:` reference. | **No.** Unlike the seventh carrier, this filename was not previously referenced by any session-authored sibling. |
| Match the Atlas-v1.1-proposed PDF home convention for Markdown. | **Yes.** That is the sole defensible justification for this file's existence. |
| Add atlas content not present in the twin (`domains-atlas-v1.1.md`). | **No.** Adding content would compound duplication. |
| Make the ADR resolution easier. | **No.** Adds one more file to migrate or supersede. |
| Make the ADR resolution more urgent. | **Yes** — by being the eighth variant, this file pushes the proliferation past the point where new authoring is defensible without ADR. |

### 2.3 Recommended next step (escalated from `domains-atlas-v1.1.md` §12.4 and `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` §3.3)

**File the atlas-Markdown naming ADR.** The decision options are cataloged in `domains-atlas-v1.1.md` §12.3 (directions A through D). At eight variants, no further atlas-family file should be authored without ADR resolution; the operating contract's *"Do not create parallel … homes without an ADR or migration note"* rule applies. Both this file and the seventh carrier are explicit migration notes; the ADR is the missing instrument.

---

## 3. Twin relationship with `domains-atlas-v1.1.md`

| Aspect | This file | Twin (`domains-atlas-v1.1.md`) |
|---|---|---|
| **Scope** | Source A standalone, pointer only. | Source A standalone, full carrier. |
| **Naming pattern** | Underscored UpperCase, matches PDF home. | Kebab-lowercase + `domains-atlas` noun phrase. |
| **Content depth** | One routing table + naming-proliferation flag. | 17-section carrier (cover block, edition note, scope rules, conflict rule, what's-new, integrated contents Mermaid, v1.0 chapter list with coverage, Chapter 24 section list, Appendix G, reversibility, distinction from consolidated, naming reconciliation, ADR backlog, verification, rollback, source ledger). |
| **Reproduces atlas wording verbatim** | **No.** | Yes — cover block, edition note, supersession scope rules, conflict rule, non-collapse rule, Chapter 24 preamble. |
| **Wording authority** | None — defers entirely to twin. | Defers to Atlas v1.1 source PDF. |
| **Long-term status** | One of these two becomes `SUPERSEDED` on ADR resolution. | Same. |

> **The twin has the depth.** This file has the underscored-UpperCase filename slot. That is the entire distinction.

---

## 4. Cross-references

| Reference | Role | Status |
|---|---|---|
| `docs/atlases/domains-atlas-v1.1.md` | **Doctrinal twin. Authoritative on all Source-A content.** | `PROPOSED file` |
| `docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` | Full-text Markdown of the consolidated artifact. | `CONFIRMED file presence` |
| `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` | Top-level navigation carrier (kebab-lowercase). | `PROPOSED file` |
| `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` | Top-level navigation carrier (underscored UpperCase). Twin of #3. | `PROPOSED file` |
| `docs/atlases/domains-v1.1.md` | Domain-focused carrier (16 chapters). | `PROPOSED file` |
| `docs/atlases/domains-v1.1-ch14.md` | Per-chapter dossier (Ch. 14). | `PROPOSED file` |
| `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` | Atlas v1.1 PROPOSED PDF home. **The filename this file mirrors.** | `PROPOSED file home`; mounted-repo presence `NEEDS VERIFICATION` |
| Atlas v1.1 front matter | Defines the proposed PDF home filename pattern (which this file mirrors for `.md`). | `CONFIRMED doctrine` |
| `directory-rules.md` v1.2 §6.1, §17, §8.3 | `docs/atlases/` lane; supersession-discipline rule; 30-day compatibility-alias window. | `CONFIRMED at commit b6a279…` |

---

## 5. ADR backlog

| ADR | Title | Status |
|---|---|---|
| **(severely blocking, new)** | **Atlas-Markdown naming convention under `docs/atlases/`** — decision required across four directions (`domains-atlas-v1.1.md` §12.3 catalogs them). Eight variants now in play. | **BLOCKING further atlas-family authoring.** |
| **(new, proposed)** | Atlas-carrier hierarchy and scope discipline — when is a new atlas-family carrier justified? | Open. |
| `ADR-S-02` | Doctrine artifact placement under `docs/`. | Atlas §24.12. |
| `ADR-S-15` | Doctrine artifact lifecycle (cadence; deprecation; supersession). | Atlas §24.12. |

---

## 6. Verification checklist

- [ ] **File the atlas-Markdown naming ADR.** (Severely blocking; this is the only meaningful action that should happen next.)
- [ ] After ADR resolution: mark whichever of `domains-atlas-v1.1.md` and this file is non-canonical as `SUPERSEDED`; preserve content as lineage.
- [ ] After ADR resolution: update related-field cross-pointers across all atlas-family carriers.
- [ ] Confirm the target path `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.md` does not already exist; resolve `docs/atlas/` mirror collisions.
- [ ] Confirm no atlas wording has crept into this file. If it has, demote — this is meant to be a pointer.
- [ ] **Audit before authoring further atlas-family files**: do not produce a ninth variant; defer to ADR.

---

## 7. Rollback / supersession

| Condition | Action |
|---|---|
| **Atlas-Markdown naming ADR selects kebab-lowercase** | Mark this file `SUPERSEDED`; alias to `domains-atlas-v1.1.md` for 30 days per `directory-rules.md` §8.3; record migration in `docs/registers/DRIFT_REGISTER.md`. |
| **Atlas-Markdown naming ADR selects underscored UpperCase** | Mark `domains-atlas-v1.1.md` `SUPERSEDED`; **migrate the twin's content into this file** (this file currently has no content of its own); alias for 30 days; record migration. |
| **Atlas-Markdown naming ADR selects a third pattern** | Mark both this file and `domains-atlas-v1.1.md` `SUPERSEDED`; produce one carrier under the chosen pattern. |
| **The Atlas v1.1 PDF home itself moves or is renamed** | Update meta-block `related:` field; if the PDF home convention is abandoned, this file's justification ends — mark `SUPERSEDED`. |
| **This file is found to contain atlas wording** | Strip the wording; route to the twin. This file is a pointer, not a carrier. |
| **This file is found to drift from the twin** | The twin wins; restore alignment. |
| **The session-authored ninth atlas-family file is proposed** | **Decline.** File the ADR instead. |

**Rollback target:** `ROLLBACK_TARGET_TBD` (PROPOSED: prior commit ref of this file as recorded in `release/manifests/`).

> **Expected lifespan:** from authorship to ADR resolution. This file is shorter-lived than the seventh carrier (which has a real bridge-state job) — it exists only to mirror the PDF-home convention and surface the proliferation cost. If the ADR is filed promptly, this file is properly `SUPERSEDED` within days.

---

## 8. Source ledger

| Source | Status | Supports |
|---|---|---|
| `docs/atlases/domains-atlas-v1.1.md` (doctrinal twin) | `PROPOSED file` (session-authored) | All routing to canonical Source-A content; §3 twin-relationship table. |
| Atlas v1.1 front matter (proposed PDF home: `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf`) | `CONFIRMED doctrine` | The filename pattern this file mirrors for `.md`. |
| Prior session-authored carriers' §11 / §12 / §3 naming-reconciliation sections | `PROPOSED files` (session-authored) | §2 seven-variant catalog (now eight); §2.3 escalation note; §5 ADR backlog. |
| `directory-rules.md` v1.2 §6.1, §17, §8.3 | `CONFIRMED at commit b6a279…` | §7 rollback actions. |

> **Memory is not evidence.** No claims about the Domains Culmination Atlas v1.1 are made in this file; for atlas claims, see `docs/atlases/domains-atlas-v1.1.md` and the source PDFs. This pointer file's only verifiable claims are the routing rows in §1, the eight-variant catalog in §2.1, and the twin-relationship table in §3 — all of which are verifiable from prior session output and the existing `/mnt/project/` files.

---

<p align="right"><a href="#kfm-domains-culmination-atlas-v11--pointer-file-underscored-variant">↑ Back to top</a></p>
