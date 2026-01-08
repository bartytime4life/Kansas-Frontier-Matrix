<div align="center">

# 📥 `data/raw/` — Raw Data (Immutable Inputs)

![stage](https://img.shields.io/badge/data%20stage-raw-2563EB)
![policy](https://img.shields.io/badge/policy-append--only-16A34A)
![integrity](https://img.shields.io/badge/integrity-checksums%20%2B%20receipts-7C3AED)
![provenance](https://img.shields.io/badge/provenance-source.json%20%2B%20PROV-0EA5E9)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-8B5CF6)
![security](https://img.shields.io/badge/security-no%20secrets%20in%20git-DC2626)

**Raw data is KFM’s first trust boundary.**  
We ingest external sources here **as-received**, preserve them **immutably**, then perform deterministic ETL in `data/work/` and publish stable products in `data/processed/`. 🧾➡️🛠️➡️📦

</div>

> [!IMPORTANT]
> **If you changed bytes, it’s not raw anymore.**  
> Reprojection, cleanup, OCR, tiling, resampling, column edits, format conversion → belongs in `data/work/` or `data/processed/`.

---

## 🔗 Quick links

- 🧭 Repo overview → `../../README.md`
- 🧪 Intermediate artifacts → [`../work/`](../work/)
- 📦 Final products → [`../processed/`](../processed/)
- ✅ QA runbooks & validators → [`../qa/`](../qa/) *(create if missing)*
- 🗂️ Discovery metadata (DCAT) → [`../catalog/`](../catalog/)
- 🛰️ Geospatial indexing (STAC) → [`../stac/`](../stac/)
- 🧬 Lineage bundles (PROV) → [`../prov/`](../prov/)
- 🛡️ Vulnerability reporting → `../../SECURITY.md` *(or `../../.github/SECURITY.md`)*

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🧭 Where raw fits in the KFM pipeline](#pipeline)
- [✅ What belongs here](#allowed)
- [🚫 What does NOT belong here](#not-allowed)
- [⭐ Raw-stage non-negotiables](#non-negotiables)
- [🗂️ Directory layout](#layout)
- [🧾 Raw drop contract](#drop-contract)
- [📄 `source.json` template](#source-json)
- [🔑 Checksums](#checksums)
- [📦 Large files & restricted redistribution](#large-files)
- [🗺️ Geospatial + document specifics](#geo-specifics)
- [🔐 Security, privacy, sovereignty](#security)
- [🧪 QA & CI expectations](#qa)
- [🧰 Intake SOP: add a new raw drop](#sop)
- [🙃 Common anti-patterns](#anti-patterns)
- [📚 Project reference shelf](#reference-shelf)

</details>

---

<a id="pipeline"></a>

## 🧭 Where raw fits in the KFM pipeline

**Canonical ordering (non‑negotiable):**  
**Raw → Work/ETL → Processed → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

```mermaid
flowchart LR
  RAW[📥 Raw inputs<br/>data/raw/] --> WORK[🧪 Work / ETL<br/>data/work/]
  WORK --> PROC[📦 Processed outputs<br/>data/processed/]
  PROC --> STAC[🛰️ STAC catalogs<br/>data/stac/]
  PROC --> DCAT[🗂️ DCAT datasets<br/>data/catalog/dcat/]
  PROC --> PROV[🧬 PROV lineage<br/>data/prov/]
  STAC --> GRAPH[🕸️ Graph (Neo4j)]
  DCAT --> GRAPH
  PROV --> GRAPH
  GRAPH --> API[🔌 Governed API]
  API --> UI[🗺️ Web UI]
  UI --> STORY[🎬 Story Nodes]
  STORY --> FOCUS[🧠 Focus Mode]
```

> [!NOTE]
> Raw is not “less important.” It’s the foundation for **reproducibility**, **auditability**, and **tamper-evidence** across catalogs, models, and narratives.

---

<a id="allowed"></a>

## ✅ What belongs here

**Allowed raw inputs (as-received):**
- 📦 Vendor/agency deliveries (ZIP/TAR bundles, exports, archives)
- 🗺️ Original GIS deliveries (GeoTIFF, SHP, GPKG, CSV, JSON, KML, etc.)
- 🧾 Documents & scans (PDFs, TIFF/JPEG/PNG masters)
- 🛰️ Remote sensing exports / pulls where you can persist **the exported files** and/or **the original response payload**
- 🧪 Sensor dumps / logs (when permitted) — stored “as recorded”

**Also allowed (with strict rules):**
- 📁 **Lossless extraction** into `extracted/` **only if** you also keep the original archive in `original/`
  - unzip/untar is allowed; *editing content is not*

---

<a id="not-allowed"></a>

## 🚫 What does NOT belong here

**Not allowed in `data/raw/`:**
- 🧼 Cleaned tables, renamed columns, changed encodings
- 🧭 Reprojection, resampling, tiling, simplification, topology repair
- 🧊 “Make it a COG”, “make it Parquet”, “make it GeoJSON”
- 🧠 Analysis outputs / model outputs / simulation outputs / reports  
  → these are first-class datasets in `data/processed/` and must ship with STAC/DCAT/PROV

> [!WARNING]
> If the only explanation for a file is “trust me,” it will fail review (and often CI).

---

<a id="non-negotiables"></a>

## ⭐ Raw-stage non-negotiables

These rules keep the pipeline deterministic and governance-safe:

- 🧱 **Append-only**: never mutate an existing drop; new pull → new folder
- 🧊 **Bytes preserved**: keep originals + sidecars; don’t “helpfully convert”
- 🧾 **Receipts required**: every drop has `README.md`, `source.json`, `checksums.sha256`
- 🏷️ **Stable identity**: `dataset_id` + `drop_id` become PROV keys later
- 🛡️ **Governance up front**: license, classification, sensitivity declared at ingest time
- 🔐 **No secrets in Git**: use `.env` + secret stores; rotate if exposed

---

<a id="layout"></a>

## 🗂️ Directory layout

Organize raw data by **domain → dataset → immutable drop**:

```text
data/raw/
└── <domain>/                         # imagery, hydro, census, docs, etc.
    └── <dataset_slug>/               # kebab-case, stable (no dates inside)
        └── <drop_id>/                # YYYY-MM-DD | vX | YYYY-MM-DDa
            ├── 📄 README.md
            ├── 📄 source.json
            ├── 🔑 checksums.sha256
            ├── 📁 original/          # upstream bundle(s) exactly as received
            ├── 📁 extracted/         # optional: lossless unpack output (no transforms)
            └── 📁 notes/             # optional: landing pages, emails (NO secrets)
```

### 🏷️ Naming guidance

- `<domain>`: broad, stable bucket (don’t overfit)
- `<dataset_slug>`: stable handle (`kebab-case`)
- `<drop_id>`:
  - `YYYY-MM-DD` for dated pulls/deliveries
  - `vX` for upstream versioned releases
  - if re-pulling “the same” drop: `YYYY-MM-DDa`, `YYYY-MM-DDb` (never overwrite)

> [!TIP]
> “Boring naming” is a feature: it makes automation, QA, and provenance simpler.

---

<a id="drop-contract"></a>

## 🧾 Raw drop contract

Every raw drop is a **reviewable, machine-validatable boundary**.

| Artifact | Required | Why it exists | Minimum contents |
|---|---:|---|---|
| 📄 `README.md` | ✅ | Human context | what it is, where it came from, what’s inside, caveats |
| 📄 `source.json` | ✅ | Machine provenance | source URLs, license, retrieval time/method, classification, extents |
| 🔑 `checksums.sha256` | ✅ | Integrity + tamper evidence | sha256 of all files in the drop (except itself) |
| 📁 `original/` | ◻️ | “As received” archive(s) | ZIP/TAR/PDF bundles, vendor deliveries |
| 📁 `extracted/` | ◻️ | Lossless unpack only | unzip/untar output (no semantic changes) |

> [!CAUTION]
> If redistribution is restricted: keep **only receipts** (README + source.json) in Git, store bytes in restricted storage, and document access.

---

<a id="source-json"></a>

## 📄 `source.json` template

`source.json` is the raw-stage **receipt** 🧾 — it should let a reviewer (or future-you) re-acquire and re-verify the same inputs.

```json
{
  "dataset_id": "<domain>/<dataset_slug>",
  "domain": "<domain>",
  "dataset_slug": "<dataset_slug>",
  "drop_id": "<YYYY-MM-DD_or_vX>",

  "title": "Human-friendly dataset name",
  "description": "What this drop contains (1–3 sentences).",

  "upstream": {
    "publisher": "Agency / org / vendor",
    "source_urls": ["https://…"],
    "retrieved_from": "https://…",
    "license": "SPDX id or URL or text statement",
    "citation": "Preferred citation string (if provided)",
    "terms_notes": "Redistribution limits / constraints."
  },

  "retrieval": {
    "retrieved_at": "YYYY-MM-DDTHH:MM:SSZ",
    "method": "manual|script|api|mirror",
    "performed_by": "name_or_handle",
    "tooling": {
      "script_path": "tools/fetch/<something>.sh",
      "container": "docker image tag (if used)",
      "commit": "git commit hash (if applicable)"
    }
  },

  "coverage": {
    "spatial": {
      "crs": "EPSG:4326 | unknown",
      "bbox_wgs84": [-102.05, 36.99, -94.59, 40.00]
    },
    "temporal": {
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD"
    }
  },

  "sensitivity": {
    "classification": "public|internal|confidential|restricted",
    "care_label": "TBD",
    "notes": "Sovereignty, sensitive sites, PII risk, redaction expectations."
  },

  "files": [
    {
      "path": "original/source_bundle.zip",
      "media_type": "application/zip",
      "size_bytes": 0,
      "sha256": "<optional duplicate of checksums.sha256>"
    }
  ]
}
```

> [!TIP]
> Keep `README.md` **human**, keep `source.json` **machine**. Don’t hide licensing or sensitivity only in prose.

---

<a id="checksums"></a>

## 🔑 Checksums

### Generate (macOS/Linux)

```bash
# from inside the drop directory: .../<drop_id>/
find . -type f \
  ! -name 'checksums.sha256' \
  -print0 | sort -z | xargs -0 sha256sum > checksums.sha256
```

### Verify (macOS/Linux)

```bash
sha256sum -c checksums.sha256
```

### Windows (PowerShell)

```powershell
Get-ChildItem -Recurse -File |
  Where-Object { $_.Name -ne "checksums.sha256" } |
  ForEach-Object {
    $h = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
    "$h  $($_.FullName.Replace((Get-Location).Path + '\','').Replace('\','/'))"
  } | Set-Content checksums.sha256
```

> [!NOTE]
> Checksums are practical tamper-evidence **and** a fast way to debug data drift.

---

<a id="large-files"></a>

## 📦 Large files & restricted redistribution

Raw often includes huge rasters and long time-series.

### Recommended patterns

- 🧳 **Small/medium files**: store directly in Git (still include checksums)
- 🧱 **Large binaries**: consider DVC (or similar) for versioned pointers
- 🔒 **Redistribution restricted**: keep only receipts in Git; store bytes in restricted storage

> [!IMPORTANT]
> The **drop folder** is still the contract boundary even if the bytes live elsewhere.

---

<a id="geo-specifics"></a>

## 🗺️ Geospatial + document specifics

### 🛰️ Raster deliveries (GeoTIFF/IMG/etc.)
✅ Raw: keep “as delivered,” including `.aux.xml`, `.tfw`, metadata sidecars  
❌ Not raw: COG conversion, resampling, overviews, tiling (do this in `data/work/`)

### 🧭 Vector deliveries (SHP/GPKG/GeoJSON/CSV)
✅ Raw: keep as delivered, preserve encoding + schema  
❌ Not raw: reprojection, geometry fixes, attribute normalization

### 🧾 Documents & scans (PDF/JPEG/PNG/TIFF)
✅ Raw: keep original masters (don’t OCR in place)  
❌ Not raw: OCR text outputs, rotated/cleaned images, compressed previews  
➡️ Put OCR + derivatives in `data/work/` (publish in `data/processed/` if they ship)

### 🧊 3D / graphics assets (glTF / 3D Tiles / meshes)
Treat as **untrusted inputs**:
- store raw assets unchanged
- validate parsers and conversion steps in `data/work/`
- never execute embedded scripts/macros; strip or sandbox during ETL

### 🛰️ API pulls (remote sensing, web services)
If you pull via API:
- store the **raw payload** (or exported files) if possible
- store the **exact request parameters** (query, filters, time window)
- store the script path + commit hash in `source.json`

> [!TIP]
> “Reproducible retrieval” is part of provenance. If a pull can’t be repeated, document why (rate limits, paid access, ephemeral tokens, etc.).

---

<a id="security"></a>

## 🔐 Security, privacy, sovereignty

Geospatial raw data can carry real-world risk.

### Hard rules
- 🔐 **No secrets in Git**: tokens/keys go in `.env` + secret stores
- 🧍 **No PII in public repos** unless explicitly governed and approved
- 🧭 **No restricted coordinates** in public drops when locations are sensitive
- 🏷️ **Declare classification** in `source.json` (and don’t “downgrade” later)

### If in doubt
- open a PR with only the receipts (no binaries)
- flag the concern clearly
- route sensitive details via private channels per `SECURITY.md`

> [!WARNING]
> “Processed outputs can still leak.” Even aggregated or derived data can reveal sensitive patterns. Raw discipline is the first step; API governance is the last.

---

<a id="qa"></a>

## 🧪 QA & CI expectations

Raw changes should be easy to validate automatically.

**Minimum checks for PRs touching `data/raw/**`:**
- [ ] Drop is append-only (no edits to existing drops)
- [ ] `README.md`, `source.json`, `checksums.sha256` exist
- [ ] `checksums.sha256` verifies locally
- [ ] `source.json` includes license + classification
- [ ] No secrets/credentials committed
- [ ] Sensitive data is flagged and handled per governance

> [!NOTE]
> Deeper geospatial QA (CRS checks, geometry validity, bounds) usually happens in `data/work/` and `data/processed/`—but raw must still declare what it *claims* to be.

---

<a id="sop"></a>

## 🧰 Intake SOP: add a new raw drop

### 1) Create the drop boundary 🧱
- choose `<domain>/<dataset_slug>/<drop_id>/`
- never overwrite an existing drop

### 2) Acquire upstream bytes 📥
- place the upstream bundle in `original/`
- optional: losslessly extract into `extracted/`

### 3) Write the receipts 🧾
- `README.md` (human: what/where/why/caveats)
- `source.json` (machine: license, retrieval, classification, extents)

### 4) Lock integrity 🔒
- generate `checksums.sha256`
- verify it locally

### 5) Open a PR ✅
Include:
- what changed (new dataset vs new drop)
- any licensing/sensitivity concerns
- how to reproduce retrieval (if applicable)

---

<a id="anti-patterns"></a>

## 🙃 Common anti-patterns

- “I fixed the CSV in place” → new drop; do cleanup in `data/work/`
- “I reprojected it so it lines up” → `data/work/` / `data/processed/`
- “I renamed files for convenience” → keep originals; map names in docs
- “I added a token to a download script” → use `.env`; rotate exposed tokens
- “I posted sensitive coordinates in a public drop” → stop, remove, report privately

---

<a id="reference-shelf"></a>

## 📚 Project reference shelf

<details>
<summary><strong>📖 Reference library (all project files)</strong></summary>

> ⚠️ Reference PDFs may have licenses different from repository code. Keep them in `docs/library/` (or outside the repo) and respect upstream terms.

### 🧭 Core KFM system docs
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

### 🗺️ GIS, mapping, cartography, geospatial tooling
- making-maps-a-visual-guide-to-map-design-for-gis.pdf
- Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf  [oai_citation:1‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)
- python-geospatial-analysis-cookbook.pdf
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf

### 🛰️ Remote sensing workflows
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf

### 🖼️ Documents, scans & file formats
- compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf  [oai_citation:2‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

### 📊 Statistics, experiments, inference & modeling integrity
- Understanding Statistics & Experimental Design.pdf
- regression-analysis-with-python.pdf
- Regression analysis using Python - slides-linear-regression.pdf  [oai_citation:3‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)
- graphical-data-analysis-with-r.pdf
- think-bayes-bayesian-statistics-in-python.pdf  [oai_citation:4‡think-bayes-bayesian-statistics-in-python.pdf](file-service://file-LXwJApPMVhRZgyqLb9eg7c)
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf *(file name as provided)*

### ⚙️ Systems, scale, interoperability
- Scalable Data Management for Future Hardware.pdf
- Data Spaces.pdf
- concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf  [oai_citation:5‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6)

### 🌐 Web UI & 3D graphics
- responsive-web-design-with-html5-and-css3.pdf
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf

### 🧮 Advanced math & optimization (optional deep dives)
- Spectral Geometry of Graphs.pdf
- Generalized Topology Optimization for Structural Design.pdf

### ❤️ Ethics, autonomy, AI law
- Introduction to Digital Humanism.pdf
- Principles of Biological Autonomy - book_9780262381833.pdf
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf

### 🛡️ Security (defensive references)
- ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf  [oai_citation:6‡ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf](file-service://file-Q7EeqPb17SD9sV8Fb12LQX)
- Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf  [oai_citation:7‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)

### 🧰 General programming shelf (bundles)
- A programming Books.pdf
- B-C programming Books.pdf
- D-E programming Books.pdf
- F-H programming Books.pdf
- I-L programming Books.pdf
- M-N programming Books.pdf
- O-R programming Books.pdf
- S-T programming Books.pdf
- U-X programming Books.pdf

</details>

---

## ✅ Definition of Done (for this README)

- [x] “Raw means bytes preserved” rule is explicit
- [x] Append-only + checksums + receipts contract defined
- [x] Layout + naming guidance included
- [x] Security/privacy/sovereignty guardrails included
- [ ] Linked from `data/README.md` (recommended)
- [ ] Reviewed by maintainers / data stewards (recommended)

<p align="right"><a href="#pipeline">⬆️ Back to top</a></p>