---
title: "🔏 KFM — Release Validation Signatures (v<semver>) · Verification Notes · Deterministic Provenance Binding"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Verification Guide"
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

intent: "remote-sensing-validation-release-signatures"
audience:
  - "Remote Sensing Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"
  - "Security Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:provenance:signatures:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-provenance-signatures-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/README.md"
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

# 🔏 **KFM — Release Validation Signatures**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/README.md`

**Purpose**  
This folder holds **detached signatures** (and related verification notes) used to bind release validation provenance for **v<semver>** to a verifiable identity and an immutable digest chain.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Provenance" src="https://img.shields.io/badge/Provenance-PROV%20%2B%20OpenLineage-informational" />
<img alt="Signatures" src="https://img.shields.io/badge/Signatures-Detached-informational" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Signatures support:

- **tamper evidence** for release-level manifests and provenance pointers,
- **replay safety** (the same release validation bundle can be verified later),
- **governance auditability** (reviewers can confirm the provenance chain was produced by an approved signer).

This folder SHOULD remain small. Store only detached signatures and minimal verification notes.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/signatures/  — Detached signatures for provenance/manifest artifacts
├── 📄 README.md                                                                              — This policy/index
├── 🧾 signatures.index.json                                                                  — Signature registry (recommended)
├── 🧾 signatures.sha256                                                                      — Optional: sha256 sums for signature files in this folder
├── 🧾 <artifact>.sig                                                                         — Detached signature for <artifact> (example)
├── 🧾 <artifact>.bundle.sig                                                                  — Detached signature for a bundled artifact (example)
└── 📁 keys/                                                                                  — Optional: public keys (ONLY if policy allows)
    ├── 📄 README.md                                                                          — Key provenance and rotation notes
    └── 🧾 <signer>.pub                                                                       — Public key material (example)
~~~

Notes:

- Public keys SHOULD generally be managed in governed security/policy locations; place keys here only if explicitly required and approved.
- Never store private keys or secrets in-repo.

---

## ✅ What should be signed (recommended)

Signatures SHOULD cover release-grade *pointers* and *manifests*, not raw payloads:

- `../provenance.index.json` (if present)
- `../../manifests/input_pack.manifest.json`
- `../../manifests/config_snapshot.json`
- `../../manifests/output_manifest.json`
- `../../evidence/release_evidence_index.json`
- `../../evidence/release_evidence_index.md`
- `../../README.md` (release report summary) (optional, policy-dependent)

If a single “bundle manifest” exists (preferred), sign that bundle manifest and rely on its internal digests.

---

## 🧾 Recommended registry: `signatures.index.json`

Use this file to enumerate signatures and what they cover, without ambiguity.

Illustrative shape:

~~~json
{
  "index_kind": "release_signatures_index",
  "index_version": "v1",
  "release_version": "v<semver>",
  "release_commit_sha": "<sha>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "signatures": [
    {
      "artifact_ref": "../../manifests/output_manifest.json",
      "artifact_sha256": "<sha256>",
      "signature_ref": "output_manifest.json.sig",
      "signature_sha256": "<sha256>",
      "signer_id": "urn:kfm:signer:<...>",
      "signature_scheme": "scheme:<project-approved>",
      "verification_note": "See README.md for verification procedure."
    }
  ]
}
~~~

Rules:

- `artifact_sha256` MUST match the bytes of the artifact being verified.
- Registry ordering MUST be deterministic (stable sort by `artifact_ref`).

---

## 🔍 Verification procedure (generic, tool-agnostic)

Because signature tooling can vary by policy, verification is expressed as a deterministic sequence:

1. **Resolve the artifact**
   - Identify the target artifact path referenced in `signatures.index.json`.

2. **Verify digest first**
   - Compute `sha256(artifact)` and confirm it matches `artifact_sha256`.

3. **Verify detached signature**
   - Verify the signature using the project-approved scheme and trusted public key material.

4. **Record verification**
   - Verification results SHOULD be captured in the release review (CI check output or governance notes), not by rewriting signatures.

If verification fails:

- treat the release evidence as untrusted,
- fail closed unless a governed override is approved and recorded.

---

## 🎯 Determinism requirements (non-negotiable)

All signature registration outputs MUST be reproducible:

- stable artifact paths,
- stable sha256 digests,
- stable serialization for indexes (`signatures.index.json`),
- no environment-specific paths, no signed URLs, no embedded secrets.

---

## 🛡️ Governance and leakage rules (mandatory)

This folder MUST NOT contain:

- private keys, tokens, credentials,
- signed URLs or internal endpoints,
- precise coordinates or restricted location descriptors,
- personal email addresses in signer identifiers (prefer `urn:kfm:signer:<id>`).

If any artifact is sovereignty-restricted, the signature registry may still reference it, but:
- the referenced artifact MUST remain governed and access-controlled,
- the public documentation MUST not leak restricted identifiers.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release validation signature storage; defined directory structure, signature registry expectations, determinism posture, and verification flow. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Signatures Detached" src="https://img.shields.io/badge/Signatures-Detached-informational" />

[⬅ Provenance](../README.md) ·
[🏷 Release Report](../../README.md) ·
[🧾 Manifests](../../manifests/README.md) ·
[📦 Evidence](../../evidence/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

