---
title: "🧾 Kansas Frontier Matrix — E2E Web App Artifact Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/artifacts/templates/README.md"

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
intent: "tests-e2e-web-app-artifact-templates-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-artifact-templates-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:artifacts:templates:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/artifacts/templates/README.md"
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

provenance_chain:
  - "tests/e2e/web-app/artifacts/templates/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — E2E Web App Artifact Templates (v11 LTS)**
`tests/e2e/web-app/artifacts/templates/README.md`

**Purpose**  
Define the canonical artifact templates used by E2E runners for Web App tests: run manifests, artifact indexes, and report skeletons. Templates are **deterministic**, **governance-safe**, and designed for **CI + telemetry** ingestion.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Artifact_Templates-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Artifacts Guide](../README.md) · [🧭 E2E Guide](../../../README.md) · [🖥️ Web App Suites](../../README.md)

</div>

---

## 📘 Overview

This directory contains **templates**, not authoritative run outputs.

Templates exist to:
- keep CI artifacts **consistent across runners**
- standardize fields required by **telemetry aggregation**
- ensure governance safety (no accidental sensitive dumps)
- reduce per-suite “homegrown” formats

Templates MUST remain:
- minimal and stable
- schema-friendly (JSON/JUnit)
- safe to publish (no real data, no tokens, no PII)
- compatible with `tests-e2e-telemetry.json` aggregation

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 artifacts/
            └── 📁 templates/
                ├── 📄 README.md                      — This guide
                │
                ├── 🧾 run-manifest.example.json      — Deterministic run manifest template
                ├── 🧾 artifact-index.example.json    — Enumeration of produced artifacts
                ├── 🧾 report.example.json            — Minimal JSON report skeleton (runner-agnostic)
                ├── 🧾 junit.example.xml              — Minimal JUnit skeleton (CI parsers)
                └── 🧾 redaction-log.example.json      — Optional: redaction events (if log capture exists)
~~~

Policy:
- Templates are examples; real runs MUST write to `reports/e2e/web-app/*`.
- Do not add “helpful” fields that encourage dumping payloads or headers.

---

## 🧭 Context

### When to use templates
Use templates when:
- bootstrapping a new runner
- adding a new suite category that needs consistent reporting
- ensuring a third-party tool output is normalized into KFM canonical shapes

### What templates must never contain
- raw coordinates (even synthetic ones at high precision, unless required and explicitly safe)
- realistic personal names or identifying strings
- copied archival text
- tokens, API keys, secrets
- full API payload examples that could normalize unsafe behavior

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Runner executes suite"] --> B["Creates run manifest"]
  B --> C["Generates report + junit"]
  C --> D["Collects traces/screenshots/videos"]
  D --> E["Writes artifact index"]
  E --> F["Telemetry aggregator reads manifest + report"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Templates MUST support narrative-surface diagnostics without encouraging leakage.

Recommended approach:
- include only synthetic entity IDs (Story Node ID, Focus Mode entity ID)
- record governance state flags (masked/restricted) as booleans
- link to artifacts (trace/screenshot) rather than embedding content

---

## 🧪 Validation & CI/CD

### Template validation rules
Templates SHOULD:
- parse as valid JSON (for `.json`)
- avoid trailing commas and ambiguous nullables
- keep examples short (do not exceed what CI needs)
- remain stable across minor versions unless a schema changes

CI may validate:
- template parse
- required keys present
- forbidden keys absent (e.g., `authorization_header`, `raw_payload_dump`)

---

## 📦 Data & Metadata

### Template: run manifest
A run manifest is the canonical “what ran” record.

Minimum keys (recommended):
- `run_id`
- `suite_tags`
- `browser_matrix`
- `seed`
- `env_hash`
- `fixture_bundle_id`
- artifact paths (report/junit/index)

Example template:
~~~json
{
  "run_id": "e2e_web_<YYYY-MM-DD>_<NNN>",
  "suite_tags": ["@smoke"],
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

### Template: artifact index
An artifact index is an enumerated list of produced artifacts.

Example template:
~~~json
{
  "run_id": "e2e_web_<YYYY-MM-DD>_<NNN>",
  "artifacts": [
    { "type": "junit", "path": "reports/e2e/web-app/junit.xml" },
    { "type": "report", "path": "reports/e2e/web-app/report.json" },
    { "type": "screenshot", "path": "reports/e2e/web-app/screenshots/<suite>/<test-id>.png" },
    { "type": "trace", "path": "reports/e2e/web-app/traces/<suite>/<test-id>.zip" }
  ]
}
~~~

### Template: report JSON
A minimal runner-agnostic JSON report skeleton should include:
- summary (pass/fail)
- failures array (test id + assertion id + artifact pointers)
- governance flags (if relevant)
- a11y counts (if relevant)

Example template:
~~~json
{
  "run_id": "e2e_web_<YYYY-MM-DD>_<NNN>",
  "summary": { "passed": 0, "failed": 0, "skipped": 0 },
  "failures": [],
  "governance": { "sensitive_precision_leak_detected": false },
  "a11y": { "violations": 0 }
}
~~~

### Template: redaction log
Use only if the runner captures logs.

Example template:
~~~json
{
  "run_id": "e2e_web_<YYYY-MM-DD>_<NNN>",
  "redactions": [
    {
      "type": "header",
      "key": "authorization",
      "action": "removed",
      "reason": "secret-scan policy"
    }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O mapping (templates)
Templates help standardize the Entities produced by a `prov:Activity` (the E2E run):
- `run-manifest.json` is a `prov:Entity` describing the activity
- `report.json` and `junit.xml` are `prov:Entity` outputs
- `artifact-index.json` enumerates entity references

Templates SHOULD keep fields stable so provenance mappings do not drift.

---

## 🧱 Architecture

### Compatibility goals
Templates should remain compatible with:
- Playwright or Cypress (runner-specific adapters)
- CI parsers (JUnit)
- telemetry aggregators (JSON)
- governance audits (flags + artifact pointers)

---

## ⚖ FAIR+CARE & Governance

Templates are part of governed documentation. They must not:
- weaken governance expectations
- encourage unsafe logging practices
- embed content that could be misconstrued as real-world

If a template change affects governance gates:
- treat as a governed change
- require review by the relevant working group

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial artifact template guide (run manifest, artifact index, report skeletons) aligned to KFM-MDP v11.2.6. |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

