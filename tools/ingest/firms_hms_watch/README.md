<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-firms-hms-watch-readme
title: tools/ingest/firms_hms_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-atmosphere-source-stewards
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context; not-for-life-safety; candidate-detections-only
owning_root: tools/
responsibility: proposed watcher helper boundary for NASA FIRMS and NOAA HMS smoke/fire source-change review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/nasa/nasa-firms.md
  - ../../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../../connectors/nasa-firms/README.md
  - ../../../connectors/noaa-hms-smoke/README.md
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/atmosphere/SOURCES.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README defines a proposed FIRMS/HMS watcher tooling boundary, not a confirmed implementation."
  - "FIRMS records are candidate remote-sensing detections, not confirmed fires. HMS smoke polygons are analyst-augmented qualitative plume boundaries, not surface PM2.5 or exposure determinations."
  - "The watcher may detect material source changes and emit review signals; it must not publish, promote, confirm events, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/firms_hms_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-FIRMS%20%2B%20HMS%20watcher-informational)
![sources](https://img.shields.io/badge/sources-NASA%20FIRMS%20%7C%20NOAA%20HMS-blueviolet)
![posture](https://img.shields.io/badge/posture-review--signal--only-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/firms_hms_watch/` is the proposed tooling lane for detecting review-worthy changes in NASA FIRMS and NOAA HMS smoke/fire source surfaces and emitting governed watcher reports. It is not a connector, not a wildfire confirmation system, not a smoke-exposure system, not a publication path, and not fire or smoke truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [FIRMS and HMS watcher posture](#firms-and-hms-watcher-posture)
- [Material-change model](#material-change-model)
- [Cross-product join posture](#cross-product-join-posture)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/firms_hms_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** NASA FIRMS + NOAA HMS source-change detector.

The watcher is a control-plane signaler. It may compare approved local metadata, sidecars, source fingerprints, dataset versions, issue times, density-class summaries, fire-point summaries, plume geometry fingerprints, or no-network fixtures to decide whether smoke/fire source material should be reviewed.

The durable KFM question for this lane is:

> Did NASA FIRMS or NOAA HMS source surfaces change enough to propose governed work?

The answer should be a review signal. It should never be a publication decision, confirmed fire event, PM2.5 concentration claim, exposure determination, or source-role correction.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/firms_hms_watch/README.md` | **CONFIRMED** | This README defines the watcher tooling boundary. |
| `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| FIRMS/HMS watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| NASA FIRMS product page | **CONFIRMED in repo evidence** | Product page frames FIRMS records as candidate detections, not confirmed fires. |
| NOAA HMS product page | **CONFIRMED in repo evidence** | Product page frames HMS as multi-component and anti-collapse-sensitive. |
| Smoke seam architecture | **CONFIRMED in repo evidence** | Architecture doc marks smoke as a cross-domain Atmosphere ↔ Hazards seam. |
| NASA FIRMS connector lane | **CONFIRMED in repo evidence / draft** | `connectors/nasa-firms/` documents source-admission-only boundaries. |
| NOAA HMS smoke connector lane | **CONFIRMED in repo evidence / draft / placement NEEDS VERIFICATION** | `connectors/noaa-hms-smoke/` documents source-admission-only boundaries. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Operational cadence must be steward-approved and fixture-tested. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must not become release gates without review. |
| Publication authority | **DENY here** | Watchers do not publish. |
| Fire confirmation / smoke exposure | **DENY here** | Watcher output is not event confirmation or exposure determination. |

> [!IMPORTANT]
> FIRMS detections, HMS fire points, and HMS smoke polygons are not interchangeable truth objects. FIRMS is candidate remote-sensing detection. HMS is analyst-augmented and multi-component. HMS smoke density is qualitative, not PM2.5.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific intake and admission code. `data/registry/sources/` owns source activation and descriptor truth. `docs/sources/catalog/` owns source-family and product documentation. `docs/architecture/` owns cross-domain seam architecture. `release/` owns release decisions.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/firms_hms_watch/README.md`.
- **PROPOSED:** FIRMS/HMS watcher code may live here if it is deterministic, bounded, review-signal-only, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether FIRMS/HMS watcher outputs should remain paired or split into source-specific watcher lanes after implementation evidence exists.
- **DENY:** any use of this path as a connector, raw-data sink, confirmed-event detector, PM2.5/exposure tool, publication path, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A FIRMS/HMS watcher may observe approved metadata or compare local artifacts, but it does not move data across lifecycle phases.

Required boundary rules:

1. **Watcher output is not publication.** It can propose work, not release a layer or record.
2. **Watcher output is not confirmed fire truth.** FIRMS and HMS fire detections remain source-bound detections unless downstream evidence and review produce a different governed artifact.
3. **Watcher output is not surface smoke truth.** HMS smoke polygons and density classes do not equal surface PM2.5, exposure, or air-quality determinations.
4. **Connector output remains separate.** FIRMS and HMS connectors may write only to raw or quarantine admission lanes according to their own boundaries.
5. **Processed artifacts remain separate.** Clustering, persistence windows, smoke-event composition, cross-product joins, and domain projections belong to downstream governed workflows.
6. **Catalog closure remains separate.** STAC, DCAT, PROV, domain catalog records, receipts, proofs, and release manifests are not owned by this folder.
7. **AI and UI remain downstream.** No Focus Mode, Story Node, dashboard, 3D scene, or map surface may treat watcher output as source truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/firms_hms_watch/` include:

- NASA FIRMS metadata watcher helpers.
- NOAA HMS metadata watcher helpers.
- FIRMS sidecar comparison helpers.
- HMS fire-point and smoke-polygon sidecar comparison helpers.
- Source fingerprint, `etag`, `last_modified`, digest, row count, file-list, and issue-time drift checks.
- Dataset-version and NRT/reprocessed supersession checks.
- FIRMS Fire Radiative Power summary drift checks as review signals.
- HMS smoke-plume geometry fingerprint and density-class distribution checks.
- Candidate FIRMS ↔ HMS join summary checks.
- Proposed-work-record emitters.
- Watcher run report generators.
- Dry-run CLI wrappers for local review.
- No-network fixture adapters for tests.
- Reviewer handoff summaries that explain what should be checked next.

A helper belongs here only when it is deterministic, bounded to watcher/reporting behavior, explicit about source descriptor references, conservative about material-change thresholds, unable to publish or confirm events, and tested with public-safe fixtures.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/firms_hms_watch/` | Correct home | Reason |
|---|---|---|
| FIRMS product doctrine | `docs/sources/catalog/nasa/nasa-firms.md` | Product documentation is not executable tooling. |
| HMS product doctrine | `docs/sources/catalog/noaa/hms-fire-smoke.md` | HMS anti-collapse rules belong in product docs and contracts. |
| Smoke seam architecture | `docs/architecture/smoke-atmosphere-hazards.md` | Architecture is not watcher code. |
| SourceDescriptor records | `data/registry/sources/` | Source activation and source-role truth belong in registry records. |
| FIRMS connector code of record | `connectors/nasa-firms/` or ratified connector home | Connectors own source admission. |
| HMS connector code of record | `connectors/noaa-hms-smoke/` or ratified NOAA connector home | Connectors own source admission. |
| Raw FIRMS/HMS downloads | `data/raw/...` or `data/quarantine/...` | Data lifecycle roots own source material. |
| Processed fire/smoke layers | `data/processed/...` | Transformation outputs are not tool code. |
| Catalog records | `data/catalog/...` | Catalog closure has its own root. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| PM2.5, AQI, or exposure products | atmosphere/air-quality source lanes plus policy/release gates | HMS density classes are not concentration measurements. |
| Observed ground-fire truth | observed-source pipelines and contracts | Satellite detections are not ground-confirmed incidents. |
| Policy rules | `policy/` | Watcher code does not own policy meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Tests | `tests/ingest/firms_hms_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |
| Sensitive real examples | nowhere public | Fixtures must be public-safe and synthetic or generalized. |

[Back to top](#top)

---

## FIRMS and HMS watcher posture

The FIRMS/HMS watcher should be understood as a **review signaler** for remote-sensing and analyst-augmented smoke/fire source change.

It may create:

- a watcher run report;
- a proposed work record;
- a FIRMS source metadata drift summary;
- a HMS issue-time or source-delivery drift summary;
- a FIRMS NRT/SQ supersession warning;
- a HMS geometry or density-class drift warning;
- a candidate FIRMS ↔ HMS join summary;
- a stale-input warning;
- a reviewer handoff file.

It must not create:

- a public fire layer;
- a public smoke-exposure layer;
- a promoted release;
- an EvidenceBundle;
- a policy decision;
- a source descriptor correction;
- a confirmed wildfire event;
- a PM2.5 or AQI value;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, why it may matter, what evidence or metadata was inspected, and what validation or steward review must happen next. It should not say the change is approved.

[Back to top](#top)

---

## Material-change model

The FIRMS product page frames records as candidate detections with NRT/reprocessed supersession risk. The HMS product page frames HMS as a multi-component product whose fire points, smoke polygons, density classes, analyst pass, and derivatives must be preserved separately.

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| FIRMS source metadata drift | Detect changed endpoint metadata, content length, digest, `etag`, `last_modified`, source file list, or declared update metadata. | **PROPOSED** |
| FIRMS dataset-version drift | Detect NRT/SQ change, missing dataset version, or supersession candidate. | **PROPOSED** |
| FIRMS FRP summary drift | Surface changed FRP distribution as a review signal, not event confirmation. | **PROPOSED** |
| FIRMS spatial-temporal cluster drift | Detect candidate cluster changes without promoting clusters to events. | **PROPOSED** |
| HMS issue-time drift | Detect new or changed HMS production pass or issue time. | **PROPOSED** |
| HMS component drift | Detect fire-point versus smoke-polygon component changes separately. | **PROPOSED** |
| HMS density-class drift | Detect changed light/medium/heavy polygon summaries without implying PM2.5. | **PROPOSED** |
| HMS geometry fingerprint drift | Detect plume geometry change requiring downstream review. | **PROPOSED** |
| Staleness check | Surface stale, missing, or expired source windows. | **PROPOSED** |
| Source-role guard | Fail closed when records cannot be separated into their correct source-role posture. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `FIRMS_SOURCE_DRIFT` | FIRMS source metadata, dataset version, digest, or summary changed. |
| `FIRMS_SUPERSESSION_CANDIDATE` | NRT/SQ or replacement relationship needs downstream review. |
| `HMS_SOURCE_DRIFT` | HMS issue time, source delivery, or component summary changed. |
| `HMS_GEOMETRY_DRIFT` | Smoke plume geometry fingerprint changed and needs review. |
| `HMS_DENSITY_CLASS_DRIFT` | Qualitative density-class distribution changed. |
| `JOIN_REVIEW_CANDIDATE` | FIRMS/HMS spatial-temporal join changed enough to review. |
| `SOURCE_ROLE_AMBIGUOUS` | The watcher cannot preserve component source roles safely; fail closed. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured acceptable window. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Cross-product join posture

FIRMS/HMS joins are useful only as bounded review signals. The HMS product page documents a proposed smoke-context construction where FIRMS points are joined to HMS plume buffers in a defined spatial/temporal window. This watcher may report that a candidate join set changed, but it must not publish a smoke event or wildfire event.

A join report should preserve source IDs, source roles, acquisition time, issue time, retrieval time, dataset version, source fingerprint, spatial window configuration, temporal window configuration, geometry hash or generalized geometry summary, and reason codes for why review was proposed.

```text
FIRMS detection + HMS plume context -> review candidate
review candidate + EvidenceBundle + policy + validation + release -> possible downstream public-safe context
watcher output alone -> never public truth
```

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- FIRMS source descriptor reference, not duplicated descriptor fields.
- HMS source descriptor reference, not duplicated descriptor fields.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Local metadata fixture for FIRMS source windows.
- Local metadata fixture for HMS source deliveries.
- FIRMS detection summary fixture.
- HMS fire-point and smoke-polygon summary fixture.
- HMS density-class distribution fixture.
- Geometry fingerprint fixture.
- Public-safe test data.

### Unsuitable inputs

- credentials or secrets;
- unrestricted raw source dumps outside lifecycle control;
- unpublished source material passed directly to public outputs;
- person-, household-, parcel-, property-, or owner-level claims;
- real sensitive private data;
- PM2.5/AQI values inferred only from HMS smoke density;
- confirmed wildfire event records not backed by separate governed evidence;
- exact restricted archaeology, rare-species, or infrastructure-risk coordinates.

### Suitable outputs

- watcher JSON report;
- proposed work record candidate;
- FIRMS source drift report;
- HMS source drift report;
- supersession candidate report;
- geometry drift report;
- density-class drift report;
- join-review candidate report;
- stale-input report;
- CI/reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice watcher report should be compact and deterministic.

```json
{
  "tool": "firms-hms-watch",
  "status": "JOIN_REVIEW_CANDIDATE",
  "sources": [
    {
      "source_id": "nasa-firms",
      "source_role": "candidate_detection"
    },
    {
      "source_id": "noaa-hms-fire-smoke",
      "source_role": "multi_component"
    }
  ],
  "geography_scope": "state:kansas",
  "inputs": {
    "prior_sidecar": "tests/ingest/firms_hms_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/firms_hms_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "firms_metadata_drift": "changed",
    "firms_dataset_version": "same",
    "firms_supersession": "none",
    "hms_issue_time": "changed",
    "hms_component_roles": "separable",
    "hms_geometry_fingerprint": "changed",
    "hms_density_class_distribution": "changed",
    "join_summary": "review_candidate"
  },
  "decision": {
    "outcome": "JOIN_REVIEW_CANDIDATE",
    "reason_codes": ["FIRMS_SOURCE_DRIFT", "HMS_GEOMETRY_DRIFT", "FIRMS_HMS_JOIN_CHANGED"],
    "blocking": false,
    "confirmed_fire_event": false,
    "pm25_or_exposure_claim": false,
    "publication": false
  },
  "next_review": [
    "confirm FIRMS and HMS source descriptors",
    "confirm connector placement and admission workflow",
    "preserve FIRMS candidate-detection posture",
    "preserve HMS multi-component source-role separation",
    "run downstream smoke/fire validation if approved",
    "route through catalog and release gates before public use",
    "abstain from PM2.5, exposure, or confirmed-event claims until separate evidence exists"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/firms_hms_watch/
├── README.md
├── test_firms_hms_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── firms_source_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── firms_supersession_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── hms_geometry_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── source_role_ambiguous/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── join_review_candidate/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same metadata and summaries return `NO_MATERIAL_CHANGE`;
- FIRMS source metadata drift returns `FIRMS_SOURCE_DRIFT` or `PROPOSED_WORK_RECORD` according to configured rules;
- FIRMS NRT/SQ replacement hints return `FIRMS_SUPERSESSION_CANDIDATE`;
- HMS issue-time or geometry changes return `HMS_SOURCE_DRIFT` or `HMS_GEOMETRY_DRIFT`;
- HMS density-class changes are reported as qualitative density drift, not PM2.5 or exposure;
- ambiguous HMS component roles return `SOURCE_ROLE_AMBIGUOUS` and fail closed;
- candidate join changes return `JOIN_REVIEW_CANDIDATE`, not a public event;
- missing sidecars return `ERROR` or `ABSTAIN` with clear reason codes;
- generated reports are deterministic;
- no test fixture contains real sensitive or private data;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/firms_hms_watch
```

```bash
python tools/ingest/firms_hms_watch/firms_hms_watch.py \
  --prior tests/ingest/firms_hms_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/firms_hms_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/firms-hms-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `firms_hms_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing FIRMS/HMS watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] FIRMS records remain candidate detections unless downstream evidence says otherwise.
- [ ] HMS fire points and smoke polygons preserve separate component roles.
- [ ] HMS density class is never treated as PM2.5, AQI, or exposure.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Network access is off by default or explicitly read-only and documented.
- [ ] Materiality thresholds are configured and fixture-tested.
- [ ] NRT/reprocessed supersession is represented explicitly where applicable.
- [ ] Join outputs are review candidates, not public events.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests cover no-change, FIRMS drift, supersession, HMS geometry drift, ambiguous source role, join-review, missing-input, and malformed-input cases.
- [ ] The helper does not write directly to `data/catalog/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with watcher lane contract | **DONE in this README** | Establishes FIRMS/HMS watcher boundaries and non-publication/non-exposure rule. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve paired versus split watcher design | **NEEDS VERIFICATION / ADR-class if broad** | Prevents accidental cross-source authority collapse. |
| Add `firms_hms_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe watcher fixtures | **PROPOSED** | Proves no-change, FIRMS drift, supersession, HMS geometry drift, source-role ambiguity, and join-review behavior. |
| Align proposed-work-record schema | **PROPOSED / NEEDS VERIFICATION** | Match accepted contracts/schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces smoke/fire source drift without publication, exposure, or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/firms_hms_watch/firms_hms_watch.py` with public-safe fixtures under `tests/ingest/firms_hms_watch/`. |
