# `data/audit/` — Audit Checkpoints (Local/Dev) 🧾🔒

![Governed Artifact](https://img.shields.io/badge/governed-artifact-critical)
![Append-only](https://img.shields.io/badge/ledger-append--only-111827)
![No Secrets](https://img.shields.io/badge/constraint-no%20secrets-critical)
![Fail Closed](https://img.shields.io/badge/posture-fail--closed-111827)
![Dev Only](https://img.shields.io/badge/scope-local%2Fdev%20checkpoints-6b7280)

> [!IMPORTANT]
> This folder is **dev/local-only**: it stores **bounded, reviewable audit checkpoints** and small fixtures.
> **Do not commit production audit logs** here unless governance explicitly approves it (size + sensitivity + retention).

> [!WARNING]
> **Must never contain secrets.** No tokens, credentials, cookies, private keys, or raw sensitive payloads.
> If unsure: **do not store it**; store a reference/hash and keep the sensitive content in secured stores.

---

## Governance Header

| Field | Value |
|---|---|
| Document | `data/audit/README.md` |
| Status | **Governed** |
| Version | `v1.0.0` |
| Effective date | `2026-02-16` |
| Owners | `.github/CODEOWNERS` |
| Scope | Audit checkpoint storage + integrity verification rules + “no secrets” constraints |
| Default posture | **Fail closed** (invalid/missing checkpoint → deny/abstain) |
| Change control | Any semantic changes require governance review (treat like policy/schema changes) |

---

## Table of Contents

- [Purpose](#purpose)
- [Non-negotiables](#non-negotiables)
- [Directory layout](#directory-layout)
- [AuditRecord contract](#auditrecord-contract)
- [Checkpoint format](#checkpoint-format)
- [Integrity verification](#integrity-verification)
- [Security and sensitivity](#security-and-sensitivity)
- [CI gates](#ci-gates)
- [Glossary](#glossary)
- [Related docs](#related-docs)

---

## Purpose

`data/audit/` exists to support **inspectability** and **governance verification** in local/dev workflows:

- Provide **bounded checkpoint exports** of the audit ledger for debugging, demos, and reproducible tests.
- Enable **integrity verification drills** (e.g., “verify hash chain after restore”).
- Keep audit artifacts near the **truth path** docs (`data/**`) without turning git into a production log sink.

> [!NOTE]
> In production, audit storage is commonly implemented as an **append-only ledger** in a database with **periodic checkpointing** to an immutable object store (with checksums).  
> This repo folder is the **local/dev mirror** of that checkpoint concept.

---

## Non-negotiables

1) **Append-only semantics**  
   - Checkpoints are immutable snapshots.
   - Never rewrite historical checkpoint files; create a new checkpoint instead.

2) **No secrets / no private keys**  
   - Never store credentials.
   - Never store auth headers, session cookies, OAuth tokens, API keys, SSH keys, etc.

3) **Trust membrane stays intact**  
   - UI/external clients must never read `data/audit/**` directly.
   - Access is always through the **governed API** + **policy decision point**.

4) **Fail closed**  
   - If checkpoint integrity can’t be verified: dependent features must **deny** (or **abstain**) rather than “best effort allow.”

5) **Privacy-safe logging**  
   - Prefer **references** (IDs, hashes, resolvers) over raw payloads (user text, coordinates, PII).

---

## Directory layout

```text
data/audit/
├─ README.md
└─ checkpoints/
   ├─ YYYY/
   │  └─ YYYY-MM/
   │     ├─ audit_checkpoint_YYYY-MM-DD.ndjson
   │     ├─ audit_checkpoint_YYYY-MM-DD.manifest.json
   │     └─ checksums.sha256
   └─ latest.ref.json   (optional pointer for tooling; do not treat as canonical truth)
```

### What each file is for

| Path | Required? | Purpose | Notes |
|---|---:|---|---|
| `checkpoints/**/audit_checkpoint_*.ndjson` | ✅ | Append-only export of `AuditRecord` events | One JSON object per line (NDJSON) |
| `checkpoints/**/audit_checkpoint_*.manifest.json` | ✅ | Snapshot metadata (range, counts, hashes) | Keep small; no sensitive payloads |
| `checkpoints/**/checksums.sha256` | ✅ | File integrity (sha256) | Must cover `.ndjson` and `.manifest.json` |
| `checkpoints/latest.ref.json` | | Convenience pointer | Optional; never required for verification |

> [!TIP]
> Prefer month-partitioning (`YYYY/YYYY-MM/`) to avoid giant directories and to keep review diffs manageable.

---

## AuditRecord contract

The **minimum** audit record is intentionally small and composable: it stores “what happened,” “who/what did it,” and “what evidence/policy context was involved.”

### Required fields (minimum)

| Field | Type | Required | Meaning |
|---|---|---:|---|
| `audit_ref` | string | ✅ | Stable handle for this audit event |
| `timestamp` | RFC3339 string | ✅ | Event time (UTC recommended) |
| `actor` | object | ✅ | Privacy-safe actor metadata (role/claims/service) |
| `event_type` | string | ✅ | e.g., `promotion`, `focus_answer`, `policy_decision` |
| `subject` | object | ✅ | Resource being acted on (dataset/version/run/story/etc.) |
| `evidence_refs` | string[] | ✅ | Resolver refs / bundle digests / citations used |
| `prev_hash` | string | | Prior event hash (for tamper-evident chaining) |
| `event_hash` | string | | This event hash (for tamper-evident chaining) |

### Recommended conventions

- `audit_ref` should be **unique** and **sortable** (ULID-style is a good fit).
- `actor` should avoid PII (do **not** store email addresses). Prefer:
  - `actor.role` (e.g., `public`, `reviewer`, `admin`, `service`)
  - `actor.subject` (opaque ID) or `actor.service_name`
- `subject` should store identifiers, not raw bytes. Typical keys:
  - `dataset_id`, `version_id`, `run_id`, `story_id`, `endpoint`, `resource_kind`
- `evidence_refs` should include stable resolvers/digests whenever possible (e.g., bundle digests; `prov://...`, `stac://...`, `dcat://...`, `doc://...`).

### Tamper-evident hashing (recommended)

If you implement hash chaining:

- Compute `event_hash = sha256(JCS(event_without_event_hash))`
- Include `prev_hash` inside the hashed payload
- Use a canonical JSON scheme (e.g., RFC 8785 JCS) to avoid hash drift across runtimes

<details>
<summary><strong>Example AuditRecord (illustrative)</strong></summary>

```json
{
  "audit_ref": "audit_01J0EXAMPLEZ7P6M7V8Q3S8V",
  "timestamp": "2026-02-16T18:34:56Z",
  "actor": { "role": "service", "service_name": "kfm-api", "claims": ["policy_enforced"] },
  "event_type": "focus_answer",
  "subject": {
    "endpoint": "POST /api/v1/ai/query",
    "view_state": { "bbox_coarse": [-102.0, 36.9, -94.6, 40.0], "time_range": ["1854-01-01", "1870-12-31"] }
  },
  "evidence_refs": [
    "bundle:sha256:deadbeef...",
    "prov://catalog/prov/dataset_x/run_run_2026-02-16T...",
    "doc://evidence/maps/usgs_sheet_1872#page=4"
  ],
  "prev_hash": "sha256:aaaa...",
  "event_hash": "sha256:bbbb..."
}
```

</details>

> [!CAUTION]
> If `event_hash`/`prev_hash` are present, **they must validate**.  
> If they are present but invalid, treat as a **governance incident** and fail closed.

---

## Checkpoint format

A checkpoint is a bounded snapshot of audit events.

### Files

1) **NDJSON event stream** (`audit_checkpoint_YYYY-MM-DD.ndjson`)  
Each line is a full `AuditRecord` JSON object.

2) **Manifest** (`audit_checkpoint_YYYY-MM-DD.manifest.json`)  
Minimal metadata required for auditability and verification:

Recommended manifest fields:

| Field | Type | Meaning |
|---|---|---|
| `checkpoint_ref` | string | Stable identifier for this checkpoint |
| `generated_at` | string | Timestamp when generated |
| `range` | object | `{start, end}` timestamps or `{min_ref, max_ref}` |
| `record_count` | number | Number of records included |
| `first_event_hash` / `last_event_hash` | string | Optional, for fast verification |
| `notes` | string | Optional, non-sensitive description |

3) **Checksums** (`checksums.sha256`)  
Must include sha256 sums for:
- `audit_checkpoint_*.ndjson`
- `audit_checkpoint_*.manifest.json`

> [!IMPORTANT]
> The **manifest** must never include secrets or raw sensitive payloads. It should only contain bounded metadata.

---

## Integrity verification

Minimum verification steps for a checkpoint:

### 1) File integrity (required)

- Verify sha256 for `.ndjson` and `.manifest.json` matches `checksums.sha256`.

### 2) Schema integrity (required)

- Parse NDJSON (every line must be valid JSON).
- Validate each record against the `AuditRecord` contract (required fields present).

### 3) Chain integrity (if hash chaining is enabled)

- Recompute each `event_hash` from canonical JSON (excluding `event_hash` itself).
- Verify that each `prev_hash` matches the prior record’s `event_hash`.

### 4) Restore drill requirement (ops)

After restoring audit storage from backup, **verify the hash chain** on the restored checkpoint set before trusting audit queries.

> [!TIP]
> A good “restore drill” is: restore → verify checksums → verify NDJSON parse → verify hash chain → run one governed query → confirm audit_ref resolves.

---

## Security and sensitivity

Audit logs are evidence artifacts and can leak information if mishandled.

### Must not store

- Credentials/tokens/secrets of any kind
- User emails, phone numbers, addresses
- Precise restricted coordinates (especially sensitive archaeology/cultural locations)
- Raw “question text” or raw content payloads (unless explicitly approved and redaction-safe)

### Prefer to store instead

- Opaque IDs (`user_id` pseudonymous), roles, scopes
- Hashes of payloads (`question_hash`) rather than full text
- Coarsened view state (generalized bbox/time windows)
- Evidence resolvers (bundle digests, prov/stac/dcat/doc refs)
- Policy metadata (e.g., policy bundle hash, reason codes) — as bounded strings

> [!WARNING]
> If you discover sensitive leakage in an audit artifact, treat it like a production incident:
> deny access via policy, preserve the audit trail, and produce a redacted replacement as a new version/checkpoint.

---

## CI gates

Recommended checks that should eventually be wired into CI (fail closed once enforced):

- [ ] Checkpoints are **append-only** (no edits to existing checkpoint files)
- [ ] `checksums.sha256` exists and validates for each checkpoint
- [ ] NDJSON parses cleanly; no malformed records
- [ ] Required fields present for each `AuditRecord`
- [ ] **No secrets** scan passes (high-signal patterns; include allowlist for false positives)
- [ ] If `event_hash` fields exist, **hash chain validates**
- [ ] (When enabled) Promotion receipts require an audit event referencing `run_id` + `version_id`
- [ ] (When enabled) Focus Mode outputs always include `audit_ref` and citations resolve or abstain

> [!NOTE]
> Actual merge-blocking enforcement is defined in `.github/` (required checks + job names).  
> If this README promises a gate that CI doesn’t enforce, treat that mismatch as a governance gap.

---

## Glossary

| Term | Meaning |
|---|---|
| **audit ledger** | Append-only record of governed system events |
| **audit_ref** | Stable handle that points to an audit event/record |
| **checkpoint** | Bounded snapshot export of audit events (immutable) |
| **NDJSON** | Newline-delimited JSON; one JSON object per line |
| **event_hash / prev_hash** | Optional tamper-evident chain fields (hash linked list) |
| **evidence_refs** | Resolver references/digests to the evidence used for decisions/claims |
| **fail closed** | If integrity/validation is missing or inconclusive → deny/abstain |

---

## Related docs

- Repo guarantees: `../../README.md`
- Data plane contract: `../README.md`
- Governance + CI gatehouse contract: `../../.github/README.md`
- Policy posture (OPA/Rego): `../../policy/README.md`
- Docs governance + templates: `../../docs/README.md`
