<!--
doc_id: NEEDS VERIFICATION
title: Kansas Mesonet Soil Moisture Domain Specification
type: standard
version: v1
status: draft
owners: [NEEDS VERIFICATION]
created: 2026-04-01
updated: 2026-04-01
policy_label: NEEDS VERIFICATION
related: [
  "docs/domains/README.md",
  "docs/governance/ROOT_GOVERNANCE.md",
  "docs/governance/ETHICS.md",
  "docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md",
  "docs/standards/markdown-rules.md"
]
tags: [kfm, hydrology, soils, mesonet, timeseries, provenance, evidence]
notes: [
  "Repo paths and adjacent domain conventions NEEDS VERIFICATION.",
  "This document is scoped to public-facing source integration and does not assert implemented ingestion or publication status.",
  "Kansas Mesonet field names and API examples were validated against public source documentation on 2026-04-01."
]
-->

<a id="top"></a>

# Kansas Mesonet Soil Moisture Domain Specification

**One-line purpose:** Define how Kansas Mesonet soil moisture and related evapotranspiration data should be represented, ingested, validated, governed, and published within KFM.

**Status:** Draft  
**Owners:** NEEDS VERIFICATION  
**Path:** `docs/domains/hydrology/mesonet-soil.md`

![Status](https://img.shields.io/badge/status-draft-orange)
![Scope](https://img.shields.io/badge/scope-hydrology%20%7C%20soil-blue)
![Data](https://img.shields.io/badge/data-public%20source-green)
![Trust](https://img.shields.io/badge/trust-evidence--first-purple)
![Repo Fit](https://img.shields.io/badge/repo_fit-NEEDS%20VERIFICATION-lightgrey)

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Source profile](#source-profile) · [Acquisition](#acquisition-pattern) · [Schema](#canonical-record-shape) · [QA](#validation-and-quality-rules) · [Publication](#publication-and-trust-surface) · [Tasks](#task-list) · [FAQ](#faq)

---

## Scope

This document specifies the **KFM handling model** for Kansas Mesonet soil moisture observations and adjacent evapotranspiration data.

It covers:

- public source characterization
- expected acquisition patterns
- variable mapping
- canonical record shape
- provenance and trust requirements
- validation and publication rules
- map and time-series use within hydrology-facing surfaces

It does **not** claim that a live ingestion pipeline, catalog entry, or public API route already exists in this repository.

> [!IMPORTANT]
> **Truth label:** `PROPOSED` for KFM integration shape unless explicitly marked otherwise.  
> Public Kansas Mesonet field names and endpoint behaviors described here are source-grounded.  
> In-repo implementation status remains `NEEDS VERIFICATION`.

---

## Repo fit

| Item | Value |
|---|---|
| Intended path | `docs/domains/hydrology/mesonet-soil.md` |
| Upstream doctrine | `docs/governance/ROOT_GOVERNANCE.md` *(NEEDS VERIFICATION)* |
| Ethics / sensitivity anchor | `docs/governance/ETHICS.md` *(NEEDS VERIFICATION)* |
| Adjacent domain parent | `docs/domains/README.md` *(NEEDS VERIFICATION)* |
| Expected downstream consumers | hydrology datasets, time-series services, map surfaces, Focus Mode evidence views *(INFERRED)* |
| Implementation coupling | low at doc level; moderate for ingestion/catalog contracts *(INFERRED)* |

This file is intended to sit as a **domain specification**, not as a runtime contract by itself. Runtime schemas, loaders, and publication manifests should remain separately versioned.

---

## Accepted inputs

This specification is written for the following source classes:

1. **Kansas Mesonet REST CSV responses**
2. **Kansas Mesonet soil moisture table/CSV exports**
3. **Kansas Mesonet evapotranspiration dashboard CSV exports**
4. **Station registry metadata** including station names, activity windows, and coordinates

Accepted observation intervals:

- `5min`
- `hour`
- `day`

Accepted station scopes:

- single station
- comma-separated station list
- network-level pull where source supports it

---

## Exclusions

This document excludes:

- non-Mesonet soil sensor networks
- subsurface modeling pipelines not tied to observed Mesonet inputs
- irrigation recommendation logic as a decision engine
- 3D subsurface visualization standards
- unpublished or private source integrations
- claims of authoritative agronomic thresholds for every crop or soil type

> [!CAUTION]
> Soil moisture values are **observed at stations**, not universally representative of surrounding parcels or fields.  
> KFM publication should not overstate spatial precision beyond what observation density and interpolation method can support.

---

## Directory context

```text
docs/
└── domains/
    ├── README.md                       # NEEDS VERIFICATION
    └── hydrology/
        ├── README.md                   # NEEDS VERIFICATION
        └── mesonet-soil.md             # this file
```

---

## Domain placement

```mermaid
flowchart LR
    A[Public Source: Kansas Mesonet] --> B[Hydrology Domain Spec]
    B --> C[Acquisition / RAW]
    C --> D[Validation / WORK]
    D --> E[Processed Time Series]
    E --> F[Catalog / Provenance]
    F --> G[Published Map + Time Series Surfaces]
```

---

## Source profile

### Source identity

| Field | Value |
|---|---|
| Source name | Kansas Mesonet |
| Steward | Kansas State University / Kansas Mesonet |
| Delivery mode | Public web pages + RESTful CSV services |
| Primary formats | CSV, HTML tables, map images |
| Observation focus | station weather, soil moisture, evapotranspiration |
| Access class | public-source |
| Authority posture | authoritative for its own published observations; not sovereign for parcel-specific field truth |

### Source posture in KFM

Kansas Mesonet should be treated as a **trusted observational source** for station-based soil moisture and ET context, while remaining subordinate to KFM rules for:

- provenance retention
- uncertainty visibility
- spatial generalization
- correction handling
- publication boundaries

### Public source facts

**CONFIRMED source facts:**

- Mesonet exposes a REST page describing CSV access and required query parameters.
- Station observations are requested through `/rest/stationdata/`.
- Required stationdata parameters include station or network, interval, start time, and end time.
- Soil moisture is reported at **5 cm, 10 cm, 20 cm, and 50 cm**.
- Soil moisture page exposes **VWC** and **percent saturation** values, plus **7-day change** fields.
- Evapotranspiration page includes a downloadable CSV surface.

---

## Source variables in scope

### Soil moisture variables

| Mesonet field | Meaning | KFM semantic class | Status |
|---|---|---|---|
| `VWC5CM` | volumetric water content at 5 cm | observed.soil.vwc.5cm | CONFIRMED |
| `VWC10CM` | volumetric water content at 10 cm | observed.soil.vwc.10cm | CONFIRMED |
| `VWC20CM` | volumetric water content at 20 cm | observed.soil.vwc.20cm | CONFIRMED |
| `VWC50CM` | volumetric water content at 50 cm | observed.soil.vwc.50cm | CONFIRMED |
| `PCNTSAT5CM` | percent saturation at 5 cm | observed.soil.pcntsat.5cm | CONFIRMED |
| `PCNTSAT10CM` | percent saturation at 10 cm | observed.soil.pcntsat.10cm | CONFIRMED |
| `PCNTSAT20CM` | percent saturation at 20 cm | observed.soil.pcntsat.20cm | CONFIRMED |
| `PCNTSAT50CM` | percent saturation at 50 cm | observed.soil.pcntsat.50cm | CONFIRMED |
| `DIFF7DAY5CM` | 7-day change at 5 cm | derived.soil.delta7d.5cm | CONFIRMED |
| `DIFF7DAY10CM` | 7-day change at 10 cm | derived.soil.delta7d.10cm | CONFIRMED |
| `DIFF7DAY20CM` | 7-day change at 20 cm | derived.soil.delta7d.20cm | CONFIRMED |
| `DIFF7DAY50CM` | 7-day change at 50 cm | derived.soil.delta7d.50cm | CONFIRMED |

### ET variables

Mesonet exposes an evapotranspiration dashboard and CSV download surface. This document does **not** lock a canonical ET field list until a source pull is verified against current CSV headers.

| Group | KFM stance |
|---|---|
| ET dashboard availability | CONFIRMED |
| CSV availability | CONFIRMED |
| exact ET field registry | NEEDS VERIFICATION |
| KFM ET canonical mapping | PROPOSED |

> [!NOTE]
> ET should be onboarded only after a header-level field capture is committed into an adjacent schema or fixture.  
> Until then, ET references in this document are intentionally conservative.

---

## Units and semantics

| Measure | Expected semantics | Notes |
|---|---|---|
| VWC | unitless fraction (`m3/m3` style interpretation) | preserve source numeric values |
| Percent saturation | percent scale | expected 0–100, but retain source value verbatim before downstream normalization |
| 7-day change | source-defined difference metric | retain sign and source units as published |
| Timestamp | source observation timestamp | preserve exact source timestamp string and normalized UTC form |
| Station name | Mesonet station identifier/name | preserve raw source station token |

### Semantic cautions

- Percent saturation is a **historically contextualized source-derived measure**, not a universal soil physics constant for arbitrary off-station interpretation.
- Shallow sensors respond faster to rainfall; deeper sensors respond more slowly and may remain elevated longer.
- Station values are affected by soil type, cover, placement, and local conditions.

---

## Acquisition pattern

### REST endpoints

| Endpoint | Use | Status |
|---|---|---|
| `/rest/stationdata/` | primary time-series CSV pull | CONFIRMED |
| `/rest/stationnames/` | station registry / coordinates | CONFIRMED |
| `/rest/stationactive/` | activity window by station and interval | CONFIRMED |
| `/rest/mostrecent` | latest ingest timestamp by interval | CONFIRMED |
| `/agriculture/soilmoist/` | soil moisture dashboard/table/download | CONFIRMED |
| `/agriculture/et/` | evapotranspiration dashboard/download | CONFIRMED |

### Required stationdata parameters

| Parameter | Meaning | Example | Status |
|---|---|---|---|
| `stn` | station name or comma-separated list | `Butler,Clay` | CONFIRMED |
| `net` | network selector alternative to `stn` | `KSRE` | CONFIRMED |
| `int` | interval | `day` | CONFIRMED |
| `t_start` | first observation timestamp | `20160101000000` | CONFIRMED |
| `t_end` | last observation timestamp | `20160201000000` | CONFIRMED |
| `vars` | optional variable list | `TEMP2MAVG,PRECIP` | CONFIRMED |

### Example pull patterns

#### Single-station daily pull

```text
https://mesonet.k-state.edu/rest/stationdata/?stn=Manhattan&int=day&t_start=20250101000000&t_end=20250131000000&vars=VWC5CM,VWC10CM,VWC20CM,VWC50CM,PCNTSAT5CM,PCNTSAT10CM,PCNTSAT20CM,PCNTSAT50CM
```

#### Multi-station hourly pull

```text
https://mesonet.k-state.edu/rest/stationdata/?stn=Butler,Clay&int=hour&t_start=20250301000000&t_end=20250307230000&vars=VWC5CM,VWC10CM,VWC20CM,VWC50CM
```

#### Latest ingest discovery

```text
https://mesonet.k-state.edu/rest/mostrecent?int=day
```

### Pull strategy

**PROPOSED KFM strategy:**

1. pull station registry
2. pull station activity windows
3. determine latest safe acquisition watermark
4. ingest observation slices by interval
5. persist raw CSV byte payloads before transformation
6. normalize to canonical records
7. publish only after validation and provenance closure

---

## Ingestion and trust flow

```mermaid
flowchart TD
    S[Source Request] --> R[RAW Capture]
    R --> W[WORK / Validation]
    W --> P[Processed Time Series]
    P --> C[Catalog Registration]
    C --> U[Published Surface]
    U --> E[Evidence Resolution]

    R -.stores.-> R1[Source URL]
    R -.stores.-> R2[Retrieval Timestamp]
    R -.stores.-> R3[Raw CSV Payload]
    P -.binds.-> P1[DatasetVersion]
    U -.shows.-> U1[Observed / Modeled / Stale Flags]
```

### RAW requirements

Each acquisition event should preserve:

- source URL
- query string
- retrieval timestamp
- raw response bytes
- HTTP status or failure class
- content hash
- parser version
- interval and station scope requested

### WORK requirements

Validation should occur before promoting to processed form.

Minimum checks:

- CSV parse success
- required key columns present
- timestamp parse success
- station token present
- variable registry match or controlled drift detection
- numeric coercion result tracking
- duplicate row handling
- missingness summary

### PROCESSED requirements

Processed records should be:

- timestamp-normalized
- station-normalized
- source-field-preserving
- provenance-linked
- safe for downstream filtering without losing source traceability

---

## Canonical record shape

### Core record

```json
{
  "source": {
    "provider": "Kansas Mesonet",
    "endpoint": "/rest/stationdata/",
    "retrieved_at": "2026-04-01T12:00:00Z",
    "content_hash": "sha256:NEEDS_VERIFICATION"
  },
  "station": {
    "source_name": "Manhattan",
    "network": "KSRE",
    "latitude": 39.0,
    "longitude": -96.0
  },
  "observation": {
    "timestamp_source": "2025-03-01 00:00:00",
    "timestamp_utc": "2025-03-01T06:00:00Z",
    "interval": "day"
  },
  "soil": {
    "vwc": {
      "5cm": 0.21,
      "10cm": 0.23,
      "20cm": 0.25,
      "50cm": 0.30
    },
    "pcntsat": {
      "5cm": 55.0,
      "10cm": 60.0,
      "20cm": 65.0,
      "50cm": 70.0
    },
    "delta7d": {
      "5cm": -0.02,
      "10cm": -0.01,
      "20cm": 0.00,
      "50cm": 0.01
    }
  },
  "trust": {
    "observation_class": "observed",
    "staleness": "fresh",
    "gap_filled": false,
    "modeled": false
  },
  "provenance": {
    "dataset_version": "NEEDS VERIFICATION",
    "evidence_ref": "NEEDS VERIFICATION"
  }
}
```

### Field mapping table

| KFM field | Source field | Required | Notes |
|---|---|---|---|
| `station.source_name` | `STATION` or station token | yes | exact source value preserved |
| `observation.timestamp_source` | `TIMESTAMP` | yes | exact source value preserved |
| `soil.vwc.5cm` | `VWC5CM` | no | nullable when absent |
| `soil.vwc.10cm` | `VWC10CM` | no | nullable when absent |
| `soil.vwc.20cm` | `VWC20CM` | no | nullable when absent |
| `soil.vwc.50cm` | `VWC50CM` | no | nullable when absent |
| `soil.pcntsat.5cm` | `PCNTSAT5CM` | no | nullable when absent |
| `soil.pcntsat.10cm` | `PCNTSAT10CM` | no | nullable when absent |
| `soil.pcntsat.20cm` | `PCNTSAT20CM` | no | nullable when absent |
| `soil.pcntsat.50cm` | `PCNTSAT50CM` | no | nullable when absent |
| `soil.delta7d.5cm` | `DIFF7DAY5CM` | no | dashboard-derived field family |
| `soil.delta7d.10cm` | `DIFF7DAY10CM` | no | dashboard-derived field family |
| `soil.delta7d.20cm` | `DIFF7DAY20CM` | no | dashboard-derived field family |
| `soil.delta7d.50cm` | `DIFF7DAY50CM` | no | dashboard-derived field family |

---

## Station registry handling

### Registry fields

**PROPOSED minimum station registry shape:**

| Field | Description |
|---|---|
| `station.source_name` | Mesonet station name |
| `station.network` | network code if present |
| `station.latitude` | source coordinate |
| `station.longitude` | source coordinate |
| `station.active_from` | first observation timestamp by interval |
| `station.active_to` | most recent observation timestamp by interval |
| `station.interval_seconds` | 300 / 3600 / 86400 where supplied |

### Registry rules

- treat station name as source key unless a stronger source identifier is available
- preserve source coordinates without silent reprojection drift
- do not infer station retirement solely from temporary source gaps
- refresh station registry before large backfills or new interval ingestion

---

## Derived metrics

The following metrics are **optional, derived, and subordinate** to source observations.

| Metric | Definition | Status |
|---|---|---|
| root-zone mean VWC | mean of selected deeper depths | PROPOSED |
| shallow-to-deep gradient | compare upper and lower depth moisture | PROPOSED |
| drydown rate | slope over rolling window | PROPOSED |
| recharge pulse flag | positive shift following precipitation event | PROPOSED |
| anomaly score | deviation from local station history | PROPOSED |

> [!WARNING]
> Derived layers must never silently replace station observations as sovereign truth.  
> Published surfaces should always distinguish **observed**, **derived**, and **modeled** products.

---

## Validation and quality rules

### Minimum validation gates

| Gate | Rule | Failure posture |
|---|---|---|
| source response | non-empty CSV payload | hold in RAW, do not promote |
| header integrity | expected key columns present | quarantine pull |
| timestamp parse | all rows parse or are explicitly marked invalid | narrow or hold invalid rows |
| station integrity | station token present per row | hold invalid rows |
| numeric coercion | numeric fields parse or become nullable with error count | continue with warning if below threshold |
| duplicate rows | duplicates detected by station + timestamp + interval | de-duplicate with logged rule |
| schema drift | unseen variables or missing expected variables | mark `NEEDS VERIFICATION` and review |
| staleness | lag exceeds publication threshold | publish only with stale flag or abstain |

### QA notes

- Missing values must not be coerced to `0`.
- Out-of-range values should be flagged, not auto-corrected.
- Source changes in field naming require explicit registry update.
- Station-specific sensor anomalies should be tracked as quality annotations, not silently dropped unless policy requires exclusion.

---

## Publication and trust surface

### Publication classes

| Surface type | Allowed | Conditions |
|---|---|---|
| station time-series | yes | direct provenance retained |
| statewide 2D map | yes | interpolation method disclosed |
| dashboard summary | yes | freshness + uncertainty visible |
| parcel-specific claims | constrained | only with explicit caveats and evidence route |
| 3D subsurface scene | conditional | burden-bearing justification required |

### Trust flags for consumers

Every published surface should support the following trust-facing distinctions where relevant:

| Flag | Meaning |
|---|---|
| `observed` | direct source observation |
| `derived` | computed from source observations |
| `modeled` | model-generated estimate |
| `stale` | source age exceeds freshness window |
| `gap_filled` | missing source values replaced or interpolated |
| `under_review` | quality concern not yet resolved |

### Evidence visibility

Consequential downstream claims should resolve back to:

- source endpoint and query
- retrieval event
- raw payload hash
- parser or transform version
- dataset version
- validation outcome

---

## Spatial handling

### Mapping stance

KFM should default to **station view first**, then carefully derived surfaces.

Recommended spatial products:

- station point layers
- depth-specific statewide interpolated rasters
- generalized moisture condition maps
- station-level change maps over rolling windows

### Spatial cautions

- interpolation method must be documented
- station sparsity must be visible
- do not imply field-level certainty from coarse surfaces
- map legends must distinguish raw observation from inferred surface values

```mermaid
flowchart LR
    A[Station Points] --> B[Optional Interpolation]
    B --> C[Generalized 2D Surface]
    C --> D[Public Map Tile / Focus Surface]

    A --> E[Station Chart View]
    E --> F[Evidence Drawer]
```

---

## Sensitivity and ethics posture

This source is public, but responsible publication still matters.

### Required posture

- preserve source attribution and citation requirements
- avoid overstating agronomic certainty
- make interpolation visible
- prefer generalization when users may mistake station data for parcel truth
- show uncertainty before persuasion
- correct visibly when source or transform issues are found

### Notable non-sensitive posture

This specification does **not** appear to trigger rare-species geoprivacy or archaeological site precision controls.  
Even so, hydrology claims should remain evidence-resolvable and uncertainty-visible.

---

## Usage examples

### Example: pull a daily station slice

```bash
curl "https://mesonet.k-state.edu/rest/stationdata/?stn=Manhattan&int=day&t_start=20250101000000&t_end=20250131000000&vars=VWC5CM,VWC10CM,VWC20CM,VWC50CM,PCNTSAT5CM,PCNTSAT10CM,PCNTSAT20CM,PCNTSAT50CM"
```

### Example: fetch station registry

```bash
curl "https://mesonet.k-state.edu/rest/stationnames/"
```

### Example: fetch latest ingest watermark

```bash
curl "https://mesonet.k-state.edu/rest/mostrecent?int=day"
```

### Example: minimal Python ingestion

```python
from __future__ import annotations

import csv
import io
import requests

URL = "https://mesonet.k-state.edu/rest/stationdata/"

params = {
    "stn": "Manhattan",
    "int": "day",
    "t_start": "20250101000000",
    "t_end": "20250131000000",
    "vars": ",".join([
        "VWC5CM", "VWC10CM", "VWC20CM", "VWC50CM",
        "PCNTSAT5CM", "PCNTSAT10CM", "PCNTSAT20CM", "PCNTSAT50CM",
    ]),
}

response = requests.get(URL, params=params, timeout=60)
response.raise_for_status()

reader = csv.DictReader(io.StringIO(response.text))
rows = list(reader)

print(f"rows={len(rows)}")
print(rows[0] if rows else "no rows")
```

---

## Implementation notes

### Recommended adjacent artifacts

| Artifact | Purpose | Status |
|---|---|---|
| dataset schema | canonical time-series contract | PROPOSED |
| source adapter | Mesonet REST puller | PROPOSED |
| validation profile | range/missingness/schema drift checks | PROPOSED |
| fixture CSVs | parser regression and contract testing | PROPOSED |
| publication manifest | release and trust metadata | PROPOSED |

### Suggested naming

| Concern | Suggested shape |
|---|---|
| source key | `source.mesonet.ksu.soil` |
| dataset key | `hydrology.mesonet.soil_moisture` |
| ET dataset key | `hydrology.mesonet.et` |
| station registry key | `hydrology.mesonet.station_registry` |

> [!NOTE]
> Key names above are recommendations only and should not be treated as in-repo truth until aligned with visible catalog conventions.

---

## Task list

### Definition of done for an initial integration slice

- [ ] Confirm adjacent hydrology directory conventions in-repo
- [ ] Capture current stationdata CSV fixture for at least one station and interval
- [ ] Capture current station registry fixture
- [ ] Verify current ET CSV header set
- [ ] Author canonical schema for soil records
- [ ] Add parser + validation rules
- [ ] Persist RAW payload metadata and content hash
- [ ] Register dataset version and provenance path
- [ ] Publish a station-level chart view with trust flags
- [ ] Document interpolation method before any statewide raster publication

### Merge gates

- [ ] All in-repo references verified
- [ ] No unmarked implementation claims remain
- [ ] Variable registry matches current source
- [ ] Freshness and stale behavior documented
- [ ] Evidence route defined for published claims

---

## FAQ

### Is Mesonet soil moisture authoritative for all Kansas soils?
No. It is authoritative for the network’s published **station observations**, not for every parcel or field in Kansas.

### Why preserve both VWC and percent saturation?
They answer different questions. VWC preserves the direct water-content style measure; percent saturation adds source-defined historical context for “how wet vs. dry” a station-depth condition is.

### Can ET be integrated under this spec today?
Partially. The dashboard and CSV availability are in scope, but the **current ET field registry** still requires a verified header capture before a canonical ET schema is locked.

### Why separate RAW from processed time series?
Because KFM trust depends on being able to resolve downstream claims back to original source payloads, parse rules, and validation outcomes.

### Should KFM publish interpolated statewide soil moisture maps?
Yes, conditionally. They should be clearly marked as generalized surfaces derived from station observations, with method and uncertainty visible.

---

## Appendix A — Truth labels used in this document

| Label | Meaning |
|---|---|
| `CONFIRMED` | directly supported by visible source documentation |
| `INFERRED` | strongly implied by doctrine or source behavior, not directly verified in-repo |
| `PROPOSED` | recommended target shape consistent with KFM posture |
| `UNKNOWN` | no reliable evidence in current session |
| `NEEDS VERIFICATION` | must be checked in repository or against current source before merge |

---

## Appendix B — Source onboarding checklist

| Step | Action |
|---|---|
| 1 | verify source citation and usage requirements |
| 2 | capture sample CSV payloads |
| 3 | record current field headers |
| 4 | define canonical schema |
| 5 | define validation thresholds |
| 6 | preserve RAW payloads and hashes |
| 7 | register dataset and provenance route |
| 8 | expose trust flags in publication surface |

---

## Appendix C — Public-source limitations

- Soil moisture history beyond source-exposed online windows may require separate handling.
- Variable availability may differ by station or interval.
- Header order is not guaranteed by the source.
- Source page dashboards may expose values not yet formalized into the REST variable registry.

---

[Back to top](#top)