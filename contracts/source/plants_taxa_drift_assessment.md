<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/plants-taxa-drift-assessment
title: PlantsTaxaDriftAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Flora source steward · Taxonomy steward · Sensitivity steward · Contract steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; source; flora; plants; taxa-drift; sensitivity; non-publisher
responsibility: Define a fixture-only assessment of synthetic PLANTS taxa-set drift under a stable taxonomy version without contacting sources, joining occurrences, exposing locations, deciding taxonomy or conservation status, admitting a source, changing lifecycle state, or granting publication authority.
truth_posture: "CONFIRMED supplied Pass 20 source, connected Drive source material, existing Flora registry and watcher boundaries, adjacent source/taxonomy contracts, and bounded repository gap; PROPOSED inactive assessment; UNKNOWN executable watcher home, live source activation, current PLANTS interface, and steward ownership; NEEDS VERIFICATION flora, taxonomy, sensitivity, source, contract, and validation review plus hosted exact-head CI"
related:
  - ./source_descriptor.md
  - ./source_intake_record.md
  - ./watcher_registry.md
  - ../crosswalks/taxonomy/taxonomic_concept_lineage.md
  - ../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../tools/ingest/plants_watch/README.md
  - ../../tools/watchers/plants_watch/README.md
  - ../../schemas/contracts/v1/source/plants_taxa_drift_assessment.schema.json
  - ../../fixtures/contracts/v1/source/plants_taxa_drift_assessment/cases.json
  - ../../tools/validators/source/validate_plants_taxa_drift_assessment.py
  - ../../tests/validators/test_validate_plants_taxa_drift_assessment.py
  - ../../docs/intake/exploratory/pass-20-plants-taxa-drift-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# PlantsTaxaDriftAssessment Candidate

`PlantsTaxaDriftAssessmentCandidate` is an additive, fixture-only comparison of
two synthetic PLANTS taxa inventories. It implements the bounded fixture proof
requested by Pass 20 `KFM-IDX-ANA-004`, `KFM-IDX-SRC-006`, and `EXP-001`:
changed and unchanged cases, stable taxonomy binding, sensitive and
non-sensitive cases, missing-attestation denial, and a non-publisher output.

This packet intentionally does not create an executable watcher. The repository
currently documents multiple proposed watcher and specification homes and marks
their authority unresolved. The assessment can be reviewed without pre-empting
that placement decision or activating a live source.

## Assessment declaration

| Concern | Required declaration | Local check |
|---|---|---|
| Source bindings | Opaque refs to a SourceDescriptor, SourceIntakeRecord candidate, watcher registry, and TaxonomicConceptLineage packet. | Refs are structural only and are never dereferenced. |
| Snapshot pair | Distinct, time-ordered prior/current refs and content digests. | Current must be newer; the assessment cannot predate current. |
| Taxonomy version | The same taxonomy-version ref for both snapshots plus an attestation ref. | Version drift abstains rather than being misclassified as taxa drift. |
| Set delta | Canonical additions, removals, and optional rename/recode candidates. | Add/remove sets are disjoint; rename sources are removed and targets are added. |
| Materiality | `CHANGE_CANDIDATE`, `NO_MATERIAL_CHANGE`, or `UNRESOLVED`. | A change needs a delta and emits `WORK_CANDIDATE`; unchanged emits no work record; unresolved abstains. |
| Sensitivity | No occurrence join, no exact locations, conservation-list intersection state, counts-only/withheld mode, policy ref when needed, and review requirement. | Occurrence joins or exact locations are denied. Present sensitive intersections are withheld and policy-bound; unknown intersections abstain while withheld. |
| Attestation and review | At least two snapshot attestations, one taxonomy-version attestation, and canonical review refs. | Missing attestations or complete review without records is denied. |

The fixture contains only invented `kfm://.../synthetic` identities. It contains
no county FIPS, scientific or common name, PLANTS symbol, occurrence record,
coordinate, geometry, conservation-list member, or live endpoint.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic bindings, snapshots, taxonomy version, set delta, materiality, sensitivity, attestations, non-public output, review, timestamp, and content identity are locally coherent. |
| `ABSTAIN` | Taxonomy version, materiality, conservation intersection, or review remains unresolved. |
| `DENY` | Snapshot, delta, rename, sensitivity, attestation, output, review, time, or content-identity declarations contradict the profile. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

`PASS` does not mean a taxon was added or removed in PLANTS, a conservation
intersection is correct, or a work candidate is admitted. The sensitive fixture
passes only because its detail remains withheld and its synthetic policy and
review refs are structurally present.

## Authority boundary

A validator result does not:

- contact USDA PLANTS, GBIF, iNaturalist, a heritage program, or any endpoint;
- perform a county, occurrence, specimen, conservation-list, or location join;
- identify, accept, rename, split, merge, or remove a taxon concept;
- decide legal, conservation, rare, protected, or cultural sensitivity status;
- resolve a SourceDescriptor, SourceIntakeRecord, watcher registry, lineage
  packet, attestation, policy decision, review record, or work-candidate ref;
- admit a source, write RAW/WORK/QUARANTINE data, promote lifecycle state, or
  authorize release, publication, map rendering, API/UI/AI use, or public use.

## Directory Rules basis

Source-drift assessment meaning belongs under `contracts/source/`. Machine
shape, synthetic replay, executable validation, conformance evidence, read-only
CI, source lineage, and authoring provenance stay in their existing
responsibility roots. No file is added under either proposed watcher executable
home, neither duplicate pipeline specification is selected, and no data,
registry, policy, release, application, or public path is created.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_plants_taxa_drift_assessment -v
python tools/validators/source/validate_plants_taxa_drift_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive candidate creates no live
source, taxonomic, conservation, occurrence, sensitivity, lifecycle, review,
release, deployment, publication, or public state that requires restoration.
