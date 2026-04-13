<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid:REVIEW_REQUIRED>
title: Promotion Summary — overlay:floodplain-kansas v1
type: standard
version: v1
status: review
owners: <REVIEW_REQUIRED>
created: 2026-04-13
updated: 2026-04-13
policy_label: <REVIEW_REQUIRED>
related: [kfm://audit/promotion/floodplain-kansas/v1, kfm://release/overlay/floodplain-kansas/v1, oci://ghcr.io/bartytime4life/kfm-promotion@sha256:deadbeef]
tags: [kfm, promotion, release, evidence, floodplain-kansas]
notes: [Values not present in the provided bundle summary remain review placeholders; this document summarizes one promotion artifact set and should not be treated as proof of mounted repo enforcement beyond the surfaced evidence.]
[/KFM_META_BLOCK_V2] -->

# Promotion Summary — `overlay:floodplain-kansas` v1

A reviewer-facing release note for the surfaced promotion artifact set and its visible proof objects.

> [!SUCCESS]
> **Observed decision:** `PROMOTE`  
> **Observed bundle state:** core artifacts present, trust artifacts present, signed decision verified  
> **Best current interpretation:** ready for reviewer/auditor handoff on the evidence shown here

## Quick navigation

- [Decision at a glance](#decision-at-a-glance)
- [Release identity](#release-identity)
- [Artifact inventory](#artifact-inventory)
- [What this proves now](#what-this-proves-now)
- [What still needs verification](#what-still-needs-verification)
- [Reviewer handoff checklist](#reviewer-handoff-checklist)
- [Trust note](#trust-note)

---

## Decision at a glance

KFM doctrine treats promotion as a **governed state change** supported by typed artifacts rather than as an informal file move. In that frame, the surfaced bundle for `overlay:floodplain-kansas` shows the minimum shape of a release-bearing proof object set: a promotion decision, a summary, a promotion record, provenance artifacts, and signature verification outputs, all tied to explicit audit and release references.

### Determination

| Field | Value |
|---|---|
| Candidate | `overlay:floodplain-kansas` |
| Decision | ✅ `PROMOTE` |
| Spec hash | `0123456789ab…` |
| Prior spec hash | `abcdef012345…` |
| Generated at | `2026-04-13T00:00:00Z` |
| Recorded at | `2026-04-13T00:05:00Z` |
| Gate runner | `tools/validators/promotion_gate@v1` |
| Repo ref | `refs/heads/main@abc123def456` |
| CI run id | `github-actions:123456789` |
| Audit ref | `kfm://audit/promotion/floodplain-kansas/v1` |
| Release ref | `kfm://release/overlay/floodplain-kansas/v1` |
| Attestation ref | `oci://ghcr.io/bartytime4life/kfm-promotion@sha256:deadbeef` |
| Attestation verified | 🔏 `True` |

### Bundle health

| Check | Observed state |
|---|---|
| Core artifact set present | `true` |
| Trust artifact set present | `true` |
| Signed decision verified | `True` |
| Reviewer/auditor handoff readiness | `Observed as sufficient in this surfaced summary` |

---

## Release identity

This promotion summary is best read as a **release-adjacent proof note**, not as a generic changelog blurb. The surfaced identifiers already give it a stable release context:

- `kfm://release/overlay/floodplain-kansas/v1` identifies the promoted outward subject.
- `kfm://audit/promotion/floodplain-kansas/v1` identifies the audit trail anchor.
- `oci://ghcr.io/bartytime4life/kfm-promotion@sha256:deadbeef` identifies the attestation-bearing OCI reference.
- `refs/heads/main@abc123def456` and `github-actions:123456789` tie the surfaced decision to a repo ref and CI run.

```text
Promotion scope shown here
candidate -> promoted release reference -> audit reference -> attestation reference
```

---

## Artifact inventory

The surfaced bundle includes six named artifacts.

| Artifact key | Path | SHA-256 | Media type | Role in the bundle |
|---|---|---|---|---|
| `decision` | `decision.json` | `aaaaaaaaaaaa…` | `application/json` | Promotion decision payload |
| `summary` | `promotion-summary.md` | `bbbbbbbbbbbb…` | `text/markdown` | Human-readable reviewer summary |
| `record` | `promotion-record.json` | `cccccccccccc…` | `application/json` | Structured promotion record |
| `prov` | `promotion-prov.json` | `dddddddddddd…` | `application/json` | Provenance payload |
| `sign_result` | `decision-sign-result.json` | `eeeeeeeeeeee…` | `application/json` | Signing output/result |
| `verify_result` | `decision-verify-result.json` | `ffffffffffff…` | `application/json` | Verification output/result |

### Relationship sketch

```mermaid
flowchart LR
    A[Candidate<br/>overlay:floodplain-kansas] --> B[decision.json]
    B --> C[promotion-record.json]
    B --> D[promotion-summary.md]
    C --> E[promotion-prov.json]
    B --> F[decision-sign-result.json]
    F --> G[decision-verify-result.json]
    C --> H[kfm://audit/promotion/floodplain-kansas/v1]
    C --> I[kfm://release/overlay/floodplain-kansas/v1]
    F --> J[oci://ghcr.io/bartytime4life/kfm-promotion@sha256:deadbeef]
```

---

## What this proves now

### CONFIRMED from the surfaced summary

- A concrete candidate was evaluated: `overlay:floodplain-kansas`.
- The surfaced decision is `PROMOTE`.
- The bundle claims both a current and prior `spec_hash`, which is consistent with KFM’s contract-first promotion posture.
- The surfaced proof set includes both human-readable and machine-readable artifacts.
- A signed-decision verification artifact is present and marked `True`.
- The bundle is framed as complete enough for reviewer/auditor handoff.

### INFERRED from KFM doctrine plus the surfaced fields

- This bundle is acting like a **promotion artifact / release proof pack slice** for one governed release unit.
- The summary, record, provenance, sign result, and verify result together form a recognizable subset of KFM’s emerging proof-object family.
- The explicit `audit_ref`, `release_ref`, `repo ref`, and CI run identifier are strong signs of a traceable promotion path.

### Why that interpretation fits KFM

KFM’s doctrinal baseline repeatedly treats promotion as a governed state change that should emit proof artifacts such as decision records, release manifests or proof packs, evidence bundles, and correction-ready lineage. This surfaced bundle aligns with that pattern even though the mounted repository schemas and validators were not directly visible in this session.

---

## What still needs verification

The surfaced summary is strong enough to describe the bundle, but it does **not** justify overclaiming beyond it.

| Area | Status | Why it remains open |
|---|---|---|
| Canonical schema conformance | **UNKNOWN** | No mounted JSON Schema, fixture, or validator output was surfaced for these exact files. |
| Catalog closure (`STAC` / `DCAT` / `PROV`) | **UNKNOWN** | The surfaced summary names a provenance file, but it does not surface outward catalog closure for this release. |
| DecisionEnvelope field compatibility | **UNKNOWN** | The summary contains a decision and audit/release refs, but not enough contract detail to prove conformance to a canonical `DecisionEnvelope` schema. |
| ReviewRecord / separation-of-duty evidence | **UNKNOWN** | Reviewer identity, approval role, or signoff trail were not surfaced. |
| Correction / rollback linkage | **UNKNOWN** | No correction notice, rollback note, or supersession artifact was surfaced. |
| Mounted repo enforcement | **UNKNOWN** | The current session exposed documents and the provided bundle summary, not the live validator code, CI logs, or emitted release assembly traces. |

> [!IMPORTANT]
> Treat this document as a **truthful summary of the surfaced promotion bundle**, not as proof that every broader KFM promotion gate, catalog matrix, or repo rule was executed end to end.

---

## Reviewer handoff checklist

Use this when carrying the bundle into governed review.

- [ ] Confirm `decision.json` and `promotion-record.json` agree on candidate, release reference, and timestamps.
- [ ] Confirm `promotion-prov.json` resolves cleanly to the expected provenance structure.
- [ ] Confirm `decision-sign-result.json` and `decision-verify-result.json` reference the same signed subject.
- [ ] Confirm the attestation reference resolves to the expected digest-bearing OCI object.
- [ ] Confirm the `spec_hash` / prior-hash transition is the intended release delta.
- [ ] Confirm whether a separate `ReleaseManifest`, `EvidenceBundle`, or catalog-closure artifact exists outside this surfaced six-file set.
- [ ] Confirm whether reviewer identity, policy basis, and obligation/reason codes were recorded elsewhere.

### Smallest reviewer-safe conclusion

On the evidence currently surfaced, this bundle supports the statement:

> `overlay:floodplain-kansas` has a visible promotion decision, visible proof artifacts, and a verified signed decision artifact sufficient for handoff into reviewer/auditor flow.

It does **not** yet support the stronger statement that every broader repo-level contract, catalog, and promotion-gate surface has been directly reverified in this session.

---

## Trust note

This promotion event is behavior-significant because it changes publication state. In KFM terms, that means the important question is not only *“was there a decision?”* but also *“can the promoted meaning be reconstructed later from typed artifacts, audit references, and proof objects?”* The surfaced summary is encouraging on that point. It shows release linkage, audit linkage, and signed-decision verification. The remaining gap is not doctrinal clarity; it is direct verification depth.

---

## Appendix — compact interpretation matrix

<details>
<summary><strong>Observed bundle vs. KFM proof-object family</strong></summary>

| Surfaced artifact or field | Closest KFM role | Current reading |
|---|---|---|
| `decision.json` | `DecisionEnvelope`-like artifact | **INFERRED** role; exact schema fit not surfaced |
| `promotion-record.json` | release/promotion record | **CONFIRMED** as surfaced artifact |
| `promotion-prov.json` | provenance carrier | **CONFIRMED** as surfaced artifact |
| `promotion-summary.md` | human-readable release note | **CONFIRMED** as surfaced artifact |
| `decision-sign-result.json` | signing result | **CONFIRMED** as surfaced artifact |
| `decision-verify-result.json` | verification result | **CONFIRMED** as surfaced artifact |
| `audit_ref` | audit linkage | **CONFIRMED** as surfaced field |
| `release_ref` | outward release linkage | **CONFIRMED** as surfaced field |
| `spec_hash` + prior hash | proof quartet member | **CONFIRMED** as surfaced field |
| `run_receipt` / `ai_receipt` | proof quartet remainder | **UNKNOWN** in this surfaced summary |
| `EvidenceBundle` | runtime/review support package | **UNKNOWN** in this surfaced summary |
| catalog closure | `STAC` / `DCAT` / `PROV` outward linkage | **UNKNOWN** in this surfaced summary |

</details>

[Back to top](#promotion-summary--overlayfloodplain-kansas-v1)
