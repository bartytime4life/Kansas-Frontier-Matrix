<a id="top"></a>

# policy :: ui

> **One-line purpose.** `policy/ui/` is the current repository boundary for
> proposed policy source intended to prevent UI-originated telemetry from
> carrying raw evidence or prompt content. It inherits authority from
> [`policy/`](../README.md); it does not implement a policy evaluator, emit
> telemetry, approve release, or publish data.

> [!IMPORTANT]
> **Safe current conclusion:** this directory contains two
> `PROPOSED` greenfield Rego stubs and this README. Each stub defines
> `default deny := false`, contains no operative denial rule, has no native
> Rego test beside it, and is not established as part of an accepted bundle or
> runtime consumer. The
> [`telemetry-policy`](../../.github/workflows/telemetry-policy.yml) workflow
> verifies those limitations and keeps operational enforcement on
> `WORKFLOW_HOLD`.

> [!CAUTION]
> A filename, package name, comment, workflow pass, or policy-shaped file is not
> protection by itself. Until accepted inputs, fail-closed rules, native tests,
> bundle selection, an evaluator, and a governed consumer are bound together,
> callers must not rely on this directory to remove or deny protected content.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Rule inventory](#current-rule-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Trust boundary](#ui-telemetry-trust-boundary) · [Evaluation](#rule-source-runtime-evaluation-and-release) · [Related evidence](#related-contracts-architecture-policy-validation-and-release) · [Validation](#validation-coverage-and-limits) · [Authoring](#authoring-and-review-contract) · [Correction](#correction-and-rollback) · [Open verification](#open-verification-register)

## Purpose

`policy/ui/` documents and contains the repository's current candidate rule
source for two narrow UI-telemetry exclusions:

1. raw evidence or source payloads must not become telemetry content; and
2. prompts, messages, model output, or reasoning content must not become
   telemetry content.

The directory name is broader than the implementation evidence. No reviewed
artifact establishes this lane as the owner of every UI policy concern. Current
tracked bytes support only the two telemetry-related candidates listed above.
General telemetry policy is also represented by the adjacent
[`policy/telemetry/`](../telemetry/README.md) lane, including the separate
[`no_restricted_coords.rego`](../telemetry/no_restricted_coords.rego) stub.
Whether that split is the intended long-term boundary remains
**NEEDS VERIFICATION**.

This README describes the boundary; it does not activate either module, repair
their non-denying defaults, create an accepted policy contract, or authorize
operational telemetry.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent authority | [`policy/`](../README.md) is KFM's canonical source root for normative allow, deny, hold, restrict, and abstain rules. |
| Directory profile | `BOUNDARY_COMPACT`: this lane is policy-bearing and sits at a UI/telemetry exposure boundary. |
| Placement basis | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy source from contracts and schemas and define the local README contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as a canonical, internal, versioned, durable policy-rule root and prohibits data instances, release decisions, and schemas. The registry projects adopted governance; it does not create authority. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, required review, independent approval, or policy acceptance. |
| Local owner | **NEEDS VERIFICATION.** No accepted UI-telemetry policy steward or independent security/privacy approver was established by the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted scope identifier for this directory was found; this README does not invent one. |
| Current evidence base | `main@35c58cb1c6cbf09567c17f9ff9776b2086c8d0bb`; target prior blob `eb88e0b34c6c26ac90e046af44843661ede41a51`. |
| Release authority | None. Policy evaluation may eventually supply one input to a release decision, but [`release/`](../../release/README.md) owns release, correction, withdrawal, and rollback decisions. |
| Publication authority | None. A policy result, workflow, commit, pull request, UI rendering, log, dashboard, or telemetry record is not publication. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Target README | 40-byte greenfield stub with the existing H1 and no boundary contract | This update replaces that stub in place; it does not change policy behavior. |
| Directory inventory | Exactly this README and two Rego files | No manifest, data document, native test module, fixture, generated output, or runtime code is tracked here. |
| Raw-evidence module | [`no_raw_in_telemetry.rego`](./no_raw_in_telemetry.rego) is marked `PROPOSED greenfield stub` | It defines `deny` as `false` and executes no denial rule. |
| Prompt module | [`no_prompt_in_telemetry.rego`](./no_prompt_in_telemetry.rego) is marked `PROPOSED greenfield stub` | It defines `deny` as `false` and executes no denial rule. |
| Commented examples | Each module contains a commented `deny[reason]` sketch | Comments are neither executable logic nor an accepted input, reason, or outcome contract. |
| General validator | [`validate_telemetry_safety.py`](../../tools/validators/validate_telemetry_safety.py) raises `NotImplementedError("Greenfield placeholder")` | No general telemetry-safety validator is implemented. |
| Readiness workflow | [`telemetry-policy`](../../.github/workflows/telemetry-policy.yml) checks admitted fixture-only profiles and asserts the stub states | It proves bounded repository-local absence checks and records `WORKFLOW_HOLD`; it does not evaluate these modules with OPA or inspect an operational event. |
| Architecture and decision posture | [UI Telemetry Architecture](../../docs/architecture/ui/TELEMETRY.md) is draft; [ADR-0016](../../docs/adr/ADR-0016-telemetry-redaction-posture.md) remains proposed | Their target posture is design evidence, not accepted runtime behavior. |
| Evaluator and consumer | No accepted bundle selector, general evaluator, emitter, sink, or production consumer was established in the reviewed evidence | Operational enforcement remains unproven and must fail closed outside any explicitly accepted baseline. |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned repository bytes, tree, workflow, or adopted decision. |
| **PROPOSED** | A candidate posture or future implementation that is not current authority. |
| **NEEDS VERIFICATION** | A concrete check or decision is still required. |
| **UNKNOWN** | The reviewed evidence is insufficient to support a stronger claim. |

[Back to top](#top)

## Current direct-child map

This map is verified from the complete tracked tree at the evidence base. It
shows `policy/ui/` and direct children only; presence does not establish
activation or maturity.

```text
policy/ui/
├── README.md
├── no_prompt_in_telemetry.rego
└── no_raw_in_telemetry.rego
```

No child is marked as generated, mirrored, localized, or converted in its
tracked bytes. Any future generator or bundle relationship must identify its
canonical source and deterministic reproduction path before this README treats
it as established.

[Back to top](#top)

## Current rule inventory

| Module | Package | Executable rule state | Current effect |
|---|---|---|---|
| [`no_prompt_in_telemetry.rego`](./no_prompt_in_telemetry.rego) | `kfm.no_prompt_in_telemetry` | `default deny := false`; no operative rule | Does not deny an input. Its commented sketch is illustrative only. |
| [`no_raw_in_telemetry.rego`](./no_raw_in_telemetry.rego) | `kfm.no_raw_in_telemetry` | `default deny := false`; no operative rule | Does not deny an input. Its commented sketch is illustrative only. |

The package names are current machine identifiers. They do not establish an
accepted bundle namespace, import path, query contract, decision shape, or
consumer. Renaming a package would be a policy compatibility change and
requires consumer discovery, native tests, migration evidence, and a separate
review.

[Back to top](#top)

## What belongs here

Subject to accepted contracts and review, this boundary may contain:

- UI-originated telemetry admissibility and protected-content exclusion rules;
- policy-local documentation for those rules, package identities, supported
  operations, finite outcomes, obligations, and failure semantics;
- an accepted manifest or bundle-local metadata only if
  [`policy/`](../README.md) and the repository's bundle authority designate
  this lane as its canonical home;
- source-level compatibility notes and supersession records for these modules.

A future rule belongs here only when `policy/` is its single policy authority
owner and the narrower UI-telemetry scope is supported by accepted evidence.
Topic or filename resemblance is not enough.

[Back to top](#top)

## What is prohibited

The following do not belong in `policy/ui/`:

- UI components, MapLibre adapters, application state, view configuration, or
  deployable telemetry emitters;
- telemetry event instances, logs, traces, metrics, dashboards, alerts, queues,
  sink payloads, or operational receipts;
- raw evidence, source payloads, prompts, messages, model output, reasoning
  content, secrets, credentials, access tokens, private URLs, or crash locals;
- exact restricted coordinates, protected identifiers, small-cohort joins, or
  reconstruction-enabling values used as policy fixtures or examples;
- semantic contracts, canonical schemas, generated types, or policy decision
  instances;
- runtime evaluator code, release decisions, publication records, proofs,
  catalogs, or lifecycle data;
- private, production, unclear-rights, or harmful-precision data.

Use synthetic, minimal, public-safe examples for policy development. Reusable
fixtures and executable tests belong under their accepted
[`fixtures/`](../../fixtures/) and [`tests/`](../../tests/) authority roots,
unless an adopted policy-bundle convention explicitly establishes a different
generated or local-test relationship.

[Back to top](#top)

## Inputs and outputs

### Current inputs

No accepted input contract is bound to either module. The commented examples
mention `input.kind` and `input.evidence_bundle_resolved`, but commented
field names are not a contract and must not be relied upon.

### Required future input posture

Before operational evaluation, an accepted input must be:

- operation-specific and closed to unknown fields;
- bound to a semantic contract and canonical schema;
- explicit about caller, audience, destination, lifecycle/release state,
  rights, consent, sensitivity, and policy version as applicable;
- composed from references and safe classifications rather than copied raw
  payloads;
- deterministic enough to replay, audit, correct, and expire;
- rejected or held when required context is missing, invalid, stale, or
  untrusted.

These are graduation requirements, not claims that such an input exists today.

### Current outputs

Neither module emits a decision instance, reason set, obligation, receipt, or
artifact. The only executable value defined by each module is `deny = false`.

### Required future output posture

An operational evaluator must normalize native policy results into an accepted,
finite decision contract with public-safe reason codes and enforceable
obligations. Decision instances belong with the governed process or release
object they record; they do not become source files in this directory.

[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Current posture |
|---|---|
| Repository visibility | The repository and these source files are publicly readable. Do not place sensitive values, production payloads, credentials, private endpoints, or restricted examples here. |
| Operating exposure | The root registry classifies `policy/` as internal policy authority. Public clients must not read Rego source or internal decision context as their normal path. |
| Mutation | Versioned feature-branch changes with review. Direct default-branch writes, force-push, and history rewrite are outside this boundary. |
| Retention | Durable repository history. Incorrect policy bytes should be corrected or superseded transparently, not erased to hide lineage. |
| Generated state | None established for the three current files. A future generated artifact must name its source, generator, version, command, and synchronized outputs. |
| Runtime cache | **UNKNOWN.** No accepted evaluator or cache binding was found. Any future cache must include policy/input identity and support expiry, correction, and revocation. |

[Back to top](#top)

## UI telemetry trust boundary

The intended protection is broader than a keyword scan:

| Protected class | Required posture before operational emission | Current evidence |
|---|---|---|
| Raw evidence and source payloads | Minimize before serialization; deny any unapproved payload-bearing field; never use telemetry as an evidence carrier. | Fixture-only structural checks; Rego enforcement absent. |
| Prompts, messages, model output, and reasoning | Exclude from event construction, logs, exceptions, receipts, and sinks. | Fixture-only forbidden-key checks; Rego enforcement absent. |
| Restricted coordinates and geometry | Apply accepted sensitivity/generalization rules or deny; prevent reconstruction through identifiers and joins. | Adjacent coordinate stub plus fixture-only absence check; operational enforcement absent. |
| Secrets and access material | Never emit; record only a bounded incident signal that does not echo the value. | General policy, emitter, and incident integration **UNKNOWN**. |
| Denial and existence leakage | Return finite, public-safe reasons without revealing whether protected content exists. | Accepted reason and outward-outcome binding not established for this lane. |
| Unknown fields or unavailable controls | Fail closed, hold, or emit only an explicitly accepted minimal baseline. | Target posture in proposed ADR-0016; no operational implementation established. |

Telemetry remains observability or process memory. It does not become source
truth, an `EvidenceBundle`, a `PolicyDecision`, release approval, or a
`PUBLISHED` artifact merely because it was emitted or retained.

[Back to top](#top)

## Rule source, runtime evaluation, and release

Keep these states separate:

| State | Owning surface | Status for this lane |
|---|---|---|
| Rule source | `policy/ui/` | Two proposed non-enforcing stubs are present. |
| Meaning and input/output contract | [`contracts/`](../../contracts/) | No accepted UI-telemetry policy contract is bound. |
| Machine shape | [`schemas/`](../../schemas/) | No accepted UI-telemetry policy-input schema is bound. |
| Reusable evaluator | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) or an accepted successor | Parent evidence describes a placeholder; operational binding is not established. |
| Governed consumer | [governed APIs](../../apps/governed-api/README.md) and accepted applications | No reviewed consumer was established for these packages. |
| Decision instance or receipt | Governed process/accountability lane | None is emitted here. |
| Release, correction, withdrawal, rollback | [`release/`](../../release/README.md) | Separate authority; no release effect. |
| Public presentation | Released public-safe artifacts through governed interfaces | Direct rule-source access is prohibited for ordinary public clients. |

The minimum safe sequence for future use is:

`accepted input → selected policy bundle → fail-closed evaluation → normalized decision → governed consumer → bounded receipt/replay`

Every arrow is a required integration boundary. Current evidence does not
establish that sequence.

[Back to top](#top)

## Related contracts, architecture, policy, validation, and release

| Surface | Relationship | Authority limit |
|---|---|---|
| [Policy root](../README.md) | Parent authority and child-lane maturity contract | Does not make this lane active. |
| [Telemetry semantic-contract lane](../../contracts/telemetry/README.md) | Describes current telemetry object-family candidates and protected-content constraints | Draft/proposed material is not accepted runtime shape. |
| [Telemetry schema lane](../../schemas/contracts/v1/telemetry/README.md) | Canonical machine-shape home for admitted telemetry profiles | Current profile validation does not establish a UI event schema or policy input. |
| [Telemetry Minimums](../../docs/standards/TELEMETRY_MINIMUMS.md) | Human telemetry safety guidance | Documentation is not enforcement. |
| [UI Telemetry Architecture](../../docs/architecture/ui/TELEMETRY.md) | Draft target architecture for UI telemetry | Several paths and interfaces remain proposed; verify before implementation. |
| [ADR-0016](../../docs/adr/ADR-0016-telemetry-redaction-posture.md) | Proposed redaction, minimization, sink, receipt, and correction posture | Decision status remains `proposed`. |
| [Telemetry policy sibling](../telemetry/README.md) | Current adjacent lane containing the restricted-coordinate stub | Boundary ownership and consolidation remain unresolved. |
| [Telemetry safety validator](../../tools/validators/validate_telemetry_safety.py) | Named general validation surface | Placeholder only; raises `NotImplementedError`. |
| [Telemetry readiness workflow](../../.github/workflows/telemetry-policy.yml) | Bounded fixture checks and explicit operational holds | Does not run OPA against these modules or prove production safety. |
| [Telemetry receipt lane](../../data/receipts/telemetry/README.md) | Accountability home for future accepted telemetry receipt instances | No operational receipt instance is established by this README. |
| [Release root](../../release/README.md) | Owns release, correction, withdrawal, and rollback decisions | Policy cannot self-release or self-publish. |

[Back to top](#top)

## Validation coverage and limits

| Check | Actual coverage | Explicit limitation |
|---|---|---|
| Direct-child reconciliation | Compares this README's map with the complete tracked `policy/ui/` tree at the evidence base. | Proves names and depth only. |
| Markdown structure review | Checks one H1, heading order, fenced blocks, tables, alerts, anchors, and final newline. | Presentation correctness is not policy correctness. |
| Bounded local link check | Resolves repository-relative file and directory targets without requesting external URLs. | Does not prove authority, adoption, runtime behavior, or external availability. |
| `telemetry-policy / no-raw-evidence` | Runs deterministic tests for admitted fixture-only profiles, rejects raw-payload-bearing keys, verifies the raw-evidence stub/validator hold, and scans selected runtime roots for surfaced telemetry code. | Does not evaluate an operational event, general policy, emitter, sink, or receipt. |
| `telemetry-policy / no-prompts` | Rejects prompt-, message-, output-, and reasoning-bearing keys in admitted fixture-only profiles and verifies the prompt stub remains a placeholder. | Does not prove source-side minimization or runtime redaction. |
| `telemetry-policy / no-restricted-coords` | Rejects coordinate- and geometry-bearing keys in admitted fixture-only profiles and verifies the adjacent coordinate stub. | Does not prove sensitivity resolution, generalization, or operational enforcement. |
| Parent policy checks | Preserve selected bounded policy profiles and structural trust boundaries. | They do not establish this lane's input, bundle, evaluator, consumer, or decision flow. |

> [!NOTE]
> A green `telemetry-policy` run proves the documented hold is intact and the
> admitted synthetic profiles satisfy their bounded absence checks. It must not
> be summarized as “UI telemetry policy passes” or “telemetry is safe.”

Any behavioral change to a Rego module requires, at minimum, accepted input and
outcome semantics, positive and negative synthetic fixtures, native Rego
evaluation, timeout/error behavior, bundle/query compatibility checks, consumer
tests, and protected-value non-echo tests. Those checks are not supplied by this
documentation-only update.

[Back to top](#top)

## Authoring and review contract

When changing this directory:

1. pin `main`, the target blob, package names, parent policy evidence, and any
   consumer or bundle references;
2. distinguish documentation, policy behavior, contract/schema, and runtime
   changes—do not hide one inside another;
3. use synthetic public-safe fixtures only;
4. define finite allow, deny, hold, restrict, abstain, and error behavior as
   applicable, including missing or malformed input;
5. keep reasons and obligations free of protected-value echo;
6. add native positive and negative evaluation before claiming enforcement;
7. verify bundle selection and every known consumer at the exact head;
8. preserve public-client separation from internal rule source and decision
   context;
9. record compatibility, correction, rollback, and any package/query migration;
10. request policy, UI/runtime, security/privacy, and sensitivity review when
    behavior changes.

Documentation-only edits must preserve the exact status of each rule. They may
clarify a hold; they may not convert a placeholder into an accepted control by
prose.

[Back to top](#top)

## Correction and rollback

### Documentation correction

Before merge, close or abandon the draft pull request and its feature branch.
After merge, revert the documentation commit or restore prior blob
`eb88e0b34c6c26ac90e046af44843661ede41a51` through a reviewable correction
pull request. Do not rewrite shared history.

### Policy correction

If a module later proves unsafe:

1. disable or hold the affected evaluator or consumer through its governed kill
   switch;
2. preserve the incorrect rule and decision lineage;
3. issue a reviewed forward fix or transparent revert;
4. supersede affected decision/receipt records rather than silently editing
   them;
5. invalidate policy caches and re-evaluate bounded affected operations;
6. execute incident, correction, withdrawal, or release rollback where
   protected content or public reliance is involved.

A Git revert restores repository bytes. It does not by itself remove telemetry
from sinks, backups, dashboards, exports, alerts, caches, or public summaries.
No such operational reliance is established today; if it is introduced, its
retention and correction path must be documented before activation.

[Back to top](#top)

## Open verification register

| ID | Unresolved item | Current posture |
|---|---|---|
| UI-POL-001 | Accepted local scope ID, policy steward, UI/runtime owner, security/privacy reviewer, and independent approver | **NEEDS VERIFICATION** |
| UI-POL-002 | Whether `policy/ui/` and `policy/telemetry/` are intentionally separate policy families, and which lane owns cross-surface telemetry controls | **NEEDS DIRECTORY AND ARCHITECTURE REVIEW** |
| UI-POL-003 | Accepted policy input contract, canonical schema, native outcome vocabulary, public-safe reason codes, obligations, and decision normalization | **UNKNOWN / NEEDS DECISION** |
| UI-POL-004 | Fail-closed replacements for both `default deny := false` stubs, including malformed-input and unavailable-control behavior | **HOLD — separate policy implementation required** |
| UI-POL-005 | Native Rego tests, deterministic valid/invalid fixtures, mutation coverage, package/query compatibility, and non-echo assertions | **NOT ESTABLISHED** |
| UI-POL-006 | Accepted bundle manifest, selector, evaluator, signature/provenance, cache identity, replay, expiry, and correction behavior | **UNKNOWN** |
| UI-POL-007 | Complete UI producer, SDK, emitter, queue, sink, dashboard, alert, export, archive, and third-party inventory | **NEEDS VERIFICATION** |
| UI-POL-008 | Governed API or runtime consumer binding and a representative producer-to-sink fail-closed test | **NOT ESTABLISHED** |
| UI-POL-009 | Retention, deletion, legal hold, access control, incident response, revocation, and downstream cache/export correction | **UNKNOWN** |
| UI-POL-010 | Reconciliation of draft UI Telemetry Architecture paths and interfaces with current contracts, schemas, code, and routes | **NEEDS VERIFICATION** |
| UI-POL-011 | Acceptance, rejection, or supersession of ADR-0016 and the resulting implementation/graduation sequence | **PROPOSED DECISION** |
| UI-POL-012 | Required hosted checks, ruleset coupling, code-owner review, and independent policy/security approval | **UNKNOWN** |

[Back to top](#top)

## Last evidence review and triggers

**Evidence review:** 2026-08-12 against
`main@35c58cb1c6cbf09567c17f9ff9776b2086c8d0bb`.

Re-review this README when:

- either Rego module, package name, input, outcome, obligation, or default
  changes;
- a manifest, native test, fixture, validator, evaluator, consumer, emitter,
  sink, receipt, or cache is added or bound;
- ADR-0016 is accepted, rejected, or superseded;
- `policy/ui/` and `policy/telemetry/` ownership is reconciled;
- telemetry contracts, schemas, architecture, minimums, retention, access, or
  incident posture changes;
- CODEOWNERS, workflow coverage, required checks, or repository controls change;
- a telemetry exposure, correction, withdrawal, rollback, or policy incident
  occurs.

## Changelog

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-08-12 | Replaced the 40-byte greenfield stub in place with a repository-grounded `BOUNDARY_COMPACT` contract; preserved the H1; documented the exact two-file rule inventory, non-enforcing defaults, workflow hold, authority and exposure boundaries, current validation limits, authoring discipline, correction/rollback path, and unresolved `ui/` versus `telemetry/` ownership. No policy behavior changed. |

[Back to top](#top)
