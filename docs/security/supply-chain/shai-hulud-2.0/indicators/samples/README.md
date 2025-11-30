---
title: "🧷 KFM v11 — Shai-Hulud 2.0 Indicator Samples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/samples/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x indicator-sample model"

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
doc_kind: "IOC-Sample-Registry"
intent: "supply-chain-defense-sample-indicators"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧷 **Shai-Hulud 2.0 — Indicator Sample Registry**
`docs/security/supply-chain/shai-hulud-2.0/indicators/samples/README.md`

**Purpose:**  
Provide a controlled, safe, synthetic environment to test, validate, and train against  
Shai-Hulud 2.0 detection signatures without exposing analysts, systems, or pipelines to harm.

**Scope:**  
Synthetic indicators · redacted assets · benign replicas · STAC sample items  
</div>

---

## 🧬 1. Overview

These samples are **non-malicious**, **fully synthetic**, and **sanitized** to mimic the *structure* and  
*behavioral shape* of real Shai-Hulud 2.0 indicators, without containing executable payloads,  
sensitive content, or harmful logic.

They enable:

- CI pipeline validation  
- analyst training  
- STAC ingestion testing  
- signature engine evaluation  
- safe reproduction of detection scenarios  

All samples are **FAIR+CARE-compliant** and follow KFM’s strict redaction policy.

---

## 🧱 2. Sample Categories

### **1. File-Hash Indicator Samples**
- Benign files with pre-generated SHA256/SHA512 values  
- Simulated loader file structures  
- Safe test blobs for hash-signature verification  

### **2. Pattern / Regex / YARA Samples**
- Harmless strings mimicking risky patterns  
- Escaped and neutralized versions of known IoCs  
- Test fixtures for pattern-matching engines  

### **3. Structural Samples**
- Fake dependency DAGs  
- Mock manifest drift scenarios  
- Synthetic provenance-break examples  
- Example SBOM delta cases  

### **4. Heuristic Samples**
- Simulated anomalous behavior sequences  
- Timing-pattern examples  
- Synthetic provenance drift bundles  

### **5. Composite Samples**
- Multi-file scenarios combining multiple sample types  
- Demonstrations of cross-ecosystem anomaly clustering  
- Controlled test cases for end-to-end signal correlation  

---

## 📦 3. STAC Integration

Every sample publishes a **STAC Item** with:

- `properties.sample_type`  
- `datetime`  
- `assets.sample` — synthetic test artifact  
- `assets.metadata` — DCAT metadata block  
- `assets.provenance` — redacted lineage bundle  
- `assets.structure` — (optional) structural graph or DAG example  

This ensures:

- deterministic CI reproducibility  
- seamless ingestion for tests  
- safe cross-environment replication  

---

## 🛡️ 4. Safety Rules

All samples MUST:

- contain **no executable content**  
- avoid any harmful or inappropriate payloads  
- be synthetic, redacted, or procedurally generated  
- pass FAIR+CARE screening  
- embed only safe strings and mock structures  
- include metadata indicating **sample:true**  

Under no circumstances may a real malware fragment be placed in this directory.

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/samples/
├── 📄 README.md            # This file
├── 🧩 file-hash/           # Benign artifacts with static known-test hash values
├── 🧪 pattern/             # Safe pattern / regex / YARA / heuristic triggers
├── 🧬 structural/          # Synthetic DAGs, SBOM deltas, provenance-break scenarios
├── 🧠 heuristic/           # Behavior-based sample indicators
├── 📦 stac/                # STAC Item examples for sample indicators
└── 🧾 metadata/            # Sample DCAT + JSON-LD metadata payloads
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Sample indicators generate **Story Node v3** entries with:

- `sample: true` metadata  
- narrative explanation of purpose  
- safe relations to synthetic events & artifacts  
- provenance-chain demonstrations  
- non-production scope markers  

Focus Mode v3 uses these only in:

- training  
- demonstrations  
- tutorials  
- system validation  

They are **never** surfaced as real threat data.

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

