# Atmosphere / Air Source Registry

Human-readable source registry posture for atmosphere-air.

## Required fields

- `source_id`
- `source_role`
- `knowledge_character`
- `publisher`
- `rights_spdx`
- `verification_status`
- `public_release_allowed`
- `last_verified_at`

## Activation rule

A source remains inactive for public release when rights, terms, verification status, or source role are unresolved.

## Role expectations

- **Observed sensor:** measured values with site/instrument context.
- **Public AQI report:** index/report semantics only.
- **Model field:** modeled outputs with uncertainty.
- **Remote sensing mask:** classification context.
- **Derived fusion:** explicit multi-source method and uncertainty.
