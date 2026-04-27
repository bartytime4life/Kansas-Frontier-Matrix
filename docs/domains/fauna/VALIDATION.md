<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-register-fauna-validation
title: Fauna Validation and Gates
type: standard
version: v1
status: draft
owners: TODO(fauna-domain-stewards)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(verify-public-or-restricted)
related: [docs/domains/fauna/README.md, docs/domains/fauna/GEOPRIVACY.md, docs/domains/fauna/runbooks/release-dry-run.md]
tags: [kfm, fauna, validation, policy]
notes: [Human-readable validation contract for fixture-first fauna lane development.]
[/KFM_META_BLOCK_V2] -->

# Fauna Validation

## Validation layers

1. **Schema checks** — required fields/types and enum boundaries.
2. **Policy checks** — source role, rights, sensitivity, and release posture.
3. **Evidence checks** — claim support must resolve to admissible evidence.
4. **Publication checks** — public payloads/layers must be geoprivacy-safe.

## Minimum fixture set

| Fixture | Purpose | Expected outcome |
|---|---|---|
| Valid public-safe occurrence | Happy path for governed publication | `PASS` |
| Protected species exact geometry | Confirm fail-closed posture | `DENY` |
| Unknown source role | Enforce role requirement | `HOLD` |
| Missing rights metadata | Prevent unsafe promotion | `QUARANTINE` |
| Habitat-only support for occurrence claim | Prevent role collapse | `ABSTAIN` |

## Required PR evidence

- Validation command output (or CI link)
- Changed fixture list (if validators changed)
- Notes for any expected HOLD/ABSTAIN/DENY scenarios
- Rollback implications if publish-facing behavior changed

## Suggested command placeholders

Use repo-native tooling once finalized:

```bash
# Example placeholders; replace with canonical repo commands.
python tools/validators/fauna/run_all.py --fixtures tests/fixtures/fauna
conftest test policy/fauna tests/fixtures/fauna
```

