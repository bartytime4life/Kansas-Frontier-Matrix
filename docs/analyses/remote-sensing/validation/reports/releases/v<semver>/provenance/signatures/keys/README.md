---
title: "🔑 KFM — Release Validation Public Keys (v<semver>) · Trust Notes · Rotation · Verification"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/keys/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Policy"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-release-public-keys"
audience:
  - "Reliability Engineering"
  - "Security Reviewers"
  - "Governance Reviewers"
  - "Remote Sensing Engineering"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:provenance:signatures:keys:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-public-keys-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/keys/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🔑 **KFM — Release Validation Public Keys**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/keys/README.md`

**Purpose**  
This folder is an **optional, release-scoped keyring** containing **public** key material used to verify detached signatures for **v<semver>**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Signatures" src="https://img.shields.io/badge/Signatures-Detached-informational" />
<img alt="Keys Public" src="https://img.shields.io/badge/Keys-Public%20Only-informational" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory exists only when release validation requires a **pinned public key set** to verify:

- detached signature files in `../`,
- and/or signature attestations referenced from `../signatures.index.json`.

Preferred practice is to manage trust roots in governed security locations and reference them.
This directory is for cases where reviewers need a **release-local, immutable** public key snapshot.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/keys/  — Optional release-local public keyring
├── 📄 README.md                                                                                   — This policy/index
├── 🧾 keys.index.json                                                                             — Public key registry (recommended)
├── 🧾 keys.sha256                                                                                 — Optional: sha256 sums for files in this folder
├── 🔑 <signer>.pub                                                                                — Public key (example)
├── 🔑 <signer>.cert.pem                                                                           — Public certificate (optional; example)
└── 🔑 <signer>.pub.sha256                                                                          — Optional per-key digest file (example)
~~~

Notes:

- Filenames are illustrative. Include only what the release produces.
- Keep this folder small. Store only public material needed for verification.

---

## ✅ What is allowed here

Allowed:

- public keys (`.pub`, `.pem`, `.crt`, `.cert.pem`) that are safe to publish,
- a registry describing key identities and intended verification scope,
- optional checksum files for reviewers and CI.

Recommended:

- `keys.index.json` as the authoritative registry for this folder.

---

## ⛔ What is forbidden here (hard rules)

Do NOT commit:

- private keys of any kind (including encrypted private keys),
- key material requiring secrets to decrypt,
- tokens, credentials, access keys,
- signed URLs or internal endpoints,
- restricted identifiers embedded in filenames.

If any of the above is required, store it outside the repo under approved secret management.

---

## 🧾 Recommended registry: `keys.index.json`

The registry enumerates which public keys are acceptable for verifying this release’s signature set.

Illustrative shape:

~~~json
{
  "index_kind": "release_public_keys_index",
  "index_version": "v1",
  "release_version": "v<semver>",
  "release_commit_sha": "<sha>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "keys": [
    {
      "signer_id": "urn:kfm:signer:<...>",
      "key_id": "urn:kfm:key:<...>",
      "public_key_ref": "<signer>.pub",
      "public_key_sha256": "<sha256>",
      "algorithm": "alg:<project-approved>",
      "fingerprint": "<fingerprint-or-thumbprint>",
      "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
      "expires_utc": "YYYY-MM-DDTHH:MM:SSZ",
      "status": "active|retired|revoked",
      "trust_scope": [
        "../signatures.index.json",
        "../../manifests/output_manifest.json"
      ],
      "notes": "Public key pinned for release-local verification."
    }
  ]
}
~~~

Rules:

- Sorting MUST be deterministic (stable sort by `signer_id`, then `key_id`).
- `public_key_sha256` MUST match the exact bytes of the referenced public key file.
- Use stable identifiers (`urn:kfm:...`) for keys and signers where possible.

---

## 🔍 Verification posture (tool-agnostic)

Verification is always a two-step check:

1. **Digest check**
   - Compute `sha256(public_key_file)` and confirm it matches `keys.index.json`.

2. **Signature verification**
   - Use the project-approved verification scheme and the pinned public key to verify detached signatures in `../`.

If either check fails:

- treat signatures as untrusted,
- fail closed unless a governed override is recorded with signed justification.

---

## 🔄 Rotation and retirement rules

To keep verification durable across time:

- New keys SHOULD be introduced before old keys expire.
- Old keys MAY be retained to verify historical releases.
- Revocation MUST be explicit:
  - set `status = "revoked"` in `keys.index.json`,
  - include a revocation note (reason code) without leaking sensitive details,
  - ensure CI blocks new releases from using revoked keys.

Key rotation SHOULD be reviewed under governance, since keys change the trust boundary.

---

## 🎯 Determinism requirements (non-negotiable)

This directory must remain reproducible:

- stable filenames and references,
- stable ordering in registries,
- sha256 checksums for every referenced key file,
- no environment-dependent metadata in committed artifacts.

---

## 🛡️ Governance and FAIR+CARE notes

Key material here is public, but still governed:

- do not embed personal contact information in signer ids,
- do not publish keys that would enable access to restricted infrastructure,
- keep trust scope explicit and minimal.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release-local public key storage; defined allowed contents, registry shape, rotation posture, determinism controls, and verification flow. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Keys Public Only" src="https://img.shields.io/badge/Keys-Public%20Only-informational" />

[⬅ Signatures](../README.md) ·
[🧬 Provenance](../../README.md) ·
[🏷 Release Report](../../../README.md) ·
[🧾 Manifests](../../../manifests/README.md) ·
[📦 Evidence](../../../evidence/README.md) ·
[🏛️ Governance Charter](../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

