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
- `unsupported_spatial_precision_deny.json` proves that unsupported precision
  labels such as `EXACT` fail closed instead of implying an unsafe location posture.
- `sensitive_geometry_deny.json` uses synthetic zero coordinates solely to prove
  that any inline coordinate field is rejected before downstream use.
- `location_bearing_reference_deny.json` proves that a nominal `kfm://`
  reference cannot smuggle query, fragment, or encoded locator material through
  a governed-reference field.
- `unbound_catalog_candidate_deny.json` proves that a candidate cannot claim
  under-review/retained posture or processed/catalog lifecycle without at least
  one governed EvidenceRef.
- `superseded_without_correction_deny.json` proves that a superseded candidate
  cannot lose its governed correction or withdrawal lineage.

Run the deterministic, standard-library-only proof with:

```bash
python tools/validators/archaeology/validate_candidate_feature.py --fixtures
python -m unittest tests.domains.archaeology.test_candidate_not_site
```

Passing these checks proves only the schema-aligned candidate identifier,
candidate-type vocabulary, and spatial-precision vocabulary; bounded candidate
discriminator; inline location denial; opaque-reference boundary; conditional
EvidenceRef binding; and supersession correction binding. It does not confirm a
site, authorize publication, or establish full EvidenceBundle closure, policy,
cultural review, or public-safe transformation.
