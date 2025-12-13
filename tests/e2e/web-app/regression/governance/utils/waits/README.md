---
title: "⏳ Kansas Frontier Matrix — Deterministic Wait Utilities (Governance Regression E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/waits/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Utility Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-utils-waits"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-utils-waits-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:waits:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/waits/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/waits/README.md@v11.2.6"
---

<div align="center">

# ⏳ **Deterministic Wait Utilities (Governance Regression E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/waits/README.md`

**Purpose**  
Define the **canonical wait strategy utilities** used by governance regression E2E suites to achieve:
- deterministic readiness checks (UI, API, map, timeline),
- reduced flake (event-driven waits, not sleeps),
- governance-safe scanning points (avoid racing into unsafe transient states),
- auditable timeouts and budgets (consistent CI behavior).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Deterministic%20Waits-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Sleep%20Reliance-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Utilities](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

Wait utilities are **shared helpers** that ensure E2E tests interact with the web app only when the relevant surface is:

- loaded,
- stable,
- and ready for deterministic assertions.

For governance regression suites, correct waiting is policy-critical: it prevents tests from sampling transient UI states that could produce false positives/negatives (or accidentally capture unsafe debug content).

### Wait utilities exist to enforce these rules

- ✅ Prefer **event- and state-based waits** over time-based sleeps.
- ✅ Use **stable selectors** (typically `data-testid`) and well-defined readiness signals.
- ✅ Keep timeouts consistent and configurable (per CI stage / suite tag).
- ✅ Return structured wait results to support telemetry and debugging.
- ✅ Fail with actionable context (what was waited for; which signal did not arrive).

### Non-goals

- Wait utilities are not “performance benchmarking” tools.
- Wait utilities do not mask governance failures; they only prevent race conditions.
- Wait utilities must not print raw payloads or store unsafe dumps in artifacts.

---

## 🗂️ Directory Layout

This folder typically contains wait primitives and composed readiness helpers used across governance E2E specs.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    ├── 📁 waits/
                    │   ├── 📄 README.md                         — This guide
                    │   ├── 📄 wait_config.ts                    — Timeout budgets + suite defaults
                    │   ├── 📄 wait_dom.ts                       — DOM/state waits (visible/hidden/attached)
                    │   ├── 📄 wait_network.ts                   — Request/response waits (idle, specific endpoints)
                    │   ├── 📄 wait_route.ts                     — Route + navigation stabilization
                    │   ├── 📄 wait_focus_mode.ts                — Focus Mode ready checks (Context/Timeline/Map)
                    │   ├── 📄 wait_story_node.ts                — Story Node ready checks (narrative/spacetime/provenance)
                    │   ├── 📄 wait_map.ts                       — Map readiness (tiles/layers/tooltips safe)
                    │   ├── 📄 wait_timeline.ts                  — Timeline readiness (events loaded, brush stable)
                    │   ├── 📄 wait_a11y.ts                      — A11y readiness (focus traps, landmarks present)
                    │   ├── 📄 wait_result.ts                    — Structured result model + serialization
                    │   └── 📄 index.ts                          — Public exports for specs
                    │
                    ├── 📁 selectors/                             — Stable selectors (data-testid registry)
                    ├── 📁 parsing/                               — Safe extraction + normalization helpers
                    ├── 📁 telemetry/                             — Telemetry utilities + schema validation
                    └── 📁 leak_checks/                           — Precision-leak detection utilities
~~~

Notes:
- Filenames above represent a **canonical target layout**. Use different names only if the intent remains identical.
- Governance suites should import waits only through a stable entry point (e.g., `waits/index.ts`) to reduce churn.

---

## 🧭 Context

### Determinism rules (waits are policy)

Wait utilities MUST:

- avoid “sleep-and-hope” patterns (e.g., `waitForTimeout(2000)`),
- tie readiness to observable state transitions,
- avoid coupling tests to rendering timing differences across CI machines,
- keep timeouts consistent and documented (budgets).

### Preferred wait types (in priority order)

1. **State readiness**
   - component indicates “ready” via deterministic selectors (e.g., `data-testid=panel-ready`)
2. **Network completion**
   - required requests finish (specific endpoint matching, not global network silence)
3. **UI stability**
   - the UI has reached a stable state (no loading spinners; counts match expected minimum)
4. **Functional invariants**
   - map layers visible; timeline entries present; provenance chips non-empty

### Anti-patterns (avoid)

- waiting on arbitrary timeouts
- waiting on CSS animation end without reduced-motion controls
- waiting on unstable selectors (e.g., brittle class names)
- waiting for “network idle” globally in apps with long polling or telemetry beacons
- using waits that cause unsafe output:
  - printing full DOM HTML
  - logging full JSON payloads to the console

### Governance-safe debug rule

When a wait fails:
- report **what signal** failed (selector, request name, condition),
- include **hashes/IDs** when useful,
- do NOT include full payload content or coordinate-like strings.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E step begins"] --> B["Select wait strategy (route/network/ui)"]
  B --> C["Wait for deterministic readiness signals"]
  C --> D["Run assertions (governance + leak checks)"]
  D --> E["Write structured wait + telemetry artifacts"]
  E --> F["CI gate: pass or block"]
~~~

Interpretation:
- Wait utilities are the “stabilizer” between navigation and governance assertions.

---

## 🧠 Story Node & Focus Mode Integration

Governance regressions frequently validate narrative surfaces. Wait utilities MUST support reliable readiness for:

### Story Node v3

Common readiness signals to wait for:

- route resolved (URL and router state stable),
- Story Node title and narrative container visible,
- spacetime panel stable (no loading state),
- provenance chips present (minimum count) without expanding into raw dumps.

Recommended helper signature (illustrative):

~~~ts
// wait_story_node.ts (illustrative)
export async function waitForStoryNodeReady(page: any, opts?: any): Promise<any> {
  // Wait for route stability + key UI anchors.
}
~~~

### Focus Mode v3

Common readiness signals to wait for:

- “Context / Timeline / Map” panels present,
- at least one evidence/provenance anchor visible (ID/hash),
- map canvas ready and layers rendered (policy-safe),
- timeline entries loaded and stable.

Recommended helper signature (illustrative):

~~~ts
// wait_focus_mode.ts (illustrative)
export async function waitForFocusModeReady(page: any, opts?: any): Promise<any> {
  // Wait for panel-ready markers + stable counts.
}
~~~

Minimum governance invariant:
- waits must not require expanding restricted details to prove readiness.

---

## 🧪 Validation & CI/CD

Wait utilities are part of CI quality enforcement.

### What CI expects

- wait utilities must be deterministic and stable under parallel execution,
- failures should be actionable (clear reason),
- suite time budgets must be respected (avoid long default timeouts).

### Recommended policies

- `@smoke` waits:
  - shorter budgets, minimal readiness
- `@governance` waits:
  - allow a slightly larger budget, but never rely on sleeps
- `@nightly` waits:
  - acceptable to include deeper readiness checks (still deterministic)

### Flake policy

If a test is flaky due to waiting:
- fix the wait strategy (event/state-based),
- do not raise timeouts as the primary solution,
- do not add retries as a substitute for determinism.

---

## 📦 Data & Metadata

### Wait configuration (recommended minimal shape)

Wait budgets should be centralized and referenced by suite tag.

~~~json
{
  "schema_version": "v11.2.6",
  "budgets_ms": {
    "@smoke": {
      "route": 5000,
      "network": 5000,
      "ui_ready": 8000
    },
    "@governance": {
      "route": 8000,
      "network": 8000,
      "ui_ready": 12000
    }
  },
  "default_suite": "@governance"
}
~~~

### Structured wait result (recommended)

Wait helpers SHOULD return structured results that can be written to artifacts safely.

~~~json
{
  "schema_version": "v11.2.6",
  "wait_id": "focus_mode_ready",
  "run_id": "e2e_2025-12-13_001",
  "scenario_id": "governance_masked_required",
  "status": "pass",
  "duration_ms": 2140,
  "signals": [
    { "type": "selector", "name": "data-testid=context-panel-ready", "observed": true },
    { "type": "selector", "name": "data-testid=timeline-panel-ready", "observed": true },
    { "type": "selector", "name": "data-testid=map-panel-ready", "observed": true }
  ],
  "evidence": {
    "hash": "<sha256>"
  }
}
~~~

Notes:
- Never store raw DOM or payload dumps in wait results.
- Prefer rule IDs, selector names, and hashes.

---

## 🌐 STAC, DCAT & PROV Alignment

Wait results and related artifacts are test outputs.

- **DCAT**
  - wait result JSON can be treated as a `dcat:Distribution` artifact (`mediaType: application/json`)
- **STAC**
  - if represented as a STAC item:
    - `geometry: null`
    - `properties.datetime` = run timestamp
    - assets: `wait-results.json`
- **PROV-O**
  - a wait is part of the E2E run `prov:Activity`
  - wait config and selector registry are `prov:Entity`
  - CI runner is a `prov:Agent`

---

## 🧱 Architecture

### Recommended composition model

Wait utilities SHOULD be layered:

1. **Primitives**
   - wait for selector visible/hidden
   - wait for route stable
   - wait for a specific network request to complete
2. **Domain waits**
   - Story Node ready
   - Focus Mode ready
   - map/timeline ready
3. **Governance waits**
   - governance overlay present
   - restricted-state banner present (without expanding restricted content)
4. **Instrumentation**
   - wait result objects for telemetry + artifact export

### Guardrails

- Avoid “global network idle” if the app emits background telemetry.
- Prefer waiting on known endpoint completion or on UI readiness markers.
- Prefer reduced-motion mode in E2E so animation timing does not cause flakes.

---

## ⚖ FAIR+CARE & Governance

Wait utilities protect governance correctness by preventing race conditions.

They MUST uphold:

- **Authority to Control**
  - do not require accessing restricted content to prove readiness
- **Responsibility**
  - fail clearly when governance states do not stabilize
- **Ethics**
  - no PII, no sensitive-like coordinates, no raw dumps
- **Collective Benefit**
  - deterministic waits reduce CI churn and prevent “works on my machine” regressions

If a wait strategy requires unsafe introspection to become reliable, treat it as a design failure:
- add a policy-safe readiness marker in the UI,
- or expose a safe state indicator in test mode,
- do not weaken governance enforcement.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial deterministic wait utilities guide aligned to KFM‑MDP v11.2.6 (event-based waits, structured results, governance-safe diagnostics). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

