<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/schema/readme
title: docs/registry/schema/ — Schema Documentation Routing Boundary
type: readme
version: v1.2
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Route readers from the registry documentation tree to current schema, fixture, validator, test, and policy owners without becoming any of those authorities."
truth_posture: "CONFIRMED current repository paths, fixture and validator child routing boundaries, and accepted placement doctrine / PARTIAL separate local schema-registry helper and hosted-workflow evidence / NOT IMPLEMENTED policy dry-run binding"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: debd3ceb1c9ce267cb26eaf8295e2371baf4ba0e
  prior_blob: 66af3122c97bc58d0f09363f6a480f73bcc48821
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

The [fixture README](fixture/README.md) and
[validator README](fixture/validator/README.md) are substantive routing-and-hold
boundaries grounded in the canonical package fixtures, partial package helper,
nine-test regression profile, and dedicated hosted workflow. The `dry-run/` leaf
is the only remaining inert placeholder and contains only a keep marker. This
documentation subtree implements no schema, fixture payload, validator, policy
rule, dry-run evaluator, approval, release effect, or publication authority.

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
- If the policy dry-run placeholder gains implementation, document its accepted
  contract, executable evaluator, consumer, validation, failure behavior, and
  authority boundary before changing its maturity claim.
- If that remaining placeholder has no intended consumer, retain it as an
  explicit open placement decision or remove it through a separately reviewed
  topology change.

Reverting this documentation commit restores this parent to v1.1 at blob
`66af3122c97bc58d0f09363f6a480f73bcc48821` and restores the validator child to
its prior blank blob. It does not roll back package behavior, schemas, fixtures,
validators, policy, tests, releases, deployments, or publication.

## Open verification register

| Question | Status |
|---|---|
| What scoped responsibility does `schema/fixture/README.md` own? | **CONFIRMED — documentation routing and evidence limits only** |
| What scoped responsibility does `schema/fixture/validator/README.md` own? | **CONFIRMED — documentation routing and evidence limits only** |
| Does `schema/fixture/validator/policy/dry-run/` have an accepted contract, executable evaluator, or consumer? | **NOT IMPLEMENTED** |
| Should the remaining policy dry-run placeholder remain, migrate to an owning root, or be retired? | **NEEDS DIRECTORY REVIEW** |
| Which reviewer owns future child-lane semantics beyond the current repository route? | **NEEDS VERIFICATION** |

[Back to registry documentation](../README.md) · [Back to top](#top)
