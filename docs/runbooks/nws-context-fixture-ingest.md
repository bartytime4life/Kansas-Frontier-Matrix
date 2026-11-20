<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/nws-context-fixture-ingest
title: NWS Context Fixture Ingest
type: runbook
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Hazards steward · Source steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-context; not-for-life-safety; no-alert-authority
owning_root: docs/
responsibility: explain bounded source-context replay and its proof limits
truth_posture: CONFIRMED bounded fixture replay; PROPOSED candidate profile; NEEDS VERIFICATION human review, source admission and any downstream use
[/KFM_META_BLOCK_V2] -->

# NWS context fixture ingest

The [ingest implementation](../../pipelines/domains/hazards/nws_context_ingest.py)
binds the existing NOAA source parser to fixed synthetic capture packets. It
prepares private held context and sends no alerts or instructions.

## Reproduce

Use Python 3.11 or 3.12 and the locked installer:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py connectors-core
export KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -B -m pipelines.domains.hazards.nws_context_ingest lineage
python -B -m pipelines.domains.hazards.nws_context_ingest expired-partial
python -B -m pipelines.domains.hazards.nws_context_ingest empty
python -B -m pytest tests/pipelines/domains/hazards/test_nws_context_ingest.py connectors/noaa/tests/test_nws_alerts.py -q --strict-config --strict-markers
```

All three commands emit aggregate `HOLD`. `lineage` retains one superseded
message and one source-window classification at the fixed instant. The partial
case retains one expired, quarantined synthetic Test message and an unresolved
next page. The empty case has zero messages and unestablished coverage. A replay
success proves the sealed expected candidate, never source admission, absence of
hazards, current warning status or operational safety.

## Input and handling limits

The bounded library accepts supplied HTTP-200 bytes for Kansas's active-alert
surface, at most 256 KiB / 64 features. It has strict JSON, time and nesting
checks and a 4 MiB in-memory candidate cap. Raw feature snapshots preserve source
instructions privately. CLI choices are fixed; it prints no message content,
IDs, geometry, source URLs or next-page URLs, and writes no files.

The [contract](../../contracts/domains/hazards/nws_context_ingest_candidate.md)
defines byte identity, source role, exact-time evaluation and hold semantics.
The proposed source descriptor lives in Atmosphere and remains unresolved;
referencing it neither duplicates source ownership nor admits cross-domain use.
There is no live fetch, polling, next-page following, notification delivery,
archive-completeness check, persistence, lifecycle advancement or release.
Individual geometry validity and official source completeness are not qualified.

## CI and review

The [workflow](../../.github/workflows/nws-context-pipeline.yml) runs the existing
source parser and new intake tests, declaration validation and all three CLI
cases under the Python network guard on 3.11 and 3.12. Local tests, hosted CI,
main merge, source admission, persistent capture, evidence closure and any public
release remain separate lanes. Review source/rights, sensitivity, semantics and
validation before downstream use. A reviewed revert rolls back this bounded
unit; historical receipts and source records remain unchanged.
