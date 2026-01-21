# 📏 MCP Metrics Reviews (KFM)

![Status](https://img.shields.io/badge/status-active%20design-blue)
![MCP](https://img.shields.io/badge/MCP-Methods%20%7C%20Controls%20%7C%20Policies-6f42c1)
![Governance](https://img.shields.io/badge/policy-fail--closed-critical)
![Telemetry](https://img.shields.io/badge/telemetry-NDJSON-informational)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-success)
![Graph](https://img.shields.io/badge/graph-Neo4j-0e7a0d)
![GIS](https://img.shields.io/badge/GIS-PostGIS-2b5daa)

> 🎯 **Goal:** This folder defines **what we measure**, **how we measure it**, and **how we review the results** so KFM stays *auditable, reproducible, provenance-first,* and *governance-aligned*.

---

## 🧭 Where this fits

KFM’s high-level pipeline is designed so each stage is traceable and governed: **Raw Data → ETL → Graph/DB → Web UI → Story Nodes → Focus Mode → Governance & Telemetry**. The metrics in this folder are the *objective evidence* that those boundaries are holding.  
[^pipeline-flow] [^arch-flow]

---

## 📚 Table of contents

- [What lives here](#-what-lives-here)
- [Metrics philosophy](#-metrics-philosophy)
- [Metric suites](#-metric-suites)
- [Artifacts and outputs](#-artifacts-and-outputs)
- [Review workflow](#-review-workflow)
- [MetricSpec format](#-metricspec-format)
- [Dashboards and UI surfacing](#-dashboards-and-ui-surfacing)
- [Security, privacy, and ethics metrics](#-security-privacy-and-ethics-metrics)
- [Adding a new metric](#-adding-a-new-metric)
- [Reference bundles](#-reference-bundles)
- [Glossary](#-glossary)
- [Source anchors](#-source-anchors)

---

## 📁 What lives here

This directory is intentionally **review-focused** (specs + templates + conventions). Generated results belong in **versioned report folders** (see [Artifacts and outputs](#-artifacts-and-outputs)).

```text
mcp/
└─ 🧠 reviews/
   └─ 📈 metrics/
      ├─ 📄 README.md                # ← you are here 📌 What metrics mean, how they’re collected, and pass/fail thresholds
      ├─ 📐 specs/                   # MetricSpec definitions (YAML/JSON; versioned, contract-first)
      ├─ 🧾 suites/                  # Suite manifests (graph_health, policy_gates, focus_qa, ui_perf, etc.)
      ├─ 🔎 queries/                 # Reusable queries (Cypher/SQL) used by suites (keep deterministic + read-only)
      ├─ 🧩 templates/               # Reviewer checklists + PR/issue templates for consistent reporting
      └─ 📚 docs/                    # (optional) Deeper rationale per suite (interpretation, pitfalls, edge cases)
```

> 🔍 **MCP context:** `mcp/` is where KFM codifies “Methods / Controls / Policies” (best practices, governance, review templates, etc.).  
[^mcp-dir]

---

## 🧠 Metrics philosophy

### 1) **Fail-closed for governance**
KFM treats governance checks like tests: if a policy gate fails, the change does not ship.  
Policy gates are expected to check **licensing, metadata completeness (STAC/DCAT/PROV), sensitivity classification, provenance completeness,** and even that **AI/Focus answers contain citations**.  
[^policy-gates] [^policies-as-tests] [^prov-enforcement]

### 2) **Provenance-first, evidence-first**
- Ingestion logs **checksums**, performs light validation, and records events to an **append-only NDJSON telemetry ledger** so pipelines can be audited and dashboards can be built.  
  [^ingestion-gate]  
- Story Nodes should be “evidence-first narratives” backed by structured manifests and CI validation.  
  [^evidence-first-stories] [^citation-manifest-ci]

### 3) **Determinism and reproducibility**
- Runs should emit a **Run Manifest** (who/what/when, inputs/outputs, tool versions, summary counts).  
- Manifests should be **canonicalized** (RFC 8785) before hashing, enabling stable **digests** and **idempotency keys**.  
  [^run-manifest]

### 4) **Measure quality, not just breakage**
Metrics aren’t only “pass/fail”. We measure **trends**, **drift**, and “quality debt”:
- Metadata completeness over time  
- Citation coverage + drift in AI behavior  
- Graph growth anomalies  
- Accessibility + UI performance regressions  
[^qa-metrics]

### 5) **Human-in-the-loop where it matters**
Automation is designed to reduce toil—not replace judgment. KFM’s governance workflow (e.g., ethics, sustainability, accessibility review) remains human accountable for high-stakes data.  
[^council-workflow] [^prov-enforcement]

---

## 🧰 Metric suites

Each suite is a *bundle* of checks with shared inputs + shared output conventions.

| Suite 🧪 | Purpose | Typical cadence ⏱️ | Output | Gate level |
|---|---|---:|---|---|
| `policy_gates` 🛡️ | Enforce FAIR/CARE + licensing + provenance + sensitivity | Every PR | PASS/WARN/FAIL report + CI annotation | **Hard gate** |
| `graph_health` 🕸️ | Detect graph corruption, drift, orphan nodes, runaway hubs, backup validity | Weekly (e.g., Sunday) | summary.md + index.csv + artifacts | **Hard gate** for critical checks |
| `intake_telemetry` 📥 | Ingest success, checksum integrity, schema sanity, anomaly flags | Continuous / nightly | time-series rollups | Soft gate (trend) + hard gate (integrity) |
| `focus_qa` 🤖 | Citation coverage, refusal correctness, latency, drift signals | Nightly + PR for model changes | QA report + drift chart | **Hard gate** for uncited claims |
| `ui_accessibility` ♿ | ARIA/semantic HTML coverage, keyboard nav, contrast regressions | On UI PRs | a11y report | Soft/Hard (project choice) |
| `ui_perf` ⚡ | Render time, tile latency, memory, offline pack size | Nightly + release | perf report | Soft gate (trend) |
| `story_evidence` 🎬 | Story Node evidence manifests + citation integrity | Every Story PR | lint report | **Hard gate** |

> ✅ **Graph health checks** should include deltas, constraint/index integrity, orphan detection, hub detection, schema drift checks, and backup verification—each producing artifacts.  
[^graph-health-checks] [^graph-artifacts]

---

## 🧾 Artifacts and outputs

### ✅ Required output pattern
Metrics must produce artifacts that are:
- **Versioned** (timestamped directories)
- **Linkable** (summary.md points to detailed CSV/JSON artifacts)
- **Trendable** (index.csv captures key values per run)

A reference pattern for graph health checks stores history under:
```text
docs/reports/qa/graph_health/
  2026-01-14T08-30-12Z/
    summary.md
    index.csv
    orphan_nodes.csv
    top_degree_nodes.csv
    schema_drift.json
    backup_verify.log
```
[^graph-artifacts]

### 🧾 Run manifests
Every suite run SHOULD emit a machine-readable manifest, stored e.g.:
```text
data/audits/<run_id>/run_manifest.json
```
…and referenced in provenance.  
[^run-manifest]

### 📦 Optional: Artifact packaging + signing
For high-integrity distribution, metric outputs (and even model/pipeline bundles) can be shipped as **OCI artifacts** (ORAS) and **signed** (Cosign) for supply-chain traceability and rollback safety.  
[^oci-artifacts]

---

## 🧑‍⚖️ Review workflow

### 1) CI + policy first (automated)
1. Suite runs (PR / nightly / weekly)
2. Policy checks run and **fail the job** on deny rules  
3. A summary is written + artifacts attached/published  
[^policy-gates] [^policies-as-tests] [^ci-fail-closed]

### 2) Triage (human)
Use this quick triage rubric:

- 🟥 **FAIL (Blocker):** provenance broken, missing license, uncited AI claims, backup invalid, constraints failing  
- 🟧 **WARN (Investigate):** drift detected, hub explosion, schema drift > threshold, orphan deltas > threshold  
- 🟩 **PASS:** all green

> If **two or more checks fail**, the system should automatically create tracker issues (labels like `ci_failure`, `data_layer_request`) to force visibility.  
[^graph-artifacts]

### 3) Escalation paths
- **Data-layer failures** → ETL maintainers + graph maintainers
- **Governance failures** → Council workflow (Ethics → FAIR → Sustainability → Accessibility → Approval)  
[^council-workflow]
- **Focus Mode failures** → AI governance + prompt security owners  
[^ai-governance-check] [^qa-metrics]

---

## 🧬 MetricSpec format

### 🧩 Why MetricSpec
MetricSpec is a versioned, reviewable contract describing:
- inputs (datasets, logs, queries)
- computation method (SQL/Cypher/script)
- thresholds + severity rules
- produced artifacts + index values

> A MetricSpec concept is explicitly described as a way to support custom evaluation metrics and reusable computations.  
[^metric-spec]

### Example MetricSpec (YAML)
```yaml
id: graph_health.orphan_nodes
version: 1
owner: graph-maintainers
description: Detect metadata/provenance nodes with no inbound/outbound edges.

inputs:
  neo4j:
    cypher: queries/graph/orphan_nodes.cypher
  baseline:
    index_csv: docs/reports/qa/graph_health/index.csv

outputs:
  artifacts:
    - orphan_nodes.csv
    - summary.md
  index_fields:
    - orphan_nodes_count

thresholds:
  warn:
    orphan_nodes_delta_pct: 5
  fail:
    orphan_nodes_count_gt: 0

severity: warn
run:
  cadence: weekly
  schedule: "0 9 * * SUN"
```

---

## 📊 Dashboards and UI surfacing

KFM’s UI roadmap includes dashboards, live data, and simulation visualization. Metrics should be consumable by these surfaces, not trapped in CI logs.  
[^ui-dashboards]

### 🗺️ Transparency surfaces
The UI’s “Layer Info” / provenance displays are a critical trust feature:
- show **source**, **license**, and summary of preparation steps  
- a “Layer Provenance” panel can list active layers + citations  
- generated views can include automatic attribution (“Map data from USGS, processed by KFM on YYYY-MM-DD”)  
[^layer-provenance]

### 📡 Live sensor + real-time layers
Live ingestion uses watchers and immutable event updates with provenance, integrated into timeline and dashboards. Metrics should include:
- ingest latency distributions  
- anomaly rate  
- access control enforcement for sensitive live feeds  
[^live-iot] [^streaming-governance]

### ♿ Accessibility + performance
Accessibility is explicitly a priority (semantic HTML, ARIA roles, keyboard nav, high-contrast mode). Track regressions like any other quality dimension.  
[^layer-provenance] [^ui-accessibility]

> 🧠 **Design note:** Treat “a11y score” and “render latency” as first-class metrics in the same dashboard as “provenance completeness”.

---

## 🔐 Security, privacy, and ethics metrics

### 🧷 Sensitive-data handling
KFM explicitly calls for:
- sensitivity tagging  
- access control  
- location generalization (coarsening coordinates when needed)  
- license tagging + usage monitoring  
[^sensitive-data]

### 🔎 Query auditing & inference control (advanced)
Privacy doesn’t stop at raw data. Even mining outputs can leak sensitive info; query auditing and inference control are known approaches to reduce disclosure risk.  
[^query-auditing]

### 🌿 Sustainability telemetry
Governance includes sustainability monitoring (e.g., energy usage of pipelines) and may gate promotion workflows on energy report artifacts.  
[^sustainability-telemetry]

---

## ➕ Adding a new metric

### Checklist ✅
- [ ] Write a `MetricSpec` in `specs/` (versioned)
- [ ] Add computation in `queries/` or a deterministic script
- [ ] Ensure the suite writes artifacts + updates `index.csv`
- [ ] Decide gate level (hard/soft) and set thresholds
- [ ] Add/extend CI job to run it
- [ ] Add a review template entry (triage questions, owner, escalation path)
- [ ] (If applicable) link it to provenance (PROV bundle / run manifest)
- [ ] Add it to dashboard ingestion

### Reviewer questions 🧑‍⚖️
- Does this metric prevent a known failure mode?
- Is it reproducible (same inputs → same outputs)?
- Are thresholds justified (baseline + reason)?
- Does it create actionable artifacts (IDs, diffs, pointers)?
- Does it respect governance constraints (CARE, sensitive handling)?

---

## 🗃️ Reference bundles

Some project PDFs are **PDF Portfolios** (containers of many embedded documents). They are intended as a **living reference library** for implementation patterns, geospatial rendering, AI evaluation, Bayesian thinking, and multi-language stacks.

### Bundles
- `AI Concepts & more.pdf` 🧠 (AI/ML concepts, evaluation, research patterns)
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` 🗺️ (WebGL, 3D worlds, GIS foundations)
- `Various programming langurages & resources 1.pdf` 🧰 (algorithms, frameworks, spatial analysis in R, etc.)
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` 🗄️ (data architectures + Bayesian methods)

### Suggested extraction workflow (local dev)
```bash
# list embedded docs
pdfdetach -list "AI Concepts & more.pdf"

# extract all embedded docs to a folder (example)
mkdir -p docs/reference/ai_concepts
pdfdetach -saveall -o docs/reference/ai_concepts "AI Concepts & more.pdf"
```

> ✅ Keep this folder lightweight: do not commit huge extracted libraries to git unless explicitly intended (use DVC/LFS/remote storage if needed).  
[^dvc-metrics]

---

## 📘 Glossary

- **MCP**: Methods / Controls / Policies — KFM’s “how we work” layer (standards, governance, review templates).  
  [^mcp-dir]
- **Policy Gates**: CI/runtime checks that block merges or outputs if standards are violated.  
  [^policy-gates]
- **Run Manifest**: A structured JSON record of what happened in a run (inputs/outputs/tool versions/counts) plus canonical hashing.  
  [^run-manifest]
- **Evidence-first Story Node**: A story that carries machine-readable evidence manifests + PROV links so claims are auditable.  
  [^evidence-first-stories]
- **Graph Health**: A suite of checks that probes Neo4j integrity, drift, and operational safety (including backups).  
  [^graph-health-checks]

---

## 🔗 Source anchors

[^pipeline-flow]: Master pipeline flow + traceability expectations. [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

[^arch-flow]: KFM architecture flow explicitly includes governance & telemetry as the final stage. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

[^mcp-dir]: `mcp/` described as “Methods / Controls / Policies” and includes review templates and related guides. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^policy-gates]: Automated policy gates include schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity classification, provenance completeness, and an AI citation requirement. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

[^policies-as-tests]: Policies treated as additional tests; failing license checks block non-compliant datasets (FAIR/CARE alignment). [oai_citation:4‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^prov-enforcement]: Provenance enforcement mechanisms include CI policy gates and runtime Focus Mode citation blocking; plus audit trails + human override. [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^ingestion-gate]: Ingestion gate includes checksums, schema sanity checks, FAIR/CARE “lite” checks, and append-only NDJSON telemetry logging. [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^qa-metrics]: Suggested QA metrics include metadata completeness, citation coverage in AI answers, and drift monitoring for model changes. [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^run-manifest]: Run manifest + canonicalization + hashing (RFC 8785) + idempotency key pattern; manifest saved under `data/audits/<run_id>/run_manifest.json`. [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^metric-spec]: MetricSpec described as a way to define custom evaluation metrics and reusable computations tied into reporting. [oai_citation:9‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^graph-health-checks]: Graph health checks include deltas, index/constraint integrity, orphans, hub detection, schema drift, and backup verification. [oai_citation:10‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^graph-artifacts]: Graph health checks save artifacts in timestamped directories, write `summary.md`, maintain `index.csv`, and can auto-open issues on multiple failures. [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^ci-fail-closed]: CI can fail with explicit policy messages (e.g., missing PROV updates), plus security scans and reporting/alerts patterns. [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^evidence-first-stories]: Story Nodes can include citation blocks + machine-readable evidence manifests + PROV bundles for governed narratives. [oai_citation:13‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^citation-manifest-ci]: CI validation can ensure each citation in story text has a corresponding manifest entry and that references resolve. [oai_citation:14‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^ai-governance-check]: Focus Mode pipeline includes a governance check to ensure compliance, including “all claims cited,” before returning answers. [oai_citation:15‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

[^layer-provenance]: UI transparency: Layer Info shows source/license/prep summary; proposed Layer Provenance panel lists citations; generated views can auto-attribute sources. [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

[^ui-dashboards]: UI system overview includes dashboards/live data/simulations; stresses caching, limiting spatial extent, replaying last 24h, and showing uncertainties. [oai_citation:17‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

[^ui-accessibility]: Accessibility emphasis includes semantic HTML, ARIA roles, keyboard navigation, high-contrast mode. [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

[^live-iot]: Live sensor/IoT layer uses a watcher pattern and immutable updates integrated into timeline (with provenance). [oai_citation:19‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

[^streaming-governance]: Streaming governance includes NDJSON/provenance logs, anomaly flagging, access control/rate limits, and latency vs provenance tradeoffs. [oai_citation:20‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^sensitive-data]: Sensitive data handling includes location generalization, access controls, sensitivity tagging, license tagging, and usage monitoring. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^query-auditing]: Data mining outputs can leak sensitive info; query auditing/inference control are approaches to reduce disclosure risk. [oai_citation:22‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

[^council-workflow]: Council oversight workflow described as: Intake → Ethical Screening → FAIR compliance → Sustainability audit → Accessibility review → Council approval. [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^sustainability-telemetry]: Governance includes sustainability monitoring (e.g., pipeline energy usage) and may add telemetry gates requiring energy report artifacts. [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

[^oci-artifacts]: OCI artifact distribution + signing (ORAS + Cosign) proposed for integrity and rollback safety. [oai_citation:25‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

[^dvc-metrics]: DVC proposed to capture metrics from runs (e.g., new references found) as part of reproducible pipelines. [oai_citation:26‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
