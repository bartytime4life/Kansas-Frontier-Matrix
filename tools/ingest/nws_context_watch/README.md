<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-nws-context-watch-readme
title: tools/ingest/nws_context_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-atmosphere-source-stewards
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context-only; watcher-only; not-for-life-safety; no-alert-authority
owning_root: tools/
responsibility: proposed NOAA NWS context watcher helper boundary for source-change, freshness, and component-role review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/sources/catalog/noaa/nws-api.md
  - ../../../connectors/nws-api/README.md
  - ../../../connectors/nws/README.md
  - ../../../connectors/noaa/README.md
  - ../../../tools/ingest/hydrology_watch/README.md
  - ../../../tools/ingest/firms_hms_watch/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README defines a proposed NWS context watcher tooling boundary, not a confirmed implementation."
  - "NWS API is multi-component: warnings/watches/advisories/alerts are contextual regulatory-context records, forecasts are modeled records, observations are observation records, and aggregates are aggregate records."
  - "The watcher may detect source-surface, component-role, freshness, and expiry changes and emit review signals; it must not publish, promote, rebroadcast, issue alerts, provide protective-action guidance, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/nws_context_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-NWS--context--watcher-informational)
![source](https://img.shields.io/badge/source-NOAA%20NWS%20API-blueviolet)
![boundary](https://img.shields.io/badge/KFM-not--alert--authority-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/nws_context_watch/` is the proposed tooling lane for detecting review-worthy changes in NOAA NWS API context surfaces and emitting governed watcher reports. It is not a connector, not a NWS API product doctrine page, not a current-warning display engine, not a public alerting surface, not a forecast authority, not a publication path, and not hazard truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [NWS context watcher posture](#nws-context-watcher-posture)
- [Material-change model](#material-change-model)
- [Component-role discipline](#component-role-discipline)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/nws_context_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** NOAA National Weather Service context detector.

The watcher may compare approved local metadata, source sidecars, CAP/message fingerprints, issue/expiry windows, forecast cycle markers, zone/geometry summaries, station-observation summaries, component-role fields, official-source links, digests, or no-network fixtures to decide whether NWS context material should be reviewed.

The durable KFM question for this lane is:

> Did the NWS context source surface, component role, freshness state, or expiry state change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, alert rebroadcast, protective-action instruction, current-warning authority, forecast truth claim, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/nws_context_watch/README.md` | **CONFIRMED** | This README defines the NWS context watcher tooling boundary. |
| NWS context watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| Hazards life-safety boundary | **CONFIRMED in repo evidence** | KFM is not an emergency alert system and must not provide life-safety instructions. |
| NWS API product page | **CONFIRMED in repo evidence** | Product docs identify NWS API as multi-component and freshness-sensitive. |
| NWS API connector lane | **CONFIRMED in repo evidence / draft placement** | Connector output is raw/quarantine only and connector placement remains open. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Cadence must be component-specific and steward-approved. |
| Freshness and expiry thresholds | **PROPOSED / NEEDS VERIFICATION** | Must be fixture-tested before workflow use. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |
| Alert authority or rebroadcast | **DENY here** | KFM must not issue or relay NWS products as KFM alerts. |
| Protective-action guidance | **DENY here** | This lane cannot produce instructions for current hazards. |

> [!IMPORTANT]
> This folder is for watcher reports only. An NWS source change does not mean KFM has a public current-warning state. It means stewards may need to review source descriptors, connector outputs, freshness, expiry, component roles, policy decisions, receipts, catalog records, release state, or rollback paths.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific fetch and admission code. `docs/sources/catalog/noaa/` owns NOAA/NWS product doctrine. `docs/domains/hazards/` owns the life-safety boundary and hazards trust posture. `docs/domains/atmosphere/` owns atmosphere/forecast/observation context. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/nws_context_watch/README.md`.
- **PROPOSED:** NWS context watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish or alert.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether the canonical NWS connector home is `connectors/nws-api/`, `connectors/nws/`, or a nested NOAA path.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, current warning layer, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A NWS context watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not a live alert state.** Current NWS warnings, watches, advisories, and alerts require official-source, issue-time, expiry-time, and policy handling outside this lane.
4. **Watcher output is not a KFM alert.** KFM must not become the issuer or rebroadcaster of NWS alerting products.
5. **Watcher output is not protective-action guidance.** Current hazard action belongs to official channels, not KFM generated surfaces.
6. **Components remain separate.** Warnings/watches/advisories/alerts, forecasts, observations, aggregates, and unknown components must not collapse into one source role.
7. **Freshness is load-bearing.** Expired operational context must not appear as current context.
8. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/nws_context_watch/` include:

- NWS API source metadata watcher helpers;
- sidecar comparison helpers;
- CAP/message id and digest drift checks;
- issue/effective/expiry time drift checks;
- freshness-state and stale-context checks;
- forecast cycle and lead-time drift checks;
- station-observation summary drift checks;
- zone/geometry fingerprint drift checks;
- event type, severity, urgency, and certainty vocabulary drift checks;
- component-role anti-collapse checks;
- official-source-link presence checks;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or alert, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/nws_context_watch/` | Correct home | Reason |
|---|---|---|
| NWS API source fetchers or API clients of record | `connectors/nws-api/`, `connectors/nws/`, or the ratified NOAA connector home | Connectors own source acquisition and admission. |
| NWS API product doctrine | `docs/sources/catalog/noaa/nws-api.md` | Product documentation is not watcher code. |
| Hazards life-safety policy | `docs/domains/hazards/` and `policy/` | Tooling does not own life-safety doctrine or policy. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw NWS captures | `data/raw/...` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/...` | Holds are lifecycle artifacts, not tool code. |
| Processed warning, forecast, or observation records | `data/processed/...` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Forecast truth or observation truth | downstream governed domain records | Watcher reports are not source truth. |
| Tests | `tests/ingest/nws_context_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## NWS context watcher posture

The NWS context watcher should be understood as a **review signaler** for source-surface, freshness, and component-role change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- a CAP/message drift summary;
- a freshness or expiry review report;
- a component-role ambiguity report;
- a zone/geometry drift report;
- a forecast-cycle drift report;
- a station-observation summary drift report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed NWS context object of record;
- a public current-warning layer;
- a KFM-issued alert;
- a protective-action instruction;
- a forecast truth claim;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what component source-role boundary is relevant, what issue/expiry or freshness evidence was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved, current, actionable, or public.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, endpoint path, or source version metadata. | **PROPOSED** |
| Expected cadence / staleness | Surface stale, missing, or delayed expected source windows. | **PROPOSED** |
| SourceDescriptor drift | Detect changed source role, rights, activation, cadence, or canonical connector reference. | **PROPOSED** |
| CAP/message drift | Detect new, amended, cancelled, expired, or changed message identifiers and digests. | **PROPOSED** |
| Issue/expiry drift | Detect changed issue, effective, onset, ends, expires, or sent timestamps. | **PROPOSED** |
| Freshness-state drift | Detect expired-as-current or missing freshness state. | **PROPOSED** |
| Event vocabulary drift | Detect unexpected event type, severity, urgency, certainty, response type, or category values. | **PROPOSED** |
| Forecast-cycle drift | Detect changed forecast cycle, lead time, valid time, or zone/grid metadata. | **PROPOSED** |
| Observation summary drift | Detect changed station inventory, variable/unit, quality flag, or timestamp summary. | **PROPOSED** |
| Component-role ambiguity | Fail closed when warnings, forecasts, observations, aggregates, or unknown components cannot be separated. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | NWS source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_CONTEXT_CANDIDATE` | A new contextual NWS record appears available for steward review. |
| `AMENDED_CONTEXT_CANDIDATE` | An existing contextual record appears changed. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `EXPIRED_AS_CURRENT` | Expired operational context is being treated as current; fail closed. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `EVENT_VOCABULARY_DRIFT` | Event/severity/urgency/certainty vocabulary changed or could not be resolved safely. |
| `FORECAST_CYCLE_DRIFT` | Forecast cycle, lead time, or valid-time metadata changed. |
| `OBSERVATION_SUMMARY_DRIFT` | Station observation inventory, units, variables, or quality posture changed. |
| `COMPONENT_ROLE_AMBIGUOUS` | The watcher cannot preserve component source roles safely; fail closed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Component-role discipline

NWS API records must remain component-separated even when delivered through a common source family.

| Component | KFM posture | Watcher guardrail |
|---|---|---|
| Warnings / watches / advisories / alerts | `regulatory-context`, contextual only, NWS-issued | Preserve NWS id, CAP/message fields, issue/effective/expiry time, zone/geometry, freshness state, official-source link, and digest. |
| Forecasts | `modeled` | Preserve issue/cycle time, lead time, valid time, office/grid/zone, source URL, and digest. |
| Station observations | `observation` | Preserve station id, timestamp, variable, unit, quality flags where available, source URL, and digest. |
| Aggregates / rollups | `aggregate` | Preserve aggregation scope, time window, component source links, and caveats. |
| Unknown or mixed component | `candidate` / quarantine | Do not publish; require source-role and freshness review. |

The watcher may report component drift, but it must not collapse components into a single source role or convert any component into KFM-issued authority.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- NWS API SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- CAP/message metadata fixtures.
- Forecast cycle metadata fixtures.
- Station observation summary fixtures.
- Event vocabulary fixtures.
- Zone/geometry fingerprint fixtures.
- Official-source-link fixtures.
- Freshness and expiry state fixtures.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- current public-facing warning layers treated as KFM authority;
- instructions for action during current hazards;
- official warning text modified into KFM-issued language;
- source material with missing issue/expiry/freshness fields promoted toward publication;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- CAP/message drift report;
- freshness/expiry drift report;
- component-role ambiguity report;
- forecast-cycle drift report;
- observation-summary drift report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice NWS context watcher report should be compact and deterministic.

```json
{
  "tool": "nws-context-watch",
  "status": "EXPIRED_AS_CURRENT",
  "source_id": "nws_api_placeholder",
  "source_family": "noaa",
  "component": "warning_context",
  "inputs": {
    "prior_sidecar": "tests/ingest/nws_context_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/nws_context_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "component_role": "regulatory-context",
    "message_id_drift": "changed",
    "issue_time": "present",
    "expiry_time": "expired",
    "freshness_state": "expired_as_current",
    "official_source_link": "present"
  },
  "decision": {
    "outcome": "EXPIRED_AS_CURRENT",
    "reason_codes": ["NWS_EXPIRY_PASSED", "CURRENT_CONTEXT_BLOCKED"],
    "blocking": true,
    "publication": false,
    "kfm_alert_authority": false,
    "protective_action_guidance": false
  },
  "next_review": [
    "confirm NWS source descriptor and rights posture",
    "preserve component source role",
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
tests/ingest/nws_context_watch/
├── README.md
├── test_nws_context_watch.py
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
    ├── component_role_ambiguous/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── forecast_cycle_drift/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- new contextual records return `NEW_CONTEXT_CANDIDATE` or `PROPOSED_WORK_RECORD` according to configured rules;
- amended message fields return `AMENDED_CONTEXT_CANDIDATE`;
- expired context treated as current returns `EXPIRED_AS_CURRENT` and blocks current-context publication;
- missing issue/expiry/freshness fields return `ABSTAIN` or `ERROR`;
- mixed warnings/forecasts/observations return `COMPONENT_ROLE_AMBIGUOUS` and fail closed;
- forecast cycle changes return `FORECAST_CYCLE_DRIFT` without becoming observations;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/nws_context_watch
```

```bash
python tools/ingest/nws_context_watch/nws_context_watch.py \
  --prior tests/ingest/nws_context_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/nws_context_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/nws-context-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `nws_context_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing NWS context watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] The helper cannot issue, relay, or reframe NWS products as KFM-issued alerts.
- [ ] The helper cannot provide protective-action guidance.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Warnings/watches/advisories/alerts, forecasts, observations, aggregates, and unknown components remain distinct.
- [ ] Issue time, effective time, expiry time, freshness state, official-source link, source URL, and digest are preserved where applicable.
- [ ] Expired operational context cannot appear as current context.
- [ ] Watcher cadence and thresholds are component-specific and reviewable.
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
| Replace empty README with governed NWS context watcher contract | **DONE in this README** | Establishes watcher boundaries, freshness discipline, and no-alert-authority posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve NWS connector canonicality | **NEEDS VERIFICATION / ADR-class** | Prevents duplicate connector authority between `connectors/nws-api/`, `connectors/nws/`, and NOAA nested paths. |
| Add `nws_context_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, new-context, amended-context, expired-as-current, component-role ambiguity, and forecast-cycle behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hazards/Atmosphere/NWS contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces NWS source-change and freshness issues without publication or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/nws_context_watch/nws_context_watch.py` with public-safe fixtures under `tests/ingest/nws_context_watch/`. |
