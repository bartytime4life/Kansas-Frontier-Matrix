<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/hydrology/glossary
title: Hydrology — Ubiquitous Language Glossary
type: standard
version: v1
status: draft
owners: <hydrology lane steward> + <docs steward>   # placeholders — resolve via CODEOWNERS / ownership register
created: 2026-06-06
updated: 2026-06-06
policy_label: public
contract_version: "3.0.0"   # pinned per ai-build-operating-contract.md v3.0
related:
  - ai-build-operating-contract.md
  - directory-rules.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hydrology/EXPANSION_BACKLOG.md
  - docs/domains/hydrology/EXPANSION_PLAN.md
  - docs/domains/hydrology/FILE_SYSTEM_PLAN.md
  - docs/domains/hydrology/OBJECT_FAMILIES.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/standards/PROV.md
tags: [kfm, domain, hydrology, glossary, ubiquitous-language, governance]
notes:
  - Domain-term meanings are CONFIRMED doctrine per Atlas [DOM-HYD] §C (ubiquitous language); field realizations are PROPOSED.
  - Satisfies backlog item HYD-M12 (hydrology ubiquitous-language glossary).
  - No mounted repo this session; all path/field claims are PROPOSED or NEEDS VERIFICATION.
[/KFM_META_BLOCK_V2] -->

# 💧 Hydrology — Ubiquitous Language Glossary

> The shared vocabulary of the hydrology lane: every object family, governance object, source-role term, and temporal field a contributor or reviewer must use with one, stable meaning — so that the same word never quietly means two different things across `contracts/`, `schemas/`, `policy/`, and the map surface.

![Status](https://img.shields.io/badge/status-draft-yellow)
![CONTRACT_VERSION](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-1f6feb)
![Domain](https://img.shields.io/badge/domain-hydrology-1f9eda)
![Terms](https://img.shields.io/badge/scope-ubiquitous_language-7d3c98)
![Policy](https://img.shields.io/badge/policy_label-public-2ea44f)
![Backlog](https://img.shields.io/badge/backlog-HYD--M12-success)

**Status:** draft · **Owners:** `<hydrology lane steward>` + `<docs steward>` · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Last updated:** 2026-06-06

---

## Quick jump

- [1 · Purpose & how to read this glossary](#1--purpose--how-to-read-this-glossary)
- [2 · Reading the labels](#2--reading-the-labels)
- [3 · Hydrology object families](#3--hydrology-object-families)
- [4 · Source families and source roles](#4--source-families-and-source-roles)
- [5 · Identity, crosswalk, and lineage terms](#5--identity-crosswalk-and-lineage-terms)
- [6 · Temporal vocabulary](#6--temporal-vocabulary)
- [7 · Cross-cutting governance terms](#7--cross-cutting-governance-terms)
- [8 · Collapse-prevention terms (what must stay distinct)](#8--collapse-prevention-terms-what-must-stay-distinct)
- [9 · Cross-lane boundary terms](#9--cross-lane-boundary-terms)
- [10 · Related docs](#10--related-docs)
- [Appendix A · Term → home crosswalk](#appendix-a--term--home-crosswalk)

---

## 1 · Purpose & how to read this glossary

This is the **ubiquitous-language glossary** for the hydrology lane — the bounded-context vocabulary that every hydrology contract, schema, policy bundle, validator, map layer, and Evidence Drawer payload must share. It satisfies backlog item **HYD-M12** and is the authoritative term reference cross-referenced by `OBJECT_FAMILIES.md`, `SOURCE_FAMILIES.md`, and `BOUNDARY.md`.

A glossary in KFM is not decoration: a domain term carries the same meaning across every responsibility root, or the trust membrane leaks. When `contracts/domains/hydrology/nfhl_zone.md` and a map popup disagree about what "flood" means, the disagreement becomes a published claim no one verified.

> [!IMPORTANT]
> Every hydrology term is **constrained by source role, evidence, time, and release state** — this is CONFIRMED doctrine from the Atlas ubiquitous-language table [DOM-HYD §C]. A term names *what kind of evidence a thing is*, not merely *what it is about*. "Flood" is not one concept; it is at least four (see §8).

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 2 · Reading the labels

Each entry carries a truth label so contributors do not promote a planning definition to repo fact.

| Label | Meaning in this glossary |
|---|---|
| **CONFIRMED** | The term and its bounded-context meaning are fixed by attached doctrine (Atlas [DOM-HYD], Directory Rules, Operating Contract). |
| **PROPOSED** | The *field realization* — exact field names, schema shape, identity digest — is design intent, not yet verified against a mounted repo. |
| **NEEDS VERIFICATION** | Checkable against a mounted repo, source endpoint, or external standard, but not yet checked. |
| **CONFLICTED** | Sources disagree; held open until an ADR or drift-register entry resolves it. |

> [!NOTE]
> A common pattern across this glossary: the **term** is CONFIRMED doctrine, while its **field realization** (the JSON Schema, the exact identity digest) is PROPOSED. That split is deliberate — KFM fixes meaning early and implementation later. [DOM-HYD §C] [DOM-HYD §E]

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 3 · Hydrology object families

**CONFIRMED terms / PROPOSED field realization** [DOM-HYD §C, §E] [ENCY]. These are the object families the hydrology lane owns. Each is *"evidence or a released derivative within Hydrology,"* with identity on the PROPOSED deterministic basis **source id + object role + temporal scope + normalized digest**, and with source/observed/valid/retrieval/release/correction times kept distinct where material.

| Term | Working definition | Notes / discipline |
|---|---|---|
| **Watershed** | A drainage area whose surface flow converges to a common outlet. | Accounting geometry; vintage-sensitive. |
| **HUCUnit** | A Watershed Boundary Dataset hydrologic unit (HUC2 … HUC12), identified by its HUC code. | `huc12` MUST be a 12-digit string; lineage carries `wbd_snapshot`. |
| **HydroFeature** | A surface-water network feature — stream, lake, wetland, or reservoir. | Generic feature; distinguish from `ReachIdentity`. |
| **ReachIdentity** | The stable identity of a flowline reach (NHDPlus permanent identifier, reachcode, version). | Ambiguous reach identity → `ABSTAIN`, never a guess. Carries `nhdplus_version`. |
| **GaugeSite** | A monitoring-location identity (e.g., USGS NWIS station) and its metadata. | Identity is the station; observations are separate objects. |
| **FlowObservation** | A time-stamped, in-situ discharge observation. | Carries `parameter_code` (e.g., `00060` discharge), `unit`, `qualifier`, `no_data`. **Observed**, not modeled. |
| **WaterLevelObservation** | A time-stamped gauge-height / stage observation. | Provisional vs final state preserved. **Observed**. |
| **WaterQualityObservation** | A parameter/value/unit/qualifier water-quality observation. | Parameter discipline required; sensitive joins fail closed. |
| **GroundwaterWell** | A well identity with screened-interval context and level observations. | Review-required class — private-property implications. |
| **AquiferObservation** | A groundwater-level or aquifer-state observation. | Cross-lane with Geology (hydrogeology); hydrology does not own aquifer geometry. |
| **NFHLZone** | A FEMA National Flood Hazard Layer regulatory flood-hazard area. | `source_role: "regulatory"` — **never** an observed-flood claim. Carries `EFFECTIVE_DATE`, `VERSION_ID`, `DFIRM_ID`. |
| **FloodContext** | Regulatory or contextual flood framing for a location. | Context, not event truth; not emergency authority. |
| **ObservedFloodEvent** | Historical or sourced inundation evidence backed by an admissible observed source. | **Observed**; never NFHL-derived (see §8). |
| **Hydrograph** | A derived projection of discharge or stage over time. | **Modeled** — carries model identity, run receipt, and bounds; never relabeled observed. |
| **UpstreamTrace** | A derived network-traversal projection (upstream/downstream reach set). | Derived from admitted network identity; not a new observation. |
| **WaterUseLink** | A link relating hydrology to water-use/withdrawal context. | Cross-lane with Agriculture; hydrology does not own use/yield claims. |
| **DroughtLink** | A link relating hydrology to drought context. | Cross-lane with Atmosphere / Hazards. |
| **IrrigationLink** | A link relating hydrology to irrigation context. | Cross-lane with Agriculture. |

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 4 · Source families and source roles

**CONFIRMED** [DOM-HYD §D] [Atlas §24.1]. A source's **role** is a first-class identity attribute, one of the canonical seven classes, **fixed at admission and never upgraded by promotion**. A single family can be admitted in more than one role at different times, but the role travels with each admitted descriptor.

| Term | Definition |
|---|---|
| **observed** | A direct reading or first-hand evidentiary record tied to a place and time (e.g., a gauge discharge reading). |
| **regulatory** | An authoritative determination by a governing body with legal/administrative force (e.g., an NFHL flood-zone designation). |
| **modeled** | A derived product from inputs, assumptions, or fitted parameters; uncertainty and input provenance must be preserved (e.g., a reconstructed hydrograph). |
| **aggregate** | A published summary/total/average over a unit (county, watershed, year); individual-record fidelity is irreversibly lost. |
| **administrative** | A compiled record produced for administration/registration — not necessarily an observation or a regulation. |
| **candidate** | A proposed record awaiting validation, evidence resolution, dedup, or steward review; must not appear on a PUBLISHED surface without promotion. |
| **synthetic** | Content generated by simulation, reconstruction, AI, or interpolation with no underlying first-hand observation; carries a Reality Boundary Note; never presented as observed reality. |

**Hydrology source families** (role assigned per admitted descriptor):

| Source family | Typical role(s) | Discipline |
|---|---|---|
| **USGS WBD / HUC12** | authority / context | Watershed boundary framework; vintage-tracked. |
| **NHDPlus HR / 3DHP-oriented hydrography** | authority / context | Flow network, catchments, VAAs; preserve permanent IDs; `nhdplus_version` carried. |
| **USGS Water Data / NWIS** | observed | Real-time and historical streamflow / gauge height. |
| **FEMA NFHL / MSC** | regulatory (context only) | Effective flood-hazard data; **never** observed inundation or forecast. |
| **3DEP terrain** | observed / context | DEM products supporting hydrologic derivatives. |
| **Water-quality / groundwater sources** | observed / context | Sensitive joins fail closed. |
| **Historical observed-flood evidence** | observed (archival) | Distinct from regulatory NFHL; never collapsed. |

> [!NOTE]
> Rights and current terms for every hydrology source family are **NEEDS VERIFICATION**, and sensitive joins fail closed. [DOM-HYD §D]

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 5 · Identity, crosswalk, and lineage terms

**CONFIRMED doctrine / PROPOSED field realization** [DOM-HYD §E] [Atlas KFM-P5-PROG-0008].

| Term | Definition |
|---|---|
| **Identity rule** | The deterministic basis for an object's identity: **source id + object role + temporal scope + normalized digest** (PROPOSED). |
| **COMID** | The NHDPlus persistent common identifier for a flowline/catchment. |
| **HUC12** | A 12-digit Watershed Boundary Dataset hydrologic-unit code. |
| **COMID ↔ HUC12 crosswalk** | The deterministic per-release mapping from COMID to HUC12, computed with a fixed fallback order, alignment scoring, geometry sanity flags, version-drift handling, and a DSSE-signed manifest. |
| **Fallback order** | Official USGS crosswalk → area-weighted polygon overlay → centroid-in-polygon (heuristic, recorded) → snap-to-pour-point (PRNG seed for ties). |
| **`alignment_score`** | The area-overlap fraction used for a crosswalk decision. The pass/fail **threshold is PROPOSED, not settled doctrine** — the crosswalk card notes it "may need tuning"; low scores without a braid flag are common in real data. |
| **`decision_reason`** | The recorded reason a crosswalk row resolved (`official_crosswalk` \| `area_weighted_overlay` \| `centroid_in_polygon` \| `snap_to_pour_point`). |
| **`geometry_sanity_flags`** | Recorded geometry health flags (self-intersection, tiny area, invalid ring, …). |
| **`nhdplus_version` / `wbd_snapshot`** | Lineage fields preventing silent version drift. NHDPlus v2.1, HR, and WBD snapshots must never be silently mixed. |
| **`multi_huc_candidate`** | Flag for coastal/braided systems that resolve to ranked `candidate_huc12s` rather than one HUC. |
| **`coverage_scope`** | The crosswalk's supported extent (e.g., `"CONUS"`); whether this is a hard gate is an open policy question. |

> [!CAUTION]
> **CONFLICTED — crosswalk validator home (ADR-S-CWV-01).** The corpus places the crosswalk tooling at `tools/probes/comid_huc12/`, `tools/validators/validators/crosswalk/`, **and** `tools/validators/hydro/` in different sources. Do not assert one; track in `DRIFT_REGISTER.md`. **3DHP supersession** of the v2.1 crosswalk key (COMID → 3DHP `universal_reference_id` → HUC12?) is unresolved in the corpus.

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 6 · Temporal vocabulary

**CONFIRMED doctrine** [DOM-HYD §E]. Hydrology keeps these times **distinct wherever they materially differ** — collapsing them is a correctness failure (e.g., reporting a retrieval time as an observed time).

| Term | Definition |
|---|---|
| **Source time** | The time the source assigns to the record at origin. |
| **Observed time** | When the phenomenon was actually measured/observed. |
| **Valid time** | The interval over which the claim holds. |
| **Retrieval time** | When KFM fetched the source payload. |
| **Release time** | When the artifact was published through a governed surface. |
| **Correction time** | When a published claim was corrected. |
| **Provisional vs final** | USGS observation status — provisional readings may be revised; final readings are settled. Status is preserved, never flattened. |

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 7 · Cross-cutting governance terms

**CONFIRMED doctrine** [ENCY] [DIRRULES] [AIBOC]. These terms are not hydrology-specific but are used constantly in the lane; their meaning is fixed system-wide and reproduced here for convenience (the canonical definitions live in the doctrine docs).

| Term | Definition | Canonical home |
|---|---|---|
| **Lifecycle invariant** | `Pre-RAW → RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. | `directory-rules.md` |
| **Pre-RAW** | The watcher-signal/admission edge before RAW; watchers emit signals here without admitting. | `directory-rules.md` |
| **Promotion** | A governed state transition between lifecycle phases — **never a file move**. Emits `ALLOW` / `DENY` / `HOLD` / `ERROR`. | `directory-rules.md` |
| **Trust membrane** | The boundary preventing raw/unreviewed/generated/internal state from becoming public truth; operational form is `apps/governed-api/`. | `trust-membrane.md` |
| **SourceDescriptor** | The admission record carrying source identity, **role**, rights, sensitivity, cadence, citation, time, and content hash. Schema home `schemas/contracts/v1/source/source-descriptor.json` (ADR-0001; `source/` vs `sources/` CONFLICTED); instances live in `data/registry/sources/hydrology/`. | `schemas/contracts/v1/source/` |
| **EvidenceRef → EvidenceBundle** | A reference (`EvidenceRef`) that must resolve to a closed support package (`EvidenceBundle`) before a public claim has authority. An unresolved ref is an `ABSTAIN` condition. | `ENCY` |
| **RunReceipt** | Process memory — inputs, outputs, hashes, commit, image, signature. Proves a step ran; does not make a claim true. | `data/receipts/` |
| **EventEnvelope / EventRunReceipt** | Pre-RAW watcher-signal objects; admission is a separate governed transition. | `data/pre_raw/`, `data/receipts/ingest/` |
| **ValidationReport** | Validator output tied to deterministic fixtures; emits `PASS` / `FAIL` / `ERROR`. | `data/proofs/` |
| **PolicyDecision** | The allow/deny/restrict/abstain decision for an exposure. | `policy/` |
| **ReleaseManifest** | The release-decision artifact listing artifact digests, release decision, and rollback target. | `release/manifests/` |
| **RollbackCard** | A rollback target plus a drilled rollback procedure. | `release/rollback_cards/` |
| **CorrectionNotice** | A public notice of a corrected claim; lists invalidated derivatives. | `release/correction_notices/` |
| **RedactionReceipt** | A record of a public-safe field/geometry transformation. | `data/proofs/` |
| **GENERATED_RECEIPT** | The per-artifact provenance record for AI-authored work; pins `CONTRACT_VERSION = "3.0.0"`. | `schemas/contracts/v1/receipts/` |
| **Finite outcomes** | The fixed result sets: promotion `ALLOW/DENY/HOLD/ERROR`; validator `PASS/FAIL/ERROR`; governed-API/AI `ANSWER/ABSTAIN/DENY/ERROR`. | `Atlas §24.3` |
| **Watcher-as-non-publisher** | A watcher observes and emits Pre-RAW signals, receipts, and candidates only; it never publishes. | `directory-rules.md` |

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 8 · Collapse-prevention terms (what must stay distinct)

**CONFIRMED doctrine** [DOM-HYD §B] [Atlas §24.1.2]. The single most consistent hydrology failure mode is collapsing distinct truth classes into one word. These pairs MUST stay distinct; collapsing them fails closed.

> [!WARNING]
> "Flood" is not one concept. Treat each of the following as a separate, labeled thing.

| Keep distinct | … from | Why |
|---|---|---|
| **NFHLZone** (regulatory context) | **ObservedFloodEvent** (observed) | NFHL is legally-effective hazard data, not real-time inundation. Collapsing → `DENY`. |
| **ObservedFloodEvent** (observed) | **Hydrograph / forecast** (modeled) | A model output is not an observation. Collapsing → `DENY` at publication, `ABSTAIN` at AI. |
| **FloodContext** (context) | **Emergency warning** (life-safety authority) | KFM is not an alert authority; warnings belong to Hazards / official sources. |
| **FlowObservation** (observed) | **Hydrograph** (modeled projection) | The derived curve is not the underlying reading. |
| **HUCUnit** (one WBD snapshot) | **HUCUnit** (a different snapshot) | Silent version/vintage mixing is a quarantine-class failure. |

> [!CAUTION]
> KFM is **not** an emergency-alert authority. Any hydrology surface drifting toward "current inundation," "active warning," or "evacuation guidance" is out of policy and must redirect life-safety action to official sources (NWS, state/county emergency management). [ENCY §20.4] [DOM-HAZ]

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 9 · Cross-lane boundary terms

**CONFIRMED / PROPOSED** [DOM-HYD §F]. These terms name the *seam* between hydrology and an adjacent lane. A cross-lane relation preserves ownership, source role, sensitivity, and `EvidenceBundle` support — it never transfers authority.

| Term | Adjacent lane | Hydrology does **not** own |
|---|---|---|
| **Hydrologic Soil Group (HSG)** | Soil | SSURGO components, pedons, horizons. |
| **Soil moisture** | Soil | Canonical soil-moisture claims. |
| **Irrigation / water-use context** | Agriculture | Crop or yield claims. |
| **Floodplain exposure context** | Settlements / Infrastructure | Critical-asset identity or precise exposure detail. |
| **Hydrogeology / aquifer geometry** | Geology | Lithology, boreholes, stratigraphy. |
| **Precipitation / drought drivers** | Atmosphere / Air | Observed/modeled atmospheric truth. |
| **Flood / drought / declaration** | Hazards | Hazard-event truth; life-safety authority. |

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## 10 · Related docs

- [`directory-rules.md`](../../../directory-rules.md) — placement law, lifecycle invariant.
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating contract; `CONTRACT_VERSION = "3.0.0"`.
- [`docs/domains/hydrology/README.md`](./README.md) — domain landing page.
- [`docs/domains/hydrology/DATA_LIFECYCLE.md`](./DATA_LIFECYCLE.md) — lane governance and gates.
- [`docs/domains/hydrology/OBJECT_FAMILIES.md`](./OBJECT_FAMILIES.md) — object-family detail (this glossary's companion).
- [`docs/domains/hydrology/FILE_SYSTEM_PLAN.md`](./FILE_SYSTEM_PLAN.md) — lane file homes.
- [`docs/domains/hydrology/EXPANSION_BACKLOG.md`](./EXPANSION_BACKLOG.md) — backlog (this doc = HYD-M12).
- [`docs/domains/hydrology/EXPANSION_PLAN.md`](./EXPANSION_PLAN.md) — phased roadmap.
- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../sources/SOURCE_DESCRIPTOR_STANDARD.md) — `SourceDescriptor` meaning.
- [`docs/standards/PROV.md`](../../standards/PROV.md) — provenance profile.

<!-- TODO: re-check link paths against the mounted repo; create BOUNDARY.md / SOURCE_FAMILIES.md cross-links once authored. -->

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

## Appendix A · Term → home crosswalk

**PROPOSED** [DIRRULES §12]. Where each object-family term's meaning, shape, and instances live. File presence is NEEDS VERIFICATION pending mounted-repo inspection.

<details>
<summary>Show the term → home crosswalk</summary>

| Term | Meaning (`contracts/`) | Shape (`schemas/contracts/v1/`) | Instances (`data/`) |
|---|---|---|---|
| Watershed | `contracts/domains/hydrology/watershed.md` | `.../domains/hydrology/watershed.schema.json` | `data/processed/hydrology/...` |
| HUCUnit | `.../huc_unit.md` | `.../huc_unit.schema.json` | `data/processed/hydrology/...` |
| HydroFeature | `.../hydro_feature.md` | `.../hydro_feature.schema.json` | `data/processed/hydrology/...` |
| ReachIdentity | `.../reach_identity.md` | `.../reach_identity.schema.json` | `data/processed/hydrology/...` |
| GaugeSite | `.../gauge_site.md` | `.../gauge_site.schema.json` | `data/processed/hydrology/...` |
| FlowObservation | `.../flow_observation.md` | `.../flow_observation.schema.json` | `data/processed/hydrology/...` |
| WaterLevelObservation | `.../water_level_observation.md` | `.../water_level_observation.schema.json` | `data/processed/hydrology/...` |
| WaterQualityObservation | `.../water_quality_observation.md` | `.../water_quality_observation.schema.json` | `data/processed/hydrology/...` |
| GroundwaterWell | `.../groundwater_well.md` | `.../groundwater_well.schema.json` | `data/processed/hydrology/...` |
| NFHLZone | `.../nfhl_zone.md` | `.../nfhl_zone.schema.json` | `data/processed/hydrology/...` |
| ObservedFloodEvent | `.../observed_flood_event.md` | `.../observed_flood_event.schema.json` | `data/processed/hydrology/...` |
| Hydrograph | `.../hydrograph.md` | `.../hydrograph.schema.json` | `data/processed/hydrology/...` |
| UpstreamTrace | `.../upstream_trace.md` | `.../upstream_trace.schema.json` | `data/processed/hydrology/...` |
| COMID↔HUC12 crosswalk | `.../comid_huc12_crosswalk.md` | `.../comid_huc12_crosswalk.schema.json` *(or `schemas/contracts/v1/crosswalks/` — OPEN)* | `data/processed/hydrology/...` |
| SourceDescriptor *(shared)* | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | `schemas/contracts/v1/source/source-descriptor.json` *(`source/` vs `sources/` CONFLICTED)* | `data/registry/sources/hydrology/` |

</details>

[Back to top](#-hydrology--ubiquitous-language-glossary)

---

**Last updated:** 2026-06-06 · **Status:** draft · **Lane:** hydrology · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Backlog:** HYD-M12

[⬆ Back to top](#-hydrology--ubiquitous-language-glossary)
