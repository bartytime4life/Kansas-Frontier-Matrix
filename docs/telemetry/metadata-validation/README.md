---
title: "🔏 KFM v11.2.6 — Metadata Validation & Trust Badge System (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Metadata Governance Board"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x badge-compatible"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../releases/v11.2.6/metadata-validation-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/metadata-validation-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
trust_profile: "KFM-TRUST v2"

classification: "Public · Governed"
sensitivity: "Low/Moderate"
sensitivity_level: "General"
public_exposure_risk: "Low"
machine_extractable: true
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded by next metadata-validator revision"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A, CARE-S, CARE-T"
care_label_detail: "CARE-level metadata validation · Sovereignty-aware compliance"

header_profile: "standard"
footer_profile: "standard"

badge_profiles:
  - "root-centered-badge-row"
layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
  - "metadata-harvest-v1"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Oversight"
  metadata: "Semantic Integrity · Provenance Verified"
  governance: "Accountability × Ethics × Resilience"

heading_registry:
  approved_h2:
    - "🧭 Purpose & Scope"
    - "🗂️ Directory Layout"
    - "🔍 Validator Coverage"
    - "🛡️ Trust Badge"
    - "⚙️ CI Workflow Logic"
    - "📘 Reference Scripts"
    - "🧩 Embedding in Other Modules"
    - "🧾 Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-schema-lint"
  - "faircare-lint"
  - "footer-check"
  - "heading-check"
  - "provenance-check"
  - "accessibility-check"
  - "telemetry-schema-check"

ci_integration:
  workflow: ".github/workflows/metadata-validation.yml"
  environment: "dev → staging → production"
  gating: "badge-must-be-green-for-main-merge"

ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "timeline-generation"
  - "semantic-highlighting"
  - "governance-warnings"

ai_transform_prohibited:
  - "content-alteration"
  - "metadata-fabrication"
  - "schema-auto-fill"
  - "governance-override"

metadata_profiles:
  - "FAIR+CARE"
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "OpenLineage"
  - "SLSA"
  - "SBOM-SPDX"
  - "KFM-Metadata-Trust-v11"

provenance_chain:
  - "docs/telemetry/metadata-validation/README.md@v11.2.3"
  - "docs/telemetry/metadata-validation/README.md@v11.2.2"
  - "docs/telemetry/metadata-validation/README.md@v11.1.0"
  - "docs/telemetry/metadata-validation/README.md@v10.4.3"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 🔏 Metadata Validation & Trust Badge System  
Automated STAC, DCAT, JSON-LD, Provenance & FAIR+CARE Metadata Integrity Validation

[![KFM Metadata Trust v11.2.6](https://img.shields.io/badge/KFM_Metadata_Trust-v11.2.6-6f42c1)]()  
[![FAIR Verified](https://img.shields.io/badge/FAIR-Verified-2ea44f)]()  
[![CARE Compliant](https://img.shields.io/badge/CARE-Compliant-0aa)]()  
[![SLSA Attested](https://img.shields.io/badge/SLSA-Attested-005bbb)]()

</div>

---

## 🧭 Purpose & Scope

The Metadata Validation & Trust Badge System ensures every dataset, STAC Collection, STAC Item, pipeline output, and documentation artifact within KFM meets **governed metadata quality**, **provenance correctness**, and **FAIR+CARE ethical compliance**.

It delivers:

• Automated metadata schema checks  
• Provenance verification  
• FAIR+CARE completeness  
• JSON-LD expansion tests  
• Trust Badge generation  
• HTML audit reports for governance review  

The system is mandatory for all v11 metadata-bearing directories.

---

## 🗂️ Directory Layout

~~~text
docs/telemetry/metadata-validation/
├── 📄 README.md                           # This file
│
├── 🧪 checks/                             # Schemas & validation rule sets
│   ├── stac-schema.json                   # STAC schema
│   ├── dcat-schema.json                   # DCAT-JSON schema
│   ├── jsonld-context.json                # JSON-LD expansion context
│   └── provenance-rules.yaml              # SBOM / SLSA / signature enforcement rules
│
├── 🛠️ ci/                                 # CI workflows
│   ├── metadata-badge.yml                 # Validator + badge emitter
│   └── report-template.html               # HTML template for validation reports
│
├── 📊 reports/                            # GitHub Pages–served validator results
│   └── index.html                         # Current metadata validation report
│
├── 🎨 badges/                             # Dynamic badge JSON outputs
│   └── metadata-badge.json                # Consumed by shields.io
│
└── 🐍 scripts/                            # Validation CLI tools
    ├── validate_metadata.py               # STAC/DCAT/LD/provenance/FAIR+CARE checks
    ├── render_report.py                   # HTML report generator
    └── utils.py                           # Shared helpers (context expansion, hashing)
~~~

---

## 🔍 Validator Coverage

### STAC Compliance
• Structural validity  
• Required + recommended field validation  
• Asset completeness & EO metadata checks  

### DCAT / JSON-LD
• JSON-LD context expansion  
• Missing vocabulary terms  
• Semantic correctness  
• Broken PROV-O lineage references  

### Provenance Integrity
• SHA256 file hashing  
• SBOM presence & completeness  
• SLSA v1.0 predicate validation  
• Signature and attestation checks  

### FAIR + CARE
• FAIR F1/F2/F3 field completeness  
• CARE-A/S/T compliance  
• Indigenous Data Sovereignty protections  

---

## 🛡️ Trust Badge

Embed the Trust Badge in any module’s README:

Badge:  
https://img.shields.io/badge/metadata--validation-dynamic-blueviolet  

Badge report target:  
https://\<pages-domain\>/docs/telemetry/metadata-validation/reports/index.html  

The badge turns green or red depending on metadata validation status.

---

## ⚙️ CI Workflow Logic

Steps:

1. Run metadata validators  
2. Compute pass/fail state  
3. Emit badge JSON  
4. Publish HTML report to GitHub Pages  
5. Attach validation evidence in CI UI  
6. Gate merges when badge is failing  

---

## 📘 Reference Scripts

**validate_metadata.py**  
• Runs STAC, DCAT, JSON-LD, provenance, FAIR+CARE validation  

**render_report.py**  
• Creates HTML validation reports served from `/reports/`  

**utils.py**  
• Hashing, context expansion, SBOM parsing, shared helpers  

---

## 🧩 Embedding in Other Modules

Recommended directories to include the Trust Badge:

• `docs/data/`  
• Any `stac/` collection  
• Any `pipelines/` output directory  
• Any metadata-driven UI component  

---

## 🧾 Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | Updated to KFM-MDP v11.2.6; release/telemetry refs bumped to v11.2.6; footer and cross-links aligned with v11.2.6 telemetry docs; no schema changes. |
| v11.2.3 | 2025-12-01 | Centralized metadata validator & Trust Badge system released.                                    |
| v11.2.2 | 2025-11-12 | DCAT/LD expansion rules standardized; schema consolidation.                                      |
| v11.2.0 | 2025-10-28 | FAIR+CARE rule integration completed; provenance model stabilized.                               |
| v10.4.x | 2025-08-xx | Early distributed validators prior to centralization.                                            |

---

<div align="center">

🔏 **Kansas Frontier Matrix — Metadata Validation & Trust Badge System (v11.2.6)**  
Semantic Integrity · Provenance Verified · FAIR+CARE-Aligned

[📘 Docs Root](../../..) ·  
[📡 Telemetry Index](../README.md) ·  
[🛡 Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🌿 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·  
[🛡 Security Policy](../../standards/security/SECURITY-POLICY.md) ·  
[📊 Metadata Validation Telemetry](../../../releases/v11.2.6/metadata-validation-telemetry.json) ·  
[🧩 Validation Schema](../../../schemas/telemetry/metadata-validation-v1.json)

</div>