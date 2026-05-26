<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-governance-provenance-citations
title: Provenance Citations Panel (cross-cutting governance health spec)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + governance-health steward + AI surface owner
created: 2026-05-26
updated: 2026-05-26
policy_label: public
related:
  - kfm://doc/dashboards-governance-readme
  - kfm://doc/atlas-v1-1                      # §24.11.1 cite-or-abstain compliance
  - kfm://card/p32-feat-0019                  # PROPOSED card: provenance citations panel
tags: [kfm, dashboards, governance, provenance, citations, cite-or-abstain, cross-cutting]
notes:
  - Source card KFM-P32-FEAT-0019 is PROPOSED in the Pass 32 New Cards Register.
  - Maps to Atlas §24.11.1 cite-or-abstain compliance — the citation-side counterpart to evidence-and-source.md.
[/KFM_META_BLOCK_V2] -->

# Provenance Citations Panel

<!-- [doc: kfm://doc/dashboards-governance-provenance-citations] -->
<a id="top"></a>

> Cross-cutting governance view focused on citation quality across all surfaces — citation-presence rate, citation-resolution rate, citation-recency distribution, and per-surface citation-vs-abstain ratios.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Lane: PROPOSED" src="https://img.shields.io/badge/lane-PROPOSED-orange">
  <img alt="Scope: cross-cutting" src="https://img.shields.io/badge/scope-cross--cutting-informational">
  <img alt="Source: KFM-P32-FEAT-0019" src="https://img.shields.io/badge/source-KFM--P32--FEAT--0019-purple">
  <img alt="Atlas §24.11.1" src="https://img.shields.io/badge/atlas-%C2%A724.11.1-purple">
  <img alt="Policy label: public" src="https://img.shields.io/badge/policy--label-public-lightgrey">
</p>

> [!IMPORTANT]
> **Truth posture.** Source card KFM-P32-FEAT-0019 is PROPOSED. The "cite-or-abstain compliance" top-line is shared with `evidence-and-source.md`; this dashboard is the **citation-quality drill-down** — the *what kind of citations* view, not the *did we cite at all* view.

---

## 1. Scope

- **Source anchor:** KFM-P32-FEAT-0019 *(PROPOSED)* + Atlas §24.11.1 (cite-or-abstain compliance indicator).
- **Audience:** AI surface owner, governance-health steward, reviewer, docs steward.
- **Aggregation scope:** Cross-cutting — citation events across all citing surfaces (AI surface, governed-API, public UI).

[↑ back to top](#top)

---

## 2. Indicators

| Indicator | What it measures | Healthy posture (PROPOSED) | Signal source |
|:---|:---|:---|:---|
| Citation-presence rate | % of citable outputs carrying at least one citation | ≥ 99% | Surface emission + AIReceipt |
| Citation-resolution rate | % of emitted citations resolving to a real `EvidenceBundle` | ≥ 99.9% | EvidenceBundle resolver |
| Citation-recency distribution | Histogram of citation age relative to release window | Median within per-domain freshness budget; long-tail tracked | Citation timestamp + freshness budget |
| Per-surface cite-vs-abstain ratio | Ratio of cited answers to ABSTAINs, per surface | Per-surface baseline; alert on sudden ABSTAIN spike | AIReceipt outcome envelope |
| Broken-citation count | Count of citations that fail to resolve | 0 *(non-zero indicates broken evidence chain)* | EvidenceBundle resolver |

[↑ back to top](#top)

---

## 3. Per-domain breakdowns

Citation quality varies materially by domain (license terms, source recency profiles):

- `docs/dashboards/domain/hydrology.md` *(time-critical citations — recency budget tight)*
- `docs/dashboards/domain/archaeology.md` *(deep citations into restricted archives)*
- `docs/dashboards/domain/fauna-flora.md` *(observation databases)*
- *…other domain specs as applicable.*

[↑ back to top](#top)

---

## 4. Ownership

- **Docs steward:** OWNER_TBD
- **Governance-health steward:** OWNER_TBD
- **AI surface owner:** OWNER_TBD
- **Implementation owner:** OWNER_TBD

[↑ back to top](#top)

---

## 5. Implementation pointer

- **Dashboard app:** `apps/review-console/citations/` *(PROPOSED; NEEDS VERIFICATION)*.
- **Telemetry:** AIReceipt + EvidenceBundle resolver logs; cross-link to `docs/dashboards/observability/openlineage-event-stream.md` (`receiptRef` facet).
- **Schemas read:** `schemas/contracts/v1/evidence/Citation.schema.json` *(NEEDS VERIFICATION).*
- **Policy bundles emitting signals:** `policy/evidence/cite-or-abstain/`, `policy/evidence/citation-recency/` *(PROPOSED).*
- **Registers visualized:** `docs/registers/DRIFT_REGISTER.md` *(broken-citation events recorded as drift).*
- **Related governance specs:** `evidence-and-source.md` (top-line cite-or-abstain rate), `ai-surface-health.md` (citation-with-evidence rate shared signal).

[↑ back to top](#top)

---

## 6. Review cadence

- Reviewed quarterly.
- Trigger events: Atlas §24.11.1 amendment, AIReceipt schema change, citation-recency budget revision, per-domain freshness budget change.

[↑ back to top](#top)

---

## 7. Open questions

- **OPEN-DASH-GOV-PC-01** — Where does per-domain citation-recency budget live — here, in `domain/<domain>.md`, or in `policy/evidence/citation-recency/`?
- **OPEN-DASH-GOV-PC-02** — Broken-citation count: page on first occurrence (consistent with parent README §10 "non-zero is an incident") or aggregate?
- **OPEN-DASH-GOV-PC-03** — Boundary with `evidence-and-source.md`: top-line vs drill-down — is this the right cut?

[↑ back to top](#top)

---

## 8. Evidence basis & citations

| Source | Status | Supports |
|:---|:---|:---|
| KFM-P32-FEAT-0019 (Provenance citations panel) | PROPOSED in corpus | §1 source anchor. |
| Atlas v1.1 §24.11.1 (Evidence and Source Integrity — cite-or-abstain compliance) | CONFIRMED (manuscript) | §2 cite-or-abstain shared indicator. |
| `docs/dashboards/governance/README.md` | CONFIRMED (this folder) | §6 template. |

<sub>Specification only. Citation-quality drill-down; top-line at `evidence-and-source.md`; receipts are the canonical artifacts.</sub>
