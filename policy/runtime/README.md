<a id="top"></a>

# policy :: runtime

> **One-line purpose.** `policy/runtime/` is the current local rule-source
> boundary for policy that may constrain runtime invocation, evidence-dependent
> answers, unpublished public exposure, runtime receipts, and proposed
> cross-lane runtime gates. It inherits authority from [`policy/`](../README.md);
> it does not implement a policy evaluator, execute a model or API, create
> evidence or receipts, approve release, or publish.

> [!IMPORTANT]
> **Safe current conclusion:** at
> `main@c249771a2dc002ab748d161ccef96ff402ae4ef2`, this directory contains this
> 45-byte README stub, four Rego files, and two `.gitkeep`-only directories.
> Three Rego files are explicit `PROPOSED greenfield stub` modules whose only
> active statement is `default deny := false`. The fourth is a `PROPOSED`
> RunReceipt scaffold whose only rule is `default allow := false`. No native
> test, accepted bundle membership, evaluator binding, outcome normalization,
> or governed consumer was established for any of them.

> [!CAUTION]
> Absence of a native denial is not permission. A package name, commented rule,
> default value, schema pass, receipt validator, workflow pass, commit, merge,
> or documentation statement is not an authenticated `PolicyDecision`,
> evidence finding, runtime authorization, lifecycle transition, release
> approval, or publication event.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Modules](#current-module-and-placeholder-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Decision boundary](#runtime-policy-decision-boundary) · [Evidence and exposure](#evidence-abstention-and-public-exposure-stubs) · [RunReceipt](#runreceipt-policy-scaffold) · [Proposed lanes](#archaeology-and-cross-lane-placeholders) · [Evaluation](#rule-source-evaluation-runtime-and-release) · [Exposure](#exposure-mutation-and-retention) · [Validation](#validation-coverage-and-limits) · [Related evidence](#related-contracts-schemas-fixtures-tests-and-workflows) · [Authoring](#authoring-and-review-contract) · [Correction](#correction-and-rollback) · [Review](#review-triggers-and-evidence-snapshot) · [Open verification](#open-verification-register)

## Purpose

`policy/runtime/` currently groups four candidate rule concerns and two proposed
sub-lanes:

1. whether missing evidence should prevent a runtime answer;
2. whether evidence is required for a bounded runtime operation;
3. whether an unpublished object must be denied from a public operation;
4. whether a RunReceipt-related operation is admissible;
5. whether archaeology runtime policy requires its own child lane; and
6. whether cross-domain runtime gates belong in a shared `cross_lane/` lane.

These concerns touch the same runtime trust membrane, but they are not one
implemented decision path. Each needs an accepted semantic input/output
contract, machine shape, package and entrypoint identity, bundle version,
evaluator, native tests, outward outcome mapping, consumer, receipts, review,
correction, and rollback before operational reliance.

This README documents the tracked bytes, direct evidence relationships, and
limits. It does not fill in the commented rules, adopt proposed ADRs, select a
runtime policy bundle, turn placeholder directories into accepted homes, or
make the current modules executable through prose.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical root for normative allow, deny, hold, restrict, and abstain rule source. |
| README profile | `BOUNDARY_COMPACT`: this child affects runtime, evidence, public-exposure, and receipt trust assumptions while inheriting the parent root contract. |
| Placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Section 9.3 places policy rule source under singular `policy/`; section 16 defines the local README and direct-child contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) projects `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The projection does not activate this child. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, independent review, approval, or effective branch protection. |
| Local owner | **NEEDS VERIFICATION.** No accepted runtime-policy steward, RunReceipt-policy steward, archaeology-policy steward, or cross-lane policy approver was established by the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** Rego package names are implementation identifiers, not accepted bundle, scope, or activation identities. |
| Evaluation authority | None. [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) remains a `0.0.0` placeholder with no accepted evaluator, bundle selector, or consumer binding. |
| Runtime authority | None. [`runtime/`](../../runtime/README.md) owns internal runtime composition; policy source must not contain provider, adapter, API, model, worker, or service implementation. |
| Release authority | None. Policy may supply one reviewed gate input; [`release/`](../../release/README.md) owns release, correction, withdrawal, rollback, promotion, and signature decisions. |
| Publication authority | None. Rule source, a receipt, a workflow, an API scaffold, a commit, or a merge cannot publish KFM knowledge. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Target README | 45-byte `Greenfield bundle stub.`, blob `b9bfee731553c504b514f07a6862ef3e68328f02` | The local boundary contract was absent before this documentation-only revision. |
| Direct-child inventory | This README, four Rego files, and two directories containing only `.gitkeep` | Presence does not establish adoption, bundle membership, execution, consumer binding, or completeness. |
| Missing-evidence module | [`abstain_on_missing_evidence.rego`](./abstain_on_missing_evidence.rego), blob `9c66097140933eba5aa7011653da12488035ad99` | Explicit `PROPOSED greenfield stub. No real rules yet.`; its only active rule is `default deny := false`. |
| Unpublished-public module | [`deny_unpublished_public.rego`](./deny_unpublished_public.rego), blob `8d46a90088c046c102b991904e56ecf32d8ae7d3` | Explicit non-enforcing stub with the same default and commented example shape. |
| Evidence-required module | [`evidence_required.rego`](./evidence_required.rego), blob `297bd7999bf19c4029bf92df6f1c2f07477c787d` | Explicit non-enforcing stub with the same default and commented example shape. |
| Stub executable effect | Each active `deny` value is boolean `false`; candidate denial bodies are comments | The three modules emit no denial, abstention, reason, obligation, or permission. A caller must not convert “no denial” into `ANSWER` or public access. |
| RunReceipt module | [`run_receipt.rego`](./run_receipt.rego), blob `5fa096c9d65183b0b3333e05434bbf6f2ab9c0b7` | Four-line proposed scaffold with package `kfm.generated.policy.runtime.run_receipt` and `default allow := false`; no rule body or reason surface. |
| RunReceipt source relationship | Comment names [`docs/domains/habitat/CANONICAL_PATHS.md`](../../docs/domains/habitat/CANONICAL_PATHS.md) as its source | A comment and `generated` package segment do not establish a generator, mirror, accepted policy derivation, or synchronized artifact contract. |
| RunReceipt machine-shape lane | Proposed [contract](../../contracts/runtime/run_receipt.md), [schema](../../schemas/contracts/v1/runtime/run_receipt.schema.json), fixtures, validator, tests, and aggregate workflow wiring exist | These validate RunReceipt shape and bounded semantic invariants; they do not execute `run_receipt.rego` or make a policy decision. |
| Archaeology directory | [`archaeology/`](./archaeology/) contains only `.gitkeep` | Placeholder presence does not implement the proposed archaeology runtime-policy surface named in domain planning. |
| Cross-lane directory | [`cross_lane/`](./cross_lane/) contains only `.gitkeep` | Archaeology planning treats placement as proposed and explicitly requires an ADR; the empty directory does not resolve that question. |
| Broad policy workflow | [`policy-test`](../../.github/workflows/policy-test.yml) recursively inventories Rego and preserves the general evaluator hold | It does not evaluate this directory. Its only native OPA execution evidence belongs to the separate Pass 12 release-gate lane. |
| General evaluator | No accepted repository-wide bundle manifest, evaluator binding, general OPA command, or functional policy-runtime package | Runtime-policy execution remains unbound. |
| Runtime integration | The runtime root records runtime policy execution as `UNKNOWN` | No provider, adapter, API, worker, or public client was proved to consume these modules. |
| Finite outward decisions | Proposed PolicyDecision and DecisionEnvelope contracts use `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` | No accepted mapping converts these modules' booleans into that vocabulary while preserving reasons, obligations, and errors. |
| Governed API | The proposed trust-membrane ADR and current app evidence remain partial and fail-closed | No governed-API binding to this directory is established. |
| Release and publication | Separate governed responsibilities | Nothing in this directory promotes, releases, deploys, or publishes an answer, source, receipt, layer, or artifact. |

All current-state claims above are pinned to
`main@c249771a2dc002ab748d161ccef96ff402ae4ef2`. Later repository changes
require a fresh inventory and claim review.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned tree, exact tracked bytes, tests, scripts, workflows, or accepted decision. |
| **PROPOSED** | Candidate rule, decision, placement, behavior, or integration not accepted as current operation. |
| **NEEDS VERIFICATION** | A bounded check, assignment, migration, or decision remains before reliance. |
| **UNKNOWN** | The inspected evidence cannot support a stronger statement. |

[Back to top](#top)

## Current direct-child map

This map was verified from the complete tracked directory at the evidence base.
It shows this directory and direct children only.

```text
policy/runtime/
├── README.md
├── abstain_on_missing_evidence.rego  # PROPOSED, non-enforcing deny stub
├── archaeology/                      # .gitkeep only; proposed home
├── cross_lane/                       # .gitkeep only; placement unresolved
├── deny_unpublished_public.rego      # PROPOSED, non-enforcing deny stub
├── evidence_required.rego            # PROPOSED, non-enforcing deny stub
└── run_receipt.rego                  # PROPOSED default-deny allow scaffold
```

The two directories share the same tree identity because each contains the
same empty `.gitkeep` blob; they are distinct tracked paths, not symlinks or one
shared authority. None of the seven direct children establishes a writable
generated or mirrored relationship. Any future generator must name its source,
command, digest, ownership, review, synchronized outputs, and rollback.

[Back to top](#top)

## Current module and placeholder inventory

| Child | Package or tracked shape | Active native surface | Current proven effect |
|---|---|---|---|
| [`abstain_on_missing_evidence.rego`](./abstain_on_missing_evidence.rego) | `kfm.abstain_on_missing_evidence` | Boolean `deny`, default `false` | No denial and no first-class abstention; candidate body is commented out. |
| [`deny_unpublished_public.rego`](./deny_unpublished_public.rego) | `kfm.deny_unpublished_public` | Boolean `deny`, default `false` | No denial or public-exposure decision; candidate body is commented out. |
| [`evidence_required.rego`](./evidence_required.rego) | `kfm.evidence_required` | Boolean `deny`, default `false` | No evidence requirement or denial; candidate body is commented out. |
| [`run_receipt.rego`](./run_receipt.rego) | `kfm.generated.policy.runtime.run_receipt` | Boolean `allow`, default `false` | A fail-closed default if queried exactly, but no rule, reason, obligation, input contract, or consumer binding. |
| [`archaeology/`](./archaeology/) | `.gitkeep` only | None | Placeholder directory only. |
| [`cross_lane/`](./cross_lane/) | `.gitkeep` only | None | Placeholder directory only; proposed placement remains unresolved. |

The modules do not share one entrypoint convention: three expose `deny`, while
one exposes `allow`. None exposes the outward finite result, reason, obligation,
review, receipt, correction, or evaluator-error surface required by the
proposed decision contracts. Callers must not invert `deny`, invert `allow`, or
collapse a missing result, false value, malformed input, or evaluator failure
into permission.

[Back to top](#top)

## What belongs here

Subject to accepted contracts, schemas, bundle conventions, and review, this
boundary may contain:

- declarative policy source governing whether a bounded runtime invocation or
  response may proceed;
- evidence-sufficiency rules that preserve missing, unresolved, stale,
  conflicted, restricted, and invalid support as distinct states;
- public-exposure rules that prevent unpublished or non-release-bound material
  from reaching public runtime operations;
- receipt-required policy that consumes governed RunReceipt references without
  becoming a receipt writer or receipt schema;
- operation-specific rules for model/runtime invocation, tool use, citation,
  answer, render, export, and other runtime-facing decisions;
- approved archaeology or cross-lane runtime policy only after placement,
  ownership, input shape, rights, sensitivity, and review decisions close;
- stable package, entrypoint, bundle, version, native-outcome, reason-code,
  obligation, effective-time, and supersession documentation; and
- fail-closed behavior for missing context, evaluator failure, revoked policy,
  stale decisions, or unsupported operations.

A file belongs here because its primary responsibility is **runtime-facing
admissibility**. Mentioning runtime, AI, evidence, a receipt, an API, a domain,
or public output is not enough.

[Back to top](#top)

## What is prohibited

| Prohibited material | Owning surface or required action |
|---|---|
| Runtime object meaning, PolicyDecision meaning, DecisionEnvelope meaning, or RunReceipt meaning | Accepted [`contracts/`](../../contracts/runtime/README.md) and [`contracts/policy/`](../../contracts/policy/policy_decision.md) families |
| JSON Schema, DTO, generated type, or field-shape authority | [`schemas/contracts/v1/runtime/`](../../schemas/contracts/v1/runtime/README.md) or another accepted schema family |
| Evaluator, bundle loader, adapter, CLI, API, server, worker, provider, model, tool, health check, or reusable library code | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md), [`runtime/`](../../runtime/README.md), [`apps/`](../../apps/governed-api/README.md), workers, or tools by responsibility |
| EvidenceBundle, EvidenceRef, citation, source payload, validation report, or claim truth | Evidence, source, validation, and lifecycle authorities; policy consumes governed status but does not create it |
| RunReceipt, AIReceipt, GENERATED_RECEIPT, review, proof, or decision instances | Their accepted receipt, accountability, evidence, review, or lifecycle lanes |
| RAW, QUARANTINE, WORK, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | Governed [`data/`](../../data/README.md) lifecycle and accountability lanes |
| ReleaseManifest, promotion approval, correction notice, withdrawal, or rollback card | [`release/`](../../release/README.md) and owning accountability families |
| Credentials, provider keys, private prompts, private chain-of-thought, production payloads, restricted sources, personal data, or harmful-precision locations | Do not commit; use governed secrets, quarantine, redaction, generalization, staged access, or denial paths |
| Domain truth or domain semantic contracts | `contracts/domains/`, domain doctrine, and evidence authorities; a domain child under policy owns admissibility only |
| A second independently writable runtime-policy authority | Resolve compatibility and migration through accepted governance; do not duplicate rule source to escape an open placement decision |

Do not copy protected inputs or model outputs into rule comments merely to show
that they should be denied. Use minimal, deterministic, public-safe fixtures in
the accepted fixture family.

[Back to top](#top)

## Inputs and outputs

### Current stub inputs

The three `deny` stubs have no executable rule body. Their commented examples
mention `input.kind` and `input.evidence_bundle_resolved`; those names are
illustrative comments only. The modules do not validate the operation, caller,
audience, evidence, source role, rights, sensitivity, lifecycle, release,
review, policy version, or evaluation time.

### Current RunReceipt-policy inputs

`run_receipt.rego` reads no input. The separate proposed RunReceipt schema and
validator define a substantial machine-shape and validation lane, including
run identity, stage, inputs, outputs, code/spec identity, source and validation
references, outcome, and optional smart-sync context. None of those fields is
bound to this Rego scaffold.

### Current outputs

The committed outputs in this directory are policy source, placeholder paths,
and this human-readable boundary document. If queried directly, the three stub
entrypoints yield `deny = false`, while the RunReceipt scaffold yields
`allow = false`. No repository evidence proves that a governed consumer queries
them, authenticates their result, or persists a decision.

The directory emits no `PolicyDecision`, DecisionEnvelope, RuntimeResponseEnvelope,
RunReceipt, AIReceipt, receipt, proof, review, answer, denial record, lifecycle
transition, release, or public artifact.

### Future evaluation inputs

Before a runtime rule family can graduate, a separately accepted input profile
should bind, as applicable:

- exact operation, actor/service, audience, purpose, request and object IDs,
  evaluation time, and requested runtime capability;
- governed SourceDescriptor, EvidenceRef/EvidenceBundle, citation-validation,
  freshness, and correction references;
- rights, terms, consent, sensitivity, precision, redaction, generalization,
  review, lifecycle, release, and withdrawal posture;
- provider, adapter, model, tool, network, timeout, cancellation, and kill-switch
  context without exposing secrets;
- RunReceipt or AIReceipt identity and integrity where receipt presence is a
  prerequisite;
- policy bundle, module, entrypoint, evaluator, version, digest, and input hash;
  and
- finite native and outward outcomes, public-safe reasons, enforceable
  obligations, expiry, supersession, correction, and rollback references.

These are graduation requirements, not claims that such a profile exists.

[Back to top](#top)

## Runtime policy decision boundary

Proposed KFM decision contracts preserve `ANSWER`, `ABSTAIN`, `DENY`, and
`ERROR` as distinct outward outcomes. Runtime-facing policy must not erase the
difference:

| Outcome | Runtime-policy meaning | Required caller posture |
|---|---|---|
| `ANSWER` | The evaluated operation may proceed under current context and obligations | Continue only through separate evidence, rights, sensitivity, release, citation, and client-safety gates |
| `ABSTAIN` | Admissible support or policy-safe context is insufficient, unresolved, or stale | Do not manufacture an answer; surface a bounded safe reason |
| `DENY` | A policy rule blocks the requested operation | Block it; never retry through a weaker path or leak the protected fact in the reason |
| `ERROR` | Shape, integrity, evaluator, dependency, or process failure prevents a trustworthy decision | Fail closed; preserve error identity and accountability without converting it to permission |

The currently tracked booleans implement none of this outward contract. A
future normalization must preserve native result type, reasons, obligations,
unknowns, and evaluator failures. In particular:

- `deny = false` is not `ANSWER`;
- `allow = false` does not explain `ABSTAIN`, `DENY`, or `ERROR`;
- missing or malformed input is not permission;
- a schema-valid envelope is not an authenticated decision; and
- an authenticated policy decision is still not evidence, release, or publication.

[ADR-0020](../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md)
documents first-class abstention as a **proposed** decision. This README does not
accept it or claim that `abstain_on_missing_evidence.rego` implements it.

[Back to top](#top)

## Evidence, abstention, and public-exposure stubs

The three named deny modules express useful candidate concerns but no operative
rules:

| Candidate concern | Safe intended boundary | Current gap |
|---|---|---|
| Missing evidence | Refuse to manufacture a claim when required support cannot be resolved | Module exposes no abstain outcome, denial reason, evidence contract, or native test |
| Evidence required | Require the right governed evidence for the exact operation | Module does not identify evidence class, sufficiency, freshness, source role, or failure posture |
| Unpublished public material | Prevent internal, candidate, unreleased, withdrawn, or non-public-safe material from public exposure | Module does not identify object, lifecycle state, release binding, audience, correction state, or public operation |

Future work must avoid combining factual insufficiency, policy prohibition, and
process failure into one boolean. Evidence shortage generally maps to an
explicit abstention or error posture; rights, sensitivity, or access rules may
deny; malformed evaluation must fail closed as an error. The accepted contract
and policy family—not a filename—must determine the mapping.

Public clients must never infer permission by reading these files, calling OPA
directly, or observing the absence of a denial. They consume only governed API
decisions or already released public-safe artifacts.

[Back to top](#top)

## RunReceipt policy scaffold

The RunReceipt family has more mature **shape validation** than its local
policy source:

| Layer | Current responsibility | Authority limit |
|---|---|---|
| Rego scaffold | `default allow := false` under a proposed package | No input, rule, reason, obligation, test, bundle, evaluator, or consumer |
| Semantic contract | Proposed meaning for execution-audit identity and provenance | Meaning is not policy permission, runtime execution, or proof of truth |
| JSON Schema | Proposed closed machine shape with declared validator and policy path | Shape does not authenticate a run or bind this Rego module |
| Fixtures and validator | Positive/negative and smart-sync cases with bounded semantic checks | Validator success is not receipt authenticity, evidence closure, or policy evaluation |
| Validator tests and aggregate workflow | Exercise receipt shape and selected no-network semantic invariants | Aggregate workflow does not execute `run_receipt.rego` |
| Receipt worker documentation | Identifies this module as a four-line default-deny scaffold | Worker documentation does not create an accepted worker or policy binding |

A future policy slice must say which operation requires which receipt profile,
how the receipt is resolved and authenticated, which fields are policy inputs,
how missing/invalid/stale/superseded receipts map to outcomes, and which
consumer enforces the decision. It must not turn receipt presence into proof of
truth or approval.

If the module is intended to be derived from Habitat canonical-path planning,
the derivation must become explicit and reproducible. Until then, treat the
comment as lineage, not generation authority.

[Back to top](#top)

## Archaeology and cross-lane placeholders

Both subdirectories contain only `.gitkeep`; neither has a README, rule,
fixture, test, owner, or consumer.

Archaeology continuity planning names `policy/runtime/archaeology/` as a
**proposed** policy surface for archaeology API behavior. Cross-domain planning
names `policy/runtime/cross_lane/` as a **proposed** home but also records an
open placement question and requires an ADR. The tracked directories confirm
path presence only; they do not close those planning questions.

Before either lane receives policy source:

- confirm that runtime-facing admissibility is its primary responsibility;
- resolve domain-specific versus shared cross-lane ownership;
- establish cultural, tribal, rights-holder, sensitivity, security, and public-
  exposure review appropriate to the rule;
- bind contracts, schemas, fixtures, native tests, reasons, obligations,
  evaluator, consumers, receipts, correction, and rollback; and
- prevent a placeholder from becoming a second authority alongside another
  domain or sensitivity policy lane.

[Back to top](#top)

## Rule source, evaluation, runtime, and release

```text
governed request and referenced context
  -> accepted runtime-policy input profile
  -> pinned policy bundle and evaluator
  -> native result with reasons and obligations
  -> lossless finite-outcome normalization
  -> authenticated decision and receipt
  -> governed API or worker enforcement
  -> separate evidence, lifecycle, review, release, and publication decisions
```

Only isolated repository ingredients are present. This lane does not establish
the accepted input profile, bundle membership, evaluator, normalization,
authenticated decision, receipt persistence, or governed consumer shown above.

The broad `policy-test` workflow confirms that policy files exist and that the
general evaluator hold remains visible. Its bounded native OPA proof belongs to
`policy/rego/release_gate_v1*`, not to `policy/runtime/`. The root Makefile still
prints a TODO for the general policy command. Do not invent
`opa test policy/runtime/`, promote recursive inventory to semantic coverage, or
assume the placeholder policy-runtime package performs evaluation.

The proposed governed-API trust-membrane decision remains separate and partial.
Even a complete governed API would consume authenticated policy decisions; it
would not make these source files into public endpoints. Browser, map, export,
AI, and ordinary client code must not load this directory or choose a weaker
policy path after abstention, denial, or error.

A policy result is still not evidence, promotion, release, or publication.
Release, correction, withdrawal, rollback, cache invalidation, and public
exposure remain separately governed transitions.

[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Current boundary |
|---|---|
| Repository visibility | These files are publicly visible. Do not include secrets, provider credentials, private prompts, restricted inputs, personal data, protected cultural information, or harmful precision. |
| Operating exposure | The root registry classifies `policy/` as internal policy-rule authority. No accepted public API or client-loadable bundle is exposed here. |
| Permitted mutation | Versioned Git review under the parent policy boundary. Effective branch protection and independent approval remain **NEEDS VERIFICATION**. |
| Runtime writes | None. Decisions, logs, traces, prompts, responses, receipts, reviews, evidence, artifacts, and releases must not be written into this source lane. |
| Retention | Durable source history under `policy/`; decision, receipt, proof, log, evidence, runtime-state, and release retention remain with their own object families. |
| Generation | No generator or mirror relationship is established for any direct child. |
| Sensitive inputs | Not retained here. Use governed references and classifications rather than copied payloads. |
| Public reasons | Must be bounded and non-reconstructive; a reason must not reveal the very fact, source, location, identity, or vulnerability being protected. |

[Back to top](#top)

## Validation coverage and limits

### Current executable coverage

| Check | Confirmed coverage | What it does not prove |
|---|---|---|
| `policy-test / OPA readiness hold` | Recursive Rego inventory, bounded Pass 12 wiring, placeholder runtime posture, and general evaluator hold | Native parsing or evaluation of this directory, accepted bundle selection, or a runtime decision |
| RunReceipt validator | Proposed schema plus bounded cross-field, URL, digest, HTTP-validator, smart-sync, and safety invariants | Execution authenticity, evidence closure, receipt authority, or Rego evaluation |
| RunReceipt validator tests | Positive, negative, drift, unsafe-input, and bounded no-network behavior for the validator | Runtime consumer binding or policy correctness |
| `schema-validation` | Configures RunReceipt and other aggregate schema/fixture families | Policy execution, rights/sensitivity review, or release approval |
| Governed-API tests | Bounded fail-closed route and envelope behavior in their own application lane | Evaluation of these Rego modules or complete trust-membrane operation |
| Policy boundary guards | Selected structural and API trust boundaries | This lane's bundle, rule semantics, reasons, obligations, or production enforcement |
| Generated-receipt validator | Bounded provenance receipt shape, local-path parity, and supported SHA-256 artifact bindings | Factual correctness, authenticated review, policy permission, merge, release, or publication |

### Repository-native checks

```bash
# Broad readiness inventory and hold; does not evaluate policy/runtime.
python -m pytest -q tests/validators/test_validate_run_receipt.py

# Proposed RunReceipt schema and semantic fixture replay; not Rego evaluation.
python tools/validators/validate_run_receipt.py --fixtures

# Aggregate machine-shape validation; broader inherited failures may remain.
make schemas
```

No repository-native command was established that safely evaluates the four
Rego files in `policy/runtime/`. Native policy tests must be added deliberately
with accepted package/entrypoint semantics and explicit positive, negative,
missing-context, malformed-input, and evaluator-error cases.

### Documentation validation for this README

This documentation revision should preserve:

- one H1, logical heading order, balanced language-tagged fences, and a final
  newline;
- the existing H1 and same-path identity;
- exact direct-child parity and verified repository-relative links;
- exact active defaults, package identities, comments, and placeholder states;
- the separation among rule source, receipt shape validation, evaluator,
  runtime implementation, API enforcement, evidence, release, and publication;
- no policy, schema, fixture, workflow, runtime, release, or public behavior
  change; and
- a generated receipt whose artifact hash matches the final README bytes.

Passing documentation checks proves presentation and evidence alignment only.
It does not activate a rule or close an open placement decision.

[Back to top](#top)

## Related contracts, schemas, fixtures, tests, and workflows

| Surface | Confirmed role | Authority limit |
|---|---|---|
| [`policy/README.md`](../README.md) | Parent policy-root authority, maturity inventory, and trust boundary | Does not activate this lane or supply an evaluator. |
| [Directory Rules v2](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted placement and README-profile authority | Do not prove policy execution. |
| [`runtime/README.md`](../../runtime/README.md) | Internal runtime composition contract with policy-subordinate, finite-outcome, secret-safe posture | Records runtime policy execution as unknown; runtime is not policy-source authority. |
| [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | Proposed reusable evaluator-helper boundary | `0.0.0` placeholder; no functional evaluator, bundle selector, or consumer binding. |
| [`policy-test`](../../.github/workflows/policy-test.yml) | Broad readiness drift guard plus one separately governed bounded Rego lane | Evaluates no rule in this directory. |
| [PolicyDecision contract](../../contracts/policy/policy_decision.md) | Proposed finite policy-decision meaning | Meaning is not evaluation, authenticity, or release approval. |
| [DecisionEnvelope contract](../../contracts/runtime/decision_envelope.md) | Proposed finite runtime transport meaning | Envelope shape is not policy execution or a public answer. |
| [RunReceipt contract](../../contracts/runtime/run_receipt.md) | Proposed execution-audit meaning | Receipt meaning is not proof, policy, or runtime execution. |
| [RunReceipt schema](../../schemas/contracts/v1/runtime/run_receipt.schema.json) | Proposed closed machine shape with smart-sync extension | Schema validity does not bind `run_receipt.rego`. |
| [RunReceipt fixtures](../../fixtures/contracts/v1/runtime/run_receipt/README.md) | Deterministic positive and negative validator inputs | Fixture polarity does not establish live receipt or policy behavior. |
| [RunReceipt validator](../../tools/validators/validate_run_receipt.py) and [tests](../../tests/validators/test_validate_run_receipt.py) | Bounded schema/cross-field/safety validation | Separate implementation path; not an OPA evaluator. |
| [`schema-validation`](../../.github/workflows/schema-validation.yml) | Aggregate schema/fixture orchestration including RunReceipt | Workflow success is not receipt authority or policy permission. |
| [ADR-0020](../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | Proposed first-class abstention decision | Remains proposed; the named Rego stub does not implement it. |
| [ADR-0004](../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) and [`apps/governed-api/`](../../apps/governed-api/README.md) | Proposed single dynamic trust-membrane direction plus bounded application scaffold | No accepted complete policy binding or deployed isolation. |
| [Archaeology continuity inventory](../../docs/domains/archaeology/CONTINUITY_INVENTORY.md) | Names a proposed archaeology runtime-policy path | Planning reference does not populate or accept the placeholder. |
| [Archaeology cross-domain plan](../../docs/domains/archaeology/CROSS_DOMAIN.md) | Records cross-lane runtime gate placement as proposed and ADR-dependent | Does not resolve the home or implement a gate. |
| [`data/receipts/`](../../data/receipts/README.md) | Accountability object families | Receipts are process memory, not rule source or proof of truth. |
| [`release/`](../../release/README.md) | Release, correction, withdrawal, and rollback authority | Policy source cannot bypass or replace it. |

Together these surfaces form partial review evidence, not an accepted
end-to-end runtime-policy decision chain.

[Back to top](#top)

## Authoring and review contract

A material rule change should identify and validate:

- the bounded operation, caller, audience, object family, and owning policy
  family;
- accepted semantic contracts and machine input/output shapes;
- stable package, entrypoint, bundle, evaluator, and version identities;
- default behavior, native outcomes, outward normalization, reason codes, and
  obligations;
- evidence, citation, source role, rights, consent, sensitivity, lifecycle,
  review, release, correction, and rollback dependencies;
- runtime provider/adapter/model/tool/network/timeout/cancellation context and
  safe behavior without committing secrets;
- positive, negative, missing-context, malformed, stale, restricted, abstain,
  deny, error, timeout, and evaluator-failure cases as applicable;
- deterministic public-safe fixtures and native Rego tests;
- a repository-native no-network command and least-privilege hosted workflow;
- governed consumer enforcement, bypass resistance, authenticated decisions,
  receipts, replay, expiry, supersession, and cache invalidation; and
- compatibility with the current stubs, proposed contracts, runtime envelopes,
  API boundary, receipt validator, placeholder lanes, and planning documents.

Changing any of the three `default deny := false` modules from their exact stub
posture requires real native policy coverage and consumer-safe normalization;
do not merely remove the stub marker. Adding an allow rule to `run_receipt.rego`
requires accepted input/receipt integrity semantics and denied/error cases.
Populating `archaeology/` or `cross_lane/` requires the unresolved placement and
review questions to close first.

README-only clarification requires policy-aware runtime/docs review. Rule,
bundle, evaluator, provider, model, API, evidence, rights, sensitivity,
receipt, release, or public-exposure changes require their corresponding policy,
runtime, application, security/privacy, validation, evidence, and release
reviewers. The author, generator, evaluator, or rule module cannot be its sole
approver for a policy-significant transition.

[Back to top](#top)

## Correction and rollback

This README revision and its generated receipt change documentation and
provenance only. They do not alter Rego, directories, contracts, schemas,
fixtures, validators, tests, workflows, evaluator code, runtime, providers,
models, APIs, evidence, receipts, lifecycle state, release state, or public
artifacts.

- **Before merge:** close or abandon the draft pull request. The target at the
  evidence base remains blob `b9bfee731553c504b514f07a6862ef3e68328f02`.
- **After an authorized merge:** revert the documentation/provenance commit or
  apply a transparent forward correction that preserves corrected evidence and
  Git history.
- **Policy correction:** version or supersede the affected rule, bundle,
  evaluator, input contract, tests, decision receipts, and consumers; do not
  rewrite this README to conceal a rule defect.
- **Unsafe reliance discovered:** disable the affected consumer, fail closed,
  preserve requests/decisions/receipts and audit evidence, reassess evidence,
  rights, sensitivity, release, and review state, then use the owning correction,
  withdrawal, release, and rollback processes.
- **Path correction:** do not roll back into two independently writable runtime-
  policy homes. Prefer a validated forward fix when reversal would recreate
  ambiguity.

A Git revert may restore source bytes but cannot by itself repair an external
answer, disclosure, model/tool action, receipt, release, or cache. Consequence-
appropriate correction remains required.

[Back to top](#top)

## Review triggers and evidence snapshot

### Evidence snapshot

| Evidence | Reviewed identity |
|---|---|
| Repository base | `main@c249771a2dc002ab748d161ccef96ff402ae4ef2` |
| Prior target | `b9bfee731553c504b514f07a6862ef3e68328f02` |
| Missing-evidence / unpublished-public / evidence-required Rego | `9c66097140933eba5aa7011653da12488035ad99` / `8d46a90088c046c102b991904e56ecf32d8ae7d3` / `297bd7999bf19c4029bf92df6f1c2f07477c787d` |
| RunReceipt Rego | `5fa096c9d65183b0b3333e05434bbf6f2ab9c0b7` |
| Placeholder child trees / `.gitkeep` | `d564d0bc3dd917926892c55e3706cc116d5b165e` / `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| Parent policy README | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` |
| Directory Rules / ADR-0029 | `fd49a0b83e55cef52c1124281f093e263526898d` / `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` |
| Root registry / CODEOWNERS | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` / `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Policy workflow / policy-runtime package | `ac8f125e8a4d3634d86f66836d2aa2c0e3925e75` / `5a20cfac50a93f497765421b7566559ae49a39b8` |
| Runtime root README | `e6843df941a57ca09159083d89ed5952c464ae72` |
| PolicyDecision / DecisionEnvelope contracts | `ebfe97f98263e6309db6d2772cb2c5e548819650` / `b5120a208910f5e2907874b03af1fc8c7f43363d` |
| RunReceipt contract / schema / validator / tests | `5592aa5e22bbdd0c668189f79b50c18f7d1b2479` / `c930ff0fd4da34d8b4ff202d9fd576110258974c` / `d57bc57234a16dc11908e1509b293124e185d388` / `128a3b41317fc9152bc66bc7d94ff2650062f028` |
| Schema-validation workflow | `0e1562f539323daa401184738a0c490b51e2999b` |
| ADR-0020 / ADR-0004 | `8d5ec63b658a1194d2c11359cecb77e7857a9471` / `11b86c462d474385befba0fb2115af9885f592af` — both proposed/draft, unchanged |
| Archaeology continuity / cross-domain planning | `a6b0e5d2cb79b9d08c13ed735f7ed696b0afb183` / `dcf7b99dfcba69d9ac6ebd00e4de07336ad12295` |
| Open-PR overlap | No open pull request was returned for the exact target or runtime-policy query immediately before authoring |
| Review date | 2026-08-12 |

Re-review this boundary when any of the following changes:

- a direct child, package, default, rule, comment, directory payload, reason,
  outcome shape, status marker, or generation relationship;
- a PolicyDecision, DecisionEnvelope, RuntimeResponseEnvelope, RunReceipt,
  AIReceipt, policy input, schema, fixture, validator, workflow, bundle,
  evaluator, runtime, API, worker, or consumer relationship;
- Directory Rules, ADR-0029, ADR-0020, ADR-0004, parent policy authority,
  root-registry projection, or archaeology/cross-lane placement posture;
- evidence, citation, source role, rights, consent, sensitivity, lifecycle,
  review, correction, release, or public exposure;
- CODEOWNERS, required checks, review independence, branch protection, or
  workflow trust posture; or
- drift between this README, tracked bytes, and executable validation.

[Back to top](#top)

## Open verification register

| ID | Open item | State | Evidence needed to close |
|---|---|---|---|
| `RUN-POL-001` | Accepted local owners and independent review route | **NEEDS VERIFICATION** | Approved policy/runtime/application/receipt assignments and effective review controls |
| `RUN-POL-002` | Accepted runtime-policy input and decision contracts | **NOT ESTABLISHED** | Versioned input/output contracts, schemas, finite outcomes, reasons, obligations, and fixtures |
| `RUN-POL-003` | Implemented first-class missing-evidence abstention | **CONFIRMED absent at the evidence base** | Native Rego semantics, tests, outward mapping, evaluator, and governed consumer |
| `RUN-POL-004` | Implemented evidence-required policy | **CONFIRMED absent at the evidence base** | Exact evidence classes/sufficiency/freshness plus fail-closed native tests |
| `RUN-POL-005` | Implemented unpublished-public denial | **CONFIRMED absent at the evidence base** | Object/lifecycle/release/audience inputs, native tests, and public-boundary enforcement |
| `RUN-POL-006` | Accepted RunReceipt-policy semantics and receipt authentication | **NOT ESTABLISHED** | Receipt profile, integrity/resolution rules, reasons, obligations, tests, and consumer binding |
| `RUN-POL-007` | Reproducible derivation of `run_receipt.rego` | **UNKNOWN** | Named generator/source contract, command, digest parity, ownership, and rollback |
| `RUN-POL-008` | Accepted archaeology runtime-policy lane | **PROPOSED / EMPTY** | Placement decision, owners, cultural/tribal/rights review, contracts, rules, and tests |
| `RUN-POL-009` | Accepted cross-lane policy home | **CONFLICTED / NEEDS ADR** | Writer/consumer inventory, accepted ADR, compatibility plan, and rollback |
| `RUN-POL-010` | Accepted runtime-policy bundle, selector, evaluator, and native outcome normalization | **UNKNOWN / NOT ESTABLISHED** | Versioned bundle/evaluator plus native-to-outward conformance tests |
| `RUN-POL-011` | Functional policy-runtime package | **CONFIRMED absent at the evidence base** | Implemented package API, build metadata, tests, consumer, security review, and release process |
| `RUN-POL-012` | Governed API/worker consumer and bypass resistance | **NOT ESTABLISHED** | Integration tests, authenticated decisions, receipts, denied/error paths, and direct-access guards |
| `RUN-POL-013` | Decision replay, expiry, revocation, correction, cache invalidation, and rollback | **UNKNOWN** | Persisted identities and exercised correction/rollback drill |
| `RUN-POL-014` | Effective required checks and separation of duties | **NEEDS VERIFICATION** | Current platform settings and exact-head hosted-check evidence |
| `RUN-POL-015` | Production or external reliance on any local module | **UNKNOWN** | Repository plus external consumer inventory with owner confirmation |
| `RUN-POL-016` | Promotion, release, and publication integration | **CONFIRMED unauthorized by current lane** | Separate governed gates and release evidence; policy source remains insufficient |

Until these items close through their owning authorities, this directory remains
a mixed placeholder boundary: three explicitly non-enforcing deny stubs, one
unbound default-deny RunReceipt scaffold, two empty proposed lanes, and no
accepted end-to-end evaluator or consumer.

[Back to top](#top)

## No-loss and change ledger

| Baseline element | Disposition |
|---|---|
| Stable path and H1 | Preserved |
| `Greenfield bundle stub.` | Replaced with a repository-grounded boundary contract; greenfield maturity remains explicit |
| Four tracked Rego modules | Preserved and documented without byte changes |
| Three `default deny := false` stubs | Preserved as explicit non-enforcing current state |
| RunReceipt `default allow := false` scaffold | Preserved and separated from contract/schema/validator maturity |
| Two `.gitkeep`-only child directories | Preserved and documented as proposed/empty without granting authority |
| Policy, evidence, runtime, receipt, API, lifecycle, release, and publication boundaries | Added from accepted parent and repository evidence |
| Direct-child navigation | Added from the verified tree |
| Validation and rollback | Added with exact current limitations and reversible documentation posture |
| Placement conflicts and unknowns | Surfaced; not silently normalized or resolved |

This README does not upgrade a stub, scaffold, or placeholder directory to
implemented status.

<p align="right"><a href="#top">Back to top</a></p>
