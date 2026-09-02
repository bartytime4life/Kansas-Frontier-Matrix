<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/layers
title: policy/layers/ — Layer Admissibility and Public-Exposure Policy Boundary
type: readme
version: v0.1
status: draft; BOUNDARY_COMPACT; repository-grounded; proposed-inactive; no-op-rule-stub; candidate-validation-implemented; runtime-admission-fixture-only; evaluator-unbound; non-runtime; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ changes to @bartytime4life; no accepted layer-policy steward, bundle authority, or independent release authority was established
created: 2026-08-10
updated: 2026-08-13
policy_label: public; policy; layers; map; admissibility; rights-aware; sensitivity-aware; release-aware; fail-closed-target; proposed-inactive; non-release; non-publication
current_path: policy/layers/README.md
owning_root: policy/
responsibility: Define the local policy-source boundary for operation-specific layer admissibility and public exposure without defining LayerManifest meaning or shape, storing layer instances, loading map sources, executing policy, approving release, or publishing artifacts.
base_commit: e6de606175bb1d352c00000486808f2e7e0f7b2f
prior_blob: eaea3cd5a580ab2899059ac88f07e204e70e5da2
prior_tree: c011b4a5c2dbb8425727b91cc6d0f0a61cc13247
truth_posture: CONFIRMED accepted placement under policy/, exact two-file local tree, one 356-byte proposed Rego stub with default deny false and no operative rule body, no local native test or bundle/evaluator/consumer binding, separate dual-profile LayerManifest candidate validation with 4 valid and 12 invalid fixtures and 13 unit-test methods, separate fixture-only runtime-admission projection with 13 cases and 3 test blocks, abstain-only governed /layers route, empty PROPOSED policy-gate register, and one separately governed proposed-inactive release-gate lane / PROPOSED BOUNDARY_COMPACT contract and future fail-closed layer-admissibility authoring posture / CONFLICTED or unresolved ownership across policy/layers, schema-declared policy/data, generic policy/runtime, domain-specific policy, release compatibility surfaces, and overlapping LayerManifest schema homes / NEEDS VERIFICATION accepted local scope ID, steward assignments, rule inputs and outcomes, PolicyDecision family and normalization, bundle and evaluator binding, native tests, governed consumers, required-check enforcement, reference and signature resolution, correction propagation, release integration, and production operation
related:
  - ../README.md
  - ../data/README.md
  - ../runtime/README.md
  - ../release/README.md
  - ../rego/release_gate_v1.rego
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/ui/LAYERING.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/policy_gate_register.yaml
  - ../../contracts/data/layer_manifest.md
  - ../../contracts/runtime/layer_manifest_admission.md
  - ../../contracts/release/layer_manifest.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../schemas/contracts/v1/runtime/layer_manifest.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../fixtures/data/layer_manifest/README.md
  - ../../fixtures/runtime/layer_manifest_admission/cases.json
  - ../../tools/validators/data/validate_layer_manifest.py
  - ../../tests/validators/test_validate_layer_manifest.py
  - ../../release/manifests/layers/README.md
  - ../../apps/governed-api/src/governed_api/routes/layers.py
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/layer-manifest.yml
  - ../../.github/workflows/layer-manifest-admission.yml
tags: [kfm, policy, layers, layer-manifest, maplibre, public-exposure, rights, sensitivity, evidence, review, release, correction, rollback, fail-closed]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: layers

`policy/layers/` is KFM's local policy-source boundary for deciding whether a
specific layer operation is admissible for a declared caller, purpose,
audience, representation, and point in time. It inherits the authority and
limitations of [`policy/`](../README.md).

> [!IMPORTANT]
> **Safe current conclusion:** this lane is a greenfield bundle stub and is
> inactive. Its only Rego module declares `default deny := false`, has no
> operative rule body, reads no inputs, emits no reason or obligation, and is
> not bound to a bundle, evaluator, decision emitter, or governed consumer.
> Separate LayerManifest and runtime-admission profiles provide deterministic
> fixture-only candidate checks; they do not activate this policy lane.

> [!CAUTION]
> [`released_only_for_public.rego`](./released_only_for_public.rego) currently
> denies nothing by static inspection. The filename, package name,
> `policy/layers/` path, commented example, schema-valid manifest, candidate
> `PASS`, runtime-admission `PASS`, green workflow, map preview, or released-looking
> URL must never be interpreted as permission to render, query, export, cache,
> register, release, or publish a layer.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) ·
[Status](#current-status-and-evidence) · [Map](#current-direct-child-map) ·
[Scope](#scope-and-bounded-context) · [Invariants](#keystone-invariants) ·
[Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) ·
[Inputs](#candidate-policy-input-profile) · [Outputs](#source-and-evaluated-outputs) ·
[Seams](#object-family-and-policy-lane-seams) · [Checks](#future-layer-admissibility-checks) ·
[Runtime](#rule-source-evaluation-and-activation-boundary) ·
[Public boundary](#public-exposure-security-and-sensitivity) ·
[Evidence](#related-contracts-schemas-fixtures-tests-and-workflows) ·
[Validation](#validation-coverage-and-limits) · [Contributing](#contributor-contract) ·
[Correction](#correction-supersession-withdrawal-and-rollback) ·
[Verification](#open-verification-register) · [No-loss review](#evidence-review-and-no-loss-ledger)

## Purpose

This boundary may hold reviewed, versioned policy source for operation-specific
layer admissibility. A mature rule family could evaluate whether a governed
layer representation may be resolved, registered, rendered, identified,
queried, inspected, exported, cached, promoted, or exposed to a particular
audience under current evidence, rights, sensitivity, review, release,
freshness, correction, and rollback context.

The policy question is:

> Given an explicit layer operation, immutable subject identity, caller,
> purpose, audience, representation, resolved support, policy version, and
> effective time, is the operation allowed, restricted, held, denied, or
> unresolved—and which enforceable obligations apply?

This README documents the repository boundary and a safe convergence target.
It does **not** define what a `LayerManifest` means, create a layer, validate
real support, activate a policy, emit a `PolicyDecision`, mutate a registry,
create a MapLibre source, approve release, or publish a carrier.

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical root for normative allow, deny, hold, restrict, and abstain rule source. |
| Directory profile | `BOUNDARY_COMPACT`: this lane changes public exposure, sensitivity, release, and runtime trust assumptions. |
| Governing placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy source from contracts, schemas, data, release records, and application code. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry projects adopted governance; it does not activate this child lane. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` changes to `@bartytime4life`. Routing is not proof of layer-policy stewardship, affected-domain review, independence, policy acceptance, release authority, or production approval. |
| Local owner | **NEEDS VERIFICATION.** No accepted layer-policy steward, bundle authority, evaluator owner, or independent release approver was established in the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted machine scope identifier for `policy/layers/` was found in the reviewed root or policy-gate projections. This README does not invent one. |
| Runtime authority | None. Policy source may be consumed by a separately accepted evaluator; repository location is not execution. |
| Release authority | None. A future layer-policy result could be one input to a governed release decision, never the decision itself. |
| Publication authority | None. Public carriers require separate evidence, policy, review, release, correction, and rollback closure. |

## Current status and evidence

All observations in this section are pinned to
`main@e6de606175bb1d352c00000486808f2e7e0f7b2f`.

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| Target README | 44-byte `# policy :: layers` greenfield stub, blob `eaea3cd5a580ab2899059ac88f07e204e70e5da2` | The prior file named the lane but did not define its responsibility or non-effects. |
| Local tree | Tree `c011b4a5c2dbb8425727b91cc6d0f0a61cc13247`; exactly this README and one Rego file | The direct-child inventory is known; no local fixture, test, manifest, bundle, evaluator, or decision emitter is present. |
| Local Rego source | 356-byte proposed stub; package `kfm.released_only_for_public`; `default deny := false`; all example logic commented out | Static source inspection establishes a no-op posture, not a released-only invariant. Rego parsing and engine compatibility are not proved by a native local test. |
| Local inputs and outcomes | The operative source reads no `input` field and defines no reason, obligation, hold, restriction, abstention, or error behavior | No candidate input contract or outward decision contract is implemented. |
| Bundle and evaluator | No accepted local bundle manifest, selector, evaluator binding, entrypoint, or digest was established | The package is not an active policy gate. |
| Policy-gate register | [`PROPOSED`](../../control_plane/policy_gate_register.yaml) with `entries: []` | No layer gate, required check, evaluator, bundle, or consumer is registered. |
| LayerManifest strict profile | Separate `PROPOSED_INACTIVE` / `FIXTURE_ONLY` dual-profile contract, closed schema, validator, 4 valid and 12 invalid fixtures, and 13 Python unit-test methods | A `PASS` proves local shape, identity, and deterministic semantic checks only; references, policy, review, artifacts, signatures, release, and public use remain unresolved. |
| Runtime-admission projection | Separate `proposed-inactive`, fixture-only TypeScript assessment with 13 cases and 3 test blocks | A `PASS` means eligibility for a later governed loader. It explicitly creates no registry mutation or MapLibre source. |
| Governed `/layers` route | Executable route delegates to the shared finite `ABSTAIN` stub | Route presence proves containment, not layer resolution, policy evaluation, or public serving. |
| General release gate | One separately governed `PROPOSED_INACTIVE` Rego source/test/fixture/workflow packet exists under `policy/rego/` | It is bounded general release-gate evidence; it is not a layer-policy bundle and does not activate this lane. |
| Release and publication | Owned by separate governed roots and transitions | Nothing in this directory releases, publishes, corrects, withdraws, or rolls back a layer. |

The strongest current evidence is therefore **candidate validation plus
fail-closed containment outside this directory**, not operative policy inside
it.

## Current direct-child map

The map is verified from the complete direct-child tree at the pinned baseline.
It shows this directory and direct children only, as required by Directory
Rules `DIR-README-003` through `DIR-README-005`.

```text
policy/layers/
├── README.md                         # this boundary and contributor contract
└── released_only_for_public.rego     # proposed no-op rule stub; not activated
```

Path presence establishes routing, not maturity or authority. No manifest,
tile, style, decision, receipt, proof, fixture, test, bundle payload, evaluator,
registry, cache, or public artifact belongs in this directory merely because
it concerns a layer.

## Scope and bounded context

### In scope for a future accepted layer-policy family

- operation-specific admission for resolve, register, render, identify, query,
  inspect, export, cache, promote, and public-exposure requests;
- subject, manifest, representation, artifact, source, and release identity
  binding;
- evidence, rights, sensitivity, consent or sovereignty, review, freshness,
  correction, withdrawal, and rollback prerequisites;
- public field allowlists, geometry transformation, audience restriction,
  attribution, citation, and stale/degraded behavior;
- refusal of direct internal, mutable, unresolved, unreleased, withdrawn,
  superseded, or authority-overclaiming sources;
- finite public-safe reasons and enforceable obligations; and
- rule versioning, effective time, expiry, supersession, replay, and consumer
  fail-closed behavior.

### Out of scope

- defining `LayerManifest`, `LayerDescriptor`, `LayerCatalogItem`, style,
  tile-artifact, release-manifest, or rollback semantics;
- selecting or changing a canonical schema home by README prose;
- building, transforming, signing, storing, moving, or serving layer payloads;
- resolving source, evidence, policy, review, artifact, signature, release, or
  correction references;
- authenticating callers, reviewers, stewards, or release authorities;
- mutating a catalog or layer registry, creating a MapLibre source, composing a
  map style, or implementing an API route;
- storing policy evaluations, review records, promotion decisions, release
  manifests, receipts, proofs, correction notices, or rollback cards; and
- deploying, releasing, publishing, or granting public use.

## Keystone invariants

1. **A layer is not released because it exists.** A manifest, catalog record,
   tile archive, style, URL, registry entry, branch, or merged pull request is
   not release or publication evidence.
2. **Validation is not authorization.** Schema or candidate `PASS` proves only
   the declared local checks; it cannot establish evidence truth, policy,
   review, rights, signatures, release, or public safety.
3. **Operations are distinct.** Permission to inspect metadata does not imply
   permission to load bytes; permission to render does not imply query, export,
   caching, AI use, promotion, or publication.
4. **Authority roles remain separate.** Contracts define meaning, schemas
   define shape, validators check bounded claims, policy evaluates
   admissibility, review records human disposition, release records approve
   transitions, and publishers materialize approved carriers.
5. **Public clients consume released carriers.** Browsers, maps, APIs, search,
   exports, graphs, and AI must not read RAW, WORK, QUARANTINE, internal
   registries, canonical stores, or unapproved model output directly.
6. **Sensitivity is enforced before delivery.** Style filters, hidden layers,
   opacity, zoom thresholds, or disabled popups are not redaction and cannot
   protect sensitive geometry or fields already delivered to a client.
7. **References remain role-specific.** Catalog, source, evidence, policy,
   review, promotion, release, artifact, correction, and rollback references
   must not collapse into a single token or stand in for one another.
8. **Unknown support fails closed.** Missing, stale, mismatched, revoked,
   superseded, unauthenticated, or unresolvable support must not become implicit
   allow.
9. **Obligations are part of the result.** A caller unable to enforce required
   redaction, generalization, attribution, citation, audience, retention,
   no-cache, review, correction, or rollback behavior must not proceed.
10. **Corrections propagate.** A later correction, rights change, sensitivity
    escalation, withdrawal, or rollback must invalidate dependent policy and
    public-surface state; cached success is not permanent authority.

## What belongs here

Subject to accepted contracts, schemas, policy conventions, and evaluator
binding, this lane may contain:

- declarative rule source whose primary responsibility is layer-specific
  operation and exposure admissibility;
- rules that consume stable references to manifest identity, source role,
  evidence, rights, sensitivity, review, release, artifacts, correction, and
  rollback without redefining those objects;
- fail-closed behavior for missing, malformed, stale, superseded, withdrawn,
  unresolved, or incompatible inputs;
- public-safe reason codes and enforceable obligations with an accepted native
  and outward decision contract;
- package, entrypoint, version, digest, effective-time, supersession, and
  correction metadata; and
- narrowly paired native policy tests if an accepted repository convention
  establishes their placement and execution.

A file belongs here because it evaluates **layer admissibility**. It does not
belong here merely because it mentions maps, MapLibre, manifests, tiles,
styles, rights, sensitivity, evidence, runtime, release, or publication.

## What is prohibited

| Prohibited material or claim | Owning surface or required action |
|---|---|
| `LayerManifest` or other layer-object meaning | [`contracts/`](../../contracts/README.md), currently the inspected [data LayerManifest contract](../../contracts/data/layer_manifest.md) for this family |
| JSON Schema, DTO, enum, or machine field shape | [`schemas/`](../../schemas/README.md), with the current strict candidate under [`schemas/contracts/v1/data/`](../../schemas/contracts/v1/data/layer_manifest.schema.json) |
| Manifest, layer, feature, catalog, registry, style, tile, PMTiles, COG, GeoJSON, sprite, glyph, screenshot, or cache instance | Its governed lifecycle, registry, release, application, or external artifact store; never policy source |
| EvidenceBundle, source descriptor, proof, receipt, signature, attestation, review, policy-decision, promotion, release, correction, withdrawal, or rollback instance | The corresponding governed object family; policy consumes references and never creates support |
| Evaluator, registry loader, MapLibre adapter, API route, UI component, cache, deployment, or publisher implementation | `packages/`, `apps/`, `runtime/`, `tools/`, or `infra/` according to responsibility |
| Reusable synthetic fixtures and conformance tests | [`fixtures/`](../../fixtures/README.md) and [`tests/`](../../tests/README.md), except an explicitly accepted engine-native co-location profile |
| Release decision or released-carrier record | [`release/`](../../release/README.md) and approved published-carrier lanes |
| Secrets, credentials, signed URLs, private actor details, exact protected sites, rare-species coordinates, living-person or genomic data, or exploit-enabling infrastructure detail | Keep out of Git, policy inputs captured in logs, reasons, fixtures, documentation, and generated receipts; use authorized restricted systems |
| A filename, comment, path, default, `PASS`, workflow, PR approval, manifest field, or `PUBLISHED` string presented as authorization | Resolve accepted policy, support, review, release, signature, consumer, and current correction state through governed mechanisms |
| Client-side hiding presented as sensitivity enforcement | Transform, generalize, redact, aggregate, delay, or deny before public bytes are produced or delivered |

## Candidate policy input profile

The current Rego stub reads **no inputs**. Before any operative rule is added,
an accepted input contract should make at least these families explicit and
versioned:

| Input family | Minimum candidate content |
|---|---|
| Request | Operation, purpose, audience, intended effect, request time, and policy-effective time. |
| Caller | Authenticated actor or service reference, role/assignment reference, tenant or jurisdictional scope, and capability context. |
| Subject | Stable `layer_id`, manifest id, manifest digest or `spec_hash`, layer version, representation id, and requested artifact digest. |
| Profile | Contract/schema profile, maturity, execution mode, and compatibility branch; legacy or fixture-only profiles must not silently graduate. |
| Lifecycle and trust | Candidate/released state, trust state, freshness, valid time, source-update time, correction, supersession, withdrawal, and rollback state. |
| Source and evidence | Role-preserving source refs, EvidenceBundle refs, resolution results, provenance or run receipt, and contradiction or degraded-support posture. |
| Rights and sensitivity | Rights/license disposition, audience, sensitivity tier, consent/CARE/sovereignty posture where applicable, public field allowlist, geometry treatment, and transform receipt. |
| Review and policy | Subject-bound review refs, reviewer-authority result, applicable policy-decision refs, unresolved obligations, and recusal or independence context. |
| Release | Promotion decision, release manifest, immutable artifact and signature/attestation results, rollback target, and public carrier classification. |
| Runtime | Governed source URL class, registry status, cache posture, supported obligations, stale/degraded behavior, and renderer or query capability requested. |
| Evaluator | Bundle id and digest, package and entrypoint, evaluator implementation/version, input-contract version, decision-normalization version, and correlation id. |

Inputs should be caller-supplied, deterministic, and inspectable. A policy
evaluation must not silently fetch hidden state, trust path location, accept a
floating `latest` authority reference, or infer release from a URL or registry
entry.

## Source and evaluated outputs

Three output layers must remain distinct:

| Layer | Current state | Required future boundary |
|---|---|---|
| Rule source value | The stub statically declares `deny := false`; no operative reasons or obligations | Define a typed native result for complete, incomplete, malformed, and evaluator-error inputs. |
| Normalized policy decision | None emitted; the current proposed `PolicyDecision` schema has no `layers` family | Accept whether this lane normalizes to an existing family such as `render` or to a new versioned family; define mapping to `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` without collapsing hold/restrict semantics. |
| Operational effect | None | A separately governed consumer may enforce an authenticated, current decision and obligations; the decision itself must not mutate a registry, release, or public carrier. |

The current `default deny := false` is especially unsafe as an authorization
signal: absence of a denial is not an affirmative allow. A future rule must not
turn malformed, missing, unknown, or evaluator-error context into permission.

Reason codes should be stable, bounded, and safe to disclose. Detailed
coordinates, private identifiers, hidden predicates, credentials, protected
source names, and exploit-relevant configuration must not appear in public
reasons, logs, traces, fixtures, or receipts.

## Object-family and policy-lane seams

The current repository contains several overlapping or adjacent surfaces.
Their presence is evidence of an unresolved convergence problem, not permission
to copy rules between them.

| Surface | Confirmed responsibility or state | Relationship to this lane |
|---|---|---|
| [`policy/data/`](../data/README.md) | Documentation-only lifecycle and public-exposure boundary; no direct executable data-policy rule established | The strict LayerManifest schema currently points here in `x-kfm.policy`; decide whether generic lifecycle exposure or layer-specific operations own each rule. |
| [`policy/runtime/`](../runtime/README.md) | Generic runtime admissibility boundary containing an overlapping `deny_unpublished_public` no-op stub | Runtime operation policy must not duplicate layer-specific exposure rules or treat client loading as release. |
| `policy/domains/hazards/layer_manifest.rego` | Domain-specific generated scaffold with `default allow := false` and no operative body or native tests established | Domain policy may add stricter hazard requirements but must not become the general LayerManifest contract or silently override parent behavior. |
| [`policy/release/`](../release/README.md) and [`policy/rego/release_gate_v1.rego`](../rego/release_gate_v1.rego) | Release-policy source; one bounded general release-gate candidate has native tests and a dedicated checksum-pinned workflow | Release admissibility remains separate; its result may be consumed but cannot be inferred or reimplemented here. |
| [Data LayerManifest contract](../../contracts/data/layer_manifest.md) | Current inspected semantic authority for the strict fixture profile | Defines candidate meaning and reference roles; does not approve public use. |
| [Release LayerManifest bridge](../../contracts/release/layer_manifest.md) | Proposed compatibility bridge for release inclusion, with schema home unresolved | Must reference the canonical manifest rather than create parallel meaning or policy authority. |
| [Runtime LayerManifest schema](../../schemas/contracts/v1/runtime/layer_manifest.schema.json) | Empty permissive proposed scaffold | Must not be mistaken for the closed data candidate profile or an active runtime contract. |
| [Release manifest record lane](../../release/manifests/layers/README.md) | Release-facing record guidance | Stores or indexes governed release records; must not store rule source or replace a policy decision. |
| [UI layering architecture](../../docs/architecture/ui/LAYERING.md) | Proposed design guidance with older path and schema assumptions | Useful risk and anti-pattern evidence, not proof that the proposed policy bundle, schema homes, or runtime are implemented. |

Before adding operative source, an accepted responsibility decision must state
which layer-specific questions cannot be owned by generic data lifecycle,
generic runtime, release, or affected-domain policy. It must also define
precedence and conservative composition without allowing one lane to weaken
another.

## Future layer-admissibility checks

The following is a **PROPOSED** check decomposition, not current behavior or an
accepted gate sequence:

1. **Request and subject binding** — operation, caller, purpose, audience,
   layer id, manifest digest, representation, artifact digest, and effective
   time are explicit and mutually consistent.
2. **Profile and lifecycle eligibility** — legacy, fixture-only, inactive,
   candidate, stale, superseded, withdrawn, malformed, or authority-overclaiming
   profiles cannot silently enter an active public path.
3. **Source and evidence closure** — source roles remain distinct; required
   support resolves; provenance is current; contradictions and degraded support
   are surfaced.
4. **Rights, sensitivity, and transformation** — rights permit the operation;
   audience and fields are bounded; sensitive geometry is transformed before
   delivery; required receipts and sovereignty or consent review resolve.
5. **Review, policy, and release closure** — subject-bound review, applicable
   policy results, promotion decision, release manifest, immutable artifacts,
   signature/attestation posture, and rollback target are current and coherent.
6. **Consumer capability** — the caller can enforce every obligation, uses a
   governed released carrier, exposes finite negative states, and cannot fall
   back to internal or stale sources.
7. **Correction and replay** — no correction, rights change, sensitivity
   escalation, withdrawal, supersession, expiry, or rollback invalidates the
   prior result; replay under pinned inputs is possible.

A mature profile needs positive, negative, held, restricted, abstained,
malformed, evaluator-error, correction, and replay cases for each operation.
The most restrictive applicable accepted policy should prevail. Exact
composition, precedence, and conflict behavior remain **NEEDS VERIFICATION**.

## Rule source, evaluation, and activation boundary

### What the current stub does

Static inspection of [`released_only_for_public.rego`](./released_only_for_public.rego)
confirms:

- package `kfm.released_only_for_public`;
- status comment `PROPOSED greenfield stub. No real rules yet.`;
- `default deny := false`;
- no operative rule body;
- no operative `input` access;
- no stable reason or obligation vocabulary; and
- no local native test, bundle manifest, selector, evaluator, or consumer.

The commented example mentions `input.kind` and
`input.evidence_bundle_resolved`. Comments are not an input contract or rule.
Do not uncomment the example or flip the default in isolation: its native
result type, Rego version compatibility, evidence semantics, outcome mapping,
tests, and consumer behavior are not established.

### Minimum graduation packet

Before this lane can claim operative enforcement, a reviewed change should
provide all of the following:

1. accepted responsibility and scope decision resolving the overlapping lanes;
2. semantic input contract and paired closed schema with explicit versioning;
3. rule package, entrypoint, native result type, reasons, obligations, and
   fail-closed malformed/evaluator-error behavior;
4. deterministic positive and negative native tests, including sensitive,
   stale, withdrawn, mismatched, unsupported-obligation, and correction cases;
5. accepted bundle manifest, selection rules, digest/signature binding, and
   reproducible no-network evaluation;
6. accepted evaluator implementation/version and native-to-outward
   normalization, including a valid `PolicyDecision` family;
7. authenticated governed consumer with proof that no negative or unresolved
   outcome reaches registry mutation, MapLibre, export, cache, release, or
   public state;
8. decision receipt, replay, expiry, correction, supersession, withdrawal, and
   rollback behavior;
9. dedicated workflow and required-check decision with least-privilege read-only
   validation where practical; and
10. qualified policy, security/privacy, evidence, release, UI/runtime,
    affected-domain, and independent review for the declared risk.

Repository-wide [`policy-test`](../../.github/workflows/policy-test.yml) is an
explicit readiness guard. It statically inventories policy surfaces and the
separately governed release-gate packet; it evaluates no general policy and
emits no `PolicyDecision`. A green run does not satisfy the graduation packet.

## Public exposure, security, and sensitivity

Layer policy sits on a high-risk trust membrane because map delivery can expose
precise location, protected attributes, relationship inference, infrastructure
detail, and reusable bulk data even when the visible style appears harmless.

### Required posture

- Public clients consume only governed, immutable, release-approved carriers
  through governed interfaces.
- Internal filesystem, database, object-store, catalog, registry, model,
  signed-source, and pipeline locations are not public layer URLs.
- Unknown rights, sensitivity, review, evidence, release, signature,
  correction, or rollback state does not become public permission.
- Public projections use an explicit field allowlist. Dropping a field in a
  popup does not remove it from tiles, feature queries, downloads, caches, or
  browser memory.
- Sensitive geometry is generalized, aggregated, delayed, transformed, or
  denied before tile or feature generation. Style-only filters are never a
  security boundary.
- Source role, attribution, temporal limits, uncertainty, stale/degraded state,
  and correction status remain visible where required.
- Export, offline cache, bulk query, screenshot, AI, and joined-derivative use
  receive their own operation-specific decisions; render permission does not
  propagate automatically.
- Diagnostics are public-safe and non-enumerating. Protected layer existence,
  exact coordinates, private actor identity, policy internals, and storage
  topology must not leak through reason text or timing-dependent fallback.
- A caller that cannot enforce an obligation must stop. Silent degradation to
  an internal source, prior release, broader audience, or less restrictive
  style is prohibited unless an accepted policy explicitly authorizes the
  fallback.

### Exposure is not publication authority

A future policy result may state that a requested use is admissible under
declared conditions. It still does not create the evidence, authenticate the
review, sign the artifact, approve the release, mutate the registry, publish
the carrier, purge stale caches, or notify affected consumers. Those are
separate governed capabilities and records.

## Related contracts, schemas, fixtures, tests, and workflows

### LayerManifest candidate validation

The inspected [LayerManifest contract](../../contracts/data/layer_manifest.md)
and [closed data schema](../../schemas/contracts/v1/data/layer_manifest.schema.json)
retain a permissive legacy branch and add a strict
`PROPOSED_INACTIVE` / `FIXTURE_ONLY` candidate profile. The strict profile:

- fixes `lifecycle_state` to `CANDIDATE` and authority-bearing governance flags
  to `false`;
- preserves distinct catalog, release, promotion, source, evidence, policy,
  review, artifact, correction, and rollback references;
- validates deterministic RFC 8785 JCS plus SHA-256 identity;
- rejects floating authority references, incoherent time/bounds/zoom,
  source-role collapse, public rights gaps, and missing transformation support;
  and
- emits finite validator outcomes `PASS`, `FAIL`, or `ERROR` with bounded
  finding codes and JSON pointers.

The [fixture family](../../fixtures/data/layer_manifest/README.md) contains 4
valid and 12 invalid JSON cases. The Python suite contains 13 unit-test methods.
Passing proves only the local carrier and deterministic checks. It does not
resolve references, inspect real artifact bytes, verify signatures, evaluate
policy, authenticate review, register a layer, approve release, or permit
public use.

The dedicated [`layer-manifest` workflow](../../.github/workflows/layer-manifest.yml)
is no-network, read-only orchestration for that profile. A README-only change
under `policy/layers/` is not one of its path triggers.

### Runtime-admission candidate

The separate [runtime-admission contract](../../contracts/runtime/layer_manifest_admission.md),
13-case [fixture matrix](../../fixtures/runtime/layer_manifest_admission/cases.json),
TypeScript evaluator, and 3-test suite exercise released eligibility and
fail-closed legacy, inactive, candidate, stale, withdrawn, superseded,
unresolved-evidence, policy-denied, subject-mismatch, direct-internal-source,
authority-overclaim, and invalid-shape paths.

Its `PASS` result still carries `authority: "NONE"`,
`registryMutated: false`, `maplibreSourceCreated: false`, and a hold stating
that runtime registration was not executed. The dedicated
[`layer-manifest-admission` workflow](../../.github/workflows/layer-manifest-admission.yml)
does not resolve real references, verify artifacts/signatures, execute policy,
release, deploy, or publish; this README path does not trigger it.

### Governed API and release evidence

The [`/layers` route](../../apps/governed-api/src/governed_api/routes/layers.py)
returns the shared finite `ABSTAIN` scaffold. The proposed release bridge and
release-manifest lane remain separate from policy source. The bounded general
release-gate candidate checks release-wide evidence and review prerequisites
under its own package and workflow; it does not prove layer-specific
admissibility or public loading.

## Validation coverage and limits

### Current local rule coverage

| Check | Current state | What remains unproven |
|---|---|---|
| File and package presence | **CONFIRMED** | Rego parsing and supported engine/version. |
| Default inspection | **CONFIRMED `deny := false`** | Any affirmative or fail-closed layer-admission behavior. |
| Operative rule bodies | **CONFIRMED absent** | Every input, outcome, reason, obligation, and error path. |
| Native Rego tests | **Not present in the local lane** | Positive, negative, hold, restrict, abstain, malformed, replay, and correction behavior. |
| Bundle and evaluator binding | **Not established** | Selection, digest/signature binding, normalization, reproducible execution, and expiry. |
| Governed consumer | **Not established** | Registry, MapLibre, API, query, export, cache, release, correction, or rollback enforcement. |
| Independent review and authority | **NEEDS VERIFICATION** | Qualified stewardship, affected-domain participation, separation of duties, and fallback behavior. |

### Repository-native related checks

```bash
# LayerManifest candidate shape, semantics, fixture polarity, and registry wiring.
python -m unittest \
  tests.validators.test_validate_layer_manifest \
  --verbose
python tools/validators/data/validate_layer_manifest.py --fixtures
python tools/validate_all.py --validate-registry
python tools/validate_all.py \
  --profile release-dry-run \
  --validator layer-manifest \
  --quiet

# Fixture-only runtime admission; eligibility only, with no registry mutation.
pnpm --filter explorer-web exec vitest run \
  tests/layer-manifest-admission.test.ts

# Documentation structure and local-link checks for this boundary.
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --format markdown \
  policy/layers/README.md
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  policy/layers/README.md
```

Passing these commands proves only the bounded contract, fixture, registry,
runtime-candidate, metadata, or link property each command declares. None is a
native test of `released_only_for_public.rego`; none evaluates an accepted
layer-policy bundle, authenticates support or reviewers, mutates a registry,
creates a MapLibre source, approves release, or publishes a layer.

## Contributor contract

Before changing this README or adding or modifying layer-policy source:

1. Pin current `main`, the target blob, the complete direct-child tree, and the
   exact policy, contract, schema, fixture, validator, test, workflow, runtime,
   release, correction, and rollback evidence in scope.
2. Search open pull requests and recent commits for the same paths, packages,
   entrypoints, object families, and outcome vocabulary.
3. Classify the change as documentation, a no-op scaffold, an inactive
   candidate, or operative policy. Never upgrade maturity by implication.
4. Resolve responsibility across `policy/layers/`, `policy/data/`,
   `policy/runtime/`, `policy/release/`, and affected-domain policy before
   duplicating or composing a rule.
5. Define the exact operation, subject ids and digests, caller, purpose,
   audience, input contract, native result, outward decision family, reasons,
   obligations, effective time, expiry, and malformed/evaluator-error behavior.
6. Keep semantic meaning in `contracts/`, machine shape in `schemas/`, reusable
   fixtures in `fixtures/`, conformance in `tests/`, evaluator/runtime code in
   implementation roots, and decision instances under their owning data or
   release family.
7. Treat missing evidence, source roles, rights, sensitivity, consent,
   sovereignty, review, policy, immutable artifacts, signatures, release,
   correction, or rollback context as a hold, denial, abstention, restriction,
   or error under an accepted profile—never implicit allow.
8. Add deterministic, synthetic, rights-safe positive and negative tests for
   every operation. Cover legacy/inactive profiles, candidate/stale/degraded/
   withdrawn state, subject and digest mismatch, direct internal sources,
   floating references, unknown rights, sensitive geometry, unsupported
   obligations, stale decisions, correction, and evaluator error.
9. Bind operative source to an accepted bundle, evaluator, input version,
   normalization, consumer, decision receipt, replay, correction, expiry,
   supersession, and rollback path before claiming enforcement.
10. Prove that negative, unresolved, malformed, stale, or unsupported results
    cannot load bytes, mutate registries, create map sources, query/export/cache
    data, approve release, or reach public surfaces.
11. Keep sensitive details out of source comments, public reasons, fixtures,
    logs, workflow summaries, screenshots, and generated receipts.
12. Run changed-area validation, inspect the full diff, and keep code review,
    policy acceptance, merge approval, runtime activation, release approval,
    deployment, and publication as separate states.

Do **not** flip `default deny`, uncomment the example body, add the file to a
bundle, or wire a consumer merely to make a readiness check green. A safe
graduation is a coherent packet, not an isolated source edit.

### Pull-request evidence

A reviewable change should state:

- pinned base and exact changed paths;
- current and proposed maturity;
- responsibility resolution across overlapping policy lanes;
- package, entrypoint, input contract, native output, and behavior delta;
- contracts and schemas consumed rather than redefined;
- fixtures, tests, commands, and exact results;
- bundle, evaluator, consumer, required-check, and public-surface effects or
  explicit non-effects;
- rights, sensitivity, privacy, security, evidence, review, release, and
  affected-domain risk;
- decision/replay, correction, expiry, supersession, withdrawal, and rollback
  behavior; and
- unresolved ownership, authority, schema-home, or operational questions.

## Review triggers

Re-review this boundary when:

- the Rego stub gains operative logic, changes default polarity, package,
  entrypoint, result type, or location;
- a native test, fixture, bundle, selector, evaluator, normalization, decision
  receipt, consumer, or required check binds to the lane;
- the policy-gate register gains a layer entry;
- `PolicyDecision` gains or selects a layer-facing family;
- the LayerManifest contract, schema profile, policy pointer, canonical home,
  validator, runtime admission, registry, or `/layers` route changes;
- rights, sensitivity, consent, sovereignty, field allowlist, geometry
  transformation, query, export, caching, or AI-use behavior changes;
- promotion, release, signature, correction, withdrawal, or rollback
  requirements change;
- a map, API, public carrier, tile service, cache, or governed loader begins
  consuming a layer decision;
- CODEOWNERS, stewardship, independent review, branch protection, or required
  checks change;
- a security, privacy, harmful-precision, rights, stale-data, correction, or
  publication-bypass incident exposes a gap; or
- parent policy, Directory Rules, or root-registry authority changes.

## Correction, supersession, withdrawal, and rollback

### Documentation correction

Correct inaccurate README claims in place through reviewed Git history. Mark
unresolved facts as **NEEDS VERIFICATION**, `UNKNOWN`, `CONFLICTED`, or `HOLD`;
do not manufacture certainty or rewrite historical receipts to keep prose tidy.

### Policy correction and supersession

If an operative layer rule is later unsafe, incomplete, or wrong:

1. stop or hold affected consumers without converting errors to allow;
2. preserve the prior rule identity, bundle digest, evaluator version, inputs,
   decisions, receipts, and effective interval;
3. issue a versioned correction or superseding policy with explicit scope;
4. identify affected manifests, registries, map sources, queries, exports,
   caches, releases, and public carriers;
5. reevaluate or invalidate dependent decisions and obligations;
6. withdraw, correct, replace, or roll back public material through authorized
   release mechanisms; and
7. verify cache purge, route behavior, user-visible finite state, and rollback
   completion without deleting audit history.

Rollback must not recreate two writable policy authorities or silently restore
an unsafe public layer. When source rollback is unsafe because decisions or
public carriers already depend on the new rule, use a governed forward fix and
record why.

### This documentation-only change

Before merge, close the draft pull request and delete the feature branch. After
an authorized merge, revert the documentation commit or merge commit. No
policy source, evaluator, registry, map source, release, cache, or public
artifact is modified by this README update, so no operational rollback is
required.

## Open verification register

| Item | Current posture | Evidence required to close |
|---|---|---|
| Accepted local responsibility and scope ID | **NEEDS VERIFICATION** | Accepted decision and machine projection distinguishing layer, data, runtime, release, and domain policy. |
| Local owner and independent reviewers | **NEEDS VERIFICATION** | Current steward assignments, qualifications, affected-domain coverage, and escalation path. |
| Canonical LayerManifest contract/schema home | **CONFLICTED / NEEDS VERIFICATION** | Accepted decision and migration/compatibility record reconciling data, runtime, layers, map, and release surfaces. |
| `x-kfm.policy` target | **CONFLICTED** | Deliberate decision to retain `policy/data/`, select `policy/layers/`, or split exact responsibilities without duplicate rules. |
| Operation vocabulary | **NEEDS VERIFICATION** | Accepted enum and per-operation input/output semantics. |
| Native rule result | **NEEDS VERIFICATION** | Typed Rego contract for allow/deny/hold/restrict/abstain/error and malformed input. |
| `PolicyDecision` family and normalization | **NEEDS VERIFICATION** | Versioned schema/contract decision and tested native-to-outward mapping; `layers` is not currently an allowed family. |
| Reason and obligation vocabulary | **NEEDS VERIFICATION** | Public-safe registry, consumer capability contract, and negative tests. |
| Bundle, selector, evaluator, and entrypoint | **Not established** | Accepted manifests, digests/signatures, versions, reproducible execution, and expiry/supersession rules. |
| Native local tests | **Absent** | Complete deterministic operation matrix and dedicated workflow. |
| Reference, artifact, and signature resolution | **Not established** | Governed resolver and verifier contracts, implementations, receipts, and negative tests. |
| Governed registry/MapLibre/API consumer | **Not established** | Authenticated consumer, finite-state UI/API behavior, no-internal-source proof, and fail-closed integration tests. |
| Required-check and branch-protection status | **UNKNOWN** | Current hosted repository configuration and successful check evidence; workflow presence is insufficient. |
| Release/publication integration | **Not established** | Promotion/release authority, immutable carriers, rollback target, signatures, and publisher receipts. |
| Correction, withdrawal, and cache invalidation | **Not established** | End-to-end replay, dependency invalidation, purge, correction notice, and rollback tests. |
| Production operation | **Not established** | Deployment identity, configuration, monitoring, incident response, and authorized activation record. |

Open items are holds on stronger claims, not permission to choose a convenient
default.

## Evidence review and no-loss ledger

This v0.1 modernization preserves and strengthens the complete prior target:

- the H1 remains exactly `# policy :: layers`;
- the prior statement `Greenfield bundle stub.` is preserved as the explicit
  current no-op and inactive conclusion rather than deleted or upgraded;
- the tracked Rego source is unchanged;
- no package, default, rule body, bundle, evaluator, test, workflow, registry,
  route, release, or public-surface behavior changes;
- verified candidate validation and runtime-admission evidence is linked but
  not relabeled as policy enforcement;
- overlapping policy and LayerManifest surfaces are surfaced as unresolved
  seams rather than silently normalized; and
- unknown ownership, authority, activation, required-check, release, and
  production facts remain visibly unverified.

Evidence was reviewed against the pinned base, exact prior blob and tree,
accepted Directory Rules authority, policy root contract, direct local source,
LayerManifest contract/schema/fixtures/validator/tests, runtime admission,
governed API stub, release bridge and record lane, policy-gate register,
workflow wiring, CODEOWNERS, and adjacent policy stubs. Repository evidence
supports this documentation boundary; it does not support an operative
layer-policy claim.

<p align="right"><a href="#top">Back to top</a></p>
