# Issue Inventory Projection fixtures

These files exercise the read-only
`kfm.briefing.issue-inventory.fixture.v1` contract.

## Valid

- `open-target.json` — issue `1647` is open; issue `1675` is also present.
- `closed-target.json` — issue `1647` is closed.
- `missing-target.json` — issue `1647` is absent.

All rows are synthetic fixture state. They are **not** a current GitHub issue
inventory and must not be cited as live repository evidence.

## Invalid

- `digest-mismatch.json` — canonical bytes do not match the declared digest.
- `duplicate-issue-number.json` — one issue number is projected twice.
- `unsorted-issues.json` — issue rows are not in deterministic ascending order.
- `mutation-allowed.json` — mutation permission is impermissibly true.
- `issue-updated-after-projection.json` — a row claims an update after the
  projection timestamp.

The fixture family contains no issue titles, bodies, comments, labels,
assignees, permissions, secrets, protected payloads, or public-release state.
