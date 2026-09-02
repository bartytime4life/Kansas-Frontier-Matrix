<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hazards-hazards-decision-envelope
title: Hazards Decision Envelope Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; CONFLICTED schema-home/path form; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Governed API steward
  - OWNER_TBD — Security steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hazards; decision-envelope; governed-api; not-for-life-safety; finite-outcomes; source-role-aware; freshness-aware; evidence-bound; release-gated; rollback-aware
tags: [kfm, contracts, hazards, HazardsDecisionEnvelope, hazards_decision_envelope, decision-envelope, feature-resolver, governed-api, ANSWER, ABSTAIN, DENY, ERROR, not-for-life-safety, official-source-referral, source-role, freshness, expiry, evidence-bundle, policy-decision, release-manifest, rollback]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_observation.md
  - ./domain_validation_report.md
  - ../../../docs/domains/hazards/API_CONTRACTS.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/IDENTITY_MODEL.md
  - ../../../docs/architecture/hazards-trust-membrane.md
  - ../../../schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hazards/
  - ../../../fixtures/domains/hazards/feature_resolver/
  - ../../../fixtures/domains/hazards/hazards_decision_envelope/
  - ../../../tests/domains/hazards/feature_resolver/
  - ../../../tests/domains/hazards/test_hazards_decision_envelope.*
  - ../../../data/registry/sources/hazards/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold at contracts/domains/hazards/hazards_decision_envelope.md."
  - "The paired schema exists at schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json, but remains a PROPOSED scaffold with empty properties and additionalProperties=true."
  - "CONFLICTED path form: mounted repo evidence uses contracts/domains/hazards/ and schemas/contracts/v1/domains/hazards/, while docs/domains/hazards/API_CONTRACTS.md proposes flat contracts/hazards/ and schemas/contracts/v1/hazards/ pending ADR-S-01 / ADR-0001. This file follows the mounted target path and paired schema pointer."
  - "HazardsDecisionEnvelope is the feature/detail resolver envelope for governed Hazards responses. It is not a layer manifest, not an EvidenceBundle, not a ReleaseManifest, not a warning, not official-source authority, not AI proof, and not life-safety guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Decision Envelope Contract

> Semantic contract for `HazardsDecisionEnvelope`: the bounded runtime envelope returned by the Hazards feature/detail resolver when KFM answers, abstains, denies, or errors on a Hazards feature/detail request without becoming an emergency-alert authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hazards" src="https://img.shields.io/badge/domain-Hazards%20%5BDOM--HAZ%5D-orange">
  <img alt="Object: HazardsDecisionEnvelope" src="https://img.shields.io/badge/object-HazardsDecisionEnvelope-blue">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
  <img alt="Boundary: not life safety" src="https://img.shields.io/badge/boundary-not__for__life__safety-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
</p>

`contracts/domains/hazards/hazards_decision_envelope.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Path conflict](#path-conflict) · [Envelope boundaries](#envelope-boundaries) · [Outcome grammar](#outcome-grammar) · [Minimum payload obligations](#minimum-payload-obligations) · [Hazards DENY register](#hazards-deny-register) · [Source-role rules](#source-role-rules) · [Temporal and freshness rules](#temporal-and-freshness-rules) · [Illustrative shape](#illustrative-shape) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/hazards/hazards_decision_envelope.md`  
> **Schema path:** `schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json`  
> **Schema posture:** paired schema exists, but remains a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Hazards API doctrine confirms the feature/detail resolver surface, finite outcome grammar, and not-for-life-safety boundary. Concrete route names, DTO field-level enforcement, validators, policy runtime, fixtures, release artifacts, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `HazardsDecisionEnvelope` is not a warning, not an advisory, not a life-safety instruction, not official-source authority, not a layer manifest, not an EvidenceBundle, and not a release decision. It is the bounded response wrapper that tells a public or internal governed surface what KFM may safely say, not say, deny, or report as an error.

---

## Meaning

`HazardsDecisionEnvelope` is the Hazards feature/detail response envelope. It wraps a Hazards feature request result with outcome, source-role posture, evidence status, policy state, release state, temporal/freshness posture, official-source referral, and not-for-life-safety boundary.

It answers:

- Can KFM answer this Hazards feature/detail request from released, evidence-backed, policy-allowed material?
- Which finite outcome applies: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`?
- Which object family is involved: `HazardEvent`, `HazardObservation`, `WarningContext`, `AdvisoryContext`, `FloodContext`, `WildfireDetection`, `SmokeContext`, `DroughtIndicator`, `EarthquakeEvent`, `ExposureSummary`, or another governed Hazards family?
- Which source role applies: observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic?
- Are issue/expiry/freshness fields present where operational context is involved?
- Does the response carry the required `not_for_life_safety` and official-source referral obligations?
- Which EvidenceRefs, EvidenceBundles, PolicyDecisions, ReleaseManifests, CorrectionNotices, and RollbackCards support or constrain the response?

The envelope is a trust-membrane object. It is where KFM refuses to overclaim.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable envelope meaning | `contracts/domains/hazards/hazards_decision_envelope.md` | This file; semantic contract for the Hazards feature/detail envelope. |
| Machine schema | `schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json` | CONFIRMED scaffold; field-level shape still empty. |
| Hazards API doctrine | `docs/domains/hazards/API_CONTRACTS.md` | Defines governed surfaces, outcomes, feature/detail DTO expectations, DENY register, and invariants. |
| Contract root | `contracts/domains/hazards/README.md` | Directory root identifies this file as planned bounded runtime/envelope semantics. |
| Feature identity | `contracts/domains/hazards/domain_feature_identity.md` | Stable identity, role, time, and digest companion. |
| Domain observation | `contracts/domains/hazards/domain_observation.md` | Observation/source-role boundary; not this envelope. |
| Layer descriptor | `contracts/domains/hazards/domain_layer_descriptor.md` | Layer delivery descriptor; not a feature/detail answer. |
| Validation report | `contracts/domains/hazards/domain_validation_report.md` | Planned validation-report semantics; still scaffold unless expanded. |
| Policy | `policy/domains/hazards/` and possibly `policy/release/hazards/` | Expected deny/abstain/restrict/release gates. |
| Release | `release/` | ReleaseManifest, CorrectionNotice, RollbackCard, PromotionDecision. |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Hazards Decision Envelope` |
| Visible properties | Empty object |
| Required fields | None visible in scaffold |
| Additional properties | `true` |
| Contract pointer | `contracts/domains/hazards/hazards_decision_envelope.md` |
| Source doc pointer | `docs/domains/hazards/API_CONTRACTS.md` |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is expanded, this Markdown contract defines intended semantics, not machine-enforced validation.

---

## Path conflict

> [!WARNING]
> **CONFLICTED / NEEDS VERIFICATION:** current mounted repo evidence uses `contracts/domains/hazards/` and `schemas/contracts/v1/domains/hazards/`. The Hazards API contract proposes `contracts/hazards/hazards_decision_envelope.md` and `schemas/contracts/v1/hazards/hazards_decision_envelope.schema.json` pending ADR-S-01 / ADR-0001. This file follows the requested mounted path and paired schema pointer. It does not resolve the ADR.

Do not create a second flat-path envelope contract without an ADR, redirect, or migration note. Parallel envelope contracts would weaken the trust membrane.

---

## Envelope boundaries

| This envelope is | This envelope is not |
|---|---|
| A finite runtime response wrapper for Hazards feature/detail requests. | A source record, source feed, or direct source response. |
| A carrier of outcome, reason, evidence, policy, release, source-role, freshness, and not-for-life-safety state. | An EvidenceBundle, PolicyDecision, ReleaseManifest, or ReviewRecord. |
| A way to deny unsafe or unsupported requests while staying inspectable. | An emergency instruction or alert replacement. |
| A public-safe projection of released or release-eligible Hazards context. | A bypass around RAW/WORK/QUARANTINE/PROCESSED/CATALOG gates. |
| A gate against source-role collapse and stale operational context. | A mechanism for turning candidate/model/regulatory/aggregate/synthetic material into observed truth. |

---

## Outcome grammar

Hazards feature/detail requests use four runtime outcomes.

| Outcome | When it applies | Required posture | Public surface behavior |
|---|---|---|---|
| `ANSWER` | Evidence resolves, policy allows, release state is valid, source role is preserved, freshness is within tolerance, and life-safety boundary is preserved. | EvidenceRefs/EvidenceBundle refs, PolicyDecision, ReleaseManifest, source role, citations, not-for-life-safety as needed. | Return bounded feature/detail payload with caveats and Evidence Drawer hooks. |
| `ABSTAIN` | Evidence is insufficient, citation cannot be validated, source role is unresolved, temporal scope is insufficient, or stale operational context lacks a safe historical framing. | Reason code and no unsupported claim. AI/focus surfaces may include AIReceipt/citation-validation details. | Explain why KFM cannot answer; do not invent or infer. |
| `DENY` | Policy, rights, sensitivity, release state, role-collapse, expired-current warning, direct-source access, candidate public exposure, or life-safety replacement request blocks the response. | PolicyDecision or deny reason; official-source referral where applicable. | Refuse the unsafe/unsupported public path; may point to official sources or released alternatives. |
| `ERROR` | Malformed request, missing required envelope/schema fields, infrastructure failure, validator failure, evidence lookup failure, release lookup failure, or unhandled contract violation. | Error code and diagnostic safe for caller. | Return finite error envelope; do not fall through to another lane or answer generically. |

`HOLD` is not a read-time outcome for this envelope. It may apply to promotion, correction, review, or release workflows.

---

## Minimum payload obligations

A public-safe `HazardsDecisionEnvelope` should carry the following **PROPOSED** semantic fields before schema promotion:

| Field | Meaning |
|---|---|
| `envelope_id` | Stable response/envelope identifier. |
| `schema_version` | Envelope schema version. |
| `outcome` | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| `domain` | Must resolve to `hazards`. |
| `request_ref` | Safe request identifier or normalized request digest. |
| `feature_ref` | Canonical feature/layer/feature reference when applicable. |
| `object_family` | Hazards object family for the response. |
| `source_role` | Canonical seven-role source role. |
| `knowledge_character` | Hazards-specific label such as `historical_event_record`, `operational_warning`, `regulatory_context`, `modeled_context`, or `remote_sensing_detection`. |
| `temporal_scope` | Event/observed/source/issue/expiry/valid/retrieval/release/correction times where material. |
| `freshness_state` | current, historical, expired, stale, superseded, unknown, or accepted enum. |
| `not_for_life_safety` | Required boolean/obligation for operational or public Hazards context. |
| `official_source_referral` | Official source referral when operational/safety-adjacent context is involved. |
| `evidence_refs` | EvidenceRefs used or attempted. |
| `evidence_bundle_refs` | Resolved EvidenceBundles supporting claims. |
| `policy_decision_ref` | PolicyDecision governing outcome. |
| `release_ref` | ReleaseManifest / PromotionDecision ref when answering from published artifacts. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | RollbackCard/rollback target refs. |
| `reason_code` | Required for `ABSTAIN`, `DENY`, and `ERROR`; recommended for `ANSWER` caveats. |
| `citation_projection` | Public-safe citation/evidence summary. |
| `drawer_ref` | Evidence Drawer payload ref or reason drawer is denied/unavailable. |
| `quality_flags` | Missing evidence, stale, expired, role conflict, source-rights gap, candidate state, sensitive geometry, release missing. |

---

## Hazards DENY register

These conditions must return `DENY` for the feature/detail envelope, or `ABSTAIN` only where the request is clearly historical/explanatory and a safe bounded response can avoid the blocked claim.

| Condition | Required outcome | Reason |
|---|---|---|
| User asks KFM to replace emergency alerting or give life-safety instructions. | `DENY` | KFM is not an alert authority. |
| Operational `WarningContext` / `AdvisoryContext` is expired but requested as current. | `DENY` | Expired operational context must not appear current. |
| Regulatory zone is used as observed event evidence. | `DENY` | Regulatory ≠ observed. |
| Modeled product is labeled or queried as observed. | `DENY` or Focus `ABSTAIN` | Modeled ≠ observed; model/run/uncertainty required. |
| Aggregate record is cited as per-place truth. | `DENY` | Aggregate ≠ individual/place observation. |
| Candidate record is requested on a public surface. | `DENY` | Candidate remains WORK/QUARANTINE until governed transition. |
| Synthetic or AI text is presented as observed reality. | `DENY` | Generated material is interpretive, not root truth. |
| AI text is treated as evidence. | `DENY` / Focus `ABSTAIN` | EvidenceBundle outranks generated language. |
| Public client attempts direct read from RAW/WORK/QUARANTINE or source endpoint. | `DENY` | Trust-membrane invariant. |
| Exact sensitive operational/infrastructure detail lacks steward-approved exposure class. | `DENY` or `RESTRICT` via review path | Sensitive lanes fail closed. |

---

## Source-role rules

`HazardsDecisionEnvelope` must preserve source roles through response construction.

| Role | Envelope behavior |
|---|---|
| `observed` | May answer observed event/observation claims when evidence/release/policy resolve. |
| `regulatory` | May answer regulatory context; must deny observed-event framing. |
| `modeled` | May answer modeled context with model identity, receipt, uncertainty; must deny observed framing. |
| `aggregate` | May answer aggregate summary with unit/window; must deny per-place framing. |
| `administrative` | May answer administrative context; must deny observed-damage/event framing unless separately evidenced. |
| `candidate` | Must deny public feature/detail answer unless a separate governed transition promotes it. |
| `synthetic` | Must deny observed-reality framing and require representation/reality-boundary posture. |

> [!WARNING]
> Operational warning/advisory/watch material remains a role-mapping conflict until ADR-S-04 or schema/policy review resolves whether it is represented as observed issuance, administrative context, or another governed overlay. This contract requires issue/expiry/freshness and not-for-life-safety fields either way.

---

## Temporal and freshness rules

| Time/freshness element | Envelope rule |
|---|---|
| `event_time` / `observed_time` | Required for event/observation claims where source supports it. |
| `issue_time` | Required for operational warning/advisory/watch context. |
| `expiry_time` / `valid_through` | Required for operational warning/advisory/watch context. |
| `valid_time` | Required for modeled/regulatory/administrative context where source claims validity window. |
| `retrieval_time` | May explain fetch state, but never becomes event or source truth. |
| `release_time` | May explain publication state, but never becomes event/source truth. |
| `correction_time` | Indicates correction lineage; never silently rewrites prior claims. |
| `freshness_state` | Required when current-vs-historical interpretation matters. |

Expired operational context may be explained as historical context only when evidence and release support that framing. It cannot be answered as current operational guidance.

---

## Illustrative shape

> [!NOTE]
> This JSON is illustrative. The authoritative machine shape must live in `schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json` or an ADR-approved migrated schema path. Current schema is still empty.

```jsonc
{
  "object_type": "HazardsDecisionEnvelope",
  "schema_version": "v1",
  "envelope_id": "haz-env-EXAMPLE",
  "domain": "hazards",
  "outcome": "ANSWER",
  "reason_code": "evidence_release_policy_ok",
  "not_for_life_safety": true,
  "official_source_referral": {
    "required": true,
    "source_family": "NWS",
    "message": "Use official emergency sources for current life-safety decisions."
  },
  "feature": {
    "feature_id": "hazard-feature-id-example",
    "object_family": "HazardEvent",
    "source_role": "observed",
    "knowledge_character": "historical_event_record",
    "temporal_scope": {
      "event_time": "SOURCE_TIME_TBD",
      "retrieval_time": "KFM_RETRIEVAL_TIME_TBD",
      "release_time": "RELEASE_TIME_TBD"
    }
  },
  "evidence_refs": ["EVIDENCE_REF_TBD"],
  "evidence_bundle_refs": ["EVIDENCE_BUNDLE_TBD"],
  "policy_decision_ref": "POLICY_DECISION_TBD",
  "release_ref": "RELEASE_MANIFEST_TBD",
  "correction_refs": [],
  "rollback_refs": ["ROLLBACK_CARD_TBD"],
  "citation_projection": {
    "status": "NEEDS VERIFICATION",
    "citations": []
  },
  "quality_flags": []
}
```

---

## Lifecycle

| Phase | Envelope handling |
|---|---|
| RAW | No public envelope. Source payloads, refs, role, rights, times, geometry, and hashes enter source/lifecycle storage. |
| WORK / QUARANTINE | Candidate envelope reasoning may exist for validation, but public read returns `DENY`, `ABSTAIN`, or no surface. |
| PROCESSED | Validated objects and evidence refs may be prepared; still not public `ANSWER` until release. |
| CATALOG / TRIPLET | EvidenceBundle projections may support drawer/focus context; public feature answer still requires release and policy closure. |
| RELEASE CANDIDATE | Envelope fields are checked: evidence, policy, source role, release, correction, rollback, freshness, disclaimer, official referral. |
| PUBLISHED | Governed API may return `ANSWER` if all gates pass, otherwise `ABSTAIN`, `DENY`, or `ERROR`. |
| CORRECTED / SUPERSEDED | Envelope must surface correction/supersession and stop returning stale or superseded information as current. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json` beyond empty `properties`.
- [ ] Resolve the flat-vs-`domains/` path conflict or record an accepted compatibility/migration rule.
- [ ] Decide whether `not_for_life_safety` is a top-level field, a policy obligation, or both.
- [ ] Decide whether "operational" is a source-role enum value or a freshness/policy overlay.
- [ ] Define canonical `outcome`, `reason_code`, `freshness_state`, `knowledge_character`, `quality_flags`, and official-referral fields.
- [ ] Add positive fixtures for observed historical event answer, regulatory-context answer, modeled-context answer, historical expired-warning explanation, and released public-safe detection answer.
- [ ] Add negative fixtures for emergency-alert replacement, expired-warning-as-current, NFHL-as-observed-flood, modeled-as-observed, aggregate-as-per-place, candidate-as-public, synthetic-as-observed, AI-as-evidence, direct-source public read, missing release, and missing disclaimer.
- [ ] Add validator coverage for EvidenceBundle resolution, PolicyDecision, ReleaseManifest, source role, freshness/expiry, not-for-life-safety, official-source referral, correction refs, and rollback refs.
- [ ] Confirm public UI, Evidence Drawer, and Focus Mode render `DENY` and `ABSTAIN` as first-class outcomes rather than generic "no result" states.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence, role, temporal scope, freshness, policy, release, correction, rollback, disclaimer, and official-source referral resolve | `ANSWER` |
| Evidence/citation/temporal context is insufficient but not forbidden | `ABSTAIN` |
| Policy, rights, sensitivity, release state, source-role collapse, expired-current framing, candidate exposure, synthetic-as-observed, or life-safety replacement blocks answer | `DENY` |
| Request/schema/lookup/runtime failure prevents evaluation | `ERROR` |

---

## Rollback

Rollback is required when the envelope allows unsafe or unsupported Hazards claims through the trust membrane.

Rollback triggers include missing not-for-life-safety marker; missing official-source referral; life-safety instruction emitted; expired operational context answered as current; regulatory context returned as observed event; modeled product returned as observation; aggregate summary returned as per-place fact; candidate record returned as public `ANSWER`; synthetic/AI material treated as observed reality or evidence; public read bypasses governed API; unreleased object receives `ANSWER`; EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, or rollback target is missing; schema/path migration causes envelope/schema mismatch; or UI collapses `DENY`/`ABSTAIN` into generic success/failure.

Rollback artifacts should include affected envelope IDs, request refs, feature refs, source descriptors, source-role summaries, temporal/freshness fields, EvidenceRefs/EvidenceBundles, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, invalidated layer descriptors, invalidated Focus Mode outputs, public-cache/style invalidation instructions, and replacement envelope/schema refs.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hazards/hazards_decision_envelope.md` scaffold | CONFIRMED | Target existed as a planned scaffold sourced from API contracts. | Did not contain authoritative envelope semantics. |
| `schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json` | CONFIRMED | Schema pointer, current scaffold status, empty schema shape, and contract_doc path. | Does not enforce envelope fields. |
| `docs/domains/hazards/API_CONTRACTS.md` | CONFIRMED | Feature/detail resolver purpose, DTO expectations, finite outcomes, DENY register, source-role rules, trust-membrane invariants, and illustrative envelope. | Route names and field shapes remain PROPOSED / NEEDS VERIFICATION. |
| `contracts/domains/hazards/README.md` | CONFIRMED | Contract-root boundary, accepted envelope role, not-for-life-safety posture, source-role/evidence/release obligations. | Orientation doc; not schema enforcement. |
| `docs/domains/hazards/SOURCE_ROLE_MATRIX.md` | CONFIRMED | Seven source-role channels, DENY conditions, promotion-never-upgrades rule. | Some matrix cells remain proposed applications pending fixtures/schema enforcement. |
| `docs/domains/hazards/README.md` | CONFIRMED | Hazards owns object families and not-for-life-safety official-link viewing mode; excludes emergency alerting and adjacent canonical truth. | Some path/implementation claims remain verification-bound. |
| `contracts/domains/hazards/domain_feature_identity.md` | CONFIRMED | Identity, role, time, digest companion semantics. | Not runtime envelope enforcement. |
| `contracts/domains/hazards/domain_layer_descriptor.md` | CONFIRMED | Layer descriptor boundary: layer delivery is not source truth or alerting. | Not feature/detail response schema. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which path is canonical: `contracts/domains/hazards/hazards_decision_envelope.md` or flat `contracts/hazards/hazards_decision_envelope.md`? | CONFLICTED / NEEDS VERIFICATION | ADR-S-01 / ADR-0001 / migration note. |
| Which fields must be required in `hazards_decision_envelope.schema.json`? | NEEDS VERIFICATION | Schema PR with positive/negative fixtures. |
| Is `not_for_life_safety` top-level, nested under policy obligations, or duplicated in both places? | OPEN / NEEDS VERIFICATION | Schema + policy decision. |
| Is operational context a source-role enum value or freshness/policy overlay? | OPEN / NEEDS VERIFICATION | ADR-S-04 source-role review. |
| Which policy file enforces feature/detail `DENY` decisions? | NEEDS VERIFICATION | Policy root inspection and tests. |
| Which governed API route returns this envelope? | NEEDS VERIFICATION | `apps/governed-api/` route inspection and routing ADR. |
| How should public UI display `ABSTAIN` vs `DENY` without confusing users? | NEEDS VERIFICATION | UI/Evidence Drawer fixture review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hazards contract-root README.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hazards identity contract.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — Hazards layer descriptor contract.
- [`./domain_observation.md`](./domain_observation.md) — Hazards observation envelope contract.
- [`./domain_validation_report.md`](./domain_validation_report.md) — planned validation-report contract scaffold.
- [`../../../docs/domains/hazards/API_CONTRACTS.md`](../../../docs/domains/hazards/API_CONTRACTS.md) — governed API and finite outcome doctrine.
- [`../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md) — Hazards domain operating doctrine.
- [`../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`](../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md) — publication and not-for-life-safety boundary.
- [`../../../docs/architecture/hazards-trust-membrane.md`](../../../docs/architecture/hazards-trust-membrane.md) — hazards trust-membrane architecture note.
- [`../../../schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json`](../../../schemas/contracts/v1/domains/hazards/hazards_decision_envelope.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
