<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-state-em-watch-readme
title: tools/ingest/state_em_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-source-steward-plus-state-context-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context-only; watcher-only; not-for-life-safety; no-alert-authority
owning_root: tools/
responsibility: proposed state emergency-context watcher helper boundary for administrative-context source-change and freshness review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../connectors/state-emergency-context/README.md
  - ../../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../../tools/ingest/fema_decl_watch/README.md
  - ../../../tools/ingest/nws_context_watch/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README defines a proposed state emergency-context watcher tooling boundary, not a confirmed implementation."
  - "State emergency-management records are generally administrative/context records. They must not be collapsed into observed hazard events, current warning authority, legal determinations, or life-safety instructions."
  - "The watcher may detect declaration, proclamation, situation/status, source-head, freshness, geography, or source-descriptor changes and emit review signals; it must not publish, promote, rebroadcast, issue alerts, provide protective-action guidance, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/state_em_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-state--em--watcher-informational)
![domain](https://img.shields.io/badge/domain-hazards-7E2F2F)
![authority](https://img.shields.io/badge/KFM-not--alert--authority-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/state_em_watch/` is the proposed tooling lane for detecting review-worthy changes in state emergency-management context records and emitting governed watcher reports. It is not a connector, not a state emergency-management authority, not a public alerting surface, not a current-warning display engine, not legal or regulatory interpretation, not a publication path, and not hazard truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [State emergency-context watcher posture](#state-emergency-context-watcher-posture)
- [Material-change model](#material-change-model)
- [Source-role discipline](#source-role-discipline)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/state_em_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** state emergency-context source-change detector.

The watcher may compare approved local metadata, source sidecars, declaration/proclamation identifiers, situation/status summaries, source-head records, issue/effective/expiration dates, geography summaries, official-source links, source descriptor references, digests, or no-network fixtures to decide whether state emergency-context material should be reviewed.

The durable KFM question for this lane is:

> Did a state emergency-context source surface, administrative record, freshness state, or geography summary change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, alert rebroadcast, protective-action instruction, current-warning authority, observed hazard-event claim, legal/regulatory determination, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/state_em_watch/README.md` | **CONFIRMED** | This README defines the state emergency-context watcher tooling boundary. |
| State emergency-context watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| State emergency-context connector lane | **CONFIRMED in repo evidence / draft placement** | Connector output may enter raw/quarantine only; placement and activation need review. |
| Hazards source-role matrix | **CONFIRMED in repo evidence** | Kansas/local emergency management is mapped as administrative context for Hazards. |
| Hazards life-safety boundary | **CONFIRMED in repo evidence** | KFM is not an emergency alert system and must not provide life-safety instructions. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Cadence must be source-specific and steward-approved. |
| Freshness and expiry thresholds | **PROPOSED / NEEDS VERIFICATION** | Must be fixture-tested before workflow use. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |
| Alert authority or rebroadcast | **DENY here** | KFM must not issue or relay emergency-management products as KFM alerts. |
| Protective-action guidance | **DENY here** | This lane cannot produce instructions for current hazards. |
| Observed hazard-event truth | **DENY here** | Administrative context is not observed-event evidence by itself. |

> [!IMPORTANT]
> This folder is for watcher reports only. A state emergency-management source change does not mean KFM has a public current-warning state or an observed hazard event. It means stewards may need to review source descriptors, connector outputs, source role, rights, freshness, geography, policy decisions, receipts, catalog records, release state, or rollback paths.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/state-emergency-context/` owns draft source-admission helpers if that connector is accepted. `docs/domains/hazards/` owns hazards source-role, boundary, publication, and anti-collapse doctrine. `data/registry/sources/` owns source activation and descriptor truth. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility. Lifecycle data, receipts, proofs, catalog records, and release decisions live outside this tooling lane.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/state_em_watch/README.md`.
- **PROPOSED:** state emergency-context watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish or alert.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether the draft connector home `connectors/state-emergency-context/` is ratified or should move under another source-family connector root.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, current warning layer, official emergency-management authority, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A state emergency-context watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer or record.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not official emergency-management authority.** State agencies remain the issuing authority for their own records.
4. **Watcher output is not a live alert state.** Current warnings, notices, and emergency communications require official-source handling outside this lane.
5. **Watcher output is not protective-action guidance.** Current hazard action belongs to official channels, not KFM generated surfaces.
6. **Administrative context remains administrative.** Declarations, proclamations, situation reports, closures, status summaries, and resource summaries are not observed hazard events by themselves.
7. **Freshness is load-bearing.** Expired, superseded, or undated context must not appear as current context.
8. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/state_em_watch/` include:

- state emergency-context source metadata watcher helpers;
- sidecar comparison helpers;
- declaration/proclamation identifier drift checks;
- situation/status summary digest checks;
- issue/effective/expiration date checks;
- freshness-state and stale-context checks;
- county, jurisdiction, tribal, state, or incident-scope summary drift checks;
- official-source-link presence checks;
- source descriptor reference checks;
- source-head `etag`, `last_modified`, `content_length`, digest, and snapshot-date checks;
- rights, attribution, and source-use posture drift checks;
- source-role anti-collapse checks;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or alert, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/state_em_watch/` | Correct home | Reason |
|---|---|---|
| State emergency-context source fetchers or clients of record | `connectors/state-emergency-context/` or ratified connector home | Connectors own source acquisition and admission. |
| Hazards domain doctrine | `docs/domains/hazards/` | Human-facing doctrine is not watcher code. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw state emergency-context captures | `data/raw/...` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/...` | Holds are lifecycle artifacts, not watcher code. |
| Processed Hazards records | `data/processed/...` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Official emergency-management guidance | official state/local channels | KFM is not the issuing authority. |
| Legal, regulatory, eligibility, or safety determinations | governed official channels or separately reviewed docs | This watcher cannot decide determinations. |
| Policy rules | `policy/` | Watchers do not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/state_em_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## State emergency-context watcher posture

The state emergency-context watcher should be understood as a **review signaler** for administrative/context source change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- a staleness or supersession report;
- a declaration/proclamation drift report;
- a situation/status context drift report;
- a geography or jurisdiction summary drift report;
- a rights or attribution drift report;
- a source-role ambiguity report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed Hazards object of record;
- a public current-warning layer;
- a KFM-issued alert;
- a protective-action instruction;
- an observed hazard event;
- a legal or regulatory determination;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what source-role boundary is relevant, what freshness or official-source evidence was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved, current, actionable, determinative, or public.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, endpoint path, file inventory, or source version metadata. | **PROPOSED** |
| Expected cadence / staleness | Surface stale, missing, superseded, or delayed expected source windows. | **PROPOSED** |
| SourceDescriptor drift | Detect changed source role, rights, activation, cadence, steward, or canonical connector reference. | **PROPOSED** |
| Declaration/proclamation drift | Detect new, amended, rescinded, expired, or changed administrative records. | **PROPOSED** |
| Situation/status drift | Detect changed situation reports, status summaries, resource summaries, closure notices, or response-context summaries. | **PROPOSED** |
| Geography/jurisdiction drift | Detect changed county, tribal, state, incident, or jurisdiction coverage without inferring hazard extent. | **PROPOSED** |
| Official-source-link drift | Detect missing or changed official source link and attribution posture. | **PROPOSED** |
| Rights/attribution drift | Detect changed terms, attribution, or source-use posture. | **PROPOSED** |
| Freshness-state drift | Detect expired-as-current, superseded-as-current, or missing date fields. | **PROPOSED** |
| Source-role ambiguity | Fail closed when administrative context, warning context, observed event, or modeled/aggregate summaries cannot be separated. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | Source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_CONTEXT_CANDIDATE` | A new state emergency-context record appears available for steward review. |
| `AMENDED_CONTEXT_CANDIDATE` | An existing context record appears changed. |
| `RESCINDED_OR_EXPIRED_CONTEXT` | A record appears expired, rescinded, or ended and needs freshness review. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `GEOGRAPHY_OR_JURISDICTION_DRIFT` | Administrative geography or jurisdiction scope changed. |
| `RIGHTS_OR_ATTRIBUTION_DRIFT` | Rights, source-use, or attribution posture changed. |
| `EXPIRED_AS_CURRENT` | Expired or superseded context is being treated as current; fail closed. |
| `SOURCE_ROLE_AMBIGUOUS` | The watcher cannot preserve source-role separation safely; fail closed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Source-role discipline

State emergency-management material must remain source-role-separated even when source pages mix administrative records, status summaries, public notices, links to NWS/FEMA products, and local context.

| Surface | KFM posture | Watcher guardrail |
|---|---|---|
| Emergency declaration / proclamation | `administrative` context unless a SourceDescriptor assigns another role | Preserve issuing agency, identifier, date, scope, official link, source role, and digest. |
| Situation/status report | `administrative` or `aggregate` context depending on source fields | Preserve report date, time window, geography, caveats, and official-source link. |
| Closure / resource / response-context summary | `administrative` context | Do not infer hazard extent or safety state from administrative coverage. |
| Embedded NWS warning/advisory link | NWS context, not state-originated KFM alert | Preserve source distinction and official source link. |
| FEMA declaration cross-reference | FEMA administrative context | Do not duplicate FEMA declaration truth; reference the FEMA lane. |
| Unknown or mixed component | `candidate` / quarantine | Do not publish; require source-role, freshness, rights, and sensitivity review. |

The watcher may report context drift, but it must not collapse components into observed hazard events or convert any component into KFM-issued authority.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- State emergency-context SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Declaration/proclamation metadata fixtures.
- Situation/status summary fixtures.
- Jurisdiction/geography summary fixtures.
- Official-source-link fixtures.
- Rights and attribution fixtures.
- Freshness and expiry state fixtures.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- current public-facing alert layers treated as KFM authority;
- instructions for action during current hazards;
- official state text modified into KFM-issued guidance;
- legal, eligibility, regulatory, or safety determinations treated as KFM decisions;
- source material with missing date/freshness/source-role fields promoted toward publication;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- declaration/proclamation drift report;
- freshness/expiry drift report;
- geography/jurisdiction drift report;
- rights/attribution drift report;
- source-role ambiguity report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice state emergency-context watcher report should be compact and deterministic.

```json
{
  "tool": "state-em-watch",
  "status": "NEW_CONTEXT_CANDIDATE",
  "source_id": "state_emergency_context_placeholder",
  "domain": "hazards",
  "source_role": "administrative",
  "inputs": {
    "prior_sidecar": "tests/ingest/state_em_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/state_em_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "context_record_type": "declaration_or_proclamation",
    "freshness_state": "needs_review",
    "official_source_link": "present",
    "geography_or_jurisdiction_drift": "changed",
    "source_role": "administrative"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["NEW_CONTEXT_CANDIDATE", "GEOGRAPHY_OR_JURISDICTION_DRIFT"],
    "blocking": false,
    "publication": false,
    "kfm_alert_authority": false,
    "protective_action_guidance": false,
    "observed_hazard_event": false
  },
  "next_review": [
    "confirm state emergency-context source descriptor and rights posture",
    "preserve administrative source role",
    "confirm connector placement and admission workflow",
    "route through source-role and freshness validation before catalog work",
    "do not publish current context without policy, review, release, and rollback controls"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/state_em_watch/
├── README.md
├── test_state_em_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── new_context_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── amended_context_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── expired_as_current/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── geography_or_jurisdiction_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── source_role_ambiguous/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- new context records return `NEW_CONTEXT_CANDIDATE` or `PROPOSED_WORK_RECORD` according to configured rules;
- amended declaration/proclamation/status fields return `AMENDED_CONTEXT_CANDIDATE`;
- expired or superseded context treated as current returns `EXPIRED_AS_CURRENT` and fails closed;
- changed administrative geography returns `GEOGRAPHY_OR_JURISDICTION_DRIFT` without hazard-extent inference;
- missing official-source links, dates, or source descriptor references return `ABSTAIN` or `ERROR`;
- mixed administrative/warning/observed/model components return `SOURCE_ROLE_AMBIGUOUS` and fail closed;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/state_em_watch
```

```bash
python tools/ingest/state_em_watch/state_em_watch.py \
  --prior tests/ingest/state_em_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/state_em_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/state-em-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `state_em_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing state emergency-context watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] The helper cannot issue, relay, or reframe emergency-management products as KFM-issued alerts.
- [ ] The helper cannot provide protective-action guidance.
- [ ] The helper cannot convert administrative context into observed hazard events.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Declarations, proclamations, situation reports, NWS links, FEMA cross-references, and observed-source material remain distinct.
- [ ] Issue/effective/expiration dates, retrieval time, official-source link, source URL, source role, and digest are preserved where applicable.
- [ ] Expired or superseded context cannot appear as current context.
- [ ] Watcher cadence and thresholds are source-specific and reviewable.
- [ ] Network access is off by default or explicitly read-only and documented.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests use public-safe fixtures only.
- [ ] The helper does not write directly to `data/catalog/`, `data/triplets/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with governed state emergency-context watcher contract | **DONE in this README** | Establishes watcher boundaries, administrative-context posture, and no-alert-authority rule. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve state emergency-context connector canonicality | **NEEDS VERIFICATION / ADR-class** | Prevents duplicate or unratified connector authority. |
| Add `state_em_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, new-context, amended-context, expired-as-current, geography drift, and source-role ambiguity behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hazards/state-context contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces state emergency-context source-change and freshness issues without publication or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/state_em_watch/state_em_watch.py` with public-safe fixtures under `tests/ingest/state_em_watch/`. |
