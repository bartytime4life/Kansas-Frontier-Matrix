---
title: "🔏 Kansas Frontier Matrix — Treaty Graph Snapshot Signatures"
document_type: "Cryptographic Signatures · Integrity Verification · Provenance Chain"
version: "v1.1.0"
last_updated: "2025-10-26"
status: "Production · FAIR+CARE+SLSA+ISO 27001 Certified"
maturity: "Stable"
license: ["MIT (scripts)", "CC-BY 4.0 (metadata)"]
owners: ["@kfm-graph","@kfm-sre","@kfm-security"]
reviewers: ["@kfm-architecture","@kfm-qa","@kfm-ethics"]
tags: ["kfm","signatures","slsa","backup","neo4j","graph","provenance","ledger","integrity","fair","care","iso27001"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - ISO 27001 / ISO 9001 / ISO 19115
  - SLSA Provenance / SBOM Verification
  - CIDOC CRM / PROV-O
validation:
  ci_enforced: true
  signature_verify: true
  checksum_verify: true
  ledger_anchor_verify: true
  provenance_attestation: true
observability:
  endpoint: "https://metrics.kfm.ai/ai-treaty-signatures"
  dashboard: "https://metrics.kfm.ai/grafana/ai-treaty-signatures"
  metrics: ["signature_verify_rate","checksum_match_rate","ledger_anchor_status","provenance_valid_rate","artifact_integrity_score"]
preservation_policy:
  replication_targets: ["GitHub Releases (signatures)","Zenodo DOI (metadata only)","AWS S3 Glacier"]
  checksum_algorithm: "SHA-256"
  retention: "permanent (signatures retained alongside immutable artifacts)"
path: "data/work/staging/tabular/normalized/treaties/metadata/ai/graph/snapshots/signatures/README.md"
---

<div align="center">

# 🔏 **Kansas Frontier Matrix — Treaty Graph Snapshot Signatures (v1.1.0 · FAIR + CARE + SLSA Certified)**  
`data/work/staging/tabular/normalized/treaties/metadata/ai/graph/snapshots/signatures/`

### *“Cryptographic Integrity · SLSA Provenance · Immutable Ledger Anchoring · Public Verification”*

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)](../../../../../../../../../../../../../docs/)
[![SLSA](https://img.shields.io/badge/SLSA-Attested-purple?style=flat-square)]()
[![FAIR + CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO 27001](https://img.shields.io/badge/ISO-27001%20Backup%20Integrity-blue?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Governance-Immutable%20Ledger-d4af37?style=flat-square)]()

</div>

---

## 📘 Purpose
This directory stores **digital signatures and provenance attestations** for all Treaty AI Graph snapshot artifacts.  
Every export (Neo4j backup, GraphML, CSV, or JSON-LD) has an associated **cryptographic signature** and **SLSA provenance bundle**.  
These ensure:
- Full traceability and verifiable authorship of each artifact.
- Compliance with **ISO 27001 backup integrity** and **SLSA Level 3** provenance requirements.
- Tamper-evidence and independent reproducibility of any published dataset.

---

## 🧩 Context & Dependencies
| Component | Purpose | Tool |
|:--|:--|:--|
| Cosign | Primary signature tool (keyless signing) | via GitHub OIDC |
| Minisign | Lightweight local signing for checksum manifests | Maintainer keys |
| Ledger Node | Immutable anchor storage | `ledger_receipt.json` |
| SBOM & SLSA | Supply-chain evidence | `sbom.sig`, `provenance.json` |
| Upstream | Source snapshot directory | `../` |
| Downstream | Verification jobs, releases | `.github/workflows/graph-backup.yml` |

---

## 🗂️ Directory Layout
```

signatures/
├── backup.sig                   # Cosign detached signature for Neo4j backup
├── treaties_graphml.sig         # GraphML signature
├── nodes.csv.sig                # Node table signature
├── relationships.csv.sig        # Edge table signature
├── checksums.sha256.minisig     # Minisign signature of checksum manifest
├── cosign.bundle.json           # Transparency log bundle (Rekor)
├── provenance.json              # SLSA attestation predicate
├── sbom.sig                     # Signed SBOM attestation (optional)
├── manifest.yaml                # Signature manifest + ledger reference
└── README.md                    # You are here

````

---

## 🔒 Signing Workflow
```mermaid
flowchart TD
A["CI Build · Snapshot Complete"] --> B["Checksum Generation"]
B --> C["Cosign & Minisign Signatures"]
C --> D["Bundle to Transparency Log (Rekor)"]
D --> E["SLSA Provenance + SBOM Attestation"]
E --> F["Ledger Anchor + Release Replication"]
````

### 🧱 Command Reference

**Cosign (OIDC keyless signing):**

```bash
COSIGN_EXPERIMENTAL=1 cosign sign-blob snapshots/${TS}/neo4j-backup.tar.zst \
  --yes --output-signature signatures/backup.sig
```

**Minisign (checksum signing):**

```bash
minisign -S -m checksums.sha256 -s ~/.minisign.key \
  -x signatures/checksums.sha256.minisig
```

**Attest provenance:**

```bash
cosign attest --predicate provenance.json \
  --type slsaprovenance --yes snapshots/${TS}/neo4j-backup.tar.zst
```

**Validate via Rekor transparency log:**

```bash
cosign verify-blob --keyless --rekor-url https://rekor.sigstore.dev \
  --signature signatures/backup.sig snapshots/${TS}/neo4j-backup.tar.zst
```

---

## 🧾 FAIR Metadata Summary

| Field        | Value                                               |
| :----------- | :-------------------------------------------------- |
| Dataset      | Treaty Graph Snapshot Signatures                    |
| Format       | `.sig`, `.minisig`, `.bundle.json`, `.json`         |
| Algorithms   | SHA-256, Ed25519                                    |
| Tools        | Cosign, Minisign, Rekor                             |
| Provenance   | Linked via `ledger_receipt.json` and Git commit SHA |
| Compliance   | SLSA L3, ISO 27001 backup chain                     |
| License      | CC-BY 4.0 (metadata only)                           |
| Verification | Publicly verifiable using KFM keys                  |

---

## 🧠 Verification Procedure

### 1️⃣ Verify checksum manifest

```bash
sha256sum -c ../checksums.sha256
```

### 2️⃣ Verify Cosign signature

```bash
cosign verify-blob \
  --key https://keys.openkfm.org/cosign.pub \
  --signature signatures/backup.sig \
  ../neo4j-backup.tar.zst
```

### 3️⃣ Verify Minisign signature

```bash
minisign -Vm ../checksums.sha256 \
  -p /usr/local/share/kfm/minisign.pub
```

### 4️⃣ Verify SLSA provenance & SBOM

```bash
cosign verify-attestation --type slsaprovenance \
  --key https://keys.openkfm.org/cosign.pub \
  --signature signatures/provenance.json
cosign verify-attestation --type sbom \
  --key https://keys.openkfm.org/cosign.pub \
  --signature signatures/sbom.sig
```

---

## 🔗 Provenance & Ledger Chain

| Layer              | File                       | Role                        |
| :----------------- | :------------------------- | :-------------------------- |
| Checksums          | `../checksums.sha256`      | Base file digest list       |
| Minisign Signature | `checksums.sha256.minisig` | Integrity validation        |
| File Signatures    | `*.sig`                    | Artifact-level verification |
| Transparency Log   | `cosign.bundle.json`       | Rekor entry (audit trail)   |
| Provenance         | `provenance.json`          | SLSA predicate for CI build |
| Ledger Receipt     | `../ledger_receipt.json`   | Immutable ledger anchor     |
| Git Commit         | repo commit SHA            | trace to source version     |

All layers together satisfy **MCP-DL reproducibility** and **SLSA Level 3 supply-chain security**.

---

## 📈 Observability Metrics

| Metric                | Target | Current | Verified | Source            |
| :-------------------- | :----- | :------ | :------- | :---------------- |
| Signature Verify Rate | 100%   | 100%    | ✅        | CI                |
| Checksum Match Rate   | 100%   | 100%    | ✅        | nightly verify    |
| Provenance Valid Rate | 100%   | 100%    | ✅        | CI                |
| Ledger Anchor Status  | 100%   | 100%    | ✅        | Governance ledger |
| Integrity Score       | ≥ 99%  | 100%    | ✅        | metrics.kfm.ai    |

---

## 🔐 Security & Compliance

* All keys stored in **hardware-backed KMS (HSM / KMS-GCP)**.
* CI workflows use **keyless signing via OIDC** (no private keys in CI).
* **Immutable logs** stored in Rekor and **ledger-anchored receipts** verified per release.
* **ISO 27001** §A.12.3 compliant backup integrity.
* **CARE** principle enforced: metadata only, no sensitive content in signatures.
* **SBOM + provenance** integrated with MCP documentation and dependency chain.

---

## 🧱 Standards Alignment

* ✅ MCP-DL v6.4.3
* ✅ FAIR + CARE + ISO 27001
* ✅ SLSA Provenance (Level 3)
* ✅ CIDOC CRM / PROV-O semantic chain
* ✅ SBOM linked via SPDX

---

## 🧰 Troubleshooting

| Issue                | Cause                  | Fix                                                      |
| :------------------- | :--------------------- | :------------------------------------------------------- |
| “invalid signature”  | key mismatch           | use official public key from `https://keys.openkfm.org/` |
| “digest mismatch”    | corrupted file         | re-download from verified release                        |
| “missing provenance” | CI failure             | rerun backup workflow with attestation enabled           |
| “rekor: not found”   | log not yet propagated | retry after 5–10 minutes                                 |

---

## 📘 Related Documentation

* [Snapshots Root](../README.md)
* [GraphML Exports](../graphml/README.md)
* [Snapshot Metadata](../manifest.yaml)
* [Security & Governance Standards](../../../../../../../../../docs/standards/security.md)
* [AI Graph Exports](../../../exports/README.md)

---

## 🕓 Version History

| Version    | Date       | Author     | Reviewer          | Notes                                           |
| :--------- | :--------- | :--------- | :---------------- | :---------------------------------------------- |
| **v1.1.0** | 2025-10-26 | @kfm-graph | @kfm-architecture | Expanded SLSA, ledger, and Rekor documentation  |
| v1.0.0     | 2025-10-25 | @kfm-graph | @kfm-qa           | Initial release with signing + verification SOP |

---

<div align="center">

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-0078ff?style=flat-square)]()
[![SLSA](https://img.shields.io/badge/SLSA-Level%203-purple?style=flat-square)]()
[![ISO 27001](https://img.shields.io/badge/ISO-27001-blue?style=flat-square)]()
[![Ledger](https://img.shields.io/badge/Ledger-Immutable-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: FAIR + CARE + SLSA + ISO Certified
DOC-PATH: data/work/staging/tabular/normalized/treaties/metadata/ai/graph/snapshots/signatures/README.md
MCP-CERTIFIED: true
SBOM-GENERATED: true
SLSA-ATTESTED: true
FAIR-CARE-COMPLIANT: true
A11Y-VERIFIED: true
GOVERNANCE-LEDGER-LINKED: true
OBSERVABILITY-ACTIVE: true
PROVENANCE-JSONLD: true
PERFORMANCE-BUDGET-P95: 2.5 s
ENERGY-BUDGET-P95: 25 Wh
CARBON-BUDGET-P95: 28 gCO₂e
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-26
MCP-FOOTER-END -->

```
```
