<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-sources-readme
title: policy/sources/ — Parallel Source-Policy Hold Boundary
type: readme
version: v0.1.0
status: draft
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: internal
owning_root: policy/
responsibility: "Route the observed plural source-policy lane and hold authority-bearing additions until its relationship to policy/source and policy/rights is decided."
truth_posture: "CONFIRMED current tree and scaffold bytes / HOLD path ownership and rule activation / NEEDS VERIFICATION steward, generator, evaluator, tests, consumers, correction, and migration"
related:
  - policy/README.md
  - policy/source/README.md
  - policy/rights/README.md
  - policy/sources/rights/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/sources/` — Parallel Source-Policy Hold Boundary

`policy/sources/` is an observed plural-name policy lane containing one
source-scoped rights child. This README documents and routes the existing bytes;
it does not make the plural lane canonical, create a compatibility relationship,
activate policy, clear source rights, admit a source, or approve publication.

> [!CAUTION]
> `policy/source/` and `policy/sources/` are both tracked. Current repository
> evidence does not establish two accepted writable authorities or an accepted
> migration between them. Authority-bearing additions remain **HOLD** until a
> reviewed path decision identifies writers, consumers, canonical identity,
> compatibility needs, migration steps, and rollback.

## Purpose and audience

Use this guide to determine whether existing material belongs to the plural
parent, its `rights/` leaf, the singular source-admission lane, or the general
rights-policy lane. It is for policy authors, source stewards, reviewers, and
maintainers investigating the current naming drift.

## Current authority map

| Surface | Current responsibility | Boundary |
|---|---|---|
| [`policy/`](../README.md) | Adopted root for normative policy source | Parent authority; not an evaluator or release authority |
| [`policy/source/`](../source/README.md) | Existing source-admission and doctrine-prerequisite candidate rules | Substantive boundary; does not establish its child name as canonical |
| `policy/sources/` | Routing and path-ownership hold | This guide does not authorize new rule families here |
| [`policy/sources/rights/`](rights/README.md) | Two source-specific rights-policy scaffolds | Leaf inventory only; path ownership and activation remain held |
| [`policy/rights/`](../rights/README.md) | General rights-admissibility policy boundary | Does not supply provider-specific rights facts or source admission |

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the adopted [Directory Rules](../../docs/doctrine/directory-rules.md) place
policy source beneath `policy/`. They do not decide the singular-versus-plural
child taxonomy.

## Current inventory and maturity

```text
policy/sources/
├── README.md
└── rights/
    ├── README.md
    ├── mesonet.rego
    └── nasa.rego
```

| Artifact | Confirmed state | Safe interpretation |
|---|---|---|
| [`rights/mesonet.rego`](rights/mesonet.rego) | Package `kfm.generated.policy.sources.rights.mesonet`; `PROPOSED scaffold`; `default allow := false` | No accepted rights semantics, evaluation, or Mesonet permission |
| [`rights/nasa.rego`](rights/nasa.rego) | Package `kfm.generated.policy.sources.rights.nasa`; `PROPOSED scaffold`; `default allow := false` | No accepted rights semantics, evaluation, or NASA permission |
| Native tests | No local `*_test.rego`, fixture family, or test directory | Behavioral coverage is not established |
| Bundle, evaluator, and consumer | No accepted relationship established by current repository evidence | Runtime enforcement is unknown |
| Agriculture verification backlog | Names these files as proposed artifacts that could help settle product-terms work | A backlog item is not implementation, adoption, source admission, or rights clearance |

The package prefix includes `generated`, but no generator, canonical input,
reproducible command, or derived-file rule is established. Do not hand-edit or
regenerate by assumption; first resolve the source relationship.

## What belongs here now

While path ownership remains held, changes should be limited to:

- correcting documentation about the observed files and their limitations;
- inventorying existing writers, consumers, references, tests, and provenance;
- recording an accepted path decision, migration plan, compatibility mapping,
  or retirement evidence; and
- preserving the two existing scaffolds without treating them as active rules.

## What does not belong here

| Do not place or claim here | Owning surface or required action |
|---|---|
| New source-admission rules added to escape the singular lane | Resolve [`policy/source/`](../source/README.md) versus this path first |
| General rights semantics | Contracts and [`policy/rights/`](../rights/README.md) |
| Source identities, descriptors, registry records, or activation state | Governed source contracts and `data/registry/sources/` |
| License text, provider terms, credentials, or restricted evidence | Authorized source-of-record and governed evidence systems |
| Evaluated decisions, receipts, proofs, or lifecycle data | Their accepted accountability and data lanes |
| Evaluator, connector, API, worker, cache, or storage implementation | `packages/`, `connectors/`, `apps/`, `runtime/`, or `tools/` by responsibility |
| Release, correction, withdrawal, or rollback decisions | `release/` |

Provider names, reachable endpoints, source availability, a default-false rule,
or passing repository checks do not establish rights, authority,
admission, release, or public-safe use.

## Validation and failure interpretation

The broad `policy-test` workflow inventories Rego while preserving the general
OPA-readiness hold. It does not parse or execute these packages. The separate
source-rights currentness assessment exercises synthetic declared-currentness
cases; it is not an evaluator for these files and does not grant rights.

There is no honest repository-native OPA command for this lane. Missing inputs,
undefined results, evaluator errors, stale terms, unresolved rights, or unknown
path ownership must not be normalized into permission. Hold or deny the
dependent operation through its governed boundary.

## Maintenance, correction, and rollback

Revisit this README when a writer or consumer changes, a path decision is
accepted, a generator is identified, or a rule gains contracts, tests, bundle
membership, an evaluator, a governed consumer, correction propagation, or
rollback evidence.

For a documentation defect, revert or forward-fix the Markdown commit. That
does not remove the two Rego files or change any external rights state. A future
path rollback must not recreate two writable source-policy authorities.

## Open verification

| ID | Open item | Posture |
|---|---|---|
| `POL-SOURCES-001` | Canonical relationship among `policy/source/`, this parent, `rights/`, and `policy/rights/` | **HOLD — accepted path decision required** |
| `POL-SOURCES-002` | Current writers, consumers, stable IDs, and compatibility requirements | **NEEDS VERIFICATION** |
| `POL-SOURCES-003` | Generator implied by the package prefix | **UNKNOWN** |
| `POL-SOURCES-004` | Accepted inputs, outcomes, tests, bundle, evaluator, consumer, and correction flow | **NOT ESTABLISHED** |
| `POL-SOURCES-005` | Source-rights steward and independent review route | **NEEDS VERIFICATION** |

[Back to `policy/`](../README.md) · [Back to top](#top)
