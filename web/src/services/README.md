---
title: "🔌 Kansas Frontier Matrix — Web Services Layer Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/services/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-services-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-services-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/services/README.md@v10.0.0"
  - "web/src/services/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-services-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-services-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-services-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-services-readme"
event_source_id: "ledger:web/src/services/README.md"
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
sunset_policy: "Superseded upon next services-layer update"
---

<div align="center">

# 🔌 **Kansas Frontier Matrix — Web Services Layer Overview**  
`web/src/services/README.md`

**Purpose:**  
Provide a comprehensive, FAIR+CARE-aligned overview of the **Services Layer** within the  
KFM Web Platform.  
The services in `web/src/services/**` manage API communication, schema validation, provenance enforcement,  
telemetry export, STAC/DCAT integration, and Focus Mode v2.5 data orchestration — forming the  
core data I/O backbone for the KFM frontend.

</div>

---

# 📘 Overview

The Services Layer handles **all external communication** between the KFM Web Platform (`web/src/**`)  
and backend systems, including:

- REST API requests  
- GraphQL queries and mutations  
- STAC/DCAT dataset discovery  
- Governance metadata retrieval  
- Telemetry submission  
- Provenance-aware interactions  
- Ethical and accessibility-aware transformation rules  
- Schema and type validation before rendering  

Services must always:

- Be deterministic  
- Validate all inbound & outbound payloads  
- Respect CARE governing rules  
- Respect ai_transform_prohibited flags  
- Generate telemetry traces for observability  

---

# 🧱 Directory Structure

~~~text
web/src/services/                 # Web Platform Services Layer
├── apiClient.ts                  # Unified REST/GraphQL client w/ error taxonomy
├── stacService.ts                # STAC v1.0.0 Collection/Item integration
├── dcatService.ts                # DCAT v3 Dataset/Distribution integration
├── telemetryService.ts           # WebVitals + A11y + story/focus telemetry export
└── governanceService.ts          # CARE, license, provenance, sovereignty lookup
~~~

---

# 🧩 Responsibilities of the Services Layer

### 1. **API Communication**
Handles:

- REST endpoints (`/api/focus`, `/api/storynodes`, `/api/timeline`, etc.)  
- GraphQL queries (story nodes, focus payloads, relations, metadata)  
- Consistent error taxonomy (`RenderingError`, `NarrativeError`, `GovernanceError`, etc.)

### 2. **Schema Validation**
Before **any** data enters the React UI:

- Story Node v3 schemas validated  
- Focus Mode payload schemas validated  
- STAC/DCAT metadata schemas validated  
- Telemetry event schemas validated  

Services act as a **firewall layer**, preventing malformed or unverifiable data from breaking the UI.

### 3. **FAIR+CARE Enforcement**
The Services Layer ensures:

- No disallowed spatial coordinates are passed upward  
- Redaction / masking metadata stays attached  
- CARE flags are always delivered to UI components  
- Provenance metadata is available for display  
- Ethical constraints override rendering when required  

### 4. **Telemetry Export**
Services push telemetry events for:

- WebVitals  
- Navigation  
- Map interactions  
- Focus Mode usage  
- Story Node engagement  
- A11y interactions  
- Sustainability metrics  

Telemetry must always be:

- Schema-valid  
- Aggregated, never PII  
- Stored in release bundles under `/releases/**`

### 5. **STAC/DCAT Integration**
Handles dataset discovery:

- Reads COG footprints  
- Loads metadata (title, description, license, publisher)  
- Applies time filters from TimeContext  
- Validates Items/Collections with schema guards  

### 6. **Governance Integration**
Includes:

- CARE labels (e.g., Public / Restricted / Sovereignty-Controlled)  
- Spatial masking rules (H3 r7+)  
- License and rights-holder retrieval  
- Provenance chain handling  
- AI explanation provenance markers  

Governance-aware services help ensure UI components display correct ethical state.

---

# 🔌 Unified API Client (`apiClient.ts`)

### Features:

- TypeScript-first (strict mode)  
- Request/response type-guards  
- Automatic schema-checking  
- Built-in telemetry events  
- Built-in governance hooks  
- Automatic provenance tracking  
- Error taxonomy alignment  

### Example Usage (pseudocode):

~~~ts
const result = await apiClient.get("/api/focus/123", {
  validate: focusSchema,
  governance: true,
  telemetry: "focus:select"
});
~~~

---

# 🌐 STAC Service (`stacService.ts`)

Responsibilities:

- Query STAC endpoints  
- Filter by temporal/spatial extent  
- Parse raster/vector assets  
- Surface provenance & license metadata  
- Validate COG footprints  
- Support Story Node v3 & Focus Mode suggestions  

Outputs must always include:

- `bbox`
- `temporal`
- `license`
- `provenance`
- `assets`

---

# 📦 DCAT Service (`dcatService.ts`)

Handles:

- Dataset discovery for DCAT v3  
- Mapping dataset distributions to STAC assets  
- Temporal/spatial metadata retrieval  
- License handling  

All distributions must undergo schema-checking and FAIR+CARE validation.

---

# 📈 Telemetry Service (`telemetryService.ts`)

Collects and exports:

- WebVitals  
- Map interactions  
- A11y interactions  
- Focus Mode events  
- Story Node engagement metrics  
- Error taxonomy logs  
- Sustainability metrics (Wh, CO₂)  

Telemetry is written to:

`releases/<version>/focus-telemetry.json`

---

# 🛡 Governance Service (`governanceService.ts`)

Provides:

- CARE metadata extraction  
- License lookup  
- Provenance chain lookup  
- Sovereignty masking rules  
- AI governance metadata bindings  

Used by:

- Focus Mode panels  
- Story Node components  
- Dataset explorers  
- Timeline + Map sync  

---

# 🧪 Testing Requirements

Every service must have:

- Unit tests  
- Integration tests  
- Schema guards  
- Governance & CARE tests  
- Telemetry correctness tests  
- Error taxonomy tests  

Tests live under:

~~~text
tests/integration/web/services/**
tests/unit/web/services/**
~~~

CI **blocks** PRs if service tests fail.

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite for KFM-MDP v10.4; governance, telemetry, STAC/DCAT compliance added |
| v10.3.2 | 2025-11-14 | Enhanced Focus Mode + Story Node bindings |
| v10.3.1 | 2025-11-13 | Initial service layer documentation |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  

</div>