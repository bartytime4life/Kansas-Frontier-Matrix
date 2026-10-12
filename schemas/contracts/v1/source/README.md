<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://schemas/contracts/v1/source/readme
title: schemas/contracts/v1/source/ — Source Schema Family Index
type: README; schema-family-index; mixed-maturity-inventory; compatibility-boundary
version: v0.3
status: repository-grounded draft; mixed maturity; SourceDescriptor validation implemented; naming drift unresolved
owners: NEEDS VERIFICATION — source, schema, contract, registry, validation, policy, evidence, and release stewards
updated: 2026-08-29
policy_label: internal-governance; schema-shape-only; no-admission-or-release-authority
current_path: schemas/contracts/v1/source/README.md
truth_posture: >
  CONFIRMED bounded file inventory, rich SourceDescriptor schema, compatibility
  alias, validator entrypoints, fixtures, tests, and workflow / PROPOSED all
  machine schemas and companion vocabulary / UNKNOWN complete family inventory,
  runtime consumers, and promotion readiness / HOLD singular-plural and
  hyphen-underscore disposition
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  prior_blob: 691e5f76ba800404fff26fabd120b7f42791e79a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  method: complete target read plus exact schema, pointer, contract, fixture, validator, test, workflow, and registry inspection
related:
  - ../README.md
  - ../sources/source_descriptor.schema.json
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../data/registry/sources/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../../../tests/validators/test_validate_source_descriptor_entrypoints.py
  - ../../../../tools/validators/validate_source_descriptor.py
  - ../../../../tools/validators/sources/validate_source_descriptor.py
  - ../../../../.github/workflows/source-descriptor-validate.yml
notes:
  - "This same-path correction changes documentation only; no schema status, identifier, validation behavior, admission state, or release state changes."
  - "The inventory is bounded to prior listed files and directly declared successors; it is not a generated or recursive manifest."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/contracts/v1/source/` — Source Schema Family Index

This directory contains machine-checkable shapes and compatibility records for source-governance objects. It is a mixed-maturity schema family, not a source registry, policy engine, receipt store, or release authority.

> [!IMPORTANT]
> A schema pass proves shape for the checked object. It does not prove source truth, rights clearance, sensitivity clearance, source admission, connector activation, lifecycle promotion, review, release, deployment, or publication.

**Quick navigation:** [Authority](#authority-boundary) · [Status](#current-status) · [Inventory](#bounded-current-inventory) · [SourceDescriptor](#sourcedescriptor-validation-profile) · [Drift](#compatibility-and-drift) · [Validation](#focused-validation) · [Maintenance](#maintenance-and-promotion) · [Open items](#open-verification-register)

## Authority boundary

Accepted [Directory Rules](../../../../docs/doctrine/directory-rules.md) assign responsibilities as follows:

| Responsibility | Authority home |
|---|---|
| Semantic meaning and invariants | [`contracts/source/`](../../../../contracts/source/README.md) |
| Machine-checkable shape | `schemas/contracts/v1/source/` or an accepted successor profile |
| Source identities and descriptor records | [`data/registry/sources/`](../../../../data/registry/sources/README.md) |
| Admissibility decisions | `policy/source/`, `policy/rights/`, and `policy/sensitivity/` |
| Deterministic examples and tests | `fixtures/` and `tests/` |
| Validator implementation | `tools/validators/` |
| Receipts, proofs, lifecycle data, and release records | Their distinct `data/` and `release/` lanes |
| Public consumption | Governed interfaces or released public-safe artifacts only |

`DIR-AUTHROOT-001` makes `schemas/contracts/v1/<family>/` the default machine-schema profile unless an accepted ADR establishes another. This README indexes current files; it does not select a successor path, accept a schema, or resolve compatibility drift.

## Current status

| Question | Repository-grounded result |
|---|---|
| Is the family uniformly mature? | No. Substantive schemas, permissive scaffolds, deprecated pointers, and proposal records coexist. |
| Is SourceDescriptor shape implemented? | Yes, as a rich `PROPOSED` schema at `source_descriptor.schema.json`. |
| Is SourceDescriptor validation implemented? | Yes, for the bounded fixture profile through two entrypoints, focused tests, and a hosted workflow. |
| Is the plural `sources/` schema a second implementation? | No. It is a declared compatibility alias referring to the rich singular schema. |
| Are hyphen/underscore names resolved? | No. A rich underscore schema and permissive hyphen scaffold coexist. |
| Are source intake and drift records still only placeholders? | No. Substantive underscore schemas exist; legacy hyphen `.json` files are deprecated compatibility pointers. |
| Is source activation shape present? | Yes, as a substantive `PROPOSED` underscore schema; a hyphen `.json` proposal record also remains. |
| Does this establish source admission or runtime use? | No. Those remain separate and unverified. |

## Bounded current inventory

This inventory covers the files named by the prior README plus their directly declared successors. It is not a recursive tree manifest.

### Substantive schemas

| File | Current posture | Verified shape signal |
|---|---|---|
| [`source_descriptor.schema.json`](source_descriptor.schema.json) | `PROPOSED`; rich implementation schema | Closed object with 20 required top-level fields, controlled substructures, and conditional rules |
| [`source_intake_record.schema.json`](source_intake_record.schema.json) | `PROPOSED`; substantive successor | Closed intake record with identity, descriptor reference, role, observation, drift, disposition, reason-code, and emitter requirements |
| [`source_activation_decision.schema.json`](source_activation_decision.schema.json) | `PROPOSED`; substantive schema | Closed activation-decision shape with source, descriptor, role, operation, context, decision, timing, lineage, and governance requirements |
| [`drift_summary.schema.json`](drift_summary.schema.json) | `PROPOSED`; substantive successor | Closed drift summary with source reference, materiality, changed fields, sensitivity implication, and public-detail posture |
| [`ingest_receipt.schema.json`](ingest_receipt.schema.json) | `PROPOSED`; substantive schema | Closed receipt with source/run identity, timing, outcome, bytes, and digests |
| [`doctrine_artifact_descriptor.schema.json`](doctrine_artifact_descriptor.schema.json) | `PROPOSED`; substantive schema | Closed descriptor requiring identity, digest, provenance, authority status, admission time, and steward signoff reference |
| [`doctrine_artifact_preflight_summary.schema.json`](doctrine_artifact_preflight_summary.schema.json) | Substantive schema; explicit status not verified in-file | Closed preflight-summary shape with required check/render results and presence input |

### Compatibility aliases, pointers, and scaffolds

| File | Classification | Required handling |
|---|---|---|
| [`../sources/source_descriptor.schema.json`](../sources/source_descriptor.schema.json) | `PROPOSED` plural-path compatibility schema | Keep as an alias to the rich singular schema; do not add divergent properties |
| [`source-descriptor.schema.json`](source-descriptor.schema.json) | Permissive `PROPOSED` scaffold | Do not treat as equivalent to the rich schema; resolve by migration/disposition |
| [`source_descriptor.json`](source_descriptor.json) | Proposal metadata record, not JSON Schema | Do not validate payloads against it |
| [`source-descriptor.json`](source-descriptor.json) | Proposal metadata record, not JSON Schema | Do not validate payloads against it |
| [`source-intake-record.json`](source-intake-record.json) | `DEPRECATED_COMPATIBILITY_POINTER` | Read-only pointer to `source_intake_record.schema.json`; writes prohibited by its record |
| [`drift-summary.json`](drift-summary.json) | `DEPRECATED_COMPATIBILITY_POINTER` | Read-only pointer to `drift_summary.schema.json`; writes prohibited by its record |
| [`source-activation-decision.json`](source-activation-decision.json) | `PROPOSED` metadata record | Not the substantive underscore schema; migration/disposition remains unresolved |
| [`run_receipt.schema.json`](run_receipt.schema.json) | Empty permissive `PROPOSED` scaffold | Does not establish a useful RunReceipt contract or validation boundary |

File presence, a `$schema` key, or a `.schema.json` suffix does not establish maturity. Check required fields, `additionalProperties`, conditional constraints, declared status, paired contract, fixtures, validator, and tests before making a support claim.

## SourceDescriptor validation profile

The SourceDescriptor family has an implemented, bounded convergence profile:

| Surface | Verified path | Role |
|---|---|---|
| Semantic contract | [`contracts/source/source_descriptor.md`](../../../../contracts/source/source_descriptor.md) | Defines meaning and anti-collapse boundaries |
| Rich schema | [`source_descriptor.schema.json`](source_descriptor.schema.json) | Implementation shape |
| Plural alias | [`../sources/source_descriptor.schema.json`](../sources/source_descriptor.schema.json) | Compatibility reference to the rich schema |
| Generic validator | [`tools/validators/validate_source_descriptor.py`](../../../../tools/validators/validate_source_descriptor.py) | Validates the fixture family against the rich schema |
| Declared plural validator | [`tools/validators/sources/validate_source_descriptor.py`](../../../../tools/validators/sources/validate_source_descriptor.py) | Validates through the compatibility alias |
| Fixtures | [`fixtures/contracts/v1/source/source_descriptor/`](../../../../fixtures/contracts/v1/source/source_descriptor/README.md) | Two valid fixtures and one expected-negative fixture |
| Convergence tests | [`tests/validators/test_validate_source_descriptor_entrypoints.py`](../../../../tests/validators/test_validate_source_descriptor_entrypoints.py) | Checks both entrypoints, explicit-input behavior, fixture polarity, and working-directory independence |
| Shared schema tests | [`tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) | Exercises common contract fixture behavior for SourceDescriptor |
| Hosted profile | [`.github/workflows/source-descriptor-validate.yml`](../../../../.github/workflows/source-descriptor-validate.yml) | Checks schema aliasing, paths, fixtures, validators, tests, receipt closure, and bounded rights failure cases |

The profile is fixture-only. It does not prove that repository registry instances conform, that an active writer uses either schema path, or that runtime policy and consumers resolve descriptors before use.

## Compatibility and drift

| Drift class | Current signal | Safe posture |
|---|---|---|
| Singular versus plural family | Rich implementation under `source/`; declared compatibility alias under `sources/` | Keep one implementation; resolve path authority through reviewed migration |
| Underscore versus hyphen | Rich `source_descriptor.schema.json`; permissive `source-descriptor.schema.json` | Do not call both canonical or schema-equivalent |
| Schema versus metadata record | `.schema.json` files coexist with proposal/pointer `.json` records | Inspect content; do not infer shape authority from location |
| Deprecated pointers | Intake and drift hyphen records point to underscore schemas with writes disabled | Preserve pointer semantics until references are migrated and rollback is defined |
| Activation naming | Substantive underscore schema coexists with hyphen proposal metadata | Keep state explicit; do not silently replace or duplicate consumers |
| Registry topology | Canonical source registry and parallel views coexist outside this folder | Schema prose must not choose registry writers or move instances |

No move, rename, deletion, alias retirement, or canonical-path change belongs in a documentation-only correction. Those actions require a consumer/reference inventory, compatibility plan, migration, readback, and rollback.

## What belongs here

- machine-checkable JSON Schemas for source-family objects;
- explicit compatibility schemas and read-only pointer records;
- schema-family indexes, migration notes, and disposition records;
- links to semantic contracts, fixtures, validators, tests, registries, policy, and release boundaries.

### What does not belong here

- source registry instances, RAW payloads, lifecycle records, emitted receipts, or release records;
- semantic contracts or policy rules;
- validator implementation, application code, pipelines, or connector code;
- secrets, credentials, private endpoints, sensitive payloads, or harmful-precision material;
- claims that validation establishes truth, admission, rights, review, release, or publication.

## Focused validation

Run from the repository root:

```bash
python tools/validators/validate_source_descriptor.py --fixtures
python tools/validators/sources/validate_source_descriptor.py --fixtures
python -m pytest -q \
  tests/validators/test_validate_source_descriptor_entrypoints.py \
  tests/schemas/test_common_contracts.py -k source_descriptor
```

The matching hosted workflow is:

```text
.github/workflows/source-descriptor-validate.yml
```

Do not append `|| true` to validation commands used as evidence. Preserve actual exit status and classify failures as introduced, inherited, unrelated, unavailable, or expected-negative.

Interpret a pass narrowly:

- schema/fixture polarity and the two SourceDescriptor entrypoints agree for the committed cases;
- the plural schema remains a bounded alias of the rich singular schema;
- required rights fields and selected fail-closed public-release conditions satisfy the workflow’s assertions;
- no source is thereby admitted, activated, retrieved, rights-cleared, sensitivity-cleared, released, or published.

## Maintenance and promotion

Before changing a source-family schema or compatibility record:

1. identify the semantic contract and every active schema/pointer path;
2. classify the file as substantive schema, alias, pointer, proposal metadata, or scaffold;
3. inventory fixtures, validators, tests, registry writers, and consumers affected by the change;
4. preserve source role, rights, sensitivity, temporal, provenance, correction, and supersession distinctions;
5. run the focused profile and retain expected-negative polarity;
6. provide compatibility, migration, readback, and rollback evidence for path or name changes;
7. keep schema acceptance, source admission, review, release, deployment, promotion, and publication as distinct states.

### Promotion evidence

The rich SourceDescriptor schema already has a paired semantic contract, required fields, positive and negative fixtures, two validator entrypoints, focused tests, and hosted CI. Those facts narrow its implementation status; they do not accept the schema or resolve naming/path drift.

Advancing any family member beyond `PROPOSED` still requires, as applicable:

- accepted canonical identity and path;
- steward and review authority;
- compatibility and migration disposition for aliases, pointers, and scaffolds;
- sufficient positive, negative, restricted, stale, correction, and supersession cases;
- registry-writer and runtime-consumer evidence;
- policy, evidence, receipt, correction, rollback, and release integration evidence.

## Open verification register

| Item | Status | Evidence required |
|---|---:|---|
| Complete source-family inventory | `UNKNOWN` | Recursive tracked tree and generated/external dependency inventory |
| Singular/plural SourceDescriptor authority | `HOLD` | Accepted path decision, reference inventory, migration, readback, rollback |
| Hyphen/underscore disposition | `HOLD` | Consumer search and retirement/alias plan for each duplicate name |
| Proposal `.json` records | `NEEDS VERIFICATION` | Object-by-object conversion, retention, migration, or deletion decision |
| RunReceipt scaffold | `NEEDS VERIFICATION` | Paired semantic contract, required shape, fixtures, validator, tests, and consumers |
| Non-SourceDescriptor validator coverage | `UNKNOWN` | Exact validators, fixtures, tests, workflows, and expected-negative cases |
| Registry writer and instance conformance | `UNKNOWN` | Writer binding, canonical record inventory, validation receipts, correction path |
| Runtime/policy consumers | `UNKNOWN` | Code paths, configuration, policy decisions, tests, and deployed-state evidence |
| Accountable ownership and approval | `NEEDS VERIFICATION` | Named authority and review records; CODEOWNERS or CI alone is insufficient |
| Release/public readiness | `DENY BY DEFAULT` | Evidence, policy, review, release, correction, rollback, and publication records |

## Evidence and lineage

This correction reconciles the complete prior README against current GitHub files and the implemented SourceDescriptor workflow. Connected Google Drive SourceDescriptor, source-intake, source-role, and fail-closed validator cards were read only as proposal lineage. Notion was read only as coordination state. Neither was treated as schema acceptance or implementation authority.

No schema, contract, validator, fixture, workflow, registry record, policy, source, lifecycle state, release, deployment, promotion, or publication state changed through this Markdown update.

[Back to top](#top)
