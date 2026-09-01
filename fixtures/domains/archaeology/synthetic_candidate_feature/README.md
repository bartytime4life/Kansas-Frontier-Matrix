# Synthetic CandidateFeature fixtures

These fixtures exercise the bounded `CandidateFeature` safety projection. They
contain only synthetic identifiers and no production, protected, private-land,
burial, sacred-place, collection-security, or culturally restricted data.

- `valid.json` remains explicitly `CANDIDATE`, uses governed references, keeps
  spatial precision withheld, and contains no inline geometry.
- `sensitive_geometry_deny.json` uses synthetic zero coordinates solely to prove
  that any inline coordinate field is rejected before downstream use.

Run the deterministic, standard-library-only proof with:

```bash
python tools/validators/archaeology/validate_candidate_feature.py --fixtures
python -m unittest tests.domains.archaeology.test_candidate_not_site
```

Passing these checks proves only the bounded candidate discriminator and inline
location denial. It does not confirm a site, authorize publication, or establish
policy, cultural review, EvidenceBundle closure, or public-safe transformation.
