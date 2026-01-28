# 🧪 `setup-conftest` (local GitHub Action)

![Type](https://img.shields.io/badge/action-composite-2ea44f?logo=githubactions&logoColor=white)
![Tool](https://img.shields.io/badge/tool-conftest-1f6feb?logo=opensourceinitiative&logoColor=white)
![Policy](https://img.shields.io/badge/policy-OPA%20(Rego)-111827?logo=openpolicyagent&logoColor=white)

> ✅ Installs **Conftest** and adds it to `PATH` so your workflows can run policy tests against YAML/JSON/HCL (Kubernetes, Terraform, Helm output, etc.).  
> 📌 This is a **local** action (lives in your repo), so you reference it with `uses: ./.github/actions/setup-conftest`.

---

<details>
<summary>🧭 Table of contents</summary>

- [✨ What this action does](#-what-this-action-does)
- [📦 Inputs](#-inputs)
- [📤 Outputs](#-outputs)
- [🚀 Quick start](#-quick-start)
- [🧩 Example workflows](#-example-workflows)
- [🔒 Security & reproducibility](#-security--reproducibility)
- [🧯 Troubleshooting](#-troubleshooting)
- [📁 Location](#-location)

</details>

---

## ✨ What this action does

- 📥 Downloads a specified **Conftest** release (or resolves `latest`, if supported by the action)
- 🧰 Makes `conftest` available on the runner via `PATH`
- ⚡ Optionally leverages caching (if implemented in `action.yml`)
- 🧾 Optionally exposes outputs like installed version / install path (if implemented)

> [!NOTE]
> The **source of truth** for inputs/outputs is the action’s `action.yml`.  
> This README documents the **intended interface**—keep it in sync if you change the action.

---

## 📦 Inputs

> [!TIP]
> If you prefer ultra-stable pipelines, **pin a version** (e.g., `0.51.0`) instead of using `latest`.

| Input | Description | Required | Default |
|------|-------------|----------|---------|
| `version` | Conftest version to install (e.g., `0.51.0`). Some implementations also accept `latest`. | ❌ | `latest` |
| `github-token` | Token used when resolving `latest` via GitHub API (helps avoid rate limits). | ❌ | `${{ github.token }}` |
| `cache` | Enables caching of the downloaded binary (if supported by this action). | ❌ | `true` |
| `install-dir` | Directory to place the `conftest` binary (if supported). | ❌ | action-defined |

> [!IMPORTANT]
> If your `action.yml` does **not** define one of the inputs above, remove it from this table (or update the action to match).

---

## 📤 Outputs

| Output | Description |
|--------|-------------|
| `version` | The installed Conftest version (if emitted by the action). |
| `path` | Absolute path to the `conftest` binary (if emitted by the action). |

---

## 🚀 Quick start

### ✅ Minimal (install + verify)

```yaml
- name: 🧪 Setup Conftest
  uses: ./.github/actions/setup-conftest
  with:
    version: "0.51.0"

- name: 🔎 Verify
  run: conftest --version
```

---

## 🧩 Example workflows

### 1) 🧯 Test Kubernetes manifests (YAML)

Assumes you keep Rego policies in `policy/` and manifests in `k8s/`.

```yaml
name: Policy Checks (Conftest)

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  conftest:
    runs-on: ubuntu-latest
    steps:
      - name: 📦 Checkout
        uses: actions/checkout@v4

      - name: 🧪 Setup Conftest
        uses: ./.github/actions/setup-conftest
        with:
          version: "0.51.0"

      - name: ✅ Run policy tests
        run: |
          conftest test ./k8s \
            --policy ./policy \
            --all-namespaces
```

### 2) 🏗️ Test Terraform plans (JSON)

Conftest works great against a Terraform plan exported as JSON.

```yaml
- name: 🧪 Setup Conftest
  uses: ./.github/actions/setup-conftest
  with:
    version: "0.51.0"

- name: 🧾 Terraform plan → JSON
  run: |
    terraform init -input=false
    terraform plan -out=tfplan -input=false
    terraform show -json tfplan > tfplan.json

- name: ✅ Conftest policy test
  run: |
    conftest test tfplan.json --policy ./policy
```

### 3) 🧠 “Latest” version (if supported)

```yaml
- name: 🧪 Setup Conftest (latest)
  uses: ./.github/actions/setup-conftest
  with:
    version: "latest"
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

> [!TIP]
> If you hit GitHub API rate limits, pin a version or pass a token with higher limits.

---

## 🔒 Security & reproducibility

- 📌 **Pin versions** for predictable CI results (`version: "0.51.0"`).
- 🧾 If your action supports it, verify release integrity (e.g., `sha256`) before executing binaries.
- 🧰 Prefer running policy tests as part of **PR checks** so non-compliant config never lands on `main`.

---

## 🧯 Troubleshooting

### `conftest: command not found`
- ✅ Ensure the step uses the **local** path:
  - `uses: ./.github/actions/setup-conftest`
- ✅ Ensure the setup step runs **before** any `conftest` commands.
- ✅ If your action installs into a custom directory, confirm it also updates `PATH`.

### `latest` fails / rate limited
- ✅ Pin a version (`0.51.0`)
- ✅ Provide `github-token` (if your action resolves latest via GitHub API)

### Policies not being picked up
- ✅ Confirm your policy path:
  - `--policy ./policy`
- ✅ Confirm you’re testing the correct files/folders:
  - `conftest test ./k8s`

---

## 📁 Location

```text
.github/ 🧩
└─ actions/ 🛠️
   └─ setup-conftest/ 🧪
      ├─ action.yml ⚙️
      └─ README.md 📘
```

---

## 🧾 Related links

- 🔍 Conftest (policy testing for config): https://www.conftest.dev/
- 🧠 Open Policy Agent (Rego): https://www.openpolicyagent.org/

> [!NOTE]
> Links are included for convenience; this repo’s policies and conventions should live in your own `/policy` folder. ✅
