# `data/` — Governed datasets, catalogs, and provenance (KFM)

> [!IMPORTANT]
> **Processed is the only publishable source of truth.**  
> `data/raw/` and `data/work/` are **never** served directly to users—only referenced by lineage/provenance. [oai_citation:2‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

This folder is the **governed data substrate** for Kansas Frontier Matrix (KFM): it contains the **Raw → Work → Processed** zones *and* the machine-readable catalogs (**DCAT/STAC/PROV**) and validation artifacts required to promote datasets safely and reproducibly. [oai_citation:3‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2) [oai_citation:4‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Table of contents

- [Truth path](#truth-path)
- [Directory layout](#directory-layout)
- [Zones and invariants](#zones-and-invariants)
  - [Raw](#raw)
  - [Work](#work)
  - [Processed](#processed)
  - [Catalog (DCAT / STAC / PROV)](#catalog-dcat--stac--prov)
- [ID strategy and naming conventions](#id-strategy-and-naming-conventions)
- [Formats and storage](#formats-and-storage)
- [Policy labels and sensitivity handling](#policy-labels-and-sensitivity-handling)
- [Ingestion workflow](#ingestion-workflow)
- [Validation gates](#validation-gates)
- [Promotion gates (CI-enforced)](#promotion-gates-ci-enforced)
- [What to commit to Git](#what-to-commit-to-git)
- [Examples](#examples)
- [Definition of Done for a dataset integration PR](#definition-of-done-for-a-dataset-integration-pr)
- [References](#references)

---

## Truth path

KFM’s end-to-end “truth path” (from governed raw inputs to public UI + auditable answers) is:

**Raw → Work → Processed → STAC/DCAT/PROV → Stores → API → UI → Stories → Focus Mode** [oai_citation:5‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

```mermaid
flowchart LR
  RAW[data/raw] --> WORK[data/work]
  WORK --> PROC[data/processed]
  PROC --> CATS[data/catalog (DCAT/STAC/PROV)]
  CATS --> STORES[Stores\n(PostGIS/Neo4j/Search/ObjectStore)]
  STORES --> API[API Gateway]
  API --> UI[Web UI]
  UI --> STORIES[Stories]
  STORIES --> FOCUS[Focus Mode]
```

> [!NOTE]
> The runtime request path is governed at the **trust membrane** (API + policy boundary). Frontend does not talk to databases directly, and policy evaluation occurs on every request. [oai_citation:6‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

---

## Directory layout

> **Design intent:** A human can browse datasets and their provenance; a pipeline can validate, promote, and publish them; CI can fail fast when governance requirements are missing.

```text
data/
  README.md                           # you are here

  raw/                                # immutable source drops + fetch manifests
  work/                               # intermediate artifacts + QA/validation outputs
  processed/                          # publishable artifacts ONLY (served via API)

  catalog/                            # machine-readable catalogs consumed by runtime services
    dcat/                             # dataset-level metadata (DCAT)
    stac/                             # spatial asset catalogs (STAC)
    prov/                             # lineage + transformations (PROV)
    _profiles/                        # KFM profile docs + validator configs (recommended)

  runs/                               # pipeline run records (JSON) + links to validation reports
  reports/                            # validation reports, profiling metrics, drift reports, QA notes

  _templates/                         # dataset skeletons (optional convenience)
  _scratch/                           # local-only scratch (should be gitignored)
```

> [!WARNING]
> Folder names are **contractual**: validators and pipeline tooling should treat these paths as stable interfaces.

---

## Zones and invariants

### Raw

**Purpose:** Immutable “source of record” drops and/or fetch manifests. Raw is referenced by lineage; it is not user-facing. [oai_citation:7‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

**Rules:**
- ✅ Raw assets must be **checksummed** and addressable by content hash. [oai_citation:8‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- ✅ Raw manifests must be **deterministic** (stable ordering; stable checksums). [oai_citation:9‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- ❌ Do not overwrite raw files in-place; new fetches create new versions (see [ID strategy](#id-strategy-and-naming-conventions)). [oai_citation:10‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

Recommended structure per dataset:
```text
data/raw/<dataset_id>/<dataset_version>/
  manifest.json
  checksums.sha256
  upstream/                # optional: preserved upstream naming/layout
```

### Work

**Purpose:** Regenerable intermediate artifacts used for normalization, QA, and debugging. [oai_citation:11‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

**Rules:**
- ✅ May be regenerated; treat as “build output” unless explicitly governed.
- ✅ Store validation reports and QA notes here (or under `data/reports/`) so promotion can be blocked when missing/incomplete. [oai_citation:12‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

Recommended structure:
```text
data/work/<dataset_id>/<dataset_version>/
  normalized/               # canonicalized raw → normalized
  validation_report.json
  profiling.json
  notes.md                  # optional: human QA notes (governed if referenced)
```

### Processed

**Purpose:** Publishable artifacts served by the API and rendered in UI/stories. Must include required catalogs + checksums. [oai_citation:13‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

**Rules:**
- ✅ Every promoted artifact must have a **PROV chain** and a deterministic checksum. [oai_citation:14‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- ✅ License + attribution must be captured in DCAT; restrictions encoded in policy. [oai_citation:15‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- ❌ Do not place ad-hoc files here—**only** artifacts that have passed validation + policy gates.

Recommended structure:
```text
data/processed/<dataset_id>/<dataset_version>/
  data/                      # parquet/geojson/cog/etc (or pointers if external)
  metadata/                  # derived metadata used by runtime
  checksums.sha256
```

### Catalog (DCAT / STAC / PROV)

Catalogs are **machine-readable** and consumed by runtime services. KFM uses:
- **DCAT** for dataset-level metadata (publisher, license, spatial/temporal coverage, update frequency, contacts). [oai_citation:16‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **STAC** for geospatial assets (rasters/vectors) for map/timeline rendering (Collection per product; Items per time/area unit). [oai_citation:17‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **PROV** for transformation lineage (inputs → activity → outputs). [oai_citation:18‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

Recommended structure:
```text
data/catalog/dcat/<dataset_id>/<dataset_version>.jsonld
data/catalog/stac/<dataset_id>/collection.json
data/catalog/stac/<dataset_id>/items/<item_id>.json
data/catalog/prov/<dataset_id>/<dataset_version>/run_<run_id>.json
```

---

## ID strategy and naming conventions

KFM’s identifier rules emphasize determinism + stability:
- Dataset IDs are **stable** (publisher + product + scope).
- DatasetVersion IDs are **content-addressed** (hash of raw manifest + metadata).
- User-visible evidence citations reference **DatasetVersion + source_record_id(s)**.
- Every transformation produces **new identifiers**; never overwrite prior versions. [oai_citation:19‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

### Naming rules (recommended)

| Concept | Field | Rule | Example |
|---|---|---|---|
| Dataset | `dataset_id` | `kebab-case`, stable | `kansas-mesonet-stations` |
| Version | `dataset_version` | content-addressed (hash) or `vYYYYMMDD...` derived from manifest hash | `sha256_4b1d...` |
| Source record | `source_record_id` | stable per upstream semantics | `nwis:site:06891000` |
| Run | `run_id` | timestamp + dataset + commit/image (implementation choice) | `run_2026-02-12T120000Z__...` |

> [!NOTE]
> Time model: use ISO-8601 timestamps with explicit time zones (or UTC); represent uncertain time as `[start,end]` intervals; for historical sources store publication date and event date claim separately (each with its provenance). [oai_citation:20‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Formats and storage

Recommended format targets for ingested sources include:
- JSON/CSV for tabular
- GeoJSON/Parquet for vectors
- COG for rasters
- PDF/JPEG/PNG for media artifacts [oai_citation:21‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

> [!NOTE]
> For extremely large datasets, store **metadata + pointers** when mirroring is impractical, and cache derived tiles for map preview (where allowed). [oai_citation:22‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Policy labels and sensitivity handling

KFM sensitivity is handled by:
1) policy labels at dataset/record/field level,  
2) derivative datasets with explicit redaction provenance, and  
3) fail-closed policy checks. [oai_citation:23‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

### Policy labels (minimum)

The integration blueprint uses (at least) `public | restricted | sensitive-location` as a config-level policy label. [oai_citation:24‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

It also recommends sensitivity classes including:
- **Public** (safe to publish)
- **Restricted** (role-based access)
- **Sensitive-location** (coordinates generalized/suppressed)
- **Aggregate-only** (publish only above thresholds) [oai_citation:25‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

> [!IMPORTANT]
> **Redaction is a first-class transformation** recorded in PROV. Raw remains immutable; the redacted derivative is a separate DatasetVersion (often separate dataset_id) with a documented policy label. [oai_citation:26‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Ingestion workflow

KFM ingestion is connector-driven and follows:
**discover → acquire → normalize → validate → enrich → publish** [oai_citation:27‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

```mermaid
flowchart TD
  D[Discover] --> A[Acquire]
  A --> N[Normalize]
  N --> V[Validate]
  V --> E[Enrich]
  E --> P[Publish]
  P --> C[Update DCAT/STAC/PROV]
  C --> R[Trigger index refresh\n(search/graph)]
```

Key expectations:
- Normalize to canonical encodings (UTF-8), geometry (WGS84), and time (ISO 8601). [oai_citation:28‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- Publish promotes to Processed, updates catalogs (DCAT/STAC/PROV), triggers index refresh. [oai_citation:29‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Validation gates

Minimum validation gates include:
- Row-level schema validation (required fields; coercion rules documented)
- Geometry validity + bounds
- Temporal consistency (no future dates for historic archives; no negative durations)
- License + attribution captured in DCAT; restrictions encoded in policy
- Provenance completeness: promoted artifact has PROV chain + deterministic checksum [oai_citation:30‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Promotion gates (CI-enforced)

Promotion gates are CI-enforced checks that must be satisfied before anything is considered publishable.

From the integration blueprint (catalog + promotion requirements):
- All raw assets checksummed and addressable by content hash
- Schema validation passes; QA report stored with stable ID
- Policy labels attached
- Catalog writers succeed (DCAT/STAC/PROV well-formed and link-check clean)
- Contract tests for dependent API queries pass [oai_citation:31‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

From the Next-Gen blueprint (promotion checklist summary):
- license present
- sensitivity classification present
- schema/geospatial checks pass
- checksums computed
- STAC/DCAT/PROV artifacts exist and validate
- audit event recorded
- human approval if sensitive [oai_citation:32‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2) [oai_citation:33‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)

---

## What to commit to Git

> [!WARNING]
> **Secrets are never committed.** If upstream requires keys, store them in vault/secret manager, not in this repo. [oai_citation:34‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

Recommended Git policy (practical + governance-friendly):
- ✅ Commit: manifests, checksums, catalogs (DCAT/STAC/PROV), run records, validation reports, small sample slices (if policy allows).
- ❌ Do not commit: large binaries and bulk raw drops unless explicitly approved (prefer object store + pointers). [oai_citation:35‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Examples

### Example: pipeline run record (illustrative)

```json
{
  "run_id": "run_2026-02-12T120000Z__example__v1",
  "dataset_id": "example_dataset",
  "inputs": [{"uri":"data/raw/example_dataset/sha256_.../manifest.json","sha256":"..."}],
  "code": {"git_sha":"...","image":"kfm/pipeline:..."},
  "outputs": [{"uri":"data/processed/example_dataset/sha256_.../data/example.parquet","sha256":"..."}],
  "validation_report": "data/reports/example_dataset/sha256_.../validation_report.json",
  "prov_ref": "data/catalog/prov/example_dataset/sha256_.../run_run_2026-02-12T120000Z__example__v1.json"
}
```

### Example: catalog expectations (at a glance)

| Standard | What it covers | Where it lives |
|---|---|---|
| DCAT | Dataset-level metadata | `data/catalog/dcat/` |
| STAC | Spatial assets (rasters/vectors) | `data/catalog/stac/` |
| PROV | Lineage (inputs → activity → outputs) | `data/catalog/prov/` |

---

## Definition of Done for a dataset integration PR

Use this checklist as a PR gate for adding/updating a dataset integration:

- [ ] Connector implemented + registered in the data-source registry config [oai_citation:36‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Raw acquisition produces deterministic manifest + checksums [oai_citation:37‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Normalization emits canonical schema and/or STAC assets [oai_citation:38‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Validation gates implemented and enforced in CI [oai_citation:39‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Policy labels defined; restricted fields/locations are redacted per rules [oai_citation:40‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Catalogs emitted (**DCAT always; STAC/PROV as applicable**) and link-check clean [oai_citation:41‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] API contract tests pass for at least one representative query [oai_citation:42‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## References

- KFM Next-Generation Blueprint (2026-02-12): repo layout, trust membrane, truth path, data zones/invariants. [oai_citation:43‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2) [oai_citation:44‡KFM_NextGen_Blueprint_and_Primary_Guide_v1_2_EXPANSIVE_TOC.pdf](sediment://file_00000000de5071fd8771d2d96fda3ac2)
- KFM Data Source Integration Blueprint (v1.0, 2026-02-12): ingestion workflow, validation gates, catalog standards, sensitivity + redaction, deterministic IDs. [oai_citation:45‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) [oai_citation:46‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)