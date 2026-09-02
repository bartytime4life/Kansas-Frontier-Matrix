<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-opentelemetry-stack
title: OpenTelemetry Stack Health (CONFIRMED-stack system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + infra owner
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://doc/standard-opentelemetry           # PROPOSED: docs/standards/OPENTELEMETRY.md (OPEN-DASH-OBS-08)
  - kfm://card/p8-prog-0026                    # CONFIRMED card: OTel CI observability stack
tags: [kfm, dashboards, observability, opentelemetry, collector, tempo, mimir, loki]
notes:
  - Source card KFM-P8-PROG-0026 (Pass 32 baseline) is CONFIRMED in the corpus.
  - The stack itself (Collector + Tempo + Mimir + Loki) is CONFIRMED; this dashboard is PROPOSED.
  - A pre-existing companion file `OPENTELEMETRY_STACK.md` (UPPER_SNAKE_CASE) is preserved as
    a separate authored artifact; this spec follows the parent README's kebab-case convention.
[/KFM_META_BLOCK_V2] -->

# OpenTelemetry Stack Health

<!-- [doc: kfm://doc/dashboards-observability-opentelemetry-stack] -->
<a id="top"></a>

> Surfaces the health of KFM's CI observability stack — OTel Collector ingest rate, Tempo / Mimir / Loki query latency and uptime, single-agent-shape conformance across runners.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / infra" src="https://img.shields.io/badge/audience-SRE%20%2F%20infra-blue">
  <img alt="Sensitivity: T0" src="https://img.shields.io/badge/sensitivity-T0-green">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: KFM-P8-PROG-0026 (CONFIRMED)" src="https://img.shields.io/badge/source-KFM--P8--PROG--0026-success">
</p>

> [!CAUTION]
> **Sensitive-content posture:** T0 — only stack-health metrics (uptime, ingest rate, queue depth, query latency). No span bodies, log lines, or metric labels are surfaced by this dashboard. If a metric label could carry sensitive content (e.g., a `domain` label sourced from an archaeology emitter), bucket it before display.

---

## 1. Scope

- **Source anchor:** KFM-P8-PROG-0026 *(CONFIRMED in corpus)* — OTel Collector + Tempo (traces) + Mimir (metrics) + Loki (logs); single agent shape across runners.
- **Audience:** SRE on-call, observability steward, infra owner.
- **Aggregation scope:** Stack-wide; per-backend health; per-runner agent conformance.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `otel.collector.spans_received` | Spans ingested by Collector (per second) | > 0 during active CI; non-zero during business hours | OTel Collector self-telemetry |
| `otel.collector.queue_depth` | Receiver queue depth | p95 < 50% of configured limit | OTel Collector self-telemetry |
| `otel.collector.dropped_spans` | Spans dropped due to queue overflow or processor failure | 0 over 1h window | OTel Collector self-telemetry |
| `tempo.query.p95_latency_ms` | Tempo trace lookup p95 | < 500ms | Tempo self-telemetry |
| `mimir.query.p95_latency_ms` | Mimir metric query p95 | < 1000ms | Mimir self-telemetry |
| `loki.query.p95_latency_ms` | Loki log query p95 | < 2000ms | Loki self-telemetry |
| `otel.runners.agent_shape_conformance` | % of CI runners reporting the canonical agent shape | 100% | runner-fleet inventory + Collector handshake |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T0 (stack-internal metrics; no domain content).
- **Redaction-at-emission rules:** N/A — self-telemetry only.
- **Sampling policy:** 100% of stack-health signals.
- **Trace-body retention window:** N/A — no trace bodies surfaced.
- **Access control on dashboard:** Internal-only (SRE + observability steward).

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** A derived public service-status page MAY summarize "observability backend: healthy / degraded / down" without exposing per-component metrics. Such a derivation requires explicit sensitivity-reviewer sign-off per parent README §11.
- **Aggregation/redaction if surfaced publicly:** Tri-state rollup only (healthy / degraded / down); no per-runner, per-backend, or per-component detail.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Infra owner:** OWNER_TBD
- **Sensitivity reviewer:** Not required *(T0 only)*; required if any public derivation is attempted.
- **Implementation owner:** OWNER_TBD *(SRE team owning the OTel stack)*

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** Grafana *(canonical for OTel stack)* — internal URL pattern `https://grafana.internal.kfm/d/otel-stack-health` *(PROPOSED; NEEDS VERIFICATION)*; alternatively `apps/admin/observability/otel-stack/`.
- **Telemetry source:** OTel Collector self-telemetry endpoint; Tempo / Mimir / Loki self-telemetry.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED; OPEN-DASH-OBS-08)*.
- **Policy bundles:** `policy/observability/agent-shape/` *(PROPOSED; Pass 10 C5-06)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** None directly. A degraded stack is surfaced through `telemetry-contract-health.md` (missing-fields counter spikes).
- **Per-domain breakdown:** N/A — stack health is whole-stack.
- **Release-lifecycle view:** `docs/dashboards/release/observability-stack-by-release.md` *(PROPOSED sibling, optional)*.
- **Related observability specs:** `telemetry-contract-health.md`, `build-ci-health.md` *(workflow-side rollup of the same stack)*.
- **Pre-existing companion:** `OPENTELEMETRY_STACK.md` *(UPPER_SNAKE_CASE; preserved from earlier authorship; coexists with this kebab-case spec; OPEN-DASH-OBS-STACK-01 — reconcile or supersede)*.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: OTel Collector / Tempo / Mimir / Loki version bump (per parent README §13 stack-version sync), agent-shape contract change, runner-fleet topology change.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-STACK-01** — Reconcile this kebab-case spec with the pre-existing `OPENTELEMETRY_STACK.md`. Supersede, merge, or define each as a distinct artifact?
- **OPEN-DASH-OBS-STACK-02** — Should the derived public service-status tri-state rollup live here or in a `release/` sibling?

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P8-PROG-0026 | **CONFIRMED** in corpus | §1, §2 (Collector + Tempo + Mimir + Loki), §8 stack-version sync. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| Atlas v1.1 §24.10 (Risk Register) | CONFIRMED | §3, §4 sensitive-content + exposure posture. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template alignment; §13 sync rules. |

<sub>Specification only. The stack itself is CONFIRMED in the corpus; the dashboard is PROPOSED. Behind the trust membrane.</sub>
