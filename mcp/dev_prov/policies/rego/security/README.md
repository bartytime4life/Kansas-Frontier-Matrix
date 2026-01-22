# 🔐 KFM Security Policy Pack (Rego) — `mcp/dev_prov`

![OPA](https://img.shields.io/badge/OPA-Open%20Policy%20Agent-7B3FE4?logo=openpolicyagent&logoColor=white)
![Rego](https://img.shields.io/badge/Policy-Rego-000000)
![Conftest](https://img.shields.io/badge/CI-Conftest-0B5FFF)
![Sigstore](https://img.shields.io/badge/Supply%20Chain-Sigstore%20%2B%20Cosign-2E7D32)
![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-1F6FEB)

> **Purpose:** This folder is the **security-focused** slice of KFM’s broader “Policy Pack” approach—**policy-as-code** enforcement using **OPA/Rego** + **Conftest** to keep the platform safe, auditable, and provenance-first.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧭 What lives here?

This directory contains **Rego policies** that enforce KFM security requirements across:

- ✅ **CI policy gates** (fail merges when a rule breaks)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- ✅ **Runtime policy checks** (API + AI + export controls consult OPA)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- ✅ **Supply chain integrity** (artifact signatures, digests, OCI packaging expectations)  [oai_citation:4‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- ✅ **Prompt & AI safety controls** (Prompt Gate, leak prevention, tool misuse blocking)  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- ✅ **Sensitive data governance** (classification, redaction, access, “no downgrades”)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

KFM’s overall stance is **fail-closed**: if policy cannot confirm safety/compliance, the gate denies.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🗂️ Recommended layout (inside this folder)

> Keep the repo tree friendly & predictable 🍱

```text
mcp/dev_prov/policies/rego/security/
  README.md
  ├─ packages/
  │   ├─ secrets.rego
  │   ├─ supply_chain.rego
  │   ├─ metadata_security.rego
  │   ├─ sensitive_data.rego
  │   ├─ ai_prompt_security.rego
  │   └─ exports.rego
  ├─ data/
  │   ├─ allowlists/
  │   │   ├─ allowed_licenses.json
  │   │   ├─ secret_false_positives.json
  │   │   └─ trusted_signers.json
  │   └─ schemas/
  │       ├─ governance_card.schema.json
  │       └─ run_manifest.schema.json
  └─ tests/
      ├─ fixtures/
      │   ├─ stac_item.sample.json
      │   ├─ dcat_dataset.sample.json
      │   ├─ prov_activity.sample.json
      │   ├─ run_manifest.sample.json
      │   └─ prompt_event.sample.json
      └─ conftest/
          └─ security_test.sh
```

> Note: KFM’s “main” policy pack is described as living in a repo policy folder (e.g., `tools/validation/policy/*.rego`). This directory is the MCP/dev_prov security subset/mirror.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧱 Policy philosophy (security-first, provenance-first)

### 1) Policy gates everywhere 🚧
KFM uses policy gates during **ingestion**, **AI inference**, and **publication**, with minimum checks including schema, STAC/DCAT/PROV completeness, licenses, sensitivity classification, and provenance completeness.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 2) No “black box” outputs 🧾
- AI answers must include citations; if it can’t cite, it refuses (policy violation).  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- UI/UX should surface provenance and sensitivity cues (e.g., lock icons, warnings).  [oai_citation:15‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### 3) Sensitive data is governed, not guessed 🧠
- Datasets carry **sensitivity classification** (public/sensitive/confidential/etc.) and usage constraints.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Techniques include masking/aggregation (e.g., fuzzing precise locations).  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **No output may be less restricted than its inputs** (sovereignty-aware constraint).  [oai_citation:18‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 4) Supply chain integrity like “code” 🔏
Artifacts can be distributed as **OCI artifacts** with immutable digests, pushed/pulled via **ORAS**, and verified via **Cosign signatures**.  [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
This supports reproducibility + tamper resistance (“content-addressed + signed”).  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 5) Prompt security is a first-class subsystem 🛡️
KFM calls out a dedicated **Prompt Gate** to sanitize inputs and reduce prompt injection / sensitive data leakage risks.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧪 How policies are evaluated

### Option A — Conftest (CI-style)
Conftest runs Rego against repo artifacts and fails the PR if a `deny` fires—this is the core “Policy Pack” workflow.  [oai_citation:23‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

```bash
# Example: evaluate security policies against changed JSON (STAC/DCAT/PROV/manifests)
conftest test \
  --policy mcp/dev_prov/policies/rego/security \
  data/stac/**/*.json data/catalogs/**/*.json data/prov/**/*.json data/audits/**/*.json
```

### Option B — OPA eval (developer loop)
```bash
opa eval \
  --data mcp/dev_prov/policies/rego/security \
  --input ./tests/fixtures/run_manifest.sample.json \
  "data.kfm.security.deny"
```

---

## 🧩 Inputs these policies commonly expect

Security policies typically evaluate **structured evidence artifacts**, including:

- **STAC / DCAT / PROV** metadata triplet (evidence-first publishing)  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Run manifests** (e.g., `data/audits/<run_id>/run_manifest.json`) used as policy-check artifacts  [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Governance card** data (allowed licenses, sensitivity flags, sovereignty flags, etc.)  [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Agent/CI events** (Detect → Validate → Promote pipeline signals)  [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **Prompt events** (Prompt Gate logs, AI response metadata with citations)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

---

## ✅ Security policy categories (what we enforce)

### 🔑 1) Secrets & credential hygiene
- **No secrets in repo** (keys, tokens, credentials) and block PRs that include obvious secrets.  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:32‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Example patterns: AWS keys, JWTs, API keys; allowlist only with review.  [oai_citation:33‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 📦 2) Supply chain controls
- Require OCI artifacts to be:
  - content-addressed (digest pinned)  [oai_citation:34‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
  - signed (Cosign)  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
  - optionally accompanied by SBoM/provenance attestation  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 🧾 3) Metadata security & governance
- Require license presence + allowed license list (FAIR-ready)  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:38‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Require sensitivity classification on relevant datasets (and handling rules)  [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Require provenance completeness (no “unsourced” publishing)  [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🧭 4) Sensitive data handling (CARE + sovereignty)
- Enforce “no downgrade” rule for derivatives.  [oai_citation:41‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Restrict export behavior for sensitive layers unless role/permission satisfied.  [oai_citation:42‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Ensure UI/API behavior matches classification expectations (hide by default / warnings / role gating).  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:44‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### 🤖 5) AI / Prompt security
- Validate “Prompt Gate” compliance metadata (sanitization, injection defense hooks).  [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Enforce “AI outputs must include citations” policy.  [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- (Optional runtime) Block disallowed content or privacy violations before responding.  [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🧰 6) Automation guardrails (agents)
- Agent PRs must follow the same rules (“parity”), and include a **kill-switch** mechanism to halt automation during incident response.  [oai_citation:48‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 🧾 Policy writing conventions (please follow 🙏)

### ✅ Package & entrypoints
Use a consistent namespace:

- `package kfm.security` (top-level)
- submodules: `kfm.security.secrets`, `kfm.security.supply_chain`, etc.

### ✅ Deny-first model (fail closed)
Prefer **`deny[msg]`** rules.

```rego
package kfm.security.secrets

deny[msg] {
  some file
  file := input.files[_]
  re_match("AKIA[0-9A-Z]{16}", file.contents)
  msg := "KFM-SEC-001: Potential AWS access key detected"
}
```

### ✅ Message format
Use stable, greppable codes:

- `KFM-SEC-###` for security violations  
- `KFM-PROV-###` for provenance-specific gates (if reused)  [oai_citation:49‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### ✅ Exceptions are code-reviewed
Add new allowlist entries via PR (no local hacks). This is aligned with “extend vocabularies only via PR” and “fail-closed by default.”  [oai_citation:50‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🔌 Runtime integration notes (OPA beyond CI)

OPA policies can also be consulted at runtime—for example, before an API executes an action or before Focus Mode returns an answer—so governance changes can be applied **without changing app code** (update the policy → enforcement updates everywhere).  [oai_citation:51‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

Typical runtime checks include:

- **Export control**: block sensitive data exports unless allowed.  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **AI response gate**: reject uncited claims or disallowed content.  [oai_citation:53‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:54‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Prompt Gate enforcement**: sanitize + validate prompt events.  [oai_citation:55‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

---

## 🔭 “Defense in depth” (policy + ops)

Policies are one layer; KFM also anticipates operational checks like:

- CI-driven workflows (Detect → Validate → Promote)  [oai_citation:56‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- Security scans (secret scanning, dependency scanning, digest pinning checks)  [oai_citation:57‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Governance-grade auditability (run manifests hashed/canonicalized for stable identity)  [oai_citation:58‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- UI transparency patterns (“map behind the map” provenance and sensitivity visibility)  [oai_citation:59‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  

---

## 📚 References (project truth sources 🧠)

- **Policy Pack (OPA + Conftest), CI + runtime gates**  [oai_citation:60‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:61‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **Automated policy gates + fail-closed**  [oai_citation:62‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Sensitive data classification + masking/aggregation + export controls**  [oai_citation:63‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Security & privacy in intake (no secrets; secure pipelines)**  [oai_citation:64‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Prompt security subsystem (“Prompt Gate”)**  [oai_citation:65‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **OCI + ORAS + Cosign signing and provenance attachments**  [oai_citation:66‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:67‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Run manifests as policy-check artifacts; canonicalization + hashing**  [oai_citation:68‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **UI transparency + provenance surfaced to users**  [oai_citation:69‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- **Data intake governance: provenance-first, STAC/DCAT/PROV evidence triplet**  [oai_citation:70‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Agent parity + kill-switch**  [oai_citation:71‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## ✅ TODO (nice next upgrades ✨)

- [ ] Add `tests/fixtures/` for each policy category (secrets, OCI, sensitivity, AI output)  
- [ ] Add a `make policy-security` target that shells out to Conftest  
- [ ] Add a “policy report” markdown generator for PR comments (list `deny` with codes + remediation tips)  
- [ ] Add an explicit `trusted_signers.json` and enforce Cosign identity/issuer constraints  [oai_citation:72‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
