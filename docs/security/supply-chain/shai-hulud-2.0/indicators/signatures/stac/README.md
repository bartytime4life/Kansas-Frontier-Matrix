---
title: "📦 KFM v11 — Shai-Hulud 2.0 STAC Signature Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/stac/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x STAC-governance model"

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
doc_kind: "IOC-STAC-Signatures"
intent: "supply-chain-defense-stac-signatures"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📦 **Shai-Hulud 2.0 — STAC Signature Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/stac/README.md`

**Purpose:**  
Define the **STAC Item / STAC Collection** structures for all Shai-Hulud 2.0 signature types  
(file-hash, pattern, regex, YARA, structural, composite), enabling standardized publication,  
cataloging, discovery, validation, and lineage-driven threat analysis across KFM.

**Scope:**  
STAC 1.0.0 · OGC API Records · DCAT 3.0 · JSON-LD · PROV-O  
</div>

---

## 🧬 1. Overview

The STAC catalog is the **canonical machine-readable registry** of all Shai-Hulud 2.0 detection signatures.

Every signature is published as:

- **STAC Item** — atomic signature instance  
- **STAC Collection** — logical grouping by type, ecosystem, or family  

STAC provides:

- uniform metadata structure  
- predictable discovery  
- schema validation  
- provenance linkability  
- integrability with KFM pipelines, Focus Mode, and security analytics  

---

## 🧱 2. STAC Item Requirements (KFM v11 Profile)

All signature STAC Items **must include**:

### **Core Fields**
- `stac_version: "1.0.0"`  
- `type: "Feature"`  
- `id` — stable UUID  
- `geometry: null` (non-geospatial)  
- `bbox: []` or omitted  
- `properties.datetime` — detection timestamp  
- `properties.signature_type` — hash | regex | yara | structural | composite  
- `properties.ecosystem` — npm | maven | pypi | bun | github-actions  

### **Assets**
- `assets.signature` — signature JSON file  
- `assets.provenance` — PROV-O lineage bundle  
- `assets.metadata` — DCAT metadata  
- `assets.evidence` — redacted artifact or structural diagram  

### **Links**
- `links[]` to Collection, related signatures, related indicators, or upstream datasets  

---

## 📚 3. STAC Collection Requirements (KFM v11 Profile)

Each signature family (hash, pattern, structural, composite) publishes one **STAC Collection**.

Collections must include:

- `type: "Collection"`  
- `stac_version: "1.0.0"`  
- `license: "MIT"`  
- `extent.temporal.interval` — from earliest `first_seen` to latest `last_seen`  
- `keywords[]` — DCAT-compatible  
- `providers[]` — toolchains, scanners, or maintainers  
- `summaries.signature_type[]`  
- `summaries.severity[]`  
- `summaries.ecosystem[]`  

---

## 🔗 4. PROV-O Integration

Every STAC Item links to a PROV-O lineage bundle:

- `prov:used` → discovery tools  
- `prov:wasGeneratedBy` → pipeline or analyst validation  
- `prov:wasDerivedFrom` → raw artifacts  
- `prov:wasAttributedTo` → KFM security guild agent identity  

This ensures metadata:

- reproducibility  
- transparency  
- auditability  
- ethical correctness (FAIR+CARE)  

---

## 📦 5. Catalog Organization

The STAC directory is organized into:

- **Collections** — `collections/*.json`  
- **Items** — `items/<signature-id>.json`  
- **Indices** — `catalog.json`, `collection-index.json`  
- **Metadata profiles**  
- **Validation schemas**  

All STAC JSON files must validate with:

- KFM STAC v11 Profile  
- STAC 1.0 schema  
- JSON-LD frames  
- DCAT mapping  

---

## 🗂️ 6. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/stac/
├── 📄 README.md                # This file
├── 📦 collections/             # STAC Collection definitions (one per signature family)
├── 📄 items/                   # Individual STAC Items for each signature UUID
├── 🧾 metadata/                # DCAT + JSON-LD overlays for STAC records
├── 🧪 validation/              # JSON Schema / SHACL validation rules for signatures
└── 🧷 samples/                 # Sample STAC Items & Collections for onboarding
~~~

---

## 🔍 7. Story Node & Focus Mode Integration

Focus Mode v3 uses the STAC catalog to:

- retrieve signature timelines  
- correlate signature activity with infected pipelines  
- enrich narrative generation with provenance-linked evidence  
- anchor Story Nodes’ temporal and structural metadata  
- provide explainable threat trajectories  

Each signature-origin Story Node references:

- STAC Item ID  
- `properties.datetime`  
- provenance links  
- associated assets  

---

## ♻️ 8. Version History

**v11.2.3 — 2025-11-29**  
• Added STAC signature catalog README  
• Integrated DCAT 3.0 + PROV-O fields  
• Added Collection + Item requirements  
• Directory layout aligned with Emoji-Prefix Standard  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**  

[📘 Docs Root](../../../../../../..) ·  
[🧪 Pipelines](../../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

