---
title: "🌐 KFM v11.2.3 — DCAT Federation Guidelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Guidelines for safely federating KFM DCAT metadata with external catalogs and portals under the STAC-first → DCAT-derived model."
path: "docs/standards/catalogs/dcat/dcat-federation-guidelines.md"
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

doc_uuid: "urn:kfm:doc:standards-catalogs-dcat-federation-guidelines-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-dcat-federation-guidelines-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:dcat:federation-guidelines:v11.2.3"

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

doc_kind: "Standards Guidance"
intent: "catalogs-dcat-federation-guidelines"
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
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/catalogs-dcat-federation-guidelines-v1.json"
shape_schema_ref: "../../schemas/shacl/catalogs-dcat-federation-guidelines-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major DCAT federation guidelines revision"
---

<div align="center">

# 🌐 Kansas Frontier Matrix — DCAT Federation Guidelines  
`docs/standards/catalogs/dcat/dcat-federation-guidelines.md`

**Purpose:**  
Define **governed patterns** for federating **KFM DCAT metadata** with external catalogs and portals (national/state data portals, CKAN instances, research exchanges) under the **STAC-first → DCAT-derived** model and **FAIR+CARE + sovereignty** constraints.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

These guidelines apply whenever KFM DCAT is:

- Exported to, or harvested by, external catalogs.  
- Used to power shared search portals.  
- Published as Linked Data endpoints.

This document is **guidance** and must be read alongside:

- `dcat/README.md` — DCAT standards index.  
- `dcat-kfm-profile.md` — KFM DCAT profile (normative).  
- `dcat-examples.md` — example DCAT records.  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived model.  
- `../crosswalks/stac-dcat-crosswalk.md` — field-level mappings.  
- FAIR+CARE & sovereignty docs referenced via `faircare_ref` and `sovereignty_ref`.

**KFM position:**

- **Only derived DCAT** from validated STAC is eligible for federation.  
- Federation MUST respect KFM **governance, FAIR+CARE, and sovereignty** requirements.

---

## 🔁 2. Federation Models

KFM supports three primary DCAT federation patterns:

1. **Push (export)**  
   - KFM periodically **pushes DCAT** dumps or records to partner catalogs.  

2. **Pull (harvest)**  
   - External catalogs **harvest DCAT** from KFM endpoints (e.g., HTTP GET, SPARQL).

3. **Linked Data endpoints**  
   - KFM exposes an API (SPARQL/LD API) that returns DCAT, and partners query it directly.

### 2.1 Push Export

Recommended when:

- Partner requires **periodic imports** (e.g., monthly catalog updates).  
- Network or security rules favor outbound data pushes.

Characteristics:

- Export of:
  - DCAT JSON-LD (primary).  
  - Optional Turtle/RDF/XML.  
- Delivery options:
  - HTTPS endpoints.  
  - Data dumps in object storage.  

### 2.2 Pull Harvest

Recommended when:

- Partner catalogs can periodically **crawl or harvest** KFM endpoints.  

Characteristics:

- KFM exposes:
  - DCAT JSON-LD catalog or dataset lists.  
  - Optionally a `dcat:Catalog` root with `dcat:dataset` links.

### 2.3 Linked Data / SPARQL

Recommended when:

- Partners need **rich query** capabilities via RDF/Linked Data.

Constraints:

- More complex infrastructure.  
- Must still respect **FAIR+CARE** and sovereignty constraints:
  - Queries must not yield records that are not meant for the requesting audience.

---

## 📦 3. Profiles & Shapes for Federation Partners

### 3.1 Internal KFM Shape (KFM DCAT Profile)

All exports MUST conform to:

- `dcat-kfm-profile.md`  
- `catalogs-dcat-*.shape.ttl` SHACL shapes

### 3.2 Partner-Specific Profiles (Examples)

For each partner, federation guidelines should define:

- Required profile:
  - `DCAT-AP`, `GeoDCAT-AP`, or custom DCAT profile.  
- Additional constraints:
  - Required fields beyond KFM DCAT profile.  
  - Specific vocabularies for `dcat:theme`, `dcat:keyword`, etc.  

KFM adapters:

- May add derived fields **without modifying STAC** (e.g., extra `dcat:theme` codes).  
- Must **not override** or contradict STAC-derived essentials.

---

## 🛡️ 4. FAIR+CARE & Sovereignty in Federation

Federation is **not purely technical** — it’s a governance event.

### 4.1 Eligible Datasets for Federation

Only datasets where:

- `kfmfc:sensitivity` ∈ { `general`, `mixed`, `restricted-generalized` (under specific conditions) }  
- `kfmfc:care_label` allows external sharing (e.g., `Public`, selected `Community-Controlled` with agreement).  
- `kfmfc:sovereignty_flag` is respected:
  - If `true`, explicit agreements and policies must exist for each partner.

Internal-only datasets:

- `kfmfc:sensitivity = "restricted-internal"`  
  - **MUST NOT** be included in external DCAT federation.

### 4.2 Spatial Generalization & Redaction

For sensitive datasets:

- Federation exports must only include **generalized** forms:
  - DCAT bounding boxes derived from generalized STAC `bbox`.  
  - No direct indication of precise geometries, site-level details, or restricted boundaries.

### 4.3 Policy References

Federation exports should include or be accompanied by:

- Links to FAIR+CARE and sovereignty policies (`faircare_ref`, `sovereignty_ref`).  
- Dataset-level `kfmfc:governance_ref` values when available.

This allows partner portals to:

- Display governance context or restrictions.  
- Implement local policies based on KFM governance metadata.

---

## 🧬 5. Provenance & Lineage for Federated DCAT

Federated DCAT artifacts must maintain clear lineage:

- **STAC source** → **KFM DCAT** → **Partner DCAT**

PROV-O patterns:

- KFM DCAT dataset as `prov:Entity`.  
- Crosswalk/derivation pipeline as `prov:Activity`.  
- STAC Item/Collection as `prov:Entity` used by the Activity.  
- Partner DCAT records as `prov:Entity` derived from KFM DCAT.

KFM should:

- Retain logs or PROV-O graphs describing:
  - When and how exports were generated.  
  - Which STAC versions they reflect.  
  - Which partner they target.

---

## 🔧 6. Technical Export Patterns

### 6.1 Data Dumps

For push exports:

~~~text
s3://kfm-dcat-exports/<partner>/<YYYY-MM-DD>/catalog.jsonld
s3://kfm-dcat-exports/<partner>/<YYYY-MM-DD>/datasets/*.jsonld
~~~

Guidelines:

- Use **versioned paths** with dates or commit hashes.  
- Provide simple index files (`catalog.jsonld`) to enumerate datasets.

### 6.2 Partner-Specific APIs

When exposing an HTTP endpoint for harvesting:

- Provide:
  - A root `dcat:Catalog` JSON-LD.  
  - `dcat:dataset` lists with pagination, if needed.

- Honor:
  - Accept headers for JSON-LD/Turtle where feasible.  
  - Rate limits and caching semantics.

---

## 🧪 7. CI & Pre-Export Validation

Before any federation export:

1. **STAC validation** (source layer)
   - Ensure all STAC Items/Collections included pass:
     - KFM STAC profile  
     - Extension schemas  
     - Best-practices linting

2. **DCAT derivation & validation**
   - Run STAC → DCAT crosswalk.  
   - Validate DCAT against:
     - KFM DCAT profile  
     - SHACL shapes  
     - Any partner-specific shapes.

3. **Governance checks**
   - Filter out datasets:
     - With `kfmfc:sensitivity = "restricted-internal"`.  
     - Without appropriate CARE/sovereignty flags for the target partner.

4. **Export artifact checks**
   - Verify that:
     - All `dcat:downloadURL`s match allowed endpoints.  
     - No internal-only endpoints are exposed.  
     - Links resolve, or at least are syntactically valid.

CI jobs (illustrative):

- `catalog-dcat-federation-validate.yml` — run full end-to-end validation for a given partner.

---

## ✅ 8. Federation Implementation Checklist

Before enabling or updating a federation link with a partner:

1. **Define the profile & scope**
   - Which datasets?  
   - Which DCAT profile?  
   - How often are updates sent/pulled?

2. **Confirm governance alignment**
   - FAIR+CARE and sovereignty conditions understood and documented.  
   - Written agreements in place if required.

3. **Implement & test crosswalk**
   - Map KFM DCAT → partner DCAT profile.  
   - Confirm no sensitive fields/records are exposed.

4. **Configure CI & monitoring**
   - Add federation-specific validation workflows.  
   - Track export counts, failures, and validation issues in telemetry.

5. **Run a pilot**
   - Limited dataset set.  
   - Close monitoring of issues.  
   - Joint review with the partner.

6. **Scale up**
   - Gradually expand dataset coverage.  
   - Periodically revalidate governance and technical assumptions.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial DCAT federation guidelines; defined push/pull/LD federation models, governance constraints, CI validation expectations, and implementation checklist aligned with STAC-first → DCAT-derived model. |

