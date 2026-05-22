<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources-catalog-noaa
title: NOAA Source Family — Catalog Entry
type: standard
version: v1.1
status: draft
owners: TODO — Docs steward + Hazards domain steward + Atmosphere/Air/Climate domain steward
created: TODO-YYYY-MM-DD
updated: 2026-05-22
policy_label: public
related:
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/sources/catalog/README.md
  - docs/domains/hazards/README.md
  - docs/domains/atmosphere/README.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0001-schema-home.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - connectors/noaa/README.md
  - policy/release/hazards/
  - policy/release/atmosphere/
  - policy/sensitivity/
tags: [kfm, sources, noaa, hazards, atmosphere, weather, climate, hms, nws, storm-events]
notes:
  - "Path `docs/sources/catalog/` is PROPOSED — Directory Rules §6.1 lists `docs/sources/` for 'source-descriptor standards, source families' but does not enumerate a `catalog/` subdirectory."
  - "Confirm with Docs steward before merging; alternative homes include `docs/sources/families/noaa.md` or a flat `docs/sources/noaa.md`. See OPEN-NOAA-01."
  - "Default `source_role` is *multi-role* — NOAA admissions span `observed` (Storm Events, station obs), `regulatory-context` (NWS warnings/advisories — contextual only), `modeled` (forecasts, HMS, model fields), and `aggregate` (climate normals). The family must never be admitted under a single role."
  - "v1.1 polish pass: section numbering unified (Repo fit is now §2); added §5.0 source-role quick reference; added §9.0 receipts quick reference; OPEN questions renumbered as `OPEN-NOAA-NN`; cross-link to sibling product-pages under `docs/sources/catalog/newspapers/` added."
[/KFM_META_BLOCK_V2] -->

# NOAA Source Family — Catalog Entry

> Catalog entry for the **National Oceanic and Atmospheric Administration (NOAA)** source family as governed inside Kansas Frontier Matrix (KFM). Doctrine, source-role posture, domains served, sensitivity controls, and lifecycle obligations — not a connector, not a release, not an alert authority.

[![Doc status](https://img.shields.io/badge/status-draft-orange)](#status)
[![Doc type](https://img.shields.io/badge/doc--type-source--family--catalog-blue)](#1-scope)
[![Authority](https://img.shields.io/badge/authority-PROPOSED-yellow)](#2-repo-fit)
[![Source role](https://img.shields.io/badge/source__role-multi--role-purple)](#5-source-role-assignments)
[![Policy](https://img.shields.io/badge/policy-fail--closed-critical)](#8-sensitivity-rights-and-publication-posture)
[![Life safety](https://img.shields.io/badge/life--safety-NOT_AN_ALERT_AUTHORITY-red)](#83-the-doctrinal-red-line)
[![Lifecycle](https://img.shields.io/badge/lifecycle-governed-informational)](#7-lifecycle-posture-raw--published)

| Field | Value |
|---|---|
| **Document role** | Source-family catalog entry under `docs/sources/` |
| **Authority of these contents** | Reflects current KFM doctrine; specific paths and field names remain `PROPOSED` until verified in the mounted repo. |
| **Status** | `draft` |
| **Version** | `v1.1` |
| **Owners** | *TODO — Docs steward + Hazards domain steward + Atmosphere/Air/Climate domain steward.* |
| **Last updated** | `2026-05-22` *(v1.1 polish pass; full review pass still pending)* |
| **Path classification** | `PROPOSED` (see [§ 2 Repo fit](#2-repo-fit) and Section 2 of the accompanying notes) |

> [!IMPORTANT]
> **KFM is not an emergency alerting system.** Per the Hazards domain (CONFIRMED doctrine: *"KFM Hazards is not an emergency alert system and must not provide life-safety instructions"*) and the Sensitive / Deny-by-Default Register, KFM publishes NOAA-derived material as **historical, analytical, or contextual evidence only**, with explicit redirection to official sources for any life-safety action. NWS warnings/advisories/watches enter KFM under a `contextual-only` posture, never as KFM-issued alerts.

---

## Quick navigation

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. Inputs — sub-sources within the NOAA family](#3-inputs--sub-sources-within-the-noaa-family)
- [4. Exclusions](#4-exclusions)
- [5. Source-role assignments](#5-source-role-assignments)
  - [5.0 Quick reference](#50-quick-reference)
  - [5.1 Canonical roles](#51-canonical-source-roles-relevant-to-noaa)
  - [5.2 Anti-collapse failures](#52-anti-collapse-failures-kfm-denies-for-the-noaa-family)
- [6. Domains served](#6-domains-served)
- [7. Lifecycle posture (RAW → PUBLISHED)](#7-lifecycle-posture-raw--published)
- [8. Sensitivity, rights, and publication posture](#8-sensitivity-rights-and-publication-posture)
- [9. Required artifacts and governance hooks](#9-required-artifacts-and-governance-hooks)
  - [9.0 Receipts quick reference](#90-receipts-quick-reference)
- [10. Validators and tests](#10-validators-and-tests)
- [11. Open questions & verification backlog](#11-open-questions--verification-backlog)
- [12. Related docs](#12-related-docs)
- [Appendix A — Source-role field crosswalk](#appendix-a--source-role-field-crosswalk-proposed)
- [Appendix B — Glossary](#appendix-b--glossary)

---

## 1. Scope

NOAA covers a wide and heterogeneous family of products. In KFM, the NOAA family is treated as a **multi-role source family**, not a single source — different NOAA products carry different `source_role` assignments and feed different domains.

What this document is:

- A **catalog entry** describing what the NOAA family is, what KFM admits from it, and under what governance.
- A **pointer hub** to the canonical `SourceDescriptor` schema home, the connector, the relevant domain dossiers, and the policy lanes that govern NOAA-derived publication.
- A **doctrine restatement** so reviewers can recognize NOAA-specific failure modes (e.g., NWS advisories rebroadcast as KFM alerts; storm-event records misread as observed inundation; HMS smoke polygons published as emergency guidance).

What this document is **not**:

- Not a connector. The fetch-and-admit code lives under `connectors/noaa/` (CONFIRMED placement per Directory Rules §7.3; specific file presence is `PROPOSED` until repo-verified).
- Not the canonical `SourceDescriptor`. That schema's home defaults to `schemas/contracts/v1/source/source_descriptor.schema.json` per ADR-0001.
- Not a release manifest, layer descriptor, or policy bundle.
- Not an alert authority.

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 2. Repo fit

> [!NOTE]
> Per **Directory Rules §6.1**, `docs/sources/` is the human-facing home for "source-descriptor standards, source families." A `catalog/` subdirectory under `docs/sources/` is **`PROPOSED`** — it is not explicitly enumerated in Directory Rules and should be confirmed (or relocated) before this entry is published. See [OPEN-NOAA-01](#11-open-questions--verification-backlog) and Section 2 of the accompanying notes for migration options.

### 2.1 Where NOAA lives across the repo (PROPOSED placements)

| Responsibility | Path | Status | Rule |
|---|---|---|---|
| Human-facing source-family catalog entry (this doc) | `docs/sources/catalog/noaa.md` | `PROPOSED` | Directory Rules §6.1 (extension) |
| Source-descriptor standard (cross-source) | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | `PROPOSED` | Directory Rules §6.1 |
| Canonical SourceDescriptor schema | `schemas/contracts/v1/source/source_descriptor.schema.json` | `PROPOSED` | ADR-0001 (schema-home) |
| Operational source register (per-family entries) | `data/registry/sources/<domain>/` and `data/registry/source_descriptors/` | `PROPOSED` | Directory Rules §7.4 / lifecycle phase rules |
| NOAA-specific fetch and admission | `connectors/noaa/` | `CONFIRMED` rule / `PROPOSED` presence | Directory Rules §7.3 |
| Source-family release/sensitivity policy | `policy/release/hazards/`, `policy/release/atmosphere/` (or per-source lanes) | `PROPOSED` | Directory Rules §6 / policy split |
| RAW lifecycle landing | `data/raw/<domain>/noaa/<run_id>/` or `data/quarantine/...` | `CONFIRMED` rule | Directory Rules §7.3 lifecycle invariant |
| Connector validators | `tools/validators/connector_gate/`, `tools/validators/source_descriptor/` | `PROPOSED` | Directory Rules §7.5 |

### 2.2 Sibling product-page convention (PROPOSED)

A parallel pattern is emerging for newspaper-family **product slices** at `docs/sources/catalog/newspapers/<product>.md` — e.g., `legal-notices.md`, `obituaries.md`, `ocr-full-text.md`. If NOAA's sub-sources (Storm Events, NWS API, HMS Fire and Smoke, climate normals, station observations) need that level of per-product documentation, the analogous layout would be `docs/sources/catalog/noaa/<sub-source>.md`. See [OPEN-NOAA-08](#11-open-questions--verification-backlog).

### 2.3 Upstream / downstream

```mermaid
flowchart LR
    NOAA["NOAA family<br/>(external authority)"]:::ext
    CONN["connectors/noaa/<br/>(fetch + admit)"]:::ops
    RAW["data/raw/<domain>/noaa/...<br/>or data/quarantine/..."]:::raw
    SDESC["SourceDescriptor<br/>(role, rights, sensitivity, cadence)"]:::gov
    WORK["WORK / QUARANTINE<br/>(normalize, validate)"]:::work
    PROC["PROCESSED<br/>(validated, canonical records)"]:::proc
    CAT["CATALOG / TRIPLET<br/>(EvidenceBundle, release candidates)"]:::cat
    PUB["PUBLISHED<br/>(governed-API surfaces, public-safe artifacts)"]:::pub

    NOAA --> CONN
    CONN --> RAW
    CONN -. emits .-> SDESC
    SDESC -. governs .-> WORK
    RAW --> WORK --> PROC --> CAT --> PUB

    classDef ext fill:#eef,stroke:#447;
    classDef ops fill:#efe,stroke:#474;
    classDef raw fill:#fee,stroke:#744;
    classDef work fill:#fef,stroke:#747;
    classDef proc fill:#ffe,stroke:#774;
    classDef cat fill:#eff,stroke:#477;
    classDef pub fill:#dfd,stroke:#272;
    classDef gov fill:#ffd,stroke:#770,stroke-dasharray: 4 2;
```

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 3. Inputs — sub-sources within the NOAA family

KFM admits NOAA inputs as **distinct sub-sources**, each with its own `SourceDescriptor`, source role, rights posture, sensitivity class, and freshness expectation. Lumping them into a single "NOAA" descriptor is a `SOURCE_ROLE_COLLAPSE` anti-pattern (see [§ 5](#5-source-role-assignments)).

The following sub-sources are named in KFM doctrine for the Hazards and Atmosphere/Air/Climate domains. Specific endpoint URLs, parameter shapes, and rate limits are **NEEDS VERIFICATION** and live under the connector, not here.

| Sub-source | Doctrinal label | Domains served | KFM source-role usage | Status in source ledger |
|---|---|---|---|---|
| NOAA Storm Events (NCEI-style records) | Historical severe-weather catalog | Hazards | **observed** (event records) with `regulatory_context` aside where applicable | `NEEDS VERIFICATION` rights/cadence |
| NWS API (forecasts, alerts, watches, warnings, advisories) | `EXT-NWS` in the external source ledger | Hazards, Atmosphere/Air/Climate | **contextual only** — warnings/advisories ingested as `AdvisoryContext` / `WarningContext`, **never** as KFM-issued alerts | `EXTERNALLY CHECKED` — supports forecast/alert/observation **context**; **cannot prove** KFM is an emergency alerting system |
| NOAA HMS Fire and Smoke | Operational fire/smoke analysis product | Hazards (smoke), Atmosphere/Air/Climate (smoke context) | **modeled / observed** (mixed; product-internal); cite-as-modeled when in doubt | `NEEDS VERIFICATION` rights/cadence |
| NOAA HRRR-Smoke / NOAA smoke forecast | Operational smoke forecast model | Atmosphere/Air/Climate, Hazards (adjacency) | **modeled** — `ModelRunReceipt` required | `NEEDS VERIFICATION` per-product |
| NOAA/NWS station observations & climate products (normals, anomalies, model fields) | Mesonet-adjacent network observations and gridded products | Atmosphere/Air/Climate | **observed** (stations), **modeled** (model/reanalysis), **aggregate** (climate normals) | `NEEDS VERIFICATION` per-product |
| (other NOAA products) | *e.g., precipitation-frequency atlases, drought monitor partners, radar mosaics* | Hazards, Atmosphere/Air/Climate | Per-product; **must not be inferred from NOAA family alone** | `UNKNOWN` until admitted with a SourceDescriptor |

> [!CAUTION]
> The list above is **not exhaustive** and **not authoritative**. The authoritative inventory of admitted NOAA sub-sources is the `data/registry/sources/...` register, not this doc. If a NOAA product is not in the register with an active `SourceDescriptor`, it is not admitted, regardless of what this catalog entry mentions.

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 4. Exclusions

What does **not** belong here, and where it goes instead:

| If it's about… | Place it under |
|---|---|
| The shape of a SourceDescriptor field | `schemas/contracts/v1/source/source_descriptor.schema.json` (ADR-0001) |
| The standard governing all source families | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (`PROPOSED`) |
| Connector code, polling cadence, ETag logic, run receipts | `connectors/noaa/` + `data/receipts/...` |
| Admission decisions for a specific NOAA product | `data/registry/sources/<domain>/` (operational register) |
| Whether to release a NOAA-derived layer publicly | `policy/release/<domain>/` |
| Sensitivity/rights for a specific feature class | `policy/sensitivity/<domain>/` |
| Hazard domain doctrine (object families, map layers, AI behavior) | `docs/domains/hazards/` |
| Atmosphere/Air/Climate domain doctrine | `docs/domains/atmosphere/` |
| Tile generation, MapLibre styling, PMTiles output | `packages/maplibre/`, `pipelines/publish/`, `data/published/pmtiles/` |
| Run receipts, ingest receipts | `data/receipts/ingest/` |

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 5. Source-role assignments

KFM treats **source role as a first-class identity attribute**. An observed reading is not interchangeable with a modeled estimate; a regulatory determination is not interchangeable with an administrative compilation; an aggregate publication is not interchangeable with candidate evidence. The lifecycle and the governed API both fail closed when these roles are conflated.

NOAA is the family **most likely** to be misclassified across these boundaries because:

- NWS alerts can look like observations to a downstream renderer.
- HMS smoke polygons can look like observed smoke to a casual viewer.
- Climate normals can look like per-place values when joined to a county polygon.
- Forecast grids can look like nowcasts when the temporal-role tag is dropped.

### 5.0 Quick reference

A one-table view of how NOAA sub-sources map to KFM source roles, the receipts those roles require, and what each role is **not**. CONFIRMED doctrine, PROPOSED field realization.

| NOAA sub-source (example) | Default `source_role` | Required receipts | What it is **not** |
|---|---|---|---|
| Storm Events tornado record | `observed` | `SourceDescriptor`, `RunReceipt`, `ValidationReport` | Not a flood-inundation observation; not authority for downstream impact claims. |
| NWS Warning / Advisory / Watch | **`regulatory-context`** *(contextual only)* | `SourceDescriptor`, `RunReceipt`, `PolicyDecision (DENY rebroadcast)` | **Not** a KFM-issued alert. Not actionable life-safety guidance. |
| NWS Forecast grid | `modeled` | `SourceDescriptor`, `ModelRunReceipt`, `ValidationReport` | Not an observation; not authority for "what is happening now." |
| NOAA HMS Fire and Smoke | `modeled` (default; cite-as-modeled when in doubt) | `SourceDescriptor`, `ModelRunReceipt` | Not observed smoke; not exposure guidance. |
| HRRR-Smoke | `modeled` | `SourceDescriptor`, `ModelRunReceipt` | Not a measurement; not exposure guidance. |
| Climate Normal (1991–2020) | `aggregate` | `SourceDescriptor`, `AggregationReceipt` | Not a per-place value; not a per-day expectation. |
| NWS / Mesonet station observation | `observed` | `SourceDescriptor`, `RunReceipt` | Not a regional generalization. |
| Unmerged or quarantined NOAA admission | `candidate` | `SourceDescriptor` with `role_candidate_disposition: pending` | **Not** publishable. `PUBLISHED` edge forbidden until `merged`. |

> [!TIP]
> See [§ 9.0 Receipts quick reference](#90-receipts-quick-reference) for the receipt shapes themselves, and [Appendix A](#appendix-a--source-role-field-crosswalk-proposed) for the field-level crosswalk.

### 5.1 Canonical source roles relevant to NOAA

| Role | NOAA-family example | KFM citation rule |
|---|---|---|
| **observed** | Storm Events records of a tornado touchdown; station temperature reading | Cite as observation; never relabel as regulatory or aggregate. |
| **regulatory-context** *(see note)* | NWS warnings/watches/advisories viewed as KFM evidence | Cite as **contextual only**, with official-source redirection. KFM never re-issues them. |
| **modeled** | NWS gridded forecast; smoke trajectory model; HMS-derived analysis | Cite with model identity + `ModelRunReceipt`; never labeled an observation. |
| **aggregate** | Climate normal (1991–2020), decadal anomaly | Cite with `AggregationReceipt`; never treated as a per-place record. |
| **candidate** | Unmerged or quarantined NOAA admission | Cite only in `WORK / QUARANTINE`; forbidden on `PUBLISHED`. |
| **synthetic** | *N/A for NOAA admissions.* Synthetic reconstructions are not NOAA outputs. | If anything synthetic is ever wrapped around a NOAA input, it requires a Reality Boundary Note and Representation Receipt. |

> [!NOTE]
> "Regulatory-context" above is shorthand. NWS advisories/watches/warnings are **issued by NWS as authoritative public-safety communications**. KFM neither rebroadcasts them as KFM-issued alerts nor treats them as KFM's own regulatory determinations. They enter KFM as `AdvisoryContext` / `WarningContext` evidence with `not-for-life-safety` posture and explicit official-source redirection.

### 5.2 Anti-collapse failures KFM denies for the NOAA family

| Collapse | Denied outcome | Required guardrail |
|---|---|---|
| NWS advisory rebroadcast as a KFM alert | `DENY` at trust membrane; UI fails closed | `not-for-life-safety` disclaimer; issue/expiry freshness; official-source redirect |
| Modeled forecast labeled as observed | `DENY` at publication; `ABSTAIN` at AI surface | `ModelRunReceipt` + uncertainty surface + role-preserving DTO field |
| HMS smoke analysis labeled as observed smoke | `DENY` at publication if role unverified | Source-role tag preserved; banner in UI; per-product source descriptor |
| Climate normal cited as a per-place truth | `DENY` join from aggregate cell to single record; `ABSTAIN` at AI | `AggregationReceipt` + geometry-scope guard |
| Storm Events record cited as observed flood inundation | `DENY` until separate flood-inundation evidence exists | Separate regulatory-layer and observed-event lanes; per-event evidence closure |
| AQI cited as concentration / AOD cited as PM2.5 | `DENY` at publication (CONFIRMED DOM-AIR doctrine) | Knowledge-character label + unit normalization tests |

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 6. Domains served

NOAA inputs feed **two primary domains** in KFM doctrine, with adjacencies into Hydrology, Agriculture, and Habitat.

```mermaid
flowchart TD
    NOAA["NOAA source family"]
    HAZ["Hazards [DOM-HAZ]"]
    AIR["Atmosphere / Air / Climate [DOM-AIR]"]
    HYD["Hydrology<br/>(adjacency — joins)"]
    AG["Agriculture<br/>(adjacency — weather/drought)"]
    HAB["Habitat<br/>(adjacency — smoke/heat stress)"]

    NOAA -->|Storm Events, NWS<br/>warnings (context), HMS| HAZ
    NOAA -->|NWS station obs,<br/>forecasts, climate normals| AIR
    HAZ -.->|hazard-hydrology joins| HYD
    AIR -.->|weather → ag baselines| AG
    AIR -.->|smoke / heat context| HAB

    classDef noaa fill:#cdf,stroke:#247;
    classDef dom fill:#dfd,stroke:#272;
    classDef adj fill:#eee,stroke:#777,stroke-dasharray: 3 3;
    class NOAA noaa;
    class HAZ,AIR dom;
    class HYD,AG,HAB adj;
```

### 6.1 Per-domain object families NOAA evidence supports

| Domain | Object families fed by NOAA (CONFIRMED doctrine; specific schema presence `PROPOSED`) |
|---|---|
| Hazards | `HazardEvent`, `HazardObservation`, `WarningContext`, `AdvisoryContext`, `SmokeContext`, `WildfireDetection` (where HMS contributes), `HazardTimeline`, `ImpactArea` |
| Atmosphere / Air / Climate | `WeatherStation`, `WeatherObservation`, `WindField`, `PrecipitationObservation`, `TemperatureObservation`, `ClimateNormal`, `ClimateAnomaly`, `ForecastContext`, `AdvisoryContext`, `SmokeContext` |

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 7. Lifecycle posture (RAW → PUBLISHED)

The KFM lifecycle invariant is **governance, not storage organization**. Promotion is a governed state transition, not a file move. NOAA admissions follow the standard lifecycle.

| Phase | NOAA-specific handling | Gate (CONFIRMED rule / `PROPOSED` implementation) |
|---|---|---|
| `raw/` | Source-edge capture (e.g., raw NWS API response, raw Storm Events CSV/JSON, raw HMS shapefile/KMZ) with retrieval metadata (ETag, Last-Modified, request URL), checksums, and a SourceDescriptor. | `SourceDescriptor` exists; ingest receipt written. |
| `work/` / `quarantine/` | Normalize schema, geometry, time, units. Quarantine on unresolved rights, unresolved sensitivity, schema drift, over-precise geometry, or stale advisory state. Warning feeds default **disabled or contextual-only** in domain fixtures. | Validation + policy gate pass, or quarantine reason recorded. |
| `processed/` | Validated, canonical, role-tagged records: `HazardEvent`, `WeatherObservation`, `AdvisoryContext`, `SmokeContext`, etc. | `EvidenceRef`, `ValidationReport`, digest closure. |
| `catalog/` / `triplets/` | STAC/DCAT/PROV records, `EvidenceBundle`s, graph projections, release candidates. NOAA's role-mixing means catalog records must preserve `source_role` and (where modeled) `role_model_run_ref`. | Catalog/proof closure. |
| `published/` | Governed-API surfaces (`/api/v1/layers`, `/api/v1/evidence/{bundle_id}`, etc.), public-safe layer manifests, PMTiles. Public clients **must** consume governed APIs, **not** RAW or canonical stores directly. | `ReleaseManifest`, correction path, rollback target, review/policy state all exist. |

> [!TIP]
> The hazards domain's **"first credible thin slice"** is documented as a historical flood/severe-weather event fixture plus NFHL context and exposure summary, **with warning feeds disabled or contextual-only**. NOAA admissions for hazard-event evidence should follow that same pattern: lean on historical Storm Events records and explicit `AdvisoryContext` framing rather than on live-warning rebroadcast.

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 8. Sensitivity, rights, and publication posture

### 8.1 Rights

| Aspect | Posture |
|---|---|
| Distribution | NOAA products are generally U.S. government works in the public domain, but **per-product rights and current terms remain `NEEDS VERIFICATION`** in the KFM source register (doctrine: rights uncertainty blocks public release). |
| Attribution | Required per the source register's `attribution` field; renderer-side attribution display tests apply. |
| Sub-product caveats | Some NOAA products embed third-party data with separate terms. The connector must capture rights on a **per-sub-source** basis, not at the family level. |

### 8.2 Sensitivity classes (Sensitive / Deny-by-Default Register)

| Class triggered by NOAA admissions | Default outcome | Required controls |
|---|---|---|
| **Emergency warning misuse** (operational warnings, forecasts, hazard instructions) | `DENY` life-safety replacement; **contextual-only** with official-source redirection | `not-for-life-safety` disclaimer; issue/expiry freshness tracked |
| **Source-rights-limited records** (any NOAA-embedded record with uncertain terms) | `DENY` public release until terms resolved | rights register entry; attribution; no public derivative if barred |
| **Stale source / stale warning** | Stale source badge in Evidence Drawer; stale warning denial in hazards | Re-admit or supersede; mark dependent claims stale |

### 8.3 The doctrinal red line

> [!WARNING]
> **KFM does not act as an emergency alerting system.** This is doctrine, not preference. The Hazards mission explicitly excludes life-safety alerting (CONFIRMED: *"KFM Hazards is not an emergency alert system and must not provide life-safety instructions"*); the Atmosphere/Air/Climate mission explicitly excludes replacing official advisories. The Sensitive / Deny-by-Default Register lists "Emergency warning misuse" as a `DENY` class. NOAA-derived layers that drift toward live-warning rebroadcast must be quarantined and a `CorrectionNotice` issued.

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 9. Required artifacts and governance hooks

Every admitted NOAA sub-source must produce or reference the following, before any `PUBLISHED` edge can exist for content derived from it.

### 9.0 Receipts quick reference

The receipt class that anchors each NOAA source-role. CONFIRMED doctrine: *if no receipt exists, the operation did not happen in the governed sense.*

| If `source_role` is… | The **anchoring receipt** is… | NOAA examples requiring it |
|---|---|---|
| `observed` | `SourceDescriptor` + `RunReceipt` (ingest receipt) | Storm Events records; NWS station obs; Mesonet-adjacent obs |
| `regulatory-context` | `SourceDescriptor` + `RunReceipt` + `PolicyDecision(DENY rebroadcast)` + freshness state | NWS warnings/advisories/watches; explicit official-source redirect required |
| `modeled` | `SourceDescriptor` + **`ModelRunReceipt`** *(MUST)* | NWS forecast grids; HMS analyses; HRRR-Smoke; model fields |
| `aggregate` | `SourceDescriptor` + **`AggregationReceipt`** *(MUST)* | Climate normals; decadal anomalies; aggregated indicators |
| `candidate` | `SourceDescriptor` with `role_candidate_disposition: pending` | Any NOAA admission caught in QUARANTINE; PUBLISHED forbidden until merged |
| (any role, sensitive transform) | Add `RedactionReceipt` | If NOAA inputs are joined against sensitive features (rare habitats, archaeology, infrastructure) |

### 9.1 Required objects

<details>
<summary><strong>Required objects (click to expand)</strong></summary>

| Object | Purpose (CONFIRMED doctrine) | NOAA-specific note |
|---|---|---|
| `SourceDescriptor` | Records source identity, rights, role, sensitivity, cadence at admission. | One descriptor **per sub-source**, not one for the whole NOAA family. |
| `RunReceipt` / ingest receipt | Records the actual fetch operation (URL, request headers, ETag, Last-Modified, content-length, spec_hash). | Conditional GETs (ETag/If-None-Match) preferred. |
| `EvidenceRef` → `EvidenceBundle` | Resolves claims to source evidence. | Must resolve before any public claim authority. |
| `ValidationReport` | Schema, geometry, temporal, rights, sensitivity, evidence checks. | Per-sub-source validators; fails closed on high-risk ambiguity. |
| `PolicyDecision` | `ALLOW` / `RESTRICT` / `DENY` / `ABSTAIN` / `ERROR` for the operation. | `DENY` by default for live-warning rebroadcast. |
| `DecisionEnvelope` | Finite-outcome envelope at governed-API boundaries. | Required at every `/api/v1/...` boundary. |
| `LayerManifest` | Declares public-safe map layer, fields, styles, evidence hooks, policy badges. | Must carry `rights_statement`, `license_spdx`, `attribution`, review status. |
| `ReleaseManifest` + `RollbackCard` | Release decision and rollback target. | Per release, not per file. |
| `CorrectionNotice` | Public correction lineage linked to a claim/release. | Used when an NOAA-derived release is later found stale, mislabeled, or rights-limited. |
| `AggregationReceipt` | Pins geometry-scope when an aggregate (e.g., climate normal) is published. | MUST exist when `source_role = aggregate`. |
| `ModelRunReceipt` | Pins inputs, parameters, and version for any modeled product. | MUST exist when `source_role = modeled` (e.g., forecasts, model fields, HMS-derived analyses). |
| `RedactionReceipt` | Records public-safe transforms when sensitivity demands. | Less commonly triggered for NOAA than for archaeology/fauna/people; still required if KFM joins NOAA inputs against sensitive features. |

</details>

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 10. Validators and tests

Tests prove the doctrine is enforceable. The following are `PROPOSED` validator families required for any NOAA sub-source to reach `PUBLISHED`.

- Schema validation against `schemas/contracts/v1/source/source_descriptor.schema.json` (and the relevant domain schemas).
- Source-role-mismatch denial: an NWS advisory cited as observation, a model field cited as observation, a climate normal cited per-place — each must `DENY`.
- Stale-warning denial: an advisory past its issue/expiry window must not appear on a public surface as live.
- Rights-unknown blocks release: missing or unresolved rights fail closed at the policy gate.
- `not-for-life-safety` banner presence on any NOAA-derived warning/advisory context layer.
- Citation validation: every `EvidenceRef` in a published NOAA-derived claim must resolve to an admissible `EvidenceBundle`.
- No-network fixtures: a deterministic, offline NOAA fixture exists for each sub-source (no live calls in CI).
- Rollback drill: at least one rehearsed rollback per NOAA release lane.
- DOM-AIR specific anti-collapse: AQI-as-concentration denial; AOD-as-PM2.5 denial; model-as-observed denial; low-cost-sensor caveat tests.

> [!NOTE]
> Test homes live under `tests/` and `fixtures/` per Directory Rules §5; specific test paths are `NEEDS VERIFICATION` until the repo is mounted.

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 11. Open questions & verification backlog

| # | Question | Label | Owner placeholder |
|---|---|---|---|
| **OPEN-NOAA-01** | Is `docs/sources/catalog/` the correct home, or should this live at `docs/sources/families/noaa.md` or flat at `docs/sources/noaa.md`? | `NEEDS VERIFICATION` (Directory Rules) | Docs steward |
| **OPEN-NOAA-02** | What is the authoritative inventory of admitted NOAA sub-sources (Storm Events, NWS API, HMS, etc.) at the moment? | `UNKNOWN` until the source register is inspected | Hazards + Atmosphere stewards |
| **OPEN-NOAA-03** | Are the rights/current terms for each NOAA sub-source recorded with a rights statement and license SPDX, per release-gate requirement? | `NEEDS VERIFICATION` | Source-registry steward |
| **OPEN-NOAA-04** | Does the `connectors/noaa/` package currently implement conditional GETs (ETag / If-None-Match) for all NOAA sub-sources? | `NEEDS VERIFICATION` | Connector owner |
| **OPEN-NOAA-05** | Is there a per-sub-source `not-for-life-safety` banner test wired into the governed-API responses for NOAA-derived layers? | `PROPOSED` | UI / governed-API owner |
| **OPEN-NOAA-06** | Where do NOAA-derived `AggregationReceipt`s live for climate normals — under `data/receipts/` or `data/proofs/`? | `NEEDS VERIFICATION` | Catalog / release steward |
| **OPEN-NOAA-07** | Is there an ADR governing the `source_role` enum exactly as `observed \| regulatory \| modeled \| aggregate \| administrative \| candidate \| synthetic`, or are the field names still proposed? | `NEEDS VERIFICATION` (ADR-0001 covers schema home, not role enum specifically) | Schema steward |
| **OPEN-NOAA-08** | Should NOAA sub-sources have their own product-page docs at `docs/sources/catalog/noaa/<sub-source>.md` (parallel to the newspapers/<product>.md pattern), or stay inside this single family entry? | `PROPOSED` | Docs steward |
| **OPEN-NOAA-09** | Is the `regulatory-context` shorthand (used in §5) precise enough, or does it need its own enum value distinct from `regulatory`? An ADR is likely warranted. | `PROPOSED` | Schema steward |
| **OPEN-NOAA-10** | Resolve `PROV.md` vs `PROVENANCE.md` reference target inherited from Directory Rules §18 OPEN-DR-01. | `NEEDS VERIFICATION` | Docs steward |

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## 12. Related docs

- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../SOURCE_DESCRIPTOR_STANDARD.md) — *PROPOSED — cross-source descriptor standard*
- [`docs/sources/catalog/README.md`](./README.md) — Catalog landing page
- [`docs/sources/catalog/newspapers/legal-notices.md`](./newspapers/legal-notices.md) — Sibling family product-page (different family; useful structural reference for `authority`-default)
- [`docs/sources/catalog/newspapers/obituaries.md`](./newspapers/obituaries.md) — Sibling family product-page (`candidate`-default)
- [`docs/sources/catalog/newspapers/ocr-full-text.md`](./newspapers/ocr-full-text.md) — Sibling family product-page (`observation` + `ModelRunReceipt`)
- [`docs/domains/hazards/README.md`](../../domains/hazards/README.md) — *Hazards domain dossier*
- [`docs/domains/atmosphere/README.md`](../../domains/atmosphere/README.md) — *Atmosphere/Air/Climate domain dossier*
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — *this catalog entry's placement authority*
- [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — *RAW → … → PUBLISHED invariant*
- [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) — *public-API-only consumption rule*
- [`docs/doctrine/truth-posture.md`](../../doctrine/truth-posture.md) — *cite-or-abstain*
- [`docs/adr/ADR-0001-schema-home.md`](../../adr/ADR-0001-schema-home.md) — *schema-home convention*
- `schemas/contracts/v1/source/source_descriptor.schema.json` — *PROPOSED — canonical SourceDescriptor*
- `connectors/noaa/README.md` — *NOAA-specific connector docs*
- `policy/release/hazards/` — *release policy for hazard-derived layers*
- `policy/release/atmosphere/` — *release policy for atmosphere-derived layers*
- `policy/sensitivity/` — *deny-by-default register implementation*

> [!NOTE]
> Anchors above assume the proposed `docs/sources/catalog/noaa.md` location. If this file lands elsewhere (`docs/sources/families/noaa.md`, `docs/sources/noaa.md`, etc.), inbound links from sibling docs and the registers will need to be updated together. Several relative paths in this list assume the proposed home and are PROPOSED until the path question (OPEN-NOAA-01) is resolved.

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## Appendix A — Source-role field crosswalk (PROPOSED)

Excerpted from KFM Atlas v1.1 §24.1.3. Field names below are `PROPOSED` shape; actual SourceDescriptor field names are `NEEDS VERIFICATION` against the mounted schema. Names are reproduced verbatim to preserve KFM terminology.

| Field | Type / vocabulary | Required when | NOAA-family note |
|---|---|---|---|
| `source_role` | enum: `observed \| regulatory \| modeled \| aggregate \| administrative \| candidate \| synthetic` | always (MUST) | Set at admission; never edited in-place. NOAA family spans `observed`, `regulatory`, `modeled`, `aggregate`. |
| `role_authority` | string (issuing body / model identity / steward) | when role ∈ {regulatory, modeled, aggregate} | For NWS warnings, NWS is the issuing authority — KFM is not. |
| `role_aggregation_unit` | geometry-scope token (county, HUC, tract, year, decade, etc.) | when `source_role = aggregate` | Climate normals and decadal anomalies must pin a unit. |
| `role_model_run_ref` | `EvidenceRef` → `ModelRunReceipt` | when `source_role = modeled` | NWS forecast grids, HMS analyses, HRRR-Smoke, model fields. |
| `role_synthetic_basis` | structured `{ method, inputs, reality_boundary_note_ref }` | when `source_role = synthetic` | Not expected for NOAA admissions. |
| `role_candidate_disposition` | enum: `pending \| merged \| rejected \| quarantined` | when `source_role = candidate` | Used for NOAA records caught in quarantine before merge. |

[Back to top ↑](#noaa-source-family--catalog-entry)

---

## Appendix B — Glossary

| Term | Working definition (CONFIRMED doctrine) |
|---|---|
| `SourceDescriptor` | The admission record for a source: identity, role, rights, sensitivity, cadence, citation, ingest hash, time. Anchors every downstream receipt. |
| `EvidenceRef` / `EvidenceBundle` | Reference and its resolved evidence package. Public claims require both. |
| `AdvisoryContext` / `WarningContext` | KFM object families that wrap NWS-style advisories/warnings as **contextual** evidence, never as KFM-issued alerts. |
| `HazardEvent` / `HazardObservation` | Hazards-domain object families that receive NOAA Storm Events records (and similar) under `source_role = observed`. |
| `ClimateNormal` / `ClimateAnomaly` | Atmosphere/Air/Climate object families that receive NOAA climate products under `source_role = aggregate`, with `AggregationReceipt`. |
| `ModelRunReceipt` | Receipt pinning model identity, inputs, parameters, version when `source_role = modeled`. Required for NWS forecasts, HMS-derived analyses, HRRR-Smoke, and other model fields. |
| `AggregationReceipt` | Receipt pinning geometry-scope and aggregation method when `source_role = aggregate`. |
| Trust membrane | Doctrine that public clients consume only governed APIs and released payloads — never RAW, WORK, QUARANTINE, canonical stores, or unpublished candidates. |
| Lifecycle invariant | `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a governed state transition, not a file move. |

[Back to top ↑](#noaa-source-family--catalog-entry)

---

**Related docs:** [hazards domain](../../domains/hazards/README.md) · [atmosphere domain](../../domains/atmosphere/README.md) · [source descriptor standard](../SOURCE_DESCRIPTOR_STANDARD.md) · [directory rules](../../doctrine/directory-rules.md) · [catalog root](./README.md)
**Last updated:** `2026-05-22` *(v1.1 polish pass; full review pass still pending)*
**Version:** `v1.1` · **Status:** `draft` · **Default `source_role`:** *multi-role (see [§5.0](#50-quick-reference))* · **Owners:** *PLACEHOLDER*

[Back to top ↑](#noaa-source-family--catalog-entry)
