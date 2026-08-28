<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/schema/fixture/validator/policy/readme
title: docs/registry/schema/fixture/validator/policy/ — Policy Documentation Routing Hold
type: readme
version: v1.0
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Explain the nested policy documentation segment, route normative work to the canonical policy root, and prevent this subtree from becoming a parallel policy, validator, fixture, or release authority."
truth_posture: "CONFIRMED documentation-only parent with one dry-run child and no policy source, contract, schema, evaluator, fixture, test, workflow, consumer, receipt, release, or publication binding / HOLD placement, migration, or retirement / UNKNOWN accepted child semantics and independent reviewer"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 630f468f9c7672309fdffade6e1537ebbafc4f03
  prior_state: no README; directory contained only the dry-run child
related:
  - ../README.md
  - dry-run/README.md
  - ../../../README.md
  - ../../../../../doctrine/directory-rules.md
  - ../../../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../../../policy/README.md
  - ../../../../../../tools/validators/validator_registry.json
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/registry/schema/fixture/validator/policy/` — Policy Documentation Routing Hold

This directory is a human-readable grouping under `docs/`. Its `policy` path
segment does not make it a policy root, policy bundle, evaluator, decision
store, validation profile, release gate, or public interface.

> [!IMPORTANT]
> Normative policy source remains under the canonical [`policy/`](../../../../../../policy/README.md)
> root. Documentation can explain a boundary, but it cannot create an allow, deny,
> hold, restrict, or abstain decision or activate an evaluator.

## Current contents and maturity

```text
docs/registry/schema/fixture/validator/policy/
├── README.md
└── dry-run/
    ├── .gitkeep
    └── README.md
```

Both Markdown files are routing-and-hold documentation. The subtree contains no
Rego, JSON, YAML, Python, shell, package metadata, policy input contract, schema,
fixture payload, test, workflow, receipt, result, proof, release object, or
consumer binding.

## Authority routing

| Need | Owning surface | Current boundary |
|---|---|---|
| Define normative outcomes | [`policy/`](../../../../../../policy/README.md) | Canonical policy source; this documentation path is not an alias |
| Define semantic inputs or outputs | [`contracts/`](../../../../../../contracts/README.md) | Semantic contract authority |
| Define machine shape | [`schemas/`](../../../../../../schemas/README.md) | Schema authority where declared |
| Implement or register a validator | [`tools/validators/`](../../../../../../tools/validators/README.md) | Executable validator and registry mechanics |
| Store reusable synthetic inputs | [`fixtures/`](../../../../../../fixtures/README.md) | Canonical fixture root |
| Exercise behavior | [`tests/`](../../../../../../tests/README.md) | Executable test evidence |
| Explain this nested hold | This README and the [dry-run child](dry-run/README.md) | Human documentation only |

The accepted [Directory Rules v2](../../../../../doctrine/directory-rules.md),
adopted by [ADR-0029](../../../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md),
separate these responsibilities and prohibit parallel writable authority.

## Dry-run child relationship

The [dry-run child](dry-run/README.md) records a marker-only implementation
state and the prerequisites for any future change. It does not define a dry-run
request, result, compiler, policy bundle, evaluator, outcome mapping, or
no-autopublish gate.

At the pinned base, the general
[validator registry](../../../../../../tools/validators/validator_registry.json)
contains 24 validators across four profiles and has no schema-registry package
entry. The dedicated
[schema-registry package workflow](../../../../../../.github/workflows/schema-registry-package.yml)
does not include this documentation subtree in its path filter. Neither fact
creates or validates a policy dry-run capability here.

## Admission and placement gate

Before executable or normative content is added, a reviewed change must establish:

1. the single responsibility and accepted canonical home;
2. a semantic contract and machine shape where required;
3. normative policy source and finite outcome mapping where required;
4. deterministic implementation, minimized synthetic fixtures, and positive,
   negative, boundary, and regression tests;
5. a named consumer and explicit no-network or bounded-network posture;
6. workflow invocation and current required-check evidence;
7. sensitivity, rights, provenance, retention, correction, and rollback behavior;
8. a migration or retirement plan for this documentation path; and
9. accountable policy, validator, security, domain, and independent review.

A README, `.gitkeep`, green workflow, commit, merge, or generated receipt cannot
satisfy this gate by itself.

## Focused documentation validation

From the repository root:

```bash
python tools/validators/docs/link-check/check_links.py \
  docs/registry/schema/fixture/validator/policy/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  docs/registry/schema/fixture/validator/policy/README.md
python tools/validators/docs/fragments/check_fragments.py \
  docs/registry/schema/fixture/validator/policy/README.md
```

Passing these checks confirms only the checked Markdown structure, metadata,
links, and fragments.

## Failure, correction, and rollback

- If repository implementation contradicts this guide, preserve the owning
  implementation and correct this documentation through review.
- If an unexpected executable or data file appears here, treat the maturity
  claim as stale and evaluate placement before treating the file as legitimate.
- Do not copy external planning prose into this subtree as active policy.
- Keep sensitive payloads, harmful precision, credentials, and rights-unclear
  source material out of documentation and fixtures.

This revision adds documentation only. Before merge, close the draft pull request
and abandon its branch. After merge, prefer a focused forward correction. Do not
delete or move the path without an accepted placement decision and verified
reference closure.

## Open verification register

| Question | Status |
|---|---|
| Why does a policy-named segment exist beneath schema-fixture-validator documentation? | **UNKNOWN / NEEDS DIRECTORY REVIEW** |
| Does any repository or external consumer depend on this path identity? | **UNKNOWN** |
| Does the child have an accepted contract, evaluator, or finite outcome mapping? | **NOT IMPLEMENTED** |
| Should this subtree remain as documentation, migrate, or retire? | **HOLD / NEEDS PLACEMENT DECISION** |
| Who owns future semantics and independent review? | **NEEDS VERIFICATION** |

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-28 | Establishes the nested policy segment as a documentation-only routing and placement hold; no policy or runtime behavior is added. |

[Back to validator documentation](../README.md) · [Open dry-run hold](dry-run/README.md) · [Back to top](#top)
