# Focus Mode Runtime Policy Boundary

> Path: `policy/focus/`
>
> Document ID: `kfm://policy/focus`
>
> Version: `v0.2`
>
> Status: `DRAFT — repository-grounded; documentation-only; executable Focus policy not established`
>
> Truth label: `PROPOSED`
>
> Last reviewed: `2026-07-22` against `main@8db841822c111cb5b6477003dc72f0455f6c41ad`

This directory is the intended policy boundary for admitting a Focus Mode request and for deciding whether a Focus Mode response may cross the Kansas Frontier Matrix trust membrane. It does not establish that those decisions are currently evaluated or enforced.

## Purpose

Focus Mode turns a bounded user question and governed map context into one finite public outcome. Policy in this directory is intended to decide whether that operation may proceed, which evidence and citation obligations apply, and whether the resulting response is admissible for its audience and release context.

The boundary is evidence-first and fail-closed:

- citations point to governed evidence; they are not decoration;
- an AI-generated statement is never promoted into proof merely because it is fluent;
- missing, stale, conflicting, unauthorized, or insufficient evidence produces a non-answer outcome;
- sensitive facts, exact locations, restricted rights, and consent state are evaluated before disclosure;
- public delivery is limited to finite, schema-valid outcomes;
- policy returns decisions and obligations; it does not silently repair evidence or invent authority.

This README replaces the former greenfield stub. It is a directory contract and implementation guide, not an executable ruleset, accepted ADR, API contract, release approval, or claim of runtime readiness.

## Authority level

`policy/` is the repository's canonical singular home for allow, deny, restrict, abstain, redaction, sensitivity, promotion, and release decisions. This sublane is therefore the intended home for Focus-specific admissibility rules that cannot be expressed solely by a more general policy family.

The placement is supported by the existing `policy/focus/` path and the policy-root ownership rule. It remains bounded by three unresolved facts:

1. the live Directory Rules also describe Focus Mode under the runtime-policy lane;
2. multiple Directory Rules copies are present and their canonical placement is unresolved;
3. relevant ADRs are proposed or draft, not accepted decisions.

Until those facts are resolved, do not create a parallel Focus policy root, duplicate the same decision rule under `policy/runtime/`, or treat this README as an ADR. General access, sensitivity, consent, evidence, release, promotion, and runtime-envelope rules remain owned by their canonical policy families. Focus policy composes those decisions; it does not supersede them.

### Authority order used for this revision

This README applies the repository authority order documented in the live Directory Rules:

1. non-negotiable KFM invariants;
2. accepted ADRs, if any;
3. Directory Rules;
4. canonical root and sublane READMEs;
5. implementation dossiers and architecture notes;
6. observed repository state.

No accepted Focus-specific ADR was established in the reviewed snapshot. Architecture and contract documents cited below are therefore design context unless their own status says otherwise.

## Status

### Evidence boundary

The following statements are confirmed only for the pinned review snapshot.

| Area | Observed state | Consequence |
|---|---|---|
| This README | Former four-line greenfield stub | This revision documents the boundary but adds no enforcement. |
| `focus_request.rego` | Proposed scaffold; `default allow := false`; no admission rules | It does not implement request policy. |
| `focus_response.rego` | Proposed scaffold; `default allow := false`; no response rules | It does not implement response policy. |
| `citation_validation_required.rego` | Proposed scaffold; `default deny := false`; no active deny rules | It does not enforce citation validation. |
| `finite_envelope_required.rego` | Proposed scaffold; `default deny := false`; no active deny rules | It does not enforce a finite response envelope. |
| Policy runtime | Package and bundle lanes report placeholder/readiness-only status | No repository-grounded evaluator or active Focus bundle was established. |
| Focus contracts | Detailed proposed documentation exists | Documentation does not prove a mounted API route or running behavior. |
| Focus schemas | `focus/` and `ui/` schema families overlap and remain permissive stubs | Schema authority and migration are `CONFLICTED / NEEDS VERIFICATION`. |
| Policy decision schema | Concrete proposed four-outcome shape exists; `focus` is not an allowed `policy_family` value | A Focus-specific policy family must not be emitted without a reviewed schema/contract change. |
| Focus fixtures | README and placeholder only | No Focus-local request/response proof suite was established. |
| Focus workflow | Explicit readiness hold and static scaffold checks | A green workflow does not prove evaluated Focus policy. |
| General policy workflow | Static readiness checks; no evaluator or decision emission | A green workflow does not prove runtime enforcement. |

### Truth labels

Use these labels when describing Focus policy evidence:

- `CONFIRMED`: directly supported by inspected repository artifacts at the pinned commit.
- `PROPOSED`: documented intent or scaffold without complete executable proof.
- `INFERRED`: a clearly identified conclusion derived from multiple confirmed facts.
- `CONFLICTED / NEEDS VERIFICATION`: competing paths, shapes, or authority claims have not been reconciled.

Do not collapse `PROPOSED` into `CONFIRMED`. In particular, the presence of a Rego file, contract document, JSON Schema, fixture README, or workflow name is not proof that a policy decision is evaluated in the governed API.

### Current maturity statement

The repository contains enough design material to specify an intended Focus policy boundary, but not enough executable evidence to declare it active. The current maturity state is:

- directory contract: documented by this README;
- rule scaffolds: present but incomplete;
- schema and contract authority: proposed and partly conflicted;
- evaluator and bundle selection: not established;
- Focus-local fixtures: not established;
- end-to-end four-outcome proof: not established;
- public release authority: not established by this directory.

## What belongs here

Only Focus-specific policy material belongs in `policy/focus/`, including:

- request-admission rules for bounded Focus operations;
- response-admission rules applied after evidence resolution and model adaptation;
- requirements that citations be present, resolvable, audience-safe, and sufficient;
- requirements that output use a finite governed envelope;
- Focus-specific obligations that compose canonical evidence, access, sensitivity, consent, rights, promotion, release, and correction decisions;
- Rego tests colocated with the rules they exercise, once the test convention is accepted;
- a small index of Focus policy packages, entrypoints, bundle membership, and implementation status;
- migration notes when a proposed Focus rule moves into a more general canonical policy family.

Every executable artifact added here must identify its inputs, decision shape, failure behavior, tests, bundle/evaluator path, and consuming trust-membrane stage.

## What does NOT belong here

Do not place the following in this directory:

- prompt templates, model weights, model routing, or adapter implementation;
- evidence records, source documents, citation payloads, or generated answers;
- canonical request, response, runtime-envelope, receipt, or evidence schemas;
- UI components, map interaction code, or direct browser-to-model calls;
- secrets, credentials, private endpoints, or deployment configuration;
- sensitivity classifications, rights grants, consent records, or release approvals as data;
- raw or work-state data made public by convenience;
- policy-engine binaries, bundle registries, or runtime orchestration code;
- duplicate rules already owned by canonical access, evidence, sensitivity, consent, release, promotion, or runtime policy lanes;
- speculative policy family names or outcome values that current reviewed schemas do not admit.

Focus policy may reference governed records by stable identifier. It must not copy protected payloads into policy decisions, logs, fixtures, receipts, or documentation.

## Inputs

### Minimum evaluation context — proposed

Before implementation is considered complete, a Focus policy evaluation should receive a versioned, schema-valid input bundle whose fields are sufficient to decide the following without hidden runtime state:

| Input class | Minimum semantics | Fail-closed condition |
|---|---|---|
| Operation | Focus operation identifier, request ID, contract version, and evaluation timestamp | Missing or unknown operation/version |
| Actor and audience | Authenticated or anonymous role, tenant/project scope if applicable, and public/internal audience | Missing role or audience where policy differs |
| Question scope | Bounded question, requested geography, time horizon, domain, and interaction intent | Unbounded or unsupported scope |
| Map context | Governed feature, layer, viewport, selection, or place references | Raw payload substituted for governed references |
| Evidence resolution | Eligible evidence references, truth labels, lifecycle/release state, source lineage, and freshness | No sufficient admissible support |
| Citation state | Claim-to-evidence bindings plus validator result and cited-item release eligibility | Missing, unresolved, stale, or unsafe citation |
| Rights and sensitivity | Classification, rights, consent, redaction/generalization, and disclosure decisions | Decision missing, expired, revoked, or denied |
| Runtime controls | Policy bundle/evaluator identity, adapter identity, finite-envelope contract, timeout, and resource bounds | Unknown evaluator, unbounded adapter, or incompatible envelope |
| Correction state | Supersession, correction, withdrawal, and cache invalidation signals | Known correction not applied |

The current `PolicyInputBundle` material is proposed and permissive. The table above is a requirement for future design and testing, not a claim that these fields are machine-enforced today.

### Input handling rules — proposed

1. Pass stable references and decision summaries across the trust membrane; do not expose restricted payloads merely so the model can decide whether they are restricted.
2. Normalize timestamps and policy versions before evaluation.
3. Preserve the distinction between absent, unknown, conflicted, restricted, and false.
4. Reject ambiguous schema versions and unsupported operations.
5. Treat stale consent, rights, release, or correction information as ineligible until re-evaluated.
6. Keep policy evaluation deterministic for the same normalized input, policy bundle, and evaluator version.
7. Record the input hash and policy identity needed for replay without recording sensitive input content.

### Proposed gate sequence

The architecture documents describe a precheck/evidence/model/postcheck flow. This directory refines that intent into eight reviewable gates:

1. **Request admission** — validate operation, schema version, actor/audience, scope, and supported capabilities.
2. **Pre-disclosure policy** — evaluate access, sensitivity, rights, consent, release, and geography-specific restrictions before assembling model context.
3. **Evidence sufficiency** — require eligible, released, current, and appropriately scoped evidence for claims the operation could answer.
4. **Citation closure** — verify that answer claims can be bound to governed evidence and that citations reveal no restricted detail.
5. **Bounded adaptation** — allow only an approved adapter with explicit context, tool, time, and output bounds; policy does not call the model directly.
6. **Envelope validation** — require a schema-valid finite runtime response before rendering or persistence.
7. **Post-generation policy** — re-evaluate citations, leakage, obligations, audience, and release state against the actual candidate response.
8. **Release and correction** — attach required audit/receipt data and recheck supersession or withdrawal before caching or publication.

Failure at any gate must produce an explicit governed outcome. Silent fallback to an uncited answer, raw model text, a privileged data path, or a less restrictive policy version is prohibited.

## Outputs

### Canonical public outcomes

The reviewed runtime-envelope and policy-decision material uses four public outcomes:

| Outcome | Intended use | Minimum rule |
|---|---|---|
| `ANSWER` | A bounded response is admissible | Evidence, citations, rights, sensitivity, release, envelope, and postcheck gates all pass. |
| `ABSTAIN` | The question is permitted but available admissible evidence cannot support a trustworthy answer | Explain the limitation without fabricating support or revealing protected facts. |
| `DENY` | The operation or disclosure is not permitted | Return a safe reason category and no restricted payload. |
| `ERROR` | A technical or integrity failure prevents a trustworthy decision | Fail closed, preserve correlation/replay data, and do not substitute model text. |

`ANSWER` is not equivalent to a model completion. It is the result of a complete governed evaluation.

### Internal decisions and normalization

Architecture notes and policy documents also discuss engine-native values such as `ALLOW`, `RESTRICT`, and `HOLD`, and validator states such as `PASS` and `FAIL`. These are not additional public outcomes unless the accepted runtime contract and schemas are revised.

Until normalization is formally accepted:

- `ALLOW` may lead to `ANSWER` only after all downstream gates pass;
- `RESTRICT` must become enforceable obligations or a non-answer outcome; it must not silently weaken controls;
- `HOLD` remains an internal review/readiness concept and must not be emitted as a current four-outcome runtime response;
- `PASS` and `FAIL` remain validator results, not user-facing Focus outcomes;
- an unmappable or conflicting engine result becomes `ERROR` or another explicitly authorized fail-closed result.

The current reviewed `policy_decision` schema does not admit `focus` as a `policy_family`. An implementation must use an accepted existing family/profile composition or revise the contract and schema through review. It must not invent `policy_family: focus` in production data.

### Decision obligations — proposed

A policy decision should carry only schema-approved, non-sensitive reason and obligation identifiers. Candidate obligations include:

- bind every material answer claim to a validated evidence reference;
- show evidence access through the governed evidence-drawer path;
- generalize or redact geography, coordinates, identity, or timing;
- omit fields or layers that are not audience-eligible;
- include limitation, freshness, attribution, or correction notices;
- prohibit caching, export, sharing, or downstream promotion;
- require human review before release;
- emit a generated receipt and policy-decision reference;
- invalidate a prior answer after correction, withdrawal, rights change, or consent revocation.

These are vocabulary requirements, not confirmation that the current policy-decision schema, evaluator, or clients support each obligation.

### Trust-membrane behavior

The governed API is the decision boundary. A compliant Focus flow must not permit:

- UI-to-model direct calls;
- model access to raw or work-state stores;
- model-selected policy bundles or audience roles;
- evidence retrieval that bypasses access, rights, sensitivity, consent, release, or correction checks;
- rendering of raw model output before envelope and post-generation validation;
- an answer becoming evidence solely through storage, citation, repetition, or model confidence.

Policy output is a decision plus obligations. Evidence resolution, model adaptation, rendering, persistence, release, and correction remain separate governed responsibilities.

### Sensitivity, rights, and consent

Sensitivity and rights are independent dimensions. Consent is necessary where required, but it is not sufficient to authorize disclosure. A Focus answer must satisfy the most restrictive applicable decision across classification, access, consent, rights, release, and audience context.

Default-deny treatment is required for exact locations or attributes involving sensitive habitats, cultural resources, private persons, private property details, protected infrastructure, embargoed field work, or other controlled classes. Safer generalized answers are allowed only when an accepted policy explicitly authorizes the transformation and the transformed result is revalidated.

Denials and abstentions must not leak the protected fact through reason text, citation metadata, map geometry, counts, timing, cache keys, or differential behavior.

## Validation

### What the current repository validates

At the pinned snapshot:

- `focus-mock-test.yml` performs static readiness checks and intentionally holds while Focus policy, schemas, fixtures, adapter, and command paths remain scaffolds;
- `policy-test.yml` performs static readiness checks and reports that no policy evaluator, accepted bundle, Rego test modules, or evaluated policy-decision suite is established;
- `make policy` is described by the workflow as a TODO/echo target, not a policy test;
- the Focus fixture lane contains documentation and a placeholder, not a complete executable matrix;
- the current workflows do not prove that a governed API evaluates these Focus rules.

Do not report these readiness checks as runtime policy conformance.

### Minimum implementation validation

Before changing this document's maturity statement to executable, a reviewed implementation must provide:

1. accepted contract/schema authority for Focus requests, responses, policy inputs, decisions, and runtime envelopes;
2. a deterministic evaluator and an explicitly selected, versioned policy bundle;
3. Rego unit tests for every rule and failure branch;
4. schema tests for valid and invalid inputs, decisions, obligations, and envelopes;
5. Focus fixtures covering at least `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
6. negative tests for missing citations, invalid evidence references, stale or corrected evidence, sensitivity leakage, revoked consent, rights denial, malformed envelopes, adapter failure, and policy timeout;
7. integration proof that precheck and postcheck run on the governed API path;
8. tests proving that direct model, raw-store, and unreviewed-publication paths fail closed;
9. deterministic decision/receipt hashes for identical normalized inputs and versions;
10. correction and rollback tests that invalidate affected outputs without deleting historical audit evidence;
11. threat review for workflow permissions, third-party actions, secrets, network use, artifact publication, and fork behavior;
12. human review by the policy owner and the owners of every composed policy family.

### Required fixture matrix

| Case | Expected outcome | Critical assertion |
|---|---|---|
| Released evidence, valid citations, safe audience | `ANSWER` | Every material claim closes to admissible evidence. |
| Insufficient or conflicting admissible evidence | `ABSTAIN` | No unsupported answer is emitted. |
| Sensitive or unauthorized disclosure request | `DENY` | Reason and metadata reveal no protected fact. |
| Invalid envelope, evaluator failure, or unmappable decision | `ERROR` | Raw model output is not rendered. |
| Citation resolves to stale or superseded evidence | non-answer | Correction state is honored. |
| Consent revoked after a prior answer | non-answer plus invalidation | Cached/persisted result is no longer eligible. |
| Generalization obligation present | policy-dependent | Transformation is authorized and revalidated. |
| Direct UI-to-model attempt | blocked | The trust membrane cannot be bypassed. |

## Review burden

Changes to `policy/focus/` have a high review burden because they may affect public claims, sensitive disclosure, model behavior, and auditability.

Every change must include:

- a pinned base commit and exact changed-path inventory;
- placement evidence and ADR/drift preflight;
- a no-loss comparison for revised documentation;
- explicit truth labels for current versus proposed behavior;
- affected contract, schema, bundle, evaluator, fixture, workflow, and consumer references;
- negative-path and rollback evidence proportional to the change;
- a generated receipt for AI-authored material;
- review from the policy CODEOWNER and relevant domain/security/release owners;
- no merge or publication claim until required review and checks are complete.

Documentation-only changes must say so. They do not authorize policy activation, schema migration, deployment, release, or publication.

## Related folders and documents

### Canonical and adjacent repository material

- [`policy/`](../README.md) — canonical policy root.
- [`policy/bundles/`](../bundles/README.md) — policy bundle lane and its current readiness boundary.
- [`policy/decision/`](../decision/README.md) — policy-decision lane.
- [`contracts/ui/focus_request.md`](../../contracts/ui/focus_request.md) — proposed UI request semantics.
- [`contracts/ui/focus_response.md`](../../contracts/ui/focus_response.md) — proposed UI response semantics.
- [`contracts/focus_mode/`](../../contracts/focus_mode/README.md) — proposed Focus Mode contract family.
- [`contracts/policy/policy_input_bundle.md`](../../contracts/policy/policy_input_bundle.md) — proposed general policy input contract.
- [`contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md) — proposed policy decision contract.
- [`contracts/runtime/runtime_response_envelope.md`](../../contracts/runtime/runtime_response_envelope.md) — proposed finite runtime-envelope contract.
- [`schemas/contracts/v1/focus/`](../../schemas/contracts/v1/focus/README.md) — proposed, permissive Focus schema lane.
- [`schemas/contracts/v1/ui/`](../../schemas/contracts/v1/ui/README.md) — overlapping proposed UI schema lane.
- [`schemas/contracts/v1/policy/policy_decision.schema.json`](../../schemas/contracts/v1/policy/policy_decision.schema.json) — reviewed four-outcome decision shape.
- [`schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) — reviewed runtime-envelope shape.
- [`tests/fixtures/focus/`](../../tests/fixtures/focus/README.md) — proposed Focus fixture lane.
- [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) — policy runtime package and current placeholder boundary.
- [`docs/architecture/ui/FOCUS_FLOW.md`](../../docs/architecture/ui/FOCUS_FLOW.md) — proposed client-side flow.
- [`docs/architecture/governed-ai/FOCUS_FLOW.md`](../../docs/architecture/governed-ai/FOCUS_FLOW.md) — proposed governed server-side flow.
- [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) — live placement rules used for this preflight.
- [`docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) — current drift-register lane.
- [`.github/workflows/focus-mock-test.yml`](../../.github/workflows/focus-mock-test.yml) — Focus readiness workflow.
- [`.github/workflows/policy-test.yml`](../../.github/workflows/policy-test.yml) — policy readiness workflow.

Some documents contain historical or proposed paths that are not present in the reviewed snapshot. A link in this section means the target was used as evidence or context; it does not promote that target to accepted authority.

## ADRs

No accepted Focus-specific ADR was established in the reviewed snapshot. The following records are relevant design context but remain proposed or draft:

- ADR-0001 — schema home;
- ADR-0002 — contracts versus schemas;
- ADR-0003 — singular canonical policy root;
- ADR-0004 — governed API trust membrane;
- ADR-0008 — subordinate model runtime;
- ADR-0010 — default deny for sensitive classes;
- ADR-0019 — AI adapter and finite envelopes;
- ADR-0020 — abstention as a first-class outcome;
- ADR-0027 — county Focus control plane;
- ADR-0028 — state-scale Focus scope;
- `ADR-focus-model-adapter-boundary.md` — proposed adapter-boundary scaffold.

Do not cite these records as accepted decisions unless their repository status changes through the governed ADR process. If implementation requires a new policy root, a schema-home decision, a new lifecycle split, a parallel authority surface, or a new public outcome, an accepted ADR is required before activation.

## Last reviewed

- Date: `2026-07-22`
- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Base: `main@8db841822c111cb5b6477003dc72f0455f6c41ad`
- Prior README blob: `f20943b20fa5ac21c4ba7769e3ec14f463685bea`
- Review mode: API-only, read-before-write, documentation scope
- Owner: `OWNER_TBD`; review routing currently identifies `@bartytime4life` for `policy/`

Re-review this README whenever a Focus rule, contract, schema, policy family, public outcome, bundle, evaluator, fixture suite, governed API route, sensitivity class, release rule, or Directory Rules/ADR authority changes.

## Smallest implementation sequence

1. Resolve the authority conflicts for `policy/focus/` versus runtime policy and for the overlapping `focus/` versus `ui/` schemas.
2. Accept or revise the Focus request, response, policy-input, policy-decision, and runtime-envelope contracts and schemas together.
3. Decide how Focus composes existing policy families; add a new family only through reviewed contract/schema governance.
4. Implement deterministic request, citation, response, and envelope rules with fail-closed defaults and explicit reasons/obligations.
5. Add colocated Rego tests and complete four-outcome plus negative-path fixtures.
6. Package and identify an immutable bundle, then implement evaluator and replay/receipt support in the policy runtime.
7. Integrate precheck and postcheck into the governed API; keep adapters and stores behind the trust membrane.
8. Prove end-to-end behavior, correction, revocation, rollback, and no-bypass properties before changing maturity or release status.

## Definition of done

### Documentation boundary

- [x] Purpose and ownership are explicit.
- [x] Current scaffolds are distinguished from executable policy.
- [x] Inputs, outputs, finite outcomes, and trust-membrane obligations are documented.
- [x] Sensitivity, rights, consent, citation, correction, and release concerns are bounded.
- [x] Validation, review burden, related material, ADR status, and re-review triggers are recorded.

### Executable boundary

- [ ] Placement and schema authority conflicts are resolved.
- [ ] Contracts and schemas are accepted and mutually consistent.
- [ ] Focus rules contain complete evaluated logic.
- [ ] Unit, schema, fixture, negative-path, and integration tests pass.
- [ ] An immutable bundle and deterministic evaluator are active on the governed API path.
- [ ] Four-outcome runtime behavior and citation closure are proven end to end.
- [ ] Correction, revocation, rollback, and audit/receipt behavior are proven.
- [ ] Security, policy, domain, and release reviews are complete.

Until every executable item is complete, this directory must remain documented as proposed/scaffolded rather than active.

## Open verification register

| ID | Question | Current label | Close only with |
|---|---|---|---|
| `FOCUS-POL-001` | Is `policy/focus/` the accepted home, or should Focus-specific rules be profiles under runtime/general policy families? | `CONFLICTED / NEEDS VERIFICATION` | Accepted ADR or authoritative Directory Rules update plus migration plan |
| `FOCUS-POL-002` | Which Focus request/response schema family is canonical? | `CONFLICTED / NEEDS VERIFICATION` | Accepted schema-home decision and compatibility plan |
| `FOCUS-POL-003` | How are Focus decisions represented when `focus` is not a policy-family enum value? | `NEEDS VERIFICATION` | Accepted contract/schema composition or reviewed enum change |
| `FOCUS-POL-004` | Which bundle and evaluator own the four rule entrypoints? | `NEEDS VERIFICATION` | Immutable bundle manifest, evaluator identity, tests, and runtime integration evidence |
| `FOCUS-POL-005` | What obligation vocabulary is accepted by the API and clients? | `NEEDS VERIFICATION` | Accepted schema, fixtures, and consumer tests |
| `FOCUS-POL-006` | Which workflow checks are required and branch-protected? | `NEEDS VERIFICATION` | Repository settings evidence plus successful required checks |
| `FOCUS-POL-007` | What exact public route mounts Focus Mode? | `NEEDS VERIFICATION` | Governed API route and integration evidence; architecture examples are insufficient |

## Evidence ledger

| Evidence | Use in this README | Limitation |
|---|---|---|
| Live Directory Rules | Canonical policy-root placement, authority order, README expectations, ADR triggers | The repository reports competing copies and unresolved canonical placement. |
| Existing files in `policy/focus/` | Current scaffold and default-rule observations | File presence does not prove bundle selection or evaluation. |
| Focus UI and governed-AI flow documents | Intended precheck, evidence, bounded adapter, postcheck, and finite-outcome sequence | Both describe proposed implementation. |
| Focus/UI/policy/runtime contracts and schemas | Current request/response/decision/envelope shapes and conflicts | Most are proposed; Focus/UI schemas remain permissive and overlapping. |
| Policy runtime and bundle READMEs | Current lack of an established evaluator/bundle | Documentation could lag implementation; runtime proof remains required. |
| Focus and policy workflows | Explicit readiness holds and static checks | Workflow names or green status are not runtime conformance. |
| Focus fixture README and directory state | Intended test taxonomy and current missing suite | No Focus-local payload matrix was established. |
| ADR records | Design questions and intended governance | Reviewed ADRs are proposed/draft, not accepted authority. |

## Correction, supersession, and rollback

Corrections to this README must preserve the evidence distinction between repository-observed facts and proposed behavior. When an implementation closes an open item, update the status table, open register, validation evidence, and last-reviewed base together.

If this revision is found to overstate authority or current capability, revert this README and its generated receipt as one documentation change. Reverting documentation does not modify runtime policy because this revision adds no executable rules, bundle, evaluator, workflow behavior, schema, contract, release approval, or publication action.
