<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/flora-continuity-inventory
title: Flora Domain — Continuity Inventory
type: standard
version: v1
status: draft
owners: <flora-domain-steward> (PLACEHOLDER), <docs-steward> (PLACEHOLDER)
created: 2026-05-16
updated: 2026-05-16
policy_label: public
related: [
  "docs/doctrine/directory-rules.md",
  "docs/domains/README.md",
  "docs/domains/flora/README.md",
  "docs/domains/fauna/CONTINUITY_INVENTORY.md",
  "docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md",
  "docs/sources/SOURCE_DESCRIPTOR_STANDARD.md",
  "docs/standards/PROV.md",
  "docs/registers/VERIFICATION_BACKLOG.md",
  "docs/registers/DRIFT_REGISTER.md"
]
tags: [kfm, domain, flora, continuity, lineage, doctrine]
notes: [
  "Prior gains carried forward as doctrine, lineage, or proposed design pressure — never as mounted repo implementation without proof.",
  "All non-directory-rules.md repo paths are PROPOSED / NEEDS VERIFICATION until checked against a mounted KFM repo.",
  "Companion of docs/domains/fauna/CONTINUITY_INVENTORY.md; the two should evolve in lockstep where lanes intersect."
]
[/KFM_META_BLOCK_V2] -->

# Flora Domain — Continuity Inventory

> Carry-forward register for KFM's Flora lane. Records what prior work earned, how each gain is reclassified for next work, and where each claim still needs repo evidence before it counts as implementation.

![Status](https://img.shields.io/badge/status-draft-orange) ![Type](https://img.shields.io/badge/type-continuity%20inventory-blue) ![Lane](https://img.shields.io/badge/lane-flora-2e8b57) ![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20WORK%2FQUARANTINE%20%E2%86%92%20PROCESSED%20%E2%86%92%20CATALOG%2FTRIPLET%20%E2%86%92%20PUBLISHED-555) ![Sensitivity](https://img.shields.io/badge/sensitive%20locations-deny%20by%20default-b22222) ![Authority](https://img.shields.io/badge/authority-doctrine%20%2B%20directory--rules.md-blueviolet) ![Build](https://img.shields.io/badge/build-TODO-lightgrey) ![Last%20updated](https://img.shields.io/badge/updated-2026--05--16-informational)

| | |
|---|---|
| **Status** | draft |
| **Owners** | `<flora-domain-steward>` (PLACEHOLDER), `<docs-steward>` (PLACEHOLDER) |
| **Last updated** | 2026-05-16 |
| **Authority** | KFM doctrine; `docs/doctrine/directory-rules.md`; flora lineage corpus (DOM-FLORA, ENCY §7.6, UNIFIED §6.5, Pass 18 → Pass 20) |
| **Companion** | `docs/domains/fauna/CONTINUITY_INVENTORY.md` (parallel lane) — PROPOSED |

> [!IMPORTANT]
> **Continuity ≠ implementation.** Items appearing in this inventory are carried forward as **doctrine**, **lineage**, or **proposed design pressure**. None are represented as mounted repo implementation without independently checked evidence. Every implementation-shaped claim is labeled `CONFIRMED`, `PROPOSED`, `NEEDS VERIFICATION`, or `UNKNOWN` per KFM truth posture.

---

## Contents

1. [Purpose & scope](#1-purpose--scope)
2. [Continuity determination](#2-continuity-determination)
3. [Authority order](#3-authority-order)
4. [How to read this inventory](#4-how-to-read-this-inventory)
5. [Prior gains — continuity classification table](#5-prior-gains--continuity-classification-table)
6. [Mission and boundary carry-forward](#6-mission-and-boundary-carry-forward)
7. [Ubiquitous-language carry-forward](#7-ubiquitous-language-carry-forward)
8. [Object-family carry-forward](#8-object-family-carry-forward)
9. [Source-family carry-forward](#9-source-family-carry-forward)
10. [Sensitivity-posture carry-forward](#10-sensitivity-posture-carry-forward)
11. [Pipeline-shape carry-forward](#11-pipeline-shape-carry-forward)
12. [Map and viewing-product carry-forward](#12-map-and-viewing-product-carry-forward)
13. [Cross-lane relations carry-forward](#13-cross-lane-relations-carry-forward)
14. [API, contract, schema-surface carry-forward](#14-api-contract-schema-surface-carry-forward)
15. [Governed-AI / Focus-Mode carry-forward](#15-governed-ai--focus-mode-carry-forward)
16. [Validators, tests, fixtures carry-forward](#16-validators-tests-fixtures-carry-forward)
17. [Publication / correction / rollback carry-forward](#17-publication--correction--rollback-carry-forward)
18. [PLANTS watcher — operational expansion pressure](#18-plants-watcher--operational-expansion-pressure)
19. [File-home and placement notes](#19-file-home-and-placement-notes)
20. [Flora-specific verification backlog](#20-flora-specific-verification-backlog)
21. [Update-propagation matrix](#21-update-propagation-matrix)
22. [Related docs](#22-related-docs)

---

## 1. Purpose & scope

This file is the **continuity register** for the Flora lane. Its job is narrow:

- **Preserve** what prior KFM flora work (blueprints, dossiers, encyclopedias, atlases, pass dossiers, ideas packets) earned that should not be silently re-derived.
- **Classify** each prior gain with one of: `KEEP AND EXTEND`, `WRAP WITH ADAPTER`, `KEEP AS LINEAGE`, `DEFER`, `RETIRE — superseded`.
- **Pin** each carried-forward item to its **evidence basis** in the indexed corpus.
- **State the preserved-next-behavior** that downstream PRs, ADRs, schemas, and runbooks should honor.
- **Surface** what cannot yet be claimed as implemented and should be entered on the [verification backlog](#20-flora-specific-verification-backlog).

This file is **not**:

- A flora architecture overview (see the proposed `docs/domains/flora/README.md`).
- An object-family contract (see proposed `contracts/domains/flora/`).
- A source-refresh runbook (see proposed `docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md`, parallel to the Fauna runbook).
- An ADR record (see `docs/adr/`).

> [!NOTE]
> **Companion document.** This inventory is the flora parallel of `docs/domains/fauna/CONTINUITY_INVENTORY.md`. The two lanes share many gains (deny-by-default exact-location posture, RedactionReceipt, watcher-as-non-publisher, taxonomy-reconciliation discipline) and should evolve in lockstep where they intersect — particularly on cross-lane joins (Flora × Fauna pollinator and food-web; Flora × Habitat vegetation community).

[Back to top ↑](#contents)

---

## 2. Continuity determination

The doctrinal carry-forward principle for KFM expansions is fixed:

> **Prior gains are not discarded. They are carried forward as doctrine, lineage, or proposed design pressure. None are represented as mounted implementation without repo evidence.**
> — adapted from the Whole-UI + Governed AI Expansion Report §6 "Prior gains and continuity inventory"

For the Flora lane specifically:

- **CONFIRMED doctrine.** Flora governs plant taxonomic identity, flora occurrences, specimens, surveys, vegetation communities, rare / protected / culturally sensitive flora controls, public-safe surfaces, evidence-backed maps, correction, and rollback. [DOM-FLORA] [ENCY §7.6]
- **CONFIRMED invariant.** Rare, protected, culturally sensitive, and steward-reviewed flora default to generalized, withheld, staged, or denied public geometry. [DOM-FLORA] [ENCY §20.5 deny-by-default register]
- **CONFIRMED non-regression posture.** Prior domain reports and implementation references "must be preserved as lineage, not silently overwritten. Domain expansion should include continuity maps, migration notes, alias/deprecation handling where needed, and non-regression tests before replacing prior scaffold semantics." [UNIFIED §5.3]
- **PROPOSED implementation.** All concrete paths, schemas, validators, routes, tests, CI, and policy enforcements relevant to flora remain **PROPOSED** until verified against a mounted KFM repository.

[Back to top ↑](#contents)

---

## 3. Authority order

When this file is updated, conflicts are resolved in this fixed order (mirrors `directory-rules.md` §2.1):

1. **KFM core invariants and doctrine** — lifecycle law (`RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`), trust membrane, cite-or-abstain, watcher-as-non-publisher, deny-by-default sensitivity.
2. **Accepted ADRs** that explicitly amend flora doctrine, by ADR number. Superseded ADRs do not count.
3. **`docs/doctrine/directory-rules.md`** (the only file viewed CONFIRMED in this session) and other accepted doctrine docs under `docs/doctrine/`.
4. **This file** and adjacent flora-lane docs (`docs/domains/flora/`).
5. **Indexed flora corpus** — DOM-FLORA blueprint, ENCY §7.6, UNIFIED §6.5, Pass 18 / Pass 19 / Pass 20 entries, New Ideas 5-15 (PLANTS drift), Domains Atlas v1.1.
6. **Current mounted repo convention** — if it conflicts with the above, file a row in `docs/registers/DRIFT_REGISTER.md` rather than treating it as new authority.

[Back to top ↑](#contents)

---

## 4. How to read this inventory

Each carry-forward row uses the four-column shape established by the Whole-UI continuity inventory:

| Column | Meaning |
|---|---|
| **Surface or prior gain** | The concept, surface, vocabulary item, contract, or object family being preserved. |
| **Classification** | `KEEP AND EXTEND`, `WRAP WITH ADAPTER`, `KEEP AS LINEAGE`, `DEFER`, or `RETIRE — superseded`. |
| **Evidence basis** | The corpus source(s) that establish the gain. Bracketed `[TAG]` references resolve in §22 Related docs and in the source ledger. |
| **Preserved next behavior** | What downstream PRs, ADRs, schemas, runbooks, and validators should do with this gain. |

Classification semantics (CONFIRMED; mirrors Whole-UI report and Pass 20 conventions):

| Label | Meaning |
|---|---|
| `KEEP AND EXTEND` | The gain stays as-is in doctrine; downstream work expands its operational artifacts (schemas, validators, fixtures, runbooks, ADRs). |
| `WRAP WITH ADAPTER` | The gain is preserved but accessed through a typed boundary (port/adapter, governed API, transform receipt) — its raw form does **not** become the public path. |
| `KEEP AS LINEAGE` | The gain is preserved as **planning lineage**, not as implementation. It informs naming, structure, and validators but does not by itself prove repo behavior. |
| `DEFER` | The gain is recognized but intentionally excluded from the next slice; a future trigger reactivates it. |
| `RETIRE — superseded` | The gain was replaced by a stronger or clearer formulation; the prior form is archived to `docs/archive/lineage/` (PROPOSED) with a forward link. |

Truth labels used in cell content follow KFM convention: `CONFIRMED`, `INFERRED`, `PROPOSED`, `NEEDS VERIFICATION`, `UNKNOWN`, `CONFLICTED`, `DEFERRED`.

[Back to top ↑](#contents)

---

## 5. Prior gains — continuity classification table

> [!NOTE]
> Source tag legend used throughout: **[DOM-FLORA]** Flora architecture blueprint PDF (lineage); **[ENCY]** `kfm_encyclopedia.pdf` (doctrine); **[UNIFIED]** Unified Implementation Architecture Build Manual (doctrine + lineage); **[ATLAS]** `KFM_Domains_Culmination_Atlas_v1_1.pdf` §8 Flora (lineage + doctrine restatement); **[P18]** Pass 18 idea-card baseline; **[P19]** Pass 19 normalized atlas; **[P20]** `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`; **[NI-5-15]** New Ideas 5-15-26 (PLANTS / CDL drift packet); **[GAI]** Governed AI doctrine; **[DIRRULES]** `docs/doctrine/directory-rules.md`.

| Surface or prior gain | Classification | Evidence basis | Preserved next behavior |
|---|---|---|---|
| **Lane mission: govern plant taxonomic identity, flora occurrences, specimens, surveys, vegetation communities, rare/protected/culturally sensitive flora controls, public-safe surfaces, evidence-backed maps, correction, and rollback.** | KEEP AND EXTEND | [DOM-FLORA] [ENCY §7.6] [ATLAS §8.A] | Mission statement is doctrine; expansions add schemas, validators, fixtures, runbooks, and ADRs, never new mission language without doctrine review. |
| **Lane boundary — explicit non-ownership** (Habitat owns habitat patches/suitability; Fauna owns animal taxa/occurrences; soil/hydrology/agriculture/hazards/roads/settlements/archaeology/people keep their truth). | KEEP AND EXTEND | [DOM-FLORA] [ATLAS §8.B] [ENCY §7.6] | Cross-lane joins must preserve ownership and route through governed surfaces; downstream work adds explicit cross-lane validators. |
| **Ubiquitous language** — Plant Taxon, FloraTaxon Crosswalk, Flora Occurrence, SpecimenRecord, Rare Plant Record, Vegetation Community, InvasivePlantRecord, Phenology Observation, RangePolygon, DistributionSurface, Habitat Association, SourceRole, Redaction Receipt. | KEEP AND EXTEND | [DOM-FLORA] [ATLAS §8.C] [ENCY §7.6] | Vocabulary is doctrine; new terms require contracts entries and ADR consideration before adoption. Casing and compound-term spelling preserved verbatim. |
| **Canonical object families** — PlantTaxon, SpecimenRecord, FloraOccurrence, RarePlantRecord, VegetationCommunity, InvasivePlantRecord, PhenologyObservation, RangePolygon, HabitatAssociation, BotanicalSurvey, RestorationPlanting, RedactionReceipt. | KEEP AND EXTEND | [ENCY §7.6.C] [DOM-FLORA] [ATLAS §8.E] [UNIFIED §6.5] | First contracts wave proposed under `contracts/domains/flora/` (PROPOSED, [DIRRULES §12]); schema home `schemas/contracts/v1/domains/flora/` (PROPOSED, [DIRRULES §7.4]). |
| **Sensitivity posture** — rare / protected / culturally sensitive plant locations default to **generalized, withheld, staged, or denied** public geometry; Redaction Receipt records transforms. | KEEP AND EXTEND | [DOM-FLORA] [ATLAS §8.I] [ENCY §20.5 deny-by-default register] [P20 KFM-IDX-POL-001] | First operational artifacts: sensitivity policy under `policy/domains/flora/` (PROPOSED); negative fixtures proving deny-by-default; transform-receipt validators. |
| **Source-role taxonomy** (authority / observation / context / model) for flora source families. | KEEP AND EXTEND | [DOM-FLORA] [ATLAS §8.D] [ENCY §7.6.B] | Per-source role assignment in source descriptors; source-role authority tests forbidding use outside declared role. |
| **Key source families** — KDWP flora / listed-species context; KDWP Ecological Review Tool / stewardship outputs; Kansas Biological Survey / KU herbarium surfaces; USFWS ECOS plant context; NatureServe Explorer / Explorer Pro; GBIF vascular-plant downloads; iDigBio specimen records; iNaturalist-derived observations. | WRAP WITH ADAPTER | [ATLAS §8.D] [DOM-FLORA] [ENCY §7.6.B] | Live connectors are DEFERRED until source descriptors, rights review, and steward agreements are in place; rights and current terms are NEEDS VERIFICATION across all listed families. Public access flows only through governed API. |
| **USDA PLANTS (county packages)** — sensitivity-prone when joined with GBIF / iNaturalist / heritage datasets. | WRAP WITH ADAPTER | [P20 KFM-IDX-ANA-004] [P20 KFM-IDX-SRC-006] [NI-5-15] | County package = taxa list under recorded taxonomy version; drift via set difference between successive packages; intersect with listed conservation species; wrap as `SourceIntakeRecord` candidate; deny exact public occurrence in joined outputs. See §18. |
| **Pipeline shape** `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED` with promotion as governed state transition (not file move). | KEEP AND EXTEND | [DIRRULES §0, §3] [ATLAS §8.H] [ENCY] [UNIFIED §6.5] | Every flora ingest must traverse all stages; pipelines/specs live under `pipelines/domains/flora/` and `pipeline_specs/flora/` (PROPOSED, [DIRRULES §12]). |
| **Watcher-as-non-publisher** — watchers emit observations, receipts, and candidate decisions only; promotion remains governed. | KEEP AND EXTEND | [NI-5-8] [P20 KFM-IDX-REL-005] [DIRRULES §13.5] | PLANTS / heritage / herbarium watchers emit to `RAW` or `WORK_CANDIDATE`; never write to `data/catalog/` or `data/published/`. |
| **Map and viewing products** — public generalized occurrence layer; public range/distribution layer; vegetation community layer; invasive plant layer; phenology / condition layer; habitat-association summary; review candidate view. | KEEP AND EXTEND | [ATLAS §8.G] [DOM-FLORA] | Layer manifests under `data/published/layers/flora/` (PROPOSED); tile field allowlist tests proving no sensitive geometry leak; trust badges visible per layer. |
| **Cross-cutting viewing surfaces** — Evidence Drawer, time-aware state, trust badges, sensitivity-redacted view, correction/stale-state view, governed Focus Mode. | KEEP AND EXTEND | [ATLAS §8.G CONFIRMED doctrine] [Whole-UI report §6] [GAI] | Flora layers consume the shared shell; no flora-specific UI shell. Drawer payloads include EvidenceBundle / EvidenceRef references. |
| **API surfaces (governed, PROPOSED)** — Flora feature/detail resolver; Flora layer manifest resolver; Flora Evidence Drawer payload; Flora Focus Mode answer. | KEEP AS LINEAGE | [ATLAS §8.J] [DOM-FLORA] | Route names, DTO names, and runtime behavior remain PROPOSED / UNKNOWN until repo / generated client inspected. Schema home `schemas/contracts/v1/domains/flora/` per [DIRRULES §7.4] / ADR-0001. |
| **Validator / test posture** — taxonomy reconciliation; rights/sensitivity validators; exact sensitive public geometry denial; catalog closure tests; API finite-outcome fixtures; no-live-network fixture pipeline. | KEEP AND EXTEND | [ATLAS §8.K] [DOM-FLORA] [UNIFIED §5.3 PROPOSED fixture rule] | Fixture rule: every major flora object family ships at least one valid, one invalid, one denied, one abstention, and one rollback/correction fixture; sensitive lanes ship public-safe transformed fixtures (no real exact rare-plant coordinates). |
| **Governed AI behavior** — AI may summarize released Flora EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. | KEEP AND EXTEND | [GAI] [ATLAS §8.L] [DOM-FLORA] | Focus Mode for flora behind governed API only; no direct model call from browser; finite outcomes `ANSWER / ABSTAIN / DENY / ERROR` rendered as typed states. |
| **Publication / correction / rollback triad** — ReleaseManifest, EvidenceBundle, validation/policy support, review state, correction path, stale-state rule, rollback target. | KEEP AND EXTEND | [ATLAS §8.M] [ENCY Appendix E] [DOM-FLORA] | Every flora release names a rollback target; correction notices propagate to derivative tiles, graph projections, Focus Mode caches per [P20 KFM-IDX-REL-004] propagation rule (still OPEN — see §17). |
| **RedactionReceipt object family** — records geoprivacy transforms, generalization, withholding, and steward review. | KEEP AND EXTEND | [DOM-FLORA] [ATLAS §8.E] [ENCY §7.6.C] | RedactionReceipt is a contract entry; receipts persist with the EvidenceBundle; explainable redaction in Evidence Drawer without leaking the withheld location. |
| **Phenology Observation, Restoration Planting, Botanical Survey** — flora-specific observational / project-record object families. | KEEP AS LINEAGE | [DOM-FLORA] [ENCY §7.6.C] | Object-family meaning is doctrine; contract files and fixtures are PROPOSED. RestorationPlanting carries its own correction posture for project-record evolution. |
| **Cross-lane relations** — Flora × Habitat (habitat association / vegetation community); Flora × Fauna (pollinator, food-web, invasive, biodiversity); Flora × Soil/Hydrology (substrate, wetland, riparian, drought); Flora × Hazards (fire, drought, flood, smoke, vegetation stress). | KEEP AND EXTEND | [ATLAS §8.F] [DOM-FLORA] [ENCY §7.6] | Relations must preserve ownership, source role, sensitivity, and EvidenceBundle support; cross-lane validators live in `tools/validators/<topic>/` per [DIRRULES §12], not under one domain. |
| **Domain scaffold reports** (Flora architecture blueprint PDF, Pass 18/19/20 entries, Domains Atlas v1.1 §8). | KEEP AS LINEAGE | [DOM-FLORA] [P18] [P19] [P20] [ATLAS] | Preserve path patterns, fixture ideas, validator ideas, and rollback shape; do not treat scaffold material as repo implementation. Archive originals to `docs/archive/lineage/` (PROPOSED). |
| **3D / Cesium flora visualization** (vegetation community vertical structure, canopy). | DEFER | [Whole-UI report §12 "Files intentionally deferred"] [P20 PLN] | Add only after 2D evidence continuity, StoryManifest, Evidence Drawer, and sensitivity gates pass; consume the same EvidenceBundle / DecisionEnvelope as 2D per [DIRRULES §11]. |
| **Live source connectors for sensitive families** (rare-plant heritage data, exact occurrence portals). | DEFER | [DOM-FLORA §17-19 "schema/fixture/validator-first"] [UNIFIED §6.5] | No live connector activation before source-role registry, rights review, sensitivity policy, public-safe transform receipts, and steward agreements are in place. |
| **Production auth / SSO for steward consoles**. | DEFER | [Whole-UI report §12] | Add after repo / environment inspection and threat model. |

[Back to top ↑](#contents)

---

## 6. Mission and boundary carry-forward

**CONFIRMED doctrine / PROPOSED implementation.** The Flora lane governs:

- Plant **taxonomic identity** (PlantTaxon, FloraTaxon Crosswalk).
- **Specimen and observation evidence** (SpecimenRecord, FloraOccurrence).
- **Rare / protected / culturally sensitive flora controls** with deny-by-default exact public geometry.
- **Vegetation communities** as polygonal community evidence.
- **Invasive plants** as separately classified records (`InvasivePlantRecord`).
- **Phenology observations** as time-series condition evidence.
- **Range and habitat association**, ecological context joins (always preserving ownership).
- **Restoration plantings** as project-record evidence.
- **Public-safe surfaces**, evidence-backed maps, correction, and rollback.
  [DOM-FLORA] [ENCY §7.6] [ATLAS §8.A]

**CONFIRMED explicit non-ownership.**

| Adjacent lane | What it owns | Constraint |
|---|---|---|
| Habitat | habitat patches and suitability | Flora references via `HabitatAssociation`; never overwrites |
| Fauna | animal taxa and occurrences | Joined via pollinator / food-web / invasive context only |
| Soil, Hydrology, Agriculture, Hazards, Roads, Settlements, Archaeology, People/Land | their respective truths | Flora links via governed cross-lane relations |

[Back to top ↑](#contents)

---

## 7. Ubiquitous-language carry-forward

> [!IMPORTANT]
> **Terminology preservation is non-negotiable.** Case, spacing, and compound-term spelling are preserved verbatim from the source corpus. PRs that silently rename `RarePlantRecord` to `RarePlant`, or collapse `Phenology Observation` into `Phenology`, MUST be rejected per [DIRRULES §2.1] doctrine and KFM truth posture.

| Term | Status | Source |
|---|---|---|
| Plant Taxon | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ENCY §7.6] |
| FloraTaxon Crosswalk | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| Flora Occurrence | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| SpecimenRecord | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ENCY §7.6] |
| Rare Plant Record | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ATLAS §8.C] |
| Vegetation Community | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| InvasivePlantRecord | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| Phenology Observation | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| RangePolygon | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ATLAS §8.E] |
| DistributionSurface | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| Habitat Association | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| BotanicalSurvey | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ENCY §7.6.C] |
| RestorationPlanting | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ENCY §7.6.C] |
| SourceRole | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] |
| Redaction Receipt | CONFIRMED term / PROPOSED field realization | [DOM-FLORA] [ENCY §7.6] |

[Back to top ↑](#contents)

---

## 8. Object-family carry-forward

```mermaid
flowchart LR
    subgraph IDENTITY ["Identity"]
        PT["PlantTaxon"]
        FTC["FloraTaxon Crosswalk"]
    end

    subgraph EVIDENCE ["Evidence / Observations"]
        SR["SpecimenRecord"]
        FO["FloraOccurrence"]
        PO["PhenologyObservation"]
        BS["BotanicalSurvey"]
        IPR["InvasivePlantRecord"]
    end

    subgraph SPATIAL ["Spatial Derivatives"]
        RP["RangePolygon"]
        DS["DistributionSurface"]
        VC["VegetationCommunity"]
    end

    subgraph SENSITIVITY ["Sensitivity / Control"]
        RPR["RarePlantRecord"]
        RR["RedactionReceipt"]
    end

    subgraph PROJECT ["Project Records"]
        RPL["RestorationPlanting"]
    end

    subgraph LINK ["Cross-Lane Link"]
        HA["HabitatAssociation"]
    end

    PT --> SR
    PT --> FO
    PT --> RP
    PT --> DS
    PT --> RPR
    PT --> IPR
    FTC -.crosswalk.-> PT
    FO --> RP
    FO --> DS
    RPR -.redact.-> RR
    BS -.aggregates.-> FO
    PO -.season.-> FO
    HA -.references.-> VC
    RPL -.references.-> PT
```

> [!NOTE]
> **Diagram status: ILLUSTRATIVE.** Shape and edges reflect the relationships described in [DOM-FLORA] / [ATLAS §8.E] / [ENCY §7.6.C]. Cardinality, key fields, and exact relation semantics are PROPOSED until contract entries are authored.

**Identity rule (PROPOSED for all object families).** Deterministic basis: `source id + object role + temporal scope + normalized digest`. [ATLAS §8.E]

**Temporal handling (CONFIRMED).** Source, observed, valid, retrieval, release, and correction times stay distinct where material. [ATLAS §8.E]

[Back to top ↑](#contents)

---

## 9. Source-family carry-forward

| Source family | Source role | Rights / sensitivity | Freshness | Status |
|---|---|---|---|---|
| KDWP flora / listed-species context | authority / observation / context / model as descriptor declares | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| KDWP Ecological Review Tool / stewardship outputs | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| Kansas Biological Survey / KU herbarium surfaces | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| USFWS ECOS plant context | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| NatureServe Explorer / Explorer Pro | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| GBIF vascular-plant downloads | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| iDigBio specimen records | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| iNaturalist-derived observations | authority / observation / context / model | rights and current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage or cadence specific | [DOM-FLORA] [ATLAS §8.D] |
| USDA PLANTS county packages | authority / context (taxa list) | benign in isolation; **sensitivity-prone when joined** with GBIF / iNaturalist / heritage occurrence data | per-package cadence | [P20 KFM-IDX-ANA-004] [NI-5-15] |
| Remote-sensing vegetation indices | observation / model | rights vary by product | per-product cadence | [ENCY §7.6.B] |
| Restoration project records | authority / project record | rights and steward agreement required | per-project | [ENCY §7.6.C] |

> [!CAUTION]
> **Rights and current source terms across all flora source families are NEEDS VERIFICATION.** Every live ingest activation requires a current SourceDescriptor with rights, license/terms text or contact reference, sensitivity classification, and a steward sign-off. Activation before that is a doctrine violation.

[Back to top ↑](#contents)

---

## 10. Sensitivity-posture carry-forward

**CONFIRMED doctrine.** Rare, protected, culturally sensitive, and steward-reviewed flora default to **generalized, withheld, staged, or denied** public geometry. [DOM-FLORA] [ATLAS §8.I] [ENCY §20.5]

**Deny-by-default register entry (CONFIRMED).** [ENCY §20.5]

| Domain | Denied by default | Allowed only when |
|---|---|---|
| Flora | exact rare / protected / culturally sensitive plant locations | review + generalized/withheld geometry + Redaction Receipt |

**Cross-lane combinatorial sensitivity (CONFIRMED, [P20 KFM-IDX-ANA-004]).** A benign source can become sensitive in combination. USDA PLANTS county taxa lists are not sensitive in isolation, but joined with GBIF / iNaturalist / heritage occurrence data they can become a poaching map. PLANTS therefore inherits flora geoprivacy discipline whenever any such join occurs.

**Preserved next behavior.**

- Sensitivity policy lives under `policy/domains/flora/` (PROPOSED, [DIRRULES §12]).
- Geoprivacy transforms (generalize, withhold, jitter, suppress) are recorded as `RedactionReceipt` entries persisted with the originating EvidenceBundle.
- Negative fixtures MUST prove that exact-precision public requests for sensitive taxa are **denied**, and that generalized derivative requests succeed only with a transform receipt.
- AI surfaces (Focus Mode, Evidence Drawer) MUST explain redaction without leaking the withheld location.
- Cross-lane joins (Flora × Fauna pollinator / food-web; Flora × People-DNA-Land any private-person link) inherit the **stricter** of the two lanes' policies.

[Back to top ↑](#contents)

---

## 11. Pipeline-shape carry-forward

```mermaid
flowchart LR
    RAW["RAW<br/>(SourceDescriptor exists)"]
    WORK["WORK / QUARANTINE<br/>(validation + policy gate)"]
    PROCESSED["PROCESSED<br/>(EvidenceRef + ValidationReport<br/>+ digest closure)"]
    CATALOG["CATALOG / TRIPLET<br/>(EvidenceBundle + graph<br/>+ release candidate)"]
    PUBLISHED["PUBLISHED<br/>(ReleaseManifest + rollback<br/>+ correction path + review)"]

    WATCH["Watcher<br/>(emits candidates only)"]
    REDACT["RedactionReceipt<br/>(geoprivacy transform)"]

    RAW --> WORK --> PROCESSED --> CATALOG --> PUBLISHED
    WATCH -.candidate.-> WORK
    WORK -. sensitive .-> REDACT
    REDACT -.public-safe.-> PROCESSED

    classDef stage fill:#eef7ee,stroke:#2e8b57;
    classDef control fill:#fff4d6,stroke:#a08000;
    class RAW,WORK,PROCESSED,CATALOG,PUBLISHED stage;
    class WATCH,REDACT control;
```

| Stage | Handling | Gate | Status |
|---|---|---|---|
| RAW | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | SourceDescriptor exists. | PROPOSED |
| WORK / QUARANTINE | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures. | Validation and policy gate pass, or quarantine reason is recorded. | PROPOSED |
| PROCESSED | Emit validated normalized objects, receipts, and public-safe candidates. | EvidenceRef, ValidationReport, and digest closure exist. | PROPOSED |
| CATALOG / TRIPLET | Emit catalog records, EvidenceBundles, graph/triplet projections, and release candidates. | Catalog / proof closure passes. | PROPOSED |
| PUBLISHED | Serve released public-safe artifacts through governed APIs and manifests. | ReleaseManifest, correction path, rollback target, and review/policy state exist. | PROPOSED |

Source citations: [ATLAS §8.H] [DOM-FLORA] [ENCY] [DIRRULES §0, §3].

[Back to top ↑](#contents)

---

## 12. Map and viewing-product carry-forward

**PROPOSED domain viewing products.** [ATLAS §8.G] [DOM-FLORA]

- Public **generalized occurrence** layer (sensitivity-safe).
- Public **range / distribution** layer.
- **Vegetation community** layer.
- **Invasive plant** layer.
- **Phenology / condition** layer (time-aware).
- **Habitat association** summary.
- **Review candidate** view (restricted, steward-only).

**CONFIRMED cross-cutting viewing surfaces.** [ATLAS §8.G] [Whole-UI report §6 "KEEP AND EXTEND"]

- Evidence Drawer (every consequential claim is one hop from EvidenceBundle / EvidenceRef resolution).
- Time-aware state (viewport time, valid time, observed time, freshness).
- Trust badges per layer.
- Sensitivity-redacted view (explains redaction without leaking the withheld location).
- Correction / stale-state view.
- Governed Focus Mode (bounded synthesis only).

**Preserved next behavior.**

- Flora layer manifests under `data/published/layers/flora/` (PROPOSED, [DIRRULES §12]).
- Tile field allowlist validators per layer (forbidding sensitive geometry leak through unexpected fields).
- Layer manifests carry rollback target, source role(s), and EvidenceBundle reference.
- 3D / Cesium flora visualization DEFERRED per §5 until 2D evidence continuity is proven.

[Back to top ↑](#contents)

---

## 13. Cross-lane relations carry-forward

| This lane | Related lane | Relation type | Constraint |
|---|---|---|---|
| Flora | Habitat | habitat association and vegetation community context | CONFIRMED / PROPOSED — must preserve ownership, source role, sensitivity, and EvidenceBundle support |
| Flora | Fauna | pollinator, food-web, invasive, biodiversity context | CONFIRMED / PROPOSED — must preserve ownership, source role, sensitivity, and EvidenceBundle support; **stricter of the two lanes' policies applies** |
| Flora | Soil / Hydrology | substrate, wetland, riparian, drought context | CONFIRMED / PROPOSED — must preserve ownership, source role, sensitivity, and EvidenceBundle support |
| Flora | Hazards | fire, drought, flood, smoke, vegetation stress | CONFIRMED / PROPOSED — must preserve ownership, source role, sensitivity, and EvidenceBundle support; Hazards lane MUST NOT be used as emergency-alert authority [DOM-HAZ] |
| Flora | Agriculture | crop / vegetation index adjacency; conservation practice context | CONFIRMED / PROPOSED — must preserve ownership; PLANTS county packages are a flora-source surface, not an agriculture surface |
| Flora | People / Land | living-person, parcel, and consent context | CONFIRMED / PROPOSED — stricter people/DNA/land policy applies on any join; living-person fields never appear in public flora outputs |

Source citations: [ATLAS §8.F] [DOM-FLORA] [DOM-FAUNA] [DOM-HAB] [DOM-HAZ] [DOM-PEOPLE] [ENCY].

> [!TIP]
> **Cross-lane shared validators** (Flora × Habitat × Fauna join validators, vegetation-community + occurrence consistency checks) belong under `tools/validators/<topic>/` per [DIRRULES §12 "Cross-domain validators"], **not** under a single domain folder.

[Back to top ↑](#contents)

---

## 14. API, contract, schema-surface carry-forward

| Endpoint or artifact | DTO / schema | Outcomes | Status |
|---|---|---|---|
| Flora feature / detail resolver; route TBD | `FloraDecisionEnvelope` | `ANSWER / ABSTAIN / DENY / ERROR` | PROPOSED governed API surface; exact route UNKNOWN |
| Flora layer manifest resolver | `LayerManifest` / domain layer descriptor | `ANSWER / DENY / ERROR` | PROPOSED; public-safe release only |
| Flora Evidence Drawer payload | `EvidenceDrawerPayload` + EvidenceBundle projection | `ANSWER / ABSTAIN / DENY / ERROR` | PROPOSED; evidence and policy filtered |
| Flora Focus Mode answer | `Runtime Response Envelope` + `AIReceipt` | `ANSWER / ABSTAIN / DENY / ERROR` | PROPOSED; AI never root truth |
| Schema responsibility root | `schemas/contracts/v1/domains/flora/` | finite validator outcomes | PROPOSED; verify with Directory Rules and ADR-0001. [DIRRULES §7.4] |
| Contract responsibility root | `contracts/domains/flora/` | semantic Markdown only | PROPOSED. [DIRRULES §7.4, §13.1] |
| Policy responsibility root | `policy/domains/flora/` | admissibility / release decisions | PROPOSED. [DIRRULES §12] |

Source citations: [ATLAS §8.J] [DOM-FLORA] [DIRRULES §7, §12].

[Back to top ↑](#contents)

---

## 15. Governed-AI / Focus-Mode carry-forward

**CONFIRMED doctrine / PROPOSED implementation.** AI may summarize released Flora EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes. AI MUST `ABSTAIN` when evidence is insufficient, and MUST `DENY` where policy, rights, sensitivity, or release state blocks the request. [GAI] [ATLAS §8.L] [DOM-FLORA]

Preserved next behavior:

- Focus Mode for flora runs behind the governed API; no direct model call from browser.
- Finite outcomes (`ANSWER / ABSTAIN / DENY / ERROR`) rendered as typed states.
- Every AI answer about flora has an `AIReceipt` and reachable citations.
- AI MUST NOT publish exact rare-plant geometry, even by paraphrase.
- AI MUST NOT treat a join between PLANTS county packages and any occurrence source as routine; the join is sensitivity-prone and must route through review (see §18).
- `MockAdapter` first; production model adapter added only after MockAdapter tests and a security review pass. [Whole-UI report §12]

[Back to top ↑](#contents)

---

## 16. Validators, tests, fixtures carry-forward

| Test class | Example assertion | Default status |
|---|---|---|
| Schema test | Required fields and versions are present for every flora object family | PROPOSED |
| Contract test | Object meaning matches vocabulary and lifecycle role | PROPOSED |
| Source-role test | A flora source is not used outside its declared authority | PROPOSED |
| Evidence test | `EvidenceRef` resolves to `EvidenceBundle` or the answer abstains | PROPOSED |
| Policy test | Unknown rights or sensitivity deny release | PROPOSED |
| Taxonomy reconciliation test | `FloraTaxon Crosswalk` resolves the source's name to a stable PlantTaxon | PROPOSED |
| Sensitivity denial test | An exact-precision request for a sensitive taxon is denied | PROPOSED |
| Geoprivacy transform test | A generalized derivative ships only with a valid `RedactionReceipt` | PROPOSED |
| Catalog closure test | Catalog and proof closure pass; rollback target named | PROPOSED |
| Release test | Manifest has proof, correction, rollback | PROPOSED |
| UI trust test | Evidence Drawer shows state and negative outcomes for flora layers | PROPOSED |
| AI boundary test | `MockAdapter` cannot answer without admissible evidence | PROPOSED |
| No-live-network fixture | Fixture-first pipeline produces RAW → PUBLISHED without any live fetch | PROPOSED |

Source citations: [ATLAS §8.K] [DOM-FLORA] [UNIFIED §5.3 PROPOSED fixture rule].

**CONFIRMED fixture rule.** Every major flora object family should ship at least **one valid**, **one invalid**, **one denied**, **one abstention**, and **one rollback or correction** fixture. Sensitive lanes ship **public-safe transformed** fixtures rather than real exact rare-plant coordinates. [UNIFIED §5.3]

[Back to top ↑](#contents)

---

## 17. Publication / correction / rollback carry-forward

**CONFIRMED doctrine / PROPOSED implementation.** Flora publication requires `ReleaseManifest`, `EvidenceBundle`, validation / policy support, review state where required, correction path, stale-state rule, and rollback target. [ATLAS §8.M] [ENCY Appendix E] [DOM-FLORA]

**Defect class → posture (CONFIRMED, generic).** [UNIFIED]

| Defect class | Correction posture | Rollback posture |
|---|---|---|
| Rights defect | DENY public use; quarantine source / artifact | Withdraw affected artifacts |
| Sensitivity leak (rare-plant location, cultural sensitivity) | Redact / generalize and notify stewards | Immediate public disablement |
| Geometry defect | Rebuild derivative layer and evidence payload | Restore previous digest-pinned artifact |
| Temporal defect | Correct valid / source / retrieval / release time | Mark stale until rebuilt |
| Policy defect | Re-run policy and decision envelope | Disable route / layer if gate failed |
| AI answer defect | Invalidate `AIReceipt` and response envelope | Remove answer; preserve EvidenceBundle |
| Catalog defect | Re-emit catalog closure after proof repair | Restore previous catalog state |

**OPEN question (carried forward).** Rollback propagation surface across tiles, graphs, Focus Mode caches, and Story Nodes for flora layers remains UNKNOWN. [P20 KFM-IDX-REL-004 OPEN]

[Back to top ↑](#contents)

---

## 18. PLANTS watcher — operational expansion pressure

> [!IMPORTANT]
> **CONFIRMED expansion pressure.** Pass 20's most concrete near-term flora operational artifact is a **PLANTS taxa-drift watcher** modeled on the CDL drift pattern, with strict sensitivity handling. [P20 KFM-IDX-ANA-004] [P20 KFM-IDX-SRC-006] [NI-5-15]

**Normalized statement (CONFIRMED).** A USDA PLANTS county package becomes a list of taxa under a recorded taxonomy version, and drift is the set difference between successive packages. Additions and removals are drift candidates **only when**:

1. The taxonomy version is stable (so additions are real, not renames).
2. The intersection with state-listed and federally-listed conservation species is computed for sensitivity policy.
3. The result is wrapped as a `SourceIntakeRecord` candidate with `publication_state: WORK_CANDIDATE` and `promotion_required: true`.

**CONFIRMED sensitivity invariant.** Pass 19/20 explicitly warns: PLANTS becomes sensitive when joined with GBIF, iNaturalist, or heritage datasets — what is a benign county species list in isolation can become a poaching map in combination. PLANTS drift therefore inherits flora and fauna geoprivacy discipline: **deny-by-default for exact public occurrences of rare species**; generalize to county or larger; record the transform in a geoprivacy receipt; route through steward review for any output that intersects sensitive lists. [P20 KFM-IDX-ANA-004]

**CONFIRMED watcher invariant.** PLANTS watchers emit candidate records only; they do not publish layers, mutate canonical truth, or expose `RAW/WORK/QUARANTINE` payloads to public surfaces. Lifecycle: `RAW → WORK_CANDIDATE → (review) → PROCESSED → CATALOG → PUBLISHED`. [P20 KFM-IDX-REL-005] [NI-5-8] [DIRRULES §13.5]

**Preserved next behavior.**

- First slice is **no-network, fixture-first**, with a deliberately mutated PLANTS fixture for one Kansas county exercising candidate emission, an unchanged fixture exercising no-trigger, and a missing-attestation case exercising denial. [P20 EXP-001]
- Threshold values are POLICY choices and route through `policy/domains/flora/` review.
- Watcher outbox placement (e.g., `tools/ingest/plants_watch/`) is **PROPOSED** and needs [DIRRULES] review before adoption. [P20 EXP-001 risk note]
- Watcher output includes a markdown steward summary alongside the machine `DriftSummary`. [P20 KFM-IDX-UIX-003]
- Taxonomy-version drift is tracked **separately** from county-package drift, because taxa changes may reflect renames rather than real presence/absence shifts.

**OPEN questions (carried forward).**

- How should taxa changes intersect legal / conservation status lists from different agencies (KDWP vs USFWS vs NatureServe)?
- Which join patterns require fail-closed denial vs steward review vs generalized release?
- Which Kansas counties and which PLANTS package year should seed the first fixture?

[Back to top ↑](#contents)

---

## 19. File-home and placement notes

> [!NOTE]
> All paths below other than `directory-rules.md` are **PROPOSED / NEEDS VERIFICATION** and follow the lane pattern in [DIRRULES §12 Domain Placement Law]. Their **presence** in the live repo has not been checked in this session.

**Lane pattern for flora (PROPOSED placements derived from [DIRRULES §12]):**

```text
docs/domains/flora/                       # human-facing flora doctrine (this file lives here)
contracts/domains/flora/                  # object-family semantic Markdown
schemas/contracts/v1/domains/flora/       # canonical schema home (ADR-0001)
policy/domains/flora/                     # sensitivity, rights, release policy
tests/domains/flora/                      # contract, schema, source-role, sensitivity tests
fixtures/domains/flora/                   # valid / invalid / denied / abstention / rollback fixtures
packages/domains/flora/                   # shared flora-lane code (if any)
pipelines/domains/flora/                  # flora pipelines (RAW → PUBLISHED)
pipeline_specs/flora/                     # pipeline specifications
data/raw/flora/                           # immutable captures
data/work/flora/                          # normalization work
data/quarantine/flora/                    # held failures
data/processed/flora/                     # validated normalized objects
data/catalog/domain/flora/                # catalog records
data/published/layers/flora/              # public-safe layer manifests
data/registry/sources/flora/              # source descriptors per family
release/candidates/flora/                 # release candidates
docs/runbooks/flora/                      # operational runbooks (parallel to docs/runbooks/fauna/)
```

<details>
<summary><b>Drift / placement open issues to track</b></summary>

| Issue | Status | Suggested resolution |
|---|---|---|
| `docs/runbooks/<domain>/` subfolder convention vs flat `docs/runbooks/<DOMAIN>_*.md` prefix convention | CONFLICTED | Mirror the fauna decision; raise ADR or `DRIFT_REGISTER.md` row if repo diverges |
| PLANTS watcher outbox path (`tools/ingest/plants_watch/` vs `pipelines/domains/flora/watchers/`) | UNKNOWN | Per [P20 EXP-001 risk note], PROPOSED; resolve via Directory Rules review and ADR before live activation |
| Whether `RestorationPlanting` contracts live under `contracts/domains/flora/` or under a cross-lane stewardship root | PROPOSED | Decide via ADR; default home is flora lane |
| `RedactionReceipt` shared vs flora-specific home | PROPOSED | Receipt **shape** is likely shared (`contracts/shared/redaction_receipt.md`); flora-specific transform catalog under `policy/domains/flora/` |
| Cross-lane Flora × Fauna pollinator-join validators | PROPOSED | `tools/validators/biodiversity/` (cross-domain), not under a single lane, per [DIRRULES §12] |

</details>

[Back to top ↑](#contents)

---

## 20. Flora-specific verification backlog

These items belong on `docs/registers/VERIFICATION_BACKLOG.md` (PROPOSED). They cannot be resolved without mounted-repo or live-source evidence.

| Item to verify | Evidence that would settle it | Status |
|---|---|---|
| Verify source endpoints and rights for every listed flora source family. | mounted repo files, registry entries, rights documents, source descriptors | NEEDS VERIFICATION |
| Verify rare-plant steward policy and review queue. | mounted repo `policy/domains/flora/`, steward agreements | NEEDS VERIFICATION |
| Verify exact / public geometry thresholds (when sensitive locations may be generalized vs withheld vs denied). | policy fixtures, sensitivity registry | NEEDS VERIFICATION |
| Verify Focus Mode and Evidence Drawer behavior for flora payloads. | mounted UI shell, mock fixtures, governed-API client | NEEDS VERIFICATION |
| Verify taxonomy resolution implementation (KU herbarium ↔ GBIF ↔ iNaturalist ↔ USDA PLANTS crosswalks). | mounted resolver, fixtures, tests | NEEDS VERIFICATION |
| Verify public layer safety and AI no-leak behavior under adversarial prompts. | red-team fixtures, AIReceipt validators | NEEDS VERIFICATION |
| Verify PLANTS watcher outbox placement and lifecycle. | mounted `tools/` or `pipelines/`, fixture run, candidate emissions | NEEDS VERIFICATION |
| Verify cross-lane Flora × Fauna pollinator-join policy. | mounted policy, shared validators, join fixtures | NEEDS VERIFICATION |
| Verify rollback propagation across flora tiles, graph projections, Focus Mode caches. | rollback drill, propagation receipts | UNKNOWN (corpus-level OPEN) |
| Verify whether `docs/runbooks/flora/` subfolder or `docs/runbooks/FLORA_*.md` flat-prefix is used. | mounted repo `docs/runbooks/` listing | NEEDS VERIFICATION |

Source citations: [ATLAS §8.N] [DOM-FLORA] [P20 KFM-IDX-REL-004 OPEN] [P20 EXP-001 risk note].

[Back to top ↑](#contents)

---

## 21. Update-propagation matrix

When a flora-relevant claim in this inventory changes, the following docs / artifacts SHOULD update in the same PR or a referenced follow-up.

| Material change | Owning README / doc | Object map / contract | Fixtures / tests | Runbooks | Continuity notes | Rollback notes | Verification backlog |
|---|---|---|---|---|---|---|---|
| Flora mission or boundary | `docs/domains/flora/README.md` (PROPOSED) | `contracts/domains/flora/` (PROPOSED) | — | — | **this file** | — | Add row if scope shifts |
| New object family or rename | `docs/domains/flora/README.md` (PROPOSED) | `contracts/domains/flora/`; `control_plane/object_family_register.yaml` | `fixtures/domains/flora/` | — | **this file (§7, §8)** | `release/rollback_cards/` | Track resolver impact |
| New / changed source family or role | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (PROPOSED) | `data/registry/sources/flora/` | source-role fixtures | `docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md` (PROPOSED) | **this file (§9, §18)** | `release/rollback_cards/` | Verify rights, endpoint, cadence |
| Sensitivity / geoprivacy posture change | `policy/domains/flora/` (PROPOSED) | `contracts/domains/flora/redaction_receipt.md` (PROPOSED) | negative + denial fixtures | — | **this file (§10, §18)** | rollback drill | Track receipt schema impact |
| New geoprivacy transform type (generalize / withhold / jitter / suppress) | `policy/domains/flora/` (PROPOSED) | `contracts/domains/flora/` | transform fixtures | refresh runbook | **this file (§10)** | rollback path per transform | Verify residual-risk policy |
| New flora layer | `docs/domains/flora/README.md` | `data/published/layers/flora/` layer manifest | tile field allowlist tests | layer validation runbook | **this file (§12)** | layer rollback | Verify field allowlist |
| Cross-lane relation change (Habitat / Fauna / Hydrology / Hazards / Agriculture / People-Land) | both lane READMEs | shared `OBJECT_MAP.md` | join fixtures | — | **this file (§13)** | release rollback if published | Verify ownership preserved |
| AI behavior / Focus Mode for flora | `docs/architecture/governed-ai/README.md` | `contracts/runtime/` | focus fixtures | governed-AI runbooks | **this file (§15)** | governed-AI rollback | Verify citation validation |
| PLANTS watcher threshold change | `policy/domains/flora/` | `data/registry/sources/flora/usda_plants.yaml` (PROPOSED) | drift fixtures | `docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md` | **this file (§18)** | candidate rollback | Track replayability |
| File-home / placement change | `docs/adr/ADR-*.md` | `control_plane/document_registry.yaml` | — | — | **this file (§19)** | migration note | Verify repo convention |

[Back to top ↑](#contents)

---

## 22. Related docs

> [!NOTE]
> All `docs/` paths below other than `directory-rules.md` are **PROPOSED / NEEDS VERIFICATION**. They reflect the placement rules in [DIRRULES §12]; their **presence** in the live repo has not been checked in this session.

- `docs/doctrine/directory-rules.md` — **CONFIRMED** (viewed this session)
- `docs/domains/README.md` — domain lane index — PROPOSED
- `docs/domains/flora/README.md` — flora lane README — PROPOSED
- `docs/domains/flora/SENSITIVITY_POSTURE.md` — companion to §10 — PROPOSED
- `docs/domains/flora/SOURCE_ROLES.md` — companion to §9 — PROPOSED
- `docs/domains/fauna/CONTINUITY_INVENTORY.md` — **parallel lane continuity inventory** — PROPOSED
- `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` — fauna source-refresh runbook (lineage / pattern reference) — PROPOSED
- `docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md` — flora source-refresh runbook — PROPOSED
- `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` — source-descriptor standard — PROPOSED
- `docs/standards/PROV.md` — provenance standards profile — PROPOSED
- `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md`, `docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md` — PROPOSED
- `docs/archive/lineage/` — archive of dossiers, scaffold reports, and PDF-only outputs (including the Flora architecture blueprint PDF) — PROPOSED
- `docs/adr/ADR-0001-schema-home.md` — schema home — PROPOSED (referenced from [DIRRULES §7.4])

**Source-corpus tag legend** (used throughout this file):

| Tag | Resolves to |
|---|---|
| `[DOM-FLORA]` | `KFM_Flora_Architecture_PDF_Only_Implementation_Blueprint.pdf` (lineage) |
| `[ENCY]` | `kfm_encyclopedia.pdf` §7.6 Flora; §20.5 deny-by-default register; Appendix E (doctrine) |
| `[UNIFIED]` | `KFM_Unified_Implementation_Architecture_Build_Manual.pdf` §6.5 Flora; §5.3 fixture rule |
| `[ATLAS]` | `KFM_Domains_Culmination_Atlas_v1_1.pdf` §8 Flora |
| `[P18]` | Pass 18 idea-card baseline |
| `[P19]` | Pass 19 normalized atlas |
| `[P20]` | `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` |
| `[NI-5-15]` | `New Ideas 5-15-26.pdf` — CDL / PLANTS source-drift packet |
| `[NI-5-8]` | `New Ideas 5-8-26.pdf` — environmental probes / run-receipt packet |
| `[GAI]` | KFM governed-AI doctrine (Encyclopedia / Whole-UI report) |
| `[DIRRULES]` | `docs/doctrine/directory-rules.md` |
| `[Whole-UI report]` | `KFM_Whole_UI_Governed_AI_Expansion_Report.pdf` |
| `[DOM-FAUNA]` | Fauna architecture blueprint (cross-lane reference) |
| `[DOM-HAB]` | Habitat architecture blueprint (cross-lane reference) |
| `[DOM-HAZ]` | Hazards extended pro PDF-only blueprint (cross-lane reference) |
| `[DOM-PEOPLE]` | People DNA Land architecture blueprint (cross-lane reference) |

---

<sub>
<b>Last reviewed:</b> 2026-05-16 ·
<b>Version:</b> v1 (draft) ·
<b>Owner:</b> &lt;flora-domain-steward&gt; (PLACEHOLDER) ·
<a href="#flora-domain--continuity-inventory">Back to top ↑</a>
</sub>
