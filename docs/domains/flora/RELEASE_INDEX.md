<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-flora-release-index
title: Flora Domain — Release Index
type: index
version: v2.1
status: draft
owners: TODO (flora domain steward + governance steward)
created: 2026-05-16
updated: 2026-10-12
policy_label: public
owning_root: docs/
responsibility: Human-facing navigation index for Flora release candidates, published artifacts, correction, and rollback; holds no release decisions or artifacts.
truth_posture: NEEDS VERIFICATION — no Flora release instance is confirmed; every path listed here is navigation only and is not release, policy, or publication authority.
related:
  - docs/domains/flora/README.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/fauna/RELEASE_INDEX.md
  - docs/registers/RELEASE_REGISTER.md
  - docs/runbooks/flora/PROMOTION_RUNBOOK.md
  - release/candidates/flora/
  - release/manifests/
  - data/published/flora/
  - data/published/layers/flora/
  - data/rollback/flora/
  - pipelines/domains/flora/publish/
tags: [kfm, domain, flora, release, index, governance]
notes:
  - "2026-10-12 (v2.1): this file was a verbatim copy of docs/domains/flora/README.md (CRLF line endings, same doc_id kfm://doc/docs-domains-flora-readme); given its own path-derived doc_id and release-index title, and the duplicated README body replaced by this index — no content lost, the full text remains in README.md (duplicate doc_id removal)."
[/KFM_META_BLOCK_V2] -->

# Flora Domain — Release Index

> Navigation index for Flora releases. It points to where Flora release candidates, published artifacts, correction, and rollback are documented. It does not hold release decisions, manifests, or artifacts, and it does not establish that any Flora release exists.

> [!NOTE]
> Until 2026-10-12 this path held a verbatim copy of the [Flora domain README](./README.md) under the README's doc_id. That copy was removed; the domain orientation, deny-by-default posture, object families, and lifecycle intent now live only in [`README.md`](./README.md).

## Release state

| Item | Status |
|---|---|
| Confirmed Flora release instances | None found — `NEEDS VERIFICATION` |
| Release candidates | [`release/candidates/flora/`](../../../release/candidates/flora/README.md) — "A candidate is not a release." |
| Release manifests | [`release/manifests/`](../../../release/manifests/) — no Flora manifest confirmed |

## Where to look

| Need | Go to |
|---|---|
| Domain scope, object families, lifecycle | [Flora README](./README.md) and its [pipeline shape](./README.md#7-pipeline-shape-raw--published) |
| Sensitivity and publication posture (deny-by-default for exact rare-plant geometry) | [README §9](./README.md#9-sensitivity-rights--publication-posture) |
| Release gate, correction, and rollback rules | [`PUBLICATION_AND_ROLLBACK.md`](./PUBLICATION_AND_ROLLBACK.md) |
| Promotion procedure | [`docs/runbooks/flora/PROMOTION_RUNBOOK.md`](../../runbooks/flora/PROMOTION_RUNBOOK.md) |
| Published Flora artifacts | [`data/published/flora/`](../../../data/published/flora/README.md), [`data/published/layers/flora/`](../../../data/published/layers/flora/README.md) |
| Rollback records | [`data/rollback/flora/`](../../../data/rollback/flora/README.md) |
| Publish pipeline | [`pipelines/domains/flora/publish/`](../../../pipelines/domains/flora/publish/README.md) |
| Cross-domain release register | [`docs/registers/RELEASE_REGISTER.md`](../../registers/RELEASE_REGISTER.md) |
| Sibling pattern | [Fauna release index](../fauna/RELEASE_INDEX.md) |

## Open questions

- Which Flora release IDs, manifests, and rollback targets exist? None are confirmed; add rows here only after a governed release is recorded under `release/`.
