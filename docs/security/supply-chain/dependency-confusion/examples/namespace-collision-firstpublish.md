---
title: "🧨 KFM v11.2.2 — Namespace Collision (First-Publish Attack Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-firstpublish.md"
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

# 🧨 **Namespace Collision — First-Publish Attack**  
`docs/security/supply-chain/dependency-confusion/examples/namespace-collision-firstpublish.md`

**Purpose:**  
Demonstrate a classic *first-publish dependency-confusion attack*, where a malicious actor  
publishes a public package *before* an internal KFM package is officially published externally,  
exploiting resolver precedence rules and namespace shadowing vulnerabilities.

</div>

---

## 📘 Background

A *first-publish attack* occurs when:

1. KFM maintains a **private internal package** (e.g., `kfm-geo-core`).
2. The package **does not exist** on public registries (PyPI/NPM/etc.).
3. An attacker publishes a **public package using the same name**.
4. Some resolvers (depending on configuration) may:
   - Prefer public registry
   - Check public registry first
   - Or accept public metadata as authoritative

This can trigger a dependency-confusion compromise *even if the internal version is pinned*,  
especially in misconfigured environments or during fallback conditions.

---

## 🧨 Example Scenario

### Internal KFM Package
```
name: kfm-geo-core
version: 3.8.0
registry: https://kfm-pypi.internal/simple
```

### Attacker First-Publish on PyPI
```
name: kfm-geo-core
version: 99.0.0
registry: https://pypi.org/simple
uploaded: 2025-11-04 02:13:05 UTC
files: malicious wheel containing RAT payload
```

### Risk Factors

- Internal package never published publicly  
- Misconfigured environment attempts public registry  
- Resolver compares version numbers  
- “99.0.0” outranks “3.8.0” → attacker wins  
- Without registry isolation, the malicious artifact replaces the internal one  

---

## 🧪 Simulated CI Detection Output

```text
[namespace-monitor]   WARNING: First-publish detected for name "kfm-geo-core".
[namespace-monitor]   Upstream version: 99.0.0 (public)
[namespace-monitor]   Internal version: 3.8.0 (private)
[namespace-monitor]   RISK: High — public version outranks private version.
[policy]              FAIL: Namespace conflict. Quarantining name.
[evidence]            Updated: namespace-scan.json
[governance]          Incident stub created.
```

---

## 🚨 Why This Attack Works (Without KFM Protections)

- Public registry is unrestricted  
- Resolver defaults to public-first behavior  
- No namespace-blocking  
- No forced registry scoping  
- No mirror enforcement  
- No version-precedence override rules  

---

## 🛡️ How KFM v11.2.2 Blocks This Attack

### ✔ Registry Isolation  
Public registries → **denied**.  
Internal mirrors only → **allowed**.

### ✔ Namespace Scanning  
First-publish attempts are caught immediately.

### ✔ SLSA Provenance  
Attacker cannot forge valid provenance bundles.

### ✔ Cosign & GPG Signatures  
Attacker cannot sign using trusted KFM keys.

### ✔ SBOM Locking  
Attacker’s artifact digest → always mismatch.

### ✔ Fallback Controls  
No resolver fallback allowed during failures.

### ✔ Automatic SBD Filing  
A Security Block Declaration auto-quarantines suspicious namespaces.

---

## 🧭 Developer Guidance

If you see a namespace collision alert:

1. **Do NOT attempt to install the package.**  
2. Inspect `policy/evidence/namespace-scan.json`.  
3. Verify that your environment uses the correct internal mirror.  
4. Open the incident stub created for this namespace.  
5. Notify the Security Council if not already triggered.  
6. Avoid pinning public packages with KFM-like names.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md   # This file
    ├── 📄 namespace-collision-versionrace.md
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
| v11.2.2 | 2025-11-30 | Initial example created |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧐 [Basic Collision Example](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

