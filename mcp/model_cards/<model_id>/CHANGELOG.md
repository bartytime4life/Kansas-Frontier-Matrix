# 🧾 CHANGELOG — `<model_id>` 🤖🗺️

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.1.0-blue)](https://keepachangelog.com/en/1.1.0/)
[![Semantic Versioning](https://img.shields.io/badge/SemVer-2.0.0-blue)](https://semver.org/)
[![MCP](https://img.shields.io/badge/MCP-model__cards-6f42c1)](#)
[![Provenance-First](https://img.shields.io/badge/Provenance-first-0a0a0a)](#)

> 📍 **File location:** `mcp/model_cards/<model_id>/CHANGELOG.md`  
> 🧠 **Scope:** Notable changes to the **model behavior contract**, **retrieval + citation rules**, **governance/safety gates**, **evaluation gates**, and **KFM UI/Map integration expectations**.

---

## 🧭 Repo Map (where this lives)

```text
📦 mcp/
└─ 🪪 model_cards/
   └─ 🧠 <model_id>/
      ├─ 🪪 MODEL_CARD.md
      ├─ 🧾 CHANGELOG.md   👈 you are here
      └─ 🧪 evals/         (optional: eval specs + golden sets)
```

---

## 🔍 How to read this changelog

**Status markers**
- ✅ **Implemented** — shipped + running
- 🧪 **Prototype** — in progress / behind a flag
- 📝 **Spec** — documented contract / roadmap target

**Keep a Changelog categories**
- **Added** for new features/capabilities
- **Changed** for behavior changes
- **Deprecated** for soon-to-be removed
- **Removed** for removals
- **Fixed** for bug fixes
- **Security** for security/safety changes

---

## 🧩 What counts as a “model change” in KFM?

Changes that should land here include:
- ✍️ Prompt/system-instruction updates that materially change answers
- 🔎 Retrieval sources, ranking, grounding strategy, or citation formatting rules
- 🧰 Tooling interface changes (map context, graph query tools, ingestion assistants)
- 🔐 Governance: policy packs, sensitivity/redaction rules, refusal thresholds
- 🧪 Evaluation additions/updates (new regression gates, golden tests, bias checks)
- 📦 Artifact provenance changes (dataset/version pinning, digests, signing)

---

## [Unreleased] 🛠️

> Target: continue evolving `<model_id>` as a **provenance-first**, **context-aware**, **governance-hardened** assistant across KFM’s maps, stories, and analytics.

### Added
- 🧠 **Deeper knowledge-graph grounding**: improve “why/why-not” answers by pulling richer relationship context (events ↔ places ↔ datasets ↔ time). 📝
- 🗂️ **Proactive “next best sources” suggestions**: recommend relevant datasets, layers, or Story Nodes as structured follow-ups (not just free-text). 📝
- 📊 **Inline analytical widgets**: optional small charts (time-series, scatter/correlation) attached to answers when a region/timeframe is active. 📝
- 🧵 **Pulse Threads**: geotagged micro-briefs that can appear as side-panel feed or map popups (human-reviewed or watcher-triggered). 🧪
- 🧭 **Scenario + “what-if” narratives**: support simulation-informed storytelling (past → present → future) with explicit provenance. 🧪
- 🧊 **4D / time-travel storyscapes**: roadmap support for temporal digital-twin-style exploration (time as a first-class dimension). 📝

### Changed
- 🧾 **Citations UX contract**: standardize how citations are presented across UI surfaces (chat, popups, story pages, exports) so users can always trace sources. 📝
- 🗺️ **Context packaging**: formalize how map state is transmitted to the model (selected feature, active layers, timeline range, viewport). 📝

### Security
- 🛡️ **Prompt-injection hardening**: strengthen instruction hierarchy + tool-use constraints, especially when untrusted documents are in context. 🧪
- 🔒 **Sensitive-output query auditing**: introduce/expand inference controls and auditing logic for potentially identifying/sensitive outputs. 📝
- 🧯 **Fail-closed governance gates**: require policy approvals before responses can reference restricted data or produce disallowed outputs. 📝

---

## [0.1.0] 📝 “Provenance-First Behavior Contract” (Design Baseline)

### Added
- 🧾 **Evidence-backed answers by default** (no “black box” answers):
  - Every claim is intended to be grounded in KFM datasets/documents/graph entities.
  - If grounding is unavailable, the model should **refuse** or **express uncertainty** instead of fabricating.
- 🗺️ **Map- & timeline-aware answering**:
  - Incorporate viewport/region/timeframe/layer context into responses.
  - Explain visible layers and narrate site-focused history when applicable.
- 🧭 **Advisory-only posture**:
  - Provide analysis and suggestions without autonomous action-taking.
- 🔍 **Explainability hooks (XAI-ready)**:
  - Support an “audit panel” pattern where feature-attributions and governance flags can be surfaced.

### Security
- 🔐 Establish “provenance-first” as a safety primitive: grounding/citations are not optional; ungrounded output is treated as a defect.

---

## [0.2.0] 📝 “Governance + Sensitive Data UX” (Ethics & Trust Layer)

### Added
- 🏷️ **Sensitivity signaling**:
  - Clear UX signals (lock/warning) for sensitive layers, plus policy-driven availability.
  - Optional generalization patterns (e.g., showing coarse geometry instead of exact points for restricted features).
- 🧯 **Governed refusal modes**:
  - Standard refusal language + safe alternatives when a request violates policy (e.g., offer aggregated outputs).
- 🕵️ **Query auditing concepts**:
  - Documented approaches for auditing queries/outputs to prevent disclosure and inference leaks (online/offline auditing patterns).

### Changed
- 🧭 Tightened “trust contract”: when governance flags are present, the model should explicitly acknowledge constraints rather than silently omitting.

### Security
- 🔒 Strengthened privacy posture by treating inference risks (not just raw data access) as part of governance.

---

## [0.3.0] 📝 “Intake + Lineage Alignment” (STAC/DCAT/PROV & Pipeline Contract)

### Added
- 🧬 **Lineage-first retrieval**:
  - Retrieval sources (datasets/docs/graph entities) are expected to carry lineage metadata (STAC/DCAT/PROV patterns).
- 🤝 **W‑P‑E orchestration alignment**:
  - Align model-assisted workflows with Watcher–Planner–Executor patterns for guarded automation (especially intake + QA).
- 🧪 **Simulation & modeling traceability**:
  - Require simulation outputs to be referenced with reproducible identifiers (run IDs, hashes/digests, provenance chains).

### Changed
- 📦 Standardized how the model references dataset “versions” (date tags, digests, or equivalent), so answers remain reproducible.

### Security
- 🧱 Policy-as-code expectations: decisions about what can be cited or exposed should be enforceable by policy gates.

---

## [0.4.0] 🧪 “Deterministic Packaging + Artifact Integrity” (Performance & Reproducibility)

### Added
- 🗺️ **Dual-format geospatial packaging**:
  - Analytics-friendly (e.g., columnar formats) + visualization-friendly (tile archives) produced from the same source.
- 🧾 **Hash-first provenance**:
  - Encourage deterministic builds where artifacts are traceable via hashes/digests.
- 📦 **OCI-registry artifact storage (design pattern)**:
  - Treat PMTiles/GeoParquet/COG outputs as content-addressable artifacts with signing/verification patterns.

### Changed
- ⚡ Performance posture: prefer pre-generated tile pyramids and client-friendly artifacts to reduce server load and improve UI responsiveness.

### Security
- 🔏 Integrity & tamper-resistance: signed artifacts and digest pinning reduce supply-chain ambiguity.

---

## [0.5.0] 🧪 “Mobile + Offline + Field Mode” (Access Everywhere)

### Added
- 📱 **Mobile-first interaction constraints**:
  - Touch-friendly, simplified layouts; field-mode “quick lookups.”
- 🧳 **Offline data packs**:
  - Bundled region/theme packages (tiles + local store + stories) for low-connectivity contexts.
  - Optional on-device small model for limited offline Q&A.

### Changed
- 🧭 Offline-aware behavior:
  - Responses should clearly label when operating on a limited offline subset.

### Security
- 🔐 Offline governance: offline packs must preserve sensitivity policy (no leaking restricted layers in “downloadable” form).

---

## [0.6.0] 🧪 “Narrative Automation” (Pulse, Patterns, and Story Assist)

### Added
- 🧵 **Pulse Threads** (geotagged, evidence-first micro updates).
- 📈 **Narrative pattern detection**:
  - Statistical/anomaly detectors + narrative templates that can draft “first pass” interpretations.
- 🧠 **Conceptual attention nodes**:
  - Use concept nodes to inject historically relevant context (e.g., “drought” analogs, prior events) into summaries.

### Changed
- ✍️ Story workflow: strengthen human-in-the-loop editing (draft → review → publish) for narratives derived from automated signals.

### Security
- 🧯 Ensure automated narratives remain “citable or silence”: no claims without attached evidence sources.

---

## [0.7.0] 📝 “MCP Compliance + Evals as Gates” (Documentation-First ML Ops)

### Added
- 🪪 **Model Card discipline**:
  - Require model card + bias notes + eval results for any model promoted toward production use.
- 🧪 **Experiment report linkage**:
  - Each material model change should be accompanied by experiment logs (goals, data, method, results, interpretation).
- ✅ **CI-style evaluation gates**:
  - Regression tests and reproducibility checks expected before promotion.

### Changed
- 📚 Documentation-first becomes enforceable:
  - “If it’s not documented, it doesn’t ship” (model behavior, data provenance, evals, limitations).

### Security
- 🔐 Governance + QA converge:
  - Safety rules, privacy constraints, and reproducibility requirements become testable, reviewable artifacts.

---

## 📚 Design & Research Inputs (this changelog is derived from these)

### KFM Core System Docs 🧭
- **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖**
- **Kansas Frontier Matrix – Comprehensive UI System Overview**
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide**
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals**
- **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)**
- **Additional Project Ideas**

### MCP / Process / QA Docs ✅
- **Scientific Method / Research / Master Coder Protocol Documentation**
- **Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities**
- **Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design**
- **MASTER_GUIDE_v13 / REDESIGN_BLUEPRINT_v13 / MARKDOWN_GUIDE_v13**

### Reference Libraries (PDF Portfolios) 🗂️
- **AI Concepts & more** *(portfolio)*
- **Maps / GoogleMaps / VirtualWorlds / Archaeological / Computer Graphics / Geospatial webgl** *(portfolio)*
- **Data Management – Theories / Architectures / Data Science / Bayesian Methods** *(portfolio)*
- **Various programming languages & resources** *(portfolio)*

### Privacy & Analytics References 🔐📈
- **Data Mining – Concepts and Applications** (privacy methods, auditing, inference control)
- **KFM Python Geospatial Analysis Cookbook** (spatial query patterns & analysis helpers)
