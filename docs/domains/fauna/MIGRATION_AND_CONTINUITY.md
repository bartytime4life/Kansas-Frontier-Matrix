<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-register-fauna-migration-continuity
title: Fauna Migration and Continuity
type: standard
version: v1
status: draft
owners: TODO(fauna-domain-stewards)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(verify-public-or-restricted)
related: [docs/domains/fauna/README.md, docs/domains/fauna/CONTROL_PLANE.md]
tags: [kfm, fauna, migration, continuity]
notes: [Protect prior fauna/habitat-fauna lineage and prevent rewrite-style migrations.]
[/KFM_META_BLOCK_V2] -->

# Fauna Migration and Continuity

## Continuity goals

- Preserve prior fauna and habitat+fauna work instead of restarting.
- Keep historical IDs and supersession lineage inspectable.
- Make migrations reversible where feasible.

## Migration protocol

1. Inventory existing fauna-adjacent files, schemas, fixtures, and releases.
2. Classify each item: retain, supersede, alias, retire, or quarantine.
3. Record mapping from prior IDs/paths to successor IDs/paths.
4. Run validation suite before and after migration.
5. Publish migration notes with rollback instructions.

## Supersession mapping template

| Prior artifact | Successor artifact | Change type | Reason | Rollback path |
|---|---|---|---|---|
| TODO | TODO | retain/supersede/alias/retire | TODO | TODO |

## Hard rules

- Never silently delete canonical lineage.
- Never repurpose identifiers without explicit mapping.
- Never publish migration results without updated validation evidence.

