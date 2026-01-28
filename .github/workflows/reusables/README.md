# ♻️ Reusable GitHub Actions Workflows (KFM)

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-workflow_call-2088FF?logo=githubactions&logoColor=white)
![KFM](https://img.shields.io/badge/KFM-governed%20CI-6f42c1?logo=github&logoColor=white)
![Fail Closed](https://img.shields.io/badge/policy-fail--closed-111827)

📍 **Path:** `.github/workflows/reusables/README.md` *(you are here)*

---

## 🧭 Critical GitHub constraint (read this first)

> ⚠️ **GitHub Actions requires workflow YAML files to live directly in** `.github/workflows/`  
> ✅ **Subdirectories are not supported for workflow files** — including reusable workflows.  
>
> **So this folder (`.github/workflows/reusables/`) is for:**
> - 📚 documentation & runbooks
> - 🧩 workflow “contracts” (inputs/secrets/outputs) and conventions
> - 🧪 templates / design notes
>
> **Actual reusable workflows must be placed at:**
> - ✅ `.github/workflows/<name>.yml` with `on: workflow_call`
>
> **If you want reusable logic in subfolders, use composite actions instead:**
> - ✅ `.github/actions/<action-name>/action.yml` *(step-level reuse)*

Reference: GitHub Docs → “Reuse workflows” (subdirectories not supported):  
`https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows`

---

## 📦 What “reusables” means in KFM

KFM uses CI/CD as a **governance enforcement layer**:
- ✅ **Fail closed** by default (if a check fails, merge is blocked)
- ✅ **Evidence/provenance-first** (metadata + lineage before interpretation)
- ✅ **Pipeline invariant enforcement** (ETL → catalogs → graph → API → UI → narratives)

Reusable workflows are how we keep those rules **consistent** across:
- Pull Requests (PR gates)
- Scheduled validation runs
- Releases (signed artifacts / attestations)
- Domain-module onboarding (new datasets, new schemas)

---

## 🗂️ Expected layout (recommended)

Even though we can’t nest workflow YAML files, we *can* keep them organized with naming + this index.

```text
📁 .github/
└── 📁 workflows/
    ├── 📄 ci.yml                          # PR entrypoint (calls reusable workflows)
    ├── 📄 release.yml                     # release entrypoint (calls reusable workflows)
    ├── 📄 kfm__docs__validate.yml          # ♻️ reusable (workflow_call)
    ├── 📄 kfm__metadata__validate.yml      # ♻️ reusable (workflow_call)
    ├── 📄 kfm__api__contract_tests.yml     # ♻️ reusable (workflow_call)
    ├── 📄 kfm__security__governance.yml    # ♻️ reusable (workflow_call)
    └── 📁 reusables/
        └── 📄 README.md                   # 📍 this doc (index + rules)
```

---

## 🔁 How to call a reusable workflow (local)

Reusable workflows are called **at the job level** via `uses:`.

```yaml
jobs:
  docs-gate:
    name: 🧾 Docs Gate
    uses: ./.github/workflows/kfm__docs__validate.yml
    with:
      changed_only: true
    secrets: inherit
```

### 🌍 Cross-repo calls (shared org patterns)

```yaml
jobs:
  security-gate:
    uses: my-org/kansas-frontier-matrix/.github/workflows/kfm__security__governance.yml@v13.0.0
    with:
      severity_threshold: high
    secrets: inherit
```

> 💡 **Tip:** Use tags/releases for “stable contracts” (`@v13.0.0`).  
> For maximum security, pin to a commit SHA.

---

## 🧾 Workflow contract conventions (KFM standard)

Reusable workflows are “mini APIs”. Treat them like **contract artifacts**.

### ✅ File naming

Pick one pattern and stick to it:

- `kfm__<subsystem>__<verb>.yml` (recommended)
  - Example: `kfm__metadata__validate.yml`
- OR `kfm-<subsystem>-<verb>.yml`

### 🧩 Inputs

- All inputs must be:
  - documented here (or in a sibling doc)
  - typed (string/boolean/number)
  - have safe defaults where possible

Example pattern:

```yaml
on:
  workflow_call:
    inputs:
      changed_only:
        description: "Validate only files changed in the calling workflow context"
        required: false
        type: boolean
        default: true
```

### 🔐 Secrets

- Prefer `secrets: inherit` for internal calls
- Never echo secrets to logs
- Keep secret names stable (breaking secret names is a breaking change)

```yaml
on:
  workflow_call:
    secrets:
      KFM_DEPLOY_TOKEN:
        required: false
```

### 📤 Outputs

Outputs should be:
- stable
- documented
- intentionally minimal

Example:

```yaml
on:
  workflow_call:
    outputs:
      report_artifact_name:
        description: "Artifact name containing validation output"
        value: ${{ jobs.validate.outputs.report_artifact_name }}
```

---

## 🔐 Security defaults (non-negotiable vibes 🔒)

- ✅ Prefer **least-privilege** `permissions:` in every workflow
- ✅ Avoid `pull_request_target` unless you *really* know why (secrets exposure risk)
- ✅ Pin third-party actions (at least to a major version; ideally commit SHA)
- ✅ Use `timeout-minutes:` for long-running jobs
- ✅ Use `concurrency:` for expensive pipelines (avoid stampedes)

Example baseline:

```yaml
permissions:
  contents: read

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---

## ✅ KFM CI Gates (recommended reusable workflow set)

These mirror KFM’s “minimum gates” philosophy and keep PRs **governed**.

| Gate 🧱 | What it enforces | Typical artifacts 📦 |
|---|---|---|
| 🧾 Docs validation | Markdown front-matter + required sections + link checks | linkcheck report |
| 🧬 Metadata validation | STAC/DCAT/PROV schema checks | schema validation report |
| 🕸️ Graph integrity | Neo4j fixture constraints + ontology rules | test logs |
| 🔌 API contract tests | OpenAPI/GraphQL lint + contract fixtures | junit / coverage |
| 🛡️ Security & governance | secrets scan + PII/sensitive content + classification propagation | scan reports |
| 🏷️ Release hardening | SBOM + provenance attestations + signing | release bundles |

> 🧠 KFM principle: **“If it’s not validated, it’s not real.”**  
> Gates aren’t bureaucracy — they’re how we keep the knowledge base trustworthy.

---

## 🧪 Add a new reusable workflow (checklist ✅)

### 1) Create the workflow at top-level
✅ `.github/workflows/kfm__<area>__<name>.yml`  
*(Do not place workflow YAML in this folder.)*

### 2) Use the reusable trigger
```yaml
on:
  workflow_call:
```

### 3) Declare a strict contract
- inputs
- secrets
- outputs (optional)

### 4) Keep it deterministic
- stable tooling versions
- consistent caching strategy
- idempotent operations where possible

### 5) Document it here 📝
Add an entry to the index below.

---

## 🗃️ Reusable workflow index (fill this in as you add them)

> ✅ Keep this list current so maintainers can quickly see what CI building blocks exist.

| Workflow file (in `.github/workflows/`) | Purpose | Key inputs | Secrets |
|---|---|---|---|
| `kfm__docs__validate.yml` | Docs front-matter + link checks | `changed_only` | *(none)* |
| `kfm__metadata__validate.yml` | STAC/DCAT/PROV schema validation | `domain`, `changed_only` | *(none)* |
| `kfm__api__contract_tests.yml` | Contract lint + tests | `api_version` | *(optional)* |
| `kfm__security__governance.yml` | Secrets/PII/classification checks | `severity_threshold` | *(optional)* |
| `kfm__release__bundle.yml` | SBOM + attestations + packaging | `tag` | `KFM_SIGNING_KEY` |

*(Replace/expand as your repo matures.)*

---

## 🧰 Troubleshooting (fast fixes)

<details>
<summary><strong>❌ “workflows must be defined at the top level of the .github/workflows directory”</strong></summary>

You’re trying to `uses:` a workflow stored in a subfolder (like `.github/workflows/reusables/...`).  
✅ Move the workflow file to `.github/workflows/` and call it from there.

</details>

<details>
<summary><strong>❌ Secrets missing in reusable workflow</strong></summary>

- Ensure the caller passes `secrets: inherit` (or specific secrets)
- Ensure `workflow_call.secrets` declares the secret (if you want to be explicit)

</details>

<details>
<summary><strong>❌ Reusable workflow can’t see PR changed files</strong></summary>

Use `actions/checkout` in the called workflow (reusable workflows don’t magically have code checked out).

</details>

---

## 🔗 Related KFM docs (repo-internal)

These are the “why” behind the gates:

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline & invariants
- ⚖️ `docs/governance/ROOT_GOVERNANCE.md` — review gates + policies
- 🧬 `docs/standards/` — STAC/DCAT/PROV profiles and schemas
- 🧾 `docs/templates/` — governed templates (docs, Story Nodes, API extensions)

---

## 🧭 Maintainer note

Keep CI reusable workflows boring, predictable, and well-documented 😄  
KFM’s trust comes from repeatable validation — not clever YAML tricks.
