---
title: "🛡️ KFM — Air Quality Data Governance"
path: "data/air-quality/governance/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Data Architecture Board"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Governance README"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles: []

intent: "air-quality-governance-readme"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "air-quality"
  applies_to:
    - "data/air-quality/**"
    - "air-quality-stac"
    - "air-quality-dcat"
    - "air-quality-prov"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (review for sensitive monitor sites, private facilities, or restricted locations)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
owner: "KFM Core · Data Engineering"
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next governed air-quality governance revision"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

source_files:
  - "data/air-quality/governance/README.md"
build_inputs:
  - "docs/standards/governance/ROOT-GOVERNANCE.md"
  - "docs/standards/faircare/FAIRCARE-GUIDE.md"
  - "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
provenance_chain:
  - "manual-authoring"
  - "ci:markdown-lint"
  - "ci:schema-lint"
  - "ci:footer-check"
  - "ci:pii-scan"
  - "ci:secret-scan"

story_node_refs: []
immutability_status: "mutable-plan"

doc_uuid: "urn:kfm:doc:data:air-quality:governance:v11.2.6"
semantic_document_id: "kfm-data-air-quality-governance-v11.2.6"
event_source_id: "ledger:kfm:doc:data:air-quality:governance:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "semantic-highlighting"
    - "metadata-extraction"
    - "layout-normalization"
    - "a11y-adaptations"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

# 🛡️ KFM — Air Quality Data Governance

> **Purpose**  
> Define the governance contract for everything under `data/air-quality/**`: how air‑quality data is stored, classified, licensed, validated, and published into STAC/DCAT with PROV lineage—without violating FAIR+CARE or sovereignty controls.

---

## 📘 Overview

This folder exists to make air‑quality data in KFM:

- **Traceable** (inputs → transforms → outputs)
- **Governable** (classification, sensitivity, stewardship, CARE considerations)
- **Publishable** (STAC/DCAT outputs are compliant and reversible)
- **Safe** (no secrets/PII; restricted locations handled per policy)

### Scope
Applies to:
- raw ingests and derived artifacts in `data/air-quality/**`
- metadata catalogs for air-quality (`data/stac/**`, `data/dcat/**`)
- provenance artifacts (`data/prov/**` or STAC assets)

Out of scope:
- writing new policy (policy lives in governed standards linked below)
- bypassing review (governance and release boards retain authority)

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
└── 📁 data/
    └── 📁 air-quality/
        ├── 📁 governance/
        │   └── 📄 README.md                           — This governance contract
        ├── 📁 raw/                                    — Unmodified ingests (treat as append-only)
        ├── 📁 processed/                               — Governed derived artifacts (commit-worthy)
        ├── 📁 stac/                                   — Air-quality STAC Items/Collections (publishable)
        ├── 📁 dcat/                                   — Air-quality DCAT exports (publishable)
        └── 📁 prov/                                   — Provenance bundles (optional; may also live as STAC assets)
~~~

Notes:
- If any of the sibling folders are missing in your current repo state, create them only via governed PRs.
- Do not add ad-hoc folders that bypass catalogs or provenance expectations.

---

## 📦 Data & Metadata

### Minimum governed metadata per publishable air-quality artifact
For each publishable dataset/artifact in `data/air-quality/processed/**`:

- **STAC**
  - a STAC Item (or Collection) describing the artifact’s spatiotemporal scope
  - checksum / versioning where applicable
- **DCAT**
  - dataset record and distribution(s) for the published artifact(s)
- **PROV**
  - run-level provenance (activity, used inputs, generated outputs)
- **Licensing**
  - dataset-level license recorded and compatible with publication target

### Classification and sensitivity
Air-quality datasets can include:
- public monitoring feeds (often low sensitivity)
- facility-adjacent sensors, private monitors, or community reports (potentially sensitive)
- locations that intersect sovereign or culturally sensitive areas (apply sovereignty policy)

Apply the most restrictive handling required by:
- governance charter
- FAIR+CARE guidance
- sovereignty / indigenous data protection policy

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC** is the primary spatial discovery surface for air-quality artifacts.
- **DCAT** is the catalog view for dataset/distribution publication and federation.
- **PROV** is required for auditability and graph lineage.

Recommended mapping (high level):
- Air-quality artifact file(s) → STAC asset(s)
- Artifact generation run → PROV `prov:Activity`
- Source and derived files → PROV `prov:Entity`
- Dataset publication record → DCAT `dcat:Dataset` + `dcat:Distribution`

---

## 🧪 Validation & CI/CD

Minimum expectations before any publishable air‑quality artifact is merged:
- metadata schema checks pass (`schema-lint`)
- docs and README compliance passes (`markdown-lint`, `footer-check`)
- PII and secrets scans pass (`pii-scan`, `secret-scan`)
- provenance is present and coherent (`provenance-check`) where the workflow requires it

If validation requirements differ by release stage, the governing standards control.

---

## ⚖ FAIR+CARE & Governance

### Required governed behaviors
- **No secrets** in data, configs, logs, or metadata.
- **No PII** in publishable artifacts.
- **Location caution**: if a dataset could reveal sensitive locations, apply masking/generalization per sovereignty policy and governance rules.
- **License clarity**: do not publish air-quality artifacts without an explicit license and redistribution posture.
- **Stewardship**: ensure dataset ownership and contact pathway are maintained (human accountability).

### When in doubt
If a dataset’s sensitivity is unclear:
- treat as restricted until reviewed by the appropriate council/board
- document the uncertainty in a governance note (do not guess)

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-16 | Initial governed air-quality data governance README |

---

<div align="center">

🛡️ **KFM — Air Quality Data Governance**  
Documentation-First · FAIR+CARE Governance · Sustainable Intelligence  

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" /> 
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" /> 
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" /> 

[📘 Docs Root](../../../docs/README.md) ·
[📂 Standards Index](../../../docs/standards/README.md) ·
[📄 Templates Index](../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6  

</div>
