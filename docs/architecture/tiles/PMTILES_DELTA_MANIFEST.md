<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: PMTiles Delta Manifest
type: standard
version: v1
status: draft
owners: OWNER_TBD
created: TODO(date): original creation date not provided
updated: 2026-05-01
policy_label: NEEDS VERIFICATION: document access label not confirmed
related: ["PROPOSED: contracts/kfm/delta_manifest.v1.json", "PROPOSED: tools/validators/tiles/validate_delta_manifest.py", "PROPOSED: policy/tiles/delta_manifest.rego", "PROPOSED: policy/tiles/delta_manifest_test.rego", "PROPOSED: tests/fixtures/tiles/delta_manifest/", "PROPOSED: .github/workflows/tiles-ci.yml"]
tags: [kfm, pmtiles, tiles, delta, manifest, publication, rollback]
notes: ["PROPOSED PMTiles time-sliced delta publication-control slice; implementation and CI wiring remain NEEDS VERIFICATION"]
[/KFM_META_BLOCK_V2] -->

# PMTiles Delta Manifest

A governed manifest contract for PMTiles delta slices, tile-level integrity checks, rollback posture, and receipt-linked publication control.

> [!IMPORTANT]
> **Status:** PROPOSED / draft  
> **Object family:** `delta_manifest.v1`  
> **Scope:** PMTiles time-sliced delta publication control slice  
> **Implementation depth:** UNKNOWN until the target repo, schema, validator, policy, tests, CI workflow, receipts, and emitted artifacts are inspected.

## Quick navigation

- [Purpose](#purpose)
- [Operating law](#operating-law)
- [Lifecycle placement](#lifecycle-placement)
- [Manifest contract](#manifest-contract)
- [Client verification behavior](#client-verification-behavior)
- [Fail-closed rules](#fail-closed-rules)
- [Rollback posture](#rollback-posture)
- [Implementation references](#implementation-references)
- [Illustrative manifest](#illustrative-manifest)
- [Verification checklist](#verification-checklist)
- [Open verification backlog](#open-verification-backlog)

## Purpose

`delta_manifest.v1` defines a governed manifest for PMTiles delta slices so clients, validators, policy gates, and promotion workflows can verify:

- which base PMTiles archive the delta is tied to;
- which time interval the delta represents;
- which tiles were added, modified, or removed;
- whether rollback digests exist where rollback requires them;
- whether every tile change resolves to a run receipt;
- whether public references stay out of `RAW`, `WORK`, and `QUARANTINE`;
- whether masked-area thresholds require review or denial before promotion.

The manifest is a **publication-control object**, not the canonical spatial truth. PMTiles remains a map-delivery artifact downstream of source evidence, transforms, receipts, proof objects, catalog records, review state, and promotion decisions.

## Operating law

This manifest preserves the KFM trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The delta manifest may support publication, rollback, and client verification, but it does not replace:

- source descriptors;
- EvidenceBundles;
- transform receipts;
- validation reports;
- policy decisions;
- catalog/proof objects;
- release manifests;
- review records;
- correction notices;
- rollback cards.

> [!WARNING]
> A PMTiles delta that cannot prove its base archive, tile digests, receipt linkage, path boundaries, masked-percentage posture, and rollback semantics must not be promoted for public use.

## Lifecycle placement

```mermaid
flowchart LR
  A["Published base PMTiles archive<br/>base_pmtiles.url + spec_hash"] --> B["Delta build<br/>time_start / time_end + tile changes"]
  B --> C["Schema validation<br/>contracts/kfm/delta_manifest.v1.json"]
  C --> D["Semantic validation<br/>counts, digests, rollback, receipts"]
  D --> E["Policy gate<br/>forbidden strata + masked thresholds"]
  E --> F{"Promotion decision"}
  F -- pass --> G["PUBLISHED delta manifest<br/>released artifact reference"]
  F -- review --> H["Review queue<br/>masked_pct or policy-sensitive"]
  F -- deny/error --> I["QUARANTINE / correction path<br/>receipt + validation report"]
```

## Definitions

| Term | Meaning |
| --- | --- |
| `base_pmtiles` | The already-published PMTiles archive that the delta is calculated against. |
| `spec_hash` | Deterministic identity for the base archive specification or content contract. Exact cross-family hash rules remain `NEEDS VERIFICATION`. |
| `delta_id` | Stable identifier for this delta manifest. It should be deterministic where practical. |
| `time_start` / `time_end` | ISO date-time interval covered by the tile delta. |
| `tile` | A changed PMTiles tile entry identified by tile coordinate and action. |
| `prior_digest` | Digest of the tile state before the delta. Required for rollback when a tile is modified or removed. |
| `new_digest` | Digest of the tile state after the delta. Required when a tile is added or modified. |
| `run_receipt_url` | Link or governed artifact reference to the run receipt that explains how this tile change was produced. |
| `masked_pct` | Percentage of the tile masked, generalized, redacted, or otherwise withheld for policy/sensitivity reasons. |
| `signature` | Optional signature metadata. `cosign` is permitted as a manifest entry method, but execution policy remains `NEEDS VERIFICATION`. |

## Manifest contract

### Top-level fields

| Field | Required | Rule |
| --- | ---: | --- |
| `manifest_version` | Yes | Must equal `v1`. |
| `delta_id` | Yes | Non-empty stable identifier. |
| `base_pmtiles.url` | Yes | Must point to the published base archive, not raw/work/quarantine storage. |
| `base_pmtiles.spec_hash` | Yes | Non-empty deterministic base identity. |
| `base_pmtiles.etag` | No | Optional upstream or storage ETag. |
| `time_start` | Yes | ISO date-time. Must be earlier than `time_end`. |
| `time_end` | Yes | ISO date-time. Must be later than `time_start`. |
| `expected_tile_count` | Yes | Expected number of tile changes. |
| `produced_tile_count` | Yes | Produced number of tile changes; must match the number of entries in `tiles[]`. |
| `tiles[]` | Yes | Tile-level change entries. Empty deltas are not accepted unless a future ADR explicitly permits no-op manifests. |
| `qc.masked_pct_pass_threshold` | Yes | Tile entries at or below this threshold may pass masked-percentage QC if all other gates pass. |
| `qc.masked_pct_review_threshold` | Yes | Tile entries above this threshold fail promotion or require review according to policy. |
| `signatures[]` | No | Optional signature records. `method=cosign` is allowed, but verification execution policy is not standardized in this document. |

### Tile entry fields

| Field | Required | Rule |
| --- | ---: | --- |
| `z` | Yes | Integer zoom level. |
| `x` | Yes | Integer tile x coordinate. |
| `y` | Yes | Integer tile y coordinate. |
| `action` | Yes | One of `added`, `modified`, `removed`. |
| `new_digest` | Conditional | Required for `added` and `modified`; must be null for `removed`. |
| `prior_digest` | Conditional | Required for `modified` and `removed`; must be null for `added`. |
| `masked_pct` | Yes | Number from 0 to 100. |
| `run_receipt_url` | Yes | Non-empty governed receipt reference. Must not reference `RAW`, `WORK`, or `QUARANTINE`. |

Recommended digest form for v1 is `sha256:<64 lowercase hex characters>` unless an existing KFM digest convention requires a different canonical digest format.

## Canonical manifest hash

Clients and validators should recompute the canonical manifest hash from sorted-key canonical JSON.

The hash should be computed over the manifest content using the repository’s approved canonicalization rule. Until cross-object-family standardization is confirmed, this document treats hash embedding as `NEEDS VERIFICATION`.

Recommended interim behavior:

1. Normalize the manifest to canonical JSON with sorted object keys.
2. Encode as UTF-8.
3. Hash the canonical bytes.
4. Store the resulting hash in the validation report, run receipt, proof pack, or promotion decision.
5. Do not add an embedded self-referential hash field unless an ADR defines whether that field is excluded from the hash input.

## Client verification behavior

Clients and policy gates should verify the manifest before public use.

Minimum behavior:

1. Validate the manifest against `contracts/kfm/delta_manifest.v1.json`.
2. Recompute canonical manifest hash from sorted-key canonical JSON.
3. Confirm `base_pmtiles.spec_hash` is present and well-formed.
4. Confirm `produced_tile_count == len(tiles[])`.
5. Confirm tile coordinate identities are unique within the manifest.
6. Enforce rollback-safety semantics:
   - `modified` and `removed` require non-null `prior_digest`;
   - `added` requires null `prior_digest`;
   - `added` and `modified` require non-null `new_digest`;
   - `removed` requires null `new_digest`.
7. Enforce receipt linkage:
   - every tile requires non-empty `run_receipt_url`.
8. Enforce public path boundaries:
   - public references to `RAW`, `WORK`, or `QUARANTINE` are denied.
9. Enforce masked-percentage QC:
   - values above the review threshold fail promotion or require review according to policy.
10. Return a finite validation result: `PASS`, `REVIEW`, `DENY`, or `ERROR`.

## Fail-closed rules

Validation fails closed when any of the following is true:

| Rule | Outcome |
| --- | --- |
| Any digest is malformed. | `DENY` |
| `base_pmtiles.spec_hash` is missing or empty. | `DENY` |
| `produced_tile_count` does not match `tiles.length`. | `DENY` |
| `expected_tile_count` does not match `produced_tile_count`. | `DENY` |
| `time_start >= time_end`. | `DENY` |
| Any tile action is outside `added`, `modified`, `removed`. | `DENY` |
| A rollback-required tile lacks `prior_digest`. | `DENY` |
| An `added` tile has non-null `prior_digest`. | `DENY` |
| A `removed` tile has non-null `new_digest`. | `DENY` |
| Any tile lacks `run_receipt_url`. | `DENY` |
| A public reference points to `RAW`, `WORK`, or `QUARANTINE`. | `DENY` |
| `masked_pct` exceeds `qc.masked_pct_review_threshold`. | `REVIEW` or `DENY`, depending on policy. |
| Optional `cosign` signature metadata exists but required signature verification policy is enabled and cannot verify it. | `DENY` or `ERROR`, depending on failure type. |

## Policy boundary

The Rego policy should evaluate at least:

- manifest version;
- base archive identity;
- tile count consistency;
- digest format;
- rollback digest semantics;
- receipt URL presence;
- forbidden storage strata;
- masked percentage thresholds;
- optional signature metadata shape;
- public-release eligibility.

Policy must treat forbidden storage strata as a hard denial for public output. A manifest may be useful for internal debugging and still be denied for publication.

## Rollback posture

Rollback is only safe when tile-level rollback information is present and receipt-linked.

| Action | Rollback requirement |
| --- | --- |
| `added` | Remove or ignore the added tile in the rollback target; `prior_digest` must be null. |
| `modified` | Restore the tile state identified by `prior_digest`. |
| `removed` | Restore the tile state identified by `prior_digest`. |

Rollback should emit a separate rollback receipt or rollback card that references:

- `delta_id`;
- canonical manifest hash;
- affected tile count;
- base PMTiles `spec_hash`;
- rollback target archive or release alias;
- operator or automation identity;
- policy decision;
- validation report;
- timestamp;
- reason for rollback.

## Implementation references

These paths are from the source draft and remain `PROPOSED / NEEDS VERIFICATION` until the target repo is inspected.

| Surface | Proposed path | Status |
| --- | --- | --- |
| Schema | `contracts/kfm/delta_manifest.v1.json` | PROPOSED / NEEDS VERIFICATION |
| Validator | `tools/validators/tiles/validate_delta_manifest.py` | PROPOSED / NEEDS VERIFICATION |
| Policy | `policy/tiles/delta_manifest.rego` | PROPOSED / NEEDS VERIFICATION |
| Policy tests | `policy/tiles/delta_manifest_test.rego` | PROPOSED / NEEDS VERIFICATION |
| Fixtures | `tests/fixtures/tiles/delta_manifest/` | PROPOSED / NEEDS VERIFICATION |
| CI workflow | `.github/workflows/tiles-ci.yml` | PROPOSED / NEEDS VERIFICATION |

> [!NOTE]
> If the mounted repository proves that `schemas/` rather than `contracts/` is the canonical machine-schema home, do not create parallel authority. Resolve through an ADR and a compatibility note before landing machine-readable files.

## Illustrative manifest

This example is illustrative. It is not evidence that a fixture exists in the repo.

```json
{
  "manifest_version": "v1",
  "delta_id": "delta-2026-05-01-example",
  "base_pmtiles": {
    "url": "published/tiles/kansas/base.pmtiles",
    "spec_hash": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
    "etag": "example-etag"
  },
  "time_start": "2026-05-01T00:00:00Z",
  "time_end": "2026-05-01T06:00:00Z",
  "expected_tile_count": 1,
  "produced_tile_count": 1,
  "qc": {
    "masked_pct_pass_threshold": 5,
    "masked_pct_review_threshold": 20
  },
  "tiles": [
    {
      "z": 8,
      "x": 56,
      "y": 105,
      "action": "modified",
      "prior_digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "new_digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
      "masked_pct": 0.25,
      "run_receipt_url": "published/receipts/tiles/delta-2026-05-01-example.run_receipt.json"
    }
  ],
  "signatures": [
    {
      "method": "cosign",
      "sig_url": "published/proofs/tiles/delta-2026-05-01-example.cosign.bundle"
    }
  ]
}
```

## Compatibility and versioning

`manifest_version = v1` is the only version defined by this document.

Breaking changes require one of:

- a new manifest version such as `v2`;
- an ADR defining compatibility behavior;
- a migration note and fixture set;
- validator support for old and new versions during a defined transition period.

Non-breaking changes may include optional fields when they do not weaken rollback safety, path-boundary checks, receipt linkage, policy posture, or canonical hash behavior.

## Verification checklist

- [ ] Confirm target document path or create ADR-backed placement.
- [ ] Confirm schema home: `contracts/` vs `schemas/`.
- [ ] Confirm `contracts/kfm/delta_manifest.v1.json` exists or is created.
- [ ] Confirm digest format and canonical JSON rule.
- [ ] Confirm whether canonical manifest hash is embedded, receipt-stored, or proof-pack-stored.
- [ ] Confirm validator rejects malformed digests.
- [ ] Confirm validator rejects missing `base_pmtiles.spec_hash`.
- [ ] Confirm validator rejects count mismatches.
- [ ] Confirm validator rejects invalid rollback digest semantics.
- [ ] Confirm policy denies public references to `RAW`, `WORK`, and `QUARANTINE`.
- [ ] Confirm masked percentage thresholds produce `PASS`, `REVIEW`, or `DENY`.
- [ ] Confirm every tile requires a non-empty `run_receipt_url`.
- [ ] Confirm optional `cosign` entries have a defined verification execution policy before promotion depends on them.
- [ ] Confirm fixtures cover valid, review, deny, and error cases.
- [ ] Confirm CI workflow runs schema, semantic validator, and policy tests.
- [ ] Confirm rollback receipt or rollback card behavior.
- [ ] Confirm no client treats PMTiles as canonical evidence.

## Rollback

Rollback is required when a promoted or candidate delta:

- fails digest validation;
- fails receipt resolution;
- points to forbidden storage strata;
- weakens masked/sensitive-location controls;
- loses rollback digests for modified or removed tiles;
- conflicts with the base archive `spec_hash`;
- cannot prove signature state when signature verification is required;
- causes public output to outrun review, policy, or release state.

Rollback target: `ROLLBACK_TARGET_TBD_AFTER_RELEASE_MANIFEST_INSPECTION`

## Open verification backlog

| Item | Status | Required check |
| --- | --- | --- |
| Production deployment wiring | NEEDS VERIFICATION | Confirm `.github/workflows/tiles-ci.yml` is wired into branch protection or release gates. |
| Canonical hash embedding field | NEEDS VERIFICATION | Decide whether hash is embedded, receipt-stored, proof-pack-stored, or all three. |
| Signature verification execution | NEEDS VERIFICATION | Define how `cosign` entries are verified and what failure mode they produce. |
| Schema authority | NEEDS VERIFICATION | Confirm `contracts/` vs `schemas/` canonical machine-contract home. |
| Public path normalization | NEEDS VERIFICATION | Confirm how URL/path normalization detects forbidden `RAW`, `WORK`, and `QUARANTINE` references. |
| Masked percentage semantics | NEEDS VERIFICATION | Confirm whether `masked_pct` is per tile, per feature contribution, or per rendered tile payload. |
| Empty deltas | NEEDS VERIFICATION | Decide whether no-op delta manifests are valid or denied. |
| Tile coordinate bounds | NEEDS VERIFICATION | Confirm zoom/x/y coordinate constraints for supported PMTiles scheme. |
