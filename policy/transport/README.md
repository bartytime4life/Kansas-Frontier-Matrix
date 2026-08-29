<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/transport/readme
title: Transport Policy Routing and Hold Boundary
type: readme
version: v1.1
status: provisional; routing-only; alias-unresolved; implementation-empty; evaluator-unbound; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy changes to @bartytime4life; transport policy stewardship, alias authority, evaluator ownership, independent review, and release authority are not established here
created: 2026-08-28
updated: 2026-08-28
current_path: policy/transport/README.md
owning_root: policy/
policy_label: public; policy; routing-boundary; hold; non-release; non-publication
responsibility: Prevent the direct policy/transport marker lane from being mistaken for an accepted alias, active policy bundle, evaluator entrypoint, transport authority, release gate, or publication surface, and route current contributors to repository-backed Roads/Rail/Trade policy evidence.
base_commit: 332a371f0be1aae68690853fba368a6289d2dab4
prior_blob: 5cd811259e322619b6f151b1f0e41d73571a49e4
directory_governance: ADR-0029 accepted Directory Rules v2; the machine domain-lane register is a PROPOSED projection and records transport as an unresolved alias for roads-rail-trade
truth_posture: CONFIRMED this directory contains only .gitkeep and this README, no Rego source, test, evaluator, workflow, consumer, receipt, bundle, release artifact, or publication behavior, and the current domain-specific policy source is under policy/domains/roads-rail-trade/ as 16 unbound scaffolds / PROPOSED this routing-and-hold boundary / CONFLICTED or unresolved transport-to-roads-rail-trade alias and compatibility posture / UNKNOWN future writer, reader, retention, migration, evaluator, consumer, decision-receipt, release, and publication bindings
[/KFM_META_BLOCK_V2] -->

# Transport policy routing and hold boundary

<a id="top"></a>

> **One-line purpose.** `policy/transport/` is a documented hold around an
> otherwise empty direct policy lane. It is not an accepted alias, policy bundle,
> evaluator entrypoint, transport fact source, release gate, or public interface.

| Current question | Repository-backed answer |
|---|---|
| Does this directory contain executable policy? | **No.** It contains only `.gitkeep` and this README. |
| Is `transport` an accepted writable alias for `roads-rail-trade`? | **No.** The proposed machine register records that mapping under `unresolved_aliases`. |
| Where is current domain-specific policy source? | [`policy/domains/roads-rail-trade/`](../domains/roads-rail-trade/README.md), where 16 direct Rego files remain unbound scaffolds. |
| Does that domain lane establish live transport decisions? | **No.** It has no accepted bundle, evaluator, native rule-test profile, authenticated decision flow, consumer, release, or publication authority. |

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-current-state) ·
[Routing](#authority-routing) · [Hold](#hold-contract) · [Inputs and outputs](#inputs-and-outputs) ·
[Safety](#rights-sensitivity-and-operational-safety) · [Validation](#validation) ·
[Maintenance](#maintenance-correction-and-rollback) · [Open questions](#open-questions) ·
[Related](#related-repository-surfaces)

## Purpose

This README closes a documentation gap without filling an implementation gap.
It gives maintainers an evidence-backed answer when they encounter the tracked
`policy/transport/` path:

- do not add policy source here merely because an external plan, legacy name, or
  nearby package uses the word `transport`;
- route Roads/Rail/Trade admissibility work to the currently documented domain
  policy lane;
- preserve the unresolved alias conflict until an accepted decision settles
  canonical naming, compatibility, migration, writers, and readers; and
- keep policy evaluation, review, release, deployment, and publication as
  separate states.

This document does not choose the future disposition of the directory. Deletion,
migration, alias acceptance, or a new responsibility would require the applicable
Directory Rules review and, when authority or canonical placement changes, an
accepted decision.

## Authority and current state

The repository at `main@332a371f0be1aae68690853fba368a6289d2dab4`
provides the controlling evidence for this boundary.

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| [Canonical policy root](../README.md) | `policy/` is the adopted policy-source responsibility root; direct children may have mixed maturity. | Every child is active, accepted, or equivalent. |
| [Accepted Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Responsibility-first placement and governed path changes. | Acceptance of the `transport` alias. |
| [Domain-lane register](../../control_plane/domain_lane_register.yaml) | A PROPOSED machine projection records `transport: roads-rail-trade` under `unresolved_aliases`. | Canonical identity, writable compatibility, migration approval, or policy activation. |
| [Roads/Rail/Trade policy boundary](../domains/roads-rail-trade/README.md) | The current domain-specific location contains 16 direct Rego scaffolds and documents its evaluator, proof, release, and publication holds. | Operative transport rules or a general evaluator. |
| This directory | `.gitkeep` and this README are tracked. | A package, entrypoint, schema, fixture, test, validator, workflow, bundle, decision, receipt, or consumer. |

The historical Google Drive architecture plan and Notion Transport Corridor
Evidence Lane reviewed for this revision are proposal lineage only. Both leave
repository implementation or placement unresolved. Their candidate paths and
language do not override current GitHub evidence, accepted doctrine, or an
accepted ADR.

## Authority routing

Use the narrowest current repository surface for the responsibility at hand.

| Responsibility | Current repository surface | Boundary |
|---|---|---|
| Policy-root placement and maturity | [`policy/README.md`](../README.md) | Root contract; not an evaluator. |
| Roads/Rail/Trade admissibility source | [`policy/domains/roads-rail-trade/`](../domains/roads-rail-trade/README.md) | Current domain lane; source remains scaffolded and unbound. |
| Human domain documentation | [`docs/domains/roads-rail-trade/`](../../docs/domains/roads-rail-trade/README.md) | Prose and domain context; not executable policy or sovereign truth. |
| Semantic contracts | [`contracts/domains/roads-rail-trade/`](../../contracts/domains/roads-rail-trade/README.md) | Meaning; not policy decisions. |
| Machine shapes | [`schemas/contracts/v1/domains/roads-rail-trade/`](../../schemas/contracts/v1/domains/roads-rail-trade/README.md) | Structure; schema validity is not admissibility. |
| Domain code | [`packages/domains/roads-rail-trade/`](../../packages/domains/roads-rail-trade/README.md) | Domain implementation boundary; not a policy authority. |
| Legacy or compatibility package marker | [`packages/domains/transport/`](../../packages/domains/transport/README.md) | Package-local boundary; it cannot accept this policy alias. |
| Bounded domain validation | [`tools/validators/domains/roads-rail-trade/`](../../tools/validators/domains/roads-rail-trade/README.md) | Synthetic contract validation; not Rego execution or transport truth. |
| Transport-facility topology proposal | [`tools/validators/transport-facility-topology/`](../../tools/validators/transport-facility-topology/README.md) | Separate validator boundary; it does not activate this directory. |
| General policy evaluation | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | Placeholder runtime boundary; no accepted general evaluator is established. |

Similar names are not enough to transfer authority. A contract, schema, package,
validator, map, test, index, generated answer, or proposed register cannot make
`policy/transport/` an accepted policy home.

## Hold contract

Until an accepted decision and implementation establish otherwise:

1. Do not place Rego, bundle manifests, evaluator configuration, decisions, or
   receipts in this directory.
2. Do not duplicate files from `policy/domains/roads-rail-trade/`.
3. Do not make `policy/transport/` a symlink, compatibility import, selector,
   or fallback path.
4. Do not interpret the unresolved machine-register alias as permission to write,
   evaluate, migrate, release, deploy, or publish.
5. When a required path or authority is unresolved, mark the operation held,
   conflicted, or needs verification rather than inventing compatibility.

A future change may supersede this hold only when it names the responsibility,
canonical path, compatibility duration, writers, readers, evaluator profile,
tests, receipts, migration and rollback plan, and independent review path.

## Inputs and outputs

This documentation boundary consumes repository evidence only:

- accepted placement doctrine and ADR status;
- the tracked tree for this directory;
- the proposed alias register, with its non-authoritative status preserved;
- the current Roads/Rail/Trade policy inventory and maturity claims; and
- directly related contract, schema, package, validator, runtime, and domain
  documentation.

Its output is contributor routing and an explicit hold. It emits no policy
decision, permit, denial, obligation, transport status, safety instruction,
evidence bundle, proof, release approval, deployment state, or public artifact.

## Rights, sensitivity, and operational safety

Transport material can touch current conditions, legal access, critical
facilities, Indigenous or historic corridors, private property, and precise
locations. This empty lane supplies no rules for those cases.

- Do not present KFM prose, maps, schemas, validators, or generated language as
  live closure, detour, safe-passage, legal-access, rail-status, bridge-condition,
  emergency, or regulatory authority.
- Preserve source rights, provenance, effective time, correction state, purpose,
  audience, sensitivity, sovereignty, and harmful-precision limits at their
  governing surfaces.
- Public clients must use governed interfaces or released public-safe artifacts,
  not policy source, canonical internal stores, or this routing document.
- If required evidence or policy authority is absent, narrow, generalize, hold,
  or abstain. A plausible route narrative is not evidence.

## Validation

Focused documentation checks:

```bash
python tools/validators/docs/link-check/check_links.py \
  policy/transport/README.md policy/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required policy/transport/README.md policy/README.md
```

The link checker covers repository-local files, directories, images, and
fragments. The metadata checker covers the bounded metadata envelope. Passing
either command confirms only its exercised documentation QA scope at this
revision.

Reviewers should also verify that this directory contains only `.gitkeep` and
this README, the current parent inventory records 40 substantive direct-child
READMEs, zero one-byte direct-child placeholders, and no missing direct README;
every relative target resolves, and the base-to-head diff changes Markdown only.

These checks prove documentation structure and link integrity. They do not parse
or execute Rego, accept an alias, establish policy semantics, prove transport
facts, authenticate a decision, bind a consumer, approve release, deploy, or
publish.

## Maintenance, correction, and rollback

Recheck this README when any of the following changes:

- the domain-lane register or its authority status;
- accepted directory doctrine or ADR status;
- the `policy/domains/roads-rail-trade/` inventory or evaluator binding;
- a transport compatibility path, migration, bundle, consumer, or receipt;
- the direct contents of this directory; or
- public-surface, rights, sensitivity, correction, or release obligations.

If a claim is wrong, narrow or correct it visibly and follow downstream effects.
For this documentation-only change, rollback means reverting the focused commits
or closing the unmerged draft PR. Reverting must not remove or alter the
Roads/Rail/Trade Rego scaffolds, machine register, contracts, schemas, packages,
validators, release artifacts, deployments, or published state.

## Open questions

| ID | Question | Current status |
|---|---|---|
| TRANSPORT-POL-001 | What accepted decision resolves `transport` versus `roads-rail-trade` for policy placement? | **UNKNOWN / NEEDS ADR** |
| TRANSPORT-POL-002 | Should this direct directory be removed, retained as a permanent hold, or become time-bounded compatibility? | **NEEDS VERIFICATION** |
| TRANSPORT-POL-003 | If compatibility is accepted, who writes and reads it, for how long, and how is divergence prevented? | **UNKNOWN** |
| TRANSPORT-POL-004 | What accepted bundle, evaluator, input profile, consumer, decision receipt, and rollback contract would make policy executable? | **UNKNOWN** |
| TRANSPORT-POL-005 | Which independent policy, domain, rights, sensitivity, sovereignty, security, and release reviews are required? | **NEEDS VERIFICATION** |

## Related repository surfaces

- [Canonical policy root](../README.md)
- [Roads/Rail/Trade policy boundary](../domains/roads-rail-trade/README.md)
- [Roads/Rail/Trade placement backlog](../../docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md)
- [Human domain-lane register](../../docs/registers/DOMAIN_LANE.md)
- [Machine domain-lane projection](../../control_plane/domain_lane_register.yaml)
- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [ADR index](../../docs/adr/README.md)

[Back to top](#top)

## Changelog

| Version | Date | Change | Runtime effect |
|---|---|---|---|
| v1.1 | 2026-08-28 | Removed a nonexistent fragment-checker command, documented the supported link checker's fragment scope, and reconciled the parent policy inventory. | None; documentation only. |
| v1.0 | 2026-08-28 | Replaced the one-byte placeholder with a repository-grounded routing-and-hold boundary; preserved the unresolved alias and routed current policy work to the documented Roads/Rail/Trade lane. | None; documentation only. |
