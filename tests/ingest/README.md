<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ingest-readme
title: tests/ingest README
type: README
version: v0.2
status: draft; bounded executable coverage
owners:
  - OWNER_TBD - tooling QA (responsible owner; identity NEEDS VERIFICATION)
required_review_roles:
  - Applicable domain steward
  - Applicable source steward
created: 2026-08-02
updated: 2026-08-31
policy_label: repository-facing; synthetic-fixtures; no-network; no-publication
owning_root: tests/
responsibility: Test ingest-adjacent watcher and preflight helpers without performing source access, lifecycle mutation, promotion, release, or publication.
truth_posture: cite-or-abstain; a passing watcher or preflight test supports only its named assertion, synthetic fixture, and checked revision and does not establish source truth, admission, rights, review, lifecycle mutation, promotion, release, or publication
related:
  - ../../tools/ingest/README.md
  - ./aqs_watch/test_aqs_site_delta.py
  - ./cdl_watch/README.md
  - ./csv_geojson_preflight/test_preflight.py
  - ./hydrology_watch/test_nhdplus_network_revision.py
  - ./ssurgo_watch/README.md
notes:
  - "The executable children are five frozen synthetic watcher or preflight lanes containing six test modules."
  - "Passing tests prove only local helper behavior; they do not admit a source or create evidence, receipt, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Ingest-adjacent helper tests

`tests/ingest/` contains bounded, deterministic tests for repository-owned
watcher and preflight helpers. Inputs are synthetic and execution is designed
for no-network validation. This lane does not contact a source, admit data, move
an artifact through the KFM lifecycle, or create a governed release or public
surface.

## Authority boundary

Test success is evidence about the inspected helper and covered fixtures only.
It does not establish source availability, rights, freshness, real-world
correctness, evidence sufficiency, policy clearance, accountable review,
promotion, release, publication, or rollback readiness. Outcomes such as
`PROPOSED_WORK_RECORD` remain review signals; they are not lifecycle writes or
release decisions.

## Direct children

```text
tests/ingest/
├── README.md
├── aqs_watch/
├── cdl_watch/
├── csv_geojson_preflight/
├── hydrology_watch/
└── ssurgo_watch/
```

The five child directories contain six executable test modules. CDL and SSURGO
have child READMEs; the other entries below link directly to their executable
tests so navigation does not imply a nonexistent document.

## Executable inventory

| Child lane | Test module and implementation | Confirmed boundary |
|---|---|---|
| AQS site delta | [`test_aqs_site_delta.py`](aqs_watch/test_aqs_site_delta.py) tests [`aqs_site_delta.py`](../../tools/ingest/aqs_watch/aqs_site_delta.py). | Ten pytest cases cover deterministic site comparison, absence handling, schema compatibility, change classifications, non-echoing coordinate protection, duplicate identity, and invalid-root failure. |
| CDL watcher | [`cdl_watch/README.md`](cdl_watch/README.md) and [`test_cdl_watch.py`](cdl_watch/test_cdl_watch.py) test [`cdl_watch.py`](../../tools/ingest/cdl_watch/cdl_watch.py). | A `unittest` suite covers the frozen material-change profile, finite outcomes, parser and integer bounds, deterministic reports, no-network behavior, CLI polarity, and create-only external output. |
| CSV/GeoJSON preflight | [`test_preflight.py`](csv_geojson_preflight/test_preflight.py) tests [`preflight.py`](../../tools/ingest/csv_geojson_preflight/preflight.py). | Ten pytest cases cover deterministic normalization candidates, exact header and profile contracts, schema-valid minimized output, invalid-input quarantine, symlink denial, atomic create-only output, and no network or lifecycle clients. |
| NHDPlus network revision | [`test_nhdplus_network_revision.py`](hydrology_watch/test_nhdplus_network_revision.py) tests [`nhdplus_network_revision.py`](../../tools/ingest/hydrology_watch/nhdplus_network_revision.py). | Eight pytest cases cover deterministic flowline comparison, bounded geometry and linear-reference changes, added identifiers, duplicate identity, and suppression of raw centroid coordinates. |
| SSURGO watcher and SDA micro snapshot | [`ssurgo_watch/README.md`](ssurgo_watch/README.md), [`test_ssurgo_watch.py`](ssurgo_watch/test_ssurgo_watch.py), and [`test_sda_micro_snapshot.py`](ssurgo_watch/test_sda_micro_snapshot.py) test the SSURGO watcher helpers under [`tools/ingest/ssurgo_watch/`](../../tools/ingest/ssurgo_watch/README.md). | The suites cover package, schema, constraint, table, geometry, derived-state, and SDA snapshot changes; deterministic hashes and reports; input and output bounds; no-network behavior; and fail-closed validation. |

## Fixture placement and safety

| Lane | Fixture location |
|---|---|
| AQS | [`tests/ingest/aqs_watch/fixtures/`](aqs_watch/fixtures/) |
| CDL | [`tests/ingest/cdl_watch/fixtures/`](cdl_watch/fixtures/) |
| CSV/GeoJSON | [`fixtures/ingest/csv_geojson_preflight/`](../../fixtures/ingest/csv_geojson_preflight/) |
| NHDPlus | [`tests/ingest/hydrology_watch/fixtures/`](hydrology_watch/fixtures/) |
| SSURGO and SDA | [`tests/ingest/ssurgo_watch/fixtures/`](ssurgo_watch/fixtures/) |

Every fixture must remain obviously synthetic, public-safe, deterministic, and
free of credentials, private records, live source payloads, and harmful
precision. Test-local fixtures are not RAW inputs, source captures,
EvidenceBundles, receipts, proofs, promotion candidates, or published
artifacts.

## Run the tests

From the repository root, pytest can collect all six modules, including the two
`unittest.TestCase` suites:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 pytest -q tests/ingest
```

Focused local equivalents of the hosted commands are:

```bash
python -m pytest tests/ingest/aqs_watch/test_aqs_site_delta.py
python -m unittest tests.ingest.cdl_watch.test_cdl_watch --verbose
python -m pytest tests/ingest/csv_geojson_preflight
python -m pytest tests/ingest/hydrology_watch/test_nhdplus_network_revision.py
python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
python -m pytest tests/ingest/ssurgo_watch/test_sda_micro_snapshot.py
```

These commands may create bounded temporary files. They must not contact a
source or write into `data/`, `release/`, policy, proof, receipt, or
publication lanes.

## Hosted workflow binding

| Test surface | Confirmed workflow |
|---|---|
| AQS site delta | [`atmosphere-aqs-site-delta.yml`](../../.github/workflows/atmosphere-aqs-site-delta.yml) |
| CDL watcher | [`domain-agriculture.yml`](../../.github/workflows/domain-agriculture.yml) |
| CSV/GeoJSON preflight | [`csv-geojson-preflight.yml`](../../.github/workflows/csv-geojson-preflight.yml) |
| NHDPlus network revision | [`hydrology-nhdplus-network-revision.yml`](../../.github/workflows/hydrology-nhdplus-network-revision.yml) |
| SSURGO watcher | [`domain-soil.yml`](../../.github/workflows/domain-soil.yml) |
| SDA micro snapshot | [`soil-ssurgo-sda-micro-snapshot.yml`](../../.github/workflows/soil-ssurgo-sda-micro-snapshot.yml) |

The dedicated AQS, CSV/GeoJSON, NHDPlus, and SDA workflows include the owning
test paths in their path filters, but not this parent README. A parent-only
documentation change therefore does not trigger those four workflows. The
Agriculture and Soil domain workflows run the CDL and SSURGO watcher suites
respectively. Workflow success applies only to the checked-out revision and
executed commands; it is not proof that a workflow is required, that every
ingest test ran, or that a live ingest control exists.

## Interpret failures

| Failure area | First investigation |
|---|---|
| Fixture validation | Check fixture shape, identity uniqueness, canonical ordering, bounds, and declared synthetic posture before changing expected outcomes. |
| Determinism or hashing | Check input ordering, normalized fields, hash roles, report serialization, and whether retrieval-only metadata entered material comparison. |
| Material-change outcome | Reconcile the helper's frozen comparison profile and finite outcome precedence; do not infer a new operational threshold from a failing test. |
| Privacy or precision | Treat raw coordinate echo, live-source fields, credentials, private records, or harmful precision as fail-closed safety defects. |
| Network or output guard | Check for new clients, ambient network calls, repository writes, overwrite behavior, or lifecycle/release side effects. |
| Hosted workflow only | Compare the exact workflow command, dependency installation, path filters, and checked-out SHA with the focused local command. |

Do not weaken a fail-closed assertion merely to make a fixture or workflow pass.
An intentional contract change should update the implementation, fixtures,
tests, and owning documentation together.

## Maintenance checklist

- Keep the direct-child and executable inventories synchronized with
  `tests/ingest/`.
- Link every new test module to its implementation, fixture home, and confirmed
  workflow binding or label the binding `UNKNOWN`.
- Keep test fixtures synthetic and separate from canonical source, evidence,
  receipt, proof, release, and published stores.
- Document no-network and output-write expectations for each new helper.
- Preserve the distinction between comparison signals, proposed work,
  accountable review, lifecycle mutation, promotion, release, and publication.

[Back to top](#top)
