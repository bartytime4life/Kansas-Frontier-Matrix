---
title: "🔁 KFM v11.2.3 — STAC → DCAT Crosswalk (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Normative field-level crosswalk for deriving DCAT from authoritative STAC records in the Kansas Frontier Matrix, under the STAC-first → DCAT-derived model."
path: "docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 2.x/3.0 crosswalk-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-crosswalks-stac-dcat-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-crosswalks-stac-dcat-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:crosswalks:stac-dcat:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

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

json_schema_ref: "../../../schemas/json/catalogs-stac-dcat-crosswalk-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-stac-dcat-crosswalk-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC → DCAT crosswalk revision"
---

<div align="center">

# 🔁 Kansas Frontier Matrix — STAC → DCAT Crosswalk  
`docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

**Purpose:**  
Define the **normative, field-level mapping** from **authoritative STAC Items & Collections** to **derived DCAT records** in the Kansas Frontier Matrix, implementing the **STAC-first → DCAT-derived** model under FAIR+CARE + sovereignty governance.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

This crosswalk is the **primary, normative mapping** for catalog metadata and must be read alongside:

- `../README.md` — catalog crosswalks index.  
- `../stac/README.md` and `../stac/stac-kfm-profile.md` — KFM STAC standards & profile.  
- `../stac/stac-best-practices.md` — STAC authoring best practices.  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived architecture.  
- `../dcat/dcat-kfm-profile.md` — KFM DCAT profile.  
- Domain STAC extensions (`stac-ext-kfm-core.md`, `stac-ext-faircare.md`, etc.).

**KFM position:**

- STAC is the **only authoritative** geospatial metadata layer.  
- DCAT is **derived exclusively** from validated STAC via the crosswalk logic described here.  
- No production DCAT may be hand-authored or maintained independent of STAC.

---

## 🧭 2. General Crosswalk Principles

1. **One-way, STAC-first**  
   - STAC → DCAT only.  
   - No DCAT → STAC backfills.

2. **Minimal loss of semantics**  
   - Preserve identifiers, spatial/temporal coverage, licensing, and asset semantics.  
   - When DCAT lacks an exact construct, map to the **closest sound pattern** or omit.

3. **Governance alignment**  
   - FAIR+CARE and sovereignty fields determine:
     - Which STAC records yield DCAT records.  
     - Which assets become `dcat:Distribution`s.  
   - Sensitive/internal-only information is **never** leaked.

4. **Stable identifiers**  
   - Identifiers and URIs are stable and resolvable.  
   - Crosswalk must not generate conflicting or ambiguous IDs.

---

## 📦 3. STAC → DCAT Dataset Mapping

This section covers the mapping from **STAC Items/Collections** to **`dcat:Dataset`**.

### 3.1 Identity & Title

| DCAT Field        | Requirement | STAC Source (conceptual)                                            |
|-------------------|------------|---------------------------------------------------------------------|
| `@id`             | REQUIRED   | Derived from `kfm:dataset_id` or STAC `id` in a KFM IRI pattern.    |
| `dct:identifier`  | REQUIRED   | STAC `id` (Item or Collection) or `kfm:dataset_id` when preferred. |
| `dct:title`       | REQUIRED   | STAC `properties.title` or Collection `title` (fallback to `id`).   |

**Recommended pattern for `@id`:**

- Collection-level dataset:

  ~~~text
  urn:kfm:dataset:<collection-id>
  ~~~

- Item-level dataset (if modeling Items as separate DCAT Datasets):

  ~~~text
  urn:kfm:dataset:<collection-id>:<item-id>
  ~~~

The exact pattern MUST be documented and stable in implementation code.

### 3.2 Description

| DCAT Field        | Requirement | STAC Source                        |
|-------------------|------------|-------------------------------------|
| `dct:description` | REQUIRED   | STAC `properties.description` or Collection `description`. |

Guidelines:

- Use **concise prose** suitable for portals.  
- Long-form documentation should be linked via `dcat:landingPage` or additional metadata.

### 3.3 Spatial Extent (`dct:spatial`)

| DCAT Field   | Requirement | STAC Source                      |
|--------------|------------|-----------------------------------|
| `dct:spatial`| REQUIRED   | STAC `bbox` or `extent.spatial`. |

Pattern:

~~~json
"dct:spatial": {
  "@type": "dct:Location",
  "bbox": [-102.0, 36.99, -94.6, 40.01]
}
~~~

Rules:

- Source `bbox` from:
  - Item `bbox` for Item-based datasets.  
  - Collection `extent.spatial.bbox` for Collection-based datasets.  
- Bbox must reflect **generalized extents** if STAC geometry has been generalized for sensitivity reasons.

### 3.4 Temporal Extent (`dct:temporal`)

| DCAT Field      | Requirement | STAC Source                                      |
|-----------------|------------|-------------------------------------------------|
| `dct:temporal`  | REQUIRED   | Item `datetime` / interval OR Collection `extent.temporal`. |

Pattern:

~~~json
"dct:temporal": {
  "@type": "dct:PeriodOfTime",
  "dcat:startDate": "2025-05-01T00:00:00Z",
  "dcat:endDate": "2025-05-31T23:59:59Z"
}
~~~

Rules:

- Instantaneous item:
  - Start/end both equal `properties.datetime`.  
- Interval item:
  - Use `properties.start_datetime` / `end_datetime`.  
- Collection:
  - Use earliest start and latest end from `extent.temporal.interval`.

### 3.5 Keywords & Themes

| DCAT Field      | Requirement    | STAC Source                           |
|-----------------|----------------|----------------------------------------|
| `dcat:keyword`  | RECOMMENDED    | STAC `keywords`, domain tags, extensions. |

Sources:

- STAC `keywords`.  
- `kfm:domain`, `kfm:subdomain`.  
- Domain extension fields (e.g., `kfmclim:variable`, `kfmhydro:variable`, `kfmarch:period`).

Guidelines:

- Normalize to lowercase short strings for general keywords.  
- Reserved/theme vocabularies (e.g., INSPIRE, GCMD) must be documented if used.

### 3.6 Publisher & Creator

| DCAT Field       | Requirement | STAC Source (via `providers`)               |
|------------------|------------|---------------------------------------------|
| `dct:publisher`  | RECOMMENDED| First provider with role `producer`/`licensor`. |
| `dct:creator`    | RECOMMENDED| List of providers with roles `producer`, `processor`, `host`. |

Pattern:

~~~json
"dct:publisher": {
  "@type": "foaf:Agent",
  "foaf:name": "NOAA"
}
~~~

Where KFM modifies or adds providers (e.g., as `processor`/`host`), these should show up in `dct:creator`.

### 3.7 Landing Page

| DCAT Field       | Requirement | Source / Rule                             |
|------------------|------------|-------------------------------------------|
| `dcat:landingPage` | RECOMMENDED | KFM dataset portal URL for human exploration. |

This is typically built from:

- Dataset identifier (KFM portal route pattern).  
- NOT directly from STAC `self` links (those are STAC API references).

---

## 📦 4. STAC Asset → DCAT Distribution Mapping

For each STAC Asset that should be discoverable:

### 4.1 URL & Access

| DCAT Field             | Requirement | STAC Source                  |
|------------------------|------------|------------------------------|
| `dcat:downloadURL` or `dcat:accessURL` | REQUIRED   | Asset `href`                 |

Guidelines:

- Use `dcat:downloadURL` for direct file downloads.  
- Use `dcat:accessURL` for services or catalogs (e.g., STAC sub-catalogs, API endpoints).

### 4.2 Format & Media Type

| DCAT Field      | Requirement | STAC Source            |
|-----------------|------------|------------------------|
| `dct:format`    | REQUIRED   | Asset `type` (MIME).   |
| `dcat:mediaType`| OPTIONAL   | Same or refined MIME.  |

If DCAT consumers rely on `dcat:mediaType`, set both `dct:format` and `dcat:mediaType`.

### 4.3 Titles & Descriptions

| DCAT Field       | Requirement | STAC Source                   |
|------------------|------------|-------------------------------|
| `dct:title`      | RECOMMENDED| Asset `title` or derived label. |
| `dct:description`| OPTIONAL   | Asset description or context. |

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

---

## 🌐 5. FAIR+CARE & Sovereignty in the Crosswalk

### 5.1 Eligibility Filter

Before STAC → DCAT conversion:

- Filter Items/Collections using `kfm-faircare` and domain extensions:

  - Exclude from **public DCAT**:
    - `kfmfc:sensitivity = "restricted-internal"`.  
  - Only include for public DCAT:
    - `kfmfc:sensitivity` in permitted values (e.g., `general`, some `restricted-generalized` with approval).

### 5.2 Visibility Rules

Use `kfmfc:visibility_rules` and domain-specific equivalents to:

- Decide which Assets become Distributions:
  - For `h3-only`, include only H3/aggregate assets in public DCAT.  
  - For `no-exact-boundaries`, avoid distributions that implicitly reveal precise boundaries.

### 5.3 Mapping Governance to DCAT

Optionally, crosswalk may:

- Expose governance hints as:
  - `dcat:keyword` (e.g., `FAIR+CARE`, `Community-Controlled`).  
  - Profile-specific properties (in a KFM DCAT extension), if defined in `dcat-kfm-profile.md`.

But:

- Must never contradict `kfmfc:*` fields.  
- Must not imply a dataset is `Public` when STAC says otherwise.

---

## 🧬 6. Domain-Specific Crosswalk Notes

### 6.1 Climate (`kfm-climate`)

Examples:

- `kfmclim:variable` → `dcat:keyword` (e.g., `precipitation`, `temperature`).  
- `kfmclim:vertical_level` → `dcat:keyword` or `dct:description` augmentation.  
- `kfmclim:temporal_aggregation` → included in description or keywords to indicate averaging/accumulation.

### 6.2 Hydrology (`kfm-hydrology`)

Examples:

- `kfmhydro:variable` → `dcat:keyword` (e.g., `discharge`, `stage`).  
- `kfmhydro:watershed_id` / `river_id` → `dcat:keyword` or `dct:spatial` context notes.  
- Internal-only IDs (e.g., `kfmhydro:gauge_id_internal`) MUST **not** be surfaced in DCAT.

### 6.3 Archaeology (`kfm-archaeology`)

Examples:

- `kfmarch:period`, `kfmarch:culture_phase` → `dcat:keyword` or description augmentation.  
- `kfmarch:sensitivity_class` interplay with `kfmfc:sensitivity` to decide:
  - Whether DCAT is produced at all.  
  - How strongly spatial generalization is enforced.

Sensitive archaeology data should only be exposed as:

- Aggregated/landscape-level DCAT Datasets.  
- With no site-level or internal IDs.

---

## 🧪 7. Validation & CI Expectations

DCAT outputs must satisfy:

1. **Profile validation**  
   - Against KFM DCAT SHACL shapes (`dcat-kfm-profile-v1.shape.ttl`).  

2. **Crosswalk consistency checks**  
   - Confirm that:
     - `dct:identifier` aligns with STAC ID / `kfm:dataset_id`.  
     - Spatial/temporal extents are consistent with STAC.  
     - Every DCAT Distribution’s URL is present in some STAC Asset.  

3. **Governance checks**  
   - Validate:

     - No `restricted-internal` datasets appear in public DCAT.  
     - Distributions in public DCAT respect `visibility_rules`.  
     - No internal-only fields (e.g., site/gauge IDs) appear.

CI workflow (indicative):

- `catalog-crosswalk-validate.yml`  
  - Uses example STAC fixtures → crosswalk code → DCAT → validates against SHACL and governance rules.

Telemetry written to:

- `catalog-metadata-telemetry.json` with:
  - Counts of datasets processed/filtered.  
  - Validation error counts and categories.

---

## ✅ 8. Implementation Checklist

When implementing or updating STAC → DCAT crosswalk code:

1. **Bind to KFM STAC profile**  
   - Assume only STAC conforming to `stac-kfm-profile.md` is input.  

2. **Implement mapping tables**  
   - Dataset-level and Distribution-level mappings exactly as defined above.  

3. **Apply FAIR+CARE & sovereignty filters**  
   - Filter out ineligible datasets and assets ahead of DCAT generation.  

4. **Validate in CI**  
   - Use this spec’s mapping and KFM DCAT profile as test oracles.  
   - Add regression tests for multiple domains (imagery, climate, hydrology, archaeology).

5. **Maintain provenance**  
   - Ensure crosswalk operations are logged and PROV-O relationships STAC → DCAT are maintained.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial STAC → DCAT crosswalk spec; defined dataset/distribution mapping, governance-aware filtering, domain-specific notes, and CI validation expectations under the STAC-first → DCAT-derived model. |

