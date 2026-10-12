<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-public-safe-geometry-readme
title: Tests — Geology Public-Safe Geometry
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <sensitivity-reviewer> + <geometry-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/geology/SENSITIVITY.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/MAP_UI_CONTRACTS.md
  - docs/domains/geology/EVIDENCE_DRAWER_PAYLOAD.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - packages/domains/geology/geometry/README.md
  - data/receipts/geology/README.md
  - data/proofs/geology/README.md
  - tests/domains/geology/catalog-closure/README.md
  - tests/domains/geology/governed-ai/README.md
  - fixtures/domains/geology/
tags:
  - kfm
  - tests
  - geology
  - geometry
  - public-safe-geometry
  - redaction
  - generalization
  - geometry-role
  - sensitivity
  - release-gated
  - fail-closed
notes:
  - "This README governs the public-safe-geometry test lane under tests/domains/geology/public-safe-geometry/."
  - "It documents intended Geology public-safe geometry test coverage; it does not claim that all tests already exist."
  - "Public-safe geometry is not root truth and not a release decision. It is a validated, policy-supported, receipt-backed derivative suitable for governed public surfaces only after release gates close."
  - "Tests must use synthetic or public-safe fixtures and must not include restricted real-world geometry."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Public-Safe Geometry

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fgeology%2Fpublic--safe--geometry-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-fail--closed-critical?style=flat-square)
![geometry](https://img.shields.io/badge/geometry-public--safe-success?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Geology-domain test lane for public-safe geometry. It proves that geometry shown through public or semi-public surfaces is validated, policy-supported, evidence-linked, receipt-backed, release-gated, and separated from internal/source geometry.

---

## 1. Placement and authority

`tests/domains/geology/public-safe-geometry/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove public-safe geometry rules are enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/geology/` |
| Test lane | `public-safe-geometry/` |
| Primary implementation-adjacent doc | `packages/domains/geology/geometry/README.md` |
| Primary promotion runbook | `docs/runbooks/geology/PROMOTION_RUNBOOK.md` |
| Fixture counterpart | `fixtures/domains/geology/` |
| Adjacent catalog lane | `tests/domains/geology/catalog-closure/` |
| Adjacent AI lane | `tests/domains/geology/governed-ai/` |
| Current implementation status | README path exists; executable tests, fixtures, validators, geometry helpers, policy wiring, and CI remain `UNKNOWN` until verified. |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific proof lanes under `tests/domains/<domain>/`. This lane tests geometry safety; it must not become a geometry package, schema home, policy home, data store, receipt store, proof store, release authority, or fixture home.

---

## 2. What this lane must prove

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Geometry role | Every output geometry has an explicit role such as source-native, internal, derived, generalized, masked, or public-safe. | `GEOMETRY_ROLE_MISSING` or fail. |
| Public-safe distinction | Public-safe geometry is distinct from source/internal geometry and cannot overwrite it. | `GEOMETRY_ROLE_COLLAPSE` or fail. |
| CRS and precision | CRS, scale, precision, and uncertainty are explicit before transform or display. | `CRS_MISSING`, `PRECISION_UNSAFE`, or fail. |
| Transform metadata | Generalization, masking, simplification, aggregation, or suppression emits receipt-ready metadata. | `MISSING_TRANSFORM_METADATA` or fail. |
| Redaction receipt | Public-safe geometry derived from restricted or sensitive geometry carries a RedactionReceipt or equivalent reference. | `MISSING_REDACTION_RECEIPT` or hold. |
| Policy decision | Rights/sensitivity policy evaluated before geometry becomes public-safe. | `POLICY_DECISION_MISSING`, `DENY`, or hold. |
| Evidence linkage | Public-safe geometry links to EvidenceBundle, SourceDescriptor, and validation context. | `MISSING_EVIDENCE` or hold. |
| Catalog/release separation | Passing geometry validation does not imply catalog closure or release. | No public edge. |
| UI/API guard | Public map/API/drawer payloads receive only public-safe or approved generalized geometry. | Output denied or withheld. |
| Finite outcomes | Unsafe or unsupported geometry returns bounded outcomes rather than silent empty success. | Structured fail. |

---

## 3. Expected test families

This folder should eventually contain focused tests for geometry safety and release boundaries.

```text
tests/domains/geology/public-safe-geometry/
├── README.md
├── test_geometry_role_required.py           # PROPOSED
├── test_public_safe_distinction.py          # PROPOSED
├── test_crs_precision_uncertainty.py        # PROPOSED
├── test_transform_metadata.py               # PROPOSED
├── test_redaction_receipt_required.py       # PROPOSED
├── test_policy_decision_required.py         # PROPOSED
├── test_evidence_linkage_required.py        # PROPOSED
├── test_release_gate_separation.py          # PROPOSED
├── test_public_surface_payload.py           # PROPOSED
├── test_finite_geometry_outcomes.py         # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If executable module names use underscores, keep Python filenames with underscores while preserving this requested `public-safe-geometry/` directory path unless a repository-wide naming migration says otherwise.

---

## 4. Fixture expectations

Tests in this lane should be no-network by default. They should use small synthetic geometries and fixture-only evidence/policy records.

Recommended fixture groups:

```text
fixtures/domains/geology/public-safe-geometry/
├── valid/
│   ├── public_safe_unit_polygon.json
│   ├── generalized_reference_point_with_receipt.json
│   ├── masked_sensitive_geometry_with_policy_decision.json
│   ├── simplified_boundary_with_precision_metadata.json
│   └── public_surface_payload_geometry.json
├── invalid/
│   ├── geometry_role_missing.json
│   ├── internal_geometry_used_as_public.json
│   ├── crs_missing.json
│   ├── precision_metadata_missing.json
│   ├── transform_metadata_missing.json
│   ├── redaction_receipt_missing.json
│   ├── policy_decision_missing.json
│   ├── evidence_bundle_missing.json
│   ├── release_gate_bypassed.json
│   └── empty_success_without_outcome.json
└── golden/
    ├── geology_public_safe_geometry_minimal.json
    └── geology_public_safe_geometry_negative_outcomes.json
```

Fixture rules:

- Use synthetic shapes by default.
- Do not include restricted real-world coordinates or private operational details.
- Invalid fixtures should fail for one primary geometry-safety reason where practical.
- Golden fixtures should make input geometry role, output geometry role, transform metadata, evidence link, policy decision, and outcome easy to inspect.

---

## 5. Geometry role vocabulary under test

The vocabulary below is a proposed testing vocabulary, not a new schema authority.

| Role | Meaning | Public posture |
|---|---|---|
| `source_native` | Geometry as supplied by source material. | Not public by default. |
| `internal_exact` | Internal normalized geometry retained for evidence or review. | Not public by default. |
| `interpreted_boundary` | Interpreted geologic boundary, map unit, line, trace, or section. | Public only when source, scale, rights, evidence, and release support it. |
| `derived_generalized` | Geometry generalized, simplified, masked, gridded, or aggregated from a more precise input. | Candidate public-safe only with metadata and policy support. |
| `public_safe` | Geometry approved for public delivery under a governed release profile. | Public only after validation, evidence, policy, review where required, and release. |
| `masked_or_suppressed` | Geometry intentionally withheld or represented only at a safe level. | Public surface may show explanation, not restricted detail. |
| `overview_shape` | Broad bbox, centroid, grid, region, or index geometry for discovery. | Public only if it cannot leak restricted detail and policy allows. |

**Rule:** geometry role is not a release decision. It is an input to validation and policy. Release still requires release-state, correction path, and rollback target.

---

## 6. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `GEOL-GEOM-001` | Valid public-safe geometry passes. | A public-safe geometry fixture with role, CRS, evidence, policy, and release-prep metadata. | Validation passes. |
| `GEOL-GEOM-002` | Missing geometry role fails. | A geometry payload without role. | Validation fails closed. |
| `GEOL-GEOM-003` | Internal geometry cannot publish. | An internal geometry fixture marked for public surface. | Public output is denied or held. |
| `GEOL-GEOM-004` | CRS missing fails. | Geometry without CRS/source-scale context. | Validation fails closed. |
| `GEOL-GEOM-005` | Transform metadata required. | Generalized output without transform metadata. | Validation fails. |
| `GEOL-GEOM-006` | Redaction receipt required where sensitivity applies. | Public-safe derivative missing receipt reference. | Hold or fail. |
| `GEOL-GEOM-007` | Policy decision required. | Geometry output without allow/restrict/deny decision. | Hold or fail. |
| `GEOL-GEOM-008` | Evidence linkage required. | Geometry output without EvidenceBundle or SourceDescriptor linkage. | Hold or fail. |
| `GEOL-GEOM-009` | Release gate cannot be bypassed. | Public-safe candidate marked as published without ReleaseManifest/rollback target. | Public edge denied. |
| `GEOL-GEOM-010` | Empty success forbidden. | Geometry helper returns blank success without outcome/reason. | Test fails. |

---

## 7. Public surface payload checks

This lane should include tests for downstream surfaces while keeping all inputs synthetic.

| Surface | What the test should verify |
|---|---|
| Governed API payload | Only public-safe or approved generalized geometry is returned. |
| Map feature payload | Geometry role and evidence reference remain attached to the rendered feature. |
| Evidence Drawer payload | Restricted geometry details are withheld; transform reason and receipt link are visible where allowed. |
| Focus Mode / AI summary | Generated text does not imply public-safe geometry is root truth or reveal restricted detail. |
| Catalog / triplet projection | Graph and catalog records reference public-safe geometry as derivative, not canonical source geometry. |

---

## 8. Non-goals

This folder must not:

- store geometry data, fixtures, source payloads, receipts, proofs, release manifests, schemas, policy rules, or package code;
- call live source, map, geocoding, model, or geometry services by default;
- decide release, rights, sensitivity, or publication state by test prose alone;
- treat public-safe display geometry as canonical source truth;
- expose restricted real-world coordinates or private operational details;
- bypass EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, correction path, or rollback target; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, missing metadata, missing evidence, or missing receipt into a passing response.

---

## 9. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] Geometry role is explicit.
- [ ] CRS, scale, precision, and uncertainty are represented where material.
- [ ] Transform metadata is receipt-ready.
- [ ] Redaction/generalization outputs carry receipt linkage where required.
- [ ] Policy, evidence, review, release, correction, and rollback boundaries are preserved.
- [ ] Public surfaces receive only public-safe or approved generalized geometry.
- [ ] Failure emits finite reason codes rather than silent success.

---

## 10. Current implementation note

This lane is documentation-first. The target README existed as an empty placeholder before this update. The Geology promotion runbook identifies a public-safe geometry test as a proposed validator target, and the Geology geometry package README describes geometry-role separation and public-safe transform preparation. This README does not prove that executable public-safe geometry tests, fixtures, validators, package helpers, policy wiring, or CI already exist.

---

## 11. Definition of done

This README becomes implementation-backed when:

- at least the `GEOL-GEOM-001` through `GEOL-GEOM-010` scenarios exist as executable tests;
- fixtures exist under the repository's approved Geology fixture home and contain no restricted real-world geometry;
- geometry helper outputs preserve geometry roles, CRS/precision metadata, transform metadata, and finite outcomes;
- policy, evidence, redaction receipt, review, release, correction, and rollback checks are represented;
- public API/map/drawer/AI payload fixtures prove restricted detail is withheld or generalized safely; and
- CI runs this lane without network access.
