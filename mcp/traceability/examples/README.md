# 🧬 MCP Traceability Examples (KFM) ⛓️

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-2ea44f)
![Provenance](https://img.shields.io/badge/Provenance-⛓%20enforced-brightgreen)
![STAC](https://img.shields.io/badge/STAC-catalog-blue)
![DCAT](https://img.shields.io/badge/DCAT-metadata-blue)
![PROV--O](https://img.shields.io/badge/PROV--O-lineage-blueviolet)
![Policy](https://img.shields.io/badge/Policy-OPA%20%2B%20Conftest-purple)
![UI](https://img.shields.io/badge/UI-MapLibre%20%2B%20Cesium-informational)

**Folder:** `mcp/traceability/examples/README.md` 📍  
**Purpose:** Copy/paste-ready **traceability patterns** for Kansas Frontier Matrix (KFM): data lineage, evidence manifests, AI citations, UI provenance, and governance-grade audit trails — aligned with the **Master Coder Protocol (MCP)**.

> ✅ **Prime directive:** if it’s not cataloged with provenance, it doesn’t ship.  
> 🧠 **Human-readable + machine-checkable** is the sweet spot: Markdown for humans, JSON/YAML/PROV for machines.

---

<details>
  <summary><strong>🧭 Table of Contents</strong> (click)</summary>

- [What “traceability” means here](#what-traceability-means-here)
- [Core invariants you can test](#core-invariants-you-can-test)
- [Traceability surface map](#traceability-surface-map)
- [Examples](#examples)
  - [01 — Dataset lineage: Raw → Processed → Catalog → Graph](#01--dataset-lineage-raw--processed--catalog--graph)
  - [02 — Run manifest: deterministic + idempotent](#02--run-manifest-deterministic--idempotent)
  - [03 — Focus Mode answer as an artifact](#03--focus-mode-answer-as-an-artifact)
  - [04 — UI “map behind the map” provenance](#04--ui-map-behind-the-map-provenance)
  - [05 — Story Node: machine-ingestible Markdown](#05--story-node-machine-ingestible-markdown)
  - [06 — PR → PROV graph integration](#06--pr--prov-graph-integration)
  - [07 — Streaming / real-time traceability](#07--streaming--real-time-traceability)
  - [08 — OCI artifacts + Cosign signing](#08--oci-artifacts--cosign-signing)
  - [09 — Uncertainty + explainability hooks](#09--uncertainty--explainability-hooks)
  - [10 — Traceability matrix template](#10--traceability-matrix-template)
- [Validation & policy gates](#validation--policy-gates)
- [Project file map (📚 uses *all* project docs)](#project-file-map--uses-all-project-docs)
- [PDF portfolio packs: extraction helper](#pdf-portfolio-packs-extraction-helper)
- [How to add a new example](#how-to-add-a-new-example)

</details>

---

## What traceability means here

In KFM, traceability is not a “nice to have” — it’s the **architecture**:

- **No dataset or layer is a black box**: every visualization points back to **source + processing** (“the map behind the map”).[^ui_overview]
- **Raw inputs are immutable evidence**: treat `data/raw/` as a **trust boundary** and never edit it in-place.[^data_intake]
- **Pipelines are deterministic**: same inputs + same config → same outputs (idempotence), or you have a bug.[^data_intake]
- **Publishing requires boundary artifacts** (e.g., **STAC**, **DCAT**, **PROV**) so lineage is queryable and enforceable.[^arch_features]
- **AI answers are “first-class artifacts”**: every claim must cite sources; if the system can’t cite, it must refuse or mark uncertainty.[^ai_overview][^data_intake]
- **Governance is auditable**: key AI outputs and decisions get logged in an **immutable ledger**, and users can inspect provenance in UI panels.[^ai_overview]

---

## Core invariants you can test

These are “rules you can automate” ✅

### 🔒 Data invariants
- `data/raw/` is immutable (no edits, only new ingests).[^data_intake]
- `data/processed/` changes only via pipeline output (no manual tweaking).[^data_intake]
- Every published dataset has:
  - DCAT metadata (license, source, etc.)[^tech_doc]
  - STAC item(s) for spatial/temporal assets[^arch_features]
  - PROV lineage linking inputs → activity → outputs[^arch_features]

### 🧠 AI invariants
- Every Focus Mode answer includes citations (hard gate).[^ai_overview][^data_intake]
- If a claim can’t be supported, the system refuses or expresses uncertainty.[^ai_overview]
- AI outputs are logged with provenance and compliance metadata.[^ai_overview]

### 🗺 UI invariants
- UI is “read-only” with respect to data; changes must go through governed pipelines/commits.[^data_intake]
- Layers, popups, exports display attribution + license info.[^ui_overview][^tech_doc]

### ⚙️ DevOps invariants
- CI enforces policy gates (OPA/Conftest) for metadata, governance, and traceability.[^additional_ideas]
- Dev history can be represented as PROV (PR activity ↔ commits ↔ agents) and queried like any other lineage.[^latest_ideas]

---

## Traceability surface map

```mermaid
flowchart LR
  A[📥 Raw Inputs<br/>data/raw] -->|deterministic ETL| B[🧪 Work Staging<br/>data/work]
  B --> C[✅ Processed Outputs<br/>data/processed]
  C --> D[🗃️ Catalog<br/>STAC + DCAT<br/>data/catalog]
  C --> E[⛓️ Provenance<br/>PROV records<br/>data/provenance]
  D --> F[🧠 Knowledge Graph<br/>Neo4j]
  E --> F
  F --> G[🌐 API<br/>REST/GraphQL]
  G --> H[🗺️ UI<br/>MapLibre/Cesium]
  F --> I[🤖 Focus Mode]
  I --> J[📜 Governance Ledger<br/>(append-only)]
  H --> J
```

---

## Examples

> 💡 All examples use **stable IDs**, **machine-readable manifests**, and **human-readable Markdown** so they can be audited and automated.

---

### 01 — Dataset lineage: Raw → Processed → Catalog → Graph

**Goal:** show a full chain from “bytes on disk” to “something the UI/AI can cite.”

#### 📁 Suggested layout (example)
```text
📦 data/
  📁 raw/
    📁 usgs_nwis_river_gauges/
      📄 fetch_2026-01-21T00-00Z.json
  📁 work/
    📁 usgs_nwis_river_gauges/
      📄 normalize.parquet
  📁 processed/
    📁 usgs_nwis_river_gauges/
      🗺️ gauges.geojson
      🧱 gauges.pmtiles
  📁 catalog/
    📁 dcat/
      📄 usgs_nwis_river_gauges.dataset.json
    📁 stac/
      📁 usgs_nwis_river_gauges/
        📄 item_2026-01-21T00-00Z.json
  📁 provenance/
    📄 prov_run_2026-01-21T00-00Z.jsonld
```

#### 🧾 DCAT dataset (minimal-ish template)
```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/"
  },
  "@type": "dcat:Dataset",
  "@id": "dcat:usgs_nwis_river_gauges",
  "dct:title": "USGS NWIS River Gauge Readings (Kansas)",
  "dct:license": "https://example.org/license/public-domain",
  "dct:source": "https://waterdata.usgs.gov/",
  "dct:description": "Real-time and historical gauge readings ingested via KFM pipeline.",
  "dct:publisher": "KFM",
  "dct:spatial": "Kansas, USA",
  "dct:temporal": "varies; see STAC items"
}
```

#### 🗺️ STAC item (minimal-ish template)
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "stac:usgs_nwis_river_gauges/2026-01-21T00:00:00Z",
  "properties": {
    "datetime": "2026-01-21T00:00:00Z",
    "license": "public-domain",
    "kfm:dcat_dataset_id": "dcat:usgs_nwis_river_gauges"
  },
  "geometry": null,
  "bbox": null,
  "assets": {
    "pmtiles": {
      "href": "oci://REGISTRY/REPO@sha256:REPLACE_ME",
      "type": "application/vnd.pmtiles",
      "roles": ["data"]
    },
    "geojson": {
      "href": "data/processed/usgs_nwis_river_gauges/gauges.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

#### ⛓️ PROV record (JSON-LD sketch)
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://example.org/kfm#"
  },
  "@id": "prov:activity/ingest/usgs_nwis_river_gauges/2026-01-21T00:00:00Z",
  "@type": "prov:Activity",
  "prov:used": [
    { "@id": "raw:usgs_nwis_fetch/2026-01-21T00:00:00Z" }
  ],
  "prov:wasAssociatedWith": { "@id": "agent:kfm_ingest_bot" },
  "prov:generated": [
    { "@id": "stac:usgs_nwis_river_gauges/2026-01-21T00:00:00Z" },
    { "@id": "dcat:usgs_nwis_river_gauges" }
  ],
  "kfm:notes": "Raw input immutable; processed outputs promoted only after validation."
}
```

---

### 02 — Run manifest: deterministic + idempotent

**Goal:** make every pipeline execution a **queryable audit event** with integrity checks.[^additional_ideas]

#### 📄 `run_manifest.json` (template)
```json
{
  "run_id": "run_2026-01-21T00:00:00Z_usgs_nwis_river_gauges",
  "run_time": "2026-01-21T00:00:00Z",
  "idempotency_key": "usgs_nwis_river_gauges|window=2026-01-21T00:00Z",
  "inputs": [
    {
      "kind": "api",
      "name": "USGS NWIS",
      "source_url": "https://waterdata.usgs.gov/",
      "retrieved_at": "2026-01-21T00:00:10Z",
      "raw_artifact": "data/raw/usgs_nwis_river_gauges/fetch_2026-01-21T00-00Z.json",
      "raw_sha256": "REPLACE_ME"
    }
  ],
  "outputs": [
    {
      "path": "data/processed/usgs_nwis_river_gauges/gauges.pmtiles",
      "sha256": "REPLACE_ME",
      "stac_item_id": "stac:usgs_nwis_river_gauges/2026-01-21T00:00:00Z"
    }
  ],
  "environment": {
    "pipeline_version": "REPLACE_ME",
    "tool_versions": {
      "python": "REPLACE_ME",
      "gdal": "REPLACE_ME"
    }
  },
  "canonical_digest": "sha256:REPLACE_ME"
}
```

#### ✅ Idempotent ingest (pseudo-pattern)
```text
1) compute idempotency_key
2) acquire lock (DB transaction / Redis SETNX / etc.)
3) if key already processed → exit (no duplicates)
4) else run deterministic ETL + emit artifacts + release lock
```

---

### 03 — Focus Mode answer as an artifact

**Goal:** treat an AI answer as something that must be **provable**, **citable**, and **auditable**.[^ai_overview][^data_intake]

#### 🗣 Example answer (with footnotes)
> **Q:** What’s the current water level of the Kansas River at Topeka?  
> **A:** As of **2026-01-21T20:00 local**, the Kansas River gauge at Topeka reports **X ft**.[^ex_nwis_dcat]  
> **Inputs:** station entity resolved via the knowledge graph, then latest reading fetched from PostGIS; the reading is logged as a PROV input entity with timestamp.[^data_intake]

#### ⛓ Answer PROV sketch
```json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@id": "prov:answer/topeka_gauge/2026-01-21T20:00",
  "@type": "prov:Entity",
  "prov:wasGeneratedBy": { "@id": "prov:activity/focus_mode_qna/2026-01-21T20:00" },
  "prov:wasDerivedFrom": [
    { "@id": "dcat:usgs_nwis_river_gauges" },
    { "@id": "graph:station/usgs/REPLACE_ME" },
    { "@id": "db:reading/usgs/REPLACE_ME@2026-01-21T01:59:59Z" }
  ]
}
```

> 🧯 **Hard gate idea:** run an output policy check that fails if any claim lacks a citation.[^data_intake][^additional_ideas]

---

### 04 — UI “map behind the map” provenance

**Goal:** every layer/feature can show:
- source
- license
- processing summary
- sensitivity flags (if any)[^ui_overview][^ai_overview][^tech_doc]

#### 🧩 Layer registry entry (example shape)
```json
{
  "layer_id": "river_gauges_realtime",
  "title": "Kansas River Gauges (Real-time)",
  "data": {
    "api_endpoint": "/api/layers/river_gauges?at=latest",
    "dcat_dataset_id": "dcat:usgs_nwis_river_gauges",
    "stac_item_id": "stac:usgs_nwis_river_gauges/2026-01-21T00:00:00Z"
  },
  "provenance": {
    "source_label": "USGS NWIS",
    "license": "Public Domain",
    "processed_by": "KFM deterministic pipeline",
    "export_attribution": "© USGS (via NWIS), processed by KFM"
  },
  "governance": {
    "classification": "public",
    "redaction": "none"
  }
}
```

> 🧭 UX cue: add an **Info ⓘ** icon for each layer that opens a “Layer Provenance” panel.[^ai_overview]

---

### 05 — Story Node: machine-ingestible Markdown

**Goal:** Story Nodes are narratives **under version control** with citations and stable graph IDs, and must separate **fact vs interpretation**.[^markdown_guide][^ui_overview]

#### 🧾 Story Node skeleton (copy/paste)
```markdown
---
kfm_story_id: story.kfm.example.dustbowl_1930s.v1
title: "Dust Bowl Impacts in Kansas (1930s) 🌾"
time:
  start: "1930-01-01"
  end: "1940-12-31"
spatial:
  bbox: [-102.0, 36.9, -94.6, 40.0]
entities:
  - graph:place:ks
  - graph:event:dust_bowl
citations:
  - id: src_drought
    ref: dcat:REPLACE_ME
    note: "Drought index dataset used for map layer."
  - id: src_map
    ref: stac:REPLACE_ME
    note: "Georeferenced historical map layer."
---

## ✅ Facts (cited)
Kansas experienced severe drought conditions during the 1930s.[^src_drought]

## 🧠 Interpretation / analysis (clearly labeled)
A plausible contributing factor is land-use practice interacting with climatic variability (hypothesis).  
Confidence: medium (0.6). Evidence: see cited drought layer + land-use data.[^src_drought]

## 🗺 Map steps (optional, machine-readable hints)
- Step 1: zoom to western Kansas; enable drought index layer
- Step 2: overlay historical land-use layer; adjust timeline to 1936
- Step 3: show summary chart for selected counties

[^src_drought]: (src_drought) dcat:REPLACE_ME
[^src_map]: (src_map) stac:REPLACE_ME
```

---

### 06 — PR → PROV graph integration

**Goal:** treat dev workflow as provenance: PRs as Activities, commits as Entities, authors/reviewers as Agents.[^latest_ideas]

#### 🔁 JSON-LD sketch
```json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@id": "prov:pr/1234",
  "@type": "prov:Activity",
  "prov:used": [
    { "@id": "git:commit/abc123" },
    { "@id": "git:commit/def456" }
  ],
  "prov:wasAssociatedWith": [
    { "@id": "agent:alice" },
    { "@id": "agent:ci_bot" }
  ],
  "prov:generated": [
    { "@id": "git:commit/merge789" }
  ]
}
```

#### 🔍 Example questions this enables
- “Which code version produced this dataset and who reviewed it?”[^latest_ideas]
- “Show all merged PRs that modified water-quality ingestion.”

---

### 07 — Streaming / real-time traceability

**Goal:** streaming data is “many small datasets over time,” still governed by provenance-first rules.[^data_intake]

#### 🌊 Example: river gauge layer
- UI requests latest readings via API
- API queries PostGIS for `max(timestamp)` per station
- UI displays “Source: USGS NWIS” from DCAT metadata
- If station is sensitive, omit or restrict by classification rules[^data_intake][^tech_doc]

#### ⛓ PROV must record dynamic reads
Even if the answer is “live,” provenance logs that the answer used **that specific reading** with **timestamp**.[^data_intake]

---

### 08 — OCI artifacts + Cosign signing

**Goal:** ship data artifacts like containers: versioned, pullable, immutable by digest, and verifiable by signature.[^additional_ideas]

#### 📦 Push + sign (example commands)
```bash
# store data artifact in an OCI registry (example)
oras push ghcr.io/ORG/kfm-data/usgs-nwis-gauges:2026-01-21 \
  --artifact-type application/vnd.kfm.pmtiles \
  ./gauges.pmtiles:application/vnd.pmtiles

# sign it (Sigstore Cosign)
cosign sign ghcr.io/ORG/kfm-data/usgs-nwis-gauges@sha256:REPLACE_ME

# verify before use
cosign verify ghcr.io/ORG/kfm-data/usgs-nwis-gauges@sha256:REPLACE_ME
```

> 🔐 This strengthens chain-of-custody: artifacts can be referenced in STAC by immutable digest.[^additional_ideas]

---

### 09 — Uncertainty + explainability hooks

**Goal:** track and communicate uncertainty (e.g., georeferencing error, NLP extraction confidence) and surface explainability in UI/audit panels.[^design_audit][^ai_overview][^arch_features]

#### 🧾 Example uncertainty fields
```json
{
  "kfm:confidence": 0.62,
  "kfm:uncertainty": {
    "type": "georeference_rmse_meters",
    "value": 37.5
  }
}
```

#### 🔎 Explainability UI hook
- Provide an **audit panel** showing which graph relationships / data points influenced the answer, plus any governance flags.[^ai_overview]

---

### 10 — Traceability matrix template

**Goal:** MCP-style traceability matrix linking **requirements → implementation → tests → evidence**.

> 🧠 Think of this as the “control panel” for end-to-end accountability.

| Req/Claim ID | Feature / Hypothesis | Artifacts (STAC/DCAT/PROV/etc.) | Tests / Gates | Evidence Link | Owner |
|---|---|---|---|---|---|
| TR-001 | Provenance-first publishing | DCAT + STAC + PROV present | Conftest `policy:catalog_required` | `prov_run_*.jsonld` | @you |
| TR-002 | Focus Mode always cites | Answer includes footnotes | OPA output check | governance ledger entry | @you |
| TR-003 | No raw mutation | `data/raw/` write-protected | CI check + git diff guard | audit log | @you |
| TR-004 | Sensitive coords protected | Redaction enforced | Policy gate | UI provenance panel | @you |

---

## Validation & policy gates

Policy gates should run automatically in CI to enforce governance rules (metadata completeness, licensing, citation coverage, redaction, etc.).[^additional_ideas]

**Common gates to include:**
- ✅ Every dataset has a license field.[^tech_doc]
- ✅ STAC/DCAT/PROV present for published outputs.[^arch_features]
- ✅ Focus Mode output has citations (hard gate).[^ai_overview]
- ✅ Sensitive location policy enforced (generalize/hide).[^tech_doc][^markdown_guide]

---

## Project file map  🗂️ uses *all* project docs

This README is grounded in (and cross-wires) the project’s documentation packs:

### 🧱 Core KFM docs
- **Data Intake philosophy + trust boundary + determinism** → `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`[^data_intake]
- **AI: citations, governance ledger, provenance UI, audit panel** → `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`[^ai_overview]
- **UI: “map behind the map”, story presentation, provenance in popups** → `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`[^ui_overview]
- **Pipeline promotion + catalog/provenance + no overwrite without trace** → `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`[^arch_features]
- **Licensing + sensitive locations + CARE-related practices** → `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`[^tech_doc]

### 🚀 “Next layer” proposals
- **PR → PROV integration + CI invariants** → `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`[^latest_ideas]
- **Human-in-loop + evidence-based AI copilot / generative mapping** → `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`[^innov_concepts]
- **Run manifests, idempotent ingest, OCI artifacts, Cosign, policy gates** → `Additional Project Ideas.pdf`[^additional_ideas]

### 📦 Deep resource packs (PDF portfolios)
These are **PDF portfolios** that contain multiple embedded books/docs (see extraction helper below):
- `AI Concepts & more.pdf` (AI/ML theory + engineering references)[^ai_pack]
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (GIS/WebGL/virtual worlds)[^maps_pack]
- `Various programming langurages & resources 1.pdf` (multi-language engineering + architecture refs)[^prog_pack]
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (data mgmt + Bayesian + science refs)[^data_pack]

---

## PDF portfolio packs: extraction helper

If you want to browse the embedded documents inside the portfolio PDFs, extract them locally.

### 🐍 Minimal extractor (Python)
```python
# Extract embedded files from a PDF portfolio (NameTree / EmbeddedFiles).
# Usage: python extract_portfolio.py "AI Concepts & more.pdf" ./out

import sys
from pathlib import Path
import PyPDF2

def collect_names(node):
    node = node.get_object()
    pairs = []
    if "/Names" in node:
        arr = node["/Names"]
        for i in range(0, len(arr), 2):
            pairs.append((arr[i], arr[i+1]))
    if "/Kids" in node:
        for kid in node["/Kids"]:
            pairs.extend(collect_names(kid))
    return pairs

def main(pdf_path, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    reader = PyPDF2.PdfReader(pdf_path)
    root = reader.trailer["/Root"]
    names = root.get("/Names")
    if not names:
        print("No /Names in PDF")
        return

    names = names.get_object()
    if "/EmbeddedFiles" not in names:
        print("No embedded files found")
        return

    emb = names["/EmbeddedFiles"]
    pairs = collect_names(emb)

    for filename, filespec in pairs:
        fs = filespec.get_object()
        ef = fs["/EF"]["/F"].get_object()
        data = ef.get_data()
        target = out_dir / str(filename)
        target.write_bytes(data)
        print("extracted:", target)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
```

---

## How to add a new example

1. Create a new section: `11 — <your example name>` 🧩  
2. Include:
   - **Goal**
   - **Artifacts**
   - **Copy/paste templates** (JSON/YAML/Markdown)
   - **Policy checks** (what would fail CI if wrong)
3. Link to relevant references using the footnotes below 📌

**PR checklist ✅**
- [ ] Has DCAT + license + source
- [ ] Has STAC for geospatial assets (if applicable)
- [ ] Has PROV linking inputs → activity → outputs
- [ ] Has run manifest (for pipelines / updates)
- [ ] Passes Conftest/OPA policy gates
- [ ] UI provenance/attribution included (if UI-facing)
- [ ] AI outputs cite sources (if AI-facing)
- [ ] Sensitive location rules respected (CARE-aware)

---

## Footnotes & references 📎

[^data_intake]: **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf** (provenance-first intake, immutable raw trust boundary, deterministic ETL, streaming provenance patterns).
[^ai_overview]: **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf** (citations-first AI, audit panel, governance ledger, user-visible provenance).
[^ui_overview]: **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf** (map behind the map, provenance in popups/side panels, story narrative UI).
[^arch_features]: **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf** (catalog + provenance linkage, staged promotion, versioning and no-overwrite-without-trace).
[^tech_doc]: **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** (licensing rules, sensitive location handling, CARE-aware constraints).
[^latest_ideas]: **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf** (GitHub PR → PROV graph integration + CI invariants).
[^innov_concepts]: **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf** (human-in-loop, evidence-based query copilot, generative mapping).
[^additional_ideas]: **Additional Project Ideas.pdf** (run manifest, deterministic/idempotent ingest, OCI artifact distribution, Cosign signatures, policy gates).
[^design_audit]: **Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf** (uncertainty quantification gap + suggested enhancements).
[^markdown_guide]: **MARKDOWN_GUIDE_v13.md.gdoc** (Story Node citation requirements, fact vs interpretation separation, Focus Mode hard gates).
[^ai_pack]: **AI Concepts & more.pdf** (PDF portfolio: embedded AI/ML references).
[^maps_pack]: **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** (PDF portfolio: embedded mapping/WebGL/GIS references).
[^prog_pack]: **Various programming langurages & resources 1.pdf** (PDF portfolio: embedded multi-language engineering references).
[^data_pack]: **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** (PDF portfolio: embedded data mgmt + Bayesian + science references).
[^ex_nwis_dcat]: Example DCAT reference used in this README: `dcat:usgs_nwis_river_gauges` (replace with real catalog IDs in your repo).

