---
title: "📏 KFM v11.2.2 — Dependency-Confusion Enforcement Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/rules.md"
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
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
pipeline_contract_version: "KFM-PDC v11"
doc_kind: "Security · Ruleset"
---

<div align="center">

# 📏 **Dependency-Confusion Enforcement Rules**  
`docs/security/supply-chain/dependency-confusion/policy/rules.md`

**Purpose:**  
Define the *mandatory enforcement rules* for detecting, preventing, and mitigating  
dependency-confusion attacks within the Kansas Frontier Matrix (KFM) v11.2.2 supply chain.  
All rules in this document are actively enforced by CI/CD, security governance, and SBOM/SLSA  
attestation layers.

</div>

---

## 📘 Overview

These rules implement the KFM dependency-confusion defense strategy across:

- Package managers (pip, npm, cargo, nuget, maven, gem, go mod)
- Registry mirrors & isolation policies  
- SBOMs + SLSA attestation rules  
- Permission boundaries in CI/CD  
- Artifact inspection and hashing requirements  
- Namespace collision detection & quarantine procedures  

Rules in this file are **non-optional** and enforced in automated governance, deterministic pipelines,  
and dependency-integrity workflows.

---

## 🧱 Enforcement Rules (Required)

### 1. 🧩 Deterministic Pinning
All dependencies MUST:

- Declare **exact versions**, **full registries**, and **hashes**.  
- Use lockfiles checked into the monorepo.  
- Align with SBOM artifact digests.

**Prohibited:**  
- Wildcards (`*`, `>`, `^`, `~`)  
- Floating versions  
- Registry defaults (implicit URLs)

---

### 2. 🔒 Registry Isolation
The only allowed registries are the KFM-governed mirrors.

Examples:

| Ecosystem | Allowed | Forbidden |
|----------|---------|-----------|
| pip | `https://kfm-pypi.internal/simple` | `pypi.org`, `test.pypi.org` |
| npm | `https://npm.pkg.github.com/@kfm/*` | `registry.npmjs.org` |
| cargo | `source = "kfm-internal"` | crates.io |
| maven | `kfm-mirror` | central.maven.org |

**Any** attempted resolution to a forbidden registry triggers a CI block.

---

### 3. 🧬 SBOM & SLSA Enforcement
Each build MUST:

- Include all dependencies in the SBOM  
- Validate digests  
- Validate provenance (SLSA ≥3)  

Discrepancies → **build halted + SBD filed.**

---

### 4. 🛰️ Namespace Collision Scanning
Automated scans run:

- On every PR  
- On every dependency-update workflow  
- Daily via schedule  

Findings include:

- Public-package name collisions  
- Shadowing attempts  
- Malicious “first publish” registrants  

Detected packages → quarantined AND added to the denylist.

---

### 5. 🧪 CI/CD Sandboxed Execution
Builds may NOT:

- Access the public Internet  
- Fetch unpinned packages  
- Install dependencies not present in mirrors  
- Modify lockfiles without governance approval  

Sandboxing is enforced via KFM-CI virtualization.

---

### 6. 🧯 Immediate Quarantine Procedures
If a suspicious dependency is identified:

1. Trigger CI fail  
2. Generate incident stub in:
   ```
   docs/security/supply-chain/dependency-confusion/policy/incidents.md
   ```
3. Move resolving package name into quarantine list  
4. Block merges until reviewed  
5. Require crisis rebuild using sealed dependencies  

---

### 7. 📝 Mandatory Governance for Exceptions
Any deviation MUST:

- Create an SER (Security Exception Request)  
- Be logged in:
  ```
  docs/security/supply-chain/dependency-confusion/policy/exceptions.md
  ```
- Be time-limited (≤ 90 days)  
- Include compensating controls  
- Pass Council vote  

No undocumented exceptions allowed.

---

### 8. 📦 Lockfile Integrity Rules
Lockfiles must:

- Include full registry URLs  
- Include exact package resolutions  
- Be cryptographically hashed  
- Be referenced in the SBOM  

Lockfile drift triggers SBOM mismatch → merge blocked.

---

### 9. 🛡️ Artifact Validation Rules
All build artifacts must:

- Include provenance  
- Match SBOM digests  
- Be built from pinned dependencies only  
- Pass hash verification  

Artifacts that fail → rejected.

---

### 10. 📡 Telemetry & Evidence Logging
Every enforcement event logs machine evidence to:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

Evidence includes:

- namespace-scan logs  
- sbom-diff results  
- registry-audit reports  
- attestation verification  

These logs are immutable and FAIR+CARE compliant.

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md           # Overview policy document
├── 📄 rules.md            # This enforcement ruleset
├── 📄 exceptions.md       # Approved exceptions (governance-required)
├── 📄 incidents.md        # Historical incident registry
└── 📂 evidence/           # Machine evidence archive
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json (optional)
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|--------|--------|--------|
| v11.2.2 | 2025-11-30 | First complete v11.2.2 enforcement-rules release |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 🗂️ [Evidence](./evidence/README.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

