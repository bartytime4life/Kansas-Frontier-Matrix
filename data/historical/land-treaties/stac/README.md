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

<div align="center">

# 🛰 **Kansas Frontier Matrix — Land Treaties STAC Catalog**  
`data/historical/land-treaties/stac/`

**Role in the pipeline**  
Deterministic ETL → **STAC/DCAT/PROV** catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

</div>

---

## 📘 Overview

The **Land Treaties STAC Catalog** is the on‑disk index of:

- Treaty **boundary geometries** (ceded lands, reservations, generalized sensitive extents)  
- Treaty **event timelines** (negotiation, signing, ratification windows)  
- Linked **document assets** (scans, transcripts, summaries)  
- **Metadata** suitable for ingestion into DCAT, PROV‑O, and the KFM Neo4j graph  

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
- Links **up** to the global KFM STAC root (e.g., `data/stac/catalog.json`) via `links[rel="parent"]`.  

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
- Declare `stac_extensions` (e.g., `projection`, `version`, `item-assets`) plus any KFM‑specific URIs.  
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

**Generalization rule (public catalogs)**

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

- `land-treaties-dataset.ttl` — DCAT 3.0 Dataset/Distribution graph.  
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

Conceptual config under `validation/`:

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
[Docs Root](../../../../docs/README.md) ·  
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


<!-- FILE: data/historical/land-treaties/stac/collections/README.md -->
---
title: "🛰 KFM — Land Treaties STAC Collections Guide"
path: "data/historical/land-treaties/stac/collections/README.md"
version: "v11.2.2"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Data Catalog Collections Guide"
intent: "stac-collection-governance"
semantic_document_id: "kfm-stac-land-treaties-collections-v11.2.2"

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
sunset_policy: "Supersedes prior land-treaties STAC collection layouts"
immutability_status: "version-pinned"
ai_training_inclusion: false

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 Collection Profiles"
    - "🧩 Common Metadata Fields"
    - "🌍 Spatial & Temporal Extents"
    - "⚖️ FAIR+CARE & Sovereignty Rules"
    - "🧬 Versioning & Deprecation"
    - "⚖️ Footer"

provenance_chain:
  - "data/historical/land-treaties/stac/README.md@v11.2.2"
  - "docs/data/historical/land-treaties/README.md@v11.2.2"
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

doc_uuid: "urn:kfm:stac:land-treaties:collections:v11.2.2"
event_source_id: "stac:kfm:land-treaties:collections:v11.2.2"
---

<div align="center">

# 🛰 **KFM — Land Treaties STAC Collections Guide**  
`data/historical/land-treaties/stac/collections/`

**Role in the pipeline**  
Deterministic ETL → **STAC Collections & Items** → DCAT/PROV → Neo4j → API → MapLibre/Cesium → Story Nodes → Focus Mode

</div>

---

## 📘 Overview

This document normatively defines the **STAC Collections** for the Land Treaties module:

- Which Collections exist.  
- What each Collection represents conceptually.  
- Required metadata and extension usage per Collection.  
- How Collections relate to Items, DCAT Datasets, PROV provenance, and Neo4j nodes.

Scope: **`data/historical/land-treaties/stac/collections/`**, inheriting governance, sovereignty, and FAIR+CARE constraints from:

- `data/historical/land-treaties/stac/README.md` (STAC submodule root)  
- `docs/data/historical/land-treaties/README.md` (Land Treaties module root)  

Any new Collection JSON introduced here **must be compatible** with those contracts.

---

## 🗂️ Directory Layout

Emoji layout (📂 = directory, 📄 = file). Names on disk remain ASCII.

~~~text
📂 data/
└─ 📂 historical/
   └─ 📂 land-treaties/
      └─ 📂 stac/
         └─ 📂 collections/
            ├─ 📄 README.md                             # This file
            ├─ 📄 treaties-kansas-v1.collection.json    # Canonical treaty polygons/time
            ├─ 📄 treaties-kansas-scans-v1.collection.json
            └─ 📄 treaties-kansas-derived-v1.collection.json
~~~

Any additional Collection JSON added under `collections/` MUST be:

1. Documented in this README (name, purpose, scope).  
2. Wired into validation configs under `../validation/`.  
3. Wired into DCAT / PROV overlays under `../dcat-prov/`.

---

## 📦 Collection Profiles

Three **primary Collections** for v11.2.2. All are `type = "Collection"` and implement STAC 1.0+ core.

### 1️⃣ `treaties-kansas-v1.collection.json` — Canonical Treaty Footprints

**Concept**  
Spatiotemporal representation of **treaty extents** (generalized) that directly affect present‑day Kansas, plus overlapping treaties whose geographies intersect the region.

**Contents**

- Geometry: generalized polygons/multipolygons (buffers, county/H3 aggregates, etc.).  
- Time: treaty negotiation and ratification intervals.  
- Links to treaty event nodes in Neo4j and to document scans/transcripts in related Collections.

**Required properties**

- `id`: `"treaties-kansas-v1"`  
- `stac_extensions`:
  - `projection` (if using non‑WGS84 assets)  
  - `version`  
  - optional KFM treaty extension (`https://kfm.land/extensions/treaty/v1.0.0/schema.json`)  
- `extent.spatial`: union of all public, generalized treaty geometries.  
- `extent.temporal`: union of negotiation/ratification intervals represented.  
- `license`: `"CC-BY-4.0"` or stricter, subject to source and tribal agreements.  
- `providers`: at minimum, KFM + relevant archives/tribal partners.

---

### 2️⃣ `treaties-kansas-scans-v1.collection.json` — Treaty Scans & Texts

**Concept**  
Digitized **treaty documents** (scans, OCR text, cleaned transcripts), with optional coarse spatial tags.

**Contents**

- Assets: PDFs/TIFFs, page images, TEI/XML, Markdown transcripts, etc.  
- Optional geometry: points/centroids for approximate locations, or `null` if geometry is carried by `treaties-kansas-v1`.

**Required properties**

- `id`: `"treaties-kansas-scans-v1"`  
- `stac_extensions` may include:
  - `version`  
  - `file` / `checksum`  
- `extent.spatial`: bounding extent of documents with spatial tags.  
- `extent.temporal`: coverage interval of documented treaties.  
- `license`, `providers` as above, with stricter per‑asset licensing where needed.

---

### 3️⃣ `treaties-kansas-derived-v1.collection.json` — Derived Analysis Layers

**Concept**  
Derived treaty **analysis products**, such as:

- Change map polygons (before/after comparisons).  
- Uncertainty buffers.  
- Influence zones used in models or interpretive Story Nodes.

**Contents**

- Assets that are **not raw treaty documents**, but results of modeling or spatial analysis.  
- Strong, explicit provenance back to underlying treaties and sources.

**Required properties**

- `id`: `"treaties-kansas-derived-v1"`  
- `stac_extensions` may include:
  - `projection`  
  - `version`  
  - analysis‑specific extensions (e.g., `raster`, `grid`) where applicable  
- `properties["kfm:derivedFrom"]`: MUST reference IDs of one or more source treaties (e.g., `["treaty-medicine-lodge-1867"]`).  
- Clear `description` explaining the derivation method.

---

## 🧩 Common Metadata Fields

Strongly recommended (often required) for all Land Treaties Collections:

- `stac_version`: `"1.0.0"` (or later once upgraded).  
- `type`: `"Collection"`  
- `id`: stable, lowercase, hyphenated (no spaces).  
- `description`: non‑speculative summary, including:
  - geographic focus (Kansas / region)  
  - time frame (approx. 1850–1890)  
  - governance note (FAIR+CARE, Indigenous sovereignty)  
- `license`: module‑level default or stricter.  
- `keywords`: include `"treaty"`, `"reservation"`, `"cession"`, `"Kansas"`, plus appropriate tribal/place names.  
- `providers`: include KFM, archives, and partner Nations where agreed.  

`links` SHOULD include:

- `rel="root"` / `rel="parent"`: to the global KFM STAC root and land‑treaties STAC root.  
- `rel="via"` / `rel="derived_from"`: for external references (e.g., KSHS, NARA finding aids).  
- `rel="license"` or equivalent when additional licensing information is required.

---

## 🌍 Spatial & Temporal Extents

### Spatial (`extent.spatial`)

- CRS: **EPSG:4326** (WGS84) for `extent.spatial.bbox`.  
- Generalization:
  - Public Collections MUST use **generalized geometries** when required by sovereignty policy:
    - county or multi‑county polygons  
    - buffered centroids  
    - coarse grid cells (e.g., H3)  
- Sensitive areas (sacred sites, burial grounds, restricted territories) MUST NOT be directly encoded as precise geometry in public Collections.

### Temporal (`extent.temporal`)

- Use treaty event intervals:
  - negotiation windows  
  - signing dates  
  - ratification dates  
- For ambiguous dates:
  - prefer **intervals** (`start_datetime` / `end_datetime`)  
  - describe uncertainty in `description` and/or `kfm:datePrecision`.

---

## ⚖️ FAIR+CARE & Sovereignty Rules

In addition to module‑level policy:

- Collections MUST NOT:
  - weaken masking/generalization chosen by partner Nations or archival agreements  
  - add more precise geometries or attributes in public catalogs without explicit approval  

Per Collection:

- Document any **default generalization strategy** at Collection level (e.g., `kfm:locationGeneralizationDefault: "county-centroid-buffer-25km"`).  
- Ensure derived Collections (like `treaties-kansas-derived-v1`) **inherit or strengthen** masking, never relax it.  

If a treaty, site, or region is reclassified as more sensitive:

- Collections MUST be updated to strengthen generalization (or suppress relevant Items) in the next version.  
- The `description` SHOULD mention the masking policy change, without revealing newly restricted details.

---

## 🧬 Versioning & Deprecation

Collections follow a **semantic‑ish versioning** pattern:

- `treaties-kansas-v1` is the initial v11.2.x series.  
- Breaking changes (schema, semantics, masking regime) should introduce:
  - `treaties-kansas-v2.collection.json`, etc.  

Rules:

- Never reuse a Collection `id` with different semantics.  
- When introducing `v2`:
  - Keep `v1` in the repo until explicitly deprecated.  
  - Use `links` such as `rel="predecessor-version"` / `rel="successor-version"` (and DCAT/PROV equivalents).  

Release‑level provenance for Collections is tracked in:

- `../dcat-prov/land-treaties-dataset.ttl`  
- `../dcat-prov/land-treaties-provenance.jsonld`  

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../docs/README.md) ·  
[Land Treaties STAC Root](../README.md) ·  
[Module Root](../../README.md) ·  
[Standards Index](../../../../../docs/standards/INDEX.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance**  
FAIR+CARE · KFM‑MDP v11.2.6 · KFM‑OP v11 · KFM‑STAC v11 · KFM‑DCAT v11 · KFM‑PROV v11 · SLSA · SPDX  

**🪶 Sovereignty**  
Operated under the **Indigenous Data Protection** standard; Collection semantics and spatial detail may be generalized or restricted at the request of affected Nations.

**♻️ Sustainability**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)  

**End of Document**

</div>


<!-- FILE: data/historical/land-treaties/stac/dcat-prov/README.md -->
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

Scope:

- `data/historical/land-treaties/stac/dcat-prov/`  

Inherits constraints from:

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
            ├─ 📄 README.md                        # This file
            ├─ 📄 land-treaties-dataset.ttl        # DCAT 3.0 Dataset/Distribution graph
            ├─ 📄 land-treaties-catalog.ttl        # DCAT Catalog wrapper
            └─ 📄 land-treaties-provenance.jsonld  # PROV-O bundle (per release)
~~~

Adding or renaming DCAT/PROV files here **requires** updating this README, plus the STAC root README and validation configs.

---

## 📦 DCAT Dataset & Catalog Graphs

Two Turtle files are normative:

- `land-treaties-dataset.ttl` — **DCAT 3.0 Dataset graph** for treaty data.  
- `land-treaties-catalog.ttl` — **DCAT Catalog** that wraps the Dataset and links into the global KFM catalog.

### DCAT Dataset Pattern (`land-treaties-dataset.ttl`)

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

Rules:

- One **primary Dataset URI** per module (e.g., `.../dataset/land-treaties`).  
- Each major export bundle (STAC snapshot, GeoJSON, zipped archive) is a `dcat:Distribution`.  
- Sovereignty constraints (masking/generalization) MUST be described in `dct:description` and/or custom `kfm:` properties.

### DCAT Catalog Pattern (`land-treaties-catalog.ttl`)

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

`land-treaties-provenance.jsonld` encodes **lineage** per release:

- Which ETL jobs ran.  
- Which sources they used.  
- Which STAC/DCAT entities they generated.  
- Which agents were responsible.

### Minimal Bundle Pattern

Conceptual JSON‑LD snippet:

~~~json
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
~~~

Requirements:

- At least one `prov:Activity` per ETL run that produced or updated the Dataset.  
- `prov:Entity` instances for the DCAT Dataset, STAC Collections, and main exports.  
- `prov:Agent` instances for the ETL pipeline and governance bodies (as permitted by policy).

---

## 🧭 Linkage to STAC & Neo4j

DCAT and PROV are **overlays** on top of STAC and the knowledge graph.

### STAC ↔ DCAT

- Each STAC Collection under `../collections/` maps to a **DCAT Dataset** in `land-treaties-dataset.ttl`.  
- Each export bundle (e.g., zipped STAC snapshot, GeoJSON export) maps to a **dcat:Distribution** with `dcat:downloadURL` or `dcat:accessURL`.

### STAC/DCAT ↔ Neo4j

- Neo4j `Dataset` / `DatasetVersion` nodes reference the DCAT Dataset URI (e.g., `ds.dcatUri`).  
- STAC Collections and Items reference their Dataset URI using `kfm:dcatDataset` (in STAC `properties` or via mapping).  
- Graph ingestion uses these URIs to align identifiers across:
  - STAC  
  - DCAT  
  - PROV  
  - Neo4j  
  - Story Nodes / Focus Mode

### FAIR+CARE & Sovereignty

- DCAT and PROV overlays MUST NOT expose more precise spatial data or sensitive attributes than allowed by STAC and sovereignty policies.  
- If a geometry or attribute is generalized or suppressed in STAC, the DCAT/PROV layers MUST respect that decision and never reveal the unmasked form.

---

## 🧪 Validation, CI & Rollback

This directory participates in **metadata CI** for the Land Treaties module.

### Validation

Conceptual checks:

- RDF/Turtle syntax validation for `*.ttl`.  
- JSON‑LD syntax/context validation for `land-treaties-provenance.jsonld`.  
- Optional SHACL or ShEx validation of DCAT and PROV shapes.

Example config:

~~~yaml
# validation/dcat-prov-validate.config.yaml
targets:
  - path: "data/historical/land-treaties/stac/dcat-prov/land-treaties-dataset.ttl"
    kind: "rdf-turtle"
  - path: "data/historical/land-treaties/stac/dcat-prov/land-treaties-catalog.ttl"
    kind: "rdf-turtle"
  - path: "data/historical/land-treaties/stac/dcat-prov/land-treaties-provenance.jsonld"
    kind: "jsonld"
checks:
  - name: "rdf-syntax"
  - name: "dcat-profile"
  - name: "prov-profile"
  - name: "faircare-metadata"
~~~

GitHub Actions (conceptual):

- `.github/workflows/metadata-land-treaties.yml`:
  - Run STAC + DCAT + PROV validation.  
  - Fail on any syntax or profile violations.

### Rollback

If DCAT/PROV validation fails on `main` or a release branch:

- Revert to the previous DCAT/PROV snapshot (in lockstep with STAC snapshot).  
- Open a FAIR+CARE / governance incident if the failure relates to sovereignty or masking metadata.  

Rollbacks MUST be represented in:

- `land-treaties-provenance.jsonld` (additional `prov:Activity` for rollback).  
- Version history in this README.

---

## 🧬 Version History

| Version | Date       | Author        | Notes                                              |
|--------:|-----------:|--------------|----------------------------------------------------|
| v11.2.2 | 2025-12-11 | `<your-name>` | Initial Land Treaties DCAT/PROV overlay README.   |

Update this table when DCAT/PROV structures, identifiers, or governance semantics change.

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../docs/README.md) ·  
[Land Treaties STAC Root](../README.md) ·  
[Collections Guide](../collections/README.md) ·  
[Module Root](../../README.md) ·  
[Standards Index](../../../../../docs/standards/INDEX.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)  

**🔐 Compliance**  
FAIR+CARE · KFM‑MDP v11.2.6 · KFM‑OP v11 · KFM‑STAC v11 · KFM‑DCAT v11 · KFM‑PROV v11 · SLSA · SPDX  

**🪶 Sovereignty**  
Operated under the **Indigenous Data Protection** standard; identifiers and graphs may be generalized or restricted at the request of affected Nations.

**♻️ Sustainability**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)  

**End of Document**

</div>
