---
title: "📊 KFM v11 — Shai-Hulud 2.0 Indicators & IOC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x defense profiles"

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
doc_kind: "Security Indicators Catalog"
intent: "supply-chain-defense-indicators"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📊 **Shai-Hulud 2.0 — KFM Indicators & IOC Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/README.md`

**Purpose:**  
Maintain KFM’s authoritative Indicators-of-Compromise (IOCs), behavioral signatures,  
heuristics, and forensic markers for detecting **Shai-Hulud 2.0** supply-chain infiltration attempts.

**Scope:**  
npm · Maven · PyPI · GitHub Actions · Bun loader · compromised runners · poisoned dependencies  
</div>

---

## 🚨 1. Indicator Categories (v11)

KFM tracks six classes of Shai-Hulud 2.0 indicators:

### 1. **File & Loader Artifacts**
- `setup_bun.js`, `bun_environment.js`, `bun_loader.js`  
- Suspicious ESBuild/Bun plugin bundles  
- Embedded obfuscated installer hooks  

### 2. **Metadata & Manifest Drift**
- Dependency manifest checksum mismatches  
- Mutated `package.json` install blocks  
- Version-pinning violations  
- Unexpected transitive graph expansion  

### 3. **Pipeline & Runner Artifacts**
- Unauthorized self-hosted runner registrations  
- Unrecognized GitHub Actions tokens  
- Shadow workflows (`discussion.yaml`, `maintenance.yaml`)  
- Lineage breaks in build provenance  

### 4. **Network & Exfiltration Patterns**
- Outbound traffic during install steps  
- Credential posting to unknown repos  
- Repeated POSTs to unregistered telemetry endpoints  

### 5. **Publication & Registry Events**
- Sudden republishing of high-trust libraries  
- Name-mirror Maven artifacts  
- Package takeover events  

### 6. **Graph & Provenance Variance**
- Missing SLSA attestations  
- Unexpected material hashes  
- Divergence between SBOM deltas and expected build graph  

---

## 🧪 2. IOC Bundles (KFM v11 Format)

KFM organizes indicators into structured IOC bundles for each ecosystem:

- `bun-loader.ioc.json`
- `npm-takeover.ioc.json`
- `maven-shadowline.ioc.json`
- `pypi-registry-diff.ioc.json`
- `runner-anomalies.ioc.json`
- `workflow-persistence.ioc.json`

Each IOC bundle includes:

- `id` — stable UUID  
- `category` — type of indicator  
- `severity` — low/medium/high/critical  
- `signature` — hash, pattern, or rule  
- `match_type` — exact | regex | heuristic | structural  
- `source` — tool, scanner, or analysis  
- `provenance` — links to raw evidence  
- `mitigation` — recommended action  

---

## 🧬 3. Provenance & STAC Integration

All IOC bundles publish STAC Items with:

- spatial footprint: N/A (non-geospatial)  
- temporal range: first-seen → last-seen  
- lineage: PROV-O record of discovery + validation  
- checksum: SHA256 or SHA512  
- asset roles: `evidence`, `signature`, `report`, `raw`  

This enables downstream systems to:

- query indicators by time or severity  
- validate lineage  
- integrate IOC signals into Focus Mode threat timelines  

---

## 🗂️ 4. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/
├── 📄 README.md                 # This file
├── 🧩 signatures/               # Indicator signatures (file-based, regex, structural)
├── 🧬 heuristics/               # Behavioral heuristics, environment checks, anomaly rules
├── 🧾 metadata/                 # DCAT/DCAT-AP + PROV-O metadata for each IOC bundle
├── 📦 stac/                     # STAC Items/Collections describing IOC bundles
└── 🧷 samples/                  # Sample IOC payloads, test artifacts, synthetic reproductions
~~~

---

## 🔍 5. Story Node & Focus Mode Integration

Focus Mode v3 uses these indicators for:

- Timeline overlays of detection events  
- Linking indicators to infected pipelines  
- Narrative insights explaining root causes  
- Graph traversal from IOC → artifact → pipeline → commit  

Each IOC produces a **Story Node v3** entry with:

- `when.start` = detection time  
- `title` = indicator class  
- `narrative.body` = concise explanation  
- `relations[]` = linked artifacts, events, and actors  

---

## ♻️ 6. Version History

**v11.2.3 — 2025-11-29**  
• Initial Indicators README for Shai-Hulud 2.0  
• Directory layout aligned to Emoji-Prefix Standard  
• Added IOC bundle structure + STAC integration  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**

[📘 Docs Root](../../../../..) · [🧪 Pipelines](../../../../../pipelines) ·  
[🌐 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

