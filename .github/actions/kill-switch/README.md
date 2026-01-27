# 🛑 Kill Switch — Composite GitHub Action

![GitHub Action](https://img.shields.io/badge/GitHub%20Action-composite-2088FF?logo=githubactions&logoColor=white)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical?logo=shield&logoColor=white)
![KFM](https://img.shields.io/badge/KFM-ops%20guard-6E56CF?logo=github&logoColor=white)

> [!IMPORTANT]
> This action is an **emergency brake** 🚨 for workflows (deploys, releases, ingestion, publishing, destructive maintenance).
> Put it **as the very first step** in any job you may need to stop quickly.

---

## ✨ What this action does

The **kill-switch** action checks a configured “switch” value and then:

- ✅ **Allows** the job to proceed when the switch is **OFF**
- 🛑 **Stops** the job immediately when the switch is **ON** (default behavior)
- ⚠️ Optionally **warns-only** (soft mode) so you can test wiring without blocking work

This is a *fail-closed guardrail*: if the switch is engaged, we assume “stop” unless an explicit override policy exists.

---

## 🧠 How it works (mental model)

```mermaid
flowchart TD
  A[Workflow starts] --> B[🛑 kill-switch step]
  B -->|Switch OFF| C[Continue job steps ✅]
  B -->|Switch ON| D[Fail fast / Warn ⚠️]
  D --> E[Job stops (fail) 🧯]
```

---

## 🚀 Quickstart

### 1) Create repo variables (recommended)

In **Repo Settings → Secrets and variables → Actions → Variables**, add:

- `KFM_KILL_SWITCH` = `false` (default)
- `KFM_KILL_SWITCH_REASON` = *(optional)* short human-readable reason

> ℹ️ GitHub docs on variables:  
> - “Store information in variables” → `vars.*` context: https://docs.github.com/actions/learn-github-actions/variables  
> - Variables reference: https://docs.github.com/en/actions/concepts/workflows-and-actions/variables

### 2) Add the guard step to workflows

Add this step at the **top** of any guarded job:

```yaml
- name: 🛑 Kill switch (guard)
  uses: ./.github/actions/kill-switch
  with:
    switch: ${{ vars.KFM_KILL_SWITCH }}
    reason: ${{ vars.KFM_KILL_SWITCH_REASON }}
```

---

## 🔧 Inputs

> **Tip:** Keep the kill switch **non-secret** (repo variable) unless you have a reason to hide it.  
> Treat `reason` as log output — **never put secrets in it**.

| Input | Required | Default | Description |
|------|----------|---------|-------------|
| `switch` | ✅ Yes | — | The kill switch state (string/boolean). Truthy values = **engaged**. |
| `reason` | No | empty | Why the switch is engaged (printed to logs / step summary). |
| `mode` | No | `fail` | `fail` = stop job with a non-zero exit, `warn` = log warning and continue. |

### ✅ Truthy values accepted for `switch`

The action treats these values (case-insensitive) as **ON / engaged**:

- `1`, `true`, `on`, `yes`, `y`, `enabled`, `engaged`

Everything else is treated as **OFF**.

---

## 📤 Outputs

| Output | Description |
|--------|-------------|
| `engaged` | `true` if the switch is engaged, else `false`. |
| `effective_reason` | The reason text actually used (may be empty). |

> [!NOTE]
> If `mode: fail` and the switch is engaged, the job fails early — downstream steps won’t run.

---

## 🧩 Usage patterns

### Pattern A — Guard a single job (most common ✅)

```yaml
name: Deploy

on:
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: 🛑 Kill switch (guard)
        uses: ./.github/actions/kill-switch
        with:
          switch: ${{ vars.KFM_KILL_SWITCH }}
          reason: ${{ vars.KFM_KILL_SWITCH_REASON }}

      - uses: actions/checkout@v4
      - name: Deploy
        run: ./ops/deploy.sh
```

---

### Pattern B — Guard multiple jobs (copy/paste safe)

Use the same step at the top of each job you want to protect.

> [!TIP]
> For big workflows, consider a **reusable workflow** or central “guard” job that other jobs `needs:`.

---

### Pattern C — Soft rollout / verification (warn-only)

```yaml
- name: 🛑 Kill switch (warn-only)
  uses: ./.github/actions/kill-switch
  with:
    switch: ${{ vars.KFM_KILL_SWITCH }}
    reason: ${{ vars.KFM_KILL_SWITCH_REASON }}
    mode: warn
```

---

### Pattern D — Ultra-fast gating (job-level `if`)

If you want to avoid allocating runners at all, you can gate at the job level:

```yaml
jobs:
  deploy:
    if: ${{ vars.KFM_KILL_SWITCH != 'true' && vars.KFM_KILL_SWITCH != 'on' }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy..."
```

> [!NOTE]
> Job-level `if` is fast, but the kill-switch action is still recommended because it gives **consistent logging** + a **single control point** for parsing truthy values and messaging.

---

## 🔥 Incident runbook: engaging the kill switch

### Engage (stop guarded workflows)
1. Go to **Settings → Secrets and variables → Actions → Variables**
2. Set:
   - `KFM_KILL_SWITCH = true`
   - `KFM_KILL_SWITCH_REASON = <short reason + ticket/link>`
3. Trigger or re-run workflows as needed (they should fail at the guard step).

### Disengage (resume normal ops)
1. Set `KFM_KILL_SWITCH = false`
2. (Optional) clear or update `KFM_KILL_SWITCH_REASON`

---

## 🧯 “Nuclear option” alternatives (when you must stop *everything*)

If you need to stop workflows regardless of whether they include this action:

- **Disable the workflow** in the Actions UI  
  Docs: https://docs.github.com/actions/using-workflows/disabling-and-enabling-a-workflow
- **Disable/limit GitHub Actions at repo/org level**  
  Docs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository

---

## 🛡️ Security & governance notes

- 🧾 **Reason is public to logs**: don’t put credentials, access tokens, or sensitive data in `reason`.
- 🔒 Combine with **branch protection**, **CODEOWNERS**, and **environment approvals** for real-world safety.
- 🧯 The kill switch is a *circuit breaker*, not a replacement for good governance.

---

## 🧪 Testing checklist

- [ ] Add the guard step to one low-risk workflow
- [ ] Flip `KFM_KILL_SWITCH` to `true` and confirm it fails quickly
- [ ] Flip it back to `false` and confirm normal behavior
- [ ] Roll out to deploy/release/ingestion workflows

---

## 📁 Directory layout

```text
.github/actions/kill-switch/
├─ action.yml           # composite action definition
├─ README.md            # (you are here)
└─ (optional) scripts/  # helper scripts if needed
```

---

## 🧭 Related docs

- 📄 `.github/README.md` (project ops + CI/CD philosophy): `../../README.md`
- 📚 GitHub Docs:
  - Variables: https://docs.github.com/actions/learn-github-actions/variables
  - Composite actions: https://docs.github.com/actions/creating-actions/creating-a-composite-action
  - Disable workflows: https://docs.github.com/actions/using-workflows/disabling-and-enabling-a-workflow