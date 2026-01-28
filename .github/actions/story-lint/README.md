# 🧹 Story Lint — KFM Story Node Validator (GitHub Action)

![KFM](https://img.shields.io/badge/KFM-governed%20atlas-6f42c1)
![CI](https://img.shields.io/badge/CI-fail--closed-critical)
![Action](https://img.shields.io/badge/type-local%20action-informational)
![Scope](https://img.shields.io/badge/scope-story%20nodes-blue)

> ✅ **Goal:** enforce a **clean, governed Story Node contract** (Markdown narrative + linked artifacts) so PRs can’t merge with broken story content.

---

<details>
<summary><strong>📚 Table of Contents</strong></summary>

- [🧠 What is a “Story Node”?](#-what-is-a-story-node)
- [✨ What this action checks](#-what-this-action-checks)
- [🧩 Where this action lives](#-where-this-action-lives)
- [🚀 Quickstart](#-quickstart)
- [⚙️ Inputs](#️-inputs)
- [📤 Outputs](#-outputs)
- [🧪 Run it locally](#-run-it-locally)
- [🧰 Troubleshooting](#-troubleshooting)
- [🛠️ Extending the rules](#️-extending-the-rules)
- [🧾 Notes](#-notes)

</details>

---

## 🧠 What is a “Story Node”?

A **Story Node** is the project’s “unit of narrative truth” — a governed story artifact that connects:
- 📝 **Narrative** (Markdown)
- 🧾 **Evidence & citations**
- 🧩 **Structured companion files** (often JSON choreography / metadata)
- 🔗 **Links to catalog items, datasets, maps, and timelines**

This action exists to keep that whole bundle consistent and merge-safe. ✅

---

## ✨ What this action checks

> The exact checks are implemented by this action’s entrypoint. The list below describes the **intent** and the most common validation gates.

### ✅ Common gates (typical)
- 🧾 **Front matter present** (if your Story Node format uses it) and includes required fields
- 🧩 **Required sections present** (e.g., Summary / Evidence / Sources) and not left as placeholders
- 🔗 **Internal links & image refs** are valid (no broken relative paths)
- 🧠 **Citation hygiene** (at minimum: a sources section; optionally: inline citation rules)
- 🧰 **Companion artifacts exist** (e.g., `story.json`, `script.json`, etc.)
- 🧪 **JSON validity** (parseable JSON; optional schema validation if configured)
- 🚫 **No “TODO/PLACEHOLDER” content** in governed areas (optional, but recommended)

### 🧯 Developer experience
- 🧷 Emits **GitHub annotations** (so errors show inline in PR checks)
- 🧾 Writes a **job summary** (what failed, where, and why)
- 🛑 Fails the job when configured to “fail-closed” (recommended for governed content)

---

## 🧩 Where this action lives

This is a **repo-local action**:

```text
.github/actions/story-lint/
├─ README.md        👈 you are here
├─ action.yml       ⚙️ action definition (source of truth)
└─ (entrypoint / scripts / tooling)
```

---

## 🚀 Quickstart

### ✅ Minimal usage (defaults)
```yaml
name: story-nodes
on:
  pull_request:
    paths:
      - "docs/stories/**"
      - "docs/reports/story_nodes/**"
  push:
    branches: [main]

jobs:
  story-lint:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout
        uses: actions/checkout@v4

      - name: 🧹 Story Lint
        uses: ./.github/actions/story-lint
```

### 🎯 Diff-focused usage (only lint what changed)
If your action supports passing explicit file lists (common in CI), pair it with a changed-files step:

```yaml
jobs:
  story-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: 🧭 Collect changed files
        id: changed
        uses: tj-actions/changed-files@v45
        with:
          files: |
            docs/stories/**
            docs/reports/story_nodes/**

      - name: 🧹 Story Lint (changed only)
        uses: ./.github/actions/story-lint
        with:
          # ⚠️ Example only — confirm supported input names in action.yml
          paths: ${{ steps.changed.outputs.all_changed_files }}
```

---

## ⚙️ Inputs

> 📌 **Source of truth:** [`./action.yml`](./action.yml)  
> If this README and `action.yml` ever disagree, **trust `action.yml`**.

Most Story Node linters expose some variation of these knobs:

| Input (common pattern) | What it does 🧩 | Typical default |
|---|---|---|
| `paths` | File(s) / glob(s) to lint | `docs/stories/**` |
| `mode` | `changed` vs `all` | `changed` (PR), `all` (main) |
| `config` | Optional config file path | _(none)_ |
| `fail_on` | `warning` or `error` threshold | `error` |
| `json_schema` | Optional schema path for companion JSON | _(none)_ |
| `report_format` | `annotations`, `summary`, `both` | `both` |

✅ **Recommendation:** keep defaults strict for governed content (fail-closed on errors).

---

## 📤 Outputs

Depending on implementation, this action may expose outputs like:

| Output (common pattern) | Meaning |
|---|---|
| `files_checked` | Number/list of files linted |
| `errors` | Count of errors |
| `warnings` | Count of warnings |
| `summary` | Short text summary (for job summary / PR comment) |

---

## 🧪 Run it locally

Many repo-local actions ship a runnable script (often `entrypoint.sh`) so you can test without waiting on CI.

### Option A: run the action’s entrypoint (if present)
```bash
bash .github/actions/story-lint/entrypoint.sh
```

### Option B: run the underlying linter tool (if the action wraps one)
Examples (pick what exists in this repo):

```bash
# Python-style
python scripts/story_lint.py docs/stories

# Node-style
node scripts/story-lint.mjs docs/stories
```

> 🔎 If you’re unsure what it wraps, open `action.yml` and follow the `runs:` section.

---

## 🧰 Troubleshooting

### “It passes locally but fails in CI”
- 🧩 CI may lint **more files** (e.g., `mode=all`)
- 🔗 CI may validate **links/assets** that you didn’t have locally
- 🧪 CI may run **schema validation** (strict) while local run is lenient

### “JSON parse error”
- Validate with:
  ```bash
  python -m json.tool path/to/file.json
  ```
- Watch for:
  - trailing commas
  - unescaped quotes
  - invalid UTF-8

### “Broken image/link path”
- Prefer **relative paths** from the Story Node file location.
- Confirm the asset exists and case matches exactly (Linux CI is case-sensitive).

---

## 🛠️ Extending the rules

When you add new governance checks:
- ✅ Keep rules **deterministic** (no network calls, no time-dependent output)
- ✅ Prefer **clear, actionable errors** (what + where + how to fix)
- ✅ Use **stable rule IDs** (helps docs + troubleshooting)
- 🧪 Add fixtures under a `tests/` folder if available

Suggested structure (if you expand this action):
```text
.github/actions/story-lint/
├─ action.yml
├─ entrypoint.sh
├─ rules/            🧩 individual rule checks
├─ schemas/          🧾 optional JSON schemas
└─ tests/            🧪 tiny story fixtures for CI
```

---

## 🧾 Notes

- 🧭 This action is intended as a **governance gate**: if Story Nodes are part of your public outputs, prefer **fail-closed** behavior.
- 🧷 Keep this README aligned with `action.yml` so contributors don’t guess inputs.
- 🧠 For Story Node authoring conventions, see the repo’s governance docs (often under `docs/` and/or `.github/`).
