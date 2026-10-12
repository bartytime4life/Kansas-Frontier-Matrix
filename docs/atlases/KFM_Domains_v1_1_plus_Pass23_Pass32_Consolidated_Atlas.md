<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-atlases-kfm-domains-v1-1-pass23-pass32-consolidated-pointer
title: KFM Domains v1.1 + Pass 23/32 Consolidated Atlas — Carrier (Underscored Variant)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-05-25
updated: 2026-08-31
policy_label: public
owning_root: docs/
responsibility: "Provide a minimal underscored pointer for the consolidated-atlas family and route readers without selecting a canonical carrier or promoting source claims."
truth_posture: "CONFIRMED file presence and current routing / source-derived atlas lineage / carrier identity, naming, migration, ownership, and document identity remain open decisions or UNKNOWN"
related:
  - docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated Atlas.md
  - docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  - docs/atlases/domains-atlas-v1.1.md
  - docs/atlases/domains-v1.1.md
  - docs/atlases/domains-v1.1-ch14.md
  - docs/atlases/receipt-catalog.md
  - docs/atlases/pipeline-gate-reference.md
  - docs/atlases/maplibre-master.md
  - docs/doctrine/directory-rules.md
tags: [kfm, atlas, v1.1, pass23, pass32, doctrine, carrier, naming-conflicted]
notes:
  - Resolves three dangling related: references in receipt-catalog.md, pipeline-gate-reference.md, and maplibre-master.md meta blocks — those files all reference this exact path.
  - Same scope as kfm-domains-v1.1-pass23-32-consolidated-atlas.md (consolidated artifact carrier); the two files are CONFLICTED at the naming-convention layer pending the atlas-Markdown naming ADR.
  - This is the SEVENTH atlas-family file under docs/atlases/; the proliferation is operationally costly and surfaced in §3.
  - Owner remains a placeholder; the path-derived doc_id follows adjacent atlas metadata convention, while machine-registry adoption remains review-only.
[/KFM_META_BLOCK_V2] -->

# KFM Domains v1.1 + Pass 23/32 Consolidated Atlas — Carrier *(underscored-UpperCase variant)*

> **A navigation carrier for the consolidated atlas (Source A + Source B + wrapper + v1.3 overlay) at the underscored-UpperCase filename pattern that Atlas v1.1 front matter itself uses for its PDF home.**
> **This file's content overlaps `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` deliberately.** The two carriers cover the same content domain at two different naming conventions, pending ADR resolution. **They are not parallel authorities** — see §3.

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Authority: carrier" src="https://img.shields.io/badge/authority-carrier--only-lightgrey">
  <img alt="Naming: 7 variants in CONFLICTED state" src="https://img.shields.io/badge/atlas--family-7%20variants%20CONFLICTED-critical">
  <img alt="Anchor: Atlas v1.1 + Pass 23/32 + v1.3 overlay" src="https://img.shields.io/badge/anchor-consolidated%20atlas-success">
  <img alt="Doctrinal twin: kfm-domains-v1.1-pass23-32-consolidated-atlas.md" src="https://img.shields.io/badge/twin-kfm--domains--v1.1--pass23--32--consolidated--atlas.md-orange">
  <img alt="ADR: BLOCKING" src="https://img.shields.io/badge/atlas--md%20naming%20ADR-BLOCKING-red">
</p>

**Quick jump:** [Purpose](#1-purpose-and-role) · [Resolves dangling refs](#2-what-this-file-resolves) · [Naming proliferation](#3-the-seventh-variant-conflicted) · [Twin relationship](#4-twin-relationship-with-kfm-domains-v11-pass23-32-consolidated-atlasmd) · [Routing](#5-routing-to-canonical-carriers) · [Atlas at a glance](#6-the-consolidated-atlas-at-a-glance) · [Verification](#9-verification-checklist) · [Rollback](#10-rollback--supersession) · [Source ledger](#11-source-ledger)

> [!IMPORTANT]
> **Status:** `PROPOSED file` / `CONFIRMED doctrine` (consolidated atlas structure) / `UNKNOWN repo implementation depth` / **`CONFLICTED` filename**
> **Owner:** `OWNER_TBD`
> **Proposed path:** `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md`
> **Filename pattern:** underscored UpperCase with `KFM_` abbreviation and `_plus_` joiner — matches Atlas v1.1 front matter's PDF home pattern (`KFM_Domains_Culmination_Atlas_v1_1.pdf`); does **not** match the kebab-lowercase convention used by the six other session-authored carriers.
> **Justification for existence:** three earlier session-authored carriers (`receipt-catalog.md`, `pipeline-gate-reference.md`, `maplibre-master.md`) reference this exact path in their `related:` meta blocks. This file resolves those references rather than leaving them orphan.
> **Truth posture:** *Atlas v1.1 + Pass 23/32 source PDFs are doctrine.* This file is a carrier. EvidenceBundle and the per-domain dossiers remain authoritative. **This carrier defers to its kebab-lowercase twin (`kfm-domains-v1.1-pass23-32-consolidated-atlas.md`) on wording and structure** until the ADR picks a canonical name.

> [!NOTE]
> **Evidence boundary.** This file exists for path-reference reasons (§2). Its
> content is intentionally minimal and routes readers to source-derived carriers
> and named source PDFs. The linked Markdown is incomplete; repository
> implementation, release, deployment, and publication require separate current
> evidence.

---

## 1. Purpose and role

This file has a narrow operational purpose: **resolve three dangling `related:` references** in earlier session-authored carriers, which all point at this exact filename, while making the underlying naming-convention drift visible enough that the ADR resolution becomes unavoidable.

It does **not** re-render the consolidated atlas. The existing source-derived
carrier, `docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated
Atlas.md`, comes from a 1,279-page PDF but retains conversion only through roughly
page 286, followed by a synthesized continuity tail. The chapter-level navigation
lives in `kfm-domains-v1.1-pass23-32-consolidated-atlas.md`. This file routes
readers to both.

Three non-collapse rules apply:

1. **Atlas v1.1 + Pass 23/32 source PDFs win on doctrine.** This file is a carrier.
2. **Check source wording at the source.** The incomplete Markdown conversion is
   closer than this pointer, but consequential wording must be verified against
   the source PDFs.
3. **This file does not establish a parallel naming authority.** Both this file and `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` exist while the ADR pends; afterward, one is canonical and the other is `SUPERSEDED` (lineage preserved per `directory-rules.md` §17).

---

## 2. What this file resolves

> **Doctrinal anchor:** the `related:` field of three session-authored sibling carriers points at exactly `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md`.

| Sibling carrier | Reference to this path | Status before this file existed |
|---|---|---|
| `docs/atlases/receipt-catalog.md` *(Atlas §24.2 carrier)* | `related:` meta-block field | **Dangling reference** to a file that did not exist. |
| `docs/atlases/pipeline-gate-reference.md` *(Atlas §24.6 carrier)* | `related:` meta-block field | **Dangling reference**. |
| `docs/atlases/maplibre-master.md` *(Master MapLibre + v1.3 overlay carrier)* | `related:` meta-block field | **Dangling reference**. |
| `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` §11 (Naming-convention reconciliation) | Flagged the dangling reference and the orphan path as `CONFLICTED`. | Honest surfacing; not a resolution. |

**With this file present**, the three dangling references resolve to a real file. The naming-convention `CONFLICTED` state in the top-level carrier's §11 is **unchanged** — the same underlying ADR question remains open — but the operational orphan-reference issue is resolved.

> [!IMPORTANT]
> **Resolving dangling references is not the same as picking a canonical name.** The proper long-term fix is to (a) file the atlas-Markdown naming ADR, (b) pick a canonical filename, (c) rename or `SUPERSEDE` the non-canonical one, (d) update the `related:` fields of the three sibling carriers to point at the canonical name. This file is a **bridge**, not a destination.

---

## 3. The seventh variant (`CONFLICTED`)

> [!WARNING]
> **`CONFLICTED`** — this catalog lists **seven** atlas-family names repository-wide:
> six under `docs/atlases/` and one current source-derived carrier at the
> `docs/` root. Naming and migration remain unresolved.

### 3.1 Catalogued atlas-family paths (one outside `docs/atlases/`)

| # | Path | Naming pattern | Scope | Authored where |
|---|---|---|---|---|
| 1 | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` | underscored UpperCase + `KFM_` abbrev, `.pdf` | Proposed Atlas v1.1 PDF home | Current path is a directory collision, not a PDF file; migration remains unresolved |
| 2 | `docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated Atlas.md` | title-style name with spaces, punctuation, and a numeric underscore | Incomplete source-derived Markdown carrier | `CONFIRMED file presence`; retained conversion through roughly page 286 plus a synthesized continuity tail |
| 3 | `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` | kebab-lowercase + `kfm-` prefix | Consolidated atlas navigation carrier | `CONFIRMED file presence`; draft source-derived navigation |
| 4 | `docs/atlases/domains-v1.1.md` | kebab-lowercase, no atlas/kfm prefix | Domain-focused carrier (16 chapters) | `CONFIRMED file presence`; internal status governs content |
| 5 | `docs/atlases/domains-v1.1-ch14.md` | kebab-lowercase + chapter suffix | Per-chapter dossier (Ch. 14) | `CONFIRMED file presence`; internal status governs content |
| 6 | `docs/atlases/domains-atlas-v1.1.md` | kebab-lowercase + `domains-atlas` noun phrase | Source A only (standalone-citable carrier) | `CONFIRMED file presence`; internal status governs content |
| **7** | **`docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md`** *(this file)* | **underscored UpperCase + `KFM_` abbrev + `_plus_` joiner, `.md`** | Consolidated atlas navigation carrier *(twins #3)* | `CONFIRMED file presence`; draft pointer |

### 3.2 The naming-variant cardinality problem

Across the seven paths, there are now **at least four genuinely distinct naming patterns** (pattern frequency in parens):

- Title-style spaces, punctuation, and numeric underscore (1 current root path).
- Underscored UpperCase + `KFM_` abbreviation (2 paths: the Atlas-proposed PDF home; this file).
- Kebab-lowercase + `kfm-` prefix (1 path: top-level navigation carrier).
- Kebab-lowercase + `domains-` family (3 paths: domain-focused, per-chapter, Source-A carriers).

This is not a stable end-state for `docs/atlases/`. The KFM operating contract is explicit: *"Do not create parallel … homes without an ADR or migration note."* The migration note is `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` §11; the ADR is unfiled. Adding this seventh file pushes the proliferation from `worth-flagging` to `blocking-further-authoring`.

### 3.3 Why this file exists despite the proliferation

The narrow justification: **three sibling carriers reference exactly this filename**, and leaving those references dangling is itself a doctrine cost (drift between meta-block `related:` fields and actual file presence). Producing this file as a routing stub resolves the orphan references at a fraction of the content-duplication cost it would take to produce a full second consolidated-atlas carrier.

The cost is real anyway: a seventh atlas-family file under one directory is operationally confusing for any reader navigating `docs/atlases/` for the first time. §10 (Rollback / supersession) sets up the merge path: when the ADR resolves, **either** this file **or** `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` (whichever is non-canonical) is marked `SUPERSEDED`, the canonical one absorbs the routing rows, and the `related:` fields of the three referring sibling carriers are updated.

---

## 4. Twin relationship with `kfm-domains-v1.1-pass23-32-consolidated-atlas.md`

> **This file and `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` are doctrinal twins** — same content domain, different naming conventions. The kebab-lowercase twin is more developed (chapter index, Pass 23/32 totals, v1.3 overlay summary, naming-reconciliation section). This file is intentionally **minimal** to avoid compounding the content-duplication cost.

| Aspect | This file | Twin (`kfm-domains-…`) |
|---|---|---|
| **Scope** | Consolidated atlas navigation. | Consolidated atlas navigation. |
| **Naming pattern** | Underscored UpperCase + `KFM_` + `_plus_`. | Kebab-lowercase + `kfm-` prefix. |
| **Content depth** | Intentionally minimal; routes to current entry points. | Full 17-section navigation (chapter index, Pass 23/32 totals, v1.3 source overlay, ADR backlog, etc.). |
| **Authored to resolve** | Dangling `related:` references in three sibling carriers (§2). | Reader-facing navigation entry point. |
| **Long-term status** | One of these two is `SUPERSEDED` once the ADR resolves. | One of these two is `SUPERSEDED` once the ADR resolves. |
| **Wording check** | Defers to named source evidence. | The incomplete Markdown helps locate retained wording; consequential wording requires source-PDF verification. |

> **Where to read more.** For the chapter index, Pass 23/32 totals, v1.3 overlay coverage, Chapter 24 section list, ADR backlog, and naming-reconciliation discussion, use **`docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md`** directly. This file does **not** duplicate that content.

---

<a id="5-routing-to-canonical-carriers"></a>

## 5. Routing to current entry points

> Use this table to find the current entry point for a consolidated-atlas concern.
> File presence and routing do not make a carrier canonical or authoritative.

| Concern | Entry point | Path |
|---|---|---|
| Retained source wording and conversion lineage | Incomplete source-derived carrier | `docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated Atlas.md` |
| Top-level navigation across Source A + Source B + wrapper + v1.3 overlay | Top-level carrier | `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` |
| Source A standalone (Atlas v1.1 as citable artifact) | Source-A carrier | `docs/atlases/domains-atlas-v1.1.md` |
| 16 domain chapters at single granularity | Domain-focused carrier | `docs/atlases/domains-v1.1.md` |
| One domain chapter at A–N granularity *(example: Ch. 14)* | Per-chapter carrier | `docs/atlases/domains-v1.1-ch14.md` |
| Master Receipt Catalog (§24.2) | Receipt-catalog carrier | `docs/atlases/receipt-catalog.md` |
| Master Pipeline Gate Reference (§24.6) | Pipeline-gate carrier | `docs/atlases/pipeline-gate-reference.md` |
| Master MapLibre Components/Functions/Features + v1.3 renderer overlay | MapLibre master carrier | `docs/atlases/maplibre-master.md` |
| Atlas v1.1 proposed PDF home | Collision record only | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/` is currently a directory, not the source PDF |

---

## 6. The consolidated atlas at a glance

> **One-screen summary only.** For depth, use `kfm-domains-v1.1-pass23-32-consolidated-atlas.md`.

| Field | Value (`CONFIRMED`) |
|---|---|
| **Title (consolidated)** | *Kansas Frontier Matrix - Domains v1.1 + Pass 23/32 Consolidated Atlas* |
| **Total pages** | 1,279 (Source A 177 + Source B 1,095 + wrapper 7) |
| **Source A** | *Kansas Frontier Matrix Domains Culmination Atlas, v1.1* (2026-05-12; SHA-256 prefix `a0dda5f…`) |
| **Source B** | *KFM Pass 23 + Pass 32 Consolidated Deduplicated Atlas* (SHA-256 prefix `9c5141a…`) |
| **Pass 32 card totals** | added=60; expanded=290; unchanged=1,239; superseded=0; quarantined=18; total=**1,607** |
| **13 categories (Pass 23/32)** | `ANA`, `CAT`, `DAT`, `DOC`, `EVD`, `MAP`, `MDP`, `MOD`, `PIP`, `POL`, `REL`, `SEC`, `UIX` |
| **v1.3 Renderer Decision Overlay** | `PROPOSED doctrine target` pending ADR-OPEN-DR-10 acceptance; freeze rule on new `cesium*` artifacts **in effect immediately** |
| **Conflict rule (Atlas v1.1)** | Where a Ch. 24 register and a v1.0 section disagree, **v1.0 retains authority**. |
| **Non-collapse rule** | Registers are navigational aids; `EvidenceBundle` and dossiers remain authoritative. |
| **Reversibility** | v1.1 minus its v1.1 additions yields v1.0 in original form; v1.0 remains standalone-citable. |

---

## 7. ADR backlog

| ADR | Title (`PROPOSED`) | Touched by this carrier |
|---|---|---|
| **(blocking, new)** | **Atlas-Markdown naming convention under `docs/atlases/`** — pick from four directions in `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` §11.2 / `domains-atlas-v1.1.md` §12.3. | **Entire §3 of this file.** This ADR's resolution determines whether this file or `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` is `SUPERSEDED`. |
| **(new, proposed)** | Atlas-carrier hierarchy and scope discipline — define when a new atlas-family carrier is justified (genuine scope distinction) vs. when it's duplication. | §3 (this file exists for path-resolution reasons, not scope-distinction reasons). |
| `ADR-S-02` | Doctrine artifact placement under `docs/` (`dossiers/` vs `atlases/`). | Lane choice. |
| `ADR-S-15` | Doctrine artifact lifecycle (revision cadence; deprecation; supersession path). | §10 supersession discipline for whichever of this file or the twin is non-canonical. |

> **The atlas-Markdown naming ADR is now severely overdue.** Seven atlas-family paths exist in one directory; further authoring is blocked.

---

## 8. Cross-references

| Reference | Role | Status |
|---|---|---|
| `docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated Atlas.md` | Full-text source-derived carrier; closest retained conversion wording, not repository implementation authority. | `CONFIRMED file presence`; source fidelity remains bounded |
| `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` | **Doctrinal twin (kebab-lowercase).** Authoritative on structure where this file paraphrases. | `PROPOSED file` |
| `docs/atlases/domains-atlas-v1.1.md` | Source-A-only carrier (sibling). | `PROPOSED file` |
| `docs/atlases/domains-v1.1.md` | Domain-focused carrier (sibling). | `PROPOSED file` |
| `docs/atlases/domains-v1.1-ch14.md` | Per-chapter dossier carrier (sibling). | `PROPOSED file` |
| `docs/atlases/receipt-catalog.md` | Atlas §24.2 sub-carrier. **References this file in its `related:` field.** | `PROPOSED file` |
| `docs/atlases/pipeline-gate-reference.md` | Atlas §24.6 sub-carrier. **References this file in its `related:` field.** | `PROPOSED file` |
| `docs/atlases/maplibre-master.md` | Master MapLibre + v1.3 overlay carrier. **References this file in its `related:` field.** | `PROPOSED file` |
| `directory-rules.md` v1.2 §6.1, §17 | `docs/atlases/` lane choice; supersession-discipline rule for rule reversal. | `CONFIRMED at commit b6a279…` |
| `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` §11 (Naming-convention reconciliation) | Pre-existing surfacing of this file's `CONFLICTED` orphan-reference status. | `PROPOSED file` |
| `domains-atlas-v1.1.md` §12 (Naming-convention reconciliation, escalated) | Pre-existing surfacing of the seven-variant proliferation problem and the four resolution directions. | `PROPOSED file` |

---

## 9. Verification checklist

- [ ] **Atlas-Markdown naming ADR (BLOCKING)**: file the ADR; pick a canonical filename pattern (kebab-lowercase, underscored UpperCase, or hybrid); apply consistently.
- [ ] After ADR: rename or `SUPERSEDE` whichever of this file and `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` is non-canonical.
- [ ] After ADR: update `related:` fields in `receipt-catalog.md`, `pipeline-gate-reference.md`, `maplibre-master.md` to point at the canonical name.
- [ ] After ADR: update `related:` field cross-pointers in `domains-v1.1.md`, `domains-v1.1-ch14.md`, `domains-atlas-v1.1.md` as needed.
- [ ] Confirm `OWNER_TBD` — docs steward.
- [ ] Review the path-derived `doc_id` through the emitted registry delta; do not replace it with an invented UUID.
- [x] Confirm this pointer exists at its current path; `docs/atlas/` convergence
  remains unresolved.
- [ ] Confirm §6 at-a-glance metadata matches the full-text Markdown carrier and the source PDFs.
- [ ] Confirm §5 routing table covers every concern the three referring sibling carriers might lead a reader to look for.
- [ ] **Audit**: confirm whether this file's *only* operational job is dangling-reference resolution. If the ADR resolution path proceeds, the file's job ends.

---

## 10. Rollback / supersession

| Condition | Action |
|---|---|
| **Atlas-Markdown naming ADR selects kebab-lowercase** | Mark this file `SUPERSEDED`; preserve content as lineage in `kfm-domains-v1.1-pass23-32-consolidated-atlas.md`; update the three sibling carriers' `related:` fields to the kebab-lowercase name; record migration in `docs/registers/DRIFT_REGISTER.md`. |
| **Atlas-Markdown naming ADR selects underscored UpperCase** | Mark `kfm-domains-v1.1-pass23-32-consolidated-atlas.md` `SUPERSEDED`; merge its content into this file; update sibling carriers' `related:` fields to this file; rename `domains-v1.1.md`, `domains-v1.1-ch14.md`, `domains-atlas-v1.1.md` per the chosen convention. |
| **Atlas-Markdown naming ADR selects a third pattern** | Mark **both** twins `SUPERSEDED`; author one carrier under the chosen pattern; migrate all referrers. |
| **Atlas v1.2 is issued** | Affects both twins identically; preserve v1.1 lineage in whichever twin survives the ADR. |
| **ADR-0007 is superseded or amended** | Reconcile the older v1.3 overlay with the accepted successor while preserving source lineage and separate runtime/release evidence. |
| **`related:` field convention changes (e.g., to UUIDs or doc-ids)** | This file's path-resolution job becomes unnecessary; mark `SUPERSEDED`. |
| **The three sibling carriers' `related:` fields are updated to point elsewhere** | This file's path-resolution job becomes unnecessary; mark `SUPERSEDED`. |
| **This carrier is found to drift from its sources or sibling navigation** | Reconcile against the source PDFs for wording and current repository evidence for implementation; preserve prior carrier state for rollback. |
| **This carrier is found to overclaim implementation** | Demote to `PROPOSED` / `UNKNOWN`; never resolve drift by lowering the truth label. |

**Rollback target:** `ROLLBACK_TARGET_TBD` (PROPOSED: prior commit ref of this file as recorded in `release/manifests/`).

> **Expected lifespan:** this file's job is **bridge state**, not destination state. Its expected lifespan is from authorship to ADR resolution. If the ADR is filed soon, this file is short-lived by design. If the ADR is delayed, this file persists with `CONFLICTED` status documented in §3.

---

## 11. Source ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated Atlas.md` (full-text source-derived carrier) | `CONFIRMED file presence` | §5 routing row; §6 at-a-glance metadata. | Closest repository carrier for converted source wording; not implementation authority. |
| `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` (navigation twin) | `CONFIRMED file presence` | §4 twin-relationship table; §5 routing row; §6 at-a-glance metadata source. | Twin has the depth; its source claims remain bounded. |
| `docs/atlases/receipt-catalog.md` meta-block `related:` field | `CONFIRMED file presence` | §2 prior dangling-reference row. | Related path now resolves to the actual root carrier. |
| `docs/atlases/pipeline-gate-reference.md` meta-block `related:` field | `CONFIRMED file presence` | §2 prior dangling-reference row. | Related path now resolves to the actual root carrier. |
| `docs/atlases/maplibre-master.md` meta-block `related:` field | `CONFIRMED file presence` | §2 prior dangling-reference row. | Related path now resolves to the actual root carrier. |
| `docs/atlases/domains-atlas-v1.1.md` §12 (naming reconciliation) | `CONFIRMED file presence`; internal proposal status retained | §3 seven-name catalog; identifies resolution directions. | Naming decision remains unresolved. |
| Atlas v1.1 front matter (cover supersession block; "What is new in v1.1"; conflict rule; non-collapse rule) | `CONFIRMED doctrine` | §6 conflict rule, non-collapse rule, reversibility rows. | Wording is reproduced in the doctrinal twin at greater length. |
| Pass 32 totals from full-text Markdown §7 ("Change Summary for Pass 32") | `CONFIRMED doctrine` | §6 Pass 32 card-totals row. | — |
| Directory Rules v2 and accepted ADR-0029 | Current placement governance | §10 migration and supersession boundary. | Names `docs/atlases/` as the proposed canonical collection; does not decide this pointer's disposition. |
| `kfm_unified_doctrine_synthesis.md` | Source-lineage filename | Historical doctrine-consistency context. | Not present under this filename in the current repository; not current authority. |

> **Memory is not evidence.** Every consequential claim in this file is traceable to one of the sources above, an Atlas table reproduced via the doctrinal twin, or an explicit `PROPOSED` / `NEEDS VERIFICATION` / `CONFLICTED` placeholder. The atlas-Markdown naming ADR is the resolution path for the `CONFLICTED` items.

---

<p align="right"><a href="#kfm-domains-v11--pass-2332-consolidated-atlas--carrier-underscored-variant">↑ Back to top</a></p>
