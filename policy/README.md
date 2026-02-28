<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8f4c5db9-1cc2-4a2f-b5b3-fb8c6a9a8e7d
title: policy/README.md
type: standard
version: v1
status: draft
owners: KFM Governance + Policy Stewards (TODO: set via CODEOWNERS)
created: 2026-02-26
updated: 2026-02-28
policy_label: public
related:
  - kfm://doc/KFM-GDG-2026  # TODO: link to in-repo copy of the Governance Guide
tags: [kfm, policy, governance, opa, rego, ci, promotion-contract]
notes:
  - Directory README for the policy bundle (CI + runtime semantics).
  - Replace <ORG>/<REPO> badge placeholders once repo metadata is known.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/` — Governed, fail-closed policy-as-code for KFM

**Purpose:** This directory contains the **policy bundle** (OPA/Rego or equivalent) that enforces KFM governance:
**access control**, **licensing/rights**, **sensitivity/redaction**, and **promotion gates** — with **the same semantics in CI and at runtime**.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Posture](https://img.shields.io/badge/posture-default--deny-critical)
![Policy-as-code](https://img.shields.io/badge/policy--as--code-Rego-blue)
![Tests](https://img.shields.io/badge/tests-required-informational)

<!-- TODO(repo): Replace <ORG>/<REPO> and workflow filenames -->
<!-- ![Policy Tests](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/policy-tests.yml?branch=main) -->
<!-- ![Conftest Gate](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/conftest.yml?branch=main) -->

> **TL;DR:** In KFM, **security is governance**. Policy is the shared source of truth for what is allowed to be served, exported, or claimed — and it must be **deterministic**, **test-covered**, and **fail-closed**.

---

## Quick navigation

- [What lives here](#what-lives-here)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Where policy sits in KFM](#where-policy-sits-in-kfm)
- [Policy decision model](#policy-decision-model)
- [Policy labels](#policy-labels)
- [Promotion Contract alignment](#promotion-contract-alignment)
- [Making changes](#making-changes)
- [Testing](#testing)
- [Directory layout](#directory-layout)
- [FAQ](#faq)

---

## What lives here

### ✅ Acceptable inputs

What belongs in `policy/`:

- **Policy code** (e.g., Rego packages) for:
  - authorization (role/label/action rules)
  - rights/licensing enforcement
  - sensitivity + redaction/generalization obligations
  - promotion gating decisions (fail closed)
  - policy-safe error shaping (no restricted inference)
- **Fixtures** representing policy decisions:
  - allow/deny outcomes
  - obligations arrays
  - stable reason codes for auditability
- **Policy tests**:
  - OPA unit tests (`opa test`)
  - and/or Conftest tests used as PR gates
- **Rubrics** used as policy inputs:
  - licensing classification rubric
  - sensitivity rubric + generalization guidance
- **Controlled vocabularies** referenced by policy:
  - `policy_label` list
  - obligation types and reason codes (recommended)

### 🚫 Exclusions

What must **not** go in `policy/`:

- **Secrets** (API keys, credentials, private tokens).
- **Raw datasets** or restricted artifacts (policy should reference **metadata**, not embed sensitive content).
- **UI logic** (UI may display policy outcomes but must not decide policy).
- **One-off exceptions** without fixtures + tests (exceptions must become governed, testable policy).

> [!WARNING]
> If a rule cannot be tested (fixtures + tests), it is not policy — it’s a suggestion. Policy must be deterministic and CI-enforced.

[Back to top](#top)

---

## Non-negotiable invariants

These invariants align to KFM north stars. Policy must **enforce** them, not merely describe them.

### 1) Default deny

- Unknown = **deny**.
- Missing metadata = **deny** (or quarantine).
- Unhandled `policy_label` = **deny**.

### 2) Trust membrane

- Clients/UI must never gain access to storage/DB/indexes by policy loophole.
- Policy must assume access happens only through governed surfaces (API, evidence resolver, pipeline runner).
- “Allowed” must not imply “bypass”: obligations must still apply.

### 3) Evidence-first

- Any “allowed to claim/serve” decision must be compatible with evidence-first UX:
  - evidence must be resolvable (or UI must degrade/abstain)
  - license/rights must be present where required
  - provenance/receipts must be linkable where policy allows

### 4) Cite-or-abstain

- If citations cannot be verified and policy-allowed, Focus Mode must **abstain** or reduce scope.
- Policy must support (and tests must cover) abstention reasons and safe alternatives.

### 5) Promotion Contract support

- Policy participates in promotion gates and must be able to deny promotion for:
  - missing license/rights
  - missing/unclear sensitivity handling
  - missing receipts/checksums policy fields
  - missing catalogs required for the dataset class (when applicable)

### 6) Canonical vs rebuildable

- Policy must treat projections/caches as rebuildable and never as authoritative truth.
- If a projection contradicts canonical catalogs/receipts, policy should bias toward **deny** or **degrade** until resolved.

### 7) Deterministic identity and hashing

- Policy cannot depend on unstable, non-deterministic fields as decision inputs.
- Policy rules that touch identity/versioning must operate on stable identifiers (`dataset_version_id`, `spec_hash`) and be test-covered.

### 8) Policy-safe errors (no restricted inference)

- A public caller must not infer the existence of restricted resources through:
  - 403 vs 404 differences
  - different error messages
  - different payload shapes
  - “helpful” metadata in errors
- Policy should support an indistinguishable, safe error posture for restricted objects.

[Back to top](#top)

---

## Where policy sits in KFM

Policy is part of the **trust membrane**. It is enforced in CI (PR gates) and at runtime (API + evidence resolver).

```mermaid
flowchart LR
  subgraph CI["CI / PR Gate (Policy Enforcement Point)"]
    PR["Pull Request"] --> Gate["Policy gate (Conftest or OPA)"]
    Gate --> CIResult["Pass or Fail (closed)"]
  end

  subgraph Runtime["Runtime (Policy Enforcement Points)"]
    API["Governed API (PEP)"] --> PDP["Policy Decision Point (OPA/Rego PDP)"]
    ER["Evidence Resolver (PEP)"] --> PDP
    Pipe["Pipeline Runner / Promotion (PEP)"] --> PDP
  end

  UI["Map / Story / Focus UI"] --> API
  UI --> ER

  CIResult --> Merge["Merge allowed only if gates pass"]
```

**Key posture**
- CI must **block merges** when policy denies.
- Runtime must **fail closed** when policy cannot evaluate or evidence cannot be resolved.
- UI must **display** policy outcomes (labels/obligations) but **never** decide authorization.

[Back to top](#top)

---

## Policy decision model

A policy evaluation should return a **decision envelope** that is stable, auditable, and easy to test.

### Required decision fields

- `decision`: `allow | deny` *(default deny)*
- `policy_label`: controlled vocabulary string for the resource
- `obligations[]`: required follow-up actions (redaction, notices, export constraints)
- `reason_codes[]`: stable identifiers (for audit + debugging without leaking sensitive info)

> [!NOTE]
> Obligations are part of the decision and must be captured in run receipts/audit logs.

### Obligations (examples)

Obligations make “allowed” safe:

- `show_notice`: UI must show a banner (e.g., “generalized due to policy”).
- `redact_fields`: evidence resolver must redact before returning.
- `force_generalization`: serve a `public_generalized` derivative only.
- `suppress_export`: block downloads/exports for the caller/action.
- `require_attribution`: exports must include license + attribution text.
- `rate_limit_class`: apply stricter limits for public endpoints.
- `log_audit`: require audit emission for this action.

### Policy-safe error shaping

Policy should support a safe error model that avoids restricted inference. A common approach:

- **Public caller:** return a “not found or not permitted” generic error for restricted targets.
- **Authorized steward/operator:** return explicit deny with reason codes and remediation hints.

> [!WARNING]
> Do not include restricted labels, precise coordinates, or rights-holder details in public error responses.

[Back to top](#top)

---

## Policy labels

Policy labels are controlled vocabulary values attached to datasets, stories, and evidence bundles.

| `policy_label` | Meaning | Default posture | Typical obligations |
|---|---|---|---|
| `public` | Safe for public display/download | allow for public `read` | require_attribution, rate_limit_class |
| `public_generalized` | Public-safe derived representation | allow for public `read` | show_notice, provenance link to redaction |
| `internal` | Visible to authenticated org users | deny to public | log_audit |
| `restricted` | Access limited to stewards/authorized roles | deny by default | policy_safe_error, log_audit |
| `restricted_sensitive_location` | Restricted + location-sensitive | deny by default | force_generalization, redact_fields, policy_safe_error |
| `embargoed` | Hidden until date/review | deny by default | embargo_until, log_audit |
| `quarantine` | Not promotable/servable | deny always | remediation_hint |

> [!IMPORTANT]
> Adding a new `policy_label` is a governance change:
> update vocabulary → update fixtures → update tests → update dependent validators/exports.

[Back to top](#top)

---

## Promotion Contract alignment

Policy is a hard dependency of the KFM Promotion Contract. Promotion must be **blocked** unless required artifacts exist and validate.

### Gate map (how policy participates)

| Promotion gate | Policy participation (examples) |
|---|---|
| Identity & versioning | deny if required IDs/spec-hash inputs missing or invalid |
| Licensing & rights | deny if license/rights/attribution missing or incompatible with intended distribution |
| Sensitivity & redaction plan | deny if restricted/sensitive lacks a recorded generalization/redaction plan |
| Catalog triplet validation | policy can deny serving/promotion if required catalog fields missing (even if schema-valid) |
| Run receipt & checksums | deny if receipts lack required policy fields or checksums are incomplete |
| Policy tests & contract tests | deny merge/promotion if fixtures-driven tests fail; deny if evidence cannot resolve in CI for allowed roles |
| Exports & redistribution | deny export if rights/policy forbid, or if obligations require suppression/generalization |

### Promotion-critical rule of thumb

If the system cannot answer **“Is it safe and permitted to publish?”** deterministically, the correct result is **deny/quarantine**.

[Back to top](#top)

---

## Making changes

Policy changes are governance changes. Treat them with the same discipline as schema/API changes.

### Change rules (non-negotiable)

- **No silent changes:** every change must add/modify **fixtures** and **tests**.
- **Fail closed:** unhandled labels/actions default to **deny**.
- **CI/runtime parity:** outcomes must match between CI evaluation and runtime PDP evaluation.
- **Policy-safe outputs:** no restricted inference through error models or payload differences.

### PR checklist (policy)

- [ ] Rego change includes stable `reason_codes` (or documented rationale).
- [ ] Fixtures cover decision **and obligations** (not just allow/deny).
- [ ] Tests cover at least:
  - public role (deny-by-default posture)
  - steward role (explicit allows where intended)
  - restricted existence inference protections
  - export/download constraints (rights + obligations)
- [ ] If vocab changed: update vocab files + downstream fixtures.
- [ ] Steward review requested and recorded (via CODEOWNERS / reviewers).

> [!TIP]
> Prefer adding new rules behind fixtures, then expanding coverage, before widening allow conditions.

[Back to top](#top)

---

## Testing

Wire these into `make test-policy` (or equivalent) so local + CI runs are identical.

### Option A — OPA unit tests (Rego)

```bash
# Run all rego tests (adjust paths to your repo conventions)
opa test -v policy/rego policy/tests
```

### Option B — Conftest gate (PR gate)

```bash
# Validate a directory of fixtures/manifests against rego policies
conftest test -p policy/rego policy/fixtures
```

### Required CI behavior

- Policy tests **must run in CI** and **block merges** on failure.
- Denies must emit actionable output:
  - stable `reason_code`
  - policy-safe remediation hint (no leaks)

[Back to top](#top)

---

## Directory layout

This is a recommended, validator-friendly starting structure. Adjust if your repo differs, but preserve:
**rego + fixtures + tests + vocab + rubrics**.

```text
policy/
├─ README.md
│
├─ rego/                                          # Policy packages (OPA/Rego)
│  ├─ kfm/                                        # Namespace root (recommended)
│  │  ├─ authz.rego                               # allow/deny rules + decision envelope
│  │  ├─ labels.rego                              # label semantics helpers
│  │  ├─ obligations.rego                         # obligation derivation rules
│  │  ├─ rights.rego                              # license/rights enforcement
│  │  ├─ sensitivity.rego                         # sensitive location + redaction/generalization rules
│  │  ├─ promotion.rego                           # promotion gate participation (deny if missing requirements)
│  │  └─ errors.rego                              # policy-safe error shaping
│  └─ _shared/                                    # Common helpers (canonicalization, set ops, etc.)
│
├─ fixtures/                                      # Deterministic decision fixtures (synthetic; safe-by-default)
│  ├─ inputs/                                     # Inputs to policy evaluation (user/action/resource/context)
│  │  ├─ public_read_public_dataset.json
│  │  ├─ public_read_restricted_dataset.json
│  │  ├─ steward_read_restricted_dataset.json
│  │  ├─ public_export_public_dataset.json
│  │  └─ focus_public_query_restricted_context.json
│  └─ expected/                                   # Expected decision envelopes
│     ├─ public_read_public_dataset.decision.json
│     ├─ public_read_restricted_dataset.decision.json
│     ├─ steward_read_restricted_dataset.decision.json
│     ├─ public_export_public_dataset.decision.json
│     └─ focus_public_query_restricted_context.decision.json
│
├─ tests/                                         # Rego unit tests (or conftest rules)
│  ├─ authz_test.rego
│  ├─ obligations_test.rego
│  ├─ rights_test.rego
│  ├─ sensitivity_test.rego
│  ├─ promotion_test.rego
│  └─ policy_safe_errors_test.rego
│
├─ vocab/                                         # Controlled vocabulary lists (versioned; referenced by policy + CI)
│  ├─ policy_labels.v1.yml
│  ├─ obligations.v1.yml
│  └─ reason_codes.v1.yml
│
└─ rubrics/                                       # Human-readable + machine-referenced policy inputs
   ├─ licensing.md                                # SPDX handling + attribution requirements
   └─ sensitivity.md                              # sensitivity rubric + generalization guidance
```

> [!NOTE]
> If your repo keeps label/obligation definitions under `configs/policy/**`, keep this directory as **enforcement logic** and treat `configs/` as **inputs** (still validated + versioned).

[Back to top](#top)

---

## FAQ

### Why “default deny”?

Because “unknown” is not the same as “allowed.” Default deny prevents accidental leakage and forces explicit governance decisions.

### Why obligations?

Some “allowed” results are only safe when accompanied by safeguards (notices, generalization, redaction, export controls). Obligations make those safeguards enforceable.

### Can the UI decide policy?

No. UI can only render policy outcomes and trust badges/notices. Authorization, redaction, and export decisions happen behind the trust membrane.

### What happens when evidence can’t be verified?

For Focus Mode and other citation-bearing surfaces: **abstain or reduce scope**. Do not guess; do not fabricate citations; do not bypass the evidence resolver.

[Back to top](#top)

---

## Appendix (optional reference)

<details>
<summary><strong>Suggested policy input shape (illustrative)</strong></summary>

```json
{
  "user": { "principal": "user:alice", "role": "public", "groups": [] },
  "action": "read",
  "resource": {
    "type": "dataset",
    "dataset_version_id": "2026-02.abcd1234",
    "policy_label": "public"
  },
  "context": {
    "purpose": "browse",
    "view_state": {
      "bbox": [-102.0, 36.9, -94.6, 40.0],
      "time_window": { "start": "1950-01-01", "end": "2024-12-31" }
    }
  }
}
```
</details>

<details>
<summary><strong>Minimal Rego skeleton (illustrative)</strong></summary>

```rego
package kfm.authz

default decision := {
  "decision": "deny",
  "policy_label": input.resource.policy_label,
  "obligations": [],
  "reason_codes": ["DEFAULT_DENY"]
}

decision := out {
  allow
  out := {
    "decision": "allow",
    "policy_label": input.resource.policy_label,
    "obligations": obligations,
    "reason_codes": ["ALLOW_MATCHED_RULE"]
  }
}

allow {
  input.user.role == "steward"
}

allow {
  input.user.role == "public"
  input.action == "read"
  input.resource.policy_label == "public"
}

obligations[o] {
  input.resource.policy_label == "public_generalized"
  o := {"type": "show_notice", "message": "Geometry generalized due to policy."}
}
```
</details>

[Back to top](#top)
