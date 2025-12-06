---
title: "🧩 Kansas Frontier Matrix — Ecology Analytical Methods (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/ecology/methods/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Data Standards Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x methods-compatible"
status: "Active / Enforced"

doc_kind: "Methods Index"
intent: "ecology-analytical-methods"
role: "methods-registry"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "ecology"
  applies_to:
    - "analyses"
    - "models"
    - "etl"
    - "validation"
    - "telemetry"
    - "governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Ecology (ethically governed)"
sensitivity: "General"
classification: "KFM-Open"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "docs/analyses/ecology/methods/README.md@v10.2.2"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-ecology-methods-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Ecology Analytical Methods**  
`docs/analyses/ecology/methods/README.md`

**Purpose**  
Document the analytical, statistical, and AI-assisted methodologies used within the **Ecology domain** of the Kansas Frontier Matrix (KFM).  
These methods ensure scientific reproducibility, ethical transparency, and **FAIR+CARE-certified governance** across ecological modeling and assessment workflows.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Verified-orange)](../../../../../../docs/standards/faircare.md)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable_branch-brightgreen)](../../../../../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

The **Ecology Analytical Methods** layer defines the scientific foundation for all ecology analyses — from **species distribution modeling (SDM)** to **landcover change detection** and **ecosystem service valuation**.  

All procedures:

- Follow **Master Coder Protocol v6.3** and **KFM‑MDP v11.2.4**  
- Are backed by **NASA-grade reproducibility** and explicit model cards  
- Are governed by **FAIR+CARE** with Indigenous and ecological ethics review  
- Emit telemetry conformant with `analyses-ecology-methods-v3` for energy, carbon, and validation metrics  

This document is the **methods index** for:

- `docs/analyses/ecology/species-distribution-modeling.md`  
- `docs/analyses/ecology/landcover-analysis.md`  
- `docs/analyses/ecology/ecosystem-services.md`  
- `docs/analyses/ecology/validation.md`  
- `docs/analyses/ecology/governance.md`  

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/ecology/methods/
├── 📘 README.md                    # This methods index
├── 📊 summary-findings.md          # Cross-method ecological findings & synthesis
├── 📈 figures/                     # Plots and visual method artifacts
│   └── 📘 README.md
├── 📋 tables/                      # Method performance tables and benchmarks
│   └── 📘 README.md
├── 📡 telemetry-logs/              # Method-level telemetry & validation exports
│   └── 📘 README.md
└── ⚖️ governance.md                # Method governance, approvals, and deprecation rules