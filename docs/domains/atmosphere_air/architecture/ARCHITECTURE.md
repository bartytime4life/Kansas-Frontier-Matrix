# Atmosphere / Air Architecture

Defines the trust-preserving architecture for the atmosphere-air lane.

## Core doctrine

- Preserve source identity, source role, and knowledge character end-to-end.
- Keep observed, modeled, reported, classified, and fused objects distinct.
- Public delivery consumes released artifacts only.
- Promotion is a governed decision, not a filesystem side effect.

## Trust path

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PROOF -> PUBLISHED -> API -> UI
```

## Bounded contexts

- **Intake:** source descriptors, rights posture, activation gating.
- **Normalization:** unit conversion, timestamp normalization, identity alignment.
- **Validation:** schema + policy + evidence checks.
- **Publication:** release manifests, rollback cards, immutable references.

## Non-negotiables

1. No direct UI access to RAW/WORK/QUARANTINE.
2. No public object without rights and evidence closure.
3. No modeled object labeled as observed.
4. No AQI index presented as concentration.
