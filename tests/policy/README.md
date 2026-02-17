# 🧭 Policy Tests (OPA/Rego + Conftest)

![Policy as Code](https://img.shields.io/badge/Policy--as--Code-OPA%2FRego-informational)
![Default Deny](https://img.shields.io/badge/Default-Deny%20by%20Default-critical)
![CI Gate](https://img.shields.io/badge/CI-Merge%20Blocking-important)
![Fixtures](https://img.shields.io/badge/Fixtures-Redaction--Safe-success)

This folder contains **policy test fixtures** and **test harness guidance** for KFM’s policy-as-code layer.

KFM’s governance posture is **fail-closed**: if policy evaluation is ambiguous, incomplete, or evidence is missing, the correct outcome is **deny**.

> [!IMPORTANT]
> Treat changes under `policy/` and `tests/policy/` as **production changes**:
> - They can block releases
> - They can change what data/answers become public
> - They can prevent sensitive-location leakage

---

## 🎯 What this directory is for

`tests/policy/` exists to make governance **measurable and non-optional**:

- **Regression fixtures** (golden pass/fail examples) for policy rules
- A stable place to add **“known leak” negatives** (redaction/generalization regressions)
- A single, documented way to run policy checks locally and in CI

This folder should **not** contain real sensitive locations, private individual data, or proprietary content. Use synthetic/redacted fixtures only.

---

## 🧱 Where policy code lives

Policy code is typically stored in `policy/opa/` (OPA/Rego). This test folder provides fixtures and expectations for those policies.

A common high-level layout:

```text
repo-root/
├─ policy/
│  └─ opa/
│     ├─ receipt.rego
│     ├─ receipts_pr_gate.rego
│     ├─ watchers.rego
│     └─ gates/
│        ├─ artifact.rego
│        └─ station.rego
└─ tests/
   └─ policy/
      ├─ README.md                # (this file)
      ├─ fixtures/
      │  ├─ receipts/             # run_receipt inputs (valid + invalid)
      │  ├─ run_manifest/         # merge/PR gate inputs
      │  ├─ promotion_manifest/   # promotion guard inputs (CARE/sensitivity/licensing)
      │  ├─ focus_mode/           # cite-or-abstain style fixtures (text/JSON)
      │  └─ leak_fixtures/         # “known leak” regression tests (redaction/generalization)
      └─ expected/
         ├─ allow/                # expected allow decisions (optional, if you snapshot outputs)
         └─ deny/                 # expected deny decisions (optional, if you snapshot outputs)
```

> [!NOTE]
> If your repository places policies elsewhere, update the commands below to point at the correct policy directory.
> The intent is invariant: **fixtures live here; policies live in `policy/`**.

---

## 🔁 How the policy gates fit into KFM

```mermaid
flowchart TD
  Dev[Developer edits: datasets / code / catalogs] --> PR[Pull Request]
  PR --> CI[CI: schema + policy + contract tests]
  CI -->|allow| Merge[Merge allowed]
  CI -->|deny| Block[Merge blocked (fail-closed)]
  Merge --> Bundle[Policy bundle/version]
  Bundle --> API[Trust-membrane API]
  API --> UI[Web UI / Focus Mode]
```

---

## ✅ What we test (typical policy surfaces)

| Policy surface | Purpose | Example fixture folder | Typical outcomes |
|---|---|---|---|
| **Receipt invariants** | Ensure every run artifact is traceable/deterministic | `fixtures/receipts/` | deny missing spec/digest/provenance |
| **Merge / PR gate** | Block merges if required evidence/attestations are missing | `fixtures/run_manifest/` | deny missing manifest/signatures/rights |
| **Promotion guard** | Block public promotion when CARE/rights/sensitivity constraints fail | `fixtures/promotion_manifest/` | deny missing license; deny missing consent; allow internal lane |
| **Sensitive-location leakage** | Prevent “inference leakage” regressions | `fixtures/leak_fixtures/` | deny if redaction/generalization absent |
| **Focus Mode “cite-or-abstain”** | Prevent uncited claims and restricted disclosure | `fixtures/focus_mode/` | deny unresolvable evidence refs; require abstention |

---

## 🧪 Running the tests locally

### Option A: Conftest (recommended)

Run policy evaluation against **fixtures** using Conftest.

```bash
# From repo root
conftest test tests/policy/fixtures -p policy/opa
```

If you keep policies in a different directory:

```bash
conftest test tests/policy/fixtures -p <path-to-your-rego-policies>
```

### Option B: OPA unit tests (optional but strongly encouraged)

OPA can run unit tests in `*_test.rego` files.

```bash
opa test policy/opa -v
```

> [!TIP]
> Use both:
> - `opa test` for **unit tests** on policy logic
> - `conftest test` for **integration-style tests** over realistic input shapes

---

## 🧩 Fixture design rules (non-negotiable)

### 1) Fixtures must be safe to publish

- **No private individuals**
- **No precise restricted coordinates**
- **No culturally restricted information**
- **No secrets, keys, tokens**
- Use synthetic IDs and redacted coordinates.

> [!WARNING]
> If you need to test redaction/generalization, use *synthetic points/polygons* designed to trigger the rule,
> not real archaeological site coordinates.

### 2) Fixtures must be deterministic

- Stable ordering (avoid map/hash order dependence)
- Explicit timestamps only when required; prefer fixed dates
- Avoid external HTTP calls or live upstream dependencies

### 3) Fixtures must include “known-bad” negatives

For every high-risk policy, add fixtures that previously failed or could plausibly regress:
- insecure `accessURL` patterns
- missing license/attribution
- missing consent facet
- “public” lane with restricted classification
- Focus output with missing citations

---

## 🧷 Suggested fixture naming convention

Use names that encode intent and expected result:

```text
<domain>__<scenario>__ALLOW.json
<domain>__<scenario>__DENY.json
```

Examples:

```text
receipts__missing_spec_hash__DENY.json
promotion__public_intersects_tribal_no_consent__DENY.json
promotion__internal_lane_no_consent__ALLOW.json
focus__answer_missing_citations__DENY.json
leak__public_precise_coords_present__DENY.json
```

---

## 🧰 Minimal input shapes (examples)

### Promotion manifest (policy input)

Policies often evaluate a *promotion manifest* describing what is being promoted and under what exposure lane.

```json
{
  "artifact": {
    "id": "example:stac-item-001",
    "labels": {
      "sensitivity": "sensitive-location",
      "authority_to_control": "tribal:EXAMPLE"
    },
    "provenance": {
      "facets": [
        {
          "name": "tribal_consent",
          "value": { "consent_id": "consent-xyz", "scope": "publish", "expires": "2027-12-31" }
        }
      ]
    },
    "spatial": {
      "intersects_authoritative_tribal_boundary": true,
      "tribes": ["EXAMPLE"]
    },
    "intended_exposure": "public"
  },
  "run": {
    "lane": "promotion:public",
    "policy_version": "v1",
    "spec_hash": "sha256:REDACTED"
  }
}
```

> [!NOTE]
> This JSON is intentionally synthetic and redaction-safe. Use it as a pattern, not as an authoritative schema.

---

## 🔒 Change control for policies

Policy changes can alter:
- what is publishable
- what is accessible at runtime
- what Focus Mode is allowed to answer

**Minimum checklist for any policy change:**

- [ ] Add/adjust at least **one ALLOW fixture** and **one DENY fixture**
- [ ] Add/adjust `*_test.rego` unit tests when logic changes
- [ ] Confirm “default deny” still holds for missing/unknown fields
- [ ] Ensure fixtures remain redaction-safe (no sensitive leakage)
- [ ] Ensure CI produces a human-readable deny reason (developer usability)
- [ ] Record policy version changes where applicable (e.g., `policy_version` in manifests/receipts)

---

## 🧯 Troubleshooting

<details>
  <summary><strong>Conftest says “no policies found”</strong></summary>

- Confirm `-p policy/opa` points to a directory containing `.rego` files.
- Confirm policies reference the right package names for your inputs.
- Confirm fixture files are valid JSON/YAML.

</details>

<details>
  <summary><strong>Unexpected ALLOW / DENY</strong></summary>

- Validate the fixture includes all required fields (missing fields should generally DENY).
- Ensure you’re testing the right policy package/namespace.
- If you recently changed policy logic, add a regression fixture for the old behavior and document why it changed.

</details>

<details>
  <summary><strong>CI differs from local</strong></summary>

- Pin tool versions (OPA/Conftest) and ensure CI uses the same versions.
- Confirm the same policy bundle is loaded in both contexts.
- Avoid environment-variable-dependent policy decisions unless explicitly intended and documented.

</details>

---

## 📌 Governance note

Policy tests are part of KFM’s **trust membrane**: the web UI and external clients should never bypass governed APIs, and policies must be enforced consistently in CI and at runtime.

If a test suggests “we should just bypass policy for convenience,” treat that as a **severity-1 governance issue**, not a workaround request.

---

## 📚 References (internal)

- KFM Integration Idea Pack: policy packs + CI fail-closed wiring (Feb 2026)
- KFM Data Source Integration Blueprint: evidence-first + policy enforcement at the trust membrane (Feb 2026)

(Adjust these references to point at your repo’s actual doc paths if/when those documents are checked in.)