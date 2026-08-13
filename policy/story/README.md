<a id="top"></a>

# policy :: story

> **One-line purpose.** `policy/story/` is the local policy-source boundary for
> deciding whether an evidence-dependent story operation may proceed, must
> abstain or be restricted, or must be denied. It inherits authority from
> [`policy/`](../README.md); it does not create story truth, resolve evidence,
> validate citations, implement a policy engine, approve release, or publish.

> [!IMPORTANT]
> **Safe current conclusion:** at
> `main@8fdcfeeb6013dc4432b8892e62e173703f6cd2f4`, this directory contains this
> README stub and one `PROPOSED` Rego stub. The module declares
> `default deny := false`; its only denial example is commented out. No
> story-native Rego test, accepted input or output contract, bundle selection,
> evaluator binding, decision receipt, or governed consumer was established by
> the reviewed evidence.

> [!CAUTION]
> The module does **not** currently enforce evidence continuity. A filename,
> package name, commented rule, passing workflow, StoryNode fixture, or rendered
> story is not a policy decision and must not be treated as evidence, review,
> release, or publication authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Rule inventory](#current-rule-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Trust boundary](#story-policy-trust-boundary) · [Evaluation](#rule-source-runtime-evaluation-and-release) · [Related evidence](#related-contracts-schemas-fixtures-tests-and-workflows) · [Validation](#validation-coverage-and-limits) · [Correction](#correction-and-rollback) · [Review](#review-triggers) · [Open verification](#open-verification-register)

## Purpose

`policy/story/` owns the narrow admissibility question for story and narrative
operations:

> Given a bounded story operation and authoritative references to its evidence,
> citations, rights, sensitivity, review, release, freshness, and correction
> posture, may the operation proceed, proceed only with obligations, abstain, or
> be denied?

This boundary may eventually supply story-specific rules to an accepted policy
bundle. It must consume facts from their owning objects and interfaces rather
than infer them from prose, pixels, map state, model output, file presence, or
repository state.

This README documents the tracked source and its limits. It does not activate
the Rego module or turn the candidate posture described below into current
behavior.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical source root for allow, deny, hold, restrict, and abstain rules. |
| README profile | `BOUNDARY_COMPACT`: this object-family lane changes evidence and presentation trust assumptions while inheriting the parent root contract. |
| Placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Section 9.3 places admissibility rules under `policy/`; section 16 defines this README profile. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry projects adopted law; it does not create authority. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, independence, review, or approval. |
| Local owner | **NEEDS VERIFICATION.** No accepted Story policy steward or independent approver was established in the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** The tracked package `kfm.evidence_continuity_required` is a current machine identifier, but no accepted local scope identifier or query contract was established. |
| Release authority | None. Story policy may eventually supply an admissibility result; [`release/`](../../release/README.md) owns release, correction, withdrawal, and rollback decisions. |
| Publication authority | None. A policy source file, evaluation result, commit, workflow, or merge cannot publish a story. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Target README | 43-byte greenfield stub, blob `64cb3860dd2b0a2d64152868ab2437148c899da2` | The local boundary contract was absent before this documentation-only update. |
| Direct-child inventory | `README.md` plus one Rego file | Presence establishes neither adoption nor completeness. |
| Rego module | [`evidence_continuity_required.rego`](./evidence_continuity_required.rego), blob `9f3791db0da8a91ef3d10c7152fc738eb53139c3` | The source is marked `PROPOSED greenfield stub. No real rules yet.` |
| Package | `kfm.evidence_continuity_required` | This is the tracked package name, not proof of an accepted bundle namespace, entrypoint, or consumer. |
| Executable rule | `default deny := false` | The module does not deny an input. |
| Commented sketch | Mentions `input.kind`, `input.evidence_bundle_resolved`, and `evidence_bundle_unresolved` | Comments are not an input contract, reason-code registry, rule, test, or decision. |
| Story-native Rego tests | None under `policy/story/` | No local allow, abstain, deny, error, malformed-input, or fail-closed behavior is demonstrated. |
| Broad policy readiness workflow | [`policy-test`](../../.github/workflows/policy-test.yml) runs for pull requests and explicitly does not evaluate Rego or emit `PolicyDecision` objects | A pass preserves the repository's broader readiness boundary; it does not validate this module's semantics. |
| StoryNode and StoryManifest profiles | Closed, synthetic, fixture-first UI projection profiles and workflows exist | They validate bounded projection inheritance; their workflow summaries explicitly deny policy-execution and release/publication effects. |
| Evaluator, bundle, decision, and consumer | **UNKNOWN / NEEDS VERIFICATION** | No complete story-policy evaluation path was proved from the inspected surfaces. |
| Release and publication | Separate governed responsibilities | Nothing in this directory releases, deploys, or publishes a story. |

All current-state claims above are pinned to
`main@8fdcfeeb6013dc4432b8892e62e173703f6cd2f4`. Later changes require a fresh
inventory and claim review.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned repository tree, tracked bytes, workflow, or accepted decision. |
| **PROPOSED** | Candidate behavior or design pressure that is not current accepted behavior. |
| **NEEDS VERIFICATION** | A specific check or decision remains before the claim can be relied upon. |
| **UNKNOWN** | The inspected evidence is insufficient to support a stronger claim. |

[Back to top](#top)

## Current direct-child map

This map was verified from the complete tracked tree at the evidence base. It
shows this directory and direct children only.

```text
policy/story/
├── README.md
└── evidence_continuity_required.rego
```

Neither child is marked as generated, mirrored, localized, or converted in its
tracked bytes. A future bundle, generator, or mirror relationship must identify
its writable canonical source and deterministic reproduction path before this
README treats that relationship as established.

[Back to top](#top)

## Current rule inventory

| Module | Package | Executable state | Current effect |
|---|---|---|---|
| [`evidence_continuity_required.rego`](./evidence_continuity_required.rego) | `kfm.evidence_continuity_required` | Boolean `deny` defaults to `false`; no operative rule follows | It denies nothing and emits no reason, obligation, receipt, or decision instance. |

The commented example sketches a possible denial condition and reason. It does
not establish field meaning, input validation, rule shape, outcome semantics,
or compatibility. A future implementation must choose and version those
elements explicitly, then bind them to native tests and an accepted evaluator.

[Back to top](#top)

## What belongs here

Subject to accepted contracts, schemas, bundle conventions, and review, this
boundary may contain:

- story-specific declarative policy source for evidence-continuity and
  narrative-display admissibility;
- operation-specific rules that consume authoritative evidence, citation,
  rights, sensitivity, review, release, freshness, and correction posture;
- fail-closed handling for missing, invalid, stale, conflicted, restricted,
  withdrawn, or superseded support;
- stable package, entrypoint, version, reason-code, obligation, and
  supersession documentation for the local rule family;
- policy-local composition guidance that references sibling rights,
  sensitivity, release, and correction rules without duplicating their
  authority; and
- bundle-local metadata only when the parent policy root and an accepted bundle
  profile designate this lane as the canonical source.

A rule belongs here because its primary responsibility is **story
admissibility**. Mentioning a story, narrative, map, citation, or evidence item
does not by itself make a file Story policy.

[Back to top](#top)

## What is prohibited

| Prohibited material | Owning surface or required action |
|---|---|
| Story, StoryNode, StoryManifest, or claim semantic meaning | [`contracts/story/`](../../contracts/story/README.md) or the accepted object-family contract |
| JSON Schema, DTO, generated type, or field-shape authority | [`schemas/`](../../schemas/README.md) |
| EvidenceBundle, EvidenceRef, citation payload, source record, or claim truth | Evidence and source authority roots; policy consumes their governed status |
| Story instances, narrative bodies, prompts, model output, screenshots, tiles, maps, or scene assets | Their governed lifecycle, runtime, application, or released-artifact homes |
| Raw, candidate, quarantined, processed, cataloged, or published data | Governed [`data/`](../../data/README.md) lifecycle lanes |
| `PolicyDecision`, review, receipt, proof, correction, withdrawal, rollback, or release instances | Their owning process, accountability, or [`release/`](../../release/README.md) families |
| Reusable evaluator, resolver, API, adapter, UI component, or deployment code | [`packages/`](../../packages/README.md), governed applications, runtime, or infrastructure |
| Reusable fixtures, validators, and conformance tests | [`fixtures/`](../../fixtures/README.md), [`tools/`](../../tools/README.md), and [`tests/`](../../tests/README.md), except an explicitly accepted engine-native co-location profile |
| Credentials, secrets, private URLs, production payloads, restricted text, or harmful-precision locations | Do not commit; use the applicable secret, quarantine, redaction, generalization, or denial path |

Do not copy protected material into a policy input example to demonstrate that
it should be denied. Synthetic, minimal, public-safe fixtures belong in their
accepted fixture family.

[Back to top](#top)

## Inputs and outputs

### Current inputs

No accepted input contract is bound to the module. The commented sketch names
`input.kind` and `input.evidence_bundle_resolved`, but those names are
illustrative text only. The module does not validate required context, reject
unknown fields, authenticate references, or resolve evidence.

### Required future input posture

Before operational use, an accepted input profile must be:

- bounded to a named story operation and audience;
- defined semantically by a contract and structurally by a canonical schema;
- explicit about the authoritative references and status needed for the
  operation, including evidence and citation support where consequential;
- explicit about rights, sensitivity, review, release, freshness, correction,
  and policy version when those dimensions are material;
- composed from public-safe identifiers and classifications rather than copied
  source payloads or narrative bodies;
- deterministic and version-bound enough to replay and audit; and
- rejected, held, or abstained when required context is absent, malformed,
  stale, conflicted, or untrusted.

These are graduation requirements, not claims that the input exists today.

### Current outputs

The module emits no `PolicyDecision`, reason set, obligation, receipt, proof,
or release signal. Its only executable policy value is `deny = false`.

### Required future output posture

An operational story-policy result must use an accepted finite native outcome
and public-safe reason/obligation vocabulary. Runtime adapters may normalize
that result only through an accepted binding. They must not coerce missing,
invalid, abstained, denied, or evaluator-error states into permission.

The exact native outcome type, query, reason codes, obligations, decision
schema, and normalization mapping are **NEEDS VERIFICATION**.

[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Current boundary |
|---|---|
| Repository visibility | The repository and tracked source are public. Do not place secrets, protected story content, private identifiers, or harmful precision here. |
| Operational exposure | The root registry classifies `policy/` as internal policy-rule authority. This lane exposes no accepted public API or client-loadable bundle. |
| Permitted mutation | Versioned source changes through review. A rule change must preserve package/query compatibility or carry explicit versioning, migration, and rollback. |
| Runtime writes | None. Evaluations, logs, telemetry, decisions, receipts, and reports must not be written into this source directory. |
| Retention | Durable source history under the parent root's registry profile. Decision and correction retention belong to their own object families. |
| Sensitive inputs | Never retained here. Use synthetic fixture references and public-safe classifications; keep restricted payloads in their governed systems. |
| Generated output | None established. Generated status, bundle, or decision artifacts must identify their canonical inputs, producer, integrity, retention, and non-authority limits. |

[Back to top](#top)

## Story-policy trust boundary

Story policy is downstream of factual and procedural authority. It may decide
whether a supplied operation is admissible; it must not manufacture the facts
that make it admissible.

| Concern | Permitted Story-policy role | Authority it must not assume |
|---|---|---|
| Evidence continuity | Require an authoritative resolution posture for consequential support | Resolve an `EvidenceRef`, create an `EvidenceBundle`, or declare a narrative true |
| Citation | Consume an authenticated citation-validation posture | Validate citation content or infer support from a link |
| Rights and consent | Consume current rights/consent posture and apply accepted obligations | Clear rights, infer consent, or override revocation |
| Sensitivity and precision | Apply accepted display, generalization, redaction, or denial rules | Downgrade sensitivity or leak the protected fact through a reason |
| Review | Require the accepted review state for the operation | Authenticate a reviewer or approve its own source change |
| Release | Require a governed release posture when public display is requested | Create, promote, approve, or publish a release |
| Freshness | Apply an accepted stale/unknown posture | Invent observation time or update source evidence |
| Correction and supersession | Require current correction/withdrawal references | Create a correction notice, replacement, rollback card, or lineage fact |
| Rendering | Return public-safe outcomes and obligations to a governed consumer | Hide restricted content with CSS, map styling, client state, or narrative omission alone |

### Fail-closed continuity posture

The adjacent proposed story contracts require missing, stale, restricted,
unreviewed, unreleased, denied, withdrawn, and superseded states to remain
visible and less permissive than a ready answer. A future Story-policy profile
must preserve those distinctions instead of collapsing them into a boolean
success or a generic error.

The exact policy-native vocabulary is not yet accepted. Until it is, callers
must not translate this stub's `deny = false` into `ALLOW` or `ANSWER`.

[Back to top](#top)

## Rule source, runtime evaluation, and release

The intended separation is:

```text
authoritative governed references and status
  -> accepted, schema-valid story-policy input
  -> accepted versioned bundle and evaluator
  -> authenticated finite policy result
  -> governed API or runtime normalization
  -> public-safe StoryNode / StoryManifest consumer
  -> separate review and release decision
```

Each arrow requires its own contract, validation, identity, and failure
semantics. This repository currently demonstrates bounded StoryNode and
StoryManifest projection validation, but the reviewed workflows explicitly say
that they do not execute policy, resolve references, approve review or release,
or publish.

Before this lane may be described as operational, the dependency-closed packet
must establish at least:

1. accepted story operations and input semantics;
2. a closed input schema with positive and negative synthetic fixtures;
3. versioned package, query, native outcome, reason, and obligation contracts;
4. fail-closed Rego rules with parser/format checks and native tests;
5. an accepted bundle selector, integrity binding, and evaluator version;
6. deterministic malformed-input, missing-context, abstain, deny, and evaluator-error behavior;
7. an authenticated decision object and replay/correction posture;
8. a governed consumer that cannot bypass, broaden, or silently coerce the result;
9. release integration that preserves separate review and release authority; and
10. changed-area CI whose trigger and required-check posture are verified.

Until those gates are closed, status remains proposed and inactive.

[Back to top](#top)

## Related contracts, schemas, fixtures, tests, and workflows

| Surface | Confirmed role | Authority limit |
|---|---|---|
| [`contracts/story/README.md`](../../contracts/story/README.md) | Proposed semantic lane for story and narrative objects | It does not accept this Rego package, choose a schema, or create policy behavior. |
| [`contracts/ui/story_node.md`](../../contracts/ui/story_node.md) | Proposed public-safe StoryNode projection with fixture-first trust inheritance | A valid projection does not prove referenced evidence, policy, review, release, or correction objects. |
| [`story_node.schema.json`](../../schemas/contracts/v1/ui/story_node.schema.json) | Closed machine profile paired with the UI contract | Shape validation is not policy evaluation. |
| [`fixtures/ui/story_node/`](../../fixtures/ui/story_node/README.md), [validator](../../tools/validators/ui/validate_story_node.py), [tests](../../tests/validators/test_validate_story_node.py), and [workflow](../../.github/workflows/story-node-trust-inheritance.yml) | Synthetic StoryNode conformance and finite trust-inheritance checks | The workflow states that it grants no policy approval, release, deployment, publication, or public-use permission. |
| [`contracts/ui/story_manifest.md`](../../contracts/ui/story_manifest.md) | Proposed composite StoryManifest trust-reduction contract | Its ordering is a validation profile, not repository-wide policy. |
| [`story_manifest.schema.json`](../../schemas/contracts/v1/ui/story_manifest.schema.json), [fixtures](../../fixtures/ui/story_manifest/cases.json), [validator](../../tools/validators/ui/validate_story_manifest.py), [tests](../../tests/validators/test_validate_story_manifest.py), and [workflow](../../.github/workflows/story-manifest-trust-inheritance.yml) | Synthetic composite-inheritance validation | It performs no reference resolution, narrative-truth determination, policy execution, review/release approval, or publication. |
| [`docs/architecture/story/README.md`](../../docs/architecture/story/README.md) and [`CONTINUITY.md`](../../docs/architecture/story/CONTINUITY.md) | Draft architecture and lineage pressure for story continuity | Their own text marks concrete paths and runtime claims proposed until repository verification; use current implementation evidence for current behavior. |
| [`apps/explorer-web` Story Player README](../../apps/explorer-web/src/features/story_player/README.md) | Application-boundary documentation for a Story Player feature | UI documentation and rendering do not activate policy or create truth. |
| [`packages/policy-runtime/README.md`](../../packages/policy-runtime/README.md) | Parent policy evidence describes the package as a placeholder | It does not establish a Story evaluator or consumer. |
| [`policy-test`](../../.github/workflows/policy-test.yml) | Broad policy-readiness drift guard | It explicitly does not evaluate Rego, bind an evaluator, emit decisions, approve release, or publish. |
| [`release/README.md`](../../release/README.md) | Release, correction, withdrawal, and rollback responsibility | A policy result is an input to a separate decision, not the decision itself. |

These surfaces are adjacent evidence, not a single accepted implementation.
Their vocabularies must not be merged or normalized by README prose.

[Back to top](#top)

## Validation coverage and limits

### Current coverage

| Check | Current coverage | What it does not prove |
|---|---|---|
| Complete direct-child inventory | README plus one Rego stub verified at the pinned base | Activation, completeness, consumer binding, or public fitness |
| Source inspection | Status comment, package, executable default, and commented example verified | Rego compilation under an accepted version, semantic correctness, or fail-closed behavior |
| Native Story-policy tests | None found in this lane | Any input or outcome case |
| `policy-test` workflow | Broad inventory and readiness assertions on pull requests | Story rule evaluation or decision authenticity |
| StoryNode / StoryManifest suites | Closed synthetic projection validation | Story-policy execution, ref resolution, evidence truth, or release |
| Repository settings | Main is reported protected by GitHub | Effective required checks, approval rules, bypass actors, and exact enforcement remain **NEEDS VERIFICATION** unless platform evidence is inspected separately. |

### Documentation validation for this README

This documentation-only change should pass:

- one H1 and logical heading order;
- exact direct-child map parity with the pinned tree;
- local links and fragments that resolve at the branch head;
- exact package/default/status claims against the Rego blob;
- no trailing whitespace, malformed fences, or missing final newline;
- one changed path with no generated or executable companion change; and
- remote blob, diff, base/head, and draft-pull-request read-back.

Passing those checks proves documentation structure and evidence alignment only.
It does not make the Rego stub protective.

### Validation required for a future rule change

A semantic Rego change requires a separate dependency-closed review that adds
or updates the accepted contract, schema, fixtures, native tests, evaluator and
bundle binding, normalization tests, consumer integration, documentation, and
rollback evidence. Include representative allowed, abstained or held, denied,
malformed, missing-context, stale, restricted, corrected, withdrawn, and
evaluator-error cases as applicable.

[Back to top](#top)

## Correction and rollback

This README is documentation only. It does not mutate a policy rule, schema,
contract, runtime, story instance, decision, receipt, release, deployment, or
public artifact.

- **Before merge:** close or abandon the draft pull request. The target on
  `main` remains blob `64cb3860dd2b0a2d64152868ab2437148c899da2`.
- **After merge:** revert the documentation commit or apply a transparent
  forward-fix that preserves the corrected evidence and history.
- **Rule correction:** do not edit this README to conceal a faulty policy
  result. Correct or supersede the accepted rule/bundle through its versioned
  source and tests, then propagate any required decision or release correction
  through the owning object families.
- **Public reliance:** a Git revert alone may not correct a released story.
  Preserve the applicable correction, withdrawal, cache invalidation,
  supersession, and rollback history.

[Back to top](#top)

## Review triggers

### Evidence snapshot

| Evidence | Reviewed identity |
|---|---|
| Repository base | `main@8fdcfeeb6013dc4432b8892e62e173703f6cd2f4` |
| Prior target blob | `64cb3860dd2b0a2d64152868ab2437148c899da2` |
| Rego blob | `9f3791db0da8a91ef3d10c7152fc738eb53139c3` |
| Parent policy README blob | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` |
| Directory Rules blob | `fd49a0b83e55cef52c1124281f093e263526898d` |
| ADR-0029 blob | `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` |
| Root-registry blob | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` |
| CODEOWNERS blob | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Open-PR overlap | No open pull request changed `policy/story/README.md` immediately before authoring |
| Review date | 2026-08-12 |

Re-review this boundary when any of the following changes:

- a direct child, package, query, rule shape, bundle, or generated relationship;
- the accepted Story-policy input, output, reason, obligation, or scope contract;
- evidence, citation, rights, sensitivity, review, release, freshness, or
  correction dependencies;
- evaluator, consumer, API, runtime normalization, or public exposure;
- story contracts, schemas, fixtures, tests, or workflows that this lane is
  required to compose with;
- CODEOWNERS, stewardship, required-check, or separation-of-duties posture;
- an accepted ADR, migration, correction, withdrawal, rollback, or security
  finding that affects the boundary; or
- drift between this README, the tracked tree, and executable source.

[Back to top](#top)

## Open verification register

| ID | Open item | State | Evidence needed to close |
|---|---|---|---|
| `STORY-POL-001` | Local Story-policy scope and accepted operation set | **NEEDS VERIFICATION** | Accepted semantic contract and scope identifier |
| `STORY-POL-002` | Story policy steward and independent approval route | **NEEDS VERIFICATION** | Accepted stewardship and review record |
| `STORY-POL-003` | Closed input schema and authoritative reference assembly | **UNKNOWN** | Canonical schema, synthetic fixtures, and producer/validator binding |
| `STORY-POL-004` | Package/query shape, native outcomes, reasons, obligations, and versioning | **NEEDS VERIFICATION** | Accepted policy contract and compatibility tests |
| `STORY-POL-005` | Fail-closed rules and native Rego coverage | **CONFIRMED absent at the evidence base** | Operative source plus positive, negative, malformed, missing-context, and error tests |
| `STORY-POL-006` | Composition with evidence, citation, rights, sensitivity, review, release, freshness, and correction authority | **UNKNOWN** | Explicit decision table and integration fixtures without duplicated authority |
| `STORY-POL-007` | Bundle selector, integrity binding, evaluator version, and runtime normalization | **UNKNOWN** | Accepted bundle manifest, evaluator tests, and mapping contract |
| `STORY-POL-008` | Authenticated decision, receipt, replay, expiry, and correction posture | **UNKNOWN** | Bound decision schema and accountability artifacts |
| `STORY-POL-009` | Governed StoryNode/StoryManifest consumer and bypass resistance | **UNKNOWN** | Consumer integration tests and public-boundary review |
| `STORY-POL-010` | Required-check and independent-release enforcement | **NEEDS VERIFICATION** | Current platform controls and exact-head hosted-check evidence |

Until these items are closed, `policy/story/` remains a proposed source lane and
must not be represented as active enforcement.

[Back to top](#top)
