---
title: "🏁 KFM v11.2.2 — Namespace Collision: Version Race Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-versionrace.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Security Council"
status: "Active · Educational Example"

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
doc_kind: "Security · Example"
---

<div align="center">

# 🏁 **Namespace Collision — Version Race Attack**  
`docs/security/supply-chain/dependency-confusion/examples/namespace-collision-versionrace.md`

**Purpose:**  
Demonstrate how an attacker exploits a **version race** in public registries  
to override internal dependencies and poison the dependency graph, even when internal  
packages already exist and are properly versioned.  
This is a more subtle and timing-based version of a namespace collision attack.

</div>

---

## 📘 Background

A **version race attack** happens when:

1. KFM maintains a legitimate internal package with stable versions.  
2. An attacker publishes the *same package name* on a public registry.  
3. The attacker continually publishes **higher versions**, especially immediately after  
   internal releases.  
4. Resolvers incorrectly choose the attacker’s version due to:
   - Version precedence  
   - Fallback registry behavior  
   - Stale lockfiles  
   - Misconfigured environment using public registries  

This is one of the most common dependency-confusion exploitation patterns across ecosystems.

---

## 🧨 Example Scenario

### 🏛 Internal KFM Package
```
name: kfm-stats-core
version: 2.7.1
registry: https://kfm-pypi.internal/simple
```

### 💣 Attacker Publishes Version Race on PyPI
```
name: kfm-stats-core
versions published (chronological):
  3.0.0
  5.0.0
  7.1.1
  20.0.0
  81.0.0
```

Attacker publishes every time an internal release occurs, always staying ahead.

### 🤖 Vulnerable Resolver Impact
A misconfigured resolver sees:

- Internal: `2.7.1`  
- Public: `81.0.0`  

Version sorting selects the malicious one.

---

## 🧪 Simulated CI Detection Output

```text
[namespace-monitor]   ERROR: Version-race detected for "kfm-stats-core".
[namespace-monitor]   Internal version: 2.7.1
[namespace-monitor]   Public highest:   81.0.0
[namespace-monitor]   RISK: High — attacker likely attempting precedence override.
[policy]              FAIL: Namespace collision version-race attack detected.
[evidence]            Updated: namespace-scan.json
```

---

## 🚨 Why This Attack Works (in unprotected environments)

- Resolver behavior favors higher versions  
- Fallback to public registries allowed  
- Lockfile outdated or missing  
- SBOM drift not checked  
- Registry metadata not validated  
- No namespace quarantine  
- No timing awareness  
- No version-precedence overrides  

Attackers exploit version rules across all major ecosystems (npm, PyPI, cargo, Maven).

---

## 🛡️ How KFM v11.2.2 Prevents Version Race Attacks

### ✔ Mandatory Registry Isolation  
Public registries → **always blocked**  
Only internal mirrors allowed.

### ✔ Namespace Scanning  
Detects suspicious version spikes, timing patterns, and publishes near internal releases.

### ✔ Deterministic Pinning  
Resolvers cannot choose higher versions because exact version + hash are required.

### ✔ SBOM Drift Enforcement  
Any drift forces freeze mode.

### ✔ Provenance Enforcement  
Attackers cannot produce valid:

- Cosign signatures  
- SLSA provenance  
- Digest-matching SBOM entries  

### ✔ Evidence-Based Quarantine  
All malicious version ranges are permanently quarantined.

### ✔ Pre-Commit & Local Scan Rules  
Developers catch namespace anomalies early.

---

## 🧭 Developer Guidance

To avoid version race attack exposure:

- Always specify **exact version + registry + digest**  
- Never rely on floating version specifiers  
- If you see a sudden high-version publish on a public registry:
  - Run `kfm-ns-scan`  
  - Report to the Security Council immediately  
- Validate your environment uses proper mirrors  
- Treat version spikes as **active security incidents**  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md    # This file
    ├── 📄 typosquat-examples.md
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    └── 📄 implicit-upgrade-attack.md
~~~

---

## 🕰️ Version History

| Version | Date       | Notes |
|---------|------------|--------|
| v11.2.2 | 2025-11-30 | Initial version-race namespace collision example |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Basic Collision](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

