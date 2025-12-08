---
title: "🌩️ Kansas Frontier Matrix — Event-Driven Pipelines Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/event-driven/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Pipelines Board · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Backward compatible with v11.0.x event-driven pipelines"

status: "Active"
doc_kind: "Module Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<sha256-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/pipeline-telemetry.json"
telemetry_schema: "schemas/telemetry/event-driven-pipelines-v3.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-compliant (auto-mask on; sovereign overlays governed)"
sensitivity: "Mixed (public + potentially sensitive joins)"
classification: "Public / Internal (architectural)"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/patterns/event-driven-deterministic-ingest.md@v11.2.4"
  - "docs/pipelines/event-driven/overview.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:event-driven:readme:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "event-driven-module-readme-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "multi-domain"
  applies_to:
    - "etl"
    - "streaming"
    - "stac"
    - "dcat"
    - "graph"
    - "provenance"
    - "telemetry"
    - "story-nodes"
    - "focus-mode"
  impacted_modules:
    - "docs/pipelines/event-driven"
    - "docs/pipelines/soil"
    - "docs/pipelines/atmo"
    - "src/pipelines/soil/*"
    - "src/pipelines/atmo/*"
    - "data/raw/*"
    - "data/processed/*"
    - "data/stac/*"
    - "dist/provenance/*"
---

<div align="center">

# 🌩️ **Kansas Frontier Matrix — Event-Driven Pipelines Module**  
`docs/pipelines/event-driven/README.md`

**Atmospheric Streams · Soil Systems · Deterministic ETL → STAC/DCAT/PROV → Graph → Tiles → Focus Mode**

</div>

---

## 🗂️ Module Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 event-driven/
        📄 README.md                      # ← This file (module index)
        📄 overview.md                    # Architecture overview for event-driven pipelines
        📁 soils/
        │   📄 triggers.md                # Soil event sources (SDA, parcels, boundaries)
        │   📄 transforms.md              # Canonical soil transforms (CRS, units, stratigraphy)
        │   📄 validations.md             # Schema, geometry, stratigraphy, CARE checks
        │   📄 publication.md             # STAC/DCAT, tiles, graph mapping
        📁 atmo/
        │   📄 triggers.md                # Atmospheric triggers (NEXRAD, HRRR, etc.)
        │   📄 transforms.md              # Grid homogenization, windows, derived fields
        │   📄 validations.md             # Coverage, QC, temporal checks
        │   📄 publication.md             # STAC, time tiles, graph integration
        📁 notes/
            📄 onboarding-checklist.md    # How to onboard a new event-driven pipeline
            📄 ops-runbook.md            # Shared operational notes (SLOs, incident playbooks)

📁 docs/
└── 📁 pipelines/
    └── 📁 patterns/
        📄 event-driven-deterministic-ingest.md  # Canonical shared pattern for all event-driven pipelines
```

---

## 📘 Overview

The **Event-Driven Pipelines Module** coordinates all KFM pipelines that are triggered by **external events** rather than purely scheduled cadences, including:

- **Atmospheric pipelines**  
  - NEXRAD Level-II, HRRR, other radar/model feeds.

- **Soil pipelines**  
  - USDA SDA (`sda-async`, `sda-weekly`), parcel updates, boundary-driven refreshes.

This module:

- Ties individual pipeline docs to a **single architectural pattern**,  
- Enforces **deterministic, idempotent, WAL-safe** behavior,  
- Ensures **STAC/DCAT/PROV alignment** and **FAIR+CARE** governance,  
- Defines how event-driven pipelines surface into **Story Nodes** and **Focus Mode**.

For the high-level architecture, see:

- `overview.md` — **Event-Driven Atmospheric & Soil Pipelines Overview**  
- `../patterns/event-driven-deterministic-ingest.md` — **canonical pattern spec**

---

## 🧩 Module Components

### 1. Architecture Overview

- **File:** `overview.md`  
- **Role:**  
  - Describes the unified event-driven shape:
    ```text
    Trigger → Ingest → Normalize → Validate → Transform → Publish → Graph → Story Nodes
    ```
  - Explains:
    - Trigger sources and fallbacks,  
    - Idempotent run keys & WAL,  
    - STAC/DCAT/PROV expectations,  
    - Telemetry & reproducibility requirements.

All domain-specific event-driven docs (soil/atmo) are **subordinate** to the rules in `overview.md`.

---

### 2. Soil Event-Driven Docs (`soils/`)

The `soils/` submodule specializes event-driven logic for soil systems:

- `triggers.md`  
  - USDA SDA metadata changes,  
  - Parcel & boundary updates,  
  - Monthly reconciliation windows.

- `transforms.md`  
  - CRS harmonization,  
  - Attribute/unit normalization,  
  - Stratigraphy linkage,  
  - H3 hex summarization.

- `validations.md`  
  - Schema continuity vs prior releases,  
  - Geometry validity and area sanity,  
  - Stratigraphy checks (depth ordering, non-overlap),  
  - CARE-aware behaviors when soil joins sensitive layers.

- `publication.md`  
  - Soil STAC Collections/Items,  
  - DCAT derivation,  
  - Tiles & Neo4j `DatasetVersion` nodes,  
  - Hooks for Story Nodes about soil changes.

All of these build on the **SDA patterns** in:

- `docs/pipelines/soil/sda-async/README.md`  
- `docs/pipelines/soil/sda-weekly/README.md`

---

### 3. Atmospheric Event-Driven Docs (`atmo/`)

The `atmo/` submodule handles streaming atmospheric data:

- `triggers.md`  
  - S3 events (NEXRAD/HRRR),  
  - Distributor webhooks,  
  - Cron fallbacks.

- `transforms.md`  
  - Spatial/temporal clipping to KFM AOIs,  
  - Grid homogenization and derived fields,  
  - Rolling windows (1h/3h/24h) for accumulations.

- `validations.md`  
  - Temporal monotonicity checks,  
  - Coverage thresholds and NaN budgets,  
  - QC-flag consistency,  
  - NEXRAD-specific watermark and finalization checks.

- `publication.md`  
  - Time-enabled tiles for MapLibre/Cesium,  
  - STAC Collections/Items for atmospheric fields,  
  - Neo4j lineage nodes,  
  - Story Node snapshots for severe weather, floods, etc.

For NEXRAD watermarks and finalization, see:

- `docs/pipelines/atmo/nexrad/watermarks/README.md`  
- `docs/pipelines/atmo/nexrad/watermarks/finalization-pattern.md`

---

### 4. Shared Pattern Reference

The **shared behavior** for all event-driven pipelines is defined in:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`

All docs under `event-driven/` are **concrete specializations** of this pattern and must not:

- Violate the idempotent/WAL contracts, or  
- Define incompatible provenance or catalog semantics.

---

## 🧭 Onboarding a New Event-Driven Pipeline (Checklist)

New pipelines (soil or atmospheric) that react to events must:

1. **Choose a trigger model**  
   - Cloud object events, webhooks, or scheduled fallback.  
   - Define the `RunEvent` schema (including `source_uri`, `content_hash`, `time_window`).

2. **Implement the event-driven pattern**  
   - Idempotency keys (`blake3(source_uri|content_hash|time_window)`),  
   - WAL logging,  
   - Deterministic transforms & seeds.

3. **Define STAC & graph mapping**  
   - Collection & Item structure,  
   - Asset layout,  
   - Neo4j node/relationship schema.

4. **Add module docs** under `event-driven/`  
   - Extend `soils/` or `atmo/` (or add a new domain folder if needed),  
   - Document transforms, validations, and publication specifics.

5. **Wire CI & telemetry**  
   - Add validation workflows (QA, STAC/PROV checks),  
   - Emit telemetry conforming to `event-driven-pipelines-v3.json`.

6. **Register in the metadata & provenance registry**  
   - Add an `analysis_id` / `pipeline_id` entry to the analytical metadata registry,  
   - Link to PROV bundles and audit reports.

---

## 🧪 Governance, QA & CI Expectations

The Event-Driven Pipelines Module is subject to:

- Root governance: `docs/standards/governance/ROOT-GOVERNANCE.md`  
- FAIR+CARE governance and IDGB oversight for sensitive overlays.  

Minimum expectations:

- CI checks for:
  - Idempotency & replay determinism,  
  - WAL integrity,  
  - STAC/DCAT & PROV correctness,  
  - Telemetry coverage,  
  - Domain QA (soil/atmo-specific validations).

- Governance reviews for:
  - CARE-sensitive data joins,  
  - Changes to finalization delays (e.g., NEXRAD watermarks),  
  - Major schema or behavior changes.

Any pipeline that fails these expectations is **not allowed** to be used in Focus Mode or Story Nodes until remediated.

---

## 🕰️ Version History

| Version  | Date       | Author / Steward                 | Summary                                                         |
|----------|------------|----------------------------------|-----------------------------------------------------------------|
| v11.2.4  | 2025-12-07 | Pipelines Board · FAIR+CARE Council | Initial event-driven module guide aligned with KFM-MDP v11.2.4. |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  

[🌩️ Event-Driven Overview](./overview.md) ·  
[📐 Event-Driven Pattern](../patterns/event-driven-deterministic-ingest.md) ·  
[🌱 Soil Pipelines](../soil/README.md) · [🌩️ Atmospheric Pipelines](../atmo/README.md) ·  
[⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🏠 Monorepo Root](../../README.md)

</div>