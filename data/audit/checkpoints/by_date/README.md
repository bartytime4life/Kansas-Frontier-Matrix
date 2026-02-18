# Audit Ledger Checkpoints — `by_date/` (UTC)

![governed](https://img.shields.io/badge/governed-yes-blue)
![append-only](https://img.shields.io/badge/append--only-yes-blueviolet)
![tamper-evident](https://img.shields.io/badge/tamper--evident-checksums%20%2B%20attestations-informational)

This directory holds **periodic checkpoints** of the **append-only KFM audit ledger**, partitioned by **UTC date**.

A checkpoint is a *small, immutable bundle* (manifest + checksums + optional signatures/attestations) that makes audits and verification fast without scanning the full ledger history.

> [!IMPORTANT]
> **Do not edit** checkpoint artifacts after they are written. If a correction is required, **write a new checkpoint** and reference the prior one (append-only history).

---

## How this fits in KFM

KFM’s architecture treats **audit** and **provenance** as first-class governed artifacts. The audit ledger is authoritative (often a DB table / ledger service), while checkpoints are the **tamper-evident, object-storage snapshots** used for long-term retention, verification, and fast range access.

```mermaid
flowchart LR
  UI[Map UI / Focus Mode UI] -->|requests| API[Governed API]
  API -->|writes audit events| LEDGER[(Audit Ledger\nappend-only)]
  LEDGER -->|periodic export| JOB[Checkpoint job\n(daily or scheduled)]
  JOB --> OBJ[(Object Storage\ncheckpoint bundles)]
  OBJ --> BYDATE[data/audit/checkpoints/by_date/]
  BYDATE --> AUDITTOOLS[Audit / Replay tooling]
```

---

## Directory layout

**Partitioning rule:** `by_date/` is keyed by **UTC** date to keep listings cheap and deterministic across environments.

Recommended layout (hierarchical folders to avoid huge directory listings):

```text
data/audit/checkpoints/by_date/
  YYYY/
    MM/
      DD/
        <checkpoint_id>/
          checkpoint.manifest.json
          audit.events.jsonl
          prov.bundle.jsonld            # optional
          digests.sha256                # required
          attestations/                 # optional (cosign/slsa/etc.)
            *.intoto.jsonl
            *.sig
```

> [!NOTE]
> If you expect **only one** checkpoint per day, you may omit the `<checkpoint_id>/` layer and place files directly under `YYYY/MM/DD/`.
> Keep the date partitioning stable; changing it is a governed decision.

---

## What belongs here

### ✅ Good fits
- **Ledger checkpoints** exported from the authoritative audit store (DB/ledger service).
- Checkpoints covering:
  - ingestion discovery events
  - promotion actions (raw → work → processed)
  - Focus Mode interactions (question/context/answer metadata)
- **Checksums** (always) and **attestations/signatures** (when available) that make checkpoints verifiable.

### ❌ Not allowed
- Secrets, API keys, session tokens, or raw credentials.
- Raw personal data (PII) unless explicitly required by policy and access-controlled (default: don’t store it).
- Any manual edits to checkpoint files after publication.

---

## Checkpoint bundle contract (v1)

This repo does not (yet) pin a single canonical schema for audit checkpoints. The following **minimal contract** is recommended as a thin-slice that supports validation and tamper evidence.

### Required files

| File | Required | Format | Purpose |
|---|---:|---|---|
| `checkpoint.manifest.json` | ✅ | JSON | Declares the checkpoint identity, coverage, and digests. |
| `digests.sha256` | ✅ | text | SHA-256 sums for all files in the bundle (manifest included). |
| `audit.events.jsonl` | ✅* | JSONL | The exported audit events for the checkpoint’s covered range. |
| `prov.bundle.jsonld` | optional | JSON-LD | PROV-O representation of checkpoint/export activity. |
| `attestations/*` | optional | varies | Supply-chain or integrity attestations (e.g., cosign/SLSA). |

\*If the manifest points to an external object (e.g., an object-store URL) instead of embedding events, then `audit.events.jsonl` can be omitted. Keep the “manifest + digests” invariant.

### Manifest fields (recommended)

```json
{
  "@type": "kfm:audit_checkpoint",
  "schema_version": "1.0",
  "checkpoint_id": "kfm-auditcp-2026-02-15T23:59:59Z-<shortdigest>",
  "date_utc": "2026-02-15",
  "created_at": "2026-02-16T00:00:05Z",

  "ledger": {
    "name": "kfm_audit_ledger",
    "from_audit_ref": "auditref:<opaque>",
    "to_audit_ref": "auditref:<opaque>",
    "event_count": 12345
  },

  "digests": {
    "checkpoint.manifest.json": "sha256:<...>",
    "audit.events.jsonl": "sha256:<...>",
    "prov.bundle.jsonld": "sha256:<...>"
  },

  "kfm:run_id": "run:<opaque>",
  "kfm:artifact_digest": "sha256:<digest-of-the-manifest-or-bundle>",
  "kfm:attestation_uri": "oci://<registry>/<path>@sha256:<...>",

  "kfm:source_license": "<spdx-id-or-expression>",
  "kfm:data_sensitivity": "public|internal|restricted"
}
```

<details>
<summary>Why keep <code>kfm:*</code> fields?</summary>

These mirror the “minimal provenance keys” approach used across KFM catalogs/provenance so that:
- policy gates can validate a small, stable set of required fields, and
- the evidence resolver can cross-link audits ↔ provenance ↔ catalogs without bespoke adapters.

</details>

---

## Governance & sensitivity rules

> [!IMPORTANT]
> KFM treats **sensitive locations** and **culturally restricted knowledge** as governed content.  
> If an audit event references restricted assets, the checkpoint must not “downgrade” that sensitivity label.

Operational rules:
- Prefer **references + digests** over embedding sensitive payloads.
- If an audit event includes an “actor” identity, store it as a **stable system identifier** (not an email address) unless policy explicitly requires otherwise.
- Do **not inline secrets** in checkpoint generation jobs; use workload identity / IAM roles and record the emitter identity in audit metadata.
- Checkpoints should be treated as **governed artifacts**: access control applies just like datasets and Story Nodes.

---

## Validation & CI gates (recommended)

To keep this directory **machine-checkable**, add CI gates that fail closed:

- [ ] JSON schema validation for `checkpoint.manifest.json`
- [ ] Verify that `digests.sha256` matches every file in the bundle
- [ ] Validate that the manifest contains:
  - `checkpoint_id`, `date_utc`, `created_at`
  - `kfm:run_id`, `kfm:artifact_digest`, `kfm:attestation_uri`
  - `kfm:source_license`, `kfm:data_sensitivity`
- [ ] (Optional) Sigstore/Cosign verification of any attestation artifacts
- [ ] Policy-as-code rules (OPA/Rego) to block:
  - missing required fields
  - insecure URLs (http://)
  - sensitivity downgrades (e.g., restricted → public)

---

## Creating a new checkpoint (operator runbook)

1. Export audit events from the authoritative ledger store for the target range/date (UTC).
2. Write a new bundle directory: `YYYY/MM/DD/<checkpoint_id>/`.
3. Generate `checkpoint.manifest.json` (deterministic ordering/canonical JSON recommended).
4. Compute SHA-256 for every file and write `digests.sha256`.
5. (If enabled) sign/attest the bundle and store under `attestations/`.
6. Publish the bundle to the configured object store (or commit as a small fixture for dev).
7. Record the checkpoint creation as an **audit event** (so the ledger explains its own checkpoints).

---

## Assumptions & TODOs

- [ ] **Decide** whether checkpoints are **daily** only or may be **hourly** (multiple per day).
- [ ] **Pin** the manifest schema as `schemas/audit/checkpoint.manifest.schema.json` (path not confirmed in repo).
- [ ] **Add** an OPA policy pack for audit checkpoint validation (path not confirmed in repo).
