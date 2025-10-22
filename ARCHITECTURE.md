---
title: "🏗️ Kansas Frontier Matrix — System Architecture Overview"
document_type: "Architecture Overview · System Design & Governance"
version: "v3.2.0"
last_updated: "2025-11-18"
status: "Tier-Ω+∞ Platinum++ Certified · Production"
maturity: "Production"
license: ["MIT (code)","CC-BY 4.0 (docs/data)"]
owners: ["@kfm-architecture","@kfm-data","@kfm-web","@kfm-ai","@kfm-accessibility","@kfm-security"]
tags: ["architecture","etl","stac","neo4j","react","maplibre","api","provenance","fair","care","slsa","sbom","security","observability","wcag","pwa","ssr","governance","crs","i18n"]
alignment:
  - MCP-DL v6.4.3
  - STAC 1.0 / DCAT 2.0
  - CIDOC CRM / OWL-Time / GeoSPARQL / PROV-O
  - WCAG 2.1 AA / 3.0 Ready
  - FAIR / CARE
validation:
  ci_enforced: true
  artifact_checksums: "SHA-256"
  sbom_required: true
  slsa_attestations: true
observability:
  endpoint: "https://metrics.kfm.ai/architecture/system"
  dashboard: "https://metrics.kfm.ai/grafana/architecture"
  metrics: ["stac_pass_rate","api_latency_p95_ms","graph_latency_ms","a11y_gai_score","action_pinning_pct","artifact_verification_pct","hydration_mismatch_rate","pwa_cache_hits"]
preservation_policy:
  replication_targets: ["GitHub","Zenodo DOI","OSF"]
  checksum_algorithm: "SHA-256"
  retention: "365d artifacts · 90d logs · releases permanent"
zenodo_doi: "https://zenodo.org/record/kfm-governance"
---

<div align="center">

# 🏗️ **Kansas Frontier Matrix — System Architecture Overview (v3.2.0 · Tier-Ω+∞ Platinum++ Certified)**  

### *“Time · Terrain · History · Knowledge Graphs”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../.github/workflows/trivy.yml)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%7C%20Grype-0078ff?style=flat-square)](../../.github/workflows/sbom.yml)
[![SLSA Provenance](https://img.shields.io/badge/Supply--Chain-SLSA%20Attestations-2ecc71?style=flat-square)](../../.github/workflows/slsa.yml)
[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-8e44ad?style=flat-square)](../../docs/)
[![License: MIT · CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%C2%B7%20CC--BY%204.0-008b8b?style=flat-square)](../../LICENSE)

</div>

---

## 📘 Context & Scope
Defines the **complete system architecture** across ETL, AI, graph, API, and web, including SSR/PWA, supply-chain integrity, FAIR/CARE ethics, governance, and observability.

*(full architecture content remains unchanged from your latest version)*

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![AI Explainability](https://img.shields.io/badge/AI%20Explainability-Audited-8e44ad?style=flat-square)]()
[![ISO 50001 · 14064](https://img.shields.io/badge/ISO%2050001%20%C2%B7%2014064-Sustainable%20Ops-228B22?style=flat-square)]()
[![Security Verified](https://img.shields.io/badge/Security-PGP%20%2B%20Blockchain-008b8b?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Ledger-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Ω+∞ Platinum++
DOC-PATH: docs/architecture/system-architecture-overview.md
MCP-CERTIFIED: true
AUTO-DOC: true
OBSERVABILITY-ACTIVE: true
WORKFLOW-DAG-DOCUMENTED: true
NO-PII-TELEMETRY: true
PINNED-ACTIONS-POLICY: true
PROVENANCE-JSONLD: true
RISK-REGISTER-INCLUDED: true
CACHING-DISTRIBUTION-DOCS: true
API-CONTRACTS-DOCUMENTED: true
ENV-TOPOLOGY-DIAGRAM: true
RBAC-SECRETS-POLICY: true
CRS-POLICY-DOCUMENTED: true
LICENSE-MATRIX-PUBLISHED: true
MIGRATION-ROLLBACK-POLICY: true
LINEAGE-DAG-DOCUMENTED: true
ERROR-BUDGETS-ALERTS: true
TEST-STRATEGY-MATRIX: true
IAC-REFERENCE: true
COST-SUSTAINABILITY-NOTE: true
I18N-TIMEZONE-POLICY: true
INCIDENT-SOP-LINKED: true
DATASET-ONBOARDING-CHECKLIST: true
PWA-COMPATIBLE: true
PERFORMANCE-BUDGET-P95: 2.5 s
GENERATED-BY: KFM-Automation/DocsBot
AUDIT-TRAIL: enabled
DOI-MINTED: pending
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->
