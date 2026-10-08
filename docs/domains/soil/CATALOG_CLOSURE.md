<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/catalog-closure
title: Soil catalog closure review
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil catalog closure review; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/README.md
  - contracts/domains/soil/catalog_closure_assessment.md
  - tools/validators/domains/soil/validate_catalog_closure_assessment.py
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Soil catalog closure

Use this guide to prepare one Soil candidate for catalog review. At the pinned
repository snapshot, `release/candidates/soil/` and `data/proofs/soil/` contain
README material only. No completed Soil catalog or proof-bearing release is
established by those lanes.

## Current bounded implementation

The [assessment contract](../../../contracts/domains/soil/catalog_closure_assessment.md)
and [validator](../../../tools/validators/domains/soil/validate_catalog_closure_assessment.py)
implement a deterministic, fixture-only declaration check. The validator does
not dereference or authenticate the supplied references. A reviewer must inspect
the actual supporting artifacts independently.

## Closure dimensions

| Required dimension | What the reviewer must establish outside the fixture assessment |
|---|---|
| Semantic contract | Exact object family and meaning apply to this candidate |
| Schema | Versioned shape and validator agree; negative cases are rejected |
| Source descriptor | Source identity, product, edition and support role match |
| Support-type profile | Survey, grid, station, profile and interpretation remain distinct |
| Deterministic identity | Digest and native-key lineage bind this candidate |
| EvidenceBundle | References resolve to the claimed evidence under permitted access |
| Validation report | Exact candidate and validator version are identified |
| Rights decision | Intended access, reuse and attribution are reviewed |
| Sensitivity decision | Precision and downstream joins are reviewed |
| Correction target | A later correction can reach affected dependents |
| Rollback target | A verified prior state or explicit empty state is available |

The machine profile requires the eleven dimensions in its declared order. Each
has `SATISFIED`, `UNRESOLVED`, or `DENIED` state. A `SATISFIED` reference is only
a declaration at this layer; its existence does not prove the underlying claim.

## Review workflow

1. Pin the repository commit, candidate identity and content digest.
2. Compare the candidate to the exact contract, schema and support-type profile.
3. Inventory every required reference and test access through its owning surface.
   Missing evidence stays `UNRESOLVED`; a failed decision stays `DENIED`.
4. Run the bounded fixture checks below before evaluating a changed profile.
5. Record the assessment outcome and independent evidence-review findings as
   separate results. Route unresolved source, rights, sensitivity or rollback
   questions to the appropriate steward role; those assignments remain unbound.
6. Request the separately governed catalog transition only after its requirements
   are established. This document creates no catalog entry or review approval.

## Validation and result interpretation

```bash
python tools/validators/domains/soil/validate_catalog_closure_assessment.py --fixtures
python -m unittest tests.validators.domains.soil.test_soil_cli_fail_closed
```

`READY_FOR_REVIEW` means all eleven declarations are satisfied. `HOLD` means a
valid declaration has unresolved or denied dimensions. `ERROR` means malformed,
contradictory or over-authoritative input. The single-file CLI can exit zero for
`HOLD`; read the emitted outcome, not only the exit status. Fixture mode checks
that each case has its expected outcome.

## Troubleshooting and completion

For `ERROR`, check dimension order, count, reference/state consistency, immutable
assessment identity and all-false effect flags. Do not replace unknown evidence
with a dummy reference to obtain `READY_FOR_REVIEW`. A useful review packet ends
with a dimension-by-dimension evidence record, residual gaps and next owner.
Catalog writes, promotion, release, deployment, publication and public use remain
separate decisions. See [definition of done](DEFINITION_OF_DONE.md).

## Release and candidate navigation

`RELEASE_INDEX.md` retains the exact marker text required by the Soil release-readiness workflow. This companion section supplies substantive release guidance while preserving the explicit no-release-producer hold.

This is the human navigation index for Soil release review. It is not a release
registry or an approval. At `ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`, the
Soil-specific candidate and proof lanes contain README files only. No completed
Soil-domain release is registered by this document.

### Current surfaces

| Surface | What is present | What remains separate |
|---|---|---|
| [Candidate lane](../../../release/candidates/soil/README.md) | Candidate boundary documentation | Candidate manifest, review and release decision |
| [Proof lane](../../../data/proofs/soil/README.md) | Domain proof navigation | Emitted proof, authenticated evidence and closure |
| [Domain workflow](../../../.github/workflows/domain-soil.yml) | Bounded fixture tests and explicit proof/release holds | Executable production release path |
| [Catalog review](CATALOG_CLOSURE.md) | Fixture-only declaration assessment | Actual resolution and catalog transition |
| [Site visual context](MAP_UI_CONTRACTS.md) | Soil-related application source and tests | Governed Soil release and hosted acceptance |

A related Agriculture manifest exists at
[`agri-soil-crop-suitability-v1-001.json`](../../../release/manifests/agri-soil-crop-suitability-v1-001.json).
It is a separate lane's artifact. Its filename or presence is not evidence that
the Soil lane has completed its own admission, proof or release requirements.
Review that manifest and its owning controls before relying on its meaning.

### Information required for a future entry

Add an index row only after inspecting the actual owning artifacts. The row
should link to, rather than duplicate, these records:

- product/candidate identity, support type, source edition and content digest;
- intended audience, geography, time coverage, units and depth support;
- source admission, rights and sensitivity results;
- EvidenceBundle and validation report bound to the exact bytes;
- policy and independent review results;
- release decision and manifest, if they actually exist;
- public carrier or governed route and readback status;
- correction/withdrawal reference and rollback target;
- exact repository revision and separately observed deployment identity.

Use distinct values for proposed candidate, pending review, approved decision,
released artifact, deployed version and browser acceptance. Do not collapse
these states into a single green status.

### Review and failure workflow

1. Start with the [definition of done](DEFINITION_OF_DONE.md) and compare the
   proposed claim to available evidence.
2. Confirm artifact digests and references through their owning surfaces.
3. Evaluate the actual release process only if it exists and is authorized.
   Current workflow hold checks must remain visible.
4. If a candidate appears in a previously empty lane, wire its validator and
   tests deliberately; do not remove a hold merely to make CI green.
5. Record a pending entry or evidence gap when verification stops short. A
   successful fixture test alone never creates a release entry.

### Correction and rollback

Keep past entries and mark supersession, withdrawal or correction with links.
A previous Site deployment, a Git revert and a governed data rollback are
separate operations. Restore only an exact previously verified target under its
own authority, then verify affected consumers. If no safe prior state exists,
record the explicit unavailable/empty state instead of silently serving a stale
candidate.
