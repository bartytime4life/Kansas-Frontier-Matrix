<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-probes-comid-huc12-readme
title: tools/probes/comid_huc12 README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-contract-schema-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public; diagnostic-probe; dry-run-only; no-publication
owning_root: tools/
responsibility: proposed dry-run diagnostic probe for COMID to HUC12 crosswalk rules, fixture checks, and reviewer handoff reports
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hydrology/CROSSWALK_RULES.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../contracts/domains/hydrology/huc_unit.md
  - ../../../contracts/domains/hydrology/
  - ../../../schemas/
  - ../../../policy/
  - ../../../data/registry/sources/
  - ../../../data/raw/hydrology/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README defines a proposed diagnostic probe boundary, not a confirmed implementation."
  - "The COMID -> HUC12 crosswalk recipe is deterministic, per release, fail-closed, and ambiguity-preserving. This probe may exercise that recipe against fixtures or local sidecars, but it must not create the authoritative crosswalk."
  - "COMID is a legacy compatibility key; hydrology identity should preserve source_id, object_role, temporal_scope, normalized digest, source versions, EvidenceRefs, and crosswalk manifest discipline."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/probes/comid_huc12

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-COMID--HUC12--probe-informational)
![mode](https://img.shields.io/badge/mode-dry--run--diagnostic-lightgrey)
![posture](https://img.shields.io/badge/posture-fail--closed-success)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/probes/comid_huc12/` is the proposed dry-run diagnostic probe lane for checking COMID → HUC12 crosswalk behavior against KFM hydrology rules. It may produce fixture reports and reviewer handoffs, but it is not a connector, not the crosswalk pipeline of record, not a manifest authority, not an EvidenceBundle creator, not a release path, and not hydrology truth.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Probe boundary](#probe-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [COMID → HUC12 probe posture](#comid--huc12-probe-posture)
- [Fallback ladder under test](#fallback-ladder-under-test)
- [Finite outcomes](#finite-outcomes)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/probes/comid_huc12/` exists to hold a small, deterministic diagnostic probe for the Hydrology lane's COMID → HUC12 crosswalk rules.

The probe may exercise the documented fallback ladder, relationship typing, geometry-sanity flags, alignment scoring, source-version pinning, and ABSTAIN behavior against public-safe fixtures or local sidecars. Its job is to expose whether a proposed crosswalk implementation behaves according to the documented rules before any governed pipeline, manifest, proof, catalog, or release workflow depends on it.

The durable KFM question for this lane is:

> Does a candidate COMID → HUC12 crosswalk assignment preserve deterministic fallback order, version pinning, alignment evidence, relationship type, ambiguity flags, and ABSTAIN semantics?

The answer should be a probe report. It should never be an authoritative crosswalk record, source capture, processed Hydrology object, EvidenceBundle, DSSE manifest, catalog closure, release manifest, public API payload, or map layer.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/probes/comid_huc12/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Probe executable | **PROPOSED-to-create / NEEDS VERIFICATION** | No script name is claimed as implemented by this README. |
| Parent `tools/probes/README.md` | **NEEDS VERIFICATION / absent in current check** | Parent probe contract should be added before expanding probe tooling broadly. |
| Hydrology crosswalk rules | **CONFIRMED in repo evidence / draft** | Crosswalk rules define deterministic fallback, relationship typing, alignment score, geometry flags, ABSTAIN, manifest posture, and version pinning. |
| Hydrology identity model | **CONFIRMED in repo evidence / draft** | Hydrology identity uses source id, object role, temporal scope, and normalized digest; COMID is not the sole identity authority. |
| Threshold constants | **PROPOSED / NEEDS VERIFICATION** | Alignment thresholds are design pressure and must be ratified before enforcement. |
| Crosswalk manifest authority | **DENY here** | Probe output cannot create or sign authoritative manifests. |
| Publication authority | **DENY here** | Probe output cannot publish or promote. |
| Hydrology truth authority | **DENY here** | Probe output is diagnostic only. |

> [!IMPORTANT]
> A passing probe report is not acceptance of a crosswalk. It means a candidate implementation behaved as expected against the supplied fixture. Governed acceptance still requires source descriptors, contracts, schemas, policy checks, receipts/proofs, validation, catalog closure, release review, and rollback controls where applicable.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `tools/probes/` is **PROPOSED** as a diagnostic sub-tree for dry-run probes and smoke checks. Hydrology crosswalk rules live in `docs/domains/hydrology/CROSSWALK_RULES.md`; contracts, schemas, policy, source descriptors, lifecycle data, receipts, proofs, catalog records, and release manifests live outside this probe lane.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/probes/comid_huc12/README.md`.
- **PROPOSED:** dry-run probe code may live here if it is deterministic, fixture-driven, report-oriented, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/probes/` is or should become a canonical probe parent under `tools/`.
- **NEEDS VERIFICATION:** where the production COMID → HUC12 crosswalk pipeline, manifest writer, and validator should live after implementation evidence exists.
- **DENY:** any use of this path as source connector, authoritative crosswalk store, processed data store, EvidenceBundle/proof root, catalog/triplet root, release root, or public API.

[Back to top](#top)

---

## Probe boundary

This lane is a diagnostic probe, not production transformation.

It may:

- load small fixtures;
- compare expected and actual probe reports;
- compute a candidate fallback rung;
- compute a candidate alignment score;
- classify relationship type;
- surface geometry-sanity flags;
- return ABSTAIN / DENY / REVIEW outcomes;
- emit deterministic JSON reports;
- support CI or reviewer smoke checks.

It must not:

- fetch source data of record;
- write `data/spatial/comid_huc12/.../manifest.json`;
- sign DSSE manifests;
- create EvidenceBundles, PolicyDecisions, ReviewRecords, or ReleaseManifests;
- mutate source descriptors;
- write to lifecycle data roots;
- publish map tiles or API payloads;
- silently choose a best match when ambiguity remains.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/probes/comid_huc12/` include:

- dry-run probe scripts for COMID → HUC12 fixtures;
- fallback-ladder demonstration helpers;
- alignment-score calculators for small synthetic geometries;
- geometry-sanity flag probes;
- relationship-type classifiers for `exact`, `split`, `merge`, and `retired` cases;
- ABSTAIN negative-fixture probes;
- source-version-pair checks for NHDPlus/WBD fixtures;
- deterministic report emitters;
- fixture comparison utilities;
- reviewer handoff summaries.

A helper belongs here only when it is deterministic, no-network by default, explicit about fixture paths, explicit about source version pairs, and unable to write authoritative outputs.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/probes/comid_huc12/` | Correct home | Reason |
|---|---|---|
| Source fetchers for NHDPlus, WBD, or USGS crosswalks | `connectors/` or ratified connector home | Connectors own source acquisition and admission. |
| Production crosswalk pipeline logic | `pipelines/domains/hydrology/...` or accepted pipeline home | Pipelines own lifecycle normalization and manifest generation. |
| Authoritative crosswalk manifests | governed data / artifact root after ADR or pipeline decision | Probe output is not source of record. |
| Source descriptors | `data/registry/sources/` | Source identity, role, rights, cadence, and activation live in the registry. |
| Contracts or schemas | `contracts/`, `schemas/` | Meaning and field shape are separate authority roots. |
| Policy rules or thresholds | `policy/` and ratified ADR/policy docs | Probe can exercise thresholds but not own them. |
| Raw source captures | `data/raw/` | RAW is a lifecycle state. |
| Quarantine records | `data/quarantine/` | Holds are lifecycle artifacts. |
| Processed hydrology records | `data/processed/` | Validated records are not probe code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog/graph closure is downstream. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are outside probe code. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Public maps or API behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/probes/comid_huc12/` or existing test convention | Tests prove this probe; they are not the probe lane itself. |

[Back to top](#top)

---

## COMID → HUC12 probe posture

The probe should be understood as a **diagnostic reviewer aid** for a known high-risk join key.

It may create:

- a probe run report;
- a fallback-ladder report;
- an alignment-score report;
- a geometry-flag report;
- a relationship-type report;
- an ABSTAIN negative-fixture report;
- a version-pair mismatch report;
- a reviewer handoff summary.

It must not create:

- a production crosswalk record;
- a released crosswalk manifest;
- a DSSE signature;
- a processed `ReachIdentity` or `HUCUnit` record;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a map tile or PMTiles release;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what fixture or local sidecar was inspected, what rung was used, what ambiguity or geometry flags appeared, and what downstream validation or steward review must happen next.

[Back to top](#top)

---

## Fallback ladder under test

The probe should exercise the documented deterministic ladder without treating the result as authoritative.

| Rung | Method | Expected decision token | Probe duty |
|---|---|---|---|
| 1 | Official COMID → HUC12 crosswalk for the NHDPlus/WBD version pair. | `official_crosswalk` | Prefer when fixture says official mapping is available. |
| 2 | Polygon overlay, area-weighted majority. | `area_weighted_overlay` | Verify highest-area HUC12 is selected when official mapping is absent. |
| 3 | Catchment centroid-in-polygon. | `centroid_in_polygon` | Verify centroid fallback only occurs after overlay is unresolved. |
| 4 | Snap-to-pour-point. | `snap_to_pour_point` | Verify outlet fallback only occurs after centroid fallback is unresolved. |
| — | No admissible assignment. | `abstain` | Verify unresolved cases produce finite ABSTAIN, not guessed assignment. |

Rules to preserve:

- The ladder is fixed and total.
- The winning rung is recorded.
- `alignment_score` and geometry flags are carried on the report.
- `relationship_type` is explicit.
- Split/merge/retired cases are not forced into one-to-one joins.
- Version pairs are pinned.
- Ambiguity is recorded, not suppressed.

[Back to top](#top)

---

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PROBE_PASS` | Fixture result matches the expected probe report. |
| `PROBE_FAIL` | Fixture result differs from expectation. |
| `OFFICIAL_CROSSWALK_USED` | Probe selected the official mapping rung. |
| `AREA_WEIGHTED_OVERLAY_USED` | Probe selected the area-weighted overlay rung. |
| `CENTROID_IN_POLYGON_USED` | Probe selected the centroid fallback rung. |
| `SNAP_TO_POUR_POINT_USED` | Probe selected the outlet fallback rung. |
| `RELATIONSHIP_TYPE_REVIEW` | `split`, `merge`, or `retired` relationship requires review. |
| `ALIGNMENT_SCORE_REVIEW` | Alignment score or geometry flags require review. |
| `VERSION_PAIR_MISMATCH` | NHDPlus/WBD version pair is missing, mixed, or inconsistent. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor reference is absent. |
| `ABSTAIN` | No admissible assignment exists with available evidence. |
| `ERROR` | Probe could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- Public-safe fixture JSON.
- Small synthetic geometry fixtures.
- Prior expected report JSON.
- Local sidecar JSON with NHDPlus version and WBD snapshot values.
- SourceDescriptor references.
- Candidate COMID / permanent identifier / HUC12 values.
- Geometry-sanity flags.
- Alignment-score fixtures.
- Relationship-type fixtures.

### Unsuitable inputs

- credentials or secrets;
- raw source downloads outside lifecycle control;
- production-scale data captures treated as probe fixtures;
- mixed NHDPlus/WBD vintages without explicit negative-test intent;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling;
- any output path under catalog, proofs, receipts, published, or release roots.

### Suitable outputs

- probe JSON report;
- expected-vs-actual diff report;
- alignment-score report;
- relationship-type report;
- version-pair mismatch report;
- ABSTAIN report;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A probe should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice COMID → HUC12 probe report should be compact and deterministic.

```json
{
  "tool": "comid-huc12-probe",
  "status": "PROBE_PASS",
  "fixture_id": "area_weighted_overlay_basic",
  "source_pair": {
    "nhdplus_version": "fixture_nhdplus_v2_1",
    "wbd_snapshot": "fixture_wbd_snapshot"
  },
  "input": {
    "comid": "12345678",
    "permanent_identifier": null,
    "candidate_huc12s": ["102600010101", "102600010102"]
  },
  "checks": {
    "source_descriptor_ref": "present",
    "fallback_rung": "area_weighted_overlay",
    "relationship_type": "split",
    "alignment_score": 0.68,
    "geometry_flags": ["multi_huc_candidate"],
    "version_pair_pinned": true,
    "abstain_required": false
  },
  "decision": {
    "outcome": "RELATIONSHIP_TYPE_REVIEW",
    "reason_codes": ["AREA_WEIGHTED_OVERLAY_USED", "MULTI_HUC_CANDIDATE"],
    "publication": false,
    "manifest_created": false,
    "evidence_bundle_created": false,
    "release_decision_created": false
  },
  "next_review": [
    "confirm source descriptors and version pair",
    "preserve ranked multi-HUC candidate list",
    "validate crosswalk schema and policy thresholds before manifest work",
    "do not publish without receipt, proof, release manifest, and rollback controls"
  ]
}
```

Reports are not receipts unless a separate governed workflow adopts them and stores them under the proper receipt root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/probes/comid_huc12/
├── README.md
├── test_comid_huc12_probe.py
└── fixtures/
    ├── official_crosswalk/
    │   ├── input.json
    │   └── expected_report.json
    ├── area_weighted_overlay/
    │   ├── input.json
    │   └── expected_report.json
    ├── centroid_in_polygon/
    │   ├── input.json
    │   └── expected_report.json
    ├── snap_to_pour_point/
    │   ├── input.json
    │   └── expected_report.json
    ├── multi_huc_abstain/
    │   ├── input.json
    │   └── expected_report.json
    └── version_pair_mismatch/
        ├── input.json
        └── expected_report.json
```

Recommended assertions:

- official mapping fixture selects `official_crosswalk`;
- overlay fixture selects `area_weighted_overlay` only when official mapping is absent;
- centroid fixture selects `centroid_in_polygon` only after overlay is unresolved;
- outlet fixture selects `snap_to_pour_point` only after centroid fallback is unresolved;
- unresolved multi-HUC fixture returns `ABSTAIN`;
- `split`, `merge`, and `retired` fixtures preserve `relationship_type`;
- alignment scores and geometry flags are emitted deterministically;
- mixed or missing version pair returns `VERSION_PAIR_MISMATCH`;
- missing SourceDescriptor reference returns `SOURCE_DESCRIPTOR_MISSING` or `ABSTAIN`;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/probes/comid_huc12
```

```bash
python tools/probes/comid_huc12/comid_huc12_probe.py \
  --input tests/probes/comid_huc12/fixtures/area_weighted_overlay/input.json \
  --expected tests/probes/comid_huc12/fixtures/area_weighted_overlay/expected_report.json \
  --output .tmp/comid-huc12-probe-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `comid_huc12_probe.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing COMID → HUC12 probe code, reviewers should confirm:

- [ ] The probe is dry-run diagnostic tooling only.
- [ ] The probe cannot fetch source material as the source-admission path of record.
- [ ] The probe cannot write authoritative crosswalk manifests.
- [ ] The probe cannot create EvidenceBundles, policy decisions, release manifests, or map outputs.
- [ ] Source descriptor references are required.
- [ ] NHDPlus and WBD version pair is explicit and pinned.
- [ ] Fallback ladder order is fixed.
- [ ] Winning rung and decision reason are recorded.
- [ ] Alignment score and geometry flags are deterministic.
- [ ] Relationship type is explicit and not forced one-to-one.
- [ ] Ambiguous cases produce ABSTAIN or review outcomes, not guessed assignments.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Outputs are deterministic and machine-readable.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with governed COMID → HUC12 probe contract | **DONE in this README** | Establishes diagnostic boundary and fail-closed posture. |
| Add parent `tools/probes/README.md` | **PROPOSED** | Clarifies probe tooling under `tools/`. |
| Add `comid_huc12_probe.py` dry-run helper | **PROPOSED** | Emits deterministic probe report from fixtures. |
| Add public-safe fixtures | **PROPOSED** | Proves official, overlay, centroid, outlet, multi-HUC ABSTAIN, and version-mismatch cases. |
| Align report envelope with schemas/policy | **PROPOSED / NEEDS VERIFICATION** | Match accepted Hydrology crosswalk contracts and thresholds once ratified. |
| Wire into CI as non-blocking diagnostic signal | **PROPOSED / later** | Surfaces crosswalk drift without source-admission, manifest, or release side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add parent `tools/probes/README.md`, then add `tests/probes/comid_huc12/README.md` and public-safe fixtures for the fallback ladder and ABSTAIN cases. |
