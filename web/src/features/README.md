---
title: "✨ Kansas Frontier Matrix — Web Features Layer Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-features-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
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
doc_uuid: "urn:kfm:doc:web-features-readme-v10.4.0"
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
Provide a comprehensive, FAIR+CARE-governed overview of the **Features Layer** within the  
KFM Web Platform (`web/src/features/**`) — encapsulating self-contained functional modules  
that integrate UI components, hooks, pipelines, governance metadata, geospatial logic, and  
telemetry instrumentation.

</div>

---

# 📘 What Are “Features” in the KFM Web Platform?

The **Features Layer** groups functionality into **modular, domain-focused slices** that  
combine components, hooks, services, governance overlays, and pipelines into cohesive  
experience units.

A Feature = *User-facing capability* with:

- Its own internal logic  
- Reusable components  
- Routing entry points  
- Governance + CARE metadata  
- A11y requirements  
- Telemetry instrumentation  
- Schema + provenance constraints  

Examples include: Focus Mode, Story Nodes, Data Explorer, Map Tools, Legends, and more.

---

# 🧱 Directory Structure

~~~text
web/src/features/
├── focus-mode/                    # Focus Mode v2.5 entity-centered reasoning
│   ├── components/                # Focus panels, related entities, AI explanations
│   ├── hooks/                     # useFocusFeature, useRelatedEntities, etc.
│   ├── pipelines/                 # Composition of focusPipeline + governance rules
│   ├── governance/                # CARE badge logic for focus flows
│   └── telemetry/                 # Focus Mode usage + A11y event reporting
│
├── story-nodes/                   # Story Node v3 feature slice
│   ├── components/                # Cards, detail views, micro-maps
│   ├── hooks/                     # useStoryNodeFeature, useStoryRelations
│   ├── pipelines/                 # storyPipeline.ts integration
│   ├── geospatial/                # Story Node footprint transforms
│   └── telemetry/                 # Story Node reading + interaction analytics
│
├── data-explorer/                 # STAC/DCAT dataset exploration
│   ├── components/                # Filters, dataset cards, previews
│   ├── hooks/                     # useDatasetSearch, useDatasetPreview
│   ├── pipelines/                 # stacPipeline.ts integration
│   ├── governance/                # Dataset licensing, CARE metadata
│   └── telemetry/                 # Dataset browsing usage metrics
│
├── map-tools/                     # Map interactions, legends, layer toggles
│   ├── components/                # Cursor inspector, layer toggles, legend UI
│   ├── hooks/                     # useMapTools, useLegend
│   ├── configs/                   # Legend definitions, color ramps
│   └── telemetry/                 # Map tool usage metrics
│
├── timeline/                      # Timeline feature slice
│   ├── components/                # Timeline UI, range sliders, granularity controls
│   ├── hooks/                     # useTimelineFeature
│   ├── pipelines/                 # timelinePipeline.ts integration
│   └── telemetry/                 # Temporal navigation metrics
│
└── governance/                    # Governance viewer (CARE/Provenance/etc.)
    ├── components/                # Rights-holder info, stewardship data
    ├── hooks/                     # useGovernanceFeature
    ├── schemas/                   # Governance JSON-LD schemas
    └── telemetry/                 # Governance viewer engagement stats
~~~

---

# 🧩 Feature Layer Responsibilities

## 1. **User-Focused Architecture**
Features define *what a user can do*:

- View a Story Node  
- Explore a dataset  
- Toggle map layers  
- Enter Focus Mode  
- Inspect provenance  
- Navigate timeline ranges  

Each of these experiences is isolated into its own feature slice.

---

## 2. **Feature Composition Pattern**

Each feature commonly provides:

- `components/` → UI building blocks  
- `hooks/` → Feature-specific logic  
- `pipelines/` → Orchestration logic  
- `governance/` → CARE + provenance metadata  
- `telemetry/` → Usage + performance signals  
- `configs/` → Feature-specific rules (optional)  
- `schemas/` → Validation schemas (optional)  
- `geospatial/` → Spatial-specific logic (optional)

This ensures predictable, reproducible structure across the Web Platform.

---

# 🧠 Integration With Other Layers

Features **bridge**:

- Hooks → State management  
- Pipelines → Data orchestration  
- Services → API & STAC/DCAT communication  
- Context → Time, Focus, A11y, Governance  
- Components → UI  
- Geospatial Pipelines → Map/3D interactions  
- Telemetry → Observability  

Features **may use** other features but must not create circular dependencies.

---

# 🔐 Governance & FAIR+CARE Responsibilities

All features must:

- Display correct CARE labels  
- Respect sovereignty redaction rules  
- Prevent sensitive geometry exposure  
- Annotate AI-generated narratives  
- Preserve provenance metadata  
- Obey `ai_transform_prohibited` constraints  
- Ensure no harmful interpretations are surfaced  

Governance failures **block merges in CI**.

---

# ♿ Accessibility (WCAG 2.1 AA)

Each feature MUST:

- Provide keyboard navigation  
- Apply proper ARIA roles  
- Include alt text for icons/images  
- Respect reduced-motion settings  
- Use A11y tokens  
- Provide accessible color ramps in legends & visualizations  

A11y regressions **fail CI**.

---

# 📈 Telemetry Responsibilities

Features generate telemetry for:

- User flow initiation  
- Feature-specific interactions  
- Sustainability metrics  
- A11y usage metrics  
- Narrative + spatial exploration  
- Focus Mode usage  
- Dataset browsing  

Telemetry MUST be:

- Schema-valid  
- Non-PII  
- Aggregated  
- Release-exported  

Telemetry appears in:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Each feature must include:

- Unit tests  
- Integration tests  
- E2E tests for user flows  
- Governance tests  
- A11y tests  
- Telemetry tests  
- Schema validation tests (if applicable)  

Test structure:

~~~text
tests/unit/web/features/<feature>/**
tests/integration/web/features/<feature>/**
tests/e2e/web/features/<feature>/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete rewrite under KFM-MDP v10.4; added structure for Focus, Story Nodes, STAC/DCAT, governance, and telemetry features |
| v10.3.2 | 2025-11-14 | Added governance + dataset explorer alignment |
| v10.3.1 | 2025-11-13 | Initial baseline structure |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>