---
title: "🧾 KFM E2E — Provenance Fixtures (Focus Mode Regression) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/README.md"

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
intent: "tests-e2e-provenance-fixtures"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-provenance-fixtures-focus-mode"
doc_uuid: "urn:kfm:tests:e2e:fixtures:provenance:focus-mode:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/provenance/README.md"
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
sunset_policy: "Superseded upon next v12 E2E provenance fixture framework update"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Provenance Fixtures — Focus Mode Regression (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/provenance/README.md`

**Purpose**  
Define the **canonical synthetic provenance fixture suite** used by Focus Mode regression E2E tests.  
These fixtures enable deterministic UI validation for **provenance chips**, **lineage panels**, and **governance overlays** without touching real, sensitive, or production data.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Provenance%20Fixtures-blueviolet" />
<img src="https://img.shields.io/badge/Focus%20Mode-Regression-informational" />
<img src="https://img.shields.io/badge/Sovereignty-Safe-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Focus Mode Fixtures](../README.md) ·
[🧪 Focus Mode Specs](../../../../specs/README.md) ·
[🧭 E2E Guide](../../../../../README.md) ·
[🧱 Test Architecture](../../../../../../ARCHITECTURE.md)

</div>

---

## 📘 Overview

### What these fixtures are
Provenance fixtures are **synthetic JSON artifacts** that simulate:

- **PROV-O** fragments (Activity / Entity / Agent + basic relations)
- **OpenLineage v2.5**-style events (job/run + inputs/outputs)
- **KFM governance facets** used by Focus Mode UI (CARE tier, sovereignty flags, masking indicators)
- **Stable IDs** suitable for UI linking (URNs, semantic IDs, placeholder hashes)

These fixtures exist so regression tests can assert:

- a provenance chip appears for a given claim/panel,
- the “evidence/lineage” view renders expected IDs and references,
- governance indicators are present and consistent,
- restricted/masked states do not leak precision.

### What these fixtures are not
These fixtures are **not**:
- production provenance records,
- authoritative scientific statements,
- a substitute for schema or contract validation in pipeline-level tests.

They are **UI-facing test inputs** designed for determinism and policy safety.

---

## 🗂️ Directory Layout

~~~text
📁 fixtures/
└── 📁 provenance/
    ├── 📄 README.md                          — This guide (policy + shapes)
    │
    ├── 🧾 provenance_manifest.json           — Required: inventory + intent + checksums
    ├── 🧾 checksums.sha256                   — Optional: detached checksums
    │
    ├── 🧾 prov_o/
    │   ├── 🧾 fm_prov_activity_001.jsonld    — PROV-O JSON-LD fragment (synthetic)
    │   ├── 🧾 fm_prov_activity_002.jsonld
    │   └── 🧾 fm_prov_activity_003.jsonld
    │
    ├── 🧾 openlineage/
    │   ├── 🧾 fm_ol_event_001.json           — OpenLineage-like event (synthetic)
    │   ├── 🧾 fm_ol_event_002.json
    │   └── 🧾 fm_ol_event_003.json
    │
    ├── 🧾 mappings/
    │   ├── 🧾 fm_claim_to_prov_map_001.json  — Claim/panel → provenance IDs
    │   └── 🧾 fm_claim_to_ol_map_001.json
    │
    └── 🧾 governance/
        ├── 🧾 fm_governance_overlay_001.json — CARE + sovereignty + masking states
        └── 🧾 fm_governance_overlay_002.json
~~~

**Directory policy**
- If any fixture exists under `prov_o/` or `openlineage/`, then `provenance_manifest.json` MUST exist.
- Keep fixture sets minimal and scenario-driven (high-signal, no filler).
- All files MUST be synthetic and non-identifying.

---

## 🧭 Context

### Determinism rules
Fixtures MUST:
- use stable identifiers (deterministic URNs, stable semantic IDs),
- avoid timestamps that change per run (use fixed `eventTime` unless explicitly testing time rendering),
- avoid random UUID generation inside fixture content unless it is version-pinned and recorded.

### Safety rules (sovereignty + ethics)
Fixtures MUST:
- contain no real coordinates, no plausible sacred site geometry, and no identifying text,
- never include raw precision “debug geometry” payloads intended for internal tooling,
- simulate restricted content states only via **flags** and **masked placeholders**.

### Compatibility rules (UI resilience)
Fixtures SHOULD:
- include both “happy path” and “restricted/redacted” states,
- include at least one case with “missing evidence” (to validate safe UI handling),
- include stable, human-readable labels for test diagnosis.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Scenario fixture (expected UI)"] --> B["API mocks return provenance payloads"]
  B --> C["Focus Mode UI renders panels"]
  C --> D["Assertions verify chips, links, and governance overlays"]
  D --> E["Artifacts + telemetry recorded"]
~~~

**Interpretation**  
Provenance fixtures sit on the API boundary (often via mocks) and enable deterministic validation of provenance surfaces and policy indicators.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode provenance surfaces (what regression tests validate)
Regression E2E tests that use these fixtures SHOULD validate:

- **Context panel**
  - provenance chip exists when claims are present,
  - evidence list renders stable IDs (dataset IDs, experiment IDs, model card IDs where applicable).

- **Timeline panel**
  - events display with traceable references,
  - ordering does not contradict declared provenance timestamps (when tested).

- **Map panel**
  - provenance for layers is visible,
  - any masked state is clearly indicated,
  - no raw coordinate precision is shown in tooltips or downloads.

### Claim mapping (required concept)
The UI must be able to map:
- a displayed claim (or panel section)
- to one or more provenance references.

Fixtures encode this mapping under `mappings/` so tests can assert:
- “Claim X shows provenance ID Y”
- “Panel Z contains at least one evidence reference”

---

## 🧪 Validation & CI/CD

### Required checks (fixture-level)
Fixtures MUST pass:
- secret scan (no tokens/keys),
- PII scan (no identifying persons),
- “no raw coordinates” scan (project policy),
- JSON parse validation.

### Recommended checks (project-level)
Fixtures SHOULD also pass:
- schema-lint for known fixture shapes (if schemas exist),
- checksum verification against `provenance_manifest.json`,
- governance overlay validation (expected keys present).

### CI behavior (recommended)
- Provenance fixture checks run with `@regression` and `@governance` suites.
- Any governance failure is treated as **merge-blocking**.

---

## 📦 Data & Metadata

### provenance_manifest.json (required)
The manifest is the source-of-truth inventory for this folder.

Shape (recommended):
~~~json
{
  "fixture_set_id": "fm_provenance_fixtures_v11_2_6",
  "scope": {
    "suite": "tests/e2e/web-app/regression/focus-mode",
    "synthetic_only": true
  },
  "version": "v11.2.6",
  "created": "2025-12-13T00:00:00Z",
  "files": [
    {
      "path": "prov_o/fm_prov_activity_001.jsonld",
      "intent": "Baseline PROV-O activity for Context panel claims",
      "sha256": "<sha256>"
    },
    {
      "path": "openlineage/fm_ol_event_001.json",
      "intent": "Baseline OpenLineage event for evidence chip rendering",
      "sha256": "<sha256>"
    },
    {
      "path": "mappings/fm_claim_to_prov_map_001.json",
      "intent": "Claim-to-provenance mapping for deterministic assertions",
      "sha256": "<sha256>"
    },
    {
      "path": "governance/fm_governance_overlay_001.json",
      "intent": "CARE + sovereignty overlay state (masked)",
      "sha256": "<sha256>"
    }
  ]
}
~~~

### PROV-O fixture fragment (recommended minimum)
Keep this small and UI-oriented:
- at least one `prov:Activity`
- at least one `prov:Entity`
- a `prov:used` edge
- a `prov:wasGeneratedBy` edge
- optional `prov:Agent` (CI job / test runner)

Example (simplified shape):
~~~json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "prov:activity": {
    "urn:kfm:prov:activity:fm_synth_003:001": {
      "prov:label": "Synthetic Focus Mode activity",
      "prov:type": "kfm:TestActivity"
    }
  },
  "prov:entity": {
    "urn:kfm:prov:entity:dataset:synthetic:001": {
      "prov:label": "Synthetic dataset reference",
      "prov:type": "kfm:TestEntity"
    }
  },
  "prov:used": [
    {
      "prov:activity": "urn:kfm:prov:activity:fm_synth_003:001",
      "prov:entity": "urn:kfm:prov:entity:dataset:synthetic:001"
    }
  ]
}
~~~

### OpenLineage-like event fixture (recommended minimum)
Keep event fields stable for UI rendering tests:
~~~json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-12-13T00:00:00Z",
  "run": { "runId": "urn:kfm:ol:run:fm_synth_003:001" },
  "job": { "namespace": "kfm-tests", "name": "focus-mode-e2e" },
  "inputs": [
    { "namespace": "kfm-synthetic", "name": "dataset/synth/001" }
  ],
  "outputs": [
    { "namespace": "kfm-synthetic", "name": "artifact/evidence/001" }
  ]
}
~~~

### Governance overlay fixture (recommended minimum)
This is what the UI uses to show safe/unsafe states without real content:
~~~json
{
  "care_tier": "Tier B",
  "sovereignty_flags": ["masked"],
  "masking": { "method": "H3", "resolution": "R8" },
  "restricted_output": false,
  "notes": "Synthetic governance overlay for regression assertions"
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV alignment
- Treat each PROV fixture file as a **PROV fragment** used for UI behavior validation.
- IDs SHOULD be URNs and MUST be synthetic.

### DCAT alignment (optional for audit tooling)
If the repo catalogs test artifacts:
- the fixture set can be represented as a `dcat:Dataset` (documentation/testing),
- each fixture file is a `dcat:Distribution` (JSON/JSON-LD media types).

### STAC alignment (optional)
If E2E artifacts are wrapped as STAC Items:
- use `geometry: null` for non-spatial provenance artifacts,
- store artifacts as STAC assets (reports + provenance JSON).

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable governance rules
These fixtures MUST ensure:
- no sensitive precision leakage,
- no culturally harmful narrative text (even synthetic),
- no secrets or PII,
- restricted states are simulated via flags and redaction placeholders only.

### Escalation policy (tests)
If a regression test indicates provenance UI can leak restricted information:
- treat as merge-blocking,
- route to FAIR+CARE Council + the Narrative Governance Team,
- record the failure per project audit policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial provenance fixture guide for Focus Mode regression E2E tests (synthetic, deterministic, sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

