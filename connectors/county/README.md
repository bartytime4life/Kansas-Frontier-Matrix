<!--
KFM Meta Block V2
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
notes: [Combined, repo-ready README for the County Connector module; reconciles prior drafts, aligned with KFM Directory Rules, evidence-first, and governance posture]
-->

# County Connector README

> **Purpose:** Ingest and harmonize county-level geospatial datasets into KFM with fully auditable, evidence-resolved joins and lifecycle governance.

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
- **Deterministic Joins:** Official crosswalks first, spatial overlays second, centroids/outlet snaps as fallbacks.
- **Governance:** Logs dataset version, join method, tolerance, and EvidenceBundle reference for audit.
- **Auditability:** Supports DecisionEnvelope tracking for manual overrides or exceptions.
- **Public Safety:** Deny-by-default for sensitive data (living persons, rare species, critical infrastructure).

---

## 📚 Overview

The **County Connector** implements hierarchical, deterministic spatial joins:

1. **Official Crosswalks**  
   COMID ⇄ HUC12 mappings from NHDPlus V2.1 or equivalent trusted sources.
2. **Catchment–Polygon Overlay**  
   Polygon-to-polygon spatial joins where official mappings are missing.
3. **Centroid Fallback**  
   Assign points to the containing HUC/county polygon when overlaps are ambiguous.
4. **Outlet Snap (Pour Point)**  
   Last-resort assignment based on pour point proximity to hydrography.

> **Audit Note:** All join tolerances, snap distances, and dataset versions must be recorded in the EvidenceBundle.

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

* [ ] Verify official crosswalks are current
* [ ] Spatial overlay tolerances recorded
* [ ] Centroid and snap fallback logged
* [ ] EvidenceBundle and DecisionEnvelope linked
* [ ] Policy and rights checks enforced
* [ ] Sensitive or restricted data DENY-by-default
* [ ] Lifecycle (RAW → WORK → PROCESSED → CATALOG → PUBLISHED) respected:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🛠 Usage

```bash
# Run ingest for a specific county
python ingest/run_county_ingest.py --county FIPS_CODE

# Validate preflight for a specific layer
python preflight/checks.py --layer parcels_sedgwick

# Example CLI with EvidenceBundle logging
python connect_county.py \
  --input dataset.csv \
  --output aligned.csv \
  --evidence-bundle kfm://evidence/NEEDS_VERIFICATION
```

**Notes:**

- Every output must reference the **EvidenceBundle** used.  
- Manual overrides or exceptions must be captured in **DecisionEnvelope**.  
- All layers progress through KFM lifecycle states; direct RAW/WORK/QUARANTINE access is prohibited:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}.

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

> Placement aligns with KFM Directory Rules: domain folders remain under `connectors/` while preserving lifecycle, governance, and evidence lineage:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}.

---

## 🎯 Quickstart

1. Install dependencies: `pip install -r requirements.txt`
2. Configure county sources in `config.yaml`
3. Run ingest: `python ingest/run_county_ingest.py --county FIPS_CODE`
4. Validate: `python preflight/checks.py --layer <layer_name>`
5. Promote to CATALOG after QA passes

---

## 📌 KFM Notes

- Always start with **hydrology or ecology proof lanes** before integrating sensitive county layers:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}.  
- Any new dataset must first pass **EvidenceBundle resolution** and **policy gates**.  
- Connector design ensures **reproducible spatial joins** and full **audit trail** for every county.
