# 🗂️ Registry — Experiment Report Tree (dev_prov)

![provenance](https://img.shields.io/badge/provenance-STAC%2FDCAT%2FPROV-2b6cb0)
![policy](https://img.shields.io/badge/policy-OPA%2FConftest%20gated-6b46c1)
![ledger](https://img.shields.io/badge/log-append--only%20ledger-0f766e)
![artifacts](https://img.shields.io/badge/artifacts-digests%20%26%20signing-9a3412)
![template](https://img.shields.io/badge/template-experiment__report__tree-334155)

> 📍 **Folder:** `mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/registry/`  
> 🎯 **Purpose:** Machine-readable **source of truth** for experiments, runs, artifacts, and provenance links — so “what happened?” is always answerable.

---

## 🧠 What this folder is (and isn’t)

### ✅ This registry **is**
- A **thin, query-friendly index** of *what* exists in the experiment tree (IDs, paths, digests, versions, metadata).
- A **provenance router** that points to the required evidence chain (STAC/DCAT/PROV) and run manifests.
- An **automation-friendly contract** used by agents (Watcher → Planner → Executor) and CI policy gates.
- The “glue layer” between human reports 📝 and machine-auditable artifacts 🧾.

### 🚫 This registry is **not**
- A dumping ground for binaries (models, rasters, PDFs, zips).  
  ➜ Store binaries in `../artifacts/` (or an OCI registry) and reference them here by digest.
- A second copy of your report.  
  ➜ Reports live in `../experiments/` (or `../reports/`) — registry only links + summarizes.

---

## 🧭 Design principles (KFM-flavored)

> [!IMPORTANT]
> **No artifact without provenance. No provenance without policy. No policy without tests.** 🧷

- **Evidence-first**: treat experiment outputs (including AI outputs) as first-class “evidence artifacts.”
- **Fail closed**: if required metadata is missing (license, classification, PROV links), the registry entry is invalid.
- **Append-only mentality**: don’t “rewrite history.” Deprecate + supersede.
- **Stable IDs + content digests**: humans remember IDs, machines trust hashes.
- **UI-ready transparency**: registry fields should support “Layer Provenance”, “Audit Panels”, and export attributions.

---

## 🧱 Expected layout (template)

> Your exact filenames may differ — this is the **contract shape** this example intends.

```text
registry/
├─ 📄 README.md                         # you are here
├─ 📄 registry.index.json               # top-level index (fast lookup)
├─ 📄 registry.index.ndjson             # optional append-only event stream
├─ 📁 experiments/                      # one folder per experiment (stable ID)
│  ├─ 📁 EXP-0001/                      
│  │  ├─ 📄 entry.json                  # experiment summary + links
│  │  ├─ 📄 prov.jsonld                 # PROV for the experiment/report itself
│  │  ├─ 📄 runs.json                   # run list (run_id → manifest + artifacts)
│  │  └─ 📄 metrics.json                # metrics snapshot (optionally DVC-friendly)
│  └─ 📁 EXP-0002/
│     └─ ...
├─ 📁 schemas/                          # JSON Schemas used by CI + tooling
│  ├─ 📄 experiment.entry.schema.json
│  ├─ 📄 run.manifest.schema.json
│  └─ 📄 artifact.ref.schema.json
└─ 📁 policies/                         # optional: local policy helpers for this example
   └─ 📄 README.md
```

---

## 📌 Canonical IDs & naming conventions

### 🧪 Experiment IDs
Format (recommended):
- `EXP-YYYYMMDD-###` ✅ (sortable + unique)  
  Example: `EXP-20260122-001`

Or (smaller template):
- `EXP-0001`, `EXP-0002`, …

### 🏃 Run IDs
Format (recommended):
- `RUN-<UTC timestamp>-<short digest>`  
  Example: `RUN-2026-01-22T21-04-12Z-8a31c2f`

### 📦 Artifact IDs
- Prefer content-addressed IDs: `sha256:<digest>`  
- If stored in an OCI registry, keep the **OCI digest** and **ref** (tag/URL) as separate fields.

---

## 🗃️ Registry files: what goes where

| File | What it does | Must contain |
|---|---|---|
| `registry.index.json` | Fast lookup for tooling/UI | list of experiment IDs + pointers |
| `experiments/<EXP>/entry.json` | “Card” for an experiment | goals, method, inputs, outputs, decision |
| `experiments/<EXP>/prov.jsonld` | Provenance for the *experiment/report* | agents, activities, used/generated entities |
| `experiments/<EXP>/runs.json` | Run ledger | run_id → manifest digest + artifacts |
| `experiments/<EXP>/metrics.json` | Metrics snapshot | key metrics + thresholds + comparisons |
| `schemas/*.schema.json` | Validation contract | used by CI + policy gates |

---

## 🧬 Minimum required fields (experiment entry)

> [!TIP]
> Think of `entry.json` as the registry equivalent of an “Experiment Report cover page.”  
> The full narrative still lives in the report markdown.

```json
{
  "experiment_id": "EXP-20260122-001",
  "title": "Compare NER approach A vs B for place-name extraction",
  "status": "completed",
  "owners": ["@you", "@kfm-bot"],
  "created_utc": "2026-01-22T21:04:12Z",
  "tags": ["nlp", "ner", "gazetteer", "kansas"],
  "goals": [
    "Increase correct place-name extraction without increasing false positives"
  ],
  "method_summary": "Ran two pipelines with identical inputs; compared precision/recall and downstream graph link rate.",
  "inputs": {
    "datasets": [
      {
        "dcat_id": "dcat:us_ks_historical_docs_v3",
        "stac_collection": "stac:docs_scans_1900s",
        "prov_entity": "prov:entity:raw_docs_bundle_sha256_..."
      }
    ],
    "code": {
      "git_commit": "abcdef123456",
      "pipeline_entrypoint": "src/pipelines/nlp/extract_places.py"
    },
    "environment": {
      "container_image": "ghcr.io/your-org/kfm-pipeline:1.2.3",
      "requirements_lock": "sha256:..."
    }
  },
  "outputs": {
    "artifacts": [
      {
        "artifact_type": "csv",
        "path": "../artifacts/EXP-20260122-001/places_extracted.csv",
        "digest": "sha256:...",
        "stac_item": "stac:item:places_extracted_v1",
        "prov_entity": "prov:entity:places_extracted_sha256_..."
      }
    ],
    "metrics_ref": "metrics.json",
    "runs_ref": "runs.json"
  },
  "decision": {
    "outcome": "adopted",
    "why": "Model B improved F1 by +0.12 and reduced false positives in county-level aggregation.",
    "followups": [
      "Add bias check for indigenous place names",
      "Update model card + pipeline docs"
    ]
  },
  "links": {
    "report_md": "../experiments/EXP-20260122-001/README.md",
    "prov_jsonld": "prov.jsonld"
  }
}
```

---

## 🧾 Run manifests (determinism + audit)

> [!NOTE]
> A **run manifest** is your “receipt.” It records inputs, outputs, tool versions, counts, and policy-relevant facts.

Suggested manifest fields:
- `idempotency_key` (derived from canonicalized JSON)
- `seed` / `clock_mode` (for deterministic simulations)
- `input_digests[]` and `output_digests[]`
- `tool_versions` (compiler/runtime/libs)
- `source_urls[]` (if pulling from upstream sources)
- `summary_counts` (records in/out, errors)

Example skeleton:
```json
{
  "run_id": "RUN-2026-01-22T21-04-12Z-8a31c2f",
  "idempotency_key": "sha256:...",
  "seed": 1337,
  "clock_mode": "virtual",
  "tool_versions": {
    "python": "3.12.1",
    "postgis": "3.x",
    "pipeline": "kfm-pipeline@abcdef123456"
  },
  "input_digests": ["sha256:..."],
  "output_digests": ["sha256:..."],
  "source_urls": ["https://example.gov/data/file.csv"],
  "summary_counts": {
    "records_in": 120034,
    "records_out": 118992,
    "errors": 0
  },
  "prov_activity": "prov:activity:run_8a31c2f"
}
```

---

## 🛡️ Policy gates & validation expectations

### CI checks this registry should be friendly to ✅
- **Schema validation** (JSON Schema / AJV)
- **Policy-as-code** (OPA/Rego via Conftest)
- **Provenance completeness** (STAC/DCAT/PROV links exist for new evidence artifacts)
- **License presence** (no dataset/artifact entry without license)
- **Sensitivity classification present** (and handled correctly)
- **“No bypass” ordering rules** (no graph/UI-facing artifacts without catalog + provenance)

> [!WARNING]
> If you can’t prove provenance, **don’t merge** the registry entry.  
> Create a draft entry and mark it `status: blocked` instead.

---

## 📦 Artifact storage strategies

### Option A: Repo-relative artifacts (simple)
- Store artifacts under `../artifacts/<EXP>/...`
- Reference by:
  - relative path
  - `sha256` digest
  - optional STAC/DCAT/PROV pointers

### Option B: OCI registry artifacts (scalable + signed)
- Push artifacts to an OCI registry (ORAS).
- Attach:
  - signatures (Cosign)
  - provenance attestations (in-toto style)
  - PROV JSON-LD as a “referrer” object
- Registry entry should carry:
  - `oci_ref` (tag/ref)
  - `oci_digest` (immutable)
  - signature verification metadata (issuer/key)

---

## 🗺️ How this connects to the rest of KFM

```mermaid
flowchart LR
  A[🧪 Experiment Report (human)] --> B[🗂️ Registry (machine index)]
  B --> C[🧾 Run Manifests (audit receipts)]
  C --> D[⛓️ PROV / STAC / DCAT (evidence chain)]
  D --> E[🧠 Graph + Search]
  E --> F[🗺️ UI (Layer Provenance / Audit Panels)]
  F --> G[🤖 Focus Mode (cite-or-refuse)]
```

- The **UI** can display experiment outcomes like a “dashboard” without guessing.
- **Focus Mode** can safely reference experiment results because the registry enforces that they’re evidence-linked.
- **Governance ledgers** (append-only logs) are consistent with this registry’s “receipt” model.

---

## 🧰 Quick workflow: adding a new experiment (template)

1. **Create report**  
   - Copy the experiment template into `../experiments/<EXP-ID>/README.md`  
   - Fill sections: *Goals → Data Used → Method → Results → Interpretation* 🧪

2. **Create registry entry**  
   - `registry/experiments/<EXP-ID>/entry.json`
   - Add `prov.jsonld` for the experiment/report itself
   - Add `runs.json` and/or run manifest references

3. **Record artifacts**  
   - Put outputs in `../artifacts/<EXP-ID>/...` (or OCI)
   - Compute digests and link them in `entry.json`

4. **Pass gates**  
   - Validate schemas
   - Run Conftest policies
   - Ensure STAC/DCAT/PROV pointers exist for evidence artifacts

5. **Append, don’t rewrite**  
   - If correcting: mark old entry as `deprecated` and add a new one that supersedes it.

---

## 📚 Project doc inputs this registry is aligned with

> This example registry structure is intentionally consistent with the broader KFM docs on:  
> provenance-first pipeline, policy gates, evidence artifacts, experiment reporting, and UI transparency.

<details>
<summary>📖 Click to expand the full project-files list</summary>

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**  
- 🧭 **Kansas Frontier Matrix (KFM) – AI System Overview**  
- 🏗️ **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**  
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview**  
- 📥 **Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide**  
- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)**  
- ➕ **Additional Project Ideas**  
- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals**  
- 🧩 **AI Concepts & more** *(PDF portfolio reference library)*  
- 🗺️ **Maps / GoogleMaps / VirtualWorlds / Archaeology / Computer Graphics / Geospatial WebGL** *(PDF portfolio reference library)*  
- 🧰 **Various programming languages & resources** *(PDF portfolio reference library)*  
- 🗄️ **Data Management / Theories / Architectures / Data Science / Bayesian Methods** *(PDF portfolio reference library)*  

</details>

---

## 🧾 Glossary (tiny but useful)

- **STAC**: “Where/when + assets” catalog for spatial/temporal data  
- **DCAT**: dataset-level catalog metadata  
- **PROV**: lineage graph of *used/generated/agents/activities*  
- **W-P-E**: Watcher → Planner → Executor automation pattern  
- **Fail closed**: missing metadata = blocked merge  
- **Evidence artifact**: any derived output that must move through the same pipeline as “real data”

---

### ✅ Definition of Done (DoD) for registry entries

- [ ] Entry has a stable `experiment_id`
- [ ] Inputs list includes dataset identifiers (and provenance pointers where required)
- [ ] Outputs list includes artifact digests (+ location)
- [ ] A run manifest exists for any non-trivial execution
- [ ] License + sensitivity classification fields are present where applicable
- [ ] Schema + policy checks pass (CI green) ✅
- [ ] Report markdown is linked (human narrative exists)

---

💬 **Rule of thumb:** If someone can’t reproduce it, audit it, or cite it… it’s not “in the system” yet.
