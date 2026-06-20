<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-tests-readme
title: connectors/nrcs/tests/ — NRCS Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · NRCS steward · Soil steward · Agriculture steward · Hydrology steward · Ecology steward · Climate steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public-doctrine; test-boundary; no-live-by-default; source-admission-only
related:
  - ../README.md
  - ../src/README.md
  - ../src/nrcs/README.md
  - ../sda/README.md
  - ../scan/README.md
  - ../ssurgo/README.md
  - ../gssurgo/README.md
  - ../gnatsgo/README.md
  - ../../nrcs-ssurgo/README.md
  - ../../nrcs-scan/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/nrcs.md
  - ../../../docs/sources/catalog/nrcs/README.md
  - ../../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../../docs/sources/catalog/nrcs/scan-soil-climate.md
  - ../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../docs/domains/soil/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, nrcs, tests, no-network, fixtures, source-admission, raw, quarantine, descriptor-gates, rights, sensitivity, ssurgo, gssurgo, gnatsgo, sda, scan, soil, governance]
notes:
  - "Replaces greenfield stub for NRCS connector tests."
  - "Tests are no-network by default and must not require live NRCS credentials, private sessions, or source-side side effects."
  - "Fixtures must be synthetic, minimized, redacted, or explicitly approved snapshots with source URL/query, digest, and fixture purpose."
  - "Tests verify connector safety and admission envelopes; they do not prove NRCS product truth, SourceDescriptor activation, catalog closure, proof closure, release readiness, public API behavior, or public UI behavior."
  - "NRCS products are multi-product and role-specific; tests must prevent role, cadence, scale, and lineage collapse."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Connector Tests

> Test boundary for the NRCS connector family under `connectors/nrcs/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Network: no live by default" src="https://img.shields.io/badge/network-no__live__by__default-orange">
  <img alt="Fixtures: approved only" src="https://img.shields.io/badge/fixtures-approved__only-blue">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/nrcs/tests/`

## Scope

`connectors/nrcs/tests/` is the test lane for NRCS connector-family code and source-admission behavior.

These tests may verify import safety, no-network defaults, fixture loading, bounded request construction, descriptor gating, product parser behavior, source-role preservation, freshness checks, rights/citation handling, sensitivity flags, digest generation, schema-drift detection, finite error behavior, and raw/quarantine admission-envelope construction.

They must not become NRCS source-family truth, NRCS product doctrine, SourceDescriptor authority, policy authority, schema authority, fixture authority, proof authority, release authority, pipeline authority, public API behavior, public UI behavior, or publication evidence by themselves.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nrcs/tests/`  
> **Truth posture:** the path exists in the repository as this README; actual test files, fixtures, markers, CI wiring, live-test opt-ins, source descriptors, and product coverage remain `NEEDS VERIFICATION`.

---

## Repo fit

```text
connectors/
└── nrcs/
    ├── README.md
    ├── src/
    │   └── nrcs/
    │       └── README.md
    ├── tests/
    │   └── README.md
    ├── sda/
    │   └── README.md
    ├── scan/
    │   └── README.md
    ├── ssurgo/
    │   └── README.md
    ├── gssurgo/
    │   └── README.md
    └── gnatsgo/
        └── README.md
```

Related responsibility roots:

```text
connectors/nrcs/                         # canonical NRCS connector-family lane
connectors/nrcs/src/                     # source-code root
connectors/nrcs/src/nrcs/                # importable package boundary
connectors/nrcs/tests/                   # this test lane
docs/sources/catalog/nrcs.md             # NRCS source-family profile
docs/sources/catalog/nrcs/               # NRCS product doctrine
data/registry/sources/                   # source descriptors and activation state
data/raw/                                # raw staged source outputs by owning domain
data/quarantine/                         # held material requiring source/role/rights/sensitivity review
data/receipts/                           # ingest, checksum, query, package, transform, and aggregation receipts
data/proofs/                             # EvidenceBundles and proof packs
policy/rights/                           # terms, attribution, and source-use review
policy/sensitivity/                      # release and sensitivity review rules
release/                                 # release decisions, manifests, rollback, correction state
```

---

## Test contract

Default test behavior:

- no live network calls;
- no NRCS credentials, cookies, tokens, or private sessions;
- no source-side side effects;
- no writes to `data/raw/`, `data/quarantine/`, `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/`, `data/receipts/`, `data/proofs/`, or `release/` except through isolated temporary directories;
- no publication, public API, public UI, public tile, or public-claim generation;
- fixtures are synthetic, minimized, redacted, or explicitly approved;
- tests fail closed when source role, rights, sensitivity, freshness, schema, or lineage is unclear.

Live integration checks, if ever added, must be opt-in, clearly marked, rate-limited, descriptor-gated, non-mutating, and excluded from default CI.

---

## Expected test groups

Actual test files are **NEEDS VERIFICATION**. A future suite may include:

```text
connectors/nrcs/tests/
├── README.md
├── fixtures/
│   ├── sda/
│   ├── scan/
│   ├── ssurgo/
│   ├── gssurgo/
│   └── gnatsgo/
├── test_import_safety.py
├── test_descriptor_gates.py
├── test_rights_sensitivity.py
├── test_digest_envelopes.py
├── test_sda_parser.py
├── test_scan_parser.py
├── test_ssurgo_manifest.py
├── test_gssurgo_metadata.py
└── test_gnatsgo_metadata.py
```

| Test group | Purpose |
|---|---|
| Import safety | Prove package import does not call network, read secrets, write lifecycle stores, publish artifacts, or emit public claims. |
| Descriptor gates | Prove live access and admission require source descriptor references and activation decisions. |
| Rights and sensitivity | Prove rights/citation and Tribal/private-land/ecology/cultural/exact-location review gates fail closed. |
| Digest and envelope | Prove query, response, package, manifest, fixture, and output envelope digests are stable and traceable. |
| SDA parser | Preserve query text, parameters, endpoint, table names, row counts, MUKEY/join fields, schema-drift findings, and digest. |
| SCAN parser | Preserve station ID, network, timestamp, sensor depth, variable, units, quality flags, cadence, freshness, and Tribal SCAN posture. |
| SSURGO manifest/parser | Preserve survey area, package date, files, spatial layers, table names, MUKEY/COKEY/CHKEY lineage, scale caveats, and digest. |
| gSSURGO metadata | Preserve product identity, native grid, CRS, resolution, MUKEY joins, source-survey vintage, SoilTimeCaveat, and digest. |
| gNATSGO metadata | Preserve product identity, native grid, CRS, resolution, product-native join fields, national-scale/generalization caveats, and digest. |

---

## Fixture rules

Fixtures must be governed like source-admission test material.

Required fixture metadata:

- product lane;
- fixture purpose;
- source URL or query when derived from a public source;
- retrieval date or synthetic creation date;
- digest;
- rights/citation posture;
- sensitivity review posture;
- redaction/minimization note;
- expected parser behavior;
- reason the fixture is safe for repository use.

Do not commit credentials, cookies, private downloads, producer records, private landowner records, unpublished source material, uncontrolled full-size datasets, or sensitive precise-location material as fixtures.

---

## Anti-collapse tests

Tests should explicitly reject common role and authority collapses.

| Collapse risk | Test expectation |
|---|---|
| NRCS-wide role collapse | Product-specific source roles, cadence, scale, and caveats remain separate. |
| SDA query as full source package | Query scope and parameters remain visible; coverage is not overstated. |
| SCAN station as area truth | Station readings do not become county, watershed, or raster truth. |
| SSURGO package as processed soil truth | Source packages do not become domain-normalized output without downstream pipeline receipts. |
| gSSURGO/gNATSGO as field verification | Grid cells are not treated as current point-observed field conditions. |
| WSS session as canonical source | WSS session outputs are not silently promoted without accepted source posture. |
| Conservation standard as local implementation proof | Technical standards do not prove practice existence on private land. |
| Fixture as source authority | Fixture success does not imply source activation, rights clearance, catalog closure, or release readiness. |
| Public surface from connector test | Tests must not create public tiles, public API responses, public UI state, or release manifests. |

---

## Validation

Before relying on this test lane, verify actual test files, pytest markers, no-network enforcement, fixture inventory, descriptor-gate fixtures, product parser coverage, rights/sensitivity tests, digest stability, schema-drift tests, CI wiring, and live-test opt-in safeguards.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual test files and fixture directories are inventoried.
- [ ] Default tests run without network, secrets, private sessions, source-side effects, or lifecycle writes outside temp directories.
- [ ] Import-safety tests cover `connectors/nrcs/src/` and `connectors/nrcs/src/nrcs/`.
- [ ] Descriptor, rights, citation, freshness, and sensitivity gates fail closed.
- [ ] Product parsers preserve native fields, caveats, lineage, query/package/station/raster metadata, and digests.
- [ ] Tests cover malformed inputs, stale sources, role collapse, schema drift, missing quality flags, missing lineage, and public-release misuse paths.
- [ ] Fixture metadata is complete and reviewed.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/nrcs/tests/` is for NRCS connector tests only. It is not NRCS source-family truth, product doctrine, SourceDescriptor authority, schema authority, policy authority, proof closure, release authority, public map authority, public API behavior, public UI behavior, pipeline authority, fixture authority, or publication evidence.

<p align="right"><a href="#top">Back to top</a></p>
