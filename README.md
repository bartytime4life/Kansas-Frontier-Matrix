---
title: "🌌 Kansas Frontier Matrix — v11 System Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Annual · FAIR+CARE Council & Architecture Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:readme:root:v11.2.2"
semantic_document_id: "kfm-doc-root-overview"
event_source_id: "ledger:README.md"
immutability_status: "version-pinned"

sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/system-telemetry.json"
telemetry_schema: "schemas/telemetry/system-v11.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "kfm-root-overview"
lifecycle_stage: "stable"

fair_category: "F1-A1-I2-R3"
care_label: "Mixed / Multi-Domain"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded by KFM v12 Root Overview"
---

<div align="center">

# 🌌 **Kansas Frontier Matrix (KFM v11)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *A State-Scale Knowledge System for Kansas — Environment, History, Culture, AI, and Time*  

`README.md`

**Purpose**  
Provide the **canonical, high-level overview** of the Kansas Frontier Matrix v11 — a fully-governed, reproducible, state-scale knowledge system unifying environment, history, culture, AI, and time into one coherent, semantic geospatial platform.

</div>

---

## 🗂️ Repository Layout (KFM v11.2.2 · Emoji Profile A)

~~~text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root system overview (this file)
│
├── 📂 data/                             # Data lifecycle & catalogs
│   ├── 📂 sources/                      # External source manifests (no large files)
│   ├── 📂 raw/                          # Downloaded raw data (DVC/LFS, ignored by git)
│   ├── 📂 work/                         # Intermediate artifacts (ephemeral/regen)
│   ├── 📂 processed/                    # Canonical processed outputs (GeoTIFF, GeoJSON, CSV)
│   ├── 📂 stac/                         # STAC 1.x catalog (Collections + Items)
│   ├── 📂 provenance/                   # PROV-O / lineage records (JSON-LD, RDF)
│   └── 📂 releases/                     # Versioned release bundles (SBOM, manifest, telemetry)
│
├── 🧪 src/                              # Backend, ETL, AI/ML, graph integration, telemetry
│   ├── 📂 pipelines/                    # LangGraph DAGs, ETL, reconciliation
│   ├── 📂 ai/                           # Models, feature extractors, Focus Mode logic
│   ├── 📂 graph/                        # Neo4j schema, queries, loaders
│   ├── 📂 server/                       # API services (FastAPI/GraphQL, etc.)
│   └── 📂 instrumentation/             # OpenLineage + OpenTelemetry helpers
│
├── 🌐 web/                              # Frontend (React + MapLibre + Cesium)
│   ├── 📂 src/                          # Components (map, timeline, Focus Mode UI)
│   ├── 📂 public/                       # Static assets
│   └── 📂 meta/                         # SEO, link cards, manifest/config
│
├── 📚 docs/                             # Documentation (user, developer, governance)
│   ├── 📂 standards/                    # KFM-MDP, FAIR+CARE, heritage, sovereignty policies
│   ├── 📂 architecture/                 # System design, pipelines, web, graph
│   ├── 📂 analyses/                     # Domain analyses and reports
│   ├── 📂 governance/                   # Council processes, charters, decision logs
│   └── 📂 templates/                    # Document & MCP templates
│
├── 🧬 mcp/                              # Master Coder Protocol (documentation-first assets)
│   ├── 📂 experiments/                  # Experiment logs (ETL, AI, modeling)
│   ├── 📂 sops/                         # Standard Operating Procedures
│   ├── 📂 model_cards/                  # Model cards for AI & statistical models
│   └── 📄 MCP-README.md                # MCP usage guide for KFM
│
├── 🧪 tests/                            # Unit, integration, and E2E tests
│   ├── 📂 backend/
│   ├── 📂 pipelines/
│   ├── 📂 web/
│   └── 📂 graph/
│
├── 🛠 tools/                            # Utility scripts & notebooks (non-core code)
│   ├── 📂 scripts/
│   └── 📂 notebooks/
│
└── ⚙️ .github/                          # GitHub infrastructure, CI/CD & governance
    ├── 📄 README.md                     # GitHub infra overview
    ├── 🏗️ ARCHITECTURE.md               # CI/CD architecture spec
    ├── 🤖 workflows/                    # CI/CD workflows (ci, docs, stac, dcat, AI, security, telemetry)
    └── 🧱 actions/                      # Composite actions (markdown-lint, schema-validate, etc.)
~~~

Author rules:

- Every directory above MUST have a `README.md`.  
- New top-level directories MUST be added here.  
- Directory trees MUST use `~~~text` fences (no backtick fences inside).

---

## 📘 What the System Is

The **Kansas Frontier Matrix (KFM)** is a unified, multi-layer, multi-epoch knowledge system integrating geospatial data, historical archives, environmental models, AI pipelines, archaeology, cultural landscapes, hazard layers, ecological datasets, and narrative modes (Story Nodes & Focus Mode v3).

Powered by **Neo4j**, governed by **FAIR+CARE**, and aligned with **CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O**, and **STAC/DCAT** catalogs.

KFM v11 serves as a **state-scale Kansas digital twin** across space + time.

---

## 🧱 Architecture

KFM v11 uses a fully-governed stacked architecture:

1. **Data & Storage** — STAC/DCAT catalogs, DVC/LFS, CF-compliant rasters  
2. **Pipelines** — LangGraph deterministic DAG ETL, CrewAI workers, OpenLineage  
3. **Graph** — Neo4j v5 with CIDOC-CRM + GeoSPARQL + OWL-Time  
4. **API Layer** — FastAPI/GraphQL with auth & rate limits  
5. **Frontend** — React + MapLibre + Cesium 3D twin  
6. **CI/CD & Governance** — AI governance, sovereignty checks, SBOM, telemetry  

All components are **reproducible** and **linked through PROV-O**.

---

## 📦 Data & Metadata

All data is:

- STAC-registered  
- DCAT-cataloged  
- PROV-O lineage-tracked  
- FAIR+CARE-labeled  
- Sovereignty-compliant  

Metadata includes CRS, vertical datums, units, temporal ranges, and processing provenance.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes (v3):

- Combine **geometry + time + narrative + graph links**  
- Are governed by metadata, sovereignty, and narrative safety rules  
- Feed **Focus Mode v3**, which provides context-aware narrative exploration backed entirely by data  

No narrative may contradict underlying datasets or governance policies.

---

## ⚖ Governance

KFM is governed by:

- FAIR+CARE Council  
- Architecture Board  
- Data/Heritage Working Groups  
- AI Safety & Narrative Governance Board  

All PRs must pass CI/CD enforcement:

- Metadata checks  
- AI governance  
- STAC/DCAT validation  
- Sovereignty / CARE compliance  
- SBOM + security  
- Markdown protocol validation  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                             |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Elevated repository layout, aligned with KFM-MDP v11.2.2, clarified architecture & governance integration.          |
| v11.1.2 | 2025-11-27 | Previous v11 root overview with initial digital twin framing.                                                       |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](docs/README.md) · [📏 Standards Index](docs/standards/ROOT-STANDARDS.md) · [🛡 Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
