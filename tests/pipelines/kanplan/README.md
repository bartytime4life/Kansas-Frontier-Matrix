<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-pipelines-kanplan
title: KanPlan synthetic fixture boundary
type: readme
version: v0.1.0
status: draft; fixture-only
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
owning_root: tests/
policy_label: public
[/KFM_META_BLOCK_V2] -->

# KanPlan capture-to-report fixture tests

Run from the repository root:

```sh
PROJ_NETWORK=OFF python -m pytest tests/pipelines/kanplan -q
```

This directory owns executable tests, not production data or policy. Its
`conftest.py` denies socket dials and urllib requests only within this suite.
The source-owned capture code accepts only synthetic transport and its dormant
HTTP placeholder always denies; there is no live-source test mixed into this run.

The suites cover bounded metadata/count/ID/chunk acquisition, incomplete capture,
source drift, duplicate and null identities, byte/content integrity, CRS and Z/M
handling, transform-version evidence identity, property projection, finite
resolution, analytical report scope and units, private-only delivery, withdrawal,
rollback guards, CLI path restrictions and deterministic replay inputs.

Fixture inputs live under `fixtures/synthetic/kanplan/`; implementation resides
in the owning connector, shared geo package and pipeline stage, not in tests.
See the [runbook](../../../docs/runbooks/kdot-kanplan-fixture-integration.md) for
placement, rights, limits, commands and remaining graduation evidence.

Passing fixture tests does not establish source permission, real completeness,
a native schema-validation pass, a released layer, browser interaction, deployment
or public operation. Authoring used pytest 9.0.2, below the current root test
baseline; supported-environment and hosted checks remain separate.
