<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-openstreetmap-tests-readme
title: connectors/openstreetmap/tests/ — OpenStreetMap Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · OpenStreetMap steward · Roads-Rail-Trade steward · Settlements-Infrastructure steward · Spatial Foundation steward · Rights steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public-doctrine; test-boundary; no-live-by-default; attribution-required; source-admission-only
related:
  - ../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/sources/catalog/README.md
  - ../../../docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../../docs/sources/catalog/OPEN-QUESTIONS.md
  - ../../../docs/architecture/source-roles.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, openstreetmap, osm, tests, no-network, fixtures, volunteered-geographic-information, attribution, odbl, source-admission, raw, quarantine, rights, sensitivity, governance]
notes:
  - "Replaces greenfield stub for OpenStreetMap connector tests."
  - "Tests are no-network by default and must not require live OSM API, Overpass, provider extracts, credentials, private sessions, or source-side side effects."
  - "Fixtures must be synthetic, minimized, redacted, or explicitly approved snapshots with provider/extract/query metadata, source date, digest, rights posture, and fixture purpose."
  - "Tests verify connector safety and admission envelopes; they do not prove OSM source authority, legal access, ownership, current operation, completeness, catalog closure, proof closure, or release readiness."
  - "Rights, attribution, ODbL/share-alike, service-use, source-role, freshness, completeness, and sensitivity gates must fail closed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# OpenStreetMap Connector Tests

> Test boundary for the OpenStreetMap connector lane under `connectors/openstreetmap/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Network: no live by default" src="https://img.shields.io/badge/network-no__live__by__default-orange">
  <img alt="Fixtures: approved only" src="https://img.shields.io/badge/fixtures-approved__only-blue">
  <img alt="Rights: attribution gate" src="https://img.shields.io/badge/rights-attribution__gate-orange">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
</p>

`connectors/openstreetmap/tests/`

## Scope

`connectors/openstreetmap/tests/` is the test lane for OpenStreetMap connector code and source-admission behavior.

These tests may verify import safety, no-network defaults, fixture loading, provider/extract manifest parsing, query construction, element parsing, native tag preservation, geometry metadata preservation, version/source-date handling, attribution and ODbL review gates, service-use safeguards, sensitivity flags, digest generation, schema-drift detection, finite error behavior, and raw/quarantine admission-envelope construction.

They must not become OpenStreetMap source-family doctrine, source descriptor authority, rights policy authority, sensitivity policy authority, fixture authority, proof authority, release authority, pipeline authority, public API behavior, public UI behavior, public map authority, routing authority, access truth, ownership truth, completeness proof, or publication evidence by themselves.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/openstreetmap/tests/`  
> **Truth posture:** the path exists in the repository as this README; actual test files, fixture inventory, pytest markers, CI wiring, live-test opt-ins, source descriptors, provider/extract policy, and coverage remain `NEEDS VERIFICATION`.

---

## Repo fit

```text
connectors/
└── openstreetmap/
    ├── README.md
    └── tests/
        └── README.md
```

Related responsibility roots:

```text
connectors/openstreetmap/                 # draft OpenStreetMap connector lane
connectors/openstreetmap/tests/           # this test lane
docs/domains/roads-rail-trade/            # roads, trails, routing-context, rail/trade adjacency
docs/domains/settlements-infrastructure/  # places, amenities, facilities, infrastructure context
docs/sources/catalog/                     # source-family/product doctrine; OSM page currently NEEDS VERIFICATION
data/registry/sources/                    # source descriptors and activation state
data/raw/                                 # raw staged source outputs by owning domain
data/quarantine/                          # held material requiring source/role/rights/sensitivity review
data/receipts/                            # ingest, checksum, query, transform, and review receipts
data/proofs/                              # EvidenceBundles and proof packs
policy/rights/                            # ODbL, attribution, share-alike, and source-use review
policy/sensitivity/                       # exact-location and release rules
release/                                  # release decisions, manifests, rollback, correction state
```

---

## Test contract

Default test behavior:

- no live network calls;
- no credentials, tokens, cookies, or private sessions;
- no source-side edits or other upstream side effects;
- no lifecycle writes outside isolated temporary directories;
- no public tiles, public API responses, public UI state, routing output, access claims, ownership claims, or release artifacts;
- fixtures are synthetic, minimized, redacted, or explicitly approved;
- tests fail closed when rights, attribution, ODbL review, service-use posture, source role, freshness, completeness, sensitivity, schema, or lineage is unclear.

Live integration checks, if ever added, must be opt-in, clearly marked, rate-limited, descriptor-gated, non-mutating, and excluded from default CI.

---

## Expected test groups

Actual test files are **NEEDS VERIFICATION**. A future suite may include:

```text
connectors/openstreetmap/tests/
├── README.md
├── fixtures/
│   ├── synthetic/
│   ├── extracts/
│   └── queries/
├── test_import_safety.py
├── test_descriptor_gates.py
├── test_rights_attribution.py
├── test_service_use_guards.py
├── test_fixture_metadata.py
├── test_element_parser.py
├── test_tag_preservation.py
├── test_geometry_metadata.py
├── test_digest_envelopes.py
└── test_anti_collapse.py
```

| Test group | Purpose |
|---|---|
| Import safety | Prove imports do not call network, read secrets, write lifecycle stores, publish artifacts, or emit public claims. |
| Descriptor gates | Prove live access and admission require source descriptor references and activation decisions. |
| Rights and attribution | Prove attribution, ODbL review, derivative-database review, and provider terms fail closed. |
| Service-use guards | Prove request helpers respect no-live defaults, explicit opt-in, rate-limit posture, user-agent posture, and non-mutating behavior. |
| Fixture metadata | Prove every fixture has source/extract/query metadata, source date, digest, rights posture, sensitivity posture, and purpose. |
| Element parser | Preserve element type, id, version, timestamp, tags, geometry, relation context, and source-date metadata. |
| Tag preservation | Preserve native OSM tags without silently converting them into KFM domain truth. |
| Geometry metadata | Preserve geometry type, CRS/bounds metadata, simplification/generalization status, and topology warnings. |
| Digest and envelope | Prove query, extract, response, fixture, and admission-envelope digests are stable and traceable. |
| Anti-collapse | Prove OSM records are not promoted into official, access, ownership, routing, current-operation, or completeness truth by tests. |

---

## Fixture rules

Fixtures must be governed like source-admission test material.

Required fixture metadata:

- fixture purpose;
- fixture source type: synthetic, redacted snapshot, approved extract, or approved query result;
- provider/extract/query reference when applicable;
- source date and retrieval date when applicable;
- digest;
- rights and attribution posture;
- ODbL/share-alike review posture;
- sensitivity review posture;
- minimization/redaction note;
- expected parser behavior;
- reason the fixture is safe for repository use.

Do not commit credentials, cookies, private session material, uncontrolled full-size datasets, high-risk exact-location material, or unreviewed third-party extracts as fixtures.

---

## Anti-collapse tests

Tests should explicitly reject common role and authority collapses.

| Collapse risk | Test expectation |
|---|---|
| OSM as official government authority | Tests do not treat volunteered edits as official records. |
| OSM as access truth | Tests do not infer permissions or public accessibility from feature presence. |
| OSM as ownership truth | Tests do not infer parcel, facility, or operator ownership from tags. |
| OSM as routing authority | Tests do not emit routing guidance or route-safe claims. |
| OSM as complete inventory | Tests preserve completeness caveats; absence is not proof of absence. |
| OSM tags as KFM objects | Tests preserve native tags until downstream contracts and receipts map them. |
| Fixture as source authority | Fixture success does not imply source activation, rights clearance, catalog closure, or release readiness. |
| Public surface from connector test | Tests must not create public tiles, public API responses, public UI state, or release manifests. |

---

## Validation

Before relying on this test lane, verify actual test files, pytest markers, no-network enforcement, fixture inventory, descriptor-gate fixtures, rights/attribution tests, service-use tests, parser coverage, digest stability, schema-drift tests, CI wiring, and live-test opt-in safeguards.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual test files and fixture directories are inventoried.
- [ ] Default tests run without network, secrets, private sessions, upstream side effects, or lifecycle writes outside temp directories.
- [ ] Fixture metadata includes purpose, source/extract/query reference, source date, digest, rights posture, sensitivity posture, and expected behavior.
- [ ] Rights, attribution, ODbL/share-alike, service-use, source-role, freshness, completeness, and sensitivity gates fail closed.
- [ ] Element parsers preserve native OSM identity, version, tags, geometry, relation context, source date, source URL, and digest.
- [ ] Tests cover malformed inputs, stale extracts, missing rights review, role collapse, schema drift, sensitive-domain joins, and public-release misuse paths.
- [ ] Outputs are verified to remain temporary test artifacts or raw/quarantine admission envelopes only.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/openstreetmap/tests/` is for OpenStreetMap connector tests only. It is not source-family doctrine, source descriptor authority, rights policy, sensitivity policy, fixture authority, proof closure, release authority, public map authority, public API behavior, public UI behavior, routing authority, access truth, ownership truth, completeness proof, or publication evidence.

<p align="right"><a href="#top">Back to top</a></p>
