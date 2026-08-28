<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-telemetry-openlineage-run-event-projection-readme
title: OpenLineage RunEvent Projection Fixtures
type: README
version: v0.1.0
status: draft; synthetic; fixture-only; no-network; non-authoritative
owners:
  - TODO-validation-steward
  - TODO-telemetry-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: public; fixtures; telemetry; synthetic
owning_root: fixtures/
responsibility: provide deterministic synthetic positive and negative cases for the inactive OpenLineage terminal RunEvent projection profile without representing real sources evidence runs releases or public data
truth_posture: CONFIRMED fixture manifest and focused local replay / PROPOSED profile pending review / NEEDS VERIFICATION hosted exact-head CI
related:
  - ../../../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../../../tools/generators/telemetry/README.md
  - ../../../../../tools/validators/telemetry/README.md
  - ../../../../../tests/validators/telemetry/README.md
notes:
  - "All identities, datasets, sources, EvidenceRefs, and EvidenceBundles are synthetic."
  - "The manifest stores exact expected validator outcomes and pins deterministic projection identities for valid cases."
[/KFM_META_BLOCK_V2] -->

# OpenLineage RunEvent Projection Fixtures

`cases.json` is the compact synthetic fixture manifest for `kfm.telemetry.openlineage-run-event-projection.v1`. The generator constructs full candidates in memory so fixture review stays focused on intent, mutation, and exact expected result rather than duplicated large JSON documents.

## Coverage

The manifest contains eighteen cases:

- internal successful run -> `PASS` with `COMPLETE` event;
- internal failed run -> `PASS` with `FAIL` event;
- public released/generalized/public-safe run -> `PASS` with `COMPLETE` event;
- partial RunReceipt -> `ABSTAIN` with no event;
- unpublished public request -> `DENY` with no event;
- restricted evidence -> `DENY` with no event;
- telemetry policy denial -> `DENY` with no event;
- unresolved EvidenceRef, dataset/receipt drift, identity drift, decision drift, invalid event presence, event identity/time drift, ordering drift, geometry side channel, and non-effects drift negatives.

Valid cases pin `expected_projection_id` where replay identity is significant. Every case declares the exact validator outcome and finding-code set.

## Run

```bash
python tools/validators/telemetry/validate_openlineage_run_event_projection.py \
  --fixtures
```

Render one case:

```bash
python tools/generators/telemetry/build_openlineage_run_event_projection.py \
  --case valid-internal-success-complete
```

## Safety boundary

The fixtures contain no live endpoint, credential, source payload, geometry, personal data, restricted location, release, or public-use authority. A fixture `PASS` proves only that the synthetic candidate matches the bounded contract.

## Rollback

Remove this fixture directory together with the paired contract, schema, generator, validator, tests, workflow, source map, and receipt. No data migration or public correction is required.
