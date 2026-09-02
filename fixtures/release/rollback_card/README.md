# RollbackCard fixtures

Synthetic, no-network fixtures for the proposed non-executing RollbackCard profile.

- `valid/` covers prior-release rollback candidates, withdrawal candidates, and
  intentional holds.
- `invalid/` covers missing prior targets, same-release targets, absent correction
  notices, invalid temporal order, false authority, and placeholder digests.

The fixtures model candidate plans only. They do not execute rollback, mutate public
state, erase history, authorize release, or publish.
