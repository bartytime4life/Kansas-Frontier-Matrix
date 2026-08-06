<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/settlements-infrastructure/historical-place-resolution
title: Historical Place Resolution Candidate Contract
type: semantic-contract; fixture-first; no-network
version: v0.1.0
status: proposed; fixture-only; no-live-gazetteer; no-publication
owners: OWNER_TBD — Settlements/Infrastructure steward · Evidence steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public-metadata-model; historical; synthetic-fixture; no-publish
related:
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/EXPANSION_BACKLOG.md
  - ../../../docs/intake/exploratory/new-ideas-3-11-26-historical-place-resolution-source-map.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/historical_place_resolution.schema.json
  - ../../../fixtures/contracts/v1/domains/settlements-infrastructure/historical_place_resolution/
  - ../../../tools/validators/validate_historical_place_resolution.py
[/KFM_META_BLOCK_V2] -->

# Historical Place Resolution Candidate Contract

> A deterministic, evidence-referenced profile for **synthetic historical place-name
> candidate resolution only**. It does not adjudicate current legal place status,
> municipal identity, boundaries, title, source rights, policy, release, or publication.

## Status and authority

| Field | Value |
|---|---|
| Status | **PROPOSED semantic contract**; executable fixture profile |
| Owning root | `contracts/` — semantic meaning |
| Paired schema | `schemas/contracts/v1/domains/settlements-infrastructure/historical_place_resolution.schema.json` |
| Fixture profile | `fixtures/contracts/v1/domains/settlements-infrastructure/historical_place_resolution/` |
| Validator | `tools/validators/validate_historical_place_resolution.py` |
| Public/release effect | None; `not_released`, `promotion_eligible=false`, `public_exposure=false` |

The attached idea packet proposes a frontier-era Kansas toponyms gazetteer that
combines GNIS/BGN name authority, AHCB historical county slices, KSHS/Baughman
post-office lifespans, and lower-authority period-map or newspaper corroboration.
It also proposes deterministic place identity from canonical name + AHCB slice +
GNIS ID. Those ideas are adapted here as a bounded synthetic fixture profile;
no live source or endpoint is activated. *New Ideas 3-11-26.pdf*, pp. 146–148.

## Meaning

`HistoricalPlaceResolutionCandidate` records one historical name-and-year query,
its candidate places, the source roles that support each candidate, and a derived
finite review outcome. It preserves four distinctions:

1. **name authority** — GNIS/BGN support accepted and variant names;
2. **historical county context** — AHCB-like support constrains county at the query year;
3. **post-office lifespan** — KSHS/Baughman-like support distinguishes a time-limited
   post office from a continuing settlement;
4. **corroboration** — period maps, newspapers, and local histories may support a
   candidate but do not become accepted-name authority.

The profile performs exact normalized matching only. It Unicode-normalizes,
case-folds, removes combining marks for comparison, and collapses whitespace.
It does not perform fuzzy or model-based matching.

## Finite derivation

A candidate is query-compatible only when its canonical/variant name, valid year,
and optional county hint match.

| Outcome | Required posture |
|---|---|
| `high / candidate_review` | exactly one query-compatible candidate; GNIS-backed name support; AHCB-backed county support; and either period corroboration or a matching post-office lifespan |
| `medium / hold_for_review` | one incomplete candidate, any corroborated rail-stop candidate, or more than one query-compatible candidate |
| `low / abstain` | no candidate has sufficient name, time, county, and authority support |

Rail-stop labels never auto-resolve in this profile. They remain review candidates even
when synthetic GNIS and period-map support are present. Ambiguous homonyms also remain
on hold.

## Deterministic identity

`resolution_id` hashes the normalized query and sorted candidate references.
For a unique high-confidence result, `place_id` is:

```text
urn:kfm:place:sha256:SHA256(canonical-json({
  canonical_name: normalized canonical name,
  ahcb_slice: synthetic historical-county slice ID,
  gnis: synthetic GNIS ID
}))
```

`spec_hash` hashes the complete candidate document except the `spec_hash` field.
The profile's canonical JSON is intentionally bounded to strings, integers, booleans,
nulls, arrays, and objects; it does not claim a repository-wide RFC 8785 implementation.

## Source-role and evidence requirements

Every support record carries:

- a unique fixture-safe `source_ref`;
- the exact synthetic fixture license label;
- minimal `scan_ids` sufficient to replay the fixture;
- one source role and one or more explicitly supported facets.

GNIS/BGN, historical-county, post-office-lifespan, and period-corroboration roles remain
non-interchangeable. A receipt or fixture reference is not an EvidenceBundle merely
because it has an `evidence_refs` field.

## Fail-closed boundaries

The validator rejects or denies:

- public-release, public-exposure, or live-source-activation claims;
- exact geometry, coordinates, addresses, parcels, current ownership, living-person,
  DNA/genomic, or critical-infrastructure fields;
- reused source references across candidates;
- unsupported authority identifiers or invalid valid-time order;
- place ID, resolution ID, confidence, disposition, reason-code, review-state, or
  `spec_hash` drift;
- undeclared fields or malformed source metadata.

## Lifecycle and publication boundary

This profile writes no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET,
PUBLISHED, proof, release, graph, search, cache, API, map, or AI state. The workflow
reads repository-owned synthetic fixtures only. A future live gazetteer, ingest adapter,
source-rights determination, map layer, or lookup API requires separate governed work.

## Rollback

Revert the PR commit or close the PR and delete its task branch. The slice is additive
and creates no lifecycle or public state, so rollback needs no migration, cache
invalidation, correction notice, or release withdrawal.
