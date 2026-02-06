# 🧩 `.github/actions/` — Reusable GitHub Actions for KFM (CI/CD Building Blocks)

<p align="center">
  <img alt="KFM CI/CD" src="https://img.shields.io/badge/KFM-CI%2FCD%20building%20blocks-0b7285?style=for-the-badge" />
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-local%20actions-blue?style=for-the-badge&logo=githubactions&logoColor=white" />
  <img alt="Composite Actions" src="https://img.shields.io/badge/composite-actions%20first-6f42c1?style=for-the-badge" />
  <img alt="Policy as Code" src="https://img.shields.io/badge/policy%20as%20code-OPA%20%2B%20Conftest-111827?style=for-the-badge" />
  <img alt="Security" src="https://img.shields.io/badge/security-least%20privilege-important?style=for-the-badge" />
  <img alt="Supply Chain" src="https://img.shields.io/badge/supply%20chain-SBOM%20%7C%20Provenance%20%7C%20Signatures-2f9e44?style=for-the-badge" />
</p>

> **What this folder is:** KFM’s internal **automation SDK** 🧰  
> A curated library of **reusable, versioned, reviewable** GitHub Actions (typically **composite actions**) used to assemble workflows under:
>
> 📁 `.github/workflows/`

> **What this folder is not:** a dumping ground for one-off YAML snippets 🧯  
> If something is repeated across workflows, it becomes a local action.

---

## 🧭 Table of contents

- [Why local actions?](#-why-local-actions)
- [Quick start](#-quick-start)
- [Folder structure](#-folder-structure)
- [Design principles](#-design-principles)
- [KFM pipeline model](#-kfm-pipeline-model)
- [Security + governance](#-security--governance)
- [Action contract](#-action-contract)
- [Versioning + compatibility](#-versioning--compatibility)
- [Catalog](#-catalog)
- [Create a new action](#-create-a-new-action)
- [Local debugging](#-local-debugging)
- [Related folders](#-related-folders)

---

## 🧠 Why local actions?

Local actions give KFM:

- ✅ **Consistency** across workflows (one setup → many pipelines)
- ✅ **Less copy/paste YAML** (fewer “almost-the-same” drifts)
- ✅ **Easier upgrades** (update once → inherit everywhere)
- ✅ **Governance by design** (policy checks become standard building blocks)
- ✅ **Security defaults** (permissions + secrets hygiene stay centralized)

Think of these as **lego bricks** 🧱 for CI/CD: small, composable, and predictable.

---

## ⚡ Quick start

Example workflow (`.github/workflows/ci.yml`) using a local action:

```yaml
jobs:
  backend:
    runs-on: ubuntu-latest

    # 🔒 Always start from least privilege
    permissions:
      contents: read

    steps:
      - uses: actions/checkout@v4

      # Local action reference 👇 (path is relative to repo root)
      - name: Setup Python + deps
        uses: ./.github/actions/setup-python

      - name: Run tests
        run: pytest -q
```

### ✅ Rule of thumb
If you’ve written the same YAML (or the same bash block) **twice**, it’s time to promote it into `.github/actions/`.

---

## 🗂️ Folder structure

Each action lives in its own folder:

```text
.github/actions/
  README.md                  👈 you are here
  <action-name>/
    action.yml               ✅ required (composite action definition)
    README.md                ✅ required (action-specific docs)
    src/                     (optional) scripts used by the action
    tests/                   (optional) fixtures for policy/lint self-tests
```

### ✅ Naming convention

Keep names:

- `kebab-case`
- **verb-first**
- scoped when helpful (`kfm-*` is encouraged for KFM-specific behavior)

Examples:
- `setup-python`
- `setup-node`
- `docker-build-push`
- `compose-smoke-test`
- `conftest-policy-check`
- `kfm-provenance-check`
- `kfm-sbom-generate`

---

## 🧱 Design principles

Local actions should be:

- **Single responsibility** 🎯  
  One action = one job to do well (setup, test, lint, build, gate, deploy).
- **Deterministic** 🧪  
  Same inputs → same outputs. No hidden “magic”.
- **Composable** 🧩  
  Designed to stack together across workflows.
- **Secure by default** 🛡️  
  Minimal permissions, safe shell settings, no secret leaks.
- **Observable** 🔎  
  Clear logs, clear failures, actionable error messages.
- **KFM-aligned** 🧭  
  KFM treats governance as a first-class feature: CI is part of the trust boundary.

---

## 🧠 KFM pipeline model

KFM CI/CD is not just “build & test.” It’s a **trust pipeline** 🔐:
lint + tests + policy gates + supply chain integrity + deploy controls.

```mermaid
flowchart TD
  A[PR / Push] --> B[Fast Checks<br/>format • lint • unit tests]
  B --> C[Governance Gates<br/>OPA/Conftest • metadata • licensing • AI rules]
  C --> D[Build Artifacts<br/>Docker images • web bundle • SBOM]
  D --> E[Verification<br/>compose smoke • security scans • attestations]
  E --> F{Deploy?}
  F -->|staging| G[Deploy Staging<br/>IaC + env protections]
  F -->|prod (gated)| H[Deploy Prod<br/>Approvals + environments]
```

> 🧠 Mental model: **fail early** and **fail loud**.  
> The closer to “PR opened” we catch issues, the cheaper they are to fix.

---

## 🔒 Security + governance

### 1) Least privilege by default 🛡️

Prefer this baseline in workflows:

```yaml
permissions:
  contents: read
```

Elevate only when required (examples):
- `packages: write` → pushing to GHCR
- `id-token: write` → OIDC cloud auth (preferred)
- `pull-requests: write` → leaving PR comments

### 2) Secrets handling 🔐

Non-negotiables:
- Never echo secrets (even “debugging”)
- Prefer OIDC over long-lived credentials when possible
- Keep deployment secrets in:
  - GitHub Environments
  - GitHub Secrets
  - external secret managers (preferred where possible)

### 3) Policy gates (KFM-style) ✅

KFM uses **policy-as-code** as a core governance mechanism:
- `policy/` is the source of truth
- Conftest/OPA gates should block non-compliant changes
- Policies should fail with **clear** “what + where + how to fix” messages

**What policy gates commonly protect:**
- Missing/invalid metadata (license, provenance, classification)
- Restricted/sensitive data handling rules
- “AI behavior” guardrails (what the system may or may not output/configure)

> 🎯 Goal: a contributor should be able to fix the issue from the CI log alone.

### 4) Supply chain integrity 🧾

Strongly encouraged for build/publish workflows:
- generate SBOMs
- attach build provenance (SLSA-style attestations)
- sign container images (e.g., Cosign) and verify before deploy
- scan dependencies and containers (CI is where we catch it first)

> KFM’s “trust story” doesn’t end at tests—it continues through **artifact integrity**.

---

## ✅ Action contract

Every local action must include:

### Required ✅
- `action.yml`
  - `name`, `description`
  - `runs: using: composite`
  - explicit `inputs` (even if minimal)
  - explicit `outputs` (if the action produces reusable values)
- `README.md` inside the action folder
  - purpose
  - inputs/outputs
  - example usage snippet
  - troubleshooting
  - security notes (permissions/secrets) where applicable

### Recommended ⭐
- a `src/` folder for scripts to keep `action.yml` readable
- safe bash defaults (`set -euo pipefail`)
- consistent logging (see below)

---

## 🔁 Versioning + compatibility

Local actions are referenced by path, so changes propagate immediately. That’s powerful—and dangerous—unless we treat these actions like a public API.

### ✅ Compatibility rules

- **No breaking changes on `main` without a migration plan**
- Prefer additive changes:
  - add optional inputs with defaults
  - add new outputs without changing existing ones
- If breaking changes are necessary, create a new versioned path:
  - `setup-python-v2/`
  - or `setup-python/v2/`

### 🧯 Deprecation policy (recommended)

When you introduce `v2`:
1. keep `v1` working for a grace period
2. mark `v1` as deprecated in its README
3. update workflows gradually
4. remove `v1` only after it is no longer referenced

---

## 📚 Catalog

> ℹ️ Source of truth is the folders in `.github/actions/*/`  
> This catalog is for humans and onboarding.

### 🧰 Action families (recommended taxonomy)

- **Setup actions** (language runtimes, deps, caches)
- **Quality actions** (lint, format, unit/integration tests)
- **Governance actions** (OPA/Conftest gates, metadata checks)
- **Build actions** (Docker, web builds, artifacts)
- **Verification actions** (compose smoke tests, security scans)
- **Deploy actions** (staging/prod steps, environment protections)

<details>
  <summary><strong>📌 Suggested catalog table template</strong> (copy/paste)</summary>

| Action | What it does | Typical jobs | Notes |
|---|---|---|---|
| `setup-python` | Setup Python + install deps | backend CI | Cache wheels where possible |
| `setup-node` | Setup Node + install deps | frontend CI | Use lockfile integrity |
| `conftest-policy-check` | Run Conftest against `policy/` | PR gate | Fail fast with file/rule hints |
| `docker-build-push` | Build + push service images | main merge | Requires `packages: write` |
| `compose-smoke-test` | Bring up stack + healthcheck | pre-deploy | Keep runtime bounded |
| `kfm-sbom-generate` | Generate SBOM | release | Attach to artifacts |
| `kfm-provenance-attest` | Emit provenance | release | For deploy-time verification |

</details>

---

## 🛠️ Create a new action

### 1) Scaffold 📁

```bash
mkdir -p .github/actions/<action-name>/src
touch .github/actions/<action-name>/action.yml
touch .github/actions/<action-name>/README.md
```

### 2) `action.yml` (composite template)

```yaml
name: "<action-name>"
description: "Describe what this action does (1 sentence)."

inputs:
  working-directory:
    description: "Working directory for the action."
    required: false
    default: "."

runs:
  using: "composite"
  steps:
    - name: Do the thing
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: |
        set -euo pipefail
        echo "Hello from <action-name>"
```

### 3) Action README template

<details>
  <summary><strong>🧾 README.md template</strong> (recommended)</summary>

```markdown
# <action-name>

## 🎯 Purpose
What this action does and why it exists.

## ✅ Inputs
| Name | Required | Default | Description |
|---|---:|---|---|
| `working-directory` | no | `.` | Where to run |

## 📤 Outputs
| Name | Description |
|---|---|
| `example` | Example output |

## 🧪 Usage
```yaml
- name: Use <action-name>
  uses: ./.github/actions/<action-name>
  with:
    working-directory: .
```

## 🔒 Security notes
- Required permissions: `contents: read`
- Secrets: none

## 🧯 Troubleshooting
- Common error → likely cause → fix
```

</details>

---

## 🧪 Local debugging

### Run workflows locally (optional) 🧰
If you use `act`, you can simulate many GitHub Actions runs locally.

> ⚠️ Caveat: service containers + networking can differ from GitHub-hosted runners.

### Run policy checks locally ✅
If you have Conftest installed:

```bash
conftest test .
```

Or target specific paths (dataset folders, configs, policies):

```bash
conftest test data/
conftest test policy/
```

### Prefer “thin actions” 🪶
If an action grows too large:
- split into smaller actions
- or move logic into `src/` scripts

---

## ✅ Definition of done

An action is “done” when:

- [ ] ✅ has docs
- [ ] ✅ deterministic output (explicit inputs/outputs)
- [ ] ✅ fails loudly and clearly (actionable errors)
- [ ] ✅ avoids hidden side effects
- [ ] ✅ minimum viable permissions
- [ ] ✅ aligns with KFM governance & trust model

---

## 🔗 Related folders

- 📁 `.github/workflows/` — pipeline definitions that call these actions
- 📁 `policy/` — governance rules (OPA/Rego), validated via Conftest
- 📁 `infra/` / `k8s/` (if present) — deployment & IaC
- 📁 `api/` / `web/` (if present) — service builds + tests + Dockerfiles

---

## 🧾 License / attribution

These local actions are part of the KFM repository and follow the repo’s license and contribution rules.