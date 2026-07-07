<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-cdl-watch-readme
title: tools/ingest/cdl_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-agriculture-source-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public
owning_root: tools/
responsibility: proposed CDL watcher helper boundary for detecting review-worthy USDA NASS Cropland Data Layer changes
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/usda/usda-nass-cdl.md
  - ../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../connectors/nass/README.md
  - ../../../connectors/usda-nass/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README defines a proposed CDL watcher tooling boundary, not a confirmed implementation."
  - "The watcher may detect material changes and emit review signals; it must not publish, promote, or mutate source-role truth."
  - "CDL product doctrine lives in docs/sources/catalog/usda/usda-nass-cdl.md; source activation lives in data/registry/sources/."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/cdl_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-CDL--watcher-informational)
![source](https://img.shields.io/badge/source-USDA%20NASS%20CDL-blueviolet)
![publication](https://img.shields.io/badge/publication-never--from--watcher-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/cdl_watch/` is the proposed tooling lane for detecting review-worthy changes in USDA NASS Cropland Data Layer inputs and emitting governed watcher reports. It is not a connector, not a downloader of record, not a publication path, and not an authority for crop truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [CDL watcher posture](#cdl-watcher-posture)
- [Material-change model](#material-change-model)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/cdl_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** CDL change detector.

The intended watcher is conservative. It may inspect allowed metadata, local sidecars, prior run records, or already-admitted CDL snapshots to decide whether a review-worthy change should be surfaced. It does not admit source data by itself, and it does not replace USDA NASS connector behavior, source descriptors, policy checks, catalog closure, or release review.

The durable KFM question for this lane is:

> Did the CDL source surface or county-level class distribution change enough to propose governed work?

The answer should be a review signal, not a publication decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/cdl_watch/README.md` | **CONFIRMED** | This README defines the lane boundary. |
| `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in current check** | Parent lane README should be added before expanding ingest tooling broadly. |
| CDL watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| CDL watcher cadence | **PROPOSED** | Product docs describe weekly HEAD and histogram-drift ideas; operational cadence requires steward approval. |
| CDL materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must be fixture-tested and reviewed before becoming CI or workflow gates. |
| CDL source descriptor | **OUTSIDE THIS FOLDER** | Source activation belongs in `data/registry/sources/`. |
| CDL connector | **OUTSIDE THIS FOLDER** | Source admission belongs in `connectors/nass/` or the ratified NASS connector home. |
| Publication authority | **DENY here** | Watchers do not publish. |

> [!IMPORTANT]
> This folder is a watcher/tooling lane. It must not become a parallel NASS connector, a source registry, a CDL product doctrine page, a crop-truth layer, a policy engine, a catalog authority, a receipt/proof store, or a release pathway.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for validators, generators, builders, QA helpers, release helpers, and other durable executable support.

`tools/ingest/cdl_watch/` is narrower than a connector and should remain a helper lane until the repository has a documented parent `tools/ingest/` contract or an accepted ADR clarifying long-lived ingest tooling placement.

Safe interpretation for now:

- **CONFIRMED:** this README exists at `tools/ingest/cdl_watch/README.md`.
- **PROPOSED:** CDL watcher code may live here if it is deterministic, bounded, and review-signal-only.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **DENY:** any use of this path as a connector, raw-data sink, publication path, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A CDL watcher may observe metadata or compare allowed local artifacts, but it does not move data across lifecycle phases.

Required boundary rules:

1. **Watcher output is not publication.** It can propose work, not release a layer.
2. **Connector output remains separate.** Connectors admit source material into `data/raw/` or `data/quarantine/` only.
3. **Processed artifacts remain separate.** Normalization and transformation belong to the governed pipeline and data lifecycle.
4. **Catalog closure remains separate.** STAC, DCAT, PROV, domain catalog records, receipts, proofs, and release manifests are not owned by this folder.
5. **CDL crop classifications remain source-role-bound.** Native CDL classification should be preserved; crosswalks are derived and advisory unless separately reviewed.
6. **AI and UI remain downstream.** No Focus Mode or map surface may treat watcher output as source truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/cdl_watch/` include:

- CDL metadata watcher helpers.
- CDL sidecar comparison helpers.
- County histogram drift detectors for already-admitted or fixture CDL artifacts.
- CDL classmap-version drift checks.
- CDL county-geometry hash checks.
- Proposed-work-record emitters.
- Watcher run report generators.
- Dry-run CLI wrappers for local review.
- Public-safe fixtures and expected-output builders only when stored through the test fixture convention.

A helper belongs here only when it is:

- deterministic;
- network-free by default or explicit about read-only network checks;
- bounded to watcher/reporting behavior;
- explicit about source descriptor references;
- conservative about material-change thresholds;
- unable to publish or promote;
- tested with public-safe fixtures;
- explicit about its output envelope and finite outcomes.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/cdl_watch/` | Correct home | Reason |
|---|---|---|
| CDL product doctrine | `docs/sources/catalog/usda/usda-nass-cdl.md` | Product documentation is not executable tooling. |
| SourceDescriptor records | `data/registry/sources/` | Source activation and role metadata belong in the registry. |
| NASS/CDL connector code of record | `connectors/nass/` or ratified connector home | Connectors own source admission. |
| Raw CDL downloads | `data/raw/...` or `data/quarantine/...` | Data lifecycle roots own source material. |
| Processed rasters or tables | `data/processed/...` | Transformation outputs are not tool code. |
| Catalog records | `data/catalog/...` | Catalog closure has its own root. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Policy rules | `policy/` | Watcher code does not own policy meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Tests | `tests/ingest/cdl_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |
| Sensitive real examples | nowhere public | Fixtures must be public-safe and synthetic or generalized. |

[Back to top](#top)

---

## CDL watcher posture

The CDL watcher should be understood as a **control-plane signaler**.

It may create:

- a watcher run report;
- a proposed work record;
- a material-change summary;
- a classmap drift warning;
- a geometry-hash drift warning;
- a reviewer handoff file.

It must not create:

- a public CDL layer;
- a promoted release;
- an EvidenceBundle;
- a policy decision;
- a source descriptor correction;
- a crop-truth claim;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should say what changed, why it may matter, what evidence or metadata was inspected, and what validation/review must happen next. It should not say the change is approved.

[Back to top](#top)

---

## Material-change model

The CDL catalog page describes a proposed watcher family with metadata checks, sidecar records, county histogram drift, classmap drift, and county geometry hash checks. This README keeps those ideas bounded as proposed implementation guidance.

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed `etag`, `last_modified`, `content_length`, digest, or declared release metadata. | **PROPOSED** |
| CDL year drift | Detect a new CDL year candidate. | **PROPOSED** |
| Classmap version drift | Fail closed when class IDs or meanings change. | **PROPOSED** |
| County histogram drift | Compare county-bounded class distributions across releases. | **PROPOSED** |
| County geometry hash drift | Avoid false crop-change signals caused by changed county geometry. | **PROPOSED** |
| Threshold report | Explain why a change did or did not propose work. | **PROPOSED** |

Thresholds should be configured, documented, and fixture-tested. Do not hard-code final materiality rules without review.

Recommended first finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `STALE_INPUT` | Input metadata or sidecar is older than the configured acceptable window. |
| `CLASSMAP_DRIFT` | CDL class semantics changed or could not be resolved safely. |
| `GEOMETRY_DRIFT` | County geometry hash changed and crop drift cannot be interpreted directly. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- CDL source descriptor reference, not duplicated descriptor fields.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Local metadata fixture for a CDL release candidate.
- County-bound class histogram fixture.
- CDL classmap version fixture.
- County geometry hash fixture.
- Public-safe test data.

### Unsuitable inputs

- credentials or secrets;
- unrestricted raw source dumps outside lifecycle control;
- unpublished or unreviewed source material passed directly to public outputs;
- parcel-, field-, farm-, person-, or owner-level claims derived from CDL alone;
- real sensitive private data;
- exact restricted archaeology, rare-species, or infrastructure-risk coordinates.

### Suitable outputs

- watcher JSON report;
- proposed work record candidate;
- material-change summary;
- classmap drift report;
- geometry drift report;
- CI/reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice watcher report should be compact and deterministic.

```json
{
  "tool": "cdl-watch",
  "status": "PROPOSED_WORK_RECORD",
  "source_id": "usda-nass-cdl",
  "cdl_year": 2026,
  "county_fips": "20115",
  "inputs": {
    "prior_sidecar": "tests/ingest/cdl_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/cdl_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "metadata_drift": "changed",
    "classmap_drift": "same",
    "county_geometry_hash": "same",
    "histogram_drift": "material"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["CDL_HISTOGRAM_DRIFT_THRESHOLD_EXCEEDED"],
    "blocking": false
  },
  "next_review": [
    "confirm source descriptor",
    "run CDL connector/admission workflow if approved",
    "validate rights and source terms",
    "route through catalog and release gates before public use"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/cdl_watch/
├── README.md
├── test_cdl_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── classmap_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── geometry_drift/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same metadata and histograms return `NO_MATERIAL_CHANGE`;
- changed histograms beyond configured threshold return `PROPOSED_WORK_RECORD`;
- classmap semantic drift returns `CLASSMAP_DRIFT` and fails closed;
- county geometry hash drift returns `GEOMETRY_DRIFT` or `ABSTAIN` rather than crop-change certainty;
- missing sidecars return `ERROR` or `ABSTAIN` with clear reason codes;
- generated reports are deterministic;
- no test fixture contains real sensitive or private data;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/cdl_watch
```

```bash
python tools/ingest/cdl_watch/cdl_watch.py \
  --prior tests/ingest/cdl_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/cdl_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/cdl-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `cdl_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing CDL watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Network access is off by default or explicitly read-only and documented.
- [ ] Materiality thresholds are configured and fixture-tested.
- [ ] Classmap drift fails closed.
- [ ] County geometry drift does not masquerade as crop change.
- [ ] Native CDL classification is preserved.
- [ ] Crosswalk outputs are labelled derived/advisory.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests cover no-change, material-change, classmap-drift, geometry-drift, missing-input, and malformed-input cases.
- [ ] The helper does not write directly to `data/catalog/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with watcher lane contract | **DONE in this README** | Establishes CDL watcher boundaries and non-publication rule. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Add `cdl_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe watcher fixtures | **PROPOSED** | Proves no-change, material-change, classmap-drift, and geometry-drift behavior. |
| Add proposed-work-record schema alignment | **PROPOSED / NEEDS VERIFICATION** | Align report envelope with accepted contracts/schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces CDL drift without publication side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/cdl_watch/cdl_watch.py` with public-safe fixtures under `tests/ingest/cdl_watch/`. |
