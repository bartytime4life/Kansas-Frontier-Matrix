<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-nfhl-watch-readme
title: tools/ingest/nfhl_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-hazards-source-stewards
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context-only; watcher-only; no-publication; not-for-life-safety
owning_root: tools/
responsibility: proposed FEMA NFHL watcher helper boundary for regulatory flood-hazard source-change review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../docs/sources/catalog/fema/map-service-center.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../contracts/domains/hydrology/nfhl_zone.md
  - ../../../connectors/fema/nfhl/README.md
  - ../../../connectors/fema-nfhl/README.md
  - ../../../pipelines/domains/hydrology/ingest_nfhl/README.md
  - ../../../tools/ingest/hydrology_watch/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/hydrology/fema_nfhl/README.md
  - ../../../data/raw/hazards/nfhl/README.md
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README defines a proposed NFHL watcher tooling boundary, not a confirmed implementation."
  - "NFHL is regulatory flood-hazard context, not observed inundation, forecast, warning, insurance determination, engineering determination, legal advice, or life-safety guidance."
  - "The watcher may detect NFHL material changes and emit review signals; it must not publish, promote, decide regulatory meaning, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/nfhl_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-NFHL--watcher-informational)
![source](https://img.shields.io/badge/source-FEMA%20NFHL-blueviolet)
![anti-collapse](https://img.shields.io/badge/NFHL-%E2%89%A0-observed--inundation-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/nfhl_watch/` is the proposed tooling lane for detecting review-worthy FEMA National Flood Hazard Layer source changes and emitting governed watcher reports. It is not a connector, not NFHL ingest normalization, not regulatory interpretation, not observed-flood evidence, not a public map layer, not a publication path, and not flood truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [NFHL watcher posture](#nfhl-watcher-posture)
- [Material-change model](#material-change-model)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/nfhl_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** FEMA NFHL regulatory-source change detector.

The watcher may compare approved local metadata, service sidecars, package inventories, feature-class lists, version markers, panel identifiers, effective-date summaries, LOMR/LOMA lineage hints, geometry fingerprints, or no-network fixtures to decide whether NFHL material should be reviewed.

The durable KFM question for this lane is:

> Did the FEMA NFHL regulatory source surface change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, raw capture of record, public layer, observed flood extent, forecast, warning, insurance determination, engineering determination, legal interpretation, processed truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/nfhl_watch/README.md` | **CONFIRMED** | This README defines the NFHL watcher tooling boundary. |
| NFHL watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| NFHL product page | **CONFIRMED in repo evidence** | Product docs state NFHL is regulatory context, not observed inundation. |
| FEMA NFHL connector lanes | **CONFIRMED in repo evidence / canonicality NEEDS VERIFICATION** | Both nested and split connector paths exist and need reconciliation. |
| NFHL ingest pipeline lane | **CONFIRMED in repo evidence / draft** | Pipeline lane owns executable NFHL normalization after source admission. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | NFHL changes may be localized and event-driven; cadence must be source-specific and reviewed. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must be fixture-tested before becoming workflow signals. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |
| Observed-inundation claim | **DENY here** | NFHL does not become observed flooding. |
| Insurance, engineering, or legal determination | **DENY here** | Watcher output cannot decide downstream determinations. |

> [!IMPORTANT]
> A change in NFHL means the regulatory source surface may need review. It does not mean a location is currently flooded, safe, unsafe, insured, uninsured, compliant, non-compliant, or eligible for anything.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific fetch and admission code. `pipelines/domains/hydrology/ingest_nfhl/` owns NFHL ingest normalization if that pipeline remains the accepted lane. `docs/sources/catalog/fema/` owns FEMA source product documentation. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility. Lifecycle data, receipts, proofs, catalog records, and release decisions live outside this tooling lane.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/nfhl_watch/README.md`.
- **PROPOSED:** NFHL watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether the canonical NFHL connector is `connectors/fema/nfhl/`, `connectors/fema-nfhl/`, or a compatibility split.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, catalog/proof/release authority, public API, map layer, observed-event surface, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A NFHL watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not NFHL normalization.** Pipeline lanes own normalization, transform receipts, validation, and quarantine handoff.
4. **Watcher output is not catalog closure.** STAC, DCAT, PROV, domain catalog records, triplets, receipts, proofs, and release manifests are outside this folder.
5. **NFHL remains regulatory context.** Regulatory flood-hazard context must not be relabeled as observed flooding.
6. **NFHL and MSC remain companions.** NFHL vector surfaces and MSC panel/FIS records need separate source identity and lineage discipline.
7. **Verbatim regulatory attributes matter.** `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone designation, BFE/datum fields, and LOMR/LOMA references should be preserved for downstream review.
8. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/nfhl_watch/` include:

- NFHL service metadata watcher helpers;
- NFHL sidecar comparison helpers;
- feature-class inventory drift checks;
- `DFIRM_ID`, `VERSION_ID`, and `EFFECTIVE_DATE` summary drift checks;
- flood-zone vocabulary drift checks;
- LOMR/LOMA lineage hint drift checks;
- BFE and vertical-datum field presence checks;
- FEMA service layer / REST endpoint fingerprint checks;
- WMS-vs-vector access-surface guard checks;
- localized panel/version change summaries;
- geometry fingerprint and CRS/datum sidecar checks;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or promote, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/nfhl_watch/` | Correct home | Reason |
|---|---|---|
| NFHL source fetchers or API clients of record | `connectors/fema/nfhl/` or the ratified NFHL connector home | Connectors own source acquisition and admission. |
| NFHL ingest pipeline logic | `pipelines/domains/hydrology/ingest_nfhl/` or accepted pipeline home | Pipelines own executable lifecycle normalization. |
| NFHL product doctrine | `docs/sources/catalog/fema/nfhl-flood-hazard.md` | Product documentation is not watcher code. |
| MSC product doctrine | `docs/sources/catalog/fema/map-service-center.md` | MSC is companion source documentation. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, and cadence belong in the registry. |
| Raw NFHL captures | `data/raw/hydrology/...`, `data/raw/hazards/...`, or ratified raw home | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/...` | Holds are lifecycle artifacts, not tool code. |
| Processed NFHLZone records | `data/processed/...` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Legal, insurance, engineering, or safety guidance | governed external/official channels or separate reviewed docs | This watcher cannot make determinations. |
| Policy rules | `policy/` | Watchers do not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/nfhl_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## NFHL watcher posture

The NFHL watcher should be understood as a **review signaler** for regulatory source change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- a source staleness report;
- a feature-class inventory drift report;
- a panel/version/effective-date drift report;
- a zone-vocabulary drift report;
- a BFE/datum field-presence warning;
- a geometry/version drift report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed `NFHLZone` object of record;
- a public flood layer;
- an observed flood event;
- a forecast or warning;
- an insurance determination;
- a legal or engineering determination;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what regulatory source-role boundary is relevant, what evidence or metadata was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved, public, or determinative.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, service metadata, endpoint path, or source version metadata. | **PROPOSED** |
| Expected cadence / staleness | Surface stale or missing expected service/package sidecars. | **PROPOSED** |
| SourceDescriptor drift | Detect changed source role, rights, activation, cadence, or canonical connector reference. | **PROPOSED** |
| Feature-class inventory drift | Detect changed FEMA layer/table inventory or expected feature classes. | **PROPOSED** |
| Regulatory attribute drift | Detect missing or changed `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone, BFE/datum, study, or revision fields. | **PROPOSED** |
| Panel/version drift | Detect localized panel/version/effective-date changes requiring review. | **PROPOSED** |
| Zone vocabulary drift | Detect unexpected flood-zone values without recoding them as new truth. | **PROPOSED** |
| Access-surface drift | Detect vector REST vs WMS ambiguity and fail closed for analytic use. | **PROPOSED** |
| Geometry/version drift | Detect changed geometry fingerprint, CRS, datum, or package version metadata. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | NFHL source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_NFHL_SOURCE_WINDOW` | A new NFHL service/package state appears available for steward review. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `FEATURE_CLASS_DRIFT` | FEMA layer/table inventory changed. |
| `REGULATORY_ATTRIBUTE_DRIFT` | Required regulatory attributes changed or are missing. |
| `PANEL_VERSION_DRIFT` | Panel/version/effective-date lineage changed. |
| `ZONE_VOCABULARY_DRIFT` | Zone vocabulary changed or could not be resolved safely. |
| `ACCESS_SURFACE_AMBIGUOUS` | Vector/WMS surface role cannot be preserved safely; fail closed. |
| `GEOMETRY_OR_VERSION_DRIFT` | Geometry, CRS, datum, or package version changed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- NFHL SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Local metadata fixtures for NFHL source windows.
- FEMA feature-service metadata fixtures.
- Feature-class inventory fixtures.
- Panel/version/effective-date summary fixtures.
- Zone vocabulary fixtures.
- BFE/datum field fixtures.
- LOMR/LOMA lineage hint fixtures.
- Geometry, CRS, and datum sidecars.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- unreviewed public-facing maps or tiles;
- WMS screenshots used as analytic truth;
- observed flood-event feeds treated as NFHL regulatory context;
- legal, insurance, engineering, or safety-decision text treated as KFM-issued guidance;
- sensitive infrastructure details without policy review;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- staleness report;
- source descriptor drift report;
- feature-class inventory drift report;
- regulatory attribute drift report;
- panel/version/effective-date drift report;
- access-surface ambiguity report;
- geometry/version drift report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice NFHL watcher report should be compact and deterministic.

```json
{
  "tool": "nfhl-watch",
  "status": "PANEL_VERSION_DRIFT",
  "source_id": "fema_nfhl_placeholder",
  "source_role": "regulatory",
  "inputs": {
    "prior_sidecar": "tests/ingest/nfhl_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/nfhl_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "feature_class_inventory": "same",
    "required_regulatory_attributes": "present",
    "panel_version_drift": "changed",
    "zone_vocabulary_drift": "none",
    "access_surface": "vector_rest",
    "geometry_or_version_drift": "changed"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["PANEL_VERSION_DRIFT", "GEOMETRY_OR_VERSION_DRIFT"],
    "blocking": false,
    "publication": false,
    "observed_inundation_claim": false,
    "determination": false
  },
  "next_review": [
    "confirm NFHL source descriptor and rights posture",
    "confirm canonical connector placement",
    "preserve regulatory source role",
    "run NFHL connector/admission workflow if approved",
    "route through NFHL ingest pipeline after admission",
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
tests/ingest/nfhl_watch/
├── README.md
├── test_nfhl_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── source_metadata_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── panel_version_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── regulatory_attribute_missing/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── access_surface_ambiguous/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── zone_vocabulary_drift/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- changed metadata returns `SOURCE_METADATA_DRIFT` or `PROPOSED_WORK_RECORD` according to configured rules;
- panel/version/effective-date changes return `PANEL_VERSION_DRIFT`;
- missing `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone, or datum-related fields return `REGULATORY_ATTRIBUTE_DRIFT` or `ABSTAIN`;
- WMS-only or ambiguous access surface returns `ACCESS_SURFACE_AMBIGUOUS` for analytic use;
- zone vocabulary changes are reported without recoding or interpretation;
- no fixture allows NFHL to pass as observed inundation;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/nfhl_watch
```

```bash
python tools/ingest/nfhl_watch/nfhl_watch.py \
  --prior tests/ingest/nfhl_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/nfhl_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/nfhl-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `nfhl_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing NFHL watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] NFHL is preserved as regulatory context only.
- [ ] NFHL cannot be treated as observed inundation, forecast, warning, or current condition.
- [ ] NFHL and MSC companion-source roles remain separate.
- [ ] `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone, BFE/datum, and revision lineage fields are preserved for review.
- [ ] Vector REST and WMS access surfaces are not collapsed.
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
| Replace empty README with governed NFHL watcher contract | **DONE in this README** | Establishes watcher boundaries and regulatory anti-collapse posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve NFHL connector canonicality | **NEEDS VERIFICATION / ADR-class** | Prevents duplicate connector authority between nested and split paths. |
| Add `nfhl_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, metadata drift, panel-version drift, missing attributes, access-surface ambiguity, and zone-vocabulary behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted NFHL/Hydrology/Hazards contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces NFHL source-change issues without publication or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/nfhl_watch/nfhl_watch.py` with public-safe fixtures under `tests/ingest/nfhl_watch/`. |
