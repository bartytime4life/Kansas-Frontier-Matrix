<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/schema/fixture/validator/readme
title: docs/registry/schema/fixture/validator/ — Schema Fixture Validator Documentation Boundary
type: readme
version: v1.2
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Route readers to the implemented schema-registry package checks, fixtures, tests, workflow, and receipt integrity boundary without becoming validator, policy, proof, or release authority."
truth_posture: "CONFIRMED package tests, fixture snapshot checks, dedicated workflow, absent orchestrator registration, and documented nested policy/dry-run holds at the pinned base / PARTIAL no-network and package validation evidence / NOT IMPLEMENTED nested policy dry-run binding"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ba8856e1fc2bf930e9b44df1cfbf4f3dc369d084
  prior_blob: cb7e3b060d5293827a0a884f62ddcc76076e07dc
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../doctrine/directory-rules.md
  - ../../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../../packages/schema-registry/IMPLEMENTATION.md
  - ../../../../../fixtures/packages/schema-registry/
  - ../../../../../tests/packages/schema_registry/test_core.py
  - ../../../../../.github/workflows/schema-registry-package.yml
  - ../../../../../tools/validators/validator_registry.json
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/registry/schema/fixture/validator/` — Schema Fixture Validator Documentation Boundary

This directory explains the current validation surfaces for the local
schema-registry package. It contains no validator implementation, package code,
fixtures, policy rule, proof, receipt, or release artifact.

> [!IMPORTANT]
> A passing validator or workflow is bounded execution evidence. It does not make
> fixture data factual, establish canonical-schema parity, decide policy,
> authenticate review, authorize consumer migration, release, deploy, promote, or
> publish anything.

## Use the owning surface

| Need | Current owning surface | Boundary |
|---|---|---|
| Understand the fixture profiles | [Parent fixture boundary](../README.md) | Human documentation only |
| Inspect package mechanics | [`packages/schema-registry/`](../../../../../packages/schema-registry/README.md) | Partial, read-only local registry helper |
| Inspect synthetic inputs | [`fixtures/packages/schema-registry/`](../../../../../fixtures/packages/schema-registry/) | Canonical reusable fixtures for this package |
| Inspect executable expectations | [`test_core.py`](../../../../../tests/packages/schema_registry/test_core.py) | Nine bounded package and CLI tests |
| Inspect hosted orchestration | [`schema-registry-package.yml`](../../../../../.github/workflows/schema-registry-package.yml) | Dedicated package workflow |
| Inspect generated authoring lineage | [Package authoring receipt](../../../../../data/receipts/generated/genrec-schema-registry-package-20260809.json) | Byte-bound authoring receipt; not runtime proof or approval |
| Inspect the general validator orchestrator | [Validator runbook](../../../../runbooks/VALIDATOR_ORCHESTRATOR.md) and [registry](../../../../../tools/validators/validator_registry.json) | Separate registered-validator system |
| Decide normative outcomes | [`policy/`](../../../../../policy/README.md) | Policy authority |

The accepted [Directory Rules v2](../../../../doctrine/directory-rules.md),
adopted by
[ADR-0029](../../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md),
keep documentation under `docs/`, executable checker mechanics under
`packages/` or `tools/validators/`, reusable inputs under `fixtures/`, tests
under `tests/`, workflows under `.github/workflows/`, and policy under
`policy/`.

## Implemented package validation

At the pinned base, the package test module contains nine tests covering:

- deterministic fixture snapshots and creation-order-independent digests;
- local resolution, unresolved lookup, and conversion to a
  `referencing.Registry`;
- duplicate `$id`, duplicate JSON key, missing-root, and file-size failures;
- symlink denial where the platform supports symlinks; and
- deterministic CLI output while the tested `socket.create_connection` entry
  point is patched to fail.

The [implementation boundary](../../../../../packages/schema-registry/IMPLEMENTATION.md)
classifies the package as partial, fixture-first, no-network, and helper-only. It
explicitly requires a separate parity change before replacing
[`tools/validators/_common/local_resolver.py`](../../../../../tools/validators/_common/local_resolver.py)
or migrating a consumer.

## Dedicated hosted workflow

The package workflow runs when its workflow, package, fixture, test, or named
generated-receipt paths change. It does not list this documentation subtree in its
path filter.

Its validation job:

1. checks out the tested revision without persisted credentials;
2. installs the declared schema-registry test profile;
3. runs the nine package tests;
4. creates a CLI snapshot from the `valid/` fixture profile;
5. asserts `RESOLVED`, two indexed records, and one skipped record; and
6. validates the generated authoring receipt's artifact hashes.

The workflow sets `KFM_NO_NETWORK=1` and the package test patches one Python
socket entry point. Treat that as the implemented bounded posture, not proof of
operating-system-wide or dependency-install egress prevention.

## Orchestrator relationship

The current
[`validator_registry.json`](../../../../../tools/validators/validator_registry.json)
contains 24 registered validators across `focused`, `changed-area`,
`release-dry-run`, and `full` profiles. None of those entries references the
schema-registry package at the pinned base.

Therefore:

- the dedicated package workflow is the hosted owner for this package slice;
- `python tools/validate_all.py --profile full` does not imply execution of the
  package's tests or CLI snapshot;
- `make schemas` remains the separately documented historical schema-fixture
  compatibility runner; and
- registering this package in the orchestrator would require a separate
  implementation and review change, not a documentation inference.

## Reproduce the current checks

Package-local commands documented by the implementation boundary:

```bash
python -m pip install -e "./packages/schema-registry[test]"
python -m pytest -q tests/packages/schema_registry
kfm-schema-registry fixtures/packages/schema-registry/valid --pretty
```

Workflow-equivalent repository commands:

```bash
python tools/ci/install_python_ci.py project-test-schema-registry-test
python -m pytest -q tests/packages/schema_registry
kfm-schema-registry fixtures/packages/schema-registry/valid
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-schema-registry-package-20260809.json \
  --repo-root .
```

Interpret success narrowly. These commands do not prove current canonical-tree
parity, validate every repository schema, create a validation receipt, evaluate
policy, or change lifecycle, release, deployment, promotion, or publication
state.

## Policy dry-run child status

This documentation subtree currently ends at:

```text
docs/registry/schema/fixture/validator/
├── README.md
└── policy/
    ├── README.md
    └── dry-run/
        ├── .gitkeep
        └── README.md
```

The [`policy/`](policy/README.md) and
[`policy/dry-run/`](policy/dry-run/README.md) READMEs now make the local routing
and admission hold explicit. The leaf contains only `.gitkeep` plus its README.
No policy input contract, bundle, evaluator, outcome mapping, fixture, test,
command, workflow, consumer, receipt, or operational rollback procedure is
implemented there.

External planning material proposes dry-run compilers and no-autopublish policy
gates, but current repository evidence does not adopt or implement those ideas in
this lane.

## Focused documentation validation

From the repository root:

```bash
python tools/validators/docs/link-check/check_links.py \
  docs/registry/schema/fixture/validator/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  docs/registry/schema/fixture/validator/README.md
```

The link checker covers repository-local files, directories, images, and
fragments; the metadata checker covers the bounded metadata envelope. Passing
either confirms only its exercised documentation QA scope at that revision.

## Failure, maintenance, and rollback

- If package code, tests, workflow, or the validator registry contradict this
  guide, preserve the owning artifact and correct this document through review.
- Update the test count, workflow steps, snapshot expectations, receipt path, and
  orchestrator-registration statement together when those surfaces change.
- Do not add policy dry-run instructions until an accepted contract, evaluator,
  fixtures, tests, consumer, failure behavior, and rollback owner exist.
- Keep validation output free of sensitive payloads and harmful precision; a
  verbose local diagnostic is not automatically public-safe evidence.

This v1.2 documentation slice changes no package, validator, or policy behavior.
Before merge, close the draft pull request and abandon its branch. After merge,
prefer a focused forward correction. Do not restore marker-only child
status merely to revise wording, and do not move or delete the held path without
an accepted placement decision and verified reference closure.

## Open verification register

| Question | Status |
|---|---|
| Does the package achieve identifier and document-resolution parity with the current canonical schema tree? | **NOT ESTABLISHED — separate parity proof required** |
| Should the package be registered in the general validator orchestrator? | **NEEDS DESIGN AND IMPLEMENTATION REVIEW** |
| Does `policy/dry-run/` have an accepted contract, evaluator, fixture profile, or consumer? | **NOT IMPLEMENTED** |
| Should the empty policy dry-run leaf remain here, migrate to an owning root, or be retired? | **NEEDS DIRECTORY REVIEW** |
| Which reviewer owns future policy dry-run semantics? | **NEEDS VERIFICATION** |

[Back to fixture documentation](../README.md) · [Back to top](#top)
