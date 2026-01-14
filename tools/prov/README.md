# 🧾 `tools/prov` — Provenance & Evidence Tooling

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Provenance](https://img.shields.io/badge/provenance-first-2ea44f)
![Standards](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Reproducibility](https://img.shields.io/badge/reproducible-deterministic%20ETL-informational)

> **KFM promise:** *No “mystery layers.”*  
> Anything that appears in the UI, API, graph, Story Nodes, or Focus Mode must be traceable back to **cataloged sources** and **provable processing**. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

## 🎯 What this folder is for

`tools/prov/` contains the **provenance-first utilities** that make Kansas Frontier Matrix auditable end-to-end:

- ✅ **Generate** PROV lineage records for datasets, models, and derived artifacts  
- ✅ **Validate** that every published artifact has a complete metadata “contract” (source, license, spatial/temporal extent, processing steps, etc.)  
- ✅ **Link** STAC/DCAT metadata ↔ PROV lineage ↔ knowledge-graph nodes ↔ narrative citations  
- ✅ **Enforce** CI gates so unsourced artifacts never land in “official” catalogs  
- ✅ **Surface** provenance in UI/Focus Mode as citations and inspectable method traces :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

---

## 🧱 Non‑Negotiable Invariants (Hard Gates)

These are the guardrails that `tools/prov/` exists to **enforce**:

1. **Pipeline ordering is absolute**  
   ETL → Catalogs (**STAC/DCAT/PROV**) → Graph → API → UI → Story Nodes → Focus Mode :contentReference[oaicite:4]{index=4}

2. **Provenance-first**  
   Nothing gets graphed, served, or narrated unless it has **STAC/DCAT metadata + a PROV lineage record**. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

3. **Deterministic, idempotent ETL**  
   Same inputs ⇒ same outputs. Runs are logged with input/output hashes or stable IDs. :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}

4. **Evidence-first narrative**  
   Story Nodes / Focus Mode must not include unsourced claims; AI text must be labeled + provenance-linked. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}

---

## 🧭 Where provenance “lives” in the repo

KFM’s data lifecycle is intentionally structured so provenance is **first-class**:

```text
data/
├─ sources/       🧾 small manifests describing external sources (URL, license, schema hints)
├─ raw/           📥 exact fetched inputs kept for auditing and reprocessing
├─ processed/     🗄 curated outputs (COGs, GeoJSON/GeoParquet, Parquet, etc.)
└─ catalog/       🗂 STAC/DCAT metadata + provenance records (often PROV JSON-LD)
   └─ provenance/ 🔗 machine-readable lineage bundles (e.g., PROV-O JSON-LD)
```

- `data/catalog/` holds STAC/DCAT entries with fields like **spatial extent, temporal range, license, attribution**, and links to the processed assets.  
- `data/provenance/` (or similar) stores machine-readable lineage (often **JSON-LD using PROV-O**) describing which sources + steps produced which outputs. :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

---

## 🧩 Standards we align to (and extend)

KFM uses open standards as contracts between subsystems:

- **STAC** → geospatial assets (imagery/features) with spatial + temporal indexing  
- **DCAT** → dataset-level catalog discovery (title, description, license, keywords, distributions)  
- **PROV (PROV‑O)** → lineage: raw inputs → intermediate steps → processed outputs, plus responsible agents and configs :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

### 📌 KFM profiles
KFM extends base standards with project-specific fields (e.g., uncertainty indicators, provenance references, sovereignty flags). Profiles are expected to live under something like:

```text
docs/standards/
├─ KFM_STAC_PROFILE.md
├─ KFM_DCAT_PROFILE.md
└─ KFM_PROV_PROFILE.md
```

…and CI validates against those profiles. :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}

---

## 🏗️ Proposed `tools/prov/` layout

> This is the “shape” we target. Adjust filenames as tooling lands.

```text
tools/prov/
├─ README.md                       ✅ you are here
├─ schemas/                        🧬 JSON Schemas for KFM PROV/STAC/DCAT extensions
│  ├─ kfm_prov_profile.schema.json
│  └─ kfm_contract.schema.json
├─ cli/                            🖥️  developer-facing entrypoints
│  └─ prov.py
├─ core/                           🧱 provenance primitives (IDs, hashing, bundles)
│  ├─ ids.py
│  ├─ hashing.py
│  └─ bundle.py
├─ emit/                           🧾 emitters (PROV JSON-LD, STAC/DCAT cross-links)
│  ├─ emit_prov_jsonld.py
│  ├─ link_stac_dcat_prov.py
│  └─ emit_attribution_report.py
├─ validate/                       🧪 validators (schemas, hashes, link integrity)
│  ├─ validate_contracts.py
│  ├─ validate_prov.py
│  └─ validate_crosslinks.py
└─ examples/                       📦 minimal examples + golden files for CI tests
   ├─ prov_bundle_example.jsonld
   └─ dataset_contract_example.json
```

---

## ⚙️ What we capture (minimum viable provenance)

### 1) Stable identifiers 🆔
Provenance depends on IDs that *don’t change* when names/labels evolve.

- Use stable, information-free IDs for:
  - datasets
  - assets (files)
  - pipeline runs (activities)
  - agents (people/software/services)
  - model artifacts & evaluation reports

This aligns with long-haul flexible design principles: stable identifiers reduce downstream brittleness. :contentReference[oaicite:17]{index=17}

### 2) Hashes for integrity 🔐
Every artifact referenced in provenance should carry a content hash (e.g., SHA‑256) so we can:
- detect tampering
- guarantee reproducibility
- confirm that citations point to the exact bytes referenced

### 3) The “data contract” requirement 📜
Every dataset must have a contract (metadata JSON) with at least:
- `source` (publisher + link)
- `license`
- spatial/temporal extent
- processing steps
- distributions / asset links
- provenance pointer(s)

KFM explicitly uses contract-first + provenance-first enforcement via validators and CI checks. :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19}

---

## 🧠 PROV mental model (KFM-friendly)

Think in **three nouns**:

- **Entity** = a thing (raw CSV, COG GeoTIFF, GeoParquet table, model weights, story node markdown)  
- **Activity** = a step (ETL run, georeference job, NDVI pipeline, regression fit, simulation run)  
- **Agent** = who/what did it (person, script, CI runner, container image)

Then connect them with:

- `Entity wasGeneratedBy Activity`
- `Activity used Entity`
- `Activity wasAssociatedWith Agent`

> This is what powers “click for sources” UX: the UI can always pull the contract + PROV bundle and display citations + method trace. :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}

---

## 🧪 Workflows

### ✅ A) Adding a new dataset (ETL → Catalogs → Provenance)

**Checklist** (what CI should enforce):

1. **Add source manifest** in `data/sources/`  
   - URL, license, expected schema hints (no bulky raw data in Git) :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}

2. **Run pipeline** to populate `data/raw/` and emit curated outputs to `data/processed/`  
   - keep exact raw files for auditing and reprocessing :contentReference[oaicite:24]{index=24} :contentReference[oaicite:25]{index=25}

3. **Generate metadata bundle**
   - STAC Item/Collection
   - DCAT dataset entry
   - PROV activity bundle with full lineage raw → intermediate → processed :contentReference[oaicite:26]{index=26}

4. **Validate**
   - schemas pass
   - links resolve
   - hashes match
   - required fields present (license, extents, attribution)

5. **Only then** allow graph ingestion / API exposure / UI use :contentReference[oaicite:27]{index=27}

---

### ✅ B) Capturing provenance for analyses & models (stats/ML/simulation)

KFM is not just “maps”—it’s a modeling platform. Provenance must cover:

- data splits & sampling strategy
- model hyperparameters
- random seeds
- metrics + evaluation datasets
- code version / commit SHA
- compute environment (container image, OS, library versions)

Why: without this, “modelable for everyone” becomes “unreproducible for most.” :contentReference[oaicite:28]{index=28}

Helpful reference pillars (project library):
- Python scientific stack conventions (environment + reproducible workflows) :contentReference[oaicite:29]{index=29}  
- ML theory + evaluation discipline :contentReference[oaicite:30]{index=30}  
- Regression workflows (for interpretable modeling) :contentReference[oaicite:31]{index=31}  

---

### ✅ C) Story Nodes & Focus Mode (evidence-first narrative)

Story Nodes are treated as **data sources** with governance metadata and citations. Documentation should be versioned, reviewed, and provenance-checked—just like code. :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33}

**Rules:**
- every factual claim has citations (preferably to cataloged datasets / graph IDs)
- fact vs interpretation must be distinguishable
- AI-generated text is opt-in, labeled, and provenance-linked
- sensitive locations must not leak through narrative/UI side-channels :contentReference[oaicite:34]{index=34} :contentReference[oaicite:35]{index=35}

---

## 🧰 CLI expectations (example interface)

> Commands below are illustrative. Implementers: feel free to align to `make` targets and CI jobs.

```bash
# 1) Build a PROV bundle for a pipeline run
python -m tools.prov.cli.prov emit \
  --run-id "urn:kfm:run:2026-01-14T12:00:00Z:ndvi:001" \
  --inputs data/raw/landsat/*.tif \
  --outputs data/processed/ndvi/ndvi_county_2020.parquet \
  --agent "urn:kfm:agent:ci:github-actions" \
  --config pipelines/remote_sensing/ndvi.yaml \
  --out data/catalog/provenance/ndvi_county_2020.prov.jsonld

# 2) Validate all catalogs + provenance
python -m tools.prov.cli.prov validate --all

# 3) Emit an attribution report for a Story Node / UI view
python -m tools.prov.cli.prov attribution \
  --story docs/reports/story_nodes/fort_riley.md \
  --out docs/reports/attributions/fort_riley_sources.md
```

---

## 🧬 Example PROV JSON‑LD (tiny, readable)

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "urn:kfm:entity:data:raw:usda:crops:2020_county_yields.csv": {
      "prov:label": "USDA crop yields (raw, 2020)",
      "kfm:sha256": "…",
      "kfm:license": "…",
      "kfm:source_url": "…"
    },
    "urn:kfm:entity:data:processed:crops:yields_by_county.parquet": {
      "prov:label": "Crop yields by county (processed)",
      "kfm:sha256": "…"
    }
  },
  "activity": {
    "urn:kfm:activity:pipeline:usda_crops_clean:v1": {
      "prov:used": ["urn:kfm:entity:data:raw:usda:crops:2020_county_yields.csv"],
      "prov:generated": ["urn:kfm:entity:data:processed:crops:yields_by_county.parquet"],
      "prov:startedAtTime": "2026-01-14T12:00:00Z",
      "prov:endedAtTime": "2026-01-14T12:03:12Z",
      "kfm:config_ref": "pipelines/agriculture/usda_crops_clean.yaml"
    }
  },
  "agent": {
    "urn:kfm:agent:ci:github-actions": {
      "prov:type": "prov:SoftwareAgent",
      "prov:label": "GitHub Actions Runner"
    }
  }
}
```

---

## 📈 Performance & scale notes (why this matters)

As KFM grows (sensor streams, large rasters, many derived products), provenance must remain:

- **Queryable** (fast lookup by dataset ID / story node / region / time)
- **Compact** (store pointers + hashes, not bulky payloads)
- **Indexable** (stable IDs, predictable shapes)

Design considerations are informed by the project’s database scalability references. :contentReference[oaicite:36]{index=36} :contentReference[oaicite:37]{index=37}

---

## 🛡️ Ethics, transparency, and trust

KFM explicitly prioritizes transparency and accountability; provenance is how we operationalize that value in software. :contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39}

**Key safeguards tied to provenance tooling:**
- **AI is advisory, evidence-backed, and citation-driven** (no autonomous decisions) :contentReference[oaicite:40]{index=40}
- **Sensitive data controls** should be enforced at the API/metadata layer, not bypassed by UI shortcuts :contentReference[oaicite:41]{index=41}
- **Governed docs** should use front-matter + consistent citation patterns so machines can validate provenance completeness :contentReference[oaicite:42]{index=42}

---

## 🗺️ Special data types we must handle well

### 🧊 3D / archaeology / volumetric assets
KFM may host or reference 3D GIS and volumetric datasets (3D models, CT volumes, stratigraphy layers). Provenance must capture:
- acquisition method (scanner/photogrammetry)
- coordinate reference / georeferencing steps
- reconstruction software + parameters
- derived layers/segments and their lineage :contentReference[oaicite:43]{index=43}

### 🛰️ Remote sensing pipelines
Remote sensing derivatives (NDVI, land cover, change detection) must capture:
- source scene IDs
- cloud mask method
- reproject/resample parameters
- compositing windows and thresholds :contentReference[oaicite:44]{index=44}

---

## 🧩 Integration points (catalogs ↔ graph ↔ UI)

Provenance linkage is only useful if it’s connected:

- **STAC Items** point to processed assets and carry attribution + license  
- **DCAT** provides discovery and distributions to STAC or direct downloads  
- **PROV** links raw → intermediate → processed outputs with run/config IDs  
- **Graph nodes** store **references** to catalogs (don’t duplicate payloads) :contentReference[oaicite:45]{index=45}

---

## ✅ Contribution “Definition of Done” for provenance

Before a PR is mergeable:

- [ ] Source manifest exists (`data/sources/**`)  
- [ ] Raw inputs are reproducible (fetchable + hashed)  
- [ ] Processed outputs are deterministic and stored under `data/processed/**`  
- [ ] STAC + DCAT + PROV records exist and cross-link correctly  
- [ ] Licenses + attribution are present  
- [ ] Validators pass locally and in CI  
- [ ] If narrative content exists: every claim has evidence + citations  
- [ ] If AI text exists: labeled + linked to evidence + confidence metadata :contentReference[oaicite:46]{index=46} :contentReference[oaicite:47]{index=47}

---

## 📚 Project sources this README is built on

### Core KFM provenance & architecture
- Kansas Frontier Matrix — Comprehensive Technical Documentation :contentReference[oaicite:48]{index=48}  
- MARKDOWN_GUIDE v13 — pipeline invariants, governance gates, evidence-first narrative :contentReference[oaicite:49]{index=49} :contentReference[oaicite:50]{index=50}  
- Documentation governance patterns (front-matter + provenance discipline) :contentReference[oaicite:51]{index=51}  

### System + data engineering references
- Database Performance at Scale (querying, scaling patterns) :contentReference[oaicite:52]{index=52}  
- Scalable Data Management for Future Hardware (stream/event + heterogeneous processing perspective) :contentReference[oaicite:53]{index=53}  

### Science, modeling, ML + “why provenance matters”
- Understanding Machine Learning: From Theory to Algorithms :contentReference[oaicite:54]{index=54}  
- SciPy Lecture Notes (Python scientific workflows) :contentReference[oaicite:55]{index=55}  
- Introduction to Digital Humanism (trust, transparency, accountability framing) :contentReference[oaicite:56]{index=56}  

### GIS & domain expansion
- Archaeological 3D GIS (3D assets + interpretation workflows) :contentReference[oaicite:57]{index=57}  

### Flexibility & long-term maintainability
- Flexible Software Design (stable identifiers, design for change) :contentReference[oaicite:58]{index=58}  

### Multi-language tooling reality (we may ingest outputs from)
- Objective‑C Notes for Professionals (mobile client tooling contexts) :contentReference[oaicite:59]{index=59}  
- Implementing Programming Languages (DSL/tooling architecture thinking) :contentReference[oaicite:60]{index=60}  
- MATLAB Notes for Professionals (scientific scripting ecosystems) :contentReference[oaicite:61]{index=61}  
- Bash Notes for Professionals / Linear algebra foundations for ML pipelines :contentReference[oaicite:62]{index=62}  

---

## 🗃️ Full project file library (staged references)

<details>
<summary><strong>📦 Click to expand the current project library list</strong></summary>

- A programming Books.pdf  
- Archaeological 3D GIS_26_01_12_17_53_09.pdf  
- B-C programming Books.pdf  
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf  
- D-E programming Books.pdf  
- Data Spaces.pdf  
- Database Performance at Scale.pdf  
- Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf  
- F-H programming Books.pdf  
- Generalized Topology Optimization for Structural Design.pdf  
- Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf  
- I-L programming Books.pdf  
- Introduction to Digital Humanism.pdf  
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
- M-N programming Books.pdf  
- Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf  
- O-R programming Books.pdf  
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf  
- Principles of Biological Autonomy - book_9780262381833.pdf  
- Regression analysis using Python - slides-linear-regression.pdf  
- S-T programming Books.pdf  
- Scalable Data Management for Future Hardware.pdf  
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf  
- Spectral Geometry of Graphs.pdf  
- U-X programming Books.pdf  
- Understanding Statistics & Experimental Design.pdf  
- compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf  
- concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf  
- ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf  
- graphical-data-analysis-with-r.pdf  
- making-maps-a-visual-guide-to-map-design-for-gis.pdf  
- python-geospatial-analysis-cookbook.pdf  
- regression-analysis-with-python.pdf  
- responsive-web-design-with-html5-and-css3.pdf  
- think-bayes-bayesian-statistics-in-python.pdf  
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  

</details>

---

## 🗺️ Mermaid map of the “no skipping steps” rule

```mermaid
flowchart LR
  A[ETL / Pipelines] --> B[Catalogs<br/>(STAC + DCAT + PROV)]
  B --> C[Knowledge Graph]
  C --> D[API Layer]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
  B -. provenance gate .-> C
  B -. evidence gate .-> F
```

---

## 🧾 Next steps (implementation roadmap)

- [ ] Define `KFM_PROV_PROFILE` schema + JSON-LD context conventions  
- [ ] Implement `emit_prov_jsonld.py` with deterministic hashing + stable IDs  
- [ ] Implement cross-link validator (STAC ↔ DCAT ↔ PROV ↔ graph refs)  
- [ ] Add CI job: fail PR if any cataloged dataset lacks license/extents/prov  
- [ ] Add “attribution report” generator for Story Nodes + Focus Mode evidence panels  

---

> If you’re reading this because a pipeline output exists but provenance doesn’t: **that output is not publishable** (yet). Fix provenance first. ✅

