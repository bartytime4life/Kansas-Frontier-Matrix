---
title: "🧭 Kansas Frontier Matrix — Root Repository Overview"
document_type: "Repository Index · Architecture & Operations"
version: "v2.2.0"
last_updated: "2025-10-20"
status: "Tier-Ω+∞ Certified · Production"
maturity: "Production"
license: ["MIT (code)", "CC-BY 4.0 (docs/data)"]
owners: ["@kfm-architecture","@kfm-data","@kfm-web","@kfm-ai","@kfm-accessibility","@kfm-security"]
tags: ["kfm","knowledge-graph","stac","neo4j","react","maplibre","etl","ai","provenance","fair","care","slsa","sbom","observability","wcag"]
alignment:
  - MCP-DL v6.3.2
  - STAC 1.0 / DCAT 2.0
  - CIDOC CRM / OWL-Time / GeoSPARQL
  - WCAG 2.1 AA (3.0 ready)
  - FAIR / CARE
validation:
  ci_enforced: true
  artifact_checksums: "SHA-256"
  sbom_required: true
  slsa_attestations: true
observability:
  dashboard: "https://metrics.kfm.ai/root"
  metrics: ["build_status","stac_pass_rate","codeql_critical","trivy_critical","a11y_score","action_pinning_pct","artifact_verification_pct"]
preservation_policy:
  replication_targets: ["GitHub Releases","Zenodo DOI (major)","OSF"]
  checksum_algorithm: "SHA-256"
  retention: "365d artifacts · 90d logs · releases permanent"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Root Repository Overview (v2.2.0 · Tier-Ω+∞ Certified)**

### *“Time · Terrain · History · Knowledge Graphs”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](./.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](./.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](./.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](./.github/workflows/trivy.yml)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%2B%20Grype-blue)](./.github/workflows/sbom.yml)
[![SLSA Provenance](https://img.shields.io/badge/Supply--Chain-SLSA%20Attestations-green)](./.github/workflows/slsa.yml)
[![Docs · MCP-DL v6.3.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.3.2-blue)](./docs/)
[![License: MIT \| CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-blue)](./LICENSE)

</div>

---

<details><summary>📚 <strong>Table of Contents</strong></summary>

- [📘 Context & Scope](#-context--scope)
- [🌾 Mission](#-mission)
- [🧠 Core Concepts](#-core-concepts)
- [🏛 Architecture Snapshot](#-architecture-snapshot)
- [🧱 Repository Structure](#-repository-structure)
- [⚙️ Quickstart](#️-quickstart)
- [🔒 Security & Supply Chain](#-security--supply-chain)
- [🧾 Provenance & FAIR Registration](#-provenance--fair-registration)
- [📑 Documentation & CI (Docs-as-Code)](#-documentation--ci-docs-as-code)
- [🤖 AI Governance (Quality & Ethics)](#-ai-governance-quality--ethics)
- [🧾 Data Ethics & Cultural Safeguards](#-data-ethics--cultural-safeguards)
- [📦 Artifacts & Evidence Registry](#-artifacts--evidence-registry)
- [📊 Governance Telemetry Snapshot](#-governance-telemetry-snapshot)
- [📜 Linked ADRs & SOPs](#-linked-adrs--sops)
- [🔗 Design → Implementation Traceability](#-design--implementation-traceability)
- [🧾 Versioning & Release Governance](#-versioning--release-governance)
- [🧾 Change-Control Register](#-change-control-register)
- [🩺 Health & Observability](#-health--observability)
- [📣 Contributor Quick-Links](#-contributor-quick-links)
- [📚 References](#-references)
- [🕓 Version History](#-version-history)

</details>

---

## 📘 Context & Scope
This document is the **root index** for the Kansas Frontier Matrix monorepo.  
It defines repository layout, architectural responsibilities, CI/CD enforcement, and governance expectations.

- **Scope:** All production code, datasets, documentation, and automation under the KFM namespace.  
- **Exclusions:** Archived experiments, personal notebooks, third-party forks, or derivative works.  
- **Purpose:** Establish a single point of orientation for contributors, automation pipelines, and governance audits.

---

## 🌾 Mission
The **Kansas Frontier Matrix (KFM)** unifies **time, terrain, and history**.  
It integrates geospatial, ecological, and archival datasets into a **semantic knowledge graph** built on **Neo4j**, following **CIDOC CRM**, **OWL-Time**, and **FAIR/CARE** principles.

> *Every dataset tells a story; every story is mapped, cited, and reproducible.*

---

## 🧠 Core Concepts
| Layer | Purpose |
|:--|:--|
| **ETL / Processing** | Ingest → transform → validate into geospatial layers (COG/GeoJSON/CSV) |
| **AI / ML Enrichment** | OCR, NLP, geocoding, summarization, entity linking |
| **Knowledge Graph** | Neo4j + CIDOC CRM + OWL-Time + GeoSPARQL; JSON-LD & GraphQL |
| **API Layer** | FastAPI + GraphQL for entities, events, and map layers |
| **Frontend** | React + MapLibre + D3 timeline; Focus Mode + AI Assistant |

---

## 🏛 Architecture Snapshot
```mermaid
flowchart TD
  A["Data Sources<br/>NOAA · USGS · FEMA · KHS · Archives · Treaties"]
    --> B["ETL + AI Pipeline<br/>Python · GDAL · Rasterio · spaCy · Transformers"]
  B --> C["Processed Layers<br/>COG · GeoJSON · CSV · NetCDF"]
  C --> D["STAC Catalog<br/>Collections · Items · Assets"]
  B --> E["Knowledge Graph<br/>Neo4j · CIDOC CRM · OWL-Time · GeoSPARQL"]
  D --> E
  E --> F["FastAPI / GraphQL API<br/>JSON/GeoJSON/JSON-LD"]
  F --> G["Web Frontend<br/>React · MapLibre · Timeline · Focus Mode / AI Assistant"]
  C --> H["Google Earth Exports<br/>KML/KMZ"]
```
<!-- END OF MERMAID -->

---

## 🧱 Repository Structure
```text
Kansas-Frontier-Matrix/
├─ src/              # ETL, AI/ML, graph, API services
│  ├─ etl/           # Ingestion & transformation (GDAL/Pandas)
│  ├─ ai/            # OCR/NLP, summarization, entity extraction
│  ├─ api/           # FastAPI + GraphQL
│  └─ graph/         # Neo4j schema & migrations
├─ web/              # React + MapLibre frontend
├─ data/
│  ├─ sources/       # Source manifests (license, coverage, URLs)
│  ├─ raw/           # Unprocessed input (LFS/DVC)
│  ├─ processed/     # GeoJSON, COGs, CSVs
│  └─ stac/          # STAC Items & Collections
├─ docs/             # Architecture, SOPs, design, templates, glossary
├─ tools/            # CLI utilities & deployment helpers
├─ tests/            # Unit, integration, and regression tests
├─ .github/          # Workflows, issue templates, governance
├─ .dvc/ (optional)  # DVC config for large files
└─ Makefile          # Canonical pipeline entry
```

> Each dataset includes **checksum (SHA-256)**, **license**, and a **STAC manifest**.  
> Large binaries are tracked through **LFS/DVC**.

---

## ⚙️ Quickstart
### 🧰 Requirements
Python 3.11+ · Node 20+ (pnpm) · Neo4j 5.x · GDAL/Rasterio · Make

### 🚀 Setup
```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
pip install -r requirements.txt
cd web && pnpm install && cd ..
```

### 🧮 Run
```bash
make fetch
make process
make stac
make serve
```
Visit **http://localhost:3000** (web UI) and **http://localhost:7474** (Neo4j).

---

## 🔒 Security & Supply Chain
- **CodeQL** (static analysis), **Trivy** (CVE scan), **Gitleaks** (secret scan)  
- **SBOM** (Syft CycloneDX) and **SLSA** attestations attached to each release  
- Actions pinned by SHA; signed commits; least-privilege OIDC tokens

---

## 🧾 Provenance & FAIR Registration
- **STAC** lineage and provider metadata (`derived_from`, `license`, `providers`)  
- **PROV-O** annotations within `docs/standards/`  
- **DOIs** minted per major release (Zenodo); provenance bundles (`.prov.json`, SBOM, SLSA) included in assets

---

## 📑 Documentation & CI (Docs-as-Code)
- `docs-validate.yml` → schema, metadata, links, and accessibility validation  
- `actionlint` → workflow syntax validation  
- `markdown_rules.md` → unified style enforcement (MCP-DL compliant)

---

## 🤖 AI Governance (Quality & Ethics)
- Model cards (`docs/models/*`) with metrics and dataset provenance  
- Bias baselines + F1/ROUGE thresholds  
- Human-in-the-loop validation (`@kfm-ai`)  
- All AI-generated summaries cite source documents and confidence scores

---

## 🧾 Data Ethics & Cultural Safeguards
- STAC `data_ethics` property for sensitive/tribal data  
- Ethics ledger at `docs/standards/ethics/ledger/`  
- Redaction of private or restricted geometry before public release

---

## 📦 Artifacts & Evidence Registry
| Artifact | Generated By | Retention | Purpose |
|:--|:--|:--|:--|
| `.prov.json` | release-please / slsa.yml | Permanent | Provenance attestations |
| `sbom.cdx.json` | sbom.yml | 1 year | Supply-chain inventory |
| `slsa.intoto.jsonl` | slsa.yml | 1 year | Build provenance |
| `docs-validate-report.json` | docs-validate.yml | 90d | Docs compliance log |
| `metrics.json` | telemetry exporter | 30d | Root CI health snapshot |

---

## 📊 Governance Telemetry Snapshot
> ![Root Dashboard](https://metrics.kfm.ai/img/root-dashboard-snapshot.png)  
> _Aggregated metrics from CI/CD, validation pipelines, and STAC audits (auto-refresh every 2h)._

---

## 📜 Linked ADRs & SOPs
| Document | Purpose | Status |
|:--|:--|:--|
| `docs/adr/ADR-001-monorepo-architecture.md` | Defines unified repo layout | ✅ |
| `docs/adr/ADR-008-release-governance.md` | Establishes versioning & governance policy | ✅ |
| `docs/sop/contributor-onboarding.md` | Contributor setup and access instructions | ✅ |
| `docs/sop/security-scanning.md` | CI security and SBOM/SLSA workflow | ✅ |

---

## 🔗 Design → Implementation Traceability
| Mockup | Component | Tokens | Status |
|:--|:--|:--|:--:|
| `map_overlay_v2.0` | `web/src/components/map/Legend.tsx` | `--kfm-color-accent`,`--kfm-space-md` | ✅ |
| `timeline_v2.3` | `web/src/components/timeline/Slider.tsx` | `--kfm-motion-smooth` | ⚙️ QA |

---

## 🧾 Versioning & Release Governance
```yaml
versioning:
  code: "SemVer"
  data: "STAC item versions"
  docs: "MCP metadata with changelog"
  models: "Model card + hash"
  automation: "release-please.yml"
  doi_on_major: true
tags:
  releases: "kfm-vMAJOR.MINOR.PATCH"
  designs: "mockups-v*"
  catalogs: "stac-v*"
```

---

## 🧾 Change-Control Register
```yaml
changes:
  - date: "2025-10-20"
    change: "Added context, evidence registry, telemetry snapshot, ADR linkage, and contributor links."
    reviewed_by: "@kfm-architecture"
    pr: "#418"
```

---

## 🩺 Health & Observability
- Dashboard: [metrics.kfm.ai/root](https://metrics.kfm.ai/root)  
- Metrics: build status, STAC pass rate, CodeQL/Trivy critical, A11y score, pinning %, artifact verification %

---

## 📣 Contributor Quick-Links
- 🗂 [Open Issues](./issues)
- 🚀 [New Pull Request](./compare)
- 🧩 [Project Board](./projects)
- 📘 [Contributing Guide](./CONTRIBUTING.md)

---

## 📚 References
- `docs/architecture/system-architecture-overview.md`  
- `docs/architecture/file-architecture.md`  
- `docs/architecture/ai-automation.md`  
- `docs/standards/markdown_rules.md`  
- `docs/standards/markdown_guide.md`  
- `data/stac/` · `data/sources/`  
- `tests/`

---

## 🕓 Version History
| Version | Date | Author | Summary | Type |
|:--|:--|:--|:--|:--|
| **v2.2.0** | 2025-10-20 | @kfm-architecture | Added context, artifacts, telemetry, ADR linkage, and change log for Tier-Ω+∞ certification. | Minor |
| v2.1.0 | 2025-10-19 | @kfm-architecture | Dropdown ToC, refined alignment to v6.3.2. | Minor |
| v2.0.0 | 2025-11-14 | @kfm-architecture | Tier-Ω+∞ upgrade: FAIR provenance, supply-chain badges, versioning policy. | Major |
| v1.6.3 | 2025-10-18 | @kfm-architecture | Consolidated Quickstart + security hardening. | Minor |
| v1.0.0 | 2024-06-01 | Founding Team | Initial repository overview. | Major |

---

<div align="center">

🏛 *Document the Frontier · Reconstruct the Past · Illuminate Connections*  
© 2025 Kansas Frontier Matrix — MIT (code) · CC-BY 4.0 (data/docs)

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.3.2
MCP-TIER: Ω+∞
DOC-PATH: README.md
DOC-HASH: sha256:root-repo-overview-v2-2-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MCP-CERTIFIED: true
AUTO-DOC: true
VALIDATION-HASH: {auto.hash}
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->