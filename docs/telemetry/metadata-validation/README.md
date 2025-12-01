---
title: "🔏 KFM v11.2.3 — Metadata Validation & Trust Badge System (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/README.md"
version: "v11.2.3"
last_updated: "2025-12-01"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Metadata Governance Board"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x badge-compatible"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../releases/v11.2.3/metadata-validation-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/metadata-validation-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
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
    - "🧭 Overview"
    - "🗂️ Directory Layout"
    - "🔍 Validator Coverage"
    - "🛡️ Trust Badge"
    - "⚙️ CI Workflow Logic"
    - "📘 Reference Scripts"
    - "🧩 Embedding in Other Modules"
    - "🧾 Version History"
    - "🔐 Governance Footer"

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
Automated STAC Validation · DCAT/JSON-LD Checks · Provenance Verification · FAIR+CARE Metadata Integrity

</div>

---

## 🧭 Overview

The Metadata Validation & Trust Badge System ensures that **every KFM dataset, directory, and metadata artifact** complies with:

• STAC / DCAT / JSON-LD schema rules  
• Provenance requirements (SBOM, SLSA, signatures)  
• FAIR+CARE ethical metadata rules  
• KFM v11 Governance Standards  

It produces:

• A **metadata trust badge**  
• A **validation report**  
• CI evidence for governance review

---

## 🗂️ Directory Layout

~~~text
docs/telemetry/metadata-validation/
├── 📄 README.md                          # This file
│
├── 🧪 checks/                             # Core schemas and rule definitions
│   ├── stac-schema.json                   # STAC validator schema
│   ├── dcat-schema.json                   # DCAT-JSON schema
│   ├── jsonld-context.json                # JSON-LD context for expansion tests
│   └── provenance-rules.yaml              # SBOM / SLSA / signature rules
│
├── 🛠️ ci/                                 # CI validation workflows
│   ├── metadata-badge.yml                 # Badge emitter + validator runner
│   └── report-template.html               # HTML validation-report template
│
├── 📊 reports/                             # GitHub Pages–served output
│   └── index.html                          # Latest validation report
│
├── 🎨 badges/                              # JSON badge outputs (for shields.io)
│   └── metadata-badge.json
│
└── 🐍 scripts/                             # CLI tools for metadata validation
    ├── validate_metadata.py               # STAC/DCAT/LD/provenance/FAIR+CARE checks
    ├── render_report.py                   # HTML report builder
    └── utils.py                           # Shared helpers (context expansion, hashing)
~~~

---

## 🔍 Validator Coverage

### STAC Compliance  
• Structure validation  
• Required fields  
• Asset completeness  

### DCAT / JSON-LD  
• JSON-LD expansion  
• Missing terms  
• Semantic correctness  
• PROV-O lineage integrity  

### Provenance Integrity  
• SHA256 hashing  
• SBOM completeness  
• SLSA predicate validation  
• Signature checks  

### FAIR + CARE  
• FAIR F1/F2/F3  
• CARE-A / CARE-S / CARE-T  
• Indigenous sovereignty metadata  

---

## 🛡️ Trust Badge

To embed a metadata trust badge in any README:

Badge URL:  
https://img.shields.io/badge/metadata--validation-dynamic-blueviolet

Badge target page:  
https://<pages-domain>/docs/telemetry/metadata-validation/reports/index.html

Badge state updates automatically after each CI run.

---

## ⚙️ CI Workflow Logic

1. Run validators  
2. Summarize metadata health  
3. Emit badge JSON (status, color, path)  
4. Publish HTML report  
5. Attach governance evidence  
6. Gate merges if badge is failing (per metadata-governance rules)

---

## 📘 Reference Scripts

validate_metadata.py  
• Validates STAC/DCAT/JSON-LD/provenance/FAIR+CARE  

render_report.py  
• Generates human-readable HTML  
• Written into docs/telemetry/metadata-validation/reports/

Scripts support selective validation via `--roots`.

---

## 🧩 Embedding in Other Modules

Recommended directories to include the metadata trust badge:

• Any docs/data/ subtree  
• Any stac/ collection  
• Any pipelines/ directory that produces data  
• Any UI component that renders metadata  

---

## 🧾 Version History

• v11.2.3 — Initial centralized metadata-validation system  
• v11.2.2 — Schema consolidation  
• v11.2.0 — FAIR+CARE validator logic finalized  
• v10.4.x — Predecessor distributed validators  

---

<div align="center">

[📘 Docs Root](../../..) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md) · [📡 Telemetry Protocol v11](../../../standards/telemetry/README.md)

</div>