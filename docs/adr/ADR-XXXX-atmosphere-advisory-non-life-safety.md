<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-candidate/atmosphere-advisory-non-life-safety
title: "ADR-XXXX — Atmosphere Advisory Context Is Referral-Only and Not for Life Safety"
type: adr-candidate
adr_id: ADR-XXXX
version: v0.3
status: proposed
effective_decision_status: not-assigned
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — Atmosphere/Air domain steward"
  - "OWNER_TBD — Hazards and life-safety boundary steward"
  - "OWNER_TBD — governed API and public-surface steward"
  - "OWNER_TBD — evidence, policy, schema, and validation stewards"
  - "OWNER_TBD — release, correction, withdrawal, and rollback stewards"
owner_status: "The canonical ADR index classifies this file as an unassigned scaffold. Decision ownership, required reviewers, independent review, operational authority, and separation-of-duties assignments remain unverified."
reviewers_required:
  - Architecture steward
  - Docs steward
  - Atmosphere/Air domain steward
  - Hazards and life-safety boundary steward
  - Source and evidence steward
  - Contract and schema steward
  - Policy and sensitivity steward
  - Governed API and public-surface steward
  - Validation and CI steward
  - Release, correction, and rollback steward
created: 2026-05-19
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Record the proposed referral-only Atmosphere/Air advisory boundary and the evidence, policy, temporal, public-surface, correction, and rollback conditions required before any advisory context can be exposed."
current_path: docs/adr/ADR-XXXX-atmosphere-advisory-non-life-safety.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3e1a929a5e23f570b40c56e473b08ef65c3c5673
  target_prior_blob: df346a651b93f6402b35a0fed9a2c539fa6fb13c
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  advisory_contract_blob: 42e49000819e8777d6c58dd753e77b33049552c0
  advisory_compatibility_pointer_blob: 8ae7c47e64314cc8d1eef879b332e7a2a6da3bd1
  decision_envelope_contract_blob: e68e33e08bc9e2ea0373ecd07f471d8f8ea24d69
  atmosphere_schema_drift_readme_blob: e7efa6509a726422e7439d52c430c0808478f39c
  advisory_schema_pascal_blob: a53deeaa6814cecf5ff1bc9df7e95c87239dc1e1
  advisory_schema_snake_blob: b7faa2ca8624de3a00cf52d287c4130a9cba2762
  advisory_schema_kebab_blob: 65ea20bb57234cb1426bf52aa5e49f6635eb2629
  advisory_policy_underscore_blob: 0f46b314048f1b844ebed75fef21b911778bd47d
  advisory_policy_kebab_blob: cf744b1603c9422b8e51bbeb9e497e3f59541063
  advisory_test_blob: 8b90232802fb6f67bd7975d08a779023172f7744
inspection_boundary: >
  Current-session GitHub reads covered the exact target; canonical ADR operating
  contract and inventory; accepted Directory Rules decision and adopted bytes;
  canonical AdvisoryContext semantic contract; lowercase compatibility pointer;
  AtmosphereAirDecisionEnvelope contract; Atmosphere schema-drift index; three
  AdvisoryContext schema variants; two advisory policy scaffolds; the placeholder
  Atmosphere advisory test; and the valid/invalid fixture directories. No live
  advisory endpoint, policy evaluator, EvidenceBundle resolver, API route,
  MapLibre surface, Focus Mode runtime, notification service, release environment,
  cache, correction workflow, or deployed public client was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-template.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md
  - docs/domains/atmosphere/POLICY.md
  - docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - docs/domains/atmosphere/API_CONTRACTS.md
  - docs/domains/atmosphere/MAP_UI_CONTRACTS.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - contracts/domains/atmosphere/AdvisoryContext.md
  - contracts/domains/atmosphere/advisory-context.md
  - contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md
  - schemas/atmosphere/README.md
  - schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json
  - schemas/contracts/v1/domains/atmosphere/advisory_context.schema.json
  - schemas/contracts/v1/domains/atmosphere/advisory-context.schema.json
  - policy/domains/atmosphere/advisory_no_life_safety.rego
  - policy/domains/atmosphere/advisory-not-alert.rego
  - fixtures/domains/atmosphere/valid/advisory-context/README.md
  - fixtures/domains/atmosphere/invalid/README.md
  - tests/domains/atmosphere/test_advisory_no_life_safety.py
  - apps/explorer-web/src/features/domains/atmosphere/README.md
tags: [kfm, adr, atmosphere, air, advisory-context, life-safety, referral-only, source-role, temporal-state, fail-closed, governed-api, maplibre, focus-mode, correction, rollback]
notes:
  - "v0.3 is a same-path, documentation-only, repository-grounded refresh. It preserves ADR-XXXX and not-assigned status and does not accept, number, implement, release, deploy, or publish this decision."
  - "The canonical AdvisoryContext semantic contract is now confirmed at contracts/domains/atmosphere/AdvisoryContext.md; the lowercase contract file is a compatibility pointer rather than a competing semantic authority."
  - "The AdvisoryContext machine-shape family remains conflicted across PascalCase, snake_case, and kebab-case permissive scaffolds."
  - "The two inspected Rego files remain generated fail-closed scaffolds without decision logic or stable reason codes; the inspected test remains a docstring-only placeholder."
  - "Fixture directories contain documentation/placeholders rather than admitted advisory payloads."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-XXXX: Atmosphere Advisory Context Is Referral-Only and Not for Life Safety

> **Proposed decision.** KFM Atmosphere/Air may expose `AdvisoryContext` only as evidence-labeled, freshness-bounded referral context to a verified issuing authority. KFM must not become the issuer, transform advisory material into protective-action guidance, imply alert authority through presentation, or substitute generated interpretation for an official life-safety instruction.

[![Decision: not assigned](https://img.shields.io/badge/decision-not--assigned-6e7781?style=flat-square)](#status)
[![Candidate: proposed](https://img.shields.io/badge/candidate-proposed-d4a72c?style=flat-square)](#status)
[![Contract: canonical](https://img.shields.io/badge/semantic%20contract-canonical-1a7f37?style=flat-square)](#current-repository-evidence)
[![Schemas: conflicted scaffolds](https://img.shields.io/badge/schemas-3%20conflicted%20scaffolds-b42318?style=flat-square)](#schema-contract-policy-and-proof-maturity)
[![Policy: scaffold only](https://img.shields.io/badge/policy-scaffold%20only-f59e0b?style=flat-square)](#schema-contract-policy-and-proof-maturity)
[![Runtime: unverified](https://img.shields.io/badge/runtime-UNKNOWN-6e7781?style=flat-square)](#current-enforcement-maturity)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **The file exists; the decision is not assigned or accepted.** The canonical ADR index classifies this exact path as an explicit placeholder with decision status `not-assigned`. `ADR-XXXX` reserves no number. A commit, pull request, merge, contract, schema, policy-shaped file, test, workflow, map, API response, or disclaimer cannot assign or accept it by implication.

> [!CAUTION]
> **Repository prose is ahead of enforcement.** The canonical semantic contract and several domain documents describe referral-only behavior, but the current schema variants are permissive scaffolds, the inspected Rego modules contain no decision rules, the inspected test contains no assertions, and the fixture directories contain no admitted advisory payloads.

> [!WARNING]
> **A verified link is necessary but not sufficient.** A generic agency homepage, stale product URL, expired advisory, unresolved issuer, or generated restatement can still mislead. A public referral must resolve the specific issuing authority and product state required by the governing contract and release profile.

> [!NOTE]
> **Directory authority is confirmed.** Accepted [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). That makes `docs/adr/` the correct human decision-record lane; it does not accept this candidate or implement the advisory boundary.

**Quick navigation:** [Status](#status) · [Evidence boundary](#evidence-boundary) · [Repository evidence](#current-repository-evidence) · [Context](#context) · [Decision](#decision) · [Surface behavior](#public-surface-behavior) · [Boundaries](#responsibility-and-cross-lane-boundaries) · [Maturity](#current-enforcement-maturity) · [Conflicts](#conflict-and-hold-register) · [Options](#options-considered) · [Consequences](#consequences) · [Implementation](#implementation-and-convergence-plan) · [Acceptance](#validation-and-acceptance-gates) · [Risks](#risk-ledger) · [Authority](#authority-and-publication-boundary) · [Rollback](#rollback-correction-and-supersession) · [Verification](#verification-checklist) · [Open questions](#open-questions) · [References](#evidence-and-references) · [No-loss ledger](#appendix-a--no-loss-reconciliation-ledger)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **Candidate ID** | `ADR-XXXX` — explicit placeholder; no repository-wide number assigned |
| **Tracked path** | `docs/adr/ADR-XXXX-atmosphere-advisory-non-life-safety.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `not-assigned` |
| **Decision class** | Cross-component Atmosphere/Hazards trust-boundary and public-surface behavior |
| **Original scaffold** | 2026-05-19 |
| **First substantive candidate** | 2026-07-24 |
| **Current evidence refresh** | 2026-08-14 |
| **Deciders** | `OWNER_TBD` / `NEEDS VERIFICATION` |
| **Current semantic-contract posture** | Canonical `AdvisoryContext.md` confirmed; lowercase contract is a compatibility pointer |
| **Current machine-shape posture** | Three conflicting permissive schema scaffolds |
| **Current policy posture** | Two generated fail-closed scaffolds; no inspected decision logic or stable reason codes |
| **Current proof posture** | Placeholder test and documentation-only fixture lanes |
| **Current runtime posture** | `UNKNOWN` |
| **Implementation effect of this revision** | Documentation only |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Assignment, acceptance, implementation, and release are separate transitions

Four different states must remain visible:

1. **Number assignment** gives this candidate a collision-free repository-wide ADR ID and synchronizes the canonical index.
2. **ADR acceptance** approves the decision and its normative boundary.
3. **Implementation graduation** closes contract, schema, policy, fixture, validator, test, API, UI, AI, correction, and rollback gates.
4. **Governed release** authorizes a specific public-safe advisory-context product or surface.

None of these transitions implies the next. A numbered or accepted ADR can remain unimplemented. A passing fixture or workflow cannot accept the ADR. A complete implementation remains unreleased until the release decision and rollback path close.

### Governing placement authority

Accepted ADR-0029 and the adopted Directory Rules separate responsibilities as follows:

| Responsibility | Owning surface |
|---|---|
| Human architectural decision | `docs/adr/` |
| Domain explanation and public posture | `docs/domains/atmosphere/` and cross-lane Hazards docs |
| `AdvisoryContext` semantic meaning | `contracts/domains/atmosphere/AdvisoryContext.md` |
| Compatibility pointer for the legacy lowercase contract path | `contracts/domains/atmosphere/advisory-context.md` |
| Machine-checkable shape | `schemas/contracts/v1/domains/atmosphere/` after schema-family convergence |
| Allow, deny, restrict, hold, or abstain rules | `policy/domains/atmosphere/` plus an accepted shared life-safety policy where required |
| Deterministic examples | `fixtures/domains/atmosphere/` |
| Validator and test implementation | `tools/validators/` and `tests/` |
| Source identity, authority role, rights, and terms | Governed source descriptors and registries |
| Evidence resolution | Governing `EvidenceRef` / `EvidenceBundle` families |
| Public client delivery | Governed APIs and released public-safe artifacts |
| Release, correction, withdrawal, and rollback | `release/` and owning accountability families |

This same-path update changes no responsibility boundary and creates no parallel contract, schema, policy, source, registry, receipt, proof, release, or data authority.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in repository evidence at `main@3e1a929a5e23f570b40c56e473b08ef65c3c5673`. The prior target blob is `df346a651b93f6402b35a0fed9a2c539fa6fb13c`.

### Truth labels

| Label | Meaning in this candidate |
|---|---|
| **CONFIRMED** | Verified from the pinned repository bytes, canonical inventory, accepted ADR, or inspected artifact. |
| **PROPOSED** | The decision, field binding, policy behavior, implementation, migration, or release posture is not accepted and proven. |
| **UNKNOWN** | Available evidence does not support a stronger statement. |
| **NEEDS VERIFICATION** | A concrete repository, test, runtime, source, review, or release check remains. |
| **CONFLICTED** | Multiple writable or identity-bearing surfaces claim incompatible shape, name, or ownership. |
| **HOLD** | A deliberate fail-closed state pending authority, evidence, policy, validation, review, or release closure. |

### Inspection boundary

**Inspected:** target ADR, ADR operating contract and index, accepted Directory Rules decision, adopted Directory Rules bytes, canonical and compatibility AdvisoryContext contracts, Atmosphere decision-envelope contract, Atmosphere schema-drift index, three AdvisoryContext schemas, two policy files, the focused test, and valid/invalid fixture directories.

**Not exercised:** official advisory endpoints, source terms, source snapshots, policy evaluator, API resolver, EvidenceBundle resolver, MapLibre renderer, Evidence Drawer, Focus Mode runtime, notification service, export path, release tooling, cache invalidation, correction propagation, rollback drill, or deployed client.

A repository file proves that bytes exist at a revision. It does not by itself prove operational enforcement, source authority, rights clearance, evidence closure, release, deployment, or publication.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | CONFIRMED state at the evidence checkpoint | What it does **not** prove |
|---|---|---|
| [`docs/adr/INDEX.md`](./INDEX.md) | Lists this exact file as an explicit placeholder with status `not-assigned`. | Number assignment, acceptance, implementation, or release. |
| [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted; adopts exact Directory Rules v2 bytes and the responsibility-root split. | Acceptance of this advisory decision. |
| [`AdvisoryContext.md`](../../contracts/domains/atmosphere/AdvisoryContext.md) | Canonical draft semantic contract; defines advisory context as `ALERT_AND_ADVISORY_CONTEXT` and referral, not KFM life-safety instruction. | Machine validation, policy evaluation, runtime behavior, or release. |
| [`advisory-context.md`](../../contracts/domains/atmosphere/advisory-context.md) | Compatibility pointer to the canonical CamelCase contract; intentionally not a second semantic authority. | Consumer closure or permission to delete the compatibility path. |
| [`AtmosphereAirDecisionEnvelope.md`](../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md) | Draft finite-outcome contract for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`, with internal `HOLD` / `RESTRICT` posture. | A live route, DTO, schema, evaluator, or public response. |
| [`schemas/atmosphere/README.md`](../../schemas/atmosphere/README.md) | Repository-grounded schema compatibility and drift index; freezes new schema growth in compatibility lanes and records naming/$id conflicts. | A completed schema migration or accepted canonical file identity. |
| [`AdvisoryContext.schema.json`](../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json) | PascalCase scaffold; empty `properties`; `additionalProperties: true`; points to the canonical contract. | Required issuer, source, time, freshness, disclosure, evidence, or decision fields. |
| [`advisory_context.schema.json`](../../schemas/contracts/v1/domains/atmosphere/advisory_context.schema.json) | Snake-case scaffold; empty and permissive; different `$id`, source, and contract pointer. | Compatibility or semantic equivalence. |
| [`advisory-context.schema.json`](../../schemas/contracts/v1/domains/atmosphere/advisory-context.schema.json) | Kebab-case scaffold; empty and permissive; points to the compatibility contract. | Compatibility or semantic equivalence. |
| [`advisory_no_life_safety.rego`](../../policy/domains/atmosphere/advisory_no_life_safety.rego) | Generated `PROPOSED` scaffold with `default allow := false`. | Input contract, decision rules, reason codes, evaluator wiring, or public explanation. |
| [`advisory-not-alert.rego`](../../policy/domains/atmosphere/advisory-not-alert.rego) | A second generated `PROPOSED` scaffold with `default allow := false`. | Canonical policy identity or parity with the underscore file. |
| [`test_advisory_no_life_safety.py`](../../tests/domains/atmosphere/test_advisory_no_life_safety.py) | Contains a module docstring only. | Any executable assertion or enforcement proof. |
| [`valid/advisory-context/`](../../fixtures/domains/atmosphere/valid/advisory-context/README.md) | Contains a README and `.gitkeep`; no admitted payload was inspected. | Positive fixture coverage. |
| [`fixtures/domains/atmosphere/invalid/`](../../fixtures/domains/atmosphere/invalid/README.md) | Contains documentation/placeholders and unrelated fixture directories; no advisory-context negative payload was inspected. | Negative life-safety fixture coverage. |
| [`POLICY.md`](../domains/atmosphere/POLICY.md) and [`PUBLICATION_POSTURE.md`](../domains/atmosphere/PUBLICATION_POSTURE.md) | Describe referral-only and non-life-safety intent. | Executable or released behavior. |
| [`LIFE_SAFETY_BOUNDARY.md`](../domains/hazards/LIFE_SAFETY_BOUNDARY.md) | Describes the shared no-alert-authority boundary across Hazards, Hydrology, and Atmosphere/Air. | Final cross-lane field ownership or evaluator placement. |
| [Explorer Web Atmosphere README](../../apps/explorer-web/src/features/domains/atmosphere/README.md) | Describes contextual rendering and issuer referral. | Wired components, tested redirects, runtime policy, or released UI. |

### Evidence correction made by this revision

The prior candidate described the canonical contract path as conflicted. Current repository evidence narrows that claim:

- `contracts/domains/atmosphere/AdvisoryContext.md` is the semantic authority named by the paired PascalCase schema.
- `contracts/domains/atmosphere/advisory-context.md` explicitly declares itself a compatibility pointer and refuses parallel semantic authority.
- **Remaining contract work:** verify consumers and define compatibility retirement criteria; do not treat the lowercase path as a second contract.
- **Remaining schema conflict:** three independent schema identities still exist and remain permissive scaffolds.

[Back to top](#top)

---

<a id="context"></a>

## Context

Atmosphere/Air can carry useful context about agency advisories, watches, warnings, bulletins, smoke, forecasts, observations, and air-quality conditions. The same material becomes unsafe when a map, API, AI answer, export, search result, badge, or notification:

- presents KFM as the issuer;
- converts an observation, model, proxy, or advisory into protective-action guidance;
- hides issue, effective, expiry, cancellation, supersession, retrieval, or freshness state;
- points to a generic authority without resolving the specific product or current status;
- paraphrases source action language in KFM voice;
- uses urgency styling or delivery mechanics that imply KFM alert authority;
- treats a generated summary, link, schema pass, or map layer as evidence and release closure.

The repository consistently describes a referral-only boundary. It does not yet prove that the boundary is enforced end to end.

### Decision drivers

- **Cite or abstain** — a consequential advisory claim needs resolvable evidence and source identity.
- **Fail-safe public behavior** — a protective-action request cannot receive a “best effort” KFM answer.
- **Source-role integrity** — ingesting or rendering an agency advisory does not transfer issuing authority to KFM.
- **Temporal integrity** — current, historical, test, expired, cancelled, superseded, withdrawn, stale, and unknown states must not collapse.
- **Anti-impersonation** — wording, styling, ranking, notifications, and first-person voice must not imply KFM issuance.
- **Trust-membrane preservation** — maps, APIs, AI, exports, and notifications remain downstream carriers.
- **Cross-lane clarity** — Atmosphere owns atmospheric context; Hazards owns hazard-event and impact context; neither becomes an emergency alert system.
- **Correction and rollback** — stale or misattributed context must be withdrawable across every downstream projection.

### Scope

This candidate applies to public and semi-public Atmosphere/Air advisory context carried by:

- governed API responses;
- MapLibre layers, popups, panels, and Evidence Drawer payloads;
- Focus Mode or other governed-AI answers;
- search results and summaries;
- exports, screenshots, stories, and reports;
- notifications or subscriptions, if such a surface is separately admitted;
- release candidates and public artifacts.

### Out of scope

This candidate does not:

- assign itself an ADR number or accept itself;
- select the final source-role or knowledge-character vocabulary;
- define medical, exposure, evacuation, shelter, route, or protective-action guidance;
- decide the complete Atmosphere-versus-Hazards ownership of `SmokeContext`;
- authorize live source activation, alert ingestion, polling, notification delivery, release, deployment, or publication;
- select or delete one of the schema variants without an inventory-backed migration;
- replace contracts, schemas, policy, fixtures, validators, tests, evidence bundles, review records, release manifests, correction notices, or rollback cards;
- establish any official agency endpoint, product URL, terms, rights, or freshness threshold as current fact.

[Back to top](#top)

---

<a id="decision"></a>

## Decision

> [!IMPORTANT]
> **If assigned and accepted:** KFM Atmosphere/Air may expose `AdvisoryContext` only as evidence-labeled, freshness-bounded referral context. It must never act as the issuing authority or generate, translate, rank, summarize into action, or relay as KFM guidance any life-safety or protective-action instruction.

### Normative boundary

A conforming implementation must preserve all of the following:

1. **Referral, not issuance.** KFM identifies the external issuer and provides a verified source-specific referral; it does not issue the advisory.
2. **Context, not action.** KFM may explain bounded provenance, scope, status, and time state. It must not tell a user what protective action to take.
3. **Evidence before presentation.** Consequential claims resolve through the governing evidence path or return a finite non-answer outcome.
4. **Temporal state is explicit.** Currentness is never inferred from retrieval success, map visibility, or a static link.
5. **Source roles do not collapse.** Observations, forecasts, models, AQI, AOD, smoke context, and generated summaries cannot impersonate official advisory context.
6. **Presentation cannot impersonate authority.** Styling, urgency, notifications, ranking, audio, first-person voice, or generated paraphrase must not make KFM appear to be the issuer.
7. **Failure is closed.** Missing issuer, product, time state, evidence, policy, rights, review, release, or runtime support cannot fall back to generated guidance.
8. **Correction propagates.** Expiry, cancellation, withdrawal, supersession, misattribution, and correction must reach every public projection that carried the context.

### Required behavior by request or state

| Condition | Public resolver outcome | Required presentation |
|---|---|---|
| Informational, historical, provenance, or planning request with resolved evidence and release support | `ANSWER` may be allowed after policy, rights, sensitivity, freshness, review, and release gates pass. | Label the item as advisory context; disclose issuer, official source, status, temporal state, freshness, evidence, and the non-emergency boundary. |
| User asks KFM what to do about a current warning, exposure, evacuation, shelter, route, or other protective action | `DENY` with a stable life-safety or alert-authority reason code. | Refer to a verified official issuing or emergency authority; add no KFM-authored action guidance. |
| Issuer or source-specific official reference cannot be resolved | `ABSTAIN`, or `DENY` when the request itself is life-safety framing. | State that KFM cannot verify the referral. Never invent a source, URL, status, or instruction. |
| Advisory is expired, cancelled, superseded, withdrawn, stale, ambiguous, test-only, or missing required time state | `ABSTAIN`, `DENY`, or internal lifecycle/release `HOLD`, according to the surface contract. | Never render as current; preserve status and correction/supersession lineage. |
| Policy, rights, sensitivity, evidence, review, or release state is unresolved | `ABSTAIN` or `DENY`; internal `RESTRICT` / `HOLD` may block promotion. | Do not bypass the blocker through a map label, link, export, notification, or generated language. |
| Tool, resolver, policy, evidence, or source-check failure | `ERROR`. | Fail closed; do not fall back to uncited generated advice. |

### Public outcomes versus internal states

Public or user-facing resolver behavior remains finite:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

`HOLD` and `RESTRICT` are lifecycle, review, or policy states. They may prevent an object from reaching a public resolver, but they are not substitutes for the public response vocabulary unless an accepted API contract explicitly says otherwise.

### Minimum referral context

Before a public surface represents advisory context as current, the governed representation must resolve and disclose, at minimum:

| Requirement | Minimum expectation |
|---|---|
| Identity | Stable advisory-context identity plus source-native product identity where available |
| Knowledge character | Explicit advisory/referral character, not observation, model, forecast, proxy, or impact |
| Issuer | Verified issuing authority identity |
| Official reference | Source-specific official reference tied to the represented product or status |
| Source role and lineage | SourceDescriptor/source role, retrieval lineage, and relevant transformations |
| Time | Issue time, effective/valid interval, expiry where applicable, retrieval time, and freshness assessment |
| Status | Active, expired, cancelled, superseded, withdrawn, historical, test, or unknown |
| Disclosure | Text-equivalent statement that KFM is not the emergency-alert or life-safety authority |
| Evidence | EvidenceRef/EvidenceBundle support appropriate to the claim |
| Policy and rights | Policy decision, rights/terms posture, sensitivity, and obligations |
| Review and release | Required review state and release reference |
| Correction and rollback | Correction, supersession, withdrawal, and rollback references appropriate to the surface |

These are decision requirements, not claims that the current schemas implement them.

### Anti-paraphrase and anti-impersonation rule

KFM may expose source-provided identity, title, issuer, status, timestamps, public-safe metadata, and a verified referral when rights and release policy allow. KFM-generated text must not:

- restate protective-action language as KFM instruction;
- infer action from atmospheric evidence;
- present a generated recommendation as an official instruction;
- strip attribution or time state from source language;
- use first-person issuer voice;
- use urgency, color, sound, notification cadence, ranking, or badges to imply KFM alert authority.

A disclaimer does not cure unsafe behavior. If the content or presentation would otherwise function as KFM life-safety guidance, the outcome remains `DENY` plus a verified official referral.

[Back to top](#top)

---

<a id="public-surface-behavior"></a>

## Public-surface behavior

| Surface | Allowed referral behavior | Denied behavior | Required negative state |
|---|---|---|---|
| Governed API | Return finite outcome, issuer, official reference, time/freshness, status, evidence, and disclosure. | Raw source pass-through, invented URL, action guidance, or unsupported “current” claim. | `ABSTAIN`, `DENY`, or `ERROR` with stable reason code. |
| MapLibre / Evidence Drawer | Show contextual feature only from a released public-safe artifact; route to evidence and issuer. | Styling or popup text that implies issuance; client-only hiding of stale/denied context. | Hide, mark historical/stale, or show a bounded denied/abstained state. |
| Focus Mode / AI | Explain bounded context over released evidence; cite the issuer and evidence. | Paraphrase into action, infer protective steps, or answer after citation/policy failure. | `DENY` or `ABSTAIN`; `ERROR` on tool failure. |
| Search and summaries | Index released identity, issuer, status, scope, and correction state. | Rank or label as active without current-state proof; omit withdrawal/supersession. | Remove or mark stale/withdrawn and preserve correction lineage. |
| Export / story / screenshot | Preserve issuer, official reference, release ID, time state, disclosure, and correction state. | Detach a warning-like visual from its evidence and current status. | Block export or stamp a bounded historical/withdrawn state. |
| Notification | Only after a separately accepted contract, policy, source, and release profile proves safe referral behavior. | KFM-authored alerting, action language, or unverified urgency. | No notification; retain internal hold/denial receipt. |

No surface may read RAW, WORK, QUARANTINE, canonical/internal stores, or direct model output as its normal public path.

[Back to top](#top)

---

<a id="responsibility-and-cross-lane-boundaries"></a>

## Responsibility and cross-lane boundaries

### Atmosphere and Hazards

| Concern | Atmosphere/Air responsibility | Hazards responsibility | Shared prohibition |
|---|---|---|---|
| Atmospheric observation, model, forecast, smoke, AQI, or air-quality context | Own the domain object and its source-role semantics. | May reference as evidence or context for a hazard-event/impact claim. | Neither converts context into KFM-issued protective action. |
| Advisory referral | Own `AdvisoryContext` when the subject is atmospheric/air context. | May join to a hazard event or impact record without replacing advisory identity. | Preserve issuer, product identity, time, status, evidence, and release state. |
| Event and impact | May link to weather/air context. | Own hazard-event, impact, exposure, and emergency-management context. | Joining does not transfer alert authority to KFM. |
| Public response | Return finite outcome through governed surfaces. | Return finite outcome through governed surfaces. | Life-safety instruction is denied and referred to the verified official authority. |

### Source-role anti-collapse

The following are distinct and must remain separately typed:

```text
official advisory context
!= atmospheric observation
!= AQI report
!= concentration measurement
!= AOD proxy
!= forecast or model field
!= smoke context
!= hazard event
!= impact or exposure
!= generated summary
!= release decision
```

A relation or join may connect these objects. It must not overwrite their identities or authority roles.

[Back to top](#top)

---

<a id="schema-contract-policy-and-proof-maturity"></a>

## Schema, contract, policy, and proof maturity

### Contract posture

| Surface | Current result | Required convergence |
|---|---|---|
| Canonical semantic contract | **CONFIRMED** at `contracts/domains/atmosphere/AdvisoryContext.md` | Keep as the semantic authority unless a reviewed migration changes it. |
| Lowercase contract | **CONFIRMED compatibility pointer** | Inventory consumers, preserve one-way routing, define deprecation/retirement evidence; do not duplicate semantics. |
| Finite decision envelope | **CONFIRMED draft contract** | Align public outcomes and advisory reason codes with accepted shared runtime contracts. |

### Schema posture

Three AdvisoryContext schema files coexist. Each has a distinct path and `$id`, and each remains an empty permissive scaffold. This is a **CONFLICTED machine-shape family**, not three implementations.

The convergence decision must preserve:

- unique fields or metadata, if any;
- current consumers and references;
- stable object identity;
- canonical `$id`;
- contract linkage;
- versioning and compatibility policy;
- positive and negative fixtures;
- migration, correction, and rollback records.

No file should be selected or deleted by casing preference alone.

### Policy posture

Both inspected Rego files fail closed by default, but neither defines:

- a canonical input envelope;
- issuer/source validation;
- life-safety request classification;
- stale/expired/cancelled behavior;
- evidence/release checks;
- obligations;
- stable reason codes;
- public-safe explanations;
- evaluator or bundle wiring.

Their existence is a useful fail-closed scaffold, not executable advisory governance.

### Fixture and test posture

The valid advisory fixture lane contains documentation and `.gitkeep`. The general invalid lane contains placeholders and no inspected advisory-context negative payload. The focused Python test contains no assertions.

A documentation-only directory and a docstring-only test do not prove behavior.

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current status | Evidence-backed conclusion |
|---|---|---|
| Candidate identity | `CONFIRMED / not-assigned` | Exact file and index row exist; no number reserved. |
| Placement | `CONFIRMED` | Accepted ADR-0029 places the human decision in `docs/adr/`. |
| Semantic meaning | `DRAFT / repository-grounded` | Canonical contract defines referral-only meaning. |
| Contract compatibility | `PARTIAL` | Lowercase path is a pointer; consumer and retirement closure remain. |
| Machine shape | `CONFLICTED / scaffold` | Three permissive schema identities coexist. |
| Policy | `SCAFFOLD / fail-closed default` | Two modules exist without decision logic. |
| Positive fixtures | `ABSENT in inspected lane` | README and `.gitkeep` only. |
| Negative fixtures | `ABSENT for this boundary` | No advisory-context negative payload inspected. |
| Focused tests | `PLACEHOLDER` | Docstring only. |
| API binding | `UNKNOWN` | No live route or DTO behavior exercised. |
| Map/UI binding | `UNKNOWN` | README intent only. |
| AI binding | `UNKNOWN` | No model adapter or citation/policy path exercised. |
| Release/correction/rollback | `UNKNOWN` | No release candidate, correction propagation, or rollback drill inspected. |
| Public operation | `NOT ESTABLISHED` | No deployment or publication evidence. |

The current safe posture is therefore **documentation-backed intent with fail-closed scaffolding**, not operational enforcement.

[Back to top](#top)

---

<a id="conflict-and-hold-register"></a>

## Conflict and hold register

| ID | Status | Conflict or gap | Required resolution |
|---|---|---|---|
| `ADV-HOLD-001` | `HOLD` | Candidate has no assigned ADR number or accepted decision owner. | Check current index, open PRs, and branches; assign a collision-free number in a reviewed change if the decision is ready. |
| `ADV-HOLD-002` | `PARTIAL` | Canonical contract exists; lowercase pointer remains an active compatibility path. | Inventory consumers and define one-way compatibility exit criteria before retirement. |
| `ADV-CONFLICT-003` | `CONFLICTED` | Three AdvisoryContext schema paths and `$id` values coexist. | Inventory, compare, choose canonical identity through governed migration, and preserve compatibility. |
| `ADV-CONFLICT-004` | `CONFLICTED` | Two policy filenames/packages claim adjacent advisory boundaries. | Select or compose one accepted policy interface; preserve unique rules and reason-code behavior. |
| `ADV-HOLD-005` | `HOLD` | No admitted positive or negative advisory payloads. | Add synthetic, no-network fixtures with deterministic identities. |
| `ADV-HOLD-006` | `HOLD` | Focused test contains no assertions. | Add contract, schema, policy, outcome, temporal, and anti-impersonation assertions. |
| `ADV-HOLD-007` | `HOLD` | Public reason-code vocabulary is not accepted. | Define stable internal codes and bounded public explanations without leaking sensitive policy internals. |
| `ADV-HOLD-008` | `HOLD` | Official-source and currentness verification protocol is not proven. | Bind source descriptor, product identity, temporal state, retrieval, and freshness checks. |
| `ADV-HOLD-009` | `HOLD` | API, MapLibre, AI, export, notification, and cache behavior is unverified. | Add governed consumer contracts and representative tests for every admitted surface. |
| `ADV-HOLD-010` | `HOLD` | Release, correction, withdrawal, and rollback propagation is unproven. | Run a synthetic release/correction/withdrawal/rollback drill before public enablement. |

[Back to top](#top)

---

<a id="options-considered"></a>

## Options considered

### Option A — Referral-only context with fail-closed life-safety denial

**Selected by this proposal.** Preserve useful advisory identity, provenance, temporal state, and evidence context while directing life-safety needs to the verified official authority.

### Option B — Relay or summarize official instructions with a disclaimer

**Rejected.** A disclaimer does not cure stale state, source-role ambiguity, missing context, transformation error, rights uncertainty, or the impression that KFM vetted the instruction for action.

### Option C — Exclude all advisory material from KFM

**Rejected.** Total exclusion would remove useful historical, regulatory, provenance, correction, and planning context. The trust goal is bounded referral, not loss of inspectable source information.

### Option D — Move all Atmosphere advisory context to Hazards

**Rejected for this decision.** Atmosphere legitimately owns atmospheric observations, forecasts, model context, air-quality context, and their advisory relationships. Hazards owns event and impact context. A blanket move would erase that distinction without resolving the join model.

### Option E — Allow generated protective-action guidance when confidence is high

**Rejected.** Model confidence is not issuing authority, evidence closure, policy approval, or release authority. High-confidence generated advice would still violate the life-safety boundary.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Public and AI surfaces gain an explicit deny condition instead of a soft disclaimer.
- Official-source referrals remain useful without elevating KFM to issuer or interpreter.
- Issuer, source role, time, freshness, status, evidence, and release state become load-bearing.
- Atmosphere and Hazards retain distinct ownership while sharing the no-alert-authority invariant.
- Negative tests can target deterministic outcomes and stable reason codes.
- Correction, withdrawal, and rollback become part of advisory truth rather than afterthoughts.

### Costs and tradeoffs

- Some seemingly helpful requests must be denied even when KFM has relevant atmospheric evidence.
- Public clients need structured issuer, source, temporal, status, disclosure, evidence, and decision fields instead of one advisory string.
- Stale or incomplete source products will be hidden, marked historical, or withheld rather than shown optimistically.
- Cross-lane review is required for smoke, visibility, heat/cold, severe weather, and similar joins.
- Schema and policy convergence requires compatibility inventory and cannot be solved by deleting duplicate filenames.
- A notification surface carries a higher proof burden than a passive evidence drawer and may remain out of scope.

### Risks if implemented poorly

- A referral can become an unsafe relay if KFM reproduces or rewrites action language.
- A static official-source link can mislead if the represented product is expired, rescinded, or unrelated.
- A schema or workflow badge can be mistaken for evidence, policy, release, or publication.
- A UI can preserve disclaimer text while urgency styling still implies KFM authority.
- Generic denials without reason codes are hard to audit; overly detailed explanations can leak internal policy or confuse users.
- Correction that reaches the API but not maps, search, exports, caches, or AI retrieval leaves contradictory public state.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

This revision changes one existing Markdown file. It performs no schema, policy, fixture, test, API, UI, AI, data, release, deployment, or publication mutation.

If maintainers decide to advance the candidate, use the smallest dependency-closed sequence below.

### Phase 1 — Assign and review the decision

1. Recheck [`INDEX.md`](./INDEX.md), open pull requests, and active ADR branches.
2. Assign a collision-free numeric ADR ID and rename the file through a reviewed migration.
3. Update the filename, H1, metadata, canonical index, inbound links, and any register pointers together.
4. Name decision owners, affected stewards, required reviewers, and the acceptance evidence.
5. Keep status `proposed` until explicit review records acceptance or rejection.

### Phase 2 — Close semantic and identity drift

1. Preserve `AdvisoryContext.md` as canonical semantic authority unless a successor decision changes it.
2. Inventory consumers of the lowercase compatibility pointer.
3. Define compatibility duration, one-way routing, deprecation signal, and rollback.
4. Inventory all three schema files, `$id` values, metadata, consumers, and generated relationships.
5. Select one schema identity through an explicit migration; do not create a fourth shape.

### Phase 3 — Define enforceable shape and outcomes

1. Bind the canonical schema to the semantic contract and accepted finite decision envelope.
2. Require issuer, official-source reference, source role, identity, temporal state, freshness, status, disclosure, evidence, policy, review/release, correction, and rollback fields appropriate to significance.
3. Define stable reason codes for:
   - life-safety or protective-action request;
   - KFM issuer impersonation;
   - missing or unverified issuer/reference;
   - stale, expired, cancelled, withdrawn, superseded, test, or unknown state;
   - source-role collapse;
   - evidence, rights, policy, review, or release gap;
   - tool or evaluator failure.
4. Keep public explanations bounded and safe.

### Phase 4 — Implement fail-closed policy and proof

1. Select the canonical policy package/interface or compose the existing intent into one governed bundle.
2. Add synthetic, deterministic, no-network positive fixtures.
3. Add negative fixtures for every reason-code family.
4. Replace the docstring-only test with executable schema, policy, temporal, anti-paraphrase, and anti-impersonation assertions.
5. Add mutation/negative-path tests that fail if generated guidance, stale context, or unverified referrals pass.
6. Emit validation evidence without treating it as release proof.

### Phase 5 — Bind governed consumers

1. Governed API: return finite outcomes and required referral metadata.
2. Map/Evidence Drawer: render only released public-safe context and visible negative states.
3. Focus Mode: retrieve released evidence, validate citations, apply policy, and deny protective-action guidance.
4. Search/export: preserve issuer, time, release, and correction state.
5. Notifications: remain disabled unless a separate accepted contract and risk review admits them.

### Phase 6 — Release, correction, and rollback drill

1. Build a synthetic release candidate with an explicit rollback target.
2. Exercise expiry, cancellation, supersession, withdrawal, and misattribution corrections.
3. Verify propagation to API, map, search, export, cache, and AI retrieval.
4. Record the review and release decision separately from test and proof objects.
5. Enable no public surface until every applicable gate closes.

No lifecycle phase may be skipped:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Passing implementation remains a release candidate until governed promotion, review, release, correction, and rollback requirements close.

[Back to top](#top)

---

<a id="validation-and-acceptance-gates"></a>

## Validation and acceptance gates

### Current maturity and acceptance target

| Gate | Current result | Acceptance requirement |
|---|---|---|
| Same-path candidate and index inventory | `CONFIRMED` | Preserve `ADR-XXXX` and `not-assigned` until reviewed numbering. |
| Directory placement | `CONFIRMED` | Continue using `docs/adr/` under accepted ADR-0029. |
| Governing prose alignment | `CONFIRMED` | Atmosphere and Hazards references continue to agree on referral-only, no-alert-authority behavior. |
| Canonical semantic contract | `CONFIRMED draft` | Preserve `AdvisoryContext.md` as authority or record a reviewed migration. |
| Lowercase contract compatibility | `PARTIAL` | Verify consumers and retirement criteria; preserve one-way pointer behavior. |
| Canonical schema identity | `CONFLICTED` | Select one schema identity and migrate references without losing unique content. |
| Required schema fields | `FAIL / not implemented` | Require issuer, official reference, time/freshness/status, disclosure, evidence, and decision linkage. |
| Canonical policy interface | `CONFLICTED / scaffold` | Select or compose one fail-closed interface with stable reason codes and evaluator wiring. |
| Positive referral fixture | `FAIL / absent in inspected lane` | Add a synthetic current referral with no action guidance. |
| Negative life-safety fixtures | `FAIL / absent` | Cover issuance impersonation, protective action, missing referral, stale/expired/cancelled/superseded state, source-role collapse, and generated paraphrase. |
| Executable focused test | `FAIL / placeholder only` | Replace the docstring with assertions and negative-path coverage. |
| API/UI/AI binding | `UNKNOWN` | Verify every admitted surface preserves outcome, disclosure, issuer, evidence, and time/freshness state. |
| Release/correction/rollback proof | `UNKNOWN` | Complete a governed synthetic dry run before public enablement. |
| Human decision review | `PENDING` | Assign deciders and affected stewards; record explicit disposition. |

### Representative test matrix

| Test family | Positive case | Negative case | Expected result |
|---|---|---|---|
| Advisory referral | Verified issuer, product-specific reference, current interval, evidence, release, and disclosure | Missing or unverified issuer/reference | `ANSWER` only after all gates pass; otherwise `ABSTAIN` or `DENY` |
| Life-safety request | Informational provenance request | User asks KFM what protective action to take | `DENY` plus verified official referral; no KFM instruction |
| Temporal state | Current and non-superseded | Expired, cancelled, withdrawn, superseded, stale, test, or unknown rendered as current | Fail closed |
| Source-role integrity | Source-declared advisory context | Model, observation, AQI, AOD, smoke context, or generated summary presented as official advisory | `DENY` |
| Anti-paraphrase | Bounded provenance explanation | Generated text rewrites protective action in KFM voice | `DENY` |
| UI anti-impersonation | Context label, issuer, time, and official link remain visible | Urgency styling, sound, notification, ranking, or badge implies issuance | Release failure or `DENY` |
| Error behavior | Deterministic safe response | Tool/evaluator failure falls back to generated advice | `ERROR`; no advice |
| Correction propagation | Expired/withdrawn state reaches every projection | API updates but map/search/export/cache/AI remain stale | Release/correction failure |
| Compatibility | Canonical schema and pointer consumers continue under migration | One variant silently diverges or remains writable | Migration failure |

### Repository-native documentation validation

Run from repository root:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

These checks validate ADR inventory coherence for the checked revision. They do not assign or accept this candidate and do not prove advisory enforcement.

Where the repository provides changed-area Markdown, link, graph, metadata, or staleness checks, run those as well. A hosted check that is pending on a draft pull request is a delivery limitation, not evidence of failure or success.

[Back to top](#top)

---

<a id="risk-ledger"></a>

## Risk ledger

| Risk | Failure mode | Required mitigation |
|---|---|---|
| Alert-authority impersonation | KFM appears to issue a warning or instruction. | Stable denial rule, visible issuer, non-emergency disclosure, anti-impersonation UI tests. |
| False currentness | Expired or withdrawn product appears active. | Explicit status/time schema, freshness policy, correction propagation, cache invalidation. |
| Generic-link substitution | Agency homepage is treated as verified product referral. | Product-specific official-reference binding and source-state checks. |
| Source-role collapse | Model/proxy/observation becomes advisory. | Typed knowledge character, source role, contract/schema validation, negative fixtures. |
| Generated paraphrase | AI converts source text into action guidance. | Citation/policy pre- and post-checks; deny on protective-action framing. |
| Duplicate authority | Contract/schema/policy variants evolve independently. | Canonical identity, compatibility pointer, migration manifest, no parallel writes. |
| Proof inflation | Green tests or schema pass are treated as release. | Separate receipts, proofs, policy decisions, review, release, correction, and rollback. |
| Partial correction | One consumer updates while another remains stale. | Release manifest fan-out inventory and correction/rollback drill across all projections. |
| Sensitive reason leakage | Public denial reveals restricted policy or source details. | Stable internal reason codes plus bounded public explanations. |
| Notification escalation | Passive context becomes operational alerting. | Separate ADR/contract/policy review; notifications disabled by default. |

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

This candidate does not:

- assign or accept an ADR;
- authorize a source, endpoint, polling schedule, connector, or live feed;
- create or select a schema or policy authority;
- create evidence, review, proof, release, correction, or rollback records;
- enable a route, layer, Focus Mode answer, export, search index, or notification;
- establish KFM as an emergency, medical, air-quality, weather, or life-safety authority;
- publish or promote any data.

The durable public unit remains an inspectable claim supported by evidence, source role, spatial and temporal scope, policy, review, release, correction, and rollback. A map, link, advisory string, generated answer, or badge is a carrier, not sovereign truth.

[Back to top](#top)

---

<a id="rollback-correction-and-supersession"></a>

## Rollback, correction, and supersession

### This documentation change

Rollback is a transparent revert of the feature-branch commit or pull request. Because the path, candidate ID, and index classification remain unchanged, no path migration or index rollback is required.

### A future accepted implementation

If the decision is later assigned and accepted:

- implementation rollback must use transparent commits and the governing release rollback process;
- the deny-by-default boundary remains in force while a source, policy, API, UI, AI, or release defect is investigated;
- stale, withdrawn, misattributed, or incorrectly summarized context must enter correction/withdrawal handling;
- affected caches, exports, search results, map artifacts, indexes, notifications, and AI retrieval surfaces must be invalidated or corrected;
- source and product identity must remain traceable through correction;
- a material weakening or replacement requires a successor ADR with reciprocal supersession links;
- history must not be rewritten and an accepted ADR must not be silently edited into the opposite decision.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Candidate and governance

- [x] Existing target inspected at a pinned `main` commit.
- [x] Canonical ADR index confirms `not-assigned`.
- [x] No number assigned or reserved by this update.
- [x] Accepted ADR-0029 and Directory Rules placement checked.
- [x] Same path and H1 placeholder identity preserved.
- [ ] Decision owners and required reviewers assigned.
- [ ] Candidate assigned a collision-free number through reviewed index synchronization.
- [ ] Explicit acceptance or rejection recorded.

### Contract, schema, and policy

- [x] Canonical semantic contract identified.
- [x] Lowercase contract classified as compatibility pointer.
- [x] Three schema variants inspected and conflict retained.
- [x] Two policy scaffolds inspected.
- [ ] Schema identity and migration accepted.
- [ ] Policy input/output and stable reason codes accepted.
- [ ] Consumer and compatibility exit criteria proven.

### Proof and consumers

- [x] Focused test confirmed as placeholder.
- [x] Valid/invalid fixture lanes inspected.
- [ ] Positive and negative payloads added.
- [ ] Schema/policy/validator tests pass.
- [ ] API, MapLibre, Evidence Drawer, Focus Mode, export, search, and notification boundaries tested as applicable.
- [ ] Correction/withdrawal/rollback propagation drill passes.
- [ ] Release decision and rollback target exist before public enablement.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open questions

1. Which collision-free numeric ADR ID should be assigned after checking the current index, open pull requests, and active branches?
2. Who owns the decision, and which independent or cross-lane reviews are required?
3. What accepted schema filename, `$id`, version, and compatibility policy should replace the three current scaffold identities?
4. When may the lowercase contract pointer retire, and which consumers must migrate first?
5. Should the two policy files converge into one package, or do they represent distinct rules behind one public decision interface?
6. Which stable internal reason codes and bounded public explanations are canonical?
7. Where should the non-emergency disclosure and source-specific official reference bind: decision envelope, every advisory payload, layer manifest, or all applicable surfaces?
8. What source role and knowledge-character vocabulary represents operational advisory context?
9. Which shared policy and validator home governs the Hazards, Hydrology, and Atmosphere life-safety boundary without creating parallel authority?
10. How should Atmosphere advisory context join Hazards event/impact identity without duplication or overwrite?
11. What freshness rules apply by product family, and how are expiry, cancellation, supersession, and withdrawal detected?
12. Are source-provided action excerpts ever permitted as clearly attributed evidence, or is public behavior referral-metadata-only?
13. What proof burden would be required before admitting any notification surface?
14. What correction and cache-invalidation service owns downstream propagation?

[Back to top](#top)

---

<a id="evidence-and-references"></a>

## Evidence and references

### Governance

- [ADR operating contract](./README.md)
- [Canonical ADR index](./INDEX.md)
- [ADR template](./ADR-template.md)
- [ADR-0020 — Abstain Is a First-Class Decision](./ADR-0020-abstain-is-a-first-class-decision.md)
- [ADR-0025 — Public Client Never Reads Canonical or Internal Stores](./ADR-0025-public-client-never-reads-canonical-internal-stores.md)
- [Accepted ADR-0029 — Adopt Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)

### Atmosphere and cross-lane doctrine

- [Atmosphere planned-files register](../domains/atmosphere/MISSING_OR_PLANNED_FILES.md)
- [Atmosphere Policy](../domains/atmosphere/POLICY.md)
- [Atmosphere Publication Posture](../domains/atmosphere/PUBLICATION_POSTURE.md)
- [Atmosphere API Contracts](../domains/atmosphere/API_CONTRACTS.md)
- [Atmosphere Map/UI Contracts](../domains/atmosphere/MAP_UI_CONTRACTS.md)
- [Atmosphere Knowledge Characters](../domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [Hazards Life-Safety Boundary](../domains/hazards/LIFE_SAFETY_BOUNDARY.md)

### Contracts and schemas

- [Canonical AdvisoryContext semantic contract](../../contracts/domains/atmosphere/AdvisoryContext.md)
- [AdvisoryContext compatibility pointer](../../contracts/domains/atmosphere/advisory-context.md)
- [AtmosphereAirDecisionEnvelope semantic contract](../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md)
- [Atmosphere schema compatibility and drift index](../../schemas/atmosphere/README.md)
- [PascalCase AdvisoryContext schema scaffold](../../schemas/contracts/v1/domains/atmosphere/AdvisoryContext.schema.json)
- [Snake-case AdvisoryContext schema scaffold](../../schemas/contracts/v1/domains/atmosphere/advisory_context.schema.json)
- [Kebab-case AdvisoryContext schema scaffold](../../schemas/contracts/v1/domains/atmosphere/advisory-context.schema.json)

### Policy, fixtures, tests, and public surface

- [Atmosphere advisory no-life-safety policy scaffold](../../policy/domains/atmosphere/advisory_no_life_safety.rego)
- [Atmosphere advisory-not-alert policy scaffold](../../policy/domains/atmosphere/advisory-not-alert.rego)
- [Valid advisory-context fixture lane](../../fixtures/domains/atmosphere/valid/advisory-context/README.md)
- [Invalid Atmosphere fixture lane](../../fixtures/domains/atmosphere/invalid/README.md)
- [Atmosphere advisory test placeholder](../../tests/domains/atmosphere/test_advisory_no_life_safety.py)
- [Explorer Web Atmosphere feature boundary](../../apps/explorer-web/src/features/domains/atmosphere/README.md)

[Back to top](#top)

---

## Change history

| Date | Change | Status |
|---|---|---|
| 2026-05-19 | Added the planned ADR scaffold from the Atmosphere documentation inventory. | `not-assigned` |
| 2026-07-24 | Replaced the 11-line scaffold with a same-path, evidence-grounded candidate; preserved `ADR-XXXX` and `not-assigned`; added decision, options, consequences, implementation gates, validation, rollback, conflicts, and open questions. | `proposed / not-assigned` |
| 2026-08-14 | Added document control, current main/blob evidence, accepted Directory Rules placement, assignment/acceptance/implementation/release separation, corrected canonical-contract status, preserved schema and policy conflicts, expanded public-surface behavior, convergence phases, acceptance gates, risk ledger, verification checklist, and no-loss reconciliation. | `proposed / not-assigned` |

---

## Appendix A — No-loss reconciliation ledger

| Prior material | Disposition | Current location |
|---|---|---|
| Referral-only one-paragraph rule | `KEEP + STRENGTHEN` | Title, proposed decision, normative boundary |
| Unassigned / not-accepted warning | `KEEP + EXPAND` | Status and assignment/acceptance separation |
| Evidence boundary | `REFRESH` | Current commit, blob identities, inspection limits |
| Decision drivers | `KEEP + EXPAND` | Context |
| Scope and out-of-scope | `KEEP + CLARIFY` | Context |
| Finite outcome table | `KEEP + ALIGN` | Decision and public outcomes/internal states |
| Minimum referral context | `KEEP + STRUCTURE` | Decision requirements table |
| Anti-paraphrase / anti-impersonation rule | `KEEP + EXPAND` | Decision and public-surface behavior |
| Responsibility boundaries | `KEEP + RECONCILE` | Status and cross-lane boundaries |
| Four original options | `KEEP` | Options A–D |
| Generated-advice option | `ADD` | Option E |
| Positive consequences, costs, and risks | `KEEP + EXPAND` | Consequences and risk ledger |
| Implementation order | `KEEP + DEPENDENCY-CLOSE` | Six-phase convergence plan |
| Current maturity table | `REFRESH` | Corrected contract status; schema/policy/test gaps retained |
| Representative tests | `KEEP + EXPAND` | Acceptance test matrix |
| ADR index validation commands | `KEEP` | Validation section |
| Rollback, correction, and supersession | `KEEP + EXPAND` | Rollback section |
| Open questions | `KEEP + REFINE` | Open questions |
| Evidence links | `KEEP + EXPAND` | References |
| Prior history row | `KEEP` | Change history |

[Back to top](#top)
