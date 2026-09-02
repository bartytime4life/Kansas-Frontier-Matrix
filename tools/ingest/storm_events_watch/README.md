<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-storm-events-watch-readme
title: tools/ingest/storm_events_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-source-steward-plus-noaa-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context; watcher-only; no-publication
owning_root: tools/
responsibility: proposed NOAA/NCEI Storm Events watcher helper boundary for source-change, release-window, schema, and source-role review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../data/registry/sources/hazards/README.md
  - ../../../tools/ingest/nws_context_watch/README.md
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README defines a proposed NOAA/NCEI Storm Events watcher tooling boundary, not a confirmed implementation."
  - "NOAA/NCEI Storm Events are historical/reported hazard records with observed/administrative source-role posture. Watcher output is a review signal, not public truth."
  - "The watcher may detect release-window, file-inventory, schema, event-type, correction, geography, source-head, or source-descriptor changes. It must not publish, promote, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/storm_events_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-storm--events--watcher-informational)
![source](https://img.shields.io/badge/source-NOAA%20%7C%20NCEI-blueviolet)
![publication](https://img.shields.io/badge/publication-never--from--watcher-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/storm_events_watch/` is the proposed tooling lane for detecting review-worthy changes in NOAA/NCEI Storm Events source surfaces and emitting governed watcher reports. It is not a connector, not a Storm Events ingest pipeline, not a publication path, and not hazards truth.

---

## Purpose

`tools/ingest/storm_events_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** NOAA/NCEI Storm Events source-change detector.

The watcher may compare approved local metadata, source sidecars, release-window manifests, file inventories, schema headers, event-type vocabularies, state/month/year partitions, county/zone summaries, correction markers, source descriptor references, digests, or no-network fixtures to decide whether Storm Events material should be reviewed.

The durable KFM question for this lane is:

> Did a NOAA/NCEI Storm Events source surface, release window, schema, correction state, or geography summary change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, raw capture of record, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/storm_events_watch/README.md` | **CONFIRMED** | This README defines the Storm Events watcher tooling boundary. |
| Storm Events watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| Hazards source registry | **CONFIRMED in repo evidence / draft** | Hazards registry defines admission and source-role controls. |
| Hazards source-role matrix | **CONFIRMED in repo evidence / draft applications** | NOAA Storm Events / NCEI is mapped as observed / administrative input for `HazardEvent`, `HazardObservation`, and `HeatColdEvent`. |
| Source descriptor activation | **NEEDS VERIFICATION** | Source role, rights, cadence, and activation must be fixed in the machine-readable source registry before use. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Cadence must match Storm Events release and correction behavior and steward review needs. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must be fixture-tested before workflow use. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |

> [!IMPORTANT]
> This folder is for watcher reports only. A Storm Events source change does not mean KFM has a new public hazards fact. It means stewards may need to review source descriptors, connector outputs, release windows, corrections, validation, receipts, proofs, catalog records, release state, or rollback paths.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific fetch and admission code. `docs/domains/hazards/` owns hazards source-role, boundary, publication, and anti-collapse doctrine. `data/registry/sources/` owns source activation and descriptor truth. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility. Lifecycle data, receipts, proofs, catalog records, and release decisions live outside this tooling lane.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/storm_events_watch/README.md`.
- **PROPOSED:** Storm Events watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether the canonical NOAA/NCEI Storm Events connector home is `connectors/noaa/`, `connectors/noaa-ncei/`, or another ratified path.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A Storm Events watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer or record.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not Storm Events normalization.** Pipeline lanes own normalization, transform receipts, validation, and quarantine handoff.
4. **Watcher output is not catalog closure.** STAC, DCAT, PROV, domain catalog records, triplets, receipts, proofs, and release manifests are outside this folder.
5. **Source role remains fixed by descriptor.** Observed, administrative, aggregate, candidate, and synthetic roles must not be collapsed by helper code.
6. **Corrections remain explicit.** Revised files, late reports, corrections, or backfills must be surfaced as review candidates, not silent replacement truth.
7. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/storm_events_watch/` include:

- NOAA/NCEI Storm Events source metadata watcher helpers;
- sidecar comparison helpers;
- release-window and staleness checks;
- file inventory and digest comparison helpers;
- CSV/header/schema drift checks;
- event-type vocabulary drift checks;
- state/month/year partition drift checks;
- county, zone, FIPS, WFO, CZ type, and location-summary drift checks;
- magnitude, damage, begin/end time, and episode/event id field-presence checks;
- correction/backfill/revision drift checks;
- source descriptor reference checks;
- source-role anti-collapse checks;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or promote, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/storm_events_watch/` | Correct home | Reason |
|---|---|---|
| Storm Events source fetchers or clients of record | ratified NOAA/NCEI connector home | Connectors own source acquisition and admission. |
| Storm Events ingest pipeline logic | `pipelines/domains/hazards/...` or accepted pipeline home | Pipelines own executable lifecycle normalization. |
| Hazards domain doctrine | `docs/domains/hazards/` | Human-facing doctrine is not watcher code. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw Storm Events captures | `data/raw/...` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/...` | Holds are lifecycle artifacts, not watcher code. |
| Processed hazard events or observations | `data/processed/...` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Policy rules | `policy/` | Watchers do not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/storm_events_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## Storm Events watcher posture

The Storm Events watcher should be understood as a **review signaler** for historical/reported hazard source change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- a release-window staleness report;
- a file inventory drift report;
- a schema/header drift report;
- an event-type vocabulary drift report;
- a geography or partition drift report;
- a correction/backfill drift report;
- a source-role ambiguity report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed `HazardEvent` or `HazardObservation` of record;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what source-role boundary is relevant, what release-window or correction evidence was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved or public.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, endpoint path, file inventory, or source version metadata. | **PROPOSED** |
| Release-window / staleness | Surface stale, missing, delayed, or unexpected month/year/source windows. | **PROPOSED** |
| SourceDescriptor drift | Detect changed source role, rights, activation, cadence, steward, or canonical connector reference. | **PROPOSED** |
| File inventory drift | Detect added, removed, renamed, or replaced details, locations, or narrative files. | **PROPOSED** |
| Schema/header drift | Detect changed headers, required fields, encoding, delimiter, or field types. | **PROPOSED** |
| Event vocabulary drift | Detect unexpected event type, CZ type, magnitude type, source, WFO, or episode/event classification values. | **PROPOSED** |
| Geography drift | Detect changed state, county, FIPS, zone, WFO, begin/end lat/lon, or location-summary fields. | **PROPOSED** |
| Correction/backfill drift | Detect revised records, late additions, deleted records, replacement windows, or changed event/episode identifiers. | **PROPOSED** |
| Source-role ambiguity | Fail closed when observed, administrative, aggregate, candidate, or synthetic roles cannot be separated. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | Storm Events source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_RELEASE_WINDOW` | A new Storm Events month/year/source window appears available for steward review. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `FILE_INVENTORY_DRIFT` | Expected Storm Events files were added, removed, renamed, or replaced. |
| `SCHEMA_OR_HEADER_DRIFT` | Headers, required fields, encoding, delimiter, or field types changed. |
| `EVENT_VOCABULARY_DRIFT` | Event, source, magnitude, WFO, or classification vocabulary changed. |
| `GEOGRAPHY_DRIFT` | State/county/zone/FIPS/location-summary fields changed. |
| `CORRECTION_OR_BACKFILL_DRIFT` | Late, revised, removed, or replaced records require review. |
| `SOURCE_ROLE_AMBIGUOUS` | The watcher cannot preserve source-role separation safely; fail closed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Source-role discipline

Storm Events source material is useful only when source-role and temporal meaning remain visible.

| Surface | KFM posture | Watcher guardrail |
|---|---|---|
| Event details | `observed` / `administrative` according to descriptor and field context | Preserve event id, episode id, event type, source, time range, geography, and caveats. |
| Narratives | administrative/contextual text | Preserve as source text, not generated truth; avoid unreviewed summarization. |
| Locations | observed or reported location context | Preserve precision, uncertainty, CZ type, and source caveats; sensitive joins fail closed. |
| Corrections / backfills | correction state | Surface as review candidates; do not silently overwrite released meaning. |
| Unknown or mixed component | `candidate` / quarantine | Do not publish; require source-role, freshness, rights, and sensitivity review. |

The watcher may report source drift, but it must not collapse historical/reported Storm Events into regulatory determinations or generated hazard truth.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- Storm Events SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Release-window metadata fixtures.
- Details/locations/narratives file inventory fixtures.
- CSV/header/schema fixtures.
- Event-type vocabulary fixtures.
- State/county/FIPS/CZ/WFO summary fixtures.
- Correction/backfill summary fixtures.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- source material with missing source-role, time, geography, or descriptor fields promoted toward publication;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- release-window staleness report;
- file inventory drift report;
- schema/header drift report;
- event vocabulary drift report;
- geography drift report;
- correction/backfill drift report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice Storm Events watcher report should be compact and deterministic.

```json
{
  "tool": "storm-events-watch",
  "status": "NEW_RELEASE_WINDOW",
  "source_id": "noaa_ncei_storm_events_placeholder",
  "domain": "hazards",
  "source_role": "observed_or_administrative",
  "inputs": {
    "prior_sidecar": "tests/ingest/storm_events_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/storm_events_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "release_window": "new_candidate",
    "file_inventory_drift": "changed",
    "schema_or_header_drift": "none",
    "event_vocabulary_drift": "none",
    "geography_drift": "needs_review",
    "correction_or_backfill_drift": "unknown"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["NEW_RELEASE_WINDOW", "FILE_INVENTORY_DRIFT", "GEOGRAPHY_DRIFT"],
    "blocking": false,
    "publication": false,
    "regulatory_determination": false
  },
  "next_review": [
    "confirm Storm Events source descriptor and rights posture",
    "preserve observed/administrative source role and correction state",
    "confirm connector placement and admission workflow",
    "route through source-role and schema validation before catalog work",
    "do not publish without policy, review, release, and rollback controls"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/storm_events_watch/
├── README.md
├── test_storm_events_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── new_release_window/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── file_inventory_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── schema_or_header_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── event_vocabulary_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── correction_or_backfill_drift/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- new source windows return `NEW_RELEASE_WINDOW` or `PROPOSED_WORK_RECORD` according to configured rules;
- changed file inventory returns `FILE_INVENTORY_DRIFT`;
- header, required-field, encoding, delimiter, or field-type changes return `SCHEMA_OR_HEADER_DRIFT`;
- unexpected event type, WFO, source, or magnitude vocabulary returns `EVENT_VOCABULARY_DRIFT`;
- changed state/county/FIPS/CZ/location summary returns `GEOGRAPHY_DRIFT` without public hazard interpretation;
- corrections/backfills return `CORRECTION_OR_BACKFILL_DRIFT` and require downstream review;
- missing source descriptor reference returns `ABSTAIN` or `ERROR`;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/storm_events_watch
```

```bash
python tools/ingest/storm_events_watch/storm_events_watch.py \
  --prior tests/ingest/storm_events_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/storm_events_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/storm-events-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `storm_events_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing Storm Events watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Observed, administrative, aggregate, candidate, and synthetic records remain distinct.
- [ ] Corrections, revisions, backfills, and deleted/replaced records are surfaced for review.
- [ ] Event id, episode id, event type, time range, geography, source, and caveats are preserved where applicable.
- [ ] Sensitive joins are handled through policy and release gates.
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
| Replace empty README with governed Storm Events watcher contract | **DONE in this README** | Establishes watcher boundaries, source-role discipline, and no-publication rule. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve NOAA/NCEI connector canonicality | **NEEDS VERIFICATION / ADR-class if contested** | Prevents duplicate or unratified connector authority. |
| Add `storm_events_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, new-release-window, inventory drift, schema drift, event vocabulary drift, geography drift, and correction/backfill behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hazards/Storm Events contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces Storm Events source-change issues without publication or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/storm_events_watch/storm_events_watch.py` with public-safe fixtures under `tests/ingest/storm_events_watch/`. |
