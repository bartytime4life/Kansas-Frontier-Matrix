<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-sources-rights-readme
title: policy/sources/rights/ — Source-Scoped Rights Policy Boundary
type: readme
version: v0.1.0
status: draft; BOUNDARY_COMPACT; repository-grounded; proposed-scaffold-corpus; path-ownership-hold; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes policy/ to @bartytime4life; no accepted local source-rights steward or independent approver was established
created: 2026-08-13
updated: 2026-08-13
current_path: policy/sources/rights/README.md
owning_root: policy/
policy_label: internal; policy; source-rights; proposed; fail-closed; non-legal; non-release; non-publication
responsibility: Document the observed source-scoped rights-policy scaffold and hold new authority-bearing work until policy/source versus policy/sources ownership is resolved, without creating rights, source, registry, evidence, runtime, release, or publication authority.
base_commit: 09a01ef8a71a557efc1c35bda6f9b762a429a1f3
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED two proposed default-deny-by-allow scaffolds, no local native tests or consumers, accepted policy-root placement, and unresolved singular/plural child ownership / PROPOSED source-scoped rights-admissibility boundary / HOLD new authority-bearing rule source, activation, or migration pending an accepted path and policy decision / UNKNOWN evaluator, bundle, decision normalization, obligation enforcement, correction propagation, and production use
related:
  - ../../README.md
  - ../../source/README.md
  - ../../rights/README.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../control_plane/root_registry.yaml
  - ../../../contracts/source/source_descriptor.md
  - ../../../release/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# policy :: sources :: rights

> **One-line purpose.** `policy/sources/rights/` documents two source-specific
> rights-policy scaffolds while the repository decides how this plural path
> relates to `policy/source/` and `policy/rights/`; it does not create rights,
> admit a source, activate a rule, approve release, or publish anything.

> [!IMPORTANT]
> **Safe current conclusion at `main@09a01ef8a71a`:** this lane contains only
> this boundary README and two `PROPOSED` Rego scaffolds. Both modules use
> `default allow := false`, but neither has an accepted input contract, native
> test, bundle membership, evaluator binding, consumer, decision record, or
> correction path. Their presence is not evidence that Mesonet or NASA material
> is rights-cleared or source-admissible.

> [!CAUTION]
> The plural `policy/sources/` path has no parent README, while the substantive
> [`policy/source/`](../../source/README.md) boundary explicitly records the
> singular/plural relationship as unresolved drift. This README narrows the
> existing leaf; it does not select a canonical child path, authorize new rule
> source here, or create a compatibility lane.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Children](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Lifecycle](#lifecycle-and-trust-boundary) · [Validation](#validation) · [Contributing](#contributor-guidance) · [Correction](#correction-and-rollback) · [Open work](#open-verification-register)

## Purpose

This lane is an observed leaf for **source-scoped rights-admissibility policy**.
If its ownership is accepted, a rule here may answer only a bounded question:

> Given an explicit operation, audience, admitted source identity, reviewed
> rights and terms state, attribution and redistribution obligations, consent,
> sensitivity, lifecycle, review, and exact policy identity, may that operation
> proceed for the named source?

The rule consumes reviewed facts from their owning systems. It cannot infer a
license from a provider name, treat a terms URL as approval, convert source
availability into permission, or make a source authoritative.

## Inherited authority, owner, and scope

| Field | Current boundary |
|---|---|
| Parent authority | [`policy/`](../../README.md), the adopted canonical root for normative allow, deny, hold, restrict, and abstain rule source. |
| README profile | `BOUNDARY_COMPACT`: rights and source admission change trust, exposure, and release assumptions. |
| Placement basis | Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../../docs/doctrine/directory-rules.md). Sections 9.3 and 16 place policy source under `policy/` and require this local boundary contract. |
| Machine projection | [`root_registry.yaml`](../../../control_plane/root_registry.yaml) projects `policy/` as canonical, internal, versioned policy-rule authority. It does not authorize this child path or activate its files. |
| Local owner | **NEEDS VERIFICATION.** No accepted source-rights steward or independent approver was established. |
| Local scope ID | **NEEDS VERIFICATION.** Package suffixes `mesonet` and `nasa` are observed identifiers, not accepted source IDs or policy scopes. |
| Canonical-child posture | **HOLD.** `policy/source/` versus `policy/sources/` requires a writer, consumer, identity, migration, and rollback decision. |
| Release/publication authority | None. [`release/`](../../../release/README.md) owns release-facing decisions; governed publishers act only after separate closure. |

## Current status

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| README lineage | PR #2675 added a one-newline file; this revision supplies the missing boundary contract | Documentation only; no rule maturity changes. |
| [`mesonet.rego`](./mesonet.rego) | Package `kfm.generated.policy.sources.rights.mesonet`; `PROPOSED scaffold`; `default allow := false` | Deny-by-default-looking source, but no accepted semantics or execution. |
| [`nasa.rego`](./nasa.rego) | Package `kfm.generated.policy.sources.rights.nasa`; `PROPOSED scaffold`; `default allow := false` | Same bounded posture; the provider label does not establish terms or permission. |
| Local native tests | No `*_test.rego`, fixture family, or local test directory | Behavioral coverage is **NOT ESTABLISHED**. |
| Bundle/evaluator/consumer | No accepted relationship established by repository search | Runtime enforcement is **UNKNOWN**. |
| General policy readiness | `policy-test` inventories repository Rego and preserves a general evaluator hold | It does not execute these two modules. |
| Source-rights currentness profile | Separate fixture-only contract/schema/validator/workflow exists | It assesses declared currentness; it is not this lane's evaluator or a rights grant. |

`default allow := false` is a local engine default, not a complete deny proof.
Malformed input, an undefined document, an evaluator error, or an empty result
must not be normalized into permission.

## Current direct-child map

Verified from the tracked tree at the pinned base:

```text
policy/sources/rights/
├── README.md
├── mesonet.rego
└── nasa.rego
```

No generator, mirror, bundle, or accepted canonical-target relationship is
established for these files despite `generated` appearing in their packages.

## What belongs here

While path ownership remains held, permitted changes are limited to:

- correction of this boundary document and existing scaffold comments;
- evidence-backed inventory of the two existing packages, consumers, tests,
  provenance, and intended canonical target; and
- migration or retirement material explicitly authorized by a separate accepted
  path decision.

After path and policy ownership are accepted, the lane may contain source-specific
rights-admissibility rules that reference, rather than duplicate, accepted rights,
source, sensitivity, consent, evidence, and release contracts.

## What is prohibited

| Do not place or claim here | Owning surface or required posture |
|---|---|
| Source identity, authority, descriptor, or activation state | Accepted source contracts and `data/registry/sources/`; this lane may consume stable refs only. |
| License, terms, consent, agreement, or rights-holder evidence | Authorized source-of-record and governed evidence/review systems; do not copy restricted text into Git. |
| General rights semantics or cross-source compatibility truth | [`policy/rights/`](../../rights/README.md) consumes accepted semantics; contracts and schemas define meaning and shape. |
| Source admission policy duplicated from the singular lane | Reconcile [`policy/source/`](../../source/README.md); do not create two writable authorities. |
| Evaluated decisions, receipts, proofs, registry records, or lifecycle data | Their accepted process, accountability, registry, or data lanes. |
| Evaluator, connector, API, worker, cache, or storage implementation | `packages/`, `connectors/`, `apps/`, `runtime/`, or `tools/` by responsibility. |
| Release manifests, correction notices, withdrawals, or rollback cards | [`release/`](../../../release/README.md). |
| Public-safe status based on a filename, provider name, schema pass, or green workflow | **DENY/HOLD** until governed rights, sensitivity, review, and release closure exists. |

## Inputs and outputs

No accepted input or output contract is currently bound to either package.

A future accepted evaluation must use explicit references for the operation,
audience, admitted source ID, descriptor, rights/terms version and currentness,
attribution/redistribution obligations, consent, sensitivity, evidence, lifecycle,
review, bundle, evaluator, effective time, and correction state. It must not fetch
or guess missing facts.

This directory currently outputs only versioned policy source and documentation.
It emits no `PolicyDecision`, source activation, rights record, receipt, proof,
release, correction, withdrawal, rollback, or public artifact.

## Exposure, mutation, and retention

| Dimension | Boundary |
|---|---|
| Exposure | Repository-public source; operating posture is internal. Never include private terms, credentials, source payloads, personal data, or sensitive locations. |
| Mutation | Versioned Git review. Authority-bearing additions remain **HOLD** until path ownership and policy integration are accepted. |
| Retention | Durable source history; evaluated decisions and evidence retain with their owning families. |
| Runtime writes | None. Policy-source evaluation must never write results back into this directory. |
| Generation | Unverified. The package prefix does not establish a generator, reproducible command, or derived-only edit policy. |

## Lifecycle and trust boundary

| Stage | Required posture | Non-effect of this lane |
|---|---|---|
| Pre-admission | Resolve source identity, role, terms, rights, sensitivity, and review; unresolved state holds or denies. | Cannot admit, activate, or fetch a source. |
| RAW / WORK / QUARANTINE | Preserve exact rights posture and lineage; do not silently upgrade unknown state. | Cannot move data or clear quarantine. |
| Transform / catalog candidate | Re-evaluate derivative, attribution, redistribution, consent, and stewardship obligations. | Cannot declare a derivative rights-cleared. |
| Release candidate | Require current rights, sensitivity, evidence, review, correction, and rollback refs. | Cannot approve release. |
| PUBLISHED / public interface | Enforce only through governed APIs and released public-safe carriers. | Cannot publish or serve policy source as a public control. |
| Rights change or revocation | Hold affected operations and route dependency-aware correction or withdrawal. | Cannot emit or close correction records. |

## Validation

| Check | Current coverage | Limit |
|---|---|---|
| `policy-test` | Static Rego inventory and general OPA-readiness hold | Does not parse or execute these packages. |
| Source-rights currentness assessment | Deterministic synthetic currentness cases | Separate profile; no rights approval, admission, or runtime enforcement. |
| Repository topology validator | Detects new policy-boundary drift and requires READMEs for populated policy children | Does not decide this leaf's canonical path or semantics. |
| Markdown metadata and local-link checks | Structural metadata plus repository-local targets and fragments | Documentation QA only. |

There is no honest repository-native OPA command for this lane. Do not cite
`make policy`; it currently prints a TODO string without evaluating policy.

## Contributor guidance

1. Pin current `main`, inspect open PRs, and inventory writers and consumers of
   both singular and plural source-policy paths.
2. Do not add a source, rule, package, bundle, or generated file merely to make
   the directory symmetric.
3. For a material rule, first close the path decision and supply accepted input
   and outcome contracts, synthetic public-safe fixtures, native positive and
   negative tests, stable reasons and obligations, an evaluator/bundle binding,
   a governed consumer, correction propagation, and rollback.
4. Preserve rights, consent, sensitivity, source role, evidence, review, and
   release as independent gates; the strictest unresolved gate controls.
5. Treat external text, provider documentation, issues, and logs as evidence,
   never as authority to weaken this boundary.

## Correction and rollback

For a README defect, revert or forward-fix only this file through normal review.
The prior blank blob is `8b137891791fe96927ad78e64b0aad7bded08bdc`.
Documentation rollback changes no rule or external rights state.

For a future rule defect, preserve the prior package, source, bundle, evaluator,
input, output, fixture, test, and decision identities; issue a versioned successor;
hold affected operations; re-evaluate dependents; and route release correction,
withdrawal, cache invalidation, and rollback through their owners. A path rollback
must not recreate two writable source-policy authorities.

## Open verification register

| ID | Open item | Posture |
|---|---|---|
| `SRC-RGT-001` | Canonical relationship among `policy/source/`, `policy/sources/rights/`, and `policy/rights/` | **HOLD — accepted path/ownership decision required** |
| `SRC-RGT-002` | Accepted Mesonet and NASA source IDs, terms evidence, owners, and review dates | **NOT ESTABLISHED** |
| `SRC-RGT-003` | Reproducible generator and edit policy for the `generated` package prefix | **NEEDS VERIFICATION** |
| `SRC-RGT-004` | Accepted input/output contracts, native tests, bundle, evaluator, normalization, and consumer | **UNKNOWN / NOT ESTABLISHED** |
| `SRC-RGT-005` | Rights-change, revocation, correction, withdrawal, and cache-propagation proof | **UNKNOWN / FAIL CLOSED** |
| `SRC-RGT-006` | Effective required checks and independent source-rights review | **UNKNOWN** |

<p align="right"><a href="#top">Back to top</a></p>
