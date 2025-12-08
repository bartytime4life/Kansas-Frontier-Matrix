---
title: "🌩️ Kansas Frontier Matrix — NEXRAD Watermarks Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmo/nexrad/watermarks/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Pipelines · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Backward compatible with v11.0.x NEXRAD pipelines"

status: "Active"
doc_kind: "Module Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/atmo-telemetry.json"
telemetry_schema: "schemas/telemetry/patterns/nexrad-watermark-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-compliant (auto-mask enabled for sensitive overlays)"
sensitivity: "Mixed (severe weather, emergency overlays, tribal lands)"
classification: "Public / Internal (operational module)"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/patterns/event-driven-deterministic-ingest.md@v11.2.4"
  - "docs/pipelines/atmo/nexrad/README.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:atmo:nexrad:watermarks:readme:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "atmo-nexrad-watermarks-module-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "atmospheric"
  applies_to:
    - "etl"
    - "streaming"
    - "stac"
    - "graph"
    - "provenance"
    - "telemetry"
    - "story-nodes"
  impacted_modules:
    - "docs/pipelines/atmo"
    - "docs/pipelines/atmo/nexrad"
    - "docs/pipelines/atmo/nexrad/watermarks"
    - "src/pipelines/atmo/nexrad"
    - "data/processed/atmo/nexrad"
    - "data/stac/atmo/nexrad"
    - "dist/provenance/*"
---

<div align="center">

# 🌩️ **Kansas Frontier Matrix — NEXRAD Watermarks Module**  
`docs/pipelines/atmo/nexrad/watermarks/README.md`

**Event-Time · Deterministic · Idempotent · lakeFS-Safe · FAIR+CARE Aligned**

</div>

---

## 📁 Module Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 atmo/
        └── 📁 nexrad/
            └── 📁 watermarks/
                📄 README.md                       # ← This file (module guide)
                📄 finalization-pattern.md         # NEXRAD event-time watermark & delay pattern
                📁 examples/
                │   📄 minimal-flow.md             # Small end-to-end example of preview → final
                │   📄 replay-behavior.md          # Deterministic replay & watermark drift analysis
                │   📄 qa-tests.md                 # QA test matrix & edge cases
                📁 design/
                │   📄 vcp-delay-rationale.md      # VCP-aware delay rationale & references
                └── 📁 notes/
                    📄 ops-runbook.md              # Operational notes for on-call / incidents

📁 src/
└── 📁 pipelines/
    └── 📁 atmo/
        └── 📁 nexrad/
            📄 config_watermarks.yaml              # Lateness buffers & VCP-specific delays
            📄 ingest_stream.py                    # NEXRAD event ingestion into stream
            📄 watermark_logic.py                  # Event-time, lateness, watermark functions
            📄 finalization_job.sql                # Streaming SQL / job definition
            📄 stac_emit.py                        # STAC Item & Collection emission utilities

📁 data/
└── 📁 processed/
    └── 📁 atmo/
        └── 📁 nexrad/
            📁 preview/                            # Optional preview-only radar products
            📁 final/                              # Final, watermark-stable radar products

📁 data/
└── 📁 stac/
    └── 📁 atmo/
        └── 📁 nexrad/
            📁 preview/                            # STAC Collections/Items for preview products
            📁 final/                              # STAC Collections/Items for final products
```

---

## 📘 Overview

The **NEXRAD Watermarks Module** defines how the Kansas Frontier Matrix:

- Applies **event-time watermarks** to NEXRAD Level-II radar streams,  
- Configures **VCP-aware finalization delays**,  
- Separates **preview** from **final** atmospheric products, and  
- Guarantees **deterministic, replay-safe behavior** for all radar-driven layers.

It is a **specialized sub-module** of:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`, and  
- The broader `docs/pipelines/atmo/nexrad/README.md` atmospheric radar pipeline family.

All NEXRAD pipelines that use streaming/event-driven ingestion **must** implement this module’s patterns for:

- Watermarking,  
- Finalization,  
- STAC/graph integration, and  
- Telemetry & FAIR+CARE compliance.

---

## 🧩 Module Components

### 1. Finalization pattern

- **Spec:** `finalization-pattern.md`  
- Defines:
  - Event-time watermark semantics,  
  - VCP-aware finalization delays,  
  - Preview vs final layer semantics,  
  - Deterministic replay & idempotent upsert rules.

All concrete NEXRAD pipelines reference this pattern as their **normative behavior spec**.

### 2. Examples

Located under `examples/`:

- `minimal-flow.md`  
  - End-to-end example from raw NEXRAD events → preview → final → STAC.

- `replay-behavior.md`  
  - Demonstrates how WAL/queue replay produces **identical final outputs** when pattern rules are followed.

- `qa-tests.md`  
  - Contains the **QA test matrix**:
    - Watermark drift tests,  
    - Volume completeness checks,  
    - VCP-delay enforcement tests,  
    - STAC & telemetry integrity tests.

### 3. Design notes

Located under `design/`:

- `vcp-delay-rationale.md`  
  - Documents:
    - VCP modes and typical scan durations,  
    - Justification for base delays and SAILS/MESO-SAILS buffers,  
    - References to NEXRAD engineering documentation.

### 4. Operational notes

Located under `notes/`:

- `ops-runbook.md`  
  - Describes:
    - How to interpret watermark & latency metrics in dashboards,  
    - What to do when volumes appear “stuck” in preview,  
    - Procedures for safe configuration changes and rollbacks.

---

## 🧭 Relationship to Other Patterns

This module is tightly coupled to two core KFM patterns:

- **Event‑Driven Deterministic Ingestion Pattern**  
  - Provides the **general** event → WAL → QA → canary → promote/rollback structure.  
  - NEXRAD watermarks reuse:
    - Idempotency keys,  
    - WAL behavior,  
    - Promotion/rollback semantics.

- **OpenLineage CI Integration Standard**  
  - Ensures NEXRAD runs emit:
    - OpenLineage run events,  
    - PROV‑O JSON-LD bundles,  
    - STAC/PROV/telemetry interlinks.

NEXRAD-specific configuration (e.g., VCP-aware delays) **must not violate** these general patterns.

---

## 🧪 Validation & CI Expectations

Pipelines under this module must integrate QA and CI checks defined in:

- `finalization-pattern.md`, and  
- `examples/qa-tests.md`.

At minimum, project CI must include:

- **Watermark drift** and **replay consistency** tests,  
- **Volume completeness** and **VCP-delay** enforcement tests,  
- **STAC integrity** tests using KFM STAC schemas,  
- **Telemetry coverage** tests using `patterns/nexrad-watermark-v1.json`.

Any failure in these checks is a **ship-blocker** for:

- New NEXRAD pipeline deployments, and  
- Configuration changes to watermark/wait-time parameters.

---

## 🧠 Story Nodes & Focus Mode

NEXRAD-driven Story Nodes (e.g., severe weather narratives, flash flood overlays) must:

- Reference **final** products as their primary data source,  
- Clearly indicate when visualizations use **preview** data (early view),  
- Link to:
  - STAC Items,  
  - PROV bundles,  
  - Telemetry and delay/latency metrics.

Focus Mode should:

- Let users understand **how stale or fresh** radar volumes are relative to event-time,  
- Indicate when data is still within a **finalization delay window**, and  
- Expose basic watermark/latency information for advanced users.

This module sets the **contracts** that Story Nodes can rely on for NEXRAD timing behavior.

---

## 🕰️ Version History

| Version  | Date       | Author / Steward                          | Summary                                                   |
|----------|------------|-------------------------------------------|-----------------------------------------------------------|
| v11.2.4  | 2025-12-07 | Atmo Pipelines + FAIR+CARE Council        | Initial NEXRAD watermarks module guide aligned with KFM v11.2.4. |

---

<div align="center">

🌩️ **Kansas Frontier Matrix — Atmospheric Pipelines Division**  

[⬅️ NEXRAD Pipelines Index](../README.md) ·  
[📐 Event-Driven Ingest Pattern](../../../patterns/event-driven-deterministic-ingest.md) ·  
[⚖️ Root Governance](../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📦 Releases](../../../../../releases/)

</div>