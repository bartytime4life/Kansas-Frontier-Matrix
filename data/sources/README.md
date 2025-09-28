# `data/sources/` — Curated Source Descriptors

This folder contains **small, hand-edited JSON descriptors** for all data sources
used in the Kansas-Frontier-Matrix pipeline.  
They serve as the **source of truth** for fetch/ETL jobs and are validated against
a schema (`schema.source.json`).

---

## Purpose

- Document external data dependencies (URLs, license, provenance).
- Provide reproducible recipes for fetching raw datasets.
- Feed into the `make fetch` and `make stac` targets.
- Ensure **transparency & reproducibility** in the historical GIS pipeline.

Descriptors are kept **tiny and explicit** (usually a few KB).  
Large raw data files are never stored here — they go to `data/raw/` (ignored by git).

---

## Descriptor schema

See [`schema.source.json`](./schema.source.json).  
Core required fields:

| Field        | Type    | Description                                                      |
|--------------|---------|------------------------------------------------------------------|
| `id`         | string  | Unique machine-safe identifier (lowercase, `_` or `-` allowed).  |
| `title`      | string  | Human-readable name of the dataset.                              |
| `type`       | enum    | One of `vector`, `raster`, `collection`, `service`.              |
| `period`     | string  | Temporal coverage (e.g. `1936`, `1930s`, `1854-1861`).           |
| `urls`       | array   | Download URLs or service endpoints.                              |
| `bbox`       | array   | Spatial extent `[west, south, east, north]` in EPSG:4326.        |
| `crs`        | string  | Coordinate system (default: `EPSG:4326`).                        |
| `license`    | object  | Name + URL to license info.                                      |
| `provenance` | object  | Attribution, publisher, DOI, or citation.                        |
| `retrieved`  | string  | ISO 8601 datetime when last fetched.                             |
| `confidence` | number  | Optional confidence score (0.0–1.0).                             |
| `notes`      | string  | Free-form comments.                                              |

---

## Workflow

1. **Create/edit a descriptor** under `data/sources/*.json`.
2. **Validate** against schema:
   ```bash
   make validate-sources
````

3. **Fetch raw data**:

   ```bash
   make fetch
   ```

   → downloads to `data/raw/` and records checksums.
4. **Process** via `make cogs`, `make vectors`, etc.
   → outputs to `data/processed/**` or `data/cogs/**`.
5. **Build STAC** metadata:

   ```bash
   make stac
   ```

---

## Examples

* `ks_hydrography.json` — Kansas surface water layers.
* `ks_roads_1930s.json` — Historic roads dataset.
* `ks_landcover_1936.json` — Land-cover classification snapshot.

Each descriptor may point to multiple files in `urls[]`
(e.g., county-by-county sheets). The fetch step will fan-out and merge.

---

## Git policy

* Descriptors are **always tracked** in git.
* `.gitignore` keeps raw data (`data/raw/**`) out of version control.
* Changes to descriptors trigger CI checks:

  * schema validation
  * license/provenance presence
  * STAC rebuild

---

✦ **Summary:**
`data/sources/` is the **curated index** of all inputs.
It guarantees reproducibility, transparency, and traceability from source → processed artifact → STAC catalog.

```
