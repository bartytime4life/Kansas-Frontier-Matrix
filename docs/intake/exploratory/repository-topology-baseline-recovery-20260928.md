---
title: Repository topology baseline recovery for three dropped waiver groups
status: owner-directed; one-time recovery
repository_ref: main@fc7c558e3439b08f7e8670a4ef24c6985e5164be
scope: directory-governance topology baseline and its trusted-base transition
---

# Repository topology baseline recovery

This records the repository owner's decision, given on 2026-09-28, to restore three
waiver groups to the topology baseline in one reviewed batch. It follows the
[ratchet review packet](repository-topology-ratchet-review-20260927.md), which
established that the groups were present in the accepted baseline at
`main@27202a0595ecdc6afd6f98b3aedaa236243e07b3` but are absent from the baseline
carried by current `main`.

## Failure being resolved

`make repository-topology` on `main@fc7c558e` reports `FAIL_NEW_DRIFT` with three new
fingerprints and fails the `validator-suite / run-validators` check on every pull
request:

| Rule | Subject | Live fingerprint | Evidence members |
|---|---|---|---|
| `KFM-TOPO-001` | `path-grammar:uppercase` | `sha256:3da8cffd3753378852fc069c240165a15e4f8cdfc90d6ee1c0d8274e6307a430` | uppercase tracked paths |
| `KFM-TOPO-004` | `catalog/` | `sha256:71a120ae8ca2b69896266c9ddd52f6d03577ea91fa2de4390b7d57b9ceeb912f` | 43 frozen `catalog/` members |
| `KFM-TOPO-009` | `scaffold-only-leaf-directories` | `sha256:265f3f934f6333b04781af9b20520842c8187d79dc35e1a36906c3835f1b1079` | scaffold-only leaf directories |

The historical entries cannot be copied back: their evidence changed, so their
fingerprints no longer match the live scan. The live entries cannot be added
directly either: `validate_baseline_transition` rejects any waiver fingerprint the
trusted base does not already carry.

## Decision

The owner chose a one-time recovery over leaving the check red or recovering only the
two non-catalog groups. For `catalog/`, this decision supersedes the
`CATALOG_MULTI_ENTRY_BINDING_HOLD` recorded in
[issue #4228](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228#issuecomment-5736885489)
for the purpose of waiving the current 43-member group only. It does not accept the
catalog correction register entries, bind ADR-0040's machine transition, or authorize
Stage 2.

## Mechanism

- The baseline gains exactly the three entries produced by
  `validate_repository_topology.py --emit-baseline` for these subjects. No other
  entry, expiry or metadata field changes.
- `validate_repository_topology.py` pins `RECOVERY_TRUSTED_BASELINE_SHA256` to the
  SHA-256 of the trusted baseline bytes on `main@fc7c558e`
  (`0a06efedd47f107c84f0ca611b6ae74050212daa99a8710363991ab4bb3e6a18`) and
  `RECOVERY_FINGERPRINTS` to the three fingerprints above.
- `validate_baseline_transition` admits an added fingerprint only when the trusted
  baseline hashes to that value, the fingerprint is one of the three, and the trusted
  base has no entry with the same rule and subject. All three must arrive together.
  Every other addition, expansion, mutation, expiry extension and metadata change is
  still rejected.
- Once this lands, the trusted baseline differs from the pinned bytes, so the
  exception can never apply again. Later transitions are shrink-only as before.

## Validation

- `make repository-topology` on the committed recovery tree (which adds this record and
  its receipt): `PASS: 13681 tracked paths; 0 invariant; 0 new drift; 122 baselined
  warnings; 0 stale baseline entries`; all four statuses are 0.
- `validate_repository_topology.py --trusted-baseline-ref origin/main` passes.
- Removing the three entries from the new baseline reproduces the `main` baseline
  byte for byte, confirming the pinned hash.
- `test_one_time_recovery_admits_only_its_exact_batch` covers the accepted batch, a
  missing or different trusted hash, a partial batch, an unrelated addition, and the
  post-recovery steady state.

## Out of scope

`control_plane/repository_governance_parity.yaml` pins `base_ref`
`f1a415639a57985f859fa66e6ca73cd5c349aa78`, which is not an ancestor of current
`main`, and stale `expected_topology` counts. Two parity tests fail on `main` for that
reason, before and after this change. Re-pinning that profile is a separate decision.

## Rollback

Revert the recovery commit. The baseline returns to the pinned bytes and the three
findings fail as new drift again; no other state changes.
