---
title: "🧩 KFM v11 — Shai-Hulud 2.0 Signature Indicators (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x signature-governance model"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"

telemetry_ref: "../../../../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/supply-chain-defense-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "IOC-Signature-Catalog"
intent: "supply-chain-defense-signatures"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **Shai-Hulud 2.0 — Signature Indicators Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/README.md`

**Purpose:**  
Define all **file-based**, **regex-based**, and **structural** signature rules used in KFM to detect  
Shai-Hulud 2.0 infiltration within package ecosystems, CI/CD environments, and provenance chains.

**Scope:**  
npm · Maven · PyPI · Bun · GitHub Actions · provenance graphs  
</div>

---

## 🧬 1. Overview

Signatures represent **deterministic detection rules** for Shai-Hulud 2.0:

- File-level indicators  
- Pattern-based signatures (regex / YARA-style)  
- Structural signatures (tree patterns, provenance mismatches)  
- Dependency-graph signatures  
- Hash-based signals (bundles, loaders, embedded payloads)  

All signatures conform to the **KFM v11 Signature Specification**, ensuring they are deterministic,  
documented, versioned, and provenance-aligned.

---

## 🧱 2. Signature Types (v11 Standard)

### 1. **File Hash Signatures**
SHA256/SHA512 of known-malicious artifacts, including:

- Bun loader implants  
- Poisoned `postinstall` wrappers  
- Compromised GitHub workflow files  
- Modified `.npm/_npx/**` execution stubs  

### 2. **Regex / Pattern Signatures**
Heuristic but deterministic patterns, e.g.:

- Obfuscated lifecycle hook payloads  
- Encoded token collectors  
- Shadow-runner registration snippets  
- De-obfuscated Bun bootstrap logic  

### 3. **Structural Signatures**
Graph- or tree-based:

- Divergent dependency subtrees  
- Manifest-to-lockfile inconsistencies  
- SLSA mismatch in materials list  
- SBOM delta anomalies  

### 4. **Bundle-Level Signatures**
Multi-file or multi-artifact connections:

- Combined loader + workflow presence  
- Precursor files dropped in `/tmp/` or install cache  
- Auth token use across multiple ecosystems  

---

## 🧪 3. Signature Schema (KFM v11)

Each signature JSON follows:

- `id` — UUIDv4  
- `severity` — low/medium/high/critical  
- `match_type` — exact | regex | structural | composite  
- `signature` — hash, pattern, or structural rule  
- `scope` — npm | maven | pypi | bun | github-actions  
- `provenance` — PROV-O lineage  
- `first_seen` / `last_seen`  
- `source_tool` — scanner, analyzer, or pipeline  
- `mitigation` — recommended isolation or purge  

All signatures are **version-pinned** and **immutability-locked**.

---

## 📦 4. STAC Integration

Each signature is published as a **STAC Item** for discovery:

- `properties.datetime` = `first_seen`  
- `assets.rule` = signature JSON  
- `assets.evidence` = raw payload, redacted  
- `assets.provenance` = PROV-O lineage bundle  
- `assets.metadata` = DCAT-compatible descriptor  

This allows downstream detection pipelines to:

- query signature families  
- compare versions  
- attach timelines in Focus Mode  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/
├── 📄 README.md            # This file
├── 🧩 file-hashes/         # SHA256/SHA512 hash-based indicators
├── 🧪 patterns/            # Regex, YARA-style patterns, heuristic string rules
├── 🧬 structural/          # Dependency graph patterns, manifest drift rules
├── 🧾 metadata/            # DCAT + JSON-LD metadata for signature bundles
├── 📦 stac/                # STAC Items / Collections for signature definitions
└── 🧷 samples/             # Synthetic samples, safe reproductions, redacted payloads
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Each signature generates a **Story Node v3** entry with:

- A narrative describing the signature class  
- Example detection events  
- Relations to artifacts, pipelines, and actors  
- Temporal footprint (first-seen → last-seen)  
- Provenance references  

Focus Mode v3 uses signatures to:

- augment threat timelines  
- highlight upstream/downstream infection paths  
- generate deterministic, provenance-backed narratives  

---

## ♻️ 7. Version History

**v11.2.3 — 2025-11-29**  
• Created signature catalog README  
• Added STAC + DCAT metadata alignment  
• Added structural + composite signature definitions  
• Directory aligned to Emoji-Prefix Standard  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**  

[📘 Docs Root](../../../../../..) ·  
[🧪 Pipelines](../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

