# Kansas-Frontier-Matrix

<details>
<summary><strong>■ Metadata (MetaBlock v2)</strong></summary>

| field | value |
|---|---|
| doc_kind | universal_doc |
| id | kfm.repo.readme |
| title | Kansas-Frontier-Matrix |
| status | draft |
| last_updated | 2026-02-19 |
| owners | kfm:team:core |
| sensitivity | public |
| licenses | CC-BY-4.0 |
| evidence_policy.focus_mode | cite_or_abstain |
| evidence_policy.redaction_profile | public_default |

```kfm-meta
{
  "doc_kind": "universal_doc",
  "id": "kfm.repo.readme",
  "title": "Kansas-Frontier-Matrix",
  "status": "draft",
  "last_updated": "2026-02-19",
  "owners": ["kfm:team:core"],
  "sensitivity": "public",
  "licenses": ["CC-BY-4.0"],
  "repo": {
    "root_name": "Kansas-Frontier-Matrix",
    "product_short_name": "KFM"
  },
  "evidence_policy": {
    "focus_mode": "cite_or_abstain",
    "redaction_profile": "public_default"
  }
}
```

</details>

<!-- Badges: wire these to real workflows once .github/workflows exist -->
![CI](https://img.shields.io/badge/CI-gates%20pending-lightgrey)
![Docs](https://img.shields.io/badge/docs-MetaBlock%20v2-lightgrey)
![Catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-lightgrey)
![Policy](https://img.shields.io/badge/policy-OPA%2FRego-lightgrey)
![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey)

**Kansas-Frontier-Matrix** is the repository + system root.  
**KFM** is the product shorthand used in docs, schemas, APIs, and the UI.

Kansas Frontier Matrix (KFM) is a **governed spatio‑temporal knowledge platform** that turns Kansas data—remote sensing, hydrology, air quality/smoke, soil, resources, infrastructure (roads/bridges), economy, migration, flora/fauna, weather, disasters, geology (incl. core samples), history/archaeology, education, and science—into:

- 🗺️ **Map layers** that are time-aware and policy-labeled
- 📖 **Story Mode** narratives that show the “why” with auditable evidence
- 🔎 **Focus Mode** answers that are **cite‑or‑abstain**
- 🧪 **What‑if scenarios** with deterministic run receipts and reproducible outputs
- 📦 **Exportable notebooks** (Kaggle-ready) for specific science projects and public demos

> [!IMPORTANT]
> **Fail‑closed governance is a feature, not a restriction.**  
> If schema/QA/policy/provenance cannot be verified, the system must **not** publish.

> [!NOTE]
> This README describes the **target architecture and governance contract**.  
> Some paths, workflows, and automation may be **planned** and not yet implemented in the repo.

---

## Table of contents

- [Start here](#start-here)
- [Canonical truth path](#canonical-truth-path)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Governance quick view](#governance-quick-view)
- [Data domains](#data-domains)
- [Kansas source registry](#kansas-source-registry)
- [Source coverage gate](#source-coverage-gate)
- [Remote sensing and gridded products](#remote-sensing-and-gridded-products)
- [Connector contract](#connector-contract)
- [Governed API](#governed-api)
- [Notebooks and Kaggle exports](#notebooks-and-kaggle-exports)
- [What-if scenarios](#what-if-scenarios)
- [Repository layout](#repository-layout)
- [Contributing](#contributing)
- [Security and sensitivity](#security-and-sensitivity)
- [License](#license)
- [Glossary](#glossary)

---

## Start here

If you are new to KFM:

1) **Understand the rules:** Read [Non-negotiable invariants](#non-negotiable-invariants) and [Governance quick view](#governance-quick-view).  
2) **Understand the flow:** Read [Canonical truth path](#canonical-truth-path) and [Connector contract](#connector-contract).  
3) **Find what’s missing:** Read [Source coverage gate](#source-coverage-gate) and the [Kansas source registry](#kansas-source-registry).  

If you want to contribute immediately:

- Add a **new source entry** to `catalogs/source_registry.json` and implement a connector that can pass all promotion gates.
- Or improve governance: add policy tests, redaction profiles, schema validators, and coverage reporting.

---

## Canonical truth path

**No bypasses.** Every layer, story, export, and Focus answer follows the same chain:

**Data Sources → Pipelines → Catalogs/Provenance → Storage/Index → Governed API → UI/Story + Focus**

### Data lifecycle zones

Promotion is append-only. Artifacts move forward only when all gates pass.

```mermaid
flowchart LR
  R[Raw\nimmutable capture + receipts] --> W[Work/Quarantine\nnormalize/repair]
  W --> P[Processed\nvalidated + index-ready]
  P --> U[Published\npolicy-reviewed + curated]
  U --> C[Curated\nblessed for teaching/products]
```

---

## Non-negotiable invariants

### Trust membrane

- The browser/UI **never** reads from databases, search, or object storage directly.
- All access flows through the **Governed API** (auth + policy + audit + provenance).
- Presigned URLs (if used) are issued **server-side after policy** and are **short-lived**.

### Promotion gates

Nothing becomes **Published/Curated** unless CI verifies:

- ✅ domain schema validation
- ✅ QA metrics + anomaly report
- ✅ policy labels + redaction rules declared
- ✅ provenance completeness (PROV)
- ✅ catalogs emitted (DCAT always; STAC for spatial assets)
- ✅ deterministic IDs + immutable versions + checksums (and attestations where required)

### Focus Mode is cite-or-abstain

- Every user-visible claim must cite governed evidence.
- If evidence is missing or blocked by policy, Focus Mode must **abstain** or return a “needs verification” response with an audit receipt.

### Deterministic identity and immutability

- Stable dataset IDs
- Immutable/content-addressed dataset versions
- No overwrite; new versions only

---

## Governance quick view

KFM treats governance as an enforcement system, not an afterthought.

| Concern | Enforcement point | Fail-closed rule | Typical mechanism |
|---|---|---|---|
| Licensing | Promotion gate + API | No publish without declared license | DCAT license fields + CI checks |
| Sensitivity | API + catalogs | Restricted ≠ public | Policy labels + redaction profiles |
| Indigenous Data Sovereignty | Governance process + policy | No assumption of permission | Authority-to-control rules + review |
| Privacy | API + exports | No doxxing | aggregation, suppression thresholds |
| Provenance | Promotion gate + Focus Mode | No cite = no claim | PROV graphs + evidence bundles |
| Auditability | API | Every response gets a receipt | request_id + decision_id |

> [!WARNING]
> If access, permission, or sensitivity is unclear, treat it as **restricted** until governance review approves publication.

---

## Data domains

KFM treats Kansas as a **spatio-temporal fabric**: environment + built systems + people + history + science.

### Domain matrix

| Domain | Examples | Primary forms | Required catalogs | Typical QA gates | Sensitivity default |
|---|---|---|---|---|---|
| Remote sensing | satellite imagery, land cover, crop vigor, smoke | rasters, grids | DCAT + STAC + PROV | georeg + timestamps + nodata + stats | public/varies |
| Weather and climate | station series, reanalysis, radar composites | time series, grids | DCAT (+STAC if spatial) + PROV | units + continuity + outliers | public |
| Hydrology | streamflow, flood extents, aquifers | time series, vectors, grids | DCAT (+STAC if spatial) + PROV | topology + gauge sanity + CRS | public/varies |
| Soil and agriculture | SSURGO, cropland layers, crop stats | vectors, grids, tables | DCAT (+STAC if spatial) + PROV | range checks + joins | public |
| Geology and resources | mineral layers, induced seismicity, core samples | vectors, tables, scans | DCAT + PROV (+STAC if spatial/scans) | schema + location generalization | **restricted by default** |
| Transportation and infrastructure | **KDOT** roads/bridges/traffic/projects | vectors, tables | DCAT + PROV | network validity + geometry + timestamps | public/varies |
| Economy and migration | census/ACS, NASS, IRS migration | tables | DCAT + PROV | totals + continuity + definitions | public |
| Flora and fauna | GBIF, eBird, iNaturalist, habitats | points, polygons | DCAT + PROV | coordinate plausibility | sensitive species restricted |
| Hazards and disasters | wildfire perimeters, storm events, drought | vectors, rasters, tables | DCAT (+STAC if spatial) + PROV | event integrity + timestamps | public |
| History and archaeology | figures, facts, KHRI summaries | text, tables, generalized geometry | DCAT + PROV | citation completeness | **restricted by default** |
| Land and ownership | patents, PLSS, parcels (if licensed) | vectors, tables | DCAT + PROV | joins + privacy rules | restricted by default |
| Public safety stats | aggregated indicators only | tables | DCAT + PROV | suppression thresholds | public stats only |
| Education and discovery | institutions, research outputs | tables, docs | DCAT + PROV | source credibility | public |

> [!NOTE]
> “Ingested” does not mean “public.” Publication is a **policy decision** plus a successful **gate**.

---

## Kansas source registry

To prevent “we forgot KDOT/core samples/etc.” KFM maintains a **Source Registry**: the canonical list of expected sources and their governance requirements.

**Expected file:** `catalogs/source_registry.json` (may be planned)

Each entry declares:

- `source_id` (stable)
- domain tags
- priority (P0/P1/P2)
- required stage (processed/published/curated)
- required catalogs (`dcat`, `stac`, `prov`)
- default sensitivity + redaction profile
- QA profile and thresholds
- authoritative upstream and access pattern (API/bulk/service/manual)

### Starter registry

> This table is a **starter list**. The canonical source-of-truth is `catalogs/source_registry.json`.

| P | source_id | Domain | What it unlocks | Sensitivity default |
|---:|---|---|---|---|
| P0 | `kdot.transportation.assets` | roads/bridges | statewide infrastructure layers + bridge/road storylines | public/varies |
| P0 | `fhwa.nbi.kansas` | bridges | independent validation of bridge inventory/condition | public |
| P0 | `fhwa.hpms.kansas` | traffic | AADT, functional class, network measures | public |
| P0 | `kgs.geology.maps` | geology | geologic & physiographic maps, stratigraphy context | public |
| P0 | `kgs.core_samples.index` | core samples | core inventory + generalized location summaries | **restricted** |
| P0 | `usgs.nwis.kansas` | hydrology | gauges, streamflow time series, water conditions | public |
| P0 | `kwo.reservoirs.operations` | hydrology | reservoir ops, policy context, drought/flood narratives | public |
| P0 | `usda.nrcs.ssurgo` | soils | soil properties for crop/water/settlement analysis | public |
| P0 | `usda.nass.quickstats` | agriculture | county/commodity ag stats (time series) | public |
| P0 | `usda.nass.cdl` | remote sensing | annual cropland classification rasters | public |
| P0 | `usgs.nlcd` | remote sensing | land cover change baselines | public |
| P0 | `noaa.ncei.climate` | climate | station climate series + extremes | public |
| P0 | `ksu.mesonet` | weather | near real-time weather observations | public |
| P0 | `irs.migration.county` | migration | county-to-county migration patterns | public |
| P0 | `us_census.acs` | demographics/economy | population, housing, income, commuting | public |
| P0 | `ipums.nhgis` | historical demographics | long-range historical GIS/stat context | public |
| P0 | `blm.glo.land_patents` | historic land | homesteads/patents mapping + named historic narratives | public/medium (names) |
| P0 | `blm.plss.grid` | land grid | township-range-section joins and patent geocoding | public |
| P0 | `kshs.kansapedia` | history | figures/facts for Story Mode | public |
| P0 | `kshs.kansas_memory` | history/media | primary-source scans/photos for stories | public/varies |
| P0 | `khri.inventory` | archaeology/history | historic resources inventory (generalized sites) | **restricted** |
| P0 | `nifc.wildfire.perimeters` | hazards | wildfire perimeters and trends | public |
| P0 | `noaa.storm_events` | hazards | tornado/hail/wind event baselines | public |
| P0 | `gbif.occurrences` | biodiversity | multi-species observations | public/varies |
| P0 | `ebird.observations` | biodiversity | bird observations + seasonality | medium (sensitive species) |
| P0 | `inaturalist.observations` | biodiversity | citizen science occurrences | medium (sensitive species) |
| P0 | `air_quality.fusion.pm25` | smoke/air quality | smoke/PM2.5 narratives + exposure indicators | public/varies |

> [!WARNING]
> **Land ownership, core samples, archaeology site coordinates, protected species locations, and any “criminal history” beyond aggregated stats are restricted by default.**  
> KFM should publish **summaries**, not doxxing.

---

## Source coverage gate

KFM automates “what’s missing?” as a **fail-closed CI gate**.

### Coverage inputs

- `catalogs/source_registry.json` (expected universe)
- `catalogs/dcat/` (what’s governed)
- `catalogs/stac/` (what’s spatial/time-sliced)
- `catalogs/prov/` (what has lineage)

### Coverage rules

The gate fails if any **P0** source:

- has no DCAT record, or
- lacks required STAC/PROV catalogs, or
- has missing/invalid sensitivity labels, or
- violates publication rules (restricted data marked public), or
- lacks provenance for any promoted artifact.

### Coverage outputs

- `reports/source_coverage.md` (human-friendly)
- `reports/source_coverage.json` (machine)
- non-zero exit code on policy violation

---

## Remote sensing and gridded products

Remote sensing is treated as first-class, STAC-native, and reproducible.

### Preferred asset formats

- **COG GeoTIFF** for imagery and derived index rasters
- **Zarr** for large time-series grids
- **GeoParquet / FlatGeobuf** for vector derivatives

### Product taxonomy

| Product type | Example | Stored as | Catalog | Notes |
|---|---|---|---|---|
| Scene | Sentinel/Landsat scenes | COG | STAC Item | immutable capture + per-scene QA |
| Mosaic | weekly/monthly composites | COG | STAC Item | derived from scenes; PROV required |
| Index raster | NDVI-like, drought proxy | COG | STAC Item | include units/scale in metadata |
| Gridded time series | precip/temp reanalysis | Zarr/NetCDF | STAC Collection (+Items) | chunk strategy matters |
| Event products | flood extent, fire perimeter raster | COG + vectors | STAC + DCAT | event IDs and timestamps required |
| ML inference | building footprints, crop type model | vectors/rasters | STAC + PROV | model card + provenance required |
| Tiles | raster tiles for UI | generated cache | not authoritative | derived convenience only |

### Remote sensing truth flow

```mermaid
flowchart TD
  A[Acquire Raw\nchecksums + receipt] --> B[Normalize\nCRS/bands/timestamps]
  B --> C[Validate\nQA metrics + anomalies]
  C --> D[Process\nCOG/Zarr + derived products]
  D --> E[Catalog\nSTAC + PROV + DCAT]
  E --> F[Index\nbbox/time/tags]
  F --> G[Serve\nGoverned API]
  G --> H[Render\nMap/Story/Focus]
```

### Minimum QA metrics

- Raster: nodata %, min/max, percentiles, band means/stddev, footprint validity
- Temporal: no future timestamps (unless forecast), monotonic ordering where expected
- Spatial: CRS + bounds within expected region, pixel size consistency
- Joinability: stable IDs and crosswalks (county, watershed, ecoregion, GeoID)

---

## Connector contract

Every connector implements the same contract:

**discover → acquire → normalize → validate → publish**

Each run must generate:

- `run_manifest.json` (inputs, versions, params, environment hashes)
- `qa_report.json` (metrics, anomalies, thresholds)
- immutable artifacts with checksums
- catalogs:
  - DCAT (always)
  - STAC (for spatial assets)
  - PROV (for lineage)

### Example run manifest

```json
{
  "run_id": "run_2026-02-19T12:34:56Z_kdot_roads",
  "source_id": "kdot.transportation.assets",
  "inputs": [
    { "uri": "https://...", "retrieved_at": "2026-02-19T12:00:00Z", "sha256": "..." }
  ],
  "params": {
    "crs": "EPSG:4326",
    "publish_stage": "processed"
  },
  "environment": {
    "container_image": "ghcr.io/kfm/pipelines@sha256:...",
    "git_commit": "not_confirmed_in_repo"
  },
  "outputs": [
    { "artifact": "kfm://dataset/kdot_roads@sha256:...", "sha256": "..." }
  ]
}
```

### Definition of Done for any new source

- [ ] added to `catalogs/source_registry.json`
- [ ] DCAT record includes license, owners, cadence, sensitivity, policy tags
- [ ] PROV lineage covers acquire→normalize→validate→publish
- [ ] STAC exists for spatial/remote sensing assets
- [ ] QA thresholds defined and met
- [ ] policy tests pass (OPA/Rego)
- [ ] governed API can serve it with provenance + decision IDs
- [ ] UI can render it without direct storage access

---

## Governed API

The governed API is the enforcement point.

It must:

1) authenticate and authorize  
2) evaluate policy (OPA) and apply redactions and aggregation  
3) attach provenance and citations  
4) log an auditable receipt (request_id + decision_id + evidence bundle hash)

### Response envelope

```json
{
  "data": {},
  "policy": {
    "label": "public",
    "redactions_applied": [],
    "decision_id": "opa:decision:..."
  },
  "provenance": {
    "bundle_ref": "oci://kfm-evidence/dataset@sha256:...",
    "citations": [
      { "dataset_version": "kfm://dataset/ID@sha256:...", "record_id": "..." }
    ]
  },
  "meta": {
    "request_id": "req_...",
    "generated_at": "2026-02-19T12:34:56Z"
  }
}
```

### Minimal endpoint set

- `GET /api/v1/datasets`
- `GET /api/v1/datasets/{dataset_id}/versions`
- `POST /api/v1/stac/search` (policy-filtered)
- `POST /api/v1/evidence/resolve` (server-side verification)
- `POST /api/v1/focus/query` (evidence → answer; cite-or-abstain)
- `POST /api/v1/exports/notebook` (policy-approved extracts + manifest)

---

## Notebooks and Kaggle exports

Notebooks are treated as **governed artifacts**, not ad-hoc files.

### Notebook project requirements

- immutable dataset version refs (no “latest”)
- pinned dependencies (lockfile)
- export manifest (checksums + provenance)
- explicit policy label for every included dataset or extract

> [!NOTE]
> Notebooks can be public even if source datasets are not—**only if exports are policy-approved and sanitized**.

---

## What-if scenarios

“What if” is a governed workflow:

- scenario spec (inputs + assumptions)
- deterministic run receipt
- derived layers (policy-labeled)
- citations to source dataset versions
- optional Story Node output (“explain this scenario”)

---

## Repository layout

> [!NOTE]
> Layout below is the intended structure. Some folders may be planned.

```text
Kansas-Frontier-Matrix/
├── README.md                          # Root overview: invariants, source universe, how to build
├── apps/
│   └── web/                           # Map UI (layers/timeline), Story Mode, Focus Mode
├── services/
│   ├── api/                           # Governed API (auth + OPA policy + evidence resolver)
│   ├── pipelines/                     # Connectors + orchestration (truth path)
│   │   ├── connectors/
│   │   │   ├── remote_sensing/        # satellite/landcover/crops/smoke; STAC-first
│   │   │   ├── hydrology/             # USGS NWIS, aquifers, reservoirs; time series + event layers
│   │   │   ├── air_quality/           # smoke/PM2.5 fusion products; aggregation-aware
│   │   │   ├── soils_ag/              # SSURGO, NASS, CDL; joins to GeoIDs
│   │   │   ├── transportation_kdot/   # KDOT roads/bridges/traffic/projects; network QA
│   │   │   ├── geology_resources/     # KGS maps/resources/seismic; restricted defaults
│   │   │   ├── core_samples/          # core inventory + generalized summaries; restricted
│   │   │   ├── economy_migration/     # Census/ACS, IRS migration, indicators
│   │   │   ├── biodiversity/          # GBIF/eBird/iNaturalist; sensitive species controls
│   │   │   ├── hazards_disasters/     # wildfire/flood/storm event products
│   │   │   ├── land_records/          # BLM GLO/PLSS; ownership rules + redactions
│   │   │   └── history_archaeology/   # Kansapedia/Kansas Memory/KHRI; generalized locations
│   │   ├── engine/                    # reusable pipeline primitives (ports/adapters)
│   │   └── specs/                     # deterministic connector specs (versioned)
│   ├── policy/                        # OPA/Rego + tests + redaction profiles
│   ├── scenarios/                     # what-if orchestration + receipts + derived products
│   └── search/                        # indexing pipelines + analyzers
├── catalogs/
│   ├── dcat/                          # Dataset governance metadata (license, owners, sensitivity, cadence)
│   ├── stac/                          # Spatial catalogs (rasters/vectors, time slices)
│   ├── prov/                          # Provenance graphs (lineage of transforms)
│   └── source_registry.json           # Expected universe (drives coverage gate)
├── schemas/
│   ├── docs/                          # MetaBlock v2 schemas + doc-lint rules
│   ├── dcat/                          # DCAT profiles/schemas
│   ├── stac/                          # STAC profiles/extensions used by KFM
│   └── prov/                          # PROV profiles
├── notebooks/
│   ├── templates/                     # Kaggle-ready templates (governed)
│   ├── projects/                      # science projects and scenario notebooks
│   └── exports/                       # generated export bundles (append-only + checksums)
├── docs/
│   ├── universal/                     # Universal docs (MetaBlock v2)
│   ├── story_nodes/                   # Story Nodes (MetaBlock v2)
│   ├── runbooks/                      # ops runbooks
│   └── standards/                     # promotion contract, policy standards, schema rules
├── infra/
│   ├── compose/                       # single-host Linux deployment
│   ├── k8s/                           # Kubernetes/OpenShift manifests
│   └── gitops/                        # ArgoCD/Flux environments
└── .github/
   └── workflows/                      # CI: docs-lint, catalog-lint, policy tests, source-coverage gate
```

---

## Contributing

KFM prefers PR-centric promotion.

1) add or modify connector spec(s) in `services/pipelines/specs/`  
2) run connector to generate artifacts + receipts + catalogs  
3) ensure `catalogs/source_registry.json` is updated (or confirm it already includes the source)  
4) open PR containing:
   - catalogs (DCAT/STAC/PROV)
   - QA reports + receipts
   - evidence bundle references (digests)
5) CI enforces gates  
6) merge promotes to Published/Curated (per policy)

> [!TIP]
> If you cannot provide provenance, QA, and policy labeling, contribute upstream improvements (schemas, validators, tests) until the gate can be satisfied.

---

## Security and sensitivity

Some domains are inherently sensitive and default to restricted handling:

- land ownership and parcel-level details
- core sample exact locations and certain resource layers (policy dependent)
- archaeology site coordinates and protected sites
- protected species precise locations
- public safety beyond aggregated statistics
- critical infrastructure details

Default behavior:

- generalize or redact location where needed
- suppress small counts
- publish summaries or aggregates only unless explicitly cleared
- log policy decisions (decision IDs) for auditability

---

## License

- Documentation in this repo is licensed **CC-BY-4.0** unless otherwise noted in-file.
- Datasets ingested by KFM retain their upstream licenses and access constraints; KFM catalogs must record this explicitly.

> [!IMPORTANT]
> “Open source repo” does not mean “all data is open.” Licenses and community authority are enforced at the catalog and API layers.

---

## Glossary

- **DCAT** — dataset governance catalog (license, ownership, cadence, sensitivity)
- **STAC** — SpatioTemporal Asset Catalog (collections/items for spatial assets)
- **PROV** — provenance graph (what transformed what, when, and how)
- **OPA/Rego** — policy engine and policy language
- **COG** — Cloud Optimized GeoTIFF
- **Zarr** — chunked array format for large gridded time series
