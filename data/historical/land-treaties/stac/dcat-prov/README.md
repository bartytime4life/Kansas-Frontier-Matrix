---
title: "🛰 KFM — Land Treaties DCAT & PROV Overlay"
path: "data/historical/land-treaties/stac/dcat-prov/README.md"
version: "v11.2.2"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Data Catalog Overlay"
intent: "dcat-prov-governance"
semantic_document_id: "kfm-stac-land-treaties-dcat-prov-v11.2.2"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/module-default-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Enforced"
sensitivity: "High (Indigenous data — masked/generalized)"
public_exposure_risk: "Medium"
classification: "Public With Safeguards"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Supersedes prior land-treaties DCAT/PROV overlays"
immutability_status: "version-pinned"
ai_training_inclusion: false

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 DCAT Dataset & Catalog Graphs"
    - "🧩 PROV-O Bundles & Lineage"
    - "🧭 Linkage to STAC & Neo4j"
    - "🧪 Validation, CI & Rollback"
    - "🧬 Version History"
    - "⚖️ Footer"

provenance_chain:
  - "data/historical/land-treaties/stac/README.md@v11.2.2"
  - "data/historical/land-treaties/stac/collections/README.md@v11.2.2"
  - "docs/data/historical/land-treaties/README.md@v11.2.2"
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

doc_uuid: "urn:kfm:stac:land-treaties:dcat-prov:v11.2.2"
event_source_id: "stac:kfm:land-treaties:dcat-prov:v11.2.2"
---

<div align="center">

# 🛰 **KFM — Land Treaties DCAT & PROV Overlay**  
`data/historical/land-treaties/stac/dcat-prov/`

**Role in the pipeline**  
Deterministic ETL → STAC Collections & Items → **DCAT/PROV overlays** → Neo4j → API → MapLibre/Cesium → Story Nodes → Focus Mode

</div>

---

## 📘 Overview

This submodule defines the **DCAT and PROV‑O overlays** for the Land Treaties STAC catalog. It does *not* introduce new data; it provides:

- DCAT 3.0–compatible **Dataset/Catalog graphs** wrapping STAC Collections & exports.  
- PROV‑O **lineage bundles** documenting ETL runs, sources, and agents.  
- Stable RDF identifiers that APIs, Story Nodes, and Focus Mode can use to reason over treaty data.

It is scoped to:

- `data/historical/land-treaties/stac/dcat-prov/`  

and inherits all constraints from:

- `data/historical/land-treaties/stac/README.md` (STAC root)  
- `data/historical/land-treaties/stac/collections/README.md` (Collections guide)  
- `docs/data/historical/land-treaties/README.md` (module root)  

---

## 🗂️ Directory Layout

Emoji layout (📂 = directory, 📄 = file). Names on disk remain ASCII.

~~~text
📂 data/
└─ 📂 historical/
   └─ 📂 land-treaties/
      └─ 📂 stac/
         └─ 📂 dcat-prov/
            ├─ 📄 README.md                    # This file
            ├─ 📄 land-treaties-dataset.ttl    # DCAT 3.0 Dataset/Distribution graph
            ├─ 📄 land-treaties-catalog.ttl    # DCAT Catalog wrapper
            └─ 📄 land-treaties-provenance.jsonld  # PROV-O bundle (per release)
~~~

Adding new DCAT/PROV files here **requires** updating this README, plus the STAC root README and validation configs.

---

## 📦 DCAT Dataset & Catalog Graphs

Two Turtle files are normative:

- `land-treaties-dataset.ttl` — **DCAT 3.0 Dataset graph** for treaty data.  
- `land-treaties-catalog.ttl` — **DCAT Catalog** that wraps the Dataset and links into the global KFM catalog.

### 3.1 DCAT Dataset Pattern (`land-treaties-dataset.ttl`)

Conceptual structure (Turtle):

~~~turtle
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix prov:  <http://www.w3.org/ns/prov#> .
@prefix kfm:   <https://kfm.land/ns#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

<https://kfm.land/dataset/land-treaties>
    a dcat:Dataset ;
    dct:title "Kansas Frontier Matrix — Land Treaties Dataset" ;
    dct:description "Generalized treaty geometries, timelines, and document references for Kansas-related land treaties (ca. 1850–1890)." ;
    dct:identifier "kfm-ds-land-treaties-v11.2.2" ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    dct:publisher <https://kfm.land/org/kfm-faircare-council> ;
    dct:spatial <https://kfm.land/place/kansas-region> ;
    dct:temporal [
        a dct:PeriodOfTime ;
        dcat:startDate "1850-01-01"^^xsd:date ;
        dcat:endDate   "1890-12-31"^^xsd:date
    ] ;
    dcat:distribution
        <https://kfm.land/dist/land-treaties-stac-collections>,
        <https://kfm.land/dist/land-treaties-geojson>,
        <https://kfm.land/dist/land-treaties-archive> ;
    prov:wasDerivedFrom <https://kfm.land/source/historical/land-treaties-manifests> ;
    kfm:datasetVersion "v11.2.2" .
~~~

**Rules:**

- One **primary Dataset URI** per module (e.g., `.../dataset/land-treaties`).  
- Each major export bundle (STAC snapshot, GeoJSON, zipped archive) is a `dcat:Distribution`.  
- Sovereignty constraints (masking/generalization) MUST be described in `dct:description` and/or custom `kfm:` properties.

### 3.2 DCAT Catalog Pattern (`land-treaties-catalog.ttl`)

Conceptual structure:

~~~turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .

<https://kfm.land/catalog/land-treaties>
    a dcat:Catalog ;
    dct:title "Kansas Frontier Matrix — Land Treaties Catalog" ;
    dct:description "Catalog of treaty-related datasets and distributions for KFM." ;
    dcat:dataset <https://kfm.land/dataset/land-treaties> ;
    dcat:record  <https://kfm.land/catalog-record/land-treaties-v11.2.2> ;
    dct:isPartOf <https://kfm.land/catalog/kfm-root> .
~~~

Catalog graphs MUST link upward into the **global KFM DCAT catalog** and be reachable from it.

---

## 🧩 PROV-O Bundles & Lineage

`land-treaties-provenance.jsonld` encodes the **lineage** of each release:

- What ETL jobs ran.  
- What sources they used.  
- What STAC/DCAT entities they generated.  
- Which agents were responsible.

### 4.1 Minimal Bundle Pattern

Conceptual JSON‑LD snippet:

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "kfm": "https://kfm.land/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "https://kfm.land/prov/land-treaties/v11.2.2",
  "@type": "prov:Bundle",
  "prov:entity": {
    "kfm:stacCollectionTreaties": {
      "@id": "https://kfm.land/stac/collections/treaties-kansas-v1",
      "@type": "prov:Entity",
      "kfm:datasetVersion": "v11.2.2"
    },
    "kfm:dcatDatasetLandTreaties": {
      "@id": "https://kfm.land/dataset/land-treaties",
      "@type": ["prov:Entity", "dcat:Dataset"]
    }
  },
  "prov:activity": {
    "kfm:etlRunLandTreatiesV11_2_2": {
      "@id": "urn:kfm:etl:land-treaties:v11.2.2:run-<run-id>",
      "@type": "prov:Activity",
      "prov:startedAtTime": { "@value": "2025-11-29T02:14:05Z", "@type": "xsd:dateTime" },
      "prov:endedAtTime":   { "@value": "2025-11-29T02:22:41Z", "@type": "xsd:dateTime" }
    }
  },
  "prov:agent": {
    "kfm:etlAgent": {
      "@id": "https://kfm.land/agent/etl/land-treaties",
      "@type": "prov:SoftwareAgent",
      "kfm:version": "11.2.2"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "prov:entity": "https://kfm.land/dataset/land-treaties",
      "prov:activity": "urn:kfm:etl:land-treaties:v11.2.2:run-<run-id>"
    }
  ],
  "prov:wasAssociatedWith": [
    {
      "prov:activity": "urn:kfm:etl:land-treaties:v11.2.2:run-<run-id>",
      "prov:agent": "https://kfm.land/agent/etl/land-treaties"
    }
  ]
}

