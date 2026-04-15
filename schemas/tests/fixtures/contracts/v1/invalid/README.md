<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Contract Fixtures v1 — Invalid
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS-VERIFICATION
updated: 2026-04-14
policy_label: public
related: [
  ../README.md,
  ../valid/README.md,
  ../../../../../schemas/contracts/v1/hydro_identity_bridge.schema.json,
  ../../../../../schemas/contracts/v1/hydro_join_receipt.schema.json,
  ../../../../../contracts/README.md,
  ../../../../../contracts/hydro_mapping/README.md,
  ../../../../../tests/README.md,
  ../../../../../tests/contracts/README.md,
  ../../../../../policy/README.md
]
tags: [kfm, schemas, tests, fixtures, contracts, v1, invalid, hydrology]
notes: [
  Negative fixture leaf for schemas/tests/fixtures/contracts/v1.
  Focused on deterministic failure conditions for hydro thin-slice contracts.
  Preserves scaffold-boundary posture while making failure cases explicit.
]
[/KFM_META_BLOCK_V2] -->

# Contract Fixtures v1 — Invalid

Negative fixture leaf for `schemas/tests/fixtures/contracts/v1/invalid/`.

This directory contains **fail-expected contract examples**.

> [!IMPORTANT]
> An invalid fixture is not random bad JSON.  
> It is a **deliberate, named failure case** that proves a contract rejects incorrect input for a specific reason.

> **Status:** experimental  
> **Doc status:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** `schemas/tests/fixtures/contracts/v1/invalid/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange)
> ![doc](https://img.shields.io/badge/doc-draft-lightgrey)
> ![leaf](https://img.shields.io/badge/leaf-invalid-red)
> ![focus](https://img.shields.io/badge/focus-fail--expected%20fixtures-b60205)

**Repo fit:** parent [`../README.md`](../README.md) · sibling [`../valid/README.md`](../valid/README.md) · paired schemas [`../../../../../schemas/contracts/v1/hydro_identity_bridge.schema.json`](../../../../../schemas/contracts/v1/hydro_identity_bridge.schema.json), [`../../../../../schemas/contracts/v1/hydro_join_receipt.schema.json`](../../../../../schemas/contracts/v1/hydro_join_receipt.schema.json)

---

## Scope

`invalid/` holds fixtures that should **fail deterministically**.

For the current hydrology thin slice, this means:

- failing identity bridge objects
- failing join receipt objects

This directory is **not**:

- a dump of malformed JSON
- a policy engine
- a validator implementation
- a release artifact store

---

## Current fixtures

### `hydro_identity_bridge.legacy-only-without-basis.v1.json`

**Pairs with:**  
`hydro_identity_bridge.schema.json`

**Failure condition:**
- `comid_legacy` is present
- but **no `crosswalk_basis` or `crosswalk_version` is declared**

**What it proves:**
Legacy compatibility must be **explicitly justified** — it cannot silently coexist with current identity.

---

### `hydro_join_receipt.crosswalk-missing-bridge.v1.json`

**Pairs with:**  
`hydro_join_receipt.schema.json`

**Failure condition:**
- `mapping_method = CROSSWALKED_INDEX`
- `decision = ACCEPT`
- but:
  - no `bridge_ref`
  - no declared `crosswalk_version`

**What it proves:**
A join that depends on crosswalked identity **must declare its bridge basis**.  
Otherwise, the result must fail closed.

---

## Rules for invalid fixtures

A fixture belongs here only if:

| Rule | Meaning |
|---|---|
| Fail-expected | It must fail validation |
| Named failure | The failure condition is explicit |
| Schema-paired | It maps to one contract schema |
| Deterministic | The failure is not ambiguous |
| Minimal | It isolates one failure condition |
| Doctrine-safe | It does not redefine policy or contracts |

---

## Hydrology failure patterns (current thin slice)

These are the **core failure modes this directory should enforce**:

### 1. Missing bridge basis

- legacy identity used
- but no crosswalk declared

→ **Fail**

---

### 2. Crosswalk without accountability

- crosswalk-based mapping used
- but no bridge reference or version

→ **Fail**

---

### 3. Declared success without closure

- `decision = ACCEPT`
- but missing:
  - mapped reach
  - mapped HUC12

→ **Fail**

---

### 4. Contradictory status

- `status = ACTIVE`
- but reason codes imply missing identity

→ **Fail**

---

## Quickstart

```bash
# Inspect invalid fixtures
find schemas/tests/fixtures/contracts/v1/invalid -type f | sort

# Open hydro invalid fixtures
sed -n '1,220p' schemas/tests/fixtures/contracts/v1/invalid/hydro_identity_bridge.legacy-only-without-basis.v1.json
sed -n '1,260p' schemas/tests/fixtures/contracts/v1/invalid/hydro_join_receipt.crosswalk-missing-bridge.v1.json

# Compare against schemas
sed -n '1,260p' schemas/contracts/v1/hydro_identity_bridge.schema.json
sed -n '1,320p' schemas/contracts/v1/hydro_join_receipt.schema.json
