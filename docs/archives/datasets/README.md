---
title: "🗂️ Kansas Frontier Matrix — Archives Datasets Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/archives/datasets/README.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:archives-datasets-layer:v11.2.4"
semantic_document_id: "kfm-doc-archives-datasets-layer"
event_source_id: "ledger:kfm:doc:archives-datasets-layer:v11.2.4"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/archives-datasets-v4.json"
signature_ref: "../../../releases/v11.2.4/signature.sig"
attestation_ref: "../../../releases/v11.2.4/slsa-attestation.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Module Subsystem Overview"
intent: "archives-datasets"

fair_category: "F1-A1-I1-R1"
care_label: "C1 · Indigenous Knowledge Protection Enabled"
sensitivity: "Culturally Sensitive (archives; auto-mask rules apply)"
sensitivity_level: "Elevated"
public_exposure_risk: "Medium"
classification: "Public (Governed · Archive-Scoped)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ontology_alignment:
  cidoc: "E78 Collection"
  schema_org: "Dataset"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/archives/datasets/README.md@v11.0.1"
  - "docs/archives/datasets/README.md@v10.4.x"
  - "docs/archives/datasets/README.md@v10.x"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../schemas/json/kfm-archives-datasets-layer-v11.2.4.schema.json"
shape_schema_ref: "../../../schemas/shacl/kfm-archives-datasets-layer-v11.2.4-shape.ttl"
story_node_refs: []

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "archives-datasets"
  applies_to:
    - "docs/archives/datasets/**"
    - "data/archives/datasets/**"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Archives Datasets Layer (v11.2.4)**  
`docs/archives/datasets/README.md`

**Purpose**  
Define the **Archives Datasets Layer** as the structured storage space for all **historical**, **scientific**, and **AI-generated** datasets preserved inside the Kansas Frontier Matrix’s immutable archives.  

This layer is strictly governed by **FAIR+CARE (C1)**, **MCP-DL v6.3**, **STAC/DCAT**, and **lineage-preservation protocols**, ensuring all datasets remain reproducible, ethically managed, and semantically compatible across future KFM versions.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-C1_Indigenous_Protection-gold" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen" />

</div>

---

## 📘 Overview

The **Archives Datasets Layer**:

- 🧩 Organizes all archived datasets with consistent, machine-checked metadata structures.  
- 🧬 Ensures PROV-O lineage, reproducibility, and **hash-verified immutability**.  
- 🗺️ Provides domain-specific categories for historical, environmental, and cultural corpora.  
- 🤖 Captures AI-generated research artifacts as **first-class archival entities**.  
- 🗄️ Aligns with **STAC 1.0 / DCAT 3.0** for interoperability with external systems and catalogs.  

Datasets in this layer are **read-only** (once archived), **versioned**, and **linked** to:

- Archive-wide STAC/DCAT metadata (`docs/archives/stac/`).  
- Provenance chains (`docs/archives/provenance/chains/`).  
- SBOM and integrity bundles (`docs/archives/provenance/sbom/`).  
- Telemetry records (`releases/v11.2.4/focus-telemetry.json`).

---

## 🗂️ Directory Layout

~~~text
📁 docs/archives/datasets/                # 🗂️ Datasets layer documentation root
│
├── 📄 README.md                          # 🗂️ This overview file (v11.2.4)
│
├── 📁 historical/                        # 📜 Historical & cultural datasets (C1-sensitive)
│   ├── 📁 treaties/                      # Treaty corpora & associated metadata
│   ├── 📁 land-records/                  # Deeds, plats, patents, allotments, parcels
│   ├── 📁 census-series/                 # Census & demographic time-series
│   └── 📁 plats-and-surveys/             # Plats, surveys, GLO/cadastral map datasets
│
├── 📁 scientific/                        # 🔬 Long-term scientific baselines
│   ├── 📁 hydrology/                     # Hydrologic baselines (streamflow, aquifers)
│   ├── 📁 climatology/                   # Climate normals & anomaly composites
│   └── 📁 ecology/                       # Ecological, biodiversity & vegetation datasets
│
└── 📁 ai-generated/                      # 🤖 AI-derived & AI-assisted datasets
    ├── 📁 focus-mode/                    # Focus Mode v2.x summary corpora
    ├── 📁 story-node-v3/                 # Story Node v3 emissions (JSON bundles)
    └── 📁 analysis-summaries/            # Cross-domain AI-generated synthesis datasets
~~~

Each subdirectory:

- Has its own `README.md` or `METADATA.*` describing scope and governance.  
- Contains datasets that follow **STAC Item + DCAT Dataset + PROV-O lineage + SBOM integrity + CARE assessment**.

---

## 🧭 Context

The Archives Datasets Layer is the **dataset-focused submodule** of the **Archives Module**:

- **Upstream:**  
  - `docs/analyses/**` (hydrology, climatology, ecology, historical, cross-domain analyses).  
  - `src/pipelines/**` ETL, model training, and AI inference workflows.

- **Within Archives:**  
  - This layer captures **canonical dataset bundles** for each domain.  
  - The `stac/` and `provenance/` directories index and trace those bundles.

- **Downstream:**  
  - Time-aware Story Nodes and Focus Mode reconstructions.  
  - External catalog integrations (state, tribal, and national archives).  
  - Governance & sustainability dashboards.

All datasets here are treated as **long-lived reference assets** — they are not ephemeral analysis scratch outputs.

---

## 📦 Data & Metadata

### 🕰 Historical Datasets

Historical datasets capture Kansas’s documented past and cultural landscape evolution:

- 📜 Treaty archives.  
- 🗺️ Survey plats & cadastral data.  
- 🧍 Census & demographic series.  
- 🗂️ Land parcels, allotments, territorial-era records.

**CARE C1 rules apply**:

- Tribal, Indigenous, or culturally sensitive materials may be:  
  - Restricted, generalized, or redacted in public views.  
  - Subject to specific governance decisions stored in the archives governance ledger.

### 🔬 Scientific Datasets

Long-term reproducible baselines spanning Kansas’s environmental domains:

- 🌊 **Hydrology**  
  - Streamflow baselines.  
  - Watershed delineations.  
  - Aquifer recharge, groundwater levels, hydraulic metrics.

- 🌦️ **Climatology**  
  - Climate normals and trend series.  
  - Multi-year anomaly composites.  
  - Paleoclimate & drought reference indices.

- 🌱 **Ecology**  
  - Species distribution maps.  
  - Vegetation & biomass layers.  
  - Biodiversity observation datasets.

All scientific datasets **must include**:

- STAC Item descriptors (with `extent`, `proj`, `raster` extensions as appropriate).  
- Data dictionaries or schema documentation.  
- Spatial and temporal coverage extents.

### 🤖 AI-Generated Datasets

AI-generated contributions are preserved as archive-grade datasets:

- Focus Mode v2.x summaries and narrative corpora.  
- Temporal reconstructions and narrative captures.  
- Story Node v3 emissions (graph-aligned JSON).  
- Synthetic or augmented tabular corpora created during analyses.

Every AI-generated dataset includes:

- **PROV-O lineage graph** (which model, which data, which config).  
- **Model + version identifiers** (e.g., `focus_transformer_v2_1`).  
- **Carbon & energy telemetry** (per workflow run).  
- **SBOM references** (software stack used to create it).  
- **Reconstruction prompts/workflows** where applicable.

### 📦 Ingestion Requirements

All datasets stored in this layer must satisfy:

1. YAML or JSON front-matter / metadata block.  
2. STAC Item + DCAT Dataset descriptor.  
3. PROV-O lineage graph (often JSON-LD in `provenance/chains/`).  
4. SHA-256 content hash (and/or checksum extension).  
5. Energy/carbon telemetry record.  
6. CARE impact review (with `care_tag`, sovereignty flags if applicable).  
7. Persistent identifier (PID / UUID / DOIs where applicable).  
8. README or Data Dictionary.  
9. Reconstruction procedure (SOP, scripts, or config references).

**No dataset may be replaced in-place** — only **versioned** into new immutable snapshots.

### 🔎 Retrieval & Discovery

Datasets in this layer may be queried via:

- STAC 1.0 search (Collections/Items, spatiotemporal filters).  
- DCAT metadata filtering (theme, license, provenance).  
- Lineage traversal (Neo4j PROV graph).  
- Story Node v3 temporal alignment (time-aware slices).  
- AI-assisted semantic search (Focus Transformer v2.x).

Examples (conceptual CLI):

~~~text
kfm archives datasets search --domain hydrology
kfm archives datasets lineage expand --id census_1890
kfm archives datasets export --dataset treaty_kp_1867
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC**  
  - Each dataset corresponds to one or more STAC Items in an appropriate Collection  
    (e.g., `kfm-archives-historical-treaties`, `kfm-archives-scientific-hydrology`).  
  - Archive-specific properties:
    - `kfm:archive_family`, `kfm:care_tag`, `kfm:governance_ledger_ref`.  
    - `checksum:multihash` or SHA-256 fields.

- **DCAT**  
  - Family-level datasets appear as `dcat:Dataset` entries in a DCAT catalog.  
  - Distributions correspond to:
    - Source files (COG, NetCDF, GeoJSON, CSV, PMTiles).  
    - Documentation (Markdown, PDF).  
    - Provenance (JSON-LD).

- **PROV-O**  
  - Each archived dataset is a `prov:Entity` in a `prov:Collection` representing its family.  
  - Creation/ingestion activities (`prov:Activity`) link:
    - Upstream sources (`prov:used`).  
    - Scripts/services/people (`prov:wasAssociatedWith`).  
    - Derived snapshots (`prov:wasGeneratedBy`, `prov:wasRevisionOf`).

---

## 🧪 Validation & CI/CD

Before acceptance into the Archives Datasets Layer, every dataset must pass:

- 🔐 **Hash verification** (SHA-256 or equivalent).  
- 🌐 **STAC/DCAT schema validation** (via `stac-validate.yml`).  
- 🔗 **PROV-O link integrity** (no broken lineage references).  
- ⚖ **FAIR+CARE scoring** (including C1 Indigenous protections).  
- 📋 **Metadata completeness audit** (required fields present and correct).  
- ♿ **Accessibility & reproducibility review** (documentation, data dictionaries, SOPs).

CI workflows involved:

- `faircare-validate.yml` — FAIR+CARE & sovereignty checks.  
- `stac-validate.yml` — STAC/DCAT + asset integrity.  
- `telemetry-export.yml` — Dataset-level telemetry contributions into `focus-telemetry.json`.  

---

## ⚖ FAIR+CARE & Governance

The Datasets Layer operates under **C1 · Indigenous Knowledge Protection Enabled**:

- **Findable (F1)** — Datasets are indexed with stable IDs, STAC/DCAT entries, and governance ledger references.  
- **Accessible (A1)** — Access governed by license, CARE level, and sovereignty policies; public when appropriate.  
- **Interoperable (I1)** — Open standards (STAC, DCAT, PROV, ISO 19115) ensure cross-system compatibility.  
- **Reusable (R1)** — Provenance, licensing, and clear documentation support long-term reuse.

**CARE C1 enforcement:**

- Indigenous and culturally sensitive datasets may require:
  - Restricted access or generalization.  
  - Council-reviewed summaries instead of raw access.  
  - Explicit mention of governance decisions in dataset metadata.

Governance records for datasets are logged into:

~~~text
docs/reports/audit/archives-datasets-governance-ledger.json
~~~

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                               |
|----------:|------------|-------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Upgraded to KFM-MDP v11.2.4; added full metadata, emoji-rich directory layout, STAC/DCAT/PROV alignment, and explicit C1 CARE posture. |
| v11.0.1  | 2025-11-19 | First KFM-MDP v11-compliant dataset-layer overview; defined ingestion requirements & retrieval patterns. |
| v10.4.x  | 2025-10-XX | Partial dataset integration; began aligning datasets with STAC/DCAT and PROV.                        |
| v10.x    | 2025-0X-XX | Initial archives dataset directory creation and basic categorization.                                 |

---

<div align="center">

🗂️ **Kansas Frontier Matrix — Archives Datasets Layer (v11.2.4)**  
Structured Knowledge · FAIR+CARE (C1) Governance · Lineage Integrity  

[⬅ Back to Archives Module](../README.md) ·  
[📁 Archives Root](../README.md) ·  
[⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
