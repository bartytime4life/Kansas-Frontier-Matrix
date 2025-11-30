---
title: "🛰️ KFM v11.2.2 — Registry Anomaly Detection Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/registry-anomaly-detection.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Supply-Chain Security Council"
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
doc_kind: "Security · Registry-Anomaly-Detection"
---

<div align="center">

# 🛰️ **Registry Anomaly Detection Rules**  
`docs/security/supply-chain/dependency-confusion/checks/registry-anomaly-detection.md`

**Purpose:**  
Define the automated anomaly-detection logic used by KFM-CI to identify, flag, quarantine,  
and escalate suspicious registry behavior that may indicate dependency-confusion attempts,  
registry poisoning, namespace hijacking, or compromise of upstream ecosystems.

</div>

---

## 📘 Overview

Registry anomaly detection is a core component of KFM’s multilayer protection strategy.  
While registry isolation prevents most direct attacks, anomaly detection adds **behavioral and  
statistical analysis** to uncover subtle or emerging threats.

This detection engine monitors:

- Namespace activity  
- Package version patterns  
- Registry metadata drift  
- TLS & certificate anomalies  
- Package publish-time anomalies  
- Publisher-account irregularities  
- Dependency-resolution deviations  
- Typosquatting signatures  
- Sudden first-publish events in public registries  

All anomalies generate machine evidence, quarantine triggers, and CI-block events.

---

## 🛰️ Detection Categories

### 1. 🧿 Namespace Activity Anomalies
CI scans all registries for:

- New packages matching internal KFM names  
- Sudden creation of high-risk namespaces  
- Suspicious subnames (e.g., `kfmmodule`, `k-fm`, `k_fm_utils`)  
- Hyphen/dot/underscore permutations  
- Shadow versions published immediately after KFM releases  

Actions:

- Auto-block  
- Name quarantine  
- Evidence logged: `namespace-scan.json`  
- Incident stub created  

---

### 2. ⏱️ Publish-Time Pattern Anomalies
Detects unexpected version behavior:

- High-frequency version spikes  
- Duplicate version numbers  
- Unexpected major-version jumps  
- Publish bursts at odd hours / coordinated time windows  
- Version patterns matching malware campaigns  

Actions:

- Version quarantine  
- Pin rollback  
- SBOM integrity recheck  

---

### 3. 🔐 TLS & Certificate Anomalies
Ensures registry connectivity is:

- Fully TLS-pinned  
- Cert chain validated  
- Not using unexpected issuers  
- Using expected SAN entries  
- Free of clock skew or stale certs  

Anomalies → **connection denied + registry quarantine**

---

### 4. 🧬 Metadata & Digest Drift Anomalies
Compares upstream registry metadata with:

- KFM-mirror metadata  
- Known-good digests  
- SLSA provenance logs  
- Artifact checksum history  

Drift indicates:

- Registry poisoning  
- Man-in-the-middle replacement  
- Malicious re-upload  
- Shadow artifact injection  

Actions:

- Immediate SBOM drift freeze  
- Mirror quarantine  
- Evidence stored in `sbom-diff.json`  

---

### 5. 🧩 Resolution Behavior Anomalies
Detects unexpected resolver behavior:

- Resolver attempting non-allow-listed registries  
- Protocol changes (HTTP→HTTPS mismatches)  
- Overridden source maps  
- Inconsistent dependency graphs  
- Unpinned / fallback resolutions  

Actions:

- Resolution halt  
- SBD (Security Block Declaration) issued  
- Governance review  

---

### 6. 🕵️ Publisher Identity Anomalies
Examines publisher metadata in upstream registries:

Flags:

- New publishers with no history  
- Publisher-email drift  
- Maintainer handoff anomalies  
- Unexpected key-rotation events  
- Package-to-publisher mismatch patterns  

May indicate targeted compromise.

---

### 7. 🔡 Typosquatting Detection
Detects near-miss names by:

- Levenshtein distance  
- Character substitution maps  
- Prefix/suffix injection  
- Unicode homoglyph detection  
- Lookalike namespace heuristics  

Example:  
`@kfm/core` → suspicious: `@kfm-cor`, `@kfm/coree`, `@kfn/core`, `@kfm0/core`.

Actions:

- Block  
- Quarantine  
- Report to security council  

---

### 8. 🚨 Sudden First-Publish Events
Flags if external registries show first-ever publishes of:

- KFM-like names  
- Names identical to internal modules  
- Known internal dependency names  
- Variants of high-value namespaces  

This is the most common dependency-confusion signal.

---

## 🗃️ Evidence Outputs

Evidence is written into:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

Including:

- 🛰️ `namespace-scan.json`  
- 🔐 `registry-audit.json`  
- 🧬 `sbom-diff.json`  
- 🧾 `attestation-verify.json`  

All evidence MUST be:

- FAIR+CARE compliant  
- Immutable  
- Timestamped  
- Schema-validated  
- Linked via PROV-O lineage  

---

## 🧪 CI Enforcement

Registry anomaly detection participates directly in:

- `namespace-monitor.yml`  
- `registry-policy-check.yml`  
- `dependency-integrity.yml`  
- `sbom-validate.yml`  
- `slsa-attestation-verify.yml`  

Any anomaly produces:

- CI hard fail  
- Quarantine activation  
- Evidence storage  
- Required governance review  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                     # Automated checks index
    ├── 📄 ci-validation-rules.md        # CI validation rules
    ├── 📄 provenance-hooks.md           # Provenance & attestation hooks
    ├── 📄 registry-anomaly-detection.md # This file — anomaly detection rules
    ├── 📄 pre-commit-rules.md           # (optional) Developer-machine checks
    └── 📄 local-scan-guidance.md        # (optional) Manual scanning guidance
~~~

---

## 🕰️ Version History

| Version | Date | Notes |
|---------|--------|--------|
| v11.2.2 | 2025-11-30 | Initial anomaly detection rule set |

---

<div align="center">

🧪 [Automated Checks](./README.md) • 🔒 [Registry Isolation](../policy/registry-isolation.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

