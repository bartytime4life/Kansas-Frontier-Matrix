---
title: "📚 Kansas Frontier Matrix — Story Nodes v3 Regression (Web App E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/storynodes/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-storynodes"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-storynodes-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:storynodes:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/storynodes/README.md"
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
  - "tests/e2e/web-app/regression/storynodes/README.md@v11.2.6"
---

<div align="center">

# 📚 **Story Nodes v3 Regression (Web App E2E) (v11 LTS)**
`tests/e2e/web-app/regression/storynodes/README.md`

**Purpose**  
Define the **canonical regression coverage** for **Story Nodes v3** in the KFM web application.  
This suite validates Story Node rendering, navigation, provenance surfaces, and governance invariants using **synthetic**, **deterministic**, **sovereignty-safe** fixtures.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Suite-Web%20App%20Regression-blueviolet" />
<img src="https://img.shields.io/badge/Surface-Story%20Nodes%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App Regression](../README.md) ·
[🧭 E2E Guide](../../../README.md) ·
[🧪 Tests Index](../../../../README.md)

</div>

---

## 📘 Overview

Story Nodes are a **user-visible governed narrative surface**. Regression E2E coverage for Story Nodes focuses on:

- 🧩 **Rendering correctness** (title, summary/narrative, relations, spacetime panels)
- 🧭 **Navigation invariants** (deep links, back/forward, refresh stability)
- 🧾 **Provenance surfaces** (IDs/hashes/links present; no raw payload dumps)
- 🛡️ **Governance behavior** (CARE tier visibility, sovereignty masking, restricted states)
- ♿ **Accessibility** (heading order, landmark structure, keyboard navigation, reduced motion)
- 🔒 **No-leak guarantees** (no raw coordinates, no high-precision geometry exposure)

### What this suite is responsible for

This suite SHOULD validate (minimum set):
- Story Node route loads without console errors.
- Critical UI panels render within deterministic budgets (ready markers).
- Provenance chips exist and remain non-empty (IDs/hashes only).
- Spacetime visualizations never expose raw precision beyond policy.
- Restricted and masked scenarios remain stable across navigation transitions.

This suite SHOULD NOT:
- depend on production services, real datasets, or unrestricted external network calls,
- embed full real-world narratives or plausible restricted knowledge,
- treat “sleep” timing as a correctness requirement.

---

## 🗂️ Directory Layout

This folder is organized for **runner-friendly specs**, **fixture discovery**, and **auditable expected outputs**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 storynodes/
                ├── 📄 README.md                                  — This guide
                │
                ├── 📁 specs/                                     — Runner entrypoints for Story Node regressions
                │   ├── 📄 storynodes_smoke.spec.ts               — Minimal merge-blocking Story Node smoke
                │   ├── 📄 storynodes_regression.spec.ts          — Broader Story Node regression coverage
                │   └── 📄 storynodes_governance.spec.ts          — Masking/restriction/leak-check focused spec
                │
                ├── 📁 fixtures/                                  — Synthetic fixtures (non-identifying, deterministic)
                │   ├── 🧾 scenario_registry.json                  — Scenario ID → bundle mapping
                │   ├── 📁 scenarios/                              — Scenario bundles
                │   │   ├── 🧾 sn_public.json                       — Public-safe Story Node scenario
                │   │   ├── 🧾 sn_masked.json                       — Masked/generalized scenario
                │   │   └── 🧾 sn_restricted.json                   — Restricted scenario (blocked/redacted UX)
                │   ├── 📁 api_mocks/                              — Optional API response stubs (if interception is used)
                │   ├── 📁 expected_ui/                            — Expected “high-signal” UI assertions
                │   └── 📁 provenance/                             — Provenance fragments (IDs/hashes only)
                │
                ├── 📁 utils/                                     — Story Node–specific helpers (selectors/waits/assertions)
                └── 📁 artifacts/                                 — Local-only templates for artifacts (no sensitive dumps)
~~~

Notes:
- The tree above is the **canonical target layout** for this suite.
- Adapt filenames/extensions to your runner, but preserve the structure and intent.

---

## 🧭 Context

### Determinism contract (Story Nodes)

E2E Story Node tests MUST:
- use synthetic fixture IDs and stable ordering,
- use deterministic clocks where supported (injectable time provider),
- wait on explicit readiness signals (route ready, panel ready) rather than time sleeps,
- isolate tests so one scenario cannot corrupt another.

Recommended “ready markers”:
- route root: `data-testid=storynode-page`
- content panel: `data-testid=storynode-narrative`
- provenance panel: `data-testid=provenance-panel`
- spacetime/map panel: `data-testid=storynode-spacetime` (or equivalent)

### Sovereignty and safety constraints (non-negotiable)

Story Node regressions MUST:
- never assert or store raw sensitive coordinates (even in “fake” examples),
- ensure masked scenarios remain masked across UI interactions,
- ensure restricted scenarios remain blocked/redacted across navigation and refresh,
- ensure any “details/JSON” surfaces do not dump raw geometry or full payloads.

### High-signal assertions (recommended)

- ✅ No raw coordinate patterns appear in page text or tooltips.
- ✅ Provenance chips show stable IDs/hashes and link safely (no expansion to raw payload dumps).
- ✅ Relations display expected counts and types for the scenario (minimal deterministic graph simulation).
- ✅ Timeline respects OWL-Time intervals (ordering and granularity are stable for the fixture).
- ✅ “Download/export” actions (if present) remain governance-safe (filenames/metadata only).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load fixture bundle"]
  B --> C["Open Story Node route"]
  C --> D["Wait for page ready markers"]
  D --> E["Assert UI panels and provenance chips"]
  E --> F["Run governance leak checks"]
  F --> G["Write artifacts and telemetry summary"]
~~~

Interpretation:
- Story Node E2E regressions are fixture-driven and must enforce governance invariants before CI allows a merge.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes frequently route into Focus Mode, and regressions should validate cross-surface invariants.

### Story Node v3 expectations

Story Node regressions SHOULD validate:
- narrative content renders with safe formatting (no broken headings/landmarks),
- provenance chips exist for governed claims (IDs/hashes only),
- spacetime is displayed safely:
  - masked/generalized where required,
  - no raw coordinate text in UI,
  - no high-precision bbox output in tooltips.

### Focus Mode v3 transition expectations

If a Story Node provides a “Focus Mode” entrypoint, regressions SHOULD validate:
- navigation into Focus Mode preserves entity identity,
- governance badges persist (CARE tier, sovereignty),
- restricted state remains restricted across the transition.

---

## 🧪 Validation & CI/CD

### Merge-blocking behavior (recommended)

At minimum:
- `storynodes_smoke.spec.*` is merge-blocking for web-app changes.
- `storynodes_governance.spec.*` is merge-blocking for changes touching governed narrative surfaces.

### Required artifacts

Each run MUST produce:
- machine-readable report (JUnit/JSON),
- traces or videos where supported,
- screenshots on failure,
- run manifest with scenario IDs and tags.

Recommended path:
~~~text
reports/
└── e2e/
    ├── junit.xml
    ├── report.json
    ├── traces/
    ├── screenshots/
    └── run-manifest.json
~~~

### Flake policy

- Story Node tests must not be “fixed” with sleeps.
- Governance-related failures are not retryable by default.
- If readiness is flaky, introduce stable test IDs and deterministic wait utilities.

---

## 📦 Data & Metadata

### Scenario registry (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "sn_public": {
      "bundle": "scenarios/sn_public.json",
      "expected": "expected_ui/sn_public_expected.json",
      "provenance": "provenance/sn_public_prov.json",
      "tags": ["@smoke", "@regression"]
    },
    "sn_masked": {
      "bundle": "scenarios/sn_masked.json",
      "expected": "expected_ui/sn_masked_expected.json",
      "provenance": "provenance/sn_masked_prov.json",
      "tags": ["@regression", "@governance"]
    },
    "sn_restricted": {
      "bundle": "scenarios/sn_restricted.json",
      "expected": "expected_ui/sn_restricted_expected.json",
      "provenance": "provenance/sn_restricted_prov.json",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Expected UI (what belongs there)

Expected UI files MUST contain only **high-signal assertions**:
- panel readiness flags,
- expected counts (relations, evidence chips),
- governance badges expected (CARE tier, sovereignty visibility),
- forbidden surface expectations (no raw coordinates; no geometry dumps).

### Provenance fragments (IDs/hashes only)

Provenance fixture fragments SHOULD include:
- synthetic dataset IDs, experiment IDs, model card IDs where relevant,
- stable hash placeholders,
- governance mode indicators for the scenario.

They MUST NOT contain full documents, full payloads, or raw geometry.

---

## 🌐 STAC, DCAT & PROV Alignment

Story Node regression artifacts are test outputs (not scientific datasets):

- **DCAT**: reports/traces may be treated as `dcat:Distribution` artifacts (`mediaType: application/json`, `video/webm`, etc.).
- **STAC**: if indexed as STAC items:
  - `geometry: null`
  - `properties.datetime` set to run timestamp
  - assets: report, junit, traces, screenshots
- **PROV-O**:
  - regression run is `prov:Activity`,
  - fixture bundles and expected files are `prov:Entity`,
  - CI runner and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended suite architecture (composition-first)

Specs SHOULD:
- select a scenario ID from the registry,
- load bundle + expected + provenance fragments,
- drive UI using page objects and stable selectors,
- call shared assertions for:
  - panel readiness,
  - provenance chip presence,
  - no-leak checks,
  - restricted/masked invariants.

Anti-patterns:
- embedding fixture JSON inline in spec files,
- duplicating selectors across tests,
- logging full API payloads to console or artifacts.

---

## ⚖ FAIR+CARE & Governance

Story Node regressions protect non-negotiable requirements:

- **CARE**: ensure correct tier labeling and routing behaviors in UI.
- **Sovereignty**: prevent precision leakage that could enable harmful inference.
- **Ethics**: block culturally harmful or unsafe narrative surfacing patterns.
- **Auditability**: ensure provenance surfaces exist without leaking raw payloads.

If a governance failure is detected:
- block merges affecting governed narrative surfaces,
- fix application behavior or fixture design,
- do not weaken allowlists as a shortcut.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial Story Nodes v3 regression guide aligned to KFM‑MDP v11.2.6 (deterministic fixtures, governance-safe assertions, artifact requirements). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

