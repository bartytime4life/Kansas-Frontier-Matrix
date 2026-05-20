<!--
doc_id: NEEDS_VERIFICATION
 title: PMIDX Sidecar Specification V1
 type: standard
 version: v1
 status: draft
 owners: [NEEDS_VERIFICATION]
 created: NEEDS_VERIFICATION
 updated: NEEDS_VERIFICATION
 policy_label: public
 related: [docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md, tools/validators/pmtiles/schemas/pmidx.schema.json]
 tags: [kfm, pmtiles, pmidx, merkle, sidecar]
 notes: [Draft specification; validate against repository conventions before publishing.]
-->

# PMIDX Sidecar Specification V1

`*.pmidx` is the KFM sidecar commitment file for a PMTiles archive. It binds tile/range byte windows to a Merkle root and shared `spec_hash`.

## Required Fields

| Field | Type | Meaning |
|---|---|---|
| `schema_version` | string | Must be `kfm.pmidx.v1`. |
| `spec_hash` | string | SHA-256 digest with `sha256:` prefix. |
| `pmtiles_sha256` | string | SHA-256 digest of the PMTiles archive. |
| `merkle.arity` | integer | Tree arity. Default/recommended: `4`. |
| `merkle.chunk_bytes` | integer | Chunk size used for leaves. |
| `merkle.root` | string | Merkle root with `sha256:` prefix. |
| `merkle.leaves` | array | Ordered leaf hashes. |
| `ranges` | array | Optional range/tile commitments. |

## Minimal Example

```json
{
  "schema_version": "kfm.pmidx.v1",
  "spec_hash": "sha256:0000000000000000000000000000000000000000000000000000000000000000",
  "pmtiles_sha256": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
  "merkle": {
    "arity": 4,
    "chunk_bytes": 1048576,
    "root": "sha256:2222222222222222222222222222222222222222222222222222222222222222",
    "leaves": []
  },
  "ranges": []
}
```

## Verification Rule

A verifier must reject the sidecar when:

- required fields are absent;
- any hash is malformed;
- Merkle root recomputation differs from `merkle.root`;
- `spec_hash` does not match PMTiles metadata and signed payload;
- `pmtiles_sha256` does not match the archive digest.

