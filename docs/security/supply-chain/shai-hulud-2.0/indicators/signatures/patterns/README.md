---
title: "🧪 KFM v11 — Shai-Hulud 2.0 Pattern Signatures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/patterns/README.md"
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
doc_kind: "IOC-Pattern-Signatures"
intent: "supply-chain-defense-pattern-signatures"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧪 **Shai-Hulud 2.0 — Pattern Signature Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/patterns/README.md`

**Purpose:**  
Define the **regex**, **string-pattern**, **YARA-style**, and **heuristic pattern** signatures used to  
detect Shai-Hulud 2.0 compromise across ecosystems and CI/CD contexts.

**Scope:**  
npm · Maven · PyPI · Bun · GitHub Actions · provenance drift  
</div>

---

## 🧬 1. Overview

Pattern signatures detect **behavioral similarities** and **code-pattern fingerprints** found in  
Shai-Hulud 2.0 artifact families.

Key pattern categories:

- Lifecycle-hook obfuscation markers  
- Bun-loader bootstrap logic  
- Cross-ecosystem beacon calls  
- Token-exfiltration string fragments  
- Shadow-runner registration stubs  
- Encoded payload loaders  
- ESBuild/Bun-plugin mutation patterns  

All pattern signatures follow the **KFM v11 Indicator Schema** and include provenance, severity,  
temporal metadata, and mitigation recommendations.

---

## 🧱 2. Pattern Signature Types

### 1. **Regex Signatures (Deterministic)**
Identify exact structures, e.g.:

- Base64-encoded payload seeds  
- Suspicious function wrappers (`(()=>{...})()`)  
- Patterns around `child_process.exec()` combinations  
- Bun runtime detection (`globalThis[Bun.loader]`)  

### 2. **YARA-Style Rules**
Match syntactic + structural slices:

- Embedded credential-grabber functions  
- Minifier-induced repetition patterns  
- Polyglot JS/WASM bundles  
- Multi-stage dispatchers  

### 3. **Heuristic Patterns**
Non-regex structural cues:

- Unused import storms  
- Manifest-to-code inconsistencies  
- Exfil URLs hidden in charmaps  
- Token-collecting function triads  

### 4. **CI/CD Behavior Patterns**
Workflow-level or runner-level shims:

- Unauthorized self-hosted runner declarations  
- `.github/workflows/discussion.yaml` with nonstandard triggers  
- Obfuscated download → exec → cleanup chains  

---

## 🧬 3. Pattern Signature Schema (KFM v11)

Each pattern signature includes:

- `id` — UUIDv4  
- `severity` — low/medium/high/critical  
- `match_type` — regex | yara | heuristic  
- `pattern` — regex body / YARA rule / heuristic descriptor  
- `ecosystem` — npm | maven | pypi | bun | github-actions  
- `confidence` — numeric 0–1  
- `provenance` — discovery lineage via PROV-O  
- `first_seen` / `last_seen`  
- `mitigation` — recommended response  
- `evidence_assets[]` — redacted artifacts  

All patterns must be reproducible and peer-reviewed.

---

## 📦 4. STAC Integration

Each signature publishes as a **STAC Item** with:

- `properties.datetime` — first detection  
- `assets.pattern` — pattern JSON  
- `assets.provenance` — lineage bundle  
- `assets.metadata` — DCAT-compatible descriptor  

This allows pipelines to:

- query by ecosystem  
- correlate patterns with file-hash signatures  
- illuminate infection timelines via Focus Mode  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/patterns/
├── 📄 README.md            # This file
├── 🧪 regex/               # Regex-based signatures (deterministic, CI-safe)
├── 🧬 yara/                # YARA-style pattern rules
├── 🧠 heuristic/           # Non-regex heuristic pattern descriptors
├── 🧾 metadata/            # DCAT + JSON-LD metadata for pattern signatures
├── 📦 stac/                # STAC Items / Collections for pattern signatures
└── 🧷 samples/             # Redacted sample artifacts / synthetic pattern triggers
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Each pattern signature generates a **Story Node v3** containing:

- A narrative explanation of the pattern class  
- Example detection contexts  
- Linked artifacts, pipelines, and events  
- Temporal footprint of the signature  
- Provenance path to discovery  

Focus Mode v3 uses pattern signatures to:

- surface ecosystem-specific compromise trails  
- enrich threat timelines  
- link patterns with file-hash + structural indicators  
- generate deterministic explanations for analyst review  

---

## ♻️ 7. Version History

**v11.2.3 — 2025-11-29**  
• Added pattern signature README  
• Integrated regex/YARA/heuristic schema  
• Added STAC + DCAT metadata support  
• Directory layout aligned to Emoji-Prefix Standard  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**

[📘 Docs Root](../../../../../../..) ·  
[🧪 Pipelines](../../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

