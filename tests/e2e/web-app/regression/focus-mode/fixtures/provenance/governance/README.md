---
title: "🛡️ KFM E2E — Governance Overlay Fixtures (Focus Mode Provenance) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/governance/README.md"

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
intent: "tests-e2e-governance-overlay-fixtures-focus-mode"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-governance-overlay-fixtures-focus-mode"
doc_uuid: "urn:kfm:tests:e2e:fixtures:provenance:governance:focus-mode:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/provenance/governance/README.md"
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
sunset_policy: "Superseded upon next v12 E2E governance fixture framework update"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/provenance/governance/README.md@v11.2.6"
---

<div align="center">

# 🛡️ **Governance Overlay Fixtures — Focus Mode Provenance (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/provenance/governance/README.md`

**Purpose**  
Define the **canonical synthetic governance overlay fixtures** used by Focus Mode regression E2E tests to validate:  
CARE tier display, sovereignty flags, masking indicators, restricted-output UI behavior, and safe redaction paths.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Governance%20Fixtures-blueviolet" />
<img src="https://img.shields.io/badge/Focus%20Mode-Regression-informational" />
<img src="https://img.shields.io/badge/Sovereignty-Safe-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Provenance Fixtures](../README.md) ·
[🧪 Focus Mode Specs](../../specs/README.md) ·
[🧭 E2E Guide](../../../../../README.md) ·
[🏗 Test Architecture](../../../../../../ARCHITECTURE.md)

</div>

---

## 📘 Overview

### What this folder contains
This folder contains **synthetic governance overlay fixtures** that emulate what the UI would receive from the API / policy engine for a given Focus Mode session.

These overlays enable deterministic E2E assertions for:

- CARE tier labels and routing (Tier A/B/C or equivalent KFM policy tiers)
- Sovereignty flags and restricted-output indicators
- Masking method and resolution presentation (H3 generalization indicators)
- “Redacted / withheld / blocked” UI behavior (safe responses, no leakage)

### What this folder must never contain
Non-negotiable exclusions:

- Real coordinates, real site geometry, or plausible sensitive shapes
- Real names, identifying text, or any PII
- Secrets (tokens, keys, credentials) or production endpoints
- Any content that could be interpreted as restricted cultural knowledge

This is a **policy simulation** fixture set, not an authoritative governance ledger.

---

## 🗂️ Directory Layout

~~~text
📁 tests/                                                                  — Test platform root (unit / integration / e2e)
└── 📁 e2e/                                                                — End-to-end suites (browser + API + governance)
    └── 📁 web-app/                                                        — UI-focused E2E suites
        └── 📁 regression/                                                 — Broader coverage (non-smoke)
            └── 📁 focus-mode/                                             — Focus Mode v3 regression suites
                └── 📁 fixtures/                                           — Deterministic synthetic inputs (non-sensitive)
                    └── 📁 provenance/                                     — Provenance fixture set (synthetic)
                        └── 📁 governance/                                 — ← This folder (governance overlays)
                            ├── 📄 README.md                               — This guide (rules + shape)
                            ├── 🧾 fm_governance_overlay_001.json           — Baseline masked overlay (Tier B example)
                            ├── 🧾 fm_governance_overlay_002.json           — Restricted output overlay (redacted UI path)
                            └── 🧾 fm_governance_overlay_003.json           — Missing/partial overlay (UI fallback behavior)
~~~

**Directory policy**
- Overlay filenames MUST be stable and referenced by scenario specs.
- If a scenario introduces a new governance state, add a new overlay file rather than mutating an existing one (preserve regression stability).

---

## 🧭 Context

### Determinism requirements
Governance overlays MUST:
- be stable across runs (no runtime-generated IDs),
- be small and UI-oriented (high-signal keys only),
- avoid variable timestamps (unless the test explicitly validates time formatting).

### Sovereignty-safe simulation
To simulate sovereignty restrictions:
- represent restricted states via flags, resolution indicators, and redaction placeholders,
- never include the restricted content that would be withheld in production.

### Why this exists
Governance failures are high-impact because they can become user-visible:
- precision leakage,
- missing policy indicators,
- incorrect routing for sensitive content,
- redaction inconsistencies.

These fixtures ensure regression E2E tests can detect those failures early and deterministically.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Scenario loads"] --> B["API mock returns governance overlay"]
  B --> C["Focus Mode UI renders policy indicators"]
  C --> D["Assertions validate masking and restricted behavior"]
  D --> E["Reports and telemetry recorded"]
~~~

**Interpretation**  
Governance overlays are injected through mocks and drive UI policy surfaces; tests verify correct display and safe failure modes.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode policy surfaces (expected behaviors)
Using these overlays, regression E2E SHOULD validate:

- CARE tier is visible where required (label + optional tooltip)
- Sovereignty flags are visible where required
- Masking indicators are visible where required:
  - method (H3)
  - resolution (R7–R9 or project-approved range)
- Restricted-output state produces safe UI behavior:
  - redacted content placeholders
  - blocked download or safe-download messaging (if applicable)
  - no raw geometry or raw coordinates in tooltips / JSON views

### Interaction with provenance chips
Governance overlays complement provenance fixtures:
- provenance answers “where did this come from?”
- governance answers “what are we allowed to show?”

E2E assertions should confirm both layers are consistent:
- masked content has masking indicators
- restricted content has restricted indicators and safe UI behavior
- non-sensitive content has normal provenance display without extra masking noise

---

## 🧪 Validation & CI/CD

### Required checks (must pass)
- JSON parse validation
- secret scan / PII scan
- “no raw coordinates” scan (repo policy)
- required keys present for each overlay type (baseline and restricted)

### Recommended checks (should pass)
- scenario references are valid (each overlay used by at least one spec)
- overlay filenames are stable (no renames without updating scenario pointers)
- telemetry tags include governance suite category when overlays are exercised (`@governance`)

### Flake policy note
Governance failures are not retryable by default:
- do not hide governance issues behind retries,
- fix the behavior or quarantine the scenario behind scheduled runs only if explicitly approved.

---

## 📦 Data & Metadata

### Minimum overlay shape
Overlays SHOULD include these high-signal keys (names may be adapted to your UI contract, but must remain stable):

~~~json
{
  "overlay_id": "fm_governance_overlay_001",
  "care_tier": "Tier B",
  "public_exposure_risk": "Low",
  "sovereignty_flags": [],
  "masking": {
    "required": true,
    "method": "H3",
    "resolution": "R8",
    "precision_leak_guard": true
  },
  "restricted_output": {
    "active": false,
    "reason_code": "none",
    "ui_mode": "normal"
  },
  "ui_hints": {
    "show_care_badge": true,
    "show_sovereignty_badge": false,
    "show_masking_badge": true
  }
}
~~~

### Restricted overlay example
Restricted overlays MUST NOT contain restricted content; represent the restriction as policy state:

~~~json
{
  "overlay_id": "fm_governance_overlay_002",
  "care_tier": "Tier A",
  "public_exposure_risk": "High",
  "sovereignty_flags": ["restricted_context"],
  "masking": {
    "required": true,
    "method": "H3",
    "resolution": "R9",
    "precision_leak_guard": true
  },
  "restricted_output": {
    "active": true,
    "reason_code": "sovereignty_restriction",
    "ui_mode": "redacted"
  },
  "ui_hints": {
    "show_care_badge": true,
    "show_sovereignty_badge": true,
    "show_masking_badge": true,
    "redaction_copy_key": "restricted_content_withheld"
  }
}
~~~

### Required stability rules
- `overlay_id` MUST match the filename stem.
- `care_tier` MUST be present even for redacted states.
- `masking.precision_leak_guard` MUST be `true` for any state that is masked or restricted.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV alignment (testing semantics)
- A governance overlay fixture is a **synthetic policy artifact**, not a governance ledger entry.
- If represented in PROV terms:
  - fixture file is a `prov:Entity` used by a `prov:Activity` (the E2E run).

### DCAT alignment (optional)
If catalogs are produced for test artifacts:
- overlay fixtures may be treated as `dcat:Distribution` artifacts (`application/json`) under a test dataset.

### STAC alignment (optional)
If test artifacts are wrapped as STAC Items:
- set `geometry: null` (these are non-spatial policy artifacts),
- attach overlays as STAC assets only when exporting E2E artifacts externally.

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable rules
These overlays MUST enforce safe testing behavior:
- no precision leakage,
- no restricted knowledge content,
- no PII or secrets,
- deterministic, auditable policy state representation.

### Escalation
If a governance overlay-driven test indicates the UI can expose restricted material:
- treat as merge-blocking,
- route to FAIR+CARE Council + relevant working group,
- record the incident per audit policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governance overlay fixture guide aligned to KFM-MDP v11.2.6; enforced emoji directory layout; defined minimum overlay shapes for masked and restricted states. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

