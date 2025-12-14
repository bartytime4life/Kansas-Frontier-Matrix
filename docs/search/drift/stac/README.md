---
title: "🗂️ KFM — DRIFT STAC (Retrieval Episode Items · Evidence Bundles · CARE-Redacted Geometry)"
path: "docs/search/drift/stac/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Catalog Profile + Runbook"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "drift-stac-retrieval-episodes"
audience:
  - "Search Engineering"
  - "Catalog + Provenance Engineering"
  - "Focus Mode Engineering"
  - "Governance Reviewers"

classification: "Public (Governed)"
fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
redaction_required: true
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:search:drift:stac:v11.2.6"
semantic_document_id: "kfm-drift-stac"
event_source_id: "ledger:docs/search/drift/stac/README.md"
immutability_status: "version-pinned"

telemetry_schema: "../../../../schemas/telemetry/drift-search-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

json_schema_ref: "../../../../schemas/json/drift-stac-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/drift-stac-v11-shape.ttl"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "fabricated-claims"
  - "content-alteration"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded by drift-search-v12"
---

<div align="center">

# 🗂️ **KFM — DRIFT STAC**
`docs/search/drift/stac/README.md`

**Purpose**  
Define how DRIFT Search emits **STAC Collections/Items** representing **retrieval episodes** and **evidence bundles**,
with **PROV-aligned lineage** and **CARE-redacted geometry** suitable for governed discovery and audit.

<img src="https://img.shields.io/badge/STAC-KFM--STAC%20v11-brightgreen" />
<img src="https://img.shields.io/badge/Provenance-PROV--O%20Aligned-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

DRIFT Search can emit STAC records to make retrieval **auditable, reproducible, and catalog-discoverable**.

A DRIFT STAC Item represents a **retrieval episode** (a single governed search execution), capturing:

- workflow identifiers and configuration hashes,
- index snapshot references (what the search ran “against”),
- policy gate outcomes (CARE/sovereignty filtering),
- evidence bundle references (STAC/DCAT/graph entity ids),
- provenance pointers (PROV-O bundle and/or OpenLineage references),
- telemetry references (latency/energy/carbon) when enabled.

### Governance posture

Because `redaction_required: true` and `sensitivity_level: Medium`, DRIFT STAC MUST:

- avoid precise site coordinates,
- use generalized spatial footprints (region/H3 aggregation) or omit geometry,
- store query text only when permitted; otherwise store **query hashes** and redacted summaries,
- keep evidence as **references** (ids/links), not raw sensitive content.

---

## 🗂️ Directory layout

~~~text
📁 docs/search/drift/stac/                            — DRIFT STAC reference and templates
├── 📄 README.md                                      — This document
└── (optional) templates/                             — Item/Collection templates (provenance-safe)
~~~

Recommended operational output paths (house defaults; may be overridden by config):

~~~text
📁 data/stac/search/drift/                            — DRIFT retrieval episode STAC Collection/Items
📁 data/processed/search/drift/                       — Retrieval artifacts (evidence manifests, redaction reports)
📁 data/processed/prov/search/drift/                  — PROV-O bundles for retrieval episodes
~~~

---

## 🧭 What gets a STAC record

### STAC Collection

A Collection SHOULD represent a stable family of retrieval episodes.

Recommended collection id:

- `kfm-search-drift-episodes`

Collection SHOULD be version-pinned by:

- `kfm:workflow_version`
- `kfm:policy_version`
- `kfm:index_snapshot_id` (or an index lineage reference)

### STAC Item (retrieval episode)

A retrieval episode Item SHOULD be created per execution that produces a governed output bundle.

Item examples include:

- a Focus Mode “research run” over a bounded topic,
- a Story Node evidence acquisition run,
- a scheduled “retrieval health check” run (with redaction-safe outputs).

---

## 🧱 Identifier and naming rules

### Episode id (deterministic)

A retrieval episode id MUST be stable when inputs and snapshots are identical.

Recommended seed material (canonical JSON; stable key order):

- `query_hash`
- `constraints` (time range, generalized bbox/h3 scope, role)
- `workflow_id` + `workflow_version`
- `policy_bundle_hash`
- `index_snapshot_id` (or catalog/graph snapshot refs)

Recommended id form:

- `urn:kfm:search:drift:episode:<sha256_16>`

### STAC Item id

Recommended:

- `id = "<episode_id>"` (string without spaces), or
- `id = "urn:kfm:search:drift:episode:<sha256_16>"`

The Item MUST also include the episode id in properties:

- `properties.kfm:retrieval_episode_id`

---

## 🧬 STAC fields and profiles

DRIFT Items MUST validate under the governed STAC profile (`KFM-STAC v11`) and SHOULD include DRIFT-specific properties.

### Required Item fields (minimum)

- `stac_version`
- `stac_extensions` (as required by KFM-STAC profile)
- `id`
- `type: "Feature"`
- `collection`
- `datetime` (retrieval execution time)
- `properties` (KFM-required + DRIFT fields)
- `assets` (links to evidence/prov/telemetry artifacts)
- `links` (to collection, related docs, and provenance anchors)

### Geometry and bbox (CARE-redacted)

One of the following MUST be used:

1) **Generalized geometry** (preferred): region-level polygon or H3-derived envelope.  
2) **Null geometry** (allowed): when any spatial footprint would be sensitive or misleading.

Rules:

- If the query concerns sensitive heritage contexts, geometry MUST NOT become more specific than allowed by policy.
- If the query is purely non-spatial, geometry MAY be null.

---

## 🧾 DRIFT STAC properties (recommended)

Properties are designed to support audit, replay, and safe discovery.

### Retrieval identity and determinism

- `kfm:retrieval_episode_id` (stable)
- `kfm:workflow_id` (e.g., `drift:hybrid-global-local`)
- `kfm:workflow_version` (e.g., `v11.2.6`)
- `kfm:config_hash` (sha256)
- `kfm:policy_bundle_hash` (sha256)
- `kfm:index_snapshot_id` (stable id)
- `kfm:code_commit_sha` (commit used to execute)

### Query representation (privacy-safe)

- `kfm:query_hash` (sha256 of normalized query)
- `kfm:query_redacted` (boolean)
- `kfm:query_summary` (short, policy-safe summary; optional)
- `kfm:constraints` (time range + generalized scope; no precise coordinates)

### CARE and governance outcomes

- `kfm:care_gate_status`: `allow` | `redact` | `deny`
- `kfm:sovereignty_gate`: `clear` | `restricted` | `conflict` | `unknown`
- `kfm:redaction_summary` (counts/categories; no sensitive details)
- `kfm:access_class` (role/scope class; if used)

### Retrieval diagnostics (non-sensitive)

- `kfm:anchor_count`
- `kfm:graph_traversal_depth_max`
- `kfm:evidence_count_by_type` (Document/Dataset/Place/Event/Person; aggregated)
- `kfm:fusion_method` (e.g., `rrf`, `weighted_sum`; optional)

---

## 📦 Assets (what the Item points to)

DRIFT STAC Items SHOULD carry assets that make the episode inspectable without leaking restricted content.

Recommended assets:

- `prov_bundle` (PROV-O JSON-LD)
- `openlineage_events` (JSON/JSONL reference, if used)
- `evidence_manifest` (JSON listing only identifiers/refs)
- `redaction_report` (JSON summary; no sensitive coordinates)
- `telemetry` (JSON reference; energy/carbon optional)
- `query_plan` (optional; policy-safe)

### Asset metadata recommendations

Each asset SHOULD include:

- `type` (MIME type)
- `roles` (e.g., `provenance`, `metadata`, `report`, `telemetry`)
- `checksum:sha256` (where supported by profile/policy)
- `created` and `updated` timestamps where relevant

---

## 🔗 PROV alignment

DRIFT STAC Items are a catalog layer; PROV is the source of truth for lineage.

Minimum PROV expectations for a retrieval episode:

- `prov:Activity` = `drift_retrieval_episode`
- `prov:Entity` = episode outputs (evidence manifest, redaction report, narrative stub)
- `prov:Agent` = service/runner (and optionally human reviewer)
- relations:
  - `prov:used` (index snapshots, configs, policies)
  - `prov:wasGeneratedBy` (outputs generated by retrieval activity)
  - `prov:wasDerivedFrom` (outputs derived from governed sources/evidence)

STAC linkages:

- `properties.prov:wasGeneratedBy` MAY reference the retrieval activity id.
- `properties.prov:wasDerivedFrom` SHOULD reference stable evidence entity ids (not raw content).

---

## 🗺️ Flow: retrieval → STAC episode item

~~~mermaid
flowchart TD
  A["DRIFT workflow run"] --> B["CARE gate + redaction summary"]
  B --> C["Evidence manifest - references only"]
  C --> D["PROV bundle - lineage"]
  D --> E["Emit STAC Item - retrieval episode"]
  E --> F["Validate STAC profile + publish (governed)"]
~~~

---

## 🧪 Validation and CI expectations

A governed DRIFT STAC Item MUST pass:

- STAC validation:
  - PySTAC `item.validate()` (or equivalent)
  - stac-validator (when used)
- KFM-STAC profile checks:
  - required `kfm:*` properties present
  - required assets and roles present
- CARE leakage checks:
  - no raw sensitive coordinates
  - no restricted identifiers that bypass redaction
- Provenance linkage checks:
  - `prov_bundle` asset exists and is schema-valid (KFM-PROV v11)
  - episode id stable and referenced consistently

---

## 🧰 Minimal example (template)

This example is schematic and uses placeholders. It demonstrates safe patterns:
hash-based query representation, generalized geometry, and provenance assets.

~~~json
{
  "stac_version": "1.0.0",
  "stac_extensions": [],
  "type": "Feature",
  "id": "urn:kfm:search:drift:episode:0123abcd4567ef89",
  "collection": "kfm-search-drift-episodes",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2025-12-13T00:00:00Z",
    "kfm:retrieval_episode_id": "urn:kfm:search:drift:episode:0123abcd4567ef89",
    "kfm:workflow_id": "drift:hybrid-global-local",
    "kfm:workflow_version": "v11.2.6",
    "kfm:query_hash": "sha256:…",
    "kfm:query_redacted": true,
    "kfm:care_gate_status": "redact",
    "kfm:sovereignty_gate": "unknown",
    "kfm:index_snapshot_id": "urn:kfm:search:index:snapshot:…",
    "kfm:code_commit_sha": "<latest-commit-hash>"
  },
  "assets": {
    "prov_bundle": {
      "href": "artifacts/prov/run.jsonld",
      "type": "application/ld+json",
      "roles": ["provenance"]
    },
    "evidence_manifest": {
      "href": "artifacts/evidence/manifest.json",
      "type": "application/json",
      "roles": ["metadata"]
    },
    "redaction_report": {
      "href": "artifacts/reports/redaction.json",
      "type": "application/json",
      "roles": ["report"]
    }
  },
  "links": [
    { "rel": "collection", "href": "./collection.json", "type": "application/json" }
  ]
}
~~~

---

## 🕰️ Version history

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed DRIFT STAC reference; codified retrieval episode Items, CARE-redacted geometry rules, asset roles, and PROV alignment. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC-KFM--STAC%20v11-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Gated-gold" />
<img src="https://img.shields.io/badge/Sensitivity-Medium%20%7C%20Redaction%20Required-orange" />

[⬅ Back to DRIFT Search](../README.md) ·
[🔍 Search Index](../../README.md) ·
[🏛️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛰 Telemetry Schema](../../../../schemas/telemetry/drift-search-v11.json)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

