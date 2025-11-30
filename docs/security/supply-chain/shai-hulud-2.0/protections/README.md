---
title: "🛡️ KFM v11 — Shai-Hulud 2.0 Protections & Defensive Controls (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/shai-hulud-2.0/protections/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Guild · FAIR+CARE Council Oversight"
backward_compatibility: "Aligned with v10.x → v11.x protection-governance model"

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
doc_kind: "Supply-Chain-Protection"
intent: "supply-chain-defense-protections"
fair_category: "F1-A2-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🛡️ **Shai-Hulud 2.0 — KFM Defensive Controls & Protection Rules**
`docs/security/supply-chain/shai-hulud-2.0/protections/README.md`

**Purpose:**  
Define the **deterministic, CI-enforced, policy-governed protections** that shield the  
KFM ecosystem from Shai-Hulud 2.0 supply-chain compromise vectors.

**Scope:**  
Dependency governance · CI/CD controls · SBOM variance checks · provenance enforcement · runner hardening  
</div>

---

## 🧬 1. Overview

KFM’s Shai-Hulud 2.0 protection framework enforces **zero-trust**, **provenance-anchored**,  
**immutable** supply-chain security.

The goal is to **prevent**, **detect**, and **contain** multi-ecosystem compromise attempts  
targeting:

- npm · Maven · PyPI  
- Bun loader runtime  
- GitHub Actions  
- Workflow orchestration  
- Attestation & SBOM pipelines  

Protections apply at:

- **install-time**
- **build-time**
- **publish-time**
- **promotion-time**
- **graph-write-time**

Every rule is deterministic and reproducible.

---

## 🧱 2. Core Protection Principles (v11)

### **1. Lifecycle Script Elimination**
- Block all `preinstall`, `install`, `postinstall` hooks  
- CI fails instantly if lifecycle scripts are detected  
- Applies to npm, PyPI, and hybrid runtimes  

### **2. Dependency Freeze & Integrity Lock**
- Full version + SHA256 pinning  
- Deterministic lockfiles  
- Dependency promotions allowed only via signed review  

### **3. Immutable CI/CD Surfaces**
- Golden runner images  
- No dynamic container pulls  
- Strict runner registration policy  

### **4. SBOM Delta Enforcement**
- Per-build SBOM diffs  
- Any unexpected delta → pipeline kill-switch  
- Licensed only via KFM-approved SBOM schemas  

### **5. Provenance (SLSA v11) Requirements**
- Mandatory attestations  
- Required materials list hashing  
- Reject build artifacts with missing or mismatched SLSA fields  

### **6. Network Isolation**
- Zero outbound traffic during install  
- Allowed endpoints hardcoded  
- Exfil-attempt detection integrated with telemetry  

### **7. Workflow Integrity Controls**
- Signed workflow templates  
- Forbidden workflow triggers (e.g., `discussion.yaml`)  
- Promotion DAG validation  

---

## 🧬 3. Protection Control Schema (KFM v11)

Each protection rule is documented with:

- `id` — UUIDv4  
- `type` — lifecycle | dependency | provenance | workflow | runner | sbom | network  
- `severity` — low / medium / high / critical  
- `enforcement` — hard | soft | advisory  
- `scope` — npm | maven | pypi | bun | github-actions  
- `rationale` — why the control exists  
- `mitigation` — what CI does if violated  
- `provenance` — PROV-O lineage record  
- `telemetry_signals[]` — linked metrics or alerts  

All protections are version-pinned and immutable once promoted.

---

## 📦 4. STAC Integration

Protection rules are represented as **STAC Items**, enabling:

- discovery of control classes  
- temporal evolution of standards  
- linking protections with indicators and signatures  
- Focus Mode narrative anchoring  

STAC Items include:

- `properties.control_type`  
- `assets.rule` — JSON rule definition  
- `assets.provenance` — lineage bundle  
- `assets.metadata` — DCAT descriptor  

---

## 🗂️ 5. Directory Layout

~~~text
docs/security/supply-chain/shai-hulud-2.0/protections/
├── 📄 README.md            # This file
├── 🛡️ lifecycle/           # Lifecycle script ban & installer-safety controls
├── 🧬 dependencies/        # Dependency freeze, checksum, manifest-lock protections
├── 🧾 provenance/          # Provenance enforcement (SLSA, attestations, materials)
├── 🛠️ workflows/           # Workflow integrity, signature enforcement, DAG validation
├── 🧪 sbom/                # SBOM delta rules, drift detection, integrity checks
├── 🔒 runners/             # Runner verification, rotation policy, registration controls
├── 🌐 network/             # Network isolation, egress-block patterns, anomaly rules
└── 📦 stac/                # STAC Items/Collections describing protection rules
~~~

---

## 🔍 6. Story Node & Focus Mode Integration

Each protection rule generates a **Story Node v3**:

- captures protection logic  
- explains rule rationale  
- links protection → indicators → pipeline events  
- includes SLSA/PROV-O lineage  
- supports Focus Mode system-narrative integration  

Focus Mode uses protection rules to:

- justify CI/CD kill-switch decisions  
- construct defensible narratives  
- correlate protections with detected threats  
- visualize hardened points in the supply-chain graph  

---

## 🧭 Version History

| Version | Date       | Summary                                                                                                   |
|---------|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete rewrite; emoji-prefix directory added; governance/H3 upgrades; aligned with KFM-MDP v11.2.2.     |
| v10.4.0 | 2025-11-15 | Earlier protections overview; pre-v11 metadata structure.                                                  |

---

<div align="center">

[📘 Docs Root](../../../../../../..) · [🧪 Pipelines](../../../../../pipelines) · [🌐 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

