---
title: "🗺️ Kansas Frontier Matrix — STAC ↔ DCAT 3.0 Translation Layer Design Spec (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/metadata_bridge/README.md"
version: "v9.5.0"
last_updated: "2025-10-30"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v9.5.0/sbom.spdx.json"
manifest_ref: "releases/v9.5.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/metadata-bridge-v1.json"
json_export: "releases/v9.5.0/metadata-bridge.meta.json"
validation_reports:
  - "reports/self-validation/stac-dcat-roundtrip.json"
  - "reports/shacl-validation/dcat-shapes-report.json"
  - "reports/audit/metadata-bridge-provenance.json"
governance_ref: "docs/standards/governance-ledger.md"
license: "MIT"
---

<div align="center">

# 🗺️ Kansas Frontier Matrix — **STAC ↔ DCAT 3.0 Translation Layer**
_“Bridging geospatial FAIR metadata between JSON and RDF worlds.”_

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)  
[![Build · Bridge CI](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/bridge-e2e.yml?label=Bridge%20CI)](../../../../.github/workflows/bridge-e2e.yml)  
[![STAC 1.0.0](https://img.shields.io/badge/STAC-1.0.0-orange)](https://stacspec.org)  
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0-purple)](https://www.w3.org/TR/vocab-dcat-3/)

</div>

---

## 🧭 Overview

The **STAC ↔ DCAT 3.0 Translation Layer** enables **bidirectional semantic interoperability** between STAC (SpatioTemporal Asset Catalog) JSON metadata and W3C DCAT 3.0 RDF graphs. It powers KFM’s governance and knowledge-graph ingestion, ensuring **FAIR+CARE** alignment and **machine-readable provenance**.

- STAC → DCAT (JSON → RDF/Turtle/JSON-LD) for **CIDOC CRM + OWL-Time** knowledge graph ingestion.  
- DCAT → STAC (RDF → JSON) for **FAIR catalog publication**.  
- Validation via **JSON Schema**, **SHACL**, and **FAIR+CARE audits**.  
- Designed for **autonomous pipelines** with **deterministic round-trip tests**.

---

## 🗂️ Directory Layout

```plaintext
src/pipelines/metadata_bridge/
├── README.md
├── bridge.py
├── stac_to_dcat.py
├── dcat_to_stac.py
├── __init__.py
├── profiles/
│   ├── base_profile.py
│   ├── dcat_ap_profile.py
│   ├── geodcat_profile.py
│   └── __init__.py
├── schemas/
│   ├── stac/
│   │   └── collection-schema.json
│   └── dcat/
│       └── dcat-shapes.ttl
├── cli.py
└── tests/
    ├── test_stac_to_dcat.py
    ├── test_dcat_to_stac.py
    ├── test_roundtrip.py
    └── fixtures/
        ├── stac_collection.json
        ├── dcat_dataset.ttl
        └── expected_roundtrip.json
```

---

## 🔎 STAC ↔ DCAT Mapping Reference

| STAC Field | DCAT / Related Property | Notes / Transformation |
|---|---|---|
| `id` | `dcterms:identifier` | Preserve global ID |
| `title` | `dcterms:title` | 1:1 |
| `description` | `dcterms:description` | 1:1 |
| `license` | `dcterms:license` | Map SPDX → canonical URI |
| `keywords[]` | `dcat:keyword` | Array flatten |
| `providers[*].name` | `dcterms:publisher` | First provider as primary |
| `extent.spatial.bbox` | `dcterms:spatial` | GeoJSON → WKT polygon |
| `extent.temporal.interval` | `dcterms:temporal` + `time:Interval` | Start/End instants |
| `assets[*].href` | `dcat:accessURL` / `dcat:downloadURL` | Role/MIME-aware |
| `assets[*].type` | `dcterms:format` | Prefer IANA MIME |
| `assets[*].roles` | `dcat:mediaType` | If available |
| `stac_extensions[]` | `owl:imports` | Link to schema IRI |
| `created` / `updated` | `prov:generatedAtTime` | Governance alignment |

---

## 🧠 Example — STAC → DCAT (JSON-LD/Turtle)

**Input — `collection.json`**

```json
{
  "stac_version": "1.0.0",
  "id": "kfm-climate-2020",
  "type": "Collection",
  "title": "Kansas Climate Observations 2020",
  "description": "Climate data from NOAA and USGS sources.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.62, 40.00]] },
    "temporal": { "interval": [["2020-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]] }
  },
  "links": [],
  "providers": [{"name": "NOAA", "roles": ["producer"]}]
}
```

**Output — `dataset.ttl` (excerpt)**

```turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

<https://data.kfm.org/dataset/kfm-climate-2020> a dcat:Dataset ;
  dct:identifier "kfm-climate-2020" ;
  dct:title "Kansas Climate Observations 2020" ;
  dct:description "Climate data from NOAA and USGS sources." ;
  dct:license <https://creativecommons.org/licenses/by/4.0/> ;
  dct:publisher "NOAA" ;
  dct:spatial "POLYGON((-102.05 36.99, -102.05 40.00, -94.62 40.00, -94.62 36.99, -102.05 36.99))" ;
  dct:temporal [ a time:Interval ;
    time:hasBeginning [ time:inXSDDateTime "2020-01-01T00:00:00Z"^^xsd:dateTime ] ;
    time:hasEnd      [ time:inXSDDateTime "2020-12-31T23:59:59Z"^^xsd:dateTime ] ] ;
  prov:generatedAtTime "2025-10-30T00:00:00Z"^^xsd:dateTime .
```

---

## 🔁 Example — DCAT → STAC Reconstruction

**Input — `dataset.ttl`** → **Output — `collection.json`** (excerpt)

```json
{
  "stac_version": "1.0.0",
  "id": "kfm-climate-2020",
  "type": "Collection",
  "title": "Kansas Climate Observations 2020",
  "description": "Climate data from NOAA and USGS sources.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.62, 40.00]] },
    "temporal": { "interval": [["2020-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]] }
  },
  "providers": [{"name": "NOAA", "roles": ["publisher"]}]
}
```

---

## 🛠️ CLI & Pipeline Usage

```bash
# Convert STAC → DCAT
python cli.py convert --from stac --to dcat data/stac/climate/collection.json --out data/dcat/climate.ttl

# Convert DCAT → STAC
python cli.py convert --from dcat --to stac data/dcat/climate.ttl --out data/stac/climate.json

# Validate both forms
python cli.py validate --type stac data/stac/climate.json
python cli.py validate --type dcat data/dcat/climate.ttl
```

---

## 🧪 Validation Workflows (GitHub Actions)

| Workflow | Purpose | Validation |
|---|---|---|
| `stac-validate.yml` | JSON Schema conformance | STAC 1.0 validator |
| `dcat-shacl.yml` | RDF graph validation | SHACL shapes |
| `bridge-e2e.yml` | Bidirectional tests | Round-trip regression |
| `governance-ledger.yml` | Provenance + FAIR+CARE | Governance sync |

---

## 🧱 Integration Diagram

```mermaid
flowchart TD
  A["STAC Collection / Item (JSON)"] --> B["STAC → DCAT Translator (stac_to_dcat.py)"]
  B --> C["RDF Graph (TTL / JSON-LD)"]
  C --> D["CIDOC CRM / OWL-Time Knowledge Graph (Neo4j)"]
  D --> E["Governance Ledger + FAIR+CARE Validation"]
  E --> F["DCAT → STAC Translator (dcat_to_stac.py)"]
  F --> G["Published FAIR Catalog (JSON)"]
```

---

## 🔐 Provenance & FAIR Alignment

- **Provenance:** PROV-O + governance-ledger workflows.  
- **Identifiers:** `https://data.kfm.org/dataset/{id}` URIs.  
- **Temporal Extents:** ISO-8601; OWL-Time intervals.  
- **FAIR+CARE Checks:** Executed in CI/CD (`faircare-validate.yml`).  

---

## 🧩 Implementation Notes

- Python **3.11+**; libs: `rdflib`, `pyshacl`, `jsonschema`.  
- Modular profiles: **GeoDCAT-AP**, **DCAT-AP 3.0** under `profiles/`.  
- YAML-driven config; fixtures + **pytest** round-trip tests.  

---

## 🗺️ Governance & References

| Attribute | Reference |
|---|---|
| Governance Ledger | `docs/standards/governance-ledger.md` |
| FAIR/CARE Protocol | `docs/standards/faircare-protocol.md` |
| Security Policy | `SECURITY.md` |
| Provenance Spec | `docs/standards/provenance-spec.md` |
| Workflow Specs | `.github/workflows/*.yml` |

---

## 🧪 Example Bridge Schema Registration

**`schemas/bridge-schema.json`**

```json
{
  "$schema": "http://json-schema.org/draft/2020-12/schema",
  "title": "KFM STAC ↔ DCAT Bridge Schema",
  "description": "Defines the translation bridge between STAC and DCAT metadata structures.",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "direction": { "enum": ["stac_to_dcat", "dcat_to_stac"] },
    "source": { "type": "string" },
    "target": { "type": "string" },
    "status": { "enum": ["pending", "validated", "failed"] }
  },
  "required": ["id", "direction", "source", "target"]
}
```

---

## ✅ Example SHACL Shape for DCAT Validation

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

dcat:DatasetShape a sh:NodeShape ;
  sh:targetClass dcat:Dataset ;
  sh:property [
    sh:path dct:title ;
    sh:datatype xsd:string ;
    sh:minCount 1
  ] ;
  sh:property [
    sh:path dct:identifier ;
    sh:minCount 1
  ] ;
  sh:property [
    sh:path dct:license ;
    sh:minCount 1
  ] .
```

---

## 🔁 Example Round-Trip Test

**`tests/test_roundtrip.py`**

```python
import json
from stac_to_dcat import convert as to_dcat
from dcat_to_stac import convert as to_stac

def test_roundtrip_equivalence():
    stac = json.load(open("tests/fixtures/stac_collection.json"))
    ttl  = to_dcat(stac)
    back = to_stac(ttl)
    assert stac["id"] == back["id"]
    assert stac["title"] == back["title"]
```

---

## 🧭 Next Steps

1. Extend mappings for **eo**, **sat**, **proj**, **raster** extensions.  
2. Add FAIR+CARE score hooks to governance ledger.  
3. Enable PROV-O/SLSA-based **dataset versioning**.  
4. Enrich metadata via AI extraction pipelines.  
5. Register outputs to **Neo4j (CIDOC CRM)** knowledge graph.

---

## 🧾 Version Notes

| Version | Date | Author | Highlights |
|---|---|---|---|
| v9.5.0 | 2025-10-30 | @kfm-architecture | Initial design spec refresh; CI hooks; SHACL profiles; round-trip tests. |

---

<div align="center">

**Kansas Frontier Matrix** · *FAIR + CARE × MCP-DL v6.3 × STAC 1.0 × DCAT 3.0*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance-ledger.md)

</div>
