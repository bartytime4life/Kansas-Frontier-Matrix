<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-dashboard-catalog
title: Dashboard Catalog — index of all KFM dashboard specifications
type: standard
version: v0.2
status: draft
owners:
  - <dashboards-stewards>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-06-11
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/INDICATOR_CATALOG.md
  - docs/dashboards/governance/README.md
  - docs/dashboards/operational/README.md
  - docs/dashboards/domain/README.md
  - docs/dashboards/observability/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, docs, dashboards, catalog, index, governance-health, observability]
notes:
  - "Every dashboard spec under docs/dashboards/ MUST appear in this catalog."
  - "Spec-file presence is separate from running-surface verification."
  - "This v0.2 refresh updates the catalog from 24 planned dashboard specs to 34 repo-observed dashboard spec files."
  - "Running dashboards, telemetry data, receipts, proofs, policy logic, schemas, release manifests, and generated reports do not live in docs/dashboards/."
  - "All running-surface claims remain PROPOSED or NEEDS VERIFICATION until checked against implementation evidence."
[/KFM_META_BLOCK_V2] -->

# Dashboard Catalog · `docs/dashboards/DASHBOARD_CATALOG.md`

> The single index of dashboard specification files under `docs/dashboards/`. Each row links a spec file to its category, source card or indicator family, proposed steward, proposed running surface, file-presence state, and implementation status.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Truth posture](https://img.shields.io/badge/truth-cite--or--abstain-blue)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)
![Specs](https://img.shields.io/badge/specs-34%20cataloged-yellow)
![Spec files](https://img.shields.io/badge/spec%20files-CONFIRMED%20by%20accessible%20repo%20search-blue)
![Runtime](https://img.shields.io/badge/runtime-NEEDS%20VERIFICATION-yellow)
![Placement](https://img.shields.io/badge/placement-PROPOSED-orange)

**Status:** draft · **Owners:** `<dashboards-stewards>` (PROPOSED) · **Last reviewed:** 2026-06-11

---

> [!IMPORTANT]
> Every dashboard spec carries its own truth posture. This catalog confirms only that specification files are cataloged from accessible repo evidence. It does **not** claim a running dashboard surface, mounted telemetry stack, validated implementation, promotion, publication, or release.

> [!CAUTION]
> `docs/dashboards/` is a documentation lane for dashboard specifications and indexes. It must not become a parallel authority for receipts, proofs, schemas, policy logic, telemetry data, release decisions, generated reports, or running dashboard code.

---

## Quick jump

- [1. How to use this catalog](#1-how-to-use-this-catalog)
- [2. Evidence and verification basis](#2-evidence-and-verification-basis)
- [3. Governance dashboards](#3-governance-dashboards)
- [4. Operational dashboards](#4-operational-dashboards)
- [5. Domain dashboards](#5-domain-dashboards)
- [6. Observability dashboards](#6-observability-dashboards)
- [7. Lifecycle states](#7-lifecycle-states)
- [8. Open questions](#8-open-questions)

---

## 1. How to use this catalog

- **Adding a dashboard spec?** Author the spec under the right category folder, then add a row here in the same PR.
- **Auditing coverage?** Cross-check this file against `docs/dashboards/INDICATOR_CATALOG.md`, category READMEs, and a fresh repo tree/search.
- **Promoting status?** Do not change `PROPOSED` to `CONFIRMED` unless implementation evidence proves the running surface and the receipts it reads.
- **Resolving drift?** Use the open questions below. Do not silently remove duplicate or lower-case/upper-case spec paths without a migration note or ADR if links may already exist.

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 2. Evidence and verification basis

| Claim | Status | Evidence basis |
|---|---|---|
| `docs/dashboards/DASHBOARD_CATALOG.md` exists in the accessible repo. | CONFIRMED | Direct fetch of current catalog. |
| `docs/dashboards/README.md` says `docs/dashboards/` is a proposed documentation surface, not the running dashboard implementation. | CONFIRMED | Direct fetch of dashboard README. |
| Category READMEs exist for governance, operational, domain, and observability. | CONFIRMED | Direct fetch/search of category README files. |
| 34 dashboard spec files are cataloged below. | CONFIRMED for accessible repo search results; NEEDS VERIFICATION for mounted checkout completeness. | Category/path searches for `docs/dashboards/([('governance/EVIDENCE_INTEGRITY.md', 'EvidenceRef resolution, cite-or-abstain compliance, source-role drift, stale-source rate, quarantine throughput.', 'Atlas v1.1 §24.11.1', 'Release / Source / AI surface stewards', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('governance/RELEASE_CORRECTION_ROLLBACK.md', 'Rollback-target coverage, correction lead time, derivative-invalidation coverage, rollback rehearsal rate, supersession lineage gaps.', 'Atlas v1.1 §24.11.2', 'Release steward · Correction reviewer', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('governance/SENSITIVITY_RIGHTS.md', 'Sensitive-lane fail-closed rate, RedactionReceipt coverage, review-aged-out incidence, rights-change response time, side-channel audit cadence.', 'Atlas v1.1 §24.11.3', 'Sensitivity reviewer · Rights-holder representative', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('governance/AI_SURFACE_HEALTH.md', 'AIReceipt presence rate, ABSTAIN rate by template, DENY reason distribution, synthetic-claim incidence.', 'Atlas v1.1 §24.11.4', 'AI surface steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('governance/DOCUMENTATION_DRIFT.md', 'ADR completeness, drift register size, per-root README presence, atlas/supplement lineage clarity.', 'Atlas v1.1 §24.11.5', 'Docs steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED')], [('operational/SLO_LIVE_FEEDS.md', 'Standards-first SLOs for live transit and other high-cadence feeds: freshness, schema validation, latency, deduplication, non-material suppression, agency license terms.', 'KFM-P11-FEAT-0002', 'Source steward · Observability steward', 'OpenTelemetry stack / apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('operational/REALTIME_FEED_FRESHNESS.md', 'Realtime feed health: schema validation, SLO freshness, canonical identity, partition output, promotion/hold state.', 'KFM-P31-FEAT-0015', 'Source steward', 'OpenTelemetry stack / apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('operational/COG_ZARR_REPRODUCIBILITY.md', 'Raster/datacube artifacts: build container, GDAL/numcodecs versions, chained hashes, overview/block layout, reproducibility verdict.', 'KFM-P31-FEAT-0016', 'Pipeline steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('operational/GEOSPATIAL_QC_PANEL.md', 'Quick geospatial QC panel — fast inspectable surface for geometry / CRS / topology checks.', 'KFM-P31-FEAT-0017', 'Pipeline steward · Domain steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED')], [('domain/hydrology.md', 'Per-domain instance of §24.11 for hydrology: EvidenceRef resolution, rollback coverage, correction lead time, derivative invalidation, documentation drift.', 'Atlas v1.1 §24.11.1 / §24.11.2 / §24.11.5', 'Hydrology domain steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/soil.md', 'Per-domain instance of §24.11 for soil: evidence resolution, source-role drift, taxonomy-edition skew, MUKEY stability.', 'Atlas v1.1 §24.11.1 / §24.11.5', 'Soil domain steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/habitat.md', 'Per-domain instance of §24.11 for habitat: evidence integrity plus sensitive-lane gating on habitat × sensitive-species intersection.', 'Atlas v1.1 §24.11.1 / §24.11.3', 'Habitat domain steward · Sensitivity reviewer', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/fauna.md', 'Per-domain instance of §24.11 for fauna (T4 defaults): fail-closed rate, redaction coverage, rights-change response, side-channel audit.', 'Atlas v1.1 §24.11.3 / §24.11.1', 'Fauna domain steward · Sensitivity reviewer · Rights-holder rep', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/flora.md', 'Per-domain instance of §24.11 for flora (T4 defaults for poaching-vulnerable taxa): fail-closed, voucher coverage, poaching-pattern audit.', 'Atlas v1.1 §24.11.3 / §24.11.1', 'Flora domain steward · Sensitivity reviewer · Rights-holder rep', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/agriculture.md', 'Per-domain instance of §24.11 for agriculture: evidence resolution, NASS suppression-rule compliance, CDL taxonomy skew, irrigation classification confidence.', 'Atlas v1.1 §24.11.1 / §24.11.5', 'Agriculture domain steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/geology.md', 'Per-domain instance of §24.11 for geology / natural resources: source breadth, stratigraphic canonicalization, well-record identifiability gate.', 'Atlas v1.1 §24.11.1', 'Geology domain steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/atmosphere.md', 'Per-domain instance of §24.11 for atmosphere / air: source posture plus AI-surface forecasting cite-or-abstain, ABSTAIN by template, synthetic-claim incidence.', 'Atlas v1.1 §24.11.1 / §24.11.4', 'Atmosphere domain steward · AI-surface steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/hazards.md', 'Per-domain instance of §24.11 for hazards: rollback coverage, correction lead time, alert-authority DENY rate, derivative invalidation cascade.', 'Atlas v1.1 §24.11.2 / §24.11.1', 'Hazards domain steward · Release steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/roads-rail-trade.md', 'Per-domain instance of §24.11 for roads / rail / trade routes: source breadth, functional-class canonicalization, historical-corpus edition pinning; rolls up transit SLOs.', 'Atlas v1.1 §24.11.1 / §24.11.5', 'Roads-rail-trade domain steward · Source steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/settlements-infrastructure.md', 'Per-domain instance of §24.11 for settlements / infrastructure (critical-asset T4): fail-closed gate, redaction coverage, rollback coverage, service-area cascade.', 'Atlas v1.1 §24.11.3 / §24.11.2', 'Settlements-infrastructure domain steward · Sensitivity reviewer', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/archaeology.md', 'Per-domain instance of §24.11 for archaeology / cultural heritage (T4 defaults, sovereignty): sovereignty review presence, NAGPRA-flag completeness, side-channel audit.', 'Atlas v1.1 §24.11.3 / §24.11.1', 'Archaeology domain steward · Sensitivity reviewer · Sovereignty rep', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/people-dna-land.md', 'Per-domain instance of §24.11 for people / genealogy / DNA / land ownership (living-person T4, DNA T4): fail-closed, rights-change response time, AIReceipt presence, synthetic-claim incidence (target zero).', 'Atlas v1.1 §24.11.3 / §24.11.4 / §24.11.1', 'People-DNA-land domain steward · Sensitivity reviewer · AI-surface steward · Rights-holder rep', 'apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('domain/air/PM_SENSOR_CALIBRATION_REVIEW.md', 'PM-sensor trust scores, meteorology features, co-location windows, low-concentration safeguards.', 'KFM-P30-FEAT-0001', 'Atmosphere domain steward', 'apps/review-console/', 'CONFIRMED', 'PROPOSED')], [('observability/OPENTELEMETRY_STACK.md', 'CI/pipeline observability via OpenTelemetry Collector → Tempo (traces) + Mimir (metrics) + Loki (logs), one agent shape across runners.', 'KFM-P8-PROG-0026', 'Observability steward', 'OpenTelemetry stack (Tempo · Mimir · Loki)', 'CONFIRMED', 'PROPOSED'), ('observability/opentelemetry-stack.md', 'Lowercase OpenTelemetry stack spec path observed alongside `OPENTELEMETRY_STACK.md`; likely naming-convention duplicate requiring reconciliation.', 'NEEDS VERIFICATION — duplicate/naming reconciliation', 'Observability steward', 'OpenTelemetry stack (Tempo · Mimir · Loki)', 'CONFIRMED', 'NEEDS VERIFICATION'), ('observability/build-ci-health.md', 'Build and CI health dashboard specification; tracks workflow health, failing checks, and CI observability posture.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · CI steward', 'OpenTelemetry / CI dashboards', 'CONFIRMED', 'PROPOSED'), ('observability/energy-carbon-footprint.md', 'Energy/carbon footprint observability specification; tracks compute/resource telemetry where supported.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Sustainability steward', 'OpenTelemetry / external carbon telemetry', 'CONFIRMED', 'PROPOSED'), ('observability/focus-overlay-telemetry.md', 'Focus-overlay telemetry dashboard specification; tracks Focus Mode UI telemetry without exposing unsafe data.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Focus Mode steward', 'OpenTelemetry / apps/review-console/', 'CONFIRMED', 'PROPOSED'), ('observability/ingest-run-trace-coverage.md', 'Ingest-run trace coverage dashboard specification; tracks whether governed ingest runs emit trace coverage and correlation IDs.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Pipeline steward', 'OpenTelemetry stack', 'CONFIRMED', 'PROPOSED'), ('observability/openlineage-event-stream.md', 'OpenLineage event-stream dashboard specification; tracks pipeline lineage emission and stream health.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Lineage steward', 'OpenLineage / OpenTelemetry stack', 'CONFIRMED', 'PROPOSED'), ('observability/pmtiles-range-diagnostics.md', 'PMTiles range-diagnostics dashboard specification; tracks byte-range and tile-serving diagnostics.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Map/tile steward', 'Tile-serving observability stack', 'CONFIRMED', 'PROPOSED'), ('observability/service-uptime-latency.md', 'Service uptime and latency dashboard specification; tracks service SLO/SLA posture.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Platform steward', 'OpenTelemetry / service monitoring', 'CONFIRMED', 'PROPOSED'), ('observability/telemetry-contract-health.md', 'Telemetry contract health dashboard specification; tracks emitted telemetry against expected contracts.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Contract steward', 'OpenTelemetry / validation reports', 'CONFIRMED', 'PROPOSED'), ('observability/validator-orchestrator-health.md', 'Validator-orchestrator health dashboard specification; tracks orchestrator availability, validator outcomes, retries, and failure classes.', 'NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog', 'Observability steward · Validator steward', 'OpenTelemetry / validator reports', 'CONFIRMED', 'PROPOSED')])/`. |
| Running dashboard surfaces exist and read the named receipts. | NEEDS VERIFICATION | No running app, telemetry stack, receipt source, or validator output was inspected here. |
| `docs/dashboards/` is canonical placement under Directory Rules. | PROPOSED / NEEDS VERIFICATION | Dashboard README records placement drift / ADR need; this catalog does not resolve it. |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 3. Governance dashboards

Governance-health dashboards mirror Atlas v1.1 Ch. 24.11. They **report** posture; validators and policy gates **enforce**.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | File presence | Runtime status |
|---|---|---|---|---|---|---|
| [`governance/EVIDENCE_INTEGRITY.md`](governance/EVIDENCE_INTEGRITY.md) | EvidenceRef resolution, cite-or-abstain compliance, source-role drift, stale-source rate, quarantine throughput. | Atlas v1.1 §24.11.1 | Release / Source / AI surface stewards | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`governance/RELEASE_CORRECTION_ROLLBACK.md`](governance/RELEASE_CORRECTION_ROLLBACK.md) | Rollback-target coverage, correction lead time, derivative-invalidation coverage, rollback rehearsal rate, supersession lineage gaps. | Atlas v1.1 §24.11.2 | Release steward · Correction reviewer | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`governance/SENSITIVITY_RIGHTS.md`](governance/SENSITIVITY_RIGHTS.md) | Sensitive-lane fail-closed rate, RedactionReceipt coverage, review-aged-out incidence, rights-change response time, side-channel audit cadence. | Atlas v1.1 §24.11.3 | Sensitivity reviewer · Rights-holder representative | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`governance/AI_SURFACE_HEALTH.md`](governance/AI_SURFACE_HEALTH.md) | AIReceipt presence rate, ABSTAIN rate by template, DENY reason distribution, synthetic-claim incidence. | Atlas v1.1 §24.11.4 | AI surface steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`governance/DOCUMENTATION_DRIFT.md`](governance/DOCUMENTATION_DRIFT.md) | ADR completeness, drift register size, per-root README presence, atlas/supplement lineage clarity. | Atlas v1.1 §24.11.5 | Docs steward | `apps/review-console/` | CONFIRMED | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 4. Operational dashboards

Feed, artifact, and QC dashboards watch the pipeline's day-to-day health.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | File presence | Runtime status |
|---|---|---|---|---|---|---|
| [`operational/SLO_LIVE_FEEDS.md`](operational/SLO_LIVE_FEEDS.md) | Standards-first SLOs for live transit and other high-cadence feeds: freshness, schema validation, latency, deduplication, non-material suppression, agency license terms. | KFM-P11-FEAT-0002 | Source steward · Observability steward | `OpenTelemetry stack / apps/review-console/` | CONFIRMED | PROPOSED |
| [`operational/REALTIME_FEED_FRESHNESS.md`](operational/REALTIME_FEED_FRESHNESS.md) | Realtime feed health: schema validation, SLO freshness, canonical identity, partition output, promotion/hold state. | KFM-P31-FEAT-0015 | Source steward | `OpenTelemetry stack / apps/review-console/` | CONFIRMED | PROPOSED |
| [`operational/COG_ZARR_REPRODUCIBILITY.md`](operational/COG_ZARR_REPRODUCIBILITY.md) | Raster/datacube artifacts: build container, GDAL/numcodecs versions, chained hashes, overview/block layout, reproducibility verdict. | KFM-P31-FEAT-0016 | Pipeline steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`operational/GEOSPATIAL_QC_PANEL.md`](operational/GEOSPATIAL_QC_PANEL.md) | Quick geospatial QC panel — fast inspectable surface for geometry / CRS / topology checks. | KFM-P31-FEAT-0017 | Pipeline steward · Domain steward | `apps/review-console/` | CONFIRMED | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 5. Domain dashboards

Domain-specific dashboards live under `domain/` and must not become domain authority. They are dashboard specs that summarize domain governance-health posture.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | File presence | Runtime status |
|---|---|---|---|---|---|---|
| [`domain/hydrology.md`](domain/hydrology.md) | Per-domain instance of §24.11 for hydrology: EvidenceRef resolution, rollback coverage, correction lead time, derivative invalidation, documentation drift. | Atlas v1.1 §24.11.1 / §24.11.2 / §24.11.5 | Hydrology domain steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/soil.md`](domain/soil.md) | Per-domain instance of §24.11 for soil: evidence resolution, source-role drift, taxonomy-edition skew, MUKEY stability. | Atlas v1.1 §24.11.1 / §24.11.5 | Soil domain steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/habitat.md`](domain/habitat.md) | Per-domain instance of §24.11 for habitat: evidence integrity plus sensitive-lane gating on habitat × sensitive-species intersection. | Atlas v1.1 §24.11.1 / §24.11.3 | Habitat domain steward · Sensitivity reviewer | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/fauna.md`](domain/fauna.md) | Per-domain instance of §24.11 for fauna (T4 defaults): fail-closed rate, redaction coverage, rights-change response, side-channel audit. | Atlas v1.1 §24.11.3 / §24.11.1 | Fauna domain steward · Sensitivity reviewer · Rights-holder rep | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/flora.md`](domain/flora.md) | Per-domain instance of §24.11 for flora (T4 defaults for poaching-vulnerable taxa): fail-closed, voucher coverage, poaching-pattern audit. | Atlas v1.1 §24.11.3 / §24.11.1 | Flora domain steward · Sensitivity reviewer · Rights-holder rep | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/agriculture.md`](domain/agriculture.md) | Per-domain instance of §24.11 for agriculture: evidence resolution, NASS suppression-rule compliance, CDL taxonomy skew, irrigation classification confidence. | Atlas v1.1 §24.11.1 / §24.11.5 | Agriculture domain steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/geology.md`](domain/geology.md) | Per-domain instance of §24.11 for geology / natural resources: source breadth, stratigraphic canonicalization, well-record identifiability gate. | Atlas v1.1 §24.11.1 | Geology domain steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/atmosphere.md`](domain/atmosphere.md) | Per-domain instance of §24.11 for atmosphere / air: source posture plus AI-surface forecasting cite-or-abstain, ABSTAIN by template, synthetic-claim incidence. | Atlas v1.1 §24.11.1 / §24.11.4 | Atmosphere domain steward · AI-surface steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/hazards.md`](domain/hazards.md) | Per-domain instance of §24.11 for hazards: rollback coverage, correction lead time, alert-authority DENY rate, derivative invalidation cascade. | Atlas v1.1 §24.11.2 / §24.11.1 | Hazards domain steward · Release steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/roads-rail-trade.md`](domain/roads-rail-trade.md) | Per-domain instance of §24.11 for roads / rail / trade routes: source breadth, functional-class canonicalization, historical-corpus edition pinning; rolls up transit SLOs. | Atlas v1.1 §24.11.1 / §24.11.5 | Roads-rail-trade domain steward · Source steward | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/settlements-infrastructure.md`](domain/settlements-infrastructure.md) | Per-domain instance of §24.11 for settlements / infrastructure (critical-asset T4): fail-closed gate, redaction coverage, rollback coverage, service-area cascade. | Atlas v1.1 §24.11.3 / §24.11.2 | Settlements-infrastructure domain steward · Sensitivity reviewer | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/archaeology.md`](domain/archaeology.md) | Per-domain instance of §24.11 for archaeology / cultural heritage (T4 defaults, sovereignty): sovereignty review presence, NAGPRA-flag completeness, side-channel audit. | Atlas v1.1 §24.11.3 / §24.11.1 | Archaeology domain steward · Sensitivity reviewer · Sovereignty rep | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/people-dna-land.md`](domain/people-dna-land.md) | Per-domain instance of §24.11 for people / genealogy / DNA / land ownership (living-person T4, DNA T4): fail-closed, rights-change response time, AIReceipt presence, synthetic-claim incidence (target zero). | Atlas v1.1 §24.11.3 / §24.11.4 / §24.11.1 | People-DNA-land domain steward · Sensitivity reviewer · AI-surface steward · Rights-holder rep | `apps/review-console/` | CONFIRMED | PROPOSED |
| [`domain/air/PM_SENSOR_CALIBRATION_REVIEW.md`](domain/air/PM_SENSOR_CALIBRATION_REVIEW.md) | PM-sensor trust scores, meteorology features, co-location windows, low-concentration safeguards. | KFM-P30-FEAT-0001 | Atmosphere domain steward | `apps/review-console/` | CONFIRMED | PROPOSED |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 6. Observability dashboards

Observability dashboards specify telemetry and substrate visibility. They carry signals; they do not by themselves prove the underlying workload is healthy.

| Spec file | Documents | Source | Owner (PROPOSED) | Runs on (PROPOSED) | File presence | Runtime status |
|---|---|---|---|---|---|---|
| [`observability/OPENTELEMETRY_STACK.md`](observability/OPENTELEMETRY_STACK.md) | CI/pipeline observability via OpenTelemetry Collector → Tempo (traces) + Mimir (metrics) + Loki (logs), one agent shape across runners. | KFM-P8-PROG-0026 | Observability steward | `OpenTelemetry stack (Tempo · Mimir · Loki)` | CONFIRMED | PROPOSED |
| [`observability/opentelemetry-stack.md`](observability/opentelemetry-stack.md) | Lowercase OpenTelemetry stack spec path observed alongside `OPENTELEMETRY_STACK.md`; likely naming-convention duplicate requiring reconciliation. | NEEDS VERIFICATION — duplicate/naming reconciliation | Observability steward | `OpenTelemetry stack (Tempo · Mimir · Loki)` | CONFIRMED | NEEDS VERIFICATION |
| [`observability/build-ci-health.md`](observability/build-ci-health.md) | Build and CI health dashboard specification; tracks workflow health, failing checks, and CI observability posture. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · CI steward | `OpenTelemetry / CI dashboards` | CONFIRMED | PROPOSED |
| [`observability/energy-carbon-footprint.md`](observability/energy-carbon-footprint.md) | Energy/carbon footprint observability specification; tracks compute/resource telemetry where supported. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Sustainability steward | `OpenTelemetry / external carbon telemetry` | CONFIRMED | PROPOSED |
| [`observability/focus-overlay-telemetry.md`](observability/focus-overlay-telemetry.md) | Focus-overlay telemetry dashboard specification; tracks Focus Mode UI telemetry without exposing unsafe data. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Focus Mode steward | `OpenTelemetry / apps/review-console/` | CONFIRMED | PROPOSED |
| [`observability/ingest-run-trace-coverage.md`](observability/ingest-run-trace-coverage.md) | Ingest-run trace coverage dashboard specification; tracks whether governed ingest runs emit trace coverage and correlation IDs. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Pipeline steward | `OpenTelemetry stack` | CONFIRMED | PROPOSED |
| [`observability/openlineage-event-stream.md`](observability/openlineage-event-stream.md) | OpenLineage event-stream dashboard specification; tracks pipeline lineage emission and stream health. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Lineage steward | `OpenLineage / OpenTelemetry stack` | CONFIRMED | PROPOSED |
| [`observability/pmtiles-range-diagnostics.md`](observability/pmtiles-range-diagnostics.md) | PMTiles range-diagnostics dashboard specification; tracks byte-range and tile-serving diagnostics. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Map/tile steward | `Tile-serving observability stack` | CONFIRMED | PROPOSED |
| [`observability/service-uptime-latency.md`](observability/service-uptime-latency.md) | Service uptime and latency dashboard specification; tracks service SLO/SLA posture. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Platform steward | `OpenTelemetry / service monitoring` | CONFIRMED | PROPOSED |
| [`observability/telemetry-contract-health.md`](observability/telemetry-contract-health.md) | Telemetry contract health dashboard specification; tracks emitted telemetry against expected contracts. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Contract steward | `OpenTelemetry / validation reports` | CONFIRMED | PROPOSED |
| [`observability/validator-orchestrator-health.md`](observability/validator-orchestrator-health.md) | Validator-orchestrator health dashboard specification; tracks orchestrator availability, validator outcomes, retries, and failure classes. | NEEDS VERIFICATION — observed spec file; source card not yet reconciled in this catalog | Observability steward · Validator steward | `OpenTelemetry / validator reports` | CONFIRMED | PROPOSED |

> [!WARNING]
> `observability/OPENTELEMETRY_STACK.md` and `observability/opentelemetry-stack.md` both appear in accessible repo search. Treat this as a naming-convention and possible duplicate-spec reconciliation item until a steward chooses the canonical file and records a migration/supersession path.

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 7. Lifecycle states

Vocabulary for the **Runtime status** column:

| Status | Meaning |
|---|---|
| `PROPOSED` | Spec exists or is cataloged; no verified running implementation is claimed. Default for dashboard specs. |
| `NEEDS VERIFICATION` | Spec/file/running-surface relationship is unclear or requires steward reconciliation before it can be treated as stable. |
| `CONFIRMED` | Implementation evidence confirms the dashboard runs and reads the receipts named in the spec. Not used for runtime status in this refresh. |
| `SUPERSEDED` | Replaced by another spec; row keeps a forward link to its successor. |
| `RETIRED` | Dashboard decommissioned; spec kept for lineage. |

Vocabulary for the **File presence** column:

| File presence | Meaning |
|---|---|
| `CONFIRMED` | File path appeared in accessible repo evidence during this update. |
| `PROPOSED` | Planned path only; not observed. |
| `NEEDS VERIFICATION` | Path evidence is ambiguous, stale, or requires mounted checkout reconciliation. |

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

## 8. Open questions

- [ ] **CAT-OQ-01 — Catalog completeness CI.** Add a check that every `.md` under `docs/dashboards/{governance,operational,domain,observability}/` has a row here, excluding folder READMEs unless the policy explicitly requires README rows.
- [ ] **CAT-OQ-02 — Running-surface verification.** Confirm each "Runs on" value against mounted-repo state, receipts read, telemetry source, access control, and UI/API route.
- [ ] **CAT-OQ-03 — Owner reconciliation.** Resolve every PROPOSED owner against steward assignments before review.
- [ ] **CAT-OQ-04 — Placement drift / ADR.** Decide whether `docs/dashboards/` is canonicalized in Directory Rules, merged into `docs/reports/`, mirrored in `control_plane/`, or renamed/migrated.
- [ ] **CAT-OQ-05 — Observability expansion reconciliation.** Reconcile the older one-card observability README inventory with the 11 observed observability spec files cataloged here.
- [ ] **CAT-OQ-06 — OpenTelemetry duplicate naming.** Choose one canonical OpenTelemetry stack spec path and mark the other `SUPERSEDED`, `RETIRED`, or migrated via `git mv`.
- [ ] **CAT-OQ-07 — Runtime proof contract.** Define what evidence is sufficient to move a dashboard from `PROPOSED` to `CONFIRMED`: route, panel config, fixture, receipt source, policy gate, access test, screenshot/artifact, and rollback path.

[↑ back to top](#dashboard-catalog--docsdashboardsdashboard_catalogmd)

---

**Related docs:** [README.md](README.md) · [INDICATOR_CATALOG.md](INDICATOR_CATALOG.md) · [registers/DRIFT_REGISTER.md](../registers/DRIFT_REGISTER.md)

**Last updated:** 2026-06-11 · **Edition:** v0.2 (draft) · **Owners:** `<dashboards-stewards>` (PROPOSED)
