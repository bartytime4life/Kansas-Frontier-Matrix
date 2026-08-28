<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/schema/fixture/validator/policy/dry-run/readme
title: docs/registry/schema/fixture/validator/policy/dry-run/ — Policy Dry-Run Documentation Hold
type: readme
version: v1.1
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Record the marker-only policy dry-run state, route future work to owning roots, and prevent proposal lineage or path names from being mistaken for implemented validation, policy, release, or publication behavior."
truth_posture: "CONFIRMED .gitkeep-only leaf before this revision and no contract, schema, policy source, bundle, evaluator, fixture, test, command, workflow, consumer, receipt, proof, release, or publication binding / PROPOSED external dry-run and no-autopublish concepts remain lineage only / HOLD implementation, placement, migration, or retirement / UNKNOWN consumers and accepted reviewer"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ba8856e1fc2bf930e9b44df1cfbf4f3dc369d084
  prior_blob: 51a731552da4866468bcbc6e225fed8dd57deaf8
  prior_state: .gitkeep only; no README or executable payload
related:
  - ../README.md
  - ../../README.md
  - ../../../../README.md
  - ../../../../../../doctrine/directory-rules.md
  - ../../../../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../../../../policy/README.md
  - ../../../../../../../packages/schema-registry/IMPLEMENTATION.md
  - ../../../../../../../tools/validators/validator_registry.json
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/registry/schema/fixture/validator/policy/dry-run/` — Policy Dry-Run Documentation Hold

> **Current boundary:** this leaf is documentation over an inert keep marker. It
> does not implement a dry-run compiler, policy gate, validator profile, schema
> registry operation, release rehearsal, or no-autopublish control.

## Current evidence

```text
docs/registry/schema/fixture/validator/policy/dry-run/
├── .gitkeep
└── README.md
```

At the pinned base, `.gitkeep` was the only tracked file. No policy input or
result contract, JSON Schema, Rego bundle, evaluator, fixture, test, command,
workflow, consumer, receipt, proof, release object, correction record, or
operational rollback procedure was implemented here.

The separate [schema-registry package](../../../../../../../packages/schema-registry/IMPLEMENTATION.md)
is a partial, read-only, fixture-first local index helper with nine bounded tests.
Its dedicated workflow does not watch this documentation path, and the general
[validator registry](../../../../../../../tools/validators/validator_registry.json)
has no schema-registry package entry at the pinned base. Package success cannot
be translated into a policy dry-run result.

## What this path does not mean

- `docs/` remains human explanation, not executable authority.
- The `policy` segment does not alias the canonical [`policy/`](../../../../../../../policy/README.md) root.
- `dry-run` does not imply side-effect freedom, no-network enforcement, replay,
  or release safety.
- A marker, README, workflow result, generated receipt, commit, or merge does not
  activate policy or authorize release, deployment, promotion, or publication.
- External Drive or Notion proposals remain read-only lineage until adopted and
  implemented through current repository evidence.

## Contributor routing

| Proposed artifact | Start with the owning root |
|---|---|
| Semantic dry-run request or result | [`contracts/`](../../../../../../../contracts/README.md) |
| Machine-checkable shape | [`schemas/`](../../../../../../../schemas/README.md) |
| Normative allow, deny, hold, restrict, or abstain rule | [`policy/`](../../../../../../../policy/README.md) |
| Reusable implementation or registered validator | [`packages/`](../../../../../../../packages/README.md) or [`tools/validators/`](../../../../../../../tools/validators/README.md) |
| Minimized synthetic inputs and expected outputs | [`fixtures/`](../../../../../../../fixtures/README.md) |
| Executable assertions | [`tests/`](../../../../../../../tests/README.md) |
| Human routing and uncertainty | This README and its [policy parent](../README.md) |

Do not select a more specific home until accepted doctrine, current implementation
evidence, and the affected root owners establish it.

## Minimum implementation evidence

Before this leaf can be described as implemented, evidence must identify:

1. a versioned semantic contract and, where needed, schema;
2. the exact policy source, evaluator, finite outcomes, and fail-closed behavior;
3. deterministic implementation with explicit side-effect and network boundaries;
4. minimized synthetic positive, negative, boundary, and regression fixtures;
5. executable tests that consume the exact fixture bytes;
6. a workflow or orchestrator entry that invokes the implementation;
7. a named consumer and authenticated result or receipt boundary;
8. sensitivity, rights, provenance, retention, correction, replay, and rollback;
9. separation among validation, review, merge, release, deployment, promotion,
   and publication; and
10. accountable implementation, policy, security, domain, and independent review.

Evidence that proves only one item cannot be used to infer the others.

## Validate the current hold

From the repository root:

```bash
git ls-tree -r --name-only HEAD -- \
  docs/registry/schema/fixture/validator/policy/dry-run

find docs/registry/schema/fixture/validator/policy/dry-run -type f \
  ! -name 'README.md' \
  ! -name '.gitkeep' \
  -print

python tools/validators/docs/link-check/check_links.py \
  docs/registry/schema/fixture/validator/policy/dry-run/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  docs/registry/schema/fixture/validator/policy/dry-run/README.md
```

The link checker covers repository-local files, directories, images, and
fragments; the metadata checker covers the bounded metadata envelope. Passing
either confirms only its exercised documentation QA scope at that revision.

For the documented state, `find` must print nothing. A nonempty result means the
inventory and maturity claim require review; it does not prove that the new file
is correctly placed, executable, safe, or authoritative.

## Safety and lifecycle limits

Keep living-person data, DNA or genomic data, private land information, protected
cultural material, exact sensitive locations, infrastructure detail, credentials,
and rights-unclear source payloads out of this documentation lane.

A future dry-run may model `RAW`, `WORK/QUARANTINE`, `PROCESSED`,
`CATALOG/TRIPLET`, or `PUBLISHED` states without performing a lifecycle
transition. Public clients must use governed interfaces or released public-safe
artifacts, never repository documentation, fixtures, policy source, internal
registries, or workflow output as live truth.

## Failure, correction, and rollback

- If owning implementation contradicts this README, preserve the implementation
  evidence and narrow or correct the documentation.
- If unexpected payload appears, classify its responsibility, sensitivity,
  consumer, and authority before use; do not normalize path drift through prose.
- If the path migrates or retires, require an accepted target, reference closure,
  single-write behavior, exit criteria, and rollback.

This revision changes documentation only. Before merge, close the draft pull
request and abandon its branch. After merge, use a focused forward correction.
Do not restore the README-less marker state merely to change wording.

## Open verification register

| Question | Status |
|---|---|
| Is any dry-run contract, evaluator, fixture profile, command, workflow, or consumer implemented for this path? | **NO — NOT IMPLEMENTED** |
| Does any repository or external consumer depend on this path identity? | **UNKNOWN** |
| Should the path remain, migrate to an owning root, or retire? | **HOLD / NEEDS DIRECTORY REVIEW** |
| What side effects and network boundaries would an eventual dry-run require? | **UNKNOWN / REQUIRES CONTRACT** |
| Who owns semantics, security review, and independent approval? | **NEEDS VERIFICATION** |

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.1 | 2026-08-28 | Removes the nonexistent standalone fragment-checker command and records that the supported link checker covers local fragments. |
| v1.0 | 2026-08-28 | Replaces a README-less marker state with an evidence-grounded routing and admission hold; no dry-run behavior is added. |

[Back to policy routing](../README.md) · [Back to validator documentation](../../README.md) · [Back to top](#top)
