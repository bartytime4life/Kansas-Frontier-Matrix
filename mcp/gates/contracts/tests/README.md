# 🧪 MCP Gate Contract Tests — `mcp/gates/contracts/tests/`

![Gates](https://img.shields.io/badge/gates-fail--closed-critical)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-6f42c1)
![Evidence](https://img.shields.io/badge/evidence-STAC%20%7C%20DCAT%20%7C%20PROV-orange)

> **Purpose:** protect KFM’s *non‑negotiable* “boundary contracts” (schemas, policy rules, and decision outputs) so changes stay **auditable**, **reproducible**, and **safe by default** 🔒

---

## 🧭 What lives here?

This directory contains **contract tests** for KFM’s **Policy Gates** — automated checks that decide whether a change is **allowed ✅** or **denied ⛔** during CI and/or at runtime checkpoints.

- **Gate** = a quality/governance checkpoint (ex: licensing, provenance completeness, sensitive data handling).
- **Contract** = a stable interface the whole system depends on:
  - schema expectations (STAC / DCAT / PROV profiles)
  - stable policy IDs + categories
  - deterministic decision output (machine‑parseable denies)
  - time‑bound waivers (when exceptions are approved)

---

## 🧠 Why is this under `mcp/`?

`mcp/` is the home for **methods & computational experiments** — the place where we keep runs, notebooks, model cards, and repeatable workflows. 🧪📓

**Gates are the seatbelt** for MCP work:
- experiments shouldn’t silently publish “mystery outputs”
- anything that becomes “evidence” must be cataloged + provenance‑linked
- if a change can’t be validated, the gate **closes** (fail‑closed posture)

---

## ✅ The invariants we enforce

These tests keep KFM’s governance posture intact by ensuring gates can reliably deny changes that violate core rules like:

1. **Schema & profile validity** 📐  
2. **STAC / DCAT / PROV completeness** 🧾  
3. **License presence** ⚖️  
4. **Sensitivity / classification labeling** 🏷️  
5. **Provenance completeness** 🧬  
6. **Focus Mode citation requirements** (no unsourced answers) 📌  
7. **No obvious secret leaks** 🔐  

> If it doesn’t pass, it doesn’t ship. That’s the point. 😄

---

## 🗺️ Where this fits in CI

```mermaid
flowchart LR
  PR[📦 Pull Request / Change] --> D[👀 Detect]
  D --> V[🧪 Validate]
  V --> S[📐 Schema + Contract Tests]
  V --> P[🔒 Policy Pack (OPA/Rego)]
  P -->|allow ✅| M[🚀 Promote (merge/deploy)]
  P -->|deny ⛔| B[🧱 Block + Report Violations]
```

---

## 🗂️ Suggested layout (keep fixtures tiny + obvious)

> Add folders as needed, but try to keep a consistent “fixtures → cases → snapshots” pattern.

```
mcp/gates/contracts/tests/
├── 📄 README.md
├── 📁 fixtures/
│   ├── ✅ pass/                 # minimal valid examples
│   └── ❌ fail/                 # minimal invalid examples (1 reason to fail)
├── 📁 cases/
│   ├── 📄 test_catalog_contracts.py
│   ├── 📄 test_provenance_contracts.py
│   ├── 📄 test_policy_pack_contracts.py
│   ├── 📄 test_waivers_contracts.py
│   └── 📄 test_run_manifest_contracts.py
└── 📁 snapshots/
    ├── 📄 expected_allow.json
    └── 📄 expected_denies.json
```

---

## 🚀 Running the tests locally

### 1) Python contract tests (pytest)

From repo root:

```bash
pytest -q mcp/gates/contracts/tests
```

### 2) Policy Pack checks (Conftest + OPA)

Typical usage pattern:

```bash
# Evaluate policy pack against failing fixtures
conftest test mcp/gates/contracts/tests/fixtures/fail \
  -p tools/validation/policy
```

✅ Tips:
- keep fixtures **deterministic**
- keep failure fixtures **single-cause**
- prefer **small JSON** and stable ordering so diffs stay readable

---

## 🧱 What does “contract test” mean here?

### 1) Boundary artifact contracts (STAC / DCAT / PROV)

We treat catalog outputs as **boundary artifacts** — downstream systems (graph, API, UI, Focus Mode) rely on them being present and valid.

Contract tests here should catch:
- missing required fields (schema violations)
- broken cross-links (STAC ↔ DCAT ↔ PROV)
- invalid profile extensions
- “published” outputs without corresponding evidence artifacts

---

### 2) Policy output contracts (stable IDs + machine-readable denies)

Policy gate results must be predictable so CI, W‑P‑E agents, dashboards, and future UI surfaces can consume them.

**Minimum contract for a violation:**
- `id` (stable, example format: `KFM-PROV-001`)
- `category` (Catalogs, Provenance, Sovereignty, API, Story, Security, Style, …)
- `message` (actionable)
- optional `paths` (files involved)

Recommended “deny” payload shape:

```json
{
  "decision": "deny",
  "violations": [
    {
      "id": "KFM-PROV-001",
      "category": "Provenance",
      "message": "Processed data changed without matching PROV update.",
      "paths": ["data/processed/.../output.parquet", "data/prov/.../run.jsonld"]
    }
  ]
}
```

> 💡 Even if Conftest outputs plain text, these contract tests should still enforce a stable **semantic shape**: stable IDs + categories + clear messages.

---

### 3) Waiver contracts (time-bound exceptions only)

If we allow exceptions, they must never be silent:

- waivers must be **explicit**
- must reference a **stable rule ID**
- must include **reason + expiry**
- must be reviewable in PR (no hidden bypass)

---

### 4) Run manifest contracts (determinism + reproducibility)

When pipelines emit a `run_manifest.json`, contract tests should verify:

- required run fields exist (inputs, tool versions, counts)
- digest/idempotency fields are stable across re-runs
- manifests can be used as policy inputs (policy‑as‑code needs structured evidence)

---

## ✍️ Adding a new contract test (recipe)

1. **Pick the contract you’re protecting** 🧱  
   Examples: license required, PROV updated with outputs, sensitive flag present, etc.

2. **Choose the right policy identity** 🏷️  
   Stable rule IDs are a feature, not bureaucracy.

3. **Create minimal fixtures** 🧫  
   - `fixtures/pass/...` for “good”
   - `fixtures/fail/...` for “bad”
   - keep failing fixtures **single-cause**

4. **Write the test** 🧪  
   Assert:
   - allow vs deny  
   - stable `id`, `category`, and message signature

5. **Fail closed** 🔒  
   If test can’t confidently evaluate, treat it as failure (no silent “skip” for governance gates).

---

## 🧯 Troubleshooting

<details>
<summary>Common failures & quick fixes (click to expand)</summary>

- **Missing license** ⚖️  
  Add an approved license to the relevant STAC/DCAT entry.

- **Missing PROV / provenance mismatch** 🧬  
  Regenerate or update the PROV bundle for the changed dataset.

- **Schema errors** 📐  
  Validate JSON against the applicable schema/profile and fill required fields.

- **Secret detected** 🔐  
  Remove credential, rotate it, and document the rotation (don’t just delete).

- **Focus Mode citation failure** 📌  
  Ensure the output contains at least one evidence-backed citation and that the cited entity exists in the catalogs.

</details>

---

## 🔗 Related “source of truth” docs (recommended reading)

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline ordering + subsystem contracts  
- 🧱 `docs/architecture/` — governance + policy gate philosophy  
- 🔒 `tools/validation/policy/` — Rego policy pack  
- 🧪 `tests/` — broader unit/integration/E2E suites  
- 📚 `docs/data/` — domain runbooks + data contracts

---

## 🧠 Quick mantra (print it on a sticker)

- **Contract-first** 🧱 — specs are first-class.
- **Evidence-first** 🧾 — no narrative without catalogs + provenance.
- **Deterministic** 🎯 — same inputs → same outputs.
- **Fail closed** 🔒 — if unsure, deny.
