<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-usgs-eq-watch-readme
title: tools/ingest/usgs_eq_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-geology-source-stewards
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context; watcher-only; no-publication; not-alerting
owning_root: tools/
responsibility: proposed USGS earthquake watcher helper boundary for source-change, event-update, sub-product, and source-role review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/usgs/earthquake-catalog.md
  - ../../../docs/sources/catalog/usgs/README.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/geology/README.md
  - ../../../connectors/usgs-earthquake/README.md
  - ../../../connectors/usgs/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README defines a proposed USGS earthquake watcher tooling boundary, not a confirmed implementation."
  - "USGS earthquake material is source-role heterogeneous: event origin records are observed, magnitude/product refinements may be modeled, ShakeMap/PAGER/focal mechanisms are modeled, and DYFI is crowdsourced observed/context evidence."
  - "USGS earthquake events refine over time; watcher output must surface event-update candidates and preserve append-only snapshot discipline rather than silently replacing prior event states."
  - "The watcher may detect source-head, event-update, product, schema, geometry, freshness, or source-descriptor changes and emit review signals; it must not publish, promote, alert, decide final event truth, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/usgs_eq_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-USGS--earthquake--watcher-informational)
![source](https://img.shields.io/badge/source-USGS%20Earthquake-blueviolet)
![versioning](https://img.shields.io/badge/versioning-append--only--snapshots-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/usgs_eq_watch/` is the proposed tooling lane for detecting review-worthy changes in USGS earthquake source surfaces and emitting governed watcher reports. It is not a connector, not an earthquake ingest pipeline, not an alerting surface, not a publication path, and not seismic truth.

---

## Purpose

`tools/ingest/usgs_eq_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** USGS Earthquake Catalog source-change detector.

The watcher may compare approved local metadata, source sidecars, feed fingerprints, event ids, update times, product-code inventories, origin/magnitude/depth summaries, ShakeMap/PAGER/DYFI/focal-mechanism product pointers, geometry fingerprints, source descriptor references, digests, or no-network fixtures to decide whether USGS earthquake material should be reviewed.

The durable KFM question for this lane is:

> Did a USGS earthquake source surface, event snapshot, sub-product, schema, geometry, or source-role summary change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, raw capture of record, final event claim, final impact claim, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/usgs_eq_watch/README.md` | **CONFIRMED** | This README defines the USGS earthquake watcher tooling boundary. |
| USGS earthquake watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| USGS earthquake product page | **CONFIRMED in repo evidence / draft** | Product docs define heterogeneous source roles and append-only event snapshot discipline. |
| USGS earthquake connector lane | **CONFIRMED in repo evidence / draft / placement NEEDS VERIFICATION** | Connector output may enter raw/quarantine only and connector canonicality remains open. |
| Hazards source-role matrix | **CONFIRMED in repo evidence / draft applications** | Matrix requires source roles to remain first-class and fail closed when conflated. |
| Source descriptor activation | **NEEDS VERIFICATION** | Source role, rights, cadence, and activation must be fixed in the source registry before operational use. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Cadence must match feed/update behavior and steward review needs. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must be fixture-tested before workflow use. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |
| Final event or impact truth | **DENY here** | Watcher output does not decide final earthquake meaning. |

> [!IMPORTANT]
> This folder is for watcher reports only. A USGS earthquake source change does not mean KFM has a new public seismic fact. It means stewards may need to review source descriptors, connector outputs, event snapshots, product updates, validation, receipts, proofs, catalog records, release state, or rollback paths.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific fetch and admission code. `docs/sources/catalog/usgs/` owns USGS product documentation. `docs/domains/hazards/` and `docs/domains/geology/` own domain interpretation. `data/registry/sources/` owns source activation and descriptor truth. `contracts/`, `schemas`, and `policy/` own meaning, shape, and admissibility. Lifecycle data, receipts, proofs, catalog records, and release decisions live outside this tooling lane.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/usgs_eq_watch/README.md`.
- **PROPOSED:** USGS earthquake watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether the canonical USGS earthquake connector home is `connectors/usgs-earthquake/`, `connectors/usgs/earthquake/`, or another ratified path.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, current-condition authority, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A USGS earthquake watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer or record.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not earthquake normalization.** Pipeline lanes own normalization, transform receipts, validation, and quarantine handoff.
4. **Watcher output is not catalog closure.** STAC, DCAT, PROV, domain catalog records, triplets, receipts, proofs, and release manifests are outside this folder.
5. **Event snapshots are append-only.** Event updates, origin refinements, magnitude revisions, and sub-product updates must be surfaced as review candidates, not silent replacement truth.
6. **Sub-products remain separate.** Origin records, magnitude estimates, ShakeMap, PAGER, focal-mechanism/moment-tensor products, and DYFI reports must not collapse into one source role.
7. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/usgs_eq_watch/` include:

- USGS earthquake feed/source metadata watcher helpers;
- sidecar comparison helpers;
- event id and event update-time drift checks;
- origin-time, magnitude, depth, geometry, and status summary drift checks;
- event product inventory drift checks;
- ShakeMap, PAGER, focal-mechanism, moment-tensor, and DYFI product pointer checks;
- event snapshot digest and provenance checks;
- source descriptor reference checks;
- feed cadence and staleness checks;
- schema/header/field-presence drift checks;
- geometry/CRS/uncertainty sidecar checks;
- source-role anti-collapse checks;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or promote, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/usgs_eq_watch/` | Correct home | Reason |
|---|---|---|
| USGS earthquake source fetchers or clients of record | ratified USGS earthquake connector home | Connectors own source acquisition and admission. |
| Earthquake ingest pipeline logic | `pipelines/domains/hazards/...`, `pipelines/domains/geology/...`, or accepted pipeline home | Pipelines own executable lifecycle normalization. |
| USGS earthquake product doctrine | `docs/sources/catalog/usgs/earthquake-catalog.md` | Product documentation is not watcher code. |
| Hazards or Geology doctrine | `docs/domains/hazards/`, `docs/domains/geology/` | Human-facing doctrine is not watcher code. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw USGS earthquake captures | `data/raw/...` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/...` | Holds are lifecycle artifacts, not watcher code. |
| Processed earthquake events or products | `data/processed/...` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Policy rules | `policy/` | Watchers do not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/usgs_eq_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## USGS earthquake watcher posture

The USGS earthquake watcher should be understood as a **review signaler** for event updates and source-surface change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- an event-update candidate report;
- an event snapshot drift report;
- a product inventory drift report;
- a sub-product role ambiguity report;
- a geometry/uncertainty drift report;
- a stale-source report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed `EarthquakeEvent` of record;
- a final impact or damage claim;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what source-role boundary is relevant, what event snapshot or product update evidence was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved or public.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, endpoint path, file inventory, or source version metadata. | **PROPOSED** |
| Event update drift | Detect changed `event_id`, `origin_time`, `update_time`, event status, magnitude, depth, or geometry summary. | **PROPOSED** |
| Snapshot digest drift | Detect changed immutable event snapshot fingerprints or missing prior snapshot links. | **PROPOSED** |
| Product inventory drift | Detect added, removed, replaced, or revised PAGER, ShakeMap, DYFI, focal mechanism, or moment tensor products. | **PROPOSED** |
| Sub-product role drift | Detect role ambiguity between observed origin records, modeled products, and crowdsourced reports. | **PROPOSED** |
| Geometry/uncertainty drift | Detect changed epicenter, depth, uncertainty, ShakeMap grid, CRS, or geometry lineage. | **PROPOSED** |
| Feed cadence / staleness | Surface stale, missing, delayed, or unexpected source windows. | **PROPOSED** |
| SourceDescriptor drift | Detect changed source role, rights, activation, cadence, steward, or canonical connector reference. | **PROPOSED** |
| Schema/header drift | Detect changed fields, expected product keys, encoding, geometry keys, or type hints. | **PROPOSED** |
| Source-role ambiguity | Fail closed when observed, modeled, crowdsourced, administrative, candidate, or synthetic roles cannot be separated. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | USGS source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_EVENT_CANDIDATE` | A new event id appears available for steward review. |
| `EVENT_UPDATE_CANDIDATE` | An existing event appears revised and needs append-only snapshot review. |
| `SNAPSHOT_DIGEST_DRIFT` | Snapshot fingerprint changed or prior snapshot linkage is missing. |
| `PRODUCT_INVENTORY_DRIFT` | Event sub-products were added, removed, replaced, or revised. |
| `GEOMETRY_OR_UNCERTAINTY_DRIFT` | Geometry, depth, uncertainty, CRS, or product geometry lineage changed. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `SCHEMA_OR_FIELD_DRIFT` | Fields, expected product keys, encoding, or type hints changed. |
| `SOURCE_ROLE_AMBIGUOUS` | The watcher cannot preserve source-role separation safely; fail closed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Source-role discipline

USGS earthquake source material is useful only when source-role and event-versioning meaning remain visible.

| Surface | KFM posture | Watcher guardrail |
|---|---|---|
| Event origin record | observed event record | Preserve USGS `event_id`, origin time, update time, location, depth, magnitude, event status, source URL, and digest. |
| Magnitude estimates | observed/model-associated attribute depending on method and update context | Preserve method, update time, uncertainty, and revision state. |
| ShakeMap | modeled ground-motion product | Preserve product id, grid/raster lineage, update time, source URL, geometry, and caveats. |
| PAGER | modeled impact/loss estimate | Preserve product id, run/update time, uncertainty, and caveats; do not relabel as measured impact. |
| Focal mechanism / moment tensor | modeled fault-parameter product | Preserve method, update time, and uncertainty/caveats. |
| DYFI | crowdsourced observed/context evidence | Preserve aggregate/report context without treating it as instrumented ground motion. |
| Event updates | correction/update state | Surface as append-only snapshot candidates; do not silently overwrite. |
| Unknown or mixed component | candidate / quarantine | Do not publish; require source-role, freshness, rights, and sensitivity review. |

The watcher may report source drift, but it must not collapse observed origins, modeled products, crowdsourced reports, or generated summaries into one authority channel.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- USGS earthquake SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Feed metadata fixtures.
- Event id / update-time summary fixtures.
- Event snapshot digest fixtures.
- Product inventory fixtures.
- ShakeMap/PAGER/DYFI/focal-mechanism pointer fixtures.
- Geometry, CRS, depth, magnitude, and uncertainty sidecars.
- Schema/header/field fixtures.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- source material with missing source-role, time, geometry, product, or descriptor fields promoted toward publication;
- modeled products treated as observations;
- crowdsourced reports treated as instrumented measurements;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- new event candidate report;
- event update candidate report;
- snapshot digest drift report;
- product inventory drift report;
- geometry/uncertainty drift report;
- source-role ambiguity report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice USGS earthquake watcher report should be compact and deterministic.

```json
{
  "tool": "usgs-eq-watch",
  "status": "EVENT_UPDATE_CANDIDATE",
  "source_id": "usgs_earthquake_placeholder",
  "domain": "hazards_geology",
  "inputs": {
    "prior_sidecar": "tests/ingest/usgs_eq_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/usgs_eq_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "event_id": "usgs_event_placeholder",
    "event_update_time": "changed",
    "snapshot_digest": "changed",
    "product_inventory_drift": "changed",
    "geometry_or_uncertainty_drift": "none",
    "source_role_separation": "preserved"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["EVENT_UPDATE_CANDIDATE", "SNAPSHOT_DIGEST_DRIFT", "PRODUCT_INVENTORY_DRIFT"],
    "blocking": false,
    "publication": false,
    "final_event_truth": false,
    "final_impact_truth": false
  },
  "next_review": [
    "confirm USGS earthquake source descriptor and rights posture",
    "preserve event snapshot append-only discipline",
    "preserve observed/model/crowdsourced sub-product roles",
    "confirm connector placement and admission workflow",
    "validate contracts and schemas before catalog or release work"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/usgs_eq_watch/
├── README.md
├── test_usgs_eq_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── new_event_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── event_update_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── product_inventory_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── geometry_or_uncertainty_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── source_role_ambiguous/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- new event ids return `NEW_EVENT_CANDIDATE` or `PROPOSED_WORK_RECORD` according to configured rules;
- changed update time or event attributes return `EVENT_UPDATE_CANDIDATE`;
- changed snapshot fingerprint returns `SNAPSHOT_DIGEST_DRIFT`;
- changed sub-product inventory returns `PRODUCT_INVENTORY_DRIFT`;
- geometry, depth, magnitude, CRS, or uncertainty changes return `GEOMETRY_OR_UNCERTAINTY_DRIFT`;
- modeled products cannot pass as observed origin records;
- DYFI cannot pass as instrumented ground motion;
- missing source descriptor reference returns `ABSTAIN` or `ERROR`;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/usgs_eq_watch
```

```bash
python tools/ingest/usgs_eq_watch/usgs_eq_watch.py \
  --prior tests/ingest/usgs_eq_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/usgs_eq_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/usgs-eq-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `usgs_eq_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing USGS earthquake watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Event origin records, magnitude estimates, ShakeMap, PAGER, focal-mechanism/moment-tensor products, and DYFI remain distinct.
- [ ] Event updates are append-only snapshot candidates, not silent overwrites.
- [ ] Modeled products are not relabeled as observations.
- [ ] DYFI is not relabeled as instrumented ground motion.
- [ ] Event id, origin time, update time, geometry, depth, magnitude, product links, source URL, and digest are preserved where applicable.
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
| Replace empty README with governed USGS earthquake watcher contract | **DONE in this README** | Establishes watcher boundaries, source-role discipline, and append-only event snapshot posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve USGS earthquake connector canonicality | **NEEDS VERIFICATION / ADR-class if contested** | Prevents duplicate or unratified connector authority. |
| Add `usgs_eq_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, new-event, event-update, product-inventory drift, geometry/uncertainty drift, and source-role ambiguity behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hazards/Geology/USGS earthquake contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces USGS earthquake source-change issues without publication or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/usgs_eq_watch/usgs_eq_watch.py` with public-safe fixtures under `tests/ingest/usgs_eq_watch/`. |
