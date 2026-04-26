# Documentation Hub

This directory contains operational and reference documentation for the repository.

## Current structure (verified on 2026-04-26)

- `docs/adr/` — architecture decision records.
- `docs/architecture/` — system and subsystem architecture notes.
- `docs/domains/` — domain-specific documentation lanes.
- `docs/registers/` — register/index style docs.
- `docs/runbooks/` — execution and remediation runbooks.
- `docs/sources/` — source-facing documentation.
- `docs/standards/` — documentation standards and conventions.

## How to use this directory

1. Start with `docs/runbooks/repository-next-steps.md` for active priorities.
2. Use `docs/runbooks/markdown-debt-backlog.md` to identify highest marker debt files.
3. Record architecture-impacting decisions in `docs/adr/` before changing folder authority or governance rules.

## Documentation change rules

- Prefer verified repo facts over speculative language.
- Keep contract/policy/runtime behavior authoritative in code and schemas, and use docs for explanation and operator guidance.
- When changing a major workflow, update the relevant runbook and ADR references in the same PR.
