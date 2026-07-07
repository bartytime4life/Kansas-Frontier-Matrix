<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-common-readme
title: tools/validators/_common README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-schema-steward-plus-validator-steward
created: 2026-05-09
updated: 2026-07-07
policy_label: repository-facing; shared-validator-helpers; no-policy-authority
owning_root: tools/
responsibility: shared implementation helpers for validator entrypoints, local schema registry construction, deterministic validation wrappers, and common result formatting
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0001-schema-home.md
  - ../../../schemas/contracts/v1/
  - ../../../fixtures/contracts/v1/
  - ../../../tests/schemas/
  - ../../../contracts/
  - ../../../policy/
notes:
  - "This README updates the existing shared-validator helper README while preserving current-session evidence that this lane supports shared JSON Schema validation helpers, local $id registry construction, fixture paths, deterministic status output, and run_all.py wiring."
  - "Common helpers may normalize validator plumbing. They must not encode domain-specific schema assumptions, policy meaning, network I/O, ingestion workflow behavior, publishing workflow behavior, or release decisions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/_common

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-shared--validator--helpers-informational)
![authority](https://img.shields.io/badge/authority-plumbing--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/_common/` is the shared implementation lane for validator plumbing used by top-level and domain validator entrypoints. It may host reusable schema-loading, registry, fixture, result-formatting, and runner helpers, but it must not become a hidden schema, contract, policy, domain, ingestion, or publication authority.

---

## Purpose

`tools/validators/_common/` holds shared JSON Schema validation helpers used by validator entrypoints.

The existing README already scoped this lane to:

- shared JSON Schema validation helpers;
- schema paths;
- fixture file paths;
- repo-root path handling for local `$id` registry construction;
- validator instances;
- deterministic pass/fail exit codes;
- per-file validation status lines;
- shared runner behavior for `run_all.py`.

This README preserves that scope and makes the authority boundary explicit.

The durable KFM question for this lane is:

> Can common validator plumbing be reused without hiding the contract, schema, policy, fixture, or domain authority that the validators are supposed to enforce?

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/_common/README.md` | **CONFIRMED** | This README updates the prior shared-helper README. |
| Shared JSON Schema helper role | **CONFIRMED from existing README** | Prior text says this lane is used by top-level and domain validator entrypoints. |
| `run_all.py` wiring | **CONFIRMED from existing README / NEEDS CODE VERIFICATION** | Prior text says `run_all.py` currently executes five top-level validators wired to the shared runner. Code shape was not verified in this edit. |
| Validator executable inventory | **NEEDS VERIFICATION** | No complete executable list is claimed here. |
| Schema-home convention | **CONFIRMED by parent/ADR reference; implementation details NEED VERIFICATION** | ADR-0001 and parent docs point to `schemas/contracts/v1/` as schema home. |
| Policy authority | **DENY here** | Common helpers do not define policy meaning. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Shared validator helper implementation | `tools/validators/_common/` |
| Validator entrypoints | `tools/validators/` or accepted validator sublanes |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/contracts/v1/` or accepted schema home |
| Policy rules and admissibility | `policy/` |
| Fixtures | `fixtures/` or `tests/fixtures/` according to accepted convention |
| Tests | `tests/` |
| Receipts, proofs, release records | dedicated `data/` and `release/` roots |

Safe interpretation:

- **CONFIRMED:** this README exists and replaces the previous short README.
- **CONFIRMED:** the previous README described this lane as shared validator helper plumbing.
- **PROPOSED:** additional common helpers may live here when they are generic, deterministic, and tested by validator suites.
- **NEEDS VERIFICATION:** exact module names, public helper APIs, current validators using this lane, and current CI behavior.
- **DENY:** using this folder to encode domain-specific schema assumptions, policy logic, network I/O, ingestion workflows, publishing workflows, or release decisions.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/_common/` include:

- JSON Schema registry construction helpers;
- local `$id` resolver helpers;
- shared fixture discovery helpers;
- path normalization helpers;
- deterministic validation result models;
- shared pass/fail/abstain/error formatting;
- common CLI argument parsing utilities used by validator entrypoints;
- shared runner utilities used by `run_all.py`;
- small helper functions that are truly cross-validator plumbing.

A helper belongs here only when it is reusable across validators and does not embed domain meaning or policy decisions.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/_common/` | Correct home |
|---|---|
| Domain-specific validator logic | `tools/validators/domains/<domain>/` or accepted validator lane |
| Top-level validator entrypoints | `tools/validators/` |
| Semantic contracts | `contracts/` |
| JSON Schemas | `schemas/contracts/v1/` or accepted schema home |
| Policy rules | `policy/` |
| Fixture files | `fixtures/` or `tests/fixtures/` |
| Tests | `tests/` |
| Ingestion or publication workflow code | `pipelines/`, `connectors/`, `tools/release/`, or accepted workflow home |
| Receipts, proofs, catalog, or release records | dedicated `data/` and `release/` roots |

[Back to top](#top)

---

## Inputs

Shared helpers may accept:

- schema paths;
- fixture file paths;
- repo root path;
- validator configuration objects;
- local `$id` registry construction inputs;
- JSON instances under validation;
- expected result definitions for tests.

They should not accept secrets, live network endpoints, source-system credentials, or public-release authority as inputs.

[Back to top](#top)

---

## Outputs

Shared helpers may produce:

- validator instances;
- local schema registries;
- deterministic status records;
- pass/fail/abstain/error result objects;
- per-file validation status lines;
- runner summaries.

The previous README stated that `run_all.py` executes five top-level validators wired to the shared runner. That statement is preserved as prior repo documentation, but the exact current code behavior still needs verification before it is used as implementation proof.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `VALIDATION_PASS` | Instance satisfied the configured schema or validator. |
| `VALIDATION_FAIL` | Instance failed the configured schema or validator. |
| `SCHEMA_NOT_FOUND` | Required schema path or `$id` could not be resolved. |
| `FIXTURE_NOT_FOUND` | Required fixture path could not be resolved. |
| `REGISTRY_BUILD_FAIL` | Local schema registry construction failed. |
| `ABSTAIN` | Helper cannot safely decide with available context. |
| `ERROR` | Helper could not safely complete. |

[Back to top](#top)

---

## Validation

Existing README guidance preserved:

```bash
python tools/validators/validate_evidence_bundle.py --fixtures
make schemas
make test
```

Recommended future test surface:

```text
tests/validators/_common/
├── README.md
├── test_schema_registry.py
├── test_result_format.py
└── fixtures/
```

> [!NOTE]
> The future test surface above is proposed. It does not prove that `tests/validators/_common/` exists.

[Back to top](#top)

---

## Review burden

**Moderate.** Changes here can affect every validator that imports shared helpers. Review should include:

- schema steward review when registry or `$id` behavior changes;
- validator steward review when result format or exit behavior changes;
- domain steward review only when a supposedly common helper risks embedding domain meaning;
- tests for positive, negative, missing-schema, missing-fixture, and error cases.

[Back to top](#top)

---

## Related folders

- `tools/validators/`
- `schemas/contracts/v1/`
- `fixtures/contracts/v1/`
- `tests/schemas/`
- `contracts/`
- `policy/`

[Back to top](#top)

---

## ADRs

- ADR-0001 — schema home convention for `schemas/contracts/v1/`.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Prior reviewed date preserved | 2026-05-09 |
| Review state | Draft README update preserving existing shared-helper claims while adding KFM metadata and authority boundaries. |
| Next smallest safe change | Verify actual helper modules and `run_all.py` wiring, then add tests for registry construction and deterministic result formatting. |
