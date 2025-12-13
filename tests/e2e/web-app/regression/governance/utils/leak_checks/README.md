---
title: "🕵️ Kansas Frontier Matrix — Governance Leak Checks (E2E Utilities) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/leak_checks/README.md"

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
intent: "tests-e2e-web-app-regression-governance-utils-leak-checks"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-utils-leak-checks-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:leak-checks:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/leak_checks/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/leak_checks/README.md@v11.2.6"
---

<div align="center">

# 🕵️ **Governance Leak Checks (E2E Utilities) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/leak_checks/README.md`

**Purpose**  
Define the **canonical leak-check utility layer** used by governance E2E regression suites to detect and block:

- sensitive-precision leakage (coordinate-like precision, bbox-like precision, geometry-like dumps),
- unsafe debug payload dumps in user-visible surfaces,
- restricted-state bypass in governed UI flows.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Precision%20Leak-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Utilities](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

Leak checks are **governance guardrail utilities** executed inside E2E regression runs to ensure the web app never exposes:

- **raw precision** that should be masked/generalized,
- **geometry-like payload dumps** in UI surfaces (panels, tooltips, debug views),
- **restricted content** that should be redacted/blocked,
- **unsafe debug output** that increases disclosure risk.

Leak checks are designed to be:

- ✅ **Deterministic**: stable rule IDs, stable severity semantics, stable report schema.
- 🛡️ **Sovereignty-safe**: focused on preventing disclosure, not reconstructing hidden content.
- 🧪 **High-signal**: “block” only when risk is meaningful; “warn” is opt-in and explicit.
- 🧾 **Auditable**: reports include rule IDs and locations without dumping full content.

### What leak checks are (KFM definition)

A leak check is a scan over **E2E-visible surfaces** (or E2E-captured summaries of surfaces) that produces:

- a structured report (`json`),
- a pass/fail decision used for CI gating,
- minimal snapshots for debugging (redacted by design).

### Non-goals

- Leak checks are not OCR systems for screenshots.
- Leak checks are not a replacement for application-side masking / policy enforcement.
- Leak checks do not validate scientific correctness; they validate **safety invariants**.

---

## 🗂️ Directory Layout

This utility is organized to support:

- reuse across governance suites,
- deterministic fixtures and allowlists,
- unit testing for the scanners and rule engine.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    ├── 📄 README.md                                       — Utilities index (shared helpers)
                    │
                    ├── 📁 fixtures/                                       — Shared utility fixtures (safe, synthetic)
                    │   ├── 📄 README.md
                    │   ├── 🧾 leak_patterns.json                           — Pattern catalog (rule definitions)
                    │   └── 🧾 leak_allowlist.json                          — Allowlisted placeholders (safe by design)
                    │
                    └── 📁 leak_checks/                                    — Leak check utilities (this folder)
                        ├── 📄 README.md                                    — This guide
                        │
                        ├── 📄 leak_check_runner.ts                          — Orchestrates a leak check pass
                        ├── 📄 leak_check_rules.ts                           — Rule normalization + registry
                        ├── 📄 leak_check_scanners.ts                        — DOM/console/network scan helpers
                        ├── 📄 leak_check_report.ts                          — Report model + serialization
                        │
                        ├── 📁 fixtures/                                    — Leak-check specific fixtures
                        │   ├── 📄 README.md
                        │   ├── 🧾 fixture_registry.json                     — Fixture ID → case path mapping
                        │   ├── 📁 bundles/                                  — Suite manifests (grouped cases)
                        │   │   └── 📄 README.md
                        │   └── 📁 cases/                                    — Atomic case fixtures (single-signal)
                        │       └── 📄 README.md
                        │
                        └── 📁 __tests__/                                    — Unit tests (optional)
                            ├── 📄 README.md
                            └── 📁 snapshots/                                — Snapshot expectations (redacted)
                                └── 📄 README.md
~~~

---

## 🧭 Context

### What leak checks scan (recommended surfaces)

Leak checks SHOULD scan the smallest set of **high-risk, high-signal** surfaces:

- **Rendered UI text** (panel body text, tooltips, banners, chips)
- **UI “detail” views** (if the UI exposes JSON/metadata panes)
- **Console output** captured during E2E (errors/warnings)
- **Network response summaries** captured by the runner (do not store raw payloads)
- **Download triggers** (names, metadata banners, “safe preview” text)

Leak checks SHOULD NOT:

- store or print raw API payloads to CI logs,
- record full DOM dumps in artifacts without redaction,
- inspect screenshots via OCR as the primary mechanism.

### What counts as a “leak”

A leak is any E2E-visible output that violates governance invariants, including:

- coordinate-like precision appearing in UI text (where masking is required),
- bbox-like precision appearing in tooltips, debug panes, or downloads,
- geometry-like fragments rendered in user-visible surfaces,
- restricted-state UI showing content that should be redacted/blocked.

### Severity model (recommended)

Leak checks SHOULD standardize severity:

- `block` — CI must fail (merge-blocking)
- `warn` — CI may pass only when explicitly configured to allow warnings
- `info` — record-only, never blocks

Rule IDs MUST be stable so governance dashboards can trend:

- counts by rule ID,
- regressions introduced by change sets,
- repeat offenders in specific surfaces.

### Allowlist philosophy (safe by construction)

Allowlists MUST:

- include only explicit placeholders (e.g., `H3_R8_CELL_ID`, `COORDINATE_REDACTED`),
- avoid anything that resembles realistic coordinate formats,
- be reviewed as carefully as code changes (they alter enforcement posture).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E step completes"] --> B["Collect scan targets"]
  B --> C["Load patterns and allowlist"]
  C --> D["Scan and match rules"]
  D --> E["Write structured report"]
  E --> F["Block merge if any block severity"]
~~~

Interpretation:
- Leak checks are an enforcement layer: they run deterministically, produce an auditable report, and fail fast on high-risk patterns.

---

## 🧠 Story Node & Focus Mode Integration

Leak checks are mandatory for **governed narrative surfaces** because they are user-visible and easy to regress.

### Story Node surfaces (typical risk points)

Leak checks SHOULD validate:

- no raw precision appears in spacetime/map UI,
- masked geometry stays masked across navigation and refresh,
- provenance chips do not expand into full payload dumps.

### Focus Mode surfaces (typical risk points)

Leak checks SHOULD validate:

- tooltips and panels do not show precision beyond policy,
- evidence/provenance surfaces show IDs/hashes, not raw sensitive fragments,
- restricted scenarios remain restricted across:
  - panel switching,
  - route transitions,
  - “copy/share/export” interactions.

---

## 🧪 Validation & CI/CD

Leak checks are **merge-blocking** when they detect any `block` severity result.

### Recommended CI behavior

- run leak checks for `@governance` suites by default,
- emit a structured report into E2E artifacts,
- contribute summary counts to telemetry (per run).

### Required artifacts (recommended)

Leak checks SHOULD write:

~~~text
📁 reports/
└── 📁 e2e/
    ├── 🧾 leak-check-report.json                 — Structured results (no raw dumps)
    ├── 🧾 leak-check-summary.json                — Totals by severity and rule ID
    └── 📁 leak-check-snapshots/                  — Minimal redacted snippets (optional)
~~~

### Flake policy

- A leak check failure is **not retryable by default**.
- If a leak check failure is flaky, treat it as a scanner/readiness design bug:
  - fix selectors,
  - use event-based waits,
  - tighten deterministic capture steps.

Do not relax governance rules to “fix” flakiness.

---

## 📦 Data & Metadata

### Rule model (recommended minimal shape)

Rules SHOULD normalize to a small interface.

~~~json
{
  "rule_id": "coordinate_like_precision_pair",
  "severity": "block",
  "matcher": {
    "type": "regex",
    "value": "<regex-redacted-in-docs>"
  },
  "description": "Detects coordinate-like precision patterns in user-visible surfaces.",
  "targets": ["ui_text", "console", "network_summary", "download_banner"],
  "tags": ["precision", "coordinates", "@governance"]
}
~~~

Notes:
- The exact regex strings may live in `../fixtures/leak_patterns.json`.
- This guide avoids embedding realistic coordinate-like examples in documentation.

### Report model (recommended)

Reports MUST avoid dumping raw content. Prefer:

- rule ID,
- severity,
- target type,
- stable location anchors (page + selector + request name),
- optional redacted snippet or hash.

~~~json
{
  "schema_version": "v11.2.6",
  "run_id": "e2e_<timestamp>_<seq>",
  "scenario_id": "<scenario_id>",
  "results": [
    {
      "rule_id": "geometry_like_dump_key",
      "severity": "block",
      "target": "ui_text",
      "location": {
        "page": "FocusMode",
        "selector": "data-testid=<selector>"
      },
      "evidence": {
        "snippet_redacted": "<redacted>",
        "hash": "<sha256>"
      }
    }
  ],
  "summary": {
    "block": 1,
    "warn": 0,
    "info": 0,
    "pass": 12
  }
}
~~~

### Fixtures and case-driven validation

Leak checks SHOULD be validated against fixture cases:

- atomic cases under `fixtures/cases/`,
- bundles under `fixtures/bundles/`,
- fixture registry under `fixtures/fixture_registry.json`.

This ensures:
- detectors have positive controls (they fire),
- detectors have negative controls (they do not over-trigger).

---

## 🌐 STAC, DCAT & PROV Alignment

Leak-check artifacts are test outputs (not real datasets):

- **DCAT**: leak-check reports may be treated as `dcat:Distribution` artifacts (`mediaType: application/json`).
- **STAC**: if represented as a STAC item, use:
  - `geometry: null`
  - `properties.datetime` set to run timestamp
  - assets: report + summary
- **PROV-O**:
  - a leak-check run is a `prov:Activity`,
  - rules/fixtures are `prov:Entity`,
  - CI runner and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended scanner pipeline

Leak checks SHOULD implement a layered approach:

1. **Normalize inputs**
   - DOM text extraction
   - console entries
   - network response summaries (safe-minimized)
   - download banner metadata
2. **Apply allowlist**
   - strip known safe placeholders
3. **Apply `block` rules**
   - fail fast if any match
4. **Apply `warn/info` rules**
   - record per configuration
5. **Write report**
   - stable JSON schema, minimal evidence

### Anti-patterns (avoid)

- printing full payloads into CI output,
- storing raw DOM dumps as artifacts,
- treating allowlists as a bypass mechanism,
- “sleep-based” timing instead of event-based readiness.

---

## ⚖ FAIR+CARE & Governance

Leak checks uphold non-negotiable constraints:

- **Authority to Control**: prevents precision leakage that could enable harmful inference.
- **Responsibility & Ethics**: blocks unsafe outputs even when the app “mostly works.”
- **Collective Benefit**: keeps public-facing surfaces safe and respectful.

### Governance routing

If leak checks detect a governance failure:

- block merges affecting governed outputs,
- route to the relevant working group and FAIR+CARE Council,
- fix underlying UI/API behavior (do not weaken rules as a shortcut).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governance leak-check utility guide aligned to KFM‑MDP v11.2.6 (deterministic scanning, safe reporting, merge-blocking on precision leaks). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
