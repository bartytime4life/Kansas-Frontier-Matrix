<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-plants-watch-readme
title: tools/ingest/plants_watch README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-flora-source-steward-plus-sensitivity-reviewer
created: 2026-07-07
updated: 2026-07-07
policy_label: public-context; watcher-only; no-publication; rare-plant-exact-geometry-fail-closed
owning_root: tools/
responsibility: proposed USDA PLANTS and flora-source watcher helper boundary for taxonomy, distribution, source-head, and sensitivity review signals
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../docs/sources/catalog/usda/usda-plants.md
  - ../../../docs/sources/catalog/kansas/ku-herbarium.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../docs/sources/catalog/eddmaps/README.md
  - ../../../data/registry/sources/flora/README.md
  - ../../../pipelines/domains/flora/ingest/README.md
  - ../../../contracts/domains/flora/rare_plant_record.md
  - ../../../contracts/domains/flora/domain_observation.md
  - ../../../data/raw/flora/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README defines a proposed PLANTS/flora watcher tooling boundary, not a confirmed implementation."
  - "USDA PLANTS is treated as the Flora taxonomic backbone and state/county distribution scaffold, but source changes are review signals, not public botanical truth."
  - "Rare, protected, culturally sensitive, or steward-reviewed plant locations must fail closed for exact public geometry."
  - "The watcher may detect taxonomy, distribution, source-head, source-descriptor, and sensitivity-relevant changes; it must not publish, promote, decide taxonomy, expose sensitive locations, or mutate source-role truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/plants_watch

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-plants--watcher-informational)
![domain](https://img.shields.io/badge/domain-flora-2e7d32)
![sensitivity](https://img.shields.io/badge/rare--exact--geometry-fail--closed-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/plants_watch/` is the proposed tooling lane for detecting review-worthy USDA PLANTS and flora-source changes and emitting governed watcher reports. It is not a connector, not a Flora ingest pipeline, not a taxonomic authority, not a rare-plant disclosure surface, not a publication path, and not botanical truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Plants watcher posture](#plants-watcher-posture)
- [Material-change model](#material-change-model)
- [Sensitivity and geoprivacy posture](#sensitivity-and-geoprivacy-posture)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/plants_watch/` exists to hold durable, repo-wide helper logic for a **watcher-style** Flora source-change detector, with USDA PLANTS as the first expected source family.

The watcher may compare approved local metadata, source sidecars, snapshot manifests, source-head records, taxon symbol inventories, name/family/growth-habit/wetland-status summaries, state/county distribution summaries, source descriptor references, rights flags, sensitivity flags, or no-network fixtures to decide whether Flora source material should be reviewed.

The durable KFM question for this lane is:

> Did a plant taxonomy, distribution, source descriptor, source-head, or sensitivity-relevant source surface change enough to propose governed review work?

The answer should be a review signal. It should never be a connector run, raw capture of record, taxonomy decision, rare-plant publication, exact sensitive-location disclosure, processed Flora truth record, EvidenceBundle, catalog closure, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/plants_watch/README.md` | **CONFIRMED** | This README defines the PLANTS/flora watcher tooling boundary. |
| Plants watcher executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| Flora domain README | **CONFIRMED in repo evidence** | Domain docs state Flora governs plant identity, occurrences, specimens, rare/protected controls, and public-safe outputs. |
| Flora source registry | **CONFIRMED in repo evidence / draft** | Human-readable registry anchors source identity, role, rights, sensitivity, cadence, and admission posture. |
| USDA PLANTS product page | **CONFIRMED in repo evidence / draft** | Product page treats PLANTS as Flora taxonomy and state/county distribution scaffold. |
| Flora ingest pipeline lane | **CONFIRMED in repo evidence / draft** | Pipeline lane owns executable normalization after source admission. |
| Watcher cadence | **PROPOSED / NEEDS VERIFICATION** | Cadence must be source-specific and steward-approved. |
| Materiality thresholds | **PROPOSED / NEEDS VERIFICATION** | Thresholds must be fixture-tested before workflow use. |
| Publication authority | **DENY here** | Watchers do not publish or promote. |
| Rare/protected exact public geometry | **DENY here** | Exact sensitive plant locations fail closed unless separate policy/release gates permit a public-safe transform. |
| Taxonomy decision authority | **DENY here** | Watcher output cannot decide accepted taxonomy or reconcile names as truth. |

> [!IMPORTANT]
> This folder is for watcher reports only. A change in PLANTS, herbarium, occurrence, invasive, phenology, restoration, or vegetation source material does not mean KFM has a public Flora fact. It means stewards may need to review source descriptors, connectors, pipeline inputs, sensitivity policy, receipts, proofs, catalog records, release state, or rollback paths.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `docs/domains/flora/` owns Flora domain doctrine. `docs/sources/catalog/` owns source-product documentation. `data/registry/sources/flora/` owns machine-readable source activation and descriptor truth when accepted. `pipelines/domains/flora/ingest/` owns executable Flora ingest normalization. `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/plants_watch/README.md`.
- **PROPOSED:** PLANTS/flora watcher code may live here if it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether watcher outputs should be split by flora source family after implementation evidence exists.
- **DENY:** any use of this path as a connector, raw-data sink, processed-data store, taxonomy authority, geoprivacy release path, catalog/proof/release authority, public API, map layer, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A plants watcher may observe metadata or compare local sidecars. It does not move data across lifecycle states by itself.

Required boundary rules:

1. **Watcher output is not publication.** It can propose review work, not release a layer.
2. **Watcher output is not source admission.** Connectors and governed workflows own raw/quarantine source capture.
3. **Watcher output is not taxonomy truth.** Taxonomic reconciliation, accepted-name decisions, synonym handling, and identity changes require downstream contracts, validation, evidence, and review.
4. **Watcher output is not occurrence truth.** Specimen and occurrence records remain source-bound until reviewed.
5. **Watcher output is not catalog closure.** STAC, DCAT, PROV, domain catalog records, triplets, receipts, proofs, and release manifests are outside this folder.
6. **Rare exact geometry fails closed.** Sensitive plant coordinates, rare/protected species locations, and culturally sensitive botanical locations must not be emitted as public exact geometry by this lane.
7. **Public map products remain downstream.** Generalized public layers require sensitivity review, transform receipts, release manifests, and rollback paths.
8. **AI and UI remain downstream.** No Focus Mode, map, dashboard, or AI answer may read directly from this watcher lane or treat watcher output as truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/plants_watch/` include:

- USDA PLANTS source metadata watcher helpers;
- Flora source sidecar comparison helpers;
- `plants:symbol` inventory drift checks;
- scientific-name, author, family, common-name, growth-habit, wetland-status, and native-status summary drift checks;
- state and county distribution summary drift checks;
- taxonomy rename / synonym / accepted-name review-signal checks;
- source descriptor reference checks;
- source-head `etag`, `last_modified`, `content_length`, digest, and snapshot-date checks;
- rights and attribution posture drift checks;
- rare/protected/sensitive source flag drift checks;
- geoprivacy transform readiness checks;
- proposed-work-record emitters;
- watcher run report generators;
- dry-run CLI wrappers for local review;
- no-network fixture adapters for tests.

A helper belongs here only when it is deterministic, read-only by default, explicit about inspected inputs, conservative about materiality thresholds, unable to publish or promote, unable to expose sensitive exact locations, and clear that its output is a review signal.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/plants_watch/` | Correct home | Reason |
|---|---|---|
| Flora domain doctrine | `docs/domains/flora/` | Human-facing doctrine is not watcher code. |
| USDA PLANTS product doctrine | `docs/sources/catalog/usda/usda-plants.md` | Product documentation is not watcher code. |
| Flora source descriptors | `data/registry/sources/flora/` | Source identity, role, rights, cadence, and activation belong in the registry. |
| Source fetchers or API clients of record | ratified connector home | Connectors own source acquisition and admission. |
| Flora ingest pipeline logic of record | `pipelines/domains/flora/ingest/` | Pipelines own executable lifecycle normalization. |
| Raw Flora source captures | `data/raw/flora/...` | Lifecycle data is outside tooling. |
| Quarantine records | `data/quarantine/...` | Holds are lifecycle artifacts, not watcher code. |
| Processed Flora records | `data/processed/flora/...` | Validated outputs are not watcher code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure has its own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Taxonomic authority decisions | downstream Flora contracts, validators, and reviewed evidence | Watcher reports cannot decide accepted botanical truth. |
| Exact rare/protected plant coordinates | never from this lane | Sensitive geometry requires policy, redaction/generalization, review, and release controls. |
| Policy rules | `policy/` | Watchers do not own admissibility or release meaning. |
| Schemas or contracts | `schemas/`, `contracts/` | Shape and meaning are separate authority roots. |
| Public maps, API payloads, or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/plants_watch/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## Plants watcher posture

The plants watcher should be understood as a **review signaler** for Flora source change.

It may create:

- a watcher run report;
- a source metadata drift summary;
- a source staleness report;
- a taxon-symbol inventory drift summary;
- a taxonomy/name/family drift report;
- a distribution summary drift report;
- a rights or attribution drift report;
- a sensitivity/geoprivacy review report;
- a proposed work record;
- a reviewer handoff summary.

It must not create:

- a raw capture of record;
- a processed Flora object of record;
- a public plant occurrence layer;
- an exact sensitive species layer;
- a taxonomic decision;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what changed, what source-role boundary is relevant, what sensitivity or rights checks are triggered, what evidence or metadata was inspected, and what downstream validation or steward review must happen next. It should not say the change is approved, public, or botanically resolved.

[Back to top](#top)

---

## Material-change model

Recommended first material-change checks:

| Check | Purpose | First-slice posture |
|---|---|---|
| Source metadata drift | Detect changed digest, `etag`, `last_modified`, content length, snapshot date, file inventory, or source version metadata. | **PROPOSED** |
| Expected cadence / staleness | Surface stale, missing, or delayed source snapshots. | **PROPOSED** |
| SourceDescriptor drift | Detect changed source role, rights, activation, cadence, steward, or canonical connector reference. | **PROPOSED** |
| Mandatory-field drift | Detect missing `plants:symbol`, scientific name with author, or family fields. | **PROPOSED** |
| Taxon inventory drift | Detect added, removed, merged, split, or renamed symbols. | **PROPOSED** |
| Taxonomy/name drift | Detect changed accepted name, synonym set, author, family, common name, or identity hash candidate. | **PROPOSED** |
| Distribution drift | Detect changed state/county distribution, FIPS coverage, presence flag, or first-observed/null semantics. | **PROPOSED** |
| Attribute drift | Detect changed growth habit, native status, wetland status, invasive status, or other mapped attributes. | **PROPOSED** |
| Rights/attribution drift | Detect changed rights, attribution, or source-use posture. | **PROPOSED** |
| Sensitivity drift | Detect rare/protected/culturally sensitive flags or exact-location risk requiring fail-closed handling. | **PROPOSED** |

Recommended finite outcomes:

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | Source metadata, digest, endpoint headers, or inventory changed. |
| `NEW_PLANTS_SNAPSHOT_CANDIDATE` | A new PLANTS snapshot or source window appears available for steward review. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `MANDATORY_FIELD_DRIFT` | Required fields are missing or changed in a way that blocks safe interpretation. |
| `TAXON_INVENTORY_DRIFT` | Taxon symbol inventory changed. |
| `TAXONOMY_REVIEW_CANDIDATE` | Names, synonyms, authors, families, or identity hashes changed. |
| `DISTRIBUTION_DRIFT` | State/county distribution summaries changed. |
| `RIGHTS_OR_ATTRIBUTION_DRIFT` | Rights, source-use, or attribution posture changed. |
| `SENSITIVITY_REVIEW_REQUIRED` | Rare/protected/sensitive flags or exact-geometry risk requires review. |
| `SOURCE_ROLE_AMBIGUOUS` | The watcher cannot preserve source-role separation safely; fail closed. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The watcher cannot decide with the available evidence. |
| `ERROR` | The watcher could not safely complete. |

[Back to top](#top)

---

## Sensitivity and geoprivacy posture

Flora public outputs must be safer than the source material when sensitive plants are involved.

| Surface | Watcher posture |
|---|---|
| Common-species checklist or county distribution | May produce review signals if source role, rights, and fields are clear. |
| Rare/protected species exact occurrence | `SENSITIVITY_REVIEW_REQUIRED`; no exact public geometry from this lane. |
| Culturally sensitive plant location | Prefer `ABSTAIN`, `QUARANTINE`, or restricted review. |
| Herbarium specimen coordinates | Treat as source-bound and sensitivity-reviewed; do not publish exact coordinates here. |
| Citizen-science occurrence coordinates | Treat as candidate/observed according to source descriptor; require rights and sensitivity review. |
| Invasive plant records | Do not collapse into agriculture, hazard, or habitat truth; preserve source role and evidence. |
| County/state distribution | Lower-risk than exact geometry, but still must preserve source, date, and source-role caveats. |
| Generalized public layer | Requires downstream transform receipt, policy decision, review record, release manifest, and rollback path. |

Safe defaults are `ABSTAIN`, `QUARANTINE`, `SENSITIVITY_REVIEW_REQUIRED`, or `DENY_PUBLIC_EXACT_GEOMETRY` when location precision, species sensitivity, rights, or steward review state is unclear.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- Flora SourceDescriptor references.
- Prior watcher sidecar JSON.
- Current watcher sidecar JSON.
- USDA PLANTS snapshot metadata fixtures.
- Taxon-symbol inventory fixtures.
- Scientific-name/family/common-name summary fixtures.
- State/county distribution summary fixtures.
- Rights and attribution fixtures.
- Sensitivity flag fixtures.
- Geometry precision and geoprivacy sidecars.
- Public-safe synthetic fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- exact rare/protected plant coordinates intended for public output;
- culturally sensitive plant locations without steward review;
- unpublished source material passed directly to public outputs;
- taxonomy decisions not backed by source descriptor, evidence, and review;
- public maps or tiles created from watcher output;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- watcher JSON report;
- source metadata drift report;
- taxon inventory drift report;
- taxonomy review candidate report;
- distribution drift report;
- rights/attribution drift report;
- sensitivity review report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A watcher should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice plants watcher report should be compact and deterministic.

```json
{
  "tool": "plants-watch",
  "status": "TAXONOMY_REVIEW_CANDIDATE",
  "source_id": "usda_plants_placeholder",
  "domain": "flora",
  "inputs": {
    "prior_sidecar": "tests/ingest/plants_watch/fixtures/prior_sidecar.json",
    "current_sidecar": "tests/ingest/plants_watch/fixtures/current_sidecar.json"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "metadata_drift": "changed",
    "mandatory_fields": "present",
    "taxon_inventory_drift": "changed",
    "taxonomy_name_drift": "changed",
    "distribution_drift": "none",
    "rights_or_attribution_drift": "none",
    "sensitivity_flags": "review_required"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["TAXON_INVENTORY_DRIFT", "TAXONOMY_REVIEW_CANDIDATE", "SENSITIVITY_REVIEW_REQUIRED"],
    "blocking": false,
    "publication": false,
    "public_exact_geometry": false,
    "taxonomy_decision": false
  },
  "next_review": [
    "confirm Flora source descriptor and rights posture",
    "preserve source role and source-head evidence",
    "route through Flora ingest pipeline after admission",
    "review rare/protected/culturally sensitive location posture",
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
tests/ingest/plants_watch/
├── README.md
├── test_plants_watch.py
└── fixtures/
    ├── no_material_change/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── source_metadata_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── taxon_inventory_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── taxonomy_review_candidate/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    ├── distribution_drift/
    │   ├── prior_sidecar.json
    │   └── current_sidecar.json
    └── sensitivity_review_required/
        ├── prior_sidecar.json
        └── current_sidecar.json
```

Recommended assertions:

- same sidecars return `NO_MATERIAL_CHANGE`;
- changed metadata returns `SOURCE_METADATA_DRIFT` or `PROPOSED_WORK_RECORD` according to configured rules;
- missing required fields returns `MANDATORY_FIELD_DRIFT` or `ABSTAIN`;
- added/removed/renamed symbols return `TAXON_INVENTORY_DRIFT` or `TAXONOMY_REVIEW_CANDIDATE`;
- county/state distribution changes return `DISTRIBUTION_DRIFT`;
- rare/protected/culturally sensitive location indicators return `SENSITIVITY_REVIEW_REQUIRED` and deny exact public geometry;
- watcher output cannot create taxonomy decisions, EvidenceBundles, release manifests, public maps, or PMTiles;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/plants_watch
```

```bash
python tools/ingest/plants_watch/plants_watch.py \
  --prior tests/ingest/plants_watch/fixtures/no_material_change/prior_sidecar.json \
  --current tests/ingest/plants_watch/fixtures/no_material_change/current_sidecar.json \
  --output .tmp/plants-watch-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `plants_watch.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing plants watcher code, reviewers should confirm:

- [ ] The helper is watcher/report-only and cannot publish.
- [ ] The helper cannot fetch source material as the source-admission path of record.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Mandatory field checks preserve `plants:symbol`, scientific name with author, and family where applicable.
- [ ] Taxonomy changes are review candidates, not accepted-name decisions.
- [ ] State/county distribution changes preserve source date and source role.
- [ ] Rare/protected/culturally sensitive exact locations fail closed.
- [ ] Geoprivacy and redaction requirements are surfaced as review requirements.
- [ ] Rights and attribution posture are checked where available.
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
| Replace empty README with governed plants watcher contract | **DONE in this README** | Establishes watcher boundaries and rare-plant geoprivacy posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve PLANTS connector canonicality | **NEEDS VERIFICATION / ADR-class if contested** | Prevents duplicate source-admission authority. |
| Add `plants_watch.py` dry-run helper | **PROPOSED** | Emits deterministic watcher report from local sidecars. |
| Add public-safe fixtures | **PROPOSED** | Proves no-change, metadata drift, taxon drift, taxonomy review, distribution drift, and sensitivity behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted Flora contracts and schemas when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces Flora source-change and sensitivity issues without publication or source-admission side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/plants_watch/plants_watch.py` with public-safe fixtures under `tests/ingest/plants_watch/`. |
