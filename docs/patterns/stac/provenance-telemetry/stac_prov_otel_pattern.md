---
title: "🧭 KFM v11.2.6 — Attaching Telemetry & Provenance to STAC (Processing, PROV‑O, OpenLineage, RO‑Crate)"
path: "docs/patterns/stac/provenance-telemetry/stac_prov_otel_pattern.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Reliability Engineering"
content_stability: "stable"
status: "Active"

doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "metadata-integration"
  applies_to:
    - "data/**/stac/**"
    - "pipelines/**"
    - "releases/**"

fair_category: "F1-A1-I1-R1"
care_label: "Sovereignty-respecting · Context & provenance first"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "FAIR+CARE Council & Reliability Engineering"

security_posture: "Diamond⁹ Ω / Crown∞Ω"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM v12"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "././releases/v11.2.6/signature.sig"
attestation_ref: "././releases/v11.2.6/slsa-attestation.json"
sbom_ref: "././releases/v11.2.6/sbom.spdx.json"
manifest_ref: "././releases/v11.2.6/manifest.zip"

telemetry_ref: "././releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "././schemas/telemetry/markdown-protocol-v11.2.6.json"
energy_schema: "././schemas/telemetry/energy-v2.json"
carbon_schema: "././schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:patterns:stac-provenance-telemetry:v11.2.6"
semantic_document_id: "kfm-pattern-stac-provenance-telemetry-v11.2.6"
event_source_id: "ledger:kfm:doc:patterns:stac-provenance-telemetry"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

# 🧭 Attaching Telemetry & Provenance to STAC

## 📘 Overview

**Purpose**  
Provide standards-aligned, schema-lintable ways to attach:

- OpenTelemetry (OTel) trace context (trace/span IDs),
- energy and carbon telemetry (kWh, kgCO₂e, method),
- provenance (W3C PROV-O as JSON-LD),

to STAC Items/Collections using:

1. STAC Processing Extension fields + links
2. (Optional) links to OpenLineage run/job resources
3. Bundled PROV-O JSON-LD or RO-Crate referenced by STAC

### 1. Minimal concepts

- **STAC Processing Extension**: records how an Item was produced (software, parameters, runtime).
- **OTel trace context**: enables end-to-end observability in governed pipelines.
- **Energy/Carbon telemetry**: stores units, scope, method, and time window for sustainability accounting.
- **W3C PROV-O**: machine-actionable lineage (Entities, Activities, Agents) serialized as JSON-LD.
- **OpenLineage**: cross-system run/job lineage; linked via `links[]` for discoverability.
- **RO-Crate**: portable research object packaging provenance + manifests + attestations.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/
│   ├── 📁 patterns/
│   │   └── 📁 stac/
│   │       └── 📁 provenance-telemetry/
│   │           └── 📄 stac_prov_otel_pattern.md       — ← This pattern
│   └── 📁 standards/
│       ├── 📁 governance/
│       │   └── 📄 ROOT-GOVERNANCE.md                  — Governance charter (required)
│       ├── 📁 faircare/
│       │   └── 📄 FAIRCARE-GUIDE.md                   — Ethics reference (required)
│       └── 📁 sovereignty/
│           └── 📄 INDIGENOUS-DATA-PROTECTION.md       — Sovereignty policy (required)
├── 📁 data/
│   └── 📁 stac/
│       ├── 📁 collections/                            — STAC Collections
│       ├── 📁 items/                                  — STAC Items
│       └── 📁 provenance/                             — PROV bundles + RO-Crates referenced by STAC
└── 📁 schemas/
    ├── 📁 stac/                                       — STAC profiles + extension constraints
    └── 📁 telemetry/                                  — Energy/carbon schemas + validators
~~~

---

## 🧭 Context

This pattern applies when:

- generating derived assets (reprojection, mosaics, model outputs),
- promoting artifacts to trusted tiers (`data/processed/**`),
- supporting Story Nodes / Focus Mode with traceable, auditable lineage,
- needing sustainability reporting (energy and carbon accounting).

---

## 🧱 Architecture

### 1. What goes where in STAC

- **Item properties**: processing metadata, trace context, telemetry values.
- **Item links**: provenance bundles (PROV JSON-LD), RO-Crate packages, OpenLineage resources.

### 2. Trace context requirements (recommended)

To keep IDs validation-friendly:

- `trace_id`: 32 lowercase hex chars
- `span_id`: 16 lowercase hex chars
- `sampled`: boolean

### 3. Telemetry requirements (recommended)

All telemetry objects SHOULD include:

- total value and unit (kWh, kgCO₂e),
- time window in UTC,
- measurement method and version,
- scope (for carbon) and factor source where applicable.

### 4. Provenance packaging requirements

- PROV bundles SHOULD be JSON-LD (`application/ld+json`).
- RO-Crate SHOULD be a portable artifact referenced by STAC (e.g., `application/zip`).
- Provenance SHOULD remain queryable even if external run systems are unavailable.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Pipeline run"] --> B["STAC Processing fields"]
  A --> C["PROV JSON-LD bundle"]
  A --> D["Energy and carbon telemetry"]
  A --> E["Optional OpenLineage run link"]
  C --> F["RO-Crate packaging"]
  B --> G["STAC Item published"]
  D --> G
  E --> G
  F --> G
~~~

This diagram shows a single run emitting multiple artifacts, all anchored to the STAC Item.

---

## 📦 Data & Metadata

### 1. STAC Item example (Processing + Telemetry + Provenance links)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/processing/v1.1.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "kfm-example-item-2025-12-12",
  "geometry": { "...": "redacted" },
  "bbox": [0, 0, 0, 0],
  "properties": {
    "datetime": "2025-12-12T00:00:00Z",

    "processing:level": "L2",
    "processing:software": [
      {
        "name": "kfm-etl",
        "version": "11.2.6",
        "parameters": { "window_days": 3, "method": "gapfill+regrid-v2" }
      }
    ],

    "processing:lineage": [
      {
        "activity": "etl-run",
        "otlp:trace_id": "f23b8e0f5c0d42a9a0e7f7d9f0e1abcd",
        "otlp:span_id": "0f1e2d3c4b5a6978",
        "otlp:sampled": true
      }
    ],

    "telemetry:energy": {
      "kwh_total": 1.92,
      "kwh_by_cloud": { "gcp": 1.52, "local": 0.4 },
      "time_window_utc": ["2025-12-12T00:01:03Z", "2025-12-12T00:07:41Z"],
      "measurement_method": "power-model-v2 (CPU/GPU nameplate × utilization × runtime)"
    },
    "telemetry:carbon": {
      "kgco2e_total": 0.83,
      "scope": "location-based",
      "grid_region": "RFCM",
      "emissions_factor_source": "egrid-2025q3",
      "conversion_version": "energy-to-co2e-v2"
    },

    "scientific:doi": "10.5281/zenodo.1234567",
    "scientific:citation": "KFM (2025). Example processing chain…"
  },
  "assets": {
    "data": {
      "href": "s3://kfm/example/data.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  },
  "links": [
    {
      "rel": "provenance",
      "type": "application/ld+json",
      "title": "KFM PROV-O lineage (JSON-LD)",
      "href": "../../dcat-prov/manifests/kfm-example-item-2025-12-12.prov.jsonld"
    },
    {
      "rel": "describedby",
      "type": "application/zip",
      "title": "RO-Crate (PROV, OpenLineage, SBOM, attestations)",
      "href": "../../dcat-prov/ro-crates/kfm-example-item-2025-12-12.ro-crate.zip"
    },
    {
      "rel": "related",
      "type": "application/json",
      "title": "OpenLineage Run (etl-run)",
      "href": "https://lineage.kfm.local/api/runs/01HFYVDEW8K0M2..."
    }
  ]
}
~~~

### 2. Minimal PROV-O JSON-LD bundle (illustrative)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "urn:kfm:"
  },
  "@graph": [
    {
      "@id": "kfm:item:kfm-example-item-2025-12-12",
      "@type": "prov:Entity"
    },
    {
      "@id": "kfm:process:proc-id",
      "@type": "prov:Activity",
      "prov:startedAtTime": { "@value": "2025-12-12T00:01:03Z", "@type": "xsd:dateTime" },
      "prov:endedAtTime": { "@value": "2025-12-12T00:07:41Z", "@type": "xsd:dateTime" }
    }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

| Concern | STAC representation | PROV/DCAT representation |
|---|---|---|
| Processing context | `processing:*` fields | `prov:Activity` metadata |
| Lineage linkage | `links[rel=provenance]` | `prov:used`, `prov:wasGeneratedBy` |
| Quality/run context | `links[rel=related]` (OpenLineage) | OpenLineage run/job facets |
| Telemetry | `telemetry:*` fields | governed telemetry schemas; optional DCAT quality/measurement linkage |
| Packaging | `links[rel=describedby]` (RO-Crate) | artifact bundles with manifests, SBOM, attestations |

---

## 🧠 Story Node & Focus Mode Integration

- Story Nodes SHOULD:
  - cite the STAC Item ID as the stable anchor,
  - render provenance links for traceability,
  - surface telemetry summaries only at governance-approved aggregation levels.
- Focus Mode SHOULD:
  - traverse from STAC → provenance bundle → upstream sources,
  - avoid exposing internal-only URIs when policy requires redaction.

---

## 🧪 Validation & CI/CD

Minimum checks SHOULD include:

- STAC validation against KFM-STAC profile (extensions locked)
- PROV JSON-LD schema validation and JSON-LD parse
- Telemetry schema validation (energy/carbon)
- Trace ID formatting validation (regex checks)
- Secret/PII scanning for any emitted links, telemetry payloads, or manifests

---

## ⚖ FAIR+CARE & Governance

- Telemetry MUST NOT disclose protected operational details (e.g., internal hostnames) in public artifacts unless allowed.
- For Indigenous or sensitive datasets:
  - prefer generalized values and coarse time windows,
  - ensure any coordinates or AOIs comply with sovereignty policy,
  - propagate access labels and care labels through all derivative products.

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---|---|
| v11.2.6 | 2025-12-12 | Initial governed release |

---

<div align="center">

🧭 **STAC Provenance & Telemetry Pattern**  
Transparent Systems · Ethical Metrics · Sustainable Intelligence

[📘 Docs Root](../../../README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>