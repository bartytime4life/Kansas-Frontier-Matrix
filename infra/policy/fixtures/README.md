# 🧱 KFM Policy Fixtures (infra/policy/fixtures)

![Governed](https://img.shields.io/badge/Governed-Evidence--first-2ea44f)
![Policy](https://img.shields.io/badge/Policy-OPA%2FConftest-blue)
![Fixtures](https://img.shields.io/badge/Fixtures-Golden%20pass%2Ffail-orange)

This directory contains **redaction-safe**, **deterministic** fixtures used to test KFM policy bundles (typically **OPA/Rego** evaluated via **Conftest**) in **CI** and locally.

Fixtures are how we make governance **enforceable** instead of “policy-by-document”: if a fixture fails, **merge/promotion should fail**.

---

## Why fixtures exist

Policy fixtures support three non-negotiables:

1. **Fail-closed governance**  
   Policies should deny by default and only allow when required evidence, rights, provenance, and sensitivity rules are satisfied.

2. **Regression protection**  
   Every time a policy changes, fixtures ensure we didn’t accidentally:
   - loosen a gate
   - break a legitimate allow-case
   - introduce a new data leak pathway

3. **Safety-first testing** (“known leak fixtures”)  
   We maintain explicit *negative* examples that should never pass—especially for sensitive-location and re-identification risks.

---

## 🚨 Safety rules for fixtures

> [!IMPORTANT]
> **Fixtures MUST NOT contain real restricted locations, PII, partner-only data, API keys, secrets, or unredacted archival content.**  
> Fixtures should be **synthetic**, **obviously fake**, or **heavily generalized** so that the repository remains safe to publish and share.

**Rules of thumb**
- ✅ Use placeholder coordinates (e.g., `0,0`) or clearly synthetic geometries.
- ✅ Use mock dataset identifiers and mock URLs (never private endpoints).
- ✅ Prefer minimal JSON/YAML shaped to the policy contract.
- ❌ Never include precise archaeology site coordinates or “real-but-sensitive” examples.
- ❌ Never include “just a little” personal data; fixtures live forever.

---

## Recommended directory layout

This folder is intentionally fixture-only. Keep fixtures grouped by the *policy concern* being tested.

```text
infra/policy/fixtures/
├── README.md
├── _meta/
│   ├── fixtures.index.yml          # (optional) human+CI-friendly index of cases
│   └── README.md                   # (optional) how the index is validated
├── receipts/                       # run_receipt / run_manifest / promotion receipts
│   ├── allow__minimal.json
│   ├── deny__missing_spec_hash.json
│   └── deny__missing_rights.json
├── catalogs/
│   ├── stac/
│   │   ├── allow__item_minimal.json
│   │   └── deny__missing_prov_link.json
│   ├── dcat/
│   │   ├── allow__dataset_minimal.json
│   │   └── deny__missing_license.json
│   └── prov/
│       ├── allow__run_minimal.jsonld
│       └── deny__broken_lineage.jsonld
├── sensitivity/
│   ├── allow__public.json
│   ├── deny__restricted_unredacted.json
│   └── deny__sensitive_location_precise_coords.json
└── leak/                           # explicit “known leak” negative cases
    ├── deny__precise_coords_present.json
    ├── deny__small_area_reid_risk.json
    └── deny__unlicensed_export.json
```

> [!NOTE]
> The exact subfolders can vary—what matters is that fixtures stay **small**, **legible**, and **tied to a single policy intent**.

---

## Fixture conventions

### Naming

Use names that encode the expected outcome:

- `allow__<case>.json`  → should **pass** (no denies)
- `deny__<case>.json`   → should **fail** (at least one deny)

Keep `<case>` in `lower_snake_case`.

### Minimalism

Fixtures should include **only** what the policy needs to evaluate.  
This reduces noise and prevents accidental coupling to irrelevant fields.

### Determinism

- Avoid timestamps like “now”
- Avoid random IDs
- Prefer stable, readable, test-only IDs

### “Why” is part of the fixture

Recommended: add a short sidecar note for any non-obvious case.

```text
deny__sensitive_location_precise_coords.json
deny__sensitive_location_precise_coords.md   # explains the rule and expected deny reason(s)
```

---

## Running policy checks

> [!TIP]
> These are common patterns. Adjust paths if your policy bundle lives somewhere other than `infra/policy/opa`.

### Conftest (common for CI gates)

```sh
# From repo root:
conftest test infra/policy/fixtures --policy infra/policy/opa
```

Run a single fixture:

```sh
conftest test infra/policy/fixtures/receipts/deny__missing_spec_hash.json --policy infra/policy/opa
```

### OPA unit tests (if using *_test.rego)

```sh
# Run Rego unit tests (if present):
opa test infra/policy/opa -v
```

---

## Adding a new fixture

Use this checklist whenever you add or modify fixtures.

### ✅ Fixture Definition of Done

- [ ] A new policy rule has **both**:
  - [ ] at least **one allow fixture**
  - [ ] at least **one deny fixture**
- [ ] The fixture is **redaction-safe** (no sensitive content).
- [ ] The fixture is **minimal** (only required fields).
- [ ] The fixture name clearly encodes expected outcome (`allow__` / `deny__`).
- [ ] (Recommended) A short `.md` sidecar explains:
  - [ ] what policy concern is being tested
  - [ ] expected deny reason(s) for `deny__*`
- [ ] CI/local policy test command passes.

---

## What we typically gate with fixtures

| Policy concern | What must be true (examples) | Fixture area |
|---|---|---|
| Rights & licensing | license present; restrictions respected; deny unknown/empty | `catalogs/dcat/`, `leak/` |
| Provenance completeness | required provenance links/keys exist; no broken lineage | `catalogs/prov/`, `catalogs/stac/` |
| Receipt invariants | required fields exist (e.g., spec hash, rights, attestations) | `receipts/` |
| Sensitivity handling | restricted data never returns precise details; redaction required | `sensitivity/`, `leak/` |
| “Known leak” regressions | explicit negative cases must always deny | `leak/` |

---

## Troubleshooting

### “I changed policy and now an allow fixture fails”
- Confirm the allow-case is still valid under governance rules.
- If the policy change is intentional, update the allow fixture **and** add a new deny fixture capturing the old unsafe path.

### “A deny fixture started passing”
Treat as **high severity**:
- This likely means a gate weakened or a rule stopped triggering.
- Add/restore the deny condition and ensure CI blocks merges.

### “Fixture is too big / unreadable”
Split it:
- One fixture = one policy intent
- Prefer 2–3 tiny fixtures over one giant fixture

---

## Governance note

Policy fixtures are governed artifacts. They define *what the system is allowed to do* and therefore:
- must be reviewable
- must be safe to share
- must be stable over time

If a fixture relates to sensitive location handling, re-identification risk, or partner restrictions, flag it for governance review.

---
