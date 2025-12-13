---
title: "🧰 Kansas Frontier Matrix — E2E Utilities (Deterministic Helpers) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/utils/README.md"

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
intent: "tests-e2e-utils-guide"

semantic_document_id: "kfm-tests-e2e-utils-readme"
doc_uuid: "urn:kfm:tests:e2e:utils:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/utils/README.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

telemetry_ref: "../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tests-e2e-v11.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_transform_permissions:
  - "summarize"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "citation-fabrication"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/utils/README.md@v11.2.6"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — E2E Utilities (Deterministic Helpers) (v11 LTS)**
`tests/e2e/utils/README.md`

**Purpose**  
Define the required utility patterns for KFM E2E tests: stable selectors, deterministic waits, governance-safe assertions, artifact capture, and telemetry hooks.

[🧭 E2E Guide](../README.md) ·
[🧪 Tests Index](../../README.md) ·
[🧱 Test Architecture](../../ARCHITECTURE.md) ·
[🧱 Fixtures](../../fixtures/README.md) ·
[🏛️ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

---

## 📘 Overview

This folder contains reusable helpers used by E2E suites to keep tests:

- ✅ deterministic (no flake-by-sleep, no nondeterministic clocks, no hidden randomness)
- 🧭 governance-safe (no coordinate leakage, no sensitive outputs, no policy bypass)
- ♿ accessibility-aware (role-based selectors, keyboard-first helpers, a11y assertions)
- 📦 artifact-rich (trace/screenshot/report manifests that are consistent in CI and local runs)
- 📊 telemetry-aligned (test run metadata emitted in predictable schema shape)

Utilities MUST be safe to use in:
- `@smoke` suites (merge-blocking)
- `@governance` suites (CARE + sovereignty gates)
- `@a11y` suites (WCAG regressions)
- `@regression` suites (broader coverage)

---

## 🧩 What Belongs Here

### ✅ Allowed
Utilities that are:
- pure helpers (selectors, waits, parsing, stable transforms)
- page objects / screen models (navigation + interaction)
- governance assertions (masking checks, redaction checks, prohibited output checks)
- artifact helpers (trace naming, screenshot capture, failure bundle formatting)
- telemetry helpers (run-manifest writers, schema-shape validators)

### ❌ Not allowed
- production secrets, tokens, or credentials
- “magic sleeps” as a strategy (utilities should provide event-based waits)
- real-world sensitive coordinates (or fixtures that resemble them)
- cross-test global state that can make tests order-dependent
- network calls to external services as a required dependency (unless explicitly mocked and approved)

---

## 🗂️ Recommended Layout

The exact file names may vary, but the intent stays stable.

~~~text
📁 tests/e2e/utils/
├── 📄 README.md                      — This file
│
├── 📁 pages/                         — Page objects (UI navigation + interaction)
│   ├── app.page.ts
│   ├── map.page.ts
│   ├── timeline.page.ts
│   ├── focusmode.page.ts
│   └── storynode.page.ts
│
├── 📁 assertions/                    — High-signal assertions (governance + UX)
│   ├── governance.assert.ts          — masking/redaction/prohibited-output checks
│   ├── a11y.assert.ts                — WCAG/ARIA/keyboard checks
│   └── telemetry.assert.ts           — telemetry-shape checks (local validation)
│
├── selectors.ts                      — Stable selectors (test ids, roles, landmarks)
├── waits.ts                          — Event-based wait helpers (no fixed sleeps)
├── network.ts                        — Request/response helpers, safe stubs/mocks
├── fixtures.ts                       — Fixture loading helpers (synthetic only)
├── telemetry.ts                      — Run manifest + telemetry emit helpers
├── artifacts.ts                      — Trace/screenshot naming + bundling helpers
└── types.ts                          — Shared types for run manifests and helpers
~~~

---

## 🧷 Selector Standards

Selectors are one of the main sources of E2E flakiness. KFM uses selector priority rules.

### Selector priority order
1. **Accessibility-first**: role/label/landmark selectors (preferred for user-visible UI)
2. **Stable test id**: `data-testid` (or `data-kfm-testid`) for complex components
3. **Semantic attributes**: stable `aria-*` where appropriate
4. **Never**: deep CSS chains or brittle DOM traversal

### Rules
- selectors must be centralized (single source of truth in `selectors.ts` or equivalent)
- selectors must be named by intent, not DOM structure
- selectors must not leak sensitive information (no IDs containing coordinates or restricted entity identifiers)

Example selector map pattern:
~~~ts
export const SEL = {
  app: {
    shell: '[data-testid="app-shell"]',
    nav:  '[data-testid="app-nav"]',
  },
  focusMode: {
    panelContext:  '[data-testid="focus-context-panel"]',
    panelTimeline: '[data-testid="focus-timeline-panel"]',
    panelMap:      '[data-testid="focus-map-panel"]',
  },
} as const;
~~~

---

## ⏱️ Wait Standards

### Hard rule
Do not add `sleep(…)` utilities as a “fix”. Use event-based waits.

### Approved wait patterns
- wait for a route transition / URL match
- wait for a specific network response predicate
- wait for a visible/attached element state
- wait for “network idle” where supported (only when paired with an explicit UI signal)

### Unapproved wait patterns
- fixed timeouts
- retry loops without explicit terminal conditions
- “wait for selector” without checking the page is in the intended state

Example wait helper pattern:
~~~ts
export async function waitForReadySignal(page: any) {
  // Example intent: wait for the UI to indicate it is ready,
  // then verify the main container is visible.
  await page.waitForSelector('[data-testid="app-ready"]', { state: "visible" });
  await page.waitForSelector('[data-testid="app-shell"]', { state: "visible" });
}
~~~

---

## 🛡️ Governance-Safe Assertions

Utilities MUST include reusable assertions that protect the platform from policy regressions.

### Required governance assertions
At minimum, utilities should provide functions to assert:

- ✅ masking is applied (H3 generalization / redaction behavior) where required
- ✅ sensitive precision never appears in:
  - tooltips
  - JSON/detail drawers
  - exports/downloads
  - console logs
- ✅ restricted entities are withheld/redacted when governance requires it
- ✅ narrative surfaces remain non-speculative when policy forbids speculation

### Coordinate leakage checks
Provide a “leak scan” helper that can scan:
- rendered DOM text
- exported JSON text
- network payloads captured in test mode

What to scan for (examples):
- raw lat/long patterns
- high-precision decimals
- “geometry dumps” that exceed permitted generalization

Example (simplified) scanner approach:
~~~ts
export function assertNoLatLongLeak(text: string) {
  // Detects patterns like: -97.123456, 38.123456
  const suspicious = /-?\d{1,3}\.\d{5,}/g;
  if (suspicious.test(text)) {
    throw new Error("Potential coordinate precision leak detected in text surface.");
  }
}
~~~

---

## ♿ Accessibility Helpers

E2E utils should include helpers that make WCAG flows repeatable.

### Minimum helper set
- keyboard navigation helpers (tab/shift-tab/enter/escape)
- “landmark present” assertions (nav/main/footer)
- role-based element location helpers
- reduced-motion mode toggles (when supported)
- screen-reader-friendly assertions (labels exist, controls are named)

Example keyboard helper:
~~~ts
export async function pressTab(page: any, times: number) {
  for (let i = 0; i < times; i += 1) {
    await page.keyboard.press("Tab");
  }
}
~~~

---

## 📦 Artifacts and Failure Bundles

Utilities should standardize artifact behavior so CI output is consistent.

### Required artifacts on failure
- screenshot
- trace (where supported)
- network log excerpt (sanitized)
- run manifest pointer

### Recommended artifact location
~~~text
reports/e2e/
├── screenshots/
├── traces/
└── run-manifest.json
~~~

### Sanitization rule
Artifacts must not contain:
- secrets
- PII
- sensitive coordinates
- restricted datasets

If a trace may contain sensitive content, the default behavior is:
- disable or redact the sensitive channels
- or store the trace only for governance-approved CI contexts

---

## 📊 Telemetry Utilities

E2E utilities must support emitting run metadata consistent with the telemetry schema:

- `run_id`, `job_id`, suite tags
- runtime seconds
- failure categories
- optional energy/carbon summaries (if available)
- a11y violation counts (if available)

Write telemetry to:
~~~text
releases/<version>/tests-e2e-telemetry.json
~~~

Run manifest should be written alongside:
~~~text
reports/e2e/run-manifest.json
~~~

---

## 🧪 Utility Quality Gates

All utilities in this folder should be validated by:
- unit tests for pure helpers (regex scanners, formatters, parsers)
- integration checks for page objects/selectors (smoke suite minimum)
- lint rules preventing:
  - sleeps
  - console logging of sensitive payloads
  - direct external network dependencies

---

## 🗺 Diagrams

Mermaid guidance:
- keep node labels ASCII-safe where possible
- avoid emojis inside Mermaid node text
- use quotes around node labels

~~~mermaid
flowchart TD
  A["Test case"] --> B["Page object actions"]
  B --> C["Governance-safe assertions"]
  C --> D["Artifacts and telemetry"]
~~~

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial E2E utilities guide aligned to KFM-MDP v11.2.6 (selectors, waits, governance assertions, artifacts, telemetry). |

---

<div align="center">

[🧭 E2E Guide](../README.md) ·
[🧪 Tests Index](../../README.md) ·
[🧱 Test Architecture](../../ARCHITECTURE.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

