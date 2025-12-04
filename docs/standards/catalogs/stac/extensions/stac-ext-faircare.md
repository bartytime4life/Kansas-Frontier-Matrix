---
title: "🛡️ KFM v11.2.3 — STAC Extension: FAIR+CARE & Sovereignty (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "KFM STAC extension capturing FAIR+CARE, sensitivity, and sovereignty metadata on Items and Collections."
path: "docs/standards/catalogs/stac/extensions/stac-ext-faircare.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x extension-profile compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:stac-ext-faircare-v11.2.3"
semantic_document_id: "kfm-stac-ext-faircare-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:extensions:faircare:v11.2.3"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "STAC Extension Spec"
intent: "catalogs-stac-ext-faircare"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: true
public_benefit_level: "High"
risk_category: "Moderate"
redaction_required: true

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/stac/stac-ext-faircare-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/stac-ext-faircare-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major FAIR+CARE extension revision"
---

<div align="center">

# 🛡️ STAC Extension — FAIR+CARE & Sovereignty (`kfm-faircare`)  
`docs/standards/catalogs/stac/extensions/stac-ext-faircare.md`

**Namespace:** `https://schema.kfm.dev/stac/faircare/1.0`  
**Prefix:** `kfmfc`

**Purpose:**  
Attach **FAIR+CARE** and **sovereignty** metadata directly to STAC Items and Collections so that governance-aware behavior can be enforced consistently in **ETL**, **catalogs**, and **web applications**.

</div>

---

## 📘 1. Scope

The `kfm-faircare` extension:

- Applies to **STAC Items and Collections**.  
- Encodes:
  - Sensitivity and FAIR+CARE labels.  
  - Sovereignty flags and notes.  
  - High-level visibility rules used by downstream systems.

This metadata supports:

- Public vs internal catalog decisions.  
- Web governance hooks (Cesium, MapLibre, other viewers).  
- Downstream STAC → DCAT derivation and portal behavior.

It must be used **together with** higher-level governance documents:

- `faircare_ref` — FAIR+CARE policy  
- `sovereignty_ref` — Indigenous data & sovereignty policy  

---

## 🧱 2. Fields

### 2.1 Item/Collection Fields

| Field                     | Type      | Card. | Description |
|---------------------------|-----------|-------|-------------|
| `kfmfc:sensitivity`       | string    | 1     | Sensitivity class, e.g. `general`, `mixed`, `restricted-generalized`, `restricted-internal`. |
| `kfmfc:care_label`        | string    | 1     | FAIR+CARE label, e.g. `Public`, `Community-Controlled`, `Restricted`, `Internal`. |
| `kfmfc:sovereignty_flag`  | boolean   | 1     | `true` if dataset is subject to sovereignty / Indigenous data governance. |
| `kfmfc:sovereignty_notes` | string    | 0..1  | Short notes describing sovereignty obligations or agreements. |
| `kfmfc:visibility_rules`  | string    | 0..1  | High-level visibility rule, e.g. `polygon-generalized`, `h3-only`, `no-exact-boundaries`. |
| `kfmfc:governance_ref`    | string    | 0..1  | URI/URN pointing to a detailed governance document for this dataset. |

### 2.2 Recommended Value Sets

**`kfmfc:sensitivity`** (illustrative):

- `general` — safe for public without additional generalization.  
- `mixed` — contains both general and sensitive elements; must be handled carefully.  
- `restricted-generalized` — generalized enough for some public/community views, but core data are sensitive.  
- `restricted-internal` — internal-only; no public release.

**`kfmfc:care_label`** (aligned with FAIR+CARE):

- `Public`  
- `Community-Controlled`  
- `Restricted`  
- `Internal`

**`kfmfc:visibility_rules`** (aligned with web governance docs):

- `polygon-generalized` — only generalized polygons in public contexts.  
- `h3-only` — only H3 cell aggregates in public contexts.  
- `no-exact-boundaries` — approximate shading, no crisp boundaries.

Final value sets must be documented in a shared vocabulary and enforced in schema/CI.

---

## 🔗 3. Relationship to Other Extensions

The `kfm-faircare` extension is intended to be used:

- Alongside **`kfm-core`** (`stac-ext-kfm-core.md`):  
  - `kfm:dataset_id`, `kfm:domain`, and `kfm:region_slug` locate and classify the dataset; `kfmfc:*` describes its governance.

- Alongside **domain extensions** (e.g., `kfm-archaeology`, `kfm-climate`):  
  - Domain-specific sensitivity (`kfmarch:sensitivity_class`) must **refine**, not contradict, `kfmfc:sensitivity`.

Downstream consumers (e.g. Cesium, discovery portals) must check **both**:

- Generic FAIR+CARE fields (`kfmfc:*`).  
- Any domain-specific refinements (e.g., `kfmarch:sensitivity_class`).

---

## 🧾 4. Example Usage (Collection-Level FAIR+CARE Metadata)

~~~json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "archaeology_cultural_regions_v1",
  "properties": {
    "kfmfc:sensitivity": "restricted-generalized",
    "kfmfc:care_label": "Community-Controlled",
    "kfmfc:sovereignty_flag": true,
    "kfmfc:sovereignty_notes": "Generalized cultural regions only; site-level information governed by tribal protocols.",
    "kfmfc:visibility_rules": "h3-only",
    "kfmfc:governance_ref": "https://kfm.dev/governance/archaeology-cultural-regions-v1"
  },
  "extent": {
    "spatial": { "...": "..." },
    "temporal": { "...": "..." }
  }
}
~~~

> **Governance note:**  
> This Collection is explicitly tagged as **sovereignty-governed**, with visibility constrained to **H3-only** representations in public contexts.

---

## 🌐 5. Web & Catalog Behavior

Downstream tools (web viewers, catalogs, APIs) should interpret `kfmfc:*` fields as follows:

- `kfmfc:sensitivity` and `kfmfc:care_label`  
  - Decide **whether** a dataset appears in public catalogs, and at what level of generalization.

- `kfmfc:visibility_rules`  
  - Decide **how** the dataset appears:
    - Use generalized polygons vs H3 vs shading.  
    - Determine zoom thresholds and interactive behavior.

- `kfmfc:sovereignty_flag` and `kfmfc:sovereignty_notes`  
  - Trigger **sovereignty-specific safeguards**:
    - Additional review for public use.  
    - Restricted access in some contexts.  
    - Specific explanatory text in UI.

- `kfmfc:governance_ref`  
  - Provide a target for “**Why am I seeing this?**” or governance information panels.

For concrete enforcement patterns, see:

- `web/cesium/docs/governance-hooks.md`  
- The relevant 2D map governance docs (if present).

---

## 🧪 6. Validation & CI Requirements

**Schema:**  
- `stac-ext-faircare-v1.schema.json` must be used alongside the core STAC schema and any KFM extension schemas.

**CI rules** (indicative):

- If any `kfmfc:*` fields are present:
  - `kfmfc:sensitivity` and `kfmfc:care_label` MUST be present.  
  - `kfmfc:sovereignty_flag` MUST be present (explicitly `true` or `false`).  
  - `kfmfc:visibility_rules` should be one of the allowed values (or omitted).

- Optional but recommended checks:
  - Ensure **sensitivity and visibility rules are consistent** with directory-level expectations (e.g., sensitive archaeologic datasets under protected regions).  
  - Validate that sovereign datasets (`kfmfc:sovereignty_flag = true`) have non-empty `kfmfc:sovereignty_notes` or a `kfmfc:governance_ref`.

CI job (indicative):

- `catalog-stac-extensions-validate.yml` must:
  - Validate extension fields against schema.  
  - Flag suspicious or inconsistent combinations of `kfmfc:*` fields.

---

## 🔁 7. Interaction with STAC → DCAT Crosswalks

In KFM’s STAC-first → DCAT-derived model, `kfmfc:*` fields influence DCAT in two ways:

1. **Public/Private Decisions**  
   - Datasets with `kfmfc:sensitivity = "restricted-internal"` may be:
     - Excluded from public DCAT exports.  
     - Present only in internal catalogs.

2. **DCAT Fields (where appropriate)**  
   - Some `kfmfc:*` content may map to DCAT or related vocabularies:
     - e.g., sensitivity and CARE labels becoming:
       - `dcat:keyword` values, or  
       - extensions in a DCAT profile for governance metadata.

Crosswalk rules must be documented in:

- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`  

and implemented in the **STAC → DCAT** pipelines.

---

## ✅ 8. Implementation Checklist

When using the `kfm-faircare` extension for a dataset:

1. **Set generic governance fields:**
   - `kfmfc:sensitivity`  
   - `kfmfc:care_label`  
   - `kfmfc:sovereignty_flag`

2. **Set visibility & governance references as appropriate:**
   - `kfmfc:visibility_rules` (if spatial generalization or masking rules are in place)  
   - `kfmfc:sovereignty_notes`  
   - `kfmfc:governance_ref` (for detailed policies)

3. **Align with domain extensions:**
   - Ensure domain-specific sensitivity (e.g., `kfmarch:sensitivity_class`) refines, not contradicts, `kfmfc:sensitivity`.

4. **Validate:**
   - Use `stac-validator` with this extension’s schema.  
   - Ensure CI passes for all Items/Collections using `kfm-faircare`.

5. **Derive DCAT safely:**
   - Confirm crosswalk logic respects FAIR+CARE and sovereignty fields.  
   - Avoid leaking internal-only datasets into public DCAT outputs.

---

## 🕰️ 9. Version History

| Version | Date       | Summary                                                                 |
|---------|------------|-------------------------------------------------------------------------|
| v1.0.0  | 2025-12-03 | Initial FAIR+CARE & sovereignty STAC extension; aligned with KFM v11.2.3, STAC-first catalog model, and web governance hooks. |

