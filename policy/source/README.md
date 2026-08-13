<a id="top"></a>

# policy :: source

> **One-line purpose.** `policy/source/` is the current local policy-source
> boundary for proposed source-admission rules and doctrine-artifact prerequisite
> rules. It inherits authority from [`policy/`](../README.md); it does not define
> source truth, admit or activate a source, resolve rights or sensitivity, execute
> a general policy engine, approve release, or publish.

> [!IMPORTANT]
> **Safe current conclusion:** at
> `main@6888e0391a1e80e45cf3724652cf34d1ec36230c`, this directory contains this
> 44-byte README stub and two Rego files. The SourceDescriptor workflow verifies
> that `descriptor_required_before_ingest.rego` remains a non-enforcing
> `PROPOSED` stub. The doctrine-artifact policy expresses a three-file missing
> prerequisite rule, but the current promotion workflow executes a separate
> Python registry check—not this Rego module—and deliberately proves the missing
> prerequisite remains visible and fail-closed.

> [!CAUTION]
> Neither file establishes an accepted source-admission policy bundle. A policy
> filename, package name, hard-coded artifact list, schema pass, Python check,
> receipt, workflow pass, commit, or merge is not a source activation,
> `PolicyDecision`, evidence finding, release approval, or publication event.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Rules](#current-rule-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Source admission](#source-admission-policy-trust-boundary) · [Doctrine artifacts](#doctrine-artifact-prerequisite-trust-boundary) · [Evaluation](#rule-source-runtime-evaluation-and-release) · [Exposure](#exposure-mutation-and-retention) · [Naming drift](#parallel-naming-and-authority-drift) · [Validation](#validation-coverage-and-limits) · [Related evidence](#related-contracts-schemas-registries-tests-and-workflows) · [Authoring](#authoring-and-review-contract) · [Correction](#correction-and-rollback) · [Review](#review-triggers-and-evidence-snapshot) · [Open verification](#open-verification-register)

## Purpose

`policy/source/` documents and contains two candidate policy concerns:

1. whether a source may cross the pre-ingest boundary without an admitted,
   governed descriptor; and
2. whether a bounded operation must be denied because required doctrine
   artifacts are absent.

These concerns are related by source prerequisites, but they are not one
operational decision path. Each requires its own accepted input contract,
outcomes, bundle and entrypoint identity, evaluator, native tests, consumer,
receipts, review, correction, and rollback before runtime reliance.

This README describes the tracked bytes, their direct evidence relationships,
and their limits. It does not activate either module, accept
[ADR-0017](../../docs/adr/ADR-0017-source-descriptor-admission-process.md),
admit a doctrine artifact, or make the current source lane canonical over a
parallel path by documentation alone.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical root for normative allow, deny, hold, restrict, and abstain rule source. |
| README profile | `BOUNDARY_COMPACT`: this child changes source-admission and prerequisite trust assumptions while inheriting the parent root contract. |
| Placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Section 9.3 places policy rule source under singular `policy/`; section 16 defines this local README contract and direct-child map law. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) projects `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The projection does not create authority. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, independent review, approval, or effective branch protection. |
| Local owner | **NEEDS VERIFICATION.** No accepted source-policy steward, doctrine-artifact policy steward, or independent approver was established by the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** The two Rego package names are machine identifiers, not accepted local scope or bundle identifiers. |
| Release authority | None. Policy may supply one reviewed gate input; [`release/`](../../release/README.md) owns release, correction, withdrawal, rollback, promotion, and signature decisions. |
| Publication authority | None. Source, doctrine, receipt, workflow, or repository state cannot publish KFM knowledge. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Target README | 44-byte `Greenfield bundle stub.`, blob `943fa9991f259721920b93f9c13eec07b4197502` | The local boundary contract was absent before this documentation-only update. |
| Direct-child inventory | This README and two Rego files | Presence does not establish adoption, bundle membership, execution, or completeness. |
| Descriptor prerequisite module | [`descriptor_required_before_ingest.rego`](./descriptor_required_before_ingest.rego), blob `aae91a65db63a6f795d35db2a3d7d71125024054` | Explicitly marked `PROPOSED greenfield stub. No real rules yet.` |
| Descriptor executable effect | `default deny := false`; the only rule sketch is commented out | The module denies no input and emits no operative reason or obligation. |
| SourceDescriptor workflow | [`source-descriptor-validate`](../../.github/workflows/source-descriptor-validate.yml) asserts the exact stub marker and non-denying default while exercising bounded schema and fixture checks | It verifies that this rule remains unimplemented; it does not run OPA or make an admission, rights, activation, review, release, or publication decision. |
| Doctrine-artifact module | [`doctrine_artifact_required.rego`](./doctrine_artifact_required.rego), blob `23135bf1528bdc10b336d878932a0de38269e42f` | Declares three required filenames and a `missing_required_doctrine_artifact:<filename>` reason for absent `input.present` entries. |
| Doctrine Rego execution | No native Rego test, accepted input schema, bundle selector, or OPA invocation was established for this module | Its source semantics are inspectable; runtime behavior and compatibility remain unproved. |
| Doctrine registry | [`document_registry_doctrine_required.yaml`](../../control_plane/document_registry_doctrine_required.yaml) is `PROPOSED` and names the same three files with `needs_verification` status | Registry presence and filename parity do not admit the files or bind the Rego module. |
| Doctrine artifact directory | `docs/doctrine/artifacts/` is absent at the evidence base | The repository-owned Python prerequisite check reports missing artifacts and returns failure. |
| Python prerequisite check | [`check_required_doctrine_artifacts.py`](../../scripts/maintenance/check_required_doctrine_artifacts.py) reads the registry, checks presence, size, status alignment, and duplicate hashes, and can emit JSON process memory | This is a separate implementation path; it does not evaluate `doctrine_artifact_required.rego`. |
| Focused doctrine test | [`test_doctrine_artifact_required.py`](../../tests/policy/test_doctrine_artifact_required.py) checks only that the Rego file contains `package` and `deny`, then proves the Python checker currently fails and can write a failure receipt | A passing pytest result confirms the expected hold, not prerequisite satisfaction or Rego correctness. |
| Promotion workflow | [`promotion-gate`](../../.github/workflows/promotion-gate.yml) runs the focused Python test with read-only permissions and records `WORKFLOW_HOLD` | It emits summaries only and never promotes, releases, or publishes. |
| General policy evaluator | The broad [`policy-test`](../../.github/workflows/policy-test.yml) workflow statically inventories Rego and preserves a repository-wide OPA hold | No accepted general bundle manifest, evaluator binding, executable policy runtime, or source-policy consumer is established. |
| Source admission architecture | [ADR-0017](../../docs/adr/ADR-0017-source-descriptor-admission-process.md) remains `proposed` | Bounded SourceDescriptor shape validation exists; admission authority and runtime remain held. |
| Release and publication | Separate governed responsibilities | Nothing in this directory promotes, releases, deploys, or publishes a source or doctrine artifact. |

All current-state claims above are pinned to
`main@6888e0391a1e80e45cf3724652cf34d1ec36230c`. Later repository changes
require a fresh inventory and claim review.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned tree, exact tracked bytes, tests, scripts, workflows, or accepted decision. |
| **PROPOSED** | Candidate rule, decision, input, behavior, placement, or integration not accepted as current operation. |
| **NEEDS VERIFICATION** | A bounded check, assignment, migration, or decision remains before reliance. |
| **UNKNOWN** | The inspected evidence cannot support a stronger statement. |

[Back to top](#top)

## Current direct-child map

This map was verified from the complete tracked directory at the evidence base.
It shows this directory and direct children only.

```text
policy/source/
├── README.md
├── descriptor_required_before_ingest.rego  # PROPOSED, non-enforcing stub
└── doctrine_artifact_required.rego          # unbound prerequisite rule source
```

None of the three files is marked as generated, mirrored, localized, or
converted in its tracked bytes. A future bundle or generated relationship must
name its writable source, generator, digest, and synchronized outputs before
this README treats that relationship as established.

[Back to top](#top)

## Current rule inventory

| Module | Package | Native source shape | Current proven effect |
|---|---|---|---|
| [`descriptor_required_before_ingest.rego`](./descriptor_required_before_ingest.rego) | `kfm.descriptor_required_before_ingest` | Boolean `deny` defaults to `false`; candidate denial is commented out | Denies nothing. The SourceDescriptor workflow checks that this stub posture remains explicit. |
| [`doctrine_artifact_required.rego`](./doctrine_artifact_required.rego) | `kfm.doctrine_artifact_required` | Set-valued `deny` defaults empty; a rule emits one reason per missing required filename in `input.present` | Source expresses a bounded prerequisite rule, but no native evaluation, input validation, or consumer binding is proved. |

The two modules also use different `deny` shapes—boolean versus a set of reason
strings. No accepted normalization maps either result into the repository's
candidate outward `PolicyDecision` vocabulary. Callers must not infer a shared
entrypoint or coerce `false`, an empty set, a validation failure, or evaluator
error into permission.

[Back to top](#top)

## What belongs here

Subject to accepted contracts, schemas, bundle conventions, and review, this
boundary may contain:

- source-admission and source-prerequisite declarative policy source;
- operation-specific rules that consume authoritative descriptor, source-role,
  rights, consent, sensitivity, provenance, review, lifecycle, release,
  correction, and doctrine-artifact context;
- fail-closed handling for missing, invalid, stale, conflicted, restricted,
  revoked, superseded, or unreviewed prerequisite state;
- stable package, entrypoint, version, native-outcome, reason-code, obligation,
  effective-time, and supersession documentation for each local rule family;
- policy-local composition references to rights, sensitivity, access, evidence,
  release, and correction rules without duplicating their authority; and
- bundle-local metadata only when the parent policy root and an accepted bundle
  profile designate this lane as its writable source.

A file belongs here because its primary responsibility is **admissibility**.
Mentioning a source, descriptor, registry, artifact, document, connector, or
ingest operation is not enough.

[Back to top](#top)

## What is prohibited

| Prohibited material | Owning surface or required action |
|---|---|
| SourceDescriptor, DoctrineArtifactDescriptor, source-role, or evidence semantic meaning | [`contracts/source/`](../../contracts/source/README.md) or the accepted semantic contract family |
| JSON Schema, DTO, generated type, or field-shape authority | [`schemas/contracts/v1/source/`](../../schemas/contracts/v1/source/README.md) or another accepted schema family |
| Source registry entries, authority assignments, activation decisions, or canonical source payloads | [`data/registry/sources/`](../../data/registry/sources/README.md), accepted control-plane records, and governed lifecycle lanes |
| Doctrine PDF bytes or converted doctrine artifacts | The accepted doctrine artifact home after rights, provenance, and placement review; never the policy-source directory |
| RAW, QUARANTINE, WORK, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | Governed [`data/`](../../data/README.md) lifecycle and accountability lanes |
| `PolicyDecision`, review, receipt, proof, promotion, release, correction, withdrawal, or rollback instances | Their owning process, accountability, evidence, or [`release/`](../../release/README.md) families |
| Connector, registry service, evaluator, resolver, API, worker, watcher, or reusable package code | [`connectors/`](../../connectors/README.md), [`packages/`](../../packages/README.md), applications, runtime, or tools by responsibility |
| Reusable fixtures, validators, and conformance tests | [`fixtures/`](../../fixtures/README.md), [`tools/`](../../tools/README.md), and [`tests/`](../../tests/README.md), except an explicitly accepted native-engine co-location profile |
| Credentials, private URLs, production payloads, restricted documents, personal data, or harmful-precision locations | Do not commit; use governed secret, quarantine, redaction, generalization, staged-access, or denial paths |
| A second independently writable policy authority | Resolve compatibility and migration through accepted governance; do not duplicate rule source to escape naming drift |

Do not copy protected source or doctrine content into policy examples merely to
show that it should be denied. Use minimal, synthetic, public-safe fixtures in
the accepted fixture family.

[Back to top](#top)

## Inputs and outputs

### Current descriptor-module inputs

No accepted input contract is bound to
`descriptor_required_before_ingest.rego`. Its commented sketch names
`input.kind` and `input.evidence_bundle_resolved`; those names are illustrative
comments only. The module does not validate required context, resolve a
descriptor or EvidenceBundle, authenticate review, or distinguish malformed
input from a permitted result.

### Current doctrine-module inputs

`doctrine_artifact_required.rego` reads an `input.present` mapping and compares
it with three hard-coded filenames. No accepted schema, canonicalization rule,
digest binding, status model, evaluator version, or relationship to the
control-plane registry is bound to that input.

The Python checker uses a different input path: it parses
`control_plane/document_registry_doctrine_required.yaml` and inspects a local
artifact directory. Similar filenames do not make these two implementations
equivalent.

### Current outputs

The current committed outputs in this directory are policy source and this
human-readable boundary document. The directory emits no evaluated decision,
receipt, proof, review, source activation, ingest disposition, release, or
public artifact.

The separate Python checker may print or write a JSON validation receipt with
presence and integrity observations. That receipt is process memory, not source
authority, doctrine proof, policy evaluation, or release approval.

### Future evaluation inputs

Before either rule family can graduate, a separately accepted input profile
should bind, as applicable:

- the exact operation, actor or service, audience, purpose, and evaluation time;
- governed SourceDescriptor, source authority, doctrine descriptor, registry,
  EvidenceRef, EvidenceBundle, review, and lifecycle references;
- source role, rights, terms, consent, sensitivity, precision, provenance,
  freshness, and correction posture;
- artifact filenames plus content digests, media types, provenance, rights,
  status, and canonical registry identity;
- policy bundle, module, entrypoint, evaluator, and input digest; and
- finite outcomes, public-safe reasons, enforceable obligations, expiry,
  supersession, correction, and rollback references.

These are graduation requirements, not claims that such a profile exists.

[Back to top](#top)

## Source-admission policy trust boundary

Source admission determines how KFM may treat a source. It does not determine
whether every claim from that source is true.

| Concern | Permitted future policy role | Authority it must not assume |
|---|---|---|
| Descriptor | Require an accepted descriptor and exact digest | Define descriptor meaning or machine shape |
| Source role | Constrain use to an accepted role and scope | Promote context, modeled output, or candidate material into primary authority |
| Rights and terms | Deny, hold, restrict, or add obligations from governed status | Infer a license, consent, redistribution right, or public permission |
| Sensitivity | Require review, redaction, generalization, aggregation, or staged access | Downgrade sensitivity or expose the protected fact in a reason |
| Evidence | Require resolvable support appropriate to the operation | Create evidence, make a source self-proving, or treat citation presence as closure |
| Connector | Require a reviewed activation posture before bounded acquisition | Activate a connector, fetch data, write beyond RAW/QUARANTINE, or publish |
| Lifecycle | Constrain a requested transition | Move, promote, release, or publish an object by policy-source presence |
| Review | Require authenticated review and separation of duties | Assign a steward or approve its own source |
| Correction | Apply current revocation, retirement, or supersession context | Create correction or withdrawal state |

Until an accepted source-admission evaluator exists, callers must fail closed
through their existing governed boundary. They must not treat
`default deny := false`, a green SourceDescriptor workflow, or ADR-0017's
proposal language as permission.

[Back to top](#top)

## Doctrine-artifact prerequisite trust boundary

The doctrine-artifact concern asks whether required artifact prerequisites are
present and conforming enough for a later operation to continue. It does not
decide whether the artifacts are authoritative, adopted, rights-cleared,
correct, safe to publish, or sufficient evidence for every claim.

| Layer | Current responsibility | Boundary |
|---|---|---|
| Rego source | Names three required filenames and missing-file reasons | Unbound; no accepted input schema, native test, evaluator, or consumer |
| Control-plane registry | Records three `needs_verification` artifact entries | Machine projection/candidate registry; not artifact admission or proof |
| Python checker | Observes local presence, status mismatch, minimum size, and duplicate hashes | Validation implementation; does not execute policy or assess semantic correctness |
| Focused tests | Require the current missing-prerequisite result and receipt shape | Passing means the hold is working, not that prerequisites are satisfied |
| Promotion workflow | Runs read-only checks and records `WORKFLOW_HOLD` | Does not promote, release, or publish |
| Validation receipt lane | Stores checker process memory | Receipt is not proof, policy permission, catalog closure, or release authority |

If the Rego module and Python checker are intended to represent one decision,
a future slice must define their shared contract, derive the filename set from
one authority or verify exact parity, exercise positive and negative native
cases, normalize results without loss, and define correction and rollback.
Until then, document them as separate paths.

[Back to top](#top)

## Rule source, runtime evaluation, and release

```text
governed facts and references
  -> accepted input profile
  -> pinned policy bundle and evaluator
  -> native result with reasons and obligations
  -> accepted outcome normalization
  -> authenticated decision and receipt
  -> governed consumer enforcement
  -> separate lifecycle, review, release, and publication decisions
```

Only the first repository ingredients are partially present. This lane does
not establish the accepted input profile, bundle membership, evaluator, outcome
normalization, authenticated decision, or governed consumer shown above.

Public clients, maps, exports, dashboards, and AI adapters must not load these
Rego files or decide source admissibility in the browser. They consume only
governed API decisions or already released, public-safe artifacts. Evaluation
errors, missing context, unknown rights, unresolved sensitivity, stale source
state, and absent review must never fall back to allow.

A policy result is still not a promotion or release. Release, correction,
withdrawal, rollback, cache invalidation, and publication remain separate
governed transitions.

[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Current boundary |
|---|---|
| Repository visibility | These files are publicly visible. Do not include secrets, private endpoints, restricted artifact bytes, personal data, or harmful precision. |
| Operating exposure | The root registry classifies `policy/` as internal policy-rule authority. No accepted public API or client-loadable bundle is exposed here. |
| Permitted mutation | Versioned Git review under the parent policy boundary. Effective branch protection and independent approval remain **NEEDS VERIFICATION**. |
| Runtime writes | None. Evaluated decisions, logs, receipts, reviews, artifacts, source payloads, and releases must not be written into this source lane. |
| Retention | Durable source history under `policy/`; decision, receipt, proof, registry, artifact, and release retention remain with their own object families. |
| Generation | No generator or mirror relationship is established for the three direct children. |
| Sensitive inputs | Not retained here. Use governed references and classifications rather than copied payloads. |

[Back to top](#top)

## Parallel naming and authority drift

The parent policy inventory contains both `policy/source/` and
`policy/sources/`. At the evidence base, the plural path contains a `rights/`
child and no direct README. This is observed drift, not evidence of two
accepted source-policy authorities.

This documentation-only update preserves `policy/source/` because it is the
existing tracked target and because workflows and source catalog documents
refer to its descriptor prerequisite module. It does **not** decide that the
singular child name is canonical, authorize new content under the plural path,
or migrate either lane.

Any convergence must first inventory writers and consumers, classify the
`rights/` child, choose one writable authority through an accepted path
decision, repair links and workflow references, preserve compatibility where
needed, and provide a rollback that cannot recreate two writable homes.

[Back to top](#top)

## Validation coverage and limits

### Current executable coverage

| Check | Confirmed coverage | What it does not prove |
|---|---|---|
| `source-descriptor-validate` | SourceDescriptor schema/alias convergence, fixture execution, required rights fields, fail-closed public-release shape, and exact stub markers | Rego evaluation, source admission, rights decision, activation, release, or publication |
| `policy-test` | Static Rego inventory, one separately governed release-gate native-test lane, placeholder runtime, and broader evaluator hold | General policy execution or this lane's native semantics |
| Focused doctrine pytest | Rego file contains two lexical markers; Python checker fails when artifacts are absent and writes a failure receipt | Rego parsing, result parity, successful prerequisite case, artifact authority, or promotion |
| Doctrine test-suite wrapper | Runs doctrine preflight validators and a bounded Python test family | Accepted source-policy bundle or OPA evaluation |
| `promotion-gate` | Read-only orchestration proving the current doctrine prerequisite is visibly held | Prerequisite satisfaction, promotion, release, or publication |
| Generated-receipt validator | Bounded receipt shape, local-path parity, and supported SHA-256 artifact bindings | Factual correctness, authenticated review, policy permission, merge, release, or publication |

### Repository-native checks

```bash
# SourceDescriptor shape and fixture entrypoints; not policy evaluation.
python tools/validators/validate_source_descriptor.py --fixtures
python tools/validators/sources/validate_source_descriptor.py --fixtures

# Doctrine prerequisite behavior. The pytest passes by proving the checker
# currently returns its expected fail-closed result.
python -m pytest -q tests/policy/test_doctrine_artifact_required.py

# Broader doctrine preflight and consistency family.
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

No repository-native command was established that safely evaluates both Rego
modules in `policy/source/`. Do not invent `opa test policy/source/` or treat the
broad policy workflow as native test coverage for this lane.

### Documentation validation for this README

This documentation revision should preserve:

- one H1, logical heading order, balanced language-tagged fences, and a final
  newline;
- the existing H1 and same-path identity;
- exact direct-child parity and verified repository-relative links;
- the distinct boolean and set-valued `deny` shapes;
- exact stub, workflow, registry, checker, test, and hold boundaries;
- no policy, schema, fixture, workflow, runtime, release, or publication change;
  and
- a generated receipt whose artifact hash matches the final README bytes.

Passing documentation checks proves presentation and evidence alignment only.
It does not activate either policy module.

[Back to top](#top)

## Related contracts, schemas, registries, tests, and workflows

| Surface | Confirmed role | Authority limit |
|---|---|---|
| [`policy/README.md`](../README.md) | Parent policy-root authority, maturity inventory, and trust boundary | Does not activate this lane or resolve singular/plural child drift. |
| [Directory Rules v2](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted placement and README-profile authority | Do not prove policy execution or accept ADR-0017. |
| [ADR-0017](../../docs/adr/ADR-0017-source-descriptor-admission-process.md) | Proposed source-admission architecture, state separation, maturity holds, and acceptance gates | Remains proposed and explicitly lacks an accepted source-admission bundle/evaluator. |
| [`source_descriptor.md`](../../contracts/source/source_descriptor.md) | Draft semantic SourceDescriptor contract | Meaning is not policy permission, machine shape, or activation. |
| [`source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Rich proposed machine shape exercised by bounded fixtures | Schema validity is not source truth or admission. |
| [SourceDescriptor fixture family](../../fixtures/contracts/v1/source/source_descriptor/README.md) | Synthetic valid and invalid cases used by bounded validation | Fixture polarity does not establish live-source fitness. |
| [`source-descriptor-validate`](../../.github/workflows/source-descriptor-validate.yml) | Read-only shape, entrypoint, fixture, and rights-presence checks with explicit holds | Does not execute policy or activate a source. |
| [`source_authority_register.yaml`](../../control_plane/source_authority_register.yaml) | Proposed, currently empty source-authority projection | Empty file establishes no activation authority. |
| [`data/registry/sources/`](../../data/registry/sources/README.md) | Documented source-registry instance boundary | Operational populated conformance and public use are not established. |
| [`packages/source-registry/`](../../packages/source-registry/README.md) | Shared source-registry mechanics boundary | ADR-0017 identifies it as a placeholder, not an operational admission service. |
| [`document_registry_doctrine_required.yaml`](../../control_plane/document_registry_doctrine_required.yaml) | Proposed three-entry prerequisite registry | Does not admit, authenticate, or prove the artifact bytes. |
| [`check_required_doctrine_artifacts.py`](../../scripts/maintenance/check_required_doctrine_artifacts.py) | Repository-owned presence and integrity checker | Separate from Rego evaluation and semantic doctrine review. |
| [`test_doctrine_artifact_required.py`](../../tests/policy/test_doctrine_artifact_required.py) | Focused expected-hold and receipt test | Lexical Rego check plus Python behavior only. |
| [Doctrine validation receipt lane](../../data/receipts/validation/doctrine_artifact_check/README.md) | Process-memory boundary for checker output | Receipt is not proof, policy, review, promotion, or release. |
| [`promotion-gate`](../../.github/workflows/promotion-gate.yml) | Read-only doctrine and promotion-readiness orchestration | Explicitly emits no promotion decision or public artifact. |
| [`policy-test`](../../.github/workflows/policy-test.yml) | Broad readiness drift guard | Evaluates no repository-wide policy and preserves the general OPA hold. |

Together these surfaces form partial review evidence, not an accepted
end-to-end source-admission or doctrine-prerequisite decision chain.

[Back to top](#top)

## Authoring and review contract

A material rule change should identify and validate:

- the bounded operation and owning policy family;
- accepted semantic contracts and machine input/output shapes;
- stable package, entrypoint, bundle, evaluator, and version identities;
- default behavior, native outcomes, outward normalization, reason codes, and
  obligations;
- source role, rights, consent, sensitivity, evidence, lifecycle, review,
  release, correction, and rollback dependencies;
- positive, negative, missing-context, malformed, stale, restricted, abstain,
  and evaluator-error cases as applicable;
- deterministic, public-safe fixtures and native Rego tests;
- a repository-native no-network command and least-privilege hosted workflow;
- governed consumer enforcement, bypass resistance, decision receipts, replay,
  expiry, supersession, and cache invalidation; and
- compatibility with existing catalog documents, workflow stub assertions,
  registry/checker behavior, and parallel-path consumers.

Changing `descriptor_required_before_ingest.rego` from its exact stub posture
will intentionally fail `source-descriptor-validate`; the implementation slice
must update that workflow's assertions and add real native policy coverage
rather than weakening the hold. Changing the doctrine filename set or result
shape must reconcile the registry, Python checker, tests, receipts, promotion
workflow, and downstream consumers—or explicitly supersede the old path.

README-only clarification requires policy-aware source/docs review. Rule,
bundle, evaluator, activation, rights, sensitivity, promotion, or release
changes require the corresponding source, policy, validation, security/privacy,
runtime, and release reviewers. The author, generator, or rule module cannot be
its sole approver for a policy-significant transition.

[Back to top](#top)

## Correction and rollback

This README revision and its generated receipt change documentation and
provenance only. They do not alter Rego, contracts, schemas, registries,
fixtures, tests, scripts, workflows, runtime, source state, doctrine artifacts,
policy decisions, release state, or public artifacts.

- **Before merge:** close or abandon the draft pull request. The target on the
  evidence base remains blob `943fa9991f259721920b93f9c13eec07b4197502`.
- **After an authorized merge:** revert the documentation/provenance commit or
  apply a transparent forward fix that preserves corrected evidence and Git
  history.
- **Policy correction:** version or supersede the affected rule, bundle,
  evaluator, input contract, tests, decision receipts, and consumers; do not
  rewrite this README to conceal a rule defect.
- **Source or doctrine reliance discovered:** stop the affected operation,
  preserve evidence and receipts, reassess rights/sensitivity/review state, and
  use the owning correction, withdrawal, release, and rollback processes. A Git
  revert alone may not repair an external decision or exposure.
- **Path convergence:** never roll back into two writable policy authorities.
  Prefer a validated forward fix when reversal would recreate ambiguity.

[Back to top](#top)

## Review triggers and evidence snapshot

### Evidence snapshot

| Evidence | Reviewed identity |
|---|---|
| Repository base | `main@6888e0391a1e80e45cf3724652cf34d1ec36230c` |
| Prior target | `943fa9991f259721920b93f9c13eec07b4197502` |
| Descriptor / doctrine Rego | `aae91a65db63a6f795d35db2a3d7d71125024054` / `23135bf1528bdc10b336d878932a0de38269e42f` |
| Parent policy README | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` |
| Directory Rules / ADR-0029 | `fd49a0b83e55cef52c1124281f093e263526898d` / `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` |
| Root registry / CODEOWNERS | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` / `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| ADR-0017 | `58693830fcdf9746c5494fdd85298529fa5594a9`; status `proposed` |
| SourceDescriptor workflow | `6d3f900efcddc17d24a528a92190544fc350b63b` |
| Policy / promotion workflows | `ac8f125e8a4d3634d86f66836d2aa2c0e3925e75` / `9b567aad17de2a7419a2a0238386745c1cb5c11c` |
| Doctrine focused test / checker / registry | `9ce6ec84f1c0080bc92f0ae3bfd3f640f42032d0` / `47b8a91a28267c0d0512cc4625fbe7791f207c69` / `1215fadf99c39978bfa6a669c888396a7ef3e277` |
| Open-PR overlap | No open pull request was returned for the repository or the exact target immediately before authoring |
| Review date | 2026-08-12 |

Re-review this boundary when any of the following changes:

- a direct child, package, default, rule, filename, reason, outcome shape,
  status marker, or generation relationship;
- a source descriptor, doctrine descriptor, registry, checker, fixture, test,
  workflow, bundle, evaluator, or consumer relationship;
- ADR-0017, ADR-0029, Directory Rules, parent policy authority, or root-registry
  projection;
- `policy/source/` versus `policy/sources/` ownership or compatibility posture;
- source role, rights, consent, sensitivity, evidence, lifecycle, review,
  correction, promotion, release, or public exposure;
- CODEOWNERS, required checks, review independence, branch protection, or
  workflow trust posture; or
- drift between this README, tracked bytes, and executable validation.

[Back to top](#top)

## Open verification register

| ID | Open item | State | Evidence needed to close |
|---|---|---|---|
| `SRC-POL-001` | Accepted local policy owners and independent review route | **NEEDS VERIFICATION** | Approved responsibility assignments and effective review controls |
| `SRC-POL-002` | Canonical local lane: `policy/source/` or `policy/sources/` | **CONFLICTED / NEEDS DIRECTORY REVIEW** | Writer/consumer inventory, accepted path decision, compatibility plan, and rollback |
| `SRC-POL-003` | Accepted SourceDescriptor schema, validator, and fixture paths | **CONFLICTED** | ADR-0017 convergence decision and migration tests |
| `SRC-POL-004` | Accepted source-admission input and decision contracts | **NOT ESTABLISHED** | Versioned contracts, schemas, finite outcomes, reasons, obligations, and fixtures |
| `SRC-POL-005` | Implemented descriptor prerequisite rule | **CONFIRMED absent at the evidence base** | Fail-closed Rego, native tests, bundle/evaluator binding, and workflow update |
| `SRC-POL-006` | Doctrine Rego input contract and native semantics | **UNKNOWN** | Accepted schema, positive/negative/error native tests, and deterministic OPA run |
| `SRC-POL-007` | One authority for the doctrine filename set | **NEEDS VERIFICATION** | Derived source or exact parity validation across Rego and registry/checker paths |
| `SRC-POL-008` | Doctrine artifact admission, authenticity, rights, and semantic review | **NOT ESTABLISHED** | Admitted descriptors, digests, provenance, rights, review, and correction evidence |
| `SRC-POL-009` | Accepted source-policy bundle, selector, evaluator, and outcome normalization | **UNKNOWN / NOT ESTABLISHED** | Versioned bundle/evaluator plus native-to-outward conformance tests |
| `SRC-POL-010` | Governed source-admission consumer and connector binding | **NOT ESTABLISHED** | Runtime integration, bypass tests, authenticated decisions, and receipts |
| `SRC-POL-011` | Decision replay, expiry, correction, retirement, and rollback | **UNKNOWN** | Persisted decision identity and exercised correction/rollback drill |
| `SRC-POL-012` | Effective required-check and separation-of-duties enforcement | **NEEDS VERIFICATION** | Current platform settings and exact-head hosted-check evidence |
| `SRC-POL-013` | Production or external reliance on either module | **UNKNOWN** | Repository and external consumer inventory with owner confirmation |
| `SRC-POL-014` | Promotion, release, and publication integration | **CONFIRMED unauthorized by current lane** | Separate governed gates and release evidence; policy source remains insufficient |

Until these items close through their owning authorities, this lane remains a
mixed-maturity policy-source boundary: one explicitly non-enforcing stub, one
unbound rule source, and no accepted end-to-end evaluator or consumer.

[Back to top](#top)

## No-loss and change ledger

| Baseline element | Disposition |
|---|---|
| Stable path and H1 | Preserved |
| `Greenfield bundle stub.` | Replaced with a repository-grounded boundary contract; current greenfield maturity remains explicit |
| Two tracked Rego modules | Preserved and documented without byte changes |
| Descriptor stub marker and non-denying default | Preserved as explicit workflow-enforced current state |
| Doctrine three-file rule | Preserved and separated from the Python checker and registry path |
| Policy, evidence, lifecycle, release, and publication boundaries | Added from accepted parent and Directory Rules authority |
| Direct-child navigation | Added from the verified tree |
| Validation and rollback | Added with exact current limitations and reversible documentation posture |
| Naming drift and unknowns | Surfaced; not silently normalized or resolved |

This README does not upgrade a stub or unbound rule to implemented status.

<p align="right"><a href="#top">Back to top</a></p>
