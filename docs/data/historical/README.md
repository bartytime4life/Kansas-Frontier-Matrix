---
title: "🕰️ Historical Data & Archives — Domain Runbook"
description: "How historical archives (maps, documents, newspapers, treaties, photos, oral histories) are ingested, cataloged, versioned, and surfaced in KFM with STAC/DCAT/PROV + FAIR+CARE governance."
path: "docs/data/historical/README.md"
version: "v0.1.0"
last_updated: "2026-01-20"
release_stage: "Draft / Governed"
status: "Active (Draft)"
review_cycle: "Quarterly · Historical Domain Steward + FAIR+CARE Council"
license: "CC-BY-4.0"

# Protocol + profile alignment (keep these in sync with repo standards)
markdown_protocol_version: "KFM-MDP v11.2.6"
stac_profile_version: "KFM-STAC v11"
dcat_profile_version: "KFM-DCAT v11"
prov_profile_version: "KFM-PROV v11"

ontology_alignment:
  cidoc_crm: true
  owl_time: true
  geosparql: true

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

classification: "Public Documentation"
sensitivity_level: "Low"
care_label: "CARE-A / Review Required (Domain Default)"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:historical:readme:v0.1.0"
commit_sha: "<latest-commit-hash>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

<div align="center">

# 🕰️ Historical Data & Archives (KFM)  
### *A governed runbook for turning Kansas history into traceable, searchable, mappable evidence* 🧭🗺️

<img src="https://img.shields.io/badge/Domain-Historical%20Data%20%26%20Archives-blue" />
<img src="https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT%20%7C%20PROV-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-success" />
<img src="https://img.shields.io/badge/UI-Timeline%20%2B%20Story%20Nodes-orange" />
<img src="https://img.shields.io/badge/AI-Focus%20Mode%20%28Citations%20Required%29-critical" />

</div>

> **Core idea:** In KFM, history isn’t trapped in books — it’s **mapped, searchable, and woven into present-day context**, with every claim traceable to sources and processing steps.:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Quick Links
- 📘 **Pipeline invariant (must not regress):** ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode:contentReference[oaicite:2]{index=2}
- 🧱 **Metadata alignment policy (required):** STAC + DCAT + PROV for every dataset/evidence artifact:contentReference[oaicite:3]{index=3}
- 🗂️ **Domain expansion rule:** Each domain maintains a runbook under `docs/data/<domain>/` (this file):contentReference[oaicite:4]{index=4}
- 🎞️ **Story Nodes (narrative playback):** step-driven map states + citations:contentReference[oaicite:5]{index=5}

---

## 📘 Overview

### Purpose
This README is the **domain runbook** for all *historical* sources and evidence artifacts in KFM — including historical maps & surveys, archival documents, treaties, newspapers, photos, and structured “event” datasets.

KFM’s historical domain supports:
- **Digital humanities + historical research** (events, archives, cultural heritage mapped in time/space):contentReference[oaicite:6]{index=6}
- **Education & public engagement** via **guided Story Nodes** (narrative + map + timeline):contentReference[oaicite:7]{index=7}
- **Evidence-first Q&A** via Focus Mode (AI assistant) that must provide citations:contentReference[oaicite:8]{index=8}

### Scope
| ✅ In Scope | 🚫 Out of Scope |
|---|---|
| Historical maps, surveys, plats (georeferenced rasters + derived vectors):contentReference[oaicite:9]{index=9} | Live/real-time sensor feeds (belongs in relevant “live” domains):contentReference[oaicite:10]{index=10} |
| OCR’d documents, newspapers, letters, reports (searchable text + linked entities):contentReference[oaicite:11]{index=11} | “Uncited narrative” (never allowed in KFM):contentReference[oaicite:12]{index=12} |
| Structured historical events (with temporal intervals + locations) | Private/sensitive cultural locations without governance clearance:contentReference[oaicite:13]{index=13} |
| Story Nodes explaining history in space/time:contentReference[oaicite:14]{index=14} | Direct UI reads from Neo4j (UI must go through governed API):contentReference[oaicite:15]{index=15} |

---

## 🗂️ Directory Layout

### What lives where (canonical staging)
KFM uses a staged lifecycle for data domains: raw → working → processed, then publishes metadata into canonical catalogs.:contentReference[oaicite:16]{index=16}

```text
📁 data/
├─ 📁 raw/                   # immutable-ish source drops (do not “clean” here)
│  └─ 📁 historical/
├─ 📁 work/                  # intermediate processing outputs (scratch / reproducible)
│  └─ 📁 historical/
├─ 📁 processed/             # publishable data products (COG, GeoParquet, text corpora, etc.)
│  └─ 📁 historical/
├─ 📁 stac/                  # STAC Collections + Items (published indexing)
├─ 📁 catalog/dcat/          # DCAT Dataset records (discovery)
└─ 📁 prov/                  # PROV bundles (lineage + agents + activities)
```
**Why this matters:** PROV must link raw → work → processed end-to-end so any artifact can be traced to original sources and exact transformations.:contentReference[oaicite:17]{index=17}

### This documentation module
```text
📁 docs/data/historical/
├─ 📄 README.md                        # (this file) domain runbook:contentReference[oaicite:18]{index=18}
├─ 📁 land-treaties/                   # example high-governance historical submodule:contentReference[oaicite:19]{index=19}
├─ 📁 templates/                       # dataset/story/prov templates (recommended)
├─ 📁 manifests/                       # checksums + evidence manifests (recommended)
└─ 📄 glossary.md                      # domain terms (recommended)
```

> 🧩 **Story content locations (watch versioning):**  
> - Some designs reference `web/story_nodes/` as story content storage:contentReference[oaicite:20]{index=20}  
> - v13 governance references a reorganized canonical home under `docs/reports/story_nodes/` (draft vs published):contentReference[oaicite:21]{index=21}  
>  
> ✅ **Rule of thumb:** treat `docs/reports/story_nodes/` as canonical for governed stories, and keep compatibility shims if older paths exist.

---

## 🧱 Historical Data Types in KFM

KFM treats historical artifacts as **first-class data layers** + **knowledge-graph entries** (not “attachments”).:contentReference[oaicite:22]{index=22}

### 1) 🗺️ Historical Maps & Surveys
- Scanned historical maps are **georeferenced** and served as map layers.  
- Each layer carries metadata: archive source, publication year, original scale, who georeferenced it, plus accuracy metrics like RMS error.:contentReference[oaicite:23]{index=23}
- Map series are grouped across eras (e.g., USGS topo sets) to enable era toggling and “history unfolding.”:contentReference[oaicite:24]{index=24}

### 2) 📰 Documents & Newspapers (Searchable Text)
- Archival documents and newspaper articles are indexed; scanned sources are OCR’d so text is searchable.:contentReference[oaicite:25]{index=25}
- Text is linked to places, dates, and topics in the graph; sources are cited (e.g., KSHS, LOC).:contentReference[oaicite:26]{index=26}

### 3) 🧾 Treaties & Governance-heavy Archives
High-governance domains (like land treaties) should live in submodules under this historical domain.:contentReference[oaicite:27]{index=27}

---

## 🧠 Data Model & Ontology Alignment

### Knowledge graph (Neo4j)
The AI + retrieval layers rely on a semantically structured graph. For history + time, KFM references ontologies such as:
- **CIDOC-CRM** (history/cultural heritage)
- **OWL-Time** (temporal intervals and relationships):contentReference[oaicite:28]{index=28}

This enables queries like: “What events happened here in the 1930s?” by pulling events for a location + timeframe, then summarizing with citations.:contentReference[oaicite:29]{index=29}

---

## 📦 Required Boundary Artifacts (Non‑Negotiable)

Every dataset or evidence artifact must ship with:
1) **STAC Collection + Items**  
2) **DCAT Dataset record**  
3) **PROV bundle**:contentReference[oaicite:30]{index=30}

These profiles are validated in CI; missing fields or broken metadata fails the build.:contentReference[oaicite:31]{index=31}

### Cross-layer linkage expectations
- STAC Items point to the actual assets in `data/processed/**` and carry source attribution + license info:contentReference[oaicite:32]{index=32}
- DCAT points to STAC and/or stable distribution endpoints:contentReference[oaicite:33]{index=33}
- PROV links raw → work → processed, including run IDs or commit hashes:contentReference[oaicite:34]{index=34}
- Graph nodes reference catalog IDs rather than duplicating bulky data:contentReference[oaicite:35]{index=35}

---

## 🧪 Ingestion Workflow (Historical)

KFM’s intake design emphasizes:
- **Provenance-first** (nothing publishable without lineage)  
- **AI never operates in shadows** (every action generates a record)  
- **Staged workflows** (raw → work → processed → catalogs)

### ✅ Step-by-step (maintainer runbook)

1) **Source acquisition & licensing**
   - Capture source URL/archive reference, license status, and any usage constraints.:contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}

2) **Drop raw files**
   - Put original scans/files in:  
     `data/raw/historical/<collection>/<source_id>/...`:contentReference[oaicite:39]{index=39}

3) **Create an evidence manifest**
   - Include checksums, retrieval date, and sensitivity label (see template below).  
   - This supports reproducibility and auditability (provenance is first-class).:contentReference[oaicite:40]{index=40}

4) **Transform in `data/work/`**
   - Georeference maps, OCR documents, clean text, derive vectors, etc.  
   - Keep pipelines deterministic/idempotent when possible (re-runnable).:contentReference[oaicite:41]{index=41}

5) **Publish to `data/processed/`**
   - Output “ready to serve” artifacts (COG, GeoParquet, index corpora).  
   - Treat OCR corpora or AI-derived layers as **first-class datasets** with full provenance.:contentReference[oaicite:42]{index=42}

6) **Generate STAC/DCAT/PROV**
   - Emit catalogs into canonical locations (`data/stac/`, `data/catalog/dcat/`, `data/prov/`).:contentReference[oaicite:43]{index=43}

7) **Load graph + spatial store**
   - PostGIS for geometry-heavy operations; Neo4j for semantic context and references.:contentReference[oaicite:44]{index=44}

8) **Expose via governed API (never direct graph reads from UI)**
   - UI must not query Neo4j directly; API enforces redaction and contracts.:contentReference[oaicite:45]{index=45}:contentReference[oaicite:46]{index=46}

9) **Optional: write a Story Node**
   - Explain the dataset in a narrative that drives map state + timeline playback.:contentReference[oaicite:47]{index=47}

---

## 🗺️ Georeferencing & Time Travel UX

### Web mapping + timeline slider
KFM’s mapping stack is designed to support time slicing:
- MapLibre GL JS supports vector/raster layers and **timeline slider controls** for time slices:contentReference[oaicite:48]{index=48}
- Cesium is considered for 3D/time-dynamic visualization; KML can serve as a lightweight 3D option:contentReference[oaicite:49]{index=49}

### Practical pipeline notes (maps)
- Use QGIS for georeferencing and export the georeferenced raster for the pipeline:contentReference[oaicite:50]{index=50}
- Preserve georeferencing accuracy metrics (e.g., RMS error) in metadata:contentReference[oaicite:51]{index=51}

---

## 📰 OCR + Semantic Extraction (Documents)

KFM’s historical ingestion design includes:
- OCR of scanned documents and newspapers for searchability:contentReference[oaicite:52]{index=52}
- Linking documents to places, dates, and topics via the graph:contentReference[oaicite:53]{index=53}
- Proposals include scaling document ingestion with OCR + structured metadata extraction

---

## 🎞️ Story Nodes for Historical Narratives

### Why Story Nodes exist
Story Nodes are a core mechanism to make Kansas history explorable:
- Domain experts can contribute stories by adding files (no code required), subject to review:contentReference[oaicite:55]{index=55}
- The UI renders Markdown narrative and advances step-by-step; each step updates map state (layers, view, timeline year):contentReference[oaicite:56]{index=56}

### What a Story Node controls
A story step can:
- Pan/zoom to a location
- Toggle layers on/off
- Set the time slider / year
- Highlight features:contentReference[oaicite:57]{index=57}

### Suggested (governed) Story Node structure
```text
📁 docs/reports/story_nodes/
├─ 📁 draft/
│  └─ 📁 historical/
│     └─ 📁 dust-bowl-1930s/
│        ├─ 📄 story.md
│        ├─ 📄 story.json            # step -> map state (camera, layers, time)
│        ├─ 📄 citations.yaml        # structured citations (recommended)
│        └─ 📁 assets/               # images, scans, clips
└─ 📁 published/
   └─ 📁 historical/...
```
(Story content governance path: v13 expects `docs/reports/story_nodes/` with draft vs published separation.):contentReference[oaicite:58]{index=58}

---

## 🤖 Focus Mode + Historical Q&A (Evidence-First)

### How the AI retrieves historical context
Focus Mode uses a hybrid retrieval pipeline (structured + unstructured) commonly called RAG:
- Queries Neo4j + GIS stores for structured context
- Uses semantic search across text documents
- Links results back to their sources for traceability:contentReference[oaicite:59]{index=59}

### Hard rule: citations required (or refuse)
KFM policy gates require citations for AI outputs; if Focus Mode can’t provide sources, it should refuse.:contentReference[oaicite:60]{index=60}

> ✅ This protects historical narratives from “hallucinated history,” and keeps KFM accountable.

---

## 🛡️ Governance: FAIR+CARE, Provenance, Sensitivity

### FAIR + CARE are enforced (not aspirational)
- KFM enforces FAIR by requiring metadata + provenance; CARE by designating sensitive data and requiring community authority for its use:contentReference[oaicite:61]{index=61}
- Provenance is first-class: derived info must carry lineage, including citations in Focus Mode outputs:contentReference[oaicite:62]{index=62}

### Policy gates (minimum set)
Automated checks include:
- Schema validation
- STAC/DCAT/PROV completeness
- License presence
- Sensitivity classification
- Provenance completeness:contentReference[oaicite:63]{index=63}

### Sovereignty exceptions (advanced, optional pattern)
For exceptional cases (e.g., restricted cultural archives), policy bundles can enforce **fail-closed** governance in CI using OPA/Conftest, signature verification, and approved agent rosters.:contentReference[oaicite:64]{index=64}

---

## 🧪 Validation & CI Expectations (Historical Domain)

CI should block merges when:
- YAML front-matter or required sections are missing (Markdown protocol enforcement):contentReference[oaicite:65]{index=65}
- Links/citations are broken:contentReference[oaicite:66]{index=66}
- STAC/DCAT/PROV fail JSON schema validation:contentReference[oaicite:67]{index=67}
- Sensitive content or classification downgrades are detected:contentReference[oaicite:68]{index=68}

---

## 🧰 Templates

### 1) Evidence Manifest (recommended)
```yaml
# docs/data/historical/manifests/<source_id>.yaml
source_id: "kshs_railroad_maps_1870s"
title: "Railroad Expansion Maps (1870s)"
source_archive: "Kansas State Historical Society"
retrieved_at: "2026-01-20"
license: "TBD"
sensitivity_level: "Low"
care_label: "CARE-A"
files:
  - path: "data/raw/historical/maps/kshs_railroad_maps_1870s/map_1872_scan.tif"
    sha256: "<sha256>"
  - path: "data/raw/historical/maps/kshs_railroad_maps_1870s/map_1878_scan.tif"
    sha256: "<sha256>"
notes:
  - "Georeference planned; capture RMS error in metadata."
```

### 2) Story Node Step Config (illustrative)
```json
{
  "id": "dust-bowl-1930s",
  "steps": [
    {
      "title": "Drought severity 1930–1936",
      "time": { "start": "1930-01-01", "end": "1936-12-31" },
      "map": {
        "camera": { "center": [-98.5, 38.5], "zoom": 5.8 },
        "layers_on": ["kfm.ks.drought.severity.v1"],
        "layers_off": ["kfm.ks.precip.normals.v1"]
      },
      "citations": [
        "stac:item:kfm.ks.drought.severity.1930_1936.v1",
        "prov:bundle:kfm.run.2026-01-20T00:00:00Z"
      ]
    }
  ]
}
```
(Story playback drives map state and timeline changes in the UI.):contentReference[oaicite:69]{index=69}

---

## 🧪 Example Use Case: Dust Bowl as “Historical + Modeling”
KFM’s modeling examples include combining:
- 1930–1936 drought severity maps (choropleth)
- Dust storm layers
- Population shifts (1930–1950)
- Crop yield graphs and other contextual analytics

This is exactly why the historical domain must be **cataloged + provenance-backed**: it becomes usable for “Why?” and “What if?” explorations without losing context.:contentReference[oaicite:71]{index=71}

---

## 🚧 Roadmap & Future Proposals (Mark clearly as “planned”)

Planned/idea-stage capabilities referenced across project proposal docs:
- **Kansas From Above**: richer 3D/2D experiences with camera transitions and historical layers
- **Scaled document ingestion**: OCR + structured semantic extraction for bulk historical archives
- **4D digital twin / “time machine” concepts** for historical change visualization (including AR overlays)

> 🔎 Governance note: future UX should still enforce evidence-first narrative and “no unsourced additions.”:contentReference[oaicite:76]{index=76}

---

## 📚 Project Files Used (Source Map)

**Core KFM design/architecture**
- *Comprehensive Technical Documentation* — historical archives, georeferenced maps, OCR docs, sourcing:contentReference[oaicite:77]{index=77}
- *Comprehensive Architecture, Features, and Design* — provenance-first + FAIR+CARE enforcement, policy gates:contentReference[oaicite:78]{index=78}:contentReference[oaicite:79]{index=79}
- *AI System Overview* — RAG + Neo4j ontology alignment (CIDOC-CRM, OWL-Time):contentReference[oaicite:80]{index=80}
- *Comprehensive UI System Overview* — Story Nodes contribution model + playback behaviors:contentReference[oaicite:81]{index=81}
- *Data Intake – Technical & Design Guide* — provenance-first staged workflows; PostGIS+Neo4j roles:contentReference[oaicite:83]{index=83}

**Forward-looking / proposal packs**
- *Latest Ideas & Future Proposals* — 3D “Kansas From Above” + scaled OCR ingestion
- *Innovative Concepts to Evolve KFM* — 4D digital twin + AR overlays + governance signals
- *Pulse Ideas* — policy bundle patterns and metadata/ontology anchoring examples:contentReference[oaicite:88]{index=88}:contentReference[oaicite:89]{index=89}

**Geospatial design**
- *Open-Source Geospatial Historical Mapping Hub Design* — MapLibre timeline slider + Cesium/KML options:contentReference[oaicite:90]{index=90}

**Reference libraries (PDF portfolios — open in Acrobat to access embedded resources)**
- *AI Concepts & more* (PDF portfolio):contentReference[oaicite:91]{index=91}
- *Maps/GoogleMaps/VirtualWorlds/Archaeological/Geospatial/WebGL* (PDF portfolio):contentReference[oaicite:92]{index=92}
- *Data Management/Theories/Architectures/Bayesian Methods* (PDF portfolio):contentReference[oaicite:93]{index=93}
- *Various programming languages & resources* (PDF portfolio):contentReference[oaicite:94]{index=94}

---

## ✅ Definition of Done

### For this runbook (docs quality)
- [x] YAML front-matter present (protocol-friendly):contentReference[oaicite:95]{index=95}:contentReference[oaicite:96]{index=96}
- [x] Directory layout + staging pattern documented:contentReference[oaicite:97]{index=97}
- [x] Required STAC/DCAT/PROV artifacts documented:contentReference[oaicite:98]{index=98}
- [x] Governance + sensitivity considerations stated:contentReference[oaicite:99]{index=99}
- [ ] Links validated against repo (CI will enforce):contentReference[oaicite:100]{index=100}
- [ ] Reviewed by domain steward + FAIR+CARE delegate

### For adding a new historical dataset (operational)
- [ ] Raw source placed under `data/raw/historical/...`:contentReference[oaicite:101]{index=101}
- [ ] Evidence manifest + checksums created
- [ ] Processed artifacts in `data/processed/historical/...`
- [ ] STAC/DCAT/PROV generated + schema-valid:contentReference[oaicite:102]{index=102}
- [ ] Sensitivity classification + CARE label set:contentReference[oaicite:103]{index=103}
- [ ] Graph references catalog IDs (no bulky duplication):contentReference[oaicite:104]{index=104}

---

## 🕰️ Version History
| Version | Date       | Summary |
|--------:|------------|---------|
| v0.1.0  | 2026-01-20 | Initial historical domain runbook (staging + metadata + governance + Story Nodes). |

---

<div align="center">

⬅️ [Back to Docs Data Index](../README.md) · 📘 [Master Guide](../../MASTER_GUIDE_v13.md) · 🛡️ [Governance](../../standards/governance/ROOT-GOVERNANCE.md) · 🪶 [Sovereignty](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

