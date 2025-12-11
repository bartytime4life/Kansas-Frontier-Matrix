---
title: "🔁 KFM v11.2.6 — STAC → DCAT Crosswalk (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Normative field-level crosswalk for deriving DCAT from authoritative STAC records in the Kansas Frontier Matrix, under the STAC-first → DCAT-derived model."
path: "docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md"
version: "v11.2.6"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 2.x/3.0 crosswalk-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-crosswalks-stac-dcat-v11.2.6"
semantic_document_id: "kfm-standards-catalogs-crosswalks-stac-dcat-v11.2.6"
event_source_id: "ledger:kfm:standards:catalogs:crosswalks:stac-dcat:v11.2.6"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/catalog-metadata-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

doc_kind: "Crosswalk Spec"
intent: "catalogs-stac-to-dcat-crosswalk"
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

json_schema_ref: "../../../../schemas/json/catalogs-stac-dcat-crosswalk-v1.json"
shape_schema_ref: "../../../../schemas/shacl/catalogs-stac-dcat-crosswalk-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC → DCAT crosswalk revision"
---

<div align="center">

# 🔁 Kansas Frontier Matrix — STAC → DCAT Crosswalk  
`docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

**Purpose**  
Define the **normative, field-level mapping** from **authoritative STAC Items & Collections** to **derived DCAT records** in the Kansas Frontier Matrix, implementing the **STAC-first → DCAT-derived** model under FAIR+CARE and sovereignty governance.

</div>

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 standards/
        └── 📁 catalogs/
            ├── 📄 README.md                         📚 Catalog & metadata standards index
            ├── 📦 stac-dcat-derivation.md           📦 STAC → DCAT derivation model
            │
            └── 📁 crosswalks/                       🔀 Catalog crosswalk standards subtree
                ├── 📄 README.md                      📚 Crosswalks index
                ├── 📄 stac-dcat-crosswalk.md         🔁 This file (STAC → DCAT field-level crosswalk)
                ├── 📄 stac-ckan-crosswalk.md         🔁 STAC → CKAN / portal crosswalk
                │
                └── 📁 profiles/                      🧩 Domain-specific crosswalk profiles
                    ├── 📄 stac-dcat-hydro-profile.md    💧 Hydrology crosswalk profile
                    └── 📄 stac-dcat-archaeo-profile.md  🏺 Archaeology / heritage crosswalk profile
~~~

**Directory rules**

- All docs under `docs/standards/catalogs/crosswalks/` are **normative** for KFM cross-model mappings.  
- Implementations in `src/**` MUST reference these docs by path and version in comments, configs, or provenance.  
- Any new crosswalk spec or profile requires:
  - FAIR+CARE review  
  - governance ledger entry  
  - an update to this directory layout in the index README.

---

## 📘 Overview

This crosswalk is the **primary, normative mapping** for catalog metadata and must be read alongside:

- `../README.md` — catalog crosswalks standards index.  
- `../stac/README.md` and `../stac/stac-kfm-profile.md` — KFM STAC standards & profile.  
- `../stac/stac-best-practices.md` — STAC authoring best practices.  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived architecture.  
- `../dcat/dcat-kfm-profile.md` — KFM DCAT profile.  
- Domain STAC extensions (e.g., `stac-ext-kfm-core.md`, `stac-ext-faircare.md`).

**KFM position**

- STAC is the **only authoritative geospatial metadata layer**.  
- DCAT is **derived exclusively** from validated STAC via the crosswalk logic described here.  
- No production DCAT may be hand-authored or maintained independently of STAC.

---

## 🧭 General Crosswalk Principles

1. **One-way, STAC-first**

   - Mapping direction is **STAC → DCAT only**.  
   - No DCAT → STAC backfills or “roundtrips”.

2. **Minimal loss of semantics**

   - Preserve:
     - identifiers  
     - spatial / temporal coverage  
     - licenses & rights  
     - asset semantics (format, role, checksum)  
   - Where DCAT lacks an exact construct, use the **closest sound pattern** or omit.

3. **Governance alignment**

   - FAIR+CARE and sovereignty fields determine:
     - which STAC records yield DCAT `dcat:Dataset`s  
     - which assets become `dcat:Distribution`s  
   - Sensitive / internal-only information is **never** leaked.

4. **Stable identifiers**

   - Identifiers and URIs are stable, dereferenceable, and non-conflicting.  
   - Crosswalk code MUST NOT generate inconsistent IDs for the same dataset over time.

5. **Deterministic & testable**

   - Given:
     - a STAC record  
     - a crosswalk version  
   - the DCAT output MUST be deterministic and regression-testable.

---

## 📦 STAC → DCAT Dataset Mapping

This section covers mapping from **STAC Items/Collections** to **`dcat:Dataset`**.

### 3.1 Identity & Title

| DCAT Field       | Requirement | STAC Source (conceptual)                                            |
|------------------|------------|---------------------------------------------------------------------|
| `@id`            | REQUIRED   | Derived from `kfm:dataset_id` or STAC `id` in a KFM IRI pattern.    |
| `dct:identifier` | REQUIRED   | STAC `id` (Item or Collection) or `kfm:dataset_id` (preferred when present). |
| `dct:title`      | REQUIRED   | STAC `properties.title` or Collection `title` (fallback: `id`).     |

**Recommended `@id` pattern**

- Collection-level dataset:

  ~~~text
  urn:kfm:dataset:<collection-id>
  ~~~

- Item-level dataset (if Items are modeled separately):

  ~~~text
  urn:kfm:dataset:<collection-id>:<item-id>
  ~~~

The exact `@id` scheme MUST be documented in `stac-dcat-derivation.md` and implemented consistently.

### 3.2 Description

| DCAT Field        | Requirement | STAC Source                          |
|-------------------|------------|---------------------------------------|
| `dct:description` | REQUIRED   | STAC `properties.description` or Collection `description`. |

Guidelines:

- Provide **clear, concise** prose.  
- Long-form documentation should be linked via `dcat:landingPage` or other metadata, not embedded wholesale.

### 3.3 Spatial Extent (`dct:spatial`)

| DCAT Field   | Requirement | STAC Source                        |
|--------------|------------|-------------------------------------|
| `dct:spatial`| REQUIRED   | STAC `bbox` or `extent.spatial`.   |

Pattern:

~~~json
"dct:spatial": {
  "@type": "dct:Location",
  "bbox": [-102.0, 36.99, -94.6, 40.01]
}
~~~

Rules:

- For Item-based datasets:
  - Use the Item’s `bbox`.  
- For Collection-based datasets:
  - Use `extent.spatial.bbox` from the Collection.  
- If STAC has been generalized (e.g., for heritage), `dct:spatial` MUST use the **generalized** extent.

### 3.4 Temporal Extent (`dct:temporal`)

| DCAT Field     | Requirement | STAC Source                                     |
|----------------|------------|-------------------------------------------------|
| `dct:temporal` | REQUIRED   | Item `datetime` / interval OR Collection `extent.temporal`. |

Pattern:

~~~json
"dct:temporal": {
  "@type": "dct:PeriodOfTime",
  "dcat:startDate": "2025-05-01T00:00:00Z",
  "dcat:endDate": "2025-05-31T23:59:59Z"
}
~~~

Rules:

- Instantaneous Item:
  - `startDate` = `endDate` = `properties.datetime`.  
- Interval Item:
  - Use `properties.start_datetime` / `properties.end_datetime`.  
- Collection:
  - Use earliest start and latest end from `extent.temporal.interval`.

### 3.5 Keywords & Themes

| DCAT Field      | Requirement | STAC Source                         |
|-----------------|------------|--------------------------------------|
| `dcat:keyword`  | RECOMMENDED| STAC `keywords` and KFM domain tags. |

Sources:

- STAC `keywords`.  
- `kfm:domain`, `kfm:subdomain`.  
- Domain extension fields (e.g., `kfmclim:variable`, `kfmhydro:variable`, `kfmarch:period`).

Guidelines:

- Normalize to short, lowercase keywords.  
- For controlled vocabularies (e.g., INSPIRE, GCMD), specify vocabularies in `dcat-kfm-profile.md`.

### 3.6 Publisher & Creator

| DCAT Field      | Requirement | STAC Source (via `providers`)             |
|-----------------|------------|-------------------------------------------|
| `dct:publisher` | RECOMMENDED| First provider with role `producer`/`licensor`. |
| `dct:creator`   | RECOMMENDED| Providers with roles `producer`, `processor`, `host`. |

Pattern:

~~~json
"dct:publisher": {
  "@type": "foaf:Agent",
  "foaf:name": "NOAA"
}
~~~

KFM’s own roles (e.g., as `processor` or `host`) SHOULD appear in `dct:creator` when appropriate.

### 3.7 Landing Page

| DCAT Field         | Requirement | Source / Rule                                 |
|--------------------|------------|-----------------------------------------------|
| `dcat:landingPage` | RECOMMENDED| KFM dataset portal URL for human exploration. |

Typically derived from:

- KFM portal route + dataset identifier.  
- NOT directly from STAC API URLs.

---

## 📦 STAC Asset → DCAT Distribution Mapping

For each STAC Asset that should be discoverable, create a `dcat:Distribution`.

### 4.1 URL & Access

| DCAT Field              | Requirement | STAC Source                      |
|-------------------------|------------|----------------------------------|
| `dcat:downloadURL`      | REQUIRED¹  | Asset `href` (direct-downloadable assets). |
| `dcat:accessURL`        | REQUIRED¹  | Asset `href` (service endpoints / catalogs). |

¹ At least one of `downloadURL` or `accessURL` MUST be provided.

Guidelines:

- Use `downloadURL` for direct, file-based assets.  
- Use `accessURL` for services (e.g., APIs, tile services, STAC sub-catalogs).

### 4.2 Format & Media Type

| DCAT Field        | Requirement | STAC Source             |
|-------------------|------------|-------------------------|
| `dct:format`      | REQUIRED   | Asset `type` (MIME).    |
| `dcat:mediaType`  | OPTIONAL   | Same MIME, if required. |

If downstream DCAT consumers rely on `dcat:mediaType`, set both fields.

### 4.3 Titles & Descriptions

| DCAT Field        | Requirement | STAC Source                   |
|-------------------|------------|-------------------------------|
| `dct:title`       | RECOMMENDED| Asset `title` or derived label. |
| `dct:description` | OPTIONAL   | Asset description or contextual text. |

Example:

~~~json
{
  "@type": "dcat:Distribution",
  "dct:title": "NAIP 2023 Tile 001 (GeoTIFF)",
  "dcat:downloadURL": "https://example.com/naip_001.tif",
  "dct:format": "image/tiff; application=geotiff"
}
~~~

### 4.4 Checksums

| DCAT Field      | Requirement | STAC Source                  |
|-----------------|------------|------------------------------|
| `spdx:checksum` | RECOMMENDED| Asset `checksum:sha256`.     |

Pattern:

~~~json
"spdx:checksum": {
  "@type": "spdx:Checksum",
  "spdx:algorithm": "sha256",
  "spdx:checksumValue": "abc123..."
}
~~~

Multiple checksum algorithms MAY be supported via additional `spdx:Checksum` objects if present in STAC.

---

## 🌐 FAIR+CARE & Sovereignty in the Crosswalk

### 5.1 Eligibility Filter

Before STAC → DCAT derivation, Apply FAIR+CARE / sovereignty filters:

- Exclude from **public DCAT**:
  - datasets with `kfmfc:sensitivity = "restricted-internal"` or equivalent.  
- Include in public DCAT only when:
  - `kfmfc:sensitivity` is in governance-approved values (e.g., `general`, `restricted-generalized`).  
  - `kfmfc:care_label` and sovereignty flags permit public or partner exposure.

Internal-only DCAT MAY exist for restricted environments (e.g., internal catalogs).

### 5.2 Visibility Rules for Assets

Use `kfmfc:visibility_rules` and domain-specific flags to decide:

- Which assets become public `dcat:Distribution`s.  
- Which assets remain internal-only, even if the dataset is discoverable.

Examples:

- Heritage:
  - Only generalized H3 or region-level products become Distributions.  
- Climate / hydrology:
  - Raw internal QC diagnostics are excluded from public DCAT.

### 5.3 Governance → DCAT Fields

Where supported by `dcat-kfm-profile.md`, governance / FAIR+CARE hints MAY appear as:

- `dcat:keyword` terms (e.g., `FAIR+CARE`, `Community-Controlled`).  
- Profile-specific properties (e.g., `kfmfc:care_label`) when modeled in DCAT extensions.

These MUST NOT contradict the underlying STAC governance fields.

---

## 🧬 Domain-Specific Crosswalk Notes

These examples complement, but do not override, the core mapping rules.

### 6.1 Climate (`kfm-climate`)

- `kfmclim:variable` → `dcat:keyword` (e.g., `precipitation`, `temperature`).  
- `kfmclim:vertical_level` → keywords or description text.  
- `kfmclim:temporal_aggregation` → keywords / description (e.g., `daily-mean`, `hourly-accumulation`).

### 6.2 Hydrology (`kfm-hydrology`)

- `kfmhydro:variable` → `dcat:keyword` (e.g., `discharge`, `stage`).  
- `kfmhydro:watershed_id` / `river_id` → `dcat:keyword` or part of `dct:description`.  
- Internal-only IDs (e.g., `kfmhydro:gauge_id_internal`) MUST NOT be exposed in DCAT.

### 6.3 Archaeology / Heritage (`kfm-archaeology`, `kfm-heritage`)

- `kfmarch:period`, `kfmarch:culture_phase` → `dcat:keyword` / description augmentation.  
- `kfmarch:sensitivity_class` + `kfmfc:sensitivity` control:
  - whether any public DCAT exists at all (e.g., aggregated region-only products).  
  - the strength of spatial generalization required.

Heritage DCAT datasets MUST NOT expose site-level identifiers or fine-grained geometries.

---

## 🧪 Validation & CI Expectations

DCAT outputs produced via this crosswalk MUST satisfy:

### 7.1 Profile Validation

- Validate against:
  - DCAT 3.0 schemas, and  
  - KFM DCAT SHACL shapes (`dcat-kfm-profile`).

### 7.2 Crosswalk Consistency

Consistency checks MUST ensure:

- `dct:identifier` matches STAC `id` / `kfm:dataset_id` consistently.  
- `dct:spatial` and `dct:temporal` match STAC extents (within expected generalization).  
- Every `dcat:Distribution` URL corresponds to a STAC Asset `href`.  
- No DCAT fields reference non-existent STAC fields.

### 7.3 Governance Checks

Before publishing DCAT into a public catalog:

- Confirm **no** `restricted-internal` datasets were included.  
- Confirm asset-level visibility rules obey FAIR+CARE & sovereignty constraints.  
- Confirm internal-only IDs, codes, or sensitive descriptions do not appear in DCAT.

### 7.4 CI Workflows & Telemetry

Typical CI workflow:

- `catalog-crosswalk-validate.yml`:
  - runs STAC validation  
  - runs crosswalk transforms to DCAT  
  - runs DCAT profile validation  
  - runs governance filters and checks

Telemetry written to:

- `catalog-metadata-telemetry.json` (see `telemetry_ref`), recording:
  - counts of STAC datasets processed  
  - counts of DCAT datasets emitted  
  - validation errors and warning categories

---

## ✅ Implementation Checklist

When implementing or updating STAC → DCAT crosswalk code:

1. **Bind to KFM STAC profile**

   - Assume only STAC conforming to `stac-kfm-profile.md` is input.  
   - Enforce extension expectations (e.g., KFM mission tags).

2. **Implement mapping tables**

   - Dataset-level and Distribution-level mappings as specified here.  
   - Keep mapping logic table-driven where possible for transparency.

3. **Apply FAIR+CARE & sovereignty filters**

   - Filter out ineligible datasets and assets prior to DCAT generation.  
   - Respect domain-specific sensitivity and visibility flags.

4. **Validate in CI**

   - Use KFM DCAT profile and this spec as test oracles.  
   - Add regression fixtures for:
     - imagery  
     - climate  
     - hydrology  
     - heritage (aggregated/generalized)

5. **Maintain provenance**

   - Record crosswalk operations as PROV activities:
     - STAC Entity → DCAT Entity  
     - Crosswalk script/tool as `prov:SoftwareAgent`  
   - Ensure telemetry and governance ledgers reference the crosswalk version.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.6  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Aligned with KFM‑MDP v11.2.6; updated release and schema references; clarified directory layout and CI expectations while preserving v11.2.3 semantics. |
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial STAC → DCAT crosswalk spec; defined dataset/distribution mapping, governance-aware filtering, domain-specific notes, and CI validation expectations under the STAC-first → DCAT-derived model. |

---

<sub>© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🔁 **KFM v11.2.6 — STAC → DCAT Crosswalk**  
STAC-First Catalogs · DCAT-Derived Discovery · Governed Crosswalks  

[📚 Catalog Standards Index](../README.md) · [📦 STAC → DCAT Derivation](../stac-dcat-derivation.md) · [⚖ Governance Charter](../../governance/ROOT-GOVERNANCE.md)

</div>