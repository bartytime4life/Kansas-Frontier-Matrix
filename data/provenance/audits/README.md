<div align="center">

# 🧾 Kansas-Frontier-Matrix — Provenance Audits  
`data/provenance/audits/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Provide **dataset-level audit logs** that capture transformations, control points, parameters,  
and quality reports for every dataset in the **Kansas Frontier Matrix**.  

Audits extend the **provenance registry** by storing **detailed reproducibility records**:  
GCP residuals, ETL configs, model parameters, QA/QC checks, and lineage notes.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw data\n(data/raw/**)"] --> B["Process / Transformation\n(scripts, Makefile targets)"]
  B --> C["Audit logs\n(data/provenance/audits/**)"]
  C --> D["Registry entries\n(data/provenance/registry.json)"]
  C --> E["STAC Items\n(data/stac/items/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer + Experiments\n(web/config/** · experiments/**)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Document how each dataset was transformed (tools, parameters, configs)
	•	Provide QA/QC reports (RMS error, validation stats, missing values)
	•	Record GCP alignment results for historic maps and aerials
	•	Store ETL configs for tabular/vector cleanup (field mappings, dissolves)
	•	Guarantee lineage transparency for MCP reproducibility

⸻

📂 Directory Layout

data/provenance/audits/
├── topo_1894_larned_gcp.json    # GCP residuals for USGS Larned topo sheet
├── dem_merge_2018.log           # GDAL/COG conversion + merge parameters
├── floodplain_fema2020_qc.json  # Validation report for FEMA floodplain dataset
├── treaty_overlay_etl.yaml      # ETL config for treaty boundary normalization
└── README.md


⸻

🧭 File Conventions
	•	JSON → QA/QC reports, structured lineage data (residuals, validation stats)
	•	YAML → ETL configs, processing pipelines
	•	LOG / TXT → direct script or GDAL/CLI logs
	•	CSV → tabular QA outputs (point errors, mismatch tables)

Each audit file should include:
	•	Dataset ID (matches registry.json + STAC Item)
	•	Processing date & tool versions
	•	Parameters used (warp order, thresholds, CRS, etc.)
	•	QA/QC results (residuals, completeness, validation checks)
	•	Author / pipeline / commit reference

⸻

📑 Example Audit (GCP residuals for historic topo)

{
  "dataset_id": "usgs_topo_1894_larned",
  "date": "2025-09-22",
  "tool": "gdalwarp",
  "parameters": {
    "order": 2,
    "target_epsg": 4326,
    "points_used": 10
  },
  "qa": {
    "rms_error": 3.1,
    "max_error": 6.4,
    "units": "meters"
  },
  "lineage_commit": "abc123def456",
  "notes": "Residuals acceptable; control points concentrated along Arkansas River confluence."
}


⸻

🔗 Integration
	•	Provenance registry → audit files linked in registry.json under each dataset
	•	STAC Items → kfm:lineage or custom audit:href points to audit file
	•	Makefile workflows → audits generated alongside processing outputs
	•	Experiments → MCP experiment logs cite audits for reproducibility

⸻

📝 Notes
	•	Every non-trivial dataset (warped, merged, modeled, digitized) must have an audit file
	•	Keep audit logs small & structured (JSON/YAML preferred)
	•	Logs are append-only; never overwrite, only version with new commit reference
	•	Store raw GCPs in data/gcp/ → results (residuals, QA) live here in audits

⸻

📚 See Also
	•	../ → provenance registry and licenses
	•	../../gcp/ → Ground Control Points (inputs for georeferencing)
	•	../../stac/items/ → STAC metadata for datasets
	•	../../experiments/ → MCP notebooks + experiment logs

⸻

✅ Mission Principle

Audits are the forensic backbone of Kansas Frontier Matrix.
Every dataset must have a traceable, validated, and reproducible audit trail.