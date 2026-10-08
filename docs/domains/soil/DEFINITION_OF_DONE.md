<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/definition-of-done
title: Soil definition of done
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil definition of done; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/VERIFICATION.md
  - docs/domains/soil/VERIFICATION_BACKLOG.md
  - .github/workflows/domain-soil.yml
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# DEFINITION OF DONE

“Done” must name the completed scope. A document, fixture profile, source review,
transformation, catalog candidate and release have different completion evidence.
This checklist is a review aid, not a replacement for owning decisions.

## Completion by deliverable

| Deliverable | Minimum evidence | Does not establish |
|---|---|---|
| Documentation | Exact-source claims, real links, metadata, preserved history and clear unknowns | Implementation or accepted doctrine |
| Contract/schema profile | Paired meaning and shape, closed invalid behavior, version/compatibility rationale | Scientific truth or source admission |
| Fixture validator | Deterministic positive and negative outcomes, malformed-input behavior, bounded inputs | Live ingestion, policy approval or release |
| Source review packet | Exact product/edition, role, rights, sensitivity, access/cadence and accountable decision | Capture, activation or publication unless separately decided |
| Offline transform | Reproducible permitted input/output, units/depth/time lineage, uncertainty and failure handling | Production operation or catalog closure |
| Catalog review candidate | Every required declared dimension plus independently resolvable support | Catalog write or review approval |
| Governed release | Exact artifacts, evidence, policy, review, manifest, correction and rollback | Hosted rendering or user acceptance without readback |
| Site change | Source tests and precise implementation identity | Provider availability, deployment or browser acceptance |

## Soil-specific invariants

- Map units, components and horizons retain native-key and source-vintage lineage.
- Component percentages and vertical depth intervals keep their units and methods.
- Station observations, satellite/model grids, static surveys, pedons and
  interpretations remain distinct support types.
- Observation time, source publication/vintage and retrieval time are not swapped.
- Missing, stale, uncertain and partial data remain visible and do not become zero.
- Public precision and cross-domain joins pass the applicable sensitivity review.
- Evidence and validation bind the exact candidate and relevant code/schema version.
- Correction, withdrawal and rollback can reach affected consumers.

## Practical review sequence

1. State one observable outcome and identify the exact base and changed paths.
2. Read the current owning contract, schema, fixture and consumer before widening
   an existing profile or adding an alias.
3. Run the smallest relevant suite from the [verification guide](VERIFICATION.md),
   preserving no-network behavior for synthetic checks.
4. Read emitted finite outcomes as well as exit codes. A valid `HOLD` or `DENY`
   declaration may be a successful test of fail-closed behavior.
5. Classify inherited failures separately from introduced failures. Do not
   change baselines, receipts or policy merely to produce a pass.
6. Record reviewer roles, actual results and remaining gates without inventing
   named owners or approval.

## Current standing limits

The [domain workflow](../../../.github/workflows/domain-soil.yml) includes
explicit proof and release dry-run holds. The
[catalog assessment](CATALOG_CLOSURE.md) checks declarations only. The
[identity candidate](IDENTITY_MODEL.md) is inactive. These controls can be
successfully validated while source admission, evidence resolution and release
remain unresolved.

## Review record

A complete result states: scope; repository/base/head; input and output identities;
commands and results; failure/negative coverage; source and support roles; rights
and sensitivity posture; review state; unresolved questions; correction and
rollback path. Link evidence rather than copying private payloads into prose.

## Reopening a completed item

Reopen or supersede an item when source rights, product edition, support type,
method, schema, policy or consumer assumptions change. Preserve the old evidence
and explain why it no longer establishes the new claim. Use the
[verification backlog](VERIFICATION_BACKLOG.md) for unresolved evidence and
[release index](RELEASE_INDEX.md) for release navigation.
