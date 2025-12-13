---
title: "📦 Kansas Frontier Matrix — E2E Web App Artifacts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/artifacts/README.md"

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
intent: "tests-e2e-web-app-artifacts-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-artifacts-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:artifacts:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/artifacts/README.md"
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

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/artifacts/README.md@v11.2.6"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — E2E Web App Artifacts (v11 LTS)**
`tests/e2e/web-app/artifacts/README.md`

**Purpose**  
Define the canonical artifact outputs for Web App E2E test runs (reports, traces, screenshots, videos, manifests), including **governance-safe handling**, **deterministic naming**, and **release/telemetry alignment**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/CI-E2E_Artifacts-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧭 E2E Guide](../../README.md) ·
[🖥️ Web App Suites](../README.md) ·
[♿ Accessibility Suites](../accessibility/README.md) ·
[🧾 Assertions](../../utils/assertions/README.md)

</div>

---

## 📘 Overview

E2E artifacts are the **audit trail** for system-level behavior. They exist to make failures:

- diagnosable (what happened, where, and why)
- reproducible (same suite + seed + env hash)
- governable (no sensitive precision, no PII, no secrets)

Artifacts MUST be:
- **deterministic in structure**
- **safe by default**
- **machine-readable where possible**
- **retained and referenced** in telemetry and provenance logs

Artifacts are produced locally and in CI, but CI output is the authoritative record for governance decisions.

---

## 🗂️ Directory Layout

This folder documents artifact conventions. CI typically writes to `reports/`, while this directory may contain only templates or local-only helper files.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 artifacts/
            ├── 📄 README.md                 — This guide (artifact policy + conventions)
            │
            ├── 🧾 .gitkeep                  — Optional: keep directory present (repo policy dependent)
            │
            └── 📁 templates/                — Optional templates (if used by runner)
                ├── 🧾 run-manifest.example.json
                ├── 🧾 artifact-index.example.json
                └── 🧾 junit.example.xml
~~~

Recommended canonical output locations for actual run artifacts:
~~~text
📁 reports/
└── 📁 e2e/
    └── 📁 web-app/
        ├── 🧾 run-manifest.json
        ├── 🧾 junit.xml
        ├── 🧾 report.json
        ├── 📁 traces/
        ├── 📁 screenshots/
        ├── 📁 videos/
        └── 🧾 artifact-index.json
~~~

---

## 🧭 Context

### Why artifacts are governed
E2E artifacts can accidentally contain:
- sensitive geometry (if UI mistakenly renders precision)
- user-identifying strings (if fixtures are not sanitized)
- secrets (if logs include environment variables)

Therefore:
- artifacts MUST be produced from **synthetic fixtures**
- logs MUST be **redacted** and **minimized**
- failures involving governance safety MUST be treated as stop-ship

### Artifact scope
Artifacts cover:
- what ran (suite tags, browsers)
- what failed (assertion IDs, route/state)
- what was emitted (telemetry references)
- what to inspect (trace/video/screenshot pointers)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E run begins"] --> B["Runner executes suites"]
  B --> C["Artifacts produced (report, junit, traces)"]
  C --> D["Governance-safe checks on artifacts"]
  D --> E["Upload to CI storage + reference from telemetry"]
  E --> F["Audit + triage + fix loop"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Artifacts MUST support investigation of failures in governed narrative surfaces without leaking restricted content.

Minimum artifact expectations for narrative surfaces:
- screenshot on failure
- trace (recommended) capturing UI state transitions
- report entry including:
  - Story Node ID (synthetic)
  - Focus Mode entity ID (synthetic)
  - governance state flags (masked/restricted)

Artifacts MUST NOT include:
- raw coordinate dumps
- full JSON payloads for restricted fixtures
- copied text that resembles real archival excerpts

---

## 🧪 Validation & CI/CD

### Artifact requirements by suite class

| Suite class | Must produce | Recommended |
|---|---|---|
| `@smoke` | `junit.xml`, `report.json`, failure screenshots | traces for failures |
| `@regression` | `junit.xml`, `report.json`, screenshots | traces + videos |
| `@a11y` | `a11y-report.json`, `axe-results.json` (if used) | screenshots of failing regions |
| `@governance` | `report.json` with governance assertions | traces + redaction logs |

### Minimal CI gate (artifact presence)
CI SHOULD fail the job if:
- the run manifest is missing
- reports are missing
- failures occur without screenshots or trace pointers (where supported)

### Flake discipline
Artifacts must make flakes diagnosable:
- include retry count and reason (if retries enabled)
- include deterministic run IDs
- include environment hash

---

## 📦 Data & Metadata

### Naming conventions (deterministic)
All artifact filenames SHOULD avoid timestamps in filenames unless required by tooling. Prefer a stable pattern:

- `run-manifest.json`
- `junit.xml`
- `report.json`
- `artifact-index.json`

Within directories, stable IDs SHOULD be used:

~~~text
reports/e2e/web-app/screenshots/<suite>/<test-id>.png
reports/e2e/web-app/traces/<suite>/<test-id>.zip
reports/e2e/web-app/videos/<suite>/<test-id>.webm
~~~

### Run manifest (required)
A run manifest is the primary machine-readable record. It SHOULD include:

- `run_id`
- `job_id`
- `suite_tags`
- `browser_matrix`
- `seed`
- `env_hash`
- `fixture_bundle_id`
- `artifact_index_ref`

Example:
~~~json
{
  "run_id": "e2e_web_2025-12-13_001",
  "suite_tags": ["@smoke", "@governance"],
  "browser_matrix": ["chromium"],
  "seed": 112233,
  "env_hash": "<sha256>",
  "fixture_bundle_id": "fixtures_webapp_v11.2.6_synthetic",
  "artifacts": {
    "junit": "reports/e2e/web-app/junit.xml",
    "report": "reports/e2e/web-app/report.json",
    "artifact_index": "reports/e2e/web-app/artifact-index.json",
    "screenshots_dir": "reports/e2e/web-app/screenshots/",
    "traces_dir": "reports/e2e/web-app/traces/"
  }
}
~~~

### Artifact index (recommended)
An artifact index provides a single place to enumerate produced artifacts.

Example:
~~~json
{
  "run_id": "e2e_web_2025-12-13_001",
  "artifacts": [
    { "type": "junit", "path": "reports/e2e/web-app/junit.xml" },
    { "type": "report", "path": "reports/e2e/web-app/report.json" },
    { "type": "trace", "path": "reports/e2e/web-app/traces/smoke/storynode_render.zip" },
    { "type": "screenshot", "path": "reports/e2e/web-app/screenshots/smoke/storynode_render.png" }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment
- The E2E run is a `prov:Activity`.
- Reports, traces, screenshots are `prov:Entity`.
- CI workflow and maintainers are `prov:Agent`.

Artifact entities should be hash-addressable (via `doc_integrity_checksum` or report-internal checksums).

### OpenLineage alignment
OpenLineage events for an E2E run SHOULD reference:
- input fixture bundle IDs
- output artifact paths
- governance facets (CARE tier, sovereignty flags)
- telemetry summary pointers

---

## 🧱 Architecture

### Safe-by-default artifact policy
Artifacts must be:
- sanitized (no secrets)
- synthetic (no real individuals, no real sensitive locations)
- minimal (collect what’s needed to debug)
- auditable (reports + manifests)

### Redaction rules
If logs are captured:
- remove headers that could contain tokens
- remove environment variable dumps
- remove full API payload dumps unless fixture-only and explicitly safe

If a redaction rule is triggered, the runner SHOULD emit a note in:
- `report.json`
- optional `redaction-log.json`

---

## ⚖ FAIR+CARE & Governance

Artifacts MUST NOT introduce harm via:
- reproducing restricted knowledge
- encoding culturally harmful text patterns
- exposing sensitive precision
- capturing personal data

Governance failures involving artifact leakage are treated as:
- stop-ship for governed surfaces
- escalation to FAIR+CARE Council and the relevant working group
- mandatory remediation + regression test addition

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governed artifact guide for Web App E2E (deterministic naming, safe defaults, telemetry/provenance alignment). |

<div align="center">

[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

