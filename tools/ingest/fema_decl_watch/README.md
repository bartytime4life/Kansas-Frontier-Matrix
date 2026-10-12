<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-fema-decl-watch-readme
title: tools/ingest/fema_decl_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-source-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context-administrative; not-for-life-safety
owning_root: tools/
responsibility: proposed OpenFEMA disaster declaration watcher helper boundary for detecting review-worthy administrative declaration changes
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/fema/README.md
  - ../../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../../connectors/fema/README.md
  - ../../../connectors/fema-openfema/README.md
  - ../../../data/registry/hazards/sources/fema_disaster_declarations.yaml
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README defines a proposed FEMA disaster declaration watcher tooling boundary, not a confirmed implementation."
  - "A FEMA Disaster Declaration is an administrative federal action, not an observed hazard event, forecast, warning, damage assessment, or eligibility determination."
  - "The watcher may detect OpenFEMA declaration changes and emit review signals; it must not publish, promote, issue alerts, decide benefits, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/fema_decl_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-FEMA--declaration--watcher-informational)
![source](https://img.shields.io/badge/source-OpenFEMA%20Disaster%20Declarations-blueviolet)
![life--safety](https://img.shields.io/badge/life--safety-not--guidance-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/fema_decl_watch/` is the proposed tooling lane for detecting review-worthy changes in OpenFEMA Disaster Declaration records and emitting governed watcher reports. It is not a connector, not an observed-hazard detector, not an emergency-alerting system, not a benefits or eligibility tool, not a publication path, and not disaster truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Disaster declaration watcher posture](#disaster-declaration-watcher-posture)
- [Material-change model](#material-change-model)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/fema_decl_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** OpenFEMA Disaster Declarations change detector.

The watcher is a control-plane signaler. It may compare approved local metadata, sidecars, declaration identifiers, incident-period fields, designated-area summaries, source digests, or no-network fixtures to decide whether OpenFEMA declaration material should be reviewed.

The durable KFM question for this lane is:

> Did OpenFEMA Disaster Declaration administrative records change enough to propose governed work?

The answer should be a review signal. It should never be a publication decision, emergency alert, observed hazard-event claim, damage assessment, eligibility determination, aid guidance, or source-role correction.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/fema_decl_watch/README.md` | **CONFIRMED** | This README defines the watcher tooling boundary. |
| `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| FEMA declaration watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| OpenFEMA Disaster Declarations product page | **CONFIRMED in repo evidence** | Product page documents the administrative source-role distinction. |
| FEMA connector family lane | **CONFIRMED in repo evidence / draft** | `connectors/fema/` documents source-admission-only boundaries. |
| OpenFEMA connector lane | **CONFIRMED in repo evidence / draft / canonicality NEEDS VERIFICATION** | `connectors/fema-openfema/` exists but its canonical relation to `connectors/fema/` needs governance resolution. |
| Source registry stub | **CONFIRMED as PROPOSED template** | `data/registry/hazards/sources/fema_disaster_declarations.yaml` exists with TBD fields. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Operational cadence must be steward-approved and fixture-tested. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must not become release gates without review. |
| Publication authority | **DENY here** | Watchers do not publish. |
| Emergency alerting / life safety | **DENY here** | Watcher output is not public emergency guidance. |
| Benefit eligibility or insurance decision | **DENY here** | FEMA declaration records must not be used here for individual determinations. |

> [!IMPORTANT]
> A Disaster Declaration is an administrative record of federal action. It is not observed flooding, observed wildfire perimeter, observed tornado track, verified damage, a forecast, an emergency warning, or proof that aid applies to a specific person or property.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `connectors/` owns source-specific intake and admission code. `data/registry/sources/` and related source-registry lanes own source activation and descriptor truth. `docs/sources/catalog/` owns source-family and product documentation. `release/` owns release decisions.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/fema_decl_watch/README.md`.
- **PROPOSED:** FEMA declaration watcher code may live here if it is deterministic, bounded, review-signal-only, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether OpenFEMA connector implementation should be canonicalized under `connectors/fema/`, `connectors/fema-openfema/`, or another ratified layout.
- **DENY:** any use of this path as a connector, raw-data sink, public alerting surface, observed-event detector, publication path, policy authority, or eligibility decision tool.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A FEMA declaration watcher may observe approved metadata or compare local artifacts, but it does not move data across lifecycle phases.

Required boundary rules:

1. **Watcher output is not publication.** It can propose work, not release a layer or record.
2. **Watcher output is not life-safety guidance.** It must not issue emergency alerts or operational warnings.
3. **Watcher output is not observed-event truth.** Declaration changes may indicate administrative action, not physical-world occurrence.
4. **Watcher output is not eligibility guidance.** It must not decide individual, household, property, county, tribal, insurance, or public-assistance eligibility.
5. **Connector output remains separate.** FEMA/OpenFEMA connectors may write only to raw or quarantine admission lanes according to their own boundaries.
6. **Processed artifacts remain separate.** Normalization, administrative object creation, joins, and domain projection belong to downstream governed workflows.
7. **Catalog closure remains separate.** STAC, DCAT, PROV, domain catalog records, receipts, proofs, and release manifests are not owned by this folder.
8. **AI and UI remain downstream.** No Focus Mode, Story Node, dashboard, or map surface may treat watcher output as source truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/fema_decl_watch/` include:

- OpenFEMA Disaster Declarations metadata watcher helpers.
- Disaster declaration sidecar comparison helpers.
- Declaration number / declaration type drift detectors.
- Incident-period and declaration-date change detectors.
- Designated-area summary drift detectors.
- OpenFEMA dataset schema or field-list drift checks.
- Source digest, `etag`, `last_modified`, row count, and pagination-state checks.
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
- unable to publish, promote, alert, decide eligibility, or mutate lifecycle records;
- tested with public-safe fixtures;
- explicit about its output envelope and finite outcomes.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/fema_decl_watch/` | Correct home | Reason |
|---|---|---|
| FEMA product doctrine | `docs/sources/catalog/fema/openfema-disaster-declarations.md` | Product documentation is not executable tooling. |
| SourceDescriptor records | `data/registry/sources/` or ratified source-registry lane | Source activation and source-role truth belong in registry records. |
| FEMA/OpenFEMA connector code of record | `connectors/fema/` or ratified OpenFEMA connector home | Connectors own source admission. |
| Raw OpenFEMA downloads | `data/raw/...` or `data/quarantine/...` | Data lifecycle roots own source material. |
| Processed DisasterDeclaration objects | `data/processed/...` | Transformation outputs are not tool code. |
| Catalog records | `data/catalog/...` | Catalog closure has its own root. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Emergency alerts or public warnings | outside this repo unless separately governed | This watcher is not an alerting system. |
| Benefit, insurance, or eligibility decisions | never here | Declaration records cannot be used by this watcher to decide individual status. |
| Observed hazard-event records | observed-source pipelines and contracts | Disaster declarations are administrative, not observed events. |
| Policy rules | `policy/` | Watcher code does not own policy meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Tests | `tests/ingest/fema_decl_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |
| Sensitive real examples | nowhere public | Fixtures must be public-safe and synthetic or generalized. |

[Back to top](#top)

---

## Disaster declaration watcher posture

The FEMA declaration watcher should be understood as a **review signaler** for administrative declaration change.

It may create:

- a watcher run report;
- a proposed work record;
- a new-declaration candidate summary;
- an amended-declaration candidate summary;
- a designated-area drift warning;
- a schema or field-list drift warning;
- a source metadata drift warning;
- a reviewer handoff file.

It must not create:

- a public disaster layer;
- a promoted release;
- an EvidenceBundle;
- a policy decision;
- a source descriptor correction;
- an observed hazard event;
- an emergency alert;
- a damage assessment;
- an individual, household, property, insurance, or benefit eligibility decision;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, why it may matter, what evidence or metadata was inspected, and what validation or steward review must happen next. It should not say the change is approved.

[Back to top](#top)

---

## Material-change model

The FEMA disaster-declarations product page defines the source-role guardrail: Disaster Declaration records are administrative federal actions and must remain distinct from observed hazard events. This README keeps watcher behavior bounded as proposed implementation guidance.

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed endpoint metadata, content length, digest, `etag`, `last_modified`, row count, pagination state, or declared update metadata. | **PROPOSED** |
| New declaration number | Detect newly visible DR / EM / FM declaration candidates. | **PROPOSED** |
| Amended declaration | Detect changed declaration date, incident period, title, incident type, program flag, or designated area for an existing declaration. | **PROPOSED** |
| Designated-area drift | Detect added or removed counties, states, tribal areas, or other declared geographies. | **PROPOSED** |
| Declaration-type drift | Detect DR / EM / FM classification changes or unexpected type vocabulary. | **PROPOSED** |
| Incident-type vocabulary drift | Detect unexpected incident-type values without treating them as observed events. | **PROPOSED** |
| Schema / field-list drift | Detect changed OpenFEMA field set or field type posture. | **PROPOSED** |
| Staleness check | Surface stale, missing, or unchanged expected source metadata according to configured cadence. | **PROPOSED** |

Thresholds should be configured, documented, and fixture-tested. Do not hard-code final materiality rules without review.

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `NEW_DECLARATION_CANDIDATE` | A new DR / EM / FM declaration candidate appears. |
| `AMENDED_DECLARATION_CANDIDATE` | An existing declaration appears to have changed. |
| `DESIGNATED_AREA_DRIFT` | Declared geography changed and downstream review is required. |
| `SCHEMA_DRIFT` | Field list or field shape changed; fail closed until reviewed. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured acceptable window. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- FEMA disaster declaration source descriptor reference, not duplicated descriptor fields.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- Local metadata fixture for an OpenFEMA dataset snapshot.
- Declaration identifier fixture.
- Declaration designated-area summary fixture.
- OpenFEMA field-list fixture.
- Public-safe test data.

### Unsuitable inputs

- credentials or secrets;
- unrestricted raw source dumps outside lifecycle control;
- unpublished source material passed directly to public outputs;
- person-, household-, parcel-, property-, insurance-, or benefit-eligibility records;
- real sensitive private data;
- observed-event records that should come from NOAA/NWS/USGS/fire/remote-sensing source lanes;
- exact restricted archaeology, rare-species, or infrastructure-risk coordinates;
- public emergency alert templates.

### Suitable outputs

- watcher JSON report;
- proposed work record candidate;
- new-declaration change summary;
- amended-declaration change summary;
- designated-area drift report;
- schema drift report;
- stale-input report;
- CI/reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice watcher report should be compact and deterministic.

```json
{
  "tool": "fema-decl-watch",
  "status": "NEW_DECLARATION_CANDIDATE",
  "source_id": "fema_disaster_declarations",
  "source_role": "administrative",
  "geography_scope": "state:kansas",
  "inputs": {
    "prior_sidecar": "tests/ingest/fema_decl_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/fema_decl_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "metadata_drift": "changed",
    "new_declaration_number": "candidate",
    "declaration_type_vocabulary": "expected",
    "designated_area_drift": "changed",
    "schema_drift": "same"
  },
  "decision": {
    "outcome": "NEW_DECLARATION_CANDIDATE",
    "reason_codes": ["FEMA_DECLARATION_NUMBER_ADDED", "FEMA_DESIGNATED_AREA_CHANGED"],
    "blocking": false,
    "life_safety_guidance": false,
    "observed_event_claim": false,
    "eligibility_decision": false
  },
  "next_review": [
    "confirm source descriptor and connector placement",
    "run FEMA/OpenFEMA connector admission workflow if approved",
    "validate rights and attribution requirements",
    "preserve administrative source role",
    "route through catalog and release gates before public use",
    "abstain from observed-event or eligibility claims until separate evidence exists"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/fema_decl_watch/
├── README.md
├── test_fema_decl_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── new_declaration/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── amended_declaration/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── designated_area_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── schema_drift/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same metadata and declaration summaries return `NO_MATERIAL_CHANGE`;
- new DR / EM / FM declaration identifier returns `NEW_DECLARATION_CANDIDATE` or `PROPOSED_WORK_RECORD` according to configured rules;
- amended incident-period or designated-area fields return `AMENDED_DECLARATION_CANDIDATE` or `DESIGNATED_AREA_DRIFT`;
- schema drift returns `SCHEMA_DRIFT` and fails closed;
- incident-type vocabulary drift is flagged without creating observed-event claims;
- missing sidecars return `ERROR` or `ABSTAIN` with clear reason codes;
- generated reports are deterministic;
- no test fixture contains real sensitive or private data;
- no helper writes to lifecycle or release roots without explicit workflow control;
- no helper emits emergency-alert, observed-event, or eligibility-decision language.

Suggested future command pattern:

```bash
pytest -q tests/ingest/fema_decl_watch
```

```bash
python tools/ingest/fema_decl_watch/fema_decl_watch.py \
  --prior tests/ingest/fema_decl_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/fema_decl_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/fema-decl-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `fema_decl_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing FEMA declaration watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot issue emergency alerts or public warnings.
- [ ] The helper cannot decide aid, benefit, insurance, or eligibility status.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Network access is off by default or explicitly read-only and documented.
- [ ] Materiality thresholds are configured and fixture-tested.
- [ ] Administrative source role is preserved.
- [ ] Incident type is not transformed into observed hazard-event truth.
- [ ] Designated-area drift does not masquerade as property-level impact.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests cover no-change, new-declaration, amended-declaration, designated-area-drift, schema-drift, missing-input, and malformed-input cases.
- [ ] The helper does not write directly to `data/catalog/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with watcher lane contract | **DONE in this README** | Establishes FEMA declaration watcher boundaries and non-publication/non-alert/non-eligibility rule. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve FEMA/OpenFEMA connector canonicality | **NEEDS VERIFICATION / ADR-class** | Prevents parallel connector authority roots. |
| Add `fema_decl_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe watcher fixtures | **PROPOSED** | Proves no-change, new-declaration, amended-declaration, designated-area-drift, and schema-drift behavior. |
| Align proposed-work-record schema | **PROPOSED / NEEDS VERIFICATION** | Match accepted contracts/schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces declaration drift without publication, alerting, eligibility, or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/fema_decl_watch/fema_decl_watch.py` with public-safe fixtures under `tests/ingest/fema_decl_watch/`. |
