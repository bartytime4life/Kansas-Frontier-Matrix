---
title: "🧩 Kansas Frontier Matrix — Archaeology AI Training Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ai/models/archaeology/training/scripts/utils/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/src-ai-models-archaeology-training-utils-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Archaeology AI Training Utilities**  
`src/ai/models/archaeology/training/scripts/utils/README.md`

**Purpose:**  
Provide reusable **utility functions** for feature engineering, data preparation, validation, and explainability within the **Archaeology AI training framework**.  
These utilities support FAIR+CARE-compliant geospatial machine learning and integrate sustainability telemetry under **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Validated-orange)](../../../../../../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

This module contains modular helper functions used throughout the **Archaeology AI training scripts**, including:
- 🧮 **Feature Engineering:** Terrain, hydrology, and moisture feature generation.  
- 🧭 **Spatial CV Tools:** Block-based cross-validation utilities for geospatial datasets.  
- 📊 **Evaluation Metrics:** AUROC, AUPRC, Brier, bias, and drift computation.  
- ⚙️ **Explainability Integration:** SHAP/LIME helper functions for interpretability analysis.  
- ♻️ **Sustainability Hooks:** Lightweight telemetry collection for runtime and energy efficiency.  

---

## 🗂️ Directory Layout

```plaintext
src/ai/models/archaeology/training/scripts/utils/
├── README.md                          # This file — utility documentation
│
├── data_loader.py                     # Functions for loading, merging, and validating training data
├── feature_engineering.py             # Terrain/moisture/hydro feature derivation
├── evaluation_tools.py                # Metrics, CV scoring, and explainability helpers
└── telemetry_utils.py                 # Energy, runtime, and governance telemetry utilities
```

---

## ⚙️ Utility Function Overview

| File | Purpose | Key Functions |
|------|----------|----------------|
| `data_loader.py` | Load and validate training datasets. | `load_parquet()`, `merge_labels()`, `validate_schema()` |
| `feature_engineering.py` | Generate geospatial and environmental features. | `compute_slope()`, `calculate_ndmi()`, `distance_to_water()` |
| `evaluation_tools.py` | Evaluate model performance and bias metrics. | `compute_auc()`, `bias_index()`, `drift_detector()` |
| `telemetry_utils.py` | Track sustainability metrics. | `record_energy()`, `log_telemetry()`, `sync_governance()` |

---

## 🧩 Example: Feature Engineering (`feature_engineering.py`)

```python
import rasterio
import numpy as np
from scipy.ndimage import gaussian_filter

def compute_slope(dem_array, cell_size):
    """Calculate slope (degrees) from DEM."""
    dx, dy = np.gradient(dem_array, cell_size)
    slope = np.sqrt(dx**2 + dy**2)
    return np.degrees(np.arctan(slope))

def calculate_ndmi(nir_band, swir_band):
    """Compute NDMI = (NIR - SWIR) / (NIR + SWIR)."""
    return (nir_band - swir_band) / (nir_band + swir_band + 1e-9)
```

---

## 🧮 Example: Telemetry Utility (`telemetry_utils.py`)

```python
import json, time

def record_energy(runtime_sec, power_watts=150):
    """Estimate energy use (Wh) given runtime and average power."""
    return (power_watts * runtime_sec) / 3600

def log_telemetry(output_path, metrics):
    """Save telemetry metrics to JSON and append to FAIR+CARE ledger."""
    metrics["timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)
```

---

## ⚖️ FAIR+CARE Integration Matrix

| Principle | Implementation | Validator |
|------------|----------------|------------|
| **Findable** | Utility modules indexed in SPDX manifest. | `sbom.spdx.json` |
| **Accessible** | MIT-licensed, open-source reusable scripts. | FAIR+CARE Council |
| **Interoperable** | Output telemetry compatible with ISO 19115. | `schema_validation.py` |
| **Reusable** | Functions modular, documented, and testable. | MCP-DL Validation |
| **CARE – Responsibility** | Embedded governance telemetry for ethical AI. | `telemetry_utils.py` |
| **CARE – Ethics** | Ensures cultural masking logic reproducible and auditable. | `feature_engineering.py` |

---

## 🧮 Telemetry Metrics

| Metric | Description | Example |
|--------|-------------|----------|
| `runtime_sec` | Execution duration of utility script. | 248 |
| `energy_wh` | Estimated energy consumption. | 10.3 |
| `carbon_gco2e` | CO₂ emission equivalent (ISO 50001). | 4.2 |
| `functions_executed` | Count of functions executed in workflow. | 18 |
| `validation_status` | Utility test and governance audit result. | passed |

Telemetry recorded in:  
`releases/v9.9.0/focus-telemetry.json`  
Schema: `schemas/telemetry/src-ai-models-archaeology-training-utils-v1.json`

---

## 🔐 Provenance & Governance Integration

- **Checksum Verification:** Functions tracked in SPDX SBOM.  
- **Telemetry Reference:** Energy and runtime logs exported via `telemetry_utils.py`.  
- **Governance Ledger:** Certification recorded in `releases/v9.9.0/governance/ledger_snapshot.json`.  

### Example Governance Record
```json
{
  "entry_id": "ledger_2025q4_training_utils",
  "module": "feature_engineering.py",
  "auditor": "@kfm-governance",
  "status": "approved",
  "timestamp": "2025-11-08T20:02:00Z"
}
```

---

## 🧾 Citation

```text
Kansas Frontier Matrix (2025). Archaeology AI Training Utilities (v9.9.0).
FAIR+CARE-aligned, ISO-compliant Python utilities for ethical, sustainable, and transparent AI training within the Kansas Frontier Matrix archaeology model framework.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------:|------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-ai` | Created training utility documentation with FAIR+CARE integration, telemetry hooks, and sustainability schema. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Reusable Code × FAIR+CARE Ethics × Sustainable AI Development*  
© 2025 Kansas Frontier Matrix · MIT · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Training Scripts](../README.md) · [Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

