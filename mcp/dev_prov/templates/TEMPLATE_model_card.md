# 🧠 Model Card — {{MODEL_NAME}} (`{{MODEL_ID}}`)

![Model Card](https://img.shields.io/badge/model%20card-KFM%20template-2ea44f)
![Evidence First](https://img.shields.io/badge/evidence--first-required-0b7285)
![Provenance](https://img.shields.io/badge/PROV-required-8a2be2)
![Policy Gates](https://img.shields.io/badge/policy%20gates-OPA%2FConftest-orange)
![Human-in-the-loop](https://img.shields.io/badge/human--in--the--loop-required-6f42c1)

> [!IMPORTANT]
> **KFM Rule:** If the model cannot ground an output in evidence (STAC/DCAT/PROV, graph entities, or approved citations), it must **refuse or defer**. No “mystery facts,” no “mystery layers,” no silent assumptions.

---

## ✅ Completion Checklist (Gate to “Production”)

- [ ] **Identity** complete (IDs, versions, owners, artifact digest, signatures)
- [ ] **Intended Use** + **Out-of-Scope** documented
- [ ] **Inputs/Outputs** schemas documented (including map/time context if relevant)
- [ ] **Evidence Policy** documented (what counts as evidence; citation format; refusal rules)
- [ ] **Data & Privacy** documented (classification, sensitive handling, CARE/TK labels if applicable)
- [ ] **Evaluation** complete (metrics + geospatial + grounding + security tests)
- [ ] **Policy Pack** checks pass in CI (OPA/Rego, conftest, schema validators)
- [ ] **Deployment** documented (runtime deps, compute, caching, rate limits, rollbacks)
- [ ] **Monitoring** documented (drift/anomaly/narrative pattern detection where applicable)
- [ ] **Sign-off** complete (security + data steward + domain reviewer)

---

<details>
<summary>📑 Table of Contents</summary>

- [🧾 1. Snapshot](#-1-snapshot)
- [🎯 2. Intended Use](#-2-intended-use)
- [🧭 3. KFM Integration Points](#-3-kfm-integration-points)
- [📥 4. Inputs](#-4-inputs)
- [📤 5. Outputs](#-5-outputs)
- [🗺️ 6. Evidence & Grounding Policy](#️-6-evidence--grounding-policy)
- [🗃️ 7. Training Data / RAG Context](#️-7-training-data--rag-context)
- [🧬 8. Provenance & DevProV](#-8-provenance--devprov)
- [🧪 9. Evaluation](#-9-evaluation)
- [🔐 10. Safety, Security, Governance](#-10-safety-security-governance)
- [📈 11. Monitoring & Maintenance](#-11-monitoring--maintenance)
- [🚀 12. Deployment & Operations](#-12-deployment--operations)
- [⚠️ 13. Limitations & Known Issues](#️-13-limitations--known-issues)
- [🗓️ 14. Change Log](#️-14-change-log)
- [✅ 15. Approvals](#-15-approvals)
- [📚 Appendix A — KFM Repo / Data Layout](#-appendix-a--kfm-repo--data-layout)
- [📎 Appendix B — Schemas & Examples](#-appendix-b--schemas--examples)
- [📚 Appendix C — Project Reference Pack](#-appendix-c--project-reference-pack)

</details>

---

## 🧾 1. Snapshot

| Field | Value |
|---|---|
| **Model Name** | {{MODEL_NAME}} |
| **Model ID** | `{{MODEL_ID}}` |
| **Version** | {{MODEL_VERSION}} |
| **Stage** | {{STAGE}} |
| **Type / Role** | {{MODEL_TYPE}} |
| **Modalities** | {{MODALITY_LIST}} |
| **Provider** | {{PROVIDER}} |
| **RAG Enabled** | {{RAG_ENABLED}} |
| **Primary Domain(s)** | {{DOMAINS}} (e.g., history, environment, hydrology, agriculture, transit, documents) |
| **Primary UI Touchpoint(s)** | {{UI_TOUCHPOINTS}} (e.g., Focus Mode, Story Nodes, layer recommendations, dashboards) |
| **Primary Data Backends** | {{BACKENDS}} (Neo4j, PostGIS, object storage, search index) |
| **Artifact Digest** | `{{SHA256_DIGEST}}` |
| **Cosign Signature** | {{COSIGN_BUNDLE_OR_REF}} |
| **SBOM (SPDX)** | {{SBOM_REF}} |

**One-liner:** {{ONE_LINE_SUMMARY}}

**Longer summary:**  
{{PARAGRAPH_SUMMARY}}

---

## 🎯 2. Intended Use

### ✅ Intended Use (What it *should* do)
- {{INTENDED_USE_BULLET_1}}
- {{INTENDED_USE_BULLET_2}}
- {{INTENDED_USE_BULLET_3}}

**Primary users:** {{USERS}} (researchers, educators, curators, public, agencies, internal devs)

**KFM principle alignment (tick all that apply):**
- [ ] Evidence-first answers (citations required)
- [ ] Provenance-first publishing (every derived artifact is traceable)
- [ ] Human-in-the-loop review for anything published/featured
- [ ] Standards-first metadata (STAC/DCAT/PROV + ontologies)
- [ ] Supports 2D/3D + time (MapLibre/Cesium + timeline slider) where relevant

### 🚫 Out of Scope (What it must *not* do)
- [ ] Invent new facts, places, dates, or relationships without evidence
- [ ] Bypass classification rules or reveal restricted/sensitive locations
- [ ] Treat AI output as authoritative without citations and review
- [ ] Auto-merge/publish content to live graph/UI without human approval (unless explicitly permitted + logged)

### 🧩 Example Use Cases (KFM-flavored)
- **Focus Mode Q&A:** Answers must cite datasets/documents/graph entities; if dynamic (e.g., “current water level”), record the queried timestamp in provenance.
- **Bulk document ingestion:** OCR → entity extraction → link places/dates/people to graph; keep source excerpts for traceability.
- **Real-time watchers (e.g., GTFS-RT):** Poll feeds idempotently; emit STAC Items + DCAT dataset entries; maintain provenance for each poll cycle.
- **Bias correction & nowcasting (environment):** Deterministic correction pipeline; include parameters + QC flags + seed in PROV.
- **Narrative generation:** Produce draft narratives (Pulse Threads / Story Nodes) with evidence manifest; require curator review.

---

## 🧭 3. KFM Integration Points

> [!NOTE]
> KFM commonly blends **PostGIS (geo truth)** + **Catalogs (describe assets)** + **Graph (links context)**, and uses **UI (MapLibre/Cesium)** + **Focus Mode** as the main discovery surface.

### 🧩 Integration Surface (check all that apply)
- [ ] 🗺️ **Map UI (2D)** — MapLibre GL JS layers, filters, time slider
- [ ] 🏔️ **Map UI (3D)** — CesiumJS terrain/tiles, camera transitions
- [ ] 🧠 **Focus Mode** — evidence-backed Q&A with citations and refusals
- [ ] 📖 **Story Nodes** — guided narratives + camera/timeline transitions + dataset citations
- [ ] 🧵 **Pulse Threads** — geotagged narrative updates (detector → template → AI polish → curator review)
- [ ] 🛰️ **Raster/Vector pipelines** — COG, MVT, PMTiles, GeoParquet, etc.
- [ ] 📚 **Document ingestion** — OCR/NLP entity extraction → Neo4j linking
- [ ] ⏱️ **Real-time ingestion** — streaming-ish “many small datasets over time”
- [ ] 🧪 **Simulations** — deterministic sandbox runner (virtual clock + fixed seed) generating diff patches + PROV
- [ ] 🌐 **Federation-ready** — interoperable APIs and schema packages

### 🧱 Dependencies (KFM core)
- **Catalogs:** STAC + DCAT
- **Lineage:** W3C PROV (inputs → activities → outputs)
- **Backends:** Neo4j (context/relationships), PostGIS (spatial truth + tiles), object storage (large assets), search index (text/semantic)
- **Governance:** OPA/Rego policy packs; CI gates; classification enforcement
- **Supply chain:** SBOM + pinned digests + signed artifacts (recommended)

---

## 📥 4. Inputs

### 4.1 Input Modalities
- **User inputs:** {{USER_INPUTS}} (question text, selected feature, time range, region, filters)
- **System context:** {{SYSTEM_CONTEXT}} (active layers, viewport bbox, time slider bounds, story mode state)
- **Evidence inputs:** {{EVIDENCE_INPUTS}} (STAC/ DCAT/ PROV refs, graph entity IDs, document excerpt IDs)

### 4.2 Input Schemas (paste links or inline schemas)
- `{{SCHEMA_REF_1}}`
- `{{SCHEMA_REF_2}}`

#### Example: UI Context Payload (Map + Time + Layers)
```json
{
  "viewport": { "bbox_wgs84": [-102.05, 36.99, -94.59, 40.00], "zoom": 6.5 },
  "time": { "start": "1950-01-01", "end": "1959-12-31" },
  "active_layers": ["kfm:landcover:1950s", "kfm:hydrology:usgs_gauges"],
  "selected_feature_ids": ["neo4j:Place:DouglasCountyKS"],
  "user_question": "What changed in land use near Lawrence during the 1950s?"
}
```

---

## 📤 5. Outputs

### 5.1 Output Types (check all that apply)
- [ ] **Answer text** (with citations)
- [ ] **Structured JSON** (for UI rendering)
- [ ] **Graph updates** (nodes/edges) — *must be governed + reviewed*
- [ ] **Catalog updates** (STAC/DCAT) — *must be governed + reviewed*
- [ ] **PROV records** (required for derived outputs)
- [ ] **Story Node / Pulse Thread draft** (must include evidence manifest)
- [ ] **Detections / Alerts** (anomaly, drift, narrative pattern triggers)

### 5.2 Minimum Output Contract (KFM Evidence-First)
**Every user-facing factual claim must provide at least one of:**
- STAC Item/Collection reference
- DCAT Dataset reference
- PROV activity/entity reference
- Neo4j entity ID + evidence pointers
- Document excerpt ID + source metadata

#### Example: Focus Mode Answer (with Evidence Slots)
```json
{
  "answer_markdown": "…",
  "citations": [
    { "kind": "dcat", "id": "dcat:usgs-nwis-realtime-water", "label": "USGS NWIS Real-time Water Data" },
    { "kind": "stac", "id": "stac:item:ks-river-gauge-topeka:2026-01-22T20:00Z" },
    { "kind": "prov", "id": "prov:activity:focusmode-query:abcd1234" }
  ],
  "confidence": { "level": "medium", "rationale": "Direct DB query + official dataset metadata." },
  "refusals": []
}
```

---

## 🗺️ 6. Evidence & Grounding Policy

> [!IMPORTANT]
> KFM’s guiding constraint: **no new geo-fact enters the knowledge base without a source reference**.  
> For interactive experiences (map layers, story nodes, AI answers), **provenance and citations are first-class UI features**, not optional footnotes.

### 6.1 What Counts as Evidence ✅
- **Catalog evidence:** STAC/DCAT entries that describe assets and metadata
- **Lineage evidence:** PROV traces showing how outputs were produced
- **Data evidence:** PostGIS query outputs *with referenced dataset metadata and timestamped inputs*
- **Document evidence:** OCR’d text + excerpts + source bibliographic metadata
- **Graph evidence:** relationships backed by catalog/prov/doc references (no orphan edges)

### 6.2 Refusal Rules 🚫
The model must refuse or soften outputs when:
- Evidence cannot be located or cited
- A request violates classification (e.g., sensitive/private station locations)
- A prompt attempts to bypass “Prompt Gate” or extract secrets
- A user asks for “the truth” without sources (“Just tell me what happened”)

### 6.3 Citation Style (KFM-friendly)
- **Preferred:** short, structured citations usable by UI (dataset IDs, graph IDs)
- **Fallback:** human-readable sources with stable identifiers (DOIs, archive IDs, URLs)

**Citation format chosen for this model:** {{CITATION_FORMAT}}

---

## 🗃️ 7. Training Data / RAG Context

### 7.1 Model Lineage
- **Base model:** {{BASE_MODEL}}  
- **Fine-tuning:** {{FINE_TUNING_METHOD}} (SFT, DPO, LoRA, none)  
- **Embeddings model (if separate):** {{EMBEDDING_MODEL}}  
- **Retrieval sources:** Neo4j, STAC/DCAT catalogs, document KB, PostGIS summaries

### 7.2 Data Inventory (Required if fine-tuned or if RAG indexes curated)
| Data Source | Purpose | License | Sensitivity | Pointer |
|---|---|---|---|---|
| {{DATASET_1}} | {{PURPOSE}} | {{LICENSE}} | {{PUBLIC/RESTRICTED}} | {{STAC/DCAT/PROV REF}} |
| {{DATASET_2}} | {{PURPOSE}} | {{LICENSE}} | {{PUBLIC/RESTRICTED}} | {{STAC/DCAT/PROV REF}} |

### 7.3 Sensitive / CARE / TK / Cultural Protocols 🪶
If any datasets touch Indigenous knowledge, sacred sites, or culturally sensitive materials:
- [ ] CARE principles considered
- [ ] TK Labels / cultural protocol metadata attached
- [ ] Access constraints enforced via policy
- [ ] UI redaction/obfuscation behavior defined

**Notes:** {{SENSITIVITY_NOTES}}

---

## 🧬 8. Provenance & DevProV

> [!NOTE]
> In KFM, provenance isn’t just “nice to have.” It’s the *guardrail* that enables trust, review, rollback, and federation.

### 8.1 Required Provenance Fields
- **repo_commit:** `{{GIT_SHA}}`
- **pipeline_run_id:** `{{PIPELINE_RUN_ID}}`
- **inputs:** list of entity refs (STAC/DCAT/doc IDs/graph IDs)
- **activities:** transformation steps (with tool versions + container digests)
- **outputs:** produced artifacts (catalog changes, graph CSVs, model outputs, reports)
- **timestamps:** start/end + any queried “as-of” times for dynamic queries

### 8.2 Determinism & Reproducibility 🎛️
For deterministic pipelines (sim runner, bias correction, etc.):
- **random_seed:** `{{SEED}}`
- **virtual_clock:** {{YES_NO}} (if simulation)
- **container_image_digest(s):** {{DIGESTS}}
- **exact parameter bundle:** {{PARAMS_REF}}

### 8.3 DevProV Attachments (Recommended)
| Artifact | Required? | Where | Notes |
|---|---:|---|---|
| Model weights / endpoint ref | ✅ | {{REF}} | include digest if applicable |
| Container image | ✅ | {{REF}} | pin by digest |
| Policy pack snapshot | ✅ | {{REF}} | Rego bundle + version |
| Evaluation report | ✅ | {{REF}} | include test matrix |
| SBOM (SPDX) | 🔶 | {{REF}} | supply chain clarity |
| Signature (cosign) | 🔶 | {{REF}} | provenance integrity |
| Evidence manifests (Story/Pulse) | 🔶 | {{REF}} | ties narrative → data |

### 8.4 OCI Artifact Distribution (If used) 📦
- **OCI registry:** {{OCI_REGISTRY}}
- **Artifact tags:** {{TAGS}}
- **Cosign verify command:** `{{COMMAND}}`
- **ORAS pull command:** `{{COMMAND}}`

---

## 🧪 9. Evaluation

### 9.1 Test Matrix ✅
- **Grounding:** citation presence, evidence correctness, refusal correctness
- **Geospatial reasoning:** bbox/time-range correctness, CRS assumptions, map layer alignment
- **Temporal reasoning:** timeline slider semantics, historic vs modern context
- **Robustness:** prompt injection resistance, adversarial queries, malformed inputs
- **Performance:** latency, throughput, caching behavior
- **Safety:** privacy leaks, sensitive location handling, policy compliance

### 9.2 Metrics (Example)
| Metric | Target | Result | Notes |
|---|---:|---:|---|
| Citation coverage (factual sentences) | ≥ {{X}}% | {{RESULT}} | |
| Refusal precision (policy) | ≥ {{X}}% | {{RESULT}} | |
| Geospatial bbox correctness | ≥ {{X}}% | {{RESULT}} | |
| Hallucination rate (no-evidence claims) | ≤ {{X}}% | {{RESULT}} | |

### 9.3 Domain-Specific Evaluations 🧠📈
**If environmental correction / nowcasting (e.g., quantile mapping, gamma tail handling, NowCast):**
- Calibration/validation datasets: {{REFS}}
- QC flags coverage: {{RESULTS}}
- Determinism confirmed with `--seed`: {{YES_NO}}

**If real-time watcher (e.g., GTFS-RT):**
- Idempotency checks: {{YES_NO}}
- Polling etiquette (ETag/Last-Modified): {{YES_NO}}
- STAC/DCAT output validation: {{YES_NO}}

**If narrative generation (Pulse Threads / Story Nodes):**
- Evidence manifest completeness: {{RESULT}}
- Narrative-to-data link integrity: {{RESULT}}
- Human review workflow adherence: {{YES_NO}}

---

## 🔐 10. Safety, Security, Governance

### 10.1 Policy Gates (OPA / Conftest) 🚦
- **Prompt Gate:** sanitize inputs, block jailbreaks, enforce “no sensitive leaks”
- **Provenance Gate:** deny publish if PROV missing or inconsistent
- **Catalog Gate:** validate STAC/DCAT schemas, required fields, licenses
- **Graph Gate:** deny if dangling edges or “hand-edited” drift from pipeline outputs
- **Secrets Gate:** scan for tokens/keys; block merge on findings
- **Supply Chain Gate:** pinned digests, SBOM present, signature verified (if required)

**Policy pack version:** {{POLICY_PACK_VERSION}}  
**CI job link(s):** {{CI_LINKS}}

### 10.2 Data Classification 🔎
- **Model output classification:** {{PUBLIC/INTERNAL/RESTRICTED}}
- **Redaction rules:** {{RULES}}
- **Geo-obfuscation:** {{YES_NO}} (e.g., rounding, generalized polygons, hidden layers)

### 10.3 Human-in-the-loop 👀
- **Required reviewers:** {{ROLES}}
- **Escalation path:** {{PROCESS}}
- **“Kill switch” / rollback plan:** {{PLAN}}

---

## 📈 11. Monitoring & Maintenance

### 11.1 Monitoring Signals
- [ ] Answer grounding failures (missing citations)
- [ ] Policy denials frequency spikes
- [ ] Drift detection (for real-time models)
- [ ] Dataset anomaly detection (EWMA/CUSUM/threshold triggers, etc.)
- [ ] Narrative pattern detection triggers (Pulse Threads)

**Dashboards / alerts:** {{WHERE}}

### 11.2 Update Cadence ♻️
- **Retraining triggers:** {{TRIGGERS}} (new data domain, drift, policy updates, major bugs)
- **Scheduled refresh:** {{CADENCE}} (monthly/quarterly/event-driven)
- **Backfill strategy:** {{STRATEGY}} (recompute catalogs/prov/graph)

---

## 🚀 12. Deployment & Operations

### 12.1 Runtime Targets
- **Where it runs:** {{API_BACKEND / WORKER / BROWSER / EDGE / MOBILE}}
- **Compute:** {{CPU/GPU/RAM}}
- **Latency targets:** {{P50/P95}}
- **Rate limits:** {{LIMITS}}

### 12.2 Interfaces
- **API endpoint(s):** {{ENDPOINTS}}
- **Tooling / MCP hooks:** {{TOOLS}}
- **Required env vars:** {{VARS}}

### 12.3 Offline / Field Mode (If applicable) 🧳
- **Offline packs:** {{YES_NO}} (pre-rendered tiles, local catalogs, limited QA)
- **On-device inference:** {{YES_NO}} (small local model)
- **Degraded behavior:** {{BEHAVIOR}} (refuse on missing evidence, show cached citations)

---

## ⚠️ 13. Limitations & Known Issues

- {{LIMITATION_1}}
- {{LIMITATION_2}}
- {{LIMITATION_3}}

**Known failure modes to watch:**
- “Evidence looks plausible but doesn’t match time range” (timeline mismatch)
- “Correct dataset but wrong location granularity” (county vs city vs station)
- “Graph relationship inferred but not explicitly supported” (must cite!)

---

## 🗓️ 14. Change Log

| Date (UTC) | Version | Change | Author |
|---|---|---|---|
| {{YYYY-MM-DD}} | {{MODEL_VERSION}} | {{CHANGE}} | {{NAME}} |

---

## ✅ 15. Approvals

| Role | Name | Approved? | Date |
|---|---|---:|---|
| Data Steward | {{NAME}} | ⬜ | {{DATE}} |
| Security | {{NAME}} | ⬜ | {{DATE}} |
| Domain Expert | {{NAME}} | ⬜ | {{DATE}} |
| Maintainer | {{NAME}} | ⬜ | {{DATE}} |

---

## 🧱 Appendix A — KFM Repo / Data Layout

> [!TIP]
> Keep the “canonical truth” in the right place: **PostGIS stores geo truth**, **Catalogs describe assets**, **Graph links context**.

```text
📦 Kansas-Frontier-Matrix/
├─ 🧠 api/                       # services, adapters, policy hooks
├─ 🖥️ ui/                        # React UI (MapLibre/Cesium, panels, Focus Mode)
├─ 📚 docs/                      # architecture, SOPs, guides, glossary
├─ 🗃️ data/
│  ├─ raw/                       # raw inputs (or pointers)
│  ├─ processed/                 # normalized, analysis-ready outputs
│  ├─ catalogs/                  # DCAT datasets (discovery metadata)
│  ├─ stac/                      # STAC items/collections (spatiotemporal asset metadata)
│  ├─ prov/                      # PROV lineage (how outputs were produced)
│  └─ graph/
│     └─ csv/                    # import-ready graph tables (no hand edits)
└─ 🧩 mcp/
   ├─ dev_prov/
   │  ├─ templates/              # 👈 this file lives here
   │  └─ model_cards/            # filled-in model cards
   └─ sops/                      # reproducible workflows (update model, georef map, etc.)
```

---

## 📎 Appendix B — Schemas & Examples

### B.1 Evidence Manifest Template (for Story Nodes / Pulse Threads) 🧾
```yaml
evidence_manifest:
  narrative_id: "{{NARRATIVE_ID}}"
  narrative_type: "story_node | pulse_thread"
  claims:
    - claim: "{{CLAIM_TEXT}}"
      evidence:
        - kind: "stac"
          id: "{{STAC_ID}}"
        - kind: "dcat"
          id: "{{DCAT_ID}}"
        - kind: "doc_excerpt"
          id: "{{DOC_EXCERPT_ID}}"
  curator_review:
    required: true
    reviewer: "{{NAME}}"
    date_utc: "{{YYYY-MM-DD}}"
```

### B.2 PROV Snippet (minimal) 🧬
```json
{
  "activity": { "id": "prov:activity:{{PIPELINE_RUN_ID}}", "type": "kfm:pipeline_run" },
  "used": ["stac:{{STAC_ID}}", "dcat:{{DCAT_ID}}", "doc:{{DOC_ID}}"],
  "generated": ["model:{{MODEL_ID}}:artifact:{{SHA256_DIGEST}}"],
  "startedAtTime": "{{START_UTC}}",
  "endedAtTime": "{{END_UTC}}"
}
```

---

## 📚 Appendix C — Project Reference Pack

> [!NOTE]
> This model card template is designed to fit **all current KFM design + architecture + AI + UI + intake + governance** materials. Use these references when filling sections.

### Core KFM Docs 🧭🌾
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**  
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**  
- **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**  
- **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**  
- **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**  
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**  
- **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**  
- **Additional Project Ideas.pdf**

### Supporting Research / Resource Packs 📦
- **AI Concepts & more.pdf** *(PDF portfolio; open with Adobe Acrobat to access embedded docs/resources)*  
- **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** *(PDF portfolio)*  
- **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** *(PDF portfolio)*  
- **Various programming langurages & resources 1.pdf** *(PDF portfolio)*

### Extra Reference Material (if present in repo) 🧰
- **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf**
- **KFM- python-geospatial-analysis-cookbook.pdf**
- **Data Mining Concepts & applictions.pdf**

---
