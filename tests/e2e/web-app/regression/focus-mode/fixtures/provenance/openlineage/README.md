---
title: "🧬 KFM E2E — OpenLineage Provenance Fixtures (Focus Mode) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/openlineage/README.md"

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
intent: "tests-e2e-provenance-openlineage-fixtures-focus-mode"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-provenance-openlineage-fixtures-focus-mode"
doc_uuid: "urn:kfm:tests:e2e:fixtures:provenance:openlineage:focus-mode:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/provenance/openlineage/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/openlineage/README.md@v11.2.6"
---

<div align="center">

# 🧬 **OpenLineage Fixtures — Focus Mode Provenance (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/provenance/openlineage/README.md`

**Purpose**  
Define the **canonical synthetic OpenLineage event fixtures** used by Focus Mode regression E2E tests to validate:  
run/job identity surfaces, input/output dataset facets, governance facets (CARE/sovereignty), and deterministic rendering of lineage references in UI.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-blue" />
<img src="https://img.shields.io/badge/Focus%20Mode-Regression-informational" />
<img src="https://img.shields.io/badge/Fixtures-Synthetic%20Only-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[🧬 Provenance Mappings](../mappings/README.md) ·
[🛡 Governance Overlays](../governance/README.md)

</div>

---

## 📘 Overview

### What these fixtures are
These fixtures are **synthetic OpenLineage v2.5 events** (JSON) that represent:
- a pipeline run (`run`)
- its stable identity (`job`)
- its inputs/outputs (datasets)
- and KFM governance facets (CARE/sovereignty + redaction modes)

They are used to validate that Focus Mode:
- surfaces lineage IDs predictably,
- groups inputs/outputs correctly,
- and never exposes restricted precision.

### What these fixtures are not
They are **not** real lineage events from production.
They must not include:
- real tokens,
- real hosts,
- real run IDs that match production,
- any sensitive dataset identifiers beyond synthetic placeholders.

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
                        └── 📁 openlineage/                                — ← This folder (synthetic OL events)
                            ├── 📄 README.md                               — This guide
                            ├── 🧾 ol_event_001_focusmode_generate.json     — Baseline run (datasets + outputs)
                            ├── 🧾 ol_event_002_governance_masked.json      — Sovereignty-masked run facet
                            ├── 🧾 ol_event_003_multi_input_output.json     — Multiple inputs/outputs grouping
                            ├── 🧾 ol_event_004_missing_optional_facets.json— UI fallback behavior
                            └── 🧾 ol_event_005_invalid_shape_negative.json — Negative test (schema rejection)
~~~

**Naming policy**
- Use `ol_event_###_<purpose>.json` for stable ordering.
- Negative fixtures MUST include `negative` in the filename and be gated to schema tests (not UI happy paths).

---

## 🧭 Context

### Determinism rules
OpenLineage fixtures MUST:
- use stable `job.namespace`, `job.name`, `run.runId` patterns (synthetic),
- avoid time-dependent fields unless pinned (e.g., fixed ISO timestamps),
- avoid environment-specific absolute paths (use repo-relative placeholders).

### Governance rules (non-negotiable)
OpenLineage fixtures MUST support testing that:
- sovereignty restrictions are represented as **facets**, not hidden fields,
- restricted outputs are redacted/masked at the UI layer,
- no sensitive coordinate precision appears anywhere in the payload.

### Why OpenLineage is tested in Focus Mode
Focus Mode surfaces “why should I trust this?” signals via:
- run identifiers,
- dataset lineage links,
- governance flags,
- and provenance chips that connect claims to evidence.

If OpenLineage parsing or rendering regresses, users lose trust and governance can be violated.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E scenario loads Focus Mode"] --> B["API mock returns OpenLineage event JSON"]
  B --> C["UI parses run/job + datasets + facets"]
  C --> D["Provenance chips + lineage panel render"]
  D --> E["Assertions validate: IDs present, facets respected, no leakage"]
~~~

**Interpretation**  
The OpenLineage fixture is the authoritative synthetic input that drives lineage rendering assertions.

---

## 🧠 Story Node & Focus Mode Integration

### How Focus Mode uses OpenLineage (testable behaviors)
E2E tests SHOULD validate:
- Job/run identity displays correctly (no blank placeholders).
- Input datasets are listed and grouped deterministically.
- Output datasets and artifacts are visible when allowed.
- Governance facets affect UI state:
  - masked / redacted modes are reflected,
  - restricted evidence stays restricted.

### Minimum provenance UI assertions (recommended)
- lineage panel shows `runId` and `job` fields,
- at least one input dataset is present for a run that claims inputs,
- governance badges (CARE tier and sovereignty flags) render when facets present,
- clicking a lineage reference does not navigate to external networks unless explicitly allowed.

---

## 🧪 Validation & CI/CD

### Required validation checks
- JSON schema validation (OpenLineage shape constraints used by repo)
- secret scan + PII scan
- governance facet checks (repo policy)

### Negative fixtures policy
Negative fixtures are allowed only for:
- schema validation tests,
- parser hardening tests.

They MUST NOT be used in:
- `@smoke` UI flows,
- happy-path regression scenarios.

---

## 📦 Data & Metadata

### Canonical OpenLineage event shape (fixture baseline)
A baseline fixture SHOULD provide:
- `eventType`
- `eventTime` (pinned)
- `run.runId`
- `job.namespace` and `job.name`
- `inputs[]` and `outputs[]` with dataset identifiers
- a KFM governance facet (synthetic)

Example (simplified):

~~~json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-12-13T00:00:00Z",
  "run": {
    "runId": "run_synth_focusmode_001",
    "facets": {
      "kfmGovernance": {
        "care_tier": "Tier B",
        "sovereignty": {
          "restricted": false,
          "masking_required": false
        }
      }
    }
  },
  "job": {
    "namespace": "kfm.tests.e2e",
    "name": "focusmode.render"
  },
  "inputs": [
    {
      "namespace": "stac",
      "name": "stac:climate/summary_stats"
    }
  ],
  "outputs": [
    {
      "namespace": "kfm",
      "name": "artifact:focusmode_panel_render_v11"
    }
  ]
}
~~~

### Masked / restricted fixture conventions
When testing restricted scenarios:
- represent restriction in governance facets,
- keep dataset identifiers synthetic,
- include masking metadata in a safe, high-level form:

~~~json
{
  "facets": {
    "kfmGovernance": {
      "care_tier": "Tier A",
      "sovereignty": {
        "restricted": true,
        "masking_required": true,
        "masking_method": "H3",
        "masking_resolution": "R8",
        "ui_mode": "redacted"
      }
    }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV semantics (testing)
- Each OpenLineage event corresponds to a `prov:Activity` in conceptual mapping.
- Datasets referenced in `inputs/outputs` correspond to `prov:Entity` placeholders.

### DCAT semantics (optional)
If exporting fixtures as a catalog:
- each OpenLineage JSON file is a `dcat:Distribution` (`mediaType: application/json`).

### STAC semantics (optional)
If representing test artifacts in STAC:
- OpenLineage JSON may be an asset attached to a non-spatial item representing the test run.

---

## ⚖ FAIR+CARE & Governance

### Fixture governance requirements
OpenLineage fixtures MUST:
- be synthetic and non-identifying,
- never include sensitive coordinates,
- support CARE/sovereignty UI gating tests,
- keep external link fields either absent or explicitly inert.

### Escalation
If tests detect:
- lineage UI renders restricted precision, or
- governance facets are ignored,
treat as merge-blocking and route per governance policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode OpenLineage fixture guide aligned to KFM-MDP v11.2.6; defined deterministic fixture naming and governance facet conventions. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

