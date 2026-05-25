<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-uuid>
title: Archived Lineage — Atlases, Supplements, and Dossiers
type: standard
version: v1
status: draft
owners:
  primary: Docs steward
  co_authoring: [KFM Domain Synthesizer (atlas-author role), subsystem owner(s) of affected scope, Release authority]
  notes: "Roles CONFIRMED per Atlas v1.1 Ch. 24.7.1. 'KFM Domain Synthesizer' is the atlas-author role (process-level, not a named person) per Atlas v1.1 G.5 assembly procedure."
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/archive/lineage/README.md
  - docs/archive/lineage/standards/README.md
  - docs/archive/lineage/runbooks/README.md
  - docs/archive/lineage/domains/README.md
  - docs/archive/lineage/doctrine/README.md
  - docs/atlases/
  - docs/doctrine/directory-rules.md
  - docs/adr/
  - docs/registers/DRIFT_REGISTER.md
  - control_plane/deprecation_register.yaml
tags: [kfm, archive, lineage, atlases, supplements, dossiers, supersession, navigational, dual-mode]
subject_taxonomy:
  atlas_families:
    - name: domains-culmination-atlas
      editions: [v1.0, v1.1]
      status: CONFIRMED authored
    - name: idea-index-category-atlas
      passes: [Pass 10, Pass 22, Pass 23, Pass 31, Pass 32]
      status: CONFIRMED authored (multi-pass)
    - name: consolidated-deduplicated-atlas
      editions: [Pass 23 + Pass 32 consolidated]
      status: CONFIRMED authored
  dossier_families:
    - name: domain-dossier
      short_names: [DOM-HYD, DOM-SOIL, DOM-HAB, DOM-FAUNA, DOM-FLORA, DOM-AG, DOM-GEOL, DOM-AIR, DOM-HAZ, DOM-ROADS, DOM-SETTLE, DOM-ARCH, DOM-PEOPLE, DOM-HF]
      status: CONFIRMED corpus references
    - name: reference-doctrine
      short_names: [ENCY, MAP-MASTER, INDEX-18, GAI, UIAI, UNIFIED]
      status: CONFIRMED corpus references
directory_rules_basis:
  - "§6.1   — docs/archive/{lineage,exploratory,deprecated} (CONFIRMED v1.3)."
  - "§6.1   — docs/atlases/ home per ADR-S-02 (PROPOSED canonical; ADR-pending)."
  - "Atlas v1.1 Ch. 24.7.2 — atlas/supplement publication: Docs steward + at least one subsystem owner."
  - "Atlas v1.1 Ch. 24.8.2 — Atlas / supplement supersession lives IN-DOCUMENT (App. E/G precedent). Drives §4 exclusion."
  - "Atlas v1.1 Ch. 24.12 ADR-S-02 — dossier home question (secondary worked example)."
  - "Atlas v1.1 Ch. 24.12 ADR-S-15 — Atlas / supplement lifecycle (primary worked example; governs this view's scope)."
notes:
  - "The subfolder 'atlases/' under docs/archive/lineage/ is a PROPOSED domain-segmented view, NEEDS VERIFICATION against ADR."
  - "DUAL-MODE INDEX: this view's INDEX.md contains both navigational entries (pointers to in-document App. E/G) AND true filings (records in parent category lanes). The entry_type column distinguishes them."
  - "Per Atlas v1.1 Ch. 24.8.2, atlas/supplement internal supersession is ALWAYS in-document; this view never duplicates an in-document App. E/G."
  - "All paths to specific files under docs/archive/lineage/atlases/ remain PROPOSED until inspected against a mounted repo."
[/KFM_META_BLOCK_V2] -->

# 🧭 Archived Lineage — Atlases, Supplements, and Dossiers

> **Dual-mode** subject view: a navigational index pointing OUT to in-document supersession appendices across the KFM atlas ecosystem, **and** a true filing surface for the narrow edge cases the in-document pattern cannot handle (atlas-adjacent docs, cross-family events, orphan dossier supersession).

![status](https://img.shields.io/badge/status-draft-orange)
![authority](https://img.shields.io/badge/authority-navigational%20%2B%20filing-7B1FA2)
![type](https://img.shields.io/badge/type-archive%20view-1F3A66)
![mode](https://img.shields.io/badge/mode-dual--mode-critical)
![subject](https://img.shields.io/badge/subject-atlases%20%2B%20dossiers-2E7D32)
![families](https://img.shields.io/badge/atlas%20families-3%20%2B%20dossiers-1F3A66)
![governing-adr](https://img.shields.io/badge/governing%20ADR-ADR--S--15%20pending-orange)
![policy](https://img.shields.io/badge/policy_label-public-2E7D32)
![convention](https://img.shields.io/badge/subfolder%20convention-PROPOSED-orange)
![dir-rules](https://img.shields.io/badge/dir--rules-v1.3%20§6.1-1F3A66)
![updated](https://img.shields.io/badge/updated-2026--05--25-lightgrey)
<!-- TODO — replace placeholder Shields targets once the docs CI surface is verified. -->

**Status:** `draft` · **Primary owner:** Docs steward <sub>(role CONFIRMED · person TODO)</sub> · **Co-authoring:** KFM Domain Synthesizer (atlas-author role), affected subsystem owner(s), Release authority · **Last updated:** `2026-05-25`

> [!IMPORTANT]
> This directory is a **curatorial view**, not a parallel filing surface. Records that DO land in the parent category lanes are **filed** at `docs/archive/lineage/{supersession-records,sunset-records,doctrine-retirements,correction-trails}/`. This `atlases/` subdirectory holds **only** a README, a dual-mode `INDEX.md`, and cross-references. Filing a record file directly here creates parallel authority (Directory Rules §2.4(5)) and is **prohibited**.

> [!CAUTION]
> **Atlas / supplement internal supersession is OUT OF SCOPE.** Per Atlas v1.1 Ch. 24.8.2, the required lineage artifact for an atlas, supplement, or dossier is the **atlas / supplement supersession appendix** — the v1.0 → v1.1 record lives in v1.1 Appendix G (complementing v1.0 Appendix E); pass-card supersession lives in each pass atlas's carry-forward register. **This view never duplicates an in-document appendix.** See §4.

> [!WARNING]
> **Dual-mode INDEX.** Unlike the four sibling views (`standards/`, `runbooks/`, `domains/`, `doctrine/`), this view's `INDEX.md` contains two distinct row types. **Navigational entries** (`entry_type: navigational`) point OUT to in-document App. E/G locations — no record file exists in the parent category lanes. **Filing entries** (`entry_type: filing`) follow the normal sibling pattern — a record file exists in the parent category lanes, and this row cross-references it. The two modes are explicitly distinguished in §11.

---

## Contents

1. [Scope](#1-scope)
2. [Repo fit](#2-repo-fit)
3. [Inputs — what this view indexes](#3-inputs--what-this-view-indexes)
4. [Exclusions — what does not belong here](#4-exclusions--what-does-not-belong-here)
5. [Directory layout](#5-directory-layout)
6. [Index ↔ category mapping (dual-mode)](#6-index--category-mapping-dual-mode)
7. [Subject-curation flow](#7-subject-curation-flow)
8. [Worked example — ADR-S-15 + ADR-S-02](#8-worked-example--adr-s-15--adr-s-02)
9. [Tracked atlases, supplements, and dossiers](#9-tracked-atlases-supplements-and-dossiers)
10. [Authoring workflow](#10-authoring-workflow)
11. [Navigational vs filing entries](#11-navigational-vs-filing-entries)
12. [FAQ](#12-faq)
13. [Related docs](#13-related-docs)
14. [Per-root README contract](#14-per-root-readme-contract)
15. [Appendix](#15-appendix)

---

## 1. Scope

This directory provides a **dual-mode subject-curated view** of supersession lineage for the KFM **atlas / supplement / dossier ecosystem** — the published reference documents (typically PDFs under `docs/atlases/`) that synthesize doctrine, idea cards, and domain knowledge into citable editions.

It exists because:

- KFM operates at least **three atlas families** plus **fourteen named dossiers** (see §9). Each atlas family evolves on its own cadence and uses its own in-document supersession primitive — Domains Culmination Atlas uses App. E + App. G; Idea Index Pass atlases use the carry-forward register; the Consolidated Atlas uses its own deduplication manifest. A reviewer asking "where do I find the v1.0 → v1.1 record?" needs a single answer. This view is that answer. **[CONFIRMED via Atlas v1.1 §2.1 + Appendix G + Pass 23/32 Consolidated Atlas evidence.]**
- Atlas internal lineage is **strictly in-document** per Atlas v1.1 Ch. 24.8.2. But a small number of atlas-related events sit **outside** any single atlas's interior — `docs/atlases/README.md` rev-ups; cross-family migrations (e.g., Idea Index Pass family folded into Domains Culmination family); orphan dossier supersession (e.g., `[DOM-HF]` thin-slice fold-down before any atlas-edition bump). These need a true filing surface, which this view provides via the parent's category lanes. **[CONFIRMED via Atlas v1.1 Ch. 24.8.2 + Atlas v1.1 §2.1 dossier list + Atlas Ch. 24.12 ADR-S-02 and ADR-S-15 backlog.]**
- Atlas v1.1 Ch. 24.12 **ADR-S-15** ("Atlas / supplement lifecycle: cadence of revisions; deprecation rule; supersession path") is the open question that directly governs this view's scope. Until ADR-S-15 lands, the dual-mode framing in §11 is the safest interpretation of the constraints. **[CONFIRMED via Atlas v1.1 Ch. 24.12.]**

The directory is **navigational and selectively filing**, not authoritative. Atlas internal authority remains with the atlas PDF itself; this view never overrides it.

> [!NOTE]
> **Status.** The placement of `docs/archive/` with `lineage/`, `exploratory/`, `deprecated/` sub-areas is **CONFIRMED** via Directory Rules v1.3 §6.1. The **subject-segmented sub-lane `atlases/`** is **PROPOSED** — an explicit ADR is needed to ratify domain-segmented views. The **dual-mode INDEX framing** is also **PROPOSED** pending ADR-S-15 resolution.

[⬆ Back to top](#-archived-lineage--atlases-supplements-and-dossiers)

---

## 2. Repo fit

This subfolder is a curated lens with a dual-mode index. It sits **inside** the documentation-surface lineage archive and points outward to active atlas/supplement/dossier surfaces, to the in-document appendices where atlas-internal lineage lives, and to the parent category lanes where atlas-adjacent records actually live.

| Direction       | Surface                                                              | Relationship                                                                                                              | Status                  |
|-----------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Parent          | [`docs/archive/lineage/README.md`](../README.md)                     | Defines record categories and append-only invariant. This view inherits both, with the dual-mode extension.               | **CONFIRMED**           |
| Subject home    | [`docs/atlases/`](../../../atlases/)                                  | Active atlases / supplements / dossiers (PROPOSED home per ADR-S-02). Subject material of every entry indexed here.       | **PROPOSED home · CONFIRMED contents** |
| In-doc appendices | Each atlas's own App. E / App. G / carry-forward register          | The **authoritative location** for atlas internal supersession per Ch. 24.8.2. **Navigational entries here point at these.** | **CONFIRMED authority** |
| Filing lanes    | `docs/archive/lineage/{supersession-records,sunset-records,doctrine-retirements,correction-trails}/` | Where filing-mode records actually live. Navigational entries have no record file in these lanes.                          | **PROPOSED**            |
| Sibling views   | [`docs/archive/lineage/standards/`](../standards/) · [`runbooks/`](../runbooks/) · [`domains/`](../domains/) · [`doctrine/`](../doctrine/) | The four other subject views. This view is structurally distinct from all four (dual-mode is unique).                       | **AUTHORED**            |
|
