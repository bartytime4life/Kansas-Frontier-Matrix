---
title: "🌐 Kansas Frontier Matrix — Web Public Meta (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/meta/README.md"
version: "v9.3.2"
last_updated: "2025-11-02"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🌐 Kansas Frontier Matrix — **Web Public Meta**
`web/public/meta/README.md`

**Purpose:** Defines metadata structure, asset provenance, and FAIR+CARE compliance for all files within `web/public/`, ensuring traceable origin, proper licensing, and audit readiness.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/architecture/repo-focus.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../docs/standards/governance/FAIR-CARE.md)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](../../.github/workflows/site.yml)
[![Data Lineage](https://img.shields.io/badge/Data-Lineage%20Verified-purple)](../../reports/audit/data-lineage.json)

</div>

---

## 📚 Overview

The **Web Public Meta directory** maintains JSON, YAML, or Markdown metadata descriptors that define the provenance, version, and compliance status of all static assets distributed in the `web/public/` folder.  
These records ensure every image, icon, CSS asset, or data file embedded in the public web build has a verified origin, checksum, and open license.

This layer underpins **FAIR+CARE certification** and the **Master Coder Protocol (MCP)** audit framework, aligning with open-science and digital humanities best practices for traceability, reproducibility, and ethical data reuse.

---

## 🧭 Directory Layout

```
web/
└── public/
    ├── images/
    ├── icons/
    ├── css/
    ├── js/
    ├── checksums/
    ├── meta/
    │   ├── components/
    │   ├── headers/
    │   ├── footers/
    │   ├── widgets/
    │   └── README.md   ← (this file)
    └── README.md
```

Each subdirectory under `meta/` documents component-specific metadata (e.g., version identifiers, licensing info, and source URLs for imagery or icons).

---

## ⚙️ Metadata Schema

Metadata files must follow the **KFM Web Meta Schema v1.4**, a YAML/JSON format aligned with **DCAT 3.0**, **schema.org**, and **STAC** principles.  
An example record:

```yaml
id: "web-public-iconset-v1"
type: "asset-meta"
title: "Public Icon Set"
description: "SVG icons for UI components — verified under MIT license."
source_url: "https://github.com/bartytime4life/Kansas-Frontier-Matrix/assets/icons"
license: "MIT"
version: "1.0.3"
checksum_sha256: "<sha256-hash>"
created_at: "2025-10-30T00:00:00Z"
validated_by: "site.yml"
status: "active"
```

All entries must be:
- **Versioned** (`version:` field)  
- **Checksum-verified** via SHA-256 under `/web/public/checksums/`  
- **Linked** to audit records in `reports/self-validation/`

---

## 🔒 Provenance and Validation

Every web asset passes through a checksum and metadata validation stage during CI/CD:

- **Checksum Validation:** Conducted via `faircare-validate.yml`
- **License Verification:** Ensures all public files are compliant with open-source licenses
- **STAC/DCAT Mapping:** Maps asset descriptors to standardized metadata schemas for interoperability
- **Governance Linkage:** Tied to `ROOT-GOVERNANCE.md` and logged in the Immutable Governance Ledger

Validation results are stored in:
```
reports/self-validation/web-public-meta.json
reports/audit/web-meta-lineage.json
```

---

## 🧩 Integration with Focus Mode & UI

The `web/public/meta/` layer supports Focus Mode operations by exposing metadata to the frontend React/MapLibre components.  
When assets are rendered (e.g., historical maps or widgets), the system fetches metadata entries via:
```
GET /meta/{asset_id}.json
```
This enables contextual display of asset provenance, licensing info, and contribution credits in UI tooltips and info modals.

---

## 🧠 Governance & Compliance

| Aspect | Standard | Reference |
|--------|-----------|------------|
| Data Licensing | MIT / CC-BY | [LICENSE](../../LICENSE) |
| FAIR Principles | Findable, Accessible, Interoperable, Reusable | FAIR+CARE Docs |
| CARE Principles | Collective Benefit, Authority, Responsibility, Ethics | FAIR+CARE Docs |
| STAC Integration | OGC STAC v1.0.0 | [STAC Overview](../../docs/standards/stac-overview.md) |
| Validation | MCP-DL v6.3 | [MCP Standards](../../docs/standards/mcp.md) |

All public metadata is included in quarterly governance reviews.

---

## 🧾 Version History

| Version | Date | Author | Notes |
|----------|------|---------|-------|
| v9.3.2 | 2025-11-02 | Frontier Matrix Maintainers | Initial creation under Diamond⁹ Ω standards |
| v9.3.1 | 2025-10-28 | Frontier Matrix Maintainers | Draft version for web/meta integration |
| v9.3.0 | 2025-10-20 | System Init | Template creation based on Platinum README v7.1 |

---

<div align="center">

**Kansas Frontier Matrix — Immutable Documentation Chain**  
*“Every asset accounted, every byte traceable.”* 🔗

</div>
