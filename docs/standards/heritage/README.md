---
title: "🛡️ Kansas Frontier Matrix — H3 Spatial Generalization Super-Standard for Sensitive Heritage Locations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/h3-generalization.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual / FAIR+CARE Council & Spatial Standards Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/standards-h3-generalization-v11.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Governance Standard"
intent: "heritage-h3-generalization"
semantic_document_id: "kfm-doc-h3-generalization"
doc_uuid: "urn:kfm:docs:heritage:h3-generalization-v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I2-R3"
care_label: "Restricted / High-Sensitivity"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
provenance_chain:
  - "docs/standards/heritage/h3-generalization.md@v10.2.3"
  - "SensitiveSiteGovernance_SuperStandard_v11.pdf"
  - "KFM_TechnicalGuide_v11.pdf"
  - "MasterCoderProtocol_2.0.pdf"
ontology_alignment:
  cidoc: "E53 Place"
  schema_org: "Place"
  prov_o: "prov:Activity"
metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "CIDOC-CRM"
  - "FAIR+CARE"
  - "ISO 19115"
ai_training_inclusion: false
jurisdiction: "Kansas / United States"
classification: "Restricted"
lifecycle_stage: "stable"
ttl_policy: "48 months"
sunset_policy: "Superseded by H3 Generalization v12"
---

<div align="center">

# 🛡️ **H3 Spatial Generalization Super-Standard for Sensitive Heritage Locations**  
### *KFM-MDP v11 · FAIR+CARE v11 · NHPA §304 · MCP-DL v6.3*  
`docs/standards/heritage/h3-generalization.md`

**Purpose:**  
Define the **maximum-protection spatial generalization standard** for sensitive heritage, Indigenous, archaeological, ecological, ceremonial, and culturally governed locations.  
Implements:  
- Sovereignty & confidentiality under **FAIR+CARE v11**  
- Legal secrecy mandates under **NHPA §304**  
- Ethical spatial masking compatible with **KFM Sensitive-Site Super-Standard**  
- Cross-domain metadata under **STAC 1.x, DCAT 3.0, CIDOC-CRM, OWL-Time, GeoSPARQL**  
- Governance lifecycle under **MCP-DL v6.3 + KFM-MDP v11**  

</div>

---

# 📘 1. Overview

This super-standard governs **all spatial generalization of sensitive site data** in KFM, including:

- Archaeological sites  
- Burial grounds  
- Sacred & ceremonial sites  
- Tribal/Indigenous cultural features  
- Ecologically sensitive areas  
- Hydrologic features with cultural meaning  
- Restricted geophysical data  
- Legacy datasets containing latent sensitive coordinates  

No dataset involving sensitive locations may:

- expose coordinates  
- expose implied coordinates  
- expose map features precise enough to infer coordinates  
- circumvent masking using geometry simplification  
- combine layers to reduce masking  
- appear in Story Nodes or Focus Mode with precise anchors  

All such datasets MUST use **H3 spatial generalization**.

---

# 🧱 2. Core Principles (Normative)

| Principle | Requirement |
|----------|-------------|
| **Sovereignty First** | Tribal authority determines precision and release. |
| **Maximum Protection** | Masking defaults to highest confidentiality. |
| **Generalization over Removal** | Always generalize before removing value. |
| **Aggregation** | Minimum 3 sites per hex for public data. |
| **Irreversibility** | No method must allow reverse-engineering of coordinates. |
| **Reproducibility** | Pipelines must be deterministic under MCP-DL v6.3. |
| **FAIR+CARE Hybrid** | Maps FAIR into technical governance, CARE into ethical sovereignty. |

---

# 🧭 3. Spatial Generalization Model (H3)

## 3.1 Default Resolution Levels

| Sensitivity Level | Required H3 Resolution | Area | Notes |
|------------------|------------------------|------|-------|
| **Very High** (Sacred/Burial) | Concealment OR r5 | ~150 km² | No geometry preferred |
| **High** (Archaeology) | **r7 (default)** | ~5.16 km² | KFM baseline |
| Moderate | r7–r8 | 5.1–0.7 km² | Requires Council review |
| Low | r8 | ~0.74 km² | Only for non-sensitive data |

**Rule:**  
If sensitivity is unknown → **assign High → use r7**.

---

# 🔒 4. Prohibited Practices

Under NO circumstances may any dataset:

- include raw lat/lon  
- include geometries simplified from raw shapes  
- infer coordinates from bounding boxes  
- expose < r7 for sensitive sites  
- reveal individually identifiable site attributes  
- include site photos with identifying landscape features  
- include time stamps that imply site location through correlation  
- embed coordinates in Story Nodes, Focus Mode, tooltips, popups  

---

# 🛡️ 5. Legal, Ethical & Sovereignty Mandates

## 5.1 NHPA §304
Raw coordinates of archaeological sites are **confidential by federal law**.

## 5.2 CARE Principles
- **Authority to Control** governs all precision decisions  
- Community can veto or revoke release  
- Cultural safety overrides scientific curiosity  

## 5.3 FAIR Principles
H3 generalization preserves *interoperable spatial structure* without disclosing coordinates.

## 5.4 KFM Sensitive-Site Governance
This standard is subordinate only to:

- Tribal authority  
- FAIR+CARE Council  
- Sensitive-Site Super-Standard v11  

---

# 🧱 6. Full H3 Workflow (Standard Pipeline)

## Step 1 — Intake (Tier-1 Secure)
```
data/work/staging/heritage/raw/
```
Tagged with:
```json
{
  "sensitivity": "high",
  "access_level": "tier1",
  "raw_coordinates": "present",
  "mcp_protected": true
}
```

## Step 2 — Convert → H3
```python
h3.latlng_to_cell(lat, lon, RES)  # RES = 7
```

## Step 3 — Drop All Coordinates
Fields removed:
- `latitude`
- `longitude`
- `geometry`
- `bbox` (raw)
- `utm_x`, `utm_y`

## Step 4 — Aggregate
- Must aggregate to **min 3 sites per hex**  
- Must include **period roll-ups**  
- Must remove rare attribute combinations

## Step 5 — STAC/DCAT Metadata Generation
Injected fields:
```json
{
  "heritage_protected": true,
  "generalization_method": "H3",
  "h3_resolution": 7,
  "coordinates_removed": true,
  "care_status": "restricted"
}
```

## Step 6 — Governance Logging
Every generalization event MUST write to:
```
docs/reports/audit/governance-ledger.json
```

## Step 7 — Telemetry Update
Telemetry records:
- energy_wh  
- carbon_gco2e  
- duration_sec  
- number_of_sites_processed  
- masking_resolution  
- review_authority  

---

# 🧬 7. H3 Metadata Schema (v11)

### Required fields:
```json
{
  "h3_id": "8728308ffffff",
  "h3_resolution": 7,
  "heritage_protected": true,
  "generalization_method": "H3",
  "raw_coordinates_removed": true,
  "site_count": 4,
  "periods": ["Great Bend Aspect"],
  "care_status": "restricted",
  "legal_basis": "NHPA §304"
}
```

### Optional extensions:
- `h3_neighbors`  
- `h3_buffer_cells`  
- `aggregated_attributes`  

---

# 📚 8. DCAT 3.0 Crosswalk

| DCAT Field | H3 Equivalent |
|-----------|---------------|
| `dcat:spatialResolutionInMeters` | `~2200` (r7 diameter) |
| `dct:provenance` | `"Generalized from Tier-1 raw heritage coordinates"` |
| `dct:conformsTo` | `"KFM H3 Spatial Generalization Standard v11"` |

---

# 🌐 9. GeoSPARQL Mapping

```ttl
:h3Cell a geo:Feature ;
    geo:hasGeometry [
        a geo:Polygon ;
        geo:asWKT "<WKT of hex>"^^geo:wktLiteral
    ] .
```

All WKT MUST represent **synthetic hex geometry**, never raw-derived.

---

# 🧠 10. Story Node v3 & Focus Mode v3 Restrictions

### Forbidden:
- Linking Story Nodes to precise coordinates  
- Attaching events to hexes smaller than r7  
- Describing landscape features tied to sensitive location  
- Embedding lat/lon in narrative metadata  
- Using photographs that reveal exact sites

### Required:
- Region-scale references  
- Temporal periods rather than dates  
- Cultural narratives reviewed by tribal authority  
- Sensory modifiers for accessibility  

---

# 🧪 11. Validation (CI/CD)

### Required jobs:
- `faircare-validate.yml`  
- `stac-validate.yml`  
- `heritage-mask-validate.yml` *(v11 addition)*  
- `telemetry-export.yml`  
- `docs-lint.yml`  

### Rejection conditions:
- Missing CARE metadata  
- H3 < r7 for sensitive sites  
- STAC properties missing  
- Periods revealing too much specificity  
- Non-concealed photo metadata  
- Any appearance of raw lat/lon  

---

# ⚙️ 12. Example Annotated STAC Item

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-heritage-gen-2025-01",
  "bbox": [-96.3, 38.8, -96.1, 39.0],
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "heritage_protected": true,
    "generalization_method": "H3",
    "h3_resolution": 7,
    "raw_coordinates_removed": true,
    "legal_basis": "NHPA §304",
    "care_status": "restricted",
    "periods": ["Great Bend Aspect"],
    "site_count": 4
  }
}
```

---

# 🌄 13. Visualization Standard

### MapLibre:
- Render **hex polygons only**
- No pseudo-centroids  
- No precision popups  
- Tooltip text MUST avoid locational inference  
- Region-level summary mandatory

### Cesium:
- Extrude hexes based on site_count  
- Disable terrain cues that reveal altitude landmarks  

### D3:
- Synthetic hex shapes only  
- No raw geometries  

---

# 🔐 14. Reverse-Engineering Mitigation

KFM prohibits:

- distance triangulation  
- spatial join inference  
- multi-layer inference  
- hex-dual combination analysis  
- matching cultural phases to geographic constraints  

KFM applies:

- neighbor randomization (optional)  
- attribute suppression  
- minimum-count aggregation  
- resolution downgrading when risk increases  

---

# 🏛️ 15. Governance Integration

Every transformation MUST produce a governance ledger entry:

```json
{
  "event": "heritage_generalization",
  "dataset": "kfm-heritage-2025-01",
  "resolution": 7,
  "raw_coordinates_removed": true,
  "authority_to_control": "Example Tribal Nation",
  "timestamp": "2025-11-20T10:33:00Z"
}
```

Governance integrates with:

- FAIR+CARE v11  
- Sensitive-Site Super-Standard v11  
- Licensing v11  
- Telemetry v11  
- Accessibility v11  

---

# 🕰️ 16. Version History

| Version | Date | Summary |
|--------:|------------|---------|
| v11.0.0 | 2025-11-20 | Full maximum-expansion Super-Standard; integrated sensitive-site governance, FAIR+CARE v11, DCAT/STAC/CIDOC, AI safety, Story Node v3 rules. |
| v10.2.3 | 2025-11-13 | Legacy standard, superseded. |
| v10.2.2 | 2025-11-13 | Initial heritage generalization specification. |

---

<div align="center">

🛡️ **Kansas Frontier Matrix — H3 Spatial Generalization Super-Standard**  
“Protecting places, cultures, and futures.”

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
Master Coder Protocol v6.3 · FAIR+CARE v11

[⬅ Back to Standards Index](../../README.md)

</div>