<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-freshness-readme
title: tools/validators/freshness README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-source-steward-plus-evidence-steward-plus-hazards-steward-plus-hydrology-steward-plus-release-steward-plus-policy-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; freshness-validator; stale-state; expiry; source-cadence; valid-time; release-gated; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed shared freshness validator lane for checking source cadence, source-head posture, observed/source/valid/retrieval/release/correction time posture, stale-state detection, warning/advisory expiry, model-run freshness, regulatory effective-date/version posture, supersession, correction, rollback, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, official-source redirects, finite negative outcomes, and public-surface denial checks while deferring domain meaning, source registry authority, evidence records, policy decisions, receipts, proof records, release authority, and public outputs to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../citation/README.md
  - ../evidence/README.md
  - ../evidence_bundle/README.md
  - ../connector_gate/README.md
  - ../domains/hazards/README.md
  - ../domains/hydrology/README.md
  - ../domains/atmosphere/README.md
  - ../flood-context/README.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../data/registry/sources/README.md
  - ../../../data/registry/sources/hazards/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Hazards validator evidence says warning, advisory, watch, and operational-context products may be represented only as evidence-bound context with visible source role, validity, expiry, disclaimer, official-source redirect, release state, correction path, and rollback support."
  - "SourceDescriptor evidence says source admission records include how current or stale the source is expected to be and source-head/content identity evidence, but they do not make claims true, approve release, pass policy, or let connectors/watchers/pipelines bypass review."
  - "Freshness validation is a gate and context check, not truth, not policy approval, not release approval, not an emergency/life-safety warning, and not a public answer by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/freshness

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-freshness--validator-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![boundary](https://img.shields.io/badge/boundary-not--truth--or--release-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/freshness/` is the proposed shared validator lane for checking whether source, evidence, observation, model, warning/advisory, regulatory, release, correction, and rollback time posture is current enough and bounded enough for the requested governed use.

---

## Purpose

`tools/validators/freshness/` exists for time-validity and stale-state checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Is this candidate fresh enough, versioned enough, effective-date-bounded enough, correction-aware enough, expiry-aware enough, and release-linked enough for the requested catalog, proof, release, map, API, graph, Focus Mode, export, or AI surface — or must KFM return `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` instead of presenting it as current?

The answer should be a deterministic validation result. This folder should not create truth, decide policy, approve release, issue warnings, store evidence, store receipts, run connectors, publish public outputs, or make stale data current by summarizing it.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/freshness/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Hazards freshness/expiry posture | **CONFIRMED README / executable NEEDS VERIFICATION** | The Hazards validator index names freshness/expiry, operational-context freshness, official-source attribution, not-for-life-safety disclaimers, release state, correction path, and rollback support. |
| SourceDescriptor staleness posture | **CONFIRMED in repo evidence / draft** | `SourceDescriptor` records how current or stale a source is expected to be, access/citation/source-head posture, public-release posture, and review/release/lifecycle state. |
| Broad freshness executable, schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Freshness validator lane | `tools/validators/freshness/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Source preflight and source-head checks | `tools/validators/connector_gate/` and source validator lanes |
| Citation and evidence closure | `tools/validators/citation/`, `tools/validators/evidence/`, `tools/validators/evidence_bundle/` |
| Hazards freshness/expiry context | `tools/validators/domains/hazards/` |
| Hydrology time/freshness context | `tools/validators/domains/hydrology/` |
| Atmosphere observation/model cadence context | `tools/validators/domains/atmosphere/` |
| Flood regulatory effective-date/version context | `tools/validators/flood-context/` |
| SourceDescriptor semantics | `contracts/source/source_descriptor.md` |
| Evidence semantics | `contracts/evidence/` |
| Source registry and cadence posture | `data/registry/sources/` |
| Proofs, receipts, release, correction, rollback | `data/proofs/`, `data/receipts/`, `release/` |
| Policy/admissibility | `policy/` |

This README does not move, replace, or override those roots. It only defines where shared freshness validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Source cadence | Does the source declare expected update cadence, access posture, and stale-state tolerance? | Proof that a claim is current. |
| Source-head posture | Are ETag, checksum, digest, modified time, retrieval time, or equivalent source-head signals present where configured? | EvidenceBundle closure. |
| Observed time | Is the observation/event/sample/measurement time present and scoped? | Release time or current truth. |
| Source time | Is the upstream source publication/update/effective time present? | Observation time by default. |
| Valid time | Does the record declare the interval during which it is valid, active, effective, or applicable? | Open-ended currency. |
| Retrieval time | Is the fetch/intake/access time recorded where relevant? | Source publication time or truth. |
| Release time | Is public-bound output tied to release state and release time? | Policy approval by itself. |
| Correction time | Are corrections, supersessions, withdrawals, and rollback targets visible? | A reason to hide stale/corrected lineage. |
| Expiry | Do warnings, advisories, watches, operational context, forecasts, model outputs, and temporary notices expire or stale out? | Life-safety authority. |
| Regulatory effective date | Do regulatory layers preserve effective date, version, and stale-state caveats? | Current observed condition. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Freshness validator lane | `tools/validators/freshness/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Domain freshness validators | `tools/validators/domains/<domain>/` |
| SourceDescriptor contract | `contracts/source/source_descriptor.md` |
| EvidenceRef/EvidenceBundle contracts | `contracts/evidence/` |
| Source registry records | `data/registry/sources/` |
| Domain meaning and contracts | `docs/domains/`, `contracts/domains/` |
| Source, evidence, and domain schemas | `schemas/contracts/v1/` |
| Policy/admissibility | `policy/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/freshness/`, `tests/domains/`, `fixtures/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared freshness, cadence, time-scope, expiry, stale-state, correction, rollback, evidence, policy, and release-reference rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, time-field schema, accepted stale thresholds, source cadence vocabulary, fixtures, report destinations, receipt emission, policy integration, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as domain doctrine, source registry, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, emergency alert authority, legal/regulatory authority, current-condition authority, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/freshness/` include checks that:

- verify candidates declare required observation, source, valid, retrieval, release, and correction time posture where applicable;
- verify source cadence and source-head posture are visible before connector/intake, catalog, proof, or release use;
- verify public-bound claims do not cite stale, superseded, withdrawn, embargoed, expired, unversioned, or correction-missing evidence;
- verify warnings, watches, advisories, forecasts, model runs, operational-context records, and temporary hazard products expire or hold when their validity window ends;
- verify regulatory context such as NFHL preserves effective dates, version IDs, source times, and caveats before public display;
- verify stale candidates return finite negative outcomes instead of being presented as current;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/freshness/` | Correct home |
|---|---|
| Domain time doctrine and object meaning | `docs/domains/`, `contracts/domains/` |
| SourceDescriptor records or source registry records | `data/registry/sources/` |
| SourceDescriptor meaning/contracts | `contracts/source/` |
| EvidenceRef/EvidenceBundle meaning | `contracts/evidence/` |
| Schemas and controlled time-field enums | `schemas/contracts/v1/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, correction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| Connectors, source refreshers, model runners, or ETL | `connectors/`, `pipelines/`, `packages/`, or accepted implementation roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Freshness validator posture

Freshness validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks required observation time, source time, valid time, retrieval time, release time, correction time, effective date, expiry, source-head, cadence, or version posture for the requested use;
- treats retrieval time as observation time, source publication time as current condition, release time as policy approval, or old evidence as current truth;
- treats regulatory effective date as real-time observed condition;
- treats model run time, forecast valid time, or warning/advisory expiry as open-ended validity;
- uses stale, superseded, withdrawn, embargoed, expired, or correction-missing evidence for public-bound claims;
- lacks official-source redirect, not-for-life-safety posture, or expiry visibility for current-sensitive hazard/operational context;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on stale-state-collapsed records;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, or incomplete proof closure;
- treats freshness validation as EvidenceBundle creation, PolicyDecision creation, release approval, publication, official-source status, emergency instruction, current-condition authority, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `FRESHNESS_PASS` | Configured freshness checks passed. |
| `FRESHNESS_FAIL` | One or more configured freshness checks failed. |
| `OBSERVED_TIME_MISSING` | Required observed/sample/event/measurement time is absent. |
| `SOURCE_TIME_MISSING` | Required upstream source publication/update/effective time is absent. |
| `VALID_TIME_MISSING` | Required validity interval is absent or unbounded. |
| `RETRIEVAL_TIME_MISSING` | Required retrieval/intake time is absent. |
| `RELEASE_TIME_MISSING` | Required release-time reference is absent for the requested use. |
| `CORRECTION_TIME_MISSING` | Required correction/supersession/withdrawal time posture is absent. |
| `EXPIRY_MISSING` | Required expiry for warning/advisory/forecast/model/temporary context is absent. |
| `SOURCE_HEAD_MISSING` | Required source-head signal, ETag, checksum, digest, timestamp, or version is absent. |
| `SOURCE_CADENCE_GAP` | Source cadence or stale-state tolerance is missing or incompatible. |
| `STALE_EVIDENCE_DENIED` | Candidate relies on stale, superseded, withdrawn, embargoed, expired, or correction-missing evidence. |
| `TIME_KIND_COLLAPSE` | Candidate collapses observed/source/valid/retrieval/release/correction time semantics. |
| `CURRENT_CONDITION_OVERCLAIM` | Candidate presents historical, regulatory, modeled, or stale context as current condition. |
| `OFFICIAL_SOURCE_REDIRECT_MISSING` | Public-bound current-sensitive surface lacks official-source redirect where required. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, source refresh, correction, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/freshness/
├── README.md
├── test_freshness_validator.py
└── fixtures/
    ├── valid_fresh_public_context/
    ├── missing_observed_time/
    ├── missing_valid_time/
    ├── expired_warning_context/
    ├── stale_source_descriptor/
    ├── missing_source_head/
    ├── regulatory_as_current_condition_denied/
    ├── time_kind_collapse/
    ├── stale_evidence_denied/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/freshness
```

```bash
python tools/validators/freshness/validate_freshness.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_freshness.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared source descriptors, contracts, schemas, evidence records, policy, release, correction, and rollback records rather than defining meaning locally.
- [ ] Observation time, source time, valid time, retrieval time, release time, and correction time are not collapsed.
- [ ] Source cadence, source-head, version, and stale-state posture remain visible.
- [ ] Current-sensitive hazards, advisories, forecasts, model outputs, and operational context expire or hold safely.
- [ ] Regulatory and historical context is not presented as current observed condition.
- [ ] Public-bound outputs include official-source redirect and not-for-life-safety posture where required.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, stale evidence, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, current-condition authority, emergency authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Freshness validator file. |
| Next smallest safe change | Verify actual freshness validator script path, accepted time-field schemas, source cadence vocabulary, stale thresholds, fixtures, report destination, receipt emission, policy enforcement, release linkage, official-source redirect behavior, and CI/runtime wiring before promoting this lane beyond draft. |
