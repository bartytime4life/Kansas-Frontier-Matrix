<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-synthetic-kanplan
title: KanPlan synthetic fixture boundary
type: readme
version: v0.1.0
status: draft; fixture-only
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
owning_root: fixtures/
policy_label: public
[/KFM_META_BLOCK_V2] -->

# KanPlan-shaped synthetic inputs

These two files are wholly authored, public-safe test inputs, not KDOT captures,
a source descriptor, a road network, or a released KFM layer. Their fictional
coordinates are outside Kansas. The metadata record limit is deliberately two.
The editorial username and route values are invented negative/projection tests.

`state-metadata.synthetic.json` supplies the test-only ArcGIS field/geometry
shape; `state-features.synthetic.json` supplies two lines, multipart geometry,
and native Z/M measures. Keep them labeled. Their private map/report evaluation
outputs must not be confused with admitted or released source data.

Owning root: `fixtures/`, reusable synthetic test input under adopted Directory
Rules. No RAW, catalog, source registry, or release authority is established.
See the [runbook](../../../docs/runbooks/kdot-kanplan-fixture-integration.md) and
[tests](../../../tests/pipelines/kanplan/README.md).
