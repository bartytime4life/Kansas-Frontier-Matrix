# schemas

Machine-checkable shape root for KFM object families; pairs with `contracts/` and stays separate from policy, data, fixtures, validator code, and release authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-readme
title: schemas/README.md — Schema Root README
type: root-readme; schema-root; governance-index; json-schema-boundary
version: v0.2
status: draft; root-schema-index; canonical-root-name; mixed-maturity-child-lanes; NEEDS VERIFICATION
owners: OWNER_TBD — Schema steward · Contract steward · Validation steward · Policy steward · Domain stewards · Docs steward
created: NEEDS VERIFICATION — short root stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; json-schema; schema-shape; no-parallel-authority
tags: [kfm, schemas, json-schema, contracts, tests, validators, fixtures, policy, governance, no-parallel-authority]
related:
  - ./contracts/v1/README.md
  - ./policy/README.md
  - ./tests/README.md
  - ../contracts/README.md
  - ../policy/
  - ../fixtures/
  - ../tests/
  - ../tools/validators/
  - ../data/
  - ../release/
notes:
  - "Expanded from a short root README that defined schemas as machine-checkable shape paired one-to-one with contracts."
  - "The previous README marked authority level canonical and status PROPOSED; this update preserves that distinction by treating the root responsibility as confirmed while child-lane maturity remains mixed and NEEDS VERIFICATION."
  - "Current-session evidence confirms direct child lanes for contracts/v1, policy, and tests. Additional child lanes may exist but are not asserted here without inspection."
  - "This README does not prove schema completeness, validator wiring, fixture coverage, CI behavior, policy behavior, release readiness, or public client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: schemas" src="https://img.shields.io/badge/root-schemas%2F-blue">
  <img alt="Authority: machine shape" src="https://img.shields.io/badge/authority-machine__shape-purple">
  <img alt="Standard: JSON Schema 2020-12" src="https://img.shields.io/badge/json--schema-2020--12-informational">
  <img alt="Boundary: not policy or data" src="https://img.shields.io/badge/boundary-not__policy__or__data-critical">
</p>

**Status:** draft / root schema index / mixed child maturity  
**Path:** `schemas/README.md`  
**Authority posture:** `schemas/` owns machine-checkable shape; `contracts/` owns semantic meaning; policy, fixtures, validators, data, proof, and release remain separate.  
**Truth posture:** CONFIRMED root responsibility from the previous README; CONFIRMED inspected child indexes for `contracts/v1/`, `policy/`, and `tests/`; NEEDS VERIFICATION for full schema inventory, executable test ownership, validator wiring, CI coverage, and release integration.

## Quick jumps

[Purpose](#purpose) · [Authority boundary](#authority-boundary) · [Repo fit](#repo-fit) · [Current child lanes](#current-child-lanes) · [Authoring rules](#authoring-rules) · [Domain alias schemas](#domain-alias-schemas) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Validation](#validation) · [Review burden](#review-burden) · [Open questions](#open-questions)

---

## Purpose

`schemas/` is the KFM machine-checkable shape root.

Use this root for JSON Schema and schema-family documentation that defines whether a payload has the expected structure. A schema may constrain shape, required fields, references, enums, and basic value form. It does not make a claim true, admit a source, approve policy, clear rights, authorize release, or publish a public map/API surface.

The root rule is simple:

```text
contracts/  -> semantic meaning
schemas/    -> machine-checkable shape
policy/     -> allow / deny / restrict / abstain rules and posture
data/       -> lifecycle records and emitted data products
release/    -> publication, correction, rollback decisions
```

## Authority boundary

| Responsibility | Correct root | Boundary rule |
|---|---|---|
| Machine-checkable shape | `schemas/` | This root. JSON Schema and schema-family README files. |
| Semantic meaning | `contracts/` | Object meaning, claim limits, review semantics, and interpretation rules. |
| Policy and admissibility | `policy/` | Allow, deny, restrict, abstain, sensitivity, rights, and release gates. |
| Examples and fixtures | `fixtures/` | Valid, invalid, negative, and golden examples unless an accepted migration says otherwise. |
| Executable tests | `tests/` or accepted project test root | Test code and CI-facing checks. `schemas/tests/` remains compatibility-indexed until ownership is verified. |
| Validator implementation | `tools/validators/` | Validator code and helper tooling, not schema authority. |
| Lifecycle records | `data/` | RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED. |
| Receipts, proofs, catalogs | accepted `data/` proof/receipt/catalog roots | Evidence and process memory are separate from schemas. |
| Release, correction, rollback | `release/` | Publication state and rollback authority. |

> [!IMPORTANT]
> Schema validation is necessary but not sufficient. A schema-valid object may still be unsupported, stale, rights-uncleared, policy-denied, unreleased, sensitive, or unsafe for public display.

## Repo fit

```text
schemas/
├── README.md                         # this file; schema root index
├── contracts/
│   └── v1/
│       └── README.md                 # inspected v1 contract-schema index
├── policy/
│   └── README.md                     # inspected policy schema compatibility guardrail
└── tests/
    └── README.md                     # inspected schema-test compatibility index

contracts/                            # semantic meaning; not JSON Schema
policy/                               # policy rules and posture; not schema shape
fixtures/                             # examples; not schema authority
tests/                                # executable test code; ownership NEEDS VERIFICATION
tools/validators/                    # validator implementation; not schema authority
data/                                 # lifecycle, proof, receipt, catalog, and emitted records
release/                              # release, correction, rollback authority
```

## Current child lanes

| Child lane | Current posture | Notes |
|---|---|---|
| `contracts/v1/` | CONFIRMED present / mixed maturity | v1 machine-checkable schema index for contract-backed object families. It includes schema families, compatibility paths, scaffolds, and guardrails. |
| `policy/` | CONFIRMED present / compatibility guardrail | Root-level policy schema compatibility path; inspected README points active policy schema work toward `schemas/contracts/v1/policy/`. |
| `tests/` | CONFIRMED present / compatibility index | Parent index for `valid/` and `invalid/` schema-test placement; executable ownership remains NEEDS VERIFICATION. |

This inventory reflects current-session inspection only. Do not treat it as a full repository tree audit.

## Authoring rules

| Rule | Requirement |
|---|---|
| Use JSON Schema 2020-12 | Schema files should use the project’s JSON Schema 2020-12 posture unless an accepted migration says otherwise. |
| Pair with contracts | Every consequential schema should point to a semantic contract or clearly mark the missing contract as NEEDS VERIFICATION. |
| Keep shape separate | Do not use schemas to store policy rules, lifecycle data, evidence, source records, release decisions, or implementation code. |
| Preserve source roles | Shape must not collapse observations, models, regulatory context, source descriptors, receipts, proofs, release records, or generated summaries. |
| Avoid parallel authority | Do not create duplicate schema homes, flat/domain mirrors, or compatibility paths without ADR/migration notes. |
| Mark maturity honestly | Use PROPOSED, NEEDS VERIFICATION, CONFLICTED, or DENY where field maturity, path authority, or publication readiness is not proven. |

## Domain alias schemas

When a domain alias schema wraps a shared runtime contract via `allOf` + `$ref`, enforce strictness with `unevaluatedProperties: false`, not wrapper-level `additionalProperties: false`.

This preserves alias strictness without false rejections because inherited properties remain recognized under JSON Schema 2020-12.

## What belongs here

- This README.
- JSON Schema files, normally under accepted versioned lanes such as `schemas/contracts/v1/`.
- Schema-family README files and compatibility guardrails.
- Schema migration notes, path-conflict notes, and drift registers when schema homes are unsettled.
- README-only schema-test placement guardrails under `schemas/tests/` while ownership is being verified.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, correction references, rollback references, and tests.

## What does not belong here

| Do not put this in `schemas/` | Correct home |
|---|---|
| Semantic contract prose | `contracts/` |
| Policy rules, bundles, access decisions, sensitivity decisions, or redaction decisions | `policy/` |
| Fixture payloads unless an accepted migration assigns them here | `fixtures/` |
| Validator implementation or helper code | `tools/validators/` or accepted tool/test root |
| Runtime code, package code, API code, UI code, or MapLibre behavior | appropriate package, app, UI, or service root |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, proof packs, receipts, catalog records, or release manifests | accepted `data/`, proof, receipt, catalog, source-registry, or release roots |
| Public map payloads, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output | governed publication/UI/artifact roots after release checks |
| Claims that a payload is true, cited, rights-cleared, policy-approved, released, public-safe, or implementation-proven | Evidence, policy, review, release, validator, and runtime evidence lanes |

## Validation

```bash
find schemas -maxdepth 4 -type f | sort
find schemas -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
find schemas/contracts/v1 -maxdepth 5 -type f 2>/dev/null | sort
find schemas/tests -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the accepted schema-test command and CI owner are confirmed.

## Review burden

Schema changes are trust-bearing when they affect evidence references, source descriptors, runtime envelopes, policy-facing payloads, UI projections, domain object families, release objects, or public map/API surfaces.

Before promoting a schema change, verify:

- [ ] paired semantic contract exists or the absence is explicitly marked NEEDS VERIFICATION;
- [ ] fixture coverage exists for valid, invalid, edge, and golden cases where material;
- [ ] validator and test ownership are confirmed;
- [ ] policy, rights, sensitivity, release, correction, and rollback boundaries remain separate;
- [ ] no public client path bypasses governed interfaces or released artifacts;
- [ ] path conflicts or compatibility mirrors have ADR/migration notes.

## Open questions

| Question | Status |
|---|---|
| Which CI workflow currently validates `schemas/contracts/v1/` and `schemas/tests/`? | NEEDS VERIFICATION |
| Should executable schema tests live under `schemas/tests/`, `tests/schemas/`, or both with a documented split? | NEEDS VERIFICATION |
| Which schema registry, if any, is authoritative for current `$id`, version, and promotion state? | NEEDS VERIFICATION |
| Which root-level schema compatibility lanes should be retired, migrated, or formalized by ADR? | NEEDS VERIFICATION |
| Should this root README link to a generated schema inventory once validator output exists? | NEEDS VERIFICATION |
