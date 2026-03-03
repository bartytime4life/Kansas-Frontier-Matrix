<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3f1d9e8a-1c53-4d2b-a1ff-7a6c0c522f6e
title: policy directory README
type: standard
version: v1
status: draft
owners:
  - kfm:team:governance
  - kfm:team:devsecops
created: 2026-03-03
updated: 2026-03-03
policy_label: public
related:
  - ../docs/governance/README.md
  - ../docs/standards/
  - ../.github/workflows/
tags: [kfm, policy, opa, rego, conftest]
notes:
  - This README documents the policy-as-code surface for KFM.
  - Paths under “Related” may not exist yet; update them once those docs land.
[/KFM_META_BLOCK_V2] -->

# policy
Deny-by-default governance rules enforced in CI and at runtime via OPA (Rego) and Conftest.

---

## Impact
**Status:** draft  
**Owners:** `kfm:team:governance`, `kfm:team:devsecops`  
**Policy posture:** deny-by-default, fail-closed

![Status](https://img.shields.io/badge/status-draft-yellow)
![Policy](https://img.shields.io/badge/policy-OPA%20Rego-blue)
![Conftest](https://img.shields.io/badge/tests-Conftest-lightgrey)
![CI](https://img.shields.io/badge/CI-required-lightgrey)
![Rego](https://img.shields.io/badge/rego-v1%20migration%20ready-lightgrey)
![Fail-Closed](https://img.shields.io/badge/posture-fail--closed-critical)

**Quick links:**  
- [`../docs/governance/README.md`](../docs/governance/README.md) (governance model)  
- [`../docs/standards/`](../docs/standards/) (schemas, standards)  
- [`../.github/workflows/`](../.github/workflows/) (CI gates)

> IMPORTANT  
> **CONFIRMED:** KFM treats policy as a **trust membrane**: clients never access storage directly; governed APIs are the enforcement boundary.  
> **PROPOSED:** This directory is the **single source of truth** for policy bundles + fixtures used by both CI and runtime.  
> **UNKNOWN:** Your local directory layout and exact tool versions (OPA/Conftest) are not verified here—see “Minimum verification steps.”

---

## Navigation
- [Scope](#scope)
- [Where this fits](#where-this-fits)
- [Inputs](#inputs)
- [Exclusions](#exclusions)
- [Directory layout](#directory-layout)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Diagrams](#diagrams)
- [Tables](#tables)
- [CI gates](#ci-gates)
- [Authoring conventions](#authoring-conventions)
- [Rego v1 migration](#rego-v1-migration)
- [Governance and review](#governance-and-review)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Appendix](#appendix)
- [Version history](#version-history)

---

## Scope

- **CONFIRMED:** Policies are evaluated **deny-by-default** and must **fail closed** when evidence/requirements are missing.
- **CONFIRMED:** Policies return **allow/deny** plus **reason codes** and **obligations** (e.g., redaction/generalization requirements).
- **PROPOSED:** CI and runtime must consume the same bundle(s) (or the same fixtures and expected outcomes), so “passes CI” implies “passes runtime.”
- **UNKNOWN:** The specific set of policy decisions KFM currently enforces in your clone (promotion, story publish, focus answers, exports, etc.). Verify by searching for `package kfm.` rules.

([Back to top](#policy))

---

## Where this fits

- **CONFIRMED:** KFM’s enforcement boundary (“trust membrane”) is: **Client UI → Governed API (PEP) → Policy Engine (PDP) + Evidence Resolver → Stores**.
- **CONFIRMED:** A critical risk is bypass: direct reads/writes to DB/object storage that skip policy evaluation.
- **PROPOSED:** This directory hosts policies and tests that (a) prevent bypass by contract and (b) enforce promotion and publish rules consistently.

([Back to top](#policy))

---

## Inputs

### Acceptable inputs

- **CONFIRMED:** Rego policy modules (`.rego`) used by CI and runtime evaluation.
- **CONFIRMED:** OPA unit tests (`*_test.rego`) and Conftest fixture tests.
- **PROPOSED:** Small, reviewed “facts” files (e.g., SPDX allowlists, sensitivity label maps, controlled vocabulary lists).
- **PROPOSED:** Example inputs (“fixtures”) that demonstrate PASS and DENY behavior for each decision surface.

([Back to top](#policy))

---

## Exclusions

- **CONFIRMED:** Secrets, credentials, tokens, private keys, or embedded auth headers.
- **CONFIRMED:** Raw restricted datasets, precise sensitive-location point sets, or anything that increases targeting risk.
- **PROPOSED:** Large binaries—policy packs should remain auditable, diff-friendly text.

> WARNING  
> **CONFIRMED:** If permissions/sensitivity are unclear, default-deny and route to stewardship review. Prefer obligations (redaction/generalization) over raw exposure.

([Back to top](#policy))

---

## Directory layout

> NOTE  
> **UNKNOWN:** Your repo’s exact policy folder structure.  
> **Minimum verification step:** run `tree -L 4 policy || ls -R policy` and align this README to what exists.

**PROPOSED structure (adjust to match your repo):**

~~~text
policy/
  README.md

  rego/
    kfm/
      merge/
        gate.rego
      promotion/
        gate.rego
        emergency_deny.rego
      story/
        publish.rego
      focus/
        answer.rego
      evidence/
        resolve.rego

  data/
    licenses_spdx_allowlist.json
    sensitivity_labels.json
    vocab.json

  tests/
    fixtures/
      receipts/
        run_receipt.ok.json
        run_receipt.fail.missing_spdx.json
      story_nodes/
        story_node.ok.json
        story_node.fail.missing_evidence_ref.json
~~~

### Minimum verification steps (fail-closed docs posture)

- **UNKNOWN → CONFIRMED:** Is the policy source under `policy/rego/` or `policy/opa/`?
  - Run: `find policy -maxdepth 3 -name '*.rego' -print`
- **UNKNOWN → CONFIRMED:** What are the entrypoint packages?
  - Run: `grep -R --line-number '^package ' policy | sort`
- **UNKNOWN → CONFIRMED:** Which artifacts are tested in CI (receipts, catalogs, story nodes, etc.)?
  - Run: `grep -R --line-number 'conftest test' .github/workflows || true`

([Back to top](#policy))

---

## Quickstart

### Prerequisites

- **PROPOSED:** Install:
  - `opa` (OPA CLI)
  - `conftest` (policy tests against JSON/YAML)

> NOTE  
> **UNKNOWN:** Your pinned versions. Pin tool versions in CI for deterministic results.

### Local commands (typical)

**Format policy (keep diffs clean):**
~~~bash
opa fmt --write ./policy
~~~

**Strict compile checks (recommended):**
~~~bash
opa check --strict ./policy
~~~

**Run OPA unit tests:**
~~~bash
opa test ./policy -v
~~~

**Run Conftest against a receipt (example path):**
~~~bash
conftest test receipts/run_receipt.json -p policy/rego -o table
~~~

([Back to top](#policy))

---

## Usage

### Decision surfaces

- **CONFIRMED:** Policy must be consumable in **CI** (Conftest, `opa test`) and **runtime** (OPA server/sidecar or embedded evaluation).
- **PROPOSED:** Standardize entrypoints so callers don’t depend on internal file paths.

### Suggested entrypoints (names are PROPOSED)

| Entry point | Tag | Purpose | Typical input |
|---|---|---|---|
| `data.kfm.merge.allow` / `deny` | **PROPOSED** | Block merges when receipts/licenses/obligations fail | PR receipt, dependency/license list |
| `data.kfm.promotion.allow` / `deny` | **PROPOSED** | Gate RAW→WORK→PROCESSED→CATALOG→PUBLISHED promotion | promotion manifest, run receipt, validation summary |
| `data.kfm.story.publish.allow` / `deny` | **PROPOSED** | Gate Story Node publish on evidence + rights + sensitivity | story-node JSON |
| `data.kfm.focus.answer.allow` / `deny` | **PROPOSED** | Enforce cite-or-abstain + safe output constraints | question + evidence bundle refs + draft answer |
| `data.kfm.evidence.resolve.allow` / `deny` | **PROPOSED** | Ensure evidence resolution respects policy | EvidenceRef + principal context |

### Decision output contract (PROPOSED minimum)

Policies should return machine-readable objects:

- `decision`: `"allow"` or `"deny"`
- `reasons[]`: stable codes/messages for audit + UX
- `obligations[]`: required transformations (redaction/generalization/attribution)

Example shape:

~~~json
{
  "decision": "deny",
  "reasons": [
    {"code": "MISSING_LICENSE", "severity": "deny", "message": "DCAT license missing"}
  ],
  "obligations": [
    {"type": "redact", "target": "geometry", "method": "generalize_to_grid_1km"}
  ]
}
~~~

([Back to top](#policy))

---

## Diagrams

### Trust membrane (policy enforcement boundary)

~~~mermaid
flowchart LR
  UI[Client UI] --> API[Governed API PEP]
  API --> PDP[Policy Decision Point OPA]
  API --> ER[Evidence Resolver]
  ER --> PDP
  API --> STO[Stores]
  ER --> CAT[Catalog triplet]

  CAT[DCAT STAC PROV] --> ER
  STO[Canonical plus projections] --> API
~~~

### Truth path and promotion gates

~~~mermaid
flowchart LR
  U[Upstream] --> RAW[RAW immutable]
  RAW --> WORK[WORK or QUARANTINE]
  WORK --> PROCESSED[PROCESSED publishable]
  PROCESSED --> CATALOG[CATALOG triplet]
  CATALOG --> PUBLISHED[PUBLISHED governed]

  PUBLISHED --> API[Governed API]
  API --> UI2[Map Story Focus UI]

  G[Promotion Contract gates] -. applies at transitions .-> RAW
  G -.-> WORK
  G -.-> PROCESSED
  G -.-> CATALOG
  G -.-> PUBLISHED
~~~

([Back to top](#policy))

---

## Tables

### Promotion Contract gates (policy relevance)

> NOTE  
> **CONFIRMED intent:** Promotion to PUBLISHED is blocked unless minimum gates are met.  
> **PROPOSED implementation:** Gate each requirement via Rego + validators + fixture tests.

| Gate | What must be present | Policy example check |
|---|---|---|
| A — Identity & versioning | dataset IDs + deterministic spec_hash + artifact digests | deny if `dataset_version_id` missing or digests don’t verify |
| B — Licensing & rights | SPDX/license fields + terms snapshot | deny if license unknown or missing |
| C — Sensitivity + plan | policy_label + obligations when needed | deny if PUBLISHED requires redaction but obligations not applied |
| D — Catalog triplet | DCAT/STAC/PROV validate + cross-link | deny if links broken or evidence refs unresolvable |
| E — QA thresholds | dataset QA outputs exist and meet thresholds | deny if QA missing/failed (or quarantine) |
| F — Run receipt & audit | run receipt present + append-only audit | deny if receipt absent or malformed |
| G — Release manifest | manifest references digests and artifacts | deny if manifest missing or inconsistent |

([Back to top](#policy))

---

## CI gates

- **CONFIRMED:** CI must fail closed on policy deny.
- **PROPOSED:** Treat policy checks as **required** status checks on protected branches.

### Minimal GitHub Actions gate (illustrative)

~~~yaml
name: policy-gate
on:
  pull_request:
    paths:
      - "policy/**"
      - "contracts/**"
      - "data/**"
      - "catalog/**"
      - "stories/**"
      - "receipts/**"

jobs:
  policy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: OPA strict compile
        run: |
          opa check --strict ./policy

      - name: OPA unit tests
        run: |
          opa test ./policy -v

      - name: Conftest on a run receipt (example)
        run: |
          conftest test receipts/run_receipt.json -p ./policy/rego -o table

      - name: Fail closed
        run: |
          echo "If any prior step denied, this job must fail."
~~~

### Kill switch pattern (PROPOSED)

- Add `policy/rego/kfm/promotion/emergency_deny.rego` that can deny promotion globally behind a single, explicit feature flag.
- Add an integration test that flips the flag on and proves the entire promotion path fails closed end-to-end.

([Back to top](#policy))

---

## Authoring conventions

### Deny-by-default

~~~rego
package kfm.example

default allow := false

deny[violation] {
  violation := {
    "code": "EXAMPLE_DENY",
    "severity": "deny",
    "message": "example deny"
  }
}

allow {
  count(deny) == 0
}
~~~

- **CONFIRMED:** Prefer structured `violation` objects over free-form strings (stable for CI logs and machine parsing).
- **PROPOSED:** Use stable `code` values (reason codes) and treat them as API surface.

### Sensitive metadata leakage rule of thumb

- **CONFIRMED:** Do not leak restricted existence via error details (e.g., avoid 403/404 “oracle” behavior).
- **PROPOSED:** Standardize “not authorized / not found” responses to reduce inference risk.

([Back to top](#policy))

---

## Rego v1 migration

- **CONFIRMED:** Rego v1 introduces compatibility requirements; authors can adopt `import rego.v1` for v1 semantics.
- **PROPOSED:** Gate policy code with strict compilation and a documented migration path.

### Practical migration steps (typical)

1) **Check strict compilation**
~~~bash
opa check --strict ./policy
~~~

2) **Format consistently**
~~~bash
opa fmt --write ./policy
~~~

3) **During migration**
- Add `import rego.v1` to packages you are actively editing (and do not mix with `future.keywords` in the same module).

4) **Conftest compatibility**
- If you must keep v0 syntax temporarily, run Conftest with a v0 setting (exact flag depends on your Conftest version).

([Back to top](#policy))

---

## Governance and review

- **CONFIRMED:** Policy changes are governance changes; treat them as reviewed, auditable artifacts.
- **PROPOSED:** Require:
  - CODEOWNER review from `kfm:team:governance` and `kfm:team:devsecops`
  - PASS + DENY fixture coverage for each changed decision
  - reason-code stability (no renames without migration note)
  - rollback plan for impactful shifts

### Definition of done (policy PRs)

- [ ] **CONFIRMED:** deny-by-default remains true
- [ ] **CONFIRMED:** at least one PASS fixture and one DENY fixture exist per decision touched
- [ ] **CONFIRMED:** reason codes are stable and documented
- [ ] **CONFIRMED:** no sensitive data or secrets added
- [ ] **PROPOSED:** CI gates updated to run on touched paths
- [ ] **PROPOSED:** integration test proves CI/runtime parity for the changed behavior

([Back to top](#policy))

---

## Troubleshooting

- **PROPOSED:** Print denies as a table for readability:
~~~bash
conftest test path/to/input.json -p policy/rego -o table
~~~

- **PROPOSED:** Debug via OPA server mode (local only):
~~~bash
opa run --server --addr :8181 ./policy/rego
# then POST inputs to /v1/data/<package>/<rule>
~~~

- **PROPOSED:** If a fixture denies unexpectedly:
  - confirm you’re testing the intended policy root (`-p policy/rego` vs `-p policy/opa`)
  - confirm the entrypoint path (package + rule)
  - confirm tool versions match CI

([Back to top](#policy))

---

## FAQ

**Why both OPA tests and Conftest?**  
- **PROPOSED:** Use `opa test` for fast, module-level unit tests; use Conftest for contract/fixture validation against real artifacts (receipts, manifests, story nodes).

**Can the UI enforce policy?**  
- **CONFIRMED:** The UI can display policy badges and notices, but it must not make policy decisions.

([Back to top](#policy))

---

## Appendix

<details>
<summary>Example fixture input and a simple Story publish gate</summary>

**PROPOSED:** A Story Node contract carries claims that reference resolvable evidence and declares a policy label and redaction profile.

~~~json
{
  "doc_kind": "story_node",
  "id": "story.example",
  "title": "Example Story",
  "status": "pending",
  "owners": ["kfm:team:stories"],
  "policy_label": "public",
  "redaction_profile": "public_default",
  "claims": [
    {"id": "claim.001", "text": "Example claim", "evidence_ref": "doc://sha256:...#page=1&span=10:200"}
  ]
}
~~~

~~~rego
package kfm.story.publish

default allow := false

deny[violation] {
  input.doc_kind != "story_node"
  violation := {"code": "NOT_STORY_NODE", "severity": "deny", "message": "doc_kind must be story_node"}
}

deny[violation] {
  some c in input.claims
  not startswith(c.evidence_ref, "doc://")
  violation := {"code": "MISSING_EVIDENCE_REF", "severity": "deny", "message": "claim missing evidence_ref"}
}

allow {
  count(deny) == 0
}
~~~

</details>

([Back to top](#policy))

---

## Version history

- **v1 (2026-03-03):** Initial KFM-aligned policy directory README (deny-by-default, CI/runtime parity posture, promotion gates, and fixtures-first testing).

([Back to top](#policy))
