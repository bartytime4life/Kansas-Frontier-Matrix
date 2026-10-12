<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-governance-readme
title: schemas/governance/ — Governance Schema Compatibility Guardrail
type: README
version: v0.3
status: draft; repository-grounded; root-level-compatibility-lane; two-permissive-PROPOSED-scaffolds; canonical-family-expanded; index-drift-visible; migration-and-retirement-HOLD; non-authoritative; non-enforcing
owner: NEEDS VERIFICATION — CODEOWNERS routes /schemas/ to @bartytime4life, but routing is not accepted stewardship, separation of duties, or independent approval
created: 2026-08-13
updated: 2026-08-13
policy_label: public
owning_root: schemas/
current_path: schemas/governance/README.md
responsibility: Preserve two historical root-level governance schema scaffolds as visible, frozen compatibility lineage while routing new machine-shape work to reviewed versioned object families and holding migration or retirement until consumer, identity, policy, validation, and rollback evidence closes.
truth_posture: CONFIRMED pinned repository bytes and bounded tracked-reference census; PROPOSED or UNKNOWN object maturity, consumers, ownership, destinations, and external reliance; HOLD on activation, migration, redirect, or retirement
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix main@98b28dc94057e29b7f79cedfd07fa81045d9f666; repository tree 531fe76a0bf5c081e594d0099b90bd4b9a0bec64; prior target blob 258ab127ad747c3be10820fc7c433c9f5cf1dfab; compatibility tree 2664193d814b02e183e983744cc5982a64027c94; versioned governance tree fdd6d6e3df3708ab4ac908af8b177342a2e72ffb; governance fixture tree a4ca23df7b543a4eef1c56e9a31e8b28846df887
related:
  - schemas/README.md
  - schemas/contracts/v1/governance/README.md
  - schemas/governance/overlay_pointer.schema.json
  - schemas/governance/consent_receipt.schema.json
  - contracts/governance/README.md
  - policy/consent/README.md
  - fixtures/contracts/v1/governance/README.md
  - tests/schemas/test_common_contracts.py
  - tests/validators/governance/
  - tools/validators/validate_review_record.py
  - tools/validators/validator_registry.json
  - .github/workflows/schema-validation.yml
  - .github/workflows/validator-suite.yml
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, schemas, governance, compatibility, consent-receipt, overlay-pointer, migration, validation, no-parallel-authority, cite-or-abstain]
notes:
  - "v0.3 reconciles the complete three-file compatibility tree, all 66 versioned governance schemas, 58 direct governance fixture directories, bounded tracked references, current validator wiring, and accepted placement authority."
  - "The versioned governance-family and governance-fixture READMEs lag their live subtrees; this README records the drift without rewriting those separate authorities."
  - "The two root-level schemas remain open, property-empty PROPOSED scaffolds with null contract pointers. This README does not activate, harden, migrate, redirect, or retire them."
  - "No schema, contract, policy, consent state, review state, fixture, validator, proof, receipt, release state, runtime, deployment, or publication behavior is changed by this README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/governance/` — Governance Schema Compatibility Guardrail

> **One-line purpose.** Preserve two historical root-level governance schema scaffolds as frozen, non-authoritative lineage while routing new machine-checkable governance shapes to reviewed versioned families.

<kbd>COMPATIBILITY LINEAGE</kbd> <kbd>2 OPEN PROPOSED SCAFFOLDS</kbd> <kbd>CANONICAL WRITES: VERSIONED FAMILY</kbd> <kbd>MIGRATION: HOLD</kbd>

> [!IMPORTANT]
> Do not add new canonical governance schemas here. Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules](../../docs/doctrine/directory-rules.md) bytes that assign machine shape to `schemas/` and default contract-backed schemas to `schemas/contracts/v1/<family>/`. The narrower [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) remains `proposed`; it is not needed to invent a second unversioned home.

> [!CAUTION]
> [`overlay_pointer.schema.json`](overlay_pointer.schema.json) and [`consent_receipt.schema.json`](consent_receipt.schema.json) accept any JSON object. Parse or meta-schema success proves only that the schema documents are structurally valid. It does not prove overlay meaning, consent, identity, authority, rights, sensitivity clearance, review, release, or public safety.

> [!WARNING]
> Consent- and People–DNA–Land-adjacent work is fail-closed. Do not place credentials, living-person data, raw DNA/genomic material, exact protected locations, private consent records, or operational decisions in this schema directory or its examples.

**Quick navigation:** [Purpose](#purpose) · [Status](#status-at-the-reviewed-snapshot) · [Authority](#authority-boundary) · [Map](#repository-fit) · [Scaffolds](#direct-scaffold-inventory) · [References](#observed-reference-inventory) · [Versioned family](#canonical-versioned-governance-family) · [Coverage](#fixture-validator-and-test-coverage) · [Compatibility](#compatibility-contract) · [Consumers](#consumer-rules) · [Validation](#validation-boundary) · [Migration](#migration-and-retirement-gates) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-and-rollback)

---

## Purpose

This README has five jobs:

1. keep the root-level path and its two schema identities visible as repository lineage;
2. prevent permissive placeholders from being mistaken for operational governance controls;
3. route new machine-shape work to the current versioned governance family or another reviewed versioned family selected by object meaning;
4. expose current references, coverage limits, index drift, and unresolved ownership without inventing maturity; and
5. define the evidence required to freeze, migrate, redirect, deprecate, or retire each scaffold safely.

This README does not select a final destination merely from a filename. `overlay_pointer` is UI, API, policy, authorization, and release adjacent. `consent_receipt` is consent, identity, rights, privacy, evidence, retention, revocation, audit, and release adjacent. Each object must be classified by meaning, lifecycle, writers, readers, sensitivity, and rollback needs before placement changes.

[Back to top](#top)

## Status at the reviewed snapshot

The statements below are pinned to `main@98b28dc94057e29b7f79cedfd07fa81045d9f666`.

| Surface | Current repository evidence | Truth label | Safe consequence |
|---|---|---|---|
| `schemas/governance/` | One README and two direct `*.schema.json` files; tree `2664193d814b02e183e983744cc5982a64027c94`. | **CONFIRMED** | This is a small compatibility lane, not the live governance-family inventory. |
| [`overlay_pointer.schema.json`](overlay_pointer.schema.json) | Draft 2020-12 object; empty `properties`; no `required`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; `contract_doc: null`. | **CONFIRMED PROPOSED SCAFFOLD** | It accepts any object and establishes no overlay or governance control. |
| [`consent_receipt.schema.json`](consent_receipt.schema.json) | Draft 2020-12 object; empty `properties`; no `required`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; `contract_doc: null`. | **CONFIRMED PROPOSED SCAFFOLD** | It accepts any object and establishes no consent, rights, privacy, revocation, or audit control. |
| [`schemas/contracts/v1/governance/`](../contracts/v1/governance/README.md) | 66 direct `*.schema.json` files plus its README; tree `fdd6d6e3df3708ab4ac908af8b177342a2e72ffb`. | **CONFIRMED MIXED MATURITY** | New governance-family shape work routes here by default, but each object still needs reviewed ownership and adjacent contracts/policy/tests. |
| Versioned governance-family README | Its v0.3 metadata and inventory still describe nine schemas. | **CONFIRMED INDEX DRIFT** | Use the live tree for the current census; repair that README in a separate scoped update. |
| Governance fixture subtree | 58 direct fixture directories; 57 names match current versioned schemas; tree `a4ca23df7b543a4eef1c56e9a31e8b28846df887`. | **CONFIRMED HETEROGENEOUS COVERAGE** | Directory presence alone does not prove common-harness polarity or dedicated-validator coverage. |
| Governance fixture README | Its v0.1 inventory still says only `review_record/` is populated. | **CONFIRMED INDEX DRIFT** | Do not use that prose as the current fixture census. |
| Exact root-path references | Two tracked documentation/policy files directly reference one or both root paths. No executable consumer surfaced in the bounded tracked scan. | **CONFIRMED BOUNDED OBSERVATION** | Preserve the paths; absence from this scan is not proof of zero generated, package, deployment, or external consumers. |
| Canonical destination for either root scaffold | No accepted per-object migration decision was verified. | **NEEDS VERIFICATION / HOLD** | Do not move, copy, redirect, repoint `$id`, or delete either schema. |
| Ownership and required review | CODEOWNERS routes `/schemas/` to `@bartytime4life`; no accepted schema steward, independent review, or ruleset significance was established. | **PARTIAL / NEEDS VERIFICATION** | Routing is not stewardship, approval, or separation-of-duties proof. |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Directly observed in pinned repository bytes, tree objects, workflow definitions, or an exact referenced run. |
| **PROPOSED** | Declared candidate or scaffold; not accepted, active, or operational. |
| **PROPOSED_INACTIVE** | Explicitly inactive candidate; shape or fixtures do not activate it. |
| **UNKNOWN** | The inspected evidence does not establish the answer. |
| **NEEDS VERIFICATION** | A concrete ownership, consumer, schema, policy, runtime, review, or migration check remains. |
| **CONFLICTED** | Current paths, indexes, proposed destinations, or authority surfaces disagree. |
| **HOLD** | Do not activate, migrate, redirect, retire, delete, release, or rely operationally until named gates close. |

A bounded non-observation is not proof of permanent absence. Recheck branches, packages, generated clients, deployments, external users, and downstream systems at the revision where a migration is proposed.

[Back to top](#top)

## Authority boundary

### Governing authority and inheritance

| Source | Status at the evidence snapshot | Effect here |
|---|---|---|
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Adopts the exact Directory Rules v2 bytes and their responsibility-root, README, no-parallel-authority, and migration discipline. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | **ADOPTED BY ADR-0029**; its pinned internal header remains part of the adopted bytes | Assigns machine-checkable shape to `schemas/` and defaults contract-backed schemas to `schemas/contracts/v1/<family>/`. |
| [`schemas/README.md`](../README.md) | **CURRENT ROOT CONTRACT** | Defines the parent machine-shape boundary, compatibility posture, validation interpretation, and non-effects. |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | **MACHINE PROJECTION ONLY** | Registers the schema responsibility root; it cannot accept a child path, migrate an object, or create authority. |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Describes a narrower canonical-home decision; it is design context, not accepted migration authority. |
| [ADR-0002](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **DRAFT source / effectively PROPOSED** | Describes the meaning/shape split; current practice and adopted Directory Rules provide the operative boundary. |

### Responsibility separation

| Responsibility | Owning surface | Rule for this lane |
|---|---|---|
| Machine-checkable governance shape | Reviewed versioned family, currently [`schemas/contracts/v1/governance/`](../contracts/v1/governance/README.md) by default | This unversioned lane must not become a parallel authoring authority. |
| Governance object meaning | [`contracts/governance/`](../../contracts/governance/README.md) or another reviewed semantic family | A title, filename, or `source_docs` pointer is not a semantic contract. |
| Human governance duties | `docs/governance/` plus accepted decisions | Schema text cannot appoint stewards, approve work, or prove separation of duties. |
| Consent, rights, sensitivity, access, and admissibility | `policy/` plus accepted policy contracts and evaluators | A consent-shaped schema does not issue or validate consent and cannot grant access. |
| Evidence and source authority | EvidenceRef/EvidenceBundle and source-governance lanes | Shape validity does not establish evidence closure, provenance, or source role. |
| Synthetic examples | [`fixtures/`](../../fixtures/README.md) | Fixtures are bounded test inputs, not records of real consent or governance action. |
| Validator implementation and executable proof | `tools/validators/` and `tests/` | A validator must declare exact inputs, outputs, failure behavior, and coverage. |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Process memory and proof remain distinct; neither belongs beside schemas. |
| Promotion, release, correction, withdrawal, rollback | [`release/`](../../release/README.md) | Governance-schema validity is not a lifecycle decision. |
| Runtime, API, MapLibre, UI, and AI behavior | Governed application, package, and API lanes | Public clients use governed APIs and released projections, not schema directories. |

### Local authority statement

This README may preserve compatibility facts, route contributors, record current inventory, and hold unsafe migration. It must not:

- accept or supersede an ADR;
- activate a schema, policy, validator, workflow, consumer, or gate;
- authenticate a person, consent grant, reviewer, steward, source, or decision;
- create release, correction, withdrawal, rollback, or publication authority;
- treat strict shape, fixtures, tests, or CI as proof that governance occurred;
- authorize moving, copying, redirecting, or deleting either root schema;
- convert an unresolved external-consumer question into a zero-consumer claim.

[Back to top](#top)

## Repository fit

Directory Rules requires a current directory map. This map shows this lane and direct children; it does not pretend to enumerate the 66-file versioned family.

```text
schemas/governance/
├── README.md                       # this compatibility and migration guardrail
├── consent_receipt.schema.json     # open, property-empty PROPOSED scaffold
└── overlay_pointer.schema.json     # open, property-empty PROPOSED scaffold
```

Adjacent responsibility lanes:

```text
schemas/contracts/v1/governance/   # default versioned governance machine-shape family
contracts/governance/              # governance object meaning
policy/consent/                    # proposed shared consent-policy boundary
fixtures/contracts/v1/governance/  # governance contract fixture material
tests/schemas/                     # common schema harness
tests/validators/governance/       # focused governance validator tests
tools/validators/                  # validator implementation and orchestration
data/receipts/                     # process memory; not schema authority
data/proofs/                       # proof closure; not schema authority
release/                           # release, correction, withdrawal, rollback authority
```

No machine mirror, redirect schema, alias map, or deprecation window is established for the root-level files.

[Back to top](#top)

## Direct scaffold inventory

| Declaration | `overlay_pointer.schema.json` | `consent_receipt.schema.json` |
|---|---|---|
| `$schema` | Draft 2020-12 | Draft 2020-12 |
| `$id` | `kfm://schemas/governance/overlay_pointer.schema.json` | `kfm://schemas/governance/consent_receipt.schema.json` |
| `type` | `object` | `object` |
| `properties` | Empty object | Empty object |
| `required` | Absent | Absent |
| `additionalProperties` | `true` | `true` |
| `x-kfm.status` | `PROPOSED` | `PROPOSED` |
| `x-kfm.contract_doc` | `null` | `null` |
| Git blob | `631f5aa39a137ebd449505f3362f5da547b384eb` | `a178b759fa19922f8d6c6adf1ec13402f9784e75` |

Both schemas accept `{}`, `{"unexpected": true}`, and any other JSON object. They reject only non-object JSON values at the schema-type layer. That is scaffold behavior, not a meaningful domain boundary.

### `overlay_pointer.schema.json`

The schema metadata names [`docs/domains/people-dna-land/sublanes/dna.md`](../../docs/domains/people-dna-land/sublanes/dna.md) as source lineage. That document directly labels both root schema homes `PROPOSED` and an open placement question.

The source pointer does not establish overlay identity, authorization, permitted precision, API/UI/MapLibre behavior, storage, caching, publication, semantic contract, fixtures, validator, consumer, release state, or rollback.

`overlay_pointer` may ultimately belong to a UI, runtime, map, domain, policy, governance, or release-adjacent family. This README does not choose.

### `consent_receipt.schema.json`

The schema metadata names [`API_CONTRACTS.md`](../../docs/domains/people-dna-land/API_CONTRACTS.md) and [`sublanes/dna.md`](../../docs/domains/people-dna-land/sublanes/dna.md) as lineage. [`policy/consent/README.md`](../../policy/consent/README.md) also links the root schema and classifies general consent shapes as placeholders.

A trustworthy consent receipt would need reviewed semantics and machine constraints for issuer, subject, holder, representative, authority, exact purpose and scope, issuance and expiry, revocation and supersession, provenance and integrity, retention and minimization, policy and evidence, audit, safe disclosure, release, correction, and rollback. It would also need valid, invalid, stale, revoked, and adversarial fixtures with executable checks.

None of those controls is enforced by this root scaffold. Separate bounded People–DNA–Land overlay and revocation-assessment profiles exist, but they use different contracts, schemas, fixtures, validators, tests, and workflows and explicitly do not issue consent, authenticate people, execute cleanup, approve release, or publish.

[Back to top](#top)

## Observed reference inventory

The bounded tracked-file scan searched exact root paths and exact root `$id` values outside this README and the two schema files.

| Reference surface | Observed relationship | Classification |
|---|---|---|
| [`docs/domains/people-dna-land/sublanes/dna.md`](../../docs/domains/people-dna-land/sublanes/dna.md) | Names both root schema paths and explicitly calls them `PROPOSED` with placement unresolved. | **CONFIRMED documentation reference** |
| [`policy/consent/README.md`](../../policy/consent/README.md) | Links `schemas/governance/consent_receipt.schema.json` and classifies general consent shapes as placeholders. | **CONFIRMED policy-documentation reference; not runtime use** |
| Root schema `x-kfm.source_docs` fields | Point to People–DNA–Land documentation as scaffold lineage. | **CONFIRMED metadata lineage; not consumer proof** |
| [`docs/domains/archaeology/CULTURAL_REVIEW.md`](../../docs/domains/archaeology/CULTURAL_REVIEW.md) | Proposes and links `schemas/contracts/v1/governance/consent_receipt.schema.json`, which is absent from the current versioned tree. | **CONFIRMED proposed-path drift; not a root-path consumer** |
| Executable code, tests, validators, workflows, or fixtures | No exact root path or `$id` reference surfaced in the bounded tracked scan. | **CONFIRMED non-observation; zero-consumer claim prohibited** |
| Generated clients, package releases, deployments, external repositories, bookmarks, or downstream systems | Not established by this repository scan. | **UNKNOWN** |

Migration work must expand this into a code-aware and deployment-aware inventory. Do not treat documentation-only references as safe to break, and do not treat the absence of an executable match as deletion authority.

[Back to top](#top)

## Canonical versioned governance family

### Current census

The live [`schemas/contracts/v1/governance/`](../contracts/v1/governance/README.md) tree contains 66 direct JSON Schemas. Its README still describes nine; the live tree is the current census, while the README remains the family navigation artifact pending its own reconciliation.

| Dimension | Pinned observation | Interpretation |
|---|---:|---|
| Direct `*.schema.json` files | 66 | Complete direct-file census at the pinned tree, not an acceptance count. |
| Draft 2020-12 declarations | 66 | Declared dialect; the unchanged tree passed the most recent observed schema-workflow meta-schema preflight. |
| Unique `$id` values within the family | 66 | Unique at this snapshot; namespace consistency remains a separate review question. |
| `additionalProperties: false` | 63 | Closed top-level shape does not establish semantic or operational maturity. |
| `additionalProperties: true` | 3 | `promotion_decision`, `redaction_receipt`, and `steward_assignment`. |
| Empty `properties` | 2 | `promotion_decision` and `redaction_receipt`; both are `PROPOSED` with null contract pointers. |
| `x-kfm.status: PROPOSED` | 16 | Declared proposed, not active. |
| `x-kfm.status: PROPOSED_INACTIVE` | 12 | Explicitly inactive. |
| `x-kfm.status: PROPOSED_FIXTURE_PROFILE` | 1 | Fixture-profile candidate only. |
| No `x-kfm.status` | 37 | Status absence must not be interpreted as acceptance. |
| Non-null `x-kfm.contract_doc` | 25 | A pointer is not proof that the target exists, matches case, or is accepted. |
| Null `x-kfm.contract_doc` | 2 | `promotion_decision` and `redaction_receipt`. |
| No `x-kfm.contract_doc` member | 39 | Pairing and semantic ownership remain object-specific. |
| Observed `$id` base forms | 8 | Identity namespace convergence requires a reviewed migration, not bulk rewriting. |

### Complete status-group inventory

<details>
<summary><strong>PROPOSED — 16 schemas</strong></summary>

`briefing_signal`, `ci_outcome`, `cross_domain_seam_register`, `governed_run_chain`, `object_family_register`, `path_alias_register`, `path_decision_record`, `promotion_decision`, `quarantine_record`, `redaction_receipt`, `repository_control_context`, `repository_control_state`, `repository_transition_authorization`, `review_record`, `root_registry`, `steward_assignment`

</details>

<details>
<summary><strong>PROPOSED_INACTIVE — 12 schemas</strong></summary>

`attested_compute_boundary_assessment`, `gate_outcome_mapping`, `gate_override_record`, `governance_event`, `graph_migration_declaration`, `graph_temporal_diff_query_profile`, `k_anonymity_assessment`, `program_outcome_chain`, `published_language_review`, `review_authority_binding`, `sensitive_overlay_gatehouse_preflight`, `temporal_retention_disposition_assessment`

</details>

<details>
<summary><strong>PROPOSED_FIXTURE_PROFILE — 1 schema</strong></summary>

`sensitive_overlay_reveal_expiry`

</details>

<details>
<summary><strong>No <code>x-kfm.status</code> — 37 schemas</strong></summary>

`agent_operation_envelope`, `aggregate_boundary_assessment`, `ai_change_proposal`, `atlas_card_delta_assessment`, `automation_pr_proposal`, `coverage_priority_scorecard`, `dependency_origin_policy`, `domain_context_map_assessment`, `domain_lane_register`, `drift_register_triage_assessment`, `evidence_resolution_record`, `github_issue_inventory_read`, `governance_health_projection`, `implementation_change_context`, `implementation_decision_record`, `inspectable_claim_carrier_assessment`, `issue_inventory_projection`, `lifecycle_gate_closure_assessment`, `model_card_envelope`, `negative_state_audit`, `object_family_domain_reference_profile`, `object_identity_kind_assessment`, `open_adr_backlog_discipline_assessment`, `proof_session_handoff`, `public_participation_submission_assessment`, `query_run_record`, `receipt_catalog_assessment`, `receipt_proof_pairing_assessment`, `recommendation_decision_authority_assessment`, `recompile_manifest`, `responsibility_layer_impact_assessment`, `sensitive_location_parity_assessment`, `sensitive_release_review_closure`, `temporal_query_disclosure`, `terminal_state_assessment`, `verification_backlog_item`, `verification_convergence_plan`

</details>

This grouping reports only literal metadata. It does not infer that status-absent schemas are accepted, active, required, release-bearing, or safe for public use.

[Back to top](#top)

## Fixture, validator, and test coverage

### Fixture topology

The current governance fixture subtree has 58 direct directories:

- 57 names match a current versioned governance schema;
- one directory, `implementation_review_packet`, has no same-named versioned governance schema;
- nine versioned governance schemas have no same-named fixture directory: `ci_outcome`, `domain_lane_register`, `promotion_decision`, `quarantine_record`, `redaction_receipt`, `repository_control_context`, `repository_control_state`, `repository_transition_authorization`, and `steward_assignment`.

The common harness in [`tests/schemas/test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) discovers a governance case whenever a same-named fixture directory exists. It then reads only:

```text
valid/valid_*.json
invalid/invalid_*.json
invalid/invalid_*.expected_error.txt
```

Only four governance directories currently use those exact positive/negative patterns:

| Common-harness family | Valid JSON files | Invalid JSON files |
|---|---:|---:|
| `ai_change_proposal` | 3 | 1 |
| `automation_pr_proposal` | 2 | 2 |
| `briefing_signal` | 6 | 5 |
| `review_record` | 2 | 3 |
| **Total** | **13** | **11** |

The other 53 matching directories use different layouts such as `cases.json`, direct `valid.json`, manifests, or family-specific files. They contribute zero files to the common harness's `valid_*.json` and `invalid_*.json` loops. Some are exercised by dedicated validators and tests; directory presence alone does not establish that mapping.

### Validator and test topology

- `tests/validators/governance/` contains 42 direct `test_*.py` modules.
- [`validate_review_record.py`](../../tools/validators/validate_review_record.py) is a 498-line fixture-only promotion-Gate-G projection validator at the pinned blob, not the short stub described by v0.2.
- The aggregate [`validator_registry.json`](../../tools/validators/validator_registry.json) full profile selects eight fixture-backed object validators plus `workflow-security` and `repository-topology`; none of the eight object validators targets the two root scaffolds.
- The root `overlay_pointer` and `consent_receipt` names have no matching governance fixture family and no dedicated exact-path validator or test surfaced in the bounded scan.

These counts show repository activity, not complete coverage. A coverage manifest mapping every schema to contract, fixture polarity, validator, test, producer, consumer, and maturity record remains **NEEDS VERIFICATION**.

[Back to top](#top)

## Compatibility contract

| Rule | Requirement |
|---|---|
| Freeze canonical growth | Do not add canonical fields, definitions, or new schema families under `schemas/governance/`. |
| Do not create new consumers | New code, validators, APIs, generators, pipelines, or UI features must not bind to these root paths or `$id` values as canonical contracts. |
| Preserve current references | Inventory and migrate every path, fragment, `$id`, generated, package, deployment, and external consumer before breaking compatibility. |
| Keep one writable authority | Do not copy a scaffold into a versioned family and continue editing both. |
| Do not silently repoint | A replacement path or `$id` requires explicit identity mapping, compatibility behavior, a bounded window, correction handling, and rollback. |
| Classify by responsibility | Choose a destination from object meaning, lifecycle, writers, readers, policy coupling, sensitivity, and release role—not filename or topic. |
| Establish meaning before maturity | Link an accepted semantic contract and relevant policy boundary before claiming an operational schema. |
| Treat permissiveness as a blocker | Empty `properties` plus `additionalProperties: true` is scaffold evidence, not useful validation. |
| Fail closed on sensitive use | Quarantine, deny, redact, generalize, restrict, or abstain when consent, living-person, DNA/genomic, cultural, location, rights, or authority evidence is unresolved. |
| Preserve lineage | Record old path, old `$id`, source lineage, decision, consumers, validators, migration result, correction path, and rollback target. |

A compatibility README may be more explicit than a scaffold, but it cannot grant the scaffold semantic, policy, runtime, review, release, or publication authority.

[Back to top](#top)

## Consumer rules

### New consumers

Do not use either root scaffold as a production contract, policy input guarantee, consent check, authorization gate, audit proof, release gate, API promise, UI guarantee, or public-data permission.

New machine-shape work must begin with the semantic object family and select a reviewed versioned schema home. If the object crosses governance, consent, UI, runtime, map, evidence, receipt, or release boundaries, document those references rather than collapsing the object into this directory.

### Existing consumers

If a consumer is found:

1. pin the consumer revision and owner;
2. classify whether it links, parses, validates, generates code, emits records, stores state, gates behavior, or exposes data;
3. record the path and `$id` dependency separately;
4. identify sensitive fields, policy dependencies, release coupling, and correction obligations;
5. preserve current behavior until a reviewed replacement and compatibility test exist;
6. test old and proposed identities during the bounded compatibility period; and
7. retain a reversible mapping until downstream and external parity are proven.

### Validators and CI

Report only what each check proves:

- JSON parse proves syntax;
- meta-schema validation proves the schema document conforms to its declared dialect;
- instance validation proves only the tested payload and schema revision;
- fixture polarity proves only the reviewed examples;
- a dedicated validator proves only its declared inputs, checks, and outcomes;
- CI success proves the exact workflow revision and commit reached a green terminal state.

None of those results proves semantic truth, authentic consent, current authority, policy approval, rights or sensitivity clearance, review completion, release readiness, or publication safety.

### Runtime and public clients

Standard clients use governed APIs and released projections. They must not read schema directories as runtime stores or interpret path presence as permission to expose consent state, People–DNA–Land material, overlay details, exact locations, reviewer identity, or internal governance state.

[Back to top](#top)

## What belongs here

- This compatibility README.
- The two existing root-level PROPOSED scaffolds while disposition, ownership, identity, and consumers remain unresolved.
- Minimal, reviewed deprecation or redirect metadata only as part of an accepted migration.
- Links to the chosen semantic contract, versioned schema, migration record, validation evidence, and rollback plan.

## What does not belong here

- New canonical governance schemas, schema versions, or object-family definitions.
- Semantic contracts, governance doctrine, policy rules, consent policy, privacy rules, rights decisions, or sensitivity decisions.
- Real consent receipts, review records, steward assignments, evidence records, proof objects, audit logs, policy decisions, promotion decisions, or release records.
- Fixtures, validator implementation, executable tests, generators, pipelines, APIs, runtime code, UI code, MapLibre configuration, or emitted artifacts.
- Secrets, credentials, private identifiers, living-person data, DNA/genomic data, protected cultural material, exact sensitive locations, or operational records.
- Claims that schema validity establishes truth, evidence closure, consent, authority, approval, compliance, review, release, or publication.

[Back to top](#top)

## Exposure, mutation, retention, and storage

| Dimension | Current posture |
|---|---|
| Exposure | Public repository machine-shape scaffolds and documentation only. No real sensitive payloads belong here. |
| Mutation | README corrections are reviewable; root schema mutation is held pending object-family, contract, policy, fixture, validator, consumer, and migration review. |
| Retention | Preserve both scaffolds until accepted disposition and reference/consumer closure exist. No retirement date is established. |
| Generation | Hand-maintained files; no canonical generator or mirror process was established. |
| Runtime use | Not established. Bounded tracked scan found documentation references but no exact executable consumer. |
| Authority | Inherited from the `schemas/` responsibility root and accepted placement doctrine; this child README and the root registry do not create authority. |

[Back to top](#top)

## Validation boundary

### Documentation checks

```bash
python tools/validators/docs/link-check/check_links.py schemas/governance/README.md

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required schemas/governance/README.md

python tools/validators/docs/document-graph/check_document_graph.py \
  --entrypoint schemas/governance/README.md schemas/governance/README.md

python tools/validators/docs/stale-scan/check_stale_docs.py \
  --as-of 2026-08-13 --profile bounded-required schemas/governance/README.md
```

These commands test documentation structure, local references, metadata, graph relationships, and freshness. They do not validate governance or consent semantics.

### Local structural checks

```bash
find schemas/governance -maxdepth 1 -type f -print | LC_ALL=C sort

python -m json.tool schemas/governance/overlay_pointer.schema.json >/dev/null
python -m json.tool schemas/governance/consent_receipt.schema.json >/dev/null

python - <<'PY'
import json
from pathlib import Path

from jsonschema import Draft202012Validator

for path in sorted(Path("schemas/governance").glob("*.schema.json")):
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    assert schema["type"] == "object"
    assert schema["properties"] == {}
    assert schema["additionalProperties"] is True
    assert schema["x-kfm"]["status"] == "PROPOSED"
    assert schema["x-kfm"]["contract_doc"] is None
    print(f"confirmed open PROPOSED scaffold: {path}")
PY

python -m pytest -q tests/schemas/test_common_contracts.py
```

The common pytest harness covers only versioned schemas with same-named fixture directories and expected file layouts. It does not instance-test the two root scaffolds.

### Current workflow boundary

The current [`schema-validation.yml`](../../.github/workflows/schema-validation.yml):

- parses every JSON file under `schemas/`;
- meta-schema checks every `*.schema.json` file under `schemas/`, including the two root scaffolds;
- separately requires every canonical `schemas/contracts/v1/**/*.schema.json` file to declare Draft 2020-12 and a unique `$id`;
- requires non-empty valid and invalid lanes plus rejection expectations for eight configured aggregate object validators;
- runs the ten-entry full validator profile through `make schemas`; and
- runs `tests/schemas` and `tests/contracts` only if the aggregate step succeeds.

The eight configured object validators target source, evidence, data/layer, and runtime families—not either root governance scaffold. The full profile adds workflow-security and repository-topology guardrails. Workflow success would therefore prove broad configured checks, not operational overlay or consent behavior.

### Most recent observed unchanged-tree evidence

The current governance trees and `schema-validation.yml` bytes are identical to those tested on PR #2752 head `f51f0a80ca320322605a6c251d345c099f0c0628`.

| Surface | Observed result | Correct interpretation |
|---|---|---|
| [`schema-validation` run 31757913816](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31757913816) | Preflight **PASS**: 874 schema-root JSON files parsed, 865 schemas passed Draft 2020-12 meta-schema checks, 855 canonical-v1 schemas had unique IDs, and eight configured validators had 27 valid plus 41 invalid fixtures. Aggregate step **FAIL** at `repository-topology`; downstream schema/contract pytest was skipped. | Supports the unchanged schema trees and workflow preflight only. It is not a green current-main or proposed-branch run and does not prove either root scaffold is operational. |
| `main@98b28dc…` workflow association | No direct workflow run was returned for the merge commit during this review. | Exact proposed-branch checks remain required. |
| Required-check and independent-review significance | Not established from workflow definitions or CODEOWNERS. | **UNKNOWN / NEEDS VERIFICATION** before relying on CI as a governance gate. |

### Negative assertions

Review must fail or hold if a change:

- adds canonical fields or another schema to this root-level lane;
- creates a new root-path or `$id` consumer;
- treats either open scaffold as a consent, policy, review, or release control;
- copies a definition while leaving two writable authorities;
- changes `$id`, path, family, strictness, or semantics without compatibility and rollback evidence;
- hides status absence, placeholder maturity, fixture-layout gaps, index drift, or skipped tests;
- uses `|| true`, empty loops, missing dependencies, or a partially completed workflow as conformance proof;
- exposes sensitive data or harmful precision in examples, diagnostics, receipts, or public surfaces;
- deletes or redirects a path on a bounded non-observation of consumers.

[Back to top](#top)

## Contributor workflow

### Documentation-only correction

1. Pin default-branch commit, target blob, direct tree, governing bytes, and open overlap.
2. Read the complete README and both root schemas.
3. Recompute versioned schema, fixture, validator, test, and exact-reference inventories.
4. Separate accepted placement authority from proposed ADRs and stale indexes.
5. Preserve every compatibility, sensitivity, consumer, migration, correction, and rollback hold.
6. Run fail-closed documentation and scaffold checks.
7. Submit the README and its required generated provenance receipt as one review boundary.

### Proposed schema or migration change

Stop and prepare a complete per-object change packet:

- accepted placement or migration authority;
- semantic contract and stable object identity;
- canonical path and `$id` mapping;
- current and proposed writers, readers, generators, packages, deployments, and external consumers;
- strict versioned schema and compatibility policy;
- valid, invalid, boundary, stale, revoked, adversarial, and sensitive-data-safe fixtures as applicable;
- deterministic validator and fail-closed tests;
- policy, consent, rights, privacy, sensitivity, retention, and audit review as applicable;
- release, correction, withdrawal, dependency invalidation, deprecation, and rollback plan;
- exact-head CI and independent approval evidence.

Do not bulk-move by filename and do not use this README update as migration authority.

[Back to top](#top)

## Review burden for any schema change

| Change class | Minimum review burden |
|---|---|
| README-only inventory or routing correction | Documentation reviewer plus schema-aware maintainer. |
| Compatibility status, alias, consumer, target, expiry, or exit-criteria change | Schema steward, architecture/docs reviewer, affected consumers, and migration owner. |
| Canonical governance schema addition or field change | Contract/schema owner, validator/test owner, producers, consumers, and affected policy or lifecycle reviewers. |
| Consent, living-person, DNA/genomic, sovereignty, rights, privacy, sensitivity, redaction, or location coupling | Policy and security/privacy reviewers plus affected domain, evidence, and release owners. |
| `$id`, filename, family, path, strictness, or version change | Identity/compatibility review, producer-consumer parity, migration record, correction plan, and rollback evidence. |
| Activation, promotion, release, publication, tombstone, redirect, retirement, or deletion | Accepted lifecycle authority, independent review, complete consumer closure, exact-head checks, and reversible transition evidence. |

Escalate conflicts to the owning responsibility roots and accepted governance process. When sources disagree, prefer accepted ADRs and adopted bytes, then exact current repository behavior, then proposed design records and stale indexes—with uncertainty kept visible.

[Back to top](#top)

## Migration and retirement gates

Migration is a governed compatibility transition, not a file move. Complete applicable gates separately for `overlay_pointer` and `consent_receipt`:

- [ ] Assign accountable schema, semantic-contract, policy, privacy/rights, domain, validation, consumer, and release reviewers.
- [ ] Produce complete repository, package, generated-client, deployment, and external path/`$id` consumer inventories.
- [ ] Decide object meaning and responsibility family without relying on topic or filename.
- [ ] Record accepted path disposition, canonical identity, and compatibility behavior.
- [ ] Establish the semantic contract, policy/sensitivity boundary, and lifecycle posture.
- [ ] Define a non-permissive versioned schema with explicit maturity and versioning.
- [ ] Add public-safe positive, negative, boundary, stale, revoked, and adversarial examples as applicable.
- [ ] Add deterministic validator and fail-closed test coverage with a schema-to-coverage map.
- [ ] Verify every producer, reader, generator, runtime, package, and deployed consumer.
- [ ] Define old-path and old-`$id` behavior, compatibility window, correction, withdrawal, and rollback.
- [ ] Migrate without maintaining divergent writable definitions.
- [ ] Prove zero writers and appropriate zero consumers before tombstone or physical deletion.
- [ ] Record the completed transition in an accepted migration, deprecation, or retirement artifact.

Until all applicable gates pass, keep both root schemas visible, frozen, and `PROPOSED`; migration and retirement remain **HOLD**.

[Back to top](#top)

## Definition of done

### This README revision

- [x] Preserves the lane as non-authoritative compatibility guidance.
- [x] Reconciles the exact three-file tree and both root schema declarations.
- [x] Replaces stale canonical-family and fixture-family counts with pinned live censuses.
- [x] Distinguishes directory presence, common-harness polarity, dedicated tests, and aggregate-validator wiring.
- [x] Records bounded tracked references without claiming complete downstream consumer closure.
- [x] Separates schema shape from contracts, policy, consent, evidence, fixtures, validators, receipts, proofs, governance action, and release authority.
- [x] Corrects the stale workflow and `validate_review_record.py` descriptions.
- [x] Preserves migration, sensitivity, correction, retirement, and rollback holds.

### Executable or migration maturity

- [ ] Accepted owners and independent reviewers are assigned.
- [ ] Complete internal and external consumer inventories exist.
- [ ] Final responsibility families and canonical identities are accepted.
- [ ] Semantic contracts and policy boundaries are accepted.
- [ ] Non-permissive schemas, representative fixtures, validators, and tests exist.
- [ ] Consent revocation, withdrawal, retention, correction, and sensitive-data controls are proven where applicable.
- [ ] Compatibility, deprecation, correction, and rollback plans are exercised.
- [ ] Exact-head required checks and review controls are verified.
- [ ] Current evidence supports migration, redirect, tombstone, retirement, or deletion.

Completing this README completes no executable, consent, governance, policy, release, migration, deployment, or publication gate.

[Back to top](#top)

## Open verification register

| ID | Question or gap | Status | Closure evidence required |
|---|---|---|---|
| SG-001 | Who owns this compatibility lane and the versioned governance family? | **NEEDS VERIFICATION** | Accepted stewardship and review assignment; CODEOWNERS alone is insufficient. |
| SG-002 | Should this lane remain frozen, become a tombstone, redirect, or retire? | **HOLD** | Accepted disposition, complete consumers, exit criteria, correction, and rollback. |
| SG-003 | Are there generated, package, deployed, or external root path/`$id` consumers? | **UNKNOWN** | Code-aware, package, deployment, and external-consumer inventory. |
| SG-004 | What is the semantic object family and final identity for `overlay_pointer`? | **NEEDS VERIFICATION** | Contract, UI/API/map/policy boundary, writers/readers, schema, fixtures, and placement decision. |
| SG-005 | What is the semantic object family and final identity for `consent_receipt`? | **NEEDS VERIFICATION** | Consent authority, purpose/scope, identity, rights/privacy, lifecycle, revocation, audit, schema, and placement decision. |
| SG-006 | Do either root scaffold have valid/invalid fixtures or dedicated runtime consumers under another name? | **NEEDS VERIFICATION** | Exact schema-to-fixture-validator-test-consumer crosswalk. |
| SG-007 | When will the versioned governance-family README be reconciled from nine to the live 66-schema tree? | **DRIFT / NEEDS VERIFICATION** | Separate same-path update with complete current inventory. |
| SG-008 | When will the governance-fixture README be reconciled from one populated family to the live 58-directory tree? | **DRIFT / NEEDS VERIFICATION** | Separate same-path update with layout-aware coverage map. |
| SG-009 | What maturity applies to the 37 versioned schemas without `x-kfm.status`? | **NEEDS VERIFICATION** | Accepted per-object maturity records; no inference from strictness or path presence. |
| SG-010 | What `$id` namespace convention should govern the eight observed base forms? | **NEEDS VERIFICATION** | Accepted identity convention plus backward-compatibility and consumer impact plan. |
| SG-011 | Which of the 58 fixture directories are covered by common versus dedicated validators and tests? | **NEEDS VERIFICATION** | Generated or reviewed coverage manifest with non-vacuous polarity. |
| SG-012 | Should `implementation_review_packet` gain a schema, move, or be reclassified? | **NEEDS VERIFICATION** | Object classification, current consumers, canonical identity, and migration decision. |
| SG-013 | How should archaeology's absent proposed canonical `consent_receipt` path references be corrected? | **CONFLICTED / NEEDS VERIFICATION** | Object-family and path decision before link or content repair. |
| SG-014 | Is `schema-validation` required, and when will inherited repository-topology rejection close? | **NEEDS VERIFICATION** | Exact-head green run, baseline correction review, and ruleset significance evidence. |
| SG-015 | Are independent approval and separation-of-duties controls enforced for governance schema changes? | **UNKNOWN** | Ruleset, branch protection, review, and steward-identity evidence. |

[Back to top](#top)

## Review checklist

- [ ] Default branch, target blob, direct tree, and open overlap were pinned.
- [ ] Both root schemas and every current direct child were inspected.
- [ ] Accepted ADR-0029 was separated from proposed ADR-0001 and draft/effectively proposed ADR-0002.
- [ ] Root-registry projection was not treated as decision authority.
- [ ] The 66-schema versioned census and 58-directory fixture census were recomputed.
- [ ] Status absence, inactive profiles, open scaffolds, and index drift remain explicit.
- [ ] Common-harness patterns were separated from dedicated-validator coverage.
- [ ] Root references were inventoried without claiming complete external closure.
- [ ] Contracts, schemas, policy, fixtures, validators, tests, receipts, proofs, decisions, release, and publication remain separate.
- [ ] Commands are fail-closed and contain no `|| true` escape.
- [ ] Baseline CI failure is disclosed and not attributed to this README change.
- [ ] Sensitive-data and consent claims remain within the evidence.
- [ ] Migration, correction, rollback, and retirement holds are explicit.
- [ ] Local links, metadata, graph, freshness, Markdown, schema, and receipt checks pass for the proposed artifact set.

[Back to top](#top)

## No-loss ledger

| v0.2 content | v0.3 disposition |
|---|---|
| Compatibility purpose and non-canonical routing | Preserved and grounded in accepted ADR-0029 plus exact adopted Directory Rules bytes. |
| Two root scaffold declarations | Preserved with exact IDs, blobs, permissiveness, status, source lineage, and contract-pointer limits. |
| Authority and responsibility split | Preserved and expanded across semantic contracts, policy, evidence, fixtures, tests, validators, receipts, proofs, runtime, and release. |
| Repository map | Preserved as a direct-child map and corrected to avoid a stale pseudo-inventory of adjacent families. |
| Consumer caution | Preserved and replaced with a bounded exact-reference census plus explicit external UNKNOWN. |
| Compatibility rules | Preserved and strengthened with one-writer, identity, sensitivity, correction, and rollback requirements. |
| Migration and retirement gates | Preserved and expanded into per-object, producer/consumer, package/deployment, and zero-writer/consumer evidence. |
| Belongs / does not belong | Preserved with explicit sensitive-data exclusions. |
| Validation boundary | Corrected: current workflow meta-schema checks every schema under `schemas/`; full profile has ten validators; common governance coverage is layout-dependent. |
| `review_record` validator note | Corrected from a short stub to the current 498-line fixture-only promotion projection. |
| Fixture posture | Corrected from one populated family to 58 direct directories, while preserving the distinction between presence and executable polarity. |
| Open questions | Preserved and converted into finite, evidence-closable SG items. |
| Correction and rollback | Preserved and expanded below. |

No schema, fixture, validator, policy, consent record, runtime, lifecycle object, release, deployment, or publication behavior changes in v0.3.

[Back to top](#top)

## Evidence ledger

### Pinned repository objects

| Evidence | Identity |
|---|---|
| Default branch snapshot | `98b28dc94057e29b7f79cedfd07fa81045d9f666` |
| Repository tree | `531fe76a0bf5c081e594d0099b90bd4b9a0bec64` |
| `schemas/governance/` tree | `2664193d814b02e183e983744cc5982a64027c94` |
| Prior target README | `258ab127ad747c3be10820fc7c433c9f5cf1dfab` |
| Root `overlay_pointer` schema | `631f5aa39a137ebd449505f3362f5da547b384eb` |
| Root `consent_receipt` schema | `a178b759fa19922f8d6c6adf1ec13402f9784e75` |
| `schemas/README.md` | `ce53d0ddb998ddcb8208d0367c90f9c25e31a8ad` |
| Versioned governance tree | `fdd6d6e3df3708ab4ac908af8b177342a2e72ffb` |
| Versioned governance README | `d6fbbbcd7db89d8f02c2dddcee93dc34b2bfd3d9` |
| Governance fixture tree | `a4ca23df7b543a4eef1c56e9a31e8b28846df887` |
| Governance fixture README | `c544d31673d139c955e3fe015394a6b900e241b3` |
| Governance semantic-contract tree | `accdf5788923e4197570c1160da3bcc9ebb1b657` |
| Common schema harness | `9cc60a66951ebf2a72a3a32c564f69c6d6eaea75` |
| Governance validator-test tree | `1071d4bb6d3395f2b2629405959f34024bb425b5` |
| `validate_review_record.py` | `a26f10fa18edaf7b2d2e3bf499e233c05f3007cd` |
| Validator registry | `c65c1c2b27b85be4bdc3c42d0555c6e8e44698e2` |
| Schema-validation workflow | `0e1562f539323daa401184738a0c490b51e2999b` |
| Validator-suite workflow | `dca889a3135b408767ff6cf21b7ce6eedfcc4781` |
| Consent policy README | `7dbae5ea1434ecf896176a891dadefea76913999` |
| Root-registry projection | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` |
| CODEOWNERS | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Adopted Directory Rules bytes | `fd49a0b83e55cef52c1124281f093e263526898d` |
| ADR-0029 | `3ba5f902ffe20a65a259cb0a7dab07f1725d204b` |
| ADR-0001 | `3c520ea8f2f8bcb3d478329a87d98b135ea335fd` |
| ADR-0002 | `e626d82970932c319a690fc6044727ed114ada6a` |

### Supplied design references

The supplied references informed the responsibility-root, schema-home, trust-membrane, lifecycle, sensitivity, and receipt/proof/release separation. They are design evidence, not proof of live repository implementation.

| Supplied artifact | SHA-256 |
|---|---|
| `Unified Implementation Architecture Build Manual.md` | `e92500f9b40007e8b69d183ecaa6247c542ffec25857875ecd2dbd00709785b1` |
| `Repository Structure Guiding Document.md` | `afe08af316d1f89779bab0d39888cdc65ee989907806a4126c331c50e4a0aa3a` |
| `KFM Repository Build-Out & Markdown Modernization Implementation Agent` v6.0.0 | `b7a203460181956333f5a4b4ccda5eea87e97254b5d6396a4ad4186f1013dabb` |

### Inspected coverage

- all three files in the compatibility lane;
- all 66 direct versioned governance schemas, including top-level strictness, status, contract-pointer posture, and `$id` values;
- all 58 direct governance fixture directories and their file layouts;
- all 42 direct governance validator test modules by path;
- the common schema harness, review-record validator, aggregate registry, schema workflow, and validator-suite workflow;
- exact tracked root-path and root-`$id` references;
- current consent-policy documentation, accepted placement doctrine, adjacent ADR status, root projection, and CODEOWNERS routing;
- the most recent observed unchanged-schema-tree workflow preflight and its later repository-topology failure.

Counts are snapshot facts, not adoption, completeness, operational use, or publication claims.

[Back to top](#top)

## Correction and rollback

Correct this README when:

- either root schema, source lineage, contract pointer, path, or `$id` changes;
- a root consumer, writer, generator, package, deployment, or external dependency is found;
- a canonical destination, compatibility behavior, owner, fixture, validator, policy binding, or release role is accepted;
- the versioned governance schema or fixture census changes;
- adjacent indexes are reconciled;
- an ADR changes status or accepted placement doctrine changes;
- a migration, redirect, deprecation, tombstone, or retirement decision is approved; or
- workflow coverage or exact-head results materially change.

### Documentation correction

If a count, link, status, or authority claim is wrong, pin the discovery revision, mark uncertainty explicitly, correct the smallest surface, rerun documentation and schema-adjacent checks, and update the generated receipt binding.

### Pre-merge rollback

Close or revise the draft pull request and abandon its unmerged branch. Do not delete remote objects, mutate main, or change either schema as a documentation rollback shortcut.

### Post-merge rollback

Use a transparent revert or forward-fix pull request that reverts this README and its generated receipt together. Re-run documentation, receipt, schema-preflight, and affected workflow checks. Never force-push shared history.

### Schema or migration correction

If a schema or identity transition is wrong, preserve the old path and identity long enough to correct consumers safely. Use reviewed versioning, compatibility, correction, withdrawal, cache or generated-client invalidation, and rollback evidence appropriate to actual reliance. Do not recreate two writable authorities.

Reverting this README changes documentation only. It does not alter schema behavior, contracts, policy, consent, privacy or rights controls, fixtures, validators, tests, governance records, evidence, receipts, proofs, release state, public interfaces, deployments, or publication state.

[Back to top](#top)

## Last reviewed

**Evidence date:** 2026-08-13 America/Chicago; the referenced unchanged-tree workflow ran 2026-08-14 UTC.

Re-review when this directory gains or loses a child, either root schema changes identity or shape, the versioned family or fixture topology changes, a consumer or owner is established, an adjacent ADR changes status, CI coverage changes, or a migration/retirement packet is proposed.

## Change log

| Version | Date | Change |
|---|---|---|
| `v0.2` | 2026-07-22 metadata / first tracked 2026-08-13 | Established the two-scaffold compatibility guardrail, routing, migration gates, and initial validation boundary. |
| `v0.3` | 2026-08-13 | Reconciled accepted placement authority, the exact compatibility tree, complete 66-schema and 58-directory censuses, bounded references, common-versus-dedicated coverage, current validator/workflow behavior, sensitive-data holds, migration, correction, rollback, and finite verification items. |

[Back to top](#top)
