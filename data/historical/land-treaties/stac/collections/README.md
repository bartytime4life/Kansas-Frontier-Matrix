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

It is scoped to **`data/historical/land-treaties/stac/collections/`** and **inherits** all governance, sovereignty, and FAIR+CARE constraints from:

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

**Rule:** Any additional Collection JSON added under `collections/` MUST be:

1. Documented in this README (name, purpose, scope).  
2. Wired into validation configs under `../validation/`.  
3. Wired into DCAT / PROV overlays under `../dcat-prov/`.

---

## 📦 Collection Profiles

We define three **primary Collections** for v11.2.2. All are `type = "Collection"` and implement STAC 1.0+ core.

### 1️⃣ `treaties-kansas-v1.collection.json` — Canonical Treaty Footprints

**Concept:**  
Spatiotemporal representation of **treaty extents** (generalized) that directly affect present‑day Kansas, plus overlapping treaties whose geographies intersect the region.

**Contents:**

- Geometry: generalized polygons / multipolygons (e.g., coarse buffers, county/H3 aggregates).  
- Time: treaty negotiation and ratification intervals.  
- Links to:
  - Treaty event nodes in Neo4j.  
  - Document scans and transcripts via related Collections / Items.

**Required properties:**

- `id`: `"treaties-kansas-v1"`  
- `stac_extensions`:
  - `projection` (if using non‑WGS84 assets)
  - `version`
  - optional KFM treaty extension (`https://kfm.land/extensions/treaty/v1.0.0/schema.json`)  
- `extent.spatial`: union of all public treaty geometries (generalized).  
- `extent.temporal`: union of negotiation/ratification intervals represented here.  
- `license`: `"CC-BY-4.0"` or stricter, subject to source and tribal agreements.  
- `providers`: at minimum, KFM + relevant archives/tribal partners.

### 2️⃣ `treaties-kansas-scans-v1.collection.json` — Treaty Scans & Texts

**Concept:**  
Digitized **treaty documents** (scans, OCR text, cleaned transcripts), with optional coarse spatial tags.

**Contents:**

- Assets: PDFs/TIFFs, page images, TEI/XML, Markdown transcripts, etc.  
- Optional geometry: points/centroids for approximate locations or `null` if geometry is carried by `treaties-kansas-v1`.

**Required properties:**

- `id`: `"treaties-kansas-scans-v1"`  
- `stac_extensions` may include:
  - `version`
  - `file` / `checksum`
- `extent.spatial`: bounding extent of documents that have spatial tags.  
- `extent.temporal`: coverage interval of documented treaties.  
- `license`, `providers` as above, with stricter per‑asset licensing noted in asset metadata if needed.

### 3️⃣ `treaties-kansas-derived-v1.collection.json` — Derived Analysis Layers

**Concept:**  
Derived treaty **analysis products** such as:

- Change map polygons (before/after comparisons).  
- Uncertainty buffers.  
- Influence zones used in models or interpretive Story Nodes.

**Contents:**

- Assets that are **not raw treaty documents**, but results of modeling or spatial analysis.  
- Strong, explicit provenance back to underlying treaties and sources.

**Required properties:**

- `id`: `"treaties-kansas-derived-v1"`  
- `stac_extensions` may include:
  - `projection`
  - `version`
  - analysis‑specific extensions (e.g., `raster`, `grid`) where applicable.
- `properties["kfm:derivedFrom"]`: MUST reference IDs of one or more source treaties (e.g., `["treaty-medicine-lodge-1867"]`).  
- Clear description field explaining **what kind of derivation** has been applied.

---

## 🧩 Common Metadata Fields

The following are **strongly recommended** (often required) for all Land Treaties Collections:

- `stac_version`: `"1.0.0"` (or later, once upgraded across KFM).  
- `type`: `"Collection"`  
- `id`: stable, lowercase, hyphenated (no spaces).  
- `description`: non‑speculative summary, including:
  - geographic focus (Kansas / Great Plains)  
  - time frame (approx. 1850–1890)  
  - governance note (FAIR+CARE, Indigenous sovereignty)  
- `license`: module‑level default or stricter.  
- `keywords`: include `"treaty"`, `"reservation"`, `"cession"`, `"Kansas"`, plus appropriate tribal/place names.  
- `providers`: include KFM, archives, and partner Nations where agreed.  

`links` SHOULD include:

- `rel="root"` / `rel="parent"`: to the global KFM STAC root and land‑treaties STAC root.  
- `rel="via"` / `rel="derived_from"`: for external references (e.g., KSHS, NARA finding aids).  
- `rel="license"` or equivalent, when external licensing information is required.

---

## 🌍 Spatial & Temporal Extents

### Spatial (`extent.spatial`)

- CRS: **EPSG:4326** (WGS84) for the explicit `extent.spatial.bbox`.  
- Geometry detail:
  - Public Collections (especially `treaties-kansas-v1`) MUST use **generalized geometries** when required by sovereignty policy:
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
  - prefer **intervals** (`start_datetime` / `end_datetime`) with a clear description of uncertainty in the Collection’s `description` and/or custom fields (e.g., `kfm:datePrecision`).

---

## ⚖️ FAIR+CARE & Sovereignty Rules

This Collections guide is **sovereignty‑first**. In addition to the module‑level policy:

- Collections MUST NOT:
  - degrade masking/generalization chosen by partner Nations or archival agreements.  
  - add new, more precise geometries or attributes in public catalogs without explicit approval.  

- For each Collection:
  - Document any **generalization strategy** at Collection level (e.g., `kfm:locationGeneralizationDefault: "county-centroid-buffer-25km"`).  
  - Ensure all derived Collections (`treaties-kansas-derived-v1`) **inherit or strengthen** masking, not relax it.  

- If a treaty, site, or region is later reclassified as more sensitive:
  - Collections here MUST be updated to strengthen generalization (or fully suppress relevant Items) in the next version.  
  - A note SHOULD be added to the Collection `description` explaining the change in masking policy, without revealing newly restricted details.

---

## 🧬 Versioning & Deprecation

Collections follow a **semantic‑ish versioning** pattern:

- `treaties-kansas-v1` is the initial v11.2.x series.  
- Future major changes (schema, semantics, masking regime) should create:
  - `treaties-kansas-v2.collection.json`, and so on.  

Rules:

- Never reuse a Collection `id` with different semantics.  
- When introducing `v2`:
  - Keep `v1` in the repo until explicitly deprecated.  
  - Use `links` such as:
    - `rel="predecessor-version"` / `rel="successor-version"` (or DCAT/PROV equivalents in `dcat-prov/`).  
- Mark deprecation in:
  - Collection `description` (brief notice + pointer to successor).  
  - DCAT graph (`dct:isReplacedBy` / `dct:replaces` or similar pattern).  

Release‑level provenance for Collections is tracked in:

- `../dcat-prov/land-treaties-dataset.ttl`  
- `../dcat-prov/land-treaties-provenance.jsonld`  

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Repo Root](../../../../../README.md) ·  
[Land Treaties STAC Root](../README.md) ·  
[Module Root](../../../README.md) ·  
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

