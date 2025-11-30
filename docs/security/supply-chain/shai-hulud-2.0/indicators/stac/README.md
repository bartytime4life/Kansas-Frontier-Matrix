---
title: "📦 KFM v11 — Shai-Hulud 2.0 Indicator STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/stac/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x STAC-governance model"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"

telemetry_ref: "../../../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/supply-chain-defense-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "IOC-STAC-Registry"
intent: "supply-chain-defense-indicator-stac"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📦 **Shai-Hulud 2.0 — Indicator STAC Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/stac/README.md`

**Purpose:**  
Define the **STAC Collections** and **STAC Items** that represent all  
Shai-Hulud 2.0 indicators (hash, pattern, YARA, structural, heuristic, composite)  
in a unified, standards-aligned discovery catalog.

**Scope:**  
STAC 1.0 · OGC API · DCAT 3 · JSON-LD · PROV-O lineaged indicator metadata  
</div>

---

## 🧬 1. Overview

The STAC registry for Shai-Hulud 2.0 provides:

- A **machine-readable catalog** of all indicators  
- STAC-compliant metadata for ingestion across tools  
- Uniform JSON formats for Items & Collections  
- DCAT + JSON-LD overlays for semantic interoperability  
- PROV-O lineage for full provenance reconstruction  
- Timeline + ecosystem indexing for Focus Mode  

Every indicator is represented as a **STAC Item**  
and grouped into **STAC Collections** by indicator family or ecosystem.

---

## 🧱 2. STAC Item Requirements (KFM v11)

Every Indicator STAC Item MUST contain:

### **Core Fields**
- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id` — UUIDv4  
- `geometry: null`  
- `bbox: []` or omitted  
- `properties.datetime` — detection timestamp  
- `properties.indicator_type` — hash | pattern | yara | structural | heuristic | composite  
- `properties.ecosystem` — npm | maven | pypi | bun | github-actions  

### **Assets**
- `assets.indicator` — the IoC JSON bundle  
- `assets.provenance` — PROV-O lineage  
- `assets.metadata` — DCAT overlay  
- `assets.evidence` — synthetic/redacted sample (optional)  

### **Links**
- Parent Collection  
- Related indicators  
- Related reports  
- Upstream/downstream lineage  

---

## 🗂️ 3. STAC Collection Requirements

Each indicator family (hash / pattern / yara / structural / heuristic / composite)  
MUST publish a STAC Collection with:

- `type: "Collection"`  
- `stac_version: "1.0.0"`  
- `license: "MIT"`  
- `extent.temporal.interval` — first_seen → last_seen  
- `keywords[]` — DCAT-compatible tags  
- `providers[]` — scanners, pipelines, or guild operators  
- `summaries.indicator_type[]`  
- `summaries.ecosystem[]`  
- `summaries.severity[]`

Collections serve as the **primary high-level discovery units**.

---

## 🧾 4. Metadata Alignment (DCAT · JSON-LD · PROV-O)

Each STAC Item & Collection MUST align with:

### **DCAT 3.0**
- Dataset-level metadata  
- Keywords, description, license, version, creator  

### **JSON-LD**
- Semantic-enhanced metadata layer  
- Exportable to RDF graphs  
- Neo4j knowledge graph ingest  

### **PROV-O**
- `prov:wasGeneratedBy` — scanner or pipeline  
- `prov:used` — source artifact  
- `prov:wasDerivedFrom` — upstream IoCs or evidence  
- `prov:wasAttributedTo` — KFM Security Guild  

This ensures the STAC catalog is fully traceable, audit-ready, and FAIR+CARE-compliant.

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/stac/
├── 📄 README.md                # This file
├── 📦 collections/             # STAC Collections for indicator families
├── 📄 items/                   # Individual STAC Items (one per indicator UUID)
├── 🧾 metadata/                # DCAT + JSON-LD overlays for STAC records
├── 🧪 validation/              # JSON Schema / SHACL validation assets
└── 🧷 samples/                 # Synthetic sample STAC Items for CI and onboarding
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Focus Mode v3 consumes the STAC registry to:

- Populate threat timelines  
- Anchor Story Nodes with STAC Item data  
- Correlate indicator families visually  
- Locate ecosystem-specific attack clusters  
- Provide explainable narrative trails using provenance  

Story Nodes link directly to:

- STAC Item `id`  
- `properties.datetime`  
- provenance assets  
- related indicators in the same Collection  

This creates a **semantic, temporal, and structural narrative graph** around the worm.

---

## 🧭 Version History

| Version | Date       | Summary                                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji-prefix directory added; governance/H3 upgrades; aligned with KFM-MDP v11.2.2.     |
| v10.4.0 | 2025-11-15 | Earlier satellite overview; pre-v11 metadata structure.                                                    |

---

<div align="center">

[📘 Docs Root](../../../../../../..) · [🧪 Pipelines](../../../../../pipelines) · [🌐 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

