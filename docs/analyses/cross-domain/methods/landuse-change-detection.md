---
title: "🏞️ Kansas Frontier Matrix — Land Use Change Detection Methods (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/cross-domain/methods/landuse-change-detection.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Historical Ecology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/analyses-crossdomain-landusechange-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏞️ **Kansas Frontier Matrix — Land Use Change Detection Methods**
`docs/analyses/cross-domain/methods/landuse-change-detection.md`

**Purpose:**  
Document the geospatial and statistical methods used to detect and quantify **land use and land cover (LULC) changes** across Kansas within the **Cross-Domain Analytical Framework**.  
This methodology integrates **remote sensing, historical cartography, census data**, and **hydrological overlays** to produce FAIR+CARE-compliant insights into ecological and cultural landscape transformation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

The **Land Use Change Detection Method** analyzes **temporal transitions** in Kansas’s landscape from the 1850s to 2025, combining:
- Historical maps, treaty data, and agricultural censuses  
- Remote sensing land cover datasets (NLCD, ESA CCI, Landsat)  
- Hydrological and ecological overlays  
- AI-assisted raster differencing for land cover classification  

This method supports cross-domain findings on **land degradation**, **urban expansion**, and **wetland loss** while maintaining ethical governance for **Indigenous territories** and culturally sensitive sites.

---

## 🗂️ Directory Context

```
docs/analyses/cross-domain/methods/
├── README.md
├── landuse-change-detection.md     # This file
├── ethical-cartography.md
└── hydro-geo-modeling.md
```

---

## ⚙️ Analytical Workflow

| Step | Process | Tools / Frameworks | Output |
|------|----------|--------------------|---------|
| **1. Data Acquisition** | Collect historical maps, census tracts, and satellite imagery. | QGIS, GDAL, ESA CCI API | GeoTIFF & CSV datasets |
| **2. Image Preprocessing** | Reproject, mosaic, and normalize rasters to a common grid. | GDAL, rasterio | `landuse_1850_2025_stack.tif` |
| **3. Classification** | Apply supervised classification (Random Forest, SVM). | Scikit-learn, ArcGIS Pro | LULC maps |
| **4. Change Detection** | Compute raster differencing and post-classification transitions. | NumPy, OpenCV | Change matrix & maps |
| **5. Historical Overlay** | Overlay treaty and census data for context. | geopandas, FAIRCARE Validator | `treaty-landuse-overlap.geojson` |
| **6. FAIR+CARE Validation** | Perform ethical governance review and metadata audit. | FAIRCARE Validator | `faircare-validation.json` |

---

## 🧩 Algorithms & Equations

### 1️⃣ **Normalized Difference Built-up Index (NDBI)**
$begin:math:display$
NDBI = \\frac{SWIR - NIR}{SWIR + NIR}
$end:math:display$

### 2️⃣ **Change Detection Matrix**
$begin:math:display$
C_{ij} = \\frac{n_{ij}}{N}
$end:math:display$
Where:
- $begin:math:text$C_{ij}$end:math:text$ = probability of transition from class i → j  
- $begin:math:text$n_{ij}$end:math:text$ = number of pixels changing from i → j  
- $begin:math:text$N$end:math:text$ = total number of pixels in class i  

### 3️⃣ **Classification Accuracy**
$begin:math:display$
OA = \\frac{TP + TN}{TP + TN + FP + FN}
$end:math:display$
- $begin:math:text$OA$end:math:text$: Overall Accuracy, validated using confusion matrix and ground truth.

---

## 🌍 Input Datasets

| Dataset | Description | Source | License |
|----------|-------------|---------|----------|
| `historical_treaty_boundaries.geojson` | Digitized historical boundaries (1850–1890). | Kappler’s Indian Affairs | CC-BY 4.0 |
| `landuse_1950_2020.tif` | Multi-temporal land cover classification (ESA CCI, NLCD). | ESA / USGS | CC-BY 4.0 |
| `census_agriculture_tracts.csv` | Historical agricultural tract records (1900–2020). | USDA / KHS | CC-BY 4.0 |
| `hydrographic_network.geojson` | River and watershed shapefiles. | KFM Hydrology | CC-BY 4.0 |

---

## 🧠 FAIR+CARE Integration

| FAIR Principle | Implementation | CARE Principle | Implementation |
|---|---|---|---|
| **Findable** | Indexed by STAC/DCAT catalog and searchable by era. | **Collective Benefit** | Supports community awareness and sustainable planning. |
| **Accessible** | Maps and change matrices published under open license. | **Authority to Control** | Indigenous overlays require IDGB consent. |
| **Interoperable** | GeoTIFF, CSV, and GeoJSON standardized outputs. | **Responsibility** | Ethical metadata embedded in map legends and files. |
| **Reusable** | Documented workflow ensures repeatability. | **Ethics** | Prevents misuse or oversimplification of historical transitions. |

---

## 🧮 Example Implementation (Python Pseudocode)

```python
import rasterio
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# Load two rasters
with rasterio.open("landuse_1950.tif") as src1, rasterio.open("landuse_2020.tif") as src2:
    lu1 = src1.read(1)
    lu2 = src2.read(1)

# Compute change matrix
change_matrix = np.zeros((len(np.unique(lu1)), len(np.unique(lu2))))
for i in np.unique(lu1):
    for j in np.unique(lu2):
        change_matrix[i-1, j-1] = np.sum((lu1 == i) & (lu2 == j))

# Normalize
change_matrix /= change_matrix.sum()
print("Land use transition probabilities:\n", change_matrix)

# Train RF for land use classification (optional step)
X_train, y_train = ..., ...
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)
```

---

## 📊 Output Artifacts

| File | Description |
|------|--------------|
| `landuse-change-matrix.csv` | Tabulated pixel-level land use transitions. |
| `landuse-change-map.png` | Visual representation of LULC transitions. |
| `treaty-overlay-visualization.png` | Overlay of historical and modern land use. |
| `faircare-validation.json` | Ethical review log confirming consent metadata. |

---

## 🧾 Example FAIR+CARE Telemetry Log

```json
{
  "analysis_id": "crossdomain_landuse_change_v10",
  "datasets_used": [
    "landuse_1950_2020.tif",
    "historical_treaty_boundaries.geojson"
  ],
  "methods": ["landuse-change-detection.md", "ethical-cartography.md"],
  "faircare_score": 97.8,
  "explainability_index": 95.2,
  "consent_verified": true,
  "validated_by": ["FAIR+CARE Council", "Indigenous Data Governance Board"],
  "last_validated": "2025-11-09"
}
```

---

## ⚙️ Validation Workflows

| Workflow | Purpose | Artifact |
|-----------|----------|----------|
| `analysis-validation.yml` | Confirms dataset–method–result linkage and accuracy. | `reports/analyses/reproducibility-summary.json` |
| `landuse-validation.yml` | Validates raster alignment, class accuracy, and CRS. | `reports/analyses/landuse-validation.json` |
| `faircare-audit.yml` | Verifies ethical and cultural compliance for sensitive datasets. | `reports/data/faircare-validation.json` |
| `telemetry-export.yml` | Logs land-use modeling metadata and FAIR+CARE scores. | `releases/v10.0.0/focus-telemetry.json` |

---

## 📈 Quality Metrics

| Metric | Target | Verified By |
|--------|---------|-------------|
| **Classification Accuracy (OA)** | ≥ 85% | CI Validation |
| **FAIR+CARE Compliance** | ≥ 95% | Governance Council |
| **Spatial Alignment (CRS)** | 100% EPSG:4326 | Data Standards Team |
| **Provenance Completeness** | 100% | FAIR+CARE Council |
| **Consent Validation** | 100% (cultural datasets) | IDGB |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE Historical Ecology Council | Added reproducible land use change detection methodology integrating historical, hydrological, and ecological layers with ethical FAIR+CARE compliance. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Methods Index](README.md) · [Hydro–Geo Modeling →](hydro-geo-modeling.md)

</div>
