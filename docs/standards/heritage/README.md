---
title: "🛡️ Kansas Frontier Matrix — H3 Spatial Generalization Super-Standard for Sensitive Heritage Locations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/h3-generalization.md"
version: "v11.0.2"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council & Spatial Standards Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-h3-generalization-v11.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Governance Standard"
intent: "heritage-h3-generalization"
semantic_document_id: "kfm-doc-h3-generalization"
doc_uuid: "urn:kfm:docs:heritage:h3-generalization:v11.0.2"
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
Define the **maximum-protection H3 spatial generalization super-standard** for sensitive heritage, Indigenous, archaeological, ecological, ceremonial, and culturally governed locations across the Kansas Frontier Matrix (KFM).  

Implements:  
- Sovereignty & confidentiality under **FAIR+CARE v11**  
- Legal secrecy mandates under **NHPA §304** and related cultural-resource protections  
- Ethical spatial masking compatible with **KFM Sensitive-Site Governance Super-Standard v11**  
- Cross-domain metadata under **STAC 1.x, DCAT 3.0, CIDOC-CRM, OWL-Time, GeoSPARQL, ISO 19115**  
- Governance lifecycle under **MCP-DL v6.3 + KFM-MDP v11**  

</div>

---

# 📘 1. Overview

This Super-Standard defines the **top-level policy** for using **H3 spatial generalization** to protect sensitive heritage and cultural locations in KFM, including but not limited to:

- Archaeological sites and complexes  
- Burial grounds and graveyards  
- Sacred and ceremonial sites  
- Tribal / Indigenous cultural landscapes and features  
- Ecologically sensitive areas with cultural meaning  
- Hydrologic features with spiritual or cultural significance  
- Restricted geophysical / geochemical measurements  
- Legacy datasets containing latent sensitive coordinates  

No dataset containing such locations may:

- expose raw coordinates  
- expose simplified geometries derived directly from raw coordinates  
- expose bounding boxes precise enough to back-calculate site coordinates  
- combine with other KFM or external layers to defeat masking  
- appear in Story Nodes or Focus Mode with precise spatial anchors  

All such data **MUST** undergo H3 generalization governed by this Super-Standard **before** any exposure outside Tier-1 secure environments.

This document sits **above** implementation standards (e.g., the *Dynamic H3 Generalization & Automated CARE Screening* standard) and MUST be applied to:

- All **static** H3 generalization pipelines (`h3_static`)  
- All **dynamic** sensitivity-aware H3 pipelines (`h3_dynamic`)  
- Any custom H3-derived masking workflows that touch sensitive heritage data  

---

# 🧱 2. Core Principles (Normative)

| Principle | Requirement (Normative) |
|----------|--------------------------|
| **Sovereignty First** | Tribal and community authorities define what may be shown, at what resolution, and when. |
| **Maximum Protection** | Default is **over-protection**; under-protection is never allowed. |
| **Generalization over Removal** | Favor H3-based aggregation instead of deletion to preserve analytical value. |
| **Aggregation** | Public-facing hexes MUST aggregate **≥ 3 sites** (k-anonymity ≥ 3; ≥ 7 strongly recommended). |
| **Irreversibility** | No published method may allow back-calculation to original coordinates or exact shapes. |
| **Reproducibility** | Pipelines MUST be deterministic and documented per MCP-DL v6.3. |
| **FAIR+CARE Hybrid** | FAIR governs technical metadata; CARE governs sovereignty, consent, and ethics. |
| **Least Privilege** | Only Tier-1 environments can access pre-generalization data; no client-side masking. |

Where this Super-Standard conflicts with any other technical standard, **this Super-Standard prevails**, except where overridden by:

1. Tribal / Indigenous governance decisions and treaties  
2. Applicable law (e.g., NHPA, NAGPRA, data protection acts)  
3. KFM **Sensitive-Site Governance Super-Standard v11**  
4. FAIR+CARE Council rulings  

---

# 🧭 3. Sensitivity Levels & H3 Resolution Policy

## 3.1 Sensitivity Levels

Sensitivity is based on **cultural, legal, and ecological risk**, not just “data type.”

High-level sensitivity bands:

- **Very High** — sacred sites, burial grounds, active ceremonial locations, restricted tribal knowledge  
- **High** — archaeological sites, rock art, settlements, historic camps, sacred hydrologic features  
- **Moderate** — ecologically sensitive areas, culturally meaningful landscapes with diffuse extents  
- **Low** — general environmental or historical locations not individually sensitive  

## 3.2 Required H3 Resolution Bands

| Sensitivity Level | Required Minimum H3 Resolution | Approx Area per Hex | Notes |
|------------------|---------------------------------|---------------------|-------|
| **Very High** | Concealment OR r5 (or coarser) | ~150 km² | Prefer no geometry; if used, only broad regional hexes. |
| **High** | **r7 (default)** | ~5.16 km² | KFM baseline for heritage masking. |
| **Moderate** | r7–r8 | 5.1–0.7 km² | Requires FAIR+CARE Council review. |
| **Low** | r8 | ~0.74 km² | Only for non-sensitive or fully de-identified layers. |

**Mandatory rule:**  
If sensitivity is **unknown**, the dataset MUST be treated as **High** → assign **r7**.

Dynamic pipelines that use a numeric `sensitivity_score` (0–100) MUST map that score into the above bands, and the resulting H3 resolution MUST respect these minima.

---

# 🔒 4. Prohibited Practices

The following are **strictly prohibited** for any KFM workflow involving sensitive heritage data:

- Including **raw latitude/longitude**, UTM, or other precise coordinates in any non-Tier-1 environment  
- Publishing geometries that are merely simplified variants of raw shapes  
- Publishing bounding boxes that allow pinpointing a site inside a very small polygon  
- Publishing H3 resolution **finer than r7** for any sensitive site  
- Using photographs that show identifiable landscape features revealing location  
- Embedding coordinates (or easily-decoded hints) inside Story Nodes or Focus Mode narratives  
- Combining multiple generalized layers (or external data) in such a way that effective resolution becomes finer than policy allows  
- Performing reverse-engineering, triangulation, or de-anonymization analyses against generalized data  

If any experiment, pipeline, or visualization risks any of the above, it MUST be rejected or redesigned before deployment.

---

# 🛡️ 5. Legal, Ethical & Sovereignty Mandates

## 5.1 NHPA §304 (United States)

Under **NHPA §304**, governmental bodies may withhold from disclosure information about the location, character, or ownership of historic resources when such disclosure could:

- cause a significant invasion of privacy  
- risk harm to the resource  
- impede the use of a traditional religious site  

KFM interprets this to require that:

- Raw coordinates and precise site locations are treated as **confidential** by default.  
- H3 generalization at or above r7 is used as standard for public-facing spatial disclosure.  
- Even generalized disclosure may be prohibited for Very High sensitivity sites.

## 5.2 CARE Principles

- **Authority to Control** — Communities and tribes have **authority** over their data and may veto or revoke publication.  
- **Collective Benefit** — Publications must demonstrably **benefit** affected communities, not solely external stakeholders.  
- **Responsibility** — KFM commits to rapid takedown, correction, and continuous oversight in collaboration with communities.  
- **Ethics** — Cultural safety and wellbeing override research curiosity or technical interest.

## 5.3 FAIR Principles

KFM uses H3 generalization to remain FAIR while masking:

- Generalized H3 data remains **interoperable** and **reusable** for many spatial analyses.  
- DCAT 3.0 and STAC 1.x metadata enable discovery and reuse of aggregated datasets without exposing raw coordinates.

## 5.4 Governance Hierarchy

This Super-Standard is subordinate only to:

1. Tribal / Indigenous governance and treaties  
2. Law (NHPA, NAGPRA, other relevant statutes)  
3. KFM **Sensitive-Site Governance Super-Standard v11**  
4. FAIR+CARE Council rulings  

---

# 🧬 6. End-to-End Super-Standard Workflow (Static H3 Generalization)

This section defines the **static** H3 generalization flow (`h3_static`). Dynamic H3 pipelines MUST, at minimum, uphold the same policy constraints.

## 6.1 Step 1 — Intake (Tier-1 Secure Workspace)

Raw data are stored in:

```text
data/work/heritage/raw/
````

Each dataset MUST be tagged with metadata equivalent to:

```json
{
  "sensitivity": "high",
  "access_level": "tier1",
  "raw_coordinates": "present",
  "heritage_protected": true,
  "mcp_protected": true
}
```

Access is strictly limited to governance-approved personnel and services.

## 6.2 Step 2 — H3 Conversion

For each raw point or polygon:

* Compute representative points as needed (e.g., centroids for polygons) in Tier-1.
* Assign H3 cells at the required resolution:

```python
h3_id = h3.latlng_to_cell(lat, lon, RES)  # RES ≥ required minimum (e.g., 7)
```

RES is determined by sensitivity per Section 3.

## 6.3 Step 3 — Drop All Raw Spatial Coordinates

After H3 assignment, **all** direct coordinate fields MUST be removed from downstream datasets:

* `latitude`, `longitude`
* `utm_x`, `utm_y`
* Raw `geometry` (points/polygons)
* Raw `bbox` values

Only synthetic H3-derived geometries may remain.

## 6.4 Step 4 — Aggregate & Anonymize

Aggregate features by H3 cell, ensuring:

* `site_count ≥ 3` (and ≥ 7 where mandated by CARE policy)
* Rare attribute combinations are suppressed or coarsened (e.g., unique period + rare site type)
* Temporal fields are bucketed (e.g., period names, decades, or centuries) rather than precise dates for highly sensitive cases

## 6.5 Step 5 — STAC/DCAT/PROV-O Enrichment

Before publish or promotion:

* Tag dataset-level STAC/DCAT metadata with:

  * `heritage_protected = true`
  * `generalization_method = "H3_static"` (or `"H3_dynamic"` as applicable)
  * `h3_resolution`
  * `raw_coordinates_removed = true`
  * `care_status` and `faircare_profile`
  * `legal_basis` (e.g., `"NHPA §304"`)
* Emit PROV-O lineage linking:

  * Source raw Tier-1 dataset
  * Generalization activity
  * Resulting H3 dataset

## 6.6 Step 6 — Governance Logging & Telemetry

Every run MUST append a governance entry plus telemetry (see Sections 11 and 12). These logs:

* allow audits of masking decisions
* provide evidence for governance review
* track energy / carbon costs of the pipeline

---

# 🧬 7. H3 Metadata Schema (v11 Super-Standard)

Each generalized H3 record MUST include at minimum:

```json
{
  "h3_id": "8728308ffffff",
  "h3_resolution": 7,
  "heritage_protected": true,
  "generalization_method": "H3_static",
  "raw_coordinates_removed": true,
  "site_count": 4,
  "periods": ["Great Bend Aspect"],
  "care_status": "restricted",
  "legal_basis": "NHPA §304",
  "faircare_profile": "F1-A1-I2-R3"
}
```

Recommended optional fields:

* `h3_neighbors`: neighboring H3 cells used in further aggregation
* `h3_buffer_cells`: cells used to blur boundaries or extend aggregation regions
* `aggregated_attributes`: statistical summaries (counts by category, etc.) that are non-identifying

---

# 📚 8. DCAT 3.0 / STAC 1.x Crosswalk

**DCAT 3.0 mapping requirements:**

| DCAT Field                       | Requirement                                                                                    |
| -------------------------------- | ---------------------------------------------------------------------------------------------- |
| `dcat:spatialResolutionInMeters` | MUST approximate the H3 hex diameter (e.g., ~2200 m for r7).                                   |
| `dct:provenance`                 | MUST state “Generalized from Tier-1 raw heritage coordinates under KFM H3 Super-Standard v11”. |
| `dct:conformsTo`                 | MUST include `"KFM H3 Spatial Generalization Super-Standard v11"`.                             |
| `dct:license`                    | MUST reflect licensing + CARE constraints (e.g., additional restrictions beyond CC-BY).        |

**STAC 1.x requirements:**

* `stac_version = "1.0.0"`
* `properties["heritage_protected"] = true`
* `properties["generalization_method"] = "H3_static"` or `"H3_dynamic"`
* `properties["h3_resolution"]` integer
* `properties["raw_coordinates_removed"] = true`
* `properties["care_status"]` string
* `properties["legal_basis"]` string

---

# 🌐 9. GeoSPARQL / CIDOC / OWL-Time Mapping

Generalized H3 cells are modeled as **places**, not as raw site geometries.

Example:

```ttl
:kfm_h3_cell_8728308ffffff a cidoc:E53_Place, geo:Feature ;
    geo:hasGeometry [
        a geo:Polygon ;
        geo:asWKT "<SYNTHETIC_HEX_WKT>"^^geo:wktLiteral
    ] ;
    cidoc:P1_is_identified_by "8728308ffffff" ;
    cidoc:P2_has_type "H3_Static_Generalized_Heritage_Cell" ;
    prov:wasGeneratedBy :H3_Generalization_Activity_2025_11_20 .
```

Temporal properties (OWL-Time) apply to the **aggregated cell-level dataset**, not to individual raw sites.

---

# 🗂 10. Directory Layout (Option B, v11-Compliant)

```text
Kansas-Frontier-Matrix/                     # Monorepo root
│
├── docs/                                   # Documentation root
│   └── standards/                          # Project-wide standards
│       └── heritage/                       # Heritage and sensitive-site standards
│           └── h3-generalization.md        # This H3 Spatial Generalization Super-Standard
│
├── src/                                    # Source code (pipelines, services, UI)
│   └── pipelines/                          # Data pipelines and processing DAGs
│       └── privacy/                        # Privacy and masking-related pipelines
│           └── h3_static/                  # Static H3 generalization implementation for heritage
│               ├── policy.yml              # Sensitivity→H3 resolution mappings and rules
│               ├── rules/                  # Legal and CARE/FAIR policies for static H3
│               │   ├── legal.yaml          # NHPA §304 / NAGPRA and legal constraints
│               │   └── care_fair.yaml      # CARE + FAIR enforcement rules for static H3
│               ├── scripts/                # Executable scripts implementing the Super-Standard
│               │   ├── h3_static_generalize.py   # Main static H3 generalization engine
│               │   └── h3_static_validate.py     # Static H3 validation/consistency checks
│               └── tests/                  # Unit/integration tests validating correct behavior
│                   ├── test_policy_static.py     # Tests for policy interpretation and H3 mapping
│                   └── test_superstandard_enforcement.py   # Tests ensuring prohibited patterns are blocked
│
└── data/                                   # Data directories (raw, work, processed)
    └── work/                               # Non-committed working directories
        └── heritage/                       # Heritage-related staging workspaces
            └── h3_static/                  # Static H3 workspace for heritage datasets
                ├── input/                  # Tier-1 secure inputs (raw coordinates, not committed)
                ├── output/                 # Generalized H3 outputs ready for publish review
                └── logs/                   # Governance and telemetry logs for each run
```

---

# 🧠 11. Story Node v3 & Focus Mode v3 Restrictions

## 11.1 Forbidden in Story Nodes

Any **Story Node v3** that touches sensitive heritage data MUST NOT:

* Include raw coordinates or map links to exact locations
* Reference uniquely identifying landscape features that reveal precise locations
* Embed clear photos that show identifiable site features or access paths, unless separately reviewed and allowed
* Pin to geometries finer than the allowed H3 resolution for the relevant sensitivity level

## 11.2 Required Story Node Behavior

* Use **regional names** or broad landscape descriptions (e.g., “central Kansas prairie,” “upper Smoky Hill region”) where precision would cause risk
* Use **periods** (e.g., “Great Bend Aspect,” “late 19th century”) rather than exact dates for Very High sensitivity cases
* Include CARE/FAIR metadata, including `care_status`, `authority_to_control`, and `heritage_protected` flags

## 11.3 Focus Mode v3 Constraints

When Focus Mode v3 centers on sensitive heritage content:

* Map views MUST show only generalized H3 cells, **never** raw sites
* Timeline annotations MUST avoid event sequences that imply exact site positions
* AI-generated summaries MUST be constrained by CARE rules and MUST NOT reveal location-level detail beyond allowed H3 resolution
* All Focus Mode outputs are subject to **CARE audit logs** and may be revoked at community request

---

# 🧪 12. Validation & CI/CD Requirements

The following CI jobs MUST validate compliance with this Super-Standard:

* `faircare-validate.yml` — FAIR+CARE metadata and ethical compliance checks
* `stac-validate.yml` — STAC Collection/Item schema compliance, including H3 and CARE fields
* `heritage-mask-validate.yml` — enforcement of H3 resolution minima and prohibition of raw coords
* `telemetry-export.yml` — export of telemetry and energy/carbon metrics
* `docs-lint.yml` — enforcement of KFM-MDP v11 markdown structure and style

**Rejection conditions (non-exhaustive):**

* Raw lat/lon, UTM, or raw `geometry` detected outside Tier-1 directories
* Generalized datasets using H3 resolutions finer than allowed for their sensitivity levels
* Missing `heritage_protected`, `generalization_method`, `h3_resolution`, or `raw_coordinates_removed` in STAC properties
* Heritage Story Nodes or Focus narratives referring to precise locations or identifiable visual cues
* Incomplete CARE/FAIR metadata on heritage datasets

---

# 🕰 13. Version History

| Version |       Date | Summary                                                                                                     |
| ------: | ---------: | ----------------------------------------------------------------------------------------------------------- |
| v11.0.2 | 2025-11-23 | Corrected fenced block spacing; enforced tight code fences; clarified Section 6 workflow formatting.        |
| v11.0.1 | 2025-11-23 | Upgraded to KFM-MDP v11 formatting; added Option-B directory tree, Story Node/Focus constraints, CI notes.  |
| v11.0.0 | 2025-11-20 | Initial v11 Super-Standard; defined maximum-protection H3 generalization policy and legal/ethical mandates. |
| v10.2.3 | 2025-11-13 | Legacy H3 generalization standard (v10), superseded by v11.                                                 |

---

[Back to Governance](../../governance/ROOT-GOVERNANCE.md) · [Releases & SBOM](../../../releases/v11.0.0/manifest.zip) · [Telemetry Schema](../../../schemas/telemetry/standards-h3-generalization-v11.json)

```
