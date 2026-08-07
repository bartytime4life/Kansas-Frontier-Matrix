<!--
KFM_WIKI_SOURCE
page_id: Repository-Map
title: Repository Map
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Repository-Map.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Repository Map

KFM uses a **responsibility-root monorepo**. A path is an authority claim: the root states which responsibility may own and mutate the artifact. Domains, sources, places, and object families refine that responsibility inside the root; they do not create new top-level roots.

## Current root map

```text
Kansas-Frontier-Matrix/
├── .github/        GitHub platform orchestration and review routing
├── apps/           deployable applications
├── configs/        non-secret configuration
├── connectors/     source acquisition and admission edges
├── contracts/      semantic meaning and invariants
├── control_plane/  machine governance projections and indexes
├── data/           lifecycle and accountability instances
├── docs/           human doctrine, decisions, architecture, and guidance
├── examples/       runnable public-safe demonstrations
├── fixtures/       deterministic valid, invalid, denied, and golden inputs
├── infra/          deployment and exposure infrastructure
├── migrations/     versioned migrations and rollback definitions
├── packages/       reusable non-deployable implementation
├── pipeline_specs/ declarative pipeline definitions
├── pipelines/      executable lifecycle transformations
├── policy/         allow, deny, restrict, hold, and abstain rules
├── release/        release, correction, withdrawal, and rollback decisions
├── runtime/        bounded local/runtime adapters
├── schemas/        machine-checkable shapes
├── scripts/        thin operational helpers
├── tests/          executable conformance evidence
└── tools/          validators, generators, builders, and operators
```

The current repository also documents `artifacts/` as a compatibility/generated-output transition, `catalog/` as a deprecated containment root frozen to new writes, and `src/` as conditional. Read the current [root README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md) and [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) before acting.

## Responsibility table

| Question | Owning root |
|---|---|
| Explain it to humans | `docs/` |
| Index governance for machines | `control_plane/` |
| Define what an object means | `contracts/` |
| Define its machine-checkable shape | `schemas/` |
| Decide whether use or exposure is allowed | `policy/` |
| Prove a rule or behavior is enforceable | `tests/` and `fixtures/` |
| Build or validate repository state | `tools/` |
| Operate a small helper | `scripts/` |
| Run a deployable service or UI | `apps/` |
| Share reusable implementation | `packages/` |
| Fetch or admit an external source | `connectors/` |
| Execute or declare a pipeline | `pipelines/` and `pipeline_specs/` |
| Store lifecycle, evidence, receipts, proofs, catalog, or published instances | the correct `data/` lane |
| Record a release, correction, withdrawal, or rollback decision | `release/` |

## Placement decision

Before creating, moving, renaming, or deleting a path:

1. Identify the artifact kind.
2. Identify exactly one authority owner.
3. Choose the candidate responsibility root.
4. Apply exclusions for lifecycle, execution role, exposure, mutability, and retention.
5. Add domain, source, geography, seam, or object-family scope only after the root is fixed.
6. Check existing canonical, compatibility, generated, and legacy homes.
7. Check dependency direction.
8. Emit one finite result: `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, or `DENY`.

"Probably here" is not a governed placement result.

## Domain-as-lane pattern

Hydrology is a domain, not a root:

```text
docs/domains/hydrology/
contracts/domains/hydrology/
schemas/contracts/v1/domains/hydrology/
policy/domains/hydrology/
fixtures/.../hydrology/
tests/domains/hydrology/
pipelines/.../hydrology/
data/raw/hydrology/
data/work/hydrology/
data/processed/hydrology/
data/catalog/hydrology/
data/published/hydrology/
```

These are illustrative responsibility segments. Verify exact current conventions before creating a path.

## Wiki placement

`docs/wiki/` belongs under `docs/` because it explains the project to humans. It does not own native-wiki platform settings, machine indexes, doctrine, policy, evidence, release, or publication. The native GitHub Wiki is a derived public projection, not a new KFM authority root.

## Authority references

- [Accepted ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md)
- [Contributing: choose the owning root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md#choose-the-owning-responsibility-root)
- [Root repository map](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md#repository-map)
