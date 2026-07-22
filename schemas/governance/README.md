# `schemas/governance/` — Governance Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-governance-readme
title: schemas/governance/ README
type: readme; compatibility-index; schema-boundary; migration-guardrail
version: v0.2
status: draft; root-level-governance-compatibility-path; non-authoritative; CONFLICTED; NEEDS VERIFICATION before migration or retirement
updated: 2026-07-22
policy_label: public
tags: [kfm, schemas, governance, compatibility, consent-receipt, overlay-pointer, migration, no-parallel-authority]
related:
  - ../README.md
  - ../contracts/v1/governance/README.md
  - ./overlay_pointer.schema.json
  - ./consent_receipt.schema.json
  - ../../contracts/governance/README.md
  - ../../fixtures/contracts/v1/governance/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/validator-suite.yml
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
notes:
  - "This README is a compatibility and migration guardrail; it is not the canonical v1 governance schema-family index."
  - "Versioned governance machine shape is authored under schemas/contracts/v1/governance/ unless an accepted ADR or migration assigns a different responsibility lane."
  - "The two directly verified root-level schemas are permissive PROPOSED scaffolds with empty properties, additionalProperties true, and no paired contract document."
  - "No schema, contract, policy, consent state, review state, fixture, validator, proof, receipt, release state, or publication behavior is changed by this README."
[/KFM_META_BLOCK_V2] -->

`schemas/governance/` preserves two root-level governance-related schema scaffolds as repository lineage without allowing this path to become a second schema authority.

**Path:** `schemas/governance/README.md`  
**Audience:** governance, schema, contract, policy, privacy, validation, release, and documentation maintainers  
**Authority posture:** compatibility and migration guidance only  
**Default versioned family:** [`schemas/contracts/v1/governance/`](../contracts/v1/governance/README.md)  
**Truth posture:** CONFIRMED target and directly linked files at the reviewed repository snapshot; CONFLICTED root-level placement; NEEDS VERIFICATION for ownership, consumer references, canonical destinations, fixture coverage, validator wiring, and retirement.

> [!IMPORTANT]
> Do not add new canonical governance schemas here. Directory Rules assigns machine-checkable shape to `schemas/` and gives `schemas/contracts/v1/<family>/...` as the default versioned schema home. The linked ADR remains proposed, so migration or retirement still requires reviewed ownership, reference inventory, compatibility planning, and rollback evidence.

> [!CAUTION]
> The current `Overlay Pointer` and `Consent Receipt` files accept any JSON object. Successful validation against either scaffold does **not** prove consent, review, stewardship, policy compliance, source authority, rights clearance, sensitivity clearance, release approval, or safe publication.

## Purpose

This README has four jobs:

1. keep the root-level path visible as lineage;
2. route active versioned governance-schema work to the accepted responsibility lane;
3. prevent permissive scaffolds from being mistaken for operational governance controls; and
4. define the evidence required to migrate, freeze, redirect, or retire the path safely.

It does not choose final homes for the two scaffolds. `overlay_pointer` is presentation and API adjacent; `consent_receipt` is consent, rights, privacy, evidence, and governance adjacent. Their names and source documents are insufficient to settle responsibility ownership.

## Status at the reviewed snapshot

| Item | Verified state | Truth label | Consequence |
|---|---|---|---|
| [`README.md`](README.md) | Existing v0.1 compatibility guardrail; replaced by this v0.2 draft. | CONFIRMED | The path already declared itself non-canonical but lacked a complete migration and validation boundary. |
| [`overlay_pointer.schema.json`](overlay_pointer.schema.json) | JSON Schema 2020-12 object; empty `properties`; no `required`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; `contract_doc: null`. | CONFIRMED | Accepts any JSON object; not a meaningful overlay contract or governance gate. |
| [`consent_receipt.schema.json`](consent_receipt.schema.json) | JSON Schema 2020-12 object; empty `properties`; no `required`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; `contract_doc: null`. | CONFIRMED | Accepts any JSON object; not a meaningful consent, rights, privacy, or audit gate. |
| [`schemas/contracts/v1/governance/`](../contracts/v1/governance/README.md) | Versioned governance-family index with four surfaced schemas of mixed maturity. | CONFIRMED | Active governance schema work belongs in the versioned family unless reviewed responsibility analysis assigns another canonical family. |
| Root-level fixture families for these two names | No matching fixture family was surfaced in the reviewed repository search. | NEEDS VERIFICATION | Do not infer positive/negative behavior, validator coverage, or safe consumer use. |
| Root-level consumers | No exhaustive reference inventory was produced by the connected repository search. | UNKNOWN | Do not rename, move, delete, or silently repoint either schema. |
| Canonical destination for each scaffold | Not decided by an accepted migration record inspected for this update. | NEEDS VERIFICATION | Preserve lineage and keep new canonical work out of this lane. |

## Authority boundary

KFM keeps related responsibilities separate:

| Responsibility | Owning surface | Rule for this lane |
|---|---|---|
| Machine-checkable governance shape | `schemas/contracts/v1/governance/` or another reviewed versioned family | This root-level lane is not a parallel authority. |
| Governance object meaning | [`contracts/governance/`](../../contracts/governance/README.md) | A source-document pointer is not a semantic contract. |
| Human governance doctrine and duties | `docs/governance/` | Documentation explains review and duty; schemas do not grant authority. |
| Allow, deny, restrict, abstain, consent, rights, and sensitivity decisions | `policy/` and the accepted policy-schema family | Shape validation must not substitute for policy evaluation. |
| Valid, invalid, negative, and golden examples | [`fixtures/contracts/v1/governance/`](../../fixtures/contracts/v1/governance/README.md) or another accepted fixture family | Fixtures are proof inputs, not schema or policy authority. |
| Validator implementation and executable tests | `tools/validators/` and `tests/` | A validator must identify its exact schema, fixtures, failure behavior, and coverage boundary. |
| Evidence, receipts, and audit records | accepted evidence and receipt lifecycle lanes | Never store emitted consent or governance records beside schemas. |
| Release, correction, withdrawal, and rollback decisions | `release/` and accepted release contracts/schemas | Governance schema validity is not release approval. |
| Runtime, API, MapLibre, or UI behavior | governed application/package/API lanes | Public and standard clients must use governed interfaces and released projections. |

The responsibility split is summarized by [`schemas/README.md`](../README.md), [Directory Rules](../../docs/doctrine/directory-rules.md), and the [contract-schema-policy split](../../docs/architecture/contract-schema-policy-split.md).

## Repository fit

```text
schemas/
├── README.md
├── governance/                         # this non-authoritative compatibility lane
│   ├── README.md                       # this file
│   ├── overlay_pointer.schema.json     # permissive PROPOSED scaffold
│   └── consent_receipt.schema.json     # permissive PROPOSED scaffold
└── contracts/
    └── v1/
        ├── governance/                 # default versioned governance family
        ├── review/                     # overlap-sensitive review family
        ├── policy/                     # policy-decision shapes
        ├── evidence/                   # evidence-reference and bundle shapes
        └── release/                    # release-decision and rollback shapes

contracts/governance/                  # semantic governance meaning
docs/governance/                       # roles, duties, escalation, separation of duties
policy/                                # admissibility, consent, rights, sensitivity
fixtures/contracts/v1/governance/      # governance schema examples
tools/validators/                      # validator implementation
tests/schemas/                         # executable schema tests
release/                               # release, correction, withdrawal, rollback authority
```

The versioned governance-family index already records overlap-sensitive work, including another review-family path. Do not use this compatibility directory to resolve those conflicts or to create another copy.

## Direct scaffold inventory

### `overlay_pointer.schema.json`

Verified declarations:

| Declaration | Current value |
|---|---|
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `kfm://schemas/governance/overlay_pointer.schema.json` |
| `type` | `object` |
| `properties` | empty |
| `required` | absent |
| `additionalProperties` | `true` |
| `x-kfm.status` | `PROPOSED` |
| `x-kfm.source_docs` | [`docs/domains/people-dna-land/sublanes/dna.md`](../../docs/domains/people-dna-land/sublanes/dna.md) |
| `x-kfm.contract_doc` | `null` |

The source document supports lineage only. It does not establish the schema's final responsibility root, field contract, overlay identity rules, API semantics, authorization posture, or publication safety.

### `consent_receipt.schema.json`

Verified declarations:

| Declaration | Current value |
|---|---|
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| `$id` | `kfm://schemas/governance/consent_receipt.schema.json` |
| `type` | `object` |
| `properties` | empty |
| `required` | absent |
| `additionalProperties` | `true` |
| `x-kfm.status` | `PROPOSED` |
| `x-kfm.source_docs` | [`API_CONTRACTS.md`](../../docs/domains/people-dna-land/API_CONTRACTS.md) and [`sublanes/dna.md`](../../docs/domains/people-dna-land/sublanes/dna.md) |
| `x-kfm.contract_doc` | `null` |

The filename does not prove a consent event exists. A trustworthy consent receipt would require accepted semantic meaning, subject and authority rules, scope and purpose, timestamps, versioning, provenance, revocation or withdrawal handling, policy and sensitivity enforcement, retention controls, audit linkage, fixtures, validators, tests, and correction/rollback behavior appropriate to the use case. Those requirements remain outside this scaffold and NEED VERIFICATION.

## Compatibility contract

| Rule | Requirement |
|---|---|
| Freeze canonical growth | Do not add new canonical fields or new schema families under `schemas/governance/`. |
| Do not create new consumers | New code, validators, APIs, pipelines, or UI features must not bind to these root-level paths or `$id` values as canonical contracts. |
| Preserve existing references | Inventory and migrate consumers before moving, renaming, redirecting, or deleting either file. |
| Do not silently repoint | A replacement path or `$id` requires an explicit migration map, compatibility window, and rollback target. |
| Keep meaning separate | Establish or link the accepted semantic contract before promoting machine shape. |
| Treat permissiveness as a blocker | Empty `properties` plus `additionalProperties: true` is scaffold evidence, not an operational validation boundary. |
| Fail safely | Where consent, living-person data, DNA/genomic data, cultural sensitivity, precise locations, or other protected information may be involved, default to quarantine, restriction, generalization, redaction, or denial until policy and authority are proven. |
| Preserve auditability | Migration must retain original path, original `$id`, source lineage, decision record, affected consumers, reviewer identity, validation evidence, and rollback instructions. |

## Consumer rules

### New consumers

Do not use either compatibility scaffold as a production contract, release gate, policy decision, consent check, audit proof, or public-interface guarantee.

### Existing consumers

If a consumer is found:

1. record its repository path, owner, runtime or build role, schema path, and `$id` dependency;
2. determine whether it parses the schema, validates payloads, generates code, emits records, or merely links documentation;
3. preserve current behavior until a reviewed replacement and test plan exist;
4. test both old and proposed paths during the compatibility window; and
5. retain a reversible mapping until downstream parity is proven.

### Validators and CI

Report only the exact burden a check proves. JSON parse success proves syntax. Meta-schema success proves the schema document conforms to the declared dialect. Fixture polarity proves only the reviewed examples. None of those results proves semantic truth, consent, authority, policy approval, rights clearance, review completion, release readiness, or publication safety.

### Runtime and public clients

Standard clients must consume governed interfaces and released projections. They must not read schema directories as runtime data stores or treat a scaffold's existence as permission to expose People-DNA-Land information, consent state, overlay details, or precise locations.

## Migration and retirement gates

Migration is a governed compatibility change, not a file move. Complete these gates separately for each scaffold:

- [ ] Assign accountable governance, schema, contract, policy, privacy/rights, validation, and release reviewers.
- [ ] Produce a repository-wide reference and `$id` consumer inventory.
- [ ] Decide the object's responsibility family from meaning and lifecycle, not its topic or current filename.
- [ ] Record the decision in an accepted ADR, migration note, or authority register.
- [ ] Create or confirm the semantic contract and its policy/sensitivity boundary.
- [ ] Define a non-permissive versioned schema with stable identity and explicit compatibility posture.
- [ ] Add public-safe valid, invalid, boundary, and revocation/withdrawal examples where applicable.
- [ ] Add dedicated or aggregate validator coverage with fail-closed negative tests.
- [ ] Verify cross-platform/runtime parity for every material consumer.
- [ ] Document old-path and old-`$id` handling, deprecation window, correction path, and rollback target.
- [ ] Migrate consumers without maintaining divergent definitions.
- [ ] Freeze or retire the compatibility file only after references and release dependencies are cleared.

Until all applicable gates pass, retain both files as PROPOSED lineage and keep this README visible.

## What belongs here

- This compatibility README.
- The two existing PROPOSED scaffolds while migration ownership and consumers remain unresolved.
- Minimal deprecation or redirect metadata approved by a migration review.
- Links to the versioned family, decision record, migration register, validation evidence, and rollback plan.

## What does not belong here

- New canonical governance schemas or a new version hierarchy.
- Semantic contracts, policy rules, consent policy, privacy rules, rights determinations, or sensitivity decisions.
- Real consent receipts, review records, steward assignments, evidence records, proof objects, audit logs, or release decisions.
- Fixtures, validator implementation, executable tests, pipelines, APIs, runtime code, UI code, MapLibre configuration, or generated artifacts.
- Secrets, credentials, personal data, DNA/genomic data, protected cultural information, exact sensitive locations, or other operational records.
- Claims that schema validity establishes truth, evidence closure, consent, approval, compliance, review, release, or publication.

## Validation boundary

### Local structural checks

```bash
find schemas/governance -maxdepth 1 -type f -print | sort

python -m json.tool schemas/governance/overlay_pointer.schema.json >/dev/null
python -m json.tool schemas/governance/consent_receipt.schema.json >/dev/null

python - <<'PY'
import json
from pathlib import Path

from jsonschema import Draft202012Validator

for path in sorted(Path("schemas/governance").glob("*.schema.json")):
    Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))
    print(f"meta-schema valid: {path}")
PY

python -m pytest -q tests/schemas/test_common_contracts.py
```

The pytest command exercises versioned families under `schemas/contracts/v1/` when matching fixture directories exist. It does not promote or fixture-test the two root-level compatibility scaffolds.

### Current workflow boundary

The inspected [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) parses JSON under `schemas/`, meta-schema checks the canonical `schemas/contracts/v1/**/*.schema.json` inventory, checks unique canonical-v1 `$id` values, requires non-empty fixtures for six configured aggregate validators, and runs repository-owned schema/contract tests.

The two root-level scaffolds are outside that canonical-v1 meta-schema and aggregate-fixture inventory. The inspected aggregate runner is bounded to source, evidence, and runtime families; [`validator-suite.yml`](../../.github/workflows/validator-suite.yml) does not establish dedicated coverage for `overlay_pointer` or `consent_receipt`. A green workflow therefore must not be reported as operational validation of these objects.

The canonical governance fixture lane confirms a populated `review_record` family, not fixture coverage for these two root-level names. The dedicated [`validate_review_record.py`](../../tools/validators/validate_review_record.py) is itself a short greenfield stub at the reviewed snapshot.

## Review burden for any schema change

Any edit to the two JSON Schema files is outside this README-only change and should require, at minimum:

- [ ] confirmed semantic contract and responsible family;
- [ ] explicit field and identity review;
- [ ] policy, rights, privacy, sensitivity, and retention review proportional to the data;
- [ ] valid and invalid fixture review;
- [ ] validator and fail-closed test review;
- [ ] consumer and `$id` compatibility review;
- [ ] source-role, evidence, review, release, correction, and rollback boundaries;
- [ ] proof that no public path bypasses governed APIs or release gates;
- [ ] a migration note if path, title, filename, family, or `$id` changes.

## Definition of done

### This README revision

- [x] Identifies the lane as non-authoritative compatibility guidance.
- [x] Describes the two directly verified scaffolds without promoting them.
- [x] Routes active versioned governance-schema work away from the root-level path.
- [x] Separates schema shape from contracts, policy, evidence, fixtures, validators, governance events, and release authority.
- [x] Documents the bounded CI and test surface.
- [x] Preserves migration, correction, and rollback questions.

### Executable or migration maturity

- [ ] Owners and accountable reviewers are assigned.
- [ ] Consumer and `$id` references are inventoried.
- [ ] Final responsibility families are accepted.
- [ ] Semantic contracts and policy boundaries are accepted.
- [ ] Non-permissive schemas, fixtures, validators, and tests exist.
- [ ] Consent withdrawal/revocation and sensitive-data controls are proven where applicable.
- [ ] Compatibility, correction, deprecation, and rollback plans are exercised.
- [ ] Current evidence supports freezing, redirecting, migrating, or retiring the root-level files.

Completing this README does not complete any executable, consent, governance, policy, release, or migration gate.

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Accountable owner for `schemas/governance/` | NEEDS VERIFICATION | Reviewed ownership or CODEOWNERS/steward assignment. |
| Complete recursive inventory | NEEDS VERIFICATION beyond the three directly reviewed files | Mounted-tree or generated schema manifest at the final commit. |
| Repository-wide path and `$id` consumers | UNKNOWN | Code-aware reference scan, generated-code inventory, and runtime/build owner confirmation. |
| ADR-0001 acceptance | PROPOSED | Required steward approvals or a superseding accepted decision. |
| `overlay_pointer` semantic contract and final family | NEEDS VERIFICATION | Object contract, API/UI boundary, consumer evidence, and placement decision. |
| `consent_receipt` semantic contract and final family | NEEDS VERIFICATION | Consent authority, purpose/scope, rights/privacy/sensitivity policy, lifecycle, revocation, audit, and placement decision. |
| Fixture and validator coverage for both root-level schemas | NOT CONFIRMED | Valid/invalid fixture families, validator wiring, negative canaries, and current passing runs. |
| Migration and deprecation window | NOT DEFINED | Accepted migration map, compatibility metadata, downstream parity, and rollback drill. |
| Public or runtime use | UNKNOWN | Governed route, policy enforcement, release evidence, and audit proof. |

## Evidence ledger

Repository evidence for this revision was reviewed against `bartytime4life/Kansas-Frontier-Matrix@640fc2f3c9720cf17d640f0267bf540328e973f0`.

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Prior `schemas/governance/README.md` blob `e0e4c7fcc09fea2069f1fb35af15418222053d18` | CONFIRMED | Existing compatibility purpose, direct inventory, and open placement questions. | Complete migration, consumer inventory, or executable behavior. |
| [`schemas/README.md`](../README.md) | CONFIRMED | Machine-shape authority, root boundaries, and current workflow description. | Acceptance or completeness of every child schema. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | CONFIRMED governing doctrine | Responsibility-root placement, default versioned schema home, no-parallel-authority rule, and migration discipline. | Accepted object placement for either scaffold. |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | CONFIRMED file / PROPOSED decision | Intended versioned schema-home convention and treatment of root topic paths as lineage/conflict. | Accepted decision or completed migration. |
| [`overlay_pointer.schema.json`](overlay_pointer.schema.json) blob `631f5aa39a137ebd449505f3362f5da547b384eb` | CONFIRMED PROPOSED scaffold | Declared dialect, identity, source lineage, empty shape, and absent contract pointer. | Overlay meaning, policy, API behavior, or publication safety. |
| [`consent_receipt.schema.json`](consent_receipt.schema.json) blob `a178b759fa19922f8d6c6adf1ec13402f9784e75` | CONFIRMED PROPOSED scaffold | Declared dialect, identity, source lineage, empty shape, and absent contract pointer. | Consent, authority, rights/privacy controls, revocation, audit, or release. |
| [`schemas/contracts/v1/governance/README.md`](../contracts/v1/governance/README.md) | CONFIRMED versioned family index | Active family routing, mixed schema maturity, and known overlap risks. | Promotion of the root scaffolds or resolution of all governance-family conflicts. |
| [`contracts/governance/README.md`](../../contracts/governance/README.md) | CONFIRMED semantic-contract lane | Separation of governance meaning from machine shape. | A paired contract for either root scaffold. |
| [`fixtures/contracts/v1/governance/README.md`](../../fixtures/contracts/v1/governance/README.md) | CONFIRMED bounded fixture index | Populated canonical `review_record` fixtures and missing coverage signals for other surfaced governance schemas. | Root-level overlay or consent fixture coverage. |
| [`tests/schemas/test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) | CONFIRMED test source / not run during drafting | Versioned governance-family fixture discovery when matching fixture directories exist. | Root-level scaffold coverage or a current successful run. |
| [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) and [`validator-suite.yml`](../../.github/workflows/validator-suite.yml) | CONFIRMED workflow definitions | Current syntax, canonical-v1, aggregate-validator, fixture, and test boundaries. | Operational governance, consent, policy, release, or dedicated coverage for these two scaffolds. |
| [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) and [`VERIFICATION_BACKLOG.md`](../../docs/registers/VERIFICATION_BACKLOG.md) | CONFIRMED repository register surfaces | Existing places to record path drift and unresolved verification work. | That these two scaffold migrations already have complete register entries. |

## Correction and rollback

Correct this README when:

- ADR-0001 is accepted, rejected, amended, or superseded;
- either scaffold gains a semantic contract, owner, destination, fixtures, validator, consumer, policy binding, or release role;
- path or `$id` references are inventoried;
- the versioned governance, review, policy, evidence, release, or receipt families change materially;
- a migration, deprecation, redirect, or retirement decision is approved; or
- any current-state statement no longer matches the repository.

Before merge, rollback means closing or abandoning the scoped review branch. After merge, use a transparent revert of the documentation commit and re-run applicable documentation, schema, contract, and link checks. Do not force-push shared history or delete, rename, or redirect the compatibility schemas as part of a README rollback.

Reverting this README changes documentation only. It does not alter schema behavior, contracts, policy, consent state, privacy or rights controls, fixtures, validators, tests, governance records, evidence, receipts, release state, public interfaces, deployments, or publication state.
