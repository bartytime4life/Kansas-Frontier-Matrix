---
title: "🗒️ Kansas Frontier Matrix — Legacy Archive Notes (Treaties & Land Cessions)"
path: "data/archive/treaties/treaties_legacy/archive_notes.md"
version: "v8.x-Legacy"
last_updated: "2025-10-28"
compiled_by: "@kfm-data-lab"
reviewed_by: "@kfm-architecture"
ethics_reviewed_by: "@kfm-cultural-liaison"
license: "CC-BY 4.0"
governance_ref: "../../../../docs/standards/governance/TREATY-GOVERNANCE.md"
related_manifest: "../../../../data/archive/treaties/treaties_legacy/migration_manifest.json"
---

<div align="center">

# 🗒️ Kansas Frontier Matrix — **Legacy Archive Notes**  
### Treaties & Land Cessions (Pre-FAIR+CARE Era)
`data/archive/treaties/treaties_legacy/archive_notes.md`

**Purpose:** Provides documentation of retrospective FAIR+CARE audits and governance review for the Kansas Frontier Matrix legacy treaty datasets.  
These notes summarize validation actions, provenance reconstruction, and ethical considerations applied to pre-standardization materials digitized before 2023.

[![Legacy Status](https://img.shields.io/badge/Status-Legacy%20Preserved-grey)](../../../../docs/standards/governance/TREATY-GOVERNANCE.md)
[![FAIR+CARE Alignment](https://img.shields.io/badge/FAIR%2BCARE-Retrospective%20Audit-yellow)](../../../../docs/standards/faircare-validation.md)
[![Indigenous Data Sovereignty](https://img.shields.io/badge/CARE%2BIDSA-Retrospective%20Compliant-brown)](../../../../docs/standards/governance/TREATY-GOVERNANCE.md)

</div>

---

## 📚 Overview

The legacy treaty datasets stored under `data/archive/treaties/treaties_legacy/` were compiled through early digitization projects between 1980 and 2015.  
These materials were created before the Kansas Frontier Matrix adopted FAIR+CARE governance, Indigenous Data Sovereignty (CARE+IDSA), and MCP-DL documentation standards.  
This record provides context and accountability for how these files were reviewed, validated, and ethically approved for retention in 2025.

---

## 🧩 Retrospective Audit Summary (2025 Review)

**Audit Conducted By:** Kansas Frontier Matrix FAIR+CARE Council  
**Review Period:** March–April 2025  
**Review Type:** Retroactive Governance and Ethical Validation  
**Governance Frameworks Applied:** FAIR+CARE v9.3.2, CARE+IDSA v2.1  

### Summary of Findings:

| Category | Result | Notes |
|-----------|--------|-------|
| **Metadata Presence** | ⚠️ Partial | Missing standard fields (version, provenance) reconstructed manually. |
| **Attribution Accuracy** | ✅ Complete | All source institutions (NARA, OHS) confirmed and cited. |
| **Coordinate System** | ✅ Aligned | Updated to EPSG:4326 (WGS84). |
| **Ethics Review** | ✅ Approved | No restricted or culturally sensitive data identified. |
| **Checksum Verification** | ✅ Verified | SHA-256 checksums generated and matched post-conversion. |
| **FAIR Score** | 86 / 100 | Based on reconstructed metadata and schema mapping. |
| **CARE Score** | 94 / 100 | High score due to Indigenous attribution and open license. |

---

## ⚙️ Retrospective Remediation Steps

1. **Metadata Reconstruction:**  
   - Added missing fields: `title`, `version`, `spatial_extent`, `temporal_extent`, `license`, and `provider`.  
   - Generated new metadata files under `data/archive/treaties/treaties_legacy/migration_manifest.json`.

2. **Checksum Generation:**  
   - All shapefile and CSV assets hashed with SHA-256.  
   - Integrity confirmed via manifest in `releases/v8.8.0/manifest.zip`.

3. **Coordinate Reference System Alignment:**  
   - All files reprojected from legacy state-plane coordinates to **EPSG:4326 (WGS84)** for modern interoperability.

4. **Ethical Validation:**  
   - Conducted CARE+IDSA retrospective review to ensure proper cultural stewardship and Indigenous attribution.

5. **Migration Mapping:**  
   - Created migration crosswalk to align legacy datasets with `treaties_v9.1.0` standardized schema.  

---

## 🧠 FAIR+CARE Council Comments

> **@kfm-data-lab (FAIR+CARE Council Lead):**  
> “Although the data predates formal MCP-DL adoption, the reconstructed metadata and governance mapping meet FAIR+CARE baseline requirements.  
> We recommend preservation for historical transparency and lineage completeness.”

> **@kfm-cultural-liaison (Indigenous Data Sovereignty Advisor):**  
> “No sensitive or restricted materials found. Legacy shapefiles contain publicly available geographic boundaries and treaty linework derived from federal archives.  
> Future users must acknowledge Indigenous sources and consult modern datasets for contextual updates.”

> **@kfm-architecture (Governance Oversight):**  
> “Migrating this legacy data into FAIR+CARE format ensures ethical and reproducible provenance for future treaty research.”

---

## 🔍 Cross-Reference to Modern Equivalents

| Legacy File | Modern Equivalent | Migration Date | Notes |
|--------------|------------------|----------------|-------|
| `kansas_treaty_lines_1980s.shp` | `treaties_v9.1.0/treaties_boundaries.geojson` | 2025-03-15 | CRS unified and metadata added |
| `digitized_texts_legacy.csv` | `treaties_v9.3.2/treaty_text_references_2025.csv` | 2025-04-02 | Texts normalized to UTF-8 and linked to STAC items |

Crosswalk maintained in:  
`data/archive/treaties/treaties_legacy/migration_manifest.json`

---

## ⚖️ Governance Integration

| Record | Purpose |
|---------|----------|
| `data/reports/audit/archive_integrity_log.json` | Audit and checksum verification of legacy files |
| `data/reports/fair/ethics_review_summary.md` | Ethical and FAIR+CARE review documentation |
| `data/archive/treaties/treaties_legacy/migration_manifest.json` | Provenance and file lineage mapping |
| `releases/v8.8.0/manifest.zip` | Checksum manifest for retro-archival datasets |

---

## 🧾 Key Takeaways

- Legacy treaty datasets are **historically significant** and will remain under permanent archival retention.  
- Metadata reconstruction ensures **continuity of provenance** from pre-digital archives to FAIR+CARE-aligned data.  
- Data users are advised to reference **modern versions (v9.1.0 or later)** for official analysis and publication.  
- Legacy datasets are open under **CC-BY 4.0** and serve as a critical part of Kansas’s historical data record.  

---

## 🧾 Recommended Citation

```text
Kansas Frontier Matrix (Legacy Archive). Kansas Treaty and Land Cession Datasets (Pre-FAIR+CARE Editions, 1980–2015).
Retrospectively audited under FAIR+CARE and CARE+IDSA frameworks (2025).
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/treaties/treaties_legacy
License: CC-BY 4.0
```

---

<div align="center">

**Kansas Frontier Matrix** · *Historical Treaty Data × FAIR+CARE Retrospective Review × Indigenous Data Sovereignty*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
