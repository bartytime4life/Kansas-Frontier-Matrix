# Contracts: release

## Purpose
Defines semantic meaning for release governance object families. Shape enforcement remains in `schemas/contracts/v1/release/`.

## Scope
This folder contains contract prose for release decisions, release manifests, rollback, corrections, and withdrawals.

## Authority
- `contracts/` owns object meaning.
- `schemas/contracts/v1/` owns machine-checkable shape.
- `policy/` owns allow/deny/restrict/abstain behavior.

## Naming
- One Markdown file per object family, using snake_case names aligned with schema titles.

## Lifecycle alignment
These contracts cover objects used at promotion/release boundaries from PROCESSED and CATALOG/TRIPLET into PUBLISHED, including rollback and correction flows.

## Review burden
Changes must preserve contract/schema split and cite governing ADRs when semantics shift.

## Files in this folder
- `README.md`
- `release_manifest.md`
- `promotion_decision.md`
- `rollback_card.md`
- `correction_notice.md`
- `withdrawal_notice.md`

## Related folders
- `schemas/contracts/v1/release/`
- `policy/release/`
- `release/`
- `contracts/runtime/`

## Governing ADRs
- `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`
- `docs/adr/ADR-0002-contracts-vs-schemas-split.md`
- `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md`

## Last reviewed
2026-05-09 (UTC)
