---
title: Repository topology baseline expiry renewal to 2027-05-10
status: owner-directed; one-time renewal
repository_ref: main@514b2367638778a0a0b6e45a6451aea70c762909
scope: directory-governance topology baseline expiry and its trusted-base transition
---

# Repository topology baseline expiry renewal

This records the repository owner's decision, given on 2026-10-14, to renew the
topology baseline's expiry once, from 2026-11-10 to 2027-05-10. It follows the
[one-time recovery](repository-topology-baseline-recovery-20260928.md), which used the
same exact-exception pattern for waiver entries.

## Failure being prevented

The baseline in `tools/validators/directory_governance/repository_topology_baseline.json`
carries `expires_on: 2026-11-10`, set when the ratchet was introduced under ADR-0029.
On `main@514b2367` it holds 93 baselined warning groups, down from 139 at generation.
`evaluate` returns `HOLD_UNRESOLVED` with exit 1 once the expiry is in the past and any
baselined warning remains. Without a renewal, `make repository-topology` and the
`validator-suite` check would fail on every pull request from 2026-11-11 until all 93
groups were burned down.

The expiry cannot simply be edited: `validate_baseline_transition` rejects any
transition whose expiry is later than the trusted base's (`baseline transition extends
expiry`), and the repository has no renewal procedure.

## Decision

The owner chose a one-time renewal of six months over removing the no-extension rule
or letting the check go red. The MRTS milestone is due on 2026-11-10; this renewal
does not change that date, the 93 waivers, or the shrink-only rules.

## Mechanism

- The baseline's `expires_on` becomes `2027-05-10`. No entry or other metadata field
  changes.
- `validate_repository_topology.py` pins `RENEWAL_FROM_EXPIRES_ON = "2026-11-10"` and
  `RENEWAL_TO_EXPIRES_ON = "2027-05-10"`. `validate_baseline_transition` admits a later
  expiry only when the trusted baseline expires on exactly the first date and the
  candidate on exactly the second. Every other extension is still rejected.
- Waiver entries keep the ordinary rules during the renewal: shrinking is allowed,
  additions and mutations are not.
- Once this lands the trusted expiry is 2027-05-10, so the exception can never apply
  again. A further renewal needs its own reviewed change.
- The `--expires-on` default used by `--emit-baseline` moves to the renewed date.

## Validation

On the committed renewal tree, against `origin/main@514b2367` as the trusted base:

- `make repository-topology`: all four statuses 0, with 92 topology tests passing.
- `validate_repository_topology.py --trusted-baseline-ref origin/main`: `PASS`, 93
  baselined warnings, 0 invariant, 0 new drift.
- Moving `expires_on` to 2027-05-11 instead fails with `ERROR_VALIDATOR`
  (`TopologyError`).
- `make repository-governance-parity`: profile integrity `PASS`, conformance
  `HOLD_INHERITED`, 93 baselined warnings, no findings.
- `test_one_time_renewal_admits_only_its_exact_expiry` covers the renewal, a shrink and
  an addition during it, over-extension, a different trusted expiry, a second
  extension after it lands, and the post-renewal steady state. The existing
  no-extension test now extends one day past the current expiry.

## Rollback

Revert the renewal commit. The baseline returns to `expires_on: 2026-11-10`, the
exception constants disappear, and the original no-extension rule applies unchanged.
