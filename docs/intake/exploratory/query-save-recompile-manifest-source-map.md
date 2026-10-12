# Query-save-recompile: RecompileManifest source adaptation

**Status:** PROPOSED source adaptation / implemented as an inactive fixture profile in the accompanying repository slice.

## Source pressure

The supplied *Kansas Frontier Matrix Pipeline Living Implementation Manual v0.3* proposes a governed incremental loop:

```text
query -> save -> validate -> compile -> review -> promote -> recompile
```

It names `QueryRunRecord`, `CandidateDelta`, and `RecompileManifest`, requires deterministic hashes and rollback references, and denies direct loop output to `PUBLISHED`.

## Repository assay

Current repository evidence before this slice contained:

- fixture-only `QueryRunRecord` validation;
- fixture-only deterministic `AIChangeProposal` compare-and-set candidates;
- shared RFC 8785 JCS + SHA-256 hashing;
- a documented `tools/generators/` responsibility lane.

Repository search did not identify an implemented `RecompileManifest` family. The existing query contract explicitly deferred it as a separate boundary because output identity, destination restrictions, compiler identity, and rollback require independent review.

## Adaptation decision

This slice does not add a generic autonomous compiler. It implements the smallest safe bridge:

- one JSON object profile;
- one explicit `WORK` destination class;
- exact `QueryRunRecord` and `AIChangeProposal` validation;
- in-memory compare-and-set application;
- canonical output bytes;
- deterministic compiler, output, manifest, and rollback bindings;
- stdout-only output with no file-write API;
- replay validation and negative fixtures.

`AIChangeProposal` remains the candidate-change authority. No parallel `CandidateDelta` contract is introduced.

## Deferred work

A later executor would require authenticated review and policy state, owning-root destination rules, concurrency/conflict handling, write authorization, receipts, correction behavior, rollback execution, and separate promotion/release review. Documentation, catalog, layer-manifest, proof-pack, and other artifact compilers remain outside this JSON-only v1 profile.
