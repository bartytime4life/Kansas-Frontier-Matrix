<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts/runtime_verification/trust_federation
title: Multi-Source Trust Federation and Conflict Detection
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-04-15
updated: 2026-04-15
policy_label: public
related: [
  ../tile_verification/README.md,
  ../evidence_timeline/README.md,
  ../../../schemas/runtime_verification/trust_federation.schema.json,
  ../../../policy/README.md,
  ../../../data/receipts/README.md,
  ../../../data/proofs/README.md,
  ../../../tests/e2e/runtime_proof/README.md
]
tags: [kfm, runtime, federation, trust, conflict, provenance, evidence]
notes: [Defines cross-dataset trust aggregation, compatibility checks, and conflict signaling for governed runtime decisions.]
[/KFM_META_BLOCK_V2] -->

# Multi-Source Trust Federation and Conflict Detection

Deterministic contract for aggregating **multiple verified evidence sources** into a governed runtime trust state.

> Doctrine:  
> Individually verified sources are not automatically jointly sufficient.

---

## 🔎 Purpose

This contract answers:

- Which sources are currently trusted?
- Are trusted sources mutually compatible?
- Does disagreement require review, abstention, or denial?
- Which source influenced the runtime answer?

---

## 🧱 Scope

This contract governs:

- federation of multiple source receipts
- trust aggregation
- conflict detection
- policy-directed conflict outcomes
- source influence visibility

---

## 📥 Inputs

| Field | Type | Description |
|------|------|-------------|
| `sources[]` | array | Runtime source states |
| `comparison_domain` | string | Domain of comparison (`geometry`, `freshness`, `classification`, `coverage`) |
| `policy_label` | string | Governing policy context |
| `tolerance_profile` | string | Allowed variance profile |

---

## 🧾 Source State

```json
{
  "source_ref": "kfm://release/hydrology/kansas/v4",
  "receipt_ref": "kfm://receipt/runtime/hydrology/run-001",
  "verified": true,
  "outcome": "ANSWER",
  "freshness": "2026-04-15T12:00:00Z",
  "domain": "hydrology"
}
```

---

## ⚖️ Federation Outcomes

| Outcome | Meaning |
|--------|---------|
| `CONSISTENT` | Sources agree within policy tolerance |
| `DIVERGENT` | Sources differ, but not critically |
| `CONFLICT` | Sources disagree in a materially relevant way |
| `INSUFFICIENT` | Not enough trusted sources |
| `REVOKED_PRESENT` | A revoked/corrected source is still participating |

---

## 🚦 Runtime Decision Guidance

| Federation Outcome | Recommended Runtime Result |
|-------------------|----------------------------|
| `CONSISTENT` | `ANSWER` |
| `DIVERGENT` | `ANSWER` with obligations or `ABSTAIN` |
| `CONFLICT` | `ABSTAIN` or `DENY` |
| `INSUFFICIENT` | `ABSTAIN` |
| `REVOKED_PRESENT` | `DENY` |

---

## 🧠 Conflict Types

| Type | Example |
|------|---------|
| `GEOMETRY_MISMATCH` | watershed boundary differs materially |
| `CLASSIFICATION_MISMATCH` | one source says wetland, another says cropland |
| `FRESHNESS_SKEW` | one source is too stale relative to the others |
| `COVERAGE_GAP` | one source lacks the queried extent/time |
| `PROVENANCE_PRIORITY_CONFLICT` | lower-authority source contradicts higher-authority source |

---

## 🔗 Influence Tracking

Each runtime answer must be able to identify:

- participating sources
- excluded sources
- dominant source(s)
- reason for exclusion

---

## 📌 Invariant

> No source marked revoked may contribute to a federated `CONSISTENT` result.

---

## 🧪 Required Tests

- two verified compatible sources → `CONSISTENT`
- two verified materially different sources → `CONFLICT`
- stale but signed source vs fresh authoritative source → policy-shaped outcome
- revoked source present → `REVOKED_PRESENT`

---

**End of Contract**