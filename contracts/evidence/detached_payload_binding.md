<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/detached-payload-binding
title: DetachedPayloadBinding Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Evidence steward · Security steward · Contracts steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; no-network; non-authoritative
related:
  - ../../schemas/contracts/v1/evidence/detached_payload_binding.schema.json
  - ../../fixtures/contracts/v1/evidence/detached_payload_binding/
  - ../../tools/validators/evidence/validate_detached_payload_binding.py
  - ../../tests/validators/evidence/test_validate_detached_payload_binding.py
  - evidence_bundle.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, detached-payload, digest, signature, mirrors, no-network]
notes:
  - "This contract adapts Pass 7 KFM-P7-PROG-0005 to the current repository hash vocabulary."
  - "The payload raw-byte digest is payload.sha256; the binding object's spec_hash remains RFC8785-JCS plus SHA-256."
  - "The first implementation is fixture-only and never fetches a URL."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DetachedPayloadBinding Contract

> **Purpose.** Bind an external binary payload to an EvidenceBundle candidate through immutable metadata: the bundle reference and semantic hash bind the metadata, the metadata names a raw-byte SHA-256 digest, and one or more locations identify where those bytes may later be retrieved.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` / `NO_NETWORK` |
| Machine shape | `schemas/contracts/v1/evidence/detached_payload_binding.schema.json` |
| Validator | `tools/validators/evidence/validate_detached_payload_binding.py` |
| Remote retrieval | Denied |
| EvidenceBundle resolution | Not performed |
| Signature verification | Not performed |
| Rights or policy decision | Not performed |
| Promotion, release, publication | Not authorized |

A `PASS` proves that one synthetic candidate has a closed shape, safe and canonical URL metadata, deterministic identity, a raw-byte digest that matches the separately supplied local fixture bytes, and explicit non-authority flags. It does not prove that a remote URL is reachable, stable, authorized, or contains those bytes; that the EvidenceBundle exists or is released; that a signature is valid; or that the payload may be used or published.

## Source-derived design

Pass 7 card `KFM-P7-PROG-0005` describes a detached mode for binary payloads too large to embed in an EvidenceBundle: the bundle records a raw-byte SHA-256 and URL, and its signature binds the bundle metadata that in turn binds the external bytes. It also identifies URL loss as a limitation and proposes multiple mirrors sharing the same digest.

This repository already reserves `spec_hash` for RFC 8785 JCS identity of semantic JSON. To avoid collapsing semantic identity with raw-byte identity, this profile uses:

| Field | Identity meaning |
|---|---|
| `payload.sha256` | Raw SHA-256 over detached payload bytes. |
| `payload.payload_id` | Stable ID derived from the first 24 hexadecimal characters of `payload.sha256`. |
| `spec_hash` | RFC 8785 JCS plus SHA-256 over the binding metadata, excluding `binding_id` and `spec_hash`. |
| `binding_id` | Stable ID derived from the first 24 hexadecimal characters of `spec_hash`. |
| `bundle_binding.evidence_bundle_spec_hash` | Carried EvidenceBundle semantic hash; not resolved or authenticated by this profile. |

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. The slice uses existing responsibility roots:

| Responsibility | Path family |
|---|---|
| Semantic meaning | `contracts/evidence/` |
| Machine shape | `schemas/contracts/v1/evidence/` |
| Synthetic bytes and JSON | `fixtures/contracts/v1/evidence/` |
| Executable validation | `tools/validators/evidence/` |
| Behavior proof | `tests/validators/evidence/` |
| Hosted orchestration | `.github/workflows/` |
| AI-authoring accountability | `data/receipts/generated/` |

No binary store, source registry, canonical evidence store, proof home, release home, mirror service, CDN, or public route is created.

## Required binding

A candidate contains:

1. `bundle_binding`
   - `evidence_bundle_ref`
   - `evidence_bundle_spec_hash`
   - `bundle_signature_ref`
2. `payload`
   - content-derived `payload_id`
   - safe display `name`
   - `media_type`
   - declared `byte_size`
   - raw-byte `sha256`
3. one to eight `locations`
   - HTTPS `url`
   - `PRIMARY` or `MIRROR` role
   - `content_addressed` declaration
4. deterministic object identity
5. non-authority governance flags.

References and declarations are carried, not resolved.

## URL and mirror rules

- Only `https` URLs are admitted.
- Credentials, fragments, control characters, localhost names, `.local`, `.internal`, and private, loopback, link-local, reserved, multicast, or unspecified IP addresses are denied.
- Locations are stored in ascending URL order and URLs are unique.
- Exactly one location is `PRIMARY`; all others are `MIRROR`.
- Every location is bound to the single `payload.sha256`; per-location digests are intentionally not duplicated.
- The validator never performs DNS, HTTP, object-store, IPFS, OCI, or CDN access.

`content_addressed: true` is a declaration only. It does not prove that a URL is actually content-addressed or immutable.

## Local fixture byte verification

The CLI accepts a separately supplied `--payload-file`. That path is not embedded in the binding object and is not a public locator. The validator reads a bounded regular non-symlink file, computes raw SHA-256 and byte size, and compares both to the candidate metadata.

| Condition | Outcome |
|---|---|
| Candidate metadata valid and supplied local bytes match | `PASS` |
| Candidate metadata valid but no local bytes supplied | `HOLD` with `PAYLOAD_BYTES_UNVERIFIED` |
| Metadata or local bytes contradict the binding | `FAIL` |
| Input or schema cannot be safely evaluated | `ERROR` |

The local fixture proves the validation algorithm; it does not establish remote availability.

## Canonical and semantic rules

- URLs are canonical and unique; exactly one is primary.
- `payload.payload_id` matches `payload.sha256`.
- `spec_hash` and `binding_id` match the canonical metadata.
- all governance flags are `false`;
- local payload bytes, when supplied, match both digest and size;
- payload files are bounded regular files and symlinks are denied.

## Compatibility and future binding

This additive profile does not modify the current EvidenceBundle schema, signature object, release objects, or external storage configuration. A later reviewed slice may add a supported `detached_payload_bindings` extension to EvidenceBundle, signature verification, mirror health receipts, content-addressed registry integration, or release-time remote verification. Those effects must not be inferred from this candidate.

## Validation

```bash
python -m unittest \
  tests.validators.evidence.test_validate_detached_payload_binding \
  --verbose

python tools/validators/evidence/validate_detached_payload_binding.py --fixtures

python tools/validators/evidence/validate_detached_payload_binding.py \
  fixtures/contracts/v1/evidence/detached_payload_binding/valid/valid_binding.json \
  --payload-file \
  fixtures/contracts/v1/evidence/detached_payload_binding/payload/synthetic_payload.bin
```

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commits. No remote payload, EvidenceBundle, signature, source, release, cache, route, or public artifact requires rollback.

## Open verification

- Which EvidenceBundle schema extension point should carry these bindings?
- Which signature object and algorithm authenticate the bundle metadata?
- Are operational URLs required to be content-addressed, release-scoped, or both?
- What mirror-health evidence is sufficient without turning a watcher into a publisher?
- Which rights and retention obligations must be evaluated before remote retrieval?
