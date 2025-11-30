---
title: "📑 KFM v11 — Shai-Hulud 2.0 Incident Reports & Threat Analysis (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/reports/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x report-governance model"

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
doc_kind: "Supply-Chain-Threat-Reports"
intent: "supply-chain-defense-reports"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📑 **Shai-Hulud 2.0 — Incident Reports & Threat Analysis**
`docs/security/supply-chain/shai-hulud-2.0/reports/README.md`

**Purpose:**  
Provide an authoritative archive of **incident reports**, **threat chronologies**,  
**postmortems**, **behavioral analyses**, and **cross-ecosystem intelligence**  
related to the Shai-Hulud 2.0 supply-chain worm.

**Scope:**  
Forensic analysis · IOC timelines · behavioral evolution · CI/CD impact · multi-ecosystem correlation  
</div>

---

## 🧬 1. Overview

This directory contains detailed **incident reports** that:

- document confirmed or suspected Shai-Hulud 2.0 intrusion attempts  
- reconstruct multi-registry attack chains  
- analyze cross-ecosystem propagation behavior  
- correlate file-hash, pattern, heuristic, and structural indicators  
- provide actionable recommendations for mitigation  
- integrate with SBOM deltas, runner logs, and workflow metadata  

All reports follow KFM’s documentation-first and FAIR+CARE principles.

---

## 🧱 2. Report Types

### **1. IOC-Oriented Reports**
Focus on IoC clusters such as:

- Bun-loader signatures  
- lifecycle hook contamination  
- shadow-runner footprints  
- poisoned artifacts  
- multi-stage bootstrap activity  

### **2. Provenance & Attestation Failures**
Reports reconstruct:

- SLSA lineage breaks  
- invalid or missing attestations  
- cross-build material inconsistencies  
- anomalous timestamp drift  

### **3. CI/CD Compromise Reports**
Investigate:

- runner registration anomalies  
- workflow template tampering  
- DAG reordering attempts  
- egress attempts during install/build  

### **4. Multi-Ecosystem Threat Correlation**
Correlation between attacks spanning:

- npm  
- Maven  
- PyPI  
- Bun  
- GitHub Actions / workflow-level injection  

### **5. Retrospective & Postmortem Reports**
Complete incident narratives documenting:

- root cause  
- timeline progression  
- indicators observed  
- protection mechanisms triggered  
- remediation & governance outcomes  

---

## 🧬 3. Report Schema (KFM v11)

Each report must include:

- `id` — UUIDv4  
- `title`  
- `summary`  
- `severity` — informational | warning | critical  
- `first_seen` / `last_seen`  
- `indicator_refs[]`  
- `provenance_refs[]`  
- `graph_relations[]` — affected artifacts, pipelines, runners  
- `analysis` — narrative timeline + technical breakdown  
- `recommendations` — remediation & prevention  
- `stac_item` — associated STAC Item(s)  
- `appendices` — diagrams / logs / redacted evidence  

Reports must be deterministic, reproducible, and fully ethics-aligned.

---

## 📦 4. STAC Integration

Each report produces:

### **STAC Item**
Containing:

- incident metadata  
- artifact evidence  
- indicator references  
- provenance bundles  
- narrative assets  

### **STAC Collection**
Grouping:

- IOC clusters  
- report families  
- severity classes  
- ecosystem categories  

This enables:

- timeline visualization  
- threat evolution analysis  
- cross-referencing with protection & signature layers  
- Focus Mode story generation  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/reports/
├── 📄 README.md            # This file
├── 📑 incidents/           # Individual incident reports (investigations, root-cause analyses)
├── 🧬 provenance/          # Provenance & attestation-focused case reports
├── 🧪 indicators/          # IOC cluster writeups (hash, pattern, structural, heuristic)
├── 🔧 workflows/           # Workflow tampering / runner-related investigation files
├── 🌐 ecosystems/          # Cross-registry multi-ecosystem correlation reports
└── 📦 stac/                # STAC Items / Collections for reports and evidence bundles
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Each report contributes **Story Node v3** entries that encode:

- root-cause narrative  
- time-anchored events  
- linked indicators & protections  
- provenance reasoning  
- cross-ecosystem threat patterns  

Focus Mode v3 uses reports to:

- generate high-fidelity threat stories  
- animate infection pathways  
- explain kill-switch activations  
- highlight systemic risk trends  
- correlate protections → indicators → outcomes  

---

## 🧭 Version History

| Version | Date       | Summary                                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji-prefix directory added; governance/H3 upgrades; aligned with KFM-MDP v11.2.2.     |
| v10.4.0 | 2025-11-15 | Earlier reports overview; pre-v11 metadata & STAC integration.                                             |

---

<div align="center">

[📘 Docs Root](../../../../../../..) · [🧪 Pipelines](../../../../../pipelines) · [🌐 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

