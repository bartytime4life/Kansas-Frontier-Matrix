<a id="top"></a>

# 🧯 `kill-switch` — Fail‑Closed Circuit Breaker for KFM CI/CD + Agents

![Fail Closed](https://img.shields.io/badge/behavior-fail--closed-critical)
![Composite Action](https://img.shields.io/badge/action-composite-informational)
![Least Privilege](https://img.shields.io/badge/security-least--privilege-black)
![Governed](https://img.shields.io/badge/governance-gated-blueviolet)
![KFM Order](https://img.shields.io/badge/KFM%20order-ETL%E2%86%92Metadata%E2%86%92Graph%E2%86%92API%E2%86%92UI-success)

> **What this is:** a repo‑local composite action that checks KFM kill‑switch signals (repo/env/feature‑flag files) and **halts dangerous lanes** (publish, agents, deploy) *before* they run.  
> **Why:** KFM is a system where **trust > speed**. When something is wrong (incidents, misclassification, broken catalogs, suspected compromise), you need a **single stop button** that’s boring, fast, and auditable. 🧾🔐

---

## 🧾 Action metadata

| Field | Value |
|---|---|
| Path | `.github/actions/kill-switch/README.md` |
| Action ID (suggested) | `kfm/kill-switch` |
| Type | Composite Action |
| Default posture | **Fail‑closed** (stop lanes on signal) |
| Last updated | **2026-01-10** |

---

## ⚡ Quick links

| Need | Go |
|---|---|
| 🧪 Workflows (CI/CD patterns) | [`../../workflows/README.md`](../../workflows/README.md) |
| 🛡️ Security policy | [`../../../SECURITY.md`](../../../SECURITY.md) *(or `../../SECURITY.md` if mirrored)* |
| 🧾 Governance scan action | [`../governance-scan/README.md`](../governance-scan/README.md) *(if present)* |
| ✅ Catalog QA action | [`../catalog-qa/README.md`](../catalog-qa/README.md) *(if present)* |

---

<details>
<summary><strong>📌 Table of contents</strong></summary>

- [🧠 What problem this solves](#-what-problem-this-solves)
- [🧭 Signals this action checks](#-signals-this-action-checks)
- [⚖️ Precedence rules](#️-precedence-rules)
- [🔌 Inputs & outputs](#-inputs--outputs)
- [🚀 Usage patterns](#-usage-patterns)
- [🗂️ Kill‑switch file formats](#️-kill-switch-file-formats)
- [🧯 Incident playbook](#-incident-playbook)
- [🔐 Security & governance notes](#-security--governance-notes)
- [🧰 Troubleshooting](#-troubleshooting)

</details>

---

## 🧠 What problem this solves

KFM workflows cover **code + data + catalogs + provenance + artifacts + (optionally) agents**.

When *any* of the following is true:

- 🔥 a publish lane is producing broken STAC/DCAT/provenance
- 🔐 secrets / credentials are suspected exposed
- 🗺️ sensitive locations risk being published at too‑fine precision
- 📦 artifact integrity checks are failing or supply chain is in doubt
- 🤖 an agent pipeline must stop immediately (Planner/Executor)

…you need an immediate, **centralized** circuit breaker that:
- runs fast (milliseconds)
- uses least privilege (read‑only)
- is auditable (prints *why* it stopped, without leaking secrets)
- is easy to wire into **every workflow** (PR lanes, nightly, release, deploy)

This action is that breaker. 🧯

---

## 🧭 Signals this action checks

This action is designed to support *multiple* “switch sources” so you can stop the system even if one channel is unavailable.

### 1) 🔐 Repo / Environment kill switch (fastest)
A repo secret/variable or workflow `env:` value like:

- `KFM_KILL_SWITCH=true` *(or `1`)*

Used to **pause builds safely** without needing a code change.  
Recommended for emergency response. 🚨

### 2) 🤖 Agent runtime kill switch (W·P·E)
A repo file (governed, reviewable):

- `ops/feature_flags/agents.yml`

Where:
- `enabled: false` disables Planner/Executor immediately (agents stop acting) 🧯

### 3) 🗂️ Optional repo kill switch file (auditable toggles)
If you want a *reviewed* “pause publish” switch (separate from secrets), you can optionally adopt a file like:

- `.kfm/kill-switch.yml` *(recommended by convention — implement if you want it)*

This is helpful when you want the stop state to be:
- visible in PR history
- CODEOWNERS‑protected
- environment‑aware (dev/stage/prod) without secrets churn

> [!NOTE]
> You can adopt **any** repo file location you prefer — this action supports overriding paths via inputs.

---

## ⚖️ Precedence rules

When multiple signals exist, this action resolves them deterministically:

1) **Repo/env kill switch** (`KFM_KILL_SWITCH`)  
2) **Explicit repo kill‑switch file** (e.g., `.kfm/kill-switch.yml`, if configured)  
3) **Agent feature flag** (`ops/feature_flags/agents.yml`) for agent scope

This precedence ensures:
- 🚨 emergency response can override everything immediately
- 🧾 reviewed toggles remain the canonical “normal ops” mechanism
- 🤖 agent safety remains enforceable by a simple feature flag file

---

## 🔌 Inputs & outputs

> Composite actions receive/emit strings. Treat booleans as `"true"` / `"false"`.

### ✅ Inputs (suggested contract)

| Input | Default | Meaning |
|---|---:|---|
| `scope` | `all` | What this check is guarding: `all`, `publish`, `agents`, `deploy` |
| `behavior` | `neutral` | What to do when switch is **ON**: `neutral`, `fail`, `continue` |
| `kill_switch_env` | `KFM_KILL_SWITCH` | Env var / secret name to read |
| `repo_kill_switch_file` | `.kfm/kill-switch.yml` | Optional repo file for audited switch |
| `agents_flag_file` | `ops/feature_flags/agents.yml` | Agent flag file |
| `enabled_values` | `true,1,yes,on` | Values considered “ON” for the env switch |
| `print_summary` | `true` | Print a safe summary (no secrets) |
| `default_if_missing` | `false` | Fail‑closed vs fail‑open when config is missing |

### ✅ Outputs (suggested contract)

| Output | Example | Meaning |
|---|---|---|
| `kill_switch_on` | `true` | Switch is ON for the given scope |
| `kill_switch_source` | `env` / `file` | Which source triggered it |
| `kill_switch_reason` | `maintenance window` | Human readable reason (if provided) |
| `kill_switch_scope` | `publish` | Resolved scope |
| `kill_switch_exit` | `78` / `1` / `0` | The exit code the action used (or would use) |

---

## 🚀 Usage patterns

### Pattern A — Guardrails job (recommended for multi‑job workflows) 🧱

This prevents expensive jobs from even starting.

```yaml
name: Publish Catalogs

on:
  workflow_dispatch:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  guardrails:
    runs-on: ubuntu-latest
    outputs:
      halt: ${{ steps.ks.outputs.kill_switch_on }}
    steps:
      - uses: actions/checkout@v4
      - id: ks
        name: 🧯 Kill switch
        uses: ./.github/actions/kill-switch
        with:
          scope: publish
          behavior: neutral

  publish:
    needs: guardrails
    if: needs.guardrails.outputs.halt != 'true'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - name: 🚀 Promote catalogs
        run: echo "publish steps…"
```

Why this works:
- guardrails are tiny + deterministic
- downstream jobs are hard‑stopped when the switch is ON ✅

---

### Pattern B — Single job early‑exit (good for simple workflows)

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - id: ks
        uses: ./.github/actions/kill-switch
        with:
          scope: all
          behavior: neutral

      - name: 🧪 Run tests
        if: steps.ks.outputs.kill_switch_on != 'true'
        run: pytest -q
```

---

### Pattern C — Agent workflows (W·P·E safety) 🤖🧯

Use the agent feature‑flag file as a hard gate:

```yaml
jobs:
  planner:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - id: ks
        uses: ./.github/actions/kill-switch
        with:
          scope: agents
          behavior: fail   # agents should hard-stop when disabled

      - name: 🧠 Plan changes
        if: steps.ks.outputs.kill_switch_on != 'true'
        run: echo "planner logic…"
```

---

## 🗂️ Kill‑switch file formats

### A) 🤖 `ops/feature_flags/agents.yml` (agent enable/disable)

Minimal:

```yaml
enabled: false
reason: "maintenance"
expires_utc: "2026-01-11T00:00:00Z"
```

Interpretation:
- `enabled: false` ⇒ **agents are OFF** (Planner/Executor stop)
- `enabled: true`  ⇒ agents may run (still gated by governance + PR rules)

> [!TIP]
> Protect this file with CODEOWNERS. Treat changes as “ops‑critical”.

---

### B) 🧾 Optional `.kfm/kill-switch.yml` (audited stop button)

Example “pause publish, allow tests” posture:

```yaml
enabled: true
scope:
  publish: true
  deploy: true
  agents: false
  pr_checks: false

reason: "incident response: catalog integrity investigation"
set_by: "@kfm/ops"
set_at_utc: "2026-01-10T05:12:00Z"
expires_utc: "2026-01-11T05:12:00Z"
ticket: "INC-2026-01-10-001"
```

Suggested interpretation:
- `enabled: true` + `scope.publish: true` ⇒ stop promotion/publish lanes
- leave PR checks running if you want dev work to continue safely

---

## 🧯 Incident playbook

### 🚨 Immediate containment (minutes)
1) Turn on the fastest switch:
   - set `KFM_KILL_SWITCH=true` in the relevant GitHub **Environment** or repo‑level secret/variable  
2) Re-run the affected workflow(s) (optional) to confirm the guard trips.
3) Start private incident tracking (don’t paste sensitive info in public issues).

### 🧾 Stabilize + document (hours)
4) If you need an auditable stop state:
   - set `.kfm/kill-switch.yml` with reason + expiry + ticket
5) Add/confirm CODEOWNERS protection for:
   - `ops/feature_flags/**`
   - `.kfm/**`
6) Run governance scans + catalog QA on a fixed snapshot.

### ✅ Recovery (after fix)
7) Turn switch OFF (revert file + unset env var)
8) Require a “return to green” checklist:
   - catalogs valid ✅
   - provenance present ✅
   - classification propagation validated ✅
   - secrets rotated if applicable ✅

---

## 🔐 Security & governance notes

- **Least privilege:** this action should run with `contents: read` only.
- **No secret printing:** never echo `KFM_KILL_SWITCH` values directly.
- **Fail‑closed matters:** if your repo uses the switch to protect publishing, default to “stop” when the switch config is missing or unreadable.
- **Keep it first:** put this action at the top of jobs that can mutate state (publish, deploy, releases, agents).

> [!CAUTION]
> Treat kill‑switch toggles like production infrastructure changes.  
> They deserve CODEOWNERS + review + change history. 🔐🧾

---

## 🧰 Troubleshooting

### “It says the kill switch is ON, but I didn’t set it”
- Check workflow `env:` blocks for a `KFM_KILL_SWITCH` override.
- Check GitHub **Environment** secrets/vars (they can shadow repo ones).
- Check `.kfm/kill-switch.yml` and `ops/feature_flags/agents.yml`.

### “It’s not stopping my workflow”
- Ensure your workflow actually calls this action (guardrails job recommended).
- Ensure downstream jobs have `if:` gates wired to the output.
- Confirm you didn’t set `behavior: continue`.

### “I want publish lanes halted but PR checks to keep running”
- Use `scope: publish` in publish workflows.
- Keep PR workflows using `scope: pr_checks` (or `all` but configured to allow checks in `.kfm/kill-switch.yml`).

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>

