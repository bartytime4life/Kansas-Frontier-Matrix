<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-22-signed-bundle-timestamp-evidence-source-map
title: Pass 22 Signed-Bundle Timestamp Evidence Source Map
type: source-map
version: v1.0.0
status: proposed
owners: OWNER_TBD - Release steward; Security steward; Contracts steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; non-authoritative
related:
  - ../../../contracts/release/signed_bundle_timestamp_evidence.md
  - ../../../schemas/contracts/v1/release/signed_bundle_timestamp_evidence.schema.json
  - ../../../contracts/release/cosign_attestation_verification_plan.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-22, pass-32, rfc3161, sigstore, timestamp, source-map]
notes:
  - "The atlas cards are proposed design sources, not cryptographic, release, or publication evidence."
[/KFM_META_BLOCK_V2] -->

# Pass 22 Signed-Bundle Timestamp Evidence Source Map

## Assayed ideas

| Stable card | Normalized source statement | Carry-forward |
|---|---|---|
| `KFM-P22-PROG-0033` | Promotion bundles should record RFC 3161 timestamp material when available alongside Rekor UUID and Cosign proof references | `CONFIRMED`: `UNCHANGED` through the Pass 23/32 consolidated atlas |
| `KFM-P22-PROG-0052` | Signed promotion bundles should preserve RFC 3161 or equivalent signer timestamp evidence when available and policy-relevant | `CONFIRMED`: `UNCHANGED` through the Pass 23/32 consolidated atlas |

`CONFIRMED`: no exact stable-ID, `RFC3161`, `TimestampEvidence`, object-name, or pull-request match was found on `main@f5efa63a3600f688cb9d6ed0255e20b9dfbac6dc` before this slice. Existing Cosign planning, signing guidance, and release-manifest surfaces remain adjacent authorities rather than duplicates.

## Source evidence

1. Google Drive `KFM_Pass_22_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, sections 8.12.59 and 8.12.60.
2. Attached `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, consolidated pages 997-998, retaining both cards and marking repository implementation `UNKNOWN` in the source document.
3. Repository `contracts/release/cosign_attestation_verification_plan.md`, `docs/standards/SIGNING.md`, accepted ADR-0029, and adopted Directory Rules v2 on the cited base.

## Adaptation decisions

| Source concept | Repository adaptation | Boundary |
|---|---|---|
| RFC 3161 material | Reference, digest, bound subject digest, capture time, policy OID | No token parsing, TSA trust, or signature verification |
| Rekor context | Nullable UUID plus Sigstore signed-entry timestamp item | No log lookup, inclusion proof, checkpoint, or integrated-time verification |
| Cosign proof reference | Digest-bound Cosign-bundle subject | Does not replace or execute the existing verification plan |
| Policy relevance | Finite `REQUIRED`/`OPTIONAL`/`UNKNOWN` declaration and policy ref | Validator checks mapping only; policy is not evaluated or authenticated |
| Missing material | Explicit `ABSTAIN`, `DENY`, or `ERROR` assessment | Outcome does not authorize or perform a release action |
| Identity | Existing RFC 8785 JCS plus SHA-256 package | Identity only; not cryptographic proof or release approval |

## Deliberate omissions

- No live TSA, Fulcio, Rekor, OCI, registry, certificate, signature, or transparency operation.
- No external version, vulnerability, or service-currentness claim.
- No `EvidenceBundle` resolution, policy evaluation, review authentication, catalog closure, promotion, release, rollback, alias update, deployment, publication, or public-use authorization.
- No changes to the existing Cosign verification plan, signing workflow, ReleaseManifest, policy bundles, repository settings, or branch protection.

## Verification posture

`PROPOSED`: timestamp-evidence object semantics and deterministic mapping. `CONFIRMED`: source-card wording, later unchanged carry-forward, current-base gap search, adjacent repository boundaries, adopted Directory Rules placement, and deterministic local fixture evidence. `NEEDS VERIFICATION`: hosted exact-head checks and human security/release review.

