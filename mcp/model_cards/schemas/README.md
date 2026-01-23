# 🪪 Model Card Schemas 📐  
**Kansas Frontier Matrix (KFM) · MCP · Contract-first AI documentation**

> **Why this folder exists:** KFM treats AI/ML models like *governed, provenance-carrying artifacts* — not “black boxes.”  
> These JSON Schemas define the **required structure** for model cards so the platform can enforce:  
> ✅ transparency · ✅ reproducibility · ✅ licensing/CARE constraints · ✅ auditability

> [!IMPORTANT]
> **Model cards are contracts.** If a model card doesn’t validate, it shouldn’t ship.  
> KFM’s broader governance approach is “automated gates” + “policy-as-tests” (fail closed). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:1‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧭 Where this fits in MCP

The **MCP (“Master Coder Protocol”) layer** includes methods + computational experiments, plus required artifacts like **model cards** and **experiment reports/logs** so work is repeatable and reviewable. [oai_citation:2‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

This directory lives at:

```text
📁 mcp/
  📁 model_cards/
    📁 schemas/        👈 you are here
      README.md
      *.schema.json
```

---

## 📁 Directory layout (recommended)

> You can use different filenames, but keep the intent clear + versioned.

```text
📁 mcp/model_cards/
  📁 schemas/
    📄 README.md
    📄 model-card.v1.schema.json
    📄 model-card.summary.v1.schema.json
    📄 model-artifact.v1.schema.json
    📄 evaluation-report.v1.schema.json
    📁 defs/
      📄 common.defs.schema.json
      📄 provenance.defs.schema.json
      📄 governance.defs.schema.json
    📁 examples/
      📄 model-card.minimal.v1.json
      📄 model-card.full.v1.json
```

---

## 🧩 What is a “Model Card” in KFM?

A KFM model card is **documentation + metadata** that explains:

- **What the model does** (task + I/O)
- **What it was trained on** (training data references)
- **How it performs** (metrics + evaluation scope)
- **Where it fails / what it shouldn’t be used for** (limitations, bias notes)
- **How it is governed** (licenses, sensitivity, CARE constraints)
- **How it can be audited** (provenance / run-manifest / evidence references)

KFM explicitly calls for model cards to include **training data, accuracy metrics, and bias notes**, and for AI-derived insights to remain **explainable and reproducible** (not just “a number or map”). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## ✅ Why schemas (not just Markdown)?

KFM’s UI and content systems are designed to be **configuration + schema driven**, so components can evolve without rewriting everything. [oai_citation:4‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

Schemas give us:

- **Machine-checkable completeness** (no missing critical fields)
- **Stable contracts for UI + APIs**
- **Policy-as-code hooks** (OPA/Conftest checks can assume structure)
- **Federation readiness** (shared formats across regions/projects)

---

## 🧱 Schema philosophy (KFM-native)

### 1) Evidence-first outputs (no “trust me”)
KFM pushes **receipts**: citations + structured evidence manifests + provenance links so users can drill down into sources. [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:6‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 2) Provenance-first publishing (fail closed)
Governance gates and validation should prevent merges/releases when provenance, licensing, or sensitivity requirements aren’t met. [oai_citation:7‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 3) FAIR + CARE by design
Model card schemas should have explicit slots for governance tags and restrictions (licenses, sensitivity, CARE alignment). KFM highlights CARE-aware handling for sensitive/culturally restricted data in content + UI policy design. [oai_citation:9‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🧾 Core model-card fields (what the schema should enforce)

> [!NOTE]
> The exact property names are up to us — but the **sections** below should exist in some form.

### 🪪 1) Identity
- `id` (stable, slug-like)
- `name`
- `version` (SemVer)
- `status` (`draft` | `active` | `deprecated`)
- `owners` / `maintainers` (people/org)
- `created_at` / `updated_at`

### 🎯 2) Task & interface
- `model_family` (e.g., LLM, classifier, segmentation, time-series)
- `tasks[]` (clear, enumerated)
- `inputs[]` / `outputs[]` (modalities, constraints)
- `dependencies[]` (pipelines, upstream services)

### 🧠 3) Intended use
- `intended_use`
- `intended_users`
- `out_of_scope`
- `assumptions[]`

### ⚠️ 4) Limitations & known risks
- `limitations[]`
- `failure_modes[]`
- `bias_notes[]`
- `safety_notes[]`

### 🧬 5) Data & provenance
- `training_data[]` (references to KFM datasets, ideally via DCAT/STAC identifiers)
- `data_filters` (time, geography, exclusions)
- `provenance`:
  - `run_manifest` (link or digest)
  - `prov_bundle` (JSON-LD / PROV refs)
  - `artifact_lineage` (optional)

KFM repeatedly emphasizes traceability (pipeline manifests, checksums, PROV capture, etc.). [oai_citation:10‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:11‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 📏 6) Evaluation
- `evaluation[]`:
  - datasets used
  - metrics (with definitions + units)
  - confidence intervals / uncertainty (when relevant)
  - slice analysis (region/time/class)
- `benchmarks[]` (optional)
- `human_review` (if required)

KFM highlights performance reporting and governance when ML models drive insights. [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 🔐 7) Governance & compliance
- `license` (SPDX-ish string or structured license object)
- `sensitivity` (public / restricted / culturally_sensitive / etc.)
- `care` (Collective Benefit / Authority to Control / Responsibility / Ethics)
- `constraints[]` (allowed uses, prohibited uses)
- `redaction_rules` (if any)

KFM’s broader system is built around sensitivity-aware handling and compliance gates (license presence, restricted content handling, etc.). [oai_citation:13‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:14‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

### 📦 8) Artifacts & releases
- `artifacts[]`:
  - `uri` (repo path, registry ref, etc.)
  - `digest` (sha256)
  - `signature` (cosign/in-toto refs if used)
  - `sbom` (optional)

KFM proposals include OCI-style artifact storage with signing and attached provenance. [oai_citation:15‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🛰️ 9) Deployment & monitoring
- `deployment_targets[]` (API, Focus Mode tool, batch pipeline, etc.)
- `monitoring`:
  - drift checks
  - alert thresholds
  - audit sampling cadence

---

## 🔗 Evidence manifests (optional but KFM-aligned)

KFM’s **evidence-manifest pattern** (used for Story Nodes / Pulse Threads) is directly applicable to model cards:

- claims → evidence items (dataset IDs, query params, timestamps, checksums)
- machine-readable manifest → UI “View Evidence” panel
- PROV bundle links claims to sources and activities

This pattern is described as a way to make narratives verifiable and auditable. [oai_citation:16‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:17‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

📌 **Schema suggestion:** allow model cards to reference:
- `evidence_manifest_ref` (path/URI)
- `prov_ref` (path/URI)
- `evaluation_run_manifest_ref` (path/URI + digest)

---

## 🚦 Validation (local + CI)

### ✅ 1) JSON Schema validation (structure)
Pick a validator that fits your stack:

```bash
# Python (jsonschema)
python -m jsonschema -i path/to/model_card.json mcp/model_cards/schemas/model-card.v1.schema.json
```

```bash
# Node (ajv)
npx ajv validate -s mcp/model_cards/schemas/model-card.v1.schema.json -d path/to/model_card.json
```

### ✅ 2) Policy-as-code gates (semantics)
Schema validation catches *shape*, but governance needs *meaning*.  
KFM proposals explicitly treat governance rules like test suites (license checks, provenance completeness, restricted content rules, etc.). [oai_citation:18‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧷 Example (minimal model card JSON)

```json
{
  "id": "kfm.model.drought-risk.llm",
  "name": "Drought Risk Narrative Assistant",
  "version": "1.0.0",
  "status": "draft",
  "owners": [{ "name": "KFM Maintainers", "role": "maintainer" }],
  "tasks": ["narrative_summarization", "qa_with_citations"],
  "intended_use": "Summarize drought indicators for Kansas regions with citations.",
  "out_of_scope": "Medical/legal advice; uncited claims; private land sensor disclosure.",
  "training_data": [
    { "ref": "dcat:usgs-nwis-streamflow", "role": "fine_tune" }
  ],
  "evaluation": [
    {
      "metric": "citation_coverage",
      "value": 0.95,
      "notes": "Percent of factual statements linked to evidence items."
    }
  ],
  "governance": {
    "license": "Apache-2.0",
    "sensitivity": "public",
    "care": ["CollectiveBenefit", "Responsibility"]
  },
  "provenance": {
    "run_manifest_ref": "data/audits/run-2026-01-01/run_manifest.json",
    "canonical_digest": "sha256:…"
  }
}
```

---

## 🧰 Adding or evolving schemas

1. **Create a new versioned schema** (avoid breaking older cards).
2. Add at least:
   - one **minimal** example
   - one **full** example
3. Add CI validation for:
   - schema compliance
   - policy checks (OPA/Conftest)
4. Document new fields in this README (or a version section).

> [!TIP]
> If model cards live as Markdown + YAML front-matter, keep the front-matter **schema-validatable** (extract to JSON in CI if needed).  
> KFM documentation style explicitly supports provenance logs and evidence-first reporting in Markdown form. [oai_citation:20‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## 📚 Project sources used (all project docs)

> [!NOTE]
> These are the primary project files that informed this README’s structure, governance posture, and schema expectations.

### 🗺️ Core KFM architecture & platform
- KFM Architecture, Features, and Design  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- KFM AI System Overview  [oai_citation:22‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- KFM Data Intake – Technical & Design Guide  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- KFM UI System Overview  [oai_citation:24‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- KFM Comprehensive Technical Documentation  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 💡 Future concepts & narrative governance
- Additional Project Ideas (Pulse Threads, Evidence Manifests, Run Manifests, policy gates)  [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Innovative Concepts to Evolve KFM  [oai_citation:27‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🌟 Latest Ideas & Future Proposals  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 🧑‍🔬 MCP / research process & quality
- Master Coder Protocol / Scientific Method doc  [oai_citation:29‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- Design Audit (gaps + enhancements; model card + experiment log needs)  [oai_citation:30‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)  
- Open-Source Geospatial Historical Mapping Hub Design  [oai_citation:31‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  

### 📦 Reference portfolios (supporting theory + implementation patterns)
- AI Concepts & more (PDF portfolio)  [oai_citation:32‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- Data Management / Architectures / Bayesian Methods (PDF portfolio)  [oai_citation:33‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- Maps / Google Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL (PDF portfolio)  [oai_citation:34‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- Various programming languages & resources (PDF)  [oai_citation:35‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  

### 🧱 Practical implementation references
- Python Geospatial Analysis Cookbook  [oai_citation:36‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- Data Mining Concepts & applications  [oai_citation:37‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  

---
