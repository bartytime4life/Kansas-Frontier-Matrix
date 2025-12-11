---
title: "🛰 Kansas Frontier Matrix — Land Treaties STAC Catalog"
path: "data/historical/land-treaties/stac/README.md"
version: "v11.2.2"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Data Catalog Submodule"
intent: "stac-catalog-governance"
semantic_document_id: "kfm-stac-land-treaties-v11.2.2"

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

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/module-default-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Enforced"
sensitivity: "High (Indigenous data — masked/generalized)"
public_exposure_risk: "Medium"
classification: "Public With Safeguards"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Supersedes prior land-treaties STAC layouts (if any)"
immutability_status: "version-pinned"
ai_training_inclusion: false

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 Collections & Item Scope"
    - "🧩 Item & Asset Schema (Treaty Layer)"
    - "🧭 Identifiers, Links & DCAT/PROV"
    - "🧪 Validation, CI & Rollback"
    - "🧠 Graph, Story Nodes & Focus Mode"
    - "🧬 Version History"
    - "⚖️ Footer"

provenance_chain:
  - "docs/data/historical/land-treaties/README.md@v11.2.2"
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

doc_uuid: "urn:kfm:stac:land-treaties:v11.2.2"
event_source_id: "stac:kfm:land-treaties:v11.2.2"
---

# 🛰 Kansas Frontier Matrix — Land Treaties STAC Catalog  
`data/historical/land-treaties/stac/`

This submodule defines the **canonical STAC layout** for land‑treaty data in Kansas Frontier Matrix, bridging deterministic ETL outputs into a governed, queryable catalog aligned with the KFM map/timeline and knowledge‑graph stack.

It follows the core KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

---

## 📘 Overview

The **Land Treaties STAC Catalog** is the on‑disk index of:

- Treaty **boundary geometries** (ceded lands, reservations, generalized sensitive extents)  
- Treaty **event timelines** (negotiation, signing, ratification windows)  
- Linked **document assets** (scans, transcripts, summaries)  
- **Metadata** suitable for ingestion into DCAT, PROV‑O and the KFM Neo4j graph  

Design goals:

- Use **STAC 1.x** for all spatiotemporal treaty assets.  
- Provide a **DCAT 3.0–compatible** view for higher‑level datasets.  
- Attach **PROV‑O** lineage for each Collection/Item and asset transformation.  
- Enforce **FAIR+CARE** and **Indigenous data sovereignty** (mask or generalize as required).  

Scope: ca. **1850–1890** treaty activity affecting present‑day Kansas, plus earlier/later treaties whose boundaries overlap the region.

---

## 🗂️ Directory Layout

Emoji layout (📂 = directory, 📄 = file). This is normative for this STAC submodule.

~~~text
📂 data/
└─ 📂 historical/
   └─ 📂 land-treaties/
      └─ 📂 stac/
         ├─ 📄 README.md                       # This file (STAC submodule contract)
         ├─ 📄 catalog.json                    # Root STAC Catalog for land-treaties
         ├─ 📂 collections/                    # STAC Collections (dataset-level)
         │  ├─ 📄 treaties-kansas-v1.collection.json
         │  ├─ 📄 treaties-kansas-scans-v1.collection.json
         │  └─ 📄 treaties-kansas-derived-v1.collection.json
         ├─ 📂 items/                          # STAC Items (asset-level)
         │  ├─ 📂 treaties-kansas-v1/
         │  │  ├─ 📄 treaty-medicine-lodge-1867.item.json
         │  │  ├─ 📄 treaty-XXXX-YYYY.item.json
         │  │  └─ 📄 ...
         │  ├─ 📂 treaties-kansas-scans-v1/
         │  │  └─ 📄 treaty-*-scan-*.item.json
         │  └─ 📂 treaties-kansas-derived-v1/
         │     └─ 📄 treaty-*-derived-*.item.json
         ├─ 📂 schemas/                        # JSON Schemas for Collections/Items
         │  ├─ 📄 stac-collection-land-treaty-v1.json
         │  ├─ 📄 stac-item-land-treaty-v1.json
         │  └─ 📄 stac-item-land-treaty-scan-v1.json
         ├─ 📂 validation/                     # Validation configs & reports
         │  ├─ 📄 stac-validate.config.yaml
         │  └─ 📂 reports/
         │     ├─ 📄 last-run.json
         │     └─ 📂 history/
         └─ 📂 dcat-prov/                      # RDF views and provenance overlays
            ├─ 📄 land-treaties-dataset.ttl           # DCAT 3.0 Dataset/Distribution graph
            ├─ 📄 land-treaties-catalog.ttl           # DCAT Catalog wrapper
            └─ 📄 land-treaties-provenance.jsonld     # PROV-O bundle (per release)
~~~

Any structural changes under `stac/` MUST be reflected here before merge.

---

## 📦 Collections & Item Scope

### Root Catalog (`catalog.json`)

- `type`: `"Catalog"`  
- Links **down** to land‑treaties Collections via `links[rel="child"]`.  
- Links **up** to the global KFM STAC root (e.g. `data/stac/catalog.json`) via `links[rel="parent"]`.  

Minimum fields:

- `id`: `"kfm-land-treaties"`  
- `description`: short, non‑speculative summary of module scope  
- `links`: root / parent / child relationships (no Items directly under root)

### Core Collections (`collections/`)

Required Collections (v1):

1. `treaties-kansas-v1.collection.json`  
   - Canonical treaty boundary/time Collection.  
   - Spatial extent: multi‑polygon covering **generalized** treaty extents; sensitive sites blurred or masked.  
   - Temporal extent: union of all included treaties’ negotiation/ratification intervals.  

2. `treaties-kansas-scans-v1.collection.json`  
   - Digitized treaty **document scans / transcripts**.  
   - Items primarily reference PDFs/TIFFs/TEI/XML, plus OCR/cleaned text assets.  

3. `treaties-kansas-derived-v1.collection.json`  
   - Derived analysis layers (e.g., change polygons, uncertainty buffers, lineage overlays).  
   - Must clearly mark derived status in `properties["kfm:derivedFrom"]`.  

Each Collection MUST:

- Conform to STAC core (`stac_version`, `type="Collection"`, `id`, `description`, `license`, `extent`, `links`, `summaries`).  
- Declare `stac_extensions` (e.g. `projection`, `version`, `item-assets`) plus any KFM‑specific URIs.  
- Use `license` and `providers` consistent with source archives and tribal agreements.

---

## 🧩 Item & Asset Schema (Treaty Layer)

This standardizes Items under `items/treaties-kansas-v1/`.

### Minimal Treaty Item

Each treaty geometry Item MUST:

- Represent exactly **one treaty spatial footprint** (or a generalized subset) at a given version.  
- Link to its parent Collection via `"collection": "treaties-kansas-v1"`.  
- Use a **stable, human‑readable ID**.  

Conceptual example:

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "treaty-medicine-lodge-1867",
  "collection": "treaties-kansas-v1",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/version/v1.0.0/schema.json",
    "https://kfm.land/extensions/treaty/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      /* generalized / masked geometry */
    ]
  },
  "bbox": [minX, minY, maxX, maxY],
  "properties": {
    "datetime": "1867-10-21T00:00:00Z",
    "start_datetime": "1867-10-21T00:00:00Z",
    "end_datetime":   "1867-10-28T00:00:00Z",

    "kfm:treatyId": "treaty-medicine-lodge-1867",
    "kfm:treatyName": "Medicine Lodge Treaty",
    "kfm:treatySeries": "Medicine Lodge Treaties (1867)",
    "kfm:tribalNations": [
      "Kiowa", "Comanche", "Apache", "Arapaho", "Cheyenne"
    ],
    "kfm:usParties": [
      "United States Government"
    ],
    "kfm:locationGeneralization": "county-centroid-buffer-25km",
    "kfm:sensitivity": "High (Indigenous data — masked/generalized)",
    "kfm:carePolicyRef": "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md",

    "kfm:sourceManifests": [
      "data/sources/historical/land-treaties/medicine-lodge-1867.yaml"
    ],
    "kfm:datasetVersion": "v11.2.2",
    "kfm:graphNode": "neo4j://Event/treaty-medicine-lodge-1867"
  },
  "assets": {
    "geometry": {
      "href": "s3://kfm-prod/land-treaties/geometry/treaty-medicine-lodge-1867.geojson",
      "type": "application/geo+json",
      "roles": ["data", "geometry"],
      "title": "Generalized treaty polygon"
    },
    "scan": {
      "href": "s3://kfm-prod/land-treaties/scans/medicine-lodge-1867.pdf",
      "type": "application/pdf",
      "roles": ["data", "document"],
      "title": "Treaty scan (masked / cleared pages only)"
    },
    "transcription": {
      "href": "s3://kfm-prod/land-treaties/text/medicine-lodge-1867.md",
      "type": "text/markdown",
      "roles": ["metadata", "transcription"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../collections/treaties-kansas-v1.collection.json",
      "type": "application/json"
    },
    {
      "rel": "derived_from",
      "href": "https://kfm.land/sources/kshs/treaty/medicine-lodge-1867",
      "type": "text/html"
    }
  ]
}
~~~

**Generalization rule (public catalogs):**

- Replace precise polygons with generalized shapes (e.g., county, H3 grid, buffers).  
- Record the method in `kfm:locationGeneralization`.  
- Never ship raw coordinates for restricted or sacred sites in public catalogs.

### Scan Items (`treaties-kansas-scans-v1`)

- `geometry` MAY be a generalized point/centroid or omitted (`null`) if spatialized elsewhere.  
- `assets` focus on document scans, derived text, and per‑page slices.  
- Link back to treaty Items via `links[rel="derived_from_treaty"]`.

---

## 🧭 Identifiers, Links & DCAT/PROV

### IDs & Slugs

Collections:

- `treaties-kansas-v1`  
- `treaties-kansas-scans-v1`  
- `treaties-kansas-derived-v1`  

Item IDs:

- Pattern: `treaty-<slug>-<year>` where `<slug>` is a lowercase, hyphenated treaty name.  
- Examples: `treaty-medicine-lodge-1867`, `treaty-kansa-cession-1825`.  

IDs MUST:

- Be **stable** once published.  
- Match corresponding graph nodes (e.g., `neo4j://Event/treaty-medicine-lodge-1867`).

### DCAT Integration (`dcat-prov/`)

- `land-treaties-dataset.ttl` — DCAT 3.0 Dataset/Distribution graph for treaty data.  
- `land-treaties-catalog.ttl` — DCAT Catalog wrapper.  

Patterns:

- Each STAC Collection ↔ one `dcat:Dataset`.  
- Each export bundle ↔ one `dcat:Distribution`.  

### PROV‑O Provenance (`land-treaties-provenance.jsonld`)

Per release, publish a PROV‑O bundle:

- `prov:Entity` — STAC Collections, Items, exported files.  
- `prov:Activity` — ETL jobs, OCR runs, geometry generalization, validation.  
- `prov:Agent` — KFM pipelines, maintainers, partner institutions, tribal authorities.  

Minimum relations:

- `prov:wasGeneratedBy` (Item/Collection → ETL job).  
- `prov:used` (ETL job → source manifests, raw scans).  
- `prov:wasAttributedTo` (Item/Collection → data steward / partner).

---

## 🧪 Validation, CI & Rollback

All STAC artifacts in this module are **CI‑enforced** before merge or release.

### Validation

Config under `validation/`:

~~~yaml
# validation/stac-validate.config.yaml
stac_version: "1.0.0"
schemas:
  collection: "schemas/stac-collection-land-treaty-v1.json"
  item_treaty: "schemas/stac-item-land-treaty-v1.json"
  item_scan: "schemas/stac-item-land-treaty-scan-v1.json"
checks:
  - name: "stac-core"
    kind: "stac-spec"
  - name: "json-schema"
    kind: "jsonschema"
  - name: "links"
    kind: "link-check"
  - name: "faircare"
    kind: "kfm-faircare"
    config:
      care_required: true
      forbid_raw_sensitive_geometries: true
~~~

GitHub Actions (conceptual):

- `.github/workflows/stac-land-treaties.yml`:
  - Run STAC spec validation.  
  - Enforce JSON Schema + link integrity + FAIR+CARE rules.  

### Rollback

If validation fails on `main` or a release branch:

- Automatically revert to the previous STAC catalog snapshot.  
- Open an incident with the FAIR+CARE Council if sovereignty/masking rules are involved.  

Snapshots and lineage MUST record:

- Snapshot ID, git commit, STAC catalog hash.  
- Upstream ETL run IDs and Story Node batches (if affected).

---

## 🧠 Graph, Story Nodes & Focus Mode

This STAC submodule bridges treaty data on disk to:

- Neo4j **treaty event** nodes (CIDOC‑CRM / GeoSPARQL / OWL‑Time aligned).  
- Focus Mode and Story Node narratives in the KFM map/timeline.

### Graph Ingestion

High‑level ingestion rules:

- Each STAC Item → `(:SpatioTemporalAsset {id, href, stacId, collectionId, geometry, datetime})`.  
- `(:SpatioTemporalAsset)-[:REPRESENTS]->(:TreatyEvent)` links assets to treaty events.  
- Geometry mirrored into `geo:Geometry` nodes (WKT/GeoJSON) for spatial queries.

### Story Nodes & Focus Mode

Story Nodes (defined in `docs/data/historical/land-treaties/`) can:

- Store **STAC Item IDs** so the UI can highlight treaty polygons.  
- Reference STAC Collections in “Sources” panels.  

Focus Mode:

1. User selects a treaty or Story Node.  
2. Backend loads related `TreatyEvent`, `Place`, `Actor` nodes and linked STAC Items.  
3. Summarization (deterministic, pinned models) produces factual narrative snippets.  
4. UI shows summary, polygons, and explicit source references.  

Focus Mode MUST:

- Respect `kfm:locationGeneralization` (no un‑masking in public views).  
- Surface STAC IDs, PROV, and ETL lineage for expert drill‑down.

---

## 🧬 Version History

| Version | Date       | Author        | Notes                                           |
|--------:|-----------:|--------------|-------------------------------------------------|
| v11.2.2 | 2025-12-11 | `<your-name>` | Initial Land Treaties STAC submodule README.   |

Update this table whenever STAC layout, schemas, or governance behavior changes.

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Repo Root](../../../../README.md) ·  
[Standards Index](../../../../docs/standards/INDEX.md) ·  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)  

**🔐 Compliance**  
FAIR+CARE · KFM‑MDP v11.2.6 · KFM‑OP v11 · KFM‑STAC v11 · KFM‑DCAT v11 · KFM‑PROV v11 · SLSA · SPDX  

**🪶 Sovereignty**  
Operated under the **Indigenous Data Protection** standard; locations and attributes may be generalized or omitted at the request of affected Nations.

**♻️ Sustainability**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)  

**End of Document**

</div>

