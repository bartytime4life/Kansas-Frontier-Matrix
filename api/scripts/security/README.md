<!-- File: api/scripts/security/README.md -->

# 🔐 KFM API — Security Scripts

![Security](https://img.shields.io/badge/security-hardening-%F0%9F%94%90-success)
![Supply Chain](https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20SLSA-blue)
![Policy Gate](https://img.shields.io/badge/policy%20gate-OPA%20%2B%20Conftest-orange)
![Auditability](https://img.shields.io/badge/auditability-provenance%20first-brightgreen)

This folder contains the **defensive security scripts** used to harden and continuously validate the **KFM API** and its supporting artifacts (dependencies, container images, configs, policies, and governance metadata).

> [!IMPORTANT]
> **Responsible disclosure:** do **not** open public issues for potential vulnerabilities. Follow the repo’s `SECURITY.md` reporting path instead. [oai_citation:0‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

---

<details>
<summary><strong>📚 Table of contents</strong></summary>

- [🧭 Why this folder exists](#-why-this-folder-exists)
- [🧩 What these scripts cover](#-what-these-scripts-cover)
- [📁 Suggested layout](#-suggested-layout)
- [🚀 Quick start](#-quick-start)
- [🛡️ Script catalog](#️-script-catalog)
- [📦 Outputs & artifacts](#-outputs--artifacts)
- [🔒 Policy Gate (FAIR/CARE + security rules)](#-policy-gate-faircare--security-rules)
- [🧾 Supply-chain security (SBOM + SLSA + signing)](#-supply-chain-security-sbom--slsa--signing)
- [🧑‍🤝‍🧑 Auth/RBAC checks](#-authrbac-checks)
- [🧪 API & GraphQL guardrails](#-api--graphql-guardrails)
- [🧯 If a check fails](#-if-a-check-fails)
- [➕ Adding a new security check](#-adding-a-new-security-check)
- [📎 References (project docs that shaped this README)](#-references-project-docs-that-shaped-this-readme)

</details>

---

## 🧭 Why this folder exists

KFM’s documentation explicitly calls out security as part of governance — not only because the API is public-facing, but because KFM aims to be *provable*, *auditable*, and *trustworthy* at the data + code level. [oai_citation:1‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

KFM’s documented security posture emphasizes:

- **Least privilege** everywhere (API, DBs, jobs, secrets). [oai_citation:2‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)
- **Reproducibility + supply-chain security** (verifiable builds, trusted dependencies). [oai_citation:3‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)
- **Data integrity & validation** to reduce poisoning/corruption risk. [oai_citation:4‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)
- **Auditability** (logs + provenance trails for actions and changes). [oai_citation:5‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

These scripts are the “hands” that implement those principles in CI and locally.

---

## 🧩 What these scripts cover

**Core lanes (most repos need all of these):**

1. 🧱 **SCA** — dependency audits & vulnerability checks  
2. 🔎 **Secrets** — scan for leaked credentials/keys/tokens  
3. 🧠 **SAST** — code scanning (Python + JS/TS if applicable)  
4. 📦 **Container** — image scanning + config linting  
5. 🧾 **SBOM + provenance** — generate SBOMs, attach attestations, sign artifacts (planned) [oai_citation:6‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)
6. 📜 **Policy Gate** — enforce governance & security rules via OPA/Conftest (planned) [oai_citation:7‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

**KFM-specific lanes (because this is a geospatial + knowledge graph platform):**

7. 🗂️ **Data governance checks** — FAIR/CARE flags, sensitive-data handling, retention rules [oai_citation:8‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)
8. 🧑‍🤝‍🧑 **RBAC sanity** — Public Viewer / Contributor / Admin behavior matches expectations [oai_citation:9‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)
9. 🧬 **Provenance & audit log integrity** — ensure actions become auditable records (planned) [oai_citation:10‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

---

## 📁 Suggested layout

> If your directory already differs, keep it — but use this as the **contract** for how scripts should behave (outputs, exit codes, artifacts).

```text
api/scripts/security/
├─ README.md
├─ run_all.sh                     # one command to run everything (local + CI-friendly)
├─ config/
│  ├─ severity.thresholds.json    # what fails CI (e.g., HIGH+)
│  └─ tools.versions.json         # pinned tool versions (best effort)
├─ checks/
│  ├─ deps_audit.sh               # pip-audit / npm audit / etc
│  ├─ secrets_scan.sh             # gitleaks / trufflehog
│  ├─ sast_python.sh              # bandit / semgrep
│  ├─ container_scan.sh           # trivy / grype
│  ├─ policy_gate.sh              # conftest (OPA/Rego)
│  ├─ rbac_smoke_test.py          # role + endpoint expectations
│  └─ graphql_guardrails.py       # depth/complexity + schema directive sanity
└─ artifacts/
   ├─ .gitkeep
   └─ (generated per run)/
```

---

## 🚀 Quick start

### 1) Run everything (recommended)
```bash
bash api/scripts/security/run_all.sh
```

### 2) Run a single lane
```bash
bash api/scripts/security/checks/secrets_scan.sh
```

### 3) Keep outputs in one place
```bash
export KFM_SECURITY_OUTDIR="api/scripts/security/artifacts/$(date +%Y%m%d-%H%M%S)"
bash api/scripts/security/run_all.sh
```

> [!NOTE]
> Scripts should be **read-only** by default (scan/validate). If a script can mutate state (e.g., rotate credentials), it must require an explicit `--i-know-what-im-doing` flag and print a loud warning.

---

## 🛡️ Script catalog

| Lane | Goal 🎯 | Typical tools | CI gate? |
|---|---|---:|:---:|
| 🔎 Secrets scan | Prevent leaked keys/tokens in git | gitleaks / trufflehog | ✅ |
| 🧱 Dependency audit | Detect vulnerable packages | pip-audit / npm audit / osv-scanner | ✅ |
| 🧠 SAST | Detect insecure patterns | bandit / semgrep | ✅ |
| 📦 Container scan | CVEs + misconfig | trivy / grype | ✅ |
| 📜 Policy gate | Enforce FAIR/CARE + security rules | OPA + conftest | ✅ |
| 🧑‍🤝‍🧑 RBAC checks | Public vs contributor vs admin | custom smoke tests | ✅ (critical paths) |
| 🧬 Provenance checks | Ensure auditable trail exists | custom validators | ✅ (gradual) |
| 🧠 GraphQL guardrails | Depth/complexity + auth directives | custom validators | ✅ |

> [!TIP]
> A “gate” means **non‑zero exit code** at/above a configured severity threshold (see [Outputs & artifacts](#-outputs--artifacts)).

---

## 📦 Outputs & artifacts

All checks must write:

- **Human-readable logs** (`.txt` or `.log`)
- **Machine-readable results** (`.json`, `.sarif`, `.cyclonedx.json`, etc.)
- A small **run manifest** (so results are provenance-friendly)

### 📄 Suggested run manifest schema (example)
```json
{
  "run_id": "2026-01-12T13:02:33Z__local__abc1234",
  "git_sha": "abc1234",
  "started_at": "2026-01-12T13:02:33Z",
  "finished_at": "2026-01-12T13:04:10Z",
  "checks": [
    {"name": "secrets_scan", "status": "pass", "artifacts": ["gitleaks.sarif"]},
    {"name": "deps_audit", "status": "fail", "severity": "high", "artifacts": ["pip-audit.json"]}
  ]
}
```

> [!NOTE]
> KFM’s “provenance-first” direction expects validation runs to be **traceable** and reproducible, and CI events to be logged as lineage/provenance events where possible. [oai_citation:11‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

---

## 🔒 Policy Gate (FAIR/CARE + security rules)

KFM’s roadmap explicitly describes a **Policy Pack** (OPA/Rego + Conftest) used as a CI gate to enforce governance constraints — including FAIR/CARE and sensitive-data handling rules. [oai_citation:12‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

### What we enforce (examples)
- ✅ Datasets marked **sensitive** must not be publicly exposed
- ✅ Restricted layers must be generalized/aggregated (no sensitive coordinates)
- ✅ Required metadata fields must exist before publish
- ✅ Retention rules: no forbidden data types in public buckets

### Why this matters
This aligns with KFM’s plan to codify data ethics safeguards so they are **not optional** or “reviewer-dependent.” [oai_citation:13‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

---

## 🧾 Supply-chain security (SBOM + SLSA + signing)

KFM’s “Latest Ideas” document describes attaching **SBOMs** and **SLSA-style attestations** to automation/PR outputs, with **Sigstore** signing as part of a detect→validate→promote pipeline. [oai_citation:14‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR) [oai_citation:15‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

### Target outputs (CI-friendly)
- 📦 `sbom.cyclonedx.json`
- 🧾 `provenance.slsa.json`
- ✍️ `signature.sig` (or keyless transparency log proof)

> [!IMPORTANT]
> This README describes the **direction/contract** for supply-chain hardening based on project docs. If the signing/attestation scripts aren’t present yet, treat this section as the blueprint for adding them.

---

## 🧑‍🤝‍🧑 Auth/RBAC checks

KFM is moving toward user accounts with roles such as:

- **Public Viewer**
- **Contributor**
- **Admin** [oai_citation:16‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

Security scripts should include *smoke tests* that ensure:

- public endpoints remain public (no auth regression)
- contributor-only endpoints require auth
- admin-only endpoints reject contributor credentials

### Data classification inspiration (future)
If/when KFM adds stronger data classification, a common model is `Public / Internal / Confidential / Restricted`, with access tied to role. [oai_citation:17‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)

---

## 🧪 API & GraphQL guardrails

The audit notes KFM offers **REST + GraphQL** for flexible retrieval. [oai_citation:18‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

Because GraphQL can be abused (deep queries, high fan-out, inference risks), add guardrails:

- **depth limiting**
- **query complexity budgeting**
- **rate limiting**
- **persisted queries** (optional)
- **auth directive coverage** (schema-level sanity)

### Privacy note: query auditing is a real tool
Query auditing / inference control is a known privacy-defense approach: deny queries that enable disclosure of confidential data. [oai_citation:19‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 🧯 If a check fails

### ✅ Normal failures (dependency CVE, lint, policy gate)
1. Fix the issue (upgrade dependency, adjust config, update policy)
2. Re-run the failing lane locally
3. Commit and open PR with the artifact logs attached (or CI link)

### 🚨 Potential vulnerability / secret leak
1. **Stop** and do not post details publicly
2. Follow `SECURITY.md` / private reporting route [oai_citation:20‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)
3. Rotate exposed credentials ASAP
4. Add a regression test (so it can’t happen again)

---

## ➕ Adding a new security check

### Script contract ✅
All scripts in `checks/` should:

- Support `--help`
- Be non-interactive in CI
- Respect `KFM_SECURITY_OUTDIR`
- Exit non‑zero on configured failure threshold
- Output:
  - `*.log` (human readable)
  - `*.json` or `*.sarif` (machine readable)
  - an entry in the run manifest

### Quality bar
KFM’s wider engineering direction values determinism & reproducibility in pipelines; treat security checks the same way (pinned versions, stable outputs, clear evidence trails). [oai_citation:21‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

---

## 📎 References (project docs that shaped this README)

<details>
<summary><strong>📚 Project sources used</strong></summary>

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  
  Security principles + disclosure expectations. [oai_citation:23‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3) [oai_citation:24‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals   
  RBAC roles, FAIR/CARE policy direction, policy pack, SBOM/SLSA/Sigstore provenance direction. [oai_citation:25‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR) [oai_citation:26‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR) [oai_citation:27‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

- Audit of the Kansas Frontier Matrix (KFM) Repository  [oai_citation:28‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)  
  Notes on documenting threat models & data ethics; mentions REST + GraphQL surface area. [oai_citation:29‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3) [oai_citation:30‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

- Data Spaces (TIKD access control + privacy-preserving logs)  [oai_citation:31‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)  
  Useful patterns for role + classification models and pseudonymized logging. [oai_citation:32‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq) [oai_citation:33‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)

- Data Mining – Concepts and Applications  [oai_citation:34‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
  Query auditing / inference control as privacy defense inspiration. [oai_citation:35‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

</details>
