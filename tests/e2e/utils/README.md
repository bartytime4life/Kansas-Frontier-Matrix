---
title: "🧰 Kansas Frontier Matrix — E2E Utilities (Deterministic Helpers) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/utils/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-utils-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

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
jurisdiction: "Kansas / United States"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tests-e2e-v11.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

provenance_chain:
  - "tests/e2e/utils/README.md@v11.2.6"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — E2E Utilities (Deterministic Helpers) (v11 LTS)**
`tests/e2e/utils/README.md`

**Purpose**  
Define the canonical utilities used by KFM E2E tests: stable selectors, deterministic waits, governance-safe assertions, artifact capture, and telemetry hooks.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧭 E2E Guide](../README.md) ·
[🧪 Tests Index](../../README.md) ·
[🧱 Test Architecture](../../ARCHITECTURE.md) ·
[🧱 Fixtures](../../fixtures/README.md)

</div>

---

## 📘 Overview

E2E utilities exist to make test behavior:

- deterministic (no sleep-based flake fixes)
- governance-safe (no sensitive precision leaks, no policy bypass)
- accessibility-aware (role-first selectors, keyboard-first helpers)
- artifact-rich (screenshots/traces/run manifests on failure)
- telemetry-aligned (run metadata emitted in a predictable schema)

### What belongs in `tests/e2e/utils/`
- page objects / screen models
- selector registry (role + `data-testid`)
- wait helpers (event-based)
- governance-safe assertions (masking/redaction/prohibited output)
- artifact helpers (trace/screenshot naming and bundling)
- run manifest + telemetry helpers

### What does not belong here
- secrets, credentials, production tokens, private endpoints
- real-world sensitive coordinates or plausible sensitive geometry
- cross-test global state that causes ordering dependency
- fixed sleeps as a primary strategy

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    ├── 📄 README.md                                 — E2E suite rules and runbook
    ├── 📁 utils/                                    — 🧰 Deterministic helpers (this folder)
    │   ├── 📄 README.md                              — This guide
    │   ├── 📁 pages/                                 — Page objects / screen models
    │   │   ├── 📄 app.page.ts                        — App shell helpers
    │   │   ├── 📄 map.page.ts                        — Map panel helpers
    │   │   ├── 📄 timeline.page.ts                   — Timeline helpers
    │   │   ├── 📄 focusmode.page.ts                  — Focus Mode panel helpers
    │   │   └── 📄 storynode.page.ts                  — Story Node view helpers
    │   │
    │   ├── 📁 assertions/                            — High-signal assertions (policy + UX)
    │   │   ├── 📄 governance.assert.ts               — Masking/redaction/prohibited output checks
    │   │   ├── 📄 a11y.assert.ts                     — WCAG helpers and assertions
    │   │   └── 📄 telemetry.assert.ts                — Telemetry shape checks
    │   │
    │   ├── 📄 selectors.ts                           — Stable selector registry (roles + test ids)
    │   ├── 📄 waits.ts                               — Event-based wait helpers (no fixed sleeps)
    │   ├── 📄 artifacts.ts                           — Trace/screenshot naming + failure bundles
    │   ├── 📄 telemetry.ts                           — Run manifest helpers + telemetry emit hooks
    │   ├── 📄 fixtures.ts                            — Synthetic fixture loader helpers
    │   └── 📄 types.ts                               — Shared types (run manifests, selectors, tags)
    │
    └── 📁 resources/                                 — E2E-only synthetic fixtures (non-sensitive)
~~~

---

## 🧭 Context

### Selector standards (priority order)
1. accessibility-first selectors (roles, labels, landmarks)
2. stable test ids (`data-testid` or `data-kfm-testid`)
3. stable semantic attributes (ARIA attributes where appropriate)

Never rely on:
- deep CSS chains
- brittle DOM traversal
- internal classnames generated by build tools

### Wait standards (no “sleep fixes”)
Utilities must provide event-based waits:
- route change and URL match
- selector visible/attached with explicit state
- expected network response predicate (when allowed)
- “ready signal” in UI (preferred)

---

## 🧱 Architecture

### Utility design contract
Each utility must be:
- pure or idempotent (safe to call repeatedly)
- environment-agnostic (CI/local parity)
- explicit about side effects (navigation, network intercepts)
- safe under sovereignty and ethics constraints

### Page object contract (recommended)
Each page object should expose:
- `goto()` or `open()` (optional, if navigation is part of that page)
- `assertReady()` (canonical “page loaded and stable” signal)
- interaction helpers (click/toggle/enter text)
- stable selectors via the central selector registry

---

## 📦 Data & Metadata

### Required artifacts for failures
On failure, utilities must support consistent capture:
- screenshot
- trace (where supported)
- sanitized network log excerpt (optional; must not include secrets)
- run manifest pointer

Recommended artifact layout:
~~~text
reports/
└── e2e/
    ├── report.json
    ├── junit.xml
    ├── run-manifest.json
    ├── screenshots/
    └── traces/
~~~

### Run manifest (minimum recommended fields)
~~~json
{
  "run_id": "e2e_YYYY-MM-DD_###",
  "suite_tags": ["@smoke"],
  "browser_matrix": ["chromium"],
  "seed": 112233,
  "env_hash": "<sha256>",
  "artifacts": {
    "report": "reports/e2e/report.json",
    "junit": "reports/e2e/junit.xml",
    "traces_dir": "reports/e2e/traces/",
    "screenshots_dir": "reports/e2e/screenshots/"
  }
}
~~~

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Test case"] --> B["Page object actions"]
  B --> C["Deterministic waits"]
  C --> D["Governance safe assertions"]
  D --> E["Artifacts and run manifest"]
  E --> F["Telemetry hook"]
~~~

---

## 🧪 Validation & CI/CD

### Utility quality gates (normative)
Utilities should be validated by:
- unit tests for pure helpers (regex scanners, formatting helpers)
- integration smoke coverage for page objects/selectors
- lint rules preventing:
  - fixed sleeps
  - unsafe logging of payloads
  - dependency on external networks

### Flake control rules
- flaky helpers are quarantined and removed from `@smoke` paths
- retries must be explicit and tracked (issue reference required)
- governance failures are not retryable by default

---

## 🌐 STAC, DCAT & PROV Alignment

### Provenance expectations for E2E
E2E utilities should enable recording references to:
- run identifiers (job/run)
- fixture pack identifiers (synthetic only)
- artifact paths and checksums (where implemented)

This document does not require emitting STAC/DCAT records, but it must not impede
pipeline-level provenance and telemetry validations.

---

## 🧠 Story Node & Focus Mode Integration

E2E utilities must support narrative-surface testing:
- Story Node v3 rendering checks (provenance chips present)
- Focus Mode panel checks (Context/Timeline/Map consistent)
- prohibited output checks for narrative-capable surfaces (no speculation, no sensitive disclosure)

Utilities must also support:
- coordinate precision leak scans on UI-visible strings and exported JSON surfaces
- “restricted state” assertions (redacted/masked/blocked behaviors)

---

## ⚖ FAIR+CARE & Governance

### Sovereignty-safe assertions (required)
Utilities must provide:
- coordinate precision leak detection (DOM text + exports)
- masking/generalization assertions (H3-safe behavior)
- restricted material handling assertions (withheld/redacted/blocked)

### Accessibility posture
Utilities must enable:
- keyboard-only path helpers
- role-based selectors
- landmark/heading order checks
- reduced-motion mode checks where supported

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial E2E utilities guide aligned to KFM-MDP v11.2.6 (approved H2 set, deterministic helpers, governance-safe assertions, artifact + telemetry hooks). |

<div align="center">

[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
