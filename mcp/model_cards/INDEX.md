# 🧠📇 KFM Model Cards Index (MCP)

![KFM](https://img.shields.io/badge/Kansas%20Frontier%20Matrix-KFM-6f42c1)
![MCP](https://img.shields.io/badge/MCP-model_cards-0ea5e9)
![Policy](https://img.shields.io/badge/policy-cite--or--refuse-success)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-informational)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-ff69b4)
![Status](https://img.shields.io/badge/status-INDEX%20registry-yellow)

> [!IMPORTANT]
> **KFM is “evidence-first.”** If an AI/ML output can’t be traced back to authoritative sources + lineage metadata, it doesn’t ship. ✅

---

## 🔗 Quick Links

- 📦 [Folder Layout](#-folder-layout)
- ✅ [Model Card Standard](#-model-card-standard-kfm)
- 🗂️ [Model Registry](#️-model-registry)
- 📚 [Project Docs Used](#-project-docs-used-by-these-model-cards)
- 🧰 [How to Add a Model Card](#-how-to-add-a-model-card)

---

## 📦 Folder Layout

```text
mcp/
  model_cards/
    INDEX.md                  👈 you are here 📍
    TEMPLATE__MODEL_CARD.md   🧩 (recommended)
    llm/
      focus_mode_llm.md
      agent_orchestrator_wpe.md
    retrieval/
      embedding_model.md
      rag_context_builder.md
      citation_engine.md
    ingestion/
      ocr_text_extractor.md
      nlp_entity_extractor.md
      geoparser_place_resolver.md
    nowcast_watchers/
      nowcast_engine.md
      drift_detection_pack.md
      anomaly_detectors.md
      gtfs_rt_watcher.md
    narratives/
      story_node_generator.md
      pulse_thread_generator.md
      conceptual_attention_nodes.md
      evidence_manifest_builder.md
    geospatial_ml/
      land_cover_classifier.md
      change_detection_model.md
      pasture_biomass_estimator.md
      map_georeferencing_model.md
    simulations/
      sim_runner.md
      bayesian_drought_frequency.md
    governance/
      policy_pack_opa_rego.md
      artifact_signing_sbom.md
      classification_propagation.md
```

> [!NOTE]
> This INDEX is designed as a **registry**. Some files above may not exist yet—treat them as **planned model cards** until created. 🚧

---

## ✅ Model Card Standard (KFM)

### 🧾 What counts as a “model” here?

In KFM, “model” includes **anything that produces interpretive or derived outputs** that may be surfaced in the UI, exported, or written into catalogs/graph:

- 🧠 **LLMs + agent orchestration** (e.g., Focus Mode Q&A, Watcher–Planner–Executor flows)
- 🔎 **Retrieval + ranking** (embeddings, RAG context building, citation assembly)
- 📄 **Document AI** (OCR, entity extraction, geoparsing, linking to knowledge graph)
- 📡 **NowCast + watchers** (real-time feeds, anomaly detection, drift detection, alerts)
- 📚 **Narrative builders** (Story Nodes, Pulse Threads, “Conceptual Attention Nodes”)
- 🛰️ **Geospatial ML** (classification, change detection, map georeferencing)
- 🧪 **Simulations & statistical models** (scenario outputs, Bayesian models, forecasts)

### 🧱 Minimum required sections

Every model card **must** include:

1. **Intent & scope**
   - Intended use ✅ / non-intended use 🚫
2. **Inputs / outputs**
   - Data contracts + schema expectations
3. **Evidence & provenance**
   - STAC Items + DCAT Dataset entries + PROV run/activity records (the “evidence triplet”)
4. **Evaluation**
   - Metrics, baselines, and acceptance thresholds
5. **Limitations & failure modes**
6. **Risk / governance**
   - Access control expectations, sensitivity tagging, CARE/FAIR notes, policy gates
7. **Monitoring**
   - Drift checks, data quality alerts, retraining triggers
8. **Versioning & distribution**
   - Artifact location (repo/OCI), digest, signatures, changelog

### 🧩 Recommended frontmatter (YAML)

```yaml
id: mc__focus_mode_llm
name: "Focus Mode Assistant"
type: llm
status: draft # proposed | draft | reviewed | production | deprecated
owners:
  - "@kfm-maintainers"
mcp:
  tool_names:
    - "kfm.focus_mode.answer"
powered_features:
  - "UI: Focus Mode"
  - "API: /ai/ask"
inputs:
  schemas:
    - "schemas/query.focus_mode.json"
  sources:
    - "catalog: dcat:datasets/*"
outputs:
  artifacts:
    - kind: "answer_bundle"
      format: "json"
      includes:
        - "answer"
        - "citations"
        - "uncertainty"
provenance:
  requires:
    - "stac_item"
    - "dcat_dataset"
    - "prov_activity"
policy_gates:
  - "cite_or_refuse"
  - "no_html_injection"
  - "sensitivity_propagation"
distribution:
  oci: "ghcr.io/<org>/kfm-models/focus-mode@sha256:<digest>"
signing:
  cosign: true
monitoring:
  drift:
    enabled: true
    signals:
      - "retrieval_hit_rate"
      - "citation_coverage"
      - "domain_shift"
```

### ✅ Definition of Done checklist (copy into each card)

- [ ] **Provenance**: Outputs are linked to STAC + DCAT + PROV
- [ ] **Citations**: “Cite-or-refuse” behavior defined & tested
- [ ] **Eval**: Metrics + thresholds recorded (and reproducible)
- [ ] **Limitations**: Known failure modes + mitigations included
- [ ] **Governance**: Sensitivity classification + access expectations defined
- [ ] **Monitoring**: Drift/quality signals + alert triggers defined
- [ ] **Artifact**: Versioned artifact location + digest + signature strategy recorded
- [ ] **UI/Export**: If user-visible → explainability + caveats provided

---

## 🗂️ Model Registry

### 🧭 Legend

- **Status**: ✅ Production · 🧪 Experimental · 📝 Draft · 🚧 Proposed · 🧊 Deprecated
- **Artifact types**: 🧾 dataset · 📄 doc-derived · 🧠 answer · 📡 live feed · 📚 narrative · 🛰️ raster/tiles · 🧪 simulation

---

### 🧠 LLM & Agent Orchestration

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`llm/focus_mode_llm.md`](./llm/focus_mode_llm.md) | 🧠 LLM | Focus Mode Q&A (UI + API) | 🧠 answer bundle + citations | 📝 |
| [`llm/agent_orchestrator_wpe.md`](./llm/agent_orchestrator_wpe.md) | 🤖 Agents | Watcher–Planner–Executor workflows | 🧾 run logs + decisions | 🚧 |
| [`governance/prompt_injection_defense.md`](./governance/prompt_injection_defense.md) | 🛡️ Filter | Input sanitization + tool safety | 🧾 policy decisions | 🚧 |
| [`llm/xai_audit_panel.md`](./llm/xai_audit_panel.md) | 🧠 XAI | “Why did I get this answer?” UI audit | 🧠 explanation bundle | 🚧 |

---

### 🔎 Retrieval, Evidence, and Ranking

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`retrieval/embedding_model.md`](./retrieval/embedding_model.md) | 🔎 Embeddings | Semantic search + similarity | 🧾 vectors + metadata | 📝 |
| [`retrieval/rag_context_builder.md`](./retrieval/rag_context_builder.md) | 🧰 Pipeline | RAG context assembly | 🧠 context bundle | 📝 |
| [`retrieval/citation_engine.md`](./retrieval/citation_engine.md) | 🧾 Evidence | Citation selection + formatting | 🧠 citations | 📝 |
| [`retrieval/temporal_spatial_resolver.md`](./retrieval/temporal_spatial_resolver.md) | 🗺️ Resolver | UI context (time, place, layers) | 🧠 context signals | 🚧 |

---

### 📄 Ingestion & Document AI

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`ingestion/ocr_text_extractor.md`](./ingestion/ocr_text_extractor.md) | 📄 OCR | Scanned PDF ingestion | 📄 extracted text + confidence | 🚧 |
| [`ingestion/nlp_entity_extractor.md`](./ingestion/nlp_entity_extractor.md) | 🧠 NLP | People/places/dates extraction | 🧾 entities + spans | 🚧 |
| [`ingestion/geoparser_place_resolver.md`](./ingestion/geoparser_place_resolver.md) | 🗺️ NLP | Place resolution → geo features | 🧾 geo-linked entities | 🚧 |
| [`ingestion/graph_linker.md`](./ingestion/graph_linker.md) | 🕸️ Linker | Entity linking into Neo4j | 🧾 graph edges | 🚧 |

---

### 📡 NowCast, Watchers, Drift & Alerts

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`nowcast_watchers/nowcast_engine.md`](./nowcast_watchers/nowcast_engine.md) | 📡 Stream | Live/real-time derived indicators | 🧾 STAC Items + DCAT entries | 🚧 |
| [`nowcast_watchers/drift_detection_pack.md`](./nowcast_watchers/drift_detection_pack.md) | 📉 Monitor | Drift + calibration checks | 🧾 drift reports | 🚧 |
| [`nowcast_watchers/anomaly_detectors.md`](./nowcast_watchers/anomaly_detectors.md) | 📈 Stats | EWMA/CUSUM-style anomaly flags | 🧾 alert events | 🚧 |
| [`nowcast_watchers/gtfs_rt_watcher.md`](./nowcast_watchers/gtfs_rt_watcher.md) | 🚌 Watcher | GTFS-RT polling → map updates | 📡 live feed items | 🚧 |

---

### 📚 Narratives: Story Nodes, Pulse Threads, Conceptual Attention Nodes

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`narratives/story_node_generator.md`](./narratives/story_node_generator.md) | 📚 Narrative | Markdown+JSON Story Node drafts | 📚 story pack + citations | 🚧 |
| [`narratives/pulse_thread_generator.md`](./narratives/pulse_thread_generator.md) | 🧵 Narrative | “Pulse Threads” summaries | 📚 thread + evidence list | 🚧 |
| [`narratives/conceptual_attention_nodes.md`](./narratives/conceptual_attention_nodes.md) | 🧭 Semantic | Pivot hubs for topics/entities | 🧾 node graphs | 🚧 |
| [`narratives/evidence_manifest_builder.md`](./narratives/evidence_manifest_builder.md) | 🧾 Evidence | Evidence manifests for narratives | 🧾 manifest + PROV | 🚧 |

---

### 🛰️ Geospatial ML & Remote Sensing

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`geospatial_ml/land_cover_classifier.md`](./geospatial_ml/land_cover_classifier.md) | 🛰️ CV/ML | Land cover tagging for imagery | 🛰️ raster labels | 🚧 |
| [`geospatial_ml/change_detection_model.md`](./geospatial_ml/change_detection_model.md) | 🛰️ CV/ML | Detect land changes across time | 🛰️ change maps | 🚧 |
| [`geospatial_ml/map_georeferencing_model.md`](./geospatial_ml/map_georeferencing_model.md) | 🗺️ CV | Align historical scans to map | 🛰️ transforms + confidence | 🚧 |
| [`geospatial_ml/pasture_biomass_estimator.md`](./geospatial_ml/pasture_biomass_estimator.md) | 🌾 ML | Pasture biomass estimation | 🧾 model outputs + uncertainty | 🚧 |

---

### 🧪 Simulations & Scenario Models

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`simulations/sim_runner.md`](./simulations/sim_runner.md) | 🧪 Pipeline | Standard simulation ingestion/run | 🧪 scenario outputs + PROV | 🚧 |
| [`simulations/bayesian_drought_frequency.md`](./simulations/bayesian_drought_frequency.md) | 📈 Stats | Bayesian drought frequency layers | 🧪 posterior summaries | 🚧 |
| [`simulations/scenario_compare.md`](./simulations/scenario_compare.md) | 🧭 UI/Analysis | Scenario comparisons in UI | 🧠 comparison artifacts | 🚧 |

---

### 🧾 Governance, Policy-as-Code & Distribution

| Model Card | Type | Powers | Outputs | Status |
|---|---|---|---|---|
| [`governance/policy_pack_opa_rego.md`](./governance/policy_pack_opa_rego.md) | 🧾 Policy | CI gates (fail closed) | 🧾 pass/fail reports | 📝 |
| [`governance/classification_propagation.md`](./governance/classification_propagation.md) | 🏷️ Tags | Sensitivity propagation rules | 🧾 tag events | 🚧 |
| [`governance/artifact_signing_sbom.md`](./governance/artifact_signing_sbom.md) | 🔏 Supply chain | OCI+SBOM+signatures for models | 🧾 attestations | 🚧 |
| [`governance/human_approval_workflow.md`](./governance/human_approval_workflow.md) | 👤 HITL | Required approvals for publishing | 🧾 approvals log | 🚧 |

---

## 📚 Project Docs Used by These Model Cards

> [!TIP]
> Prefer linking to canonical **repo docs** when available (e.g., `docs/MASTER_GUIDE_v13.md`).  
> Keep PDFs in `docs/pdfs/` (suggested) and update paths if your repo differs.

### 🧩 Core KFM Design & Architecture

- 🏗️ **Comprehensive Technical Documentation**  
  Suggested path: `../../docs/pdfs/KFM_Comprehensive_Technical_Documentation.pdf`  
  Used for: overall platform rules, stack overview, governance expectations, “no black boxes.”
- 🧭 **Comprehensive Architecture, Features, and Design**  
  Suggested path: `../../docs/pdfs/KFM_Architecture_Features_Design.pdf`  
  Used for: system modules, AI integration, simulation outputs, extensibility.
- 🤖 **AI System Overview**  
  Suggested path: `../../docs/pdfs/KFM_AI_System_Overview.pdf`  
  Used for: Focus Mode requirements (citations, context awareness, XAI/audit panel), AI-assisted curation.
- 🖥️ **UI System Overview**  
  Suggested path: `../../docs/pdfs/KFM_UI_System_Overview.pdf`  
  Used for: Story Nodes (Markdown + JSON), narrative playback, offline packs, AR direction, “view model details” UX.

### 📥 Intake, Provenance & Policy Gates

- 📦 **Data Intake – Technical & Design Guide**  
  Suggested path: `../../docs/pdfs/KFM_Data_Intake_Guide.pdf`  
  Used for: evidence triplet (STAC/DCAT/PROV), policy-as-code approach (OPA/Rego), CI+QA framing.
- 🧷 **MASTER_GUIDE / Markdown Guide**  
  Suggested path: `../../docs/MASTER_GUIDE_v13.md`  
  Used for: required artifact conventions, provenance discipline, narrative authoring constraints.

### 🧠 Roadmap, Proposals, and “Next Features”

- ✨ **Latest Ideas & Future Proposals**  
  Suggested path: `../../docs/pdfs/KFM_Latest_Ideas_Future_Proposals.pdf`  
  Used for: live feeds (e.g., GTFS-RT Watcher), bulk document ingestion, deeper Focus Mode integration.
- 🧪 **Innovative Concepts to Evolve KFM**  
  Suggested path: `../../docs/pdfs/KFM_Innovative_Concepts.pdf`  
  Used for: NowCast governance packs, narrative pattern detection, operational hardening ideas.
- 💡 **Additional Project Ideas**  
  Suggested path: `../../docs/pdfs/KFM_Additional_Project_Ideas.pdf`  
  Used for: evidence manifests, policy packs, artifact distribution (OCI), “model outputs as evidence.”

### 🔍 Audits & Best-Practice Scaffolding

- 🧯 **Design Audit – Gaps and Enhancement Opportunities**  
  Suggested path: `../../docs/pdfs/KFM_Design_Audit_Gaps.pdf`  
  Used for: backlog alignment + quality improvements (docs, testing, governance, UX consistency).
- 🧪 **Scientific Method / Research / Master Coder Protocol Documentation**  
  Suggested path: `../../mcp/MASTER_CODER_PROTOCOL.pdf`  
  Used for: consistent experiment hygiene, documentation templates, reproducible research posture.

### 🧰 Reference Packs & Implementation Reading

> [!NOTE]
> Some “portfolio PDFs” require opening with a PDF portfolio-capable viewer (e.g., Acrobat) to access embedded books/docs.

- 🧠 **AI Concepts & More** (portfolio) → model fundamentals & mental models  
  Suggested path: `../../docs/reference_packs/AI_Concepts_and_More.pdf`
- 🗺️ **Maps / GoogleMaps / Virtual Worlds / Archaeology / WebGL** (portfolio) → geospatial + 3D/web rendering references  
  Suggested path: `../../docs/reference_packs/Maps_Geo_WebGL_Portfolio.pdf`
- 💻 **Various Programming Languages & Resources** (portfolio) → implementation references  
  Suggested path: `../../docs/reference_packs/Programming_Resources_Portfolio.pdf`
- 🧮 **Data Management / Theories / Architectures / Bayesian Methods** (portfolio) → statistical + data architecture references  
  Suggested path: `../../docs/reference_packs/Data_Management_Bayesian_Portfolio.pdf`
- 🧑‍🔬 **KFM Python Geospatial Analysis Cookbook** → practical geospatial pipelines & workflows  
  Suggested path: `../../docs/reference_packs/KFM_Python_Geospatial_Cookbook.pdf`
- 📘 **Data Mining Concepts & Applications** → core ML + evaluation building blocks  
  Suggested path: `../../docs/reference_packs/Data_Mining_Concepts_Applications.pdf`
- ✍️ **Comprehensive Markdown Guide (Syntax + Best Practices)** → writing consistency for Story Nodes & cards  
  Suggested path: `../../docs/reference_packs/Comprehensive_Markdown_Guide.docx`

---

## 🧰 How to Add a Model Card

1. 🧩 Create a new file using `TEMPLATE__MODEL_CARD.md` (recommended)  
2. 🧠 Fill out **intent, I/O, provenance, evaluation, limitations, governance, monitoring**  
3. 🧾 Add/verify **evidence triplet** references (STAC/DCAT/PROV) for any published outputs  
4. 🛡️ Add/update a **policy gate** (OPA/Rego + conftest-style checks) if the model creates user-visible or exportable outputs  
5. 🧱 Register the card in **this INDEX** (correct category + status)  
6. 👤 Route for review (especially if touching sensitive domains or human-subject narratives)

> [!TIP]
> If a model powers **Story Nodes** or **Focus Mode**, treat the model card as **UI-adjacent documentation** too:
> - include “what the UI shows”
> - include “what warnings/caveats the UI must display”
> - include “how users can verify claims” ✅

---

## 🧾 Appendix: TEMPLATE Stub (mini)

If you haven’t created `TEMPLATE__MODEL_CARD.md` yet, here’s a minimal stub you can copy:

```markdown
---
id: mc__<slug>
name: "<Human-friendly name>"
type: <llm|embedding|classifier|regressor|simulation|pipeline>
status: proposed
owners: []
mcp:
  tool_names: []
powered_features: []
---

# <Name> 🧠

## 1) Intent & Scope 🎯
- Intended use:
- Not intended use:

## 2) Inputs / Outputs 🔁
- Inputs:
- Outputs:

## 3) Evidence & Provenance 🧾
- STAC:
- DCAT:
- PROV:

## 4) Evaluation 📏
- Metrics:
- Acceptance thresholds:

## 5) Limitations & Failure Modes ⚠️

## 6) Governance / Safety 🛡️
- Sensitivity tags:
- Policy gates:

## 7) Monitoring & Drift 📉

## 8) Versioning & Distribution 📦
- Artifact location:
- Digest/signatures:

## 9) References 📚
```

---

_If it’s not documented, it doesn’t exist._ ✨
