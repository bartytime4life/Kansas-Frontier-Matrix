---
title: "📚 KFM v11.2.2 — Dependency-Confusion Examples & Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/examples/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Security Council · FAIR+CARE"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/security-v3.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
doc_kind: "Security · Examples"
---

<div align="center">

# 📚 **Dependency-Confusion Examples & Patterns**  
`docs/security/supply-chain/dependency-confusion/examples/README.md`

**Purpose:**  
Provide concrete examples that illustrate how dependency-confusion vulnerabilities occur,  
how KFM detects and blocks them, and how developers can understand and identify  
risky patterns.  
This directory serves as a curated educational and test reference for KFM developers,  
security engineers, auditors, and automated reasoning systems.

</div>

---

## 📘 Overview

Dependency-confusion attacks exploit mismatches between:

- **Public registry package names**  
- **Internal/private package names**  
- **Resolver precedence rules**  
- **Namespace ambiguity**  
- **Version ordering behavior**  

This examples directory contains:

- Good vs. bad dependency declarations  
- Attack-pattern demonstrations  
- Typical resolver-conflict scenarios  
- Typosquatting examples  
- Namespace collision illustrations  
- Mock SBOM & lockfile examples  
- Safe and unsafe registry-resolution behaviors  
- Failed provenance and signature examples  

These examples exist for learning and for automated reasoning engines  
(e.g., KFM Focus Mode v3 security heuristics).

---

## 🎯 Example Categories

### 1. 🧨 Namespace Collision Examples  
Showcases cases where:

- A public package shares the name of an internal KFM library  
- A rogue public version outranks a private version  
- Attackers publish compatible-looking versions  

Files may include:

- `namespace-collision-basic.md`  
- `namespace-collision-firstpublish.md`  
- `namespace-collision-versionrace.md`

---

### 2. 🧿 Typosquatting Examples  
Illustrations of:

- Homoglyph attacks  
- Dash/dot/underscore swaps  
- Visual-confusable variants  
- Lookalike vendor prefixes  

Examples:

- Internal: `@kfm/core`  
- Attacker: `@kfm-cor`, `@kfn/core`, `@kfm0/core`

---

### 3. 🔐 Registry-Resolution Failure Examples  
Document what happens when:

- A resolver falls back to public registries  
- Registry URLs are malformed  
- TLS pinning breaks  
- Mirror metadata drifts  

May include:

- `registry-fallback.md`  
- `registry-mismatch.md`  
- `mirror-drift.md`

---

### 4. 🧬 SBOM & Lockfile Drift Examples  
Showcases:

- Shadow dependencies appearing in the graph  
- Unexpected version changes  
- Hash mismatches  
- SBOM divergence from lockfiles  

Example files:

- `sbom-drift-basic.json`  
- `lockfile-drift-attack.md`

---

### 5. ✍️ Signature & Provenance Failure Examples  
Includes:

- Invalid Cosign signatures  
- Missing GPG commit signatures  
- Missing SLSA provenance  
- Corrupted signature bundles  

Examples:

- `invalid-cosign.sig`  
- `missing-provenance.json`

---

### 6. 🧱 Hermetic Sandbox Violation Examples  
Demonstrates:

- Outbound network leakage  
- Resolver auto-upgrade behavior  
- Unauthorized registry contact  
- Plugin auto-installation  

Examples:

- `sandbox-network-leak.md`  
- `implicit-upgrade-attack.md`

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md                       # This file — index of examples
    ├── 📄 namespace-collision-basic.md    # Example: simple collision case
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
    ├── 📄 typosquat-examples.md           # Homoglyph/variants examples
    ├── 📄 registry-fallback.md            # Resolver fallback demonstration
    ├── 📄 mirror-drift.md                 # Mirror integrity issue example
    ├── 📄 sbom-drift-basic.json           # Simple drift example
    ├── 📄 lockfile-drift-attack.md        # Lockfile manipulation example
    ├── 📄 invalid-cosign.sig              # Example of invalid signature
    ├── 📄 missing-provenance.json         # Missing SLSA provenance example
    ├── 📄 sandbox-network-leak.md         # Hermeticity violation example
    └── 📄 implicit-upgrade-attack.md      # Auto-upgrade exploit example
~~~

---

## 🕰️ Version History

| Version | Date       | Notes |
|---------|------------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of examples directory README |

---

<div align="center">

🧪 [Automated Checks](../checks/README.md) • 🛡️ [Policy Overview](../policy/README.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

