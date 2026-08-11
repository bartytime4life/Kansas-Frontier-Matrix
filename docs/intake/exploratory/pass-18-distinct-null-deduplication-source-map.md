<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-distinct-null-deduplication
title: Pass 18 DISTINCT and NULL Deduplication Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Analytics steward · Common contract steward · Identity steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; analytics; distinct; null; deduplication
responsibility: Preserve source and repository lineage for bounded DISTINCT/NULL semantics without turning tuple declarations into query, identity, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive metadata, and inspected-repository comparison; PROPOSED bounded adaptation; UNKNOWN cross-engine parity; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/distinct_null_deduplication_assessment.md
  - ../../../contracts/common/aggregate_null_semantics_disclosure.md
  - ../../../contracts/common/reversible_entity_reconciliation.md
  - ../../../contracts/evidence/count_population_disclosure.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 DISTINCT and NULL Deduplication Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 234-235 / printed pages 231-232 | Card `KFM-P18-INV-155` proposes documenting DISTINCT-like NULL handling and multi-column uniqueness before counts or entity matches are promoted. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| `contracts/evidence/count_population_disclosure.md` | The existing count profile discloses distinct value-tuple population but explicitly does not perform identity reconciliation or deduplication. | `CONFIRMED` adjacent, non-duplicate family |
| `contracts/common/aggregate_null_semantics_disclosure.md` | The existing aggregate profile declares aggregate input, grouping-key, and empty-input NULL behavior; it does not assess DISTINCT tuple deduplication or identity use. | `CONFIRMED` adjacent, non-duplicate family |
| `contracts/common/reversible_entity_reconciliation.md` | The existing reconciliation profile preserves source assertions and requires explicit reversible match decisions. It supplies the safe identity boundary that SQL DISTINCT must not replace. | `CONFIRMED` adjacent authority boundary |
| Starting `main@12911a862033546160737479681bed0ac68d1f7b` plus GitHub PR/code searches | No exact card ID, DISTINCT/NULL deduplication assessment, schema, fixture family, validator, workflow, branch, or PR was found before implementation. Search matches were adjacent count and aggregate-NULL work only. | `CONFIRMED` inspected snapshot |

The source artifact is design evidence, not repository instruction authority.
Placement and scope follow accepted Directory Rules and current responsibility
roots.

## Selected increment

The implementation is a small, additive `contracts/common/` disclosure value
object. It binds an opaque operation and dialect profile to canonical tuple
fields, explicit NULL semantics, a synthetic fixture summary, adjacent contract
references, disclosure, and a deterministic profile hash.

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Document NULL behavior. | Declare row inclusion and NULL equivalence separately. | No row inspection, SQL execution, or engine-parity claim. |
| Document multi-column uniqueness. | Canonical ordered field tuples distinguish one-field and multi-field operations. | No source-native identity values or composite-key registry. |
| Add null, duplicate, and multi-column fixtures. | Digest-bound synthetic coverage flags plus expected/observed distinct counts. | No embedded source rows or receipt authentication. |
| Protect counts and entity matches. | Count use references the existing population disclosure; entity-match use requires deterministic reconciliation. | SQL DISTINCT and GROUP BY cannot authorize identity matching or merging. |

## Directory Rules basis

The artifact has one authority owner: reusable cross-domain DISTINCT/NULL tuple
semantics. It therefore uses the existing common-contract responsibility root,
with shape, fixtures, validator, tests, workflow, source map, and generated
receipt in their established roots. No parallel analytics, identity, evidence,
policy, release, or publication authority is created.

## Deferred questions

- Which engine profiles have reviewed parity fixtures for NULL-bearing tuples?
- Whether adopted count receipts embed this assessment or reference it remains undecided.
- Production reconciliation thresholds and source-specific identity rules remain domain- and steward-owned.

## Rollback

Rollback is a focused revert of the additive packet. No query rerun, entity
split, data correction, release withdrawal, cache invalidation, or public
cleanup is required because the profile is inactive and has no consumer.
