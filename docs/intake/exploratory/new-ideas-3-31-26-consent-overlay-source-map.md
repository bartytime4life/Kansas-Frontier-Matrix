<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/new-ideas-3-31-26-consent-overlay-source-map
title: New Ideas 3-31-26 - Consent-Safe Genealogy Overlay Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - intake steward; People/DNA/Land steward; consent steward; privacy steward; validation steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public-doc; restricted-domain-aware; intake; exploratory; cite-or-abstain
owning_root: docs/
responsibility: Preserve a reviewable identity and disposition map from the supplied New Ideas 3-31-26 packet to the bounded synthetic consent-safe genealogy-overlay contract, schemas, fixtures, validator, tests, workflow wiring, and generated receipt without promoting packet prose, real-person data, consent validity, DNA evidence, policy, release, or publication claims into authority.
source_evidence:
  captured_filename: New Ideas 3-31-26.pdf
  source_date: 2026-03-31
  capture_date: 2026-08-03
  sha256: 7cb8822a9e0b3adf98607c80dcd649ef95df3fb009f33d21b66f8760fddade86
  byte_count: 3940707
  page_count: 403
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  remote_main_snapshot: 2569267dd1291af920cb912acf6c95f46a2a62e6
  remote_state_verified_at: 2026-08-03
  concurrent_open_prs:
    - "PR #1956 - Smart Sync HTTP RunReceipt profile; disjoint paths"
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/people-dna-land/CONSENT_MODEL.md
  - ../../../contracts/domains/people-dna-land/consented_genealogy_overlay.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/consented_genealogy_overlay.schema.json
  - ../../../schemas/contracts/v1/domains/people-dna-land/genealogy_overlay_revocation_manifest.schema.json
  - ../../../fixtures/domains/people-dna-land/consent_overlay/README.md
  - ../../../tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - ../../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py
tags: [kfm, intake, new-ideas, people-dna-land, genealogy, consent, revocation, privacy, fixtures, no-network]
notes:
  - "The PDF is not committed. Its filename, byte count, page count, and SHA-256 preserve attachment identity."
  - "Pages 317-361 contain the source packet's schema-validator-fixture-CI implementation bundle and proposed follow-on order."
  - "The source packet's docs-local schema and validator paths were not copied; responsibility-root paths were selected from current repository and Directory Rules evidence."
  - "This batch is fixture-only and not released. It performs no source activation, real consent validation, revocation execution, lifecycle promotion, public export, UI integration, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 3-31-26 - consent-safe genealogy overlay source map

> **Outcome:** adapt the packet's strongest unimplemented People/DNA/Land idea
> into one bounded, synthetic, no-network profile: a semantic contract, two
> closed schemas, a revocation-manifest-bound validator, exact positive and
> negative fixtures, executable tests, and explicit domain-workflow wiring.

## Source identity

| Field | Confirmed value |
|---|---|
| Captured filename | `New Ideas 3-31-26.pdf` |
| Source date | `2026-03-31` |
| Capture date | `2026-08-03` |
| SHA-256 | `7cb8822a9e0b3adf98607c80dcd649ef95df3fb009f33d21b66f8760fddade86` |
| Size | `3,940,707` bytes |
| Page count | `403` |
| Repository comparison | `main@2569267dd1291af920cb912acf6c95f46a2a62e6` |
| Concurrent open work | PR #1956, Smart Sync HTTP RunReceipt; no changed-path overlap with this slice |

The packet is exploratory evidence. It does not prove that any proposed
genealogy overlay, consent token, revocation manifest, path, workflow, source,
rights posture, or public product is implemented or approved.

## Directory Rules reconciliation

The packet proposed placing schema and validator code below a documentation
folder. Current repository evidence and adopted Directory Rules separate those
responsibilities:

| Responsibility | Selected home | Basis |
|---|---|---|
| Exploratory source identity and disposition | `docs/intake/exploratory/` | Human-readable intake evidence |
| Object meaning | `contracts/domains/people-dna-land/` | Existing domain semantic-contract lane |
| Machine shape | `schemas/contracts/v1/domains/people-dna-land/` | Existing schema authority lane and ADR-0001 convention |
| Synthetic examples | `fixtures/domains/people-dna-land/consent_overlay/` | Fixture responsibility root |
| Executable validation | `tools/validators/domains/people-dna-land/` | Existing domain-validator lane |
| Enforceability proof | `tests/domains/people-dna-land/consent/revocation/` | Existing consent-revocation test lane |
| CI orchestration | `.github/workflows/domain-people-dna-land.yml` | Existing stable domain-workflow identity |
| Generated provenance | `data/receipts/generated/` | Existing generated-receipt family |

No new root, policy authority, source registry, proof store, release family,
runtime surface, or published data lane is created.

## Source-page map and disposition

| Packet pages | Proposal pressure | Repository-grounded disposition |
|---:|---|---|
| 317-321 | Make a non-identifying genealogy overlay machine-validatable before adding producers or UI; provide schema, semantic validator, CI, and pass/fail fixtures. | `ADAPT / IMPLEMENT` as a responsibility-rooted fixture profile. |
| 337-340 | Hash kit material, bind consent interval and revocation root, use coarse place/time buckets, evidence refs, and explicit disclosure state. | `ADAPT / NARROW` to synthetic fixture hashes, `99999` county sentinel, restricted/internal disclosure, and `not_released` governance. |
| 343-361 | Full implementation bundle, forbidden identifying fields, expired-consent checks, revocation-manifest membership, evidence requirements, deterministic runner, workflow, and definition of done. | `ADAPT / IMPLEMENT` with bounded parser mechanics, exact findings, existing workflow identity, and no external dependency install. |
| 341, 361 | Follow with revocation-manifest generator, overlay builder, catalog/public export, then Focus/Evidence Drawer. | `DEFER` after this profile; no producer, catalog, public export, or UI work is admitted in this slice. |
| Remaining pages | Historic routes, soil, atmosphere, hydrology, biodiversity, watchers, MapLibre, and other proposals. | `CORROBORATIVE / BACKLOG` for separately governed slices. |

## Repository gap confirmed at the base

At the inspected base:

- `tools/validators/genealogy/validate_consent_receipt.py` was documentation-only;
- `tests/domains/people-dna-land/README.md` was a greenfield stub;
- the consent-revocation test lane documented the desired behavior but had no
  executable test;
- the People/DNA/Land workflow explicitly rejected any surfaced fixture payload
  and treated every test and validator as held;
- the domain schema index did not confirm a concrete schema for this profile; and
- the consent policy README warned that repository presence is not policy
  activation.

The selected change closes only that executable fixture-profile gap.

## Bounded implementation

The profile proves:

- DNA-derived summaries require active, time-valid fixture consent;
- living-person posture requires active consent;
- revoked and expired consent fail closed;
- a separately validated revocation manifest is mandatory;
- manifest membership and root mismatch are denied;
- vendor kit identifiers, raw genomic material, and exact coordinates are denied;
- time and place are coarse and synthetic;
- high-confidence summaries require stronger fixture evidence;
- deterministic `spec_hash` values reproduce;
- public/released/promotion-eligible states are rejected;
- malformed, duplicate-key, non-finite, oversized, and non-object JSON fail
  closed;
- diagnostics contain codes and paths, not sensitive values; and
- no network access occurs.

A pass does not establish identity, kinship, consent validity, DNA support,
source rights, policy approval, release readiness, or publication safety.

## Deferred follow-on order

1. revocation-manifest generator and correction/withdrawal semantics;
2. overlay builder producing candidates only;
3. EvidenceRef-to-EvidenceBundle resolution and policy evaluation;
4. catalog and release-candidate wiring;
5. restricted steward UI, then any public-safe map or Focus surface.

Every follow-on remains `PROPOSED / NEEDS VERIFICATION`.

## Rollback

Revert the bounded feature-branch commits. No source, real person record, consent
record, revocation system, lifecycle data, proof, release, cache, API, map,
graph, search, AI, or published state is created.

[Back to top](#top)
