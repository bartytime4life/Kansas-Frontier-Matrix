---
title: "🧾 KFM E2E — PROV-O Provenance Fixtures (Focus Mode) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/prov_o/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-provenance-provo-fixtures-focus-mode"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-provenance-provo-fixtures-focus-mode"
doc_uuid: "urn:kfm:tests:e2e:fixtures:provenance:prov-o:focus-mode:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/provenance/prov_o/README.md"
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

signature_ref: "../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E provenance framework update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/prov_o/README.md@v11.2.6"
---

<div align="center">

# 🧾 **PROV-O Fixtures — Focus Mode Provenance (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/provenance/prov_o/README.md`

**Purpose**  
Define the **canonical synthetic PROV‑O fixtures** used by Focus Mode regression E2E tests to validate:  
evidence chaining (Entity/Activity/Agent), UI provenance chips, governance-safe redaction behavior, and deterministic mapping to OpenLineage and STAC/DCAT references.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/PROV--O-W3C-blue" />
<img src="https://img.shields.io/badge/Focus%20Mode-Regression-informational" />
<img src="https://img.shields.io/badge/Fixtures-Synthetic%20Only-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[🧬 OpenLineage Fixtures](../openlineage/README.md) ·
[🧭 Provenance Mappings](../mappings/README.md) ·
[🛡 Governance Overlays](../governance/README.md)

</div>

---

## 📘 Overview

### What these fixtures are
These fixtures are **synthetic PROV‑O JSON‑LD fragments** (and optional RDF/Turtle equivalents, if used by the repo) that represent:

- `prov:Entity` — datasets, artifacts, rendered panels, redacted views
- `prov:Activity` — pipeline runs, render steps, validation steps
- `prov:Agent` — CI, test runner, governance bodies (synthetic identifiers)
- core links such as:
  - `prov:used`
  - `prov:wasGeneratedBy`
  - `prov:wasAssociatedWith`
  - `prov:wasDerivedFrom`

They exist to make provenance **testable** as a user-visible contract in Focus Mode.

### What these fixtures are not
They are not real provenance from production or restricted data. Fixtures MUST NOT include:
- real people, real organizations outside synthetic placeholders
- real restricted site geometries or plausible sensitive coordinates
- production hostnames, tokens, or secrets
- external URLs that CI would need to resolve

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 fixtures/
                    └── 📁 provenance/
                        └── 📁 prov_o/                                    — ← This folder (synthetic PROV-O)
                            ├── 📄 README.md                               — This guide
                            ├── 🧾 prov_001_entity_dataset.jsonld          — Dataset entity (STAC/DCAT refs)
                            ├── 🧾 prov_002_activity_render.jsonld         — Focus Mode render activity
                            ├── 🧾 prov_003_agent_ci_runner.jsonld         — CI/test-runner agent
                            ├── 🧾 prov_004_chain_storynode_to_panel.jsonld— End-to-end evidence chain
                            ├── 🧾 prov_005_governance_redacted.jsonld     — Restricted/redacted provenance view
                            └── 🧾 prov_006_invalid_negative.jsonld        — Negative fixture (schema rejection)
~~~

**Naming policy**
- Use `prov_###_<purpose>.jsonld` for stable ordering and deterministic selection.
- Negative fixtures MUST include `invalid` or `negative` in the filename and must be restricted to schema/parser tests (not UI happy paths).

---

## 🧭 Context

### Determinism requirements
PROV‑O fixtures MUST:
- be stable across platforms (no environment-specific absolute paths)
- use pinned timestamps when included (ISO 8601, fixed values)
- avoid random identifiers unless seeded and recorded in the scenario manifest

### Why PROV‑O is required in E2E
OpenLineage captures run/job/dataset edges for pipelines. PROV‑O captures the **semantic provenance narrative** that Focus Mode can surface as:
- provenance chips
- evidence panels
- “what produced this?” chains

E2E tests ensure the UI never regresses into:
- missing provenance references,
- broken chain ordering,
- or unsafe details leaking through “debug” views.

### Governance constraints
PROV‑O fixtures are governance-sensitive because provenance can accidentally reveal:
- restricted dataset identifiers,
- location precision via geometry artifacts,
- or “hidden” relationships.

All governance-sensitive fields must be represented at **safe abstraction** (redacted/masked) when the scenario requires it.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E scenario loads Focus Mode"] --> B["API mock returns PROV-O JSON-LD"]
  B --> C["UI builds evidence chain"]
  C --> D["Render provenance chips and lineage panel"]
  D --> E["Assertions validate: chain complete and safe"]
~~~

**Interpretation**  
The PROV‑O fixture is the synthetic truth source for proving that Focus Mode renders provenance consistently and safely.

---

## 🧠 Story Node & Focus Mode Integration

### What Focus Mode should do with PROV‑O fixtures
E2E suites SHOULD validate that Focus Mode:
- identifies and displays the “primary” `prov:Entity` for the active panel
- traces `prov:wasGeneratedBy` to the producing `prov:Activity`
- shows `prov:used` datasets as evidence links (synthetic STAC/DCAT identifiers)
- displays `prov:wasAssociatedWith` agents (CI, pipeline runner) using safe labels
- honors governance mode:
  - if redacted, restrict the fields shown and suppress unsafe detail

### Minimum provenance UI assertions (recommended)
- At least one provenance chip is visible for governed narrative surfaces.
- Clicking a provenance chip opens a details view that:
  - contains stable IDs,
  - contains no restricted precision,
  - and does not require network access.
- Evidence chain ordering is deterministic (same input → same displayed order).

---

## 🧪 Validation & CI/CD

### Required validations
Fixtures MUST pass:
- JSON-LD parse checks (and Turtle parse checks if applicable)
- schema linting (repo provenance fixture schema, if present)
- secret scan + PII scan
- governance-safe checks (no sensitive coordinates, no prohibited strings)

### Negative fixtures policy
Negative fixtures MUST:
- be isolated to schema/parser tests,
- never be loaded by `@smoke`,
- and never be used as the default provenance input for regression scenarios.

---

## 📦 Data & Metadata

### Canonical PROV‑O JSON‑LD conventions (fixture baseline)
A baseline fixture SHOULD:
- declare `@context` (repo-approved JSON-LD context)
- include stable identifiers for Entities/Activities/Agents
- include only the fields required to test UI behavior

Example (simplified):

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "urn:kfm:"
  },
  "prov:Entity": {
    "kfm:entity:focus_panel_context_001": {
      "prov:label": "Focus Mode Context Panel (synthetic)",
      "prov:type": "kfm:FocusPanel"
    }
  },
  "prov:Activity": {
    "kfm:activity:focusmode_render_001": {
      "prov:label": "Focus Mode render (synthetic)",
      "prov:type": "kfm:TestRun"
    }
  },
  "prov:Agent": {
    "kfm:agent:ci_runner": {
      "prov:label": "CI Runner (synthetic)",
      "prov:type": "kfm:AutomationAgent"
    }
  },
  "prov:wasGeneratedBy": {
    "kfm:gen:1": {
      "prov:entity": "kfm:entity:focus_panel_context_001",
      "prov:activity": "kfm:activity:focusmode_render_001"
    }
  },
  "prov:wasAssociatedWith": {
    "kfm:assoc:1": {
      "prov:activity": "kfm:activity:focusmode_render_001",
      "prov:agent": "kfm:agent:ci_runner"
    }
  }
}
~~~

### Governance-redacted fixture conventions
When a scenario requires redaction, fixtures SHOULD represent it explicitly:

~~~json
{
  "kfm:governance": {
    "care_tier": "Tier A",
    "sovereignty": {
      "restricted": true,
      "ui_mode": "redacted"
    }
  }
}
~~~

The UI must treat redaction as binding and suppress unsafe details.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O semantics (testing)
- Each fixture represents a provenance graph fragment:
  - Entities, Activities, and Agents linked by PROV relations.
- The UI should surface a **human-friendly** view of these links without leaking restricted detail.

### DCAT semantics (optional)
If fixtures are cataloged:
- each PROV‑O JSON‑LD fixture is a `dcat:Distribution` (`mediaType: application/ld+json`).

### STAC semantics (optional)
If fixtures are represented as STAC assets:
- they may attach as an asset to a non-spatial STAC Item representing a test run:
  - `geometry: null`
  - `assets.prov.href` points to the JSON‑LD artifact

---

## ⚖ FAIR+CARE & Governance

### Fixture governance requirements
PROV‑O fixtures MUST:
- be synthetic and non-identifying
- avoid any location precision that could be interpreted as a real site
- support testing that sovereignty masking/redaction is honored in UI
- avoid colonial or harmful framing even in synthetic text

### Escalation policy
If an E2E test detects:
- provenance surfaces show restricted precision,
- or redaction signals are ignored,
treat as merge-blocking and route to governance review per repo policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode PROV‑O fixture guide aligned to KFM‑MDP v11.2.6; defined naming conventions, determinism rules, and governance‑redaction patterns. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

