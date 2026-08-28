<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass20-expansion-conformance-baseline
title: Pass 20 Expansion Agenda — Repository Conformance Baseline
type: exploratory-conformance-baseline
version: v0.1.0
status: exploratory; repository-grounded; point-in-time; non-authoritative
owners: OWNER_TBD — Docs steward · Architecture steward · Policy steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory-intake; conformance; pass20; no-authority
owning_root: docs/
responsibility: Record a point-in-time, path-evidenced duplicate assay for the Pass 20 EXP-001 through EXP-015 agenda without promoting source proposals or repository file presence into runtime, release, or publication claims.
truth_posture: CONFIRMED repository paths at main@8a671552785b773364f01d2e76d8ca6892a405ea / PARTIAL bounded implementation where named proof criteria are incomplete / OPEN where the proposed owning surface remains unresolved / UNKNOWN hosted, deployed, required-check, live-source, and public behavior
related:
  - ../README.md
  - ../new-ideas-register.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/OBJECT_MAP.md
  - ../../../control_plane/root_registry.yaml
  - ./resource-lifecycle-object-map-source-map.md
notes:
  - "Source proposal: KFM Pass 20 Part 2 expansion agenda EXP-001 through EXP-015."
  - "This is EXP-009's bounded repository scan, not a replacement backlog, architecture authority, release gate, or assertion of deployed behavior."
[/KFM_META_BLOCK_V2] -->

# Pass 20 expansion agenda — repository conformance baseline

> **Snapshot:** `main@8a671552785b773364f01d2e76d8ca6892a405ea`, inspected
> 2026-08-10. This record is deliberately point-in-time. Later repository
> changes must be re-assayed rather than silently treated as covered here.

## Goal

Implement the smallest collision-safe form of Pass 20 `EXP-009`: compare the
fifteen expansion proposals with current repository evidence, identify existing
owners before adding paths, and leave unresolved proof criteria visible.

The scan answers **whether bounded repository surfaces were found**. It does not
answer whether a workflow is required, a source is live, an evaluator is active,
a public client consumes the surface, or a release has occurred.

## Evidence basis

| Evidence | Status in this scan | Use |
|---|---|---|
| Attached `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` (`sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`) | `PROPOSAL LINEAGE` | Supplies the `EXP-001`…`EXP-015` names, dependencies, proof-of-closure statements, and risks. |
| Google Drive `New Ideas 5-15-26` (`gdrive://1boJrrqtqk9DcnzU8zymxFBv83r2-jvbep2kecj7WRCQ`) | `PROPOSAL LINEAGE` | Corroborates fixture-first watcher, materiality-threshold, source-drift, and non-publisher pressure. It is not current endpoint or threshold authority. |
| `docs/doctrine/directory-rules.md` (`sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`) | `CONFIRMED ADOPTED AUTHORITY` through ADR-0029 | Controls path ownership and prevents duplicate roots or parallel authorities. |
| Repository tree at the pinned base | `CONFIRMED POINT-IN-TIME EVIDENCE` | Supports only the file, contract, fixture, validator, test, and workflow observations named below. |

The Drive and attached sources establish implementation pressure. Repository
evidence controls implementation claims.

## Status vocabulary

| Status | Meaning |
|---|---|
| `BOUNDED_CONFIRMED` | A dependency-closed, no-network or fixture-first implementation matching the proposal's core local proof was found. Live integration and authority remain excluded unless separately proved. |
| `PARTIAL` | One or more named surfaces exist, but the proposal's full dependency or proof-of-closure statement is not satisfied. |
| `OPEN` | No collision-safe implementation of the named target was found, or the owning authority remains explicitly unresolved. |
| `THIS_BASELINE` | The current document supplies the bounded point-in-time scan proposed by `EXP-009`; it is not a continuous conformance service. |

File presence alone never means `BOUNDED_CONFIRMED`. The classification also
requires an inspectable contract or standard plus executable validation or
focused tests for the bounded claim.

## Conformance matrix

| ID | Proposal | Snapshot status | Repository evidence | Remaining closure |
|---|---|---|---|---|
| `EXP-001` | CDL/PLANTS source-drift watcher | `PARTIAL` | `tools/ingest/cdl_watch/cdl_watch.py` and its README provide a bounded CDL candidate path; `tools/ingest/plants_watch/` remains README-only. | A shared dependency-closed CDL/PLANTS proof with exact fixture polarity, attestation-deny behavior, and governed outbox binding was not established by this scan. |
| `EXP-002` | PMTiles attestation and sidecar validation | `BOUNDED_CONFIRMED` | `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md`, `tools/validators/pmtiles/validate_attestation_bundle.py`, `fixtures/pmtiles/attestation/`, `tests/validators/test_pmtiles_attestation_bundle.py`, and `.github/workflows/pmtiles-attestation.yml`. | Canonical schema/signature authority, key trust, release approval, and viewer enforcement remain explicitly held. |
| `EXP-003` | Source-watch registry for environmental probes | `PARTIAL` | `contracts/source/watcher_registry.md`, `schemas/contracts/v1/source/watcher_registry.schema.json`, `control_plane/watcher_registry.json`, validator, fixtures, tests, and workflow exist. The registry is `PROPOSED_INACTIVE`; one watcher is a placeholder and another is inactive/manual-only. | Live environmental-probe coverage, accepted threshold bindings, signed probe-receipt reconciliation, dashboard generation, and source activation remain unproved. |
| `EXP-004` | Hash policy ADR by object family | `PARTIAL` | `contracts/common/hash_profile_readiness_matrix.md`, `control_plane/hash_profile_readiness_matrix.json`, schema, validator, tests, and workflow distinguish hash roles. | The contract states that it is not an ADR. Cross-family adoption, algorithm/canonicalization decisions, migration, compatibility, and signature policy remain open. |
| `EXP-005` | Evidence Drawer payloads for source drift and artifact integrity | `BOUNDED_CONFIRMED` | `contracts/ui/evidence_drawer_drift_integrity_profile.md` reuses the existing public-safe schema and fixtures cover drift, missing sidecar, unresolved provenance, rights denial, and hash error; focused validator/tests and workflow exist for the parent payload. | Source comparison, artifact verification, rights/policy evaluation, and deployed UI behavior are outside the bounded proof. |
| `EXP-006` | STAC profiles for CDL and PMTiles | `OPEN` | `docs/standards/STAC.md`, `docs/standards/stac.md`, and `docs/standards/PMTILES.md` contain draft relationships; no collision-safe CDL-and-PMTiles profile/schema/fixture/validator pair was found. | Resolve the competing STAC profile/namespace surfaces, then land local Item fixtures and link-closure validation without treating PMTiles as evidence. |
| `EXP-007` | Domain source-role matrices | `PARTIAL` | Explicit matrices exist for geology, hazards, and hydrology; multiple domain `SOURCES.md` files contain role material. | A complete domain inventory, one accepted role vocabulary, LayerManifest references, machine parity checks, and maintenance ownership were not established. |
| `EXP-008` | Threshold policy registry | `OPEN` | Domain threshold profiles and validators exist, but searches found no canonical cross-domain registry. Multiple domain backlogs still call the registry `PROPOSED`. | Add only an inactive, steward-reviewable registry candidate first; do not adopt illustrative values or bind watchers until domain policy review is explicit. |
| `EXP-009` | Live repository conformance scan | `THIS_BASELINE` | This point-in-time matrix records the base commit, source lineage, status vocabulary, collisions, owners, and remaining closure. | Continuous scanning, hosted observation, drift notification, and automatic backlog mutation are excluded. Re-run manually after material repository changes. |
| `EXP-010` | Publication-deny dry run | `BOUNDED_CONFIRMED` | `tools/release/release_dry_run.py` and `tests/release/test_publication_deny_dry_run.py` deterministically exercise five deny paths, emit no files, use no network, and create no authority. | Required-check status, full validator coverage, release assembly, and actual publication enforcement remain unproved. |
| `EXP-011` | Sensitive exact-location denial fixtures | `PARTIAL` | Archaeology exact-location Rego and focused tests exist; roads/rail/trade includes a public-generalization receipt test; additional domain sensitivity rules exist. | One cross-domain fixture matrix for nests, dens, roosts, archaeology, and infrastructure with exact-deny/generalized-allow polarity was not found. |
| `EXP-012` | Resource ontology and API lifecycle map | `BOUNDED_CONFIRMED` | `contracts/OBJECT_MAP.md` is extended through the bounded implementation mapped by `docs/intake/exploratory/resource-lifecycle-object-map-source-map.md`, with validator and tests. | Completeness, production routes, deployed behavior, and public availability remain out of scope. |
| `EXP-013` | Temporal-support acceptance criteria | `PARTIAL` | `contracts/evidence/temporal_support_assessment.md`, paired schema, valid/invalid fixtures, validator, and tests establish evidence-support assessment. | A shared acceptance profile spanning tiles, LayerManifest, EvidenceBundle, PolicyDecision, and AI envelopes was not established. |
| `EXP-014` | Planning scenario manifest | `BOUNDED_CONFIRMED` | `contracts/domains/water_planning/planning_scenario_manifest.md`, paired schema, synthetic cases, validator, and tests provide a Kansas water-planning candidate. | Public-safe summary consumption, Evidence Drawer binding, steward participation, and release remain outside the local proof. |
| `EXP-015` | MapLibre layer-registry validator | `PARTIAL` | The strict inactive `LayerManifest` profile, `tools/validators/data/validate_layer_manifest.py`, runtime admission projection, Explorer admission code, fixtures, and tests fail closed on several trust boundaries. | A live layer registry, reference resolution, artifact/signature verification, accepted renderer-binding policy, and production MapLibre registration gate remain absent. |

## Collision findings

The scan rejects several tempting duplicate implementations:

1. Do not create a second watcher registry beside `control_plane/watcher_registry.json`.
2. Do not create another Evidence Drawer schema for drift/integrity; the existing
   subordinate profile intentionally reuses the public-safe payload.
3. Do not create another LayerManifest authority under `contracts/map/` or
   `contracts/runtime/`; the current object contract is
   `contracts/data/layer_manifest.md`, with compatibility seams preserved.
4. Do not call the hash-readiness matrix an adopted policy or ADR.
5. Do not turn domain-local illustrative threshold files into a cross-domain
   authority by aggregation.

## Candidate queue after the scan

| Priority | Candidate | Why it is collision-safe | Required boundary |
|---|---|---|---|
| 1 | `EXP-008` inactive threshold-policy registry candidate | No canonical cross-domain registry was found; existing policy-root guidance permits inactive candidate registries with paired semantics, shape, fixtures, validator, and tests. | No live numeric policy adoption, watcher binding, policy evaluation, source activation, promotion, release, or publication. |
| 2 | `EXP-006` STAC CDL/PMTiles profile decision packet | The gap is real, but competing STAC documents and namespaces make direct schema implementation unsafe. | Start with conflict resolution and an accepted owner; do not add another profile file first. |
| 3 | `EXP-011` cross-domain location-safety parity assessment | Domain implementations exist, so a parity assessment could reveal exact missing cases without replacing domain policy. | Synthetic locations only; no sensitive coordinate payloads or weakening of existing deny rules. |

This ordering is a review recommendation, not an implementation authorization.

## Path decision

| Question | Decision |
|---|---|
| What responsibility is created? | Non-authoritative source-to-repository conformance reasoning. |
| Existing owner? | `docs/intake/exploratory/` is the adopted waiting room for source maps, duplicate assays, and promotion candidates. |
| New root or parallel authority? | No. |
| Why not `docs/reports/`? | This is manually authored exploratory intake, not a generated or released report. |
| Why not `control_plane/`? | The matrix must not become runtime registry state or mutate the verification backlog. |
| Why not contracts, schemas, or policy? | It defines no object meaning, machine shape, or admissibility rule. |

## Validation and non-effects

Reviewers can replay the bounded assay with repository-local `find`, `rg`, file
inspection, and the named focused tests. A clean Markdown/link result proves
only that this record is readable and points at the inspected checkout.

This baseline does not:

- fetch or activate a source;
- adopt a threshold or hash policy;
- execute a watcher, policy evaluator, release gate, or renderer;
- mutate a registry, backlog, lifecycle record, receipt, proof, or release;
- establish required-check, deployment, runtime, or public behavior; or
- authorize promotion, release, publication, or public use.

## Refresh and rollback

Refresh by creating a new reviewed revision that names a new base commit and
explains every status change. Never edit the base SHA without replaying the
assay.

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the documentation commit. No live source, registry,
policy, release, deployment, or public artifact requires cleanup.
