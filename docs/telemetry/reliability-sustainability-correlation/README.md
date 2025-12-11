---
title: "⚡🌱 KFM v11.2.6 — Reliability × Sustainability Correlation Telemetry (Retries/Replays ↔ Energy/CO₂e)"
path: "docs/telemetry/reliability-sustainability-correlation/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Design + Implementation Guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

semantic_document_id: "kfm-doc-telemetry-reliability-sustainability-correlation"
doc_uuid: "urn:kfm:doc:telemetry:reliability-sustainability-correlation:v11.2.6"
event_source_id: "ledger:docs/telemetry/reliability-sustainability-correlation/README.md"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/reliability-sustainability-correlation-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/correlation-reliability-sustainability-v2.json"
reliability_schema: "../../../schemas/telemetry/reliability-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Operational Telemetry"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"

scope:
  domain: "telemetry"
  applies_to:
    - "otel"
    - "stac-lineage"
    - "orchestrators"
    - "energy-carbon"
    - "reliability"

semantic_intent:
  - "otel-schema"
  - "reliability-telemetry"
  - "sustainability-correlation"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"
  - "telemetry-schema-check"
---

# ⚡🌱 Reliability × Sustainability Correlation Telemetry

## 1. Overview & Purpose

This guide defines how KFM tracks **time-series correlations** between CI/CD **retry/replay activity** (WAL/replay, flake retries, job requeues) and **energy + CO₂e telemetry** across the platform.

**Outcome:** a governed, reproducible way to quantify how reliability mechanisms affect sustainability, support **SLO + error-budget** decisions, and expose **CI waste hotspots**.

For each CI job execution (original or retry), the system MUST emit **aligned spans and metrics** keyed by a shared correlation ID so we can compute:

- Extra **kWh** and **CO₂e** from retries & replays.  
- **Marginal cost of flakiness** per workflow, path, runner, and dependency set.  
- **Abatement opportunities** (caching, sharding, deflaking, dependency tuning).

This design assumes baseline familiarity with:

- Experimental design and statistical reasoning (correlation, confounding, uncertainty).  
- Data-science and ML-style time-series analysis for telemetry.  
- Basic neural-network and agentic decision-surface concepts for closing the loop between telemetry and automated CI/CD policy changes.

These foundations are documented in KFM’s internal statistics, data-science, and AI reference materials.

---

## 2. Architecture

### 2.1 Signals (Metrics & Traces)

**Metrics (OpenTelemetry → Prometheus/Mimir):**

- `reliability.retry_count`, `reliability.replay_count`, `reliability.outcome` (pass/fail/flaky).  
- `energy.kwh`, `energy.duration_seconds`, `energy.power_watts_avg`.  
- `carbon.co2e_grams`, `carbon.factor_source` (grid/region/profile).

All keyed (directly or via aggregation) by:

- `kfm.exec_correlation_id`  
- `kfm.wal_session_id` (when a replay framework is present)

**Traces (OTel → Tempo/Jaeger):**

- Root span per workflow run: `ci.workflow.run`.  
- Child spans per job attempt: `ci.job.attempt`.  
- Span attributes and links (see §4).

### 2.2 Lineage & PROV-O

Each CI attempt is modeled as:

- `prov:Activity` — single job attempt.  
- `prov:Entity` — energy/carbon telemetry bundles, WAL snapshots, artifact bundles.  
- `prov:Agent` — CI runner pool, project, and responsible team (for governance).

Relationships:

- `prov:wasGeneratedBy` → energy/carbon entities generated by an attempt.  
- `prov:wasInformedBy` → previous failed/flaky attempts (retries / replays).  
- `prov:wasAssociatedWith` → CI runner/image, project, and owning team.

### 2.3 Storage & Query Surfaces

- **Metrics** — Prometheus/Mimir, with **cardinality-governed** label sets (see metric cardinality standards).  
- **Traces** — Tempo/Jaeger with `trace_id == kfm.exec_correlation_id`.  
- **Long-term** — daily Parquet snapshots written under `data/telemetry/ci/` for governed audits and analyses.  
- **Catalogs** — STAC/DCAT/PROV snapshots (see §6) for FAIR findability and reuse.

---

## 3. Metrics & Labels

### 3.1 Minimal Labels (Cardinality-Safe)

Required correlation / routing labels (non-exhaustive):

- `kfm.exec_correlation_id` — UUID; one per workflow execution tree.  
- `kfm.wal_session_id` — shared across replay sessions when WAL is present.  
- `ci.workflow`, `ci.job`, `ci.repo`, `ci.ref_kind` (branch/tag).  
- `ci.runner_type` — e.g., `github-hosted`, `self-hosted-aws`, `self-hosted-lab`.  
- `artifact.group` — high-level component (`api`, `graph`, `ui`, `etl-historical`, `etl-remote-sensing`, etc.).  
- `test.suite` — sharded test group IDs (e.g., `unit-01`, `unit-02`, `e2e-01`).  
- `grid.region` — e.g., `US-MISO`, `US-SPP`, `EU-ENTSOE`, `Unknown`.  
- `carbon.method` — `location-based` or `market-based`.

**MUST NOT:**

- Use per-commit hashes or PR IDs as metric labels (store in traces/logs instead).  
- Embed high-cardinality env names or ephemeral pod IDs in labels.  
- Include user identifiers, feature IDs, or raw paths/URLs as metric labels.

### 3.2 Metrics (Prometheus) — Recording Rules

Core counters:

- `reliability_retry_total{ci.workflow, ci.job, attempt_kind="retry"}`  
- `reliability_replay_total{ci.workflow, ci.job, attempt_kind="replay"}`  

Energy / CO₂e per attempt (exporter-produced, then aggregated):

- `ci_attempt_energy_kwh_sum{ci.workflow, ci.job, attempt_kind}`  
- `ci_attempt_carbon_co2e_g_sum{ci.workflow, ci.job, attempt_kind}`  

Example derived series (recording rules):

~~~text
# Energy attributable to retries (last 24h)
ci_retry_energy_kwh_24h =
  sum_over_time(ci_attempt_energy_kwh_sum{attempt_kind="retry"}[24h])

# Marginal CO₂e from retries per workflow (rolling 24h window)
ci_retry_co2e_g_24h_by_wf =
  sum by (ci.workflow) (
    rate(ci_attempt_carbon_co2e_g_sum{attempt_kind="retry"}[24h])
  )
~~~

---

## 4. Tracing & CI Attempt Correlation

### 4.1 Span Model (OpenTelemetry)

**Root span** — one per workflow run:

- `name`: `ci.workflow.run`  
- Attributes:
  - `kfm.exec_correlation_id` (also used as trace ID).  
  - `ci.workflow`, `ci.repo`, `ci.ref`, `ci.ref_kind`.  
  - `ci.trigger` (push, PR, schedule, manual).  
  - `ci.runner_type`, `grid.region`.

**Child spans** — one per job attempt:

- `name`: `ci.job.attempt`  
- Attributes:
  - `ci.job`  
  - `attempt.index` (`0` = first, `1` = retry1, …)  
  - `attempt.kind` (`first`, `retry`, `replay`)  
  - `attempt.reason` (`timeout`, `network`, `test-flake`, `infra`, `manual-replay`, …)  
  - `duration.seconds`  
  - `energy.kwh`, `energy.power_watts_avg`  
  - `carbon.co2e_g`, `carbon.factor_source`, `grid.region`  
  - `cache.hit_ratio` (if cache layer present)  
  - `flake.suspect` (boolean heuristic: true if test flake suspected)  
  - `runner.cpu_model`, `runner.tdp_w`

**Relationships:**

- `SpanLink` (or equivalent) to the previous attempt span for that job.  
- `prov:wasInformedBy` backbone in the PROV bundle mirroring span links.

### 4.2 CI/CD Integration (GitHub Actions)

**Correlation IDs:**

1. At workflow start:  
   - Generate `kfm.exec_correlation_id` (UUID v4).  
   - Export to `GITHUB_ENV` and OTel resource attributes.

2. For retries:  
   - Increment `attempt.index` and set `attempt.kind="retry"` on job spans.  
   - For WAL-based replays, include `kfm.wal_session_id`.

**Runner-side exporters:**

- **Energy sampler**:
  - Polls CPU usage, core count, and nominal TDP.  
  - Applies device-specific power models to estimate `energy.kwh`.

- **Carbon calculator**:
  - Combines `energy.kwh` with `grid.region` and `carbon.method`.  
  - Applies governed emission factors to compute `carbon.co2e_g`.  
  - Records `carbon.factor_source` and version for reproducibility.

**Composite actions (seed layout):**

- `.github/actions/otel-export/`  
  - Sets OTel env, injects correlation IDs, exports spans/metrics.  
- `.github/actions/energy-sampler/`  
  - Estimates `energy.kwh` and `carbon.co2e_g`, emits to OTel.  
- `.github/actions/reliability-emit/`  
  - Standardizes retry/replay events, reasons, and attempt labels.

---

## 5. Data Contracts & Schemas

All telemetry MUST conform to the following JSON Schemas (or successors) under `schemas/telemetry/`:

### 5.1 Reliability Telemetry (`reliability-v2.json`)

Minimum fields:

- `attempt.index` — integer ≥ 0.  
- `attempt.kind` — enum: `first`, `retry`, `replay`.  
- `attempt.reason` — constrained enum (governed list).  
- `duration.seconds`.  
- `outcome` — `pass`, `fail`, `flaky`, `canceled`.  
- `kfm.exec_correlation_id` — UUID.  

Optional but recommended:

- `kfm.wal_session_id`, `test.suite`, `artifact.group`.

### 5.2 Energy Telemetry (`energy-v2.json`)

Minimum fields:

- `energy.kwh`.  
- `power.w_avg`.  
- `device.tdp_w`.  
- `runner.cpu_model`.  
- `grid.region`.

### 5.3 Carbon Telemetry (`carbon-v2.json`)

Minimum fields:

- `carbon.co2e_g`.  
- `carbon.factor.method` — `location-based` or `market-based`.  
- `carbon.factor.source_ref` — URI/URN for factor dataset.  
- `carbon.time_weighting` — how time of day and grid profile were applied.

### 5.4 Correlation Envelope (`correlation-reliability-sustainability-v2.json`)

Envelope binding reliability, energy, and carbon:

- `kfm.exec_correlation_id`.  
- `ci.workflow`, `ci.job`.  
- Embedded:
  - `reliability` (per `reliability-v2.json`).  
  - `energy` (per `energy-v2.json`).  
  - `carbon` (per `carbon-v2.json`).  
- `prov` references:
  - `activity_id` (attempt).  
  - `entity_ids` (telemetry bundles, WAL snapshots).  
  - `agent_ids` (runner, owning team, project).

---

## 6. STAC/DCAT & PROV Alignment

### 6.1 STAC

Daily **aggregated CI telemetry snapshots** SHOULD be published as STAC Items under a dedicated Collection, for example:

- Collection ID: `kfm-ci-telemetry-reliability-sustainability`.  
- Item properties:
  - `kfm.exec_date` — `YYYY-MM-DD`.  
  - `kfm.metrics.retry_energy_kwh`.  
  - `kfm.metrics.retry_co2e_g`.  
  - `kfm.metrics.retry_count`.  

Assets:

- `metrics_parquet` — Parquet file with per-attempt rolled-up metrics.  
- `trace_manifest` — JSON mapping `kfm.exec_correlation_id` → trace URIs.

### 6.2 DCAT

Define a DCAT Dataset:

- Title: `KFM CI Telemetry — Reliability × Sustainability`.  
- Description: scope, schemas, and limitations.  
- Spatial: optional (grid-region coverage).  
- Temporal: dataset time range; Items per day.  

Distributions:

- Links to STAC Collections/Items.  
- Links to Parquet snapshots and trace manifests.

### 6.3 PROV-O

Each daily snapshot is a `prov:Entity` generated by a snapshotter `prov:Activity` (for example, `ci.snapshotter@vX.Y`):

- `prov:wasGeneratedBy` → snapshotter job.  
- `prov:used` → raw Prometheus/Mimir series, trace store.  
- `prov:wasAssociatedWith` → reliability engineering team, platform ops.

---

## 7. FAIR+CARE & Governance

Reliability × sustainability telemetry is inherently **governance-driven**:

- **FAIR:**
  - *Findable* — STAC/DCAT catalogs; stable IDs for metrics/snapshots.  
  - *Accessible* — governed access via telemetry APIs and CI dashboards.  
  - *Interoperable* — JSON Schemas, PROV-O, OpenTelemetry standards.  
  - *Reusable* — documented factors, methods, and caveats.

- **CARE:**
  - *Collective Benefit* — visibility into CI waste supports resource stewardship and climate goals.  
  - *Authority to Control* — project and team owners MUST be able to see and govern how their pipelines are measured and optimized.  
  - *Responsibility* — telemetry is used to improve systems, not to punish individuals.  
  - *Ethics* — no per-person metrics; no cross-team shaming dashboards.

**Error-budget policy hooks:**

- Define governed thresholds for:
  - `retry_co2e_g_24h_by_wf` per workflow.  
  - `retry_energy_kwh_24h` for the whole org.

When thresholds are exceeded, CI SHOULD:

- Trigger flaky-test quarantine workflows.  
- Require caching/deflake plans before merging high-risk changes.  
- Route notifications to responsible **teams**, not individuals.

All assumptions about grid factors, device models, and uncertainty ranges MUST be documented in `GOVERNANCE.md` and referenced in dashboards and docs.

---

## 8. Example Queries & Dashboards

### 8.1 Example PromQL Queries

**Top 10 wasteful jobs (CO₂e, last 7 days):**

~~~text
topk(
  10,
  sum by (ci.job) (
    increase(ci_attempt_carbon_co2e_g_sum{attempt_kind="retry"}[7d])
  )
)
~~~

**Marginal CO₂e per passed build (by workflow):**

~~~text
(
  sum by (ci.workflow) (ci_attempt_carbon_co2e_g_sum{attempt_kind="retry"})
)
/
(
  sum by (ci.workflow) (ci_builds_passed_total)
)
~~~

**Before/after deflake PR (A/B across 14-day windows):**

- Use `kfm.exec_correlation_id` cohorts and `ci.ref` / `ci.ref_kind` to slice pre/post ranges.  
- Compare:
  - Retry counts.  
  - Retry CO₂e.  
  - Success rate.

### 8.2 Dashboard Themes

- **Org overview:** total retry energy and CO₂e by week; top offenders.  
- **Workflow detail:** timeline of retries and waste; forecasted reduction under proposed fixes.  
- **Experiment view:** effect of specific PRs or caching changes on metrics.

---

## 9. Directory Layout

Telemetry correlation docs and configuration MUST follow KFM emoji-style directory conventions.

~~~text
📂 docs/
└── 📂 telemetry/
    └── 📂 reliability-sustainability-correlation/
        ├── 📝 README.md          # This file – design + implementation guide
        ├── 🧱 EXAMPLES.md        # Dashboard configs, PromQL examples, analysis snippets
        ├── 🧪 VALIDATION.md      # Schema checks, CI test matrix, governance review steps
        ├── 📊 DASHBOARDS/        # Grafana JSON exports and wiring notes
        ├── 🧩 ALERTS/            # Prometheus alerting rules + runbooks
        └── 🧭 GOVERNANCE.md      # Thresholds, ownership, review cadence, exceptions process

📂 schemas/
└── 📂 telemetry/
    ├── 📄 reliability-v2.json
    ├── 📄 energy-v2.json
       📄 carbon-v2.json
    └── 📄 correlation-reliability-sustainability-v2.json

📂 .github/
└── 📂 actions/
    ├── ⚙️ otel-export/
    ├── ⚙️ energy-sampler/
    └── ⚙️ reliability-emit/

📂 data/
└── 📂 telemetry/
    └── 📂 ci/
        ├── 📦 snapshots/YYYY/MM/DD/*.parquet
        └── 🧾 trace-manifests/*.json
~~~

Any deviations from this structure MUST be documented here and in `VALIDATION.md`.

---

## 10. CI/CD Validation & Gates

Changes to this module MUST pass at least:

- **Markdown checks**
  - KFM-MDP v11.2.6 compliance (single YAML front matter, heading layout, emoji directory style).

- **Schema validation**
  - `reliability-v2.json`.  
  - `energy-v2.json`.  
  - `carbon-v2.json`.  
  - `correlation-reliability-sustainability-v2.json`.

- **Provenance checks**
  - PROV entities and activities for each daily snapshot.  
  - OpenLineage (or equivalent) events for snapshot jobs, referencing CI runs.

- **Cardinality guards**
  - Label sets for metrics MUST remain within governed limits (see metric cardinality standards).  
  - CI jobs MUST fail if new labels would exceed configured max-cardinality thresholds.

- **Sustainability gates (optional → enforced)**
  - If per-workflow `retry_co2e_g_24h_by_wf` exceeds configured budgets:
    - fail fast on optional stages (e.g., non-critical matrix expansions).  
    - require annotation or override from responsible team.

---

## 11. Implementation Steps (Fast Path)

A “90-minute pass” implementation SHOULD:

1. **Wire correlation IDs**  
   - Generate and propagate `kfm.exec_correlation_id` in all GitHub Actions workflows.

2. **Emit spans & metrics**  
   - Add `.github/actions/otel-export/` to all CI entrypoints.  
   - Ensure `attempt.index` / `attempt.kind` labels for retries and replays.

3. **Estimate energy & CO₂e**  
   - Install `.github/actions/energy-sampler/` and `.github/actions/reliability-emit/`.

4. **Snapshot & catalog**  
   - Deploy daily snapshot job writing Parquet + STAC/DCAT + PROV.

5. **Dashboards & alerts**  
   - Import baseline dashboards and alerts from `DASHBOARDS/` and `ALERTS/`.

6. **Governance hooks**  
   - Configure thresholds in `GOVERNANCE.md`.  
   - Wire alerts to Reliability Engineering + FAIR+CARE Council channels.

Subsequent passes can refine device models, grid factors, and machine-learning layers (for example, anomaly detection on correlations) without breaking the contract defined here.

---

## 12. Version History

| Version | Date       | Summary                                                                                                              |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | Initial governed spec; defines schemas, CI hooks, dashboards, alerts, and SLO/sustainability integration.           |

---

<div align="center">

⚡🌱 **KFM v11.2.6 — Reliability × Sustainability Correlation Telemetry**  
Reliability With Purpose · Sustainable CI · FAIR+CARE-Aligned Telemetry  

[📘 Docs Root](../../README.md) ·  
[📡 Telemetry Index](../README.md) ·  
[📊 Metrics & Cardinality Standards](../metrics/README.md) ·  
[📡 OTel + STAC Lineage Schema](../otel-stac-lineage/README.md) ·  
[🧭 Standards Index](../../standards/README.md) ·  
[⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🌿 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>