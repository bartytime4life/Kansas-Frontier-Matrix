<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8d6f6d0a-5f6e-4f19-9f83-20b3a7c5c2a1
title: Contract Schemas
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-27
updated: 2026-02-27
policy_label: public
related:
  - apps/api/src/contracts/
  - apps/api/src/contracts/schemas/
tags: [kfm, contracts, schemas, api]
notes:
  - Canonical home for machine-validated contract artifacts used by the governed API boundary and governance gates.
[/KFM_META_BLOCK_V2] -->

# Contract Schemas

Single source of truth for **machine-validated contract artifacts** at the API boundary.

![status](https://img.shields.io/badge/status-draft-lightgrey)
![scope](https://img.shields.io/badge/scope-api%20contracts-blue)
![governance](https://img.shields.io/badge/governance-fail--closed-important)

> **WARNING**
> These schemas are part of the KFM “trust membrane.” Changing them can be a breaking change for:
> - policy gates
> - promotion workflows
> - evidence resolution
> - UI trust surfaces and Focus Mode evaluation

---

## Quick links

- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [What belongs here](#what-belongs-here)
- [Schema inventory](#schema-inventory)
- [Naming and versioning](#naming-and-versioning)
- [Validation and tests](#validation-and-tests)
- [Change workflow](#change-workflow)
- [Appendix: Recommended directory layout](#appendix-recommended-directory-layout)

---

## Purpose

This directory contains **contract schemas** used to validate artifacts and API payloads that cross governed boundaries.

In KFM, **contracts are first-class**: implementation follows the contract, and contract changes trigger strict versioning/compatibility checks (including API versioning when relevant).  

---

## Where this fits

KFM layering model:

- **Domain**: concepts like Dataset, EvidenceBundle, StoryNode
- **Use cases**: workflows like “resolve evidence,” “publish story,” “answer focus query”
- **Interfaces**: **contracts** (schemas, DTOs, policy adapters)
- **Infrastructure**: databases, object storage, indexes, CI

This folder is in the **Interfaces** layer: it defines *what is allowed to cross the boundary*.

---

## What belongs here

### Acceptable inputs

✅ Keep **only** contract artifacts and small supporting fixtures:

- JSON Schema files (recommended suffix: `*.schema.json`)
- Schema registry exports (example: `index.ts`) **if** the API code imports schemas as modules
- Minimal fixtures for tests (example: `__fixtures__/good/*.json`, `__fixtures__/bad/*.json`)
- Documentation that explains schema intent and versioning (this `README.md`)

### Exclusions

❌ Do **not** put these here:

- runtime code (routes, services, controllers)
- production data or catalog outputs (STAC/DCAT/PROV instances)
- large example payload dumps
- secrets or tokens
- “temporary” one-off schemas that aren’t versioned

---

## Schema inventory

> **NOTE**
> Treat this as a living registry. Update it in the same PR as any schema changes.

| Contract | Recommended file name | Used by | Why it exists |
|---|---|---|---|
| Run Receipt v1 | `run_receipt_v1.schema.json` | Pipelines + CI + promotion gates | Typed per-run receipt (inputs/outputs/checks/timestamps) used to block promotion fail-closed. |
| Run Manifest v1 | `run_manifest_v1.schema.json` | Promotion workflow | Promotion-focused rollup (digests/rights/attestation pointers). |
| Watchers Registry v1 | `watcher_v1.schema.json` | Automation allow-list | Signed allow-list to constrain automation safely. |
| Spec v1 | `spec_v1.schema.json` | Hashing + controlled vocab | Deterministic `spec_hash` inputs (canonicalization + vocab validation). |
| Evidence Bundle v1 | `evidence_bundle_v1.schema.json` | Evidence resolver endpoint | Ensures citations resolve to structured, policy-filterable evidence bundles. |
| Story Node v3 | `story_node_v3.schema.json` | Story publish gate + UI | Machine-ingestible narrative format with resolvable citations and review states. |
| Focus Response v1 | `focus_response_v1.schema.json` | Focus Mode + eval harness | Output contract: answer text + resolvable citations + audit reference. |

If this API also validates **catalog profiles** (STAC/DCAT/PROV) at runtime, prefer keeping those schemas in a *single canonical location* (repo-level `schemas/` or a shared package) and importing them here rather than duplicating them.

---

## Naming and versioning

### Naming rules

**Rule 1: Version in the filename for breaking changes**

- `*_v1.schema.json`
- `*_v2.schema.json`

**Rule 2: Stable identifiers**

If you use `$id` in JSON Schema, treat it as a stable identifier for the schema version. Avoid reusing a `$id` for a breaking change.

### Compatibility rules

- **Non-breaking change**: additive/optional fields, relaxed constraints that don’t break existing valid payloads.
- **Breaking change**: removing fields, changing required/optional status, changing types/meaning, renaming keys.

When a change is breaking, ship a **new major schema** and keep the old one intact until all producers/consumers are migrated.

### API versioning linkage

If these schemas drive API request/response validation, then a breaking schema change usually implies:
- a versioned endpoint change, or
- a negotiation/compat strategy,
because the OpenAPI/GraphQL spec is the published contract.

---

## Validation and tests

At minimum, contract schemas should be validated by automated checks that fail closed:

- **Schema validation tests**: payload fixtures must validate against the intended schema version.
- **Policy tests**: deny-by-default rules should reject artifacts that fail schema requirements or violate obligations.
- **Contract tests**: ensure API responses remain compatible with the OpenAPI/GraphQL contract and schema expectations.
- **Integration tests**: evidence resolver resolves references into bundles without leaking restricted data.

> **Guardrail**
> Anything that produces user-facing claims (Story/Focus) should be blocked if citations can’t be verified/resolved.

---

## Change workflow

Use this checklist for any PR that adds or changes a schema:

- [ ] Add or update schema file (new versioned file for breaking change)
- [ ] Add fixtures: at least one **known-good** and one **known-bad** payload
- [ ] Add/adjust schema validation tests to cover fixtures
- [ ] If the schema is used in runtime endpoints, update endpoint validation + contract tests
- [ ] If the schema is used in CI gates (promotion/policy), update policy fixtures and ensure deny-by-default still holds
- [ ] Update the [Schema inventory](#schema-inventory) table
- [ ] Document migration notes when introducing a new major version

---

## Appendix: Recommended directory layout

```text
apps/api/src/contracts/schemas/
├── README.md
├── index.ts                 # optional: central export/registry
├── run_receipt_v1.schema.json
├── run_manifest_v1.schema.json
├── watcher_v1.schema.json
├── spec_v1.schema.json
├── evidence_bundle_v1.schema.json
├── story_node_v3.schema.json
├── focus_response_v1.schema.json
└── __fixtures__/
    ├── good/
    │   ├── run_receipt.v1.json
    │   └── focus_response.v1.json
    └── bad/
        ├── run_receipt.v1.missing_checks.json
        └── focus_response.v1.missing_citations.json
```

---

<a id="back-to-top"></a>
**Back to top:** [Quick links](#quick-links)
