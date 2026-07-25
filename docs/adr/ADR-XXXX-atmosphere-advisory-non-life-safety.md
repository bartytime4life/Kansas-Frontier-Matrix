<a id="adr-xxxx-atmosphere-advisory-non-life-safety"></a>

# ADR-XXXX: Atmosphere Advisory Context Is Referral-Only and Not for Life Safety

Atmosphere/Air may present governed advisory context and a verified link to the issuing authority, but KFM must not issue, interpret, paraphrase as action, or replace an official alert or life-safety instruction.

> [!CAUTION]
> This is an **unassigned proposed ADR candidate**, not an accepted decision or proof of enforcement. `ADR-XXXX` is a placeholder; the repository index classifies this file as `not-assigned`. The current policy, schema, fixture, test, API, and UI gaps in [Validation and acceptance gates](#validation-and-acceptance-gates) must remain visible until independently closed.

**Quick links:** [Status](#status) · [Context](#context) · [Decision](#decision) · [Options](#options-considered) · [Consequences](#consequences) · [Implementation](#implementation-and-migration) · [Validation](#validation-and-acceptance-gates) · [Rollback](#rollback-correction-and-supersession) · [Open questions](#open-questions) · [References](#evidence-and-references)

## Status

| Field | Value |
| --- | --- |
| **ID** | `ADR-XXXX` - unassigned placeholder |
| **Decision status** | `proposed` / `not-assigned` |
| **Date** | 2026-07-24 |
| **Deciders** | NEEDS VERIFICATION |
| **Affected stewards** | Atmosphere, Hazards/life-safety, governed API, UI, policy, evidence, validation, release, correction, and rollback stewards - assignments NEED VERIFICATION |
| **Supersedes** | None verified |
| **Superseded by** | None |
| **Directory Rules classification** | Non-structural, cross-component trust-boundary decision; canonical human record belongs in `docs/adr/` |
| **Primary responsibility root** | `docs/` |
| **Path migration** | No; this candidate remains at its existing scaffold path until a reviewed numbering decision |
| **Truth posture** | CONFIRMED repository evidence / PROPOSED decision / UNKNOWN runtime enforcement / NEEDS VERIFICATION before acceptance |

This candidate preserves the original scaffold's source relationship to [`docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`](../domains/atmosphere/MISSING_OR_PLANNED_FILES.md), which describes the intended decision as: AdvisoryContext is referral-only and Atmosphere/Air produces no life-safety output.

## Context

KFM's Atmosphere/Air lane can carry useful context about agency advisories, watches, warnings, bulletins, smoke, forecasts, observations, and air-quality conditions. The same material becomes unsafe when a map, API, AI answer, export, or notification presents KFM as the issuer, converts source material into protective-action guidance, hides expiry or freshness, or substitutes a derived summary for the official source.

The repository already states the intended boundary in several human-facing documents. It does not yet prove that boundary is enforced end to end.

### Evidence boundary

The following snapshot was inspected at `main@fc0f77ac32103ee355c1e595b6e554267930ed14`; the prior target blob was `ac6a5efb19fffbc5df4bcf52642417edf5a01ece`.

| Evidence | CONFIRMED observation | Limit |
| --- | --- | --- |
| [`MISSING_OR_PLANNED_FILES.md`](../domains/atmosphere/MISSING_OR_PLANNED_FILES.md) | Lists this exact ADR path and the referral-only decision. | Planning evidence does not accept the ADR. |
| [`AdvisoryContext.md`](../../contracts/domains/atmosphere/AdvisoryContext.md) | Defines advisory context as a governed referral, not KFM-issued life-safety guidance. | The contract is draft and does not prove runtime behavior. |
| [`POLICY.md`](../domains/atmosphere/POLICY.md) | States that advisory context must not become life-safety instruction and should redirect to the authoritative source. | It describes policy intent, not executable enforcement. |
| [`PUBLICATION_POSTURE.md`](../domains/atmosphere/PUBLICATION_POSTURE.md) | Requires referral-only presentation, an official-source redirect, and no KFM life-safety instruction. | It does not prove release-gate implementation. |
| [`LIFE_SAFETY_BOUNDARY.md`](../domains/hazards/LIFE_SAFETY_BOUNDARY.md) | Makes protective-action and alert-authority framing a deny condition shared by Hazards, Hydrology, and Atmosphere/Air. | Several field bindings and cross-lane policy homes remain open. |
| [`advisory_no_life_safety.rego`](../../policy/domains/atmosphere/advisory_no_life_safety.rego) and [`advisory-not-alert.rego`](../../policy/domains/atmosphere/advisory-not-alert.rego) | Both files exist and default to deny. | Both are generated `PROPOSED` scaffolds without decision logic or reason-code behavior. |
| [`test_advisory_no_life_safety.py`](../../tests/domains/atmosphere/test_advisory_no_life_safety.py) | The expected test path exists. | It contains only a module docstring; no executable test establishes enforcement. |
| AdvisoryContext schemas | Three named variants exist and are permissive scaffolds with empty `properties` and `additionalProperties: true`. | No inspected schema requires issuer, official-source reference, expiry, freshness, disclosure, or outcome fields. |
| [`apps/explorer-web` Atmosphere README](../../apps/explorer-web/src/features/domains/atmosphere/README.md) | Specifies contextual rendering and official-issuer redirection. | The README explicitly leaves feature wiring, redirects, fixtures, and runtime behavior unverified. |

### Decision drivers

- **Cite-or-abstain:** relevant evidence must resolve before KFM presents a consequential claim.
- **Fail-safe public behavior:** protective-action requests cannot receive a bounded "best effort" answer from KFM.
- **Source-role integrity:** an agency-issued advisory remains external authority context; KFM does not inherit issuing authority by ingesting or displaying it.
- **Time awareness:** issue, effective, expiry, cancellation, supersession, retrieval, and freshness state must not collapse into one timestamp or an unlabeled "current" state.
- **Trust-membrane preservation:** maps, AI text, API envelopes, exports, notifications, and badges are downstream carriers, not sovereign truth or publication authority.
- **Cross-lane clarity:** Atmosphere owns atmospheric context; Hazards owns hazard-event and impact context; neither lane becomes an emergency alert system.

### Scope

This decision applies to Atmosphere/Air advisory context on public or semi-public KFM surfaces, including governed API responses, Focus Mode or other AI answers, the map and Evidence Drawer, exports, search results, notifications, release candidates, and public artifacts.

### Out of scope

This ADR does not:

- choose the final knowledge-character enum or source-role vocabulary;
- decide the Atmosphere-versus-Hazards ownership of `SmokeContext`;
- select one of the duplicate AdvisoryContext contract or schema filenames;
- define medical, exposure, evacuation, shelter, or protective-action guidance;
- authorize live alert ingestion, notification delivery, public release, deployment, or publication;
- replace contracts, schemas, policy, fixtures, validators, tests, evidence bundles, review records, release manifests, correction notices, or rollback cards.

## Decision

> [!IMPORTANT]
> **PROPOSED decision:** KFM Atmosphere/Air may expose `AdvisoryContext` only as evidence-labeled, freshness-bounded referral context. It must never act as the issuing authority or generate, translate, rank, summarize into action, or relay as KFM guidance any life-safety or protective-action instruction.

### Required behavior by request or state

| Condition | Required governed outcome | Required presentation |
| --- | --- | --- |
| Informational, historical, or planning request with resolved evidence and release support | `ANSWER` may be allowed after policy, rights, sensitivity, freshness, review, and release gates pass. | Clearly label advisory context; show issuer, official source reference, temporal state, freshness, and the non-emergency boundary. |
| Request asks what to do about a current warning, exposure, evacuation, shelter, route, or other protective action | `DENY` with a stable life-safety or alert-authority reason code. | Refer to a verified official issuing or emergency authority; do not add KFM-authored action guidance. |
| Official source reference or issuing authority cannot be resolved | `ABSTAIN` for the advisory claim, or `DENY` when the request itself is life-safety framing. | State that KFM cannot verify the referral; never invent a source, URL, status, or instruction. |
| Advisory is expired, cancelled, superseded, withdrawn, stale, ambiguous, or missing required time state | Fail closed through `ABSTAIN`, `DENY`, or a lifecycle/release `HOLD`, according to the governing surface contract. | Do not render it as current; preserve status and correction/supersession lineage. |
| Policy, evidence, rights, sensitivity, review, or release state is unresolved | `ABSTAIN`, `DENY`, `RESTRICT`, or lifecycle `HOLD`, as defined by the governing contract. | Do not bypass the blocker through generated language, a map label, an export, or a direct source link. |
| Tool or runtime failure | `ERROR`. | Fail closed; do not fall back to uncited generated advice. |

`HOLD` and `RESTRICT` are lifecycle or policy states, not substitutes for the public response outcomes `ANSWER | ABSTAIN | DENY | ERROR` unless an accepted surface contract explicitly defines otherwise.

### Minimum referral context

Before a public surface shows advisory context as current, the governed representation must be able to resolve and disclose, at minimum:

- advisory identity and knowledge character;
- issuing authority and verified official-source reference;
- source role and source lineage;
- issue time, effective/valid interval, expiry when applicable, retrieval time, and freshness state;
- active, expired, cancelled, superseded, withdrawn, historical, test, or unknown status;
- the text-equivalent disclosure that KFM is not the emergency alert or life-safety authority;
- EvidenceRef/EvidenceBundle support appropriate to the claim;
- policy, rights, sensitivity, review, release, correction, and rollback references required by the governing surface.

These are decision requirements, not claims that the current schemas already implement them.

### Anti-paraphrase and anti-impersonation rule

KFM may show source-provided identifiers, title, issuer, status, timestamps, public-safe metadata, and a verified link when rights and release policy allow. KFM-generated text must not restate protective-action language as KFM instruction, infer an action from atmospheric evidence, or use styling, notifications, urgency ranking, or first-person voice that implies KFM issued the advisory.

A disclaimer alone does not make unsafe guidance acceptable. If the content would otherwise be a life-safety instruction, the outcome remains `DENY` plus referral.

### Responsibility boundaries

| Responsibility | Owning surface |
| --- | --- |
| AdvisoryContext semantic meaning | [`contracts/domains/atmosphere/`](../../contracts/domains/atmosphere/) |
| Machine-checkable shape | [`schemas/contracts/v1/domains/atmosphere/`](../../schemas/contracts/v1/domains/atmosphere/) after canonical-path reconciliation |
| Allow, deny, restrict, hold, and abstain decisions | [`policy/domains/atmosphere/`](../../policy/domains/atmosphere/) plus verified cross-lane policy where required |
| Deterministic proof of behavior | [`tests/domains/atmosphere/`](../../tests/domains/atmosphere/) and [`fixtures/domains/atmosphere/`](../../fixtures/domains/atmosphere/) |
| Advisory source identity, rights, terms, and authority role | Governed source descriptors and registries |
| Evidence support | `data/proofs/` through resolvable EvidenceRefs/EvidenceBundles |
| Public client delivery | Governed APIs and released public-safe artifacts |
| Hazard-event and impact context | Hazards lane, without alert-authority status |
| Release, correction, withdrawal, and rollback decisions | [`release/`](../../release/) |

Directory Rules places this human decision record in `docs/adr/`. It does not authorize parallel contract, schema, policy, source, registry, release, proof, or receipt homes.

## Options considered

### Option A - Referral-only context with fail-closed life-safety denial

**Selected.** Preserve useful advisory metadata and evidence context while directing life-safety needs to the verified official authority. This keeps the boundary explicit across API, UI, map, AI, export, release, and correction surfaces.

### Option B - Relay or summarize official instructions with a disclaimer

**Rejected.** A disclaimer does not cure stale state, source-role ambiguity, incomplete context, transformation error, or the impression that KFM vetted the instruction for life-safety use. Relaying action language would move KFM back into the denied authority role.

### Option C - Exclude all advisory material from KFM

**Rejected.** Total exclusion would remove useful historical, regulatory, planning, freshness, and provenance context. The trust goal is governed referral and bounded context, not loss of inspectable source information.

### Option D - Move all Atmosphere advisory context to Hazards

**Rejected for this decision.** Atmosphere legitimately owns atmospheric observations, modeled context, air-quality reporting context, and their advisory relationships. Hazards owns hazard-event and impact context. Moving all advisory context would erase that distinction without resolving the separate cross-lane object and join questions.

## Consequences

### Positive

- Public and AI surfaces have an explicit deny condition instead of a soft disclaimer.
- Official-source referrals remain useful without elevating KFM to issuer or interpreter.
- Time, freshness, source role, evidence, and release state remain load-bearing.
- Atmosphere and Hazards retain distinct responsibilities while sharing the no-alert-authority invariant.
- Negative tests can target deterministic outcomes and stable reason codes.

### Costs and tradeoffs

- Some seemingly helpful requests must be denied even when KFM has relevant atmospheric evidence.
- Public clients need issuer, official-source, temporal, freshness, status, evidence, and decision fields instead of a single advisory string.
- Stale or incomplete advisory feeds will be hidden, marked historical, or withheld rather than presented optimistically.
- Cross-lane review is required for smoke, visibility, heat/cold, and similar Atmosphere-Hazards joins.
- The current duplicate contract/schema names and placeholder enforcement files must be reconciled before acceptance.

### Risks if implemented poorly

- A referral can become an unsafe relay if KFM reproduces or rewrites action language.
- A static official-source link can mislead if the specific product is expired or withdrawn.
- A green schema or CI badge can be mistaken for evidence, policy approval, release, or publication.
- A UI may preserve the words of the disclaimer while urgency styling or notifications still imply KFM authority.
- Generic `DENY` behavior without safe reason codes may be hard to audit or test.

## Implementation and migration

This one-file ADR modernization performs no runtime, schema, policy, test, UI, data, release, or publication mutation. If the decision is assigned and accepted, implementation should proceed through the owning roots in this order:

1. Assign a collision-free numeric ADR ID and update the ADR index in the same reviewed change.
2. Reconcile the duplicate AdvisoryContext contract and schema paths without creating another authority surface.
3. Define the canonical AdvisoryContext machine shape and finite decision-envelope binding.
4. Implement fail-closed policy with stable reason codes for alert-authority substitution, life-safety instruction, missing official referral, stale/expired state, and evidence/release gaps.
5. Add synthetic, deterministic, no-network positive and negative fixtures.
6. Replace placeholder tests with executable contract, policy, API, and UI boundary tests.
7. Bind the disclosure and official-source referral through governed API, map/Evidence Drawer, Focus Mode, export, and any notification surface.
8. Add release, correction, withdrawal, stale-state, and rollback gates; then perform human review before any public enablement.

No lifecycle phase may be skipped. A passing implementation remains a release candidate until governed promotion, review, release, correction, and rollback requirements close.

## Validation and acceptance gates

### Current maturity

| Gate | Current result | Acceptance requirement |
| --- | --- | --- |
| Same-path ADR candidate | CONFIRMED | Preserve path until reviewed numbering; keep index classification `not-assigned`. |
| Governing prose alignment | CONFIRMED | Atmosphere and Hazards references continue to agree on referral-only, no-alert-authority behavior. |
| Canonical contract path | CONFLICTED | Select one canonical contract and document compatibility or migration for the other. |
| Canonical schema path | CONFLICTED | Select one canonical schema; remove permissive parallel evolution through reviewed migration. |
| Required schema fields | FAIL / not implemented | Require issuer, official source, time/freshness/status, disclosure, evidence, and decision linkage. |
| Executable policy | FAIL / scaffold only | Implement deterministic deny/abstain/hold behavior and reason codes. |
| Positive referral fixture | NEEDS VERIFICATION | Add a synthetic current advisory-context referral with no action guidance. |
| Negative life-safety fixtures | FAIL / absent | Cover KFM-issued warning, protective-action request, missing referral, stale/expired/cancelled context, and generated paraphrase. |
| Executable Atmosphere test | FAIL / placeholder only | Replace the docstring-only test with assertions that fail if the boundary is bypassed. |
| API/UI/AI binding | UNKNOWN | Verify every public surface preserves outcome, disclosure, official source, and temporal/freshness state. |
| Release/correction/rollback proof | UNKNOWN | Require governed records and at least one dry-run before public enablement. |
| Human decision review | PENDING | Assign deciders and affected stewards; record explicit disposition. |

### Required representative tests

| Test family | Positive case | Negative case | Expected outcome |
| --- | --- | --- | --- |
| Advisory referral | Verified issuer, official reference, current interval, evidence, and disclosure | Missing or unverified issuer/reference | `ANSWER` only when all gates pass; otherwise `ABSTAIN` or `DENY` |
| Life-safety request | Not applicable | User asks KFM what protective action to take | `DENY` plus verified official referral, no KFM instruction |
| Temporal state | Current, non-superseded context | Expired, cancelled, withdrawn, superseded, stale, or unknown state rendered as current | Fail closed |
| Source-role integrity | Source-declared advisory context | Model, observation, AQI, AOD, or generated summary presented as official advisory | `DENY` |
| UI/AI anti-impersonation | Context label and official-source link remain visible | KFM voice, urgency styling, notification, or paraphrase implies issuer status | `DENY` or release failure |
| Error behavior | Deterministic safe response | Tool failure falls back to generated advice | `ERROR`, no advice |

Repository-native ADR index validation remains applicable:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

Passing those checks proves index coherence only. It does not accept this decision or prove advisory enforcement.

## Rollback, correction, and supersession

While this candidate remains unassigned and proposed, rollback means abandoning or reverting its unmerged implementation change without altering other authority surfaces. If the candidate is later assigned and accepted:

- implementation rollback must use transparent commits and the applicable release rollback process;
- the deny-by-default boundary remains in force while a policy, UI, API, source, or release defect is investigated;
- stale, withdrawn, misattributed, or incorrectly summarized advisory context must be removed or marked through a correction/withdrawal path;
- public caches, exports, indexes, tiles, search results, and AI retrieval surfaces must be invalidated where they carried the affected context;
- a material weakening or replacement of this decision requires a successor ADR with forward and backward supersession links;
- history must not be rewritten and an accepted ADR must not be silently edited into the opposite decision.

## Open questions

- Which collision-free numeric ADR ID should be assigned after checking the current index, open PRs, and active ADR branches?
- Which AdvisoryContext contract and schema filenames are canonical, and what migration or compatibility treatment applies to the alternatives?
- Where should `not_emergency_alert_system` and the official-source reference bind: decision envelope, every advisory layer payload, or both?
- Which stable policy reason codes and public-safe explanations should be canonical?
- What canonical source role and knowledge-character enum represents operational advisory context?
- Which cross-cutting policy and validator home governs the shared Hazards, Hydrology, and Atmosphere life-safety boundary?
- How should Atmosphere advisory context and Hazards event/impact context join without duplicating or overwriting identity?
- Who are the decision owners, required reviewers, and separation-of-duties participants for acceptance?

## Evidence and references

- [ADR operating contract](./README.md)
- [Canonical ADR index](./INDEX.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [Atmosphere planned-files register](../domains/atmosphere/MISSING_OR_PLANNED_FILES.md)
- [Atmosphere Policy](../domains/atmosphere/POLICY.md)
- [Atmosphere Publication Posture](../domains/atmosphere/PUBLICATION_POSTURE.md)
- [Atmosphere API Contracts](../domains/atmosphere/API_CONTRACTS.md)
- [Atmosphere Map/UI Contracts](../domains/atmosphere/MAP_UI_CONTRACTS.md)
- [Atmosphere Knowledge Characters](../domains/atmosphere/KNOWLEDGE_CHARACTERS.md)
- [AdvisoryContext semantic contract](../../contracts/domains/atmosphere/AdvisoryContext.md)
- [Atmosphere advisory policy scaffold](../../policy/domains/atmosphere/advisory_no_life_safety.rego)
- [Atmosphere advisory test placeholder](../../tests/domains/atmosphere/test_advisory_no_life_safety.py)
- [Hazards Life-Safety Boundary](../domains/hazards/LIFE_SAFETY_BOUNDARY.md)
- [Explorer Web Atmosphere feature boundary](../../apps/explorer-web/src/features/domains/atmosphere/README.md)

## Change history

| Date | Change | Status |
| --- | --- | --- |
| 2026-07-24 | Replaced the 11-line planned-file scaffold with a same-path, evidence-grounded ADR candidate; preserved `ADR-XXXX` and `not-assigned` posture; added decision, options, consequences, implementation gates, validation, rollback, conflicts, and open questions. | PROPOSED |
