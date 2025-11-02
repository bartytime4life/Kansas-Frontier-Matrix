---
title: "🧮 Kansas Frontier Matrix — Web Public Meta Widgets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/meta/widgets/README.md"
version: "v9.3.3"
last_updated: "2025-11-02"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.3.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.3.3/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v9.3.3/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-public-meta-widgets-v1.json"
json_export: "../../../../releases/v9.3.3/web-public-meta-widgets.meta.json"
validation_reports:
  - "../../../../reports/self-validation/web-public-meta-widgets-validation.json"
  - "../../../../reports/audit/web-public-meta-widgets-lineage.json"
  - "../../../../reports/fair/web-public-meta-widgets-summary.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
security_ref: "../../../../docs/standards/security/web-metadata-security.md"
observability_ref: "../../../../docs/telemetry/observability-matrix.md"
sbom_audit_ref: "../../../../reports/audit/sbom-web-public-meta-widgets.json"
release_notes_ref: "../../../../releases/v9.3.3/CHANGELOG.md"
---

<div align="center">

# 🧮 Kansas Frontier Matrix — **Web Public Meta Widgets**
`web/public/meta/widgets/README.md`

**Purpose:** Defines metadata, validation standards, and governance lineage for all interactive widget components within the Kansas Frontier Matrix web application.  
Ensures that each widget — analytical, visual, or AI-driven — maintains full provenance, versioning, FAIR+CARE certification, and telemetry observability.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../docs/standards/governance/FAIR-CARE.md)  
[![Security Audit](https://img.shields.io/badge/Security-Audited%20(SBOM)-blueviolet)](../../../../reports/audit/sbom-web-public-meta-widgets.json)  
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](../../../../.github/workflows/site.yml)  
[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256%20Verified-purple)](../../../../reports/audit/web-public-meta-widgets-lineage.json)

</div>

---

## 📚 Overview

The **Web Public Meta Widgets directory** tracks provenance and compliance metadata for all **interactive UI widgets** used within the KFM web interface — such as search bars, filters, dynamic analytics panels, and Focus Mode AI tools.  
It defines a modular, machine-readable framework ensuring each widget’s data integrity, provenance, and ethical compliance.

Metadata records here guarantee:
- **Reproducibility:** Each widget’s configuration and dependencies are version-tracked.  
- **Auditability:** Every widget is checksum-verified and validated in CI/CD pipelines.  
- **FAIR+CARE compliance:** Open, ethical, and transparent AI-driven web design.  
- **Governance integration:** Automatic linkage to Immutable Governance Chain ledgers.  

---

## 📁 Directory Layout

```
web/public/meta/widgets/
├── widget-search.json       # Metadata for the site-wide search widget (index, query logic, provenance)
├── widget-focus.json        # Metadata for Focus Mode AI widget (contextual entity explorer & summaries)
├── widget-timeline.json     # Metadata for interactive timeline component (temporal slider, data binding)
├── widget-layercontrol.json # Metadata for map layer control widget (toggle logic, metadata source)
└── README.md                # Directory governance, schema alignment, and validation specifications
```

**File Descriptions:**

- **`widget-search.json`** — Captures the configuration, provenance, and dependency metadata for the search interface.  
  Defines API endpoints, source indexes, and lineage to ensure consistent, transparent search experiences.

- **`widget-focus.json`** — Governs metadata for the AI-powered Focus Mode widget.  
  Includes entity linkage schema, context sources, and telemetry integration for explainability and drift tracking.

- **`widget-timeline.json`** — Defines temporal metadata for timeline visualization.  
  Tracks slider configuration, time schema alignment (OWL-Time), and STAC dataset relationships for spatiotemporal data navigation.

- **`widget-layercontrol.json`** — Documents metadata for layer toggling and map overlay management.  
  Ensures all layer references in MapLibre adhere to validated STAC/DCAT catalog entries and checksum verification.

- **`README.md`** — Provides comprehensive documentation for this directory’s metadata schema, audit logs, and governance connections.

---

## ⚙️ Metadata Specification

Each metadata file follows the **KFM Web Meta Schema v1.4**, ensuring uniformity, compliance, and interoperability.

```yaml
id: "web-meta-widget-focus-v1"
type: "asset-meta"
title: "Focus Mode Widget Metadata"
description: "Metadata record defining provenance, dependencies, and compliance for the Focus Mode interactive widget."
source_url: "https://github.com/bartytime4life/Kansas-Frontier-Matrix/web/public/meta/widgets/widget-focus.json"
license: "MIT"
version: "1.0.3"
checksum_sha256: "<sha256-hash>"
created_at: "2025-11-02T00:00:00Z"
validated_by: "faircare-validate.yml"
status: "active"
tags:
  - "web"
  - "widget"
  - "focus-mode"
alignment:
  - "STAC v1.0.0"
  - "DCAT 3.0"
  - "CIDOC CRM"
```

All widget metadata must include:
- **Unique ID and version number** for identification  
- **License and checksum verification** for reproducibility  
- **FAIR+CARE alignment** and **MCP-DL v6.3** conformance  
- **Links to validation and telemetry reports** for governance logging  

---

## 🧪 Validation & Observability

Validation workflows continuously verify each metadata file’s structure, ethics compliance, and telemetry logging.

| Validation Type | Workflow | Output Report |
|-----------------|------------|----------------|
| FAIR+CARE Certification | `faircare-validate.yml` | `reports/fair/web-public-meta-widgets-summary.json` |
| Schema Validation | `stac-validate.yml` | `reports/self-validation/web-public-meta-widgets-validation.json` |
| Lineage Verification | `data-lineage.yml` | `reports/audit/web-public-meta-widgets-lineage.json` |
| Telemetry Recording | `focus-telemetry.yml` | `releases/v9.3.3/focus-telemetry.json` |

Telemetry schemas (defined in `schemas/telemetry/web-public-meta-widgets-v1.json`) feed into the **Observability Matrix**, monitoring widget lifecycles, dependency drift, and interaction metrics.

---

## 🧠 Governance & Security Integration

All widget metadata files participate in the **Immutable Governance Chain**:
- Registered under `ROOT-GOVERNANCE.md`  
- Linked to SBOM audits and SPDX records  
- Verified through continuous integration telemetry  

Security and governance audits verify:
- Open licensing (MIT or CC-BY)  
- Safe data handling for AI and Focus Mode features  
- Valid SPDX-tagged dependencies in `sbom-web-public-meta-widgets.json`  

Governance and audit logs:
```
reports/audit/governance-ledger.json
reports/audit/web-meta-widgets-integrity.json
```

---

## 🧩 Role in System Architecture

Widget metadata provides:
- **Focus Mode traceability:** AI-driven components log contextual entity relationships.  
- **Governance transparency:** UI-level governance links directly to metadata lineage.  
- **Observability integration:** Logs event-level telemetry for map, timeline, and query interactions.  
- **Automated documentation:** Metadata auto-generates compliance info for developers and governance reviewers.  

This directory acts as the **dynamic governance bridge** between AI, web interaction, and validation systems in the KFM architecture.

---

## 🧾 Version History

| Version | Date | Author | Notes |
|----------|------|---------|-------|
| v9.3.3 | 2025-11-02 | Frontier Matrix Maintainers | Added detailed file descriptions, SBOM, and telemetry schema integration |
| v9.3.2 | 2025-11-01 | Frontier Matrix Maintainers | Added FAIR+CARE compliance mapping and lineage references |
| v9.3.1 | 2025-10-28 | Frontier Matrix Maintainers | Initial schema alignment and metadata structure |
| v9.3.0 | 2025-10-20 | System Init | Directory established under Platinum README Template v7.1 and MCP-DL v6.3 |

---

<div align="center">

**Kansas Frontier Matrix — Immutable Documentation Chain**  
*“Every widget validated, every insight governed, every byte traceable.”* 🔗

</div>
