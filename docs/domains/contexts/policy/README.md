<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/4f0f5b3c-0b6d-4a0a-8a31-7f0d3aee47b2
title: Policy Context
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/domains/contexts/README.md
  - policy/                       # policy-as-code bundle (OPA/Rego) — confirm in repo
  - contracts/                    # OpenAPI + schema surfaces — confirm in repo
  - docs/domains/contexts/evidence/README.md
tags: [kfm, policy, context, governance, trust-membrane]
notes:
  - This README defines the documentation contract for the “policy” context: labels, obligations, PDP/PEP, and how to change policy safely.
[/KFM_META_BLOCK_V2] -->

# Policy Context
**Purpose:** Documentation for how KFM classifies access/sensitivity and enforces it (CI + runtime) using **policy labels**, **policy decisions**, and **obligations**.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Policy Label](https://img.shields.io/badge/policy_label-public-blue)
![Owners](https://img.shields.io/badge/owners-TBD-lightgrey)
![PDP](https://img.shields.io/badge/PDP-OPA%20(Rego)-informational)
![PEP](https://img.shields.io/badge/PEP-CI%20%2B%20Runtime-success)
![Trust Membrane](https://img.shields.io/badge/trust_membrane-fail--closed-critical)

---

## Navigation
- [What this directory is](#what-this-directory-is)
- [Where it fits in KFM](#where-it-fits-in-kfm)
- [Key concepts](#key-concepts)
- [Policy label taxonomy](#policy-label-taxonomy)
- [Obligations](#obligations)
- [PDP/PEP architecture](#pdppep-architecture)
- [Change workflow](#change-workflow)
- [Directory contract](#directory-contract)
- [Glossary](#glossary)

---

## What this directory is
This folder is the **documentation context** for KFM policy:

- **Policy labels** (controlled vocabulary) used to classify datasets, artifacts, story nodes, and outputs.
- **Policy decisions** (allow/deny + reason codes + obligations) as the system’s “explainable verdict.”
- **Obligations** as first-class, auditable transforms (redaction/generalization/notice requirements).
- **PDP/PEP** wiring rules so CI and runtime agree, and the system fails closed.

> NOTE  
> This is *documentation*. **Policy code** (Rego), fixtures, and policy tests typically live under the repo’s `policy/` directory (confirm in repo).

[⬆️ Back to top](#policy-context)

---

## Where it fits in KFM
Policy is part of the **trust membrane**:
- Promotion to runtime surfaces is blocked unless a dataset version has a **policy label** and any required **obligations** are applied.
- CI and runtime must share the **same policy semantics** (or at minimum the same fixtures and expected outcomes).
- Policy is enforced at multiple points (CI checks, runtime API checks, evidence resolver checks). The UI displays policy state but does not decide it.

[⬆️ Back to top](#policy-context)

---

## Key concepts

### Policy label
A `policy_label` is the **primary classification input** used for access + sensitivity decisions. It is:
- assigned during promotion / publishing,
- carried through catalogs and API responses (public-safe),
- used to drive **default deny** behavior for restricted classes.

### Policy decision
A decision is a structured evaluation result (at minimum):
- `decision`: `allow` or `deny`
- `policy_label`: classification input
- `reason_codes`: codes suitable for audit + UX (policy-safe)
- `obligations`: required transforms or notices
- `rule_id`: stable identifier for the deciding rule

### Obligation
An obligation is a machine-readable requirement that must be applied before serving or publishing:
- redaction (remove attributes, suppress fields),
- generalization (geometry coarsening, aggregation thresholds),
- UI notices (e.g., “generalized due to policy”),
- logging/audit constraints.

### EvidenceRef and EvidenceBundle
In KFM:
- a “citation” is an **EvidenceRef** (not a pasted URL),
- EvidenceRefs must resolve (via the evidence resolver) into **EvidenceBundles** containing metadata, provenance, artifacts, and policy decision info,
- if citations can’t be resolved and policy-allowed, the system must narrow scope or abstain.

[⬆️ Back to top](#policy-context)

---

## Policy label taxonomy
This is the **starter** controlled vocabulary (extend via governed change):

| policy_label | Intended visibility | Typical handling |
|---|---|---|
| `public` | Public | Safe to list and serve. |
| `public_generalized` | Public | Serve only generalized outputs; show notice(s). |
| `restricted` | Authorized only | Deny by default; allow only for approved roles. |
| `restricted_sensitive_location` | Authorized only | Default deny; never emit precise coordinates unless explicitly allowed. |
| `internal` | Operators/stewards | Hidden from public discovery; internal tooling only. |
| `embargoed` | Time-limited restriction | Treat as restricted until embargo lifts. |
| `quarantine` | Not promotable | Block promotion; unresolved licensing/QA/sensitivity. |

> WARNING — Sensitive locations  
> If a public representation is allowed, **produce a separate** `public_generalized` dataset/version rather than weakening protections on precise data.

[⬆️ Back to top](#policy-context)

---

## Obligations

### Obligation catalog (starter)
Not exhaustive — treat as a typed contract that grows carefully.

| obligation.type | Parameters (examples) | Outcome |
|---|---|---|
| `generalize_geometry` | `min_cell_size_m`, `method` | Coarsen geometry before serving/publishing. |
| `remove_attributes` | `fields: ["exact_location", "owner_name"]` | Remove sensitive columns from outputs. |
| `show_notice` | `message` | Display required notice in UI / exports. |

### Example policy decision object
```json
{
  "decision_id": "kfm://policy_decision/xyz",
  "policy_label": "restricted",
  "decision": "deny",
  "reason_codes": ["SENSITIVE_SITE", "RIGHTS_UNCLEAR"],
  "obligations": [
    { "type": "generalize_geometry", "min_cell_size_m": 5000 },
    { "type": "remove_attributes", "fields": ["exact_location", "owner_name"] }
  ],
  "evaluated_at": "2026-02-20T12:00:00Z",
  "rule_id": "deny.restricted_dataset.default"
}
```

[⬆️ Back to top](#policy-context)

---

## PDP/PEP architecture
**Goal:** identical policy outcomes in CI and runtime.

- **PDP (Policy Decision Point):** OPA (Rego) running in-process or sidecar.
- **PEPs (Policy Enforcement Points):**
  - **CI:** policy tests + schema checks block merges.
  - **Runtime API:** policy check before serving data.
  - **Evidence resolver:** policy check before resolving and rendering evidence bundles.
  - **UI:** displays policy badges and notices; does not decide.

```mermaid
flowchart LR
  subgraph CI
    A[Repo change] --> B[Policy tests and fixtures]
    B --> C[Merge allowed]
    B --> D[Merge blocked]
  end

  subgraph Runtime
    E[Request] --> F[PEP API]
    F --> G[PDP Policy Engine]
    G --> H[Enforce obligations]
    H --> I[Evidence resolver]
    I --> J[Policy safe response]
  end
```

**Non-negotiable invariants**
- Fail closed (deny by default where classification is sensitive or unclear).
- Do not leak restricted existence via error differences.
- UI is not a decision-maker; it is a renderer of policy state and rationale.

[⬆️ Back to top](#policy-context)

---

## Change workflow
Policy changes are governance changes. Treat them like production code.

### When you change policy labels, rules, or obligations
- [ ] Update the controlled vocabulary (labels or obligation types) and rationale.
- [ ] Add/adjust **fixtures** representing the input shapes you expect.
- [ ] Add/adjust policy tests that cover allow/deny and obligations.
- [ ] Confirm CI and runtime semantics match (same fixtures, same results).
- [ ] Confirm promotion gates that depend on policy_label/obligations still fail closed.
- [ ] Confirm API error handling is policy-safe (no restricted metadata leakage).
- [ ] Confirm evidence resolution still works end-to-end for Story + Focus.

### PR template snippet (paste into your PR body)
```text
Policy change summary:
- Labels affected:
- Rules affected (rule_id):
- New/changed obligations:
- Fixtures added/updated:
- Tests added/updated:
- Expected behavior changes (who can see what):
- UX notice changes:
- Audit impact (reason_codes / logging):
```

[⬆️ Back to top](#policy-context)

---

## Directory contract

### Acceptable inputs
This directory **may contain**:
- Policy label taxonomy docs and change logs
- Obligation catalogs and semantics (what each obligation means)
- PDP/PEP architecture notes (CI + runtime alignment)
- Templates (policy decision JSON examples, UX notice copy)
- Rubrics (licensing classification, sensitivity/generalization guidance)
- Runbooks for policy review (what stewards check before approval)

### Exclusions
This directory **must not** contain:
- Actual Rego policies, policy fixtures, or policy tests (these belong with policy code, typically under `policy/`)
- Secrets, tokens, keys, or auth configs
- Restricted datasets or raw sensitive coordinates
- “Policy by rumor” (undocumented, untested rules)

### Recommended local layout (create as needed)
```text
docs/domains/contexts/policy/
  README.md                # you are here
  policy-labels.md         # definitions + rationale + change history
  obligations.md           # obligation catalog + examples
  pdp-pep.md               # enforcement points + integration notes
  decision-shapes.md       # input/output schemas for PDP decisions
  examples/
    policy-decision.json   # example allow/deny + obligations
    ui-notices.md          # standard notice text + triggers
  adr/
    ADR-xxxx-policy-*.md   # policy-related architecture decisions
```

[⬆️ Back to top](#policy-context)

---

## Glossary
- **PDP:** Policy Decision Point (evaluates policy and returns decisions)
- **PEP:** Policy Enforcement Point (calls PDP and enforces the result)
- **Policy label:** controlled vocabulary classification input
- **Obligation:** required transform/notice applied when policy allows access
- **EvidenceRef:** resolvable citation reference (not a raw URL)
- **EvidenceBundle:** resolved evidence payload including provenance + policy + license + artifacts

---
