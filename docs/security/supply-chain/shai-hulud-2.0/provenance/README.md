---
title: "🧬 KFM v11 — Shai-Hulud 2.0 Provenance Enforcement & Lineage Controls (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/provenance/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x provenance-governance model"

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
doc_kind: "Supply-Chain-Provenance"
intent: "supply-chain-defense-provenance-controls"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Shai-Hulud 2.0 — Provenance Enforcement & Lineage Controls**
`docs/security/supply-chain/shai-hulud-2.0/provenance/README.md`

**Purpose:**  
Define the **lineage, attestation, and provenance controls** required to validate, authenticate,  
and chain-verify all artifacts in the KFM supply-chain, ensuring immunity to Shai-Hulud 2.0  
provenance-spoofing and tampering attacks.

**Scope:**  
SLSA v11 · PROV-O · attestation bundles · lineage graphs · SBOM+materials enforcement  
</div>

---

## 🧬 1. Overview

Provenance enforcement is the **first and last line of defense** against Shai-Hulud 2.0.  
The worm’s most powerful evasion vectors rely on:

- forged provenance  
- missing attestations  
- tampered materials lists  
- inconsistent build step lineage  
- shadow-runner provenance breakpoints

KFM v11 mandates **deterministic, verifiable, chain-linked provenance** for all packages, workflows,  
artifacts, and build graph elements.

---

## 🧱 2. Provenance Enforcement Principles (v11)

### **1. Attestation Required for All Artifacts**
- SLSA v11 attestation mandatory  
- Missing or invalid attestation ⇒ hard fail  
- Materials list checks required  

### **2. Lineage Chain Integrity**
- `prov:used` and `prov:wasGeneratedBy` must resolve to valid entities  
- Lineage gaps forbidden  
- Rerun detection flags unexpected build deltas  

### **3. Material Hash Consistency**
- Hash mismatch → kill-switch  
- Redundant hashing across build environment required  
- Multi-source correlation mandatory  

### **4. Runner & Workflow Provenance**
- Actions must publish build provenance  
- Unauthorized runner provenance invalid by default  
- Workflow-level provenance validated via signed templates  

### **5. Temporal Provenance**
- Build timestamps must align with commit DAG  
- Unexpected drift → block and notify  
- Requires time-consistency within <2s tolerance  

### **6. Cross-Ecosystem Provenance Coherence**
- npm ↔ Maven ↔ PyPI ↔ Bun cross-checks  
- Divergent materials list → immediate quarantine  
- Multi-registry provenance mismatch detection  

---

## 🧬 3. Provenance Schema (KFM v11)

Each provenance bundle includes:

- `id` — UUIDv4  
- `source_artifact`  
- `builder.id`  
- `invocation.configSource`  
- `materials[]` — hashed list  
- `slsa_level`  
- `provenance_chain[]` — PROV-O relations  
- `first_seen` / `last_seen`  
- `attestation_assets[]`  
- `verdict` — pass | fail | questionable  

Bundles must be:

- machine-validated  
- version-pinned  
- redacted for sensitive data  
- fully compliant with SLSA v11  

---

## 📦 4. STAC Integration

All provenance bundles publish as **STAC Items**, enabling:

- lineage navigation  
- temporal provenance timelines  
- signature → artifact → pipeline correlation  
- Focus Mode narrative integration  

STAC Item assets include:

- `assets.provenance` — provenance JSON  
- `assets.attestation` — SLSA proof bundle  
- `assets.metadata` — DCAT overlay  
- `assets.diff` — optional lineage delta  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/provenance/
├── 📄 README.md            # This file
├── 🧬 attestation/         # SLSA v11 attestations, redacted proof bundles
├── 🧾 metadata/            # DCAT + PROV-O metadata overlays
├── 📦 stac/                # STAC Items / Collections describing provenance bundles
├── 🔎 lineage/             # PROV-O lineage graphs, diff outputs, integrity checks
└── 🧷 samples/             # Synthetic provenance examples for CI and onboarding
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Provenance bundles produce **Story Node v3** entities describing:

- how the artifact was created  
- who/what generated it (builder, workflow, runner)  
- whether the lineage is consistent  
- how it correlates with Shai-Hulud 2.0 indicators  
- temporal evidence from attestation timestamps  

Focus Mode v3 uses provenance to:

- highlight supply-chain anomalies  
- differentiate benign vs compromised artifacts  
- explain kill-switch activations  
- generate deterministic, verified narratives  

---

## 🧭 Version History

| Version | Date       | Summary                                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji-prefix directory added; governance/H3 upgrades; aligned with KFM-MDP v11.2.2.     |
| v10.4.0 | 2025-11-15 | Earlier provenance overview; pre-v11 metadata structure.                                                   |

---

<div align="center">

[📘 Docs Root](../../../../../../..) · [🧪 Pipelines](../../../../../pipelines) · [🌐 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

