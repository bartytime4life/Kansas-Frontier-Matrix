---
title: "📊 Kansas Frontier Matrix — Analytics Pipeline Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/analytics-guide.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-analytics-guide-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "analytics-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Analytics Pipeline Guide**  
`docs/guides/pipelines/analytics-guide.md`

**Purpose**  
Define the **canonical architecture and governance pattern** for all analytics pipelines  
in the Kansas Frontier Matrix (KFM).  
Analytics pipelines consume validated data from `processed/`, apply **deterministic  
analysis models**, integrate **FAIR+CARE v2**, emit **lineage v2**, register results  
in the **Governance Ledger**, and publish **STAC/DCAT/Graph/RDF** artifacts when required.

This guide governs:
- Time-series analytics  
- Climate & drought indicators  
- Hazard models  
- Hydrology & remote-sensing analytics  
- AI-assisted analytics pipelines  
- Aggregation / summarization pipelines  

</div>

---

# 📘 Overview

Analytics pipelines operate *after* ingestion + preprocessing + GX validation and  
transform certified `processed/` datasets into:

- Derived analytics layers (tabular, raster, vector)  
- Indicators (climate, hydrology, hazards)  
- Feature sets for AI pipelines  
- Summaries for Story Nodes  
- Aggregated or resampled geospatial layers  
- Multi-temporal composites  
- Metadata-rich outputs ready for publication  

All analytics pipelines must:

- Be **deterministic** (same input → same output)  
- Emit **lineage v2** bundles  
- Integrate **CARE v2 governance** at every output  
- Emit **telemetry v2**  
- Pass CI governance checks  
- Produce **publish-ready** artifacts (STAC/DCAT/RDF) when applicable  

---

# 🗂️ Directory Layout (Canonical Analytics Layer)

~~~text
src/pipelines/analytics/
├── README.md                           # This guide’s architecture for analytics
├── config.py                           # Domain parameters, AOIs, periods, thresholds
├── run_analytics.py                    # Main orchestrator
├── steps/
│   ├── load_inputs.py                  # Load processed datasets
│   ├── spatial_ops.py                  # Spatial transformations (resample, clip, AOI)
│   ├── temporal_ops.py                 # Rolling windows, aggregates, anomaly detection
│   ├── models.py                       # Climate/hazard models, indices, regressions
│   ├── indicators.py                   # Derived metrics (SPI, SPEI, NDVI, etc.)
│   ├── summaries.py                    # Statistical summaries, trend extraction
│   ├── governance.py                   # CARE v2 logic for analytics outputs
│   ├── telemetry.py                    # Telemetry v2 emission
│   └── write_outputs.py                # Save outputs into data/processed + catalogs
└── utils/
    ├── math_utils.py                   # Z-scores, rolling ops
    ├── geo_utils.py                    # Raster/Vector utilities
    ├── time_utils.py                   # Temporal handling
    └── io_utils.py                     # I/O helpers
~~~

---

# 📊 Analytics Architecture (GitHub-Safe Mermaid)

```mermaid
flowchart TD

subgraph LOAD["Load Inputs"]
  A["Processed Inputs<br/>data/processed/<dataset>/<version>"]
end

subgraph ANALYTICS["Analytics Ops"]
  B["Spatial Ops<br/>clip · resample · join"]
  C["Temporal Ops<br/>rolling · anomaly · windows"]
  D["Models<br/>hazard · climate · hydrology"]
  E["Indicators<br/>SPI · SPEI · NDVI etc."]
end

subgraph OUTPUTS["Output Assembly"]
  F["Outputs<br/>tabular · raster · vector · summaries"]
end

subgraph GOVERN["Governance Layer"]
  G["CARE v2 Enforcement"]
  H["Provenance + Lineage v2"]
  I["Telemetry v2"]
end

subgraph PUBLISH["Publication"]
  J["STAC · DCAT · Neo4j · RDF (optional)"]
end

A --> B --> C --> D --> E --> F --> G --> H --> I --> J

classDef load fill:#ebf8ff,stroke:#2b6cb0,color:#1a365d;
classDef anal fill:#faf5ff,stroke:#805ad5,color:#553c9a;
classDef out fill:#f0fff4,stroke:#38a169,color:#22543d;
classDef gov fill:#fffbea,stroke:#dd6b20,color:#7b341e;
classDef pub fill:#fff5f5,stroke:#e53e3e,color:#742a2a;

class LOAD load;
class ANALYTICS anal;
class OUTPUTS out;
class GOVERN gov;
class PUBLISH pub;
````

---

# 1️⃣ Load Inputs

Analytics pipelines **must** read from official:

```text
data/processed/<dataset>/<version>/
```

Inputs must include:

* `processed_manifest.json`
* Any rasters/vectors/tables (aligned to KFM schemas)
* Lineage v2
* CARE v2 metadata
* Telemetry references

Loading step MUST:

* Validate checksums and manifest integrity
* Validate careLabel + maskingStrategy
* Load lineage chain to support analysis metadata

---

# 2️⃣ Spatial Operations

Spatial operations include:

* Clip to AOI
* Reproject (if needed)
* Resample (nearest/bilinear/cubic as appropriate)
* Spatial join
* Aggregation to H3 cells
* Mosaic / merge

Spatial ops must:

* Maintain CRS consistency
* Ensure no increase in resolution beyond source dataset
* Carry forward CARE v2 masking and sovereignty logic
* Emit intermediate telemetry

---

# 3️⃣ Temporal Operations

Temporal operations include:

* Rolling mean/median
* Windowed variance
* Monthly/seasonal composites
* Year-over-year anomalies
* Breakpoint detection (climate trends)
* Time alignment (OWL-Time consistency)

Temporal ops must:

* Preserve monotonic timestamps
* Validate temporal models
* Carry temporal metadata into lineage

---

# 4️⃣ Models (Hazards · Climate · Hydrology)

Analytics pipelines may implement domain models:

## 4.1 Hazard Models

* Drought index (SPI/SPEI)
* Flood risk indices
* Fire weather index
* Severe weather clusters

## 4.2 Climate Models

* Temperature anomaly detection
* Precipitation trend regression
* Heatwave modeling
* ENSO signal extraction

## 4.3 Hydrology Models

* Basin runoff estimation
* Streamflow anomaly detection
* Soil moisture modeling
* Snowpack/cryosphere indicators

All models must be:

* **Deterministic**
* Versioned (`model_version`)
* Explainable (model metadata into lineage)
* CARE v2 aware (mask sensitive watersheds or tribal areas as required)

---

# 5️⃣ Indicators

Indicators (NDVI, EVI, SPI, SPEI, NDWI, etc.) must:

* Maintain physical meaning
* Be versioned (`indicator_version`)
* Carry metadata:

  * source datasets
  * derivation chain
  * units
  * resolution
  * temporal coverage

Indicators are saved under:

```text
data/processed/<indicator>/<version>/
```

and linked in lineage.

---

# 6️⃣ Output Assembly

Outputs can include:

* **Tabular** (CSV/Parquet)
* **Raster** (COG GeoTIFF)
* **Vector** (GeoJSON/FlatGeobuf)
* **Summaries** (JSON)
* **Graphs/derived features**

Every output MUST:

* Include CARE v2 metadata
* Include lineage v2 reference
* Include telemetry reference
* Include checksums.txt
* Pass post-output sanity checks

---

# 7️⃣ Governance Layer

Governance checks integrate:

## 7.1 CARE v2 Enforcement

* Propagate careLabel from inputs
* Apply new masking if outputs increase resolution or reveal new sensitive details
* Update `maskingStrategy` and `sovereigntyFlags`

## 7.2 Lineage v2

Analytics lineage must record:

* Inputs used
* Spatial + temporal transforms
* Models and indicator logic
* CARE decisions
* Telemetry summary

Stored in:

```text
data/processed/lineage/<analytics_type>/<version>.jsonld
```

## 7.3 Telemetry v2

Minimum fields:

* `stage: "analytics"`
* `duration_ms`
* `model_version` / `indicator_version`
* `rows_processed` / `pixels_processed`
* `energy_wh`, `co2_g`
* `care_violations`
* `errors`

---

# 8️⃣ Publication (Optional Per Pipeline)

If analytics create publishable layers:

* Build STAC Item (+ update Collection)
* Build DCAT Dataset JSON-LD
* Create Neo4j nodes/edges
* Generate RDF GeoSPARQL triples

All require Promotion Gate compliance:

* proper CARE v2 masking
* complete lineage v2 bundle
* telemetry integration
* checksums
* governance ledger registration

---

# 9️⃣ CI Enforcement

Analytics pipelines MUST pass:

| Workflow                   | Responsibility                   |
| -------------------------- | -------------------------------- |
| `analytics-validate.yml`   | Basic validation + schema checks |
| `faircare-validate.yml`    | CARE v2 governance               |
| `lineage-validate.yml`     | Lineage v2 JSON-LD validation    |
| `stac-validate.yml`        | STAC structure (if publishing)   |
| `dcat-validate.yml`        | DCAT validation (if publishing)  |
| `linked-data-validate.yml` | RDF/GeoSPARQL validation         |
| `telemetry-export.yml`     | Telemetry v2 validation          |
| `sbom-validate.yml`        | Supply-chain integrity           |
| `docs-lint.yml`            | Markdown protocol compliance     |

---

# 🔟 Developer Checklist

* [ ] Input datasets validated & in `processed/`
* [ ] CARE v2 metadata read + applied
* [ ] Spatial/temporal operations deterministic
* [ ] Model version recorded
* [ ] Lineage v2 bundle created
* [ ] Telemetry v2 emitted
* [ ] Governance ledger updated
* [ ] STAC/DCAT/RDF/Graph written (if required)
* [ ] All CI workflows green

---

# 🕰 Version History

| Version | Date       | Summary                                                                              |
| ------: | ---------- | ------------------------------------------------------------------------------------ |
| v10.4.2 | 2025-11-16 | Initial analytics-guide.md aligned to KFM v10.4.2; CARE v2, lineage v2, telemetry v2 |

---

<div align="center">

**Kansas Frontier Matrix — Analytics Pipeline Guide (v10.4.2)**
Deterministic Analytics × FAIR+CARE v2 × Lineage v2 × Publishing Gate Compliance
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
