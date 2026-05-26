<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-energy-carbon-footprint
title: Energy / Carbon Footprint (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + sustainability owner
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://card/p20-feat-0007                   # PROPOSED card: telemetry contract incl. energy/carbon
tags: [kfm, dashboards, observability, energy, carbon, sustainability, telemetry]
notes:
  - Source card KFM-P20-FEAT-0007 bundles energy/carbon with telemetry contract health.
  - OPEN-DASH-OBS-07 flags possible merger with telemetry-contract-health.md; treated as separate here pending ratification.
[/KFM_META_BLOCK_V2] -->

# Energy / Carbon Footprint

<!-- [doc: kfm://doc/dashboards-observability-energy-carbon-footprint] -->
<a id="top"></a>

> Surfaces per-run and rolled-up energy (joules) and carbon (gCO₂eq) telemetry — per CI workflow, per pipeline run, per package — with trend analysis and budget tracking.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / sustainability owner" src="https://img.shields.io/badge/audience-SRE%20%2F%20sustainability-blue">
  <img alt="Sensitivity: T0" src="https://img.shields.io/badge/sensitivity-T0-green">
  <img alt="Public-exposure: INTERNAL (rollup MAY be public)" src="https://img.shields.io/badge/public--exposure-INTERNAL%20%28rollup%20MAY%29-orange">
  <img alt="Source: KFM-P20-FEAT-0007" src="https://img.shields.io/badge/source-KFM--P20--FEAT--0007-purple">
</p>

> [!CAUTION]
> **Sensitive-content posture:** T0. Energy/carbon numbers themselves are not domain content. **However:** per-workflow energy can reveal which datasets are large or which validators are slow; per-package detail is internal-only by default. Whole-fleet monthly rollup MAY be published as a sustainability report.

---

## 1. Scope

- **Source anchor:** KFM-P20-FEAT-0007 *(PROPOSED card)* — per-run energy & carbon telemetry; rollup view.
- **Audience:** Sustainability owner, observability steward, infra-budget owner.
- **Aggregation scope:** Per run × per workflow × per package; daily / weekly / monthly / quarterly rollups.

> [!NOTE]
> **Granularity decision pending.** OPEN-DASH-OBS-07 in the parent README asks whether this should be a first-class spec or a sub-panel of `telemetry-contract-health.md` (which is where P20-FEAT-0007 bundles it). Treated as separate here pending ratification.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `energy.per_run.joules` | Energy estimate per CI/pipeline run | Tracked; alert on > 2× rolling-30d-median for the same workflow | `runtime/observability/energy-adapter/` *(PROPOSED)* |
| `carbon.per_run.grams_co2eq` | Carbon estimate per run | Tracked; alert on > 2× rolling median | same |
| `energy.daily.joules_total` | Daily energy across all workflows | Tracking metric | rollup processor |
| `carbon.daily.grams_co2eq_total` | Daily carbon across all workflows | Tracking metric; quarterly budget *(PROPOSED)* | rollup processor |
| `energy.coverage.runs_with_estimate_rate` | % of runs producing a non-null energy estimate | ≥ 99% | telemetry-contract validator |
| `energy.per_package.joules_p95` | p95 energy per package over 7d | Tracked per package | per-package adapter |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T0.
- **Redaction-at-emission rules:** N/A *(numeric metrics only)*.
- **Sampling policy:** 100%.
- **Trace-body retention window:** Per Mimir policy.
- **Access control on dashboard:** Internal for per-package / per-workflow detail; whole-fleet rollup MAY be made public.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL for per-package / per-workflow detail.
- **Documented exceptions:** Whole-fleet **monthly or quarterly** energy and carbon rollups MAY be published as part of a sustainability report, with no per-workflow / per-package detail. Requires sustainability-owner sign-off.
- **Aggregation/redaction if surfaced publicly:** Monthly+ rollups only; no per-workflow detail; no per-package detail; no per-runner detail.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Sustainability owner:** OWNER_TBD
- **Sensitivity reviewer:** Required only for public-rollup exception.
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/energy-carbon/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry source:** `runtime/observability/energy-adapter/` *(PROPOSED)*; per-package energy emitters.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED)*; external sustainability accounting standard *(NEEDS VERIFICATION — methodology choice)*.
- **Policy bundles:** `policy/observability/energy-coverage/` *(PROPOSED; Pass 10 C5-06; enforces non-null per-run energy)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** N/A *(energy/carbon is infra-posture, not doctrine-posture)*.
- **Per-domain breakdown:** Not by default — per-package, not per-domain.
- **Release-lifecycle view:** `docs/dashboards/release/energy-by-release.md` *(PROPOSED sibling; per-release energy attribution)*.
- **Related observability specs:** `telemetry-contract-health.md` *(possible merger per OPEN-DASH-OBS-07);* `build-ci-health.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: Sustainability accounting methodology change, energy-adapter SDK bump, addition of a new workflow class, quarterly budget breach.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-ENERGY-01** — Merge with `telemetry-contract-health.md` (inherits OPEN-DASH-OBS-07 from parent)?
- **OPEN-DASH-OBS-ENERGY-02** — What sustainability accounting methodology applies? (SCI / GHG Protocol / other.)
- **OPEN-DASH-OBS-ENERGY-03** — What is the quarterly carbon budget? Listed PROPOSED.

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P20-FEAT-0007 | PROPOSED in corpus | §1 scope, §2 signals, §9 OPEN-DASH-OBS-ENERGY-01. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template; §11 public-exposure exception path; OPEN-DASH-OBS-07. |

<sub>Specification only. Per-package / per-workflow detail is internal; monthly+ whole-fleet rollup MAY be public with sustainability-owner sign-off.</sub>
