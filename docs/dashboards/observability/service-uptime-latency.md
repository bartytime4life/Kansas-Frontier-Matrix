<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-service-uptime-latency
title: Service Uptime & Latency (governed-API SLO spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + service owner
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://doc/standard-opentelemetry           # PROPOSED
  - kfm://operating-law-invariant-1            # public clients use governed interfaces
tags: [kfm, dashboards, observability, uptime, latency, slo, governed-api]
notes:
  - Anchored to operating-law invariant 1 — public clients consume governed interfaces, not canonical stores.
  - Sensitive-content posture is T1 by default; per-endpoint labels MUST NOT encode T2+ identifiers.
[/KFM_META_BLOCK_V2] -->

# Service Uptime & Latency

<!-- [doc: kfm://doc/dashboards-observability-service-uptime-latency] -->
<a id="top"></a>

> Surfaces uptime, p95/p99 latency, and error-rate posture for the governed API surfaces that public clients consume — per endpoint, per region, decomposed by error class.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / service owner" src="https://img.shields.io/badge/audience-SRE%20%2F%20service%20owner-blue">
  <img alt="Sensitivity: T1" src="https://img.shields.io/badge/sensitivity-T1-yellow">
  <img alt="Public-exposure: INTERNAL (rollup exception)" src="https://img.shields.io/badge/public--exposure-INTERNAL%20%28rollup%20OK%29-orange">
  <img alt="Source: governed-API SLO" src="https://img.shields.io/badge/source-governed--API%20SLO-informational">
</p>

> [!CAUTION]
> **Sensitive-content posture:** T1 internal. Endpoint paths surfaced here MUST NOT embed T2+ identifiers (no `/api/v1/archaeology-sites/{precise-coords}/...` in labels). Per-tenant or per-user dimensional cuts forbidden without sensitivity-reviewer sign-off.

---

## 1. Scope

- **Source anchor:** Governed-API SLO (operating-law invariant 1 — *public clients and normal UI surfaces use governed interfaces, not canonical/internal stores*).
- **Audience:** SRE on-call, service owner, observability steward.
- **Aggregation scope:** Per endpoint × per region × per error class.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `api.uptime.rolling_30d` | 30-day rolling uptime per endpoint | ≥ 99.9% (governed-API SLO; PROPOSED threshold) | service self-telemetry → OTel Collector |
| `api.latency.p95_ms` | Per-endpoint p95 latency | < 500ms for read endpoints; < 1500ms for resolver endpoints | same |
| `api.latency.p99_ms` | Per-endpoint p99 latency | < 1500ms read; < 4000ms resolver | same |
| `api.error_rate_5xx` | 5xx error rate per endpoint | < 0.1% | same |
| `api.error_rate_4xx` | 4xx error rate (decomposed by class) | Stable per-endpoint baseline; alert on doubling | same |
| `api.evidence_ref_resolver.p95_ms` | EvidenceRef resolver p95 latency | < 800ms | resolver self-telemetry |
| `api.governed_surface_only_violations` | Requests that bypassed the governed surface | 0 | edge audit |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T1 internal.
- **Redaction-at-emission rules:**
  - Path-parameter values stripped from endpoint labels (e.g., `/api/v1/sites/{id}` not `/api/v1/sites/12345`).
  - Per-tenant or per-user dimensional labels suppressed by default.
  - Query-string contents never logged.
- **Sampling policy:** 100% of aggregate metrics; trace sampling per OTel Collector config (PROPOSED).
- **Trace-body retention window:** Per Tempo policy.
- **Access control on dashboard:** Internal-only.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** A **public service-status page** MAY be derived showing per-surface uptime tri-state (operational / degraded / outage) — per parent README §11. This is the only documented exception in this folder so far and is contingent on OPEN-DASH-OBS-05.
- **Aggregation/redaction if surfaced publicly:** Per-endpoint p95 numbers, per-region detail, and error-rate decomposition are all **internal-only**; the public page is tri-state per surface, no quantities.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Service owner:** OWNER_TBD *(per governed surface)*
- **Sensitivity reviewer:** Required only for the public-derivation exception.
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** Grafana — `https://grafana.internal.kfm/d/governed-api-slo` *(PROPOSED; NEEDS VERIFICATION)*; alternative `apps/admin/observability/service-slo/`.
- **Telemetry source:** Service-level OTel SDK; edge audit emitter.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED)*.
- **Policy bundles:** `policy/observability/governed-surface-only/` *(PROPOSED; Pass 10 C5-06; enforces invariant 1).*

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/evidence-and-source.md` *(EvidenceRef resolver SLO informs the doctrinal "is provenance reachable" indicator).*
- **Per-domain breakdown:** N/A *(service surfaces are domain-agnostic at the governed-API layer).*
- **Release-lifecycle view:** `docs/dashboards/release/slo-burn-by-release.md` *(PROPOSED sibling).*
- **Related observability specs:** `pmtiles-range-diagnostics.md` *(tile-serving sub-surface);* `opentelemetry-stack.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: SLO threshold revision, addition of a new governed endpoint, error-budget exhaustion event, sensitivity reclassification of any path parameter.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-SLO-01** — Should the public service-status page derivation live as its own spec (e.g., `docs/dashboards/public/service-status.md` in a new sibling lane) rather than as an exception clause here? Relates to OPEN-DASH-OBS-05.
- **OPEN-DASH-OBS-SLO-02** — What is the canonical SLO percentage and error budget per governed endpoint? Listed as 99.9% PROPOSED; needs ratification.
- **OPEN-DASH-OBS-SLO-03** — Where do per-region SLOs live if KFM goes multi-region — here, or in a per-region sub-spec?

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Operating-law invariant 1 (governed interfaces) | CONFIRMED (KFM operating contract) | §1 scope; §2 governed-surface-only violations signal; §6 policy bundle. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| Atlas v1.1 §24.5 (Sensitivity Tiers) | CONFIRMED | §3 path-label redaction. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template; §11 public-exposure exception path. |

<sub>Specification only. The public service-status page exception is the **only** exposure exception in this folder; everything else stays behind the trust membrane.</sub>
