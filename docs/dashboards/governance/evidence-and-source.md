<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-evidence-and-source
title: Evidence and Source Integrity (system-wide governance health spec; Atlas §24.11.1)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.1 — master indicator catalog (5 indicators)
  - kfm://doc/dashboards-domain-readme        # per-domain reciprocal breakdowns
  - kfm://register/drift                      # docs/registers/DRIFT_REGISTER.md
  - kfm://register/verification-backlog       # docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, dashboards, governance, evidence, source, integrity, 24-11-1]
notes:
  - Indicator catalog: Atlas §24.11.1 (5 indicators); labeled PROPOSED in source.
  - Instrumentation and steward ownership are NEEDS VERIFICATION per VB-11-08.
  - Specification only; implementation lives in apps/; register data lives in docs/registers/.
[/KFM_META_BLOCK_V2] -->

# Evidence and Source Integrity

<!-- [doc: kfm://doc/dashboards-governance-evidence-and-source] -->
<a id="top"></a>

> System-wide governance health view of evidence and source integrity — EvidenceRef resolution rate, EvidenceBundle completeness, stale-source rate, cite-or-abstain compliance, and provenance-chain depth distribution. Atlas §24.11.1.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: system-wide" src="https://img.shields.io/badge/scope-system--wide-informational">
  <img alt="Atlas §24.11.1" src="https://img.shields.io/badge/atlas-%C2%A724.11.1-purple">
  <img alt="Indicators: 5" src="https://img.shields.io/badge/indicators-5-yellow">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Indicator catalog from Atlas §24.11.1 (text CONFIRMED in source, indicators labeled PROPOSED). Instrumentation and steward ownership are NEEDS VERIFICATION per Atlas §G.7 VB-11-08. Healthy-posture thresholds listed here are PROPOSED.

---

## 1. Scope

- **Atlas reference:** §24.11.1 — Evidence and Source Integrity (5 indicators).
- **Audience:** Reviewer, governance-health steward, docs steward.
- **Aggregation scope:** System-wide. Per-domain breakdowns live in `docs/dashboards/domain/<domain>.md`.

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| EvidenceRef resolution rate | % of public-surface EvidenceRefs that resolve to a real `EvidenceBundle` | > 99.9% over trailing release window | EvidenceBundle resolver logs |
| EvidenceBundle completeness | % of EvidenceBundles carrying all required facets (source, license, retrieval timestamp, content hash) | 100% on the active manifest | EvidenceBundle validator |
| Stale-source rate | % of cited sources whose retrieval timestamp is past the per-source staleness budget | < 5% system-wide; per-domain budgets in `domain/` | Source-watch validator + `source-availability-watch.md` |
| Cite-or-abstain compliance | % of AI-surfaced answers that either carry a valid citation or returned `ABSTAIN` | ≥ 99% over trailing release window | AIReceipt outcomes; cross-link to `provenance-citations.md` |
| Provenance-chain depth distribution | Histogram of provenance-chain depths on resolved EvidenceRefs (1-hop, multi-hop, transitive) | No degradation of multi-hop chains over time; tracked, not thresholded | EvidenceBundle resolver + lineage events |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Each KFM domain that surfaces evidence has a corresponding spec in `docs/dashboards/domain/`. Listed for reciprocal linking (each domain spec links back here):

- `docs/dashboards/domain/hydrology.md`
- `docs/dashboards/domain/archaeology.md`
- `docs/dashboards/domain/fauna-flora.md`
- `docs/dashboards/domain/settlements-infrastructure.md`
- *…and any additional domain spec that emits EvidenceRefs (see `docs/dashboards/domain/README.md` §5).*

Per-domain healthy-posture thresholds may differ from the system-wide threshold with documented context (e.g., archaeology may run a stricter cite-or-abstain bar than 99%).

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **Implementation owner:** OWNER_TBD *(apps team rendering the review console).*

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/evidence-source/` *(PROPOSED; NEEDS VERIFICATION)*; alternatively future `apps/dashboards/governance/evidence/`.
- **Telemetry:** `runtime/observability/evidence-resolver/` *(PROPOSED).*
- **Schemas read:** `schemas/contracts/v1/evidence/EvidenceBundle.schema.json`, `schemas/contracts/v1/evidence/EvidenceRef.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/evidence/cite-or-abstain/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` (when resolution-rate drops are recorded as drift), `docs/registers/VERIFICATION_BACKLOG.md` (VB-11-08 instrumentation tracking).
- **Related observability:** `docs/dashboards/observability/service-uptime-latency.md` (resolver SLO), `docs/dashboards/observability/openlineage-event-stream.md` (`receiptRef` resolution rate).

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.11.1 amendment, EvidenceBundle schema change, AIReceipt outcome envelope revision, register restructure of `DRIFT_REGISTER.md`.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-EVID-01** — Per-domain stale-source budgets: per `domain/` spec or central table in this file? Convention question.
- **OPEN-DASH-GOV-EVID-02** — Provenance-chain depth distribution — tracked-only or should a degradation alert exist? Relates to Atlas §24.8 (Stale-State/Supersession).
- **OPEN-DASH-GOV-EVID-03** — Reconcile this kebab-case spec with the pre-existing `EVIDENCE_INTEGRITY.md` (UPPER_SNAKE_CASE; preserved for now).

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| Atlas v1.1 §24.11.1 (Evidence and Source Integrity — 5 indicators) | CONFIRMED (manuscript) | §1, §2 indicator catalog. |
| Atlas v1.1 §G.7 VB-11-08 (governance-health instrumentation backlog) | CONFIRMED | Truth posture; §5 implementation NEEDS VERIFICATION. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template alignment. |
| `docs/dashboards/domain/README.md` | CONFIRMED (sibling) | §3 reciprocal linking. |
| `docs/registers/DRIFT_REGISTER.md`, `VERIFICATION_BACKLOG.md` | CONFIRMED (corpus, mounted-repo NEEDS VERIFICATION) | §5 register pointers. |

<sub>Specification only. Indicators reported, not enforced; registers carry data; apps render. Five layers, no collapse.</sub>
