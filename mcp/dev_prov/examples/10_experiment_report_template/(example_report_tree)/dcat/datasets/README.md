<!-- According to a document from 2026-01-22: this template follows the KFM “STAC + DCAT + PROV” evidence-first, catalog-driven approach. -->

# 🗃️ DCAT Datasets — Experiment Report Template

`🧪 TEMPLATE` `📦 dcat:Dataset` `🔗 STAC + PROV` `✅ CI / Policy Gates` `🧭 KFM-aligned`

This folder is the **dataset-level discovery layer** for an experiment report.  
If your experiment **uses**, **produces**, or **cites** a dataset, it should have a **DCAT dataset entry** here.

**What you get (when you do this right):**
- 🔎 **Discoverability** (search + filters + external harvesters)
- 🧾 **Attribution & licensing** (UI “Source: …” + exports)
- ⛓️ **Traceability** (every dataset links to STAC + PROV)
- 🤖 **Explainable AI** (Focus Mode citations, no-source = no-answer)

---

## 📁 Folder Contract

```text
dcat/
  datasets/
    README.md
    dataset--<dataset_id>.jsonld          # ✅ preferred (JSON-LD)
    dataset--<dataset_id>.ttl             # optional (Turtle)
  catalog.jsonld                          # optional roll-up catalog
```

> ✅ Rule of thumb: If it can show up in the UI, in search, in a report, or in Focus Mode as something you can cite… it should have a DCAT entry.

---

## 🧠 Core Concepts

### Dataset vs Distribution
- **Dataset** = the “what”  
  Human-facing description + governance + scope (spatial/temporal/theme).
- **Distribution** = the “how to access it”  
  Download file, tile endpoint, API query, STAC collection, OCI artifact, offline pack, etc.

### Why DCAT lives next to STAC & PROV
This template assumes a **3-layer evidence spine**:

- **STAC** → geospatial asset indexing (spatial/temporal + asset pointers)  
- **DCAT** → dataset catalog (discovery + license + publisher + keywords)  
- **PROV** → lineage (inputs → activities → outputs, plus agents/run IDs)

That triad is the “no mystery layers” rule: every dataset is **findable** and **auditable**.

---

## 🏷️ Naming & IDs

### ✅ Canonical Dataset ID (stable + versioned)
Use a stable ID (example pattern):

- `kfm.ks.landcover.2000_2020.v1`

**Recommended filename:**
- `dataset--kfm.ks.landcover.2000_2020.v1.jsonld`

> 🔁 If the meaning changes, bump the version (`v2`) and create a new dataset file.  
> ✅ IDs should be immutable; history lives in versioning + provenance.

### 🧾 Required Local Extensions
At minimum, datasets should carry:

- `kfm:dataset_id` (canonical ID)
- `kfm:classification` (`public` | `internal` | `restricted` | …)

You can extend further (sovereignty/sensitivity, uncertainty flags, etc.) via your project DCAT profile.

---

## ✅ Minimum Required Fields (Checklist)

- [ ] `@id` (stable URI/URN for the dataset)
- [ ] `@type: dcat:Dataset`
- [ ] `kfm:dataset_id`
- [ ] `dct:title`
- [ ] `dct:description`
- [ ] `dct:publisher`
- [ ] `dct:license`
- [ ] `dcat:keyword` (≥ 3 recommended)
- [ ] `dct:spatial` (bbox/region)
- [ ] `dct:temporal` (start/end)
- [ ] `kfm:classification`
- [ ] `dcat:distribution` (**must include STAC + PROV at minimum**)

---

## 🔗 Cross-Linking Rules (STAC + PROV)

### Required distributions
Every dataset should include distributions for:

1) **STAC Collection** (and/or key STAC Item(s))  
2) **PROV bundle** (JSON-LD)

Optionally include:
- processed file downloads (GeoParquet/COG/CSV/etc.)
- tile endpoints (vector/raster)
- API endpoints for queryable tables
- OCI artifact references (oras + cosign)
- offline packs (PMTiles, packaged COG sets, etc.)
- model cards / scenario docs for simulations

---

## 🧩 Template: Minimal JSON-LD Dataset

<details>
<summary>📄 Click to expand: dataset JSON-LD skeleton (copy/paste)</summary>

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "urn:kfm:terms:"
  },
  "@id": "urn:kfm:dataset:kfm.ks.landcover.2000_2020.v1",
  "@type": "dcat:Dataset",

  "kfm:dataset_id": "kfm.ks.landcover.2000_2020.v1",
  "kfm:classification": "public",

  "dct:title": "Kansas Landcover 2000–2020",
  "dct:description": "Landcover classifications for Kansas from 2000 through 2020, published as annual rasters and derived summaries.",
  "dct:publisher": { "@id": "urn:kfm:org:kansas-gis" },
  "dct:license": { "@id": "urn:license:CC-BY-4.0" },

  "dcat:keyword": ["kansas", "landcover", "remote sensing", "raster"],

  "dct:spatial": {
    "@type": "dct:Location",
    "dcat:bbox": "POLYGON((...))"
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2000-01-01",
    "dcat:endDate": "2020-12-31"
  },

  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC collection",
      "dcat:mediaType": "application/json",
      "dcat:accessURL": "../../stac/collections/kfm.ks.landcover.2000_2020.v1.json"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "PROV lineage bundle (JSON-LD)",
      "dcat:mediaType": "application/ld+json",
      "dcat:accessURL": "../../prov/kfm.ks.landcover.2000_2020.v1.prov.jsonld"
    }
  ]
}
```

</details>

---

## 🧠 Themes, Ontology & Concept Nodes

To make datasets searchable and narratable, tag them consistently.

**Recommended pattern**
- Use `dcat:theme` to point to stable concept IDs (concept nodes / controlled vocabulary).
- Keep `dcat:keyword` for human-friendly search phrases.

Example snippet:

```json
{
  "dcat:theme": [
    { "@id": "urn:kfm:concept:landcover" },
    { "@id": "urn:kfm:concept:remote_sensing" }
  ],
  "dcat:keyword": ["landcover", "classification", "satellite imagery"]
}
```

> 🧩 This keeps “themes” machine-stable (good for graph + AI) while keywords stay flexible (good for UX).

---

## 🧬 Reproducibility Hooks (dev_prov-friendly)

Even though lineage “lives” in PROV, it’s useful to leave breadcrumbs in DCAT for quick inspection:

- pipeline run ID
- commit hash
- PR/review reference
- scenario/model card reference (for simulations)

Example add-on:

```json
{
  "dct:provenance": {
    "@id": "urn:kfm:prov:bundle:kfm.ks.landcover.2000_2020.v1"
  },
  "prov:wasGeneratedBy": {
    "@id": "urn:kfm:prov:activity:run_2026_01_22T1200Z"
  }
}
```

---

## 📦 Distribution Patterns (Pick what fits)

### 1) File download (static artifact)
Use when you have a stable file (GeoParquet, CSV, COG, etc.).

```json
{
  "@type": "dcat:Distribution",
  "dct:title": "Processed GeoParquet (authoritative)",
  "dcat:mediaType": "application/x-parquet",
  "dcat:downloadURL": "../../artifacts/processed/kfm.ks.landcover.2000_2020.v1.geoparquet"
}
```

### 2) API access (queryable / real-time)
Use for tables served through an API (PostGIS-backed, timeseries, etc.).

```json
{
  "@type": "dcat:Distribution",
  "dct:title": "API query endpoint (GeoJSON)",
  "dcat:mediaType": "application/geo+json",
  "dcat:accessURL": "/api/v1/query?table=geo_counties"
}
```

> ⚠️ “Live” sources are still **cataloged** here; the runtime query is separate, but identity/licensing/classification still come from DCAT.

### 3) Tiles / map delivery
Use for web-friendly serving (vector tiles, raster tiles, etc.).

```json
{
  "@type": "dcat:Distribution",
  "dct:title": "Vector tiles (XYZ)",
  "dcat:mediaType": "application/x-protobuf",
  "dcat:accessURL": "/tiles/kfm.ks.landcover/{z}/{x}/{y}.pbf"
}
```

### 4) Offline packs (field mode)
Use for field-ready bundles (PMTiles, packaged rasters, etc.).

```json
{
  "@type": "dcat:Distribution",
  "dct:title": "Offline PMTiles pack",
  "dcat:mediaType": "application/vnd.pmtiles",
  "dcat:downloadURL": "../../offline/packs/kfm.ks.landcover.2000_2020.v1.pmtiles"
}
```

### 5) OCI artifacts (reproducible, signed)
Use when the dataset is published as an OCI artifact (oras) and signed (cosign).

```json
{
  "@type": "dcat:Distribution",
  "dct:title": "OCI artifact (oras)",
  "dcat:mediaType": "application/vnd.oci.image.manifest.v1+json",
  "dcat:accessURL": "oci://registry.example/kfm/landcover:2000_2020-v1"
}
```

---

## ⏱ Rapid Data, Simulations & Scenario Outputs

If your experiment outputs scenarios (future projections, “what-if” runs, digital-twin slices):

- treat each scenario output as a **Dataset**
- include a distribution for the **model card / scenario notes**
- include PROV details (inputs, parameters, run IDs)

**UI hint:** scenario compare becomes easier when each scenario is a separately cataloged dataset.

---

## 🛡️ Sensitivity, Sovereignty & Ethics

If a dataset has restrictions (private land monitors, culturally sensitive locations, etc.):

- set `kfm:classification` appropriately
- add explicit access notes (policy tags / redaction expectations)
- ensure derived distributions do not leak sensitive coordinates
- prefer generalized/blurred spatial coverage in public-facing metadata when needed

> 🔒 Principle: **no bypassing catalogs + provenance required** applies to sensitive and real-time layers too.

---

## 🤖 AI + UI Expectations

Your DCAT record is used by:

- 🗺️ UI legend & layer info (“Source: …” pulled from metadata)
- 🔎 dataset discovery & faceted search (keywords/themes/spatiotemporal)
- 🧭 Focus Mode citations (no-source = no-answer)
- 🧬 knowledge graph ingestion (Dataset nodes come from DCAT)

So keep:
- titles human-readable
- descriptions crisp but complete
- keywords consistent
- licenses explicit
- classification accurate (drives redaction + display rules)

---

## ✅ Validation & CI Gates (Metadata-as-Code)

Before merging:
- run schema validation (JSON Schema / SHACL)
- run policy checks (license present, classification present, provenance linked)
- ensure STAC + PROV paths resolve
- fail closed (no “best effort” publishing)

Suggested local workflow:
```bash
# Example commands — wire these to your repo tooling
make validate-dcat
make validate-stac
make validate-prov
make policy-check
```

---

## 🧾 PR Reviewer Checklist

- [ ] DCAT file added/updated under `dcat/datasets/`
- [ ] `kfm:dataset_id` matches filename and STAC/PROV IDs
- [ ] `dct:license` is present and correct
- [ ] `kfm:classification` is present and correct
- [ ] `dcat:distribution` includes STAC + PROV links
- [ ] If AI assisted, it is labeled + provenance is captured
- [ ] If sensitive, redaction rules are documented and tested

---

## 🧵 Bonus Pattern: “Narratives & Answers are Datasets Too”
If your experiment report produces:
- an analysis narrative
- an AI-generated answer bundle
- a story node / pulse thread / derived interpretation

…treat it as a **dataset**, publish it here, and link the supporting evidence via PROV.

That keeps “report artifacts” citeable and auditable just like “data artifacts”.

---

## 📚 Project Docs This README Aligns With (KFM Bundle)

- `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`
- `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`
- `Additional Project Ideas.pdf`
- `AI Concepts & more.pdf` (PDF portfolio)
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (PDF portfolio)
- `Various programming langurages & resources 1.pdf` (PDF portfolio)
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (PDF portfolio)
