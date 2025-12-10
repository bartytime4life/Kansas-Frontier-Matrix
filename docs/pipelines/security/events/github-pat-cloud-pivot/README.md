---
title: "🛡️ GitHub PAT Compromise → Cloud Control Plane Attack Vector (KFM Security Event Brief)"
path: "docs/security/events/github-pat-cloud-pivot/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & Supply Chain Council"
content_stability: "stable"

doc_kind: "Security Event Brief"
status: "Active"
intent: "security-threat-analysis"
semantic_document_id: "kfm-doc-security-github-pat-cloud-pivot-v11.2.6"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

header_profile: "standard"
footer_profile: "standard"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
telemetry_ref: "../../../releases/v11.2.6/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/security/github-pat-cloud-pivot-v1.json"
---

# 🛡️ GitHub PAT → Cloud Control Plane Pivot  
A Security Event Analysis for KFM v11.2.6

---

## 📘 Overview

This brief documents a validated security pattern in which **compromised GitHub Personal Access Tokens (PATs)** enable attackers to **pivot from source-code access into cloud control-plane compromise**.

The attack chain, first highlighted by external security research and incorporated into KFM’s threat modeling, aligns with concerns in KFM’s **SLSA-aligned supply-chain model** and **Security Policy & Recommendations** around:

- CI/CD trust boundaries  
- inherited secrets in GitHub Actions  
- long-lived credentials  
- opaque workflow execution environments  

KFM classifies this as a **High-Severity Supply-Chain Threat Pattern (HS-SCTP)** within the broader security program.

---

## 🗂️ Directory Layout

~~~text
docs/security/events/github-pat-cloud-pivot/
├── 📄 README.md
├── 📁 examples/
│   ├── 📄 malicious-workflow-injection.yaml
│   ├── 📄 enumeration-patterns.md
│   └── 📁 mitigations/
│       ├── 📄 oidc-migration-guide.md
│       └── 📄 permissions-hardening.md
└── 📁 evidence/
    ├── 📄 attack-patterns.json
    ├── 📁 provenance/
    │   └── 📄 event-provenance.jsonld
    └── 📁 lineage/
        └── 📄 threat-lineage.json
~~~

---

## ⚠️ Threat Summary

### 1. Initial Access via PAT Exposure

Attackers acquire PATs through:

- credential reuse  
- phishing and social engineering  
- leaked tokens in repositories, CI logs, or artifacts  
- compromise of developer endpoints (laptops/CI runners)

Even **read-only** tokens can become stepping stones if workflows or repository permissions are misconfigured (e.g., ability to open PRs that trigger privileged workflows).

---

### 2. Repository Enumeration

Once inside, attackers enumerate the repo and org for:

- `secrets.*` references and secret names  
- workflow definitions and triggers under `.github/workflows/`  
- environment variable names and patterns  
- cloud-credential injection points in deploy stages  

This builds a map of the **CI/CD attack surface** and potential cloud entry points.

---

### 3. Malicious Workflow Injection

If the stolen PAT has **write access** (or indirectly via abused org/team roles), attackers can:

- push modified workflow YAML  
- create new malicious workflows and dispatch them  
- open PRs that auto-execute via misconfigured triggers (`pull_request_target`, broad `repository_dispatch`, unsafe `workflow_run`)

These workflows execute *inside* GitHub’s infrastructure with KFM’s trusted project identity, often inheriting powerful secrets.

---

### 4. Secret Exfiltration → Cloud Pivot

Actions workflows frequently hold:

- cloud API keys and long-lived access tokens  
- cloud service account JSON (GCP/AWS/Azure)  
- Terraform or Pulumi backends and state access  
- privileged deployment tokens and container-registry credentials  

Once exfiltrated, these secrets unlock:

- **IAM privilege escalation** in cloud providers  
- **control-plane modifications** (creating new users, keys, policies)  
- **establishing persistence** via new credentials or backdoors  
- **lateral movement** into other environments (staging/prod, data planes)

The PAT → CI → cloud chain effectively bypasses many perimeter controls.

---

### 5. Persistence & Covering Tracks

To reduce detection likelihood, attackers may:

- delete or hide workflow runs and branches (where permissions allow)  
- re-use legitimate deployment job names to blend into noise  
- operate during expected deployment windows  
- minimize runtime and logs (e.g., short-lived exfil scripts, stdout suppression)

Because workflow logs are often ephemeral and noisy, these patterns can be missed without **dedicated security telemetry and anomaly detection**.

---

## 🔧 Required KFM Mitigations

The following mitigations are **mandatory** for KFM and must be enforced via policy, CI/CD, and org settings.

### 🔹 1. Hard Enforcement of OIDC for CI/CD

Eliminate long-lived static cloud credentials in GitHub:

- Workflows **MUST** obtain cloud access via **short-lived OIDC tokens** exchanged with cloud providers.  
- Cloud roles **MUST** be bound to GitHub identity (repo, environment, branch, etc.), not to PATs.  
- Any residual static secrets for cloud access must be tracked for deprecation and rotated aggressively.

---

### 🔹 2. Mandatory `permissions:` Blocks (Least Privilege)

Every workflow **MUST** declare explicit `permissions:` blocks:

- Default to `permissions: read-all` or narrower; opt-in to `write` on specific scopes only when required.  
- Sensitive scopes (`id-token`, `actions`, `contents:write`, `secrets`) **MUST** be reviewed and justified.  
- CI security checks must fail PRs that add or broaden permissions without Security & Supply Chain Council approval.

---

### 🔹 3. Disallow Dangerous Workflow Dispatch from Forks

- Disable auto-run of privileged workflows for forked PRs.  
- Replace `pull_request_target` and similar risky patterns with **safe, non-privileged validation workflows**.  
- Require explicit, human-in-the-loop approval and environment protections for any workflow that touches production secrets or cloud control-plane resources.

---

### 🔹 4. PAT Scope Limitation & Rotation

All developer PATs that interact with KFM repos must:

- prohibit **write access** to workflow files and protected branches wherever possible  
- be **short-lived** (max 30 days) with enforced rotation  
- be registered and validated against KFM’s **SLSA and security policy profiles**  
- avoid overly broad scopes like `repo` when narrower scopes suffice

Org-level policies should prevent PATs from being required for normal workflows where GitHub Apps or OIDC are viable.

---

### 🔹 5. Secret Minimization in GitHub Actions

KFM workflows must:

- **eliminate cloud master keys** from GitHub Secrets, replacing them with OIDC federation or per-run tokens  
- centralize remaining secrets into internal secret stores with per-execution credentials and strict scoping  
- ensure that any secret exposed to a job is scoped to the **minimal environment** (e.g., environment-only, environment with required branch protections)

---

### 🔹 6. Detection & Telemetry Requirements

Security telemetry must capture at minimum:

- workflow creation, modification, and deletion events  
- changes to repository or org secrets (creation, update, deletion)  
- unusual or high-risk `permissions:` changes  
- OIDC token exchange anomalies (unexpected audiences, elevated roles)  
- abnormal job graph changes (e.g., new fan-out steps doing network egress)

These signals must be wired into the **security-telemetry.json** stream for correlation and alerting.

---

## 🧾 Provenance (PROV-O Excerpt)

Security event documentation for this pattern must include a minimal PROV-O summary:

- `prov:wasDerivedFrom`: external security disclosures and research artifacts  
- `prov:generatedAtTime`: `2025-12-10` (initial codification for KFM v11.2.6)  
- `prov:wasAttributedTo`: KFM Security & Supply Chain Council (as the accountable agent)  
- `prov:Entity`: this README as a security event brief  
- `prov:Activity`: the analysis and internal validation process that generated this brief  
- `prov:Agent`: individual contributors and councils (modeled as `prov:Person` / `prov:Organization`)

This PROV bundle should live under:

- `docs/security/events/github-pat-cloud-pivot/evidence/provenance/event-provenance.jsonld`

and be linked from higher-level security catalogs (DCAT/STAC) as appropriate.

---

## 🕰️ Version History

| Version | Date       | Description                                      |
|--------|------------|--------------------------------------------------|
| v11.2.6 | 2025-12-10 | Initial security event brief added to KFM stack. |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **FAIR+CARE**, and KFM’s security governance policies  
- is governed by the **Security & Supply Chain Council**, with required co-review from the Governance Council for material changes  
- must be updated whenever KFM’s **GitHub, CI/CD, or cloud identity posture** changes in ways that affect this attack path

Edits require approval from the **Security & Supply Chain Council** and must pass `markdown-lint`, `schema-lint`, `footer-check`, and security/secret scans per KFM-MDP test profiles.

<br/>

<sub>© Kansas Frontier Matrix · CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM-MDP v11.2.6</sub>

<br/>

<div align="center">

🛡️ **Kansas Frontier Matrix — GitHub PAT Compromise → Cloud Control Plane Attack Vector (KFM Security Event Brief) v11.2.6**  
Security · Supply Chain Defense · Provenance-Driven CI/CD · FAIR+CARE Aligned  

[📘 Docs Root](../../../README.md) · [🛡️ Security Index](../../README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>