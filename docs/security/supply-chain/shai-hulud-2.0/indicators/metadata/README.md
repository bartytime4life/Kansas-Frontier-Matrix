---
title: "🧾 KFM v11 — Shai-Hulud 2.0 Indicator Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/metadata/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x metadata-governance model"

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
doc_kind: "IOC-Metadata"
intent: "supply-chain-defense-indicator-metadata"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **Shai-Hulud 2.0 — Indicator Metadata Registry**
`docs/security/supply-chain/shai-hulud-2.0/indicators/metadata/README.md`

**Purpose:**  
Define canonical metadata requirements for all Shai-Hulud 2.0 indicator types  
(file-hash · pattern · YARA · structural · heuristic · composite), ensuring complete traceability,  
interoperability, and FAIR+CARE compliance.

**Scope:**  
DCAT 3 · STAC 1.0 · JSON-LD · PROV-O · Governance metadata  
</div>

---

## 🧬 1. Overview

This registry unifies **metadata rules** across all Shai-Hulud 2.0 indicator families.

All indicators must export metadata that is:

- **DCAT 3 compliant**  
- **STAC-publishable**  
- **JSON-LD structured**  
- **Provenance-linked via PROV-O**  
- **Machine-extractable**  
- **FAIR+CARE aligned**  
- **Versioned and immutable**  

This ensures:

- consistent ingestion  
- predictable cataloging  
- reproducible analytics  
- complete lineage & ethics tracking  
- seamless Focus Mode integration  

---

## 📦 2. Required Metadata Fields (KFM v11 Standard)

### **General Metadata**
- `id` — globally unique identifier  
- `title` — human-readable name  
- `description` — short summary  
- `indicator_type` — hash | regex | yara | structural | heuristic | composite  
- `ecosystem` — npm | maven | pypi | bun | github-actions  
- `severity` — low/medium/high/critical  
- `keywords[]` — DCAT-compatible  

### **Temporal Metadata**
- `first_seen`  
- `last_seen`  
- `last_updated`  
- `observation_window`  

### **Governance Metadata**
- `status` — Active | Suspended | Deprecated  
- `review_cycle`  
- `immutability_status` — version-pinned | frozen  
- `governance_ref` — policy anchor  

### **STAC Fields**
- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `properties.datetime`  
- `assets.signature`  
- `assets.metadata`  
- `assets.provenance`  

### **DCAT Fields**
- `dct:title`  
- `dct:description`  
- `dct:modified`  
- `dct:license`  
- `dct:creator`  
- `dcat:keyword[]`  

### **PROV-O Lineage**
- `prov:used`  
- `prov:wasGeneratedBy`  
- `prov:wasAttributedTo`  
- `prov:wasDerivedFrom`  

---

## 🧱 3. Metadata Profiles

### **1. DCAT 3 Profile**
Dataset-level metadata for indicator bundles.

### **2. STAC 1.0 Profile**
Item-level publication & asset linking.

### **3. PROV-O Profile**
Complete lineage chain (entity → activity → agent).

### **4. JSON-LD Context**
Machine interoperability for:

- RDF graphs  
- Neo4j KG ingestion  
- external catalogs (OGC/CKAN)  

---

## 🗂️ 4. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/metadata/
├── 📄 README.md            # This file
├── 🧾 dcat/                # DCAT 3.0 metadata files for each indicator
├── 📦 stac/                # STAC Collections / Items for indicator metadata
├── 🧬 prov/                # PROV-O lineage bundles for indicators
├── 🧠 jsonld/              # JSON-LD contexts for metadata expansion
└── 🧷 samples/             # Synthetic metadata payloads for CI and onboarding
~~~

---

## 🔍 5. Story Node & Focus Mode Integration

Metadata powers:

- Focus Mode’s narrative accuracy  
- Timeline placement using `first_seen`  
- Cross-indicator grouping via keywords  
- Latent relationship discovery in the KG  
- Provenance-backed storytelling  
- Extraction of semantic meaning from indicators  

Every indicator’s Story Node includes:

- `when.start` = `first_seen`  
- `narrative.body` = metadata-derived summary  
- `relations[]` = indicator → artifact → pipeline → event  
- STAC + PROV-O references  

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

