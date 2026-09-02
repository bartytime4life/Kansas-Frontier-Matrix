<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-opa-readme
title: policy/opa/ — OPA Placeholder and Convergence-Hold Boundary
type: readme
version: v0.1.0
status: draft; BOUNDARY_COMPACT; repository-grounded; placeholder-only; convergence-hold; no-evaluator; no-bundle; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ to @bartytime4life; accepted OPA-lane stewardship, independent policy approval, and a local scope ID were not established
created: 2026-08-13
updated: 2026-08-13
current_path: policy/opa/README.md
owning_root: policy/
policy_label: internal; policy; opa; placeholder; convergence-hold; fail-closed; non-runtime; non-release; non-publication
responsibility: Document the current OPA placeholder, preserve the general evaluator hold, and prevent this path from becoming parallel rule-source, bundle, evaluator, decision, release, or publication authority before an accepted convergence decision.
base_commit: ad31275429d715ad92002f8f2e160299193c9f50
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED README plus zero-byte .gitkeep only, no OPA payload or promotion child, existing Rego source lane, separate bundle-packaging lane, placeholder policy-runtime package, one bounded checksum-pinned OPA workflow outside this directory, general repository evaluator hold, and draft documents that mention an uncreated policy/opa/promotion path / PROPOSED BOUNDARY_COMPACT placeholder and no-parallel-writers contract / CONFLICTED unimplemented policy/opa naming versus established policy/rego, policy/bundles, policy/runtime, and packages/policy-runtime responsibilities / UNKNOWN accepted final purpose, owner, scope ID, migration or retirement decision, bundle format, selector, evaluator, production consumers, decision receipts, replay, correction propagation, and required-check coupling
related:
  - ../README.md
  - ../rego/README.md
  - ../bundles/README.md
  - ../runtime/README.md
  - ../../packages/policy-runtime/README.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/standards/RUN_RECEIPT.md
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/pass12-release-policy-v1.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: opa

> **One-line purpose.** `policy/opa/` is a tracked placeholder whose current
> responsibility is to expose an unresolved OPA-path decision and prevent
> parallel policy authority; it is not a rule-source lane, bundle, evaluator,
> runtime, decision store, release gate, or publication surface.

> [!IMPORTANT]
> **Safe current conclusion at `main@ad31275429d7`:** this directory contains
> exactly this README and a zero-byte `.gitkeep`. It contains no Rego module,
> OPA bundle, manifest, data document, configuration, binary, WebAssembly
> artifact, test, fixture, selector, adapter, decision, receipt, or promotion
> child. No operational writer or consumer is established.

> [!WARNING]
> Draft documents mention a proposed `policy/opa/promotion/` path, but that
> directory does not exist and those drafts explicitly mark the path proposed
> or in need of verification. Do not create it, copy promotion rules into it,
> or cite the references as placement authority.

> [!CAUTION]
> KFM has one bounded workflow that executes checksum-pinned OPA against the
> separate [`policy/rego/`](../rego/README.md) Pass 12 profile. That evidence is
> real but narrow. It does not activate this directory, establish a general OPA
> installation, approve a repository-wide bundle, or authorize a release.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Children](#current-direct-child-map) · [Convergence](#responsibility-and-convergence-boundary) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Lifecycle](#lifecycle-and-trust-boundary) · [Exposure](#exposure-mutation-and-retention) · [Validation](#validation) · [Contributing](#contributor-guidance) · [Correction](#correction-rollback-and-supersession) · [Related](#related-surfaces) · [Open work](#open-verification-register) · [Evidence](#evidence-and-no-loss-ledger)

## Purpose

This README gives the existing `policy/opa/` path an honest, narrow boundary.
The path is repository-present, but its operational purpose is unresolved. The
document therefore does two things:

1. records what the directory does and does not contain; and
2. holds new operational payloads until KFM selects one non-overlapping home
   for rule source, bundle packaging, evaluator integration, and activation.

The README does **not** reserve OPA as KFM's accepted general evaluator. It does
not make engine choice part of policy authority, and it does not convert a
placeholder into implemented status. OPA-specific design remains subordinate
to KFM's evidence, rights, consent, sensitivity, lifecycle, review, correction,
rollback, release, and public-trust invariants.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current boundary |
|---|---|
| Parent authority | [`policy/`](../README.md), KFM's singular root for reviewed admissibility rule source. |
| README profile | `BOUNDARY_COMPACT`; the path changes ownership and engine/bundle expectations even while empty. |
| Placement basis | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 2, 9.3, 14, and 16 prevent documentation or repository drift from creating parallel authority. |
| Current path disposition | **PLACE for this boundary README; HOLD for new operational payloads.** Same-path documentation may explain the current state, but the unresolved lane must not acquire a second writer. |
| Local owner | **NEEDS VERIFICATION.** CODEOWNERS routing is review routing, not accepted OPA stewardship or independent approval. |
| Local scope ID | **NOT ESTABLISHED.** No accepted bundle family, evaluator profile, or capability ID names this lane. |
| Exposure | Repository-public documentation and placeholder bytes; intended policy operating exposure is internal. |
| Mutation | Versioned Git review. Runtime, evaluator, API, worker, and public-client writes are prohibited. |
| Release/publication authority | None. Neither a source file nor an evaluator result approves release or publication. |

The root registry classifies `policy/` as the canonical home for normative
allow, deny, hold, restrict, and abstain rules and bundles. It does not assign
special authority to an `opa/` child or make a technology name a responsibility
root.

[Back to top](#top)

## Current status

| Surface | Confirmed evidence | Safe conclusion |
|---|---|---|
| Directory tree | `README.md` plus zero-byte `.gitkeep` only | **PLACEHOLDER_ONLY**; no functional policy content. |
| OPA/Rego source in this lane | None | No package, entrypoint, native result, reason, or obligation exists here. |
| `promotion/` child | Absent | Draft references are lineage, not an implementation or accepted destination. |
| General bundle payload | None here; [`policy/bundles/`](../bundles/README.md) is documentation plus an inactive Pass 12 packaging profile | No accepted bundle format, manifest instance, selector, signature, or activation. |
| Rego source lane | [`policy/rego/`](../rego/README.md) contains three Rego files, including one bounded native-test profile | This path must not duplicate or shadow those sources. |
| Runtime-facing policy source | [`policy/runtime/`](../runtime/README.md) contains proposed scaffolds and placeholders | Those files are not an evaluator and must not be copied here. |
| General evaluator package | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) is version `0.0.0` with an empty initializer and comment-only core | No functional OPA adapter, loader, selector, or consumer library is established. |
| Bounded OPA execution | [`pass12-release-policy-v1`](../../.github/workflows/pass12-release-policy-v1.yml) downloads checksum-pinned OPA 1.19.0 and executes one separate Rego profile | Bounded test evidence only; no general evaluator or this-lane activation. |
| Broad policy workflow | [`policy-test`](../../.github/workflows/policy-test.yml) performs static readiness checks and preserves the general OPA hold | It evaluates no repository-wide policy and emits no `PolicyDecision`. |
| Root policy command | `make policy` prints `TODO: opa test policy/ -v` | A zero exit is a readiness placeholder, not validation. |
| Operational writer or consumer | Not established in the bounded repository search | Treat as absent until exact code, configuration, deployment, and receipts prove otherwise. |
| Required-check and independent-review coupling | Not established by workflow names or CODEOWNERS | **UNKNOWN / NEEDS VERIFICATION.** |

### Current maturity

| Level | Evidence | This lane |
|---|---|---|
| M0 — tracked placeholder | Empty marker or stub | **CONFIRMED** |
| M1 — boundary documented | Responsibility and non-ownership contract | **PROPOSED by this README** |
| M2 — accepted engine-specific profile | Source/bundle identity, version, inputs, outputs, tests, owner | **NOT ESTABLISHED** |
| M3 — evaluator-backed proof | Pinned evaluator, bundle, native tests, fixtures, deterministic CI | **NOT ESTABLISHED here** |
| M4 — governed consumer and replay | Authenticated decision, receipt, enforcement, replay, expiry, correction | **NOT ESTABLISHED** |
| M5 — release-significant enforcement | Required checks, independent review, deployment and rollback evidence | **UNKNOWN / NOT ESTABLISHED** |

The bounded Pass 12 profile may have evidence at a later level for its exact
files and workflow. Maturity does not transfer between paths by technology
name.

[Back to top](#top)

## Current direct-child map

Verified from the tracked tree at the evidence base:

```text
policy/opa/
├── .gitkeep   # zero-byte placeholder marker; no runtime effect
└── README.md  # this boundary and convergence hold
```

There is no `promotion/`, `bundles/`, `data/`, `tests/`, `config/`, `.manifest`,
or compiled-output child. This tree describes current bytes only; it is not a
proposed future layout.

[Back to top](#top)

## Responsibility and convergence boundary

Current repository responsibilities already divide the policy substrate as
follows:

| Responsibility | Current owning surface | `policy/opa/` posture |
|---|---|---|
| Reviewed engine-native Rego source and the specifically governed co-located native test | [`policy/rego/`](../rego/README.md) | Do not duplicate, mirror, or shadow. |
| Operation- or domain-scoped policy source | Accepted child lanes beneath [`policy/`](../README.md) | Do not centralize merely because OPA may evaluate it. |
| Bundle composition, immutable packaging, manifest, selection, signing, and rollback contract | [`policy/bundles/`](../bundles/README.md) after acceptance | Do not create a second bundle home. |
| Runtime-facing admissibility rule source | [`policy/runtime/`](../runtime/README.md) | Do not turn source into evaluator implementation. |
| Reusable evaluator, adapter, normalization, or loader mechanics | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) after implementation and review | No implementation belongs under `policy/opa/`. |
| Semantic input and decision meaning | [`contracts/policy/`](../../contracts/policy/README.md) | Consume; never redefine. |
| Machine shapes | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/README.md) | Consume; never redefine. |
| Reusable fixtures and executable conformance | Root `fixtures/` and `tests/`, except a specifically governed native-test co-location | No test authority here while the lane is held. |
| Validation and repository tooling | `tools/validators/` and governed workflows | No validator or OPA binary here. |
| Runtime/deployment configuration | `configs/`, `runtime/`, and infrastructure surfaces according to accepted responsibility | No secret or deployment configuration here. |
| Emitted decisions, receipts, proofs, reviews, and lifecycle records | Their accepted process and accountability families | Never store instances beside source. |
| Release, correction, withdrawal, and rollback decisions | [`release/`](../../release/README.md) | No approval or publication authority. |

### No-parallel-writers rule

Until an accepted decision resolves this path:

- do not add Rego that also exists or would naturally live in `policy/rego/` or
  another policy child;
- do not add an OPA directory bundle, tar archive, lock, manifest, or selector
  that competes with `policy/bundles/`;
- do not add evaluator code or configuration that competes with
  `packages/policy-runtime/`, `configs/`, or runtime/deployment ownership;
- do not create `policy/opa/promotion/` from a draft reference;
- do not establish copy-and-sync, generated-mirror, or compatibility behavior
  through convention alone; and
- do not use this README to pre-decide whether the path is retained, narrowed,
  migrated, frozen as compatibility, or retired.

The safe current action for operational payloads is **HOLD**. A future decision
must select one writer, preserve references and history, and prevent two active
homes for the same rule or bundle.

[Back to top](#top)

## What belongs here

While the convergence hold is active, the admissible contents are deliberately
narrow:

- this evidence-grounded boundary README;
- the existing zero-byte placeholder marker;
- a pointer to an **accepted** ADR, path decision, migration record, or
  deprecation record that resolves this directory's fate; and
- migration-only documentation required to move or retire the path without
  breaking verified consumers, if such consumers are later found.

Operational content belongs here only after an accepted decision gives this
lane a unique responsibility that does not overlap Rego source, bundle
packaging, evaluator implementation, runtime configuration, tests, receipts, or
release records. That decision must name its owner, scope ID, writers, readers,
inputs, outputs, versioning, validation, exposure, retention, correction, and
rollback.

[Back to top](#top)

## What is prohibited

| Do not place or claim here | Required posture or owning surface |
|---|---|
| Rego modules, package trees, or native tests copied from another policy lane | Keep one reviewed source under its accepted `policy/` child. |
| `promotion/` merely because a draft standard names it | Resolve placement and authority first; promotion policy currently has its own lane. |
| OPA bundle archive, data document, manifest, lock, index, selector, signature, or active-version pointer | Use the accepted [`policy/bundles/`](../bundles/README.md) contract after graduation. |
| OPA executable, container image, WebAssembly compiler, plugin, SDK, adapter, loader, server, or sidecar implementation | Implementation, build, runtime, package, or infrastructure roots by responsibility. |
| `.opa/` configuration, credentials, tokens, private endpoints, trust roots, signing keys, or deployment secrets | Never commit secrets; configuration and deployment remain separately governed. |
| Real `PolicyInputBundle`, source payload, evidence, personal record, restricted location, or protected static policy data | Use governed references and restricted stores; public Git is not an input store. |
| Emitted engine result, `PolicyDecision`, decision log, trace, receipt, review, validation report, proof, or cache | Use the accepted accountability, runtime, test-artifact, or data lane. |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, RollbackCard, deployment, or publication state | [`release/`](../../release/README.md) and governed operations. |
| Public-client bundle discovery or browser-side rule selection | Governed server-side enforcement and released public-safe carriers only. |
| Hidden fetch logic or fallback-to-allow behavior | Explicit input assembly and fail-closed evaluator handling are mandatory. |
| README prose presented as policy activation, engine approval, security proof, compliance, or release permission | Require the owning decision and executable evidence. |

Protected details must not be embedded in rules, examples, reasons, logs, or
fixtures merely to demonstrate denial. Use minimal synthetic public-safe cases
under the accepted fixture lane.

[Back to top](#top)

## Inputs and outputs

### Current inputs

This placeholder accepts no runtime input. It does not read a request, actor,
audience, source, evidence reference, rights status, consent status,
sensitivity label, lifecycle state, review record, bundle digest, evaluator
version, release reference, correction state, or clock.

The README's evidence inputs are the pinned repository tree, accepted placement
rules, parent and adjacent boundary documents, current workflow definitions,
and the two draft references that name an uncreated child.

### Current outputs

The only committed outputs are documentation and an empty marker. This lane
emits no native OPA value, decision, reason, obligation, receipt, proof, review,
artifact, lifecycle transition, release, or public response.

### Future evaluation boundary

If KFM accepts an OPA-backed evaluation profile, the complete flow must remain
explicit and responsibility-separated:

```text
governed facts and references
  -> accepted PolicyInputBundle profile
  -> immutable policy source or bundle plus exact digest
  -> pinned evaluator family, version, entrypoint, and limits
  -> engine-native result, reasons, obligations, or evaluator error
  -> lossless normalization into the accepted decision contract
  -> authenticated decision and replay receipt
  -> governed consumer enforcement
  -> separate lifecycle, release, correction, and publication decisions
```

An engine-native boolean or set is not automatically a canonical outcome.
Undefined, empty, malformed, stale, untrusted, or failed evaluation must never
be converted to `ANSWER` or permission. Any mapping into `ANSWER`, `ABSTAIN`,
`DENY`, or `ERROR` must be accepted, versioned, tested, reason-preserving, and
obligation-preserving.

[Back to top](#top)

## Lifecycle and trust boundary

`policy/opa/` changes no KFM data or publication lifecycle state. In
particular:

- a rule file does not admit source data;
- a bundle does not create evidence closure;
- an OPA evaluation does not authenticate a reviewer;
- a policy answer does not promote RAW, WORK, QUARANTINE, PROCESSED, CATALOG,
  TRIPLET, or PUBLISHED state;
- a workflow pass does not approve release;
- a commit, pull request, merge, tag, or GitHub release does not publish KFM
  knowledge; and
- public clients must not bypass governed APIs by reading policy source or
  selecting a bundle directly.

Rights, consent, sensitivity, cultural sovereignty, living-person and genomic
information, rare-species locations, archaeology, infrastructure, private-land
joins, and harmful precision remain fail-closed inputs. OPA may evaluate
governed classifications; it cannot discover, invent, downgrade, or clear them.

[Back to top](#top)

## Exposure, mutation, and retention

| Dimension | Boundary |
|---|---|
| Repository visibility | Public. Documentation and future source comments must be safe to disclose. |
| Intended operating exposure | Internal policy substrate only; no ordinary public-client access. |
| Current mutation | Versioned changes to README and marker bytes only. New operational payloads remain held. |
| Permitted writers | **NEEDS VERIFICATION.** CODEOWNERS is routing evidence, not a complete writer or approval policy. |
| Runtime writes | None. Evaluators and consumers must treat accepted policy bytes as read-only. |
| Retention | Durable Git history until an accepted migration or retirement decision; emitted runtime state retains elsewhere. |
| Generation | No generator, mirror, compiled output, or synchronization relationship is established. |
| Secrets and protected data | Prohibited. Use secret management and governed restricted stores. |
| Public reasons | Must be stable, bounded, and non-reconstructive; detailed protected context stays restricted. |

[Back to top](#top)

## Validation

### Current evidence checks

| Check | What it proves | What it does not prove |
|---|---|---|
| Exact tree and blob inspection | The directory has exactly README plus zero-byte `.gitkeep` at the pinned base | Permanent absence, intended future purpose, or runtime behavior. |
| Bounded repository-reference search | Two draft documents name `policy/opa/`; one names proposed `promotion/` | Acceptance, consumer binding, or permission to create the path. |
| [`policy-test`](../../.github/workflows/policy-test.yml) source inspection | Broad static readiness hold, one separate native-test inventory, placeholder runtime, no general command | OPA evaluation in this lane or production enforcement. |
| [`pass12-release-policy-v1`](../../.github/workflows/pass12-release-policy-v1.yml) source inspection | One workflow definition pins OPA 1.19.0 and executes exact files under `policy/rego/` | Hosted success at every ref, general OPA adoption, or this-lane activation. |
| `make policy` source inspection | The general target remains a TODO echo | Any policy parsing, test, or decision. |
| Local Markdown link check | Repository-relative links and fragments in this README resolve | External availability, semantic truth, or policy correctness. |
| Metadata-block validation | The bounded metadata envelope is structurally valid | Registry acceptance, owner approval, or currentness forever. |
| Generated-receipt validation | Final authored bytes are hash-bound with declared evidence and checks | Factual authority, policy permission, merge, release, or publication. |

### Documentation command surface

The following checks are appropriate for this README-only boundary change:

```bash
git diff --check

python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  policy/opa/README.md

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --output /tmp/policy-opa-meta-report.json \
  policy/opa/README.md

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<generated-receipt>.json \
  --repo-root .
```

The generated-receipt filename is supplied by the pull request that changes
this README. Do not report the placeholder `make policy` target as validation,
and do not invent `opa test policy/opa/`: there is no rule or native test here.

### Graduation validation minimum

Before any operational content can leave hold, require the dependency-closed
set appropriate to the accepted role:

1. accepted path and ownership decision with one canonical writer;
2. stable profile, package, entrypoint, bundle, evaluator, and toolchain
   identities;
3. explicit input contract and schema with no hidden fetches;
4. fail-closed defaults and lossless native-to-outward outcome normalization;
5. public-safe reason codes and enforceable obligations;
6. synthetic positive, negative, abstain/hold, missing-context, malformed,
   stale, restricted, and evaluator-error fixtures;
7. native parse, format, unit, fixture-polarity, mutation, and anti-coercion
   coverage as applicable;
8. deterministic, checksum- or provenance-pinned evaluator installation;
9. read-only least-privilege CI with stable failure semantics;
10. governed consumer enforcement, authenticated decisions, receipt/replay,
    expiry, cache invalidation, correction, withdrawal, and rollback tests; and
11. review by policy, contracts/schema, validation, security/privacy, affected
    domain/source, runtime, supply-chain, and release owners as applicable.

A green test proves only its named inputs, evaluator, source, and assertions. It
does not establish evidence sufficiency, rights clearance, reviewer authority,
release readiness, or public safety.

[Back to top](#top)

## Contributor guidance

### README-only changes

1. Pin current `main`, inspect open work and this directory's exact tree.
2. Preserve the placeholder and convergence-hold truth unless current accepted
   evidence has changed it.
3. Reconcile `policy/rego/`, `policy/bundles/`, `policy/runtime/`,
   `packages/policy-runtime/`, draft `policy/opa/` references, and policy-test
   behavior before changing responsibility claims.
4. Keep exactly one H1, stable document identity, valid local links, a final
   newline, and an accurate generated receipt for substantive AI work.
5. Do not turn a proposed path, example, workflow name, badge, or passing check
   into implementation or authority.

### Any proposed operational payload

Stop and open a focused design/convergence review before adding a non-document
file or child directory. That review must answer:

- What unique responsibility would this lane own?
- Why can the artifact not remain under `policy/rego/`, another policy family,
  `policy/bundles/`, `packages/policy-runtime/`, `configs/`, `runtime/`,
  `fixtures/`, `tests/`, or `release/`?
- Is this path canonical, compatibility-only, migration-bound, deprecated, or
  retired?
- Which existing and proposed references must move or redirect?
- Who writes, reviews, selects, consumes, and rolls back the artifact?
- Which exact version, digest, entrypoint, input, native output, canonical
  outcome, reason, obligation, receipt, correction, and expiry contracts bind
  it?
- How are secrets, private policy data, restricted reasons, and public-client
  access excluded?
- What native and end-to-end negative evidence proves fail-closed behavior?

Do not answer those questions by adding the files first. If the decision would
change canonical placement, split/merge authority, or create compatibility
behavior, use the accepted ADR and migration process before dependent
implementation.

### Review burden

| Change class | Minimum review posture |
|---|---|
| README-only evidence repair | Policy-aware maintainer plus documentation review. |
| Path purpose, compatibility, migration, or retirement | Policy owner, Directory Rules/governance reviewer, affected lane owners, and migration review. |
| Rego or bundle content | Policy, affected domain/source, validation, security/privacy, bundle/runtime, and release review. |
| Evaluator, adapter, binary, container, or toolchain | Runtime/package, supply-chain/security, CI, policy, validation, and operations review. |
| Input/decision/reason/obligation semantics | Contracts, schemas, policy, consumers, fixtures/tests, and migration review. |
| Promotion, release, correction, withdrawal, or rollback coupling | Independent policy and release/accountability review with separation of duties. |

No author, generator, workflow, CODEOWNERS route, or repository administrator is
treated as sole policy approver merely by holding write access.

[Back to top](#top)

## Correction, rollback, and supersession

For a defect in this README, use a transparent same-path forward fix or revert
the documentation commit. The prior README blob is
`8b137891791fe96927ad78e64b0aad7bded08bdc`, containing one newline. Restoring
that blob removes guidance and should not be mistaken for restoring policy
behavior, because this lane has none.

Before merge, abandoning the draft branch and pull request leaves `main`
unchanged. After an authorized merge, revert this README and its generated-work
receipt together or issue a reviewable forward fix. The `.gitkeep` is unchanged
and should remain unless an accepted path decision explicitly removes or
replaces the placeholder.

If an operational payload is added here incorrectly:

1. hold affected evaluation, promotion, release, and public use;
2. preserve the exact bytes, commit, bundle/evaluator identity, inputs,
   decisions, receipts, consumers, and effective interval for audit;
3. determine the one accepted canonical destination before moving anything;
4. stop parallel writers and invalidate stale selectors, caches, and decisions;
5. repair references and emit owning correction, withdrawal, or rollback
   records where actual reliance occurred; and
6. use a versioned migration or transparent revert rather than rewriting shared
   history.

A Git revert may repair repository source. It does not by itself retract a
decision, invalidate a deployed cache, withdraw a release, or correct public
reliance.

[Back to top](#top)

## Related surfaces

| Surface | Current relationship | Authority limit |
|---|---|---|
| [`policy/README.md`](../README.md) | Parent policy authority, maturity model, authoring contract, and trust membrane | Does not assign an OPA child role by implication. |
| [`policy/rego/`](../rego/README.md) | Current engine-native Rego source lane and sole separately governed native test | Does not create a general bundle or evaluator. |
| [`policy/bundles/`](../bundles/README.md) | Bundle packaging, manifest, selection, replay, and rollback boundary | No accepted executable bundle or selector is established. |
| [`policy/runtime/`](../runtime/README.md) | Runtime-facing policy source and placeholder sublanes | Not a runtime engine or active evaluator. |
| [`policy/promotion/`](../promotion/README.md) | Promotion-admissibility boundary | Must not be duplicated under a proposed OPA technology path. |
| [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | Future reusable evaluator-helper boundary | Version `0.0.0` placeholder; no functional OPA adapter. |
| [PolicyInputBundle contract](../../contracts/policy/policy_input_bundle.md) | Proposed semantic input boundary with explicit-context posture | Meaning does not prove input assembly or evaluation. |
| [PolicyDecision contract](../../contracts/policy/policy_decision.md) | Proposed canonical finite decision meaning | Does not authenticate an engine result or authorize release. |
| [RunReceipt standard](../../docs/standards/RUN_RECEIPT.md) | Draft lineage that names proposed `policy/opa/promotion/` | Explicitly not accepted path evidence. |
| [Flora file-system plan](../../docs/domains/flora/FILE_SYSTEM_PLAN.md) | Draft lineage that lists `policy/opa/` among proposed policy locations | Lower authority than accepted Directory Rules and current lane contracts. |
| [`policy-test`](../../.github/workflows/policy-test.yml) | Static readiness guard and general evaluator hold | Evaluates no rule in this lane. |
| [`pass12-release-policy-v1`](../../.github/workflows/pass12-release-policy-v1.yml) | Bounded checksum-pinned OPA execution for exact Rego files elsewhere | Does not activate or validate `policy/opa/`. |
| [`release/`](../../release/README.md) | Release, correction, withdrawal, and rollback decision plane | Policy source and evaluator results are inputs, never approval. |

[Back to top](#top)

## Open verification register

| ID | Open item | Current posture |
|---|---|---|
| `OPA-001` | Is `policy/opa/` retained, narrowed, migrated, frozen as compatibility, or retired? | **NEEDS GOVERNANCE / PATH DECISION** |
| `OPA-002` | What unique responsibility, owner, local scope ID, permitted writer, and reader would justify this lane? | **UNKNOWN** |
| `OPA-003` | How should the two draft `policy/opa/` references converge, especially the absent `promotion/` child? | **NEEDS REFERENCE AND MIGRATION REVIEW** |
| `OPA-004` | What relationship, if any, should exist among this path, `policy/rego/`, `policy/bundles/`, and `policy/runtime/`? | **CONFLICTED / HOLD** |
| `OPA-005` | Which bundle format, manifest, lock, selector, signature, static-data rule, and activation process are accepted? | **NOT ESTABLISHED** |
| `OPA-006` | Which evaluator family/version, OPA provenance and checksum process, entrypoints, resource limits, and error semantics are accepted? | **PARTIAL ONLY FOR PASS 12; GENERAL PROFILE UNKNOWN** |
| `OPA-007` | Which adapter, normalization, governed consumer, decision authentication, reason registry, and obligation enforcement are accepted? | **NOT ESTABLISHED** |
| `OPA-008` | Which evaluation receipt, replay, expiry, cache-key, correction, withdrawal, and rollback contracts bind consequential decisions? | **NOT ESTABLISHED** |
| `OPA-009` | Which tests and workflows are merge- or release-significant, and how is independent approval enforced? | **UNKNOWN / NEEDS SETTINGS EVIDENCE** |
| `OPA-010` | Where do non-secret evaluator configuration, protected static policy data, trust roots, and deployment controls belong? | **NEEDS RESPONSIBILITY AND SECURITY REVIEW** |
| `OPA-011` | What migration proves zero parallel writers and repairs every verified reference and consumer? | **NEEDS MIGRATION PLAN AND DRILL** |

[Back to top](#top)

## Evidence and no-loss ledger

### Evidence snapshot

| Evidence | Pinned state | Supported conclusion |
|---|---|---|
| Repository base | `main@ad31275429d715ad92002f8f2e160299193c9f50` | Exact authoring snapshot. |
| `policy/opa/` tree | `f7fbc9bbbbbc0f140ec86ba639f31e0a69108edd` | Exactly two direct files. |
| Prior README | `8b137891791fe96927ad78e64b0aad7bded08bdc` | One-newline placeholder; no prior prose or anchor to preserve. |
| `.gitkeep` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | Zero-byte marker only. |
| Parent policy README | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` | OPA child role was explicitly `NEEDS VERIFICATION`. |
| Rego lane README | `0d8ddd117e091d5af099fa36aaa94487eafd20a4` | Current engine-native source and bounded native-test boundary. |
| Bundle lane README | `77f59c399fbce668c916cbbc385009121d6169f4` | Separate packaging/manifest/selection responsibility. |
| Runtime-policy README | `80b63e7651429903385066b53c7fb41af3cd1298` | Runtime-facing rule-source scaffolds, not evaluator implementation. |
| Policy-runtime package README | `5a20cfac50a93f497765421b7566559ae49a39b8` | `0.0.0` placeholder and no OPA adapter. |
| Broad policy workflow | `ac8f125e8a4d3634d86f66836d2aa2c0e3925e75` | Static hold plus one separately governed lane. |
| Pass 12 OPA workflow | `478f910e8e899796d15b8921e3baa55f4ce1ce73` | Checksum-pinned OPA execution outside this directory. |
| Draft RunReceipt standard | `144f6a153ba9223a617e2718bca3e161bf24e605` | Proposed absent `policy/opa/promotion/` reference. |
| Draft Flora plan | `80e808f4c327b113b02abb8dd48ca2465f8983ae` | Design-lineage reference to `policy/opa/`, not adoption. |
| Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` | Placement order, one policy authority root, dependency separation, and README profile. |
| ADR-0029 | `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` | Directory Rules v2 adoption and non-effects. |

### Material no-loss disposition

| Baseline element | Disposition |
|---|---|
| Existing path | **PRESERVED** — same-path modernization. |
| Prior content | **PRESERVED BY DISCLOSURE** — prior file contained only one newline. |
| Existing marker | **PRESERVED** — `.gitkeep` is unchanged. |
| Proposed OPA/promotion reference | **SURFACED AS CONFLICT** — recorded without creating or accepting it. |
| Current Rego source lane | **PRESERVED / NON-DUPLICATED**. |
| Bundle and evaluator boundaries | **CLARIFIED** without changing their bytes or maturity. |
| General OPA readiness hold | **PRESERVED**. |
| Policy, lifecycle, evidence, rights, sensitivity, release, correction, and publication separation | **PRESERVED AND ENRICHED**. |
| Operational behavior | **UNCHANGED** — documentation and provenance only. |

### Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| placeholder | 2026-08-13 | Added a one-newline README beside `.gitkeep`. | Historical blob `8b137891…`. |
| v0.1.0 | 2026-08-13 | Documents the exact placeholder state, unresolved OPA-path conflict, no-parallel-writers hold, responsibility split, validation limits, contributor gates, correction, rollback, and open decision register. No policy or runtime behavior changes. | Revert this README and its generated-work receipt together or apply a transparent forward fix. |

<p align="right"><a href="#top">Back to top</a></p>
