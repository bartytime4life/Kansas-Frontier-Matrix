<a id="top"></a>

# 🧪🧑‍⚖️ `setup-conftest` — Install Conftest (OPA/Rego) for KFM Policy Gates

[![Composite Action](https://img.shields.io/badge/action-composite-informational)](#-what-this-action-does)
![Policy as Code](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-7c3aed)
![Least Privilege](https://img.shields.io/badge/security-least--privilege-black)
![Fail Closed](https://img.shields.io/badge/gates-fail--closed-important)
![Deterministic](https://img.shields.io/badge/CI-deterministic-success)
![KFM](https://img.shields.io/badge/KFM-provenance--first-6f42c1)

> `setup-conftest` is a **repo-local composite action** that installs **Conftest** (OPA/Rego policy testing) in a **repeatable, pinned, CI-friendly** way.  
> It’s the standard bootstrap for **KFM policy gates** (catalog safety, provenance requirements, governance rules, and supply-chain controls).
>
> 🧭 KFM order stays sacred: **🧰 ETL → 🗂️ Metadata (STAC/DCAT/PROV) → 🕸️ Graph → 🔌 API → 🌐 UI → 🎬 Story Nodes → 🧠 Focus Mode**  
> This action supports the “🧑‍⚖️ policy-as-code” layer that keeps promotion **fail‑closed** and auditable. ✅🧾

---

## 🧾 Action metadata

| Field | Value |
|---|---|
| 🧩 Action name | `kfm/setup-conftest` |
| 🧱 Type | Composite Action |
| 📁 Folder | 📁 `.github/actions/setup-conftest/` |
| 📄 Action file | 📄 `.github/actions/setup-conftest/action.yml` *(expected)* |
| 📄 This doc | 📄 `.github/actions/setup-conftest/README.md` |
| ✅ Status | Active (spec + operating guide) |
| 🗓️ Last updated | **2026-01-10** |
| 🔐 Secrets needed | ❌ none (safe for fork PRs) |
| 🎯 Why it exists | Standardizes policy toolchain installs across workflows |

---

## ⚡ Quick links

| Need | Go |
|---|---|
| 🧩 Actions hub | 📄 [`../README.md`](../README.md) |
| 🤖 Workflows hub | 📄 [`../../workflows/README.md`](../../workflows/README.md) |
| 🧑‍⚖️ Policy gate action | 📄 [`../policy-gate/README.md`](../policy-gate/README.md) |
| 🧭 Governance scan | 📄 [`../governance-scan/README.md`](../governance-scan/README.md) |
| ✅ Catalog QA | 📄 [`../catalog-qa/README.md`](../catalog-qa/README.md) |
| 🧬 Provenance enforcement | 📄 [`../provenance-guard/README.md`](../provenance-guard/README.md) |
| 🛡️ Security policy | 📄 [`../../../SECURITY.md`](../../../SECURITY.md) |
| 🧑‍⚖️ Policy source folder | 📁 `tools/validation/policy/` |

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🎯 What this action does](#-what-this-action-does)
- [🧠 Why KFM needs Conftest](#-why-kfm-needs-conftest)
- [📁 Policy folder layout (KFM standard)](#-policy-folder-layout-kfm-standard)
- [⚙️ Inputs](#️-inputs)
- [📤 Outputs](#-outputs)
- [✅ Usage patterns](#-usage-patterns)
- [🧪 Local developer usage](#-local-developer-usage)
- [🧩 Target folder shape](#-target-folder-shape)
- [🧯 Troubleshooting](#-troubleshooting)
- [🔐 Security & determinism notes](#-security--determinism-notes)
- [📚 Reference library (project files)](#-reference-library-project-files)

</details>

---

## 🎯 What this action does

`setup-conftest` is the **toolchain bootstrap** for policy checks.

### ✅ Expected behavior
- 📥 Downloads and installs a **pinned** version of:
  - 🧪 `conftest` (required)
  - (optional) 🧠 `opa` (helpful for debugging and advanced policy workflows)
- 🧷 Adds the binaries to `PATH`
- 🧾 Prints tool versions (safe, audit-friendly)
- ♻️ Optionally uses caching to reduce download time
- 🧯 Fails fast on unsupported OS/arch (so CI fails clearly)

> [!IMPORTANT]
> This action should **not** run policies itself.  
> It only installs the tools. Policy evaluation belongs in:
> - 🧑‍⚖️ `policy-gate` action, or
> - a workflow step invoking `conftest test ...`

---

## 🧠 Why KFM needs Conftest

KFM’s “what ships” isn’t just code—it's **data catalogs**, **provenance**, **stories**, and **release artifacts**.

Conftest + OPA lets us write policy rules that can validate:
- 🗂️ **Catalog contracts**: STAC/DCAT required fields, link safety, schema profiles
- 🧬 **Lineage rules**: PROV required for promoted artifacts; provenance presence in promotion lanes
- 🧭 **Governance**: classification propagation; sensitive locations redaction; attribution completeness
- 🔐 **Supply chain**: least-privilege workflows; action pinning; SBOM presence and digest pinning (promotion lanes)

It keeps the repo “boring and safe” at scale by making gates:
- ✅ machine-checkable  
- ✅ repeatable  
- ✅ diffable  
- ✅ fail‑closed  

---

## 📁 Policy folder layout (KFM standard)

KFM policy-as-code is organized so it stays readable, testable, and extensible:

```text
📁 tools/
└─ ✅📁 validation/
   └─ 🧑‍⚖️📁 policy/
      ├─ 📄 README.md
      ├─ 🧠📁 rego/
      │  ├─ 🧰📁 common/
      │  │  ├─ 🧩 helpers.rego
      │  │  ├─ 🧾 license_allowlist.rego
      │  │  └─ 🔗 url_allowlist.rego
      │  ├─ 🗂️📁 catalogs/
      │  │  ├─ 🛰️ stac_required.rego
      │  │  ├─ 🗃️ dcat_required.rego
      │  │  ├─ 🧬 prov_required.rego
      │  │  └─ 🛡️ link_safety.rego
      │  ├─ 🧭📁 governance/
      │  │  ├─ 🧬 classification_propagation.rego
      │  │  ├─ 🗺️ sensitive_locations.rego
      │  │  └─ 🏷️ attribution.rego
      │  ├─ 🔐📁 supply_chain/
      │  │  ├─ 🧷 workflows_least_privilege.rego
      │  │  └─ 📌 actions_pinning.rego
      │  └─ 📦 bundles.rego
      └─ 🧪📁 tests/
         ├─ 🧪 *_test.rego
         └─ 🧫📁 samples/
            ├─ ✅📁 good/
            └─ ❌📁 bad/
```

> [!TIP]
> Your workflows should treat policy as a **first-class contract**:
> - add unit tests (`*_test.rego`)
> - keep sample inputs (`samples/good` + `samples/bad`)
> - run Conftest in PR lanes when policy-relevant paths change

---

## ⚙️ Inputs

> GitHub Actions inputs are strings. Use `"true"` / `"false"` for booleans.

| Input | Required | Default | Meaning |
|---|---:|---|---|
| `conftest_version` | ❌ | `0.56.0` | Conftest version to install *(pin for determinism)* |
| `install_opa` | ❌ | `"false"` | Install `opa` binary as well |
| `opa_version` | ❌ | `0.64.1` | OPA version when `install_opa=true` |
| `install_jq` | ❌ | `"true"` | Install `jq` for JSON piping (Linux only) |
| `install_yq` | ❌ | `"false"` | Install `yq` for YAML piping (Linux only) |
| `cache` | ❌ | `"true"` | Cache downloaded binaries in runner cache |
| `cache_key_suffix` | ❌ | `""` | Optional suffix to bust cache (e.g., `-v2`) |
| `verify_checksums` | ❌ | `"true"` | Verify downloaded artifacts with release checksums (recommended) |
| `print_versions` | ❌ | `"true"` | Print `conftest --version` (and `opa version` if installed) |

> [!NOTE]
> If your repo uses a pinned toolchain container for promotion lanes, you may disable downloads entirely and make this action a no-op in that lane.  
> For PR lanes, downloading pinned versions is usually fine.

---

## 📤 Outputs

| Output | Meaning |
|---|---|
| `conftest_path` | Path to the installed `conftest` binary |
| `conftest_version` | Installed conftest version |
| `opa_path` | Path to installed `opa` (empty if not installed) |
| `opa_version` | Installed OPA version (empty if not installed) |

---

## ✅ Usage patterns

### 1) 🧪 PR lane: run policy tests only when relevant paths change

```yaml
name: Policy (Conftest)

on:
  pull_request:
    paths:
      - "tools/validation/policy/**"
      - "data/catalog/**"
      - "data/prov/**"
      - ".github/workflows/**"
      - ".github/actions/**"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  policy:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v4

      - name: 🧪 Setup Conftest
        uses: ./.github/actions/setup-conftest
        with:
          conftest_version: "0.56.0"
          install_opa: "false"

      - name: 🧑‍⚖️ Conftest (unit tests)
        run: |
          conftest test \
            --policy tools/validation/policy/rego \
            tools/validation/policy/tests

      - name: 🧫 Conftest (samples — good must pass, bad must fail)
        run: |
          set -euo pipefail
          conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/good
          # For bad samples, you might invert expected behavior in a scripted harness.
```

### 2) 🚀 Promotion lane: call policy-gate (recommended)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧪 Setup Conftest
    uses: ./.github/actions/setup-conftest
    with:
      conftest_version: "0.56.0"
      install_opa: "true"
      opa_version: "0.64.1"

  - name: 🧑‍⚖️ Policy gate (fail closed)
    uses: ./.github/actions/policy-gate
    with:
      fail_on_warn: "true"
      mode: promotion
```

### 3) 🔐 Supply-chain lane: evaluate workflow hygiene
Useful when `.github/workflows/**` or `.github/actions/**` changes:

```bash
conftest test \
  --policy tools/validation/policy/rego \
  .github/workflows
```

> 📌 This is where rules like:
> - 🧷 `workflows_least_privilege.rego`
> - 📌 `actions_pinning.rego`  
> help prevent unsafe CI drift.

---

## 🧪 Local developer usage

If you have Conftest installed locally:

```bash
# 1) Run rego unit tests
conftest test --policy tools/validation/policy/rego tools/validation/policy/tests

# 2) Run sample fixtures
conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/good
conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/bad
```

> [!TIP]
> If you want local parity with CI, add a tiny Make target:
> - `make policy-test`
> - `make policy-samples`

---

## 🧩 Target folder shape

```text
📁 .github/
└─ 🧩📁 actions/
   └─ 🧪📁 setup-conftest/
      ├─ 📄 action.yml
      └─ 📄 README.md   👈 you are here
```

---

## 🧯 Troubleshooting

### “conftest: command not found”
- Ensure the action added the tool directory to `PATH`
- Ensure the job runs on a supported runner (recommended: `ubuntu-latest`)

### “Checksum verification failed”
- Verify the requested version exists upstream
- If upstream checksum formats change, temporarily set:
  - `verify_checksums: "false"` *(not recommended for promotion lanes)*

### “Policies pass locally but fail in CI”
Common causes:
- different Conftest/OPA versions
- inputs differ (CI evaluates a generated JSON report, local uses raw files)
- newline/encoding differences in YAML

Fix:
- pin versions via this action
- keep policy inputs deterministic (generate `reports/gates.json` in CI and store it)

### “Policy tests are slow”
- use `paths:` filters to run only when relevant files change
- keep PR lane tests fast; move heavy checks to nightly/promotion lanes

---

## 🔐 Security & determinism notes

### ✅ Least privilege
This action should run with:

```yaml
permissions:
  contents: read
```

No secrets required.

### ✅ Determinism is the point
- Pin `conftest_version` and `opa_version`
- Prefer checksum verification
- Avoid unpinned downloads in promotion lanes

### 🚫 Avoid dangerous workflow patterns
- avoid `pull_request_target` for policy tooling unless you *really* understand the risk
- never run publishing steps on fork PRs
- treat policy tooling + workflow YAML as **security-sensitive**

---

## 📚 Reference library (project files)

This action exists because KFM treats **governance + provenance + supply-chain** as first-class constraints.

<details>
<summary><strong>📚 Project files that influence setup-conftest</strong></summary>

### 🧭 Canonical KFM direction
- 📄 `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- 📄 `docs/specs/MARKDOWN_GUIDE_v13.md(.gdoc)`
- 📄 `docs/specs/Latest Ideas.pdf`

### 🛡️ Security posture and supply-chain mindset
- 📄 `SECURITY.md`
- 📄 `docs/library/ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` *(defense mindset)*
- 📄 `docs/library/Data Spaces.pdf` *(classification + access thinking)*

### 🧪 Why “policy gates” matter (integrity + reproducibility)
- 📄 `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- 📄 `docs/library/Understanding Statistics & Experimental Design.pdf`

</details>

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>

