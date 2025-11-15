---
title: "🌾 Kansas Frontier Matrix — Monorepo Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.4.0/sbom.spdx.json"
manifest_ref: "releases/v10.4.0/manifest.zip"
telemetry_ref: "releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/root-readme-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "root-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed Dataset Classification"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false
provenance_chain:
  - "README.md@v10.0.0"
  - "README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWorkSeries"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "schemas/json/root-readme.schema.json"
shape_schema_ref: "schemas/shacl/root-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:root-readme-v10.4.0"
semantic_document_id: "kfm-doc-root-readme"
event_source_id: "ledger:README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next major KFM release"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Monorepo Overview**  
`README.md`

**Purpose:**  
Provide a unified **FAIR+CARE-governed**, **schema-aligned**, and **architecture-driven** overview of the  
**Kansas Frontier Matrix (KFM)** monorepo — including its directories, governance model, documentation system,  
CI/CD automation, data platform, test architecture, and web platform components.

This repository follows **MCP-DL v6.3** and **KFM-MDP v10.4** to guarantee deterministic, ethical, accessible,  
and reproducible scientific computing.

</div>

---

## 📘 What Is the Kansas Frontier Matrix?

The **Kansas Frontier Matrix (KFM)** is an integrated, ontology-driven, provenance-secure knowledge system combining:

- Geospatial + temporal data  
- Historical + environmental datasets  
- ETL + AI enrichment pipelines  
- FAIR+CARE governance  
- Semantic knowledge graph (Neo4j + CIDOC-CRM + GeoSPARQL + OWL-Time)  
- Story Node v3 narrative units  
- Focus Mode v2.5 reasoning engine  
- Interactive 2D/3D Web Platform (MapLibre + Cesium)  
- Documentation, testing, governance, and observability systems  

The monorepo provides the full end-to-end pipeline from **raw data ingestion → AI enrichment → knowledge graph  
construction → 2D/3D narrative-driven web visualization**.

---

## 🧱 Monorepo Structure

A complete KFM directory structure using the official `~~~text` stable tree:

~~~text
.
├── README.md                       # This monorepo overview
├── ARCHITECTURE.md                 # Root system architecture (KFM v10)
│
├── data/                           # Data platform: raw → work → processed → STAC/DCAT
│   ├── ARCHITECTURE.md
│   └── ...                         
│
├── docs/                           # Standards, governance, audits, analyses
│   ├── ARCHITECTURE.md
│   └── standards/
│
├── web/                            # Web Platform (2D/3D UI + Focus Mode)
│   ├── ARCHITECTURE.md
│   └── src/
│       └── ARCHITECTURE.md
│
├── tools/                          # Automation, governance, telemetry, validation
│   ├── ARCHITECTURE.md
│   └── ...
│
├── tests/                          # Unit, integration, E2E, schema, governance, A11y
│   ├── ARCHITECTURE.md
│   └── ...
│
├── schemas/                        # JSON/SHACL/ontology schemas
│   └── ...
│
├── releases/                       # SBOM, manifest, telemetry per release
│   └── v10.4.0/
│
├── .github/                        # CI/CD, governance automation, security
│   ├── ARCHITECTURE.md
│   └── README.md
│
└── scripts/                        # Optional helper utilities
~~~

---

## 🧩 System Architecture Summary

The KFM monorepo has six high-level subsystems:

### 1. **Data Platform (`data/**`)**
- Multi-stage ingestion pipeline  
- STAC/DCAT generation  
- Provenance/CARE governance  
- Drift detection, sustainability telemetry  
- Neo4j ingestion interface  

### 2. **ETL + AI Pipelines (`src/pipelines/**`)**
- OCR → NER → entity linking  
- Spatial/temporal normalization  
- Story Node enrichment  
- Predictive & remote-sensing models  

### 3. **Web Platform (`web/**`)**
- MapLibre (2D), Cesium (3D)  
- Focus Mode v2.5  
- Story Node v3  
- Accessibility-first React  
- Governance overlays  
- Telemetry integration  

### 4. **Tools Platform (`tools/**`)**
- AI audits  
- Validation suites  
- Governance ledger updates  
- Sustainability telemetry  
- CLI & CI/CD orchestration  

### 5. **Test Platform (`tests/**`)**
- Unit, integration, E2E  
- Schema tests  
- Governance & CARE validation  
- A11y tests & telemetry validation  

### 6. **GitHub Infrastructure (`.github/**`)**
- Autonomous CI/CD engine  
- Markdown, schema, governance, security validation  
- Telemetry export  
- Release creation + SBOM verification  

---

## 🛡 Governance & FAIR+CARE Integration

The monorepo deeply integrates:

- CARE principles  
- Indigenous Data Sovereignty  
- FAIR metadata  
- Provenance chain validation  
- Licensing integrity  
- Redaction/generalization (H3 spatial masking)  
- Ethical AI boundaries (no fabricated data, no unverified history)  
- SBOM + manifest compliance  
- Audit-ready workflows  

All architectural documents include:

- Front-matter metadata  
- Provenance chains  
- Governance references  
- Telemetry links  
- Version pinning  

---

## ♿ Accessibility Integration

The entire KFM system adheres to **WCAG 2.1 AA**:

- Semantic HTML  
- A11y tokens in design system  
- Keyboard navigation  
- High-contrast / reduced-motion support  
- Alternative text mapping  
- A11y testing under `tests/e2e/**` and `tests/unit/**`

Accessibility is a **release-blocking CI requirement**.

---

## 📈 Telemetry & Observability

Telemetry is collected from:

- Web UI  
- Pipelines  
- Tools  
- Tests  
- CI/CD  
- Sustainability monitors  

Telemetry bundles appear in:

`releases/<version>/focus-telemetry.json`

Metrics include:

- Energy (Wh)  
- Carbon (gCO₂e)  
- A11y events  
- Governance audit results  
- Map/Focus/Story Node usage  
- Performance/WebVitals  

---

## 🔐 Security & Supply Chain

Security policies enforced via:

- `.github/SECURITY.md`  
- SBOM + checksum verification  
- SLSA-aligned workflow integrity  
- Protected branches + CODEOWNERS  
- Dependency vulnerability scans  
- Immutable provenance  

Zero PII, zero sensitive coordinate exposure.

---

## 🧪 Testing Requirements Summary

All PRs must pass:

- TypeScript strict mode  
- Linting & formatting  
- Schema validation  
- Unit + integration + E2E  
- A11y tests  
- FAIR+CARE validation  
- Telemetry validation  
- Security scans  

Merges are **blocked** on any failure.

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full monorepo overview aligned to KFM-MDP v10.4; integrated governance, schemas, CARE, telemetry |
| v10.3.2 | 2025-11-14 | Expanded subsystem architecture references |
| v10.3.1 | 2025-11-13 | Initial monorepo overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>