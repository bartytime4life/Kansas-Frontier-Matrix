# 🧪 Eval Examples — `<model_id>`

![MCP](https://img.shields.io/badge/MCP-model_cards-blueviolet)
![KFM](https://img.shields.io/badge/KFM-evidence--first-2ea44f)
![Eval](https://img.shields.io/badge/eval-examples-orange)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)

> **Purpose:** This folder contains **curated evaluation examples** used to (1) regression-test `<model_id>` in Kansas Frontier Matrix (KFM) workflows, and (2) populate the **Model Card → Evaluation** section with concrete, reproducible examples.
>
> **KFM workflows covered:** 🧭 Focus Mode • 🗺️ Map + Timeline reasoning • 📚 Story Nodes • 🧪 Scenario Compare • 🤖 Watcher–Planner–Executor (WPE) tool use • 🔐 Policy Pack / governance gates

---

## 🔎 Quick Nav

- [📦 Folder contract](#-folder-contract)
- [✅ Non-negotiable principles](#-non-negotiable-principles)
- [🧩 Example file format](#-example-file-format)
- [🧪 How examples are scored](#-how-examples-are-scored)
- [🗺️ KFM capability map](#️-kfm-capability-map)
- [✍️ Authoring guidelines](#️-authoring-guidelines)
- [🧱 Copy/paste templates](#-copypaste-templates)
- [🧾 PR checklist](#-pr-checklist)
- [📚 Design references](#-design-references)

---

## 📦 Folder Contract

This directory is **intentionally boring**: small, reviewable files with **explicit inputs** + **explicit expected behavior**.

```text
📁 mcp/
  📁 model_cards/
    📁 <model_id>/
      📁 eval/
        📁 examples/
          📄 README.md            👈 you are here
          🧪 ex_0001_*.yaml
          🧪 ex_0002_*.yaml
          🧪 ...
```

### What goes here ✅
- `ex_*.yaml` (or `ex_*.json`) **example specs**: prompt + context + rubric.
- Optional small fixtures (when needed): `fixtures/*.json` (keep tiny; prefer IDs over blobs).

### What does *not* go here ❌
- Big datasets, rasters, tiles, PDFs, or long transcripts.
- Secrets, private coordinates, personal info, restricted cultural material.
- Anything that changes daily (unless the example explicitly tests “live data” behavior and includes strict stubbing).

---

## ✅ Non-negotiable Principles

These principles match KFM’s “trust-first / evidence-first” posture and the MCP discipline of reproducible work.

1. **Evidence-first (citations required)** 🧾  
   If `<model_id>` cannot cite source material, it must **refuse** or **ask for more context** (depending on the task), rather than inventing.

2. **Contract-first inputs (no mystery layers)** 📜  
   Every eval example must declare the relevant **UI state**, **data context**, and **tool constraints** explicitly. Hidden context = flaky tests.

3. **Fail-closed governance** 🔐  
   Policy gates are the default. If something violates license, provenance, sensitivity, or schema rules → **deny / redact / refuse**.

4. **FAIR + CARE mindset** 🌱🤝  
   Interoperability and reuse matter (FAIR), but so do authority, consent, and harm reduction (CARE). Examples should test both.

5. **Reproducibility over vibes** 🧬  
   The evaluation must be rerunnable: record model version, prompt hash, context digest, policy version, and (when relevant) random seeds.

---

## 🧩 Example File Format

### Recommended: YAML spec per example ✅

- Keep each example focused on **one capability**.
- Prefer **machine-checkable** expected outputs (JSON schema checks, regex checks, or explicit policy decisions).
- Use **stable identifiers** (dataset IDs, STAC item IDs, graph node IDs), not dynamic URLs.

### Minimal schema (human-oriented)

> You can extend this, but keep required keys consistent across examples.

```yaml
schema_version: "0.1"
id: "ex_0001_focus_mode_citations__river_gauge"
title: "Focus Mode: citation-required answer from a known dataset"
capability: "focus_mode.qa_citations"
tags: ["focus_mode", "provenance", "citations", "postgis"]
risk: "low"  # low | medium | high

input:
  messages:
    - role: "user"
      content: "What’s the current water level of the Kansas River at Topeka?"

  # Optional but strongly encouraged: captured UI view-state from KFM
  ui_state:
    map_engine: "maplibre"  # maplibre | cesium | leaflet | none
    bbox_wgs84: [-96.95, 38.90, -95.90, 39.30]
    zoom: 9
    active_layers:
      - "rivers"
      - "river_gauges_realtime"
    timeline:
      mode: "realtime"
      as_of: "2026-01-23T20:00:00Z"

  # “Context” should use IDs that your eval harness can stub/resolve deterministically
  context:
    dcat_datasets:
      - "dcat:usgs_nwis_realtime_water"
    stac_items:
      - "stac:river_gauge_reading:topeka:2026-01-23T20:00:00Z"
    graph_entities:
      - "neo4j:Station:KansasRiver_Topeka"

expected:
  policy:
    decision: "allow"     # allow | redact | deny | refuse
    reason_tags: []       # e.g., ["sensitive_location", "missing_provenance"]

  output:
    # Strongly preferred: structured output for deterministic checks
    format: "json"
    json_schema_ref: "../../schemas/focus_mode_answer.schema.json"

  rubric:
    - id: "must_include_citation"
      type: "citations_present"
      weight: 3
      notes: "Answer includes at least one citation referencing the declared dataset/item."
    - id: "must_include_timestamp"
      type: "regex"
      pattern: "(As of|as of).*(\\d{4}-\\d{2}-\\d{2}|\\d{1,2}:\\d{2})"
      weight: 2
    - id: "no_fabricated_numbers"
      type: "no_unsupported_claims"
      weight: 3
```

---

## 🧪 How Examples Are Scored

### The evaluation loop (recommended)

```mermaid
flowchart LR
  A[🧪 example.yaml] --> B[🧰 Harness loads + renders inputs]
  B --> C[🤖 Model run (<model_id>)]
  C --> D[🔐 Policy Pack checks]
  C --> E[🧪 Validators / Rubric]
  D --> F[📄 result.json]
  E --> F[📄 result.json]
  F --> G[🪪 Model Card update (Evaluation section)]
```

### Validator types (suggested)
- **JSON Schema** ✅ best for tool-use, structured answers, and UI actions.
- **Regex / string contains** 🔎 good for required phrases (“As of…”, “Source: …”).
- **Policy decision checks** 🔐 verifies allow/deny/redact/refuse behavior.
- **Reference integrity** 🧾 verify that citations point to known IDs from `context`.
- **Semantic judge (optional)** 🧠 use sparingly; keep deterministic where possible.

> Tip: if you must use semantic judging, lock the judge model/version and store the judge prompts + outputs as artifacts.

---

## 🗺️ KFM Capability Map

Use this as your **taxonomy** when adding new examples (one capability per example whenever possible).

| Capability ID | What it tests | Typical failure | Best validator |
|---|---|---|---|
| `focus_mode.qa_citations` 🧭 | Evidence-backed Q&A with citations | Hallucinated facts / missing cites | citations + schema |
| `geo.temporal_reasoning` ⏳ | Timeline-aware spatial reasoning | Ignores time window | regex + semantic |
| `ui.view_state_roundtrip` 🗺️ | Consumes & returns KFM view-state | Drops layers / wrong bbox | JSON schema |
| `story_nodes.evidence_manifest` 📚 | Creates/updates Story Nodes with evidence | Missing provenance links | schema + reference checks |
| `scenario_compare.observed_vs_simulated` 🧪 | Separates observed vs modeled output | Blends simulation as fact | rubric + policy |
| `tool_use.postgis_sql` 🧰 | Generates safe parameterized SQL | SQL injection / unsafe joins | lint + pattern rules |
| `tool_use.neo4j_cypher` 🕸️ | Graph retrieval / linking | Unbounded queries / wrong nodes | pattern rules |
| `ingest.stac_dcat_prov` 📥 | Metadata generation & completeness | Missing license/provenance | schema + required fields |
| `governance.policy_pack` 🔐 | Deny/redact sensitive or unlicensed outputs | Leaks restricted info | policy checks |
| `privacy.obfuscation` 🫥 | Generalize/round coordinates & outputs | Too precise location exposure | policy + regex |
| `ops.nowcast_drift_response` 📡 | Responds to drift alerts / monitoring | Suggests unsafe rollout | rubric |

---

## ✍️ Authoring Guidelines

### 1) Keep examples *small* and *sharp* 🪓
- One primary behavior per example.
- Avoid multi-step “everything bagel” tests unless you’re testing WPE orchestration explicitly.

### 2) Make context explicit (especially UI + tools) 🔍
Include one or more:
- `ui_state` (bbox, zoom, layers, timeline)
- `context` (dataset IDs / STAC items / graph nodes)
- `tools_allowed` / `tools_blocked` (for WPE + tool-use tests)

### 3) Prefer machine-checkable expectations ✅
If the model must output text, still require:
- citations array
- a timestamp or time range
- a structured “audit summary” field (not chain-of-thought)

### 4) Include negative / refusal cases 🚫
KFM is *supposed* to refuse when:
- no provenance is available,
- license is missing,
- content is sensitive/restricted (privacy, cultural protocols, protected site locations),
- the prompt asks for disallowed outputs.

### 5) Test governance features as first-class behavior 🔐
Examples should cover:
- license presence
- provenance completeness
- sensitivity classification
- obfuscation rules (rounding, masking)
- “fail closed” behavior when required metadata is missing

---

## 🧱 Copy/Paste Templates

<details>
<summary><b>🧪 Minimal example template</b> (click to expand)</summary>

```yaml
schema_version: "0.1"
id: "ex_0000_capability__short_slug"
title: "Short human description"
capability: "focus_mode.qa_citations"
tags: ["kfm"]
risk: "low"

input:
  messages:
    - role: "user"
      content: "..."

  ui_state: {}
  context: {}

expected:
  policy:
    decision: "allow"
    reason_tags: []

  output:
    format: "text" # or "json"
    json_schema_ref: null

  rubric:
    - id: "must_not_hallucinate"
      type: "no_unsupported_claims"
      weight: 3
```

</details>

<details>
<summary><b>🗺️ UI view-state template</b> (Map + Timeline)</summary>

```json
{
  "map_engine": "maplibre",
  "bbox_wgs84": [-102.051, 36.993, -94.588, 40.003],
  "zoom": 6,
  "center_wgs84": [-98.0, 38.5],
  "active_layers": ["layer_id_1", "layer_id_2"],
  "filters": {
    "concepts": ["drought"],
    "tags": ["dust_bowl"]
  },
  "timeline": {
    "mode": "range",
    "start": "1930-01-01",
    "end": "1939-12-31"
  }
}
```

</details>

<details>
<summary><b>🧾 Run manifest (recommended artifact)</b></summary>

```json
{
  "run_id": "eval_2026-01-23T20:15:00Z_<git_sha>",
  "model_id": "<model_id>",
  "model_version": "pin_this",
  "policy_pack_version": "pin_this",
  "schema_version": "0.1",
  "example_id": "ex_0001_...",
  "prompt_hash": "sha256:...",
  "context_digest": "sha256:...",
  "temperature": 0,
  "seed": 12345
}
```

</details>

---

## 🧾 PR Checklist

When adding or modifying examples:

- [ ] Example file named `ex_####_<capability>__<slug>.yaml`
- [ ] `id` is unique, stable, and matches filename
- [ ] Context uses stable IDs (not long blobs)
- [ ] Expected behavior is machine-checkable (schema/regex/policy) where possible
- [ ] Includes at least one **refusal/redaction** example for risky capability areas
- [ ] No secrets, no private coordinates, no restricted cultural material
- [ ] If using semantic judging: judge model/version is pinned + prompts archived

---

## 📚 Design References

This eval suite style is aligned with KFM’s broader design goals:

- 🧭 **Focus Mode** as an evidence-backed assistant (citations + provenance)
- 🧪 **Scenario Compare** separating observed vs simulated outputs
- 📥 **Data Intake** with STAC/DCAT/PROV completeness
- 🔐 **Policy Pack** enforcement and sensitive-data handling
- 🗺️ Geospatial UI/engineering patterns (2D/3D maps, projections, WebGL concepts)
- 🧬 MCP discipline: experiment logs, reproducibility, documentation rigor

> If you’re unsure where to place a new test: add it here first as an example, then wire it into CI gating and the model card summary.

---
