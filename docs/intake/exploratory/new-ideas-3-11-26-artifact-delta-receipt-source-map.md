<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-3-11-26/artifact-delta-receipt
title: New Ideas 3-11-26 — Artifact Delta Receipt Source Map
type: exploratory-source-map; implementation-adaptation
version: v0.1.0
status: proposed; source-bounded; no-network; no-release-effect
owners: OWNER_TBD — Intake steward · Receipt steward · Release steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; exploratory; receipts; no-publication-authority
related:
  - ../../../contracts/receipts/artifact_delta_receipt.md
  - ../../../schemas/contracts/v1/receipts/artifact_delta_receipt.schema.json
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, new-ideas, artifact-delta, receipt, jcs, cose, oci]
[/KFM_META_BLOCK_V2] -->

# Source map: artifact delta receipt candidate

## Source-derived idea

*New Ideas 3-11-26.pdf* proposes a small tamper-evident delta receipt that binds:

- a `before` run receipt and spec hash;
- an `after` run receipt and spec hash;
- the policy decision and steward identity;
- canonical JCS bytes and SHA-256 identity;
- a COSE_Sign1 signature; and
- an OCI referrer attached to the resulting artifact.

The packet also describes the same concept in a change-data-capture flow: compute pre- and
post-apply spec hashes, include run receipts and a policy decision, sign the record, and require
downstream verification before higher-trust transitions.

## Repository comparison

Current-main inspection found receipt semantic and schema families, promotion/rollback
contracts, generated authoring receipts, and deterministic fixture validators. Searches for
`delta_receipt`, `ArtifactDeltaReceipt`, `COSE_Sign1`, `oci_referrer_uri`, and paired
`from_spec_hash` / `to_spec_hash` fields found no existing generic artifact-delta receipt
implementation. The existing `PlaceNameAuthorityGraph` and historical person-place-event
profile cover different ideas from the attachment and were not duplicated.

## Adaptation decision

The implementation keeps the valuable dependency-closed core:

1. a receipt-family semantic contract;
2. a closed Draft 2020-12 schema;
3. deterministic before/after and payload-digest checks;
4. positive and negative synthetic fixtures;
5. a no-network validator and focused tests;
6. a read-only workflow and generated authoring receipt.

It deliberately excludes live signing, secret material, registry access, OCI uploads, Conftest
policy execution, lifecycle writes, release assembly, and PR-triggered publication. Those require
separate source/tool verification, security review, policy/release authority, and operational
credentials.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 controlling. The placement result is `PLACE`:

| Artifact | Owning responsibility |
|---|---|
| Human meaning | `contracts/receipts/` |
| Machine shape | `schemas/contracts/v1/receipts/` |
| Synthetic examples | `fixtures/contracts/v1/receipts/` |
| Validator and tests | `tools/validators/`, `tests/validators/` |
| CI | `.github/workflows/` |
| Source adaptation record | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, compatibility path, live receipt instance, release record, proof object, or public
carrier is created.

## Status

- **CONFIRMED:** source packet contains the delta-receipt pattern; current-main receipt and
  release families were inspected; no generic delta-receipt implementation was found.
- **PROPOSED:** `ArtifactDeltaReceiptCandidate` semantics and future production use.
- **NEEDS VERIFICATION:** real RFC 8785 library selection, COSE/DSSE/Sigstore verifier,
  OCI registry/referrer support, key custody, policy binding, and release integration.
- **UNKNOWN:** whether a future operational signer/verifier should use COSE, DSSE/Sigstore,
  or a governed profile supporting both.
