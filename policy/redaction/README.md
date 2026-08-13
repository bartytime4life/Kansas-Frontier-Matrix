<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-redaction-readme
title: policy/redaction/ — Redaction Profile Policy Boundary
type: readme
version: v0.1
status: draft; BOUNDARY_COMPACT; repository-grounded; proposed-inactive; catalog-home-conflicted; default-hold; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ review to @bartytime4life; no accepted redaction-profile steward or independent approver was established
created: 2026-08-13
updated: 2026-08-13
policy_label: public; policy; redaction; profile-catalog; sensitivity; geoprivacy; trust-boundary; default-hold; non-release; non-publication
owning_root: policy/
responsibility: Define the local redaction-profile policy boundary, its inherited authority, current placeholder inventory, unresolved catalog-home conflict, safe authoring envelope, separation rules, evidence limits, and correction handoffs without claiming an active catalog, transform runtime, release authority, or publication authority.
truth_posture: CONFIRMED accepted placement under policy/, absent prior README, one PROPOSED placeholder profile file, a parallel sensitivity placeholder, an explicit unresolved catalog-home question, draft design standards, a closed PROPOSED_INACTIVE fixture-only RedactionReceipt profile, a greenfield transform package, public repository visibility, internal policy exposure, and bounded validation surfaces / PROPOSED BOUNDARY_COMPACT contract, single-writer convergence hold, profile authoring envelope, and fail-closed evaluation posture / NEEDS VERIFICATION accepted catalog home, local scope ID, steward assignments, profile schema and lifecycle, parameter-classification rules, evaluator and consumer binding, transform implementation, complete conformance vectors, receipt compatibility, correction propagation, release integration, and required-check enforcement
related:
  - ../README.md
  - ../sensitivity/README.md
  - ../sensitivity/profiles.yaml
  - ../geoprivacy/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../docs/doctrine/sensitivity.md
  - ../../docs/standards/REDACTION_PROFILES.md
  - ../../docs/standards/REDACTION_DETERMINISM.md
  - ../../contracts/shared/redaction_receipt.md
  - ../../docs/intake/exploratory/redaction-receipt-v1-source-map.md
  - ../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../fixtures/contracts/v1/receipts/redaction_receipt/cases.json
  - ../../tools/validators/receipts/validate_redaction_receipt.py
  - ../../tests/validators/test_validate_redaction_receipt.py
  - ../../packages/redaction/README.md
  - ../../apps/explorer-web/README.md
  - ../../release/README.md
  - ../../.github/workflows/redaction-receipt.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: redaction

`policy/redaction/` is KFM's **BOUNDARY_COMPACT local policy-source boundary**
for candidate named redaction profiles. It inherits the authority and limits of
[`policy/`](../README.md). It does not classify source material, execute a
transform, prove that a derivative is safe, approve release, or publish data.

> [!IMPORTANT]
> **Safe current conclusion:** this lane is proposed and inactive. Its only
> payload is [`profiles.yaml`](./profiles.yaml), a five-line `PROPOSED`
> placeholder with no profile entries. No accepted catalog schema, active
> profile, bundle selector, evaluator, transform executor, governed consumer,
> authenticated review, release binding, or publication enforcement is
> established here.

> [!CAUTION]
> **The catalog home is unresolved.** Both this lane and
> [`policy/sensitivity/profiles.yaml`](../sensitivity/profiles.yaml) exist, and
> the Habitat canonical-path document explicitly leaves their relationship to
> a future ADR. Until that decision and a reviewed migration land, neither file
> may be treated as the accepted catalog or populated as a parallel writable
> authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Conflict](#catalog-home-conflict-and-convergence-hold) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Objects](#object-and-decision-boundaries) · [Inputs and outputs](#inputs-and-outputs) · [Profile contract](#candidate-profile-authoring-contract) · [Safety](#fail-closed-hold-and-abstain-posture) · [Runtime and release](#policy-selection-transform-execution-and-release) · [Exposure](#exposure-mutation-and-retention) · [Evidence](#related-contracts-schemas-fixtures-tests-and-workflows) · [Validation](#validation-coverage-and-limits) · [Contributing](#contributor-contract) · [Correction](#correction-supersession-revocation-and-rollback) · [Open work](#open-verification-register)

## Purpose

This boundary may eventually hold reviewed, versioned policy definitions for
named protective transforms. A profile identifies **which transformation
contract is required** for an explicit sensitivity, purpose, audience, scope,
and release context. It can constrain transform class, output precision,
parameter handling, determinism, validation, review, and correction behavior.

The bounded policy question is:

> Given explicit governed context and an accepted profile catalog, which
> versioned protective-transform profile is admissible, and what hold, denial,
> restriction, review, receipt, or re-evaluation obligations remain?

This lane does not answer whether a claim is true, whether rights or consent
exist, whether a sensitivity assessment is correct, how transform code runs,
whether the result is sufficiently protective, or whether the result may be
released. Those questions remain with their owning contracts, evidence,
policy, runtime, validation, review, and release mechanisms.

This README documents the current repository state and defines a conservative
contributor boundary. It does not adopt the draft profile standard, activate
the placeholder, settle the catalog path, or authorize operational use.

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical responsibility root for normative allow, deny, hold, restrict, and abstain rule source. |
| Directory profile | `BOUNDARY_COMPACT`, because profile selection changes sensitivity, exposure, precision, replay, correction, and release trust assumptions. |
| Governing placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 separate policy from contracts and schemas and define the local README contract. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) classifies `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry projects adopted governance; it does not create new authority. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing is not evidence of review, stewardship, independence, qualification, or approval. |
| Local owner | **NEEDS VERIFICATION.** No accepted redaction-profile steward or independently authorized sensitivity/privacy approver was established in the reviewed evidence. |
| Local scope ID | **NEEDS VERIFICATION.** No accepted machine scope identifier for this local boundary was found in the reviewed root projection or target tree. This README does not invent one. |
| Catalog authority | **CONFLICTED / HOLD.** The repository contains parallel placeholder paths, and an ADR is explicitly required to select or reconcile the home. |
| Transform authority | None. Transform mechanics belong to an accepted implementation, not to a YAML profile declaration or this README. |
| Release authority | None. A selected profile and completed receipt may support a release decision; neither makes that decision. |
| Publication authority | None. Public carriers require separate evidence, policy, validation, review, release, correction, and rollback closure. |

## Current status

All observations in this section are pinned to
`main@f9b29f555f5c8075a832cb05deea575fd7b5ba80` on 2026-08-13. Before this
change, the `policy/redaction/` tree was
`82f7cb68baeea544f7c30f227dc3f83f59b5e683`.

| Surface | Confirmed state at baseline | Safe interpretation |
|---|---|---|
| Target README | Absent | The populated boundary lacked the local contract required by Directory Rules. This addition documents the boundary; it does not change profile behavior. |
| [`profiles.yaml`](./profiles.yaml) | Blob `e928e91ccf278fe42ac0cd83f571ba323787573d`; status `PROPOSED`; source points to Habitat canonical-path planning; no profile entries | Path presence is a scaffold, not an accepted catalog, active profile, policy bundle, or transform configuration. |
| Parallel sensitivity file | [`policy/sensitivity/profiles.yaml`](../sensitivity/profiles.yaml), blob `967f058a82919eab69c40cdc12df2eea27a83b18`, is also a `PROPOSED` placeholder | Two candidate files exist; neither is established as the single writable authority. |
| Catalog-home decision | [Habitat canonical paths §12](../../docs/domains/habitat/CANONICAL_PATHS.md#12-open-questions--needs-verification) explicitly leaves `policy/redaction/profiles.yaml` versus `policy/sensitivity/profiles.yaml` open for an ADR | Treat the catalog location and split, if any, as unresolved. |
| Profile design | [Redaction Profiles](../../docs/standards/REDACTION_PROFILES.md) and [Redaction Determinism](../../docs/standards/REDACTION_DETERMINISM.md) are draft/proposed design material | They provide requirements and risks for future work, not accepted parameters or implementation evidence. |
| Receipt profile | The [closed receipt schema](../../schemas/contracts/v1/receipts/redaction_receipt.schema.json) declares `PROPOSED_INACTIVE` and fixture-only governance | Deterministic receipt fixtures validate declarations only; they do not execute policy, open restricted input, run transforms, or authorize release. |
| Transform package | [`packages/redaction/`](../../packages/redaction/README.md) is version `0.0.0` with an empty initializer and comment-only core scaffold | No supported redaction API, executor, profile loader, or production consumer is established. |
| Explorer preview | [`apps/explorer-web/`](../../apps/explorer-web/README.md) contains fixture-first, public-safe preview work | UI projection and preview are not policy selection, transform execution, or an exposure control. |
| Topology guard | Rule `KFM-TOPO-018` requires populated policy boundaries to have a README, and the committed [baseline](../../tools/validators/directory_governance/repository_topology_baseline.json) records `policy/redaction/` | This README is intended to close that inherited documentation finding. It does not close unrelated topology findings. |
| Runtime and release | No accepted catalog resolver, evaluator, executor, receipt writer, release consumer, or publication path was established by the reviewed lane | Operational protection remains **UNKNOWN** and must not be inferred from repository structure. |

The current semantic [RedactionReceipt contract](../../contracts/shared/redaction_receipt.md)
contains older draft schema-posture language than the newer fixture-only schema
packet. Consumers must not resolve that drift by silently treating either
document as accepted operational authority.

## Current direct-child map

The map is verified from the complete direct-child tree at the pinned baseline.
It intentionally does not describe deeper repository content.

| Direct child | Kind | Current role | Maturity and authority |
|---|---|---|---|
| `README.md` | Boundary document | Local purpose, exclusions, authoring hold, validation limits, and handoffs | Added by this documentation-only change; no runtime authority |
| [`profiles.yaml`](./profiles.yaml) | YAML placeholder | Candidate path for a future named-profile catalog | `PROPOSED`; empty of profiles; catalog-home authority unresolved |

Presence in this map proves only that a path is tracked. It does not establish
adoption, completeness, ownership, validation, a consumer, or operational
maturity.

## Catalog-home conflict and convergence hold

Repository evidence currently supports three simultaneous facts:

1. draft redaction documents commonly point to
   `policy/redaction/profiles.yaml` as a proposed catalog;
2. [`policy/sensitivity/profiles.yaml`](../sensitivity/profiles.yaml) also exists
   as a proposed placeholder; and
3. the Habitat canonical-path document explicitly requires an ADR to choose
   `policy/redaction/`, `policy/sensitivity/`, or a defined split.

Accordingly, this boundary uses the following **convergence hold**:

- do not label either placeholder `canonical`, `active`, `accepted`, or
  production-ready;
- do not add live profile entries to both files or build consumers that merge
  them implicitly;
- do not copy draft examples or exact operational parameters into the
  placeholder as though they were approved;
- do not add a loader, evaluator, transform executor, or public client binding
  until a single authoritative resolution algorithm is accepted;
- route path selection or any deliberate split through an ADR that names one
  writer, compatibility rules, migration order, consumer cutover, correction,
  and rollback; and
- preserve the superseded file and Git history as lineage rather than
  silently deleting or repurposing them.

This is a contributor-safety hold, not a claim that an ADR has already selected
this directory. A path-resolution change must update every normative link,
schema reference, fixture, validator, workflow, package, application, release
gate, and generated projection that relies on the prior location.

## What belongs here

Only after the catalog-home conflict is resolved, this boundary may contain
reviewed, versioned policy source whose primary responsibility is naming and
constraining protective-transform profiles, including:

- stable profile identifiers, versions, lifecycle state, effective windows,
  digests, and supersession links;
- transform-class declarations and public-safe output constraints;
- sensitivity, purpose, audience, geography, temporal, precision, and
  operation applicability;
- explicit required inputs and fail-closed behavior for missing, stale,
  revoked, mismatched, or unresolved context;
- parameter-classification and withholding rules that prevent reversal or
  inference from public artifacts, logs, reasons, or receipts;
- determinism, canonicalization, replay, verifier, synthetic-vector, and
  cross-implementation parity obligations;
- public-safe reason codes and review, receipt, correction, reprocessing,
  withdrawal, or escalation obligations; and
- links to accepted semantic contracts, machine schemas, fixtures, tests,
  evaluators, transform implementations, consumers, release gates, and
  rollback procedures.

A profile belongs here because it is **policy-selected configuration for a
protective transform**. It does not belong here merely because a document,
domain, package, test, UI, or receipt mentions redaction.

## What is prohibited

| Prohibited material or claim | Owning surface or required action |
|---|---|
| Sensitivity labels, assessments, claim truth, rights, consent, source-role, review, release, or correction instances | Their accepted contracts and governed record lanes; a profile may consume references but cannot create these facts |
| Semantic definition of a profile, receipt, review, decision, or release object | [`contracts/`](../../contracts/README.md) |
| JSON Schema, DTO, generated type, or machine-shape authority | [`schemas/`](../../schemas/README.md) |
| Transform executor, profile loader, evaluator, API, cache, storage, UI, deployment, or authentication code | [`packages/redaction/`](../../packages/redaction/README.md), governed apps, tools, runtime, or infrastructure by responsibility |
| RedactionReceipt, PolicyDecision, ReviewRecord, validation report, proof, release decision, correction, withdrawal, or rollback instance | Governed process, receipt, evidence, review, or [`release/`](../../release/README.md) lanes |
| Reusable synthetic fixtures and conformance tests | [`fixtures/`](../../fixtures/README.md) and [`tests/`](../../tests/README.md), except an explicitly accepted native-policy co-location convention |
| Protected source or output payloads, exact sensitive locations, living-person records, genomic material, private cultural knowledge, or exploit-enabling infrastructure detail | Keep out of Git and public documentation; use authorized restricted systems and public-safe references |
| Secret seeds, salts, keys, credentials, reversal material, hidden thresholds, or parameter combinations that materially weaken protection | Keep out of public policy, reasons, fixtures, logs, receipts, and generated provenance; use accepted secret and restricted-parameter handling |
| Exact operational radii, grids, seeds, thresholds, or algorithms copied from draft examples | Keep in reviewed restricted or public-safe design surfaces only after security/privacy review and acceptance |
| Public-client hiding, styling, clipping, filtering, or AI wording presented as the protection boundary | Enforce before public delivery through governed server-side transforms and released public-safe carriers |
| A valid receipt presented as proof that the transform is sufficient or the output may be released | Require independent policy, validation, review, and release closure |
| A second writable profile catalog, silent merge of catalogs, or hand-maintained mirror | Resolve through the catalog-home ADR and a single-writer migration |
| File presence, YAML validity, a workflow pass, PR approval, or prose presented as activation | Activation requires accepted authority, implementation, tests, consumer binding, and accountable review evidence |

Existing placeholders do not authorize prohibited writes. If legacy or draft
content conflicts with this separation, classify and migrate it through a
separately reviewed change that preserves lineage and names consumer repair,
correction, and rollback.

## Object and decision boundaries

Redaction touches several objects and transitions that must remain distinct.

| Object or surface | Question it owns | Relationship to this boundary |
|---|---|---|
| Sensitivity label or assessment | What is protected, at what tier, for which audience and context? | Profile selection may consume it; a profile cannot create or downgrade it. |
| Policy decision | Is a named operation allowed, denied, held, restricted, or unresolved under exact policy context? | May select or require a profile; selection is not transform execution. |
| Redaction profile | Which versioned protective-transform obligations and constraints apply? | Candidate source responsibility of this lane only after the path is accepted. |
| Transform implementation | How are explicit protected inputs transformed under the selected profile? | Belongs to reviewed executable code, not YAML or documentation. |
| Transform result | What derivative and public-safe metadata did one execution produce? | Must remain bound to inputs, implementation, profile, time, and digests. |
| RedactionReceipt | What transform is declared to have occurred, under which profile and support references? | A receipt records execution claims; it does not select policy, expose hidden parameters, or authorize release. |
| Validation report or proof | Did bounded structural, deterministic, parity, leak, and output checks pass? | Supports review; does not establish rights, sufficient protection, or release authority. |
| Review record | What did an authorized reviewer decide about a bounded subject? | May support profile acceptance or output review; it is not the profile or release decision. |
| Release manifest and decision | Which exact derivative is approved for which audience and lifecycle transition? | Consumes exact policy, receipt, validation, and review references; owned by [`release/`](../../release/README.md). |
| Published carrier | What immutable public-safe object was actually delivered? | Must derive from the approved artifact; never from an ungoverned preview or profile declaration. |

Redaction is not declassification by itself. A transformed result retains the
most restrictive applicable handling until an accepted assessment, policy,
validation, review, and release path determines otherwise.

## Inputs and outputs

### Candidate profile-selection inputs

A mature selector must receive explicit, normalized, versioned context rather
than silently fetching or inferring missing facts. Depending on the accepted
policy family, inputs may include:

- operation, purpose, actor or caller, audience, requested exposure, and
  effective time;
- stable subject and source references, input version or digest, domain,
  geography, temporal scope, and requested precision;
- sensitivity label or assessment, join and re-identification risk, and
  source-role constraints;
- rights, license, consent, revocation, sovereignty, embargo, and permitted-use
  posture;
- evidence, validation, review, release-candidate, correction, withdrawal, and
  rollback references where material;
- exact catalog ID, version, digest, accepted home, selector entrypoint, and
  evaluator version; and
- available transform implementation and verifier identities with compatible
  versions and public-safe capabilities.

**Current limitation:** `profiles.yaml` defines no accepted profile-selection
input contract and no current code in this lane consumes these fields. The list
above is an authoring burden, not implementation evidence.

### Source and evaluated outputs

Authoring in this directory may eventually produce versioned profile policy
source and local documentation. Those source artifacts are not evaluated
decisions or transformed data.

An accepted selector may produce a profile reference, version, digest,
public-safe reasons, and obligations. It must preserve finite outcomes such as
selected, denied, held, abstained, or errored according to an accepted outward
contract. It must not collapse missing context or evaluator failure into a
profile selection.

This boundary emits no protected payload, transformed derivative,
RedactionReceipt, validation report, review record, release decision, or public
artifact.

## Candidate profile authoring contract

The following is a **proposed minimum envelope** for future accepted profiles.
It deliberately avoids operational parameter values.

| Field family | Required burden | Safety constraint |
|---|---|---|
| Identity | Stable profile ID, semantic version, exact digest, lifecycle state, effective time, and supersession lineage | Identity must not be inferred from a filename or mutable alias alone. |
| Scope | Applicable operations, domains, sensitivity classes, audiences, purposes, geographies, time ranges, and output forms | Unsupported or ambiguous scope must hold or deny. |
| Transform declaration | Ordered transform classes and public-safe method reference | The profile must not embed executable code or imply implementation equivalence. |
| Input requirements | Required labels, rights, consent, source-role, review, precision, and risk context | Missing, stale, revoked, or mismatched context must not fall back to a weaker transform. |
| Output constraints | Maximum public-safe precision, field/geometry restrictions, aggregation or suppression obligations, and residual-risk posture | A transform must not promise zero risk or automatic declassification. |
| Parameter handling | Public, internal, restricted, or secret classification; source of truth; access rule; receipt/log projection | Public artifacts must omit reversal-enabling or protection-weakening material. |
| Determinism and replay | Canonical input rules, implementation identity, deterministic/replay posture, and allowed nondeterminism | Replay support must not require publishing hidden material. |
| Verification | Verifier ID/version, synthetic vectors, negative cases, leak checks, parity requirements, and resource bounds | A green fixture test proves only its declared profile and must use non-sensitive data. |
| Decision and receipt binding | Selector policy reference, reason and obligation vocabulary, receipt requirements, and hidden-parameter posture | Receipt validity is not policy sufficiency or release approval. |
| Review and acceptance | Accountable steward roles, independent security/privacy review where required, acceptance record, and effective date | CODEOWNERS or PR approval alone must not be treated as profile acceptance. |
| Correction and rollback | Prior version, affected-output discovery, re-evaluation trigger, withdrawal/correction posture, and rollback target | Never overwrite history or silently reuse an ID for changed semantics. |

Profile aliases, if allowed, must resolve deterministically to one immutable
version at evaluation time. Mutable aliases must never be the sole identity in
a receipt, proof, review, or release record.

## Fail-closed, hold, and abstain posture

For unresolved catalog authority, profile identity, sensitivity, rights,
consent, source role, evidence, review, implementation compatibility,
parameter protection, output safety, release state, correction state, or
replay integrity, the safe posture is to **deny, hold, abstain, withhold,
generalize, suppress, quarantine, or route to authorized review** under an
accepted operation-specific contract. Errors must not fall back to pass-through
or to the least restrictive profile.

In particular:

- a missing, unknown, deprecated, revoked, stale, or digest-mismatched profile
  is not usable;
- a profile that does not cover the exact purpose, audience, scope, and output
  form is not reusable by analogy;
- an unavailable executor or verifier is not permission to skip transformation
  or validation;
- unresolved parameter classification is not permission to expose parameters;
- an apparently public output is not releasable when supporting rights,
  consent, review, or release state is unresolved;
- selector, executor, validator, receipt, or storage errors must preserve the
  restrictive posture and avoid leaking protected values in diagnostics; and
- any explicit pass-through profile, if ever accepted, requires the same exact
  policy, evidence, sensitivity, review, receipt, and release bindings as a
  transforming profile.

This is a governance and authoring requirement. The current placeholder does
not enforce it.

## Policy selection, transform execution, and release

| Stage | Owning responsibility | What this boundary may eventually supply | What it cannot do |
|---|---|---|---|
| Sensitivity and prerequisite context | Accepted contracts, assessments, evidence, rights, consent, and review mechanisms | Declare required input references and fail-closed preconditions | Create or repair missing facts |
| Profile source | `policy/redaction/` or the ADR-selected catalog home under [`policy/`](../README.md) | Hold one reviewed, versioned catalog and its local boundary documentation | Self-select its canonical path or activate itself |
| Policy selection | Accepted evaluator and selector | Supply exact catalog bytes, profile identities, reasons, and obligations | Authenticate actors, silently fetch context, or transform data |
| Transform execution | Accepted implementation such as a future [`packages/redaction/`](../../packages/redaction/README.md) consumer | Supply an immutable selected profile reference and constraints | Execute code, open restricted input, or write outputs from YAML |
| Receipt and validation | Governed receipt writer, validators, tests, and proof lanes | Require exact profile, implementation, input/output, support, and hidden-parameter bindings | Prove sufficiency, truth, rights, consent, or review merely from schema validity |
| Public enforcement | Governed APIs, pipelines, tile/export builders, and immutable public-safe carriers | Constrain server-side behavior after acceptance | Rely on browser filters, map styling, UI labels, or AI explanation as the control |
| Release and correction | [`release/`](../../release/README.md) plus accountable evidence, review, receipt, proof, and propagation mechanisms | Supply one bounded policy input and re-evaluation obligations | Approve, promote, release, publish, correct, withdraw, or roll back by itself |

A successful YAML parse, metadata check, schema validation, fixture run,
workflow, pull request, or merge is evidence about that bounded check only. None
is an operational policy decision or release authorization.

## Exposure, mutation, and retention

| Dimension | Boundary contract |
|---|---|
| Repository visibility | The repository is public, so tracked profiles and documentation are publicly readable. Never commit protected payloads, hidden facts, secret material, or reversal-enabling parameters. |
| Operating exposure | The root registry classifies `policy/` as internal. Normal clients consume governed decisions and released public-safe outputs, not repository catalogs or policy source. |
| Mutation | Versioned and review-bound. Material semantic or parameter changes require a new immutable version, digest, effective time, compatibility statement, tests, review, supersession, and rollback plan. |
| Retention | Durable policy source and Git history. Decision instances, receipts, proofs, review records, release records, and protected payloads retain under their owning roots and policies. |
| Parameter storage | Public-safe declarations may live here only after classification and review. Restricted or secret parameter material belongs in authorized systems with stable governed references. |
| Generation | Generated or scaffolded profiles remain proposed until provenance, deterministic regeneration where applicable, review, schema, fixtures, validators, evaluator binding, and consumer evidence exist. |
| Logging and telemetry | Use public-safe identifiers, digests, reason codes, and bounded error classes. Never log protected input, exact sensitive output, hidden parameters, seeds, credentials, or reconstructive intermediate state. |
| Caching | Cache keys and entries must bind profile version/digest, input identity, relevant decision context, implementation, and correction state. Revocation or supersession must invalidate affected material. |

## Related contracts, schemas, fixtures, tests, and workflows

| Family | Current linked evidence | Boundary and maturity |
|---|---|---|
| Parent policy authority | [`policy/README.md`](../README.md) | Canonical policy-source root and inherited non-effects. |
| Adjacent sensitivity boundary | [`policy/sensitivity/README.md`](../sensitivity/README.md) and [`profiles.yaml`](../sensitivity/profiles.yaml) | Proposed sensitivity source plus a parallel catalog placeholder; does not settle redaction catalog authority. |
| Adjacent geoprivacy boundary | [`policy/geoprivacy/README.md`](../geoprivacy/README.md) | Separates policy selection and transform receipts from public-client hiding; its evaluator binding remains unresolved. |
| Catalog path evidence | [Habitat canonical paths](../../docs/domains/habitat/CANONICAL_PATHS.md) | Explicitly records the catalog-home ADR as open. |
| Profile and determinism design | [Redaction Profiles](../../docs/standards/REDACTION_PROFILES.md) and [Redaction Determinism](../../docs/standards/REDACTION_DETERMINISM.md) | Draft/proposed standards containing illustrative design. They are not accepted profile values or runtime proof. |
| Sensitivity doctrine | [`docs/doctrine/sensitivity.md`](../../docs/doctrine/sensitivity.md) | Draft doctrine and candidate mapping context; concrete paths and operating details remain proposed. |
| Receipt meaning | [shared RedactionReceipt contract](../../contracts/shared/redaction_receipt.md) | Draft semantic authority candidate. A receipt records a declared transform and cannot self-authorize release. |
| Receipt machine profile | [source/adaptation map](../../docs/intake/exploratory/redaction-receipt-v1-source-map.md), [schema](../../schemas/contracts/v1/receipts/redaction_receipt.schema.json), and [fixtures](../../fixtures/contracts/v1/receipts/redaction_receipt/cases.json) | `PROPOSED_INACTIVE`, closed, fixture-only declaration profile with all operational authority flags false. |
| Receipt validation | [validator](../../tools/validators/receipts/validate_redaction_receipt.py), [tests](../../tests/validators/test_validate_redaction_receipt.py), and [read-only workflow](../../.github/workflows/redaction-receipt.yml) | Deterministic fixture polarity and leak/non-effect checks; no policy execution, geometry/content transform, restricted-input access, or release. |
| Transform implementation | [`packages/redaction/README.md`](../../packages/redaction/README.md) | Greenfield `0.0.0` package boundary with no supported API or functional core. |
| Preview consumer | [`apps/explorer-web/README.md`](../../apps/explorer-web/README.md) | Fixture-first public-safe preview surface; not a profile resolver, executor, or enforcement boundary. |
| Release authority | [`release/README.md`](../../release/README.md) | Owns accountable release, correction, withdrawal, and rollback decisions. |

Multiple repository schema families currently contain RedactionReceipt-like
shapes. The linked receipt schema is the closed fixture-only profile for its
declared packet; this README does not claim it has resolved all shared versus
domain-extension compatibility or canonical-schema questions.

## Validation coverage and limits

| Validation surface | What a green result establishes | What it does not establish |
|---|---|---|
| Markdown structure and link checks | This README is structurally readable and its checked relative links resolve | Profile correctness, catalog authority, transform safety, or runtime enforcement |
| Metadata validation | The KFM metadata envelope is syntactically acceptable to the checked profile | Document acceptance, steward approval, or registry enrollment unless separately completed |
| Directory-topology unit tests | The validator's policy-boundary README rule behaves as tested | A full repository scan, unrelated baseline closure, or deployment readiness |
| `KFM-TOPO-018` focused state | A populated direct child now has a local README path | Accepted redaction semantics or operation |
| RedactionReceipt schema and fixtures | The fixture-only receipt declarations match a closed proposed profile, including negative polarity | An actual transform, sufficient protection, authenticated review, release, or publication |
| Generated-work receipt validation | This documentation artifact is bound to declared generation inputs and citations | Truth of every claim, human approval, or policy activation |
| Secret and sensitive-content scan | No checked credential pattern or deliberately prohibited operational value was added | Absence of every possible sensitive inference or leak |

The redaction-receipt workflow is path-scoped to its own schema, fixtures,
validator, source map, and generated receipt. A green or untriggered run must
not be reported as validation of this profile catalog.

The full repository-topology scan may require Git objects not present in a
shallow or partial checkout. If it cannot run without fetching, report it as
**NOT RUN / BLOCKED** rather than inferring a pass from unit tests or a baseline
diff.

## Contributor contract

Before changing this boundary or its catalog candidate:

1. **Classify the change.** Distinguish documentation, path-resolution,
   profile semantics, parameter changes, schema, evaluator, executor,
   consumer, receipt, release, correction, and migration work.
2. **Respect the convergence hold.** Do not populate parallel catalogs or
   silently choose a home. Path authority requires the catalog-home ADR and a
   single-writer migration plan.
3. **Keep protected material out of Git.** Use synthetic or public-safe
   examples. Do not paste operational parameters, hidden values, secret seeds,
   exact sensitive locations, restricted inputs, or reconstructive outputs.
4. **Separate authorities.** Put meaning in contracts, shape in schemas,
   reusable mechanics in packages, tests in tests/fixtures, receipts in their
   governed lane, and release decisions under `release/`.
5. **Define non-effects.** State what the profile, evaluator, executor,
   validator, workflow, UI, and receipt cannot authorize or mutate.
6. **Bind identity.** Use immutable versions and digests for catalog, profile,
   evaluator, implementation, inputs, outputs, validation, review, and release
   references.
7. **Test failure behavior.** Cover missing, unknown, stale, revoked,
   superseded, mismatched, unsupported, malformed, leaking, nondeterministic,
   and resource-exhaustion cases with synthetic material.
8. **Plan correction.** Name affected-output discovery, cache invalidation,
   re-evaluation, reprocessing, notice, withdrawal, supersession, and rollback
   behavior before acceptance.
9. **Record generation provenance.** Follow [`CONTRIBUTING.md`](../../CONTRIBUTING.md)
   and validate the generated-work receipt for AI-assisted artifacts.
10. **Do not overclaim checks.** Report exact commands, scope, result, and
    limitations. Hosted checks remain pending until GitHub reports them.

Changes that affect profile semantics or protection strength require review by
the accountable policy, sensitivity/privacy, domain, implementation,
validation, security, and release roles defined by accepted governance. A
single CODEOWNERS route does not prove that separation.

## Correction, supersession, revocation, and rollback

Redaction changes can affect already produced derivatives, caches, tiles,
exports, search indexes, releases, and downstream copies. Profile history must
therefore remain append-only and reviewable.

For a material profile correction:

1. hold new selection and release when the safety impact is unresolved;
2. identify the exact affected profile versions, catalog digests,
   implementations, inputs, receipts, validations, reviews, manifests,
   releases, caches, and public carriers;
3. preserve the prior profile and mark its lifecycle state without rewriting
   history or reusing its immutable identity;
4. publish a corrected or superseding version with explicit compatibility,
   effective time, rationale, and rollback target;
5. re-evaluate and, where authorized, re-run transforms and validators against
   the corrected version;
6. route affected releases through governed correction, withdrawal, notice,
   replacement, cache invalidation, and propagation mechanisms; and
7. verify downstream convergence before closing the incident or migration.

Rollback means restoring a previously reviewed catalog and implementation
state **only when that state remains safe and applicable**. If the prior state
is itself unsafe or rights/consent have changed, the correct response is hold,
withdrawal, or a new corrected profile—not mechanical reversion.

Current repository evidence does not establish complete affected-output
discovery, revocation propagation, cache invalidation, withdrawal, or rollback
drills for this lane. Those capabilities remain **NEEDS VERIFICATION**.

## Open verification register

| ID | Open item | Closure evidence required | Safe posture until closed |
|---|---|---|---|
| REDACT-001 | Which path is the accepted profile catalog home, or what exact split is allowed? | Accepted ADR, root projection update if needed, one-writer rule, migration and rollback plan | `HOLD`; do not populate parallel catalogs |
| REDACT-002 | Who owns profile semantics, privacy/security review, acceptance, and independent approval? | Accepted stewardship and authority assignments with subject and scope binding | Do not infer from CODEOWNERS |
| REDACT-003 | What is the accepted local scope identifier? | Governed registry or contract entry | Use repository path only; do not invent a URI |
| REDACT-004 | What semantic contract and schema define a profile and its lifecycle? | Accepted contract, closed schema, compatibility rules, fixtures, validator, and tests | Treat current YAML as a placeholder |
| REDACT-005 | Which parameters may be public, internal, restricted, or secret? | Threat model, classification rules, security/privacy review, projection and logging rules | Withhold unresolved operational values |
| REDACT-006 | How are catalog, profile, selector, evaluator, and implementation versions bound? | Accepted immutable identity and digest contract with replay tests | No activation or mutable-alias-only binding |
| REDACT-007 | Which transform implementations and verifiers are accepted? | Supported APIs, deterministic vectors, negative/leak/parity tests, supply-chain review, and consumer evidence | No operational transform claim |
| REDACT-008 | How does the selector preserve deny, hold, abstain, error, and obligations? | Accepted input/output contract, normalization mapping, decision receipt, and tests | Fail closed; no boolean shortcut |
| REDACT-009 | How do shared and domain RedactionReceipt schemas interoperate? | Accepted extension/convergence ADR, closed schemas, fixtures, validators, and migration | Do not claim one schema resolves all families |
| REDACT-010 | Which governed component consumes profile selection and writes receipts? | Exact application/package binding, auth, restricted-input controls, observability, replay, and tests | No consumer or writer claim |
| REDACT-011 | How are profile changes propagated to prior derivatives and releases? | Dependency index, re-evaluation/reprocessing process, correction/withdrawal evidence, cache invalidation, and drills | Hold affected outputs when impact is unknown |
| REDACT-012 | Which checks are required before merge and activation? | Branch-protection evidence, workflow triggers, required checks, review rules, and acceptance record | Report local and hosted checks separately |

Until these items close, the only supportable repository claim is that
`policy/redaction/` is a documented, proposed, inactive candidate policy
boundary with one empty placeholder and unresolved catalog authority.

[Back to top](#top)
