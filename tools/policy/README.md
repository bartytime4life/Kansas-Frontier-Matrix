# tools/policy

![KFM](https://img.shields.io/badge/KFM-governed%20artifacts-blue)
![Policy](https://img.shields.io/badge/policy-deny--by--default-red)
![OPA](https://img.shields.io/badge/OPA-Rego-black)
![Conftest](https://img.shields.io/badge/Conftest-CI%20gate-informational)

Policy-as-code tooling for **KFM governance gates**.

This directory is the canonical home for:
- **OPA/Rego policy packs** used to block promotion/merge when governance requirements are not met.
- **Local + CI runners** (Conftest/OPA) for deterministic, explainable policy evaluation.
- **Fixtures + tests** so policy behavior is reviewable, reproducible, and auditable.

> [!IMPORTANT]
> KFM policy is not “documentation.” It is **system behavior**. Treat policy changes as production changes:
> - require review,
> - require tests,
> - pin tool versions,
> - and maintain an audit trail of policy bundle versions.

---

## Why this exists

KFM’s repo wiring converges on a governance-by-construction loop where policy gates are **merge-blocking** and **fail closed** (default deny). These gates enforce:
- required metadata and provenance fields (e.g., STAC/DCAT/PROV),
- license/restriction rules (e.g., SPDX allow-lists),
- sensitivity/CARE constraints (e.g., restricted locations, consent),
- and runtime authorization defaults (every API call must be explicitly allowed).

---

## Non-negotiable invariants

> [!NOTE]
> These are KFM “musts” — if violated, the system’s guarantees degrade.

1. **Deny by default**  
   If a policy input is missing/unknown/ambiguous → deny.

2. **Explainable denies**  
   Failure output must clearly state:
   - what failed,
   - where it failed (field/path),
   - and how to remediate.

3. **CI and runtime must agree**
   CI gates and runtime authorization must share the same **core rules** (or at minimum identical semantics + fixtures).  
   Otherwise the repo cannot claim system-level governance.

4. **Governed versioning**
   Policy bundles are versioned artifacts:
   - track commit SHA / digest,
   - and include the policy bundle identity in receipts / audit records.

5. **No trust-membrane bypass**
   UI and external clients do **not** access storage directly.  
   Access decisions happen at the governed API boundary with policy enforcement.

---

## Directory layout

> [!TIP]
> The KFM docs propose a `policy/` folder at repo root; some CI wiring references `tools/validation/policy`.
> If your repo standardizes on `tools/policy/`, keep CI pointers consistent (symlink or update workflow paths).

Recommended structure (adapt as needed):

```text
tools/policy/
├─ README.md
├─ rego/
│  ├─ bundles.rego
│  ├─ common/
│  │  ├─ helpers.rego
│  │  └─ license_allowlist.rego
│  ├─ catalogs/
│  │  ├─ stac_required.rego
│  │  ├─ dcat_required.rego
│  │  └─ prov_required.rego
│  ├─ receipts/
│  │  ├─ receipt_invariants.rego
│  │  └─ receipts_pr_gate.rego
│  ├─ care/
│  │  └─ tribal_boundary_gate.rego
│  ├─ runtime/
│  │  └─ authz.rego
│  └─ focus/
│     └─ cite_or_abstain.rego
└─ tests/
   ├─ *_test.rego
   └─ samples/
      ├─ receipts/
      ├─ catalogs/
      ├─ promotion/
      └─ focus/
```

---

## Policy registry (starter)

| Policy pack | Stage | Input | Decision shape | Notes |
|---|---|---|---|---|
| `catalogs/*_required.rego` | CI (PR gate) | STAC/DCAT/PROV JSON | `allow`, `deny_reasons[]` | Required fields, required links, minimal profiles |
| `common/license_allowlist.rego` | CI (PR gate) | DCAT + license metadata | `allow`, `deny_reasons[]` | SPDX allowlist / restrictions-as-policy |
| `receipts/*.rego` | CI (PR gate) | `run_receipt` JSON | `allow`, `deny_reasons[]` | Receipt invariants + provenance completeness |
| `care/tribal_boundary_gate.rego` | CI + runtime | promotion manifest + provenance facets | `allow`, `deny_reasons[]`, `requires_consent` | Blocks public promotion when consent is required |
| `runtime/authz.rego` | Runtime | `{user, request, resource}` | `allow`, `deny_reasons[]`, `redactions[]` | Baseline RBAC + dataset access level + ownerGroup |
| `focus/cite_or_abstain.rego` | Runtime (AI) | Focus output payload | `allow`, `deny_reasons[]` | Missing citations ⇒ policy deny/refusal |

---

## Running locally

### Prereqs
- `conftest` (pinned in CI)
- `opa` (recommended for debugging + unit tests)

### Common workflows

#### 1) Run policy checks on an input (Conftest)
```bash
# Example: run policy packs against a JSON input
conftest test \
  --policy tools/policy/rego \
  tools/policy/tests/samples/receipts/valid.run_receipt.json
```

#### 2) Run Rego unit tests (OPA)
```bash
opa test tools/policy/rego tools/policy/tests -v
```

#### 3) Debug a decision (OPA eval)
```bash
opa eval \
  --data tools/policy/rego \
  --input tools/policy/tests/samples/focus/output_missing_citations.json \
  "data.kfm.allow"
```

> [!WARNING]
> Keep policy evaluation **deterministic**. Avoid time-dependent logic unless the input explicitly carries timestamps.

---

## CI integration

KFM’s baseline recommends a **Conftest-based PR gate** that blocks merges on policy failure and supports a repo/environment kill-switch. Ensure:
- the workflow points at this directory (or a stable alias),
- tool versions are pinned,
- and policy updates are reviewed like production code.

Minimal expectation:
- Every PR touching governed artifacts runs the policy gate.
- Branch protection requires the gate to pass.
- A kill-switch exists and is tested (forcing the gate to fail quickly).

---

## Inputs and decision shapes

### Standard decision object

Policies should return a structured decision object, not just a boolean, e.g.:

```json
{
  "allow": false,
  "deny_reasons": [
    {
      "code": "MISSING_FIELD",
      "path": "properties.kfm:artifact_digest",
      "message": "Required provenance field is missing."
    }
  ],
  "requires_consent": false,
  "redactions": []
}
```

### Example: “promotion manifest” (policy input)
Use a single, explicit input shape for promotion gating so CI and runtime share semantics:

```json
{
  "artifact": {
    "labels": {
      "kfm.data_sensitivity": "restricted",
      "kfm.care.tribal_boundary_intersection": "true"
    }
  },
  "provenance": {
    "facets": {
      "tribal_consent": {
        "status": "missing",
        "scope": null,
        "expires_at": null
      }
    }
  },
  "promotion": {
    "intended_exposure": "public"
  }
}
```

---

## Adding a new policy pack

1. **Define the contract**
   - What is the input object?
   - What is the decision object?
   - What are the invariants?

2. **Implement the Rego**
   - Default deny (explicit).
   - Emit remediation-friendly messages.

3. **Add tests**
   - `*_test.rego` unit tests for edge cases.
   - JSON fixtures in `tests/samples/`:
     - at least 1 valid allow,
     - at least 2 denies (missing field, invalid value),
     - and at least 1 “sensitive” regression fixture.

4. **Wire into bundles**
   - Update `rego/bundles.rego` (or bundle index) so CI loads it.

5. **Update the registry table**
   - Keep this README accurate.

6. **Governance review**
   - If the policy affects public narrative, sensitive locations, or community authority-to-control:
     - require governance council / data steward review before merge.

---

## CARE and sensitive locations

Some datasets (e.g., heritage/archaeology) require special handling:
- generalize location,
- restrict visibility,
- or require explicit consent before promotion.

Policies must support:
- “authority to control” constraints (e.g., `ownerGroup` access rules),
- takedown/withdrawal status denial,
- and “public vs internal vs restricted” exposure logic.

---

## Focus Mode and “cite or abstain”

KFM’s Focus Mode posture is: **cite every factual claim or abstain**.

Policy hooks should enforce that:
- the AI output contains at least one citation object,
- citations resolve to evidence (or produce correct 403/404),
- and sensitive fields are redacted/generalized with surfaced CARE/sensitivity flags.

If citations cannot be produced, the system must refuse output rather than hallucinate.

---

## Governance checklist (PR-ready)

- [ ] Policy gate is merge-blocking.
- [ ] Default deny behavior is covered by tests.
- [ ] Deny messages are readable and remediation-focused.
- [ ] Fixtures include sensitive-data regression cases (no leakage through logs/receipts).
- [ ] Tool versions are pinned (Conftest/OPA).
- [ ] Kill-switch is documented and tested.
- [ ] Policy bundle identity is included in receipts/audit metadata.

---

## Troubleshooting

**“Conftest can’t find policies”**
- Confirm the CI/workflow points to `tools/policy/rego` (or your canonical path).
- Confirm bundle/index file includes the new module.

**“OPA test passes but CI fails”**
- CI and local tool versions may differ.
- Ensure pinned versions and identical policy roots.

**“Policy denies unexpectedly”**
- Inspect `deny_reasons[]` first.
- If the deny is ambiguous, improve the message and add a fixture.

---

## Related KFM artifacts (typical)

- `schemas/` — JSON Schemas for receipts/manifests/watchers (contracts-first)
- `ops/` — playbooks for evidence distribution, signing/attestation
- `.github/workflows/` — CI policy gate + reusable lane runners

> Keep policy, schemas, and receipts aligned: contracts-first → fail-closed gates → evidence distribution → UI trust badges.