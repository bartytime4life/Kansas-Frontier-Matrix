# 🔗 `data/prov/` — Provenance & Lineage (Evidence-First) ⛓️🧭

![Provenance First](https://img.shields.io/badge/provenance-first-1f6feb?style=flat-square)
![W3C PROV](https://img.shields.io/badge/W3C-PROV--O-0b7285?style=flat-square)
![STAC + DCAT](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT-6f42c1?style=flat-square)
![Append-Only](https://img.shields.io/badge/logs-append--only-orange?style=flat-square)

KFM is **evidence-first**: every dataset, map layer, and AI output must be traceable back to its sources — the **“map behind the map”** 🗺️✨

This folder stores **W3C PROV-style lineage bundles** (and related run manifests) that explain **how** something was produced, **from what**, **by whom/what**, **when**, and **with which configuration**.

> **v13 note:** `data/prov/` is the canonical provenance root (v13+). Older docs may mention `data/provenance/` — treat that as legacy and prefer a symlink or mirror index to avoid confusion.

---

## 🧭 Quick Navigation

- [Why this exists](#-why-this-exists)
- [Non-negotiables](#-non-negotiables)
- [What belongs in `data/prov/`](#-what-belongs-in-dataprov)
- [Recommended layout](#-recommended-layout)
- [Naming conventions](#-naming-conventions)
- [PROV concepts used (KFM minimum)](#-prov-concepts-used-kfm-minimum)
- [Cross-links to STAC & DCAT](#-cross-links-to-stac--dcat)
- [Validation & CI gates](#-validation--ci-gates)
- [How to add a provenance record](#-how-to-add-a-provenance-record)
- [AI Answer Provenance](#-ai-answer-provenance)
- [Governance & security notes](#-governance--security-notes)
- [Anti-patterns](#-anti-patterns)

---

## 🎯 Why this exists

In KFM, provenance is a **boundary artifact**: it is required before data is considered fully publishable, and it serves as an interface contract into downstream stages (graph, API, UI, narratives).

Provenance enforces these invariants ✅:

- **Nothing is publishable without lineage** (missing provenance = 🚫 not shippable).
- Data flows through the canonical “truth path”:
  - **Raw ➜ Work ➜ Processed ➜ Catalog outputs (STAC/DCAT/PROV) ➜ Graph ➜ API ➜ UI ➜ Story Nodes ➜ Focus Mode**
- **AI is “No Source, No Answer”**: outputs must be backed by citations and logged for audit.

If you can’t answer **“Where did this come from?”** using this folder (plus linked catalogs), the artifact isn’t ready.

---

## ✅ Non-negotiables

These are KFM invariants that `data/prov/` helps enforce:

1. **Provenance first:** a dataset/evidence artifact must have a PROV lineage record before it can be used by the graph, UI, Story Nodes, or Focus Mode.
2. **No leapfrogging:** no stage may bypass previous stages’ contract outputs.
3. **Machine-validated metadata:** provenance records are meant to be validated against schemas/profiles (fail-closed).
4. **Append-only mindset:** provenance should be treated like an immutable audit record — add new runs; don’t mutate history.
5. **No output less restricted than input:** classification/sensitivity must propagate; redactions must be documented and enforced.

---

## 📦 What belongs in `data/prov/`

This directory holds provenance artifacts for:

### 1) 📚 Published datasets (primary)
A **PROV bundle per dataset version/run**, capturing:
- input source entities (raw files / source URLs / origin systems)
- processing activities (ETL steps, scripts, containers)
- agents (software + human operators where applicable)
- output entities (final processed files / database loads)
- hashes/checksums and immutable identifiers
- links to catalog entries (STAC/DCAT)

### 2) 🏗️ Pipeline runs (manifests)
Append-only run manifests that capture operational details:
- run ID, timestamps, environment
- config files used
- input/output checksums
- pipeline version / git commit
- (optional) validation summaries

> **Rule of thumb:** the **PROV bundle** answers “what/why/how”; the **manifest** answers “what exactly ran.”

### 3) 🧾 Evidence artifacts (AI/analysis outputs)
If an AI/analysis output is persisted as a dataset or map layer, treat it like any other dataset:
- store in `data/processed/...`
- catalog in STAC/DCAT
- trace in PROV (model/activity/params + source entities)

### 4) 🤖 AI provenance (auditable answers)
For each answer (or batch), record:
- question + scope (bbox/time/entities)
- retrieved sources (doc IDs, dataset IDs, graph node IDs)
- model name/version + runtime config
- policy decision result (allowed/blocked)
- output checksum / immutable ID

---

## 🗂️ Recommended layout

> Keep it **boringly consistent**. Predictability is a feature. 😄

```text
data/
└── prov/
    ├── README.md
    ├── 📁 datasets/                  # dataset-level provenance bundles
    │   └── <domain>/
    │       └── <dataset_id>/
    │           ├── <dataset_id>__<run_id>.prov.jsonld
    │           ├── <dataset_id>__<run_id>.manifest.json
    │           └── checksums__<run_id>.json
    ├── 📁 ai/                        # AI answer provenance + audit exports
    │   └── <yyyy-mm>/
    │       ├── answer__<answer_id>.prov.jsonld
    │       └── session__<session_id>.json
    ├── 📁 templates/                 # starter templates for new bundles
    │   ├── TEMPLATE__DATASET_PROV.jsonld
    │   └── TEMPLATE__AI_ANSWER_PROV.jsonld
    └── 📁 index/                     # optional indices for quick lookup (regenerable)
        ├── datasets.index.json
        └── ai.index.json
```

> ⚠️ Legacy note: older docs may refer to `data/provenance/`. Prefer `data/prov/` for v13+. If you keep a legacy path, prefer a **symlink** (or a mirror index) to avoid split-brain lineage.

---

## 🏷️ Naming conventions

### Run ID
Use a stable, sortable run identifier:
- `YYYYMMDDThhmmssZ__<pipeline>__<shortsha>`
- Example: `20260131T034455Z__import_hydro__a1b2c3d`

### Dataset PROV bundle filename
- `<dataset_id>__<run_id>.prov.jsonld`

### Manifest filename
- `<dataset_id>__<run_id>.manifest.json`

### Checksums filename
- `checksums__<run_id>.json` (or inline in the manifest)

### AI answer IDs
Prefer stable IDs that can be correlated with API correlation IDs and/or session IDs:
- `YYYYMMDDThhmmssZ__focus__<shortsha>` (example)
- Or a UUID if that’s easier for the runtime

---

## 🧠 PROV concepts used (KFM minimum)

We follow **W3C PROV** ideas with a KFM-minimal vocabulary:

- **Entity**: a thing (file, table, API resource, STAC Item, DCAT Dataset, model output)
- **Activity**: a process (ETL step, normalization, join, raster reprojection, model run)
- **Agent**: who/what acted (pipeline container, script version, operator, CI runner)

### Storage formats
- Preferred: **JSON-LD** (`.prov.jsonld`) using PROV-O terms.
- Allowed: RDF Turtle (`.prov.ttl`) if needed by tooling or integration.

### Minimum required fields (dataset bundles)
At minimum, a dataset bundle must include:

- **Entities**
  - inputs (raw + intermediate if material)
  - outputs (processed + published)
- **Activities**
  - each major step (or one bundle activity if needed)
- **Agents**
  - software agent (name, version, image tag, commit)
  - optional human agent (role, identifier)
- **Integrity**
  - `sha256` for key entities
- **Linkage**
  - STAC Item/Collection IDs and DCAT Dataset ID (or paths)
- **Governance**
  - license + sensitivity/classification tags
  - (if applicable) redaction/generalization notes

> **KFM requirement:** provenance should allow a reviewer to trace a processed data point back to the raw snapshot and the exact transform code/config that produced it.

---

## 🔄 Cross-links to STAC & DCAT

In KFM, provenance is one of the three required catalog boundary artifacts:

- **STAC** describes the *geospatial assets* (Items/Collections).
- **DCAT** describes the *catalog discovery view* (dataset-level metadata, license, keywords, distributions).
- **PROV** describes the *how it was produced* chain (inputs → steps → outputs).

**Expectation:** a published dataset has all 3:
- `data/stac/...` ✅
- `data/catalog/dcat/...` ✅
- `data/prov/...` ✅

### Cross-layer linkage expectations (practical)
- **STAC Item(s) → data assets** (files/URLs in `data/processed/**` or stable storage).
- **DCAT → STAC/distributions** (discovery layer points to STAC or downloads).
- **PROV end-to-end:** raw inputs → work intermediates → processed outputs + **run/config IDs**.
- **Graph references catalogs:** graph nodes should reference STAC/DCAT/PROV identifiers rather than duplicating payloads.

---

## 🧪 Validation & CI gates

Provenance is not “documentation-only” — it is meant to be **validated**.

Recommended validations:
- JSON-LD parses; required fields present.
- `sha256` checksums match actual artifacts.
- Links resolve:
  - PROV → processed paths exist
  - PROV → STAC/DCAT IDs exist
- Classification consistency:
  - no outputs are less restricted than inputs
- Provenance completeness:
  - raw sources + code/config references are present
  - timestamps are present

> Repo hints (v13 layout): schemas/profiles are expected under `schemas/prov/` and `docs/standards/` (e.g., “KFM_PROV_PROFILE.md”).

---

## 🛠️ How to add a provenance record

### ✅ Checklist (Definition of Done)
When publishing a dataset version:

1. **Create a `run_id`**
2. **Record inputs**
   - origin system / source URL (or citation)
   - raw path
   - checksum (sha256)
   - license + attribution
3. **Record processing**
   - pipeline name + entrypoint
   - container image tag (if any)
   - git commit SHA / version
   - parameters + config paths
4. **Record outputs**
   - processed file path(s) + checksum(s)
   - optional DB load target (table/view ID)
5. **Link catalogs**
   - STAC collection/item IDs
   - DCAT dataset ID
6. **Write bundle**
   - to: `data/prov/datasets/<domain>/<dataset_id>/<dataset_id>__<run_id>.prov.jsonld`
7. **Write manifest**
   - same folder: `<dataset_id>__<run_id>.manifest.json`
8. **Never mutate old records**
   - provenance is **append-only**: new run = new files ✅

---

## 🧾 Example (minimal) dataset PROV bundle (JSON-LD)

> This is intentionally compact. Expand as needed, but don’t omit the minimums.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "https://kansasfrontiermatrix.org/ns#"
  },
  "@id": "kfm:prov/datasets/ks_hydrology_1880/20260131T034455Z__import_hydro__a1b2c3d",
  "@type": "prov:Bundle",
  "@graph": [
    {
      "@id": "kfm:agent/software/import_hydro",
      "@type": "prov:SoftwareAgent",
      "dcterms:title": "import_hydro pipeline",
      "kfm:gitCommit": "a1b2c3d",
      "kfm:containerImage": "ghcr.io/kfm/pipelines/import_hydro:2026.01.31"
    },
    {
      "@id": "kfm:activity/import_hydro__20260131T034455Z",
      "@type": "prov:Activity",
      "prov:startedAtTime": { "@value": "2026-01-31T03:44:55Z", "@type": "xsd:dateTime" },
      "prov:endedAtTime": { "@value": "2026-01-31T03:49:12Z", "@type": "xsd:dateTime" },
      "kfm:runId": "20260131T034455Z__import_hydro__a1b2c3d",
      "kfm:paramsRef": "data/work/hydrology/import_hydro/config.yaml",
      "prov:wasAssociatedWith": [{ "@id": "kfm:agent/software/import_hydro" }],
      "prov:used": [{ "@id": "kfm:entity/raw/usgs_source_csv" }]
    },
    {
      "@id": "kfm:entity/raw/usgs_source_csv",
      "@type": "prov:Entity",
      "kfm:path": "data/raw/hydrology/usgs_hydro_1880.csv",
      "kfm:sha256": "<sha256-here>",
      "kfm:sourceUrl": "<source-url-here>",
      "dcterms:license": "<license-or-source-terms>"
    },
    {
      "@id": "kfm:entity/processed/ks_hydrology_1880",
      "@type": "prov:Entity",
      "kfm:path": "data/processed/hydrology/ks_hydrology_1880.parquet",
      "kfm:sha256": "<sha256-here>",
      "kfm:stacItemId": "stac:item:ks_hydrology_1880__20260131",
      "kfm:dcatDatasetId": "dcat:dataset:ks_hydrology_1880",
      "prov:wasGeneratedBy": { "@id": "kfm:activity/import_hydro__20260131T034455Z" }
    }
  ]
}
```

---

## 🧾 Example (minimal) run manifest (JSON)

```json
{
  "run_id": "20260131T034455Z__import_hydro__a1b2c3d",
  "dataset_id": "ks_hydrology_1880",
  "domain": "hydrology",
  "started_at": "2026-01-31T03:44:55Z",
  "ended_at": "2026-01-31T03:49:12Z",
  "pipeline": {
    "name": "import_hydro",
    "git_commit": "a1b2c3d",
    "container_image": "ghcr.io/kfm/pipelines/import_hydro:2026.01.31",
    "params_ref": "data/work/hydrology/import_hydro/config.yaml"
  },
  "inputs": [
    {
      "path": "data/raw/hydrology/usgs_hydro_1880.csv",
      "sha256": "<sha256-here>",
      "source_url": "<source-url-here>",
      "license": "<license-or-source-terms>"
    }
  ],
  "outputs": [
    {
      "path": "data/processed/hydrology/ks_hydrology_1880.parquet",
      "sha256": "<sha256-here>"
    }
  ],
  "catalog_links": {
    "stac_item_ids": ["stac:item:ks_hydrology_1880__20260131"],
    "dcat_dataset_id": "dcat:dataset:ks_hydrology_1880",
    "prov_bundle_path": "data/prov/datasets/hydrology/ks_hydrology_1880/ks_hydrology_1880__20260131T034455Z__import_hydro__a1b2c3d.prov.jsonld"
  }
}
```

---

## 🤖 AI answer provenance

AI output is treated as a first-class “evidence artifact”:

- it should be **citable**
- it should be **auditable**
- it should be **replayable** (same inputs + same model config = explainable differences)

### What we log (minimum)
- `question`
- `retrieved_sources[]` (doc IDs, dataset IDs, graph node IDs, STAC/DCAT IDs)
- `model` (name/tag), `runtime` (temperature, etc.)
- `policy_gate` outcome (allowed/blocked + reason)
- `answer_hash` (sha256), `created_at`
- (recommended) `correlation_id` that matches API logs

### Example (minimal) AI answer PROV bundle (JSON-LD)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "https://kansasfrontiermatrix.org/ns#"
  },
  "@id": "kfm:prov/ai/answer/20260208T141200Z__focus__9fd3c21",
  "@type": "prov:Bundle",
  "@graph": [
    {
      "@id": "kfm:agent/model/focus_mode_llm",
      "@type": "prov:SoftwareAgent",
      "kfm:model": "focus-mode-llm",
      "kfm:modelVersion": "<model-version-here>"
    },
    {
      "@id": "kfm:activity/focus_mode_query__20260208T141200Z",
      "@type": "prov:Activity",
      "prov:startedAtTime": { "@value": "2026-02-08T14:12:00Z", "@type": "xsd:dateTime" },
      "kfm:correlationId": "<correlation-id-here>",
      "kfm:policyGate": {
        "decision": "allow",
        "policy_version": "<opa-policy-version-here>"
      },
      "prov:wasAssociatedWith": [{ "@id": "kfm:agent/model/focus_mode_llm" }],
      "prov:used": [
        { "@id": "kfm:entity/source/doc/land_treaties_story_node_v3" },
        { "@id": "kfm:entity/source/dataset/ks_hydrology_1880" }
      ]
    },
    {
      "@id": "kfm:entity/question/20260208T141200Z",
      "@type": "prov:Entity",
      "kfm:question": "What waterways changed most between 1880 and 1900 in this county?",
      "kfm:scope": { "bbox": "<bbox>", "time": "<time-range>" }
    },
    {
      "@id": "kfm:entity/answer/20260208T141200Z",
      "@type": "prov:Entity",
      "kfm:answerHashSha256": "<sha256-here>",
      "prov:wasGeneratedBy": { "@id": "kfm:activity/focus_mode_query__20260208T141200Z" }
    }
  ]
}
```

---

## 🔐 Governance & security notes

- **Fail-closed:** missing provenance/metadata blocks publication.
- **Append-only:** treat provenance like an immutable ledger (new run = new files).
- **Sensitivity-aware:** provenance may reference restricted inputs; don’t leak restricted values into public metadata.
- **Classification propagation:** never produce an output less restricted than its input; document redactions/generalizations.
- **Auditability:** provenance should support “who saw what and why” reviews (especially for sensitive layers).
- **Signing (optional but recommended):** future-friendly path is signing manifests/log exports for tamper-evidence.

---

## 🚫 Anti-patterns

Avoid these (they break trust fast):

- ❌ “We processed it somehow” (no activity details)
- ❌ missing checksums (can’t verify integrity)
- ❌ no source URL / attribution (license risk)
- ❌ editing old PROV files (breaks audit trail)
- ❌ publishing a dataset with STAC/DCAT but no PROV (incomplete boundary artifacts)
- ❌ bypassing catalogs (direct-to-UI or direct-to-graph without boundary artifacts)

---

## ✅ Bottom line

If it’s visible in the UI, referenced in the graph, or answerable by Focus Mode, it must be explainable here — **prov or it didn’t happen** 😄⛓️
