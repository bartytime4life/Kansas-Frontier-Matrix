# 📜 CHANGELOG

![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.1.0-informational)
![SemVer](https://img.shields.io/badge/SemVer-2.0.0-blue)
![Status](https://img.shields.io/badge/status-draft-yellow)
![Repo](https://img.shields.io/badge/repo-Kansas%20Frontier%20Matrix%20(KFM)-black)

All notable changes to this repository will be documented in this file.  
This format is based on **Keep a Changelog**, and the repository follows **Semantic Versioning** with major versions reflecting structural shifts (e.g., `v13`) and minor versions adding backwards-compatible enhancements. :contentReference[oaicite:0]{index=0}

---

## ✨ Legend

- **➕ Added** — new features, modules, docs, schemas, datasets, or workflows  
- **✏️ Changed** — modifications to behavior, structure, contracts, governance, or pipelines  
- **⚠️ Deprecated** — still available, but planned for removal  
- **🗑️ Removed** — removed features, files, or APIs  
- **🛠️ Fixed** — bug fixes, broken links, broken build steps, etc.  
- **🔒 Security** — security hardening, scanning, sensitive data protections  

---

## 🧭 Project invariants (do not regress)

KFM enforces a strict pipeline order and boundary contracts. Releases should **never** introduce changes that violate these invariants without an explicit breaking-change note and migration path. :contentReference[oaicite:1]{index=1}

- **Pipeline ordering is absolute:**  
  `ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode` :contentReference[oaicite:2]{index=2}
- **API boundary rule:** the UI must not query Neo4j directly; access is through governed APIs. :contentReference[oaicite:3]{index=3}
- **Provenance-first publishing:** published data must be registered with provenance before graph/UI use. :contentReference[oaicite:4]{index=4}
- **Evidence-first narrative:** Story Nodes / Focus Mode content must be provenance-linked; no unsourced narrative; AI output must be disclosed and evidence-bound. :contentReference[oaicite:5]{index=5}

---

## 🧰 Repo structure snapshot (v13 expectation)

<details>
<summary>🗂️ Canonical top-level layout (click to expand)</summary>

```text
📁 data/
📁 docs/
📁 mcp/
📁 schemas/
📁 src/
📁 tests/
📁 tools/
📁 web/
📁 releases/

📄 README.md
📄 LICENSE
📄 CITATION.cff
📄 CHANGELOG.md
📄 CONTRIBUTING.md
📄 SECURITY.md
📄 docker-compose.yml
📄 .env.example
```

(Shown in the v13 Master Guide’s repo layout.) :contentReference[oaicite:6]{index=6}
</details>

---

## [Unreleased] 🚧

### ➕ Added (planned / in-progress)
- 🧠 **Focus Mode AI assistant** (governed, evidence-bound): natural-language queries routed through approved tools/APIs, requiring citations for factual outputs. :contentReference[oaicite:7]{index=7}
- 🦙 **Local LLM runtime via Ollama** for privacy/offline capability in sensitive + field deployments (no external AI API calls). :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}
- 🧲 **Local embeddings + retrieval** to support semantic search / RAG style workflows (local vectorization + optional tool-calling models). :contentReference[oaicite:10]{index=10}
- 🧭 **Navigation & map-reading capability modules** (research + UI concepts), including distance/direction workflow patterns for field use. :contentReference[oaicite:11]{index=11}
- 🧱 **3D GIS / immersive research track** for future visualization and analysis modes (incl. machine learning classification trends in 3D GIS platforms). :contentReference[oaicite:12]{index=12}

### ✏️ Changed (planned / in-progress)
- 📦 Tighten “contract-first” change workflow: schema/API changes require explicit changelog notes + version bump + compatibility notes. :contentReference[oaicite:13]{index=13}
- 🧾 Stronger provenance guarantees for “evidence artifacts” (AI/analysis outputs) so they behave like first-class datasets (catalog + lineage + governed API exposure). :contentReference[oaicite:14]{index=14}

### 🔒 Security (planned / in-progress)
- 🔍 Expand automated scanning for secrets + PII + sensitive layers, with governance triggers on high-risk additions. :contentReference[oaicite:15]{index=15}

---

## [v13.0.0-draft] 🧱 - 2025-12-28

### ➕ Added
- 📁 Introduced/standardized canonical roots used across the pipeline, including:  
  `schemas/`, `releases/`, `data/prov/`, `data/catalog/dcat/`. :contentReference[oaicite:16]{index=16}
- 🗂️ Moved Story content into governed structure under `docs/reports/story_nodes/` with `draft/` vs `published/` workflow. :contentReference[oaicite:17]{index=17}

### ✏️ Changed
- 🧭 Enforced **one canonical directory per subsystem** (reducing duplicate/mystery folders) and clarified canonical homes (e.g., `src/server/` for APIs and `web/` for UI). :contentReference[oaicite:18]{index=18}
- ✅ Strengthened “contract-first” and “evidence-first” workflows repo-wide (catalog-before-narrative; schemas/contracts first-class). :contentReference[oaicite:19]{index=19}
- 🧪 Updated profiles references (STAC/DCAT/PROV v11) and expanded CI/validation expectations. :contentReference[oaicite:20]{index=20}

### ⚠️ Breaking / migration notes
- Any integrations relying on pre-v13 folder locations may require path updates (canonical home enforcement). :contentReference[oaicite:21]{index=21}

---

## [v12.0.1-draft] ✍️ - 2025-12-27

### ✏️ Changed
- 📐 Refined documentation structure to align with the Universal Doc template.
- 🧭 Clarified canonical paths, invariants, and contract-first / evidence-first boundaries. :contentReference[oaicite:22]{index=22}

---

## [v12.0.0-draft] 🏁 - 2025-12-17

### ➕ Added
- 🧩 Initial scaffolding of Master Guide v12.
- 🧭 Established pipeline ordering and governance structure foundation. :contentReference[oaicite:23]{index=23}

---

## 📚 Provenance notes (why this changelog looks like this)

This changelog is aligned to the **KFM Master Guide v13** concept of:
- strict pipeline ordering,
- contract-first interfaces,
- evidence-first narrative governance,
- and repo-level semantic versioning expectations. :contentReference[oaicite:24]{index=24}:contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}

The **AI / Focus Mode** roadmap items are sourced from the **Comprehensive Technical Blueprint**, which describes local LLM operation via Ollama and evidence-bound, governed AI behavior. :contentReference[oaicite:27]{index=27}

---

## 🔗 Link references (optional)

> TODO: Add GitHub compare links once tags are created (e.g., `v12.0.1-draft...v13.0.0-draft`) ✅
