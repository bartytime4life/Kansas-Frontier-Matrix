---
title: "🔧 Kansas Frontier Matrix — Web Pipelines Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-pipelines-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-pipelines-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/README.md@v10.0.0"
  - "web/src/pipelines/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-pipelines-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-pipelines-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-pipelines-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-pipelines-readme"
event_source_id: "ledger:web/src/pipelines/README.md"
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
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded on next web pipeline overhaul"
---

<div align="center">

# 🔧 **Kansas Frontier Matrix — Web Source Pipelines Overview**  
`web/src/pipelines/README.md`

**Purpose:**  
Provide a FAIR+CARE-aligned overview of the **frontend orchestration pipelines** in `web/src/pipelines/**`, which  
coordinate data retrieval, schema validation, governance enforcement, Focus Mode v2.5 orchestration, timeline–map  
synchronization, STAC/DCAT flows, and UI state propagation.

</div>

---

# 📘 Overview

The **Pipelines Layer** is the “brain” of the Web Platform — connecting UI components, services, state contexts,  
telemetry, and governance rules into coherent, predictable flows.

Pipelines:

- Are deterministic and type-safe  
- Enforce schema + governance validation  
- Operate as orchestration layers (NOT UI, NOT API clients)  
- Bind together multiple services, hooks, and contexts  
- Ensure no data enters the UI unvalidated or ungoverned  
- Drive major KFM features: Focus Mode, Story Node v3, Map/Timeline sync, STAC/DCAT exploration  
- Generate telemetry traces for observability  

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/
├── focusPipeline.ts            # Focus Mode v2.5 orchestration
├── stacPipeline.ts             # STAC dataset discovery + temporal syncing
├── storyPipeline.ts            # Story Node v3 + Focus Mode combined flow
└── timelinePipeline.ts         # Timeline → map → narrative propagation
~~~

---

# 🧩 Pipeline Architecture

Pipelines operate in a **layered orchestration model**:

### 1. **Input Stage**
- Receives events from user interactions  
  - Selecting an entity  
  - Moving the timeline  
  - Choosing a dataset  
  - Activating a Focus Mode item  

### 2. **Service Stage**
- Calls backend APIs via:
  - `apiClient.ts` (REST/GraphQL)  
  - `stacService.ts`  
  - `dcatService.ts`  
  - `governanceService.ts`  
- Performs schema guards before continuing  

### 3. **Governance Stage**
- Enforces:
  - CARE metadata  
  - Sovereignty masking (H3 r7+)  
  - License/rights-holder requirements  
  - Provenance chain injection  
  - Ethical AI boundaries  

### 4. **Transformation Stage**
- Shapes data for UI components:
  - Story Node v3 assembly  
  - Focus Mode narrative packages  
  - Timeline + geometry alignment  
  - Footprint + map layer styling  

### 5. **Telemetry Stage**
- Emits telemetry events:
  - WebVitals  
  - Focus Mode usage  
  - Story Node interaction  
  - Map interactions  
  - A11y events  
  - Sustainability metrics  

### 6. **Output Stage**
- Updates Context Providers:
  - FocusContext  
  - TimeContext  
  - GovernanceContext  
  - A11yContext  
  - ThemeContext  
- Triggers UI re-renders  

---

# 🔧 Focus Mode Pipeline (`focusPipeline.ts`)

### Responsibilities

- Fetch and validate Focus Mode payloads  
- Merge Story Nodes + graph relations  
- Enforce FAIR+CARE:
  - Labeling  
  - Restrictions  
  - No unverified historical claims  
- Highlight relevant map features  
- Suggest related Story Nodes  
- Push telemetry entries for narrative exploration  

### Guarantees

- No speculative or hallucinated relationships  
- JSON schema validation before UI use  
- Provenance chips always present  
- AI-generated text is clearly labeled  

---

# 🗺️ STAC Pipeline (`stacPipeline.ts`)

### Responsibilities

- Query STAC endpoints  
- Filter by:
  - Time  
  - Bounding box  
  - Dataset type  
- Validate Items/Collections  
- Extract COG metadata  
- Align footprints with MapLibre  
- Produce dataset previews for UI  

### Guarantees

- All STAC payloads are schema-checked  
- Licensing, provenance, temporal extents always surfaced  
- CARE-sensitive datasets flagged immediately  

---

# 📖 Story Node Pipeline (`storyPipeline.ts`)

### Responsibilities

- Assemble Story Node v3 narrative payloads  
- Validate against Story Node schema  
- Integrate with Focus Mode  
- Align map geometry + timeline range  
- Provide contextual connections across narrative layers  

### Guarantees

- Narrative content is clearly segmented  
- Temporal and geospatial consistency enforced  
- CARE rules fully respected  

---

# ⏱️ Timeline Pipeline (`timelinePipeline.ts`)

### Responsibilities

- Synchronize:
  - Timeline → Map  
  - Timeline → Focus Mode  
  - Timeline → Story Node lists  
- Apply time filters to:
  - Vector layers  
  - Story Node markers  
  - Focus Mode neighborhood  
- Emit telemetry for timeline interactions  

### Guarantees

- No stale or inconsistent temporal state  
- OWL-Time alignment maintained  
- Timeline filters propagate deterministically  

---

# 🎛 Pipeline Invariants

All pipelines must obey the following invariants:

- **Type Safety:** All inputs/outputs strongly typed  
- **Schema Validity:** Data must pass JSON schema guards  
- **Governance:** CARE & provenance enforced at pipeline level  
- **A11y:** Pipelines must not bypass accessibility states  
- **Telemetried:** Every major action logged ethically  
- **Deterministic:** No random branching or unstable behavior  
- **No UI Logic:** Pipelines never manipulate visual state directly  

---

# 🧪 Testing Requirements

Pipelines must have:

- Unit tests  
- Integration tests  
- Governance tests  
- Schema validation tests  
- Telemetry correctness tests  
- Temporal/spatial propagation tests  
- Focus Mode relationship tests (where applicable)  

Test locations:

~~~text
tests/unit/web/pipelines/**
tests/integration/web/pipelines/**
~~~

CI requires all pipeline tests to pass before merging.

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite under KFM-MDP v10.4; added governance, telemetry, STAC, Story Node, Focus Mode flows |
| v10.3.2 | 2025-11-14 | Improved synchronization logic + STAC integration |
| v10.3.1 | 2025-11-13 | Initial pipeline overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>