<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION
title: County Connector README
type: standard
version: v1
status: draft
owners: [Bartytime]
created: 2026-05-07
updated: 2026-05-07
policy_label: restricted
related: [kfm://doc/NEEDS_VERIFICATION]
tags: [kfm, connector, county]
notes: [Repo-ready README for County Connector module; reconciles prior drafts, aligned with KFM Directory Rules, evidence-first, hydrology-first audit posture; all paths and IDs PROPOSED pending repo verification]
[/KFM_META_BLOCK_V2] -->

# County Connector README

> **Purpose:** Ingest, harmonize, and audit county-level geospatial datasets into KFM, preserving reproducible spatial joins, lifecycle governance, and traceable evidence lineage.

---

## 🚀 Quick Links

| Resource | Link |
|----------|------|
| Source Code | [GitHub Repo](NEEDS_VERIFICATION) |
| Issues | [GitHub Issues](NEEDS_VERIFICATION) |
| Pull Requests | [GitHub PRs](NEEDS_VERIFICATION) |
| Design Doc | [KFM Design Doc](NEEDS_VERIFICATION) |
| Evidence Bundles | [Public Evidence](NEEDS_VERIFICATION) |
| Directory Rules | [KFM Directory Rules](NEEDS_VERIFICATION) |

---

## ⚡ Impact Block

- **Integration:** Aligns county geographies (parcels, roads, hydrology, admin boundaries) into KFM.  
- **Deterministic Joins:** Official crosswalks first; spatial overlays second; centroids/outlet snaps as last resort.  
- **Governance:** Dataset version, join method, tolerance, and EvidenceBundle reference logged for full audit.  
- **Auditability:** DecisionEnvelope supports manual overrides and exceptions.  
- **Public Safety:** DENY-by-default for sensitive sources (living persons, rare species, critical infrastructure).  
- **Hydrology-First:** All new county layers start downstream of hydrology/ecology proof lanes for safe audit sequencing.

---

## 📚 Overview

The **County Connector** implements hierarchical, deterministic spatial joins:

1. **Official Crosswalks**  
   - COMID ⇄ HUC12 mappings from NHDPlus V2.1 or trusted equivalents.  
2. **Catchment–Polygon Overlay**  
   - Polygon-to-polygon spatial joins where official mappings are absent.  
3. **Centroid Fallback**  
   - Assign points to containing HUC/county polygon when overlaps are ambiguous.  
4. **Outlet Snap (Pour Point)**  
   - Last-resort assignment based on pour point proximity to hydrography.

> **Audit Note:** Record all join tolerances, snap distances, and dataset versions in the EvidenceBundle for reproducibility.

---

<details>
<summary>References & Evidence</summary>

1. [USGS NHDPlus V2.1 Data Catalog](https://data.usgs.gov/datacatalog/data/USGS%3A5c86a747e4b09388244b3da1)  
2. [EPA NHDPlus User Guide](https://www.epa.gov/system/files/documents/2023-04/NHDPlusV2_User_Guide.pdf)  
3. [USGS 12-Digit Hydrologic Unit Pour Points](https://www.usgs.gov/data/12-digit-hydrologic-unit-outlet-pour-points-nhdplus-v21-wbd-snapshot)  
4. KFM EvidenceBundle references: `kfm://evidence/NEEDS_VERIFICATION`  

</details>

---

## ✅ Governance Checklist

* [ ] Official crosswalks are current and verified.  
* [ ] Spatial overlay tolerances recorded.  
* [ ] Centroid and snap fallback documented.  
* [ ] EvidenceBundle and DecisionEnvelope linked.  
* [ ] Policy and rights enforcement checked.  
* [ ] Sensitive/restricted data DENY-by-default.  
* [ ] Lifecycle respected: `RAW → WORK → PROCESSED → CATALOG → PUBLISHED`:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}.

---

## 🛠 Usage

```bash
# Run ingest for a specific county
python ingest/run_county_ingest.py --county FIPS_CODE

# Preflight validation for a specific layer
python preflight/checks.py --layer parcels_sedgwick

# Example CLI with EvidenceBundle logging
python connect_county.py \
  --input dataset.csv \
  --output aligned.csv \
  --evidence-bundle kfm://evidence/NEEDS_VERIFICATION
```

**Notes:**

- Every output **must reference the EvidenceBundle** used.  
- Manual overrides or exceptions are captured in **DecisionEnvelope**.  
- Direct RAW/WORK/QUARANTINE access is prohibited; all layers follow the KFM lifecycle.  
- All spatial joins **must be reproducible** for audit and review.

---

## 📁 Proposed Directory Layout (PROPOSED)

```
connectors/
└── county/
    ├── README.md
    ├── ingest/
    │   ├── nwis/
    │   ├── ssurgo/
    │   └── parcels/
    ├── preflight/
    │   └── validators/
    ├── processed/
    └── fixtures/
```

> This layout follows KFM Directory Rules: domain folders stay under `connectors/` with lifecycle, governance, and evidence lineage preserved:contentReference[oaicite:2]{index=2}.

---

## 🎯 Quickstart

1. Install dependencies: `pip install -r requirements.txt`  
2. Configure county sources in `config.yaml`  
3. Run ingest: `python ingest/run_county_ingest.py --county FIPS_CODE`  
4. Validate: `python preflight/checks.py --layer <layer_name>`  
5. Promote to **CATALOG** after QA passes  

---

## 📌 KFM Notes

- Start with **hydrology or ecology proof lanes** before integrating sensitive county layers:contentReference[oaicite:3]{index=3}.  
- New datasets must pass **EvidenceBundle resolution** and **policy gates** before ingest.  
- Connector ensures reproducible spatial joins, full audit trail, and governance compliance.  
- Layered fallback ensures deterministic assignment for unaligned geometries.
