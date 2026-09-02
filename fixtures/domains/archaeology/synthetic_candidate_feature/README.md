# Synthetic CandidateFeature fixtures

These fixtures exercise the bounded `CandidateFeature` safety projection. They
contain only synthetic identifiers and no production, protected, private-land,
burial, sacred-place, collection-security, or culturally restricted data.

- `valid.json` remains explicitly `CANDIDATE`, uses governed references, keeps
  spatial precision withheld, and contains no inline geometry.
- `malformed_candidate_id_deny.json` proves that the validator and schema share
  the same lowercase candidate-identifier grammar.
- `unsupported_candidate_type_deny.json` proves that the validator rejects
  confirmed-site-like or otherwise unsupported candidate-type labels rather than
  allowing them to weaken the candidate boundary.
- `non_string_vocabulary_deny.json` proves that malformed structured vocabulary
  values return a finite denial rather than raising an exception during bounded
  membership or evidence-binding checks.
- `malformed_spec_hash_deny.json` proves that optional evidence-binding digests
  use the same lowercase SHA-256 grammar in the schema and executable validator.
- `null_optional_scalars_deny.json` proves that explicitly null candidate type,
  spatial precision, and evidence-binding digest values fail closed instead of
  being treated as omitted.
- `malformed_confidence_statement_deny.json` proves that optional confidence
  prose remains a bounded string instead of accepting empty or structured values.
- `unicode_invisible_confidence_deny.json` proves that a confidence statement
  containing only an Arabic Letter Mark plus a variation selector cannot
  masquerade as reviewable text.
- `unsupported_spatial_precision_deny.json` proves that unsupported precision
  labels such as `EXACT` fail closed instead of implying an unsafe location posture.
- `unclassified_geometry_reference_deny.json` proves that even an opaque internal
  geometry reference cannot omit its withheld or generalized precision posture.
- `sensitive_geometry_deny.json` uses synthetic zero coordinates solely to prove
  that any inline coordinate field is rejected before downstream use.
- `location_bearing_reference_deny.json` proves that a nominal `kfm://`
  reference cannot smuggle query, fragment, or encoded locator material through
  a governed-reference field.
- `path_locator_reference_deny.json` proves that a nominally opaque geometry
  reference cannot smuggle case-varied latitude, longitude, bounding-box,
  coordinate-system, or other protected locator tokens through its path.
- `compact_locator_reference_deny.json` proves that joining a locator token
  directly to digits, such as `lat39`, cannot evade the protected-path rule.
- `misbound_reference_family_deny.json` proves that a syntactically valid
  source reference cannot satisfy an EvidenceRef/EvidenceBundle binding.
- `non_string_reference_deny.json` proves that malformed structured reference
  values return a finite denial rather than crashing validation.
- `unbound_catalog_candidate_deny.json` proves that a candidate cannot claim
  under-review/retained posture or processed/catalog lifecycle without at least
  one governed EvidenceRef.
- `empty_evidence_refs_deny.json` proves that an explicitly present EvidenceRef
  binding cannot be an empty array, even while the candidate remains in `WORK`.
- `superseded_without_correction_deny.json` proves that a superseded candidate
  cannot lose its governed correction or withdrawal lineage.

Run the deterministic, standard-library-only proof with:

```bash
python tools/validators/archaeology/validate_candidate_feature.py --fixtures
python -m unittest tests.domains.archaeology.test_candidate_not_site
```

Passing these checks proves only the schema-aligned candidate identifier,
candidate-type vocabulary, spatial-precision vocabulary, and geometry-reference
precision binding; bounded candidate discriminator; inline location denial;
opaque-reference, protected-locator-token, and reference-family boundaries;
conditional EvidenceRef binding; and supersession
correction binding; malformed-reference finite denial; and nonempty governed
reference bindings; malformed-vocabulary and null-scalar finite denial; and
schema-aligned `spec_hash` and deterministic Unicode-safe confidence-statement
validation. It
does not confirm a site,
authorize publication, or establish full EvidenceBundle closure, policy,
cultural review, or public-safe transformation.
