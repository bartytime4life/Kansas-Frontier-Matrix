---
title: "🧾 Kansas Frontier Matrix — Governance Regression Artifacts (E2E Web App) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/artifacts/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Artifacts Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-artifacts"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-artifacts-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:artifacts:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/artifacts/README.md"
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

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/governance/artifacts/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Governance Regression Artifacts (E2E Web App) (v11 LTS)**
`tests/e2e/web-app/regression/governance/artifacts/README.md`

**Purpose**  
Define the **canonical artifact contract** for governance regression E2E suites:
- what artifacts must be produced,
- where they must be written,
- how they must be redacted (no precision leaks),
- and how artifacts map into telemetry + provenance for auditability.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Artifacts-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-Safe%20Artifacts-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Regression](../README.md) ·
[🕵️ Leak Checks](../utils/leak_checks/README.md) ·
[🧭 E2E Guide](../../../../README.md)

</div>

---

## 📘 Overview

Governance regression artifacts are the **audit trail** produced by E2E suites that verify:

- sovereignty masking is enforced,
- restricted states remain restricted,
- no sensitive-precision content leaks through UI surfaces,
- governance badges and routing behavior remain correct,
- telemetry/provenance surfaces remain present and non-empty (IDs/hashes only).

Artifacts MUST be:

- ✅ **deterministic** (stable filenames, stable schemas, stable summaries),
- ✅ **governance-safe** (no raw coordinate-like strings, no geometry dumps, no full payload logs),
- ✅ **machine-readable** (JSON/JUnit where applicable),
- ✅ **human-debuggable** (screenshots/traces where supported, with redaction rules).

Artifacts MUST NOT include:

- real persons, real addresses, or identifying narrative text,
- sensitive or plausible coordinate pairs,
- full network payloads (unless explicitly redacted and policy-approved),
- secrets, tokens, or credentials.

**Artifact philosophy**
- Artifacts exist to explain failures without exposing restricted information.
- Prefer **rule IDs, selectors, request names, and hashes** over raw content.

---

## 🗂️ Directory Layout

This folder contains **artifact templates and contracts** (not the runtime outputs themselves).

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                ├── 📁 artifacts/
                │   ├── 📄 README.md                               — This guide (artifact contract)
                │   ├── 📁 templates/                              — Canonical JSON templates (safe-by-design)
                │   │   ├── 🧾 artifact_manifest.template.json     — Run manifest template (IDs/hashes only)
                │   │   ├── 🧾 governance_summary.template.json    — High-signal governance summary template
                │   │   └── 🧾 leak_check_report.template.json     — Leak-check report template (redacted snippets)
                │   └── 📁 redaction/                              — Optional policy-safe redaction helpers
                │       └── 🧾 redaction_rules.json                — Patterns + safe placeholders (no real examples)
                │
                └── 📁 utils/
                    └── 📁 leak_checks/                             — Generates leak-check artifacts (see README)
~~~

**Runtime output location (canonical)**
- Governance regression suites SHOULD write artifacts under:

~~~text
📁 reports/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 governance/
            ├── 🧾 report.json
            ├── 🧾 junit.xml
            ├── 🧾 artifact-manifest.json
            ├── 🧾 governance-summary.json
            ├── 🧾 leak-check-report.json
            ├── 📁 screenshots/
            ├── 📁 traces/
            └── 📁 videos/
~~~

Notes:
- The `reports/` tree is intentionally outside `tests/` to avoid committing artifacts to source control.
- If your repo uses a different reports root, preserve the same intent and structure.

---

## 🧭 Context

### Artifact categories (what exists and why)

1. **Run manifest**
   - stable identifiers, suite tags, environment hash, artifact paths
2. **Test results**
   - JUnit/XML or JSON summary used by CI and dashboards
3. **Governance summary**
   - high-signal outcomes (CARE tier routing checks, masking checks, restricted-state checks)
4. **Leak-check report**
   - rule IDs, severity counts, locations (selectors/paths), and redacted evidence
5. **Debug artifacts**
   - screenshots/traces/videos (policy-safe; no raw dumps)

### Redaction policy (non-negotiable)

Artifacts MUST be redacted such that they do not contain:

- coordinate-like pairs,
- GeoJSON/WKT fragments,
- high-precision bboxes,
- payload dumps containing restricted fields.

If an artifact type cannot be made safe:
- do not produce it by default,
- replace it with a **hashed summary** and **rule-level evidence**.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Governance E2E suite runs"] --> B["Write run manifest (IDs and hashes)"]
  B --> C["Write test reports (JUnit/JSON)"]
  C --> D["Run leak checks and write redacted report"]
  D --> E["Collect debug artifacts (screenshots/traces)"]
  E --> F["Validate artifact schemas and redaction rules"]
  F --> G["Upload artifacts and emit telemetry summary"]
~~~

Interpretation:
- Artifacts are produced as a gated, policy-safe chain: creation → redaction → validation → upload → telemetry.

---

## 🧠 Story Node & Focus Mode Integration

Governance E2E artifacts often correspond to user-visible narrative surfaces.

Artifacts SHOULD support:
- identifying which surface failed (Story Node page vs Focus Mode panel),
- capturing the minimum safe evidence needed to reproduce and fix,
- ensuring “restricted stays restricted” across navigation and panel switching.

Minimum invariants captured in artifacts:
- route/page identity (safe path, not full query payloads),
- scenario ID and suite tags,
- governance state flags (Tier, masking required, restricted state),
- evidence anchors as IDs/hashes (not raw content).

---

## 🧪 Validation & CI/CD

Artifacts are merge-gating inputs for governance regressions.

### Required artifact checks (recommended)

- ✅ `artifact-manifest.json` exists and is valid JSON
- ✅ `governance-summary.json` exists and includes mandatory keys
- ✅ `leak-check-report.json` exists when `@governance` suites run
- ✅ no secrets / tokens present
- ✅ no coordinate-like patterns present (leak scan on artifacts)
- ✅ schema validation passes (where schemas exist)
- ✅ upload step succeeds (if CI stores artifacts)

### Flake policy for artifacts

- A missing artifact that is required for governance gating is **CI-failing**.
- A redaction failure is **stop-ship** (not retryable by default).
- Debug artifacts may be optional for passing tests, but required for failures.

---

## 📦 Data & Metadata

### Artifact manifest (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "run_id": "e2e_2025-12-13_001",
  "job_id": "<ci_job_id>",
  "suite_tags": ["@regression", "@governance"],
  "scenario_ids": ["governance_masked_required"],
  "env_hash": "<sha256>",
  "artifacts": {
    "junit": "reports/e2e/web-app/governance/junit.xml",
    "report": "reports/e2e/web-app/governance/report.json",
    "governance_summary": "reports/e2e/web-app/governance/governance-summary.json",
    "leak_check_report": "reports/e2e/web-app/governance/leak-check-report.json",
    "screenshots_dir": "reports/e2e/web-app/governance/screenshots/",
    "traces_dir": "reports/e2e/web-app/governance/traces/"
  }
}
~~~

### Governance summary (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "run_id": "e2e_2025-12-13_001",
  "summary": {
    "masking_invariants_pass": true,
    "restricted_state_invariants_pass": true,
    "care_tier_routing_pass": true,
    "raw_precision_leak_detected": false
  },
  "counts": {
    "tests_total": 42,
    "tests_failed": 0,
    "leak_blocks": 0,
    "leak_warns": 0
  }
}
~~~

### Screenshot/tracing guardrail

If screenshots/traces exist, they MUST be treated as potentially sensitive surfaces.

Recommended controls:
- use synthetic fixtures only,
- avoid displaying raw payload inspector panes in screenshots,
- redact/blur any accidental coordinate-like strings if a tool supports it,
- keep traces internal to CI artifact storage (do not commit).

---

## 🌐 STAC, DCAT & PROV Alignment

Artifacts are test outputs (not domain datasets).

- **DCAT**
  - artifacts (report JSON, JUnit, leak-check report) can be represented as `dcat:Distribution` objects
- **STAC**
  - artifacts may be represented as non-spatial STAC items:
    - `geometry: null`
    - `properties.datetime`: run timestamp
    - assets: report, junit, screenshots, traces
- **PROV-O**
  - the E2E run is a `prov:Activity`
  - fixtures/configs/artifact templates are `prov:Entity`
  - CI runner and maintainers are `prov:Agent`

---

## 🧱 Architecture

### Artifact production pipeline (recommended pattern)

1. **Create** (runner writes raw outputs)
2. **Normalize** (ensure stable filenames and directories)
3. **Redact** (apply artifact-safe redaction rules)
4. **Validate** (schema + leak scan on artifacts)
5. **Publish** (upload to CI artifacts store)
6. **Summarize** (emit telemetry counters and hashes only)

### Anti-patterns (avoid)

- printing full network bodies into `report.json`
- embedding raw DOM HTML into artifacts
- storing unredacted traces publicly
- using artifacts as a bypass to governance restrictions

---

## ⚖ FAIR+CARE & Governance

Artifacts are governed outputs.

They MUST uphold:

- **Authority to Control**
  - do not expose sensitive precision through “debug convenience”
- **Responsibility**
  - fail fast when artifact safety rules are violated
- **Ethics**
  - avoid harmful or culturally sensitive phrasing in synthetic fixtures and reports
- **Collective Benefit**
  - produce enough evidence to fix issues without creating new risk

If artifact safety fails:
- block merges for affected governance surfaces,
- remove/rotate unsafe artifacts from storage per policy,
- fix the underlying test or UI behavior (do not weaken rules).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial governance regression artifacts guide aligned to KFM‑MDP v11.2.6 (safe-by-design templates, redaction-first artifacts, CI validation). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

