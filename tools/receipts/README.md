# tests/receipts

![Governed](https://img.shields.io/badge/governed-yes-2ea44f)
![Evidence-First](https://img.shields.io/badge/evidence--first-required-blue)
![Fail-Closed](https://img.shields.io/badge/gates-fail--closed-critical)

> [!IMPORTANT]
> **These are test fixtures.** They are intentionally small, synthetic “receipts” used to prove KFM’s governance rules (schemas + policy-as-code) behave correctly.
> 
> Treat everything in `tests/receipts/` as **publishable**: **never** commit secrets, private identifiers, or precise sensitive locations.

## Why this folder exists

KFM’s promotion and serving model depends on **receipts**: machine-checkable artifacts that explain *what ran*, *what inputs were used*, *what was produced*, and *why it is allowed to ship*.

This directory provides:

- **Golden pass fixtures** (should validate and be allowed)
- **Golden fail fixtures** (should be denied by policy and/or rejected by schema validation)
- Stable examples used by CI to prevent **silent drift** in:
  - receipt schemas (`run_receipt`, `run_manifest`, `validation_report`, etc.)
  - OPA/Conftest policies (promotion gates, required fields, deny-by-default posture)
  - deterministic identity (`spec_hash`) and idempotency invariants

## Directory layout

```text
tests/receipts/
  README.md

  golden/
    valid/
      run_receipt.v1.json
      run_manifest.v1.json
      validation_report.v1.json

    invalid/
      run_manifest.missing_rights.v1.json
      run_manifest.missing_signatures.v1.json
      run_receipt.schema_break.v1.json

  fixtures/
    minimal/
      ...
    edge_cases/
      ...
```

> [!NOTE]
> The exact filenames are conventions, not constraints. What matters is that fixtures are **deterministic**, **small**, and **clearly named for the rule they test**.

## Receipt types (contract quick reference)

| Artifact | What it proves | Typical gate(s) it feeds | “Must not include” |
|---|---|---|---|
| `run_receipt` | A pipeline run occurred and captured inputs/outputs as evidence | Schema validation; policy invariants; audit linking | Secrets, tokens, unredacted PII, precise restricted locations |
| `run_manifest` | A promotion candidate is complete: signatures/attestations/rights exist; stable `spec_hash` is present | PR merge gate; promotion contract | Same as above + any direct DB credentials |
| `validation_report` | Validators ran and results are preserved (STAC/DCAT/PROV checks, QA metrics, etc.) | “Required checks” evidence; UI “why trust this?” drawer | Raw source payloads; large logs |

### Required fields (example)

Some gates intentionally require `run_manifest` to carry **minimum evidence** (fail-closed). A typical rule set expects fields like:

- `spec_hash`
- `signatures`
- `attestations`
- `rights`
- `rekor_uuid` (or equivalent transparency-log reference)

> [!TIP]
> When you update a required field list in policy, add **two fixtures**:
> 1) a valid manifest that includes the new field
> 2) an invalid manifest missing the field (must fail)

## How fixtures are used in tests

```mermaid
flowchart LR
  A[Fixture JSON in tests/receipts] --> B[Schema validation]
  A --> C[OPA/Conftest policy checks]
  B --> D{Pass?}
  C --> E{Allowed?}
  D -- yes --> F[Golden-valid stays valid]
  D -- no --> G[Golden-invalid stays invalid]
  E -- yes --> F
  E -- no --> G

  F --> H[CI green ✅]
  G --> I[CI red ❌ (fail-closed)]
```

## Fixture rules (non-negotiable)

### ✅ Deterministic

- Use fixed timestamps (or omit them) in fixtures.
- Keep JSON key ordering stable.
- If you compute hashes (like `spec_hash`), document the algorithm in the fixture comment block or accompanying `.md` note.

### ✅ Minimal & focused

- Each fixture should test **one rule** (or a tight cluster of related invariants).
- Prefer small payloads that isolate the failure.

### ✅ No sensitive data

> [!WARNING]
> Receipts are a common source of accidental leakage (URLs with tokens, email addresses, internal bucket paths, or precise site coordinates).

Scrub or replace:

- access tokens / API keys / cookies
- personal names, emails, phone numbers
- precise coordinates for restricted heritage/safety features
- internal hostnames, private bucket paths

If a test truly needs “realistic” values, use **synthetic placeholders**:

- `user@example.invalid`
- `00000000-0000-0000-0000-000000000000`
- coordinates snapped/rounded to coarse precision

## Adding a new receipt fixture

1. **Name the rule you are testing** in the filename.
   - ✅ `run_manifest.missing_rights.v1.json`
   - ❌ `bad1.json`
2. Add a **golden valid** and **golden invalid** case.
3. Add/extend tests that:
   - assert valid fixtures pass schema validation
   - assert invalid fixtures fail schema validation *or* are denied by policy
   - assert policy is **deny-by-default** when required evidence is missing
4. Run the local checks (examples below) and ensure CI will enforce them.

## Local validation (example commands)

> [!NOTE]
> Commands vary by repo tooling. Keep this section aligned with the project’s actual test runner.

```bash
# 1) JSON Schema validation (example)
# jq is only used here to ensure JSON parses; schema validation depends on your chosen tool.
jq -e . tests/receipts/golden/valid/run_manifest.v1.json > /dev/null

# 2) Policy-as-code (OPA/Conftest) example
conftest test tests/receipts/golden/valid/run_manifest.v1.json --policy policy/opa
conftest test tests/receipts/golden/invalid/run_manifest.missing_rights.v1.json --policy policy/opa
```

## Definition of Done for receipt-related changes

- [ ] Schema change includes updated fixtures **and** a failing fixture that proves the rule.
- [ ] Policy change includes updated fixtures **and** unit tests for the policy.
- [ ] CI fails closed on:
  - missing receipts/manifests
  - missing required fields
  - invalid signatures/attestations (when applicable)
- [ ] No fixture contains secrets/PII/sensitive coordinates.
- [ ] Fixtures remain small and deterministic.

---

### Footnotes

1. `spec_hash` should be computed using a deterministic canonicalization strategy to prevent hash drift (for JSON, RFC 8785 JCS is the typical choice).
