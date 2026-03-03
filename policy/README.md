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

Deny-by-default governance rules enforced in CI and at runtime via OPA Rego and Conftest.

**Status:** draft  
**Owners:** `kfm:team:governance`, `kfm:team:devsecops`

![Status](https://img.shields.io/badge/status-draft-yellow)
![Policy](https://img.shields.io/badge/policy-OPA%20Rego-blue)
![CI](https://img.shields.io/badge/CI-required-lightgrey)
![Tests](https://img.shields.io/badge/tests-Conftest-lightgrey)
![Rego](https://img.shields.io/badge/rego-v1%20migration%20ready-lightgrey)

> NOTE  
> **Confirmed:** The KFM architecture uses a “trust membrane” where the governed API is the enforcement boundary and policy is evaluated consistently (no direct store bypass).  
> **Proposed:** This directory houses the policy bundle(s) used by both CI and runtime, plus fixtures/tests to prevent regressions.  
> **Unknown:** The exact folder layout in *your* clone. See “Verify your local layout” below.

## Navigation

- [Overview](#overview)
- [Where this fits](#where-this-fits)
- [What belongs here](#what-belongs-here)
- [Directory layout](#directory-layout)
- [Decision surfaces](#decision-surfaces)
- [Run locally](#run-locally)
- [CI gates](#ci-gates)
- [Authoring conventions](#authoring-conventions)
- [Rego v1 migration](#rego-v1-migration)
- [Governance and review](#governance-and-review)
- [Troubleshooting](#troubleshooting)
- [Appendix](#appendix)

---

## Overview

- **Confirmed:** Policy is evaluated **deny-by-default** and must **fail closed** when requirements are missing or a rule denies.  
- **Confirmed:** CI uses **Conftest** to evaluate Rego policies against structured artifacts (stories, receipts, catalogs, etc.).  
- **Confirmed:** Policy decisions should return **allow/deny** plus **obligations** (redaction/generalization) and **reason codes** for UX + auditing.  
- **Proposed:** Runtime services use the same bundle(s) as CI to avoid “works in CI, bypasses at runtime.”

### Evidence tags used in this repository

This project uses three tags for meaningful governance claims:

- **Confirmed:** backed by evidence (tests, contracts, or cited design docs)
- **Proposed:** recommended default (may change as implementation lands)
- **Unknown:** not yet verified; includes minimum steps to confirm

---

## Where this fits

- **Confirmed:** The “trust membrane” is: **Client UI → Governed API (policy enforcement) → Policy engine + evidence resolver → Stores**.  
- **Confirmed:** A key risk is policy bypass via direct DB/storage access; mitigations include tests and network/code rules that prevent bypass.  
- **Proposed:** This directory is the “single source of truth” for the Rego rules used across CI and runtime.

~~~mermaid
flowchart LR
  UI[Map Story Focus UI] --> API[Governed API]
  API --> PEP[Policy enforcement]
  PEP --> OPA[Policy engine]
  API --> ER[Evidence resolver]
  ER --> OPA
  ER --> CAT[Catalogs]
  API --> STO[Stores]

  CAT[DCAT STAC PROV] --> ER
  STO[PostGIS Object Graph Search] --> API
~~~

([Back to top](#policy))

---

## What belongs here

### Acceptable inputs

- **Confirmed:** Rego policy files (`.rego`) used by CI and runtime.
- **Confirmed:** Policy test files (OPA unit tests) and Conftest fixture tests.
- **Proposed:** Small JSON/YAML “facts” files (approved licenses, sensitivity label maps, controlled vocab lists).
- **Proposed:** Example inputs (“fixtures”) that demonstrate PASS and DENY behavior.

### Exclusions

- **Confirmed:** Secrets, credentials, tokens, private keys.
- **Confirmed:** Raw restricted datasets, precise sensitive-location point sets, or anything that increases targeting risk.
- **Proposed:** Large binaries; policy packs should remain auditable diffs.

> WARNING  
> **Confirmed:** If permissions/sensitivity are unclear, default-deny and require stewardship review; prefer generalized derivatives and redaction obligations over raw exposure.

([Back to top](#policy))

---

## Directory layout

- **Unknown:** Your repository’s exact directory layout.
- **Proposed:** Recommended structure (adjust to match the repo):

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
        audit.rego
      manifest/
        gate.rego

  data/
    licenses.json
    sensitivity.json
    vocab.json

  tests/
    fixtures/
      story_nodes/
        story_node.ok.json
        story_node.fail.missing_evidence.json
      receipts/
        run_receipt.ok.json
        run_receipt.fail.missing_spdx.json
~~~

### Verify your local layout

- **Unknown:** Whether your repo uses `policy/rego`, `policy/opa`, or `policies/`.
- **Minimum verification step:** Run:

~~~bash
tree -L 4 policy || ls -R policy
~~~

…and update the examples in this README to match.

([Back to top](#policy))

---

## Decision surfaces

- **Confirmed:** Policy should be consumable in **CI** (Conftest, `opa test`) and **runtime** (OPA server or embedded evaluation).
- **Proposed:** Standardize entrypoints so callers don’t depend on internal file paths.

### Suggested entrypoints

| Entry point | Tag | Purpose | Typical input |
|---|---|---|---|
| `data.kfm.merge.allow` / `deny` | **Proposed** | Block merges/promotions if licensing/redaction requirements fail | PR receipt, dependency list, target zone |
| `data.kfm.promotion.allow` / `deny` | **Proposed** | Gate RAW→WORK→PROCESSED→PUBLISHED promotion | run_receipt, validation summary, policy_label |
| `data.kfm.story.audit.allow` / `deny` | **Proposed** | Gate Story Node publish on evidence + redaction consistency | story-node JSON |
| `data.kfm.manifest.allow` / `deny` | **Proposed** | Require required fields (SPDX, digests, receipts) | incoming manifest bundle |

### Decision outputs

- **Confirmed:** Every decision should be machine-readable, at minimum:

  - `decision`: `"allow"` or `"deny"`
  - `reasons`: stable reason codes/messages for audit + UX
  - `obligations`: required redaction/generalization steps if publishable with transformations

([Back to top](#policy))

---

## Run locally

### Prerequisites

- **Proposed:** Install tools:
  - OPA CLI (`opa`)
  - Conftest (`conftest`)
- **Unknown:** Your pinned versions. (Pin for deterministic CI.)

### Common commands

**Format and typecheck policies (Rego v1 compatible checks):**

~~~bash
opa fmt --write --v0-v1 ./policy
opa check --v0-v1 --strict ./policy
~~~

**Run OPA unit tests:**

~~~bash
opa test ./policy -v
~~~

**Run Conftest on Story Nodes (example path):**

~~~bash
conftest test "stories/**/story-node.json" -p "policy/rego"
~~~

> NOTE  
> **Unknown:** Whether your Story Nodes live under `stories/`.  
> **Minimum verification step:** locate them (e.g., `git ls-files | grep -i story-node.json`).

([Back to top](#policy))

---

## CI gates

- **Confirmed:** CI must fail closed on policy deny.
- **Proposed:** Treat policy checks as **required** status checks on protected branches.

### Minimal GitHub Actions gate

~~~yaml
name: policy-gate
on:
  pull_request:
    paths:
      - "policy/**"
      - "data/**"
      - "catalog/**"
      - "stories/**"

jobs:
  policy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Rego compile check
        run: |
          opa check --v0-v1 --strict ./policy

      - name: Conftest policy tests
        run: |
          conftest test ./receipts/run_receipt.json -p ./policy/rego

      - name: Fail closed on deny
        run: |
          echo "If conftest denied, this job should already be failing. Fail closed anyway."
~~~

### Policy kill switch pattern

- **Proposed:** Add a synthetic “emergency deny” rule and a CI job that flips it on to prove the stack fails closed end-to-end.

([Back to top](#policy))

---

## Authoring conventions

### Deny by default

- **Confirmed:** Start with an explicit deny-by-default posture:

~~~rego
package kfm.example

default allow := false

deny[msg] {
  msg := {"code": "EXAMPLE_DENY", "severity": "deny", "msg": "example deny"}
}

allow {
  count(deny) == 0
}
~~~

### Prefer structured violations

- **Confirmed:** Prefer `violation[]` objects (machine-parsable) over free-form strings so CI logs and JSON artifacts stay stable.

### Common gates

- **Confirmed:** Licensing checks (SPDX allowlist), provenance receipt presence, and redaction obligations for publish targets are standard examples of gates.

([Back to top](#policy))

---

## Rego v1 migration

- **Confirmed:** Rego v1 migration is supported via `opa fmt/check` in v1 compatibility modes, and CI should gate on strict compile.
- **Confirmed:** Conftest behavior can change when its defaults change; pin versions or pass `--rego-version` during transition.

### Practical migration steps

1) **Check:** strict compile in v1 mode

~~~bash
opa check --v0-v1 --strict ./policy
~~~

2) **Rewrite:** apply formatter in v1 mode

~~~bash
opa fmt --write --v0-v1 ./policy
~~~

3) **During migration:** add `import rego.v1` to packages you are actively editing (until all downstreams are v1-clean).

4) **Bundles:** if you ship OPA bundles, set `rego_version: 1` in the bundle manifest (and optionally per-file overrides while migrating).

([Back to top](#policy))

---

## Governance and review

- **Confirmed:** Policy changes are governance changes; treat them as PR-reviewed, auditable artifacts.
- **Proposed:** Require:
  - code review from owners
  - tests proving PASS and DENY cases
  - an audit trail for any overrides (no silent bypass)
  - a rollback plan for impactful policy shifts

### Definition of done for policy changes

- [ ] **Confirmed:** deny-by-default remains true
- [ ] **Confirmed:** at least one PASS fixture and one DENY fixture exist
- [ ] **Confirmed:** reason codes are stable and documented
- [ ] **Confirmed:** no sensitive data or secrets added
- [ ] **Proposed:** CI gates updated to run on touched paths

([Back to top](#policy))

---

## Troubleshooting

- **Proposed:** Print denies as a table for readability:

~~~bash
conftest test path/to/input.json -p policy/rego -o table
~~~

- **Proposed:** Use OPA server mode for interactive debugging (local only):

~~~bash
opa run --server --addr :8181 ./policy/rego
# then POST inputs to /v1/data/<package>/<rule>
~~~

- **Confirmed:** Avoid “ghost metadata” leaks: error behavior should not reveal restricted existence unless policy allows.

([Back to top](#policy))

---

## Appendix

<details>
<summary>Example Story Node inputs and a simple audit policy</summary>

- **Proposed:** Use a Story Node contract that carries:
  - claims with `evidence_ref`
  - datasets with `spec_hash`
  - `sensitivity` plus `redaction_profile`

~~~json
{
  "doc_kind": "story_node",
  "id": "story.example",
  "title": "Example Story",
  "status": "pending",
  "owners": ["kfm:team:stories"],
  "sensitivity": "public",
  "redaction_profile": "public_default",
  "claims": [{"id": "claim.001", "text": "Example claim", "evidence_ref": "oci:..."}],
  "datasets": [{"ref": "catalog:stac/items/example.json", "spec_hash": "sha256-..."}]
}
~~~

~~~rego
package kfm.story.audit

default allow := false

deny[msg] {
  input.doc_kind != "story_node"
  msg := {"code": "NOT_STORY_NODE", "severity": "deny", "msg": "doc_kind must be story_node"}
}

deny[msg] {
  some c in input.claims
  not startswith(c.evidence_ref, "oci:")
  msg := {"code": "MISSING_EVIDENCE_REF", "severity": "deny", "msg": "claim missing evidence_ref"}
}

allow {
  count(deny) == 0
}
~~~

</details>
