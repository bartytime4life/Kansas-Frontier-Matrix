# Generic SourceDescriptor Fixtures

This lane contains small, reviewable `SourceDescriptor` fixtures for generic source-admission behavior.

## Layout

- `valid/`: positive fixtures that should pass source-admission checks.
- `invalid/`: negative fixtures named by failure reason.
- `expected/`: compact expected decision fragments consumed by tests or validators.

These fixtures are intentionally tiny and public-safe; they are not source registry, receipt, proof, or release artifacts.
