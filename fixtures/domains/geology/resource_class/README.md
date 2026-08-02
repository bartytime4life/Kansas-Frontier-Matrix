# Geology resource-class fixture profile

This lane contains synthetic, deterministic inputs for
`tools/validators/domains/geology/validate_resource_class_distinction.py`.
It proves a bounded anti-collapse profile for `MineralOccurrence`,
`ResourceDeposit`, and `ResourceEstimate` records plus exact negative cases.
It is not a canonical classification scheme, mineral occurrence or deposit,
resource or reserve estimate, title or permit record, `PolicyDecision`,
`EvidenceBundle`, release record, or publication authority.

The profile ID is `kfm-geology-resource-class-fixture-v1`. The three object
families and anti-collapse rules are supported by current draft Geology
doctrine. The exact JSON shape, source-role pairings, synthetic classification
references, and finding codes are `PROPOSED` fixture bindings. Existing
permissive schemas remain unchanged until the repository resolves their naming,
classification-vocabulary, and canonical-home questions.

## Inventory

`valid/` contains one public-safe case for each bounded character:

- `MINERAL_OCCURRENCE` — reported presence, not a deposit or estimate;
- `RESOURCE_DEPOSIT` — compiled deposit context, not a permit or reserve;
- `RESOURCE_ESTIMATE` — modeled quantity with a synthetic scheme, method,
  effective date, confidence class, and assumptions.

`invalid/` contains exact fail-closed cases for occurrence-as-deposit,
modeled-potential-as-deposit, permit-as-deposit, production-as-deposit,
estimate-as-observation, estimate-as-reserve, missing estimate classification,
and precise resource-location exposure. Every invalid JSON file has a sorted
`.expected_error.txt` sidecar containing only finding code and JSON path.

All records use the non-real county sentinel `99999`. No file contains a live
endpoint, credential, source row, real commodity claim, precise coordinate,
owner or parcel identity, extraction guidance, or release-ready data.

## Run

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/geology/test_source_role_anti_collapse.py --verbose
```

Rollback is a clean revert of the feature change. No source, lifecycle, proof,
release, or published state is created by these fixtures.
