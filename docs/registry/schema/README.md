<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/schema/readme
title: docs/registry/schema/ — Schema Documentation Routing Boundary
type: readme
version: v1.0
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Route readers from the registry documentation tree to current schema, fixture, validator, test, and policy owners without becoming any of those authorities."
truth_posture: "CONFIRMED current repository paths, placeholder topology, and accepted placement doctrine / PARTIAL separate local schema-registry helper implementation / UNKNOWN intended ownership and future use of the nested fixture-validator dry-run lane"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e52165e820b07e65c54830fde519a9c90df8eb1c
  prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../schemas/README.md
  - ../../../packages/schema-registry/README.md
  - ../../../fixtures/README.md
  - ../../../tools/validators/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/registry/schema/` — Schema Documentation Routing Boundary

This directory explains where to find current schema-related registry evidence. It
is a human documentation lane under `docs/`; it does not own schemas, fixtures,
validators, policy, tests, registry records, or runtime behavior.

> [!IMPORTANT]
> A schema can constrain machine shape. It does not by itself establish semantic
> truth, source admission, rights, policy permission, review, release,
> deployment, promotion, or publication.

## Use the owning surface

| Need | Current owning surface | Boundary |
|---|---|---|
| Understand this documentation lane | [Registry documentation boundary](../README.md) | Human navigation only |
| Define machine-checkable shape | [`schemas/`](../../../schemas/README.md) | Schema authority where the owning artifact declares it |
| Define semantic meaning and interface promises | [`contracts/`](../../../contracts/README.md) | Semantic contract authority |
| Reuse synthetic test inputs and expected outputs | [`fixtures/`](../../../fixtures/README.md) | Canonical reusable fixture root; fixtures are not governed runtime data |
| Implement or register validators | [`tools/validators/`](../../../tools/validators/README.md) and [`validator_registry.json`](../../../tools/validators/validator_registry.json) | Executable checks and their registry, not policy or release authority |
| Exercise behavior | [`tests/`](../../../tests/README.md) | Bounded executable evidence |
| Decide allow, deny, hold, restrict, or abstain outcomes | [`policy/`](../../../policy/README.md) | Normative policy authority |
| Build a local read-only schema index for package consumers | [`packages/schema-registry/`](../../../packages/schema-registry/README.md) | Separate, partial helper implementation; not owned by this documentation path |

The accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted by
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), keep
human documentation under `docs/`, machine shapes under `schemas/`, reusable
fixtures under `fixtures/`, and executable checks under their implementation
and test roots.

## Current repository evidence

The separate [schema-registry package](../../../packages/schema-registry/README.md)
currently provides fixture-first, no-network, read-only local indexing mechanics.
Its [implementation boundary](../../../packages/schema-registry/IMPLEMENTATION.md)
classifies the package as partial and states that it does not replace the existing
[local validator resolver](../../../tools/validators/_common/local_resolver.py).
That package is implementation evidence for its own scope; it does not make this
documentation directory a schema registry or transfer authority into `docs/`.

At the pinned base, this documentation subtree contains:

```text
docs/registry/schema/
├── README.md
└── fixture/
    ├── README.md
    └── validator/
        ├── README.md
        └── policy/
            └── dry-run/
                └── .gitkeep
```

The two deeper README files are one-byte placeholders, and the `dry-run/` leaf
contains only a keep marker. No schema file, fixture payload, validator
implementation, policy rule, executable dry-run command, test, workflow, or
consumer is established by this subtree.

## Inputs and outputs

This README accepts current repository paths and accepted placement doctrine as
evidence. Its output is navigation and explicit uncertainty only.

Do not write canonical schema definitions, reusable fixture payloads, validator
code, policy rules, test results, or release artifacts here. When a future child
document is justified, it should identify the owning implementation and link to
it without duplicating the authoritative bytes.

## Focused documentation validation

From the repository root:

```bash
python tools/validators/docs/link-check/check_links.py docs/registry/schema/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  docs/registry/schema/README.md
python tools/validators/docs/fragments/check_fragments.py \
  docs/registry/schema/README.md
```

A passing documentation check confirms only that the checked Markdown structure,
metadata, links, and fragments satisfy the exercised rules at that revision. It
does not implement or approve a schema, fixture contract, validator policy,
dry-run capability, release, or publication.

## Failure and correction guidance

- If a link fails, verify the owning path on current `main`; do not create a
  parallel authority merely to preserve this document.
- If an owning artifact contradicts this guide, preserve the owning artifact and
  correct this documentation through review.
- If a child placeholder gains implementation, document its exact consumer,
  validation, inputs, outputs, failure behavior, and authority boundary before
  changing its maturity claim.
- If the placeholder chain has no intended consumer, retain it as an explicit
  open placement decision or remove it through a separately reviewed topology
  change.

Reverting this documentation commit restores the prior blank file. It does not
roll back package behavior, schemas, fixtures, validators, policy, tests,
releases, deployments, or publication.

## Open verification register

| Question | Status |
|---|---|
| What scoped responsibility, if any, should `schema/fixture/README.md` own? | **UNKNOWN** |
| Is `schema/fixture/validator/README.md` intended to document an implemented consumer? | **UNKNOWN — no consumer is established by this subtree** |
| Does `schema/fixture/validator/policy/dry-run/` have an accepted contract or executable entry point? | **NOT IMPLEMENTED in this subtree** |
| Should the nested placeholder chain remain, migrate to an owning root, or be retired? | **NEEDS DIRECTORY REVIEW** |
| Which reviewer owns future child-lane semantics beyond the current repository route? | **NEEDS VERIFICATION** |

[Back to registry documentation](../README.md) · [Back to top](#top)
