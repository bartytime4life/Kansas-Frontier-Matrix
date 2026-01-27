# 🛑 `check-kill-switch` (Composite Action)

![GitHub Action](https://img.shields.io/badge/GitHub%20Action-composite-2ea44f?logo=githubactions&logoColor=white)
![Safety](https://img.shields.io/badge/safety-fail--closed-critical)
![Ops](https://img.shields.io/badge/ops-emergency%20brake-orange)
![KFM](https://img.shields.io/badge/KFM-governance%20gate-blueviolet)

A tiny “emergency brake” for GitHub Actions.  
This composite action checks whether the repo-wide **kill switch** is engaged and—depending on configuration—**halts** the current workflow/job early (hard stop) or **signals** downstream steps/jobs to skip (soft stop).

---

## 🎯 Why this exists

When something is on fire 🔥 (security incident, runaway costs, broken deployment, corrupted data pipelines), you want **one switch** that stops CI/CD consistently across workflows—without editing 15 YAML files under pressure.

Typical reasons to use a kill switch:

- 🧯 **Incident response:** stop deployments / data ingestion immediately
- 💸 **Cost control:** stop expensive workflows temporarily
- 🧪 **Stability:** block known-bad pipeline runs until a fix merges
- 🧭 **Governance:** enforce “fail closed” behavior for critical flows (e.g., provenance-first pipelines)

---

## ✅ Quickstart

> [!IMPORTANT]
> Because this is a **local** action (`uses: ./.github/...`), you **must** checkout the repo first with `actions/checkout`, otherwise the runner won’t have the action’s files.

### 1) Soft stop (recommended for most CI)
Stops *subsequent* steps/jobs (via `if:`), but keeps the job “green” ✅.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: 📦 Checkout
        uses: actions/checkout@v4

      - name: 🛑 Kill switch gate
        id: kill
        uses: ./.github/actions/check-kill-switch

      - name: 🧪 Run tests
        if: steps.kill.outputs.proceed == 'true'
        run: npm test
```

### 2) Hard stop (fail fast) 🚫
Fails the job immediately if the kill switch is engaged.

```yaml
- name: 🛑 Kill switch (hard stop)
  uses: ./.github/actions/check-kill-switch
  with:
    mode: hard
```

---

## 🧩 What this action checks

This action is designed to support **multiple kill switch sources**, so ops can flip the switch using the fastest available method.

### Precedence (highest → lowest)

1. **Explicit inputs** passed to the action (if supported)
2. **Repository variable** (recommended default)
3. **Kill switch file** in the repo (handy when you want kill state versioned)

> [!NOTE]
> Your exact precedence/inputs are defined in `action.yml`. This README describes the intended contract and recommended usage patterns.

---

## ⚙️ Inputs

| Input | Required | Default | What it does |
|---|---:|---|---|
| `mode` | no | `soft` | `soft` → sets outputs and allows workflow to continue; `hard` → exits non‑zero when engaged |
| `var-name` | no | `KFM_KILL_SWITCH` | Repo variable name to read (values like `true`, `1`, `on`, `enabled` are treated as engaged) |
| `file-path` | no | `.github/kill-switch` | File path to check for kill switch engagement (existence and/or contents, per `action.yml`) |
| `default` | no | `off` | What to do if neither variable nor file is present |

> [!TIP]
> Prefer **repository variables** for the fastest “flip the switch” response. The file-based approach is great when you want the kill switch to be **auditable in git history**.

---

## 📤 Outputs

| Output | Type | Meaning |
|---|---|---|
| `proceed` | `true/false` | `true` means “safe to continue”; `false` means “kill switch engaged, skip downstream work” |
| `engaged` | `true/false` | Alias for whether the kill switch is on |
| `reason` | string | Human-friendly reason (e.g., which source triggered the stop) |
| `source` | string | Where the decision came from (e.g., `var`, `file`, `input`, `default`) |

---

## 🧠 Truthy values (recommended)

When interpreting a variable/file value, these are commonly treated as “ON”:

- `1`, `true`, `yes`, `on`, `enabled`, `engaged`

…and these as “OFF”:

- `0`, `false`, `no`, `off`, `disabled`

If your repo wants stricter semantics, define them explicitly in `action.yml` and keep this README aligned.

---

## 🧪 Usage patterns

### ✅ Gate an entire job (fastest skip)
If you can rely on a repo variable at job start, you can avoid spinning up the whole runner:

```yaml
jobs:
  ingest:
    if: ${{ vars.KFM_KILL_SWITCH != 'true' }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ./pipelines/run_ingestion.sh
```

> [!NOTE]
> The step-based action gate is still valuable for **consistent messaging**, **output-based gating**, and **file-based kill switch** checks.

### 🔁 Gate downstream jobs with `needs`
Use a tiny “gate” job that outputs `proceed`, then block everything else:

```yaml
jobs:
  gate:
    runs-on: ubuntu-latest
    outputs:
      proceed: ${{ steps.kill.outputs.proceed }}
    steps:
      - uses: actions/checkout@v4
      - id: kill
        uses: ./.github/actions/check-kill-switch

  build:
    needs: gate
    if: needs.gate.outputs.proceed == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm test
```

### 🧑‍💻 Allow manual override for `workflow_dispatch`
For urgent debugging, you may want an override:

```yaml
on:
  workflow_dispatch:
    inputs:
      bypassKillSwitch:
        description: "Bypass kill switch (maintainers only)"
        required: false
        default: "false"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - id: kill
        uses: ./.github/actions/check-kill-switch
        with:
          bypass: ${{ inputs.bypassKillSwitch }}
```

(Exact input name/behavior depends on your `action.yml` contract.)

---

## 🧯 Operating the kill switch

### Turn it ON
Pick **one** (depending on how your repo is configured):

- ✅ Set repository variable `KFM_KILL_SWITCH=true`
- ✅ Commit/create `.github/kill-switch` (if file-based kill is enabled)

### Turn it OFF
- Set `KFM_KILL_SWITCH=false` (or delete it), **and/or**
- Remove/clear the `.github/kill-switch` file

---

## 🔐 Security + governance notes

- 🧷 **This is not an access control mechanism.** It’s an operational safety net.
- 🧱 Prefer `mode: hard` for workflows that must **never** run under incident conditions (deployments, prod migrations, irreversible data writes).
- 🧼 Keep the kill switch decision **loud and obvious** in logs (this action should emit `notice`/`warning` messages so failures/skips aren’t mysterious).

---

## 📁 Where this lives

```text
📁 .github/actions/check-kill-switch/
├── action.yml   # 👈 composite action definition (source of truth)
└── README.md    # 📘 you are here
```

---

## 🤝 Contributing

If you adjust kill switch rules (inputs, truthy values, precedence), please update **both**:

- `action.yml` ✅
- this README ✅

That keeps the “operational contract” explicit and prevents surprise behavior during incidents.