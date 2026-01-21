# 🧪 Example 09 — Policy Pack Smoke Tests ⚖️

![Example](https://img.shields.io/badge/example-09-blue)
![Module](https://img.shields.io/badge/module-mcp%2Fdev__prov-orange)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Rego-6e40c9)
![Runner](https://img.shields.io/badge/tests-Conftest-0aa)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-success)
![Posture](https://img.shields.io/badge/security-fail--closed-critical)
![Provenance](https://img.shields.io/badge/provenance-first-✅-informational)

📍 **Path:** `mcp/dev_prov/examples/09_policy_pack_smoke_tests/`

> [!NOTE]
> This example provides a **fast, deterministic “smoke test” harness** for KFM’s policy packs (OPA/Rego + Conftest).  
> The intent is simple: **if policies are broken, or if governance can be bypassed, we find out immediately** — locally and in CI.

---

## 🎯 What this example is for

This example is built to help `mcp/dev_prov` teams validate that:

- ✅ The **policy pack compiles** (no broken Rego, no missing imports, no namespace drift)
- ✅ “Golden” fixtures still **PASS** (allowed) and **FAIL** (denied) as expected
- ✅ Deny messages remain **stable + actionable** (ex: `KFM-PROV-001: ...`)
- ✅ KFM’s **non‑negotiables** remain enforceable:
  - **provenance-first**
  - **canonical pipeline ordering**
  - **API boundary**
  - **evidence-first outputs** (AI + narrative)
  - **fail‑closed** posture

---

## 🧠 Why smoke tests (not just unit tests)?

Policy packs are *governance as code*. That means they are **production safety rails** — not documentation.

Smoke tests give you:

- 🚦 **Early warning** when a policy change accidentally weakens governance
- 🔁 **Repeatability** (MCP mindset): same inputs → same outcomes
- 🧷 **Regression protection** for “social contracts” (FAIR/CARE, sovereignty, security)
- 🧩 A clear path to scale: add a fixture → lock in expected behavior

> [!TIP]
> Treat these fixtures like **golden experiments**: they encode “what must always be true” about KFM.

---

## 📦 What gets tested (recommended coverage)

You can tailor this to your repo, but these are the **KFM-aligned domains** this example expects to cover:

| Domain 🧱 | What we smoke-test ✅ | Example fixture idea 🧪 |
|---|---|---|
| 🧬 Provenance-first | Derived data changes require PROV updates | processed CSV without matching `data/prov/*` |
| 🧭 Pipeline ordering | No later stage without earlier stage artifacts | graph export added but no STAC/DCAT/PROV |
| 🧾 FAIR metadata | license/provider/contact required | DCAT missing license / provider |
| 🪶 CARE / sovereignty | sensitivity labels + propagation | culturally sensitive dataset lacking `care_label` |
| 🤖 AI output governance | AI answers must be labeled + cited | Focus Mode answer missing citations |
| 🧵 Story Nodes / Pulse | evidence manifest present + resolvable | Story Node missing `evidence_manifest` |
| 🔐 Secrets / security | block obvious secrets in configs | “AWS key-like” strings in JSON/YAML |
| 🧾 dev_prov run manifests | schema present + canonical digest | run_manifest missing `tool_versions` / digest |

---

## 🗂️ Suggested folder layout (inside this example)

Use this as a **reference layout** to keep smoke tests clean and discoverable:

```text
mcp/dev_prov/examples/09_policy_pack_smoke_tests/
├─ 📘📄 README.md                      # 📘 What this pack tests + how to run locally/CI + expected pass/fail signals
├─ 🧪 fixtures/                        # 🧪 Policy test fixtures (known-pass/known-fail) used by conftest/OPA
│  ├─ ✅ pass/                          # ✅ Fixtures that MUST pass (baseline “good” examples)
│  │  ├─ ✅🧾 dcat.valid.json            # Valid DCAT record (license, distributions, links present)
│  │  ├─ ✅🧾 stac.valid.json            # Valid STAC object (profile-compliant; links resolvable)
│  │  ├─ ✅📝 story_node.valid.md        # Valid Story Node markdown (front-matter + citations policy satisfied)
│  │  └─ ✅🧾 run_manifest.valid.json    # Valid run manifest (ids, timestamps, inputs/outputs, hashes present)
│  └─ ❌ fail/                          # ❌ Fixtures that MUST fail (proves policies catch regressions)
│     ├─ ❌🧾 dcat.missing_license.json   # Missing/invalid license → should be denied
│     ├─ ❌🧬🧾 prov.missing_for_processed_change.json # Processed change without PROV linkage → should be denied
│     ├─ ❌🤖🧾 ai_answer.no_citations.json # AI output with no citations → should be denied (evidence-first)
│     └─ ❌🔒🧾 secrets.detected.yaml     # Secret-like content fixture → should be denied by secret/PII policies
├─ 📥 inputs/                          # Inputs describing “what changed” (used to scope which policies run)
│  └─ 📥🧾 pr_changed_files.sample.json  # Sample PR file-change list used by gate runner routing logic
└─ ⚙️ scripts/                         # Helper scripts to execute the smoke suite consistently
   └─ ⚙️🧪📄 smoke.sh                    # Runs conftest/OPA against fixtures and exits non-zero on unexpected results
```

> [!NOTE]
> The exact filenames don’t matter — consistency and intent do.  
> Keep fixtures tiny, explicit, and named like “what should happen.”

---

## 🚀 Quickstart

### 1) Pick your policy pack directory 🎯

KFM docs commonly describe policy packs living in one of these locations:

- `api/scripts/policy/` (CI governance pack)
- `tools/validation/policy/` (validation/runtime policy pack)

Set a `POLICY_DIR` that matches **your repo’s** structure:

```bash
# from repo root
export POLICY_DIR="api/scripts/policy"
# OR
export POLICY_DIR="tools/validation/policy"
```

### 2) Run the smoke tests 🧪

#### Option A — helper script (if present)
```bash
bash mcp/dev_prov/examples/09_policy_pack_smoke_tests/scripts/smoke.sh
```

#### Option B — direct Conftest execution
```bash
# PASS fixtures should produce zero denies
conftest test \
  -p "$POLICY_DIR" \
  mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/pass

# FAIL fixtures should produce denies (this should FAIL the command)
conftest test \
  -p "$POLICY_DIR" \
  mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/fail
```

#### Option C — OPA compile / unit tests (optional, but recommended)
If your policy pack includes `_test.rego` tests:

```bash
opa test "$POLICY_DIR" -v
```

---

## ✅ Expected behavior

### ✅ “pass/” fixtures
- should return **0 denies**
- should not require waivers
- should remain stable over time

### ❌ “fail/” fixtures
- should return **1+ denies**
- denies should include:
  - a **stable rule id** (ex: `KFM-PROV-001`)
  - a **human-friendly message**
  - (optional) a remediation hint

<details>
<summary>📌 Example deny message style</summary>

```text
FAIL - prov.missing_for_processed_change.json - KFM-PROV-001:
Processed data changed without matching PROV update.
Fix: add/refresh the related PROV bundle under data/prov/...
```
</details>

---

## 🧩 Adding a new smoke test

### Add a fixture
1. Decide whether it’s **PASS** or **FAIL**
2. Put it under:
   - `fixtures/pass/` ✅  (should remain compliant)
   - `fixtures/fail/` ❌  (should be denied)

### Lock the behavior
- Run the suite and confirm it behaves the way you intend.
- If your deny message format changed, fix the policy output (preferable) rather than “teaching” fixtures to accept vague output.

> [!TIP]
> Fixtures should be **minimal**: one violation per fixture, unless you’re explicitly testing bundling behavior.

---

## 🧾 Waivers policy (use sparingly)

KFM-style governance expects waivers to be:

- ⏳ **time-bound** (expiration date)
- 🧾 **justified** (why this is acceptable temporarily)
- 🎯 **scoped** (rule id + file scope, not “disable everything”)

> [!WARNING]
> If you add a waiver, you are making a governance exception.  
> Treat it like a production incident workaround: tracked, reviewed, and removed.

---

## 🔁 CI integration sketch (GitHub Actions)

Add a fast job that runs on PRs:

```yaml
name: policy-pack-smoke
on:
  pull_request:

jobs:
  smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Install conftest/opa however your repo standardizes tooling
      # (pinned versions recommended)
      - name: Run Policy Pack Smoke Tests
        run: |
          export POLICY_DIR="api/scripts/policy"
          conftest test -p "$POLICY_DIR" mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/pass
          # fail fixtures should DENY; invert expectation if you assert denies via a script
          conftest test -p "$POLICY_DIR" mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/fail && exit 1 || exit 0
```

> [!TIP]
> For the “fail fixtures should fail” step, it’s cleaner to wrap it in `scripts/smoke.sh` so the CI logic stays readable.

---

## 🔒 What “good” looks like (governance signals)

This example should make it easy to confirm:

- ✅ Policy pack denies **pipeline bypass** attempts
- ✅ Policy pack denies **missing provenance** for derived artifacts
- ✅ Policy pack denies **unsourced AI outputs**
- ✅ Policy pack denies **metadata incompleteness** (license/provider)
- ✅ Policy pack denies **sensitive data mishandling**
- ✅ Policy pack denies **secret leakage**
- ✅ dev_prov artifacts (run manifests, attestations) remain **valid inputs** to governance

---

## 📚 Design inputs used for this example

This example is aligned with KFM’s documented approach to:

- 🧭 **canonical pipeline ordering** (ETL → catalogs → graph → APIs → UI → narratives → Focus Mode)
- 🧬 **provenance-first** enforcement + fail‑closed posture
- ⚖️ **OPA/Rego policy packs** executed via **Conftest**
- 🧾 **evidence-first narratives** (Story Nodes, evidence manifests, citations)
- 🤖 **AI citations as a hard gate**
- 🔐 **security + supply-chain hygiene**
- 🧪 **MCP reproducibility workflows** (docs-first, repeatable experiments, traceable outputs)

<details>
<summary>🗃️ Project docs & reference material (for deeper context)</summary>

- 📘 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- 🤖 Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- 🧭 Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- 🗺️ Kansas Frontier Matrix – Comprehensive UI System Overview
- 📥 KFM Data Intake – Technical & Design Guide
- 💡 Innovative Concepts to Evolve KFM
- 🧠 AI Concepts & more
- 🗃️ Data Management Theories / Architectures / Data Science (Bayesian, etc.)
- 🌍 Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL
- 🧰 Various programming languages & resources
- 🌟 Latest Ideas & Future Proposals
- 🧵 Additional Project Ideas (Pulse Threads, evidence manifests, run manifests)
- 🧪 Scientific Method / Research / Master Coder Protocol documentation
</details>

---

## ✅ Acceptance checklist (keep this green)

- [ ] Policy pack compiles (`opa test` or equivalent compile check)
- [ ] PASS fixtures: no denies
- [ ] FAIL fixtures: denies fire reliably
- [ ] Denies contain stable rule IDs (ex: `KFM-PROV-001`)
- [ ] Waivers are time-bound + justified (if any)
- [ ] CI runs this suite on every PR touching policies or governed artifacts

---

## 🧭 Related links (repo-local)

> These are *intended* repo paths based on the KFM architecture docs. Adjust if your tree differs.

- `../../../../api/scripts/policy/README.md` 🧾
- `../../../../docs/MASTER_GUIDE_v13.md` 🧭
- `../../../../docs/guides/pipelines/` 🛠️
- `../../../../mcp/` 🧪
- `../../../../schemas/` 📐

---
