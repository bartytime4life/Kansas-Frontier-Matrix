---
title: "KFM Tool — AI Drift Monitor"
path: "tools/ai/drift/docs/README.md"
version: "v0.1.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Tool Documentation"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:tools:ai:drift:readme:v0.1.0"
semantic_document_id: "kfm-tool-ai-drift-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:tools:ai:drift:readme:v0.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "speculative_additions"
  - "infer_sensitive_locations"
  - "generate_policy"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Tool — AI Drift Monitor

## 📘 Overview

This directory documents the **AI Drift Monitor** capability for Kansas Frontier Matrix (KFM).

**Goal:** detect and report “drift” (meaningful change over time) in **AI-adjacent pipeline outputs** and the **data distributions that those outputs depend on**, so downstream surfaces (APIs, UI, Story Nodes, Focus Mode) remain **evidence-first**, **contract-first**, and **provenance-anchored**.

This README is written as a **contract + operating guide**. Where an implementation detail is not verifiable from the repository snapshot available to this author, it is labeled **not confirmed in repo** and kept as a recommendation rather than a claim.

### Canonical references

- `docs/MASTER_GUIDE_v12.md` (pipeline ordering + invariants)
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` (this doc’s governing structure)
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` (story/focus invariants)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (if drift results become API-visible)
- *Comprehensive Guide to Markdown in Programming and Documentation.pdf* (style + Markdown hygiene)
- *KFM 1.0 System Documentation (PDF)* — **not confirmed in repo** (recommended path: `docs/architecture/`)

### What “drift” means in KFM

Drift can occur at multiple boundaries. This tool’s scope is to detect, quantify, and record drift in a way that is:

- **replayable** (same inputs ⇒ same report),
- **auditable** (PROV-linked, with stable IDs),
- **safe** (no sensitive location inference; honors redaction/generalization),
- **actionable** (clear “OK/WARN/FAIL” signals and human-readable summary).

Common drift categories (non-exhaustive):

1. **Input / dataset drift**
   - Shifts in incoming source distributions (e.g., new imagery characteristics, new text OCR noise profile).
2. **Feature / extraction drift**
   - Changes in extracted entities, embeddings, classifications, topic tags, etc., given “equivalent” inputs.
3. **Model / prompt drift**
   - Changes in outputs tied to model version, prompt templates, or decoding parameters.
4. **Narrative-support drift**
   - Changes in draft summaries or draft Story Node candidates produced by AI assistance (must remain opt-in and clearly labeled if surfaced).

### Non-goals

- This tool **does not** bypass KFM governance rules.
- This tool **does not** publish Story Nodes automatically.
- This tool **does not** introduce UI behavior that reads Neo4j directly (UI must remain API-contract-bound).

---

## 🗂️ Directory Layout

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 drift/
        ├── 📁 docs/
        │   └── 📄 README.md
        ├── 📁 src/                 (not confirmed in repo)
        ├── 📁 configs/             (not confirmed in repo)
        ├── 📁 schemas/             (not confirmed in repo; prefer `schemas/telemetry/`)
        └── 📁 tests/               (not confirmed in repo)
~~~

Related canonical locations (by KFM convention):

- 📁 `schemas/telemetry/` — telemetry schemas used by CI and runs (preferred home for drift-report schemas)
- 📁 `data/prov/` — PROV bundles for lineage
- 📁 `data/stac/` and 📁 `data/catalog/dcat/` — evidence/catalog bindings
- 📁 `mcp/runs/` — run logs / experiment artifacts (**preferred for drift runs if treated like analysis runs**)

---

## 🧭 Context

KFM’s core invariants include:

- **No unsourced narrative** in Focus Mode contexts.
- **Provenance is first-class** (STAC/DCAT/PROV and graph lineage).
- **Reproducibility and deterministic pipelines**.

The Drift Monitor exists to support those invariants when AI components (or AI-adjacent transforms) are introduced or evolve.

### When drift checks should run (recommended)

- **CI / PR gates**
  - If model version, prompt templates, extraction logic, schemas, or redaction rules change.
- **Scheduled drift audits**
  - Periodic runs for critical domains/datasets to detect slow distribution shifts.
- **Before publishing or promoting AI-derived artifacts**
  - Especially if drift affects anything that could surface in Story Nodes or Focus Mode.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["Processed + Catalog-ready outputs"]
    C --> D["STAC/DCAT/PROV"]
  end

  D --> G["Graph Build (Neo4j)"]
  G --> H["API Layer"]
  H --> I["UI (React/MapLibre/Cesium)"]
  I --> J["Story Nodes"]
  J --> K["Focus Mode"]

  subgraph AI["AI / Analysis Stage"]
    C --> M["AI Transforms (extraction, embeddings, summarization)"]
    M --> N["Drift Monitor"]
    N --> R["Drift Report + Telemetry Signal"]
  end

  R --> D
  R --> H
~~~

Key takeaway: drift outputs are treated as **evidence/telemetry artifacts** that can be referenced via **contracts** (schemas) and **provenance** (PROV), not as free-form narrative.

---

## 📦 Data & Metadata

### Inputs (recommended contract)

A drift run should declare *exactly what it is comparing*, including identifiers that can be resolved later.

- **Baseline bundle**
  - STAC Item IDs and/or DCAT dataset IDs
  - Reference window (time range or version pin)
- **Monitor bundle**
  - Same types of IDs, representing current/latest window/version
- **Transform identity**
  - Code version (`commit_sha`)
  - Model identifier/version (if applicable) (**not confirmed in repo** how models are identified)
  - Prompt template identifier (if applicable) (**not confirmed in repo**)

### Outputs (recommended contract)

At minimum:

1. **Machine-readable drift report** (JSON)
2. **Human-readable summary** (Markdown)
3. **Lineage record** (PROV Activity/Bundle)

Recommended canonical output placement (choose one pattern and standardize):

- Pattern A (analysis-run oriented): `mcp/runs/<run_id>/drift_report.json` (**not confirmed in repo**)
- Pattern B (data-report oriented): `data/reports/ai/drift/<run_id>/drift_report.json` (**not confirmed in repo**)

If surfaced to users, drift results should be exposed via **API contracts**, not direct file reads.

---

## 🌐 STAC, DCAT & PROV Alignment

### Evidence-first linkage

A drift report should be linkable as an **evidence artifact**:

- STAC: attach drift report as an `asset` on an Item or as a dedicated Item representing the report (preferred if drift reports are first-class evidence products).
- DCAT: reference drift reports as distributions or related resources (if externally published).
- PROV: record drift evaluation as a `prov:Activity` with:
  - `prov:used` ⇒ baseline bundle identifiers
  - `prov:used` ⇒ monitor bundle identifiers
  - `prov:wasAssociatedWith` ⇒ tool + model identity
  - `prov:generated` ⇒ drift report artifact(s)

### Drift as a “quality signal” (recommended)

Treat drift status as a quality signal that can inform:

- curator review queues,
- CI gating,
- “data freshness / model changed” warnings in audit panels (UI),
- opt-in AI sections in Focus Mode (never as unmarked fact).

---

## 🧱 Architecture

### Components (conceptual)

- **Collector**
  - Resolves baseline/monitor bundles into comparable samples.
- **Metric engine**
  - Computes drift metrics (distribution distance, frequency shifts, embedding-space shifts, label drift, etc.).
- **Evaluator**
  - Compares metrics to thresholds and assigns status (OK/WARN/FAIL).
- **Reporter**
  - Writes JSON report + Markdown summary.
- **Validator**
  - Validates report payloads against JSON Schema (prefer `schemas/telemetry/`).
- **Governance guardrails**
  - Ensures output does not leak sensitive locations; enforces redaction/generalization where required.

### Configuration (recommended shape)

~~~yaml
# not confirmed in repo: example contract proposal only

run:
  run_id: "prov:activity:<uuid-or-stable-id>"
  created_at: "2025-12-22T00:00:00Z"
  commit_sha: "<latest-commit-hash>"

compare:
  baseline:
    stac_item_ids: [ "stac:item:<id>" ]
    dcat_dataset_ids: [ "dcat:<id>" ]
    time_range: { start: "TBD", end: "TBD" }
  monitor:
    stac_item_ids: [ "stac:item:<id>" ]
    dcat_dataset_ids: [ "dcat:<id>" ]
    time_range: { start: "TBD", end: "TBD" }

metrics:
  - name: "population_stability_index"
    field: "TBD"
    warn: 0.1
    fail: 0.2
  - name: "js_divergence"
    field: "TBD"
    warn: 0.05
    fail: 0.1

governance:
  infer_sensitive_locations: false
  redact_restricted_geometry: true
  include_ai_outputs: false
~~~

### Drift report payload (recommended shape)

~~~json
{
  "schema_version": "kfm-telemetry-drift-report-v0.1.0",
  "run_id": "prov:activity:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "created_at": "2025-12-22T00:00:00Z",
  "commit_sha": "<latest-commit-hash>",
  "baseline": {
    "stac_item_ids": ["stac:item:..."],
    "dcat_dataset_ids": ["dcat:..."],
    "time_range": { "start": "TBD", "end": "TBD" }
  },
  "monitor": {
    "stac_item_ids": ["stac:item:..."],
    "dcat_dataset_ids": ["dcat:..."],
    "time_range": { "start": "TBD", "end": "TBD" }
  },
  "metrics": [
    { "name": "population_stability_index", "field": "TBD", "value": 0.12, "warn": 0.1, "fail": 0.2, "status": "warn" }
  ],
  "overall_status": "warn",
  "provenance": {
    "prov_bundle_path": "data/prov/<bundle>.json"
  },
  "notes": "Drift detected above WARN threshold for field TBD."
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How drift results should surface (recommended)

- **Curator workflow**
  - Drift reports flag areas where AI-derived drafts may need re-review.
- **Story Nodes**
  - Drift findings can be referenced as supporting evidence for “what changed,” but must not be used to fabricate narrative.
- **Focus Mode**
  - Focus Mode consumes **provenance-linked** context only.
  - Predictive or AI-generated content must be **opt-in** and include uncertainty/confidence metadata.

Recommended UX behaviors (if drift signals are surfaced):

- show a non-intrusive **audit badge** (“AI outputs changed since baseline”),
- link badge to drift report artifact IDs (STAC/DCAT/PROV),
- never replace curated narrative automatically.

---

## 🧪 Validation & CI/CD

### Minimum CI gates (align with repo standards)

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests (if drift results are graph-linked)
- API contract tests (if drift results are exposed)
- Security + sovereignty scanning gates (where applicable)

### Drift-tool PR checklist (recommended)

- [ ] Determinism: repeated run on same inputs produces identical report (except timestamps/run_id)
- [ ] Report schema exists and validates (prefer `schemas/telemetry/`)
- [ ] PROV activity recorded and points to baseline + monitor bundles
- [ ] No sensitive location inference; redaction/generalization rules honored
- [ ] No UI direct reads from Neo4j introduced (API boundary preserved)
- [ ] If surfaced externally: API contract doc + contract tests added

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers (applies strongly here)

- New AI narrative behaviors
- New telemetry signals
- New external data sources used for baselines/monitors
- Any public-facing endpoints that expose drift status

### Sovereignty safety

- Drift tooling must never “reconstruct” or infer restricted locations from partial signals.
- Any geometry used for drift evaluation must obey the same generalization/redaction rules as other pipeline products.
- Log redaction decisions and provenance, but do not log restricted coordinates.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-22 | Initial README scaffold for AI drift tool docs | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`