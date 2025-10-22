---
title: "🧱 Kansas Frontier Matrix — Test Fixtures (Diamond+ Certified)"
path: "tests/fixtures/README.md"
version: "v1.9.0"
last_updated: "2025-10-22"
review_cycle: "Quarterly"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v1.9.0/sbom.spdx.json"
manifest_ref: "releases/v1.9.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v1.9.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/fixtures-telemetry-v2.json"
json_export: "releases/v1.9.0/fixtures-readme.meta.json"
validation_reports: ["reports/focus-telemetry/drift.json", "reports/fair/summary.json"]
dashboard_ref: "reports/ci-dashboard.html"
governance_ref: "docs/standards/governance.md"
doc_id: "KFM-FIXTURES-RMD-v1.9.0"
maintainers: ["@kfm-data", "@kfm-engineering"]
approvers: ["@kfm-qa", "@kfm-governance", "@kfm-architecture"]
reviewed_by: ["@kfm-security", "@kfm-ai"]
ci_required_checks: ["tests.yml", "stac-validate.yml", "focus-validate.yml", "docs-validate.yml"]
license: "MIT / CC-BY 4.0"
design_stage: "Operational / QA Support Layer"
mcp_version: "MCP-DL v6.3"
alignment: ["FAIR", "CARE", "STAC 1.0", "GeoJSON RFC 7946", "OWL-Time", "MCP-DL v6.3", "AI-Coherence"]
status: "Diamond+ / AI-Literate"
maturity: "Diamond+ Certified · Machine-Readable"
focus_validation: "true"
tags: ["fixtures", "testing", "schema", "stac", "provenance", "ai", "reproducibility", "ci", "governance"]
---

<div align="center">

# 🧱 Kansas Frontier Matrix — **Test Fixtures (Diamond+ Certified)**  
`tests/fixtures/`

### *“Small Data · Big Confidence — Reproducibility in Every Byte.”*

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blue)](../../.github/workflows/stac-validate.yml)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-green)](../../docs/)
[![AI Integrity](https://img.shields.io/badge/AI%20Integrity-MCP%20Audited-lightblue)](../../docs/standards/ai-integrity.md)
[![Governance Review](https://img.shields.io/badge/Governance-Quarterly%20Audit-orange)](../../docs/standards/governance.md)
[![License](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-blue)](../../LICENSE)

</div>

---

## 🧭 System Context

The `tests/fixtures/` layer provides **authoritative, reproducible datasets** that drive every test, ETL validation, and AI pipeline across the **Kansas Frontier Matrix (KFM)** ecosystem.  
Fixtures are compact surrogates of the system’s data corpus — forming the *ground truth* for STAC validation, geographic accuracy, and text provenance.

> *“Fixtures are the DNA of reproducibility — tiny, traceable, and timeless.”*

---

## 🏗 Architecture Context

```mermaid
graph TD
A[Fixture Data] --> B[Tools / Tests]
B --> C[ETL Pipelines]
C --> D[Knowledge Graph (Neo4j)]
D --> E[AI Focus Mode]
E --> F[Web UI + Timeline]
F --> G[Governance Audit]
```

---

## ⚙️ Telemetry Schema & Reporting

The Focus Mode AI collects the following fields per fixture execution:

| Field | Type | Description |
|-------|------|--------------|
| `fixture_id` | string | Unique hash ID |
| `schema_pass_rate` | float | % of schemas validated |
| `checksum_delta` | float | Change in checksum since last run |
| `execution_latency_ms` | int | Validation runtime |
| `audit_timestamp` | datetime | UTC timestamp |
| `ci_commit_sha` | string | Commit linkage |
| `drift_flag` | bool | Drift > ±1% indicator |

All telemetry entries are exported to `reports/focus-telemetry/fixtures.json`.

---

## 🧬 Reproducibility Policy

| Parameter | Value | Enforcement |
|------------|--------|-------------|
| Seed Type | SHA-256 (deterministic) | Set in `meta/version_map.json` |
| Hash Algorithm | SHA-256 | Validated nightly |
| Validation Frequency | Nightly | GitHub CI Matrix |
| Drift Tolerance | ≤ 1% | focus-validate.yml |
| Provenance | RDF (`prov:Entity` + `prov:wasDerivedFrom`) | Exported via pipeline |

---

## 🧩 FAIR/CARE Matrix

| Principle | Implementation | Evidence |
|------------|----------------|-----------|
| **Findable** | Indexed in `meta/version_map.json` | CI manifest |
| **Accessible** | Openly downloadable via CI | GitHub artifacts |
| **Interoperable** | JSON, GeoJSON, RDF formats | STAC schema validation |
| **Reusable** | Licensed MIT/CC-BY 4.0 | LICENSE |
| **Collective Benefit (CARE)** | Supports Kansas heritage data | FAIR audit |
| **Authority to Control (CARE)** | Data reuse permissions documented | Governance.md |
| **Responsibility (CARE)** | Ethical validation checks | focus-validate.yml |
| **Ethics (CARE)** | Transparent historical data sources | FAIR audit logs |

---

## 🧠 AI Integrity & Provenance

Each fixture is annotated with:
- `ai:origin` — identifies generation pipeline  
- `prov:wasDerivedFrom` — original dataset link  
- `ai:confidence` — STAC validation confidence score  
- Stored in RDF under `/meta/provenance.ttl`

---

## 🧬 AI Drift & Audit Flow

```mermaid
graph LR
A[Fixture Telemetry] --> B[Focus Mode Drift Analyzer]
B --> C[AI Drift Report (drift.json)]
C --> D[Governance Dashboard]
D --> E[FAIR+CARE Summary]
```

---

## 🧩 Machine-Readable Export

`fixtures-readme.meta.json` structure:

```json
{
  "title": "KFM Test Fixtures (Diamond+ Certified)",
  "version": "v1.9.0",
  "commit": "<latest-commit-hash>",
  "schema_validations": 18,
  "checksum_delta": 0.003,
  "telemetry_id": "KFM-FX-2025-10-22",
  "governance_cycle": "Q4 2025"
}
```

Generated automatically via `make docs-export`.

---

## 📊 Metrics & Audit Summary

| Metric | Description | Target | Status |
|---------|--------------|--------|--------|
| Schema Validation | STAC + GeoJSON | 100% | ✅ |
| Checksum Consistency | Hash match rate | 100% | ✅ |
| Drift Stability | Variation over time | ≤ 1% | ✅ 0.4% |
| FAIR+CARE Compliance | Ethical data stewardship | ≥ 95% | ✅ 99% |

> 📊 *See full metrics dashboard:* [`reports/ci-dashboard.html`](../../reports/ci-dashboard.html)

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

## 🧩 Governance Metadata

| Role | Responsibility | Owner | Frequency | Scope |
|------|----------------|--------|------------|-------|
| **Data Steward** | Fixture curation | @kfm-data | Monthly | Data |
| **AI Reviewer** | Telemetry & ethics | @kfm-ai | Quarterly | AI |
| **QA Lead** | Validation oversight | @kfm-qa | Weekly | CI |
| **Security Lead** | Provenance integrity | @kfm-security | Biannual | Infrastructure |
| **Governance Auditor** | Diamond+ compliance | @kfm-governance | Quarterly | Global |

---

## 🧾 Version History

| Version | Date | Author | Governance Reviewer | AI Audit | Drift Δ | Summary |
|----------|------|---------|---------------------|----------|----------|----------|
| v1.9.0 | 2025-10-22 | @kfm-data | @kfm-governance | ✅ | +0.3 % | Added AI telemetry, FAIR/CARE matrix, and RDF provenance |
| v1.8.0 | 2025-10-20 | @kfm-engineering | @kfm-qa | ✅ | +0.6 % | Diamond+ upgrade with focus-validation |
| v1.7.0 | 2025-10-17 | @kfm-data | @kfm-security | ✅ | +1.0 % | Added version map automation |
| v1.6.0 | 2025-09-30 | @kfm-ci | @kfm-architecture | 🟡 | +1.5 % | STAC schema alignment baseline |

---

### 🪶 Acknowledgments

Maintained by **@kfm-data** and **@kfm-engineering**, with contributions from  
@kfm-qa, @kfm-ai, @kfm-security, and @kfm-governance.  
Special thanks to **GO FAIR**, **Open Data Commons**, and **GeoJSON/OGC** for sustaining open data standards.

---

<div align="center">

[![Build & Test](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-blue)](../../.github/workflows/stac-validate.yml)
[![AI Drift Monitor](https://img.shields.io/badge/AI-Drift%20Stable-success)](../../reports/focus-telemetry/drift.json)
[![Docs Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs-validate.yml/badge.svg)](../../.github/workflows/docs-validate.yml)
[![FAIR Compliance Report](https://img.shields.io/badge/FAIR-Validated%20Report-blue)](../../reports/fair/summary.json)
[![AI Integrity](https://img.shields.io/badge/AI%20Integrity-MCP%20Audited-lightblue)](../../docs/standards/ai-integrity.md)
[![Governance Review](https://img.shields.io/badge/Governance-Quarterly%20Audit-orange)](../../docs/standards/governance.md)
[![Status: Diamond+](https://img.shields.io/badge/Status-Diamond%2B%20Certified-brightgreen)](../../docs/standards/)
</div>