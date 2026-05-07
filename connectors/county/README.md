<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: County Connector README
type: standard
version: v1
status: draft
owners: Bartytime
created: 2026-05-07
updated: 2026-05-07
policy_label: restricted
related: []
tags: [kfm, connector, county]
notes: [Draft README for the County connector; structure, integration, and examples PROPOSED pending repository verification.]
[/KFM_META_BLOCK_V2] -->

# County Connector README

_A KFM data connector for ingesting county-scale geospatial and administrative datasets._

---

## Status & Owners
- **Status:** Experimental
- **Owners:** Bartytime
- **Badges:** `TODO` (coverage, build, latest release)

---

## Quick Links
- [Scope](#scope)
- [Repo Fit](#repo-fit)
- [Accepted Inputs](#accepted-inputs)
- [Exclusions](#exclusions)
- [Directory Tree](#directory-tree)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Validation & QA](#validation--qa)
- [Back to Top](#back-to-top)

---

## Scope
- Ingest county-scale public datasets (hydrology, soils, parcels, roads, administrative boundaries).
- Provide RAW → WORK/QUARANTINE → PROCESSED → CATALOG → PUBLISHED lifecycle integration.
- Attach source metadata, rights, sensitivity, and lineage for each layer.

## Repo Fit
- Resides under `connectors/county/` (PROPOSED path).
- Upstream: RAW downloads from USGS, NRCS, state and county GIS portals.
- Downstream: Processed KFM catalog layers, ReleaseManifests, EvidenceBundles.

## Accepted Inputs
- USGS NWIS gage and groundwater data
- NRCS SSURGO soil polygons and attributes
- State and county parcel and assessor feeds
- Road centerlines, address points, and admin boundaries
- County-scale hydrography and imagery footprint indices

## Exclusions
- Non-county-scale datasets
- Proprietary or restricted-use data without explicit license
- Raw data not linked to an EvidenceRef
- Direct ingestion into PUBLIC without policy review

## Directory Tree (PROPOSED)
```
connectors/
└── county/
    ├── README.md
    ├── ingest/
    │   ├── nwis/
    │   ├── ssurgo/
    │   └── parcels/
    ├── preflight/
    │   └── validators/
    ├── processed/
    └── fixtures/
```

## Quickstart
1. Install dependencies: `pip install -r requirements.txt`
2. Configure county sources in `config.yaml`
3. Run ingest: `python ingest/run_county_ingest.py --county FIPS_CODE`
4. Validate preflight: `python preflight/checks.py --layer <layer_name>`
5. Promote to CATALOG after passing QA

## Usage
```bash
# Example ingest for Sedgwick County
python ingest/run_county_ingest.py --county 20177

# Validate geometry, temporal coverage, and licensing
python preflight/checks.py --layer parcels_sedgwick
```

- Attach EvidenceRef metadata for each dataset
- Record spec_hash and source_id for lineage
- Apply rights and sensitivity policies per domain (e.g., ownership restricted, rare species generalized)

## Validation & QA
- Geometry checks: validity, CRS, extent
- Time coverage: observed_at / effective_on / effective_through populated
- License & rights verified
- Stable IDs present (APN, site_no, MUKEY)
- Attribute QA: required fields non-null, domain consistency
- Provenance recorded with source_ref and transform_ops
- Fail-closed on missing, invalid, or sensitive fields

## Back to Top
