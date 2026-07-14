<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/biotopes
title: Biotopes Policy Compatibility Guardrail
type: policy-readme
version: v0.2
status: draft; CONFLICTED; compatibility-guardrail; non-authoritative
owners: OWNER_TBD — Habitat steward · Policy steward · Sensitivity steward · Flora steward · Fauna steward · Release steward · Docs steward
created: 2026-06-15
updated: 2026-07-14
policy_label: restricted
supersedes: v0.1 (2026-06-15)
path: policy/biotopes/README.md
related:
  - ../README.md
  - ../domains/habitat/README.md
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
  - ../../docs/architecture/trust-membrane.md
  - ../../packages/policy-runtime/README.md
  - ../../apps/governed-api/README.md
  - ../../tests/policy/README.md
tags: [kfm, policy, biotopes, habitat, compatibility, guardrail, non-canonical, sensitivity, geoprivacy, source-role, classifier-vintage, deny-by-default, migration, rollback]
notes:
  - "v0.2 preserves policy/biotopes as a compatibility guardrail and does not activate it as a policy family or executable policy lane."
  - "Biotopes evidence was first inspected on main at commit 65a0d9f6159efa03aba0711d38a51eb203079c3f and rechecked unchanged at branch base 30f7bdda720310a14376791b6d1e02e1d3639e91."
  - "The repository contains parallel compatibility READMEs at policy/biotopes, contracts/biotopes, and schemas/biotopes, while Habitat biotopes doctrine explicitly forbids those topic-name paths from becoming independent authority."
  - "policy/domains/habitat/README.md exists as a PROPOSED greenfield Habitat policy scaffold; policy/sensitivity/habitat/README.md was not found at the tested path."
  - "PolicyInputBundle and PolicyDecision are the shared policy contracts. Runtime-facing PolicyDecision outcomes are ANSWER | ABSTAIN | DENY | ERROR; biotopes is not a permitted policy_family value."
  - "No active policy module, package-local biotopes policy test lane, biotopes fixture lane, deployed evaluator wiring, release behavior, or public runtime behavior is claimed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Biotopes Policy Compatibility Guardrail

`policy/biotopes/`

> Compatibility and drift-prevention boundary for a **non-canonical topic-name path**. This directory may explain why biotope-like policy concerns must be evaluated through Habitat-owned objects and the shared KFM policy contracts; it must not become a sovereign `biotopes` policy family, sensitivity authority, object authority, or publication gate.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-1f6feb)
![posture](https://img.shields.io/badge/posture-compatibility__guardrail-orange)
![authority](https://img.shields.io/badge/authority-non--canonical-critical)
![conflict](https://img.shields.io/badge/path-CONFLICTED-yellow)
![default](https://img.shields.io/badge/default-fail__closed-d62728)
![publication](https://img.shields.io/badge/publication-not__authorized-critical)

> [!IMPORTANT]
> **Repository branch base:** `main` at `30f7bdda720310a14376791b6d1e02e1d3639e91`  
> **Initial biotopes evidence snapshot:** `65a0d9f6159efa03aba0711d38a51eb203079c3f`; the target blob remained unchanged at the branch base  
> **Owning root:** `policy/` — admissibility and exposure policy  
> **Owning domain:** Habitat, through canonical Habitat object families  
> **Current path posture:** compatibility guardrail only  
> **Runtime policy family:** never `biotopes`; use an accepted shared family such as `sensitivity`, `render`, `capability`, or `access` according to the evaluated operation  
> **Implementation depth:** active policy code, fixtures, tests, evaluator wiring, and deployed enforcement are not established by this README

> [!CAUTION]
> `Biotope` is not KFM ubiquitous language and is not an accepted object family. In operational policy, use the canonical object being evaluated—`HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, or a Flora-owned `Vegetation Community` reference—and preserve its owning lane, source role, classifier version, time, evidence, rights, sensitivity, review, and release state.

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

The table separates repository evidence from proposed policy design.

| Surface | Evidence at inspected ref | Status | Consequence |
|---|---|---|---|
| `policy/biotopes/README.md` | Existing v0.1 guardrail README was read from `main`. | **CONFIRMED** | This revision updates the guardrail in place. |
| [`policy/README.md`](../README.md) | Declares singular `policy/` authority for allow, deny, restrict, abstain, redaction, sensitivity, promotion, and release policy. | **CONFIRMED root README / status PROPOSED** | A child path still requires a coherent policy responsibility; topic naming alone is insufficient. |
| [`docs/domains/habitat/sublanes/biotopes.md`](../../docs/domains/habitat/sublanes/biotopes.md) | States that `Biotope` is not KFM ubiquitous language and the sublane is a docs-only grouping over canonical objects. | **CONFIRMED document / sublane convention PROPOSED** | This path must not create independent policy authority. |
| [`contracts/biotopes/README.md`](../../contracts/biotopes/README.md) | Exists as a non-canonical compatibility contract guardrail. | **CONFIRMED compatibility README** | The same drift exists under the contract root; it is not corroboration for a new object family. |
| [`schemas/biotopes/README.md`](../../schemas/biotopes/README.md) | Exists as a schema compatibility index and forbids new canonical schema definitions there without a decision. | **CONFIRMED compatibility README** | The same drift exists under the schema root; it must not become machine-shape authority. |
| [`policy/domains/habitat/README.md`](../domains/habitat/README.md) | Exists and calls itself the canonical Habitat policy lane, with status `PROPOSED (greenfield scaffold)`. | **CONFIRMED path / PROPOSED scaffold** | It is the strongest repository candidate for Habitat-owned policy, but implemented behavior remains unverified. |
| `policy/sensitivity/habitat/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | Do not claim a dedicated Habitat sensitivity sublane currently exists. |
| [`contracts/policy/policy_input_bundle.md`](../../contracts/policy/policy_input_bundle.md) | Shared semantic input contract exists; paired schema is a permissive placeholder requiring only `id`. | **CONFIRMED contract / schema incomplete** | Future policy must supply explicit context without pretending the schema enforces all semantics. |
| [`contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md) | Shared decision contract and strict paired schema exist. | **CONFIRMED contract and field surface** | Runtime-facing outcomes and policy-family values must align with the shared contract. |
| `tests/policy/biotopes/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | No dedicated biotopes policy-test lane is documented. |
| `fixtures/policy/biotopes/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | No dedicated synthetic fixture lane is documented. |
| Open pull requests containing `biotopes` | Search returned no open PR before this update. | **CONFIRMED search result** | No known concurrent PR was found for the target. |
| Active policy modules under this directory | Indexed search found the guardrail README, not executable policy. Complete recursive tree evidence was unavailable. | **NOT OBSERVED / search-limited** | Do not claim active policy or categorical directory emptiness beyond tested paths. |
| Runtime evaluation and public enforcement | No runtime logs, deployed bundles, audit receipts, or route behavior were inspected. | **UNKNOWN** | This README is not implementation proof. |

### Evidence boundary

```text
guardrail README present                  = CONFIRMED
parallel compatibility roots present     = CONFIRMED
Habitat policy scaffold present          = CONFIRMED path / PROPOSED behavior
dedicated Habitat sensitivity README     = NOT FOUND at tested path
shared PolicyInputBundle contract        = CONFIRMED
shared PolicyDecision contract/schema    = CONFIRMED
active biotopes policy module             = NOT OBSERVED
dedicated biotopes tests/fixtures         = NOT OBSERVED
runtime enforcement                       = UNKNOWN
release behavior                          = UNKNOWN
public API/UI behavior                     = UNKNOWN
```

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

> **May this Habitat object be exposed, rendered, joined, exported, promoted, or published?**

That operational question belongs to active policy under an accepted Habitat or sensitivity policy lane, consuming shared policy contracts and returning a governed `PolicyDecision`.

```text
policy/biotopes/                  = compatibility and drift guardrail
policy/domains/habitat/           = existing Habitat policy scaffold; runtime depth unknown
policy/sensitivity/<accepted>/    = sensitivity/geoprivacy policy if and when established
contracts/policy/                 = shared policy-object meaning
schemas/contracts/v1/policy/      = shared policy-object machine shape
contracts/domains/habitat/        = Habitat object meaning
schemas/contracts/v1/domains/...  = Habitat object machine shape, subject to schema-home decisions
packages/policy-runtime/          = reusable evaluation helpers
apps/governed-api/                = governed executable interface
tests/policy/                     = policy enforceability
fixtures/                         = synthetic valid/invalid inputs
data/                             = lifecycle objects, receipts, proofs, registries
release/                          = promotion, correction, withdrawal, rollback
```

This README does not:

- authorize executable policy;
- bind a runtime package;
- declare an OPA/Rego package name;
- create a sensitivity tier;
- make a source authoritative;
- grant access;
- release a layer;
- approve a geoprivacy transform;
- supersede Habitat, Flora, or Fauna policy;
- resolve the schema-home conflict.

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

Any future active Habitat policy triggered by a biotope-like concern should consume the shared semantic contracts:

```text
PolicyInputBundle
  -> active policy under accepted policy lane
  -> PolicyDecision
  -> governed runtime/release gate
```

### Shared input contract

[`PolicyInputBundle`](../../contracts/policy/policy_input_bundle.md) is the explicit input carrier. The current paired schema is a greenfield placeholder, so semantic completeness cannot be inferred from schema validity alone.

A future Habitat evaluator must not:

- silently fetch missing evidence or source facts;
- read RAW/WORK/QUARANTINE as a public shortcut;
- infer rights from public availability;
- infer sensitivity from absence of a flag;
- trust map/UI state as policy truth;
- use model prose or embeddings as authorization;
- mutate the input bundle after evaluation.

### Shared decision contract

[`PolicyDecision`](../../contracts/policy/policy_decision.md) requires:

- `decision_id`;
- `outcome`;
- `policy_family`;
- `reasons`;
- `obligations`;
- `evaluated_at`.

The paired schema permits only these policy families:

```text
promotion
access
render
capability
consent
sensitivity
```

`biotopes` is not a permitted policy family. A Habitat object may be evaluated by one or more accepted families according to the operation:

| Operation | Likely shared policy family | Example |
|---|---|---|
| Public map display | `render` or `sensitivity` | Generalize a habitat patch before display. |
| Restricted steward review | `access` | Permit a bounded reviewer to inspect restricted evidence. |
| Cross-lane analytical join | `capability` and/or `sensitivity` | Block joining public habitat geometry to restricted occurrence data. |
| Public export | `sensitivity` or `capability` | Deny exact-coordinate export or require aggregation. |
| Promotion/release handoff | `promotion` plus prior sensitivity decisions | Require evidence, rights, review, correction, and rollback closure. |

Exact policy-family composition is **PROPOSED / NEEDS VERIFICATION** until executable policy and integration tests establish it.

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

Directory Rules assign files by responsibility, not topic. This path is within the correct **root** for policy documentation but has an unresolved **lane** name.

### Current compatibility cluster

```text
policy/biotopes/README.md       # compatibility guardrail
contracts/biotopes/README.md    # compatibility contract warning
schemas/biotopes/README.md      # compatibility schema index
```

### Existing and candidate owning surfaces

```text
policy/domains/habitat/README.md                    # present; PROPOSED scaffold
contracts/domains/habitat/habitat_patch.md          # present
contracts/domains/habitat/land_cover_observation.md # present
contracts/domains/habitat/ecological_system.md      # present
schemas/contracts/v1/domains/habitat/               # repository surface; exact schema maturity varies
```

### Unresolved sensitivity surface

```text
policy/sensitivity/habitat/README.md  # not found at tested path
```

Do not create the missing sensitivity path merely to make the documentation symmetrical. First determine whether:

- Habitat-specific sensitivity rules belong under `policy/domains/habitat/`;
- a shared sensitivity lane should own them;
- an accepted policy package convention already exists elsewhere;
- an ADR or migration record is required.

### Path decision rule

| Proposed change | Required response |
|---|---|
| Edit this guardrail without changing authority | Routine docs review plus Habitat and Policy steward awareness. |
| Add active Habitat policy under `policy/domains/habitat/` | Policy, Habitat, contracts/schema, fixtures/tests, and runtime review. |
| Add `policy/sensitivity/habitat/` | Verify Directory Rules and policy-root conventions first; document owner and migration. |
| Make `policy/biotopes/` canonical | ADR and full object/policy migration plan required. |
| Remove this directory | Confirm no consumers; add forward link/migration note; preserve history and rollback. |
| Create new parallel biotope roots | Deny absent accepted ADR. |

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

No dedicated `tests/policy/biotopes/README.md` or `fixtures/policy/biotopes/README.md` was found at the tested paths. The tests below are **PROPOSED**.

### Guardrail tests

| Test | Expected result |
|---|---|
| Only allowed compatibility docs exist under `policy/biotopes/`. | Pass; unexpected active file fails. |
| No runtime import references `policy/biotopes/`. | Pass; import is a boundary failure. |
| No policy bundle registers `biotopes` as a policy family. | Pass; registration fails. |
| Contract/schema compatibility folders contain no canonical active definitions. | Pass or drift failure. |
| Links resolve to current Habitat/shared policy surfaces. | Pass. |
| Deletion/migration retains forward and rollback references. | Pass. |

### Runtime-policy negative cases

| Scenario | Expected outcome |
|---|---|
| Umbrella term supplied without canonical object/owner | `ABSTAIN` or `ERROR`, depending input validity |
| Source role unresolved | `ABSTAIN` / `DENY` |
| Rights unresolved | `DENY` or `ABSTAIN` per accepted rights policy |
| Classifier version missing | `ABSTAIN` |
| Unverified crosswalk used as equivalence | `ABSTAIN` / `DENY` |
| Model output presented as observation | `DENY` |
| Regulatory designation presented as ecological classification | `DENY` |
| Public join includes restricted occurrence | `DENY` |
| Exact geometry lacks public-safe transform | `DENY` |
| Generalization still permits reverse inference | `DENY` |
| Evidence unresolved | `ABSTAIN` |
| Policy bundle stale or evaluator unavailable | `ERROR` |
| Release state absent for public render | `DENY` / `ABSTAIN` |
| All checks pass with required generalization | `ANSWER` with obligations; not release approval |

### Fixture posture

Fixtures must be:

- synthetic;
- generalized;
- free of actual rare-species, rare-plant, cultural, or private-location coordinates;
- explicit about source role and classifier version;
- paired valid/invalid cases;
- incapable of being mistaken for production records;
- no-network by default.

### Suggested test homes

These are **PROPOSED** and require placement verification before creation:

```text
tests/policy/test_biotopes_compatibility_guardrail.py
tests/domains/habitat/test_biotope_like_policy.py
fixtures/policy/habitat/biotope_like/
```

Prefer tests organized by the **owning policy/domain responsibility**, not by the rejected umbrella term.

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

1. identify the unsupported or stale claim;
2. cite current repo/doctrine evidence;
3. update the truth label;
4. preserve the previous version in Git history;
5. note any affected migrations or active policy consumers.

### Policy supersession

Active policy decisions must be superseded through new immutable decisions, not overwritten.

Triggers include:

- source rights change;
- classifier or crosswalk correction;
- new sensitive occurrence information;
- sensitivity-policy revision;
- changed geometry transform;
- release withdrawal;
- evaluator or bundle vulnerability;
- correction to domain ownership.

### Migration rollback

A migration away from this path must record:

- source and destination paths;
- commit/blob hashes;
- compatibility window;
- affected imports/configs;
- tests run;
- forward and rollback commands;
- policy decisions or releases affected;
- whether old paths are removed, mirrored, or guardrail-only.

Rollback must restore safe behavior, not restore duplicate authority.

### This README rollback

Revert the documentation commit or close its draft PR without merging. Do not rewrite shared history.

[Back to top](#top)

---

## 21. Validation commands

These commands are inspection aids, not proof that the referenced tests or tools exist.

```bash
#: Inspect compatibility paths.
find policy/biotopes contracts/biotopes schemas/biotopes \
  -maxdepth 4 -type f -print | sort

#: Locate references that could make the compatibility path operational.
git grep -nE 'policy/biotopes|contracts/biotopes|schemas/biotopes'

#: Inspect likely owning policy and policy contracts.
find policy/domains/habitat contracts/policy schemas/contracts/v1/policy \
  -maxdepth 5 -type f -print | sort

#: Inspect Habitat contracts and policy-related tests.
find contracts/domains/habitat tests/policy tests/domains/habitat \
  -maxdepth 5 -type f -print | sort
```

Proposed documentation checks:

```bash
#: One top-level H1.
grep -c '^# ' policy/biotopes/README.md

#: No active-policy file extensions in the compatibility directory.
find policy/biotopes -type f \
  ! -name 'README.md' \
  ! -name '*migration*.md' \
  ! -name '*deprecation*.md' \
  -print

#: Confirm no prohibited biotopes policy-family claim.
git grep -nE 'policy_family.*biotopes|package[[:space:]]+biotopes' -- \
  policy packages apps tests
```

Any future executable command must be taken from verified repository tooling and CI configuration.

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

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `BIO-POL-001` | Should `policy/biotopes/` remain README-only, be deprecated, or be removed? | NEEDS VERIFICATION | Steward disposition and recursive inventory. |
| `BIO-POL-002` | Is `policy/domains/habitat/` the accepted active home for all Habitat policy? | NEEDS VERIFICATION | Current policy convention, imports, tests, ADRs. |
| `BIO-POL-003` | Should Habitat sensitivity live under the domain policy lane or a shared sensitivity lane? | UNKNOWN | Policy architecture decision and existing bundle structure. |
| `BIO-POL-004` | Are there unindexed files or consumers under the three compatibility paths? | NEEDS VERIFICATION | Recursive tree and code/config search. |
| `BIO-POL-005` | Is *biotope* retained as docs-only vocabulary or renamed to habitat types? | PROPOSED owner decision | Habitat steward vocabulary decision and doc migration. |
| `BIO-POL-006` | What reason-code registry and obligation interpreter govern Habitat policy? | UNKNOWN | Active policy bundle, contract, tests, runtime adapter. |
| `BIO-POL-007` | What object contract/schema versions are production-ready? | UNKNOWN | Schema registry, validators, fixtures, CI evidence. |
| `BIO-POL-008` | What public-safe geometry transforms are accepted? | UNKNOWN | Sensitivity policy, transform contract, receipts, tests. |
| `BIO-POL-009` | How is reverse-join and differencing risk tested? | UNKNOWN | Threat model, fixtures, regression tests, release gate. |
| `BIO-POL-010` | Which sources and crosswalks are activated for Habitat classifications? | UNKNOWN | Source descriptors, activation decisions, rights review. |
| `BIO-POL-011` | Is policy decision caching used, and how is it invalidated? | UNKNOWN | Runtime implementation, cache key, revocation tests. |
| `BIO-POL-012` | Which CI workflow enforces compatibility and Habitat policy boundaries? | UNKNOWN | Workflow, logs, required-check settings. |
| `BIO-POL-013` | Does any public API or map surface depend on this path? | UNKNOWN | Route/import audit and runtime tests. |
| `BIO-POL-014` | What rollback target applies to future path migration? | NEEDS VERIFICATION | Migration record and release/consumer inventory. |

[Back to top](#top)

---

## 24. Evidence ledger

Repository evidence inspected for this revision:

| Evidence | Blob / ref | What it supports | Limitation |
|---|---|---|---|
| `policy/biotopes/README.md` v0.1 | `70f291293f31f525369ec57d289d252958ca8d98` | Existing guardrail and conflict posture. | Does not prove full directory inventory. |
| `docs/domains/habitat/sublanes/biotopes.md` | `6690a312fcac8464a749f4e8d470404afa80adec` | Docs-only grouping, canonical object crosswalk, no parallel authority, sensitive-join posture. | Sublane convention itself is PROPOSED. |
| `contracts/biotopes/README.md` | `4ae31607df03c3d1f4de99b783f88b99946e184a` | Contract compatibility-path conflict and Habitat/Flora ownership. | Does not prove complete contract inventory. |
| `schemas/biotopes/README.md` | `3206e6ffce1cb0054e3542318e4485c5accc19a0` | Schema compatibility/index posture and no-new-canonical-schema rule. | Does not prove full schema inventory or CI. |
| `policy/README.md` | `09cd966ab188d5e831960869117522a98274cb7f` | Singular policy responsibility root. | Root README status remains PROPOSED. |
| `policy/domains/habitat/README.md` | `8456c65196354695b8eb5b8178ecb61cfc12b7dd` | Existing Habitat policy scaffold. | Greenfield scaffold; no runtime proof. |
| `contracts/policy/policy_input_bundle.md` | `545c352681dd0db0cd4d169a5d2f9c364356457c` | Explicit policy-input semantics and no-hidden-fetch rule. | Paired schema is a placeholder. |
| `contracts/policy/policy_decision.md` | `ebfe97f98263e6309db6d2772cb2c5e548819650` | Runtime outcomes, policy-family enum, reasons, obligations, timestamp. | Executable policy and wiring remain unverified. |
| `docs/domains/habitat/CANONICAL_PATHS.md` | `837aa111f70b8df678b5545c72f92c1fdca73b66` | Proposed Habitat responsibility-root placement and deny-by-default joins. | Specific paths are PROPOSED; schema slug is conflicted. |
| `docs/doctrine/directory-rules.md` | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Responsibility-root placement, conflict handling, and domain placement law. | Does not prove implementation presence. |
| `tests/policy/README.md` | `e64e81df769ac9f6b398f40fd46875f30eda5c8f` | Policy-test root and fail-closed negative-test posture. | Dedicated biotopes tests not found. |
| Initial biotopes evidence snapshot | `65a0d9f6159efa03aba0711d38a51eb203079c3f` | Commit-pinned detailed inspection context. | Runtime, branch protection, and full recursive tree not inspected. |
| Review-branch base | `30f7bdda720310a14376791b6d1e02e1d3639e91` | Target blob rechecked unchanged; intervening commits changed unrelated paths. | Does not add runtime evidence. |

### Truth summary

```text
CONFIRMED:
  target exists
  conflict is documented
  parallel compatibility READMEs exist
  canonical Habitat objects and owner lanes are documented
  shared policy contracts exist
  PolicyDecision finite field surface exists
  Habitat policy scaffold exists
  dedicated tested README paths were absent

PROPOSED:
  migration sequence
  reason codes and obligations
  future fixture/test locations
  exact policy-family composition
  active Habitat sensitivity home

UNKNOWN:
  executable policy
  complete tree inventory
  evaluator integration
  CI enforcement
  public route behavior
  release behavior
  production source/crosswalk activation
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

## Status summary

`policy/biotopes/` remains a **non-canonical compatibility guardrail**.

It may help maintainers route Habitat classification and sensitive-join policy to the correct owning surfaces. It must not acquire executable policy, a new policy family, schema/contract authority, source or lifecycle data, or release power without an accepted architectural decision and a reversible migration.

<p align="right"><a href="#top">Back to top</a></p>
