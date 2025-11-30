---
title: "🧷 KFM v11 — Shai-Hulud 2.0 Signature Samples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/samples/README.md"
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
doc_kind: "IOC-Signature-Samples"
intent: "supply-chain-defense-signature-samples"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧷 **Shai-Hulud 2.0 — Sample Signature Artifacts**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/samples/README.md`

**Purpose:**  
Provide **safe**, **sanitized**, and **synthetic** artifacts that mimic Shai-Hulud 2.0 indicators  
without containing harmful payloads—used for onboarding, CI testing, education, and signature verification.

**Scope:**  
Redacted payloads · synthetic samples · mock artifacts · benign replicas  
</div>

---

## 🧬 1. Overview

These samples are **non-malicious** and designed to:

- validate signature-matching engines  
- test STAC & DCAT metadata consumption  
- enable CI pipelines to exercise detection logic  
- support analyst training  
- provide reproducible, controlled examples for experiments  

Samples reflect the **structure**, **naming**, and **behavioral cues** of actual Shai-Hulud 2.0 artifacts  
but contain **no executable code**, **no sensitive content**, and **no live threat behaviors**.

---

## 🧱 2. Sample Categories

### **1. File-Hash Samples**
- Synthetic files with fixed SHA256/SHA512 signatures  
- Replicas of expected loader shapes  
- Benign buffers used to validate file-hash matching  

### **2. Regex / Pattern Matching Samples**
- Strings containing harmless analogs of known patterns  
- Escaped versions of high-risk markers  
- JSON/JS fixtures to exercise regex engines  

### **3. YARA-Style Sample Rules**
- Minimal, safe byte sequences  
- Context-only examples demonstrating rule boundaries  

### **4. Structural Graph Samples**
- Synthetic dependency DAGs  
- Manifest-vs-lockfile drift scenarios  
- Mock provenance chains exhibiting intended anomalies  

### **5. Composite Samples**
- Multi-file patterns replicating complex indicators  
- Fake loader + fake workflow combos  
- Metadata bundles that test correlation engines  

---

## 📦 3. STAC Integration

All samples generate **STAC Items** with:

- `properties.sample_type` — file-hash | regex | yara | structural | composite  
- `datetime` — sample creation timestamp  
- `assets.sample` — the synthetic artifact  
- `assets.metadata` — sample descriptor  
- `assets.provenance` — redacted lineage file  

This enables:

- validation of signature ingestion flow  
- CI testing of schema compliance  
- reproducibility of experiments  

---

## 🛡️ 4. Safety & Ethics Policies

All sample artifacts must:

- contain **zero executable code**  
- contain **no personally identifiable**, sensitive, or harmful content  
- avoid embedding offensive or inappropriate terms  
- be fully **redacted**, **synthetic**, or **generated** specifically for testing  
- pass KFM FAIR+CARE compliance checks  
- remain fully open-source and safe for distribution  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/samples/
├── 📄 README.md            # This file
├── 🧩 file-hash/           # Synthetic artifacts matching hash-based IoC structures
├── 🧪 pattern/             # Safe regex/YARA/heuristic pattern triggers
├── 🧬 structural/          # Mock dependency graphs, drift examples, DAG anomalies
├── 🧾 metadata/            # Sample DCAT/JSON-LD/PROV-O metadata bundles
├── 📦 stac/                # Sample STAC Items / Collections for validation
└── 🧷 misc/                # Miscellaneous safe fixtures used in CI or training
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Sample artifacts generate **Story Node v3** entries tagged `sample:true`  
to support:

- training-mode narrative overlays  
- demonstration of signature relationships  
- safe-focus testing for analysts  
- lineage-aware example trails  

Focus Mode v3 ensures these samples **never** appear as real threat indicators.

---

## ♻️ 7. Version History

**v11.2.3 — 2025-11-29**  
• Added synthetic sample catalog README  
• Established category taxonomy  
• Ensured strong FAIR+CARE + safety compliance  
• Directory layout aligned to Emoji-Prefix Standard  

---

<div align="center">

**🛡️ KFM Security · Safe · Deterministic · FAIR+CARE**  

[📘 Docs Root](../../../../../../..) ·  
[🧪 Pipelines](../../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

