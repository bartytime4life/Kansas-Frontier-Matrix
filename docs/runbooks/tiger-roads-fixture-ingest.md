<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/tiger-roads-fixture-ingest
title: TIGER Roads Fixture Ingest
type: runbook
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Source steward · Roads/Rail/Trade steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public; source-capture; candidate-only; no-road-authority
owning_root: docs/
responsibility: explain reproducible no-network TIGER ingest checks and their verification limits
truth_posture: CONFIRMED local fixture commands; PROPOSED review handoff; NEEDS VERIFICATION hosted CI and source admission
[/KFM_META_BLOCK_V2] -->

# TIGER roads fixture ingest

The [ingest implementation](../../pipelines/domains/roads-rail-trade/ingest_tiger_roads.py)
composes the existing Census package inspector with bounded archive validation,
provider-reference comparison and a strict held-candidate projection. It is the
fixture-first `INGEST` binding for `tiger_roads.yaml`, not road normalization.

## Run and verify

Use supported Python 3.11 or 3.12 with the existing locked installer:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py connectors-core
export KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -B -m pipelines.domains.roads-rail-trade.ingest_tiger_roads clean
python -B -m pipelines.domains.roads-rail-trade.ingest_tiger_roads duplicate-identity
python -B -m pytest tests/pipelines/domains/roads_rail_trade/test_tiger_roads_ingest.py connectors/census/tests/test_tiger_package.py -q --strict-config --strict-markers
```

Both commands succeed as replays and emit `HOLD`. The clean case has two
provisional raw features; the duplicate case has two features with an explicit
identity quarantine. A successful command means the sealed golden matched;
it never means source admission or lifecycle advancement. The CLI accepts only
these fixed cases, prints aggregate status and hashes, and writes no files.
Library candidates remain private in memory.

## Input, identity and limits

Packets contain deterministic synthetic ZIP bytes, expected digest, a filename
and capture time, plus a complete golden candidate. The two 2025 synthetic
polylines are invented examples, not Census data or surveyed road locations.
Expected provider bytes are retained separately from synthetic capture identity;
both fixtures report `REFERENCE_BYTES_NOT_MATCHED`.

The [contract](../../contracts/domains/roads-rail-trade/tiger_roads_ingest_candidate.md)
defines byte identity, canonical UTC times, strict output, archive budgets and
finite holds. Source ZIP size is at most 2 MiB; this deliberately does not cover
all real county packages. The existing connector has a larger separate envelope.
No files are extracted. Every member's CRC is read, including geometry bytes;
individual SHP geometry records and SHX offsets are not interpreted. This is
not geometry, topology, CRS transformation or package-completeness qualification.
It does not acquire from Census, retry, schedule, store, project a road graph,
activate the proposed domain descriptor, release or publish.

## Proof and review

The [dedicated workflow](../../.github/workflows/tiger-roads-pipeline.yml)
uses hash-locked test/connector profiles and the Python network guard on 3.11
and 3.12. It checks the declaration, existing inspector tests, positive/negative
intake tests and both CLI goldens. The offline aggregate pipeline workflow also
collects the new tests. Local proof, hosted CI, main delivery, source admission,
geometry qualification and deployment remain separate evidence lanes.

Human source/rights, sensitivity, contract/schema and validation review remain
required. The final route stays held even if future supplied bytes exactly match
the provider manifest. Roll back with a normal reviewed revert; preserve the
historical authoring receipts and unchanged Census reference inventory.
