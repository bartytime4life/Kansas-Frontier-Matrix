# TemporalViewState fixtures

This fixture-first family proves the closed v1 shape and bounded local semantics of `kfm.temporal.view-state.v1`.

- `valid/` contains supported instant and comparison state.
- `unsupported/` contains schema-valid states that return explicit bounded outcomes, such as an unknown timezone or geologic-age profile.
- `invalid/` contains schema-invalid candidates for closed-profile drift.
- Fixtures are fictional, public-safe, and no-network. They are not source data, evidence, releases, or production observations.

`state_id` is the SHA-256 identity of canonical JSON with `state_id` omitted. Canonical JSON uses sorted object keys, preserved array order, UTF-8, finite numbers, and no insignificant whitespace.

A passing validator proves only local shape, identity, temporal precision, mode compatibility, and bounded outcomes. It does not resolve references or authorize any lifecycle or public transition.