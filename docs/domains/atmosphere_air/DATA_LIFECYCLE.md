# Atmosphere / Air Data Lifecycle

Lifecycle rules for atmosphere-air data and artifacts.

## State model

1. **RAW**: source-native payloads, not public.
2. **WORK**: normalized candidates and QC staging.
3. **QUARANTINE**: failed validation/policy/evidence items.
4. **PROCESSED**: validated canonical candidates.
5. **CATALOG**: discoverability and lineage objects.
6. **PROOF**: EvidenceBundle and decision candidates.
7. **PUBLISHED**: released artifacts only.

## Promotion requirements

- schema validity
- evidence closure
- policy compliance
- reviewer sign-off
- rollback target
