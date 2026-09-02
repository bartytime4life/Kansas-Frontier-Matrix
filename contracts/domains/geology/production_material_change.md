<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/geology/production-material-change
title: KGS Production Material Change Assessment
type: semantic-contract
version: v1
status: proposed
owners: [geology-domain-steward]
created: 2026-08-07
policy_label: internal
related:
  - schemas/contracts/v1/domains/geology/production_material_change.schema.json
  - tools/validators/domains/geology/validate_production_material_change.py
  - fixtures/contracts/v1/domains/geology/production_material_change/
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
source_ideas:
  - KFM-P25-PROG-0002
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# KGS Production Material Change Assessment

## Purpose

`ProductionMaterialChange` is a **non-authoritative, no-network comparison record** for two
version-pinned Kansas Geological Survey oil-and-gas production snapshots. It answers one
bounded operational question:

> Did the declared snapshot metadata change enough to require steward review?

The object does not fetch KGS data, prove that a production value is correct, reinterpret a
lease as a well, infer a geologic deposit, alter canonical data, approve rights, or publish a
release. It is process evidence for a watcher or dry-run comparison only.

The source idea is the KFM card `KFM-P25-PROG-0002`, derived from the attached
*New Ideas 4-19-26* packet: compare production-table manifests and `spec_hash`-bound
snapshots when monthly coverage or spatial footprints change.

## Authority boundary

- KGS/KDOR production records remain **production-record evidence**, not physical-geology
  truth.
- A watcher may emit `NO_CHANGE`, `REVIEW`, `HOLD`, or `ERROR`; it may not promote,
  release, or publish.
- `REVIEW` means only that declared snapshot metadata differs. It does not establish that the
  upstream change is correct, material to a public claim, or safe to release.
- `HOLD` is required when the prior snapshot or rights posture is unresolved, or when monthly
  coverage regresses.
- Exact source bytes, record-level claims, and release decisions remain outside this contract.

## Required fields

| Field | Meaning |
|---|---|
| `assessment_id` | Deterministic ID derived from the canonical packet excluding `assessment_id` and `spec_hash`. |
| `schema_version` | `v1`. |
| `source_descriptor_ref` | Reference to the admitted KGS production source descriptor. |
| `dataset_role` | `PRODUCTION_RECORDS`; prevents collapse into geology observations or reserves. |
| `prior_snapshot` | Prior comparison snapshot, or `null` when no baseline exists. |
| `current_snapshot` | Current snapshot metadata. |
| `assessment` | Finite watcher outcome, exact change dimensions, reason codes, and evidence closure. |
| `governance` | Explicit non-publisher and no-authority boundary. |
| `spec_hash` | SHA-256 of canonical JSON excluding `assessment_id` and `spec_hash`. |

Each snapshot binds:

- snapshot reference and retrieval time;
- monthly coverage end (`YYYY-MM`);
- record count;
- manifest and public-footprint digests;
- rights state;
- source-role/support-type declarations;
- evidence references.

## Computed change dimensions

The validator computes the exact sorted set:

- `COVERAGE_END`
- `RECORD_COUNT`
- `MANIFEST_DIGEST`
- `FOOTPRINT_DIGEST`

`REVIEW` must name precisely the dimensions that changed. `NO_CHANGE` must name none.

## Finite outcomes

| Outcome | Required semantics |
|---|---|
| `NO_CHANGE` | Prior/current snapshots are comparable, rights are verified, all compared fields match, and reason includes `SNAPSHOTS_MATCH`. |
| `REVIEW` | Rights are verified, coverage did not regress, at least one computed dimension changed, and reason includes `MATERIAL_CHANGE_DETECTED`. |
| `HOLD` | Prior snapshot missing, rights unresolved, or monthly coverage regressed; no materiality claim is made. |
| `ERROR` | Operational failure; no change claim is made. |

## Deterministic validation

```bash
python tools/validators/domains/geology/validate_production_material_change.py \
  fixtures/contracts/v1/domains/geology/production_material_change/valid/material_change_review.json

pytest -q tests/domains/geology/test_production_material_change.py
```

## Non-goals

This contract does not:

- activate a connector or perform a network request;
- compare raw production rows or geometry bytes;
- establish KGS completeness or accuracy;
- turn lease production into well production;
- establish a resource occurrence, deposit, estimate, reserve, permit, or ownership claim;
- evaluate policy, promotion, release, deployment, or publication.
