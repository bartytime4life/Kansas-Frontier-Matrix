---
title: "🧩 KFM v11 — Shai-Hulud 2.0 File-Hash Signatures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/file-hashes/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x signature-governance model"

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
doc_kind: "IOC-FileHash-Signatures"
intent: "supply-chain-defense-file-hash-signatures"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **Shai-Hulud 2.0 — File Hash Signature Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/file-hashes/README.md`

**Purpose:**  
Define the authoritative **hash-based IoCs** (SHA256/SHA512) used to detect  
Shai-Hulud 2.0 loader implants, poisoned libraries, malicious workflow files, and cross-ecosystem payloads.

**Scope:**  
npm · Maven · PyPI · Bun · GitHub Actions · Provenance artifacts  
</div>

---

## 🧬 1. Overview

File-hash signatures provide **deterministic** identification of Shai-Hulud 2.0 artifacts.  
These represent the most stable, least ambiguous indicators KFM uses to identify worm components.

Hash-level IoCs include:

- Bun loader bootstrap implants  
- Lifecycle-script droppers  
- Modified GitHub workflow dispatch files  
- Token-exfiltration stagers  
- Cross-language polyglot bundles  
- Compromised `node_modules`/`dist/` artifacts  

Each hash signature is:

- **Version-pinned**  
- **Immutability-locked**  
- **Provenance-backed**  
- **Cataloged in STAC + DCAT**  

---

## 🧱 2. Signature Structure (KFM v11 Schema)

Each file-hash signature conforms to the KFM v11 IOC schema:

- `id` — stable UUID  
- `severity` — low/medium/high/critical  
- `hash_type` — sha256 | sha512  
- `value` — hex-encoded hash  
- `origin` — ingestion pipeline, scanner, or intelligence feed  
- `first_seen` / `last_seen`  
- `ecosystem` — npm | maven | pypi | bun | github-actions  
- `provenance` — PROV-O lineage of how the hash was discovered  
- `mitigation` — quarantine / pipeline-purge / key rotation  
- `evidence_assets[]` — raw, redacted files  

Hashes are **never** to be included in plaintext form here unless redacted or synthetic.

---

## 🔐 3. File Categories

Shai-Hulud 2.0 file hashes are grouped into:

### **1. Bun Loader Payloads**
- `setup_bun.js` variants  
- Polyglot JS/TS → WASM loader stubs  
- Shadow runtime initializers  

### **2. Lifecycle Hook Droppers**
- Tainted `preinstall` / `postinstall` wrappers  
- Shellcode-bearing JS fragments  
- Minified exfil-call payloads  

### **3. Maven Poisoned Artifacts**
- Name-mirror shadow JARs  
- Build-time bytecode inserters  

### **4. GitHub Workflow Implants**
- Fake `.github/workflows/discussion.yaml`  
- Rogue runner registration payloads  

### **5. Trans-ecosystem Worm Bundles**
- Combined loader packages  
- Bundled obfuscation layers  
- Metadata-manipulation artifacts  

---

## 📦 4. STAC Integration

Each file-hash signature publishes as a **STAC Item** with:

- `properties.datetime` = detection timestamp  
- `properties.ecosystem` = target ecosystem  
- `assets.signature` = signature JSON  
- `assets.evidence` = redacted artifact  
- `assets.provenance` = lineage bundle  

This allows KFM systems to:

- search by ecosystem  
- correlate with SBOM deltas  
- integrate signatures into Focus Mode threat timelines  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/file-hashes/
├── 📄 README.md            # This file
├── 🧪 sha256/              # SHA256 signature bundles (KFM v11 IOC schema)
├── 🧬 sha512/              # SHA512 signature bundles with extended provenance
├── 🧾 metadata/            # DCAT + JSON-LD metadata for file-hash signatures
├── 📦 stac/                # STAC Items / Collections for file-hash IoCs
└── 🧷 samples/             # Safe synthetic artifacts / redacted evidence samples
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Each hash signature generates a **Story Node v3** with:

- Title = signature class  
- Narrative = explanation of detection context  
- Relations = affected artifacts, pipelines, and events  
- Temporal anchors = first_seen → last_seen  
- Provenance links = ingestion source, evidence bundles  

Focus Mode v3 uses file-hash signatures to:

- render threat timelines  
- identify upstream/downstream compromise paths  
- annotate infected pipelines with deterministic evidence  

---

## ♻️ 7. Version History

**v11.2.3 — 2025-11-29**  
• Initial file-hash signature catalog  
• STAC + DCAT integration  
• Directory aligned to Emoji-Prefix Standard  
• Structural alignment to KFM v11 IOC schema  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**

[📘 Docs Root](../../../../../../..) ·  
[🧪 Pipelines](../../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

