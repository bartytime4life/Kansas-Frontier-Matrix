<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/habitat/source-families
title: Habitat Domain — Source Family Dossiers
type: standard
version: v1
status: draft
owners: <habitat-domain-steward>, <source-steward>, <rights-reviewer>, <docs-steward>   # placeholders pending owner-registry verification
created: 2026-06-05
updated: 2026-06-05
policy_label: public
contract_version: "3.0.0"   # pinned per ai-build-operating-contract.md
related:
  - docs/domains/habitat/SOURCES.md
  - docs/domains/habitat/README.md
  - docs/domains/habitat/SENSITIVITY.md
  - docs/domains/habitat/RELEASE_INDEX.md
  - docs/domains/habitat/REASON_CODES.md
  - docs/domains/fauna/README.md
  - docs/doctrine/evidence-first.md
  - docs/doctrine/directory-rules.md
  - data/registry/sources/habitat/
  - schemas/contracts/v1/source/source-descriptor.json
  - ai-build-operating-contract.md
tags: [kfm, domain:habitat, sources, source-families, source-descriptor, dossier, rights, governance]
notes:
  - "Per-family DEEP DOSSIERS. Companion to docs/domains/habitat/SOURCES.md (the one-row-per-family index). This doc holds one detailed profile per source family; SOURCES.md stays the lightweight index. Division of responsibility recorded in §1 and OQ-HAB-SF-01."
  - "Navigation/explainer doc. The append-only authority is the SourceDescriptor records under data/registry/sources/; this doc explains, it does not own descriptors."
  - "Source-role labels use the CONFIRMED 7-role enum (Atlas §24.1.1). Role assignments are PROPOSED per family/product, pending rights/terms verification; role is set at admission and never edited in-place."
  - "Per-family descriptor fields are drawn from CONFIRMED idea-cards (NWI 0008, PAD-US 0009, GAP/LANDFIRE 0010, NEON 0011, land-cover 0028, NatureServe 0023/IDEA-0009, freshness FEAT-0003)."
  - "Rights/terms for every family are NEEDS VERIFICATION; sensitive joins fail closed. No exact coordinates, tokens, or restricted-source-derived fields appear."
  - "Path uses Directory Rules §12 segment form; registry path form is OQ-HAB-SF-04. CONTRACT_VERSION = \"3.0.0\"."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌿 Habitat — Source Family Dossiers

> One detailed profile per Habitat source family: what it is, the source-role it carries, the descriptor fields it must capture, how it is ingested and diffed, what it crosswalks to, its sensitivity gate, and its freshness expectation. The companion [`SOURCES.md`](SOURCES.md) is the one-row-per-family index; **this is the deep dive.**

<p align="center">
  <b>One dossier per family · Native classification preserved · Crosswalks advisory · Rights known or held</b>
</p>

![status](https://img.shields.io/badge/status-draft-yellow)
![domain](https://img.shields.io/badge/domain-habitat-2E7D32)
![role](https://img.shields.io/badge/role-source_dossiers-lightgrey)
![families](https://img.shields.io/badge/families-8_core_%2B_adjacent-blue)
![rights](https://img.shields.io/badge/rights-NEEDS_VERIFICATION-orange)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![meta](https://img.shields.io/badge/meta-KFM__v2-lightgrey)
<!-- TODO: replace static badges with CI-driven Shields endpoints once owners + registry are verified (NEEDS VERIFICATION). -->

**Status:** draft &middot; **Owners:** habitat steward · source steward · rights reviewer · docs steward *(placeholders)* &middot; **Contract:** `CONTRACT_VERSION = "3.0.0"` &middot; **Last updated:** 2026-06-05

> [!IMPORTANT]
> **This is the dossier set, not the registry and not the index.** The authoritative `SourceDescriptor` records are append-only under `data/registry/sources/`. The one-row summary lives in [`SOURCES.md`](SOURCES.md). This doc holds the *detailed profile* of each family. If this doc and a descriptor disagree, the **descriptor wins**; open a `DRIFT_REGISTER` entry. **(CONFIRMED doctrine — registry is append-only authority.)**

---

## Contents

1. [Purpose & division from SOURCES.md](#1-purpose--division-from-sourcesmd)
2. [Dossier template](#2-dossier-template)
3. [USFWS ECOS / critical habitat](#3-usfws-ecos--critical-habitat)
4. [KDWP state review](#4-kdwp-state-review)
5. [NLCD land cover](#5-nlcd-land-cover)
6. [NWI wetlands](#6-nwi-wetlands)
7. [GAP / LANDFIRE](#7-gap--landfire)
8. [NatureServe & controlled biodiversity](#8-natureserve--controlled-biodiversity)
9. [GBIF / iNaturalist / iDigBio occurrence](#9-gbif--inaturalist--idigbio-occurrence)
10. [PAD-US stewardship context](#10-pad-us-stewardship-context)
11. [Adjacent context-fabric families](#11-adjacent-context-fabric-families)
12. [Cross-family crosswalk posture](#12-cross-family-crosswalk-posture)
13. [Open questions register](#13-open-questions-register)
14. [Open verification backlog](#14-open-verification-backlog)
15. [Changelog & definition of done](#15-changelog--definition-of-done)
16. [Related docs](#16-related-docs)

---

## 1. Purpose & division from SOURCES.md

These two source docs split cleanly and MUST stay split.

| Concern | Lives in | This doc |
|---|---|---|
| One-row-per-family index (role, rights posture, freshness at a glance) | [`SOURCES.md`](SOURCES.md) | Summarized only, cross-linked. |
| SourceDescriptor model, admission gates A–C, registry homes | [`SOURCES.md`](SOURCES.md) | Referenced, not restated. |
| Per-family deep profile: descriptor fields, ingest/diff strategy, crosswalk, sensitivity gate, freshness | this doc | Authoritative depth. |

> [!NOTE]
> Each dossier below is **descriptive**, not the descriptor itself. The `SourceDescriptor` model and the admission gates are defined once in `SOURCES.md`; the dossiers here apply that model to each family. Keep the role/rights/freshness *facts* single-sourced — if a dossier and the index disagree, that is a drift defect (OQ-HAB-SF-01). **(CONFIRMED that an index/dossier split is appropriate; PROPOSED for every concrete path until mounted-repo verification.)**

[⬆ back to top](#top)

---

## 2. Dossier template

Each family dossier uses the same shape so they are comparable. Role labels use the **CONFIRMED 7-role enum** (`observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`); assignments are **PROPOSED per family/product**.

- **What it is** — one-line identity.
- **Source-role (PROPOSED)** — enum value + why.
- **Descriptor fields** — the family-specific fields its `SourceDescriptor` must capture (CONFIRMED card where one exists).
- **Habitat use** — what Habitat does with it.
- **Ingest & diff** — admission and change-tracking posture.
- **Crosswalk** — native classification + advisory crosswalk.
- **Sensitivity gate** — the fail-closed condition.
- **Freshness** — cadence and watch note.
- **Evidence** — the CONFIRMED card(s) backing the dossier.

[⬆ back to top](#top)

---

## 3. USFWS ECOS / critical habitat

- **What it is.** Federal critical-habitat designations and species data from USFWS ECOS services.
- **Source-role (PROPOSED).** `regulatory` — a legal designation, never an observation or a model. **MUST NOT** be collapsed with modeled habitat (`CRITICAL_HABITAT_FRAMING` denial; Atlas §24.1.2).
- **Descriptor fields.** `role_authority` = USFWS (required for `regulatory`); designation type; species reference; product version; service URI; rights.
- **Habitat use.** Regulatory critical-habitat overlay; never framed as modeled suitability.
- **Ingest & diff.** Service pull; designation-change diff. A designation change may trigger a downstream `CorrectionNotice`.
- **Crosswalk.** Species reference crosswalks to Fauna taxonomy (Fauna-owned); Habitat does not own taxon truth.
- **Sensitivity gate.** Public designation, **but** any join that narrows a sensitive occurrence fails closed (deny → geoprivacy + receipts + review).
- **Freshness.** Cadence varies; designation-change watch.
- **Evidence.** Habitat dossier §D; anti-collapse register Atlas §24.1.2.

> [!CAUTION]
> Regulatory ≠ modeled. A modeled suitability surface served or framed as a USFWS critical-habitat determination is a `ROLE_COLLAPSE` / `CRITICAL_HABITAT_FRAMING` denial. **(CONFIRMED — Atlas §24.1.2; see [`REASON_CODES.md`](REASON_CODES.md).)**

[⬆ back to top](#top)

---

## 4. KDWP state review

- **What it is.** Kansas Department of Wildlife & Parks state review context — SGCN lists, state designations, survey context.
- **Source-role (PROPOSED).** **Per product:** `regulatory` for state designations; `observed` for survey observations. A single provider yields multiple descriptors, one role each.
- **Descriptor fields.** `role_authority` = KDWP (when regulatory); product type; designation vs survey flag; rights; steward terms.
- **Habitat use.** State wildlife review context; SGCN-linked habitat context.
- **Ingest & diff.** Steward-mediated; rights/terms **NEEDS VERIFICATION** before any admission.
- **Crosswalk.** State designations crosswalk to federal (USFWS) and Fauna taxonomy where applicable.
- **Sensitivity gate.** May carry sensitive SGCN locations → **deny-by-default on join** until geoprivacy + receipts + review.
- **Freshness.** Designation/list cadence varies.
- **Evidence.** Habitat dossier §D; Fauna dossier §D (KDWP-like steward sources).

[⬆ back to top](#top)

---

## 5. NLCD land cover

- **What it is.** National Land Cover Database — multi-year, broad remotely-sensed land-cover classification.
- **Source-role (PROPOSED).** `observed` — a remotely-sensed classification product.
- **Descriptor fields.** Product version/vintage; classification scheme; raster form; source URI; rights.
- **Habitat use.** Land-cover basis for habitat patches and suitability inputs.
- **Ingest & diff.** Periodic national-release pull; diff on new vintage; never silently overwrite a prior vintage.
- **Crosswalk.** Native NLCD classes preserved; crosswalk to a common land-cover vocabulary is **advisory, not authoritative** (crosswalks are inherently lossy).
- **Sensitivity gate.** Low intrinsic sensitivity; sensitivity arises on join to a sensitive occurrence.
- **Freshness.** Multi-year releases (vintage-specific).
- **Evidence.** KFM-P2-IDEA-0028 (CONFIRMED — NLCD among CDL/NLCD/LANDFIRE/GAP land-cover authorities, native classification preserved + crosswalk).

[⬆ back to top](#top)

---

## 6. NWI wetlands

- **What it is.** National Wetlands Inventory — federal wetlands mapping (US Fish & Wildlife Service Wetlands Mapper).
- **Source-role (PROPOSED).** `observed` — a wetlands-inventory observation product; federal wetlands source role.
- **Descriptor fields (CONFIRMED card KFM-P25-PROG-0008).** Wetlands Mapper metadata; **Cowardin class fields**; download/service URI; **project delta strategy**; federal wetlands source role.
- **Habitat use.** Wetlands extent and Cowardin classes as habitat support (riparian/wetland habitat).
- **Ingest & diff.** Wetlands Mapper service; project delta strategy per descriptor.
- **Crosswalk.** Cowardin classification preserved; advisory crosswalk to habitat vocabulary where applicable.
- **Sensitivity gate.** Low intrinsic sensitivity; arises on join.
- **Freshness.** Mapper updates; delta-strategy-driven.
- **Evidence.** KFM-P25-PROG-0008 (CONFIRMED card / PROPOSED descriptor shape).

[⬆ back to top](#top)

---

## 7. GAP / LANDFIRE

- **What it is.** USGS GAP (Gap Analysis Program, biodiversity-focused) and LANDFIRE (fire-related land cover) — modeled vegetation / land-cover and ecological-system products.
- **Source-role (PROPOSED).** `modeled` — modeled products; require `role_model_run_ref → ModelRunReceipt` and a paired uncertainty surface.
- **Descriptor fields (CONFIRMED card KFM-P25-PROG-0010).** Ecological system **or USNVC classification**; product version; **raster/vector form**; source URI; thematic role.
- **Habitat use.** Ecological systems and modeled vegetation for `EcologicalSystem` and suitability inputs.
- **Ingest & diff.** Periodic modeled-release pull; a new model run = a new `ModelRunReceipt`.
- **Crosswalk.** USNVC / ecological-system classification preserved; advisory crosswalk only.
- **Sensitivity gate.** Modeled; must carry model identity + uncertainty; framing-as-regulatory denied (`MODEL_LABEL_COLLAPSE`).
- **Freshness.** Periodic modeled releases.
- **Evidence.** KFM-P25-PROG-0010; KFM-P2-IDEA-0028 (LANDFIRE/GAP among land-cover authorities).

> [!CAUTION]
> GAP/LANDFIRE are **modeled**, not observed. A GAP/LANDFIRE surface released without a `ModelRunReceipt` + `UncertaintySurface`, or framed as observation, is a `UNCERTAINTY_MISSING` / `MODEL_LABEL_COLLAPSE` failure. **(CONFIRMED — Atlas §24.1.2; [`REASON_CODES.md`](REASON_CODES.md).)**

[⬆ back to top](#top)

---

## 8. NatureServe & controlled biodiversity

- **What it is.** NatureServe / Natural Heritage conservation ranks, ecological-system definitions, and controlled rare-data.
- **Source-role (PROPOSED).** `aggregate` — heritage rankings and aggregated assessments; require `role_aggregation_unit`.
- **Descriptor fields.** Rank type; ecological-system definition reference; **access-control class**; license terms; public-safe-derivative rule; `role_aggregation_unit`.
- **Habitat use.** Conservation ranks and ecological-system definitions; rare-data context (gated).
- **Ingest & diff.** **Access-gated** controlled release; re-check rights on each release.
- **Crosswalk.** Ecological-system definitions inform GAP/LANDFIRE systems; advisory.
- **Sensitivity gate.** **Rare-data access controls, redaction, license checks, and public-safe-derivative rules required** before any public exposure. Species-by-county / community-composition matrices only when rights and sensitivity controls are explicit.
- **Freshness.** Controlled releases; rights re-check each cycle.
- **Evidence.** KFM-P25-PROG-0023 (CONFIRMED — NatureServe rare-data access gate); KFM-P25-IDEA-0009 (biodiversity matrix backbone, rights/sensitivity explicit).

> [!CAUTION]
> NatureServe rare-data is **access-gated and restricted-source**. No exact rare-species location, access token, or restricted-source-derived field appears in this doc; the gate and the public-safe-derivative rule are governed in `policy/` (see [`SENSITIVITY.md`](SENSITIVITY.md)). Rights for this family are **NEEDS VERIFICATION** and an access agreement is likely required. **(Sensitive-source discipline.)**

[⬆ back to top](#top)

---

## 9. GBIF / iNaturalist / iDigBio occurrence

- **What it is.** Biodiversity occurrence aggregators (GBIF, iNaturalist, iDigBio).
- **Source-role (PROPOSED).** `observed` — occurrence observations. *(Fauna owns occurrence truth; Habitat consumes occurrence context.)*
- **Descriptor fields.** Darwin Core terms; per-record license; **`geoprivacy_status`**; `public_safe_geometry`; source URI.
- **Habitat use.** Occurrence context joined to habitat — **geoprivacy-bound** at all times.
- **Ingest & diff.** Continuous/per-record; geoprivacy status re-checked on ingest.
- **Crosswalk.** STAC × Darwin Core hybrid (KFM-P1-PROG-0022): generalizes or suppresses sensitive coordinates before public display and carries transform receipts.
- **Sensitivity gate.** Sensitive coordinates generalized/suppressed before any public display; `public_safe_geometry` required when `geoprivacy_status ∈ {obscured, private, generalized}` (`JOIN_SENSITIVE_OCCURRENCE`).
- **Freshness.** Continuous; per-record.
- **Evidence.** KFM-P1-PROG-0022 (CONFIRMED — STAC × Darwin Core geoprivacy hybrid); Fauna dossier §D (aggregators).

> [!CAUTION]
> Occurrence inputs are the highest-sensitivity Habitat source. Habitat **never** publishes an occurrence-linked product at finer resolution than the generalized Fauna geoprivacy product. **(CONFIRMED — Atlas §20.5 deny-by-default; [`SENSITIVITY_AND_GEOPRIVACY.md`](SENSITIVITY_AND_GEOPRIVACY.md).)**

[⬆ back to top](#top)

---

## 10. PAD-US stewardship context

- **What it is.** USGS Protected Areas Database of the US — protected-area / easement boundaries and stewardship context.
- **Source-role (PROPOSED).** `administrative` — a protected-area/easement compilation, not an observed event.
- **Descriptor fields (CONFIRMED card KFM-P25-PROG-0009).** Protected-area/easement **version**; **GAP-status fields**; **boundary-diff strategy**; rights; source URI.
- **Habitat use.** Protected-area / easement / stewardship-zone context for `StewardshipZone`.
- **Ingest & diff.** Versioned releases; boundary-diff strategy per descriptor.
- **Crosswalk.** GAP-status fields inform stewardship classification; advisory.
- **Sensitivity gate.** Administrative boundaries are generally public; **tribal/sovereign stewardship zones may withhold** (rights-holder / sovereignty review; `STEWARD_ZONE_OVERRIDE`).
- **Freshness.** Versioned protected-area releases.
- **Evidence.** KFM-P25-PROG-0009 (CONFIRMED card / PROPOSED descriptor shape).

[⬆ back to top](#top)

---

## 11. Adjacent context-fabric families

These families are named in the project source idea-set as landscape context layers that *may* be admitted as Habitat context — each as **versioned context with a source role, not a sovereign truth root.** Scope and ownership are **PROPOSED** (OQ-HAB-SF-03).

<details>
<summary><b>Adjacent context-fabric dossiers (PROPOSED) — expand</b></summary>

| Family | What it is | Role (PROPOSED) | Descriptor / evidence note |
|---|---|---|---|
| **NEON** | National Ecological Observatory Network ecological products. | `observed` (Released) / `candidate` (Provisional) | Descriptor distinguishes **Released** products with citable DOI from **Provisional** products that may change (KFM-P25-PROG-0011). |
| **USDA CDL** | Cropland Data Layer — annual, crop-focused land cover. | `observed` | Land-cover authority alongside NLCD/LANDFIRE/GAP; native classification preserved + advisory crosswalk (KFM-P2-IDEA-0028). |
| **EPA ecoregions / PLSS / WBD HUC12** | Landscape context fabric (ecoregion, survey units, watershed boundaries). | `administrative` | Catalogued as context layers with source roles, not interchangeable geometry truth (KFM-P25-IDEA-0011). |
| **USDA PLANTS / VegBank / herbaria** | Species-by-county and community-composition matrices. | `aggregate` / `observed` (per product) | Rights and sensitivity must be explicit; **taxonomy ownership routes to Flora** (KFM-P25-IDEA-0009). |

</details>

> [!NOTE]
> NEON's Released-vs-Provisional split is a useful general pattern: a **Provisional** product behaves like a `candidate` source (no PUBLISHED edge until it stabilizes), while a **Released** product with a citable DOI behaves like `observed`. **(CONFIRMED card KFM-P25-PROG-0011.)**

[⬆ back to top](#top)

---

## 12. Cross-family crosswalk posture

Multiple land-cover authorities cover complementary needs (CDL annual/crop, NLCD multi-year/broad, LANDFIRE fire, GAP biodiversity). The CONFIRMED posture:

- **Preserve each native classification.** Never overwrite a source's own scheme.
- **Crosswalks are advisory, not authoritative.** Class crosswalks are inherently lossy; they inform, they do not replace.
- **Per-source primary; unified secondary.** Produce per-source artifacts as primary; a unified land-cover product is a **research-derived artifact with caveats**, never a sovereign truth root.

**(CONFIRMED — KFM-P2-IDEA-0028; consistent with KFM-P25-IDEA-0004 "versioned context, not sovereign truth roots.")**

[⬆ back to top](#top)

---

## 13. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-HAB-SF-01 | Keep `SOURCE_FAMILIES.md` (dossiers) and `SOURCES.md` (index) split, or merge? Keep role/rights/freshness facts single-sourced. | Docs steward + source steward | DRIFT_REGISTER decision; single-source the shared facts. |
| OQ-HAB-SF-02 | Confirm per-family role assignments (esp. KDWP regulatory-vs-observed split; NatureServe aggregate). | Source steward | Registry inspection; per-product descriptors. |
| OQ-HAB-SF-03 | Which adjacent families (NEON, CDL, EPA/PLSS/WBD, PLANTS/VegBank) are in Habitat scope vs Fauna/Flora/Hydrology. | Domain stewards | Cross-lane ownership review; ADR-S-14. |
| OQ-HAB-SF-04 | Registry path form: `data/registry/sources/habitat/` vs `data/registry/habitat/`. | Directory steward | Per-root README. (Same as OQ-HAB-SRC-05 / OQ-HAB-REL-05.) |
| OQ-HAB-SF-05 | NatureServe access-gate terms and public-safe-derivative rules. | Rights + sensitivity reviewer | Source agreement; `policy/rights/` + `policy/sensitivity/`. |
| OQ-HAB-SF-06 | Per-family descriptor field names (vs the PROPOSED idea-card shapes here). | Schema steward | Schema PR; ADR-0001. |

[⬆ back to top](#top)

---

## 14. Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Reconciliation/division with `SOURCES.md` (OQ-HAB-SF-01) — shared facts single-sourced.
2. Presence and contents of each family's `SourceDescriptor` under `data/registry/sources/habitat/`.
3. Rights/terms for all families (Gate B) — none resolved in this docs-only pass.
4. Per-family role assignments confirmed against admitted descriptors (OQ-HAB-SF-02).
5. Per-family descriptor field names vs the PROPOSED card shapes (OQ-HAB-SF-06).
6. NatureServe access-gate and occurrence geoprivacy bindings (OQ-HAB-SF-05).
7. Adjacent-family scope/ownership (OQ-HAB-SF-03).
8. Registry path form (OQ-HAB-SF-04) and the HAB-V-009 path-form conflict.

[⬆ back to top](#top)

---

## 15. Changelog & definition of done

### 15.1 Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial Habitat source-family dossiers (one deep profile per family). | new | Created per explicit user instruction (per-family deep dossiers, distinct from the SOURCES.md index). |
| Established the index/dossier division from `SOURCES.md` (§1) with a single-source-the-facts rule (OQ-HAB-SF-01). | gap closure | Avoids parallel-authority drift between the two source docs. |
| Grounded each dossier in its CONFIRMED descriptor card (NWI 0008, PAD-US 0009, GAP/LANDFIRE 0010, NEON 0011, land-cover 0028, NatureServe 0023 / IDEA-0009, freshness FEAT-0003). | clarification | Each profile is evidence-backed, not padded. |
| Applied the CONFIRMED 7-role enum per family (PROPOSED per product); USFWS = regulatory, NLCD/NWI/occurrence = observed, GAP/LANDFIRE = modeled, NatureServe = aggregate, PAD-US = administrative. | reconciliation | Consistent with SOURCES.md §4 and the README / Reason Codes / Release Index corrections. |
| Added cross-family crosswalk posture (§12) and adjacent context-fabric dossiers (§11, `<details>`). | gap closure | Captures the CONFIRMED preserve-native / advisory-crosswalk / per-source-primary rule. |
| Pinned `CONTRACT_VERSION = "3.0.0"`; used Directory Rules §12 segment path; stated no exact coordinates / tokens / restricted-source fields. | housekeeping / safety | Required for doctrine-adjacent docs; sensitive-source discipline. |

> **Backward compatibility.** New document — no prior anchors. Companion to `SOURCES.md`; the two must keep shared facts single-sourced (OQ-HAB-SF-01).

### 15.2 Definition of done

This document is done enough to enter the repository when:

- the division from `SOURCES.md` is confirmed (OQ-HAB-SF-01) and role/rights/freshness facts are single-sourced across the two;
- it is placed per Directory Rules §12, with the registry path form (OQ-HAB-SF-04) and HAB-V-009 logged in `docs/registers/DRIFT_REGISTER.md`;
- the source steward, rights reviewer, habitat domain steward, and docs steward review it;
- per-family role assignments are confirmed against admitted descriptors;
- rights/terms (Gate B) are resolved or each unresolved family is clearly marked NEEDS VERIFICATION and not asserted as admitted;
- it remains descriptive — confirmed at review that it states no exact coordinates, tokens, or restricted-source-derived fields;
- the `GENERATED_RECEIPT.json` planned in the PR is wired into CI with `contract_version: "3.0.0"`;
- future changes follow the operating contract's §37 lifecycle.

[⬆ back to top](#top)

---

## 16. Related docs

**All targets PROPOSED until confirmed against a mounted repo; path form follows Directory Rules §12.**

- [`docs/domains/habitat/SOURCES.md`](SOURCES.md) — the one-row-per-family **index** (companion to this dossier set).
- [`docs/domains/habitat/README.md`](README.md) — Habitat lane orientation (§3 source roles).
- [`docs/domains/habitat/SENSITIVITY.md`](SENSITIVITY.md) — sensitivity posture for occurrence-linked and restricted sources.
- [`docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md`](SENSITIVITY_AND_GEOPRIVACY.md) — geoprivacy mechanics for occurrence inputs.
- [`docs/domains/habitat/RELEASE_INDEX.md`](RELEASE_INDEX.md) — releases carry `source_roles` drawn from these families.
- [`docs/domains/habitat/REASON_CODES.md`](REASON_CODES.md) — `ROLE_COLLAPSE`, `CRITICAL_HABITAT_FRAMING`, `MODEL_LABEL_COLLAPSE`, `RIGHTS_UNKNOWN`.
- [`docs/domains/fauna/README.md`](../fauna/README.md) — Fauna owns occurrence truth; Habitat consumes occurrence context.
- [`docs/doctrine/evidence-first.md`](../../doctrine/evidence-first.md) — evidence-first / cite-or-abstain doctrine.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — §7.4 source schema home; §12 Domain Placement Law.
- `data/registry/sources/habitat/` — append-only descriptor authority *(CONFIRMED home / PROPOSED presence)*.
- `schemas/contracts/v1/source/source-descriptor.json` — `SourceDescriptor` schema *(CONFIRMED default home / PROPOSED presence)*.
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — gates A–G; canonical operating contract (`CONTRACT_VERSION = "3.0.0"`).

---

**Last updated:** 2026-06-05 &middot; **Status:** draft &middot; **Contract:** `CONTRACT_VERSION = "3.0.0"` &middot; **Role:** per-family dossiers (companion to SOURCES.md index) &middot; **Citation short-names:** [DOM-HAB], [DOM-HF], [DOM-FAUNA], [DOM-FLORA], [ENCY], [DIRRULES]

[⬆ back to top](#top)
