# ⚙️ Model Configs (`mcp/model_cards/<model_id>/configs/`)

![contract-first](https://img.shields.io/badge/contract--first-yes-success)
![policy-gated](https://img.shields.io/badge/policy--gated-OPA%20%2B%20Conftest-blue)
![evidence-first](https://img.shields.io/badge/evidence--first-citations%20required-orange)

> [!IMPORTANT]
> These configs define the **runtime + governance contract** for a specific model (`<model_id>`).  
> In KFM terms: **fail closed 🧯** → if configs are missing, invalid, or policy-denied, the model **must not run**.

---

## 🧭 Where you are

**Path:** `mcp/model_cards/<model_id>/configs/README.md`

- `../README.md` → the **Model Card** (what the model is, why we use it, limitations, evaluation notes, risk notes)
- `./` (this folder) → **how KFM is allowed to use it** (tools, retrieval, policy gates, output contracts, telemetry)

---

## 🧠 Mental model (KFM-style)

### Model Card = “Who/what/why” 📇  
- Intended use, non-goals, known limitations, evaluation results, risks, governance notes.

### Configs = “How it behaves inside KFM” 🧰  
- Focus Mode settings (retrieval + citations + redaction)
- Allowed tools + budgets
- Privacy/sensitivity handling
- Observability + audit hooks
- Optional “future flags” (AR/offline packs/story manifests/etc.)

---

## 🗂️ Recommended layout (per `<model_id>`)

> [!NOTE]
> File names here are **recommended defaults**. If your repo uses different names, keep the *same intent* and document deviations.

```text
mcp/model_cards/<model_id>/
├─ 📄 README.md                      # Model Card (human-facing)
└─ 📁 configs/
   ├─ 📄 README.md                   # (this file)
   ├─ ⚙️ model.yaml                  # provider + runtime knobs + limits
   ├─ 🧾 output_contract.yaml         # citations, formatting, refusal rules
   ├─ 🔎 retrieval.yaml               # hybrid RAG: graph + text + map context
   ├─ 🧰 tools.yaml                   # allowed tool calls + per-tool quotas
   ├─ 🛡️ privacy.yaml                 # PII/sensitivity + aggregation thresholds
   ├─ 📡 telemetry.yaml               # logging, metrics, audit trail fields
   ├─ 🧪 evals.yaml                   # eval suite config + thresholds
   ├─ 🧭 ui_context.yaml              # what UI context is passed (bbox/time/layers)
   ├─ 📁 prompts/
   │  ├─ 🧠 system.md                 # system prompt template
   │  ├─ 🧩 tool_instructions.md       # tool calling rules + tool schema reminders
   │  ├─ ✍️ style.md                  # tone + formatting rules
   │  └─ 🧷 citations.md              # citation style + constraints
   └─ 📁 policy_overrides/
      └─ 🧾 README.md                 # (optional) model-specific policy notes ONLY
```

---

## 🔒 Non‑negotiables (KFM invariants)

These are the “musts” that align with KFM’s governance + provenance architecture:

- **Evidence-first answers** 🧾  
  If the model cannot cite sources, it must **refuse** (or return a “not enough evidence” response).
- **Hybrid retrieval** 🔎  
  Prefer **structured** (graph/GIS/catalog) + **unstructured** (docs) retrieval together, not “LLM-only”.
- **Context-aware** 🗺️  
  Retrieval should respect **map viewport (bbox)**, **time slider**, and **active layers** when available.
- **Advisory-only by default** 🚦  
  Focus Mode is a guide and analyst—**not** an autonomous actor (no silent writes, no hidden actions).
- **Fail-closed governance** 🧯  
  Policy gates decide whether outputs are allowed to ship, including sensitive-data handling.
- **Traceability** 🧬  
  Every meaningful output should be loggable to an audit trail (request → evidence → policy decision → response).

---

## 🧩 Config surfaces (what each file controls)

| File | What it controls | Typical knobs |
|---|---|---|
| `model.yaml` | Provider + runtime execution | model name, temperature, max tokens, timeouts, retries, streaming |
| `retrieval.yaml` | RAG strategy | graph hops, vector top_k, dataset filters, map/time conditioning |
| `tools.yaml` | Allowed tool calls | allowlist, per-tool quotas, “read-only” vs “write” tools |
| `output_contract.yaml` | Output contract | citation requirements, refusal templates, formatting constraints |
| `privacy.yaml` | Privacy & sensitivity | PII redaction modes, aggregation thresholds, access tiers |
| `telemetry.yaml` | Audit + observability | what to log, correlation IDs, metrics, sampling, sinks |
| `evals.yaml` | Evaluation & drift | tests, thresholds, golden sets, regression rules |
| `ui_context.yaml` | UI → model context | bbox/time/layers/selected entity/story node state |

---

## 🧾 Minimal example (`model.yaml`) ✅

> [!TIP]
> Keep this config *boring* and *deterministic*. If you add “smart” logic, put it in code—then test it.

```yaml
model:
  id: "<model_id>"
  display_name: "KFM Focus Mode - <model_id>"
  provider: "openai|anthropic|local|other"
  base_model: "<provider_model_name>"
  version: "1.0.0"

runtime:
  temperature: 0.2
  max_output_tokens: 1400
  timeout_ms: 45000
  retries: 2
  streaming: true

capabilities:
  tool_calling: true
  json_mode: false
  vision: false

guardrails:
  advisory_only: true
  refuse_without_evidence: true
  citations_required: true
```

---

## 🔎 Retrieval (`retrieval.yaml`) — hybrid + map‑aware

KFM’s best answers come from combining:
- **Knowledge graph** (people/place/event relationships, ontologies, multi-hop context)
- **GIS + catalog** (PostGIS queries, STAC/DCAT metadata, dataset lineage)
- **Docs** (reports, scans, story nodes, narratives)

Recommended pattern:

```yaml
retrieval:
  strategy: "hybrid"

  budgets:
    max_sources: 12
    max_graph_hops: 3
    max_tool_calls: 8

  context:
    use_ui_bbox: true
    use_ui_time_range: true
    use_active_layers: true

  graph:
    enabled: true
    ontology_hints:
      - "CIDOC-CRM"
      - "OWL-Time"

  vector_search:
    enabled: true
    top_k: 20
    min_score: 0.25

  structured_queries:
    postgis_enabled: true
    stac_catalog_enabled: true
```

---

## 🧰 Tools (`tools.yaml`) — allowlist + quotas

> [!IMPORTANT]
> Tools are an **attack surface** and a **governance surface**.  
> Prefer **read-only tools** for Focus Mode. If you enable write tools, treat that model as *not Focus Mode*.

```yaml
tools:
  mode: "allowlist"

  allow:
    - "kfm.search_catalog"
    - "kfm.query_graph"
    - "kfm.fetch_document"
    - "kfm.spatial_query"
    - "kfm.realtime_latest_reading"

  quotas:
    kfm.query_graph: 4
    kfm.search_catalog: 2
    kfm.fetch_document: 4
    kfm.spatial_query: 2
    kfm.realtime_latest_reading: 1

  safety:
    require_request_id: true
    require_user_context: true
    deny_write_tools: true
```

---

## 🛡️ Output Contract (`output_contract.yaml`) — citations + refusal rules

This is where we encode “**no evidence, no claim**”.

```yaml
output_contract:
  citations:
    required: true
    min_citations: 1
    style: "inline|footnote"
    allow_uncited_background: false

  refusals:
    when_no_evidence: "I can’t answer that from the available sources in KFM."
    when_sensitive: "I can’t share that detail due to sensitivity rules."

  formatting:
    prefer_bullets: true
    include_assumptions: true
    include_next_steps: true
```

---

## 🔐 Privacy & sensitivity (`privacy.yaml`) — don’t leak, don’t infer

Use this to enforce:
- redaction (PII, sensitive places)
- aggregation thresholds (avoid deanonymization)
- access tiers (public vs restricted)
- safe summarization vs exact coordinates

```yaml
privacy:
  pii_redaction: "strict|balanced|off"
  location_precision:
    default: "coarse"          # e.g., county-level unless allowed
    allow_exact_for_roles:
      - "admin"
      - "research_partner"

  aggregation:
    min_group_size: 10         # k-anonymity style safeguard
    suppress_small_counts: true

  sensitivity:
    respect_dataset_classification: true
    default_classification: "public"
```

---

## 📡 Telemetry (`telemetry.yaml`) — auditability by design

Log enough to support:
- governance audits
- reproducibility (“why did it answer that?”)
- drift monitoring (model updates)

```yaml
telemetry:
  enabled: true
  log_fields:
    - request_id
    - model_id
    - model_version
    - policy_decision
    - citations_used
    - tool_calls
    - ui_context_hash
  metrics:
    - citation_coverage
    - refusal_rate
    - tool_call_rate
```

---

## 🧪 Evals (`evals.yaml`) — regression‑safe upgrades

Evals should test what KFM *cares about*:
- citation correctness & coverage
- hallucination resistance
- sensitivity redaction
- map/time conditioning
- “advisory-only” behavior (no unauthorized actions)

```yaml
evals:
  suites:
    - name: "focus_mode_citations"
      threshold: 0.95
    - name: "safety_redaction"
      threshold: 0.99
    - name: "map_context_alignment"
      threshold: 0.90

  drift:
    block_release_if_below_threshold: true
```

---

## 🚦 Change process (PR checklist) ✅

When you edit anything in `configs/`:

- [ ] Update `../README.md` (Model Card) with **what changed** and **why**
- [ ] Bump `model.yaml -> model.version`
- [ ] Run validation (schema + policy + lint)
- [ ] Run evals & attach results to PR
- [ ] Confirm citations/refusals work as expected
- [ ] Confirm privacy rules still hold
- [ ] Confirm tool allowlist/quotas still match intended access tier

---

## 🧪 “Future flags” (optional, but planned) 🚀

KFM’s roadmap includes capabilities that benefit from explicit toggles in configs:

- 🕶️ **AR / in-situ overlays** (mobile + camera-aligned experiences)
- 📦 **Offline packs** (county-level bundles with PMTiles/MBTiles + story content)
- 🧷 **Evidence manifests for story nodes** (YAML/PROV-based citations that CI can validate)
- 🧠 **Conceptual attention nodes** (user-controlled thematic “lenses” that steer retrieval)

Keep these behind a deliberate flag:

```yaml
future_flags:
  ar_enabled: false
  offline_pack_enabled: false
  story_evidence_manifest_enabled: true
  conceptual_attention_nodes_enabled: false
```

---

## 📚 Project references (design lineage) 📎

These configs are derived from the KFM architecture + AI + UI + data governance documents, plus supporting engineering guides:

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design  
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖  
- Kansas Frontier Matrix – Comprehensive UI System Overview  
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide  
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals  
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)  
- Additional Project Ideas  
- KFM_REDESIGN_BLUEPRINT_v13 (MARKDOWN_GUIDE_v13)  
- Data Mining Concepts & applications (privacy-preserving patterns)  
- KFM Python Geospatial Analysis Cookbook (GIS/remote sensing recipes + 3D notes)  
- Maps / GoogleMaps / VirtualWorlds / Archaeological / Computer Graphics / Geospatial WebGL bundle  
- AI Concepts & more (reference bundle)  
- Various programming languages & resources bundle  
- Data Management / Architectures / Data Science / Bayesian Methods bundle

> [!NOTE]
> If any of the above documents aren’t committed into the repo yet, consider adding them under `docs/references/` (or equivalent) and linking them from the root docs index.
