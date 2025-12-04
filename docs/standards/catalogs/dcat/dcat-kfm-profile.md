---
title: "📘 KFM v11.2.3 — DCAT KFM Profile (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Normative DCAT profile for the Kansas Frontier Matrix, defining required fields, classes, and patterns for DCAT Datasets, Distributions, and DataServices under the STAC-first → DCAT-derived model."
path: "docs/standards/catalogs/dcat/dcat-kfm-profile.md"
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

doc_uuid: "urn:kfm:doc:standards-catalogs-dcat-kfm-profile-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-dcat-kfm-profile-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:dcat:kfm-profile:v11.2.3"

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

doc_kind: "Standard"
intent: "catalogs-dcat-kfm-profile"
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
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/catalogs-dcat-kfm-profile-v1.json"
shape_schema_ref: "../../schemas/shacl/catalogs-dcat-kfm-profile-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major KFM DCAT profile revision"
---

<div align="center">

# 📘 Kansas Frontier Matrix — DCAT KFM Profile  
`docs/standards/catalogs/dcat/dcat-kfm-profile.md`

**Purpose:**  
Define the **normative DCAT profile** for the Kansas Frontier Matrix (KFM):  
which DCAT classes and properties are required, how they are populated **from STAC**, and how DCAT artifacts must behave to support **discovery, federation, and governance** under the **STAC-first → DCAT-derived** model.

</div>

---

## 📘 1. Scope & Compatibility

This profile applies to:

- `dcat:Dataset` records representing KFM datasets.  
- `dcat:Distribution` records representing access/download options.  
- `dcat:DataService` records representing APIs and live services.  
- Optional `dcat:Catalog` / `dcat:CatalogRecord` for portal integration.

It is:

- Compatible with **DCAT 2.x and DCAT 3.0** (core terms only).  
- Designed to be used with:

  - KFM STAC profile (`stac-kfm-profile.md`).  
  - STAC-first → DCAT-derived model (`../stac-dcat-derivation.md`).  
  - STAC → DCAT crosswalk (`../crosswalks/stac-dcat-crosswalk.md`).

**KFM position:**

- **STAC is authoritative.**  
- DCAT is a **derived discovery and federation layer**, never the source of truth.

---

## 🧱 2. Core Classes & Shapes

### 2.1 Required Classes

KFM DCAT MUST use:

- `dcat:Dataset` — core class representing a dataset.  
- `dcat:Distribution` — access/distribution options for a dataset.  

KFM DCAT MAY use:

- `dcat:DataService` — for APIs, tile services, and dynamic endpoints.  
- `dcat:Catalog` / `dcat:CatalogRecord` — for portal implementations and external federation where needed.

### 2.2 Identification

- Every `dcat:Dataset` MUST have:

  - A stable IRI (`@id`).  
  - `dct:identifier` matching the STAC/registry identifier (see §3).

- Every `dcat:Distribution` MUST be associated with exactly one `dcat:Dataset` (in this profile).

---

## 📦 3. Dataset Profile (Derived from STAC)

This section specifies what **every KFM `dcat:Dataset`** MUST or SHOULD include. All fields are derived from STAC via the governed crosswalk.

### 3.1 Required Dataset Properties

| Property            | Requirement | STAC Source (conceptual)                 |
|---------------------|------------|------------------------------------------|
| `dct:identifier`    | REQUIRED   | STAC `id` or `kfm:dataset_id`           |
| `dct:title`         | REQUIRED   | STAC `properties.title` or Collection title |
| `dct:description`   | REQUIRED   | STAC `properties.description` or Collection description |
| `dct:spatial`       | REQUIRED   | STAC `bbox` / `extent.spatial`          |
| `dct:temporal`      | REQUIRED   | STAC `datetime` or temporal intervals    |
| `dcat:distribution` | REQUIRED   | Derived from STAC `assets`              |
| `dct:license`       | REQUIRED   | STAC `license` (Collection or Item, as per profile) |

### 3.2 Recommended Dataset Properties

| Property           | Recommendation | STAC Source / Notes                    |
|--------------------|----------------|----------------------------------------|
| `dcat:keyword`     | RECOMMENDED   | STAC `keywords`, domains, extensions   |
| `dct:publisher`    | RECOMMENDED   | STAC `providers` with role `producer`/`licensor` |
| `dct:creator`      | RECOMMENDED   | STAC `providers` with `processor`/`host` |
| `dcat:landingPage` | RECOMMENDED   | KFM catalog/portal landing URL         |
| `dct:type`         | OPTIONAL      | High-level resource type (e.g., `Dataset`, `Collection`) |
| `dct:subject`      | OPTIONAL      | Additional thematic classification     |

### 3.3 Spatial Representation (`dct:spatial`)

KFM DCAT uses:

- `dct:spatial` with a `dct:Location` node.  
- The `bbox` is derived from STAC `bbox` (Items) or `extent.spatial.bbox` (Collections).

Example pattern (simplified):

~~~json
"dct:spatial": {
  "@type": "dct:Location",
  "bbox": [-102.0, 36.99, -94.6, 40.01]
}
~~~

Federation partners MAY map this into their own spatial representations, but must not assume more precision than STAC provides.

### 3.4 Temporal Representation (`dct:temporal`)

DCAT `dct:temporal` MUST be a `dct:PeriodOfTime` with:

- `dcat:startDate`  
- `dcat:endDate` (which MAY be `null` or omitted for open-ended series)

Derived from:

- `properties.datetime` (instant) → same start/end date.  
- `properties.start_datetime` / `end_datetime` → start/end mapping.  
- `extent.temporal.interval` for Collections.

---

## 📦 4. Distribution Profile

Every `dcat:Distribution` represents one access path or file derived from a STAC Asset.

### 4.1 Required Distribution Properties

| Property             | Requirement | STAC Source                 |
|----------------------|------------|-----------------------------|
| `dcat:downloadURL` or `dcat:accessURL` | REQUIRED   | Asset `href`              |
| `dct:format`         | REQUIRED   | Asset `type` (MIME)        |

Rules:

- Use `dcat:downloadURL` when direct downloads are available.  
- Use `dcat:accessURL` when accesses are mediated via services (APIs, OGC services, etc.).

### 4.2 Recommended Distribution Properties

| Property       | Recommendation | STAC Source / Notes              |
|----------------|----------------|----------------------------------|
| `dct:title`    | RECOMMENDED   | Asset `title` or derived label   |
| `dct:description` | OPTIONAL    | Asset-level description (if present) |
| `spdx:checksum`| RECOMMENDED   | Asset `checksum:sha256`          |
| `dcat:mediaType` | OPTIONAL    | Same as `dct:format` or refined  |
| `dct:license`  | OPTIONAL      | Overrides dataset license if necessary |

Checksum example:

~~~json
"spdx:checksum": {
  "@type": "spdx:Checksum",
  "spdx:algorithm": "sha256",
  "spdx:checksumValue": "abc123..."
}
~~~

### 4.3 Multi-Asset Datasets

When a STAC Item has multiple assets:

- Each asset that is relevant for discovery/downloading SHOULD be mapped to a corresponding `dcat:Distribution`.  
- Some internal or derived assets (debug, QA, internal-only) may be omitted from public DCAT based on FAIR+CARE and sovereignty policies.

---

## 🌐 5. DataService Profile

KFM MAY expose `dcat:DataService` records for:

- Public APIs (REST/GraphQL).  
- OGC services (WMS/WFS/WCS/WMTS).  
- Tile services (XYZ, vector tiles, Cloud-optimized services).

### 5.1 Required DataService Properties

| Property        | Requirement | Notes                             |
|-----------------|------------|------------------------------------|
| `@type`         | REQUIRED   | `dcat:DataService`                |
| `dct:identifier`| REQUIRED   | Service identifier                |
| `dct:title`     | REQUIRED   | Human-readable title              |
| `dcat:endpointURL` | REQUIRED| Base URL for the service          |

### 5.2 Recommended Properties

- `dct:description` — description of the service and dataset coverage.  
- `dcat:servesDataset` — references to one or more `dcat:Dataset`s served by the service.  
- `dct:license` — license terms for usage.  
- `dct:conformsTo` — standards (e.g., OGC API specifications).

---

## 🛡️ 6. FAIR+CARE & Sovereignty Semantics in DCAT

DCAT records derived from STAC MUST respect:

- `kfm-faircare` extension semantics (`kfmfc:*`).  
- Domain-specific sensitivity fields (e.g., `kfmarch:sensitivity_class`, `kfmhydro:hydro_sensitivity`).

### 6.1 Eligibility for Public DCAT

DCAT records intended for **public** catalogs must only represent:

- Datasets where `kfmfc:sensitivity` and `kfmfc:care_label` permit public exposure.  
- Derived/generalized forms where required (no leaking of precise STAC geometries or asset URLs).

### 6.2 Representing Governance in DCAT

KFM DCAT MAY:

- Include governance-related keywords (e.g., `FAIR+CARE`, `Community-Controlled`).  
- Embed links to governance docs via:
  - `dcat:landingPage` pointing to dataset pages that surface governance info.  
  - Custom properties in the KFM DCAT profile extension (if standardized).

No DCAT fields should misrepresent the underlying governance status.

---

## 🔁 7. STAC Integration & Crosswalk Expectations

This profile relies on:

- STAC KFM profile (`stac-kfm-profile.md`) for source metadata requirements.  
- STAC extensions (`kfm-core`, `kfm-faircare`, domain extensions) for rich semantics.  
- STAC → DCAT crosswalks (`../crosswalks/stac-dcat-crosswalk.md`) for implementation details.

**Normative expectations:**

- For every published `dcat:Dataset`, there MUST be at least one corresponding STAC Item or Collection that satisfies the KFM STAC profile.  
- The following fields MUST be consistent between STAC and DCAT:

  - Identifier (`id` / `kfm:dataset_id` ↔ `dct:identifier`).  
  - Temporal coverage.  
  - Spatial coverage (LC-level bbox).  
  - Licensing and provenance information (at appropriate abstracted level).

---

## 🧪 8. Validation & SHACL Shapes

KFM DCAT artifacts MUST be validated against:

- JSON schema (where used) for basic JSON structure.  
- **SHACL shapes** defined in:

  - `catalogs-dcat-kfm-profile-v1.shape.ttl` (referenced in front matter).

Validation MUST ensure:

- Presence of all required properties in Datasets, Distributions, and DataServices.  
- Correct data types (string, URI, dateTime, array).  
- Conformance with controlled vocabularies (where relevant).  
- Consistency with crosswalk-derived expectations (e.g., presence of distributions for each dataset).

CI workflows (indicative):

- `catalog-dcat-validate.yml`  
- `catalog-crosswalk-validate.yml`

These MUST fail builds when:

- DCAT does not conform to the KFM DCAT profile.  
- Crosswalk-derived invariants are violated.

---

## ✅ 9. Implementation Checklist (DCAT Generation)

Before DCAT artifacts are accepted as KFM-compliant:

1. **STAC validation**
   - Source STAC Items/Collections pass the KFM STAC profile and extension schemas.

2. **Crosswalk application**
   - DCAT generated exclusively from STAC using governed crosswalk code.  
   - No manual edits for production DCAT.

3. **Profile validation**
   - DCAT JSON-LD passes KFM DCAT SHACL shapes.  
   - All required Dataset/Distribution/DataService fields are present.

4. **Governance checks**
   - Only datasets that satisfy FAIR+CARE & sovereignty criteria appear in public DCAT exports.  
   - No sensitive internal-only assets or URLs are exposed.

5. **Continuous integration**
   - CI jobs for DCAT validation and STAC ↔ DCAT consistency are configured and passing.

6. **Telemetry**
   - Validation results and export statistics recorded in `catalog-metadata-telemetry.json`.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial KFM DCAT profile; defined Dataset, Distribution, and DataService requirements; clarified STAC integration, governance semantics, and validation expectations under the STAC-first → DCAT-derived model. |

