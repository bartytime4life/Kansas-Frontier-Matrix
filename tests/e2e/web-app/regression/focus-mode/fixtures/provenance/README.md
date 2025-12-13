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
intent: "tests-e2e-provenance-fixtures-focus-mode"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

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

signature_ref: "../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
These fixtures enable deterministic UI validation for **provenance chips**, **lineage panels**, and **governance overlays** without using real, sensitive, or production data.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Provenance%20Fixtures-blueviolet" />
<img src="https://img.shields.io/badge/Focus%20Mode-Regression-informational" />
<img src="https://img.shields.io/badge/Sovereignty-Safe-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Focus Mode Fixtures](../README.md) ·
[🧪 Focus Mode Specs](../../specs/README.md) ·
[🧭 E2E Guide](../../../../../README.md) ·
[🏗 Test Architecture](../../../../../../ARCHITECTURE.md)

</div>

---

## 📘 Overview

### What these fixtures are
Provenance fixtures are **synthetic artifacts** that simulate:

- **PROV-O** fragments (Activity / Entity / Agent and basic relations)
- **OpenLineage v2.5-like** events (job/run + inputs/outputs)
- **KFM governance facets** consumed by the UI (CARE tier, sovereignty flags, masking indicators)
- **Stable IDs** suitable for UI linking (URNs, semantic IDs, placeholder hashes)

These fixtures exist so E2E regression tests can assert:

- provenance chips render where required,
- evidence/lineage views show expected identifiers and references,
- governance indicators are present and consistent,
- restricted/masked states never leak raw precision.

### What these fixtures are not
These fixtures are **not**:
- production provenance records,
- authoritative scientific statements,
- a substitute for pipeline-level lineage validation.

They are **UI-facing inputs** optimized for determinism and policy safety.

---

## 🗂️ Directory Layout

~~~text
📁 tests/                                                                  — Test platform root (unit / integration / e2e)
└── 📁 e2e/                                                                — End-to-end suites (browser + API + governance)
    └── 📁 web-app/                                                        — UI-focused E2E suites
        └── 📁 regression/                                                 — Broader coverage (non-smoke)
            └── 📁 focus-mode/                                             — Focus Mode v3 regression suites
                └── 📁 fixtures/                                           — Deterministic synthetic inputs (non-sensitive)
                    └── 📁 provenance/                                     — ← This folder (provenance fixture set)
                        ├── 📄 README.md                                   — This guide (rules + expected shapes)
                        ├── 📄 provenance_manifest.json                    — 🧾 Inventory + intent + SHA-256 per fixture
                        ├── 📄 checksums.sha256                            — 🧾 Optional detached checksums (CI fast-path)
                        │
                        ├── 📁 prov_o/                                     — 🧾 PROV-O JSON-LD fragments (synthetic)
                        │   ├── 📄 fm_prov_activity_001.jsonld             — Baseline provenance for Context panel
                        │   ├── 📄 fm_prov_activity_002.jsonld             — Restricted/masked variant (no precision)
                        │   └── 📄 fm_prov_activity_003.jsonld             — Missing-evidence variant (safe UI behavior)
                        │
                        ├── 📁 openlineage/                                — 🧾 OpenLineage-like events (synthetic)
                        │   ├── 📄 fm_ol_event_001.json                     — Baseline job/run + inputs/outputs
                        │   ├── 📄 fm_ol_event_002.json                     — Multi-input / multi-output variant
                        │   └── 📄 fm_ol_event_003.json                     — Redacted variant (restricted state)
                        │
                        ├── 📁 mappings/                                   — 🧾 Claim/panel → provenance ID maps
                        │   ├── 📄 fm_claim_to_prov_map_001.json            — Claim keys → PROV entity/activity URNs
                        │   └── 📄 fm_claim_to_ol_map_001.json              — Claim keys → OpenLineage run/job IDs
                        │
                        └── 📁 governance/                                 — 🧾 CARE + sovereignty overlay states (synthetic)
                            ├── 📄 fm_governance_overlay_001.json           — Tier B (masked geometry)
                            └── 📄 fm_governance_overlay_002.json           — Restricted output state (redacted UI)
~~~

**Directory policy**
- If any file exists under `prov_o/` or `openlineage/`, `provenance_manifest.json` MUST exist.
- Fixtures MUST remain synthetic, deterministic, and non-identifying.
- JSON/JSON-LD fixtures SHOULD be small and UI-oriented (high-signal, minimal noise).

---

## 🧭 Context

### Determinism rules
Fixtures MUST:
- use stable identifiers (deterministic URNs, stable semantic IDs),
- avoid timestamps that change per run (use fixed timestamps unless explicitly testing time rendering),
- avoid runtime-generated UUIDs unless version-pinned and listed in the manifest.

### Sovereignty + ethics rules
Fixtures MUST:
- contain no real coordinates and no plausible “real site” geometry,
- never include raw-precision geometry dumps for restricted contexts,
- simulate restricted states via **flags and redaction placeholders**, not sensitive content.

### UI resilience rules
Fixtures SHOULD include:
- a baseline “happy path” provenance set,
- at least one restricted/redacted case,
- at least one “missing evidence” case to validate safe UI fallback behavior.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Scenario loads (expected UI)"] --> B["API mocks return provenance payloads"]
  B --> C["Focus Mode UI renders panels and chips"]
  C --> D["Assertions verify IDs, links, and governance overlays"]
  D --> E["Artifacts and telemetry recorded"]
~~~

**Interpretation**  
Provenance fixtures sit behind API mocks and enable deterministic validation of provenance surfaces and policy indicators in Focus Mode.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode provenance surfaces (what regression E2E validates)
Regression E2E tests using these fixtures SHOULD validate:

- **Context panel**
  - provenance chip exists when claims are present,
  - evidence list renders stable IDs (dataset IDs, experiment IDs, model card IDs when applicable).

- **Timeline panel**
  - events display traceable references,
  - ordering is stable and consistent (when time rendering is under test).

- **Map panel**
  - provenance for layers is visible and linkable,
  - masked/restricted states are clearly indicated,
  - raw coordinate precision never appears in tooltips, JSON views, or downloads.

### Claim mapping is required for deterministic assertions
The UI must map:
- a displayed claim (or panel section)
- to one or more provenance references.

Fixtures encode this mapping under `mappings/` so tests can assert:
- “Claim X shows provenance reference Y”
- “Panel Z contains at least one evidence reference”

---

## 🧪 Validation & CI/CD

### Required checks
Fixtures MUST pass:
- JSON/JSON-LD parse validation,
- secret scan (no tokens/keys),
- PII scan (no identifying persons),
- “no raw coordinates” scan (project policy),
- manifest consistency checks (all referenced files exist).

### Recommended checks
Fixtures SHOULD pass:
- checksum verification against `provenance_manifest.json`,
- governance overlay key validation (required UI keys present),
- schema-lint (if fixture schemas exist in `tests/e2e/**/schemas/`).

### CI behavior (recommended)
- Provenance fixture checks run with `@regression` and `@governance` suites.
- Governance-related failures are treated as **merge-blocking**.

---

## 📦 Data & Metadata

### provenance_manifest.json is the source of truth
The manifest is the canonical inventory for this folder.

Recommended shape:
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
      "intent": "Baseline OpenLineage-like event for chip rendering",
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

### PROV-O fragment minimum
Keep PROV-O fixtures small and UI-oriented:
- at least one `prov:Activity`,
- at least one `prov:Entity`,
- at least one `prov:used` edge,
- at least one `prov:wasGeneratedBy` edge,
- optional `prov:Agent` (CI runner, synthetic actor).

### Governance overlay minimum
Governance fixtures SHOULD include keys the UI can render deterministically:
- `care_tier`,
- `sovereignty_flags`,
- `masking.method`,
- `masking.resolution`,
- `restricted_output` (boolean).

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV alignment
- Each PROV-O fixture file is a **synthetic PROV fragment** used to test UI behavior.
- Identifiers SHOULD be URNs and MUST be synthetic.

### DCAT alignment (optional)
If the repo catalogs test artifacts:
- the fixture set may be represented as a `dcat:Dataset` (testing documentation),
- each fixture file may be treated as a `dcat:Distribution` (`application/json`, `application/ld+json`).

### STAC alignment (optional)
If E2E artifacts are wrapped as STAC Items:
- use `geometry: null` for non-spatial provenance artifacts,
- store fixtures as STAC assets only when publishing test artifacts externally.

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable governance rules
Fixtures MUST ensure:
- no sensitive precision leakage,
- no culturally harmful narrative text (even synthetic),
- no secrets or PII,
- restricted states are represented via redaction and flags only.

### Escalation policy
If regression tests indicate provenance UI can leak restricted information:
- treat as merge-blocking,
- route to FAIR+CARE Council + Narrative Governance Team,
- record the failure per audit policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Realigned directory layout to KFM-MDP v11.2.6 emoji tree rules; clarified fixture set structure (PROV-O, OpenLineage-like, mappings, governance overlays); corrected relative references. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
