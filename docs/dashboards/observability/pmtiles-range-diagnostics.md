<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-pmtiles-range-diagnostics
title: PMTiles Range Diagnostics (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + tile-serving owner + sensitivity reviewer
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://card/p32-feat-0013                   # PROPOSED card: PMTiles range diagnostics
tags: [kfm, dashboards, observability, pmtiles, tiles, range, cache, http]
notes:
  - Source card KFM-P32-FEAT-0013 is PROPOSED in the corpus.
  - Sensitive-content concern is bounding-box queries — high-zoom requests near T3+ coordinates leak coordinates via access patterns.
[/KFM_META_BLOCK_V2] -->

# PMTiles Range Diagnostics

<!-- [doc: kfm://doc/dashboards-observability-pmtiles-range-diagnostics] -->
<a id="top"></a>

> Surfaces health of PMTiles byte-range serving — tile-request range coverage, cache hit rate, byte-range failure rate, p95 fetch duration, suppressed-region access attempts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / tile-serving owner" src="https://img.shields.io/badge/audience-SRE%20%2F%20tile--serving-blue">
  <img alt="Sensitivity: T2" src="https://img.shields.io/badge/sensitivity-T2-orange">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: KFM-P32-FEAT-0013" src="https://img.shields.io/badge/source-KFM--P32--FEAT--0013-purple">
</p>

> [!CAUTION]
> **Sensitive-content posture:** **T2 restricted**. Tile coordinates (z/x/y) at high zoom near T3+ regions (archaeology sites, rare-species coordinates, critical infrastructure) are themselves sensitive — request-pattern dashboards can reverse-engineer coordinates even without raw payloads. This dashboard bins coordinates at zoom ≤ 10 by default; finer-grained per-tile detail requires sensitivity-reviewer sign-off.

---

## 1. Scope

- **Source anchor:** KFM-P32-FEAT-0013 *(PMTiles range diagnostics, PROPOSED)*.
- **Audience:** Tile-serving owner, SRE on-call, observability steward.
- **Aggregation scope:** Per-archive PMTiles file; cache-tier rollup; coarse-zoom coordinate buckets only.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `pmtiles.range.request_count` | Byte-range requests per archive | non-zero per active archive | tile-serving adapter |
| `pmtiles.range.coverage_completeness` | % of expected tile ranges actually fetchable | ≥ 99.9% | archive index integrity probe |
| `pmtiles.range.cache_hit_rate` | CDN / edge cache hit rate | ≥ 90% on hot archives | cache adapter |
| `pmtiles.range.failure_rate` | 4xx/5xx on byte-range requests | < 0.5% | tile-serving adapter |
| `pmtiles.range.p95_fetch_ms` | p95 single-tile fetch duration | < 400ms | tile-serving adapter |
| `pmtiles.range.suppressed_region_access_attempts` | Requests for tiles in a deny-listed sensitive region | 0 *(non-zero is an incident)* | policy-aware tile gate |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T2 restricted.
- **Redaction-at-emission rules:**
  - Per-tile (z/x/y) detail bucketed to zoom ≤ 10 in dashboard surfacing.
  - Tile IDs covering T3+ regions never displayed in coordinate form; rendered as opaque IDs.
  - Per-client-IP dimensional cuts suppressed.
- **Sampling policy:** 100% of aggregate metrics; per-tile detail sampled at 1% with sensitive-region exclusion.
- **Trace-body retention window:** Per tile-serving adapter config.
- **Access control on dashboard:** Internal-only; T2 access group required.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Forbidden. Tile access patterns are a known archaeology-location-disclosure surface.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Tile-serving owner:** OWNER_TBD
- **Sensitivity reviewer:** OWNER_TBD *(required — T2+, with archaeology/rare-species concern).*
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/pmtiles-range/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry source:** Tile-serving adapter self-telemetry; CDN / edge logs (redacted at intake).
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED)*; PMTiles spec (external).
- **Policy bundles:** `policy/observability/tile-suppression/` *(PROPOSED; Pass 10 C5-06; encodes the deny-list of sensitive regions).*

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/sensitive-content-handling.md` *(suppressed-region attempts feed the doctrinal "are we leaking" indicator)*.
- **Per-domain breakdown:** `docs/dashboards/domain/archaeology.md`, `docs/dashboards/domain/fauna-flora.md` *(per-domain tile health subsumed there — with the same coordinate-bucketing rule).*
- **Release-lifecycle view:** `docs/dashboards/release/tiles-by-release.md` *(PROPOSED sibling).*
- **Related observability specs:** `service-uptime-latency.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: New PMTiles archive published, tile-suppression deny-list update, CDN/edge topology change, sensitivity reclassification of any covered region.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-PMTILES-01** — What is the canonical zoom-bucket cutoff for safe display? Listed as zoom ≤ 10 PROPOSED.
- **OPEN-DASH-OBS-PMTILES-02** — How is "suppressed region access attempts" alerted on — page on first, or rate-threshold?

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P32-FEAT-0013 | PROPOSED in corpus | §1, §2 signals. |
| Atlas v1.1 §24.5 (Sensitivity Tiers) | CONFIRMED | §3 default-deny on high-zoom near-T3+. |
| Atlas v1.1 §24.10 (Risk Register — coordinates leakage) | CONFIRMED | §3, §4 access-pattern risk. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 tile-suppression policy bundle. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template; §10 sensitive-content posture. |

<sub>Specification only. Tile-access patterns are sensitive even without payloads. Behind the trust membrane; T2-default; zoom-bucketed.</sub>
