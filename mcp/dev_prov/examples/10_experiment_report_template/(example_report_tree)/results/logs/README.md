# 🧾 Experiment Logs (`results/logs/`)

![PROV](https://img.shields.io/badge/PROV-provenance--first-success)
![Format](https://img.shields.io/badge/format-NDJSON%20%7C%20JSON--LD-informational)
![Audit](https://img.shields.io/badge/audit-traceable%20runs-blue)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)

> 🧠 **Goal:** make every experiment run *reproducible, auditable, and explainable* — “receipts included.”  
> KFM treats *all data* and *all derived outputs* as untrusted until validated + cataloged, and logging is part of that contract.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧭 Where this fits in the KFM pipeline

KFM enforces a strict “no skipping stages” pipeline: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**. Logs in this folder should help you prove you followed the ordering and didn’t bypass trust boundaries.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ What belongs in `results/logs/`

Store **run-time evidence** here — the stuff you’d need to debug, reproduce, audit, or defend the result later:

### 📌 Core run trace (recommended minimum)
- **`telemetry.ndjson`** — structured event stream (append-only JSON Lines / NDJSON)
- **`stdout.log` / `stderr.log`** — raw process output (captured once; don’t edit)
- **`run_manifest.json`** — the “ledger” of the run (who/what/when/inputs/outputs/tools) with integrity hash
- **`policy/`** — governance gates + policy decision logs (OPA/Conftest output)
- **`prov/`** — provenance bundle export (PROV JSON-LD or equivalent)
- **`checksums.sha256`** — hashes for log artifacts (and optionally all result artifacts)

KFM explicitly calls for **append-only telemetry logging** during ingest/pipeline runs (e.g., “fetched X bytes from URL Y … outcome=success”), stored as NDJSON.  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🧩 Optional (but powerful) add-ons
- **`ui/`** — UI interaction + performance traces (especially if you’re testing map layers, provenance UI, etc.)
- **`ai/`** — AI-related run telemetry (drift checks, evaluation summaries, redacted prompt traces)
- **`perf/`** — profiler outputs (CPU, memory, GPU), FPS traces for WebGL map scenes
- **`dev_prov/`** — developer provenance events (CI, PR checks, review steps) as a structured feed

Observability is a first-class system concern (correlation/request IDs, metrics, traces, and “Focus telemetry”), so logs should carry those identifiers when relevant. 

---

## 🚫 What does *not* belong here

- ❌ Final figures, tables, dashboards (those go in other `results/` folders)
- ❌ Raw datasets (those belong in the governed data lifecycle, not ad-hoc logs)
- ❌ Secrets, tokens, API keys, or unredacted PII  
  - KFM governance can include **policy-as-code** checks that block secrets from being committed and “fail closed” in CI.  [oai_citation:3‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- ❌ “Mystery logs” with no `experiment_id` / `run_id` / timestamps

> [!IMPORTANT]
> If you’re doing anything user-facing (UI tests, Focus Mode tests, query logs), treat logs as potentially sensitive. Privacy- and access-aware audit trails are part of responsible data practice.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗂️ Recommended folder layout (per-run isolation)

Use a **run-per-folder** layout so that logs are self-contained and easy to diff.

```text
📁 results/
  📁 logs/
    📄 README.md
    📁 runs/
      📁 2026-01-22T013045Z__EXP-010__run-7f3a1c/
        📄 run_manifest.json
        📄 telemetry.ndjson
        📄 stdout.log
        📄 stderr.log
        📄 checksums.sha256
        📁 policy/
          📄 opa_decisions.ndjson
          📄 conftest_report.json
        📁 prov/
          📄 prov_bundle.jsonld
        📁 ui/
          📄 ui_events.ndjson
          📄 webgl_perf.json
        📁 ai/
          📄 drift_eval.json
          📄 focus_telemetry.ndjson  # redacted
```

**Naming convention suggestion:**

`<ISO8601>__<experiment_id>__<run_id>/`

This makes logs sortable and easy to locate. Your `run_id` should match whatever the pipeline uses as the unique identifier.

---

## 🧾 Run manifest contract (what “good” looks like)

A Run Manifest is a structured JSON record of the run — including:
- `run_id`, `run_time`
- `idempotency_key`
- `canonical_digest` (hash of canonicalized manifest)
- `source_urls`, `tool_versions`, summary counts, errors, etc.

KFM’s design notes describe canonicalizing the manifest (RFC 8785) and hashing with SHA-256 to produce a stable digest used as an idempotency key and immutable run identifier.  [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> [!TIP]
> Treat `run_manifest.json` as the *index* into everything else. Your report should link to it first.

---

## 📦 Log formats we expect

### 1) NDJSON telemetry (`*.ndjson`)
- One JSON object per line
- Append-only (don’t “rewrite history” — append corrections as new events)
- Easy to stream and grep
- Matches KFM’s ingest telemetry pattern  [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Suggested event fields (template):**
- `ts` (ISO8601)
- `level` (`debug|info|warn|error`)
- `experiment_id`
- `run_id`
- `component` (`etl|catalog|graph|api|ui|focus|policy|ci`)
- `event` (stable name: `etl.extract.start`, `policy.opa.decision`, etc.)
- `message` (human hint)
- `metrics` (numbers)
- `artifacts` (paths/digests)
- `prov` (optional: activity/entity IDs)
- `git` (commit, branch)
- `correlation_id` / `request_id` (if applicable) 

**Example telemetry line:**
```json
{"ts":"2026-01-22T01:30:45Z","level":"info","experiment_id":"EXP-010","run_id":"run-7f3a1c","component":"etl","event":"etl.extract.fetch","source_url":"https://example.org/data.csv","bytes":184233,"sha256":"...","outcome":"success","prov":{"activity":"kfm:prov:activity/run-7f3a1c#extract"}}
```

### 2) Provenance bundles (`prov/*.jsonld`)
KFM relies on PROV-O lineage bundles as boundary artifacts for trust and traceability.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) Policy outputs (`policy/*`)
KFM governance is designed to be enforced through automated policy gates (OPA/Conftest), including secret scanning and metadata requirements. Logs should capture **inputs → decision → reason**.  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

---

## 🧪 AI + Focus Mode logs (special handling)

KFM’s AI system includes **drift monitoring** and **prompt security controls**; those outputs belong here (as summaries), but raw prompts/contexts must be handled carefully. 

**Recommended pattern:**
- ✅ Store **evaluation summaries** (metrics, pass/fail, dataset IDs)
- ✅ Store **redacted prompt traces** (hashes, token counts, citation IDs)
- ❌ Don’t store raw user text unless explicitly approved & classified

---

## 🗺️ UI & map experiments: provenance + performance logs

The UI design includes **Layer Info** and a **Provenance Panel** (including “export attributions + provenance”). UI experiments should log:
- layer toggles / filters / time slider changes
- provenance panel opens + export events
- FPS + tile load timing (esp. WebGL scenes)

These UI provenance features are explicitly described as a first-class UI affordance. 

---

## 🧠 Dev provenance (`dev_prov`) for experiment runs

This is an **experiment report template** inside `mcp/dev_prov/…`, so we treat development actions as provenance too:

- PR/CI events can be represented as structured provenance (JSON-LD) and integrated into the graph.
- Capturing “who reviewed what, which checks ran, which artifacts were produced” makes experiments defensible.

KFM’s proposals explicitly describe **GitHub PR → PROV Graph Integration**, ingesting PR events as structured provenance so changes and reviews become traceable graph facts.  [oai_citation:9‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

**Suggested files:**
- `dev_prov/events.ndjson` (CI + PR + review events)
- `dev_prov/prov_bundle.jsonld` (optional PROV view)
- `dev_prov/checks/` (test reports, lint outputs)

---

## 🔐 Redaction + governance checklist (before committing logs)

- [ ] No secrets (keys/tokens) — policy should catch common patterns, but don’t rely on it alone.  [oai_citation:10‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] No unapproved PII / sensitive content (or it’s properly classified + stored privately)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Every log file includes `experiment_id` and `run_id`
- [ ] `run_manifest.json` exists and links to inputs/outputs
- [ ] `checksums.sha256` updated
- [ ] Provenance bundle exists for any derived dataset/model that matters (PROV is not optional in an evidence-first system)  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!NOTE]
> For large artifacts/logs, prefer “pointer + receipt + checksum” patterns (don’t bloat the repo). The KFM intake guide explicitly supports pointer/receipt approaches for large external files.  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧰 Practical tips (debugging & parsing)

### Quick CLI patterns
```bash
# Find errors quickly
rg '"level":"error"' results/logs/runs/**/telemetry.ndjson

# Inspect last 50 events
tail -n 50 results/logs/runs/**/telemetry.ndjson | jq

# Compare two runs (manifest first)
diff -u runs/<runA>/run_manifest.json runs/<runB>/run_manifest.json
```

### Python pipeline logging
Structured logging is encouraged — even “debug statements / logging” are called out as a practical necessity in geospatial automation workflows.  [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🔎 How logs connect back to the experiment report

Your report should be able to answer:
- What question did we test?
- What changed between runs?
- What data/code/config produced these outputs?
- Can someone reproduce it?

The MCP/Scientific Method guidance explicitly requires a **data logging process**, traceability via IDs/timestamps, and linking results back to the exact procedure and inputs.  [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

If you maintain an experiment-level traceability matrix (highly recommended), you can link:
`Experiment ID → hypothesis/feature → code version → data version → result reference`.  [oai_citation:16‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 🌌 “Use all project files” — how these logs support KFM’s broader scope

KFM experiments aren’t only ETL. This logs template supports work across:
- 🗺️ Geospatial pipelines + WebGL map UIs
- 🤖 AI & Focus Mode experiments (drift/evals)
- 🧱 Governance + policy gates
- 🧬 “Scientific method” style investigations with reproducible receipts
- 🕰️ 4D digital twins + AR overlays (prototype experiments need performance + provenance logs)

KFM’s future concepts include “4D digital twins,” “interactive 3D Kansas,” and AR overlays — all of which benefit from robust logging of performance + provenance and simulation inputs/outputs.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📚 Project source pack (documents informing this template)

These are the KFM docs/resources this README is aligned to:

- **KFM data contracts & audit emphasis**: “don’t trust the data… data contract… logging for audit”  [oai_citation:18‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Data intake telemetry + NDJSON pattern**  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Observability / correlation IDs / Focus telemetry** 
- **Policy-as-code governance gates (OPA/Conftest)**  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **Run manifest + canonical digest hashing**  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **UI provenance panel + export attributions** 
- **AI drift monitoring + prompt security** 
- **Dev provenance / PR→PROV integration**  [oai_citation:22‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- **Scientific Method + experiment log rigor**  [oai_citation:23‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- **Privacy + auditing considerations**  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Geospatial workflow logging reminders**  [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### 📦 Resource bundles (PDF portfolios)
Some provided resources are packaged as PDF portfolios (open in Acrobat for the embedded docs):
- AI Concepts & more (portfolio)  [oai_citation:26‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- Maps / Google Maps / Virtual Worlds / WebGL (portfolio)  [oai_citation:27‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Various programming languages & resources (portfolio)  [oai_citation:28‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- Data management / data science / Bayesian methods (portfolio) 

---

## 📎 Direct file links (workspace)
(Convenience links to the project PDFs referenced across this template.)
-  [oai_citation:29‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
-  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
-  [oai_citation:31‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
-  [oai_citation:32‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

---
