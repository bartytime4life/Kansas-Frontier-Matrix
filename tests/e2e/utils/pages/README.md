---
title: "📄 Kansas Frontier Matrix — E2E Page Objects & Selectors (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/utils/pages/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-pages-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-pages-readme"
doc_uuid: "urn:kfm:tests:e2e:pages:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/utils/pages/README.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/tests-e2e-v11.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

provenance_chain:
  - "tests/e2e/utils/pages/README.md@v11.2.6"
---

<div align="center">

# 📄 **Kansas Frontier Matrix — E2E Page Objects & Selectors (v11 LTS)**
`tests/e2e/utils/pages/README.md`

**Purpose**  
Define the canonical Page Object layer for KFM E2E tests: stable page models, role-first selectors, deterministic wait strategies, and governance-safe UI interaction patterns for Map/Timeline/Narrative flows.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧭 E2E Guide](../../README.md) ·
[🧰 E2E Utils](../README.md) ·
[🧾 Assertions](../assertions/README.md)

</div>

---

## 📘 Overview

The Page Object layer exists to make E2E tests:

- **stable** across UI refactors (selectors don’t break on CSS changes)
- **accessible by default** (role/name/label selection patterns)
- **deterministic** (explicit readiness checks instead of sleeps)
- **governance-aware** (safe handling of restricted surfaces and masked content)
- **auditable** (page actions map to user workflows and CI artifacts)

### Page Objects (KFM definition)
A Page Object is a small module that:
- exposes **intent-based actions** (e.g., `openStoryNode(id)`, `toggleLayer(name)`)
- exposes **stable locators** (role-first; data-testid only when needed)
- encapsulates **wait and readiness logic** for that page surface

Page Objects are not test suites. They are shared utilities used by suites.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 utils/
        └── 📁 pages/
            ├── 📄 README.md                      — This guide (page patterns + selector contracts)
            ├── 📄 app.page.ts                    — Global app shell (nav, headers, routing readiness)
            ├── 📄 map.page.ts                    — Map surface (MapLibre/Cesium wrappers, layer toggles)
            ├── 📄 timeline.page.ts               — Timeline surface (brush, range filters, ordering)
            ├── 📄 storynode.page.ts              — Story Node v3 view (provenance chips, relations)
            ├── 📄 focusmode.page.ts              — Focus Mode v3 panels (Context/Timeline/Map)
            ├── 📄 governance.page.ts             — Governance overlays (CARE tier, sovereignty flags)
            ├── 📄 dataset_workflow.page.ts       — Synthetic dataset flows (ingest/validate/publish)
            └── 📄 selectors.ts                   — Central selector registry (approved patterns)
~~~

---

## 🧭 Context

### Selector stability policy (normative)
Selectors MUST be resilient to layout and style changes.

Preferred selector order:
1. **Role + accessible name** (WCAG-aligned)
2. **Label text** (for inputs)
3. **Semantic landmarks** (banner, navigation, main, complementary)
4. **data-testid** only when:
   - there is no stable accessible label
   - the UI element is otherwise ambiguous
   - the test requires a precise target (e.g., canvas overlays)

Selectors MUST NOT rely on:
- CSS classes
- DOM depth chains
- pixel coordinates
- rendered map tile contents (unless using dedicated map-test hooks)

### Readiness and wait policy (normative)
Page Objects MUST:
- provide a readiness method (e.g., `waitForReady()`)
- wait on deterministic signals:
  - route settled
  - key UI element visible
  - network idle (if supported and safe)
  - explicit “ready” marker element (preferred for complex pages)

Page Objects MUST NOT:
- use hard sleeps as a primary strategy
- hide timing problems by adding retries inside page methods

### Governance safety policy
Page Objects MUST:
- avoid scraping raw payloads that could contain sensitive fields
- expose helpers for “restricted content state” detection that are UI-based
- never log coordinate-like strings even in debug output

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Test suite"] --> B["Page Object action"]
  B --> C["Stable locator (role-first)"]
  C --> D["Deterministic readiness wait"]
  D --> E["Assertion (governance/a11y/telemetry)"]
  E --> F["Artifacts on failure"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Node v3 page object responsibilities
The Story Node page object SHOULD expose:
- `openById(nodeId)`
- `getTitle()`
- `getNarrativeBody()`
- `getProvenanceChips()`
- `openEvidenceLink(index)`
- `getSpacetimeSummary()` (no raw geometry dumps)

Governance-safe helpers:
- `isMaskedGeometryDisplayed()` (boolean; no coordinates returned)
- `hasRestrictedStateBanner()` (boolean)
- `getCareTierLabel()` (returns tier label text only)

### Focus Mode v3 page object responsibilities
The Focus Mode page object SHOULD expose:
- `openForEntity(entityId)`
- `selectPanel("Context" | "Timeline" | "Map")`
- `getPanelText(panel)`
- `hasSovereigntyFlag()`
- `hasCareTierChip()`

Focus Mode MUST NOT provide methods that:
- extract raw internal graph payloads from debug views (unless explicitly allowed in test mode)
- return coordinate arrays or GeoJSON strings for restricted content

---

## 🧪 Validation & CI/CD

### Page Objects and CI reliability
To keep CI stable:
- Page Objects should be the only place that “knows” selector details.
- Tests should call intent-level actions and assert outcomes.
- When a selector changes, only the page object should need edits.

### Regression rules
If a page object must change because the UI changed:
- update `selectors.ts` first
- update page methods second
- update tests last (only if workflow semantics changed)

This keeps test churn low and increases signal.

---

## 📦 Data & Metadata

### Synthetic-only interaction
Page Objects in E2E must interact with:
- synthetic Story Node IDs
- synthetic dataset workflow items
- synthetic governance states (simulated via fixtures)

No production data. No restricted coordinate sources.

### Logging guidance
Page objects SHOULD:
- log only high-level action steps (optional)
- avoid dumping HTML or JSON payloads into logs

When logging is enabled:
- keep output short
- redact any accidental coordinate-like sequences
- never print tokens, headers, or secrets

---

## 🌐 STAC, DCAT & PROV Alignment

Page Objects may help validate that documentation and provenance surfaces exist, but they must not invent metadata.

Recommended validations supported by page objects:
- presence of provenance chips/IDs
- presence of links to experiment/model card references (when shown)
- UI indication of catalog alignment (labels, badges, link presence)

Not supported:
- parsing STAC/DCAT JSON from UI unless explicitly exposed as a sanitized test fixture view

---

## 🧱 Architecture

### Page Object design conventions (recommended)
- One file per page/surface
- No cross-import cycles
- Central selector registry (`selectors.ts`)
- Prefer small, composable helpers:
  - `open()`
  - `waitForReady()`
  - `actionX()`
  - `getY()`

### Locator conventions (recommended)
- `getByRole` with `name` when possible
- Use `data-testid` for:
  - canvas/map layers
  - timeline brush handles
  - complex composite widgets

Example pattern (illustrative):
~~~ts
// locator (role-first)
const openGovPanelButton = page.getByRole("button", { name: "Governance" });

// readiness
await expect(page.getByRole("main")).toBeVisible();
await expect(page.getByRole("heading", { name: /Focus Mode/i })).toBeVisible();
~~~

---

## ⚖ FAIR+CARE & Governance

### Minimum governance checks supported by Page Objects
Page Objects should expose booleans for:
- restricted state present
- masking applied (as UI state)
- sovereignty badge visible
- CARE tier visible and non-empty

Page Objects must not:
- expose restricted details to tests “for convenience”
- leak coordinate precision by returning raw geometry strings

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial E2E Page Objects guide aligned to KFM-MDP v11.2.6 (role-first selectors, deterministic readiness, governance-safe patterns). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

