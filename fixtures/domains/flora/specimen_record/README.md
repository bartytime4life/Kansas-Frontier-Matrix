# Synthetic Flora SpecimenRecord conformance fixtures

`cases.json` is a closed, no-network fixture profile for the existing
`SpecimenRecord` contract. It carries one shared synthetic base candidate and
deterministic per-case mutations. The validator recomputes candidate identity
and `spec_hash` unless a case deliberately tests one of those fields.

The profile proves only local schema and semantic conformance. It does not
contact KANU, KSC, iDigBio, GBIF, USDA PLANTS, NatureServe, a herbarium, or any
other source. It does not admit a source, establish real specimen identity,
resolve taxonomy or evidence, approve rights or sensitivity, assert current
occurrence, authorize release, or publish a record.

The valid cases cover:

- a public-safe **candidate** derived from historical voucher evidence;
- a sensitive specimen held from public projection;
- an unresolved catalog candidate; and
- an explicitly synthetic reality-boundary case.

The negative matrix covers current-occurrence overclaim, label-text taxonomy
overclaim, exact-locality exposure, false governance effects, identity and hash
drift, source-role mismatches, missing redaction, image-rights conflict,
restricted public projection, raw coordinates, incomplete correction lineage,
noncanonical reference ordering, missing collection time, unresolved current
determination, locality-reference conflicts, and rare-taxon handling.
