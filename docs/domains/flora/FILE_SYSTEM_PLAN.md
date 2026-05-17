<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/flora-file-system-plan-v1
title: Flora Domain File System Plan
type: standard
version: v1
status: draft
owners: <flora-domain-stewards>, <docs-stewards>
created: 2026-05-16
updated: 2026-05-16
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/domains/README.md
  - docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - docs/standards/PROV.md
  - docs/standards/PMTILES.md
  - docs/standards/OGC-API-TILES.md
  - docs/standards/OAI-PMH.md
  - docs/standards/ISO-19115.md
tags: [kfm, flora, directory-rules, file-system, governance, plan]
notes:
  - All concrete paths are PROPOSED until verified against a mounted repository.
  - Domain segment name is `flora` per Domain Placement Law (Directory Rules §12).
  - Authoritative precedence: Directory Rules > ADR > this plan > prior lineage.
[/KFM_META_BLOCK_V2] -->

# 🌱 Flora Domain — File System Plan

> The canonical map of where every flora-domain artifact lives across KFM's
> responsibility roots, derived from Directory Rules §12 Domain Placement Law
> and the flora dossier.

![status](https://img.shields.io/badge/status-draft-blue)
![scope](https://img.shields.io/badge/scope-domain%3A%20flora-2e7d32)
![authority](https://img.shields.io/badge/authority-Directory%20Rules%20%C2%A712-6f42c1)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-0a7ea4)
![sensitivity](https://img.shields.io/badge/sensitivity-rare%2Fjoin--induced-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft · **Owners:** `<flora-domain-stewards>`, `<docs-stewards>` · **Last updated:** 2026-05-16

---

## Quick jump

- [1. Purpose & scope](#1-purpose--scope)
- [2. Authority & precedence](#2-authority--precedence)
- [3. Repo fit — accepted inputs and exclusions](#3-repo-fit--accepted-inputs-and-exclusions)
- [4. Lane map at a glance](#4-lane-map-at-a-glance)
- [5. Master placement table](#5-master-placement-table)
- [6. Per-root flora layouts](#6-per-root-flora-layouts)
- [7. Lifecycle alignment (`data/`)](#7-lifecycle-alignment-data)
- [8. Sensitivity, rights, and join-induced risk](#8-sensitivity-rights-and-join-induced-risk)
- [9. Watcher and connector placement](#9-watcher-and-connector-placement)
- [10. Cross-lane and cross-cutting files](#10-cross-lane-and-cross-cutting-files)
- [11. Compatibility, drift, and migration notes](#11-compatibility-drift-and-migration-notes)
- [12. Open questions & verification backlog](#12-open-questions--verification-backlog)
- [13. Related docs](#13-related-docs)
- [Appendix A — Full PROPOSED path manifest](#appendix-a--full-proposed-path-manifest)

---

## 1. Purpose & scope

The Flora Domain File System Plan declares **where** every flora-related artifact
in KFM is allowed to live, **why** that placement is correct, and **what** has to
exist before files land there. It is a placement contract, not an implementation
status report.

It exists because flora is a high-sensitivity, multi-source botanical domain that
intersects Habitat, Fauna, Soil/Hydrology, Hazards, and Agriculture, and because
rare-plant locations and join-induced sensitivity (e.g., PLANTS × GBIF/iNaturalist)
require deny-by-default placement discipline before a single file is written.

> [!IMPORTANT]
> **Truth posture for this document.** No mounted KFM repository is available
> in this session. Every concrete path below is **PROPOSED** under Directory
> Rules §12 (Domain Placement Law). Promotion of any path to CONFIRMED
> requires repository inspection, an ADR where the rules do not pre-decide,
> and the per-root `README.md` declared in Directory Rules §9.

**In scope**

- File-home mapping for the flora domain across all canonical responsibility roots.
- Lifecycle phase placement under `data/`.
- Sensitivity, rights, watcher, connector, and cross-lane file placement rules.
- Compatibility-root posture for flora-adjacent legacy or mirror locations.

**Out of scope**

- Implementation status of any specific file.
- Schema bodies, contract bodies, validator code, policy bundles, or pipeline logic.
- Final route names, DTO field lists, or API responses.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 2. Authority & precedence

The flora placement decisions in this document derive their authority from a
fixed hierarchy. **Lower layers may operationalize higher layers; they may not
override them silently.**

| Order | Authority | Role for this plan | Status |
|---|---|---|---|
| 1 | **Directory Rules** (`docs/doctrine/directory-rules.md`) | Placement law, including §12 Domain Placement Law, §6 governance roots, §7 implementation roots, §8 compatibility roots, §9.1 `data/` lifecycle | CONFIRMED doctrine |
| 2 | **Accepted ADRs** (e.g., ADR-0001 schema home) | May refine but not contradict Directory Rules | CONFIRMED rule / PROPOSED instances |
| 3 | **Flora dossier** (encyclopedia §7.6, atlas chapter 8) | Object families, source families, sensitivity posture, viewing products | CONFIRMED doctrine / PROPOSED implementation |
| 4 | **This file** (`FILE_SYSTEM_PLAN.md`) | Domain-level path map that translates 1–3 into flora-specific paths | PROPOSED |
| 5 | **Prior reports and lineage PDFs** | Source-ledger evidence; never new canon on placement | Lineage only |

> [!NOTE]
> Where Directory Rules and a flora dossier appear to conflict (e.g.,
> `policy/sensitivity/flora/` referenced by the Domains Culmination Atlas vs.
> `policy/domains/flora/` referenced by Directory Rules §12), this plan treats
> the rules as **compatible, not competing**: `policy/sensitivity/` is a
> cross-cutting sensitivity lane; `policy/domains/` is the domain-segmented
> lane. Both can carry flora content. See §10 for the full crosswalk.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 3. Repo fit — accepted inputs and exclusions

**Upstream of this file**

- Directory Rules — the source of the lane pattern.
- Flora dossier (encyclopedia §7.6) — the source of object families, sources, sensitivity.
- Domains Culmination Atlas, Flora chapter — operationalized lane-by-lane mapping.

**Downstream of this file**

- `docs/domains/flora/README.md` (PROPOSED) — domain landing page; links here for
  the path map.
- `contracts/domains/flora/`, `schemas/contracts/v1/domains/flora/`,
  `policy/domains/flora/`, `tests/domains/flora/`, `fixtures/domains/flora/`,
  `packages/domains/flora/`, `pipelines/domains/flora/`, `pipeline_specs/flora/`,
  `data/<phase>/flora/`, `release/candidates/flora/` — actual flora content
  files; this plan governs their location.

**Accepted inputs (what belongs in this doc)**

- Flora-specific placement claims with a Directory Rules citation.
- Sensitivity and rights placement notes for flora artifacts.
- Cross-lane placement rules where flora joins another domain.
- Compatibility and migration notes for flora-adjacent legacy roots.

**Exclusions (what does NOT belong here)**

- Schema field lists → `contracts/domains/flora/*.md` (meaning) +
  `schemas/contracts/v1/domains/flora/*.schema.json` (shape).
- Policy bundle logic → `policy/domains/flora/`, `policy/sensitivity/flora/`,
  `policy/rights/`, `policy/opa/` per ADR.
- Connector code → `connectors/<source_id>/`; flora-domain output lands under
  `data/raw/flora/<source_id>/<run_id>/`.
- Operational procedures → `docs/runbooks/flora/...` (PROPOSED; see §11 on
  runbook subfolder vs. flat-prefix naming).
- Map renderer or style code → `packages/maplibre/`, `packages/ui/`.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 4. Lane map at a glance

```mermaid
flowchart LR
  subgraph GOV["Governance & meaning (CONFIRMED roots)"]
    DOCS["docs/domains/flora/"]
    CONTRACTS["contracts/domains/flora/"]
    SCHEMAS["schemas/contracts/v1/domains/flora/"]
    POLICY_D["policy/domains/flora/"]
    POLICY_S["policy/sensitivity/flora/"]
  end

  subgraph IMPL["Implementation & proof (CONFIRMED roots)"]
    PKGS["packages/domains/flora/"]
    PIPES["pipelines/domains/flora/"]
    SPECS["pipeline_specs/flora/"]
    TESTS["tests/domains/flora/"]
    FIX["fixtures/domains/flora/"]
  end

  subgraph DATA["Lifecycle data (governance, not storage)"]
    RAW["data/raw/flora/"] --> WORK["data/work/flora/"]
    WORK --> QUAR["data/quarantine/flora/"]
    WORK --> PROC["data/processed/flora/"]
    PROC --> CAT["data/catalog/domain/flora/"]
    PROC --> TRIP["data/triplets/ (cross-domain)"]
    CAT --> PUB["data/published/layers/flora/"]
    TRIP --> PUB
  end

  subgraph REL["Release & rollback"]
    REGISTRY["data/registry/sources/flora/"]
    CANDS["release/candidates/flora/"]
    MANIF["release/manifests/"]
    ROLL["release/rollback_cards/"]
    CORR["release/correction_notices/"]
  end

  DOCS -.cites.-> CONTRACTS
  CONTRACTS -.validated by.-> SCHEMAS
  SCHEMAS -.gated by.-> POLICY_D
  POLICY_D -.composes with.-> POLICY_S
  SPECS -.declares.-> PIPES
  PIPES -.emits to.-> RAW
  PIPES -.promotes.-> PROC
  CAT --> CANDS
  CANDS --> MANIF
  MANIF -.rollback target.-> ROLL
  MANIF -.correction path.-> CORR
  REGISTRY -.admits.-> RAW
```

> [!NOTE]
> The diagram reflects **PROPOSED** flora-specific placement under Directory
> Rules §12. Solid edges show file-system parent/child or lifecycle promotion.
> Dotted edges show governance references (e.g., a doc citing a contract).

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 5. Master placement table

This table is the single-row-per-responsibility-root authoritative summary. Every
path is PROPOSED until verified against a mounted repo.

| Responsibility root | Flora lane | What lives there | Authority | Status |
|---|---|---|---|---|
| `docs/` | `docs/domains/flora/` | Human-facing domain doctrine, this plan, runbooks pointers | Directory Rules §6.1, §12 | PROPOSED placement |
| `contracts/` | `contracts/domains/flora/` | Object meaning: `PlantTaxon.md`, `FloraOccurrence.md`, `RarePlantRecord.md`, etc. | Directory Rules §6.3, §12 | PROPOSED |
| `schemas/` | `schemas/contracts/v1/domains/flora/` | Machine schema: `*.schema.json` per object family | Directory Rules §6.4, ADR-0001, §12 | PROPOSED |
| `policy/` | `policy/domains/flora/` | Allow/deny/restrict/abstain rules scoped to flora | Directory Rules §6.5, §12 | PROPOSED |
| `policy/` (cross-cut) | `policy/sensitivity/flora/` | Rare-plant + join-induced sensitivity rules | Directory Rules §6.5 | PROPOSED |
| `policy/` (cross-cut) | `policy/rights/` (flora entries) | Source-rights enforcement (GBIF, iNat, etc.) | Directory Rules §6.5 | PROPOSED |
| `tests/` | `tests/domains/flora/` | Deterministic enforcement proofs | Directory Rules §4 Step 1, §12 | PROPOSED |
| `fixtures/` | `fixtures/domains/flora/` | Valid/invalid golden inputs, no-network | Directory Rules §4 Step 1, §12 | PROPOSED |
| `packages/` | `packages/domains/flora/` | Reusable flora-typed code (resolvers, normalizers) | Directory Rules §7.2, §12 | PROPOSED |
| `pipelines/` | `pipelines/domains/flora/` | Executable pipeline logic for flora | Directory Rules §7.4, §12 | PROPOSED |
| `pipeline_specs/` | `pipeline_specs/flora/` | Declarative pipeline configs for flora | Directory Rules §7.4, §12 | PROPOSED |
| `pipeline_specs/` (watchers) | `pipeline_specs/watchers/<flora-watcher>.yaml` | PLANTS taxa-drift watcher spec | Directory Rules §7.4; Pass 20 SRC-006 | PROPOSED |
| `connectors/` | `connectors/gbif/`, `connectors/inaturalist/`, `connectors/usfws/`, `connectors/kdwp/` (or equivalents) | Source-specific fetch/admit; flora output → `data/raw/flora/` | Directory Rules §7.3 | PROPOSED |
| `data/raw/` | `data/raw/flora/<source_id>/<run_id>/` | Immutable admitted source payloads | Directory Rules §9.1 | PROPOSED |
| `data/work/` | `data/work/flora/<run_id>/` | Normalization workspace | Directory Rules §9.1 | PROPOSED |
| `data/quarantine/` | `data/quarantine/flora/<reason>/<run_id>/` | Failed gates, never silently promoted | Directory Rules §9.1 | PROPOSED |
| `data/processed/` | `data/processed/flora/<dataset_id>/<version>/` | Validated normalized objects + receipts | Directory Rules §9.1 | PROPOSED |
| `data/catalog/` | `data/catalog/domain/flora/` | STAC/DCAT/PROV catalog records | Directory Rules §9.1 | PROPOSED |
| `data/triplets/` | `data/triplets/graph_deltas/` (cross-domain, flora-tagged) | Graph projections; not a flora-only root | Directory Rules §9.1, §12 multi-domain | PROPOSED |
| `data/receipts/` | `data/receipts/{ingest,validation,pipeline,ai,release}/` (flora-tagged) | Phase-tagged process receipts | Directory Rules §9.1 | PROPOSED |
| `data/proofs/` | `data/proofs/evidence_bundle/` (flora-tagged) | `EvidenceBundle`, `ProofPack`, citation validation | Directory Rules §9.1 | PROPOSED |
| `data/published/` | `data/published/layers/flora/`, `data/published/pmtiles/flora/`, `data/published/api_payloads/flora/` | Released, public-safe flora artifacts | Directory Rules §9.1 | PROPOSED |
| `data/registry/` | `data/registry/sources/flora/`, `data/registry/source_descriptors/<flora-source-ids>/` | Admission and authority control | Directory Rules §9.1 | PROPOSED |
| `data/rollback/` | `data/rollback/flora/<release_id>/` | Alias-revert receipts (data plane) | Directory Rules §9.1 | PROPOSED |
| `release/` | `release/candidates/flora/`, `release/manifests/`, `release/rollback_cards/`, `release/correction_notices/` | Release decisions, rollback cards, correction notices | Directory Rules §6 | PROPOSED |

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 6. Per-root flora layouts

This section drills into each responsibility root that has a flora lane.
All trees are PROPOSED placement; file names are illustrative.

### 6.1 `docs/domains/flora/`

```text
docs/domains/flora/
├── README.md                       # Domain landing page (PROPOSED)
├── FILE_SYSTEM_PLAN.md             # this document
├── OBJECT_FAMILIES.md              # PROPOSED: per-object overview
├── SOURCE_FAMILIES.md              # PROPOSED: source-role-aware overview
├── SENSITIVITY_POSTURE.md          # PROPOSED: rare/join-induced rules summary
├── THIN_SLICE_PLAN.md              # PROPOSED: first credible slice spec
└── CROSS_LANE_NOTES.md             # PROPOSED: Habitat/Fauna/Soil/Hazards joins
```

> [!TIP]
> Operational procedures for flora **do not** belong here. They go under
> `docs/runbooks/...`. See §11 on the subfolder-vs-prefix naming question
> already flagged for fauna (`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`).

### 6.2 `contracts/domains/flora/`

Object **meaning** in Markdown. One file per canonical object family from the
flora dossier (encyclopedia §7.6).

```text
contracts/domains/flora/
├── README.md                       # PROPOSED
├── PlantTaxon.md                   # PROPOSED
├── FloraTaxonCrosswalk.md          # PROPOSED
├── FloraOccurrence.md              # PROPOSED
├── SpecimenRecord.md               # PROPOSED
├── RarePlantRecord.md              # PROPOSED
├── VegetationCommunity.md          # PROPOSED
├── InvasivePlantRecord.md          # PROPOSED
├── PhenologyObservation.md         # PROPOSED
├── RangePolygon.md                 # PROPOSED
├── DistributionSurface.md          # PROPOSED
├── HabitatAssociation.md           # PROPOSED  (cross-lane: flora ↔ habitat)
├── BotanicalSurvey.md              # PROPOSED
├── RestorationPlanting.md          # PROPOSED
└── RedactionReceipt.flora.md       # PROPOSED  (domain-flavored crosswalk to generic)
```

### 6.3 `schemas/contracts/v1/domains/flora/`

Machine **shape**. Authoritative per ADR-0001. One `.schema.json` per object,
plus `tests/valid/` and `tests/invalid/` siblings under the canonical schemas
home (Directory Rules §6.4).

```text
schemas/contracts/v1/domains/flora/
├── plant_taxon.schema.json                  # PROPOSED
├── flora_taxon_crosswalk.schema.json        # PROPOSED
├── flora_occurrence.schema.json             # PROPOSED
├── specimen_record.schema.json              # PROPOSED
├── rare_plant_record.schema.json            # PROPOSED
├── vegetation_community.schema.json         # PROPOSED
├── invasive_plant_record.schema.json        # PROPOSED
├── phenology_observation.schema.json        # PROPOSED
├── range_polygon.flora.schema.json          # PROPOSED
├── distribution_surface.flora.schema.json   # PROPOSED
├── habitat_association.flora.schema.json    # PROPOSED  (cross-lane shape)
├── botanical_survey.schema.json             # PROPOSED
├── restoration_planting.schema.json         # PROPOSED
└── redaction_receipt.flora.schema.json      # PROPOSED
```

> [!WARNING]
> Per Directory Rules §13.1 and ADR-0001, `contracts/domains/flora/*.schema.json`
> is **drift**, not an alternate home. Schema bodies live only under
> `schemas/contracts/v1/...`. Contracts retain semantic Markdown only.

### 6.4 `policy/domains/flora/` and cross-cutting policy lanes

```text
policy/domains/flora/
├── README.md                                # PROPOSED
├── flora_rights.rego                        # PROPOSED  (or equivalent OPA bundle)
├── flora_source_role.rego                   # PROPOSED
├── flora_taxonomy_resolution.rego           # PROPOSED
└── flora_publication_gate.rego              # PROPOSED

policy/sensitivity/flora/                    # PROPOSED  (cross-cut: sensitivity)
├── rare_plant_geoprivacy.rego               # PROPOSED
├── join_induced_sensitivity.rego            # PROPOSED  (PLANTS × GBIF/iNat)
└── exact_geometry_deny.rego                 # PROPOSED

policy/rights/                               # (cross-cut: source rights)
└── flora/                                   # PROPOSED  (GBIF, iNat, USFWS terms)

policy/release/                              # (cross-cut: release class)
└── flora/                                   # PROPOSED  (public-safe gates)
```

### 6.5 `tests/domains/flora/` and `fixtures/domains/flora/`

Tests prove rules are enforceable; fixtures provide valid/invalid inputs. Both
must be **no-network** by default per flora dossier and Pass-19/20 watcher rules.

```text
tests/domains/flora/
├── README.md                                # PROPOSED
├── schema/                                  # schema validation tests
├── source_descriptor/                       # admission gate tests
├── rights/                                  # rights validator tests
├── sensitivity/                             # rare-plant + join-induced deny tests
├── evidence_closure/                        # EvidenceBundle resolution tests
├── temporal/                                # observed/valid/retrieval/release distinct
├── geometry/                                # generalization + redaction transforms
├── policy_deny/                             # exact sensitive geometry deny
├── citation/                                # citation-validation cases
├── release_manifest/                        # ReleaseManifest checks
├── rollback_drill/                          # rollback test harness
└── no_network/                              # no-live-network fixture pipeline

fixtures/domains/flora/
├── README.md                                # PROPOSED
├── valid/                                   # green-path inputs
├── invalid/                                 # negative cases (one per validator)
├── golden/                                  # canonical reference inputs
├── synthetic/                               # synthesized rare-plant cases
└── plants_drift/                            # PLANTS taxa-drift fixtures
```

### 6.6 `packages/domains/flora/`

Reusable flora-typed code (resolvers, normalizers, taxonomy helpers). Anything
that runs once as a workflow step belongs in `tools/` or `pipelines/`, not here
(Directory Rules §7.2).

```text
packages/domains/flora/
├── README.md                                # PROPOSED
├── taxonomy_resolver/                       # PROPOSED  (ITIS/GBIF Backbone)
├── geoprivacy_transformer/                  # PROPOSED  (rare-plant generalization)
├── source_role_resolver/                    # PROPOSED  (per flora source)
└── flora_evidence_projector/                # PROPOSED  (Evidence Drawer payload)
```

### 6.7 `pipelines/domains/flora/` and `pipeline_specs/flora/`

```text
pipelines/domains/flora/
├── README.md                                # PROPOSED
├── ingest/                                  # connector → RAW
├── normalize/                               # RAW → WORK
├── validate/                                # WORK → PROCESSED
├── catalog/                                 # PROCESSED → CATALOG/TRIPLET
├── publish/                                 # CATALOG → PUBLISHED  (governed)
└── rollback/                                # release → rollback target

pipeline_specs/flora/
├── README.md                                # PROPOSED
├── gbif_ingest.yaml                         # PROPOSED
├── inaturalist_ingest.yaml                  # PROPOSED
├── usfws_ecos_ingest.yaml                   # PROPOSED
├── plants_drift_watcher.yaml                # PROPOSED  (paired with CDL pattern)
└── flora_publish_dryrun.yaml                # PROPOSED  (release dry-run)
```

### 6.8 `release/` flora entries

```text
release/
├── candidates/flora/<release_candidate_id>/ # PROPOSED
├── manifests/<release_id>.yaml              # PROPOSED  (release-wide)
├── rollback_cards/<release_id>.yaml         # PROPOSED
└── correction_notices/<notice_id>.yaml      # PROPOSED
```

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 7. Lifecycle alignment (`data/`)

Promotion is a **governed state transition, not a file move** (Directory Rules
§9.1, KFM Operating Law). Flora follows the canonical lifecycle invariant:

> **RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED**

| Phase | Flora path | Required artifacts (PROPOSED) | Failure-closed outcome |
|---|---|---|---|
| Admission → RAW | `data/raw/flora/<source_id>/<run_id>/` | `SourceDescriptor` (role, authority, rights, sensitivity, cadence); payload hash | Not admitted; logged as candidate awaiting steward |
| RAW → WORK | `data/work/flora/<run_id>/` | `TransformReceipt`; `ValidationReport` (working); `PolicyDecision` | Routed to `data/quarantine/flora/<reason>/<run_id>/` |
| RAW/WORK → QUARANTINE | `data/quarantine/flora/<reason>/<run_id>/` | Reason record; quarantine receipt | Never silently promoted |
| WORK → PROCESSED | `data/processed/flora/<dataset_id>/<version>/` | `ValidationReport` pass; `RedactionReceipt` if rare/sensitive; `AggregationReceipt` if applicable | Stay in WORK; structured FAIL |
| PROCESSED → CATALOG/TRIPLET | `data/catalog/domain/flora/`, `data/triplets/graph_deltas/` | `EvidenceBundle`; `CatalogMatrix` entry; STAC/DCAT/PROV records | HOLD at PROCESSED; no public edge |
| CATALOG → PUBLISHED | `data/published/layers/flora/`, `data/published/pmtiles/flora/`, `data/published/api_payloads/flora/` | `ReleaseManifest` + `RollbackCard` + correction path + `ReviewRecord` where required | HOLD at CATALOG; no public surface change |

> [!IMPORTANT]
> **Watcher-as-non-publisher invariant** applies to flora unconditionally:
> watchers (e.g., PLANTS taxa-drift, GBIF source-head, iNaturalist polling) emit
> `SourceIntakeRecord` candidates with `publication_state = WORK_CANDIDATE` into
> `data/quarantine/flora/` or `data/work/flora/`. **They MUST NOT write to**
> `data/processed/`, `data/catalog/`, `data/published/`, or `release/`.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 8. Sensitivity, rights, and join-induced risk

Flora carries two distinct fail-closed dimensions: **rare-species sensitivity**
(intrinsic to the taxon) and **join-induced sensitivity** (emerges when a benign
source is combined with another). Each has a dedicated placement.

| Sensitivity dimension | Trigger | Placement of rule | Placement of receipt |
|---|---|---|---|
| Rare-plant exact geometry | Federal/state listing, NatureServe S1/S2, KDWP SINC, steward flag | `policy/sensitivity/flora/rare_plant_geoprivacy.rego` (PROPOSED) | `data/proofs/evidence_bundle/.../redaction_receipt/` (PROPOSED) |
| Join-induced (PLANTS × GBIF/iNat) | Cross-source join produces poaching-risk surface | `policy/sensitivity/flora/join_induced_sensitivity.rego` (PROPOSED) | `data/receipts/pipeline/.../join_decision/` (PROPOSED) |
| Culturally sensitive plant knowledge | Steward/tribal review flag | `policy/sensitivity/flora/cultural_sensitivity.rego` (PROPOSED); steward review in `release/candidates/flora/` | `data/proofs/.../review_record/` (PROPOSED) |
| Unclear rights | Missing license, missing redistribution class | `policy/rights/flora/` (PROPOSED) | Quarantine: `data/quarantine/flora/rights_unresolved/` |
| Source-role mismatch | Authority cited as observation, etc. | `policy/domains/flora/flora_source_role.rego` (PROPOSED) | `data/quarantine/flora/source_role_mismatch/` (PROPOSED) |

> [!CAUTION]
> **Join-induced sensitivity is not a property of either input alone.** A PLANTS
> county taxa list and a GBIF occurrence dataset can each be public-safe
> individually and become a sensitive rare-plant exposure when joined. Place
> deny rules at the **derived product**, not only at sources, and emit a
> transform receipt in `data/proofs/evidence_bundle/`.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 9. Watcher and connector placement

| Function | Code home | Spec/config home | Output home | Cannot write to |
|---|---|---|---|---|
| GBIF connector | `connectors/gbif/` | per-connector `README.md` + source descriptor | `data/raw/flora/gbif/<run_id>/` or `data/quarantine/flora/` | `data/processed/`, `data/catalog/`, `data/published/`, `release/` |
| iNaturalist connector | `connectors/inaturalist/` | per-connector `README.md` + source descriptor | `data/raw/flora/inaturalist/<run_id>/` | same |
| USFWS ECOS connector | `connectors/usfws/` (PROPOSED) | per-connector `README.md` + source descriptor | `data/raw/flora/usfws_ecos/<run_id>/` | same |
| NatureServe connector | `connectors/natureserve/` (PROPOSED) | per-connector `README.md` + source descriptor | `data/raw/flora/natureserve/<run_id>/` | same |
| KDWP / KBS / KU herbarium connectors | `connectors/kdwp/`, `connectors/kbs/`, `connectors/ku_herbarium/` (PROPOSED) | per-connector `README.md` + source descriptor | `data/raw/flora/<source_id>/<run_id>/` | same |
| PLANTS taxa-drift watcher | `tools/watchers/plants_watch/` (PROPOSED) or `pipelines/watchers/plants/` per ADR | `pipeline_specs/watchers/plants_drift.yaml` (PROPOSED) | `data/work/flora/.../source_intake_record/` (`publication_state = WORK_CANDIDATE`) | `data/published/`, `release/` |
| Watcher-shared tooling | `tools/watchers/` | n/a | n/a | same |

> [!NOTE]
> The PLANTS watcher pattern mirrors the CDL watcher pattern documented in
> Pass-19/20 (sidecars with `spec_hash`, `classmap_version`, ETag,
> Last-Modified, materiality thresholds). Whether watcher code lives under
> `tools/watchers/` or `pipelines/watchers/` is **NEEDS VERIFICATION** — the
> Unified Implementation Manual proposes `pipeline_specs/watchers/` for specs,
> but the executable home for watcher code awaits ADR.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 10. Cross-lane and cross-cutting files

Per Directory Rules §12 Multi-domain and cross-cutting subsection, files that
**legitimately span domains** go under the **lowest common responsibility root
without a domain segment**.

| Cross-lane concern | Correct home | Wrong home |
|---|---|---|
| Habitat × Flora geometry validator | `tools/validators/habitat_flora/` (PROPOSED) | `tools/validators/domains/flora/` |
| Flora × Fauna pollinator/food-web join | `schemas/contracts/v1/biodiversity/` (PROPOSED) | `schemas/contracts/v1/domains/flora/` only |
| Flora × Soil substrate context | `contracts/domains/flora/HabitatAssociation.md` if flora-owned; or shared semantic doc under `contracts/biodiversity/` (PROPOSED) | A duplicate file in `contracts/domains/soil/` |
| Flora × Hazards vegetation stress | `pipelines/biodiversity/vegetation_stress/` (PROPOSED) | `pipelines/domains/flora/hazards/` |
| Generic redaction receipt | `schemas/contracts/v1/release/redaction_receipt.schema.json` | `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json` (flora-flavored crosswalk is OK; do not duplicate the generic) |

> [!IMPORTANT]
> Flora **owns** plant taxa, plant occurrences, vegetation communities,
> invasive plants, phenology, range and habitat associations. Flora **does
> not own** habitat patches (Habitat), animal records (Fauna), crops
> (Agriculture), or land tenure (People/Land). Cross-lane files that touch
> non-flora-owned objects must be placed by ownership, not topic.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 11. Compatibility, drift, and migration notes

Compatibility roots exist for legacy/mirror/external-export/transitional content
(Directory Rules §8). For flora, the relevant ones are:

| Compatibility root | Canonical home | Class | Action for flora content |
|---|---|---|---|
| `contracts/<domain>/<x>.schema.json` if present | `schemas/contracts/v1/domains/flora/` | `legacy` / `CONFLICTED` | Migrate per ADR-0001; do not author new flora schemas under `contracts/` |
| `policies/` if present | `policy/` | `mirror` / `legacy` | New flora policy lands under `policy/` only |
| `jsonschema/` if present | `schemas/` | `mirror` / `legacy` | Flora schemas land under `schemas/contracts/v1/domains/flora/` only |
| `data/manifests/` | `release/manifests/` | OPEN per Directory Rules §18 | Pending ADR; this plan defers to the eventual resolution |

> [!NOTE]
> **Runbook subfolder vs. flat-prefix naming.** Existing runbook precedent
> diverges: the Whole-UI Governed AI Expansion Report proposes flat-prefix
> names (e.g., `docs/runbooks/ui_LOCAL_DEV.md`), while a published flora-adjacent
> runbook uses a subfolder (`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`).
> **Status: NEEDS VERIFICATION via ADR.** This plan reserves both
> `docs/runbooks/flora_*.md` and `docs/runbooks/flora/*.md` as PROPOSED until
> the convention is locked. Any flora runbook created before the ADR should
> link back here and flag the convention choice in its meta block.

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 12. Open questions & verification backlog

| # | Item | Evidence that would settle it | Status |
|---|---|---|---|
| 1 | Existence of `docs/domains/flora/` and surrounding files in the live repo | Mounted-repo directory listing | NEEDS VERIFICATION |
| 2 | Schema home verified under `schemas/contracts/v1/domains/flora/` for at least one object | Mounted file + ADR-0001 reference | NEEDS VERIFICATION |
| 3 | Whether `policy/sensitivity/flora/` and `policy/domains/flora/` both exist or are merged | Mounted-repo `policy/` listing + per-root README | NEEDS VERIFICATION |
| 4 | Flora connector identities for KDWP, KBS, KU herbarium (paths and source IDs) | Source descriptor entries; mounted `connectors/` | NEEDS VERIFICATION |
| 5 | PLANTS watcher executable home (`tools/watchers/` vs. `pipelines/watchers/`) | ADR + mounted home | NEEDS VERIFICATION |
| 6 | Flora runbook naming (`flora_*.md` flat vs. `flora/*.md` subfolder) | ADR; existing repo convention | OPEN |
| 7 | Whether `data/manifests/` is a real sibling of `data/proofs/` / `data/receipts/` for flora release artifacts | Directory Rules §18 open question; ADR | OPEN |
| 8 | Exact rare-plant generalization radius and steward review thresholds | Mounted `policy/sensitivity/flora/`; steward decisions | NEEDS VERIFICATION |
| 9 | Whether `policy/release/flora/` is a separate lane or composed via `policy/release/` only | Directory Rules + ADR | NEEDS VERIFICATION |
| 10 | Final list of viewing products published under `data/published/layers/flora/` | Flora thin-slice spec + release manifest fixtures | NEEDS VERIFICATION |
| 11 | Naming continuity with neighboring standard docs (e.g., is `PROV.md` or `PROVENANCE.md` the canonical filename) | ADR (already flagged elsewhere) | OPEN |
| 12 | Whether `data/registry/sources/flora/` or `data/registry/flora/` is canonical for flora source descriptors | Mounted-repo `data/registry/` layout + Directory Rules §9.1 | NEEDS VERIFICATION |

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## 13. Related docs

- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Directory Rules, §12 Domain Placement Law
- [`docs/domains/README.md`](../README.md) — Domain lane index (PROPOSED)
- [`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`](../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) — Companion runbook precedent
- [`docs/standards/PROV.md`](../../standards/PROV.md) — W3C PROV-O / PAV profile
- [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) — PMTiles delivery profile
- [`docs/standards/OGC-API-TILES.md`](../../standards/OGC-API-TILES.md) — OGC API Tiles profile
- [`docs/standards/OAI-PMH.md`](../../standards/OAI-PMH.md) — OAI-PMH harvest governance
- [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) — ISO 19115 crosswalk
- `docs/adr/ADR-0001-schema-home.md` (PROPOSED reference) — canonical schema home
- `docs/registers/DRIFT_REGISTER.md` (PROPOSED reference) — for any flora drift entries
- `docs/registers/VERIFICATION_BACKLOG.md` (PROPOSED reference) — for items 1–12 above

[⤴ Back to top](#-flora-domain--file-system-plan)

---

## Appendix A — Full PROPOSED path manifest

<details>
<summary>Complete, sorted manifest of every flora-domain path proposed in this plan</summary>

```text
# docs
docs/domains/flora/
docs/domains/flora/README.md
docs/domains/flora/FILE_SYSTEM_PLAN.md           # this document
docs/domains/flora/OBJECT_FAMILIES.md
docs/domains/flora/SOURCE_FAMILIES.md
docs/domains/flora/SENSITIVITY_POSTURE.md
docs/domains/flora/THIN_SLICE_PLAN.md
docs/domains/flora/CROSS_LANE_NOTES.md
docs/runbooks/flora_*.md      OR     docs/runbooks/flora/*.md   # NEEDS VERIFICATION via ADR

# contracts (object meaning)
contracts/domains/flora/README.md
contracts/domains/flora/PlantTaxon.md
contracts/domains/flora/FloraTaxonCrosswalk.md
contracts/domains/flora/FloraOccurrence.md
contracts/domains/flora/SpecimenRecord.md
contracts/domains/flora/RarePlantRecord.md
contracts/domains/flora/VegetationCommunity.md
contracts/domains/flora/InvasivePlantRecord.md
contracts/domains/flora/PhenologyObservation.md
contracts/domains/flora/RangePolygon.md
contracts/domains/flora/DistributionSurface.md
contracts/domains/flora/HabitatAssociation.md
contracts/domains/flora/BotanicalSurvey.md
contracts/domains/flora/RestorationPlanting.md
contracts/domains/flora/RedactionReceipt.flora.md

# schemas (machine shape)
schemas/contracts/v1/domains/flora/plant_taxon.schema.json
schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json
schemas/contracts/v1/domains/flora/flora_occurrence.schema.json
schemas/contracts/v1/domains/flora/specimen_record.schema.json
schemas/contracts/v1/domains/flora/rare_plant_record.schema.json
schemas/contracts/v1/domains/flora/vegetation_community.schema.json
schemas/contracts/v1/domains/flora/invasive_plant_record.schema.json
schemas/contracts/v1/domains/flora/phenology_observation.schema.json
schemas/contracts/v1/domains/flora/range_polygon.flora.schema.json
schemas/contracts/v1/domains/flora/distribution_surface.flora.schema.json
schemas/contracts/v1/domains/flora/habitat_association.flora.schema.json
schemas/contracts/v1/domains/flora/botanical_survey.schema.json
schemas/contracts/v1/domains/flora/restoration_planting.schema.json
schemas/contracts/v1/domains/flora/redaction_receipt.flora.schema.json

# policy
policy/domains/flora/README.md
policy/domains/flora/flora_rights.rego
policy/domains/flora/flora_source_role.rego
policy/domains/flora/flora_taxonomy_resolution.rego
policy/domains/flora/flora_publication_gate.rego
policy/sensitivity/flora/rare_plant_geoprivacy.rego
policy/sensitivity/flora/join_induced_sensitivity.rego
policy/sensitivity/flora/exact_geometry_deny.rego
policy/sensitivity/flora/cultural_sensitivity.rego
policy/rights/flora/...
policy/release/flora/...

# tests
tests/domains/flora/README.md
tests/domains/flora/schema/
tests/domains/flora/source_descriptor/
tests/domains/flora/rights/
tests/domains/flora/sensitivity/
tests/domains/flora/evidence_closure/
tests/domains/flora/temporal/
tests/domains/flora/geometry/
tests/domains/flora/policy_deny/
tests/domains/flora/citation/
tests/domains/flora/release_manifest/
tests/domains/flora/rollback_drill/
tests/domains/flora/no_network/

# fixtures
fixtures/domains/flora/README.md
fixtures/domains/flora/valid/
fixtures/domains/flora/invalid/
fixtures/domains/flora/golden/
fixtures/domains/flora/synthetic/
fixtures/domains/flora/plants_drift/

# packages
packages/domains/flora/README.md
packages/domains/flora/taxonomy_resolver/
packages/domains/flora/geoprivacy_transformer/
packages/domains/flora/source_role_resolver/
packages/domains/flora/flora_evidence_projector/

# pipelines
pipelines/domains/flora/README.md
pipelines/domains/flora/ingest/
pipelines/domains/flora/normalize/
pipelines/domains/flora/validate/
pipelines/domains/flora/catalog/
pipelines/domains/flora/publish/
pipelines/domains/flora/rollback/

# pipeline_specs
pipeline_specs/flora/README.md
pipeline_specs/flora/gbif_ingest.yaml
pipeline_specs/flora/inaturalist_ingest.yaml
pipeline_specs/flora/usfws_ecos_ingest.yaml
pipeline_specs/flora/plants_drift_watcher.yaml
pipeline_specs/flora/flora_publish_dryrun.yaml
pipeline_specs/watchers/plants_drift.yaml

# connectors (source-specific; flora-tagged via source_id)
connectors/gbif/...
connectors/inaturalist/...
connectors/usfws/...
connectors/natureserve/...
connectors/kdwp/...
connectors/kbs/...
connectors/ku_herbarium/...

# data (lifecycle; promotion is a state transition, not a file move)
data/raw/flora/<source_id>/<run_id>/
data/work/flora/<run_id>/
data/quarantine/flora/<reason>/<run_id>/
data/processed/flora/<dataset_id>/<version>/
data/catalog/domain/flora/
data/triplets/graph_deltas/                              # cross-domain, flora-tagged
data/receipts/{ingest,validation,pipeline,ai,release}/   # cross-domain, flora-tagged
data/proofs/{evidence_bundle,proof_pack,validation_report,citation_validation}/
data/published/layers/flora/
data/published/pmtiles/flora/
data/published/api_payloads/flora/
data/registry/sources/flora/
data/registry/source_descriptors/<flora-source-ids>/
data/rollback/flora/<release_id>/

# release
release/candidates/flora/<release_candidate_id>/
release/manifests/<release_id>.yaml
release/rollback_cards/<release_id>.yaml
release/correction_notices/<notice_id>.yaml
```

</details>

[⤴ Back to top](#-flora-domain--file-system-plan)

---

> [!NOTE]
> **Lineage and citations.** This plan is grounded in Directory Rules §§3–13
> (placement law), §§9.1 and 24.x (lifecycle and catalog), the KFM Encyclopedia
> §7.6 (Flora dossier), the Domains Culmination Atlas v1.1 chapter 8 (Flora),
> the Unified Implementation Architecture Build Manual §§3.4–3.6 and 6.5 (root
> plan and Flora lane), Pass 20 dossier (PLANTS/CDL watcher patterns, source
> roles, sensitivity discipline), and the Whole-UI Governed AI Expansion Report
> (runbook lineage). Every concrete path is **PROPOSED** until verified
> against a mounted repository. No path here may be cited as repo state.

---

**Related docs:** [Directory Rules](../../doctrine/directory-rules.md) ·
[Domains README](../README.md) ·
[Fauna Source Refresh Runbook](../../runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md) ·
[PROV.md](../../standards/PROV.md) ·
[PMTILES.md](../../standards/PMTILES.md)

**Last updated:** 2026-05-16 · [⤴ Back to top](#-flora-domain--file-system-plan)
