---
title: "🌩️ Kansas Frontier Matrix — Event-Time Watermarks for NEXRAD Ingest (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/radar/nexrad/event-time-watermarks.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Radar Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Ingest Standard"
header_profile: "standard"
footer_profile: "standard"

markdown_protocol_version: "KFM-MDP v11.2.4"
mcp_version: "MCP-DL v6.3"
license: "CC-BY 4.0"

scope:
  domain: "atmo.radar.nexrad"
  applies_to:
    - "etl"
    - "streaming-ingest"
    - "watermarks"
    - "stac"
    - "catalogs"
    - "graph"
    - "telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed · CARE-sensitive"
sensitivity: "Mixed (enable dynamic generalization & tribal review)"
classification: "Public / Internal (governed ingest standard)"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/ingest-radar-telemetry.json"
telemetry_schema: "schemas/telemetry/pipelines-radar-ingest-v3.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/RADAR-SOVEREIGNTY-GUIDE.md"
---

<div align="center">

# 🌩️ **Event-Time Watermarks for NEXRAD Ingest (KFM v11.2.4)**  
`docs/pipelines/radar/nexrad/event-time-watermarks.md`  

**Deterministic ingest · AVSET-safe · WAL-replayable · STAC/DCAT/PROV-aligned**

</div>

---

## 🗂️ Directory Layout (KFM v11.x Monorepo)

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 radar/
        └── 📁 nexrad/
            📄 event-time-watermarks.md          # ← This ingest standard
            📁 watermarks/                       # Finalization & delay patterns (canary/final)
            📁 qc/
            │   📄 tilt-detection.md
            │   📄 avset-rules.md
            │   📄 wedges.md
            📁 lineage/
            │   📄 prov-patterns.md
            └── 📁 sops/
                📄 ingest-runbook.md             # Operational SOPs (alerts, incident steps)