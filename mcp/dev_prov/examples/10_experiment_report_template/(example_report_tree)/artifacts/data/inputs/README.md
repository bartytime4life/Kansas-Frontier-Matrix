# 📥 Experiment Inputs (Immutable Evidence)

![inputs](https://img.shields.io/badge/artifacts-inputs-0b7285)
![reproducible](https://img.shields.io/badge/reproducibility-required-2f9e44)
![prov](https://img.shields.io/badge/provenance-PROV--O-1c7ed6)
![stac](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT-7950f2)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-f76707)

This folder is the **input trust boundary** for an experiment report.

✅ Put **every byte (or immutable reference)** that influences results here: datasets, documents, prompts, configs, model weights, API snapshots, etc.

🚫 Don’t put derived outputs here (plots, tables, processed data). Those belong in `../outputs/`.

---

## 🧭 Golden Rules

1. **If it affects the result, it belongs here.**
2. **Treat inputs as read-only evidence.** Never edit an input file “in place.” If you must change it, create a new versioned copy and update manifests.
3. **No black boxes:** every input must be explainable via metadata (source, license, timestamps, checksums, and—when relevant—STAC/DCAT/PROV).
4. **Prefer deterministic & config-driven workflows:** the same inputs + same config should reproduce the same outputs.

---

## 🗂️ Recommended Layout

```text
artifacts/
  data/
    inputs/   📥 (you are here)
    outputs/  📤 derived files (figures, metrics, model outputs)
    work/     🧪 scratch space (optional, not “official”)
```

Inside `inputs/`, keep things tidy:

```text
inputs/
  manifest/                 # ✅ what was used, where it came from, why it’s allowed
    input_manifest.yaml
    run_manifest.json
  checksums/                # ✅ integrity
    sha256sum.txt
  datasets/                  # raw snapshots OR pointers + receipts
  docs/                      # papers, PDFs, scans, OCR inputs
  configs/                   # yaml/json/toml configs, parameters, seeds
  prompts/                   # system/user prompts or templates used
  models/                    # model weights used as input (if any)
  receipts/                  # API responses, headers, query text, export receipts
```

> Tip: if you’re unsure where something goes, drop it in the closest bucket and **record it in the manifest**.

---

## ✅ Minimum Required Files (Per Experiment)

### 1) `manifest/input_manifest.yaml`
A human-friendly inventory of everything in this folder.

**Must include** for each input item:
- `id` (stable)
- `type` (dataset | document | api_snapshot | config | model | prompt | other)
- `description`
- `source` (URL / archive / system-of-record / person)
- `retrieved_at` (ISO 8601) and/or `version`
- `license` (or usage terms)
- `classification` (public | internal | restricted)
- `path` (relative path in this folder)
- `sha256`

<details>
<summary>📄 Example <code>input_manifest.yaml</code></summary>

```yaml
schema_version: 1
experiment_id: EXP-000
run_id: RUN-00000000
created_at: 2026-01-22T00:00:00Z

inputs:
  - id: inp_usgs_nwis_06887500_iv_20260122T000512Z
    type: api_snapshot
    description: "USGS NWIS instantaneous values for Kansas River at Topeka (gage height)."
    source:
      uri: "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=06887500&parameterCd=00065"
      retrieved_at: "2026-01-22T00:05:12Z"
      method: GET
    license: "Public Domain (verify)"
    classification: public
    path: receipts/usgs_nwis_06887500_20260122T000512Z.json
    sha256: "<sha256>"

  - id: cfg_model_run_params
    type: config
    description: "All parameters for the run (including seeds)."
    source: { uri: "repo://configs/run.yaml" }
    license: "Project"
    classification: public
    path: configs/run.yaml
    sha256: "<sha256>"
```
</details>

### 2) `checksums/sha256sum.txt`
A flat list of `sha256` checksums for **every** file under `inputs/`.

```bash
# from inputs/
find . -type f -not -path './checksums/*' -print0 | sort -z | xargs -0 sha256sum > checksums/sha256sum.txt
```

### 3) (When applicable) STAC/DCAT/PROV sidecars
If an input is a **dataset** (especially geospatial), include:

- `*.stac.json` (STAC Item/Collection)
- `*.dcat.json` (DCAT dataset entry)
- `*.prov.jsonld` (PROV lineage)

Put these under `manifest/` (or alongside the dataset file) and reference them from `input_manifest.yaml`.

---

## 🌍 Handling Geospatial Inputs (KFM-style)

When inputs are spatial/temporal, strongly prefer:
- **COG** (`.tif`) for rasters
- **GeoParquet / GeoPackage / GeoJSON** for vectors
- **PMTiles / MBTiles** for tile archives

Also capture:
- CRS / EPSG
- bounding box + time range
- any reprojection/warping parameters (as config)

> If your experiment consumes a *map layer*, your inputs should be enough to regenerate the published layer metadata and provenance later.

---

## 🧠 Handling AI / ML Inputs

If this experiment uses AI components, treat these as first-class inputs:
- training/eval datasets (or immutable pointers)
- **model weights** (exact artifact digest)
- prompts/templates
- random seeds
- evaluation metric definitions

Optional-but-awesome:
- `model_card.md`
- dataset “datasheet” / data dictionary

---

## ⏱️ Handling Real-Time / API / Query-Based Inputs

Dynamic sources must be **snapshotted**.

Recommended approach:
- store the raw response in `receipts/`
- store request details (URL, params, headers) either inside the receipt or as a `*.request.json`
- record the timestamped snapshot in `input_manifest.yaml`

> KFM-style rule of thumb: if it’s computed “live,” **log it like an input dataset** with a timestamp.

---

## 🔐 Sensitive Data (FAIR + CARE)

If an input includes sensitive information (PII, sensitive locations, restricted licenses):

- **Do not commit the raw sensitive bytes** into public repos.
- Instead, store:
  - a redacted/aggregated derivative (allowed for this repo)
  - and a manifest entry pointing to the secure system-of-record
  - plus a note describing the redaction method

Common mitigation patterns:
- spatial generalization (fuzzing/coarsening coordinates)
- aggregation (time/space binning)
- suppression of identifiers

---

## 📦 Large Inputs (Too Big for Git)

If a file is too large for normal Git:

✅ Preferred options:
- **DVC / Git LFS**
- **OCI registry artifacts** (store data like container images; reference by immutable digest)

In all cases:
- keep a small manifest here
- include hashes/digests
- include license + access rules

---

## 🧪 Definition of Done ✅ (Copy/Paste Checklist)

- [ ] Every input file is listed in `manifest/input_manifest.yaml`
- [ ] `checksums/sha256sum.txt` covers **all** files (and matches)
- [ ] Licenses/terms are recorded for every external source
- [ ] Sensitive data is either redacted or referenced (not leaked)
- [ ] Any API/streaming input has an immutable snapshot + timestamp
- [ ] Any geospatial dataset has STAC/DCAT/PROV (when applicable)
- [ ] Any ML run has configs + seeds + model artifact digests

---

## 🔎 Quick “What goes where?”

| If you have… | Put it in… | Why |
|---|---|---|
| Raw CSV/GeoTIFF/PMTiles used in run | `datasets/` | immutable evidence |
| A PDF / scan / OCR source | `docs/` | traceable document input |
| Parameter files / seeds | `configs/` | reproducibility |
| Prompt templates | `prompts/` | AI traceability |
| API response JSON | `receipts/` | replayable snapshot |
| STAC/DCAT/PROV JSON | `manifest/` | discoverability + lineage |
| Checksums | `checksums/` | integrity |

---

## 📚 Reference Shelf (Project Docs)

If you’re unsure about rules, these project docs are the “north star”:

- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
- `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`
- (Libraries) `AI Concepts & more.pdf`, `Maps-…-webgl.pdf`, `Data Managment-…Ideas.pdf`, `Various programming langurages & resources 1.pdf`

---

### 🧩 Why this matters

KFM’s promise is that users can always trace “the map behind the map.” Keeping inputs clean and provable is how we earn that trust. 🧠🗺️✨

---

## 🧾 Run Manifest (Strongly Recommended)

Create `manifest/run_manifest.json` to capture a **machine-readable ledger** of the run:

- `run_id`, timestamps
- git commit / branch
- tool + dependency versions
- input IDs + hashes
- output paths (in `../outputs/`)
- an optional `canonical_digest` (self-fingerprint) to make the manifest content-addressable

<details>
<summary>🧩 Example <code>run_manifest.json</code></summary>

```json
{
  "schema_version": 1,
  "experiment_id": "EXP-000",
  "run_id": "RUN-00000000",
  "run_time_utc": "2026-01-22T00:00:00Z",
  "git": { "repo": "repo://", "commit": "<sha>", "dirty": false },
  "environment": {
    "container_image": "ghcr.io/org/project@sha256:<digest>",
    "python": "3.11.7",
    "tools": { "gdal": "<ver>", "tippecanoe": "<ver>", "node": "<ver>" }
  },
  "inputs": [
    { "id": "inp_usgs_nwis_06887500_iv_20260122T000512Z", "sha256": "<sha256>" },
    { "id": "cfg_model_run_params", "sha256": "<sha256>" }
  ],
  "outputs": [
    { "path": "../outputs/figures/figure_01.png" },
    { "path": "../outputs/metrics/metrics.json" }
  ],
  "notes": "Set random seed = 1337. Deterministic mode enabled.",
  "canonical_digest": "sha256:<digest_of_this_json_canonicalized>"
}
```
</details>

---


## 🛡️ Safety, Sensitivity & Governance

### 🚫 Never commit secrets
No API keys, tokens, passwords, private SSH keys, etc.

### 🧠 Classify everything
Each input must be labeled:
- `public` ✅
- `internal` 🟡
- `restricted` 🔴 (PII, sensitive locations, culturally sensitive data, embargoed sources)

### 🧯 If it’s sensitive…
- Prefer **aggregation / redaction / generalization**.
- If originals must be used, store them in **restricted storage** and keep only:
  - a pointer (URI)
  - access policy
  - checksum/digest
  - justification

---

## 🧪 PROV: How Inputs Connect to the Experiment

Think of each input file as a **PROV Entity**.
The experiment run is a **PROV Activity** that `prov:used` those entities and `prov:generated` the outputs.

If your report template includes `artifacts/provenance/`, link to it from your report.