---
title: "📦 KFM v11 — Shai-Hulud 2.0 STAC Collections & Items (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/stac/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x STAC integration model"

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
doc_kind: "STAC-Collections"
intent: "supply-chain-defense-stac-catalog"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📦 **Shai-Hulud 2.0 — STAC Collections & Items**
`docs/security/supply-chain/shai-hulud-2.0/stac/README.md`

**Purpose:**  
Provide the unified **STAC 1.0.0–aligned catalog** for all Shai-Hulud 2.0  
indicators, protections, provenance bundles, workflows, and reports.

**Scope:**  
STAC Items · STAC Collections · DCAT mappings · JSON-LD contexts · PROV-O lineage  
</div>

---

## 🧬 1. Overview

The STAC directory is the **canonical machine-readable catalog** for all Shai-Hulud 2.0 entities.

It includes:

- Indicators: hash, pattern, YARA, heuristic, structural, composite  
- Protections: lifecycle, dependency, workflow, provenance, sbom, runner, network  
- Reports: incidents, threat analyses, correlation dossiers  
- Workflow hardening items  
- Sample artifacts for CI/onboarding  

All STAC entities follow the **KFM STAC v11 Profile** extending STAC 1.0.0 with:

- DCAT 3.0 dataset semantics  
- PROV-O lineage  
- KFM operational metadata  
- JSON-LD semantic interoperability  

---

## 🧱 2. STAC Item Requirements (KFM v11 Profile)

Each Shai-Hulud 2.0 STAC Item must include:

### **Core Fields**
- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id` — unique UUID  
- `geometry: null` (non-geospatial)  
- `bbox: []` (or omitted)  
- `properties.datetime` — time of detection, creation, or event  
- `properties.kfm_domain` — indicator | protection | report | workflow | provenance | sample  
- `properties.ecosystem` — npm | maven | pypi | bun | github-actions (optional per domain)  

### **Assets**
- `assets.entity` — canonical JSON for the item  
- `assets.metadata` — DCAT 3 descriptor  
- `assets.provenance` — PROV-O lineage bundle  
- `assets.evidence` — redacted, synthetic, or zero-risk attachments  

### **Links**
- Parent Collection  
- Related items (indicator ↔ protection ↔ report ↔ workflow)  
- Upstream/downstream lineage nodes  

---

## 🗂️ 3. STAC Collection Requirements

Each category (indicator family, protection class, report family, workflow domain) has a STAC Collection with:

- `stac_version: "1.0.0"`  
- `type: "Collection"`  
- `extent.temporal.interval` — earliest → latest item timestamp  
- `keywords[]` — DCAT tags  
- `providers[]` — KFM Security Guild, tooling, ETL systems  
- `summaries.*` — indicator types, severities, ecosystems  

Collections serve as the **semantic grouping layer** for the STAC catalog.

---

## 🧾 4. Metadata Alignment (DCAT · JSON-LD · PROV-O)

Each STAC entity must include:

### **DCAT 3.0 Fields**
- `dct:title`  
- `dct:description`  
- `dct:license`  
- `dct:creator`  
- `dcat:keyword[]`  

### **JSON-LD Context**
Added for external cataloging + KG ingestion.

### **PROV-O**
Used for full lineage:

- `prov:wasGeneratedBy`  
- `prov:wasDerivedFrom`  
- `prov:used`  
- `prov:wasAttributedTo`  

This ensures full reproducibility and ethical accountability (FAIR+CARE).

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/stac/
├── 📄 README.md                # This file
├── 📦 collections/             # STAC Collection definitions for each entity family
├── 📄 items/                   # Individual STAC Items (one per UUID)
├── 🧾 metadata/                # DCAT + JSON-LD augmented metadata overlays
├── 🧪 validation/              # JSON Schema / SHACL validation rules for STAC entries
└── 🧷 samples/                 # Synthetic, safe example STAC Items for onboarding & CI tests
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Focus Mode v3 reads directly from the STAC catalog to:

- render entity timelines  
- build multi-ecosystem threat narratives  
- correlate reports, protections, and indicators  
- anchor Story Nodes to STAC Items  
- surface provenance-backed explanations  

Every Story Node links to:

- STAC Item ID  
- associated metadata  
- temporal footprint  
- provenance evidence bundle  

This yields a **complete semantic + temporal + structural** representation of Shai-Hulud 2.0 across the platform.

---

## 🧭 Version History

| Version | Date       | Summary                                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji-prefix directory added; governance/H3 upgrades; aligned with KFM-MDP v11.2.2.     |
| v10.4.0 | 2025-11-15 | Earlier STAC overview; pre-v11 architecture & metadata model.                                             |

---

<div align="center">

[📘 Docs Root](../../../../../../..) · [🧪 Pipelines](../../../../../pipelines) · [🌐 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

