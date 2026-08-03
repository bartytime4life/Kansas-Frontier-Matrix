<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ingest-ssurgo-watch-readme
title: SSURGO package drift fixture tests
type: README
version: v0.1
status: bounded executable coverage
owners:
  - OWNER_TBD - tooling QA (responsible owner; identity NEEDS VERIFICATION)
required_review_roles:
  - Soil steward
  - NRCS source steward
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; synthetic-fixtures; no-network; no-publication
owning_root: tests/
responsibility: Prove deterministic SSURGO fixture-comparison behavior without source access or lifecycle mutation.
related:
  - ../../../tools/ingest/ssurgo_watch/README.md
  - ../README.md
  - ../../../.github/workflows/domain-soil.yml
notes:
  - "All fixtures use non-real survey-area symbol ZZ999 and a fixture:// source reference."
  - "Passing tests do not admit SSURGO, establish a live threshold, or create evidence, receipt, policy, review, release, or publication authority."
  - "Soil and NRCS source stewards are required review roles, not parallel authority owners for this test lane."
[/KFM_META_BLOCK_V2] -->

# SSURGO package drift fixture tests

This lane proves the bounded behavior of
[`tools/ingest/ssurgo_watch/`](../../../tools/ingest/ssurgo_watch/README.md).
It performs no network access and contains no live SSURGO package, endpoint,
county record, source descriptor, or rights assertion.

## Fixture matrix

| Case | Expected outcome | Boundary proved |
|---|---|---|
| `no_material_change` | `NO_MATERIAL_CHANGE` | Same package, schema, geometry, and mapunit partition. |
| `below_threshold` | `NO_MATERIAL_CHANGE` | Bound spatial artifact declares 4,000 ppm label disagreement. |
| `threshold_boundary` | `NO_MATERIAL_CHANGE` | Bound spatial artifact reaches the exact 5,000 ppm strict boundary. |
| `material_area_change` | `PROPOSED_WORK_RECORD` | Bound spatial artifact declares 6,000 ppm label disagreement. |
| `equal_total_label_drift` | `PROPOSED_WORK_RECORD` | Aggregate areas are unchanged, but exact label disagreement is 6,000 ppm. |
| `schema_change` | `PROPOSED_WORK_RECORD` | Canonical attribute-column inventory changed. |
| `constraint_change` | `PROPOSED_WORK_RECORD` | Profiled primary/foreign-key relationship changed. |
| `table_content_change` | `PROPOSED_WORK_RECORD` | Profiled table values changed without schema drift. |
| `geometry_drift` | `GEOMETRY_DRIFT` | Same-area mapunit geometry fingerprint changed; area math is not evaluated. |
| `derived_state_drift` | `ERROR` | Derived output changed while package and extraction-profile hashes stayed fixed. |
| `stale_input` | `STALE_INPUT` | Package publication date regressed. |

Each case carries a prior/current pair. Cases with geometry-fingerprint drift
and evaluable materiality also carry a separate `spatial_diff.json`. Repeated
prior fixtures are intentional: they keep each case independently runnable and
mirror the explicit input interface.

## Additional negative coverage

The standard-library test suite also checks:

- duplicate JSON key denial;
- undeclared live-source field denial;
- `fixture_only` enforcement;
- mapunit coverage closure;
- canonical schema-column ordering;
- profiled-table digest closure;
- primary/foreign-key drift detection;
- nullable primary-key, missing foreign-key target, and reference-type denial;
- materiality-profile drift abstention;
- extraction-profile drift abstention;
- geometry-profile drift abstention;
- spatial-diff content, sidecar, geometry-set, profile, CRS, unit, and area-bound
  validation;
- rejection of a spatial-diff artifact when geometry did not drift;
- bounded rejection of oversized integers;
- stable spec-hash and run-content-hash separation;
- deterministic serialized reports;
- active socket, DNS, and `urllib` network denial;
- CLI exit polarity; and
- create-only external output with repository destinations denied.

## Run

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
```

A green result proves only this frozen synthetic profile. It does not prove
current NRCS metadata, SSURGO rights, package freshness, survey-area geometry,
table semantics, source admission, Soil truth, EvidenceBundle closure, policy,
promotion, release, or publication readiness.

## Direct children

```text
tests/ingest/ssurgo_watch/
├── README.md
├── fixtures/
│   └── <case>/{prior.sidecar.json,current.sidecar.json[,spatial_diff.json]}
└── test_ssurgo_watch.py
```

All fixture files are test-local, synthetic, public-safe, and durable only as
proof inputs for this helper. They are not reusable domain fixtures, source
captures, receipts, or evidence objects.
