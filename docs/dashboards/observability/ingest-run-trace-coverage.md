<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-observability-ingest-run-trace-coverage
title: Ingest-Run Trace Coverage (system-health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: observability steward + pipelines owner + sensitivity reviewer
created: 2026-05-26
updated: 2026-05-26
policy_label: internal
related:
  - kfm://doc/dashboards-observability-readme
  - kfm://card/p13-prog-0005                   # PROPOSED card: OTel ingest-run trace contract
  - kfm://card/p15-prog-0006                   # PROPOSED card: pipeline OTel root trace
  - kfm://doc/standard-opentelemetry           # PROPOSED: docs/standards/OPENTELEMETRY.md
tags: [kfm, dashboards, observability, ingest, trace, coverage, pipelines]
notes:
  - Source cards KFM-P13-PROG-0005 and KFM-P15-PROG-0006 are PROPOSED in the corpus.
  - Span vocabulary follows Atlas §24.6 pipeline gates (fetch / transform / policy / signing / publication).
  - Sensitive-content risk concentrated in fetch-span attributes (URLs, dataset names).
[/KFM_META_BLOCK_V2] -->

# Ingest-Run Trace Coverage

<!-- [doc: kfm://doc/dashboards-observability-ingest-run-trace-coverage] -->
<a id="top"></a>

> Surfaces whether every ingest run produced a complete OTel root trace with the canonical span tree (fetch / transform / policy / signing / publication) and a `trace_id` that joins back into receipts, AIReceipts, logs, and attestations.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Audience: SRE / pipelines" src="https://img.shields.io/badge/audience-SRE%20%2F%20pipelines-blue">
  <img alt="Sensitivity: T2" src="https://img.shields.io/badge/sensitivity-T2-orange">
  <img alt="Public-exposure: INTERNAL" src="https://img.shields.io/badge/public--exposure-INTERNAL-critical">
  <img alt="Source: P13-PROG-0005 + P15-PROG-0006" src="https://img.shields.io/badge/source-P13%20%2B%20P15-purple">
</p>

> [!CAUTION]
> **Sensitive-content posture:** **T2 restricted**. Fetch-span attributes can carry source URLs that, in archaeology and rare-species lanes, name precise coordinates. Source-URL fields MUST be redacted-at-emission when the dataset's sensitivity tier is T3+ (Atlas §24.5). This dashboard surfaces span shape and trace-ID join rates — never raw URLs.

---

## 1. Scope

- **Source anchor:** KFM-P13-PROG-0005 *(OTel ingest-run trace contract, PROPOSED)* + KFM-P15-PROG-0006 *(pipeline OTel root trace with trace_id in receipts, PROPOSED)*.
- **Audience:** Pipelines owner, observability steward, SRE on-call.
- **Aggregation scope:** Per-run trace shape conformance; per-package fetch-span attribute coverage; trace-ID propagation across receipts/logs/attestations.

[↑ back to top](#top)

---

## 2. Signals

| Signal | What it carries | Healthy posture | Emitting adapter / path |
|:---|:---|:---|:---|
| `ingest.trace.root_span_present_rate` | % of ingest runs with a root trace span | 100% | `runtime/observability/otel-pipeline/` *(PROPOSED)* |
| `ingest.trace.canonical_span_tree_conformance` | % of runs whose span tree matches the canonical fetch→transform→policy→signing→publication shape | ≥ 99.5% | same |
| `ingest.trace.fetch_span_p95_seconds` | p95 fetch-span duration | < 30s for standard sources | same |
| `ingest.trace.trace_id_in_receipt_rate` | % of run_manifests carrying the run's `trace_id` | 100% | receipt writer |
| `ingest.trace.trace_id_in_ai_receipt_rate` | % of AIReceipts carrying the run's `trace_id` | 100% | AIReceipt writer |
| `ingest.trace.trace_id_in_attestation_rate` | % of attestations carrying the run's `trace_id` | 100% | attestation signer |
| `ingest.trace.policy_span_decision_present_rate` | % of policy spans carrying the `PolicyDecision` identifier | 100% | policy evaluator |

[↑ back to top](#top)

---

## 3. Sensitive-content posture

- **Sensitivity tier of signals:** T2 restricted *(shape metrics are T0, but fetch-span attributes upstream may carry T3+ content).*
- **Redaction-at-emission rules:**
  - Source URLs from T3+ packages replaced with content-addressed digests at emission.
  - Span attributes MUST NOT contain raw coordinates, person identifiers, DNA sample IDs, or critical-infrastructure precise locations.
  - Stack traces in span events redacted via central processor before reaching Tempo.
- **Sampling policy:** 100% for shape-conformance metrics; per-package sampling for span bodies (T0–T1: 100%; T2: 100% with redaction; T3: shape-only; T4: span suppressed, count only — per parent README §10.1).
- **Trace-body retention window:** Per Tempo configuration; not set by this spec.
- **Access control on dashboard:** Internal-only; T2 access group required.

[↑ back to top](#top)

---

## 4. Public-exposure policy

- **Default:** INTERNAL.
- **Documented exceptions:** None.
- **Aggregation/redaction if surfaced publicly:** Forbidden without sensitivity-reviewer sign-off; per-package detail never public.

[↑ back to top](#top)

---

## 5. Ownership

- **Observability steward:** OWNER_TBD
- **Pipelines owner / infra owner:** OWNER_TBD
- **Sensitivity reviewer:** OWNER_TBD *(required — T2+).*
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 6. Implementation pointer

- **Dashboard UI:** `apps/admin/observability/ingest-trace-coverage/` *(PROPOSED; NEEDS VERIFICATION)*; trace drill-down via internal Tempo UI.
- **Telemetry source:** `runtime/observability/otel-pipeline/` *(PROPOSED)*; receipts written by `pipelines/`.
- **Standards:** `docs/standards/OPENTELEMETRY.md` *(PROPOSED; OPEN-DASH-OBS-08)*; span vocabulary aligned to Atlas §24.6.
- **Policy bundles:** `policy/observability/ingest-trace-minimums/` *(PROPOSED; Pass 10 C5-06)*.

[↑ back to top](#top)

---

## 7. Cross-links

- **Governance dashboards consuming this signal:** `docs/dashboards/governance/lineage-and-provenance.md` *(trace-ID join key is the lineage anchor)*; `docs/dashboards/governance/evidence-and-source.md` *(trace-ID-in-receipt rate).*
- **Per-domain breakdown:** `docs/dashboards/domain/<domain>.md` *(per-domain ingest health).*
- **Release-lifecycle view:** `docs/dashboards/release/ingest-by-release.md` *(PROPOSED sibling).*
- **Related observability specs:** `openlineage-event-stream.md` *(shares `trace_id` ↔ `run` join);* `validator-orchestrator-health.md`.

[↑ back to top](#top)

---

## 8. Review cadence

- Reviewed quarterly.
- Trigger events: Pipeline gate vocabulary change (Atlas §24.6), trace contract revision (P13-PROG-0005 update), addition of a new pipeline stage.

[↑ back to top](#top)

---

## 9. Open questions

- **OPEN-DASH-OBS-INGEST-01** — How are partial-failure runs represented (e.g., fetch OK, transform failed, no signing span)? As "canonical shape met up to span N" or as "canonical shape failed"?
- **OPEN-DASH-OBS-INGEST-02** — When trace-ID propagation fails for a single sink (e.g., AIReceipt missing trace_id), is that a single-signal red or a dashboard-wide red?

[↑ back to top](#top)

---

## 10. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P13-PROG-0005 (OTel ingest-run trace contract) | PROPOSED in corpus | §1, §2 span vocabulary. |
| KFM-P15-PROG-0006 (pipeline OTel root trace; trace_id in receipts) | PROPOSED in corpus | §2 trace-ID-in-receipt signals; §7 cross-links. |
| Atlas v1.1 §24.6 (Pipeline Gate Reference) | CONFIRMED | §1 span vocabulary alignment. |
| Atlas v1.1 §24.5 (Sensitivity Tiers) | CONFIRMED | §3 redaction rules. |
| Pass 10 C5-06 (Observability as Code via OPA) | CONFIRMED in corpus | §6 policy-bundle pointer. |
| `docs/dashboards/observability/README.md` | CONFIRMED (this folder) | §6 template alignment; §10.1 sensitivity tier table. |

<sub>Specification only. Behind the trust membrane; T2-default access.</sub>
