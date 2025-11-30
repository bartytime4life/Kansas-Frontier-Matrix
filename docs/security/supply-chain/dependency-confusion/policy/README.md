---
title: "🛡️ KFM v11.2.2 — Dependency-Confusion Defense Policy (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Supply-Chain Security · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
doc_kind: "Policy"
---

<div align="center">

# 🛡️ **KFM v11.2.2 — Dependency-Confusion Defense Policy**  
`docs/security/supply-chain/dependency-confusion/policy/README.md`

**Purpose:**  
Define the *formal, enforceable security controls* that protect the Kansas Frontier Matrix supply-chain  
from dependency-confusion attacks across all languages, registries, CI/CD environments, and pipeline layers.  
This policy is Diamond⁹ Ω / Crown∞Ω certified and enforced continuously by KFM-CI.

</div>

---

## 📘 Overview

Dependency-confusion (a.k.a. namespace shadowing) occurs when a rogue public-registry package  
overrides or supersedes an internal/private dependency by exploiting version precedence rules or  
unqualified namespace resolution.

KFM v11.2.2 enforces multilayer protection that combines:

- **Deterministic package pinning** (PyPI, NPM, Cargo, NuGet, Maven, RubyGems)  
- **Registry isolation + allow-listing**  
- **Artifact provenance attestation (SLSA-Level ≥ 3)**  
- **SBOM-driven build sealing**  
- **Namespace collision scanning**  
- **CI/CD isolation + sandboxing**  
- **Automatic diff-monitoring of upstream names**  

All supply-chain defenses must remain deterministic, reproducible, SBOM-aligned, and FAIR+CARE compliant.

---

## 🧱 Security Requirements (Enforced)

### 1. 📦 Deterministic Dependency Pinning
All packages MUST be pinned to:

- Exact version  
- Exact registry  
- Exact hash (pip/poetry hash-mode, npm `integrity`, cargo `checksum`, etc.)

**No unbounded (`*`, `>`, `^`, `~`) version specifiers** are allowed.

### 2. 🧰 Registry Isolation & Allow-Lists
KFM uses strict registry policies:

- PyPI → internal mirror only  
- NPM → `npm.pkg.github.com` scoped packages only  
- Cargo → `source = "kfm-internal"` unless explicitly allowed  
- Maven → `kfm-mirror` only  

**Public registries are blocked** unless explicitly added via governance override.

### 3. 🔐 SLSA + Provenance Enforcement
Every dependency MUST include:

- SLSA attestation (≥ Level 3)  
- SBOM inclusion  
- Immutable tamper-proof metadata  

### 4. 🛰️ Namespace Collision Scanning
Automated KFM-CI jobs:

- Scan all public registries for name collisions  
- Seal vulnerable namespace ranges  
- Auto-file a **Security Block Declaration (SBD)**  

### 5. 🧪 CI/CD Isolation & Sandboxed Builds
Builds MUST:

- Execute in hermetic, sandboxed environments  
- Have zero outbound Internet access  
- Rely exclusively on pinned, mirrored artifacts  

### 6. 📝 Governance & Incident Response
If any namespace conflict emerges:

1. CI blocks merge  
2. Security Council notified  
3. SBD filed  
4. Incident logged in `docs/security/incidents/YYYY/`  
5. Package quarantined until review  
6. Attacker packages permanently added to blacklist  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 policy/
    ├── 📄 README.md              # This file — formal KFM v11.2.2 policy
    ├── 📄 rules.md               # Detailed enforcement rules
    ├── 📄 exceptions.md          # Governance-approved exceptions
    ├── 📄 incidents.md           # Historical incident register
    └── 📂 evidence/
        ├── 📄 namespace-scan.json     # Automated namespace scan results
        ├── 📄 sbom-diff.json          # SBOM drift logs
        └── 📄 registry-audit.json     # Registry policy audit logs
~~~

---

## 🧪 Validation & CI/CD Enforcement

This policy is validated by:

- `security-depscan.yml`  
- `sbom-validate.yml`  
- `namespace-monitor.yml`  
- `slsa-attestation-verify.yml`  
- `governance-policy-check.yml`  

CI **cannot** be bypassed.  
All failures block merges into `main`, `release/*`, and `secure/*` branches.

---

## 🕰️ Version History

| Version | Date | Changes |
|--------|-------|---------|
| v11.2.2 | 2025-11-30 | Full rewrite, KFM-MDP v11.2.2 compliance, emoji layouts, CI-enforcement integration |
| v11.1.0 | 2025-10-02 | Added SLSA-3 requirement & namespace-diff monitoring |
| v11.0.0 | 2025-08-11 | Initial v11 policy release |

---

<div align="center">

🌐 [KFM Project](../../../../../README.md) • 🔐 [Security Standards](../../../../standards/README.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

