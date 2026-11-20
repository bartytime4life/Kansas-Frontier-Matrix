<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-policy-readme
title: migrations/policy/ — Policy-Path Migration Records
type: README; per-directory-readme; nested-migration-lane
version: v1.0
status: draft; repository-grounded; documented-lane; non-release; non-publication
owner: "@bartytime4life (CODEOWNERS default route)"
created: 2026-11-20
updated: 2026-11-20
current_path: migrations/policy/README.md
owning_root: migrations/
responsibility: record moves, renames and retirements of policy rule source into or within policy/, without becoming policy authority, an evaluator, a bundle, or a release or publication surface
decision_refs:
  - "ADR-0003 (accepted 2026-11-20): policy/ singular is canonical; names this lane in §8.4"
  - "ADR-0029: adopts Directory Rules v2, including DIR-AUTHROOT-003 and the §18 migration contract"
[/KFM_META_BLOCK_V2] -->

# `migrations/policy/`

Records for moving policy rule source into, or within, `policy/`. The
repository owner named this lane when accepting
[ADR-0003](<../../docs/adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>)
on 2026-11-20 (§8.4). Before that, `migrations/` had database, schema, data,
graph and rollback lanes and no home for policy-path moves.

## What belongs here

- One record per policy-path migration, named `YYYYMMDD_<slug>.yaml`, using the
  [Directory Rules §18.2](../../docs/doctrine/directory-rules.md) migration
  minimum for each moved or retired file: old and new paths, content digests
  before and after, producers, consumers, compatibility mode, validation and
  the recovery reference.
- A paired recovery record under [`../rollback/`](../rollback/) for every
  record here, including forward-fix-only cases.

## What does not belong here

- Policy rule source itself, which stays under [`policy/`](../../policy/).
- Policy decisions, bundles, release manifests or rollback cards.
- Database, schema, data or graph migrations, which have their own lanes.

A record here does not activate a bundle or evaluator, approve a release, or
publish anything.

## Records

| Record | Paired recovery | Summary |
|---|---|---|
| [`20261120_g_place_01_release_rego.yaml`](./20261120_g_place_01_release_rego.yaml) | [`../rollback/20261120_g_place_01_release_rego.yaml`](../rollback/20261120_g_place_01_release_rego.yaml) | Gap `G-PLACE-01`: retires the three Rego scaffolds at the `release/` root in favour of the existing `policy/domains/hydrology/release.rego` and `policy/domains/geology/release/` scaffolds. |

## Validation

No migration-manifest schema or runner exists yet; records use the §18.2 field
names verbatim. Each record lists the checks run for it, for example the
topology validator, scaffold and gap ratchets, and the OPA-backed
`tests/policy/` suite.
