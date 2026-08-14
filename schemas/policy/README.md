<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-policy-readme
title: schemas/policy/ — Policy-Schema Compatibility and Routing Boundary
type: README
version: v0.2
status: draft; repository-grounded; compatibility-orientation-only; no-direct-schema-payloads; migration-unresolved; non-authoritative; non-enforcing
owner: NEEDS VERIFICATION — CODEOWNERS routes /schemas/ to @bartytime4life, but routing is not accepted stewardship or independent approval
created: 2026-07-04
updated: 2026-08-13
policy_label: public
owning_root: schemas/
current_path: schemas/policy/README.md
responsibility: Preserve a bounded compatibility index for the historical root-level policy-schema path and route all new machine-shape work to schemas/contracts/v1/policy/ unless an accepted migration establishes another versioned profile.
truth_posture: CONFIRMED repository evidence; PROPOSED or UNKNOWN maturity where authority, activation, ownership, consumers, or retirement evidence is absent
evidence_snapshot: main@57466766124f2f64448a5d8ba1cb682367fc1d72; target blob 92cc831c2f22e8b7fb0fcb7b876efa53e78ab850; directory tree 2fe22c2280bb7bd68d7cfee12c4daf38c4264981
related:
  - schemas/README.md
  - schemas/contracts/v1/policy/README.md
  - contracts/policy/README.md
  - policy/README.md
  - fixtures/contracts/v1/policy/README.md
  - tools/validators/policy/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, schemas, policy, compatibility, routing, validation, migration, evidence]
notes:
  - This README documents current bytes and boundaries; it does not accept an ADR, create a canonical root, activate policy, authorize a migration, or retire a path.
  - The canonical versioned policy-schema family has mixed maturity. File presence and shape validity are not implementation, evaluation, enforcement, promotion, release, or publication evidence.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/policy/` — Policy-Schema Compatibility and Routing Boundary

> **One-line purpose.** Keep the historical root-level policy-schema path navigable and non-authoritative while routing machine-checkable policy object shapes to [`schemas/contracts/v1/policy/`](../contracts/v1/policy/README.md).

<kbd>COMPATIBILITY ORIENTATION</kbd> <kbd>0 DIRECT SCHEMAS</kbd> <kbd>CANONICAL WRITES: VERSIONED FAMILY</kbd> <kbd>NO POLICY EFFECT</kbd>

> [!IMPORTANT]
> `schemas/policy/` is not the canonical policy-schema family. It contains this README and a documentation-only `tests/` guardrail. New policy schemas belong under the versioned family unless an accepted decision authorizes a different profile.

> [!CAUTION]
> A parsed JSON document, a valid JSON Schema instance, a green workflow, or a policy-shaped record does **not** mean that policy ran. Shape validity does not grant access, clear rights or sensitivity, authenticate evidence, satisfy review, promote data, approve release, publish an artifact, or prove public safety.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-inheritance) · [Status](#status-and-evidence) · [Map](#current-directory-map) · [Canonical family](#canonical-policy-schema-family) · [Routing](#responsibility-routing) · [Boundaries](#what-belongs-here) · [Validation](#validation-and-negative-checks) · [Migration](#compatibility-migration-and-retirement) · [Review](#review-burden-and-escalation) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Purpose

This directory is a **compatibility and orientation lane** beneath the canonical [`schemas/`](../README.md) responsibility root. It exists to:

- preserve navigation for the historical `schemas/policy/` spelling;
- prevent new machine payloads from creating an unversioned parallel schema home;
- point contributors to the current versioned policy-schema family;
- distinguish machine shape from semantic meaning, normative policy, fixtures, executable tests, validators, decisions, receipts, proofs, and release state;
- record the evidence required before this path can be migrated, tombstoned, or retired.

This README does not make the path canonical, accepted, active, implemented, or safe to delete.

## Authority and inheritance

### Governing authority

| Source | Status at the evidence snapshot | Effect here |
|---|---|---|
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Adopts the exact Directory Rules v2 bytes and their placement and README contract. |
| [Directory Rules v2](../../docs/doctrine/directory-rules.md) | **ADOPTED BY ADR-0029**; its pinned internal header still says `PROPOSED_FOR_ADOPTION` | Defines `schemas/` as machine shape, makes the contracts/schemas/policy split mandatory, and defaults schemas to `schemas/contracts/v1/<family>/`. |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | **MACHINE PROJECTION ONLY** | Registers `root.schemas` for schema artifacts. It does not create authority, accept migration, or activate this child path. |
| [`schemas/README.md`](../README.md) | **CURRENT ROOT CONTRACT** | Supplies the parent machine-shape boundary, validation posture, maturity rules, and compatibility controls. |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Describes the versioned schema-home decision but is not accepted authority. The adopted Directory Rules independently provide the current default placement. |
| [ADR-0002](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **DRAFT source / effectively PROPOSED** | Useful design context only; it does not accept object-family placement or migration. |
| [ADR-0003](../../docs/adr/ADR-0003-policy-singular-is-canonical-%28policies-is-compatibility%29.md) | **PROPOSED** | Concerns the singular policy-rule root. It does not make this schema compatibility lane canonical or active. |

### Local authority statement

This README may document repository state, route contributors, preserve compatibility facts, and name unresolved decisions. It must not:

- accept or supersede an ADR;
- create a second schema authority;
- move or copy canonical schema payloads;
- activate a policy bundle, evaluator, validator, consumer, gate, or runtime;
- authorize promotion, release, publication, correction, withdrawal, rollback execution, or deletion;
- convert a placeholder or scaffold into implemented status through prose.

`CODEOWNERS` routes `/schemas/` review to `@bartytime4life`. That is review routing, not proof of an accepted schema steward, independent approval, separation of duties, or branch-protection enforcement.

## Status and evidence

The following statements are pinned to `main@57466766124f2f64448a5d8ba1cb682367fc1d72`.

| Question | Evidence-backed answer | Truth label |
|---|---|---|
| Is `schemas/policy/` tracked? | Yes; tree `2fe22c2280bb7bd68d7cfee12c4daf38c4264981`. | **CONFIRMED** |
| Does it contain direct schema JSON? | No. Its only direct file is this README; its only child directory is `tests/`. | **CONFIRMED** |
| Does `tests/` contain executable tests? | No. It contains `README.md` and an empty `.gitkeep`. | **CONFIRMED** |
| Where is the configured versioned family? | `schemas/contracts/v1/policy/`, tree `9f28503b77a7876f09e1f786221828b2f170661e`. | **CONFIRMED** |
| What is in that family? | 15 Draft 2020-12 `*.schema.json` files, one non-schema JSON placeholder, and one README. | **CONFIRMED** |
| Are all family artifacts mature or active? | No. Explicit statuses include `PROPOSED` and `PROPOSED_INACTIVE`; some files omit a status; two artifacts are permissive scaffolds/placeholders. | **CONFIRMED MIXED MATURITY** |
| Is this path an accepted compatibility root with verified owner, consumers, expiry, and exit criteria? | No complete acceptance or closure record was verified. | **NEEDS VERIFICATION** |
| May this README be used as retirement authority? | No. Consumer closure, reference closure, migration evidence, rollback, and an accepted decision remain absent. | **HOLD** |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Directly observed in the pinned Git tree, file bytes, workflow definition, or hosted run. |
| **PROPOSED** | Declared candidate or draft; not accepted or active. |
| **PROPOSED_INACTIVE** | Structured and testable candidate that explicitly denies activation or operational authority. |
| **NEEDS VERIFICATION** | Evidence is incomplete, stale, indirect, or absent. |
| **UNKNOWN** | The repository snapshot does not establish the answer. |
| **HOLD** | Do not migrate, delete, activate, or rely operationally until named gates close. |

## Current directory map

Directory Rules `DIR-README-003` requires a current map to show this directory and direct children only. The deeper `tests/` inventory belongs to its own README.

```text
schemas/policy/
├── README.md    # This compatibility, routing, evidence, and migration boundary
└── tests/       # Documentation-only test-placement guardrail; no executable tests
```

Exact tracked subtree:

| Path | Git object | Current role |
|---|---|---|
| `schemas/policy/README.md` | blob `92cc831c2f22e8b7fb0fcb7b876efa53e78ab850` before this update | Compatibility index being modernized. |
| [`schemas/policy/tests/README.md`](./tests/README.md) | blob `955264812535fe6a7a10e38821b049b401bc0fe9` | Child compatibility guardrail; its inventory text predates the tracked `.gitkeep` and requires a separate reconciliation. |
| `schemas/policy/tests/.gitkeep` | empty blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | Materializes the empty directory; it is not a test, fixture, schema, or implementation marker. |

No deeper file is implied by this map. No future tree is proposed here.

## Canonical policy schema family

### Placement

The configured machine-shape family is [`schemas/contracts/v1/policy/`](../contracts/v1/policy/README.md). The unversioned [`schemas/contracts/policy/`](../contracts/policy/README.md) path is itself a compatibility and migration index, not the preferred destination for new schemas.

The canonical family tree contains 18 entries including its directory and README: 15 JSON Schemas, one ordinary JSON placeholder, and the README. All 15 `*.schema.json` files parse as JSON, declare Draft 2020-12, and carry unique `$id` values at the pinned snapshot. Those facts establish machine-schema identity only.

### Complete JSON artifact inventory

| Artifact | Observed machine posture | Declared maturity or evidence limit |
|---|---|---|
| [`conditional_decision_closure.schema.json`](../contracts/v1/policy/conditional_decision_closure.schema.json) | Closed object; 14 required properties. | No explicit status field; description says fixture-only and grants no authority. |
| [`policy_decision.schema.json`](../contracts/v1/policy/policy_decision.schema.json) | Closed object; six required properties. | `PROPOSED`; declared validator and policy paths are intentionally absent in the current readiness hold. |
| [`policy_decision_vocabulary.schema.json`](../contracts/v1/policy/policy_decision_vocabulary.schema.json) | Closed object; seven required properties. | `PROPOSED_INACTIVE`; fixture-only. |
| [`policy_enforcement_maturity.schema.json`](../contracts/v1/policy/policy_enforcement_maturity.schema.json) | Closed object; 12 required properties. | No explicit status field; current evidence is fixture/validator oriented, not enforcement proof. |
| [`policy_evaluation_binding_v1.schema.json`](../contracts/v1/policy/policy_evaluation_binding_v1.schema.json) | Closed object; seven required properties. | `PROPOSED_INACTIVE`; fixture-only declaration, not evaluator execution. |
| [`policy_input_bundle.schema.json`](../contracts/v1/policy/policy_input_bundle.schema.json) | Open object; one required and three declared properties; additional properties allowed. | `PROPOSED`; description calls it a greenfield placeholder. |
| [`policy_input_bundle_profile_v1.schema.json`](../contracts/v1/policy/policy_input_bundle_profile_v1.schema.json) | Closed object; 14 required properties. | `PROPOSED_INACTIVE`; explicit fixture-only profile. |
| [`policy_obligation_reduction.schema.json`](../contracts/v1/policy/policy_obligation_reduction.schema.json) | Closed object; 15 required properties. | `PROPOSED_INACTIVE`; deterministic reduction record only, with explicit non-effects. |
| [`policy_obligation_set.schema.json`](../contracts/v1/policy/policy_obligation_set.schema.json) | Closed object; 10 required properties. | No explicit status field; metadata says candidate carrier only and denies evaluation, enforcement, release, and publication. |
| [`policy_reviewer_role_vocabulary.schema.json`](../contracts/v1/policy/policy_reviewer_role_vocabulary.schema.json) | Closed object; six required properties. | No explicit status field; activation and authority remain **NEEDS VERIFICATION**. |
| [`policy_transform_plan_simulation.schema.json`](../contracts/v1/policy/policy_transform_plan_simulation.schema.json) | Closed object; 16 required properties. | `PROPOSED_INACTIVE`; fixture-only, no transform or authority. |
| [`promotion_decision.schema.json`](../contracts/v1/policy/promotion_decision.schema.json) | Open object; zero declared properties; additional properties allowed. | `PROPOSED` scaffold; `contract_doc` is null. It is not a promotion decision implementation. |
| [`redaction-receipt.json`](../contracts/v1/policy/redaction-receipt.json) | Ordinary JSON with no `$schema`, `$id`, title, type, or property contract. | `PROPOSED` placeholder located beside schemas; classification and migration remain open. |
| [`sensitivity_label.schema.json`](../contracts/v1/policy/sensitivity_label.schema.json) | Closed object; three required properties. | `PROPOSED`; declared validator and policy paths are absent. |
| [`sovereignty_exception_receipt.schema.json`](../contracts/v1/policy/sovereignty_exception_receipt.schema.json) | Closed object; 14 required properties. | `PROPOSED_INACTIVE`; records an asserted external decision and grants no exception. |
| [`threshold_policy_registry.schema.json`](../contracts/v1/policy/threshold_policy_registry.schema.json) | Closed object; eight required properties. | `PROPOSED_INACTIVE`; unresolved-slot registration only. |

### Confirmed drift and review triggers

The exact family inventory exposes review work; it does not authorize repair in this README change.

- The 15 schema `$id` values use five observed base patterns: `https://schemas.kfm.local/…`, `https://kansasfrontiermatrix.org/…`, `https://kfm.local/…`, `kfm://schema/…`, and `kfm://schemas/…`.
- `redaction-receipt.json` is not a JSON Schema even though it sits in the schema family.
- `policy_input_bundle.schema.json` and `promotion_decision.schema.json` remain permissive scaffolds.
- `promotion_decision.schema.json` has no paired contract document in its metadata.
- `policy_decision.schema.json`, `policy_input_bundle.schema.json`, and `sensitivity_label.schema.json` declare validator paths that are absent from the pinned tree.
- The same candidate metadata points to absent `policy/policy/` and, for the input bundle, absent `fixtures/policy/policy_input_bundle/` paths.
- The broad `policy-test` workflow deliberately asserts that the declared `PolicyDecision` validator and policy path remain absent until a reviewed graduation wires them.

These are **CONFIRMED current-state observations**, not findings that every artifact is invalid. Resolve object by object with contract, schema, fixture, validator, consumer, migration, and rollback review.

## Responsibility routing

| Need or artifact | Owning lane | Boundary |
|---|---|---|
| Machine-valid policy object shape | [`schemas/contracts/v1/policy/`](../contracts/v1/policy/README.md) | Shape only; mixed maturity remains explicit. |
| Policy object meaning and invariants | [`contracts/policy/`](../../contracts/policy/README.md) | Semantics, not canonical machine shape or policy outcome. |
| Allow, deny, hold, restrict, or abstain rules and bundles | [`policy/`](../../policy/README.md) | Normative admissibility source; not schema authority or decision-instance storage. |
| Synthetic valid/invalid examples | [`fixtures/contracts/v1/policy/`](../../fixtures/contracts/v1/policy/README.md) | Reusable fixture evidence; not public truth or runtime state. |
| Executable schema and contract tests | [`tests/schemas/`](../../tests/schemas/README.md) and [`tests/contracts/`](../../tests/contracts/README.md) | Executable conformance evidence; not this compatibility child. |
| Deterministic policy-profile validators | [`tools/validators/policy/`](../../tools/validators/policy/README.md) | Candidate semantic/profile checks; not a policy evaluator. |
| Policy decision, process record, or receipt instance | Owning process or lifecycle lane under `data/`, `release/`, or another accepted home | Instances do not live beside rule source merely because their type contains “policy.” |
| Promotion, release, correction, withdrawal, and rollback decision | [`release/`](../../release/README.md) | Lifecycle authority; schema validity cannot substitute. |
| This historical spelling and migration guidance | `schemas/policy/` | README-only compatibility orientation pending a governed disposition. |

### Dependency direction

```text
semantic contract
      ↓ informs
canonical versioned schema ──→ reusable fixtures ──→ executable tests / validators
      ↑ referenced by                                  ↓ bounded evidence
normative policy source ──→ evaluator / governed consumer ──→ lifecycle decision

schemas/policy/README.md ──routes to these lanes; it is not in the execution path
```

The arrows describe responsibility and evidence flow. They do not establish that an evaluator, consumer, or lifecycle gate exists for every schema.

## What belongs here

Only bounded compatibility material belongs in the current lane:

- this README;
- a direct-child README that explains compatibility, placement, migration, or retirement status;
- verified old-path-to-canonical-target mappings;
- inventories of known writers, readers, references, and unresolved consumers;
- migration, parity, correction, rollback, expiry, and exit criteria;
- evidence labels that keep scaffolds, placeholders, fixture-only profiles, and active implementations distinct.

Any future file beyond documentation requires an accepted placement decision and a complete change packet. An empty `.gitkeep` remains inert.

## What is prohibited

| Do not place here | Correct responsibility |
|---|---|
| New canonical or versioned policy schemas | `schemas/contracts/v1/policy/` |
| Semantic Markdown defining policy object meaning | `contracts/policy/` |
| Rego, OPA bundles, allow/deny/hold/restrict/abstain rules, or evaluator configuration | `policy/` and an accepted runtime boundary |
| Valid/invalid JSON fixtures or expected findings | `fixtures/contracts/v1/policy/` |
| Pytest, unittest, validator implementation, or evaluator code | `tests/` or `tools/validators/` as appropriate |
| Emitted decisions, validation reports, receipts, proofs, logs, or runtime state | The accepted process, data, evidence, or release lane |
| Rights, sensitivity, access, consent, redaction, promotion, release, or publication approval | The accepted policy/review/release authority; never a schema directory |
| Generated bindings without source identity and regeneration controls | Declared generated-output lane with canonical schema source and command |
| Secrets, restricted source payloads, exact sensitive geometry, or production credentials | Approved protected storage outside this public documentation lane |
| A live mirror or independently writable copy of the versioned family | Prohibited; preserve single-write authority |

## Inputs, outputs, writers, and consumers

### Inputs

- accepted placement doctrine and ADR status;
- the exact `schemas/policy/` Git tree and target history;
- the current versioned policy-schema inventory and metadata;
- paired contract, fixture, validator, test, policy, workflow, and consumer evidence;
- verified migration or retirement records when they exist.

### Outputs

- contributor routing;
- a bounded current-state inventory;
- non-effects and trust-boundary warnings;
- a migration and retirement hold with explicit exit gates;
- review triggers and open verification items.

This README emits no schema, policy decision, validation report, receipt, proof, promotion, release, or publication artifact.

### Permitted writers

Documentation-only edits may be proposed by maintainers with schema-aware and documentation review. New machine payloads, mirrors, generated files, tests, fixtures, or validators are not permitted here without accepted placement and migration authority.

### Consumers

Confirmed consumers are repository readers and contributors using this index for navigation. Historical code, automation, packages, external links, or downstream systems that require the `schemas/policy/` spelling remain **UNKNOWN / NEEDS VERIFICATION**. Absence from a bounded search is not proof of zero consumers.

## Non-effects and trust boundary

Neither this lane nor the canonical shape family can, by itself:

- determine whether an action is allowed, denied, held, restricted, or abstained;
- prove that policy inputs were complete, authentic, current, or authorized;
- bind or execute a policy evaluator;
- authenticate a reviewer or satisfy independent approval;
- clear source rights, consent, sovereignty, privacy, geoprivacy, or sensitivity obligations;
- apply redaction, generalization, suppression, embargo, date fuzzing, or another transform;
- promote a dataset or artifact between lifecycle phases;
- approve release, publication, or public use;
- create a receipt or proof merely because an instance validates;
- authorize correction, withdrawal, rollback execution, migration, tombstoning, or deletion.

When evidence is incomplete, the correct outcome is `NEEDS VERIFICATION`, `UNKNOWN`, or `HOLD`—not an inferred pass.

## Exposure, mutation, retention, and storage

| Dimension | Current posture |
|---|---|
| Exposure | Public repository documentation. Do not add secrets, restricted payloads, or sensitive source examples. |
| Mutation | Reviewable Markdown changes only under the current compatibility posture. Canonical machine writes go to the versioned family. |
| Retention | Retain until a governed migration proves reference and consumer closure and records retirement. No expiry is currently accepted. |
| Generation | Hand-maintained documentation. No generator or mirror is established for this lane. |
| Physical storage | Git-tracked UTF-8 Markdown plus an empty `.gitkeep` in the child directory. |
| Authority storage | Inherited from accepted doctrine and the canonical `schemas/` root contract, not from this README or the root-registry projection. |

## Validation and negative checks

Validation must be fail-closed and interpreted at the correct layer.

### Documentation checks

```bash
python tools/validators/docs/link-check/check_links.py schemas/policy/README.md

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required schemas/policy/README.md

python tools/validators/docs/document-graph/check_document_graph.py \
  --entrypoint schemas/policy/README.md schemas/policy/README.md

python tools/validators/docs/stale-scan/check_stale_docs.py \
  --as-of 2026-08-13 --profile bounded-required schemas/policy/README.md
```

These commands test local documentation properties. They do not validate policy semantics, evaluator behavior, schema fixtures, or lifecycle authority.

### Compatibility-lane inventory

```bash
# Current tracked material: README, tests/README, and tests/.gitkeep only.
find schemas/policy -type f -print | LC_ALL=C sort

# These commands must print nothing while the README-only posture holds.
find schemas/policy -type f -name '*.json' -print
find schemas/policy -type f \( -name '*.py' -o -name '*.rego' -o -name '*.wasm' \) -print
```

Any unexpected output is a review trigger. It is not automatically safe to delete; first classify history, writers, consumers, authority, and rollback.

### Current schema checks

```bash
# Registered schema orchestrator. Current-main baseline status is documented below.
make schemas

# Repository-owned executable shape/contract suites.
python -m pytest -q tests/schemas tests/contracts
```

The [`schema-validation`](../../.github/workflows/schema-validation.yml) definition additionally:

- parses every JSON file under `schemas/`;
- meta-validates every `*.schema.json` file;
- requires canonical v1 schemas to declare Draft 2020-12 and unique `$id` values;
- requires non-empty valid and invalid fixtures with reviewed rejection evidence for eight configured aggregate families;
- runs `make schemas` and then `tests/schemas` plus `tests/contracts` if the earlier step succeeds.

The eight configured aggregate families are not policy families. Policy shape coverage is additive through the common schema harness and specific readiness checks; it is not proof that every policy artifact has complete valid/invalid, semantic, evaluator, or consumer coverage.

### Hosted exact-head evidence

| Surface | Exact-head result at `5746676…` | Correct interpretation |
|---|---|---|
| [`schema-validation` run 31757075637](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31757075637) | **FAIL** | JSON parsing, meta-schema checks, 855 canonical-v1 unique IDs, and configured fixture preflight passed. `make schemas` failed because the aggregate `repository-topology` validator rejected; the executable schema/contract tests were skipped. This README change does not claim to fix that baseline failure. |
| [`policy-test` run 31757075636](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31757075636) | **PASS / WORKFLOW HOLD** | Static readiness and bounded `PolicyDecision` shape checks passed. The job evaluated no repository-wide policy and emitted no `PolicyDecision`. |
| `docs-build`, `link-check`, `docs-meta-block`, and `docs-document-graph` at the same head | **PASS** | Establishes the prior main documentation state only, not this proposed README until its own PR checks run. |
| Required-check coupling and independent approval | **UNKNOWN** | Workflow and CODEOWNERS presence do not prove branch rules, ruleset significance, or separation of duties. |

### Negative assertions

Review must fail or hold if a change:

- introduces direct schema, fixture, test, validator, rule, bundle, receipt, proof, or decision payloads here without accepted placement;
- duplicates a canonical versioned schema under this unversioned path;
- treats `PROPOSED`, `PROPOSED_INACTIVE`, placeholder, or status-absent artifacts as active;
- weakens strict schema shape without a contract, fixture, consumer, and migration assessment;
- interprets schema validity as policy, rights, sensitivity, review, release, or publication approval;
- adds a new `$id` collision or silently changes object identity;
- deletes the lane without reference, writer, consumer, link, and rollback closure;
- uses `|| true`, empty-fixture success, skipped tests, or missing dependencies as conformance evidence.

## CI and execution surface

| Surface | What it checks | What it does not prove |
|---|---|---|
| `schema-validation` | Repository schema JSON, meta-schema validity, canonical-v1 identity, configured aggregate fixtures, orchestrator, and executable schema/contract tests when reached. | Meaning, evidence closure, policy outcome, rights, sensitivity, release, or publication. |
| `policy-test` | Broad policy-readiness holds, bounded Rego-lane wiring, `PolicyDecision` fixture shape, and policy-validator test/workflow wiring. | General policy evaluation, evaluator binding, active bundle selection, or authentic decisions. |
| `policy-boundary-guards` | Selected structural/static/API trust boundaries. | Policy-bundle, rights, sensitivity, release, or publication proof. |
| Documentation workflows | Metadata, links/fragments, graph reachability, freshness, and rendering/build properties. | Correct architecture, accepted ownership, operational enforcement, or external consumer closure. |
| Repository-topology validator | Adopted placement rules against a bounded inherited-drift baseline. | New authority, migration approval, policy correctness, or deletion permission. |

No workflow in this table writes canonical policy decisions, receipts, proofs, releases, or published data.

## Contributor workflow

### Documentation-only clarification

1. Pin the current default-branch commit and target blob.
2. Read this README completely and inspect the exact direct-child tree.
3. Check open PRs and branches for target overlap.
4. Reconcile accepted doctrine, ADR status, root registry, parent README, canonical target, paired lanes, workflows, and recent exact-head runs.
5. Preserve all prior scope, routing, boundary, validation, and open-question content in corrected form.
6. Run documentation validation and record any baseline failures separately from change-induced failures.
7. Submit a focused review change; do not combine schema migration or activation work.

### Proposed machine payload or migration

Stop and prepare a complete object-family change packet before writing:

- accepted placement or migration authority;
- stable object identity and canonical `$id` plan;
- semantic contract and machine schema;
- valid, invalid, boundary, and adversarial fixtures;
- deterministic validator and executable tests;
- producer and consumer inventory;
- compatibility and versioning strategy;
- rights, sensitivity, and public-exposure review where applicable;
- correction, rollback, and retirement plan;
- observed CI and independent approval evidence.

Do not bulk-move by filename. Classify each object by authority, meaning, shape, policy relation, lifecycle state, writers, readers, sensitivity, and rollback needs.

## Review burden and escalation

| Change class | Minimum review burden |
|---|---|
| README-only evidence or routing correction | Documentation reviewer plus schema-aware maintainer. |
| Compatibility status, alias, target, writer, consumer, expiry, or exit-criteria change | Schema steward, architecture/docs reviewer, affected consumers, and migration owner; accepted authority where required. |
| Canonical schema addition or change | Contract/schema owner, validator/test owner, producers, consumers, and affected policy or lifecycle reviewers. |
| Policy, rights, sensitivity, consent, sovereignty, or redaction coupling | Policy and security/privacy reviewers plus affected domain and release owners. |
| Promotion, release, publication, correction, withdrawal, rollback, tombstone, or deletion | Accepted lifecycle authority, independent review, consumer closure, and rollback evidence. |

Escalate conflicts to the owning schema root and accepted governance process. When two sources conflict, use this order: accepted ADR and adopted bytes; accepted machine projection as projection only; current exact repository state; proposed ADRs and design documents; stale or illustrative README prose.

## Compatibility, migration, and retirement

### Current posture

Repository history shows that a placeholder version of this lane existed in March 2026, was deleted, and the current README path was recreated on 2026-07-04 local repository time. History proves prior path existence; it does not prove current external consumers, accepted compatibility status, or deletion safety.

Under the current single-write posture:

- new schemas go only to the canonical versioned family;
- this path stays documentation-only;
- consumers may navigate through this README, but no machine mirror is established;
- a compatibility note cannot be more authoritative, permissive, public, or mutable than its target.

### Migration or retirement gates

Do not tombstone or delete `schemas/policy/` until a reviewed migration establishes all applicable evidence:

1. accepted path disposition and accountable owner;
2. canonical target and object-family identity mapping;
3. complete repository reference and fragment inventory;
4. verified internal and external writers and consumers;
5. canonical-only writes and any bounded dual-read period;
6. parity checks for every remaining old-path read;
7. documentation and package-reference updates;
8. expiry, exit criteria, and rollback behavior;
9. zero-writer and zero-consumer closure appropriate to physical deletion;
10. retirement receipt or other accepted lifecycle record.

Until those gates close, retirement is **HOLD**.

## Correction and rollback

### Documentation correction

If this README contains an incorrect count, link, status, or authority claim:

1. pin the discovery commit and affected bytes;
2. mark the claim `NEEDS VERIFICATION` or `CONFLICTED` rather than silently substituting certainty;
3. correct the smallest documentation surface;
4. rerun local link, metadata, graph, and freshness checks;
5. update the generated-receipt evidence for the corrected artifact;
6. preserve prior history through Git.

### Pre-merge rollback

Close or revise the proposed branch. Because this change is documentation-only, no schema, fixture, policy, runtime, data, release, or publication rollback should be necessary.

### Post-merge rollback

Revert the focused README and its generated receipt together if the update is materially wrong. Do not delete the compatibility directory or mutate the canonical family as a documentation rollback shortcut.

### Machine-schema correction

If a paired schema is wrong, correct it in its canonical versioned family with contract, fixture, validator, consumer, migration, and versioning review. This README may record the result but cannot execute that correction.

## Open verification register

| ID | Question or gap | Status | Closure evidence required |
|---|---|---|---|
| SP-001 | Who is the accepted steward for this compatibility lane and the canonical policy-schema family? | **NEEDS VERIFICATION** | Accepted ownership record; CODEOWNERS alone is insufficient. |
| SP-002 | Should `schemas/policy/` remain an orientation lane, become a tombstone, or retire? | **HOLD** | Accepted disposition, consumer/reference closure, exit criteria, and rollback. |
| SP-003 | Are there historical or external consumers of the root-level spelling? | **UNKNOWN** | Repository, package, documentation, deployment, and external-consumer inventory. |
| SP-004 | Should `schemas/policy/tests/` remain, migrate, or retire? | **NEEDS VERIFICATION** | Accepted test-placement decision and reference closure. |
| SP-005 | What single `$id` namespace/profile should the policy family use? | **NEEDS VERIFICATION** | Accepted identity convention and migration impact assessment. |
| SP-006 | Should `redaction-receipt.json` become a schema, fixture, example, or migrate elsewhere? | **NEEDS VERIFICATION** | Object classification, contract, canonical identity, consumers, and migration. |
| SP-007 | When may permissive `policy_input_bundle` and `promotion_decision` scaffolds graduate? | **HOLD** | Closed contracts, negative fixtures, validators, consumers, and accepted lifecycle semantics. |
| SP-008 | How should absent validator and `policy/policy/` metadata references be corrected? | **NEEDS VERIFICATION** | Object-by-object authority and migration review; no blind path rewrite. |
| SP-009 | Which policy schema families have complete positive, negative, semantic, and consumer tests? | **NEEDS VERIFICATION** | Coverage manifest mapped to exact schemas, fixtures, validators, tests, and consumers. |
| SP-010 | Is `schema-validation` a required check, and when will the current repository-topology rejection close? | **NEEDS VERIFICATION** | Exact-head green run plus ruleset/branch-protection evidence and an independently reviewed baseline correction. |
| SP-011 | Are branch rules and independent approval controls enforced for schema changes? | **UNKNOWN** | Repository settings or ruleset evidence. |
| SP-012 | Is every status-absent policy schema intentionally fixture-only, proposed, or accepted? | **NEEDS VERIFICATION** | Accepted per-object maturity records without inference from file presence. |

## Review checklist

- [ ] The default-branch commit and target blob were pinned before editing.
- [ ] Open PRs and branches were checked for target overlap.
- [ ] The exact `schemas/policy/` direct-child tree was inspected.
- [ ] Accepted ADRs were separated from proposed or draft records.
- [ ] The root-registry projection was not treated as decision authority.
- [ ] The canonical policy-family inventory is complete for the pinned snapshot.
- [ ] Scaffolds, placeholders, status-absent files, and inactive profiles are labeled distinctly.
- [ ] Contracts, schemas, policy, fixtures, tests, validators, decisions, receipts, proofs, and release authority remain separated.
- [ ] Commands are fail-closed and contain no `|| true` escape.
- [ ] Current-main baseline failures are disclosed and not attributed to this documentation change.
- [ ] No operational maturity, enforcement, review, release, or public-safety claim exceeds the evidence.
- [ ] Migration, correction, rollback, and retirement gates are explicit.
- [ ] Local links, metadata, document graph, and freshness checks pass for the proposed artifact.

## No-loss ledger

| v0.1 content | v0.2 disposition |
|---|---|
| Purpose and active-family routing | Preserved and grounded in accepted Directory Rules plus exact current paths. |
| Status table | Expanded with tree/blob identities, counts, mixed maturity, and truth labels. |
| Boundary and non-effects | Preserved and strengthened into explicit responsibility and trust-boundary sections. |
| Current inventory | Corrected to include `tests/.gitkeep` and a direct-child-only map. |
| Correct nearby lanes | Preserved as the responsibility-routing matrix. |
| Belongs / does not belong | Preserved with artifact-specific destinations and placement gates. |
| Compatibility rules | Preserved as single-write, migration, and retirement controls. |
| Validation commands | Corrected from `tests/contract || true` to the workflow-backed fail-closed `tests/contracts` command; exact-main failure evidence is disclosed. |
| Open questions | Preserved and expanded into finite, evidence-closable verification items. |

No canonical schema, fixture, validator, policy rule, test, runtime, data, release, or publication behavior is changed by this README update.

## Evidence ledger

### Pinned repository objects

| Evidence | Identity |
|---|---|
| Default branch snapshot | `57466766124f2f64448a5d8ba1cb682367fc1d72` |
| Repository tree | `8682429c4eb5108bc46b1c780900a2314736afb7` |
| `schemas/policy/` tree | `2fe22c2280bb7bd68d7cfee12c4daf38c4264981` |
| Prior target blob | `92cc831c2f22e8b7fb0fcb7b876efa53e78ab850` |
| `schemas/policy/tests/` tree | `b9cce1e8a4b99abdb4c30dd881af6d184268b27d` |
| Canonical policy-family tree | `9f28503b77a7876f09e1f786221828b2f170661e` |
| Canonical policy-family README | `5129bc970b8c87dc1350b09611c21dbd697c368e` |
| Policy fixture-family tree | `90038604cefe81e8c0e1c05664f53f340ddfd6c9` |
| Policy semantic-contract tree | `d013aed619117f286d01f697428f8af1e6ba5734` |
| Policy validator tree | `9d27cf72099a1234e2ba0187fd0247e5f8ac9760` |
| `tests/schemas/` tree | `d03bdeed77cc084c0c926d05be8d71b2f43df6b1` |
| `tests/contracts/` tree | `7aaff0b5ffe5361d51a94006efc0501b60cb6734` |
| `schema-validation` workflow | `0e1562f539323daa401184738a0c490b51e2999b` |
| `policy-test` workflow | `ac8f125e8a4d3634d86f66836d2aa2c0e3925e75` |
| `policy-boundary-guards` workflow | `1d7ba1df0f8ed291a15b1d9a44e404ba95d9e35c` |
| CODEOWNERS | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Adopted Directory Rules bytes | `fd49a0b83e55cef52c1124281f093e263526898d` |
| ADR-0029 | `3ba5f902ffe20a65a259cb0a7dab07f1725d204b` |
| ADR-0001 | `3c520ea8f2f8bcb3d478329a87d98b135ea335fd` |
| ADR-0002 | `e626d82970932c319a690fc6044727ed114ada6a` |
| ADR-0003 | `08ed360975943e69b171f53346a860f4a4a11bd4` |

### Inspected coverage

- all 5 entries in the current `schemas/policy/` subtree;
- all 18 entries in the current canonical policy-schema subtree;
- all 16 canonical-family JSON artifacts, including their schema identities, top-level shape, declared maturity, and candidate metadata;
- 14 direct policy fixture families across 141 subtree entries;
- 15 direct semantic policy contract documents plus one deeper `policy_decision/` boundary;
- 12 dedicated Python validators under `tools/validators/policy/`;
- executable `tests/schemas/` and `tests/contracts/` roots;
- current workflow definitions and hosted exact-head results;
- target history, accepted Directory Rules adoption, proposed adjacent ADRs, root projection, and CODEOWNERS routing.

## Last reviewed

**Evidence date:** 2026-08-13 America/Chicago; hosted exact-head runs completed 2026-08-14 UTC.

Re-review when this directory gains or loses a child, the canonical target changes, a policy schema changes identity or maturity, a validator/fixture/test/consumer is added, an adjacent ADR changes status, CI coverage or CODEOWNERS changes, a compatibility deadline is set, a correction occurs, or retirement evidence is proposed.

## Change log

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-07-04 | Established the root-level policy-schema compatibility guardrail and basic routing. |
| `v0.2` | 2026-08-13 | Reconciled accepted placement authority, exact topology, the complete canonical-family inventory, mixed maturity, adjacent responsibility lanes, current CI evidence, fail-closed validation, review burden, migration/retirement gates, rollback, and a finite verification register. |

[Back to top](#top)
