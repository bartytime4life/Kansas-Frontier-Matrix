<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/geoprivacy
title: Geoprivacy Policy Routing Index
type: policy-readme
version: v0.2
status: draft; repository-grounded; current-state-reconciled; cross-domain-routing; non-executable; evaluator-unbound; fail-closed; non-release; non-publication
owner: NEEDS VERIFICATION — .github/CODEOWNERS routes /policy/ to @bartytime4life; accepted geoprivacy stewardship and independent approval controls remain unproved
created: 2026-07-24
updated: 2026-08-13
policy_label: repository-facing; geoprivacy; harmful-precision; sensitivity-composition; public-safe-geometry; fail-closed; no-sensitive-parameters; non-release; non-publication
current_path: policy/geoprivacy/README.md
owning_root: policy/
canonical_relationship: PROPOSED cross-domain geoprivacy routing and composition boundary; current PolicyDecision schema does not include a geoprivacy family, and child rule placement across policy/geoprivacy/, policy/sensitivity/, and policy/domains/ remains CONFLICTED / NEEDS VERIFICATION
directory_governance: accepted ADR-0029 adopts Directory Rules v2; policy/ is the singular policy-source root; this same-path BOUNDARY_COMPACT README remains documentation-only
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3e6db4917f89d71331d7f46c08dc64c5000558bf
  target_baseline_blob: a70e691881c0d6bc3e2ebd48290e9c4cb1b90f0e
  target_initial_empty_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  geoprivacy_flora_readme_blob: 47c7c64ff9ca53ab9842bc78b501a64e0bc15167
  sensitivity_root_readme_blob: 06197c7a7255264b94fb9dd8d7f73844cfa35682
  sensitivity_flora_readme_blob: 4c65abec24135f7e4467fd108e163cdce594d5f9
  sensitivity_flora_rego_blob: 2f7e87019f9cd3759c2b8f90ae22183eddea1b1a
  domain_flora_rego_blob: e07d7bd0fe40cf99defb58e43e7b1d8f1e0e536a
  flora_canonical_paths_blob: 367d40d9781387019443fbd5ca98070be543f31c
  policy_input_contract_blob: 545c352681dd0db0cd4d169a5d2f9c364356457c
  policy_input_schema_blob: b89db4b1730c61258441e0eed037276b910b1990
  policy_decision_contract_blob: ebfe97f98263e6309db6d2772cb2c5e548819650
  policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
  policy_runtime_readme_blob: 5a20cfac50a93f497765421b7566559ae49a39b8
  geoprivacy_validator_readme_blob: 15bfbc21cfadea284a17f5807a3c6054ff8894fb
  sensitive_geometry_validator_readme_blob: 166d08f780e96396dbcf8690e3b7218d6d74331b
  geoprivacy_transform_validator_readme_blob: 8f0927ca9b1338b25253e1ed7808b80055d58d8f
  adr_0010_blob: f9145957bf124e3865f5142a02d414f0f685e6a6
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  contributing_blob: de5bf143e601e36a794e6e5442ae8f91c6f75aad
  pull_request_template_blob: c5624d7dbc2b83055421b4fb4542794bafa10bee
  open_overlapping_pull_requests_found: "0"
related:
  - ../README.md
  - ./flora/README.md
  - ../sensitivity/README.md
  - ../sensitivity/flora/README.md
  - ../sensitivity/flora/rare_plant_geoprivacy.md
  - ../sensitivity/flora/rare_plant_geoprivacy.rego
  - ../domains/flora/geoprivacy.rego
  - ../../docs/domains/flora/CANONICAL_PATHS.md
  - ../access/flora-steward/README.md
  - ../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../packages/policy-runtime/README.md
  - ../../tools/validators/geoprivacy/README.md
  - ../../tools/validators/sensitive_geometry/README.md
  - ../../tools/validators/geoprivacy_transform/README.md
  - ../../apps/governed-api/README.md
  - ../../release/README.md
  - ../../.github/CODEOWNERS
  - ../../CONTRIBUTING.md
tags: [kfm, policy, geoprivacy, sensitivity, harmful-precision, public-safe-geometry, rare-species, archaeology, infrastructure, people-dna-land, fail-closed, routing-index]
truth_posture: CONFIRMED populated v0.1 target and exact direct-child inventory, singular policy root, accepted ADR-0029 placement, current policy-root v0.3.1 contract, substantive sensitivity boundary with a proposed scaffold corpus, populated but placement-conflicted Flora child routing README, proposed Flora rule scaffolds in multiple lanes, permissive PolicyInputBundle schema, closed PolicyDecision schema without geoprivacy, validator documentation, proposed ADR-0010, and unproved evaluator/bundle/runtime/release integration / PROPOSED cross-domain routing contract, input profile, evaluation order, reason codes, obligations, tests, convergence plan, correction, revocation, and rollback / UNKNOWN accepted geoprivacy family, canonical child-rule placement, active bundle, native geoprivacy tests, runtime consumers, decision receipts, required-check enforcement, release enforcement, and production operation
notes:
  - "This v0.2 revision reconciles the existing v0.1 README with current main. It creates no executable rule, schema, contract, fixture, validator, policy bundle, release object, or publication state."
  - "This path remains a proposed cross-domain routing and composition boundary. It must not become a second independently evolving source of sensitivity thresholds or domain-specific rule authority."
  - "The current PolicyDecision schema permits promotion, access, render, capability, consent, and sensitivity only; policy_family=geoprivacy is schema-invalid at the inspected snapshot."
  - "No exact sensitive coordinates, generalization radii, grid sizes, geohash precision, reconstruction thresholds, protected identifiers, or operational security details belong in this repository-facing README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geoprivacy Policy Routing Index

> **One-line purpose.** `policy/geoprivacy/` defines the cross-domain routing boundary for location-exposure decisions while keeping domain sensitivity rules, rights checks, access rules, transforms, validation, release, and evidence in their proper responsibility roots.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-verification-boundary)
[![Scope: cross-domain geoprivacy](https://img.shields.io/badge/scope-cross--domain%20geoprivacy-0969da?style=flat-square)](#purpose)
[![Default: fail closed](https://img.shields.io/badge/default-fail%20closed-b42318?style=flat-square)](#default-posture)
[![Evaluator: unbound](https://img.shields.io/badge/evaluator-unbound-d97706?style=flat-square)](#status-and-verification-boundary)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary)

**Quick navigation:** [Purpose](#purpose) · [Status](#status-and-verification-boundary) · [Directory](#current-directory-map) · [Authority](#authority-boundary) · [Boundary contract](#boundary_compact-responsibility-signature) · [Routing](#policy-family-routing) · [Inputs](#policy-input-profile) · [Evaluation](#evaluation-order) · [Outcomes](#normalized-outcomes) · [Reasons](#reason-code-vocabulary) · [Obligations](#obligation-vocabulary) · [Surfaces](#public-surface-controls) · [Validation](#validation-and-acceptance) · [Review](#review-burden) · [Rollback](#correction-revocation-and-rollback) · [Open work](#open-verification-register) · [Evidence ledger](#no-loss-and-evidence-ledger) · [Changelog](#changelog)

> [!IMPORTANT]
> **Safe current conclusion:** this path exists as a proposed cross-domain geoprivacy routing and composition boundary, but current repository evidence does **not** establish an accepted geoprivacy bundle, approved threshold vocabulary, native policy tests, functional evaluator, decision-receipt flow, governed consumer enforcement, release integration, or production operation.

> [!CAUTION]
> **Client-side concealment is never an allow path.** Hidden properties, omitted popups, coarse zoom, style filters, restricted-looking URLs, model refusal prompts, or missing coordinate fields cannot make protected information public-safe. Policy and transformation must run before public delivery, and the produced derivative must be tested for reconstruction risk.

> [!WARNING]
> This repository-facing README must not contain operational values that could help reconstruct sensitive locations. Exact coordinates, named restricted records, generalization radii, grid sizes, geohash precision, buffer parameters, suppression thresholds, or attack-specific detection limits belong only in steward-gated policy and test surfaces.

---

## Purpose

`policy/geoprivacy/` is the policy-family routing index for one bounded question:

> Given an operation, actor, audience, purpose, governed object references, source and evidence posture, rights, sensitivity, requested precision, derivative context, review state, and release state, may location-bearing information be exposed—and under which enforceable obligations?

The lane should provide:

- a stable boundary for cross-domain geoprivacy policy questions;
- a routing map to domain sensitivity, rights, access, transform, validation, and release surfaces;
- a common input profile for harmful-precision and reconstruction-risk evaluation;
- normalized finite outcomes and public-safe reason codes;
- obligations that callers must enforce before serving, exporting, caching, indexing, rendering, or summarizing location-bearing information;
- a convergence plan that prevents duplicate rule authority.

This lane does **not** decide whether a claim is true. It decides whether a requested location-bearing operation is admissible under explicit context.

[Back to top](#top)

---

## Status and verification boundary

Evidence snapshot: `main@3e6db4917f89d71331d7f46c08dc64c5000558bf`; target baseline blob `a70e691881c0d6bc3e2ebd48290e9c4cb1b90f0e`.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `policy/geoprivacy/README.md` | **CONFIRMED populated v0.1 baseline** | This v0.2 revision reconciles the existing README in place; it does not create executable policy behavior. |
| `policy/geoprivacy/` inventory | **CONFIRMED this README plus one `flora/` child** | The parent lane contains no Rego module, bundle manifest, fixture, native policy test, or decision instance. |
| `policy/geoprivacy/flora/` | **CONFIRMED populated routing README plus empty `.gitkeep`** | The child explicitly records placement conflict and non-executable status; it is not an active rule home. |
| Singular `policy/` root | **CONFIRMED v0.3.1 responsibility root** | Policy source belongs under singular `policy/`; one bounded executable lane elsewhere does not activate geoprivacy. |
| Accepted ADR-0029 and Directory Rules v2 | **CONFIRMED placement authority** | `policy/` owns normative admissibility source; this BOUNDARY_COMPACT README cannot become schema, runtime, decision-instance, release, or publication authority. |
| `policy/sensitivity/README.md` | **CONFIRMED substantive v0.1 BOUNDARY_COMPACT contract** | Its tracked corpus is still documented as proposed scaffolding with no accepted general evaluator, bundle, native tests, or consumer binding. |
| Flora rule candidates | **CONFIRMED proposed scaffolds under `policy/sensitivity/flora/` and `policy/domains/flora/`** | Both visible Rego files only declare `default allow := false`; presence does not settle canonical placement or prove evaluation. |
| Flora canonical-path register | **CONFIRMED draft v1.1 register** | Names `policy/sensitivity/flora/` and `policy/domains/flora/` as proposed lanes and leaves their relationship unresolved; it does not establish this parent as an executable rule home. |
| ADR-0010 | **CONFIRMED draft / effective status proposed** | Deny-by-default intent is documented but not accepted or end-to-end enforced. |
| Policy input contract/schema | **CONFIRMED semantic contract plus permissive schema** | The schema requires only `id` and does not machine-enforce a complete geoprivacy input profile. |
| Policy decision contract/schema | **CONFIRMED finite, closed proposed shape** | Outcomes are `ANSWER | ABSTAIN | DENY | ERROR`; policy families exclude `geoprivacy`. |
| Validator documentation | **CONFIRMED parent and related README boundaries** | Concepts and proposed checks exist; complete executable coverage, fixtures, thresholds, and required CI enforcement remain unproved. |
| Active evaluator, bundle, receipts, consumers, release gates | **UNKNOWN / NEEDS VERIFICATION** | No complete governed geoprivacy decision path is established by this README. |

### Current directory map

Verified from the pinned repository tree; deeper Flora detail belongs to the child README.

```text
policy/geoprivacy/
├── README.md    # This cross-domain routing and composition boundary
└── flora/       # Populated, placement-conflicted, non-executable child boundary
```

The child directory's existence does not establish accepted policy placement, a bundle, evaluator behavior, or release authority.

### Evidence limits

**CONFIRMED:** the complete v0.1 target, exact direct-child tree, current policy and sensitivity roots, proposed Flora rule candidates, contracts, schemas, validator READMEs, accepted ADR-0029, proposed ADR-0010, and repository review-routing surfaces named in the evidence snapshot were inspected for this update.

**PROPOSED:** the routing model, input profile, evaluation sequence, generic reason codes, obligations, acceptance tests, and convergence plan below.

**CONFLICTED / NEEDS VERIFICATION:** the authoritative relationship among `policy/geoprivacy/`, `policy/sensitivity/`, and `policy/domains/`, including the single writable home for each domain rule and composition profile.

**UNKNOWN / NEEDS VERIFICATION:** exact package names, entrypoints, bundle manifests, threshold ownership, fixture inventory, native rule tests, runtime imports, caching behavior, audit sinks, review enforcement, required checks, release integration, and production incident response.

This README is boundary documentation, not implementation proof.

[Back to top](#top)

---

## Authority boundary

`policy/geoprivacy/` may own a **cross-domain policy-family index and routing contract**. It must not absorb adjacent responsibilities.

| Responsibility | Owning surface | Role of `policy/geoprivacy/` |
|---|---|---|
| Object and domain meaning | `contracts/` and `docs/domains/` | Consume definitions; never redefine domain truth. |
| Machine-checkable input/output shape | `schemas/contracts/v1/` | Require accepted schemas; never become schema authority. |
| Source identity and source role | `data/registry/sources/` and source contracts | Evaluate supplied references; never invent source authority. |
| Rights and license posture | accepted rights-policy and registry surfaces | Require resolution; never clear rights by assertion. |
| Domain sensitivity rules | `policy/sensitivity/<domain>/` or accepted domain-policy home | Route to the authoritative domain profile; do not copy thresholds. |
| Actor and capability access | `policy/access/` | Require a bounded access decision; do not grant roles here. |
| Transform implementation | `packages/`, `pipelines/`, or accepted implementation root | Require deterministic, receipt-bearing transforms; do not implement them in policy docs. |
| Validation | `tools/validators/`, `tests/`, and `fixtures/` | Declare required checks; do not treat validation as policy authority. |
| Evidence, receipts, and proofs | `data/proofs/`, `data/receipts/`, and contracts/schemas | Require governed references; do not create evidence or receipts here. |
| Public enforcement | governed applications and APIs | Supply normalized decisions; public clients must not read policy source directly. |
| Release, correction, withdrawal, rollback | `release/` | Supply gate inputs; never approve or publish by itself. |

### BOUNDARY_COMPACT responsibility signature

| Field | Current contract |
|---|---|
| Purpose and inherited parent | Inherit the singular admissibility authority of [`policy/`](../README.md); route cross-domain harmful-precision questions without copying domain rules. |
| Local owner | **NEEDS VERIFICATION.** CODEOWNERS routes `/policy/` review to `@bartytime4life`; that is review routing, not accepted stewardship or independent approval. |
| Local scope ID | **NEEDS VERIFICATION.** `kfm://policy/geoprivacy` identifies this document; it is not proof of an accepted machine policy scope or family. |
| Belongs here | Cross-domain routing, composition constraints, public-safe input expectations, proposed normalized reasons and obligations, maturity evidence, and convergence guidance. |
| Prohibited here | Exact protected locations, operational thresholds, copied domain rules, schemas, contracts, runtime code, credentials, real sensitive fixtures, decision instances, release records, and publication state. |
| Inputs | Explicit governed references for operation, actor/audience, object, source/evidence, rights/consent, sensitivity, geometry, joins, transform, review, lifecycle, release, and evaluator context. |
| Outputs | A future accepted evaluator may emit a bounded normalized decision and enforceable obligations; this README emits no decision or artifact. |
| Permitted writers | Reviewable repository changes by authorized contributors; executable policy requires resolved placement, accepted stewardship, tests, consumers, and release evidence. |
| Consumers | Policy runtime and governed applications only after deliberate binding; public clients consume released derivatives through governed interfaces, never this source tree. |
| Exposure | Repository-facing and safe for public review only while operational parameters, protected content, and reconstructive detail remain excluded. |
| Mutation and generation | Human-maintained boundary documentation. Generated rule candidates must retain provenance and cannot be activated by editing this README. |
| Retention and rollback | Preserve history, correction, supersession, and path-decision lineage; roll back through reviewed Git history without erasing safety incidents or release effects. |
| Validation | Structural Markdown, repository-link, metadata, policy-boundary, secret-safety, and representative negative checks; a pass proves only the bounded check. |

### Non-collapse rules

1. A geoprivacy `ANSWER` is not a release approval.
2. A generalized geometry is not public-safe without policy, transform lineage, validation, and required review.
3. A policy result cannot create an `EvidenceBundle`, clear rights, or change source role.
4. A steward's ability to inspect exact coordinates does not make those coordinates public.
5. A hidden map feature is not redacted data.
6. A passed geometry check is not a sensitivity decision.
7. A `RedactionReceipt` records a transform; it does not prove the underlying claim.
8. A release manifest cannot repair missing rights, evidence, or review.
9. Generated language cannot choose a safer location by intuition.
10. A merge, deployment, badge, or green workflow is not publication.

[Back to top](#top)

---

## Operating invariants

This lane preserves the KFM lifecycle and trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Invariant | Geoprivacy consequence |
|---|---|
| Cite or abstain | A location-bearing claim requires resolvable evidence support or an explicit non-answer. |
| Policy-aware, fail-safe defaults | Missing or untrusted context never becomes implicit permission. |
| Public clients use governed interfaces | Public clients cannot inspect canonical or restricted geometry stores directly. |
| Source role does not change by promotion | Modeled, aggregate, administrative, candidate, and observed sources remain distinct. |
| Most restrictive applicable posture wins | Joins and derivatives cannot weaken the strongest relevant restriction. |
| Produced outputs are evaluated | Safety is determined from the emitted geometry and surrounding context, not input fields alone. |
| Promotion is governed | A transform or policy decision cannot promote or publish by itself. |
| Corrections are first-class | Increased restriction, withdrawal, revocation, and cache invalidation preserve lineage. |
| Determinism where practical | The same governed inputs, policy version, transform version, and release profile should reproduce the same result. |
| AI is interpretive only | AI receives public-safe, released context; it does not inspect or infer protected locations. |

[Back to top](#top)

---

## Default posture

The default posture is **no public or semi-public location exposure until the operation-specific policy context is complete and the safest permissible representation is established**.

A request should return `ABSTAIN`, `DENY`, or `ERROR` rather than `ANSWER` when any required context is missing, malformed, stale, conflicted, unsupported, unreviewed, or cannot be evaluated safely.

### Default-deny classes

The following classes require deny-by-default or equally fail-safe treatment when precise exposure could cause harm:

- rare, protected, collectable, or culturally sensitive species;
- archaeology, burial, sacred, heritage, and looting-risk locations;
- living-person, family, DNA/genomic, health, or consent-sensitive locations;
- critical infrastructure, operational dependencies, vulnerabilities, and continuity assets;
- private or steward-restricted land and access-controlled source material;
- exact locations derived from restricted joins even when each input appears benign alone;
- any derivative that can reconstruct a protected location through repeated releases, overlays, graph relations, search, tiles, screenshots, or model context.

This list is a routing trigger, not a complete classification scheme. Domain stewards and accepted policy profiles own the actual disposition.

[Back to top](#top)

---

## Policy-family routing

The parent index should route policy questions without becoming a duplicate rule store.

| Policy question | Preferred policy family | Current posture |
|---|---|---|
| Is the object or place sensitive? | `policy/sensitivity/<domain>/` or accepted cross-domain profile | Mixed; shared root is substantive boundary documentation, while its tracked rule corpus remains proposed scaffolding. |
| May this actor inspect restricted geometry? | `policy/access/<role-or-capability>/` | Some documentation exists; enforcement remains unproved. |
| Do source terms permit the requested derivative? | accepted rights/admissibility profile under `policy/` | NEEDS VERIFICATION by source and operation. |
| What public precision is permitted? | domain sensitivity profile plus cross-domain geoprivacy composition | PROPOSED routing; `geoprivacy` is not a current PolicyDecision family and thresholds must not be duplicated here. |
| Is a transform acceptable? | geoprivacy policy + transform contract + validator + receipt requirement | Implementation and rule bindings NEED VERIFICATION. |
| Does a join or derivative increase sensitivity? | cross-domain composition policy using most-restrictive propagation | PROPOSED; representative tests required. |
| May the result enter a public surface? | geoprivacy + rights + evidence + review + release-gate composition | No complete enforced path proved. |
| Must prior exposure be revoked or withdrawn? | correction/withdrawal/rollback policy and release surfaces | Requires tested operational integration. |

### Child-lane posture

The following child lanes are **not automatically authorized by this README**:

- `flora/` — populated, placement-conflicted, non-executable child boundary; its relationship to `policy/sensitivity/flora/` and `policy/domains/flora/` remains unresolved;
- future domain or composition lanes for fauna, habitat, archaeology, infrastructure, or people-DNA-land;
- tile, graph, search, vector, export, screenshot, or AI-surface profiles;
- cross-domain join profiles.

Before adding an executable child rule, maintainers should identify one authoritative home, document precedence and composition, and migrate rather than copy existing rules.

[Back to top](#top)

---

## Policy input profile

A geoprivacy evaluation should consume an explicit, versioned input bundle. It must not silently fetch missing facts or infer clearance from absence.

> [!NOTE]
> **Current machine limitation:** the inspected PolicyInputBundle schema requires only `id` and permits additional properties. The richer profile below is a proposed semantic requirement, not a machine-enforced current shape.

| Input class | Minimum governed context | Fail-closed trigger |
|---|---|---|
| Operation | capability, request ID, evaluation time, intended action | unknown or overly broad operation |
| Actor and audience | subject/service class, purpose, public/restricted/steward audience | missing or stale identity context |
| Object and scope | stable refs, domain, spatial/temporal scope, requested precision | raw payload substituted for governed references |
| Source and evidence | SourceDescriptor refs, source roles, EvidenceBundle state, citations, freshness | unresolved role, missing evidence, stale support |
| Rights and consent | license/terms, redistribution, attribution, consent applicability/revocation | unknown, restricted, expired, revoked, unsupported |
| Sensitivity | protected class, steward disposition, cultural/sovereignty context, current classification | missing or conflicted classification |
| Geometry | internal geometry ref, source precision, uncertainty, requested public representation | exact content copied into public input or logs |
| Join and derivative context | contributing datasets, inherited restrictions, reconstruction-risk surfaces | strongest restriction absent or weakened |
| Transform context | requested method, transform version, prior output, receipt expectation | unapproved, nondeterministic, or receiptless transform |
| Review state | required reviewer classes, review record refs, expiry | missing, self-approved, stale, or wrong reviewer |
| Lifecycle and release | current stage, candidate/release IDs, correction and rollback refs | skipped lifecycle or missing release context |
| Policy execution | bundle ID/version/digest, evaluator profile, entrypoint, input hash | unaccepted or non-replayable execution context |

The policy input should carry references rather than copying protected coordinates or sensitive payloads into decision logs.

[Back to top](#top)

---

## Evaluation order

A governed evaluator should apply an explicit sequence and preserve every hold, denial, and obligation.

```text
1. validate request and evaluator context
2. resolve operation, actor, audience, and purpose
3. resolve object, source role, evidence, rights, and consent
4. resolve sensitivity and harmful-precision posture
5. propagate restrictions from joins and derivatives
6. evaluate requested public precision and surface
7. require an approved deterministic transform when needed
8. require transform receipt, validation, and specialist review
9. require lifecycle, release, correction, expiry, and rollback support
10. return a normalized finite outcome with reasons and obligations
```

### Evaluation rules

- Missing evaluator or bundle identity should not fall back to permissive behavior.
- Unknown rights should not be converted into attribution-only obligations.
- Missing sensitivity context should not be interpreted as non-sensitive.
- Public exact geometry should require explicit operation-specific support, not a default.
- Generalization must be evaluated against reconstruction risk across all served surfaces.
- A more restrictive source, domain, relation, or review state should not be weakened by aggregation.
- Policy exceptions must be explicit, time-bounded, purpose-bounded, reviewable, auditable, and revocable.
- Any error that prevents safe evaluation returns `ERROR`, not `ANSWER`.

[Back to top](#top)

---

## Normalized outcomes

KFM's common normalized outward vocabulary is:

| Outcome | Geoprivacy meaning |
|---|---|
| `ANSWER` | The requested operation is admissible under the supplied context and all listed obligations remain enforceable. |
| `ABSTAIN` | The evaluator cannot safely decide because support is missing, stale, conflicted, unresolved, or outside scope. |
| `DENY` | The requested exposure is prohibited under the current operation, audience, precision, rights, sensitivity, review, or release context. |
| `ERROR` | The request, schema, evaluator, bundle, dependency, or execution failed; the caller must not infer permission. |

### Important interpretation

An `ANSWER` should be read as **"the bounded operation may proceed under these obligations"**, not as:

- the claim is true;
- rights are permanently cleared;
- exact geometry is public;
- the record is released;
- the transform is complete;
- the object is safe for every audience or surface;
- the result may be cached indefinitely;
- a human reviewer may be bypassed.

Engine-native decisions may differ internally, but public and shared consumers should receive the normalized contract required by the accepted policy-decision surface.

> [!IMPORTANT]
> **Decision-family compatibility:** the current closed PolicyDecision schema has no `geoprivacy` family. A conforming implementation must either compose geoprivacy posture into an accepted family such as `sensitivity`, or deliberately version the contract, schema, fixtures, consumers, and migration. It must not emit schema-invalid `policy_family: geoprivacy` records by convention.

[Back to top](#top)

---

## Reason-code vocabulary

Reason codes should be stable, public-safe, operation-specific, and free of protected content.

### Deny or abstain reasons

- `geoprivacy_context_incomplete`
- `source_role_unresolved`
- `evidence_unresolved`
- `rights_unknown`
- `consent_missing_or_revoked`
- `sensitivity_unresolved`
- `protected_precision_denied`
- `public_exact_geometry_not_allowed`
- `join_inherits_stronger_restriction`
- `derivative_reconstruction_risk`
- `transform_required`
- `transform_not_approved`
- `transform_receipt_missing`
- `specialist_review_required`
- `review_missing_or_stale`
- `release_state_missing`
- `correction_or_withdrawal_pending`
- `policy_bundle_unaccepted`
- `evaluator_unavailable`
- `input_invalid`

### Answer reasons

- `public_representation_allowed`
- `generalized_representation_allowed`
- `aggregate_representation_allowed`
- `withheld_geometry_descriptor_allowed`
- `restricted_review_access_allowed`
- `time_bounded_exception_allowed`

Reason codes do not disclose the sensitive class, precise location, protected identifier, threshold crossed, or exact transform parameter unless the audience and policy explicitly permit that detail.

[Back to top](#top)

---

## Obligation vocabulary

An `ANSWER` may carry one or more enforceable obligations.

| Obligation | Required caller behavior |
|---|---|
| `use_public_safe_geometry_only` | Resolve only the approved public-safe geometry reference. |
| `withhold_geometry` | Return no geometry; provide only an approved safe descriptor. |
| `preserve_source_role` | Keep observed, modeled, aggregate, candidate, and other roles distinct. |
| `preserve_evidence_refs` | Carry resolvable evidence references without exposing restricted evidence. |
| `attach_transform_receipt` | Link the accepted redaction/generalization/aggregation receipt. |
| `require_specialist_review` | Block serving until the named review class is satisfied. |
| `restrict_audience` | Enforce the approved audience and purpose. |
| `deny_bulk_export` | Prevent bulk download, enumeration, or automated extraction. |
| `disable_sensitive_caching` | Apply approved cache controls and expiry. |
| `exclude_from_search_index` | Keep the object out of public search and autocomplete. |
| `exclude_from_graph_projection` | Do not emit relations that reconstruct protected locations. |
| `exclude_from_vector_or_ai_context` | Keep protected content out of embeddings, retrieval, prompts, and model logs. |
| `sanitize_logs_and_errors` | Emit only safe IDs, digests, and reason codes. |
| `preserve_correction_lineage` | Carry correction, withdrawal, and supersession references. |
| `recheck_on_policy_or_source_change` | Invalidate prior decisions when governing context changes. |
| `require_release_gate` | Treat policy success only as one input to governed release. |

Callers must fail closed when they cannot enforce an obligation.

[Back to top](#top)

---

## Public-surface controls

Geoprivacy applies to every derivative surface, not only API coordinates.

| Surface | Required geoprivacy question |
|---|---|
| Governed API | Does the payload expose, link, or permit retrieval of protected geometry or identifiers? |
| MapLibre tiles and layers | Can source data, tile boundaries, feature density, zoom behavior, or styling reveal location? |
| Screenshots and print exports | Can exported pixels, labels, legends, or metadata reconstruct protected places? |
| Search and autocomplete | Do result ordering, snippets, counts, or suggestions reveal restricted presence? |
| Graph and triplet projections | Do relations connect a protected object to an identifiable place? |
| Vector indexes and embeddings | Can retrieval, similarity, metadata, or prompt context reconstruct location? |
| Focus Mode and AI | Does generated text name, infer, narrow, or triangulate protected places? |
| Catalogs and manifests | Do bounds, asset names, source URLs, counts, or previews reveal sensitive scope? |
| Logs, traces, receipts, and errors | Do diagnostics echo protected payloads, identifiers, or before/after geometry? |
| Caches and CDNs | Can stale or withdrawn sensitive outputs remain retrievable? |
| Repeated releases | Can differences between releases reverse-engineer the original location? |

Public-surface validation should inspect the produced artifact and surrounding metadata, not only the original record.

[Back to top](#top)

---

## Transform boundary

Policy selects or requires an admissible transform profile; implementation performs it; validators check it; receipts record it; release governs exposure.

```text
governed restricted geometry reference
  -> accepted composed PolicyDecision carrying geoprivacy posture
  -> deterministic transform implementation
  -> public-safe candidate + transform receipt
  -> validators inspect produced geometry and reconstruction risk
  -> specialist review where required
  -> release candidate and promotion gates
  -> governed public interface
```

### Transform constraints

- Do not transform by generating a plausible replacement location.
- Do not use random jitter as an undocumented default.
- Do not expose before-and-after coordinate pairs in public artifacts.
- Do not let client code perform consequential redaction.
- Do not overwrite restricted canonical geometry with a public derivative.
- Do not reuse one transform profile across domains without specialist review.
- Do not treat cartographic simplification as a geoprivacy transform unless policy explicitly governs it.
- Do not consider a transform complete until the output, receipt, review, and release references agree.

[Back to top](#top)

---

## Validation and acceptance

Validation proves bounded behavior. It does not define policy, create evidence, approve release, or make protected information public-safe.

### Minimum representative tests

| Test family | Required result |
|---|---|
| Missing source role or evidence | `ABSTAIN` or `DENY`, never implicit `ANSWER` |
| Unknown rights or revoked consent | fail closed |
| Missing sensitivity context | fail closed |
| Public exact request for protected precision | `DENY` |
| Approved generalized candidate with required receipt and review | bounded `ANSWER` with obligations |
| Join with a more restrictive input | strongest restriction preserved |
| Reverse-engineerable derivative | `DENY` or hold |
| Protected content in logs/errors | test failure |
| Protected content in search/graph/vector/AI projection | test failure or policy denial |
| Missing transform receipt | fail closed |
| Stale review or expired exception | `ABSTAIN` or `DENY` |
| Evaluator unavailable or bundle mismatch | `ERROR`, never permissive fallback |
| Correction or withdrawal | prior public alias invalidated |
| Rollback drill | prior safe release restored without re-exposing withdrawn content |

### Acceptance matrix

Before executable geoprivacy policy is treated as active, require:

- [ ] one accepted policy-family placement and precedence model;
- [ ] accepted policy input and decision contracts and schemas;
- [ ] an accepted evaluator version and immutable bundle identity;
- [ ] domain and cross-domain profiles with no duplicated thresholds;
- [ ] positive, negative, error, expiry, correction, and rollback tests;
- [ ] synthetic or already public-safe fixtures only;
- [ ] deterministic transforms and receipt schemas;
- [ ] validators for geometry, joins, surfaces, and reconstruction risk;
- [ ] governed API and review-console consumers that enforce obligations;
- [ ] audit events that do not leak protected content;
- [ ] release-gate integration and observed dry-run evidence;
- [ ] required CI checks and review protection;
- [ ] cache invalidation, withdrawal, and rollback drills;
- [ ] independent specialist and release review where significance requires it.

A README, Rego file, schema pass, unit test, commit, or pull request alone cannot satisfy this matrix.

[Back to top](#top)

---

## Threat model

The geoprivacy family should defend against:

- direct exact-coordinate disclosure;
- indirect disclosure through source-native IDs or linked records;
- joins that narrow a location beyond the approved representation;
- repeated-release differencing;
- tile-boundary, density, zoom, or feature-count inference;
- graph-neighbor and search-result triangulation;
- vector retrieval and AI synthesis of protected places;
- cache retention after withdrawal;
- privileged role abuse and bulk enumeration;
- stale policy, review, rights, consent, or sensitivity state;
- permissive fallback during evaluator or dependency failure;
- duplicate rule homes with diverging thresholds;
- logs, traces, screenshots, fixtures, and error messages that leak protected content.

Threat details and operational thresholds should remain in restricted review artifacts, not this public README.

[Back to top](#top)

---

## Review burden

| Change class | Minimum review posture |
|---|---|
| README-only clarification | Policy-aware maintainer plus docs review. |
| Generic reason or obligation vocabulary | Policy, contract/schema, runtime consumer, and validator review. |
| Domain sensitivity profile | Affected domain steward plus sensitivity/privacy and policy review. |
| Rare species or habitat composition | Flora/fauna/habitat specialists plus sensitivity and release review. |
| Archaeology or culturally sensitive place | Archaeology/cultural-sovereignty/rights-holder review plus policy and release. |
| Living-person or DNA/genomic location | Privacy, consent, genomics, security, policy, and release review. |
| Critical infrastructure | Security and infrastructure specialist plus policy and release review. |
| Transform algorithm or reconstruction test | Implementation owner, security/privacy reviewer, validator owner, domain steward, and release reviewer. |
| Bundle, evaluator, signing, or activation | Policy-runtime, supply-chain/security, validation, operations, and release review. |
| Public API, map, search, graph, vector, export, or AI enforcement | Policy plus affected application, security/privacy, domain, validation, and release review. |
| Correction, withdrawal, or rollback | Policy, evidence, operations, release, and affected domain reviewers with separation of duties where required. |

CODEOWNERS routing, an administrator role, or a PR approval does not by itself prove accepted stewardship or sufficient independent review.

[Back to top](#top)

---

## Correction, revocation, and rollback

Geoprivacy decisions are time-bound and context-bound. They must be invalidated when:

- source rights or terms change;
- consent is revoked or expires;
- sensitivity classification increases;
- new evidence creates join-induced or derivative risk;
- a transform is found reversible or insufficient;
- a reviewer decision is corrected;
- an object or source is withdrawn;
- a policy or evaluator version is superseded;
- a public artifact is discovered to expose protected information.

### Required response

1. deny or hold new access;
2. invalidate cached decisions and public aliases;
3. quarantine or withdraw affected derivatives;
4. emit correction or withdrawal records;
5. preserve evidence, review, policy, and release lineage;
6. identify a safe rollback target;
7. rebuild public artifacts from governed inputs where appropriate;
8. verify that maps, APIs, catalogs, search, graph, vector, exports, and AI surfaces no longer expose the material;
9. record the incident and remediation without reproducing protected content.

Rollback restores a known safe governed state. It must not silently restore an earlier artifact that carries the same exposure flaw.

### Documentation rollback

Before merge, close or abandon the draft pull request and its feature branch. After an authorized merge, revert the README commit or restore the v0.1 baseline blob `a70e691881c0d6bc3e2ebd48290e9c4cb1b90f0e` through a reviewable pull request. The original empty blob `8b137891791fe96927ad78e64b0aad7bded08bdc` is historical lineage, not the current rollback target.

This documentation-only revision activates no rules. If future implementation depends on this lane, rollback must include contracts, schemas, policy bundles, selectors, transforms, caches, receipts, consumer behavior, migrations, and release effects—not merely this Markdown file.

[Back to top](#top)

---

## Convergence and migration plan

The repository currently exposes multiple plausible geoprivacy and sensitivity homes. The pinned tree confirms rule-shaped Flora candidates under both `policy/sensitivity/flora/` and `policy/domains/flora/`, plus non-executable routing documentation under `policy/geoprivacy/flora/`. The safe path is convergence, not duplication.

1. Inventory current geoprivacy, sensitivity, rights, access, transform, validator, test, and runtime surfaces, beginning from the pinned multi-lane Flora evidence.
2. Identify the authoritative policy-family relationship through an accepted ADR or equivalent reviewed decision.
3. Keep `policy/geoprivacy/` as an index/composition family only if that role is accepted.
4. Choose one authoritative home for each domain threshold and rule profile.
5. Migrate with history and compatibility notes; do not copy rules into parallel active homes.
6. Define bundle composition, precedence, and most-restrictive propagation.
7. Align contracts, schemas, fixtures, validators, consumers, receipts, and release gates.
8. Add deprecation and rollback records for retired paths.
9. Prove equivalent or safer behavior before removing compatibility files.
10. Keep public documentation free of protected operational parameters.

Until convergence is accepted, ambiguous rule placement should fail closed and be recorded as `NEEDS VERIFICATION` or `CONFLICTED`.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Closure evidence |
|---|---|---|---|
| `GEOPRIV-001` | Is `policy/geoprivacy/` an accepted policy family, a routing index, or a transitional path? | **NEEDS VERIFICATION** | accepted ADR or governing policy-root decision |
| `GEOPRIV-002` | What is the precedence and composition relationship with `policy/sensitivity/` and `policy/domains/`? | **NEEDS VERIFICATION** | bundle contract and native policy tests |
| `GEOPRIV-003` | Which child lanes exist and which are authoritative? | **PARTIAL / NEEDS VERIFICATION** | direct child inventory is confirmed; accepted ownership and canonical rule-home decision remain required |
| `GEOPRIV-004` | Which evaluator, language, version, and entrypoint are accepted? | **UNKNOWN** | pinned evaluator and observed test run |
| `GEOPRIV-005` | Which immutable bundle manifest and signing path are accepted? | **UNKNOWN** | bundle digest, signature, selector, and activation record |
| `GEOPRIV-006` | Does the policy input schema enforce the full geoprivacy context? | **NO at the pinned snapshot / NEEDS DECISION** | current schema requires only `id`; close with an accepted version plus valid/invalid fixtures |
| `GEOPRIV-007` | Which policy family, generic reason codes, and obligations are canonical? | **PROPOSED / SCHEMA-CONFLICTED** | current schema excludes `geoprivacy`; close with contract/schema review, migration, and consumer tests |
| `GEOPRIV-008` | Which domains and cross-domain joins require native policy profiles? | **NEEDS VERIFICATION** | domain steward matrix and synthetic fixtures |
| `GEOPRIV-009` | Which transform and receipt contracts are accepted? | **NEEDS VERIFICATION** | contracts, schemas, deterministic implementation, tests |
| `GEOPRIV-010` | Which validators inspect tiles, search, graphs, vectors, exports, screenshots, and AI reconstruction risk? | **UNKNOWN** | executable inventory and coverage report |
| `GEOPRIV-011` | Which governed applications consume and enforce geoprivacy obligations? | **UNKNOWN** | implementation, contract tests, and runtime evidence |
| `GEOPRIV-012` | Which audit sink records decisions without leaking protected content? | **UNKNOWN** | threat-reviewed audit schema and tests |
| `GEOPRIV-013` | Which CI checks are required and branch-protected? | **UNKNOWN** | workflow runs and ruleset evidence |
| `GEOPRIV-014` | What are decision expiry and revocation-latency requirements? | **UNKNOWN** | operational contract and tested invalidation drill |
| `GEOPRIV-015` | Who owns policy, privacy/security, sensitivity, rights, domain, runtime, validation, and release approval? | **NEEDS VERIFICATION** | accepted stewardship and separation-of-duties record |
| `GEOPRIV-016` | Has a public-surface withdrawal and rollback drill succeeded end to end? | **UNKNOWN** | signed drill report and verified artifact state |

[Back to top](#top)

---

## Last reviewed

**2026-08-13 — v0.2 current-state reconciliation against `main@3e6db4917f89d71331d7f46c08dc64c5000558bf`.**

Reviewed:

- the complete v0.1 target at blob `a70e691881c0d6bc3e2ebd48290e9c4cb1b90f0e` and its historical empty predecessor;
- the exact `policy/geoprivacy/` direct-child tree and the populated, placement-conflicted Flora child README;
- the current policy-root v0.3.1 and sensitivity-root v0.1 BOUNDARY_COMPACT contracts;
- proposed rule candidates under `policy/sensitivity/flora/` and `policy/domains/flora/`, plus the draft Flora canonical-path register;
- the PolicyInputBundle and PolicyDecision contracts and schemas;
- policy-runtime, governed-API, release, and geoprivacy-related validator boundaries;
- proposed ADR-0010, accepted ADR-0029, the adopted Directory Rules v2 `policy/` and `BOUNDARY_COMPACT` requirements, CODEOWNERS, CONTRIBUTING, and the pull-request template;
- current open pull requests and target history for overlap.

This review confirms current files, placement conflict, scaffold maturity, and the schema incompatibility of `policy_family: geoprivacy`. It does not accept this lane as an executable policy family, select a canonical domain-rule home, activate a bundle, approve operational thresholds, authorize protected-location access, clear rights or consent, approve release, or create publication state.

[Back to top](#top)

---

## No-loss and evidence ledger

| Material element | v0.2 disposition |
|---|---|
| Stable path, document ID, H1, and existing heading anchors | **Preserved** |
| Cross-domain routing purpose and non-ownership boundaries | **Preserved and reverified** |
| Fail-closed posture, protected classes, threat model, public-surface controls, and transform constraints | **Preserved** |
| Proposed input profile, evaluation order, reasons, obligations, tests, convergence, correction, and rollback | **Preserved as proposed** |
| Stale claim that the current target is empty | **Corrected to the populated v0.1 baseline** |
| Current direct-child contents | **Added from the pinned tree** |
| Stale claim that the shared sensitivity README is a stub | **Corrected to its substantive v0.1 boundary while retaining its documented scaffold-corpus posture** |
| Flora child and duplicate-looking rule-home evidence | **Reconciled as populated/non-executable child documentation plus proposed scaffolds under sensitivity and domain lanes** |
| PolicyDecision family compatibility | **Added: current closed schema excludes `geoprivacy`** |
| BOUNDARY_COMPACT coverage | **Added explicit owner/scope, belongs/prohibited, inputs/outputs, exposure, mutation, retention, writers, consumers, and validation posture** |
| Runtime, policy, schema, contract, validator, release, and publication behavior | **Unchanged; no implementation claimed** |
| Rollback target | **Corrected from the historical empty blob to the v0.1 baseline** |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| v0.1 | 2026-07-24 | Completed the previously empty tracked README with a cross-domain geoprivacy routing boundary, fail-closed posture, proposed inputs/reasons/obligations, public-surface controls, validation expectations, and rollback discipline. | Historical empty blob `8b137891791fe96927ad78e64b0aad7bded08bdc` |
| v0.2 | 2026-08-13 | Reconciles current repository state, records the exact direct-child map and accepted placement authority, distinguishes populated documentation from proposed rule scaffolds, adds decision-family compatibility and BOUNDARY_COMPACT fields, repins evidence, and corrects rollback. No executable behavior changes. | Restore v0.1 blob `a70e691881c0d6bc3e2ebd48290e9c4cb1b90f0e` through a reviewed revert or forward fix |

[Back to top](#top)

---

## Maintainer checklist

Before adding executable policy or new child lanes:

- [ ] resolve the policy-family placement and precedence;
- [ ] identify one authoritative rule home per domain and composition;
- [ ] verify the evaluator, bundle, schemas, fixtures, and native tests;
- [ ] keep exact locations and operational thresholds out of public docs and fixtures;
- [ ] preserve the most restrictive applicable disposition across joins and derivatives;
- [ ] require deterministic transforms and governed receipts;
- [ ] validate every public surface, not only API coordinates;
- [ ] enforce obligations in governed applications;
- [ ] prove expiry, correction, withdrawal, cache invalidation, and rollback;
- [ ] keep release approval and publication outside this directory.

> **Final boundary:** evidence supports claims; policy decides bounded admissibility; transforms produce public-safe candidates; validators test declared behavior; release governs publication; public clients consume only released outputs through governed interfaces.

[Back to top](#top)
