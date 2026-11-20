<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/inaturalist-fixture-ingest
title: iNaturalist Fixture Ingest
type: runbook
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Flora steward · iNaturalist source steward · Rights and sensitivity reviewers · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-source-candidates; no-public-coordinates
owning_root: docs/
responsibility: reproduce private plant-query intake and explain proof limits
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION cross-domain source admission, human review and downstream use
[/KFM_META_BLOCK_V2] -->

# iNaturalist Fixture Ingest

The [intake](../../pipelines/domains/flora/inaturalist_ingest.py) composes the
existing observation parser and cursor reconciler. The fixed plant-context query
and [contract](../../contracts/domains/flora/inaturalist_ingest_candidate.md) are
proposed; source admission and cross-domain use remain unreviewed.

## Reproduce

Use Python 3.11 or 3.12 with the existing locked profiles:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py connectors-core
export KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -B -m pipelines.domains.flora.inaturalist_ingest complete
python -B -m pipelines.domains.flora.inaturalist_ingest count-drift
python -B -m pipelines.domains.flora.inaturalist_ingest empty
python -B -m unittest discover -s connectors/inaturalist/tests -p 'test_*.py' -v
python -B -m pytest tests/pipelines/domains/flora/test_inaturalist_ingest.py -q --strict-config --strict-markers
```

The complete case has three invented observations in two pages: an open source
point, an obscured needs-ID/noncommercial record, and a private unresolved-license
record with unverified plant lineage. The last two retain quarantine. All cases
return final `HOLD`. Count drift remains incomplete; the empty walk proves no
absence. No live observations, real observer accounts or sensitive plant sites
are used. Only the documented Plantae root ID is a provider taxon identifier.

## Source/runtime repairs

Before this change, dictionary/list quality grades raised uncaught `TypeError`
during query planning; malformed non-string grades now produce finite
`QUALITY_GRADE`. Capture formatting previously discarded fractional seconds;
UTC normalization now retains them. Existing privacy fixes, source flags and
injected retrieval behavior continue to run under the source workflow.

## Minimized snapshots and stronger verification

`prepare_capture(raw_bytes)` verifies the original supplied capture before returning
a private candidate. Returned snapshots minimize nested user objects to scalar
ID/login and discard incidental response metadata. Record text and private or
obscured geometry can still be sensitive. Minimization grants no public use.

Original and minimized bodies have separate byte hashes and lengths. Replaying a
minimized candidate alone cannot prove discarded original bytes. To reverify those,
call `validate_candidate(candidate, original_capture=raw_bytes)`. Never treat a
minimized digest as the original-source digest or claim persistent capture
availability. No source authentication, source admission or evidence closure occurs.

## CI and rollback

The [dedicated workflow](../../.github/workflows/inaturalist-pipeline.yml) installs
locked profiles, runs all connector unittest cases, declaration validation, new
intake tests and three goldens under the Python network guard on 3.11/3.12.
The existing source workflow remains in place. This is Python-process egress
control, not host-wide isolation. Local proof, hosted CI, main delivery and live
source behavior remain separate. Roll back through a reviewed revert and preserve
previous generated receipts; no provider operation or data migration is involved.
