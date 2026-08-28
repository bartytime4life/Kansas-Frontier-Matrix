<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-policy-readme
title: schemas/contracts/policy/ — Policy Schema Compatibility, Routing, and Migration Index
type: readme; directory-readme; compatibility-index; schema-routing-guardrail; migration-index
version: v1.1
status: draft; index-only; deprecated-for-new-schemas; canonical-target-present; mixed-target-maturity; overlap-unresolved; NEEDS VERIFICATION
policy_label: public
owners: OWNER_TBD — Schema steward · Policy steward · Contract steward · Governance steward · Release steward · Sensitivity steward · Redaction steward · Validation steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — blank file was replaced by v1 on 2026-07-03
updated: 2026-07-15
current_path: schemas/contracts/policy/README.md
proposed_canonical_target: schemas/contracts/v1/policy/
truth_posture: CONFIRMED target README and prior blob, schemas root responsibility, proposed ADR-0001 versioned schema-home direction, current schemas/contracts/v1/policy family index and five surfaced files, concrete PolicyDecision and SensitivityLabel schemas, permissive PolicyInputBundle and PromotionDecision scaffolds, redaction receipt placeholder/naming drift, PolicyDecision fixtures and common schema harness coverage, missing declared validate_policy_decision.py at the checked path, and policy/governance/release overlap at the pinned snapshot / UNKNOWN exhaustive recursive inventory, active consumers, accepted registry records, validator coverage beyond checked paths, policy runtime enforcement, release integration, and production use / NEEDS VERIFICATION migration manifest, object ownership decisions, namespace normalization, fixture expansion, validators, negative tests, registry state, deprecation window, correction propagation, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 21e44bb292afe8227a08b08b47683e581e92fc5b
  prior_blob: aa0f01fe231ee73381180b3f29c248c2e172b7fd
related:
  - ../../README.md
  - ../v1/policy/README.md
  - ../v1/policy/policy_decision.schema.json
  - ../v1/policy/sensitivity_label.schema.json
  - ../v1/policy/policy_input_bundle.schema.json
  - ../v1/policy/promotion_decision.schema.json
  - ../v1/policy/redaction-receipt.json
  - ../v1/governance/README.md
  - ../../../contracts/policy/README.md
  - ../../../contracts/policy/policy_decision.md
  - ../../../contracts/policy/policy_input_bundle.md
  - ../../../contracts/policy/sensitivity_label.md
  - ../../../policy/README.md
  - ../../../fixtures/contracts/v1/policy/README.md
  - ../../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/registers/DRIFT_REGISTER.md
tags: [kfm, schemas, contracts, policy, compatibility-index, versioned-schema-home, policy-decision, sensitivity-label, policy-input-bundle, promotion-decision, redaction-receipt, governance-overlap, release-overlap, migration, no-parallel-authority]
notes:
  - "v1.1 replaces a generic path-pointer README with a repository-grounded compatibility, routing, and migration guardrail."
  - "The versioned policy schema family now exists; this unversioned path is frozen for new schemas."
  - "Object ownership and maturity differ across PolicyDecision, SensitivityLabel, PolicyInputBundle, PromotionDecision, and RedactionReceipt."
  - "This revision changes documentation only and selects, moves, renames, deletes, activates, or publishes no schema."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/contracts/policy/` — Policy Schema Compatibility, Routing, and Migration Index

> **Purpose.** Keep the unversioned policy-schema path frozen and inspectable while routing machine-checkable policy-support shapes to the current versioned family and exposing unresolved policy, governance, release, sensitivity, redaction, validator, fixture, namespace, and activation boundaries.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility index" src="https://img.shields.io/badge/path-compatibility__index-orange">
  <img alt="New schemas: frozen" src="https://img.shields.io/badge/new__schemas-frozen-critical">
  <img alt="Target: v1 policy" src="https://img.shields.io/badge/target-v1%2Fpolicy-blueviolet">
  <img alt="Target maturity: mixed" src="https://img.shields.io/badge/target-mixed__maturity-red">
</p>

> [!IMPORTANT]
> `schemas/contracts/policy/` is **index-only and deprecated for new machine-schema definitions**. The current versioned family exists at `schemas/contracts/v1/policy/`. New schemas, `$ref` targets, registry activations, fixtures, validators, or consumer bindings must not be added to this unversioned path.

> [!WARNING]
> The versioned family is not uniformly mature or conflict-free. It contains concrete proposed schemas, permissive scaffolds, a non-schema placeholder, namespace and fixture-path drift, and objects that overlap governance and release responsibilities. Do not bulk-copy, rename, activate, or delete files until an inventory-backed migration resolves object ownership and preserves consumers.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Routing](#object-and-responsibility-routing) · [Inventory](#confirmed-versioned-family-inventory) · [Drift](#confirmed-drift-and-conflicts) · [Semantics](#policy-object-anti-collapse-rules) · [Proof](#fixtures-tests-validators-and-ci) · [Migration](#governed-migration-sequence) · [Status model](#finite-status-model) · [Template](#minimal-compatibility-note) · [Done](#definition-of-done) · [Validation](#validation) · [Rollback](#correction-deprecation-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `schemas/contracts/policy/README.md` | **CONFIRMED** | Compatibility target exists; prior blob is pinned in metadata. |
| Other direct files under `schemas/contracts/policy/` | **NOT SURFACED in bounded search** | Treat this path as README-only until recursive inventory proves otherwise. |
| `schemas/` | **CONFIRMED responsibility root** | Owns machine-checkable shape, not semantic meaning, policy execution, fixtures, validators, records, or release authority. |
| ADR-0001 | **CONFIRMED document / status PROPOSED** | Proposes versioned schema homes under `schemas/contracts/v1/`; this README does not accept or amend it. |
| `schemas/contracts/v1/policy/` | **CONFIRMED present / mixed maturity** | Current versioned policy-support schema family exists. |
| `policy_decision.schema.json` | **CONFIRMED concrete / PROPOSED** | Closed schema with required fields and finite outcomes. |
| `sensitivity_label.schema.json` | **CONFIRMED concrete / PROPOSED** | Closed schema with explicit sensitivity levels. |
| `policy_input_bundle.schema.json` | **CONFIRMED permissive scaffold / PROPOSED** | Requires only `id`; field-level enforcement is incomplete. |
| `promotion_decision.schema.json` | **CONFIRMED empty scaffold / PROPOSED** | Ownership overlaps governance and release; placement is unresolved. |
| `redaction-receipt.json` | **CONFIRMED placeholder / non-schema filename** | Must not be treated as an active JSON Schema. |
| PolicyDecision fixtures | **CONFIRMED minimal family** | One valid and one missing-required-field invalid example are documented. |
| Common schema harness | **CONFIRMED discovers top-level `policy/*.schema.json`** | Matching versioned policy fixtures can be tested; this does not cover the unversioned compatibility path. |
| Declared PolicyDecision validator | **ABSENT at checked path** | `tools/validators/validate_policy_decision.py` was not found; schema metadata is not implementation proof. |
| Active registry, consumers, runtime enforcement, release use | **UNKNOWN** | Path presence and schema validity do not prove activation or production use. |

**Authority of this document:** compatibility guidance, routing, drift disclosure, and migration guardrails only. Accepted ADRs, semantic contracts, schema files, registries, policy bundles, validators, fixtures, tests, runtime evidence, review records, release records, correction records, and steward decisions outrank this README.

---

## Placement and authority

### Responsibility split

```text
contracts/policy/                 semantic meaning
schemas/contracts/v1/policy/     machine-checkable policy-support shape
policy/                           executable or declarative policy authority
fixtures/contracts/v1/policy/    deterministic valid and invalid examples
tests/                            enforceability proof
tools/validators/                 validator implementation
data/receipts/ and data/proofs/   emitted audit and proof artifacts
release/                          promotion, release, correction, withdrawal, rollback authority
```

This compatibility path must not become any of those authorities.

### Current path class

| Field | Value |
|---|---|
| Compatibility class | `deprecated` for new schemas; `index-only` while references remain |
| Write posture | README, drift notes, and migration pointers only |
| Schema posture | No new `*.schema.json` or schema-like JSON files |
| Consumer posture | No new imports, `$ref` targets, registry activations, or API bindings |
| Migration posture | Object-by-object; never blind folder copy |
| Removal posture | Not removal-ready until recursive inventory and inbound-reference checks pass |
| Required review | Schema, policy, contract, governance, release, sensitivity/redaction, migration, validation, and docs stewards |

### Lifecycle and publication boundary

Schema validation can constrain the shape of a policy-support record. It cannot:

- execute policy;
- grant access;
- lower sensitivity;
- establish consent;
- prove evidence closure;
- approve promotion;
- publish a layer or answer;
- create a release manifest;
- authorize correction or rollback.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a schema-validation side effect.

---

## Object and responsibility routing

| Object or concern | Current or proposed owner | Routing posture |
|---|---|---|
| `PolicyDecision` meaning | `contracts/policy/policy_decision.md` | Schema shape belongs in versioned policy family. |
| `PolicyDecision` shape | `schemas/contracts/v1/policy/policy_decision.schema.json` | Concrete PROPOSED schema; activation still requires proof. |
| `PolicyInputBundle` meaning | `contracts/policy/policy_input_bundle.md` | Input object; must not collapse into decision output. |
| `PolicyInputBundle` shape | `schemas/contracts/v1/policy/policy_input_bundle.schema.json` | Permissive scaffold; hardening required before activation. |
| `SensitivityLabel` meaning | `contracts/policy/sensitivity_label.md` | Label semantics and obligations remain contract/policy concerns. |
| `SensitivityLabel` shape | `schemas/contracts/v1/policy/sensitivity_label.schema.json` | Concrete PROPOSED schema; public-safe use still policy-gated. |
| `PromotionDecision` | governance/release-adjacent | Do not select policy, governance, or release schema home without explicit decision and migration record. |
| `RedactionReceipt` | receipt/proof/governance-adjacent | Placeholder must not become receipt authority; emitted receipts belong in governed receipt roots. |
| Policy rules and bundles | `policy/` | Never stored or executed from schema directories. |
| Runtime policy evaluation | governed runtime/package lanes | Must consume accepted schemas and policy bundles; no direct authority here. |
| Fixtures and tests | `fixtures/` and `tests/` | Examples and proof only. |
| Release/correction/rollback | `release/` | Schema records may reference release state but never create it. |

### No generic bulk migration

A migration must classify each artifact by object identity and responsibility. A folder-level move from `schemas/contracts/policy/` to `schemas/contracts/v1/policy/` is safe only if recursive inventory proves that every artifact is a policy-support schema, every `$id` and `$ref` is preserved or migrated, and no governance, release, receipt, policy-code, or record content is mixed in.

---

## Confirmed versioned family inventory

| File | Current maturity | Key facts | Required next step |
|---|---|---|---|
| `policy_decision.schema.json` | `DRAFT_SCHEMA` / PROPOSED | Requires `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, `evaluated_at`; closed object. | Expand negative fixtures, verify validator, registry, policy-version semantics, and consumers. |
| `sensitivity_label.schema.json` | `DRAFT_SCHEMA` / PROPOSED | Closed object; levels include `public`, `generalized`, `restricted`, `quarantine`. | Verify obligations, transition rules, fixtures, validator, and policy integration. |
| `policy_input_bundle.schema.json` | `STUB` / PROPOSED | Requires only `id`; additional properties allowed. | Define inputs, policy/version refs, subject/resource/action context, evidence and consent refs, and closed-shape strategy. |
| `promotion_decision.schema.json` | `STUB` / CONFLICTED | Empty properties and permissive shape; overlaps governance/release. | Resolve object owner and canonical schema family before hardening or consumer use. |
| `redaction-receipt.json` | `PLACEHOLDER` / CONFLICTED | Not named `*.schema.json`; overlaps governance/receipt lanes. | Inventory competing receipt definitions and select canonical contract/schema/receipt roles. |

### PolicyDecision shape currently enforced

```text
decision_id
outcome = ANSWER | ABSTAIN | DENY | ERROR
policy_family = promotion | access | render | capability | consent | sensitivity
reasons[]
obligations[]
evaluated_at
additionalProperties = false
```

This vocabulary is schema evidence, not proof that every policy domain should use these exact outcomes or families forever. Any change requires contract, policy, fixture, validator, consumer, and migration review.

---

## Confirmed drift and conflicts

| Drift | Current evidence | Governance implication |
|---|---|---|
| Unversioned versus versioned path | This README is under `schemas/contracts/policy/`; active family index is under `schemas/contracts/v1/policy/`. | Freeze unversioned writes and migrate references deliberately. |
| ADR status inconsistency | ADR-0001 is PROPOSED while some adjacent docs may describe it more strongly. | Follow the ADR artifact's own status until accepted successor evidence exists. |
| Policy versus governance/release | `PromotionDecision` appears in policy and governance/release-adjacent surfaces. | Owner and canonical schema family need explicit resolution. |
| Redaction receipt duplication/naming | Policy placeholder uses `redaction-receipt.json`; governance has schema-shaped receipt surfaces. | Do not infer equivalence or delete either without semantic and consumer comparison. |
| `$id` namespace drift | Policy schemas use HTTPS local schema IDs while other families may use `kfm://`. | Namespace decision and migration mapping required. |
| Fixture-root drift | Policy schema metadata points to more than one fixture-root convention. | Normalize after inventory; do not silently move fixtures. |
| Policy path drift | Schema metadata points to `policy/policy/`, while actual policy root has other families. | Correct metadata only with verified policy ownership and consumer tests. |
| Validator-pointer drift | PolicyDecision schema declares a validator file absent at the checked path. | Mark validator support missing; do not claim dedicated validation. |
| Schema maturity drift | Concrete closed schemas coexist with permissive and non-schema placeholders. | Family-level “schema validation passed” must not imply every object is enforced. |

---

## Policy object anti-collapse rules

1. **Shape is not policy execution.**
2. **A PolicyInputBundle is input, not a decision.**
3. **A PolicyDecision is not a Runtime DecisionEnvelope.**
4. **A PolicyDecision is not a ReviewRecord.**
5. **A PolicyDecision is not a ReleaseManifest or PromotionDecision.**
6. **A SensitivityLabel is not permission to publish.**
7. **A redaction schema or placeholder is not an emitted RedactionReceipt.**
8. **A receipt is not evidence closure or release approval.**
9. **A schema-valid record may still be semantically invalid, unsupported, stale, unauthorized, or unreleased.**
10. **Missing policy, sensitivity, consent, rights, review, evidence, or release support fails closed where risk matters.**
11. **Public clients consume governed decisions through governed interfaces, never schema files or internal stores directly.**
12. **Generated language cannot replace policy inputs, policy evaluation, evidence, review, or release state.**

### Minimum audit posture

An accepted policy-support record should be traceable, where material, to:

- stable object identity and schema version;
- policy family and exact policy/bundle version;
- evaluated subject, resource, action, purpose, and context;
- EvidenceRefs or evidence-support state;
- sensitivity, consent, rights, and access context;
- deterministic finite outcome;
- structured reasons and obligations;
- evaluation timestamp and evaluator identity/class;
- review state where required;
- release, correction, supersession, and rollback references where applicable.

The current PolicyDecision schema does not enforce all of these fields. Their inclusion here is a **PROPOSED hardening target**, not a claim of present implementation.

---

## Fixtures, tests, validators, and CI

### Confirmed fixture support

`fixtures/contracts/v1/policy/policy_decision/` documents:

- one minimal valid fixture;
- one invalid fixture missing `decision_id`;
- one broad expected-error matcher;
- the common schema harness discovery convention.

This is useful but insufficient for active policy assurance.

### Required negative cases

Before promotion, tests should reject or route safely when:

- outcome is outside the accepted finite set;
- policy family is unknown;
- decision ID violates its pattern;
- evaluation time is malformed or missing;
- unknown properties are present in a closed schema;
- reasons or obligations have invalid types;
- a decision lacks policy/bundle version;
- an input bundle lacks subject, resource, action, or purpose context;
- sensitivity is absent, unsupported, or improperly downgraded;
- consent or rights are required but unresolved;
- promotion is treated as release approval;
- redaction placeholder is treated as an emitted receipt;
- policy record is used as EvidenceBundle;
- stale or superseded decision is reused;
- public output bypasses release, correction, or rollback controls.

### Current validation boundary

| Validation surface | Current status |
|---|---|
| Common schema harness | Discovers top-level `schemas/contracts/v1/policy/*.schema.json` with matching fixture families. |
| PolicyDecision fixtures | Minimal valid/invalid family confirmed. |
| Dedicated `validate_policy_decision.py` | Absent at checked path. |
| Policy runtime execution | UNKNOWN. |
| Registry activation | UNKNOWN. |
| Consumer integration | UNKNOWN. |
| CI pass for this future PR | Must be observed after PR creation. |

A repository-wide schema-validation success would prove only the checks actually wired into that workflow. It would not prove policy correctness, policy runtime execution, complete negative coverage, release readiness, or public safety.

---

## Governed migration sequence

### Phase 0 — Freeze

- Keep this path README-only.
- Deny new schema files, `$ref` targets, consumers, or registry entries here.
- Record emergency exceptions with owner, reason, expiry, and rollback.

### Phase 1 — Inventory

- Recursively enumerate every file under the compatibility path.
- Enumerate inbound links, `$ref` uses, imports, registry records, generated outputs, and documentation references.
- Record hashes, authorship/provenance, generated/manual status, and last-known consumers.

### Phase 2 — Classify

For each artifact, determine:

- object identity;
- semantic contract;
- owning responsibility root;
- canonical schema family;
- sensitivity and release impact;
- whether it is schema, placeholder, example, policy code, receipt, record, or documentation.

### Phase 3 — Resolve conflicts

- Decide PolicyDecision versus runtime envelope boundaries.
- Decide PromotionDecision policy versus governance/release ownership.
- Decide RedactionReceipt schema and emitted-receipt ownership.
- Select `$id`, filename, fixture-root, validator, and registry conventions.
- Record ADR, drift, or migration decisions before file movement.

### Phase 4 — Harden canonical schemas

- Pair every schema with semantic contract.
- Replace permissive scaffolds with reviewed fields or explicitly retain stub status.
- Close objects where appropriate.
- Define versioning, supersession, compatibility, and correction semantics.
- Add valid, invalid, edge, deny, abstain, error, sensitivity, consent, and release-blocked fixtures.

### Phase 5 — Implement proof

- Add or repair validators.
- Register validators in accepted runner/control plane.
- Add fixture-driven tests and consumer contract tests.
- Exercise negative and fail-closed behavior.
- Verify no policy schema creates policy or release authority.

### Phase 6 — Migrate consumers

- Update `$ref`s, imports, registry records, docs, generated artifacts, and API/runtime bindings.
- Provide compatibility mapping and deprecation window.
- Verify old and new behavior against golden fixtures.
- Record receipts for generated migration outputs where required.

### Phase 7 — Retire

Retire this compatibility path only after:

- recursive inventory is complete;
- no machine schemas remain;
- inbound consumers and links are migrated;
- redirect/index needs are resolved;
- correction and rollback plans are tested;
- steward approval is recorded.

### Stop conditions

Stop migration when:

- object ownership is disputed;
- unique content cannot be preserved;
- consumers are unknown;
- `$id` or `$ref` migration is ambiguous;
- policy/governance/release boundaries are unresolved;
- fixtures or validators cannot prove compatibility;
- sensitivity, consent, rights, or release effects are unclear;
- rollback cannot restore the prior state.

---

## Finite status model

### Compatibility-path status

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | Documentation and pointers only. |
| `FROZEN` | No new schemas, consumers, or registry activations. |
| `INVENTORY_REQUIRED` | Recursive file and inbound-reference inventory is incomplete. |
| `OBJECT_ROUTING_REQUIRED` | Artifacts need owner and canonical-family classification. |
| `TRANSITIONAL` | Migration is approved and actively tracked. |
| `DEPRECATED` | No new consumers; compatibility references remain temporarily. |
| `RETIREMENT_READY` | Inventory, migration, tests, review, correction, and rollback are complete. |
| `RETIRED` | Path removed or retained only as an approved redirect/index. |
| `BLOCKED` | Conflict, rights, sensitivity, consumer, proof, or rollback gap prevents change. |

Current status:

```text
INDEX_ONLY + FROZEN + INVENTORY_REQUIRED + OBJECT_ROUTING_REQUIRED
```

### Schema maturity status

| Status | Meaning |
|---|---|
| `PLACEHOLDER` | Not a machine schema or intentionally non-enforcing placeholder. |
| `STUB` | Schema exists but is permissive or field-incomplete. |
| `DRAFT_SCHEMA` | Meaningful constraints exist; review and proof remain incomplete. |
| `ACTIVE_SCHEMA` | Accepted contract pairing, registry, validators, fixtures, tests, consumers, and review exist. |
| `SUPERSEDED` | Replaced by a newer accepted schema with migration mapping. |
| `DEPRECATED` | No new consumers; compatibility period remains. |
| `RETIRED` | Consumers and references are removed or redirected. |
| `CONFLICTED` | Ownership, identity, or compatibility is unresolved. |

---

## Minimal compatibility note

```markdown
# <policy-schema-compatibility-note-id>

## Status
INDEX_ONLY / FROZEN / INVENTORY_REQUIRED / OBJECT_ROUTING_REQUIRED / TRANSITIONAL / DEPRECATED / RETIREMENT_READY / RETIRED / BLOCKED

## Compatibility path
<schemas/contracts/policy/...>

## Object identity
<PolicyDecision / PolicyInputBundle / SensitivityLabel / PromotionDecision / RedactionReceipt / other / UNKNOWN>

## Canonical schema candidate
<schemas/contracts/v1/... or NEEDS VERIFICATION>

## Paired contract
<contracts/... or NEEDS VERIFICATION>

## Policy authority
<policy/... or N/A>

## Fixtures and tests
<paths or NEEDS VERIFICATION>

## Validator and registry
<paths/records or NEEDS VERIFICATION>

## Consumers
<verified consumers or UNKNOWN>

## Migration and rollback
<migration record and rollback target or BLOCKED>

## Evidence
<repository evidence supporting each claim>
```

---

## Definition of done

This compatibility README is complete when:

- [x] unversioned path is classified as compatibility-only;
- [x] versioned policy family is identified;
- [x] current mixed schema maturity is disclosed;
- [x] policy, governance, release, sensitivity, redaction, fixture, validator, and receipt boundaries are explicit;
- [x] no new canonical schema is authorized here;
- [x] migration is object-by-object and reversible;
- [ ] recursive compatibility-path inventory is complete;
- [ ] inbound links and consumers are inventoried;
- [ ] canonical object ownership decisions are accepted;
- [ ] `$id`, filename, fixture, validator, and registry conventions are accepted;
- [ ] canonical schemas are hardened or explicitly retained as stubs;
- [ ] validators and negative tests are implemented;
- [ ] consumer migration and compatibility window are verified;
- [ ] correction and rollback are exercised;
- [ ] retirement decision is recorded.

---

## Validation

### Documentation checks

For this README update:

- one rendered H1;
- no heading-level jumps outside fenced examples;
- balanced fenced blocks;
- unique rendered headings;
- internal navigation anchors resolve;
- no trailing whitespace;
- no credential or private-key material;
- one-file remote diff;
- exact remote blob readback.

### Repository checks

Relevant commands for a future implementation-capable environment include:

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
python tools/validators/validate_policy_decision.py --fixtures
```

The second command is currently **not runnable at the checked path** because the declared validator file was not found. Do not document it as operational until implementation and wiring are verified.

Schema tests alone remain insufficient for policy promotion. Add policy-runtime, consumer, sensitivity, consent, release, correction, and rollback tests appropriate to the affected objects.

---

## Correction, deprecation, and rollback

### Documentation correction

If this README contains an incorrect claim:

1. identify the exact claim and evidence conflict;
2. label the correction;
3. update the evidence snapshot;
4. preserve prior history through a normal commit;
5. record downstream documentation or migration effects.

### Pre-merge rollback

Leave the draft PR unmerged or restore prior blob:

```text
aa0f01fe231ee73381180b3f29c248c2e172b7fd
```

### Post-merge rollback

Use a transparent revert commit or revert PR. Do not reset or rewrite shared history.

### Schema migration rollback

Any future schema migration must preserve:

- old and new `$id` mappings;
- old and new file paths;
- consumer inventory;
- registry states;
- fixture and validator versions;
- compatibility window;
- correction notices;
- rollback commit or migration identifier.

Rollback must restore behavior, references, and governed state—not merely copy a file back.

---

## Open verification backlog

### Placement and authority

- [ ] Confirm CODEOWNERS and actual stewards.
- [ ] Confirm ADR-0001 acceptance status or successor decision.
- [ ] Recursively inventory `schemas/contracts/policy/`.
- [ ] Confirm whether a parent `schemas/contracts/README.md` should index compatibility lanes.
- [ ] Record this path and its target in the drift register.
- [ ] Confirm retirement versus long-term redirect/index posture.

### Object identity and schemas

- [ ] Confirm PolicyDecision canonical contract and schema profile.
- [ ] Confirm PolicyInputBundle required semantic fields.
- [ ] Confirm SensitivityLabel transitions and obligations.
- [ ] Resolve PromotionDecision policy/governance/release ownership.
- [ ] Resolve RedactionReceipt schema, receipt, proof, and governance ownership.
- [ ] Normalize filenames and `$id` namespaces.
- [ ] Normalize fixture roots and metadata policy pointers.
- [ ] Verify cross-schema `$ref` compatibility.

### Proof and operation

- [ ] Implement or locate `validate_policy_decision.py`.
- [ ] Verify all policy schema validators and registry entries.
- [ ] Expand valid and invalid fixture coverage.
- [ ] Add deny, abstain, error, consent-gap, sensitivity-gap, stale, superseded, and release-blocked tests.
- [ ] Verify policy runtime consumes accepted schemas.
- [ ] Verify public clients receive governed outputs only.
- [ ] Verify emitted decisions, receipts, proofs, and release records use their owning roots.
- [ ] Verify CI actually executes each required check.
- [ ] Verify correction, supersession, cache invalidation, and rollback behavior.

### Consumers and migration

- [ ] Inventory `$ref`s, imports, registry activations, generated code, API bindings, and docs links.
- [ ] Define deprecation window and compatibility mapping.
- [ ] Migrate consumers in reversible increments.
- [ ] Verify no consumer depends on unversioned paths after migration.
- [ ] Record final retirement approval.

---

## Evidence basis

| Evidence | Status | Supports | Limitation |
|---|---|---|---|
| Previous `schemas/contracts/policy/README.md` | **CONFIRMED** | Prior compatibility intent and rollback blob. | Stale: said versioned family was unconfirmed. |
| `schemas/contracts/v1/policy/README.md` | **CONFIRMED** | Current inventory, mixed maturity, overlap, naming, namespace, and fixture-path drift. | Documentation does not prove activation. |
| `policy_decision.schema.json` | **CONFIRMED / PROPOSED** | Required fields, finite outcomes, policy families, date-time, closed shape, metadata pointers. | Does not prove policy execution or validator existence. |
| PolicyDecision fixture README | **CONFIRMED** | Minimal valid/invalid inventory and common-harness behavior. | Coverage is narrow; tests were not run in this documentation task. |
| `tests/schemas/test_common_contracts.py` | **CONFIRMED** | Top-level policy schema/fixture discovery behavior. | Does not prove semantic policy correctness or production use. |
| Checked validator path | **ABSENT** | Declared dedicated PolicyDecision validator is not implementation proof. | Another implementation could exist elsewhere; bounded absence only. |
| Directory Rules and ADR-0001 | **CONFIRMED doctrine/document** | Responsibility split and versioned schema-home direction. | ADR acceptance remains governed by its own status. |
| Bounded repository searches | **CONFIRMED bounded evidence** | Target and adjacent surfaces. | Not an exhaustive consumer graph or recursive inventory. |

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-15 |
| Evidence base | `main@21e44bb292afe8227a08b08b47683e581e92fc5b` |
| Prior blob | `aa0f01fe231ee73381180b3f29c248c2e172b7fd` |
| Current posture | `INDEX_ONLY + FROZEN + INVENTORY_REQUIRED + OBJECT_ROUTING_REQUIRED` |
| Next review trigger | Schema/ADR decision, policy-family migration, validator implementation, fixture/test expansion, registry activation, consumer migration, correction, rollback, or retirement decision |
