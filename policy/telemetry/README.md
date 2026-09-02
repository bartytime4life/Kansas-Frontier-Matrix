<a id="top"></a>

# policy :: telemetry

> **One-line purpose.** `policy/telemetry/` is the current repository boundary
> for proposed policy source intended to keep exact or reconstructable
> restricted locations out of telemetry. It inherits authority from
> [`policy/`](../README.md); it does not define telemetry meaning or shape,
> implement a policy evaluator, emit telemetry, approve release, or publish
> data.

> [!IMPORTANT]
> **Safe current conclusion:** this directory contains one `PROPOSED`
> greenfield Rego stub and this README. The module defines
> `default deny := false`, contains no operative denial rule, has no native Rego
> test beside it, and is not established as part of an accepted bundle or
> runtime consumer. The
> [`telemetry-policy`](../../.github/workflows/telemetry-policy.yml) workflow
> verifies that limitation, checks four admitted synthetic telemetry profiles
> for coordinate-bearing keys, and keeps operational enforcement on
> `WORKFLOW_HOLD`.

**Operational caution.** A filename, package name, comment, coordinate-free
fixture, workflow pass, or policy-shaped file is not protection by itself.
Until accepted inputs, fail-closed rules, spatial classifications, native tests,
bundle selection, an evaluator, and a governed consumer are bound together,
callers must not rely on this directory to remove, generalize, suppress, or
deny a location.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Rule inventory](#current-rule-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Trust boundary](#restricted-location-telemetry-trust-boundary) · [Evaluation](#rule-source-runtime-evaluation-and-release) · [Related evidence](#related-contracts-architecture-policy-validation-and-release) · [Validation](#validation-coverage-and-limits) · [Authoring](#authoring-and-review-contract) · [Correction](#correction-and-rollback) · [Open verification](#open-verification-register)

## Purpose

`policy/telemetry/` documents and contains the repository's current candidate
rule source for one narrow telemetry exclusion: exact or reconstructable
restricted locations must not cross a telemetry boundary.

Its audience is policy authors, telemetry maintainers, sensitivity and privacy
reviewers, runtime integrators, and release reviewers who need to understand
what the current source does—and, more importantly, what it does not do.

The intended protection is broader than removing fields named `lat` or `lon`.
Depending on an accepted sensitivity and generalization profile, restricted
location can also be reconstructed from geometry, bounding boxes, WKT, tile or
grid identifiers, geohashes, station or site identifiers, route segments,
parcel identifiers, viewport centers, camera traces, small-cohort joins, or
timing sequences.

Current tracked bytes do not implement that posture. The only Rego module is a
non-enforcing scaffold. Its commented example mentions `input.kind` and
`input.evidence_bundle_resolved`, but comments and illustrative field names are
not an accepted input contract.

Related telemetry exclusions are split across the adjacent
[`policy/ui/`](../ui/README.md) lane, which contains separate raw-evidence and
prompt-content stubs. Whether this split is the intended long-term policy-family
boundary remains **NEEDS VERIFICATION**.

This README describes the boundary; it does not activate the module, repair its
non-denying default, accept a telemetry policy contract, or authorize
operational telemetry.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent authority | [`policy/`](../README.md) is KFM's canonical source root for normative allow, deny, hold, restrict, and abstain rules. |
| Directory profile | `BOUNDARY_COMPACT`: this lane is policy-bearing and sits at a telemetry, sensitivity, and spatial-exposure boundary. |
| Placement basis | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy source from contracts and schemas and define the local README contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as a canonical, internal, versioned, durable policy-rule root and prohibits data instances, release decisions, and schemas. The registry projects adopted governance; it does not create authority. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove stewardship, required review, independent approval, or policy acceptance. |
| Local owner | **NEEDS VERIFICATION.** No accepted telemetry-policy steward, sensitivity steward, spatial-privacy reviewer, or independent security/privacy approver was established by the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted scope identifier for this directory was found; this README does not invent one. |
| Current evidence base | `main@0358516e7deaefaf3cbc8a2d7752ff174e1937e2`; target prior blob `ed676a82e181a80bd9934cfe8fd8f0cac85b99c3`. |
| Release authority | None. Policy evaluation may eventually supply one input to a release decision, but [`release/`](../../release/README.md) owns release, correction, withdrawal, and rollback decisions. |
| Publication authority | None. A policy result, workflow, commit, pull request, telemetry event, log, metric, trace, dashboard, or receipt is not publication. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Target README | 47-byte greenfield stub with the existing H1 and no boundary contract | This update replaces that stub in place; it does not change policy behavior. |
| Directory inventory | Exactly this README and one Rego file | No manifest, data document, native test module, fixture, generated output, evaluator, or runtime code is tracked here. |
| Restricted-coordinate module | [`no_restricted_coords.rego`](./no_restricted_coords.rego) is marked `PROPOSED greenfield stub` | It defines `deny` as `false` and executes no denial rule. |
| Commented example | The module contains a commented `deny[reason]` sketch | The comment neither validates an input nor produces a denial, reason, obligation, or decision. |
| General safety validator | [`validate_telemetry_safety.py`](../../tools/validators/validate_telemetry_safety.py) raises `NotImplementedError("Greenfield placeholder")` | No general telemetry-safety validator is implemented. |
| Readiness workflow | [`telemetry-policy / no-restricted-coords`](../../.github/workflows/telemetry-policy.yml) checks four admitted fixture-only profiles for `lat`, `lon`, `latitude`, `longitude`, `coordinates`, `geometry`, `bbox`, and `wkt` keys and asserts this module's stub state | It proves a bounded repository-local absence check and records `WORKFLOW_HOLD`; it does not run OPA, inspect an operational event, apply generalization, or evaluate indirect reconstruction risk. |
| Telemetry contracts and schemas | Four fixture-first telemetry profiles have contracts, schemas, validators, and synthetic tests | Those profiles do not establish a policy-input schema, accepted telemetry-event envelope, or runtime binding for this module. |
| Architecture and decision posture | [UI Telemetry Architecture](../../docs/architecture/ui/TELEMETRY.md) is draft; [ADR-0016](../../docs/adr/ADR-0016-telemetry-redaction-posture.md) remains proposed | Their location-protection posture is design and decision evidence, not accepted runtime behavior. ADR-0016's repository-evidence snapshot predates the current fixture-first profiles. |
| Evaluator and consumer | No accepted bundle selector, general evaluator, producer binding, emitter, sink, or production consumer was established by the reviewed evidence | Operational enforcement remains unproven and must fail closed outside any explicitly accepted baseline. |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned repository bytes, complete tree, workflow, or adopted decision. |
| **PROPOSED** | A candidate posture or future implementation that is not current authority. |
| **NEEDS VERIFICATION** | A concrete check or decision is still required. |
| **UNKNOWN** | The reviewed evidence is insufficient to support a stronger claim. |

[Back to top](#top)

## Current direct-child map

This map is verified from the complete tracked tree at the evidence base. It
shows `policy/telemetry/` and direct children only; presence does not establish
activation or maturity.

```text
policy/telemetry/
├── README.md
└── no_restricted_coords.rego
```

Neither child is marked as generated, mirrored, localized, or converted in its
tracked bytes. Any future generator or bundle relationship must identify its
canonical source and deterministic reproduction path before this README treats
it as established.

[Back to top](#top)

## Current rule inventory

| Module | Package | Executable rule state | Current effect |
|---|---|---|---|
| [`no_restricted_coords.rego`](./no_restricted_coords.rego) | `kfm.no_restricted_coords` | `default deny := false`; no operative rule | Does not deny an input. Its commented sketch is illustrative only. |

The package name is a current machine identifier. It does not establish an
accepted bundle namespace, import path, query contract, spatial classification,
decision shape, or consumer. Renaming the package would be a policy
compatibility change and requires consumer discovery, native tests, migration
evidence, and a separate review.

[Back to top](#top)

## What belongs here

Subject to accepted contracts and review, this boundary may contain:

- cross-surface telemetry admissibility rules for restricted coordinates,
  geometry, harmful precision, or reconstruction-enabling spatial identifiers;
- reviewed spatial allowlists, sensitivity-class bindings, and obligations to
  deny, suppress, aggregate, or generalize telemetry before emission when
  their semantics and machine shape are owned by the correct contract and
  schema roots;
- policy-local documentation for package identities, supported operations,
  finite outcomes, public-safe reasons, obligations, failure behavior, and
  supersession;
- an accepted manifest or bundle-local metadata only if
  [`policy/`](../README.md) and the repository's bundle authority designate
  this lane as its canonical home;
- source-level compatibility and migration notes for this policy family.

General telemetry semantics, event shape, observability minimums, source data,
domain sensitivity facts, and release state do not become local authority merely
because this lane evaluates them.

[Back to top](#top)

## What is prohibited

The following do not belong in `policy/telemetry/`:

- telemetry events, logs, traces, metrics, profiles, dashboards, alerts, queues,
  sink payloads, crash reports, or operational receipt instances;
- real restricted coordinates, exact geometry, sensitive site identifiers,
  private routes, parcels, viewport traces, protected joins, or production
  telemetry used as policy examples;
- raw evidence, source payloads, prompts, messages, model output, reasoning
  content, secrets, credentials, tokens, private URLs, or crash locals;
- semantic contracts, canonical schemas, generated types, policy decisions,
  sensitivity determinations, or source-rights records;
- producers, SDKs, redactors, exporters, collectors, evaluator code, sink
  configuration, dashboards, or deployable runtime logic;
- release decisions, publication records, proofs, catalogs, lifecycle data,
  correction notices, withdrawal notices, or rollback cards;
- private, production, unclear-rights, or harmful-precision data.

Use synthetic, minimal, public-safe examples for policy development. Reusable
fixtures and executable tests belong under their accepted
[`fixtures/`](../../fixtures/) and [`tests/`](../../tests/) authority roots,
unless an adopted policy-bundle convention explicitly establishes a different
engine-native co-location profile.

[Back to top](#top)

## Inputs and outputs

### Current inputs

No accepted input contract is bound to this module. The commented example
mentions `input.kind` and `input.evidence_bundle_resolved`, but commented field
names are not a contract and must not be relied upon.

### Required future input posture

Before operational evaluation, an accepted input must be:

- operation-specific and closed to unknown fields;
- bound to a semantic contract and canonical schema;
- explicit about producer, caller, audience, destination, event family,
  lifecycle/release state, rights, consent, sensitivity, and policy version;
- explicit about requested precision, spatial classification, applicable
  generalization profile, and reconstruction risk;
- composed from governed references and safe classifications rather than copied
  telemetry, evidence, or protected geometry where practical;
- assembled at an authorized boundary without hidden fetches;
- deterministic enough to replay, audit, correct, revoke, and expire;
- denied, held, or errored when required context is missing, invalid, stale,
  conflicted, or untrusted.

These are graduation requirements, not claims that such an input exists today.

### Current outputs

The module emits no decision instance, safe alternative, reason set, obligation,
receipt, or artifact. Its only executable value is `deny = false`.

### Required future output posture

An operational evaluator must normalize native policy results into an accepted,
finite decision contract with public-safe reason codes and enforceable
obligations. A generalization or suppression obligation must name an accepted
profile without echoing the protected value. Decision instances belong with the
governed process or release object they record; they do not become source files
in this directory.

[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Current posture |
|---|---|
| Repository visibility | The repository and these source files are publicly readable. Do not place sensitive coordinates, production payloads, credentials, private endpoints, restricted identifiers, or reconstruction-enabling examples here. |
| Operating exposure | The root registry classifies `policy/` as internal policy authority. Public clients must not read Rego source or internal decision context as their normal path. |
| Mutation | Versioned feature-branch changes with review. Direct default-branch writes, force-push, and history rewrite are outside this boundary. |
| Retention | Durable repository history. Incorrect policy bytes should be corrected or superseded transparently, not erased to hide lineage. |
| Generated state | None established for the two current files. A future generated artifact must name its source, generator, version, command, and synchronized outputs. |
| Runtime cache | **UNKNOWN.** No accepted evaluator or cache binding was found. Any future cache must include policy, input, audience, spatial-profile, expiry, and correction identity and support revocation. |
| Telemetry storage | Outside this source boundary. Any future sink must define access, retention, deletion, incident, correction, export, and backup behavior before activation. |

[Back to top](#top)

## Restricted-location telemetry trust boundary

The intended protection covers direct and indirect spatial disclosure:

| Location class | Required posture before operational emission | Current evidence |
|---|---|---|
| Exact coordinates | Replace with an accepted public-safe region, grid, category, or band, or deny the event. | Fixture-only key absence check; Rego enforcement absent. |
| Geometry, bounding boxes, and WKT | Generalize or suppress through an accepted sensitivity-aware profile before serialization; never rely on display hiding. | Fixture-only key absence check; no operational redactor established. |
| Tile, grid, geohash, station, site, parcel, or route identifiers | Treat as location-bearing when they can reconstruct a protected place; use audience- and profile-specific allowlists. | Not evaluated by the current forbidden-key set. |
| Viewports, camera traces, timing, and interaction sequences | Assess composition and temporal reconstruction risk, not fields in isolation. | No accepted evaluation or negative fixture matrix established. |
| Small cohorts and joins | Propagate the stricter sensitivity and deny or aggregate when a join reveals a location or protected existence. | General policy posture documented; lane-specific implementation absent. |
| Denial and existence leakage | Return finite, public-safe reasons without echoing the coordinate, identifier, cohort, or fact being protected. | Accepted reason and outward-outcome binding not established for this lane. |
| Unknown profile or unavailable controls | Fail closed, hold, or emit only an explicitly accepted minimal baseline. | Target posture in proposed ADR-0016; no operational implementation established. |

Telemetry remains observability or process memory. It does not become source
truth, an `EvidenceBundle`, a `PolicyDecision`, release approval, or a
`PUBLISHED` artifact merely because it was emitted, aggregated, retained, or
displayed.

[Back to top](#top)

## Rule source, runtime evaluation, and release

Keep these states separate:

| State | Owning surface | Status for this lane |
|---|---|---|
| Rule source | `policy/telemetry/` | One proposed non-enforcing stub is present. |
| Meaning and input/output contract | [`contracts/telemetry/`](../../contracts/telemetry/README.md) and other accepted contract families | Four fixture-first telemetry profiles exist; no accepted input/output contract is bound to this module. |
| Machine shape | [`schemas/contracts/v1/telemetry/`](../../schemas/contracts/v1/telemetry/README.md) | Four profile schemas exist; no telemetry-event or policy-input schema is bound to this rule. |
| Sensitivity and generalization context | [`policy/sensitivity/`](../sensitivity/README.md) plus accepted contracts and schemas | No accepted spatial-profile binding to this module was established. |
| Reusable evaluator | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) or an accepted successor | The package is documented as a placeholder; operational binding is not established. |
| Governed producer and consumer | Accepted applications, runtime, pipelines, and [governed APIs](../../apps/governed-api/README.md) | No reviewed producer-to-policy-to-sink chain was established for this package. |
| Decision instance or receipt | Governed process/accountability lane | None is emitted here. |
| Release, correction, withdrawal, rollback | [`release/`](../../release/README.md) | Separate authority; no release effect. |
| Public presentation | Released public-safe artifacts through governed interfaces | Direct rule-source or telemetry-sink access is prohibited for ordinary public clients. |

The minimum safe sequence for future use is:

`accepted event context → sensitivity/profile resolution → selected policy bundle → fail-closed evaluation → enforced deny/generalize/suppress obligation → governed sink → bounded receipt/replay`

Every arrow is a required integration boundary. Current evidence does not
establish that sequence.

[Back to top](#top)

## Related contracts, architecture, policy, validation, and release

| Surface | Relationship | Authority limit |
|---|---|---|
| [Policy root](../README.md) | Parent authority and child-lane maturity contract | Does not make this lane active. |
| [UI policy sibling](../ui/README.md) | Contains the adjacent raw-evidence and prompt-content telemetry stubs | Cross-surface telemetry ownership and bundle composition remain unresolved. |
| [Telemetry semantic-contract lane](../../contracts/telemetry/README.md) | Defines candidate telemetry meanings and four current fixture-first profiles | Draft/proposed contracts are not this rule's accepted input or runtime authority. |
| [Telemetry schema lane](../../schemas/contracts/v1/telemetry/README.md) | Machine-shape home for four admitted telemetry profiles | Shape validation does not establish policy admissibility or a telemetry-event schema. |
| [Telemetry fixtures](../../fixtures/contracts/v1/telemetry/) | Synthetic cases for the four admitted profiles | Fixture content is not operational telemetry, policy input, evidence truth, or release authority. |
| [Focused telemetry validators](../../tools/validators/telemetry/README.md) | Validate inactive OpenLineage, remote-sensing lineage, and map-build sustainability profiles | They do not evaluate this Rego module or authorize runtime use. |
| [General telemetry safety validator](../../tools/validators/validate_telemetry_safety.py) | Named general safety surface | Placeholder only; raises `NotImplementedError`. |
| [Telemetry Minimums](../../docs/standards/TELEMETRY_MINIMUMS.md) | Draft human telemetry and sensitivity guidance | Documentation is not enforcement. |
| [UI Telemetry Architecture](../../docs/architecture/ui/TELEMETRY.md) | Draft target architecture for event fields, policy gates, and location exclusions | Several paths and interfaces remain proposed or absent; verify before implementation. |
| [ADR-0016](../../docs/adr/ADR-0016-telemetry-redaction-posture.md) | Proposed minimization, spatial redaction, sink, receipt, correction, and rollback posture | Decision status remains `proposed`; its implementation snapshot is older than current fixture profiles. |
| [Telemetry readiness workflow](../../.github/workflows/telemetry-policy.yml) | Bounded fixture checks and explicit operational holds | Does not run OPA against this module, model indirect reconstruction, or prove production safety. |
| [Telemetry receipt lane](../../data/receipts/telemetry/README.md) | Accountability home for future accepted telemetry receipt instances | No operational receipt is emitted by this policy lane. |
| [Release root](../../release/README.md) | Owns release, correction, withdrawal, and rollback decisions | Policy cannot self-release or self-publish. |

[Back to top](#top)

## Validation coverage and limits

| Check | Actual coverage | Explicit limitation |
|---|---|---|
| Direct-child reconciliation | Compares this README's map with the complete tracked `policy/telemetry/` tree at the evidence base. | Proves names and depth only. |
| Markdown structure review | Checks one H1, heading order, fenced blocks, tables, alerts, anchors, and final newline. | Presentation correctness is not policy correctness. |
| Bounded local link check | Resolves repository-relative file and directory targets without requesting external URLs. | Does not prove authority, adoption, runtime behavior, or external availability. |
| `telemetry-policy / no-restricted-coords` | Verifies the stub markers and rejects eight direct coordinate/geometry key names in four admitted synthetic profile trees. | Does not run OPA, inspect strings or indirect identifiers, resolve sensitivity, apply generalization, or evaluate an operational event. |
| `telemetry-policy / no-raw-evidence` and `no-prompts` | Exercise related forbidden-key sets, fixture-profile validators, general-validator hold, selected implementation scans, and receipt-instance absence. | Do not prove source-side minimization, runtime redaction, or this module's behavior. |
| Focused telemetry profile tests and validators | Prove declared shape, polarity, deterministic identity, and no-network behavior for bounded inactive profiles. | Do not establish a general telemetry event, producer, policy evaluator, sink, or release gate. |
| Parent policy checks | Preserve selected bounded policy profiles and structural trust boundaries. | They do not establish this lane's input, bundle, evaluator, consumer, or decision flow. |

> [!NOTE]
> A green `telemetry-policy` run proves the documented hold is intact and the
> admitted synthetic profiles satisfy bounded absence checks. It must not be
> summarized as “restricted coordinates are blocked” or “telemetry is safe.”

Any behavioral change to the Rego module requires, at minimum, accepted input
and outcome semantics, positive and negative synthetic fixtures, native Rego
evaluation, indirect-reconstruction cases, timeout/error behavior,
bundle/query compatibility checks, producer and consumer tests, and
protected-value non-echo assertions. Those checks are not supplied by this
documentation-only update.

[Back to top](#top)

## Authoring and review contract

When changing this directory:

1. pin `main`, the target blob, package name, parent policy evidence, and every
   known bundle, producer, consumer, or spatial-profile reference;
2. distinguish documentation, policy behavior, contract/schema, sensitivity,
   and runtime changes—do not hide one inside another;
3. use synthetic public-safe fixtures only; never copy a real restricted
   coordinate or reconstruction-enabling identifier into Git;
4. define direct and indirect location classes, finite outcomes, missing-input
   behavior, and accepted generalization or suppression obligations;
5. keep reasons, logs, receipts, and test output free of protected-value and
   protected-existence echo;
6. add native positive and negative evaluation, including unknown fields,
   malformed input, joins, identifiers, and unavailable-control cases, before
   claiming enforcement;
7. verify bundle selection, package/query compatibility, and every known
   producer and consumer at the exact head;
8. preserve public-client separation from internal policy source, telemetry
   sinks, and decision context;
9. record effective time, supersession, cache invalidation, correction,
   revocation, retention, deletion, and rollback;
10. request policy, sensitivity, spatial-privacy, security/privacy,
    producer/runtime, and release review when behavior changes.

Documentation-only edits must preserve the exact status of the rule. They may
clarify a hold; they may not convert a placeholder or coordinate-free fixture
into an accepted control by prose.

[Back to top](#top)

## Correction and rollback

### Documentation correction

Before merge, close or abandon the draft pull request and its feature branch.
After merge, revert the documentation commit or restore prior blob
`ed676a82e181a80bd9934cfe8fd8f0cac85b99c3` through a reviewable correction
pull request. Do not rewrite shared history.

### Policy and exposure correction

If a module, redactor, producer, consumer, or sink later proves unsafe:

1. disable or hold the affected emission path through its governed kill switch;
2. preserve the incorrect rule, decision, receipt, and release lineage;
3. restrict or quarantine affected telemetry without copying protected values
   into public incident text;
4. issue a reviewed forward fix or transparent revert;
5. supersede affected decisions and receipts rather than silently editing them;
6. invalidate policy and telemetry caches and re-evaluate bounded affected
   operations;
7. rotate identifiers or access material where linkability or exposure requires
   it; and
8. execute incident, deletion, correction, withdrawal, or release rollback where
   protected content or public reliance is involved.

A Git revert restores repository bytes. It does not by itself remove telemetry
from queues, sinks, backups, dashboards, exports, alerts, caches, or public
summaries. No such operational reliance is established today; if it is
introduced, its retention and correction path must be documented before
activation.

[Back to top](#top)

## Open verification register

| ID | Unresolved item | Current posture |
|---|---|---|
| TEL-POL-001 | Accepted local scope ID, telemetry-policy steward, sensitivity steward, spatial-privacy reviewer, security/privacy reviewer, and independent approver | **NEEDS VERIFICATION** |
| TEL-POL-002 | Whether `policy/telemetry/` and `policy/ui/` are intentionally separate policy families, and which lane owns cross-surface telemetry controls and bundle composition | **NEEDS DIRECTORY AND ARCHITECTURE REVIEW** |
| TEL-POL-003 | Accepted policy input contract, canonical schema, native outcome vocabulary, public-safe reason codes, obligations, and decision normalization | **UNKNOWN / NEEDS DECISION** |
| TEL-POL-004 | A fail-closed replacement for `default deny := false`, including malformed-input, unknown-field, policy-error, and unavailable-control behavior | **HOLD — separate policy implementation required** |
| TEL-POL-005 | Accepted spatial classification and generalization profiles covering coordinates, geometry, indirect identifiers, joins, viewports, camera paths, timing, and existence leakage | **NOT ESTABLISHED** |
| TEL-POL-006 | Native Rego tests, deterministic valid/invalid fixtures, mutation coverage, indirect-reconstruction cases, package/query compatibility, and non-echo assertions | **NOT ESTABLISHED** |
| TEL-POL-007 | Accepted bundle manifest, selector, evaluator, signature/provenance, cache identity, replay, expiry, correction, and revocation behavior | **UNKNOWN** |
| TEL-POL-008 | Complete producer, SDK, redactor, emitter, queue, exporter, collector, sink, dashboard, alert, archive, backup, and third-party inventory | **NEEDS VERIFICATION** |
| TEL-POL-009 | Governed producer-to-policy-to-sink binding and representative fail-closed integration tests | **NOT ESTABLISHED** |
| TEL-POL-010 | Whether the current eight-key fixture scan is a permanent baseline, a temporary readiness check, or one layer in a broader spatial disclosure detector | **NEEDS DECISION** |
| TEL-POL-011 | Retention, deletion, legal hold, access control, incident response, consent/rights revocation, and downstream cache/export correction | **UNKNOWN** |
| TEL-POL-012 | Reconciliation of draft UI Telemetry Architecture paths and interfaces with current contracts, four admitted schemas, code, routes, and runtime evidence | **NEEDS VERIFICATION** |
| TEL-POL-013 | Acceptance, rejection, or supersession of ADR-0016 and the resulting implementation and graduation sequence | **PROPOSED DECISION** |
| TEL-POL-014 | Required hosted checks, ruleset coupling, code-owner review, and independent policy/sensitivity/security approval | **UNKNOWN** |

[Back to top](#top)

## Last evidence review and triggers

**Evidence review:** 2026-08-12 against
`main@0358516e7deaefaf3cbc8a2d7752ff174e1937e2`.

Re-review this README when:

- the Rego module, package name, input, outcome, reason, obligation, default, or
  spatial classification changes;
- a manifest, native test, fixture, validator, evaluator, producer, consumer,
  redactor, emitter, collector, sink, receipt, dashboard, or cache is added or
  bound;
- ADR-0016 is accepted, rejected, or superseded;
- `policy/telemetry/` and `policy/ui/` ownership is reconciled;
- telemetry contracts, schemas, architecture, minimums, sensitivity profiles,
  retention, access, incident, or deletion posture changes;
- CODEOWNERS, workflow coverage, required checks, or repository controls change;
- a telemetry exposure, correction, withdrawal, rollback, privacy, or policy
  incident occurs.

## Changelog

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-08-12 | Replaced the 47-byte greenfield stub in place with a repository-grounded `BOUNDARY_COMPACT` contract; preserved the H1; documented the exact one-file rule inventory, non-enforcing default, eight-key fixture scan, workflow hold, direct and indirect spatial-exposure boundaries, current validation limits, authoring discipline, correction/rollback path, and unresolved `telemetry/` versus `ui/` ownership. No policy behavior changed. |

[Back to top](#top)
