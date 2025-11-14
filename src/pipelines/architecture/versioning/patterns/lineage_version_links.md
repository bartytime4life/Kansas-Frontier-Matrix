---
title: "🔗 Kansas Frontier Matrix — Lineage Version Linking Pattern (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/patterns/lineage_version_links.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-lineage-links-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔗 **Kansas Frontier Matrix — Lineage Version Linking Pattern**  
`src/pipelines/architecture/versioning/patterns/lineage_version_links.md`

**Purpose:**  
Define the **standard pattern for linking lineage across versions** of datasets, artifacts, STAC/DCAT entries, AI outputs, and Story Nodes in the Kansas Frontier Matrix (KFM).  
This pattern ensures **deterministic version chains**, **immutable provenance**, **FAIR+CARE visibility**, and **replay-safe temporal navigation** across all releases.

<img alt="Lineage" src="https://img.shields.io/badge/Lineage-Versioned-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="MCP" src="https://img.shields.io/badge/MCP_v6.3-Compliant-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Pattern_Active-success"/>

</div>

---

## 📘 Overview

The **lineage version linking pattern** governs how KFM:

- Connects each dataset version to its **predecessor and successor**  
- Maintains immutable **PROV-O lineage bundles** per version  
- Aligns lineage chains with **STAC/DCAT version graphs**  
- Encodes **CARE & sovereignty metadata** across versions  
- Supports **deterministic replays** and **time-travel analyses**  
- Provides **auditable history** for FAIR+CARE governance  

This pattern is used by:

- ETL pipelines  
- Geospatial processing chains  
- AI/Focus Mode pipelines  
- Metadata/STAC/DCAT builders  
- Governance & audit tools  

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/versioning/patterns/
├── README.md
├── artifact_lifecycle.md
├── semver_rules.md
├── stac_dcat_alignment.md
├── lineage_version_links.md        # This file
└── governance_version_contract.md
~~~~~

---

## 🧩 Lineage Version Chain Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["v10.2.2<br/>Lineage Bundle"] --> B["v10.3.0<br/>Lineage Bundle"]
  B --> C["v10.3.1<br/>Lineage Bundle"]
  C --> D["Version Chain Index<br/>version_chain.schema.json"]
  D --> E["Replay Engine<br/>Deterministic Reprocessing"]
  D --> F["Governance & FAIR+CARE<br/>Version-Aware Review"]
~~~~~

---

## 🧱 Versioned Lineage Location Pattern

Each version’s lineage is stored at a **fixed, immutable path**:

~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

Examples:

~~~~~text
data/lineage/hydrology_flow_ks/v10.2.2/lineage.json
data/lineage/hydrology_flow_ks/v10.3.0/lineage.json
data/lineage/hydrology_flow_ks/v10.3.1/lineage.json
~~~~~

Lineage files MUST:

- Be immutable after publication  
- Be unique per `{dataset_id, version}` pair  
- Encode links to previous versions  

---

## 🔗 Lineage Cross-Version Link Fields

Each lineage bundle MUST include:

| Field | Description |
|-------|-------------|
| `dataset_id` | Target dataset ID |
| `version` | Current version (SemVer) |
| `previous_version` | Immediate prior version, or `null` |
| `next_versions` | Optional list of known successors |
| `lineage_ref` | Self reference to lineage path |
| `stac_item_ref` | Matching STAC Item path |
| `dcat_dataset_ref` | Matching DCAT Dataset path |

Example snippet:

~~~~~json
{
  "dataset_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "previous_version": "v10.3.0",
  "next_versions": [],
  "lineage_ref": "data/lineage/hydrology_flow_ks/v10.3.1/lineage.json",
  "stac_item_ref": "data/stac/hydrology_flow_ks_v10.3.1.json",
  "dcat_dataset_ref": "data/reports/dcat_exports/hydrology_flow_ks.json"
}
~~~~~

---

## 🧬 Version Chain Index Pattern

For each dataset, an index file may summarize the chain:

~~~~~text
data/lineage/{dataset_id}/version_chain.json
~~~~~

Example (abbreviated):

~~~~~json
{
  "dataset_id": "hydrology_flow_ks",
  "versions": [
    { "version": "v10.2.2", "previous": null },
    { "version": "v10.3.0", "previous": "v10.2.2" },
    { "version": "v10.3.1", "previous": "v10.3.0" }
  ]
}
~~~~~

This file is validated using `version_chain.schema.json` and MUST be updated only by version-aware pipelines.

---

## ⚖️ FAIR+CARE Integration Across Versions

Lineage links MUST propagate:

- CARE labels (`public`, `sensitive`, `restricted`)  
- Sovereignty metadata (tribal authority, masking rules)  
- License metadata (SPDX)  

Rules:

- CARE label can change over time (e.g., from `public` → `restricted`) but changes MUST be explicitly recorded in lineage and governance contracts.  
- Sovereignty metadata MUST be included whenever any version involves Indigenous or heritage data.  
- Governance decisions (approved/rejected/conditional) MUST be linkable to each lineage file.

Governance references used in lineage:

~~~~~text
docs/reports/audit/versioning_ledger.json
~~~~~

---

## 🔍 Replay Engine & Lineage Links

The **Replay Engine** uses lineage links to:

- Discover prior versions  
- Compare checksums across versions  
- Validate deterministic behavior  
- Identify divergence regions  

Replay MUST NOT mutate lineage; it may:

- Append replay session records  
- Log telemetry about divergences  
- Feed governance follow-ups  

---

## 📡 Telemetry Requirements for Lineage Chains

For each lineage publication or version link update, telemetry MUST include:

- `dataset_id`  
- `version`  
- `previous_version` (or `null`)  
- `lineage_checksum`  
- `care_label`  
- `governance_status`  
- `energy_wh`  
- `co2_g`  

Telemetry appended to:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🚫 Forbidden Lineage Link Violations

❌ Skipping versions in `previous_version` chains  
❌ Pointing to non-existent previous versions  
❌ Editing lineage links retroactively for already published versions  
❌ Omitting `previous_version` for non-initial versions  
❌ Linking STAC/DCAT to lineage for the wrong version  
❌ Publishing a lineage file without updating version chain index (where used)  

Any violation triggers a **Critical CI Failure** and governance review.

---

## 🧾 Example Lineage Chain (End-to-End)

~~~~~json
{
  "dataset_id": "ks_treaty_boundaries",
  "versions": [
    {
      "version": "v10.0.0",
      "previous": null,
      "care_label": "sensitive"
    },
    {
      "version": "v10.1.0",
      "previous": "v10.0.0",
      "care_label": "sensitive"
    },
    {
      "version": "v10.2.0",
      "previous": "v10.1.0",
      "care_label": "restricted"
    }
  ]
}
~~~~~

Governance MAY use this to identify when and why CARE classification changed.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Established lineage linking pattern for all versioned datasets; aligned with STAC/DCAT, governance, and replay engine. |

---

<div align="center">

**Kansas Frontier Matrix — Lineage Version Linking Pattern**  
Immutable Chains × FAIR+CARE × Deterministic Replay × Governance-Ready  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Patterns](../README.md)

</div>
