---
title: "🧪 KFM v11.2.2 — Pytest Runner Composite Action"
path: ".github/actions/pytest-runner/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Infrastructure & Provenance Committee"
content_stability: "stable"
backward_compatibility: "Aligned with v10.x → v11.x CI/CD model"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.2/signature.sig"
telemetry_ref: "../../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/actions-library-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Guide"
intent: "github-composite-actions"
role: "ci-cd-infrastructure"
category: "CI/CD · Automation · Governance · Reusability"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
fair_category: "F1-A1-I1-R1"

data_steward: "KFM Infrastructure & Provenance Committee"

provenance_chain:
  - ".github/actions/pytest-runner/README.md@v11.2.2"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 (CI/CD events)"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/actions-pytest-runner-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/actions-pytest-runner-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions-pytest-runner:v11.2.2"
semantic_document_id: "kfm-doc-github-actions-pytest-runner"
event_source_id: "ledger:.github/actions/pytest-runner/README.md"

immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧪 Test Execution & CI/CD"
    - "📊 Coverage & Telemetry"
    - "📦 Data & Metadata Contract"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev · staging · production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "CI-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Pipelines × Responsible Automation"
  pipeline: "Deterministic CI/CD · Explainable Workflows · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Automation Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: false
requires_governance_links_in_footer: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

deprecated_fields:
  - "old_pytest_runner_action_readme_v10.4"
---

<div align="center">

# 🧪 **KFM v11 — Pytest Runner Composite Action**  
`.github/actions/pytest-runner/README.md`

**Purpose**  
Provide a **governed, deterministic composite GitHub Action** for running **pytest** across KFM modules  
(`src/pipelines`, `src/graph`, `src/api`, `src/web`, `docs` where applicable) with **standardized options**,  
**coverage & xfail policy**, and **telemetry + provenance** suitable for CI dashboards and OpenLineage.

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../../docs/standards/kfm_markdown_protocol_v11.2.2.md)
· [![CI/CD Profile](https://img.shields.io/badge/CI%2FCD-KFM--PDC_v11-navy)]()
· [![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

The **`pytest-runner` composite action** is the canonical way to execute **Python test suites** in the  
Kansas Frontier Matrix monorepo:

- Normalizes **pytest invocation** across workflows and services.  
- Enforces **minimum coverage thresholds** and **xfail policies**.  
- Produces **JUnit** & **coverage** artifacts for CI, code review, and long‑term QA.  
- Emits **telemetry** and **OpenLineage events** for test runs (pass/fail, duration, coverage).  
- Ensures tests run in a **deterministic, pinned environment** aligned with KFM reproducibility standards.

Use this action instead of ad‑hoc `pytest` steps to:

- Avoid duplicate configuration across workflows.  
- Centralize KFM‑specific behaviours (e.g., xfail leakage detection, coverage minima).  
- Maintain a single governed contract for “what a test run means” across the platform.

---

## 🧪 Test Execution & CI/CD

This composite action is **contract‑driven**: workflows MAY extend around it, but MUST treat its inputs/outputs  
as the authoritative interface for Python tests in CI.

### 1. Typical Usage

In `.github/workflows/kfm-ci.yml`:

```yaml
- name: 🧪 Run pytest (core)
  uses: ./.github/actions/pytest-runner
  with:
    python_version: "3.11"
    working_directory: "."
    test_paths: |
      tests/
    cov_paths: |
      src/
    min_coverage: 85
    xfail_policy: "no-new-xfails"
    junit_report_path: artifacts/pytest/junit-core.xml
    coverage_xml_path: artifacts/pytest/coverage-core.xml
```

Examples:

- **Core pipeline & graph tests**  
  - `test_paths: tests/pipelines tests/graph`  
  - `cov_paths: src/pipelines src/graph`

- **API & web**  
  - `test_paths: tests/api tests/web`  
  - `cov_paths: src/api src/web`

### 2. Normative Execution Stages

The composite action MUST, at minimum, perform these stages in order:

1. **Environment setup**  
   - Select `python_version` via `actions/setup-python@<pinned_sha>`.  
   - Configure deterministic pip cache (cache key tied to `lockfile`, `python_version`, and `cache_key_suffix`).  
   - Install dependencies using **pinned** constraints:
     - Prefer `requirements.txt`/`requirements-dev.txt` or `poetry.lock`/`pip-tools` lock.  
     - Fail if no deterministic dependency definition is found (unless `allow_unlocked_deps: true` is explicitly set in the future).

2. **Test selection**  
   - Resolve `test_paths` relative to `working_directory`.  
   - If no tests are found, treat as **configuration error**, not success.

3. **Pytest invocation**  
   - Run `pytest` with:
     - Configurable `pytest_args` (appended to defaults).  
     - Coverage options when `cov_paths` is non‑empty.  
     - Standard KFM flags (e.g., `-ra`, `--maxfail=1` by default, unless overridden).  
   - Ensure exit code is captured and combined with subsequent policy checks.

4. **Coverage enforcement**  
   - If `cov_paths` is specified:
     - Generate coverage XML (and optionally HTML) using `coverage.py` or `pytest-cov`.  
     - Parse coverage result to compute overall coverage (line or branch, as configured).  
     - If coverage < `min_coverage`, treat as **error** regardless of pytest exit code.

5. **Xfail policy enforcement**  
   - If `xfail_policy` is defined:
     - Parse pytest summary / JUnit results.  
     - Detect:
       - New xfails (tests newly marked xfail, relative to baseline).  
       - Xfails that unexpectedly pass (xfail leakage).  
     - For `xfail_policy: "no-new-xfails"`:
       - New xfails MUST be treated as errors.  
     - For `xfail_policy: "no-xfail-leaks"`:
       - Xpasses (xfail but passed) MUST be treated as errors.

6. **Artifact generation**  
   - Always produce:
     - JUnit XML (`junit_report_path`) for CI and code review.  
     - Coverage XML when `cov_paths` is set (`coverage_xml_path`).  
   - Optionally produce HTML coverage reports (if `coverage_html_dir` is non‑empty).

7. **Telemetry & provenance**  
   - Generate a machine‑readable **test run telemetry** JSON:
     - Start/end timestamps, duration.  
     - Python & pytest versions.  
     - Test counts (passed/failed/xfail/xpass/skipped/error).  
     - Coverage values and thresholds.  
   - Emit an OpenLineage/PROV event:
     - Model test run as a `prov:Activity` that **uses** the repository sources and **generates** JUnit & coverage reports.  
     - Attach `event_source_id`, `commit_sha`, and `workflow` identifiers.

8. **Exit semantics**  
   - Base exit code = pytest exit code.  
   - Elevate to failure if:
     - Coverage < `min_coverage`, OR  
     - Xfail policy violated, OR  
     - Telemetry/report generation fails.  
   - Set composite `status` accordingly (`passed`/`failed`).

All third‑party GitHub Actions and test tooling MUST be pinned to `@<commit_sha>` or equivalent digests in `action.yml`.

---

## 📊 Coverage & Telemetry

### Coverage Semantics

The `pytest-runner` composite action provides a **standard definition of coverage** for KFM:

- Default **mode**: line coverage via `coverage.py` or `pytest-cov`.  
- Default **scope**: union of all paths listed in `cov_paths`.  
- Exclusions:
  - Tests themselves (`tests/`),  
  - Auto‑generated code,  
  - Migrations or pure configuration files may be excluded via `.coveragerc` (checked into the repo).

Key behaviours:

- `min_coverage` is a hard threshold for CI (for the paths under test).  
- For multi‑module runs, coverage MAY be calculated per module and aggregated; this should be reflected in the telemetry.  
- For gradual enforcement, `min_coverage` can be increased over time while CI blocks on regressions.

### Telemetry Contract

The action SHOULD emit a JSON report (path controlled by `telemetry_path`) with at least:

```jsonc
{
  "schema_version": "kfm-pytest-telemetry-v1",
  "run": {
    "started_at": "2025-11-28T12:34:56Z",
    "finished_at": "2025-11-28T12:35:23Z",
    "duration_seconds": 27.1,
    "workflow": "kfm-ci.yml",
    "job_name": "pytest-core",
    "commit_sha": "<commit>"
  },
  "environment": {
    "python_version": "3.11.7",
    "pytest_version": "7.4.0"
  },
  "tests": {
    "total": 420,
    "passed": 410,
    "failed": 2,
    "skipped": 5,
    "xfail": 3,
    "xpass": 0,
    "error": 0
  },
  "coverage": {
    "enabled": true,
    "mode": "line",
    "overall_percent": 87.3,
    "threshold": 85.0
  },
  "policies": {
    "xfail_policy": "no-new-xfails",
    "min_coverage_enforced": true
  }
}
```

Exact schema is defined in `telemetry_schema` and MUST remain backward‑compatible within v11 patch releases.

Telemetry MUST NOT contain:

- Raw source code,  
- Full test names for sensitive/private suites (unless governance allows),  
- Secrets, tokens, or environment values.

---

## 📦 Data & Metadata Contract

### Inputs

| Input                 | Type    | Required | Default                               | Description |
|----------------------|---------|----------|---------------------------------------|-------------|
| `python_version`     | string  | ✅ Yes   | _none_                                | Python version to use (e.g., `3.11`). |
| `working_directory`  | string  | ❌ No    | `${{ github.workspace }}`            | Base directory for resolving `test_paths` and config files. |
| `test_paths`         | string  | ✅ Yes   | _none_                                | Newline‑separated list of test path globs (relative to `working_directory`). |
| `pytest_args`        | string  | ❌ No    | `-ra`                                 | Additional arguments passed to `pytest` after defaults. |
| `cov_paths`          | string  | ❌ No    | _empty_                               | Newline‑separated list of source paths to measure coverage for. |
| `min_coverage`       | number  | ❌ No    | `0`                                   | Minimum allowed coverage percentage (0 disables enforcement). |
| `xfail_policy`       | string  | ❌ No    | `none`                                | One of `none` \| `no-new-xfails` \| `no-xfail-leaks` (policy for expected failures). |
| `junit_report_path`  | string  | ❌ No    | `artifacts/pytest/junit.xml`          | Path (relative) for JUnit XML report. |
| `coverage_xml_path`  | string  | ❌ No    | `artifacts/pytest/coverage.xml`       | Path (relative) for coverage XML report (if coverage is enabled). |
| `coverage_html_dir`  | string  | ❌ No    | `""`                                  | Directory (relative) for optional HTML coverage report; empty disables. |
| `telemetry_path`     | string  | ❌ No    | `artifacts/pytest/pytest-telemetry.json` | Path (relative) for telemetry JSON. |
| `cache_key_suffix`   | string  | ❌ No    | `""`                                  | Optional string to disambiguate pip cache entries (e.g., `graph`, `api`). |

### Outputs

| Output          | Type   | Description |
|-----------------|--------|-------------|
| `status`        | enum   | `"passed"` or `"failed"` after combining pytest exit code, coverage, and policy checks. |
| `tests_total`   | int    | Total number of tests executed. |
| `tests_failed`  | int    | Number of failing tests. |
| `coverage`      | number | Overall coverage percentage (if coverage enabled, else `0` or `null`). |
| `junit_report`  | string | Final resolved path to JUnit XML report. |
| `coverage_xml`  | string | Final resolved path to coverage XML report (if generated). |
| `telemetry`     | string | Final resolved path to telemetry JSON report. |

---

## ⚖ FAIR+CARE & Governance

The `pytest-runner` composite action participates in KFM governance in the following ways:

1. **Pinned implementations only**  
   - All underlying actions (`actions/checkout`, `actions/setup-python`, caching actions, etc.) MUST be pinned by `@<commit_sha>`.  
   - Pytest and coverage tools MUST be pinned via lockfiles to guarantee reproducibility.

2. **No implicit secret usage**  
   - Test execution MUST NOT implicitly use secrets unless explicitly configured in the workflow (e.g., integration tests using service tokens).  
   - Where secrets are used, test suites MUST avoid printing or leaking them into logs or JUnit/coverage artifacts.

3. **Reproducibility & determinism**  
   - Only deterministic operations are allowed by default (no random seeds without explicit seeding and logging).  
   - Test runs SHOULD be repeatable locally by developers using the same configuration and lockfiles.

4. **FAIR+CARE alignment**  
   - Test telemetry MUST be free of personally identifiable information and sensitive content.  
   - When tests involve Indigenous or restricted datasets, datasets themselves MUST be mocked or properly access‑controlled; the action MUST NOT override these safeguards.

5. **Change management**  
   - Any change to:
     - Inputs/outputs,  
     - Coverage/xfail semantics,  
     - Telemetry structure  
     MUST be accompanied by:
       - Updates to `action.yml` and this README,  
       - Schema updates (JSON/SHACL) where relevant,  
       - Passing the full test profile listed in `test_profiles`.

6. **CI enforcement**  
   - `kfm-ci.yml` SHOULD treat a failed `pytest-runner` step as a **hard block** for merging.  
   - Temporary relaxations (e.g., reduced `min_coverage`) MUST be:
     - Scoped and documented in the PR,  
     - Time‑bounded,  
     - Approved via Infrastructure & Provenance Committee procedures where required.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial governed Pytest Runner composite action; standardized coverage + xfail policy + telemetry v1.   |

---

<div align="center">

🧪 **KFM v11 — Pytest Runner Composite Action**  
Standardized Test Runs · Deterministic Coverage · FAIR+CARE‑Aligned QA Telemetry  

[⬅ Composite Actions Library](../README.md) · [📘 Markdown Protocol](../../../docs/standards/kfm_markdown_protocol_v11.2.2.md) · [⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

