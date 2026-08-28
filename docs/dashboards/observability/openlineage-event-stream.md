<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-openlineage-event-stream
title: OpenLineage Event Stream Health (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + infra owner + sensitivity reviewer
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://doc/standard-openlineage             # PROPOSED: docs/standards/OPENLINEAGE.md (OPEN-DR-05)
  - kfm://card/c1-05                           # CONFIRMED card: OpenLineage events end-to-end
  - kfm://card/p15-prog-0006                   # PROPOSED card: pipeline OTel root trace
tags: [kfm, dashboards, observability, openlineage, lineage, facets, events]
notes:
  - Source card C1-05 (Pass 10) is CONFIRMED in the corpus.
  - Facet vocabulary is "still evolving" per source; KFM-specific facets are namespaced.
  - High-risk surface for sensitive content — input/output dataset names can carry T2+ identifiers.
[/KFM_META_BLOCK_V2] -->

# OpenLineage Event Stream Health

<!-- [doc: kfm://doc/dashboards-observability-openlineage-event-stream] -->
<a id="top"></a>

> Surfaces the health of the OpenLineage event stream — START/COMPLETE event pairing, facet completeness, backend ingestion lag, and KFM-specific facet conformance.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / lineage steward" src="https://img.shields.io/badge/audience-SRE%20%2F%20lineage%20steward-blue">
  <img alt="Sensitivity: T2" src="https://img.shields.io/badge/sensitivity-T2-orange">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: C1-05 (CONFIRMED)" src="https://img.shields.io/badge/source-C1--05-success">
</p>

> [!CAUTION]
> **Sensitive-content posture:** **T2 restricted** by default. Lineage `inputs`/`outputs` facets can name datasets that, in cross-lane joins, expose sensitive identifiers (person-parcel, archaeology site, rare-species coordinate). Field-level redaction applies at emission: dataset names are replaced with content-addressed digests when the upstream package is T3+ (Atlas §24.5).

---

## 1. Scope

- **Source anchor:** **C1-05** (Pass 10, CONFIRMED) — START/COMPLETE events with facets (`job`, `run`, `inputs`, `outputs`, `spec_hash`, `inputs_hash`, `policy_labels`, `dataset_version`, `quality_status`, `receiptRef`). Plus KFM-P15-PROG-0006 (pipeline OTel root trace anchor).
- **Audience:** Lineage steward, observability steward, sensitivity reviewer.
- **Aggregation scope:** Event-stream-wide; per-job; per-namespace.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `openlineage.events.start_complete_pair_rate` | % of jobs with matched START/COMPLETE within retention | ≥ 99.5% over 24h | `runtime/observability/openlineage-emitter/` *(PROPOSED)* |
| `openlineage.events.orphan_start_count` | START events without COMPLETE within SLA window | 0 over 1h | same |
| `openlineage.facets.required_present_rate` | % of events with all required KFM facets | 100% | same |
| `openlineage.facets.receiptRef_resolves_rate` | % of `receiptRef` facets resolving to a real receipt | ≥ 99.9% | receipt resolver |
| `openlineage.backend.ingest_lag_seconds` | Lag between event emission and backend availability | p95 < 5s | OpenLineage backend self-telemetry |
| `openlineage.dataset.redaction_violations` | Events naming T3+ datasets without content-addressed-digest substitution | 0 | redaction-enforcement processor |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** **T2 restricted**. Conformance counts are T0; but the underlying events that feed those counts may carry T2+ identifiers. Dashboard access controls match T2 rules.
- **Redaction-at-emission rules:**
  - Dataset names from packages classified T3+ MUST be replaced with content-addressed digests at the OpenLineage emitter — never raw.
  - `job.namespace` MUST NOT encode location coordinates, person identifiers, or DNA sample IDs.
  - `inputs`/`outputs` MUST use the namespaced KFM facet for sensitivity tier (`kfm.policy.sensitivity_tier`).
- **Sampling policy:** 100% of conformance metrics; 0% of raw event bodies surfaced in this dashboard.
- **Trace-body retention window:** Per backend policy; not set by this spec.
- **Access control on dashboard:** Internal-only; T2 access group required.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL. Never linked from public surfaces.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Forbidden. Lineage event metrics are not safe to publish even in aggregate without case-by-case sensitivity-reviewer sign-off, because aggregation patterns themselves can leak (e.g., "events for the archaeology namespace spiked at 02:00").

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Infra owner:** OWNER_TBD
- **Sensitivity reviewer:** OWNER_TBD *(required — T2+ default).*
- **Implementation owner:** OWNER_TBD *(SRE team owning the lineage backend)*

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/openlineage/` *(PROPOSED; NEEDS VERIFICATION)*; alternatively Marquez or OpenMetadata internal instance (see OPEN-DASH-OBS-04).
- **Telemetry source:** `runtime/observability/openlineage-emitter/` *(PROPOSED)*; OpenLineage backend store.
- **Standards:** `docs/standards/OPENLINEAGE.md` *(PROPOSED; OPEN-DR-05)*.
- **Policy bundles:** `policy/observability/lineage-facet-minimums/` *(PROPOSED; Pass 10 C5-06)*; `policy/observability/dataset-redaction/` *(PROPOSED)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/lineage-and-provenance.md` *(consumes facet conformance to assert lineage completeness)*; `docs/dashboards/governance/evidence-and-source.md` *(consumes `receiptRef` resolution rate)*.
- **Per-domain breakdown:** `docs/dashboards/domain/<domain>.md` *(per-namespace lineage views)*.
- **Release-lifecycle view:** `docs/dashboards/release/lineage-by-release.md` *(PROPOSED sibling)*.
- **Related observability specs:** `ingest-run-trace-coverage.md` (shares `trace_id` join key with lineage `run`); `telemetry-contract-health.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: OpenLineage facet schema change, addition of a KFM-specific facet, backend version bump, sensitivity-tier reclassification of any upstream package.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-OL-01** — Should the lineage backend be Marquez, OpenMetadata, or a custom KFM admin console? Relates to OPEN-DASH-OBS-04 in parent README.
- **OPEN-DASH-OBS-OL-02** — What is the canonical KFM facet namespace prefix? (`kfm.*` is implied but not ratified.)
- **OPEN-DASH-OBS-OL-03** — Whose responsibility is dataset-name redaction — per-package adapter or central processor? Relates to OPEN-DASH-OBS-03.

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Pass 10 C1-05 (OpenLineage events end-to-end) | **CONFIRMED** in corpus | §1, §2 facet vocabulary, §7 cross-links. |
| KFM-P15-PROG-0006 (pipeline OTel root trace) | PROPOSED in corpus | §7 trace_id join key. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| Atlas v1.1 §24.5 (Sensitivity Tiers) | CONFIRMED | §3 redaction rules. |
| Atlas v1.1 §24.10 (Risk Register — cross-lane joins) | CONFIRMED | §3 inference-risk anchor. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template alignment. |

<sub>Specification only. The lineage event stream itself is CONFIRMED via Pass 10 C1-05; this dashboard is PROPOSED. Behind the trust membrane; default-deny public exposure.</sub>
