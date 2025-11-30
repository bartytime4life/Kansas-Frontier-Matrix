---
title: "🧬 KFM v11 — Shai-Hulud 2.0 Structural Signatures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/structural/README.md"
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
doc_kind: "IOC-Structural-Signatures"
intent: "supply-chain-defense-structural-signatures"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Shai-Hulud 2.0 — Structural Signature Catalog**
`docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/structural/README.md`

**Purpose:**  
Define the **graph-based**, **tree-based**, **manifest-based**, and **provenance-based** structural  
signatures used to detect Shai-Hulud 2.0 infiltration across ecosystems and CI/CD systems.

**Scope:**  
Dependency graph drift · manifest inconsistencies · SBOM deltas · provenance mismatch · CI/CD structural anomalies  
</div>

---

## 🧠 1. Overview

Structural signatures detect compromise by analyzing **relationships** and **structural deviations** rather  
than file content or specific byte sequences.

These signatures catch advanced variants of Shai-Hulud 2.0 that mutate payloads but preserve  
malicious *structure*, including:

- Dependency shortcutting and bypass edges  
- Manifest-to-lockfile divergence  
- Provenance lineage breaks  
- Dependency tree expansion anomalies  
- Build-time pipeline mutations  
- SLSA material-list mismatch  
- SBOM delta inconsistencies across builds  

Structural signatures are among the **most reliable** detectors for polymorphic worm variants.

---

## 🧱 2. Structural Signature Types

### 1. **Dependency Graph Anomalies**
- Unexpected nodes added during install  
- Disallowed degree increases in leaf dependencies  
- Cyclic dependency reintroductions  
- Manifest-vs-lockfile inconsistency patterns  

### 2. **Provenance Chain Breaks**
- Missing or altered SLSA materials  
- Absent builder claims (`builder.id`)  
- Lineage inconsistencies between build steps  
- Material hash divergence from expected SBOM  

### 3. **CI/CD Structural Mutations**
- Shadow workflows injected into branch promotion pipelines  
- Unauthorized runner chain-of-trust alterations  
- Build-step reordering (e.g., install → test → build inversion)  
- Synthetic workflow dispatch injections  

### 4. **Cross-Ecosystem Structural Correlation**
- npm + Maven dual-tree contamination  
- PyPI + Bun loader layering patterns  
- Multi-registry propagation with consistent DAG anomalies  

---

## 🧬 3. Structural Signature Schema (KFM v11)

Each structural signature includes:

- `id` — UUIDv4  
- `severity` — low/medium/high/critical  
- `match_type` — structural  
- `structure` — graph spec, tree spec, or DAG rule  
- `ecosystem` — npm | maven | pypi | bun | github-actions  
- `first_seen` / `last_seen`  
- `confidence` — numeric 0–1  
- `provenance` — PROV-O lineage  
- `mitigation` — corrective action (rebuild, revert, isolate)  
- `evidence_assets[]` — diagrams, deltas, redacted materials  

These signatures are **deterministic**, **version-pinned**, and **review-enforced**.

---

## 📦 4. STAC Integration

Each structural signature is published as a **STAC Item**:

- `properties.datetime` — detection timestamp  
- `properties.ecosystem` — affected ecosystem  
- `assets.structure` — JSON signature rule  
- `assets.provenance` — PROV-O lineage  
- `assets.metadata` — DCAT metadata  

Supports:

- structural search  
- lineage integrity comparison  
- Focus Mode threat-timeline integration  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/structural/
├── 📄 README.md            # This file
├── 🧬 graphs/              # Dependency/DAG signatures (tree, graph, lineage rules)
├── 🧱 manifest-drift/      # Manifest → lockfile divergence signatures
├── 🧾 metadata/            # DCAT + JSON-LD metadata for structural signatures
├── 📦 stac/                # STAC Items / Collections for structural IoCs
└── 🧷 samples/             # Safe synthetic DAGs, example graph diffs, redacted evidence
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Structural signatures produce **Story Node v3** entries that describe:

- The structural anomaly class  
- Graph evidence and lineage breakpoints  
- Affected pipelines and ecosystems  
- First detection → timeline evolution  
- Relationships to related IoCs (hash or pattern)  

Focus Mode v3 uses structural signatures to:

- overlay infection pathways  
- correlate structural drift with artifact infection  
- explain provenance inconsistencies using deterministic logic  

---

## ♻️ 7. Version History

**v11.2.3 — 2025-11-29**  
• Added structural signature catalog  
• Integrated provenance + SBOM-delta patterns  
• Added ecosystem-crossing DAG signatures  
• Directory layout aligned to Emoji-Prefix Standard  

---

<div align="center">

**🛡️ KFM Security · Deterministic · FAIR+CARE**

[📘 Docs Root](../../../../../../..) ·  
[🧪 Pipelines](../../../../../../../pipelines) ·  
[🌐 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

