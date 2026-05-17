<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/fauna/missing-or-planned-files
title: Fauna — Missing or Planned Files Register
type: standard
version: v0.1
status: draft
owners: Fauna Domain Steward (TBD) + Docs Steward (TBD)
created: 2026-05-16
updated: 2026-05-16
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/domains/fauna/README.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
  - control_plane/verification_backlog.yaml
  - docs/adr/README.md
  - docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
tags: [kfm, fauna, register, planning, governance]
notes:
  - Planning artifact; not proof of repo state.
  - All paths PROPOSED until verified against mounted repo.
  - Sensitive-occurrence handling defaults deny-closed.
[/KFM_META_BLOCK_V2] -->

# Fauna — Missing or Planned Files Register

> **A per-domain inventory of files that the Fauna lane is expected to grow, organized by responsibility root and lifecycle phase. This is a planning register, not a repo-state report.**

[![Status: draft](https://img.shields.io/badge/status-draft-orange)](#status--ownership)
[![Authority: lineage / proposed](https://img.shields.io/badge/authority-lineage%20%2F%20proposed-blue)](#how-to-read-this-register)
[![Sensitivity: deny-default](https://img.shields.io/badge/sensitivity-deny--default-red)](#sensitivity--rights-rule)
[![Doctrine: KFM v1.1](https://img.shields.io/badge/doctrine-KFM%20Atlas%20v1.1-informational)](#evidence-and-grounding)
[![Last reviewed: 2026-05-16](https://img.shields.io/badge/last%20reviewed-2026--05--16-lightgrey)](#footer)
<!-- TODO: replace static last-reviewed shield with a CI-driven endpoint when the docs CI is wired. -->

| Field | Value |
|---|---|
| **Status** | `draft` — first cut; awaiting domain-steward review |
| **Authority class** | Planning register (lineage + PROPOSED inventory) — **not** canonical placement authority |
| **Owners** | Fauna Domain Steward (TBD) + Docs Steward (TBD) — `CODEOWNERS` reference TBD |
| **Last reviewed** | `2026-05-16` |
| **Supersedes** | None (first version) |
| **Governed by** | `docs/doctrine/directory-rules.md` (placement), `docs/adr/` (decisions), Atlas v1.1 Ch. 7 (Fauna scope) |

---

## Contents

1. [Purpose and scope](#1-purpose-and-scope)
2. [How to read this register](#2-how-to-read-this-register)
3. [Evidence and grounding](#3-evidence-and-grounding)
4. [Fauna lane at a glance](#4-fauna-lane-at-a-glance)
5. [Sensitivity & rights rule](#5-sensitivity--rights-rule)
6. [Inventory by responsibility root](#6-inventory-by-responsibility-root)
   - [6.1 `docs/domains/fauna/`](#61-docsdomainsfauna)
   - [6.2 `docs/sources/` and source descriptors](#62-docssources-and-source-descriptors)
   - [6.3 `docs/runbooks/fauna/`](#63-docsrunbooksfauna)
   - [6.4 `contracts/domains/fauna/`](#64-contractsdomainsfauna)
   - [6.5 `schemas/contracts/v1/domains/fauna/`](#65-schemascontractsv1domainsfauna)
   - [6.6 `policy/domains/fauna/` and `policy/sensitivity/fauna/`](#66-policydomainsfauna-and-policysensitivityfauna)
   - [6.7 `tests/domains/fauna/`](#67-testsdomainsfauna)
   - [6.8 `fixtures/domains/fauna/`](#68-fixturesdomainsfauna)
   - [6.9 `tools/validators/...` (fauna-touching)](#69-toolsvalidators-fauna-touching)
   - [6.10 `connectors/`](#610-connectors)
   - [6.11 `packages/domains/fauna/`](#611-packagesdomainsfauna)
   - [6.12 `pipelines/` and `pipeline_specs/fauna/`](#612-pipelines-and-pipeline_specsfauna)
   - [6.13 `data/` lifecycle lanes](#613-data-lifecycle-lanes)
   - [6.14 `release/candidates/fauna/`](#614-releasecandidatesfauna)
   - [6.15 `control_plane/` register entries](#615-control_plane-register-entries)
7. [Open ADRs that gate file creation](#7-open-adrs-that-gate-file-creation)
8. [Verification backlog (fauna scope)](#8-verification-backlog-fauna-scope)
9. [How to update this register](#9-how-to-update-this-register)
10. [Related docs](#10-related-docs)

---

## 1. Purpose and scope

The **Missing or Planned Files Register** lists artefacts that current KFM doctrine expects to exist in the **Fauna lane** but which this session cannot confirm are present in the live repository. It is the per-domain companion to `docs/registers/VERIFICATION_BACKLOG.md` and the human-readable counterpart to `control_plane/verification_backlog.yaml`.

> [!IMPORTANT]
> **This register does not create files.** It records what doctrine expects. Creating a file requires:
> a clear responsibility root (Directory Rules §3, §12), an applicable per-root README (§15), any
> required ADR (§2.4), and — for sensitive content — a passing sensitivity / rights / review gate.

**In scope**

- Files that the Fauna domain dossier, the Atlas v1.1 Fauna chapter, or the Encyclopedia Fauna section expects to exist (schemas, contracts, policies, tests, fixtures, runbooks, source descriptors, lifecycle scaffolding, release candidates).
- Placement implied by `docs/doctrine/directory-rules.md` for any of the object families owned by Fauna.
- Open ADRs whose resolution materially gates which files can be created (e.g., schema-home, sensitivity tier scheme).

**Out of scope**

- Decisions about whether a file *should* exist. That is doctrine, not placement. See `contracts/`, `schemas/`, `policy/`, and ADRs.
- Habitat, Flora, Hydrology, Hazards, and other lanes — except where a cross-lane file legitimately overlaps Fauna (called out explicitly per row).
- Repo-state assertions. Until this register is reconciled against a mounted repo (see §8), every "expected" path is **PROPOSED**.

[⬆ back to top](#contents)

---

## 2. How to read this register

Each row identifies a **proposed path**, the **responsibility** it carries, the **doctrine source** that grounds it, and a **truth label** describing what is known about its current existence.

### Truth labels used in this register

| Label | Meaning |
|---|---|
| **CONFIRMED (doctrine)** | The *requirement* is grounded in attached doctrine. The *file* may or may not yet exist. |
| **PROPOSED** | Path, name, or shape is a design recommendation derived from doctrine; not yet implemented (or implementation unknown this session). |
| **NEEDS VERIFICATION** | Requires inspection of a mounted repository, test run, or release manifest to settle. |
| **UNKNOWN** | Not resolvable from currently available evidence; no defensible inference. |
| **CONFLICTED** | Doctrine source A and doctrine source B point at different placements; an ADR or correction notice is needed. |

> [!NOTE]
> Repo presence of any file listed here is **NEEDS VERIFICATION** by default for this session, regardless of how confident doctrine is about the requirement. The register intentionally separates *"the lane requires this"* (often CONFIRMED) from *"this path exists"* (UNKNOWN without inspection).

### Filename conventions (PROPOSED)

- Schemas: `<object_family>.schema.json` in snake_case, under `schemas/contracts/v1/domains/fauna/`.
- Contract markdown: `<object_family>.md` in snake_case, under `contracts/domains/fauna/`.
- Policy bundles: `.rego` / `.yaml` under `policy/domains/fauna/...`.
- Tests: pytest-style names; mirror the schema or contract under test.
- Runbooks: `UPPER_SNAKE_CASE.md` under `docs/runbooks/fauna/` (subfolder convention itself is **open ADR**; see §7).

If the repo adopts a different convention, **the repo convention wins** and this register MUST be updated accordingly via PR.

[⬆ back to top](#contents)

---

## 3. Evidence and grounding

The inventories below are grounded in the following project sources. Where a row cites a source, the citation is to a *requirement*, not a *file*. None of these sources prove a current file exists in the repository.

- **Directory Rules** (`docs/doctrine/directory-rules.md`) — §3 (root responsibility), §6 (governance roots), §9 (data lifecycle), §12 (Domain Placement Law), §15 (Required README Contract). [CONFIRMED doctrine]
- **KFM Domains Culmination Atlas v1.1**, Ch. 7 Fauna (A–N), Ch. 24.13 (Domain ↔ Responsibility-Root Crosswalk), App. G (verification backlog). [CONFIRMED dossier]
- **KFM Domain and Capability Encyclopedia**, §7.5 Fauna (A–N). [CONFIRMED dossier]
- **KFM Unified Implementation Architecture Build Manual**, §30.4 Fauna scope and open items. [CONFIRMED dossier]
- **Atlas Pass 20 Idea Index** — POL, VAL, MAP, GOV doctrine surfaces that the fauna lane inherits. [CONFIRMED lineage]
- **ADR-0001** (schema home: `schemas/contracts/v1/...`). [CONFIRMED doctrine, ADR text NEEDS VERIFICATION]

> [!NOTE]
> Where doctrine sources disagree on placement — for example, Atlas Ch. 24.13's `contracts/fauna/` versus Directory Rules §6.3's `contracts/domains/<domain>/` pattern — Directory Rules wins per §2.1 (authority order). The Atlas reference is treated as lineage and flagged below.

[⬆ back to top](#contents)

---

## 4. Fauna lane at a glance

The diagram below shows the responsibility roots that the Fauna lane is expected to populate. Every shape is **PROPOSED** for this repo's current state; only the *pattern* (Directory Rules §12) is CONFIRMED.

```mermaid
flowchart LR
  subgraph DOC["📚 docs/  (human-facing)"]
    D1[docs/domains/fauna/]
    D2[docs/sources/.../fauna_*]
    D3[docs/runbooks/fauna/]
    D4[docs/adr/ADR-*-fauna-*]
  end

  subgraph MEAN["📐 contracts/ + schemas/  (meaning + shape)"]
    C1[contracts/domains/fauna/]
    S1[schemas/contracts/v1/domains/fauna/]
  end

  subgraph GOV["🛡 policy/  (admissibility)"]
    P1[policy/domains/fauna/]
    P2[policy/sensitivity/fauna/]
    P3[policy/rights/fauna/]
  end

  subgraph PROOF["🧪 tests/ + fixtures/  (enforceability)"]
    T1[tests/domains/fauna/]
    F1[fixtures/domains/fauna/]
  end

  subgraph EXEC["⚙ pipelines/ + connectors/ + tools/"]
    PL1[pipelines/.../fauna]
    PS1[pipeline_specs/fauna/]
    CN1[connectors/&lt;source&gt;/...]
    TL1[tools/validators/...]
    PKG1[packages/domains/fauna/]
  end

  subgraph DATA["💾 data/  (lifecycle)"]
    R1[data/raw/fauna/]
    W1[data/work/fauna/]
    Q1[data/quarantine/fauna/]
    PR1[data/processed/fauna/]
    CT1[data/catalog/domain/fauna/]
    PB1[data/published/layers/fauna/]
    RG1[data/registry/sources/fauna/]
  end

  subgraph REL["🚀 release/  (decisions)"]
    RC1[release/candidates/fauna/]
  end

  DOC --> MEAN --> GOV --> PROOF --> EXEC --> DATA --> REL
```

> [!WARNING]
> **The diagram is illustrative.** Arrows represent governance flow (doctrine → meaning → admissibility → proof → execution → data → release), not file generation or runtime call order. Promotion through `data/` phases is a **governed state transition**, not a file move (Directory Rules §9.1).

[⬆ back to top](#contents)

---

## 5. Sensitivity & rights rule

> [!CAUTION]
> **Fauna is a deny-default lane for sensitive occurrence content.** Exact sensitive occurrences, **nests, dens, roosts, hibernacula, spawning sites**, and steward-controlled records fail closed. Public exact-occurrence tiles for sensitive taxa are denied. Any new fauna file that touches these object families MUST carry a sensitivity tier, a redaction receipt path (where applicable), and a documented review state before promotion.
> *(Atlas v1.1 §7.I; Encyclopedia §7.5; Pass 20 POL doctrine.)*

When a planned file under this register touches sensitive content, the corresponding rows in §6 will explicitly call out **deny-default** in the *Gate / dependency* column. The sensitivity-tier vocabulary itself remains open under **ADR-S-05** (see §7).

[⬆ back to top](#contents)

---

## 6. Inventory by responsibility root

Each subsection follows the same shape: a brief root-level note, a table of expected paths, and any per-root caveats. Paths and exact filenames are **PROPOSED** unless explicitly noted otherwise.

### 6.1 `docs/domains/fauna/`

**Purpose.** Human-facing fauna domain doctrine: dossier, ubiquitous language, source-family overview, sensitivity posture, viewing products, pipeline shape, open questions. Authority is **lineage / proposed-canonical** — `docs/domains/<domain>/` is CONFIRMED as a canonical subpath of `docs/` (Directory Rules §6.1).

| Proposed path | Purpose | Doctrine basis | Status / gate |
|---|---|---|---|
| `docs/domains/fauna/README.md` | Domain dossier and orientation page; ubiquitous language, scope and non-ownership, sources, pipeline shape, public-safety posture. | Atlas v1.1 Ch. 7; Directory Rules §15 (Required README Contract). | **CONFIRMED required** / **NEEDS VERIFICATION** present |
| `docs/domains/fauna/MISSING_OR_PLANNED_FILES.md` | *(this document)* | Atlas v1.1 §G.7 (forward verification backlog); Directory Rules §2.5 (drift handling). | Present in this PR |
| `docs/domains/fauna/OBJECT_FAMILIES.md` | Per-object-family reference: Taxon, Taxon Crosswalk, Conservation Status, Occurrence Evidence, Occurrence Restricted, Occurrence Public, RangePolygon, SeasonalRange, MigrationRoute, SensitiveSite, MortalityObservation, DiseaseObservation, Invasive Species Record, Redaction Receipt, MonitoringEvent. | Atlas v1.1 §7.E; Encyclopedia §7.5.C. | **PROPOSED** |
| `docs/domains/fauna/SOURCE_FAMILIES.md` | KDWP-like steward, USFWS ECOS, NatureServe, GBIF / eBird / iNaturalist / iDigBio / BISON, EDDMapS, agency monitoring (surveys / eDNA / acoustic / telemetry), NLCD / NWI / PADUS / SSURGO context. | Atlas v1.1 §7.D; Encyclopedia §7.5.B. | **PROPOSED** |
| `docs/domains/fauna/SENSITIVITY_POSTURE.md` | Deny-default rule set, geoprivacy transforms, redaction-receipt requirement, sensitive-site object families, tier mapping under ADR-S-05. | Atlas v1.1 §7.I; Pass 20 POL doctrine. | **PROPOSED**; gated on ADR-S-05 (tier scheme) |
| `docs/domains/fauna/CROSS_LANE_RELATIONS.md` | Fauna ↔ Habitat, ↔ Flora, ↔ Hydrology, ↔ Hazards relations; ownership preservation; EvidenceBundle support. | Atlas v1.1 §7.F. | **PROPOSED** |
| `docs/domains/fauna/VERIFICATION_BACKLOG.md` | Per-domain backlog mirroring repo-wide `docs/registers/VERIFICATION_BACKLOG.md` for fauna-scoped items. | Atlas v1.1 §7.N. | **PROPOSED** |

> [!NOTE]
> Some of the above may be folded into `docs/domains/fauna/README.md` rather than created as siblings; that is a per-root README authoring decision, not a placement question.

[⬆ back to top](#contents)

### 6.2 `docs/sources/` and source descriptors

Source-descriptor standards live at `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (repo-wide). Fauna-specific source descriptions belong under either `docs/sources/<source>/` (per-source) or under the fauna domain page; the exact pattern **NEEDS VERIFICATION** against repo convention.

| Proposed path | Purpose | Doctrine basis | Status / gate |
|---|---|---|---|
| `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | Repo-wide standard. | Directory Rules §6.1. | **CONFIRMED required**, **NEEDS VERIFICATION** present |
| `docs/sources/gbif/README.md` | GBIF Occurrence API and Backbone notes. | Encyclopedia §7.5.B; New Ideas 5-15. | **PROPOSED** |
| `docs/sources/inaturalist/README.md` | iNaturalist research-grade observations. | Atlas v1.1 §7.D. | **PROPOSED** |
| `docs/sources/ebird/README.md` | eBird EBD — **restricted-use terms** govern any derivative release. | Atlas v1.1 §7.D; Pass 10 C10-06. | **PROPOSED**; rights review **MUST** precede any release |
| `docs/sources/natureserve/README.md` | NatureServe conservation rankings; drives sensitivity classifications. | Atlas v1.1 §7.D. | **PROPOSED** |
| `docs/sources/usfws-ecos/README.md` | USFWS ECOS listed-species and critical-habitat datasets. | Atlas v1.1 §7.D. | **PROPOSED** |
| `docs/sources/kdwp/README.md` | KDWP steward sources (incl. SINC). | Atlas v1.1 §7.D; New Ideas 5-8. | **PROPOSED**; rights / steward review **NEEDS VERIFICATION** |
| `docs/sources/eddmaps/README.md` | EDDMapS invasive species records. | Atlas v1.1 §7.D. | **PROPOSED** |
| `docs/sources/idigbio/README.md` | iDigBio specimen aggregation. | Atlas v1.1 §7.D. | **PROPOSED** |
| `docs/sources/ku-nhm/README.md` | KU Biodiversity Institute Natural History Museum (in-state collection of record). | Pass 10 C10-06. | **PROPOSED**; specimen-count denominators **NEEDS VERIFICATION** |
| `docs/sources/fhsu-sternberg/README.md` | Sternberg Museum (FHSU). | Pass 10 C10-06. | **PROPOSED** |

[⬆ back to top](#contents)

### 6.3 `docs/runbooks/fauna/`

> [!NOTE]
> The runbook **subfolder convention** (`docs/runbooks/fauna/...` vs. flat `docs/runbooks/fauna_*.md`) is itself an open ADR — see §7. This register uses the subfolder form; if the ADR resolves the other way, every row below requires a name flip.

| Proposed path | Purpose | Doctrine basis | Status / gate |
|---|---|---|---|
| `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` | Source-refresh, drift detection, quarantine recovery for fauna sources. | Atlas v1.1 §7.H; New Ideas 5-15 ecology watcher slice. | **NEEDS VERIFICATION** present in repo |
| `docs/runbooks/fauna/TAXONOMY_RESOLUTION_RUNBOOK.md` | ITIS / GBIF Backbone resolution and tie-breaks; ambiguity handling. | Atlas v1.1 §7.N; Pass 10 C7-07 / C7-08. | **PROPOSED** |
| `docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md` | Geoprivacy transform application, redaction-receipt issuance, steward-review path. | Atlas v1.1 §7.I; Encyclopedia §7.5.M. | **PROPOSED**; gated on ADR-S-05 |
| `docs/runbooks/fauna/PUBLICATION_GATE_DRY_RUN.md` | Pre-promotion gate dry run for fauna release candidates. | Encyclopedia §7.5.M; Atlas Pass 20 VAL-004. | **PROPOSED** |
| `docs/runbooks/fauna/ROLLBACK_DRILL.md` | RollbackCard exercise for a released fauna layer or feature. | Encyclopedia §7.5.M; Atlas v1.1 App. E. | **PROPOSED** |
| `docs/runbooks/fauna/EBD_DERIVATIVE_RELEASE.md` | eBird EBD restricted-use derivative release checklist. | Pass 10 C10-06; Atlas v1.1 §7.D. | **PROPOSED**; rights review **MUST** precede |

[⬆ back to top](#contents)

### 6.4 `contracts/domains/fauna/`

**Purpose.** Object **meaning** (Markdown). Pairs one-for-one with `schemas/contracts/v1/domains/fauna/` (shape). Per Directory Rules §6.3 the canonical lane home is `contracts/domains/fauna/` — note this is **CONFLICTED** against Atlas v1.1 Ch. 24.13 which uses `contracts/fauna/` (no `domains/` segment). Directory Rules wins (§2.1); the Atlas crosswalk is lineage.

| Proposed path | Object family | Doctrine basis | Status |
|---|---|---|---|
| `contracts/domains/fauna/README.md` | Per-root README (§15). | Directory Rules §15. | **PROPOSED** |
| `contracts/domains/fauna/taxon.md` | `Taxon` semantic spec. | Atlas v1.1 §7.C, §7.E. | **PROPOSED** |
| `contracts/domains/fauna/taxon_crosswalk.md` | `TaxonCrosswalk` (ITIS↔GBIF↔others) semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/conservation_status.md` | `ConservationStatus` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/occurrence_evidence.md` | `OccurrenceEvidence` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/occurrence_restricted.md` | `OccurrenceRestricted` — exact, steward-only. | Atlas v1.1 §7.E, §7.I. | **PROPOSED**; deny-default |
| `contracts/domains/fauna/occurrence_public.md` | `OccurrencePublic` — generalized / public-safe derivative. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/range_polygon.md` | `RangePolygon` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/seasonal_range.md` | `SeasonalRange` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/migration_route.md` | `MigrationRoute` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/sensitive_site.md` | `SensitiveSite` semantic spec — nests / dens / roosts / hibernacula / spawning. | Atlas v1.1 §7.E, §7.I. | **PROPOSED**; deny-default |
| `contracts/domains/fauna/mortality_observation.md` | `MortalityObservation` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/disease_observation.md` | `DiseaseObservation` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/invasive_species_record.md` | `InvasiveSpeciesRecord` semantic spec. | Atlas v1.1 §7.E. | **PROPOSED** |
| `contracts/domains/fauna/monitoring_event.md` | `MonitoringEvent` semantic spec (surveys, eDNA, acoustic, telemetry). | Atlas v1.1 §7.C. | **PROPOSED** |
| `contracts/domains/fauna/redaction_receipt.md` | `RedactionReceipt` — record of geoprivacy / field-redaction transforms. | Atlas v1.1 §7.E; Encyclopedia §7.5.C. | **PROPOSED** |

> [!IMPORTANT]
> Per Directory Rules §6.3, executable schema definitions **MUST NOT** live alongside contract Markdown. Any `*.schema.json` found under `contracts/...` is **CONFLICTED** per ADR-0001 and must migrate to §6.5.

[⬆ back to top](#contents)

### 6.5 `schemas/contracts/v1/domains/fauna/`

**Purpose.** Object **shape** (JSON Schema). Canonical home per ADR-0001.

<details>
<summary><strong>Expand: full fauna schema inventory (PROPOSED)</strong></summary>

| Proposed path | Object family | Status |
|---|---|---|
| `schemas/contracts/v1/domains/fauna/taxon.schema.json` | `Taxon` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/taxon_crosswalk.schema.json` | `TaxonCrosswalk` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/conservation_status.schema.json` | `ConservationStatus` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json` | `OccurrenceEvidence` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/occurrence_restricted.schema.json` | `OccurrenceRestricted` | **PROPOSED** (deny-default) |
| `schemas/contracts/v1/domains/fauna/occurrence_public.schema.json` | `OccurrencePublic` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/range_polygon.schema.json` | `RangePolygon` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/seasonal_range.schema.json` | `SeasonalRange` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/migration_route.schema.json` | `MigrationRoute` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/sensitive_site.schema.json` | `SensitiveSite` | **PROPOSED** (deny-default) |
| `schemas/contracts/v1/domains/fauna/mortality_observation.schema.json` | `MortalityObservation` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/disease_observation.schema.json` | `DiseaseObservation` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/invasive_species_record.schema.json` | `InvasiveSpeciesRecord` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/monitoring_event.schema.json` | `MonitoringEvent` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/redaction_receipt.schema.json` | `RedactionReceipt` | **PROPOSED** |
| `schemas/contracts/v1/domains/fauna/abundance_indicator.schema.json` | `AbundanceIndicator` | **PROPOSED** (Encyclopedia §7.5.C) |
| `schemas/contracts/v1/domains/fauna/richness_indicator.schema.json` | `RichnessIndicator` | **PROPOSED** (Encyclopedia §7.5.C) |
| `schemas/tests/valid/domains/fauna/...` | Positive fixtures (paths mirror schemas). | **PROPOSED** |
| `schemas/tests/invalid/domains/fauna/...` | Negative fixtures (paths mirror schemas). | **PROPOSED** |

</details>

> [!NOTE]
> Whether per-domain receipt schemas live under `schemas/contracts/v1/domains/fauna/receipts/` or under a shared `schemas/contracts/v1/receipts/` home is open under **ADR-S-03**. This register intentionally does *not* yet enumerate receipt schemas under `fauna/` to avoid prejudging that ADR.

[⬆ back to top](#contents)

### 6.6 `policy/domains/fauna/` and `policy/sensitivity/fauna/`

**Purpose.** Admissibility, sensitivity, rights, and release-gate policy for fauna content. Canonical singular root is `policy/` (Directory Rules §6.5); `policies/` is treated as compatibility.

| Proposed path | Purpose | Doctrine basis | Status / gate |
|---|---|---|---|
| `policy/domains/fauna/README.md` | Per-root README (§15). | Directory Rules §15. | **PROPOSED** |
| `policy/sensitivity/fauna/deny_default.rego` (or `.yaml`) | Default-deny for sensitive occurrence, nest, den, roost, hibernacula, spawning, steward-controlled records. | Atlas v1.1 §7.I; Atlas Ch. 24.13. | **PROPOSED**; deny-default |
| `policy/sensitivity/fauna/tier_mapping.yaml` | NatureServe S1/S2 → sensitivity tier mapping. | Pass 10 C10-06; ADR-S-05. | **PROPOSED**; gated on ADR-S-05 |
| `policy/sensitivity/fauna/sensitive_taxa.yaml` | Curated list of sensitive taxa (steward-maintained, not public). | Atlas v1.1 §7.I. | **PROPOSED**; restricted |
| `policy/rights/fauna/ebd_terms.yaml` | eBird EBD restricted-use terms enforcement. | Pass 10 C10-06. | **PROPOSED** |
| `policy/rights/fauna/source_terms.yaml` | Per-source rights, license, attribution, redistribution class. | Atlas v1.1 §7.D. | **PROPOSED** |
| `policy/domains/fauna/tile_field_allowlist.yaml` | Public PMTiles field allowlist for fauna layers. | Atlas v1.1 §7.K (tile field allowlist tests). | **PROPOSED** |
| `policy/domains/fauna/api_envelope.rego` | `FaunaDecisionEnvelope` finite-outcome policy: ANSWER / ABSTAIN / DENY / ERROR. | Atlas v1.1 §7.J; Encyclopedia §7.5.I. | **PROPOSED** |
| `policy/release/fauna/promotion_gate.rego` | Promotion gate: source-role registry + rights + taxonomic resolution + sensitivity/geoprivacy + evidence closure + public-safe derivative + rollback support. | Build Manual §30.4. | **PROPOSED** |
| `policy/tests/domains/fauna/...` | Policy tests (deny / abstain / allow / restrict). | Directory Rules §6.5. | **PROPOSED** |
| `policy/fixtures/domains/fauna/...` | Policy fixtures distinct from `tests/fixtures/`. | Directory Rules §6.5. | **PROPOSED** |

[⬆ back to top](#contents)

### 6.7 `tests/domains/fauna/`

**Purpose.** Proof that fauna rules are enforceable. Directly maps to the proposed validator list in Atlas v1.1 §7.K.

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `tests/domains/fauna/test_source_role_authority.py` | Source-role anti-collapse for legal status / aggregator / model / observation. | Atlas v1.1 §7.K. | **PROPOSED** |
| `tests/domains/fauna/test_taxonomy_resolution.py` | ITIS / GBIF Backbone resolution + ambiguity handling. | Atlas v1.1 §7.K; §7.N (taxonomy resolution implementation NEEDS VERIFICATION). | **PROPOSED** |
| `tests/domains/fauna/test_occurrence_split.py` | Restricted vs. public occurrence split — sensitive-taxa fail closed. | Atlas v1.1 §7.K; §7.I. | **PROPOSED**; deny-default |
| `tests/domains/fauna/test_redaction_receipt.py` | RedactionReceipt validation for geoprivacy transforms. | Atlas v1.1 §7.K. | **PROPOSED** |
| `tests/domains/fauna/test_tile_field_allowlist.py` | Public-tile field allowlist enforcement. | Atlas v1.1 §7.K. | **PROPOSED** |
| `tests/domains/fauna/test_runtime_envelope_negative.py` | Runtime Response Envelope negative cases (ABSTAIN / DENY / ERROR). | Atlas v1.1 §7.K. | **PROPOSED** |
| `tests/domains/fauna/test_evidence_closure.py` | EvidenceRef → EvidenceBundle resolution for fauna features. | Encyclopedia §7.5.H. | **PROPOSED** |
| `tests/domains/fauna/test_publication_gate.py` | Publication gate fail-closed on missing proof, sidecar, signature, rights, sensitivity. | Build Manual §30.4; Pass 20 VAL-004. | **PROPOSED** |
| `tests/domains/fauna/test_rollback_drill.py` | RollbackCard exercise. | Encyclopedia §7.5.M. | **PROPOSED** |
| `tests/domains/fauna/test_ai_no_leak.py` | AI Focus Mode never leaks sensitive exact locations for fauna. | Atlas v1.1 §7.L, §7.N. | **PROPOSED**; deny-default |

[⬆ back to top](#contents)

### 6.8 `fixtures/domains/fauna/`

**Purpose.** Golden, valid, invalid, and synthetic test inputs for fauna. Per Directory Rules §6.6, fixtures MAY live under `tests/fixtures/` OR `fixtures/`, but not both without a per-root README distinguishing scope.

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `fixtures/domains/fauna/valid/non_sensitive_occurrence.json` | One non-sensitive public occurrence fixture joined to a habitat patch. | Encyclopedia §7.5.N (first credible thin slice). | **PROPOSED** |
| `fixtures/domains/fauna/valid/range_polygon.geojson` | A small valid `RangePolygon`. | Atlas v1.1 §7.E. | **PROPOSED** |
| `fixtures/domains/fauna/valid/seasonal_range.geojson` | A `SeasonalRange` with valid temporal scope. | Atlas v1.1 §7.E. | **PROPOSED** |
| `fixtures/domains/fauna/invalid/missing_source_descriptor.json` | Negative fixture for source-role authority test. | Pass 20 VAL-003. | **PROPOSED** |
| `fixtures/domains/fauna/invalid/over_precise_sensitive.json` | Negative fixture: exact location for sensitive taxon (must DENY). | Atlas v1.1 §7.I. | **PROPOSED**; deny-default |
| `fixtures/domains/fauna/invalid/unresolved_taxonomy.json` | Negative fixture: ambiguous TaxonCrosswalk. | Atlas v1.1 §7.N. | **PROPOSED** |
| `fixtures/domains/fauna/synthetic/no_network_drift_window.json` | Synthetic source-drift watcher input (no live network). | New Ideas 5-15; Pass 20 EXP-001. | **PROPOSED** |
| `fixtures/domains/fauna/golden/public_safe_density_grid.json` | Golden public-safe occurrence density grid. | Atlas v1.1 §7.G. | **PROPOSED** |

[⬆ back to top](#contents)

### 6.9 `tools/validators/...` (fauna-touching)

> [!NOTE]
> Per Directory Rules §12 (Multi-domain and cross-cutting files), shared validators **MUST NOT** be placed under a single-domain segment. The rows below are *fauna-touching* validators whose canonical home is under `tools/validators/<topic>/`, not `tools/validators/domains/fauna/`.

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `tools/validators/source_descriptor/` | Validates `SourceDescriptor` including fauna sources. | Directory Rules §7.5. | **NEEDS VERIFICATION** present |
| `tools/validators/evidence_bundle/` | Validates `EvidenceBundle` including fauna projections. | Directory Rules §7.5. | **NEEDS VERIFICATION** present |
| `tools/validators/taxonomy_resolver/` | ITIS / GBIF / NatureServe taxonomy resolver and tie-breaker. | Atlas v1.1 §7.N; Pass 10 C7-07 / C7-08. | **PROPOSED** |
| `tools/validators/geoprivacy_transform/` | Validates geoprivacy transform + RedactionReceipt. | Atlas v1.1 §7.I. | **PROPOSED** |
| `tools/validators/sensitive_location_allow/` | Pre-publication check that no exact sensitive coordinates leak. | Atlas v1.1 §7.I. | **PROPOSED**; deny-default |

[⬆ back to top](#contents)

### 6.10 `connectors/`

Per Directory Rules §7.3, connectors emit only to `data/raw/` or `data/quarantine/` — **connectors do not publish**. Connector files are organized by source, not by domain, but every connector below admits fauna content.

| Proposed path | Source | Doctrine basis | Status / gate |
|---|---|---|---|
| `connectors/gbif/` | GBIF Occurrence API + Backbone. | Atlas v1.1 §7.D; New Ideas 5-15. | **PROPOSED**; rights review required |
| `connectors/inaturalist/` | iNaturalist research-grade observations. | Atlas v1.1 §7.D. | **PROPOSED** |
| `connectors/ebird/` | eBird EBD. | Pass 10 C10-06. | **PROPOSED**; **restricted-use terms gate** |
| `connectors/natureserve/` | NatureServe rankings. | Atlas v1.1 §7.D. | **PROPOSED** |
| `connectors/usfws-ecos/` | USFWS ECOS. | Atlas v1.1 §7.D. | **PROPOSED** |
| `connectors/kdwp/` | KDWP steward sources. | Atlas v1.1 §7.D. | **PROPOSED**; steward agreement **NEEDS VERIFICATION** |
| `connectors/eddmaps/` | EDDMapS invasive feeds. | Atlas v1.1 §7.D. | **PROPOSED** |
| `connectors/idigbio/` | iDigBio specimen records. | Atlas v1.1 §7.D. | **PROPOSED** |

> [!WARNING]
> **No live wildlife connector should be activated** until source rights, source role, steward permissions, taxonomic resolver, and sensitivity policy are settled. Per the Build Manual §30.4, the proposed first PR for fauna is synthetic and non-live-source.

[⬆ back to top](#contents)

### 6.11 `packages/domains/fauna/`

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `packages/domains/fauna/README.md` | Per-root README (§15). | Directory Rules §15. | **PROPOSED** |
| `packages/domains/fauna/identity/` | Fauna identity rules (source id + object role + temporal scope + normalized digest). | Atlas v1.1 §7.E. | **PROPOSED** |
| `packages/domains/fauna/normalize/` | Domain-specific normalization helpers (taxonomy, temporal, geometry). | Atlas v1.1 §7.H. | **PROPOSED** |
| `packages/domains/fauna/public_safe/` | Public-safe derivative builders (density grids, generalized ranges). | Atlas v1.1 §7.G. | **PROPOSED** |

[⬆ back to top](#contents)

### 6.12 `pipelines/` and `pipeline_specs/fauna/`

Per Directory Rules §7.4: `pipeline_specs/` is *what* should run (declarative); `pipelines/` is *how* it runs (executable).

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `pipeline_specs/fauna/README.md` | Per-root README for fauna specs. | Directory Rules §15. | **PROPOSED** |
| `pipeline_specs/fauna/ingest.yaml` | Ingest spec per fauna source family. | Atlas v1.1 §7.H. | **PROPOSED** |
| `pipeline_specs/fauna/normalize.yaml` | Normalize spec (taxonomy, geometry, time, identity, evidence, rights, policy). | Atlas v1.1 §7.H. | **PROPOSED** |
| `pipeline_specs/fauna/catalog.yaml` | Catalog spec (STAC / DCAT / PROV emissions for fauna). | Atlas v1.1 §7.H. | **PROPOSED** |
| `pipeline_specs/fauna/publish.yaml` | Publish spec (public-safe layers, manifests). | Atlas v1.1 §7.H. | **PROPOSED** |
| `pipelines/ingest/fauna/...` | Executable ingest steps. | Directory Rules §7.4. | **PROPOSED** |
| `pipelines/normalize/fauna/...` | Executable normalize steps. | Directory Rules §7.4. | **PROPOSED** |
| `pipelines/publish/fauna/...` | Executable publish steps. | Directory Rules §7.4. | **PROPOSED** |
| `pipelines/rollback/fauna/...` | Rollback drill executors. | Directory Rules §7.4. | **PROPOSED** |

[⬆ back to top](#contents)

### 6.13 `data/` lifecycle lanes

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move** (Directory Rules §9.1). The presence of a phase directory in this register is the *expectation*; whether *bytes* may be promoted into it is governed by validators, policy gates, EvidenceBundle creation, catalog closure, and release-decision recording — never by the directory existing.

<details>
<summary><strong>Expand: full fauna data-lane inventory (PROPOSED)</strong></summary>

| Phase | Proposed path | Allowed | MUST NOT | Status |
|---|---|---|---|---|
| RAW | `data/raw/fauna/<source_id>/<run_id>/` | Immutable source captures with retrieval metadata + checksums. | Public clients, AI context, UI layers, normalized records. | **PROPOSED** |
| WORK | `data/work/fauna/<run_id>/` | Normalized intermediates, candidate assertions. | Public API/UI, release aliases. | **PROPOSED** |
| QUARANTINE | `data/quarantine/fauna/<reason>/<run_id>/` | Failed validation, unresolved rights/sensitivity, schema drift, over-precise geometry. | Promotion candidates without remediation. | **PROPOSED**; deny-default for over-precise sensitive |
| PROCESSED | `data/processed/fauna/<dataset_id>/<version>/` | Validated canonical records. | Assumption of public/release status. | **PROPOSED** |
| CATALOG | `data/catalog/domain/fauna/` | STAC / DCAT / PROV records for fauna; domain catalog entries. | Uncited claims, unclosed identifiers. | **PROPOSED** |
| TRIPLETS | `data/triplets/...` (cross-cutting; fauna projections only) | Relationship projections, graph-compatible triples. | Canonical replacement semantics. | **PROPOSED** |
| PUBLISHED | `data/published/layers/fauna/` | Released public-safe artifacts (PMTiles, GeoParquet, API payloads). | RAW / WORK / QUARANTINE / exact restricted geometry. | **PROPOSED**; deny-default for sensitive exact |
| RECEIPTS | `data/receipts/{ingest,validation,pipeline,ai,release}/...` (cross-cutting) | Process memory for fauna runs. | Proof of release by themselves. | **PROPOSED** |
| PROOFS | `data/proofs/{evidence_bundle,proof_pack,validation_report,citation_validation}/...` (cross-cutting; fauna entries) | EvidenceBundle, ProofPack, integrity bundles for fauna. | Process-only receipts without release context. | **PROPOSED** |
| ROLLBACK | `data/rollback/fauna/<release_id>/` | Rollback cards, alias revert receipts. | Deleting prior meanings. | **PROPOSED** |
| REGISTRY | `data/registry/sources/fauna/` | Append-only source descriptor records for fauna. | Canonical domain truth. | **PROPOSED** |

</details>

[⬆ back to top](#contents)

### 6.14 `release/candidates/fauna/`

Per Directory Rules §9.2, **release decisions** live under `release/`, distinct from released artefacts under `data/published/`.

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `release/candidates/fauna/README.md` | Per-root note on fauna release-candidate dossiers. | Directory Rules §15. | **PROPOSED** |
| `release/candidates/fauna/<candidate_id>/manifest.json` | ReleaseManifest candidate referencing fauna proofs. | Encyclopedia §7.5.M. | **PROPOSED** |
| `release/candidates/fauna/<candidate_id>/rollback_card.json` | RollbackCard for candidate. | Encyclopedia §7.5.M. | **PROPOSED** |
| `release/candidates/fauna/<candidate_id>/policy_decision.json` | PromotionDecision record. | Atlas v1.1 §7.H. | **PROPOSED** |

[⬆ back to top](#contents)

### 6.15 `control_plane/` register entries

The fauna lane is also represented in machine-readable governance maps.

| Proposed path | Purpose | Doctrine basis | Status |
|---|---|---|---|
| `control_plane/source_authority_register.yaml` (fauna entries) | Per-source authority class for KDWP, USFWS, NatureServe, GBIF, eBird, iNaturalist, EDDMapS, iDigBio. | Directory Rules §6.2. | **PROPOSED**; fauna rows **NEEDS VERIFICATION** |
| `control_plane/domain_lane_register.yaml` (fauna entry) | Fauna lane row pointing to canonical roots. | Directory Rules §6.2. | **PROPOSED** |
| `control_plane/object_family_register.yaml` (fauna families) | Object family rows for fauna. | Directory Rules §6.2. | **PROPOSED** |
| `control_plane/verification_backlog.yaml` (fauna entries) | Machine-readable mirror of §8 below. | Directory Rules §6.2. | **PROPOSED** |

[⬆ back to top](#contents)

---

## 7. Open ADRs that gate file creation

Several files in §6 cannot be created (or named) without first resolving an outstanding ADR. The list below is drawn from Atlas v1.1 Ch. 24.12 Master Open-ADR Backlog and from the runbook subfolder convention question surfaced in companion work.

| ADR | Question | Files it gates |
|---|---|---|
| **ADR-0001** | Canonical schema home: `schemas/contracts/v1/...` (default) — confirm or amend. | All of §6.5; resolves any `contracts/domains/fauna/*.schema.json` drift. |
| **ADR-S-03** | Receipt class home: `schemas/contracts/v1/receipts/` vs. `schemas/contracts/v1/<domain>/receipts/`. | Whether `schemas/contracts/v1/domains/fauna/receipts/` belongs in §6.5. |
| **ADR-S-04** | Source-role enum — canonical vocabulary and evolution rule. | All source-role-asserting fauna schemas; `policy/rights/fauna/source_terms.yaml`. |
| **ADR-S-05** | Sensitivity tier scheme (T0–T4) — adopt as canonical or revise. | `policy/sensitivity/fauna/tier_mapping.yaml`, `SENSITIVITY_POSTURE.md`, every deny-default policy row. |
| **ADR-S-10** | Stale-state propagation across lanes. | Fauna ↔ Habitat ↔ Hydrology cross-lane joins. |
| **ADR-S-12** | Connector cadence and quarantine recovery policy. | `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md` parameter set. |
| **ADR-S-14** | Cross-lane join policy. | `docs/domains/fauna/CROSS_LANE_RELATIONS.md`; Fauna ↔ Habitat seasonal-support joins. |
| **ADR — runbook subfolders** *(not yet numbered)* | Whether runbooks use `docs/runbooks/<domain>/...` subfolders or a flat `docs/runbooks/<domain>_*.md` naming. | All of §6.3. |
| **ADR — `PROV.md` vs `PROVENANCE.md` naming** *(not yet numbered)* | Standards-doc filename convention. | Indirect: governs cross-referenceability from fauna standards anchors. |
| **ADR — validator exit-code contract** *(not yet numbered)* | Uniform validator exit semantics. | `tests/domains/fauna/test_publication_gate.py`, every validator under §6.9. |

[⬆ back to top](#contents)

---

## 8. Verification backlog (fauna scope)

These items lift directly from Atlas v1.1 §7.N and §G.7 into a working backlog. Each row is something a mounted-repo inspection — or a single targeted artefact — would settle.

| # | Item to verify | Evidence that would settle it | Status |
|---|---|---|---|
| FAUNA-VB-01 | Fauna source rights and steward roles. | Source descriptors under `data/registry/sources/fauna/`; signed steward agreements; rights register. | **NEEDS VERIFICATION** |
| FAUNA-VB-02 | Taxonomy resolution implementation. | `tools/validators/taxonomy_resolver/` + tests + ValidationReports. | **NEEDS VERIFICATION** |
| FAUNA-VB-03 | Restricted vs. public occurrence split. | Schemas under §6.5 + policy under §6.6 + tests under §6.7. | **NEEDS VERIFICATION** |
| FAUNA-VB-04 | Public layer safety and AI no-leak behaviour. | Tile field allowlist tests + Focus Mode citation validation + redaction-receipt audit. | **NEEDS VERIFICATION** |
| FAUNA-VB-05 | Schema home conformance to ADR-0001 for fauna. | `git ls-tree`-equivalent over `schemas/contracts/v1/domains/fauna/` and absence of `contracts/.../*.schema.json` drift. | **NEEDS VERIFICATION** |
| FAUNA-VB-06 | Per-root README presence for every fauna lane segment. | Mounted-repo scan against Directory Rules §15. | **NEEDS VERIFICATION** |
| FAUNA-VB-07 | EvidenceBundle ↔ EvidenceRef closure for at least one fauna feature. | One released non-sensitive fauna feature with `EvidenceBundle` resolvable from its `EvidenceRef`. | **NEEDS VERIFICATION** |
| FAUNA-VB-08 | RollbackCard exercise for a fauna release candidate. | Release dry-run report + rollback card + restored prior manifest. | **NEEDS VERIFICATION** |
| FAUNA-VB-09 | eBird EBD derivative-release terms enforced in policy. | `policy/rights/fauna/ebd_terms.yaml` + passing policy test. | **NEEDS VERIFICATION** |
| FAUNA-VB-10 | Sensitive-site geoprivacy transform with RedactionReceipt. | One non-public sensitive fixture + transform pipeline + signed RedactionReceipt. | **NEEDS VERIFICATION** |

[⬆ back to top](#contents)

---

## 9. How to update this register

> [!TIP]
> Treat this file as a *working* register. The most useful changes are the ones that move rows from **PROPOSED** / **NEEDS VERIFICATION** into **CONFIRMED**, or that retire rows by replacing them with links to the now-created files.

**When a planned file is created**

1. Open a PR that adds the file under the proposed path (or a path you justify in the PR description per Directory Rules §4 Step 5).
2. In the same PR, **update the row** in this register: change the status, swap the *Proposed path* cell for a link, and remove the row when the file is stable.
3. If the actual path differs from the proposed path, add a one-line *Drift register* entry under `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5.

**When doctrine changes**

1. Update the doctrine source (Atlas, Encyclopedia, ADR).
2. Reflect the change here in the same PR or a follow-up. Cite the new doctrine in the row.

**When an ADR resolves an §7 item**

1. Strike or remove the corresponding ADR row in §7.
2. Update any §6 rows that were gated on that ADR.
3. If the ADR introduces a new file family, add new §6 rows under the appropriate root.

**When a row cannot be verified**

Leave it. Honest incompleteness is preferable to persuasive overclaiming (Failure Rule, KFM operating posture).

[⬆ back to top](#contents)

---

## 10. Related docs

- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — canonical placement law and lifecycle invariant
- [`docs/domains/fauna/README.md`](./README.md) *(NEEDS VERIFICATION present)* — fauna domain dossier
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) *(NEEDS VERIFICATION present)* — repo-wide verification backlog
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) *(NEEDS VERIFICATION present)* — repo-wide drift register
- [`control_plane/verification_backlog.yaml`](../../../control_plane/verification_backlog.yaml) *(NEEDS VERIFICATION present)* — machine-readable mirror
- [`docs/adr/README.md`](../../adr/README.md) *(NEEDS VERIFICATION present)* — ADR index, including ADR-0001 schema home and the ADR-S backlog
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) *(NEEDS VERIFICATION present)* — fauna source refresh runbook
- [`docs/standards/PROV.md`](../../standards/PROV.md) *(NEEDS VERIFICATION present)* — W3C PROV-O / PAV profile
- [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) *(NEEDS VERIFICATION present)* — PMTiles delivery profile
- [`docs/standards/OAI-PMH.md`](../../standards/OAI-PMH.md) *(NEEDS VERIFICATION present)* — harvest profile
- [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) *(NEEDS VERIFICATION present)* — metadata crosswalk

> [!NOTE]
> Links above use repo-relative paths. Where a target file's existence is **NEEDS VERIFICATION** for this session, that is called out inline; the link is preserved so it can be validated by a mounted-repo link checker.

[⬆ back to top](#contents)

---

<a id="footer"></a>

<sub>**Last updated:** 2026-05-16 · **Doc id:** `kfm://doc/domains/fauna/missing-or-planned-files` · **Authority:** planning register · **Sensitivity:** public · [⬆ back to top](#contents)</sub>
