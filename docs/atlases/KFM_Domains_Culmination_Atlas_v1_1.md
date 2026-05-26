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
| Make the ADR resolution easier. | **No.** Adds one more file to migrate or
