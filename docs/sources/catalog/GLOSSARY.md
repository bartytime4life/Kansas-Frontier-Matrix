<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-glossary
title: Source catalog glossary
type: register
version: v0.1
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward>
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, sources, catalog]
notes:
  - "PROPOSED scaffold; sibling-link presence verified in Claude Code session."
[/KFM_META_BLOCK_V2] -->

# Source catalog glossary

> One-line definitions of catalog and provenance terms used across the `docs/sources/catalog/` lane.

**Status:** scaffold (PROPOSED)

Definitions here are **convenience summaries**. The authoritative definition of each term lives in the KFM encyclopedia and the relevant `contracts/` and `schemas/` records. Encyclopedia deep-link targets are **NEEDS VERIFICATION** — no canonical anchor was confirmed in this session.

## Terms

| Term | One-line meaning (PROPOSED) | Authority |
|---|---|---|
| `EvidenceBundle` | Content-addressed, sealed collection of evidence backing a claim or artifact. | encyclopedia — NEEDS VERIFICATION |
| `EvidenceRef` | Pointer of the form `kfm://evidence/<digest>` resolving to an `EvidenceBundle`. | encyclopedia — NEEDS VERIFICATION |
| `SourceDescriptor` | Authoritative record describing an ingestible source; lives in `data/registry/sources/<family>/`. | ADR-0017 · `data/registry/sources/` |
| `RunReceipt` | Recorded outcome of a pipeline run — inputs, outputs, and digests. | ADR-0011 — NEEDS VERIFICATION |
| `PolicyDecision` | Recorded result of evaluating a policy gate (admit / hold / deny). | `policy/` — NEEDS VERIFICATION |
| `PromotionDecision` | Recorded result of a promotion gate advancing an artifact toward publication. | ADR-0018 |
| `ReleaseManifest` | Digest-bearing manifest enumerating what a release publishes. | ADR-0011 |
| `RollbackCard` | Record enabling reversal of a release to a prior known-good state. | ADR-0015 |
| `kfm:provenance` | STAC `properties` extension block carrying KFM provenance fields. | `schemas/contracts/v1/source/` — NEEDS VERIFICATION |
| `kfm:care` | STAC / DCAT extension block carrying CARE governance fields. | `policy/sensitivity/` — NEEDS VERIFICATION |
| `file:checksum` | Per-asset integrity digest (STAC `file` extension) used for catalog closure. | STAC `file` extension — EXTERNAL |
| `spec_hash` | sha256 digest of a canonicalized record, used as its content identity. | ADR-0013 |
| `source_role` | Declared role a source plays for a product (e.g. primary, context). | `data/registry/sources/` — NEEDS VERIFICATION |
| `watcher-as-non-publisher` | Doctrine that a watcher may detect change but never itself publishes catalog entries. | `docs/doctrine/` — NEEDS VERIFICATION |

> [!NOTE]
> The one-line meanings above are PROPOSED summaries for navigation. Confirm each against the encyclopedia and the cited `contracts/` / `schemas/` records before relying on them.

## Related docs
- [`docs/sources/catalog/README.md`](./README.md) — lane root.
- [`docs/sources/catalog/PROFILES.md`](./PROFILES.md) — catalog profile definitions.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority.

**Last reviewed:** 2026-05-20
