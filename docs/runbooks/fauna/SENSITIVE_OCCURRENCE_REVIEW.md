<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/sensitive-occurrence-review
title: Fauna — Sensitive Occurrence Review Runbook
type: runbook; operational-procedure; sensitivity-review; geoprivacy; pre-release; non-authoritative
version: v1.0
prior_version: PROPOSED scaffold
status: draft; repository-grounded; fail-closed; review-only; no-network-by-default; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: >-
  Fauna, occurrence, taxonomy, source, rights, evidence, sensitivity,
  geoprivacy, policy, access-control, correction, release, operations, and
  independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing
  does not create those authorities.
created: NEEDS VERIFICATION — the prior scaffold carried no creation date
updated: 2026-08-24
policy_label: public-review; fauna; sensitive-occurrence; geoprivacy; fail-closed; no-sensitive-payloads; no-publication-authority
current_path: docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md
owning_root: docs/
responsibility: >-
  Document how an authorized operator should validate, classify, and hand off a
  potentially sensitive Fauna occurrence without exposing exact or
  reverse-engineerable location information, inventing sensitivity or taxonomic
  authority, weakening source terms, or confusing validation and review with
  release or publication.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path modernization; no new or parallel authority
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a
  target_prior_blob: 7ba828b1b70327b08f10e844109b3dbf48c65622
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  occurrence_evidence_contract_blob: f38ae38055d03149471a97b63d38a7b8f7cfbd35
  occurrence_evidence_validator_blob: fd54968e4e013284d8c633ea6782252a0a4ec90c
  occurrence_evidence_test_blob: 785868d14423530cab7180d4e54f98fad5eb5e73
  occurrence_evidence_workflow_blob: faae7732e4cafe7f997bc367dc67ba5c61f8dd06
  public_safe_fixture_validator_blob: fe96d8c4cc78f44679ddf617b2b1251fe621928c
  domain_fauna_workflow_blob: 0edc73a77ee0ddb3193db2c0386ed6ac685b139a
  occurrence_public_contract_blob: d0c1481160b4979445a916915ff96d04d48f7033
  sensitivity_policy_readme_blob: aac9f7b6316b89238d209c7ef4045fbf4df15ea9
  rare_species_policy_stub_blob: a7269d357bb7570fc3680c299486e5d62cb33a68
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  fauna_source_registry_readme_blob: c3a36f721b445ae41d2d9407f7b3524872ed1128
inspection_boundary: >-
  Current-session GitHub reads covered the target scaffold, accepted Directory
  Rules decision, contribution and pull-request controls, Fauna sensitivity and
  source-role documentation, OccurrenceEvidence/Public/Restricted and
  SensitiveSite contracts, the occurrence schema/validator/fixtures/tests,
  synthetic public-safe fixture validation, Fauna workflows, sensitivity-policy
  scaffolds, source-authority and Fauna source-registry state, processed public
  and restricted lane guides, and the cross-domain fail-closed architecture.
  Repository-native commands were not run in a mounted checkout during
  authoring. No live source, occurrence payload, exact location, taxon-sensitive
  identifier, private review record, transform parameter, policy decision,
  release object, deployment, promotion, or publication was accessed or changed.
related:
  - docs/runbooks/README.md
  - docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/fauna/TAXONOMY_RESOLUTION_RUNBOOK.md
  - docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
  - docs/runbooks/fauna/PUBLICATION_GATE_DRY_RUN.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/architecture/sensitive-domain-fail-closed.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/SOURCES.md
  - docs/domains/fauna/SOURCE_ROLES.md
  - contracts/domains/fauna/occurrence_evidence.md
  - contracts/domains/fauna/occurrence_public.md
  - contracts/domains/fauna/occurrence_restricted.md
  - contracts/domains/fauna/sensitive_site.md
  - schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py
  - tools/validators/domains/fauna/validate_public_safe_fixture.py
  - fixtures/domains/fauna/occurrence_evidence/README.md
  - tests/domains/fauna/test_occurrence_evidence.py
  - tests/domains/fauna/test_fauna_smoke.py
  - .github/workflows/fauna-occurrence-evidence.yml
  - .github/workflows/domain-fauna.yml
  - policy/sensitivity/fauna/README.md
  - policy/domains/fauna/rare_species_redaction.rego
  - control_plane/source_authority_register.yaml
  - data/registry/sources/fauna/README.md
  - data/processed/fauna/restricted/occurrences/README.md
  - data/processed/fauna/public/occurrences_generalized/README.md
  - release/candidates/fauna/README.md
tags: [kfm, fauna, occurrence, sensitivity, geoprivacy, review, quarantine, redaction, no-network, fail-closed]
notes:
  - "v1.0 replaces an inventory-generated placeholder with a repository-grounded, public-safe review and handoff procedure."
  - "The runbook deliberately contains no exact coordinates, source-native protected identifiers, transform radii, seeds, offsets, or other reversal-enabling details."
  - "The current repository has a bounded OccurrenceEvidence machine profile, not a complete real-world sensitive-occurrence policy/review/release path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — Sensitive Occurrence Review Runbook

> **Validate, classify, and hand off a potentially sensitive Fauna occurrence without exposing protected detail or turning a schema pass, review note, pull request, or merge into policy, release, or publication authority.**

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail%20closed-b42318">
  <img alt="Validation: occurrence profile available" src="https://img.shields.io/badge/validation-bounded%20profile-0969da">
  <img alt="Policy runtime: hold" src="https://img.shields.io/badge/policy%20runtime-HOLD-d4a72c">
  <img alt="Current result: review handoff only" src="https://img.shields.io/badge/current%20result-review%20handoff%20only-6e7781">
  <img alt="Publisher: no" src="https://img.shields.io/badge/publisher-no-6e7781">
</p>

> [!IMPORTANT]
> **Current repository result: `HOLD_FOR_POLICY_AND_STEWARD_REVIEW`.** KFM has a closed, deterministic, no-network `OccurrenceEvidence` draft schema and validator, including a valid sensitive-withheld `quarantine` fixture. It does not yet have an accepted Fauna sensitivity-policy implementation, admitted real source descriptor set, authenticated sensitivity-review route, field-complete `OccurrencePublic` or `OccurrenceRestricted` machine contract, functional geoprivacy executor, or candidate-specific release path.

> [!CAUTION]
> **Do not place a real sensitive occurrence payload in a pull request, issue, discussion, workflow input, hosted CI artifact, shell history, screenshot, report, or public review packet.** Use opaque references and code/path-only findings. Even a filename, taxon label, time, stable identifier, join key, or coarse-looking map cell can assist re-identification when combined with other information.

> [!WARNING]
> **Client-side hiding is not protection.** Removing a popup field, lowering map opacity, omitting a label, hiding a layer by default, or instructing an AI not to answer does not make delivered bytes public-safe. Protected detail must be withheld or transformed before public delivery, and the delivered representation plus likely joins must be reviewed.

**Quick navigation:** [Purpose](#1-purpose-scope-and-terminal-boundary) · [Authority](#2-authority-placement-and-current-state) · [Safety](#3-sensitive-material-handling-contract) · [Roles](#4-roles-and-separation-of-duties) · [Preflight](#5-preconditions-and-mandatory-stop-conditions) · [Classification](#6-classify-the-record-before-review) · [Validation](#7-current-executable-machine-validation) · [Procedure](#8-sensitive-occurrence-review-procedure) · [Derivative](#9-public-safe-derivative-assessment) · [Outcomes](#10-finite-outcomes-and-reason-codes) · [Handoff](#11-public-safe-review-handoff) · [Recovery](#12-correction-withdrawal-and-rollback) · [CI](#13-hosted-ci-and-exact-head-evidence) · [Graduation](#14-current-holds-and-graduation-criteria) · [Maintenance](#15-maintenance-and-document-rollback) · [Checklist](#appendix-a-operator-checklist) · [Template](#appendix-b-review-handoff-template) · [Evidence](#appendix-c-evidence-basis)

---

## 1. Purpose, scope, and terminal boundary

Use this runbook when a Fauna occurrence, occurrence candidate, occurrence-derived representation, or related site record may expose a sensitive taxon, sensitive site, protected source condition, steward-controlled knowledge, private-land context, observer-linked information, exact or reverse-engineerable location support, or a risky cross-domain join.

It separates four questions that must not be collapsed:

1. **Machine consistency** — does the candidate satisfy the current draft `OccurrenceEvidence` schema and bounded validator checks?
2. **Scientific and source interpretation** — what does the source actually support, with which source role, taxonomic scope, time, and method?
3. **Sensitivity disposition** — must the record remain quarantined, restricted, withheld, generalized, aggregated, delayed, denied, or abstained from for the exact audience and operation?
4. **Release disposition** — may a separately derived public-safe representation advance through evidence, policy, review, release, correction, and rollback gates?

Only question 1 has a current bounded executable profile. Questions 2–4 require authorities and implementations that remain incomplete, proposed, unknown, or held.

### In scope

- freeze repository, candidate, purpose, audience, operation, time, and requested precision;
- use opaque record references and public-safe findings rather than protected values;
- validate the current `OccurrenceEvidence` machine profile in an authorized no-network environment;
- distinguish CLI validation outcome from the candidate's declared lifecycle/review posture;
- preserve source role and basis-of-record anti-collapse;
- route unresolved taxonomy through the Taxonomy Resolution Runbook;
- assess rights, evidence, sensitivity, site, re-identification, observer/privacy, private-land, and join risks;
- determine whether the record remains in WORK/QUARANTINE, may enter a restricted processed lane, or may support a future public-safe derivative request;
- prepare a review handoff containing references and reason codes only; and
- route suspected exposure, correction, withdrawal, and rollback work to their owning procedures.

### Out of scope

This runbook does not:

- fetch, open, decode, reproduce, transform, or publish a live sensitive occurrence;
- decide that a real taxon, nest, den, roost, hibernaculum, spawning or breeding site, stopover, telemetry path, parcel, or steward record is safe;
- admit a source or create a `SourceDescriptor`;
- resolve legal, contractual, sovereignty, consent, or stewardship obligations;
- treat a nonempty accepted taxon name as taxonomic-authority resolution;
- resolve an `EvidenceRef` into an authoritative `EvidenceBundle`;
- choose, reveal, or execute geoprivacy parameters;
- authenticate reviewers or establish separation of duties;
- convert an `OccurrenceEvidence` object into an authoritative `OccurrenceRestricted` or `OccurrencePublic` object;
- create a `PolicyDecision`, `ReviewRecord`, `RedactionReceipt`, `ReleaseManifest`, correction, withdrawal, or rollback record;
- move lifecycle data, write public carriers, deploy a route, or publish anything; or
- provide hunting, fishing, enforcement, land-access, emergency, or intervention guidance.

### Terminal boundary

The maximum current output is a **public-safe review handoff**, never an allow or release decision.

```text
NO_ACTION
QUARANTINE
HOLD_FOR_SOURCE_ADMISSION
HOLD_FOR_RIGHTS
HOLD_FOR_TAXONOMY
HOLD_FOR_EVIDENCE
HOLD_FOR_SENSITIVITY_REVIEW
HOLD_FOR_POLICY
HOLD_FOR_GEOPRIVACY_TRANSFORM
HOLD_FOR_REIDENTIFICATION_REVIEW
HOLD_FOR_ACCESS_CONTROL
HOLD_FOR_CORRECTION_PATH
HOLD_FOR_ROLLBACK
RESTRICTED_HANDOFF_READY
PUBLIC_DERIVATIVE_REQUEST_READY
DENY
ABSTAIN
ERROR
```

`PUBLIC_DERIVATIVE_REQUEST_READY` means only that an authorized team may begin a separately governed public-safe derivative assessment. It does not mean the occurrence is public-safe, released, or publishable.

[Back to top](#top)

---

## 2. Authority, placement, and current state

### 2.1 Directory result

**Placement outcome: `PLACE` — CONFIRMED for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the writable [Directory Rules](../../doctrine/directory-rules.md). This tracked file explains a human operational procedure, so it remains under `docs/runbooks/fauna/`. The update creates no new root, alias, contract, schema, policy, registry, data, proof, receipt, release, correction, or publication authority.

| Concern | Owning authority | This runbook's role |
|---|---|---|
| Human review procedure | `docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md` | Explain operator sequence and handoff |
| Fauna sensitivity doctrine | [`docs/domains/fauna/SENSITIVITY.md`](../../domains/fauna/SENSITIVITY.md) | Explain posture; do not make decisions |
| Cross-domain fail-closed architecture | [`docs/architecture/sensitive-domain-fail-closed.md`](../../architecture/sensitive-domain-fail-closed.md) | Preserve operation-specific closure |
| Occurrence meaning | [`contracts/domains/fauna/occurrence_evidence.md`](../../../contracts/domains/fauna/occurrence_evidence.md) and siblings | Reference semantics |
| Machine shape | `schemas/contracts/v1/domains/fauna/` | Validate accepted shape only |
| Source identity and role | `data/registry/sources/fauna/` plus accepted source authority | Require references; do not admit |
| Sensitivity and access decision | `policy/sensitivity/fauna/`, `policy/domains/fauna/`, bound evaluator | Require decision; do not substitute |
| Validation | `tools/validators/`, `tests/`, workflows | Run bounded checks and interpret limits |
| Lifecycle instances | `data/<phase>/fauna/` | Respect stage and access boundary |
| Evidence and proof | EvidenceRef/EvidenceBundle and proof families | Require resolution |
| Review and release | accepted review and `release/` objects | Hand off; do not approve |
| Correction and rollback | correction/release procedures and records | Escalate and preserve lineage |
| Public clients | governed API and released public-safe carriers | Never use protected/internal objects directly |

### 2.2 Current repository state

Pinned checkpoint: `main@df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a`.

| Surface | CONFIRMED observation | Safe conclusion |
|---|---|---|
| Target file | Inventory-generated scaffold, blob `7ba828b1...` | Substantive procedure is missing |
| `OccurrenceEvidence` contract | Draft semantic contract with closed draft schema and deterministic validator | Machine consistency can be checked in a bounded fixture-first profile |
| Sensitive fixture | Valid sensitive-withheld record declares `quarantine` and exposes no public coordinates | A validator can pass a non-public record; valid does not mean publishable |
| Public/restricted occurrence contracts | Substantive semantic drafts; paired schemas remain permissive scaffolds | No field-complete machine conversion contract is established |
| `SensitiveSite` contract | Substantive semantic draft; paired schema remains a scaffold | Site meaning exists as proposal; machine enforcement is unproved |
| Fauna sensitivity policy README | Proposed scaffold | No accepted Fauna sensitivity policy surface is established there |
| `rare_species_redaction.rego` | Greenfield stub with `default deny := false` and no operative rule | Do not treat file presence as fail-closed enforcement |
| Source authority projection | `implementation_status: ABSENT`, `completeness: empty`, `entries: []` | No central admitted source set is proved |
| Fauna source registry directory | README plus `.gitkeep`; no descriptor record at the inspected ref | Real source admission remains held |
| Restricted/public processed lanes | Detailed boundary guides | Payload inventory, access enforcement, transforms, and promotion behavior remain unverified |
| `fauna-occurrence-evidence` workflow | Runs focused no-network schema, validator, fixture, and receipt checks when its scoped paths change | Does not classify real sensitivity or release data |
| `domain-fauna` workflow | Runs synthetic fixture safety; proof and publication jobs remain explicit holds | Green held jobs are readiness evidence, not implemented proof/release capability |
| Governed public boundary | Cross-domain architecture records an `ABSTAIN`/safe `ERROR` scaffold, not a sensitive-domain `ANSWER` route | No public sensitive-occurrence response path is established |

Current determination:

```text
bounded occurrence machine profile      = CONFIRMED
live source admission                    = HOLD
real taxonomy authority                  = HOLD / NEEDS VERIFICATION
EvidenceBundle resolution                = HOLD
Fauna sensitivity policy implementation  = HOLD
authenticated sensitivity review         = HOLD
functional geoprivacy transform          = HOLD
restricted/public conversion contract    = HOLD
candidate-specific release path          = HOLD
public sensitive-occurrence exposure     = DENY BY DEFAULT
```

[Back to top](#top)

---

## 3. Sensitive-material handling contract

### 3.1 Minimum-safe working environment

Review real protected material only in an environment authorized for the source, purpose, audience, and sensitivity class. The environment must be capable of preventing accidental network transmission, shared-shell history, public logs, unreviewed artifact upload, clipboard synchronization, screenshot capture, and uncontrolled backup where those controls are required.

This repository runbook cannot prove such an environment exists. Record the environment control reference, not its secrets or protected configuration.

### 3.2 Public surfaces that must remain payload-free

Do not place protected values in:

- Git branch names, commit messages, pull-request titles or bodies;
- issues, discussions, review comments, chat transcripts, or email summaries;
- workflow inputs, job logs, annotations, step summaries, artifacts, caches, or badges;
- terminal commands, filenames, shell history, crash reports, stack traces, or temporary paths visible to other users;
- screenshots, screen recordings, dashboards, map previews, notebooks, reports, or slide decks;
- public JSON, HTML, tiles, PMTiles, COGs, GeoParquet, search indexes, graph projections, exports, or AI prompts/responses;
- `EvidenceRef` labels, stable identifiers, metadata, or join keys that reveal or enable reconstruction; or
- transform receipts whose public fields expose reversal-enabling parameters.

### 3.3 Opaque-reference rule

Use an opaque candidate reference that reveals no taxon, site, geography, observer, source-native identifier, exact time, sensitivity class, or transform method. The reference must still resolve inside the authorized review system to an auditable object.

A public handoff may include:

- opaque candidate and review IDs;
- repository commit and validator version;
- safe reason codes and JSON Pointer paths;
- high-level source role and evidence class when policy permits;
- state labels such as `QUARANTINE`, `HOLD`, `DENY`, or `ABSTAIN`;
- pointers to restricted review records; and
- correction and rollback references that do not expose protected content.

### 3.4 Output-minimization rule

The current occurrence validator reports only finding code and JSON Pointer path. Preserve that behavior. Do not add record values to public diagnostics merely to make review easier. Where a path itself is sensitive, map it to an opaque internal locator before sharing.

### 3.5 Composition risk

A representation that appears safe alone may become unsafe when combined with:

- fine observation time;
- rare taxon identity;
- habitat, hydrography, road, parcel, ownership, infrastructure, or land-management layers;
- observer, media, device, project, permit, or institution identifiers;
- repeated generalized releases that intersect to narrow a location;
- range, migration, telemetry, breeding, roosting, or seasonal-use products;
- map camera, viewport, feature count, or empty-cell behavior;
- search suggestions, cache keys, URLs, downloadable filenames, or error timing; or
- AI summaries that restate withheld context.

Review the **delivered bytes and likely compositions**, not only the nominal coordinate field.

[Back to top](#top)

---

## 4. Roles and separation of duties

GitHub review routing is not substantive sensitivity authority. The following roles remain logically separate even when one person temporarily performs more than one role under a documented bootstrap exception.

| Role | Minimum responsibility | Must not be inferred from |
|---|---|---|
| Occurrence operator | Run bounded checks and preserve protected-data handling | Tool access or file ownership |
| Source steward | Confirm source identity, source role, terms, purpose, and permitted handling | Connector directory or URL |
| Taxonomy reviewer | Resolve taxon concept and authority snapshot | Nonempty accepted-name field |
| Evidence reviewer | Resolve EvidenceRefs and bound claim support | Schema pass or citation string |
| Rights/stewardship reviewer | Confirm reuse, privacy, consent, sovereignty, embargo, and steward conditions | Public availability or attribution |
| Sensitivity reviewer | Determine protected detail and public-safe obligations for exact operation/audience | Species rarity alone or generic tier prose |
| Geoprivacy reviewer | Review transform sufficiency and reconstruction risk | Reduced decimal precision or hidden map field |
| Policy steward/evaluator owner | Produce an operation-specific finite policy result | Rego file presence |
| Access-control steward | Prove role-gated restricted handling | Folder name or UI login |
| Independent reviewer | Challenge classification, transform, evidence, and composition assumptions | Author self-review |
| Release authority | Decide release after all gates close | Pull-request approval or merge |
| Correction/rollback owner | Propagate withdrawal, correction, invalidation, and rollback | Deleting one file or hiding one layer |

Minimum separation for a public-safe derivative request:

1. the generator/operator must not be the sole sensitivity or release approver;
2. source/rights conditions must be reviewed independently of scientific desirability;
3. transform sufficiency must be reviewed against reconstruction and composition risk;
4. release approval must be separate from schema validation and GitHub merge; and
5. correction/rollback ownership must be identified before public exposure.

When named or accountable roles are unavailable, return `HOLD_FOR_SENSITIVITY_REVIEW`, `HOLD_FOR_POLICY`, or `HOLD_FOR_ACCESS_CONTROL`. Do not substitute a repository username for a missing functional authority.

[Back to top](#top)

---

## 5. Preconditions and mandatory stop conditions

### 5.1 Preconditions

Before reviewing a real candidate, record or resolve all of the following inside the authorized environment:

| Precondition | Required evidence | Failure outcome |
|---|---|---|
| Exact review purpose | Approved use, audience, operation, output class, and requested precision | `HOLD_FOR_RIGHTS` or `ABSTAIN` |
| Immutable candidate identity | Opaque ID plus content/spec hash under the governing contract | `ERROR` or `QUARANTINE` |
| Source identity | Accepted SourceDescriptor or equivalent source-admission record | `HOLD_FOR_SOURCE_ADMISSION` |
| Source role | Canonical role and source-native basis of record | `QUARANTINE` on mismatch |
| Taxonomic scope | Authority-versioned taxon concept or explicit unresolved status | `HOLD_FOR_TAXONOMY` |
| Evidence support | Resolvable EvidenceRefs and bounded EvidenceBundle support | `HOLD_FOR_EVIDENCE` |
| Rights/stewardship | License, redistribution, commercial-use, attribution, privacy, agreement, embargo, and steward conditions as applicable | `HOLD_FOR_RIGHTS` or `DENY` |
| Sensitivity inputs | Policy-recognized sensitivity and site signals, without public disclosure | `HOLD_FOR_SENSITIVITY_REVIEW` |
| Review roles | Accountable reviewers and required separation | `HOLD_FOR_SENSITIVITY_REVIEW` |
| Correction path | How classification, taxonomy, source withdrawal, or new sensitivity evidence propagates | `HOLD_FOR_CORRECTION_PATH` |
| Rollback target | Prior safe state and affected carrier/cache/index inventory | `HOLD_FOR_ROLLBACK` |

At the current repository checkpoint, real source admission, binding policy, authenticated review, and release closure are not proved. A real candidate therefore normally stops at a restricted review handoff.

### 5.2 Mandatory stop conditions

Stop immediately and do not continue public-derivative work when any of these occurs:

- protected values appear in a public or shared surface;
- candidate identity or hash cannot be verified;
- source identity, role, terms, or approved purpose is missing or conflicted;
- taxonomy is unresolved in a way material to sensitivity or public meaning;
- an observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic source is being relabeled as another role;
- rights or steward conditions are unknown, expired, revoked, or incompatible with the use;
- a sensitive-species or sensitive-site signal lacks accountable review;
- a non-open, generalized, or withheld record lacks explicit public-safe geometry posture;
- withheld output still carries coordinates or reconstructable location clues;
- generalization-required output claims exact public precision;
- repeated releases or joins can narrow a protected location;
- a proposed policy scaffold is being treated as an operative decision;
- a transform is improvised, nondeterministic where determinism is required, unreviewed, or not receipt-bearing;
- public/restricted conversion relies on permissive scaffold schemas as if field-complete;
- a review packet contains transform secrets or protected data;
- no correction, withdrawal, cache invalidation, or rollback path exists; or
- anyone treats validation, review, commit, pull request, merge, or workflow success as publication authority.

Suspected exposure is an incident and correction problem, not an ordinary documentation task. Follow [§12](#12-correction-withdrawal-and-rollback) and keep sensitive details out of public channels.

[Back to top](#top)

---

## 6. Classify the record before review

### 6.1 Separate object families

Do not treat all animal-related geometry as one object type.

| Object family | Meaning | Sensitive-review implication |
|---|---|---|
| `OccurrenceEvidence` | Source-bound occurrence support before sensitivity split | Validate current draft profile; never publication authority |
| `OccurrenceRestricted` | Held/restricted occurrence representation | Public access denied; machine schema remains incomplete |
| `OccurrencePublic` | Proposed public-safe occurrence representation downstream of evidence and policy | Requires separate transform, review, release, correction, and rollback closure |
| `SensitiveSite` | Nest, den, roost, hibernaculum, spawning/breeding/nursery/stopover or other protected site | T4-default doctrine; do not reduce to ordinary occurrence |
| Range or seasonal range | Derived spatial extent, not an event | Review aggregate/model support and reverse inference |
| Migration or telemetry product | Route, detections, or modeled utilization | Exact paths and repeated points can be highly revealing |
| Model output | Predicted or derived support | Must not masquerade as observed occurrence |
| Aggregate | Count, density, rank, or roll-up | Small-cell and reconstruction risk remain material |
| Regulatory/administrative record | Status or compiled context | Does not prove an observed event |
| Candidate/synthetic record | Unreviewed or generated context | Cannot become observed truth through review wording |

A sensitive site can be supported by occurrence evidence, but it remains a distinct site-class object with its own disclosure risk. Conversely, a sensitive occurrence is not automatically proof of a persistent site, range, population, abundance, habitat condition, or conservation status.

### 6.2 Preserve canonical source role

Use the seven-class source-role vocabulary documented in [Fauna Source Roles](../../domains/fauna/SOURCE_ROLES.md):

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

The source-native occurrence form belongs in `observation.basis_of_record`. An aggregator is an access path, not automatically the `aggregate` role. Promotion or review does not upgrade a role. A correction requires a new governed record and lineage, not an in-place relabel that hides history.

### 6.3 Taxonomy before sensitivity-dependent interpretation

Use the [Taxonomy Resolution Runbook](./TAXONOMY_RESOLUTION_RUNBOOK.md) when accepted name, concept, authority snapshot, synonymy, ambiguity, or source-native taxonomy is unresolved.

A nonempty `accepted_scientific_name` satisfies only the current validator's bounded normalization check. It does not establish:

- authoritative taxon-concept identity;
- current nomenclatural acceptance;
- synonym or split/merge resolution;
- conservation, regulatory, or sensitive-species status;
- geographic occurrence; or
- permission to disclose the taxon label when the label itself increases risk.

### 6.4 Sensitivity-review trigger classes

Route a candidate through this runbook when any of the following is present or unresolved:

- source geoprivacy is non-open, generalized, obscured, embargoed, or withheld;
- `sensitive_species_flag`, `review_required`, `generalization_required`, or `withhold_required` is true;
- exact-location public safety is uncertain or conflicts with other flags;
- the occurrence relates to a nest, den, roost, hibernaculum, spawning/breeding/nursery site, stopover, colony, aggregation, or recurring-use site;
- source terms, steward control, tribal/community authority, landowner conditions, observer privacy, media, device, project, permit, or private-land context restrict use;
- telemetry, acoustic, camera, specimen, eDNA, or repeated temporal records permit reverse inference;
- a small cell, sparse count, rare combination, or repeated generalized output could identify a site;
- a modeled surface or range layer reveals likely protected locations;
- a cross-domain join materially increases precision or harm; or
- the reviewer cannot prove that the requested public output is the safest representation that still answers the legitimate need.

[Back to top](#top)

---

## 7. Current executable machine validation

### 7.1 What is implemented

The current repository provides a deterministic, no-network validator for the draft `OccurrenceEvidence` profile:

```text
tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py
```

It validates:

- closed Draft 2020-12 shape;
- deterministic JCS + SHA-256 identity and occurrence URI binding;
- canonical source-role/basis-of-record relationships;
- declared rights resolution consistency;
- accepted-name nonempty normalization;
- required raw-artifact support for selected roles;
- exact/public-safe geometry consistency;
- sensitive-species review posture;
- finite declared result and canonical reason-code consistency; and
- exact fixture inventory and expected findings.

It does **not** decide which taxon or site is sensitive, resolve real source terms, authenticate review, execute a transform, evaluate production policy, resolve an EvidenceBundle, convert object families, release data, or publish.

### 7.2 Authorized no-network command map

Run these only in a repository checkout and environment authorized for the material. The fixture commands contain synthetic data only.

Install the repository-declared test profile when needed:

```bash
python tools/ci/install_python_ci.py project-test
```

Run the focused occurrence unit suite:

```bash
python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_occurrence_evidence.py' \
  --verbose
```

Replay the exact occurrence fixture manifest:

```bash
python tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py --fixtures
```

Run the broader synthetic Fauna public-safe fixture suite:

```bash
python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Validate one authorized local candidate:

```bash
python tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py \
  /authorized/private/review/candidate.json
```

> [!CAUTION]
> The CLI prints the input path. Do not use a real taxon, site, geography, observer, source identifier, or sensitivity label in the filename or directory name. Do not run a real sensitive candidate in hosted CI or a shared terminal unless that environment and its logs are explicitly authorized.

### 7.3 Interpret the two result layers correctly

The CLI has an outer result:

```text
PASS  = no schema or bounded semantic findings
ERROR = one or more findings
```

The candidate itself declares an inner `validation.validator_result`:

```text
pass | quarantine | deny | error
```

These are not the same axis. A valid sensitive-withheld candidate may declare `quarantine` and still produce CLI `PASS`. That means the object consistently describes a non-public held state. It does not mean the occurrence passed policy, review, release, or publication gates.

### 7.4 Current fixture evidence

The occurrence fixture family includes:

| Fixture posture | What it proves | What it does not prove |
|---|---|---|
| Valid observed open | Bounded direct-observation shape and consistency | Real source, taxonomy, rights, or public safety |
| Valid modeled context | Modeled role remains distinct from observed | Model validity or occurrence truth |
| Valid sensitive withheld quarantine | Withheld public geometry and non-public review posture can be schema-valid | Transform sufficiency, steward approval, or release |
| Modeled as observed | Role/basis anti-collapse is rejected | Full scientific interpretation |
| Observed without raw artifact | Required provenance support is enforced for bounded roles | EvidenceBundle closure |
| Unresolved rights claimed as pass | A false rights-pass claim is rejected | Legal review |
| Sensitive exact without generalization | Conflicting public precision is rejected | Selection or execution of a safe transform |
| Spec-hash mismatch | Deterministic identity mismatch is rejected | Source authenticity beyond declared inputs |

The broader synthetic fixture validator also rejects undeclared or numeric location-bearing fields, coordinate-like strings, live URLs, malformed caveats, unresolved governance state, and missing synthetic redaction references. It is deliberately narrower than a production `OccurrencePublic` validator.

### 7.5 Privacy-preserving diagnostics

The occurrence validator emits findings in this shape:

```json
{
  "code": "sens.review_required",
  "path": "/sensitivity/review_required"
}
```

Do not add the rejected value to public diagnostics. Report counts, codes, and safe paths only. If the path itself reveals sensitive structure, replace it with an opaque review locator outside the public packet.

[Back to top](#top)

---

## 8. Sensitive-occurrence review procedure

### Step 0 — Freeze scope and authority

Record:

```text
repository_ref
repository_commit
candidate_opaque_id
candidate_spec_hash
review_purpose
requested_operation
requested_audience
requested_precision_class
source_descriptor_ref
review_environment_ref
```

Confirm that no overlapping pull request, branch, incident, correction, source withdrawal, or steward hold owns the same candidate or procedure. Repository coordination may use opaque IDs only.

Stop if the base, candidate, purpose, or authority cannot be frozen.

### Step 1 — Confirm source identity, role, and purpose

Require an accepted source record that states, as applicable:

- source and dataset identity;
- source role and basis of record;
- rights, redistribution, commercial-use, attribution, privacy, and citation posture;
- approved purpose and audience;
- access agreement, embargo, and steward conditions;
- sensitivity floor and geoprivacy supplied by the source;
- source version, retrieval time, and correction/withdrawal channel; and
- whether source-native IDs or labels may appear in a derived output.

At the current checkpoint, the central source-authority register is empty and the Fauna source-registry lane contains no verified descriptor record. A real candidate without separately verified source-admission evidence returns `HOLD_FOR_SOURCE_ADMISSION`.

### Step 2 — Verify identity and integrity

Run the current occurrence validator in the authorized environment or use the governing successor validator if the candidate uses a later accepted profile.

Require:

- schema edition and validator version;
- deterministic `spec_hash`;
- occurrence ID bound to the digest;
- immutable input reference;
- validator result and safe finding set; and
- no protected values in output.

A hash proves identity of declared bytes under the specified subject. It does not prove source authority, scientific truth, rights, sensitivity clearance, or release.

### Step 3 — Resolve taxonomy or hold

Check:

- source-native taxon assertion preserved;
- accepted concept and authority version identified;
- synonym, split, merge, hybrid, subspecies, unidentified, or ambiguous state handled explicitly;
- taxon label public-safety reviewed where revealing identity raises risk; and
- taxonomic correction propagation planned.

Use `HOLD_FOR_TAXONOMY` rather than guessing or silently normalizing.

### Step 4 — Resolve evidence support or hold

Require EvidenceRefs that can resolve to admissible EvidenceBundles in the authorized environment. Confirm that the evidence supports only the bounded occurrence claim and does not silently assert:

- abundance or population size;
- persistence, breeding, denning, nesting, or occupancy;
- range or habitat suitability;
- conservation or regulatory status;
- disease, mortality, or threat;
- land access, ownership, or management rights; or
- current presence outside the evidence's time and support scope.

Use `HOLD_FOR_EVIDENCE` or `ABSTAIN` when support is insufficient.

### Step 5 — Check rights, stewardship, and privacy

Review the exact requested use, not a generic source summary. Confirm:

- redistribution and derivative permissions;
- commercial/noncommercial restrictions;
- attribution and citation obligations;
- observer, contributor, institution, media, device, and project privacy;
- landowner, agency, tribal/community, research-partner, or steward control;
- embargo and delayed-publication requirements;
- source withdrawal and correction obligations; and
- whether the public-safe derivative can be reconstructed into source rows.

Unknown or incompatible conditions return `HOLD_FOR_RIGHTS` or `DENY`.

### Step 6 — Classify sensitivity without exposing it

The sensitivity reviewer assesses the exact candidate, audience, operation, precision, time, and likely compositions.

At minimum, ask:

1. Can the taxon identity itself increase collection, disturbance, persecution, or exploitation risk?
2. Is the record associated with a site class whose existence or location is protected?
3. Can time, repeated records, media, observer, project, habitat, route, parcel, or infrastructure context narrow the site?
4. Does source geoprivacy already signal withholding or generalization?
5. Could a modeled or aggregate output reveal the same protected location indirectly?
6. Could a public response confirm absence/presence patterns through error, count, timing, cache, or empty-cell behavior?
7. Is delayed release or complete suppression safer than generalization?
8. Does any steward or rights holder require a stricter posture?

Record only the finite disposition and safe reason codes in the public handoff. Protected rationale stays in the authorized review record.

### Step 7 — Choose restricted, quarantine, or derivative-request posture

Use this decision table:

| Condition | Current safe posture |
|---|---|
| Identity/shape failure | `ERROR` and return to WORK |
| Source, rights, taxonomy, evidence, policy, or review unresolved | `QUARANTINE` plus the specific `HOLD_FOR_*` reason |
| Exact/reconstructable sensitive detail required by the requested public use | `DENY` or narrow the request |
| Protected occurrence may be retained for authorized internal review | `RESTRICTED_HANDOFF_READY`, subject to access-control authority |
| A separate safer representation appears feasible | `PUBLIC_DERIVATIVE_REQUEST_READY`; do not create or release it here |
| Even existence or broad summary is unsafe or unsupported | `DENY` or `ABSTAIN` |
| Suspected prior exposure | Stop and invoke correction/withdrawal/rollback handling |

Do not use `ALLOW`, `APPROVE`, `PUBLIC`, or `RELEASED` as this runbook's terminal result.

### Step 8 — Review joins and side channels

Before requesting a public-safe derivative, enumerate downstream carriers and joins:

```text
catalog
triplets / graph
search / autocomplete
API and error envelopes
MapLibre source, tiles, feature properties, and camera state
Evidence Drawer and Focus Mode
reports and exports
caches and CDNs
analytics and logs
AI retrieval indexes and summaries
```

For each surface, test whether a user can infer protected detail through composition, repeated queries, differential responses, IDs, timing, filenames, or metadata. Any unresolved path returns `HOLD_FOR_REIDENTIFICATION_REVIEW`.

### Step 9 — Prepare the public-safe handoff

Use [Appendix B](#appendix-b-review-handoff-template). Include only opaque references, statuses, safe reason codes, reviewer-role requirements, and non-effects. Store protected rationale and data in the authorized system, not the PR or runbook.

### Step 10 — Stop before release

The review handoff may be routed to source, taxonomy, evidence, rights, sensitivity, policy, access-control, independent review, correction, and release authorities. This runbook does not perform their decisions.

[Back to top](#top)

---

## 9. Public-safe derivative assessment

A public-safe derivative is a **new governed representation**, not a sanitized view of a restricted object and not an in-place mutation that erases lineage.

### 9.1 Required separation

Preserve distinct references for:

```text
source/raw occurrence
OccurrenceEvidence
OccurrenceRestricted or quarantine record
transform request
transform receipt
candidate public representation
policy decision
review record
validation report
release manifest
governed public carrier
correction and rollback lineage
```

A public object must not contain a public pointer that resolves directly to restricted geometry or source-native protected values.

### 9.2 Transform families

The Fauna sensitivity documentation discusses generalization, aggregation, masking, withholding, suppression, and delayed publication. This runbook does not select among them and deliberately does not state parameters.

A proposed transform must be:

- authorized for the source and purpose;
- deterministic where policy requires replayability;
- evaluated for repeated-release and composition attacks;
- receipt-bearing without exposing reversal-enabling details;
- validated on the output bytes and all derived carriers;
- reviewed by accountable sensitivity/geoprivacy roles;
- reversible through correction and rollback; and
- strictly upstream of public delivery.

### 9.3 Candidate admission checks

A future public-safe occurrence candidate should not advance unless all are true:

| Gate | Required closure |
|---|---|
| Identity | Stable candidate ID and digest distinct from the restricted source object |
| Source | Accepted source descriptor and permitted derivative use |
| Taxonomy | Authority-versioned concept or safe bounded label |
| Evidence | Resolved EvidenceBundle support for the exact public claim |
| Rights/stewardship | Approved audience, purpose, reuse, privacy, consent, and attribution |
| Sensitivity | Operation-specific reviewer disposition |
| Transform | Accepted method and receipt, with no protected detail in public bytes |
| Reconstruction | Direct, join, repeated-query, and side-channel assessment passes |
| Policy | Bound evaluator returns the accepted finite outcome and obligations |
| Validation | Candidate-specific positive and negative tests pass |
| Independent review | Accountable review separate from generator/operator |
| Correction | Taxonomic, source, rights, sensitivity, or evidence change can propagate |
| Rollback | Prior safe carrier and cache/index invalidation target identified |
| Release | Separate release authority and manifest close |

At the current checkpoint, this matrix does not close for a real Fauna occurrence. The correct default remains `HOLD` or `DENY`, not optimistic release.

### 9.4 Public-byte inspection

Review the actual candidate artifacts, not only a source object or rendering screenshot. Inspect, as applicable:

- JSON fields, headers, links, and error messages;
- vector-tile properties and source-layer contents;
- PMTiles/COG/GeoParquet metadata and sidecars;
- map feature IDs, promote IDs, cluster behavior, hover/click payloads, and feature state;
- report tables, footnotes, alt text, captions, filenames, and embedded metadata;
- graph nodes/edges and search index terms;
- cache keys, URL state, deep links, analytics, and logs; and
- AI retrieval chunks, citations, prompts, tool outputs, summaries, and abstention behavior.

The safest representation may be no geometry, no taxon label, a broad aggregate, delayed release, restricted access, or no release at all.

[Back to top](#top)

---

## 10. Finite outcomes and reason codes

### 10.1 Validator findings

The current occurrence validator uses stable code families. These examples are operationally relevant and reveal no protected values.

| Code or family | Meaning | Operator response |
|---|---|---|
| `schema.*` | Shape, declared-check, finite-state, fixture, or canonical-array inconsistency | Return to WORK; do not interpret as sensitivity decision |
| `identity.*` | Hash or occurrence ID mismatch/unavailable | Stop; verify immutable input and identity subject |
| `obs.source_role_mismatch` | Canonical source role and basis of record conflict | Quarantine; correct through governed lineage |
| `prov.raw_artifact_ref_required` | Required source-bound support missing | `HOLD_FOR_EVIDENCE` or source/provenance repair |
| `rights.unresolved` | Declared rights are incomplete or unresolved | `HOLD_FOR_RIGHTS` |
| `taxon.accepted_name_unresolved` | Bounded accepted-name check unresolved | `HOLD_FOR_TAXONOMY` |
| `geom.public_safe_geometry_required` | Non-open/generalized/withheld posture lacks explicit public-safe geometry object | Quarantine; do not infer a safe representation |
| `geom.public_safe_precision_invalid` | Generalization-required output claims exact public precision | `DENY` current candidate; request governed transform review |
| `geom.withheld_geometry_required` | Withhold-required posture does not declare withheld public geometry | Quarantine or deny |
| `geom.withheld_coordinates_forbidden` | Withheld public geometry still contains coordinates | Stop; treat as potential exposure |
| `sens.exact_location_public_safe_conflict` | Exact-public claim conflicts with geoprivacy/generalization/withholding | `DENY` or narrow request |
| `geom.exact_public_geometry_required` | Exact-public declaration lacks matching exact public geometry | Return to WORK; exact exposure still needs policy/review |
| `sens.review_required` | Sensitive-species flag lacks required review posture | `HOLD_FOR_SENSITIVITY_REVIEW` |
| `sens.review_reason_required` | Review-pending candidate lacks canonical hold reason | Correct metadata; remain held |
| `sens.review_reason_stale` | Hold reason remains after declared review condition changed | Reconcile state and audit lineage |

`sens.steward_review_required` is the current candidate reason expected when review remains pending. It is a hold reason, not a finding that grants authority.

### 10.2 Runbook disposition codes

| Disposition | Meaning | Public effect |
|---|---|---|
| `NO_ACTION` | Duplicate or already governed task; no new work | None |
| `QUARANTINE` | Candidate remains non-public while defects or authority gaps are resolved | None |
| `HOLD_FOR_*` | Named gate is incomplete | None |
| `RESTRICTED_HANDOFF_READY` | Public-safe metadata packet is ready for authorized restricted-handling review | None |
| `PUBLIC_DERIVATIVE_REQUEST_READY` | Public-safe metadata packet may request a separate derivative process | None |
| `DENY` | Requested operation or precision is not permitted under current evidence/controls | None |
| `ABSTAIN` | Evidence or interpretation is insufficient for the requested claim | None |
| `ERROR` | Machine, identity, environment, or procedure failed | None |

Do not convert one disposition into another merely to make a workflow green. Preserve the reason and the state transition history.

### 10.3 Public reason language

Public-facing reasons should explain the boundary without revealing protected detail. Examples:

```text
Sensitive-location review is incomplete.
Required source-use authority is unresolved.
The requested precision is not available for public use.
Evidence is insufficient for the requested claim.
A public-safe representation has not been released.
```

Do not disclose the exact taxon/site, hidden coordinate, transform parameters, reviewer rationale, source-native ID, or inference path in a public reason.

[Back to top](#top)

---

## 11. Public-safe review handoff

### 11.1 Required packet

The handoff should contain only:

- opaque review and candidate IDs;
- repository base and validator version;
- immutable candidate digest;
- source descriptor and EvidenceRef pointers that resolve only for authorized reviewers;
- requested purpose, audience, operation, and precision class;
- source role and basis class when safe to disclose;
- machine outcome and safe finding codes/paths;
- taxonomy, evidence, rights, sensitivity, geoprivacy, policy, access, correction, and rollback statuses;
- proposed runbook disposition;
- required reviewer roles and separation-of-duties gaps;
- public-safe derivative request reference, if any;
- non-effects; and
- review expiration or revalidation triggers.

### 11.2 Prohibited packet content

Do not include:

- exact or approximate coordinates, bounding boxes, centroids, routes, polygons, or site labels;
- fine observation time when it increases risk;
- protected taxon identity or status when the label is itself sensitive;
- source-native, observer, media, device, project, permit, parcel, institution, or private agreement identifiers;
- screenshots or maps of protected context;
- raw records, excerpts, exports, or reversible encodings;
- transform radii, seeds, offsets, grid rules, masks, thresholds, or suppression secrets;
- private reviewer rationale or credentials;
- evidence excerpts not cleared for the handoff audience; or
- release language such as `approved`, `public`, or `publishable` unless a separate governing object already establishes that state and the packet merely cites it.

### 11.3 Handoff verification

Before sending:

1. inspect the packet as an untrusted recipient would;
2. search for location-bearing fields, coordinate-like values, live URLs, embedded metadata, and protected identifiers;
3. verify all references enforce audience restrictions;
4. confirm the packet cannot be joined with public KFM surfaces to narrow a site;
5. confirm no workflow or bot will echo the packet into public logs;
6. record correction and rollback contacts; and
7. state that review, release, deployment, promotion, and publication remain separate.

[Back to top](#top)

---

## 12. Correction, withdrawal, and rollback

### 12.1 Exposure or near-exposure response

When protected detail may have reached an unauthorized surface:

1. **Stop distribution and automated processing.** Do not reproduce the value to confirm it publicly.
2. **Preserve a private incident reference.** Record affected object/carrier identifiers without copying protected payloads into public systems.
3. **Notify authorized sensitivity, security, source, rights, release, and correction owners.** Use private channels appropriate to the incident.
4. **Identify every derived carrier.** Include repositories, branches, workflow logs/artifacts, caches, tiles, APIs, exports, indexes, graphs, reports, AI retrieval stores, and downstream mirrors.
5. **Withdraw or restrict through owning controls.** Do not rely on UI hiding.
6. **Invalidate caches and derived indexes.** Confirm propagation rather than assuming expiry.
7. **Issue correction/withdrawal records and lineage.** Preserve why and what supersedes the unsafe state without publishing protected detail.
8. **Re-evaluate transform, policy, review, and release controls.** A single bad carrier may reveal a systemic composition gap.
9. **Verify the safe state from an unauthorized-client perspective.** Avoid using privileged access as proof of public behavior.
10. **Record rollback and follow-up proof.** A deletion request alone is not closure.

Use the [Fauna Rollback Runbook](./ROLLBACK_RUNBOOK.md) for the domain rollback path and the repository's governing correction/withdrawal procedures for public state.

### 12.2 Taxonomic, source, or sensitivity change

A record may become more sensitive after release because of:

- taxonomic split, merge, synonym, or identification correction;
- new rarity or regulatory information;
- source withdrawal or terms change;
- newly discovered sensitive-site association;
- a new re-identifying join or public dataset;
- improved inference techniques;
- changed steward, community, landowner, privacy, or consent requirement; or
- correction of observation time, geometry, or method.

Treat these as correction triggers. Re-run sensitivity and public-byte review; do not assume an earlier release remains safe.

### 12.3 Rollback target

Every released public-safe derivative should identify:

- prior safe manifest/carrier;
- candidate and restricted lineage;
- affected catalogs, tiles, APIs, caches, search, graph, exports, and AI indexes;
- invalidation/rebuild commands or owners;
- correction and withdrawal references;
- verification method and audience; and
- criteria for re-release.

This runbook creates none of those objects. Missing rollback closure returns `HOLD_FOR_ROLLBACK`.

[Back to top](#top)

---

## 13. Hosted CI and exact-head evidence

### 13.1 Relevant workflows

| Workflow | Current bounded scope | Relationship to this runbook |
|---|---|---|
| `fauna-occurrence-evidence` | Closed draft schema, deterministic identity, role/rights/sensitivity consistency, exact synthetic fixtures, authoring receipt | Path-filtered; this runbook-only change does not by itself exercise the occurrence implementation |
| `domain-fauna` | Synthetic public-safe fixture validation plus explicit proof/release holds | Runs on pull requests; validates only its declared synthetic boundary |
| Repository docs/validator workflows | Markdown, stale-doc, topology, link, or general repository checks as configured | May validate document structure or expose inherited baseline debt |

A workflow result is valid PR evidence only when it belongs to the exact current head SHA and relevant event. A green hold job means the hold check behaved as designed; it does not mean the held capability exists.

### 13.2 Exact-head reporting template

```text
PR: <number>
base: <base branch>@<base SHA>
head: <branch>@<exact head SHA>
changed paths: <verified list>
workflow: <name>
run id: <id>
event: pull_request
status: queued | in_progress | completed
conclusion: success | failure | cancelled | skipped | neutral | action_required
introduced/shared/inherited classification: <evidence>
review state: pending | approved | changes requested
release/deployment/promotion/publication effect: none
```

### 13.3 Failure classification

Before attributing a failure to this runbook:

1. verify the run tested the exact current head;
2. inspect the failing job and step;
3. identify the exact file, rule, test, or fingerprint;
4. compare with current base or peer documentation PRs when evidence exists;
5. determine whether the target Markdown introduced the failure;
6. keep inherited repository debt separate from introduced defects; and
7. correct introduced defects without weakening a governing validator or baseline.

Do not dismiss a failure merely because the change is documentation-only. Do not claim a shared failure is introduced without path or behavior evidence.

[Back to top](#top)

---

## 14. Current holds and graduation criteria

### 14.1 Current hold register

| Capability | Current status | Graduation evidence required |
|---|---|---|
| Real source admission | `HOLD` | Accepted source descriptors, authority roles, terms, sensitivity floor, and resolver integration |
| Real taxonomy resolution | `HOLD` | Version-pinned authority snapshot, deterministic resolver, review/correction path |
| EvidenceBundle resolution | `HOLD` | Resolvable bundles and proof closure for the exact claim |
| Fauna sensitivity policy | `HOLD` | Accepted policy source, tests, bundle selection, evaluator, finite outcomes, and obligations |
| Sensitivity review | `HOLD` | Accountable named roles, access control, review record, and separation of duties |
| Geoprivacy transform | `HOLD` | Functional executor, accepted profile, deterministic/secure proof, receipt, and reconstruction tests |
| `OccurrenceRestricted` machine path | `HOLD` | Closed schema, fixtures, validator, access-control tests, correction path |
| `OccurrencePublic` machine path | `HOLD` | Closed schema, candidate validator, public-byte negative tests, policy/review/release integration |
| SensitiveSite machine path | `HOLD` | Closed schema, fixtures, policy, access and transform tests |
| Candidate-specific release | `HOLD` | Candidate dossier, policy/review/validation/proof/manifest/correction/rollback closure |
| Governed public response | `DENY BY DEFAULT` | Released public-safe carrier, governed API enforcement, finite negative states, audit and rollback proof |

### 14.2 Minimum graduation slice

The smallest credible successor is not live public release. It is a no-network, synthetic, dependency-closed review proof that:

1. starts from the existing sensitive-withheld `OccurrenceEvidence` fixture;
2. produces an explicit restricted or quarantine decision under a reviewed finite policy profile;
3. creates a synthetic public-safe derivative candidate with no protected values;
4. emits a fixture-only redaction/withholding receipt;
5. proves rejection of exact, reverse-engineerable, repeated-query, and join-based leakage;
6. records review separation, correction, and rollback references;
7. returns only `HOLD`, `DENY`, `ABSTAIN`, or a narrowly named review-ready state; and
8. has no source activation, lifecycle write, release, deployment, or publication effect.

That slice still would not authorize real occurrence handling. Real-source graduation requires separate terms, stewardship, security, access-control, and operational review.

### 14.3 Definition of done for this runbook

This documentation update is complete when:

- the prior scaffold is replaced at the same path;
- current executable and held states are distinguished;
- sensitive payloads and reversal-enabling details are absent;
- occurrence, site, source role, taxonomy, evidence, policy, review, transform, release, and correction responsibilities remain separate;
- commands are copied from current repository workflows/validators and labeled by scope;
- finite outcomes and stop conditions are explicit;
- a public-safe handoff template and rollback path exist;
- internal headings, anchors, and repository-relative links resolve; and
- the change remains one reversible documentation path on a review branch.

[Back to top](#top)

---

## 15. Maintenance and document rollback

Review this runbook when any of the following changes:

- the `OccurrenceEvidence`, `OccurrenceRestricted`, `OccurrencePublic`, or `SensitiveSite` contract/schema editions;
- validator result fields, reason codes, CLI output, or identity subject;
- accepted source-role vocabulary;
- source-authority or Fauna source-registry state;
- sensitivity tiers/rubrics, policy package, evaluator, or geoprivacy profile authority;
- review roles, access-control model, or separation-of-duties requirements;
- public-byte carriers, governed API, MapLibre/Evidence Drawer/Focus Mode behavior;
- correction, withdrawal, cache invalidation, or rollback mechanics;
- release candidate/manifest topology; or
- hosted workflow triggers, commands, or required checks.

When implementation and this runbook conflict, treat the discrepancy as drift. Do not rewrite current behavior from memory or make the document sound more mature than the repository evidence.

### Document rollback

Before merge, close the draft pull request and delete or abandon its feature branch. `main` remains unchanged.

After an authorized merge, use a transparent revert or reviewed forward correction against the actual merge commit. Do not rewrite shared history. Reverting this Markdown file does not withdraw a source, delete an occurrence, reverse a policy decision, or roll back a public release because the document itself performs none of those actions.

[Back to top](#top)

---

## Appendix A — Operator checklist

### Scope and environment

- [ ] Repository base and exact commit are frozen.
- [ ] Candidate uses an opaque ID and immutable digest.
- [ ] Purpose, audience, operation, and requested precision are explicit.
- [ ] Review environment and logging/export restrictions are authorized.
- [ ] No protected payload appears in public/shared surfaces.
- [ ] No overlapping incident, correction, withdrawal, or review owns the candidate.

### Source, taxonomy, and evidence

- [ ] Accepted source descriptor or equivalent authority record resolves.
- [ ] Source role and basis of record are consistent.
- [ ] Source terms and approved purpose cover the requested handling.
- [ ] Taxon concept and authority snapshot resolve, or review is held.
- [ ] EvidenceRefs resolve to admissible EvidenceBundles for the exact claim.
- [ ] Occurrence evidence is not overextended to range, abundance, breeding, status, or habitat claims.

### Machine validation

- [ ] Schema and validator versions are recorded.
- [ ] Identity/hash checks pass or the candidate remains in WORK/QUARANTINE.
- [ ] CLI output contains codes/paths only and no protected values.
- [ ] Outer CLI `PASS` is not confused with inner `pass/quarantine/deny/error` posture.
- [ ] Review-required sensitive records cannot claim release readiness.
- [ ] Exact/generalized/withheld geometry flags are internally consistent.

### Sensitivity and rights

- [ ] Rights, privacy, stewardship, agreement, embargo, and attribution are resolved.
- [ ] Sensitive occurrence and SensitiveSite are not collapsed.
- [ ] Taxon label, time, identifiers, media, observer, project, and join risks are reviewed.
- [ ] Repeated releases and differential queries are assessed.
- [ ] Proposed transform is authorized, receipt-bearing, and non-reversible from public details.
- [ ] Client-side hiding is not used as the protection mechanism.

### Handoff and recovery

- [ ] Public packet contains only opaque references and safe reason codes.
- [ ] Required reviewer roles and separation gaps are named.
- [ ] Correction, withdrawal, invalidation, and rollback owners are identified.
- [ ] Every affected carrier/cache/index is in the recovery scope.
- [ ] Review expiration and revalidation triggers are recorded.
- [ ] Release, deployment, promotion, and publication remain separate and unperformed.

[Back to top](#top)

---

## Appendix B — Review handoff template

```yaml
review_handoff:
  handoff_id: "opaque-review-id"
  created_at: "<UTC timestamp>"
  repository:
    name: "bartytime4life/Kansas-Frontier-Matrix"
    base_ref: "<branch or tag>"
    commit: "<immutable SHA>"
  candidate:
    opaque_id: "<non-revealing identifier>"
    spec_hash: "sha256:<digest>"
    object_family: "OccurrenceEvidence | OccurrenceRestricted | SensitiveSite | derivative-request"
    protected_payload_included: false
  request:
    purpose_ref: "<authorized purpose reference>"
    audience_class: "<controlled class>"
    operation: "<reviewed operation>"
    requested_precision_class: "<safe controlled value>"
  support:
    source_descriptor_ref: "<restricted resolver reference>"
    evidence_refs: ["<restricted resolver reference>"]
    taxonomy_review_ref: "<reference or HOLD>"
  machine_validation:
    schema_version: "<version>"
    validator_version: "<version>"
    cli_outcome: "PASS | ERROR"
    declared_candidate_result: "pass | quarantine | deny | error"
    finding_codes: []
    finding_paths: []
    protected_values_logged: false
  gate_status:
    source: "CONFIRMED | HOLD | DENY"
    taxonomy: "CONFIRMED | HOLD | ABSTAIN"
    evidence: "CONFIRMED | HOLD | ABSTAIN"
    rights_and_stewardship: "CONFIRMED | HOLD | DENY"
    sensitivity_review: "CONFIRMED | HOLD | DENY"
    geoprivacy_transform: "NOT_REQUIRED | HOLD | REVIEWED"
    reidentification_review: "CONFIRMED | HOLD | DENY"
    policy: "CONFIRMED | HOLD | DENY | ABSTAIN"
    access_control: "CONFIRMED | HOLD | DENY"
    correction_path: "CONFIRMED | HOLD"
    rollback_path: "CONFIRMED | HOLD"
  disposition:
    outcome: "QUARANTINE | HOLD_FOR_* | RESTRICTED_HANDOFF_READY | PUBLIC_DERIVATIVE_REQUEST_READY | DENY | ABSTAIN | ERROR"
    public_reason: "<non-revealing reason>"
    protected_rationale_ref: "<private reference>"
  required_review_roles: []
  revalidate_on:
    - "source terms or withdrawal"
    - "taxonomic change"
    - "sensitivity or policy change"
    - "new join, carrier, or inference risk"
    - "correction or rollback event"
  non_effects:
    source_activation: false
    lifecycle_promotion: false
    release: false
    deployment: false
    publication: false
```

[Back to top](#top)

---

## Appendix C — Evidence basis

### Repository evidence inspected

- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) and [pull-request template](../../../.github/PULL_REQUEST_TEMPLATE.md) for contribution, review, sensitive-data, validation, and rollback discipline.
- [Directory Rules](../../doctrine/directory-rules.md) and accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) for same-path placement and authority separation.
- [Sensitive-domain fail-closed architecture](../../architecture/sensitive-domain-fail-closed.md) for operation-specific closure and pre-delivery protection.
- [Fauna sensitivity](../../domains/fauna/SENSITIVITY.md), [sources](../../domains/fauna/SOURCES.md), and [source roles](../../domains/fauna/SOURCE_ROLES.md) for deny-by-default, source-role, and geoprivacy posture.
- [`OccurrenceEvidence`](../../../contracts/domains/fauna/occurrence_evidence.md), [`OccurrencePublic`](../../../contracts/domains/fauna/occurrence_public.md), [`OccurrenceRestricted`](../../../contracts/domains/fauna/occurrence_restricted.md), and [`SensitiveSite`](../../../contracts/domains/fauna/sensitive_site.md) for object-family boundaries and current maturity.
- [`OccurrenceEvidence` validator](../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py), [fixtures](../../../fixtures/domains/fauna/occurrence_evidence/README.md), and [tests](../../../tests/domains/fauna/test_occurrence_evidence.py) for the bounded machine profile and reason codes.
- [Synthetic public-safe fixture validator](../../../tools/validators/domains/fauna/validate_public_safe_fixture.py) and [Fauna smoke tests](../../../tests/domains/fauna/test_fauna_smoke.py) for payload-minimizing synthetic safety checks.
- [`fauna-occurrence-evidence`](../../../.github/workflows/fauna-occurrence-evidence.yml) and [`domain-fauna`](../../../.github/workflows/domain-fauna.yml) workflows for current commands, triggers, and held capability boundaries.
- [Fauna sensitivity-policy scaffold](../../../policy/sensitivity/fauna/README.md) and [rare-species Rego stub](../../../policy/domains/fauna/rare_species_redaction.rego) for the explicit non-enforcement posture.
- [Source-authority register](../../../control_plane/source_authority_register.yaml) and [Fauna source-registry lane](../../../data/registry/sources/fauna/README.md) for current source-admission gaps.
- [Restricted occurrence lane](../../../data/processed/fauna/restricted/occurrences/README.md), [generalized occurrence candidate lane](../../../data/processed/fauna/public/occurrences_generalized/README.md), and [Fauna release candidates](../../../release/candidates/fauna/README.md) for lifecycle and public-candidate boundaries.

### Evidence limits

- Repository files prove bytes and declared boundaries at the pinned commit, not operational deployment or public safety.
- Synthetic fixtures prove only their declared cases and contain no real biological evidence.
- A validator pass proves only current schema and bounded consistency checks.
- Draft contracts and scaffold schemas do not prove conversion or runtime enforcement.
- Rego source without a bound evaluator and tested consumer does not prove policy effect.
- CODEOWNERS routing does not prove accountable specialist authority or branch-protection enforcement.
- This runbook does not establish source admission, taxonomic truth, rights clearance, sensitivity classification, geoprivacy sufficiency, review approval, release, deployment, promotion, or publication.

[Back to top](#top)
