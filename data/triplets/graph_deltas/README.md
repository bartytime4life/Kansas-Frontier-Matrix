<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/triplets/graph-deltas/readme
title: data/triplets/graph_deltas — Relationship Delta Hold Boundary
type: README; child-lane contract; implementation-status boundary
version: v1.0.0
status: repository-grounded; placeholder-only; no operational writer; no release; no publication
owners: NEEDS VERIFICATION — data, graph, evidence, policy, correction, and release stewards
updated: 2026-08-29
supersedes: Greenfield stub at the same path; no payload, lifecycle, correction, release, or publication state
policy_label: internal-by-default; correction-aware; release-gated; no-direct-public-path
current_path: data/triplets/graph_deltas/README.md
owning_root: data/
truth_posture: >
  CONFIRMED path, parent contract, three placeholder domain directories, and no
  committed delta payloads at the reviewed base / UNKNOWN writers, consumers,
  operation vocabulary, contract and schema binding, retention, and external
  storage / DENY correction, rollback, released, or public-feed interpretation
  from path or filename alone
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  prior_blob: c9ac561cf63e02d1100a3f516de3e6d0af405006
  method: complete target read; parent, data-root, lifecycle, published-lane, tree, and literal-reference inspection
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/triplets/graph_deltas/` — Relationship Delta Hold Boundary

This lane is reserved for rebuildable relationship-change candidates derived
at the CATALOG/TRIPLET stage. It is **not** a correction ledger, withdrawal
decision, release log, rollback plan, public change feed, or source of sovereign
truth.

> [!IMPORTANT]
> “Delta” describes a change between identified graph projections. It does not
> establish why the change is correct, authorize its application, or make the
> result released or public.

## Current implementation status

The reviewed tree contains this README and three domain placeholders. Each
domain directory contains only an empty `.gitkeep` file.

| Path | Committed payload state | Operational status |
|---|---|---|
| `atmosphere/` | No graph-delta payloads | Placeholder only |
| `flora/` | No graph-delta payloads | Placeholder only |
| `soil/` | No graph-delta payloads | Placeholder only |

At base `2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0`:

- no committed delta payload, manifest, index, or digest exists in this lane;
- repository code search returned no literal reference to
  `data/triplets/graph_deltas` or a `graph_delta` identifier;
- no writer, consumer, operation vocabulary, contract/schema binding,
  validator, retention rule, or application workflow was established by the
  inspected evidence.

Those observations prove only the reviewed repository state. Dynamically
constructed paths and external systems remain **UNKNOWN**.

## Authority and lifecycle boundary

[`data/triplets/`](../README.md) owns optional, rebuildable relationship and
graph projections. This child lane may hold candidate differences between two
identified projections when an implemented writer and validation contract are
established.

It does not own:

- canonical domain records or source payloads;
- decisions to correct, supersede, withdraw, release, publish, or roll back;
- contracts, schemas, policy, receipts, proofs, or release manifests;
- public-serving routes or authorization to mutate a graph consumer;
- factual truth merely because an edge is added, removed, or replaced.

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Generating or applying a delta does not perform the transition to `PUBLISHED`.

## Preconditions for a graph-delta payload

Do not treat this lane as an operational destination until the proposed payload
has an evidence-backed contract covering the applicable items below.

| Required boundary | Minimum evidence |
|---|---|
| Delta identity | Stable identity, version, media type, and content digest |
| Base and target | Base projection identity and digest, plus target identity and digest or a deterministic resulting-state digest |
| Operations | Defined add/remove/replace vocabulary, ordering, duplicate handling, and canonicalization |
| Derivation | Resolvable input identities, transformation version, and run receipt |
| Semantics | Contract/schema binding and governed relationship vocabulary |
| Evidence | Evidence or source references supporting each consequential relationship change |
| Scope | Spatial and temporal extent, CRS where applicable, and known limitations |
| Rights and sensitivity | Rights, attribution, privacy, sovereignty, harmful-precision, and access disposition |
| Validation | Replay or reconstruction checks, deterministic positive and negative cases, and declared coverage |
| Correction and release | Distinct correction, withdrawal, review, release, invalidation, and rollback references where applicable |

The operation names in this table are descriptive only; the repository does not
yet establish an accepted delta vocabulary. Missing or conflicted evidence must
narrow the delta, route it to a governed hold, or prevent creation. It must not
be replaced by generated prose or a plausible default.

## Validation and review

No lane-specific executable validator was verified. Until one exists, a review
of a proposed payload should at minimum confirm:

1. the base identity and digest match the projection to which the delta applies;
2. applying the payload deterministically produces the declared target state;
3. unsupported relationships are absent or explicitly withheld;
4. evidence, scope, rights, and sensitivity remain resolvable after the change;
5. sensitive joins and precise locations fail closed;
6. correction, withdrawal, release, cache invalidation, and rollback remain
   distinct decisions with resolvable evidence;
7. no public client or deployment reads or applies this internal lane directly.

A Markdown file, schema, fixture, test, workflow, pull request, merge, or passing
check is bounded evidence only. None independently establishes review approval,
correction acceptance, release, deployment, promotion, or publication.

## Maintenance guidance

- Preserve the three placeholder directories until a reviewed topology change
  explicitly adds, moves, or retires them.
- Add a domain payload only with its direct contract, validation, provenance,
  sensitivity, correction, and rollback dependencies.
- Update this inventory when the committed tree, writer, consumer, operation
  vocabulary, or authority boundary changes.
- Keep public-safe released carriers in
  [`data/published/`](../../published/README.md); do not expose this lane as a
  public change feed.

## Open verification register

| Question | Status |
|---|---|
| Accountable owner and independent reviewer route | `NEEDS VERIFICATION` |
| Delta format, operation vocabulary, and ordering rules | `UNKNOWN` |
| Writer, applier, and consumer identities | `UNKNOWN` |
| Contract, schema, fixtures, replay checks, and validator | `UNKNOWN` |
| Retention and external object-storage behavior | `UNKNOWN` |
| Correction propagation, invalidation, and rollback rehearsal | `UNKNOWN` |

## Related documentation

- [Triplet parent contract](../README.md)
- [Data-root contract](../../README.md)
- [Catalog projections](../../catalog/README.md)
- [Published public-safe carriers](../../published/README.md)
- [Receipts](../../receipts/README.md) and [proofs](../../proofs/README.md)
- [Release authority](../../../release/README.md)
- [Directory Rules](../../../docs/doctrine/directory-rules.md)
- [Lifecycle Law](../../../docs/doctrine/lifecycle-law.md)

[Back to top](#top)
