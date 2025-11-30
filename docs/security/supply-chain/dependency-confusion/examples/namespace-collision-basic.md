---
title: "🧨 KFM v11.2.2 — Namespace Collision (Basic Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md"
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

# 🧨 **Namespace Collision — Basic Example**  
`docs/security/supply-chain/dependency-confusion/examples/namespace-collision-basic.md`

**Purpose:**  
Provide a minimal, introductory example of how a namespace collision can lead to a  
dependency-confusion vulnerability when registries, resolvers, or environments are  
misconfigured or insufficiently isolated.  
This example is used for baseline training, threat-modeling, and CI simulation.

</div>

---

## 📘 Background

A namespace collision occurs when:

- A **public package** and an **internal KFM package** share the **same name**  
- A resolver cannot distinguish between the two without registry isolation  
- Version precedence or fallback behavior causes the wrong package to be chosen  

This is the most foundational pattern in dependency-confusion exploitation.

---

## 🧨 Example Scenario

### 🏛 Internal KFM Package
```
name: kfm-data-core
version: 2.3.0
registry: https://kfm-pypi.internal/simple
```

### 💣 Public Package (Malicious or Accidental)
```
name: kfm-data-core
version: 50.0.0
registry: https://pypi.org/simple
uploaded: 2025-11-28
files: attacker_payload.whl
```

### 🤖 Misconfigured Resolver Behavior
The resolver:

1. Checks public registry first  
2. Finds version `50.0.0`  
3. Sees it satisfies version constraints (or outranks internal version)  
4. Selects the public malicious package  

---

## 🧪 Simulated CI Detection Output

```text
[namespace-monitor]   ERROR: Public registry collision detected for "kfm-data-core".
[namespace-monitor]   Public version:   50.0.0
[namespace-monitor]   Internal version: 2.3.0
[policy]              FAIL: Namespace collision — high-risk.
[evidence]            Updated: namespace-scan.json
```

---

## 🚨 Why This Attack Works (Without Protection)

- Resolver does not enforce private registry usage  
- No namespace blacklist  
- Floating version specifiers  
- No SBOM-lockfile alignment  
- No provenance validation  
- No mirror integrity checks  

---

## 🛡️ How KFM v11.2.2 Prevents Namespace Collisions

### ✔ Strict Registry Isolation  
Public registries → **blocked**  
Internal mirrors → **mandatory**

### ✔ Namespace Collision Scanning  
Public registry publishes using internal names are detected immediately.

### ✔ Deterministic Pinning  
Requires version + registry + digest consistency.

### ✔ Provenance & Signature Enforcement  
Malicious packages cannot satisfy SLSA or signature requirements.

### ✔ SBOM Drift Checks  
Ensures only sealed, known-good dependencies are allowed.

### ✔ Hermetic Build Sandbox  
Prevents unintended registry fallback behavior.

---

## 🧭 Developer Guidance

To avoid namespace collision risk:

- Always rely on internal mirrors  
- Never pin dependencies without registry specification  
- Run local namespace scan before committing:
  ```bash
  kfm-ns-scan .
  ```
- Treat collision alerts as **high severity**  
- Immediately escalate to the Security Council  
- Validate your dev environment uses correct mirror URLs  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md     # This file
    ├── 📄 namespace-collision-firstpublish.md
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
| v11.2.2 | 2025-11-30 | Initial creation of basic namespace collision example |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [First-Publish Example](./namespace-collision-firstpublish.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

