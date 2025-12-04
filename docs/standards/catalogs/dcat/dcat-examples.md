---
title: "📘 KFM v11.2.3 — DCAT Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Concrete DCAT JSON-LD and Turtle examples derived from STAC Items and Collections under the KFM STAC-first → DCAT-derived model."
path: "docs/standards/catalogs/dcat/dcat-examples.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "DCAT 2.x / 3.0 profile-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-dcat-examples-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-dcat-examples-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:dcat:examples:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Standards Examples"
intent: "catalogs-dcat-examples"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/catalogs-dcat-examples-v1.json"
shape_schema_ref: "../../schemas/shacl/catalogs-dcat-examples-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major DCAT examples revision"
---

<div align="center">

# 📘 Kansas Frontier Matrix — DCAT Examples  
`docs/standards/catalogs/dcat/dcat-examples.md`

**Purpose:**  
Provide **concrete, end-to-end examples** of **DCAT JSON-LD and Turtle** derived from KFM STAC Items and Collections, demonstrating the **STAC-first → DCAT-derived** model and the KFM DCAT profile.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

This document is **illustrative** (not normative). It must be read alongside:

- `dcat-kfm-profile.md` — KFM DCAT profile (normative).  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived standard.  
- `../crosswalks/stac-dcat-crosswalk.md` — field-level STAC → DCAT mappings.  
- `../stac/stac-kfm-profile.md` — KFM STAC profile.

Key goals:

- Show **realistic, simplified DCAT outputs** derived from STAC.  
- Demonstrate how **assets** become `dcat:Distribution`s.  
- Show how FAIR+CARE and governance metadata influence DCAT fields.

---

## 🛰️ 2. Example 1 — Imagery STAC Item → DCAT Dataset

### 2.1 Source STAC Item (Simplified)

This STAC Item conforms to the KFM STAC profile and `kfm-core` extension.

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "naip_2023_tile_001",
  "geometry": { "...": "..." },
  "bbox": [-98.0, 38.1, -97.9, 38.2],
  "properties": {
    "datetime": "2023-07-11T18:22:00Z",
    "title": "NAIP 2023 Tile 001",
    "description": "NAIP 2023 imagery tile over central Kansas.",
    "kfm:dataset_id": "urn:kfm:dataset:naip-ks-2023",
    "kfm:domain": "imagery",
    "kfm:release_stage": "stable"
  },
  "assets": {
    "image": {
      "href": "https://example.com/naip_001.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"],
      "checksum:sha256": "abc123..."
    },
    "thumbnail": {
      "href": "https://example.com/naip_001.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://catalog.kfm.dev/stac/naip_2023_tile_001.json"
    },
    {
      "rel": "collection",
      "href": "https://catalog.kfm.dev/stac/collections/naip_ks_2023.json"
    }
  ]
}
~~~

### 2.2 Derived DCAT JSON-LD (Dataset + Distributions)

~~~json
{
  "@context": [
    "https://www.w3.org/ns/dcat.jsonld",
    {
      "spdx": "http://spdx.org/rdf/terms#"
    }
  ],
  "@id": "urn:kfm:dataset:naip-ks-2023:naip_2023_tile_001",
  "@type": "dcat:Dataset",
  "dct:identifier": "naip_2023_tile_001",
  "dct:title": "NAIP 2023 Tile 001",
  "dct:description": "NAIP 2023 imagery tile over central Kansas.",
  "dct:spatial": {
    "@type": "dct:Location",
    "bbox": [-98.0, 38.1, -97.9, 38.2]
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2023-07-11T18:22:00Z",
    "dcat:endDate": "2023-07-11T18:22:00Z"
  },
  "dct:publisher": {
    "@type": "foaf:Agent",
    "foaf:name": "Kansas Frontier Matrix"
  },
  "dcat:landingPage": "https://catalog.kfm.dev/datasets/naip_2023_tile_001",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "NAIP 2023 Tile 001 (GeoTIFF)",
      "dcat:downloadURL": "https://example.com/naip_001.tif",
      "dct:format": "image/tiff; application=geotiff",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "sha256",
        "spdx:checksumValue": "abc123..."
      }
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "NAIP 2023 Tile 001 (Thumbnail PNG)",
      "dcat:downloadURL": "https://example.com/naip_001.png",
      "dct:format": "image/png"
    }
  ]
}
~~~

### 2.3 Equivalent DCAT Turtle

~~~turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .

<urn:kfm:dataset:naip-ks-2023:naip_2023_tile_001>
  a dcat:Dataset ;
  dct:identifier "naip_2023_tile_001" ;
  dct:title "NAIP 2023 Tile 001" ;
  dct:description "NAIP 2023 imagery tile over central Kansas." ;
  dct:spatial [
    a dct:Location ;
    dcat:bbox "-98.0,38.1,-97.9,38.2"
  ] ;
  dct:temporal [
    a dct:PeriodOfTime ;
    dcat:startDate "2023-07-11T18:22:00Z" ;
    dcat:endDate   "2023-07-11T18:22:00Z"
  ] ;
  dct:publisher [
    a foaf:Agent ;
    foaf:name "Kansas Frontier Matrix"
  ] ;
  dcat:landingPage <https://catalog.kfm.dev/datasets/naip_2023_tile_001> ;
  dcat:distribution
    [
      a dcat:Distribution ;
      dct:title "NAIP 2023 Tile 001 (GeoTIFF)" ;
      dcat:downloadURL <https://example.com/naip_001.tif> ;
      dct:format "image/tiff; application=geotiff" ;
      spdx:checksum [
        a spdx:Checksum ;
        spdx:algorithm spdx:checksumAlgorithm_sha256 ;
        spdx:checksumValue "abc123..."
      ]
    ] ,
    [
      a dcat:Distribution ;
      dct:title "NAIP 2023 Tile 001 (Thumbnail PNG)" ;
      dcat:downloadURL <https://example.com/naip_001.png> ;
      dct:format "image/png"
    ] .
~~~

---

## 🌦️ 3. Example 2 — Climate Tile Collection → DCAT Dataset

### 3.1 Source STAC Collection (Simplified)

~~~json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "hrrr_precip_ks_3km",
  "description": "HRRR precipitation accumulation over Kansas at 3 km resolution.",
  "extent": {
    "spatial": {
      "bbox": [[-102.0, 36.99, -94.6, 40.01]]
    },
    "temporal": {
      "interval": [["2025-05-01T00:00:00Z", null]]
    }
  },
  "license": "CC-BY-4.0",
  "keywords": ["precipitation", "HRRR", "Kansas", "climate"],
  "providers": [
    {
      "name": "NOAA",
      "roles": ["producer"],
      "url": "https://www.noaa.gov/"
    },
    {
      "name": "Kansas Frontier Matrix",
      "roles": ["processor", "host"],
      "url": "https://kfm.dev/"
    }
  ],
  "links": [
    {
      "rel": "self",
      "href": "https://catalog.kfm.dev/stac/collections/hrrr_precip_ks_3km.json"
    }
  ]
}
~~~

### 3.2 Derived DCAT JSON-LD Dataset

~~~json
{
  "@context": "https://www.w3.org/ns/dcat.jsonld",
  "@id": "urn:kfm:dataset:hrrr_precip_ks_3km",
  "@type": "dcat:Dataset",
  "dct:identifier": "hrrr_precip_ks_3km",
  "dct:title": "HRRR Precipitation, Kansas, 3 km",
  "dct:description": "HRRR precipitation accumulation over Kansas at 3 km resolution.",
  "dct:spatial": {
    "@type": "dct:Location",
    "bbox": [-102.0, 36.99, -94.6, 40.01]
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2025-05-01T00:00:00Z",
    "dcat:endDate": null
  },
  "dct:license": "CC-BY-4.0",
  "dcat:keyword": ["precipitation", "HRRR", "Kansas", "climate"],
  "dct:publisher": {
    "@type": "foaf:Agent",
    "foaf:name": "NOAA"
  },
  "dct:creator": [
    {
      "@type": "foaf:Agent",
      "foaf:name": "NOAA"
    },
    {
      "@type": "foaf:Agent",
      "foaf:name": "Kansas Frontier Matrix"
    }
  ],
  "dcat:landingPage": "https://catalog.kfm.dev/datasets/hrrr_precip_ks_3km",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "HRRR Precipitation, Kansas, 3 km (Zarr)",
      "dcat:accessURL": "https://data.kfm.dev/hrrr/precip/ks_3km/catalog.json",
      "dct:format": "application/x-zarr"
    }
  ]
}
~~~

---

## 🌊 4. Example 3 — Hydrology Gauge Dataset (FAIR+CARE-Aware)

### 4.1 Source STAC Item (Hydrology-Oriented, Simplified)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "usgs_06887500_daily_2025-06-01",
  "geometry": { "type": "Point", "coordinates": [-97.345, 37.896] },
  "bbox": [-97.345, 37.896, -97.345, 37.896],
  "properties": {
    "datetime": "2025-06-01T12:00:00Z",
    "kfm:dataset_id": "urn:kfm:dataset:ks-river-gauges-daily-v1",
    "kfm:domain": "hydrology",
    "kfm:region_slug": "arkansas-river-basin",
    "kfm:release_stage": "stable",
    "kfmfc:sensitivity": "general",
    "kfmfc:care_label": "Public",
    "kfmfc:sovereignty_flag": false,
    "kfmhydro:watershed_id": "huc8-11030001",
    "kfmhydro:river_id": "arkansas-river-mainstem",
    "kfmhydro:gauge_kind": "usgs-gage",
    "kfmhydro:variable": "discharge",
    "kfmhydro:units": "ft3/s",
    "kfmhydro:time_aggregation": "daily-mean"
  },
  "assets": {
    "timeseries": {
      "href": "https://data.kfm.dev/hydro/usgs/daily/06887500_2025-06-01.parquet",
      "type": "application/x-parquet",
      "roles": ["data"],
      "checksum:sha256": "def456..."
    }
  }
}
~~~

### 4.2 Derived DCAT JSON-LD Dataset (Public-Safe)

~~~json
{
  "@context": [
    "https://www.w3.org/ns/dcat.jsonld",
    {
      "spdx": "http://spdx.org/rdf/terms#"
    }
  ],
  "@id": "urn:kfm:dataset:ks-river-gauges-daily-v1:usgs_06887500_daily_2025-06-01",
  "@type": "dcat:Dataset",
  "dct:identifier": "usgs_06887500_daily_2025-06-01",
  "dct:title": "Daily Mean Discharge — Arkansas River Gauge (Kansas)",
  "dct:description": "Daily mean streamflow at a mainstem Arkansas River gauge in Kansas.",
  "dct:spatial": {
    "@type": "dct:Location",
    "bbox": [-97.345, 37.896, -97.345, 37.896]
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2025-06-01T00:00:00Z",
    "dcat:endDate": "2025-06-01T23:59:59Z"
  },
  "dcat:keyword": [
    "streamflow",
    "discharge",
    "Arkansas River",
    "hydrology",
    "Kansas"
  ],
  "dct:publisher": {
    "@type": "foaf:Agent",
    "foaf:name": "Kansas Frontier Matrix"
  },
  "dcat:landingPage": "https://catalog.kfm.dev/datasets/ks-river-gauges-daily-v1",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "Daily Mean Discharge Time Series (Parquet)",
      "dcat:downloadURL": "https://data.kfm.dev/hydro/usgs/daily/06887500_2025-06-01.parquet",
      "dct:format": "application/x-parquet",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "sha256",
        "spdx:checksumValue": "def456..."
      }
    }
  ]
}
~~~

> **FAIR+CARE note:**  
> Because `kfmfc:sensitivity = "general"` and `kfmfc:care_label = "Public"`, this DCAT record can appear in public catalogs. For more sensitive cases, crosswalk logic would either omit certain datasets or generalize them further.

---

## 🧪 5. Validation & CI Expectations for Examples

Even example DCAT artifacts used in tests and docs should:

- **Validate** against the KFM DCAT profile and SHACL shapes.  
- Be **internally consistent** with the STAC examples they derive from.  
- Avoid embedding any **real sensitive identifiers** unless:
  - They are already public (e.g., public USGS gauge IDs), and  
  - Governance has approved their use.

CI workflows may:

- Use these examples as **fixtures** for:
  - Unit tests of the STAC → DCAT crosswalk code.  
  - Validation tests for the KFM DCAT profile.

---

## ✅ 6. Implementation Notes

When implementing DCAT derivation in KFM:

- Use examples here as **templates** for:
  - JSON-LD structure and `@context` usage.  
  - How to populate spatial/temporal extents.  
  - How to model distributions and checksums.

- Always refer back to:
  - `dcat-kfm-profile.md` for normative requirements.  
  - `stac-dcat-derivation.md` for architectural constraints.  
  - `stac-dcat-crosswalk.md` for up-to-date mappings.

---

## 🕰️ 7. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial DCAT examples document; added imagery, climate, and hydrology DCAT JSON-LD/Turtle examples derived from STAC in line with KFM DCAT profile and STAC-first → DCAT-derived standard. |


