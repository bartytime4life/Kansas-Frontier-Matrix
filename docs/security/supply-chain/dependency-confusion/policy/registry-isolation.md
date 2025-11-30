---
title: "🔒 KFM v11.2.2 — Registry Isolation Policy (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/registry-isolation.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Supply-Chain Security Council"
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
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
doc_kind: "Security · Registry-Isolation"
---

<div align="center">

# 🔒 **Registry Isolation Policy**  
`docs/security/supply-chain/dependency-confusion/policy/registry-isolation.md`

**Purpose:**  
Enforce strict registry isolation to prevent dependency-confusion attacks via unauthorized or  
public dependency-resolution channels across all KFM ecosystems (pip, npm, cargo, maven, nuget, gem).  
Defines the exact allow-lists, mirror rules, blocking behavior, and CI/CD enforcement boundaries.

</div>

---

## 📘 Overview

Registry isolation is the **first and most critical layer** in KFM’s dependency-confusion defense strategy.

KFM v11.2.2 mandates **complete closure** of all public registries by default.  
Only explicitly approved internal mirrors and scoped registries may be used.

This policy:

- Prevents namespace shadowing  
- Blocks rogue upstream packages  
- Ensures SLSA and SBOM reproducibility  
- Guarantees deterministic, hermetic builds  
- Protects CI/CD from accidental registry leakage  
- Maintains FAIR+CARE compliance for software provenance  

Registry isolation is *always active* and cannot be bypassed without a documented Security Exception Request (SER).

---

## 🔐 Allowed Registries (Strict Allow-List)

Each package ecosystem must use only the following sealed registries:

### 🐍 Python (pip / poetry)
- **Allowed:**  
  - `https://kfm-pypi.internal/simple`  
- **Forbidden:**  
  - `https://pypi.org/simple`  
  - `https://test.pypi.org/simple`  
  - Any non-KFM domain

### 📦 NPM (JavaScript / TypeScript)
- **Allowed:**  
  - `https://npm.pkg.github.com/@kfm/*`  
- **Forbidden:**  
  - `https://registry.npmjs.org/*`  
  - Any unscoped access

### 🦀 Cargo (Rust)
- **Allowed:**  
  - `[source.kfm]` internal mirror  
- **Forbidden:**  
  - crates.io  
  - Any fallback sources

### ☕ Maven / Gradle (Java)
- **Allowed:**  
  - `kfm-mirror`  
- **Forbidden:**  
  - `central.maven.org`  
  - `repo1.maven.org`  
  - Any OSSSonatype endpoint

### 📦 NuGet (.NET)
- **Allowed:**  
  - `https://nuget.kfm.internal/v3/index.json`  
- **Forbidden:**  
  - `https://api.nuget.org/v3/index.json`

### 💎 RubyGems
- **Allowed:**  
  - `https://gems.kfm.internal/`  
- **Forbidden:**  
  - `https://rubygems.org/`

---

## 🧱 Mandatory Isolation Rules

### 1. 🌐 Outbound Registry Firewall
All CI builds run in network-sealed containers:

- No outbound internet  
- No external DNS resolution  
- No implicit registry fallbacks  
- All resolution forced through internal mirrors  

### 2. 🧩 Explicit Registry Declaration
Every dependency MUST specify:

- Full registry URL  
- Exact version  
- Hash integrity  

Implicit defaults → **merge blocked.**

### 3. 🛑 Public Registry Denylist
A denylist is maintained for:

- Public registries (e.g., PyPI, npmjs)  
- Known malicious mirrors  
- Package names associated with namespace collisions  

Denylist violations generate:

1. CI hard-fail  
2. Evidence record  
3. Incident stub in `incidents.md`  
4. Governance review

### 4. 🛰️ Registry Integrity Verification
Internal mirrors are validated daily via:

- TLS pinning  
- Digest verification  
- Mirror-content diff checks  
- SLSA provenance validation  
- Quarantine for mismatches  

### 5. 🔍 Drift & Rollback Controls
If a mirror:

- Has drifted  
- Returns mismatched artifacts  
- Becomes unverifiable  

Then:

- Mirror is quarantined  
- Local artifact cache becomes sole source  
- Fallback-controls.md Tier 1 freeze activates  

---

## 🧪 CI Enforcement

Registry isolation is enforced by:

- `registry-policy-check.yml`  
- `namespace-monitor.yml`  
- `dependency-integrity.yml`  
- `slsa-attestation-verify.yml`  
- `sbom-validate.yml`  

Failures → **merge blocked** on all protected branches.

---

## 📂 Directory Layout

~~~text
📁 policy/
├── 📄 README.md               # High-level dependency-confusion policy
├── 📄 rules.md                # Enforcement rules
├── 📄 registry-isolation.md   # This file — registry isolation policy
├── 📄 exceptions.md           # SER-approved exceptions
├── 📄 incidents.md            # Historical incident registry
└── 📂 evidence/
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json (optional)
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial registry-isolation policy created |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 📏 [Enforcement Rules](./rules.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

