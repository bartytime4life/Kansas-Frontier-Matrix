<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/local-data-manifest
title: Local data quarantine capture manifest
type: semantic-contract; operator-input
version: v0.1
status: proposed; branch-review; quarantine-only
owners: ["@bartytime4life"]
created: 2026-09-17
updated: 2026-09-17
policy_label: public-documentation
owning_root: contracts/
truth_posture: implementation and tests are branch evidence; independent acceptance pending
notes: ["Directory Rules ADR-0029 applies. No source admission, release, deployment, or publication authority."]
[/KFM_META_BLOCK_V2] -->

# Local data quarantine capture manifest

Status: proposed operator-input contract; implemented behavior must be verified at
the branch under review. This manifest never admits a source or grants release
authority. Its machine shape lives in
[`schemas/contracts/v1/source/local_data_manifest.schema.json`](../../schemas/contracts/v1/source/local_data_manifest.schema.json).

## Purpose and ownership

An explicit manifest selects already downloaded maps, pictures, archives,
documents, and other regular files for bounded offline preservation. The
repository operator in [`tools/local_data/`](../../tools/local_data/) delegates
byte capture to the existing `connectors/local_upload/` source edge. The
operator's physical store is outside the checkout, with logical lifecycle homes
under `data/`. Placement follows accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and [Directory Rules](../../docs/doctrine/directory-rules.md) §§10.1, 11.4, 12.3.

This is an operator input, not a parallel source registry, SourceDescriptor,
SourceArtifact, SourceActivationDecision, EvidenceBundle, or ReleaseManifest.
`source_id` is a declared association, not evidence of canonical registration.
The existing source registry and admission process retain their authority.

## Input meaning

The object has `schema_version: "1"` and a nonempty `items` array. Each item has:

| Field | Meaning |
|---|---|
| `source_id`, `dataset_id`, `version` | Declared source, dataset, and immutable capture revision; corrections use a new version. |
| `domain` | Classification for downstream review; never a duplicate byte store. |
| `relative_path` | POSIX-style path relative to the operator's downloads directory. No absolute paths, traversal, backslashes, symlinks, or special files. |
| `source_uri` | Credential-free original reference: HTTPS, `kfm://`, or opaque `file-ref:`. Never fetched by this tool. |
| `media_type` | Declared native content type; does not prove format validity. |
| `rights.license_id` | Operator-supplied license identifier or `null` when unknown. |
| `rights.redistribution` | `unknown`, `allowed`, `restricted`, or `denied`; a snapshot assertion, never an authorization. |
| `sensitivity` | `unknown`, `public`, `restricted`, or `controlled`; no value bypasses quarantine. |
| `sha256`, `size_bytes` | Exact expected byte identity. A checksum computed locally detects later changes, not provider authenticity. |
| `captured_at` | Operator-recorded capture time in whole-second UTC, ending in `Z`; not observation time or historical coverage. |

HTTPS references cannot contain credentials, query strings, or fragments; keep
signed URLs and tokens out of manifests. Provider request details and historical
coverage belong in reviewed source metadata. Unknown fields, duplicate JSON
keys, nonfinite numbers, empty manifests, conflicting identities, and configured
resource-limit breaches fail closed. JSON Schema handles shape; the operator
additionally enforces filesystem and byte invariants. No filename, media type,
checksum, or operator rights assertion establishes scientific validity.

## Synchronization and recovery

`plan` performs no writes or network requests. `sync` checks expected bytes and
captures only explicitly selected files into QUARANTINE. Existing valid objects
are reused; old versions remain. A missing upstream file is never a deletion
instruction. Existing corrupt destination bytes are a failure, not permission to
overwrite. There is no latest-pointer promotion or public path.

The store retains the canonical manifest snapshot and per-source process receipts
using the existing [IngestReceipt shape](../../schemas/contracts/v1/source/ingest_receipt.schema.json).
These receipts mean local capture/integrity processing only, not governed source
admission. Failed or interrupted batches may leave independently verified
quarantined objects. Re-running the exact manifest verifies them and completes
missing process records. No successful batch is claimed before required outputs
are durable. Partial temporary files are not accepted payloads.

## Limits and validation

The default envelope is 1,000 items, 8 GiB per file, 64 GiB per batch, a 4 MiB
manifest, and 256 MiB of free-space reserve. Operator reductions are supported;
any increases remain bounded by the implementation's explicit checks. Streaming
limits memory use independently of payload size. No recursive discovery,
archive extraction, HTTP, scheduler, executable payload, source activation,
normalization, or lifecycle promotion is included.

Validation lives in [`tests/local_data/`](../../tests/local_data/). Run
`make local-data-check` for the contract, capture, path-safety, recovery, and
doctor checks. Local success does not imply hosted CI, independent review,
production map integration, or operating-system portability acceptance.

## Retention and correction

Retention and legal holds are operator-owned. The tool does not garbage-collect,
delete, repair by overwrite, encrypt a drive, or configure host access control.
Keep the physical store private; backups must preserve payloads, manifests, and
receipts together. Restoring and verifying a backup does not publish its contents.
See the [local-PC runbook](../../docs/runbooks/local-pc-data-store.md) for update,
backfill, backup, correction, and remaining integration steps.
