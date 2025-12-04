---
title: "🛰️ KFM v11.2.3 — STAC Best Practices (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Best-practice guidance for STAC Items, Collections, and Catalogs in the Kansas Frontier Matrix, covering geometry, temporal fields, assets, naming, links, and governance alignment."
path: "docs/standards/catalogs/stac/stac-best-practices.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x profile-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-best-practices-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-stac-best-practices-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:best-practices:v11.2.3"

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

doc_kind: "Best Practices"
intent: "catalogs-stac-best-practices"
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

json_schema_ref: "../../../schemas/json/catalogs-stac-best-practices-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-stac-best-practices-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC best-practices revision"
---

<div align="center">

# 🛰️ Kansas Frontier Matrix — STAC Best Practices  
`docs/standards/catalogs/stac/stac-best-practices.md`

**Purpose:**  
Provide **concrete, enforceable best practices** for STAC Items, Collections, and Catalogs in KFM, covering:

- Geometry & `bbox`  
- Temporal fields  
- Assets & checksums  
- Naming & IDs  
- Links & relations  
- Extensions & governance alignment  

This document extends the KFM STAC profile (`stac-kfm-profile.md`) with **“how we actually do it”** guidance.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

This document must be read together with:

- `docs/standards/catalogs/stac/README.md` — STAC standards index  
- `docs/standards/catalogs/stac/stac-kfm-profile.md` — formal KFM STAC profile (required fields & constraints)  
- `docs/standards/catalogs/stac-dcat-derivation.md` — STAC-first → DCAT-derived model  
- KFM STAC extensions under:  
  - `docs/standards/catalogs/stac/extensions/`

**This file focuses on**:

- Concrete patterns that are **tested in CI**.  
- Recommended conventions for new STAC content.  
- Anti-patterns that must be avoided.

---

## 🌍 2. Geometry & BBOX Best Practices

### 2.1 Geometry is Authoritative

- `geometry` in STAC Items is the **authoritative spatial footprint**.  
- `bbox` is a **derived envelope** used for:
  - Quick spatial search  
  - Derived DCAT `dct:spatial` summaries  
  - Higher-level catalogs

**Best practices:**

- Ensure `geometry` is:
  - Valid GeoJSON (Polygon/MultiPolygon, LineString, or Point as appropriate).  
  - Topologically valid (no self-intersections) for polygons.  
  - Simplified where necessary for performance, but not so coarse that it misrepresents coverage.

- Always generate `bbox` from `geometry` in pipelines, rather than hand-editing.

### 2.2 Sensitive / Generalized Geometries

For domains like **archaeology**:

- **Public STAC** must use generalized geometries:
  - `polygon-generalized`  
  - `h3-only` (H3 mosaics as assets)  
- Exact footprints should be:
  - Internal-only STAC Items, or  
  - Kept entirely outside public STAC and only referenced via provenance.

Use the `kfm-faircare` and domain extensions (e.g., `kfm-archaeology`) to drive:

- Geometry generalization levels  
- Visibility rules in web apps (see governance docs for viewers)

---

## ⏱️ 3. Temporal Fields: `datetime` and Ranges

### 3.1 Instantaneous vs Ranged Time

For **instantaneous** datasets:

- Use `properties

