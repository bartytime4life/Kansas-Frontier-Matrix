# Reveal session projection fixtures

Synthetic fixtures for the Explorer's app-local, public-safe reveal-session
projection. They contain no key material, credential, genomic payload,
row-level data, exact sensitive geometry, source payload, or production
identifier.

- `valid/active.json` is a two-minute active interval with four fixed scope
  codes and opaque synthetic references.
- `valid/deny.json` proves that a negative projection carries no reveal detail.
- `invalid/extra-field.json` proves unknown/free-form fields fail closed.
- `invalid/ttl-too-long.json` proves the 24-hour maximum is enforced.

These fixtures do not establish policy, consent, credential, key-store, audit,
release, or publication authority.
