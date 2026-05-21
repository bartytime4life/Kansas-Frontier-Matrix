<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-readme
title: docs/sources/catalog/ — Source-to-Catalog Documentation Lane
type: readme
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward (CODEOWNERS NEEDS VERIFICATION)>
created: 2026-05-20
updated: 2026-05-20
supersedes: v0.1 (2026-05-20)
policy_label: public
related:
  - docs/sources/README.md
  - docs/standards/README.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - data/catalog/README.md
  - data/registry/sources/README.md
  - connectors/README.md
  - control_plane/source_authority_register.yaml
tags: [kfm, docs, sources, catalog, stac, dcat, prov, trust-membrane]
notes:
  - "PROPOSED path: docs/sources/catalog/ is not enumerated in directory-rules.md §6.1; see §1.1 below."
  - "Source-family inventory drawn from connectors/ §7.3 and per-domain Key source families tables in the Consolidated Atlas."
  - "v0.2 refresh: aligned with Pass-32 catalog extension fields (KFM-P3-IDEA-0004), added trust-membrane subsection, added per-family authoring tracker, expanded STAC appendix to include kfm:trust_class/run_receipt_ref/proof_ref/source_role."
[/KFM_META_BLOCK_V2] -->

# `docs/sources/catalog/`

> Human-facing documentation for **how KFM source families become catalog entries** — the explanatory lane between `connectors/`, `data/registry/sources/`, and `data/catalog/{stac,dcat,prov,domain}/`.

[![Status: draft](https://img.shields.io/badge/status-draft-orange)](#5-status)
[![Edition: v0.2](https://img.shields.io/badge/edition-v0.2-blue)](#22-changelog)
[![Authority: docs-companion](https://img.shields.io/badge/authority-docs--companion-blue)](#4-authority-level)
[![Truth posture: cite--or--abstain](https://img.shields.io/badge/truth--posture-cite--or--abstain-success)](../../doctrine/truth-posture.md)
[![Lifecycle: RAW→WORK→PROCESSED→CATALOG→PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92WORK%E2%86%92PROCESSED%E2%86%92CATALOG%E2%86%92PUBLISHED-informational)](../../doctrine/lifecycle-law.md)
[![Trust membrane: governed--api](https://img.shields.io/badge/trust--membrane-governed--api-2b6cb0)](../../doctrine/trust-membrane.md)
[![Last reviewed: 2026-05-20](https://img.shields.io/badge/last%20reviewed-2026--05--20-lightgrey)](#last-reviewed)
<!-- TODO: replace CI badge with a working Shields.io endpoint once the docs lint workflow is wired -->
[![CI: docs lint](https://img.shields.io/badge/CI-NEEDS%20VERIFICATION-lightgrey)](#14-validation)

**Status:** draft &nbsp;·&nbsp; **Edition:** v0.2 &nbsp;·&nbsp; **Owners:** `<PLACEHOLDER — Docs steward + Source steward>` &nbsp;·&nbsp; **Last reviewed:** 2026-05-20

---

## Contents <a id="contents"></a>

- [1. Scope and path](#1-scope-and-path)
- [2. Repo fit](#2-repo-fit)
- [3. Purpose](#3-purpose)
- [4. Authority level](#4-authority-level)
- [5. Status](#5-status)
- [6. What belongs here](#6-what-belongs-here)
- [7. What does NOT belong here](#7-what-does-not-belong-here)
- [8. Directory tree (PROPOSED)](#8-directory-tree-proposed)
- [9. Flow — source → catalog → published](#9-flow--source--catalog--published)
- [10. Source families indexed here](#10-source-families-indexed-here)
- [11. Catalog profiles and identity conventions](#11-catalog-profiles-and-identity-conventions)
- [12. Trust membrane discipline](#12-trust-membrane-discipline)
- [13. Inputs](#13-inputs)
- [14. Outputs](#14-outputs)
- [15. Validation](#15-validation)
- [16. Review burden](#16-review-burden)
- [17. Authoring guide for a per-family page](#17-authoring-guide-for-a-per-family-page)
- [18. Per-family authoring status](#18-per-family-authoring-status)
- [19. Related folders and docs](#19-related-folders-and-docs)
- [20. ADRs](#20-adrs)
- [21. Open questions](#21-open-questions)
- [22. Changelog](#22-changelog)
- [23. FAQ](#23-faq)
- [24. Appendix — minimal STAC `kfm:provenance` shape](#24-appendix--minimal-stac-kfmprovenance-shape)
- [Last reviewed](#last-reviewed)

---

## 1. Scope and path

This folder is the **human-readable, source-oriented view of catalog closure**. For each source family KFM ingests — USGS, FEMA, NOAA, NRCS, Kansas, GBIF, iNaturalist, Census, `local_upload`, and others — this lane explains:

- which **catalog profiles** the family lands in (STAC, DCAT, PROV-O, or the domain projection in `data/catalog/domain/`);
- what the **identity, namespace, and provenance** conventions are for that family's entries;
- which **policy, rights, and sensitivity** considerations gate publication;
- where to find the **machine-readable contracts, schemas, and validators** that the documentation here only narrates.

> [!IMPORTANT]
> **PROPOSED path.** `docs/sources/` is enumerated in `directory-rules.md` §6.1 as *"source-descriptor standards, source families."* A `catalog/` subfolder beneath it is **not** explicitly listed there. This README assumes the subfolder is the natural docs-side companion to `data/catalog/`'s `stac/ · dcat/ · prov/ · domain/` lanes. **Confirmation required** in a per-root note in `docs/sources/README.md` or via the path-validation checklist (`directory-rules.md` §16). See [§21 OPEN-DSC-01](#21-open-questions).

### 1.1 Two interpretations on the table

| Interpretation | What this folder would hold | Status |
|---|---|---|
| **A. Source-perspective catalog companion** *(adopted in this README)* | Per-family pages explaining how each source family lands in `data/catalog/{stac,dcat,prov,domain}/`, with identity, provenance, and rights notes. | PROPOSED |
| **B. Catalog-of-source-families index** | A flat index of all source families KFM consumes, with cross-links to connectors and registries. | PROPOSED — alternative |

Interpretation A is adopted because it is the gap not already filled by `docs/sources/README.md` (orientation), `connectors/README.md` (fetch/admission), or `data/catalog/README.md` (artifact-side layout). The two interpretations may also merge if [§21 OPEN-DSC-02](#21-open-questions) is resolved in that direction.

[↑ Back to top](#contents)

---

## 2. Repo fit

```
repo root
└── docs/
    ├── README.md
    ├── doctrine/
    │   ├── directory-rules.md           ← placement authority
    │   ├── trust-membrane.md            ← public-path discipline
    │   └── lifecycle-law.md             ← RAW → … → PUBLISHED
    ├── standards/                       ← STAC, DCAT, PROV, PMTILES, OGC-API-TILES, …
    │   ├── README.md
    │   └── …
    └── sources/                         ← parent: source-descriptor standards, source families
        ├── README.md                    ← orientation for the sources lane
        └── catalog/                     ← THIS FOLDER (PROPOSED)
            ├── README.md                ← this file
            └── <source-family>/         ← per-family catalog notes (PROPOSED)
```

**Upstream:** `docs/sources/README.md` (orientation), `docs/standards/` (external spec profiles), `docs/doctrine/directory-rules.md` (placement), `docs/doctrine/trust-membrane.md` (public-path discipline).
**Downstream:** `data/catalog/{stac,dcat,prov,domain}/` (the artifacts these docs describe), `data/registry/sources/` (machine-readable source descriptors).

[↑ Back to top](#contents)

---

## 3. Purpose

A reader who lands here should be able to:

1. Find the **per-family page** for the source they care about (e.g. USGS, GBIF).
2. Learn which **catalog profile(s)** that family uses (STAC, DCAT, PROV-O, domain projection).
3. See the **identity and namespace conventions** (`kfm:provenance`, `kfm:trust_class`, `kfm:source_role`, Collection-id pattern, asset roles, `file:checksum`).
4. Read the **rights / sensitivity disposition** for that family and where the corresponding policy gates live.
5. Click through to the **contracts, schemas, validators, and ADRs** that machine-enforce what the docs here narrate.

This README is **documentation, not authority**. It does not decide whether a source is admissible, what its rights state is, or which profile is canonical for a given artifact type — those decisions live in `contracts/`, `policy/`, `data/registry/sources/`, and the ADR index.

[↑ Back to top](#contents)

---

## 4. Authority level

**Authority level:** `docs-companion` — explanatory only.

`docs/sources/catalog/` does not own placement, contracts, schemas, or policy. It narrates and indexes what those layers decide. Per `directory-rules.md` §2.3, this folder is **out of scope** for object-family meaning, field shape, admissibility, or source identity decisions.

| Concern | Owner (canonical) |
|---|---|
| Source identity, rights, sensitivity | `data/registry/sources/`, `policy/sensitivity/` |
| Object-family meaning | `contracts/` |
| Field-level shape | `schemas/contracts/v1/...` (default schema home per ADR-0001) |
| Allow / deny / restrict / abstain | `policy/` |
| Catalog artifact layout | `data/catalog/` |
| External standard profiles (STAC, DCAT, PROV, …) | `docs/standards/` |
| Public-path discipline | `docs/doctrine/trust-membrane.md`, `apps/governed-api/` |
| **This folder** | **Source-family explanation and cross-linking** |

[↑ Back to top](#contents)

---

## 5. Status

**Status:** PROPOSED.

| Aspect | Label | Basis |
|---|---|---|
| The `docs/sources/catalog/` path | PROPOSED | Not enumerated in `directory-rules.md` §6.1; see [§21](#21-open-questions). |
| Per-family page convention | PROPOSED | Pattern in [§17](#17-authoring-guide-for-a-per-family-page) is illustrative until adopted. |
| Connector inventory (USGS, FEMA, NOAA, NRCS, Kansas, GBIF, iNaturalist, Census, `local_upload`) | CONFIRMED (in doctrine corpus) | `directory-rules.md` §7.3; mounted-repo presence NEEDS VERIFICATION. |
| `data/catalog/{stac,dcat,prov,domain}/` lanes | CONFIRMED (in doctrine corpus) | `directory-rules.md` §6.5 and lifecycle phase rules. |
| STAC `kfm:provenance` namespace contents | CONFIRMED (doctrine) | Pass-10 idea index, C4-01. |
| KFM catalog extensions `kfm:run_receipt_ref`, `kfm:proof_ref`, `kfm:trust_class`, `kfm:source_role` | CONFIRMED (doctrine) | Atlas Pass-32 §8.7.62 (KFM-P3-IDEA-0004). |
| Repository implementation maturity (this lane) | UNKNOWN | No mounted repo inspected in this authoring session. |

[↑ Back to top](#contents)

---

## 6. What belongs here

- **Per-source-family pages** (one Markdown file per family, or one folder per family if the family has many catalog products) describing how that family lands in `data/catalog/`.
- **Profile crosswalks** between the source's native vocabulary (e.g. DwC for biodiversity, GTFS for transit) and KFM's STAC/DCAT/PROV envelopes.
- **Identity-convention notes** — Collection-id patterns, asset-role conventions, `kfm:provenance` field expectations, `kfm:trust_class` and `kfm:source_role` declarations, `file:checksum` placement.
- **Rights and sensitivity narrative** that points at the actual `policy/sensitivity/` rules — never restates them.
- **Catalog-closure checklists** for the family (links into validators in `tools/validators/`, never duplicating their logic).
- **Cross-links** to `connectors/<family>/`, `data/registry/sources/<family>/`, `pipeline_specs/<domain>/`, and any related ADRs.

[↑ Back to top](#contents)

---

## 7. What does NOT belong here

> [!WARNING]
> Documentation in this lane MUST NOT become a parallel authority for any of the following. If a contributor's instinct is to put a fact here that is enforceable elsewhere, the fact belongs there with a link from here.

| Anti-pattern | Goes here instead |
|---|---|
| Source descriptors themselves (`SourceDescriptor` records) | `data/registry/sources/<domain>/` |
| Field-level schema (JSON Schema, Pydantic) | `schemas/contracts/v1/source/` (per ADR-0001, schema home) |
| Object-family contracts | `contracts/` |
| Rights and sensitivity rules (machine-enforceable) | `policy/sensitivity/`, `policy/sources/` |
| Connector code, fetchers, watchers | `connectors/<family>/`, `pipelines/watchers/` |
| Catalog artifacts (`*.json`, STAC items, DCAT distributions, PROV-O graphs) | `data/catalog/{stac,dcat,prov,domain}/` |
| External-spec definitions (STAC 1.1, DCAT-AP, PROV-O syntax) | `docs/standards/` |
| Operational runbooks (refresh, rollback drills) | `docs/runbooks/<domain>/` |
| Release decisions / manifests | `release/` |
| Validator logic (including the catalog-QA surface KFM-P27-FEAT-0004 and STAC Projection lint KFM-P27-FEAT-0003) | `tools/validators/` |
| Cited per-place truth claims | Catalog entries with EvidenceBundle, not narrative docs |

A page here that begins to dictate behavior is **drift**. Open a `docs/registers/DRIFT_REGISTER.md` entry and propose either deletion or migration.

[↑ Back to top](#contents)

---

## 8. Directory tree (PROPOSED)

> [!NOTE]
> As of **2026-05-20** the per-family folders below **exist** — the lane's flat per-source pages were reorganized into one folder per source family, and per-product pages have been scaffolded for every family. See [`INDEX.md`](./INDEX.md) for per-family product-page counts.

```text
docs/sources/catalog/
├── README.md                       # this file
├── INDEX.md                        # family navigation index
├── GLOSSARY.md   CROSSWALKS.md   PROFILES.md   IDENTITY.md   NAMING.md
├── RIGHTS-AND-SENSITIVITY-MAP.md   CARE-COMPLIANCE.md   COVERAGE-MATRIX.md
├── OPEN-QUESTIONS.md   CHANGELOG.md     # ← cross-cutting governance docs
├── _template/                      # SOURCE_FAMILY / SOURCE_PRODUCT / CROSSWALK / RIGHTS_NOTE
├── _examples/                      # illustrative STAC / DCAT / PROV-O payloads
│
│                                   # directory-rules.md §7.3 source families
├── usgs/README.md
├── fema/README.md
├── noaa/README.md
├── nrcs/README.md
├── kansas/                         # Kansas state-scoped sources
│   ├── README.md
│   ├── ksgs.md   kdwp.md   khri.md   kansas-memory.md
│   ├── kansas-state-archives.md   ksu-research-extension.md
│   └── ku-nhm.md   fhsu-sternberg.md
├── gbif/README.md
├── inaturalist/README.md
├── census/README.md
├── local_upload/README.md
│
│                                   # additional families — beyond §7.3, pending ADR
├── ahgp/   blm/   ebird/   eddmaps/   epa/   familysearch/   ftdna/
├── idigbio/   loc/   manual_curation/   natureserve/   newspapers/
├── openstreetmap/   usfws_ecos/
│                                   # connector-derived families (2026-05-21, OPEN-DSC-14)
└── nasa/   usda/   usdot/   openaq/   hifld/   isric/   drought_monitor/   landfire/
```

Nine of the folders above mirror the `connectors/` inventory in `directory-rules.md` §7.3 (CONFIRMED in doctrine corpus; sibling `connectors/<family>/` presence CONFIRMED in a mounted-repo session). The other twenty-two **exceed** the §7.3 nine — fourteen added by the 2026-05-20 reorganization and eight scaffolded 2026-05-21 from the `connectors/` inventory — and are tracked for ADR ratification in [§19](#19-open-questions) (`OPEN-DSC-09`–`OPEN-DSC-14`). A family folder SHOULD have a `connectors/<family>/` and `data/registry/sources/<family>/` companion.

[↑ Back to top](#contents)

---

## 9. Flow — source → catalog → published

The diagram below shows where this docs lane sits relative to the lifecycle. **Promotion is a governed state transition, not a file move** (`directory-rules.md` §3, lifecycle invariant). **Connectors do not publish.** They land bytes in `data/raw/...` or `data/quarantine/...` and emit ingest receipts; they MUST NOT write into `data/processed/`, `data/catalog/`, or `data/published/` (`directory-rules.md` §7.3).

```mermaid
flowchart LR
  subgraph EXT[External source]
    SRC[Source family<br/>USGS · FEMA · NOAA · NRCS · GBIF · …]
  end

  subgraph INT[Internal — NOT public]
    direction TB
    CONN[connectors/<br/>fetcher · watcher]
    RAW[(data/raw/<br/>+ ingest receipt)]
    WORK[(data/work/ ·<br/>data/quarantine/)]
    PROC[(data/processed/)]
  end

  subgraph CAT[data/catalog/ — governed boundary]
    direction TB
    STAC[stac/<br/>STAC Items + Collections]
    DCAT[dcat/<br/>DCAT Datasets + Distributions]
    PROV[prov/<br/>PROV-O activities]
    DOM[domain/<br/>domain projections]
  end

  subgraph REL[release/ + data/proofs/]
    REL_MAN[ReleaseManifest<br/>+ EvidenceBundle<br/>+ RollbackCard]
  end

  subgraph PUB[Public surfaces — released only]
    direction TB
    PUB_ART[(data/published/<br/>api_payloads · layers · pmtiles · …)]
    API[apps/governed-api/]
    UI[Map shell · Focus Mode · Review · Story]
  end

  SRC --> CONN --> RAW --> WORK --> PROC
  PROC --> STAC
  PROC --> DCAT
  PROC --> PROV
  PROC --> DOM
  STAC --> REL_MAN
  DCAT --> REL_MAN
  PROV --> REL_MAN
  DOM --> REL_MAN
  REL_MAN --> PUB_ART --> API --> UI

  classDef docsHere fill:#fff4cc,stroke:#b58a00,stroke-width:2px,color:#000;
  classDef internal fill:#fff3e0,stroke:#ef6c00,color:#bf360c;
  classDef public fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
  classDef invariant fill:#e6f0ff,stroke:#2b6cb0,color:#000;
  class CAT docsHere;
  class INT internal;
  class PUB public;
  class REL invariant;
```

`docs/sources/catalog/` (highlighted in yellow) is **the documentation lens onto the `data/catalog/` artifacts** — produced by pipelines, never written by connectors. The orange band is internal-only; the green band is public; the boundary between them is the trust membrane discussed in [§12](#12-trust-membrane-discipline).

[↑ Back to top](#contents)

---

## 10. Source families indexed here

The table below mirrors the connector inventory from `directory-rules.md` §7.3 (CONFIRMED in doctrine corpus). The "Catalog profiles" column is PROPOSED — confirm against the family's per-page documentation when authored.

| Source family | Typical domains | Catalog profiles likely used | Notes |
|---|---|---|---|
| `usgs/` | hydrology, geology, hazards | STAC · DCAT · PROV · domain | Earthquake catalog, NWIS water, NHDPlus context. |
| `fema/` | hazards | DCAT · PROV · domain | OpenFEMA, NFHL/MSC; rights / current terms **NEEDS VERIFICATION**. |
| `noaa/` | atmosphere, hazards | STAC · DCAT · PROV | Storm Events, NWS alerts, HMS Fire-and-Smoke. |
| `nrcs/` | soil, agriculture | DCAT · PROV · domain | SSURGO, gSSURGO, gNATSGO, SCAN. |
| `kansas/` | many (state-scoped) | STAC · DCAT · PROV · domain | Kansas Mesonet, KGS Geoportal, KHRI, KSHS Kansas Memory. |
| `gbif/` | fauna, flora | **STAC × Darwin Core hybrid** · DCAT | DwC terms under `properties.taxon`; redaction + sensitivity gates required. |
| `inaturalist/` | fauna, flora | **STAC × Darwin Core hybrid** · DCAT | Citizen-science cadence; provenance trail to observer; sensitivity gates required. |
| `census/` | settlements, people-DNA-land | DCAT · PROV · domain | Aggregate-cell discipline (no join from aggregate to single record). |
| `local_upload/` | any | DCAT · PROV (typically) | Curated uploads admitted via the trust membrane; rights review mandatory. |

For per-family rights, freshness, and sensitivity treatment, see the domain dossiers' *Key source families* sections in the Consolidated Atlas and the `data/registry/sources/` records when present.

### 10.1 Additional families (beyond §7.3)

Beyond the §7.3 nine, the lane carries **twenty-two** additional family folders — fourteen from the 2026-05-20 reorganization and eight scaffolded 2026-05-21 from the `connectors/` inventory. Promotion to a full §7.3 family (with a populated `connectors/` and `data/registry/sources/` companion) is gated on a per-family ADR — see [§19](#19-open-questions) `OPEN-DSC-09`–`OPEN-DSC-14`.

| Folder(s) | Source(s) | Deferral tracked in |
|---|---|---|
| `blm/`, `epa/` | Bureau of Land Management, EPA | OPEN-DSC-09 |
| `loc/`, `familysearch/`, `ahgp/`, `newspapers/` | Library of Congress, FamilySearch, AHGP, Newspapers | OPEN-DSC-10 |
| `ebird/`, `eddmaps/` | eBird, EDDMapS | OPEN-DSC-11 |
| `idigbio/`, `natureserve/`, `usfws_ecos/`, `ftdna/` | iDigBio, NatureServe, USFWS ECOS, Family Tree DNA | OPEN-DSC-12 |
| `openstreetmap/`, `manual_curation/` | OpenStreetMap, Manual Curation | OPEN-DSC-13 |
| `nasa/`, `usda/`, `usdot/`, `openaq/`, `hifld/`, `isric/`, `drought_monitor/`, `landfire/` | NASA, USDA, USDOT, OpenAQ, HIFLD, ISRIC, U.S. Drought Monitor, LANDFIRE | OPEN-DSC-14 |

[↑ Back to top](#contents)

---

## 11. Catalog profiles and identity conventions

These conventions are **doctrine-grounded** (Pass-10 idea index, category C4; Pass-32 §8.7.62, §8.7.71, §8.7.72) but their **implementation in any mounted repository is NEEDS VERIFICATION**. The narrative below is documentation; the enforceable form lives in `contracts/`, `schemas/`, and the validators in `tools/validators/`.

| Profile lane | Primary use | Identity / namespace pattern | Key fields (PROPOSED) |
|---|---|---|---|
| `data/catalog/stac/` | Spatiotemporal assets (rasters, vectors, scenes) | STAC 1.1 Item / Collection; collection id `kfm-<org>-<product>` *(PROPOSED convention)* | `properties.kfm:provenance` with `spec_hash`, `evidence_bundle_ref`, `run_record_ref`, `audit_ref`, `policy_digest`; plus extension fields `kfm:run_receipt_ref`, `kfm:proof_ref`, `kfm:trust_class`, `kfm:source_role`; `file:checksum` per asset. |
| `data/catalog/dcat/` | Non-spatial datasets, evidence-bundle distributions | DCAT Dataset + Distribution; `conformsTo` points at KFM evidence-bundle profile | `dcat:Distribution` with `mediaType: application/ld+json` for evidence bundles; `kfm:id`, `kfm:spec_hash`, `kfm:trust_class`, `kfm:source_role` at Dataset level. |
| `data/catalog/prov/` | Provenance graphs | PROV-O activities, agents, entities | `wasDerivedFrom` links to RAW capture; `wasGeneratedBy` to pipeline run; ties to `RunReceipt` via `kfm:run_receipt_ref`. |
| `data/catalog/domain/` | Domain-specific projections | Per-domain segment under `<domain>/` | Domain object families (Hydrology, Soil, Fauna, …) per Encyclopedia §7. |

### 11.1 KFM catalog extensions (Pass-32 §8.7.62 — KFM-P3-IDEA-0004)

STAC items, DCAT distributions, and PROV activities carry KFM-namespaced extension fields:

| Field | Purpose | Trust-class values |
|---|---|---|
| `kfm:run_receipt_ref` | Link to the `RunReceipt` that produced the artifact. | n/a |
| `kfm:proof_ref` | Link to the DSSE proof when one exists. | n/a |
| `kfm:trust_class` | Maturity tag the catalog consumer can branch on. | `receipt` · `proof` · `catalog` · `publication` |
| `kfm:source_role` | The source role declared at ingestion. | `observed` · `regulatory` · `modeled` · `aggregate` · `administrative` · `candidate` · `synthetic` |

Per-family pages MUST link to the `kfm-stac-extension` document (in `docs/standards/`) for the authoritative definition of these fields. **Implementation in any mounted repo is NEEDS VERIFICATION.**

### 11.2 `spec_hash` canonicalization (Pass-10 C8-05)

`spec_hash` values referenced in `kfm:provenance` are computed via **JCS (RFC 8785) canonical JSON + SHA-256** by default; URDNA2015 is reserved for cases that require RDF-semantic equivalence. Per-family pages SHOULD NOT re-derive hashes — they link to the `hashing/` package and the `docs/standards/SIGNING.md` profile (PROPOSED, not yet authored — see `directory-rules.md` §18 OPEN-DR-05).

### 11.3 Biodiversity hybrid (STAC × Darwin Core)

For occurrence and event records under `gbif/`, `inaturalist/`, and Kansas natural-history sources, doctrine adopts the **STAC × DwC hybrid** (Pass-10 C4-03): DwC terms (`scientific_name`, `common_name`, `kbs_id`, `kdwp_status`, `sensitivity_rank`) live inside `properties.taxon`, with a sibling `redaction_profile` and `evidence` block. Per-family pages MUST cross-link to the DwC profile (PROPOSED `docs/standards/STAC_DWC_PROFILE.md`) and the sensitivity rubric.

### 11.4 CARE-bound metadata (`kfm:care`)

When a source's `SourceDescriptor` declares a non-empty `authority_to_control` (Pass-10 C15-02), the `kfm:care` extension namespace surfaces consent, steward contact, locality restrictions, and review expiry in STAC properties / DCAT distributions. **Default-deny on publication applies** (Pass-10 C15-03). Per-family pages MUST link to the actual `policy/sensitivity/` rules — never restate them.

### 11.5 STAC 1.1 profile contract (PROPOSED, KFM-P31-PROG-0004)

The KFM STAC profile pins STAC version 1.1, the conformance set, the allowed extension set, collection-ID pattern, item identity, asset roles, and MIME types. Per-family pages MUST link to the profile document (PROPOSED `docs/standards/STAC.md`) rather than restating these conventions inline.

[↑ Back to top](#contents)

---

## 12. Trust membrane discipline

> [!CAUTION]
> **Public surfaces consume only released, governed artifacts.** Map shells, Focus Mode, Story players, Review consoles, exports, and AI surfaces MUST NOT read from `data/raw/`, `data/work/`, `data/quarantine/`, or pre-RAW event objects. The DENY surface is the governed API and the layer-manifest resolver.
> *(`directory-rules.md` §3 invariant; `docs/doctrine/trust-membrane.md`.)*

The catalog lane sits **inside the trust membrane**. STAC, DCAT, and PROV entries under `data/catalog/` are **not** automatically public — they are governed artifacts that may surface publicly only after passing the release gate in `release/` and being projected into `data/published/` via the governed API.

Per-family pages MUST observe these rules:

- Do not link directly from public docs to RAW/WORK/QUARANTINE paths even for illustration. Use placeholder hostnames or `kfm://` URIs.
- Do not document a "back door" or an internal-only retrieval pattern that public clients could mistake for a normal path.
- Surface the `kfm:trust_class` value on examples so a reader can tell at a glance whether the example artifact has reached `publication` class or remains at `receipt` / `proof` / `catalog`.
- When the family carries sensitive content (Fauna nests/dens/roosts/hibernacula/spawning sites; archaeology precise locations; living-person data), the per-family page MUST link to `policy/sensitivity/` and call out the **deny-by-default** posture explicitly.

[↑ Back to top](#contents)

---

## 13. Inputs

The documentation here is **derived from** (not authoritative over):

- `contracts/` — `SourceDescriptor`, `EvidenceBundle`, `RunReceipt`, `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, `RollbackCard`.
- `schemas/contracts/v1/source/` — machine shape (per ADR-0001 schema-home rule).
- `policy/sources/`, `policy/sensitivity/` — admissibility and release gates.
- `data/registry/sources/<domain>/` — per-source registry entries with rights, cadence, authority.
- `control_plane/source_authority_register.yaml` *(PROPOSED canonical home)* — machine-readable source authority ledger.
- `docs/standards/` — STAC, DCAT, PROV-O, PMTILES, OGC-API-TILES, ISO-19115, OAI-PMH profile documents.
- Pass-23 / Pass-32 Consolidated Atlas — *Key source families* tables per domain.

[↑ Back to top](#contents)

---

## 14. Outputs

- **Per-family Markdown pages** (and optional sub-pages per product) consumed by humans reading the repo on GitHub.
- **Cross-links** that make the trust membrane visible from a source's point of view.
- **No machine artifacts.** This folder does not emit JSON, YAML, schemas, manifests, or validators. If a contributor needs a machine output, the work belongs in `tools/`, `pipelines/`, `contracts/`, `schemas/`, or `data/`.

[↑ Back to top](#contents)

---

## 15. Validation

How this folder is checked:

| Check | Tool / location | Status |
|---|---|---|
| Markdown lint (heading levels, dead links) | `<PLACEHOLDER — docs lint workflow>` in `.github/workflows/` | NEEDS VERIFICATION |
| Per-root README contract presence | `tools/validators/<docs-readme-validator>` *(PROPOSED)* | PROPOSED |
| Link integrity against `connectors/`, `data/registry/sources/`, `data/catalog/`, `docs/standards/` | Repo-wide link checker | NEEDS VERIFICATION |
| No restatement of `policy/` rules in narrative form | Manual review; periodic drift sweep into `docs/registers/DRIFT_REGISTER.md` | PROPOSED |
| Per-family page conforms to the `_template/SOURCE_FAMILY_TEMPLATE.md` shape | Manual review at PR time | PROPOSED |
| STAC Projection lint (`proj:code`, `proj:bbox`, `proj:geometry`, `proj:shape`, `proj:transform`) — KFM-P27-FEAT-0003 | `tools/validators/catalog/` *(PROPOSED)* | PROPOSED |
| Catalog QA CI result surface (missing license, providers, stac_extensions, broken links, JSON errors) — KFM-P27-FEAT-0004 | `tools/validators/catalog/` *(PROPOSED)* | PROPOSED |

> [!CAUTION]
> Validators MUST exercise **DENY / ABSTAIN / ERROR** paths, not only the happy path (`directory-rules.md` §7.5.a, negative-state rule). A docs-lint that only reports successes is incomplete. The validator orchestrator contract (`validate_all.py`, exit `0` = pass / `1` = any fail / `2` = system error) is PROPOSED pending ADR — see `directory-rules.md` §18 OPEN-DR-03.

[↑ Back to top](#contents)

---

## 16. Review burden

| Change type | Required reviewers (PROPOSED) |
|---|---|
| New per-family page | Docs steward + Source steward for that family. |
| Edits that touch rights, sensitivity, or consent narrative | Docs steward + Sensitivity reviewer + (where applicable) Rights-holder representative. |
| Edits that touch STAC / DCAT / PROV identity conventions | Docs steward + at least one subsystem owner (`data/catalog/` or `contracts/`). |
| Edits that touch `kfm:trust_class` / `kfm:source_role` / `kfm:run_receipt_ref` / `kfm:proof_ref` extension narrative | Docs steward + contract owner (catalog extensions). |
| Path moves under this folder | Docs steward; raise drift entry if convention shifts. |
| Promotion of a PROPOSED convention here to a binding rule | **Not done in this folder.** Open an ADR (`directory-rules.md` §2.4). |

CODEOWNERS for `docs/sources/catalog/` — `<PLACEHOLDER — confirm against repo .github/CODEOWNERS>`.

[↑ Back to top](#contents)

---

## 17. Authoring guide for a per-family page

Each per-family page SHOULD use the section order below. The template lives at `_template/SOURCE_FAMILY_TEMPLATE.md` *(PROPOSED — not yet authored)*.

```text
# <family-name>

## Overview          — what the family is, who runs it, why KFM uses it
## Source authority  — link to data/registry/sources/<family>/; never restate
## Catalog profiles  — STAC, DCAT, PROV, domain — what this family lands in
## Identity & namespaces — Collection-id pattern, asset roles, kfm:provenance fields,
                          kfm:trust_class, kfm:source_role
## Rights & sensitivity — link to policy/sensitivity/; never restate
## Validation         — link to tools/validators/; never restate
## Related contracts & schemas — links into contracts/, schemas/
## Related connectors & pipelines — links into connectors/<family>/, pipelines/, pipeline_specs/
## Open questions     — anything UNKNOWN or NEEDS VERIFICATION
```

> [!TIP]
> Truth labels (`CONFIRMED`, `INFERRED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`) are mandatory where confidence materially matters. Don't upgrade uncertainty through tone.

[↑ Back to top](#contents)

---

## 18. Per-family authoring status

The table below tracks which per-family pages are authored. **All entries currently show `not started`**: this README ships first; the per-family pages are subsequent routine PRs. Each row's "owner" is `<PLACEHOLDER>` until `.github/CODEOWNERS` is confirmed.

| Family | Page path (PROPOSED) | Status | Owner |
|---|---|---|---|
| USGS | `docs/sources/catalog/usgs/README.md` | not started | `<PLACEHOLDER>` |
| FEMA | `docs/sources/catalog/fema/README.md` | not started | `<PLACEHOLDER>` |
| NOAA | `docs/sources/catalog/noaa/README.md` | not started | `<PLACEHOLDER>` |
| NRCS | `docs/sources/catalog/nrcs/README.md` | not started | `<PLACEHOLDER>` |
| Kansas (state) | `docs/sources/catalog/kansas/README.md` | not started | `<PLACEHOLDER>` |
| GBIF | `docs/sources/catalog/gbif/README.md` | not started | `<PLACEHOLDER>` |
| iNaturalist | `docs/sources/catalog/inaturalist/README.md` | not started | `<PLACEHOLDER>` |
| Census | `docs/sources/catalog/census/README.md` | not started | `<PLACEHOLDER>` |
| `local_upload` | `docs/sources/catalog/local_upload/README.md` | not started | `<PLACEHOLDER>` |

The status column SHOULD update via PR when a page moves through `not started → draft → review → published`. Authoring SHOULD be sequenced behind the per-family `connectors/<family>/README.md` and `data/registry/sources/<family>/` records — a per-family page that references a connector that doesn't exist is documentation-as-fiction.

[↑ Back to top](#contents)

---

## 19. Related folders and docs

- [`docs/sources/README.md`](../README.md) — parent: source-descriptor standards, source families orientation.
- [`docs/standards/README.md`](../../standards/README.md) — external standards index (STAC, DCAT, PROV, PMTILES, OGC-API-TILES, ISO-19115, OAI-PMH).
- [`docs/standards/STAC.md`](../../standards/STAC.md) *(PROPOSED — KFM-P31-PROG-0004)* — STAC 1.1 profile contract.
- [`docs/standards/DCAT.md`](../../standards/DCAT.md) *(PROPOSED)* — DCAT profile.
- [`docs/standards/PROV.md`](../../standards/PROV.md) — PROV-O / PAV profile *(authored prior session; see `directory-rules.md` §18 OPEN-DR-01)*.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority (esp. §6.1, §6.5, §7.3, §15).
- [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED.
- [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) — governed-API as the public path; raw/work/quarantine are not.
- [`docs/runbooks/`](../../runbooks/) — operational procedures including refresh and rollback drills.
- [`data/catalog/README.md`](../../../data/catalog/README.md) *(PROPOSED — verify presence)* — artifact-side companion.
- [`data/registry/sources/`](../../../data/registry/sources/) — machine-readable source descriptors.
- [`connectors/README.md`](../../../connectors/README.md) — fetch / admission / watcher layer.
- [`control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) *(PROPOSED canonical)*.

[↑ Back to top](#contents)

---

## 20. ADRs

| ADR | Relevance | Status |
|---|---|---|
| ADR-0001 (schema home) | Sets `schemas/contracts/v1/` as default schema home; per-family pages link there. | CONFIRMED in doctrine corpus; repo presence NEEDS VERIFICATION. |
| ADR-0003 (`policy/` singular is canonical) | Per-family pages link to `policy/`, never `policies/`. | CONFIRMED authored (prior session); repo presence NEEDS VERIFICATION. |
| **PROPOSED ADR** — *Adopt `docs/sources/catalog/` as a documentation lane under `docs/sources/`.* | Would resolve [§21 OPEN-DSC-01](#21-open-questions). | Not yet opened. |
| **PROPOSED ADR** — *Pin the KFM provenance namespace to `kfm:` (vs. `ks-kfm:`).* | Pass-10 C4-01 flags this as an open question affecting every STAC item KFM publishes; cross-references `directory-rules.md` Atlas ADR-S backlog. | Not yet opened. |
| **PROPOSED ADR** — *Pin the KFM STAC 1.1 profile contract.* | KFM-P31-PROG-0004 requires explicit conformance, extension set, identity, asset role, and MIME-type pins. | Not yet opened. |

The atlas v1.1 Ch. 24.12 "Master Open-ADR Backlog" (ADR-S-01 … ADR-S-15) is the cross-document register; this folder's ADR proposals SHOULD be added to that backlog when opened.

[↑ Back to top](#contents)

---

## 21. Open questions

<details>
<summary><b>Click to expand — verification backlog for this folder</b></summary>

- **OPEN-DSC-01.** Should `docs/sources/catalog/` exist as a docs subfolder, or should source-catalog narrative live inside `docs/sources/<family>/` directly with no intermediate `catalog/` segment? *Status: PROPOSED; resolution by per-root note in `docs/sources/README.md` or by ADR.*
- **OPEN-DSC-02.** Does the per-family page list live here, or in `docs/sources/README.md` as a flat index? (Interpretation A vs. B in [§1.1](#11-two-interpretations-on-the-table).) *Status: PROPOSED.*
- **OPEN-DSC-03.** Is the KFM provenance namespace `kfm:` (KFM-global) or `ks-kfm:` (Kansas-scoped)? (Pass-10 C4-01.) *Status: UNKNOWN; ADR-class.*
- **OPEN-DSC-04.** Should STAC Collections carry a `kfm:promotion_state` summary field? (Pass-10 C4-02.) *Status: PROPOSED.*
- **OPEN-DSC-05.** Canonical disposition between STAC and DCAT for spatiotemporal datasets that *could* go either way. (Pass-10 C4-05.) *Status: NEEDS VERIFICATION.*
- **OPEN-DSC-06.** Should `kfm:care` be proposed upstream to the STAC-extensions registry or kept KFM-local? (Pass-10 C15-02.) *Status: UNKNOWN.*
- **OPEN-DSC-07.** Filename casing convention for per-family pages — hyphens (mirroring `docs/standards/` external-spec convention) or underscores (mirroring KFM-coined topical docs)? See `directory-rules.md` §18 OPEN-DR-04. *Status: PROPOSED.*
- **OPEN-DSC-08.** Should `kfm:trust_class` be exposed in DCAT distributions as well as STAC items, or only in STAC? (KFM-P3-IDEA-0004 implies both; verify on first authored family page.) *Status: NEEDS VERIFICATION.*
- **OPEN-DSC-09.** Does the STAC 1.1 profile contract (KFM-P31-PROG-0004) live in `docs/standards/STAC.md` or in `docs/standards/STAC_KFM_PROFILE.md`? Naming follows `directory-rules.md` §18 OPEN-DR-04 once resolved. *Status: PROPOSED.*
- **OPEN-DSC-10.** Repository implementation maturity for everything in this README. *Status: UNKNOWN; no mounted repo inspected in this authoring session.*

</details>

Open items SHOULD be tracked in `docs/registers/VERIFICATION_BACKLOG.md` and surfaced in the Friday material-change report.

[↑ Back to top](#contents)

---

## 22. Changelog

| Edition | Date | Change | Evidence |
|---|---|---|---|
| **v0.2** | 2026-05-20 | Added §12 Trust membrane discipline; added §11.1 KFM catalog extensions (`kfm:run_receipt_ref`, `kfm:proof_ref`, `kfm:trust_class`, `kfm:source_role`) per Pass-32 §8.7.62 (KFM-P3-IDEA-0004); added §11.2 `spec_hash` JCS+SHA-256 note (Pass-10 C8-05); added §11.5 STAC 1.1 profile contract reference (KFM-P31-PROG-0004); added §15 rows for STAC Projection lint (KFM-P27-FEAT-0003) and Catalog QA CI surface (KFM-P27-FEAT-0004); added §18 Per-family authoring status tracker; expanded §20 ADR table to include ADR-0003 and STAC 1.1 profile-pin proposal; added §22 Changelog; expanded §24 appendix to include `kfm:trust_class` and `kfm:source_role` in the example; tightened §9 Mermaid flow with internal / governed / public bands; reordered contents accordingly. | Pass-32 atlas §8.7.62, §8.7.71; Pass-10 idea index C4, C8-05, C15-02, C15-03; `directory-rules.md` §3, §6.1, §7.3, §7.5.a, §18. |
| v0.1 | 2026-05-20 | Initial draft. | First authoring session for this lane. |

Removal of v0.2 is reversible: drop §12, §11.1, §11.2, §11.5, the two §15 catalog-lint rows, §18, the v0.2 ADR rows in §20, this §22, and revert §24 to the v0.1 example — and v0.1 is back intact.

[↑ Back to top](#contents)

---

## 23. FAQ

<details>
<summary><b>Why isn't this just inside <code>data/catalog/</code>?</b></summary>

`data/catalog/` holds **artifacts** (STAC items, DCAT distributions, PROV-O graphs, domain projections). It is governed by lifecycle law and policy gates. Narrative documentation does not belong alongside lifecycle data — it belongs under `docs/`. This folder is the human-facing lens on those artifacts, organized by source family.

</details>

<details>
<summary><b>Why by source family, not by domain?</b></summary>

Domain views already exist under `docs/domains/<domain>/` and `data/catalog/domain/<domain>/`. Source-family organization here serves a different need: a reader investigating how *NRCS SSURGO* flows through KFM wants one page, not five hops through soil, agriculture, and habitat domain docs. Cross-links to domain pages are mandatory.

</details>

<details>
<summary><b>Can I put a SourceDescriptor JSON example here?</b></summary>

Short, **illustrative** examples are fine. The **authoritative** descriptor and its schema live in `data/registry/sources/` and `schemas/contracts/v1/source/`. An example in this folder MUST link to the authoritative location and MUST be labeled illustrative.

</details>

<details>
<summary><b>What if a source family doesn't fit STAC, DCAT, or PROV?</b></summary>

Then the per-family page documents that gap. The corpus is explicit that STAC / DCAT / PROV cover most cases (Pass-10 §6.4) but not all — e.g. some prosopography and genealogy records share the catalog envelope under C4.e but require additional care. Flag it as an open question and route to ADR if a new profile is genuinely needed (`directory-rules.md` §2.4 — parallel-authority rule).

</details>

<details>
<summary><b>How should a per-family page show the trust class of an artifact?</b></summary>

Use the `kfm:trust_class` field shown in the appendix. Valid values are `receipt`, `proof`, `catalog`, and `publication` (Pass-32 §8.7.62). In narrative prose, distinguish: a `receipt`-class artifact has only a `RunReceipt`; `proof` adds a DSSE proof; `catalog` adds STAC/DCAT/PROV closure; `publication` adds the release manifest and the release decision. Never show a public-surface screenshot of an artifact below `publication` class without an explicit "not yet released" callout.

</details>

<details>
<summary><b>Is this folder canonical for anything?</b></summary>

**No.** It is `docs-companion` authority only. Any contributor who finds themselves treating a page here as a binding rule should open a drift entry. Binding rules live in `contracts/`, `schemas/`, `policy/`, `release/`, or ADRs.

</details>

[↑ Back to top](#contents)

---

## 24. Appendix — minimal STAC `kfm:provenance` shape

The shape below is **illustrative** (derived from Pass-10 C4-01 and Pass-32 §8.7.62) and **NEEDS VERIFICATION** against the mounted-repo schema in `schemas/contracts/v1/source/` (per ADR-0001). It now includes the Pass-32 KFM catalog extension fields.

```json
{
  "stac_version": "1.1.0",
  "id": "kfm-noaa-storm-events-2024-04-12",
  "type": "Feature",
  "collection": "kfm-noaa-storm-events",
  "stac_extensions": [
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
    "kfm://stac-extensions/kfm-provenance/v0.1/schema.json"
  ],
  "properties": {
    "datetime": "2024-04-12T17:42:00Z",
    "kfm:provenance": {
      "spec_hash": "sha256:<JCS+SHA-256 of canonicalized payload>",
      "evidence_bundle_ref": "kfm://evidence/<bundle-digest>",
      "run_record_ref": "kfm://run/<run-id>",
      "audit_ref": "kfm://audit/<attestation-id>",
      "policy_digest": "sha256:<policy-bundle-digest>"
    },
    "kfm:run_receipt_ref": "kfm://receipt/<receipt-id>",
    "kfm:proof_ref": "kfm://proof/<dsse-envelope-id>",
    "kfm:trust_class": "publication",
    "kfm:source_role": "observed"
  },
  "assets": {
    "data": {
      "href": "s3://kfm-cataloged/.../events.parquet",
      "type": "application/vnd.apache.parquet",
      "file:checksum": "sha256:<...>",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../collection.json" },
    { "rel": "attestation", "href": "kfm://evidence/<bundle-digest>" }
  ]
}
```

Notes:

- `kfm:provenance` fields and `file:checksum` are doctrine-grounded (Pass-10 C4-01 CONFIRMED).
- `kfm:run_receipt_ref`, `kfm:proof_ref`, `kfm:trust_class`, `kfm:source_role` are doctrine-grounded (Pass-32 §8.7.62, KFM-P3-IDEA-0004 CONFIRMED in doctrine).
- The `attestation` link relation is **PROPOSED** — not a registered STAC link rel today (`KFM-P7-PROG-0001`); upstream submission to the STAC-extensions registry is an open expansion.
- The namespace prefix shown here is `kfm:` — this is **UNKNOWN** until [OPEN-DSC-03](#21-open-questions) is resolved.
- `spec_hash` is computed as **JCS (RFC 8785) + SHA-256** per Pass-10 C8-05; URDNA2015 is reserved for cases needing RDF-semantic equivalence.

[↑ Back to top](#contents)

---

## Related docs

- [`docs/sources/README.md`](../README.md) — parent orientation.
- [`docs/standards/README.md`](../../standards/README.md) — external standard profiles.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority.
- [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) — public-path discipline.
- [`data/catalog/README.md`](../../../data/catalog/README.md) — artifact-side companion *(verify presence)*.
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — backlog including the open questions listed above.

## Last reviewed <a id="last-reviewed"></a>

**2026-05-20** *(updated for the flat-to-folder reorganization — Claude Code session, mounted repo; §8 and §10.1 reflect the realized per-family folder layout)*.
Re-review trigger: any of (a) `docs/sources/` reorganization, (b) ADR resolving [§19 OPEN-DSC-01](#19-open-questions), (c) addition of a new connector family in `connectors/`, (d) change to STAC / DCAT / PROV profile choice in `docs/standards/`.

[↑ Back to top](#contents)
