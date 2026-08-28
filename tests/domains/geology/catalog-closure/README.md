<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-catalog-closure-readme
title: Tests — Geology Catalog Closure
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <catalog-steward> + <evidence-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/domains/geology/README.md
  - docs/domains/geology/DATA_LIFECYCLE.md
  - docs/domains/geology/CANONICAL_PATHS.md
  - docs/domains/geology/SOURCE_REGISTRY.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - data/catalog/domain/geology/README.md
  - data/proofs/geology/README.md
  - data/catalog/stac/geology/
  - data/catalog/dcat/geology/
  - data/catalog/prov/geology/
  - data/triplets/
  - contracts/domains/geology/
  - schemas/contracts/v1/domains/geology/
  - tests/domains/geology/README.md
  - fixtures/domains/geology/
tags:
  - kfm
  - tests
  - geology
  - natural-resources
  - catalog-closure
  - evidence-bundle
  - evidence-ref
  - catalog-matrix
  - triplet
  - stac
  - dcat
  - prov
  - fail-closed
notes:
  - "This README governs the catalog-closure test lane under tests/domains/geology/catalog-closure/."
  - "It documents intended Geology catalog-closure test coverage; it does not claim that all tests already exist."
  - "Catalog closure is a governed transition from PROCESSED to CATALOG / TRIPLET; it is not public release and not proof by file placement."
  - "The existing Geology root test README is still a greenfield stub as of this update, so this lane remains locally documented but not globally indexed by an expanded test root."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Catalog Closure

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fgeology%2Fcatalog--closure-blue?style=flat-square)
![lifecycle](https://img.shields.io/badge/gate-PROCESSED%E2%86%92CATALOG%2FTRIPLET-purple?style=flat-square)
![posture](https://img.shields.io/badge/posture-fail--closed-critical?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Geology-domain test lane for catalog closure. It proves that processed Geology/Natural Resources artifacts do not advance to `CATALOG / TRIPLET` unless EvidenceRefs resolve, EvidenceBundles close, catalog records are source-role safe, graph/triplet projections remain derivative, and policy/review state is recorded.

---

## 1. Placement and authority

`tests/domains/geology/catalog-closure/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove the Geology catalog-closure gate is enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/geology/` |
| Test lane | `catalog-closure/` |
| Lifecycle transition under test | `PROCESSED -> CATALOG / TRIPLET` |
| Primary runbook | `docs/runbooks/geology/PROMOTION_RUNBOOK.md` |
| Catalog lane | `data/catalog/domain/geology/` |
| Proof lane | `data/proofs/geology/` |
| Fixture counterpart | `fixtures/domains/geology/` |
| Current implementation status | README path exists; executable tests, fixtures, validators, and CI wiring remain `UNKNOWN` until verified. |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific proof lanes under `tests/domains/<domain>/`. This lane tests a gate; it must not become a catalog, proof, release, fixture, schema, policy, or implementation home.

---

## 2. Gate under test

Catalog closure is the governed transition from validated processed Geology material into catalog and graph/triplet structures.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
                                      ^
                                      |
                         this lane proves this gate closes safely
```

A Geology catalog-closure test should not ask whether a claim is interesting or visually useful. It should ask whether the required closure artifacts exist, resolve, agree, and preserve policy and source-role boundaries.

---

## 3. What this lane must prove

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| EvidenceRef resolution | Every `EvidenceRef` resolves to a closed `EvidenceBundle`, not just a string or path. | Hold at PROCESSED; structured fail. |
| EvidenceBundle closure | EvidenceBundle contains source, scope, provenance, policy, citation, review, and digest context required for the claim. | `MISSING_EVIDENCE`, `INCOMPLETE_BUNDLE`, or equivalent. |
| SourceDescriptor linkage | `source_id` resolves to an admitted `SourceDescriptor` with role, rights, sensitivity, and cadence. | `SOURCE_DESCRIPTOR_MISSING` or hold. |
| CatalogMatrix entry | Domain catalog record exists and points to the processed object, evidence, source role, policy posture, and release-prep state. | `CATALOG_MATRIX_MISSING` or hold. |
| Digest closure | Processed artifact, catalog record, proof bundle, receipt set, and projection digests agree. | `DIGEST_MISMATCH` or hold. |
| STAC/DCAT/PROV closure | If STAC, DCAT, or PROV projections exist, they agree with the domain catalog record and do not add unsupported claims. | `CATALOG_PROJECTION_MISMATCH` or hold. |
| Triplet projection | Graph/triplet records are derivative indexes, not root truth; they preserve source-role and EvidenceBundle references. | `TRIPLET_UNSUPPORTED` or hold. |
| Source-role anti-collapse | Occurrence, deposit, estimate, permit, production, reserve, model, observation, and interpretation remain distinct. | `ROLE_COLLAPSE` or hold. |
| Sensitivity and rights | Exact borehole, sample, well-log, private-well, sensitive-resource, proprietary, or infrastructure-risk content has review/policy posture before cataloging. | `SENSITIVITY_UNRESOLVED`, `RIGHTS_UNKNOWN`, or hold. |
| Cross-lane ownership | Geology catalog closure does not rewrite Soil, Hydrology, Hazards, People/Land, Archaeology, or Settlements truth. | `CROSS_LANE_OWNERSHIP_VIOLATION` or hold. |
| Public edge guard | Catalog closure alone does not imply PUBLISHED state. ReleaseManifest and rollback target are still required later. | No public edge exposed. |

---

## 4. Expected test families

This folder should eventually contain narrowly scoped tests, not a single mixed proof harness.

```text
tests/domains/geology/catalog-closure/
├── README.md
├── test_evidence_ref_resolution.py          # PROPOSED
├── test_evidence_bundle_closure.py          # PROPOSED
├── test_source_descriptor_linkage.py        # PROPOSED
├── test_catalog_matrix_entry.py             # PROPOSED
├── test_digest_closure.py                   # PROPOSED
├── test_stac_dcat_prov_alignment.py         # PROPOSED
├── test_triplet_projection_support.py       # PROPOSED
├── test_source_role_anti_collapse.py        # PROPOSED
├── test_sensitivity_and_rights_linkage.py   # PROPOSED
├── test_cross_lane_ownership.py             # PROPOSED
├── test_public_edge_guard.py                # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If the repository standardizes on underscore test names (`catalog_closure`) while the directory uses a hyphen (`catalog-closure`), keep the existing path but name Python modules with underscores so test discovery remains conventional.

---

## 5. Fixture expectations

Tests in this lane should be no-network by default. They should use small, synthetic, public-safe Geology catalog/proof objects.

Recommended fixture groups:

```text
fixtures/domains/geology/catalog-closure/
├── valid/
│   ├── geologic_unit_catalog_closure.json
│   ├── borehole_reference_restricted_closure.json
│   ├── mineral_occurrence_public_safe_closure.json
│   ├── resource_estimate_modeled_closure.json
│   └── stac_dcat_prov_aligned_closure.json
├── invalid/
│   ├── evidence_ref_missing_bundle.json
│   ├── source_descriptor_missing.json
│   ├── catalog_matrix_missing.json
│   ├── digest_mismatch.json
│   ├── triplet_without_evidence_bundle.json
│   ├── stac_claim_exceeds_domain_catalog.json
│   ├── resource_estimate_collapsed_to_deposit.json
│   ├── exact_borehole_public_without_review.json
│   ├── cross_lane_hydrology_rewritten_by_geology.json
│   └── catalog_record_claims_published_without_release_manifest.json
└── golden/
    ├── geology_catalog_closure_minimal.json
    └── geology_catalog_closure_sensitive_restricted.json
```

Fixture rules:

- Use synthetic geology examples unless a public-safe, rights-reviewed fixture is intentionally included.
- Do not include real precise borehole, private-well, sample, well-log, sensitive-resource, proprietary, or infrastructure-risk locations.
- Do not include mineral-rights, parcel-owner, lease, operator, or production details that could be interpreted as legal/property truth.
- Invalid fixtures should fail for one primary closure reason where practical.
- Golden fixtures should remain small enough for maintainers to inspect manually.

---

## 6. Closure artifact checklist

A passing catalog-closure test should show at least these artifacts or equivalent validated structures.

| Artifact | Required for closure? | Notes |
|---|---:|---|
| Processed Geology object | Yes | The candidate being cataloged; not raw source material. |
| `SourceDescriptor` | Yes | Source role, authority, rights, sensitivity, cadence, steward. |
| `EvidenceBundle` | Yes | Closed support for the claim; EvidenceRef must resolve to this. |
| `ValidationReport` | Yes | Shows deterministic validator pass against schema/contract expectations. |
| `PolicyDecision` | Yes | Shows allow/restrict/deny/hold/abstain decision for the catalog candidate. |
| `RedactionReceipt` | When sensitivity applies | Required for public-safe geometry or restricted geometry handling. |
| `AggregationReceipt` | When aggregation applies | Prevents per-place reading of aggregate geology/resource outputs. |
| `CatalogMatrix` entry | Yes | Domain catalog closure record. |
| STAC/DCAT/PROV projection | When emitted | Must agree with domain catalog and not expand authority. |
| Graph/triplet projection | When emitted | Must reference evidence and preserve source role. |
| `ReviewRecord` | When sensitive/material | Required for restricted geology or material public release preparation. |
| Release reference | Not for closure itself | Catalog closure may prepare release, but ReleaseManifest belongs to the release gate. |

---

## 7. Geology-specific catalog checks

The Geology catalog-closure lane should add domain assertions only where Geology/Natural Resources creates closure risk.

| ID | Geology-specific assertion | Why it matters |
|---|---|---|
| `GEOL-CAT-001` | Geologic unit, lithology, structure, and stratigraphic interval records preserve map/source version and interpretation context. | Prevents interpreted map products from becoming generic facts. |
| `GEOL-CAT-002` | Borehole, well-log, core/sample, geophysics, and geochemistry records carry sensitivity and access posture before cataloging. | Prevents precise or restricted subsurface leakage. |
| `GEOL-CAT-003` | Mineral occurrence, resource deposit, resource estimate, permit, production, reserve, extraction, and reclamation records remain distinct. | Prevents resource-class anti-collapse. |
| `GEOL-CAT-004` | Modeled surfaces and interpreted cross-sections cite model/input provenance and are not labeled observed. | Preserves source-role truth. |
| `GEOL-CAT-005` | STAC/DCAT/PROV projections do not assert claims absent from the domain catalog and EvidenceBundle. | Prevents projection drift. |
| `GEOL-CAT-006` | Triplet edges reference the same EvidenceBundle and source role as the catalog record. | Keeps graph projections derivative and inspectable. |
| `GEOL-CAT-007` | Cross-lane references preserve the owning lane's authority. | Geology cannot prove hydrology measurements, soil mapunit truth, hazard risk, or land ownership. |
| `GEOL-CAT-008` | Catalog closure does not expose public output without ReleaseManifest, review state, correction path, and rollback target. | Keeps release separate from cataloging. |

---

## 8. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `GEOL-CAT-001` | Valid catalog closure passes. | A processed GeologicUnit with SourceDescriptor, EvidenceBundle, ValidationReport, PolicyDecision, and CatalogMatrix entry. | Closure passes. |
| `GEOL-CAT-002` | Missing EvidenceBundle fails. | A catalog candidate with an EvidenceRef string that does not resolve. | Hold at PROCESSED. |
| `GEOL-CAT-003` | Missing SourceDescriptor fails. | A catalog candidate whose source_id cannot resolve to source admission record. | Hold with source-descriptor failure. |
| `GEOL-CAT-004` | Digest mismatch fails. | Processed artifact digest differs from catalog/proof digest. | Hold with digest mismatch. |
| `GEOL-CAT-005` | STAC/DCAT/PROV projection drift fails. | Projection states a broader claim than the domain catalog. | Hold with projection mismatch. |
| `GEOL-CAT-006` | Triplet without evidence fails. | Graph edge lacks EvidenceBundle reference or source role. | Hold with unsupported-triplet failure. |
| `GEOL-CAT-007` | Resource-class collapse fails. | A resource estimate is treated as a reserve or deposit. | Hold with anti-collapse failure. |
| `GEOL-CAT-008` | Sensitive exact geometry fails. | Borehole/sample/private-well exact geometry is cataloged for public use without review/redaction. | Hold or deny public-safe closure. |
| `GEOL-CAT-009` | Cross-lane rewrite fails. | Geology catalog record claims to prove hydrology measurement or land ownership. | Hold with cross-lane ownership failure. |
| `GEOL-CAT-010` | Catalog is not release. | A closed catalog record lacks ReleaseManifest but is marked public. | Public edge denied. |

---

## 9. Non-goals

This folder must not:

- store catalog records, proofs, triplets, release manifests, source records, fixtures, schemas, or policy rules;
- call live KGS, USGS, KCC, well-log, borehole, geophysics, or mineral-resource services;
- publish public map, tile, API, UI, Evidence Drawer, Focus Mode, or story-export payloads;
- treat a catalog record or graph/triplet edge as root truth;
- turn mineral/resource descriptions into legal, ownership, leasing, engineering, reserve, or investment conclusions;
- expose precise sensitive subsurface/resource/private-well locations;
- bypass `ReleaseManifest`, review state, correction path, or rollback target; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, or unresolved evidence into a passing result.

---

## 10. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] The test proves catalog closure, not release or botanical/geologic truth by prose.
- [ ] EvidenceRef resolution reaches a concrete EvidenceBundle fixture or mock object.
- [ ] SourceDescriptor, ValidationReport, PolicyDecision, and relevant receipts are represented.
- [ ] STAC/DCAT/PROV/triplet projections remain derivative and do not add unsupported claims.
- [ ] Source-role and resource-class anti-collapse are preserved.
- [ ] Sensitive geometry and rights failures hold or deny rather than pass.
- [ ] Public exposure remains blocked until the release gate.
- [ ] Any path or naming conflict is recorded as drift or verification backlog, not silently normalized.

---

## 11. Current implementation note

This lane is documentation-first. The target README existed as an empty placeholder before this update. The Geology promotion runbook defines catalog closure behavior, and the data catalog/proofs READMEs describe adjacent catalog and proof lanes, but this README does not prove that executable catalog-closure tests, fixtures, validators, or CI wiring already exist.

---

## 12. Definition of done

This README becomes implementation-backed when:

- at least the `GEOL-CAT-001` through `GEOL-CAT-010` scenarios exist as executable tests;
- fixtures exist under the repository's approved Geology fixture home and contain no sensitive real locations;
- tests validate EvidenceRef resolution, EvidenceBundle closure, CatalogMatrix entries, digest closure, and projection alignment;
- source-role/resource-class anti-collapse failures emit finite reason codes;
- exact sensitive geometry and restricted rights cases fail closed;
- catalog closure tests explicitly prove that release still requires ReleaseManifest and rollback target; and
- CI runs this lane without network access.
