---
title: "🧬 KFM E2E — Provenance Mappings Fixtures (Focus Mode) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/mappings/README.md"

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
intent: "tests-e2e-provenance-mappings-fixtures-focus-mode"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-provenance-mappings-fixtures-focus-mode"
doc_uuid: "urn:kfm:tests:e2e:fixtures:provenance:mappings:focus-mode:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/provenance/mappings/README.md"
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
sunset_policy: "Superseded upon next v12 E2E provenance mapping framework update"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/mappings/README.md@v11.2.6"
---

<div align="center">

# 🧬 **Provenance Mappings Fixtures — Focus Mode (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/provenance/mappings/README.md`

**Purpose**  
Define the **canonical synthetic provenance mappings** used by Focus Mode regression E2E tests to validate:  
statement → evidence linkage, panel → dataset lineage wiring, and stable rendering of provenance chips without leaking sensitive precision.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Provenance%20Mappings-blueviolet" />
<img src="https://img.shields.io/badge/Focus%20Mode-Regression-informational" />
<img src="https://img.shields.io/badge/Deterministic-Synthetic-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[🛡 Governance Overlays](../governance/README.md) ·
[🧪 Focus Mode Specs](../../specs/README.md)

</div>

---

## 📘 Overview

### What a “provenance mapping” means in E2E fixtures
A provenance mapping fixture defines how Focus Mode UI elements relate to evidence:

- **statement_id** (or UI claim key) → evidence set
- **panel** (Context / Timeline / Map) → evidence groups
- **evidence** → datasets, documents, experiments, model cards (synthetic references)

These mappings enable deterministic assertions like:
- “Every visible statement has at least one evidence reference.”
- “Provenance chips show stable IDs and do not appear empty.”
- “Restricted states do not show raw coordinates, raw geometry dumps, or leaked precision.”

### What this folder does not do
This folder does **not** store:
- the full narrative text (that belongs in scenario fixtures),
- governance states (that belongs in `provenance/governance/`),
- API mock wiring (that belongs in `fixtures/api_mocks/`).

It stores **the glue** between UI claims and synthetic evidence.

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
                        └── 📁 mappings/                                  — ← This folder (claim→evidence glue)
                            ├── 📄 README.md                              — This guide
                            ├── 🧾 fm_prov_map_001.json                    — Baseline mapping (Context/Timeline/Map)
                            ├── 🧾 fm_prov_map_002.json                    — Missing-evidence edge case (UI fallback)
                            ├── 🧾 fm_prov_map_003.json                    — Multi-evidence mapping (chips + grouping)
                            └── 🧾 fm_prov_map_004.json                    — Restricted mapping (redacted evidence surfaces)
~~~

**Naming policy**
- File stem MUST match `mapping_id` inside the JSON.
- Avoid renames; add new versions as new files to preserve regression stability.

---

## 🧭 Context

### Determinism rules
Mappings MUST:
- use fixed IDs (no runtime UUID generation),
- use stable ordering for arrays where UI order matters,
- be small enough to be human-reviewed in PRs.

### Sovereignty-safe rules
Mappings MUST:
- never reference real or plausible sensitive locations,
- never include raw coordinates,
- allow tests to assert that restricted evidence is:
  - withheld, or
  - generalized, or
  - represented as a safe placeholder.

### Why mappings are separated from evidence catalogs
Separating claim→evidence glue from evidence catalog fixtures helps:
- keep API mock payloads small and composable,
- reuse evidence catalogs across multiple scenarios,
- isolate regressions to either mapping logic or evidence rendering.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Focus Mode UI statement (statement_id)"] --> B["Provenance mapping fixture"]
  B --> C["Evidence IDs (datasets/docs/experiments/model-cards)"]
  C --> D["UI provenance chips + details panel"]
~~~

**Interpretation**  
Mappings tie UI claims to evidence records; tests assert the UI remains grounded and safe.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode panels covered by mappings
Mappings SHOULD support coverage for:
- **Context panel**: summary claims and entity grounding
- **Timeline panel**: event claims, date ranges, ordering
- **Map panel**: layer attributions, masked geometry references, safe spatial grounding

### Minimum expectations for “grounded UI”
For governed narrative surfaces, E2E SHOULD assert:
- every rendered “claim” (statement) has evidence,
- evidence identifiers are present and stable,
- the UI never renders:
  - empty provenance chips,
  - “unknown source” without fallback messaging,
  - raw geometry coordinates or JSON dumps.

---

## 🧪 Validation & CI/CD

### Required validation checks
- JSON parse and schema lint (repo policy)
- secret scan and PII scan
- “no raw coordinates” scanning (repo policy)

### Mapping integrity checks (recommended)
- each `statement_id` referenced in mappings exists in the scenario UI expectations,
- each `evidence_id` referenced exists in the evidence catalogs (or is explicitly “placeholder”).

If a mapping fails validation:
- treat as regression-blocking for the scenario(s) that depend on it.

---

## 📦 Data & Metadata

### Minimum mapping shape (canonical)
Mappings SHOULD follow a stable structure like:

~~~json
{
  "mapping_id": "fm_prov_map_001",
  "scenario_id": "fm_synth_001",
  "panels": {
    "context": [
      {
        "statement_id": "ctx_001",
        "evidence": ["ev_ds_001", "ev_doc_001"]
      }
    ],
    "timeline": [
      {
        "statement_id": "tl_001",
        "evidence": ["ev_event_001", "ev_ds_002"]
      }
    ],
    "map": [
      {
        "statement_id": "map_001",
        "evidence": ["ev_layer_001"],
        "spatial_precision": {
          "masked": true,
          "method": "H3",
          "resolution": "R8"
        }
      }
    ]
  },
  "ui_hints": {
    "chip_grouping": "by_statement",
    "max_chips_inline": 3
  }
}
~~~

### Restricted mapping conventions
If a statement is restricted:
- mark it as restricted using safe flags and placeholders,
- do not embed hidden content.

~~~json
{
  "statement_id": "map_003",
  "evidence": ["ev_restricted_placeholder_001"],
  "restricted_output": {
    "active": true,
    "reason_code": "sovereignty_restriction",
    "ui_mode": "redacted"
  }
}
~~~

### Stability rules
- Arrays SHOULD be in expected UI display order.
- `panels.*[].statement_id` MUST be unique within a panel.
- Any spatial reference MUST include a `spatial_precision` block when masked.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV (testing semantics)
- Mappings are `prov:Entity` test inputs.
- The E2E run is a `prov:Activity`.
- The UI rendering is validated output, recorded as test artifacts.

### DCAT (optional)
If exporting test fixtures as a catalog:
- provenance mapping JSON files are `dcat:Distribution` items (`application/json`) under a test dataset.

### STAC (optional)
If wrapping test runs as non-spatial STAC items:
- mappings can be attached as STAC assets (non-spatial).

---

## ⚖ FAIR+CARE & Governance

### Policy requirements (fixtures)
Mappings MUST:
- enable governance-safe assertions (no leakage),
- support CARE tier display tests when paired with governance overlays,
- remain synthetic, non-identifying, and bias-neutral.

### Escalation
If a mapping is used to test restricted behavior and the UI exposes precision:
- treat as merge-blocking,
- route to FAIR+CARE Council + Focus Mode working group,
- record per audit policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial provenance mappings fixture guide aligned to KFM-MDP v11.2.6; enforced emoji directory layout; defined canonical mapping shapes for panel-based statement grounding. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

