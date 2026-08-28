<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/schema/fixture/readme
title: docs/registry/schema/fixture/ — Schema Fixture Documentation Boundary
type: readme
version: v1.1
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Explain the current schema-registry fixture profiles and route readers to their canonical fixture, package, and test owners without storing fixture payloads or executable behavior here."
truth_posture: "CONFIRMED current fixture profiles, consumers, and validator documentation route / PARTIAL package and hosted-workflow evidence / NOT IMPLEMENTED policy dry-run binding"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: debd3ceb1c9ce267cb26eaf8295e2371baf4ba0e
  prior_blob: e37d9e04bd31aabd53a1c088dca17f8d4b78dcb6
related:
  - ../README.md
  - ../../README.md
  - ../../../doctrine/directory-rules.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../fixtures/README.md
  - ../../../../fixtures/packages/schema-registry/
  - ../../../../packages/schema-registry/IMPLEMENTATION.md
  - ../../../../tests/packages/schema_registry/test_core.py
  - validator/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/registry/schema/fixture/` — Schema Fixture Documentation Boundary

This directory documents how to find the current synthetic fixture evidence used
by the local schema-registry package. It does not contain the fixture payloads and
is not a fixture, schema, validator, test, policy, registry, or release authority.

> [!IMPORTANT]
> Fixture-backed success proves only the checked behavior over the committed
> synthetic cases at that revision. It does not prove canonical-schema parity,
> semantic truth, source admission, rights, policy permission, review, release,
> deployment, promotion, or publication.

## Use the owning surface

| Need | Current owning surface | Boundary |
|---|---|---|
| Understand schema-registry documentation | [Parent schema boundary](../README.md) | Human navigation only |
| Store reusable synthetic fixture payloads | [`fixtures/`](../../../../fixtures/README.md) | Canonical reusable fixture root |
| Inspect this package's fixture profiles | [`fixtures/packages/schema-registry/`](../../../../fixtures/packages/schema-registry/) | Synthetic package inputs; not governed runtime data |
| Inspect the consumer implementation | [`packages/schema-registry/`](../../../../packages/schema-registry/README.md) | Partial, read-only local registry helper |
| Inspect executable expectations | [`test_core.py`](../../../../tests/packages/schema_registry/test_core.py) | Bounded regression evidence |
| Define canonical machine shape | [`schemas/`](../../../../schemas/README.md) | Schema authority where declared |
| Implement or register validators | [`tools/validators/`](../../../../tools/validators/README.md) | Executable checks and registry mechanics |
| Decide normative outcomes | [`policy/`](../../../../policy/README.md) | Policy authority |

The accepted [Directory Rules v2](../../../doctrine/directory-rules.md), adopted
by [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md),
separate human documentation under `docs/` from reusable fixtures under
`fixtures/`, package mechanics under `packages/`, tests under `tests/`, and
machine shapes under `schemas/`.

## Current fixture profiles

At the pinned base, the canonical package fixture directory contains six schema
files across three profiles:

| Profile | Current files | Exercised outcome |
|---|---:|---|
| [`valid/`](../../../../fixtures/packages/schema-registry/valid/) | 3 | Two schemas with distinct `$id` values are indexed deterministically; one schema without `$id` is visibly skipped as `MISSING_ID` |
| [`duplicate/`](../../../../fixtures/packages/schema-registry/duplicate/) | 2 | Two schemas reuse one `$id`; registry construction fails closed with `DUPLICATE_ID` |
| [`invalid/`](../../../../fixtures/packages/schema-registry/invalid/) | 1 | One JSON document repeats a key; registry construction fails closed with `JSON_DUPLICATE_KEY` |

The package [implementation boundary](../../../../packages/schema-registry/IMPLEMENTATION.md)
also documents rejection of malformed roots, non-finite numbers, symlinks, path
escape, and bounded resource-limit violations. Some of those cases are created
temporarily inside the test module rather than stored in the canonical package
fixture directory.

The tests additionally exercise deterministic snapshot digests, local lookup,
unresolved lookup, file-size limits, symlink denial where the platform supports
symlinks, and deterministic command output with the tested network entry point
patched to fail. Read those results narrowly: the package remains partial and
does not yet replace
[`tools/validators/_common/local_resolver.py`](../../../../tools/validators/_common/local_resolver.py).

## Reproduce the implemented slice

The package implementation boundary defines these focused commands:

```bash
python -m pip install -e "./packages/schema-registry[test]"
python -m pytest -q tests/packages/schema_registry
kfm-schema-registry fixtures/packages/schema-registry/valid --pretty
```

Expected interpretation:

- a passing test run confirms the bounded package behaviors exercised by the
  current test module and synthetic inputs;
- the CLI command builds a read-only snapshot from the `valid/` profile;
- neither command mutates canonical schemas, writes lifecycle state, proves
  resolver parity over the canonical schema tree, or authorizes a consumer
  migration.

## This documentation subtree

The remaining child structure is:

```text
docs/registry/schema/fixture/
├── README.md
└── validator/
    ├── README.md
    └── policy/
        └── dry-run/
            └── .gitkeep
```

The [validator boundary](validator/README.md) now routes readers to the partial
package implementation, nine-test regression profile, dedicated hosted workflow,
and generated authoring receipt that currently own this bounded evidence. The
`dry-run/` leaf still contains only a keep marker. No policy dry-run contract,
registered orchestrator entry, executable policy evaluator, approval, release
effect, or publication authority is established by this documentation tree.

## Focused documentation validation

From the repository root:

```bash
python tools/validators/docs/link-check/check_links.py \
  docs/registry/schema/fixture/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  docs/registry/schema/fixture/README.md
python tools/validators/docs/fragments/check_fragments.py \
  docs/registry/schema/fixture/README.md
```

Passing documentation checks confirm only the checked Markdown metadata, links,
and fragments at that revision.

## Failure, maintenance, and rollback

- If fixture bytes and this guide disagree, preserve the canonical fixture and
  test evidence and correct this documentation through review.
- If a fixture profile changes, update its file count, expected outcome, named
  consumer, and focused reproduction command together.
- Keep real, restricted, rights-unclear, sensitive, or harmful-precision data out
  of repository fixtures; use minimized synthetic public-safe cases.
- Do not expand the policy dry-run child until an accepted contract, executable
  evaluator, and identified consumer are present in an owning implementation
  root.

Reverting this documentation commit restores this parent to v1.0 at blob
`e37d9e04bd31aabd53a1c088dca17f8d4b78dcb6` and restores the validator child to
its prior blank blob. It does not remove or change fixture payloads, package code,
tests, schemas, validators, policy, releases, deployments, or publication.

## Open verification register

| Question | Status |
|---|---|
| Does the package achieve identifier and document-resolution parity with the current canonical schema tree? | **NOT ESTABLISHED — separate parity proof required** |
| What scoped responsibility does `validator/README.md` own today? | **CONFIRMED — documentation routing and evidence limits only** |
| Does `validator/policy/dry-run/` have an accepted contract, executable entry point, or consumer? | **NOT IMPLEMENTED** |
| Should the remaining policy dry-run placeholder stay here, migrate to an owning root, or be retired? | **NEEDS DIRECTORY REVIEW** |
| Which reviewer owns future child-lane semantics beyond the current repository route? | **NEEDS VERIFICATION** |

[Back to schema documentation](../README.md) · [Back to top](#top)
