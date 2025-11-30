---
title: "🧾 KFM v11 — Shai-Hulud 2.0 Signature Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/metadata/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x metadata-governance model"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
signature_ref: "../../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.3/slsa-attestation.json"

telemetry_ref: "../../../../../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/supply-chain-defense-v11.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "IOC-Signature-Metadata"
intent: "supply-chain-defense-signature-metadata"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **Shai-Hulud 2.0 — Signature Metadata Registry**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/metadata/README.md`

**Purpose:**  
Define the authoritative **metadata layer** for all signature types  
(file-hashes · regex/pattern · YARA · structural · composite)  
governing traceability, discovery, interoperability, and provenance of Shai-Hulud 2.0 indicators.

**Scope:**  
STAC · DCAT · PROV-O · JSON-LD · CKAN/OGC-aligned metadata profiles  
</div>

---

## 🧬 1. Overview

This registry provides **uniform metadata specifications** for all Shai-Hulud 2.0 signature bundles.

Each signature—regardless of type—must publish metadata that is:

- **DCAT-compatible**  
- **STAC-publishable**  
- **JSON-LD structured**  
- **Provenance-rich (PROV-O)**  
- **FAIR+CARE aligned**  
- **Versioned & immutable**  

Metadata is the connective tissue enabling:

- lineage reconstruction  
- indicator validation  
- cross-ecosystem signature correlation  
- Focus Mode narrative grounding  
- reproducible threat analytics  

---

## 📦 2. Required Metadata Fields (KFM v11)

All signature bundles must include:

### **General Metadata**
- `id` — stable UUID  
- `title` — signature name  
- `description` — concise functional description  
- `ecosystem` — npm | maven | pypi | bun | github-actions  
- `severity` — low/medium/high/critical  
- `signature_type` — file-hash | regex | yara | structural | composite  

### **Temporal Metadata**
- `first_seen`  
- `last_seen`  
- `last_updated`  
- `observation_window`  

### **Lineage (PROV-O)**
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasDerivedFrom`  
- `prov:wasAttributedTo`  

### **STAC Fields**
- `stac_version`  
- `bbox` (optional for non-geospatial items)  
- `datetime`  
- `assets` (signature rule, metadata, provenance bundle)  

### **DCAT Fields**
- `dct:title`  
- `dct:description`  
- `dct:license`  
- `dct:creator`  
- `dct:issued`  
- `dct:modified`  
- `dcat:keyword[]`  

### **Governance**
- `status` — Active / Suspended / Deprecated  
- `review_cycle` — policy-driven  
- `immutability_status` — version-pinned | frozen  
- `governance_ref` — link to ROOT governance  

---

## 🧱 3. Metadata Profiles

### **1. DCAT 3.0 Profile**
Used for dataset-level description of signature bundles.

### **2. STAC 1.0 Profile**
Used for item-level representation & asset publication.

### **3. PROV-O Profile**
Tracks complete lineage, including:

- ingestion source  
- tooling pipeline  
- validation steps  
- evidence artifacts  

### **4. JSON-LD Context**
Ensures all metadata is machine-readable and exportable to:

- RDF  
- Graph DB  
- CKAN  
- OGC-compliant catalogs  

---

## 🗂️ 4. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/metadata/
├── 📄 README.md            # This file
├── 🧾 dcat/                # DCAT 3.0 metadata objects for signature bundles
├── 📦 stac/                # STAC Items / Collections (metadata layer only)
├── 🧬 prov/                # PROV-O lineage bundles (entity/activity/agent chains)
├── 🧠 jsonld/              # JSON-LD contexts and metadata expansion frames
└── 🧷 samples/             # Sample metadata payloads for onboarding & CI tests
~~~

---

## 🔍 5. Story Node & Focus Mode Integration

Metadata is required for **narrative extraction and explainability**.

Focus Mode v3 integrates metadata into:

- timeline placement (via `datetime`, `first_seen`)  
- narrative justification (via PROV-O lineage)  
- signature grouping (via DCAT keywords & ecosystem tags)  
- cross-linking signatures with artifacts, pipelines, and events  

Story Nodes associated with signatures embed:

- `when.start` = `first_seen`  
- `narrative.body` = metadata-driven summary  
- `relations[]` = references to rule assets, evidence, and upstream/downstream entities  

---

## ♻️ 6. Version History

**v11.2.3 — 2025-11-29**  
• Added metadata registry README  
• Integrated DCAT + STAC + PROV-O roles  
• Added JSON-LD context directory  
• Directory layout aligned to Emoji-Prefix Standard  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**  

[📘 Docs Root](../../../../../../..) ·  
[🧪 Pipelines](../../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

