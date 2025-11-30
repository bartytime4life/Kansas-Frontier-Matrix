---
title: "⛓️ KFM v11.2.2 — Registry Fallback Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/registry-fallback.md"
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

# ⛓️ **Registry Fallback Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/registry-fallback.md`

**Purpose:**  
Illustrate how a resolver or build environment that silently **falls back** to a public registry  
can trigger a full dependency-confusion compromise—even when internal mirrors exist  
and internal packages are properly pinned.  
This example demonstrates a common real-world misconfiguration scenario.

</div>

---

## 📘 Background

A **registry fallback attack** occurs when:

1. The primary (internal) registry or mirror returns an error (timeout, TLS mismatch, 404, etc.).
2. The resolver attempts **secondary registries**, often including public ones.
3. A malicious public package with the same name exists.
4. The resolver installs the public package silently.
5. SBOM, lockfile, or provenance checks are bypassed in misconfigured environments.

This attack is extremely common in unsealed environments and early-stage CI systems.

---

## 🔗 Example Scenario

### 🏛 Internal KFM Package (Expected)
```
package: kfm-routing-core
version: 1.9.3
registry: https://kfm-pypi.internal/simple
hash: sha256:ee71bb12...
```

### 💣 Public Package (Malicious)
```
package: kfm-routing-core
version: 88.0.0
registry: https://pypi.org/simple
hash: sha256:abee990e...
payload: remote-exec, credential exfiltration
```

### ⚠️ Fallback Misconfiguration
Example (pip config):

```
[global]
timeout = 2
extra-index-url = https://pypi.org/simple         # ❌ dangerous fallback
trusted-host = pypi.org
```

Resolver behavior:

1. Internal mirror → timeout after 2 seconds  
2. Resolver falls back to PyPI  
3. Installs malicious version (`88.0.0`)  
4. Lockfile + SBOM become invalid  
5. No provenance metadata  

---

## 🧪 Simulated CI Detection Output

```text
[registry-policy-check] FAIL: Public registry contact detected for "kfm-routing-core".
[namespace-monitor]    WARNING: Public version outranks private version.
[attestation-verify]   ERROR: No valid SLSA provenance for fetched artifact.
[sbom-validate]        ERROR: SBOM mismatch with installed package.
[policy]               FAIL: Registry fallback attack detected — quarantine required.
```

Evidence written to:

- `policy/evidence/registry-audit.json`
- `policy/evidence/namespace-scan.json`

---

## 🚨 Why This Attack Works (in unprotected systems)

- Resolver fallback behavior enabled  
- Internal registry configured as non-blocking  
- Short timeouts  
- Public registry access allowed  
- No SBOM or hash validation  
- No provenance enforcement  
- No namespace-scanning system  

---

## 🛡️ How KFM v11.2.2 Prevents Registry Fallback Attacks

### ✔ Registry Isolation (Mandatory)
Public registries → **blocked**, never attempted.  
Internal mirrors → **exclusive** source.

### ✔ Hermetic Sandbox Enforcement  
Resolvers cannot reach external endpoints.

### ✔ Deterministic Pinning  
Exact registry + version + digest ensures no fallback override.

### ✔ Namespace Collision Detection  
High-version public variants immediately flagged.

### ✔ SBOM Drift Enforcement  
Detects mismatch between expected & installed versions.

### ✔ Provenance Requirements  
Malicious public packages lack valid SLSA bundles or Cosign signatures.

### ✔ Mirror Integrity Monitoring  
Detects mirror failure *before* resolvers attempt fallback.

### ✔ Fallback Tier Activation  
If mirror issue detected → freezes dependency graph rather than falling back.

---

## 🧭 Developer Guidance

To prevent registry fallback issues:

- **Never** use `extra-index-url` or `--index-url` pointing to public registries  
- Avoid short `timeout` values  
- Use only KFM-approved mirror configs  
- Validate pip/npm/cargo settings with:
  ```bash
  kfm-reg-audit --strict
  ```
- Ensure pre-commit hooks prevent fallback-prone configs  
- Treat fallback warnings as **critical incidents**  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 examples/
    ├── 📄 README.md
    ├── 📄 namespace-collision-basic.md
    ├── 📄 namespace-collision-firstpublish.md
    ├── 📄 namespace-collision-versionrace.md
    ├── 📄 typosquat-examples.md
    ├── 📄 registry-fallback.md           # This file
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
| v11.2.2 | 2025-11-30 | Initial registry-fallback example |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧨 [Basic Collision](./namespace-collision-basic.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

