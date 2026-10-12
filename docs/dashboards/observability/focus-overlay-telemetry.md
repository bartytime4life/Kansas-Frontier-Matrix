<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-focus-overlay-telemetry
title: Focus Overlay Telemetry Conformance (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + frontend owner + sensitivity reviewer
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://card/p29-prog-0023                   # PROPOSED card: Focus Mode UI overlay telemetry
tags: [kfm, dashboards, observability, ui, focus-mode, overlay, telemetry, timeline]
notes:
  - Source card KFM-P29-PROG-0023 is PROPOSED in the corpus.
  - UI telemetry can carry user-identifying context (session ID, viewport extent) — T2 by default.
[/KFM_META_BLOCK_V2] -->

# Focus Overlay Telemetry Conformance

<!-- [doc: kfm://doc/dashboards-observability-focus-overlay-telemetry] -->
<a id="top"></a>

> Surfaces conformance of the Focus Mode UI overlay telemetry contract — timeline / contextual-panel sync events, viewport extent reporting, dropped-event rate, and per-session telemetry completeness — without surfacing per-user dimensional data.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / frontend owner" src="https://img.shields.io/badge/audience-SRE%20%2F%20frontend-blue">
  <img alt="Sensitivity: T2" src="https://img.shields.io/badge/sensitivity-T2-orange">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: KFM-P29-PROG-0023" src="https://img.shields.io/badge/source-KFM--P29--PROG--0023-purple">
</p>

> [!CAUTION]
> **Sensitive-content posture:** **T2 restricted**. UI telemetry can carry: session IDs, viewport coordinates that re-derive what the user was looking at, dwell time on T3+ artifacts. Session IDs are hashed at emission; viewport extents bucketed to coarse zoom; dwell-time on T3+ artifacts is suppressed (count-only, no per-artifact ID).

---

## 1. Scope

- **Source anchor:** KFM-P29-PROG-0023 *(Focus Mode UI overlay telemetry contract, PROPOSED)*.
- **Audience:** Frontend owner, observability steward, sensitivity reviewer.
- **Aggregation scope:** Per-session conformance rolled up to whole-fleet; per-overlay-type breakdown.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `focus.telemetry.contract_conformance` | % of overlay activations emitting all required telemetry keys | 100% | frontend telemetry adapter |
| `focus.telemetry.timeline_panel_sync_event_rate` | Rate of timeline ↔ contextual-panel sync events per session | non-zero on active sessions | same |
| `focus.telemetry.dropped_event_rate` | % of overlay events dropped before reaching the Collector | < 0.1% | same |
| `focus.telemetry.viewport_extent_emission_rate` | % of overlay activations reporting viewport extent (bucketed) | ≥ 99% | same |
| `focus.telemetry.t3_artifact_dwell_count` | Count-only dwell events on T3+ artifacts | tracking metric; per-artifact identity NOT emitted | same |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T2 restricted.
- **Redaction-at-emission rules:**
  - Session IDs hashed (HMAC with rotating per-day key) before leaving the browser.
  - Viewport extents bucketed to zoom ≤ 10 buckets; no raw lat/lng pairs.
  - Per-artifact IDs for T3+ artifacts suppressed; only the count metric survives.
  - Pointer-trail / mouse-movement traces never emitted.
- **Sampling policy:** 100% of conformance metrics; 10% sampling for non-sensitive overlay events; 0% for T3+ artifact-specific events (count-only).
- **Trace-body retention window:** Per Tempo policy.
- **Access control on dashboard:** Internal-only; T2 access group required.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Forbidden. UI telemetry aggregates can reveal which artifacts users dwell on, which is itself sensitive for T3+ content.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Frontend owner:** OWNER_TBD
- **Sensitivity reviewer:** OWNER_TBD *(required — T2+).*
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/focus-overlay/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry source:** Frontend telemetry adapter in `apps/<public-shell>/telemetry/focus/` *(PROPOSED path)*; OTel Collector receiver.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED)*.
- **Policy bundles:** `policy/observability/ui-telemetry-redaction/` *(PROPOSED; Pass 10 C5-06)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/sensitive-content-handling.md` *(t3-artifact-dwell-count rollups feed the doctrinal "is the UI leaking dwell signal" indicator).*
- **Per-domain breakdown:** N/A *(per-domain breakdown forbidden — would defeat redaction).*
- **Release-lifecycle view:** `docs/dashboards/release/ui-by-release.md` *(PROPOSED sibling, with same redaction rules).*
- **Related observability specs:** `telemetry-contract-health.md` *(this is the UI-side instance of the same conformance pattern).*

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: Focus Mode UI redesign, telemetry contract revision, sensitivity-tier reclassification of any surfaced artifact class, change in session-ID hashing scheme.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-FOCUS-01** — What is the rotation period for the session-ID HMAC key? Listed as per-day PROPOSED.
- **OPEN-DASH-OBS-FOCUS-02** — Should dwell-time on T3+ artifacts be suppressed even at count level if the count itself could leak via small-cohort inference?

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P29-PROG-0023 | PROPOSED in corpus | §1 scope, §2 signals. |
| Atlas v1.1 §24.5 (Sensitivity Tiers) | CONFIRMED | §3 default-deny T3+. |
| Atlas v1.1 §24.10 (Risk Register — UI dwell inference) | CONFIRMED | §3, §4 dwell-inference risk. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template; §10 sensitive-content posture. |

<sub>Specification only. Behind the trust membrane; T2-default; dwell-on-T3+ is count-only.</sub>
