<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/verification-backlog
title: Soil - Verification Backlog
type: domain-verification-backlog
version: v1.0
status: active; repository-grounded; open
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Source and rights steward
  - OWNER_TBD - Policy and release steward
created: 2026-05-19
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: Human-readable Soil verification queue; does not replace machine registries, tests, policy, review, or release decisions
truth_posture: CONFIRMED current-session path inventory and bounded executable evidence / PROPOSED backlog ordering / UNKNOWN source, runtime, proof, release, and deployment state unless explicitly verified
evidence_snapshot: "repository=bartytime4life/Kansas-Frontier-Matrix; base_commit=813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80; planning_lineage_sha256=7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea"
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/MISSING_OR_PLANNED_FILES.md
  - docs/domains/soil/EXPANSION_BACKLOG.md
  - docs/domains/soil/VERIFICATION.md
  - data/registry/soil/verification_backlog.yaml
  - docs/registers/VERIFICATION_BACKLOG.md
  - .github/workflows/domain-soil.yml
  - .github/workflows/soil-moisture-observation.yml
tags: [kfm, soil, verification, backlog, evidence, no-network, source-admission, release-hold]
notes:
  - "Replaces a three-line greenfield placeholder with a current-session repository inventory."
  - "The supplied Soil architecture report is design lineage; its proposed paths do not become repository authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil verification backlog

This is the Soil lane's human-readable queue for evidence that is still needed.
It records current repository state without turning path presence, fixtures,
validator success, or workflow success into source admission, scientific truth,
policy approval, proof closure, release, deployment, promotion, or publication.

## Current result

At `main@813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80`, Soil is
`PARTIAL / FIXTURE-FIRST / RELEASE-HELD`.

- The canonical Soil schema lane contains 38 JSON schema files with mixed
  maturity: several strict profiles coexist with permissive or compatibility
  surfaces.
- The Soil validator lane contains 23 Python files with mixed maturity.
- Forty-one Soil-related Python files are present across test roots. Presence
  is inventory evidence, not proof that every file is executable or CI-bound.
- [`domain-soil.yml`](../../../.github/workflows/domain-soil.yml) runs three
  bounded synthetic fixture suites plus the SSURGO package-drift fixture proof.
  Its proof and release-dry-run jobs are explicit holds.
- [`soil-moisture-observation.yml`](../../../.github/workflows/soil-moisture-observation.yml)
  separately runs the strict SoilMoistureObservation contract, schema, fixture,
  validator, test, and retained-receipt profile. It does not yet inject the
  shared Python startup no-network guard.
- Ten files exist directly under the canonical Soil source-registry lane.
  None establishes source activation by itself.
- No Soil candidate record or Soil proof artifact exists beyond README and
  placeholder material in the inspected candidate/proof lanes.
- The Soil-specific machine file, planned-file, and verification registers
  remain empty templates. This document does not silently populate or replace
  them.

## Authority and closure rules

1. Close an item only against exact repository evidence, a current external
   source record, an accepted decision, a reviewed test result, or an emitted
   artifact appropriate to the claim.
2. Keep source identity, rights, sensitivity, schema validity, scientific
   fitness, evidence closure, policy result, review, promotion, release, and
   publication as separate states.
3. Move cross-domain items to the repository-wide
   [verification backlog](../../registers/VERIFICATION_BACKLOG.md) when Soil no
   longer owns the whole question.
4. Preserve stable item IDs when an item closes, moves, or is superseded.

## Open queue

| ID | Verification item | Current evidence | State | Evidence needed to close |
|---|---|---|---|---|
| `SOIL-VB-001` | Assign accountable owners | Soil docs, tests, and validator indexes still use `OWNER_TBD` | `OPEN` | Reviewed owner bindings and routing evidence; CODEOWNERS alone is not proof of review |
| `SOIL-VB-002` | Converge support-type vocabulary | Strict support profiles and an alias-map validator exist, while older docs and smoke fixtures use different token sets | `PARTIAL / CONFLICTED` | One reviewed semantic vocabulary, compatibility map, schema bindings, fixtures, negative tests, and consumer inventory |
| `SOIL-VB-003` | Reconcile source-registry identity and path history | Canonical `data/registry/sources/soil/` exists; historical Soil registry shapes also remain | `PARTIAL` | Single-writer inventory, source-ID crosswalk, consumer map, migration or alias decision, and rollback |
| `SOIL-VB-004` | Verify source rights and activation state | Source descriptors and human source pages are present; no activation decision is established here | `OPEN / HOLD` | Current terms, role, steward, cadence, sensitivity, redistribution, attribution, activation decision, fixture proof, and rollback for one source |
| `SOIL-VB-005` | Classify strict, permissive, and compatibility schemas | Strict object-family profiles coexist with permissive three-property and alias schemas | `PARTIAL` | Per-schema authority classification, canonical target, consumer evidence, invalid fixtures, and compatibility exit criteria |
| `SOIL-VB-006` | Bind implemented validators to declared CI profiles | `domain-soil` names three suites while additional profiles use dedicated workflows or remain isolated; the repository has no reviewed aggregate coverage projection | `PARTIAL` | Exact profile registry, deterministic commands, startup no-network enforcement, expected outcomes, and hosted exact-head evidence |
| `SOIL-VB-007` | Replace placeholder package and pipeline behavior | Soil package modules and lifecycle stage modules still identify as placeholders | `OPEN / HOLD` | One contract/schema/source/policy/fixture-closed offline transformation with tests and a reversible lifecycle boundary |
| `SOIL-VB-008` | Establish executable Soil policy evaluation | Soil Rego files are present, but this review did not establish a bound policy runtime and decision receipt | `OPEN / HOLD` | Policy input contract, pinned evaluator, allow/deny/abstain fixtures, decision output, review, and CI evidence |
| `SOIL-VB-009` | Close evidence and catalog support for one candidate | A fixture-only catalog-closure assessment exists; no accepted Soil EvidenceBundle/proof packet is present | `PARTIAL / HOLD` | Resolvable EvidenceRefs, EvidenceBundle, validation report, policy result, catalog identity, correction target, and reviewed closure |
| `SOIL-VB-010` | Establish proof and release dry-run implementation | Workflow jobs explicitly retain proof and release holds; candidate and proof lanes contain no material records | `OPEN / HOLD` | Proof producer, candidate manifest contract, exact digests, review separation, correction/withdrawal, rollback target, and dry-run readback |
| `SOIL-VB-011` | Verify governed API, MapLibre, Evidence Drawer, export, and Focus Mode behavior | Human contracts exist; no released Soil carrier or verified deployed resolver is established | `OPEN / HOLD` | Released public-safe fixture carrier, governed resolver, UI tests, citation behavior, sensitivity denial, stale state, rollback, and deployed readback |
| `SOIL-VB-012` | Reconcile human and machine planning registers | This human backlog is populated; `data/registry/soil/verification_backlog.yaml` remains an empty template | `OPEN` | Accepted projection contract, schema, generator or single-writer process, parity validation, and correction path |

## Bounded proof already available

These profiles can support future closure work but do not close the queue by
themselves:

- public-safe Soil fixture validation;
- station soil-moisture validation;
- SMAP L4 support-type anti-collapse;
- SoilMoistureObservation finite outcomes and multi-clock validation;
- support-type profile and alias-map validation;
- map-unit, component, and component-horizon profile validation;
- time-caveat, watcher-spec, yearly-diff, promotion-materiality, and catalog-
  closure fixture profiles;
- public-safe Soil-Agriculture and Soil-Hydrology context fixtures.

## Review checklist

- [ ] The exact base and changed paths are recorded.
- [ ] An item is not marked closed from path presence alone.
- [ ] Unknown rights, sensitivity, or source role continues to fail closed.
- [ ] Station, satellite grid, static survey, profile, interpretation, and
      derived support remain distinct.
- [ ] Tests run without live source access.
- [ ] Public clients remain downstream of governed released carriers.
- [ ] Correction, withdrawal, derivative invalidation, and rollback remain
      explicit.

[Back to top](#top)
