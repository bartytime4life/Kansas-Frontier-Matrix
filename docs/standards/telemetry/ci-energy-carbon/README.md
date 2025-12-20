---
title: "⚡🌿 KFM — CI/CD Energy + Carbon Telemetry & Gating (OpenTelemetry + kWh/CO₂e Estimation + PR Policy Gates)"
path: "docs/standards/telemetry/ci-energy-carbon/README.md"
version: "v11.2.6"
last_updated: "2025-12-20"
status: "Active / Canonical"
doc_kind: "Standard"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE_CHARTER.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:standards:telemetry:ci-energy-carbon:v11.2.6"
semantic_document_id: "kfm-standard-telemetry-ci-energy-carbon-v11.2.6"
event_source_id: "ledger:kfm:doc:standards:telemetry:ci-energy-carbon:v11.2.6"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# ⚡🌿 KFM — CI/CD Energy + Carbon Telemetry & Gating (OpenTelemetry + kWh/CO₂e Estimation + PR Policy Gates)

## 📘 Overview

### Purpose
This document is a governed KFM standard defining CI/CD energy + carbon telemetry, estimation, publication, and policy gating. The full, unmodified standard content is preserved below (see: **Canonical Standard Content (Preserved)**).

### Scope

| In Scope | Out of Scope |
|---|---|
| CI/CD workflow/job/step observability (OTel) | Anything not covered by the data model and gates defined in this standard |
| kWh + kgCO₂e estimation for CI runs | Non-CI/CD compute unless explicitly instrumented under this standard |
| PR/release gating thresholds and baseline regression logic | Any additional governance domains not explicitly defined here |

### Audience
- Primary: CI/CD owners, KFM maintainers, DevOps/Platform engineers implementing CI telemetry + policy gates
- Secondary: CI/CD + FAIR+CARE Council reviewers, governance stakeholders consuming dashboards/artifacts

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc are defined in the preserved standard body (see **2) 🧠 Key Concepts & Definitions**).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Telemetry schema (CI) | `docs/telemetry/schemas/kfm-telemetry-ci-v1.json` | Telemetry | Referenced by preserved legacy metadata |
| Telemetry docs | `docs/telemetry/README.md` | Telemetry | Referenced by preserved legacy metadata |
| Governance reference | `docs/governance/ROOT_GOVERNANCE_CHARTER.md` | Governance | Referenced by preserved legacy metadata |
| CI telemetry artifacts | `artifacts/telemetry/ci/<run_id>.json` | CI/CD | Output location described in preserved standard body |
| Optional JSON-LD | `artifacts/telemetry/ci/<run_id>.jsonld` | CI/CD | Optional PROV alignment described in preserved standard body |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Preserved standard content retained without removal or shortening
- [ ] Validation steps are listed and repeatable (see **10) ✅ Validation & CI/CD Integration**)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (see **8.2 Waiver governance**)

## 🗂️ Directory Layout

### This document
- `path`: `docs/standards/telemetry/ci-energy-carbon/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Telemetry docs | `docs/telemetry/` | Telemetry overview + guidance |
| Telemetry schemas | `docs/telemetry/schemas/` | Telemetry JSON schemas (CI included) |
| CI workflows | `.github/workflows/` | CI workflows producing telemetry artifacts |
| Local composite action (recommended) | `.github/actions/ci-energy-carbon-gate/` | Estimation + gating scripts |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 standards/
│   └── 📁 telemetry/
│       └── 📁 ci-energy-carbon/
│           └── 📄 README.md
├── 📁 telemetry/
│   ├── 📄 README.md
│   └── 📁 schemas/
│       └── 📄 kfm-telemetry-ci-v1.json
└── 📁 governance/
    └── 📄 ROOT_GOVERNANCE_CHARTER.md

📁 .github/
├── 📁 actions/
│   └── 📁 ci-energy-carbon-gate/
│       ├── 📄 action.yml
│       ├── 📄 README.md
│       └── 📁 scripts/
│           ├── 📄 estimate_energy.py
│           ├── 📄 gate.py
│           └── 📄 baseline.py
└── 📁 workflows/
    ├── 📄 ci.yml
    └── 📄 telemetry-ci.yml
~~~

## 🧭 Context

### Background
- KFM treats CI/CD environmental impact as a first-class quality signal alongside tests/security.
- This standard specifies a consistent telemetry + estimation + gating pattern for CI/CD runs.

### Assumptions
- CI pipelines can export or derive sufficient resource usage signals to estimate energy and emissions.
- Where runner region/carbon factor is unknown, defaults are explicitly marked with confidence/uncertainty.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| TBD (not specified in preserved standard body) | TBD | TBD |

### Future extensions
- Optional marginal carbon intensity support (policy opt-in) is described in preserved standard content.
- Optional PROV-aligned JSON-LD artifact emission is described in preserved standard content.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  M["Measure (CI run telemetry)"] --> N["Normalize (OTel CI/CD + KFM extensions)"]
  N --> A["Attribute (kWh + kgCO₂e estimation)"]
  A --> E["Enforce (PR/Release policy gates)"]
  E --> P["Publish (JSON/JSON-LD artifacts + dashboards)"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| CI run metadata | OTel spans/attributes + CI metadata | CI provider (e.g., GitHub Actions) | Telemetry schema + required identity fields |
| Usage metrics | CPU seconds, utilization, memory, duration | CI runner metrics / estimator action | Range + completeness checks |
| Carbon intensity factor | numeric + source metadata | region factor / provider factor / default | Must store factor + source + vintage (if known) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI energy/carbon artifact | JSON | `artifacts/telemetry/ci/<run_id>.json` | `kfm-ci-energy-v1` shape (see preserved standard content) |
| Optional provenance artifact | JSON-LD | `artifacts/telemetry/ci/<run_id>.jsonld` | PROV alignment (recommended) |
| CI gate result | CI check | CI provider status checks | Gate version + thresholds recorded in artifact |

### Sensitivity & redaction
- Default classification is `open` and `public`; do not publish secrets, tokens, or sensitive runner details.

### Quality signals
- Schema validation for policy + artifact
- Determinism/version pinning for estimator + factor source
- Baseline robustness (rolling median guidance)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not required for CI telemetry artifacts unless explicitly minted into catalog assets (not specified in preserved standard body).

### DCAT
- Not required for CI telemetry artifacts unless published as datasets in catalog form (not specified in preserved standard body).

### PROV-O
- Recommended: emit PROV-like summary per run (see preserved standard content **10.2 Provenance alignment**).

### Versioning
- Use stable schema versions for telemetry artifacts and policy gates; record estimator + factor vintage.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| OTel CI/CD emitter | Exports CI spans/attrs/metrics | OTLP exporter |
| Energy estimator | Computes kWh + CO₂e | Action/script output → normalized artifact |
| Policy gate | Evaluates thresholds + regressions | CI check + artifact policy block |
| Artifact publisher | Uploads artifacts (always) | CI artifact storage |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Telemetry schema | `docs/telemetry/schemas/` | Semver + schema validation |
| Policy configuration | `.github/actions/.../policy.yml` | `policy_version` bump on breaking change |
| Artifact shape | `kfm-ci-energy-v1` | Versioned shape; changes recorded in history |

### Extension points checklist (for future work)
- [ ] Telemetry: new signals + schema version bump
- [ ] PROV: enrich JSON-LD linkage for audits
- [ ] CI providers: additional exporters and runner models

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Not a direct narrative input by default; intended as governance/quality telemetry that may feed dashboards and audit panels.

### Provenance-linked narrative rule
- If CI emissions claims are shown in UI contexts, they must cite artifacts and provenance refs.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Policy file schema validation
- [ ] Artifact schema validation (`kfm-ci-energy-v1`)
- [ ] Determinism checks (pinned estimator + pinned factor source where possible)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands:
# 1) validate policy schema
# 2) validate artifact schema
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI spans/attrs | OTel exporter | OTLP backend + artifact normalization |
| kWh estimate | estimator | `artifacts/telemetry/ci/<run_id>.json` |
| CO₂e estimate | estimator + CI factor | `artifacts/telemetry/ci/<run_id>.json` |
| policy outcome | gate script | artifact `policy` block + CI check |

## ⚖ FAIR+CARE & Governance

### Review gates
- Governed standard: changes reviewed on the specified cycle (see preserved legacy metadata).

### CARE / sovereignty considerations
- This standard is infrastructure-focused; avoid introducing sensitive location inference or disallowed disclosures via telemetry outputs.

### AI usage constraints
- Follow AI permissions/prohibitions in front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v11.2.6 | 2025-12-20 | Initial governed standard for CI energy + carbon telemetry & gating. | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE_CHARTER.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

---

## 🧾 Canonical Standard Content (Preserved)

### Preserved legacy front-matter (verbatim; not used as active front-matter)
~~~yaml
---
title: "⚡🌿 KFM — CI/CD Energy + Carbon Telemetry & Gating (OpenTelemetry + kWh/CO₂e Estimation + PR Policy Gates)"
path: "docs/standards/telemetry/ci-energy-carbon/README.md"
version: "v11.2.6"
last_updated: "2025-12-20"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · CI/CD + FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-ci-energy-carbon-gating"

license: "CC-BY-4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"

telemetry_schema: "docs/telemetry/schemas/kfm-telemetry-ci-v1.json"
telemetry_ref: "docs/telemetry/README.md"
governance_ref: "docs/governance/ROOT_GOVERNANCE_CHARTER.md"
---
~~~



## 1) 🎯 Purpose

This standard defines how KFM measures, estimates, publishes, and **enforces** CI/CD environmental impact:

- **Observe** CI/CD runs (workflow/job/step) with OpenTelemetry (OTel) using CI/CD semantic conventions.
- **Estimate** energy (kWh) and emissions (kgCO₂e) per workflow run using a transparent, reproducible method.
- **Gate** pull requests and releases with policy thresholds (absolute caps, regressions vs baseline, and budgeted error bars).
- **Publish** results as machine-readable artifacts (JSON/JSON-LD) and dashboards, tied to provenance.

KFM treats CI/CD impact as a first-class quality signal alongside tests/security.

---

## 2) 🧠 Key Concepts & Definitions

### 2.1 What we’re measuring

**Direct measurements** (best when feasible)
- CPU utilization / CPU time
- Memory usage and residency
- Disk and network I/O
- Runtime duration
- (Optional) On-runner power sensors (rare on hosted runners)

**Derived quantities**
- **Energy (kWh)**: estimated from utilization + runner power model + time
- **Carbon emissions (kgCO₂e)**: energy × grid carbon intensity (kgCO₂e/kWh)

### 2.2 Location-based vs market-based reporting

- **Location-based**: uses average grid emissions factors for the region (typical baseline approach).
- **Market-based**: can incorporate contractual instruments (RECs, PPAs). In CI, this is often unknown; KFM defaults to location-based unless an auditable market-based factor is supplied.

### 2.3 Marginal vs average carbon intensity

- **Average** intensity answers: “What is the typical emissions rate for electricity consumed?”
- **Marginal** intensity answers: “What emissions were caused by consuming electricity at that time?”  
  Marginal signals are useful for “carbon-aware scheduling” but are generally more complex and provider-dependent.

KFM supports both, but defaults to **average** unless a marginal signal is available and policy opts in.

---

## 3) 🧱 Architecture Overview

### 3.1 Pipeline pattern

KFM uses a consistent “Measure → Normalize → Attribute → Enforce → Publish” pattern:

1) Measure / collect run metadata and resource usage
2) Normalize into OTel CI/CD semantic conventions + KFM extensions
3) Attribute energy + emissions to workflow/job/step
4) Enforce policy gates (PR checks / release blockers)
5) Publish artifacts:
   - `artifacts/telemetry/ci/<run_id>.json`
   - `artifacts/telemetry/ci/<run_id>.jsonld` (optional PROV alignment)
   - Summary badges / PR comments / dashboards

### 3.2 Recommended components

- **OTel CI/CD emitter**: exports workflow/job telemetry to an OTLP endpoint
- **Energy estimator**: computes kWh and CO₂e
- **Policy gate**: compares against thresholds and baselines; fails the job if violated
- **Artifact publisher**: stores machine-readable results (and optionally signs them)

---

## 4) 📐 Data Model

### 4.1 Core identity fields

Every CI/CD energy record MUST include:

- `run_id` (workflow run)
- `workflow_name`, `workflow_ref` (branch/tag)
- `job_id`, `job_name` (if job scoped)
- `repo`, `org`
- `commit_sha`
- `actor` (service account/human)
- `runner_type` (hosted/self-hosted)
- `runner_os`, `runner_arch`
- `started_at`, `finished_at`, `duration_seconds`

### 4.2 OTel CI/CD semantic conventions mapping

KFM aligns to OTel’s CI/CD semantic conventions for:

- pipeline identity (name, run id, action)
- worker identity (runner/agent)
- run results (success/failure/cancel)
- span structure: pipeline run span + task spans where available

KFM adds a minimal extension namespace for environment metrics:

- `kfm.cicd.energy.kwh.estimated`
- `kfm.cicd.co2e.kg.estimated`
- `kfm.cicd.ci_factor.kg_per_kwh.used`
- `kfm.cicd.ci_factor.source`
- `kfm.cicd.estimation.method`
- `kfm.cicd.estimation.uncertainty.pct`

### 4.3 Minimal JSON artifact (example shape)

    {
      "schema_version": "kfm-ci-energy-v1",
      "identity": {
        "run_id": "1234567890",
        "repo": "Kansas-Frontier-Matrix",
        "commit_sha": "abc123...",
        "workflow_name": "CI",
        "job_name": "tests",
        "runner_type": "github-hosted",
        "runner_os": "ubuntu-latest"
      },
      "timing": {
        "started_at": "2025-12-20T03:14:15Z",
        "finished_at": "2025-12-20T03:24:15Z",
        "duration_seconds": 600
      },
      "usage": {
        "cpu_seconds": 820.4,
        "avg_cpu_utilization": 0.62,
        "memory_gb_seconds": 2100.0
      },
      "estimation": {
        "method": "eco-ci + region-factor",
        "energy_kwh_est": 0.12,
        "co2e_kg_est": 0.05,
        "ci_factor_kg_per_kwh": 0.42,
        "ci_factor_source": "eGRID subregion or global average",
        "uncertainty_pct": 25
      },
      "policy": {
        "gate_version": "kfm-ci-carbon-gate-v1",
        "status": "pass",
        "thresholds": {
          "max_energy_kwh": 0.30,
          "max_co2e_kg": 0.20,
          "max_regression_pct": 15
        }
      }
    }

---

## 5) 🔢 Estimation Methodology

### 5.1 The core equations

Energy estimation typically resolves to:

- Energy (kWh) = Average Power (kW) × Duration (hours)

To estimate average power, you can use a utilization-weighted model:

- P_avg = P_idle + (P_max − P_idle) × U_cpu^α

Where:
- P_idle and P_max come from a runner power profile
- U_cpu is mean CPU utilization (0..1)
- α is a tuning exponent (often between 1.0 and 2.0; KFM defaults to 1.0 unless calibrated)

Then:
- kWh = (P_avg / 1000) × (duration_seconds / 3600)

Carbon emissions:
- kgCO₂e = kWh × CI_factor_kg_per_kWh

### 5.2 Choosing the carbon intensity factor

KFM supports a priority order:

1) **Known region factor** (e.g., EPA eGRID subregion) when runner location is known and US-based
2) **Cloud provider region factor** when cloud region is known
3) **Global default** when region is unknown (explicitly marked as “low confidence”)

KFM always stores:
- factor value
- factor source
- factor year/vintage (where known)

### 5.3 Uncertainty & policy

CI energy/carbon estimates are **models**, not lab-grade measurement. KFM mandates an uncertainty term:

- Default uncertainty: 25% for hosted runners without power sensors
- Policy gates MUST either:
  - include a buffer (thresholds account for uncertainty), or
  - use regression tests that require repeated runs / rolling averages

---

## 6) 🛡️ Gating Patterns

KFM uses three complementary gates. Repos may enable any subset, but “Release” repos SHOULD enable all.

### 6.1 Absolute caps

Fail if:
- `energy_kwh_est > max_energy_kwh`, or
- `co2e_kg_est > max_co2e_kg`

Use for:
- runaway workflows
- accidental infinite loops
- expensive integration tests triggered too often

### 6.2 Regression vs baseline

Compare the current run to a baseline (e.g., `main` branch median of last N runs for same job).

Fail if:
- (current − baseline) / baseline > max_regression_pct

Baseline guidance:
- Use at least N=20 recent runs where possible
- Prefer median over mean (robust to outliers)
- Maintain separate baselines per workflow/job/runner OS

### 6.3 Budgeted “PR allowance”

Treat CI carbon like an error budget:
- Each PR “spends” an allowance, replenished over time (weekly/monthly)
- If budget exhausted, PR must reduce impact or request an explicit waiver

---

## 7) 🧰 Implementation — GitHub Actions Reference Design

This section is copy/paste scaffolding. It is written to be vendor-neutral and compatible with OTel backends.

### 7.1 Directory placement (recommended)

    📂 .github/
      📂 actions/
        📂 ci-energy-carbon-gate/
          📄 action.yml
          📄 README.md
          📂 scripts/
            📄 estimate_energy.py
            📄 gate.py
            📄 baseline.py
      📂 workflows/
        📄 ci.yml
        📄 telemetry-ci.yml

### 7.2 Workflow wiring (high level)

Recommended job ordering:

1) Build/Test job(s)
2) Telemetry export job (OTel)
3) Energy/Carbon estimate job
4) Gate job (can run in same job as estimate)
5) Upload artifacts (always, even on fail)

### 7.3 Example workflow snippet (indent-only YAML)

    name: CI

    on:
      pull_request:
      push:
        branches: [ main ]

    jobs:
      tests:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - name: Run tests
            run: |
              make test

      energy-carbon:
        needs: [ tests ]
        runs-on: ubuntu-latest
        permissions:
          contents: read
          pull-requests: write
        steps:
          - uses: actions/checkout@v4

          # (A) Export CI/CD spans/metrics (OTel) — optional but recommended
          - name: Export CI telemetry
            uses: paper2/github-actions-opentelemetry@v1
            with:
              otlpEndpoint: ${{ secrets.OTEL_EXPORTER_OTLP_ENDPOINT }}
              otlpHeaders: ${{ secrets.OTEL_EXPORTER_OTLP_HEADERS }}

          # (B) Estimate energy & carbon and produce artifact JSON
          - name: Estimate energy/carbon
            uses: green-coding-solutions/eco-ci-energy-estimation@v4
            with:
              # Example inputs vary by action version; pin versions and record actual inputs in artifact
              co2i: "0.42"        # kgCO2e/kWh (example)
              # output formats are action-specific; ensure we capture outputs to a file

          # (C) Gate
          - name: Gate on carbon policy
            run: |
              python .github/actions/ci-energy-carbon-gate/scripts/gate.py \
                --input artifacts/telemetry/ci/current.json \
                --policy .github/actions/ci-energy-carbon-gate/policy.yml

          # (D) Upload artifacts (always)
          - name: Upload telemetry artifacts
            if: always()
            uses: actions/upload-artifact@v4
            with:
              name: ci-energy-carbon
              path: artifacts/telemetry/ci/

Notes:
- The estimator step may produce outputs as env vars, action outputs, or files; normalize them into KFM’s JSON artifact.
- Always “upload artifacts” with `if: always()` so failed gates still publish evidence.

---

## 8) 📦 Policy Configuration

### 8.1 Policy file (example)

    # .github/actions/ci-energy-carbon-gate/policy.yml
    policy_version: kfm-ci-carbon-gate-v1
    default_uncertainty_pct: 25

    thresholds:
      max_energy_kwh: 0.35
      max_co2e_kg: 0.20
      max_regression_pct: 15

    baselines:
      mode: rolling_median
      window_runs: 30
      key_fields:
        - workflow_name
        - job_name
        - runner_os

    behavior:
      fail_on_missing_baseline: false
      fail_on_unknown_ci_factor: false
      require_factor_vintage: false

    waivers:
      allowed_labels:
        - "ci-carbon-waiver"
      require_reason: true

### 8.2 Waiver governance

Waivers are allowed, but must be explicit and auditable:
- PR label applied by maintainers only
- PR comment must include reason + expiry (date)
- Waivers are logged into telemetry artifacts (`policy.waiver_applied=true`)

---

## 9) 📊 Dashboards & Alerts

KFM recommends 3 dashboard layers:

1) **Engineering dashboard**
   - kWh and kgCO₂e by workflow/job over time
   - regressions highlighted
2) **Governance dashboard**
   - monthly totals
   - waiver counts
   - trend lines vs targets
3) **FinOps crosswalk**
   - correlate runner minutes / cloud costs / energy

Alerting patterns:
- “Runaway CI” (absolute caps exceeded)
- “Sustained regression” (p95 over baseline for 7 days)
- “Waiver abuse” (too many waivers or long-lived waivers)

---

## 10) ✅ Validation & CI/CD Integration

### 10.1 Validation checks (required)

- Policy file schema validation
- Artifact schema validation (`kfm-ci-energy-v1`)
- Determinism checks:
  - estimator version pinned
  - factor source pinned (or minted with a known vintage)
  - commit SHA recorded

### 10.2 Provenance alignment (recommended)

Emit a PROV-like summary for each CI run:
- Activity: CI workflow run
- Entities: source tree, lockfiles, container images, artifacts
- Agents: GitHub Actions runner, actor, service account

This makes it possible to answer:
- “What changed that increased CI emissions?”
- “Which workflows drive most of our CI carbon?”

---

## 11) 🔍 Practical Optimization Playbook

Common fixes that reduce CI energy immediately:

- **Cancel superseded runs** on PR updates
- Add **path filters** so docs-only changes don’t run heavy jobs
- Use **caching** intelligently (dependency cache; build cache)
- Split “quick checks” vs “full suite”
- Reduce matrix explosion; run full matrix on schedule, not every PR
- Prefer smaller test datasets and fewer integration environments per PR
- Move expensive jobs to nightly + allow on-demand manual trigger

Carbon-aware enhancements (advanced):
- Run scheduled jobs when grid intensity is lower (requires marginal signal + scheduler integration)
- Prefer runner regions with lower average carbon intensity where feasible

---

## 12) 🧾 Reference Tooling Matrix

KFM commonly uses (or interoperates with):

- OTel CI/CD exporters for GitHub Actions (workflow/job telemetry to OTLP)
- Eco CI (CI energy estimation)
- Cloud Carbon Footprint (cloud emissions estimation methodology and factors)
- CodeCarbon (application-level compute emissions estimation; especially for ML workloads)
- eGRID (US electricity emissions factor source)

KFM does not require any single vendor backend; any OTLP-compatible stack can be used.

---

## 13) 🗂️ Version History

- v11.2.6 (2025-12-20): Initial governed standard for CI energy + carbon telemetry & gating.

---

## 14) 🔗 Footer

- ⬅️ Back to Index: `docs/README.md`
- 🧱 Telemetry: `docs/telemetry/README.md`
- 🛡️ Governance Charter: `docs/governance/ROOT_GOVERNANCE_CHARTER.md`

