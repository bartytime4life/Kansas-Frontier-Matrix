<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/arch-trust-membrane
title: Trust Membrane — Architectural Contract and Crossing Model
type: architecture-reference
version: v2.0-draft
status: draft; repository-grounded; case-collision-hold; non-authoritative
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — architecture, evidence, policy, release, and public-client stewardship"
created: 2026-05-06
updated: 2026-08-19
policy_label: public
owning_root: docs/
responsibility: Explain the durable cross-root crossing model that separates internal lifecycle state, release decisions, governed delivery, and public-client behavior without becoming doctrine, policy, release authority, or implementation proof.
truth_posture: CONFIRMED commit-pinned repository evidence / PROPOSED integrated target model / UNKNOWN production enforcement / HOLD on case-colliding document migration
related:
  - README.md
  - TRUST_MEMBRANE.md
  - document-convergence-plan.md
  - governed-api/README.md
  - evidence-drawer.md
  - publication/promotion-gates.md
  - ../doctrine/directory-rules.md
  - ../doctrine/trust-membrane.md
  - ../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags:
  - kfm
  - architecture
  - trust-membrane
  - governed-api
  - evidence
  - policy
  - release
  - public-client
  - correction
  - rollback
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, code, data, release, deployment, or publication effect."
  - "The case-colliding TRUST_MEMBRANE.md sibling remains present and the structural migration remains on explicit HOLD."
  - "This page owns a durable explanatory crossing model; it does not choose a canonical survivor or convert current bounded proofs into operational authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="trust-membrane--architecture"></a>

# Trust Membrane — Architectural Contract and Crossing Model

> **Purpose.** Explain how KFM is intended to move from internal, not-yet-warranted material to governed release and public-safe delivery while preserving evidence, policy, review, correction, and rollback boundaries.

> [!IMPORTANT]
> **Architecture is explanatory, not sovereign.** This page does not define semantic object meaning, machine shape, admissibility, review authority, release state, or publication. Those responsibilities remain with accepted doctrine and ADRs, `contracts/`, `schemas/`, `policy/`, executable implementation and tests, evidence and proof records, and append-only release/correction/rollback records.

> [!CAUTION]
> **The case-colliding sibling remains unresolved.** [`TRUST_MEMBRANE.md`](./TRUST_MEMBRANE.md) and this lowercase page have different document identities, content, and historical fragments but collide on case-insensitive filesystems. The architecture convergence plan proposes an eventual no-loss convergence to one lowercase path; that migration is still **HOLD**. This update neither selects a survivor nor repairs or retires either identity.

## Current bounded result

| Field | Repository-grounded result |
|---|---|
| Evidence snapshot | `main@45fc45556a007196aa29e725f3a4b9fe9af8294e` |
| Prior lowercase blob | `40602152f13044fa87d57c73c71d797f95afa61e` |
| Uppercase sibling blob | `e260a1dbe20ec011901fbe8fb752cd3bb66a9eeb` |
| Placement authority | Accepted ADR-0029 and adopted Directory Rules v2 |
| Current dynamic API surface | Three fail-closed GET scaffolds under `apps/governed-api/` |
| Current successful public answers | None proved; scaffolded routes return `ABSTAIN / NOT_IMPLEMENTED` |
| Current evidence resolver | Internal, no-network, non-authoritative candidate check |
| Current browser integration | Fixture-only governed projection parser; no live API transport proved |
| Current release machinery | Mixed-maturity, fixture-first readiness surfaces; operational release remains held |
| Structural migration | `HOLD` |
| Release or publication effect | None |

**Quick navigation:** [Role](#1) · [Boundary model](#2) · [Enforcement points](#3) · [Crossings](#4) · [Outcomes](#5) · [Gates A–G](#6) · [Anti-patterns](#7) · [Duties](#8) · [Correction](#9) · [Failure modes](#10) · [Placement](#11) · [Validation](#12) · [Backlog](#13) · [Glossary](#14) · [Related docs](#related)

---

<a id="1"></a>

## 1. Architectural role, authority, and scope

KFM's trust membrane is a **distributed architectural composition**, not one file, package, endpoint, validator, or badge. It is the combined boundary through which a claim-bearing or trust-bearing response must pass before a normal client may treat it as renderable.

At minimum, the composition has to keep these responsibilities distinct:

1. **Internal lifecycle state** — source material, candidates, unresolved evidence, quarantine, and processing state.
2. **Evidence and policy evaluation** — support, source role, rights, sensitivity, audience, freshness, review, and obligation checks.
3. **Release governance** — promotion readiness, accountable decision records, correction, withdrawal, and rollback.
4. **Governed delivery** — API or separately governed static delivery of already released public-safe carriers.
5. **Client rendering** — map, Evidence Drawer, Focus Mode, export, search, graph, and other public surfaces that obey the governed result.

The membrane is therefore a boundary of **composed responsibilities**. No one component may silently inherit all five.

### 1.1 What this page owns

This page owns a human-readable architecture model for:

- the two sides of the boundary;
- the two distinct crossings—promotion and exposure;
- the role of finite runtime outcomes;
- the difference between readiness, release, and public rendering;
- the interaction among evidence, policy, review, release, correction, and rollback;
- the failure posture when one dependency is unavailable or unresolved; and
- the repository responsibility roots that participate.

It does **not** own:

- the meaning of `EvidenceRef`, `EvidenceBundle`, `DecisionEnvelope`, `PolicyDecision`, `RuntimeResponseEnvelope`, `PromotionDecision`, or `ReleaseManifest`;
- their JSON Schema shapes;
- executable policy;
- authenticated review or release decisions;
- API routing or deployment;
- public artifact bytes; or
- a decision about the case-colliding document pair.

<a id="1.2"></a>

### 1.2 Doctrine, architecture, decision, and implementation are different evidence classes

| Surface | Current role | Authority limit |
|---|---|---|
| Accepted [Directory Rules v2](../doctrine/directory-rules.md) through [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Placement authority | Does not prove trust-membrane runtime behavior. |
| [`docs/doctrine/trust-membrane.md`](../doctrine/trust-membrane.md) | Repository-present draft trust-language articulation | Presence and polished prose do not establish adoption or enforcement. |
| This page | Durable explanatory crossing model | Does not create doctrine, policy, release, or implementation authority. |
| [`TRUST_MEMBRANE.md`](./TRUST_MEMBRANE.md) | Repository-grounded current architecture and enforcement snapshot | Does not choose the case-collision survivor. |
| [ADR-0004](../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) | Proposed dynamic trust-boundary decision | Source remains draft/effectively proposed; configured code does not imply acceptance. |
| Current code, schemas, tests, workflows, and emitted artifacts | Implementation evidence for their exact scope | A passing fixture or route test does not prove production enforcement. |

### 1.3 Non-negotiable invariants carried into this model

- `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` remains a governance sequence.
- Promotion is a governed state transition, not a file move, commit, pull request, merge, workflow result, or badge.
- Ordinary clients use governed interfaces or already released public-safe artifacts, not canonical/internal stores as their normal path.
- `EvidenceRef` should resolve to admissible evidence before a consequential `ANSWER`.
- Evidence, policy, review, release, correction, and rollback state remain distinguishable.
- Unknown rights, sensitivity, sovereignty, harmful precision, release state, or evidence support fails closed.
- Maps, tiles, graphs, indexes, scenes, dashboards, exports, and generated language remain carriers or interpretations, not sovereign truth.
- A current warrant can be corrected, withdrawn, superseded, or rolled back.

[Back to top](#top)

---

<a id="2"></a>

## 2. Boundary model: two sides, three planes, two crossings

The simplest architectural model has two sides.

### Internal side

Material on the internal side may be legitimate work, but it is not yet warranted for ordinary public rendering:

```text
source edge / pre-RAW
  -> RAW
  -> WORK or QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET candidate state
```

This side may contain source responses, candidates, exact or sensitive values, unresolved evidence, incomplete rights review, model output, draft relations, proposed catalog records, and unreleased artifacts. Location inside the repository does not itself grant access or publication status.

### Governed-delivery side

Material on the governed-delivery side is still bounded. It is not “permanently true”; it is supported for a declared use, audience, precision, time, and release state:

```text
reviewed promotion packet
  -> release decision and manifest
  -> public-safe released carrier or governed runtime response
  -> client rendering with evidence, obligations, and correction state
```

### Three responsibility planes

| Plane | Owns | Must not become |
|---|---|---|
| Internal lifecycle and evidence plane | Source capture, processing, candidate evidence, proofs, receipts, catalog/triplet preparation | A normal public data path |
| Release-decision plane | Promotion, release, correction, withdrawal, rollback, signatures, accountable review records | A payload store or automatic publisher |
| Governed-delivery plane | Runtime envelopes and released public-safe carrier access | Canonical truth, policy source, or hidden release authority |

### Two crossings

The membrane is easiest to reason about when the crossings are separated:

1. **Promotion crossing:** `CATALOG / TRIPLET candidate -> PUBLISHED release state`.
2. **Exposure crossing:** released or policy-safe state -> governed response or public-safe carrier -> client.

A system can have a valid promotion record and still deny a particular caller, audience, precision, export, or render operation. Conversely, a runtime route cannot manufacture release state merely because it returns schema-valid JSON.

```text
INTERNAL LIFECYCLE
  |
  |  Crossing A: evidence + policy + validation + review + release + rollback
  v
RELEASED STATE
  |
  |  Crossing B: caller/surface + evidence resolution + policy + freshness + correction
  v
GOVERNED DELIVERY
  |
  v
PUBLIC CLIENT
```

Every arrow is a responsibility boundary. The diagram is a target composition, not proof that the current repository executes the full chain.

[Back to top](#top)

---

<a id="3"></a>

## 3. Current enforcement points and their exact limits

The repository contains bounded implementation surfaces that protect parts of the membrane. None currently proves the full composition.

| Surface | CONFIRMED bounded behavior | What remains unproved |
|---|---|---|
| [`apps/governed-api/`](../../apps/governed-api/README.md) | WSGI scaffold dispatches three registered GET routes. | Authentication, authorization, accepted policy evaluation, evidence resolution, release binding, deployed isolation, production traffic. |
| [`routes/registry.py`](../../apps/governed-api/src/governed_api/routes/registry.py) | Exact route set is `/bootstrap`, `/layers`, `/evidence`. | Versioned production API catalogue or live consumer integration. |
| [`stub.py`](../../apps/governed-api/src/governed_api/stub.py) | Routes return `ABSTAIN / NOT_IMPLEMENTED`; safe errors avoid detailed leakage. | Any evidence-backed `ANSWER`. |
| API boundary tests | Verify 404/405 behavior, safe error shape, exact route manifest, forbidden renderer/model imports, and selected internal-store literal guards. | Complete information-flow, auth, exfiltration, policy, or deployment proof. |
| [`RuntimeResponseEnvelope`](../../contracts/runtime/runtime_response_envelope.md) and paired schema | Proposed closed four-outcome client envelope; `ANSWER` requires evidence refs and `precision_actually_used`. | Accepted semantics, live route emission, policy-state vocabulary, public-client enforcement. |
| [`DecisionEnvelope`](../../contracts/runtime/decision_envelope.md) | Proposed finite runtime decision record with policy family, reasons, and obligations. | Policy execution, release approval, or transport behavior. |
| [`PolicyDecision`](../../contracts/policy/policy_decision.md) | Proposed semantic record for one policy evaluation event. | Accepted policy bundle, evaluator binding, authenticated authority, operational enforcement. |
| [`packages/evidence-resolver/`](../../packages/evidence-resolver/README.md) | Internal no-network v1alpha1 candidate check over explicit caller-supplied inputs. | Authoritative lookup, claim-scope closure, rights/sensitivity evaluation, public outcome mapping, production consumer. |
| [`GovernedClient.ts`](../../apps/explorer-web/src/adapters/GovernedClient.ts) | Strict fixture-only Evidence Drawer projection parser; no network or lifecycle-store access. | Live Governed API transport or production runtime parity. |
| [`release/`](../../release/README.md) | Canonical append-only release-decision root with multiple fixture-first validation surfaces. | Authenticated operational release, public alias mutation, correction propagation, cache invalidation, deployed rollback. |
| [Promotion-gate readiness validator](../../tools/validators/promotion_gate/README.md) | Deterministic, no-network A–G packet checks with finite results and no writes. | Existence/authenticity of referenced objects, live policy, signatures, release execution, publication. |

### Composition rule

A mature `ANSWER` path must compose these responsibilities without collapsing them:

```text
request and caller context
  -> released-state selection
  -> evidence resolution
  -> policy / rights / sensitivity / audience evaluation
  -> freshness and correction evaluation
  -> precision actually supported
  -> runtime response envelope
  -> client rendering under obligations
```

A current repository component may prove one step. It must not advertise the entire sequence unless the missing steps are also evidenced.

[Back to top](#top)

---

<a id="4"></a>

## 4. Legitimate crossings and crossing preconditions

### 4.1 Crossing A — promotion into released state

A promotion crossing is legitimate only when the candidate is bound to enough evidence and governance for its consequence. The exact required records depend on the profile, but the architecture requires these categories to remain inspectable:

- deterministic candidate and artifact identity;
- source and evidence support;
- validation appropriate to object type;
- rights, sensitivity, audience, and permitted-use posture;
- provenance and integrity records;
- accountable review;
- release decision and manifest;
- correction or withdrawal path;
- rollback target; and
- a record of obligations that downstream delivery must preserve.

A readiness validator may say a declared packet is `APPROVE_READY`. It does not perform the promotion, authenticate the reviewer, or create the release.

### 4.2 Crossing B — exposure to a client

A release does not grant universal exposure. Each request or delivery surface may add constraints:

- caller identity and role;
- requested operation—view, query, export, download, analyze, narrate, or administer;
- audience and purpose;
- requested spatial, temporal, and attribute precision;
- current policy and sensitivity state;
- evidence resolvability;
- freshness;
- correction, supersession, withdrawal, or rollback state;
- obligations such as citation, attribution, generalization, no-export, or review.

The runtime must expose only the precision actually supported and allowed. Client-side hiding, opacity, styling, zoom limits, or collapsed panels are presentation behavior, not protection.

### 4.3 Static delivery is not an escape hatch

A separately governed static edge may serve already released public-safe PMTiles, COGs, GeoParquet, manifests, styles, or similar carriers. It must preserve release identity, integrity, correction state, rights, and rollback obligations. It must not become:

- a second policy authority;
- a direct internal-store path;
- a way to serve unreleased candidate bytes;
- an unsigned mutable alias whose provenance cannot be reconstructed; or
- a public artifact whose source and release binding are invisible.

### 4.4 Administrative and break-glass paths

Operational administration may require access that normal clients never receive. Such access should be:

- authenticated and least-privilege;
- purpose-bound and time-bounded where practical;
- logged without leaking the protected payload;
- separated from normal public routes;
- reviewable and revocable; and
- incapable of silently creating release or publication state.

No administrative shortcut belongs in the ordinary public request path.

[Back to top](#top)

---

<a id="5"></a>

## 5. Finite outcomes and state vocabulary

### 5.1 Public runtime outcomes

The paired runtime response schema currently closes the public outcome vocabulary to four values:

| Outcome | Meaning | Client posture |
|---|---|---|
| `ANSWER` | Evidence, policy, freshness, correction, release, and requested scope support a bounded response. | Render only with evidence refs, precision actually used, and required obligations. |
| `ABSTAIN` | Support is insufficient, stale, unresolved, conflicted, or too broad without proving a prohibition. | Explain the safe limitation; do not infer an answer. |
| `DENY` | Policy, rights, sensitivity, audience, consent, or operation rules prohibit exposure. | Do not render the protected payload; use a safe non-oracular reason. |
| `ERROR` | The governed operation could not complete safely or deterministically. | Fail closed; do not infer truth or permission. |

Unknown or missing outcomes must never default to `ANSWER`.

### 5.2 Internal states are not fifth public outcomes

The repository also uses internal or profile-local vocabulary such as:

- `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`;
- `HOLD`;
- `RESOLVED`, `UNRESOLVED`, `DENIED`;
- `PASS`, `APPROVE_READY`, `BLOCKED`;
- `REVIEWED`, `PENDING`, `WITHDRAWN`, `SUPERSEDED`, `REVOKED`.

These terms describe lifecycle, review, readiness, resolver, release, or history state. They must not be added to a public runtime envelope merely because they are meaningful elsewhere.

### 5.3 Object-family separation

| Object or result | Owns | Does not own |
|---|---|---|
| `DecisionEnvelope` | Finite runtime decision semantics, reasons, obligations, policy family | Policy execution, release, transport |
| `PolicyDecision` | One policy-evaluation record | Runtime response, promotion, publication |
| `RuntimeResponseEnvelope` | Client-facing outcome, evidence refs, state summaries, answer precision | Evidence storage, policy execution, release approval |
| Evidence resolver result | Internal candidate closure result | Public `ANSWER`, rights clearance, release |
| Promotion-gate result | Readiness finding | `PromotionDecision`, release, publication |
| `ReleaseManifest` / release records | Release identity and transition support | Public payload bytes or universal access |

The same words may appear in several families. The family and owning authority determine their meaning.

[Back to top](#top)

---

<a id="6"></a>

## 6. Current bounded promotion gates A–G

The repository's implemented no-network readiness validator uses the following current gate vocabulary:

| Gate | Current name | Bounded checks | Current limit |
|:---:|---|---|---|
| A | Identity and closure | Candidate, author, profile, spec hash, lifecycle boundary, manifest identity | Declared packet consistency only |
| B | Asset integrity | Candidate/manifest/receipt hash agreement and digest-set equality | Does not authenticate external bytes or signatures |
| C | Geometry and CRS | Declared validity, deterministic processing, `EPSG:4326`, bounded world bbox | Does not inspect a live production artifact |
| D | Temporal semantics | Real UTC-second interval and supplied evaluation time | Does not decide domain fitness or currentness |
| E | Rights/sensitivity policy context | Known profile/labels and finite supplied policy result | Does not run an accepted policy evaluator |
| F | Proof and catalog support | Evidence, attestation, STAC/DCAT/PROV, run receipt, conditional AI receipt | Does not dereference or authenticate references |
| G | Review and rollback | Fixture-only review, identity/authority declarations, separation, scope, bindings, correction and rollback links | Does not authenticate actors, assignments, or execute rollback |

The validator returns `PASS`, `ABSTAIN`, `DENY`, or `ERROR`, with precedence `ERROR > DENY > ABSTAIN > PASS`.

> [!IMPORTANT]
> `PASS` means only that the bounded declared packet has no finding under the current profile. It does not mean `APPROVED`, `PROMOTED`, `RELEASED`, `PUBLISHED`, or safe for a public client.

The architecture depends on gate meanings remaining stable and versioned. Changing gate names, order, required inputs, or transition semantics is authority-bearing work and should not be smuggled into an explanatory Markdown edit.

[Back to top](#top)

---

<a id="7"></a>

## 7. Anti-patterns and deny surfaces

The membrane is breached when a normal public path does any of the following:

| Anti-pattern | Why it fails | Required posture |
|---|---|---|
| Browser reads `RAW`, `WORK`, `QUARANTINE`, candidate, or internal evidence stores directly | Bypasses evidence, policy, release, and correction controls | `DENY` and remove the direct path |
| Route returns an `ANSWER` with unresolved or empty evidence support | Converts absence into authority | `ABSTAIN` or `ERROR` |
| Client requests exact sensitive data and hides it with styling | Payload already crossed the boundary | Transform or deny before delivery |
| Search, graph, vector index, or tile service is treated as canonical truth | Derived carrier replaces evidence | Resolve through governed evidence and release state |
| Model output is exposed directly | Generated language bypasses evidence and policy | Governed adapter and envelope only |
| Readiness `PASS` is represented as release | Confuses validation with accountable transition | Keep readiness and release records separate |
| Merge or GitHub release is represented as KFM publication | Repository state is not lifecycle state | Require governed release evidence |
| Denial reasons reveal protected facts | Negative outcome becomes an oracle | Return safe reason families only |
| Error handling falls back to stale or cached `ANSWER` | Failure becomes unsafe success | Fail closed and expose correction/freshness state |
| One service owns evidence, policy, review, release, and client rendering | Eliminates independent checks and audit boundaries | Split responsibilities or record an explicit bounded exception |
| Documentation chooses a canonical survivor while migration evidence is open | Prose performs structural authority | Keep the collision on `HOLD` |

### Cross-surface inference

Protection must cover more than the primary payload. Review must include:

- errors and reason codes;
- feature counts and bounding boxes;
- timing and cache behavior;
- search facets and autocomplete;
- graph neighborhoods;
- map labels, tiles, styles, and source-layer metadata;
- exports and screenshots;
- story and Focus Mode summaries;
- telemetry and logs;
- 3D scenes and terrain-derived views; and
- joins that reconstruct protected precision from public fragments.

A public-safe layer can still be unsafe when combined with another layer. The operation and composition matter, not only each input's label.

[Back to top](#top)

---

<a id="8"></a>

## 8. Separation of duties and review burden

### Current verified review route

The current `.github/CODEOWNERS` routes repository review to `@bartytime4life`. That is a verified GitHub review route, not proof of:

- an authenticated `StewardshipAssignment`;
- independent review;
- policy or sensitivity qualification;
- release authority;
- required code-owner enforcement;
- branch-protection coupling; or
- completed human approval.

### Mature target separation

As KFM matures, policy-significant crossings should separate at least these functions where consequence justifies it:

| Function | Responsibility |
|---|---|
| Producer or transform author | Creates candidate bytes and receipts |
| Evidence reviewer | Checks source role, scope, limitations, and evidence closure |
| Policy/sensitivity reviewer | Evaluates rights, audience, precision, consent, sovereignty, and obligations |
| Release reviewer | Decides whether the candidate may enter a named release state |
| Operator | Executes an authorized transition or rollback |
| Client/runtime owner | Ensures governed outcomes and obligations survive delivery |
| Correction/incident owner | Coordinates withdrawal, replacement, invalidation, and public correction |

One person may temporarily hold multiple roles in a bootstrap project, but the overlap should be visible. A generator, validator, or coding agent must never represent itself as independent approval.

### High-consequence review

Living-person data, genomics, rare species, archaeology, culturally restricted knowledge, private land or wells, critical infrastructure, and harmful precise locations require domain-appropriate review before less restrictive handling. This page does not establish the qualified reviewers or thresholds; those remain policy and stewardship decisions.

[Back to top](#top)

---

<a id="9"></a>

## 9. Freshness, correction, withdrawal, and rollback

Trust is current and bounded, not permanent.

### State and outcome are separate

- A response may be `ABSTAIN` because support is stale.
- A public artifact may be `WITHDRAWN` while the runtime returns `DENY` or `ABSTAIN`.
- A corrected release may support `ANSWER` only through the active replacement evidence.
- A runtime failure may return `ERROR` without changing the underlying release state.

### Required correction path

A material correction should preserve and propagate:

1. prior identity and release lineage;
2. the correction, withdrawal, supersession, or rollback decision;
3. the active replacement or explicit absence of one;
4. evidence and reason references safe for the audience;
5. cache, index, tile, search, graph, export, and AI invalidation requirements;
6. public-facing state and notices;
7. replay evidence; and
8. rollback or forward-fix target.

### Dynamic and static delivery

Dynamic APIs can check correction state on each request. Static carriers require explicit invalidation, alias, manifest, and cache discipline. A static file remaining reachable after withdrawal is not automatically a valid release.

### Current maturity

The repository contains release, rollback, correction, and alias-verification guidance and fixture-first validators. It does not currently prove operational public correction propagation, alias mutation, cache invalidation, or deployed rollback. Those capabilities remain `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="10"></a>

## 10. Failure modes and fail-closed behavior

| Failure | Safe result | Evidence required to graduate |
|---|---|---|
| Evidence reference missing or unresolved | `ABSTAIN` | Governed EvidenceRef-to-EvidenceBundle resolution with admissibility and scope |
| Policy bundle or evaluator unavailable | `ERROR` or `DENY` according to accepted policy contract | Bound accepted evaluator, versioned inputs, negative tests, audit record |
| Rights or sensitivity unclear | `DENY`, `ABSTAIN`, or quarantine | Qualified review, source terms, transform profile, obligations |
| Requested precision exceeds support | Narrow scope or `ABSTAIN`; never invent precision | Evidence-backed `precision_actually_used` and transform receipts |
| Release state missing | `ABSTAIN` or `DENY` | Valid release binding and correction/rollback references |
| Release withdrawn or superseded | Do not render old payload as current | Active correction lineage and invalidation proof |
| API route unavailable | `ERROR` | Safe retry/degradation design that does not bypass the API |
| Static artifact integrity mismatch | `DENY` or `ERROR` | Manifest/digest verification and replacement or rollback |
| Client payload malformed | `ERROR`; render no protected content | Closed parser/schema and negative fixtures |
| Internal store becomes reachable from public path | Incident/containment; `DENY` | Route isolation, auth, tests, logs, and review |
| Validator or workflow fails | Block the claimed transition | Root-cause evidence; never weaken a gate solely to obtain green status |
| Case-collision migration is incomplete | `HOLD` structural change | Identity, content, inbound-link, fragment, consumer, history, and rollback closure |

A system must not turn absence, ambiguity, stale state, or operational failure into a permissive default.

[Back to top](#top)

---

<a id="11"></a>

## 11. Repository placement and responsibility map

### Directory Rules basis

Accepted ADR-0029 makes `docs/doctrine/directory-rules.md` the single writable human Directory Rules authority. This page remains at `docs/architecture/trust-membrane.md` because its primary responsibility is cross-root human explanation.

The same-path update is `PLACE` for documentation purpose. It does not authorize the later structural migration of the case-colliding pair.

### Current responsibility roots

| Responsibility | Current or governing home | Boundary |
|---|---|---|
| Human architecture explanation | `docs/architecture/` | Explanatory only |
| Accepted placement doctrine | `docs/doctrine/directory-rules.md` plus ADR-0029 | Placement authority only |
| Architecture decisions | `docs/adr/` | Proposed or accepted according to each record |
| Semantic meaning | `contracts/` | No executable or release authority |
| Machine shape | `schemas/` | Validation is not approval |
| Policy source | `policy/` | Rules do not publish by themselves |
| Deployable dynamic trust boundary | `apps/governed-api/` | Current scaffold is fail-closed, not complete |
| Public map/client shell | `apps/explorer-web/` | Current governed adapter is fixture-only |
| Reusable evidence candidate logic | `packages/evidence-resolver/` | Internal and non-authoritative |
| Validators | `tools/validators/` | Findings are bounded evidence |
| Synthetic proof inputs | `fixtures/` | Fixtures are not source truth |
| Executable tests | `tests/` and app-local test lanes | Tests prove declared scope |
| Process receipts and proofs | `data/receipts/`, `data/proofs/` | Distinct from decisions and payloads |
| Release decisions | `release/` | Append-only decision plane, not payload store |
| Released public-safe carriers | `data/published/` | Require governed release; path presence alone is insufficient |

### No parallel authority

Do not create another trust-membrane package, policy root, schema home, release root, or public API merely to make the architecture diagram look complete. A missing integration seam should remain explicit until its owner and authority are established.

### Case-collision hold

The current planning direction favors eventual lowercase convergence, but this page does not execute it. Before any rename, deletion, consolidation, or tombstone:

1. freeze a base commit;
2. compare both complete documents;
3. reconcile both `doc_id` values and titles;
4. inventory inbound links, fragments, generators, workflows, and external compatibility;
5. preserve unique governance-significant content;
6. choose a survivor through accountable review;
7. repair references atomically;
8. validate on case-sensitive and case-insensitive expectations; and
9. record rollback.

[Back to top](#top)

---

<a id="12"></a>

## 12. Validation and acceptance evidence

### CONFIRMED bounded validation surfaces

| Surface | Current proof |
|---|---|
| Governed API route tests | Three routes remain deterministic `ABSTAIN`; unknown routes and unsupported methods fail safely |
| Governed API boundary tests | Selected forbidden imports and internal-store path literals are blocked |
| Runtime response schema/validator | Four finite outcomes, closed shape, conditional answer precision, EvidenceRef shape binding |
| Evidence resolver | Synthetic no-network candidate matrix, deterministic result ordering, socket/DNS denial |
| Promotion readiness | Synthetic A–G matrix with PASS/ABSTAIN/DENY/ERROR polarity, no writes, no network |
| Explorer governed projection parser | Strict fixture-only parser, correction-history checks, finite states, no network/lifecycle access |
| Documentation controls | Link, metadata, document-graph, build, and topology workflows exist; exact-head results remain separate evidence |

### Missing integrated proof

The following remain required before claiming an operational trust membrane:

- one authoritative repository-local EvidenceRef-to-EvidenceBundle lookup and scope model;
- accepted policy inputs, bundles, evaluator, reason/obligation vocabularies, and consumer binding;
- authenticated caller and review authority;
- release-bound `RuntimeResponseEnvelope` emission from the dynamic API;
- a real Explorer transport that consumes the governed API without internal-store fallback;
- separately governed static-delivery integrity and correction behavior;
- a complete negative matrix for unauthorized callers, restricted precision, withdrawn releases, stale evidence, policy failure, and upstream outages;
- correction propagation through dynamic responses, caches, tiles, search, graph, exports, and AI;
- deployment isolation, least privilege, telemetry minimization, and operational logs;
- rollback and forward-correction rehearsal against a bounded released fixture; and
- exact-head hosted checks plus human review for the implemented slice.

### Documentation acceptance for this page

This page is acceptable when:

- the metadata block is structurally valid;
- the same path and document identity are preserved;
- the H1 compatibility anchor and numbered legacy anchors remain;
- links and fragments resolve at the pinned base;
- current implementation claims match inspected repository evidence;
- target architecture is labeled rather than presented as current fact;
- the case-collision migration remains held;
- one file changes; and
- rollback is exact and documented.

A green documentation check cannot accept ADR-0004, activate a source, approve policy, establish release authority, or publish KFM knowledge.

[Back to top](#top)

---

<a id="13"></a>

## 13. Dependency-ordered verification backlog

### P0 — authority and safety closure

1. **Case-collision decision packet:** compare complete uppercase/lowercase identities, content, fragments, consumers, and history; choose a survivor or continue `HOLD`.
2. **ADR-0004 disposition:** accept, revise, or hold the dynamic Governed API decision without inferring acceptance from configured code.
3. **Policy runtime:** establish accountable input, bundle, evaluator, outcome, reason, obligation, correction, and rollback semantics.
4. **Evidence resolution:** graduate from caller-supplied candidate checking to an authoritative, no-network repository abstraction for one bounded fixture.
5. **Release authority:** bind authenticated review, release decision, manifest, correction, and rollback without treating readiness as release.
6. **Sensitive handling:** ratify operation- and domain-specific rights, consent, sovereignty, precision, audience, and reviewer requirements.

### P1 — dependency-closed proof slice

Build one synthetic, public-safe, no-network flow:

```text
released candidate
  -> authoritative EvidenceRef resolution
  -> policy decision
  -> review/release binding
  -> RuntimeResponseEnvelope
  -> governed client parsing and rendering
  -> correction or withdrawal replay
  -> rollback verification
```

The slice should include `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`, and prove no model, connector, DNS, or external store call.

### P2 — operational and public-surface maturity

- production authentication and authorization;
- dynamic/static parity;
- cache and index invalidation;
- browser, export, search, graph, map, story, and AI obligation parity;
- performance and accessibility budgets;
- telemetry and audit retention;
- incident response;
- public correction visibility; and
- deployment, recovery, and rollback rehearsal.

### Open questions

- Which document identity survives the case-collision migration?
- Which current object is the authoritative public response envelope for each surface?
- Which reason and obligation vocabularies are safe and accepted?
- Which repository abstraction owns evidence lookup without becoming a second evidence store?
- Which release alias, registry, or manifest is authoritative at runtime?
- Which review roles are accountable and independently enforceable?
- Which static carriers may be served directly, under which integrity and correction checks?
- How are stale, corrected, withdrawn, and rollback-affected responses represented consistently across all clients?
- Which checks are actually required by repository rules at the exact head?

[Back to top](#top)

---

<a id="14"></a>

## 14. Glossary and bounded definitions

| Term | Meaning in this page |
|---|---|
| Trust membrane | Distributed composition separating internal lifecycle state from governed release and delivery |
| Internal side | Not-yet-warranted source, candidate, quarantine, work, and processing state |
| Promotion crossing | Governed transition from candidate catalog/triplet state toward a named release |
| Exposure crossing | Governed transition from released/policy-safe state to a client response or public-safe carrier |
| Warrant | Recorded support for a bounded use, audience, precision, time, and release state |
| Evidence closure | Evidence references resolve to admissible support for the claim and operation |
| Readiness | Validator result indicating declared preconditions passed; not release |
| Release | Accountable state transition with manifest, correction, and rollback support |
| Public-safe carrier | Released derivative suitable for a declared public audience; still not sovereign truth |
| Governed API | Proposed single dynamic trust boundary under ADR-0004; current implementation is a fail-closed scaffold |
| Static-delivery edge | Separately governed delivery of already released public-safe artifacts |
| Finite outcome | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` for public runtime responses |
| HOLD | Internal governance state that blocks a decision or structural change; not a public runtime outcome |
| Obligation | Requirement a downstream surface must preserve, such as citation, attribution, generalization, or no-export |
| Correction lineage | Inspectable relation among prior, corrected, superseded, withdrawn, replacement, and rollback states |
| Non-oracular denial | Safe negative response that does not disclose the protected fact through its reason |
| Case collision | Two tracked paths differ only by case and cannot coexist safely on common case-insensitive filesystems |

---

<a id="related"></a>

## Related documents and evidence surfaces

### Architecture and convergence

- [`README.md`](./README.md) — architecture lane map and explicit structural migration hold.
- [`TRUST_MEMBRANE.md`](./TRUST_MEMBRANE.md) — current repository-grounded architecture/enforcement snapshot.
- [`document-convergence-plan.md`](./document-convergence-plan.md) — provisional no-loss convergence direction.
- [`governed-api/README.md`](./governed-api/README.md) — dynamic API architecture.
- [`evidence-drawer.md`](./evidence-drawer.md) — universal client explanation surface.
- [`publication/promotion-gates.md`](./publication/promotion-gates.md) — promotion-gate architecture context.
- [`contract-schema-policy-split.md`](./contract-schema-policy-split.md) — meaning, shape, admissibility, execution, and proof boundaries.

### Doctrine and decisions

- [Directory Rules v2](../doctrine/directory-rules.md) and [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md).
- [Draft trust-membrane doctrine articulation](../doctrine/trust-membrane.md).
- [ADR-0004](../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) — proposed Governed API decision.

### Contracts, implementation, and bounded proof

- [`RuntimeResponseEnvelope`](../../contracts/runtime/runtime_response_envelope.md) and its [paired schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json).
- [`DecisionEnvelope`](../../contracts/runtime/decision_envelope.md).
- [`PolicyDecision`](../../contracts/policy/policy_decision.md).
- [`apps/governed-api/`](../../apps/governed-api/README.md).
- [`packages/evidence-resolver/`](../../packages/evidence-resolver/README.md).
- [`release/`](../../release/README.md).
- [Promotion-gate readiness validator](../../tools/validators/promotion_gate/README.md).
- [Explorer fixture-only governed adapter](../../apps/explorer-web/src/adapters/GovernedClient.ts).

## Non-effects

This documentation update does not:

- accept, reject, or supersede an ADR;
- choose the case-collision survivor;
- move, rename, delete, mirror, or tombstone a path;
- change a contract, schema, policy, fixture, validator, test, workflow, application, package, data record, receipt, proof, release record, or repository setting;
- authenticate a reviewer or caller;
- activate a source, connector, model, route, policy evaluator, evidence store, or public artifact;
- promote lifecycle state;
- release, deploy, publish, correct, withdraw, or roll back KFM knowledge.

## Last reviewed and rollback

**Last reviewed:** 2026-08-19 against `main@45fc45556a007196aa29e725f3a4b9fe9af8294e`.

**Rollback:** Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the documentation commit or restore prior blob `40602152f13044fa87d57c73c71d797f95afa61e`. No data migration, source deactivation, cache invalidation, correction notice, release rollback, deployment rollback, or public withdrawal is required because this page changes explanatory Markdown only.

[Back to top](#top)
