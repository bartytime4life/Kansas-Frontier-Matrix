<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-review-readme
title: policy/review/ — Review Admissibility Policy Boundary
type: readme
version: v0.1
status: draft; BOUNDARY_COMPACT; repository-grounded; proposed-inactive; non-runtime; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ review to @bartytime4life; no accepted review-policy steward or independent approver was established
created: 2026-05-08
updated: 2026-08-13
policy_label: public; policy; review; trust-boundary; proposed-inactive; non-release; non-publication
owning_root: policy/
responsibility: Define the local policy-source boundary for review sufficiency, reviewer-role, authority-binding, independence, and escalation conditions without storing review records, authenticating reviewers, executing policy, approving release, or publishing data.
truth_posture: CONFIRMED accepted placement under policy/, exact three-entry local tree, one no-op proposed Rego stub, one empty placeholder child, separate fixture-tested inactive reviewer-role and review-authority profiles, and no local runtime or release authority / PROPOSED BOUNDARY_COMPACT contract and future fail-closed review-policy authoring posture / NEEDS VERIFICATION accepted local scope ID, steward assignments, rule inputs and outcomes, bundle and evaluator binding, native tests, governed consumers, independent reviewer capacity, required-check enforcement, correction propagation, and release integration
related:
  - ../README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../control_plane/root_registry.yaml
  - ../../contracts/policy/policy_reviewer_role_vocabulary.md
  - ../decision/reviewer_roles.v1.json
  - ../../contracts/governance/review_authority_binding.md
  - ../../contracts/governance/ReviewRecord.md
  - ../../contracts/review/README.md
  - ../../release/reviews/README.md
  - ../../data/proofs/review/README.md
  - ../../.github/workflows/policy-test.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: review

`policy/review/` is KFM's local policy-source boundary for deciding whether a
review requirement is satisfied, unresolved, restricted, or must fail closed.
It inherits the authority and limitations of [`policy/`](../README.md).

> [!IMPORTANT]
> **Safe current conclusion:** this lane is proposed and inactive. Its only
> Rego module is an explicit greenfield stub with no operative rule, and its
> only child directory contains an empty marker. Separate reviewer-role and
> review-authority profiles have deterministic fixture validation, but neither
> profile activates this lane or grants review, mutation, release, or
> publication authority.

> [!CAUTION]
> [`two_steward_required.rego`](./two_steward_required.rego) defines
> `default deny := false`. Because every denial body is commented out, the
> module currently denies nothing. Do not cite the filename, package name,
> repository location, or a green unrelated workflow as evidence that two
> stewards are required or that separation of duties is enforced.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Decision boundaries](#decision-and-object-family-boundaries) · [Separation of duties](#reviewer-roles-authority-and-separation-of-duties) · [Runtime and release](#rule-source-runtime-evaluation-and-release) · [Related evidence](#related-contracts-schemas-fixtures-tests-and-workflows) · [Validation](#validation-coverage-and-limits) · [Contributing](#contributor-contract) · [Correction](#correction-supersession-and-rollback) · [Open verification](#open-verification-register)

## Purpose

This boundary may hold reviewed, versioned policy source that evaluates
review-related admissibility. A mature rule family could determine whether a
bounded operation has the required review roles, current assignments,
independent actors, subject and digest binding, eligible dispositions,
evidence support, effective time, and unresolved obligations.

The boundary answers a policy question:

> Given an explicit operation, subject, review requirement, reviewer-role and
> authority context, review evidence, policy version, and effective time, is
> the review condition satisfied—and what hold, denial, abstention,
> restriction, or escalation obligations remain?

It does **not** answer whether a claim is true, assign a person to a role,
authenticate an actor, record that a review happened, approve a change,
authorize a lifecycle transition, approve release, or publish an artifact.

This README documents current repository evidence. It does not activate the
stub, accept a reviewer vocabulary, adopt the draft separation-of-duties model,
or create an enforcement claim.

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical responsibility root for normative allow, deny, hold, restrict, and abstain rule source. |
| Directory profile | `BOUNDARY_COMPACT`: this lane changes review, authority, independence, and release trust assumptions. |
| Governing placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy from contracts and schemas and define the local README contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry projects adopted governance; it does not create it. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing is not proof of review, qualification, independence, role assignment, or approval. |
| Local owner | **NEEDS VERIFICATION.** No accepted review-policy steward or independently authorized approver was established in the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted machine scope identifier for `policy/review/` was found in the reviewed root projection or target tree. This README does not invent one. |
| Release authority | None. A review-policy result may become one input to a governed release decision; it cannot approve release itself. |
| Publication authority | None. Public carriers require separate evidence, policy, review, release, correction, and rollback closure. |

## Current status

All observations in this section are pinned to
`main@09a01ef8a71a557efc1c35bda6f9b762a429a1f3`.

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| Target README | 44-byte greenfield stub, blob `82eb4cf18445e859abbc4478aa6c948a71b03363` | The local authority and non-ownership contract was previously absent. |
| `two_steward_required.rego` | 344-byte `PROPOSED` stub; package `kfm.two_steward_required`; `default deny := false`; all example denial logic commented out | The module currently has no operative two-steward, evidence, or separation-of-duties rule. |
| `release/` child | Contains only an empty `.gitkeep` blob | It is placeholder topology, not a release-review rule set, record lane, bundle, evaluator, or consumer. |
| Reviewer-role vocabulary | Separate `PROPOSED_INACTIVE` contract, registry, schema, fixtures, validator, tests, and read-only workflow | Five stable role codes are fixture-tested as an inactive vocabulary; they assign no people and grant no authority. |
| Review-authority binding | Separate `proposed-inactive`, fixture-only contract, schema, fixtures, validator, tests, and read-only workflow | Structural `BOUND`/`HOLD`/`DENY` projection is testable; actor authentication, policy resolution, write authority, and release remain out of scope. |
| Local native tests | No native Rego test or dedicated workflow is present beside the stub | Parsing, inputs, outcomes, fail-closed behavior, bundle membership, and evaluator compatibility are not established. |
| Runtime and consumer | No accepted local evaluator, bundle selector, decision emitter, or governed consumer is established by the reviewed lane | Repository source presence is not operational enforcement. |
| Independent review | CODEOWNERS names one account; draft ADR-0024 records reviewer-capacity and enforcement gaps | Independent qualified reviewer capacity and machine-enforced separation of duties remain unverified. |
| Release and publication | Owned by separate governed roots and transitions | Nothing in this directory releases, publishes, corrects, withdraws, or rolls back an object. |

The nearby [ADR-0024 separation-of-duties proposal](../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md)
is `draft`. It is useful design and gap evidence, but it is not adopted authority
for claiming that the proposed model is enforced.

## Current direct-child map

The map is verified from the complete direct-child tree at the pinned baseline.
It shows this directory and direct children only, as required by Directory
Rules `DIR-README-003` through `DIR-README-005`.

```text
policy/review/
├── README.md                    # local boundary and contributor contract
├── release/                     # empty placeholder; ownership remains unresolved
└── two_steward_required.rego    # proposed no-op rule stub; not activated
```

Presence in this map establishes only that the path is tracked. The
`release/` child must not become a parallel home for release-policy source,
release review records, or release decisions. Its intended relationship to
[`policy/release/`](../release/README.md) and
[`release/reviews/`](../../release/reviews/README.md) is **NEEDS
VERIFICATION** before new authority-bearing files are added.

## What belongs here

Subject to accepted contracts, schemas, policy conventions, and evaluator
binding, this boundary may contain:

- declarative policy source that checks operation-specific review
  prerequisites;
- rules for required reviewer-role classes, subject binding, effective windows,
  independence, recusal, disposition eligibility, and unresolved obligations;
- fail-closed conditions for missing, stale, superseded, revoked, mismatched, or
  unauthenticated review context;
- public-safe reason codes and enforceable escalation, hold, redaction,
  re-review, or abstention obligations;
- bounded rule-family documentation naming exact inputs, native outcomes,
  normalized outcomes, bundle and evaluator identity, tests, consumers,
  supersession, and rollback; and
- versioned policy references that a separately governed decision or release
  record can cite without copying the rule or its authority.

A review topic or domain remains a lane beneath the `policy/` responsibility
root. It does not become a new authority root.

## What is prohibited

| Prohibited material or claim | Owning surface or required action |
|---|---|
| Meaning of `ReviewRecord`, reviewer roles, assignments, review authority, or release objects | [`contracts/`](../../contracts/README.md) semantic authority |
| JSON Schema, DTO, enum, or machine field shape | [`schemas/`](../../schemas/README.md) machine-shape authority |
| Reviewer identity, credential, account, group membership, qualification, delegation, or assignment instance | Governed identity and stewardship records; never infer from a role token or username string |
| Emitted review, assignment, policy-decision, validation, receipt, proof, promotion, release, correction, withdrawal, or rollback instances | Their owning process, `data/`, proof, or [`release/`](../../release/README.md) object families |
| EvidenceBundle contents, citations, proofs, or claim truth | Evidence and proof responsibility; policy may consume references but cannot create support |
| Reusable evaluator, API, UI, cache, storage, deployment, or authentication code | `packages/`, `apps/`, `runtime/`, `tools/`, or `infra/` according to responsibility |
| Reusable synthetic fixtures and executable conformance tests | Root [`fixtures/`](../../fixtures/README.md) and [`tests/`](../../tests/README.md), except an explicitly accepted engine-native co-location profile |
| Release review records or release decisions | [`release/reviews/`](../../release/reviews/README.md) or another accepted release object-family lane |
| Secrets, credentials, private review notes, personal data, protected cultural information, genomic material, exact sensitive locations, or exploit-enabling infrastructure detail | Keep out of Git, policy reasons, tests, logs, documentation, and generated receipts; use authorized restricted systems |
| A filename, comment, default, workflow, CODEOWNERS route, PR approval, or string inequality presented as proof of independent review | Resolve actor identity, current authority, subject binding, policy, review evidence, and required separation through accepted mechanisms |
| Generated language or AI output presented as approval | Route through authorized human review and governed decision records; generation is never approval |

Existing placeholder paths do not authorize prohibited writes. Any migration or
convergence work must preserve history, repair references, avoid two writable
authorities, and name correction and rollback behavior.

## Inputs and outputs

### Candidate evaluation inputs

A mature review-policy evaluation should receive explicit, normalized,
versioned context and must not silently fetch missing facts. Depending on the
accepted rule family, inputs may include:

- operation, purpose, audience, risk class, lifecycle transition, and requested
  effect;
- stable subject reference, object type, version or digest, scope, and effective
  time;
- required reviewer-role classes and separation constraints;
- governed reviewer actor and current assignment references, including role,
  scope, status, effective window, delegation, and recusal context;
- subject-bound `ReviewRecord` or proof references with disposition, reasons,
  obligations, issuance time, supersession, and revocation state;
- EvidenceRef-to-EvidenceBundle resolution, validation, source-role, rights,
  consent, sensitivity, and correction posture when material;
- exact policy source or bundle ID, digest, evaluator version, entrypoint, and
  input hash; and
- release-candidate, correction, withdrawal, or rollback references when the
  operation crosses that boundary.

**Current limitation:** the local Rego stub defines no accepted input profile
and reads no operative input. The list above is an inherited authoring
requirement, not a claim that current code consumes these fields.

### Source and evaluated outputs

Authoring in this directory produces versioned policy source and documentation.
Those artifacts are not evaluated decisions.

If an accepted evaluator later executes a rule, the result should preserve a
finite native outcome, public-safe reasons, obligations, exact policy and input
identity, effective time, and replay information. An accepted normalization
contract must map that native result into the applicable outward decision
vocabulary without collapsing:

- approval into evidence truth;
- hold or abstention into approval;
- evaluator error into denial or allow;
- role vocabulary into actor authority;
- structural binding into authentication; or
- policy satisfaction into promotion, release, or publication.

The current stub produces no governed `PolicyDecision`, `ReviewRecord`, proof,
receipt, release decision, or public payload.

## Decision and object-family boundaries

| Surface | Question it owns | Relationship to `policy/review/` |
|---|---|---|
| [`contracts/governance/ReviewRecord.md`](../../contracts/governance/ReviewRecord.md) | What does an individual review record mean? | Consume accepted meaning; never redefine it in Rego or this README. |
| [`contracts/policy/policy_reviewer_role_vocabulary.md`](../../contracts/policy/policy_reviewer_role_vocabulary.md) | What do stable reviewer-role classes mean? | Reference the inactive vocabulary only with its status and authority flags intact. |
| [`contracts/governance/review_authority_binding.md`](../../contracts/governance/review_authority_binding.md) | How can declared review, assignment, and subject projections be checked for structural agreement? | Treat a `BOUND` candidate as structural support only, never authentication or permission. |
| [`contracts/review/`](../../contracts/review/README.md) and [`schemas/contracts/v1/review/`](../../schemas/contracts/v1/review/README.md) | What do review-family interfaces mean and what shapes are valid? | Consume accepted versions; do not create a duplicate review-object family here. |
| [`data/proofs/review/`](../../data/proofs/review/README.md) | Where does review-proof support belong? | Consume governed references; proof supports but does not replace policy or release decisions. |
| [`release/reviews/`](../../release/reviews/README.md) | Where does release-review record guidance live? | Supply exact policy references and results when required; never store records here. |
| [`release/`](../../release/README.md) | Who owns promotion, release, correction, withdrawal, and rollback decisions? | Provide one bounded gate input; never perform the transition. |

Review request, role definition, actor assignment, review action, review proof,
policy evaluation, accountable decision, execution receipt, and publication are
distinct objects and transitions. They may reference one another; they must not
be collapsed into a single file, boolean, comment, or workflow result.

## Reviewer roles, authority, and separation of duties

The repository contains a fixture-tested, `PROPOSED_INACTIVE` reviewer-role
vocabulary with five role codes:

| Proposed role code | Bounded responsibility class | Authority limit |
|---|---|---|
| `DOMAIN_STEWARD` | Domain meaning, burden, and admissibility implications | Does not assign a domain steward or record approval. |
| `EVIDENCE_STEWARD` | Evidence resolution, provenance, freshness, and support burden | Does not create evidence or certify truth. |
| `POLICY_STEWARD` | Policy source, outcomes, reasons, obligations, and fail-closed behavior | Does not accept or activate policy alone. |
| `RELEASE_STEWARD` | Release eligibility, proof, correction, and rollback posture | Does not release or publish by role token. |
| `SECURITY_PRIVACY_REVIEWER` | Security, privacy, access, living-person, sensitive-location, and exposure controls | Does not clear risk without a governed review action. |

The registry's authority flags are all `false`. Acceptance of the vocabulary,
assignment of qualified people, current authority resolution, subject-bound
review, and independent approval are separate governance actions.

The fixture-only `ReviewAuthorityBinding` profile tests declared actor/role,
subject, time-window, status, disposition, and author/reviewer separation. Its
`BOUND`, `HOLD`, and `DENY` outcomes are useful candidate semantics, but a valid
binding still does not authenticate an actor, resolve policy, emit a write,
approve merge, promote, release, deploy, publish, or authorize public use.

When independence is required and no qualified independent reviewer can be
resolved, the safe posture is `HOLD`, `DENY`, or `ABSTAIN` according to an
accepted operation-specific contract—not self-approval, username inequality,
or silent role substitution.

## Exposure, mutation, retention, and sensitivity

| Dimension | Boundary contract |
|---|---|
| Repository visibility | The repository is public, so tracked policy source and documentation are publicly readable. That visibility is not permission to expose restricted review material. |
| Operating exposure | The root registry classifies `policy/` as internal. Normal clients consume governed decisions and released public-safe artifacts, not repository policy source. |
| Mutation | Versioned and review-bound. Material rule changes preserve package and entrypoint identity, prior versions, effective time, tests, bundle/evaluator binding, reasons, obligations, and supersession lineage. |
| Retention | Durable policy source and Git history. Review records, assignments, receipts, proofs, release records, and protected payloads retain under their owning roots and policies. |
| Generation | Generated or scaffolded source remains proposed until provenance, review, tests, deterministic regeneration where applicable, bundle/evaluator binding, and consumer evidence exist. |
| Sensitive review | Detailed reasons, identities, conflicts, private deliberation, or hidden facts may require restricted handling. Public-safe reason codes must not reveal the fact they protect. |

Missing or untrusted evidence, rights, consent, sensitivity, source-role,
identity, assignment, review, release, or correction context must not fall back
to allow. Appropriate safe outcomes include hold, deny, abstain, quarantine,
redaction, generalization, delayed action, or authorized escalation.

That is the inherited governance posture. It is not a claim that the current
stub enforces it.

## Rule source, runtime evaluation, and release

| Stage | Owning responsibility | What this directory may do | What it cannot do |
|---|---|---|---|
| Rule source | `policy/review/` under [`policy/`](../README.md) | Hold reviewed declarative review-admissibility rules and exact policy references. | Create review facts, actor authority, evidence, or release state. |
| Meaning | [`contracts/`](../../contracts/README.md) | Reference accepted review, role, assignment, binding, decision, and release semantics. | Redefine semantic objects locally. |
| Machine shape | [`schemas/`](../../schemas/README.md) | Reference accepted schemas. | Treat Rego or prose as schema authority. |
| Runtime evaluation | An accepted evaluator and bundle contract | Supply exact versioned source, package, and entrypoint. | Execute itself, perform hidden fetches, authenticate actors, or invent normalization. |
| Review evidence | Governed record and proof mechanisms | Require explicit subject-bound references. | Store records here or treat a PR approval as the general review record. |
| Public enforcement | Governed server-side interfaces and released public-safe carriers | Provide one accepted decision input. | Rely on client hiding, UI state, AI explanation, or repository files as the control. |
| Release and correction | [`release/`](../../release/README.md) with required evidence, policy, review, proof, and receipts | Supply a result, reasons, and obligations. | Promote, release, publish, correct, withdraw, or roll back by itself. |

A schema pass, static search, Rego parse, unit test, workflow run, commit, pull
request, CODEOWNERS review, or generated receipt proves only its declared
scope. None is automatically a policy decision, independent approval, release
decision, or publication event.

## Related contracts, schemas, fixtures, tests, and workflows

### Reviewer-role vocabulary candidate

| Surface | Repository evidence | Boundary |
|---|---|---|
| [Semantic contract](../../contracts/policy/policy_reviewer_role_vocabulary.md) | Status `PROPOSED_INACTIVE`; five role classes | Meaning only; no assignments or authority. |
| [Registry candidate](../decision/reviewer_roles.v1.json) | Version `v1`; all authority flags `false` | Inactive policy vocabulary source. |
| [Schema](../../schemas/contracts/v1/policy/policy_reviewer_role_vocabulary.schema.json) | Closed candidate shape | Shape validation is not adoption. |
| [Fixtures](../../fixtures/contracts/v1/policy/policy_reviewer_role_vocabulary/) | Positive and negative cases | Synthetic evidence only. |
| [Validator](../../tools/validators/policy/validate_policy_reviewer_role_vocabulary.py) and [tests](../../tests/validators/test_validate_policy_reviewer_role_vocabulary.py) | Deterministic registry and fixture checks | Not a Rego evaluator or authority resolver. |
| [Workflow](../../.github/workflows/policy-reviewer-role-vocabulary.yml) | Read-only, no-network, path-scoped execution | A green result does not activate the vocabulary. |

### Review-authority binding candidate

| Surface | Repository evidence | Boundary |
|---|---|---|
| [Semantic contract](../../contracts/governance/review_authority_binding.md) | `proposed-inactive`; fixture-only; no-write | Structural agreement only. |
| [Schema](../../schemas/contracts/v1/governance/review_authority_binding.schema.json) | Candidate machine shape | Does not authenticate declared values. |
| [Fixtures](../../fixtures/contracts/v1/governance/review_authority_binding/) | `BOUND`, `HOLD`, and `DENY` cases | Synthetic evidence only. |
| [Validator](../../tools/validators/governance/validate_review_authority_binding.py) and [tests](../../tests/validators/governance/test_review_authority_binding.py) | Deterministic identity and binding checks | No policy resolution, write, release, or public effect. |
| [Workflow](../../.github/workflows/review-authority-binding.yml) | Read-only, no-network fixture profile | Hosted success remains bounded to the exact tested head. |

These candidate profiles are related evidence, not direct proof that
`two_steward_required.rego` is valid, tested, bundled, evaluated, or consumed.

## Validation coverage and limits

### Current local rule coverage

| Check | Current state | What remains unproven |
|---|---|---|
| File and package presence | **CONFIRMED** | Rego parse and supported language version. |
| Default inspection | **CONFIRMED `deny := false`** | Fail-closed behavior. |
| Operative rule bodies | **CONFIRMED absent** | Any review requirement or reason code. |
| Native Rego tests | **Not present in the local lane** | Positive, negative, hold, abstain, error, replay, and correction behavior. |
| Bundle and evaluator binding | **UNKNOWN / not established by reviewed evidence** | Selection, digest binding, normalization, and reproducible execution. |
| Governed consumer | **UNKNOWN / not established by reviewed evidence** | Actual request, promotion, release, correction, or rollback enforcement. |
| Independent reviewer capacity | **NEEDS VERIFICATION** | Qualified human independence and fallback behavior. |

### Repository-native related checks

```bash
# Inactive reviewer-role vocabulary: shape, invariants, and synthetic cases.
python -m unittest \
  tests.validators.test_validate_policy_reviewer_role_vocabulary \
  --verbose
python tools/validators/policy/validate_policy_reviewer_role_vocabulary.py \
  --registry
python tools/validators/policy/validate_policy_reviewer_role_vocabulary.py \
  --fixtures

# Fixture-only review/assignment/subject structural binding.
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_review_authority_binding.py' \
  --verbose
python tools/validators/governance/validate_review_authority_binding.py \
  --fixtures

# Documentation structure and local-link checks for this boundary.
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --format markdown \
  policy/review/README.md
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  policy/review/README.md
```

Passing these commands proves only the bounded contract, fixture, metadata, or
local-link property each command declares. They do not test the local Rego stub,
authenticate reviewers, resolve current assignments, accept policy, change a
required check, approve release, or publish data.

Do not add the stub to a bundle or consumer merely to make a readiness check
green. Graduation requires an accepted rule contract, explicit inputs,
fail-closed native behavior, positive and negative tests, versioned reasons and
obligations, bundle/evaluator identity, normalization, governed consumer,
decision receipts, replay, correction, and rollback.

## Contributor contract

Before changing this lane:

1. Pin current `main`, read this complete README and target source, and inspect
   active work for overlapping paths.
2. Classify the change as documentation, policy source, semantic contract,
   schema, evaluator, assignment, review record, release integration, or
   structural migration; keep each artifact under its owning root.
3. Define the exact operation, subject identity and digest, required context,
   native outcomes, outward normalization, reason codes, obligations, effective
   time, supersession, and error behavior.
4. Treat missing evidence, rights, consent, sensitivity, identity, authority,
   assignment, review, or correction context as a hold, denial, abstention, or
   error under an accepted profile—never implicit allow.
5. Add deterministic, synthetic, rights-safe positive and negative tests. Cover
   wrong subject or digest, stale or revoked review, inactive or provisional
   assignment, role mismatch, author/reviewer collapse, missing specialist
   review, evaluator error, and correction invalidation where applicable.
6. Keep detailed or sensitive reasons out of public outputs, logs, fixtures,
   documentation, and generated receipts.
7. Bind any executable rule to an accepted bundle, evaluator, version, digest,
   entrypoint, input contract, normalization, consumer, receipt, replay, and
   rollback path before claiming enforcement.
8. Update this README and directly affected contracts, schemas, fixtures,
   validators, tests, workflows, consumers, and migration notes together when
   behavior actually changes.
9. Run changed-area validation, review the full diff, and keep human review,
   merge approval, policy acceptance, release, and publication as separate
   states.

Do **not** activate `two_steward_required.rego` by changing its default in
isolation. A default flip without accepted inputs, outcomes, tests, bundle
selection, evaluator compatibility, consumer behavior, and rollback would
replace one unproven posture with another.

Do **not** populate `policy/review/release/` until its responsibility is
reconciled with `policy/release/`, `release/reviews/`, and Directory Rules. A
new file must not create parallel review-policy or release-record authority.

## Review triggers

Re-review this boundary when any of the following changes:

- the stub gains operative logic, native tests, or a package/entrypoint change;
- a bundle, evaluator, selector, normalization, consumer, or decision receipt
  binds to the lane;
- reviewer-role, assignment, identity, recusal, or authority semantics change;
- review records or proof references become required for promotion, release,
  correction, withdrawal, or rollback;
- the `release/` placeholder is populated, moved, renamed, or retired;
- CODEOWNERS, required checks, reviewer capacity, or repository-control
  enforcement changes;
- ADR-0024 or a successor is accepted, rejected, superseded, or materially
  revised;
- a sensitive-domain, rights, privacy, security, or harmful-precision incident
  exposes a gap;
- correction, withdrawal, rollback, cache invalidation, or stale-review drift
  occurs; or
- parent policy, Directory Rules, or root-registry authority changes.

## Correction, supersession, and rollback

Material review-policy changes should be versioned and preserve prior policy
source, package, entrypoint, bundle, evaluator, input, test, reason, obligation,
and decision identities needed for replay. Supersession must invalidate stale
review-policy results and route affected decisions, releases, caches, and public
artifacts through their owning correction or withdrawal mechanisms.

This v0.1 change is documentation and provenance only. It changes no Rego rule,
contract, schema, registry, fixture, validator, workflow, evaluator, consumer,
review record, repository setting, release, deployment, publication, or public
artifact.

- **Before merge:** close or abandon the draft pull request and feature branch;
  `main` remains unchanged.
- **After merge:** revert the README commit and its paired generated receipt, or
  issue a transparent forward-fix PR. Do not rewrite shared history.
- **If policy behavior later changes:** restore an accepted prior
  bundle/evaluator/consumer binding through a governed rollback; do not copy a
  file into a second writable authority.
- **If public reliance exists:** a Git revert may be insufficient. Preserve
  correction, withdrawal, cache invalidation, supersession, and notification
  lineage required by the affected release.

The pre-modernization README is recoverable as blob
`82eb4cf18445e859abbc4478aa6c948a71b03363`.

## Open verification register

| ID | Question | Status |
|---|---|---|
| REV-POL-001 | What accepted scope ID and steward assignment govern `policy/review/`? | **UNKNOWN / NEEDS VERIFICATION** |
| REV-POL-002 | Should `two_steward_required.rego` be repaired as a versioned rule, replaced by a broader accepted profile, or retired? | **NEEDS DECISION** |
| REV-POL-003 | What exact input contract and finite native outcomes apply to review-policy evaluation? | **UNKNOWN** |
| REV-POL-004 | Which reason and obligation vocabularies are accepted for missing, stale, mismatched, revoked, or non-independent review? | **PROPOSED / NEEDS VERIFICATION** |
| REV-POL-005 | Which accepted identity and assignment mechanisms resolve a reviewer actor's current role, scope, delegation, recusal, and effective window? | **UNKNOWN** |
| REV-POL-006 | How do `ReviewRecord`, stewardship assignment, review proof, policy evaluation, `PromotionDecision`, and `ReleaseManifest` bind without authority collapse? | **PARTIAL fixture-only candidates; active binding unknown** |
| REV-POL-007 | Which bundle, evaluator, selector, entrypoint, normalization, and consumer would activate a review-policy rule? | **UNKNOWN** |
| REV-POL-008 | What is the authoritative purpose or retirement path for `policy/review/release/` relative to `policy/release/` and `release/reviews/`? | **HOLD / NEEDS DIRECTORY REVIEW** |
| REV-POL-009 | Which review-policy checks are required on exact PR heads, and how is branch/ruleset coupling verified? | **UNKNOWN / NEEDS VERIFICATION** |
| REV-POL-010 | Does KFM have at least two qualified independent actors for every release class that requires separation of duties? | **UNKNOWN; draft ADR-0024 records a capacity hold** |
| REV-POL-011 | How are revoked or superseded reviews propagated to cached decisions, release candidates, corrections, withdrawals, and public carriers? | **UNKNOWN** |
| REV-POL-012 | What rollback drill proves restoration of prior policy plus invalidation of stale review decisions? | **UNKNOWN** |

## Evidence review and no-loss ledger

**Last reviewed:** 2026-08-13 against
`main@09a01ef8a71a557efc1c35bda6f9b762a429a1f3`.

| Baseline element | Disposition in v0.1 |
|---|---|
| Path and H1 | **KEEP** — preserved in place. |
| “Greenfield bundle stub” | **CLARIFY** — replaced with the verified local boundary, exact maturity, and non-effects. |
| `two_steward_required.rego` | **SURFACE CONFLICT** — retained unchanged; no-op default and absent operative rule made prominent. |
| `release/` child | **CLARIFY** — retained unchanged; placeholder status and parallel-authority risk documented. |
| Parent policy authority | **ENRICH** — inherited authority, outcome, runtime, release, and public-path limits made explicit. |
| Reviewer-role and authority-binding profiles | **ENRICH** — linked as separate inactive fixture evidence without claiming activation. |
| Directory Rules profile | **ENRICH** — `BOUNDARY_COMPACT` fields, direct-child map, and review triggers supplied. |
| Validation, contribution, correction, and rollback | **ADD** — bounded commands, non-effects, change discipline, and recovery path recorded. |
| Unknowns | **SURFACE** — accepted inputs, evaluator, consumer, reviewer capacity, enforcement, and child-lane ownership remain open. |

This update makes no claim that review policy is active, that two stewards are
required, that any reviewer is qualified or independent, or that any release is
approved or public.

[Back to top](#top)
