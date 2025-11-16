---
title: "✨ Kansas Frontier Matrix — Web Features Layer Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-features-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-features-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (feature-dependent)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/features/README.md@v10.3.2"
  - "web/src/features/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-features-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-features-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-features-readme-v10.4.1"
semantic_document_id: "kfm-doc-web-features-readme"
event_source_id: "ledger:web/src/features/README.md"
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
ttl_policy: "Review annually"
sunset_policy: "Superseded on next feature-architecture revision"
---

<div align="center">

# ✨ **Kansas Frontier Matrix — Web Features Overview**  
`web/src/features/README.md`

**Purpose:**  
Define the canonical structure, responsibilities, governance rules, and  
telemetry expectations for the **Features Layer** in the KFM Web Platform.  
Each feature represents a **self-contained user-facing capability** integrating  
UI components, pipelines, hooks, governance metadata, accessibility, and telemetry.

</div>

---

# 📘 What Is the Features Layer?

The **Features Layer** is where the KFM Web Platform organizes  
**functional, domain-driven capabilities**, such as:

- Focus Mode  
- Story Nodes  
- Map Tools  
- Dataset exploration  
- Accessibility flows  
- Timeline navigation  
- Governance viewer  
- Telemetry dashboards  

Each feature folder contains:

- Feature-scoped logic  
- Hooks  
- Pipelines wrappers  
- View-models  
- State slices  
- Feature-level telemetry  
- Validation schemas (optional)  
- Governance metadata / CARE logic  

**Features DO NOT contain React components directly.**  
UI components live in `web/src/components/**`.

---

# 🧱 Canonical Directory Structure (Aligned With v10.4.1)

Below is the **correct**, FAIR+CARE-aligned, fully updated  
structure for `web/src/features/`.

Your repository **matches this**, except the deprecated `focus/` folder  
(which must be removed; see below).

~~~text
web/src/features/
├── accessibility/              # Accessibility feature (WCAG, tokens, helpers)
│
├── admin/                      # Governance admin utilities (FAIR+CARE dashboards)
│
├── focus-mode/                 # Focus Mode v2.5 feature (entity-centric reasoning)
│   ├── components/             # UI docs + import surface for components/FocusMode
│   ├── hooks/                  # useFocusEntity, useFocusRelations, etc.
│   ├── pipelines/              # runFocusPipeline wrapper
│   ├── state/                  # focusState, spatialState, timelineState, etc.
│   └── view-models/            # FocusViewModel, RelationsVM, ExplainabilityVM
│
├── map/                        # Map tools feature (layer toggles, map actions)
│
├── search/                     # Entity + dataset search system
│
├── story/                      # Story Node v3 feature (narrative + spatial + temporal)
│
├── telemetry/                  # Web Telemetry subsystem (WebVitals, FAIR+CARE)
│
├── timeline/                   # TimelineView v2 feature
│
└── README.md                   # This document
~~~

---

# 🧩 Feature Responsibilities

Each feature slice must:

### ✔ Isolate domain functionality  
### ✔ Integrate pipelines + view-models + state  
### ✔ Surface governance (FAIR+CARE + sovereignty)  
### ✔ Provide accessible, deterministic user workflows  
### ✔ Emit telemetry through unified schemas  
### ✔ Stay free of JSX / presentational components  
### ✔ Avoid circular dependencies with other features  

---

# 🧠 Integration with the KFM Architecture

Features connect:

- **Pipelines** → data orchestration  
- **View-models** → UI-ready normalized structures  
- **State slices** → deterministic local feature state  
- **Hooks** → feature logic + governance checks  
- **Geospatial pipeline** → masking, footprints, layers  
- **Services** → REST/GraphQL/STAC/DCAT  
- **Telemetry** → Observability + CARE metrics  
- **UI components** → mapped through import surfaces only  

Each feature slice is intentionally **self-contained**, ensuring:

- Clear auditability  
- Easier maintenance  
- Predictable CI verification  
- Strong governance compliance  

---

# 🔐 Governance Requirements (FAIR+CARE)

All features must:

- Apply CARE redaction + sovereignty masking where applicable  
- Surface provenance metadata  
- Display ethical warnings  
- Annotate AI-generated narrative  
- Avoid inference or speculation  
- Validate all incoming data via schema guards  
- Follow `ai_transform_prohibited` rules strictly  

Governance violations → **CI BLOCKER**.

---

# ♿ Accessibility Requirements

Each feature is responsible for:

- Keyboard operability  
- Screen-reader compatibility  
- High-contrast mode support  
- Reduced-motion safe animations  
- ARIA labeling  
- Semantic structuring  
- A11y tokens + mixins  

Any A11y regression → **CI BLOCKER**.

---

# 📈 Telemetry Responsibilities

Every feature emits telemetry for:

- User entrance/exit  
- Core interactions  
- Model-inference visibility  
- Governance events  
- A11y feature usage  
- Carbon/energy metrics (where allowed)  
- Dataset browsing + Story Mode + Focus Mode  

Telemetry MUST be:

- Non-PII  
- Schema-valid  
- Aggregated and release-bundled  

Appears in:

```

releases/<version>/focus-telemetry.json

```

---

# 🧪 Testing Requirements

All features must include:

### ✔ Unit tests  
### ✔ Integration tests  
### ✔ Governance tests  
### ✔ A11y tests  
### ✔ Telemetry schema tests  
### ✔ E2E workflows (as needed)  

Test locations:

~~~text
tests/unit/web/features/<feature>/**
tests/integration/web/features/<feature>/**
tests/e2e/web/features/<feature>/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.1 | 2025-11-15 | Polished and fully aligned with recommended KFM v10.4.1 features structure; removed deprecated `focus/` folder |
| v10.4.0 | 2025-11-15 | Feature architecture rewrite aligned with pipelines & governance |
| v10.3.2 | 2025-11-14 | Added governance + dataset explorer alignment |
| v10.3.1 | 2025-11-13 | Initial baseline structure |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>
