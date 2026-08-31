<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/explorer-web/readme
title: Explorer Web App README
type: app-readme
version: v0.7
status: draft
owners: OWNER_TBD — Apps steward · UI steward · Map steward · Governed API steward · Policy steward · Accessibility steward · Docs steward
created: 2026-06-16
updated: 2026-08-31
policy_label: public
owning_root: apps/
responsibility: "Orient maintainers to the bounded Explorer Web deployable, its trust boundary, verified executable slices, validation path, and graduation gates without claiming release or deployment."
truth_posture: "CONFIRMED repository-grounded local composition and exact-one governed synthetic integration / PROPOSED shell decision / UNKNOWN broader production integration and deployment"
evidence_snapshot:
  snapshot_role: prior_to_v0_7_slice
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 366cfa9185b0d10ca27f128a8a041ca8c5312896
  target_prior_blob: a668a318b56cd3d8987162b366d0ffbae779c50c
related:
  - ../README.md
  - ../governed-api/README.md
  - ../review-console/README.md
  - ./src/README.md
  - ./src/site/README.md
  - ./src/adapters/README.md
  - ./src/features/README.md
  - ./src/features/story_player/current-implementation.md
  - ./src/features/map_runtime/MOBILE_PMTILES_VERIFICATION_FIXTURE.md
  - ../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../../docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - ../../docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/workflows/ui-build.yml
  - ../../tests/policy/test_explorer_web_adapter_boundary.py
tags: [kfm, apps, explorer-web, map-first, governed-ui, evidence-drawer, focus-mode, story-player, finite-outcomes, fail-closed]
notes:
  - "v0.7 records the exact-one same-origin governed map/evidence slice, package-owned MapLibre activation, identity-preserving selection, Evidence Drawer resolution, and Null fallback while preserving the broader readiness HOLD."
  - "The mounted composition now includes one bounded same-origin governed map/evidence slice and package-owned renderer with Null fallback; this is not proof of broader production routing, source admission, deployment, release, or publication."
  - "The synthetic Focus workspace accepts bounded user questions but resolves them only against deterministic repository fixtures; it does not contact a source, policy service, model runtime, or release service."
  - "ADR-0005 remains proposed; repository presence and passing checks do not accept the shell decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Explorer Web

`apps/explorer-web/`

**KFM's bounded browser-shell workspace: a repository-grounded local composition plus fixture-first projections for evidence, trust, time, Focus, story, map-selection, artifact-verification, and review surfaces.**

![status](https://img.shields.io/badge/status-draft-blue)
![default](https://img.shields.io/badge/default-ABSTAIN%20fail--closed-d4a72c)
![implementation](https://img.shields.io/badge/implementation-bounded%20slices-0969da)
![renderer](https://img.shields.io/badge/renderer-HOLD-b42318)
![deployment](https://img.shields.io/badge/deployment-UNKNOWN-6e7781)

[Current state](#0-current-evidence-snapshot) · [Purpose](#1-purpose) · [Boundary](#3-authority-boundary) · [Surfaces](#7-shell-surfaces) · [Run locally](#12-inspection-path) · [Validation](#13-validation-expectations) · [Open work](#15-open-verification-items)

</div>

---

> [!IMPORTANT]
> **This app is not a released KFM product.** The tracked workspace, locked build/test scripts, repository-grounded site composition, bounded projections, and synthetic browser proofs are real repository implementation. The default entrypoint mounts Map, Knowledge, Features, and Trust regions, public anchor navigation, a shared trust surface, a bounded synthetic Focus workspace, and one exact-one governed synthetic map slice through same-origin `/layers` and `/evidence`. It exposes no production route tree, arbitrary source loading, model runtime, deployment, release, or publication path.

> [!CAUTION]
> Explorer Web is downstream of trust. A rendered feature, tile, popup, story, diagnostic, score, screenshot, or generated explanation is never evidence authority. Claim-bearing UI must consume a governed finite-outcome envelope or an already released public-safe artifact and preserve evidence, policy, time, sensitivity, correction, and release context.

## Quick jump

- [0. Current evidence snapshot](#0-current-evidence-snapshot)
- [1. Purpose](#1-purpose)
- [2. Repo fit](#2-repo-fit)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Inputs](#5-inputs)
- [6. Exclusions](#6-exclusions)
- [7. Shell surfaces](#7-shell-surfaces)
- [8. Diagram](#8-diagram)
- [9. Decision vocabulary](#9-decision-vocabulary)
- [10. UI obligations](#10-ui-obligations)
- [11. Route contract](#11-route-contract)
- [12. Inspection path](#12-inspection-path)
- [13. Validation expectations](#13-validation-expectations)
- [14. Definition of done](#14-definition-of-done)
- [15. Open verification items](#15-open-verification-items)

---

## 0. Current evidence snapshot

This README distinguishes the **mounted local composition** from the larger set of **independently executable feature slices** and from **unverified live operation**. That three-way distinction is the safest current maturity description.

| Surface | Verified repository state | Authority limit |
|---|---|---|
| Workspace and toolchain | `package.json` provides real Vite, TypeScript, Vitest, and Playwright scripts under the locked pnpm workspace. | Buildability is not deployment, release, or publication. |
| Default entrypoint | `src/main.ts` mounts the repository-grounded Explorer site, public workspace navigation, bounded synthetic Focus workspace, and public trust surface. | Composition is local and deterministic; it is not a production route tree, transport, deployment, release, or publication path. |
| Baseline shell posture | The composed hero preserves `ABSTAIN / NO_GOVERNED_RESPONSE`; the underlying fixed shell resolver still rejects unsupported baseline input. | The baseline remains a trust posture inside the larger composition, not the complete entrypoint. |
| Site and workspace navigation | `src/site/` implements Map, Knowledge, Features, and Trust regions, code-owned anchor destinations, bounded public URL context, a synthetic map stage, and conservative repository catalogs. | Anchors and public context are not authenticated routes, released-layer identity, evidence authority, or live data. |
| Adapters and feature modules | `src/adapters/` and `src/features/` contain app-local, defensive projections for multiple trust-visible surfaces. | Most are fixture-first consumers or view-model builders, not composed live routes. |
| Evidence Drawer and trust surface | A bounded parser/resolver, keyboard-operable drawer, shared six-label trust grammar, negative copy, correction/history display, and browser tests exist; the synthetic map slice resolves it through `/evidence`. | No general `EvidenceBundle` resolver or broader production cross-root contract is established. |
| Focus workspace | The normal entrypoint mounts a bounded question form that submits through an injected synthetic governed boundary and preserves finite outcomes, evidence support, withheld-context limitations, and correction history. | Deterministic fixtures only; no source retrieval, model call, policy execution, live evidence authentication, or publication. |
| Story Player | A bounded 2D-only consumer of an already-governed public-safe StoryManifest projection and focused unit tests exist. | No live route, fetch, StoryNode resolution, map continuity, authoring, or publication. |
| Map and PMTiles proof | The exact-one `/layers` slice boots the package-owned MapLibre adapter, preserves pointer/keyboard selection identity, and falls back to `NullMapRuntime`; mobile-emulated PMTiles verification remains separate. | Broader MapLibre readiness remains `HOLD`; this does not admit arbitrary sources, make a trust decision, activate released data, deploy, or publish. |
| UI validation | The `ui-build` workflow performs locked install, build, unit tests, and browser tests; a policy test constrains renderer imports and internal-store path literals. | CI is a bounded signal, not evidence, policy, review, release, deployment, or publication authority. |
| Shell decision | ADR-0005 documents the proposed single Explorer shell and current implementation evidence. | ADR-0005 remains `proposed`; repository presence does not accept it. |
| Deployment and operation | No current evidence in this README establishes hosting, authentication, CSP, observability, service health, or public use. | `UNKNOWN` until tied to current deployment and runtime evidence. |

### Maturity summary

```text
CONFIRMED
  configured workspace
  locked build and test lane
  repository-grounded local site composition
  code-owned public anchor navigation and bounded URL context
  shared trust-state surface and synthetic Focus workspace
  independently tested fixture-first projections
  synthetic browser and boundary proofs

PROPOSED
  one canonical map-first Explorer composition root
  live route families and full governed-shell composition

HOLD
  broader renderer readiness and production map operation
  general trust-bearing transport and public artifact loading beyond the bounded slice

UNKNOWN
  deployment, authentication, CSP, operations, public availability,
  production data flows, and release posture
```

[Back to top](#top)

---

## 1. Purpose

Explorer Web is the deployable browser workspace in which KFM's map-first, time-aware, evidence-first posture can become inspectable to users.

Its intended role is to compose:

- a persistent governed shell;
- bounded map interaction and layer discovery;
- trust, freshness, time-kind, sensitivity, and release indicators;
- Evidence Drawer handoffs;
- finite Focus Mode outcomes;
- Story Player, Compare, Export, Settings, Diagnostics, and read-only review views;
- accessible non-map alternatives and negative states.

The current implementation proves a defensive, repository-grounded local composition, multiple bounded projection slices, and one integrated exact-one synthetic map/evidence path. It does **not** prove a broader production map application, arbitrary source admission, released data, deployment, or public operation. See the [site-composition README](./src/site/README.md), [feature catalog](./src/features/README.md), and [ADR-0005](../../docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) for the deeper implementation boundary and proposed shell decision.

[Back to top](#top)

---

## 2. Repo fit

Accepted Directory Rules place deployable application code under `apps/`. This existing README remains at the app boundary; no path, root, or authority migration is introduced here.

| Concern | Owning surface | Relationship to Explorer Web |
|---|---|---|
| Deployable browser composition | `apps/explorer-web/` | App workspace, default entrypoint, app-local features, adapters, and tests |
| Dynamic trust-bearing interface | [`apps/governed-api/`](../governed-api/) | Current bounded `/layers` and `/evidence` slice; broader claim-bearing transport remains future work |
| Steward review | [`apps/review-console/`](../review-console/) | Separate review authority; Explorer may expose read-only projections only |
| App-local boundary adapters | [`src/adapters/`](./src/adapters/) | Defensive translation of governed or bounded fixture inputs |
| App-local feature modules | [`src/features/`](./src/features/) | UI composition and view-model behavior |
| Shared UI primitives | [`packages/ui/`](../../packages/ui/) | Reusable components when extracted from app-local ownership |
| Renderer wrapper | [`packages/maplibre/`](../../packages/maplibre/) | Package-owned adapter renders the bounded inline slice; broader runtime readiness and source/layer/style admission remain held |
| Contracts and schemas | `contracts/`, `schemas/` | Meaning and machine shape; Explorer references but does not redefine them |
| Policy | `policy/` | Rights, sensitivity, access, telemetry, and admissibility decisions |
| Lifecycle and evidence objects | `data/` | Internal records, receipts, proofs, catalogs, and published artifacts; never direct browser stores |
| Release and rollback | `release/` | Publication, correction, withdrawal, supersession, and rollback authority |
| Architecture and decisions | `docs/` | Doctrine, proposed decisions, UI architecture, and operational guidance |
| Cross-root enforcement | [`tests/policy/test_explorer_web_adapter_boundary.py`](../../tests/policy/test_explorer_web_adapter_boundary.py) | Bounded static guard against renderer-import and internal-store bypass |

### Placement basis

- **CONFIRMED:** `apps/` owns deployable applications under accepted Directory Rules and ADR-0029.
- **CONFIRMED:** this is a same-path README modernization; there are no new, moved, renamed, or deleted paths.
- **PROPOSED:** ADR-0005 would make this exact child workspace the single canonical map-first shell.
- **NEEDS VERIFICATION:** final owner roles and any branch-protection or required-review enforcement.

[Back to top](#top)

---

## 3. Authority boundary

Explorer Web may present governed results. It may not create or silently strengthen their authority.

```text
sources / lifecycle stores / evidence / policy / review / release
                              |
                              v
              governed interface or released public-safe artifact
                              |
                              v
                   apps/explorer-web/src/adapters
                              |
                              v
                   apps/explorer-web/src/features
                              |
                              v
              shell / drawer / story / compare / export / diagnostics
```

### Explorer Web may

- validate and project a bounded response before rendering;
- preserve finite outcomes, evidence handles, citations, time kinds, policy labels, release state, and correction lineage;
- treat map interactions as candidate scope for governed resolution;
- render already released public-safe immutable artifacts with integrity and release context;
- propose safe user actions or navigation without executing authority-bearing transitions;
- emit minimized, non-secret UI telemetry only when the applicable contract and policy allow it.

### Explorer Web must not

- read `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, candidate, canonical, internal, graph, vector, or object stores directly as browser truth;
- call model providers or model runtimes directly;
- infer evidence from pixels, feature properties, route parameters, telemetry, local files, or generated prose;
- execute source admission, policy, review, promotion, release, correction, rollback, or publication;
- reverse server-side redaction, generalization, suppression, delay, or denial;
- redefine contracts, schemas, policy, renderer authority, receipt semantics, or release meaning inside feature code.

> [!IMPORTANT]
> A static edge may serve an already released public-safe artifact. It must not become a second API, canonical store, policy engine, or publication authority.

[Back to top](#top)

---

## 4. Default posture

The browser fails safe.

When a required trust-bearing input is absent, malformed, stale, denied, unsupported, conflicted, unreleased, superseded, or outside scope, the UI must show a bounded negative state instead of guessing or silently falling back.

Required context depends on consequence, but claim-bearing views normally need:

- a validated finite-outcome envelope;
- evidence or citation handles where a claim is made;
- source role and provenance summary;
- valid, observed, source, retrieval, release, correction, and freshness time where material;
- rights, sensitivity, access, redaction, and generalization obligations;
- release, correction, supersession, withdrawal, and rollback context;
- an accessible textual status that does not rely on color, map position, or animation alone.

The default shell deliberately proves the absence path first. Broader feature slices may implement positive fixture cases, but they do not override the composed app's fail-closed maturity boundary.

[Back to top](#top)

---

## 5. Inputs

| Input family | Examples | Required posture |
|---|---|---|
| Finite response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, reason code, bounded message | Parse and validate before render |
| Evidence support | `EvidenceRef`, EvidenceBundle-derived summary, citation and support references | Required for consequential claims |
| Policy and rights | audience, access, sensitivity, rights, redaction, generalization, delay, suppression | Preserve; never weaken client-side |
| Release support | release reference, artifact digest, correction lineage, rollback target | Visible where material |
| Time support | valid, observed, source, retrieval, release, correction, freshness, stale state | Keep time kinds distinct |
| Layer and map state | released layer manifest, selected feature candidate, viewport, tile status | Candidate interaction, never truth by itself |
| Story state | public-safe StoryManifest projection, node order, support references | Playback only when all gates remain satisfied |
| Export state | selected scope, citations, policy obligations, release identity | Governed export only |
| Review projection | status, history, provenance, reviewer-facing summary | Read-only unless a separate authorized workflow owns mutation |
| Diagnostics and telemetry | bounded version/status metadata and minimized event names | No secrets, raw evidence, prompts, model output, or restricted geometry |
| Accessibility state | labels, focus return, keyboard paths, reduced motion, contrast, non-map alternative | Required for public and semi-public use |

Inputs may come from test fixtures while a feature is under development. Fixture success must remain visibly distinct from live transport or released-data support.

[Back to top](#top)

---

## 6. Exclusions

| Does not belong in Explorer Web authority | Owning surface |
|---|---|
| Governed API implementation and trust-bearing transport | `apps/governed-api/` |
| Mutating steward review workflows | `apps/review-console/` and review governance |
| Shared reusable UI primitives | `packages/ui/` |
| Renderer wrapper implementation | `packages/maplibre/` or an accepted successor |
| Model runtime and provider clients | `runtime/` behind governed interfaces |
| Source connectors and admission | `connectors/`, registries, and source policy |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/` |
| Rights, sensitivity, access, telemetry, and release policy | `policy/` |
| RAW through PUBLISHED lifecycle records | `data/` under the correct phase/family |
| Release manifests, correction notices, withdrawal, and rollback cards | `release/` |
| Secrets, tokens, private keys, protected endpoints | deployment secret manager or environment |
| Production evidence copied into fixtures | prohibited; use deterministic synthetic or public-safe minimized fixtures |

[Back to top](#top)

---

## 7. Shell surfaces

The directory contains a growing catalog of bounded feature families. Presence means a path exists; maturity must be established from its implementation, fixtures, tests, and composition.

| Family | Current evidence | Current boundary |
|---|---|---|
| Shell and trust chrome | Repository-grounded site composition, public anchor navigation/context, baseline shell posture, shared trust surface, and focused tests | Local/static and fixture-first; no production route tree, authentication, transport, or deployment |
| Evidence surfaces | Mounted Evidence Drawer/trust projections plus citation pill, tooltip, provenance, attestation, lineage, and denial slices; the exact-one map path resolves `/evidence` | Bounded synthetic resolver only; no general production EvidenceBundle resolver |
| Focus and story | Mounted synthetic Focus workspace, Focus composed-claim tests, and bounded Story Player consumer | No live governed transport, model call, story route, or story publication |
| Map and layers | Exact-one governed layer/evidence transport, package-owned MapLibre rendering, identity-preserving pointer/list selection, Null fallback, plus separate catalog/lineage and mobile PMTiles proofs | Broader MapLibre readiness remains `HOLD`; no arbitrary source admission or released live layer |
| Domain panels | Fauna and environmental/soil/hydrology-oriented projections | Domain UI projections, not domain truth |
| Review and governance visibility | Read-only review, promotion-gate, watcher/source-health, STAC, OCI, and diagnostics projections | No review mutation or authority transition |
| Compare and export | App-local feature boundaries and defensive contracts | Integrated public workflows remain `NEEDS VERIFICATION` |
| Settings and accessibility | Feature-boundary obligations and focused behavior in tested slices | Full integrated preference persistence and accessibility audit remain open |

For the authoritative child inventory and per-feature obligations, use [`src/features/README.md`](./src/features/README.md). Two high-signal current implementation notes are:

- [`Story Player current implementation`](./src/features/story_player/current-implementation.md)
- [`Mobile PMTiles verification fixture`](./src/features/map_runtime/MOBILE_PMTILES_VERIFICATION_FIXTURE.md)

> [!WARNING]
> Do not convert this table into a route list. A feature directory, test, README, or view-model builder does not prove navigation wiring, live transport, released inputs, deployment, or public readiness.

[Back to top](#top)

---

## 8. Diagram

```mermaid
flowchart LR
    released["governed response or released public-safe artifact"] --> adapters["src/adapters"]
    adapters --> features["src/features"]
    features --> shell["Explorer shell"]
    features --> drawer["Evidence Drawer"]
    features --> story["Story / Focus / Compare / Export"]
    features --> diagnostics["safe diagnostics"]

    mapEvent["map or tile interaction candidate"] --> mapPort["renderer-neutral map port"]
    mapPort --> resolver["injected governed resolver"]
    resolver --> outcome{{"ANSWER / ABSTAIN / DENY / ERROR"}}
    outcome --> features

    internal["RAW / WORK / QUARANTINE / canonical stores / model providers / secrets"] -. "DENY" .-> features
    authority["policy / review / release / correction / rollback"] -. "display state only" .-> features
```

The renderer, UI, and generated language remain downstream carriers. Evidence and release authority stay outside the browser.

[Back to top](#top)

---

## 9. Decision vocabulary

### Outward finite outcomes

| Outcome | UI behavior |
|---|---|
| `ANSWER` | Render only the bounded supported content, citations, and governing context. |
| `ABSTAIN` | Explain that support is missing, stale, conflicted, out of scope, or not released. |
| `DENY` | Withhold protected content and show only a safe public reason class or next step. |
| `ERROR` | Report an operational failure without falling back to unvalidated content. |

### Supporting UI states

`LOADING`, `EMPTY`, `HOLD`, `RESTRICTED`, `STALE`, `DEGRADED`, `CONFLICT`, `SUPERSEDED`, `WITHDRAWN`, and `UNAVAILABLE` may refine the interface. They must not silently coerce into `ANSWER`.

Rules:

1. Unknown outcome values fail closed.
2. A prior positive render is cleared when the next result denies or errors.
3. Negative copy does not leak restricted fields or hidden policy reasons.
4. Retry is offered only when retry is safe and meaningful.
5. Correction, supersession, and withdrawal state outrank cached positive presentation.

[Back to top](#top)

---

## 10. UI obligations

| Obligation | Required effect |
|---|---|
| `governed_interface_only` | Claim-bearing dynamic data enters through a governed boundary. |
| `released_static_only` | Static artifacts are already released, public-safe, integrity-bound, and correction-aware. |
| `runtime_validation` | Malformed or unknown envelopes cannot become display truth. |
| `evidence_visible` | Consequential claims expose inspectable support or abstain. |
| `policy_preserved` | Rights, sensitivity, access, redaction, and generalization survive every handoff. |
| `time_kinds_preserved` | Distinct time semantics are not flattened into one timestamp. |
| `renderer_downstream` | Map state scopes a request; it does not prove the result. |
| `finite_negative_states` | Deny, abstain, error, stale, conflict, and unavailable states are first-class. |
| `correction_aware` | Corrected, superseded, withdrawn, or rolled-back content cannot remain silently current. |
| `safe_export` | Exports preserve citation, release, rights, redaction, and correction context. |
| `safe_telemetry` | Telemetry contains minimized event metadata only. |
| `accessible_by_default` | Keyboard, focus, screen reader, reduced motion, contrast, non-color status, and non-map alternatives are testable. |
| `no_browser_model` | No direct provider SDK or model-runtime call exists in public client code. |
| `no_authority_fork` | Feature code does not reimplement schema, policy, evidence, release, or review authority. |

[Back to top](#top)

---

## 11. Route contract

A production route tree is not yet established. Any future long-lived route must document or encode:

- stable route identity, owner, purpose, audience, and sensitivity posture;
- accepted inputs and the governed adapter or released-artifact source;
- finite outcomes and all negative states;
- evidence, citation, policy, release, correction, and time display;
- map-selection and Evidence Drawer handoffs;
- redaction/generalization behavior that cannot be reversed in the browser;
- loading, empty, stale, denied, abstained, errored, conflicted, superseded, and withdrawn behavior;
- accessible heading, landmark, keyboard, focus-entry, focus-return, announcement, reduced-motion, and non-map paths;
- export and telemetry behavior, if present;
- deterministic fixtures and tests;
- rollback or disable path.

A route is not considered implemented because its name appears in documentation or a feature folder. Evidence requires route wiring, accepted inputs, focused tests, browser behavior, and the relevant governed upstream support.

[Back to top](#top)

---

## 12. Inspection path

### Run the bounded workspace

From the repository root:

```bash
corepack enable
pnpm install --frozen-lockfile
pnpm --filter explorer-web build
pnpm --filter explorer-web test
```

Focused commands:

```bash
pnpm --filter explorer-web test:unit
pnpm --filter explorer-web test:browser
pnpm --filter explorer-web dev
```

The development server displays the repository-grounded local site composition, including the exact-one governed synthetic map/evidence workspace, public workspace navigation, bounded Focus request surface, and shared trust-state cases. Tests exercise a broader set of fixture-first slices than the composed page.

### Inspect current implementation

```bash
find apps/explorer-web/src -maxdepth 6 -type f | sort
find apps/explorer-web/tests -maxdepth 4 -type f | sort
find apps/explorer-web/src/features -mindepth 1 -maxdepth 1 -type d | sort
```

High-signal files:

- [`package.json`](./package.json)
- [`src/main.ts`](./src/main.ts)
- [`src/README.md`](./src/README.md)
- [`src/adapters/README.md`](./src/adapters/README.md)
- [`src/features/README.md`](./src/features/README.md)
- [`ui-build.yml`](../../.github/workflows/ui-build.yml)
- [`test_explorer_web_adapter_boundary.py`](../../tests/policy/test_explorer_web_adapter_boundary.py)

### Evidence discipline

When reporting a result, record the exact branch/commit and distinguish:

- source presence;
- focused local test result;
- hosted exact-head result;
- route composition;
- deployed runtime evidence;
- release/publication state.

These are separate claims.

[Back to top](#top)

---

## 13. Validation expectations

### Repository-native Explorer lane

The maintained workflow runs:

```bash
pnpm --filter explorer-web build
pnpm --filter explorer-web test
```

A trustworthy validation report should identify the exact tested SHA and separate unit, browser, boundary, and hosted conclusions.

### Required checks by change type

| Change type | Minimum focused evidence |
|---|---|
| README only | One H1; heading/anchor and relative-link checks; balanced fences/HTML; no stale maturity claims; final newline; `git diff --check`; generated receipt for AI-authored work |
| Shell or feature projection | Unit cases for positive and finite negative states; no-leak checks; evidence/policy/time preservation |
| Browser interaction | Playwright keyboard/focus and prior-render clearing; no external request when fixture-only |
| Map-facing feature | Renderer import boundary, synthetic selection, governed resolver injection, no direct store access |
| Evidence Drawer or claim display | Missing/malformed support fails closed; citations and correction/history remain visible |
| Story, Compare, or Export | Public-safe support gates, ordering/identity validation, citation/redaction/release continuity |
| Diagnostics or telemetry | Secret/restricted-field denial and minimized event payloads |
| Renderer admission | Accepted dependency/adapter decision, locked supply chain, browser proof, performance/accessibility budget, rollback |
| Live transport | Accepted response contract, authentication/exposure review, CSP/CORS, error isolation, policy and citation validation, integration tests |
| Deployment | Environment-specific security, observability, rollback, release, and public-operation evidence |

### Boundary checks

The app must continue to prove that:

- renderer imports stay behind the adapter boundary;
- internal lifecycle-store path literals do not enter browser source;
- direct model-provider calls are absent;
- fixture-only modules make no undeclared external requests;
- denied or errored results clear prior positive content;
- redacted or generalized content cannot be reconstructed client-side;
- documentation does not promote a fixture slice into a live-product claim.

> [!NOTE]
> A green `ui-build` run proves the workflow's declared build/test scope for its exact SHA. It does not prove deployment, evidence closure, policy approval, release, or publication.

[Back to top](#top)

---

## 14. Definition of done

### For changes inside this app

- [ ] Scope, base SHA, target paths, and owner/review route are recorded.
- [ ] The feature or route contract names its inputs, finite outcomes, evidence and policy obligations, accessibility behavior, tests, and rollback.
- [ ] Dynamic claim-bearing inputs use a governed interface; static inputs are already released public-safe artifacts.
- [ ] Evidence, citation, time, rights, sensitivity, release, correction, and rollback state survive composition.
- [ ] Negative, malformed, stale, denied, superseded, and unavailable cases fail closed.
- [ ] Direct internal-store and model-runtime access remains denied.
- [ ] Map-facing code preserves the adapter boundary.
- [ ] Export, diagnostics, and telemetry paths are minimized and non-leaking.
- [ ] Keyboard, focus, screen-reader, reduced-motion, contrast, non-color, and non-map paths are tested in proportion to the surface.
- [ ] Documentation describes only verified maturity.
- [ ] Targeted local and exact-head hosted validation are recorded separately.
- [ ] AI-authored changes include a generated receipt with pending human review.
- [ ] Rollback is a specific revert/disable path and does not imply data publication.

### Before describing Explorer as an integrated map product

- [ ] ADR-0005 or a successor resolves the shell decision.
- [x] A renderer dependency and adapter boundary are accepted, pinned, and exercised for the bounded inline synthetic slice.
- [ ] The default entrypoint composes an explicit route inventory.
- [x] Same-origin Governed API transport and strict envelope validation are wired for the bounded `/layers` and `/evidence` slice.
- [ ] At least one released public-safe layer loads through the governed delivery path.
- [x] Pointer and accessible-list selection resolve evidence and finite outcomes through the governed interface for the exact-one synthetic slice.
- [ ] Evidence Drawer, Focus, Story, Compare, and Export handoffs are integrated and accessible.
- [ ] Authentication, CSP/CORS, telemetry, diagnostics, deployment, observability, correction, and rollback are verified.
- [ ] Public operation and release state are proven by governed runtime and release evidence rather than documentation.

[Back to top](#top)

---

## 15. Open verification items

| Item | Why it remains open |
|---|---|
| ADR-0005 acceptance or successor decision | The intended single-shell posture is documented but not binding. |
| Confirmed owner and independent review route | `OWNER_TBD` must not be replaced without evidence. |
| Broader MapLibre runtime readiness | The bounded inline adapter is active, but arbitrary sources, styles, tiles, protocols, operational probes, and production use remain held. |
| General Governed API response contracts and production transport | The exact-one `/layers` and `/evidence` integration does not establish broader authenticated or production API operation. |
| Production route inventory | Code-owned anchor destinations and public URL context exist, but feature paths and anchors are not proof of authenticated or production routes. |
| Released layer and artifact discovery | Synthetic PMTiles proof does not load a governed public release. |
| General EvidenceBundle resolution and citation validation | The bounded exact-one resolver is not broader end-to-end evidence closure. |
| Integrated Focus, Story, Compare, and Export flows | Bounded consumers exist, but cross-feature composition remains incomplete. |
| Authentication, authorization, CSP, CORS, and exposure posture | No deployed-system evidence is established here. |
| Telemetry contract, policy, retention, and runtime wiring | Feature guidance does not prove operational telemetry safety. |
| Complete accessibility audit | Focused tests do not establish whole-app conformance. |
| Offline, service-worker, mobile-device, and hosting Range behavior | Mobile-emulated synthetic proof is intentionally narrower. |
| Production observability and incident response | Workflow output is not service-health evidence. |
| Deployment, release, correction propagation, and rollback drill | No current public operation or released Explorer state is established. |
| Exact current file/test counts | Counts drift quickly and should be generated from the inspected commit, not copied into this README. |

## Status summary

Explorer Web is best described as a **bounded, executable, repository-grounded local composition and fixture-first UI laboratory**.

That is more mature than a placeholder or inert shell and less mature than a live map product. The repository proves real build/test tooling, a mounted local site and navigation composition, bounded public context, shared trust states, a synthetic Focus request surface, defensive adapters, many finite-state projections, Evidence Drawer behavior, a bounded Story Player consumer, one exact-one governed MapLibre/evidence integration, separate mobile PMTiles verification, and static anti-bypass checks. It does not prove a production route tree, general Governed API transport, arbitrary source admission, a released map layer, broader renderer readiness, model-backed Focus execution, deployment, or public operation.

<p align="right"><a href="#top">Back to top</a></p>
