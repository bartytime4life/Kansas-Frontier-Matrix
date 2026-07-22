# `schemas/people-dna-land/` — People / DNA / Land Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-people-dna-land-readme
title: schemas/people-dna-land/ README
type: readme; compatibility-index; schema-boundary
version: v0.2
status: draft; compatibility; transitional; restricted-review; CONFLICTED
updated: 2026-07-22
policy_label: restricted-review
tags: [kfm, schemas, people-dna-land, people, dna, land, compatibility, restricted-review]
[/KFM_META_BLOCK_V2] -->

`schemas/people-dna-land/` is a documentation-only compatibility guard for a non-versioned People / DNA / Land schema path. The inspected machine-schema implementation lane is [`schemas/contracts/v1/domains/people-dna-land/`](../contracts/v1/domains/people-dna-land/README.md), but its canonical status remains **PROPOSED / CONFLICTED** until the schema-home ADR and duplicate Directory Rules authority are resolved.

> [!IMPORTANT]
> This directory is not an accepted home for new schemas. It contains no schema authority, validates no person or land claim, grants no consent, and authorizes no release. Living-person, DNA/genomic, private person-land, and title-like surfaces remain restricted and fail closed unless their independent evidence, rights, consent where required, policy, review, release, correction, and rollback gates pass.

## Purpose

This README prevents `schemas/people-dna-land/` from becoming a second machine-schema authority while the repository converges on one versioned schema home.

It also records the verified maturity boundary of the inspected People / DNA / Land schema lane so maintainers do not mistake schema presence or CI syntax checks for accepted domain contracts, executable validation, evidence closure, policy approval, or publication readiness.

## Authority level

| Field | Value |
|---|---|
| Owning responsibility root | `schemas/` — machine-checkable shape only |
| Directory class | Compatibility / transitional index |
| Authority | Pointer and drift guard; not a machine schema or registry |
| Inspected implementation lane | [`../contracts/v1/domains/people-dna-land/`](../contracts/v1/domains/people-dna-land/README.md) |
| Canonical posture | **PROPOSED / CONFLICTED** — repository placement follows the proposed ADR-0001 shape, but ADR-0001 is not accepted and Directory Rules authority is duplicated |
| Domain posture | Restricted review; deny by default for unsupported living-person, DNA/genomic, private person-land, and title-like output |
| Truth posture | Shape is not truth; EvidenceBundle, policy, review, release state, correction lineage, and rollback support remain separate |

The file's `doc_id` is unique in the inspected repository search. No generator, mirror source, localization source, or superseding document was identified for this README.

## Status

| Surface | Current-session result | Truth status |
|---|---|---|
| This README | Present; documentation-only compatibility guard | **CONFIRMED** |
| Direct schema files in `schemas/people-dna-land/` | None surfaced by the scoped repository search; absence is not a recursive tree proof | **NEEDS VERIFICATION** |
| Versioned People / DNA / Land schema lane | README, three child warning READMEs, and 16 direct `*.schema.json` files inspected | **CONFIRMED** |
| Schema maturity | Fifteen permissive greenfield stubs plus one empty land-ownership scaffold | **CONFIRMED** |
| Exact paired semantic contracts | 4 of 16 schema pointers resolve at their declared domain-contract paths | **CONFIRMED** |
| Exact schema-declared validator pointers | 2 of 15 declared pointers resolve; both implementations raise `NotImplementedError`; the land scaffold declares no validator | **CONFIRMED** |
| Exact schema-declared fixture roots | No referenced fixture-root README resolved for the 15 uniform stubs | **CONFIRMED within inspected paths** |
| Domain instance-validation coverage | Not established; the schema workflow meta-validates all schemas but its configured fixture families are cross-cutting source/evidence/runtime schemas | **CONFIRMED / HOLD** |
| Domain policy, consent, proof, or release enforcement | Explicitly not established by the domain workflow | **CONFIRMED / HOLD** |
| Schema-home ADR | ADR-0001 exists with `status: proposed` | **CONFIRMED** |
| Directory Rules authority | Multiple repository copies exist; the architecture copy calls its own placement proposed/conflicted | **CONFLICTED** |
| Path-specific drift record | No `schemas/people-dna-land/` or parallel land-schema entry appears in the inspected drift register | **NEEDS VERIFICATION** |

## What belongs here

- This compatibility README.
- A temporary, human-readable migration pointer if a reviewed schema-home migration affects this path.
- A deprecation or retirement notice that names the accepted target, effective state, affected consumers, validation, and rollback.
- No generated mirror unless an accepted migration contract identifies the source, generator, digest, edit prohibition, and sunset.

## What does not belong here

- New People / DNA / Land JSON Schemas.
- Hand-maintained copies of schemas from `schemas/contracts/v1/` or `contracts/`.
- Semantic contracts, policy rules, consent grants, revocation records, source descriptors, registry records, fixtures, validators, tests, or runtime code.
- Person, genealogy, DNA/genomic, parcel, deed, title, assessor, tax, court, or private person-land payloads.
- EvidenceBundle or ProofPack instances, validation reports, receipts, catalog records, release manifests, correction notices, rollback cards, or published artifacts.
- Public API, map, tile, graph, search, vector-index, Evidence Drawer, Focus Mode, export, screenshot, or generated-answer payloads.
- Claims that schema conformance proves identity, kinship, consent, death status, DNA relationship, land ownership, title, boundary, rights, sensitivity clearance, legal sufficiency, release, or public safety.

## Lifecycle relationship

Schemas constrain machine shape across the KFM lifecycle; they do not move an object through it:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion remains a governed state transition. A valid schema instance can still be quarantined, restricted, denied, abstained, corrected, withdrawn, or rolled back because evidence, source role, rights, consent, sensitivity, review, release, or integrity requirements are missing.

This compatibility path must never become a lifecycle store or a shortcut around the governed API and released-artifact boundary.

## Naming and placement

The inspected placement evidence establishes the following bounded rule set:

| Question | Current rule |
|---|---|
| What does `schemas/` own? | Machine-checkable shape, not object meaning or policy. |
| Where does the proposed schema-home ADR place domain schemas? | `schemas/contracts/v1/domains/<domain>/...` |
| What is the inspected People / DNA / Land implementation lane? | `schemas/contracts/v1/domains/people-dna-land/` |
| May `schemas/people-dna-land/` evolve independently? | No. That would create parallel schema authority. |
| May `contracts/people-dna-land/*.schema.json` remain a second schema home? | Not as steady state; it requires an ADR-backed migration, mirror, grandfathering, or removal decision. |
| What filename style do current schemas use? | Lowercase snake case plus `.schema.json`; this is implementation evidence, not a ratified naming ADR. |
| What dialect do inspected schemas declare? | JSON Schema Draft 2020-12. |

The proposed ADR permits top-level `schemas/<topic>/` only as a time-bounded scratch surface with tracked migration. This directory is therefore documented as compatibility/transitional, not upgraded to canonical by this README.

## Review burden

Changes require review appropriate to both shape authority and the domain's irreversibility risk:

- schema and contract stewardship for object-family ownership and shape/meaning separation;
- People / DNA / Land domain review for identity, genealogy, DNA/genomic, and land semantics;
- privacy, sensitivity, consent, and rights review for living-person or DNA-bearing surfaces;
- land/title assertion review for assessor/title, parcel/boundary, instrument/ownership, and legal-description distinctions;
- validation review for fixtures, negative cases, validator outputs, and CI coverage;
- release and correction review when a schema change affects a released consumer;
- documentation and Directory Rules review for placement, compatibility, migration, and drift closure.

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `schemas/` changes to `@bartytime4life`; it does not prove semantic approval, sensitivity review, consent authority, release approval, or separation of duties.

## Related folders

| Responsibility | Repository surface | Relationship |
|---|---|---|
| Schema root | [`schemas/`](../README.md) | Owns machine-checkable shape. |
| Domain schema index | [`schemas/contracts/v1/domains/`](../contracts/v1/domains/README.md) | Proposed ADR-0001 domain-lane index. |
| Inspected schema lane | [`schemas/contracts/v1/domains/people-dna-land/`](../contracts/v1/domains/people-dna-land/README.md) | Holds the 16 inspected schema files and transitional child indexes. |
| Semantic contracts | [`contracts/domains/people-dna-land/`](../../contracts/domains/people-dna-land/README.md) | Owns domain object meaning; four exact schema pointers currently resolve here. |
| Contract compatibility path | [`contracts/people-dna-land/`](../../contracts/people-dna-land/README.md) | Pointer-only lane that currently also contains a conflicting land schema. |
| Domain doctrine | [`docs/domains/people-dna-land/`](../../docs/domains/people-dna-land/README.md) | Human-facing scope, identity, sensitivity, consent, land, API, and release guidance. |
| Domain policy | [`policy/domains/people-dna-land/`](../../policy/domains/people-dna-land/README.md) | Domain admissibility boundary. |
| Consent policy | [`policy/consent/people-dna-land/`](../../policy/consent/people-dna-land/README.md) | Consent posture; repository presence is not activation. |
| Fixtures | [`fixtures/domains/people-dna-land/`](../../fixtures/domains/people-dna-land/README.md) | Synthetic example boundary; the domain workflow rejects newly surfaced payloads pending review. |
| Tests | [`tests/domains/people-dna-land/`](../../tests/domains/people-dna-land/README.md) | Intended enforceability proof; executable domain tests are not established. |
| Validators | [`tools/validators/domains/people-dna-land/`](../../tools/validators/domains/people-dna-land/README.md) | Validator index with placeholder implementations. |
| Release candidates | [`release/candidates/people-dna-land/`](../../release/candidates/people-dna-land/README.md) | Candidate boundary; a candidate is not a release. |

## ADRs

| Decision source | Status | Effect on this path |
|---|---|---|
| [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | `proposed` | Proposes `schemas/contracts/v1/domains/<domain>/` as the domain machine-schema home and forbids divergent definitions across `schemas/` and `contracts/`. |
| [`ADR-0002`](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | `draft`; proposed decision; number conflicted | Proposes the responsibility split among contracts, schemas, policy, fixtures, tests, and validators. |
| [`ADR-0010`](../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | `proposed / conflicted` | Records the fail-closed direction for DNA/genomic exposure; its number and relationship to other sensitivity ADRs remain unresolved. |

No inspected ADR has accepted this compatibility directory as a second schema home. Do not cite an ADR filename as an accepted decision without checking its in-file status.

## Boundary

### Shape is not truth

The 16 inspected schemas establish only draft machine-shape surfaces. They do not establish that any producer, consumer, validator, policy evaluator, release gate, or public client uses those shapes correctly.

### Domain shape is not cross-cutting authority

Several domain-local stubs reuse cross-cutting object-family names such as `EvidenceBundle`, `RunReceipt`, `ReleaseManifest`, `CorrectionNotice`, `PromotionDecision`, and `DecisionEnvelope`. Shared schema families also exist elsewhere under `schemas/contracts/v1/`.

Treat the domain-local copies as **PROPOSED / NEEDS VERIFICATION**, not automatic profiles or overrides. Before expanding one, decide whether it should:

1. reference a shared schema;
2. compose a reviewed domain profile;
3. remain a temporary stub; or
4. be deprecated through a migration.

Do not evolve both a shared schema and a domain-local copy independently.

### Sensitive-domain boundary

Schema fields must not turn administrative records into title authority, parcel geometry into boundary proof, identity candidates into canonical people, relationship hypotheses into kinship facts, consent presence into publication authority, or DNA-derived similarity into a public fact.

Public or semi-public consumers must use governed interfaces and released public-safe artifacts. They must not read this directory, the versioned schema lane, canonical stores, restricted stores, or unreleased lifecycle data as truth sources.

## Current inventory

The following inventory is grounded in exact file reads at the inspected repository commit. It is not a claim that the lane is complete or accepted.

### Compatibility directory

| Path | Role | Status |
|---|---|---|
| `schemas/people-dna-land/README.md` | This compatibility and drift guard | **CONFIRMED** |
| Other direct files | None surfaced by scoped search | **NEEDS VERIFICATION** pending recursive tree inventory |

### Versioned domain schemas

Fifteen schemas share this permissive placeholder shape:

- JSON Schema Draft 2020-12;
- unique `$id` under the current CI uniqueness rule;
- `type: object`;
- `required: ["id"]`;
- properties `id`, `spec_hash`, and `version`;
- `additionalProperties: true`;
- `x-kfm.status: PROPOSED`;
- a description that calls the file a greenfield contract-schema stub.

The land-ownership scaffold is even looser: it declares no properties and no required fields, permits additional properties, and remains `PROPOSED`.

| Schema | Current shape | Closure at inspected ref |
|---|---|---|
| [`run_receipt.schema.json`](../contracts/v1/domains/people-dna-land/run_receipt.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`rollback_card.schema.json`](../contracts/v1/domains/people-dna-land/rollback_card.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`domain_validation_report.schema.json`](../contracts/v1/domains/people-dna-land/domain_validation_report.schema.json) | `id`-only stub | Draft semantic contract resolves; declared validator and fixture root do not. |
| [`layer_manifest.schema.json`](../contracts/v1/domains/people-dna-land/layer_manifest.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`catalog_matrix.schema.json`](../contracts/v1/domains/people-dna-land/catalog_matrix.schema.json) | `id`-only stub | Contract and fixture root do not resolve; validator path resolves to a `NotImplementedError` placeholder. |
| [`evidence_bundle.schema.json`](../contracts/v1/domains/people-dna-land/evidence_bundle.schema.json) | `id`-only stub | Contract and fixture root do not resolve; validator path resolves to a `NotImplementedError` placeholder. |
| [`release_manifest.schema.json`](../contracts/v1/domains/people-dna-land/release_manifest.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`decision_envelope.schema.json`](../contracts/v1/domains/people-dna-land/decision_envelope.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`source_state_hash.schema.json`](../contracts/v1/domains/people-dna-land/source_state_hash.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`correction_notice.schema.json`](../contracts/v1/domains/people-dna-land/correction_notice.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`domain_observation.schema.json`](../contracts/v1/domains/people-dna-land/domain_observation.schema.json) | `id`-only stub | Draft semantic contract resolves; declared validator and fixture root do not. |
| [`promotion_decision.schema.json`](../contracts/v1/domains/people-dna-land/promotion_decision.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`domain_layer_descriptor.schema.json`](../contracts/v1/domains/people-dna-land/domain_layer_descriptor.schema.json) | `id`-only stub | Draft semantic contract resolves; declared validator and fixture root do not. |
| [`evidence_drawer_payload.schema.json`](../contracts/v1/domains/people-dna-land/evidence_drawer_payload.schema.json) | `id`-only stub | Declared domain contract, validator, and fixture root do not resolve. |
| [`domain_feature_identity.schema.json`](../contracts/v1/domains/people-dna-land/domain_feature_identity.schema.json) | `id`-only stub | Draft semantic contract resolves; declared validator and fixture root do not. |
| [`land_ownership_assertion.schema.json`](../contracts/v1/domains/people-dna-land/land_ownership_assertion.schema.json) | Empty permissive scaffold | Declared semantic contract does not resolve; no validator or fixture pointer; a divergent copy exists under `contracts/people-dna-land/`. |

### Child indexes

| Child path | Current role |
|---|---|
| [`people/`](../contracts/v1/domains/people-dna-land/people/README.md) | Transitional warning index; not a confirmed schema sublane. |
| [`genealogy/`](../contracts/v1/domains/people-dna-land/genealogy/README.md) | Transitional warning index; not a confirmed schema sublane. |
| [`land-ownership/`](../contracts/v1/domains/people-dna-land/land-ownership/README.md) | Transitional warning index; the concrete land assertion schema is currently in the parent lane. |

### Confirmed parallel-schema drift

[`contracts/people-dna-land/land_ownership_assertion.schema.json`](../../contracts/people-dna-land/land_ownership_assertion.schema.json) and [`schemas/contracts/v1/domains/people-dna-land/land_ownership_assertion.schema.json`](../contracts/v1/domains/people-dna-land/land_ownership_assertion.schema.json) are distinct permissive definitions with different `$id`, description, and `x-kfm` metadata.

The contract compatibility README says that directory is pointer-only and that JSON Schema belongs under the versioned schema lane. The duplicate is therefore **CONFLICTED** and must not receive new fields until an ADR-backed migration or deprecation decision chooses one authority and preserves compatibility.

### `$id` note

The 15 uniform stubs use `https://schemas.kfm.local/contracts/v1/domains/people-dna-land/...`. The land-ownership scaffold uses `https://schemas.kfm.local/schemas/contracts/v1/domains/people-dna-land/...`.

Both are unique under the current workflow check, but `$id` derivation is deferred by ADR-0001. Namespace parity and consumer impact remain **NEEDS VERIFICATION**.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Freeze this path | Do not add schemas or mirrors under `schemas/people-dna-land/`. |
| One machine authority | Resolve shared, domain-local, and contract-root copies before adding fields or consumers. |
| Preserve meaning/shape split | Link each schema to one reviewed semantic contract; do not duplicate contract prose in JSON Schema descriptions. |
| Require closure before promotion | A schema remains `PROPOSED` until contract, registry, valid and invalid fixtures, validator, tests, consumers, policy binding, migration, and steward review are demonstrated. |
| Fail closed | Missing or ambiguous identity, living-person state, consent, DNA authorization, rights, title support, evidence, review, or release state cannot be converted into a permissive output by schema defaults. |
| Reject source-role collapse | Assessor/tax is not title; parcel geometry is not boundary proof; a DNA or genealogy hypothesis is not a confirmed relationship. |
| Keep public paths governed | Public clients use governed APIs and released public-safe artifacts, never schemas or internal stores directly. |
| Record correction impact | Breaking or authority-changing schema work must identify affected fixtures, validators, producers, consumers, releases, correction notices, withdrawals, caches, indexes, and rollback targets. |

## Validation

### What current CI checks

[`schema-validation.yml`](../../.github/workflows/schema-validation.yml) currently:

1. parses every JSON file under `schemas/`;
2. checks every `*.schema.json` against the Draft 2020-12 meta-schema;
3. requires every `schemas/contracts/v1/**/*.schema.json` file to declare Draft 2020-12 and a unique `$id`;
4. runs configured aggregate validators for six shared source/evidence/runtime families;
5. runs `tests/schemas` and `tests/contracts`.

That workflow does **not** configure People / DNA / Land domain instances or fixtures for the 16 schemas listed here. A green run proves their JSON/meta-schema validity and unique IDs, not their field completeness or domain correctness.

[`domain-people-dna-land.yml`](../../.github/workflows/domain-people-dna-land.yml) is a read-only readiness workflow. It intentionally holds executable validation, proof production, consent/revocation enforcement, and release dry-run activity. It refuses to open newly surfaced fixture payloads automatically and does not publish or mutate lifecycle state.

The domain workflow is also designed to fail when executable validator bodies surface before ownership, fixtures, policy binding, and report semantics are accepted. Four inspected domain scripts define `main()` functions that raise `NotImplementedError`; they are placeholders, not validators that maintainers should run as a quickstart.

### Repository-native checks

Use the repository workflow as the controlling executable check. In a trusted checkout, its current commands include:

```bash
make schemas
python -m pytest -q tests/schemas tests/contracts
```

For a documentation-only review, also inspect the exact lane and compatibility conflict:

```bash
find schemas/people-dna-land -maxdepth 2 -type f -print | sort
find schemas/contracts/v1/domains/people-dna-land -maxdepth 2 -type f -print | sort
find contracts/people-dna-land -maxdepth 2 -type f -print | sort
```

Do not add `|| true`, run placeholder domain validators as evidence of success, or interpret a readiness hold as release approval.

### Promotion gates for a schema

A schema may advance beyond a permissive `PROPOSED` stub only when all applicable items are reviewable:

- [ ] one object-family owner and one machine-schema authority are identified;
- [ ] the semantic contract resolves and matches the schema's intended meaning;
- [ ] stable `$id`, version, dialect, compatibility, and normalization rules are accepted;
- [ ] valid and invalid synthetic/public-safe fixtures exist;
- [ ] negative fixtures cover deny, abstain, quarantine, error, correction, and rollback paths where applicable;
- [ ] an executable validator rejects invalid fixtures for the expected reason;
- [ ] tests prove living-person, DNA/genomic, consent/revocation, private-join, assessor/title, parcel/boundary, and evidence-release boundaries where applicable;
- [ ] source role, rights, sensitivity, temporal, EvidenceRef/EvidenceBundle, review, and release references are explicit;
- [ ] producers and consumers pin a compatible schema version;
- [ ] registry and CI coverage are linked;
- [ ] correction, withdrawal, cache/index invalidation, migration, and rollback impact are documented;
- [ ] no restricted payload or secret is stored in schemas, fixtures, logs, or CI artifacts.

## Open questions

| ID | Question | Status | Evidence that closes it |
|---|---|---|---|
| `PDL-SCHEMA-001` | Will ADR-0001 be accepted, amended, or superseded? | **NEEDS VERIFICATION** | Accepted ADR status and schema-home migration plan. |
| `PDL-SCHEMA-002` | Which Directory Rules copy controls placement? | **CONFLICTED** | Authority/supersession decision and stable canonical link. |
| `PDL-SCHEMA-003` | Should this compatibility directory be retained, deprecated, or removed? | **NEEDS VERIFICATION** | Inbound-link/consumer inventory plus migration and rollback decision. |
| `PDL-SCHEMA-004` | Which of the 15 uniform stubs are domain profiles versus misplaced copies of shared object families? | **NEEDS VERIFICATION** | Object-family registry, paired contracts, consumer inventory, and steward decision. |
| `PDL-SCHEMA-005` | Which land-ownership schema path is authoritative? | **CONFLICTED** | ADR/migration decision covering both definitions, `$id`, fixtures, consumers, and deprecation. |
| `PDL-SCHEMA-006` | What `$id` namespace and derivation rule is accepted? | **NEEDS VERIFICATION** | Spec-normalization ADR and registry/consumer parity tests. |
| `PDL-SCHEMA-007` | Where are the valid and invalid fixtures for each accepted domain schema? | **UNKNOWN** | Recursive inventory plus public-safe fixture review. |
| `PDL-SCHEMA-008` | Which executable validators and tests enforce each schema? | **UNKNOWN / HOLD** | Implementations, expected-error fixtures, CI wiring, and successful negative-path results. |
| `PDL-SCHEMA-009` | Which producers or governed consumers use these schemas? | **UNKNOWN** | Code/config references, version pins, integration tests, and run receipts. |
| `PDL-SCHEMA-010` | Which schemas, if any, are eligible for a public-safe derivative? | **NEEDS VERIFICATION** | Evidence, rights, sensitivity, consent where required, policy, review, release, correction, and rollback proof. |
| `PDL-SCHEMA-011` | Why is the parallel land schema absent from the current drift register? | **NEEDS VERIFICATION** | Drift-register review and an ADR-backed resolution entry if required. |

## Rollback

Before merge, abandon or close the draft pull request only with the appropriate authorization. After merge, revert the documentation commit transparently and re-run the documentation and schema checks.

Reverting this README does not resolve schema drift. If a schema has been consumed or released, rollback must preserve its prior version and `$id`, update or revert fixtures/validators/producers/consumers, assess released artifacts and derived indexes, issue correction or withdrawal records where required, and retain a reviewable migration history.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-22 |
| Evidence snapshot | `bartytime4life/Kansas-Frontier-Matrix` at the commit recorded in the implementing pull request |
| Document lifecycle | Draft compatibility guard; not KFM-published |
| Next review trigger | Schema-home or Directory Rules decision; schema add/change; contract, fixture, validator, test, workflow, registry, consumer, policy, consent, release, correction, or rollback change; resolution of the parallel land schema |
