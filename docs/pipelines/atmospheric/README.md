---
title: "🌤️ Kansas Frontier Matrix — Atmospheric Pipelines Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmospheric/README.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Pipelines Domain Index"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256-or-null>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../releases/v11.2.4/atmospheric-pipelines-telemetry.json"
telemetry_schema: "../../schemas/telemetry/atmospheric-pipelines-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "atmospheric"
  applies_to:
    - "etl"
    - "streaming-ingest"
    - "watermarks"
    - "windowing"
    - "regridding"
    - "stac"
    - "graph"
    - "telemetry"
    - "story-nodes"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (with sovereign/critical-infra joins masked)"
classification: "Public / Internal (governed pipelines)"
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Environmental Modelling / Atmospheric Data"
indigenous_rights_flag: true
redaction_required: true

doc_uuid: "urn:kfm:doc:pipelines:atmospheric:index:v11.2.4"
semantic_document_id: "kfm-pipelines-atmospheric-index"
event_source_id: "ledger:docs/pipelines/atmospheric/README.md"
machine_extractable: true
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified atmospheric claims"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next atmospheric pipelines reorganization"
---

<div align="center">

# 🌤️ **Kansas Frontier Matrix — Atmospheric Pipelines Index**  
`docs/pipelines/atmospheric/README.md`

**Purpose**  
Act as the **governed index** for all **atmospheric pipelines** in KFM — including NEXRAD, HRRR, and related patterns — and connect them to STAC/DCAT catalogs, Neo4j, telemetry, and Story Nodes.

</div>

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
├── 📁 docs/
│   └── 📁 pipelines/
│       └── 📁 atmospheric/
│           ├── 📄 README.md                      # ← This file (atmospheric pipelines index)
│           ├── 📁 hrrr/
│           │   ├── 📄 README.md                  # HRRR domain pipelines index
│           │   └── 📁 windowing/
│           │       ├── 📄 README.md              # HRRR Zarr windowing & subsetting pattern
│           │       ├── 📁 examples/
│           │       │   ├── 📄 bbox-basic.md
│           │       │   ├── 📄 polygon-windowing.md
│           │       │   └── 📄 stac-subset-example.json
│           │       └── 📁 tests/
│           │           ├── 📄 test-windowing-shapes.py
│           │           ├── 📄 test-stac-provenance.py
│           │           └── 📁 fixtures/
│           └── 📁 radar/
│               └── 📁 nexrad/
│                   ├── 📄 event-time-watermarks.md   # NEXRAD ingest watermark standard
│                   ├── 📁 watermarks/
│                   │   └── 📄 finalization-pattern.md# Preview vs final volume pattern
│                   ├── 📁 qc/
│                   │   ├── 📄 tilt-detection.md
│                   │   ├── 📄 avset-rules.md
│                   │   └── 📄 wedges.md
│                   └── 📁 lineage/
│                       └── 📄 prov-patterns.md       # Radar PROV & OpenLineage patterns
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 atmospheric/
│           ├── 📁 hrrr/
│           │   └── 📁 windowing/
│           │       ├── 📄 run_window.py             # Time/space windowing entrypoint
│           │       ├── 📄 run_state.py              # Run-state & idempotency keys
│           │       ├── 📄 stac_emit.py              # STAC processing:subset emitter
│           │       └── 📄 config.py                 # HRRR datasets/versions/selectors
│           └── 📁 radar/
│               └── 📁 nexrad/
│                   ├── 📄 ingest.py                 # Event-time keyed ingest
│                   ├── 📄 qc.py                     # Tilt/AVSET/wedge metrics
│                   ├── 📄 watermark_gate.py         # Implements this watermark standard
│                   ├── 📄 stac_emit.py              # Radar STAC item creation
│                   └── 📄 graph_emit.py             # Neo4j upserts for RadarVolume/QC
└── 📁 data/
    └── 📁 atmospheric/
        ├── 📁 hrrr/
        │   ├── 📁 zarr_index/                       # Optional HRRR Zarr index metadata
        │   └── 📁 subsets/                          # Materialized HRRR windows
        └── 📁 radar/
            └── 📁 nexrad/
                ├── 📁 raw/                          # Raw Level-II/III blobs
                ├── 📁 work/                         # Decoded headers/tilts
                ├── 📁 processed/                    # Volume-level composites
                └── 📁 stac/                         # STAC Collections/Items
```

---

## 📘 Overview

The **Atmospheric Pipelines** domain covers:

- **Radar** pipelines (NEXRAD Level-II/III), with strict event-time watermarking and QC, and  
- **HRRR** pipelines (Zarr-based forecast fields), with deterministic windowing and subsetting.

This index:

- Provides a single **navigation point** for atmospheric pipeline documentation and code,  
- Connects atmospheric patterns to KFM’s global ETL, catalog, and governance patterns,  
- Ensures that all atmospheric pipelines are:

  - Deterministic and replayable,  
  - WAL- and idempotent-node compliant,  
  - STAC/DCAT/PROV-aligned,  
  - FAIR+CARE-aware and sovereignty-respecting.

---

## 🧭 Context

Atmospheric data in KFM is used to:

- Model and understand **severe weather**, drought, and flood risk,  
- Provide forcing for **hydrology**, **ecology**, and **energy** analyses,  
- Power Story Nodes that explain **when and how** atmospheric events shaped Kansas.

Key sources:

- **NEXRAD** — high-frequency radar volumes, ingest with event-time watermarks, AVSET-aware QC.  
- **HRRR** — high-resolution forecast fields, windowed around Kansas AOIs and specific narrative needs.

Because of the spatial and temporal density of atmospheric data, KFM emphasizes:

- **Windowing**, not bulk ingestion,  
- Catalogs with rich **processing:subset** metadata,  
- Tight integration with **event-driven deterministic ingest** and **reliability test suites**.

---

## 🧱 Architecture (Atmospheric Pipelines)

At a high level, atmospheric pipelines follow:

```text
Trigger → Ingest → QC → Watermark/Window → STAC/DCAT → Graph → Tiles/Views
```

### NEXRAD (Radar)

- Event-driven ingest (S3/Kafka).  
- Header decode → tilt enumeration → QC → **Event-Time Watermark Gate**.  
- Final volumes promoted only when watermark & QC rules are satisfied.  
- STAC Items record `kfm.radar.*` and watermark metadata; DCAT derived.  
- Graph nodes for `:RadarVolume`, `:QCReport`, `:Watermark`.

### HRRR (Zarr)

- Zarr store is treated as a **static dataset version**.  
- Windowing pattern selects bbox/polygon + forecast hour + variables.  
- Run-state key prevents duplicate work and ensures deterministic subsets.  
- STAC `processing:subset` metadata documents each subset.  
- Graph nodes for `:AtmosWindow`, `:AtmosDatasetVersion` tied to hydrology & risk nodes.

Atmospheric pipelines are expected to reuse:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`  
- `docs/pipelines/patterns/idempotent-safety-governance.md`  
- `docs/pipelines/reliability/tests/etl-determinism-suite.md`

---

## 📦 Data & Metadata

Atmospheric outputs must:

- Live under `data/atmospheric/**`, partitioned by:

  - Source (e.g., `hrrr`, `radar`),  
  - Version (dataset version or release),  
  - Derived window/volume identifiers.

- Be cataloged via STAC Collections and Items with:

  - Event-time (`datetime`),  
  - Spatial footprints (bbox/polygon),  
  - `processing:subset` or `kfm.radar.*` fields as appropriate,  
  - Catalog-level references to energy/carbon telemetry where heavy runs are involved.

- Have corresponding DCAT records derived from STAC using KFM’s STAC→DCAT derivation rules.

---

## 🧪 Validation & CI/CD

Atmospheric pipelines must pass:

- **NEXRAD-specific tests**:

  - Event-time watermark invariants (no out-of-order promotion),  
  - QC logic for AVSET, tilts, wedges, and partial volumes,  
  - Replay tests verifying WAL recovery & determinism.

- **HRRR-specific tests**:

  - Shape and coordinate checks (window extents),  
  - STAC `processing:subset` JSON validation,  
  - Idempotent run-state behavior.

- **Global reliability tests** (see `etl-determinism-suite.md`):

  - Replayability (R1/R2),  
  - WAL recovery (W1/W2),  
  - Idempotent upserts (I1/I2),  
  - Mixed load behavior (L1).

CI workflows should gate merges into atmospheric pipelines on:

- Tests under `docs/pipelines/atmospheric/**/tests/`,  
- Reliability tests in `src/tests/reliability/**`,  
- Telemetry schema conformance.

---

## 🧠 Story Node & Focus Mode Integration

Atmospheric pipelines feed Story Nodes and Focus Mode by:

- Supplying **time-scoped layers** (e.g., HRRR windows, NEXRAD volumes).  
- Representing severe weather events, heat waves, and atmospheric drivers in:

  - History Story Nodes (e.g., 2007 Greensburg tornado context via radar),  
  - Hydrology Story Nodes (e.g., flash flood narratives with HRRR and NEXRAD),  
  - Energy Story Nodes (e.g., cooling load narratives).

Responsibilities:

- When atmospheric data intersects **sensitive geographies** (Tribal lands, critical infrastructure):

  - Apply masking/generalization per FAIR+CARE and sovereignty policies,  
  - Document such behavior in STAC and PROV,  
  - Ensure that public Story Nodes respect these protections.

Atmospheric domain maintainers should coordinate with Story Node boards to:

- Provide **documented endpoints** (datasets, tiles, STAC IDs) for narrative builders.  
- Offer guidance on **typical AOIs**, time windows, and variables for common narratives.

---

## ⚖ FAIR+CARE & Governance

Atmospheric pipelines:

- Are generally **low-risk** in isolation (meteorological fields).  
- May become higher risk when **joined** with:

  - Critical infrastructure,  
  - Sensitive demographic distributions,  
  - Sovereign lands & cultural sites.

Governance requirements:

- Use FAIR+CARE guidance (`FAIRCARE-GUIDE.md`) and sovereignty policies for:

  - Derived products that might expose vulnerable populations,  
  - Story Nodes combining atmo data with sensitive overlays.

- Include energy/carbon telemetry for heavy workloads (HRRR windows, NEXRAD ingest) to:

  - Support sustainability goals,  
  - Enable carbon-aware scheduling (future roadmap).

---

## 🕰️ Version History

| Version | Date       | Notes                                                                 |
|--------:|------------|-----------------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Initial governed atmospheric pipelines index; aligned with HRRR windowing & NEXRAD watermark patterns. |

---

## 🛡️ Governance Footer

This document is governed by:

- **Atmospheric Working Group**  
- **FAIR+CARE Council**  
- **KFM Documentation & Pipeline Standards**

All modifications MUST:

- Maintain `markdown_protocol_version` alignment,  
- Update `doc_integrity_checksum`, `commit_sha`, and `previous_version_hash`,  
- Pass **docs-lint**, **schema-lint**, and **telemetry-lint** checks in CI.

<div align="center">

🌤️ **Kansas Frontier Matrix — Atmospheric Pipelines**  

[📘 Docs Root](../../README.md) ·  
[🌪️ HRRR Pipelines](hrrr/README.md) · [🌩️ NEXRAD Watermarks](radar/nexrad/event-time-watermarks.md) ·  
[⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
