<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-hydrology-watch-readme
title: tools/ingest/hydrology_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-source-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public; watcher-only; no-publication; not-for-life-safety
owning_root: tools/
responsibility: proposed hydrology watcher helper boundary for source-change detection and review-signal reports
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../pipelines/domains/hydrology/ingest/README.md
  - ../../../tools/ingest/hydrology/README.md
  - ../../../connectors/usgs/water_data/README.md
  - ../../../connectors/usgs/nhdplus_hr/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../data/raw/hydrology/README.md
  - ../../../data/quarantine/
  - ../../../data/receipts/hydrology/README.md
  - ../../../data/proofs/hydrology/README.md
  - ../../../release/candidates/hydrology/README.md
notes:
  - "This README defines a proposed hydrology watcher tooling boundary, not a confirmed implementation."
  - "Hydrology watcher helpers may detect source-surface or sidecar changes and emit review signals; they do not fetch sources of record, normalize pipeline data, publish, promote, or decide hydrologic truth."
  - "Observed gauge readings, aggregate values, modeled hydrographs, regulatory context, official-source context, derived terrain/topology, and generated summaries must remain separate truth classes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/hydrology_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydrology--watcher-informational)
![anti-collapse](https://img.shields.io/badge/NFHL-%E2%89%A0-observed--flooding-red)
![publication](https://img.shields.io/badge/publication-never--from--watcher-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/hydrology_watch/` is the proposed tooling lane for hydrology source-change watchers: compare metadata, sidecars, source fingerprints, expected release windows, and review summaries so stewards know when hydrology source material may need governed work. It is not a connector, not the hydrology ingest pipeline, not a preflight validator of record, not a publication path, and not hydrologic truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Hydrology watcher posture](#hydrology-watcher-posture)
- [Material-change model](#material-change-model)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/hydrology_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** hydrology source-change detector.

The watcher may compare approved local metadata, source sidecars, endpoint fingerprints, source descriptor references, expected cadence windows, file inventories, schema hints, gauge/site counts, parameter-code summaries, HUC/reach version markers, NFHL package metadata, or no-network fixtures to decide whether hydrology source material should be reviewed.

The durable KFM question for this lane is:

> Did a hydrology source surface change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, public layer, current-condition assertion, official warning, regulatory determination, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/hydrology_watch/README.md` | **CONFIRMED** | This README defines the watcher tooling boundary. |
| Hydrology watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| `tools/ingest/hydrology/README.md` | **CONFIRMED in repo evidence** | Nearby helper lane is preflight/report tooling, not watcher cadence logic. |
| Hydrology domain README | **CONFIRMED in repo evidence** | Domain docs define Hydrology as evidence-bound and time-aware. |
| Hydrology ingest pipeline README | **CONFIRMED in repo evidence / draft** | Pipeline lane owns executable ingest normalization after source admission. |
| USGS Water Data connector lane | **CONFIRMED in repo evidence / draft** | Connector output is raw/quarantine only and preserves provisional/approved distinctions. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Cadence must be source-specific and steward-approved. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must be fixture-tested before becoming workflow signals. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |
| Current safety guidance | **DENY here** | This lane cannot issue current operational guidance. |
| NFHL observed-flood claim | **DENY here** | NFHL and similar regulatory sources remain regulatory context, not observed inundation. |

> [!IMPORTANT]
> This folder is for watcher reports only. A change in a hydrology source surface does not mean KFM has a new public fact. It means stewards may need to review source descriptors, connector outputs, pipeline inputs, validation, receipts, proofs, catalog records, release state, or rollback paths.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific fetch and admission code. `tools/ingest/hydrology/` owns helper preflight/report support. `pipelines/domains/hydrology/ingest/` owns the executable hydrology ingest pipeline boundary. `docs/domains/hydrology/` owns human-facing domain doctrine. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/hydrology_watch/README.md`.
- **PROPOSED:** hydrology watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether hydrology watcher outputs should be split by source family after implementation evidence exists.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, map layer, current-condition surface, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A hydrology watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not processed hydrology truth.** Processed records require pipeline validation and downstream governance.
4. **Watcher output is not catalog closure.** STAC, DCAT, PROV, domain catalog records, triplets, receipts, proofs, and release manifests are outside this folder.
5. **NFHL remains regulatory context.** Regulatory flood-hazard context must not be relabeled as observed flooding.
6. **Provisional and approved values remain distinct.** Source updates must preserve approval state and revision state.
7. **Modeled outputs remain modeled.** Reconstructed hydrographs and model-derived surfaces require method/model receipts and must not be relabeled as observations.
8. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/hydrology_watch/` include:

- source metadata watcher helpers;
- sidecar comparison helpers;
- source descriptor reference checks;
- expected cadence and staleness checks;
- endpoint fingerprint comparison helpers;
- file inventory and digest comparison helpers;
- USGS site/parameter/count drift summaries;
- provisional/approved state drift summaries;
- WBD/HUC version drift summaries;
- NHDPlus/3DHP reach version drift summaries;
- NFHL package/version metadata drift summaries;
- water-quality parameter-code or method-list drift summaries;
- groundwater well inventory drift summaries;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or promote, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/hydrology_watch/` | Correct home | Reason |
|---|---|---|
| Source fetchers or API clients of record | `connectors/<source>/` | Connectors own source acquisition and admission. |
| Hydrology ingest preflight helpers | `tools/ingest/hydrology/` | Preflight validation support is adjacent but distinct from watch cadence logic. |
| Hydrology ingest pipeline logic of record | `pipelines/domains/hydrology/ingest/` | Pipelines own executable lifecycle normalization. |
| Declarative pipeline specs | `pipeline_specs/hydrology/` | Run configuration is not watcher code. |
| Hydrology domain doctrine | `docs/domains/hydrology/` | Human-facing doctrine is not executable tooling. |
| Source product documentation | `docs/sources/catalog/...` | Product docs are not watcher code. |
| Source descriptors | `data/registry/sources/hydrology/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw source captures | `data/raw/hydrology/` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/hydrology/` | Holds are lifecycle artifacts, not tool code. |
| Processed hydrology records | `data/processed/hydrology/` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Policy rules | `policy/` | Watchers do not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/hydrology_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## Hydrology watcher posture

The hydrology watcher should be understood as a **review signaler** for hydrology source change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- a source staleness report;
- a source version drift report;
- a parameter/site/inventory drift summary;
- an approval-state drift report;
- a regulatory-context package drift report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed hydrology object of record;
- a public hydrology layer;
- a current condition claim;
- an NFHL observed-inundation claim;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what source-role boundary is relevant, what evidence or metadata was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved or public.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, file inventory, or source version metadata. | **PROPOSED** |
| Expected cadence / staleness | Surface missing, stale, or delayed expected source windows. | **PROPOSED** |
| SourceDescriptor drift | Detect changed descriptor reference, source role, rights, cadence, or activation state. | **PROPOSED** |
| Site inventory drift | Detect changed gauge, well, station, reach, HUC, or waterbody inventory counts. | **PROPOSED** |
| Parameter-code drift | Detect changed parameter vocabulary, units, statistic types, or method fields. | **PROPOSED** |
| Approval-state drift | Detect provisional/approved replacement or approval-state change requiring review. | **PROPOSED** |
| Geometry/version drift | Detect changed HUC, reach, CRS, datum, or regulatory-package version metadata. | **PROPOSED** |
| Source-role ambiguity | Fail closed when observed, aggregate, modeled, regulatory, official-source, derived, or generated roles cannot be separated. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | Source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_SOURCE_WINDOW` | A new source window or version appears available for steward review. |
| `STALE_INPUT` | Expected source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `PARAMETER_OR_UNIT_DRIFT` | Parameter, unit, statistic, or method vocabulary changed. |
| `APPROVAL_STATE_DRIFT` | Provisional/approved or revision state changed. |
| `GEOMETRY_OR_VERSION_DRIFT` | Geometry, datum, CRS, HUC/reach, or package version changed. |
| `SOURCE_ROLE_AMBIGUOUS` | The watcher cannot preserve source-role separation safely; fail closed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Local metadata fixtures for hydrology source windows.
- USGS Water Data endpoint metadata fixtures.
- WBD/HUC version metadata fixtures.
- NHDPlus/3DHP reach metadata fixtures.
- NFHL regulatory package metadata fixtures.
- Water-quality parameter-code fixtures.
- Groundwater well inventory fixtures.
- Geometry, CRS, datum, and unit sidecars.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- unreviewed public-facing maps or tiles;
- official warning text treated as KFM-issued guidance;
- sensitive infrastructure details without policy review;
- private well owner details or precise private infrastructure where rights/sensitivity are unresolved;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- staleness report;
- source descriptor drift report;
- inventory drift report;
- approval-state drift report;
- geometry/version drift report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice hydrology watcher report should be compact and deterministic.

```json
{
  "tool": "hydrology-watch",
  "status": "SOURCE_METADATA_DRIFT",
  "source_id": "usgs_water_data_placeholder",
  "domain": "hydrology",
  "inputs": {
    "prior_sidecar": "tests/ingest/hydrology_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/hydrology_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "staleness": "fresh",
    "parameter_or_unit_drift": "none",
    "approval_state_drift": "provisional_to_approved_candidate",
    "geometry_or_version_drift": "none",
    "source_role": "observed"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["SOURCE_METADATA_DRIFT", "APPROVAL_STATE_DRIFT"],
    "blocking": false,
    "publication": false
  },
  "next_review": [
    "confirm source descriptor and rights posture",
    "preserve observed versus aggregate versus regulatory source role",
    "run connector/admission workflow if approved",
    "route through hydrology ingest pipeline after admission",
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
tests/ingest/hydrology_watch/
├── README.md
├── test_hydrology_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── source_metadata_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── stale_input/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── approval_state_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── nfhl_version_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── source_role_ambiguous/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- changed metadata returns `SOURCE_METADATA_DRIFT` or `PROPOSED_WORK_RECORD` according to configured rules;
- stale expected source windows return `STALE_INPUT`;
- provisional-to-approved replacement hints return `APPROVAL_STATE_DRIFT`;
- NFHL fixture reports version/regulatory package drift without observed-flood language;
- missing source descriptor reference returns `ABSTAIN` or `ERROR`;
- ambiguous source role returns `SOURCE_ROLE_AMBIGUOUS` and fails closed;
- generated reports are deterministic;
- no test fixture contains sensitive private infrastructure or private well-owner details;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/hydrology_watch
```

```bash
python tools/ingest/hydrology_watch/hydrology_watch.py \
  --prior tests/ingest/hydrology_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/hydrology_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/hydrology-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `hydrology_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing hydrology watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Observed, aggregate, modeled, regulatory, official-source, derived, and generated records remain distinct.
- [ ] NFHL and similar regulatory layers cannot be treated as observed flooding.
- [ ] Provisional and approved values remain distinct.
- [ ] Unit, parameter, datum/CRS, time basis, and source role are checked where applicable.
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
| Replace empty README with governed hydrology watcher contract | **DONE in this README** | Establishes watcher boundaries and anti-collapse posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve watcher-vs-preflight split | **NEEDS VERIFICATION** | Prevents duplication between `hydrology_watch/` and `hydrology/`. |
| Add `hydrology_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, metadata drift, stale input, approval-state drift, NFHL version drift, and source-role ambiguity behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hydrology contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces source-change and anti-collapse issues without publication side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/hydrology_watch/hydrology_watch.py` with public-safe fixtures under `tests/ingest/hydrology_watch/`. |
