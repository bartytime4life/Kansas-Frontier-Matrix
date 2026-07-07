<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-readme
title: tools/ingest README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-domain-source-stewards
created: 2026-07-07
updated: 2026-07-07
policy_label: public; tooling-index; watcher-and-preflight-boundary; no-publication
owning_root: tools/
responsibility: parent boundary and index for ingest-adjacent watcher, preflight, and review-signal helpers under tools/
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/people-dna-land/ARCHITECTURE.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../connectors/
  - ../../pipelines/
  - ../../policy/
  - ../../release/
notes:
  - "This README defines the parent boundary for tools/ingest helper lanes, not proof that every proposed executable exists."
  - "tools/ingest helpers may inspect, compare, preflight, and report. They must not fetch as source-of-record connectors, normalize as pipelines of record, publish, promote, create EvidenceBundles, or decide source-role truth."
  - "Child folders with *_watch names are watcher/review-signal lanes. Child folders without *_watch may be dry-run preflight or ingest-support lanes only when their README says so."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-ingest--adjacent--helpers-informational)
![publication](https://img.shields.io/badge/publication-denied-lightgrey)
![authority](https://img.shields.io/badge/authority-review--signals--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/` is the parent tooling lane for ingest-adjacent helpers that inspect, compare, preflight, and report source-material changes for steward review. It is not a connector root, not a pipeline root, not a lifecycle data root, not a catalog/proof/release root, not a public API, and not truth authority.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Authority boundary](#authority-boundary)
- [Child lanes](#child-lanes)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Standard lifecycle boundary](#standard-lifecycle-boundary)
- [Standard finite outcomes](#standard-finite-outcomes)
- [Standard report envelope](#standard-report-envelope)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/` collects long-lived, repo-wide helper tooling that supports source intake and refresh review **without becoming the intake authority itself**.

The lane exists because many KFM domains need the same kind of deterministic, dry-run-friendly support:

- compare a prior source sidecar with a current sidecar;
- detect material source-surface drift;
- check source descriptor references;
- flag source-role ambiguity;
- surface freshness or staleness problems;
- create review-signal reports;
- produce proposed work records;
- help reviewers decide whether a connector, pipeline, validation, receipt, proof, catalog, or release workflow should run next.

The durable KFM question for this parent lane is:

> Did source-adjacent evidence change or fail checks in a way that requires governed review?

The answer should be a bounded report. It should never be a source capture of record, processed truth, EvidenceBundle, catalog closure, public product, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/README.md` | **CONFIRMED** | This parent README replaces the previous empty file. |
| `tools/` root authority | **CONFIRMED in repo evidence** | `tools/` owns repo-wide validators, generators, builders, and trust tooling; it does not own policy, contract, schema, or release authority. |
| `tools/ingest/` parent lane | **PROPOSED / draft** | The folder now has a parent contract, but executable layout and CI wiring remain unverified. |
| Child watcher READMEs | **CONFIRMED where current-session fetched or recently updated** | Child lanes are documented as review-signal, preflight, or watcher-only. |
| Child executables | **PROPOSED-to-create / NEEDS VERIFICATION** | This README does not claim scripts exist unless current repo evidence proves them. |
| Source descriptors | **Owned elsewhere** | Source identity, role, rights, cadence, and activation belong under `data/registry/sources/`. |
| Connectors | **Owned elsewhere** | Source acquisition and raw/quarantine handoff belong under `connectors/` or ratified connector homes. |
| Pipelines | **Owned elsewhere** | Executable lifecycle normalization belongs under `pipelines/` or accepted pipeline homes. |
| Publication authority | **DENY here** | Helpers under this folder do not publish or promote. |

> [!IMPORTANT]
> `tools/ingest/` is a support lane. It may say **review needed**. It must not say **truth accepted**, **source admitted**, **record promoted**, **catalog closed**, or **release approved**.

[Back to top](#top)

---

## Authority boundary

`tools/ingest/` inherits the `tools/` root boundary:

- `tools/` owns durable executable support and repo-wide trust tooling.
- `connectors/` owns source-specific fetch/admission paths.
- `pipelines/` owns executable domain normalization and transform workflows.
- `data/raw/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, and `data/triplets/` own lifecycle data states.
- `data/receipts/` and `data/proofs/` own trust artifacts.
- `contracts/`, `schemas/`, and `policy/` own meaning, shape, and admissibility.
- `release/` owns release manifests, rollback cards, correction state, and publication decisions.

Safe interpretation for this path:

- **CONFIRMED:** the parent README exists at `tools/ingest/README.md`.
- **PROPOSED:** helper code may live here when it is deterministic, dry-run friendly, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether every child folder has executable code, tests, CI wiring, source descriptors, and fixtures.
- **DENY:** any use of this folder as connector authority, source registry, lifecycle data store, processed truth store, catalog/proof/release authority, public API, or policy authority.

[Back to top](#top)

---

## Child lanes

Known child README lanes in this folder are listed below. Status is intentionally conservative: a README can be confirmed while executable code remains proposed.

| Child lane | Type | Primary review signal | Status |
|---|---|---|---|
| `cdl_watch/` | watcher | USDA NASS Cropland Data Layer source changes. | README confirmed; executable proposed. |
| `drought_watch/` | watcher | U.S. Drought Monitor source changes. | README confirmed; executable proposed. |
| `fema_decl_watch/` | watcher | OpenFEMA disaster declaration administrative-record changes. | README confirmed; executable proposed. |
| `firms_hms_watch/` | watcher | NASA FIRMS and NOAA HMS fire/smoke source-surface changes. | README confirmed; executable proposed. |
| `genealogy/` | preflight / ingest support | Genealogy source parsing, privacy, consent, and candidate assertion review. | README confirmed; executable proposed. |
| `hydrology/` | preflight / ingest support | Hydrology source-shape, unit, datum, time, and source-role preflight review. | README confirmed; executable proposed. |
| `hydrology_watch/` | watcher | Hydrology source metadata, version, staleness, and inventory drift. | README confirmed; executable proposed. |
| `nfhl_watch/` | watcher | FEMA NFHL regulatory-source drift. | README confirmed; executable proposed. |
| `nws_context_watch/` | watcher | NOAA NWS context freshness, expiry, and component-role drift. | README confirmed; executable proposed. |
| `plants_watch/` | watcher | USDA PLANTS and Flora taxonomy/distribution/sensitivity drift. | README confirmed; executable proposed. |
| `state_em_watch/` | watcher | State emergency-management administrative-context drift. | README confirmed; executable proposed. |
| `storm_events_watch/` | watcher | NOAA/NCEI Storm Events release-window, schema, correction, and geography drift. | README confirmed; executable proposed. |
| `usgs_eq_watch/` | watcher | USGS earthquake event-update, sub-product, snapshot, and source-role drift. | README confirmed; executable proposed. |

Naming rule:

- `*_watch/` means watcher/review-signal only.
- Non-`*_watch/` folders under this parent must clearly state whether they are dry-run preflight helpers, ingest-support helpers, or another bounded support pattern.
- A child folder name must not imply source authority, truth authority, release authority, or public API status.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/` include:

- watcher helpers that compare prior/current sidecars;
- source-head and source-window comparison helpers;
- dry-run preflight helpers for source-shape checks;
- source descriptor reference checks;
- source-role anti-collapse checks;
- freshness, staleness, expiry, or supersession checks;
- unit, datum, CRS, geometry, identifier, or schema/header checks;
- materiality-threshold evaluation helpers;
- deterministic JSON report emitters;
- proposed-work-record emitters;
- reviewer handoff generators;
- no-network fixture adapters.

A helper belongs here only when it is:

- deterministic;
- read-only or dry-run by default;
- explicit about input paths and output paths;
- explicit about source descriptor references;
- clear about finite outcomes;
- unable to publish, promote, or create catalog/proof/release authority;
- tested with public-safe or synthetic fixtures;
- owned by tooling/QA plus the relevant domain/source steward.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/` | Correct home | Reason |
|---|---|---|
| Source fetchers or API clients of record | `connectors/` or ratified source connector home | Connectors own source acquisition and admission. |
| Domain ingest pipelines of record | `pipelines/domains/...` or accepted pipeline home | Pipelines own lifecycle normalization. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, cadence, and activation are registry authority. |
| Raw source captures | `data/raw/` | RAW is a lifecycle state, not tooling. |
| Quarantine holds | `data/quarantine/` | Holds are lifecycle artifacts, not helper code. |
| Processed records | `data/processed/` | Processed truth candidates are not tool code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog and graph closure have their own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Contracts or schemas | `contracts/`, `schemas/` | Meaning and shape live outside this helper lane. |
| Policy rules | `policy/` | Admissibility and sensitivity decisions live outside this helper lane. |
| Public API behavior or UI surfaces | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/ingest/...` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## Standard lifecycle boundary

The lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

`tools/ingest/` helpers may inspect or compare material associated with lifecycle states, but they do not move records through those states on their own.

Allowed helper outputs:

- `NO_MATERIAL_CHANGE` report;
- drift report;
- preflight report;
- source-role ambiguity report;
- sensitivity review report;
- proposed work record;
- reviewer handoff summary.

Denied helper outputs:

- raw capture of record;
- processed object of record;
- canonical source descriptor;
- EvidenceBundle;
- PolicyDecision;
- ReviewRecord;
- ReleaseManifest;
- public map/tile/API payload;
- AI answer treated as truth.

[Back to top](#top)

---

## Standard finite outcomes

Child lanes may extend these, but should preserve the core pattern.

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Valid comparison found no review-worthy change under configured rules. |
| `SOURCE_METADATA_DRIFT` | Source metadata, digest, endpoint headers, sidecars, or inventory changed. |
| `NEW_SOURCE_WINDOW` | A new source window, snapshot, version, or event candidate appears available for steward review. |
| `STALE_INPUT` | Source metadata or sidecar is older than the configured window. |
| `SOURCE_DESCRIPTOR_DRIFT` | Source descriptor posture changed and review is required. |
| `SCHEMA_OR_FIELD_DRIFT` | Required fields, headers, encoding, expected keys, or type hints changed. |
| `GEOMETRY_OR_VERSION_DRIFT` | Geometry, CRS, datum, package version, or feature inventory changed. |
| `SOURCE_ROLE_AMBIGUOUS` | The helper cannot preserve source-role separation safely; fail closed. |
| `SENSITIVITY_REVIEW_REQUIRED` | Rights, privacy, location precision, or sensitivity posture requires review before any downstream exposure. |
| `PROPOSED_WORK_RECORD` | Valid comparison found review-worthy change; downstream review is required. |
| `ABSTAIN` | The helper cannot decide with the available evidence. |
| `ERROR` | The helper could not safely complete. |

[Back to top](#top)

---

## Standard report envelope

Child lanes should keep reports deterministic and machine-readable.

```json
{
  "tool": "example-watch-or-preflight",
  "status": "PROPOSED_WORK_RECORD",
  "source_id": "source_descriptor_placeholder",
  "domain": "domain_placeholder",
  "inputs": {
    "prior_sidecar": "path/or/null",
    "current_sidecar": "path/or/null"
  },
  "checks": {
    "source_descriptor_ref": "present",
    "source_role_separation": "preserved",
    "metadata_drift": "changed",
    "schema_or_field_drift": "none",
    "sensitivity_review": "not_required"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["SOURCE_METADATA_DRIFT"],
    "blocking": false,
    "publication": false
  },
  "next_review": [
    "confirm source descriptor and rights posture",
    "confirm connector or pipeline home before execution",
    "preserve source-role boundaries",
    "validate contracts and schemas before catalog work",
    "do not publish without policy, review, release, and rollback controls"
  ]
}
```

Reports are not receipts unless a separate governed workflow adopts them and stores them under the proper receipt root.

[Back to top](#top)

---

## Review checklist

Before adding or changing anything under `tools/ingest/`, reviewers should confirm:

- [ ] The helper is watcher/preflight/report-only unless invoked by a governed workflow.
- [ ] The helper cannot publish or promote.
- [ ] The helper cannot become the source connector of record unless moved/ratified under connector authority.
- [ ] The helper does not own SourceDescriptor truth.
- [ ] The helper does not own contract, schema, policy, catalog, proof, or release authority.
- [ ] Source roles remain separate.
- [ ] Rights, privacy, sensitivity, and geoprivacy issues fail closed.
- [ ] Input and output paths are explicit.
- [ ] Network access is off by default or documented as read-only probe behavior.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty parent README with governed `tools/ingest/` contract | **DONE in this README** | Establishes the parent boundary and child-lane index. |
| Reconcile child README links after path audit | **PROPOSED** | Ensure all related links point to existing doctrine, connector, registry, and pipeline files. |
| Add shared report schema or fixture convention | **PROPOSED / NEEDS VERIFICATION** | Prevent each watcher from inventing incompatible report envelopes. |
| Add `tests/ingest/README.md` | **PROPOSED** | Defines public-safe fixture rules and deterministic output expectations. |
| Add CI non-blocking review summary | **PROPOSED / later** | Surfaces watcher/preflight drift without promotion or release side effects. |
| Promote stable helpers into guarded workflows | **PROPOSED / later** | Only after fixtures, tests, descriptor activation, and steward review are in place. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft parent README replacement for existing empty file. |
| Next smallest safe change | Add or verify `tests/ingest/README.md`, then add shared fixture/report conventions for watcher lanes. |
