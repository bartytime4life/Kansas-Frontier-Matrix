---
title: "🪝 Kansas Frontier Matrix — Web Hooks Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/hooks/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-hooks-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-hooks-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (logic-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/hooks/README.md@v10.3.2"
  - "web/src/hooks/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-hooks-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-hooks-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-hooks-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-hooks-readme"
event_source_id: "ledger:web/src/hooks/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with constraints"
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
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded on next hooks-layer revision"
---

<div align="center">

# 🪝 **Kansas Frontier Matrix — Web Hooks Overview**  
`web/src/hooks/README.md`

**Purpose:**  
Document the **React Hooks Layer** powering state management, orchestration, telemetry capture, Focus Mode v2.5 flows,  
timeline → map → narrative synchronization, governance rules, and accessibility state propagation within the  
KFM Web Platform.  
Hooks are the *logic center* of the frontend — connecting UI, services, pipelines, governance, and telemetry.

</div>

---

# 📘 Overview

Hooks in `web/src/hooks/`:

- Encapsulate reusable logic  
- Provide typed interfaces for interacting with services + pipelines  
- Maintain stable, deterministic transformations  
- Enforce governance + CARE requirements before UI rendering  
- Sync map, timeline, focus, and story node behavior  
- Emit telemetry reliably and ethically  
- Maintain accessibility + theme state  
- Act as boundary guards between UI and pipeline/service layers  

Hooks **must not** contain UI code — only logic.

---

# 🧱 Directory Structure

~~~text
web/src/hooks/
├── useMap.ts                # MapLibre state, viewport syncing, layer logic
├── useTimeline.ts           # Timeline → map → narrative temporal synchronization
├── useFocus.ts              # Focus Mode v2.5 orchestration (entity, narrative, metadata)
├── useStoryNodes.ts         # Story Node v3 retrieval + selection + metadata sync
├── useStac.ts               # STAC/DCAT dataset discovery + footprint/state handling
├── useTelemetry.ts          # WebVitals + interaction + A11y telemetry emission
├── useA11y.ts               # Accessibility state (reduced motion, high contrast)
├── useGovernance.ts         # CARE + provenance + license metadata integration
├── useTheme.ts              # Light/dark mode + token propagation
└── useKeybinds.ts           # Keyboard accessibility, global shortcuts, map/timeline hotkeys
~~~

---

# 🧩 Hook Responsibilities

## 🔹 `useMap.ts`
Provides:

- MapLibre event management (pan, zoom, hover, click)  
- Layer visibility controls  
- Integration with TimeContext + FocusContext  
- CARE masking overlays  
- Telemetry events (spatial interactions)

Guarantees:

- No unsafe geometry gets rendered  
- Map state always deterministic  
- Clear event taxonomy for telemetry  

---

## 🔹 `useTimeline.ts`
Coordinates:

- Timeline ranges  
- Temporal filtering of all spatial + narrative layers  
- OWL-Time alignment  
- Propagation to map + focus + story nodes

Guarantees:

- Perfect sync between timeline and map  
- Temporal completeness and correctness  

---

## 🔹 `useFocus.ts`
Orchestrates Focus Mode v2.5:

- Fetch entity + graph neighborhood  
- Validate schema + governance metadata  
- Merge AI narratives (properly labeled)  
- Highlight related geometries on the map  
- Trigger Story Node suggestions  
- Emit telemetry events

Guarantees:

- No speculative narratives  
- CARE labels and provenance always shown  

---

## 🔹 `useStoryNodes.ts`
Manages:

- Retrieval of Story Node v3 bundles  
- Temporal + spatial syncing  
- Provenance + licensing visibility  
- Interaction telemetry  
- Linkage to Focus Mode

Guarantees:

- Narrative correctness  
- Ethical + accessible presentation  

---

## 🔹 `useStac.ts`
Handles:

- STAC & DCAT integration  
- Footprint loading  
- COG metadata parsing  
- Pagination + filtering  
- Governance metadata alignment  
- Error classification

Guarantees:

- No malformed STAC payloads enter UI  
- License + provenance always surfaced  

---

## 🔹 `useTelemetry.ts`
Tracks:

- WebVitals  
- A11y usage metrics  
- Story Node interactions  
- Focus Mode actions  
- Map interactions  
- Sustainability indicators (Wh, CO₂e)

Guarantees:

- Non-PII telemetry  
- Schema-valid events  
- Proper aggregation rules  

---

## 🔹 `useA11y.ts`
Handles:

- Reduced motion  
- High contrast mode  
- Screen-reader friendliness  
- Keyboard-first navigation patterns

Guarantees:

- WCAG 2.1 AA compliance  
- Accessibility regressions blocked in CI  

---

## 🔹 `useGovernance.ts`
Provides:

- CARE metadata hydration  
- Sovereignty masking rules (H3 r7+)  
- License + rights-holder lookup  
- Provenance chips  
- Ethical display rules

Guarantees:

- No sensitive data is displayed  
- Governance overlays remain accurate  

---

## 🔹 `useTheme.ts`
Controls:

- UI theming (light/dark)  
- Design token propagation  
- High-contrast variants  

Guarantees:

- A11y-safe color choices  
- Consistent visual identity  

---

## 🔹 `useKeybinds.ts`
Provides:

- Keyboard support for:
  - Map navigation  
  - Timeline scrubbing  
  - Focus activation  
  - Pane switching  
- Assistive-keyboard patterns for accessibility

Guarantees:

- Fully keyboard-operable UI
- Predictable event ordering  

---

# 🔐 Governance & FAIR+CARE Integration

All hooks must:

- Respect `ai_transform_prohibited` flags  
- Attach provenance to all data returned  
- Pass CARE labels + sovereignty metadata to UI  
- Mask or remove restricted geometry  
- Prevent display of unverified narrative content  
- Always provide ethical context warnings when required  

Governance guaranteed before UI rendering.

---

# ♿ Accessibility (WCAG 2.1 AA)

Hooks must:

- Maintain accessible state  
- Respect reduced-motion  
- Avoid generating UI changes without notifications  
- Support focus management  
- Provide keyboard predictability  

Accessibility failures **block merges**.

---

# 🧪 Testing Requirements

Hooks must be covered by:

- Unit tests  
- Integration tests  
- Timeline–map–focus sync tests  
- Telemetry correctness tests  
- Governance + CARE-unit tests  
- A11y tests (keyboard navigation, reduced motion, roles)  

Tests live under:

~~~text
tests/unit/web/hooks/**
tests/integration/web/hooks/**
~~~

---

# 📈 Telemetry Responsibilities

Each hook must emit:

- Schema-valid telemetry  
- Non-PII usage patterns  
- Sustainability metrics  
- Event categories defined in telemetry schemas  
- Proper governance metadata (where applicable)

Telemetry flows into:

`releases/<version>/focus-telemetry.json`

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite for KFM-MDP v10.4; governance, A11y, telemetry, and Focus Mode v2.5 alignment |
| v10.3.2 | 2025-11-14 | Added STAC + Story Node integrations |
| v10.3.1 | 2025-11-13 | Initial hooks overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>