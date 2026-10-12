<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://architecture/ui/map-context-evidence-drawer-admission
title: MapContextEnvelope to EvidenceDrawerPayload Admission Boundary
type: architecture-reference
version: v2.0-draft
status: draft; repository-grounded; bounded-executable; inactive-runtime; no-authority
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — independent UI, runtime, evidence, policy, release, accessibility, security, and validation stewardship"
created: 2026-08-07
updated: 2026-08-19
policy_label: public; ui; runtime; evidence-drawer; renderer-neutral; public-safe; no-release; no-publication
owning_root: docs/
responsibility: "Explain the repository-present MapContextEnvelope-to-EvidenceDrawerPayload admission helper, its finite candidate behavior, proof limits, integration HOLD, and graduation requirements without becoming contract, schema, policy, evidence, review, release, or runtime authority."
truth_posture: "CONFIRMED repository evidence / PROPOSED semantics and integration / UNKNOWN deployed behavior; cite-or-abstain"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0764316bfb920d076219a26c06ce1e335dbaf9fd
  target_prior_blob: 32a9d4da2d778014e88033ab205ba08491c43ca0
  feature_pull_request: 2105
  feature_merge_commit: a889f8b596e0ddcac0955cfb4227f9b0c87625f9
related:
  - ./README.md
  - ./BOUNDARIES.md
  - ./EVIDENCE_DRAWER.md
  - ./MAP_RUNTIME_BOUNDARY.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../../contracts/ui/map_context_envelope.md
  - ../../../contracts/ui/evidence_drawer_payload.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../packages/envelopes/src/envelopes/map_context_evidence_drawer.py
  - ../../../packages/envelopes/src/envelopes/__init__.py
  - ../../../fixtures/ui/map_context_evidence_drawer_admission/README.md
  - ../../../fixtures/ui/map_context_evidence_drawer_admission/cases.json
  - ../../../tools/validators/ui/validate_map_context_evidence_drawer_admission.py
  - ../../../tests/packages/envelopes/test_map_context_evidence_drawer_admission.py
  - ../../../.github/workflows/map-context-evidence-drawer-admission.yml
  - ../../../data/receipts/generated/genrec-map-context-evidence-drawer-admission-20260807.json
  - ../../../data/receipts/generated/genrec-map-context-evidence-drawer-admission-doc-workflow-20260819.json
  - ../../../apps/explorer-web/src/adapters/GovernedClient.ts
tags: [kfm, architecture, ui, map-context, evidence-drawer, anticorruption-layer, decision-envelope, finite-outcomes, no-network, fail-closed]
notes:
  - "v2.0-draft replaces the proposal-era summary with a current repository-grounded architecture reference at the same path."
  - "The helper and its focused fixture/test/validator/workflow packet are present, but no apps/ caller or deployed route invocation is established."
  - "The original feature receipt remains immutable process memory; it is not updated or treated as review, release, or publication authority."
  - "This maintenance slice repoints the path-scoped workflow from the immutable 2026 feature receipt to the current docs-and-workflow authoring receipt; validation scope and permissions remain unchanged."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Map context to Evidence Drawer admission

> **Operating rule.** A map selection and an Evidence Drawer projection may cross this boundary only as already validated, renderer-neutral declarations. The helper can emit a finite `DecisionEnvelope` **candidate** about their local alignment; it cannot resolve evidence, execute policy, authenticate review, establish release state, authorize public use, or publish anything.

| Field | Current result |
|---|---|
| **Document role** | Human-readable architecture reference under `docs/`; not doctrine, a semantic contract, machine schema, policy rule, proof, release record, or runtime implementation. |
| **Evidence snapshot** | `main@0764316bfb920d076219a26c06ce1e335dbaf9fd`; prior target blob `32a9d4da2d778014e88033ab205ba08491c43ca0`. |
| **Placement authority** | **CONFIRMED:** accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md); the existing `docs/architecture/ui/` lane is placement-safe. |
| **Implementation** | **CONFIRMED / BOUNDED:** one side-effect-minimal Python helper, package export, eight-case synthetic packet, deterministic replay validator, focused tests, and a read-only path-scoped workflow are present. |
| **Input and output authority** | The current contracts and schemas remain `draft` or `PROPOSED`; the helper emits a schema-shaped candidate, not an accepted policy or release decision. |
| **Runtime integration** | **HOLD / NEEDS VERIFICATION:** repository search found the helper symbol only in the package implementation, package export, replay validator, and focused tests. No `apps/` caller or deployed route invocation was found. |
| **Evidence, policy, review, and release** | Declaration alignment only. No reference resolution, policy evaluation, reviewer authentication, release lookup, correction lookup, or rollback execution occurs. |
| **Release/publication effect** | None. A passing helper call, test, workflow, commit, pull request, or documentation update is not publication. |

> [!IMPORTANT]
> **Current maturity is bounded executable, not integrated runtime.** The packet proves deterministic fixture-level cross-object behavior. It does not prove that Explorer Web, the governed API, a map renderer, or a deployed service invokes the helper.

> [!CAUTION]
> **A declaration is not authority.** `release_state = "PUBLISHED"` and a release reference are checked for local consistency only. The helper does not prove that the release exists, is active, is public-safe, or has survived correction or withdrawal.

---

## Quick jump

- [1. Purpose and scope](#1-purpose-and-scope)
- [2. Authority by question](#2-authority-by-question)
- [3. Current repository state](#3-current-repository-state)
- [4. Why this boundary exists](#why-this-boundary-exists)
- [5. Inputs and output](#inputs-and-output)
- [6. Admission sequence](#6-admission-sequence)
- [7. Admission checks](#admission-checks)
- [8. Finite outcomes](#finite-outcomes)
- [9. Data minimization and no-leak behavior](#9-data-minimization-and-no-leak-behavior)
- [10. Synthetic cases and executable proof](#10-synthetic-cases-and-executable-proof)
- [11. Runtime integration status](#11-runtime-integration-status)
- [12. Security, rights, and sensitivity boundary](#12-security-rights-and-sensitivity-boundary)
- [13. Non-effects](#non-effects)
- [14. Directory Rules basis](#directory-rules-basis)
- [15. Validation](#validation)
- [16. Graduation gates and verification backlog](#16-graduation-gates-and-verification-backlog)
- [17. Compatibility, correction, and rollback](#17-compatibility-correction-and-rollback)
- [18. Rollback](#rollback)
- [Related documents](#related-documents)

---

## 1. Purpose and scope

This page explains the repository-present admission seam between:

1. a validated renderer-neutral [`MapContextEnvelope`](../../../contracts/ui/map_context_envelope.md);
2. a validated public-safe [`EvidenceDrawerPayload`](../../../contracts/ui/evidence_drawer_payload.md); and
3. a bounded [`DecisionEnvelope`](../../../contracts/runtime/decision_envelope.md) candidate with `policy_family = "render"`.

The seam answers one narrow question:

> Do these two already validated declarations remain locally aligned for exactly one selected feature at the stated evaluation time?

It does **not** answer whether the selected claim is true, whether evidence is authentic, whether policy permits exposure, whether review is accountable, whether the release is active, or whether a browser may render the result in production.

### In scope

- exact profile and time checks;
- selected-feature, selected-layer, evidence-set, and release-reference relationships;
- finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` propagation;
- fixed obligations and safe reason text;
- selected-feature evidence scoping;
- deterministic replay, input immutability, schema conformance, and no-network proof;
- explicit non-effects and runtime-integration HOLD.

### Out of scope

- `EvidenceRef -> EvidenceBundle` resolution;
- source, rights, consent, sovereignty, sensitivity, access, or render-policy evaluation;
- caller identity or role authentication;
- reviewer, steward, signer, or release-authority authentication;
- release-manifest, correction-notice, withdrawal, or rollback resolution;
- MapLibre or any other renderer admission;
- browser, governed-API, Focus Mode, export, cache, deployment, or publication behavior;
- accepting an ADR, contract, schema profile, policy bundle, or public interface by documentation.

[Back to top](#top)

---

## 2. Authority by question

This architecture page describes the boundary; it does not own the objects or decisions that cross it.

| Question | Controlling surface |
|---|---|
| Where does this page belong? | Accepted ADR-0029, adopted Directory Rules v2, and the existing `docs/architecture/ui/` lane. |
| What does `MapContextEnvelope` mean? | [`contracts/ui/map_context_envelope.md`](../../../contracts/ui/map_context_envelope.md). |
| What does the drawer projection mean? | [`contracts/ui/evidence_drawer_payload.md`](../../../contracts/ui/evidence_drawer_payload.md), while its final UI/evidence-family authority seam remains unresolved. |
| What machine shapes are admitted? | The paired schemas under [`schemas/contracts/v1/ui/`](../../../schemas/contracts/v1/ui/) and [`schemas/contracts/v1/runtime/`](../../../schemas/contracts/v1/runtime/). |
| What does the helper currently do? | [`map_context_evidence_drawer.py`](../../../packages/envelopes/src/envelopes/map_context_evidence_drawer.py), its export, fixtures, validator, and focused tests at the pinned commit. |
| May a caller render or expose a claim? | Resolved evidence plus applicable policy, rights, sensitivity, review, release, correction, and runtime controls—not this helper or page. |
| Is an object released or published? | A governed release record and active released state—not a local string, schema-valid fixture, workflow, or candidate envelope. |

The helper is an **anticorruption adapter** between bounded models. It must not become a fourth semantic authority or a shortcut around the governed runtime.

[Back to top](#top)

---

## 3. Current repository state

### Confirmed surfaces

| Surface | Current repository evidence | Boundary |
|---|---|---|
| Map-context contract | Proposed, inactive, renderer-neutral semantic contract with released-input declarations and deterministic identity rules. | Contract meaning only; no evidence, policy, or release authority. |
| Drawer contract | Proposed closed public-safe projection profile with finite outcomes, correction history, and DENY/ERROR no-leak rules. | UI projection only; the UI/evidence contract-home seam remains unresolved. |
| Decision schema | Closed Draft 2020-12 shape requiring `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, and `evaluated_at`. | Schema status is `PROPOSED`; shape conformance is not policy or release approval. |
| Adapter | [`build_map_context_evidence_drawer_admission_candidate`](../../../packages/envelopes/src/envelopes/map_context_evidence_drawer.py) is present with `ADAPTER_VERSION = "1.0.0"`. | Side-effect-minimal candidate builder only. |
| Package export | The helper and profile constants are exported by [`packages/envelopes`](../../../packages/envelopes/src/envelopes/__init__.py). | Export presence does not prove an application caller. |
| Fixture packet | [`cases.json`](../../../fixtures/ui/map_context_evidence_drawer_admission/cases.json) defines exactly eight expected cases. | Synthetic declarations only. |
| Replay validator | The UI validator safely parses bounded local JSON, restricts fixture paths, replays cases, and validates candidate shape. | No evidence dereference, policy execution, or release lookup. |
| Focused tests | Tests cover exact outcomes, schema conformance, deterministic replay, immutability, no content copying, ambiguous selection, governance overclaim, unpublished declaration, invalid build inputs, and socket denial. | Source-level assertions; exact-current-head execution remains a separate check. |
| Workflow | A path-scoped workflow uses read-only contents permission, pinned actions, Python 3.11, the repository lock installer, source validators, focused tests, case replay, and current authoring-receipt validation. | The maintenance slice changes only the receipt target and digest reporting; executable admission scope and permissions are unchanged. |
| Original generated receipt | The merged feature packet has an immutable authoring receipt with human review recorded as `pending`. | Process memory only; not approval, proof, release, or publication authority. |
| Current maintenance receipt | The docs-and-workflow receipt binds the current documentation and path-scoped workflow bytes with human review recorded as `pending`. | Authoring provenance only; not approval, proof, release, or publication authority. |

### Current HOLDs

- No application or governed-API import of the helper was found in the current symbol search.
- Explorer's current [`GovernedClient.ts`](../../../apps/explorer-web/src/adapters/GovernedClient.ts) is fixture-only and explicitly performs no network or lifecycle-store access.
- Evidence-reference resolution, render policy, caller authentication, active release lookup, correction propagation, and deployed use remain unproved.
- The `DecisionEnvelope` contract and paired schema remain proposed rather than accepted runtime authority.
- The drawer's final semantic authority split between UI-facing projection and evidence-family material remains unresolved.

[Back to top](#top)

---

## Why this boundary exists

The map shell knows which layer and feature the user selected. The Evidence Drawer projection knows the finite public-safe state the governed runtime intends the browser to display. These are distinct models with distinct responsibilities.

Without a cross-object boundary, individually valid inputs could still be unsafe together. Examples include:

- a drawer answer citing evidence visible elsewhere in the viewport but unrelated to the selected feature;
- a selected layer whose release reference is absent from the context release set;
- stale or denied drawer state being treated as a current answer;
- multiple selections being silently reduced to one;
- test-only caller posture reaching a normal path;
- denial or error content leaking titles, summaries, citations, limitations, or history.

The adapter therefore acts as a small published-language boundary:

```text
released-state declarations
  -> validated MapContextEnvelope
  -> validated EvidenceDrawerPayload
  -> local cross-object admission checks
  -> DecisionEnvelope candidate
  -> separately governed runtime / evidence / policy / release handling
```

The helper does not replace either input validator. Callers are expected to validate both input objects with their owning validators before invoking the cross-object adapter.

[Back to top](#top)

---

## Inputs and output

| Surface | Current role | Authority limit |
|---|---|---|
| `MapContextEnvelope` | Carries renderer-neutral layer, selection, time, area, evidence, release, caller-role, filter, and non-effect declarations. | Context only; no renderer object, raw property blob, evidence closure, policy decision, or release authority. |
| `EvidenceDrawerPayload` | Carries a closed public-safe projection with finite outcome, reason, evidence refs, citations, limitations, trust state, and bounded history. | Projection only; does not authenticate evidence, policy, review, release, or correction. |
| Adapter parameters | Supply a bounded decision ID, canonical evaluation time, and explicit fixture-only `SYSTEM_TEST` opt-in. | A caller-supplied role remains a declaration, not authenticated identity. |
| `DecisionEnvelope` candidate | Carries one finite render-admission posture with fixed safe reasons and obligations. | Candidate only; not `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, full API response, or public-use authorization. |

No new contract, schema, policy family, evidence object, release object, or publication authority is introduced.

### Emitted field surface

The current helper emits exactly:

```text
decision_id
id
outcome
decision
policy_family
reason_code
reasons
obligations
evidence_refs
evaluated_at
issued_at
version
```

`outcome` and `decision` match, `policy_family` is `render`, and `version` is the adapter version. The candidate does not copy drawer title, summary, citation URLs, limitations, history, renderer state, raw properties, geometry, or source text.

[Back to top](#top)

---

## 6. Admission sequence

Order matters because the helper fails closed at the earliest unsafe condition.

| Step | Check | Finite behavior |
|---:|---|---|
| 1 | Builder identity, evaluation-time syntax, object types, and exact input profiles | Unbuildable local input raises a bounded `EnvelopeBuildError`; the caller must convert it to a safe runtime error without reflecting untrusted input. |
| 2 | Context assembly, expiry, and evaluation ordering | Inconsistent time returns `ERROR`; expired context returns `ABSTAIN`. |
| 3 | Exact governance/non-effect field set, all `false` | Any overclaim returns `ERROR`. |
| 4 | Caller-role vocabulary and fixture-only `SYSTEM_TEST` opt-in | Unknown role returns `ERROR`; unadmitted `SYSTEM_TEST` returns `DENY`. |
| 5 | Selection cardinality | Zero selection returns `ABSTAIN`; multiple selections return `ABSTAIN`. |
| 6 | Canonical selected evidence and context evidence binding | Invalid or unbound selected evidence returns `ERROR`. |
| 7 | Exactly one selected layer, declared `PUBLISHED`, with a context-bound release ref | Unresolved, unpublished, or unbound layer declaration returns `ERROR`. |
| 8 | Drawer finite outcome, reason, trust state, evidence, citations, and history compatibility | Contradiction returns `ERROR`. |
| 9 | `ANSWER` or `ABSTAIN` drawer evidence is a subset of selected-feature evidence | Cross-selection support returns `ERROR`. |
| 10 | Candidate construction | Safe fixed reasons and obligations are emitted; DENY/ERROR support is stripped. |

The sequence validates local declarations and relationships. It does not turn any declaration into authenticated evidence, policy, review, release, or identity.

[Back to top](#top)

---

## Admission checks

The adapter checks these explicit relationships:

1. Both objects use the expected existing profiles.
2. Evaluation occurs after context assembly and no later than context expiry.
3. Every `MapContextEnvelope.governance` declaration exists and remains exactly `false`.
4. `SYSTEM_TEST` is denied unless the caller explicitly enables fixture-only use.
5. Exactly one selected feature is present; zero or multiple selections abstain.
6. The selected layer resolves exactly once, is declared `PUBLISHED`, and its release reference belongs to the context release set.
7. Selected evidence belongs to the context evidence set.
8. `ANSWER` and `ABSTAIN` drawer evidence is a subset of the selected feature's evidence, not merely any visible layer evidence.
9. Drawer outcome, reason, citations, history, and trust-state declarations are internally compatible with `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
10. `DENY` and `ERROR` never copy evidence, citations, history, title, summary, URL, limitation, or source text into the emitted candidate.
11. Reference arrays are canonical, sorted, duplicate-free, and free of denied RAW, WORK, QUARANTINE, canonical, internal, proof, or direct-model prefixes; individual refs are syntax-bounded.

These checks are deliberately narrower than the input contracts' full validation. The dedicated source validators remain the authority for each input profile.

[Back to top](#top)

---

## Finite outcomes

| Outcome | Representative current reasons | Candidate behavior |
|---|---|---|
| `ANSWER` | `SUPPORTED` | Carries only selected-feature-scoped evidence refs and obligations to display citations and preserve limitations. The candidate itself does not carry citation URLs or limitations. |
| `ABSTAIN` | `STALE_EVIDENCE`, `CONTEXT_EXPIRED`, `SELECTION_REQUIRED`, `SELECTION_AMBIGUOUS`, bounded unresolved/held/corrected states | Carries only safe selected-feature refs when the validated drawer profile permits them; otherwise carries none. Never fabricates an answer. |
| `DENY` | `SENSITIVE_DETAIL_RESTRICTED`, `POLICY_DENIED`, `CALLER_ROLE_DENIED` | Carries no evidence refs or drawer support content and requires safe denial display. |
| `ERROR` | `UPSTREAM_ERROR`, `CONTEXT_TIME_INCONSISTENT`, `CONTEXT_GOVERNANCE_INVALID`, `DRAWER_EVIDENCE_OUTSIDE_SELECTION`, `DRAWER_TRUST_STATE_MISMATCH`, invalid or unbound layer/evidence declarations | Carries no evidence refs or drawer support content and requires safe error display. |

### Outcome distinctions

- `ABSTAIN` means the boundary cannot safely support a current answer.
- `DENY` means the declared caller or public projection is prohibited.
- `ERROR` means the inputs or local relationship checks are inconsistent, malformed, or failed safely.
- `ANSWER` means only that the two validated declarations are locally aligned under this fixture-first profile.

No finite outcome from this helper is a release, policy, access, or publication decision.

[Back to top](#top)

---

## 9. Data minimization and no-leak behavior

The boundary minimizes what moves downstream.

### Candidate data that may survive

- stable decision identity;
- finite outcome and matching compatibility alias;
- fixed policy-family label;
- stable reason code plus fixed safe reason text;
- fixed obligations selected by outcome;
- selected-feature-scoped evidence refs for allowed `ANSWER` or bounded `ABSTAIN`;
- evaluation and issuance time;
- adapter version.

### Data that never survives

- drawer title or summary;
- citation labels or URLs;
- limitations;
- negative or correction history;
- rendered feature properties;
- geometry or coordinates;
- MapLibre or other renderer objects;
- style, paint, layout, feature-state, or camera internals;
- source snippets or generated prose;
- RAW, WORK, QUARANTINE, canonical/internal, proof-store, or direct-model references;
- evidence refs for `DENY` or `ERROR`.

Unknown reason text is not echoed. The helper converts an unrecognized reason to a fixed safe `ERROR / DRAWER_PAYLOAD_INVALID` candidate.

> [!WARNING]
> **Minimization is not redaction authority.** Sensitive geometry and protected attributes must be denied, transformed, or generalized before they reach either input. The adapter cannot make unsafe payload bytes public-safe after the fact.

[Back to top](#top)

---

## 10. Synthetic cases and executable proof

The current manifest contains exactly eight cases.

| Case | Expected outcome | Expected reason | Evidence projection |
|---|---|---|---|
| `answer-aligned` | `ANSWER` | `SUPPORTED` | Selected soil evidence ref retained. |
| `abstain-stale-aligned` | `ABSTAIN` | `STALE_EVIDENCE` | Selected stale evidence ref retained under the bounded drawer profile. |
| `deny-sensitive` | `DENY` | `SENSITIVE_DETAIL_RESTRICTED` | Empty. |
| `error-upstream` | `ERROR` | `UPSTREAM_ERROR` | Empty. |
| `answer-outside-selection` | `ERROR` | `DRAWER_EVIDENCE_OUTSIDE_SELECTION` | Empty. |
| `context-expired` | `ABSTAIN` | `CONTEXT_EXPIRED` | Empty. |
| `system-test-not-admitted` | `DENY` | `CALLER_ROLE_DENIED` | Empty. |
| `selection-required` | `ABSTAIN` | `SELECTION_REQUIRED` | Empty. |

Focused tests add direct checks for:

- all eight exact results;
- current `DecisionEnvelope` schema conformance;
- deterministic replay and input immutability;
- exact closed output fields;
- no title, summary, limitation, or citation-URL copying;
- ambiguous multiple-selection abstention;
- governance-overclaim failure;
- unpublished selected-layer failure;
- safe rejection of invalid decision identity and time;
- no-network execution through socket denial.

### What the proof means

A green focused run proves the current source code and synthetic packet behave as asserted for those cases. It does not prove:

- source or release authenticity;
- completeness of negative-case coverage;
- application integration;
- production network isolation;
- policy correctness;
- public safety for a real dataset;
- release, correction, rollback, deployment, or publication.

[Back to top](#top)

---

## 11. Runtime integration status

A current symbol search for `build_map_context_evidence_drawer_admission_candidate` returned only:

- the package implementation;
- the package export;
- the fixture replay validator; and
- the focused package tests.

No `apps/` caller was found. That makes the current runtime status:

```text
package helper: PRESENT
synthetic fixture profile: PRESENT
deterministic validator/tests: PRESENT
path-scoped workflow: PRESENT
Explorer/governed-API invocation: NOT ESTABLISHED
deployed invocation: UNKNOWN
public operation: NOT ESTABLISHED
```

The current Explorer `GovernedClient.ts` remains a fixture-only parser and explicitly performs no network or lifecycle-store access. It validates the drawer projection profile independently; it does not prove this Python admission helper is in the browser or API path.

### Required integration direction

A future integration must preserve this dependency direction:

```text
renderer selection candidate
  -> renderer-neutral MapContextEnvelope construction
  -> authoritative MapContext validation
  -> governed claim-resolution path
  -> evidence / policy / review / release checks
  -> public-safe EvidenceDrawerPayload construction
  -> authoritative drawer validation
  -> cross-object admission candidate
  -> governed response envelope
  -> browser rendering of finite state
```

The helper must not be wired as a browser-side substitute for the governed claim-resolution path.

[Back to top](#top)

---

## 12. Security, rights, and sensitivity boundary

| Risk | Current boundary | Remaining requirement |
|---|---|---|
| Direct internal-store access | Context references with RAW, WORK, QUARANTINE, canonical/internal, proof, and direct-model prefixes are rejected; the helper performs no store access. | Network, IAM, object-store, database, and deployment isolation remain unproved. |
| Cross-feature evidence confusion | Drawer support for `ANSWER` and `ABSTAIN` must be a subset of the selected feature's evidence. | Upstream evidence resolution must authenticate the referenced bundle and claim support. |
| Sensitive denial leakage | `DENY` carries no evidence refs or copied drawer content. | Policy must decide sensitivity and safe reason granularity before projection. |
| Error reflection | Unknown reason text and drawer content are not echoed into candidates. | API error middleware and logs must preserve the same no-reflection rule. |
| Test-role escape | `SYSTEM_TEST` is denied by default and requires an explicit fixture-only opt-in. | Production configuration must make the opt-in unreachable from public requests. |
| Caller-role spoofing | Role vocabulary is finite. | Identity, authentication, authorization, purpose, and audience checks must occur outside this helper. |
| Oversized or malformed fixture input | The replay validator rejects symlinks, non-files, duplicate keys, non-finite numbers, noncanonical paths, and payloads above its budget. | Production request budgets and parser controls remain separate work. |
| Stale or withdrawn public state | Drawer trust declarations can yield abstention/denial/error. | Current release, correction, withdrawal, cache, and rollback state must be resolved from authoritative stores. |

Rights, sovereignty, consent, cultural sensitivity, living-person data, genomics, rare-species locations, archaeology, infrastructure, private-property details, wells, and other harmful precision remain upstream fail-closed concerns. This adapter must never be used to infer permission from an absence of denial metadata.

[Back to top](#top)

---

## Non-effects

A successful adapter call, validator run, test, workflow, or documentation update does **not**:

- resolve `EvidenceRef` to `EvidenceBundle`;
- verify that a release reference exists, is active, or is public;
- evaluate rights, sensitivity, access, consent, purpose, audience, or render policy;
- authenticate a caller, reviewer, steward, signer, source, or release authority;
- create or approve a `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard`;
- authorize a capability, API response, map display, Focus Mode answer, export, cache, deployment, release, publication, or public use;
- read RAW, WORK, QUARANTINE, canonical, proof, graph, vector, model, catalog, release, or published stores;
- mutate repository, runtime, map, catalog, lifecycle, release, correction, or rollback state;
- prove that Explorer Web, the governed API, a renderer, or a deployed runtime invokes the helper;
- accept any proposed ADR, contract, schema, policy profile, or architecture choice.

[Back to top](#top)

---

## Directory Rules basis

Accepted ADR-0029 adopts Directory Rules v2 and makes `docs/` the human-readable documentation responsibility root. This is a same-path update to an existing architecture page.

| Responsibility | Home | Current posture |
|---|---|---|
| Human architecture explanation | `docs/architecture/ui/` | This page; `PLACE`. |
| Semantic meaning | `contracts/ui/` and `contracts/runtime/` | Existing proposed contracts; this page does not redefine them. |
| Machine shape | `schemas/contracts/v1/ui/` and `schemas/contracts/v1/runtime/` | Existing proposed schemas. |
| Reusable side-effect-minimal code | `packages/envelopes/src/envelopes/` | Existing helper and export. |
| Synthetic examples | `fixtures/ui/map_context_evidence_drawer_admission/` | Existing eight-case packet. |
| Operational fixture replay | `tools/validators/ui/` | Existing deterministic validator. |
| Package behavior tests | `tests/packages/envelopes/` | Existing focused tests. |
| Read-only hosted validation | `.github/workflows/` | Existing path-scoped workflow; this maintenance slice updates only its current receipt pointer and digest reporting. |
| AI authoring provenance | `data/receipts/generated/` | Immutable feature receipt plus a separate current docs-and-workflow receipt. |
| Policy, evidence, review, release, correction, rollback | Their owning roots and object families | Not created or modified here. |

The placement creates no new root and no parallel contract, schema, policy, evidence, source, registry, proof, receipt, release, correction, rollback, or publication authority.

[Back to top](#top)

---

## Validation

### Repository-native focused commands

The path-scoped workflow currently composes the relevant checks. Equivalent focused commands include:

```bash
python tools/validators/ui/validate_map_context_envelope.py \
  fixtures/ui/map_context_envelope/base_viewport.json

python tools/validators/ui/validate_map_context_envelope.py \
  fixtures/ui/map_context_envelope/base_geography.json

python tools/validators/ui/validate_evidence_drawer_payload.py \
  fixtures/ui/map_context_evidence_drawer_admission/payloads/answer-aligned.json

PYTHONPATH=packages/envelopes/src \
python -m pytest \
  tests/packages/envelopes/test_map_context_evidence_drawer_admission.py \
  -q --strict-config --strict-markers

python tools/validators/ui/validate_map_context_evidence_drawer_admission.py \
  --cases

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-map-context-evidence-drawer-admission-doc-workflow-20260819.json \
  --repo-root .
```

Repository-wide documentation, metadata, link, graph, topology, security, and aggregate checks remain applicable according to their path triggers and current workflow configuration.

### Source-confirmed validation coverage

The current source files show that focused validation is designed to check:

- both source profiles before cross-object replay;
- exact eight-case outcomes and reason codes;
- current `DecisionEnvelope` schema conformance;
- deterministic replay and input immutability;
- no drawer-content leakage;
- safe local parsing and path confinement;
- no-network behavior;
- generated-receipt integrity.

### Exact-head maintenance repair

The first hosted run for this maintenance pull request proved the source validators, all `10` focused tests, and all `8` exact replay cases, then failed only at generated-receipt integrity. The workflow was still validating the immutable 2026 feature receipt, whose original artifact set included the prior bytes of this documentation page. Updating the page therefore made that historical digest mismatch by design.

The bounded repair is to:

1. keep the original feature receipt immutable as lineage;
2. point the path-scoped workflow at the current docs-and-workflow authoring receipt;
3. bind both changed artifacts in that new receipt; and
4. preserve the same permissions, input validators, focused tests, replay, no-network posture, and trust-boundary summary.

This correction does not weaken the receipt gate. It restores the gate to the current authoring artifact set instead of rewriting history or pretending old bytes remain current.

### Needs verification for this documentation update

- exact-head hosted outcomes after the receipt-pointer repair;
- whether every relevant aggregate workflow is triggered and completes;
- whether any residual failure is introduced, inherited, or external;
- required-check and branch/ruleset coupling;
- human architecture, runtime, evidence, policy, release, accessibility, security, and validation review;
- host-rendered Markdown appearance.

A historical generated receipt reports focused PASS results for the original feature packet. That record is useful lineage, not a substitute for exact-current-head execution.

[Back to top](#top)

---

## 16. Graduation gates and verification backlog

The boundary must remain `BOUNDED_EXECUTABLE / INACTIVE_RUNTIME` until the following evidence closes.

| Priority | Required closure | Evidence needed |
|---:|---|---|
| P0 | Canonical input-contract and schema relationships | Reviewed disposition for the drawer UI/evidence semantic seam and any compatibility obligations. |
| P0 | Evidence resolution | A no-network repository abstraction first, then an admitted runtime resolver proving `EvidenceRef -> EvidenceBundle` closure or finite abstention/denial/error. |
| P0 | Render policy | Operative policy bundle, bounded reason/obligation vocabulary, positive and negative fixtures, and fail-closed tests. |
| P0 | Caller authority | Authenticated identity, role, purpose, audience, and `SYSTEM_TEST` isolation. |
| P0 | Active release and correction state | Authoritative release lookup, correction/withdrawal propagation, rollback target, and stale-cache behavior. |
| P0 | Governed runtime composition | One dependency-closed route or service path that validates both inputs, invokes the adapter, wraps the candidate in the governed response envelope, and never exposes internal stores. |
| P1 | Explorer integration | Renderer-neutral selection construction, governed transport, strict response parsing, finite-state rendering, and no direct model or lifecycle-store access. |
| P1 | Sensitive-domain proof | Synthetic fixtures proving upstream denial/generalization and no harmful-precision leakage. |
| P1 | Accessibility | Keyboard, focus, screen-reader, non-map alternative, error/denial copy, reduced-motion, and color-independent state tests. |
| P1 | Security and operations | Request budgets, authentication/authorization tests, CSP/CORS, network isolation, logging minimization, telemetry, incident response, and recovery. |
| P1 | End-to-end correction and rollback | Released candidate, correction or withdrawal, cache/search/map/AI propagation, and deterministic rollback rehearsal. |
| P2 | Performance and scale | Bounded latency, memory, concurrent-request, fixture-growth, and observability budgets without weakening fail-closed behavior. |
| P2 | Accountable stewardship | Verified owners, independent review route, maintenance expectations, deprecation policy, and operational runbook. |

### Graduation states

| State | Minimum meaning |
|---|---|
| `BOUNDED_EXECUTABLE` | Current helper, fixtures, validator, tests, and workflow exist; no runtime caller is established. |
| `INTEGRATED_CANDIDATE` | One governed no-network application path invokes the helper with authoritative input validators and finite response wrapping. |
| `RUNTIME_ADMITTED` | Identity, evidence, policy, release, correction, security, accessibility, and operational controls are reviewed and enforced. |
| `PUBLIC_OPERATION` | A separately governed release/deployment/publication transition has occurred with monitoring, correction, and rollback evidence. |

Documentation, a passing fixture, or a merged pull request cannot advance these states by itself.

[Back to top](#top)

---

## 17. Compatibility, correction, and rollback

### Compatibility

- The document ID, path, and H1 remain stable.
- The original headings `Why this boundary exists`, `Inputs and output`, `Admission checks`, `Finite outcomes`, `Non-effects`, `Directory Rules basis`, `Validation`, and `Rollback` remain present so existing generated GitHub fragments continue to resolve.
- No contract, schema, code, fixture, validator, test, package export, application, or runtime behavior changes in this maintenance slice.
- The only workflow delta repoints authoring-receipt validation from the immutable original feature receipt to the current docs-and-workflow receipt and records deterministic artifact digests; its permissions and admission-validation scope remain unchanged.
- The original feature receipt remains immutable and continues to describe the feature packet it hashed.
- The new docs-and-workflow receipt binds only the current documentation and workflow bytes and remains `human_review: pending` until an authorized reviewer acts.

### Documentation correction

If repository behavior changes, this page should be corrected in the same dependency order:

1. inspect the exact current implementation and accepted authority;
2. update the controlling contract, schema, policy, code, or decision in its owning root;
3. run the relevant executable checks;
4. reconcile this architecture page to the verified result;
5. emit a new authoring receipt rather than rewriting historical receipts;
6. preserve or explicitly migrate stable fragments and inbound links.

A correction to this page cannot silently upgrade a proposal to accepted architecture or a fixture to released behavior.

[Back to top](#top)

---

## Rollback

Before merge:

- close the draft pull request; and
- abandon or delete only its feature branch after confirming no other work depends on it.

After an authorized merge:

- revert the maintenance commits or merge commit through a reviewed pull request;
- restore prior target blob `32a9d4da2d778014e88033ab205ba08491c43ca0`;
- restore the workflow's original historical-receipt validation target;
- remove only the companion docs-and-workflow authoring receipt introduced by the same change; and
- rerun the same Markdown, metadata, link, generated-receipt, topology, security, and aggregate checks.

No data migration, source deactivation, lifecycle reprocessing, renderer rollback, API rollback, cache invalidation, release correction, withdrawal, public notice, or publication rollback is required because this update changes documentation, a validation receipt pointer, and authoring provenance only.

[Back to top](#top)

---

## Related documents

- [UI subsystem architecture README](./README.md)
- [UI boundaries](./BOUNDARIES.md)
- [Evidence Drawer architecture](./EVIDENCE_DRAWER.md)
- [Map runtime boundary](./MAP_RUNTIME_BOUNDARY.md)
- [`MapContextEnvelope` semantic contract](../../../contracts/ui/map_context_envelope.md)
- [`EvidenceDrawerPayload` semantic contract](../../../contracts/ui/evidence_drawer_payload.md)
- [`DecisionEnvelope` semantic contract](../../../contracts/runtime/decision_envelope.md)
- [Cross-object fixture packet](../../../fixtures/ui/map_context_evidence_drawer_admission/README.md)
- [Replay validator](../../../tools/validators/ui/validate_map_context_evidence_drawer_admission.py)
- [Focused package tests](../../../tests/packages/envelopes/test_map_context_evidence_drawer_admission.py)
- [Path-scoped workflow](../../../.github/workflows/map-context-evidence-drawer-admission.yml)
- [Original feature authoring receipt](../../../data/receipts/generated/genrec-map-context-evidence-drawer-admission-20260807.json)
- [Current docs-and-workflow authoring receipt](../../../data/receipts/generated/genrec-map-context-evidence-drawer-admission-doc-workflow-20260819.json)

[Back to top](#top)
