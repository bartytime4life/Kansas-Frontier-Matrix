<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/cross-domain-invasives
title: Cross-Domain Invasives — Architectural Treatment
type: standard
version: v1
status: draft
owners: <TBD: docs steward + fauna-domain steward + flora-domain steward + governance lead>
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related: [
  docs/architecture/TRUST_MEMBRANE.md,
  docs/architecture/critical-asset-exposure.md,
  docs/architecture/system-context.md,
  docs/architecture/governed-api.md,
  docs/architecture/map-shell.md,
  docs/architecture/ui/CONTINUITY_NOTES.md,
  docs/standards/MAP_TRUST_STATES.md,
  docs/standards/EVIDENCE_BUNDLE.md,
  docs/standards/RELEASE_MANIFEST.md,
  docs/standards/PROV/README.md,
  docs/standards/DUO_PROFILE.md,
  docs/standards/SENSITIVITY_RUBRIC.md,
  contracts/v1/fauna/,
  contracts/v1/flora/,
  schemas/contracts/v1/fauna/,
  schemas/contracts/v1/flora/,
  policy/sensitivity/fauna/,
  policy/sensitivity/flora/,
  policy/invasives/
]
tags: [kfm, architecture, invasives, fauna, flora, habitat, agriculture, hydrology, hazards, archaeology, cross-domain, source-role-anti-collapse, sensitivity]
notes: [
  "Architectural treatment of how KFM handles invasive species across the Fauna, Flora, Habitat, Agriculture, Hydrology, Hazards, and Archaeology domains.",
  "Fauna owns `Invasive Species Record`; Flora owns `InvasivePlantRecord` — both CONFIRMED per Atlas §7.B and §8.B. This document does not claim a third InvasiveRecord home; it proposes the cross-domain integration architecture between the two.",
  "Critical doctrine line preserved verbatim: 'Invasive-plant context informs management framing; never an instruction' (Flora × Agriculture, Atlas §24.4.6) — see §10."
]
[/KFM_META_BLOCK_V2] -->

# Cross-Domain Invasives — Architectural Treatment

> The architecture of how KFM handles **invasive species** as a concept that lives across the **Fauna**, **Flora**, **Habitat**, **Agriculture**, **Hydrology**, **Hazards**, and **Archaeology** domains simultaneously — and how the membrane keeps each domain's authority intact when those concerns overlap.

[![status: draft](https://img.shields.io/badge/status-draft-orange)](#)
[![type: architecture explainer](https://img.shields.io/badge/type-architecture--explainer-informational)](#)
[![scope: cross-domain integration](https://img.shields.io/badge/scope-cross--domain%20integration-blueviolet)](#)
[![framing rule: management framing not instruction](https://img.shields.io/badge/framing%20rule-management%20framing%20not%20instruction-critical)](#)
[![source-role: anti-collapse](https://img.shields.io/badge/source--role-anti--collapse-yellowgreen)](#)
[![sensitivity: per-class](https://img.shields.io/badge/sensitivity-per--class-9cf)](#)
[![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)](#)

| Status | Owners | Last reviewed |
|---|---|---|
| **draft** | _TBD — docs steward + fauna-domain steward + flora-domain steward + governance lead_ | 2026-05-24 |

---

> [!CAUTION]
> **This document is an architectural treatment, not the doctrine for either Fauna or Flora.** Fauna's `Invasive Species Record` and Flora's `InvasivePlantRecord` are domain-owned object families with meaning fixed in their respective domain contracts. This document does **not** redefine them, does **not** propose a third unified `InvasiveRecord` home, and does **not** override per-domain sensitivity rules. It proposes the **architecture of integration** between them — the cross-lane joins, the source-role discipline, and the cross-cutting framing rule. See §2.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Scope and repo fit](#2-scope-and-repo-fit)
- [3. Authority and standing](#3-authority-and-standing)
- [4. What KFM calls an invasive](#4-what-kfm-calls-an-invasive)
- [5. The invasives architecture overview](#5-the-invasives-architecture-overview)
- [6. Domain ownership — Fauna and Flora](#6-domain-ownership--fauna-and-flora)
- [7. Cross-lane joins — the eight cross-cutting paths](#7-cross-lane-joins--the-eight-cross-cutting-paths)
- [8. Source-role anti-collapse for invasives](#8-source-role-anti-collapse-for-invasives)
- [9. Sensitivity and exposure architecture](#9-sensitivity-and-exposure-architecture)
- [10. Management framing vs instruction — the line KFM does not cross](#10-management-framing-vs-instruction--the-line-kfm-does-not-cross)
- [11. Cross-lane joins as governed projections](#11-cross-lane-joins-as-governed-projections)
- [12. Public products](#12-public-products)
- [13. Anti-patterns](#13-anti-patterns)
- [14. Tensions and known limits](#14-tensions-and-known-limits)
- [15. Open questions](#15-open-questions)
- [16. Related docs](#16-related-docs)
- [Appendix A — Cross-lane invasive scenarios matrix](#appendix-a--cross-lane-invasive-scenarios-matrix)
- [Appendix B — Source-role anti-collapse worked example](#appendix-b--source-role-anti-collapse-worked-example)

---

## 1. Purpose

CONFIRMED doctrine — Atlas §7.A (Fauna):

> *"Govern animal taxonomic identity, conservation/legal status, occurrence evidence, monitoring, range, seasonal support, sensitive sites, mortality, disease, **invasive species**, geoprivacy, public-safe products, and bounded APIs."*

CONFIRMED doctrine — `KFM_Unified_Implementation_Architecture_Build_Manual.md` §10.6 (Flora):

> *"Coverage: taxonomic identity, plant occurrences/specimens, rare plants, vegetation communities, **invasive plants**, phenology, remote-sensing vegetation indices."*

CONFIRMED doctrine — Atlas §24.4.6 (Flora cross-lane to Agriculture):

> *"Invasive-plant context informs management framing; **never an instruction**."*

These three lines describe an architectural reality the corpus names but does not consolidate: invasives are simultaneously a **Fauna concern** (animal invasives), a **Flora concern** (plant invasives), and a **cross-lane joining concept** that touches Habitat, Agriculture, Hydrology, Hazards, and Archaeology. The same architectural rules that hold for any other cross-lane interaction in KFM — most-restrictive tier wins, source-role never collapses, governed joins emit their own receipts — hold here. But invasives also carry a doctrine-level framing rule that is **stricter than the cross-lane default**: KFM may describe an invasive's context to inform management; KFM **may not** instruct management.

This document documents the existing domain-by-domain doctrine (CONFIRMED), proposes the cross-domain integration architecture (PROPOSED), and names the failure modes the architecture exists to prevent.

> [!NOTE]
> Invasives are an example of a class of KFM concept that is **structurally cross-domain** by nature — meaning the wrong response is to invent a "Invasives domain" that competes with Fauna and Flora. The architectural answer is integration discipline, not domain proliferation.

[Back to top](#quick-jump)

---

## 2. Scope and repo fit

### 2.1 What this document is

| Aspect | Value | Label |
|---|---|---|
| Document class | KFM architecture explainer (cross-domain integration) | CONFIRMED per Directory Rules §6.1 (`docs/architecture/`) |
| Proposed path | `docs/architecture/cross-domain-invasives.md` | PROPOSED; casing matches sibling architecture-folder convention |
| Sibling architecture docs | `system-context.md`, `governed-api.md`, `map-shell.md`, `maplibre-3d.md`, `contract-schema-policy-split.md`, `TRUST_MEMBRANE.md`, `critical-asset-exposure.md`, `ui/CONTINUITY_NOTES.md` | CONFIRMED per Directory Rules §6.1 (mounted-repo presence NEEDS VERIFICATION) |
| Primary doctrine anchors | Atlas §7 (Fauna), §8 (Flora), §24.4.5 (edges owned by Fauna), §24.4.6 (edges owned by Flora), §24.4.7 (edges owned by Agriculture); `kfm_unified_doctrine_synthesis.md` §16 (per-domain sensitivity matrix), §17 (cross-lane joins); UIABM §10.5–§10.6 | CONFIRMED |
| Authority NOT held | Per-domain contract Markdown; per-domain schemas; per-domain policy code; observation-level records | CONFIRMED |

### 2.2 What this document is NOT

| If the content is about… | …it lives at | …not here |
|---|---|---|
| The `Invasive Species Record` object meaning (Fauna) | `contracts/v1/fauna/invasive_species_record.md` (PROPOSED home) | this doc |
| The `InvasivePlantRecord` object meaning (Flora) | `contracts/v1/flora/invasive_plant_record.md` (PROPOSED home) | this doc |
| Their JSON Schemas | `schemas/contracts/v1/fauna/`, `schemas/contracts/v1/flora/` (PROPOSED homes) | this doc |
| OPA rules that gate invasive-occurrence exposure per domain | `policy/sensitivity/fauna/`, `policy/sensitivity/flora/` (PROPOSED homes per Atlas crosswalk) | this doc |
| Cross-domain join rules for invasives (the OPA code) | `policy/invasives/` (PROPOSED home, parallels `policy/sensitivity/`) | this doc |
| The taxonomic-identity rules | per-domain contracts | this doc |
| Source admission for invasives data sources (GBIF, eBird, EDDMapS, USDA APHIS, KBS) | `data/source/` + `contracts/v1/source/` | this doc |
| Per-species lists (which species are designated invasive in which jurisdiction) | per-domain registries; **not doctrine** | this doc |
| Render-time invasive layer styling | `packages/maplibre-runtime/` | this doc |
| Tests and fixtures | `tests/invasives/`, `fixtures/invasives/` | this doc |
| Per-domain runbooks | `docs/runbooks/fauna/`, `docs/runbooks/flora/` | this doc |

What this document **does** own:

- The architectural definition of what KFM treats as an invasive (§4).
- The cross-domain architecture overview (§5).
- The domain-ownership map (§6).
- The cross-lane join register (§7, §11).
- The source-role anti-collapse rule for invasives (§8).
- The sensitivity-and-exposure architecture for invasives (§9).
- The management-framing-not-instruction rule (§10).
- The public-products inventory (§12).
- The anti-pattern register (§13).

[Back to top](#quick-jump)

---

## 3. Authority and standing

| Aspect | Value | Label |
|---|---|---|
| Document class | KFM cross-domain integration architecture | CONFIRMED per Directory Rules §6.1 |
| Canonical path | `docs/architecture/cross-domain-invasives.md` | PROPOSED |
| Fauna ownership anchor | **Atlas §7.A, §7.B** — Fauna domain owns `Invasive Species Record`; explicitly names "invasive species" in one-line purpose | CONFIRMED |
| Flora ownership anchor | **Atlas §8.B** — Flora domain owns `InvasivePlantRecord` | CONFIRMED |
| Cross-lane Fauna × Flora | **Atlas §7.F** — "ecological community, pollinator, **invasive**, food-web context" | CONFIRMED |
| Cross-lane Flora × Agriculture | **Atlas §24.4.6** — *"Invasive-plant context informs management framing; never an instruction."* | CONFIRMED |
| Cross-lane Fauna × Agriculture | **Atlas §24.4.5** — *"Pest stress indicators are agriculture-owned; fauna is the source of taxonomic identity only."* | CONFIRMED |
| Public product anchor | **Atlas §7.G** — Fauna viewing products include "invasive monitoring public layer" | CONFIRMED |
| UIABM coverage anchors | **UIABM §10.5** (Fauna invasive species); **§10.6** (Flora invasive plants) | CONFIRMED |
| Source-role doctrine | **`kfm_unified_doctrine_synthesis.md` §17** — source-role anti-collapse rule | CONFIRMED |
| Cross-domain policy home | `policy/invasives/` | **PROPOSED** — parallels `policy/sensitivity/`; ADR or Directory Rules update NEEDED |
| Authority NOT held | Per-domain object meaning, machine shape, admissibility code, per-species jurisdictional lists | CONFIRMED |

[Back to top](#quick-jump)

---

## 4. What KFM calls an invasive

The corpus uses *"invasive"* as a property of a record, not as a separate object family that competes with `Taxon`, `Occurrence`, `RangePolygon`, etc. An invasive in KFM is **a designated taxon plus its occurrence context**, where the designation is a property of the taxon (per-jurisdiction, per-time) and the occurrence is governed by the same evidence/policy/release rules as any other occurrence.

CONFIRMED corpus families:

| Object family | Owning domain | What it records |
|---|---|---|
| `Invasive Species Record` (Fauna) | Atlas §7.B | An animal taxon's invasive-species designation + occurrence/management context |
| `InvasivePlantRecord` (Flora) | Atlas §8.B | A plant taxon's invasive designation + occurrence/management context |
| `Pest stress indicator` (Agriculture-owned per Fauna×Agriculture edge) | Atlas §24.4.5 | Pest impact on agricultural systems — Agriculture authority, with Fauna as taxonomic source only |

### 4.1 What an invasive **is not** (architecturally)

- Not a separate "Invasives" domain. KFM does not have one; this document does not propose one.
- Not a property that overrides per-domain sensitivity defaults. A rare-but-invasive plant carries Flora's rare-plant sensitivity rule; an invasive aquatic species at a sensitive spawning ground carries Fauna's `SensitiveSite` rule.
- Not an alert authority. KFM observes and reports invasive context; the doctrinal *"KFM is never an alert authority"* rule (`kfm_unified_doctrine_synthesis.md` §16) applies fully.
- Not management instruction. The doctrine line is explicit: invasive-plant context **informs management framing; never an instruction** (Atlas §24.4.6).

### 4.2 The taxonomic-identity discipline

CONFIRMED — Atlas §24.4.5 (Fauna × Agriculture):

> *"Pest stress indicators are agriculture-owned; fauna is the source of taxonomic identity only."*

This is the architectural answer to a recurring naming question: when an invasive species is observed damaging a crop, is the record a `Fauna.InvasiveSpeciesRecord` or an `Agriculture.PestStressIndicator`? The corpus answers cleanly: **the species identity is Fauna; the crop impact is Agriculture**; the join produces a derivative that cites both. Neither owns the other's authority.

[Back to top](#quick-jump)

---

## 5. The invasives architecture overview

PROPOSED — synthesizing Atlas §7.B + §8.B + §24.4.5 + §24.4.6 + the §16 sensitivity matrix + the §17 cross-lane rule.

```mermaid
flowchart TB
  subgraph Sources["Sources (T0/T1/T4 per source class)"]
    GBIF[GBIF / iNaturalist<br/>citizen science]
    EDDM[EDDMapS<br/>volunteer reports]
    APHIS[USDA APHIS<br/>regulatory surveys]
    KSU[KBS / KSU<br/>academic surveys]
    NRCS[NRCS / KDA<br/>management records]
    MODEL[Modeled spread<br/>e.g., MaxEnt]
  end

  subgraph Fauna["Fauna domain"]
    F_TAX[Taxon + Crosswalk]
    F_ISR[Invasive Species Record]
    F_OCC[Occurrence Restricted / Public]
    F_DIS[DiseaseObservation]
  end

  subgraph Flora["Flora domain"]
    FL_TAX[Plant Taxon + Crosswalk]
    FL_IPR[InvasivePlantRecord]
    FL_OCC[Flora Occurrence]
    FL_VC[Vegetation Community]
  end

  subgraph CrossLane["Cross-lane projections (governed joins)"]
    HAB[Habitat impact projection]
    AG[Agriculture pest projection]
    HYD[Aquatic invasive projection]
    HAZ[Hazard-class projection]
    ARCH[Archaeology context]
  end

  subgraph Public["Public products"]
    PUB_F[Invasive monitoring public layer<br/>(Fauna §7.G)]
    PUB_FL[Invasive-plant public layer]
    PUB_J[Cross-lane management-framing view]
  end

  GBIF --> F_TAX
  GBIF --> FL_TAX
  EDDM --> F_ISR
  EDDM --> FL_IPR
  APHIS --> F_ISR
  APHIS --> FL_IPR
  KSU --> F_OCC
  KSU --> FL_OCC
  NRCS --> F_ISR
  NRCS --> FL_IPR
  MODEL -. "treat as modeled<br/>source role" .-> F_ISR
  MODEL -. "treat as modeled<br/>source role" .-> FL_IPR

  F_ISR --> HAB
  FL_IPR --> HAB
  F_ISR --> AG
  FL_IPR --> AG
  F_ISR --> HYD
  F_DIS --> HAZ
  FL_IPR --> ARCH

  HAB --> PUB_J
  AG --> PUB_J
  HYD --> PUB_J
  HAZ --> PUB_J
  ARCH --> PUB_J
  F_ISR --> PUB_F
  FL_IPR --> PUB_FL

  style F_ISR fill:#d9eaff,stroke:#2c5282
  style FL_IPR fill:#d9eaff,stroke:#2c5282
  style CrossLane fill:#fff4cc,stroke:#b58900
  style MODEL fill:#ffe4e1,stroke:#a04545
```

PROPOSED — diagram composes the Atlas Fauna/Flora object families with the cross-lane edges from Atlas §24.4.4 through §24.4.7. Tooling and route names NEEDS VERIFICATION.

### 5.1 What the diagram is and isn't

The diagram is **a composition map**, not a data-flow specification. It shows:

- **Fauna owns the animal-invasive line** end-to-end (`Taxon` → `Invasive Species Record` → public products).
- **Flora owns the plant-invasive line** end-to-end.
- **Sources contribute to one or both domains** depending on the source's authority.
- **Modeled spread (e.g., MaxEnt distribution predictions) is a distinct source role** — never collapses with observed occurrences (§8).
- **Cross-lane projections are derivative artifacts** with their own evidence bundles; they are not free composition of the upstream records.
- **Public products are downstream of cross-lane projections, not of raw records.**

[Back to top](#quick-jump)

---

## 6. Domain ownership — Fauna and Flora

CONFIRMED — Atlas §7.B and §8.B.

| Domain | Owns | Explicitly does NOT own |
|---|---|---|
| **Fauna** | `Taxon`, `Taxon Crosswalk`, `Conservation Status`, `Occurrence Evidence`, `Occurrence Restricted`, `Occurrence Public`, `RangePolygon`, `SeasonalRange`, `MigrationRoute`, `SensitiveSite`, `MortalityObservation`, `DiseaseObservation`, **`Invasive Species Record`**, `Redaction Receipt` | Habitat patches (Habitat); plant records (Flora); context-only from Hydrology/Soil/Agriculture/Roads/People |
| **Flora** | `Plant Taxon`, `FloraTaxon Crosswalk`, `Flora Occurrence`, `SpecimenRecord`, `Rare Plant Record`, `Vegetation Community`, **`InvasivePlantRecord`**, `Phenology Observation`, `RangePolygon`, `Habitat Association`, `Botanical Survey`, `Restoration Planting`, `Redaction Receipt` | Habitat patches (Habitat); animal records (Fauna); other domains' truth |

### 6.1 The clean separation

KFM does **not** have:

- A unified `InvasiveRecord` family.
- An "Invasives" responsibility root.
- A doctrine that elevates invasives above other cross-domain concerns.

KFM **does** have:

- A clear ownership: Fauna owns animal-invasive records; Flora owns plant-invasive records.
- A clear edge: Fauna × Flora explicitly cites "invasive" as a join (Atlas §7.F).
- A clear constraint at each cross-domain edge (§7).

This document does not invent a third home. It documents the architecture between the two existing homes.

[Back to top](#quick-jump)

---

## 7. Cross-lane joins — the eight cross-cutting paths

CONFIRMED — Atlas §24.4.4 through §24.4.7 (edges owned by Habitat, Fauna, Flora, Agriculture); §24.4.x (per-domain cross-lane tables). The corpus enumerates the per-domain edges; this section consolidates those edges that touch invasive context.

| # | Join | Owning side | Relation type (CONFIRMED) | Architectural constraint |
|---|---|---|---|---|
| 1 | **Fauna × Flora** | bidirectional | ecological community, pollinator, **invasive**, food-web context | Preserve ownership, source role, sensitivity, EvidenceBundle (Atlas §7.F) |
| 2 | **Fauna × Habitat** | Habitat consumes Fauna | Occurrence records (public-safe only) feed habitat-quality model evaluation | Restricted occurrences never cross (Atlas §24.4.5) |
| 3 | **Fauna × Agriculture** | Agriculture consumes Fauna | Pest stress indicators are agriculture-owned; fauna is the source of taxonomic identity only | Identity-only flow (Atlas §24.4.5) |
| 4 | **Fauna × Hydrology** | Fauna context | aquatic/riparian/wetland/spawning context | Aquatic-invasive context flows here; preserve EvidenceBundle (Atlas §7.F) |
| 5 | **Fauna × Hazards** | Fauna consumes Hazards | disease, mortality, wildfire, flood, drought exposure | Wildlife disease (some are themselves invasive vectors) as hazard context with rights/stewardship checks (Atlas §24.4.5) |
| 6 | **Flora × Habitat** | Habitat consumes Flora | Vegetation community feeds ecological system mapping | Rare-plant exact location denied to public; invasive plants flow with their own sensitivity (Atlas §24.4.6) |
| 7 | **Flora × Agriculture** | Agriculture consumes Flora | **Invasive-plant context informs management framing; never an instruction** | The instruction-prohibition rule (§10) — Atlas §24.4.6 |
| 8 | **Flora × Archaeology** | Archaeology consumes Flora | Ethnobotanical context (steward-reviewed) may bound site interpretation | Never overrides cultural-heritage authority; some invasives obscure sites (Atlas §24.4.6) |

### 7.1 The aquatic invasive special case

Atlas §7.F lists Fauna × Hydrology context as *"aquatic/riparian/wetland/spawning context."* Aquatic invasives (zebra mussels, Asian carp, hydrilla, etc.) are a recurring real-world category that combines:

- **Fauna or Flora identity** (the invasive species itself).
- **Hydrology authority** (the watershed, reach, waterbody, gauge).
- **Hazards context** (some aquatic invasives are managed under hazard frameworks).

The architectural answer is: the **Hydrology authority owns the waterbody identity**; the **Fauna or Flora authority owns the species identity**; the **join produces a derivative** with cross-references to both. The join is governed by `policy/invasives/aquatic/` (PROPOSED home, not yet authored).

> [!NOTE]
> An aquatic invasive observed at a `SensitiveSite` (e.g., near a fish spawning location) inherits the **most-restrictive** sensitivity — usually `SensitiveSite`'s T4 default — even if the species itself is widely-known invasive. The most-restrictive-tier rule from `MAP_TRUST_STATES.md` §6.2 governs.

[Back to top](#quick-jump)

---

## 8. Source-role anti-collapse for invasives

CONFIRMED — `kfm_unified_doctrine_synthesis.md` §17:

> *"Source-role collapse is the most common silent failure. A modeled value cited as an observation, an aggregate cited as a per-place observation, a synthetic surface presented as reality — these are doctrine violations even when the underlying data are correct."*

Invasives are a category where source-role collapse is especially likely. Multiple very different source types report on the same species in the same area, and the resulting records look superficially similar. They are **not** the same kind of evidence.

### 8.1 The source-role taxonomy for invasives

PROPOSED — extending the §17 source-role doctrine to the invasives case.

| Source role | What it is | Example source class | Authority weight |
|---|---|---|---|
| **Observed (citizen-science)** | A volunteer observation, often with photograph; identification quality varies | GBIF, iNaturalist, eBird, EDDMapS volunteer reports | Lower individually; can aggregate to a meaningful signal |
| **Observed (official survey)** | A planned, methodology-documented survey by a qualified party | USDA APHIS pest detection survey; KDA survey; KSU vegetation transect | Higher; methodology is itself evidence |
| **Modeled (distribution / spread)** | A predicted distribution from a statistical or process model | MaxEnt distribution model; APHIS spread model | Modeled; never an observation |
| **Aggregate** | A summary statistic over a region / time | County-decade invasive-presence summary | Aggregate; never a per-place observation |
| **Regulatory** | A formally-designated jurisdictional list | Kansas noxious-weed list; federal injurious-wildlife list | Designation, not observation |
| **Management record** | A record of a management action taken (treatment, removal, eradication) | NRCS conservation record; KDWP eradication log | Record of action, not record of presence |

### 8.2 The anti-collapse rule

Each of the six source roles produces records with **different epistemic weight**. Architectural rules:

1. **A modeled record never cites itself as an observation.** A predicted MaxEnt range polygon is a `ModelRunReceipt`-bearing artifact; it is never indexed as an `Occurrence`.
2. **An aggregate never cites itself as a per-place observation.** A county-decade summary is an `AggregationReceipt`-bearing artifact; it is never displayed as a point on the map at a precise location.
3. **A regulatory designation never substitutes for observation.** Kansas listing *Bromus tectorum* as a noxious weed is a designation; it is not evidence that any given parcel contains *Bromus tectorum*.
4. **A management record never substitutes for occurrence.** A removal log proves treatment occurred; it implies but does not record presence.
5. **A citizen-science observation is an observation** (with its own identification-quality concerns), but is **not** a regulatory designation or an official survey.

### 8.3 Architectural enforcement

PROPOSED. The cross-domain invasives projection MUST:

1. Tag every contributing record with its source role.
2. Refuse joins that would silently collapse roles (e.g., joining a modeled spread polygon with an aggregate to produce a point map).
3. Emit a `PolicyDecision` that records the source-role check, even when ALLOW.
4. In Focus Mode / AI responses, qualify any answer about invasive presence with the source-role of the supporting evidence ("Based on a modeled spread prediction" vs "Based on an APHIS-confirmed survey").

> [!WARNING]
> *"Source-role collapse is the most common silent failure"* applies forcefully here. The pressure to "just say where the invasive is" is real; the architectural answer is to surface the source role at every cross-domain handoff, not to flatten the distinction in the name of usability.

[Back to top](#quick-jump)

---

## 9. Sensitivity and exposure architecture

Invasives have an unusual sensitivity profile: most established invasives are **less sensitive than typical Fauna/Flora occurrences**, while certain invasive-related records are **more sensitive than typical**.

### 9.1 Lower-sensitivity cases (T0/T1 default)

Established, regulated invasives are typically T0–T1 public-safe:

- **Designated noxious weeds** (Kansas noxious-weed list, federal injurious-wildlife list) — designations are public.
- **Common, widespread invasives** (cheatgrass, sericea lespedeza, eastern red cedar, feral hog, European starling) — occurrence at coarse geometry is public.
- **Regulatory-survey results** — APHIS publishes survey results; KFM mirrors them at T0/T1 per source rights.

These cases default to T0/T1 not because invasives have a special rule, but because the **source-class rights and the sensitivity rubric** (`kfm_unified_doctrine_synthesis.md` §15–§16) produce that result.

### 9.2 Higher-sensitivity cases (T2/T4 default)

CONFIRMED — Atlas §24.5.2 sensitivity defaults still apply. Several invasive-related categories carry **higher-than-typical** sensitivity:

| Case | Tier | Why |
|---|---|---|
| Early-detection observation of a high-priority invasive | **T2** or **T4** | Disclosure of an early infestation may impede eradication (analogous to critical-asset vulnerability — `docs/architecture/critical-asset-exposure.md`) |
| Invasive at a sensitive ecological site (`SensitiveSite`, rare-plant location, archaeological site) | **T4** (inherited) | Most-restrictive rule wins; the host site's sensitivity governs |
| Invasive on private land (operator-identifiable) | **T2/T4** | Commercial harm; private person × parcel join restrictions apply (Atlas §24.4.5) |
| Invasive pest causing condition damage to critical infrastructure (e.g., emerald ash borer on critical-route trees) | **T4** | Treated under critical-asset-exposure rules; see `docs/architecture/critical-asset-exposure.md` §9 join risks |
| Invasive disease vector at a wildlife disease observation site | **T4** | DiseaseObservation rules govern; the invasive identity does not reduce the wildlife-disease sensitivity |

### 9.3 The asymmetry

The asymmetry is consequential: an established invasive that everyone knows about may be **less** sensitive than the same species observed for the first time in a county. The latter triggers an early-detection sensitivity rule that the former does not.

> [!IMPORTANT]
> Sensitivity for invasives is **never a property of the species alone**; it is a property of the species, the site, the time, and the public-record state. The architecture defers to per-class policy (`policy/sensitivity/fauna/`, `policy/sensitivity/flora/`) and per-case steward review for the early-detection rule.

[Back to top](#quick-jump)

---

## 10. Management framing vs instruction — the line KFM does not cross

CONFIRMED — Atlas §24.4.6 (Flora × Agriculture):

> *"Invasive-plant context informs management framing; **never an instruction**."*

This is the single most consequential doctrinal line for cross-domain invasives, and the architecture has a clear shape around it.

### 10.1 What "management framing" means

KFM may publish:

- *"The cheatgrass invasive context for rangeland in this region includes the following considerations: …"* — framing.
- *"Cheatgrass is a designated noxious weed in Kansas. The Kansas Department of Agriculture maintains the official designation."* — citation of an external authority.
- *"Observed presence of cheatgrass in this watershed, per APHIS survey [evidence ref]."* — observation with source role.

KFM **may not** publish:

- *"Apply herbicide X at rate Y to control cheatgrass on this parcel."* — instruction.
- *"Begin treatment of feral hogs in this corridor."* — instruction.
- *"This area should be sprayed in March."* — instruction.

### 10.2 Why the line is architectural, not editorial

The instruction-prohibition is not about caution or politeness. It is the same rule that prevents KFM from being a hazard alert authority (`kfm_unified_doctrine_synthesis.md` §16: *"KFM is never an alert authority"*):

| Concern | KFM's role | Authority that may instruct |
|---|---|---|
| Invasive plant management | Frame the context; cite the regulatory designation | KDA, NRCS, USDA APHIS, county weed director |
| Invasive animal management | Frame the context; cite the designation | KDWP, USDA APHIS Wildlife Services |
| Aquatic invasive response | Frame the context; cite the designation | KDWP, USACE, EPA |
| Forest-pest response | Frame the context; cite the designation | Kansas Forest Service, USDA APHIS |
| Wildlife-disease response | Frame the context; cite the designation | KDWP, KDA, USDA APHIS Veterinary Services |

The architectural enforcement is at the trust membrane:

1. **At the API surface** (governed-API audience-class projection): the API does not expose endpoints that return instructions; the response envelope does not contain instruction-class fields.
2. **At the AI runtime** (governed AI runtime): the AI is bound by `kfm_unified_doctrine_synthesis.md` §20 — it summarizes resolved evidence with citations; an answer that would constitute an instruction must ABSTAIN with the reason *"management instruction is outside KFM's scope."*
3. **At the export pipeline**: exports may include framing and citations; they do not generate management plans.

> [!CAUTION]
> A user request phrased as *"What should I do about the cheatgrass on my pasture?"* is a request for instruction. The architectural answer is to ABSTAIN with explicit redirection: *"KFM provides management framing and source-of-record citations; specific management instructions are the responsibility of [KDA / NRCS / county weed director / etc.]."* The AI does not become a management consultant.

### 10.3 The line in cross-lane joins

Joins do not get to relax the rule. A Flora × Agriculture join (the canonical case from §7 row 7) produces management framing; it does not produce management instruction even when both inputs would individually permit a framing claim. A Fauna × Hazards join cites disease/mortality context; it does not produce eradication instruction even when the disease is itself invasive.

[Back to top](#quick-jump)

---

## 11. Cross-lane joins as governed projections

PROPOSED — synthesizing the §7 join register, the §8 source-role rule, the §9 sensitivity rule, and the §10 framing rule.

Every cross-lane invasive join MUST satisfy:

1. **Source-role preservation** — each contributing record's source role travels with the join; the join derivative records it (§8).
2. **Most-restrictive tier** — the join's sensitivity tier is the most-restrictive of any contributing record (§9, `MAP_TRUST_STATES.md` §6.2).
3. **EvidenceBundle composition** — the join produces a new `EvidenceBundle` that references each contributing bundle by `EvidenceRef`; it does not flatten them (`docs/standards/EVIDENCE_BUNDLE.md`).
4. **Receipt emission** — the join emits its own receipt (`TransformReceipt` for the join logic; `AggregationReceipt` if the join produces summaries; `PolicyDecision` for the source-role check).
5. **Framing constraint** — the join's output is framing, not instruction (§10).
6. **Authority preservation** — the join does not transfer authority from one domain to another; if Fauna identifies a taxon and Agriculture records its pest impact, the join cites both; it does not promote Agriculture to taxonomic authority.

### 11.1 What a governed projection looks like

A cross-lane invasive projection (e.g., "invasive plant pressure in agricultural watersheds") is:

```text
InvasivePlantRecord (Flora, source role: APHIS survey)
  +
HUC12 watershed boundary (Hydrology, source role: regulatory)
  +
Cropland Data Layer (Agriculture, source role: aggregate)
  ↓ governed by policy/invasives/agriculture-watershed/
    ↓ TransformReceipt: spatial intersection
      ↓ AggregationReceipt: county-watershed summary
        ↓ ReviewRecord: Flora steward + Agriculture steward
          ↓ PolicyDecision: framing-not-instruction check ALLOW
            ↓ EvidenceBundle: cites all three inputs
              ↓ PromotionDecision → ReleaseManifest
                ↓ Public layer: "Invasive-plant pressure overview, county-watershed summary"
```

The public layer **frames** invasive context across two domains; it does **not** instruct any action; it carries the framing constraint as part of its release manifest's `policy_result` slot.

[Back to top](#quick-jump)

---

## 12. Public products

CONFIRMED — Atlas §7.G:

> *"Domain viewing products [Fauna] include … invasive monitoring public layer …"*

The corpus names one public product directly (Fauna's invasive monitoring public layer). The full PROPOSED inventory:

| Public product | Domain | Source records | Sensitivity |
|---|---|---|---|
| Invasive monitoring public layer (animal) | Fauna | `Invasive Species Record` + public-safe occurrences | T0 / T1 generalized |
| Invasive-plant public layer | Flora | `InvasivePlantRecord` + public-safe occurrences | T0 / T1 generalized |
| Cross-lane invasive pressure summary | Cross-lane projection | Multiple inputs; framing-constrained | T1 aggregate |
| Aquatic invasive watershed status | Fauna × Hydrology projection | `Invasive Species Record` + `HUCUnit` | T0 / T1 generalized |
| Forest-pest county status | Fauna × Settlements/Infrastructure | Critical-asset rules apply where pest impacts critical infrastructure | T1 county-level; precise tree locations follow `critical-asset-exposure.md` |
| Designated-list browser | Regulatory crosswalk | KDA noxious-weed list; federal injurious-wildlife list | T0 designations |
| Early-detection alert framing (informational only — never an alert) | Fauna / Flora | High-priority early observations | T2 default; public version may be T4 / `unavailable` chip |

> [!NOTE]
> "Early-detection alert framing" (last row) is the most delicate. It is **framing** — KFM publishes that a high-priority detection has occurred (without precise location) so that the responsible authority can act. It is **not** an alert — the responsible authority is the alert authority. The public version may withhold even the existence of the detection until eradication response permits disclosure.

[Back to top](#quick-jump)

---

## 13. Anti-patterns

CONFIRMED — synthesized from Atlas §24.4.5, §24.4.6, §24.9.2, §24.9.3; `kfm_unified_doctrine_synthesis.md` §17, §20.

| Anti-pattern | What goes wrong | DENY surface |
|---|---|---|
| **Modeled spread polygon presented as observed occurrence** | Source-role collapse; "Asian carp observed in lake X" when the source is a model prediction. | Validator; Focus Mode citation evaluator; AI runtime. |
| **Aggregate cited as per-place observation** | Source-role collapse; county-decade summary plotted as a point. | Validator. |
| **Regulatory designation substituted for observation** | "Cheatgrass is in this parcel" (citing the noxious-weed list, not a survey). | Validator; Focus Mode. |
| **Management record substituted for occurrence** | "Cheatgrass is here" (citing a treatment log, which proves treatment, not presence). | Validator. |
| **Invasive-plant management instruction** | "Apply herbicide X at rate Y" — the doctrine §10 violation. | Governed API (no instruction endpoint); AI runtime ABSTAIN. |
| **KFM as invasive-response alert authority** | "Spray now" — generalizes the alert-authority anti-pattern. | Trust-membrane anti-pattern row; same denial. |
| **Citizen-science observation treated as authoritative survey** | GBIF point treated as APHIS-confirmed; identification-quality concerns ignored. | Source-role gate; Focus Mode. |
| **Early-detection precise location leaked via Focus Mode inference** | AI stitches public-safe layers to imply an early-infestation point. | Governed AI runtime; ABSTAIN. |
| **Invasive identity claimed by Agriculture** | A pest stress record names a species without citing Fauna or Flora as the taxonomic source. | Validator; cross-lane authority-preservation check. |
| **Aquatic invasive published at precise spawning-ground location** | Most-restrictive rule violated; `SensitiveSite` sensitivity overridden by invasive context. | Promotion gate; sensitivity reviewer. |
| **Cross-lane derivative without its own EvidenceBundle** | The join silently inherits one side's bundle; the audit chain breaks. | Validator; promotion gate. |
| **Invasive list maintained ad hoc rather than in policy** | Per-jurisdiction designations drift; KFM's view diverges from KDA's. | `policy/invasives/registry/`; per-source synchronization. |
| **Forest-pest impact on critical infrastructure published precisely** | Critical-asset-exposure rules ignored. | `docs/architecture/critical-asset-exposure.md` §9; promotion gate. |
| **Steward review skipped on early-detection observation** | Early-detection sensitivity rule (§9.2) bypassed. | Promotion gate; review-record validator. |

[Back to top](#quick-jump)

---

## 14. Tensions and known limits

| # | Tension | Source | KFM posture |
|---|---|---|---|
| 1 | **No corpus-level `policy/invasives/` home** — sensitivity policy lives at `policy/sensitivity/fauna/` and `policy/sensitivity/flora/`; cross-domain invasives logic has no documented home. | Atlas crosswalk (§24.13) | PROPOSED `policy/invasives/` parallel to `policy/sensitivity/`. ADR / Directory Rules update NEEDED — §15 item 1. |
| 2 | **Source-role normalization** across citizen-science aggregators (GBIF, iNaturalist, eBird, EDDMapS) is non-trivial; each has different identification-quality conventions. | §8 | Per-source `SourceDescriptor` records the convention; `policy/invasives/source-role-rubric/` (PROPOSED) defines the cross-source role-equivalence. |
| 3 | **Early-detection sensitivity** is per-case (depends on response capacity, regional context, eradication feasibility); it cannot be hardcoded. | §9.2 | Steward-review-gated; no single tier rule. The architecture defers to per-class steward judgment. |
| 4 | **Asymmetry between established and early-detection invasives** complicates uniform UI presentation. | §9.3 | Per-record sensitivity tier carried explicitly in the `EvidenceBundle`; the UI consumes the tier, not a heuristic. |
| 5 | **Cross-jurisdictional designation differences** — a species designated noxious in Kansas may not be designated in a neighboring state. | §4, §12 | Designation is per-jurisdiction; the record carries the jurisdiction. KFM does not unify the lists. |
| 6 | **Aquatic vs terrestrial split** — aquatic invasives cross Fauna × Hydrology in a way that terrestrial invasives do not; the policy surface is asymmetric. | §7.1 | PROPOSED separate `policy/invasives/aquatic/` and `policy/invasives/terrestrial/` subspecializations. NEEDS DECISION. |
| 7 | **Forest pest × critical infrastructure** — emerald ash borer impact on critical-route trees crosses §9 sensitivity floor. | §9.2, `critical-asset-exposure.md` §9 | Most-restrictive rule applies; critical-asset rules dominate. |
| 8 | **Citizen-science volume** can drown out official-survey records in joins; high-volume but lower-authority sources risk false equivalence. | §8 | The architecture preserves source role; the UI weights presentation by source role; the AI qualifies answers by source role. |
| 9 | **Modeled-spread predictions are useful** but trivial to misuse as if observations. | §8 anti-pattern, §13 | Strict source-role tagging; refuse displays that would erase the modeling distinction; `RealityBoundaryNote`-class chip for modeled-spread layers. |
| 10 | **Some invasive-related questions are legitimately answerable as alerts** (e.g., a regulated noxious-weed obligation triggers a landowner's legal duty). | §10 | KFM still does not issue the alert — it cites the obligation and the responsible authority. The user's legal duty is between them and KDA, not KFM. |
| 11 | **Public-record / regulatory-list synchronization** — KDA updates the noxious-weed list; KFM's view must follow. Latency creates inconsistency. | §12 | `SourceDescriptor` records the cadence; out-of-date list triggers stale-state badge; cache invalidation per `RELEASE_MANIFEST.md` §10. |
| 12 | **Pest stress overlaps with disease overlaps with invasive** in some real cases (e.g., a vector-borne plant disease caused by an invasive insect). | §7 | Each contributing domain owns its slice; the join cites all three; the resulting derivative is a framing-only product. |

[Back to top](#quick-jump)

---

## 15. Open questions

UNKNOWN / NEEDS VERIFICATION items, tracked here until resolved by ADR or mounted-repo evidence.

1. **`policy/invasives/` as a new policy folder** — PROPOSED in §3 and §14 item 1. ADR or Directory Rules update NEEDED.
2. **Per-source identification-quality rubric** — `policy/invasives/source-role-rubric/` (PROPOSED) needs to be authored before cross-source joins can be admitted.
3. **Aquatic vs terrestrial split** — separate subspecializations (§14 item 6) or one unified rule.
4. **Early-detection threshold** — what triggers the early-detection sensitivity rule (§9.2); per-class, per-region, per-steward.
5. **Forest pest × critical infrastructure** integration point with `docs/architecture/critical-asset-exposure.md`.
6. **Designated-list mirroring cadence** — how often KFM resyncs noxious-weed and injurious-wildlife lists.
7. **AI ABSTAIN copy for invasive-management requests** — exact phrasing of the §10 redirect.
8. **`RealityBoundaryNote`-class chip for modeled-spread predictions** — visual treatment parallel to 3D scenes (§14 item 9); needs design.
9. **Per-jurisdiction governance** — when KFM serves data across state boundaries, whose designation list governs the display?
10. **Aggregation thresholds** for invasive-pressure summaries — minimum cell counts to avoid implying a per-place observation.
11. **Cross-domain Story Node templates** for invasive narratives — `ui/CONTINUITY_NOTES.md` §5 narrative continuity applies.
12. **Citizen-science volume weighting** in cross-source joins (§14 item 8).
13. **Public-record exception** for already-public invasive observations (parallel to `critical-asset-exposure.md` §14 item 7).
14. **Where the per-jurisdiction designation registry lives** — `data/registry/invasive-designations/` (PROPOSED).

[Back to top](#quick-jump)

---

## 16. Related docs

PROPOSED links — verify all paths against mounted repo before publishing.

### Architecture

- [`docs/architecture/TRUST_MEMBRANE.md`](./TRUST_MEMBRANE.md) — the membrane this document's joins traverse.
- [`docs/architecture/critical-asset-exposure.md`](./critical-asset-exposure.md) — the §9.2 sensitivity rule for forest-pest × critical infrastructure interactions.
- [`docs/architecture/system-context.md`](./system-context.md) — _PROPOSED placement._
- [`docs/architecture/governed-api.md`](./governed-api.md) — _PROPOSED placement._ The framing-not-instruction enforcement point.
- [`docs/architecture/map-shell.md`](./map-shell.md) — _PROPOSED placement._
- [`docs/architecture/maplibre-3d.md`](./maplibre-3d.md) — anchors any 3D invasive-monitoring product.
- [`docs/architecture/ui/CONTINUITY_NOTES.md`](./ui/CONTINUITY_NOTES.md) — narrative continuity for invasive Story Nodes.
- [`docs/architecture/contract-schema-policy-split.md`](./contract-schema-policy-split.md) — _PROPOSED placement._

### Standards

- [`docs/standards/MAP_TRUST_STATES.md`](../standards/MAP_TRUST_STATES.md) — most-restrictive-tier rule, trust-state vocabulary.
- [`docs/standards/EVIDENCE_BUNDLE.md`](../standards/EVIDENCE_BUNDLE.md) — bundle composition for cross-lane derivatives.
- [`docs/standards/RELEASE_MANIFEST.md`](../standards/RELEASE_MANIFEST.md) — release-side handling of cross-lane derivatives.
- [`docs/standards/PROV/README.md`](../standards/PROV/README.md) — provenance threading across the join.
- [`docs/standards/DUO_PROFILE.md`](../standards/DUO_PROFILE.md) — consent gates where invasive data is consent-bearing.
- [`docs/standards/SENSITIVITY_RUBRIC.md`](../standards/SENSITIVITY_RUBRIC.md) — _PROPOSED, not yet authored._

### Per-domain implementation homes (per Atlas §24.13 crosswalk)

- [`contracts/v1/fauna/`](../../contracts/v1/fauna/) — `Invasive Species Record` and sibling Fauna objects.
- [`contracts/v1/flora/`](../../contracts/v1/flora/) — `InvasivePlantRecord` and sibling Flora objects.
- [`contracts/v1/agriculture/`](../../contracts/v1/agriculture/) — `PestStressIndicator` (Agriculture-owned identity per Atlas §24.4.5).
- [`contracts/v1/hydrology/`](../../contracts/v1/hydrology/) — `HUCUnit` and waterbody identities for aquatic-invasive joins.
- [`schemas/contracts/v1/fauna/`](../../schemas/contracts/v1/fauna/), [`schemas/contracts/v1/flora/`](../../schemas/contracts/v1/flora/) — machine shapes.
- [`policy/sensitivity/fauna/`](../../policy/sensitivity/fauna/) — Fauna sensitivity rules (Atlas crosswalk).
- [`policy/sensitivity/flora/`](../../policy/sensitivity/flora/) — Flora sensitivity rules (Atlas crosswalk).
- [`policy/invasives/`](../../policy/invasives/) — _PROPOSED home._ Cross-domain invasives policy.
- [`policy/invasives/source-role-rubric/`](../../policy/invasives/source-role-rubric/) — _PROPOSED._ Cross-source role-equivalence rules.
- [`policy/invasives/aquatic/`](../../policy/invasives/aquatic/) — _PROPOSED._ Aquatic-invasive-specific cross-lane rules.

### Tests / runbooks

- [`tests/invasives/`](../../tests/invasives/) — cross-lane join fixtures; source-role anti-collapse negative tests.
- [`fixtures/invasives/`](../../fixtures/invasives/) — citizen-science, official-survey, modeled-spread, aggregate, regulatory, management-record fixtures (one per source role).
- [`docs/runbooks/fauna/`](../runbooks/fauna/) — Fauna domain runbook (prior-session-authored Fauna source-refresh runbook).
- [`docs/runbooks/flora/`](../runbooks/flora/) — _PROPOSED._ Flora analog.
- [`docs/runbooks/invasives/`](../runbooks/invasives/) — _PROPOSED._ Cross-domain runbook for steward review of early-detection observations.

[Back to top](#quick-jump)

---

<details>
<summary><strong>Appendix A — Cross-lane invasive scenarios matrix</strong></summary>

PROPOSED — illustrative scenarios mapping each cross-lane join from §7 to a concrete invasive case. Species named for illustration only; jurisdictional designation is per-source and per-time.

| Scenario | Cross-lane | Authoritative identity | Authoritative context | Architectural disposition |
|---|---|---|---|---|
| Cheatgrass coverage across rangeland | Flora × Habitat × Agriculture | Flora `InvasivePlantRecord` | Habitat ecological system; Agriculture rangeland CDL | Framing layer; T0/T1; AggregationReceipt at county-watershed |
| Sericea lespedeza in CRP fields | Flora × Agriculture | Flora `InvasivePlantRecord` | Agriculture CRP enrollment | Framing layer; T1 county-summary; no instruction on treatment |
| Eastern red cedar encroachment | Flora × Habitat | Flora `InvasivePlantRecord` (regional designation) | Habitat ecological system shift | Framing layer; T0 county-decade trend; private-parcel detail denied |
| Feral hog occurrence | Fauna × Agriculture | Fauna `Invasive Species Record` | Agriculture damage records | Framing layer; T1; pest stress = Agriculture-owned |
| Emerald ash borer on critical-route street trees | Fauna × Settlements/Infrastructure | Fauna `Invasive Species Record` | Critical-asset detail | T4 for precise tree-by-tree; T1 generalized; `critical-asset-exposure.md` §9 governs |
| Asian carp in a watershed | Fauna × Hydrology | Fauna `Invasive Species Record` | Hydrology `HUCUnit` | Framing layer; T0/T1 watershed-level; spawning-ground precise denied |
| Zebra mussels at boat-ramp entries | Fauna × Hydrology × Settlements | Fauna `Invasive Species Record` | Hydrology + Settlements/Infrastructure | Framing layer; T0 site-level (public boat ramps are public); commercial-marina detail per `critical-asset-exposure.md` |
| West Nile virus in mosquito populations | Fauna × Hazards | Fauna `DiseaseObservation` + Fauna `Invasive Species Record` (vector) | Hazards public-health frame | T2/T4; KDHE-class data; KFM cites authority, does not issue alert |
| Chronic wasting disease in cervid populations | Fauna × Hazards | Fauna `DiseaseObservation` | Hazards / wildlife-health frame | T2 default; KDWP authority; framing only |
| Hydrilla in an irrigation district | Flora × Hydrology × Agriculture | Flora `InvasivePlantRecord` | Hydrology district + Agriculture irrigation | Framing layer; T1 county-summary |
| Salt cedar in riparian corridors | Flora × Hydrology | Flora `InvasivePlantRecord` | Hydrology reach | Framing layer; T0/T1 |
| Invasive plant obscuring an archaeological site | Flora × Archaeology | Flora `InvasivePlantRecord` | Archaeology context (steward-gated) | Site location denied per `policy/sensitivity/archaeology/`; invasive context published with site-anonymized |
| Early-detection observation of a high-priority Q-listed pest | Fauna or Flora (single record) | Fauna or Flora identity | Per-class steward review | T2 / T4 depending on response capacity; "unavailable" chip in public (§6.1 of `critical-asset-exposure.md`) |
| Modeled spread prediction of an emerging invasive | Fauna or Flora + Model | Modeled source role | None observed yet | `ModelRunReceipt`; `RealityBoundaryNote`-class chip; never displayed as an observation |
| Aggregate county-decade invasive pressure | Cross-lane aggregate | All contributing domains | County panel | `AggregationReceipt`; T0/T1; framing only |

</details>

<details>
<summary><strong>Appendix B — Source-role anti-collapse worked example</strong></summary>

A real-shape question: *"Is Asian carp in Cheney Reservoir?"*

**Available evidence (illustrative; not a claim about actual Cheney Reservoir data):**

| Source | Source role | What it says |
|---|---|---|
| GBIF / iNaturalist observation by a fisher | Observed (citizen-science) | One photographed catch, identified by community |
| KDWP fish survey 2024 | Observed (official survey) | Multi-method survey; species detected at low abundance |
| USACE modeled spread prediction | Modeled | High suitability for Asian carp habitat |
| Kansas designation list | Regulatory | Asian carp is a designated injurious species |
| KDWP eradication/monitoring log | Management record | Documented monitoring activity at the reservoir |

**The collapse failure mode (what NOT to do):**

```text
AI answer: "Yes, Asian carp is in Cheney Reservoir."
```

This answer collapses five distinct source roles into a single assertion. It is wrong in five different ways:

1. The citizen-science observation is *an* observation, not a population estimate.
2. The KDWP survey is the authoritative observed record.
3. The USACE model is a prediction, not an observation.
4. The regulatory designation is a list entry, not a record of presence.
5. The management log is a record of *action*, not of *presence*.

**The architectural answer (what KFM does):**

```text
AI answer (FocusModeResponse with citations):
"Asian carp has been documented in Cheney Reservoir by the 2024 KDWP fish survey
[evidence ref: KDWP-fish-survey-2024], at low abundance with stated methodology
[methodology evidence ref]. A 2022 citizen-science observation [evidence ref: 
GBIF-record-XYZ] is consistent with this. The USACE spread model predicts high
habitat suitability for the species in this watershed [evidence ref: USACE-model-2023];
this is a prediction, not an observation. Asian carp is a designated injurious
species in Kansas [evidence ref: KDA-designation-list]. KDWP maintains a monitoring
log for this reservoir [evidence ref: KDWP-monitoring-log]; KDWP is the responsible
authority for management decisions."
```

This answer:

- Preserves five distinct source roles.
- Cites each contributing piece of evidence.
- Distinguishes "documented at low abundance" (observation) from "predicted high suitability" (model).
- Cites the regulatory designation without substituting it for evidence.
- Acknowledges the management log as a record of action, not presence.
- Identifies KDWP as the responsible authority, framing not instruction.
- Returns ANSWER (not ABSTAIN) because evidence closure holds for the cited claims.

**What the AI does NOT include:**

- *"You should…"* anything. The §10 framing-not-instruction rule.
- *"The carp will spread to…"* — a prediction phrased as fact.
- *"Cheney Reservoir is contaminated"* — value-laden language not in the evidence.
- A point on a map at the precise observation coordinates if those coordinates are restricted under Fauna's `SensitiveSite` or geoprivacy rules.

This is the architecture, end-to-end, for one cross-lane invasive question. The same source-role discipline applies to every row in Appendix A.

</details>

---

### Footer

> **Document class:** Cross-domain integration architecture explainer · **Scope:** How KFM handles invasive species across Fauna, Flora, Habitat, Agriculture, Hydrology, Hazards, and Archaeology · **Authority NOT held:** per-domain object meaning, machine shape, admissibility code, observation-level records, per-species jurisdictional lists.

| | |
|---|---|
| **Domain anchors** | Fauna ownership — Atlas §7 · Flora ownership — Atlas §8 · Cross-lane edges — Atlas §24.4 |
| **Membrane** | [`TRUST_MEMBRANE.md`](./TRUST_MEMBRANE.md) — the broader architecture this document's joins traverse |
| **Adjacent** | [`critical-asset-exposure.md`](./critical-asset-exposure.md) — forest-pest × critical-infrastructure rule |
| **Sibling architecture** | [system-context.md](./system-context.md) · [governed-api.md](./governed-api.md) · [map-shell.md](./map-shell.md) · [maplibre-3d.md](./maplibre-3d.md) · [ui/CONTINUITY_NOTES.md](./ui/CONTINUITY_NOTES.md) |
| **Companion standards** | [MAP_TRUST_STATES.md](../standards/MAP_TRUST_STATES.md) · [EVIDENCE_BUNDLE.md](../standards/EVIDENCE_BUNDLE.md) · [RELEASE_MANIFEST.md](../standards/RELEASE_MANIFEST.md) · [PROV/](../standards/PROV/README.md) · [DUO_PROFILE.md](../standards/DUO_PROFILE.md) |
| **Per-domain homes** | [`contracts/v1/fauna/`](../../contracts/v1/fauna/) · [`contracts/v1/flora/`](../../contracts/v1/flora/) · [`policy/sensitivity/fauna/`](../../policy/sensitivity/fauna/) · [`policy/sensitivity/flora/`](../../policy/sensitivity/flora/) · _`policy/invasives/` (PROPOSED)_ |
| **Last updated** | 2026-05-24 |
| **Doc owner** | _TBD_ |

[Back to top](#quick-jump)
