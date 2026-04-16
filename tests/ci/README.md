<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION_UUID
title: tests/ci
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: 2026-04-16
policy_label: public
related: [
  ../README.md,
  ../../README.md,
  ../../.github/README.md,
  ../../.github/CODEOWNERS,
  ../../.github/workflows/README.md,
  ../../.github/actions/README.md,
  ../../.github/watchers/README.md,
  ../../scripts/README.md,
  ../../contracts/README.md,
  ../../schemas/README.md,
  ../../policy/README.md,
  ../../data/receipts/README.md,
  ../../data/proofs/README.md,
  ../../tools/ci/README.md,
  ../../tools/diff/README.md,
  ../../tools/attest/README.md,
  ../../tools/validators/README.md,
  ../../tools/validators/promotion_gate/README.md,
  ./test_render_diff_summary.py,
  ./test_render_bundle_diff_policy_summary.py,
  ./test_render_promotion_review_handoff.py,
  ../validators/test_promotion_gate_e2e.py
]
tags: [kfm, tests, ci, fixtures, renderer-tests, promotion, diff, policy-summary, review-handoff, receipts, proofs]
notes: [
  Updated to align with workflow publication order, validator/attest boundaries, and receipt/proof separation.
  This revision makes explicit that tests/ci proves renderer behavior only, not policy, promotion, or attestation authority.
  Exact mounted test inventory and runner wiring remain NEEDS VERIFICATION.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/ci/`

Deterministic, public-safe proof surface for **KFM CI renderer helpers and reviewer-facing summaries**.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Role:** helper-proof lane  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Usage](#usage) · [Coverage matrix](#coverage-matrix) · [Definition of done](#definition-of-done)

---

## Scope

`tests/ci/` exists to **prove renderer behavior** for helpers in `tools/ci/`.

This lane answers one question:

> “Do CI-facing summaries and handoff artifacts render correctly from already-governed inputs?”

It does **not** answer:

- whether promotion is allowed
- whether policy is correct
- whether attestation is valid
- whether a release should happen

Those belong to:

- `tools/validators/`
- `tools/attest/`
- `policy/`
- `tests/e2e/`

---

## Core principle

> **Rendering ≠ decision ≠ validation ≠ proof**

| Layer | Responsibility |
|------|----------------|
| `tests/contracts/` | prove object validity |
| `tools/validators/` | enforce fail-closed logic |
| `tools/attest/` | sign / verify |
| `data/receipts/` | process memory |
| `data/proofs/` | trust objects |
| `tools/ci/` | render summaries |
| `tests/ci/` | prove rendering correctness |

---

## Repo fit

This lane sits between:

- **Upstream truth sources**
  - contracts / schemas / policy
  - receipts and proofs

- **Downstream reviewer surfaces**
  - CI summaries
  - PR annotations
  - promotion review handoff docs

It ensures the rendering layer **does not distort truth**.

---

## Inputs

Accepted inputs must already be governed:

| Input type | Example |
|-----------|--------|
| decision objects | `decision.json` |
| bundles | `promotion-bundle.json` |
| diff reports | `promotion-bundle-diff.json` |
| diff-policy reports | `promotion-bundle-diff-policy.json` |
| attestation results | `decision-verify-result.json` |
| receipt refs | `receipt_ref` |

### Input rule

> **If the input is not already validated, it does not belong here.**

---

## Exclusions

This lane must not:

- compute diffs
- evaluate policy
- validate contracts
- sign artifacts
- store receipts or proofs
- replace machine artifacts with markdown

---

## Directory tree

```text
tests/ci/
├── README.md
├── test_render_diff_summary.py
├── test_render_bundle_diff_policy_summary.py
└── test_render_promotion_review_handoff.py
```

---

## Usage

### What to test here

- deterministic output
- correct ordering of sections
- correct rendering of:
  - blocking state
  - review-required state
  - counts
  - key lists
  - conclusions
- failure on malformed input

### What NOT to test here

- policy correctness
- promotion logic
- schema validation
- attestation validity

---

## Coverage matrix

| Renderer | Input | Must prove |
|----------|------|-----------|
| diff summary | diff JSON | counts, blocking state |
| diff-policy summary | policy JSON | classification, review flags |
| review handoff | bundle + diff + policy | composed output, no loss of information |

---

## Critical rule: no authority drift

A renderer must never:

- reinterpret policy
- recompute diff logic
- imply promotion success
- hide missing inputs
- merge receipts and proofs into one surface

---

## Publication order (must match workflows)

Tests must enforce that output ordering remains:

1. bundle summary  
2. diff summary  
3. diff-policy summary  
4. review handoff  

This ensures reviewers see:

```
what exists → what changed → what policy says → final conclusion
```

---

## Definition of done

A renderer test is complete when:

- [ ] input is minimal and deterministic  
- [ ] output is stable and reviewable  
- [ ] malformed input fails clearly  
- [ ] no hidden logic is introduced  
- [ ] ordering matches workflow expectations  
- [ ] receipt/proof distinction is preserved  
- [ ] composed output does not replace underlying artifacts  

---

## FAQ

### Why not test logic here?

Because this lane proves **presentation**, not **truth**.

### Why emphasize receipt vs proof?

Because CI output is the easiest place to accidentally collapse them.

### Why test ordering?

Because review correctness depends on sequence, not just content.

### Why keep tests small?

Because reviewers must understand them at a glance.

---

## Appendix

### Rendering chain

```text
validated objects
  ↓
tools/ci renderer
  ↓
tests/ci verification
  ↓
workflow publication
  ↓
human review
```

### Golden rule

> If a renderer could mislead a reviewer, it must fail here.
