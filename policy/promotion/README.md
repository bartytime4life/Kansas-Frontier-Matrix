<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-promotion-readme
title: policy/promotion/ — Promotion Admissibility Policy Boundary
type: readme
version: v0.1
status: draft; BOUNDARY_COMPACT; repository-grounded; proposed-inactive; no-op-rule-stubs; non-runtime; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ changes to @bartytime4life; no accepted promotion-policy steward or independent release authority was established
created: 2026-08-11
updated: 2026-08-13
policy_label: public; policy; promotion; lifecycle; review-required; rollback-aware; proposed-inactive; non-release; non-publication
owning_root: policy/
responsibility: Define the local policy-source boundary for promotion prerequisites and rollback-card admissibility without storing promotion decisions, executing lifecycle transitions, authenticating support, approving release, or publishing data.
truth_posture: CONFIRMED accepted placement under policy/, exact three-file local tree, two no-op proposed Rego stubs, separate bounded fixture-first promotion readiness and receipt validation, and no local evaluator or transition authority / PROPOSED BOUNDARY_COMPACT contract and future fail-closed promotion-policy authoring posture / CONFLICTED or unresolved A-G gate names and responsibilities across proposed ADR, draft runbook, architecture guidance, and validator profile / NEEDS VERIFICATION accepted local scope ID, steward assignments, policy input and outcome contracts, bundle and evaluator binding, native Rego tests, governed consumer, authoritative gate sequence, independent reviewer capacity, required-check enforcement, decision and receipt emission, rollback execution, and publication integration
related:
  - ../README.md
  - ../release/README.md
  - ../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/policy_gate_register.yaml
  - ../../contracts/release/promotion_decision.md
  - ../../contracts/release/promotion_receipt.md
  - ../../contracts/release/rollback_card.md
  - ../../tools/validators/promotion_gate/README.md
  - ../../release/promotion_decisions/README.md
  - ../../.github/workflows/promotion-gate.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: promotion

`policy/promotion/` is KFM's local policy-source boundary for determining
whether a named lifecycle-promotion operation satisfies its admissibility
prerequisites, must be held, should abstain, or must be denied. It inherits the
authority and limitations of [`policy/`](../README.md).

> [!IMPORTANT]
> **Safe current conclusion:** this lane is proposed and inactive. Both local
> Rego modules are explicit greenfield stubs. They define `default deny :=
> false`, contain no operative denial body, and are not executed by the
> repository's promotion-gate workflow. The separate A–G readiness validator
> is implemented and fixture-tested, but its `PASS` means only
> `APPROVE_READY` for accountable review—not promoted, released, or published.

> [!CAUTION]
> **Promotion is not a file move, workflow pass, merge, deployment, or
> filename.** A copied artifact does not earn a lifecycle state. A schema-valid
> `APPROVE`, a readiness `PASS`, or a Rego package name cannot substitute for
> evidence closure, accepted policy evaluation, accountable review, a governed
> `PromotionDecision`, release records, rollback readiness, or authorized
> publication.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Map](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs](#candidate-evaluation-inputs) · [Outputs](#source-and-evaluated-outputs) · [Boundaries](#decision-receipt-and-object-family-boundaries) · [Sequences](#gate-sequence-and-vocabulary-boundary) · [Runtime](#rule-source-readiness-validation-and-runtime) · [Validation](#validation-coverage-and-limits) · [Contributing](#contributor-contract) · [Correction](#correction-supersession-and-rollback) · [Verification](#open-verification-register)

## Purpose

This boundary may hold reviewed, versioned policy source that evaluates the
admissibility of a bounded promotion request. A mature rule family could check
whether the candidate, requested transition, evidence, policy context, rights,
sensitivity, validation, review, receipt, manifest, correction, and rollback
support are sufficient for further release processing.

The boundary answers a policy question:

> Given an explicit candidate, current and requested lifecycle states,
> evidence and validation support, rights and sensitivity posture, review
> context, rollback target, policy identity, and evaluation time, may this
> promotion operation proceed—and which denial, hold, abstention, restriction,
> or escalation obligations remain?

It does **not** answer whether evidence is true, whether a reference is
authentic, whether a reviewer is authorized, whether a transition occurred,
whether a release is approved, or whether an artifact may be served publicly.

This README documents current repository evidence. It does not activate either
stub, accept a gate sequence, upgrade a proposed contract or schema, bind a
policy bundle, create a decision or receipt, or authorize lifecycle mutation.

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical responsibility root for normative allow, deny, hold, restrict, and abstain rule source. |
| Directory profile | `BOUNDARY_COMPACT`: this lane changes lifecycle, evidence, review, rollback, release, and public-trust assumptions. |
| Governing placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy from contracts and schemas and define the local README contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry projects adopted governance; it does not create it. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing is not proof of qualification, independence, policy acceptance, or release approval. |
| Local owner | **NEEDS VERIFICATION.** No accepted promotion-policy steward or independently authorized release approver was established in the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted machine scope identifier for `policy/promotion/` was found. This README does not invent one. |
| Policy-gate register | [`policy_gate_register.yaml`](../../control_plane/policy_gate_register.yaml) is `PROPOSED` and has an empty `entries` list. It establishes no active gate, bundle, evaluator, required check, or consumer. |
| Release authority | None. A promotion-policy result may become one input to a governed release-family decision; it cannot approve or apply the transition itself. |
| Publication authority | None. Public carriers require separate evidence, policy, review, release, correction, rollback, and delivery closure. |

## Current status

All observations in this section are pinned to
`main@87ef04d532df34bee8dc62ef8b28dfac69f35a0e`.

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| Target README | 47-byte greenfield stub, blob `b082c06e5f0889739e56a07216e89164e46e4076` | The local authority and non-ownership contract was previously absent. |
| Local tree | Tree `b008629776b8e39a55387a25fc3ab68a10bf1508` with this README and two Rego files | Path presence is confirmed; implementation is not. |
| `promotion_prerequisites.rego` | Explicit `PROPOSED` stub; package `kfm.promotion_prerequisites`; `default deny := false`; example body commented out | The module currently denies nothing and evaluates no promotion prerequisite. |
| `rollback_card_required.rego` | Explicit `PROPOSED` stub; package `kfm.rollback_card_required`; `default deny := false`; example body commented out | The module currently denies nothing and does not require a rollback card. |
| Local native tests | No `_test.rego` or dedicated Rego test is present in this lane | Parse compatibility, input shape, rule polarity, reason codes, and fail-closed behavior are not established. |
| Bundle and evaluator | No accepted local bundle manifest, selector, evaluator contract, entrypoint binding, or decision normalization was established | Repository source presence is not operational policy enforcement. |
| Bounded A–G validator | Implemented separately under [`tools/validators/promotion_gate/`](../../tools/validators/promotion_gate/README.md) with synthetic fixtures and tests | It validates declared readiness context without executing these Rego stubs, dereferencing support, mutating state, or granting authority. |
| `PromotionDecision` | Separate draft/`PROPOSED` semantic contract, closed release schema, synthetic shape fixtures, validator, and tests | Machine-valid `APPROVE`, `DENY`, or `ABSTAIN` is not an authenticated decision or transition. |
| `PromotionReceipt` | Separate `PROPOSED`, fixture-first contract, schema, validator, tests, and read-only workflow | It checks declared attempt consistency and digest binding; it does not prove that a transition occurred. |
| Verification adapter | Fixture-first, no-network adapter uses fake Cosign and Conftest tools and local synthetic references | It proves bounded adapter behavior only, not production cryptography, policy evaluation, support authenticity, or release readiness. |
| Gate sequence | Proposed ADR-0018, draft runbook, publication guidance, and bounded validator use materially different A–G names or responsibilities | The authoritative sequence and mapping remain unresolved; no one surface may silently overwrite the others. |
| Independent review and release | CODEOWNERS names one account; accountable reviewer identity, current authority, separation, and release authorization remain unverified | No local file or green check may be treated as independent approval. |

## Current direct-child map

The map is verified from the complete direct-child tree at the pinned baseline.
It shows this directory and direct children only, as required by Directory Rules
`DIR-README-003` through `DIR-README-005`.

```text
policy/promotion/
├── README.md                       # local boundary and contributor contract
├── promotion_prerequisites.rego    # proposed no-op prerequisite stub
└── rollback_card_required.rego     # proposed no-op rollback-support stub
```

Both rule filenames describe intended concerns, not implemented guarantees.
Their current `default deny := false` values and commented examples must not be
read as permission, fail-closed safety, or a transition contract.

## What belongs here

Subject to accepted semantic contracts, machine schemas, policy conventions,
and evaluator binding, this boundary may contain:

- declarative policy source whose primary responsibility is promotion
  admissibility;
- operation-specific prerequisites for candidate identity, lifecycle boundary,
  evidence closure, validation, rights, sensitivity, review, manifests,
  signatures, correction, and rollback context;
- fail-closed rules for missing, unresolved, stale, superseded, revoked,
  contradictory, unauthenticated, or out-of-scope support;
- public-safe reason codes and enforceable hold, abstention, restriction,
  re-review, correction, rollback, or escalation obligations;
- stable policy packages, entrypoints, versions, effective times, supersession
  links, native outcomes, and normalized-outcome mappings;
- narrowly paired engine-native policy tests only when an accepted repository
  convention establishes their placement and execution; and
- links to the accepted contracts, schemas, fixtures, tests, evaluator,
  consumer, decisions, receipts, manifests, correction path, and rollback
  target needed to understand a rule's actual effect.

A file belongs here because it decides whether a promotion-related operation is
**admissible**, not merely because it mentions a lifecycle state, validator,
workflow, release, or rollback.

## What is prohibited

| Prohibited material or claim | Owning surface or required action |
|---|---|
| Meaning of `PromotionDecision`, `PromotionReceipt`, `RollbackCard`, `ReleaseManifest`, review, or evidence objects | [`contracts/`](../../contracts/README.md) semantic authority |
| JSON Schema, DTO, enum, or machine field shape | [`schemas/`](../../schemas/README.md) machine-shape authority |
| Promotion decisions, reviews, candidates, manifests, corrections, withdrawals, rollback cards, or signatures | [`release/`](../../release/README.md), including [`release/promotion_decisions/`](../../release/promotion_decisions/README.md) and [`release/rollback_cards/`](../../release/rollback_cards/README.md) |
| Operational receipts, proofs, attestations, or EvidenceBundles | Governed `data/receipts/`, `data/proofs/`, and evidence-family lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | The applicable `data/` lifecycle or released-carrier lane |
| Evaluator, transition operator, pipeline, release service, API, UI, cache, storage, authentication, or deployment code | `packages/`, `pipelines/`, `tools/`, `runtime/`, `apps/`, or `infra/` according to responsibility |
| Reusable synthetic fixtures and executable conformance tests | Root [`fixtures/`](../../fixtures/README.md) and [`tests/`](../../tests/README.md), except an accepted engine-native co-location profile |
| Reviewer identity, credentials, private tickets, group membership, qualification, assignment, signing key, token, or secret | Governed identity/authority and external secret-management systems; never infer or store them here |
| Real restricted payloads, personal data, protected cultural information, genomic material, exact sensitive locations, or exploit-enabling infrastructure detail | Keep out of Git, policy reasons, tests, logs, documentation, and generated receipts; use synthetic or governed references |
| A `PASS`, `APPROVE`, filename, path move, workflow, PR approval, merge, deployment, or schema-valid object presented as promotion proof | Resolve the complete governed transition and its accountable records instead |
| Generated language or AI output presented as policy or release approval | Route through authorized human review and governed decisions; generation is never approval |

## Candidate evaluation inputs

An operational promotion-policy evaluation must receive explicit, normalized,
versioned context and must not silently fetch missing facts.

| Input family | Minimum governed context | Fail-closed trigger |
|---|---|---|
| Operation and lifecycle | Stable operation, candidate and run IDs, current state, requested state, target audience, effective time | Anonymous candidate, skipped state, ambiguous operation, or unsupported boundary |
| Candidate integrity | Exact specification, artifact, manifest, run, and input digests with canonicalization profile | Missing, zero, malformed, inconsistent, or mutable identity |
| Source and evidence | Source roles, EvidenceRefs, resolved EvidenceBundle support, provenance, freshness, citation closure | Unresolved, stale, contradictory, role-collapsed, or unsupported evidence |
| Validation | Schema and domain validation refs, deterministic tool/profile versions, negative-check status | Missing validation, non-replayable result, known failure, or incompatible profile |
| Rights and sensitivity | Rights, license/terms, consent, sovereignty, sensitivity, precision, audience, transform posture | Unknown, expired, revoked, downgraded, or unsupported public-use posture |
| Review and authority | Subject-bound review refs, actor and assignment refs, scope, disposition, effective window, obligations, separation state | Missing, stale, superseded, self-review, unbound subject, open obligation, or unverified authority |
| Release support | Candidate, manifest, decision, signature/attestation, correction, withdrawal, and changelog refs as applicable | Missing or contradictory release-family support |
| Rollback | Rollback-card ref, affected and prior target refs, correction path, invalidation/restoration scope, drill or verification state | No safe target, unresolved card, incomplete correction linkage, or unusable restoration posture |
| Policy execution | Exact source or bundle ID/version/digest, selector, evaluator version, entrypoint, input hash, evaluation time | Unaccepted bundle, selector, evaluator, entrypoint, or non-replayable context |

**Current limitation:** neither local Rego stub defines an accepted input
profile or reads operative input. The table is a future authoring requirement,
not a claim that current code consumes these fields.

## Source and evaluated outputs

Authoring in this directory produces versioned policy source and documentation.
Those artifacts are not evaluated decisions.

If an accepted evaluator later executes a promotion rule, the result should
preserve:

- one finite native outcome with explicit error and uncertainty handling;
- public-safe reason codes and enforceable obligations;
- exact rule, bundle, evaluator, entrypoint, input, and effective-time identity;
- subject and candidate binding;
- expiry, supersession, correction, and replay context; and
- references suitable for a separately governed decision and receipt.

An accepted normalization contract must keep these states distinct:

| State | Must not be collapsed into |
|---|---|
| Policy allow or prerequisite satisfaction | Evidence truth, reviewer authority, transition application, release approval, or publication |
| Hold or abstention | Approval, denial, or silent success |
| Denial | Evaluator error, missing context, or applied rollback |
| Evaluator error | Allow, ordinary denial, or an omitted record |
| Readiness `PASS` / `APPROVE_READY` | `PromotionDecision.APPROVE`, `transition.applied: true`, release, or publication |
| Schema-valid `APPROVE` fixture | Authenticated approval or an actual lifecycle change |

The current stubs emit no governed `PolicyDecision`, `PromotionDecision`,
`PromotionReceipt`, review, proof, manifest, release, or public artifact.

## Decision, receipt, and object-family boundaries

| Object or result | Meaning owner | Instance owner | Relationship to this lane |
|---|---|---|---|
| Promotion-policy source | [`policy/`](../README.md) and this lane | Versioned Git source | This lane may own admissibility rules after acceptance and testing. |
| Bounded A–G readiness result | [`tools/validators/promotion_gate/`](../../tools/validators/promotion_gate/README.md) profile | Ephemeral command/CI output unless separately governed | Checks declared closure; does not execute local Rego or authorize transition. |
| `PromotionDecision` | [`contracts/release/promotion_decision.md`](../../contracts/release/promotion_decision.md) | [`release/promotion_decisions/`](../../release/promotion_decisions/README.md) or another accepted release lane | May cite exact policy identity; must not be stored beside rule source. |
| `PromotionReceipt` | [`contracts/release/promotion_receipt.md`](../../contracts/release/promotion_receipt.md) | Accepted release/receipt lane | Records one declared attempt; does not replace the decision or prove application. |
| `RollbackCard` | [`contracts/release/rollback_card.md`](../../contracts/release/rollback_card.md) | [`release/rollback_cards/`](../../release/rollback_cards/README.md) | Supplies rollback target and posture; this lane may evaluate its sufficiency. |
| `ReleaseManifest` and release approval | Release contracts and [`release/`](../../release/README.md) | Append-only release decision plane | Downstream of policy; not created or approved here. |
| Evidence, receipts, and proofs | Their semantic and trust-artifact families | Governed `data/` lanes | Policy consumes resolvable refs and cannot create support. |
| Published carrier | Released-data and public-delivery contracts | `data/published/` or accepted carrier | Never served from policy source or inferred from a policy result. |

Directory Rules `DIR-AUTHROOT-003` requires decision instances to live with the
process or release object they record. Placing a JSON or YAML decision beside a
Rego rule would create an authority collision.

## Gate sequence and vocabulary boundary

Repository surfaces currently use several A–G descriptions. They are related
design and implementation evidence, but they are not interchangeable.

| Surface | Current posture | Vocabulary or responsibility boundary |
|---|---|---|
| [ADR-0018](../../docs/adr/ADR-0018-promotion-gate-sequence.md) | `proposed`; governance checkpoint `REVISE` | Candidate promotion-evaluation sequence and explicit unresolved mapping/authority ledger. |
| [Promotion runbook](../../docs/runbooks/PROMOTION_RUNBOOK.md) | `draft`; implementation paths marked proposed | Operating guidance across lifecycle transitions; it must not activate policy by prose. |
| [Publication promotion-gates guidance](../../docs/architecture/publication/promotion-gates.md) | `draft` | A–G source/provenance/sensitivity/validation/evidence/review/release overview. |
| [Bounded readiness validator](../../tools/validators/promotion_gate/README.md) | Implemented, synthetic, no-network, non-authoritative | A–G identity/closure, asset integrity, geometry, time, rights/sensitivity, proof/catalog, and review/rollback profile. |
| `PromotionDecision` | Draft/`PROPOSED` release-family contract and schema | `APPROVE`, `DENY`, `ABSTAIN`; distinct from validator and runtime/policy vocabularies. |
| `PromotionReceipt` | `PROPOSED`, fixture-first | Gate statuses `PASS`, `ABSTAIN`, `DENY`, `ERROR`; `PASS` maps only to `APPROVE_READY`. |

Until an accepted decision reconciles these surfaces, contributors must:

1. name the exact profile and version they are changing;
2. avoid saying “Gate A–G” without citing the specific sequence;
3. preserve each finite vocabulary and its error/uncertainty semantics;
4. avoid remapping gates or outcomes in a README-only or rule-only change; and
5. record incompatible claims as `CONFLICTED`, `HOLD`, or **NEEDS
   VERIFICATION** rather than selecting one by convenience.

## Exposure, mutation, retention, and sensitivity

| Dimension | Local contract |
|---|---|
| Exposure | Internal policy source and public-safe boundary documentation. Policy source is not a public API, client bundle, or released carrier. |
| Mutation | Versioned, reviewable Git changes. Once relied upon, preserve effective dates, digests, supersession, and prior behavior through history. |
| Retention | Durable policy lineage sufficient to reproduce decisions and support correction, expiry, withdrawal, and rollback analysis. |
| Generation | Generated suggestions may be proposed, but generated language and receipts grant no policy, review, release, or publication authority. |
| Physical storage | Repository source only. Secrets, sensitive payloads, private reviews, signing material, and operational decision instances do not belong here. |
| Sensitivity | Rule inputs should be stable governed references. Reasons, fixtures, logs, and docs must not echo restricted values or precise protected locations. |

Policy changes that broaden allowable states, audiences, precision, or exposure
carry greater review burden than denial-tightening changes, but every material
change still requires negative tests, consumer analysis, correction posture,
and a rollback plan.

## Rule source, readiness validation, and runtime

Three layers must remain distinct:

1. **Rule source** — the two files here are proposed no-op stubs.
2. **Readiness validation** — the separate bounded validator checks a declared
   synthetic promotion packet and returns deterministic readiness findings.
3. **Runtime or release action** — no accepted local evaluator, transition
   operator, or release authority is established by this directory.

The repository's [`promotion-gate` workflow](../../.github/workflows/promotion-gate.yml):

- has read-only `contents` permission;
- runs doctrine, schema-shape, bounded readiness, and fixture-only review
  checks;
- verifies that the two local Rego paths remain present;
- does **not** execute either local Rego module;
- deliberately preserves workflow holds around unresolved support, live review,
  and release authority; and
- emits no EvidenceBundle, decision, receipt, proof, manifest, rollback card,
  release, or public artifact.

The separate [promotion-verification workflow](../../.github/workflows/promotion-verification-execution.yml)
executes a fixture-first offline adapter with fake tools. That is useful adapter
evidence, not production signature verification or promotion authority.

No browser, map, public API, pipeline, or release operator should load these
stubs directly or infer permission from `default deny := false`.

## Related contracts, schemas, fixtures, tests, and workflows

| Family | Current evidence | Limit |
|---|---|---|
| `PromotionDecision` | [Contract](../../contracts/release/promotion_decision.md), [release schema](../../schemas/contracts/v1/release/promotion_decision.schema.json), [fixtures](../../fixtures/release/promotion_decision/README.md), validator, and focused schema test | Proposed shape and synthetic checks do not authenticate support or apply a transition. |
| Policy-side promotion schema | [`schemas/contracts/v1/policy/promotion_decision.schema.json`](../../schemas/contracts/v1/policy/promotion_decision.schema.json) is a permissive proposed scaffold with no contract document | It conflicts by name with the release-family decision and must not become parallel authority. |
| A–G readiness | [Validator contract](../../tools/validators/promotion_gate/README.md), [fixtures](../../fixtures/release/promotion_gate/README.md), [`test_promotion_gate.py`](../../tests/release/test_promotion_gate.py), and [`test_review_record.py`](../../tests/release/test_review_record.py) | Declared-context validation only; no dereference, Rego execution, state write, or authority. |
| `PromotionReceipt` | [Contract](../../contracts/release/promotion_receipt.md), [schema](../../schemas/contracts/v1/release/promotion_receipt.schema.json), [fixtures](../../fixtures/release/promotion_receipt/README.md), validator, tests, and [workflow](../../.github/workflows/promotion-receipt.yml) | Internal consistency and digest binding only; synthetic applied example is not a real transition. |
| Verification execution | [Contract](../../contracts/release/promotion_verification_execution.md), paired schemas, fixtures, adapter, tests, and [workflow](../../.github/workflows/promotion-verification-execution.yml) | Fixture tools and local references only; no production cryptography, live service, or authority. |
| Rollback support | [RollbackCard contract](../../contracts/release/rollback_card.md), [schema](../../schemas/contracts/v1/release/rollback_card.schema.json), fixtures, validator, tests, and [workflow](../../.github/workflows/rollback-card.yml) | Candidate shape and local consistency; no rollback execution or public mutation. |
| Release decisions | [`release/promotion_decisions/`](../../release/promotion_decisions/README.md) | Release-plane records; path presence or scaffold records do not prove authentic approval. |

## Validation coverage and limits

### Current local rule coverage

There is no native test for either local Rego stub. A future operative change
must add an accepted engine-native test profile and prove at least:

- explicit input contract and unknown-field behavior;
- default and rule polarity for complete, incomplete, and malformed context;
- missing evidence, review, authority, policy, decision, manifest, correction,
  and rollback support;
- stale, superseded, revoked, digest-mismatched, and out-of-scope references;
- self-review, expired authority, unresolved obligations, and separation cases;
- evaluator error distinct from deny, hold, and abstain;
- stable reason codes and obligation semantics;
- native-to-outward outcome mapping;
- bundle selection, digest pinning, replay, expiry, correction, and
  supersession; and
- proof that no denied or unresolved result can mutate lifecycle, release, or
  public state.

### Repository-native related checks

Current focused commands include:

```bash
# Bounded declared-context A–G readiness and review fixtures.
make publish-check

# PromotionDecision proposed schema fixtures.
python tools/validators/release/validate_promotion_decision.py --fixtures
python -m pytest -q tests/release/test_promotion_decision_schema.py

# PromotionReceipt proposed contract and fixture polarity.
python tools/validators/release/validate_promotion_receipt.py --fixtures
python -m unittest -q tests.release.test_promotion_receipt

# Fixture-first verification adapter; no production tools or public writes.
python -m pytest -q tests/release/test_promotion_verification_execution.py

# Candidate RollbackCard shape and consistency.
python tools/validators/release/validate_rollback_card.py --fixtures
python -m unittest -q tests.validators.test_validate_rollback_card
```

A pass proves only the bounded surface each command documents. It does not
prove local Rego behavior, evidence truth, rights or sensitivity clearance,
reviewer authentication, required-check configuration, a transition, release,
deployment, rollback execution, publication, or public use.

## Contributor contract

Before changing this README or adding or modifying promotion-policy source:

1. Pin current `main`, the target blob, the complete direct-child tree, and the
   exact policy, contract, schema, fixture, validator, test, workflow,
   decision, receipt, correction, and rollback evidence in scope.
2. Search open pull requests and recent commits for the same paths, package,
   decision family, gate profile, and outcome vocabulary.
3. State whether the change is documentation, a no-op scaffold, an inactive
   candidate, or an operative rule. Do not upgrade maturity by implication.
4. Name the exact operation, lifecycle boundary, subject, input contract,
   native outcome, normalized outcome, reason codes, obligations, policy
   bundle, evaluator, consumer, effective time, and supersession behavior.
5. Keep semantic meaning in `contracts/`, machine shape in `schemas/`, reusable
   fixtures in `fixtures/`, conformance in `tests/`, implementation in
   `tools/` or runtime roots, and decision instances under their owning
   release or data family.
6. Add complete positive, negative, uncertainty, malformed-input, stale,
   superseded, rights, sensitivity, review, rollback, and evaluator-error
   cases before making an operative claim.
7. Prove no-network and no-write behavior for validation paths. Treat any
   credential, repository write, lifecycle mutation, release, or publication
   capability as a separate security and governance change.
8. Review all consumers for fail-open defaults, outcome collapse, stale caches,
   fallback behavior, and direct public loading of policy source.
9. Record correction, expiry, supersession, replay, and rollback behavior for
   decisions already made under the prior rule.
10. Keep the pull request draft until qualified policy, evidence, validation,
    review, release, rollback, security/privacy, and affected-domain review is
    complete for the declared scope.

### Pull-request evidence

A reviewable change should state:

- pinned base and exact changed paths;
- current and proposed maturity;
- rule package, entrypoint, and behavior delta;
- contracts and schemas consumed, not redefined;
- fixtures, tests, commands, and exact results;
- bundle/evaluator/consumer effect or explicit non-effect;
- rights, sensitivity, review, release, and public-surface risk;
- correction, migration, supersession, and rollback plan; and
- unresolved ownership, authority, required-check, or operational questions.

## Review triggers

Re-review this boundary when:

- either Rego stub gains operative logic, changes default polarity, is renamed,
  or leaves the directory;
- a bundle, selector, evaluator, entrypoint, native test, normalized decision,
  receipt, replay path, or governed consumer binds to this lane;
- ADR-0018 is accepted, rejected, superseded, or its A–G mapping changes;
- the runbook, publication guidance, validator profile, or decision vocabulary
  is reconciled or diverges further;
- the policy-gate register gains an entry for promotion;
- a rule or workflow becomes a required check;
- reviewer roles, authority, separation of duties, or release stewardship
  changes;
- a promotion decision or receipt becomes authoritative or transition-capable;
- rights, sensitivity, evidence, correction, rollback, retention, exposure, or
  public-serving behavior changes; or
- drift, an incident, a correction, a withdrawal, a rollback, or a false
  promotion claim reveals a boundary defect.

## Correction, supersession, and rollback

### Documentation correction

Correct inaccurate README claims in place through reviewed Git history. Mark
unresolved facts as **NEEDS VERIFICATION**, `UNKNOWN`, `CONFLICTED`, or `HOLD`;
do not manufacture certainty to keep prose tidy.

### Policy correction and supersession

If an operative rule is later found unsafe or wrong:

1. halt affected evaluation or downstream consumption without treating the
   halt as a transition decision;
2. identify exact rule, bundle, evaluator, input, decision, receipt, candidate,
   release, and public consumers;
3. preserve prior source, digests, decisions, and receipts for audit;
4. publish a reviewed successor or explicit withdrawal—never silently rewrite
   relied-upon policy history;
5. re-evaluate affected candidates and decisions under an accepted profile;
6. issue correction, withdrawal, supersession, rollback, or invalidation
   records through their owning families; and
7. verify caches, catalogs, indexes, APIs, tiles, maps, exports, and AI outputs
   no longer expose invalid state where applicable.

### Repository rollback

Before merge, close the draft PR and remove only its scoped branch. After
merge, revert the bounded commit through a reviewed PR. Reverting this README
restores documentation only; it does not reverse a lifecycle transition. An
actual released-state rollback requires a governed `RollbackCard`, correction
and release records, accountable authorization, execution receipts, validation,
and downstream invalidation.

## Open verification register

| ID | Open item | Current posture | Closure evidence required |
|---|---|---|---|
| `PROMO-OPEN-01` | Accepted local owner, promotion-policy steward, and escalation route | **NEEDS VERIFICATION** | Accepted stewardship record with scope and effective period |
| `PROMO-OPEN-02` | Independent reviewer and release-authority capacity | `HOLD` | Authenticated actors, current assignments, separation policy, and observed enforcement |
| `PROMO-OPEN-03` | Authoritative A–G sequence and mapping | `CONFLICTED` | Accepted ADR or equivalent reconciliation across runbook, architecture, validator, and decision vocabularies |
| `PROMO-OPEN-04` | Local input contract, native outcome, reason, and obligation profile | `UNKNOWN` | Accepted contract/schema pair and negative cases |
| `PROMO-OPEN-05` | Bundle manifest, selector, digest, evaluator, and entrypoint binding | `UNKNOWN` | Accepted versioned bundle and deterministic evaluator proof |
| `PROMO-OPEN-06` | Native Rego tests and fail-closed default | `HOLD` | Engine-native positive, negative, malformed, uncertainty, and error tests |
| `PROMO-OPEN-07` | Native-to-outward outcome normalization | `UNKNOWN` | Accepted mapping that preserves error, denial, abstention, hold, readiness, and approval boundaries |
| `PROMO-OPEN-08` | Governed consumer and enforcement point | `UNKNOWN` | Consumer contract, no-bypass tests, receipts, replay, and correction behavior |
| `PROMO-OPEN-09` | Policy-gate register entry and required-check status | `UNKNOWN` | Accepted projection plus observed repository-rule evidence; workflow presence is insufficient |
| `PROMO-OPEN-10` | Authentic decision and receipt emission | `HOLD` | Accountable producer, resolved support, immutable identity, schema/semantic validation, and append-only storage |
| `PROMO-OPEN-11` | Rollback target verification and execution | `HOLD` | Resolved card, safe prior target, authorization, dry run, execution receipt, and invalidation proof |
| `PROMO-OPEN-12` | Live promotion, release, deployment, or publication integration | `UNKNOWN` | Explicitly authorized, observed, auditable transition evidence; never infer from fixtures or CI |

## Evidence review and no-loss ledger

| Field | Value |
|---|---|
| Evidence base | `main@87ef04d532df34bee8dc62ef8b28dfac69f35a0e` |
| Prior README blob | `b082c06e5f0889739e56a07216e89164e46e4076` |
| Prior directory tree | `b008629776b8e39a55387a25fc3ab68a10bf1508` |
| `promotion_prerequisites.rego` blob | `782b24af3c0fe28871a58da202a3efdbd5991647` |
| `rollback_card_required.rego` blob | `b2eb37b31b572e1d97d1afbe4babe8200f87df7d` |
| Evidence review date | 2026-08-13 |
| Change class | Same-path `BOUNDARY_COMPACT` documentation modernization; generated provenance receipt paired separately |
| Runtime effect | None |
| Policy behavior effect | None; both Rego stubs are unchanged |
| Lifecycle, release, or publication effect | None |
| Human review | Pending |

### Material baseline disposition

| Prior material | Disposition |
|---|---|
| H1 `policy :: promotion` | Preserved exactly. |
| “Greenfield bundle stub.” | Replaced with evidence-backed boundary, status, validation, contributor, correction, and rollback guidance. |
| Two Rego stubs | Preserved byte-for-byte; documented as proposed no-ops. |
| Proposed future behavior | Labeled as future authoring requirements, not current implementation. |
| Unknown authority or integration | Preserved as explicit verification items rather than inferred. |

This README is process guidance and evidence memory. Authorized human review
remains pending, and nothing here grants policy acceptance, reviewer authority,
lifecycle mutation, release, deployment, publication, or public-use authority.

[Back to top](#top)
