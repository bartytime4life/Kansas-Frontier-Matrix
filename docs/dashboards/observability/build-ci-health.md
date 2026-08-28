<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-build-ci-health
title: Build & CI Health (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + CI owner
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://card/p8-prog-0026                    # CONFIRMED: OTel CI observability stack
tags: [kfm, dashboards, observability, ci, build, workflow, runners]
notes:
  - Workflow-side rollup of the same stack as opentelemetry-stack.md.
  - Focus is build/CI runner conformance to the single-agent shape, plus build-job health metrics.
[/KFM_META_BLOCK_V2] -->

# Build & CI Health

<!-- [doc: kfm://doc/dashboards-observability-build-ci-health] -->
<a id="top"></a>

> Surfaces CI workflow health — build pass-rate, p95 build wallclock, runner conformance to the canonical single-agent OTel shape, telemetry sampling-rate compliance per workflow.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / CI owner" src="https://img.shields.io/badge/audience-SRE%20%2F%20CI%20owner-blue">
  <img alt="Sensitivity: T0" src="https://img.shields.io/badge/sensitivity-T0-green">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: KFM-P8-PROG-0026 (CONFIRMED)" src="https://img.shields.io/badge/source-KFM--P8--PROG--0026-success">
</p>

> [!CAUTION]
> **Sensitive-content posture:** T0. Workflow names, job names, and runner IDs are not domain content. If a workflow name encodes a sensitive dataset (e.g., `build-archaeology-private-bundle`), redact to `build-domain-private-bundle` at emission.

---

## 1. Scope

- **Source anchor:** KFM-P8-PROG-0026 *(CONFIRMED in corpus)* — workflow-side rollup of the OTel stack (Collector + Tempo + Mimir + Loki); single agent shape across CI runners.
- **Audience:** CI owner, SRE on-call, observability steward.
- **Aggregation scope:** Per workflow × per runner × per branch class (main / release / PR).

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `ci.workflow.pass_rate_24h` | % of workflow runs passing in 24h window | ≥ 95% on main; ≥ 70% on PR | CI runner telemetry |
| `ci.workflow.p95_wallclock_seconds` | p95 end-to-end workflow wallclock | per-workflow budget *(PROPOSED)* | same |
| `ci.runner.agent_shape_conformance` | % of CI runners reporting the canonical OTel agent shape | 100% | runner-fleet inventory + Collector handshake |
| `ci.workflow.sampling_rate_compliance` | % of workflows whose sampling rate matches the per-class policy | 100% | OTel SDK config check |
| `ci.runner.flake_rate` | % of jobs failing then passing on retry | < 5% *(PROPOSED)* | retry telemetry |
| `ci.workflow.telemetry_emit_rate` | % of workflow runs emitting at least one OTel span | 100% | Collector self-telemetry |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T0.
- **Redaction-at-emission rules:** Workflow names and job names with sensitive substrings replaced at emission.
- **Sampling policy:** 100% of workflow-level metrics.
- **Trace-body retention window:** Per Tempo policy.
- **Access control on dashboard:** Internal-only.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Forbidden by default; "CI green / yellow / red" badge on a public README is acceptable if it derives from a CI provider's own public-build badge, not from this dashboard.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **CI owner:** OWNER_TBD
- **Sensitivity reviewer:** Not required *(T0 only)*.
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** Grafana — `https://grafana.internal.kfm/d/ci-health` *(PROPOSED; NEEDS VERIFICATION)*; alternative `apps/admin/observability/ci-health/`.
- **Telemetry source:** CI runner OTel SDK; Collector self-telemetry.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED)*.
- **Policy bundles:** `policy/observability/agent-shape/`, `policy/observability/sampling-rate/` *(PROPOSED; Pass 10 C5-06)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/release-readiness.md` *(workflow pass-rate feeds the doctrinal "is the release green" indicator).*
- **Per-domain breakdown:** N/A.
- **Release-lifecycle view:** `docs/dashboards/release/ci-by-release.md` *(PROPOSED sibling).*
- **Related observability specs:** `opentelemetry-stack.md` *(stack side of the same coverage);* `validator-orchestrator-health.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: CI provider change, runner-fleet topology change, agent-shape contract change, addition of a new workflow class.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-CI-01** — What is the per-workflow wallclock budget set to? Listed as PROPOSED.
- **OPEN-DASH-OBS-CI-02** — Is flake-rate a paging signal or a trend-only signal?

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P8-PROG-0026 | **CONFIRMED** in corpus | §1 scope, §2 agent-shape / sampling-rate signals. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template. |

<sub>Specification only. Behind the trust membrane.</sub>
