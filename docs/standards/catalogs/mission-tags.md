---
title: "🏷️ Kansas Frontier Matrix — Mission Tags Standard (product-availability · reprocessing · algorithm-change · mission-status)"
path: "docs/standards/catalogs/mission-tags.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Reliability Guild"
content_stability: "stable"

doc_kind: "Standard"
status: "Active / Canonical"
intent: "mission-tagging-standard"
semantic_document_id: "kfm-std-catalogs-mission-tags-v11.2.6"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

header_profile: "standard"
footer_profile: "standard"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
telemetry_ref: "../../../releases/v11.2.6/catalog-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalogs/mission-tags-v1.json"
---

# 🏷️ Mission Tags Standard for KFM STAC/DCAT Catalogs

This standard defines **four canonical mission-level tags** that **every KFM collection / mission** MUST use in STAC, DCAT, the Neo4j graph, and Story Nodes:

- `product-availability`
- `reprocessing`
- `algorithm-change`
- `mission-status`

They keep catalogs, graph, and UI aligned across providers, missions, and time.

---

## 🗂️ Directory Layout

Mission tags appear consistently in the KFM monorepo, using the standard emoji directory style:

~~~text
data/
└── 📁 stac/
    └── 📁 missions/
        └── 📄 collection.json          # STAC Collections with kfm:tags & kfm:mission:* fields

docs/
└── 📁 catalogs/
    └── 📁 dcat/
        └── 📄 <mission>.jsonld         # DCAT Datasets mirroring mission tags

src/
└── 📁 pipelines/
    └── 📁 catalogs/
        └── 📄 mission_tags.py          # ETL for applying/maintaining mission tags

configs/
└── 📁 pipelines/
    └── 📁 catalogs/
        └── 📄 mission-tags.yaml        # Config for mission tag derivation and validation

.github/
└── 📁 workflows/
    └── 📄 catalogs-metadata.yml        # CI for STAC/DCAT schema & mission-tag checks
~~~

ETL and CI treat these locations as **canonical** when validating and updating mission tags.

---

## 📘 Conceptual Overview

Mission tags answer four questions about any mission or collection at any point in time:

1. **`product-availability`** — *Can users actually get the product right now?*  
2. **`reprocessing`** — *Is bulk reprocessing underway, and at what scope?*  
3. **`algorithm-change`** — *Has the algorithm changed in a way that affects interpretation?*  
4. **`mission-status`** — *Is the mission healthy, degraded, in incident, or ended?*

They are:

- stored in **STAC** as `properties.kfm:tags[]` and `properties.kfm:mission:*`  
- mirrored in **DCAT** via `dcat:keyword`, `dct:subject`, and `kfm:mission:*` extensions  
- propagated into the **Neo4j mission/catalog graph**  
- exposed in **Story Nodes & Focus Mode** as filters, badges, and timeline markers  

> Pipeline fit: ETL → STAC/DCAT (with mission tags) → Neo4j mission graph → API → Story Nodes / Focus Mode.

---

## 🧱 Canonical Tag Semantics

### Tag summary

| Tag name               | Field prefix                        | Question answered                                      | Scope                  |
|------------------------|-------------------------------------|--------------------------------------------------------|------------------------|
| `product-availability` | `kfm:mission:product_availability`  | “Can users obtain products from this mission?”         | mission / product line |
| `reprocessing`         | `kfm:mission:reprocessing`          | “Is bulk reprocessing happening, and how broad is it?” | mission-wide or subset |
| `algorithm-change`     | `kfm:mission:algorithm_change`      | “What algorithm versions are in effect and when?”      | mission / collection   |
| `mission-status`       | `kfm:mission:status`                | “What is the operational state of the mission?”        | mission                |

### 1️⃣ `product-availability`

Represents **operational availability of deliverables** in KFM:

- `operational` — normal production and access  
- `paused` — no new products; historical access unchanged  
- `degraded` — products are available but with reduced quality, coverage, or timeliness  
- `retired` — products are frozen; no new products will be generated (mission or product line ended)

### 2️⃣ `reprocessing`

Captures **bulk reprocessing campaigns** that can change products historically:

- `active` — whether a reprocessing campaign is currently running (`true` / `false`)  
- `scope` — scope of campaign; aligned to mission-specific semantics:
  - `R1` — first major reprocessing cycle or partial (e.g., critical period or subset)  
  - `R2` — second or subsequent structured reprocessing cycle  
  - `full` — campaign is effectively mission-wide, across all relevant time and space  
- `since` — ISO-8601 date when the current campaign started

### 3️⃣ `algorithm-change`

Represents **algorithm versioning events** affecting interpretation:

- `version_from` — previous algorithm version (or `null` for first version)  
- `version_to` — new algorithm version (semantic version string or provider-native version)  
- `effective` — ISO-8601 date when the new algorithm became effective for new products  
- `notes` — short free-text description explaining the user-visible effect

Algorithm changes are **point-in-time events**; reprocessing may apply that change historically.

### 4️⃣ `mission-status`

Represents **overall operational status** of the mission:

- `nominal` — expected performance, no active anomaly  
- `anomaly` — issues detected but not yet escalated to incident; monitoring and investigation ongoing  
- `incident` — confirmed significant problem; may affect data quality, availability, or safety  
- `ended` — mission has concluded; no new acquisitions, but products may still be accessible

---

## ✅ STAC Implementation (Normative)

### STAC Collections

Every **STAC Collection** relevant to a mission MUST:

1. Include all four tags in `properties.kfm:tags[]`.  
2. Include the mission-level fields under `properties.kfm:mission:*`.

Example (collection-level):

~~~json
{
  "type": "Collection",
  "id": "example-collection",
  "properties": {
    "kfm:tags": [
      "product-availability",
      "reprocessing",
      "algorithm-change",
      "mission-status"
    ],
    "kfm:mission:product_availability": "operational",
    "kfm:mission:reprocessing": {
      "active": true,
      "scope": "R1",
      "since": "2025-12-01"
    },
    "kfm:mission:algorithm_change": {
      "version_from": "v2.1",
      "version_to": "v2.2",
      "effective": "2025-12-08",
      "notes": "Cloud mask threshold updated"
    },
    "kfm:mission:status": "nominal"
  }
}
~~~

### STAC Items (optional but recommended)

STAC Items MAY specialize or override mission-level status when relevant:

- e.g., a specific Item produced during an incident window:

~~~json
{
  "type": "Feature",
  "id": "example-item-2025-12-09T15:00Z",
  "collection": "example-collection",
  "properties": {
    "datetime": "2025-12-09T15:00:00Z",
    "kfm:mission:status": "incident",
    "kfm:mission:product_availability": "degraded"
  }
}
~~~

If Item-level tags are omitted, UIs and graph ingestion SHOULD fall back to Collection-level tags.

---

## ✅ DCAT Implementation (Normative)

Every **DCAT Dataset** representing a mission or collection MUST:

1. Mirror the four tags in both `dcat:keyword` and `dct:subject`.  
2. Carry the `kfm:mission:*` extension properties aligned with STAC.

Example:

~~~json
{
  "@type": "dcat:Dataset",
  "dct:identifier": "example-collection",
  "dct:title": "Example Mission / Collection",
  "dcat:keyword": [
    "product-availability",
    "reprocessing",
    "algorithm-change",
    "mission-status"
  ],
  "dct:subject": [
    "product-availability",
    "reprocessing",
    "algorithm-change",
    "mission-status"
  ],
  "kfm:mission:product_availability": "operational",
  "kfm:mission:reprocessing": {
    "active": false
  },
  "kfm:mission:algorithm_change": {
    "version_to": "v2.2"
  },
  "kfm:mission:status": "nominal"
}
~~~

DCAT providers that cannot store nested objects MAY encode them via JSON-LD embedding or separate linked Entities, as long as semantics are preserved.

---

## 🎛️ Allowed Values & Field Definitions

### Enumerations

- **`kfm:mission:product_availability`**  
  - `operational`  
  - `paused`  
  - `degraded`  
  - `retired`

- **`kfm:mission:reprocessing.active`**  
  - `true` / `false`

- **`kfm:mission:reprocessing.scope`**  
  - `R1` — first/limited reprocessing campaign  
  - `R2` — second or subsequent campaign  
  - `full` — mission-wide reprocessing  

- **`kfm:mission:algorithm_change.version_from` / `version_to`**  
  - free-text semantic version strings, **strongly RECOMMENDED**: `vMAJOR.MINOR[.PATCH]`

- **`kfm:mission:algorithm_change.effective`**, **`kfm:mission:reprocessing.since`**  
  - ISO-8601 calendar dates: `YYYY-MM-DD`  

- **`kfm:mission:status`**  
  - `nominal`  
  - `anomaly`  
  - `incident`  
  - `ended`

### Field behavior

- If a mission has **never** undergone reprocessing, set:
  - `kfm:mission:reprocessing: { "active": false }`
- If an algorithm has **no prior version**, `version_from` MAY be omitted.  
- When a mission transitions to `ended`, new data MUST NOT be added, but Collection and Dataset records MUST remain discoverable.

---

## 🕸️ Neo4j / Graph Integration

Mission tags must be reflected in the **KFM Neo4j graph** for querying and Story Node integration.

### Graph mapping (draft schema, subject to KFM-OP review)

**Nodes:**

- `Mission` — represents a mission/collection family  
- `Dataset` — specific KFM dataset or collection  
- `MissionStatusEvent` — status changes over time (optional but recommended)  
- `AlgorithmVersion` — semantic version of mission algorithm  
- `ReprocessingCampaign` — reprocessing campaigns  

**Relationships (draft):**

- `(:Dataset)-[:PART_OF_MISSION]->(:Mission)`  
- `(:Mission)-[:HAS_CURRENT_STATUS]->(:MissionStatusEvent)`  
- `(:MissionStatusEvent)-[:APPLIES_TO]->(:Mission)`  
- `(:Mission)-[:HAS_ALGORITHM_VERSION]->(:AlgorithmVersion)`  
- `(:ReprocessingCampaign)-[:APPLIES_TO]->(:Mission)`  

**Key properties:**

- On `Mission` / `Dataset` nodes:
  - `mission_product_availability` (string)  
  - `mission_status` (string)  
- On `MissionStatusEvent`:
  - `status` (enum)  
  - `effective_date` (date)  
- On `AlgorithmVersion`:
  - `version` (string)  
  - `effective_date` (date)  
- On `ReprocessingCampaign`:
  - `scope` (enum)  
  - `active` (boolean)  
  - `since` (date)

Graph ingestion jobs MUST:

- derive node properties from STAC/DCAT `kfm:mission:*`  
- avoid duplicating secrets or sensitive provider internals  
- link back to STAC/DCAT identifiers and PROV Entities where appropriate

---

## 🧮 ETL & Backfill Workflows

Mission tags are applied and maintained via **deterministic ETL**:

- **Config location**  
  - `configs/pipelines/catalogs/mission-tags.yaml` — controls tag derivation and mapping.  

- **ETL code**  
  - `src/pipelines/catalogs/mission_tags.py` — reads provider catalogs or signals, writes updated STAC/DCAT and graph mappings.

- **Provenance & logs**  
  - Run logs: `mcp/experiments/catalogs/mission-tags/logs/`  
  - PROV bundles: `mcp/experiments/catalogs/mission-tags/prov.jsonld`

### Backfill strategy

1. **Discovery**  
   - Enumerate all relevant Collections / Datasets under `data/stac/**/collection.json` and `docs/catalogs/dcat/*.jsonld`.

2. **Derivation**  
   - If provider exposes status feeds, notices, or changelogs, use them as primary sources.  
   - If not, derive tags from:
     - internal operational knowledge  
     - release notes  
     - data gaps and anomaly records

3. **Update & PROV**  
   - Patch STAC/DCAT records deterministically with mission tags.  
   - Record each run as a PROV `Activity` linking old and new Entities.

4. **Drift control**  
   - CI must fail if:
     - any mission Collection / Dataset is missing required tags  
     - any value is outside allowed enumerations.

---

## 🧩 Story Node & Focus Mode Integration

Mission tags directly drive **Story Nodes** and **Focus Mode** behavior:

### Filters & facets

- Story Node and Focus Mode UIs expose:
  - **Availability** — filter by `product-availability`  
  - **Reprocessing** — filter by current or historical `reprocessing.active` / `scope`  
  - **Algorithm** — filter by `algorithm_change.version_to` and effective date  
  - **Status** — filter by `mission-status` (nominal / anomaly / incident / ended)

### Timeline badges & events

- When `kfm:mission:algorithm_change.effective` is set:
  - show a **timeline badge** marking algorithm version change  
  - offer details from `notes` and change logs
- When `kfm:mission:reprocessing.since` is set and `active == true`:
  - show continuous badges spanning reprocessing period  
- When `kfm:mission:status` ≠ `nominal`:
  - highlight affected time range and Story Nodes as **anomaly/incident** narratives

### Story Node content

Story Nodes referencing missions MUST:

- include mission tags in the Node metadata  
- clearly distinguish:
  - **facts** (tag values and dates)  
  - **interpretation** (what that means for quality/availability)  
  - **speculation** (possible causes, if not confirmed)  

This standard ensures Story Nodes can **cross-filter by mission state** without relying on provider-specific logic.

---

## 🧪 CI Policy (Must-Pass Rules)

Mission tag enforcement is handled via **catalog metadata CI workflows**.

### Validation rules

- **Rule CATALOG-MISSION-TAGS-001**  
  - All STAC Collections under `data/stac/**/collection.json` MUST:
    - include the four tags in `properties.kfm:tags[]`  
    - include all required `kfm:mission:*` fields

- **Rule CATALOG-MISSION-TAGS-DCAT-001**  
  - All DCAT Datasets under `docs/catalogs/dcat/*.jsonld` MUST:
    - include the four tags in both `dcat:keyword` and `dct:subject`  
    - include `kfm:mission:*` properties consistent with their STAC counterparts

- **Rule KFM-MISSION-TAGS-ENUMS-001**  
  - `product_availability`, `reprocessing.scope`, and `status` values MUST match the enumerations defined in this document.  
  - Dates MUST be ISO-8601 calendar dates (`YYYY-MM-DD`).

### CI implementation

- Workflows:
  - `.github/workflows/catalogs-metadata.yml`
- Responsibilities:
  - run JSON Schema validation for STAC/DCAT  
  - run mission-tag specific checks (allowed values, presence, consistency)  
  - emit telemetry to `catalog-telemetry.json` for governance audits

---

## ⚖ FAIR+CARE, Sovereignty, and Mission Tags

Mission tags intersect with FAIR+CARE and sovereignty in the following ways:

- **FAIR**  
  - Tags make mission status and changes **Findable** and **Accessible** via standard fields.  
  - Reprocessing and algorithm changes make data **Reusable** by exposing versioning and quality context.

- **CARE & sovereignty**  
  - When missions intersect with sensitive or sovereign knowledge:
    - mission tags MUST NOT reveal restricted operational details or sensitive incident context.  
    - reprocessing notes and algorithm descriptions MAY be generalized (e.g., “quality improvement”) where needed.  
  - Spatial details remain in STAC geometry; tags apply at mission-level but MAY avoid revealing sensitive operational patterns.

Any mission where sovereignty or privacy concerns apply must be reviewed by the **FAIR+CARE Council** before changes to mission tags are deployed.

---

## 🕰️ Version History

| Version  | Date       | Description                                                            |
|----------|------------|------------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Aligned with KFM-MDP v11.2.6; directory layout moved to top with standard emojis; expanded STAC/DCAT/graph/CI sections; added FAIR+CARE and pipeline integration. |
| v11.2.5  | 2025-12-01 | Initial definition of mission tags standard (four canonical tags).     |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **FAIR+CARE Council** and the **Reliability Guild**, with co-review by the Governance Council  
- must be updated whenever KFM changes mission tagging semantics, enumerations, or catalog/graph integration

Edits require approval from the **FAIR+CARE Council** and **Reliability Guild** and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and catalog metadata validation in CI.

<br/>

<sub>© Kansas Frontier Matrix · CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM-MDP v11.2.6</sub>

<br/>

<div align="center">

🏷️ **Kansas Frontier Matrix — Mission Tags Standard v11.2.6**  
Unified Mission Status · Catalog-Graph Harmony · FAIR+CARE Aligned  

[📘 Docs Root](../../README.md) · [📂 Standards Index](../README.md) · [📚 Catalog Standards Index](./README.md) · [⚖ Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>