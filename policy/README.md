# policy/ — KFM Policy-as-Code (OPA/Rego)

🏷️ **governed-doc** · 🏷️ **policy-as-code** · 🏷️ **OPA/Rego** · 🏷️ **CI-gated** · 🏷️ **FAIR+CARE**

> [!IMPORTANT]
> **This directory is governed.** Changes here can affect **data access**, **content redaction**, and **AI/Focus Mode outputs**.
> Treat policy PRs as **high-risk** and ensure review + CI gates are satisfied before merge.

---

## 📘 Overview

### Purpose
This folder contains **KFM policy-as-code** used to:
- Enforce **governance rules** (FAIR + CARE, privacy, sensitive locations, licensing metadata).
- Gate contributions in **CI** (preventing non-compliant data/docs/config from merging).
- Enforce **runtime authorization + redaction** decisions (API + AI output constraints).

### Scope
In-scope for this folder:
- Rego policies (OPA) and supporting policy data (e.g., dataset classification registries).
- Policy tests and examples used by CI and developer workflows.
- Documentation explaining enforcement points, decision contracts, and review gates.

Out-of-scope:
- Application business logic (belongs in service/use-case layer).
- Database access logic (belongs behind repositories/adapters).
- Secrets/credentials (never store in repo, never include in docs).

### Audience
- **Engineers** implementing API/Focus Mode enforcement points.
- **Maintainers & governance reviewers** validating rule intent, fairness, and sensitivity handling.
- **Contributors** running local policy checks before opening PRs.

### Definitions
- **OPA**: Open Policy Agent, a policy decision engine.
- **Rego**: Policy language evaluated by OPA.
- **Policy bundle**: A packaged set of policies + data deployed to OPA/runtime.
- **Decision log**: Audit trail of allow/deny decisions, ideally including policy hash/commit.
- **Redaction**: Policy-directed transformation of outputs (e.g., masking or generalizing sensitive coordinates).

---

## 🗂️ Directory Layout

> [!NOTE]
> Some filenames/directories below are shown as a **recommended structure**. If your repo differs, update this README to match and remove any `*(not confirmed in repo)*` markers.

### Recommended layout (policy/)
```text
policy/
├── README.md                         # This document
├── rego/                             # Rego modules (OPA policies)
│   ├── data_policies.rego            # Dataset governance (license/citation/access) *(not confirmed in repo)*
│   ├── ai_policies.rego              # AI/Focus Mode governance *(not confirmed in repo)*
│   ├── security.rego                 # Access control rules *(not confirmed in repo)*
│   └── compliance.rego               # Regulatory / privacy / takedown rules *(not confirmed in repo)*
├── data/                             # Policy input data (registries used by Rego)
│   ├── datasets.json                 # Dataset registry (ids, accessLevel, ownerGroup, status) *(not confirmed in repo)*
│   └── roles.json                    # Role/group registry *(not confirmed in repo)*
├── tests/                            # Policy tests
│   ├── rego/                         # `opa test` unit tests *(not confirmed in repo)*
│   └── conftest/                     # CI test fixtures *(not confirmed in repo)*
└── examples/                         # Example inputs/outputs for local verification
    ├── input_access.json             # OPA input contract example *(not confirmed in repo)*
    └── output_decision.json          # OPA output contract example *(not confirmed in repo)*
```

---

## 🧭 Context

### Non‑negotiable invariants (KFM-wide)
- **Pipeline order is sacred**: do not bypass the canonical pipeline steps (no UI/database shortcuts, no missing provenance/metadata steps).
- **Trust membrane**: the UI never talks directly to databases; access is mediated via governed APIs/services.
- **Evidence-first + safe-by-default**: avoid uncited assertions, and omit/flag sensitive information when uncertain.
- **No secrets**: never place credentials, API keys, or private tokens in this repo or docs.

### Policy goals (what “good” looks like)
- **Least privilege by default**: deny unless explicit allow.
- **Actionable denials**: every deny should return a clear reason and remediation path.
- **Auditability**: decisions should be reproducible later (policy hash/commit + input context).
- **CARE-aligned controls**: enable authority-to-control, takedown/withdrawal, and safe handling of culturally sensitive data.

---

## 🗺️ Diagrams

### Policy lifecycle (CI + runtime)

```mermaid
flowchart LR
  A[Contributor PR] --> B[CI: Conftest + Policy Checks]
  B -->|pass| C[Merge to main]
  B -->|fail| D[Fix metadata/policy violations]
  C --> E[Build policy bundle]
  E --> F[Deploy runtime (OPA sidecar or embedded)]
  F --> G[API + AI request]
  G --> H[OPA evaluate input]
  H -->|allow| I[Return response]
  H -->|deny| J[Return 403 / refusal]
  H -->|redact| K[Return sanitized output]
  H --> L[Decision log (policy hash/commit)]
```

---

## 📦 Data & Metadata

### Minimum policy-controlled metadata (recommended contract)
Policies commonly depend on dataset/story metadata fields like:

| Field | Type | Example | Why it matters |
|---|---:|---|---|
| `id` | string | `dataset_ks_census_1880` | Stable referent for policy decisions |
| `license` | string | `CC-BY-4.0` | FAIR reuse gate (legal clarity) |
| `citation` | string | `Author, Title, Year...` | Evidence traceability |
| `accessLevel` | string | `Restricted` | Authorization + redaction decisions |
| `ownerGroup` | string | `TribeABC` | CARE Authority-to-Control |
| `status` | string | `active` / `withdrawn` | Takedown/withdraw enforcement |
| `sensitivityTags` | array | `["sacred_site","living_persons"]` | Drives redaction + review gates |

> [!CAUTION]
> If `status = withdrawn`, policies should deny display/use and ensure the UI does not surface the resource.

### Example: FAIR enforcement rule (illustrative)
```rego
# Illustrative only — adapt package/rules to your repo.
package kfm.data

deny[msg] {
  input.dataset.license == ""
  msg := "Dataset missing license (FAIR: Reusable). Add a non-empty license field."
}

deny[msg] {
  input.dataset.citation == ""
  msg := "Dataset missing citation (evidence-first). Add a citation string or dataset reference."
}
```

---

## 🧱 Architecture

### Where policy is enforced

1) **CI (static enforcement)**
- Runs on PRs to prevent merging non-compliant changes.
- Typical failures include missing provenance/metadata or disallowed content patterns.

2) **Runtime (dynamic enforcement)**
- Backend calls OPA before returning:
  - **Dataset access** results (allow/deny/sanitize).
  - **AI/Focus Mode** outputs (block restricted references; refuse disallowed queries; require citations).
- Deployment pattern options:
  - OPA **sidecar** queried via HTTP
  - Embedded OPA evaluation (e.g., WASM/Go library)

### Decision contract (recommended)

#### Input (OPA request)
```json
{
  "subject": {
    "userId": "user123",
    "roles": ["public"],
    "groups": []
  },
  "action": "read",
  "resource": {
    "type": "dataset",
    "id": "dataset456",
    "accessLevel": "Restricted",
    "ownerGroup": "TribeABC",
    "status": "active"
  },
  "context": {
    "channel": "api",
    "endpoint": "/v1/datasets/dataset456",
    "requestedFields": ["geometry", "title", "summary"]
  }
}
```

#### Output (OPA decision)
```json
{
  "allow": false,
  "deny_reason": "Restricted dataset: user not in ownerGroup",
  "redactions": null,
  "policy_ref": {
    "bundle_hash": "<sha256>",
    "commit": "<git_sha>"
  }
}
```

> [!NOTE]
> Prefer returning **structured reasons** (machine-readable codes + human text) so the API/UI can render helpful feedback.

---

## 🧪 Validation & CI/CD

### CI gates (expected)
- ✅ Policy checks via **Conftest** (evaluating repo artifacts against Rego policies)
- ✅ Policy unit tests via `opa test` (if present)
- ✅ Markdown lint / structure checks for governed docs where relevant
- ✅ Sensitivity scans (flag potential leaks requiring review)

### Local workflow (recommended)
1. Run policy tests locally before PR.
2. Confirm any new dataset/story includes required metadata fields (license/citation/provenance).
3. Ensure denial messages are actionable (what failed + how to fix).

#### Example local commands (illustrative)
```bash
# Run policy unit tests (if you have opa tests)
opa test policy/rego -v

# Run Conftest on repo content (paths will vary)
conftest test data/ -p policy/rego
conftest test docs/ -p policy/rego
```

---

## ⚖️ FAIR+CARE & Governance

### CARE-aligned policy behaviors
- **Collective benefit**: refuse or restrict exploitative uses (especially for sensitive cultural data).
- **Authority to control**: enforce `ownerGroup` access; support takedown by setting `status=withdrawn`.
- **Responsibility & ethics**: require warnings/redactions for sensitive narratives; avoid exposing sacred/vulnerable site locations.

### Review gates (recommended minimum)
| Change type | Examples | Required review |
|---|---|---|
| Access control logic | role/group allowlists, `ownerGroup` behavior | Maintainer + Governance reviewer |
| Redaction rules | coordinate rounding/masking, sensitive tags | Governance reviewer |
| AI policy rules | refusal conditions, citation requirements | Maintainer + Governance reviewer |
| FAIR enforcement | required metadata, license compatibility rules | Data steward + Maintainer |
| Compliance/takedown | `withdrawn` behavior, privacy constraints | Governance reviewer |

> [!IMPORTANT]
> The Governance section for any policy change PR should state whether **additional review** is required and why.

### AI assistance disclosure
This document may be drafted or edited with AI assistance, but must remain **project-file grounded** and must not invent repo facts.

---

## 🕰️ Version History

| Version | Date (YYYY-MM-DD) | Summary of Changes | Author |
|---:|---:|---|---|
| v0.1.0 | 2026-02-10 | Initial `policy/README.md` establishing policy-as-code conventions, enforcement points, and review gates. | KFM AI Assistant |