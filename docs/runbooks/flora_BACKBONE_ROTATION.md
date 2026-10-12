<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/flora-backbone-rotation
title: Flora taxonomic backbone rotation review
type: runbook
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and taxonomy stewards
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Flora taxonomic backbone rotation review; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/flora/VERIFICATION_BACKLOG.md
  - contracts/domains/flora/flora_taxon_crosswalk.md
  - schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Flora BACKBONE ROTATION

Use this procedure when a taxonomy/backbone or list version changes accepted
names, synonyms, concepts, ranks or identifiers used by Flora candidates. A
backbone rotation is a versioned mapping review, not a bulk rename.

## Implementation boundary

The [FloraTaxonCrosswalk contract](../../contracts/domains/flora/flora_taxon_crosswalk.md)
explains source/target identity, relationship types, evidence and correction.
Its [paired schema](../../schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json)
still has empty properties and `additionalProperties: true` at the evidence
snapshot. The [taxonomy policy](../../policy/domains/flora/flora_taxonomy_resolution.rego)
is a proposed scaffold with `default allow := false`.

No accepted executable rotation or rollback command is established here. Schema
parsing alone cannot prove concept mappings. This runbook prepares a reviewable
comparison and identifies what implementation must be supplied before execution.

## Required inputs

- old and proposed taxonomy provider, exact version/date and permitted snapshot;
- source-native taxon IDs, names, rank and source status;
- proposed target concept and relationship, with evidence and uncertainty;
- current consumers: occurrence/specimen records, range or habitat context,
  conservation/invasive lists, search labels and public projections;
- rights, sensitivity and reviewer routing, including taxonomic expertise;
- immutable baseline and a proposed correction/rollback boundary.

Keep source values alongside target values. Do not include protected occurrence
coordinates or private steward notes in a public comparison packet.

## Comparison and review

1. Inventory every consumer of the old mapping and its version binding.
2. Produce a side-by-side mapping table with unchanged, changed and unresolved
   rows. Preserve the old concept/ID even when the accepted display name changes.
3. Classify exact identifiers, synonyms, broader/narrower concepts, ambiguous,
   provisional and rejected matches. String similarity is candidate evidence.
4. Review splits and merges explicitly. Do not distribute old occurrence counts
   across new concepts without a supported method.
5. Re-evaluate sensitivity and regulatory/list implications. A new name can
   alter rare/protected status handling without changing a coordinate.
6. Hold ambiguous or unreviewed consequential mappings. A taxonomy source is not
   evidence of a new occurrence, legal status or botanical identification.
7. Require dependency-closed contract/schema/fixture/validator work before any
   automated migration. Include reverse lookup and correction propagation.
8. Route accepted mapping decisions and proposed release effects separately.

## Suggested comparison record

| Field | Required content |
|---|---|
| Source binding | Native ID, name, rank, provider and old version |
| Candidate binding | Target ID/name and proposed version |
| Relationship | Explicit category and evidence basis |
| Consequence | Consumers, counts, labels and sensitivity affected |
| Disposition | Reviewed mapping, unresolved conflict or rejected candidate |
| Lineage | Prior mapping, reviewer evidence and correction target |

This is an authoring aid, not the permissive schema's enforced field list.

## Available checks and missing proof

```bash
python -m unittest discover --start-directory tests/domains/flora --pattern 'test_flora_smoke.py' --verbose
python tools/validators/domains/flora/validate_schema.py
```

The smoke profile exercises role/taxonomy-collapse rejection on synthetic data.
The schema entry point checks its declared scope. Neither performs this rotation
or proves every mapping. Before implementation, add exact negative fixtures for
ambiguous matches, split/merge loss, missing source version, sensitivity changes
and rollback incompatibility; then bind them to the chosen schema and evaluator.

## Rollback and acceptance

Retain old mapping versions and a consumer impact inventory so an authorized
rollback can restore the exact prior mapping and invalidate derivatives. Restoring
a label alone is insufficient if evidence, search or exported aggregates changed.
A complete review packet records unresolved mappings and tested migration scope;
it does not claim that production taxonomy or public products have been rotated.
