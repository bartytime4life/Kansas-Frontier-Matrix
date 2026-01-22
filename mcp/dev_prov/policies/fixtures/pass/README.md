# ✅ PASS Fixtures — Dev Provenance Policy Pack

`🛡️ Policy-as-Code` `⛓️ Provenance-First` `🔐 Fail-Closed` `🧾 Evidence-First`

These fixtures are the **golden “allowed” examples** for the Dev Provenance policy suite.

If anything in this folder starts failing, it usually means one of two things:

- **We tightened governance** ✅ (update fixtures + document the new expectation)
- **We regressed policy logic / harness** ❌ (fix the policy or the test runner)

---

## 🧭 What “PASS” means

A **PASS fixture** represents a mini change-set that is **safe to merge + safe to publish**:

- 🧾 **Metadata complete** (FAIR-minded: license/contact/provider, consistent IDs)
- ⛓️ **Provenance intact** (no broken lineage; evidence for outputs exists)
- 🔐 **Ethics & sensitivity respected** (CARE-minded: classification, review flags, redaction/generalization)
- 🧰 **Supply chain signals present** (SBOM/SLSA/signatures/digests when required)
- 🧠 **AI transparency preserved** (citations + audit context; no “black box” outputs)
- 🤖 **No agent bypass** (Watcher/Planner/Executor output is held to the same gates as human PRs)

PASS fixtures are how we keep KFM’s promises from silently drifting. 🧭

---

## 📦 Folder layout 🗂️

```text
mcp/
  dev_prov/
    policies/
      fixtures/
        pass/   ✅ allowed cases (this folder)
        fail/   ❌ denied cases (negative tests)
```

### ✅ Recommended fixture structure

```text
pass/
  <policy_id>/                 # rego package, rule group, or policy bundle
    <case_name>/               # kebab-case scenario name
      input.json               # the Conftest/OPA `input`
      repo/                    # (optional) tiny repo snapshot the policy reads
      expected.json            # (optional) expected allow/warn metadata
      README.md                # (optional) short notes for this case
```

> 💡 Keep fixtures tiny, deterministic, and readable in a PR diff.

---

## 🧩 Fixture anatomy

### 1) `input.json` (required) 🧪

This is the object fed to policy evaluation as `input`.

**Design rules:**
- ✅ **Minimal**: only include fields the policy reads
- ✅ **Deterministic**: no random UUIDs, no `now()`, no unstable ordering
- ✅ **Self-contained**: don’t rely on external network calls

Example skeleton (adapt to your harness):

```json
{
  "changed_files": [
    "data/processed/example.parquet",
    "data/prov/example_prov.json"
  ],
  "metadata": {
    "dcat": {},
    "stac": {}
  },
  "provenance": {
    "prov_bundle": {}
  },
  "dev": {
    "pr_prov": {},
    "attestations": {
      "sbom": {},
      "slsa": {}
    }
  },
  "ai": {
    "output": {},
    "citations": [],
    "governance_flags": []
  }
}
```

### 2) `repo/` (optional, recommended when policies read files) 📁

Some policies validate actual repository files (catalog JSON, PROV bundles, evidence manifests, etc.).  
In those cases, add a minimal `repo/` subtree that mirrors the real repo paths.

```text
repo/
  data/
    stac/...
    catalog/dcat/...
    prov/...
    processed/...
  docs/...
```

### 3) `expected.json` (optional) 🎯

If the harness supports assertions, capture “what success looks like”:

- `allow: true`
- `warnings: []`
- `explanations: []`
- `policy_version: "..."`

---

## ✅ Common PASS scenarios (what we expect to model)

<details>
<summary><strong>🧾 Metadata integrity (FAIR-minded)</strong></summary>

PASS fixtures should demonstrate required metadata is present and consistent across standards:
- license present and valid
- provider/contact fields present
- stable dataset IDs
- DCAT ↔ STAC ↔ PROV references line up

</details>

<details>
<summary><strong>⛓️ Provenance-first publishing</strong></summary>

PASS fixtures should demonstrate that whenever “downstream” artifacts change, matching lineage exists too:
- processed data change ⇒ PROV updated
- new dataset/layer ⇒ STAC + DCAT updated
- graph/UI references ⇒ backed by catalog + provenance

</details>

<details>
<summary><strong>🔐 Sensitive data & CARE safeguards</strong></summary>

PASS fixtures should demonstrate:
- classification / care labels are present
- review flags are present when sovereignty/cultural sensitivity is involved
- coordinate generalization / redaction is applied where required

</details>

<details>
<summary><strong>🧠 AI transparency (Focus Mode / narratives)</strong></summary>

PASS fixtures should demonstrate:
- AI outputs include citations (no black-box answers)
- governance flags are surfaced when relevant
- optional explainability/audit context is present (what entities/layers were used)

</details>

<details>
<summary><strong>🧰 Supply chain integrity (SBOM / SLSA / signatures)</strong></summary>

PASS fixtures should demonstrate:
- build/ingest artifacts include provenance attestations
- SBOM exists for produced artifacts
- digests are stable and reproducible (canonicalized where required)

</details>

<details>
<summary><strong>🧑‍💻 Dev provenance invariants (PR → PROV)</strong></summary>

PASS fixtures should demonstrate a complete, queryable dev lineage:
- PR modeled as a provenance Activity
- commits modeled as Entities
- authors/reviewers/bots modeled as Agents
- required relations exist (e.g., used / wasAssociatedWith / wasGeneratedBy)

</details>

<details>
<summary><strong>🧱 Pipeline ordering & API boundary</strong></summary>

PASS fixtures should demonstrate:
- pipeline ordering is respected (no “skipping stages”)
- UI/clients access data through approved APIs (no direct DB/graph calls)

</details>

---

## 🧪 Running the PASS fixture suite

Because each repo wires policy testing differently, look for a root policy runner (common places):

- `api/scripts/policy/`
- `tools/validation/policy/`
- `mcp/dev_prov/policies/`

Typical commands (adjust paths to match this repo):

```bash
# Run everything
conftest test mcp/dev_prov/policies

# Run only PASS fixtures
conftest test mcp/dev_prov/policies/fixtures/pass

# Run one specific case
conftest test mcp/dev_prov/policies/fixtures/pass/<policy_id>/<case_name>
```

---

## 🧱 Adding a new PASS fixture

1. **Start with the FAIL case** (it defines the boundary).
2. Create the PASS case by making the smallest possible change that satisfies the rule.
3. Keep it deterministic (no randomness, stable ordering, stable digests where required).
4. Ensure it is safe to publish (no secrets, no private data, no real credentials).
5. Run policy tests locally and ensure CI agrees.

### ✅ PASS fixture checklist

- [ ] No secrets / tokens / API keys (even fake-looking patterns can trip scanners)
- [ ] License + provider/contact present when metadata is involved
- [ ] PROV exists and links Activity ↔ Entities ↔ Agents
- [ ] If `changed_files` is used, it matches the fixture’s `repo/` snapshot
- [ ] Sensitive data includes classification/care labels + review flags (and generalization if needed)
- [ ] AI artifacts include citations + governance flags when relevant
- [ ] Run manifests / digests are stable and reproducible (if the policy checks them)

---

## 🧩 Why this exists (the bigger picture)

KFM treats **data like code**: everything ships through PRs, is reviewable, and is governed by automated policy gates.

PASS fixtures are our “living examples” of what **good** looks like—so policy and platform values can’t drift silently. 🧭
