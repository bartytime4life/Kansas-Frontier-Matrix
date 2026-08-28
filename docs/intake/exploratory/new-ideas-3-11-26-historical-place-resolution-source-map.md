<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-3-11-26/historical-place-resolution
title: New Ideas 3-11-26 — Historical Place Resolution Source Map
type: exploratory-source-map
version: v0.1.0
status: proposed; source-adaptation-record
owners: OWNER_TBD — Settlements/Infrastructure steward · Docs steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; exploratory; no-live-source-activation
[/KFM_META_BLOCK_V2] -->

# New Ideas 3-11-26 — Historical Place Resolution Source Map

## Source boundary

This adaptation uses the frontier-era Kansas toponyms gazetteer section of
*New Ideas 3-11-26.pdf*, pages 146–148. The source proposes:

- GNIS/BGN accepted-name and variant-name authority;
- AHCB historical county slices for county-at-year bounding;
- KSHS/Baughman post-office open/close dates;
- lower confidence for rail-stop labels without stronger corroboration;
- deterministic identity from canonical name + AHCB slice + GNIS ID;
- small ambiguous-name fixtures before broad ingestion.

The document's concrete source claims and illustrative identifiers are proposal inputs,
not current repository or live-source proof.

## Repository adaptation

| Source idea | Adapted implementation | Deliberately deferred |
|---|---|---|
| compact gazetteer JSON | closed Draft 2020-12 candidate schema | production gazetteer schema or public API |
| normalized names and variants | deterministic Unicode/case/whitespace comparison | fuzzy/ML matching |
| AHCB county-at-year bounding | synthetic historical-county support role | live AHCB download or spatial join |
| KSHS/Baughman lifespan | synthetic post-office-lifespan role | live parsing, terms, or rights decision |
| rail-stop caution | `medium / hold_for_review` ceiling | automatic rail-stop acceptance |
| deterministic `place_id` | SHA-256 over normalized canonical name + synthetic AHCB + synthetic GNIS | global identity-policy adoption |
| ambiguous-name test set | valid hold and abstain fixtures plus invalid overclaim fixtures | real names or real source records |

## Directory Rules basis

Accepted ADR-0029 makes `docs/doctrine/directory-rules.md` the writable Directory
Rules authority. This slice uses existing responsibility lanes:

- `contracts/domains/settlements-infrastructure/` for semantic meaning;
- `schemas/contracts/v1/domains/settlements-infrastructure/` for machine shape;
- `fixtures/contracts/v1/domains/settlements-infrastructure/` for deterministic examples;
- `tools/validators/` and `tests/validators/` for enforceability;
- `.github/workflows/` for least-privilege CI;
- `data/receipts/generated/` for authoring provenance only.

No root, migration, live source, policy authority, catalog authority, release authority,
or public path is created.

## Verification still required before live use

- current official endpoints, identifiers, terms, licenses, attribution, and redistribution
  rules for GNIS/BGN, AHCB/Newberry, KSHS/Baughman, and period maps;
- a steward-approved source-role and SourceDescriptor set;
- real historical county and place identity edge cases;
- EvidenceBundle resolution, policy review, correction, release, and rollback closure;
- public-safe geometry and API behavior.
