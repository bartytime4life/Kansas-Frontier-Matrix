---
title: "🧩 Kansas Frontier Matrix — Event Schema Versioning & Deprecation Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/events/versioning/README.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Reliability Boards · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Core Standard"

header_profile: "standard"
footer_profile: "standard"
markdown_protocol_version: "KFM-MDP v11.2.4"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/events-versioning-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Event Schema Versioning & Deprecation Standard**  
`docs/standards/events/versioning/README.md`

**Purpose**  
Define how the Kansas Frontier Matrix (KFM) maintains **deterministic, evolvable, FAIR+CARE-aligned event contracts** across all ingest, lineage, telemetry, and Focus Mode execution flows, with auditable schema evolution and CI-enforced governance.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Event_Schemas-orange)](../../faircare/FAIRCARE-GUIDE.md)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable_Standard-brightgreen)](../../../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

This standard defines how KFM ensures **deterministic, evolvable event schemas** and prevents:

- Silent drift between event producers and consumers  
- Incompatible schema changes across versions or services  
- Non-auditable or ad-hoc changes to core contracts

Event schemas in KFM are the backbone of:

- ETL & streaming ingest  
- OpenLineage & STAC/DCAT/PROV-O derivation  
- Neo4j graph mutation events  
- Focus Mode narrative computation  
- Energy & carbon telemetry reporting  
- Automated auditing & reproducibility

To preserve determinism and governance, all schemas follow:

- **Strict SemVer**  
- **Machine-readable deprecation & sunset metadata**  
- **Canonical event envelopes**  
- **Schema registries** and CI/CD enforcement

---

## 🗂️ Directory Layout

```text
📁 repo-root/
├── 📁 docs/
│   └── 📁 standards/
│       └── 📁 events/
│           └── 📁 versioning/
│               └── 📄 README.md                  # This document (event versioning standard)
└── 📁 schemas/
    └── 📁 events/
        └── 📁 <event-type>/
            ├── 📄 1.0.0.json
            ├── 📄 1.1.0.json
            ├── 📄 1.1.1.json
            ├── 📄 CHANGELOG.md
            └── 📄 index.json                     # Machine-readable registry for this event type
```

- **Docs** capture the normative rules (this file).  
- **Schemas** hold the JSON Schema definitions and registry metadata used by CI and runtime validation.

---

## 🧩 SemVer Rules for KFM Event Schemas

Event schemas obey **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`.

### 🟥 MAJOR (`X.0.0`) — Breaking Changes

Triggered by:

- Removing or renaming fields  
- Changing type or semantic meaning of a field  
- Changing requiredness (optional → required or vice versa)  
- Rewriting the event structure or envelope semantics  

Requirements:

- Formal **governance approval** (Metadata Board, Reliability, FAIR+CARE as needed)  
- Expired **sunset period** for any deprecated fields being removed  
- **Impact statement** for downstream systems (graph, telemetry, Focus Mode)  
- Updated registry and CHANGELOG entries

---

### 🟧 MINOR (`X.Y.0`) — Backward Compatible Additions

Used for:

- Adding new **optional** fields  
- Adding **new event types** within a family  
- Marking fields with `"deprecated": true` and an `x-sunset` date  
- Extending metadata blocks (e.g., telemetry, FAIR+CARE markers)

Rules:

- No required fields may be removed or made stricter.  
- Any planned removal must be **announced via deprecation** and scheduled for the next MAJOR.  

---

### 🟩 PATCH (`X.Y.Z`) — Non-Structural Changes

Used for:

- Clarifying descriptions and docs  
- Correcting default values (without changing semantics)  
- Telemetry alignment and non-breaking constraints (e.g., narrower enums that are a subset of existing values)  
- Bug fixes in examples, not in the schema’s structural shape

Rules:

- **No shape changes** allowed:
  - No new fields, no removals.  
  - No type changes, no new required fields.

---

## 🔧 Event Envelope (Canonical)

All events MUST follow this canonical **envelope structure**:

```json
{
  "event_type": "string",
  "schema_version": "X.Y.Z",
  "occurred_at": "ISO-8601 timestamp",
  "id": "evt_<unique>",
  "source": "producer-identifier",
  "payload": {}
}
```

Notes:

- The **envelope** is versioned separately from the **payload** schema.  
- `schema_version` refers to the **payload schema** used for this event.  
- Envelope-level changes follow the same SemVer rules and must be documented in their own schema.

---

## 🧱 Deprecation & Sunset Rules

Deprecation is **explicit and machine-readable**.

| Rule                                      | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| **Deprecation requires MINOR bump**       | Fields are not removed immediately; MAJOR is required for removal.         |
| **Sunset window: ≥ 2 MINOR versions**     | A field must persist for at least two MINOR versions before removal.       |
| `"deprecated": true` marker               | Required on any field scheduled for removal.                               |
| `"x-sunset": "YYYY-MM-DD"`                | Required; removal MUST align with next MAJOR after this date.              |
| Automated CI deprecation checks           | Fail builds if sunset date has passed without a corresponding MAJOR bump.  |

Example field definition in JSON Schema:

```json
{
  "type": "string",
  "title": "Legacy href",
  "description": "Legacy link field; use payload.assets[].href instead.",
  "deprecated": true,
  "x-sunset": "2026-06-30"
}
```

---

## 🗃️ Schema Registry Requirements

Each event type must maintain a **machine-readable registry** (e.g. `schemas/events/<event-type>/index.json`) that tracks:

- **Latest stable version**  
- **Supported MINOR ranges** (e.g. `N` and `N-1`)  
- **Deprecated fields** per MINOR range  
- Links to **schema files**, **CHANGELOG**, and **integrity hashes**

Example registry entry:

```json
{
  "stac.item.ingested": {
    "latest": "2.4.0",
    "supported_minors": ["2.4.x", "2.3.x"],
    "deprecated_fields": {
      "2.3.x": ["payload.assets[].legacyHref"]
    },
    "links": {
      "schema": "/schemas/events/stac.item.ingested/2.4.0.json",
      "changelog": "/schemas/events/stac.item.ingested/CHANGELOG.md"
    }
  }
}
```

CI and runtime tooling use this registry to:

- Enforce **supported version ranges**  
- Warn or block on use of **unsupported or sunset versions**  
- Cross-check **hashes** and **immutability** of schemas

---

## 🛡️ CI/CD Enforcement

KFM CI/CD workflows MUST validate:

- **SemVer correctness** for all schema changes  
- **Schema immutability** (no changes to files with existing versions; hashes locked)  
- **Backward compatibility** for MINOR/PATCH updates  
- **Deprecation budgets** (sunset rules and timelines)  
- **Change audit trail & provenance stamping** (PROV/O penLineage alignment)  
- **FAIR+CARE metadata alignment** (presence of sensitivity, provenance, and sovereignty markers where applicable)

Violations:

- **Block merge** for breaking or governance-violating changes.  
- **Require human approval** (Metadata & Reliability Boards, FAIR+CARE Council) for edge cases and MAJOR upgrades.

---

## 🌿 FAIR+CARE Integration

Event schemas MUST embed or link:

- **Provenance semantics** (PROV-O terms, where applicable)  
- **GeoSPARQL constraints** for spatial fields (valid geometries, CRS metadata)  
- **Cultural sensitivity markers**, such as:
  - `x-sensitivity-level`, `x-indigenous-flag`, `x-sovereignty-scope`  
- **AI transparency metadata** for model-generated fields (e.g. `x-ai-generated: true`)

These markers enable:

- FAIR+CARE-aware downstream processing  
- Appropriate **masking / aggregation** in Story Nodes and Focus Mode  
- **Governance-aware routing** (e.g., restricted vs public event sinks)

---

## 🔌 Focus Mode Integration

Events relevant to Focus Mode (narrative triggers, spatial/temporal transitions, model inference spans) MUST declare:

- `"x-focus-scope"` — e.g., `"story-node-trigger"`, `"map-layer-update"`  
- `"x-focus-sensitivity"` — e.g., `"low"`, `"medium"`, `"high"`  
- `"x-story-node-link"` — Story Node IDs or patterns influencing narrative flows

These fields enable:

- Deterministic, explainable Focus Mode journeys  
- Clear separation between **data updates** and **narrative semantics**  
- Governance-aware controls over which events can influence user-facing stories

---

## 🧮 Energy & Carbon Telemetry

All event schemas MUST support an optional, **standard telemetry block**:

```json
{
  "telemetry": {
    "energy_kwh": "number",
    "carbon_kg": "number",
    "hardware": "string"
  }
}
```

Guidelines:

- Telemetry is **optional** at the event level, but **strongly recommended** for:
  - Long-running computation  
  - Model inference runs  
  - Bulk ETL or aggregation operations  
- Values feed into:
  - `energy_schema` / `carbon_schema`  
  - Telemetry Council dashboards and FAIR+CARE sustainability reporting

---

## 📝 Version History

| Version | Date       | Summary                                                                            |
|---------|-----------:|------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Initial creation of unified event-schema versioning & deprecation standard under KFM-MDP v11.2.4. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · 🧩 Diamond⁹ Ω / 👑 Crown∞Ω Ultimate Certified  

Deterministic Events · CI-Enforced · Telemetry-Backed · FAIR+CARE-Aligned  

[🧩 Events Standards Index](../README.md) • [📚 Standards Home](../../README.md) • [⚖️ Governance Charter](../../governance/ROOT-GOVERNANCE.md)

</div>