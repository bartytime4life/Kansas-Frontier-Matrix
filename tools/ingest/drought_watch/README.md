<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-drought-watch-readme
title: tools/ingest/drought_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-drought-hazards-source-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public
owning_root: tools/
responsibility: proposed U.S. Drought Monitor watcher helper boundary for detecting review-worthy weekly drought-classification changes
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/drought_monitor/README.md
  - ../../../docs/sources/catalog/drought_monitor/drought-monitor.md
  - ../../../connectors/drought-monitor/README.md
  - ../../../pipeline_specs/hazards/drought_monitor.yaml
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hydrology/SOURCES.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README defines a proposed drought watcher tooling boundary, not a confirmed implementation."
  - "The watcher may detect USDM material changes and emit review signals; it must not publish, promote, issue emergency alerts, or mutate source-role truth."
  - "USDM product doctrine lives in docs/sources/catalog/drought_monitor/drought-monitor.md; connector intake lives in connectors/drought-monitor/; source activation lives in data/registry/sources/."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/drought_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-drought--watcher-informational)
![source](https://img.shields.io/badge/source-U.S.%20Drought%20Monitor-blueviolet)
![alerts](https://img.shields.io/badge/emergency--alerts-denied-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/drought_watch/` is the proposed tooling lane for detecting review-worthy changes in U.S. Drought Monitor (USDM) source surfaces and emitting governed watcher reports. It is not a connector, not an emergency-alerting system, not a public map layer, not a publication path, and not drought truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Drought watcher posture](#drought-watcher-posture)
- [Material-change model](#material-change-model)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/drought_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** U.S. Drought Monitor change detector.

The watcher is a control-plane signaler. It may compare approved local metadata, sidecars, release-week references, classification summaries, geometry fingerprints, or no-network fixtures to decide whether drought-source material should be reviewed.

The durable KFM question for this lane is:

> Did the USDM source surface, release week, geometry, classification distribution, or provenance metadata change enough to propose governed work?

The answer should be a review signal. It should never be a publication decision, emergency alert, policy decision, drought-impact claim, or domain-truth claim.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/drought_watch/README.md` | **CONFIRMED** | This README defines the watcher tooling boundary. |
| `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in current check** | Parent lane README should be added before expanding ingest tooling broadly. |
| Drought watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| USDM product page | **CONFIRMED in repo evidence** | `docs/sources/catalog/drought_monitor/drought-monitor.md` documents USDM product posture. |
| USDM connector lane | **CONFIRMED in repo evidence / draft** | `connectors/drought-monitor/README.md` documents source-admission-only boundary. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Operational cadence must be steward-approved and fixture-tested. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must not become release gates without review. |
| SourceDescriptor activation | **OUTSIDE THIS FOLDER** | Activation belongs in `data/registry/sources/`. |
| Publication authority | **DENY here** | Watchers do not publish. |
| Emergency alerting | **DENY here** | KFM drought watcher output is not public emergency guidance. |

> [!IMPORTANT]
> This folder is a watcher/reporting lane. It must not become a parallel USDM connector, a source registry, a hazards doctrine page, a drought-truth model, an emergency-alert system, a policy engine, a catalog authority, a receipt/proof store, or a release pathway.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific intake and admission code. `data/registry/sources/` owns source activation and descriptor truth. `docs/sources/catalog/` owns source-family and product documentation. `release/` owns release decisions.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/drought_watch/README.md`.
- **PROPOSED:** USDM watcher code may live here if it is deterministic, bounded, review-signal-only, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **DENY:** any use of this path as a connector, raw-data sink, public alerting surface, publication path, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A drought watcher may observe approved metadata or compare local artifacts, but it does not move data across lifecycle phases.

Required boundary rules:

1. **Watcher output is not publication.** It can propose work, not release a layer.
2. **Watcher output is not emergency guidance.** It must not issue public alerts or operational warnings.
3. **Connector output remains separate.** The USDM connector may write only to `data/raw/` or `data/quarantine/` according to its own boundary.
4. **Processed artifacts remain separate.** Drought normalization, domain projection, classification transforms, and threshold updates belong to downstream governed workflows.
5. **Catalog closure remains separate.** STAC, DCAT, PROV, domain catalog records, receipts, proofs, and release manifests are not owned by this folder.
6. **Native USDM classes remain source-bound.** Any derived hydrology, agriculture, hazard, or habitat indicator must cite the source class and its transformation lineage.
7. **AI and UI remain downstream.** No Focus Mode, Story Node, dashboard, or map surface may treat watcher output as source truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/drought_watch/` include:

- USDM metadata watcher helpers.
- Release-week sidecar comparison helpers.
- Drought-class distribution drift detectors for already-admitted or fixture USDM artifacts.
- Polygon/geometry fingerprint drift checks.
- Native class-set drift checks.
- Proposed-work-record emitters.
- Watcher run report generators.
- Dry-run CLI wrappers for local review.
- No-network fixture adapters for tests.
- Reviewer handoff summaries that explain what should be checked next.

A helper belongs here only when it is:

- deterministic;
- network-free by default or explicit about read-only network checks;
- bounded to watcher/reporting behavior;
- explicit about source descriptor references;
- conservative about material-change thresholds;
- unable to publish, promote, alert, or mutate lifecycle records;
- tested with public-safe fixtures;
- explicit about its output envelope and finite outcomes.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/drought_watch/` | Correct home | Reason |
|---|---|---|
| USDM product doctrine | `docs/sources/catalog/drought_monitor/drought-monitor.md` | Product documentation is not executable tooling. |
| SourceDescriptor records | `data/registry/sources/` | Source activation and source-role truth belong in the registry. |
| USDM connector code of record | `connectors/drought-monitor/` | Connectors own source admission. |
| Raw USDM downloads | `data/raw/...` or `data/quarantine/...` | Data lifecycle roots own source material. |
| Processed drought layers | `data/processed/...` | Transformation outputs are not tool code. |
| Catalog records | `data/catalog/...` | Catalog closure has its own root. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Emergency alerts or public warnings | outside this repo unless separately governed | This watcher is not an alerting system. |
| Policy rules | `policy/` | Watcher code does not own policy meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Tests | `tests/ingest/drought_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |
| Sensitive real examples | nowhere public | Fixtures must be public-safe and synthetic or generalized. |

[Back to top](#top)

---

## Drought watcher posture

The drought watcher should be understood as a **review signaler** for USDM-related change.

It may create:

- a watcher run report;
- a proposed work record;
- a release-week drift summary;
- a geometry drift warning;
- a class-distribution drift warning;
- a source metadata drift warning;
- a reviewer handoff file.

It must not create:

- a public drought layer;
- a promoted release;
- an EvidenceBundle;
- a policy decision;
- a source descriptor correction;
- a drought-impact claim;
- a drought emergency alert;
- a hydrology/agriculture/hazards threshold update by itself;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, why it may matter, what evidence or metadata was inspected, and what validation or steward review must happen next. It should not say the change is approved.

[Back to top](#top)

---

## Material-change model

The USDM product page describes a weekly drought-classification product that can inform agriculture, hydrology, hazards, and habitat contexts. This README keeps watcher behavior bounded as proposed implementation guidance.

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed endpoint metadata, content length, digest, `etag`, `last_modified`, or declared release metadata. | **PROPOSED** |
| Release-week drift | Detect a new or missing USDM release week. | **PROPOSED** |
| Native class-set drift | Confirm expected USDM class vocabulary before downstream interpretation. | **PROPOSED** |
| Geometry fingerprint drift | Detect polygon/topology change without making impact claims. | **PROPOSED** |
| County or HUC summary drift | Compare generalized drought-class area summaries where configured. | **PROPOSED** |
| Threshold review signal | Explain whether downstream threshold-review workflows should be considered. | **PROPOSED** |
| Staleness check | Surface stale or missing expected releases. | **PROPOSED** |

Thresholds should be configured, documented, and fixture-tested. Do not hard-code final materiality rules without review.

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `NEW_RELEASE_CANDIDATE` | A new USDM release week appears to be available. |
| `STALE_INPUT` | Expected release metadata or sidecar is older than the configured window. |
| `CLASS_SET_DRIFT` | Native class vocabulary or mapping could not be resolved safely. |
| `GEOMETRY_DRIFT` | Geometry fingerprint changed and downstream summary interpretation needs review. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- USDM source descriptor reference, not duplicated descriptor fields.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Local metadata fixture for a USDM release candidate.
- Release-week summary fixture.
- Drought-class distribution fixture.
- Geometry fingerprint fixture.
- Public-safe test data.

### Unsuitable inputs

- credentials or secrets;
- unrestricted raw source dumps outside lifecycle control;
- unpublished source material passed directly to public outputs;
- parcel-, field-, farm-, person-, or owner-level claims derived from drought classes alone;
- real sensitive private data;
- exact restricted archaeology, rare-species, or infrastructure-risk coordinates;
- public emergency alert templates.

### Suitable outputs

- watcher JSON report;
- proposed work record candidate;
- release-week change summary;
- geometry drift report;
- class-set drift report;
- stale-input report;
- CI/reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice watcher report should be compact and deterministic.

```json
{
  "tool": "drought-watch",
  "status": "PROPOSED_WORK_RECORD",
  "source_id": "drought_monitor",
  "release_week": "2026-W27",
  "geography_scope": "state:kansas",
  "inputs": {
    "prior_sidecar": "tests/ingest/drought_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/drought_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "metadata_drift": "changed",
    "release_week": "new_candidate",
    "class_set_drift": "same",
    "geometry_fingerprint": "same",
    "summary_drift": "material"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["USDM_RELEASE_WEEK_CHANGED", "USDM_SUMMARY_DRIFT_THRESHOLD_EXCEEDED"],
    "blocking": false,
    "emergency_alert": false
  },
  "next_review": [
    "confirm source descriptor and connector placement",
    "run USDM connector/admission workflow if approved",
    "validate rights and attribution requirements",
    "route through catalog and release gates before public use",
    "abstain from public impact claims until EvidenceBundle and PolicyDecision exist"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/drought_watch/
├── README.md
├── test_drought_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── new_release_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── material_summary_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── class_set_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── geometry_drift/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same metadata and summaries return `NO_MATERIAL_CHANGE`;
- a new release week returns `NEW_RELEASE_CANDIDATE` or `PROPOSED_WORK_RECORD` according to configured rules;
- summary drift beyond configured threshold returns `PROPOSED_WORK_RECORD`;
- class-set drift returns `CLASS_SET_DRIFT` and fails closed;
- geometry fingerprint drift returns `GEOMETRY_DRIFT` or `ABSTAIN` rather than drought-impact certainty;
- missing sidecars return `ERROR` or `ABSTAIN` with clear reason codes;
- generated reports are deterministic;
- no test fixture contains real sensitive or private data;
- no helper writes to lifecycle or release roots without explicit workflow control;
- no helper emits emergency-alert language.

Suggested future command pattern:

```bash
pytest -q tests/ingest/drought_watch
```

```bash
python tools/ingest/drought_watch/drought_watch.py \
  --prior tests/ingest/drought_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/drought_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/drought-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `drought_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing drought watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot issue emergency alerts or public warnings.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Network access is off by default or explicitly read-only and documented.
- [ ] Materiality thresholds are configured and fixture-tested.
- [ ] Native USDM class vocabulary is preserved.
- [ ] Geometry drift does not masquerade as drought-impact certainty.
- [ ] Cross-domain threshold update signals are review requests, not automatic updates.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests cover no-change, new-release, material-summary-change, class-set-drift, geometry-drift, missing-input, and malformed-input cases.
- [ ] The helper does not write directly to `data/catalog/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with watcher lane contract | **DONE in this README** | Establishes USDM watcher boundaries and non-publication/non-alert rule. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Add `drought_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe watcher fixtures | **PROPOSED** | Proves no-change, new-release, summary-drift, class-set-drift, and geometry-drift behavior. |
| Align proposed-work-record schema | **PROPOSED / NEEDS VERIFICATION** | Match accepted contracts/schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces USDM drift without publication, alerting, or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/drought_watch/drought_watch.py` with public-safe fixtures under `tests/ingest/drought_watch/`. |
