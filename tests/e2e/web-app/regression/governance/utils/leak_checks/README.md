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
- sensitive-precision leakage (coordinates, geometry, bboxes),
- unsafe debug payload dumps,
- prohibited-output patterns in governed UI surfaces.

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

Leak checks are **guardrail utilities** that scan E2E-visible surfaces to ensure the application never exposes:

- **raw coordinate precision** (lat/long-like pairs, high-precision bboxes),
- **geometry dumps** (GeoJSON/WKT-like fragments) in tooltips, JSON views, or downloads,
- **restricted-state bypass** (UI shows content that should be masked/redacted/blocked),
- **unsafe debug output** (full payload prints, stack traces containing sensitive fragments).

Leak checks are designed to be:

- ✅ **deterministic** (stable rule sets, stable allowlists, stable report format),
- 🛡️ **sovereignty-safe** (focus on preventing precision leakage, not reconstructing it),
- 🧪 **high-signal** (block when risk is meaningful; warn only when explicitly allowed),
- 🧾 **auditable** (reports show rule IDs and locations without dumping full content).

**Non-goals**
- Leak checks are not OCR systems for screenshots.
- Leak checks are not a replacement for governance policy enforcement in the application.
- Leak checks do not validate scientific correctness; they validate **safety invariants**.

---

## 🗂️ Directory Layout

This folder typically contains leak-check rules, scanners, and report writers.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    ├── 📁 fixtures/                              — Utility fixtures (patterns, allowlists, expectations)
                    │   ├── 🧾 leak_patterns.json                  — Pattern catalog (block/warn)
                    │   └── 🧾 leak_allowlist.json                 — Safe placeholder allowlist
                    │
                    └── 📁 leak_checks/
                        ├── 📄 README.md                           — This guide
                        │
                        ├── 📄 leak_check_runner.ts                 — Orchestrates checks for a test step
                        ├── 📄 leak_check_rules.ts                  — Normalized rule set interface
                        ├── 📄 leak_check_scanners.ts               — DOM / console / network scanning helpers
                        ├── 📄 leak_check_report.ts                 — Report model + serialization
                        │
                        └── 📁 __tests__/                           — Unit tests for leak utilities (optional)
                            └── 📄 leak_checks.spec.ts
~~~

Notes:
- Names above represent the **canonical target layout**. Your repo may use different filenames or languages.
- Fixtures are intentionally stored in `../fixtures/` so leak checks can be reused across governance suites.

---

## 🧭 Context

### What leak checks scan (recommended surfaces)
Leak checks SHOULD scan the smallest set of **high-risk, high-signal** surfaces:

- **Rendered UI text** (DOM text content for panels, tooltips, overlays)
- **“Details/JSON” views** (if the UI exposes a structured debug pane)
- **Console logs** (errors/warns printed during E2E runs)
- **Network responses used by the UI** (intercepted responses, only summarized in reports)
- **Download triggers** (filenames, link hrefs, and metadata banners — not full file contents)

### What counts as a “leak”
A leak is any E2E-visible content that violates governance invariants, such as:

- a high-precision coordinate-like pair in UI text,
- a GeoJSON-like `"coordinates"` fragment rendered to the user,
- a bbox presented at raw precision where masking is required,
- restricted text shown in a scenario that should be redacted/blocked.

### Allowlist philosophy (safe by construction)
Allowlists MUST:
- contain only explicit placeholders (e.g., `H3_R8_CELL_ID`, `LAT_REDACTED`),
- never contain realistic coordinate examples,
- be reviewed as carefully as code changes (they change governance posture).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E spec step completes"] --> B["Collect scan targets"]
  B --> C["Load patterns and allowlist"]
  C --> D["Run scanners and rule matching"]
  D --> E["Generate leak check report"]
  E --> F["Block merge if severity is block"]
~~~

Interpretation:
- Leak checks run as an enforcement layer: they produce an auditable report and fail fast on policy-breaking patterns.

---

## 🧠 Story Node & Focus Mode Integration

Leak checks are mandatory for governed narrative surfaces because they are user-visible and easy to regress.

### Story Node surfaces (typical risk points)
Leak checks SHOULD validate:
- no raw coordinates appear in “spacetime” UI,
- masked geometry stays masked across navigation and refresh,
- provenance chips do not expand into full payload dumps.

### Focus Mode surfaces (typical risk points)
Leak checks SHOULD validate:
- map tooltips and context panels never show precision beyond policy,
- “evidence” surfaces show IDs/hashes, not raw sensitive fragments,
- restricted scenarios remain restricted across panel switching.

---

## 🧪 Validation & CI/CD

Leak checks are expected to be:

- **merge-blocking** when they detect severity `block`,
- **reporting** when severity is `warn` (only when explicitly allowed by rules).

Recommended CI behavior:
- run leak checks in `@governance` suites by default,
- emit a structured report to E2E artifacts,
- upload a summary to telemetry (counts by severity and rule ID).

**Flake policy**
- A leak check failure is not retryable by default.
- If a failure is flaky, treat that as a design bug in scanners/waits, not a reason to relax rules.

---

## 📦 Data & Metadata

### Rule model (recommended minimal shape)
Rules SHOULD be normalized into a small consistent interface.

~~~json
{
  "rule_id": "lat_long_pair_high_precision",
  "severity": "block",
  "matcher": {
    "type": "regex",
    "value": "(-?\\d{1,3}\\.\\d{4,})\\s*,\\s*(-?\\d{1,3}\\.\\d{4,})"
  },
  "description": "Detects coordinate-like pairs with high precision.",
  "tags": ["precision", "coordinates", "@governance"]
}
~~~

### Report model (recommended)
Reports MUST avoid dumping raw content. Prefer:
- rule ID,
- target type,
- a small redacted snippet (optional),
- stable location anchors (selector name, URL path, request name).

~~~json
{
  "schema_version": "v11.2.6",
  "run_id": "e2e_2025-12-13_001",
  "scenario_id": "governance_masked_required",
  "results": [
    {
      "rule_id": "geojson_coordinates_key",
      "severity": "block",
      "target": "ui_text",
      "location": {
        "page": "FocusMode",
        "selector": "data-testid=provenance-panel"
      },
      "evidence": {
        "snippet_redacted": "\"coordinates\" …",
        "hash": "<sha256>"
      }
    }
  ],
  "summary": {
    "block": 1,
    "warn": 0,
    "pass": 12
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Leak-check artifacts are test outputs (not real datasets):

- **DCAT**: leak-check reports can be treated as `dcat:Distribution` artifacts (`mediaType: application/json`).
- **STAC**: if represented as a STAC item, use:
  - `geometry: null`
  - `properties.datetime` as the run timestamp
  - assets: `leak-check-report.json`
- **PROV-O**:
  - a leak-check run is a `prov:Activity`,
  - rules/fixtures are `prov:Entity`,
  - CI is a `prov:Agent`.

---

## 🧱 Architecture

### Recommended scanner pipeline
Leak checks SHOULD implement a layered approach:

1. **Normalize inputs**
   - DOM text, console entries, intercepted response summaries
2. **Apply allowlist first**
   - remove known safe placeholders from consideration
3. **Apply block rules**
   - fail fast if block rules match
4. **Apply warn rules**
   - record for review if configured
5. **Write report**
   - stable JSON schema, minimal safe snippets

### Anti-patterns (avoid)
- Logging full network payloads to CI output
- Storing raw UI dumps in artifacts without redaction
- Using “sleep” timing instead of event-based readiness
- Treating allowlists as a general bypass mechanism

---

## ⚖ FAIR+CARE & Governance

Leak checks exist to uphold non-negotiable constraints:

- **Authority to Control**: prevents precision leakage that could enable harmful inference.
- **Responsibility & Ethics**: blocks unsafe outputs even when the app “mostly works.”
- **Collective Benefit**: ensures public-facing surfaces remain safe and respectful.

If leak checks detect a governance failure:
- block merges affecting governed surfaces,
- route review to the appropriate working group and FAIR+CARE Council,
- fix the underlying UI/API behavior (do not weaken rules as a shortcut).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governance leak-check utility guide aligned to KFM‑MDP v11.2.6 (deterministic scanning, safe reporting, merge-blocking on precision leaks). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

