---
title: "🧭 Kansas Frontier Matrix — Navigation Utilities (Governance Regression E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/navigation/README.md"

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
intent: "tests-e2e-web-app-regression-governance-utils-navigation"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-utils-navigation-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:navigation:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/navigation/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/navigation/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Navigation Utilities (Governance Regression E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/navigation/README.md`

**Purpose**  
Define the **canonical navigation helpers** used by governance regression E2E suites to move through the web app **deterministically** and **policy-safely**, including:

- stable route builders (no hardcoded magic strings scattered across specs),
- navigation guards (event-based readiness over sleeps),
- governance-safe deep links (no unsafe “dump view” shortcuts),
- consistent artifact anchors (URLs/paths recorded without leaking content).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Focus-Deterministic%20Navigation-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Utilities](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

Navigation utilities exist to keep governance E2E suites:

- ✅ **Deterministic**: stable URLs, stable waits, stable “ready” conditions.
- ✅ **Readable**: “what the test does” is obvious; route mechanics are shared.
- ✅ **Safe**: navigation helpers must not introduce policy bypasses (e.g., hidden debug routes that reveal raw precision).
- ✅ **Maintainable**: when routes change, one update fixes many specs.

### What belongs in this folder

Navigation utilities SHOULD include:

- route builders and typed route parameters,
- navigation wrappers around the test runner (Playwright/Cypress),
- “ready” guards that wait for stable UI state (not time),
- standard patterns for query strings used in governance scenarios.

Navigation utilities SHOULD NOT include:

- large page-object implementations (those belong in `tests/e2e/utils/pages/` or equivalent),
- fixture payloads (those belong in `fixtures/`),
- governance leak rules (those belong in `leak_checks/`).

---

## 🗂️ Directory Layout

This folder is intentionally small and stable.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    ├── 📁 navigation/
                    │   ├── 📄 README.md                              — This guide
                    │   ├── 📄 routes.ts                               — Route builders + canonical paths
                    │   ├── 📄 navigate.ts                             — Wrapper helpers around runner navigation
                    │   ├── 📄 guards.ts                               — Deterministic “ready” guards (event/state based)
                    │   ├── 📄 query_params.ts                         — Canonical query string helpers (stable ordering)
                    │   └── 📄 url_safety.ts                            — URL allow/deny rules (no unsafe debug routes)
                    │
                    ├── 📁 leak_checks/                                — Precision and payload leak detection utilities
                    └── 📁 fixtures/                                   — Shared utility fixtures (allowlists/patterns)
~~~

---

## 🧭 Context

### Determinism rules (navigation must not be flaky)

Navigation helpers MUST:

- avoid arbitrary sleeps,
- prefer event-based readiness checks:
  - “page loaded”
  - “network idle” (if supported)
  - “selector visible”
  - “panel ready state true”
- standardize query param ordering (so URLs and snapshots are stable),
- avoid reliance on machine-local time (inject deterministic time when required).

### Governance rules (navigation must not bypass policy)

Navigation helpers MUST:

- avoid “debug routes” that expose raw payloads to the UI,
- avoid query parameters that expand restricted information,
- ensure restricted-state routes remain restricted (no “force show” toggles),
- record only safe URL artifacts (no embedding sensitive fragments in query strings).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Spec selects a governance scenario"] --> B["Build route (routes.ts)"]
  B --> C["Navigate (navigate.ts)"]
  C --> D["Wait for ready (guards.ts)"]
  D --> E["Run assertions"]
  E --> F["Write artifacts (safe URLs only)"]
~~~

Interpretation:
- Governance suites should be able to switch scenarios by changing **only** the scenario ID and route builder parameters, while navigation mechanics remain stable and centralized.

---

## 🧠 Story Node & Focus Mode Integration

Governance regression suites often traverse narrative surfaces:

- Story Node routes (narrative + provenance chips),
- Focus Mode routes (Context/Timeline/Map panels),
- governance overlays (CARE tier indicators, sovereignty flags).

Navigation utilities SHOULD support these flows without encoding product-specific assumptions into every spec.

### Recommended navigation invariants

- A route helper returns a URL that is:
  - stable,
  - deterministic,
  - safe (no prohibited query params).
- A guard helper blocks until:
  - the expected surface is “ready,”
  - the governance state is visible when required (e.g., CARE badge present).

---

## 🧪 Validation & CI/CD

Navigation helpers SHOULD be validated by:

- unit tests (pure route builders and query normalization),
- E2E smoke coverage (a minimal “can navigate + ready” check),
- linting rules that prevent:
  - unused routes,
  - unsafe allowlist expansions,
  - non-deterministic query param ordering.

Recommended CI placement:
- navigation unit tests run with unit suite,
- navigation readiness validated in `@governance` or `@smoke` suites (fast).

---

## 📦 Data & Metadata

### Canonical route builder pattern (example)

Use centralized builders so URL changes are localized.

~~~ts
// Example shape only: adapt names to repo conventions.
export const routes = {
  governance: {
    overview: () => "/governance",
    audit: (runId: string) => `/governance/audit/${encodeURIComponent(runId)}`,
  },
};
~~~

### Canonical query param normalization (example)

Ensure stable query ordering for snapshots and reports.

~~~ts
// Example shape only: keep sorting stable.
export function toStableQuery(params: Record<string, string | number | boolean>): string {
  const entries = Object.entries(params)
    .map(([k, v]) => [k, String(v)] as const)
    .sort(([a], [b]) => a.localeCompare(b));

  const usp = new URLSearchParams();
  for (const [k, v] of entries) usp.set(k, v);
  const qs = usp.toString();
  return qs ? `?${qs}` : "";
}
~~~

### URL safety checks (example)

Block unsafe routes/params at the utility layer.

~~~ts
// Example shape only: avoid embedding policy bypasses.
export function assertUrlSafe(url: string): void {
  const deny = ["debug", "raw", "dump"];
  for (const token of deny) {
    if (url.includes(token)) throw new Error(`Unsafe URL token detected: ${token}`);
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Navigation utilities are **documentation + code-adjacent test tooling**:

- **DCAT**: this guide is documentation (`text/markdown`).
- **STAC**: not applicable as spatial data; any STAC representation should use `geometry: null`.
- **PROV-O**:
  - a navigation action in an E2E run is part of a `prov:Activity` (the test run),
  - the route registry is a `prov:Entity`,
  - CI runner is a `prov:Agent`.

---

## 🧱 Architecture

### Design pattern (recommended)

- `routes.ts` is “pure” (no runner coupling).
- `navigate.ts` is runner-coupled (Playwright/Cypress wrapper).
- `guards.ts` is readiness logic (selectors/events, no sleeps).
- `url_safety.ts` is governance enforcement at the navigation boundary.

This separation helps governance suites avoid:
- scattered route strings,
- inconsistent waits,
- accidental policy bypass via query params.

---

## ⚖ FAIR+CARE & Governance

Navigation is part of governance posture because it can:

- unintentionally expose restricted debug views,
- create URLs that encode sensitive fragments,
- bypass masked states by toggling query flags.

Therefore:

- URL safety checks are treated as governance controls.
- Any attempt to add unsafe deep links must be reviewed with the governance policy in mind.
- “Convenience routes” that reveal raw payloads are prohibited in governed E2E suites.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial navigation utilities guide aligned to KFM‑MDP v11.2.6 (deterministic routing, readiness guards, URL safety constraints). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

