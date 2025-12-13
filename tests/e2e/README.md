---
title: "🧭 Kansas Frontier Matrix — End-to-End (E2E) Tests (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-tests-e2e-readme"
doc_uuid: "urn:kfm:tests:e2e:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/README.md"
immutability_status: "version-pinned"

signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active · Enforced"
doc_kind: "Testing Guide"
intent: "tests-e2e-guide"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_transform_permissions:
  - "formatting"
  - "clarity-edits"
  - "determinism-hardening"
  - "accessibility-improvements"
  - "governance-alignment"
ai_transform_prohibited:
  - "citation-fabrication"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — End-to-End (E2E) Tests (v11 LTS)**
`tests/e2e/README.md`

**Purpose**  
Define the **canonical E2E test suite** for Kansas Frontier Matrix (KFM) v11:  
UI + API + governance + narrative flows validated end-to-end using **deterministic, sovereignty-safe, synthetic** data and **CI-enforced** gates.

</div>

---

## 📘 Overview

E2E tests are the **system-level trust harness** for KFM. They validate that:

- 🧩 **User-facing workflows** behave correctly (navigation, rendering, interactions).
- 🔒 **Governance controls** are enforced (FAIR+CARE, sovereignty masking, prohibited outputs).
- 🧠 **Narrative surfaces** remain grounded and safe (Story Nodes, Focus Mode panels).
- 🗺️ **Spatial + temporal UX** is coherent (map layers, timeline interactions, query filters).
- 📊 **Telemetry + provenance** are emitted in expected shapes (OpenTelemetry + OpenLineage facets, test run artifacts, energy/carbon summaries).

E2E tests are **not** allowed to rely on:
- Real individuals, real sensitive locations, production tokens, or restricted datasets.
- External networks as a required dependency (unless explicitly whitelisted by governance).
- Non-deterministic clocks, random seeds, or flaky “sleep-and-hope” timing.

**Definition (KFM):**  
An E2E test is any test that crosses at least **two** of these boundaries in one run:
- UI ↔ API
- UI ↔ Graph-backed behavior (via API)
- UI ↔ Governance overlays / provenance views
- Dataset workflow ↔ validation ↔ publish gating
- Narrative surface ↔ masking / ethics / citation rules

---

## 🗂 Directory Layout

The E2E folder is organized for **stable discovery**, **CI parallelism**, and **governance-safe fixtures**.

~~~text
tests/
└── e2e/
    ├── README.md                       # This guide (E2E rules + runbook)
    │
    ├── web-app/                        # Browser-driven UI flows (maps, timeline, navigation)
    │   ├── smoke/                      # Fast “PR gate” scenarios (minimal, high-signal)
    │   ├── regression/                 # Broader UI behavior coverage
    │   └── accessibility/              # WCAG flows (keyboard, landmarks, reduced-motion)
    │
    ├── dataset-workflows/              # Upload → validate → publish flows (synthetic)
    │   ├── ingest-validate/            # Contract + schema gates
    │   └── publish-preview/            # Preview modes + release gating
    │
    ├── governance/                     # Ledger/provenance surfaces + masking enforcement
    │   ├── care/                       # CARE classification and routing
    │   └── sovereignty/                # Masking + restricted-output assertions
    │
    ├── storynodes/                     # Story Node v3 UI flows (rendering + provenance chips)
    ├── focus-mode/                     # Focus Mode v3 flows (Context/Timeline/Map panels)
    │
    ├── resources/                      # E2E-only deterministic fixtures (synthetic, non-sensitive)
    └── utils/                          # Page objects, selectors, stable helpers, wait strategies
~~~

**Directory policy**
- Keep **smoke** tests minimal and stable: they are merge-blocking.
- Put anything slower/flakier behind **nightly** or **scheduled** workflows.
- Fixtures must remain **synthetic**, **non-identifying**, and **mask-safe**.

---

## 🧭 Context

### Determinism rules (E2E is not allowed to “guess”)
E2E tests MUST:
- Use stable deterministic data fixtures (no live random generation at runtime unless seeded and recorded).
- Use deterministic time where possible (fixed clock / injectable time provider).
- Prefer event-based waits (UI state change, network idle, selector visible) over arbitrary sleeps.
- Avoid cross-test coupling: each test is isolated and idempotent.

### Sovereignty + ethics rules (non-negotiable)
E2E tests MUST:
- Never embed or assert raw sensitive coordinates (or any plausible “real site” geometry).
- Validate that restricted outputs remain masked/generalized at required H3 resolutions.
- Avoid narratives that imply genealogy, sacred-site inference, or culturally harmful framing.
- Use synthetic examples that **simulate** governance states without exposing real-world harm.

### What E2E tests should validate (high-signal checks)
Recommended assertions for KFM E2E suites:
- ✅ UI loads and renders without console errors.
- ✅ Map layers toggle and render within budgets (no “blank tile” regressions).
- ✅ Timeline interactions update filters deterministically.
- ✅ Provenance/lineage UI surfaces show expected references (IDs, hashes, links).
- ✅ CARE tier labels display correctly and route to expected gating behavior.
- ✅ Sovereignty masking is applied where required; raw precision never appears.

### Test naming + tagging
Use tags to control CI behavior:
- `@smoke` — PR gate, fastest, deterministic.
- `@regression` — broader coverage, allowed to take longer.
- `@governance` — CARE + sovereignty gating.
- `@a11y` — accessibility flows.
- `@nightly` — slow or high-volume suites.

---

## 🗺 Diagrams

The E2E test run is structured as a **gated pipeline** that blocks unsafe merges.

~~~mermaid
flowchart TD
  A["Trigger (PR or schedule)"] --> B["Build + boot test stack"]
  B --> C["Load synthetic fixtures"]
  C --> D["Run E2E suites (smoke/regression/governance/a11y)"]
  D --> E["Collect artifacts (screenshots/traces/reports)"]
  E --> F["Validate telemetry + governance outputs"]
  F --> G["CI gates: pass or block"]
~~~

**Interpretation:**  
E2E tests are executed only against a **controlled test stack**, using **synthetic fixtures**, and they must produce artifacts that can be audited (reports + telemetry) before CI allows a merge.

---

## 🧠 Story Node & Focus Mode Integration

E2E coverage must include **narrative surfaces** because they are where policy failures become user-visible.

### Story Node v3 E2E expectations
E2E tests SHOULD validate:
- Rendering of Story Node v3 fields (title, narrative body, spacetime, relations).
- Provenance chips / evidence links are present and non-empty.
- Spatial geometry is rendered only at permitted precision:
  - masked/generalized if sensitive
  - no raw coordinates displayed in UI
- Timeline panel respects OWL-Time intervals (start/end, ordering, granularity).

### Focus Mode v3 E2E expectations
E2E tests SHOULD validate:
- Three-panel behavior (Context / Timeline / Map) with consistent entity grounding.
- All claims shown in UI remain attributable to:
  - a graph entity, dataset reference, or experiment/model card reference
- Governance overlays trigger correctly:
  - CARE tier visible
  - sovereignty flags visible where required
  - restricted material withheld or generalized

### Minimum governance assertions (narrative)
E2E tests MUST assert:
- No speculative language is surfaced in governed outputs where the policy forbids it.
- No sensitive location precision is surfaced in tooltips, JSON views, or downloads.
- Any “restricted” state returns a safe UI response (redacted, masked, or blocked).

---

## 🧪 Validation & CI/CD

### Where E2E runs in CI
E2E is merge-blocking when tagged as `@smoke` (and optionally `@governance`).

Common CI stages:
1. Unit tests
2. Schema tests
3. Integration tests
4. **E2E smoke**
5. Accessibility
6. Governance validation
7. Telemetry validation

### Local runbook (canonical pattern)
Use project scripts (Node-based runner or equivalent). Keep these commands stable and documented in repo configs.

~~~bash
# From repo root (example pattern)
# 1) Start local stack (API + UI) in a deterministic test mode
# 2) Run E2E smoke suite
# 3) Store artifacts under reports/e2e/

make test-stack-up
make e2e-smoke
make test-stack-down
~~~

If the repo uses Playwright/Cypress scripts, ensure the same intent exists:
- `e2e:smoke`
- `e2e:regression`
- `e2e:a11y`
- `e2e:governance`

### Required E2E artifacts
Every E2E run MUST produce:
- A machine-readable report (JUnit/JSON)
- Screenshots for failures
- A trace or video artifact (where supported)
- A deterministic run manifest (seed, environment hash, suite tags)

Recommended artifact locations:
~~~text
reports/
└── e2e/
    ├── junit.xml
    ├── report.json
    ├── traces/
    ├── screenshots/
    └── run-manifest.json
~~~

### Flake policy (strict)
- Flaky tests are quarantined behind `@nightly` until fixed.
- Retries are allowed only with a recorded reason and a tracking issue.
- Any governance-related failure is **not** retryable by default.

---

## 📦 Data & Metadata

### Fixture source of truth
E2E tests MUST use synthetic fixtures from:
- `tests/fixtures/` (general synthetic assets)
- `tests/e2e/resources/` (E2E-specific synthetic assets)

No production data. No sensitive coordinates. No identifying text.

### Metadata requirements for E2E runs
Each E2E run SHOULD write a run manifest including:
- `run_id`, `job_id`
- suite tags executed
- browser + viewport profiles
- environment hash
- seed(s)
- artifact paths
- governance mode flags

Example:
~~~json
{
  "run_id": "e2e_2025-12-13_001",
  "suite_tags": ["@smoke", "@governance"],
  "browser_matrix": ["chromium"],
  "seed": 112233,
  "env_hash": "<sha256>",
  "artifacts": {
    "report": "reports/e2e/report.json",
    "junit": "reports/e2e/junit.xml",
    "traces_dir": "reports/e2e/traces/"
  }
}
~~~

### Telemetry requirements
E2E must contribute to repo-level telemetry:
- runtime duration
- failures by category
- a11y counts (violations, regressions)
- energy/carbon where available

Expected aggregation target:
~~~text
releases/<version>/tests-e2e-telemetry.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT alignment (documentation + reports)
- This document may be treated as a documentation dataset (`dcat:Dataset`).
- E2E reports are `dcat:Distribution` artifacts (e.g., `mediaType: application/json`).

### STAC alignment (non-spatial artifacts)
E2E outputs may be represented as non-spatial STAC Items:
- `geometry: null`
- `properties.datetime` set to run timestamp
- assets: report, junit, traces, screenshots

### PROV-O alignment (what E2E produces)
- An E2E run is a `prov:Activity`.
- Fixtures, configs, and built artifacts are `prov:Entity`.
- CI, maintainers, and governance bodies are `prov:Agent`.

Example PROV fragment (simplified):
~~~json
{
  "prov:entity": {
    "e2e_report": { "prov:label": "E2E report JSON", "prov:type": "kfm:TestArtifact" }
  },
  "prov:activity": {
    "e2e_run": { "prov:label": "E2E run", "prov:type": "kfm:TestRun" }
  },
  "prov:wasGeneratedBy": {
    "e2e_report_generation": { "prov:entity": "e2e_report", "prov:activity": "e2e_run" }
  }
}
~~~

---

## 🧱 Architecture

### E2E platform components (conceptual)
E2E testing is built from these stable parts:
- **Runner**: executes suites, manages retries/quarantine, records artifacts.
- **Stack bootstrap**: brings up UI/API in deterministic “test mode”.
- **Synthetic fixture loader**: injects non-sensitive test data and known states.
- **Governance gate**: ensures masking and policy enforcement is testable and visible.
- **Telemetry sink**: validates emissions and aggregates run summaries.

### E2E test design pattern (recommended)
- Page objects or stable selectors for UI interactions
- Explicit waits on events/state (not time)
- One test → one primary claim (high-signal failure diagnosis)
- Deterministic test IDs for Story Nodes / entities
- Clear separation of:
  - “smoke” (fast PR gate)
  - “regression” (broader)
  - “governance/a11y” (policy + UX quality)

---

## ⚖ FAIR+CARE & Governance

### Minimum governance gate (E2E must enforce)
E2E suites MUST block merges if they detect:
- Sensitive precision leakage (coordinates, geometry dumps, tooltips, downloads)
- CARE tier routing failures (Tier A/B/C logic mismatched)
- Narrative safety failures in governed surfaces
- Provenance surfaces missing required references (IDs/hashes/links)
- Accessibility regressions (WCAG-critical failures)

### Ethical fixture rules
Fixtures MUST:
- Remain synthetic and non-identifying
- Avoid colonial framing or culturally harmful phrasing (even in test text)
- Avoid plausible reproduction of restricted knowledge
- Carry minimal metadata needed for deterministic testing

### Escalation
If a governance-related E2E test fails:
- Treat as a **stop-ship** for merges affecting governed outputs.
- Route to FAIR+CARE Council and the relevant working group for review.
- Document the failure in the governance/audit ledger (per project policy).

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed E2E guide aligned to KFM-MDP v11.2.6 (deterministic, sovereignty-safe, telemetry-aware). |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
**Diamond⁹ Ω / Crown∞Ω** · E2E Testing · Deterministic · Sovereignty-Safe · FAIR+CARE

[⬅️ Back to Tests Index](../README.md) · [🏗 Test Architecture](../ARCHITECTURE.md) · [🛡 Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

