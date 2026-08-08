<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/wimas-wwc5-aggregate-first-profile
title: WIMAS/WWC5 Aggregate-First Evidence Profile
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; evidence; water-use; private-well; fixture-only; no-authority
owning_root: contracts/
responsibility: Keep WIMAS aggregate water-use, water-right context, and WWC5 well-record references separate while enforcing aggregate-first public safety.
truth_posture: "CONFIRMED repository dependencies; PROPOSED profile; NEEDS VERIFICATION source terms and human review"
related:
  - ./evidence_bundle.md
  - ../../schemas/contracts/v1/evidence/wimas_wwc5_aggregate_first_profile.schema.json
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, wimas, wwc5, water-use, private-well, pass-2]
[/KFM_META_BLOCK_V2] -->

# WIMAS/WWC5 Aggregate-First Evidence Profile

This fixture-only profile adapts `KFM-P2-IDEA-0027` and `KFM-P2-PROG-0009`. It preserves three source roles: `WIMAS_WATER_USE_AGGREGATE`, `WIMAS_WATER_RIGHT_CONTEXT`, and `WWC5_WELL_RECORD_REFERENCE`.

## Boundary

- Public posture is aggregate-first at county or HUC12 scale.
- Owner names, contact details, and exact private-well coordinates must be suppressed.
- Legal-description-derived, geocoded, measured, and unknown position quality remain explicit and non-interchangeable.
- A water-right record is context; it does not prove title, current legal entitlement, or current use.
- A WWC5 record is a source reference; it does not prove current condition, ownership, or potable-water status.
- Missing policy, review, or evidence support returns `ABSTAIN`; unsafe precision or living-person detail returns `DENY`; identity, time, arithmetic, and hash contradictions return `ERROR`.
- `PASS` proves local synthetic consistency only.

## Directory Rules basis

The packet uses existing `contracts/`, `schemas/`, `fixtures/`, `tools/`, `tests/`, `.github/workflows/`, `docs/intake/exploratory/`, and `data/receipts/generated/` responsibility roots. It creates no connector, source registry, policy authority, lifecycle object, proof, release, API, map layer, or publication path.

## Validation

```bash
python -m unittest discover --start-directory tests/validators --pattern 'test_validate_wimas_wwc5_aggregate_first_profile.py' --verbose
KFM_NO_NETWORK=1 python tools/validators/validate_wimas_wwc5_aggregate_first_profile.py --fixtures
```

## Non-effects and rollback

No live WIMAS/WWC5 access, source admission, private-well disclosure, policy decision, lifecycle write, release, deployment, or publication occurs. Before merge, close the draft PR. After an authorized merge, revert its bounded commit or merge commit.
