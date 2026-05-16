<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/atmosphere/map-ui-contracts
title: Atmosphere/Air — Map & UI Contracts
type: standard
version: v0.1
status: draft
owners: <atmosphere-air domain steward> + <map-ui contract steward>  # PLACEHOLDER — assign in repo
created: 2026-05-16
updated: 2026-05-16
policy_label: public
related:
  - docs/domains/atmosphere/README.md            # PROPOSED — verify presence
  - docs/architecture/map-shell.md               # PROPOSED — verify presence
  - docs/architecture/governed-api.md            # PROPOSED — verify presence
  - docs/adr/ADR-0001-schema-home.md             # CONFIRMED doctrine; verify file presence
  - schemas/contracts/v1/map/                    # PROPOSED — verify presence per ADR-0001
  - schemas/contracts/v1/ui/                     # PROPOSED — verify presence per ADR-0001
  - schemas/contracts/v1/ai/                     # PROPOSED — verify presence per ADR-0001
tags: [kfm, atmosphere, air, map, ui, contracts, evidence-drawer, focus-mode, knowledge-character]
notes:
  - Lane name "atmosphere/" CONFIRMED from directory-rules.md §5, §12.
  - Lane name conflict with Atlas crosswalk "air/" surfaced in §11 (Open Questions).
[/KFM_META_BLOCK_V2] -->

# Atmosphere/Air — Map & UI Contracts

> Defines how Atmosphere/Air objects bind to the KFM map shell, Evidence Drawer, Focus Mode, and release manifests — and the knowledge-character discipline that public surfaces must enforce before render.

<!-- Badges: placeholders until CI/owners are confirmed in the mounted repo -->
![status: draft](https://img.shields.io/badge/status-draft-lightgrey)
![doctrine: CONFIRMED](https://img.shields.io/badge/doctrine-CONFIRMED-blue)
![implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-orange)
![lifecycle: RAW→PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-success)
![policy: public-safe-only](https://img.shields.io/badge/policy-public--safe--only-informational)
![last updated: 2026-05-16](https://img.shields.io/badge/updated-2026--05--16-blue)

**Status:** draft · **Owners:** `<atmosphere-air steward>` + `<map-ui contract steward>` *(placeholder — assign)* · **Updated:** 2026-05-16

---

## Contents

1. [Scope and boundary](#1-scope-and-boundary)
2. [Authority hierarchy and source posture](#2-authority-hierarchy-and-source-posture)
3. [Contract surface (KFM map/UI object families)](#3-contract-surface-kfm-mapui-object-families)
4. [Atmosphere/Air layer families and knowledge-character labels](#4-atmosphereair-layer-families-and-knowledge-character-labels)
5. [LayerManifest atmosphere-specific expectations](#5-layermanifest-atmosphere-specific-expectations)
6. [Trust-visible state, badges, and freshness](#6-trust-visible-state-badges-and-freshness)
7. [Click resolution and the Evidence Drawer](#7-click-resolution-and-the-evidence-drawer)
8. [Focus Mode and MapContextEnvelope for atmosphere](#8-focus-mode-and-mapcontextenvelope-for-atmosphere)
9. [Finite outcomes on public map surfaces](#9-finite-outcomes-on-public-map-surfaces)
10. [Lifecycle, promotion gates, and rollback](#10-lifecycle-promotion-gates-and-rollback)
11. [Anti-collapse rules — knowledge-character denials](#11-anti-collapse-rules--knowledge-character-denials)
12. [Cross-lane relations](#12-cross-lane-relations)
13. [Validators, tests, fixtures](#13-validators-tests-fixtures)
14. [Open questions and verification backlog](#14-open-questions-and-verification-backlog)
15. [Related docs](#15-related-docs)

---

## 1. Scope and boundary

> [!IMPORTANT]
> This document is a **map/UI contract specification** for the Atmosphere/Air lane. It governs how atmospheric objects bind to KFM's released map artifacts and trust-visible UI surfaces. It is not an emergency-alert system, an advisory authority, or a substitute for the official sources it carries.

**In scope.** CONFIRMED doctrine / PROPOSED implementation:

- How Atmosphere/Air objects map onto the KFM `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `MapReleaseManifest`, `EvidenceDrawerPayload`, `MapContextEnvelope`, `FocusModeRequest/Response`, and `AIReceipt` contracts.
- Required knowledge-character labels on every air-quality, smoke, model-field, and remote-sensing layer.
- Trust-visible state expectations (freshness, stale/degraded, redaction posture, denial reasons).
- Finite-outcome semantics on every governed surface that touches an atmosphere layer.
- Cross-lane boundaries with Hazards, Hydrology, Agriculture, and biodiversity domains.

**Out of scope.** CONFIRMED / PROPOSED:

- **Not** an emergency-alert authority; KFM never replaces NOAA/NWS, KDHE, AirNow, or other official advisory issuers. [DOM-AIR][ENCY]
- **Not** a source-onboarding spec — that lives with the source descriptor catalogs, not here.
- **Not** a renderer build guide — MapLibre toolchain, style authoring, and tile generation are owned by the map shell and packages docs.
- **Not** a schema definition — JSON Schemas live under `schemas/contracts/v1/...` per ADR-0001; this doc describes intent and atmosphere-specific bindings.

[↑ Back to top](#contents)

---

## 2. Authority hierarchy and source posture

> [!NOTE]
> The Atmosphere/Air domain is doctrinally subordinate to (a) KFM trust-membrane invariants, (b) Directory Rules, and (c) the Master MapLibre operating architecture for renderer behavior. This file refines map/UI binding details for atmosphere only; it never overrides upstream doctrine.

CONFIRMED authority hierarchy for atmosphere map/UI surfaces:

| # | Authority | What it owns | Citation |
|---|---|---|---|
| 1 | **Directory Rules** | Responsibility-root placement; lane = `atmosphere/`. | [DIRRULES] §5, §12 |
| 2 | **DOM-AIR dossier + Encyclopedia §7.9** | Atmosphere/Air knowledge-character discipline; object families; source roles. | [DOM-AIR][ENCY] |
| 3 | **Master MapLibre architecture / UIAI-MAP** | Renderer boundary; Evidence Drawer; Focus Mode; finite outcomes. | [MAP-MASTER][UIAI-MAP] |
| 4 | **Governed AI dossier** | AIReceipt, citation validation, cite-or-abstain posture. | [GAI] |
| 5 | **This file** | Atmosphere-specific binding rules on the contract surfaces above. | (this doc) |

**Source-role posture (CONFIRMED / PROPOSED).** Atmosphere/Air source families include EPA AQS-like archive, AirNow / agency reporting, OpenAQ-like aggregators, NOAA/NWS, Kansas Mesonet, CAMS / ECMWF-family model fields, HRRR-Smoke, HMS smoke, GOES/ABI AOD, VIIRS fire/hotspot, and PurpleAir-class low-cost sensors with EPA correction. Each family is admitted with a single source role — `authority`, `observation`, `context`, or `model` — and **roles are never silently collapsed** at the UI layer. [DOM-AIR][ENCY]

[↑ Back to top](#contents)

---

## 3. Contract surface (KFM map/UI object families)

CONFIRMED doctrine: every atmosphere layer renders through this fixed set of contracts. PROPOSED implementation: all schema home paths below resolve under `schemas/contracts/v1/...` per ADR-0001 and remain UNKNOWN until verified in a mounted repo.

| Contract | Role in atmosphere map UI | Required atmosphere bindings | PROPOSED schema home |
|---|---|---|---|
| `SourceDescriptor` | Admits an air/weather/smoke source with role, rights, sensitivity, cadence, limitations. | `source_role` ∈ {authority, observation, context, model}; `cadence`; `rights_status`. | `schemas/contracts/v1/sources/source_descriptor.schema.json` |
| `LayerManifest` | Binds a UI layer to source/evidence/policy/release. | `evidence_ref_field`; `temporal_fields`; `policy_label`; `release_state`; **atmosphere-specific** knowledge-character label (§5). | `schemas/contracts/v1/map/layer_manifest.schema.json` |
| `StyleManifest` | Versioned style identity, sprites, glyphs, digest. | Style validation; only references released atmosphere `layer_ids`. | `schemas/contracts/v1/map/style_manifest.schema.json` |
| `TileArtifactManifest` | Binds PMTiles/MVT/COG bytes to digest + range/CORS. | Atmosphere rasters (e.g., AOD, model fields) carry COG layout + NODATA + CRS proof. | `schemas/contracts/v1/map/tile_artifact_manifest.schema.json` |
| `MapReleaseManifest` | Complete published map release. | Atmosphere layers grouped by knowledge-character class; `rollback_target` required. | `schemas/contracts/v1/map/map_release_manifest.schema.json` |
| `EvidenceBundle` | Truth-bearing evidence object. | `domain: "atmosphere"`; `observation_basis`; `units`; `temporal_basis`. | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` |
| `EvidenceDrawerPayload` | Click-resolution payload. | Atmosphere-class limitations (e.g., "low-cost sensor; EPA Barkjohn correction applied"). | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` |
| `MapContextEnvelope` | Bounded map context for Focus Mode. | Includes `visible_layers` with knowledge-character class so Focus Mode never crosses classes silently. | `schemas/contracts/v1/ui/map_context_envelope.schema.json` |
| `FocusModeRequest` / `Response` | Governed AI question/answer over atmosphere context. | Finite outcome required; atmosphere-specific abstain reasons enumerated. | `schemas/contracts/v1/ai/focus_mode_*.schema.json` |
| `AIReceipt` | Audit trail for model execution. | Records evidence used + atmosphere policy decisions. | `schemas/contracts/v1/ai/ai_receipt.schema.json` |
| `CitationValidationReport` | Cite-or-abstain enforcement. | Atmosphere AI answers fail closed when citation refs don't resolve. | `schemas/contracts/v1/evidence/citation_validation_report.schema.json` |
| `PolicyDecision` | Atmosphere policy verdict and obligations. | Carries obligations like *show freshness warning*, *show source-role label*, *generalize geometry*. | `schemas/contracts/v1/policy/policy_decision.schema.json` |
| `PromotionDecision` | Governed transition to PUBLISHED. | Includes atmosphere-specific gates (units, AQI vs. concentration, model vs. observed). | `schemas/contracts/v1/policy/promotion_decision.schema.json` |

> [!NOTE]
> Contract field lists above reflect the Master MapLibre object-map (CONFIRMED doctrine from [MAP-MASTER]). Atmosphere-specific bindings are PROPOSED additions; all field-level additions require schema and ADR confirmation in the mounted repo.

[↑ Back to top](#contents)

---

## 4. Atmosphere/Air layer families and knowledge-character labels

CONFIRMED doctrine: atmosphere layers split into **non-interchangeable knowledge-character classes**. PROPOSED implementation: each class becomes a `LayerManifest.knowledge_character` value (or equivalent enum); public surfaces must display the label and never collapse classes. [DOM-AIR][ENCY]

```mermaid
flowchart LR
  subgraph CLASS["Atmosphere/Air knowledge-character classes (PROPOSED)"]
    OBS["observed_sensor<br/>(regulatory & reference monitors)"]
    AQI["public_aqi_report<br/>(AirNow-class index)"]
    REG["regulatory_archive<br/>(EPA AQS-class QA/QC)"]
    LCS["low_cost_sensor<br/>(PurpleAir-class; correction applied)"]
    MODEL["model_field<br/>(HRRR-Smoke, CAMS, forecast)"]
    EO["remote_sensing<br/>(GOES/ABI AOD, VIIRS hotspot, HMS mask)"]
    CLIM["climate_context<br/>(normals, anomalies)"]
    FUSION["derived_fusion<br/>(multi-source synthesis)"]
    ADV["advisory_context<br/>(redirect to official issuer)"]
  end
  CLASS --> LM["LayerManifest<br/>knowledge_character label"]
  LM --> DRAWER["Evidence Drawer<br/>shows class + limitations"]
  LM --> FOCUS["Focus Mode<br/>refuses cross-class claims w/o evidence"]
```

| Class | Map family | Knowledge-character label | Source-role binding | Sensitivity default |
|---|---|---|---|---|
| `observed_sensor` | Air-quality stations, weather stations, mesonet points. | "Observation" | observation | public |
| `public_aqi_report` | Public AQI report layers. | "Public AQI report (index, not concentration)" | authority / context | public |
| `regulatory_archive` | EPA AQS-class regulatory archive. | "Regulatory archive (QA/QC)" | authority | public |
| `low_cost_sensor` | PurpleAir-class community sensors. | "Low-cost sensor — correction applied; see limitations" | observation (corrected) | public-with-caveat |
| `model_field` | HRRR-Smoke, CAMS, ECMWF forecasts. | "Model field — not an observation" | model | public-with-caveat |
| `remote_sensing` | GOES/ABI AOD, VIIRS, HMS smoke. | "Remote sensing — derivative; not in-situ" | observation (remote) | public-with-caveat |
| `climate_context` | Climate normals, anomalies. | "Climate context — long-record reference" | context | public |
| `derived_fusion` | Multi-source synthesis (e.g., PM2.5 fusion outputs). | "Derived fusion — uncertainty inherited" | derived | public-with-caveat |
| `advisory_context` | Advisory layer with redirect to official issuer. | "Advisory context — not a KFM-issued advisory" | context | public |

> [!CAUTION]
> The label is **load-bearing UI state**, not decoration. A `model_field` layer that loses its class label and appears as a generic point measurement is a knowledge-character violation regardless of geometry correctness. CI must include a regression that asserts each atmosphere layer in a `MapReleaseManifest` carries a populated knowledge-character label. [PROPOSED]

[↑ Back to top](#contents)

---

## 5. LayerManifest atmosphere-specific expectations

PROPOSED additions to `LayerManifest` for atmosphere layers, layered on the CONFIRMED Master MapLibre field set (`layer_id`, `title`, `geometry_type`, `source_id`, `source_layer`, `evidence_ref_field`, `temporal_fields`, `policy_label`, `release_state`):

| Field (PROPOSED) | Purpose | Example | Validator behavior |
|---|---|---|---|
| `knowledge_character` | Class label from §4 enum. | `"model_field"` | FAIL CLOSED if missing or unknown enum. |
| `parameter` | Pollutant / weather parameter. | `"PM2.5"`, `"O3"`, `"AOD550"`, `"wind_10m"` | FAIL CLOSED if missing on `observed_sensor` / `regulatory_archive` / `low_cost_sensor`. |
| `unit` | Reported unit (no implicit conversion). | `"µg/m³"`, `"ppb"`, `"dimensionless"` | FAIL CLOSED if missing for measurement parameters. |
| `correction_method` | Required for low-cost sensors. | `"EPA Barkjohn v1"` | FAIL CLOSED on `low_cost_sensor` without method. |
| `model_run_time` | Required for `model_field`. | ISO-8601 | FAIL CLOSED on `model_field` without run time. |
| `valid_time_window` | Validity period for model/forecast layers. | `[start, end]` ISO-8601 | FAIL CLOSED if absent on `model_field` / `advisory_context`. |
| `temporal_basis` | Aggregation basis. | `"hourly"`, `"daily_summary"`, `"24h_avg"` | FAIL CLOSED on regulatory/observed layers. |
| `source_role_label` | Display string echoing the source role. | `"observation"`, `"authority"`, `"model"`, `"context"` | FAIL CLOSED if not consistent with `SourceDescriptor.source_role`. |
| `freshness_policy` | Stale/degraded thresholds for this layer. | `{"warn_after_minutes": 90, "stale_after_minutes": 240}` | Used by §6 trust-visible state machine. |
| `redaction_profile` | Reference to redaction receipt if applicable. | `"kfm://redaction/<id>"` | FAIL CLOSED if `sensitivity != public` and no profile. |
| `advisory_redirect` | Required for `advisory_context`. | `{"issuer": "...", "url": "..."}` | FAIL CLOSED on `advisory_context` without redirect. |

> [!TIP]
> `temporal_fields` (CONFIRMED Master MapLibre field) on atmosphere layers must enumerate distinct **source time**, **observed time**, **valid time**, **retrieval time**, **release time**, and **correction time** where material. CONFIRMED doctrine: these times stay distinct on every atmosphere object. [DOM-AIR §F][ENCY]

<details>
<summary><strong>Illustrative LayerManifest excerpt (PROPOSED; illustrative only)</strong></summary>

```json
{
  "object_type": "LayerManifest",
  "schema_version": "v1",
  "layer_id": "atmosphere.pm25.observed.airnow.hourly",
  "title": "PM2.5 — AirNow public report (hourly)",
  "geometry_type": "Point",
  "source_id": "<source_descriptor_id>",
  "source_layer": "pm25_airnow_hourly",
  "knowledge_character": "public_aqi_report",
  "parameter": "PM2.5",
  "unit": "µg/m³",
  "temporal_basis": "hourly",
  "source_role_label": "authority",
  "evidence_ref_field": "evidence_ref",
  "temporal_fields": {
    "observed_time": "observed_at",
    "valid_time": "valid_at",
    "retrieval_time": "retrieved_at",
    "release_time": "released_at"
  },
  "policy_label": "public",
  "release_state": "PUBLISHED",
  "freshness_policy": { "warn_after_minutes": 90, "stale_after_minutes": 240 }
}
```

This snippet is **illustrative only**. Field names and enum values are PROPOSED and must be confirmed against the actual `schemas/contracts/v1/map/layer_manifest.schema.json` in the mounted repo.
</details>

[↑ Back to top](#contents)

---

## 6. Trust-visible state, badges, and freshness

CONFIRMED doctrine (Master MapLibre): the MapLibre shell **must** show released layer state, stale/degraded badges, evidence resolution, denial/abstain reasons, and correction/rollback visibility — without exposing raw or restricted data. Atmosphere/Air refines this with class-aware badges.

### 6.1 Required trust-visible states per atmosphere class

| State | Triggered when | UI rendering | Click behavior |
|---|---|---|---|
| `fresh` | Within `freshness_policy.warn_after_minutes`. | Default badge. | Opens Evidence Drawer. |
| `warn` | Past `warn_after_minutes`, before `stale_after_minutes`. | Distinct warn badge; tooltip with last-update time. | Opens Evidence Drawer with freshness banner. |
| `stale` | Past `stale_after_minutes`. | Distinct stale badge; reduced visual emphasis. | Opens Evidence Drawer; Focus Mode flags as stale evidence. |
| `degraded_stream` | Source stream falling back to polling, sparse updates. | Stream-degraded badge. | Evidence Drawer notes streaming posture. |
| `correction_applied` | Low-cost sensor with correction. | Correction badge. | Evidence Drawer shows correction method + caveat. |
| `redacted_or_generalized` | Sensitivity transform applied. | Redaction badge with transform reason. | Evidence Drawer surfaces redaction receipt (without restricted geometry). |
| `quarantined_excluded` | AOD or other gate excluded this source from a fusion product. | Not rendered on public layer; appears only in steward views. | n/a on public surface. |

### 6.2 Anti-patterns

> [!WARNING]
> The following are **trust violations** regardless of technical correctness:
>
> - **Badge as proof substitute.** A badge that decorates a tile without resolving to a receipt or `EvidenceBundle`. [MAP-MASTER]
> - **Popup as Evidence Drawer substitute.** Popups may summarize; only the Evidence Drawer resolves evidence and trust state. [MAP-MASTER]
> - **Sensitive geometry hidden only by style.** Style toggling never substitutes for upstream redaction/generalization with a recorded receipt. [MAP-MASTER]
> - **Visual sameness across knowledge-character classes.** `observed_sensor` and `model_field` must not render identically; the user must see they're different epistemic kinds. [DOM-AIR]
> - **Source-role mismatch in display.** A `model_field` layer must never be labeled or described as an observation. [DOM-AIR][ENCY]

[↑ Back to top](#contents)

---

## 7. Click resolution and the Evidence Drawer

CONFIRMED doctrine (Master MapLibre):
> *released layer → user click → governed API → EvidenceBundle → Evidence Drawer → Focus Mode answer / abstain / deny / error*

This is the only path. Public clients **never** read RAW, WORK, QUARANTINE, candidate, or canonical/internal stores — atmosphere included.

```mermaid
sequenceDiagram
  autonumber
  participant U as User (map shell)
  participant ML as MapLibre layer<br/>(atmosphere, released)
  participant API as Governed API
  participant EB as EvidenceBundle resolver
  participant POL as PolicyDecision
  participant DR as Evidence Drawer
  participant FM as Focus Mode (optional)
  U->>ML: click feature
  ML->>API: feature_id + layer_id (released only)
  API->>EB: resolve EvidenceRef
  API->>POL: evaluate policy/rights/sensitivity
  POL-->>API: outcome + obligations
  alt outcome = ANSWER
    EB-->>API: EvidenceBundle (atmosphere)
    API-->>DR: EvidenceDrawerPayload
    DR-->>U: render citations + class + limitations
  else outcome = ABSTAIN
    API-->>DR: abstain payload + reason
    DR-->>U: "Evidence insufficient — see why"
  else outcome = DENY
    API-->>DR: deny payload + reason_code
    DR-->>U: denial with non-restricted alternative
  else outcome = ERROR
    API-->>DR: error envelope (no claim leakage)
    DR-->>U: actionable error
  end
  U->>FM: optional follow-up question
  FM->>API: FocusModeRequest with MapContextEnvelope
  API-->>FM: FocusModeResponse + AIReceipt
```

### 7.1 EvidenceDrawerPayload — atmosphere-specific surfaces

CONFIRMED Master MapLibre fields (`feature_id`, `layer_id`, `evidence_bundle_refs`, source summary, citations, policy state, release state, limitations). Atmosphere PROPOSED additions:

- **Knowledge-character chip.** Class label from §4, rendered prominently.
- **Parameter + unit chip.** e.g., `PM2.5 · µg/m³` — never elided into a unitless number.
- **Source-role chip.** `observation` / `authority` / `model` / `context` — must agree with `SourceDescriptor.source_role`.
- **Temporal chip(s).** Distinguished `observed_time` / `valid_time` / `model_run_time` / `release_time` per class.
- **Correction chip.** For `low_cost_sensor`: correction method + version.
- **Stale / degraded chip.** From §6 state machine.
- **Limitations panel.** Required for `low_cost_sensor`, `model_field`, `remote_sensing`, `derived_fusion`. Free-text bounded by the layer's `EvidenceBundle.limitations`.
- **Advisory redirect.** For `advisory_context` only: link to the official issuer (NOAA/NWS, KDHE, AirNow, etc.); KFM never paraphrases the advisory.

[↑ Back to top](#contents)

---

## 8. Focus Mode and MapContextEnvelope for atmosphere

CONFIRMED doctrine (UIAI-MAP, GAI): Focus Mode is bounded — it answers, abstains, denies, or errors over **released atmosphere context only**. It never substitutes for evidence and never reaches RAW/WORK/QUARANTINE.

### 8.1 MapContextEnvelope rules

The envelope passed to Focus Mode must:

1. **Enumerate visible atmosphere layers with their knowledge-character class.** Focus Mode reasoning that crosses classes without explicit evidence is treated as ABSTAIN. [DOM-AIR §L][GAI]
2. **Carry only EvidenceRefs** — never raw features or restricted geometry. [MAP-MASTER]
3. **Include the time window** that the user has actually scoped (timeline state), not the model's preferred window.
4. **Include selected_features** as IDs only; evidence resolves through the governed API.
5. **Include freshness state** from §6 so the model can refuse to claim "current PM2.5" over stale evidence.

### 8.2 Atmosphere-specific abstain and deny patterns

CONFIRMED doctrine / PROPOSED enumeration of reason codes for atmosphere:

| Outcome | reason_code (PROPOSED) | When |
|---|---|---|
| ABSTAIN | `atmosphere.evidence_insufficient` | Question requires evidence not present in the envelope. |
| ABSTAIN | `atmosphere.evidence_stale` | Layer is `stale`; no released alternative is available. |
| ABSTAIN | `atmosphere.knowledge_character_cross_class` | Answering would require mixing `model_field` and `observed_sensor` claims as one. |
| ABSTAIN | `atmosphere.citation_unresolved` | One or more EvidenceRefs failed to resolve. |
| DENY | `atmosphere.alert_authority_substitution` | User asks Focus Mode to issue an advisory or life-safety instruction. |
| DENY | `atmosphere.exact_location_restricted` | Cross-lane request would expose a restricted location (e.g., sensitive species locality from biodiversity). |
| DENY | `atmosphere.unit_collapse` | User asks for AQI as concentration or AOD as PM2.5 (see §11). |
| DENY | `atmosphere.model_as_observed` | User asks the model to assert a forecast as if it were observed. |
| DENY | `atmosphere.rights_unresolved` | Source rights are NEEDS VERIFICATION; output blocked until resolved. |
| ERROR | `atmosphere.contract_violation` | Malformed envelope, schema violation, or missing required field. |

> [!IMPORTANT]
> Focus Mode must never **silently** rephrase a question that would otherwise hit one of the DENY codes above. The path is: detect → DENY with `reason_code` → offer a non-restricted alternative where possible. [GAI][DOM-AIR §L]

[↑ Back to top](#contents)

---

## 9. Finite outcomes on public map surfaces

CONFIRMED doctrine: every governed surface returns a finite outcome from a small, well-known set. PROPOSED atmosphere binding:

| Surface | Outcomes | Forbidden behavior |
|---|---|---|
| Atmosphere feature/detail resolver | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Returning unreleased candidate as ANSWER; exposing internal store IDs. |
| Atmosphere layer manifest resolver | `ANSWER` / `DENY` / `ERROR` | Serving a layer that lacks a `ReleaseManifest`; serving WORK/CATALOG-stage layers. |
| Atmosphere Evidence Drawer payload | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Returning raw bytes; bypassing policy filter. |
| Atmosphere Focus Mode | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Treating model output as observation; uncited claims. |
| Promotion gate (internal) | `PASS` / `FAIL` / `HOLD` | Promoting without unit/parameter validation; without knowledge-character label. |

[↑ Back to top](#contents)

---

## 10. Lifecycle, promotion gates, and rollback

CONFIRMED doctrine: Atmosphere/Air follows the KFM invariant `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a governed state transition, not a file move. [DIRRULES][DOM-AIR][ENCY]

```mermaid
flowchart LR
  RAW[("RAW<br/>SourceDescriptor exists")]
  WORK[("WORK / QUARANTINE<br/>schema, units, geometry, identity, evidence, rights, policy")]
  PROC[("PROCESSED<br/>EvidenceRef + ValidationReport + digest closure")]
  CAT[("CATALOG / TRIPLET<br/>EvidenceBundle + catalog/proof closure")]
  PUB[("PUBLISHED<br/>ReleaseManifest + correction path + rollback target")]
  RAW --> WORK
  WORK -->|fail| Q[(QUARANTINE<br/>reason recorded)]
  WORK --> PROC
  PROC --> CAT
  CAT --> PUB
  PUB -. correction .-> CAT
  PUB -. rollback .-> PUB
```

### 10.1 Atmosphere-specific publication gates (PROPOSED)

Promotion to `PUBLISHED` requires all of:

- [ ] `SourceDescriptor` present with explicit `source_role`.
- [ ] Parameter and unit validation passed (no implicit unit conversion).
- [ ] Knowledge-character label assigned and matches source role.
- [ ] Freshness state computable (`temporal_fields` complete enough for §6).
- [ ] `EvidenceBundle` closure: `evidence_refs` resolve; `spec_hash` set; `rights_status` ≠ `unknown`; `sensitivity` set.
- [ ] `PolicyDecision = allow` with any obligations recorded on the layer.
- [ ] `ReleaseManifest` present with `rollback_target`.
- [ ] For `low_cost_sensor`: correction method + version recorded.
- [ ] For `model_field` / `remote_sensing`: limitations text present in the bundle.
- [ ] No-network / dry-run fixture passes (no live fetch on publication path).

> [!CAUTION]
> Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks** public promotion. CONFIRMED doctrine. [ENCY][DIRRULES]

### 10.2 Rollback and correction

- **Rollback**: `RollbackCard` repoints current released state to a prior `ReleaseManifest`; history is preserved, not destroyed.
- **Correction**: a published claim is corrected via `CorrectionNotice` and a new `ReleaseManifest`, with the correction lineage carried forward. The Evidence Drawer surfaces `correction_state` so users see when a layer was corrected.

[↑ Back to top](#contents)

---

## 11. Anti-collapse rules — knowledge-character denials

CONFIRMED doctrine (DOM-AIR, Encyclopedia §7.9): these denials are the **core trust posture** of the Atmosphere/Air lane in any UI. They must be enforced before render, before drawer display, and before any Focus Mode answer.

| Denial rule | Rationale | Required outcome |
|---|---|---|
| **AQI is not concentration.** | AQI is a public index, not µg/m³ or ppb. Treating them as the same number is a category error. | DENY (`atmosphere.unit_collapse`) any UI/API path that returns AQI as concentration or vice versa. |
| **AOD is not PM2.5.** | Aerosol optical depth is a column-integrated optical property; PM2.5 is a surface concentration. | DENY (`atmosphere.unit_collapse`) any UI/API path that elides AOD into PM2.5. |
| **Model fields are not observations.** | Forecast/analysis fields are model output regardless of how realistic they appear. | DENY (`atmosphere.model_as_observed`) any UI/API path that labels a `model_field` layer as observation. |
| **Low-cost sensor public release requires correction, caveats, confidence, limitations.** | PurpleAir-class outputs without EPA-style correction are not equivalent to regulatory monitors. | ABSTAIN or DENY in absence of `correction_method` + limitations on the layer. |
| **Smoke masks ≠ smoke exposure.** | A satellite smoke mask shows column-detected smoke; surface exposure requires HRRR-Smoke-class fields and ground evidence. | ABSTAIN when a UI/API path would conflate them. |
| **KFM is never an alert authority.** | KFM carries advisories as context only; users are redirected to official issuers. | DENY (`atmosphere.alert_authority_substitution`) for any path that would issue or paraphrase an advisory. |

> [!IMPORTANT]
> These rules apply uniformly across the map shell, click flow, Evidence Drawer, Focus Mode, exports, screenshots, and downstream APIs. A denial that fires only on one surface is a leak.

[↑ Back to top](#contents)

---

## 12. Cross-lane relations

CONFIRMED / PROPOSED: atmosphere joins with adjacent lanes must preserve ownership, source role, sensitivity, and `EvidenceBundle` support on both sides. [DOM-AIR §F][ENCY]

| Counterpart lane | Atmosphere relation | UI/contract constraint |
|---|---|---|
| **Hazards** | Smoke, heat/cold, advisory, visibility, fire/emissions context. | Atmosphere never asserts hazard alerts; hazards never replace atmosphere observations. Map shell renders each in its lane with its own `LayerManifest`. |
| **Hydrology** | Precipitation, drought signals, flood-weather forcing. | Joined views must cite both lanes' EvidenceBundles; no silent unit harmonization. |
| **Agriculture** | Heat, smoke, precipitation, vegetation stress. | Joins emit a derived layer with its own knowledge-character class (`derived_fusion`) and combined limitations. |
| **Biodiversity** (Fauna / Flora / Habitat) | Phenology, smoke, fire, drought stress. | **No exposure of sensitive species locations** via atmosphere overlay tricks. Generalize or deny per biodiversity sensitivity profile before render. |

[↑ Back to top](#contents)

---

## 13. Validators, tests, fixtures

PROPOSED test catalog for atmosphere map/UI contracts. CONFIRMED doctrine: every public-surface invariant must be enforced by a fixture or fail-closed gate; cite-or-abstain and no-network-on-publish are non-negotiable. [DOM-AIR §K][ENCY][MAP-MASTER]

### 13.1 Schema / contract tests

- [ ] `LayerManifest` schema validation, including atmosphere PROPOSED additions (§5).
- [ ] `StyleManifest` digest stability; only references released atmosphere `layer_ids`.
- [ ] `TileArtifactManifest` digest / range / CORS validation; COG layout/NODATA for raster atmosphere layers.
- [ ] `MapReleaseManifest` rollback-target presence; supersedes-chain coherence.
- [ ] `EvidenceBundle` closure: `evidence_refs` resolve, `spec_hash` deterministic, atmosphere extensions present.
- [ ] `EvidenceDrawerPayload` includes knowledge-character chip + parameter/unit chip + source-role chip.
- [ ] `MapContextEnvelope` carries `visible_layers` with knowledge-character class.

### 13.2 Negative / anti-pattern fixtures

| Fixture (PROPOSED) | Expected outcome |
|---|---|
| `aqi_as_concentration.json` | DENY |
| `aod_as_pm25.json` | DENY |
| `model_as_observed.json` | DENY |
| `low_cost_sensor_no_correction.json` | DENY |
| `missing_units.json` | DENY |
| `missing_knowledge_character.json` | FAIL CLOSED on promotion |
| `stale_air_window.json` | ABSTAIN |
| `raw_path_exposure.json` | DENY |
| `invalid_spec_hash.json` | DENY |
| `dryrun_live_fetch.json` | FAIL CLOSED |
| `alert_authority_substitution.json` | DENY |
| `cross_lane_sensitive_location_leak.json` | DENY |
| `popup_as_evidence_drawer.json` | FAIL CLOSED on UI snapshot test |
| `badge_without_receipt.json` | FAIL CLOSED on badge-binding test |

### 13.3 Accessibility, UX, and visual regression

CONFIRMED Master MapLibre expectation: trust-visible states require keyboard, contrast, badge-state, and screen-reader checks. PROPOSED atmosphere additions:

- Knowledge-character chip is reachable by keyboard and announced by screen readers.
- Stale / degraded / correction badges have distinct visual treatments and ARIA labels.
- Evidence Drawer renders correctly with each atmosphere class fixture.

[↑ Back to top](#contents)

---

## 14. Open questions and verification backlog

| # | Item | Status | What would resolve it |
|---|---|---|---|
| 1 | Atlas crosswalk uses `schemas/contracts/v1/air/`; Directory Rules §12 uses `atmosphere/` as lane. Two names for the same lane. | NEEDS VERIFICATION / ADR | ADR pinning the canonical lane name (`atmosphere` recommended, matching Directory Rules §12) and the schema-home segment. Atlas crosswalk to follow. |
| 2 | Exact schema file homes under `schemas/contracts/v1/...` for atmosphere additions to `LayerManifest`. | PROPOSED | Inspect mounted repo `schemas/contracts/v1/map/` and `schemas/contracts/v1/ui/`. |
| 3 | Whether `knowledge_character` belongs on `LayerManifest` directly or on a sidecar `AtmosphereLayerProfile`. | PROPOSED | ADR after schema-team review. |
| 4 | Exact route names for atmosphere feature/detail/layer manifest/Focus Mode resolvers. | UNKNOWN | Inspect mounted `apps/governed-api/` routes. |
| 5 | Source rights / terms / quotas for OpenAQ, AirNow, EPA AQS, NOAA, Mesonet, PurpleAir, CAMS, HRRR-Smoke, HMS, GOES/ABI, VIIRS. | NEEDS VERIFICATION | Source-onboarding receipts and the source registry under `data/registry/sources/atmosphere/`. |
| 6 | Whether `low_cost_sensor` correction is gated to EPA Barkjohn-class methods only. | PROPOSED | Policy gate decision + ADR. |
| 7 | Whether smoke advisories ever render as a dedicated atmosphere advisory layer or always defer to Hazards. | NEEDS VERIFICATION | Cross-lane ADR with Hazards. |
| 8 | Whether `AutomationBadgePayload` is in scope here or only on the Master MapLibre badge contracts. | PROPOSED | Confirm shared `packages/maplibre/` placement and reference from this doc rather than redefining. |
| 9 | Whether atmosphere `EvidenceBundle` extensions (`observation_basis`, `units`, `temporal_basis`) are typed in the bundle schema or in a domain sidecar. | PROPOSED | Schema-team ADR. |
| 10 | MLT (next-gen tile) pilot applicability to atmosphere rasters (AOD, model fields). | UNKNOWN | Map-shell pilot results; not a blocker for v0.1. |

[↑ Back to top](#contents)

---

## 15. Related docs

> [!NOTE]
> All paths below are **PROPOSED** until confirmed in the mounted repo. They follow Directory Rules placement.

- `docs/domains/atmosphere/README.md` — atmosphere lane landing page (PROPOSED; verify).
- `docs/domains/atmosphere/SOURCES.md` — atmosphere source families and roles (PROPOSED).
- `docs/domains/atmosphere/POLICY.md` — atmosphere sensitivity, rights, publication posture (PROPOSED).
- `docs/architecture/map-shell.md` — map shell operating architecture (PROPOSED; verify).
- `docs/architecture/governed-api.md` — trust-membrane and finite-outcome contract (PROPOSED; verify).
- `docs/adr/ADR-0001-schema-home.md` — schemas/contracts/v1 as canonical schema home (CONFIRMED doctrine; verify file).
- `docs/standards/PROV.md` — provenance profile (CONFIRMED file from project state).
- `docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md` — atmosphere refresh runbook (PROPOSED; not yet authored).
- `schemas/contracts/v1/map/layer_manifest.schema.json` — `LayerManifest` schema (PROPOSED home per ADR-0001).
- `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` — `EvidenceDrawerPayload` schema (PROPOSED home).
- `schemas/contracts/v1/ai/focus_mode_request.schema.json` / `focus_mode_response.schema.json` — Focus Mode contracts (PROPOSED home).

---

### Citation key (Atlas short-names)

- **[DIRRULES]** — Directory Rules.
- **[ENCY]** — KFM Domain and Capability Encyclopedia.
- **[DOM-AIR]** — Atmosphere/Air dossier (`KFM_Atmosphere_Air_PDF_Only_Architecture_Report_2026-04-21.pdf`).
- **[DOM-HAZ]** — Hazards dossier.
- **[MAP-MASTER]** — Master MapLibre Components-Functions-Features.
- **[UIAI-MAP]** — KFM MapLibre Operating Architecture (Governed UI/AI Interaction Manual).
- **[GAI]** — Governed AI dossier.

---

**Related docs:** see [§15](#15-related-docs) · **Last updated:** 2026-05-16 · **Version:** v0.1 (draft) · [↑ Back to top](#contents)
