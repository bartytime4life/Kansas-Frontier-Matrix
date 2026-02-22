# data/audit — Audit Ledger & Run Receipts

Append-only, policy-aware audit artifacts that make KFM runs reproducible, reviewable, and enforceable.

**Status:** Draft (vNext)  
**Owners:** TBD — Steward + Operator  

<kbd>governed</kbd> <kbd>append-only</kbd> <kbd>schema-first</kbd> <kbd>restricted-by-default</kbd>

**Quick nav:** [Purpose](#purpose) · [What lives here](#what-lives-here) · [Directory layout](#directory-layout) · [Data contracts](#data-contracts) · [Write path](#write-path) · [Read path](#read-path) · [Security and privacy](#security-and-privacy) · [Definition of Done](#definition-of-done) · [Appendix](#appendix)

> [!WARNING]
> This directory is intended for **governed audit artifacts**. Treat contents as **sensitive operational data** by default.
> Do **not** publish or mirror outside controlled storage without an explicit retention + access policy.

---

## Purpose

`data/audit/` holds the **audit ledger** (append-only event stream) and **run receipts** (one per governed operation).

KFM uses these artifacts to:
- make **pipeline runs** (ingest/transform/publish) reproducible,
- record **policy decisions** (allow/deny + obligations),
- prove that **promotion gates** were satisfied,
- and allow stewards/operators to review “what happened” without relying on ad-hoc logs.

---

## What lives here

### Run receipts (per operation)

A **run receipt** is a structured record emitted for:
- every pipeline run (ingest/transform/publish),
- and every governed query path (e.g., Focus Mode, evidence resolution), if implemented.

Receipts capture:
- inputs/outputs **by digest**,
- execution environment,
- validation status,
- and policy decision references.

### Audit ledger (append-only)

The **audit ledger** is:
- an **append-only** log,
- treated as a **governed dataset itself**,
- with redactions/generalizations applied *via governed process* (typically by creating controlled “views”, not by rewriting history).

---

## Audit in the truth path

```mermaid
flowchart LR
  U[Upstream source] --> C[Connectors / Runners]
  C --> R[Run receipt<br/>inputs/outputs/env/validation/policy]
  R --> L[Audit ledger<br/>append-only events]
  R --> P[PROV bundle<br/>Activity/Entity/Agent]
  P --> T[Catalog triplet<br/>DCAT + STAC + PROV]
  T --> A[Governed API<br/>policy + evidence resolver]
  L --> A
  A --> UI[Map / Story / Focus UI<br/>shows audit_ref (policy-safe)]
```

---

## Directory layout

> [!NOTE]
> The exact subfolders may vary by environment (repo checkout vs. object store).  
> The structure below is the **recommended on-disk convention** for local/dev + CI artifacts.

```text
data/audit/
  README.md

  ledger/                      # append-only audit stream(s)
    audit_ledger.jsonl         # JSONL: 1 event per line (see "Audit ledger contract")
    audit_ledger.jsonl.sha256  # optional: digest snapshot of the ledger file

  run_receipts/                # 1 JSON per run (immutable once written)
    YYYY/MM/DD/
      <run_id>.json

  policy_decisions/            # optional: decision snapshots referenced by receipts/ledger
    YYYY/MM/DD/
      <decision_id>.json

  promotions/                  # optional: promotion manifests + approvals
    YYYY/MM/DD/
      <dataset_version_id>.json

  _views/                      # derived, publish-safe projections (NOT canonical)
    redacted_audit_ledger.jsonl
```

**Canonical vs rebuildable note:** the **audit ledger** is canonical; any `_views/` are rebuildable projections.

---

## Data contracts

### Run receipt contract (minimum)

A run receipt **MUST** include:
- a stable `run_id`,
- `actor` (principal + role),
- `operation`,
- `dataset_version_id` (when applicable),
- `inputs[]` and `outputs[]` with digests,
- `environment` fields sufficient to reproduce (at least container + commit + params digest),
- `validation` result,
- a `policy.decision_id` link,
- `created_at` timestamp.

#### Example (template)

```json
{
  "run_id": "kfm://run/<rfc3339>.<suffix>",
  "actor": { "principal": "svc:<name>", "role": "<role>" },
  "operation": "<op>",
  "dataset_version_id": "<dataset_version_id>",
  "inputs": [
    { "uri": "<input-uri>", "digest": "sha256:<hex>" }
  ],
  "outputs": [
    { "uri": "<output-uri>", "digest": "sha256:<hex>" }
  ],
  "environment": {
    "container_digest": "sha256:<hex>",
    "git_commit": "<sha>",
    "params_digest": "sha256:<hex>"
  },
  "validation": { "status": "pass|fail", "report_digest": "sha256:<hex>" },
  "policy": { "decision_id": "kfm://policy_decision/<id>" },
  "created_at": "<rfc3339>"
}
```

> [!TIP]
> Keep receipts **hashable** and **safe to render**: store **digests + references**, not secrets.

---

### Audit ledger contract (PROPOSED v1)

The audit ledger is a JSONL file. Each line is a single **append-only** event.

An audit event **SHOULD** include:
- `audit_ref` (stable identifier for this entry),
- `event_type` (controlled vocabulary),
- `who` (principal + role),
- `what` (operation/endpoint + parameters summary),
- `when` (timestamp),
- `why` (optional purpose string, if declared),
- `inputs`/`outputs` (digests),
- `policy` outcome summary + decision reference,
- `links` to run receipt / PROV / catalogs.

#### Example event (template)

```json
{
  "audit_ref": "kfm://audit/entry/<id>",
  "event_type": "run_receipt_emitted",
  "who": { "principal": "svc:pipeline", "role": "operator" },
  "what": {
    "operation": "ingest+publish",
    "dataset_version_id": "<dataset_version_id>"
  },
  "when": "<rfc3339>",
  "why": "<optional-purpose>",
  "io": {
    "inputs": [{ "digest": "sha256:<hex>", "uri": "<uri>" }],
    "outputs": [{ "digest": "sha256:<hex>", "uri": "<uri>" }]
  },
  "policy": {
    "decision_id": "kfm://policy_decision/<id>",
    "decision": "allow|deny",
    "reason_codes": ["<code>"]
  },
  "links": {
    "run_receipt": "data/audit/run_receipts/YYYY/MM/DD/<run_id>.json",
    "prov_bundle": "<prov-uri-or-digest>",
    "catalogs": ["<dcat-uri>", "<stac-uri>"]
  }
}
```

> [!IMPORTANT]
> Treat audit events as **policy-sensitive**: avoid including precise restricted geometry/PII.
> Prefer digests and high-level summaries that can be expanded only under authorization.

---

## Write path

### Rules (fail-closed posture)

- **Append-only:** never edit or delete existing ledger entries or receipts.
- **Corrections:** emit a *new* event that references the prior `audit_ref` and explains the correction.
- **Redaction:** do not rewrite history in-place; create a governed redacted view in `_views/` (or an equivalent controlled projection).
- **Linkability:** audit entries should link to run receipts and any promotion manifests/approvals.

### Minimum emission points

A governed workflow is incomplete unless it emits:
1. Run receipt (per run),
2. Audit ledger append (per run + key governance actions),
3. References from catalogs/PROV to the run receipt (as applicable).

---

## Read path

Consumers typically include:
- stewards/operators reviewing promotions or incidents,
- CI checks verifying required artifacts exist and conform,
- UI components rendering safe “receipt views” (read-only) where allowed.

**Policy rule:** UI may show audit metadata only in **policy-safe** form; it must not leak restricted existence through error differences or “ghost metadata.”

---

## Security and privacy

Audit artifacts may contain sensitive operational detail.

Minimum posture:
- logs/receipts are append-only,
- redact for PII/restricted info,
- access restricted to stewards/operators,
- retention + deletion policy defined and enforced.

---

## Definition of Done

Use this checklist when adding a new pipeline / governed feature:

- [ ] Run receipt emitted for the operation (pipeline run / query / publish).
- [ ] Audit ledger appended with `who/what/when/(why)/inputs/outputs/policy` summary.
- [ ] Inputs/outputs recorded **by digest**, not by mutable path alone.
- [ ] Validation results recorded and fail-closed semantics enforced.
- [ ] Policy decision reference recorded (decision_id + reason codes).
- [ ] If promotion-related: approvals captured where required.
- [ ] Audit artifacts treated as governed: access + retention policy exists.

---

## Appendix

<details>
<summary><strong>Controlled vocabulary: suggested <code>event_type</code> values</strong></summary>

- `run_receipt_emitted`
- `policy_decision_recorded`
- `dataset_promotion_requested`
- `dataset_promotion_approved`
- `catalog_triplet_published`
- `evidence_resolved`
- `focus_query_executed`
- `access_denied` (policy-safe summary only)

</details>

<details>
<summary><strong>Notes on storage</strong></summary>

If `data/audit/` is mirrored to object storage, treat it as **canonical**. Any indexes/search views over audit data are rebuildable and must be derived from canonical records.

</details>

---
_Back to top: [↑](#dataaudit--audit-ledger--run-receipts)_
