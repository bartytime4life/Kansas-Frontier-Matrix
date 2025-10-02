<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Data Source Request

<!-- Core CI/CD -->
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  

<!-- Security -->
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](../../.github/workflows/secret-scanning.yml)  
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](../../.github/workflows/ossf-scorecard.yml)  

<!-- Governance -->
[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../../.github/workflows/roadmap.yml)  
[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](../../.github/workflows/labels.yml)  
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](../../.github/workflows/pr-labeler.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../.github/workflows/automerge.yml)  

<!-- Repo Hygiene -->
![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 📂 Dataset

- **Name:**  
- **Publisher/Host:**  
- **URL / Access Notes:**  
- **License / Usage:**  

---

## 🌍 Coverage & Schema

- **Spatial extent (bbox or AOI):**  
- **Temporal range:**  
- **Format(s):** (COG, GeoJSON, MBTiles, CSV, Shapefile, PDF, etc.)  
- **Key attributes / schema fields:**  

---

## 📑 Use Cases

_What layers, maps, or stories will this dataset support?_  
- Timeline or story relevance  
- Viewer/UI integration potential  

---

## 🧾 Provenance & Reliability

- **Citation(s):**  
- **Update cadence:**  
- **Versioning policy:**  
- **Known caveats/uncertainties:**  

---

## 📦 Integration Plan

- **Proposed storage:** Git LFS / DVC / small in-repo  
- **Proposed STAC entry:** Collection or Item (`stac/collections/**`, `stac/items/**`)  
- **Derivatives needed?** (hillshade, slope, tiles, etc.)  

---

## 🧮 Validation & Checks

```bash
# Sanity check JSON structure
jq -e 'type=="object"' data/sources/<file>.json

# Validate STAC (if draft provided)
kgt validate-stac stac/items --no-strict || true
````

---

## 📑 Roadmap Link (if applicable)

* Milestone: …
* Related epic/issue: …
* Roadmap marker:

  ```
  <!-- roadmap:key=source-<stable-key> -->
  ```

---

## ✅ Checklist

* [ ] Source & license verified (redistribution OK or documented)
* [ ] Spatial/temporal coverage specified
* [ ] Draft **STAC entry** or **source descriptor** proposed
* [ ] Validation steps included (`jq`, `kgt validate-stac`)
* [ ] Roadmap/milestone linkage (if relevant)
