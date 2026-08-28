<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-rego-readme
title: policy/rego/ — Rego Policy-Source Lane
type: readme
version: v0.1.0
status: draft; BOUNDARY_COMPACT; repository-grounded; mixed-maturity; one-bounded-native-test-profile; general-evaluator-unbound; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ to @bartytime4life; accepted Rego-lane stewardship and independent policy approval were not established
created: 2026-08-13
updated: 2026-08-13
current_path: policy/rego/README.md
owning_root: policy/
policy_label: internal; policy; rego; opa; mixed-maturity; fail-closed; non-release; non-publication
responsibility: Define the Rego source and native-test lane, its exact module inventory, validation boundaries, lifecycle non-effects, and contribution contract without becoming bundle selection, evaluator, decision, release, or publication authority.
base_commit: 09a01ef8a71a557efc1c35bda6f9b762a429a1f3
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED three Rego files, one PROPOSED_INACTIVE Pass 12 profile with checksum-pinned OPA 1.19.0 native tests and fixtures, one PMTiles publication rule with marker-only workflow inspection, and broad repository evaluator hold / PROPOSED BOUNDARY_COMPACT Rego lane contract / NEEDS VERIFICATION accepted general package conventions, bundle selector, evaluator binding, normalization, decision receipts, production consumers, correction propagation, and required-check coupling
related:
  - ../README.md
  - ../bundles/README.md
  - ../bundles/pass12-release-gate-v1/README.md
  - ../../fixtures/policy/release_gate_v1/README.md
  - ../../packages/policy-runtime/README.md
  - ../../tools/validators/policy/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../release/README.md
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/pass12-release-policy-v1.yml
  - ../../.github/workflows/pmtiles-attestation.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: rego

> **One-line purpose.** `policy/rego/` holds reviewed Rego policy source and the
> repository's currently co-located engine-native Rego test; it does not select
> a bundle, provide a general evaluator, emit authoritative decisions, approve
> release, or publish.

> [!IMPORTANT]
> **Safe current conclusion at `main@09a01ef8a71a`:** this lane has mixed
> maturity. `release_gate_v1.rego` is a bounded `PROPOSED_INACTIVE` profile with
> a native test, four synthetic fixtures, and a dedicated workflow that installs
> checksum-pinned OPA 1.19.0. `tiles_publish.rego` is deny-by-default source whose
> current PMTiles workflow checks selected text markers but does not run OPA or
> native policy tests. No accepted repository-wide bundle, selector, evaluator,
> policy-runtime implementation, decision receipt, or production consumer is
> established.

> [!CAUTION]
> A parse, format pass, unit test, fixture result, static marker check, workflow
> success, or `allow: true` result is bounded validation evidence. It cannot
> resolve evidence, rights, consent, sensitivity, cryptography, reviewer
> authority, lifecycle state, release approval, or publication.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Children](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Lifecycle](#lifecycle-and-trust-boundary) · [Validation](#validation) · [Contributing](#contributor-guidance) · [Correction](#correction-and-rollback) · [Open work](#open-verification-register)

## Purpose

This directory is the engine-native Rego **source lane** beneath the canonical
[`policy/`](../README.md) root. A module here may evaluate one explicit,
versioned input and expose engine-native outcomes, reasons, and obligations for
a bounded operation.

The directory is not itself an OPA bundle, evaluator installation, bundle
registry, runtime service, or decision store. General policy packaging belongs
to [`policy/bundles/`](../bundles/README.md) after acceptance; execution and
normalization belong to an accepted evaluator such as a governed implementation
under [`packages/policy-runtime/`](../../packages/policy-runtime/README.md).

## Inherited authority, owner, and scope

| Field | Current boundary |
|---|---|
| Parent authority | [`policy/`](../README.md), the adopted root for normative admissibility rule source. |
| README profile | `BOUNDARY_COMPACT`: executable rule source changes trust, runtime, lifecycle, exposure, and release assumptions. |
| Placement basis | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3, 14, and 16 separate policy source from contracts, schemas, applications, decisions, and release records. |
| Local owner and scope ID | **NEEDS VERIFICATION.** CODEOWNERS routing is not accepted policy stewardship or independent approval. Each package/profile supplies a local identity, but no general lane scope ID is accepted. |
| Exposure | Repository-public source; intended operating exposure is internal. Public clients must not load or choose repository rules. |
| Mutation and retention | Versioned, durable Git source. Prior accepted versions and evaluation identities must remain replayable. |
| Release/publication authority | None. Engine-native results are inputs to separate governed review, lifecycle, and release decisions. |

## Current status

| Surface | Confirmed evidence | Safe status |
|---|---|---|
| README lineage | PR #2683 added a one-newline file at current main; this revision supplies the missing boundary | Documentation only. |
| [`release_gate_v1.rego`](./release_gate_v1.rego) | Package `kfm.pass12.release_gate_v1`; `default allow := false`; deterministic deny set and sorted decision reasons | **PROPOSED_INACTIVE bounded executable profile**. |
| [`release_gate_v1_test.rego`](./release_gate_v1_test.rego) | Six native tests: one allow and five denial cases | **CONFIRMED native coverage for the named cases only**. |
| Pass 12 fixtures | One positive and three workflow-evaluated negative fixtures | **CONFIRMED bounded polarity evidence**; not complete policy or release proof. |
| Pass 12 workflow | Downloads OPA 1.19.0, verifies SHA-256, formats, tests, evaluates fixture polarity, and checks stable deny reasons | **CONFIRMED command-bearing definition**; hosted exact-head result remains separate evidence. |
| Pass 12 bundle directory | Documentation-only packaging profile | No bundle payload, selector, signature, or activation. |
| [`tiles_publish.rego`](./tiles_publish.rego) | Package `kfm.tiles.publish`; deny-by-default rule and denial messages | **Source present; native test and accepted evaluator binding not established**. |
| PMTiles workflow | Checks required policy text markers while validating a partial attestation boundary | Marker/static evidence only; it does not parse or execute the Rego module. |
| `policy-test` | Requires exactly the Pass 12 native-test inventory and preserves a broader OPA/runtime hold | Does not evaluate repository-wide policy. |
| `make policy` | Prints `TODO: opa test policy/ -v` | Readiness marker only; a zero exit proves no policy behavior. |

## Current direct-child map

Verified from the tracked tree at the pinned base:

```text
policy/rego/
├── README.md
├── release_gate_v1.rego
├── release_gate_v1_test.rego
└── tiles_publish.rego
```

`release_gate_v1_test.rego` is the sole Rego test currently recognized by the
broad `policy-test` readiness guard. That observed co-location does not establish
a general convention for every policy family.

## What belongs here

- reviewed Rego modules whose primary responsibility is operation-specific
  admissibility under the parent policy contract;
- stable package and entrypoint identities, fail-closed defaults, engine-native
  outcomes, public-safe reasons, and machine-enforceable obligations;
- small engine-native test modules only when a specific profile deliberately
  owns the co-location and a dedicated workflow executes them;
- comments that state maturity, non-effects, expected input identity, and
  supersession posture; and
- links to accepted contracts, schemas, fixtures, validators, bundles,
  evaluators, consumers, decisions, receipts, release gates, correction, and
  rollback.

A `.rego` extension does not by itself justify placement. The primary
responsibility must be policy source, not test fixture data, application code,
release state, or generated output.

## What is prohibited

| Do not place or claim here | Owning surface or posture |
|---|---|
| Semantic object definitions | `contracts/`; Rego consumes accepted meaning. |
| JSON Schema, generated types, or DTO authority | `schemas/`; Rego input checks do not become schema authority. |
| General bundle manifest, archive, selector, signature, or activation state | [`policy/bundles/`](../bundles/README.md) and accepted control/evaluator systems. |
| OPA binary, runtime adapter, API, CLI, cache, or evaluator service | `packages/`, `runtime/`, `apps/`, or tools by responsibility. |
| Reusable generic fixtures and conformance tests | Root `fixtures/` and `tests/`, except a specifically governed engine-native co-location. |
| Evaluated `PolicyDecision`, review, receipt, proof, validation report, or lifecycle instance | Their accepted process and accountability families. |
| ReleaseManifest, CorrectionNotice, WithdrawalNotice, RollbackCard, promotion, deployment, or publication state | [`release/`](../../release/README.md) and governed operations. |
| Secrets, source payloads, private terms, personal data, DNA, exact sensitive locations, or protected facts in reasons/tests | Keep out of Git; use synthetic public-safe references and restricted systems. |
| Browser-side bundle selection or client-side hiding as enforcement | Governed server-side decisions and released public-safe carriers only. |

## Inputs and outputs

### Current Pass 12 profile

The profile reads a declared release scope, spec digest, evidence references,
sensitivity review/class, attestation posture, human review, and release,
correction, and rollback references. It exposes:

- `allow`, default `false`;
- a deterministic `deny` set with stable reason codes; and
- `decision` containing profile ID, allow, and sorted denial reasons.

It does not resolve those references, authenticate review, verify signatures,
normalize into the four-value `PolicyDecision` contract, or perform release.

### Current PMTiles profile

The module reads nested PMTiles/PMIDX/PMSIG, RunReceipt, release, and policy
fields. It exposes `allow` and message-valued `deny` rules. No accepted schema
binding, native fixture family, evaluator invocation, or normalization contract
for this Rego package is established by the current workflow.

### General output boundary

Rego evaluation may produce engine-native values only. An accepted adapter must
preserve denial, restriction, hold, abstention, and error semantics, reasons,
obligations, bundle/evaluator identity, exact input digest, effective time, and
correction state. Undefined or malformed results must never become permission.

This directory stores no emitted decisions or runtime logs.

## Exposure, mutation, and retention

| Dimension | Boundary |
|---|---|
| Repository visibility | Public. Rules, comments, reasons, and tests must be safe to disclose. |
| Operating exposure | Internal policy source; public clients consume governed decisions or released carriers, not `.rego` files. |
| Mutation | Versioned review. Material changes update the dependency-closed rule, tests, fixtures, package/profile docs, workflow, consumer expectations, and correction plan. |
| Retention | Durable source/test history sufficient for replay; decisions, inputs, receipts, and releases retain elsewhere. |
| Runtime writes | None. Evaluators treat source as read-only. |
| Generation | No direct child is declared generated. Generated bundles or bindings require a named source, generator, digest, and derived-only edit policy. |

## Lifecycle and trust boundary

```text
governed facts and references
  -> accepted input profile
  -> pinned Rego source or bundle plus evaluator
  -> engine-native result, reasons, and obligations
  -> accepted normalization and authenticated decision/receipt
  -> governed consumer enforcement
  -> separate lifecycle, review, release, correction, and publication actions
```

This directory owns only the source/test portion of that sequence. A rule may
constrain a requested lifecycle transition, but it cannot move RAW, WORK,
QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state. Public exposure
requires independently resolved evidence, rights, consent, sensitivity, review,
release, correction, and rollback context.

## Validation

### Bounded executable coverage

The current repository defines this exact Pass 12 command surface:

```bash
/tmp/opa fmt --fail \
  policy/rego/release_gate_v1.rego \
  policy/rego/release_gate_v1_test.rego

/tmp/opa test \
  policy/rego/release_gate_v1.rego \
  policy/rego/release_gate_v1_test.rego
```

The dedicated workflow obtains `/tmp/opa` from the OPA 1.19.0 release and
verifies the pinned binary digest before those commands. Local execution is
valid only with an independently verified matching binary; do not substitute an
unpinned download and report equivalent provenance.

### Current limits

| Check | What it proves | What it does not prove |
|---|---|---|
| Pass 12 OPA format/test | The two named files format and six native tests pass under the pinned workflow binary | Complete input validity, accepted bundle/evaluator, reviewer authentication, release, or publication. |
| Pass 12 fixture polarity/reasons | Four fixture outcomes and three named denial reasons match expectations | All negative cases, mutation coverage, consumer enforcement, or normalized decisions. |
| `policy-test` | Expected file inventory, dedicated workflow markers, placeholder runtime, and broader hold remain visible | General OPA execution or `tiles_publish` behavior. |
| PMTiles attestation workflow | Selected `tiles_publish.rego` text markers remain and adjacent Python/JSON checks run | Rego parsing, native policy semantics, cryptographic closure, release, or publication. |
| Metadata, local-link, and topology checks | README structure, local references, and repository drift posture | Policy correctness or runtime behavior. |

Do not report `make policy` as validation. The target intentionally echoes a
TODO and is guarded in that state by `policy-test`.

## Contributor guidance

1. Pin current `main`, inspect open work and package consumers, and classify the
   change as documentation, rule behavior, test coverage, bundle/evaluator, or
   release integration.
2. Preserve one stable package/entrypoint identity or version it deliberately;
   do not silently change boolean, set, object, reason, or obligation shapes.
3. Rule changes require native positive, negative, missing-context, malformed,
   stale, restricted, evaluator-error, and anti-coercion cases as applicable,
   using synthetic public-safe fixtures.
4. Reconcile bundle/profile docs, pinned evaluator provenance, workflow paths,
   consumer normalization, receipts/replay, correction, expiry, cache
   invalidation, and rollback in the same dependency-closed slice.
5. A second `*_test.rego` changes the exact inventory enforced by `policy-test`;
   add it only with deliberate local ownership and workflow coverage.
6. Never weaken a fail-closed default or static hold merely to make a workflow
   green. Expose the dependency or maturity change explicitly.
7. Require policy, affected domain/source, contracts/schema, validation,
   security/privacy, runtime consumer, and release review as applicable.

## Correction and rollback

For a README defect, revert or forward-fix this file. The prior blank blob is
`8b137891791fe96927ad78e64b0aad7bded08bdc`; documentation rollback changes no
Rego behavior.

For a rule defect, hold affected operations, preserve the prior source, package,
bundle, evaluator, inputs, outputs, fixtures, tests, decisions, and receipts,
issue a versioned successor with effective time and supersession linkage, and
re-evaluate dependent decisions and releases. Route correction, withdrawal,
cache invalidation, and rollback through their owning systems. Do not rewrite
shared history or restore an older rule without proving bundle selection and
stale-decision invalidation.

Before merge, abandoning the draft PR leaves main unchanged. After an authorized
merge, a transparent revert is appropriate only when it does not recreate a
known unsafe or ambiguous policy state; otherwise use a reviewed forward fix.

## Open verification register

| ID | Open item | Posture |
|---|---|---|
| `REGO-001` | Accepted lane owner, package/version convention, and engine-native test co-location rule | **NEEDS VERIFICATION** |
| `REGO-002` | Accepted bundle format, manifest, selector, signature, evaluator, and activation process | **UNKNOWN / NOT ESTABLISHED** |
| `REGO-003` | Accepted normalization from each native result shape into governed decision objects | **NEEDS CONTRACT/IMPLEMENTATION DECISION** |
| `REGO-004` | Native tests, fixtures, and actual OPA execution for `tiles_publish.rego` | **NOT ESTABLISHED** |
| `REGO-005` | Governed production consumers, decision receipts, replay, expiry, and cache-key binding | **UNKNOWN** |
| `REGO-006` | Rights, sensitivity, consent, review, correction, and rollback propagation under rule changes | **PARTIAL / NEEDS IMPLEMENTATION** |
| `REGO-007` | Required-check coupling and independent approval for policy-significant changes | **UNKNOWN** |

<p align="right"><a href="#top">Back to top</a></p>
