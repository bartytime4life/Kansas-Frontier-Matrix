# ADR 0003: Canonical `spec_hash`

## Status

Accepted.

## Decision area

Evidence integrity, release-candidate hashing, promotion Gate `A`, and downstream receipt alignment.

## Context

KFM promotion must approve an exact, inspectable evidence state, not a merely plausible artifact folder. Gate `A` of the Promotion Contract is responsible for evidence integrity and must prove that the release candidate's `EvidenceBundle` is present, parseable, and bound to the declared content hash.

A raw file hash is not sufficient for this role because the `EvidenceBundle` may carry its own `spec_hash`, computed hash, signatures, or attestations. Hashing those wrapper fields creates recursive or unstable digests. Formatting-only changes should not alter the digest, but semantic changes to the releasable evidence state must alter it.

KFM therefore needs a repo-specific canonical hash algorithm for `EvidenceBundle` content.

## Decision

Use algorithm id `canonical-json-v1` for `spec_hash`.

The normative validator for this ADR is:

```text
tools/validators/check_spec_hash.py
```

The validator computes and verifies `spec_hash` as follows:

1. Read the candidate `EvidenceBundle` JSON. The default input path is:

   ```text
   artifacts/EvidenceBundle.json
   ```

2. Require the `EvidenceBundle` root to be a JSON object.

3. Deep-copy the root object and remove only these root-level keys before hashing:

   ```text
   spec_hash
   computed_spec_hash
   signatures
   attestations
   _signature
   ```

   These keys are excluded only at the root level. Identically named nested fields remain part of the hash unless a later ADR changes the algorithm.

4. Serialize the remaining object using repo-local canonical JSON settings:

   ```python
   json.dumps(
       normalized,
       sort_keys=True,
       separators=(",", ":"),
       ensure_ascii=False,
   ).encode("utf-8")
   ```

5. Compute SHA-256 over those canonical bytes.

6. Represent the digest as a lowercase 64-character hex string.

7. Compare the computed digest with:

   ```text
   artifacts/spec_hash.txt
   ```

8. If `EvidenceBundle.spec_hash` is present, require it to match `artifacts/spec_hash.txt`.

9. When Gate `A` runs, write the verification receipt to:

   ```text
   .promotion/spec_hash_check.json
   ```

   `.promotion/` is disposable validator material. It is not canonical release evidence unless a later ADR explicitly changes that rule.

After any transform that changes evidence or releasable content, recompute `spec_hash` and update downstream receipts, release-candidate artifacts, and any embedded `EvidenceBundle.spec_hash`.

## Scope and non-goals

`canonical-json-v1` is a KFM release-candidate digest algorithm for `EvidenceBundle` content.

It is not:

- a raw source-file checksum;
- a signature digest;
- a full proof-pack digest;
- a release-manifest artifact hash;
- a graph, tile, PMTiles, GeoParquet, or index hash;
- a guarantee that rights, sensitivity, review, or publication gates passed;
- a general-purpose JSON canonicalization standard for every repo file.

This ADR does not make generated text, map tiles, search indexes, graph projections, AI answers, dashboards, scenes, or exported reports into root truth. Those outputs remain downstream carriers whose claims must resolve to evidence and release state.

## Required invariants

| Invariant | Rule |
| --- | --- |
| Stable formatting | Whitespace and object-key order changes must not change `spec_hash`. |
| Semantic sensitivity | Meaningful `EvidenceBundle` content changes must change `spec_hash`. |
| Signature non-recursion | Signature and attestation wrapper fields are excluded from the root hash. |
| Root-only exclusion | Only the listed root-level keys are excluded. |
| Evidence before publication | `spec_hash` validation is necessary for promotion but not sufficient for publication. |
| No hand edits | Maintainers must not hand-edit `artifacts/spec_hash.txt` to force a pass. |
| Explicit future migration | Any incompatible algorithm change must use a new algorithm id such as `canonical-json-v2`. |

## Affected surfaces

| Surface | Expected relationship to this ADR |
| --- | --- |
| `docs/adr/0002-promotion-contract.md` | Gate `A` uses canonical `spec_hash` verification as its evidence-integrity check. |
| `docs/runbooks/promotion-gates.md` | Operational instructions must tell maintainers that Gate `A` runs canonical `spec_hash` validation. |
| `tools/validators/check_spec_hash.py` | Normative implementation of `canonical-json-v1`. |
| `tools/validators/run_gate.sh` | Gate `A` must invoke `check_spec_hash.py` and emit `.promotion/spec_hash_check.json`. |
| `artifacts/EvidenceBundle.json` | Default release-candidate evidence bundle input. |
| `artifacts/spec_hash.txt` | Default release-candidate declared digest. |
| `.promotion/spec_hash_check.json` | Generated validation receipt for the Gate `A` check. |
| `EvidenceBundle.spec_hash` | Optional embedded digest; if present, must match `artifacts/spec_hash.txt`. |

`tools/compute_spec_hash.py` is a generic JSON hash helper unless it is updated to implement this ADR's root-key exclusions and receipt behavior. It must not be treated as the Gate `A` `EvidenceBundle` validator unless it is aligned with `canonical-json-v1` or explicitly superseded.

## Consequences

Positive consequences:

- release candidates get a stable digest for evidence content;
- formatting changes do not create false evidence changes;
- signature and attestation material can be added without hash recursion;
- Gate `A` can fail closed on missing, malformed, stale, or mismatched candidate evidence;
- downstream receipts and release manifests can refer to a deterministic evidence-state digest.

Costs and obligations:

- transforms that modify evidence must recompute `spec_hash` and downstream receipts;
- fixtures must cover both positive and negative hash cases;
- any tooling that computes `spec_hash` must use the same exclusions and serialization settings;
- algorithm changes require explicit versioning and migration.

## Validation and enforcement

Minimum local Gate `A` validation:

```bash
python tools/validators/check_spec_hash.py \
  artifacts/EvidenceBundle.json \
  artifacts/spec_hash.txt \
  --receipt-out .promotion/spec_hash_check.json
```

Promotion-gate validation:

```bash
tools/validators/run_gate.sh A
```

Expected pass condition:

- `artifacts/EvidenceBundle.json` exists;
- `artifacts/EvidenceBundle.json` parses as a JSON object;
- `artifacts/spec_hash.txt` exists;
- `artifacts/spec_hash.txt` contains a 64-character SHA-256 hex digest;
- computed canonical digest equals `artifacts/spec_hash.txt`;
- embedded `EvidenceBundle.spec_hash`, when present, equals `artifacts/spec_hash.txt`;
- `.promotion/spec_hash_check.json` records `algorithm`, inputs, computed value, declared value, embedded value, excluded root keys, and `valid: true`.

Required negative checks:

| Case | Expected outcome |
| --- | --- |
| Missing `EvidenceBundle.json` | `ERROR`; Gate `A` fails. |
| Invalid JSON | `ERROR`; Gate `A` fails. |
| Root is not a JSON object | `ERROR`; Gate `A` fails. |
| Missing `spec_hash.txt` | `ERROR`; Gate `A` fails. |
| Non-SHA-256 digest text | `ERROR`; Gate `A` fails. |
| Declared digest differs from computed digest | `ERROR`; Gate `A` fails. |
| Embedded `EvidenceBundle.spec_hash` differs from `spec_hash.txt` | `ERROR`; Gate `A` fails. |
| Root-level signature material changes only | Hash should remain unchanged. |
| Nested evidence content changes | Hash should change. |

## Failure handling

When `spec_hash` validation fails, maintainers must rebuild or regenerate the release candidate from governed inputs. They must not edit `artifacts/spec_hash.txt` merely to match a changed bundle.

If a mismatch is caused by a legitimate evidence/content transform:

1. regenerate `artifacts/EvidenceBundle.json` from the governed input state;
2. recompute `artifacts/spec_hash.txt` using `canonical-json-v1`;
3. update downstream receipts affected by the transform;
4. rerun Gate `A`;
5. rerun later gates whose inputs depend on evidence integrity.

If the mismatch is caused by tampering, stale artifacts, or unexplained drift, the candidate must remain blocked until the source of drift is recorded and resolved.

## Migration and rollback

Existing bundles using `canonical-json-v1` remain verifiable under `canonical-json-v1`.

A future incompatible algorithm must be introduced under a new id, for example:

```text
canonical-json-v2
```

A safe migration must include:

- a successor ADR;
- compatibility handling for existing `canonical-json-v1` bundles;
- fixtures for v1 and v2;
- validator updates;
- runbook updates;
- release-manifest or proof-pack references that record which algorithm was used;
- rollback instructions.

Rollback of this ADR's file content is allowed only if `tools/validators/check_spec_hash.py`, `tools/validators/run_gate.sh`, promotion docs, fixtures, and workflows remain consistent with the rollback state. Partial rollback that leaves docs and validator behavior in conflict is denied.

## Open verification

- [ ] Confirm all Gate `A` fixtures include expected positive and negative `spec_hash` cases.
- [ ] Confirm CI invokes the same `tools/validators/check_spec_hash.py` path used locally.
- [ ] Confirm `tools/validators/run_gate.sh` uses the canonical promotion-contract path defined by ADR 0002 or records an explicit compatibility exception.
- [ ] Decide whether `tools/compute_spec_hash.py` should be renamed, deprecated, or aligned with this ADR.
- [ ] Confirm any `EvidenceBundle` schema documents the optional embedded `spec_hash` field and the `canonical-json-v1` algorithm id.
- [ ] Confirm release manifests or proof packs record enough information to replay the hash calculation.

## Related files

```text
docs/adr/0002-promotion-contract.md
docs/runbooks/promotion-gates.md
tools/validators/check_spec_hash.py
tools/validators/run_gate.sh
tools/validators/build_gate_input.py
artifacts/EvidenceBundle.json
artifacts/spec_hash.txt
.promotion/spec_hash_check.json
```
