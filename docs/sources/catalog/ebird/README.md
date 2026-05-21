<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources/catalog/ebird
title: eBird — Source Profile (family README)
type: standard
version: v1.1
status: draft
owners: [PLACEHOLDER — biodiversity steward + source-registry steward; CODEOWNERS NEEDS VERIFICATION]
created: 2026-05-13
updated: 2026-05-21
policy_label: restricted
related:
  - docs/sources/catalog/ebird/ebird-api.md
  - docs/sources/catalog/ebird/ebird-ebd.md
  - docs/sources/catalog/ebird/ebird-sed.md
  - docs/sources/catalog/README.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/domains/fauna/README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - schemas/contracts/v1/source/source-descriptor.schema.json
  - policy/sensitivity/
  - data/registry/sources/fauna/
tags: [kfm, source-profile, biodiversity, fauna, birds, ebird, restricted-use, observed]
notes:
  - "eBird EBD travels under restricted-use terms that limit republication; cite-or-abstain applies."
  - "All path claims herein are PROPOSED until verified against mounted-repo evidence."
  - "v1.1 update — integrates three sibling product pages (eBird API 2.0, EBD, SED); refreshes atlas-card grounding (KFM-P2-IDEA-0020, KFM-P2-PROG-0005, KFM-P24-PROG-0001, KFM-P24-PROG-0013, KFM-P24-PROG-0015, KFM-P24-PROG-0020, KFM-P27-PROG-0005); surfaces canonical-home question (docs/sources/catalog/ebird.md vs. docs/sources/catalog/ebird/README.md); strengthens §7.3 placement discussion (OPEN-DSC-14)."
[/KFM_META_BLOCK_V2] -->

# 🐦 eBird — Source Profile

> Human-facing companion to the eBird `SourceDescriptor`. This is the **family-level README** for the eBird source family; per-product specifics live in three sibling pages — the **eBird API 2.0**, the **eBird Basic Dataset (EBD)**, and the **Sampling Event Data (SED)**. Captures identity, role, rights posture, sensitivity treatment, cadence, KFM lifecycle, and public-release class.

[![Status](https://img.shields.io/badge/status-draft-yellow)](#)
[![Source role](https://img.shields.io/badge/source__role-observed-blue)](#3-source-role--authority-anchoring)
[![Rights posture](https://img.shields.io/badge/rights-restricted--use-orange)](#5-rights--restricted-use-posture)
[![Sensitivity class](https://img.shields.io/badge/sensitivity-domain--governed-lightgrey)](#6-sensitivity--c6-redaction-mapping)
[![Release class](https://img.shields.io/badge/public__release-deny--by--default-red)](#7-public-release-posture)
[![Family pages](https://img.shields.io/badge/family%20pages-API%20%E2%80%A2%20EBD%20%E2%80%A2%20SED-blueviolet)](#1-overview)
[![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-blueviolet)](#8-kfm-pipeline-shape-raw--published)
[![CI](https://img.shields.io/badge/CI-TODO-lightgrey)](#)
[![Last reviewed](https://img.shields.io/badge/last__reviewed-2026--05--21-informational)](#)

**Status:** draft · **Version:** v1.1 · **Owners:** *PLACEHOLDER — biodiversity steward + source-registry steward (NEEDS VERIFICATION)* · **Last updated:** 2026-05-21

---

## Quick jump

1. [Overview](#1-overview)
2. [Repo fit & authority](#2-repo-fit--authority)
3. [Source role & authority anchoring](#3-source-role--authority-anchoring)
4. [At-a-glance source profile](#4-at-a-glance-source-profile)
5. [Rights & restricted-use posture](#5-rights--restricted-use-posture)
6. [Sensitivity & C6 redaction mapping](#6-sensitivity--c6-redaction-mapping)
7. [Public release posture](#7-public-release-posture)
8. [KFM pipeline shape (RAW → PUBLISHED)](#8-kfm-pipeline-shape-raw--published)
9. [Connectors, cadence & smart-sync](#9-connectors-cadence--smart-sync)
10. [Validation, evidence & receipts](#10-validation-evidence--receipts)
11. [Open questions & verification backlog](#11-open-questions--verification-backlog)
12. [Related docs](#12-related-docs)
13. [Appendix](#13-appendix)

---

## 1. Overview

eBird is a community-observation dataset for bird occurrences, organized around effort-quantified checklists. **CONFIRMED KFM doctrine** (`KFM-P2-IDEA-0020`): *"eBird (Cornell Lab) is treated as the canonical citizen-science avian authority, ingested via the eBird API with appropriate license and rate-limit handling. eBird data carries observer attribution that flows through the watcher into the EvidenceBundle."*

KFM models **three distinct eBird products** — each with its own dedicated product page sitting alongside this family README:

| Product page | Distribution | Role within KFM | Key KFM atlas card |
|---|---|---|---|
| [`ebird-api.md`](./ebird-api.md) | **eBird API 2.0** — near-real-time HTTP REST; API key | Operational / coverage layer; watcher-driven freshness | `KFM-P2-IDEA-0020`, `KFM-P2-PROG-0005` |
| [`ebird-ebd.md`](./ebird-ebd.md) | **eBird Basic Dataset (EBD)** — monthly bulk TSV; restricted access agreement | Research-grade authority for historical occurrences | `KFM-P24-PROG-0001`, `KFM-P24-PROG-0020` |
| [`ebird-sed.md`](./ebird-sed.md) | **Sampling Event Data (SED)** — checklist-level effort companion to EBD | Join key for EBD; enables zero-filled presence-absence | `KFM-P24-PROG-0001`, `KFM-P27-PROG-0005` |

This file does **not** restate the per-product detail — see the dedicated pages for STAC profiles, identity skeletons, provenance fields, temporal handling, redaction profiles, and gate sequences specific to each product. This file covers the **family-level** concerns that apply across all three: rights posture, sensitivity rubric mapping, role and authority anchoring, and the cross-product gates.

The corpus places eBird inside the **C10-06 Biodiversity Stack**, alongside GBIF, iNaturalist, NatureServe, USFWS, iDigBio, Symbiota, KU NHM, and FHSU Sternberg. KFM's biodiversity convention is to **anchor every occurrence to ITIS TSN** (or GBIF Backbone where ITIS is silent), preserve the originating institution, and **apply C6 redaction** for any species ranked S1/S2 by NatureServe or KDWP SINC.

```mermaid
flowchart TB
  README["docs/sources/catalog/ebird/<br/><b>README.md</b> · family profile"]
  API[ebird-api.md]
  EBD[ebird-ebd.md]
  SED[ebird-sed.md]

  README -->|orients| API
  README -->|orients| EBD
  README -->|orients| SED
  EBD <-->|paired download<br/>pair-coherence gate| SED
  EBD -. share SourceDescriptor .- SED

  classDef family fill:#1f6feb,stroke:#0a2e6b,color:#fff;
  classDef product fill:#bf8700,stroke:#5c4400,color:#fff;
  class README family;
  class API,EBD,SED product;
```

> [!IMPORTANT]
> eBird EBD is a **restricted-use** source. KFM may *ingest* EBD into governed lanes for internal evidence resolution, but any **public derivative** must be evaluated against the current EBD terms and may require explicit approval. The default release class for EBD-derived public artifacts is **DENY** until an `EBD-derivative-release policy` is authored and an upstream `SourceActivationDecision` records the allowed scope.

---

## 2. Repo fit & authority

### Canonical home of this file

The prior version's PROPOSED home was `docs/sources/catalog/ebird.md` (flat). Authoring the three sibling product pages established a folder pattern at `docs/sources/catalog/ebird/`, which conflicts with the flat-file home for the family README.

| Option | Path | Status |
|---|---|---|
| **A — folder + README (PREFERRED in this v1.1)** | `docs/sources/catalog/ebird/README.md` (this file) + `ebird-api.md`, `ebird-ebd.md`, `ebird-sed.md` as siblings | PROPOSED; sibling-link references in the three product pages assume this layout |
| B — flat family file | `docs/sources/catalog/ebird.md` plus a separate `docs/sources/catalog/ebird/` folder for products | PROPOSED alternative; defensible but introduces parallel-path drift |

**Action required:** ADR or steward decision to pin the canonical layout. Until then, this file's `doc_id` (`kfm://doc/sources/catalog/ebird`) is layout-agnostic and resolves to either. See [§11](#11-open-questions--verification-backlog) `OPEN-DSC-14` for the broader §7.3 placement discussion.

> [!NOTE]
> The **`docs/sources/catalog/` subdirectory** is **PROPOSED** in this document. Directory Rules cite `docs/sources/` as the canonical lane and `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` as a known sibling, but the existence of a `catalog/` segment is **NEEDS VERIFICATION** against mounted-repo evidence. Confirm before merging, or open a drift entry in `docs/registers/DRIFT_REGISTER.md`.

### Adjacent authority surfaces (PROPOSED unless noted)

| Layer | Path | Authority | Status |
|---|---|---|---|
| Source-descriptor standard | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | Human-facing standard | PROPOSED |
| `SourceDescriptor` schema home | `schemas/contracts/v1/source/source-descriptor.schema.json` | Machine shape (per ADR-0001) | PROPOSED |
| Source authority register | `control_plane/source_authority_register.yaml` | Machine-readable register | PROPOSED |
| Sensitivity policy | `policy/sensitivity/` | Decision rules | PROPOSED |
| Observer-privacy policy *(SED-specific need)* | `policy/privacy/` | Decision rules — observer PII | PROPOSED (new lane, NEEDS VERIFICATION) |
| Registry entry | `data/registry/sources/fauna/ebird/` | Operational registry | PROPOSED |
| Connector | `connectors/ebird/` *(beyond §7.3 — see [§9](#9-connectors-cadence--smart-sync))* | Source-specific fetcher | PROPOSED |
| Domain dossier | `docs/domains/fauna/README.md` | Domain landing | PROPOSED |
| Fauna pipeline | `pipelines/domains/fauna/` and `pipeline_specs/fauna/` | Executable + declarative | PROPOSED |

**Lifecycle invariant** (CONFIRMED doctrine): `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a **governed state transition, not a file move.**

```mermaid
flowchart LR
  subgraph Upstream["eBird (upstream — Cornell Lab of Ornithology)"]
    EBD["eBird Basic Dataset (EBD)<br/><i>monthly · 15th</i>"]
    SED["Sampling Event Data (SED)<br/><i>paired with EBD</i>"]
    API["eBird API 2.0<br/><i>near-real-time · API key</i>"]
    GBIFR["eBird-in-GBIF (EOD)<br/><i>annual · no effort fields</i>"]
  end

  subgraph Admission["KFM admission (governed)"]
    SD["SourceDescriptor<br/>source_role: observed"]
    SAD["SourceActivationDecision<br/>allowed | restricted | denied | needs-review"]
    CONN["connectors/ebird/<br/>(beyond §7.3 — OPEN-DSC-14)"]
  end

  subgraph Lifecycle["RAW → PUBLISHED"]
    RAW["data/raw/fauna/ebird/&lt;run_id&gt;/"]
    WORK["data/work/ or data/quarantine/"]
    PROC["data/processed/fauna/<br/><i>partitioned parquet by event_date month</i><br/>(KFM-P24-PROG-0020)"]
    CAT["data/catalog/ + EvidenceBundle"]
    PUB["data/published/<br/><i>public-safe derivatives only</i>"]
  end

  subgraph Trust["Trust membrane"]
    API_GOV["apps/governed-api/"]
    UI["apps/explorer-web/"]
  end

  EBD --> SD
  SED --> SD
  API --> SD
  GBIFR -. crosswalk · rights inherit .-> SD
  SD --> SAD --> CONN --> RAW --> WORK --> PROC --> CAT --> PUB
  PUB --> API_GOV --> UI

  classDef restricted fill:#fff3cd,stroke:#b08800,color:#3b2e00;
  classDef governed fill:#e8f0ff,stroke:#3b6cb3,color:#0b2545;
  class EBD,SED,API restricted
  class SD,SAD,CONN,API_GOV governed
```

---

## 3. Source role & authority anchoring

### Source role assignment

`source_role = observed` (community / citizen-science observation).

- **Why `observed` and not `aggregate`** — checklists record per-observer detections in a defined effort window. The atomic record is an observation event with effort metadata, not a roll-up. KFM doctrine forbids inferring source role from convenience; this assignment is set at admission and persisted in the `SourceDescriptor`.
- **eBird is `observation`, not `specimen`** — CONFIRMED rule (`KFM-P2-IDEA-0020`): *"eBird is treated as a coverage-layer / observation source rather than as authoritative specimen-backed evidence; the ingest layer must annotate that distinction and avoid letting eBird records displace KANU/KSC specimen records in dedupe."* Downstream UI MUST NOT render eBird points and specimen points with identical UI weight.
- **GBIF-redistributed EBD** — when eBird records reach KFM via the GBIF Occurrence API (the EOD distribution), the *provider* is GBIF and the *upstream source* is eBird. Both must be preserved in `EvidenceBundle` citations. Crosswalking via GBIF does **not** relax eBird's restricted-use posture. The corpus open question favors direct eBird ingest over GBIF-subset because the GBIF EOD distribution lacks the EBD's effort fields.

### Authority anchoring (CONFIRMED KFM convention)

| Anchor | Role | Status |
|---|---|---|
| **ITIS TSN** | U.S.-canonical taxonomic authority; required anchor where ITIS has coverage | CONFIRMED doctrine |
| **GBIF Backbone Taxonomy** (DOI `10.15468/39omei`) | International crosswalk; second-line authority where ITIS is silent/stale | CONFIRMED doctrine |
| **Originating institution** | Preserved through admission and downstream catalog records | CONFIRMED doctrine |
| **Per-observation observer attribution** | Flows through the watcher into the EvidenceBundle | CONFIRMED — `KFM-P2-IDEA-0020` |
| **KDWP listing status** | Canonical Kansas regulatory authority for endangered, threatened, and SINC species | CONFIRMED — `KFM-P19-IDEA-0005` |
| Sensitivity ranking | NatureServe + KDWP SINC drive C6 redaction posture | CONFIRMED doctrine |

> [!TIP]
> Where ITIS and GBIF disagree on accepted name, the KFM-wide tie-breaker policy is **NEEDS VERIFICATION** — the corpus flags this as an unresolved open question. Until the policy is authored, downstream consumers should treat such records as having two equally legitimate anchors and surface both.

---

## 4. At-a-glance source profile

**Field shape below is PROPOSED**, modeled on the doctrinal `SourceDescriptor` surface and anchored where possible to the EBD source-descriptor field list in `KFM-P24-PROG-0001`. **Actual field names in the mounted schema are NEEDS VERIFICATION**.

| Field | Value | Truth label |
|---|---|---|
| `source_id` | `ebird` *(or `cornell-ebird` — choose at registry creation; product variants `ebird:api2`, `ebird:ebd`, `ebird:sed`)* | PROPOSED |
| `source_family` | `biodiversity / fauna / birds` | CONFIRMED doctrine |
| `source_role` | `observed` (EBD/SED/API); `effort_metadata` for SED if separately descriptored | PROPOSED at admission |
| `provider` | Cornell Lab of Ornithology (operator) | EXTERNAL — see product-page appendices |
| `role_authority` | Cornell Lab of Ornithology | EXTERNAL |
| `surfaces` | EBD (bulk monthly TSV) · SED (effort companion) · eBird API 2.0 (near-real-time REST) · eBird-in-GBIF EOD (annual, occurrence-only) | EXTERNAL — see [§1](#1-overview) family table and product pages |
| `access_method` | EBD/SED: Cornell data-request form + bulk file download; API: `x-ebirdapitoken` header, HTTPS REST | EXTERNAL — see product pages |
| `endpoint(s)` | *NEEDS VERIFICATION — record exact URLs in the descriptor, not here* | NEEDS VERIFICATION |
| `cadence` | EBD/SED: **monthly · 15th of each month**; API: continuous (1–30 day lookback) | EXTERNAL — confirmed via product pages |
| `species_code` *(EBD field)* | eBird species-code carried through normalization | PROPOSED — `KFM-P24-PROG-0001` |
| `observation_id` *(EBD field)* | eBird per-observation identifier | PROPOSED — `KFM-P24-PROG-0001` |
| `checklist_id` *(EBD/SED join key)* | Sampling event identifier (e.g., `S22536787`) | PROPOSED — `KFM-P24-PROG-0001`; `KFM-P27-PROG-0005` "dedupe by stable checklist keys" |
| `effort_fields` | survey protocol · duration · distance · area · number of observers · time of day · `ALL SPECIES REPORTED` flag · `GROUP IDENTIFIER` | PROPOSED — `KFM-P24-PROG-0001` (EBD); EXTERNAL on specific names |
| `rights_posture` | **Restricted-use; redistribution limited** | CONFIRMED in corpus |
| `license` | *Not asserted here — record SPDX/text reference in the descriptor* | NEEDS VERIFICATION |
| `attribution_required` | `true` — Cornell Lab + per-observation observer attribution | CONFIRMED — `KFM-P2-IDEA-0020` |
| `sensitivity_default` | Per-record, driven by NatureServe / KDWP SINC rank | CONFIRMED doctrine |
| `observer_privacy` *(SED dimension)* | Observer-ID hashing/stripping + k-anonymity at aggregation | PROPOSED — SED-specific extension |
| `release_class` | **DENY** for public derivatives until terms reviewed | CONFIRMED doctrine posture |
| `taxonomic_anchor` | ITIS TSN (primary), GBIF Backbone (secondary) | CONFIRMED doctrine |
| `staging_strategy` | Partitioned parquet by `event_date` month before normalization | PROPOSED — `KFM-P24-PROG-0020` |
| `steward` | *NEEDS VERIFICATION — assign at admission* | NEEDS VERIFICATION |
| `activation_decision` | `needs-review` until policy + terms confirmed | PROPOSED default |

> [!NOTE]
> Per Directory Rules §2.3, **source identity, rights, and sensitivity are owned by `data/registry/` and `policy/sensitivity/`** — this document is the human-facing profile, not the authoritative descriptor. When this doc and the descriptor disagree, **the descriptor and policy bundle win.** Raise the conflict as a drift entry.

---

## 5. Rights & restricted-use posture

The KFM corpus records the following as **CONFIRMED**:

> *"eBird EBD restricted-use terms limit redistribution; the corpus warns that any KFM release derived from EBD must be checked against the EBD terms and may require approval."*
> *"Author an EBD-derivative-release policy that names what KFM can and cannot publish; pilot a request to eBird for KFM-specific terms."*

### Operational rules (PROPOSED, derived from CONFIRMED doctrine)

| Operation | Default | Required controls |
|---|---|---|
| **Ingest into governed lanes** (RAW/WORK) | ALLOW under access agreement | `SourceDescriptor` + `SourceActivationDecision`; rights text captured in `RunReceipt` |
| **Internal evidence resolution** | ALLOW | EvidenceRef → EvidenceBundle; no caching outside governed stores |
| **PROCESSED / CATALOG inside trust membrane** | ALLOW with provenance | Source preserved end-to-end; no source erasure during normalization |
| **Public download of EBD-derived records** | **DENY** by default | No EBD-derivative-release policy exists yet (PROPOSED in corpus) |
| **Public map of EBD-derived occurrence points** | **DENY** by default | C6 sensitivity overrides this anyway for many taxa |
| **Public aggregate** (county roll-up, hex grid, HUC12) | RESTRICT pending policy | `AggregationReceipt` + matrix-cell semantics + effort-weighting + DP receipt for aggregates if applied; HUC12 alternative per `KFM-P24-PROG-0015` |
| **Public effort-coverage layer** (SED-derived, no species) | RESTRICT pending policy | k-anonymity threshold met; observer-ID stripped; trip comments dropped |
| **Republication to a third party** | **DENY** | Out-of-scope until upstream terms expressly allow it |
| **Citation of eBird as evidence in governed answers** | ALLOW | Citation must travel with the answer; cite-or-abstain default |

> [!WARNING]
> **Do not** publish exact-coordinate EBD-derived points on a public surface, in tiles, in published vector layers, or in evidence-drawer payloads. Trust-membrane discipline (CONFIRMED doctrine): public clients use governed APIs and **released public-safe** artifacts only — never RAW, WORK, QUARANTINE, candidates, or model-internal stores. A connector or watcher that bypasses this is a **SEVERE** drift event and must be reverted, not patched downstream.

> [!CAUTION]
> Per CONFIRMED doctrine `ML-062-016` (Master MapLibre Components): **"license travels with deltas before map ingestion."** Map-layer admission MUST fail closed when license or use terms are unknown.

---

## 6. Sensitivity & C6 redaction mapping

The KFM **C6 sensitivity rubric** (CONFIRMED) assigns each record a `sensitivity_rank` in 0–5. eBird records inherit rank from the species' published status (NatureServe, KDWP SINC) plus any per-record steward flag.

| Rank | Meaning | Default profile for eBird records | Public exposure |
|---|---|---|---|
| **0** | Public / open | `profile:none` | Allowed *— but EBD rights still gate downstream publication* |
| **1** | Common, non-sensitive | `profile:none` or coarse-cell summary | Allowed — *rights still apply* |
| **2** | Watchlist | Named profile (e.g., `point_10km_hex_seeded_v1`) | Generalized only |
| **3** | KDWP SINC / locally sensitive | `profile:sinc-obscure-10km` (corpus default) | Generalized cell or centroid; **NEEDS VERIFICATION** of exact profile |
| **4** | Threatened / rare (e.g., NatureServe S1/S2) | Strict mask or embargo | DENY exact; generalized public products only |
| **5** | Sacred / critical | Fail-closed | **No map or timeline exposure** |

PROPOSED doctrine (`KFM-P24-IDEA-0002`, `KFM-P24-PROG-0013`): *"Fauna occurrence records for sensitive taxa should default to DENY or ABSTAIN until redaction, aggregation, or role-gated access is explicitly approved."* OPA policy returns ABSTAIN or DENY for sensitive fauna unless spatial generalization, aggregation, or access gating obligations are satisfied.

Profile changes are versioned (`...@v1`) and each release of an EBD-derived public product **must** produce a `RedactionReceipt` recording `policy_ref`, `redaction_method`, `kept_fields`, `removed_fields`, `geometry_transform`, and `reviewer`.

> [!CAUTION]
> Even for rank-0/1 records, **eBird's restricted-use posture is a separate gate** from the C6 sensitivity gate. Both must pass. Passing C6 alone does not authorize an EBD-derived public release.

### Two privacy layers, not one (carries from SED page)

The eBird family carries **two privacy gates** that operate independently:

1. **Sensitive-species privacy** (C6 + KFM-P24-IDEA-0002) — applies wherever species records are exposed.
2. **Observer privacy** (SED-specific, also relevant for joined EBD+SED views) — Observer IDs, precise checklist locations and timestamps, group identifiers, and trip-comment text MUST be redacted before any public release, independently of whether sensitive-species records are present.

Both gates must close before any public artifact is released. See [`ebird-sed.md`](./ebird-sed.md) §10.2 for the observer-privacy framing.

### Geoprivacy transform expectations

- **Display jitter** is *not* a substitute for actual geoprivacy. Use seeded, reproducible jitter only for display obfuscation, never as a privacy guarantee (CONFIRMED doctrine: C6-03; seed = `spec_hash + occurrence_id` for EBD, `spec_hash + checklist_id` for SED).
- **Grid generalization** (H3 hex or PostGIS `ST_SnapToGrid`) is the recommended primary transform for biodiversity occurrences (CONFIRMED doctrine: C6-04).
- **HUC12 aggregation** is an alternative to point publication for sensitive occurrences (PROPOSED — `KFM-P24-PROG-0015`).
- **Differential privacy** applies only to *aggregate* outputs (counts, heatmaps), never to raw points (CONFIRMED doctrine: C6-05).
- **k-Anonymity** applies at render time, including for observer-pattern privacy on SED-derived effort layers (CONFIRMED doctrine: C6-06).

---

## 7. Public release posture

| Class | Decision | Reason |
|---|---|---|
| **EBD raw checklists / records** | DENY | Restricted-use terms + cite-or-abstain default |
| **SED raw checklists** | DENY | Observer-PII + join-key value (would expose sensitive observations when re-joined with EBD) |
| **Per-record occurrence points** | DENY | Both rights gate and C6 sensitivity gate must clear |
| **Range-polygon products** | RESTRICT | Allowed only when derived without per-point exposure and approved by EBD-derivative policy |
| **Hex / county / HUC12 aggregates without per-point recovery** | RESTRICT pending policy | Needs EBD-derivative-release policy + `AggregationReceipt` + effort-weighting |
| **SED-derived effort-coverage layers (no species)** | RESTRICT pending policy | Observer-PII stripped + k-anonymity enforced + Cornell agreement honored |
| **Authoritative species lists for a region** | RESTRICT | Possible under attribution; verify against current terms |
| **Citation references to eBird** (without redistributing data) | ALLOW | Treat eBird as an evidence source via `EvidenceBundle` |
| **eBird-in-GBIF citations (where applicable)** | ALLOW | Cite GBIF distribution + DOI; rights still inherit from upstream eBird |

> [!IMPORTANT]
> **Required before any public derivative ships:** `SourceActivationDecision = allowed`, EBD-derivative-release policy authored and pinned in the policy bundle, attribution copy approved, evidence closure complete, sensitivity transforms applied where C6 demands, observer-PII removal verified for SED-touching outputs, `RedactionReceipt` + `AggregationReceipt` (if applicable) emitted, `ReleaseManifest` produced, rollback target recorded, correction path defined.

---

## 8. KFM pipeline shape (RAW → PUBLISHED)

Per the Fauna domain's pipeline contract (CONFIRMED doctrine; PROPOSED lane application):

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable EBD/SED/API payload (or reference) with `source_role`, rights text, sensitivity hint, citation, time, content hash | `SourceDescriptor` exists; `SourceActivationDecision ∈ {allowed, restricted}`; **EBD ⨯ SED pair-coherence check for paired downloads** | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, taxon identity (ITIS/GBIF), evidence, rights, observer-PII handling, and policy; hold failures (malformed rows, missing effort fields, taxa without anchor, rights ambiguity, observer-PII unresolved) | Validation + policy gate pass, or `QuarantineRecord` with reason | PROPOSED |
| **PROCESSED** | Partitioned parquet by `event_date` month (per `KFM-P24-PROG-0020`); validated normalized objects (`Occurrence Evidence`, `Occurrence Restricted`, `MonitoringEvent`, `EffortRecord`), receipts, public-safe candidates where C6 + rights + observer-privacy permit | `EvidenceRef` resolves, `ValidationReport`, digest closure | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`, graph/triplet projections, release candidates | Catalog/proof closure passes; STAC × Darwin Core hybrid pattern for occurrence Items; tri-checksum closure (`KFM-P22-PROG-0037/38/39`) | PROPOSED |
| **PUBLISHED** | Serve **only** released public-safe artifacts through `apps/governed-api/`; no raw points; no restricted derivatives; effort-weighted aggregates only | `ReleaseManifest`, correction path, rollback target, review + policy state exist | PROPOSED |

### Trust-membrane reminders

- Public clients (`apps/explorer-web/`) and normal UI surfaces **MUST** use governed interfaces (`apps/governed-api/`), never canonical or internal stores.
- Connectors emit to `data/raw/...` or `data/quarantine/...` — **never** to `data/processed/`, `data/catalog/`, or `data/published/`.
- Watchers are non-publishing: they emit receipts and candidate decisions, not authoritative artifacts.

> [!TIP]
> **Per-product gate sequences live in the product pages.** This README's gates are the family-level minimum. The full eBird API gate sequence is in [`ebird-api.md`](./ebird-api.md) §11; the EBD sequence in [`ebird-ebd.md`](./ebird-ebd.md) §11 (14 gates including agreement validity); the SED sequence in [`ebird-sed.md`](./ebird-sed.md) §11 (15 gates including pair-coherence and observer-privacy).

---

## 9. Connectors, cadence & smart-sync

### §7.3 placement (OPEN-DSC-14)

`directory-rules.md` §7.3 enumerates exactly nine canonical connector roots: `usgs`, `fema`, `noaa`, `nrcs`, `kansas`, `gbif`, `inaturalist`, `census`, `local_upload`. **`ebird` is not among them.** This is a real placement question — particularly notable because the §7.3 list already contains two citizen-science aggregators (`gbif`, `inaturalist`) but omits the family the corpus names as the **canonical citizen-science avian authority** (`KFM-P2-IDEA-0020`).

| Candidate connector placement | Argument | Argument against |
|---|---|---|
| `connectors/ebird/` *(this v1.1 default)* | Treats eBird as a peer of `gbif/`/`inaturalist/`; matches the corpus's canonical-authority framing | Requires §7.3 amendment / ADR |
| `connectors/cornell/ebird/` | Hosts eBird under its producing institution; could absorb other Cornell sources later | Requires new `cornell/` root → §7.3 amendment |
| `connectors/gbif/ebird/` (via EOD redistribution) | No §7.3 amendment needed | **Discouraged.** Corpus favors direct eBird ingest (`KFM-P2-IDEA-0020` open question) because EOD lacks effort fields. Flattening eBird under GBIF would misrepresent source identity. |

**ADR required.** Tracked as `OPEN-DSC-14`.

### Cadence & smart-sync

| Aspect | Doctrine / posture | Notes |
|---|---|---|
| Cadence — EBD | **Monthly release · 15th of each month** | Snapshot-based; each release supersedes prior; partition-diff is the correction-detection mechanism |
| Cadence — SED | **Paired with EBD release (same date)** | Pair-coherence gate at connector exit: release-date match + checklist-key inclusion |
| Cadence — eBird API | Continuous; 1–30 day lookback per request | Rate limits real — *"Use the API with some restraint"* per Cornell guidance |
| Smart-sync (EBD/SED) | Resumable bulk download; content hash on intake | EBD bulk file SHOULD be content-hashed at intake |
| Smart-sync (API) | C3-01 Conditional GET (ETag / `If-None-Match`, `Last-Modified` / `If-Modified-Since`); pair with manifest SHA-256 verification (C3-02) when publisher exposes checksums | API rate-limit discipline is doctrinal |
| Connector pattern | `KFM-P2-PROG-0005` — "reproducible eBird ingest adapter that pulls citizen-science bird observations under Cornell Lab terms, runs ingest-time QA on basic-observation fields … maps eBird license and attribution metadata to the KFM license model, applies sensitivity rules for sensitive species, and emits an EvidenceBundle plus run receipt." | Applies across API/EBD/SED |
| Normalizer pattern | `KFM-P27-PROG-0005` — "eBird harvest normalizer … dedupe by stable occurrence/checklist keys" | The SED's `checklist_id` is the dedupe primary for joined views |
| Staging strategy | Partitioned parquet by `event_date` month before normalization | PROPOSED — `KFM-P24-PROG-0020` |
| Tooling | Cornell's `auk` R package is the reference EBD-extraction tool | KFM tooling choice (`auk` vs. parquet-native DuckDB / Polars) is open |
| Quarantine triggers | Missing effort fields; incomplete checklist when downstream requires `ALL SPECIES REPORTED = TRUE`; taxon without ITIS/GBIF anchor; rights ambiguity; schema drift; license posture change; observer-PII handling not configured | Each produces a `QuarantineRecord` with a reason code |
| Receipt content | `spec_hash`, `source_head` (ETag, Last-Modified, content length, source commit), `source_url`, `license` (SPDX id + text ref), `evidence_refs[]`, `decision_log`, `runner_id`, `timestamp`, `kfm_spec_version`, `target_zone` | Canonical KFM `run_receipt.json` shape |

> [!NOTE]
> If EBD ships without a checksums manifest in a given release, fall back to publisher validator headers (ETag / Last-Modified). Track whether eBird exposes a manifest in the registry's `has_manifest` flag — and surface it on the Friday material-change check-in.

---

## 10. Validation, evidence & receipts

### Required objects (per KFM doctrine, PROPOSED implementation for this source)

| Object | Purpose | Required for eBird? |
|---|---|---|
| `SourceDescriptor` | Identity, role, rights, cadence, access, sensitivity, release posture | Yes — at admission |
| `SourceActivationDecision` | Gate deciding allowed / restricted / quarantined / denied / needs-review | Yes — before connector activates |
| `RunReceipt` | Auditable record of intake / transform / validation / catalog / release / rebuild | Yes — every connector run |
| `PairCoherenceReceipt` *(EBD ⨯ SED-specific)* | Proves SED partition matches EBD release date and checklist-key set | Yes — for any EBD/SED pair operation |
| `ValidationReport` | Schema, geometry, temporal, rights, sensitivity, observer-privacy, evidence checks | Yes — at WORK gate |
| `EvidenceRef` → `EvidenceBundle` | Pointer from claim/feature/layer to evidence support; bundle returns source list, excerpts/records, provenance, policy/review/release state | Yes — for any consequential downstream claim |
| `RedactionReceipt` | Public-safe transformation record (masking, generalization, suppression) | Yes — whenever C6 transforms apply |
| `AggregationReceipt` | Pins geometry scope for aggregated outputs | Required for any aggregated public product |
| `PolicyDecision` | `allow | deny | restrict | abstain | error` envelope | Yes — at every gate |
| `PromotionReceipt` | Auditable representation of Promotion Gates A–G | Yes — at promotion |
| `ReleaseManifest` | Published artifact set, digests, policy posture, rollback target | Yes — at PUBLISHED |
| `CorrectionNotice` | When records change, are withdrawn, or shift sensitivity | On material change |

### Promotion Gate Matrix (A–G)

| Gate | Intent | What it checks for eBird |
|---|---|---|
| **A** — Structure & Metadata | MetaBlock presence and zone correctness | `SourceDescriptor` exists; `source_role = observed`; zones consistent |
| **B** — Schemas & Contracts | Schema and OpenAPI validation | Occurrence / event / checklist shapes valid; STAC × Darwin Core hybrid clean |
| **C** — Policy Parity | Conftest/OPA decisions match runtime | CI bundle digest pinned; same Rego runs at PDP |
| **D** — Security & Sensitivity | Sensitivity, license, AND observer-privacy scans | C6 redaction profile applied; EBD rights text captured; observer-PII removal verified |
| **E** — Data Quality | DQ profilers/assertions with thresholds | Complete-checklist invariants where required; effort variables present; taxon anchored; EBD ⨯ SED pair-coherent |
| **F** — Provenance & Lineage | Receipt and lineage validation | Run, source, content, geometry, spec hashes all closed; tri-checksum closure (`KFM-P22-PROG-0037/38/39`) |
| **G** — Reviewability | CODEOWNERS-enforced human + policy approval | Biodiversity steward + source-registry steward signoff; sensitive-lane ReviewRecord where applicable |

---

## 11. Open questions & verification backlog

<details>
<summary><b>Click to expand — eBird-specific open items derived from KFM corpus (PROPOSED / NEEDS VERIFICATION)</b></summary>

| # | Item | Class |
|---|---|---|
| 1 | Author the **EBD-derivative-release policy** as a small machine-readable asset under the policy bundle | Writing |
| 2 | Pilot a request to eBird / Cornell Lab for **KFM-specific terms** that bound permissible derivatives | Process |
| 3 | Confirm current redistribution-terms posture of eBird EBD (corpus flags this as an evidence-needed question) | Verification |
| 4 | Confirm `connectors/ebird/` placement under `directory-rules.md` §7.3 — **OPEN-DSC-14** | ADR / Design |
| 5 | Confirm whether SED gets its own SourceDescriptor or is folded into the EBD's (per `KFM-P24-PROG-0001`'s field-list reading) | Design |
| 6 | **Confirm canonical home of this file** — flat `docs/sources/catalog/ebird.md` vs. folder + README `docs/sources/catalog/ebird/README.md`. v1.1 default is folder + README. | Design |
| 7 | Determine the right cell size for KDWP SINC species in eBird-derived public layers; does it vary by county density? | Design |
| 8 | Document the **eBird-in-GBIF (EOD)** crosswalk: when KFM ingests an EBD record via GBIF, how is upstream attribution preserved and how do rights propagate? Confirm corpus preference for direct EBD over GBIF EOD (`KFM-P2-IDEA-0020` open question). | Design |
| 9 | Pin the exact endpoint URLs and access methods in the `SourceDescriptor` (do not pin them in this doc) | Verification |
| 10 | Confirm `has_manifest` posture (does eBird publish a SHA-256 manifest for EBD releases?) | Verification |
| 11 | Define the **monthly snapshot handler** — receipt must capture exact release identifier to prevent downstream double-counting; partition-diff for correction detection | Implementation |
| 12 | Add CI check that flags any eBird-derived record lacking both an ITIS and a GBIF Backbone anchor | Implementation |
| 13 | Add a fixture suite: rank 0–5 examples, complete vs. incomplete checklists, ambiguous taxon, rights-unknown, observer-PII test cases | Implementation |
| 14 | Confirm `policy/sensitivity/` decision rules treat EBD restricted-use as a *separate* gate from C6 sensitivity (per `KFM-P24-IDEA-0002`/`KFM-P24-PROG-0013`) | Verification |
| 15 | Confirm whether `policy/privacy/` exists as a separate lane for observer-PII or whether observer-privacy rules live alongside sensitive-species in `policy/sensitivity/` | Design |
| 16 | Confirm tooling choice: Cornell's `auk` R package vs. parquet-native (DuckDB / Polars) for EBD processing | Design |
| 17 | Resolve eBird-API admissibility — confirm `source_role`, `SourceActivationDecision`, and per-product sensitivity posture matches the family stance | Design |
| 18 | Confirm k-anonymity threshold values for SED-derived effort-coverage layers (per-region) | Design |
| 19 | Confirm right-to-be-forgotten handling for observer-data requests; how does it interact with snapshot-based monthly releases? Pass-10 `C5-09` tombstone pattern is the likely floor | Design |
| 20 | Open atlas question (`KFM-P2-IDEA-0020`): "Should eBird records ever be promoted to a public layer at point precision, or should they always be aggregated to a coarser cell for public release?" — answer **never at point precision for sensitive taxa**; the open question is point precision for non-sensitive taxa | Design |

</details>

---

## 12. Related docs

### Sibling product pages (within this family)

- [`ebird-api.md`](./ebird-api.md) — eBird API 2.0 product page
- [`ebird-ebd.md`](./ebird-ebd.md) — eBird Basic Dataset (EBD) product page
- [`ebird-sed.md`](./ebird-sed.md) — Sampling Event Data (SED) product page

### Catalog-lane siblings

- [`docs/sources/catalog/README.md`](../README.md) — catalog lane index *(PROPOSED path)*
- [`docs/sources/catalog/PROFILES.md`](../PROFILES.md) — STAC / DCAT / PROV-O / domain-projection registry *(PROPOSED path)*
- [`docs/sources/catalog/IDENTITY.md`](../IDENTITY.md) — identity & namespace conventions *(PROPOSED path)*
- [`docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) — rights & sensitivity mapping *(PROPOSED path)*
- [`docs/sources/catalog/OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — lane-wide `OPEN-DSC-*` register *(PROPOSED path)*
- [`docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) — per-product page template *(PROPOSED path)*

### Doctrine, standards, and registers

- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../SOURCE_DESCRIPTOR_STANDARD.md) — source-descriptor standard *(PROPOSED path)*
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement law (§7.3 connectors, §7.4 pipelines) *(PROPOSED path)*
- [`docs/doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) — cite-or-abstain *(PROPOSED path)*
- [`docs/doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) — RAW → PUBLISHED *(PROPOSED path)*
- [`docs/architecture/contract-schema-policy-split.md`](../../../architecture/contract-schema-policy-split.md) — split of contracts / schemas / policy *(PROPOSED path)*
- [`docs/domains/fauna/README.md`](../../../domains/fauna/README.md) — Fauna domain landing *(PROPOSED path)*
- [`docs/standards/SENSITIVITY_RUBRIC.md`](../../../standards/SENSITIVITY_RUBRIC.md) — C6 rubric 0–5 *(PROPOSED path)*
- [`docs/standards/REDACTION_DETERMINISM.md`](../../../standards/REDACTION_DETERMINISM.md) — seeded jitter & grid rules *(PROPOSED path)*
- [`docs/registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md) — record any path drift uncovered while wiring eBird *(PROPOSED path)*
- *Sibling source profiles* (PROPOSED): `gbif/`, `inaturalist/`, `natureserve/`, `usfws/`, `idigbio/`, `symbiota/`

---

## 13. Appendix

<details>
<summary><b>A. Why eBird is governed differently from the broader biodiversity stack</b></summary>

The KFM corpus (CONFIRMED) treats biodiversity as the most plurally-sourced domain in the system. GBIF, iNaturalist, NatureServe, USFWS, iDigBio, Symbiota, KU NHM, and FHSU Sternberg all sit alongside eBird in the C10-06 stack. Most of those sources are **permissive** with respect to redistribution. eBird is the exception: EBD's restricted-use terms make it the canonical *restricted* biodiversity dataset in the corpus.

This is why eBird gets a dedicated source profile rather than living inside a generic "biodiversity aggregators" entry: its rights gate is materially different and must be enforced separately from the C6 sensitivity gate. Treating them as a single gate is a known anti-pattern.

A related observation: the §7.3 connector list names `gbif` and `inaturalist` but omits `ebird`, even though the corpus designates eBird as the canonical citizen-science avian authority. This v1.1 reads that as a §7.3 omission requiring ADR resolution rather than as evidence that eBird should be flattened under another agency — see [§9](#9-connectors-cadence--smart-sync) and `OPEN-DSC-14`.

</details>

<details>
<summary><b>B. EvidenceBundle expectations for eBird-cited claims</b></summary>

When a KFM answer, layer, or feature cites eBird as supporting evidence, the resolved `EvidenceBundle` SHOULD include:

- **Source list:** eBird (and GBIF if redistributed via GBIF / EOD), with stable identifiers. **Per-observation observer attribution** flows in (CONFIRMED — `KFM-P2-IDEA-0020`).
- **Excerpts / records:** the record identifiers actually cited (never the full row when restricted-use applies; cite-or-abstain).
- **Provenance:** ingest receipt hash, EBD release identifier, run receipt reference, **pair-coherence receipt** for any EBD ⨯ SED join, **Cornell data-use agreement reference** for EBD-touching evidence.
- **Policy / review / release state:** current `SourceActivationDecision`, applicable `RedactionReceipt` reference, `ReleaseManifest` reference.
- **Temporal scope:** observed time, source time, retrieval time, release time, correction time — kept distinct where material.
- **Rights text:** SPDX identifier where applicable; otherwise reference to current upstream terms.

Generated text never substitutes for `EvidenceBundle`: bundles outrank fluent generation.

</details>

<details>
<summary><b>C. STAC × Darwin Core hybrid for eBird occurrence Items (PROPOSED pattern)</b></summary>

Per the corpus's STAC × DwC hybrid (CONFIRMED doctrine, PROPOSED for eBird):

- STAC envelope: `id`, `stac_version`, `type: Feature`, `geometry`, `bbox`, `properties.datetime`, `assets`, `links`, `collection`, `stac_extensions[]`.
- DwC payload lives in `properties.taxon` and `properties.event`:
  - `taxon`: `scientific_name`, `common_name`, `itis_tsn`, `gbif_taxon_id`, `kdwp_status`, `nature_serve_rank`, `sensitivity_rank`, `redaction_profile`.
  - `event`: `eventID` (eBird `SAMPLING EVENT IDENTIFIER`), `eventDate`, `samplingProtocol`, `sampleSizeValue` (effort), `samplingEffort` (duration), `ALL SPECIES REPORTED` completeness flag.
- KFM-namespaced enrichments: `kfm:evidence_bundle`, `kfm:policy_label`, `kfm:sensitivity`, `kfm:spec_hash`, `kfm:release_state`, `kfm:data_use_agreement_ref` (EBD/SED), `kfm:pair_coherence_ref` (SED).
- Provenance via `links` with `derived_from` / `was_generated_by` rel values rather than inventing top-level fields.

Field names above are **PROPOSED**; the authoritative shapes live in `schemas/contracts/v1/...`. Verify before depending on any name.

</details>

<details>
<summary><b>D. Anti-patterns to avoid</b></summary>

- ❌ Publishing exact EBD-derived points on a public surface.
- ❌ Treating GBIF redistribution as relaxing eBird's upstream rights posture.
- ❌ Collapsing the rights gate, the C6 sensitivity gate, and the observer-privacy gate into a single check — they are three independent gates.
- ❌ Naming the connector path after a topic (e.g., `connectors/birds/`) rather than the source (`connectors/ebird/`).
- ❌ Flattening eBird under `gbif/` because §7.3 names GBIF but not eBird — corpus favors direct eBird ingest.
- ❌ Cache-storing EBD payloads outside governed lanes (e.g., in `artifacts/`, browser caches, public S3).
- ❌ Re-rolling jitter on each render of a sensitive point (triangulation risk; use seeded jitter per `C6-03`).
- ❌ Publishing SED-derived effort-coverage layers without observer-ID stripping and k-anonymity enforcement.
- ❌ Letting eBird records displace KANU/KSC specimen records in dedupe (CONFIRMED rule, `KFM-P2-IDEA-0020`).
- ❌ Citing eBird in a published artifact without an `EvidenceBundle` and rights text.
- ❌ Joining EBD with SED without emitting a `PairCoherenceReceipt`.
- ❌ Restating policy rules inside this README; this doc orients, policy decides.

</details>

---

<sub>Last reviewed: 2026-05-21 · Doc version: v1.1 · [⬆ Back to top](#-ebird--source-profile)</sub>
