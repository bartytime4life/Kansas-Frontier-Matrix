<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-flora-taxon-crosswalk
title: Flora Taxon Crosswalk Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Taxonomy steward · Crosswalk steward · Contract steward · Source steward · Schema steward · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; taxonomy; taxon-crosswalk; source-role-aware; evidence-bound; correction-aware; no-taxonomic-sovereignty
tags: [kfm, contracts, flora, flora-taxon-crosswalk, taxonomy, plant-taxon, crosswalk, synonymy, accepted-name, source-role, evidence, provenance, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./rare_plant_record.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json
  - ../../../fixtures/domains/flora/flora_taxon_crosswalk/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora taxon-crosswalk semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "FloraTaxonCrosswalk links source taxon concepts, names, IDs, and statuses across taxonomic systems; it does not make KFM a taxonomic authority."
  - "Crosswalk decisions can affect occurrence claims, rare-plant exposure, invasive status, public labels, and correction lineage; unresolved taxon conflicts should cause abstain/review, not silent normalization."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Taxon Crosswalk

> Semantic contract for `FloraTaxonCrosswalk`: the Flora lane's evidence-bound mapping between source taxon identifiers, source names, accepted names, synonyms, state lists, conservation statuses, and KFM `PlantTaxon` identities.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: crosswalk not taxonomic authority" src="https://img.shields.io/badge/boundary-crosswalk__not__authority-critical">
</p>

`contracts/domains/flora/flora_taxon_crosswalk.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Crosswalk relationship types](#crosswalk-relationship-types) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/flora_taxon_crosswalk.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `FloraTaxon Crosswalk` as the crosswalk between PLANTS, GBIF backbone, NatureServe, and state lists. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `FloraTaxonCrosswalk` records mapping posture and decision support. It does **not** make KFM the taxonomic authority, does **not** erase source-native names, does **not** silently convert source concepts into accepted names, and does **not** approve occurrence, rare-plant, invasive, range, or public-layer release decisions by itself.

---

## Meaning

`FloraTaxonCrosswalk` is the Flora semantic object for mapping a **source taxon concept, source taxon identifier, source scientific name, vernacular name, synonym, conservation-list name, invasive-list name, specimen determination, occurrence label, or vegetation-community taxon reference** to a KFM `PlantTaxon` identity or reviewed taxon-candidate state.

It answers:

- Which source taxon string or ID was received?
- Which external or internal taxonomy/list did it come from?
- Which KFM `PlantTaxon` identity, candidate, or conflict cluster does it map to?
- Is the relationship exact, synonymic, broader, narrower, ambiguous, provisional, deprecated, or rejected?
- Which evidence, source role, source date, accepted-name date, review state, and correction lineage support the mapping?
- What downstream claims are allowed or blocked by this crosswalk decision?

A crosswalk can support normalization and search, but it is not source truth and is not a replacement for source citation, expert review, or correction history.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Crosswalk meaning | `contracts/domains/flora/flora_taxon_crosswalk.md` | Owned here |
| Canonical taxon identity | `contracts/domains/flora/plant_taxon.md` | Crosswalk target or candidate identity |
| Machine schema shape | `schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json` | Linked only; currently scaffolded |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, cadence, terms, and authority limits |
| Observation/occurrence users | `domain_observation.md`, `flora_occurrence.md`, `specimen_record.md` | Downstream consumers of taxon mappings |
| Sensitive Flora users | `rare_plant_record.md`, `invasive_plant_record.md`, `range_polygon.md` | Require careful status and sensitivity handling |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Exposure/admissibility decisions when mappings affect release |
| Fixtures/tests | `fixtures/domains/flora/flora_taxon_crosswalk/`, `tests/domains/flora/` | Expected proof surfaces before promotion |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only; not owned by this contract |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json` |
| Schema title | `Flora Taxon Crosswalk` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/flora_taxon_crosswalk.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, policy checks, taxon-review workflows, source registry links, public labels, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `FloraTaxonCrosswalk` should semantically assert:

1. **Crosswalk identity** — a deterministic identity for the mapping decision, not just a text match.
2. **Source taxon state** — the source system, source taxon ID, source name, rank, authorship, status, and source timestamp where available.
3. **Target taxon state** — the KFM `PlantTaxon` identity, candidate, unresolved cluster, or rejected target.
4. **Relationship type** — exact match, accepted-name mapping, synonym, homotypic synonym, heterotypic synonym, broader/narrower concept, vernacular match, list-status link, ambiguous match, provisional match, or rejected match.
5. **Evidence support** — EvidenceRef/EvidenceBundle links for consequential mappings.
6. **Source-role posture** — whether the source is observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic, and what that role allows.
7. **Review state** — whether the mapping is automatic, curator-reviewed, steward-reviewed, source-confirmed, deprecated, superseded, or blocked.
8. **Downstream impact** — which occurrence, specimen, rare-plant, invasive, range, habitat, phenology, vegetation-community, or public-label claims may rely on the mapping.
9. **Correction posture** — whether the mapping has correction notices, supersession, source withdrawal, taxonomy update, or rollback dependencies.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a string match as accepted taxonomy | Text similarity is not taxonomic authority and must not create authoritative identity by itself. |
| Replacing source-native names | Original source names and IDs must remain auditable for provenance and correction. |
| Upgrading candidate mappings into reviewed mappings | Automatic or unresolved matches must remain candidate/provisional until reviewed. |
| Collapsing different taxon concepts | Name equivalence does not always imply concept equivalence; ambiguous concepts require review. |
| Publishing sensitive status from a mapping alone | Rare/protected status can affect exposure and must route through policy and sensitivity review. |
| Treating crosswalk success as occurrence proof | Crosswalks normalize identity; they do not prove that a plant occurred. |
| Treating one source as globally controlling | Crosswalks record source relationships and authority limits; KFM does not silently override all sources. |
| Ignoring taxonomy drift | Taxonomic backbones, state lists, and conservation statuses change; stale mappings require correction handling. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical crosswalk identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and role reference. |
| `source_role` | Canonical source role: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. |
| `source_taxon_id` | Source-native taxon identifier, if available. |
| `source_taxon_name` | Source-native scientific name or taxon label. |
| `source_taxon_rank` | Source-native rank. |
| `source_taxon_authority` | Authorship or authority string, when present. |
| `source_taxon_status` | Source-native status such as accepted, synonym, unresolved, doubtful, listed, invasive, rare, or deprecated. |
| `source_taxonomy_version` | Source taxonomy/backbone/list version or date. |
| `target_plant_taxon_ref` | KFM `PlantTaxon` target, candidate, or unresolved cluster. |
| `target_taxon_name` | Normalized target name used by KFM when review allows it. |
| `relationship_type` | Crosswalk relationship category. |
| `relationship_confidence` | Confidence score or categorical confidence, when supported. |
| `relationship_basis` | Evidence basis: exact ID, canonical source, synonym table, expert review, source crosswalk, string match, manual decision, or legacy import. |
| `review_state` | `automatic`, `candidate`, `reviewed`, `steward_reviewed`, `source_confirmed`, `deprecated`, `superseded`, `rejected`, or `blocked`. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links supporting the mapping. |
| `taxonomic_notes` | Restricted/internal notes about concept boundaries or unresolved conflicts. |
| `public_label` | Public-safe label approved for UI or map display, when available. |
| `sensitivity_flags` | Flags if the mapping implies rare/protected, invasive, culturally sensitive, or source-restricted handling. |
| `policy_decision_ref` | Policy result when mapping affects exposure or release. |
| `validation_report_ref` | Validation report for the crosswalk or source batch. |
| `effective_time` | Time the mapping is valid for KFM use. |
| `retrieval_time` | Time KFM retrieved the source mapping. |
| `supersedes_ref` | Older mapping replaced by this mapping. |
| `correction_refs` | CorrectionNotice, supersession, source withdrawal, stale-state, and rollback lineage. |

---

## Crosswalk relationship types

| Relationship | Meaning | Default posture |
|---|---|---|
| `exact_identifier_match` | Source ID maps directly to a reviewed target ID. | Strongest machine support, still needs source/version evidence. |
| `accepted_name_match` | Source accepted name maps to KFM accepted name. | Review recommended when downstream claim is consequential. |
| `synonym_match` | Source synonym maps to an accepted target. | Preserve source name and synonym basis. |
| `homotypic_synonym` | Same type basis under different name. | Review/source evidence required. |
| `heterotypic_synonym` | Different type basis treated as synonym by a source. | Higher review risk; do not silently collapse conflicts. |
| `broader_concept` | Source concept is broader than target. | ABSTAIN or review for occurrence-level claims. |
| `narrower_concept` | Source concept is narrower than target. | Review required before aggregation or public labels. |
| `vernacular_match` | Common name or local label mapped to taxon. | Candidate only unless reviewed. |
| `list_status_link` | Source list/status entry links to taxon. | Supports status context, not occurrence proof. |
| `ambiguous_match` | Multiple plausible targets or unresolved concept. | Blocks promotion for consequential claims. |
| `provisional_match` | Temporary mapping awaiting review. | Candidate state; no public authoritative label. |
| `rejected_match` | Candidate mapping was reviewed and denied. | Must remain in correction/audit lineage. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Crosswalk posture |
|---|---|---|
| Taxonomic backbone, curated plant database, herbarium determination table | `administrative` or `observed` depending on source family | Can support mapping when source authority and version are recorded. |
| Conservation status list, rare-plant list, regulatory list | `regulatory` | Supports status/list posture; not occurrence proof. |
| Species distribution model or habitat model label | `modeled` | Taxon label must remain model-associated; not observed fact. |
| Atlas, portal summary, aggregate checklist | `aggregate` | Supports aggregate/list context only. |
| Watcher/imported unresolved source row | `candidate` | Hold in WORK/QUARANTINE until reviewed. |
| AI-generated or reconstructed taxon label | `synthetic` | Requires reality-boundary disclosure; never authoritative taxonomy. |

Source role is part of the mapping's meaning. A mapping may be promoted to reviewed status, but promotion must not erase the source's original authority limits.

---

## Sensitivity and release

Taxon crosswalks can look harmless while still affecting sensitive outputs. A name mapping may change whether a record is treated as rare, protected, invasive, culturally sensitive, public-safe, or restricted.

Rules:

- Crosswalks that affect rare/protected taxon status must be reviewed before public release.
- A public label must not expose a restricted source, private steward note, or sensitive plant-knowledge context.
- Candidate, synthetic, ambiguous, rights-unknown, and evidence-incomplete mappings must not be used for authoritative public claims.
- Crosswalk decisions used by `RarePlantRecord`, `OccurrenceRestricted`, `OccurrencePublic`, or `RedactionReceipt` must be traceable and rollback-ready.
- Public maps and AI answers must preserve uncertainty when a mapping is provisional, broader/narrower, ambiguous, or stale.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native names, IDs, determinations, statuses, and list entries are retained without silent rewriting. |
| WORK / QUARANTINE | Candidate mappings are normalized, compared, evidence-linked, source-role checked, and reviewed. Ambiguous or sensitive mappings remain quarantined. |
| PROCESSED | Reviewed mappings receive deterministic identity, source/version support, evidence links, relationship type, review state, and correction posture. |
| CATALOG / TRIPLET | Taxon-linked claims may be cataloged or projected only with mapping evidence, source role, time, and caveats preserved. |
| PUBLISHED | Only public-safe labels and released derivatives appear in public API/UI/map layers, with sensitive statuses and caveats handled by policy. |
| CORRECTION | Taxonomy update, source withdrawal, synonym change, list-status change, or reviewer correction requires supersession, revalidation, and downstream impact review. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/flora_taxon_crosswalk.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for exact identifier match, accepted-name match, synonym match, list-status link, reviewed ambiguous resolution, and rejected mapping.
- [ ] Add invalid fixtures for missing source descriptor, missing source taxon label/ID, unreviewed candidate used as public label, ambiguous mapping used for occurrence proof, synthetic label treated as authoritative, missing evidence for consequential mapping, stale taxonomy without correction posture, and rare/protected status change without sensitivity review.
- [ ] Add validator checks for deterministic identity, source role, relationship type, source taxonomy version, target `PlantTaxon` ref, evidence refs, review state, sensitivity flags, correction refs, and public-label safety.
- [ ] Add tests proving crosswalk success does not equal occurrence proof or publication authority.
- [ ] Add no-network fixtures so CI can validate the contract without live taxonomy/source access.
- [ ] Add revalidation tests for taxonomy backbone update, source-list update, synonym change, and source withdrawal.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Mapping resolves, evidence is sufficient, review state allows use | `ANSWER` / mapping usable within stated scope |
| Evidence missing, mapping ambiguous, source version stale, review incomplete | `ABSTAIN` |
| Sensitive/public exposure forbidden, rights denied, candidate/synthetic mapping misused | `DENY` |
| Schema/validator/runtime/source-read failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Flora canonical path register | Confirms `FloraTaxon Crosswalk` is a Flora object-family contract and describes its intended crosswalk role across PLANTS, GBIF backbone, NatureServe, and state lists. |
| Flora object-family register | Confirms `FloraTaxon Crosswalk` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms EvidenceBundle, source role, policy, review state, release state, correction, and rollback must outrank generated labels or summaries. |

---

## Rollback

Taxon crosswalk rollback is required when a mapping changes a public label, occurrence meaning, rare/protected status, invasive status, range claim, habitat association, catalog claim, AI answer, or released map layer.

Rollback triggers include:

- taxonomic backbone update;
- synonym or accepted-name correction;
- state-list or conservation-status update;
- source withdrawal or rights change;
- mistaken broader/narrower concept collapse;
- ambiguous mapping promoted without review;
- candidate or synthetic mapping used as authoritative;
- rare/protected status misclassification;
- public label exposes sensitive source context;
- downstream occurrence, specimen, range, invasive, or rare-plant record depends on a superseded mapping.

Rollback artifacts should include affected crosswalk IDs, target `PlantTaxon` IDs, source records, downstream occurrence/specimen/range/rare-plant records, release IDs, catalog IDs, evidence refs, policy decisions, correction notices, rollback cards, and replacement mapping reports.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which source is the default KFM backbone when multiple accepted-name systems conflict? | PROPOSED / NEEDS VERIFICATION | Confirm with Flora steward and taxonomy steward before schema expansion. |
| Should `relationship_type` use a local enum or align to an external taxonomic concept vocabulary? | NEEDS VERIFICATION | Resolve in schema/ADR review. |
| How should state-list statuses interact with accepted taxonomy when names differ? | NEEDS VERIFICATION | Define fixtures for rare/protected and invasive examples. |
| Which mappings require steward review versus automated validation only? | NEEDS VERIFICATION | Policy + validation steward decision. |
| How should source-version drift trigger downstream revalidation? | NEEDS VERIFICATION | Define revalidation runbook and rollback references. |
| Should public labels always come from `PlantTaxon`, or can a released crosswalk override display labels? | NEEDS VERIFICATION | Decide with UI/API steward and release steward. |

---

## Related contracts

- `plant_taxon.md` — target taxon identity and accepted/candidate taxon meaning.
- `domain_observation.md` — source observation envelope that may carry source taxon labels.
- `flora_occurrence.md` — occurrence-class records that depend on crosswalked taxon support.
- `specimen_record.md` — specimen/voucher determinations that may drive or revise mappings.
- `rare_plant_record.md` — sensitive/protected plant record affected by taxon status mapping.
- `invasive_plant_record.md` — invasive status records affected by list/taxon mapping.
- `range_polygon.md` — range/distribution claims that depend on taxon identity.
- `habitat_association.md` — habitat links that should not outlive superseded taxon mappings.
- `domain_validation_report.md` — validation reports for mappings, fixtures, policy checks, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any occurrence or public label depends on this contract.
- [ ] Add policy tests for rare/protected, invasive, sensitive-source, and public-label cases.
- [ ] Confirm source registry entries for each taxonomic/list source before activation.
- [ ] Confirm public API/UI surfaces do not expose candidate, ambiguous, synthetic, or sensitive mappings as authoritative.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
