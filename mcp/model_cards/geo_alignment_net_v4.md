---
title: "🗺️ Model Card — Geo Alignment Net v4 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/geo_alignment_net_v4.md"

version: "v11.0.0"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Geospatial Working Group · FAIR+CARE Council · AI Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Card"
header_profile: "standard"
footer_profile: "standard"
intent: "geo-alignment-net-v4"
semantic_document_id: "kfm-modelcard-geo-alignment-net-v4"
doc_uuid: "urn:kfm:modelcard:geo-alignment-net-v4:v11.0.0"
event_source_id: "urn:kfm:modelcard:geo-alignment-net-v4"

machine_extractable: true
classification: "AI Model Documentation"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Ethics · Responsibility"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "mcp/experiments/2025-11-14_GEO-EXP-009.md@v11.0.0"

ai_transform_permissions:
  - "summarize"
  - "extract-metadata"
  - "a11y-adaptations"
  - "layout-normalization"
ai_transform_prohibited:
  - "fabricate-results"
  - "fabricate-provenance"
  - "invent-dataset-ids"
  - "invent-license-rights"
  - "override-governance"
  - "expose-sensitive-coordinates"
  - "deanonymize"
---

<div align="center">

# 🗺️ **Geo Alignment Net v4 — Model Card (v11 LTS)**
`mcp/model_cards/geo_alignment_net_v4.md`

**Purpose**  
Document architecture, evaluation, governance, and provenance for **Geo Alignment Net v4 (GAN‑v4)** —
KFM’s geospatial harmonization and alignment model used for coordinate correction, shape adjustment,
vertical-datum normalization, raster alignment, and multi-source GIS integration.

</div>

---

## 📘 Overview

**Geo Alignment Net v4 (GAN‑v4)** is a hybrid deep geospatial alignment model combining:

- CNN-based spatial feature detectors
- coordinate residual regression heads
- multigrid cross-scale attention
- vertical datum adjustment nets (NAVD88 ↔ NGVD29 ↔ EGM96)
- H3-aware spatial correction logic

GAN‑v4 assists with:

- aligning historical maps to modern basemaps
- correcting scanned GIS layers
- harmonizing multi-source geospatial datasets
- detecting and fixing raster/feature offsets
- aligning hydrology, climate, landcover, and archaeology layers (subject to governance rules)
- improving map accuracy for Story Nodes and Focus Mode v3

**Non-goals**
- GAN‑v4 does not create new geometries; it refines and aligns existing geometries.
- GAN‑v4 must not be used to infer sensitive cultural locations or produce precision outputs for restricted geographies.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 model_cards/
│   │   └── 📄 geo_alignment_net_v4.md                   # This model card (GAN‑v4)
│   └── 📁 experiments/
│       └── 📄 2025-11-14_GEO-EXP-009.md                 # Training / evaluation run log (as referenced)
├── 📁 src/
│   └── 📁 pipelines/
│       ├── 📁 geo_alignment/                            # Alignment pipeline stages (as referenced)
│       ├── 📁 climate/                                  # Downstream raster alignment consumers
│       └── 📁 hydrology/                                # Downstream alignment consumers
├── 📁 data/
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 geo_alignment_net_v4/
│               └── 📁 <timestamp>/
│                   ├── 🧾 prov.jsonld                   # PROV‑O JSON‑LD
│                   ├── 🧾 openlineage.json              # OpenLineage event(s)
│                   ├── 🧾 config_snapshot.json          # Run configuration snapshot
│                   └── 🧾 checksums.json                # Output checksums
└── 📁 releases/
    └── 📁 v11.0.0/
        └── 🧾 mcp-modelcards-telemetry.json             # Energy/carbon/runtime telemetry bundle
~~~

---

## 🧭 Context

### Intended use
Approved uses include:
- GIS dataset alignment (vector + raster)
- vertical datum harmonization for elevation surfaces
- geospatial coherence checks and QA flags
- feature correction for historical maps (public / non-sensitive)
- basemap deformation analysis
- automated ETL alignment step in deterministic pipelines

### Out-of-scope use
GAN‑v4 must not be used for:
- creating new archaeological geometries
- inferring or refining sensitive cultural site locations
- precision elevation corrections on sovereign lands without approval
- governance-critical decisions (legal boundaries, high-stakes enforcement) without human review

---

## 📦 Data & Metadata

### Training datasets (as referenced)
| Dataset | ID | Notes |
|---------|----|------|
| USGS 3DEP DEM | `stac:terrain/3dep` | Vertical-datum correction learning |
| NAIP Imagery | `stac:imagery/naip_kansas` | Ground-truth alignment reference |
| Kansas Historical Maps | `stac:archives/maps_public` | Public-domain, digitized & cleaned |
| Hydrology basins | `stac:hydrology/basins_core` | Watershed alignment bounds |
| Climate rasters | `stac:climate/core_rasters` | Raster / hybrid alignment learning |

### Governance (as reported)
- datasets are FAIR-compliant
- sensitive heritage datasets are not included for training
- no tribal or restricted site datasets used for training

### Bias considerations (as reported)
Known risk areas:
- historical maps vary heavily in accuracy
- western Kansas has less high-resolution basemap diversity
- NAIP cloud coverage can bias alignment

Mitigations (as reported):
- domain-balanced sampling
- raster augmentation
- focal-region equalization

---

## 🧱 Architecture

### Architecture components (as reported)
- tiered CNN encoder for spatial edge/feature extraction
- transformer-based spatial attention for global alignment
- residual regression heads for dx/dy offset prediction
- vertical datum subnetwork for dz alignment
- H3 correction layer for grid-based constraints
- GeoSPARQL alignment validator

### Outputs (as reported)
- offset vectors: (dx, dy, dz)
- rotation angle (optional)
- scale correction
- confidence map

### Safety boundary
- outputs must respect masking/generalization rules for restricted layers
- confidence outputs must be propagated to downstream QA gates (do not “force” corrections on low-confidence regions)

---

## 🧪 Validation & CI/CD

### Key metrics (as reported)
| Metric | Score |
|--------|-------|
| RMSE (dx/dy offset) | 0.38 m |
| RMSE (dz) | 0.27 m |
| Rotation error | <0.15° |
| Scale drift | <0.3% |
| H3 grid alignment accuracy | 0.93 |
| GeoSPARQL validity | 1.00 |

### Validation methods (as reported)
- hand-checked georeferencing points
- raster cross-correlation maps
- vertical-datum cross-check vs 3DEP

Reported effect:
- reduces misalignment in historical maps by ~60–85% depending on era and scan quality

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 map context
GAN‑v4 supports:
- aligning non-sensitive map layers used for Focus Mode spatial reasoning
- improving visual coherence for overlays (hydrology, climate, landcover)

### Story Node map context
GAN‑v4 may be used to align non-sensitive layers for Story Nodes. For any layer with potential cultural sensitivity:
- apply masking/generalization (H3 R7–R9 or project policy)
- require sovereignty review if applicable
- do not emit precision geometry in publishable artifacts

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC / DCAT expectations
- aligned outputs should be cataloged with STAC Items/Collections (for spatial assets)
- publishable bundles should include DCAT dataset records with license/rights and CARE/sovereignty fields
- all derived artifacts must carry versioning and checksum references

### PROV‑O example
~~~json
{
  "prov:entity": "geo_alignment_net_v4",
  "prov:wasGeneratedBy": "training:2025-11-14_GEO-EXP-009",
  "prov:used": [
    "stac:terrain/3dep",
    "stac:imagery/naip_kansas",
    "stac:archives/maps_public",
    "stac:hydrology/basins_core",
    "stac:climate/core_rasters"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
~~~

### OpenLineage storage (as referenced)
~~~text
data/provenance/experiments/geo_alignment_net_v4/<timestamp>/
~~~

---

## ⚖ FAIR+CARE & Governance

### FAIR compliance (as reported)
- STAC/DCAT metadata included for publishable artifacts
- PROV‑O lineage complete for training and key runs
- JSON‑LD context applied where required

### CARE + sovereignty constraints
GAN‑v4 itself does not require sensitive cultural datasets for training, but its outputs may interact with them.

Rules:
- never output refined coordinates for archaeological or sacred sites
- only apply alignment to sensitive layers when:
  - data is already generalized (H3 R7–R9 or project policy)
  - sovereignty approval exists
  - CARE metadata is fully populated and validated

### Limitations (as reported)
GAN‑v4 may be less accurate when:
- input rasters are heavily distorted
- features lack clear edges
- historical maps use inconsistent projections
- very sparse control points exist
- imagery mismatch due to seasonal differences

Not suitable for:
- archaeological precision mapping
- high-stakes legal boundary corrections
- hydrologic enforcement (use hydrology pipelines instead)

### Deployment boundaries
Allowed:
- ETL alignment stages
- preprocessing for climate/hydrology rasters
- Story Node map-context alignment (non-sensitive datasets)
- Focus Mode map reasoning (non-sensitive datasets)

Restricted:
- sensitive cultural datasets without masking + approval
- tribal geographies requiring sovereignty review
- precision cadastral boundary correction

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial model card for Geo Alignment Net v4, aligned with FAIR+CARE and KFM v11. |
| v11.0.0 | 2025-12-12 | Normalized document to KFM‑MDP v11.2.6 (approved H2 set, required directory layout section, tilde fences, governance links in footer). No model behavior changes. |

---

<div align="center">

🗺️ **Geo Alignment Net v4 — Model Card**  
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Sovereignty‑Aware · Ethical AI · Full Governance  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
