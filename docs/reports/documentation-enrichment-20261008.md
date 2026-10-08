<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/documentation-enrichment-20261008
title: KFM documentation enrichment inventory and validation
type: report
version: v1.0-draft
status: draft; source-grounded; review-pending
owners: ["@bartytime4life via CODEOWNERS"]
created: 2026-10-08
updated: 2026-10-08
policy_label: repository-facing
owning_root: docs/
responsibility: Record the documentation enrichment scope, placeholder dispositions, evidence basis and validation limits.
truth_posture: CONFIRMED source inventory and document checks; PROPOSED draft guidance and independent review pending.
related:
  - docs/README.md
  - docs/encyclopedia/INDEX.md
  - tools/qa/gap_scan.py
[/KFM_META_BLOCK_V2] -->

# Documentation enrichment — 2026-10-08

## Scope and evidence

Base: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe` (merged PR #4933). The work uses an isolated documentation branch and preserves the separate dirty application checkout. Changes are Markdown only; no runtime, schema, executable policy, machine register, receipt or baseline is rewritten.

The initial inventory covered 1,821 Markdown files under `docs/`. The repository gap scanner identified 94 Markdown header markers, 138 broken local links and nine unratcheted non-Markdown placeholders. A marker is a review lead, not proof that a document is empty: four long policy boundary guides already contain substantive content and truthfully describe unfinished executable rule corpora. Those four are retained. Two substantive package namespace guides are enriched while their actual empty-library status stays visible.

## Material improvements

- Seventeen encyclopedia chapters now contain original draft reference text: reader routes, source-ledger fields, operating rules, domain/capability/feature/action tables, cross-domain limits, viewing modes, backlog, roadmap, sensitivity and validation guidance.
- Soil guides, short runbooks and intake instructions now provide useful inputs, procedures, expected outputs, rejection/recovery paths and review criteria.
- Legacy Flora contract paths route readers to existing semantic owners, preserving compatibility without inventing another contract authority; the hazards report guide explains the evidence needed for a report.
- Fixture markers become domain-specific authoring guides that name actual payloads, meaningful consumers and empty lanes. They do not create new fixture coverage.
- Source-rights and sensitivity notes become review packet guides. They make no blanket provider license or operational-enforcement claim.
- Register and domain navigation now explains evidence inventory, continuity, release records, source families and sensitivity without inventing decisions.

The encyclopedia remains a **draft reference**. ADR-0036 remains proposed, the formal lane-placement hold remains, the historical source PDF is not copied, and no generated whole-book assembly is claimed. Earlier index and boundary assessments are preserved as dated history with current reading routes placed first.

## Connected documentation

Seven existing Google Docs working records and ten existing Notion reference hubs were enriched in place. Google Docs used fresh revision guards and native date elements with post-write text readback. Notion readback confirmed all 35 original child/database references remained. Historical material and native structures were retained; current guidance is distinguished from earlier checkpoints.

Sites metadata was inspected for the existing owner-private Explorer: latest saved version 185 at the read. Saved-version metadata does not by itself prove which source is deployed or browser acceptance. The documentation update does not republish or change the application's audience.

Private document identities and contents remain in their connected workspaces rather than being copied into this repository report.

## Validation and limits

The change contains 105 Markdown documents (104 existing files plus this report), including all 87 initial marker files smaller than 2,000 bytes. It adds approximately 47,600 net words across the existing files. Larger existing guides were preserved or selectively enriched.

| Local check | Result |
|---|---|
| Changed-document links | PASS: 105 documents, 1,183 local targets |
| Metadata | PASS: 105 valid blocks, no missing blocks or failures; 153 bounded-parser/truth-label warnings |
| Scoped document graph | PASS: no failures; 127 navigation/metadata warnings |
| ADR index | PASS: 43 numbered records and 11 unassigned records; no acceptance change |
| Placeholder scan | 94 initial Markdown markers reduced to six retained implementation-status markers |
| Existing broken links | 138 inherited findings; new report enters the tracked set before final gap check |

Final staged gap/whitespace checks and exact-commit metadata/graph checks are required before the draft PR is pushed. Warnings are recorded rather than hidden; graph reachability within a changed-file-only scope is not a repository-wide orphan assessment. Checks classify external links without asserting current remote availability. Source-linked contributor test commands are documented procedures unless a specific execution result is recorded.

This is an extensive placeholder and navigation pass, not a claim that all 1,821 documents were semantically re-reviewed or that every historical source statement was refreshed. The 138 inherited broken-link findings and executable implementation gaps are separate follow-up work; this change must introduce none. The gap baseline is retained unchanged.

## Placeholder disposition inventory

All 94 initial Markdown marker findings are accounted for below. Same-path documentation authoring does not upgrade the implementation, source-admission, review or release state described by a document.

| Path in initial scan | Disposition |
|---|---|
| `contracts/domains/flora/DistributionSurface.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/FloraOccurrence.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/FloraTaxonCrosswalk.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/HabitatAssociation.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/InvasivePlantRecord.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/PhenologyObservation.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/PlantTaxon.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/RangePolygon.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/RarePlantRecord.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/RedactionReceipt.flora.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/RestorationPlanting.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/SpecimenRecord.md` | Substantive guide authored or expanded in place |
| `contracts/domains/flora/VegetationCommunity.md` | Substantive guide authored or expanded in place |
| `contracts/domains/hazards/domain_validation_report.md` | Substantive guide authored or expanded in place |
| `docs/domains/roads-rail-trade/CHANGELOG.md` | Substantive guide authored or expanded in place |
| `docs/domains/settlements-infrastructure/SENSITIVITY.md` | Substantive guide authored or expanded in place |
| `docs/domains/settlements-infrastructure/SOURCE_FAMILIES.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/CROSS_LANES.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/DEFINITION_OF_DONE.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/EXPANSION_PLAN.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/FILE_SYSTEM_PLAN.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/GLOSSARY.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/MAP_UI_CONTRACTS.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/PRESERVATION_MATRIX.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/RELEASE_INDEX.md` | Substantive guide authored or expanded in place |
| `docs/domains/soil/SOURCES.md` | Substantive guide authored or expanded in place |
| `docs/domains/spatial-foundation/README.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/01-cover.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/02-executive-summary.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/03-source-ledger.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/04-operating-law.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/05-master-domain-atlas.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/06-cross-domain-capability-taxonomy.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/07-domain-chapters.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/08-cross-domain-systems.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/09-master-feature-matrix.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/10-master-action-matrix.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/11-master-viewing-mode-atlas.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/11-settlements-infrastructure.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/12-programming-possibilities-backlog.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/13-sensitive-deny-by-default-register.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/14-implementation-roadmap.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/15-validation-and-acceptance-plan.md` | Substantive guide authored or expanded in place |
| `docs/encyclopedia/chapters/16-appendices.md` | Substantive guide authored or expanded in place |
| `docs/registers/CONTINUITY_INVENTORY.md` | Substantive guide authored or expanded in place |
| `docs/registers/RELEASE_REGISTER.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/flora_BACKBONE_ROTATION.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/flora_SOURCE_REFRESH.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/hydrology_VALIDATION.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/retention-agriculture.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/revocation.md` | Substantive guide authored or expanded in place |
| `docs/runbooks/roads_rail_trade_source_refresh.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/agriculture/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/agriculture/invalid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/agriculture/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/archaeology/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/archaeology/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/atmosphere/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/flora/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/geology/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/geology/invalid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/geology/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/habitat/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/habitat/invalid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/habitat/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/hazards/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/hazards/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/hydrology/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/people-dna-land/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/people-dna-land/invalid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/people-dna-land/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/roads-rail-trade/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/roads-rail-trade/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/settlements-infrastructure/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/settlements-infrastructure/invalid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/settlements-infrastructure/valid/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `fixtures/domains/soil/golden/PLACEHOLDER.md` | Substantive guide authored or expanded in place |
| `packages/domains/geology/src/geology/README.md` | Substantive guide enriched; package implementation remains absent |
| `packages/domains/soil/src/soil/README.md` | Substantive guide enriched; package implementation remains absent |
| `policy/domains/fauna/ebird_redistribution.md` | Substantive guide authored or expanded in place |
| `policy/domains/roads-rail-trade/README.md` | Existing substantive policy boundary retained; marker describes unfinished rule corpus |
| `policy/domains/settlements-infrastructure/README.md` | Existing substantive policy boundary retained; marker describes unfinished rule corpus |
| `policy/rights/flora/gbif_license.md` | Substantive guide authored or expanded in place |
| `policy/rights/flora/inaturalist_usage.md` | Substantive guide authored or expanded in place |
| `policy/rights/flora/knhi_access.md` | Substantive guide authored or expanded in place |
| `policy/rights/flora/natureserve_explorer_pro.md` | Substantive guide authored or expanded in place |
| `policy/sensitivity/README.md` | Existing substantive policy boundary retained; marker describes unfinished rule corpus |
| `policy/sensitivity/fauna/README.md` | Substantive guide authored or expanded in place |
| `policy/sensitivity/flora/README.md` | Substantive guide authored or expanded in place |
| `policy/sensitivity/flora/plants_join_sensitivity.md` | Substantive guide authored or expanded in place |
| `policy/sensitivity/flora/rare_plant_geoprivacy.md` | Substantive guide authored or expanded in place |
| `policy/sensitivity/infrastructure/reservation-community-boundary.md` | Substantive guide authored or expanded in place |
| `policy/sources/rights/README.md` | Existing substantive policy boundary retained; marker describes unfinished rule corpus |
