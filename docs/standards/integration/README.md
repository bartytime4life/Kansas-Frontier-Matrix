---
title: "🔗 Kansas Frontier Matrix — Integration Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/integration/README.md"
version: "v11.2.6"
last_updated: "2026-01-12"
review_cycle: "Annual · FAIR+CARE Council + Architecture Board"
status: "Active / Enforced"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-integration-index-v11.json"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

doc_kind: "Standards Index"
intent: "integration-standards-index"
semantic_document_id: "kfm-standards-integration-index"
doc_uuid: "urn:kfm:standards:integration:index:v11.2.6"
event_source_id: "ledger:docs/standards/integration/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public Standard"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Interoperability · Governance Enforced"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Kansas Frontier Matrix — Integration Standards Index (v11)**  
`docs/standards/integration/README.md`

**Purpose**  
This README is the **authoritative index** for KFM’s **integration standards**: the governed “interop surface” that connects KFM’s internal pipeline to external geospatial and metadata ecosystems (OGC, SDI, STAC, DCAT, PROV, GeoSPARQL/OWL‑Time, and JSON‑LD).

[![Status: Active](https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen)]()
[![STAC](https://img.shields.io/badge/STAC-1.x-0b7285)]()
[![DCAT](https://img.shields.io/badge/DCAT-3.0-1c7ed6)]()
[![PROV](https://img.shields.io/badge/PROV--O-Lineage-343a40)]()
[![OpenAPI](https://img.shields.io/badge/OpenAPI-Contract--First-2f9e44)]()
[![WCAG](https://img.shields.io/badge/WCAG-2.1%20AA%2B-blueviolet)]()
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue)]()

</div>

---

## 📘 Overview

### What “integration standards” mean in KFM 🧩

Integration standards define **how KFM data + evidence becomes safely reusable** outside the repo and across tooling:

- **Data formats**: GeoJSON (vector), Cloud‑Optimized GeoTIFF (COG) (raster), and other interoperable assets (e.g., 3D Tiles) 📦  
- **Metadata catalogs**: STAC (assets), DCAT (dataset/distribution discovery), PROV‑O (lineage) 🧾  
- **Semantics**: GeoSPARQL + OWL‑Time + JSON‑LD contexts (plus domain ontology crosswalk patterns) 🧠  
- **Service surfaces**: REST (OpenAPI) + GraphQL, and optional compatibility layers (e.g., OGC API – Features / WMS/WFS) 🌐  
- **Governance**: FAIR+CARE, sovereignty protection, and “no sensitive leakage” constraints ⚖️

### Non‑negotiable pipeline ordering 🚦

> **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

**Integration standards live at the boundaries** between these stages and must never introduce shortcuts that bypass catalogs, provenance, or the API boundary.

### Contract‑first + evidence‑first (how v13 thinking shapes v11 interop) 🧾➡️✅

Even though this index is versioned as **v11**, KFM’s current direction emphasizes:

- **Contract‑first**: schemas and API specs are first‑class repo artifacts; changes trigger compatibility/version checks.  
- **Evidence‑first**: catalogs + provenance are produced before interpretation or narrative.

This index aligns integration work to those constraints so external interoperability does not weaken trust.

---

## 🗂️ Directory Layout

This directory provides the **documentation + mapping assets** that define integration behavior. Some entries may be **planned** if a referenced document has not been committed yet.

~~~text
📁 docs/
  📁 standards/
    📁 integration/
      📄 README.md                         # This file — integration standards index ✅
      📄 MASTER-OGC-SDI-INTEGRATION.md     # SDI / OGC alignment master spec (planned)
      📁 ogc/                              # OGC API deep-dives (planned/active as added)
      │  ├─ 📄 ogc_api_features_integration.md
      │  ├─ 📄 ogc_api_records_integration.md
      │  ├─ 📄 ogc_api_tiles_integration.md
      │  └─ 📄 ogc_api_coverages_integration.md
      📁 mapping/                          # Crosswalks (planned/active as added)
      │  ├─ 📄 stac_to_ogc_records.md
      │  ├─ 📄 dcat_to_ogc_records.md
      │  └─ 📄 kfm_ontology_to_ogc.md
      📁 test_vectors/                     # Example payloads + expected mappings (recommended)
         ├─ 🧾 stac_examples/
         ├─ 🧾 dcat_examples/
         └─ 🧾 ogc_examples/

📁 schemas/                                # Contract artifacts (repo-root; required for contract-first)
  📁 stac/                                 # STAC validation schemas / profiles
  📁 dcat/                                 # DCAT validation schemas / profiles
  📁 prov/                                 # PROV validation schemas / profiles
  📁 ogc/                                  # OGC contract/schema helpers (as needed)
  📁 jsonld/                               # JSON-LD contexts (as needed)

📁 data/                                   # Published boundary artifacts (repo-root; canonical homes)
  📁 processed/                            # Produced assets (GeoJSON, COG, 3D Tiles, etc.)
  📁 stac/                                 # STAC catalogs/items
  📁 catalog/
  │  └─ 📁 dcat/                           # DCAT feed entries
  └─ 📁 prov/                              # PROV lineage bundles

📁 src/                                    # Canonical code homes (directional; target structure)
  📁 pipelines/                            # ETL transforms (deterministic)
  📁 graph/                                # Neo4j ingest + ontology bindings
  └─ 📁 server/                            # API boundary (REST/OpenAPI + GraphQL + optional OGC compat)

📁 web/                                    # UI (React/MapLibre/Cesium)
📁 tests/                                  # Contract + integration tests
📁 releases/                               # Versioned manifests/SBOM/telemetry bundles
~~~

**Repo structure note:** KFM docs describe a move toward **one canonical home per subsystem** (e.g., `src/server/` for APIs, `web/` for UI). If your current repo still contains legacy/duplicate folders, the integration standards MUST reference the **canonical** paths and document any transitional shims explicitly.

---

## 🧭 Context

### Interop philosophy: “open standards, low friction” 🌎

KFM is designed to plug into the broader geospatial + data science ecosystem by:

- publishing vector data as **GeoJSON** and raster as **COG** (typically in **WGS84**)  
- producing per‑dataset **STAC JSON** records, a **DCAT** discovery feed, and **PROV‑O JSON‑LD** lineage bundles  
- exposing data via an API documented with **OpenAPI** and offering **GraphQL** for flexible integration

Integration standards formalize these patterns so downstream adopters (researchers, portals, GIS tools, APIs) can rely on stable contracts.

### External clients and compatibility 🧰

While KFM’s UI may not directly use classic OGC services, KFM can provide compatibility routes when needed:

- **OGC API – Features** on top of KFM’s API  
- optional **WMS/WFS** outputs for ArcGIS/QGIS consumers  
- tiling endpoints (e.g., COG tiles) for raster browsing

If implemented, these must be treated as **contracted surfaces** (spec + tests + versioning), not ad‑hoc endpoints.

### Canonical references 🔗

- 📘 **Master Guide (v13 draft)**: `docs/MASTER_GUIDE_v13.md` (repo-level invariants, contracts, canonical homes)  
- 🧱 **Architecture blueprints**:  
  - `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`  
  - `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`  
  - `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`  
- 🧾 **Metadata profiles (v11)**:  
  - `docs/standards/KFM_STAC_PROFILE.md`  
  - `docs/standards/KFM_DCAT_PROFILE.md`  
  - `docs/standards/KFM_PROV_PROFILE.md`  
- 🧭 **Design decisions (ADRs)**: `docs/architecture/adr/README.md`

---

## 🧱 Architecture

### Where integration standards “attach” to the pipeline 🪢

~~~mermaid
flowchart LR
  subgraph EXT[🌐 External Ecosystem]
    HARV[🧾 Catalog Harvesters<br/>(DCAT / JSON-LD)]
    STACCL[🛰️ STAC Clients]
    GIS[🗺️ GIS Tools<br/>(QGIS/ArcGIS)]
    DEV[🧑‍💻 Developers / Apps]
  end

  subgraph KFM[🧩 KFM Core (Contracts + Evidence)]
    ETL[⚙️ ETL (deterministic)<br/>src/pipelines/**]
    DATA[📦 Data products<br/>data/processed/**]
    STAC[🛰️ STAC catalog<br/>data/stac/**]
    DCAT[🧾 DCAT feed<br/>data/catalog/dcat/**]
    PROV[🔍 PROV lineage<br/>data/prov/**]
    GRAPH[🕸️ Neo4j graph<br/>src/graph/**]
    API[🔌 APIs (contracted)<br/>src/server/**]
    OGC[🌐 OGC compat layer<br/>(optional)]
  end

  ETL --> DATA
  DATA --> STAC
  DATA --> DCAT
  ETL --> PROV

  STAC --> GRAPH
  DCAT --> GRAPH
  PROV --> GRAPH

  GRAPH --> API

  STAC --> STACCL
  DCAT --> HARV
  API --> DEV
  API --> GIS
  API --> OGC
  OGC --> GIS
~~~

### Integration boundary rules ✅

- **Catalogs are boundary artifacts**: STAC/DCAT/PROV are produced **before** graph/API/UI consumption.  
- **Graph stores references, not payloads**: the graph should point to catalog IDs/URLs rather than duplicate full datasets.  
- **API boundary is mandatory**: external consumers and the UI must access governed outputs through the API layer so redaction/classification controls can be enforced.

---

## 📦 Data & Metadata

### “If it’s published, it’s cataloged” 📌

Any dataset (including derived/analysis outputs) must ship with:

- **STAC** (collection + items; even non-spatial datasets may have a STAC collection for consistency)  
- **DCAT** dataset/distribution entry for discovery  
- **PROV** activity bundle for lineage (inputs → processing → outputs; agents; parameters/config refs)

Integration standards define the **minimum required fields**, allowed extensions, and mapping practices so that KFM catalogs remain consistent and machine‑validatable.

### Common delivery shapes 🧱

- **Vector**: GeoJSON FeatureCollection (or line-delimited GeoJSON if needed for streaming)  
- **Raster**: COG (plus tile endpoints / byte‑range access patterns)  
- **3D**: 3D Tiles (for narrative + terrain/feature context)  
- **Metadata**: JSON(-LD) for STAC/DCAT/PROV, validated against KFM profiles

---

## 🌐 STAC, DCAT & PROV Alignment

### Profiles governed by KFM standards 🧾

KFM extends base standards using project‑specific fields (e.g., provenance refs, uncertainty indicators). These profiles are expected to be defined here:

- `docs/standards/KFM_STAC_PROFILE.md`  
- `docs/standards/KFM_DCAT_PROFILE.md`  
- `docs/standards/KFM_PROV_PROFILE.md`  

### Crosswalk families maintained here 🔁

| Crosswalk Family | What it enables | Where it lives |
|---|---|---|
| **STAC ↔ OGC Records** | discoverability across catalog ecosystems | `mapping/stac_to_ogc_records.md` |
| **DCAT 3.0 ↔ OGC Records** | SDI catalog alignment, harvesting | `mapping/dcat_to_ogc_records.md` |
| **KFM ontology ↔ OGC/semantic models** | semantic interop (GeoSPARQL/Time + domain models) | `mapping/kfm_ontology_to_ogc.md` |
| **Formats & delivery** | GeoJSON/COG/3D Tiles delivery expectations | `MASTER-OGC-SDI-INTEGRATION.md` (or a dedicated doc) |

### External semantic standards 🌐🧠

Integration work may reference and map to:

- **GeoSPARQL** (spatial semantics)  
- **OWL‑Time** (temporal semantics)  
- **PROV‑O** (lineage)  
- **CIDOC‑CRM** (historical/cultural heritage semantics)  
- **JSON‑LD** contexts (distribution and semantic portability)

---

## ⚖ FAIR+CARE & Governance

### Governance triggers 🧨

Any integration change that impacts:

- data **discoverability** (DCAT)  
- asset **interpretation** (STAC properties, spatial/temporal semantics)  
- **lineage** (PROV)  
- **external access** (API surface, OGC compatibility endpoints)  

…should be treated as a **governance‑review event**, and may require an ADR under `docs/architecture/adr/`.

### Sovereignty and sensitive data safety 🪶🛡️

Interoperability must not “leak” sensitive context by accident.

- Prefer **generalized extents** and governance-reviewed disclosure rules for sensitive sites.  
- Enforce **redaction/classification** through the **API boundary**, not via UI-only controls.  
- Ensure exports (GeoJSON/COG/tiles/services) respect the same rules as internal visualization.

**Canonical references**:
- `docs/governance/ROOT_GOVERNANCE.md`  
- `docs/governance/ETHICS.md`  
- `docs/governance/SOVEREIGNTY.md`

---

## 🧪 Validation & CI/CD

### Minimum checks for integration standard changes ✅

Integration standards are “contracts”; changes should be validated by:

- **schema‑lint** for STAC/DCAT/PROV JSON schemas  
- **example/test-vector validation** (payloads under `test_vectors/` should validate and map deterministically)  
- **API contract checks** (OpenAPI + GraphQL SDL compatibility; version bump rules for breaking changes)  
- optional **OGC conformance tests** where OGC endpoints are implemented

### Telemetry and observability 📈

Integration work produces telemetry capturing:

- contract compliance pass/fail rates  
- mapping coverage % for crosswalk families  
- conformance test results  
- energy/carbon estimates (where applicable)

Canonical bundle refs:
- `releases/<version>/standards-telemetry.json`  
- `releases/<version>/manifest.zip` + `releases/<version>/sbom.spdx.json`

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2026-01-12 | Updated index to align with contract‑first / evidence‑first direction and canonical governance paths; normalized directory layout to include schemas/, releases/, data/catalog/dcat/, data/prov/, and `src/server/` API boundary. |
| v11.2.2 | 2025-11-28 | Initial integration standards index; Emoji Style A directory; MASTER OGC SDI alignment + telemetry links. |

---

<div align="center">

© 2026 Kansas Frontier Matrix — CC‑BY 4.0  
🔗 Integration Standards Index · FAIR+CARE + Sovereignty Guardrails · **Diamond⁹ Ω / Crown∞Ω**

[⬅️ Standards Index](../README.md) ·
[🧱 ADRs](../../architecture/adr/README.md) ·
[🌐 OGC SDI Master](MASTER-OGC-SDI-INTEGRATION.md) ·
[⚖ Governance](../../governance/ROOT_GOVERNANCE.md)

</div>