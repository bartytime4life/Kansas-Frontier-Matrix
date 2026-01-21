# 00 — Quickstart: Minimal Evidence Triplet (STAC + DCAT + PROV) 🧪🧾

![KFM](https://img.shields.io/badge/KFM-v13-blue)
![Evidence-first](https://img.shields.io/badge/Evidence--First-Required-success)
![Catalog](https://img.shields.io/badge/Catalog-STAC%20%2B%20DCAT-orange)
![Provenance](https://img.shields.io/badge/Provenance-PROV--O%20JSON--LD-9cf)
![Policy%20Gates](https://img.shields.io/badge/Policy%20Gates-OPA%20%2B%20Conftest-critical)

A **minimal, copy-pasteable “publishable unit”** for Kansas Frontier Matrix (KFM): generate the **STAC + DCAT + PROV** triplet (plus checksums + run manifest) so the dataset can safely move downstream into **Graph → API → UI → Story Nodes → Focus Mode** ✅

---

## Contents 🧭

- [Why this exists](#why-this-exists-)
- [What you’ll build](#what-youll-build-)
- [Folder layout](#folder-layout-)
- [Quickstart](#quickstart-)
- [The Triplet, explained](#the-triplet-explained-)
- [Validation gates](#validation-gates-)
- [Promote into KFM canonical dirs](#promote-into-kfm-canonical-dirs-)
- [How it shows up in the UI + Focus Mode](#how-it-shows-up-in-the-ui--focus-mode-)
- [Optional hardening](#optional-hardening-)
- [Definition of Done](#definition-of-done-)
- [Further reading](#further-reading-)

---

## Why this exists 🧠

KFM’s architecture is **catalog-driven** and **evidence-first**:

- **No dataset should be discoverable** until it has:
  - **STAC** (spatiotemporal asset catalog metadata)
  - **DCAT** (dataset discovery + publishing metadata)
  - **PROV** (lineage: inputs → activities → outputs)
- **Policy gates “fail closed”**: if required metadata is missing (license, classification, provenance, etc.), the dataset should **not** enter the system.
- **Focus Mode is gated too**: if an answer can’t cite sources, it’s treated as a policy violation and should be refused.

This folder is the smallest demo of that contract: **create the triplet first**, then (only then) integrate downstream.

> [!NOTE]
> Think of the triplet as the *minimum evidence “passport”* a dataset needs to travel through KFM safely.

---

## What you’ll build 🧰

You will generate:

- 🗺️ **STAC**
  - `collection.json` (dataset-level)
  - `items/*.json` (asset-level)
- 🏷️ **DCAT**
  - `dataset.jsonld` (JSON-LD)
- 🧾 **PROV**
  - `run.jsonld` (JSON-LD provenance graph)
- 🔐 **Integrity**
  - `SHA256SUMS` (checksums)
- 🧪 **Run Manifest**
  - `run-manifest.json` (environment + inputs + outputs + IDs)

---

## Folder layout 📁

```text
mcp/dev_prov/examples/00_quickstart_minimal_triplet/
├─ ✅📄 README.md                         # 👈 you are here 📌 Fastest “evidence triplet” walkthrough (inputs → outputs)
├─ 📥 input/
│  ├─ 🧊 raw/                             # 🧊 Immutable snapshot (as-received bytes; treat as read-only)
│  └─ 📜 contract/                        # 📜 Minimal dataset contract (the metadata you promise is true)
│     └─ 📜🧾 dataset.yml                 # Contract file (or .json per repo convention): id, license, source, extent, notes
└─ 📦 out/
   ├─ 🛰️ stac/                            # STAC outputs: dataset collection + one or more items (time/version snapshots)
   │  ├─ 🧾 collection.json               # STAC Collection (dataset-level metadata + links)
   │  └─ 📁 items/
   │     └─ 🧾 <item_id>.json             # STAC Item (one snapshot pointing to assets/artifacts)
   ├─ 🗂️ dcat/                            # DCAT outputs: discovery/registry metadata (dataset + distributions)
   │  └─ 🧾 dataset.jsonld                # DCAT Dataset record (license, publisher, access, distribution links)
   ├─ 🧬 prov/                            # PROV outputs: lineage linking raw → contract → generated catalogs
   │  └─ 🧾 run.jsonld                    # PROV run bundle (entities/activities/agents + derivations)
   ├─ 🧾 manifest/                        # Run manifests: reproducibility ledger for this example run
   │  └─ 🧾 run-manifest.json             # Commands/inputs/outputs/tool versions + pointers + checksums references
   └─ 🔐 checksums/                       # Integrity proofs: hashes for everything in input/ and out/
      └─ 🔐📄 SHA256SUMS                  # sha256 digest list (tamper detection + reproducibility)
```

> [!IMPORTANT]
> In KFM’s pipeline philosophy, **raw inputs are append-only / immutable**. If the upstream source changes, you create **a new version**, not a silent overwrite.

---

## Quickstart 🚀

### 1) Put *raw bytes* in place 🧊

Drop your source files into:

- `input/raw/`

Examples:
- `input/raw/counties.geojson`
- `input/raw/landcover_2020.tif` (ideally already COG)
- `input/raw/population_1860_2020.csv`

### 2) Write the minimal contract 📜

Create `input/contract/dataset.yml` (or JSON if your repo standardizes on JSON).

Minimal (example) contract:

```yaml
dataset_id: kfm.ks.example.minimal_triplet.v1
title: "Minimal Triplet Example"
description: "A tiny example dataset showing KFM’s STAC/DCAT/PROV evidence contract."
license: "CC-BY-4.0"        # 🔒 policy-gated: required
classification: "public"    # 🔒 policy-gated: required (public/sensitive/confidential/etc.)

spatial:
  # Replace with your dataset extent
  bbox: [-102.051, 36.993, -94.589, 40.003]  # KS-ish bounding box (example)

temporal:
  start: "2020-01-01"
  end: "2020-12-31"

sources:
  - name: "Example upstream"
    url: "https://example.org/data-source"
    retrieved_at: "2026-01-21"

contacts:
  - role: "publisher"
    name: "Kansas Frontier Matrix"
```

> [!TIP]
> If you’re not sure what the contract should look like in this repo, search for `docs/data/contracts/examples/` and mirror the closest one.

### 3) Run the triplet generator ⚙️

This example is intentionally **runner-agnostic**. Your repo might expose `dev_prov` as a Python module, a CLI, or a task runner command.

Start here:

```bash
# from repo root
cd mcp/dev_prov/examples/00_quickstart_minimal_triplet

# Find the implementation entrypoint (pick one that matches your stack)
rg -n "dev_prov|triplet|stac|dcat|prov" ../../..
```

Typical shapes you might see:

```bash
# Option A: Python module style (common in KFM tooling)
python -m mcp.dev_prov.triplet \
  --contract ./input/contract/dataset.yml \
  --raw ./input/raw \
  --out ./out

# Option B: Repo task runner (Make/Just/Task)
make dev_prov-triplet EXAMPLE=00_quickstart_minimal_triplet
# or:
just dev_prov triplet ./input/contract/dataset.yml ./input/raw ./out
```

When it completes, you should see `out/{stac,dcat,prov,manifest,checksums}/...`

---

## The Triplet, explained 🧩

### STAC 🗺️
STAC answers: **what are the assets, where, and when?**

Minimal STAC conventions (for KFM):
- `properties["kfm:dataset_id"]` ties the item to a canonical dataset id
- `assets.*` must include `href`, `type`, and ideally checksums + file sizes

Example STAC Item snippet:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm.ks.example.minimal_triplet.v1__asset01",
  "properties": {
    "datetime": "2020-06-01T00:00:00Z",
    "kfm:dataset_id": "kfm.ks.example.minimal_triplet.v1",
    "kfm:classification": "public"
  },
  "geometry": null,
  "bbox": [-102.051, 36.993, -94.589, 40.003],
  "assets": {
    "data": {
      "href": "../../input/raw/example.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

### DCAT 🏷️
DCAT answers: **what is this dataset, who publishes it, what’s the license, how do I access it?**

Minimal DCAT conventions:
- Must include **title/description/license**
- Should include a distribution pointing to:
  - a STAC Collection (or an API endpoint that returns the collection)
  - and/or a download URL / access URL

Example DCAT snippet (JSON-LD):

```json
{
  "@context": "https://www.w3.org/ns/dcat.jsonld",
  "@type": "dcat:Dataset",
  "dct:identifier": "kfm.ks.example.minimal_triplet.v1",
  "dct:title": "Minimal Triplet Example",
  "dct:license": "CC-BY-4.0",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "application/json",
      "dcat:accessURL": "stac/collection.json"
    }
  ]
}
```

### PROV 🧾
PROV answers: **how was it produced, from what inputs, by which activity, attributed to who/what?**

Minimal PROV should include:
- `prov:Entity` for each raw input (with checksums)
- `prov:Activity` for the ingestion/transform
- `prov:Entity` for each output artifact (STAC/DCAT outputs count too!)
- `prov:Agent` (human or automation), linked via `wasAssociatedWith`

Example PROV concept (JSON-LD-ish):

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "raw:example.geojson": { "prov:label": "raw input", "kfm:sha256": "..." },
    "out:stac_collection": { "prov:label": "stac collection", "kfm:sha256": "..." }
  },
  "activity": {
    "act:ingest_run_001": {
      "prov:label": "dev_prov triplet generation",
      "prov:startedAtTime": "2026-01-21T00:00:00Z"
    }
  },
  "used": {
    "_:use1": { "prov:activity": "act:ingest_run_001", "prov:entity": "raw:example.geojson" }
  },
  "wasGeneratedBy": {
    "_:gen1": { "prov:entity": "out:stac_collection", "prov:activity": "act:ingest_run_001" }
  }
}
```

---

## Validation gates ✅⛔

This example is meant to pass KFM’s minimum gates:

### Structural gates (schemas)
- STAC JSON validates (and follows KFM STAC profile)
- DCAT JSON-LD validates (and follows KFM DCAT profile)
- PROV JSON-LD validates (and follows KFM PROV profile)

### Governance gates (policy-as-code)
- ✅ license present
- ✅ classification present
- ✅ provenance complete (inputs + steps declared)
- ✅ cross-links resolve (dataset IDs consistent)
- ✅ no “orphan” metadata nodes (everything connected)

### Data quality gates (quick sanity)
- geometry validity (if vector)
- CRS declared and consistent
- obvious range checks (if numeric fields)

> [!TIP]
> A KFM mantra that helps place responsibilities:
> **“PostGIS stores geo truth (vectors/rasters), Catalogs describe the assets, Graph links the context.”**

---

## Promote into KFM canonical dirs 🏗️

Once the triplet is generated and validated, you can “promote” it into the repo’s canonical locations (names may vary slightly by KFM version):

- `data/catalog/stac/...` (collection + items)
- `data/catalog/dcat/...` (dataset records)
- `data/prov/...` (lineage runs)
- `data/graph/csv/...` (if/when you add graph import snapshots)

> [!IMPORTANT]
> KFM’s ordering is non-negotiable: **catalogs first**, then graph ingestion, then API/UI surfacing.

---

## How it shows up in the UI + Focus Mode 🗺️🤖

Once promoted and ingested downstream:

- **UI**
  - 2D map layers (MapLibre-style workflow) + optional 3D (Cesium-style workflow)
  - Timeline-driven layers (time slider → filtered STAC items)
  - Story Nodes can reference the dataset by `dataset_id` and/or STAC item IDs
- **API**
  - REST endpoints serve data/tiles/summaries
  - GraphQL queries traverse graph relationships (people ↔ events ↔ places ↔ datasets)
  - API mediates access (redaction/classification), UI should not hit DB/graph directly
- **Focus Mode**
  - Retrieval uses catalog + graph context
  - Responses must cite sources; **triplet links are how Focus Mode stays auditably grounded**

> [!NOTE]
> The minimal triplet is not “extra paperwork.” It’s the **mechanism** that makes the UI and AI trustworthy.

---

## Optional hardening 🛡️

### 1) Add an Evidence Manifest 🧾
For Story Nodes and derived outputs, add a small “evidence manifest” that lists:
- dataset IDs used
- STAC item IDs used
- PROV run IDs used
- checksums / digests for reproducibility

### 2) Package artifacts into OCI + sign them 🔐📦
If you store large artifacts (PMTiles, GeoParquet, COGs) outside Git, consider:
- pushing them to an **OCI registry** (ORAS)
- signing with **Cosign**
- referencing digests inside STAC/DCAT/PROV so the system can always retrieve the exact bytes

Example (shape):

```bash
oras push ghcr.io/<org>/kfm-artifacts:20260121 \
  ./out/some_layer.pmtiles:application/vnd.pmtiles \
  ./out/some_layer.geoparquet:application/vnd.geo+parquet

cosign sign --yes ghcr.io/<org>/kfm-artifacts@sha256:<digest>
```

### 3) Prep for W-P-E automation 🤖
If this example becomes a template for automated ingestion:
- ensure the run manifest captures environment versions
- ensure PRs are reviewable (summaries + stable IDs)
- keep a global **kill-switch** mechanism for agents

---

## Definition of Done ✅

Use this checklist before calling the triplet “ready”:

- [ ] Raw bytes are stored as an immutable snapshot (`input/raw/` or equivalent)
- [ ] Contract includes: **license** + **classification** + spatial/temporal extent
- [ ] STAC validates + includes stable `kfm:dataset_id`
- [ ] DCAT validates + links to STAC + includes license
- [ ] PROV validates + connects inputs → activity → outputs + agent attribution
- [ ] Checksums exist for inputs + outputs
- [ ] Policy gates pass (schema + governance)
- [ ] (Optional) OCI artifact digests + signatures recorded if artifacts are external

---

## Further reading 📚

### Core KFM docs (high signal)
- 📘 Technical architecture, API, formats (GeoJSON/GeoParquet/COG), GraphQL patterns
- 📥 Data intake lifecycle (raw → work → processed → catalogs → graph)
- 🧭 v13 Master Guide / Markdown Guide (pipeline ordering, evidence artifact pattern, templates)
- 🧠 AI system overview (retrieval, governance, citations hard-gate)
- 🗺️ UI system overview (map/timeline/story nodes + layer control)

### Reference libraries (PDF portfolios) 📦
<details>
<summary><b>AI Concepts & more</b> 🤖</summary>

Suggested picks relevant to KFM-style evidence-first AI:
- Deep Learning with Python (2nd Ed)
- Hands-On Machine Learning (3rd Ed)
- Probabilistic Machine Learning (Intro)
- The Turing Way (Reproducible Data Science)
- AI Foundations of Computational Agents (3rd Ed)

</details>

<details>
<summary><b>Data Management / Data Engineering</b> 🗄️</summary>

Suggested picks relevant to governance + provenance:
- Designing Data-Intensive Applications
- Fundamentals of Data Engineering
- Database Performance at Scale
- Data Governance: The Definitive Guide
- Practical Statistics for Data Scientists

</details>

<details>
<summary><b>Maps / WebGL / Geovisualization</b> 🌍</summary>

Suggested picks for map UI + 3D/4D ambitions:
- Making Maps (2nd Ed)
- Thematic Cartography & Geovisualization
- Time in GIS and Geographical Databases
- WebGL Programming Guide
- WebGL Insights

</details>

<details>
<summary><b>Programming Languages & DevOps Resources</b> 🧰</summary>

Suggested picks for implementation + CI/CD:
- Python Notes for Professionals
- JavaScript Notes for Professionals
- TypeScript Notes for Professionals
- PostgreSQL Notes for Professionals
- Comprehensive CI/CD Guide for Software and Data Projects

</details>

---

### If you improve this example ✍️
- Prefer **small deterministic outputs**
- Avoid magic defaults; record everything in the run manifest
- Add more examples by extending “minimal triplet” → “triplet + graph ingest” → “triplet + story node + evidence manifest”
