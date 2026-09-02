<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-analytical-view-manifest
title: Pass 18 Analytical View Manifest Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Data contract steward · Analytics steward · Database steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; data; analytics; database-view; check-option
responsibility: Preserve source and repository lineage for a bounded analytical-view manifest without turning view metadata into database, data-mutation, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive metadata, and inspected-repository comparison; PROPOSED bounded adaptation; UNKNOWN database portability and consumer adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/data/analytical_view_manifest.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../contracts/governance/query_run_record.md
  - ../../../contracts/ui/view_registry_profile.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Analytical View Manifest Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 225-226 / printed pages 222-223 | Card `KFM-P18-INV-107` proposes documenting database/materialized-view definition, purpose, validation status, SQL digest, and upstream tables as contract surfaces. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Same supplied dossier, physical PDF pages 257-258 / printed pages 254-255 | Card `KFM-P18-INV-311` proposes distinguishing read-only views from governed write-through views and declaring `WITH CHECK OPTION`-style predicate preservation. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| `contracts/data/layer_manifest.md` | The existing manifest binds one map-layer representation to catalog, artifact, policy, review, and release references. It does not describe a database/materialized-view definition or write-through predicate guard. | `CONFIRMED` adjacent, non-duplicate family |
| `contracts/ui/view_registry_profile.md` | The UI profile resolves routes to governed delivery contracts and explicitly excludes embedded queries and direct database endpoints. It is not a database-view manifest. | `CONFIRMED` adjacent, non-duplicate family |
| `contracts/governance/query_run_record.md` | The query-run record describes one governed query iteration. It is not a stable view definition, upstream-dependency, refresh, or mutation contract. | `CONFIRMED` adjacent, non-duplicate family |
| Starting `main@12911a862033546160737479681bed0ac68d1f7b` plus GitHub PR/code searches | No exact source-card IDs, analytical-view manifest, database/materialized-view contract, predicate-guard profile, schema, fixture family, validator, workflow, branch, or PR was found before implementation. | `CONFIRMED` inspected snapshot |

The source artifacts are design evidence, not repository instruction authority.
Placement and scope follow accepted Directory Rules and current responsibility
roots.

## Selected increment

The implementation is a small, additive `contracts/data/` manifest. It binds a
safe definition digest and dialect profile to upstream datasets, hidden
semantic dependencies, validation evidence, materialization posture, mutation
posture, predicate guard, correction policy, rollback target, and deterministic
identity.

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Prevent undocumented shadow truth. | Stable view identity, purpose, definition digest, dialect profile, and upstream refs. | No raw SQL, database endpoint, catalog inspection, or registry activation. |
| Expose hidden joins, filters, and caveats. | Separate opaque join, filter, aggregate, deduplication, and window-disclosure refs. | No reference resolution or analytical recomputation. |
| Record validation status. | Finite validation state with report and fixture-receipt refs. | No report authentication, policy decision, or release gate. |
| Guard writes through filtered views. | Internal governed-updatable posture requires the declared filter predicate and local, cascaded, or equivalent guard. | No DML execution or claim that a database enforces the guard. |
| Preserve correction and rollback. | Explicit correction-policy and rollback-target refs. | No database rollback, data correction, or release withdrawal. |

## Directory Rules basis

The artifact has one authority owner: semantic meaning for a derived analytical
data contract surface. It therefore uses `contracts/data/` and the paired data
schema/fixture/validator lanes. The existing UI view registry continues to own
route-to-delivery resolution, while governance records continue to own review
and decision meaning. No parallel authority root is created.

## Deferred questions

- Which SQL dialect profiles and view-definition digests are acceptable for an adopted registry?
- Whether any public-facing KFM view may ever be write-through remains a separate policy decision; v1 denies it.
- Database catalog discovery, refresh orchestration, runtime query routing, and real `WITH CHECK OPTION` verification require separate reviewed components.

## Rollback

Rollback is a focused revert of the additive packet. No database object must be
dropped, no refresh job stopped, no data corrected, and no public artifact
withdrawn because the manifest is inactive and has no consumer.
