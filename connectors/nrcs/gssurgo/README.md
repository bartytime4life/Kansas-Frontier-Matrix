<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-gssurgo-readme
title: connectors/nrcs/gssurgo/ — NRCS gSSURGO Gridded-Derivative and Source-Admission Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NRCS steward · Soil steward · Agriculture steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Schema steward · CI steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; connector-boundary; nested-product-lane; nrcs; gssurgo; gridded-soil-survey; descriptor-identity-conflicted; source-inactive; no-network-by-default; raw-quarantine-only; descriptor-gated; resolution-aware; survey-vintage-aware; support-type-aware; mukey-lineage; fixture-first; not-field-verification; no-publication; rollback-aware; no-secrets"
current_path: connectors/nrcs/gssurgo/README.md
truth_posture: CONFIRMED repository path and prior v0.1 README, NRCS family/source/package/test README scaffolds, draft gSSURGO product page, kfm-connector-nrcs 0.0.0 metadata, empty package initializer, minimal PROPOSED Soil and Agriculture gSSURGO registry placeholders, empty source-authority register, updated gNATSGO and SSURGO connector boundaries, TODO-only connector workflow, and bounded absence of a flat gSSURGO lane, central products/gssurgo.py module, gSSURGO tests, gSSURGO pipeline/spec, and gSSURGO source-descriptor schema / PROPOSED request/package/grid/attribute preservation contract, descriptor/collection identity contract, source-role/support-type reconciliation, admission candidates, finite connector-local outcomes, fixture taxonomy, negative tests, implementation sequence, correction, deprecation, descriptor migration, and rollback / CONFLICTED draft observed source-role wording versus gridded-derivative support type, separate versus shared SSURGO/gSSURGO descriptor or collection identity, product release date versus constituent survey-area vintage, and documentation-rich posture versus absent executable implementation / UNKNOWN active SourceDescriptor, approved acquisition surfaces, current package formats, native CRS and resolution, band and attribute structure, exact survey-vintage model, rights, executable behavior, fixtures, tests, CI enforcement, schedules, receipts, deployment, downstream consumers, and runtime health / NEEDS VERIFICATION owners, source and collection identity, activation, rights and attribution, source-role/support-type vocabulary, endpoint allowlist, package profile, schemas, validators, fixtures, CI, lifecycle routing, correction, deprecation, descriptor migration, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 28de9ef2710d978a5c00f3057cc33868cbedd698
  prior_blob: 4a491da7f519c06eaec7fe17301eaa8e4626bb77
  nrcs_family_blob: 888236f218fc0892c54c947c0c2651b34ca5137b
  nrcs_source_root_blob: 3b26759548ddaf52eb5b6de0e25dfa354e1d62ec
  nrcs_package_readme_blob: 3e022257cc553e8661b988e9e01c61cccc1fddc8
  nrcs_tests_blob: 7c65ba6ef85a8369e17c40d5e3fbc388b04a306b
  package_metadata_blob: c6bb1565db7df490bee52a597d04d694e2b9f8a4
  package_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  product_page_blob: e3a8a053889e31437c6d900cfd7f7ef0a2f08442
  soil_registry_placeholder_blob: d87433278da53d17be164dacbeebeccd949a8fb8
  agriculture_registry_placeholder_blob: a573cc212428b65c060ac221cae61ef46a9ad810
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  gnatsgo_boundary_blob: 83b3816033fc558fd552480edefdde978488ccfd
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - connectors/nrcs/gssurgo/README.md exists at v0.1 before this revision
    - connectors/nrcs-gssurgo/README.md was not found
    - connectors/nrcs/src/nrcs/__init__.py is empty
    - connectors/nrcs/src/nrcs/products/gssurgo.py was not found
    - connectors/nrcs/tests/test_gssurgo.py was not found
    - connectors/nrcs/tests/test_gssurgo_metadata.py was not found
    - connectors/nrcs/pyproject.toml contains only project name and version 0.0.0
    - data/registry/sources/soil/nrcs-gssurgo.yaml is a minimal PROPOSED placeholder
    - data/registry/sources/agriculture/gssurgo.yaml is a minimal PROPOSED placeholder
    - control_plane/source_authority_register.yaml is PROPOSED and entries is empty
    - schemas/contracts/v1/domains/soil/gssurgo_source_descriptor.schema.json was not found
    - pipelines/domains/soil/gssurgo_ingest/README.md was not found
    - pipeline_specs/soil/gssurgo_ingest.yaml was not found
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ../src/README.md
  - ../src/nrcs/README.md
  - ../tests/README.md
  - ../gnatsgo/README.md
  - ../ssurgo/README.md
  - ../sda/README.md
  - ../pyproject.toml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../docs/sources/catalog/nrcs.md
  - ../../../docs/sources/catalog/nrcs/README.md
  - ../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/soil/nrcs-gssurgo.yaml
  - ../../../data/registry/sources/agriculture/gssurgo.yaml
  - ../../../contracts/domains/soil/soil_map_unit.md
  - ../../../contracts/domains/soil/soil_property.md
  - ../../../contracts/domains/soil/soil_time_caveat.md
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
  - ../../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, nrcs, gssurgo, gridded-soil-survey, raster, grid, resolution, crs, transform, nodata, band-identity, mukey, source-survey-vintage, soil-time-caveat, rasterization-lineage, raw, quarantine, no-network, fixture-first, anti-collapse, correction, descriptor-migration, rollback]
notes:
  - "This revision changes only connectors/nrcs/gssurgo/README.md."
  - "The nested path is repository-present, but path presence does not establish an active source, executable implementation, accepted descriptor/collection identity, or publication readiness."
  - "The gSSURGO product page exists but is draft/pre-activation and leaves separate-versus-shared SSURGO/gSSURGO collection identity open."
  - "The only inspected Soil and Agriculture gSSURGO registry records are minimal PROPOSED inventory placeholders, and the source-authority register has no entries."
  - "Draft source doctrine uses observed source-role language while family doctrine calls gSSURGO a derived gridded product; an accepted descriptor must pin role and support type without collapsing them."
  - "External details such as current URLs, package names, formats, CRS, transform, resolution, bands, attributes, rights, and refresh cadence are version-sensitive and are not asserted here as implementation facts."
  - "A gSSURGO record remains product-, package-, grid-, band-, MUKEY-, attribute-, resolution-, CRS-, survey-vintage-, rasterization-lineage-, and correction-scoped."
  - "Connector activity is limited to explicit source admission and RAW or QUARANTINE handoff."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS gSSURGO Gridded-Derivative and Source-Admission Boundary

`connectors/nrcs/gssurgo/`

> Repository-present nested boundary for candidate USDA NRCS gSSURGO source admission. Current evidence establishes a README-only lane—not an active source, approved acquisition profile, runnable connector, tested parser, validated schema, or release-ready gridded soil-survey workflow.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![descriptor identity](https://img.shields.io/badge/descriptor__identity-CONFLICTED-orange)
![source state](https://img.shields.io/badge/source-inactive-critical)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![field verification](https://img.shields.io/badge/field__verification-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#directory-rules-basis) · [Identity](#identity-boundary) · [Invariants](#keystone-invariants) · [Inputs](#explicit-input-contract) · [Transport](#transport-and-security) · [Grid](#grid-and-lineage-contract) · [Products](#product-separation) · [Admission](#source-admission-handoff) · [Outcomes](#connector-outcomes) · [Testing](#testing-and-fixtures) · [Implementation](#implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **This README is not a source activation, descriptor/collection identity, or implementation decision.** It does not establish an active SourceDescriptor, approved endpoint, current package profile, final source role or support type, parser, schema, fixtures, tests, receipts, schedule, deployment, or release state.

> [!CAUTION]
> **A gSSURGO raster cell is not parcel truth, finer-than-survey precision, or current field verification.** A connector may preserve a source package and its native lineage. It may not silently convert cell size into survey precision, map units into parcels, interpretations into regulatory determinations, or connector success into public release.

---

<a id="purpose"></a>

## Purpose

This README defines the allowed source-edge boundary for candidate gSSURGO work under the established `connectors/nrcs/` family root.

A future implementation may exist here only after governance verifies:

1. whether gSSURGO has its own SourceDescriptor and collection identity or shares a governed family identity with SSURGO;
2. the canonical KFM source ID, package identity, and activation decision;
3. the approved acquisition surface and package/asset profile;
4. source role and support type, including source survey evidence, rasterized representation, and downstream modeled derivatives;
5. source-survey vintage, `MUKEY` lineage, and `SoilTimeCaveat` behavior;
6. rights, attribution, sensitivity, and redistribution posture;
7. schemas, validators, fixtures, tests, CI gates, receipt requirements, and downstream pipeline boundaries.

Any implementation must remain descriptor-gated, no-network by default, fixture-first, deterministic, bounded in redirects/timeouts/retries/rate/payload/archive/decompression, lossless about grid and lineage metadata, and limited to RAW or QUARANTINE candidates.

It must not become a second NRCS family root, parallel source registry, mutable endpoint catalog, general raster transformer, SSURGO replacement, Soil pipeline, policy engine, proof service, release service, or public map/API/UI/AI surface.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v0.1 before revision** | A nested documentation boundary exists. |
| Flat `connectors/nrcs-gssurgo/` | **NOT FOUND** | No competing flat lane was established. |
| NRCS family root | **CONFIRMED** | `connectors/nrcs/` is the family spine. |
| gSSURGO product page | **CONFIRMED draft/pre-activation** | Product doctrine exists but does not activate the source. |
| Product-page source role | **PROPOSED `observed`** | Must be reconciled with gridded-derivative support type. |
| Collection/descriptor identity | **OPEN** | Separate gSSURGO identity versus shared SSURGO identity is unresolved. |
| NRCS package | **CONFIRMED `0.0.0` shell** | Package presence does not prove gSSURGO support. |
| Central initializer | **CONFIRMED empty** | No runtime behavior is exposed. |
| `products/gssurgo.py` | **NOT FOUND** | No executable adapter is established. |
| gSSURGO tests | **NOT FOUND** | No product-specific test behavior is established. |
| Soil registry pointer | **Minimal `PROPOSED` placeholder** | Inventory presence is not activation. |
| Agriculture registry pointer | **Minimal `PROPOSED` placeholder** | Domain inventory is not source authority. |
| Source-authority register | **`PROPOSED`, `entries: []`** | gSSURGO is not activated. |
| Product-specific schema | **NOT FOUND** | No enforcing machine shape is established. |
| Product-specific pipeline/spec | **NOT FOUND** | No dedicated downstream implementation is established. |
| Connector workflow | **TODO-only** | A green run cannot prove connector or receipt behavior. |

**CONFIRMED:** path presence, parent family, draft product page, placeholder package, empty initializer, registry placeholders, empty authority register, and RAW/QUARANTINE connector law.

**PROPOSED:** the contracts, outcomes, reason codes, fixtures, tests, implementation sequence, and rollback procedures in this README.

**CONFLICTED:** observed source-role wording versus gridded-derivative support type; separate versus shared SSURGO/gSSURGO descriptor/collection identity; product release date versus constituent survey-area vintage.

**UNKNOWN:** approved source surfaces, package structure, raster format, native CRS/transform/resolution, bands, attributes, exact vintage model, rights, implementation, deployment, and health.

**NEEDS VERIFICATION:** owners, identity, activation, rights, source role/support type, package profile, schema, validators, fixtures, CI, pipeline, catalog, evidence, release, correction, and rollback.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### May eventually

- construct an explicit request profile;
- retrieve an approved object or inspect a supplied package;
- preserve response, package, file, and digest identity;
- inventory archives safely;
- extract native raster and attribute metadata without transformation;
- preserve `MUKEY`, product release, source-survey vintage, and correction lineage;
- construct RAW or QUARANTINE admission candidates;
- emit finite connector-local outcomes and receipt inputs.

### Must not

```text
activate a source
define source or collection identity
assign final source role or support type
reproject, resample, mosaic, clip, tile, or build overviews
normalize components or horizons
infer field conditions
create parcel, compliance, regulatory, engineering, or crop/yield claims
write WORK, PROCESSED, CATALOG, TRIPLET, or PUBLISHED
close EvidenceBundle or proof state
issue ReleaseManifest
serve public API/UI/map/AI output
```

Connector success is not validation, promotion, evidence closure, catalog closure, or release.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

`connectors/` is the owning root because this file governs source-specific retrieval, package inspection, integrity, provenance, and admission behavior.

Directory Rules establish:

- `connectors/nrcs/` as the NRCS family spine;
- connector output only to `data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/...`;
- no connector publication or later-lifecycle writes;
- `pipeline_specs/` for declarative intent and `pipelines/` for executable transforms;
- docs, contracts, schemas, policy, registry, evidence, release, and public interfaces as separate authority roots.

This README does not create a new root, SourceDescriptor, schema, contract, pipeline, collection, release, or public path.

[Back to top](#top)

---

<a id="identity-boundary"></a>

## Identity boundary

| Layer | Candidate identity | Status |
|---|---|---:|
| Repository path | `connectors/nrcs/gssurgo/` | **CONFIRMED** |
| Product-page short ref | `nrcs.gssurgo` | **PROPOSED** |
| Soil registry pointer | `data/registry/sources/soil/nrcs-gssurgo.yaml` | **CONFIRMED placeholder** |
| Agriculture pointer | `data/registry/sources/agriculture/gssurgo.yaml` | **CONFIRMED placeholder** |
| Product-page collection pattern | `kfm-nrcs-gssurgo` | **PROPOSED** |
| Shared SSURGO descriptor/collection option | unresolved | **OPEN / CONFLICTED** |

An accepted decision must pin source family, product/package identity, descriptor ID, aliases, collection identity, upstream package/release identifiers, asset roles, source role, support type, source-survey vintage, correction behavior, and rights.

Until then:

- do not create a flat competing implementation;
- do not activate multiple source IDs;
- do not give SSURGO and gSSURGO the same mutable source object ID;
- do not publish collection IDs;
- do not create modules, fixtures, tests, schedules, or pipelines that disagree on identity.

A shared descriptor or collection may be acceptable only if distinct product/assets, geometry forms, digests, vintages, and correction lineage remain explicit.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. gSSURGO remains distinct from SSURGO vector geometry and relational tables.
2. A raster cell is not a current field observation.
3. Cell size is not claim precision.
4. `MUKEY` is a lineage key, not a complete soil claim.
5. Product release date does not erase constituent survey-area vintages.
6. `SoilTimeCaveat` survives admission and downstream handoff.
7. Native CRS, transform, resolution, extent, bands, nodata, and masks remain inspectable.
8. Rasterization is a transform and requires lineage to SSURGO mapping.
9. Source role and support type are separate dimensions.
10. Downstream suitability or erosion surfaces remain modeled.
11. gSSURGO is not gNATSGO, STATSGO2, SoilGrids, SMAP, or station data.
12. Package identity and digest precede extraction.
13. Unknown rights, lineage, CRS, vintage, or integrity fail closed.
14. Corrections append lineage rather than overwrite.
15. Network is disabled by default.
16. Public clients never read connector outputs directly.
17. Connector success is not publication.
18. Secrets never enter URLs, fixtures, logs, receipts, or source objects.

[Back to top](#top)

---

<a id="explicit-input-contract"></a>

## Explicit input contract

A future runner must provide an explicit, reviewed profile:

```yaml
# PROPOSED illustrative shape — not canonical or active.
source_descriptor_ref: kfm://source/NEEDS-VERIFICATION
activation_ref: kfm://source-activation/NEEDS-VERIFICATION
product_id: nrcs.gssurgo
collection_id: NEEDS_VERIFICATION
source_object:
  url: https://approved.example/NEEDS-VERIFICATION
request_profile_ref: kfm://request-profile/NEEDS-VERIFICATION
package_profile_ref: kfm://package-profile/NEEDS-VERIFICATION
expected_digest: null
rights_ref: kfm://policy/rights/NEEDS-VERIFICATION
sensitivity_ref: kfm://policy/sensitivity/NEEDS-VERIFICATION
evaluation_time: 2026-07-15T00:00:00Z
```

Required controls include active descriptor/activation references, approved URL/host, finite timeout/retry/rate/payload limits, expected product/package identity, rights/sensitivity references, and an explicit evaluation time.

Ambient environment variables must not silently activate network access, select a source, choose a collection, or change lifecycle output.

[Back to top](#top)

---

<a id="transport-and-security"></a>

## Transport and security

Network access is off by default. A future live client must enforce:

- `https` and exact host allowlists;
- DNS/private-network/loopback/link-local denial;
- redirect limits with revalidation on every hop;
- finite connect/read/total timeouts;
- bounded retry count and backoff;
- rate limits and pagination/object caps;
- compressed and decompressed byte limits;
- archive-member, nesting, path-length, and collision limits;
- content-type plus file-signature checks;
- TLS verification;
- redacted logs and errors;
- no URL credentials, tokens, signed-query leakage, cookies, or private endpoints;
- no unsafe deserialization or executable archive members.

Temporary files must be isolated and removed safely. The connector must not follow symlinks, path traversal, absolute archive paths, devices, sockets, or nested archives unless explicitly allowed and tested.

[Back to top](#top)

---

<a id="grid-and-lineage-contract"></a>

## Grid and lineage contract

Preserve before transformation:

### Package and files

- product/package/release ID;
- source URL and retrieval time;
- response metadata;
- original filename and media type;
- compressed and uncompressed sizes;
- archive-member inventory;
- file signatures and digests;
- manifest and metadata references;
- correction or supersession markers.

### Native grid

- width, height, band count, data type;
- CRS and axis order;
- affine transform/grid mapping;
- native pixel size and units;
- origin, extent, alignment, and pixel semantics;
- nodata/mask, scale, offset, categories;
- compression, blocks, and overviews;
- source-survey vintage and product-generation version.

### Attributes and joins

- attribute/table identity, schema, encoding, row count, digest;
- exact `MUKEY` field name/type/format;
- key uniqueness, nulls, duplicates, unmatched counts;
- target SSURGO table/product and release compatibility;
- constituent survey-area/source-vintage context;
- `SoilTimeCaveat`.

### Prohibited silent changes

```text
reproject
resample
snap to another grid
change cell size or origin
mosaic or clip
build overviews
change nodata
cast types
apply scale/offset
fill gaps
derive categories
join attributes without receipt
```

### Lineage anti-collapse

```text
gSSURGO cell -> current point observation
cell size -> source survey claim precision
MUKEY -> component or horizon fact
product release date -> uniform survey-area vintage
raster asset -> SSURGO vector geometry
successful join -> semantic validity
downstream model output -> observed source value
```

[Back to top](#top)

---

<a id="product-separation"></a>

## Product separation

| Product/support family | Required distinction |
|---|---|
| SSURGO | Vector/static survey packages and relational tables; gSSURGO does not replace full geometry or component/horizon fidelity. |
| gSSURGO | Rasterized SSURGO map-unit representation with `MUKEY`, native grid, product release, and survey-vintage caveats. |
| gNATSGO | Separate national gridded soil product with different source composition and generalization posture. |
| STATSGO2 | Generalized regional/national context, not detailed SSURGO mapping. |
| SDA | Query surface whose query text, parameters, response scope, and receipt remain separate. |
| Web Soil Survey | AOI/session/download surface; session output does not silently become canonical package truth. |
| SoilGrids | Modeled global soil grid with distinct model, depth, uncertainty, and resolution semantics. |
| SMAP | Satellite soil-moisture product, not soil-survey mapping. |
| SCAN, USCRN, Mesonet | Station observations with time, depth, quality, and freshness semantics. |
| KFM suitability/erosion surfaces | Downstream modeled interpretations requiring model/transform receipts. |

Comparisons and fusions belong downstream and require explicit transform/model receipts, uncertainty treatment, source-role/support-type preservation, and release review.

[Back to top](#top)

---

<a id="source-admission-handoff"></a>

## Source-admission handoff

The connector may produce only a RAW or QUARANTINE candidate.

```yaml
# PROPOSED illustrative envelope.
candidate_id: kfm://candidate/NEEDS-VERIFICATION
source_descriptor_ref: kfm://source/NEEDS-VERIFICATION
source_object_ref: kfm://source-object/NEEDS-VERIFICATION
retrieval:
  requested_at: 2026-07-15T00:00:00Z
  completed_at: 2026-07-15T00:00:01Z
package:
  digest: sha256:...
  compressed_bytes: 0
  members: []
grid:
  crs: NEEDS_VERIFICATION
  resolution: NEEDS_VERIFICATION
  transform: NEEDS_VERIFICATION
  bands: []
  nodata: NEEDS_VERIFICATION
lineage:
  mukey_field: NEEDS_VERIFICATION
  product_release: NEEDS_VERIFICATION
  survey_vintages: []
rights_ref: kfm://policy/rights/NEEDS-VERIFICATION
sensitivity_ref: kfm://policy/sensitivity/NEEDS-VERIFICATION
outcome: QUARANTINE_CANDIDATE
reason_codes:
  - GSSURGO_PACKAGE_PROFILE_UNVERIFIED
lifecycle_ceiling: [RAW, QUARANTINE]
```

A RAW candidate requires active source authority, approved surface/profile, integrity closure, required grid/lineage fields, resolved rights/sensitivity, deterministic identity, and complete receipt inputs.

Quarantine for unresolved identity, package profile, CRS/transform/resolution, band/nodata semantics, `MUKEY` lineage, survey vintage, rights, sensitivity, schema drift, correction state, unexpected executable content, or resource-limit breaches.

The connector must never emit WORK/PROCESSED/catalog/triplet/proof/release/public artifacts.

[Back to top](#top)

---

<a id="connector-outcomes"></a>

## Connector outcomes

These are **PROPOSED connector-local results**, not canonical policy or release decisions.

| Outcome | Meaning |
|---|---|
| `ADMIT_RAW_CANDIDATE` | Connector-level prerequisites passed; downstream gates remain. |
| `QUARANTINE_CANDIDATE` | Bytes are preserved but review is required. |
| `SKIP_NO_CHANGE` | Accepted deterministic comparison proves no material change. |
| `ABSTAIN_UNSUPPORTED` | Source/package/version is outside the implemented profile. |
| `RETRY_LATER` | Bounded transient failure occurred and retry policy allows another attempt. |
| `ERROR` | Safe completion was impossible. |

Representative reason codes:

```text
GSSURGO_SOURCE_INACTIVE
GSSURGO_DESCRIPTOR_OR_PRODUCT_ID_AMBIGUOUS
GSSURGO_COLLECTION_OR_ALIAS_UNAPPROVED
GSSURGO_SOURCE_SURFACE_UNAPPROVED
GSSURGO_NETWORK_DISABLED
GSSURGO_HOST_DENIED
GSSURGO_REDIRECT_DENIED
GSSURGO_TIMEOUT
GSSURGO_RATE_LIMITED
GSSURGO_RESPONSE_TOO_LARGE
GSSURGO_SIGNATURE_MISMATCH
GSSURGO_ARCHIVE_UNSAFE
GSSURGO_PACKAGE_PROFILE_UNVERIFIED
GSSURGO_REQUIRED_MEMBER_MISSING
GSSURGO_DIGEST_MISMATCH
GSSURGO_GRID_METADATA_MISSING
GSSURGO_CRS_UNKNOWN
GSSURGO_RESOLUTION_UNKNOWN
GSSURGO_TRANSFORM_UNKNOWN
GSSURGO_BAND_IDENTITY_UNKNOWN
GSSURGO_NODATA_UNKNOWN
GSSURGO_JOIN_FIELD_INVALID
GSSURGO_LINEAGE_MISSING
GSSURGO_SUPPORT_TYPE_UNRESOLVED
GSSURGO_SOURCE_ROLE_UNRESOLVED
GSSURGO_SOURCE_VINTAGE_UNKNOWN
GSSURGO_RIGHTS_UNRESOLVED
GSSURGO_SENSITIVITY_UNRESOLVED
GSSURGO_SCHEMA_DRIFT
GSSURGO_UNSUPPORTED_VERSION
GSSURGO_INTERNAL_ERROR
```

Reason codes are finite, secret-safe, compatibility-reviewed, and do not imply policy or release approval.

[Back to top](#top)

---

<a id="testing-and-fixtures"></a>

## Testing and fixtures

Current repository evidence describes future gSSURGO fixtures/tests, but the named product test files were not found. This is therefore a proposed test contract.

### Default posture

- no live network;
- no credentials/cookies/private sessions;
- no writes outside temporary directories;
- no lifecycle writes;
- no publication;
- deterministic fixtures and expected outputs;
- explicit negative-path coverage.

### Fixture classes

| Class | Purpose |
|---|---|
| Synthetic package | Exercise package/parser shape without copied source data. |
| Generated raster | Test CRS/transform/resolution/band/nodata behavior. |
| Minimized public sample | Tiny reviewed structural sample. |
| Malformed archive | Traversal, collision, limit, and signature tests. |
| Schema-drift sample | Changed fields, types, or missing members. |
| Vintage-mismatch sample | Product release versus survey-area vintage behavior. |
| Rights-uncertain sample | Fail-closed policy handoff. |
| Live integration | Isolated, opt-in, read-only, non-authoritative. |

Required tests cover import safety, descriptor/activation gates, transport/SSRF, archive limits, digest stability, native grid preservation, `MUKEY` joins, survey-vintage/SoilTimeCaveat handling, source-role/support-type separation, no silent transforms, RAW/QUARANTINE-only output, secret-safe logging, and public-output denial.

Negative tests must reject:

- SSURGO or gNATSGO mislabeled as gSSURGO;
- missing activation;
- unknown package version;
- missing CRS/resolution/nodata;
- silent resampling or reprojection;
- cell-as-point or cell-as-parcel claims;
- `MUKEY` treated as component/horizon truth;
- modeled interpretation labeled observed;
- SDA/WSS output treated as package truth;
- public tile or release payload generation.

[Back to top](#top)

---

<a id="implementation-sequence"></a>

## Implementation sequence

1. **Resolve identity.** Decide separate/shared SSURGO-gSSURGO descriptor and collection identities; pin source ID and aliases.
2. **Approve SourceDescriptor.** Define authority, surfaces, package profile, role/support type, cadence, rights, sensitivity, vintage, correction, and activation.
3. **Define contracts and schemas.** Package manifest, grid metadata, lineage, candidate, outcomes, valid/invalid fixtures.
4. **Implement offline inspection first.** Import-safe module, supplied-file parsing, archive safety, digests, raster/attribute metadata.
5. **Implement admission candidates.** Descriptor gates, rights/sensitivity prerequisites, RAW/QUARANTINE envelopes, reason codes.
6. **Add bounded live retrieval.** Allowlists, redirects, timeouts, retries, rate, byte/decompression caps, isolated live tests.
7. **Create downstream pipeline/spec.** Normalization, transforms, lineage validation, catalog handoff, correction, rollback.
8. **Wire real CI.** Import/no-network/security/grid/lineage/rights/lifecycle tests—not TODO echoes.
9. **Run a reviewed dry-run.** Produce inventory, digests, grid metadata, lineage, candidate outcome, and no public output.
10. **Govern promotion separately.** Only downstream governed workflows create catalog, proof, release, or public artifacts.

Stop at any stage when identity, rights, source authority, schema, lineage, or validation remains unresolved.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners are assigned.
- [ ] Product, descriptor, collection, and aliases are approved.
- [ ] Existing gSSURGO product doctrine is reviewed and aligned.
- [ ] SourceDescriptor is enforcing and active.
- [ ] Source role and gridded-derivative support type are unambiguous.
- [ ] SSURGO rasterization, `MUKEY`, product-release, and survey-vintage lineage are represented.
- [ ] Rights, attribution, redistribution, and sensitivity are approved.
- [ ] Semantic contracts and enforcing schemas exist.
- [ ] Valid and invalid fixtures prove behavior.
- [ ] Central product module is import-safe.
- [ ] Offline parsing preserves package/grid/attribute/lineage identity.
- [ ] Archive, SSRF, timeout, rate, payload, and decompression limits are enforced.
- [ ] No silent repair, resampling, reprojection, filling, or interpretation occurs.
- [ ] Output is limited to RAW or QUARANTINE candidates.
- [ ] Product-specific negative tests pass.
- [ ] CI runs real checks.
- [ ] Pipeline/spec and receipt handoff are accepted.
- [ ] Catalog/evidence/release remain separate.
- [ ] Correction, supersession, deprecation, and rollback drills are verified.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status |
|---|---|---:|
| GSS-001 | Assign owners | NEEDS VERIFICATION |
| GSS-002 | Decide separate/shared descriptor identity | NEEDS VERIFICATION |
| GSS-003 | Decide separate/shared collection identity | NEEDS VERIFICATION |
| GSS-004 | Pin source ID and aliases | NEEDS VERIFICATION |
| GSS-005 | Review existing product page | NEEDS VERIFICATION |
| GSS-006 | Reconcile source role and support type | NEEDS VERIFICATION |
| GSS-007 | Approve source surfaces and allowlist | NEEDS VERIFICATION |
| GSS-008 | Verify package/archive structure | NEEDS VERIFICATION |
| GSS-009 | Verify native CRS/transform/resolution | NEEDS VERIFICATION |
| GSS-010 | Verify bands/nodata/masks/categories | NEEDS VERIFICATION |
| GSS-011 | Verify attribute tables and `MUKEY` joins | NEEDS VERIFICATION |
| GSS-012 | Verify product and survey-area vintage model | NEEDS VERIFICATION |
| GSS-013 | Define SoilTimeCaveat propagation | NEEDS VERIFICATION |
| GSS-014 | Document rasterization lineage | NEEDS VERIFICATION |
| GSS-015 | Approve rights/citation/redistribution | NEEDS VERIFICATION |
| GSS-016 | Approve sensitivity posture | NEEDS VERIFICATION |
| GSS-017 | Create/activate SourceDescriptor | NEEDS VERIFICATION |
| GSS-018 | Create semantic contracts and schemas | NEEDS VERIFICATION |
| GSS-019 | Implement central module and offline parser | NEEDS VERIFICATION |
| GSS-020 | Implement archive/resource/SSRF controls | NEEDS VERIFICATION |
| GSS-021 | Implement candidate envelopes/outcomes | NEEDS VERIFICATION |
| GSS-022 | Create fixtures and product tests | NEEDS VERIFICATION |
| GSS-023 | Add grid/lineage/anti-collapse tests | NEEDS VERIFICATION |
| GSS-024 | Wire real connector CI | NEEDS VERIFICATION |
| GSS-025 | Define live-test isolation | NEEDS VERIFICATION |
| GSS-026 | Create pipeline/spec | NEEDS VERIFICATION |
| GSS-027 | Verify receipt and catalog/evidence handoff | NEEDS VERIFICATION |
| GSS-028 | Verify release/public-interface separation | NEEDS VERIFICATION |
| GSS-029 | Define correction/deprecation/migration | NEEDS VERIFICATION |
| GSS-030 | Exercise rollback drill | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="rollback-and-correction"></a>

## Rollback and correction

### Documentation rollback

Restore prior blob `4a491da7f519c06eaec7fe17301eaa8e4626bb77` or revert the documentation commit. A README rollback must not delete registry, source, receipt, evidence, or release history.

### Future implementation rollback

Record code, package, configuration, descriptor, schema, fixture, test, workflow, and last-known-safe versions; affected runs; quarantine/cleanup actions; and a tested rollback target.

### Data correction

Do not silently overwrite admitted bytes. A correction creates a new package/source identity, digest, CorrectionNotice, supersession links, impact inventory, revalidation, release decision where applicable, and rollback target.

### Descriptor/collection migration

A separate/shared SSURGO-gSSURGO identity change requires an ADR or migration note, old/new IDs and aliases, coordinated updates across descriptor/module/fixtures/tests/pipeline/receipts/catalog/release, one active implementation, compatibility duration if justified, and rollback instructions.

### Emergency disable

Live acquisition must be disableable without deleting code or history, breaking evidence resolution, altering prior receipts, or publishing a release. Activation and scheduling remain external to this README and product module.

[Back to top](#top)

---

## Status summary

`connectors/nrcs/gssurgo/` is a repository-present but implementation-unproved source-admission boundary.

Until the verification register closes:

```text
README-only
source inactive
descriptor and collection identity conflicted
network off by default
fixtures first
RAW or QUARANTINE only
cite or abstain
no publication
```

It is not SSURGO full fidelity, field or parcel truth, regulatory or engineering authority, schema/policy/evidence/release authority, or a public map/API/UI/AI surface.

<p align="right"><a href="#top">Back to top</a></p>
