# Data Catalog

> [!IMPORTANT]
> KFM’s governed “truth path” is **Raw → Work → Processed → STAC/DCAT/PROV → Stores → API → UI → Stories → Focus Mode**. Catalog outputs live at the **STAC/DCAT/PROV** stage and are **required** for publication.  [oai_citation:0‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

## Why this directory exists

This folder holds the **DCAT** side of KFM’s catalog layer: the machine-readable dataset catalog used for:

- **Discovery** (search/browse datasets and distributions)
- **Governance enforcement** (license + sensitivity + checksums must be present before promotion/serving)
- **Cross-linking** with **STAC** (spatiotemporal assets) and **PROV** (lineage) so that “review evidence” is always possible.  [oai_citation:1‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a) [oai_citation:2‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

> [!IMPORTANT]
> **Processed is the only publishable source of truth.** Raw/work are never served directly to users.  [oai_citation:3‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

---

## System invariants this README assumes

These are not “nice to have”—they are architectural invariants in the KFM docs:

1. **Fail-closed promotion:** jobs must emit receipts and validation artifacts; promotion is blocked otherwise.  [oai_citation:4‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)
2. **Trust membrane:** the UI never directly accesses databases/object storage; access is through a governed API behind policy evaluation.  [oai_citation:5‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)
3. **Catalog + provenance required:** every publishable artifact must be described in catalogs (DCAT required; STAC + PROV core), and cross-links must validate.  [oai_citation:6‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

---

## Directory layout

The v13 repository layout guide describes `data/catalog/` as the home for DCAT outputs, alongside `data/stac/` and `data/prov/`.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

```text
data/
├── stac/
│   ├── collections/                 # STAC Collections
│   └── items/                       # STAC Items
├── catalog/
│   ├── README.md                    # You are here
│   └── dcat/                        # DCAT outputs (JSON-LD)
└── prov/                            # PROV bundles (per run / per dataset)
```
 [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Recommended sub-structure inside `data/catalog/dcat/`

> [!NOTE]
> The guide specifies `data/catalog/dcat/` but does not mandate internal subfolders. The structure below is a **recommended** convention to keep artifacts stable and reviewable.

```text
data/catalog/dcat/
├── catalog.jsonld                   # Optional: top-level dcat:Catalog graph
├── datasets/
│   ├── <dataset_id>.jsonld          # One dataset record per file (preferred)
│   └── ...
└── _index/
    └── datasets.csv                 # Optional: lightweight listing for CI/QA diffing
```

---

## What is DCAT in KFM terms

DCAT’s core model is: a **Catalog** contains **Dataset** records; each **Dataset** can have multiple **Distributions** (files or endpoints). DCAT also supports **DataService** entries for APIs.  [oai_citation:9‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1)

In KFM, treat these as governed runtime inputs:

| DCAT concept | KFM meaning | Governing intent |
|---|---|---|
| `dcat:Catalog` | The curated dataset-of-datasets | Stable entry point for harvesting/search |
| `dcat:Dataset` | A logical dataset release/series | Must include license + spatial/temporal scope |
| `dcat:Distribution` | A concrete artifact (GeoParquet, COG, PMTiles, etc.) | Must include checksums; points to processed artifact |
| `dcat:DataService` | An API endpoint serving datasets | Must be policy-gated like any other access |

---

## Cross-links: DCAT ↔ STAC ↔ PROV

KFM recommends a small “profile” approach so validators can enforce consistency:

- Every **STAC collection** should include license + extents, and link to a **DCAT dataset** entry.
- Every **DCAT dataset** should reference a **PROV activity** for publication (lineage).  [oai_citation:10‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

This is what enables auditability and “cite-or-abstain” behavior in Focus Mode.  [oai_citation:11‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

---

## KFM minimum DCAT profile

> [!NOTE]
> This is a **minimum** set aligned with examples in KFM docs (not a full DCAT-AP implementation). It’s meant to be machine-validatable and promotion-gate friendly.  [oai_citation:12‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

### Dataset fields

| Field | Required | Notes |
|---|---:|---|
| `dct:identifier` | ✅ | Stable, deterministic ID (e.g., `dataset:<id>` or URN strategy) |
| `dct:title` | ✅ | Human title |
| `dct:description` | ✅ | What it is + what it’s for |
| `dct:license` | ✅ | Must be present to pass promotion gates  [oai_citation:13‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a) |
| `dcat:keyword` | ✅ | Searchability |
| `dcat:distribution` | ✅ | At least one distribution |
| `dct:spatial` | ✅ | Region/coverage (URI or bbox strategy) |
| `dct:temporal` | ✅ | Interval/period |
| `dct:issued` / `dct:modified` | ◻️ | Recommended for release tracking |
| `prov:wasGeneratedBy` | ✅ | Points to the PROV Activity for the run/publication  [oai_citation:14‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a) |
| Sensitivity classification | ✅ | Required by promotion gate checklist  [oai_citation:15‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a) |

### Distribution fields

| Field | Required | Notes |
|---|---:|---|
| `dcat:downloadURL` (or equivalent access URL) | ✅ | Must resolve via governed resolver/API (never direct DB access)  [oai_citation:16‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46) |
| `dct:format` / `dcat:mediaType` | ✅ | Machine-readable type (GeoParquet, COG, etc.) |
| Checksums | ✅ | DCAT 3 supports `spdx:checksum` on distributions for integrity metadata.  [oai_citation:17‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1) |
| Size | ◻️ | Optional but helpful (`dcat:byteSize`) |

---

## Promotion gate checklist

KFM’s v1.2 Next-Gen blueprint proposes that each pipeline job emits a **run record** and a **validation report**, and **promotion is blocked unless both exist and are complete**.  [oai_citation:18‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

Use this checklist when reviewing a PR that changes catalog artifacts:

- [ ] License present and allowed
- [ ] Sensitivity classification present
- [ ] Schema and geospatial checks pass
- [ ] Checksums computed
- [ ] STAC/DCAT/PROV artifacts exist, validate, and cross-link correctly
- [ ] Audit event recorded
- [ ] Human approval recorded if sensitive
 [oai_citation:19‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

> [!TIP]
> DCAT profile validation is commonly enforced via **SHACL** (or equivalent shape validation), which can be integrated into CI to catch missing titles/licenses, invalid formats, and other structural errors before publishing.  [oai_citation:20‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1)

---

## Resolvable identifiers

The Next-Gen blueprint recommends that every provenance/citation reference is resolvable via an API endpoint scheme such as:

- `prov://`
- `stac://`
- `dcat://`
- `doc://`
- `graph://`
 [oai_citation:21‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)

This directory is the **source of truth** for the `dcat://…` namespace.

---

## How to add or update a dataset entry

1. **Create or update processed artifacts** (outside this folder).
2. Ensure the pipeline run produced receipts:
   - `run_record.json`
   - `validation_report.json`
   - (and any required manifests)
   Promotion should not proceed without them.  [oai_citation:22‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)
3. Create/refresh the dataset’s DCAT JSON-LD under:
   - `data/catalog/dcat/datasets/<dataset_id>.jsonld` (recommended)
4. Ensure the dataset record:
   - includes license + sensitivity classification
   - includes distributions pointing to publishable artifacts
   - includes checksum metadata for each distribution
   - links to the PROV Activity (`prov:wasGeneratedBy`)
5. Ensure cross-links exist:
   - STAC Collection links to the DCAT dataset
   - DCAT dataset references the PROV Activity
   (and all validate under current KFM profile expectations).  [oai_citation:23‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)
6. Run validators in CI (SHACL / JSON Schema / domain checks).  [oai_citation:24‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1)

<details>
<summary>Example JSON-LD skeleton for a dataset record</summary>

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "dataset:example_dataset",
  "dct:title": "Example Dataset",
  "dct:description": "What this dataset represents and why it exists.",
  "dct:license": "CC-BY-4.0",
  "dcat:keyword": ["kansas", "history"],
  "dct:spatial": "urn:kfm:place:kansas",
  "dct:temporal": "urn:kfm:period:1850-1900",
  "prov:wasGeneratedBy": "urn:kfm:prov:activity:run_YYYY_MM_DD_example_v1",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "application/parquet",
      "dcat:downloadURL": "dcat://download/processed/example.parquet",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "spdx:checksumAlgorithm_sha256",
        "spdx:checksumValue": "<sha256-hex>"
      }
    }
  ]
}
```

</details>

---

## Governance note on sensitive domains

KFM design docs explicitly call out sensitivity handling and generalization requirements for certain domains (e.g., archaeology/cultural heritage). Treat catalog metadata as **governed** too—do not publish fields that increase risk (precise locations, restricted site metadata, etc.) without an explicit policy decision and the required approvals.  [oai_citation:25‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

---

## Sources

This README is grounded primarily in these KFM documents:

- Next-Gen blueprint: truth path, data zones, catalog profiles, promotion gates, resolvable scheme requirements.  [oai_citation:26‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a) [oai_citation:27‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_0000000093e8722f9f2ac3ad03df334a)
- Master guide v13 layout notes: canonical repo paths for `data/catalog/dcat/` and related folders.  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Blueprint ideas pack: trust membrane + catalog/provenance plane requirement + sensitivity note.  [oai_citation:29‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46) [oai_citation:30‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)
- DCAT support notes: DCAT core model and checksum guidance; SHACL validation in CI.  [oai_citation:31‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1) [oai_citation:32‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1) [oai_citation:33‡KFM-Software Support.pdf](sediment://file_00000000ab28722fa3482ac03433a8e1)