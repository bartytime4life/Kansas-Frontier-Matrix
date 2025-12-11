---
title: "🔐 Kansas Frontier Matrix — Data Checksums & Integrity Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/checksums/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-checksums-readme-v11.0.0"
semantic_document_id: "kfm-doc-data-checksums-readme"
event_source_id: "ledger:data/checksums/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-checksums-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Overview"
header_profile: "root-centered-badge-row"
footer_profile: "standard"
fencing_profile: "outer-backticks-inner-tildes-v1"
intent: "data-checksums-registry"
role: "integrity-registry"
category: "Data · Integrity · Provenance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/data-checksums-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/data-checksums-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next integrity-registry update"
---

<div align="center">

# 🔐 **Kansas Frontier Matrix — Data Checksums & Integrity Registry**  
`data/checksums/README.md`

**Purpose**  
Describe the **checksum verification system**, integrity tracking, and **catalog/provenance linkage** for all governed datasets and releases in the **Kansas Frontier Matrix (KFM)** across the core pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

Every artifact—from raw dataset to Story Node-ready release bundle—is:

- Cryptographically hashed (SHA-256)  
- Registered into governance ledgers and Neo4j (via PROV/GeoSPARQL views)  
- Cross-checked with SBOM and release manifests  
- Integrated with FAIR+CARE governance and sustainability telemetry  

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)]() ·
[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-informational.svg)]() ·
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)]() ·
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Integrity%20Certified-gold.svg)]() ·
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Checksum Integrity Registry** manages **SHA-256 manifests** for:

- Datasets under `data/**` (raw, work, processed, releases)  
- STAC/DCAT metadata files and PROV sidecars  
- Release artifacts (`manifest.zip`, SBOMs, STAC collections, DCAT catalogs)  
- Critical governance files (data contracts, ontology schemas, Story Node templates)  

Checksums serve as **verifiable fingerprints** binding:

- Data files → STAC/DCAT/PROV records → Neo4j nodes → Story Nodes → Focus Mode telemetry  
- Release assets → SBOM entries → supply-chain attestations  

In the KFM pipeline, this registry sits **between ETL output and catalog/graph publication**:

1. Deterministic ETL writes normalized assets to `data/work/` and `data/processed/`.  
2. Catalog builders emit STAC/DCAT/PROV artifacts into `data/stac/`, `data/dcat/`, and provenance stores.  
3. The checksum layer fingerprints these assets and governance docs into manifests under `data/checksums/`.  
4. Neo4j ingesters attach checksum identifiers to graph entities (datasets, releases, Story Nodes).  
5. APIs and Focus Mode expose integrity status for downstream users.

Primary objectives:

- Detect unauthorized modifications or corruption  
- Provide public verifiability of releases and Story Node backing data  
- Support reproducibility of historical analyses and Focus Mode narratives  
- Feed integrity signals into governance, telemetry, and reliability dashboards  

---

## 🗂️ Directory Layout

~~~text
data/checksums/
├── 📄 README.md                     # This file (governed by KFM-MDP v11.2.6)
├── 📘 manifest.json                 # Master SHA-256 manifest for core datasets
├── 🧪 processed_datasets.json       # Checksums for FAIR+CARE-certified processed outputs
├── 🧱 staging_datasets.json         # Checksums for normalized/staging artifacts
├── 🧰 work_datasets.json            # Checksums for ETL workspaces (optional, may be pruned)
└── 🧾 release_hashes.json           # Checksums mapped to SBOM + manifest.zip entries
~~~

Rules:

- `manifest.json` is the canonical index of checksums for key, graph-exposed datasets.  
- Other manifests partition coverage by lifecycle stage (processed, staging, work, release).  
- Every manifest is a **first-class catalog asset**, discoverable via STAC/DCAT and PROV links.  
- All files must conform to `data-checksums-readme-v11`-compatible schemas and pass CI schema checks.  

---

## 🧱 Architecture & Integrity Flow

~~~mermaid
flowchart TD
    ETL["Deterministic ETL & Validation\nsrc/pipelines/** → data/{work,processed}"]
        --> CATALOGS["STAC/DCAT/PROV Catalogs\ndata/stac · data/dcat · provenance store"]

    ETL --> GEN["Checksum Generator\n(tools/validation/checksums_*.py)"]
    CATALOGS --> GEN

    GEN --> REG["Integrity Registry\n(data/checksums/*.json)"]

    REG --> LEDGER["Governance Ledger\n(docs/reports/audit/data_provenance_ledger.json)"]
    REG --> SBOM["SBOM & Release Manifests\n(releases/v11.x.x/)"]

    CATALOGS --> GRAPH["Neo4j Graph & GeoSPARQL Views\nsrc/graph/**"]
    REG --> GRAPH

    GRAPH --> API["API Layer\nsrc/api/**"]
    API --> UI["React / MapLibre / Cesium UIs\nsrc/web/**"]
    UI --> STORY["Story Nodes & Focus Mode\nStory Node registry"]

    REG --> STORY
    SBOM --> PUBLIC["Public Release Verification\nExternal users & tools"]
~~~

### Flow Description

1. **ETL & Cataloging**  
   - Deterministic ETL produces raw/work/processed assets.  
   - STAC/DCAT/PROV emitters describe these assets as catalog entities and provenance graphs.  

2. **Checksum Generation**  
   - Checksum tooling computes SHA-256 for all governed artifacts (data, catalogs, governance docs).  
   - The generator consumes both filesystem paths and catalog/provenance identifiers to avoid drift.  

3. **Registry & Governance**  
   - Results are written into manifest files under `data/checksums/`.  
   - Governance ledgers record `prov:Entity` entries for checksum manifests and link them to ETL/STAC activities.  

4. **Graph Integration**  
   - Neo4j nodes for datasets, releases, and Story Nodes gain checksum properties / relationships (draft labels):  
     - `(:KfmDataset)-[:HAS_CHECKSUM]->(:ChecksumDigest)`  
     - `(:Release)-[:VERIFIES_ASSET]->(:ChecksumManifest)`  

5. **Publication & Verification**  
   - Releases embed checksum sets and SBOM parity information.  
   - Public users and automated agents can verify assets against `data/checksums/*.json` and release bundles.  
   - Focus Mode surfaces integrity status (e.g., “✅ Checksums verified for all backing datasets”).  

---

## ⚙️ Manifest Structure

All checksum manifests share a core structure:

~~~json
{
  "version": "v11.0.0",
  "generated_on": "2025-11-19T19:25:00Z",
  "hash_algorithm": "SHA-256",
  "datasets": [
    {
      "id": "hazards_processed_v11.0.0",
      "path": "data/processed/hazards/hazards_composite_v11.0.0.geojson",
      "checksum": "sha256-2f1e3b8c97df84b5d2c3e39bbd95b9e8d12b64ad38a62400f745d68ec6d1b75e",
      "fairstatus": "certified",
      "governance_ref": "docs/reports/audit/data_provenance_ledger.json",
      "stac_ref": "data/stac/items/hazards_v11_2025Q4.json",
      "dcat_ref": "data/dcat/hazards_v11_2025Q4.jsonld"
    },
    {
      "id": "climate_staging_v11.0.0",
      "path": "data/staging/climate/climate_aggregate_v11.0.0.parquet",
      "checksum": "sha256-a8373fa4d12d49be5f5f2178a91d79981b1d28b947f05eaa52e9e7e8d2cfadcd",
      "fairstatus": "pending"
    }
  ]
}
~~~

**Checksum format:** `sha256-<hex>`.

Required per dataset:

- `id` — stable dataset identifier, aligned with STAC/DCAT/Neo4j IDs where feasible  
- `path` — repository-relative path to the asset  
- `checksum` — SHA-256 digest in `sha256-<hex>` form  
- `fairstatus` — e.g., `certified`, `pending`, `deprecated`  

Recommended:

- `governance_ref` — JSON/JSON-LD ledger entry referencing PROV activities  
- `stac_ref`, `dcat_ref` — STAC/DCAT records for catalog discoverability  

**Provenance alignment:**

- Manifests are modeled as `prov:Entity` with `prov:wasGeneratedBy` ETL/checksum activities.  
- Individual dataset checksum entries may be mapped to `spdx:checksum` fields in SBOMs.  

---

## 🧠 FAIR+CARE Integrity Governance

Checksums are deeply integrated with FAIR+CARE and Indigenous data sovereignty:

| Principle                 | Implementation                                                                       | Verified By          |
|---------------------------|--------------------------------------------------------------------------------------|----------------------|
| **Findable**              | Checksum references embedded in STAC/DCAT, Neo4j, and release manifests             | @kfm-data            |
| **Accessible**            | JSON manifests under CC-BY 4.0, publicly browsable when risk allows                 | @kfm-accessibility   |
| **Interoperable**         | Structures compatible with SPDX, STAC 1.x, DCAT 3, and PROV-O                       | @kfm-architecture    |
| **Reusable**              | Immutable, versioned logs with explicit provenance and ontology alignment           | @kfm-governance      |
| **Collective Benefit**    | Public can independently verify dataset integrity and Story Node backing data       | @faircare-council    |
| **Authority to Control**  | Governance Council defines checksum coverage/policy for sensitive datasets          | @kfm-governance      |
| **Responsibility**        | Telemetry-backed coverage metrics; periodic audits and anomaly alerts               | @kfm-security        |
| **Ethics & Sovereignty**  | Integrity guardrails for Indigenous and sensitive data; redaction where necessary   | @kfm-ethics          |

Notes:

- For **sensitive Indigenous datasets**, checksum manifests may be **scope-limited** or redacted, while still recording the fact of verification in governance ledgers.  
- Integrity violations on governed datasets can trigger governance workflows (e.g., Story Node de-publication, Focus Mode warnings).  

---

## 🧪 Validation & CI/CD

Several workflows in `.github/workflows/` enforce checksum correctness and governance alignment:

| Workflow                  | Description                                                | Outputs                                                              |
|---------------------------|------------------------------------------------------------|----------------------------------------------------------------------|
| `checksum-verify.yml`     | Generates & verifies SHA-256 hashes for governed assets    | `data/checksums/manifest.json`, per-stage checksum manifests        |
| `faircare_validate.yml`   | Ensures checksumming respects FAIR+CARE & sovereignty     | `docs/reports/fair/faircare_summary.json`                           |
| `governance-ledger.yml`   | Aligns checksum records with governance/provenance ledger | `docs/reports/audit/data_provenance_ledger.json`                    |
| `sbom_verify.yml`         | Confirms SBOM→checksum→manifest consistency               | `releases/v11.x.x/sbom.spdx.json`, `releases/v11.x.x/manifest.zip`  |

Rules:

- Any PR touching `data/checksums/`, `data/stac/`, `data/dcat/`, or `releases/` **must** pass these workflows.  
- Security policy may add **secret- and PII-scan profiles** that treat checksum manifests as code-like assets.  
- Failures in checksum verification **block merges** until resolved or explicitly waived under governance rules.  

---

## 📊 Example CLI Verification

Local verification using standard tools:

~~~bash
# 1) Compute checksum locally
sha256sum data/processed/hazards/hazards_composite_v11.0.0.geojson

# 2) Look up expected checksum in manifest
jq '.datasets[] | select(.id=="hazards_processed_v11.0.0")' data/checksums/manifest.json

# 3) Optionally, compare via script (non-zero exit on mismatch)
python tools/validation/check_checksum.py \
  --id hazards_processed_v11.0.0 \
  --manifest data/checksums/manifest.json \
  --file data/processed/hazards/hazards_composite_v11.0.0.geojson
~~~

This pattern is suitable for:

- Developer spot checks  
- Reproducibility notebooks (under `docs/analyses/**`)  
- External users verifying published releases against `data/checksums/` plus SBOMs  

---

## 🌱 Sustainability & Integrity Metrics

Sustainability and integrity metrics captured in telemetry include:

| Metric                | Target                      | Verified By         |
|-----------------------|----------------------------|---------------------|
| Checksum Coverage     | 100% for released datasets | @kfm-validation     |
| Governance Sync       | 100% for archived datasets | @kfm-governance     |
| SBOM Parity           | ≥ 99.9% SBOM–manifest match| @kfm-architecture   |
| Energy per Batch      | ≤ 10 Wh per checksum batch | @kfm-sustainability |
| FAIR+CARE Compliance  | Certified-only processes   | @faircare-council   |

Telemetry destinations:

~~~text
../../releases/v11.2.2/focus-telemetry.json
docs/reports/telemetry/data-checksums-*.json
~~~

These metrics are used by Focus Mode and governance dashboards to:

- Flag integrity regressions between releases  
- Track sustainability of large checksum runs  
- Provide public transparency into integrity practices  

---

## 🏷️ Naming & Conventions

- **Data files:** `<domain>_<layer>_v<semver>.<ext>`  
  - e.g., `hazards_composite_v11.0.0.geojson`  

- **Checksum IDs:** `<dataset_id>`  
  - Prefer IDs aligned with STAC/DCAT/Neo4j identifiers (e.g., `hazards_processed_v11.0.0`).  

- **Checksum field:**  
  - All manifests must include a `checksum` field in `sha256-<hex>` format.  

- **Immutability rule:**  
  - Once a release is tagged, its checksum entries become **append-only**.  
  - Corrections add **new records** (e.g., `hazards_processed_v11.0.0_fix1`), never overwrite existing ones.  

- **Graph mapping (draft):**  
  - `:ChecksumManifest { id, version, generated_on, hash_algorithm }`  
  - `:ChecksumDigest { checksum, path, fairstatus }`  
  - Relationships:  
    - `(:ChecksumManifest)-[:CONTAINS_DIGEST]->(:ChecksumDigest)`  
    - `(:KfmDataset)-[:HAS_CHECKSUM]->(:ChecksumDigest)`  

All new labels/relationships are **draft** and require schema review under KFM-OP v11.

---

## 🧾 Internal Citation

Recommended internal citation for this registry:

~~~text
Kansas Frontier Matrix (2025). Data Checksums & Integrity Registry (v11.2.6).
Checksum governance, cryptographic verification, and FAIR+CARE-integrated integrity
processes for KFM datasets, catalogs, and releases. Ensures dataset immutability,
reproducibility, and public verifiability across versions and Story Nodes.
~~~

Use this in related docs (ETL guides, STAC/DCAT specs, Story Node standards) when referring to checksum policy.

---

## 🕰️ Version History

| Version  | Date       | Author      | Summary                                                                                                                 |
|---------:|-----------:|------------|-------------------------------------------------------------------------------------------------------------------------|
| v11.2.6  | 2025-12-11 | @kfm-data  | Aligned with KFM-MDP v11.2.6; moved 🗂️ Directory Layout to second H2; updated FAIR+CARE fields; added pipeline/Neo4j links. |
| v11.2.2  | 2025-11-27 | @kfm-data  | Upgraded to v11.2.x series; applied emoji layout; aligned references; clarified governance and telemetry integration.  |
| v11.0.0  | 2025-11-19 | @kfm-data  | Upgraded to v11; added sustainability telemetry, ROOT-GOVERNANCE link, and ontology hooks.                             |
| v10.2.2  | 2025-11-12 | @kfm-data  | Aligned with v10.2; SBOM/manifest linkage, JSON-LD guidance, CLI examples, telemetry.                                  |
| v10.0.0  | 2025-11-10 | @kfm-data  | Baseline registry; governance mapping, manifest examples, and core integrity metrics.                                   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[⬅️ Back](../README.md) · [🗃️ Archive & Provenance Registry](../archive/README.md) · [🛡️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
