<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-decision-logs-readme
title: Decision Logs — Receipts & Traceability
type: standard
version: v1
status: draft
owners: TODO
created: TODO
updated: TODO
policy_label: public
related: [kfm://object/DecisionEnvelope, kfm://object/ReleaseManifest, kfm://object/run_receipt]
tags: [kfm, governance, receipts, policy]
notes: [Placeholders require verification against repo registers]
[/KFM_META_BLOCK_V2] -->

# Decision Logs (Receipts & Traceability)
> Append-only, evidence-bound records of policy evaluations and outcomes across the KFM trust membrane.

---

## Status · Owners · Quick Links
**Status:** `experimental`  
**Owners:** `TODO`  
![policy](https://img.shields.io/badge/policy-OPA%2FRego-blue)
![receipts](https://img.shields.io/badge/receipts-append--only-green)
![integrity](https://img.shields.io/badge/integrity-signed%20optional-lightgrey)

**Jump to:**
- [Scope](#scope)
- [Repo Fit](#repo-fit)
- [Schema](#schema-decisionlog-v1)
- [Storage Layout](#storage-layout)
- [ID & Hashing](#id--hashing)
- [Validation & Gates](#validation--gates)
- [UI Surfaces](#ui-surfaces)
- [Examples](#examples)
- [Checklist](#checklist)

---

## Scope
Decision Logs capture **what policy decided**, **with which inputs**, and **under which bundle** at a specific time.  
They provide **auditability**, **reproducibility**, and **promotion gating evidence**.

**Key properties**
- Append-only (no in-place mutation)
- Deterministic linkage to inputs (`spec_hash`)
- Explicit reference to **policy bundle digest** and **pipeline run receipt**
- Optional cryptographic signing

---

## Repo Fit
**Path:** `data/receipts/decisions/`  
**Upstream:** policy evaluation (OPA/Rego), pipeline runs (`run_receipt`)  
**Downstream:** promotion gates, ReleaseManifest validation, UI (Evidence Drawer / Focus Mode)

| Layer | Role |
|------|------|
| `policy/**` | Produces evaluation outcomes |
| `tools/validators/**` | Enforces schema & linkage |
| `data/receipts/decisions/**` | Stores Decision Logs |
| `apps/governed_api/**` | Serves logs to clients |
| `apps/web/**` | Displays outcomes |

---

## Inputs
Accepted sources for Decision Logs:

- Policy evaluation outputs (OPA/Rego)
- EvidenceBundle or DTO references
- Pipeline run receipts (`run_receipt`)
- Bundle metadata (`digest`, `version`)

---

## Exclusions
Not stored here:

- Raw policy inputs (kept in EvidenceBundle)
- Policy code itself (stored in `policy/**`)
- Derived UI summaries (rendered downstream)
- Mutable audit edits (handled via correction lineage elsewhere)

---

## Storage Layout
```
data/receipts/decisions/
  README.md
  YYYY/
    MM/
      DD/
        shard-0001.ndjson
        shard-0002.ndjson
```

Optional per-domain mirrors:
```
data/receipts/decisions/ecology/
data/receipts/decisions/archaeology/
```

---

## Schema: DecisionLog (v1)

```json
{
  "schema_version": "v1",
  "object_type": "DecisionLog",
  "decision_id": "kfm://decision/<date>/<hash>",
  "decision_time": "ISO-8601 UTC",
  "policy_engine": "opa@version",

  "bundle_ref": {
    "name": "string",
    "digest": "sha256:...",
    "version": "string"
  },

  "pipeline_run_receipt_ref": "kfm://run/...",

  "input_ref": "kfm://...",
  "input_spec_hash": "sha256:...",

  "rule_ref": "path#rule",
  "outcome": "ANSWER|ABSTAIN|DENY|ERROR",

  "explanation": {
    "reasons": ["string"],
    "bindings": { "key": "value" }
  },

  "metrics": {
    "eval_ms": 0
  },

  "signing": {
    "sigstore_bundle_ref": "kfm://proofs/...",
    "signed_at": "ISO-8601"
  }
}
```

---

## ID & Hashing

**Decision ID generation (PROPOSED)**

```
decision_id = sha256(
  canonical_json({
    bundle_digest,
    rule_ref,
    input_spec_hash,
    decision_time_truncated_to_seconds
  })
)
```

**Requirements**
- Canonical JSON (JCS or equivalent)
- Stable ordering
- Excludes non-deterministic fields

---

## Validation & Gates

### Required checks
- Schema validity
- `bundle_ref.digest` exists
- `pipeline_run_receipt_ref` resolves
- `input_spec_hash` matches referenced object
- Outcome is finite enum

### Promotion gate rule (example)
- A ReleaseManifest **must reference at least one DecisionLog**
- All DecisionLogs must reference the same bundle digest as the release candidate

---

## UI Surfaces

### Evidence Drawer
Display:
- Outcome (badge)
- Reasons (if present)
- Bundle version + digest
- Decision timestamp
- Link to run receipt

### Focus Mode
- If `outcome = DENY` → block render
- If no DecisionLog → treat as **ABSTAIN**
- Never expose restricted fields even if decision exists

---

## Example

```json
{
  "schema_version": "v1",
  "object_type": "DecisionLog",
  "decision_id": "kfm://decision/2026-04-29/8b1c3b",
  "decision_time": "2026-04-29T12:34:56Z",
  "policy_engine": "opa@0.60.0",
  "bundle_ref": {
    "name": "ecology-publication",
    "digest": "sha256:abc123",
    "version": "2026.04.29.1"
  },
  "pipeline_run_receipt_ref": "kfm://run/ci/1234567",
  "input_ref": "kfm://evidence/ecology/xyz",
  "input_spec_hash": "sha256:def456",
  "rule_ref": "policy/ecology/publication.rego#allow_release",
  "outcome": "DENY",
  "explanation": {
    "reasons": ["unknown_rights"],
    "bindings": { "species_code": "EO12345" }
  },
  "metrics": { "eval_ms": 12 }
}
```

---

## Diagram

```mermaid
flowchart TD
  A[EvidenceBundle] --> B[Policy Evaluation (OPA)]
  B --> C[DecisionLog]
  C --> D[run_receipt]
  C --> E[Promotion Gate]
  E --> F[ReleaseManifest]
  F --> G[Published Layer/API]
```

---

## Checklist

- [ ] Schema validated
- [ ] Bundle digest present
- [ ] Run receipt linked
- [ ] Input hash verified
- [ ] DecisionLog emitted for each promotion candidate
- [ ] Stored append-only
- [ ] Optional signature attached

---

## Appendix
<details>
<summary>Notes & Open Questions</summary>

- Schema authority location: NEEDS VERIFICATION  
- Signing enforcement: PROPOSED  
- Domain mirrors: OPTIONAL  

</details>

---

**Back to top ↑**
