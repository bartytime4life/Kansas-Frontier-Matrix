---
title: "🛡️ Kansas Frontier Matrix — Governance Regression Tests (E2E Web App) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/README.md"

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
intent: "tests-e2e-web-app-regression-governance"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/README.md"
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
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

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
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/web-app/regression/governance/README.md@v11.2.6"
---

<div align="center">

# 🛡️ **Governance Regression Tests (E2E Web App) (v11 LTS)**
`tests/e2e/web-app/regression/governance/README.md`

**Purpose**  
Define the **canonical governance regression E2E suite** for the KFM web app.  
This folder validates **FAIR+CARE routing**, **sovereignty masking**, **restricted-state UX**, and **provenance surfaces** using **deterministic, synthetic fixtures**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App-blueviolet" />
<img src="https://img.shields.io/badge/Suite-Regression-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Regression Index](../README.md) ·
[🧭 E2E Guide](../../../README.md) ·
[🧪 Tests Index](../../../../README.md)

</div>

---

## 📘 Overview

Governance regression tests are **policy-level E2E assertions** that confirm the UI does not regress into unsafe or non-compliant behavior.

This suite focuses on **user-visible governance behavior**, including:
- 🏷️ CARE tier display and routing (Tier A/B/C behaviors).
- 🪶 Sovereignty masking invariants (no precision leakage; generalized/blocked where required).
- 🧾 Provenance and evidence surfaces (IDs/hashes/links are present; no payload dumps).
- 🚫 Restricted states (redacted, masked, or blocked UX behaves deterministically).
- 📦 Export/download behaviors (no sensitive precision in tooltips, JSON views, or downloads).

Out of scope:
- Model accuracy evaluation (handled by model cards + experiments).
- Back-end policy engines beyond the surfaces they expose to the UI.
- Any test relying on production tokens, production data, or external networks as a required dependency.

---

## 🗂️ Directory Layout

This folder is organized for **clear policy intent**, **CI parallelism**, and **fixture safety**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                ├── 📄 README.md                           — This guide (governance regression scope + rules)
                │
                ├── 📁 specs/                              — Governance regression specs (runner-specific)
                │   ├── 📄 README.md                        — Spec conventions (tags, determinism, flake policy)
                │   └── 🧾 *.spec.*                         — Test specs (format depends on runner)
                │
                ├── 📁 fixtures/                            — Synthetic governance states (non-identifying)
                │   ├── 📄 README.md                        — Fixture rules (no raw coords, no real entities)
                │   ├── 🧾 governance_registry.json          — Scenario registry (ID → bundle refs)
                │   └── 📁 scenarios/
                │       ├── 📄 README.md                    — Scenarios index
                │       └── 📁 gov_synth_00x/               — Scenario bundles (safe/masked/restricted)
                │
                ├── 📁 assertions/                          — Shared governance assertions (high-signal, reusable)
                │   └── 📄 README.md                        — Assertion catalog + required invariants
                │
                ├── 📁 artifacts/                           — Runner outputs (reports/traces/screenshots)
                │   └── 📄 README.md                        — Artifact layout + retention rules
                │
                └── 📁 utils/                               — Helpers (selectors, waits, policy-safe parsers)
                    └── 📄 README.md                        — Utility conventions (no sleeps; event-based waits)
~~~

Policy notes:
- Keep governance assertions centralized under `📁 assertions/` so they remain consistent across suites.
- Keep fixtures minimal and synthetic; store only what is required for deterministic policy checks.

---

## 🧭 Context

### Determinism contract (non-negotiable)
Governance regressions MUST:
- use synthetic, deterministic fixtures,
- use event-based waits (selector/state/network idle), not time-based sleeps,
- be idempotent and isolated (no cross-test coupling),
- avoid “live time” unless injected by a deterministic clock provider.

### Governance invariants (what must never regress)
All governance regressions SHOULD assert at least these invariants:

1. **No sensitive precision leakage**
   - No raw coordinates in UI text, tooltips, debug views, downloads, or exported JSON.
   - Masked/restricted states must remain masked/restricted through navigation.

2. **CARE routing is visible and consistent**
   - CARE tier label is present when required.
   - Tier routing produces correct UX state (allowed vs masked vs blocked).

3. **Sovereignty indicators behave correctly**
   - Sovereignty flag visibility is consistent with fixture state.
   - Any “restricted” state triggers safe fallback UI.

4. **Provenance surfaces are present**
   - Evidence/provenance chips contain stable IDs/hashes/links.
   - Provenance does not expose full payloads or raw sensitive geometry.

5. **Exports remain policy-safe**
   - Export actions produce either safe content (masked/generalized) or a blocked response.
   - Any “download” flow is audited and deterministic.

### Tagging guidance (runner-agnostic)
Recommended tags:
- `@regression` for this folder by default
- `@governance` for policy-level gates
- `@nightly` for slow matrix tests (browser permutations, heavy artifact generation)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Start E2E regression run"] --> B["Boot test stack (UI/API)"]
  B --> C["Load synthetic governance fixtures"]
  C --> D["Run governance specs"]
  D --> E["Assert masking and routing invariants"]
  E --> F["Collect artifacts (report, trace, screenshots)"]
  F --> G["Write telemetry summary"]
  G --> H["CI gate: pass or block merge"]
~~~

Interpretation:
- Governance regressions are executed against a controlled test stack using synthetic fixtures and must produce auditable artifacts and telemetry before CI allows merges.

---

## 🧪 Validation & CI/CD

Governance regressions are **merge-blocking** when included in required pipelines.

Minimum CI expectations:
- Secrets scan and PII scan must pass.
- Fixture validation must pass (JSON parse + schema where available).
- Governance assertions must be **retry-resistant**:
  - governance failures are not retried by default,
  - any retry must be explicitly justified and tracked.

Required artifacts per run (recommended):
~~~text
📁 reports/
└── 📁 e2e/
    ├── 🧾 junit.xml
    ├── 🧾 report.json
    ├── 📁 traces/
    ├── 📁 screenshots/
    └── 🧾 run-manifest.json
~~~

Telemetry aggregation target (repo standard):
~~~text
📁 releases/
└── 📁 <version>/
    └── 🧾 tests-e2e-telemetry.json
~~~

---

## 📦 Data & Metadata

### Fixture source of truth
Governance regressions MUST use synthetic fixtures from:
- `tests/e2e/web-app/regression/governance/fixtures/`
- and/or shared synthetic assets under `tests/fixtures/`

No production datasets. No real individuals. No plausible real “site-like” coordinates.

### Recommended run-manifest fields
A governance regression run SHOULD emit:
- `run_id`
- `suite_tags`
- `scenario_ids` executed
- `browser_matrix`
- `seed` (if used)
- `env_hash`
- `artifact_paths`
- `governance_mode_flags`

Example (simplified):
~~~json
{
  "run_id": "e2e_governance_2025-12-13_001",
  "suite_tags": ["@regression", "@governance"],
  "scenario_ids": ["gov_synth_001", "gov_synth_002"],
  "browser_matrix": ["chromium"],
  "env_hash": "<sha256>",
  "artifacts": {
    "report": "reports/e2e/report.json",
    "junit": "reports/e2e/junit.xml"
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (tests as governed activities)
- A governance regression run is a `prov:Activity`.
- Fixtures, configs, and reports are `prov:Entity`.
- CI jobs, maintainers, and councils are `prov:Agent`.

### DCAT alignment (reports as distributions)
- The suite report is a `dcat:Distribution` (e.g., `mediaType: application/json`).
- The README and runbook docs are documentation records (`text/markdown`).

### STAC alignment (optional)
If E2E artifacts are indexed as STAC items:
- use `geometry: null`,
- store artifacts as assets (report, traces, screenshots),
- keep content synthetic and non-sensitive.

---

## 🧱 Architecture

Governance regressions should follow a stable pattern:
- Page objects for navigation and stable selectors
- Shared assertion library for governance invariants
- Scenario registry + fixture bundles for deterministic state selection
- Event-based waiting (UI state / network idle / DOM ready)

Recommended separation of concerns:
- `specs/` decides what to test
- `fixtures/` defines safe scenario inputs
- `assertions/` defines policy invariants
- `utils/` provides stable primitives (selectors, waits)

---

## ⚖ FAIR+CARE & Governance

### Sovereignty rules (binding)
These tests MUST:
- never include raw sensitive precision,
- confirm masked and restricted states are enforced end-to-end,
- treat any detected leakage as a stop-ship failure.

### Ethical language in fixtures (required)
Synthetic text used in governance tests MUST:
- avoid colonial framing or harmful phrasing,
- avoid implying genealogy or sacred knowledge,
- remain minimal and functional.

### Escalation path
Any governance regression failure that indicates:
- precision leakage,
- policy bypass,
- restricted-state malfunction,
must be routed to the relevant working group and the FAIR+CARE Council per governance policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governance regression E2E guide aligned to KFM‑MDP v11.2.6 (emoji layout, determinism rules, policy invariants, artifact + telemetry expectations). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

