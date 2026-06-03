<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/flora-missing-or-planned-files
title: Flora — Missing or Planned Files Register
type: register
version: v1.1
status: draft
owners: <flora domain steward> · <docs steward>
created: 2026-05-16
updated: 2026-06-03
policy_label: public
related:
  - ai-build-operating-contract.md                 # CONFIRMED canonical operating contract (CONTRACT_VERSION 3.0.0)
  - directory-rules.md                             # CONFIRMED placement authority (§12 Domain Placement Law, §15 README contract)
  - docs/domains/flora/README.md                   # NEEDS VERIFICATION
  - docs/domains/flora/IDENTITY_MODEL.md           # companion identity charter (envelope + object-family decisions)
  - docs/domains/flora/MAP_UI_CONTRACTS.md         # companion map-binding contracts
  - docs/registers/VERIFICATION_BACKLOG.md         # NEEDS VERIFICATION
  - docs/registers/DRIFT_REGISTER.md               # CONFLICTED entries land here
  - docs/adr/ADR-0001-schema-home.md               # NEEDS VERIFICATION (acceptance)
tags: [kfm, domains, flora, register, planning, verification-backlog]
notes:
  # CONTRACT_VERSION pin: this register is doctrine-adjacent; it tracks ai-build-operating-contract.md v3.0.0.
  # All paths in this register are PROPOSED until verified against a mounted repository.
  # This register implements the Domain Placement Law (Directory Rules §12) for the Flora lane.
  # Schema leaf follows Directory Rules §12 (schemas/contracts/v1/domains/flora/); the Encyclopedia/Atlas crosswalk uses the bare flora/ form — CONFLICTED, see §10.
  # Rare-plant exact locations are T4 (Denied) deny-by-default per the Master Sensitivity / Rights Tier Reference (Atlas Ch. 24.5).
  # Finite-outcome envelope aligned to RuntimeResponseEnvelope; bespoke FloraDecisionEnvelope flagged CONFLICTED / migration-tracked.
[/KFM_META_BLOCK_V2] -->

# 🌿 Flora — Missing or Planned Files Register

> Per-lane inventory of files the Flora domain is expected to carry across the KFM
> responsibility-root pattern, with truth-labeled status for each. Implementation
> presence is **not** asserted by this document; this is a planning and verification
> backlog grounded in the Flora dossier and Directory Rules §12.

[![Status: Draft](https://img.shields.io/badge/status-draft-yellow)](#status)
[![Type: Register](https://img.shields.io/badge/type-register-blue)](#1-scope-and-intent)
[![Policy: Public](https://img.shields.io/badge/policy-public-green)](#8-sensitivity-controls-rare-plant-defaults)
[![Domain: Flora](https://img.shields.io/badge/domain-flora-2ea043)](README.md)
[![Implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-orange)](#4-lane-status-overview)
[![Sensitivity: T4 deny-by-default](https://img.shields.io/badge/sensitivity-T4%20deny--by--default-red)](#8-sensitivity-controls-rare-plant-defaults)
[![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-555)](#)
[![Last reviewed](https://img.shields.io/badge/last%20reviewed-2026--06--03-informational)](#document-footer)

| Status | Owners | Contract | Last updated |
|---|---|---|---|
| `draft` (v1.1) | `<flora domain steward>` · `<docs steward>` | `CONTRACT_VERSION = "3.0.0"` | 2026-06-03 |

---

## Quick jump

- [1. Scope and intent](#1-scope-and-intent)
- [2. How to read this register](#2-how-to-read-this-register)
- [3. Flora lane pattern](#3-flora-lane-pattern)
- [4. Lane status overview](#4-lane-status-overview)
- [5. Per-lane file inventory](#5-per-lane-file-inventory)
  - [5.1 `docs/domains/flora/`](#51-docsdomainsflora)
  - [5.2 `contracts/domains/flora/`](#52-contractsdomainsflora)
  - [5.3 `schemas/contracts/v1/domains/flora/`](#53-schemascontractsv1domainsflora)
  - [5.4 `policy/domains/flora/`](#54-policydomainsflora)
  - [5.5 `tests/domains/flora/`](#55-testsdomainsflora)
  - [5.6 `fixtures/domains/flora/`](#56-fixturesdomainsflora)
  - [5.7 `packages/domains/flora/`](#57-packagesdomainsflora)
  - [5.8 `pipelines/domains/flora/` and `pipeline_specs/flora/`](#58-pipelinesdomainsflora-and-pipeline_specsflora)
  - [5.9 `connectors/` — Flora source connectors](#59-connectors--flora-source-connectors)
  - [5.10 `data/` — lifecycle lanes for Flora](#510-data--lifecycle-lanes-for-flora)
  - [5.11 `release/candidates/flora/`](#511-releasecandidatesflora)
  - [5.12 `control_plane/` — Flora register entries](#512-control_plane--flora-register-entries)
- [6. Per-object-family artifact checklist](#6-per-object-family-artifact-checklist)
- [7. Validators, tests, and fixtures backlog](#7-validators-tests-and-fixtures-backlog)
- [8. Sensitivity controls (rare-plant defaults)](#8-sensitivity-controls-rare-plant-defaults)
- [9. Cross-lane handoffs](#9-cross-lane-handoffs)
- [10. Open questions and NEEDS VERIFICATION](#10-open-questions-and-needs-verification)
- [11. Changelog](#11-changelog)
- [12. Definition of done](#12-definition-of-done)
- [13. Related docs](#13-related-docs)

---

## 1. Scope and intent

This register enumerates the **files the Flora domain is expected to carry** across the
KFM responsibility-root pattern, together with each file's planning status. It is the
domain-level companion to `docs/registers/VERIFICATION_BACKLOG.md` and the per-domain
landing page at `docs/domains/flora/README.md` (PROPOSED).

> [!IMPORTANT]
> **This document does not assert that any file exists.** No mounted KFM repository
> is visible in the session that produced this register. Every "expected" path below
> is **PROPOSED** under Directory Rules §12 Domain Placement Law and remains
> **NEEDS VERIFICATION** until a `git ls-tree`-equivalent inspection confirms it.
> No file or schema or policy or test is described as present, enforced, integrated,
> or covered.

**This register covers:**

- Files expected under each responsibility root for the Flora domain.
- Owned object families (`PlantTaxon`, `FloraTaxon Crosswalk`, `SpecimenRecord`,
  `FloraOccurrence`, `RarePlantRecord`, `VegetationCommunity`, `InvasivePlantRecord`,
  `PhenologyObservation`, `RangePolygon`, `HabitatAssociation`, `BotanicalSurvey`,
  `RestorationPlanting`, `RedactionReceipt`) and the artifacts each implies.
- Validator, fixture, and policy-test backlog drawn from the Flora dossier.
- Sensitivity defaults and deny-by-default surfaces.

**This register does NOT cover:**

- Field-level shape of contracts or schemas — see `contracts/domains/flora/` (PROPOSED)
  and `schemas/contracts/v1/domains/flora/` (PROPOSED) once present.
- Object meaning — see the Flora dossier and `docs/domains/flora/README.md` (PROPOSED).
- Live source endpoints or rights determinations — see
  `data/registry/sources/flora/` (PROPOSED) and the Source Authority Register.
- Release decisions — those live under `release/candidates/flora/` (PROPOSED) and
  `release/manifests/` once an approved candidate exists.

[Back to top](#quick-jump)

---

## 2. How to read this register

Each row in the per-lane tables below carries a **status** drawn from the KFM truth
labels:

| Label | Meaning in this register |
|---|---|
| **CONFIRMED** | Verified in this session from attached project docs (doctrine only). No file presence is ever CONFIRMED here without a mounted repository. |
| **PROPOSED** | Path placement derived from Directory Rules §12 and the Flora dossier. Not verified in implementation. |
| **NEEDS VERIFICATION** | Checkable against a mounted repo; not yet checked in this session. |
| **CONFLICTED** | Two governing sources disagree (e.g., Directory Rules vs the Encyclopedia/Atlas crosswalk on a path form). Routed to `docs/registers/DRIFT_REGISTER.md`. |
| **UNKNOWN** | Cannot be resolved without more evidence (e.g., live source rights, current implementation maturity). |
| **DENY (by default)** | Sensitive surface (T4) — explicit governed approval required before any artifact lands. |

> [!NOTE]
> Placeholders such as `<flora domain steward>` are deliberate. The register
> prefers a clearly reviewable placeholder over a fabricated owner, badge target,
> CI URL, or ADR reference.

[Back to top](#quick-jump)

---

## 3. Flora lane pattern

Per Directory Rules §12, the Flora domain must appear as a **segment** under each
applicable responsibility root, never as a root folder. The lane pattern below is
PROPOSED for Flora and mirrors the canonical pattern shared by all KFM domains
(Directory Rules §12 lists the segment forms verbatim).

```mermaid
flowchart LR
  subgraph DOC["docs/ — human-facing"]
    DDF["docs/domains/flora/<br/>(this register lives here)"]
  end

  subgraph MEANING["contracts/ + schemas/ — meaning + shape"]
    CDF["contracts/domains/flora/"]
    SDF["schemas/contracts/v1/<br/>domains/flora/"]
  end

  subgraph GATE["policy/ + tests/ + fixtures/ — admissibility"]
    PDF["policy/domains/flora/"]
    TDF["tests/domains/flora/"]
    FDF["fixtures/domains/flora/"]
  end

  subgraph CODE["packages/ + pipelines/ — code"]
    KDF["packages/domains/flora/"]
    PLF["pipelines/domains/flora/"]
    PSF["pipeline_specs/flora/"]
  end

  subgraph INGEST["connectors/ — source-specific fetch"]
    CON["connectors/&lt;vendor&gt;/&lt;source&gt;/<br/>(gbif, inaturalist, kansas, …)"]
  end

  subgraph LIFE["data/ — lifecycle lanes for Flora"]
    RAW["data/raw/flora/"]
    WORK["data/work/flora/"]
    QUAR["data/quarantine/flora/"]
    PROC["data/processed/flora/"]
    CAT["data/catalog/domain/flora/"]
    PUB["data/published/layers/flora/"]
    REG["data/registry/sources/flora/"]
  end

  subgraph REL["release/ — release decisions"]
    RCF["release/candidates/flora/"]
  end

  CON --> RAW
  RAW --> WORK
  WORK --> QUAR
  WORK --> PROC
  PROC --> CAT
  CAT --> RCF
  RCF -->|"governed promotion"| PUB

  MEANING -.-> GATE
  GATE -.-> CODE
  CODE -.-> LIFE
  REG -.-> RAW

  classDef proposed fill:#fff4e6,stroke:#c97800,color:#444
  classDef deny fill:#ffe5e5,stroke:#b30000,color:#444
  class DDF,CDF,SDF,PDF,TDF,FDF,KDF,PLF,PSF,CON,RAW,WORK,QUAR,PROC,CAT,REG,RCF proposed
  class PUB deny
```

> [!WARNING]
> The diagram is **structural**, not an assertion of current implementation. Arrows
> represent governed lifecycle transitions; no transition is automated, scheduled,
> or guaranteed without a verified pipeline and policy gate. Connectors output **only**
> to `data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/...` and MUST NOT
> publish (Directory Rules §7.3).

[Back to top](#quick-jump)

---

## 4. Lane status overview

| Lane | Expected segment | Implementation status | Sensitivity posture |
|---|---|---|---|
| Docs | `docs/domains/flora/` | PROPOSED / NEEDS VERIFICATION | public |
| Contracts (meaning) | `contracts/domains/flora/` | PROPOSED / NEEDS VERIFICATION | public |
| Schemas (shape) | `schemas/contracts/v1/domains/flora/` | PROPOSED / NEEDS VERIFICATION; ADR-0001 governs home; **CONFLICTED** leaf form (see §10) | public |
| Policy (admissibility) | `policy/domains/flora/` | PROPOSED / NEEDS VERIFICATION | deny-by-default for sensitive geometry |
| Tests | `tests/domains/flora/` | PROPOSED / NEEDS VERIFICATION | n/a (test code) |
| Fixtures | `fixtures/domains/flora/` | PROPOSED / NEEDS VERIFICATION; no-network only | synthetic, no live PII |
| Packages | `packages/domains/flora/` | PROPOSED / NEEDS VERIFICATION | n/a (library code) |
| Pipelines (exec) | `pipelines/domains/flora/` | PROPOSED / NEEDS VERIFICATION | watcher-as-non-publisher |
| Pipeline specs | `pipeline_specs/flora/` | PROPOSED / NEEDS VERIFICATION | declarative only |
| Connectors | `connectors/<vendor>/<source>/` (per source) | PROPOSED / NEEDS VERIFICATION; rights TODO per source | source-rights gated; output to `data/raw`/`quarantine` only |
| Data — raw | `data/raw/flora/` | PROPOSED / NEEDS VERIFICATION | internal; never public |
| Data — work / quarantine | `data/work/flora/`, `data/quarantine/flora/` | PROPOSED / NEEDS VERIFICATION | internal; never public |
| Data — processed | `data/processed/flora/` | PROPOSED / NEEDS VERIFICATION | review-gated |
| Data — catalog | `data/catalog/domain/flora/` | PROPOSED / NEEDS VERIFICATION | review-gated |
| Data — published | `data/published/layers/flora/` | PROPOSED / NEEDS VERIFICATION | public-safe derivatives only |
| Data — registry | `data/registry/sources/flora/` | PROPOSED / NEEDS VERIFICATION | source-rights gated |
| Release candidates | `release/candidates/flora/` | PROPOSED / NEEDS VERIFICATION | governed promotion only |
| Control-plane entries | `control_plane/*.yaml` | PROPOSED / NEEDS VERIFICATION | machine-readable registry |

[Back to top](#quick-jump)

---

## 5. Per-lane file inventory

Each subsection below lists the **expected** files in that lane. Every path is
PROPOSED unless a mounted repo verifies otherwise. The "Driver" column references
the doctrinal source or invariant that calls for the file.

### 5.1 `docs/domains/flora/`

Human-facing landing and supporting documentation for the Flora bounded context.

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `docs/domains/flora/README.md` | Domain landing page; bounded-context purpose, scope, non-ownership, terminology. | PROPOSED / NEEDS VERIFICATION | Atlas §8.A–C; Encyclopedia §7.6 |
| `docs/domains/flora/MISSING_OR_PLANNED_FILES.md` | **This document.** | PROPOSED (draft v1.1) | Domain Placement Law (Directory Rules §12) |
| `docs/domains/flora/IDENTITY_MODEL.md` | Deterministic identity charter (spec_hash, temporal facets, authority anchors). | PROPOSED / NEEDS VERIFICATION | Atlas §8.E; C1-02 |
| `docs/domains/flora/MAP_UI_CONTRACTS.md` | Map-surface binding (LayerManifest, Evidence Drawer, Focus Mode). | PROPOSED / NEEDS VERIFICATION | Atlas §8.G/J; MAP-MASTER |
| `docs/domains/flora/SOURCE_REFRESH_RUNBOOK.md` | Per-source admission / refresh / quarantine procedure for Flora connectors. | PROPOSED / NEEDS VERIFICATION | mirrors Fauna runbook precedent |
| `docs/domains/flora/SENSITIVITY_POSTURE.md` | Rare-plant generalization / withholding / `RedactionReceipt` rules. | PROPOSED / NEEDS VERIFICATION | Atlas Ch. 24.5; §8.I |
| `docs/domains/flora/OBJECT_FAMILIES.md` | Per-object family reference: identity, temporal handling, evidence rules. | PROPOSED / NEEDS VERIFICATION | Atlas §8.C, §8.E |
| `docs/domains/flora/CROSSWALKS.md` | `FloraTaxon Crosswalk` and external-taxonomy reconciliation (ITIS, GBIF, WFO, USDA PLANTS, NatureServe). | PROPOSED / NEEDS VERIFICATION | Encyclopedia §7.6.C; Atlas §8.C; C7.c |
| `docs/domains/flora/PUBLICATION_AND_ROLLBACK.md` | Publication gate, correction path, rollback target rules for Flora. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |

### 5.2 `contracts/domains/flora/`

Semantic (Markdown) definitions of Flora object families. Field-level shape lives in
`schemas/`, not here, per the canonical split (Directory Rules §6.3 / §6.4).

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `contracts/domains/flora/README.md` | Per-root README declaring class and contents. | PROPOSED / NEEDS VERIFICATION | Required README contract (Directory Rules §15) |
| `contracts/domains/flora/plant_taxon.md` | `PlantTaxon` meaning, invariants, identity basis. | PROPOSED / NEEDS VERIFICATION | Atlas §8.C, §8.E |
| `contracts/domains/flora/flora_taxon_crosswalk.md` | `FloraTaxon Crosswalk` between external taxonomies. | PROPOSED / NEEDS VERIFICATION | Atlas §8.C |
| `contracts/domains/flora/specimen_record.md` | `SpecimenRecord` meaning (herbarium / collection origin). | PROPOSED / NEEDS VERIFICATION | Atlas §8.B–C |
| `contracts/domains/flora/flora_occurrence.md` | `FloraOccurrence` meaning (point observation with uncertainty / geoprivacy). | PROPOSED / NEEDS VERIFICATION | Atlas §8.B–C |
| `contracts/domains/flora/rare_plant_record.md` | `RarePlantRecord` — sensitive-by-default object (T4). | PROPOSED / NEEDS VERIFICATION | Atlas §8.I; Ch. 24.5 |
| `contracts/domains/flora/vegetation_community.md` | `VegetationCommunity` polygons / classification. | PROPOSED / NEEDS VERIFICATION | Atlas §8.B–C |
| `contracts/domains/flora/invasive_plant_record.md` | `InvasivePlantRecord`. | PROPOSED / NEEDS VERIFICATION | Atlas §8.B–C |
| `contracts/domains/flora/phenology_observation.md` | `PhenologyObservation` / time-series semantics. | PROPOSED / NEEDS VERIFICATION | Atlas §8.B–C |
| `contracts/domains/flora/range_polygon.md` | `RangePolygon` (canonical Flora range family; a prior draft also named a separate `DistributionSurface` — folded here). | PROPOSED / NEEDS VERIFICATION | Atlas §8.C, §8.E |
| `contracts/domains/flora/habitat_association.md` | `HabitatAssociation` (relation to Habitat lane). | PROPOSED / NEEDS VERIFICATION | Atlas §8.C, §8.F |
| `contracts/domains/flora/botanical_survey.md` | `BotanicalSurvey` object. | PROPOSED / NEEDS VERIFICATION | Atlas §8.B |
| `contracts/domains/flora/restoration_planting.md` | `RestorationPlanting` object. | PROPOSED / NEEDS VERIFICATION | Atlas §8.B |
| `contracts/domains/flora/redaction_receipt.md` | Domain-flavored `RedactionReceipt` (shared-kernel reference). | PROPOSED / NEEDS VERIFICATION | Atlas §8.C; shared kernel |

> [!NOTE]
> `contracts/` retains semantic Markdown only. Per **ADR-0001** (and Directory Rules
> §6.4 / §13.1), machine-checkable JSON Schemas live under `schemas/contracts/v1/...`
> and never alongside the Markdown contracts. Any pre-existing
> `contracts/domains/flora/*.schema.json` is a drift candidate (§13.1).

### 5.3 `schemas/contracts/v1/domains/flora/`

Machine-checkable JSON Schemas. Home per **ADR-0001** and Directory Rules §12
(`schemas/contracts/v1/domains/<domain>/`). NEEDS VERIFICATION that the ADR is
accepted in the current repo.

> [!CAUTION]
> **CONFLICTED leaf form.** Directory Rules §12 specifies `schemas/contracts/v1/domains/flora/`
> (used here). The KFM Encyclopedia §7.6 / Atlas Ch. 24.13 crosswalk uses the **bare**
> form `schemas/contracts/v1/flora/`, and the companion Flora Identity Model and Map UI
> Contracts docs followed that bare form. Per Directory Rules §2.1 authority order,
> **Directory Rules wins on path questions**, so this register uses `domains/flora/`.
> The divergence is logged for a one-line reconciliation (see [§10](#10-open-questions-and-needs-verification) and the Drift Register).

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `schemas/contracts/v1/domains/flora/README.md` | Per-root README, class declaration. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `schemas/contracts/v1/domains/flora/plant_taxon.schema.json` | JSON Schema for `PlantTaxon`. | PROPOSED / NEEDS VERIFICATION | ADR-0001; Atlas §8.J |
| `schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json` | Crosswalk schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/specimen_record.schema.json` | Specimen schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/flora_occurrence.schema.json` | Public-vs-restricted occurrence shape. | PROPOSED / NEEDS VERIFICATION | ADR-0001; Atlas §8.I |
| `schemas/contracts/v1/domains/flora/rare_plant_record.schema.json` | Sensitive-by-default schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001; Ch. 24.5 |
| `schemas/contracts/v1/domains/flora/vegetation_community.schema.json` | Community polygon schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json` | Invasive observation schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/phenology_observation.schema.json` | Phenology time-series schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/range_polygon.schema.json` | Range schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/habitat_association.schema.json` | Cross-lane relation schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/botanical_survey.schema.json` | Survey schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/contracts/v1/domains/flora/restoration_planting.schema.json` | Restoration planting schema. | PROPOSED / NEEDS VERIFICATION | ADR-0001 |
| `schemas/tests/valid/domains/flora/*.json` | Golden valid fixtures per object family. | PROPOSED / NEEDS VERIFICATION | Directory Rules §6.4 |
| `schemas/tests/invalid/domains/flora/*.json` | Negative fixtures per object family. | PROPOSED / NEEDS VERIFICATION | Directory Rules §6.4 |

> [!WARNING]
> **No `flora_decision_envelope.schema.json` here.** The finite-outcome envelope is the
> **cross-cutting** `RuntimeResponseEnvelope` (schema home `schemas/contracts/v1/runtime/`,
> CONFIRMED per Directory Rules glossary), not a Flora-domain-local schema. The Atlas
> §8.J names a bespoke `FloraDecisionEnvelope`; that is **CONFLICTED / migration-tracked**
> (`DecisionEnvelope → RuntimeResponseEnvelope`). A Flora-local envelope schema in this
> lane would be a Domain Placement Law (§12) violation. See [§10](#10-open-questions-and-needs-verification).

### 5.4 `policy/domains/flora/`

Admissibility, sensitivity, rights, and release policy specific to Flora.

> [!NOTE]
> **Two policy homes to reconcile.** Directory Rules §12 gives the per-domain policy
> lane as `policy/domains/flora/` (used here). The Encyclopedia §7.6 / Atlas Ch. 24.13
> crosswalk also names `policy/sensitivity/flora/` (a sensitivity-specific home).
> Both are CONFIRMED in their respective sources; whether the Flora sensitivity rules
> live under `policy/domains/flora/sensitivity.rego` or `policy/sensitivity/flora/`
> is a reconciliation item (see [§10](#10-open-questions-and-needs-verification)).

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `policy/domains/flora/README.md` | Per-root README. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `policy/domains/flora/sensitivity.rego` | Rare/protected/culturally-sensitive deny rules (T4 default). | PROPOSED / NEEDS VERIFICATION | Atlas §8.I; Ch. 24.5 |
| `policy/domains/flora/rights.rego` | Source-role and license enforcement for Flora connectors. | PROPOSED / NEEDS VERIFICATION | Atlas §8.D |
| `policy/domains/flora/redaction.rego` | Geoprivacy / generalization / withholding decisions; emits `RedactionReceipt`. | PROPOSED / NEEDS VERIFICATION | Atlas §8.I, §8.C |
| `policy/domains/flora/promotion.rego` | Per-domain promotion-gate composition. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M; Encyclopedia §12 |
| `policy/domains/flora/citation.rego` | Cite-or-abstain enforcement for Flora Focus Mode answers. | PROPOSED / NEEDS VERIFICATION | Atlas §8.L; [GAI] |
| `policy/domains/flora/source_role.rego` | Authority / observation / context / model role discipline. | PROPOSED / NEEDS VERIFICATION | Atlas §8.D |
| `policy/domains/flora/fixtures/` | Policy fixtures distinct from `tests/fixtures/`. | PROPOSED / NEEDS VERIFICATION | Directory Rules §6.5 |
| `policy/domains/flora/tests/` | Policy unit tests. | PROPOSED / NEEDS VERIFICATION | Directory Rules §6.5 |

> [!CAUTION]
> Exact locations of rare, protected, or culturally sensitive flora are **T4 — DENY by
> default** (Atlas Ch. 24.5). Any policy change loosening this default requires steward
> review **and** a `RedactionReceipt` path — see [§8](#8-sensitivity-controls-rare-plant-defaults).

### 5.5 `tests/domains/flora/`

Proof that Flora rules are enforceable. Tests must be no-network and fixture-backed.

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `tests/domains/flora/README.md` | Per-root README; lists validators covered. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `tests/domains/flora/test_schema_validation.py` (or equivalent) | All Flora object-family schemas accept valid / reject invalid fixtures. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `tests/domains/flora/test_taxonomy_reconciliation.py` | `FloraTaxon Crosswalk` closure / non-collision tests. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K (taxonomy reconciliation) |
| `tests/domains/flora/test_rights_validators.py` | Source-rights and source-role gates. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K (rights/sensitivity validators) |
| `tests/domains/flora/test_sensitivity_denial.py` | Exact sensitive public-geometry DENY. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `tests/domains/flora/test_redaction_receipts.py` | `RedactionReceipt` lineage / closure. | PROPOSED / NEEDS VERIFICATION | Atlas §8.C, §8.I |
| `tests/domains/flora/test_catalog_closure.py` | Catalog / `EvidenceBundle` closure for Flora records. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K (catalog closure tests) |
| `tests/domains/flora/test_api_envelopes.py` | API finite-outcome (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`) fixtures via `RuntimeResponseEnvelope`. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K (API finite-outcome fixtures) |
| `tests/domains/flora/test_no_live_network.py` | Assert the Flora test corpus runs without live-network calls. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K (no-live-network fixture pipeline) |
| `tests/domains/flora/test_temporal_logic.py` | source / observed / valid / retrieval / release / correction time distinctions. | PROPOSED / NEEDS VERIFICATION | Atlas §8.E |
| `tests/domains/flora/test_geometry_validity.py` | Geometry validity + generalization invariants. | PROPOSED / NEEDS VERIFICATION | Encyclopedia §7.6.K |
| `tests/domains/flora/test_release_manifest.py` | `ReleaseManifest` validation and rollback chain. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |

### 5.6 `fixtures/domains/flora/`

Golden, valid, and invalid sample data backing Flora tests. **No live data, no live
network.**

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `fixtures/domains/flora/README.md` | Per-root README. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `fixtures/domains/flora/source_descriptors/` | One `SourceDescriptor` per Flora source family. | PROPOSED / NEEDS VERIFICATION | Encyclopedia §7.6.L; Atlas §8.D |
| `fixtures/domains/flora/plant_taxon/` | Valid / invalid taxon fixtures. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `fixtures/domains/flora/flora_occurrence/` | Public-safe and sensitive occurrence fixtures (sensitive ones must never publish). | PROPOSED / NEEDS VERIFICATION | Atlas §8.K; Ch. 24.5 |
| `fixtures/domains/flora/rare_plant_record/` | Synthetic rare-plant fixtures with generalized geometry; **no real rare-plant locations**. | PROPOSED / NEEDS VERIFICATION | Atlas Ch. 24.5 |
| `fixtures/domains/flora/vegetation_community/` | Community polygon fixtures. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `fixtures/domains/flora/invasive_plant_record/` | Invasive observation fixtures. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `fixtures/domains/flora/phenology_observation/` | Time-series fixtures. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `fixtures/domains/flora/evidence_bundles/` | `EvidenceBundle` fixtures for catalog closure. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `fixtures/domains/flora/runtime_envelopes/` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` fixtures (`RuntimeResponseEnvelope`). | PROPOSED / NEEDS VERIFICATION | Atlas §8.J |

> [!IMPORTANT]
> Rare-plant fixtures **must** use synthetic or generalized geometry. Real precise
> rare-plant locations must not be checked into the repo at any lifecycle phase —
> Atlas Ch. 24.5 / Flora §I.

### 5.7 `packages/domains/flora/`

Reusable library code specific to the Flora bounded context. One-off scripts belong
in `scripts/` until they earn library status (Directory Rules §7.5).

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `packages/domains/flora/README.md` | Per-root README. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `packages/domains/flora/taxonomy/` | `FloraTaxon` resolution / crosswalk reconciliation. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K; Encyclopedia §7.6 |
| `packages/domains/flora/geoprivacy/` | Generalization, withholding, `RedactionReceipt` emission helpers. | PROPOSED / NEEDS VERIFICATION | Atlas §8.I |
| `packages/domains/flora/normalizers/` | Per-source normalizers (GBIF DwC, iNaturalist, USDA PLANTS, NatureServe). | PROPOSED / NEEDS VERIFICATION | Encyclopedia §7.6.B |
| `packages/domains/flora/evidence/` | `EvidenceBundle` assemblers for Flora records. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |
| `packages/domains/flora/layer_manifests/` | `LayerManifest` builders for Flora public surfaces. | PROPOSED / NEEDS VERIFICATION | Atlas §8.J |

### 5.8 `pipelines/domains/flora/` and `pipeline_specs/flora/`

Executable pipeline logic (`pipelines/`) and its declarative spec (`pipeline_specs/`).
Split: `pipeline_specs/` says **what** should run; `pipelines/` says **how** (Directory Rules §7.4).

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `pipelines/domains/flora/README.md` | Per-root README. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `pipelines/domains/flora/ingest/` | Connector → RAW admission for Flora sources. | PROPOSED / NEEDS VERIFICATION | Directory Rules §7.3–§7.4 |
| `pipelines/domains/flora/normalize/` | RAW → WORK normalization. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H |
| `pipelines/domains/flora/validate/` | Schema / rights / sensitivity / geometry validation. | PROPOSED / NEEDS VERIFICATION | Atlas §8.K |
| `pipelines/domains/flora/catalog/` | PROCESSED → CATALOG and `EvidenceBundle` assembly. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H |
| `pipelines/domains/flora/redact/` | `RedactionReceipt` emission for sensitive records. | PROPOSED / NEEDS VERIFICATION | Atlas §8.I |
| `pipeline_specs/flora/README.md` | Declarative spec README. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `pipeline_specs/flora/*.yaml` | Per-source / per-product specs (one per Flora source family). | PROPOSED / NEEDS VERIFICATION | Directory Rules §7.4 |

### 5.9 `connectors/` — Flora source connectors

Source-specific fetchers and admitters, grouped by vendor (Directory Rules §7.3:
`connectors/<vendor>/`). Connector output MUST go to
`data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/...`; connectors **MUST
NOT** publish, mutate canonical truth, or write under `data/processed/`,
`data/catalog/`, or `data/published/` (§7.3).

| Source family (from Flora dossier) | Expected connector path | Status | Rights / sensitivity |
|---|---|---|---|
| KDWP flora / listed-species context | `connectors/kansas/kdwp_flora/` | PROPOSED / NEEDS VERIFICATION | rights TODO; sensitive joins fail closed |
| KDWP Ecological Review Tool / stewardship outputs | `connectors/kansas/kdwp_ert/` | PROPOSED / NEEDS VERIFICATION | rights TODO; stewardship gating |
| Kansas Biological Survey / KU herbarium (McGregor) | `connectors/kansas/kbs_herbarium/` | PROPOSED / NEEDS VERIFICATION | rights TODO; per-collection terms |
| USFWS ECOS (plant context) | `connectors/usfws/ecos_plants/` | PROPOSED / NEEDS VERIFICATION | public; verify terms |
| NatureServe Explorer / Explorer Pro | `connectors/natureserve/explorer/` | PROPOSED / NEEDS VERIFICATION | account / license required; sensitive |
| GBIF vascular-plant downloads | `connectors/gbif/plants/` | PROPOSED / NEEDS VERIFICATION | citation + DOI obligations (Backbone version pinned) |
| iDigBio specimen records | `connectors/idigbio/specimens/` | PROPOSED / NEEDS VERIFICATION | per-collection license |
| iNaturalist-derived observations | `connectors/inaturalist/observations/` | PROPOSED / NEEDS VERIFICATION | per-record license; obscured locations |
| USDA PLANTS (vascular checklists / distributions) | `connectors/usda/plants/` | PROPOSED / NEEDS VERIFICATION | public domain per source; cite per guidance |

> [!NOTE]
> The vendor-grouping shape (`connectors/<vendor>/<source>/`) matches the Directory Rules
> §7.3 connector tree (`usgs/`, `fema/`, `noaa/`, `nrcs/`, `kansas/`, `gbif/`,
> `inaturalist/`, `census/`, `local_upload/`). Whether a deeper per-domain segment is
> permitted under `connectors/` beyond the canonical roots is an OPEN doctrine item
> (OPEN-DSC-14). Concrete rights, current API surfaces, and per-source terms are
> **NEEDS VERIFICATION** and must be resolved before any connector is admitted.

### 5.10 `data/` — lifecycle lanes for Flora

Lifecycle directories under `data/`. The phase is the **governance invariant**; a
file's lifecycle phase MUST be explicit (Directory Rules §9.1).

```text
data/
├── raw/flora/<source_id>/<run_id>/
├── work/flora/<run_id>/
├── quarantine/flora/<reason>/<run_id>/
├── processed/flora/<dataset_id>/<version>/
├── catalog/domain/flora/
├── triplets/                # cross-domain; flora deltas live here, not in a flora/ root
├── published/layers/flora/
├── registry/sources/flora/
├── receipts/                # ingest/validation/pipeline/ai/release — cross-domain
├── proofs/                  # evidence_bundle/proof_pack/... — cross-domain
└── rollback/flora/<release_id>/
```

| Lane | Purpose | Status | Driver |
|---|---|---|---|
| `data/raw/flora/` | Immutable source payloads with `SourceDescriptor` + hash. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H (RAW) |
| `data/work/flora/` | Normalization scratch. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H (WORK) |
| `data/quarantine/flora/` | Records held on validation/policy failure with quarantine reason. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H (QUARANTINE) |
| `data/processed/flora/` | Validated, normalized objects + receipts. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H (PROCESSED) |
| `data/catalog/domain/flora/` | Catalog records + `EvidenceBundle`s + triplet projections. | PROPOSED / NEEDS VERIFICATION | Atlas §8.H (CATALOG) |
| `data/published/layers/flora/` | Public-safe released layers (generalized occurrence, vegetation community, phenology, etc.). | PROPOSED / NEEDS VERIFICATION | Atlas §8.G, §8.H (PUBLISHED) |
| `data/registry/sources/flora/` | Per-source registry entries (`SourceDescriptor` IDs, rights, freshness). | PROPOSED / NEEDS VERIFICATION | Directory Rules §9.1 |
| `data/rollback/flora/<release_id>/` | Rollback targets for prior Flora releases. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |

> [!WARNING]
> Public clients **MUST NOT** read directly from `data/raw/`, `data/work/`,
> `data/quarantine/`, `data/processed/`, or `data/catalog/`. All public reads go
> through the governed API (`apps/governed-api/` — PROPOSED). Direct reads of
> canonical stores by `apps/explorer-web/` or any other shell are a trust-membrane
> violation (Directory Rules §7.1 / §13).

### 5.11 `release/candidates/flora/`

Release decisions and candidates for Flora. Release **decisions** live here; released
**artifacts** live under `data/published/layers/flora/` — the two are deliberately
distinct (Directory Rules §9.2; mixing them is a §10 drift pattern).

| Expected path | Purpose | Status | Driver |
|---|---|---|---|
| `release/candidates/flora/README.md` | Per-root README. | PROPOSED / NEEDS VERIFICATION | Directory Rules §15 |
| `release/candidates/flora/<candidate_id>/manifest.yaml` | Candidate `ReleaseManifest`. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |
| `release/candidates/flora/<candidate_id>/evidence_bundle.json` | Evidence basis for the candidate. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |
| `release/candidates/flora/<candidate_id>/policy_decision.json` | Captured `PolicyDecision`. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |
| `release/candidates/flora/<candidate_id>/rollback_card.json` | Rollback target. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |
| `release/correction_notices/flora/` (shared root) | Public correction notices touching Flora releases. | PROPOSED / NEEDS VERIFICATION | Atlas §8.M |

### 5.12 `control_plane/` — Flora register entries

The control plane is the **machine-readable** "what governs what" layer; it indexes,
it does not store source data (Directory Rules §6.2). Flora entries appear in shared
registers, not in a Flora-specific subtree.

| Expected entry | Where | Status |
|---|---|---|
| Flora source families | `control_plane/source_authority_register.yaml` (Flora section) | PROPOSED / NEEDS VERIFICATION |
| Flora object families | `control_plane/object_family_register.yaml` (Flora section) | PROPOSED / NEEDS VERIFICATION |
| Flora domain lane definition | `control_plane/domain_lane_register.yaml` (Flora entry) | PROPOSED / NEEDS VERIFICATION |
| Flora policy gates | `control_plane/policy_gate_register.yaml` (Flora-tagged gates) | PROPOSED / NEEDS VERIFICATION |
| Flora release states | `control_plane/release_state_register.yaml` (Flora entries) | PROPOSED / NEEDS VERIFICATION |
| Flora verification backlog items | `control_plane/verification_backlog.yaml` (Flora-tagged) | PROPOSED / NEEDS VERIFICATION |

> [!NOTE]
> Register file names above are PROPOSED. The actual register filenames are NEEDS
> VERIFICATION; `control_plane/` is confirmed as the machine-readable governance root
> (Directory Rules §6.2).

[Back to top](#quick-jump)

---

## 6. Per-object-family artifact checklist

For each owned Flora object family, the lane pattern implies a consistent set of
artifacts. The matrix below is the per-object completeness check. No row is
CONFIRMED; every cell is PROPOSED / NEEDS VERIFICATION until a mounted repo
inspection lands.

<details>
<summary><strong>Object-family artifact matrix (click to expand)</strong></summary>

| Object family | Contract (`contracts/.../<name>.md`) | Schema (`schemas/.../<name>.schema.json`) | Valid fixture | Invalid fixture | Policy hooks | Normalizer | Catalog projection | Sensitivity default |
|---|---|---|---|---|---|---|---|---|
| `PlantTaxon` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, citation | PROPOSED | PROPOSED | public (T0) |
| `FloraTaxon Crosswalk` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, citation | PROPOSED | PROPOSED | public (T0) |
| `SpecimenRecord` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights | PROPOSED | PROPOSED | per-collection terms |
| `FloraOccurrence` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, sensitivity | PROPOSED | PROPOSED | generalize if uncertain |
| `RarePlantRecord` | PROPOSED | PROPOSED | PROPOSED (synthetic) | PROPOSED | sensitivity (T4 DENY default), redaction | PROPOSED | PROPOSED | **T4 — DENY by default** |
| `VegetationCommunity` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, citation | PROPOSED | PROPOSED | public (T0) |
| `InvasivePlantRecord` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, citation | PROPOSED | PROPOSED | public (T0–T2) |
| `PhenologyObservation` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, temporal | PROPOSED | PROPOSED | public (T0–T1) |
| `RangePolygon` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, sensitivity | PROPOSED | PROPOSED | generalized (T1) for rare taxa |
| `HabitatAssociation` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | cross-lane integrity | PROPOSED | PROPOSED | derived; strictest of inputs |
| `BotanicalSurvey` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, completeness | PROPOSED | PROPOSED | public (T0–T2) |
| `RestorationPlanting` | PROPOSED | PROPOSED | PROPOSED | PROPOSED | rights, sensitivity | PROPOSED | PROPOSED | per-project terms |
| `RedactionReceipt` | PROPOSED | PROPOSED (shared kernel) | PROPOSED | PROPOSED | emitted by `redact/` | n/a | PROPOSED | public (the receipt is public) |

</details>

[Back to top](#quick-jump)

---

## 7. Validators, tests, and fixtures backlog

The Flora dossier names the following PROPOSED validator and test surfaces.
Implementation presence is **NEEDS VERIFICATION** for every row.

| Validator / test | Surface | Status | Source |
|---|---|---|---|
| Taxonomy reconciliation tests | crosswalks; `FloraTaxon` resolution | PROPOSED | Atlas §8.K |
| Rights / sensitivity validators | source-rights, sensitivity tags | PROPOSED | Atlas §8.K |
| Exact-sensitive public-geometry denial | rare-plant T4 DENY | PROPOSED | Atlas §8.K; Ch. 24.5 |
| Catalog closure tests | `EvidenceBundle` / digest closure | PROPOSED | Atlas §8.K |
| API finite-outcome fixtures | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` (`RuntimeResponseEnvelope`) | PROPOSED | Atlas §8.K |
| No-live-network fixture pipeline | all Flora tests | PROPOSED | Atlas §8.K |
| Source-descriptor validation | per-source admission | PROPOSED | Encyclopedia §7.6.K |
| Temporal logic tests | source/observed/valid/retrieval/release/correction times | PROPOSED | Atlas §8.E |
| Geometry validity tests | OGC validity + generalization invariants | PROPOSED | Encyclopedia §7.6.K |
| Citation validation | cite-or-abstain enforcement | PROPOSED | Atlas §8.L; [GAI] |
| `ReleaseManifest` validation | promotion / rollback chain | PROPOSED | Atlas §8.M |
| Rollback drill | exercise rollback target | PROPOSED | Atlas §8.M |

[Back to top](#quick-jump)

---

## 8. Sensitivity controls (rare-plant defaults)

The Master Sensitivity / Rights Tier Reference (Atlas Ch. 24.5) places Flora rare,
protected, or culturally sensitive **exact** plant locations at **T4 (Denied)**. The
Flora dossier reinforces that "rare, protected, culturally sensitive, and
steward-reviewed flora default to generalized, withheld, staged, or denied public
geometry" (Atlas §8.I).

> [!NOTE]
> **Canonical five-tier register (Atlas Ch. 24.5.1).** `T0` Open · `T1` Generalized ·
> `T2` Reviewer · `T3` Restricted (named agreement) · **`T4` Denied**. The canonical
> Flora row: *rare or culturally sensitive plant location → **T4** → generalized
> geometry + steward review → `T2` or `T1` → `RedactionReceipt` + `ReviewRecord`.*
> Tier *upgrade* (toward public) needs a transform receipt **and** a review record;
> tier *downgrade* needs only a `CorrectionNotice` + `ReviewRecord` and precedes
> derivative invalidation.

> [!CAUTION]
> **Deny-by-default (T4) surfaces for Flora:**
>
> - Exact precise locations of rare or protected plant taxa.
> - Exact precise locations of culturally sensitive / ethnobotanical taxa (where steward
>   review identifies them).
> - Records joined to sensitive habitat, archaeology, or land assertions where the join
>   itself elevates exposure.
>
> Public release is permitted only with: explicit steward / cultural review, generalized
> or withheld geometry, an emitted `RedactionReceipt`, and an approved `ReleaseManifest`
> pointing at a public-safe derivative. (Atlas Ch. 24.5; operating contract §23.2.)

| Sensitive surface | Default tier | Public-safe path | Receipt required |
|---|---|---|---|
| `RarePlantRecord` (exact location) | T4 | Generalized `RangePolygon` / withheld geometry → T1 | `RedactionReceipt` + `ReviewRecord` |
| Sensitive collection joins (herbarium ↔ rare taxa) | T4 | Aggregated / generalized join surface → T1 | `RedactionReceipt` |
| Culturally sensitive / ethnobotanical taxa | T4 | Steward-reviewed surface only (T2/T3) | `RedactionReceipt` + `ReviewRecord` |
| iNaturalist-obscured locations | T1 | Use source-obscured geometry only | per-source citation |

[Back to top](#quick-jump)

---

## 9. Cross-lane handoffs

Flora is a bounded context. Cross-lane handoffs MUST preserve ownership, source
role, sensitivity, and `EvidenceBundle` support (Atlas §8.F).

| From | To | Relation | Files implicated |
|---|---|---|---|
| Flora | Habitat | `HabitatAssociation`; vegetation-community context | `contracts/domains/flora/habitat_association.md`; cross-domain validator in `tools/validators/<topic>/` (not in either domain's folder) |
| Flora | Fauna | Pollinator, food-web, invasive context | shared kernel; no flora-rooted fauna artifacts |
| Flora | Soil / Hydrology | Substrate, wetland, riparian, drought context | derived joins; cross-domain validator |
| Flora | Hazards | Fire, drought, flood, smoke, vegetation stress context | derived joins; cross-domain validator |
| Flora | People / Land | Ethnobotanical context; traditional plant knowledge | T4 deny-default; steward/sovereignty review required |

> [!NOTE]
> Per Directory Rules §12, cross-lane files belong under the **lowest common
> responsibility root** (e.g., `tools/validators/<topic>/`,
> `schemas/contracts/v1/<topic>/`), **not** under one domain's lane. Sensitivity of a
> cross-lane product is the **strictest** of the contributing tiers.

[Back to top](#quick-jump)

---

## 10. Open questions and NEEDS VERIFICATION

| ID | Item | Status | Resolution path |
|---|---|---|---|
| OQ-FLORA-MPF-01 | Does the mounted repo contain `docs/domains/flora/`, and which §5.1 files already exist? | NEEDS VERIFICATION | Mounted-repo inspection |
| OQ-FLORA-MPF-02 | Is ADR-0001 (canonical schema home `schemas/contracts/v1/...`) accepted in the current repo? | NEEDS VERIFICATION | Mounted ADR set |
| OQ-FLORA-MPF-03 | Schema leaf form: `schemas/contracts/v1/domains/flora/` (Directory Rules §12) vs `schemas/contracts/v1/flora/` (Encyclopedia/Atlas crosswalk) | **CONFLICTED** | One-line reconciliation; DRIFT_REGISTER entry; Directory Rules §2.1 favors `domains/flora/` |
| OQ-FLORA-MPF-04 | Policy home: `policy/domains/flora/` (§12) vs `policy/sensitivity/flora/` (crosswalk) | **CONFLICTED** | Reconciliation note; DRIFT_REGISTER |
| OQ-FLORA-MPF-05 | Reconcile bespoke `FloraDecisionEnvelope` to canonical `RuntimeResponseEnvelope` | **CONFLICTED** | `DecisionEnvelope → RuntimeResponseEnvelope` migration ADR |
| OQ-FLORA-MPF-06 | Are any `contracts/domains/flora/*.schema.json` files present (drift candidates per §13.1)? | NEEDS VERIFICATION | Mounted-repo inspection |
| OQ-FLORA-MPF-07 | Source rights, license terms, current API surfaces for KDWP, KU/KBS herbaria, USFWS ECOS, NatureServe, GBIF, iDigBio, iNaturalist, USDA PLANTS | NEEDS VERIFICATION | Source registry + per-source terms |
| OQ-FLORA-MPF-08 | Steward roles and approval authority for sensitive Flora promotions | NEEDS VERIFICATION | Atlas Ch. 24.7 separation-of-duties matrix; steward roster |
| OQ-FLORA-MPF-09 | Current state of `data/registry/sources/flora/` and the `SourceDescriptor` record form actually used | NEEDS VERIFICATION | Mounted-repo inspection |
| OQ-FLORA-MPF-10 | Pipeline-spec format (YAML / JSON / other) under `pipeline_specs/flora/` | NEEDS VERIFICATION | Pipeline framework conventions |
| OQ-FLORA-MPF-11 | Is `release/correction_notices/` per-domain or cross-domain in the current layout? | NEEDS VERIFICATION | Mounted-repo inspection |
| OQ-FLORA-MPF-12 | Connector path beyond the §7.3 canonical vendor roots (per-domain segment under `connectors/`?) | OPEN | OPEN-DSC-14 resolution |
| OQ-FLORA-MPF-13 | Flora's own `EVIDENCE_DRAWER.md` vs a shared `docs/architecture/evidence-drawer.md` | OPEN | Docs-steward decision |
| OQ-FLORA-MPF-14 | Subfolder conventions inside `docs/domains/flora/` (flat vs `runbooks/`, `references/`) | OPEN | Per-root README convention |
| OQ-FLORA-MPF-15 | Should `FloraTaxon Crosswalk` live under `contracts/domains/flora/` or a shared `contracts/crosswalks/taxonomy/`? | OPEN | Crosswalk-home ADR |

[Back to top](#quick-jump)

---

## 11. Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Pinned `CONTRACT_VERSION = "3.0.0"`; added contract + companion docs to `related`; added Contract badge/column | housekeeping | Doctrine-adjacent register; contract requires the pin |
| Surfaced the `domains/flora/` vs `flora/` schema-leaf divergence as CONFLICTED (Directory Rules §12 vs Encyclopedia/Atlas crosswalk); Directory Rules §2.1 favors `domains/flora/` | reconciliation | Real cross-doc inconsistency vs the companion Identity Model / Map UI Contracts docs |
| Flagged `policy/domains/flora/` vs `policy/sensitivity/flora/` divergence as CONFLICTED | reconciliation | §12 vs crosswalk both CONFIRMED in their sources |
| Aligned the finite-outcome envelope to `RuntimeResponseEnvelope`; removed `flora_decision_envelope.schema.json` from the Flora schema lane and flagged the bespoke `FloraDecisionEnvelope` as CONFLICTED / migration-tracked | reconciliation | Contract §8 + Directory Rules glossary make `RuntimeResponseEnvelope` canonical; a Flora-local envelope is a §12 violation |
| Aligned sensitivity vocabulary to the canonical five-tier `T0–T4` register; rare/cultural exact locations stated as `T4` (Denied) | clarification | Atlas Ch. 24.5.1 is CONFIRMED doctrine |
| Noted the `DistributionSurface` → `RangePolygon` consolidation | clarification | CONFIRMED atlas Flora object list names `RangePolygon` |
| Corrected `directory-rules.md` link from `docs/doctrine/directory-rules.md` to repo-root `directory-rules.md` | housekeeping | Mounted path is repo-root |
| Added connector-output-path note (`data/raw/<domain>/<source_id>/<run_id>/`) and OPEN-DSC-14 | gap closure | Directory Rules §7.3 |
| Promoted the tail to doctrine companion sections (Open Questions as a register, Changelog, Definition of done) | housekeeping | Contract companion-section pattern |

> **Backward compatibility.** Section anchors `#1`–`#9` are unchanged. The former free-form
> "Open questions and NEEDS VERIFICATION" (§10) is preserved as §10 but tabulated with IDs;
> former §11 "Related docs" moves to §13. Update inbound links to `#11-related-docs` →
> `#13-related-docs`. The fixtures lane renamed `decision_envelopes/` → `runtime_envelopes/`
> to match the canonical envelope. Truth labels preserved or narrowed, never loosened.

[Back to top](#quick-jump)

---

## 12. Definition of done

This register is done enough to enter the repository when:

- it is placed at `docs/domains/flora/MISSING_OR_PLANNED_FILES.md` per Directory Rules §12 (PROPOSED; NEEDS VERIFICATION);
- the flora domain steward and a docs steward review it;
- it is linked from the Flora domain README and `docs/registers/VERIFICATION_BACKLOG.md`;
- the schema-leaf and policy-home CONFLICTED items (OQ-FLORA-MPF-03/04) are logged in `docs/registers/DRIFT_REGISTER.md`;
- the `FloraDecisionEnvelope → RuntimeResponseEnvelope` migration (OQ-FLORA-MPF-05) has a tracking ADR;
- it does not conflict with accepted ADRs (ADR-0001 schema home; the envelope-migration ADR; ADR-S-05 tier scheme);
- the `GENERATED_RECEIPT.json` planned in the PR is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

[Back to top](#quick-jump)

---

## 13. Related docs

| Document | Path | Purpose |
|---|---|---|
| Operating contract | `ai-build-operating-contract.md` | Canonical operating contract, `CONTRACT_VERSION = "3.0.0"`. |
| Directory Rules | `directory-rules.md` | Canonical placement and lifecycle doctrine (§12, §15). |
| ADR-0001 (schema home) | `docs/adr/ADR-0001-schema-home.md` | Default schema authority `schemas/contracts/v1/...` *(NEEDS VERIFICATION)*. |
| Flora landing README | `docs/domains/flora/README.md` | Domain landing / scope / non-ownership *(PROPOSED)*. |
| Flora Identity Model | `docs/domains/flora/IDENTITY_MODEL.md` | Deterministic identity charter (companion). |
| Flora Map UI Contracts | `docs/domains/flora/MAP_UI_CONTRACTS.md` | Map-surface binding (companion). |
| Sensitivity Posture | `docs/domains/flora/SENSITIVITY_POSTURE.md` | Rare-plant generalization / withholding rules *(PROPOSED)*. |
| Verification Backlog | `docs/registers/VERIFICATION_BACKLOG.md` | Repo-wide verification items *(NEEDS VERIFICATION)*. |
| Drift Register | `docs/registers/DRIFT_REGISTER.md` | Conflicts between doctrine and repo state. |
| Fauna analogue | `docs/domains/fauna/SOURCE_REFRESH_RUNBOOK.md` | Precedent for per-domain runbooks. |
| Atlas v1.1 §8 Flora | `[DOM-FLORA]` / Domains Culmination Atlas | Doctrinal basis for this register. |
| Encyclopedia §7.6 Flora | KFM Encyclopedia | Domain capability summary. |

[Back to top](#quick-jump)

---

## Document footer

> [!NOTE]
> **Document status:** `draft v1.1` · **Coverage:** Flora bounded context only ·
> **Implementation maturity:** UNKNOWN (no mounted repository inspected in this session).
> Every file path in this register is **PROPOSED** under Directory Rules §12 and remains
> **NEEDS VERIFICATION** until a `git ls-tree`-equivalent inspection confirms it.

<sub>Last reviewed: 2026-06-03 · Version: v1.1 · `CONTRACT_VERSION = "3.0.0"` · Owners: `<flora domain steward>` · `<docs steward>` · Change discipline: Directory Rules §17 / contract §37 · Doctrine sources: Atlas v1.1 (§8 Flora; Ch. 24.5 tier reference; Ch. 24.13 crosswalk); Encyclopedia §7.6; `directory-rules.md` v1.3 (§7.3, §9, §12, §15); `ai-build-operating-contract.md` v3.0 (§8, §23.2).</sub>

[Back to top](#quick-jump)
