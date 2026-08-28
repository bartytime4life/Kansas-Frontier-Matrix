<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-hydrology-readme
title: tools/ingest/hydrology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-source-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public; source-admission-support; no-publication; not-for-life-safety
owning_root: tools/
responsibility: proposed hydrology ingest helper boundary for source-shape checks, preflight reports, and governed handoff support
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../pipelines/domains/hydrology/ingest/README.md
  - ../../../connectors/usgs/water_data/README.md
  - ../../../connectors/usgs/nhdplus_hr/README.md
  - ../../../docs/sources/catalog/usgs/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../data/raw/hydrology/README.md
  - ../../../data/quarantine/
  - ../../../data/receipts/hydrology/README.md
  - ../../../data/proofs/hydrology/README.md
  - ../../../release/candidates/hydrology/README.md
notes:
  - "This README defines a proposed hydrology ingest tooling boundary, not a confirmed implementation."
  - "Hydrology ingest helpers may inspect, preflight, normalize-preview, and report on admitted source material; they do not fetch sources of record, publish, promote, or decide hydrologic truth."
  - "Observed gauge readings, aggregate values, modeled hydrographs, regulatory context, official-source context, derived terrain/topology, and generated summaries must remain separate truth classes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/hydrology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydrology--ingest--helpers-informational)
![anti-collapse](https://img.shields.io/badge/NFHL-%E2%89%A0-observed--flooding-red)
![publication](https://img.shields.io/badge/publication-never--from--tools-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/hydrology/` is the proposed tooling lane for hydrology ingest support: source-shape checks, source-role preflight, timestamp/unit/datum checks, report generation, and reviewer handoff helpers. It is not a connector, not the hydrology pipeline of record, not a catalog/proof/release root, not an emergency-warning surface, and not hydrologic truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Hydrology ingest posture](#hydrology-ingest-posture)
- [Source-role and temporal discipline](#source-role-and-temporal-discipline)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/hydrology/` exists to hold durable, repo-wide helper logic that supports hydrology ingest review without becoming the hydrology ingest pipeline itself.

The lane may inspect already-admitted lifecycle inputs, fixtures, manifests, sidecars, or source-shape samples for hydrology sources such as USGS Water Data, WBD/HUC units, NHDPlus/3DHP, NFHL context, groundwater wells, water-quality observations, terrain/topology inputs, and state water datasets.

The durable KFM question for this lane is:

> Can this hydrology source material be represented as reviewable, evidence-bound ingest candidates without collapsing observed, aggregate, modeled, regulatory, official-source, derived, generated, or release-state semantics?

The answer should be a preflight report, dry-run handoff, or reviewer signal. It should never be a public layer, official warning, regulatory determination, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/hydrology/README.md` | **CONFIRMED** | This README defines the hydrology ingest-tooling boundary. |
| Hydrology ingest helper executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| Hydrology domain README | **CONFIRMED in repo evidence** | Domain docs define Hydrology as evidence-bound and time-aware. |
| Hydrology ingest pipeline README | **CONFIRMED in repo evidence / draft** | Pipeline lane owns executable ingest normalization after source admission. |
| USGS Water Data connector lane | **CONFIRMED in repo evidence / draft** | Connector output is raw/quarantine only and preserves provisional/approved distinctions. |
| Source descriptors | **NEEDS VERIFICATION** | Activation and source-specific rights must be verified before relying on any source. |
| Publication authority | **DENY here** | Tools do not publish or promote. |
| Emergency warning or operational guidance | **DENY here** | This lane cannot issue current safety guidance. |
| NFHL observed-flood claim | **DENY here** | NFHL and similar regulatory sources remain regulatory context, not observed inundation. |

> [!IMPORTANT]
> Hydrology ingest tooling must preserve truth-class separation. Observed gauge readings, aggregate values, site metadata, modeled hydrographs, NFHL/regulatory context, terrain/topology derivatives, and generated summaries are different kinds of records and must not be collapsed by helper code.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific fetch and admission code. `pipelines/domains/hydrology/ingest/` owns the executable hydrology ingest pipeline boundary. `docs/domains/hydrology/` owns human-facing domain doctrine. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility. Lifecycle data, receipts, proofs, catalog records, and release decisions live outside this tooling lane.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/hydrology/README.md`.
- **PROPOSED:** hydrology ingest helper code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** which helper functions belong here versus in `pipelines/domains/hydrology/ingest/` after implementation evidence exists.
- **DENY:** any use of this path as a source connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, map layer, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A hydrology ingest helper may inspect, preflight, compare, normalize-preview, or report on source material. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Tool output is not publication.** It can propose review work, not release a layer.
2. **Tool output is not a connector receipt.** Connector admission remains in connector or workflow-owned surfaces.
3. **Tool output is not processed hydrology truth.** Processed records require pipeline validation and downstream governance.
4. **Tool output is not catalog closure.** STAC, DCAT, PROV, domain catalog records, triplets, receipts, proofs, and release manifests are outside this folder.
5. **NFHL remains regulatory context.** Regulatory flood-hazard context must not be relabeled as observed flooding.
6. **Provisional and approved values remain distinct.** USGS Water Data and similar sources must preserve approval state and revision state.
7. **Modeled outputs remain modeled.** Reconstructed hydrographs and model-derived surfaces need model/method receipts and must not be relabeled as observations.
8. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this helper lane or treat helper output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/hydrology/` include:

- source-shape preflight helpers;
- SourceDescriptor-reference checkers;
- site/time/parameter/unit/datum validators used before a pipeline run;
- provisional/approved state checks;
- source-role anti-collapse checks;
- NFHL regulatory-context guard checks;
- HUC/WBD and reach-identity sidecar checks;
- geometry/datum/CRS preflight checks;
- water-quality method/parameter-code preflight checks;
- groundwater well metadata sanity checks;
- input manifest and sidecar diff helpers;
- quarantine-reason report generators;
- dry-run handoff generators for hydrology pipelines;
- reviewer handoff summaries;
- no-network fixture adapters for tests.

A helper belongs here only when it is:

- deterministic;
- network-free by default;
- explicit about read paths and write paths;
- dry-run friendly;
- explicit about source role, time basis, units, datum, and approval state;
- unable to publish or promote;
- unable to write directly to lifecycle authority roots without an explicit governed workflow;
- tested with public-safe fixtures;
- clear about whether its output is a report, candidate handoff, or quarantine signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/hydrology/` | Correct home | Reason |
|---|---|---|
| Source fetchers or API clients of record | `connectors/<source>/` | Connectors own source acquisition and admission. |
| Hydrology ingest pipeline logic of record | `pipelines/domains/hydrology/ingest/` | Pipelines own executable lifecycle normalization. |
| Declarative pipeline specs | `pipeline_specs/hydrology/` | Run configuration is not tooling support code. |
| Hydrology domain doctrine | `docs/domains/hydrology/` | Human-facing doctrine is not executable tooling. |
| Source product documentation | `docs/sources/catalog/...` | Product docs are not helper code. |
| Source descriptors | `data/registry/sources/hydrology/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw source captures | `data/raw/hydrology/` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/hydrology/` | Holds are lifecycle artifacts, not tool code. |
| Processed hydrology records | `data/processed/hydrology/` | Validated outputs are not tool code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Policy rules | `policy/` | Tooling does not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/hydrology/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## Hydrology ingest posture

The hydrology ingest helper should be understood as an **operator and reviewer support lane**.

It may create:

- a source-shape report;
- a source-role preflight report;
- a unit/datum/time-basis report;
- an approval-state report;
- a geometry/CRS preflight report;
- a quarantine-reason report;
- a pipeline dry-run handoff file;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed hydrology object of record;
- a public hydrology layer;
- a flood event or current condition claim;
- an NFHL observed-inundation claim;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what source material was inspected, what uncertainty was found, what source-role boundary is relevant, and what downstream validation/review must happen next. It should not say the claim is true, safe, official, or approved.

[Back to top](#top)

---

## Source-role and temporal discipline

Hydrology ingest tooling must keep these distinctions visible.

| Surface | Required posture |
|---|---|
| Gauge/site metadata | Administrative context; not an observation. |
| Instantaneous values | Observed reading with site, parameter, unit, qualifier, timestamp, and approval/provisional state. |
| Daily values / annual statistics | Aggregate values with statistic type and period. |
| Peak flows | Observed or observed-with-uncertainty according to source fields; preserve caveats. |
| Water-quality samples | Observed sample/analysis records with method metadata and qualifiers where available. |
| Groundwater/aquifer observations | Observation records with site, depth/context, time basis, unit, and method where available. |
| WBD/HUC units | Watershed boundary context; preserve version/source. |
| NHDPlus / 3DHP / reaches | Hydro-network identity/context; preserve version and reach identifiers. |
| NFHL | Regulatory flood-hazard context; never observed flooding. |
| Modeled or reconstructed hydrographs | Modeled outputs with method/model receipt references. |
| Terrain/topology derivatives | Derived surfaces; not source observations. |
| Generated summaries | Downstream carriers; not evidence. |

Time kinds should not be collapsed. Preserve observation time, valid time, retrieval time, processing time, catalog time, release time, and correction time where available.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- SourceDescriptor references.
- Local manifests and sidecars for admitted hydrology source material.
- USGS Water Data site/time-series fixtures.
- WBD/HUC metadata fixtures.
- NHDPlus/3DHP reach metadata fixtures.
- NFHL regulatory-context fixtures.
- Water-quality parameter-code fixtures.
- Groundwater well metadata fixtures.
- Geometry, CRS, datum, and unit sidecars.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- unreviewed public-facing maps or tiles;
- official alert or warning text used as KFM-issued guidance;
- sensitive infrastructure details without policy review;
- private well owner details or precise private infrastructure where rights/sensitivity are unresolved;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- ingest preflight JSON report;
- source-shape report;
- unit/datum/time-basis report;
- source-role anti-collapse report;
- quarantine-reason report;
- proposed work record candidate;
- pipeline dry-run handoff summary;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A helper should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice hydrology ingest report should be compact and deterministic.

```json
{
  "tool": "hydrology-ingest-preflight",
  "status": "QUARANTINE_REVIEW_REQUIRED",
  "source_id": "usgs_water_data_placeholder",
  "input_kind": "time_series_manifest",
  "domain": "hydrology",
  "checks": {
    "source_descriptor_ref": "present",
    "source_role": "observed",
    "time_basis": "timestamped",
    "unit_basis": "present",
    "datum_or_crs": "present",
    "approval_state": "provisional",
    "nfhl_regulatory_context": "not_applicable",
    "schema_shape": "needs_review"
  },
  "decision": {
    "outcome": "QUARANTINE_REVIEW_REQUIRED",
    "reason_codes": ["PROVISIONAL_VALUES_PRESENT", "SCHEMA_SHAPE_NEEDS_REVIEW"],
    "blocking": true,
    "publication": false
  },
  "next_review": [
    "confirm source descriptor and rights posture",
    "preserve observed versus aggregate versus regulatory source role",
    "route through hydrology ingest pipeline if approved",
    "validate contracts and schemas",
    "do not publish without EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, and rollback path"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/hydrology/
├── README.md
├── test_hydrology_ingest_preflight.py
└── fixtures/
    ├── usgs_iv_valid/
    │   ├── input_manifest.json
    │   └── expected_report.json
    ├── provisional_values/
    │   ├── input_manifest.json
    │   └── expected_report.json
    ├── nfhl_regulatory_context/
    │   ├── input_manifest.json
    │   └── expected_report.json
    ├── missing_unit_or_time/
    │   ├── input_manifest.json
    │   └── expected_report.json
    └── source_role_collapse/
        ├── input_manifest.json
        └── expected_report.json
```

Recommended assertions:

- valid observed time-series fixture returns a reviewable candidate report, not public output;
- provisional values remain explicitly provisional;
- NFHL fixture is regulatory context and cannot pass as observed inundation;
- missing unit, datum, CRS, time, or parameter code yields `QUARANTINE_REVIEW_REQUIRED`, `ABSTAIN`, or `ERROR` with reason codes;
- modeled hydrograph fixture is not relabeled as observed;
- aggregate fixture is not relabeled as instantaneous observation;
- source descriptor reference is required;
- generated reports are deterministic;
- no test fixture contains sensitive private infrastructure or private well-owner details;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/hydrology
```

```bash
python tools/ingest/hydrology/hydrology_ingest_preflight.py \
  --input tests/ingest/hydrology/fixtures/usgs_iv_valid/input_manifest.json \
  --source-id usgs_water_data_placeholder \
  --output .tmp/hydrology-ingest-preflight-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `hydrology_ingest_preflight.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing hydrology ingest helper code, reviewers should confirm:

- [ ] The helper is preflight/report-only unless invoked by a governed workflow.
- [ ] The helper cannot publish or promote.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Observed, aggregate, modeled, regulatory, official-source, derived, and generated records remain distinct.
- [ ] NFHL and similar regulatory layers cannot be treated as observed flooding.
- [ ] Provisional and approved values remain distinct.
- [ ] Unit, parameter, datum/CRS, time basis, and source role are checked where applicable.
- [ ] Network access is off by default.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests use public-safe fixtures only.
- [ ] The helper does not write directly to `data/catalog/`, `data/triplets/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with governed hydrology ingest-tooling contract | **DONE in this README** | Establishes helper boundaries and anti-collapse posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve helper-vs-pipeline split | **NEEDS VERIFICATION** | Prevents duplication between `tools/ingest/hydrology/` and `pipelines/domains/hydrology/ingest/`. |
| Add `hydrology_ingest_preflight.py` dry-run helper | **PROPOSED** | Emits deterministic preflight report from local manifests. |
| Add public-safe fixtures | **PROPOSED** | Proves provisional, NFHL, missing-unit/time, and source-role-collapse behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hydrology contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces source-shape and anti-collapse issues without publication side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/hydrology/hydrology_ingest_preflight.py` with public-safe fixtures under `tests/ingest/hydrology/`. |
