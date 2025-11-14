---
title: "🤝 Kansas Frontier Matrix — Contribution Guidelines (Diamond⁹ Ω / Crown∞Ω · MCP-DL v6.3 · Platinum README v7.1)"
path: "CONTRIBUTING.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.3.1/sbom.spdx.json"
manifest_ref: "releases/v10.3.1/manifest.zip"
telemetry_ref: "releases/v10.3.1/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-contributing-v2.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🤝 **Kansas Frontier Matrix — Contribution Guidelines**  
`CONTRIBUTING.md`

**Purpose:**  
Define the complete, **documentation-first**, **FAIR+CARE-aligned**, **MCP-certified** workflow for contributing **code, data, models, Story Nodes, ETL pipelines, STAC Collections, UI components, and graph structures** to the Kansas Frontier Matrix (KFM).  
All contributions must pass the **Diamond⁹ Ω / Crown∞Ω Governance Standard**, meaning:  
- **Reproducibility** (deterministic builds, documented steps)  
- **Traceability** (commit → artifact → ledger → STAC/DCAT → graph)  
- **Ethical compliance** (CARE sovereignty, heritage protection, H3 generalization)  
- **Validation** (CI/CD, lint, schema, FAIR+CARE, security, telemetry)

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](docs/README.md)  
[![License](https://img.shields.io/badge/License-MIT%20%2F%20CC--BY%204.0-green)](LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](docs/standards/faircare.md)  
[![Status](https://img.shields.io/badge/Status-Automated-success)]()

</div>

---

## 📘 Overview
KFM v10.x is a **fully containerized**, **FAIR+CARE-compliant**, **MCP-governed**, documentation-driven monorepo.  
All contributions must adhere to:

- **Platinum README v7.1 formatting**  
- **Markdown Structural Rules**  
- **Semantic versioning**  
- **Provenance + SBOM + SLSA**  
- **Graph schema migration protocols**  
- **Dataset contract requirements**  
- **Story Node narrative standards**  
- **AI model governance**

Every PR must ship **code + documentation + metadata** together, with **no undocumented behavior**.  
If it’s not documented, it does not exist.

---

## 🗂️ Repository Layout (Authoritative Structure)

~~~~~text
KansasFrontierMatrix/
├── src/
│   ├── ai/                # Focus Transformer v2, summarizers, explainability
│   ├── api/               # FastAPI + GraphQL endpoints
│   ├── graph/             # Neo4j schema, queries, migrations
│   ├── pipelines/
│   │   ├── etl/           # Batch ETL (OCR → NER → STAC/DCAT → Neo4j)
│   │   ├── etl/streaming/ # Kafka/WebSocket streaming ingestion
│   │   ├── ai/            # AI-augmented pipeline steps
│   │   ├── validation/    # Schema, STAC, DCAT, FAIR+CARE verify
│   │   └── utils/         # Shared helpers
│   └── telemetry/         # OpenTelemetry, metrics, dashboards
├── web/                   # React + MapLibre + Cesium client
├── data/
│   ├── sources/           # Dataset contracts (JSON)
│   ├── raw/               # Pulled data (LFS/DVC pointers)
│   ├── processed/         # Cleaned GeoJSON/COG/CSV
│   └── stac/              # STAC 1.0.0 catalogs (Items/Collections)
├── docs/                  # Standards, governance, pipelines, templates
├── tools/                 # STAC validators, ingest scripts, converters
├── tests/                 # Unit + integration tests
├── .github/               # Actions, issue templates, PR templates
└── Makefile               # Orchestration entrypoints
~~~~~

---

## 📜 Guiding Principles (v10.3.1)

1. **Documentation-First**  
   Every feature must include a README, schema, or narrative.

2. **Reproducibility**  
   Exact commands, seeds, environment, dataset contracts, and outputs must be included.

3. **FAIR+CARE Compliance**  
   All data, metadata, models, and Story Nodes must follow ethical/sovereignty protocols.

4. **Governance**  
   Contributions enter the governance ledger (automated by CI).

5. **Validation-Before-Merge**  
   All checks must be green. No warnings. No exceptions.

---

## 🧪 Contribution Workflow (Golden Path)

### 1️⃣ Create a Topic Branch
~~~~~bash
git checkout -b feature/<short-kebab-name>
~~~~~

Allowed prefixes:  
`feature/` · `fix/` · `docs/` · `data/` · `model/` · `story/` · `refactor/` · `test/`

---

### 2️⃣ Prepare the Change

### 🧾 Code Contributions
- Python → **PEP8 + Black**  
- TypeScript → **ESLint + Prettier**  
- Add README for all new modules  
- Add docstrings + schemas  
- Add tests:

~~~~~bash
make test
~~~~~

---

### 🗺 Data Contributions (STAC/DCAT + Contract Required)

Every dataset **must** include a dataset contract:

~~~~~json
{
  "id": "usgs_soils_1937",
  "title": "Historic Soil Survey Map (1937)",
  "description": "Digitized soil survey for western Kansas.",
  "type": "raster",
  "spatial": [-102.05, 37.0, -94.6, 40.0],
  "temporal": { "start": "1937-01-01", "end": "1937-12-31" },
  "license": "Public Domain",
  "provenance": "USGS Archive",
  "checksum": "sha256-<hex>",
  "care_label": "public",
  "updated": "2025-11-13"
}
~~~~~

Processing requirements:

- Raster → **COG**  
- Vector → **GeoJSON**  
- CRS → **EPSG:4326**  
- Validate:

~~~~~bash
make validate
~~~~~

---

### 🤖 AI / Model Contributions (Model Cards Required)
All models must include:

- Model card (`docs/models/<model>.md`)  
- Training config  
- Dataset sources & licensing  
- Metrics + bias evaluation  
- SHAP/LIME explainability setup  
- STAC Item for model artifact  

Stored in:

~~~~~text
src/ai/models/<model_name>/
~~~~~

---

### 📝 Story Node Contributions
Each Story Node requires:

- `story-node.json` (schema-valid)  
- Narrative body (Markdown)  
- Spatial footprint (GeoJSON)  
- Time interval (OWL-Time)  
- Relations to graph nodes  

---

## ✏️ Documentation Requirements

| Contribution | Required Docs |
|-------------|----------------|
| New ETL pipeline | `src/pipelines/<id>/README.md` |
| Dataset | Dataset contract + STAC Item |
| UI feature | `web/src/components/<feature>/README.md` |
| AI model | Model card + training notes |
| Story Node | JSON + narrative + relations |

All docs follow:

- `docs/standards/markdown_rules.md`  
- YAML front-matter  
- Centered title block  
- Version history  

---

## 🧩 Mermaid Example (Required Style)

~~~~~mermaid
flowchart TD
  A["Input"]
  B["Processing"]
  C["Output"]
  A --> B --> C
~~~~~

---

## 🧪 Local Validation

~~~~~bash
make lint
make validate
make test
~~~~~

Commit example:

~~~~~bash
git commit -m "data: add usgs_soils_1937 (STAC + FAIR+CARE validated)"
~~~~~

---

## 🔀 Pull Request Checklist

- [ ] Summary  
- [ ] Updated docs  
- [ ] STAC/DCAT generated  
- [ ] Graph migrations  
- [ ] Tests added & passing  
- [ ] CI green  
- [ ] Governance ledger updated  

---

## 🧩 Issue Templates

| Template | Purpose |
|----------|---------|
| `data_submission.yml` | New dataset |
| `feature_request.yml` | New feature |
| `bug_report.yml` | Bug |
| `governance_form.yml` | CARE review |

---

## 🔒 Governance & Ethics

- Sensitive locations → **H3 generalization**  
- CARE labels required  
- Provenance tracked (STAC/DCAT/graph/SBOM)  
- Indigenous + treaty data requires special review  

---

## 🧾 Conventional Commits

| Type | Example |
|------|---------|
| `feat:` | `feat: add treaty boundary diff` |
| `fix:` | `fix: resolve neo4j duplicate rels` |
| `docs:` | `docs: update contributing guide` |
| `data:` | `data: integrate mesonet feed` |
| `model:` | `model: train focus transformer v2` |
| `story:` | `story: add Fort Larned narrative` |

---

## ⚙️ CI/CD Workflows

| Workflow | Purpose |
|---------|----------|
| `stac-validate.yml` | STAC validation |
| `dcat-validate.yml` | DCAT validation |
| `faircare-validate.yml` | FAIR+CARE ethics |
| `docs-lint.yml` | Markdown + YAML |
| `model-audit.yml` | Drift/bias |
| `codeql.yml` | Security |
| `trivy.yml` | Vulnerabilities |
| `neo4j-schema-guard.yml` | Schema guard |
| `build-and-deploy.yml` | Web deploy |

Artifacts in:

~~~~~text
reports/
  ├── fair/
  ├── security/
  ├── self-validation/
  ├── stac/
  └── telemetry/
~~~~~

---

## 🧭 Support

- Documentation: `docs/README.md`  
- Standards: `docs/standards/*`  
- Governance: `docs/standards/governance/ROOT-GOVERNANCE.md`  
- Discussions: GitHub  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|-------|---------|---------|
| v10.3.1 | 2025-11-13 | A. Barta | Full v10 rewrite; Platinum README; Story Nodes; predictive ETL; STAC/DCAT bridge. |
| v9.7.0 | 2025-11-05 | A. Barta | Added workflow–artifact map; telemetry schemas. |
| v9.5.0 | 2025-10-20 | A. Barta | FAIR+CARE updates; dataset contract expansion. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial MCP contribution guide. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Documentation Index](docs/README.md) · [Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
