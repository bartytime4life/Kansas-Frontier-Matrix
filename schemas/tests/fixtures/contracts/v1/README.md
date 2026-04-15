<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Contract Fixtures v1
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS-VERIFICATION
updated: 2026-04-14
policy_label: public
related: [
  ../README.md,
  ./valid/README.md,
  ./invalid/README.md,
  ../../README.md,
  ../../../README.md,
  ../../../../README.md,
  ../../../../contracts/README.md,
  ../../../../contracts/v1/README.md,
  ../../../../../contracts/README.md,
  ../../../../../contracts/hydro_mapping/README.md,
  ../../../../../schemas/contracts/v1/hydro_identity_bridge.schema.json,
  ../../../../../schemas/contracts/v1/hydro_join_receipt.schema.json,
  ../../../../../tests/README.md,
  ../../../../../tests/contracts/README.md,
  ../../../../../policy/README.md,
  ../../../../../docs/standards/README.md,
  ../../../../../.github/workflows/README.md
]
tags: [kfm, schemas, tests, fixtures, contracts, v1, hydrology, identity-bridge, join-receipt]
notes: [
  Version-root README for local contract fixtures under schemas/tests/fixtures/contracts/v1.
  Updated to reflect the current thin-slice hydro fixture pairings without overstating canonical fixture-home authority.
  doc_id and created remain NEEDS-VERIFICATION against checked-out branch evidence.
]
[/KFM_META_BLOCK_V2] -->

# Contract Fixtures v1

Versioned fixture boundary for local contract examples under `schemas/tests/fixtures/contracts/v1/`.

This subtree exists to keep **versioned fixture families reviewable** without silently turning the schema-side fixture lane into a second authority surface.

> [!NOTE]
> This README is intentionally conservative.  
> It acknowledges the local `v1/` fixture subtree, but it does **not** claim that this path has become the repo’s sole canonical fixture home.

> **Status:** experimental  
> **Doc status:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** `schemas/tests/fixtures/contracts/v1/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange)
> ![doc](https://img.shields.io/badge/doc-draft-lightgrey)
> ![owners](https://img.shields.io/badge/owners-%40bartytime4life-blue)
> ![posture](https://img.shields.io/badge/posture-boundary%20guide-blueviolet)
> ![authority](https://img.shields.io/badge/authority-still%20reviewable-red)
> ![focus](https://img.shields.io/badge/focus-hydro%20fixtures%20landed-1f6feb)

**Repo fit:** path `schemas/tests/fixtures/contracts/v1/README.md` · parent [`../README.md`](../README.md) · leaves [`./valid/README.md`](./valid/README.md), [`./invalid/README.md`](./invalid/README.md) · schema-side chain [`../../README.md`](../../README.md), [`../../../README.md`](../../../README.md), [`../../../../README.md`](../../../../README.md) · schema-side contracts [`../../../../contracts/README.md`](../../../../contracts/README.md), [`../../../../contracts/v1/README.md`](../../../../contracts/v1/README.md) · stronger repo surfaces [`../../../../../contracts/README.md`](../../../../../contracts/README.md), [`../../../../../contracts/hydro_mapping/README.md`](../../../../../contracts/hydro_mapping/README.md), [`../../../../../tests/README.md`](../../../../../tests/README.md), [`../../../../../tests/contracts/README.md`](../../../../../tests/contracts/README.md), [`../../../../../policy/README.md`](../../../../../policy/README.md), [`../../../../../.github/workflows/README.md`](../../../../../.github/workflows/README.md)

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current fixture snapshot](#current-fixture-snapshot) · [Directory tree](#directory-tree) · [Hydrology thin slice now visible](#hydrology-thin-slice-now-visible) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Task list](#task-list--definition-of-done) · [FAQ](#faq)

> [!IMPORTANT]
> The current recommended thin slice in this subtree is now specific enough to be useful:
>
> - `hydro_identity_bridge` fixtures prove **explicit current↔legacy hydro identity translation**
> - `hydro_join_receipt` fixtures prove **deterministic join process memory**
>
> That still does **not** settle broader fixture-home authority for the repo.

> [!WARNING]
> Keep the core doctrine visible:
>
> - contracts define machine-shape expectations
> - fixtures demonstrate shape and fail-closed behavior
> - receipts remain process memory
> - policy and merge gates are owned elsewhere unless explicitly wired and proven

---

## Scope

`schemas/tests/fixtures/contracts/v1/` is the **version root** for local contract fixtures.

Its job is to:

- make `v1/` fixture inventory visible
- keep positive and negative examples organized
- help reviewers see which examples are thin-slice contract proofs
- route broader authority questions back to stronger neighboring lanes

Its job is **not** to:

- replace root `contracts/`
- replace root `tests/` or `tests/contracts/`
- become an accidental shadow schema-home
- imply CI enforcement or merge-gate behavior without branch-backed proof

### Truth labels used here

| Label | Meaning |
| --- | --- |
| **CONFIRMED** | Directly supported by checked-in repo text or landed local fixture/schema work in this thin slice |
| **INFERRED** | Conservative interpretation of visible structure and adjacent doctrine |
| **PROPOSED** | Repo-fitting next move that is not yet proven as landed |
| **NEEDS VERIFICATION** | Still not strong enough to present as settled repo law |

[Back to top](#contract-fixtures-v1)

---

## Repo fit

**Path:** `schemas/tests/fixtures/contracts/v1/README.md`  
**Role:** version-root README for local contract fixtures and fixture-family orientation

| Dimension | Current reading |
| --- | --- |
| Immediate parent | [`../README.md`](../README.md) |
| Local leaves | [`./valid/README.md`](./valid/README.md) · [`./invalid/README.md`](./invalid/README.md) |
| Schema-side contract neighbors | [`../../../../contracts/README.md`](../../../../contracts/README.md) · [`../../../../contracts/v1/README.md`](../../../../contracts/v1/README.md) |
| Stronger machine-contract guide | [`../../../../../contracts/README.md`](../../../../../contracts/README.md) |
| Hydrology contract lane | [`../../../../../contracts/hydro_mapping/README.md`](../../../../../contracts/hydro_mapping/README.md) |
| Stronger verification lanes | [`../../../../../tests/README.md`](../../../../../tests/README.md) · [`../../../../../tests/contracts/README.md`](../../../../../tests/contracts/README.md) |
| Workflow / control-plane lane | [`../../../../../.github/workflows/README.md`](../../../../../.github/workflows/README.md) |
| Current authority posture | **NEEDS VERIFICATION** — real local fixture lane, but broader canonical-home law still unresolved |
| Current maturity reading | **Useful thin slice exists**; broad enforcement depth still must be proven separately |

### Working interpretation

This `v1/` lane is now strong enough to hold a narrow contract-fixture family for hydrology without pretending that every fixture family is equally mature.

The healthy reading is:

- local examples may exist here
- they should remain crisp and bounded
- their contract family should be obvious
- stronger neighboring lanes still own broader repo law

[Back to top](#contract-fixtures-v1)

---

## Accepted inputs

This version root should stay narrow, explicit, and reviewable.

| Accepted here | Why it belongs here |
| --- | --- |
| This README | Defines the version-root boundary |
| Version-scoped valid fixtures | Positive examples for a landed contract family |
| Version-scoped invalid fixtures | Deliberate fail-closed cases for a landed contract family |
| Thin-slice fixture family notes | Helps reviewers understand how fixture pairs relate to schemas |
| Cross-links to schema files | Keeps fixture/schema pairing visible |
| Minimal family-specific README notes | Appropriate when they prevent drift or ambiguity |

### Minimum bar for anything added here

- it is clearly version-scoped
- it belongs to a declared contract family
- it has an obvious relationship to a real schema
- it helps validation or review
- it does not silently redefine policy or authority
- it is public-safe and rights-safe

---

## Exclusions

| Do **not** place here by default | Put it here instead | Why |
| --- | --- | --- |
| Canonical policy vocabularies or reason-code law | `policy/` | policy should stay singular |
| Workflow YAML or required-check claims | `.github/workflows/` | execution wiring lives in workflow/control lanes |
| Release proofs, attestations, manifests | their owning release / proof lanes | this is not a release artifact home |
| Runtime envelopes or outward answer artifacts | runtime / evidence owning lanes | fixture root is not runtime surface |
| Large duplicated fixture inventories with unclear authority | stronger root test lanes or resolved canonical fixture home | avoids second-authority drift |
| Schema definitions themselves | `schemas/contracts/v1/` or canonical schema home | keeps schema and fixture roles distinct |

> [!CAUTION]
> The main failure mode here is not missing examples.  
> The main failure mode is a helpful fixture tree quietly becoming a shadow authority surface.

[Back to top](#contract-fixtures-v1)

---

## Current fixture snapshot

The current thin slice should be read as **family-paired**.

### Landed or expected family pairings

| Contract family | Schema pair | Fixture expectation |
| --- | --- | --- |
| `hydro_identity_bridge` | `schemas/contracts/v1/hydro_identity_bridge.schema.json` | one valid bridge + one invalid missing-basis bridge |
| `hydro_join_receipt` | `schemas/contracts/v1/hydro_join_receipt.schema.json` | one valid accepted snap receipt + one invalid crosswalk-without-bridge receipt |

### Reading rule

- `hydro_identity_bridge` fixtures prove explicit current↔legacy hydro identity translation
- `hydro_join_receipt` fixtures prove deterministic join process memory
- crosswalked receipts should point to a bridge object instead of silently treating legacy identifiers as current truth

### What this does **not** mean

It does **not** mean:

- every contract family now has equivalent fixture maturity
- root verification lanes are obsolete
- workflow enforcement is already landed
- broader schema-home and fixture-home authority questions are resolved

[Back to top](#contract-fixtures-v1)

---

## Directory tree

### Recommended current shape

```text
schemas/tests/fixtures/contracts/v1/
├── README.md
├── invalid/
│   ├── README.md
│   ├── hydro_identity_bridge.legacy-only-without-basis.v1.json
│   └── hydro_join_receipt.crosswalk-missing-bridge.v1.json
└── valid/
    ├── README.md
    ├── hydro_identity_bridge.minimal.v1.json
    └── hydro_join_receipt.accept.snap.v1.json
