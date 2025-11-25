---
title: "🌿 Kansas Frontier Matrix — Paleoenvironment Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/paleoenvironment/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Sovereignty Review Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_guid: "urn:kfm:doc:archaeology-paleoenvironment-v11.0.0"
doc_kind: "Dataset Category"
intent: "archaeology-paleoenvironment-datasets"
semantic_document_id: "kfm-doc-archaeology-paleoenvironment"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenvironment-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Sovereignty-Governed"
sensitivity: "Environmental · Archaeological"
sensitivity_level: "Low–Moderate"
indigenous_data_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Governed Public"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Paleoenvironment Datasets (v11)**  
`docs/analyses/archaeology/datasets/paleoenvironment/README.md`

FAIR+CARE v11 · Sovereignty-Governed  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

---

# 📘 Overview (v11)

The **Paleoenvironment Layer** provides environmental context for archaeological interpretation across prehistoric, protohistoric, and historic Kansas.  
This includes:

- Pollen and macrofossil reconstruction  
- Charcoal accumulation → fire regime inference  
- Lake/river sediment geochemistry  
- Dendrochronological climate series  
- Hydroclimate proxies (SPEI, PDSI, RCS anomalies)  
- Paleoecological AI-assisted reconstructions (v11 explainability-required)

All datasets are:

- **FAIR+CARE v11 certified**  
- **Culturally reviewed** (if relevant)  
- **PROV-O v11 lineage recorded**  
- **STAC/DCAT v11 compliant**  
- **Generalized via H3 r7–r10** when eco-cultural sensitivity applies  

---

# 🗂 Directory Layout (v11 · ASCII-only · Box-safe)

~~~text
docs/analyses/archaeology/datasets/paleoenvironment/
├── README.md                  # This file
├── pollen/                    # Pollen cores, vegetation proxies
├── charcoal/                  # Charcoal/fire histories
├── fauna/                     # Open-access fauna-only paleo data
├── sediments/                 # Lake/river cores, geochemistry
├── dendrochronology/          # Tree-ring climate signals
├── climate-proxies/           # SPEI/PDSI/temperature/hydro indicators
├── stac/                      # STAC v11 items + collections
├── metadata/                  # DCAT 3.0 + CARE v11 metadata
└── provenance/                # PROV-O v11 lineage bundles
~~~

---

# 🧭 Paleoenvironment Dataset Categories (v11)

| Category | Description | CARE Level | Allowed | Notes |
|---------|-------------|------------|---------|------|
| **Pollen Cores** | Vegetation composition through time | C1 | Yes | Must include depth–age model |
| **Charcoal Proxies** | Fire frequency & biomass burning | C1 | Yes | Temporal calibration required |
| **Faunal Paleo Data** | Fauna shifts, extinction markers | C2 | Conditional | Sacred species must be excluded |
| **Sediment Cores** | Basin stratigraphy & geochemistry | C1 | Yes | May require H3 generalization |
| **Dendrochronology** | Tree-ring climate series | C1 | Yes | PD datasets only |
| **Climate Proxy Layers** | Aridity, drought, and hydrology indices | C1 | Yes | Derivative models must include metadata |
| **Ancient Hydrology** | Paleo flood/drought cycles | C2–C3 | Conditional | Must avoid sensitive tribal hydrology |

Forbidden (v11):

- Burial-associated eco-samples  
- Tribal-restricted hydrology or ecology datasets  
- Proprietary or unvalidated core datasets  
- Faunal records containing sacred species metadata  
- Exact coordinates for protected ecological features  

---

# 📦 Metadata Requirements (v11)

## STAC v11 Item Requirements

Fields required:

- `stac_version: "1.0.0"`
- Unique `id`
- H3-generalized `bbox`
- Polygon or point geometry (generalized)
- OWL-Time `start_datetime` / `end_datetime`
- `care:sensitivity`, `care:sovereignty`, `care:consent_status`
- `kfm:proxy_type` (pollen, charcoal, etc.)
- `kfm:generalization` (H3-r7 to H3-r10)
- `kfm:provenance` → PROV-O file
- Asset links for CSV/COG/GeoJSON

## DCAT 3.0 Requirements

- `dct:title`, `dct:description`
- `dct:temporal`
- `dct:license` (CC-BY/CC0/PD)
- `dcat:distribution` entries
- Keywords for “paleoenvironment”, “archaeology”, “climate proxy”

## CARE v11 Requirements

- Cultural notes for eco-cultural relevance  
- Sovereignty governance route  
- Consent verification & review board  
- Eco-cultural sensitivity flagging  
- Required masking for sensitive fauna or hydrology  

---

# 🧪 Data Preparation Requirements (v11)

All datasets must include:

- **Depth–age modeling** (Bayesian, linear, or RCS)  
- **Error bounds** (σ or CI)  
- **Sampling metadata** (interval, lab method, calibration curve)  
- **Climate proxy metadata** (`aridity_index`, `charcoal_flux`, `pollen_pct`)  
- **Standardized schema fields**  
- **PROV-O v11 lineage bundle**

Generalization rules:

- Replace exact lake/pond coordinates with H3 r7–r10 mosaic  
- Remove sacred or restricted fauna flags  
- Remove exact locations of culturally protected eco-features  

---

# 🛰 KFM System Integration (v11)

## Neo4j Knowledge Graph

Nodes:
- `PaleoRecord`
- `PollenCore`
- `CharcoalProxy`
- `SedimentLayer`
- `TreeRingSeries`
- `ClimateProxy`
- `HydroProxy`

Relationships:
- `INDICATES`
- `CORRELATED_WITH`
- `LOCATED_AT`
- `OCCURRED_DURING`
- `GENERALIZED_FROM`
- `SUPPORTED_BY_PROVENANCE`

## Story Node v3 Integration

- Environmental context for cultural timelines  
- Fire regime transitions  
- Climate-linked occupation shifts  
- Ecology–culture narratives  

## Focus Mode v3 Integration

- AI-assisted summaries with required provenance chips  
- Uncertainty bands for proxy data  
- CARE-governed tone filters  
- Explainability overlays (SHAP/IG)  

## Visualization

- Pollen density reconstructions  
- Charcoal flux rasters  
- Hydroclimate anomaly tiles  
- Cesium 3D sediment models  

---

# 📊 Dataset Index (v11)

| Dataset | Category | Status | Review | Notes |
|--------|----------|--------|--------|-------|
| `pollen/flint-hills-core-v2` | Pollen | 🟢 Active | 2025-11 | Depth–age model validated |
| `charcoal/prairie-fire-history-v2` | Charcoal | 🟢 Active | 2025-11 | Proxy normalization validated |
| `fauna/pleistocene-fauna-v1` | Faunal | 🟡 Needs Review | 2025-09 | Sacred species check required |
| `sediments/smoky-hill-core-v3` | Sediments | 🟢 Active | 2025-11 | Geochemical metadata v11-complete |

---

# 🧠 Example STAC Item (v11)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "pollen-flint-hills-v2",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "properties": {
    "kfm:proxy_type": "pollen",
    "care:sensitivity": "generalized",
    "care:sovereignty": "approved",
    "care:consent_status": "verified",
    "start_datetime": "8500-01-01T00:00:00Z",
    "end_datetime": "2020-01-01T00:00:00Z",
    "kfm:generalization": "H3-r8",
    "kfm:provenance": "provenance/pollen-flint-hills-v2.json"
  },
  "assets": {
    "core_data": {
      "href": "https://example.org/paleo/pollen/flint_hills_core_v2.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.0.0** | 2025-11-24 | Full v11 rebuild: sovereignty gates, CARE v11, H3 r7–r10, PROV-O v11, STAC/DCAT v11, telemetry v11 |
| v10.4.0 | 2025-11-17 | First complete v10 paleoenvironment index |
| v10.0.0 | 2025-11-10 | Initial dataset structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE v11 · Sovereignty-Governed  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Archaeology Datasets](../README.md)

</div>