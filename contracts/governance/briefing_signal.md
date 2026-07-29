<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-governance-briefing-signal
title: BriefingSignal Governance Contract
type: semantic-contract
version: v0.1.0
status: proposed; discovery-only; non-authoritative
owners: OWNER_TBD — Governance steward · Intake steward · Domain steward · Source steward · Evidence steward · Docs steward
created: 2026-07-29
updated: 2026-07-29
policy_label: public; governance; briefing-intake; cite-or-abstain; no-public-authority
related:
  - ./README.md
  - ../../docs/architecture/briefing-integration.md
  - ../../docs/intake/README.md
  - ../../schemas/contracts/v1/governance/briefing_signal.schema.json
  - ../../tools/validators/governance/validate_briefing_signal.py
  - ../../tests/governance/test_briefing_signal.py
tags: [kfm, governance, briefing-signal, intake, materiality, evidence, routing, non-authoritative]
notes:
  - "BriefingSignal records why a development may deserve verification or modeling; it is never evidence or publication authority."
  - "Generated briefing prose cannot populate confirmed claims without explicit evidence references."
  - "The first implementation is deterministic and no-network and keeps every consequential permission false."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BriefingSignal

> A `BriefingSignal` is a non-authoritative discovery and routing record created from a daily briefing story. It preserves materiality, candidate sources, uncertainty, proposed KFM relationships, and the smallest next action without turning narrative prose into evidence or authority.

## Purpose

The daily briefing can discover material developments faster than KFM can admit sources, model objects, validate claims, or release public products. `BriefingSignal` creates a governed boundary between those activities.

It answers:

- what development was noticed;
- why it may matter to KFM;
- which domains and geographic scopes may be affected;
- which factual claims are confirmed, conflicted, or unresolved;
- which official sources should be snapshotted or verified;
- whether equivalent work already exists;
- which object families may be relevant; and
- what bounded follow-up is appropriate.

It does not answer whether a source is admitted, a claim is true, policy permits use, a meeting occurred, a plan was approved, a project was funded, or an artifact may be published.

## Authority boundary

A `BriefingSignal` is **discovery metadata only**.

It is not:

- an `EvidenceRef` or `EvidenceBundle`;
- a `SourceDescriptor` or source-activation decision;
- a `GovernanceEvent`, advisory, observation, award, project, or completion record;
- a `ReviewRecord`, `PolicyDecision`, or `PromotionDecision`;
- a repository-control authorization;
- a release manifest, correction notice, withdrawal notice, or rollback card;
- a public map, API, search, graph, Focus Mode, or AI-answer object.

A valid signal always carries:

```text
public_use_allowed = false
source_activation = false
proof_construction = false
release = false
deployment = false
publication = false
repository_mutation_allowed = false
```

Those fields are guards, not a permission mechanism. Changing them is invalid rather than an escalation path.

## Anti-collapse rules

| Never collapse | Required distinction |
|---|---|
| Briefing story → evidence | Generated prose identifies a verification target; official snapshots and evidence records support claims. |
| Announced meeting → held meeting | Schedule facts may be confirmed while occurrence, attendance, submissions, recommendations, and decisions remain unresolved. |
| Link presence → submission or approval | An official index may expose a document link without proving acceptance, review, approval, implementation, or effectiveness. |
| Venue → regional scope | A venue point and a planning region are separate geographies. |
| Missing link → non-existence | Missing or inaccessible links become `UNKNOWN` or `NEEDS_VERIFICATION`. |
| Correlation → causation | Contextual relations retain source roles and uncertainty. |
| Issue or PR → implementation authority | Repository work requires a separate exact claim and current control-state evaluation. |
| Schema pass → public use | Shape validation never supplies evidence, policy, review, release, or publication authority. |

## Signal lifecycle

```text
DISCOVERED
  ├─> DUPLICATE
  ├─> NEEDS_VERIFICATION
  ├─> CONFLICTED
  ├─> ACCEPTED_FOR_MODELING
  │     └─> IMPLEMENTATION_TRACKED
  ├─> REJECTED
  └─> CLOSED
```

Signal state is independent from:

1. the real-world object state, such as `scheduled`, `rescinded`, `awarded`, or `completed`; and
2. the KFM data lifecycle, such as `RAW`, `QUARANTINE`, `CATALOG`, or `PUBLISHED`.

## Semantic shape

| Field | Meaning |
|---|---|
| `signal_id` | Stable daily signal identity. |
| `briefing_date` | Date of the briefing that produced the signal. |
| `status` | Discovery workflow state. |
| `headline` | Short human-readable summary, not evidence. |
| `story_type` | Reusable routing category. |
| `domains[]` | Candidate KFM domains. |
| `materiality` | Priority and bounded rationale. |
| `geographic_scope` | Named scope plus geometry reference state; no inline guessed geometry. |
| `claims[]` | Claim text, truth label, and evidence references. |
| `official_source_candidates[]` | Candidate authorities and locators to snapshot or verify. |
| `existing_kfm_links` | Issues, repository paths, or object references already addressing the signal. |
| `proposed_object_families[]` | Candidate semantic homes, not accepted object creation. |
| `next_action` | Deterministic issue disposition and bounded scope. |
| `permissions` | Consequential operations fixed to false. |
| `candidate_payload` | Optional production-shaped sketch with explicit non-authority boundary. |
| `expires_at` | Time when the signal should be refreshed, closed, or reverified. |

## Claim rules

- `CONFIRMED` requires at least one evidence reference.
- `NEEDS_VERIFICATION`, `UNKNOWN`, and `CONFLICTED` may have no evidence reference when the absence itself is explicit.
- Official-source locators are candidates until immutable snapshots and evidence records are created.
- Memory, generated text, likely behavior, missing search results, or path names are not evidence.
- Corrections preserve the prior claim and link the superseding evidence.

## Geographic rules

- Use named identifiers before geometry is admitted.
- `geometry_ref` points to a governed geometry object; it does not contain coordinates.
- Venue, municipal, district, watershed, service-area, warning-zone, and project geometries remain distinct.
- Unknown geometry fails closed and does not block human-facing intake documentation.
- A briefing signal cannot create a parcel, field, facility, sensitive-site, or protected-location inference.

## Deterministic issue routing

A signal resolves to exactly one disposition:

- `UPDATE_EXISTING_ISSUE`
- `OPEN_SOURCE_DISCOVERY_ISSUE`
- `OPEN_OBJECT_MODEL_ISSUE`
- `NO_ACTION`

Issue routing is a recommendation. The signal cannot create or modify repository content by itself.

## Validation

The first validator proves only that:

- the schema is closed and parseable;
- confirmed claims carry evidence references;
- public and consequential permissions remain false;
- inline geometry and coordinate aliases are rejected from candidate payloads;
- trust-bearing true states are rejected;
- official-source candidates and materiality are explicit; and
- CLI output is deterministic and no-network.

A passing result does not prove the source, claim, event, plan, geometry, rights, policy, review, release, or public product.

## Correction and rollback

Before merge, close the draft PR and abandon its branch. After merge, use a reviewed corrective or revert PR. Preserve signal identifiers and prior claims when evidence changes; do not erase the record that a claim was once unresolved or conflicted.

[Back to top](#top)
