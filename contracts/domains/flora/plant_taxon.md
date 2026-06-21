<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-plant-taxon
title: Plant Taxon Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Taxonomy steward · Contract steward · Source steward · Schema steward · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; plant-taxon; botanical-identity; taxonomy; source-role-aware; evidence-bound; no-taxonomic-sovereignty
tags: [kfm, contracts, flora, plant-taxon, taxonomy, botanical-identity, accepted-name, synonym, rank, crosswalk, evidence, source-role, provenance, correction, rollback]
related:
  - ./README.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
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
  - ../../../schemas/contracts/v1/domains/flora/plant_taxon.schema.json
  - ../../../fixtures/domains/flora/plant_taxon/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora plant-taxonomy semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "PlantTaxon is the Flora lane's canonical botanical identity object; USDA PLANTS is recorded in the canonical path register as a recommended taxonomic backbone, but that backbone choice remains PROPOSED."
  - "PlantTaxon normalizes identity for KFM use but does not make KFM a taxonomic authority, erase source-native names, or approve occurrence, rare-plant, invasive, range, habitat, or public-release claims by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Plant Taxon — Flora

> Semantic contract for Flora `PlantTaxon`: the evidence-bound botanical identity object used to anchor plant names, accepted/candidate taxonomy, source taxon labels, synonyms, rank, status, provenance, crosswalks, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: identity not taxonomic authority" src="https://img.shields.io/badge/boundary-identity__not__taxonomic__authority-critical">
</p>

`contracts/domains/flora/plant_taxon.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Taxon states](#taxon-states) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/plant_taxon.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/plant_taxon.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `PlantTaxon` as canonical botanical identity with USDA PLANTS as a recommended taxonomic backbone in PROPOSED status. Field-level schema shape, fixtures, validators, source registry terms, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `PlantTaxon` is KFM's Flora identity object, not a taxonomic authority. It must preserve source-native names and authority limits, route external mappings through `FloraTaxonCrosswalk`, and avoid silently upgrading candidate, synonym, unresolved, deprecated, source-conflicted, or synthetic labels into accepted botanical truth.

---

## Meaning

`PlantTaxon` is the Flora semantic object for a plant taxon identity used inside KFM. It provides a governed identity anchor for names, ranks, accepted/candidate status, synonymy, source identifiers, provenance, source-role posture, and correction lineage.

It answers:

- Which plant taxon identity is KFM referring to?
- What accepted, candidate, source-native, synonym, vernacular, or deprecated names are associated with that identity?
- Which taxonomic backbone, source registry entry, crosswalk, review record, and evidence support the identity?
- What rank, authorship, taxonomic status, conservation/invasive/list status, and source-version context are safe to use?
- Which downstream Flora records may rely on this identity, and what caveats must follow it?
- What correction, supersession, rollback, or revalidation is required if taxonomy changes?

A plant taxon identity can support normalized search, joins, public labels, occurrence grouping, range layers, habitat association, phenology, invasive plant context, rare-plant handling, and restoration workflows. It does not prove occurrence, sensitivity, range, habitat, public release, or management recommendation by itself.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Taxon identity meaning | `contracts/domains/flora/plant_taxon.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/plant_taxon.schema.json` | Linked only; currently scaffolded |
| Crosswalk support | `contracts/domains/flora/flora_taxon_crosswalk.md` | Maps source IDs/names/backbones/lists to this identity |
| Observation support | `domain_observation.md`, `flora_occurrence.md` | Downstream records reference taxon identity; not replaced |
| Voucher support | `specimen_record.md` | Can strengthen or correct determination and identity support |
| Sensitive Flora support | `rare_plant_record.md`, `occurrence_restricted.md`, `occurrence_public.md` | Taxon identity can affect sensitivity and release posture |
| Time/community/context users | `phenology_observation.md`, `vegetation_community.md`, `range_polygon.md`, `habitat_association.md` | Downstream consumers that must preserve taxon caveats |
| Invasive/restoration users | `invasive_plant_record.md`, `restoration_planting.md` | Use identity/status with source-role caveats |
| Source registry | `data/registry/sources/flora/` | Source identity, authority limits, cadence, rights, attribution |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Release and sensitive-context decisions when identity affects exposure |
| Published layers | `data/published/layers/flora/`, `release/` | Public-safe derivatives only after review/release |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/plant_taxon.schema.json` |
| Schema title | `Plant Taxon` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/plant_taxon.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, crosswalk rules, source registry links, public labels, policy checks, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `PlantTaxon` should semantically assert:

1. **Taxon identity** — a deterministic KFM identity for a plant taxon or taxon candidate.
2. **Name support** — accepted/candidate/source-native name, authorship, rank, vernacular labels, synonym state, and deprecated names where material.
3. **Backbone support** — taxonomic backbone/source, version/date, source descriptor, and authority limits.
4. **Crosswalk support** — mapping records connecting source taxon IDs, external identifiers, state lists, conservation lists, invasive lists, and KFM identity.
5. **Review state** — automatic, candidate, curator-reviewed, steward-reviewed, source-confirmed, deprecated, superseded, rejected, or blocked posture.
6. **Evidence support** — EvidenceRef/EvidenceBundle links for consequential identity claims.
7. **Source-role posture** — whether the identity support comes from administrative, observed, regulatory, aggregate, modeled, candidate, or synthetic context.
8. **Downstream caveats** — any limitations that must follow occurrence, range, habitat, phenology, invasive, rare-plant, public-label, or AI-answer use.
9. **Sensitivity relevance** — flags when identity implies rare/protected, invasive, culturally sensitive, source-restricted, or other policy-significant handling.
10. **Correction posture** — taxonomic updates, synonym changes, source withdrawals, supersession, merge/split events, and rollback lineage.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating KFM identity as global taxonomic authority | KFM normalizes for project use; external authority and source limits remain explicit. |
| Treating a text match as identity proof | String similarity is not sufficient for accepted taxonomy. |
| Erasing source-native names | Original source names/IDs must remain auditable for provenance and correction. |
| Collapsing conflicting taxon concepts | Broader/narrower or ambiguous concepts require review and caveats. |
| Treating taxon identity as occurrence proof | Identity says what taxon is referenced; it does not prove presence. |
| Treating taxon identity as public-release approval | Rare/protected, private, rights, evidence, policy, review, and release gates remain separate. |
| Treating regulatory/invasive/conservation status as accepted taxonomy | List status and taxonomic identity are different claim types. |
| Publishing sensitive labels without review | A public label can expose rare/protected or culturally sensitive context. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM plant taxon identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `taxon_key` | Stable normalized key or slug, if adopted. |
| `accepted_name` | KFM accepted display name, when review supports one. |
| `accepted_name_authority` | Authorship/authority string for accepted name. |
| `rank` | Taxonomic rank. |
| `taxonomic_status` | Accepted, synonym, candidate, unresolved, deprecated, superseded, rejected, or blocked. |
| `source_taxon_name` | Source-native name retained for audit. |
| `source_taxon_id` | Source-native identifier. |
| `backbone_source_ref` | SourceDescriptor for selected backbone or source family. |
| `backbone_version` | Backbone/list version or effective date. |
| `source_role` | Canonical source role supporting the identity posture. |
| `flora_taxon_crosswalk_refs` | Crosswalk records linking external IDs/names/statuses. |
| `synonym_refs` | Synonym records or crosswalk refs. |
| `vernacular_names` | Public-safe vernacular labels, with source/caveat if needed. |
| `conservation_status_refs` | Rare/protected/list status references, not collapsed into identity. |
| `invasive_status_refs` | Invasive/noxious/watch-list references, not collapsed into identity. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links for consequential identity assertions. |
| `review_state` | Automatic, candidate, reviewed, steward-reviewed, source-confirmed, deprecated, superseded, rejected, or blocked. |
| `review_record_ref` | Taxonomy/source/steward review record. |
| `validation_report_ref` | Validation report for identity/crosswalk fixtures. |
| `public_label` | Public-safe label approved for UI/map/API display. |
| `public_label_caveat` | Safe caveat for synonym, candidate, aggregate, source-label, or unresolved status. |
| `sensitivity_flags` | Rare/protected, invasive, cultural, source-restricted, public-safe, or unknown posture. |
| `policy_decision_ref` | Policy result when identity affects exposure/release. |
| `created_from_source_time` | Source effective/retrieval time that created identity. |
| `updated_from_source_time` | Source effective/retrieval time that last updated identity. |
| `supersedes_ref` | Prior taxon identity superseded by this object. |
| `superseded_by_ref` | Replacement taxon identity, when applicable. |
| `correction_refs` | CorrectionNotice, merge/split, source withdrawal, stale-state, and rollback lineage. |
| `quality_flags` | Taxon-conflict, rank-conflict, synonym-conflict, source-version-stale, candidate-only, rights-unknown, or review-needed flags. |

---

## Taxon states

| State | Meaning | Default posture |
|---|---|---|
| `accepted` | Reviewed identity has an accepted name for KFM use. | Usable within scope and source/version caveats. |
| `synonym` | Name maps to another accepted/candidate identity. | Preserve source name and synonym basis. |
| `candidate` | Identity imported or proposed but not reviewed. | Work/quarantine or clearly caveated; no authoritative public claims. |
| `unresolved` | Multiple possible identities or insufficient support. | ABSTAIN for consequential claims. |
| `deprecated` | Older identity retained for lineage. | Keep for rollback/correction, avoid new claims. |
| `superseded` | Replaced by newer identity after taxonomic update. | Revalidate downstream dependents. |
| `rejected` | Candidate identity was reviewed and denied. | Retain audit lineage; block use. |
| `blocked` | Policy/source/sensitivity issue blocks use. | DENY or hold until resolved. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | PlantTaxon posture |
|---|---|---|
| Taxonomic backbone, curated plant database, nomenclatural source | `administrative` | Supports identity when source/version/authority limits are recorded. |
| Specimen determination or expert-verified occurrence identity | `observed` | Can strengthen identity use but should not alone become global taxonomy. |
| Rare/protected/noxious/invasive/state-list source | `regulatory` | Supports status/list context; does not define accepted taxonomy by itself. |
| Range or species distribution model label | `modeled` | Model label must not be treated as accepted identity without crosswalk/review. |
| Atlas, checklist, portal rollup, literature summary | `aggregate` | Supports aggregate name usage at stated scope only. |
| Unreviewed import, watcher result, unresolved source row | `candidate` | Hold as candidate until reviewed. |
| AI-generated/reconstructed name | `synthetic` | Requires reality-boundary disclosure; never authoritative identity. |

Source role is part of the identity's trust posture. Promotion cannot erase source authority limits.

---

## Sensitivity and release

A taxon identity can be policy-significant even without coordinates. Names can imply rare/protected status, culturally sensitive plant knowledge, invasive status, restoration use, or source restrictions.

Rules:

- Public labels must avoid exposing restricted source context, steward-only knowledge, or sensitive plant-use context.
- Rare/protected or culturally sensitive labels require policy review before being used in public maps, AI answers, or search facets when exposure risk is material.
- Candidate, synthetic, unresolved, rights-unknown, source-restricted, or review-incomplete identities must not be used as authoritative public labels.
- Conservation, invasive, and regulatory statuses must remain separate linked claims, not silently merged into accepted taxonomy.
- Downstream public records must preserve taxon caveats where identity is synonymic, candidate, aggregate, modeled, stale, or superseded.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native taxon names, IDs, ranks, statuses, and notes are retained without silent rewriting. |
| WORK / QUARANTINE | Candidate identities are normalized, crosswalked, source-role checked, evidence-linked, and reviewed. Ambiguous/conflicted identities remain quarantined. |
| PROCESSED | Reviewed identities receive deterministic identity, accepted/candidate status, source/version support, crosswalk links, evidence, review state, and correction posture. |
| CATALOG / TRIPLET | Taxon-linked claims may be cataloged or projected only with identity evidence, source role, time/version, caveats, and sensitivity posture preserved. |
| RELEASE CANDIDATE | Public labels or taxon facets require validation, policy decision when material, review state, release context, and rollback target. |
| PUBLISHED | Public API/UI/map/search surfaces use released public-safe labels and caveats, not raw source labels or unresolved candidates. |
| CORRECTION | Taxonomy update, synonym change, backbone update, source withdrawal, merge/split, or reviewer correction triggers revalidation and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/plant_taxon.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for accepted taxon, synonym taxon, candidate taxon, unresolved conflict, superseded taxon, rejected candidate, and rare/protected public-label caveat.
- [ ] Add invalid fixtures for missing source descriptor, missing taxon name/ID, authoritative public label from candidate, conservation status collapsed into taxonomy, invasive status collapsed into taxonomy, string-match-only accepted identity, missing crosswalk evidence for consequential mapping, and stale backbone without correction posture.
- [ ] Add validator checks for deterministic identity, rank, taxonomic status, source role, backbone source/version, crosswalk refs, evidence refs, review state, public label caveat, sensitivity flags, correction refs, and supersession linkage.
- [ ] Add policy tests proving taxon identity alone cannot authorize occurrence, rare-plant exposure, invasive status, range, habitat association, or publication.
- [ ] Add no-network fixtures so CI can validate this contract without live taxonomy/source access.
- [ ] Add revalidation tests for backbone update, source-list update, synonym change, taxon split/merge, source withdrawal, and public-label rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Identity resolves, evidence is sufficient, review state allows use | `ANSWER` / identity usable within stated scope |
| Evidence missing, source version stale, mapping ambiguous, review incomplete | `ABSTAIN` |
| Sensitive/source-restricted public exposure, candidate/synthetic identity misused, policy denial | `DENY` |
| Schema/validator/runtime/source-read failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules | Confirms `contracts/` owns object meaning, `schemas/` owns machine shape, and domain-specific files live as segments inside responsibility roots. |
| Flora canonical path register | Confirms `PlantTaxon` is the Flora canonical botanical identity contract and notes USDA PLANTS as recommended taxonomic backbone in PROPOSED status. |
| Flora object-family register | Confirms `PlantTaxon` is an expected Flora object family and that field-level shape remains outside the register. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated labels, maps, search facets, or summaries. |

---

## Rollback

Plant taxon rollback is required when a released or review-authorized identity changes labels, occurrence grouping, rare/protected status handling, invasive status handling, range layers, habitat associations, phenology records, restoration decisions, search facets, AI answers, or published layers.

Rollback triggers include:

- accepted-name correction;
- synonym correction;
- taxon split, lump, merge, or concept revision;
- backbone/source version update;
- source withdrawal or rights change;
- candidate identity used as authoritative;
- string-match-only identity promoted without review;
- conservation/invasive/status list incorrectly collapsed into taxonomy;
- public label exposes sensitive or restricted context;
- downstream records depend on a superseded identity;
- release manifest or public layer uses stale taxon label/caveat.

Rollback artifacts should include affected PlantTaxon IDs, crosswalk IDs, source records, downstream occurrence/specimen/rare/invasive/range/habitat/phenology records, public derivative IDs, release IDs, layer IDs, evidence refs, policy decisions, correction notices, rollback cards, replacement identities, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is USDA PLANTS the default backbone, or only one preferred source among several? | PROPOSED / NEEDS VERIFICATION | Resolve with Flora steward, taxonomy steward, source steward, and schema steward. |
| Which normalized taxonomic-status enum should KFM use? | NEEDS VERIFICATION | Define in schema fixtures and crosswalk tests. |
| How should taxon split/lump/merge events be represented? | NEEDS VERIFICATION | Add supersession/correction fixtures and rollback tests. |
| Should conservation and invasive statuses live only in linked records, or also as cached public-safe summaries on PlantTaxon? | NEEDS VERIFICATION | Resolve with policy and API/UI stewards. |
| How should public labels expose synonym/candidate caveats without confusing users? | NEEDS VERIFICATION | Define public-label projection rules and fixtures. |
| Which identity claims require steward review rather than automated crosswalk validation? | NEEDS VERIFICATION | Policy + validation steward decision. |

---

## Related contracts

- `flora_taxon_crosswalk.md` — source taxon IDs/names/statuses mapped to PlantTaxon identity.
- `domain_observation.md` — source observation envelope that can carry source-native taxon labels.
- `specimen_record.md` — voucher and determination evidence that can support or correct taxon identity.
- `flora_occurrence.md` — occurrence-family records that reference taxon identity.
- `occurrence_public.md` and `occurrence_restricted.md` — public-safe and restricted occurrence surfaces that depend on taxon labels/caveats.
- `rare_plant_record.md` — rare/protected plant handling affected by taxon identity.
- `phenology_observation.md` — time-series seasonal observations tied to plant identity.
- `invasive_plant_record.md` — invasive/noxious/watch-list context linked to taxon identity.
- `range_polygon.md` and `habitat_association.md` — spatial/contextual claims dependent on taxon identity.
- `domain_validation_report.md` — validation reports for taxonomy, crosswalk, fixtures, policy checks, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Resolve whether USDA PLANTS is the governing backbone, preferred backbone, or one source among several.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any occurrence, range, habitat, rare-plant, invasive, phenology, or public label depends on this contract.
- [ ] Add source profiles for approved taxonomic backbone/list sources before activation.
- [ ] Add policy tests proving PlantTaxon does not authorize occurrence proof, sensitive exposure, or publication by itself.
- [ ] Confirm public API/UI/map/search surfaces preserve candidate/synonym/stale/source-role caveats.
- [ ] Record any contract/schema/path/backbone conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
