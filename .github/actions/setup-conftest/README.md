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
> 🧭 **KFM order stays sacred:** **🧰 ETL → 🗂️ STAC/DCAT/PROV catalogs → 🕸️ Neo4j graph → 🔌 APIs → 🌐 UI → 🎬 Story Nodes → 🧠 Focus Mode**
> This action supports the “🧑‍⚖️ policy-as-code” layer that keeps promotion **fail‑closed** and auditable. ✅🧾

---

## 🧾 Action metadata

| Field             | Value                                                                    |
| ----------------- | ------------------------------------------------------------------------ |
| 🧩 Action name    | `kfm/setup-conftest`                                                     |
| 🧱 Type           | Composite Action                                                         |
| 📁 Folder         | `.github/actions/setup-conftest/`                                        |
| 📄 Action file    | `.github/actions/setup-conftest/action.yml` *(contract source of truth)* |
| 📄 This doc       | `.github/actions/setup-conftest/README.md`                               |
| ✅ Status          | Active (spec + operating guide)                                          |
| 🗓️ Last updated  | **2026-01-12**                                                           |
| 🔐 Secrets needed | ❌ none (safe for fork PRs)                                               |
| 🎯 Why it exists  | Standardizes policy toolchain installs across workflows                  |

> [!NOTE]
> KFM expects **validation gates on contributions** (schema validation, provenance completeness, security/governance scans, policy rules) to reject non-compliant changes in CI. This action is one small “toolchain primitive” that keeps those gates consistent. ✅

---

## ⚡ Quick links

| Need                       | Go                                                                                              |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| 🧩 Actions hub             | [`../README.md`](../README.md)                                                                  |
| 🤖 Workflows hub           | [`../../workflows/README.md`](../../workflows/README.md)                                        |
| 🧑‍⚖️ Policy gate action   | [`../policy-gate/README.md`](../policy-gate/README.md)                                          |
| 🧭 Governance scan         | [`../governance-scan/README.md`](../governance-scan/README.md)                                  |
| ✅ Catalog QA               | [`../catalog-qa/README.md`](../catalog-qa/README.md)                                            |
| 🧬 Provenance enforcement  | [`../provenance-guard/README.md`](../provenance-guard/README.md)                                |
| 🧯 Kill switch             | [`../kill-switch/README.md`](../kill-switch/README.md)                                          |
| 🛡️ Security policy        | [`../../../SECURITY.md`](../../../SECURITY.md)                                                  |
| 📘 Master guide (v13)      | [`../../../docs/MASTER_GUIDE_v13.md`](../../../docs/MASTER_GUIDE_v13.md) *(path per v13 draft)* |
| 🧑‍⚖️ Policy source folder | [`../../../tools/validation/policy/`](../../../tools/validation/policy/)                        |

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

* [🎯 What this action does](#-what-this-action-does)
* [🧠 Why KFM needs Conftest](#-why-kfm-needs-conftest)
* [📁 Policy folder layout](#-policy-folder-layout)
* [⚙️ Inputs](#️-inputs)
* [📤 Outputs](#-outputs)
* [✅ Usage patterns](#-usage-patterns)
* [🧪 Local developer usage](#-local-developer-usage)
* [🧩 Target folder shape](#-target-folder-shape)
* [🧯 Troubleshooting](#-troubleshooting)
* [🔐 Security & determinism notes](#-security--determinism-notes)
* [📚 Reference library](#-reference-library)

</details>

---

## 🎯 What this action does

`setup-conftest` is the **toolchain bootstrap** for KFM policy checks.

### ✅ Expected behavior (contract)

* 📥 Downloads and installs a **pinned** version of:

  * 🧪 `conftest` (required)
  * 🧠 `opa` (optional — helpful for debugging and advanced workflows)
* 🧷 Adds the installed binaries to `PATH` (so later steps can run `conftest …`)
* 🧾 Prints tool versions (audit-friendly)
* ♻️ Optionally uses caching to reduce download time
* 🧯 Fails fast on unsupported OS/arch (clear CI failures, no partial installs)

> [!IMPORTANT]
> This action should **not** run policies itself.
> It only installs tools. Policy evaluation belongs in:
>
> * 🧑‍⚖️ `policy-gate`, or
> * a workflow step invoking `conftest test …`

---

## 🧠 Why KFM needs Conftest

KFM is “contract-first + evidence-first”: schemas, catalogs, and provenance define the trust boundary — and CI gates are expected to enforce those invariants automatically. 

Conftest + OPA/Rego enables **policy-as-code** that can enforce meaning beyond schema shape, including:

* 🗂️ **Catalog governance**: link safety, required fields, domain restrictions
* 🧬 **Lineage requirements**: “no mystery artifacts” in promotion lanes
* 🧭 **Governance rules**: FAIR+CARE, sensitive information handling, retention rules
* 🔐 **Supply-chain hygiene**: least-privilege workflows, pinning rules, SBOM presence

KFM’s Latest Ideas explicitly calls for a **Policy Pack using OPA (Rego) + Conftest**, run in CI as a **Policy Gate** that rejects changes violating governance rules, with policies treated as code (versioned, tested) under a dedicated folder like `tools/validation/policy/`. 

---

## 📁 Policy folder layout

KFM policy-as-code is designed to be readable, testable, and extensible.

Recommended shape (matches the “Policy Pack” guidance):

```text
tools/
└─ validation/
   └─ policy/
      ├─ README.md
      ├─ rego/
      │  ├─ common/
      │  │  ├─ helpers.rego
      │  │  ├─ license_allowlist.rego
      │  │  └─ url_allowlist.rego
      │  ├─ catalogs/
      │  │  ├─ stac_required.rego
      │  │  ├─ dcat_required.rego
      │  │  ├─ prov_required.rego
      │  │  └─ link_safety.rego
      │  ├─ governance/
      │  │  ├─ classification_propagation.rego
      │  │  ├─ sensitive_locations.rego
      │  │  └─ attribution.rego
      │  ├─ supply_chain/
      │  │  ├─ workflows_least_privilege.rego
      │  │  └─ actions_pinning.rego
      │  └─ bundles.rego
      ├─ tests/
      │  ├─ *_test.rego
      │  └─ samples/
      │     ├─ good/
      │     └─ bad/
      └─ (optional) conftest config file
```

> [!TIP]
> Keep policies deterministic. Avoid rules that depend on current time, network availability, or runner-specific state.

---

## ⚙️ Inputs

> GitHub Actions inputs are strings. Use `"true"` / `"false"` for booleans.

| Input              | Required | Default   | Meaning                                                                 |
| ------------------ | -------: | --------- | ----------------------------------------------------------------------- |
| `conftest_version` |        ❌ | `0.56.0`  | Conftest version to install *(pin for determinism)*                     |
| `install_opa`      |        ❌ | `"false"` | Install `opa` binary as well                                            |
| `opa_version`      |        ❌ | `0.64.1`  | OPA version when `install_opa=true`                                     |
| `install_jq`       |        ❌ | `"true"`  | Install `jq` for JSON piping *(Linux only)*                             |
| `install_yq`       |        ❌ | `"false"` | Install `yq` for YAML piping *(Linux only)*                             |
| `cache`            |        ❌ | `"true"`  | Cache downloaded binaries in runner cache                               |
| `cache_key_suffix` |        ❌ | `""`      | Optional suffix to bust cache (e.g., `-v2`)                             |
| `verify_checksums` |        ❌ | `"true"`  | Verify downloads with upstream checksums when available *(recommended)* |
| `print_versions`   |        ❌ | `"true"`  | Print tool versions for auditability                                    |

> [!NOTE]
> In hardened promotion lanes, you can move tool installation into a pinned toolchain container and make this action a no-op.
> In PR lanes, downloading pinned versions is usually fine (no secrets required).

---

## 📤 Outputs

| Output             | Meaning                                          |
| ------------------ | ------------------------------------------------ |
| `conftest_path`    | Path to the installed `conftest` binary          |
| `conftest_version` | Installed conftest version                       |
| `opa_path`         | Path to installed `opa` (empty if not installed) |
| `opa_version`      | Installed OPA version (empty if not installed)   |

---

## ✅ Usage patterns

### 1) 🧪 PR lane: run policy tests when governance-relevant paths change

This aligns to the v13 directory expectations for catalog boundary artifacts:

* STAC outputs under `data/stac/**`
* DCAT under `data/catalog/dcat/**`
* PROV under `data/prov/**` 

```yaml
name: Policy (Conftest)

on:
  pull_request:
    paths:
      - "tools/validation/policy/**"
      - "data/stac/**"
      - "data/catalog/dcat/**"
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

      - name: 🧑‍⚖️ Conftest (rego unit tests)
        run: |
          conftest test \
            --policy tools/validation/policy/rego \
            tools/validation/policy/tests

      - name: 🧫 Conftest (samples)
        run: |
          set -euo pipefail
          conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/good
          # Bad samples should fail:
          if conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/bad; then
            echo "ERROR: bad samples unexpectedly passed"
            exit 1
          fi
```

---

### 2) 🚀 Promotion lane: install tooling once, then call `policy-gate` (recommended)

```yaml
steps:
  - uses: actions/checkout@v4

  - name: 🧯 Kill switch
    uses: ./.github/actions/kill-switch
    with:
      scope: publish
      behavior: fail

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
```

---

### 3) 🔐 Supply-chain lane: evaluate workflow hygiene

```bash
conftest test \
  --policy tools/validation/policy/rego \
  .github/workflows
```

---

## 🧪 Local developer usage

If you have Conftest installed locally:

```bash
# Rego unit tests
conftest test --policy tools/validation/policy/rego tools/validation/policy/tests

# Fixture samples
conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/good
conftest test --policy tools/validation/policy/rego tools/validation/policy/tests/samples/bad
```

---

## 🧩 Target folder shape

```text
.github/
└─ actions/
   └─ setup-conftest/
      ├─ action.yml
      └─ README.md   👈 you are here
```

---

## 🧯 Troubleshooting

### “conftest: command not found”

* Ensure the action adds the install directory to `PATH`
* Confirm the job uses a supported runner (recommended: `ubuntu-latest`)

### “Checksum verification failed”

* Verify the requested version exists upstream
* If upstream checksum formats change, you can temporarily set:

  * `verify_checksums: "false"` *(avoid this in promotion lanes)*

### “Policies pass locally but fail in CI”

Common causes:

* different Conftest versions
* CI evaluates **more/other targets** than local
* newline/encoding differences in YAML

Fix:

* pin versions via this action
* keep policy inputs deterministic
* store policy reports as artifacts for review

### “Policy tests are slow”

* tighten `paths:` filters
* keep PR lane tests fast; move heavy checks to nightly/promotion lanes

---

## 🔐 Security & determinism notes

### ✅ Least privilege

This action should run with:

```yaml
permissions:
  contents: read
```

No secrets required (safe for fork PRs).

### ✅ Determinism is the point

* Pin `conftest_version` and `opa_version`
* Prefer checksum verification when available
* Avoid unpinned downloads in hardened lanes

### 🚫 Avoid dangerous workflow patterns

* Avoid `pull_request_target` for policy tooling unless you *fully* understand the risk
* Never run publishing steps on fork PRs
* Treat policy tooling + workflow YAML as **security-sensitive**

---

## 📚 Reference library

This action exists because KFM treats **governance + provenance + supply-chain** as first-class constraints, enforced through deterministic CI gates. 

<details>
<summary><strong>📚 Project files that influence setup-conftest</strong></summary>

### 🧭 Canonical KFM direction (v13)

* `docs/specs/MARKDOWN_GUIDE_v13.md(.gdoc)` — contract-first + deterministic pipeline + validation gates; canonical ordering and catalog boundary artifacts
* `docs/MASTER_GUIDE_v13.md` — master reference path noted in v13 draft guide *(if present in repo)*

### 🧑‍⚖️ Policy Pack direction (OPA/Rego + Conftest)

* `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx` — “Policy Pack” concept, run as CI policy gate; policies treated as versioned, tested code under `tools/validation/policy/`

### 🛡️ Governance & policy enforcement concepts

* `docs/library/Data Spaces.pdf` — policy specification & enforcement framing (background)
* `docs/library/Introduction to Digital Humanism.pdf` — governance & trust framing (background)

</details>

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>
