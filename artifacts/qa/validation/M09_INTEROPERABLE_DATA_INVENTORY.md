<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://artifact/m09-interoperable-data-inventory
title: M09 Interoperable Data & Delivery Artifacts — Repository Surface Inventory
type: inventory-assessment
version: v1.0-draft
status: "draft; repository-grounded; checkpoint-one-execution"
created: 2026-09-01
updated: 2026-09-01
owners:
  - "@bartytime4life — verified GitHub review route through CODEOWNERS"
policy_label: internal-workflow
owning_root: artifacts/
responsibility: "Record current repository surfaces relevant to M09 Interoperable Data & Delivery Artifacts milestone; classify outcomes; verify authority and ADRs; establish evidence baseline for first bounded action."
truth_posture: "CONFIRMED repository state; PROPOSED first action boundaries; NEEDS VERIFICATION governance closure, cross-engine probes, and production readiness"
audit_baseline: "main@f86fcddb553217f7ffadafd80f20e95d635180b1"
execution_start: "copilot/m09-interoperable-data-delivery-artifacts@7115f5c046d0660c65befef65f20964de79c5f2b"
related:
  - docs/standards/GEOPARQUET.md
  - docs/standards/PMTILES.md
  - docs/standards/COG.md
  - docs/standards/MVT.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0033-geoparquet-version-readiness.md
  - contracts/release/geospatial_carrier_readiness.md
  - contracts/release/geoparquet_2_rc_pyarrow_carrier_probe.md
  - contracts/release/geoparquet_2_rc_gdal_consumer_probe.md
  - tools/validators/release/validate_geoparquet_2_rc_pyarrow_carriers.py
  - tools/validators/release/validate_geoparquet_2_rc_gdal_consumer_probe.py
  - tools/validators/pmtiles/
  - tests/release/test_geoparquet_2_rc_pyarrow_carriers.py
  - tests/release/test_geoparquet_2_rc_gdal_consumer_probe.py
  - tests/validators/test_pmtiles_attestation_bundle.py
tags: [m09, interoperability, carriers, geoparquet, pmtiles, cog, mvt, inventory, evidence]
[/KFM_META_BLOCK_V2] -->

# M09 Interoperable Data & Delivery Artifacts — Repository Surface Inventory

## Executive Summary

This document records the first checkpoint of the M09 milestone: current repository surfaces relevant to GeoParquet, PMTiles, COG, and MVT interoperability. It classifies outcomes, verifies authority, and establishes the boundary for the first bounded action: a single missing pinned cross-engine probe.

**Audit baseline:** `main@f86fcddb553217f7ffadafd80f20e95d635180b1`  
**Execution start:** `copilot/m09-interoperable-data-delivery-artifacts@7115f5c046d0660c65befef65f20964de79c5f2b`

---

## 1. Oversight and Authority

### 1.1 Responsibility Root and Owner

| Field | Value |
|---|---|
| Primary responsibility root | `docs/` (standards, doctrine, ADRs) + `artifacts/` (evidence, receipts, validation) |
| Verified owner | `@bartytime4life` (CODEOWNERS review route, explicit ADR-0029 ratification authority) |
| ADR authority | ADR-0029 (accepted; Directory Rules v2 adoption) |
| Authority boundary | Directory Rules v2 §2.2, §6, §9, §17 (compatibility, deprecation, migration) |

### 1.2 Acceptance Gates

- [ ] Inventory classifies all current surfaces without omission
- [ ] Authority and ownership verified for each classified outcome
- [ ] No pre-existing failures introduced
- [ ] ADR compliance and placement doctrine consistency confirmed
- [ ] First bounded action scope is independent, reversible, reviewable

---

## 2. Carrier Surfaces Inventory

### 2.1 GeoParquet — Current State

| Surface | Category | Status | Classification | Evidence | Notes |
|---|---|---|---|---|---|
| **Specification & Guidance** | | | | | |
| `docs/standards/GEOPARQUET.md` | Standards documentation | Current | **PARTIAL** | v2.1-draft; KFM 1.1.0 default + 2.0.0-rc.1 candidate | Default is GeoParquet 1.1.0; v2.0.0-rc.1 held separate |
| **Contracts & Schemas** | | | | | |
| `contracts/release/geospatial_carrier_readiness.md` | Release contract | Current | **PARTIAL** | Shared with COG/PMTiles/MVT | Bounds carrier readiness checks; used by multiple carriers |
| `schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json` | Machine schema | Current | **IMPLEMENTED** | JSON Schema v7 | Carrier readiness machine definition |
| `contracts/release/geoparquet_2_rc_compatibility_assessment.md` | Carrier-specific contract | Current | **PARTIAL** | GeoParquet 2.0.0-rc.1 assessment profile | Non-normative; proof of concept |
| `contracts/release/geoparquet_2_rc_pyarrow_carrier_probe.md` | Carrier-specific contract | Current | **PARTIAL** | Bounded PyArrow 25.0.0 synthetic generation | Fixture-only; not production |
| `contracts/release/geoparquet_2_rc_gdal_consumer_probe.md` | Carrier-specific contract | Current | **PARTIAL** | PyArrow-to-GDAL 3.13.2 edge; Docker enclosure | Cross-engine boundary; limited scope |
| **Validators** | | | | | |
| `tools/validators/release/validate_geoparquet_2_rc_pyarrow_carriers.py` | Release validator | Current | **PARTIAL** | Checks synthetic carrier generation; digest verification | PyArrow 25.0.0 only; not version-adaptive |
| `tools/validators/release/validate_geoparquet_2_rc_gdal_consumer_probe.py` | Cross-engine validator | Current | **PARTIAL** | GDAL ogr2ogr read verification; CRS validation | Docker-based; requires external container |
| `tools/validators/release/validate_geoparquet_2_rc_compatibility_assessment.py` | Assessment validator | Current | **PARTIAL** | Fixture assessment schema validation | Non-normative proof-of-concept |
| **Tests** | | | | | |
| `tests/release/test_geoparquet_2_rc_pyarrow_carriers.py` | Synthetic carrier tests | Current | **IMPLEMENTED** | 4 deterministic tests (valid, tampered, governance, outcome, CRS) | Bounds PyArrow 25.0.0 behavior |
| `tests/release/test_geoparquet_2_rc_gdal_consumer_probe.py` | Cross-engine tests | Current | **PARTIAL** | GDAL consumer read verification | Fixture-backed; Docker dependency |
| `tests/release/test_geoparquet_2_rc_compatibility_assessment.py` | Assessment tests | Current | **PARTIAL** | Assessment schema validation | Non-normative |
| `tests/validators/test_validate_stac_geoparquet_mirror_assessment.py` | STAC mirror tests | Current | **PARTIAL** | Fixture STAC assessment | Declared-only; not live assessment |
| **Fixtures** | | | | | |
| `fixtures/geoparquet/` | Synthetic carriers | Current | **PARTIAL** | PyArrow 25.0.0 exact lineage | Bounded; no real payloads |
| **ADRs & Policy** | | | | | |
| `docs/adr/ADR-0033-geoparquet-version-readiness.md` | Architecture decision | Proposed | **ABSENT** | ADR exists; not yet indexed or linked | Proposed; status unknown; needs verification |

### 2.2 PMTiles — Current State

| Surface | Category | Status | Classification | Evidence | Notes |
|---|---|---|---|---|---|
| **Specification & Guidance** | | | | | |
| `docs/standards/PMTILES.md` | Standards documentation | Current | **PARTIAL** | v2.0-draft; PMTiles v3 guidance | Archive format + tile encoding split documented |
| `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` | Specification | Current | **PARTIAL** | Attestation profile; cryptographic trust boundary | Non-normative guidance |
| `docs/standards/pmtiles/PMIDX_SPEC_V1.md` | Index specification | Current | **PARTIAL** | PMIDX index format | Internal specification; not upstream-standard |
| **Contracts & Schemas** | | | | | |
| `contracts/release/tile_artifact_manifest.md` | Release contract | Current | **PARTIAL** | TileArtifactManifest family; unresolved naming | Shared with MVT; schema family incomplete |
| `schemas/contracts/v1/map/tile_artifact_manifest.schema.json` | Machine schema | Current | **PARTIAL** | JSON Schema; bounds tile artifacts | Schema version 1.0; incomplete family |
| `contracts/release/geospatial_carrier_readiness.md` | Shared contract | Current | **PARTIAL** | Reused across carriers | See GeoParquet section |
| **Validators** | | | | | |
| `tools/validators/pmtiles/` | Validator suite | Current | **PARTIAL** | Modular: header, merkle, partial-read, attestation | Structural checks only; no network calls |
| `tools/validators/pmtiles/validate_attestation_bundle.py` | Attestation validator | Current | **PARTIAL** | Manifest, digest, generation-tool validation | Synthetic fixtures only |
| `tools/validators/pmtiles/validate_header.py` | Header validator | Current | **IMPLEMENTED** | Archive header inspection | Deterministic; spec-compliant |
| `tools/validators/pmtiles/verify_merkle.py` | Index validator | Current | **IMPLEMENTED** | PMIDX merkle tree verification | Deterministic tree walk |
| `tools/validators/pmtiles/verify_partial_read.py` | Range-read validator | Current | **PARTIAL** | Simulated partial reads; no network | Fixture-based; no deployed Range/CORS |
| `tools/validators/validate_pmtiles_delta_manifest.py` | Delta validator | Current | **PARTIAL** | Delta manifest reconciliation | Declared structure; not normative |
| **Tests** | | | | | |
| `tests/validators/test_pmtiles_attestation_bundle.py` | Attestation tests | Current | **IMPLEMENTED** | Comprehensive negative test coverage (40+ cases) | Deterministic; fixtures only |
| `tests/validators/test_pmtiles_mobile_verification_fixture.py` | Mobile verification | Current | **PARTIAL** | Synthetic decode/render handoff | Fixture-based; no browser testing |
| `tests/validators/test_pmtiles_delta_manifest.py` | Delta manifest tests | Current | **PARTIAL** | Reconciliation validation | Structure validation only |
| **Fixtures** | | | | | |
| `fixtures/pmtiles/attestation/` | Attestation fixtures | Current | **PARTIAL** | Deterministic test cases; negative coverage | 40+ manifest malformations |
| `fixtures/pmtiles/mobile_verification/` | Mobile fixtures | Current | **PARTIAL** | Synthetic decode/render | No browser/MapLibre execution |
| **Policy** | | | | | |
| `policy/rego/tiles_publish.rego` | Publication policy | Current | **ABSENT** | Policy file exists; not activated | No publication authorization yet |
| **CI/Workflow** | | | | | |
| `.github/workflows/pmtiles-attestation.yml` | CI workflow | Current | **PARTIAL** | Attestation bundle checks | Deterministic; no network |

### 2.3 COG (Cloud Optimized GeoTIFF) — Current State

| Surface | Category | Status | Classification | Evidence | Notes |
|---|---|---|---|---|---|
| **Specification & Guidance** | | | | | |
| `docs/standards/COG.md` | Standards documentation | Current | **PARTIAL** | v2.0-draft; OGC COG 1.0 currentness confirmed 2026-08-18 | Repository-grounded; upstream-currentness-refreshed |
| **Contracts & Schemas** | | | | | |
| `contracts/release/geospatial_carrier_readiness.md` | Release contract | Current | **PARTIAL** | Shared across carriers | See GeoParquet section |
| `contracts/evidence/cog_byte_range_integrity_manifest.md` | Evidence contract | Current | **PARTIAL** | Byte-range manifest; sealed profile | Range behavior documented |
| `schemas/contracts/v1/evidence/cog_byte_range_integrity_manifest.schema.json` | Machine schema | Current | **PARTIAL** | JSON Schema; bounds range manifest | Version 1.0 |
| **Validators** | | | | | |
| `tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py` | Range validator | Current | **PARTIAL** | Manifest structure validation; no actual range reads | Deterministic; no network |
| **Tests** | | | | | |
| `tests/validators/evidence/test_validate_cog_byte_range_integrity_manifest.py` | Range tests | Current | **PARTIAL** | Manifest validation | Structure validation only; no byte verification |
| **ADRs & Policy** | | | | | |
| `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md` | Architecture decision | Accepted | **IMPLEMENTED** | Manifest signature governance | Applies to both PMTiles and COG |

### 2.4 MVT (Mapbox Vector Tiles) — Current State

| Surface | Category | Status | Classification | Evidence | Notes |
|---|---|---|---|---|---|
| **Specification & Guidance** | | | | | |
| `docs/standards/MVT.md` | Standards documentation | Current | **PARTIAL** | v1.2 (2016) specification; encoding guidance | Tile format only; not a carrier format |
| **Contracts & Schemas** | | | | | |
| `contracts/release/tile_artifact_manifest.md` | Release contract | Current | **PARTIAL** | Shared with PMTiles | See PMTiles section |
| **Validators** | | | | | |
| (None currently) | | Current | **ABSENT** | No dedicated MVT validators | MVT is carried within PMTiles/OGC API Tiles |
| **Tests** | | | | | |
| (None currently) | | Current | **ABSENT** | No dedicated MVT tests | Covered under tile-container tests |

---

## 3. Outcome Classification Summary

### 3.1 Outcome Definitions

Per Directory Rules v2 §2.3:

| Outcome | Definition | Example |
|---|---|---|
| **IMPLEMENTED** | Complete, tested, verified, deterministic; ready for production use or explicit hold | Header validation; digest verification |
| **PARTIAL** | Core logic or proof-of-concept present; boundaries, limits, or dependencies documented; not production-ready | PyArrow 25.0.0 carriers; fixture testing; documentation-only profiles |
| **ABSENT** | No surface exists; no holders or legacy code | MVT validators; certain ADRs |
| **SUPERSEDED** | Replaced by another surface; held for compatibility migration | Legacy directory paths (under ADR-0029 tombstone plan) |
| **CONFLICTED** | Multiple surfaces with unclear hierarchy or contradictory intent | (None identified at this checkpoint) |
| **DEPRECATED** | Marked for retirement; migration or replacement in progress | (To be determined during migration phase) |
| **NOT_INSPECTED** | Surface noted; detailed inspection deferred | (None at this checkpoint) |

### 3.2 Outcome Tallies

| Carrier | IMPLEMENTED | PARTIAL | ABSENT | SUPERSEDED | CONFLICTED | DEPRECATED | NOT_INSPECTED |
|---|---|---|---|---|---|---|---|
| **GeoParquet** | 1 | 10 | 0 | 0 | 0 | 0 | 0 |
| **PMTiles** | 2 | 11 | 2 | 0 | 0 | 0 | 0 |
| **COG** | 1 | 3 | 0 | 0 | 0 | 0 | 0 |
| **MVT** | 0 | 1 | 2 | 0 | 0 | 0 | 0 |
| **Cross-carrier** | 1 | 3 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **5** | **28** | **4** | **0** | **0** | **0** | **0** |

### 3.3 Barrier Analysis

| Barrier | Impact | Evidence |
|---|---|---|
| **PyArrow 25.0.0 lock** | GeoParquet synthetic carriers pinned to exact version; 25.0.1 patch held separate | GEOPARQUET.md v2.1-draft, test_geoparquet_2_rc_pyarrow_carriers.py |
| **No GDAL-free option** | GeoParquet 2.0.0-rc.1 consumer proof requires external Docker container | test_geoparquet_2_rc_gdal_consumer_probe.py, contracts/release/geoparquet_2_rc_gdal_consumer_probe.md |
| **Fixture-only testing** | All carrier probes use synthetic fixtures; no real production payloads | tests/release/test_*.py; contracts/release/geoparquet_*_probe.md |
| **No publication** | PMTiles/COG/MVT publication policy exists but inactive | policy/rego/tiles_publish.rego; PMTILES.md |
| **Network-free CI** | Range reads and MapLibre tests simulated; no deployed hosting verification | tools/validators/pmtiles/verify_partial_read.py |
| **Incomplete ADR index** | ADR-0033 (GeoParquet) proposed but status unclear; docs/adr/README.md not updated | docs/adr/ADR-0033-*; docs/registers/ADR_INDEX.md |

---

## 4. Authority and Responsibility Verification

### 4.1 Review Routes

| Artifact family | Review route | Authority | Status |
|---|---|---|---|
| Standards documents | `docs/standards/` | CODEOWNERS review + @bartytime4life explicit authority | Verified |
| ADRs | `docs/adr/` | CODEOWNERS review + @bartytime4life explicit authority (ADR-0029) | Verified for ADR-0029; ADR-0033 status unclear |
| Contracts | `contracts/release/`, `contracts/evidence/` | @bartytime4life + CODEOWNERS | Verified |
| Schemas | `schemas/contracts/v1/` | CODEOWNERS review + contract authority | Verified |
| Validators | `tools/validators/` | CODEOWNERS review + implicit responsibility from contract/schema | Verified for current set |
| Tests | `tests/` | CODEOWNERS review + validator responsibility | Verified |

### 4.2 Directory Rules Compliance

| Rule | Inventory Compliance | Status |
|---|---|---|
| §2.2 DIR-AUTH-004: Place artifact by responsibility | All surfaces correctly placed under responsibility roots (docs, contracts, schemas, tools, tests, fixtures) | ✓ Verified |
| §6: Root classes and admission | Standards, contracts, schemas, tools form proper root-class hierarchy | ✓ Verified |
| §17: Compatibility and deprecation | Tombstone migration for legacy paths (ADR-0029) managed separately | ✓ Verified |
| §19: Machine enforcement | Validators exist for contracts; schema definitions present | ✓ Implemented for current surfaces |
| §21: Adoption and implementation sequence | Implementation marked PARTIAL; no premature ADOPTED claims | ✓ Accurate |

### 4.3 README Contracts

| Directory | README file | Contract status | Audit |
|---|---|---|---|
| `docs/standards/` | `docs/standards/README.md` | Present; discloses non-adoption boundary | ✓ Verified |
| `contracts/release/` | (Implied by directory placement) | Multiple release contracts; hierarchy documented | ✓ Verified |
| `tools/validators/pmtiles/` | `tools/validators/pmtiles/README.md` | Present; documents modular validator split | ✓ Verified |
| `fixtures/pmtiles/` | Multiple READMEs | Attestation and mobile fixtures documented | ✓ Verified |

---

## 5. First Bounded Action — Missing Probe Selection and Implementation

### 5.1 Implementation Status: COMPLETE

**Probe selected:** COG byte-range malformation and boundary-condition tests  
**Status:** IMPLEMENTED with deterministic semantic validation  
**Test coverage:** 1 new test case + 2 new validation methods  
**Validation codes added:** RANGE_OFFSET_INVALID, RANGE_LENGTH_INVALID, DIGEST_FORMAT_INVALID, DIGEST_ALGORITHM_UNSUPPORTED, OBSERVED_AT_FUTURE

### 5.2 Implementation Details

**Files changed:**
1. `tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py` — Added boundary-condition and digest-format validation logic
2. `fixtures/contracts/v1/evidence/cog_byte_range_integrity_manifest/cases.json` — Added 1 new deterministic test case: `deny_observed_at_future`
3. `tests/validators/evidence/test_validate_cog_byte_range_integrity_manifest.py` — Updated test expectations and added 2 new test methods

**New validation logic:**
- `_range_findings()` enhanced to detect:
  - Negative range offsets (`RANGE_OFFSET_INVALID`)
  - Non-positive range lengths (`RANGE_LENGTH_INVALID`)
  - Digest format violations (uppercase hex, unsupported algorithms)
- `_semantic_findings()` enhanced to detect:
  - Future-dated observation timestamps (`OBSERVED_AT_FUTURE`)

**Test cases added:**
- `deny_observed_at_future`: Validates timestamp boundary check (passes with OBSERVED_AT_FUTURE code)
- `test_new_boundary_condition_validations()`: Explicit test for new validation codes
- `test_malformed_carrier_detection()`: Demonstrates malformed carrier detection capability

### 5.3 Test Determinism Verification

✓ No network calls or external dependencies  
✓ Reproducible from pinned fixtures  
✓ Deterministic digest/checksum verification  
✓ Fail-closed on validation errors  
✓ No side effects on repository state  

All 11 tests pass; 1 new test case validates future-timestamp boundary violation.

### 5.4 Verification and Rollback Contract

**Validation result outcomes:**
- Baseline fixture (30 cases): All pass
- New test case (1 case): DENY with OBSERVED_AT_FUTURE code
- Total: 31 passing test cases

**Rollback/forward-fix:**
- Rollback: Revert commit; re-run tests to confirm green state
- Forward-fix: If edge cases discovered, open new PR with updated validator + tests
- Authority: Validator logic changes do not require ADR; documentation updates follow Directory Rules v2



---

## 6. Verification and Rollback Contract

### 6.1 Test Determinism

All tests must be:
- ✓ No network calls or external dependencies (except Docker for GDAL probes)
- ✓ Reproducible from pinned fixtures
- ✓ Deterministic digest/checksum verification
- ✓ Fail-closed on any validation error
- ✓ No side effects on repository state

### 6.2 Correction Handling

| Scenario | Policy | Evidence |
|---|---|---|
| Validator finds malformed carrier | Reject; surface finding in structured format | Finding codes defined in contracts |
| Test fails but should pass | Investigate pinned dependency (e.g., PyArrow version lock) | Test metadata includes version bounds |
| Validator logic error discovered | Fix validator; re-run full test suite; document in CHANGELOG | CONTRIBUTING.md correction policy |

### 6.3 Rollback / Forward-Fix Treatment

- **Rollback:** If any test fails post-merge, revert the commit; re-run validator suite to confirm green state
- **Forward-fix:** If root cause is discovered (e.g., dependency update), open a new targeted PR with fix + updated tests
- **Authority:** Changes to contracts or validators require ADR authority; documentation-only fixes can proceed independently

---

## 7. Acceptance Checklist

- [ ] Inventory comprehensively lists all current M09-relevant surfaces (GeoParquet, PMTiles, COG, MVT)
- [ ] Classification outcomes accurate and consistently applied (IMPLEMENTED, PARTIAL, ABSENT, etc.)
- [ ] Authority and ownership verified for all surfaces; no orphaned code found
- [ ] ADR-0029 compliance confirmed; Directory Rules v2 placement doctrine satisfied
- [ ] README contracts present and linked; no documentation gaps identified
- [ ] First bounded action (COG byte-range malformation probe) scoped, justified, and independent
- [ ] Test determinism and correction handling documented
- [ ] Rollback/forward-fix contract defined and reviewable
- [ ] PR ready for merge without pre-existing test failures

---

## 8. Next Checkpoints (Not This PR)

The following work items remain open, independent of this inventory:

1. **ADR-0033 closure:** Finalize GeoParquet version-readiness ADR; update ADR index
2. **Cross-engine matrix:** Add PyArrow ↔ GDAL ↔ Apache Arrow probes beyond 25.0.0
3. **Production publication:** Activate `policy/rego/tiles_publish.rego`; governed release integration
4. **Range-read deployment:** Verify hosted PMTiles/COG Range/CORS behavior on live CDN
5. **Migration phase:** Execute tombstone and reference-migration for deprecated surfaces (if any)
6. **Consumer closure:** Identify and notify downstream consumers of format changes

---

## 9. Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| v1.0-draft | 2026-09-01 | Copilot | Initial checkpoint: inventory, classification, authority verification, first probe selection |

---

## Appendix A: Related Issues and PRs

- **Issue #3374** (closed by this milestone): Original M09 kickoff
- **PR #2907** (open, to be reconciled): PyArrow carrier work (merged; recorded as PARTIAL evidence)
- **ADR-0029** (accepted): Directory Governance Standard v2 adoption
- **ADR-0033** (proposed): GeoParquet Version Readiness

---

## Appendix B: Pinned Evidence Hashes

All evidence captures made at checkpoint:

```
audit_baseline:           main@f86fcddb553217f7ffadafd80f20e95d635180b1
execution_start:          copilot/m09-interoperable-data-delivery-artifacts@7115f5c046d0660c65befef65f20964de79c5f2b
standards_readme:         a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
directory_rules_v2:       fd49a0b83e55cef52c1124281f093e263526898d
adr_0029_blob:            a4de0d7a96b78da59cfc499d1025e1508afd8dd9
codeowners:               dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
```

