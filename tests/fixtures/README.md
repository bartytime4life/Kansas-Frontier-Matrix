---
title: "🧱 Kansas Frontier Matrix — Test Fixtures (Diamond+ Certified)"
path: "tests/fixtures/README.md"
version: "v1.8.0"
last_updated: "2025-10-22"
review_cycle: "Quarterly"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v1.8.0/sbom.spdx.json"
manifest_ref: "releases/v1.8.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v1.8.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/fixtures-telemetry-v1.json"
json_export: "releases/v1.8.0/fixtures-readme.meta.json"
validation_reports: ["reports/focus-telemetry/drift.json", "reports/fair/summary.json"]
dashboard_ref: "reports/ci-dashboard.html"
governance_ref: "docs/standards/governance.md"
doc_id: "KFM-FIXTURES-RMD-v1.8.0"
maintainers: ["@kfm-data", "@kfm-engineering"]
approvers: ["@kfm-qa", "@kfm-governance", "@kfm-architecture"]
reviewed_by: ["@kfm-security", "@kfm-ai"]
ci_required_checks: ["tests.yml", "stac-validate.yml", "focus-validate.yml", "docs-validate.yml"]
license: "MIT / CC-BY 4.0"
design_stage: "Operational / QA Support Layer"
mcp_version: "MCP-DL v6.3"
alignment: ["FAIR", "CARE", "STAC 1.0", "GeoJSON RFC 7946", "OWL-Time", "MCP-DL v6.3"]
status: "Diamond+ / AI-Literate"
maturity: "Diamond+ Certified · Machine-Readable"
tags: ["fixtures", "testing", "schema", "stac", "provenance", "ai", "reproducibility", "ci"]
focus_validation: "true"
---

<div align="center">

# 🧱 Kansas Frontier Matrix — **Test Fixtures (Diamond+ Certified)**  
`tests/fixtures/`

### *“Small Data · Big Confidence — Reproducibility in Every Byte.”*

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blue)](../../.github/workflows/stac-validate.yml)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-green)](../../docs/)
[![AI Integrity](https://img.shields.io/badge/AI%20Integrity-MCP%20Audited-lightblue)](../../docs/standards/ai-integrity.md)
[![Governance Review](https://img.shields.io/badge/Governance-Quarterly%20Audit-orange)](../../docs/standards/governance.md)
[![License](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-blue)](../../LICENSE)

</div>

---

## 🧭 System Context

The `tests/fixtures/` directory provides the **canonical reference datasets** that make every test in the **Kansas Frontier Matrix (KFM)** reproducible and verifiable.  
It feeds both **local testing** and **AI telemetry pipelines**, supplying consistent, schema-aligned “small data” representing Kansas’ geographic and textual history.

> *“Fixtures are the fingerprints of reproducibility — small, immutable, and full of truth.”*

---

## ⚙️ Fixture Lifecycle Diagram

```mermaid
graph TD
A[Fixture Creation<br/>Geo · Text · STAC · Config] --> B[Validation<br/>STAC · JSON Schema]
B --> C[Integration<br/>Pytest · CI/CD Pipelines]
C --> D[Telemetry Export<br/>AI Focus · Drift Monitor]
D --> E[Governance Audit<br/>FAIR+CARE Validation]
E --> F[Reproducible Deploys<br/>Web UI + Docs]
classDef step fill:#e6f2ff,stroke:#005cc5,color:#111;
class A,B,C,D,E,F step;
```

---

## 🗂 Directory Layout

```text
tests/fixtures/
├── geo/                     # GeoJSON & raster samples
│   ├── ks_county_sample.geojson
│   ├── tiny_vector.geojson
│   └── dem_sample.tif
├── text/                    # OCR / diary / treaty excerpts
│   ├── sample_diary.txt
│   └── treaty_excerpt.txt
├── stac/                    # STAC Item/Collection examples
│   ├── stac_item_min.json
│   └── stac_collection_min.json
├── sources/                 # Mock dataset manifests
│   └── usgs_topo_sample.json
├── configs/                 # Web UI config fixtures
│   ├── layers_min.json
│   └── app_config_min.json
├── meta/                    # Fixture metadata & changelogs
│   ├── CHANGELOG.md
│   └── version_map.json
└── __init__.py
```

---

## 🧩 Fixture Standards

| Category | Used By | Schema / Purpose |
|-----------|---------|------------------|
| **Geo** | GIS tools, STAC validator | Validate GeoJSON & COG conversion |
| **Text** | NLP / OCR pipelines | Entity extraction (people, places, treaties) |
| **STAC** | `validate_stac.py` | Schema + temporal structure validation |
| **Sources** | `fetch_data.py` | Mock dataset registry (JSON manifest) |
| **Configs** | Web UI, `build_config.py` | UI configuration + STAC layer mapping |

---

## 🧬 AI Drift & Provenance Monitoring

Fixture telemetry logs are analyzed nightly by the **Focus Mode AI**.  
Any deviation in schema or checksum values is recorded in `reports/focus-telemetry/drift.json`.  
If drift > ±1%, CI raises a governance audit flag.

---

## 🧾 Provenance & Integrity

| Artifact | Description |
|-----------|-------------|
| **Inputs** | Raw test files & generated metadata |
| **Outputs** | Validated fixtures, checksum maps |
| **Integrity** | SHA-256 & version parity verified in CI |
| **Traceability** | Linked to STAC Item IDs and commit SHAs |

---

## 🧩 FAIR/CARE Declaration

- **Findable:** Fixtures discoverable via `meta/version_map.json`  
- **Accessible:** Publicly visible and downloadable in CI artifacts  
- **Interoperable:** Follows STAC 1.0, GeoJSON RFC 7946  
- **Reusable:** Released under MIT/CC-BY 4.0  
- **CARE:** Data represents historical material ethically and transparently  

---

## 🧩 Reproduction Checklist

- [x] Fixture hashes verified nightly  
- [x] Schema validation passed  
- [x] Metadata exported to `/reports/fair/summary.json`  
- [x] Machine-readable README (`fixtures-readme.meta.json`) generated  
- [x] Telemetry drift < 1%  
- [x] Governance audit completed  

---

## 📊 Metrics & Audit Summary

| Metric | Description | Target | Status |
|--------|-------------|---------|--------|
| Schema Validation | STAC + GeoJSON tests | 100% | ✅ |
| Checksum Verification | Hash match across runs | 100% | ✅ |
| Drift Stability | Fixture consistency over time | ≤ 1% | ✅ 0.6% |
| FAIR+CARE Compliance | Audit conformance | ≥ 95% | ✅ 99% |

> 📊 *View live dashboard:* [`reports/ci-dashboard.html`](../../reports/ci-dashboard.html)

---

## ⚖️ Legal & Licensing Notes

All code samples: **MIT License**  
All documentation and metadata: **CC-BY 4.0**  
All test data: public domain or derivative of open datasets.  
Attribution and citation required where applicable.  

Machine-readable export available at:  
`releases/v1.8.0/fixtures-readme.meta.json`

---

## 🧮 Compliance Summary

| Standard | Validation Source | Status | Audit Cycle |
|-----------|------------------|---------|--------------|
| **MCP-DL v6.3** | `docs/standards/mcp-validation.yml` | ✅ | Continuous |
| **STAC / GeoJSON** | `data/stac/schema/` | ✅ | Nightly |
| **FAIR+CARE** | `docs/standards/fair.md` | ✅ | Quarterly |
| **AI-Coherence / Drift** | `focus-validate.yml` | ✅ | Continuous |
| **Governance Audit** | `docs/standards/governance.md` | ✅ | Quarterly |

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Drift Δ | Summary |
|----------|------|---------|-----------|---------|----------|
| v1.8.0 | 2025-10-22 | @kfm-data | @kfm-governance | +0.3 % | Diamond+ certification, AI telemetry & FAIR reporting |
| v1.7.0 | 2025-10-20 | @kfm-engineering | @kfm-qa | +0.5 % | Added AI drift and provenance monitoring |
| v1.6.0 | 2025-10-17 | @kfm-data | @kfm-security | +1.0 % | Version mapping + checksum alignment |
| v1.5.0 | 2025-09-30 | @kfm-ci | @kfm-architecture | +1.3 % | STAC schema automation baseline |

---

## 🧠 MCP-DL v6.3 Compliance

| Principle | Implementation |
|-----------|----------------|
| Documentation-First | Fixtures documented + version-mapped |
| Reproducibility | Seed-based, deterministic generation |
| Provenance | SHA-256 embedded in every artifact |
| Accessibility | JSON/GeoJSON open formats |
| Open Standards | STAC, GeoJSON, OWL-Time |
| Auditability | Nightly CI schema & hash checks |

---

### 🪶 Acknowledgments

Maintained by **@kfm-data** and **@kfm-engineering**, with support from  
@kfm-qa, @kfm-ai, @kfm-governance, and @kfm-architecture.  
Thanks to **GO FAIR**, **Open Data Commons**, and **GeoJSON/OGC** for advancing open and auditable data standards.

---

<div align="center">

[![Build & Test](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blue)](../../.github/workflows/stac-validate.yml)
[![AI Drift Monitor](https://img.shields.io/badge/AI-Drift%20Stable-success)](../../reports/focus-telemetry/drift.json)
[![FAIR Compliance Report](https://img.shields.io/badge/FAIR-Validated%20Report-blue)](../../reports/fair/summary.json)
[![Governance Review](https://img.shields.io/badge/Governance-Quarterly%20Audit-orange)](../../docs/standards/governance.md)
[![Status: Diamond+](https://img.shields.io/badge/Status-Diamond%2B%20Certified-brightgreen)](../../docs/standards/)
</div>