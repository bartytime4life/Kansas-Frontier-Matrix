---
title: "🌫️ KFM v11.2.2 — Mirror Drift Attack (Dependency-Confusion Example)"
path: "docs/security/supply-chain/dependency-confusion/examples/mirror-drift.md"
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

# 🌫️ **Mirror Drift Attack Example**  
`docs/security/supply-chain/dependency-confusion/examples/mirror-drift.md`

**Purpose:**  
Illustrate how **mirror drift**—a divergence between KFM’s internal package mirror and  
the authoritative upstream registry—can enable dependency-confusion attacks, SBOM drift,  
and artifact injection, especially in misconfigured environments or when provenance checks fail.

</div>

---

## 📘 Background

A **mirror drift attack** occurs when:

1. The internal KFM mirror reflects package metadata inconsistently.
2. Upstream (public) registry content changes unexpectedly.
3. The mirror synchronizes partially or with corrupted metadata.
4. Malicious actors exploit upstream changes to inject altered packages.
5. CI or local environments fetch mismatched versions, hashes, or metadata.

Mirror drift is especially dangerous because it:

- Breaks reproducibility  
- Creates SBOM mismatches  
- Enables stealthy package replacement  
- Undermines provenance validation  
- Might bypass naive caching systems  

Attackers often aim for drift windows during sync operations.

---

## 🌫️ Example Scenario

### 🏛 Internal Mirror Should Contain
```
package: kfm-analytics-core
version: 1.4.0
digest: sha256:6fd202aa...
slsa_provenance: VALID
signature: cosign OK
```

### 💣 Upstream Registry Is Tampered
```
package: kfm-analytics-core
version: 1.4.0
digest: sha256:a7dd900b...   # different hash!
slsa_provenance: MISSING
signature: INVALID
uploaded: 2025-11-29 02:15:10 UTC
```

### 😱 Resulting Mirror Drift
During an automated sync:

- Mirror pulls the *malicious* upstream version  
- Metadata overwrites internal entry  
- SBOM digest no longer matches  
- Resolver quietly installs malicious artifact  

---

## 🧪 Simulated CI Detection Output

```text
[mirror-integrity]    ERROR: Mirror digest mismatch detected for kfm-analytics-core.
[namespace-monitor]   WARNING: upstream publish timestamp suggests suspicious activity.
[attestation-verify]  ERROR: SLSA provenance missing.
[sbom-validate]       ERROR: SBOM mismatch: expected sha256:6fd202aa..., actual sha256:a7dd900b...
[policy]              FAIL: Mirror drift attack detected — quarantine activated.
```

Evidence is stored in:

- `policy/evidence/registry-audit.json`
- `policy/evidence/sbom-diff.json`
- `policy/evidence/attestation-verify.json`

---

## 🚨 Why This Attack Works (in unprotected systems)

- Mirrors sync blindly from upstream  
- No digest or metadata verification  
- No provenance validation  
- No TLS pinning or SAN validation  
- No namespace or timestamp anomaly detection  
- Lack of SBOM enforcement  
- Resolver trusts mirror without verifying signatures  

This allows attackers to poison mirrors with lookalike versions.

---

## 🛡️ How KFM v11.2.2 Blocks This Attack

### ✔ TLS Pinning  
Mirror-sync must validate certificate chain and SAN entries.

### ✔ Digest Equivalence Enforcement  
Checks SBOM vs. upstream vs. mirror digests.

### ✔ Provenance Validation  
Mirror refuses artifacts lacking valid:

- Cosign signatures  
- SLSA v3+ provenance bundles  

### ✔ Drift Freeze Mode  
If drift is detected:

- Tier 1 fallback activated  
- Only sealed dependencies allowed  
- Mirror quarantined  
- No further sync permitted  

### ✔ Evidence Logging  
Drift alerts populate multiple evidence records for forensics.

### ✔ CI Hard-Fail  
Build immediately blocked.

### ✔ Namespace Scanning  
Upstream timestamp anomalies flagged.

---

## 🧭 Developer Guidance

If mirror drift is detected:

1. **Stop using the affected mirror** immediately.  
2. Inspect `policy/evidence/registry-audit.json`.  
3. Compare against last-known-good sealed artifacts.  
4. Trigger a rollback to a sealed dependency snapshot.  
5. Notify the Security Council to review the drift event.  
6. Never manually override drift detections.

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
    ├── 📄 mirror-drift.md              # This file
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
| v11.2.2 | 2025-11-30 | Initial mirror-drift example added |

---

<div align="center">

📚 [Examples Index](./README.md) • 🧩 [Lockfile Drift](./lockfile-dri)

