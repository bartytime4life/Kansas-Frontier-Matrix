# ⛓️ Provenance Contract (KFM-PROV) — MCP Gate

![Status](https://img.shields.io/badge/status-draft-orange)
![Profile](https://img.shields.io/badge/profile-KFM--PROV%20v11.0.0-blue)
![Format](https://img.shields.io/badge/format-JSON--LD%20%2F%20PROV--O-blueviolet)
![Principle](https://img.shields.io/badge/principle-evidence--first-brightgreen)
![Policy](https://img.shields.io/badge/policy-fail--closed-red)
![Gate](https://img.shields.io/badge/gate-OPA%20%2B%20Conftest-informational)

📍 **Location:** `mcp/gates/contracts/data/schema/provenance/`  
🎯 **Purpose:** Make lineage **mandatory**, **machine-verifiable**, and **user-visible** across KFM (data → graph → API → UI → AI).

> [!IMPORTANT]
> **No mystery layers.** If an output can’t be traced to inputs + process + agent, it **doesn’t ship**.

---

<details>
<summary>📚 Table of Contents</summary>

- [Why this exists](#-why-this-exists)
- [How provenance fits KFM](#-how-provenance-fits-kfm)
- [Evidence Triplet](#-evidence-triplet)
- [What this contract covers](#-what-this-contract-covers)
- [Expected folder contents](#-expected-folder-contents)
- [KFM-PROV model](#-kfm-prov-model)
  - [Core PROV types](#core-prov-types)
  - [KFM extensions](#kfm-extensions)
  - [Required invariants](#required-invariants)
- [IDs, namespaces, and linking](#-ids-namespaces-and-linking)
- [Run manifest binding](#-run-manifest-binding)
- [Gate rules (what fails the build)](#-gate-rules-what-fails-the-build)
- [UI + Focus Mode requirements](#-ui--focus-mode-requirements)
- [Sensitivity, CARE, and privacy](#-sensitivity-care-and-privacy)
- [Streaming + simulation considerations](#-streaming--simulation-considerations)
- [Local validation](#-local-validation)
- [Examples](#-examples)
- [References (project docs)](#-references-project-docs)
- [Definition of Done](#-definition-of-done)

</details>

---

## 🧭 Why this exists

KFM’s platform philosophy is **provenance-first** and **contract-first**:

- ✅ Every dataset has a **data contract** (metadata + schema + processing steps).
- ✅ Every derived output includes a **lineage record** (inputs → process → agent).
- ✅ Every UI/AI surface can explain **where the information came from** (citations, license, preparation summary).
- ✅ CI enforces this with **fail-closed gates** (schema + completeness + ethics).

This directory is the **authoritative contract** for the provenance side of that promise.

---

## 🧩 How provenance fits KFM

KFM’s pipeline treats data as evidence with explicit trust boundaries:

- `data/raw/` is **immutable evidence** (never edited in place).
- deterministic ETL produces outputs into `data/work/` then `data/processed/`.
- publication requires “boundary artifacts” (catalog + lineage) before the dataset is usable downstream.

This provenance contract is the “lineage boundary artifact” that unlocks:

- 🧠 **Neo4j ingest** (graph edges back to catalogs)
- 🔌 **API contracts & redaction** (classification-aware delivery)
- 🗺️ **UI attribution & layer provenance**
- 🤖 **Focus Mode citations + audit panel** (XAI / governance flags)

---

## 🔗 Evidence Triplet

KFM publishes data using an evidence triplet:

- 🛰️ **STAC** — geospatial assets + item/collection metadata  
- 📇 **DCAT** — discovery/catalog metadata (license, publisher, access)  
- ⛓️ **PROV** — lineage + chain-of-custody (how it was produced)

```mermaid
flowchart LR
  A[📥 Raw Sources<br/>data/raw/] --> B[🧪 ETL + Normalization<br/>data/work/]
  B --> C[🗄️ Curated Outputs<br/>data/processed/]

  C --> D[🛰️ STAC<br/>data/stac/]
  C --> E[📇 DCAT<br/>data/catalog/dcat/]
  C --> F[⛓️ PROV<br/>data/prov/]

  D --> G[🧠 Neo4j Knowledge Graph]
  E --> G
  F --> G

  G --> H[🔌 API Layer<br/>(contracts + redaction)]
  H --> I[🗺️ UI + 🤖 Focus Mode<br/>(citations + attribution)]
```

> [!NOTE]
> “Evidence-first” means the metadata isn’t optional garnish — it’s part of the deliverable. 🍽️

---

## ✅ What this contract covers

This contract defines a **KFM-PROV profile** used for:

- 📦 Dataset and layer production lineage (ETL runs, transforms, reprojections, joins)
- 🧠 Analysis / modeling outputs as first-class datasets (simulations, bias correction, OCR corpora)
- 🤖 AI outputs (Focus Mode answers and generated narratives) with **mandatory citations**
- 🔐 Governance events (classification decisions, approvals, redactions)
- 🧰 CI/CD & DevOps provenance (optional but supported): PR → PROV graph records, build attestations

---

## 📁 Expected folder contents

This README is the **spec**; schema/policy files live alongside it.

```text
mcp/gates/contracts/data/schema/provenance/
├─ 📘 README.md                      # you are here
├─ 🧾 kfm-prov.schema.json            # JSON Schema for KFM-PROV bundles (JSON-LD)
├─ 🧠 kfm-prov.context.jsonld         # JSON-LD context extensions (kfm namespace)
├─ 🧾 run-manifest.schema.json        # schema for per-run manifest (audit trail)
├─ 🧾 evidence-manifest.schema.json   # schema for Story Node evidence manifests
├─ 🧾 agent-action.schema.json        # schema for agent actions (Watcher/Planner/Executor)
├─ 🧪 examples/
│  ├─ minimal.bundle.jsonld
│  ├─ dataset-etl.bundle.jsonld
│  ├─ streaming-query.bundle.jsonld
│  ├─ story-node.bundle.jsonld
│  └─ pr-activity.bundle.jsonld
└─ ✅ tests/
   ├─ fixtures/
   └─ expected-failures/
```

> [!TIP]
> Keep schemas tiny and composable. Prefer `$ref` over mega-files. 🧱

---

## 🧬 KFM-PROV model

### Core PROV types

We model provenance using **W3C PROV** (PROV-O semantics, serialized as JSON-LD):

- **Entity** — a thing (file, dataset, table, STAC item, DCAT record, model output, AI answer)
- **Activity** — something that happens (ingest run, transform, query, simulation, export)
- **Agent** — who/what did it (human contributor, CI bot, pipeline container, AI agent)

### KFM extensions

KFM extends PROV with fields needed for enforcement and UX:

**KFM envelope fields (recommended):**
- `kfm:profile` — `"kfm-prov/11.0.0"`
- `kfm:bundle_id` — stable ID for this PROV bundle
- `kfm:dataset_id` — canonical dataset ID (matches STAC/DCAT)
- `kfm:run_id` — pipeline run identifier (ties to run manifest)
- `kfm:policy_pack_version` — governance policy pack version used
- `kfm:classification` — sensitivity level (public/internal/restricted/etc)
- `kfm:license` — license identifier (must match DCAT)
- `kfm:artifacts` — digests/URIs for produced outputs (sha256, OCI digest, etc)
- `kfm:signatures` — optional signature refs (cosign/in-toto/SLSA)

**Agent typing (recommended):**
- `kfm:agent_type`: `human | pipeline | ci | watcher | planner | executor | ai`
- `kfm:role`: e.g., `maintainer`, `contributor`, `reviewer`, `system`

**AI outputs (required if AI involved):**
- `kfm:citations` — machine-readable citations (dataset IDs / graph entities / doc refs)
- `kfm:explainability` — optional pointers to audit-panel data (features, graph edges, flags)
- `kfm:governance_flags` — e.g., `sensitive_data_notice`, `bias_flag`, `needs_review`

### Required invariants

These are the invariants the **gate** enforces (see [Gate rules](#-gate-rules-what-fails-the-build)):

1. **Every published dataset has lineage**  
   If `data/processed/**` changes, a matching `data/prov/**` update must exist.

2. **Every output entity has a generator activity**  
   Each produced Entity must have `prov:wasGeneratedBy` → Activity.

3. **Each activity declares inputs**  
   Activities must enumerate `prov:used` Entities (including raw sources + configs).

4. **Each activity is tied to an agent**  
   Activity must link to `prov:wasAssociatedWith` Agent (human or system).

5. **License + sensitivity exist before UI/Graph**  
   Missing `license` or `classification` is a block.

6. **AI citations are mandatory**  
   If Focus Mode produces an answer/story and cannot cite, the correct behavior is **refusal**.

---

## 🆔 IDs, namespaces, and linking

### ID patterns (recommended)

Use stable, dereferenceable-ish URNs (or URLs if your deployment has them):

- `urn:kfm:dataset:<domain>.<name>.<version>`
- `urn:kfm:run:<timestamp-or-ulid>`
- `urn:kfm:activity:<run_id>#<step>`
- `urn:kfm:entity:<content-hash-or-path>`
- `urn:kfm:agent:<user-or-service>`

### Linking across STAC + DCAT + PROV

**One dataset = one canonical ID**:

- STAC: `id` or `properties["kfm:dataset_id"]`
- DCAT: `dct:identifier` (or equivalent)
- PROV: `kfm:dataset_id`

> [!IMPORTANT]
> If these IDs diverge, citations break and the UI loses attribution. Keep them in lock-step. 🔗

---

## 🧾 Run manifest binding

Every pipeline or simulation run should emit a **Run Manifest** (audit trail) that the PROV bundle references.

**Goals:**
- reproducibility (inputs + tool versions + config)
- integrity (canonical digest / idempotency key)
- reviewability (summary counts, errors, warnings)

### Minimal run-manifest fields (recommended)

- `run_id`
- `run_time`
- `idempotency_key`
- `canonical_digest` (self-fingerprinting hash)
- `source_urls[]`
- `tool_versions{}` (gdal, tippecanoe, python, node, etc)
- `summary_counts{}` (rows in/out, errors, warnings)
- `outputs[]` (paths + digests)

> [!NOTE]
> Canonicalization (RFC 8785) + SHA-256 is recommended so hashes are stable across environments. 🔒

---

## 🚦 Gate rules (what fails the build)

These checks are designed to run in:
- ✅ CI (Conftest/OPA policy pack)
- ✅ ingestion pipelines (validator library)
- ✅ agent PR workflows (Watcher/Planner/Executor parity)

### Gate matrix

| Gate ID | What it checks | Typical trigger | Fail behavior |
|---|---|---|---|
| `KFM-PROV-001` | Processed data updated without provenance update | PR changes `data/processed/**` | **Block merge** |
| `KFM-PROV-002` | PROV bundle schema invalid | any PROV file changed | **Block merge** |
| `KFM-PROV-003` | Missing license/classification | new dataset or layer | **Block merge** |
| `KFM-PROV-004` | Missing/invalid links to STAC/DCAT IDs | metadata changes | **Block merge** |
| `KFM-PROV-005` | Missing run manifest binding | pipeline outputs | **Block merge** (or warn in dev) |
| `KFM-PROV-006` | AI output lacks citations | Focus Mode/story output | **Refuse output** + block publish |

> [!CAUTION]
> “Fail closed” is intentional. If something doesn’t pass, it **does not** enter the system. 🛑

---

## 🧠 UI + Focus Mode requirements

### UI: provenance is visible, not hidden 🗺️

UI surfaces should be able to read this contract to show:

- Layer source + license (Layer Info)
- Full active-layer citations list (Layer Provenance panel)
- Auto-generated attribution text on exports (screenshots, share links, story exports)

### Focus Mode: citations + auditability 🤖

Focus Mode MUST:
- cite sources for every factual claim (datasets, docs, graph entities)
- refuse if it cannot derive from available evidence
- optionally expose an audit panel: factors/edges used + governance flags

> [!IMPORTANT]
> AI output is treated as a derived artifact — it must carry lineage like any other output.

### Story Nodes: evidence manifests 📖

When producing narratives, attach:

- a human-readable short citations block (3–7 lines)
- a machine-readable evidence manifest (YAML/JSON)
- an embedded PROV snippet linking story → evidence → creation activity

This makes narratives **machine-verifiable** and **exportable with trust**.

---

## 🔐 Sensitivity, CARE, and privacy

KFM governance requires:
- explicit sensitivity labeling
- respectful handling of culturally sensitive / restricted data
- auditability of redaction and approvals

Recommended fields:
- `kfm:classification`: `public | internal | restricted | embargoed`
- `kfm:access_policy`: `rbac:<role>` / `terms:<id>` / `approval:<workflow>`
- `kfm:redaction`: method + reason + approver agent (if applied)

> [!NOTE]
> CARE emphasizes **collective benefit** and **authority to control**. Provenance must record *who approved what* and *why*.

---

## 🌊 Streaming + simulation considerations

### Streaming / live data

If data is real-time:
- provenance is still required
- you may batch provenance into an append-only ledger (NDJSON) for high-throughput streams
- dynamic query results should be captured as Activities that `prov:used` the specific reading(s) with timestamps

### Simulation / modeling

For simulations (e.g., deterministic scenario runners):
- capture input datasets, model code version, parameters, seeds
- store produced diffs, updated STAC, and PROV lineage
- treat model outputs as **first-class datasets** (same workflow, same gates)

---

## 🧰 Local validation

> [!TIP]
> Keep local checks fast so contributors can run them before pushing. ⚡

Suggested developer loop:
1. Validate JSON/JSON-LD against schema
2. Validate cross-links (STAC/DCAT/PROV IDs)
3. Run OPA policies (fail closed)

Example commands (adjust to your toolchain):

```bash
# 1) Schema validation (example placeholders)
check-jsonschema --schemafile mcp/gates/contracts/data/schema/provenance/kfm-prov.schema.json data/prov/**/*.jsonld

# 2) Policy gate (Conftest + OPA)
conftest test --policy mcp/gates/policy --data mcp/gates/data .
```

---

## 🧪 Examples

<details>
<summary>🧾 Minimal PROV bundle (JSON-LD)</summary>

```json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    {
      "kfm": "urn:kfm:",
      "dataset": "urn:kfm:dataset:",
      "run": "urn:kfm:run:",
      "activity": "urn:kfm:activity:",
      "agent": "urn:kfm:agent:",
      "entity": "urn:kfm:entity:",
      "sha256": "urn:hash:sha256:"
    }
  ],
  "@id": "run:01J0EXAMPLE",
  "@type": "prov:Bundle",
  "kfm:profile": "kfm-prov/11.0.0",
  "kfm:dataset_id": "dataset:hydrology.river_gauges.v1",
  "prov:agent": {
    "agent:kfm-ci": {
      "prov:type": "prov:SoftwareAgent",
      "kfm:agent_type": "ci",
      "kfm:role": "system"
    }
  },
  "prov:activity": {
    "activity:01J0EXAMPLE#ingest": {
      "prov:startedAtTime": "2026-01-23T12:00:00Z",
      "prov:endedAtTime": "2026-01-23T12:03:10Z",
      "prov:wasAssociatedWith": "agent:kfm-ci"
    }
  },
  "prov:entity": {
    "entity:usgs-nwis.json": {
      "prov:type": "prov:Entity",
      "kfm:source_url": "https://example.invalid/usgs/nwis",
      "kfm:license": "public-domain"
    },
    "entity:river_gauges.parquet": {
      "prov:type": "prov:Entity",
      "kfm:artifact_path": "data/processed/hydrology/river_gauges.parquet",
      "kfm:digest": "sha256:DEADBEEF..."
    }
  },
  "prov:used": {
    "_:use1": {
      "prov:activity": "activity:01J0EXAMPLE#ingest",
      "prov:entity": "entity:usgs-nwis.json",
      "prov:role": "input"
    }
  },
  "prov:wasGeneratedBy": {
    "_:gen1": {
      "prov:entity": "entity:river_gauges.parquet",
      "prov:activity": "activity:01J0EXAMPLE#ingest"
    }
  }
}
```

</details>

<details>
<summary>🧑‍💻 DevOps provenance (PR as PROV Activity)</summary>

When enabled, PRs can be recorded as PROV:

- PR = `prov:Activity`
- commits = `prov:Entity`
- author/reviewer/CI = `prov:Agent`

This makes “which code version produced this dataset?” queryable in the same provenance graph.

</details>

---

## 📚 References (project docs)

These documents informed this contract (keep this list updated as the project evolves):

### 🧱 Core KFM architecture & governance
- *Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design*
- *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*
- *🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals*
- *Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)*
- *Additional Project Ideas*

### 🧭 UI & AI behavior (provenance must be user-visible)
- *Kansas Frontier Matrix – Comprehensive UI System Overview*
- *Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖*

### 📥 Data intake & metadata standards
- *📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide*
- *Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design*

### 🧰 Supporting reference packs (libraries / portfolios)
- *AI Concepts & more* (PDF portfolio)
- *Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas* (PDF portfolio)
- *Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl* (PDF portfolio)
- *Various programming langurages & resources 1* (PDF portfolio)
- *KFM python geospatial analysis cookbook*
- *Data Mining Concepts & applictions*
- *Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices*
- *MARKDOWN_GUIDE_v13*

---

## ✅ Definition of Done

When adding or modifying a dataset/layer, you should be able to check all boxes:

- [ ] Raw sources live under `data/raw/<domain>/` and are treated immutable 📥
- [ ] Outputs live under `data/processed/<domain>/` 🗄️
- [ ] STAC updated in canonical location (`data/stac/...`) 🛰️
- [ ] DCAT updated in canonical location (`data/catalog/dcat/...`) 📇
- [ ] PROV bundle written to canonical location (`data/prov/...`) ⛓️
- [ ] PROV bundle validates against `kfm-prov.schema.json` ✅
- [ ] License + classification present and consistent across metadata 🔐
- [ ] Run manifest exists and is referenced by PROV 🧾
- [ ] If AI generated/assisted, output includes citations or refuses 🤖
- [ ] Policy gates pass locally and in CI 🚦

---

> [!TIP]
> Provenance isn’t bureaucracy — it’s the **feature** that makes KFM trustworthy. 🧠✨

