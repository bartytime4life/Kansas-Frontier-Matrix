<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/biotopes
title: Biotopes Policy Compatibility Guardrail
type: policy-readme; directory-readme; boundary-compact; compatibility-guardrail
version: v0.3
status: draft; repository-grounded; current-state-reconciled; CONFLICTED; compatibility-guardrail; non-authoritative; documentation-only; evaluator-unbound; non-release; non-publication
owners: OWNER_TBD — Habitat steward · Policy steward · Sensitivity steward · Flora steward · Fauna steward · Release steward · Docs steward; CODEOWNERS routing is not accepted role assignment
created: 2026-06-15
updated: 2026-08-13
policy_label: restricted; compatibility; fail-closed; no-independent-authority; no-release-authority; no-publication-authority
supersedes: v0.2 (2026-07-14)
current_path: policy/biotopes/README.md
owning_root: policy/
local_scope_id: NEEDS VERIFICATION — the document ID is not an accepted evaluator scope or policy family
canonical_relationship: compatibility-only guardrail for a non-canonical umbrella term; operational policy remains with accepted Habitat or shared policy lanes and canonical object families
directory_governance: accepted ADR-0029 adopts Directory Rules v2; policy/ is the singular policy-source root; this BOUNDARY_COMPACT README does not upgrade the lane to implemented status
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: a893b30f4dd1edfed151620c529734f4fd789a89
  target_baseline_blob: cb1f7144290951fc8209f094b3ccacfacf006c92
  target_tree: a0b5896b91bd6403281848fa89cbba575fa85ae7
  contracts_compatibility_tree: 6367c1e4ff8178a13f7ba0a06e08f4fa75161ea5
  schemas_compatibility_tree: 62458cf021a53cfbe71e4b46a9b3d0ee29cdaa32
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_lane_files_confirmed:
    - policy/biotopes/.gitkeep
    - policy/biotopes/README.md
  open_overlapping_pull_requests_found: "0 at preflight"
  inventory_method: authenticated GitHub reads of the exact target, history, complete recursive tree, governing doctrine and ADR, root registry, compatibility siblings, Habitat policy and tests, shared policy contracts and schemas, runtime/API scaffolds, workflows, CODEOWNERS, contribution controls, branches, and open pull requests
  bounded_inventory_note: no executable rule, fixture, test, bundle manifest, evaluator binding, decision instance, release record, or publisher exists directly in policy/biotopes; bounded absence is not proof of permanent absence
related:
  - ../README.md
  - ../domains/habitat/README.md
  - ../sensitivity/README.md
  - ../sensitivity/habitat_classes.yaml
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../contracts/biotopes/README.md
  - ../../contracts/domains/habitat/habitat_patch.md
  - ../../contracts/domains/habitat/land_cover_observation.md
  - ../../contracts/domains/habitat/ecological_system.md
  - ../../schemas/biotopes/README.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../docs/domains/habitat/sublanes/biotopes.md
  - ../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../docs/domains/habitat/README.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/architecture/trust-membrane.md
  - ../../control_plane/root_registry.yaml
  - ../../packages/policy-runtime/README.md
  - ../../apps/governed-api/README.md
  - ../../tests/policy/README.md
  - ../../tests/domains/habitat/policy/README.md
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/domain-habitat.yml
  - ../../.github/CODEOWNERS
  - ../../CONTRIBUTING.md
  - ../../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, policy, biotopes, habitat, compatibility, guardrail, non-canonical, sensitivity, geoprivacy, source-role, classifier-vintage, deny-by-default, migration, rollback, boundary-compact]
truth_posture: "CONFIRMED exact two-file direct lane, three README-plus-marker compatibility lanes, singular policy root, accepted ADR-0029 placement, Habitat docs vocabulary boundary, eighteen default-only Habitat Rego stubs, placeholder Habitat policy tests, shared PolicyInputBundle and PolicyDecision candidates, placeholder general policy runtime, abstain-only governed API scaffold, and non-evaluating broad policy readiness workflow / PROPOSED future placement disposition, active Habitat rule semantics, policy-family composition, reason codes, obligations, fixtures, negative tests, evaluator binding, decision receipts, migration, and deprecation / CONFLICTED top-level compatibility paths versus the no-parallel-authority doctrine and umbrella Biotope vocabulary versus canonical Habitat and Flora objects / UNKNOWN accepted local owner, active bundle, evaluator, governed consumer, branch-protection significance, production enforcement, release integration, public behavior, and external consumers"
notes:
  - "v0.3 reconciles the existing v0.2 guardrail against current main while preserving its substantive purpose, scope, gates, negative cases, migration discipline, and trust boundaries."
  - "The direct policy/biotopes lane remains README plus zero-byte marker only."
  - "The eighteen Rego files under policy/domains/habitat are explicitly PROPOSED default-only stubs; their presence does not establish rule semantics, native Habitat Rego tests, bundle activation, evaluator binding, or runtime enforcement."
  - "policy/sensitivity/habitat contains only a marker; habitat_classes.yaml is a separate PROPOSED placeholder."
  - "This revision changes documentation only and creates no policy decision, rule behavior, schema, contract, fixture, evaluator, release, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Biotopes Policy Compatibility Guardrail

`policy/biotopes/`

> **One-line purpose.** Preserve a fail-closed compatibility and drift-prevention boundary for a non-canonical topic-name path without creating a sovereign `biotopes` policy family, sensitivity authority, object authority, release gate, or publication surface.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#2-current-repository-state)
[![Version: v0.3](https://img.shields.io/badge/version-v0.3-1f6feb?style=flat-square)](#26-changelog)
[![Lane: two tracked files](https://img.shields.io/badge/lane-README%20%2B%20marker-0969da?style=flat-square)](#15-directory-contract)
[![Authority: compatibility only](https://img.shields.io/badge/authority-compatibility%20only-d97706?style=flat-square)](#5-authority-boundary)
[![Habitat rules: default-only stubs](https://img.shields.io/badge/Habitat%20rules-default--only%20stubs-8250df?style=flat-square)](#17-validation-and-test-strategy)
[![Runtime: evaluator unbound](https://img.shields.io/badge/runtime-evaluator%20unbound-b42318?style=flat-square)](#8-runtime-policy-interface)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#12-lifecycle-and-public-trust-boundary)

> [!IMPORTANT]
> **Safe current conclusion:** at `main@a893b30f4dd1edfed151620c529734f4fd789a89`, the complete direct lane is this README plus a zero-byte marker. The adjacent Habitat policy lane contains eighteen Rego files, but every one is an explicitly proposed default-only stub: sixteen expose only `default allow := false` and two expose only `default deny := false`. No native Habitat Rego test, active bundle, evaluator binding, emitted `PolicyDecision`, governed consumer, release integration, or production enforcement was established.

> [!CAUTION]
> `Biotope` is not KFM ubiquitous language and is not an accepted object family. Operational policy must name the canonical object being evaluated—such as `HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, or a Flora-owned `Vegetation Community` reference—and preserve its owner, source role, classifier version, time, evidence, rights, sensitivity, review, and release state.

> [!WARNING]
> File presence is not policy activation. A default-only Rego stub, passing schema or validator, green workflow, merged pull request, generated receipt, API scaffold, or map rendering must never be interpreted as an allow decision, evidence closure, review approval, release, or publication.

**Evidence snapshot:** `main@a893b30f4dd1edfed151620c529734f4fd789a89` · target baseline blob `cb1f7144290951fc8209f094b3ccacfacf006c92` · no overlapping open PR at preflight.

---

## Quick jump

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Current repository state](#2-current-repository-state)
- [3. Conflict statement](#3-conflict-statement)
- [4. Bounded context and language](#4-bounded-context-and-language)
- [5. Authority boundary](#5-authority-boundary)
- [6. Operating invariants](#6-operating-invariants)
- [7. Placement-review dispositions](#7-placement-review-dispositions)
- [8. Runtime policy interface](#8-runtime-policy-interface)
- [9. Required policy inputs](#9-required-policy-inputs)
- [10. Runtime outcome semantics](#10-runtime-outcome-semantics)
- [11. Biotope-like policy concerns](#11-biotope-like-policy-concerns)
- [12. Lifecycle and public trust boundary](#12-lifecycle-and-public-trust-boundary)
- [13. Allowed contents](#13-allowed-contents)
- [14. Prohibited contents](#14-prohibited-contents)
- [15. Directory contract](#15-directory-contract)
- [16. Resolution and migration sequence](#16-resolution-and-migration-sequence)
- [17. Validation and test strategy](#17-validation-and-test-strategy)
- [18. Security, privacy, and information minimization](#18-security-privacy-and-information-minimization)
- [19. Review and separation of duties](#19-review-and-separation-of-duties)
- [20. Correction, supersession, and rollback](#20-correction-supersession-and-rollback)
- [21. Validation commands](#21-validation-commands)
- [22. Definition of done](#22-definition-of-done)
- [23. Open verification register](#23-open-verification-register)
- [24. Evidence ledger](#24-evidence-ledger)
- [25. Maintainer checklist](#25-maintainer-checklist)
- [26. Changelog](#26-changelog)

---

## 1. Purpose and audience

`policy/biotopes/` exists to prevent a requested or legacy topic-name folder from silently becoming policy authority.

The directory may document:

- why *biotope* is a bounded documentation term rather than a canonical KFM policy or object family;
- how biotope-like concerns map to Habitat- and Flora-owned objects;
- why active policy belongs under accepted policy responsibility lanes;
- which shared policy inputs and decisions a future Habitat policy gate must use;
- how sensitive joins, source roles, classifier versions, and public-safe geometry must be handled;
- how the path is redirected, deprecated, retained as a guardrail, or accepted through a governed decision;
- how any migration can be reviewed, audited, corrected, and rolled back.

It does not grant authority merely because it is under the canonical `policy/` root.

**Primary audience**

- Habitat, Flora, and Fauna stewards;
- policy, sensitivity, evidence, release, and security stewards;
- contract and schema reviewers;
- package, pipeline, API, and map maintainers consuming Habitat policy;
- reviewers assessing directory drift;
- maintainers planning migration from compatibility paths.

[Back to top](#top)

---

## 2. Current repository state

Evidence snapshot: `main@a893b30f4dd1edfed151620c529734f4fd789a89`; target baseline blob `cb1f7144290951fc8209f094b3ccacfacf006c92`.

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| `policy/biotopes/` direct inventory | **CONFIRMED exactly two tracked files** | This README and a zero-byte `.gitkeep` are the complete direct lane. No local rule, fixture, test, bundle, decision, release record, or publisher exists. |
| Existing target and history | **CONFIRMED populated v0.2 baseline** | v0.3 reconciles the guardrail in place; it does not create behavior. |
| `contracts/biotopes/` | **CONFIRMED README plus marker** | Compatibility contract guidance exists; it is not semantic authority for a new object family. |
| `schemas/biotopes/` | **CONFIRMED README plus marker** | The index is frozen for new schemas and requires object-by-object routing; it is not machine-shape authority for `Biotope`. |
| Directory governance | **CONFIRMED adopted** | ADR-0029 adopts Directory Rules v2. `policy/` is the singular policy-source root, and this lane requires a `BOUNDARY_COMPACT` contract because authority changes here. |
| Root registry projection | **CONFIRMED `root.policy`** | Policy source is internal, versioned, and durable; the projection creates no local owner, activation, evaluator, decision, or public permission. |
| Habitat Biotopes doctrine | **CONFIRMED draft docs grouping** | `Biotope` is not KFM ubiquitous language and must not introduce independent contract, schema, policy, data, or object-family authority. |
| `policy/domains/habitat/README.md` | **CONFIRMED canonical-placement claim / PROPOSED greenfield scaffold** | It is the current candidate Habitat policy home, but its README does not prove active enforcement. |
| Habitat Rego inventory | **CONFIRMED eighteen default-only proposed stubs** | Sixteen contain only a package declaration plus `default allow := false`; `abstain_on_ambiguous.rego` and `deny_unpublished.rego` contain only package declarations plus `default deny := false` and commented examples. No operative Habitat rule body was established. |
| Habitat sensitivity surfaces | **CONFIRMED marker plus separate placeholder** | `policy/sensitivity/habitat/` contains only `.gitkeep`; sibling `habitat_classes.yaml` is explicitly `PROPOSED`. No dedicated Habitat sensitivity README or active rule was established there. |
| Dedicated Biotopes fixtures/tests | **CONFIRMED absent from exact candidate paths** | `tests/policy/biotopes/` and `fixtures/policy/biotopes/` do not exist in the complete tree. Do not create them merely for topic symmetry. |
| Habitat policy-test lane | **CONFIRMED README plus marker** | `tests/domains/habitat/policy/` documents a proposed test boundary but contains no executable test module. |
| Named Habitat policy tests | **CONFIRMED three docstring-only placeholders** | The modeled-as-critical, occurrence-geoprivacy, and critical-habitat-source-role Python files contain no test functions or assertions. |
| Broad `policy-test` workflow | **CONFIRMED static readiness hold** | It inventories all Rego files but recognizes only the bounded Pass 12 test as a native Rego test; it evaluates no repository-wide or Habitat policy and emits no `PolicyDecision`. |
| `domain-habitat` workflow | **CONFIRMED bounded mixed workflow** | It executes synthetic land-cover materiality validation, while Habitat proof and release dry-run remain explicit holds. It does not evaluate the Habitat Rego stubs. |
| `PolicyInputBundle` | **CONFIRMED semantic contract / permissive PROPOSED schema stub** | The paired schema requires only `id` and permits additional properties; schema validity cannot prove complete policy input. |
| `PolicyDecision` | **CONFIRMED contract and closed PROPOSED schema** | Outcomes are `ANSWER / ABSTAIN / DENY / ERROR` and policy families exclude `biotopes`. Shape validity is not decision authenticity or permission. |
| General policy runtime | **CONFIRMED `0.0.0` placeholder** | `core.py` is comment-only, the namespace initializer is empty, and the root `make policy` target prints a TODO. No general evaluator is established. |
| Governed API | **CONFIRMED fail-closed scaffold** | Three scaffold routes return generic `ABSTAIN` / `NOT_IMPLEMENTED` envelopes; none is a Biotopes or Habitat evaluator. |
| Open-PR overlap | **CONFIRMED none at preflight** | The sole open PR changed Consent files only; no target-path overlap was found. |
| Accepted owners, active bundle, evaluator, required checks, deployment, release integration, public behavior | **UNKNOWN / NEEDS VERIFICATION** | Repository bytes and workflow definitions do not establish production operation or repository-settings significance. |

### Current direct map

```text
policy/biotopes/
├── .gitkeep   # Zero-byte marker; no authority or implementation
└── README.md  # This documentation-only compatibility boundary
```

### Evidence limits and truth labels

- **CONFIRMED** — verified from the pinned repository state in this update.
- **PROPOSED** — a design, rule, placement, fixture, obligation, or implementation step not established as accepted active behavior.
- **PARTIAL** — a bounded implementation or route exists, but its complete authority or enforcement chain is not proved.
- **CONFLICTED** — inspected paths or vocabularies disagree and must not be silently normalized.
- **UNKNOWN** — available evidence is insufficient for a current-state claim.
- **NEEDS VERIFICATION** — a concrete owner, code, runtime, review, ruleset, or release check is required.
- **NOT ESTABLISHED** — the inspected evidence does not support treating a capability as active.

A bounded non-observation is not proof of permanent absence. Re-verify any later branch, bundle, runtime, repository setting, deployment, or external consumer at its own exact revision.

[Back to top](#top)

---

## 3. Conflict statement

The repository currently contains three topic-name compatibility paths:

```text
policy/biotopes/
contracts/biotopes/
schemas/biotopes/
```

The Habitat biotopes document explicitly says that the docs-layer grouping must not create those paths as independent authority. Their simultaneous presence is therefore **drift evidence**, not three-way confirmation that `biotopes` is a canonical family.

The conflict has four dimensions:

| Dimension | Current evidence | Required posture |
|---|---|---|
| Vocabulary | `Biotope` is not KFM ubiquitous language. | Use canonical Habitat/Flora object names in operational artifacts. |
| Responsibility | Policy, contract, and schema compatibility folders exist. | Each stays non-authoritative until redirected or accepted through governance. |
| Domain ownership | Habitat owns typed habitat areas, land-cover observations, and ecological systems; Flora owns vegetation communities. | Policy must preserve owning-lane boundaries. |
| Implementation | No active policy/tests/fixtures are established here. | Do not infer runtime maturity from README presence. |

> [!WARNING]
> Creating matching folders in multiple responsibility roots can make a planning label look like an accepted object family. KFM treats that as authority drift unless an accepted ADR, migration record, contracts, schemas, tests, and steward review establish otherwise.

[Back to top](#top)

---

## 4. Bounded context and language

### Bounded context

Within this README, *biotope-like policy concern* means:

> A policy question about a typed habitat area, land-cover classification, ecological-system classification, or a governed cross-lane join involving those objects.

It does not mean:

- a new domain;
- a new canonical `Biotope` entity;
- a new policy family;
- a new schema or contract family;
- a generic label that erases source role or time;
- a synonym for regulatory critical habitat;
- a synonym for habitat suitability;
- a place to move Flora or Fauna authority into Habitat.

### Operational crosswalk

| Umbrella or external wording | Canonical KFM object / label | Owner | Policy implication |
|---|---|---|---|
| Typed habitat area | `HabitatPatch` | Habitat | Evaluate source, geometry, sensitivity, review, and release state. |
| Land-cover class assignment | `LandCoverObservation` | Habitat | Preserve classifier, version, effective time, and observation character. |
| Ecological-system label | `EcologicalSystem` | Habitat | Preserve source vocabulary, model/context status, vintage, and uncertainty. |
| Floristic plant community | `Vegetation Community` | Flora | Habitat policy may consume a reference; it must not own or redefine it. |
| Regulatory critical habitat | Regulatory designation / source-role label | Habitat context | Never flatten into ecological classification truth. |
| Modeled suitability | `SuitabilityModel`, `Habitat Quality Score` | Habitat suitability concern | Keep model output separate from observed/classified habitat. |
| Sensitive species-habitat join | Habitat object plus public/restricted Fauna or Flora reference | Cross-lane | Exact disclosure fails closed; public-safe transform and review may be required. |

### Language rules

- Use the canonical object name in policy inputs, reason codes, receipts, and tests.
- Use *biotope* only as a documentation grouping or external-vocabulary label.
- Preserve the original classifier and external term through a namespaced source field or crosswalk.
- Do not promote a convenient umbrella term into a shared kernel without a deliberate contract and ADR decision.
- A vocabulary mapping is not evidence that two classifications are ecologically equivalent.

[Back to top](#top)

---

## 5. Authority boundary

This directory may answer:

> **What must a maintainer do when content is proposed under the contested `policy/biotopes/` path?**

It must not independently answer:

> **May this Habitat or Flora object be exposed, rendered, joined, exported, promoted, released, or published?**

That operational question belongs to accepted policy source under the singular `policy/` root, evaluated through an accepted bundle and evaluator against explicit input, normalized into a governed decision, and enforced by the owning consumer and release process.

| Responsibility | Owning surface | Role of `policy/biotopes/` |
|---|---|---|
| Policy source and reviewed bundles | [`policy/`](../README.md) and an accepted child lane | Route by responsibility; never create a second authority or infer activation. |
| Habitat policy source candidate | [`policy/domains/habitat/`](../domains/habitat/README.md) | Point to the current scaffold while preserving its default-only, unbound maturity. |
| Shared sensitivity policy | [`policy/sensitivity/`](../sensitivity/README.md) | Require accepted sensitivity/geoprivacy handling; never invent Habitat rules from a marker or placeholder. |
| Shared policy-object meaning | [`contracts/policy/`](../../contracts/policy/policy_decision.md) | Consume contract semantics; never redefine them. |
| Shared policy-object shape | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/policy_decision.schema.json) | Require the accepted profile; never treat validation as permission. |
| Habitat object meaning and shape | [`contracts/domains/habitat/`](../../contracts/domains/habitat/README.md) and [`schemas/contracts/v1/domains/habitat/`](../../schemas/contracts/v1/domains/habitat/README.md) | Preserve canonical object ownership and maturity. |
| Evaluator helper implementation | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | External implementation surface; currently a placeholder and never policy authority. |
| Governed API | [`apps/governed-api/`](../../apps/governed-api/README.md) | Enforce accepted decisions at the trust membrane; current generic abstain scaffold is not Habitat policy. |
| Enforceability proof | [`tests/`](../../tests/policy/README.md) and accepted fixtures | Prove bounded behavior; test pass is not a decision or release. |
| Lifecycle objects, receipts, and proofs | `data/` responsibility lanes | Supply governed inputs and records; never author policy here. |
| Promotion, release, correction, withdrawal, rollback | `release/` | Own release-facing decisions; policy output is only one required input. |

### BOUNDARY_COMPACT responsibility signature

| Field | Current boundary |
|---|---|
| Purpose and inherited parent | Compatibility and drift guardrail beneath the singular [`policy/`](../README.md) root. |
| Local owner and scope ID | **NEEDS VERIFICATION.** CODEOWNERS routes `/policy/` to `@bartytime4life`; accepted Habitat/Policy stewardship, independent review, and executable local scope remain unproved. |
| Belongs here | This README, a marker, compatibility rationale, placement dispositions, migration/deprecation pointers, evidence ledger, and rollback guidance. |
| Prohibited | Active rules, sovereign `biotopes` family registration, contracts, schemas, fixtures, data, decision instances, receipts, proofs, release records, credentials, sensitive coordinates, or public artifacts. |
| Inputs | Proposed path change, canonical object identity, operation, audience, source role, classifier/time context, evidence, rights, sensitivity, review, release, correction, and rollback context. |
| Outputs | Documentation-only placement disposition, verification item, migration pointer, or drift record; never runtime permission. |
| Exposure | Root projection is `internal`. Public repository visibility and rendered Markdown do not make this a public runtime interface. |
| Mutation and retention | `versioned` and `durable` under `root.policy`; history and supersession remain reviewable. |
| Validation | Exact direct inventory, metadata/Markdown/link checks, no-active-payload guard, reference search, governing-doctrine checks, and exact-head PR CI. |
| Related trust set | Habitat and shared policy source, contracts, schemas, fixtures, tests, evaluator, governed consumer, receipts/proofs, release, correction, and rollback surfaces. |
| Status and open items | **CONFLICTED compatibility guardrail; evaluator unbound.** Ownership, final path disposition, active policy home, normalization, enforcement, external consumers, and release integration remain open. |

This README does not authorize executable policy, bind a runtime package, declare an OPA/Rego package, create a sensitivity tier, make a source authoritative, grant access, release a layer, approve a geoprivacy transform, supersede Habitat/Flora/Fauna authority, resolve schema placement, or create public behavior.

[Back to top](#top)

---

## 6. Operating invariants

1. `Biotope` remains a documentation umbrella unless a governed vocabulary decision accepts it.
2. Canonical object and domain ownership must be explicit in every policy input.
3. Missing source role, rights, classifier version, time, evidence, sensitivity, review, or release context fails closed.
4. Regulatory, modeled, observed, classified, and derived products must remain distinguishable.
5. Public and restricted geometry must never be conflated.
6. A safe source alone does not make a sensitive join safe.
7. A generalized output must be tested for inference and reverse-join risk.
8. Policy consumes EvidenceRef/EvidenceBundle status; it does not fabricate evidence.
9. Policy consumes source and rights posture; it does not declare source authority.
10. Policy may permit an operation; it does not approve publication by itself.
11. `ANSWER` is subject to obligations and downstream release gates.
12. `ABSTAIN`, `DENY`, and `ERROR` remain semantically distinct.
13. AI-generated classification, summary, or confidence cannot create policy authority.
14. Watchers, classifiers, and pipelines are non-publishers.
15. Every active policy decision must be auditable and supersedable.
16. Correction, withdrawal, and rollback paths must survive public release.
17. Compatibility paths must not accumulate executable logic while placement remains unresolved.
18. A path-resolution decision must be reversible.

[Back to top](#top)

---

## 7. Placement-review dispositions

The values below are **documentation and repository-review dispositions**. They are not `PolicyDecision.outcome` values and must not be serialized as runtime authorization.

| Disposition | Meaning | Required action |
|---|---|---|
| `KEEP_GUARDRAIL_ONLY` | The directory remains as a README-only compatibility boundary. | Reject active policy files and keep links current. |
| `REDIRECT_TO_HABITAT_POLICY` | Proposed content belongs under the accepted Habitat policy lane. | Move through a reviewed migration; update references and rollback notes. |
| `REDIRECT_TO_SHARED_POLICY` | Proposed content belongs in a shared sensitivity, render, access, or capability policy family. | Route by responsibility, not topic. |
| `REQUIRE_ADR` | A proposal would make `biotopes` a canonical policy/object family or change domain placement. | Do not merge until an accepted ADR resolves authority and migration. |
| `DEPRECATE_PATH` | The path should stop receiving changes and eventually be removed. | Add deprecation and forward links; preserve history. |
| `ABSTAIN_PLACEMENT` | Evidence is insufficient to choose the destination safely. | Create no new authority; record a verification or drift item. |
| `ERROR_INSPECTION` | Repository or validation inspection failed. | Stop; report the failure; never default to acceptance. |

A placement review should record:

```yaml
path: policy/biotopes/
disposition: KEEP_GUARDRAIL_ONLY
basis:
  - docs/domains/habitat/sublanes/biotopes.md
  - docs/doctrine/directory-rules.md
reviewers:
  - habitat_steward
  - policy_steward
migration_ref: null
rollback_ref: null
notes: "Documentation disposition only; not a runtime PolicyDecision."
```

[Back to top](#top)

---

## 8. Runtime policy interface

Any future active Habitat policy triggered by a biotope-like concern must use explicit, accepted policy interfaces:

```text
PolicyInputBundle or accepted successor
  -> selected immutable policy bundle and evaluator
  -> engine-native result
  -> accepted normalization
  -> PolicyDecision
  -> obligation-capable governed consumer
  -> separate review and release gates
```

### Shared input contract

[`PolicyInputBundle`](../../contracts/policy/policy_input_bundle.md) is the current semantic input carrier. Its paired schema remains a permissive `PROPOSED` stub requiring only `id`, so semantic completeness cannot be inferred from schema validity.

A future evaluator must not:

- silently fetch missing evidence, rights, source, sensitivity, review, or release facts;
- read RAW, WORK, QUARANTINE, candidate, or internal stores as a public shortcut;
- infer rights from public availability;
- infer sensitivity from absence of a flag;
- trust map/UI state as policy truth;
- use model prose or embeddings as authorization;
- mutate the input bundle during evaluation;
- treat a default-only Rego result as a complete decision.

### Shared decision contract

[`PolicyDecision`](../../contracts/policy/policy_decision.md) requires `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, and `evaluated_at`. The paired schema permits only:

```text
outcome:       ANSWER | ABSTAIN | DENY | ERROR
policy_family: promotion | access | render | capability | consent | sensitivity
```

`biotopes` is not a permitted policy family. Engine-native `allow` or `deny` booleans must not be serialized into this closed outward schema without an accepted, tested normalization that preserves reasons, obligations, input identity, bundle/evaluator identity, and failure semantics.

| Operation | Candidate shared family | Boundary example |
|---|---|---|
| Public map display | `render` or `sensitivity` | Generalize a supported Habitat geometry before display. |
| Restricted steward review | `access` | Permit a bounded reviewer to inspect restricted support. |
| Cross-lane analytical join | `capability` and/or `sensitivity` | Deny or restrict a join that could reveal protected occurrence detail. |
| Public export | `sensitivity` or `capability` | Deny exact-coordinate export or require an accepted transform. |
| Promotion/release handoff | `promotion` plus prerequisite policy results | Require evidence, rights, sensitivity, review, correction, and rollback closure. |

Exact family composition remains **PROPOSED / NEEDS VERIFICATION** until accepted executable policy and integration tests establish it.

### Current implementation qualification

- all eighteen inspected Habitat Rego files are default-only proposed stubs;
- no native Habitat Rego test was found;
- the broad `policy-test` workflow performs static readiness checks and evaluates no Habitat rule;
- the general policy runtime remains a comment-only `0.0.0` placeholder;
- the root `make policy` command still prints a TODO;
- the governed API emits generic `ABSTAIN / NOT_IMPLEMENTED` scaffolds and has no Habitat route;
- no accepted bundle selector, evaluator binding, decision receipt, obligation interpreter, cache invalidation, correction propagation, promotion integration, or production consumer was established.

Therefore this section defines a future interface boundary, not current runtime behavior.

[Back to top](#top)

---

## 9. Required policy inputs

A biotope-like policy evaluation should receive explicit, inspectable context.

| Input family | Minimum meaning | Fail-closed condition |
|---|---|---|
| Operation | Render, join, query, export, review, promote, release, correct, or rollback. | Missing or generic operation. |
| Audience | Public, restricted reviewer, steward, internal service, export consumer, map runtime, AI adapter. | Missing or ambiguous audience. |
| Canonical object | `HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, or cross-lane reference. | Umbrella `biotope` supplied without canonical object/owner. |
| Domain owner | Habitat, Flora, Fauna, or another owning lane. | Ownership unresolved or reassigned by convenience. |
| Source descriptor | Source ref, role, rights, active/deprecated state, caveats. | Missing source role or rights. |
| Classification | Class scheme, classifier/version, source vocabulary, crosswalk version. | Missing classifier or unverified crosswalk. |
| Temporal context | Observation/effective time, source vintage, retrieval time, release time, correction time where material. | Requested time unsupported or stale. |
| Evidence context | EvidenceRef/Bundle refs, resolver state, citation status, quality limits. | Evidence unresolved for consequential claim. |
| Geometry context | Precision, spatial support, generalization/redaction state, target scale. | Exact or overly precise geometry without safe disposition. |
| Sensitivity context | Restricted habitat, species/plant join, cultural/tribal, landowner, infrastructure, inference risk. | Missing or unresolved sensitivity. |
| Rights context | License, redistribution, attribution, export restrictions, embargo. | Unknown rights or terms. |
| Review context | Steward review refs, required separation of duties, unresolved flags. | Required review absent. |
| Release context | Candidate/release state, ReleaseManifest ref, correction and rollback refs. | Public exposure without release support. |
| Evaluator context | Policy bundle id/hash/version and evaluator mode. | Missing, stale, or unverifiable evaluator. |
| Prior decisions | Superseded decisions and their timestamps. | Stale decision treated as current. |

### No hidden facts

A policy evaluation must not silently derive an allow from:

- directory location;
- map visibility;
- a public-looking source URL;
- a classifier confidence score;
- a lack of known sensitive occurrences;
- a missing policy field;
- a previous release of a related layer;
- an AI summary;
- a cached decision whose inputs changed.

[Back to top](#top)

---

## 10. Runtime outcome semantics

Runtime policy uses only the shared finite outcomes.

| Outcome | Biotope-like meaning | Required downstream behavior |
|---|---|---|
| `ANSWER` | The evaluated operation is policy-supported for the supplied context. | Proceed only after obligations and all other gates pass. |
| `ABSTAIN` | Admissible support is missing, stale, conflicted, or too incomplete to decide safely. | Do not render, join, export, answer, or promote; surface a bounded explanation. |
| `DENY` | A policy rule blocks the operation. | Block it; expose only a safe reason; preserve audit context. |
| `ERROR` | Input shape, evaluator integrity, bundle freshness, wiring, or process failed. | Fail closed; do not convert to `ANSWER` or hide as ordinary denial. |

### Illustrative reason codes

These are **PROPOSED** until a reason-code registry is accepted.

```text
BIOTOPE_UMBRELLA_TERM_NOT_OPERATIONAL
CANONICAL_OBJECT_OWNER_MISSING
SOURCE_ROLE_UNRESOLVED
RIGHTS_UNRESOLVED
CLASSIFIER_VERSION_MISSING
CROSSWALK_UNVERIFIED
MODEL_OBSERVATION_COLLAPSE
REGULATORY_ECOLOGICAL_COLLAPSE
SENSITIVE_JOIN_EXACT_LOCATION
PUBLIC_GEOMETRY_NOT_GENERALIZED
REVERSE_JOIN_DISCLOSURE_RISK
EVIDENCE_UNRESOLVED
REVIEW_REQUIRED
RELEASE_STATE_MISSING
POLICY_BUNDLE_STALE
EVALUATOR_FAILURE
```

### Illustrative obligations

```text
attach_citation
preserve_source_role
preserve_classifier_version
label_model_output
label_regulatory_designation
generalize_geometry
redact_coordinates
aggregate_cells
withhold_exact_location
block_reverse_join
require_habitat_steward_review
require_flora_steward_review
require_fauna_steward_review
attach_rights_notice
block_export
delay_publication
attach_correction_lineage
verify_rollback_target
```

Obligations are mandatory. A caller unable to enforce one must fail closed.

[Back to top](#top)

---

## 11. Biotope-like policy concerns

### 11.1 Source-role anti-collapse

A classification source may be:

- an observation;
- an authoritative regulatory designation;
- a model output;
- a contextual dataset;
- a steward-reviewed interpretation.

Policy must preserve the declared role. It must deny or abstain when a user-facing product would imply a stronger role than the source supports.

### 11.2 Classifier, vocabulary, and vintage

Typed habitat claims are time- and classifier-dependent.

Policy should require:

- source vocabulary identifier;
- classifier or class-scheme version;
- mapping/crosswalk version;
- effective or observation time;
- source vintage;
- uncertainty and review status where material.

A class crosswalk is not lossless by default. Ambiguous or many-to-many mappings should be surfaced, not collapsed.

### 11.3 Observation versus model

`LandCoverObservation`, interpreted ecological systems, suitability models, and remote-sensing derivatives have different knowledge character.

Public policy should deny:

- a model shown as observed truth;
- a classified raster shown as a field-verified boundary without support;
- an uncertainty surface omitted where it materially changes interpretation;
- a derived habitat patch presented without lineage to source data and transform receipts.

### 11.4 Regulatory versus ecological meaning

Regulatory critical habitat must remain a regulatory designation. It must not be relabeled as:

- observed occupancy;
- ecological-system truth;
- modeled suitability;
- species range;
- general habitat type.

The reverse confusion is also unsafe: an ecological classification must not imply legal status.

### 11.5 Sensitive cross-lane joins

The highest-risk biotope-like operations are joins that reveal restricted information indirectly.

Examples:

- habitat polygon plus rare-species occurrence;
- ecological-system cell plus nest/den/roost/hibernaculum/spawning site;
- vegetation community plus rare-plant record;
- small habitat patch plus private-land or steward identity;
- repeated generalized releases that permit differencing to recover a hidden site;
- suitability or density surfaces that expose a protected population cluster.

Default posture:

```text
exact sensitive disclosure -> DENY
insufficient sensitivity context -> ABSTAIN
evaluator or transform failure -> ERROR
public-safe generalized result -> ANSWER only with obligations and release gates
```

### 11.6 Geometry and scale

A public-safe transform should be evaluated for:

- coordinate precision;
- polygon simplification;
- aggregation cell size;
- buffer or displacement method;
- minimum feature count;
- small-area uniqueness;
- edge and topology leakage;
- tile-level and zoom-level exposure;
- differencing across releases;
- reversibility or inference attacks.

A `RedactionReceipt` or accepted equivalent should bind the transform, input digest, output digest, reason, policy decision, reviewer, and release context where required. Exact object name and schema remain **NEEDS VERIFICATION**.

### 11.7 Rights and source terms

Public availability is not rights clearance.

Policy must check:

- redistribution;
- derivative-work permission;
- attribution;
- service or download terms;
- embargo;
- export restrictions;
- source-required disclaimers;
- controlled biodiversity or steward terms.

Unknown rights fail closed.

### 11.8 Temporal support and stale state

A habitat classification may become stale because:

- the source published a new vintage;
- the classifier changed;
- land cover changed;
- a crosswalk was corrected;
- a regulatory designation changed;
- a sensitivity rule changed;
- a source was withdrawn or deprecated.

Policy should distinguish stale-but-inspectable material from current public truth. Re-release requires a new decision, not mutation of the prior record.

### 11.9 AI and automated classification

AI may help:

- draft crosswalk candidates;
- summarize evidence;
- identify classification conflicts;
- propose review notes;
- explain public-safe limitations.

AI must not:

- accept a new canonical class;
- decide source authority;
- infer rights or consent;
- lower sensitivity;
- approve a geoprivacy transform;
- promote or release a layer;
- replace missing field verification;
- expose hidden coordinates through explanation.

[Back to top](#top)

---

## 12. Lifecycle and public trust boundary

Biotope-like records follow the Habitat lifecycle. This compatibility path introduces no new stage.

```text
source admission
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> release review
  -> PUBLISHED
  -> correction / withdrawal / rollback
```

| Stage | Policy concern | Required posture |
|---|---|---|
| Source admission / RAW | Source identity, role, rights, sensitivity, citation, retrieval integrity. | Admit only through governed source records; unresolved terms hold or deny activation. |
| WORK / QUARANTINE | Normalization, classifier/crosswalk mapping, geometry, time, uncertainty, sensitive joins. | Failures remain quarantined with reasons; no public exposure. |
| PROCESSED | Canonical Habitat objects, evidence refs, validation reports, public-safe candidates. | Policy pass does not imply release. |
| CATALOG / TRIPLET | Discovery and relation projections. | Catalog/graph carriers cannot replace evidence or reveal restricted joins. |
| Release review | Evidence, rights, sensitivity, review, transform receipts, correction, rollback. | Promotion is a governed state transition. |
| PUBLISHED | Governed API, released artifacts, public-safe tiles/layers/exports. | Serve only the approved public-safe representation. |
| Correction / rollback | Changed source, classifier, policy, sensitivity, or evidence. | Preserve prior release lineage and withdrawal/supersession status. |

### Trust membrane

Public clients must not:

- import or execute policy from this compatibility directory;
- read internal Habitat stores directly;
- infer permission from a policy file path;
- query restricted occurrence records to enrich public habitat objects;
- render an unreleased candidate;
- access internal reason details that reveal sensitive facts.

[Back to top](#top)

---

## 13. Allowed contents

Only non-authoritative compatibility material belongs here while the conflict remains unresolved.

| Allowed content | Conditions |
|---|---|
| This README | Must retain non-canonical and guardrail posture. |
| Placement notes | Must cite Directory Rules and current repository evidence. |
| Migration plan | Must identify source, destination, reviewers, compatibility window, and rollback. |
| Deprecation notice | Must forward-link to the accepted policy home. |
| Drift-register pointer | Must not duplicate the register as a local authority. |
| Evidence ledger | Must distinguish repository facts from proposals. |
| Review checklist | Must not act as executable policy. |
| Historical compatibility note | Must be clearly superseded or retained as lineage. |

A file proposed here should pass this test:

> Is its primary responsibility documenting the compatibility-path conflict rather than deciding an operational policy outcome?

If the answer is no, redirect it.

[Back to top](#top)

---

## 14. Prohibited contents

| Prohibited content | Correct responsibility |
|---|---|
| OPA/Rego or equivalent active policy module | Accepted Habitat/shared policy lane |
| Policy bundle or bundle manifest | Accepted policy runtime/bundle lane |
| New `biotopes` policy family | Requires contract/schema/ADR change; default deny |
| Habitat or Flora object contract | Owning domain under `contracts/` |
| JSON Schema | Owning domain under accepted `schemas/contracts/v1/...` home |
| SourceDescriptor or source record | `data/registry/sources/` |
| RAW/WORK/QUARANTINE/PROCESSED data | Owning lifecycle lane under `data/` |
| Catalog, triplet, tile, layer, or public export | Governed lifecycle/release homes |
| EvidenceBundle, proof, or receipt instance | Accepted proof/receipt home |
| ReleaseManifest or PromotionDecision | `release/` |
| Sensitive coordinates or restricted joins | Restricted lifecycle/proof systems, never this README lane |
| Runtime evaluator code | `packages/policy-runtime/` or accepted implementation home |
| Governed API route | `apps/governed-api/` |
| UI rule that bypasses policy | Governed app surface consuming decisions |
| Credentials, secrets, tokens, keys | Approved secret management, never repository docs |

[Back to top](#top)

---

## 15. Directory contract

Directory Rules assign files by responsibility, not topic. This path sits under the correct policy root but remains a contested compatibility lane. Its `BOUNDARY_COMPACT` map must show direct children only.

### Current direct lane

```text
policy/biotopes/
├── .gitkeep   # Zero-byte compatibility marker; no authority
└── README.md  # Documentation-only drift and placement guardrail
```

### Current compatibility cluster

| Path | Complete direct inventory at the pinned snapshot | Authority posture |
|---|---|---|
| `policy/biotopes/` | `.gitkeep`, `README.md` | Compatibility policy guardrail only. |
| `contracts/biotopes/` | `.gitkeep`, `README.md` | Compatibility semantic warning only. |
| `schemas/biotopes/` | `.gitkeep`, `README.md` | Frozen compatibility/migration index only. |

Three matching names are drift evidence, not three-way confirmation of a canonical family.

### Existing candidate owning surfaces

| Surface | Current evidence | Limitation |
|---|---|---|
| `policy/domains/habitat/` | README, eighteen default-only Rego stubs, and marker-only subdirectories | Proposed scaffold; no accepted Habitat bundle/evaluator or native Rego test. |
| `policy/sensitivity/habitat/` | Zero-byte marker only | No dedicated README or active Habitat sensitivity rule. |
| `policy/sensitivity/habitat_classes.yaml` | Explicit `PROPOSED` placeholder | No class semantics or enforcement. |
| `contracts/domains/habitat/` | Typed Habitat semantic contracts | Individual maturity varies; semantic meaning is not policy execution. |
| `schemas/contracts/v1/domains/habitat/` | Typed Habitat machine-shape surfaces | Individual maturity varies; schema validity is not policy permission. |
| `tests/domains/habitat/policy/` | README plus marker | Proposed test boundary; no executable module in that child lane. |

Do not create missing symmetry. First determine whether a concern belongs to Habitat-owned policy, shared sensitivity/access/render/capability policy, a contract/schema family, executable tests, or a separately governed release surface.

### Path decision rule

| Proposed change | Required response |
|---|---|
| Edit this guardrail without changing authority | Scoped docs review plus Habitat/Policy awareness; preserve exact evidence and rollback. |
| Add an active file here | Reject or hold. Route by responsibility unless an accepted ADR and migration explicitly canonicalize this lane. |
| Graduate a Habitat Rego stub | Require accepted semantics, package/entrypoint identity, native positive/negative tests, fixtures, bundle membership, evaluator binding, normalization, consumer enforcement, receipts, and rollback. |
| Add Habitat sensitivity rules | Verify accepted owner and home; marker or placeholder presence is insufficient. |
| Make `policy/biotopes/` canonical | Require accepted ADR, object/policy migration manifest, consumer inventory, deprecation window, correction propagation, and rollback proof. |
| Remove this directory | Confirm zero writers/consumers and link closure; preserve history and a forward target. |
| Create another parallel Biotopes root | Deny absent accepted authority and a bounded compatibility plan. |

[Back to top](#top)

---

## 16. Resolution and migration sequence

Use the smallest reversible sequence.

### Phase 0 — Freeze authority

- Keep this directory README-only.
- Reject active policy, schemas, contracts, data, and release objects here.
- Record any discovered consumers or imports.

### Phase 1 — Inventory

Inspect:

- all files under the three compatibility paths;
- references to those paths in docs, code, configs, tests, workflows, and generated artifacts;
- active policy package names;
- Habitat policy and sensitivity conventions;
- current schema/contract pairs;
- source and release dependencies.

### Phase 2 — Choose disposition

Select one:

1. **Guardrail retained** — no consumers; path remains a warning/index.
2. **Redirect and deprecate** — accepted Habitat/shared policy home exists.
3. **Migrate active content** — move with tests and compatibility notes.
4. **Canonicalize by ADR** — exceptional; requires proof that a distinct biotopes policy family is necessary and non-duplicative.
5. **Remove** — after references are migrated and rollback is defined.

### Phase 3 — Implement the owning policy

For active policy, require together:

- semantic contract alignment;
- schema alignment;
- synthetic valid/invalid fixtures;
- evaluator implementation;
- reason-code and obligation vocabulary;
- negative-first tests;
- governed API/release integration tests;
- audit and supersession behavior;
- documentation and ownership updates.

### Phase 4 — Migrate references

- update imports and configuration;
- update docs and examples;
- add deprecation or alias window only if necessary;
- prevent new writes to the old path;
- validate no public/runtime surface resolves policy from the compatibility folder.

### Phase 5 — Prove rollback

- retain old commit/blob references;
- define rollback command or revert target;
- test fallback without restoring parallel authority;
- preserve prior PolicyDecision and release history;
- record the reason for reversal.

[Back to top](#top)

---

## 17. Validation and test strategy

### Confirmed current test and workflow posture

| Surface | What exists | What it proves |
|---|---|---|
| `policy/biotopes/` | README and marker only | No local executable coverage or policy payload. |
| `tests/policy/biotopes/` | No path in the complete tree | No dedicated cross-cutting Biotopes test lane. |
| `fixtures/policy/biotopes/` and `fixtures/policy/habitat/` | No paths in the complete tree | No dedicated policy fixture family at those exact homes. |
| `tests/domains/habitat/policy/` | README and marker | Proposed testing responsibility only. |
| Three named Habitat policy Python files | Docstring-only placeholders | No assertions, case matrix, or policy execution. |
| Eighteen Habitat Rego files | Package declaration plus one default each | Parseable-looking source presence only; no operative case rules or complete decision semantics. |
| `policy-test` workflow | Static inventory/readiness checks | It preserves the general OPA hold and evaluates no Habitat policy. |
| `domain-habitat` workflow | Synthetic land-cover materiality validation plus proof/release holds | Bounded contract/fixture evidence, not Biotopes policy or public authorization. |
| General policy runtime | Comment-only `core.py` and `0.0.0` package | Placeholder identity only. |
| Governed API boundary tests | Generic abstain routes and structural guards | Fail-closed scaffold containment, not Habitat policy enforcement. |

A green repository or pull-request check must be interpreted at its exact workflow scope. It does not activate these stubs.

### Required guardrail tests

The following remain **PROPOSED** until placed under an accepted test owner:

| Test | Required result |
|---|---|
| Complete direct inventory contains only allowed compatibility documentation and marker files. | Pass; an unexpected active payload fails. |
| No bundle, evaluator, runtime import, or consumer selects `policy/biotopes/`. | Pass; operational dependency is a boundary failure. |
| No contract/schema registry creates `Biotope` as an object or policy family without accepted governance. | Pass or explicit migration hold. |
| Each Habitat Rego stub remains visibly proposed until graduated with operative rules and native tests. | Pass; silent graduation fails. |
| `biotopes` is absent from the closed `PolicyDecision.policy_family` vocabulary. | Pass. |
| Compatibility links, forward targets, deprecation notes, and rollback references resolve. | Pass. |
| Public examples contain no real restricted coordinates or reverse-inference payloads. | Pass. |

### Future policy negative cases

| Scenario | Required fail-closed posture |
|---|---|
| Umbrella term supplied without canonical object and owner | `ABSTAIN` or `ERROR` according to input validity |
| Source role unresolved | `ABSTAIN` / `DENY` |
| Rights unresolved | `DENY` or `ABSTAIN` under accepted rights policy |
| Classifier or vocabulary version missing | `ABSTAIN` |
| Unverified crosswalk used as equivalence | `ABSTAIN` / `DENY` |
| Model output presented as observation | `DENY` |
| Regulatory designation presented as ecological classification | `DENY` |
| Public join includes restricted occurrence detail | `DENY` |
| Exact geometry lacks accepted public-safe transform | `DENY` |
| Generalization still permits reverse inference | `DENY` |
| Evidence unresolved or stale | `ABSTAIN` |
| Bundle stale, missing, digest-mismatched, or evaluator unavailable | `ERROR` |
| Release state absent for public render/export | `DENY` / `ABSTAIN` |
| All checks pass with enforceable generalization | `ANSWER` with obligations; still not release approval |

### Fixture posture

Any future fixtures must be synthetic, public-safe, no-network by default, explicit about source role/classifier/time, paired positive/negative, incapable of being mistaken for production records, and free of actual rare-species, rare-plant, cultural, private, or protected coordinates.

Prefer placement by the owning policy/domain responsibility. Candidate paths must be reviewed before creation; the rejected umbrella term must not determine authority.

[Back to top](#top)

---

## 18. Security, privacy, and information minimization

### Sensitive facts in policy inputs

Policy inputs should use references or safe summaries instead of embedding:

- exact restricted coordinates;
- names of private stewards or landowners;
- precise nest/den/roost/hibernaculum/spawning sites;
- rare-plant locations;
- culturally sensitive site details;
- internal enforcement logic;
- credentials or tokens.

### Sensitive facts in decisions

Public `reasons` and `obligations` must not reveal why a location is sensitive in a way that defeats the denial.

Prefer:

```text
reason: SENSITIVE_JOIN_EXACT_LOCATION
```

Avoid:

```text
reason: "Denied because species X nests at coordinates Y."
```

### Logging and audit

- Hash or reference policy inputs where possible.
- Separate public explanations from internal audit details.
- Apply retention and access controls to restricted decision records.
- Do not log raw query payloads containing sensitive geometry.
- Audit override, break-glass, and export attempts.
- Treat decision-cache invalidation as security-relevant.
- Re-evaluate when source, policy, sensitivity, or release state changes.

### Inference and composition risk

A public-safe individual layer may become unsafe when composed with another layer. Policy must consider:

- intersection;
- differencing;
- temporal comparison;
- repeated zoom/query behavior;
- small counts;
- cross-domain joins;
- export of selected subsets;
- AI explanations that combine safe fragments into restricted knowledge.

[Back to top](#top)

---

## 19. Review and separation of duties

### Minimum review roles

| Change | Required review posture |
|---|---|
| Guardrail wording only | Docs steward plus Habitat or Policy steward. |
| Placement disposition | Habitat steward + Policy steward + Directory Rules check. |
| Sensitivity/geoprivacy behavior | Sensitivity steward + Habitat steward; Flora/Fauna steward when their data is involved. |
| Contract/schema change | Contract steward + Schema steward + policy/runtime owner. |
| Executable policy | Policy steward + owning domain + tests/runtime reviewers. |
| Public rendering/export behavior | Policy + release + governed API/map owner. |
| Canonicalizing `biotopes` | ADR reviewers, architecture/docs/policy/domain stewards. |
| Release, correction, withdrawal, rollback | Release steward; separation from sole policy author where maturity requires. |

### Separation rules

The same actor should not unilaterally:

- author a sensitive policy;
- approve the transform it requires;
- approve the release;
- verify rollback;
- close the correction.

Automated checks may support these duties but cannot replace required human review.

[Back to top](#top)

---

## 20. Correction, supersession, and rollback

### Documentation correction

When this README is wrong:

1. identify the unsupported, stale, or overbroad claim;
2. pin the current repository/doctrine evidence;
3. update the truth label and affected evidence entry;
4. preserve prior bytes in Git history;
5. record affected migrations, consumers, decisions, releases, and caches where any exist;
6. prefer a transparent forward correction when a simple revert would reintroduce known inaccuracy.

### Policy supersession

Future active policy must be superseded through versioned source, bundles, decisions, and governed transition records rather than overwritten in place. Material triggers include source-rights change, classifier/crosswalk correction, new sensitivity information, changed geometry transforms, evaluator/bundle vulnerability, owner/path correction, release withdrawal, or correction to domain meaning.

### Migration rollback

A migration away from this path must record source and destination paths, exact blobs/commits, compatibility class/window, writers and consumers, registry/`$ref`/import changes, tests, forward and rollback commands, affected decisions/releases, correction propagation, cache invalidation, and whether old paths are removed, redirected, or retained as guardrails.

Rollback must restore one safe authority surface; it must not restore duplicate authority.

### This README rollback

Before merge, close the draft PR and leave main unchanged. After merge, revert only the scoped README commit or issue a reviewed forward correction, then rerun the exact documentation and hosted checks. The v0.2 preimage is blob `cb1f7144290951fc8209f094b3ccacfacf006c92`. Do not rewrite shared history, activate old stubs, or alter release/publication state as part of documentation rollback.

[Back to top](#top)

---

## 21. Validation commands

The commands below are repository inspection aids. They do not prove runtime enforcement or release authority.

```bash
#: Pin the revision before inspection.
git rev-parse HEAD

#: Verify the three direct compatibility lanes.
git ls-tree -r --name-only HEAD --   policy/biotopes contracts/biotopes schemas/biotopes

#: Inventory Habitat policy source and exact candidate test/fixture homes.
git ls-tree -r --name-only HEAD --   policy/domains/habitat policy/sensitivity/habitat   tests/domains/habitat/policy tests/policy/biotopes   fixtures/policy/biotopes fixtures/policy/habitat

#: Find path, vocabulary, bundle, evaluator, and consumer references.
git grep -nEi   'policy/biotopes|contracts/biotopes|schemas/biotopes|biotope|biotopes'   -- . ':(exclude)policy/biotopes/README.md'

#: Inspect active non-comment statements in Habitat Rego files.
for f in policy/domains/habitat/*.rego; do
  printf '%s\n' "$f"
  sed -E '/^[[:space:]]*(#|$)/d' "$f"
done

#: Confirm the root evaluator hold; this prints TODO at the pinned snapshot.
make policy
```

Documentation checks for this update:

```bash
#: One H1 and one metadata block.
test "$(grep -c '^# ' policy/biotopes/README.md)" -eq 1
test "$(grep -c '\[KFM_META_BLOCK_V2\]' policy/biotopes/README.md)" -eq 1
test "$(grep -c '\[/KFM_META_BLOCK_V2\]' policy/biotopes/README.md)" -eq 1

#: No unexpected active payload in the compatibility lane.
find policy/biotopes -mindepth 1 -maxdepth 1 -type f   ! -name 'README.md' ! -name '.gitkeep' -print

#: No prohibited Biotopes policy-family or package declaration.
git grep -nEi   'policy_family[^[:alnum:]]*[:=][^[:alnum:]]*biotopes?|package[[:space:]].*biotopes?'   -- policy packages apps tests   ':(exclude)policy/biotopes/README.md'
```

Run repository-native Markdown, metadata, link, topology, schema, policy, documentation, and domain checks through the pull request. Interpret each result at its exact scope and classify unrelated inherited failures instead of weakening the guardrail.

[Back to top](#top)

---

## 22. Definition of done

This README revision is done when:

- [x] it preserves the guardrail-only posture;
- [x] it identifies the three-root compatibility conflict;
- [x] it uses canonical Habitat and Flora object ownership;
- [x] it separates placement dispositions from runtime policy outcomes;
- [x] it aligns future runtime behavior to `PolicyInputBundle` and `PolicyDecision`;
- [x] it states that `biotopes` is not a permitted policy family;
- [x] it documents source-role, classifier, temporal, rights, sensitivity, evidence, review, and release inputs;
- [x] it defines sensitive-join and inference-risk controls;
- [x] it records current tests/fixtures as not observed;
- [x] it provides migration, correction, and rollback guidance;
- [x] it does not claim active policy or deployed enforcement.

The path is fully resolved only when:

- [ ] Habitat and Policy stewards choose and record a disposition;
- [ ] all three compatibility paths are inventoried recursively;
- [ ] the accepted active policy home is confirmed;
- [ ] sensitivity-policy placement is resolved;
- [ ] any active content is migrated with tests;
- [ ] reason codes and obligations are registered;
- [ ] fixtures and negative tests exist;
- [ ] runtime and release integration are verified;
- [ ] docs, contracts, schemas, and policy references agree;
- [ ] deprecation and rollback are proven;
- [ ] drift/ADR records are closed or linked.

[Back to top](#top)

---

## 23. Open verification register

| ID | Question | Current status | Evidence needed |
|---|---|---|---|
| `BIO-POL-001` | Should `policy/biotopes/` remain README-only, be deprecated, or be removed? | **PARTIAL — exact two-file lane confirmed; disposition open** | Habitat/Policy owner decision, consumer closure, and migration/deprecation record. |
| `BIO-POL-002` | Is `policy/domains/habitat/` the accepted active home for Habitat policy? | **PLACEMENT CANDIDATE CONFIRMED / ACTIVATION UNKNOWN** | Accepted package/entrypoint convention, bundle/evaluator binding, native tests, consumers, and ADR if required. |
| `BIO-POL-003` | Should Habitat sensitivity live under the domain lane, shared sensitivity lane, or both through explicit composition? | **UNKNOWN** | Policy architecture decision, owner assignments, input/output contract, and bundle composition. |
| `BIO-POL-004` | Are there hidden files or direct consumers under the three compatibility paths? | **DIRECT INVENTORIES CONFIRMED / INBOUND CONSUMERS NEED VERIFICATION** | Content-aware repository and external-consumer search at migration time. |
| `BIO-POL-005` | Is `biotope` retained as docs-only vocabulary, renamed to habitat types, or fully deprecated? | **PROPOSED owner decision** | Habitat/Flora vocabulary decision and reference migration. |
| `BIO-POL-006` | What reason-code registry and obligation interpreter govern Habitat policy? | **UNKNOWN** | Accepted policy contract, evaluator, consumer, tests, and registry. |
| `BIO-POL-007` | Which Habitat contract/schema profiles are production-ready? | **MIXED / NEEDS VERIFICATION** | Per-object contract, schema, fixtures, validators, registry, CI, and consumer evidence. |
| `BIO-POL-008` | What public-safe geometry transforms are accepted? | **UNKNOWN** | Sensitivity policy, transform contract, fixtures, receipts, tests, and release gate. |
| `BIO-POL-009` | How is reverse-join, differencing, and composition risk tested? | **UNKNOWN** | Threat model, synthetic negative fixtures, runtime tests, and correction/rollback behavior. |
| `BIO-POL-010` | Which sources, classifiers, and crosswalks are active for Habitat classifications? | **UNKNOWN** | Source descriptors, activation decisions, rights review, version pins, and release records. |
| `BIO-POL-011` | Is policy-decision caching used, and how is it invalidated? | **UNKNOWN** | Runtime implementation, cache keys, expiry/revocation/correction tests, and receipts. |
| `BIO-POL-012` | Which CI enforces this compatibility boundary and Habitat policy behavior? | **PARTIAL** | `policy-test` is a static readiness hold and `domain-habitat` does not evaluate Rego; a dedicated accepted guard/evaluator workflow and required-check evidence remain absent. |
| `BIO-POL-013` | Does any public API, map, export, graph, search, or AI surface depend on this path? | **UNKNOWN** | Complete internal and external consumer inventory plus runtime tests. |
| `BIO-POL-014` | What rollback target applies to a future path migration? | **README PREIMAGE CONFIRMED / MIGRATION TARGET OPEN** | Accepted migration manifest, zero-writer/consumer checks, forward pointer, and rollback drill. |
| `BIO-POL-015` | What graduates the eighteen Habitat Rego stubs from default-only scaffolds? | **NEEDS VERIFICATION** | Operative rules, stable identities, positive/negative native tests, fixtures, bundle membership, evaluator binding, normalization, consumers, receipts, and rollback. |

[Back to top](#top)

---

## 24. Evidence ledger

Repository evidence inspected for this revision:

| Evidence | Blob / ref | What it supports | Limitation |
|---|---|---|---|
| `policy/biotopes/README.md` v0.2 | `cb1f7144290951fc8209f094b3ccacfacf006c92` | Existing substantive guardrail and rollback preimage. | Documentation only. |
| Complete repository tree | `main@a893b30f4dd1edfed151620c529734f4fd789a89` | Exact direct-lane inventories and candidate-path presence/absence. | Does not inspect external consumers, runtime, or repository settings. |
| `docs/domains/habitat/sublanes/biotopes.md` | `6690a312fcac8464a749f4e8d470404afa80adec` | Docs-only grouping, object crosswalk, no-parallel-authority, sensitivity posture. | Draft docs convention; not executable authority. |
| `contracts/biotopes/README.md` | `4ae31607df03c3d1f4de99b783f88b99946e184a` | Contract compatibility conflict and owning object families. | Does not prove complete semantic maturity. |
| `schemas/biotopes/README.md` | `6a892088d5a0f8be5a8554a8b866ded1da595c8e` | Frozen compatibility/index posture and object-split migration rule. | Does not select or activate schemas. |
| `policy/README.md` | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` | Singular policy root and current policy maturity boundary. | Root doctrine does not activate this child lane. |
| Directory Rules v2 | `fd49a0b83e55cef52c1124281f093e263526898d` | Mandatory contract/schema/policy split and `BOUNDARY_COMPACT` fields. | Does not decide Biotopes disposition or implementation. |
| ADR-0029 | `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` | Accepted exact Directory Rules identity and single human authority. | Does not activate a local policy family. |
| Root registry | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` | `root.policy` responsibility, exposure, mutation, retention, and non-effects. | Machine projection only. |
| `policy/domains/habitat/README.md` | `8456c65196354695b8eb5b8178ecb61cfc12b7dd` | Current canonical-placement claim and explicit greenfield status. | Does not prove rules, bundle, or runtime. |
| Eighteen Habitat Rego files | pinned recursive tree plus exact file reads | All operative content is package declaration plus one default; sixteen default-allow-false and two default-deny-false. | Parse, bundle selection, evaluator execution, and consumers were not established. |
| Habitat sensitivity placeholder | `864474071907172a69a892054662abb38f67cab2` | `habitat_classes.yaml` is explicitly `PROPOSED`. | Supplies no active class semantics or enforcement. |
| Habitat policy-test README | `b09092132fbadefadece14a30c3d0e49a1048c0f` | Proposed test ownership and fail-closed expectations. | Child lane has no executable test module. |
| Three named Habitat policy Python files | `dc61a31288d2c8e47b370179758de60448fa7478`, `03bd5dbcaf46ceb1263cd7f84875d017b1366f4d`, `0446c47b6cb83a35aed3687b60b8072234de912a` | They are docstring-only placeholders. | No assertions or policy execution. |
| `PolicyInputBundle` contract/schema | `545c352681dd0db0cd4d169a5d2f9c364356457c` / `b89db4b1730c61258441e0eed037276b910b1990` | Explicit-input semantics and permissive placeholder shape. | Schema requires only `id`. |
| `PolicyDecision` contract/schema | `ebfe97f98263e6309db6d2772cb2c5e548819650` / `1472d26a42c73f17545b4464a275412ffa1d098e` | Closed outcomes, policy-family enum, reasons, obligations, timestamp. | No decision authenticity, evaluator, or enforcement proof. |
| `policy-test` workflow | `ac8f125e8a4d3634d86f66836d2aa2c0e3925e75` | Static general OPA readiness hold and exact bounded native-test exception. | Evaluates no Habitat policy and emits no decision. |
| `domain-habitat` workflow | `59771c027f688d7028a46c4635c0ec710b34e3ab` | Bounded materiality validation plus explicit proof/release holds. | Does not execute Habitat Rego. |
| Policy runtime core | `e7e14cf39ae6919fbbc80f1b471de6b907292edb` | Comment-only general runtime placeholder. | No evaluator API. |
| Governed API stub | `5d7c137d2e78ddfca35a1356a96333ac2e84952b` | Generic `ABSTAIN / NOT_IMPLEMENTED` envelope. | No Habitat/Biotopes policy or release behavior. |
| Root Makefile | `c5d0aee3de558d76c1e1639bcfd8cf1c71a0d326` | `make policy` remains a TODO echo. | No repository-wide policy execution. |
| CODEOWNERS | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | `/policy/` review routing. | Routing is not accepted role assignment or independent approval. |
| Open pull-request inventory | preflight API read | One open Consent PR; zero target overlap. | Must be refreshed immediately before write. |

### Truth summary

```text
CONFIRMED:
  exact README-plus-marker direct lane
  README-plus-marker compatibility siblings
  accepted singular policy root and BOUNDARY_COMPACT requirement
  docs-only Biotope vocabulary posture
  eighteen Habitat default-only proposed Rego stubs
  placeholder Habitat policy tests
  shared candidate input and decision shapes
  static policy readiness hold
  placeholder policy runtime and generic abstain API scaffold

PROPOSED:
  final path disposition and migration
  active Habitat rule semantics and policy-family composition
  reason codes, obligations, fixtures, tests, bundle/evaluator binding
  decision receipts, consumer enforcement, correction propagation

CONFLICTED:
  parallel topic-name paths versus no-parallel-authority doctrine
  umbrella Biotope term versus canonical Habitat and Flora object families

UNKNOWN / NEEDS VERIFICATION:
  accepted owners and independent approval
  active evaluator, bundle, runtime consumer, and policy receipts
  required-check significance and production enforcement
  external consumers, release integration, deployment, and public behavior
```

[Back to top](#top)

---

## 25. Maintainer checklist

Before editing this directory:

- [ ] Confirm the change is compatibility documentation, not active policy.
- [ ] Read the Habitat biotopes sublane and Directory Rules.
- [ ] Use canonical Habitat/Flora/Fauna object names.
- [ ] Preserve source-role, model/observation, regulatory/ecological, and public/restricted distinctions.
- [ ] Check whether the same concern already belongs under `policy/domains/habitat/`.
- [ ] Do not create a new `biotopes` policy family.
- [ ] Do not add sensitive coordinates or real restricted examples.
- [ ] Separate placement dispositions from runtime outcomes.
- [ ] Use `PolicyInputBundle` and `PolicyDecision` for proposed runtime interfaces.
- [ ] Require explicit rights, evidence, sensitivity, review, and release context.
- [ ] Add negative-first synthetic tests with active policy changes.
- [ ] Update contracts, schemas, docs, fixtures, and runtime adapters together when behavior changes.
- [ ] Record migration and rollback targets.
- [ ] Keep public clients behind governed interfaces.
- [ ] Mark unresolved implementation claims `UNKNOWN` or `NEEDS VERIFICATION`.

## 26. Changelog

### v0.3 — 2026-08-13

- pinned the exact current main commit, target preimage, complete tree, open-PR inventory, and governing evidence;
- adopted the required `BOUNDARY_COMPACT` responsibility signature without changing authority;
- resolved the direct-lane inventory to README plus marker and refreshed both compatibility siblings;
- reconciled the current Habitat policy scaffold: eighteen default-only proposed Rego files, placeholder policy tests, non-evaluating broad workflow, placeholder runtime, and generic abstain API;
- updated Directory Rules from superseded v1.4 evidence to accepted v2 through ADR-0029 and the active root-registry projection;
- preserved the v0.2 purpose, language boundary, placement dispositions, input model, outcome semantics, sensitive-join rules, lifecycle boundary, allowed/prohibited contents, migration phases, negative cases, review separation, correction/rollback discipline, definition of done, verification register, and maintainer checklist;
- changed documentation only.

### No-loss reconciliation ledger

| v0.2 content family | v0.3 disposition |
|---|---|
| Compatibility purpose and non-canonical language | Preserved and tightened. |
| Habitat/Flora object crosswalk and anti-collapse rules | Preserved. |
| Authority, lifecycle, public-trust, sensitivity, rights, AI, and publication boundaries | Preserved and grounded in current evidence. |
| Placement dispositions and migration phases | Preserved. |
| Required inputs, finite outcomes, reasons, and obligations | Preserved as proposed design; current implementation caveats added. |
| Guardrail and runtime negative cases | Preserved; current test gaps made explicit. |
| Review, separation of duties, correction, supersession, and rollback | Preserved; exact v0.2 blob added. |
| Open verification items | Preserved by stable IDs and updated with current partial resolutions. |
| Evidence ledger | Superseded with current blobs, workflows, implementation stubs, and limitations. |

### v0.2 — 2026-07-14

Established the substantive compatibility guardrail, conflict statement, object-family routing, fail-closed policy design, migration sequence, security posture, verification register, and evidence ledger.

[Back to top](#top)

---

## Status summary

`policy/biotopes/` remains a **non-canonical, documentation-only compatibility guardrail**. The complete direct lane is this README plus a marker.

The current Habitat policy candidate contains eighteen explicit default-only stubs, not an accepted evaluator or active policy family. This lane may route Habitat classification, source-role, sensitivity, geoprivacy, and join concerns to their owning surfaces, but it must not acquire executable rules, `biotopes` family registration, contract/schema authority, source or lifecycle data, decision instances, release power, or publication behavior without accepted governance and a reversible migration.

<p align="right"><a href="#top">Back to top</a></p>

---

