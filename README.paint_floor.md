# paint_floor.sh

`paint_floor.sh` generates backdated empty commits to fill your GitHub contribution graph for the last 365 days (from 365 days ago through today).

It requires these environment variables:

- `GIT_USER_NAME`
- `GIT_USER_EMAIL`

> Important: `GIT_USER_EMAIL` must be a verified email on your GitHub account. If it is not verified on GitHub, contributions may not appear on your graph.

Optional environment variables:

- `MIN_COMMITS` (default: `1`)
- `MAX_COMMITS` (default: `4`)

The script is idempotent for the computed date window. After a successful run, it writes a `.painted` marker file with the exact start/end range and exits early on repeat runs for the same range.

Commit timestamps are set at random whole hours between `09:00:00` and `21:00:00` local time for each generated commit.
