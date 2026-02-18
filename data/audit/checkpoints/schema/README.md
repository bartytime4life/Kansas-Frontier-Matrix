# Audit Checkpoints Schema

✅ **Governed artifact** • ✅ **Append-only audit trail** • ✅ **Fail-closed by default**

This directory contains the **versioned schema contracts** for **KFM audit checkpoints**.

Audit checkpoints are the *atomic, machine-validated records* that prove governance gates actually ran — for example:
- ingestion validation
- policy evaluation (allow/deny)
- promotion gates (raw → work → processed)
- Focus Mode / governed API responses emitting an `audit_ref`

> [!IMPORTANT]
> **Trust membrane rule:** clients/UI must *never* fetch raw audit storage directly.  
> Audit/evidence links must resolve via the **governed API boundary**.

---

## Directory layout

```text
data/
  audit/
    checkpoints/
      schema/
        README.md
        # Proposed convention (add as you implement):
        # io.kfm.audit.checkpoint.v1.schema.json
        # examples/
        #   io.kfm.audit.checkpoint.v1.pass.json
        #   io.kfm.audit.checkpoint.v1.fail.json
        # vocab/
        #   checkpoint_kind.v1.json
        #   severity.v1.json
```

> [!NOTE]
> Filenames above are a **recommended** convention (not confirmed in repo).  
> The only hard requirement is: **schemas are versioned, reviewable, and validated in CI**.

---

## What is a checkpoint?

A **checkpoint** is an **immutable record** of a governance or quality decision at a specific time.

In KFM terms, checkpoints support:
- **Accountability** (who/what/when/why)
- **Reproducibility** (inputs/outputs + hashes)
- **Governed publication** (promotion gates don’t pass without receipts)
- **Explainability** (“cite-or-abstain” outputs reference an `audit_ref`)

---

## Relationship to audit ledger, receipts, and promotion

A checkpoint is typically emitted into an **append-only audit ledger**. That ledger may contain multiple record types (checkpoint, receipt, attestation), but this folder is specifically for the **checkpoint contract**.

Recommended conceptual model:

- **Checkpoint**: “A gate ran and produced a decision.”
- **Receipt**: “A pipeline step produced an artifact and here is the verifiable fingerprint.”
- **Attestation**: “A signer (human/service) affirms the checkpoint/receipt is valid.”

> [!TIP]
> Keep checkpoints **small** and **link out** to heavier evidence bundles (PROV/STAC/DCAT, logs, artifacts).

---

## Minimal checkpoint contract

This section describes a **minimum viable schema** (recommended baseline). Adjust as KFM evolves, but keep compatibility rules strict.

### Required top-level fields (recommended)

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `schema` | string | ✅ | Example: `io.kfm.audit.checkpoint.v1` |
| `checkpoint_id` | string | ✅ | Deterministic ID preferred (see hashing section) |
| `created_at` | string | ✅ | RFC 3339 timestamp |
| `checkpoint_kind` | string | ✅ | Controlled vocabulary (examples below) |
| `result` | object | ✅ | Pass/fail/warn + details |
| `subject` | object | ✅ | The “thing being checked” (dataset/run/response) |
| `actor` | object | ✅ | Agent/service creating the checkpoint |
| `inputs` | array | ✅ | Artifact refs + hashes used for the decision |
| `links` | object | ✅ | At minimum `audit_ref` (API-resolvable) |

### `subject` (recommended shape)

- `type`: `dataset` | `run` | `api_response` | `catalog_entry` | `artifact`
- `id`: stable identifier in your system (string)
- `version`: optional version tag/commit/run-id (string)
- `uri`: optional canonical URI (string)

### `actor` (recommended shape)

- `type`: `service` | `human`
- `id`: stable identifier (service account, user id, etc.)
- `role`: optional role string (e.g., `pipeline`, `policy_engine`, `release_manager`)
- `on_behalf_of`: optional delegator id (string)

### `inputs[]` items (recommended shape)

- `role`: `source` | `config` | `policy_bundle` | `catalog` | `artifact`
- `ref`: URI-ish pointer (do **not** require direct storage access)
- `hash`: content hash string (e.g., `sha256:...`)
- `media_type`: optional (e.g., `application/geo+json`, `application/pdf`)

### `result` (recommended shape)

- `status`: `pass` | `fail` | `warn`
- `summary`: human-readable short string
- `reason_code`: stable machine-readable code (string)
- `violations`: optional array of `{code, message, severity, path?}`

### `links` (recommended shape)

- `audit_ref`: API-resolvable reference (string)
- `evidence_ref`: optional pointer to evidence bundle (string)
- `run_ref`: optional pointer to run record (string)

> [!WARNING]
> **Do not** embed secrets, tokens, or private URLs in checkpoint records.  
> Checkpoints should be safe to replicate into lower-trust environments (with redaction where needed).

---

## Controlled vocabularies

Treat these as versioned “registries” (recommended):

- `checkpoint_kind` — examples:
  - `ingest.schema_validate`
  - `ingest.geospatial_sanity`
  - `policy.request_authorize`
  - `promotion.raw_to_work`
  - `promotion.work_to_processed`
  - `serve.focus_mode_response`
  - `catalog.publish`

- `severity` — examples: `info`, `low`, `medium`, `high`, `critical`

> [!NOTE]
> Keep vocabularies **stable**. Additive changes are fine; breaking renames require a new schema version.

---

## Deterministic IDs and hashing

If `checkpoint_id` is deterministic, two independent systems emitting the *same checkpoint* will converge on the *same ID*.

Recommended pattern:
1. Select the **fingerprint fields** (stable subset).
2. Canonicalize JSON deterministically (JCS / RFC 8785 style canonicalization recommended).
3. Hash with SHA-256.
4. Prefix with algorithm: `sha256:<hex>`.

Example fingerprint fields (recommended):
- `schema`
- `checkpoint_kind`
- `subject.{type,id,version}`
- `inputs[].{role,hash}` (sorted by `role,hash`)
- `result.status`
- `policy_hash` (if applicable)

> [!TIP]
> If timestamps cause non-determinism, keep `created_at` **out** of the fingerprint and store it as metadata.

---

## Redaction and sensitivity

Audit artifacts can leak sensitive information (locations, personal identifiers, internal paths).

Recommended approach:
- Define a redaction policy per checkpoint kind.
- Separate **internal checkpoints** from **public checkpoints** if needed.
- Treat coordinates as sensitive by default unless explicitly cleared.

> [!IMPORTANT]
> CARE/FAIR governance applies to audit logs too: don’t publish what communities or policies say must not be shared.

---

## Validation and CI gates

**Schema is policy.** Treat schema changes as production changes.

Recommended CI checks:
- ✅ JSON Schema validation (self-validate schema)
- ✅ Example fixtures validate against schema
- ✅ Fail-closed gate: schema or example failures block merge/promotion
- ✅ Contract tests across producers/consumers (pipeline, API, UI)

---

## Mapping to PROV

If you maintain a PROV layer, checkpoints map cleanly:

- checkpoint ≈ `prov:Activity`
- subject & inputs ≈ `prov:Entity`
- actor ≈ `prov:Agent`
- result/decision ≈ activity attributes + derived entities (optional)

This mapping is useful when you want a checkpoint to be a *thin receipt* that links into a richer provenance bundle.

---

## Example checkpoint (illustrative)

```json
{
  "schema": "io.kfm.audit.checkpoint.v1",
  "checkpoint_id": "sha256:2d3b1c...example",
  "created_at": "2026-02-18T15:04:05Z",
  "checkpoint_kind": "promotion.work_to_processed",
  "subject": {
    "type": "dataset",
    "id": "ks-water-rights",
    "version": "run:2026-02-18T15:00Z"
  },
  "actor": {
    "type": "service",
    "id": "kfm-pipeline-orchestrator",
    "role": "pipeline"
  },
  "inputs": [
    {
      "role": "artifact",
      "ref": "kfm://object/processed/ks-water-rights/v3.parquet",
      "hash": "sha256:9b7c...example",
      "media_type": "application/x-parquet"
    },
    {
      "role": "catalog",
      "ref": "kfm://catalog/dcat/ks-water-rights.json",
      "hash": "sha256:aa12...example",
      "media_type": "application/json"
    }
  ],
  "result": {
    "status": "pass",
    "summary": "Promotion allowed: receipts + catalogs present; policy checks passed.",
    "reason_code": "PROMOTION_OK"
  },
  "links": {
    "audit_ref": "kfm://audit/ckpt/sha256:2d3b1c...example",
    "evidence_ref": "kfm://evidence/bundle/sha256:77a0...example",
    "run_ref": "kfm://runs/sha256:abcd...example"
  }
}
```

> [!NOTE]
> The example uses `kfm://...` URIs as placeholders (not confirmed in repo).  
> Replace with your actual governed URI scheme and resolvers.

---

## Change rules

✅ Allowed without bumping major:
- Add optional fields
- Add new `checkpoint_kind` values (vocab bump)
- Add new violation codes

🚫 Requires new major schema (`v2`, `v3`, ...):
- Rename/remove fields
- Change required fields
- Change semantics of existing fields

---

## Definition of Done

- [ ] Schema contract exists and is versioned (schema + examples)
- [ ] Fail-closed CI gate exists (policy/schema/attestation) and is required for merge/promotion
- [ ] ≥ 1 end-to-end integration test covers a happy path and a fail-closed path
- [ ] Audit/evidence links resolve through the governed API boundary (no direct storage access from UI)
- [ ] Governance review notes recorded for sensitivity/sovereignty-related changes
