# ReleaseProofPackClosure

Status: **PROPOSED** · scope: deterministic completeness record for a candidate release proof pack.

Pass 9 identifies a complete release proof pack as a high-value verification milestone: manifest, receipts, catalog closure, review references, correction path, and rollback must be inspectable together. This contract defines a bounded closure record without making the candidate a release or publication.

## Invariants

- one release-manifest reference is required;
- receipt, proof, catalog, and review reference sets are non-empty, duplicate-free, and sorted;
- correction and rollback references are explicit;
- the record is limited to `CANDIDATE` or `HELD`; `PUBLISHED` is not accepted here;
- a `PASS` closure requires every required reference family and all authority flags false;
- this closure record proves only declared pack completeness, not the validity or authority of referenced objects;
- branch, commit, pull request, merge, schema validity, or closure `PASS` is never publication.

## Directory Rules basis

Accepted ADR-0029 places release semantics in `contracts/release/`, machine shape in `schemas/contracts/v1/release/`, synthetic examples in `fixtures/contracts/v1/release/`, deterministic validation in `tools/validators/release/`, tests in `tests/validators/`, CI in `.github/workflows/`, and source lineage in `docs/intake/exploratory/`.
