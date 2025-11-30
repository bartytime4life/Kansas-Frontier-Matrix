---
title: "❌ KFM v11.2.2 — Verification Failure Case (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/verification-failure-case.md"
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

# ❌ **Verification Failure Case**  
`docs/security/supply-chain/dependency-confusion/examples/verification-failure-case.md`

**Purpose:**  
Provide a clear, realistic example of a **cryptographic verification failure** that signals  
a possible dependency-confusion attack, provenance compromise, or registry poisoning event.  
This example is used by training materials, KFM security auditors, and automated reasoning engines  
to illustrate how a malicious or damaged artifact is detected within KFM v11.2.2 protections.

</div>

---

## 📘 Context

This example demonstrates what happens when:

- A dependency is fetched from an internal mirror  
- Its digest does **not** match the SBOM  
- Its Cosign signature cannot be verified  
- Its SLSA provenance bundle is missing or malformed  
- Metadata from upstream differs from the internal mirror  

This type of failure often indicates:

- Shadow-package injection  
- Registry poisoning  
- Man-in-the-middle artifact replacement  
- Broken or spoofed provenance  
- Compromised build pipeline  

---

## ❌ Example Verification Failure

### 🔐 Artifact Under Test
```
package:    kfm-utils-core
version:    4.2.1
registry:   https://kfm-pypi.internal/simple
digest_sbom: sha256:4af81c22f8b5...c316a1
digest_fetched: sha256:b91c003bd7cc...f22181
cosign_signature: INVALID (public key mismatch)
slsa_provenance: MISSING
```

### 🧪 Validation Output (Simulated)

```text
[attestation-verify] ERROR: SLSA provenance bundle missing.
[digest-check]      ERROR: Digest mismatch between SBOM and fetched artifact.
[cosign-verify]     ERROR: Cosign signature invalid — key not recognized.
[registry-audit]    WARNING: Artifact metadata differs from mirror baseline.
[policy]            FAIL: Artifact verification failure — quarantine required.
```

---

## 🚩 Why This Fails Verification

### 1. 🔑 **Cosign signature invalid**
The signature was produced using a key unknown to KFM’s trust store.

### 2. 🧬 **Missing SLSA v3+ provenance**
All artifacts must provide verifiable supply-chain lineage.

### 3. 🧪 **Digest mismatch**
KFM compares:

- SBOM digest  
- Fetched artifact digest  
- Lockfile digest  
- Historical digest ledger  

Any inconsistency → immediate block.

### 4. 🛰️ **Registry metadata drift**
Mirror metadata differs from the authoritative record.

---

## 🛑 Required KFM Response

Upon this failure, KFM-CI must:

1. **Block the build**  
2. Create an **incident stub** in:  
   ```
   docs/security/supply-chain/dependency-confusion/policy/incidents.md
   ```
3. Add the package name to **quarantine**  
4. Trigger a **mirror integrity diff-check**  
5. Activate **fallback Tier 1** if SBOM drift persists  
6. Require Security Council review  
7. Rebuild from last known-good sealed dependencies  

---

## 🧭 Developer Guidance

- Do **not** override or bypass failures.  
- Regenerate local SBOM using sealed dependencies.  
- Validate GPG keys and Cosign trust store.  
- Check if your environment is using correct registries.  
- Report unexpected namespace behavior immediately.  

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
    ├── 📄 registry-fallback.md
    ├── 📄 mirror-drift.md
    ├── 📄 sbom-drift-basic.json
    ├── 📄 lockfile-drift-attack.md
    ├── 📄 invalid-cosign.sig
    ├── 📄 missing-provenance.json
    ├── 📄 sandbox-network-leak.md
    ├── 📄 implicit-upgrade-attack.md
    └── 📄 verification-failure-case.md   # This file
~~~

---

## 🕰️ Version History

| Version | Date       | Notes |
|---------|------------|--------|
| v11.2.2 | 2025-11-30 | Initial creation of verification failure example |

---

<div align="center">

📚 [Examples Index](./README.md) • 🛡️ [Policy Overview](../policy/README.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

