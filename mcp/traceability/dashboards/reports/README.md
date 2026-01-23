# 📊 Traceability Dashboards & Reports (MCP)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-blue)
![Traceability](https://img.shields.io/badge/traceability-PROV%20%7C%20STAC%20%7C%20DCAT-8A2BE2)
![Artifacts](https://img.shields.io/badge/artifacts-run__manifest%20%7C%20telemetry%20%7C%20reports-success)
![Status](https://img.shields.io/badge/status-WIP-yellow)

> 📍 **You are here:** `mcp/traceability/dashboards/reports/README.md`

KFM’s UI promise is that **every visualization is linked to source data + metadata**—so users can trace “the map behind the map.” [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
This folder is where the **auditable artifacts** live that make that promise measurable, enforceable, and reviewable. ✅

---

## 🧭 Quick Navigation

- [🎯 What lives here](#-what-lives-here)
- [🧱 Design constraints](#-design-constraints)
- [🗂️ Folder layout](#️-folder-layout)
- [🧾 Report contract](#-report-contract)
- [🧪 Report types](#-report-types)
- [🔁 Generation workflow](#-generation-workflow)
- [🔐 Governance & safety](#-governance--safety)
- [➕ Add a report](#-add-a-report)
- [📚 Project references](#-project-references)

---

## 🎯 What lives here

### ✅ Reports (this folder)
**Reports** are **versioned, append-only** artifacts produced by CI, QA checks, pipelines, or governance processes. They are:
- **Human-readable** (Markdown summaries)
- **Machine-readable** (JSON/CSV for dashboards + automation)
- **Trace-linked** (tie back to provenance + run manifests + telemetry)

### 📈 Dashboards (consumers of reports)
**Dashboards** (web UI panels, maintainer consoles, QA boards) are *views* powered by report artifacts + telemetry. The UI roadmap explicitly calls out **dashboards + live data** as a future extension [oai_citation:1‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) and also describes real-time layers and charting flows that still remain provenance-governed [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj).

> [!NOTE]  
> This directory is the **canonical, file-based source of truth** for “what happened, when, with which inputs, under which policies, producing which outputs.”

---

## 🧱 Design constraints

These are the “non-negotiables” that shape every report stored here:

1. **Provenance-first, evidence-first**
   - KFM’s design is **provenance-first**: every output is traceable; there are no black boxes [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj).
   - Pipelines are deterministic, config-driven, and designed to keep raw input immutable [oai_citation:4‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj).

2. **Contract-first (“no mystery layers”)**
   - KFM adopts a **contract-first** approach: each dataset has a metadata JSON contract and the system avoids “mystery layers,” enabling automated attribution/citations. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

3. **Focus Mode citations are a hard gate**
   - Focus Mode is explicitly a **hard gate**: it only uses provenance-linked content and refuses otherwise [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU).

4. **Policy-as-code (Policy Pack) + CI gates**
   - Governance rules are enforced via a Policy Pack (OPA/Rego + Conftest) [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) and automated policy gates (schema + STAC/DCAT/PROV completeness + licensing + sensitivity + provenance completeness) are intended to fail closed [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC).

5. **Telemetry is append-only + dashboard-ready**
   - Telemetry logging is an **append-only NDJSON event stream** and is explicitly called out as input for dashboards and audits [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj).

6. **Observability = logs + metrics + traces**
   - Architecture includes **observability and logging** to monitor performance and policy violations, maintaining an audit trail [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC).

7. **MCP expects traceability artifacts**
   - Design audit calls out that MCP’s promise is end-to-end traceability and asks for **model cards + experiment tracking + modular docs** [oai_citation:11‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH).

8. **Report artifacts should be verifiable**
   - Additional proposals include **run manifests** (with hashes/refs) and distributing/verifying artifacts via OCI (ORAS) + Cosign signatures [oai_citation:12‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:13‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T).

9. **Ethics + cultural protocols matter**
   - Innovative concepts explicitly include **cultural protocol mapping** + CARE/sensitivity-aware governance for datasets [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC).

---

## 🗂️ Folder layout

Recommended structure (append-only, time-bucketed, report-type grouped):

```text
mcp/traceability/dashboards/reports/
├─ 📌 README.md
├─ 🧬 _schemas/
│  ├─ report.schema.json
│  ├─ run_manifest.schema.json
│  └─ telemetry_event.schema.json
├─ 🧩 _templates/
│  ├─ summary.template.md
│  ├─ report.template.json
│  └─ dashboard_panel.template.json
├─ ✅ qa/
│  └─ graph_health/
│     └─ 2026-W04/
│        ├─ report.json
│        ├─ summary.md
│        ├─ index.csv
│        ├─ metrics.json
│        └─ artifacts/
├─ 🛡️ governance/
│  ├─ policy_pack/
│  │  └─ 2026-01-23/
│  │     ├─ report.json
│  │     ├─ summary.md
│  │     └─ violations.json
│  └─ licensing_sensitivity/
│     └─ 2026-01-23/
├─ 🧾 provenance/
│  ├─ coverage/
│  │  └─ 2026-01/
│  └─ chain_integrity/
│     └─ 2026-01/
├─ 🤖 ai/
│  ├─ citations_coverage/
│  │  └─ 2026-01/
│  └─ governance_ledger_rollups/
│     └─ 2026-01/
└─ 📈 telemetry/
   ├─ pipeline_runs/
   │  └─ 2026-01-23/
   └─ energy/
      └─ 2026-01/
```

> [!TIP]  
> If you also publish rendered, public-facing pages under `docs/reports/...`, treat this folder as the **canonical artifact store** and `docs/reports/` as a rendered mirror (copy/symlink at publish time). The “Weekly Graph Health Check” proposal explicitly targets `docs/reports/qa/graph_health/...` [oai_citation:15‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T).

---

## 🧾 Report contract

Every report run should produce (minimum):

1. **`report.json`** ✅ machine-readable contract (dashboards/automation)
2. **`summary.md`** 📝 human-readable narrative (MCP/scientific-method friendly)
3. Optional but common:
   - `metrics.json` (time-series friendly metrics)
   - `index.csv` (dashboard ingest, pivot-ready)
   - `tables/*.csv` (detail tables)
   - `artifacts/*` (supporting evidence, screenshots, query logs)

### `report.json` minimum fields (recommended)
This contract intentionally links to pipeline provenance/telemetry and aligns with run manifest best practices:

```json
{
  "report_id": "qa.graph_health",
  "report_version": "1.0",
  "generated_at": "2026-01-23T12:34:56Z",
  "period": { "type": "weekly", "bucket": "2026-W04" },

  "run": {
    "run_id": "run_2026-01-23T12-00-00Z_abc123",
    "git_commit": "abcdef123456",
    "config_hash": "sha256:...",
    "input_hashes": { "stac_items": "sha256:...", "dcat": "sha256:..." },
    "output_hashes": { "report_json": "sha256:...", "summary_md": "sha256:..." }
  },

  "refs": {
    "run_manifest_ref": "data/audits/<run_id>/run_manifest.json",
    "telemetry_ref": "telemetry/pipeline.ndjson",
    "policy_ref": "governance/policy_pack/<bucket>/violations.json",
    "provenance_ref": "data/provenance/<bundle>.jsonld"
  },

  "results": {
    "status": "pass",
    "highlights": ["..."],
    "metrics": { "node_count": 0, "edge_count": 0 }
  },

  "integrity": {
    "canonicalization": "RFC8785",
    "signature": "cosign://..."
  }
}
```

**Why so strict?**  
Because we want dashboards to be *provably grounded*, not vibes-based—aligned with KFM’s evidence-first and policy-gated design [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) and with proposed run manifest + signature patterns [oai_citation:17‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:18‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T).

### Append-only rule ✅
Reports should never be overwritten. If you must re-run:
- create a new `run_id`, or
- add a suffix folder (e.g., `2026-W04/rerun-02/`).

This aligns with MCP/scientific-method discipline (versioned outputs, no overwriting raw data). [oai_citation:19‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🧪 Report types

A practical set of report families that directly match the project docs:

| Family 🧩 | Report Type | Typical Outputs | Why it exists |
|---|---|---|---|
| ✅ QA | `qa/graph_health` | `summary.md`, `index.csv`, `metrics.json` | Weekly “graph integrity” checks and trend tracking [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) |
| 🛡️ Governance | `governance/policy_pack` | `violations.json`, `summary.md` | Policy-as-code enforcement (OPA + conftest) [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| 🧾 Provenance | `provenance/coverage` | `% coverage`, missing refs tables | Measure “no mystery layers” compliance [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| 🤖 AI | `ai/citations_coverage` | coverage metrics, refusal counts | Validate Focus Mode “hard gate” behavior [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| 📈 Ops | `telemetry/pipeline_runs` | rollups per run_id | Dashboard fuel: append-only NDJSON telemetry [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| 🌱 Sustainability | `telemetry/energy` | energy/carbon estimates | OpenTelemetry + energy monitoring proposals [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| 🧭 UI Trust | `ui/attribution_exports` | attribution bundles | Exported views should “carry credits” [oai_citation:26‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |
| 🧑‍🤝‍🧑 Community | `community/verification` | voting/flags rollups | Supports community verification + data health concepts [oai_citation:27‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) |

### SLO tracking (recommended)
The roadmap proposes measurable goals that belong in dashboards:
- **95%** of pipeline runs have full provenance & validation metadata
- **99%** of AI answers include citations and provenance links [oai_citation:28‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

Store monthly rollups under `telemetry/slo/YYYY-MM/`.

---

## 🔁 Generation workflow

### High-level flow (traceability chain)
```mermaid
flowchart LR
  A[🧱 Sources] --> B[📥 Ingestion / ETL]
  B --> C[🗃️ data/catalog (STAC/DCAT)]
  B --> D[🧾 data/provenance (PROV)]
  B --> E[📈 telemetry (NDJSON / traces)]
  C --> F[🧠 Knowledge Graph (Neo4j)]
  D --> F
  E --> G[📊 Reports (this folder)]
  F --> G
  G --> H[🖥️ Dashboards / UI Panels]
  F --> I[🤖 Focus Mode (citations hard gate)]
  I --> G
```

### “Evidence packaging” (future-forward but designed-in)
The proposal set includes:
- `run_manifest.json` per run (hashes, refs, config, inputs/outputs) [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- optional distribution as OCI artifact via ORAS and signature verification via Cosign [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

That maps cleanly to this folder: **reports are artifacts**; manifests prove integrity; dashboards visualize status.

### DevOps → PROV (bonus power)
Latest Ideas proposes mapping PR events into PROV-O so development history becomes queryable provenance [oai_citation:31‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe).  
That implies a report family like:

```text
governance/devops_prov/
  2026-01/
    report.json
    summary.md
    pr_activity.csv
```

---

## 🔐 Governance & safety

### Focus Mode rules apply to reports too
If a report claims a fact, it must link to the evidence (or state uncertainty). That matches the Focus Mode rule that provenance-linked content is mandatory and refusal is expected when evidence is missing [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU).

### Sensitivity & cultural protocol awareness
Some datasets/layers may have access restrictions, CARE-based controls, or cultural protocols [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC).
**Rule of thumb:**
- ✅ Public rollups → okay in repo
- 🔒 Restricted details → keep out of repo or store encrypted / access-controlled

### Telemetry hygiene
Telemetry is for auditability + dashboards, not for leaking secrets. Keep it minimal, hashed where possible, and policy-reviewed (aligned with governance concepts in intake + policy pack docs). [oai_citation:34‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## ➕ Add a report

Use this checklist when introducing a new report type:

- [ ] Define **objective** (what decision does this report support?)
- [ ] Define **inputs** (STAC/DCAT IDs, graph queries, telemetry streams)
- [ ] Define **policy expectations** (what should fail the build?)
- [ ] Implement **report.json** contract + **summary.md** template
- [ ] Ensure **append-only** output (no overwrites) [oai_citation:36‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- [ ] Add CI job (scheduled, PR-gated, or both)
- [ ] Add dashboard consumer panel (UI / maintainer dashboard)
- [ ] Add/extend schemas under `_schemas/`

> [!TIP]  
> If you don’t know where to start, start with QA: **graph health checks** already have a proposed cadence and output structure [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T).

---

## 📚 Project references

This README is synthesized from the project’s design + protocol docs. 🔗  
Use these as the authoritative sources for decisions in this folder:

### Core KFM system docs 🧭🌾
- **Comprehensive Technical Documentation** (contract-first, no mystery layers)  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Comprehensive Architecture, Features, and Design** (policy gates, observability)  [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Data Intake – Technical & Design Guide** (provenance-first intake, NDJSON telemetry)  [oai_citation:40‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **AI System Overview** (auditability, governance ledger concepts)  [oai_citation:41‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **UI System Overview** (dashboards, provenance UX, “map behind the map”)  [oai_citation:42‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- **Latest Ideas & Future Proposals** (Policy Pack, OpenTelemetry/energy, PROV devops)  [oai_citation:43‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

### Traceability + governance proposals ✅🛡️
- **Additional Project Ideas** (graph health checks, run manifests, ORAS/Cosign packaging)  [oai_citation:44‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Innovative Concepts** (data health dashboard + cultural protocol mapping)  [oai_citation:45‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### MCP + documentation protocols 🧪📝
- **Design Audit – Gaps & Enhancements** (MCP traceability expectations: model cards, experiment logs)  [oai_citation:46‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
- **Open-Source Mapping Hub Design** (mcp/ experiments + run manifests concept)  [oai_citation:47‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
- **Scientific Method / Master Coder Protocol Documentation** (traceability matrix, versioned outputs)  [oai_citation:48‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
- **MARKDOWN_GUIDE_v13** (Focus Mode rules + repo doc structure)  [oai_citation:49‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- **Comprehensive Markdown Guide** (doc best practices)  [oai_citation:50‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### Analytics + implementation support 📈🧰
- **Data Mining Concepts & Applications** (methods for metrics + validation analytics)  [oai_citation:51‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
- **Python Geospatial Analysis Cookbook** (geospatial analytics patterns)   

### 📦 Reference libraries (PDF portfolios)
These are “bundles” of embedded resources useful for implementing dashboards/ETL/visualization:
- **AI Concepts & more (PDF portfolio)**  [oai_citation:52‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- **Data Management / CI-CD / Architecture (PDF portfolio)**  [oai_citation:53‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- **Maps / WebGL / GIS / Visualization (PDF portfolio)**  [oai_citation:54‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- **Programming Languages & Resources (PDF portfolio)**  [oai_citation:55‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  

> [!NOTE]  
> PDF portfolios may require special tools (e.g., Acrobat) to browse embedded documents. In dev environments, tools like `pdfdetach -list` can enumerate embedded files.

---

## 🏁 Bottom line

If it’s not in:
- **provenance** (PROV/STAC/DCAT),
- **telemetry** (append-only events),
- **policy results** (policy pack / CI gates), or
- **report artifacts** (this folder),

…then it doesn’t “exist” for traceability. That’s how we keep KFM trustworthy. 🧭✅
