<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/preservation-matrix
title: Soil preservation and correction matrix
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
responsibility: Soil preservation and correction matrix; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/doctrine/retention.md
  - docs/runbooks/revocation.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# soil — PRESERVATION_MATRIX.md

This matrix helps reviewers identify what a Soil change must preserve. It does
not establish a retention duration, authorize deletion or implement a storage
service. Actual source rights, consent, policy and release constraints govern
custody and access.

## Preservation by artifact

| Artifact | Preserve with it | Consequence of loss |
|---|---|---|
| Source capture | Product/edition, retrieval time, extent, permitted custody and payload digest | A derived claim cannot be reconstructed or attributed |
| Map unit | Native MUKEY lineage, survey/vintage, geometry support and method | Spatial joins can refer to the wrong survey unit |
| Component | COKEY, map-unit relationship, component percentage and source version | A mixed map unit may be misrepresented as uniform soil |
| Horizon/profile | CHKEY where supplied, top/bottom depth, unit, method and component link | Vertical properties lose their support and meaning |
| Moisture observation | Station/grid identity, depth, units, observation time, QC and uncertainty | Values can be mistaken for current field observations |
| Modeled grid | Product/version, grid support, model role, cadence and limitations | A modeled derivative may appear to be a direct measurement |
| Derived suitability/context | Input identities, method/version, scale and limiting assumptions | Output cannot be reproduced or bounded to its intended use |
| Validation/evidence | Exact subject and code/schema hashes, findings and reference lineage | Passing results may be attached to changed bytes |
| Correction/withdrawal | Superseded identity, reason, dependents and effective time | Old claims can continue through cached or exported derivatives |
| Release/rollback | Manifest identity, exact artifacts, decision and verified restore target | A map may restore bytes with the wrong authority or evidence |

## Lifecycle handling

RAW remains source evidence under its custody rules. WORK and QUARANTINE retain
candidate status, reasons and dependencies. PROCESSED carries transformation and
validation lineage. CATALOG/TRIPLET references must remain resolvable. PUBLISHED
artifacts retain the evidence, decision and correction route that justified
exposure. Moving bytes does not itself advance lifecycle state.

Do not infer that a named lane contains substantive data from a README. At the
pinned snapshot, the Soil proof and release-candidate lanes establish navigation,
not completed proof or release records.

## Proposed review workflow

1. Identify the exact source/candidate/released artifact and all affected versions.
2. Inventory downstream map layers, APIs, evidence links, exports, graphs, indexes,
   caches and answers before changing a referenced object.
3. Record the desired action: retain, correct, supersede, archive, withdraw or
   seek separate erasure review. Explain the evidence and rights basis.
4. Test whether historical queries and reproduction still work after the change.
   An unresolved lost-query capability is a hold, not routine cleanup.
5. Establish an accessible rollback target or explicit empty state, then obtain
   the decisions required by the owning surface.
6. Verify dependent correction or denial after authorized execution. Keep its
   readback distinct from a successful fixture assessment.

## Retention and erasure boundary

The [retention doctrine](../../doctrine/retention.md) is a draft guidance surface
and supplies no adopted Soil duration here. The bounded
[temporal-disposition assessment](../../../contracts/governance/temporal_retention_disposition_assessment.md)
can check declared retention, archive or compaction controls; it cannot delete
history or approve erasure. Privacy obligations may restrict what is retained and
where. Resolve them with accountable reviewers instead of putting sensitive
payloads into a public audit record.

## Failure handling and acceptance

Missing source vintage, native-key linkage, a detached receipt or an unresolved
rollback target blocks the corresponding claim. Preserve the candidate and gap
record, route it to the source/evidence/release steward role, and use
[revocation routing](../../runbooks/revocation.md) when a permission or consent
change is involved. Completion means both retained evidence and affected
consumer state have been checked at the claimed scope.
